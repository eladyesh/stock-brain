import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import refresh_desk as refresh
import research_pipeline as p


class RefreshTests(unittest.TestCase):
    def test_financial_refresh_preserves_verified_split_without_reapproving_new_facts(self):
        from test_financial_history import COMPANY, REVENUE, facts, year, split_review
        old = year(3.85)
        raw = facts({REVENUE: [year()], 'EarningsPerShareDiluted': {'USD/shares': [old]}})
        review = split_review('eps_diluted', [old])
        history = refresh.financials.normalize_companyfacts(raw, COMPANY, '2026-02-02', normalization_reviews=[review])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            p.write_json(root / 'research/financials/TEST.json', history)
            with patch.object(p, 'universe', return_value=[COMPANY]), patch.object(p.Fetcher, 'fetch', return_value=(json.dumps(raw), {})):
                result = refresh.collect_financials(root, '2026-02-03')
                self.assertEqual(result[0]['status'], 'collected', result)
                saved = refresh.financials.load_history(root, 'TEST')
                self.assertAlmostEqual(refresh.financials.get_metric(saved, 'eps_diluted')['value'], .385)
                self.assertTrue(refresh.financials.get_metric(saved, 'eps_diluted')['model_usable'])
                # A newly filed observation has not been source-reviewed.
                raw['facts']['us-gaap']['EarningsPerShareDiluted']['units']['USD/shares'].append(
                    year(.4, filed='2026-02-03', accn='0000000001-26-000009'))
            with patch.object(p, 'universe', return_value=[COMPANY]), patch.object(p.Fetcher, 'fetch', return_value=(json.dumps(raw), {})):
                refresh.collect_financials(root, '2026-02-04')
                saved = refresh.financials.load_history(root, 'TEST')
                self.assertFalse(refresh.financials.get_metric(saved, 'eps_diluted')['model_usable'])

    def test_queue_restore_keeps_events_from_both_histories(self):
        current = {'queue': [{'id': 'a', 'title': 'current'}, {'id': 'b', 'title': 'new'}]}
        saved = {'queue': [{'id': 'a', 'title': 'saved'}, {'id': 'c', 'title': 'old'}], 'checked_at': 'earlier'}
        merged = refresh.merge_reports(current, saved)
        self.assertEqual({e['id'] for e in merged['queue']}, {'a', 'b', 'c'})
        self.assertEqual(current['queue'][0]['title'], 'current')

    def test_review_restore_keeps_both_audit_histories(self):
        merged = refresh.merge_reviews({'reviews': [{'record_id': 'one'}]}, {'reviews': [{'record_id': 'two'}]})
        self.assertEqual({r['record_id'] for r in merged['reviews']}, {'one', 'two'})

    def test_missing_state_ref_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                refresh.read_state_ref(Path(directory), 'origin/automation/research-data', 'latest.json')
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_mismatched_snapshot_universe_is_rejected_before_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payloads = [{'schema_version': 1, 'companies': [{'ticker': 'OTHER'}]}, {'queue': []}, {'reviews': []}, {}]
            with patch.object(refresh, 'read_state_ref', side_effect=payloads), patch.object(p, 'universe', return_value=[{'ticker': 'MSFT', 'cik': '0000789019'}]):
                with self.assertRaises(ValueError):
                    refresh.restore_state(root, 'saved')
            self.assertEqual(list(root.iterdir()), [])

    def test_failed_discovery_preserves_queue_and_date_but_exports_error(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            seed = {'checked_at': '2026-01-01T00:00:00+00:00', 'queue': [{'id': 'a', 'status': 'pending_review'}]}
            p.write_json(root / 'research/monitoring/latest.json', seed)
            p.write_json(root / 'research/monitoring/triage.json', {'reviews': []})
            def build(target_root, target):
                snapshot = {'built_at': '2026-10-18T00:00:00+00:00'}
                p.write_json(target, snapshot)
                return snapshot
            with patch.object(refresh.kb, 'export_records'), patch.object(refresh.monitor, 'run', side_effect=OSError('offline')), \
                 patch.object(refresh.triage, 'triage', return_value={'summary': {'pending': 1}, 'reviews': []}), \
                 patch.object(refresh, 'collect_financials', return_value=[{'ticker': 'MSFT', 'status': 'error'}]), \
                 patch.object(refresh.market_data, 'collect', return_value={'results': [{'ticker': 'MSFT', 'status': 'error'}]}), \
                 patch.object(refresh.build_desk, 'build', side_effect=build):
                result = refresh.refresh(root, root / 'publish')
            self.assertEqual(result['status'], 'partial')
            self.assertFalse(result['research_changed'])
            self.assertEqual(p.read_json(root / 'publish/latest.json'), seed)
            self.assertIn('offline', result['discovery']['error'])
            manifest = p.read_json(root / 'publish/publish-manifest.json')
            self.assertEqual({f['path'] for f in manifest['files']}, {'desk.json', 'latest.json', 'triage.json', 'run-status.json'})
            self.assertEqual(manifest['refresh_status'], 'partial')


if __name__ == '__main__':
    unittest.main()

