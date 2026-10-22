#!/usr/bin/env python3
"""Local, verified SQLite snapshots; no claim of off-host durability.

Examples::

    python scripts/coverage_backup.py backup build/coverage.sqlite3 /mounted/coverage-20261022.sqlite3
    python scripts/coverage_backup.py status /mounted/coverage-20261022.sqlite3
    python scripts/coverage_backup.py restore snapshot.sqlite3 snapshot.sqlite3.manifest.json restored.sqlite3

Use versioned backup destinations. ``backup --replace`` only replaces a verified
previous snapshot. Database and manifest are individually atomically renamed,
with the manifest last; they are not a two-file atomic transaction. A crash
between renames leaves a missing/mismatched manifest and verification fails.

Before ``restore --replace --quiesced``, stop every reader, writer and scheduled
job using the destination; checkpoint and close it normally. The flag records
the operator's assertion, not proof that processes have stopped. Existing WAL,
SHM or rollback-journal files cause refusal; this tool never removes them.
Restore while the service remains stopped, then reopen it after success.

Keep both snapshot and manifest in operator-managed durable storage outside an
ephemeral host. This CLI does not upload anything, configure persistence, or
authenticate provenance: a hash detects mismatches, not a malicious replacement
of both files. Only restore a trusted snapshot and manifest.
"""
from contextlib import closing, contextmanager, ExitStack
from datetime import datetime, timezone
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import sqlite3
import tempfile
import time


MANIFEST_VERSION = 1
FORMAT = 'stock-brain-sqlite-online-backup'
WARNING = 'Local verification only; off-host durable storage and recovery after host loss are not verified.'
SQLITE_HEADER = b'SQLite format 3\x00'
SIDECARS = ('-wal', '-shm', '-journal')


class BackupError(ValueError):
    """A snapshot or destination cannot be used safely."""


def _now():
    return datetime.now(timezone.utc).isoformat()


def manifest_path(snapshot):
    return Path(str(snapshot) + '.manifest.json')


def _path(value):
    # Do not resolve a destination symlink into an unintended overwrite target.
    return Path(os.path.abspath(os.fspath(value)))


def _file(path):
    if not path.is_file() or path.is_symlink():
        raise BackupError(f'Expected an existing regular file, not a symlink: {path}')


def _no_sidecars(path):
    found = [str(path) + suffix for suffix in SIDECARS
             if os.path.lexists(str(path) + suffix)]
    if found:
        raise BackupError('SQLite sidecars exist; stop users and checkpoint/close normally: ' + ', '.join(found))


def _distinct(destination, *inputs):
    for source in inputs:
        if destination.resolve() == source.resolve() or (
                destination.exists() and source.exists() and os.path.samefile(destination, source)):
            raise BackupError('Destination must not overwrite an input file')
        if destination.resolve() in {Path(str(source) + suffix).resolve() for suffix in SIDECARS}:
            raise BackupError('Destination must not overwrite an input SQLite sidecar')


def _hash(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def _sync_file(path):
    with path.open('rb') as stream:
        os.fsync(stream.fileno())


def _sync_directory(path):
    descriptor = os.open(path, os.O_RDONLY | getattr(os, 'O_DIRECTORY', 0))
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _temporary(parent, name):
    descriptor, name = tempfile.mkstemp(prefix='.' + name + '.', suffix='.tmp', dir=parent)
    os.close(descriptor)
    return Path(name)


def _cleanup_temporary(path):
    # Only the unique temporary pathname allocated by this invocation is removed.
    for suffix in ('', *SIDECARS):
        temporary = Path(str(path) + suffix)
        if os.path.lexists(temporary):
            temporary.unlink()


@contextmanager
def _destination_lock(destination):
    lock = Path(str(destination) + '.backup.lock')
    try:
        descriptor = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError as error:
        raise BackupError(f'Destination lock exists: {lock}; do not remove it until its owner is stopped') from error
    identity = os.fstat(descriptor)
    try:
        os.write(descriptor, json.dumps({'pid': os.getpid(), 'created_at': _now()}).encode())
        os.fsync(descriptor)
        yield
    finally:
        os.close(descriptor)
        try:
            current = lock.lstat()
            if (current.st_dev, current.st_ino) == (identity.st_dev, identity.st_ino):
                lock.unlink()
        except FileNotFoundError:
            pass


def _connect_readonly(path, *, snapshot=False):
    uri = path.as_uri() + '?mode=ro' + ('&immutable=1' if snapshot else '')
    connection = sqlite3.connect(uri, uri=True, timeout=5)
    connection.execute('PRAGMA query_only=ON')
    connection.execute('PRAGMA trusted_schema=OFF')
    return connection


def _check(connection, full=False):
    result = connection.execute('PRAGMA integrity_check' if full else 'PRAGMA quick_check').fetchall()
    if result != [('ok',)]:
        raise BackupError('SQLite integrity check failed: ' + repr(result[:5]))


def _snapshot_stats(connection):
    # Counts come from the copied snapshot, never from a later live-source read.
    names = connection.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name").fetchall()
    counts = {}
    for (name,) in names:
        quoted = '"' + name.replace('"', '""') + '"'
        counts[name] = connection.execute('SELECT COUNT(*) FROM ' + quoted).fetchone()[0]
    return {'database_schema_version': connection.execute('PRAGMA user_version').fetchone()[0],
            'sqlite_schema_version': connection.execute('PRAGMA schema_version').fetchone()[0],
            'application_id': connection.execute('PRAGMA application_id').fetchone()[0],
            'page_count': connection.execute('PRAGMA page_count').fetchone()[0],
            'page_size': connection.execute('PRAGMA page_size').fetchone()[0],
            'table_row_counts': counts}


def _manifest(path, snapshot):
    _file(path)
    if path.stat().st_size > 1024 * 1024:
        raise BackupError('Manifest exceeds the 1 MiB limit')
    try:
        value = json.loads(path.read_text(encoding='utf-8'))
    except (ValueError, UnicodeError) as error:
        raise BackupError('Invalid JSON manifest') from error
    if not isinstance(value, dict) or type(value.get('schema_version')) is not int or value.get('schema_version') != MANIFEST_VERSION or value.get('format') != FORMAT:
        raise BackupError('Unsupported backup manifest format/version')
    artifact = value.get('snapshot')
    if not isinstance(artifact, dict) or artifact.get('file_name') != snapshot.name:
        raise BackupError('Manifest names a different snapshot')
    if not isinstance(artifact.get('sha256'), str) or not re.fullmatch('[0-9a-f]{64}', artifact['sha256']):
        raise BackupError('Manifest needs a SHA-256 digest')
    if type(artifact.get('size_bytes')) is not int or artifact['size_bytes'] < 512 or artifact.get('integrity_check') != 'ok':
        raise BackupError('Manifest snapshot size/integrity evidence is invalid')
    if not isinstance(artifact.get('stats'), dict) or type(artifact['stats'].get('database_schema_version')) is not int:
        raise BackupError('Manifest lacks the database schema version')
    return value


def _verify_bytes(path, manifest):
    artifact = manifest['snapshot']
    if path.stat().st_size != artifact['size_bytes'] or _hash(path) != artifact['sha256']:
        raise BackupError('Snapshot bytes do not match the manifest SHA-256/size')
    with path.open('rb') as stream:
        if stream.read(len(SQLITE_HEADER)) != SQLITE_HEADER:
            raise BackupError('Snapshot is not a SQLite database')
    connection = _connect_readonly(path, snapshot=True)
    try:
        _check(connection)
        if _snapshot_stats(connection) != artifact['stats']:
            raise BackupError('Snapshot statistics/schema differ from the manifest')
    finally:
        connection.close()
    if path.stat().st_size != artifact['size_bytes'] or _hash(path) != artifact['sha256']:
        raise BackupError('Snapshot changed during verification')


def status(snapshot, manifest=None):
    """Read-only verification; existence alone never means verified or durable."""
    snapshot = _path(snapshot)
    manifest = _path(manifest) if manifest is not None else manifest_path(snapshot)
    result = {'snapshot_path': str(snapshot), 'manifest_path': str(manifest),
              'durability': 'not_verified', 'warnings': [WARNING]}
    try:
        _file(snapshot)
        _no_sidecars(snapshot)
        value = _manifest(manifest, snapshot)
        _verify_bytes(snapshot, value)
        result.update(status='verified_local_snapshot', sha256=value['snapshot']['sha256'],
                      completed_at=value.get('completed_at'), stats=value['snapshot']['stats'])
    except (BackupError, OSError, sqlite3.Error) as error:
        result.update(status='unverified', error=str(error))
    return result


def backup(source, target, *, replace=False, timeout=300):
    """Create a standalone, consistent SQLite online backup and its manifest."""
    source, target = _path(source), _path(target)
    _file(source)
    manifest = manifest_path(target)
    _distinct(target, source)
    _distinct(manifest, source)
    if not isinstance(timeout, (int, float)) or not math.isfinite(timeout) or timeout <= 0:
        raise BackupError('Timeout must be a positive finite number of seconds')
    if not target.parent.is_dir():
        raise BackupError('Destination directory must already exist')
    started = _now()
    with _destination_lock(target):
        _no_sidecars(target)
        if os.path.lexists(target) or os.path.lexists(manifest):
            if not replace:
                raise BackupError('Backup destination exists; use a new path or explicit --replace')
            if status(target, manifest)['status'] != 'verified_local_snapshot':
                raise BackupError('Only an existing verified snapshot may be replaced; choose a new destination')
        temporary = _temporary(target.parent, target.name)
        temporary_manifest = _temporary(target.parent, manifest.name)
        try:
            deadline = time.monotonic() + timeout
            def progress(*_):
                if time.monotonic() > deadline:
                    raise BackupError('SQLite online backup exceeded its timeout')
            with ExitStack() as connections:
                reader = connections.enter_context(closing(_connect_readonly(source)))
                writer = connections.enter_context(closing(sqlite3.connect(temporary)))
                # Pin a read snapshot, including committed WAL pages, before copy.
                reader.execute('BEGIN')
                reader.execute('SELECT name FROM sqlite_schema LIMIT 1').fetchone()
                reader.backup(writer, pages=256, progress=progress, sleep=0.05)
                writer.execute('PRAGMA trusted_schema=OFF')
                writer.execute('PRAGMA journal_mode=DELETE')
                _check(writer, full=True)
                stats = _snapshot_stats(writer)
            _no_sidecars(temporary)
            _sync_file(temporary)
            value = {'schema_version': MANIFEST_VERSION, 'format': FORMAT,
                     'started_at': started, 'completed_at': _now(),
                     'source': {'path': str(source), 'snapshot_method': 'sqlite3.Connection.backup with pinned read transaction'},
                     'snapshot': {'file_name': target.name, 'sha256': _hash(temporary),
                                  'size_bytes': temporary.stat().st_size, 'integrity_check': 'ok', 'stats': stats},
                     'sqlite_version': sqlite3.sqlite_version,
                     'durability': 'not_verified', 'warnings': [WARNING]}
            temporary_manifest.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            _sync_file(temporary_manifest)
            os.replace(temporary, target)
            _sync_directory(target.parent)
            os.replace(temporary_manifest, manifest)
            _sync_directory(target.parent)
            return {'status': 'verified_local_snapshot', 'snapshot_path': str(target),
                    'manifest_path': str(manifest), 'manifest': value,
                    'durability': 'not_verified', 'warnings': [WARNING]}
        finally:
            _cleanup_temporary(temporary)
            _cleanup_temporary(temporary_manifest)


def restore(snapshot, manifest, destination, *, replace=False, quiesced=False):
    """Validate a staged copy before installation; never erase SQLite sidecars."""
    snapshot, manifest, destination = map(_path, (snapshot, manifest, destination))
    _file(snapshot)
    _no_sidecars(snapshot)
    _distinct(destination, snapshot, manifest)
    if replace and not quiesced:
        raise BackupError('--replace requires --quiesced after stopping all readers, writers and jobs')
    if not destination.parent.is_dir():
        raise BackupError('Destination directory must already exist')
    value = _manifest(manifest, snapshot)
    with _destination_lock(destination):
        _no_sidecars(destination)
        if os.path.lexists(destination):
            _file(destination)
            if not replace or not quiesced:
                raise BackupError('Existing destination requires --replace --quiesced after stopping all readers, writers and jobs')
        temporary = _temporary(destination.parent, destination.name)
        try:
            # Verify the actual copied bytes, avoiding a hash-then-copy race.
            with snapshot.open('rb') as source, temporary.open('wb') as output:
                shutil.copyfileobj(source, output, length=1024 * 1024)
                output.flush()
                os.fsync(output.fileno())
            _verify_bytes(temporary, value)
            # Recheck before publication; no live journal is ever removed.
            _no_sidecars(destination)
            if not replace and os.path.lexists(destination):
                raise BackupError('Destination appeared while restore was being prepared')
            if replace:
                os.replace(temporary, destination)
            else:
                # Atomic no-clobber publication also protects against a file
                # appearing after the existence check. Both paths share a device.
                os.link(temporary, destination, follow_symlinks=False)
                temporary.unlink()
            _sync_directory(destination.parent)
            return {'status': 'restored_local_copy', 'destination_path': str(destination),
                    'sha256': value['snapshot']['sha256'], 'quick_check': 'ok',
                    'stats': value['snapshot']['stats'], 'operator_asserted_quiesced': bool(quiesced),
                    'durability': 'not_verified', 'warnings': [WARNING]}
        finally:
            _cleanup_temporary(temporary)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest='command', required=True)
    make = commands.add_parser('backup', help='Create a local, verified online snapshot')
    make.add_argument('source', type=Path)
    make.add_argument('target', type=Path)
    make.add_argument('--replace', action='store_true', help='Replace only an existing verified backup pair')
    make.add_argument('--timeout', type=float, default=300)
    load = commands.add_parser('restore', help='Restore only after validating copied bytes and SQLite integrity')
    load.add_argument('snapshot', type=Path)
    load.add_argument('manifest', type=Path)
    load.add_argument('destination', type=Path)
    load.add_argument('--replace', action='store_true', help='Explicitly allow replacing the destination')
    load.add_argument('--quiesced', action='store_true', help='Assert every destination reader/writer/job is stopped and SQLite was checkpointed and closed')
    inspect = commands.add_parser('status', help='Verify bytes, manifest and SQLite; does not prove persistence')
    inspect.add_argument('snapshot', type=Path)
    inspect.add_argument('--manifest', type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == 'backup':
            result = backup(args.source, args.target, replace=args.replace, timeout=args.timeout)
        elif args.command == 'restore':
            result = restore(args.snapshot, args.manifest, args.destination, replace=args.replace, quiesced=args.quiesced)
        else:
            result = status(args.snapshot, args.manifest)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result['status'] == 'unverified' else 0
    except (BackupError, OSError, sqlite3.Error) as error:
        print(json.dumps({'status': 'error', 'error': str(error), 'durability': 'not_verified', 'warnings': [WARNING]}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
