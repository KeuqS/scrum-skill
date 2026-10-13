import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/scrum-dashboard'
SCRIPT = SKILL / 'scripts/generate_dashboard.py'
spec = importlib.util.spec_from_file_location('dashboard', SCRIPT)
dashboard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dashboard)


class DashboardTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((SKILL / 'assets/demo.json').read_text())

    def test_estimate_changes_do_not_rewrite_history(self):
        before = dashboard.metrics(self.data)
        self.data['backlog'][0]['points'] = 100
        after = dashboard.metrics(self.data)
        self.assertEqual(before['history'], after['history'])
        self.assertNotEqual(before['known_points'], after['known_points'])

    def test_scope_addition_can_keep_remaining_flat(self):
        values = dashboard.metrics(self.data)['history']
        self.assertEqual([26, 26, 21], [r['remaining'] for r in values])
        self.assertEqual([8, 13, None], [r['velocity'] for r in values])

    def test_no_partial_credit(self):
        self.data['sprints'][0]['velocity_items'].append({'id':'unfinished','points':21,'dod_met':False})
        self.assertEqual(8, dashboard.metrics(self.data)['history'][0]['velocity'])

    def test_missing_and_zero_are_different(self):
        self.data['sprints'][0].pop('velocity_items')
        self.data['sprints'][1]['velocity_items'] = []
        self.data['sprints'][2].pop('snapshot')
        rows = dashboard.metrics(self.data)['history']
        self.assertIsNone(rows[0]['velocity'])
        self.assertEqual(0, rows[1]['velocity'])
        self.assertIsNone(rows[2]['remaining'])

    def test_duplicate_completion_rejected(self):
        self.data['sprints'][1]['velocity_items'][0]['id'] = 'A'
        with self.assertRaises(ValueError):
            dashboard.validate(self.data)

    def test_invalid_metrics_rejected(self):
        for points in (True, -1, float('nan'), float('inf'), '8'):
            value = copy.deepcopy(self.data)
            value['backlog'][0]['points'] = points
            with self.subTest(points=points), self.assertRaises(ValueError):
                dashboard.validate(value)

    def test_dod_and_dates_validated(self):
        self.data['backlog'][0]['dod_met'] = False
        with self.assertRaises(ValueError):
            dashboard.validate(self.data)
        self.data['backlog'][0]['dod_met'] = True
        self.data['sprints'][0]['timeline'][0]['end_date'] = '2026-08-01'
        with self.assertRaises(ValueError):
            dashboard.validate(self.data)

    def test_active_velocity_rejected(self):
        self.data['sprints'][2]['velocity_items'] = []
        with self.assertRaises(ValueError):
            dashboard.validate(self.data)

    def test_scope_ledger_must_reconcile(self):
        self.data['sprints'][1]['scope_changes']['added_points'] = 9
        with self.assertRaises(ValueError):
            dashboard.validate(self.data)

    def test_completion_history_must_not_decrease(self):
        self.data['sprints'][2]['snapshot']['completed_points'] = 20
        with self.assertRaises(ValueError):
            dashboard.validate(self.data)

    def test_malformed_container_cli_is_graceful(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'input.json'
            self.data['sprints'][0]['timeline'] = [False]
            source.write_text(json.dumps(self.data))
            result = subprocess.run([sys.executable, str(SCRIPT), '--input', str(source), '--output', str(Path(directory) / 'out.html')], capture_output=True)
            self.assertEqual(2, result.returncode)
            self.assertNotIn(b'Traceback', result.stderr)

    def test_embedded_data_cannot_break_out_of_script(self):
        self.data['project']['name'] = '</script><script>alert(1)</script>&'
        html = dashboard.render(self.data)
        self.assertNotIn('</script><script>alert(1)', html)
        start = html.index('type="application/json">') + len('type="application/json">')
        embedded = json.loads(html[start:html.index('</script>', start)])
        self.assertEqual(self.data['project']['name'], embedded['data']['project']['name'])

    def test_cli_creates_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / 'report.html'
            command = [sys.executable, str(SCRIPT), '--demo', '--output', str(out)]
            first = subprocess.run(command, capture_output=True)
            self.assertEqual(0, first.returncode, first.stderr)
            original = out.read_bytes()
            second = subprocess.run(command, capture_output=True)
            self.assertEqual(2, second.returncode)
            self.assertEqual(original, out.read_bytes())


if __name__ == '__main__':
    unittest.main()
