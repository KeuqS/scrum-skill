import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("package_checks", ROOT / "scripts/validate_package.py")
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class PackageTests(unittest.TestCase):
    def test_actual_package_is_consistent(self):
        self.assertEqual(len(checks.validate()), 3)

    def fixture(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name) / "package"
        shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(
            ".git", "__pycache__", ".eval-output", "node_modules"))
        return root

    def test_host_version_drift_is_detected(self):
        root = self.fixture()
        path = root / ".codex-plugin/plugin.json"
        manifest = json.loads(path.read_text())
        manifest["version"] = "9.9.9"
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "version drift"):
            checks.validate(root)

    def test_missing_skill_resource_is_detected(self):
        root = self.fixture()
        (root / "skills/scrum-skill/references/roles.md").unlink()
        with self.assertRaisesRegex(ValueError, "broken local reference"):
            checks.validate(root)

    def test_unsafe_manifest_path_is_rejected(self):
        with self.assertRaises(ValueError):
            checks.inside(ROOT, "./../outside")

    def test_dashboard_identity_drift_is_detected(self):
        root = self.fixture()
        path = root / "skills/scrum-dashboard/SKILL.md"
        path.write_text(path.read_text().replace("name: scrum-dashboard", "name: wrong-name"))
        with self.assertRaisesRegex(ValueError, "dashboard skill identity"):
            checks.validate(root)

    def test_source_pdf_in_package_is_rejected(self):
        root = self.fixture()
        (root / "reference.pdf").write_bytes(b"synthetic fixture")
        with self.assertRaisesRegex(ValueError, "local/source document"):
            checks.validate(root)

    def test_listing_subtitle_limit_is_enforced(self):
        root = self.fixture()
        path = root / ".codex-plugin/plugin.json"
        manifest = json.loads(path.read_text())
        manifest["interface"]["shortDescription"] = "x" * 31
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "invalid listing field: shortDescription"):
            checks.validate(root)

    def test_missing_listing_icon_is_rejected(self):
        root = self.fixture()
        (root / "assets/icon.svg").unlink()
        with self.assertRaisesRegex(ValueError, "missing/escaping package path"):
            checks.validate(root)


if __name__ == "__main__":
    unittest.main()
