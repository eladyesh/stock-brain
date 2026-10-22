"""Verified, immutable coverage releases in the existing public GitHub repository.

The daily builder is the only broad-registry writer. Web replicas download and
validate a new generation before swapping readers; no live SQLite file is replaced.
Releases contain public research data only. API credentials are never persisted.
"""
import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import json
import logging
import os
from pathlib import Path
import re
import shutil
import sqlite3
import subprocess
import tempfile
import threading
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import coverage_backup as backup
from coverage_runtime import initialize_coverage
from coverage_store import CoverageStore, SCHEMA_VERSION, require
import market_directory
import runtime_data
import vendor_data

REPOSITORY = 'eladyesh/stock-brain'
API = 'https://api.github.com/repos/' + REPOSITORY
MAX_COMPRESSED = 128 * 1024 * 1024
MAX_DATABASE = 512 * 1024 * 1024
ASSET = 'coverage.sqlite3.gz'
MANIFEST = 'coverage-manifest.json'
PROOF = 'offhost-verification.json'
TAG = re.compile(r'coverage-\d{8}-[0-9]+-[0-9]+\Z')
LOG = logging.getLogger('stock-brain.coverage')


def _download(url, destination, limit):
    # Fixed repository/asset URLs only; callers never accept user-supplied URLs.
    with urlopen(Request(url, headers={'User-Agent': 'StockBrain/1.0 coverage-recovery',
                                      'Accept': 'application/vnd.github+json' if url.startswith(API) else '*/*'}), timeout=45) as response:
        size = 0
        with Path(destination).open('xb') as output:
            while block := response.read(1024 * 1024):
                size += len(block)
                require(size <= limit, 'download exceeds configured size limit')
                output.write(block)
    return size


def latest_release():
    with tempfile.TemporaryDirectory() as d:
        target = Path(d) / 'releases.json'
        _download(API + '/releases?per_page=100', target, 2_000_000)
        releases = json.loads(target.read_text())
    require(isinstance(releases, list), 'invalid release response')
    matches = [r for r in releases if not r.get('draft') and TAG.fullmatch(r.get('tag_name', ''))
               and {ASSET, MANIFEST, PROOF} <= {a.get('name') for a in r.get('assets', [])}]
    require(matches or len(releases) < 100, 'complete coverage release is outside the bounded lookup window')
    return max(matches, key=lambda r: (r['published_at'], r.get('id', 0))) if matches else None


def unpack(compressed, manifest_path, destination):
    """Bounds, hashes, SQLite integrity and schema checked before a generation is used."""
    destination = Path(destination)
    manifest_path, compressed = Path(manifest_path), Path(compressed)
    require(manifest_path.stat().st_size <= 1_000_000, 'manifest too large')
    manifest = json.loads(manifest_path.read_text())
    require(manifest.get('format') == 'stock-brain-coverage-release' and manifest.get('version') == 1, 'unsupported release format')
    item = manifest['compressed']
    require(item['file_name'] == ASSET and 0 < item['size_bytes'] <= MAX_COMPRESSED, 'invalid compressed metadata')
    require(compressed.stat().st_size == item['size_bytes'] and backup._hash(compressed) == item['sha256'], 'compressed digest mismatch')
    raw_manifest = manifest['database_manifest']
    require(raw_manifest['snapshot']['file_name'] == 'coverage.sqlite3', 'unexpected database filename')
    expected_size = raw_manifest['snapshot']['size_bytes']
    require(type(expected_size) is int and 512 <= expected_size <= MAX_DATABASE, 'database exceeds capacity limit')
    require(1 <= raw_manifest['snapshot']['stats']['database_schema_version'] <= SCHEMA_VERSION, 'unsupported database schema')
    require(not destination.exists(), 'refuse to replace an existing generation')
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination.parent) as d:
        raw_path, raw_manifest_path = Path(d) / 'coverage.sqlite3', Path(d) / 'coverage.sqlite3.manifest.json'
        total = 0
        with gzip.open(compressed, 'rb') as source, raw_path.open('xb') as out:
            while block := source.read(1024 * 1024):
                total += len(block)
                require(total <= expected_size, 'decompressed database exceeds manifest size')
                out.write(block)
        require(total == expected_size, 'truncated database')
        raw_manifest_path.write_text(json.dumps(raw_manifest))
        backup.restore(raw_path, raw_manifest_path, destination)
    return manifest


def download_release(release, destination):
    tag = release['tag_name']
    require(TAG.fullmatch(tag) is not None, 'invalid release tag')
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination.parent) as d:
        root = Path(d)
        base = 'https://github.com/' + REPOSITORY + '/releases/download/' + tag + '/'
        _download(base + MANIFEST, root / MANIFEST, 1_000_000)
        require(json.loads((root / MANIFEST).read_text()).get('release_tag') == tag, 'manifest/release mismatch')
        _download(base + ASSET, root / ASSET, MAX_COMPRESSED)
        result = unpack(root / ASSET, root / MANIFEST, destination)
        return result


def package(store, destination, *, release_tag, execution):
    require(TAG.fullmatch(release_tag) is not None, 'invalid release tag')
    out = Path(destination)
    out.mkdir(parents=True, exist_ok=True)
    raw = out / 'coverage.sqlite3'
    result = backup.backup(store.path, raw)
    require(raw.stat().st_size <= MAX_DATABASE, 'database exceeds release capacity; migrate storage before continuing')
    compressed = out / ASSET
    with raw.open('rb') as source, compressed.open('xb') as target:
        with gzip.GzipFile(fileobj=target, mode='wb', mtime=0) as stream:
            shutil.copyfileobj(source, stream)
    require(compressed.stat().st_size <= MAX_COMPRESSED, 'compressed database exceeds release capacity')
    manifest = {'format': 'stock-brain-coverage-release', 'version': 1, 'release_tag': release_tag,
        'created_at': datetime.now(timezone.utc).isoformat(), 'execution': execution,
        'compressed': {'file_name': ASSET, 'size_bytes': compressed.stat().st_size, 'sha256': backup._hash(compressed)},
        'database_manifest': result['manifest'], 'directory': market_directory.directory_status(store),
        'scope': 'Public directory and available dated datasets. Does not establish complete financial or research coverage.'}
    # Internal build paths are irrelevant to recovery and are not published.
    manifest['database_manifest']['source'].pop('path', None)
    (out / MANIFEST).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    with tempfile.TemporaryDirectory() as d:
        restored = Path(d) / 'restored.sqlite3'
        unpack(compressed, out / MANIFEST, restored)
        recovered = CoverageStore(restored)
        recovered_status = market_directory.directory_status(recovered)
        require(all(recovered_status[k] == manifest['directory'][k] for k in
                    ('sources', 'listed_securities', 'instrument_counts', 'linked_issuer_count')), 'cold restore counts/evidence differ')
    return manifest


def build(root, output, *, tag, use_saved_directories=None):
    root, output = Path(root), Path(output)
    output.mkdir(parents=True, exist_ok=True)
    database = output / 'working.sqlite3'
    require(not database.exists(), 'build requires a fresh output directory')
    previous = latest_release()
    if previous:
        download_release(previous, database)
    checkpoint = runtime_data.github_checkpoint()
    store = initialize_coverage(root, checkpoint['files']['desk.json'], database)
    if use_saved_directories:
        sources = Path(use_saved_directories)
        directories = [market_directory.parse_directory((sources / name).read_bytes(), name,
                       retrieved_at=json.loads((sources / (name + '.source.json')).read_text())['retrieved_at']) for name in market_directory.FILES]
    else:
        directories = market_directory.fetch_directories()
    result = market_directory.import_directories(store, directories)
    copy_pilot_prices(store, checkpoint['files']['desk.json'])
    vendor = vendor_data.collect(store)
    execution = {'event': os.environ.get('GITHUB_EVENT_NAME', 'local'), 'run_id': os.environ.get('GITHUB_RUN_ID'),
                 'scheduled_execution_observed': os.environ.get('GITHUB_EVENT_NAME') == 'schedule',
                 'previous_release': previous['tag_name'] if previous else None,
                 'source_commit': os.environ.get('GITHUB_SHA'), 'vendor_collection': vendor}
    manifest = package(store, output / 'release', release_tag=tag, execution=execution)
    return {'import': result, 'vendor_collection': vendor, 'manifest': manifest, 'local_cold_restore': 'pass'}


def copy_pilot_prices(store, snapshot):
    """Carry existing dated public quotes without making a new provider request."""
    for company in snapshot['companies']:
        quote = company.get('quote') or {}
        if quote.get('status') != 'available': continue
        require(quote.get('ticker') == company['ticker'], 'pilot quote identity mismatch')
        require(re.fullmatch('[0-9a-f]{64}', quote.get('source_sha256', '')) is not None, 'pilot quote source hash missing')
        with store._connection(write=True) as db:
            rows = db.execute("SELECT * FROM market_securities WHERE cik=? AND ticker=? AND directory_status='present'",
                              (company['history']['cik'], company['ticker'])).fetchall()
            for row in rows:
                source = {'url': quote['request_url'], 'sha256': quote['source_sha256'], 'retrieved_at': quote['retrieved_at']}
                payload = json.dumps({'data': {'snapshot': quote}, 'review_status': 'provider_snapshot',
                                      'validation': {'as_of_basis': 'last_regular_session_trade'}}, sort_keys=True, ensure_ascii=False)
                sha = hashlib.sha256((payload + json.dumps(source, sort_keys=True)).encode()).hexdigest()
                db.execute('''INSERT OR IGNORE INTO market_observations(listing_key,identity_revision,dataset,provider,
                              retrieved_at,as_of,source_json,payload_json,sha256) VALUES (?,?,?,?,?,?,?,?,?)''',
                           (row['listing_key'], row['identity_revision'], 'prices', quote['provider'], quote['retrieved_at'],
                            quote['trade_at'], json.dumps(source), payload, sha))


def verify_published(tag):
    require(TAG.fullmatch(tag) is not None, 'invalid release tag')
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / 'restored.sqlite3'
        manifest = download_release({'tag_name': tag}, path)
        store = CoverageStore(path)
        status = market_directory.directory_status(store)
        require(status['listed_securities'] == manifest['directory']['listed_securities'], 'off-host restored count differs')
        return {'verification_status': 'pass', 'cold_restore': 'pass', 'release_tag': tag,
                'verified_at': datetime.now(timezone.utc).isoformat(), 'directory': status,
                'execution': manifest['execution'], 'database_sha256': manifest['database_manifest']['snapshot']['sha256']}


class CoverageMirror:
    """Single downloader; generation swap never overwrites a database in use."""
    def __init__(self, app, interval=900):
        self.app, self.interval = app, interval
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.run, name='coverage-mirror', daemon=True)
        self.state = {'mode': 'release_mirror', 'status': 'waiting', 'release_tag': None,
                      'last_checked_at': None, 'last_success_at': None, 'last_error': None}

    def refresh(self):
        now = datetime.now(timezone.utc).isoformat()
        self.state = {**self.state, 'last_checked_at': now}
        try:
            release = latest_release()
            require(release is not None, 'no_complete_coverage_release')
            if release['tag_name'] == self.state['release_tag']:
                self.state = {**self.state, 'status': 'ready', 'last_error': None}
                return
            directory = self.app.store.directory / 'coverage-generations'
            directory.mkdir(exist_ok=True)
            with tempfile.TemporaryDirectory(dir=directory) as temporary:
                staged = Path(temporary) / 'coverage.sqlite3'
                manifest = download_release(release, staged)
                # New unique directory. Leave old readers and their WAL files intact.
                target = Path(tempfile.mkdtemp(prefix=release['tag_name'] + '-', dir=directory)) / 'coverage.sqlite3'
                staged.replace(target)
            store = initialize_coverage(self.app.root, self.app.store.read()['files']['desk.json'], target)
            with self.app.coverage_lock:
                previous_path = self.app.coverage.path
                self.app.coverage = store
                # All HTTP registry reads share this lock. Retain the active and
                # previous generations locally; durable release history is untouched.
                for child in directory.iterdir():
                    if (child.is_dir() and not child.is_symlink() and child.name.startswith('coverage-')
                            and child not in {target.parent, previous_path.parent}):
                        shutil.rmtree(child)
            self.state = {**self.state, 'status': 'ready', 'release_tag': release['tag_name'],
                          'last_success_at': now, 'last_error': None, 'source_created_at': manifest['created_at'],
                          'collection': manifest['execution'].get('vendor_collection'),
                          'scheduled_execution_observed': manifest['execution'].get('scheduled_execution_observed', False)}
            LOG.info('Loaded verified coverage release %s', release['tag_name'])
        except Exception as error:
            # Do not expose provider bodies or credentials through status endpoints.
            self.state = {**self.state, 'status': 'degraded', 'last_error': type(error).__name__}
            LOG.warning('Coverage mirror unavailable (%s); retaining previous generation', type(error).__name__)

    def run(self):
        while not self.stop_event.is_set():
            self.refresh()
            self.stop_event.wait(self.interval)

    def stop(self):
        self.stop_event.set()
        self.thread.join(timeout=5)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['build', 'verify'])
    parser.add_argument('--tag', required=True)
    parser.add_argument('--output', type=Path, default=Path('build/coverage-daily'))
    parser.add_argument('--saved-directories', type=Path)
    args = parser.parse_args(argv)
    if args.command == 'build':
        result = build(Path(__file__).resolve().parents[1], args.output, tag=args.tag, use_saved_directories=args.saved_directories)
    else:
        result = verify_published(args.tag)
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / 'offhost-verification.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False))
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with Path(summary).open('a') as stream:
            stream.write('\n## Daily coverage data\n\n```json\n' + json.dumps(result, ensure_ascii=False, indent=2) + '\n```\n')


if __name__ == '__main__': main()
