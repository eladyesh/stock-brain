"""Verify bounded automatic progression and paused-source behavior, without HTTP."""
from datetime import datetime, timezone
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import coverage_cycle
from coverage_store import CoverageStore


class CycleTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.now = datetime(2026, 10, 22, 10, tzinfo=timezone.utc)
        self.store = CoverageStore(Path(self.temporary.name) / 'coverage.sqlite3', clock=lambda: self.now)
        self.store.seed_companies([{'cik': n, 'ticker': 'T' + str(n), 'company_name': 'Issuer ' + str(n),
                                    'exchange': 'NASDAQ'} for n in range(1, 5)])
        self.provider = Mock()
        self.provider.readiness.return_value = {'ready': True, 'reason': None}

    def test_paused_source_never_queues_claims_or_refreshes_listings(self):
        self.provider.readiness.return_value = {'ready': False, 'reason': 'operator paused'}
        loader = Mock(side_effect=AssertionError('network must not be used'))
        report = coverage_cycle.run_cycle(self.store, self.provider, refresh_listings=True, listing_loader=loader)
        self.assertEqual(report['stopped_reason'], 'operator paused')
        self.assertEqual(sum(self.store.stats()['jobs'].values()), 0)
        loader.assert_not_called()

    def test_bounded_cycles_progress_across_issuers_after_restart(self):
        def collect(worker, job):
            return {'collector_state': {'value': {'last_checked_at': self.now.isoformat()}}}, {'action': 'no_supported_filing'}
        with patch.object(coverage_cycle.CoverageWorker, 'collect', collect):
            first = coverage_cycle.run_cycle(self.store, self.provider, limit=2, now=self.now)
            reopened = CoverageStore(self.store.path, clock=lambda: self.now)
            second = coverage_cycle.run_cycle(reopened, self.provider, limit=2, now=self.now)
        self.assertEqual(first['worker']['succeeded'], 2)
        self.assertEqual(second['worker']['succeeded'], 2)
        observed = [job['cik'] for report in (first, second) for job in report['worker']['jobs']]
        self.assertEqual(len(set(observed)), 4)
        self.assertEqual(reopened.stats()['jobs']['completed'], 4)

    def test_opted_in_listing_import_is_partial_and_not_repeated_same_day(self):
        payload = {'fields': ['cik', 'name', 'ticker', 'exchange'], 'data': [[5, 'Fifth', 'FIVE', 'NYSE']]}
        source = {'url': coverage_cycle.coverage_cli.SEC_LISTINGS_URL, 'retrieved_at': self.now.isoformat(), 'sha256': 'a' * 64}
        loader = Mock(return_value=(payload, source, {}))
        with patch.object(coverage_cycle.CoverageWorker, 'run', return_value={'stopped_reason': None, 'failed': 0}):
            coverage_cycle.run_cycle(self.store, self.provider, refresh_listings=True, now=self.now, listing_loader=loader)
            coverage_cycle.run_cycle(self.store, self.provider, refresh_listings=True, now=self.now, listing_loader=loader)
        loader.assert_called_once()
        self.assertEqual(self.store.stats()['active_listings'], 5)

    def test_failed_listing_import_preserves_registry_and_creates_no_jobs(self):
        loader = Mock(side_effect=ValueError('invalid source'))
        report = coverage_cycle.run_cycle(self.store, self.provider, refresh_listings=True, now=self.now, listing_loader=loader)
        self.assertIn('existing registry retained', report['stopped_reason'])
        self.assertEqual(self.store.stats()['issuers'], 4)
        self.assertEqual(sum(self.store.stats()['jobs'].values()), 0)


if __name__ == '__main__':
    unittest.main()
