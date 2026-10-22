import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import sec_acquire as acquire


class Response(io.BytesIO):
    def __init__(self, kind, raw=b'PK\x03\x04fixture', length=None, url=None):
        super().__init__(raw)
        self.status, self.url = 200, url or acquire.URLS[kind]
        self.headers = {'Content-Length': str(len(raw) if length is None else length)}


class AcquisitionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'archives'
        # Test-only synthetic identity; no tests make network requests.
        self.env = {'STOCK_BRAIN_SEC_ENABLED': '1', 'SEC_USER_AGENT': 'TestApplication tests@fixture.test'}

    def test_streams_fixed_sources_records_hashes_and_never_logs_identity(self):
        opener = Mock()
        opener.open.side_effect = [Response(kind) for kind in acquire.URLS]
        with patch.object(acquire.time, 'sleep'), patch('builtins.print') as output:
            manifest = acquire.acquire(self.path, environ=self.env, opener=opener)
        data = json.loads(manifest.read_text())
        self.assertEqual(data['network_requests'], 2)
        for kind in acquire.URLS:
            self.assertEqual(data[kind]['url'], acquire.URLS[kind])
            self.assertEqual(data[kind]['size_bytes'], (self.path / (kind + '.zip')).stat().st_size)
        self.assertNotIn('fixture.test', str(output.call_args_list) + manifest.read_text())
        self.assertEqual([c.args[0].full_url for c in opener.open.call_args_list], list(acquire.URLS.values()))

    def test_pause_or_missing_identity_prevents_any_request(self):
        for env in ({}, {'STOCK_BRAIN_SEC_ENABLED': '1'}, {**self.env, 'STOCK_BRAIN_SEC_ENABLED': '0'}):
            opener = Mock()
            with self.subTest(env=env), self.assertRaises(ValueError):
                acquire.acquire(self.path, environ=env, opener=opener)
            opener.open.assert_not_called()

    def test_denial_stops_without_retry_second_archive_or_response_body(self):
        opener = Mock()
        opener.open.side_effect = HTTPError(acquire.URLS['submissions'], 403, 'Forbidden', {}, io.BytesIO(b'private-response'))
        with self.assertRaisesRegex(ValueError, 'HTTP 403.*no retry') as error:
            acquire.acquire(self.path, environ=self.env, opener=opener)
        self.assertNotIn('private-response', str(error.exception))
        self.assertEqual(opener.open.call_count, 1)
        self.assertFalse((self.path / 'acquisition.json').exists())

    def test_truncated_oversized_redirected_and_nonzip_downloads_never_publish_manifest(self):
        for response in (Response('submissions', length=200), Response('submissions', length=1),
                         Response('submissions', raw=b'<html>denied'), Response('submissions', url='https://other.test/a')):
            with tempfile.TemporaryDirectory() as temp:
                path = Path(temp) / 'archives'
                with self.assertRaises(ValueError):
                    acquire.acquire(path, environ=self.env, opener=Mock(open=Mock(return_value=response)))
                self.assertFalse((path / 'acquisition.json').exists())
                self.assertFalse((path / 'submissions.zip').exists())
                self.assertFalse((path / 'submissions.partial').exists())

    def test_redirect_handler_never_follows(self):
        self.assertIsNone(acquire.NoRedirect().redirect_request(None, None, 302, None, None, 'https://other.test'))


if __name__ == '__main__':
    unittest.main()
