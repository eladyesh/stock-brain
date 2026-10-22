#!/usr/bin/env python3
"""Resume bounded ingestion of legitimately acquired SEC bulk ZIPs, offline.

No downloader, network fallback, host rotation, or auto-enabling of SEC access.
Inputs are the SEC submissions/companyfacts archives plus their actual retrieval
timestamps and SHA-256 hashes. ZIP members are read individually, never extracted.
The registry remains source-relative; private filers do not become listed stocks.
"""
from contextlib import ExitStack
from datetime import datetime, timedelta, timezone
import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import time
import zipfile

from coverage_store import CoverageStore, _datetime, _stamp, _json, normalize_cik, require
from coverage_worker import CoverageWorker
import market_directory as directory

URLS = {
    'submissions': 'https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip',
    'companyfacts': 'https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip',
}
MAX_ARCHIVE = 8 * 1024**3
MAX_EXPANDED = 96 * 1024**3
MAX_MEMBER = 64 * 1024**2
# The 2026-10-22 official submissions ZIP contains 995,360 entries (ZIP64
# central directory: 87,678,109 bytes). Import runs on the existing Actions
# runner, never inside the 512 MiB public web process.
MAX_ENTRIES = 1_200_000


def digest_file(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def strict_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, 'duplicate JSON field')
            result[key] = value
        return result
    def nonfinite(_):
        raise ValueError('non-finite JSON number')
    return json.loads(raw, object_pairs_hook=pairs, parse_constant=nonfinite)


class SECArchive:
    def __init__(self, path, kind, *, retrieved_at, sha256, now=None):
        require(kind in URLS, 'unknown SEC archive type')
        self.path, self.kind = Path(path), kind
        self.retrieved_at = _stamp(retrieved_at)
        require(_datetime(retrieved_at) <= _datetime(now or datetime.now(timezone.utc)) + timedelta(minutes=5),
                'archive retrieval time is in the future')
        require(re.fullmatch(r'[0-9a-f]{64}', sha256 or '') is not None, 'expected archive SHA-256 is required')
        require(0 < self.path.stat().st_size <= MAX_ARCHIVE, 'SEC archive exceeds compressed size limit')
        require(digest_file(self.path) == sha256, 'SEC archive SHA-256 mismatch')
        self.sha256 = sha256
        self.archive = zipfile.ZipFile(self.path)
        try:
            self.members, self.issuers = {}, {}
            entries = self.archive.infolist()
            require(0 < len(entries) <= MAX_ENTRIES,
                    f'SEC archive entry count outside bounds: {len(entries)} (limit {MAX_ENTRIES})')
            total = 0
            for entry in entries:
                # SEC includes this non-issuer marker in its real submissions
                # archive. Accept only this exact bounded regular entry, verify
                # its CRC, and never interpret it as a company document.
                if kind == 'submissions' and entry.filename == 'placeholder.txt':
                    require(entry.filename not in self.members, 'duplicate SEC ZIP member')
                    require(not stat.S_ISLNK(entry.external_attr >> 16) and not entry.flag_bits & 1
                            and 0 <= entry.file_size <= 1024, 'invalid SEC archive placeholder')
                    with self.archive.open(entry) as marker:
                        require(len(marker.read(1025)) == entry.file_size, 'invalid SEC archive placeholder length')
                    self.members[entry.filename] = entry
                    continue
                pattern = r'CIK([0-9]{10})(?:-submissions-[0-9]{3,})?\.json' if kind == 'submissions' else r'CIK([0-9]{10})\.json'
                match = re.fullmatch(pattern, entry.filename)
                require(match is not None and int(match[1]) > 0, 'unexpected SEC ZIP member name')
                require(entry.filename not in self.members, 'duplicate SEC ZIP member')
                mode = entry.external_attr >> 16
                require(not stat.S_ISLNK(mode) and not entry.flag_bits & 1, 'encrypted or linked ZIP member')
                require(0 < entry.file_size <= MAX_MEMBER and entry.compress_size > 0,
                        'SEC ZIP member exceeds size limit')
                require(entry.file_size <= entry.compress_size * 1000, 'SEC ZIP compression ratio exceeds limit')
                total += entry.file_size
                require(total <= MAX_EXPANDED, 'SEC ZIP expanded size exceeds limit')
                self.members[entry.filename] = entry
                if entry.filename == f'CIK{match[1]}.json':
                    self.issuers[match[1]] = entry.filename
            require(self.issuers, 'SEC archive contains no issuer documents')
        except Exception:
            self.archive.close()
            raise

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.archive.close()

    def read(self, cik):
        cik = normalize_cik(cik)
        require(cik in self.issuers, 'issuer missing from supplied SEC archive')
        name = self.issuers[cik]
        with self.archive.open(self.members[name]) as stream:
            raw = stream.read(MAX_MEMBER + 1)  # CRC is also verified by ZipFile.
        require(len(raw) == self.members[name].file_size <= MAX_MEMBER, 'SEC ZIP member length mismatch')
        value = strict_json(raw)
        require(isinstance(value, dict) and normalize_cik(value.get('cik')) == cik, 'SEC ZIP issuer identity mismatch')
        url = (f'https://data.sec.gov/submissions/CIK{cik}.json' if self.kind == 'submissions' else
               f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json')
        source = {'url': url, 'retrieved_at': self.retrieved_at, 'sha256': hashlib.sha256(raw).hexdigest(),
                  'acquisition': 'operator_supplied_sec_bulk_archive',
                  'archive': {'url': URLS[self.kind], 'sha256': self.sha256, 'member': name}}
        return value, source


class BulkProvider:
    force_facts = True  # Same-accession XBRL corrections can change between archives.

    def __init__(self, submissions, facts):
        self.sub_archive, self.fact_archive = submissions, facts
        self.cutoff = min(submissions.retrieved_at, facts.retrieved_at)[:10]

    def readiness(self):
        return {'ready': True, 'reason': None, 'provider': 'sec_bulk_offline', 'network_checked': False}

    def submissions(self, cik):
        return self.sub_archive.read(cik)

    def companyfacts(self, cik):
        return self.fact_archive.read(cik)


def run_key(store, submissions, facts=None):
    # A new directory generation rechecks previously unmatched filers too.
    with store._connection() as db:
        row = db.execute('SELECT sources_json FROM market_directory_runs ORDER BY id DESC LIMIT 1').fetchone()
    scope = json.loads(row[0]) if row else {}
    return hashlib.sha256(_json({'submissions': submissions.sha256,
        'submissions_retrieved_at': submissions.retrieved_at,
        'companyfacts': facts.sha256 if facts else None,
        'companyfacts_retrieved_at': facts.retrieved_at if facts else None,
        'directory_sources': scope}).encode()).hexdigest()


def checkpoint(store, key, phase, cursor, report, errors):
    with store._connection(write=True) as db:
        for cik, message in errors:
            db.execute('INSERT OR REPLACE INTO sec_bulk_errors VALUES (?,?,?,?,?)',
                       (key, phase, cik, message[:1000], _stamp(store._now())))
        db.execute('INSERT OR REPLACE INTO sec_bulk_runs VALUES (?,?,?,?,?)',
                   (key, phase, cursor, _json(report), _stamp(store._now())))


def progress(store, key, phase):
    with store._connection() as db:
        row = db.execute('SELECT * FROM sec_bulk_runs WHERE run_key=? AND phase=?', (key, phase)).fetchone()
    return (row['cursor'], json.loads(row['report_json'])) if row else ('', {'scanned': 0, 'imported': 0, 'skipped': 0, 'failed': 0})


def import_issuers(store, archive, *, limit=1000):
    """Match current stock slots to explicit SEC tickers, venues and issuer name.

    Never zip ticker/exchange arrays or assume their positions correspond. An
    association needs independent exact directory venue/symbol/name evidence.
    Replay after a crash is idempotent; a failed issuer is quarantined by CIK.
    """
    require(type(limit) is int and 1 <= limit <= 5000, 'issuer scan limit must be 1..5000')
    require(directory.directory_status(store)['status'] == 'checked', 'a fresh listing directory is required')
    key = run_key(store, archive)
    cursor, report = progress(store, key, 'issuers')
    candidates = sorted(cik for cik in archive.issuers if cik > cursor)
    with store._connection() as db:
        rows = [dict(row) for row in db.execute("SELECT * FROM market_securities WHERE directory_status='present' AND is_test=0")]
    by_ticker = {}
    for row in rows:
        if row['instrument_type'] in directory.EQUITY_TYPES:
            by_ticker.setdefault(directory.sec_symbol(row), []).append(row)
    errors = []
    for cik in candidates[:limit]:
        matches = {}
        report['scanned'] += 1
        try:
            value, source = archive.read(cik)
            name, tickers, venues = value.get('name'), value.get('tickers'), value.get('exchanges')
            require(isinstance(name, str) and name.strip(), 'SEC issuer name is missing')
            require(isinstance(tickers, list) and isinstance(venues, list) and len(tickers) <= 1000 and len(venues) <= 1000,
                    'invalid SEC ticker/exchange arrays')
            require(all(isinstance(item, str) for item in tickers + venues), 'invalid SEC identity field')
            exchanges = {x.upper().replace(' ', '_') for x in venues}
            matches = {row['listing_key']: row for ticker in tickers for row in by_ticker.get(ticker, [])
                       if directory.sec_venue_matches(row['exchange'], exchanges)
                       and directory._name_matches(row['security_name'], name)}
            require(len({(directory.sec_symbol(row), row['exchange']) for row in matches.values()}) == len(matches),
                    'ambiguous directory aliases for one SEC symbol and venue')
            if not matches:
                report['skipped'] += 1
            else:
                require(all(not row['cik'] or row['cik'] == cik for row in matches.values()), 'conflicting directory issuer')
                result = store.import_listings({'fields': ['cik', 'name', 'ticker', 'exchange'],
                    'data': [[cik, name, row['ticker'], row['exchange']] for row in matches.values()]}, source, complete=False)
                if result['applied']:
                    with store._connection(write=True) as db:
                        for row in matches.values():
                            db.execute('''UPDATE market_securities SET cik=?,mapping_basis=?
                                WHERE listing_key=? AND identity_revision=? AND (cik IS NULL OR cik=?)''',
                                (cik, 'SEC submission: equivalent symbol and legal name; SEC venue family and exact directory venue',
                                 row['listing_key'], row['identity_revision'], cik))
                    identity = {'cik': cik, 'name': name, 'tickers': tickers,
                                'exchanges': venues, 'review_status': 'unreviewed'}
                    if store.get_payload(cik, 'sec_bulk_identity') != identity:
                        store.put_payload(cik, 'sec_bulk_identity', identity, source)
                    report['imported'] += 1
                else:
                    report['skipped'] += 1
        except (ValueError, KeyError, TypeError, OSError, zipfile.BadZipFile) as error:
            report['failed'] += 1
            errors.append((cik, str(error)))
        cursor = cik
        # Matched issuers and errors commit immediately. Unmatched private filers
        # can safely replay; avoid one fsync per filer across the whole SEC archive.
        if matches or errors and errors[-1][0] == cik or report['scanned'] % 100 == 0:
            checkpoint(store, key, 'issuers', cursor, report, errors[-1:] if errors and errors[-1][0] == cik else [])
    checkpoint(store, key, 'issuers', cursor, report, [])
    return {**report, 'run_key': key, 'cursor': cursor, 'complete': len(candidates) <= limit,
            'network_requests': 0, 'scope': 'matched current exchange-listed stock slots only'}


def collect_financials(store, submissions, facts, *, root, limit=25):
    require(type(limit) is int and 1 <= limit <= 100, 'financial batch limit must be 1..100')
    require(directory.directory_status(store)['status'] == 'checked', 'a fresh listing directory is required')
    issuer_cursor, _ = progress(store, run_key(store, submissions), 'issuers')
    require(issuer_cursor >= max(submissions.issuers), 'finish this archive issuer scan before collecting financials')
    key = run_key(store, submissions, facts)
    cursor, report = progress(store, key, 'financials')
    with store._connection() as db:
        candidates = [row[0] for row in db.execute('''SELECT DISTINCT cik FROM market_securities
            WHERE cik IS NOT NULL AND cik>? AND directory_status='present' AND is_test=0 ORDER BY cik''', (cursor,))
            if row[0] in submissions.issuers]
    worker = CoverageWorker(store, BulkProvider(submissions, facts), root=root, clock=store._now)
    for cik in candidates[:limit]:
        job = store.enqueue(cik, kind='refresh_company_bulk')
        claimed = store.claim('sec-bulk-' + key[:16], job_id=job['job_id'], lease_seconds=300)
        if claimed is None:
            # Do not advance over another worker or a pending retry.
            return {**report, 'run_key': key, 'cursor': cursor, 'complete': False, 'network_requests': 0,
                    'waiting_for_job': job['job_id']}
        report['scanned'] += 1
        errors = []
        try:
            payloads, outcome = worker.collect(claimed)
            store.commit_job(claimed['job_id'], claimed['lease_owner'], claimed['lease_token'], payloads, result=outcome)
            report['imported'] += 1
        except (ValueError, KeyError, TypeError, OSError, RuntimeError, zipfile.BadZipFile) as error:
            # Preserve independently valid filing metadata without approving the
            # failed financial payload or changing its last processed accession.
            try:
                payloads, outcome = worker.collect(claimed, filings_only=True)
            except (ValueError, KeyError, TypeError, OSError, RuntimeError, zipfile.BadZipFile):
                store.fail(claimed['job_id'], claimed['lease_owner'], claimed['lease_token'], str(error), blocked=True)
            else:
                store.commit_job(claimed['job_id'], claimed['lease_owner'], claimed['lease_token'], payloads,
                                 result={**outcome, 'financial_error': str(error)[:1000]})
            report['failed'] += 1
            errors.append((cik, str(error)))
        cursor = cik
        checkpoint(store, key, 'financials', cursor, report, errors)
    return {**report, 'run_key': key, 'cursor': cursor, 'complete': len(candidates) <= limit, 'network_requests': 0}


def open_manifest(path, stack, *, require_facts=True):
    path = Path(path)
    require(path.stat().st_size <= 100_000, 'acquisition manifest is too large')
    manifest = strict_json(path.read_bytes())
    require(isinstance(manifest, dict) and manifest.get('format') == 'stock-brain-sec-bulk-v1', 'invalid acquisition manifest')
    archives = {}
    for kind in ('submissions', 'companyfacts') if require_facts else ('submissions',):
        entry = manifest[kind]
        require(entry['url'] == URLS[kind], 'unrecognized SEC archive source')
        archives[kind] = stack.enter_context(SECArchive(path.parent / entry['file'], kind,
            retrieved_at=entry['retrieved_at'], sha256=entry['sha256']))
    return archives


def ingest_manifest(store, path, *, root, issuer_limit=5000, financial_limit=100,
                    complete=False, max_seconds=5400, on_progress=None):
    require(type(max_seconds) is int and 1 <= max_seconds <= 10800, 'invalid bulk time budget')
    deadline = time.monotonic() + max_seconds
    with ExitStack() as stack:
        archives = open_manifest(path, stack)
        stopped = None
        financials = None
        while True:
            identities = import_issuers(store, archives['submissions'], limit=issuer_limit)
            if on_progress:
                on_progress({'phase': 'issuers', **identities})
            if identities['complete'] or not complete:
                break
            if time.monotonic() >= deadline:
                stopped = 'time_budget'
                break
        if identities['complete']:
            while True:
                # Keep room for a batch, release metadata and the next daily check.
                # No versions are deleted and the release cap is unchanged.
                from coverage_storage import MAX_DATABASE
                with store._connection() as db:
                    used = (db.execute('PRAGMA page_count').fetchone()[0] -
                            db.execute('PRAGMA freelist_count').fetchone()[0]) * db.execute('PRAGMA page_size').fetchone()[0]
                if used > MAX_DATABASE - 64 * 1024**2:
                    stopped = 'storage_headroom'
                    break
                if time.monotonic() >= deadline:
                    stopped = 'time_budget'
                    break
                financials = collect_financials(store, archives['submissions'], archives['companyfacts'],
                    root=root, limit=financial_limit)
                if on_progress:
                    on_progress({'phase': 'financials', **financials})
                if financials['complete'] or not complete or financials.get('waiting_for_job'):
                    break
        failed = identities['failed'] + (financials or {}).get('failed', 0)
        return {'status': ('completed_with_errors' if failed else 'completed') if financials and financials['complete'] else 'in_progress',
                'issuers': identities, 'financials': financials, 'network_requests': 0,
                'failed': failed, 'stopped_reason': stopped,
                'archives': {kind: {'sha256': value.sha256, 'retrieved_at': value.retrieved_at,
                    'issuers': len(value.issuers)} for kind, value in archives.items()}}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=['inspect', 'issuers', 'financials', 'cycle'])
    parser.add_argument('--manifest', type=Path, required=True, help='Local acquisition manifest; see docs/SEC_BULK.md')
    parser.add_argument('--db', type=Path)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--limit', type=int)
    args = parser.parse_args(argv)
    if args.phase != 'inspect' and not args.db:
        parser.error('--db is required for ingestion')
    try:
        if args.phase == 'cycle':
            report = ingest_manifest(CoverageStore(args.db), args.manifest, root=args.root,
                                     financial_limit=args.limit if args.limit is not None else 100)
            print(json.dumps(report, ensure_ascii=False))
            return 1 if report['failed'] else 0
        with ExitStack() as stack:
            archives = open_manifest(args.manifest, stack, require_facts=args.phase != 'issuers')
            if args.phase == 'inspect':
                report = {'network_requests': 0, 'archives': {kind: {'issuers': len(archive.issuers),
                    'members': len(archive.members), 'sha256': archive.sha256, 'retrieved_at': archive.retrieved_at}
                    for kind, archive in archives.items()}, 'integrity': 'archive hash and inventory verified; members checked when read'}
            else:
                store = CoverageStore(args.db)
                report = (import_issuers(store, archives['submissions'], limit=args.limit if args.limit is not None else 1000) if args.phase == 'issuers' else
                    collect_financials(store, archives['submissions'], archives['companyfacts'], root=args.root, limit=args.limit if args.limit is not None else 25))
            print(json.dumps(report, ensure_ascii=False))
            return 1 if report.get('failed') else 0
    except (ValueError, KeyError, TypeError, OSError, zipfile.BadZipFile) as error:
        print(json.dumps({'error': str(error), 'network_requests': 0, 'prior_data_retained': True}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
