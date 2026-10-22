from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import threading
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import coverage_release as release
from coverage_store import CoverageStore
import market_directory as directory
from test_market_directory import fixtures, NOW


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = CoverageStore(self.root / 'working.db', clock=lambda: NOW)
        directory.import_directories(self.store, fixtures())
        self.out = self.root / 'release'
        self.manifest = release.package(self.store, self.out, release_tag='coverage-20261022-123-1', execution={'event': 'test'})

    def test_roundtrip_preserves_directory_and_cold_restores_empty_database(self):
        target = self.root / 'restored.db'
        release.unpack(self.out / release.ASSET, self.out / release.MANIFEST, target)
        restored = CoverageStore(target, clock=lambda: NOW)
        self.assertEqual(directory.list_securities(restored, instrument='all'), directory.list_securities(self.store, instrument='all'))
        self.assertEqual(self.manifest['database_manifest']['snapshot']['stats']['table_row_counts']['market_securities'], 16)
        with self.assertRaises(ValueError): release.unpack(self.out / release.ASSET, self.out / release.MANIFEST, target)

    def test_corrupt_bytes_and_incompatible_schema_never_install(self):
        compressed = self.out / release.ASSET
        original = compressed.read_bytes()
        compressed.write_bytes(original[:-1] + bytes([original[-1] ^ 1]))
        target = self.root / 'bad.db'
        with self.assertRaises(ValueError): release.unpack(compressed, self.out / release.MANIFEST, target)
        self.assertFalse(target.exists())
        compressed.write_bytes(original)
        changed = deepcopy(self.manifest)
        changed['database_manifest']['snapshot']['stats']['database_schema_version'] = 999
        (self.out / release.MANIFEST).write_text(json.dumps(changed))
        with self.assertRaises(ValueError): release.unpack(compressed, self.out / release.MANIFEST, target)
        self.assertFalse(target.exists())

    def test_decompression_capacity_limit_and_tag_validation(self):
        changed = deepcopy(self.manifest)
        changed['database_manifest']['snapshot']['size_bytes'] = release.MAX_DATABASE + 1
        (self.out / release.MANIFEST).write_text(json.dumps(changed))
        with self.assertRaises(ValueError): release.unpack(self.out / release.ASSET, self.out / release.MANIFEST, self.root / 'huge.db')
        with self.assertRaises(ValueError): release.download_release({'tag_name': '../other'}, self.root / 'unsafe.db')

    def test_partial_release_is_not_selected_before_offhost_proof(self):
        def fake_download(url, destination, limit):
            complete = {'tag_name': 'coverage-20261022-123-1', 'published_at': '2026-10-22T12:00:00Z',
                        'assets': [{'name': n} for n in (release.ASSET, release.MANIFEST, release.PROOF)]}
            newer = {**complete, 'tag_name': 'coverage-20261022-124-1', 'published_at': '2026-10-22T13:00:00Z',
                     'assets': [{'name': n} for n in (release.ASSET, release.MANIFEST)]}
            Path(destination).write_text(json.dumps([newer, complete]))
        with patch.object(release, '_download', fake_download):
            self.assertEqual(release.latest_release()['tag_name'], 'coverage-20261022-123-1')

    def test_mirror_failure_retains_previous_database_without_exposing_error_body(self):
        app = SimpleNamespace(coverage=self.store, coverage_lock=threading.RLock())
        mirror = release.CoverageMirror(app)
        with patch.object(release, 'latest_release', side_effect=ValueError('secret-provider-body')):
            mirror.refresh()
        self.assertIs(app.coverage, self.store)
        self.assertEqual(mirror.state['status'], 'degraded')
        self.assertNotIn('secret', json.dumps(mirror.state))

    def test_mirror_installs_verified_generation_and_retains_previous_then_prunes_older(self):
        app = SimpleNamespace(root=self.root, coverage=self.store, coverage_lock=threading.RLock(),
            store=SimpleNamespace(directory=self.root, read=lambda: {'files': {'desk.json': {}}}))
        mirror = release.CoverageMirror(app)
        def download(item, path):
            return release.unpack(self.out / release.ASSET, self.out / release.MANIFEST, path)
        paths = []
        for number in range(3):
            with patch.object(release, 'latest_release', return_value={'tag_name': f'coverage-20261022-{123 + number}-1'}), \
                 patch.object(release, 'download_release', side_effect=download), \
                 patch.object(release, 'initialize_coverage', side_effect=lambda root, snapshot, path: CoverageStore(path)):
                mirror.refresh()
            self.assertEqual(mirror.state['status'], 'ready')
            self.assertEqual(directory.list_securities(app.coverage)['total'], 13)
            paths.append(app.coverage.path)
        self.assertFalse(paths[0].exists())
        self.assertTrue(paths[1].exists())
        self.assertTrue(paths[2].exists())
        self.assertTrue(self.store.path.exists())


if __name__ == '__main__': unittest.main()
