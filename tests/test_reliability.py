"""Regression tests for corruption, blocked sources and bounded public answers."""
import copy
from datetime import datetime, timezone, timedelta
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
import urllib.error
from unittest.mock import patch, Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import financial_history as f
import research_pipeline as p
import refresh_desk
import runtime_data as data
import serve_public
from test_financial_history import facts, year, COMPANY, REVENUE


class IntegrityTests(unittest.TestCase):
    def setUp(self):
        self.raw = facts({REVENUE: [year()], 'NetCashProvidedByUsedInOperatingActivities': [year(400)],
                          'PaymentsToAcquirePropertyPlantAndEquipment': [year(100)]})
        self.history = f.normalize_companyfacts(self.raw, COMPANY, '2026-01-01')
        self.cells = self.history['financials'][self.history['periods'][0]['id']]

    def test_tampered_numbers_calculations_and_eligibility_are_rejected(self):
        changes = [lambda h, c: c['revenue'].update(value=999),
                   lambda h, c: c['revenue'].update(value=True),
                   lambda h, c: c['free_cash_flow'].update(value=301),
                   lambda h, c: c['eps_diluted'].update(model_usable=True),
                   lambda h, c: c.pop('capex'),
                   lambda h, c: h.update(company_id='company-cik-0000000002'),
                   lambda h, c: c['revenue']['provenance'][0].update(url='https://example.com/')]
        for change in changes:
            with self.subTest(change=change):
                history = copy.deepcopy(self.history)
                change(history, next(iter(history['financials'].values())))
                with self.assertRaises(ValueError): f.validate_history(history)

    def test_empty_or_truncated_success_retains_previous_financial_file(self):
        for raw in [facts({}), facts({REVENUE: [year()]})]:
            with self.subTest(raw=raw), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                path = root / 'research/financials/TEST.json'
                p.write_json(path, self.history)
                before = path.read_bytes()
                with patch.object(p, 'universe', return_value=[COMPANY]), patch.object(p.Fetcher, 'fetch', return_value=(json.dumps(raw), {})):
                    result = refresh_desk.collect_financials(root, '2026-01-02')
                self.assertEqual(result[0]['status'], 'error')
                self.assertEqual(path.read_bytes(), before)

    def test_sec_403_stops_remaining_sec_requests_without_stopping_other_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            fetcher = p.Fetcher(Path(directory), 'StockBrain test')
            error = urllib.error.HTTPError('https://data.sec.gov/example', 403, 'Forbidden', {},
                                          io.BytesIO(b'<title>SEC.gov | Your Request Originates from an Undeclared Automated Tool</title>'))
            with patch.object(p.urllib.request, 'urlopen', side_effect=error) as request, patch.object(p.time, 'sleep'):
                for url in ['https://data.sec.gov/example', 'https://www.sec.gov/another']:
                    with self.assertRaisesRegex(ValueError, 'undeclared automated tool'): fetcher.fetch(url)
                self.assertEqual(request.call_count, 1)
                with self.assertRaises(urllib.error.HTTPError): fetcher.fetch('https://issuer.example/news')
                self.assertEqual(request.call_count, 2)

    def test_operator_sec_pause_does_not_attempt_network(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(p.os.environ, {'STOCK_BRAIN_SEC_ENABLED': '0'}):
            with patch.object(p.urllib.request, 'urlopen') as request:
                with self.assertRaisesRegex(ValueError, 'paused by operator'):
                    p.Fetcher(Path(directory), 'StockBrain test').fetch('https://data.sec.gov/example')
                request.assert_not_called()


class AnswerApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory()
        cls.store = data.StateStore(cls.temporary.name)
        data.initialize(data.kb.ROOT, cls.store)
        cls.app = serve_public.Application(data.kb.ROOT, cls.store, scheduler_enabled=False)

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def request(self, payload, **extra):
        raw = data.encode(payload)
        received = {}
        def start(status, headers): received.update(status=status, headers=dict(headers))
        body = b''.join(self.app({'PATH_INFO': '/api/ask', 'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': 'application/json',
                                 'CONTENT_LENGTH': str(len(raw)), 'wsgi.input': io.BytesIO(raw), **extra}, start))
        return received, json.loads(body)

    def test_real_worker_returns_cited_answer_and_abstention_without_full_history(self):
        for question, abstain in [('How does Microsoft make money?', False), ('Should I buy MSFT?', True),
                                  ('MSFT revenue in latest available fiscal year', False)]:
            head, result = self.request({'question': question})
            self.assertEqual(head['status'], '200 OK', result)
            self.assertEqual(result['abstain'], abstain, result)
            self.assertEqual(head['headers']['Cache-Control'], 'no-store')
            self.assertEqual(len(result['generation']), 64)
            self.assertNotIn('history', result['companies'][0] if result['companies'] else {})
            if not abstain: self.assertTrue(all(s['sources'] for s in result['statements']))

    def test_invalid_requests_and_busy_worker_are_bounded(self):
        for value in [[], {'question': ''}, {'question': 1}, {'question': 'x' * 4001}, {'question': 'MSFT', 'path': '/etc/passwd'}]:
            self.assertEqual(self.request(value)[0]['status'], '400 Bad Request')
        self.assertEqual(self.request({'question': 'MSFT'}, CONTENT_TYPE='text/plain')[0]['status'], '415 Unsupported Media Type')
        self.assertEqual(self.request({'question': 'MSFT'}, CONTENT_LENGTH='9000')[0]['status'], '413 Content Too Large')
        self.assertEqual(self.request({'question': 'MSFT'}, REQUEST_METHOD='GET')[0]['headers']['Allow'], 'POST')
        self.app.answer_slot.acquire()
        try:
            head, result = self.request({'question': 'MSFT'})
            self.assertEqual(result['error'], 'answer_busy')
            self.assertEqual(head['headers']['Retry-After'], '1')
        finally: self.app.answer_slot.release()
        with patch.object(serve_public.subprocess, 'run', side_effect=serve_public.subprocess.TimeoutExpired('node', 8)):
            self.assertEqual(self.request({'question': 'MSFT'})[1]['error'], 'answer_unavailable')
        self.assertTrue(self.app.answer_slot.acquire(blocking=False))
        self.app.answer_slot.release()

    def test_failed_startup_collection_retries_today_even_after_a_completed_run(self):
        clock = {'now': datetime(2026, 10, 22, 10, tzinfo=timezone.utc), 'loops': 0}
        class Clock:
            @staticmethod
            def now(zone): return clock['now']
        class Stop:
            def is_set(self): return clock['loops'] >= 2
            def wait(self, seconds):
                clock['loops'] += 1
                clock['now'] += timedelta(hours=1, seconds=1)
        app = Mock(root=data.kb.ROOT, store=Mock(directory=self.store.directory), zone='Asia/Jerusalem', clock='08:30')
        app._load.return_value = {'bundle': {'files': {'run-status.json': {'completed_at': '2026-10-22T09:00:00+00:00'}}}}
        collector = serve_public.Collector(app)
        collector.stop_event = Stop()
        with patch.object(serve_public, 'datetime', Clock), patch.object(serve_public.subprocess, 'Popen', side_effect=[Mock(wait=Mock(return_value=1)), Mock(wait=Mock(return_value=0))]) as process:
            collector.run()
        self.assertEqual(process.call_count, 2)


if __name__ == '__main__': unittest.main()
