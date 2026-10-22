from datetime import timedelta
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from urllib.error import HTTPError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from coverage_store import CoverageStore
import market_directory as directory
import vendor_data as vendor
from test_market_directory import fixtures, NOW


class Response(io.BytesIO):
    def __init__(self, value, url):
        super().__init__(json.dumps(value).encode()); self.url = url
    def geturl(self): return self.url


class VendorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.store = CoverageStore(Path(self.temp.name) / 'data.db', clock=lambda: NOW)
        self.store.seed_companies([{'cik': 123, 'ticker': 'T0', 'company_name': 'Company 0', 'exchange': 'NASDAQ'}])
        directory.import_directories(self.store, fixtures())
        self.security = directory.list_securities(self.store, query='T0')['items'][0]
        self.env = {'STOCK_BRAIN_FD_ENABLED': '1', 'STOCK_BRAIN_FD_PUBLIC_DATA_LICENSE': '1',
                    'STOCK_BRAIN_FD_MAX_DAILY_REQUESTS': '3', 'FINANCIAL_DATASETS_API_KEY': 'synthetic-test-key'}
        self.source = {'url': vendor.API + '/company/facts?ticker=T0', 'sha256': 'a' * 64, 'retrieved_at': NOW.isoformat()}

    def test_missing_enable_key_license_or_budget_uses_no_network(self):
        for key in self.env:
            env = {k: v for k, v in self.env.items() if k != key}
            provider = vendor.FinancialDatasets(self.store, environ=env, opener=lambda *a, **k: self.fail('network called'))
            self.assertFalse(provider.readiness()['ready'])
            self.assertEqual(vendor.collect(self.store, provider)['attempted'], 0)

    def test_atomic_budget_caps_failures_and_stops_cross_run_overrun(self):
        calls = []
        def opener(request, **kwargs):
            calls.append(request)
            return Response({'snapshot': {'ticker': 'T0', 'price': 10, 'time': NOW.isoformat()}}, request.full_url)
        provider = vendor.FinancialDatasets(self.store, environ=self.env, opener=opener, sleep=lambda _: None)
        for _ in range(3): provider.request(self.security, 'prices')
        with self.assertRaisesRegex(vendor.ProviderStop, 'daily_budget_exhausted'): provider.request(self.security, 'prices')
        self.assertEqual(len(calls), 3)
        self.assertNotIn('synthetic-test-key', calls[0].full_url)
        with self.store._connection() as db:
            self.assertEqual(db.execute('SELECT request_count FROM provider_daily_usage').fetchone()[0], 3)

    def test_auth_or_payment_failure_pauses_source_and_preserves_existing_data(self):
        def opener(request, **kwargs): raise HTTPError(request.full_url, 402, 'private billing detail', {}, None)
        provider = vendor.FinancialDatasets(self.store, environ=self.env, opener=opener)
        with self.assertRaisesRegex(vendor.ProviderStop, 'http_402'): provider.request(self.security, 'profile')
        self.assertFalse(provider.readiness()['ready'])
        self.assertNotIn('private', json.dumps(self.store.source_status(vendor.PROVIDER)))

    def test_profile_mismatch_and_future_price_are_not_stored(self):
        bad = {'company_facts': {'ticker': 'OTHER', 'name': 'Company 0', 'cik': '123', 'exchange': 'NASDAQ', 'is_active': True}}
        with self.assertRaises(ValueError): vendor.save_observation(self.store, self.security, 'profile', bad, self.source)
        future = {'snapshot': {'ticker': 'T0', 'price': 10, 'time': (NOW + timedelta(days=1)).isoformat()}}
        with self.assertRaises(ValueError): vendor.save_observation(self.store, self.security, 'prices', future, self.source)
        with self.store._connection() as db:
            self.assertEqual(db.execute('SELECT count(*) FROM market_observations').fetchone()[0], 0)

    def test_fair_plan_includes_existing_issuer_while_unlinked_profiles_wait(self):
        tasks = vendor.due_tasks(self.store, limit=3)
        self.assertEqual({t[0] for t in tasks}, {'profile', 'financials', 'prices'})
        self.assertTrue(all(row['cik'] for dataset, row in tasks if dataset != 'profile'))

    def test_existing_daily_ledger_reservation_prevents_all_calls(self):
        provider = vendor.FinancialDatasets(self.store, environ=self.env, opener=lambda *a, **k: self.fail('network called'))
        result = vendor.collect(self.store, provider, reserve=lambda _: False)
        self.assertEqual(result['stopped_reason'], 'daily_allowance_already_reserved')

    def test_remote_budget_reservation_is_create_only_and_secret_is_not_in_payload(self):
        requests = []
        def opener(request, **kwargs):
            requests.append(request)
            if request.method == 'GET': return Response({'object': {'sha': 'a' * 40}}, request.full_url)
            if sum(r.method == 'PUT' for r in requests) > 1:
                raise HTTPError(request.full_url, 422, 'sha required for existing file', {}, None)
            return Response({'content': {'sha': 'b' * 40}}, request.full_url)
        env = {**self.env, 'GITHUB_ACTIONS': 'true', 'GH_TOKEN': 'synthetic-github-secret',
               'GITHUB_SHA': 'c' * 40, 'GITHUB_RUN_ID': '123', 'GITHUB_RUN_ATTEMPT': '1'}
        self.assertTrue(vendor.reserve_daily_run(env, opener=opener))
        self.assertFalse(vendor.reserve_daily_run(env, opener=opener))
        for request in requests:
            self.assertTrue(request.full_url.startswith('https://api.github.com/repos/eladyesh/stock-brain/'))
            self.assertNotIn('synthetic-github-secret', (request.data or b'').decode())
            if request.method == 'PUT': self.assertNotIn('sha', json.loads(request.data))

    def test_partial_financials_missing_currency_or_provenance_are_rejected(self):
        base = {'ticker': 'T0', 'report_period': '2026-06-30', 'period': 'quarterly', 'currency': 'USD',
                'accession_number': '0000000123-26-000001', 'filing_url': 'https://www.sec.gov/Archives/fixture.htm'}
        value = {'financials': {k: [dict(base)] for k in ('income_statements', 'balance_sheets', 'cash_flow_statements')}}
        valid = vendor.save_observation(self.store, self.security, 'financials', value, self.source)
        self.assertEqual(valid['accounting_status'], 'vendor_normalized_unreviewed')
        value['financials']['balance_sheets'][0]['currency'] = ''
        with self.assertRaises(ValueError): vendor.save_observation(self.store, self.security, 'financials', value, self.source)


if __name__ == '__main__': unittest.main()
