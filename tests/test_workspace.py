"""Behavioral regressions for preservation, planning honesty and path safety."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "skills/scrum-skill/scripts/init_workspace.py"
spec = importlib.util.spec_from_file_location("scrum_workspace", SCRIPT)
workspace = importlib.util.module_from_spec(spec)
spec.loader.exec_module(workspace)


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def plan(self, **changes):
        params = dict(root=self.root, name="inventory", goal="Staff can inspect stock",
                      roles=["engineering", "qa"], start=date(2026, 10, 19), sprint_days=14)
        params.update(changes)
        return workspace.plan(**params)

    def test_initial_records_are_proposed_and_no_events_claimed(self):
        workspace.apply(self.plan())
        state = json.loads((self.root / ".scrum/workspace.json").read_text())
        self.assertEqual(state["state"], "proposed")
        self.assertEqual(state["forecast_end"], "2026-11-01")
        self.assertEqual(state["specialists"], ["engineering", "qa"])
        self.assertEqual(state["skill_version"], "0.5.1")
        self.assertIsNone(state["product_owner"])
        self.assertIsNone(state["scrum_master"])
        self.assertEqual(state["accountabilities"], "unresolved")
        self.assertIn("Product Owner: unresolved", (self.root / ".scrum/TEAM.md").read_text())
        self.assertTrue((self.root / ".scrum/sprints/SPRINT-01-RETROSPECTIVE.md").is_file())
        self.assertTrue((self.root / ".scrum/handoffs/LATEST.md").is_file())

    def test_dashboard_input_starts_empty_and_preserves_recorded_history(self):
        workspace.apply(self.plan())
        path = self.root / ".scrum/metrics.json"
        data = json.loads(path.read_text())
        self.assertEqual(data["backlog"], [])
        self.assertEqual(data["sprints"], [])
        spec = importlib.util.spec_from_file_location("dashboard_bridge", REPO /
            "skills/scrum-dashboard/scripts/generate_dashboard.py")
        dashboard = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(dashboard)
        self.assertEqual(dashboard.metrics(data)["history"], [])
        data["backlog"] = [{"id": "US-1", "title": "Inspect stock", "points": None,
                            "status": "backlog", "dod_met": False}]
        path.write_text(json.dumps(data), encoding="utf-8")
        before = path.read_bytes()
        workspace.apply(self.plan())
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(dashboard.metrics(data)["unestimated"], 1)

    def test_existing_instructions_preserved_byte_for_byte(self):
        original = b"# Existing policy\r\nDo not publish plans.\r\n"
        (self.root / "AGENTS.md").write_bytes(original)
        workspace.apply(self.plan())
        result = (self.root / "AGENTS.md").read_bytes()
        self.assertTrue(result.startswith(original))
        self.assertEqual(result.count(workspace.START.encode()), 1)

    def test_repeat_has_no_writes_and_keeps_working_decisions(self):
        workspace.apply(self.plan())
        record = self.root / ".scrum/DECISIONS.md"
        record.write_text("An actual user decision.\n", encoding="utf-8")
        self.assertEqual(self.plan(), {})
        self.assertEqual(record.read_text(), "An actual user decision.\n")

    def test_conflicting_project_identity_rejected(self):
        workspace.apply(self.plan())
        with self.assertRaisesRegex(ValueError, "different project"):
            self.plan(name="another-project")

    def test_repair_uses_current_project_decisions_not_bootstrap_defaults(self):
        workspace.apply(self.plan())
        manifest = self.root / ".scrum/workspace.json"
        state = json.loads(manifest.read_text())
        state.update(product_goal="Coordinate neighborhood planting", specialists=["horticulture"],
                     sprint_days=7, forecast_end="2026-10-25")
        manifest.write_text(json.dumps(state), encoding="utf-8")
        (self.root / ".scrum/TEAM.md").unlink()
        (self.root / ".scrum/sprints/SPRINT-01.md").unlink()
        workspace.apply(self.plan())
        self.assertEqual(json.loads(manifest.read_text()), state)
        self.assertIn("horticulture", (self.root / ".scrum/TEAM.md").read_text())
        self.assertIn("2026-10-25", (self.root / ".scrum/sprints/SPRINT-01.md").read_text())
        self.assertTrue((self.root / ".scrum/roles/horticulture.md").is_file())

    def test_generalist_and_custom_domain_do_not_require_counsel(self):
        workspace.apply(self.plan(roles=[]))
        state = json.loads((self.root / ".scrum/workspace.json").read_text())
        self.assertEqual(state["specialists"], [])
        self.assertFalse((self.root / ".scrum/roles").exists())
        self.assertEqual(workspace.specialists("research,qa"), ["research", "qa"])

    def test_invalid_roles_and_duplicates_fail(self):
        for raw in ("qa,qa", "../../outside", "research,", "Domain Expert"):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                workspace.specialists(raw)

    def test_supplied_accountabilities_survive_cli_defaults_and_repair(self):
        subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root),
                        "--name", "inventory", "--goal", "Track stock",
                        "--product-owner", "Product owner A", "--scrum-master", "Scrum master B"],
                       capture_output=True, text=True, check=True)
        manifest = self.root / ".scrum/workspace.json"
        before = manifest.read_bytes()
        state = json.loads(before)
        self.assertEqual(state["product_owner"], "Product owner A")
        self.assertEqual(state["scrum_master"], "Scrum master B")
        self.assertEqual(state["accountabilities"], "identified")
        self.assertIn("preparation", state["framework_status"])
        (self.root / ".scrum/TEAM.md").unlink()
        workspace.apply(self.plan(product_owner="Different label", scrum_master="Other label"))
        self.assertEqual(manifest.read_bytes(), before)
        team = (self.root / ".scrum/TEAM.md").read_text()
        self.assertIn("Product Owner: Product owner A", team)
        self.assertIn("Scrum Master: Scrum master B", team)
        self.assertNotIn("Different label", team)

    def test_partial_identity_remains_unresolved_and_blank_is_rejected(self):
        workspace.apply(self.plan(product_owner="Product owner A"))
        state = json.loads((self.root / ".scrum/workspace.json").read_text())
        self.assertEqual(state["accountabilities"], "unresolved")
        self.assertIsNone(state["scrum_master"])
        with self.assertRaisesRegex(ValueError, "non-empty"):
            self.plan(product_owner=" ")

    def test_legacy_assumed_user_is_not_promoted_to_identity_during_repair(self):
        workspace.apply(self.plan())
        manifest = self.root / ".scrum/workspace.json"
        state = json.loads(manifest.read_text())
        state["product_owner"] = "human user (confirm identity if needed)"
        state.pop("scrum_master")
        manifest.write_text(json.dumps(state), encoding="utf-8")
        before = manifest.read_bytes()
        (self.root / ".scrum/TEAM.md").unlink()
        workspace.apply(self.plan())
        self.assertEqual(manifest.read_bytes(), before)
        team = (self.root / ".scrum/TEAM.md").read_text()
        self.assertIn("Product Owner: unresolved", team)
        self.assertIn("Scrum Master: unresolved", team)

    def test_selected_presets_include_behavior_and_preserve_customization(self):
        roles = ["engineering", "qa", "design", "security", "ai", "operations",
                 "domain-reviewer", "legal-counsel", "privacy-counsel"]
        workspace.apply(self.plan(roles=roles))
        for role in roles:
            with self.subTest(role=role):
                copied = self.root / f".scrum/roles/{role}.md"
                preset = REPO / f"skills/scrum-skill/assets/profiles/{role}.md"
                self.assertEqual(copied.read_bytes(), preset.read_bytes())
        customized = self.root / ".scrum/roles/qa.md"
        customized.write_text("Actual project QA decisions.\n", encoding="utf-8")
        self.assertEqual(self.plan(roles=roles), {})
        self.assertEqual(customized.read_text(), "Actual project QA decisions.\n")

    def test_custom_specialism_retains_template_fallback(self):
        workspace.apply(self.plan(roles=["horticulture"]))
        profile = (self.root / ".scrum/roles/horticulture.md").read_text()
        self.assertIn("horticulture", profile)
        self.assertIn("Owned files/work scope:", profile)

    def test_crlf_packaged_preset_is_copied_without_newline_translation(self):
        with tempfile.TemporaryDirectory() as packaged:
            skill = Path(packaged)
            (skill / "assets/profiles").mkdir(parents=True)
            (skill / "references").mkdir()
            body = b"# QA guide\r\n\r\nEvidence and boundaries.\r\n"
            (skill / "assets/profiles/qa.md").write_bytes(body)
            (skill / "assets/role-profile.md").write_text("# [specialism]\n")
            (skill / "references/accountabilities.md").write_text("# Accountabilities\n")
            with patch.object(workspace, "SKILL", skill):
                workspace.apply(self.plan(roles=["qa"]))
            copied = self.root / ".scrum/roles/qa.md"
            self.assertEqual(copied.read_bytes(), body)
            self.assertEqual(self.plan(roles=["qa"]), {})

    def test_accountability_guidance_is_available_without_specialists(self):
        workspace.apply(self.plan(roles=[]))
        guide = self.root / ".scrum/ACCOUNTABILITIES.md"
        self.assertIn("## Scrum Master", guide.read_text(encoding="utf-8"))
        self.assertIn("ACCOUNTABILITIES.md", (self.root / ".scrum/TEAM.md").read_text())
        self.assertFalse((self.root / ".scrum/roles").exists())

    def test_file_collision_is_detected_before_any_writes(self):
        (self.root / "CLAUDE.md").mkdir()
        with self.assertRaises(ValueError):
            self.plan()
        self.assertFalse((self.root / ".scrum").exists())

    def test_parent_collision_is_detected_before_writes(self):
        (self.root / ".scrum").mkdir()
        (self.root / ".scrum/sprints").write_text("not a directory")
        with self.assertRaises(ValueError):
            self.plan()
        self.assertFalse((self.root / ".scrum/workspace.json").exists())

    def test_malformed_markers_fail_without_overwriting(self):
        policy = self.root / "AGENTS.md"
        policy.write_text("Existing\n" + workspace.START)
        with self.assertRaisesRegex(ValueError, "malformed"):
            self.plan()
        self.assertFalse((self.root / ".scrum").exists())
        self.assertEqual(policy.read_text(), "Existing\n" + workspace.START)

    def test_symlink_escape_fails_before_writes(self):
        with tempfile.TemporaryDirectory() as outside:
            try:
                (self.root / ".scrum").symlink_to(outside, target_is_directory=True)
            except OSError as error:
                self.skipTest(f"symlink creation unsupported: {error}")
            with self.assertRaisesRegex(ValueError, "escape|symlink"):
                self.plan()
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_cadence_cannot_exceed_one_calendar_month(self):
        with self.assertRaisesRegex(ValueError, "calendar month"):
            self.plan(start=date(2027, 2, 1), sprint_days=31)
        with self.assertRaises(ValueError):
            self.plan(sprint_days=0)

    def test_dry_run_cli_never_writes(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root),
                                 "--name", "inventory", "--goal", "Track stock", "--dry-run"],
                                capture_output=True, text=True, check=True)
        self.assertIn("Would write", result.stdout)
        self.assertEqual(list(self.root.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
