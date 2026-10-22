"""Lossless migration, snapshot recovery and corruption boundaries for large corpora."""
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
import zlib

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import coverage_backup as backup
from coverage_store import CoverageStore, MIGRATIONS, _json
import coverage_storage
import payload_codec
from coverage_api import serve_coverage


class StorageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.now = datetime(2026, 10, 22, 15, tzinfo=timezone.utc)
        self.path = self.root / 'data.db'
        self.store = CoverageStore(self.path, clock=lambda: self.now)
        self.store.seed_companies([{'cik': 1, 'ticker': 'SYNTH$A', 'company_name': 'Synthetic Preferred', 'exchange': 'NYSE'}])
        self.value = {'synthetic_fixture': True, 'data': [{'period': n, 'value': n * 13, 'note': 'מקור בדיקה' * 10} for n in range(300)]}

    def source(self, hour=10):
        return {'url': 'https://issuer.example/fixture', 'sha256': 'a' * 64,
                'retrieved_at': self.now.replace(hour=hour).isoformat()}

    def test_source_only_versions_deduplicate_content_but_keep_exact_history_and_cas(self):
        sha = self.store.put_payload(1, 'history', self.value, self.source())
        first = self.store.get_payload_record(1, 'history')
        self.store.put_payload(1, 'history', self.value, self.source(11))
        second = self.store.get_payload_record(1, 'history')
        self.assertEqual(first['value'], second['value'])
        self.assertEqual(second['metadata']['version'], 2)
        self.assertEqual(first, self.store.get_payload_record(1, 'history', version=1))
        self.assertIsNone(self.store.put_payload_if_current(1, 'history', {'lost': True}, sha,
                                                           expected_version=first['metadata']['version']))
        info = coverage_storage.status(self.store)
        self.assertEqual((info['unique_objects'], info['object_references'], info['payload_versions']), (1, 2, 2))
        self.assertLess(info['stored_content_bytes'], info['logical_version_bytes'] / 5)
        self.assertEqual(self.store.company('SYNTH$A')['cik'], '0000000001')
        self.assertEqual(serve_coverage(self.store, '/api/companies/SYNTH%24A', '')[0], '200 OK')

    def test_v5_migration_resumes_without_rewriting_dates_hashes_or_versions(self):
        path = self.root / 'legacy.db'
        encoded = _json(self.value)
        digest = hashlib.sha256(encoded.encode()).hexdigest()
        with sqlite3.connect(path) as db:
            for version in range(1, 6):
                for sql in MIGRATIONS[version]:
                    db.execute(sql)
                db.execute('INSERT INTO schema_migrations VALUES (?,?)', (version, self.now.isoformat()))
            db.execute('PRAGMA user_version=5')
            db.execute("INSERT INTO issuers VALUES ('0000000001','Synthetic','{}',?,?)", (self.now.isoformat(),) * 2)
            for version in range(1, 4):
                source = self.source(9 + version)
                db.execute('''INSERT INTO company_payloads(cik,kind,version,sha256,value_json,stored_at,
                    source_url,source_sha256,source_retrieved_at,source_json) VALUES (?,?,?,?,?,?,?,?,?,?)''',
                    ('0000000001', 'history', version, digest, encoded, self.now.isoformat(),
                     source['url'], source['sha256'], source['retrieved_at'], _json(source)))
        store = CoverageStore(path, clock=lambda: self.now)
        original = [store.get_payload_record(1, 'history', version=i) for i in range(1, 4)]
        self.assertEqual(store.compact_payloads(limit=1)['remaining'], 2)
        # A restart may read both inline and compressed versions.
        store = CoverageStore(path, clock=lambda: self.now)
        self.assertEqual([store.get_payload_record(1, 'history', version=i) for i in range(1, 4)], original)
        self.assertEqual(store.compact_payloads(limit=2)['remaining'], 0)
        self.assertEqual(store.compact_payloads()['converted'], 0)
        self.assertEqual([store.get_payload_record(1, 'history', version=i) for i in range(1, 4)], original)
        self.assertEqual(coverage_storage.status(store)['unique_objects'], 1)

    def test_online_backup_cold_restore_preserves_compressed_history(self):
        self.store.put_payload(1, 'history', self.value, self.source())
        self.store.put_payload(1, 'history', {**self.value, 'revised': True}, self.source(11))
        target = self.root / 'snapshot.db'
        backup.backup(self.path, target, compact=True)
        restored = self.root / 'restored.db'
        backup.restore(target, backup.manifest_path(target), restored)
        store = CoverageStore(restored)
        for version in (1, 2):
            self.assertEqual(store.get_payload_record(1, 'history', version=version),
                             self.store.get_payload_record(1, 'history', version=version))
        self.assertEqual(backup.status(target)['status'], 'verified_local_snapshot')

    def test_corrupt_object_never_reads_or_publishes_a_backup(self):
        self.store.put_payload(1, 'history', self.value, self.source())
        with self.store._connection(write=True) as db:
            db.execute('UPDATE payload_objects SET data=?', (zlib.compress(b'{"wrong":true}'),))
        with self.assertRaises(payload_codec.PayloadIntegrityError):
            self.store.get_payload(1, 'history')
        self.assertEqual(serve_coverage(self.store, '/api/companies/1', '')[0], '503 Service Unavailable')
        with self.assertRaises(backup.BackupError):
            backup.backup(self.path, self.root / 'bad.db')
        self.assertFalse((self.root / 'bad.db').exists())

    def test_compaction_digest_failure_rolls_back_entire_batch(self):
        encoded = _json(self.value)
        with self.store._connection(write=True) as db:
            for version, sha in ((1, hashlib.sha256(encoded.encode()).hexdigest()), (2, 'b' * 64)):
                db.execute('''INSERT INTO company_payloads(cik,kind,version,sha256,value_json,stored_at)
                    VALUES ('0000000001','history',?,?,?,?)''', (version, sha, encoded, self.now.isoformat()))
        with self.assertRaisesRegex(ValueError, 'digest mismatch'):
            self.store.compact_payloads()
        info = coverage_storage.status(self.store)
        self.assertEqual((info['unique_objects'], info['legacy_large_payloads']), (0, 2))

    def test_restore_rejects_corrupt_content_even_when_outer_database_hash_matches(self):
        self.store.put_payload(1, 'history', self.value, self.source())
        target = self.root / 'snapshot.db'
        backup.backup(self.path, target)
        with sqlite3.connect(target) as db:
            db.execute('UPDATE payload_objects SET data=?', (zlib.compress(b'{"wrong":true}'),))
        manifest_path = backup.manifest_path(target)
        manifest = json.loads(manifest_path.read_text())
        manifest['snapshot'].update(sha256=backup._hash(target), size_bytes=target.stat().st_size)
        with sqlite3.connect(target) as db:
            manifest['snapshot']['stats'] = backup._snapshot_stats(db)
        manifest_path.write_text(json.dumps(manifest))
        restored = self.root / 'corrupt-restored.db'
        with self.assertRaisesRegex(backup.BackupError, 'payload integrity'):
            backup.restore(target, manifest_path, restored)
        self.assertFalse(restored.exists())

    def test_decode_size_digest_truncation_and_extra_stream_are_rejected(self):
        raw = _json(self.value).encode()
        sha, data = hashlib.sha256(raw).hexdigest(), zlib.compress(raw)
        for digest, size, compressed in ((sha, 1, data), ('b' * 64, len(raw), data),
                                         (sha, len(raw), data[:-1]), (sha, len(raw), data + data)):
            with self.subTest(size=size, digest=digest), self.assertRaises(payload_codec.PayloadIntegrityError):
                payload_codec.unpack(digest, payload_codec.CODEC, size, compressed)
        self.assertEqual(payload_codec.unpack(sha, payload_codec.CODEC, len(raw), data), self.value)

    def test_scoped_claim_does_not_reclaim_or_exhaust_another_queue(self):
        bulk = self.store.enqueue(1, kind='refresh_company_bulk')
        with self.store._connection(write=True) as db:
            db.execute('UPDATE jobs SET max_attempts=1 WHERE id=?', (bulk['job_id'],))
        lease = self.store.claim('bulk', job_id=bulk['job_id'], lease_seconds=1)
        self.now += timedelta(seconds=2)
        online = self.store.enqueue(1)
        self.assertIsNone(self.store.claim('online', job_id=bulk['job_id'], kind='refresh_company'))
        self.assertEqual(self.store.claim('online', kind='refresh_company')['job_id'], online['job_id'])
        with self.store._connection() as db:
            row = db.execute('SELECT status,attempts,lease_token FROM jobs WHERE id=?', (bulk['job_id'],)).fetchone()
        self.assertEqual(tuple(row), ('running', 1, lease['lease_token']))
        self.assertIsNone(self.store.claim('bulk', job_id=bulk['job_id'], kind='refresh_company_bulk'))


if __name__ == '__main__':
    unittest.main()
