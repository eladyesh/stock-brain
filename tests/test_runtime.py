from datetime import datetime, timezone
import gzip
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import backup_runtime
import runtime_data as data
from serve_public import Application


class RuntimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory()
        cls.store = data.StateStore(Path(cls.temporary.name) / 'state')
        cls.root = data.kb.ROOT
        data.initialize(cls.root, cls.store)
        cls.bundle = cls.store.read()

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def test_atomic_checkpoint_rejects_mixed_generation_and_preserves_previous(self):
        original = self.store.path.read_bytes()
        broken = json.loads(original)
        broken['files']['run-status.json']['completed_at'] = '2026-01-01T00:00:00+00:00'
        with self.assertRaises(ValueError): self.store.commit(broken)
        self.assertEqual(original, self.store.path.read_bytes())

    def test_failed_collection_does_not_replace_served_data(self):
        original = self.store.path.read_bytes()
        with patch.object(data.refresh_desk, 'refresh', side_effect=OSError('source unavailable')):
            with self.assertRaises(OSError): data.collect(self.root, self.store)
        self.assertEqual(original, self.store.path.read_bytes())
        attempt = data.p.read_json(self.store.directory / 'attempt.json')
        self.assertEqual(attempt['status'], 'failed')
        self.assertTrue(attempt['previous_data_retained'])

    def test_cold_restore_preserves_queue_reviews_prices_and_histories(self):
        with tempfile.TemporaryDirectory() as directory:
            store = data.StateStore(directory)
            with patch.object(data, 'github_checkpoint', return_value=self.bundle) as restore:
                data.initialize(self.root, store, bootstrap=True)
                restore.assert_called_once()
            restored = store.read()['files']
            for name in ['latest.json', 'triage.json', 'run-status.json']:
                self.assertEqual(restored[name], self.bundle['files'][name])
            for old, new in zip(self.bundle['files']['desk.json']['companies'], restored['desk.json']['companies']):
                self.assertEqual(old['history'], new['history'])
                self.assertEqual(old['quote'], new['quote'])
            with patch.object(data, 'github_checkpoint', side_effect=AssertionError('unexpected network')):
                data.initialize(self.root, store, bootstrap=True)

    def test_expected_remote_checkpoint_failure_does_not_reset_state(self):
        with tempfile.TemporaryDirectory() as directory:
            store = data.StateStore(directory)
            with patch.object(data, 'github_checkpoint', side_effect=OSError('offline')):
                with self.assertRaises(OSError): data.initialize(self.root, store, bootstrap=True)
            self.assertFalse(store.path.exists())

    def test_daily_schedule_uses_israel_timezone_and_handles_dst(self):
        for now, expected in [('2026-10-24T00:00:00+00:00', '2026-10-24T05:30:00+00:00'),
                              ('2026-10-25T00:00:00+00:00', '2026-10-25T06:30:00+00:00')]:
            self.assertEqual(data.next_refresh(datetime.fromisoformat(now), None).isoformat(), expected)
        now = datetime(2026, 10, 22, 10, tzinfo=timezone.utc)
        self.assertEqual(data.next_refresh(now, '2026-10-21T10:00:00+00:00'), now)
        self.assertEqual(data.next_refresh(now, now.isoformat()).isoformat(), '2026-10-23T05:30:00+00:00')

    def test_backup_does_not_overwrite_a_newer_refresh_with_an_older_rebuild(self):
        old = json.loads(json.dumps(self.bundle['files']))
        old['run-status.json']['completed_at'] = '2026-01-01T00:00:00+00:00'
        old['desk.json']['built_at'] = '2030-01-01T00:00:00+00:00'
        self.assertFalse(backup_runtime.newer(old, self.bundle['files']))
        self.assertFalse(backup_runtime.newer(self.bundle['files'], self.bundle['files']))

    def test_public_routes_are_read_only_and_do_not_expose_repository_files(self):
        app = Application(self.root, self.store, scheduler_enabled=False)
        def request(path, **extra):
            received = {}
            def start(status, headers): received.update(status=status, headers=dict(headers))
            body = b''.join(app({'PATH_INFO': path, 'REQUEST_METHOD': 'GET', 'wsgi.input': io.BytesIO(), **extra}, start))
            return received, body
        for path in ['/.env', '/.git/config', '/research/monitoring/triage.json', '/../README.md', '/api/refresh']:
            self.assertEqual(request(path)[0]['status'], '404 Not Found')
        self.assertEqual(request('/api/snapshot', REQUEST_METHOD='POST')[0]['status'], '405 Method Not Allowed')
        head, body = request('/api/snapshot', HTTP_ACCEPT_ENCODING='gzip')
        self.assertEqual(head['headers']['Content-Encoding'], 'gzip')
        self.assertEqual(json.loads(gzip.decompress(body)), self.bundle['files']['desk.json'])
        self.assertEqual(request('/api/snapshot', HTTP_IF_NONE_MATCH=head['headers']['ETag'])[0]['status'], '304 Not Modified')
        self.assertEqual(request('/api/snapshot', REQUEST_METHOD='HEAD')[1], b'')
        self.assertEqual(json.loads(request('/api/state')[1]), self.bundle)
        self.assertEqual(json.loads(request('/healthz')[1])['status'], 'ok')
        self.assertIn("connect-src 'self'", request('/')[0]['headers']['Content-Security-Policy'])


if __name__ == '__main__': unittest.main()
