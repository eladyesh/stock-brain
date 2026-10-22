from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import coverage_backup as snapshots


class CoverageBackupTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.source = self.root / 'coverage.sqlite3'
        self.snapshot = self.root / 'backup.sqlite3'
        self.destination = self.root / 'restored.sqlite3'
        with sqlite3.connect(self.source) as connection:
            connection.execute('PRAGMA user_version=1')
            connection.execute('CREATE TABLE issuers (cik TEXT PRIMARY KEY, name TEXT NOT NULL)')
            connection.execute('CREATE TABLE jobs (id INTEGER PRIMARY KEY, status TEXT NOT NULL)')
            connection.execute('INSERT INTO issuers VALUES (?, ?)', ('0000789019', 'Microsoft'))
            connection.execute('INSERT INTO jobs VALUES (1, ?)', ('pending',))

    def _backup(self):
        return snapshots.backup(self.source, self.snapshot)

    def _rows(self, path, table='issuers'):
        with sqlite3.connect(path) as connection:
            return connection.execute('SELECT * FROM ' + table + ' ORDER BY 1').fetchall()

    def _manifest(self):
        return snapshots.manifest_path(self.snapshot)

    def test_round_trip_and_snapshot_statistics(self):
        result = self._backup()
        manifest = json.loads(self._manifest().read_text())
        self.assertEqual(result['status'], 'verified_local_snapshot')
        self.assertEqual(manifest['schema_version'], 1)
        self.assertEqual(manifest['snapshot']['stats']['database_schema_version'], 1)
        self.assertEqual(manifest['snapshot']['stats']['table_row_counts'], {'issuers': 1, 'jobs': 1})
        self.assertEqual(manifest['snapshot']['sha256'], hashlib.sha256(self.snapshot.read_bytes()).hexdigest())
        self.assertIn('+00:00', manifest['started_at'])
        self.assertIn('+00:00', manifest['completed_at'])
        restored = snapshots.restore(self.snapshot, self._manifest(), self.destination)
        self.assertEqual(restored['status'], 'restored_local_copy')
        self.assertEqual(self._rows(self.destination), self._rows(self.source))
        self.assertEqual(snapshots.status(self.snapshot)['status'], 'verified_local_snapshot')
        self.assertEqual(restored['durability'], 'not_verified')
        self.assertTrue(restored['warnings'])

    def test_committed_wal_pages_are_included_without_checkpointing_live_source(self):
        writer = sqlite3.connect(self.source)
        self.addCleanup(writer.close)
        writer.execute('PRAGMA journal_mode=WAL')
        writer.execute('PRAGMA wal_autocheckpoint=0')
        writer.execute('PRAGMA wal_checkpoint(TRUNCATE)')
        main_before = self.source.read_bytes()
        writer.execute('INSERT INTO issuers VALUES (?, ?)', ('0000101829', 'RTX'))
        writer.commit()
        wal = Path(str(self.source) + '-wal')
        self.assertGreater(wal.stat().st_size, 0)
        self.assertEqual(self.source.read_bytes(), main_before)
        self._backup()
        self.assertEqual(len(self._rows(self.snapshot)), 2)
        self.assertEqual(self.source.read_bytes(), main_before)
        self.assertTrue(wal.exists())
        self.assertFalse(Path(str(self.snapshot) + '-wal').exists())
        snapshots.restore(self.snapshot, self._manifest(), self.destination)
        self.assertEqual(len(self._rows(self.destination)), 2)

    def test_concurrent_commits_do_not_split_a_multi_table_transaction(self):
        with sqlite3.connect(self.source) as connection:
            connection.execute('PRAGMA journal_mode=WAL')
            connection.execute('CREATE TABLE left_updates (id INTEGER PRIMARY KEY, payload BLOB)')
            connection.execute('CREATE TABLE right_updates (id INTEGER PRIMARY KEY, payload BLOB)')
        started, stop = threading.Event(), threading.Event()
        failures = []
        def write():
            connection = sqlite3.connect(self.source, timeout=5)
            try:
                i = 0
                while not stop.is_set():
                    i += 1
                    with connection:
                        connection.execute('INSERT INTO left_updates VALUES (?, ?)', (i, b'x' * 4096))
                        connection.execute('INSERT INTO right_updates VALUES (?, ?)', (i, b'y' * 4096))
                    started.set()
            except Exception as error:
                failures.append(error)
                started.set()
            finally:
                connection.close()
        thread = threading.Thread(target=write, daemon=True)
        thread.start()
        try:
            self.assertTrue(started.wait(5))
            result = self._backup()
        finally:
            stop.set()
            thread.join(5)
        self.assertFalse(thread.is_alive())
        self.assertEqual(failures, [])
        with sqlite3.connect(self.snapshot) as connection:
            left = connection.execute('SELECT id FROM left_updates ORDER BY id').fetchall()
            right = connection.execute('SELECT id FROM right_updates ORDER BY id').fetchall()
        self.assertTrue(left)
        self.assertEqual(left, right)
        counts = result['manifest']['snapshot']['stats']['table_row_counts']
        self.assertEqual(counts['left_updates'], len(left))
        self.assertEqual(counts['right_updates'], len(right))

    def test_hash_mismatch_refuses_restore_and_keeps_existing_destination(self):
        self._backup()
        self.destination.write_bytes(b'existing destination must survive')
        before = self.destination.read_bytes()
        raw = bytearray(self.snapshot.read_bytes())
        raw[-1] ^= 1
        self.snapshot.write_bytes(raw)
        self.assertEqual(snapshots.status(self.snapshot)['status'], 'unverified')
        with self.assertRaisesRegex(snapshots.BackupError, 'SHA-256'):
            snapshots.restore(self.snapshot, self._manifest(), self.destination, replace=True, quiesced=True)
        self.assertEqual(self.destination.read_bytes(), before)

    def test_matching_hash_does_not_make_a_corrupt_sqlite_file_restorable(self):
        self._backup()
        raw = bytearray(self.snapshot.read_bytes())
        raw[100] = 0  # Invalid b-tree page type; leave the SQLite header intact.
        self.snapshot.write_bytes(raw)
        manifest = json.loads(self._manifest().read_text())
        manifest['snapshot']['sha256'] = hashlib.sha256(raw).hexdigest()
        self._manifest().write_text(json.dumps(manifest))
        with self.assertRaises((snapshots.BackupError, sqlite3.DatabaseError)):
            snapshots.restore(self.snapshot, self._manifest(), self.destination)
        self.assertFalse(self.destination.exists())
        self.assertEqual(snapshots.status(self.snapshot)['status'], 'unverified')

    def test_restore_requires_explicit_replace_and_quiescence(self):
        self._backup()
        snapshots.restore(self.snapshot, self._manifest(), self.destination)
        before = self.destination.read_bytes()
        for kwargs in ({}, {'replace': True}, {'quiesced': True}):
            with self.assertRaisesRegex(snapshots.BackupError, 'quiesced'):
                snapshots.restore(self.snapshot, self._manifest(), self.destination, **kwargs)
            self.assertEqual(self.destination.read_bytes(), before)
        result = snapshots.restore(self.snapshot, self._manifest(), self.destination, replace=True, quiesced=True)
        self.assertTrue(result['operator_asserted_quiesced'])

    def test_live_destination_sidecars_are_never_deleted(self):
        self._backup()
        snapshots.restore(self.snapshot, self._manifest(), self.destination)
        writer = sqlite3.connect(self.destination)
        self.addCleanup(writer.close)
        writer.execute('PRAGMA journal_mode=WAL')
        writer.execute('INSERT INTO issuers VALUES (?, ?)', ('new', 'Only in destination WAL'))
        writer.commit()
        wal = Path(str(self.destination) + '-wal')
        wal_before = wal.read_bytes()
        with self.assertRaisesRegex(snapshots.BackupError, 'sidecars'):
            snapshots.restore(self.snapshot, self._manifest(), self.destination, replace=True, quiesced=True)
        self.assertEqual(wal.read_bytes(), wal_before)
        self.assertEqual(writer.execute('SELECT COUNT(*) FROM issuers').fetchone()[0], 2)

    def test_input_aliases_and_symlink_destinations_are_refused(self):
        with self.assertRaises(snapshots.BackupError):
            snapshots.backup(self.source, self.source)
        self._backup()
        with self.assertRaises(snapshots.BackupError):
            snapshots.restore(self.snapshot, self._manifest(), self.snapshot, replace=True, quiesced=True)
        self.destination.symlink_to(self.source)
        before = self.source.read_bytes()
        with self.assertRaisesRegex(snapshots.BackupError, 'symlink'):
            snapshots.restore(self.snapshot, self._manifest(), self.destination, replace=True, quiesced=True)
        self.assertEqual(self.source.read_bytes(), before)

    def test_restore_never_clobbers_a_destination_created_during_publication(self):
        self._backup()
        original_link = snapshots.os.link
        def create_competing_file(source, destination, **kwargs):
            Path(destination).write_bytes(b'created by another process')
            return original_link(source, destination, **kwargs)
        with patch.object(snapshots.os, 'link', side_effect=create_competing_file):
            with self.assertRaises(FileExistsError):
                snapshots.restore(self.snapshot, self._manifest(), self.destination)
        self.assertEqual(self.destination.read_bytes(), b'created by another process')

    def test_file_existence_and_missing_manifest_never_claim_durability(self):
        self.snapshot.write_bytes(self.source.read_bytes())
        result = snapshots.status(self.snapshot)
        self.assertEqual(result['status'], 'unverified')
        self.assertEqual(result['durability'], 'not_verified')
        self.assertTrue(result['warnings'])

    def test_interrupted_manifest_publication_is_detected(self):
        self._backup()
        with sqlite3.connect(self.source) as connection:
            connection.execute('INSERT INTO issuers VALUES (?, ?)', ('new', 'New snapshot'))
        original_replace = snapshots.os.replace
        def interrupt(source, destination):
            if Path(destination) == self._manifest():
                raise OSError('Simulated interruption before manifest publication')
            return original_replace(source, destination)
        with patch.object(snapshots.os, 'replace', side_effect=interrupt):
            with self.assertRaisesRegex(OSError, 'interruption'):
                snapshots.backup(self.source, self.snapshot, replace=True)
        self.assertEqual(snapshots.status(self.snapshot)['status'], 'unverified')
        self.assertFalse(Path(str(self.snapshot) + '.backup.lock').exists())
        self.assertEqual(list(self.root.glob('.*.tmp')), [])

    def test_backup_replacement_requires_a_verified_existing_pair(self):
        self._backup()
        with self.assertRaisesRegex(snapshots.BackupError, 'exists'):
            self._backup()
        snapshots.backup(self.source, self.snapshot, replace=True)
        self._manifest().unlink()
        with self.assertRaisesRegex(snapshots.BackupError, 'verified snapshot'):
            snapshots.backup(self.source, self.snapshot, replace=True)

    def test_table_names_are_quoted_as_identifiers_not_executed_as_sql(self):
        name = 'strange"; DROP TABLE issuers;--'
        with sqlite3.connect(self.source) as connection:
            connection.execute('CREATE TABLE "' + name.replace('"', '""') + '" (value INTEGER)')
        result = self._backup()
        self.assertIn(name, result['manifest']['snapshot']['stats']['table_row_counts'])
        self.assertEqual(len(self._rows(self.snapshot)), 1)

    def test_cli_reports_verification_and_errors_as_json(self):
        output = io.StringIO()
        with redirect_stdout(output):
            code = snapshots.main(['backup', str(self.source), str(self.snapshot)])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(output.getvalue())['status'], 'verified_local_snapshot')
        output = io.StringIO()
        with redirect_stdout(output):
            code = snapshots.main(['status', str(self.root / 'missing.sqlite3')])
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(output.getvalue())['status'], 'unverified')


if __name__ == '__main__':
    unittest.main()
