"""SQLite registry, versioned company data and leased work for coverage expansion.

This store contains only the universe actually seeded or imported. A complete
listing snapshot is complete relative to its stated source, not proof of all
U.S. securities, collected financials or reviewed research. No network is used.
Keep this database on a durable single-host volume and back it up separately
from the small desk's four-file GitHub checkpoint.
"""
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
from urllib.parse import urlsplit
import uuid


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = 2
MAX_RETRY_SECONDS = 24 * 60 * 60
ACTIVE_JOB_STATUSES = ('queued', 'running', 'retry')
JOB_STATUSES = (*ACTIVE_JOB_STATUSES, 'completed', 'failed', 'blocked')
KIND = re.compile(r'[a-z][a-z0-9_]{0,63}\Z')
TICKER = re.compile(r'[A-Z0-9][A-Z0-9.\-^/+=]{0,31}\Z')
SCOPE = ('Imported or seeded issuer/listing registry only. Source-relative snapshot completeness '
         'does not establish all U.S.-listed securities, collected data, or reviewed research.')


class LeaseLostError(ValueError):
    """The job no longer belongs to this unexpired worker lease."""


def require(condition, message):
    if not condition:
        raise ValueError(message)


def normalize_cik(value):
    require(type(value) in (str, int), 'CIK must be a positive integer or digit string')
    text = str(value).strip()
    require(bool(re.fullmatch(r'\d{1,10}', text, flags=re.ASCII)) and int(text) > 0,
            'CIK must contain 1 to 10 digits and be positive')
    return text.zfill(10)


def _text(value, label, maximum=500):
    require(isinstance(value, str) and bool(value.strip()), label + ' is required')
    require(len(value) <= maximum and not any(ord(c) < 32 for c in value), label + ' is invalid')
    return value.strip()


def _ticker(value):
    value = _text(value, 'ticker', 32).upper()
    require(bool(TICKER.fullmatch(value)), 'ticker has unsupported characters')
    return value


def _exchange(value):
    if value is None:
        return ''
    value = _text(value, 'exchange', 80).upper()
    # Preserve unknown venues and OTC records; never silently filter the source.
    require(bool(re.fullmatch(r'[A-Z0-9][A-Z0-9 ._/-]*', value)), 'exchange has unsupported characters')
    value = re.sub(r'[\s_-]+', '_', value)
    return {'NASDAQ_STOCK_MARKET': 'NASDAQ', 'NYSE_AMEX': 'NYSE_AMERICAN'}.get(value, value)


def _datetime(value):
    if isinstance(value, str):
        try:
            value = datetime.fromisoformat(value.replace('Z', '+00:00'))
        except ValueError as error:
            raise ValueError('timestamp must be an ISO datetime with timezone') from error
    require(isinstance(value, datetime) and value.tzinfo is not None and value.utcoffset() is not None,
            'timestamp must be an ISO datetime with timezone')
    return value.astimezone(timezone.utc)


def _stamp(value):
    return _datetime(value).isoformat(timespec='microseconds')


def _json(value):
    try:
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)
    except (TypeError, ValueError) as error:
        raise ValueError('value must be finite JSON data') from error


def _hash(encoded):
    return hashlib.sha256(encoded.encode()).hexdigest()


def _kind(value):
    require(isinstance(value, str) and bool(KIND.fullmatch(value)), 'invalid payload or job kind')
    return value


def _error(value):
    # A provider's long or multiline error must not prevent recording its failure.
    return ' '.join(str(value).split())[:8000] or 'Unspecified source or job failure'


def _source(value, now):
    require(isinstance(value, dict), 'source evidence is required')
    url = value.get('url')
    require(isinstance(url, str), 'source.url is required')
    parsed = urlsplit(url)
    require(parsed.scheme == 'https' and parsed.hostname and not parsed.username and not parsed.password,
            'source.url must be public HTTPS without credentials')
    sha = value.get('sha256')
    require(isinstance(sha, str) and bool(re.fullmatch(r'[0-9a-fA-F]{64}', sha)), 'source.sha256 must be SHA-256 hex')
    retrieved = _datetime(value.get('retrieved_at'))
    require(retrieved <= now + timedelta(minutes=5), 'source retrieval timestamp is in the future')
    result = {**value, 'url': url, 'sha256': sha.lower(), 'retrieved_at': _stamp(retrieved)}
    _json(result)
    return result


def _listing_rows(payload):
    require(isinstance(payload, dict), 'listing payload must be an object')
    fields, data = payload.get('fields'), payload.get('data')
    require(isinstance(fields, list) and all(isinstance(f, str) for f in fields) and len(set(fields)) == len(fields),
            'listing fields must be unique strings')
    require({'cik', 'name', 'ticker', 'exchange'} <= set(fields), 'listing payload lacks SEC exchange-ticker fields')
    require(isinstance(data, list), 'listing data must be an array')
    require(len(data) <= 250_000, 'listing snapshot exceeds the supported row limit')
    rows, identities, names = [], {}, {}
    for index, values in enumerate(data):
        require(isinstance(values, list) and len(values) == len(fields), f'listing row {index} does not match fields')
        row = dict(zip(fields, values))
        cik, ticker = normalize_cik(row['cik']), _ticker(row['ticker'])
        exchange, name = _exchange(row['exchange']), ' '.join(_text(row['name'], 'company name').split())
        key = (ticker, exchange)
        require(key not in identities, f'duplicate or ambiguous listing {ticker}/{exchange}')
        require(cik not in names or names[cik] == name, f'conflicting names for issuer {cik}')
        identities[key], names[cik] = cik, name
        rows.append({'cik': cik, 'ticker': ticker, 'exchange': exchange, 'company_name': name,
                     'raw_exchange': row['exchange']})
    return rows


MIGRATIONS = {1: [
    '''CREATE TABLE schema_migrations (version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL)''',
    '''CREATE TABLE issuers (
        cik TEXT PRIMARY KEY CHECK(length(cik)=10 AND cik NOT GLOB '*[^0-9]*'),
        company_name TEXT NOT NULL, metadata_json TEXT NOT NULL DEFAULT '{}',
        created_at TEXT NOT NULL, updated_at TEXT NOT NULL)''',
    '''CREATE TABLE listing_snapshots (
        id INTEGER PRIMARY KEY, source_url TEXT NOT NULL, source_sha256 TEXT NOT NULL,
        retrieved_at TEXT NOT NULL, imported_at TEXT NOT NULL, complete INTEGER NOT NULL CHECK(complete IN (0,1)),
        is_seed INTEGER NOT NULL CHECK(is_seed IN (0,1)), applied INTEGER NOT NULL CHECK(applied IN (0,1)),
        payload_sha256 TEXT NOT NULL, payload_json TEXT NOT NULL, row_count INTEGER NOT NULL,
        issuer_count INTEGER NOT NULL, summary_json TEXT NOT NULL DEFAULT '{}',
        UNIQUE(source_url,source_sha256,retrieved_at,complete,is_seed,payload_sha256))''',
    '''CREATE INDEX listing_snapshots_source ON listing_snapshots(source_url,retrieved_at DESC)''',
    '''CREATE TABLE listings (
        id INTEGER PRIMARY KEY, cik TEXT NOT NULL REFERENCES issuers(cik), ticker TEXT NOT NULL,
        exchange TEXT NOT NULL, raw_exchange_json TEXT NOT NULL, status TEXT NOT NULL CHECK(status IN ('active','inactive')),
        first_seen_at TEXT NOT NULL, last_seen_at TEXT NOT NULL, inactivated_at TEXT,
        first_snapshot_id INTEGER NOT NULL REFERENCES listing_snapshots(id),
        last_snapshot_id INTEGER NOT NULL REFERENCES listing_snapshots(id),
        UNIQUE(cik,ticker,exchange))''',
    '''CREATE UNIQUE INDEX listings_active_identity ON listings(ticker,exchange) WHERE status='active' ''',
    '''CREATE INDEX listings_issuer ON listings(cik,status,ticker)''',
    '''CREATE INDEX listings_ticker ON listings(ticker,status)''',
    '''CREATE TABLE listing_events (
        id INTEGER PRIMARY KEY, listing_id INTEGER NOT NULL REFERENCES listings(id),
        snapshot_id INTEGER NOT NULL REFERENCES listing_snapshots(id), event TEXT NOT NULL,
        observed_at TEXT NOT NULL, details_json TEXT NOT NULL)''',
    '''CREATE TABLE company_payloads (
        id INTEGER PRIMARY KEY, cik TEXT NOT NULL REFERENCES issuers(cik), kind TEXT NOT NULL,
        version INTEGER NOT NULL, sha256 TEXT NOT NULL, value_json TEXT NOT NULL,
        stored_at TEXT NOT NULL, source_url TEXT, source_sha256 TEXT, source_retrieved_at TEXT,
        source_json TEXT, UNIQUE(cik,kind,version))''',
    '''CREATE INDEX company_payloads_latest ON company_payloads(cik,kind,version DESC)''',
    '''CREATE TABLE jobs (
        id INTEGER PRIMARY KEY, cik TEXT NOT NULL REFERENCES issuers(cik), kind TEXT NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('queued','running','retry','completed','failed','blocked')),
        attempts INTEGER NOT NULL DEFAULT 0, max_attempts INTEGER NOT NULL DEFAULT 5,
        available_at TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
        lease_owner TEXT, lease_token TEXT, lease_expires_at TEXT, finished_at TEXT,
        error TEXT, result_json TEXT)''',
    '''CREATE UNIQUE INDEX jobs_active_identity ON jobs(cik,kind) WHERE status IN ('queued','running','retry')''',
    '''CREATE INDEX jobs_claim ON jobs(status,available_at,id)''',
    '''CREATE INDEX jobs_issuer ON jobs(cik,kind,id DESC)''',
    '''CREATE TABLE job_events (
        id INTEGER PRIMARY KEY, job_id INTEGER NOT NULL REFERENCES jobs(id), event TEXT NOT NULL,
        observed_at TEXT NOT NULL, worker_id TEXT, details_json TEXT NOT NULL)''',
], 2: [
    '''CREATE INDEX issuers_name ON issuers(company_name COLLATE NOCASE,cik)''',
    '''CREATE TABLE source_limits (
        source TEXT PRIMARY KEY, next_request_at TEXT, blocked_until TEXT, error TEXT,
        interval_seconds REAL NOT NULL DEFAULT 0.25, updated_at TEXT NOT NULL)''',
    '''CREATE TABLE source_events (
        id INTEGER PRIMARY KEY, source TEXT NOT NULL REFERENCES source_limits(source),
        event TEXT NOT NULL, observed_at TEXT NOT NULL, details_json TEXT NOT NULL)''',
]}


class CoverageStore:
    def __init__(self, path=None, *, clock=None):
        self.path = Path(path or os.environ.get('STOCK_BRAIN_COVERAGE_DB') or ROOT / 'build/coverage.sqlite3')
        require(str(self.path) != ':memory:', 'use a filesystem path for the durable coverage store')
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.clock = clock or (lambda: datetime.now(timezone.utc))
        self._migrate()

    def _now(self):
        return _datetime(self.clock())

    @contextmanager
    def _connection(self, write=False):
        db = sqlite3.connect(self.path, timeout=30, isolation_level=None)
        db.row_factory = sqlite3.Row
        db.execute('PRAGMA foreign_keys=ON')
        db.execute('PRAGMA busy_timeout=30000')
        try:
            db.execute('BEGIN IMMEDIATE' if write else 'BEGIN')
            yield db
            db.commit()
        except BaseException:
            db.rollback()
            raise
        finally:
            db.close()

    def _migrate(self):
        db = sqlite3.connect(self.path, timeout=30)
        try:
            db.execute('PRAGMA journal_mode=WAL')
        finally:
            db.close()
        with self._connection(write=True) as db:
            current = db.execute('PRAGMA user_version').fetchone()[0]
            require(current <= SCHEMA_VERSION, 'coverage database schema is newer than this application')
            for version in range(current + 1, SCHEMA_VERSION + 1):
                for statement in MIGRATIONS[version]:
                    db.execute(statement)
                db.execute('INSERT INTO schema_migrations VALUES (?,?)', (version, _stamp(self._now())))
                db.execute(f'PRAGMA user_version={version}')

    @staticmethod
    def _issuer_exists(db, cik):
        require(db.execute('SELECT 1 FROM issuers WHERE cik=?', (cik,)).fetchone() is not None,
                'issuer is not registered: ' + cik)

    def seed_companies(self, companies):
        """Register local pilot identities without pretending to retrieve a live listing feed."""
        require(isinstance(companies, list), 'seed companies must be a list')
        payload = {'fields': ['cik', 'name', 'ticker', 'exchange'], 'data': [
            [c.get('cik'), c.get('company_name'), c.get('ticker'), c.get('exchange')]
            for c in companies if isinstance(c, dict)]}
        require(len(payload['data']) == len(companies), 'seed company must be an object')
        rows = _listing_rows(payload)
        encoded, now = _json(companies), _stamp(self._now())
        sha = _hash(encoded)
        with self._connection(write=True) as db:
            old = db.execute('SELECT summary_json FROM listing_snapshots WHERE is_seed=1 AND payload_sha256=? LIMIT 1', (sha,)).fetchone()
            if old:
                return {**json.loads(old['summary_json']), 'duplicate': True}
            snapshot = db.execute('''INSERT INTO listing_snapshots
                (source_url,source_sha256,retrieved_at,imported_at,complete,is_seed,applied,payload_sha256,payload_json,row_count,issuer_count)
                VALUES (?,?,?,?,0,1,1,?,?,?,?)''',
                ('repository:config/universe.json', sha, now, now, sha, encoded, len(rows), len({r['cik'] for r in rows}))).lastrowid
            summary = {'snapshot_id': snapshot, 'source_kind': 'repository_seed', 'complete': False, 'applied': True,
                       'rows': len(rows), 'issuers': len({r['cik'] for r in rows}), 'added_issuers': 0,
                       'added_listings': 0, 'reactivated_listings': 0, 'inactivated_listings': 0, 'duplicate': False}
            for original, row in zip(companies, rows):
                issuer = db.execute('SELECT metadata_json FROM issuers WHERE cik=?', (row['cik'],)).fetchone()
                if not issuer:
                    db.execute('INSERT INTO issuers VALUES (?,?,?,?,?)',
                               (row['cik'], row['company_name'], _json({'seed': original}), now, now))
                    summary['added_issuers'] += 1
                else:
                    metadata = json.loads(issuer['metadata_json'])
                    metadata['seed'] = original
                    db.execute('UPDATE issuers SET metadata_json=? WHERE cik=?', (_json(metadata), row['cik']))
                existing = db.execute('SELECT id FROM listings WHERE cik=? AND ticker=? AND exchange=?',
                                      (row['cik'], row['ticker'], row['exchange'])).fetchone()
                if not existing:
                    conflict = db.execute("SELECT cik FROM listings WHERE ticker=? AND exchange=? AND status='active'",
                                          (row['ticker'], row['exchange'])).fetchone()
                    require(not conflict, 'seed listing conflicts with an existing active issuer')
                    self._insert_listing(db, row, snapshot, now)
                    summary['added_listings'] += 1
            db.execute('UPDATE listing_snapshots SET summary_json=? WHERE id=?', (_json(summary), snapshot))
            return summary

    @staticmethod
    def _insert_listing(db, row, snapshot, observed_at):
        listing = db.execute('''INSERT INTO listings
            (cik,ticker,exchange,raw_exchange_json,status,first_seen_at,last_seen_at,first_snapshot_id,last_snapshot_id)
            VALUES (?,?,?,?,'active',?,?,?,?)''',
            (row['cik'], row['ticker'], row['exchange'], _json(row['raw_exchange']), observed_at, observed_at, snapshot, snapshot)).lastrowid
        db.execute('INSERT INTO listing_events(listing_id,snapshot_id,event,observed_at,details_json) VALUES (?,?,?,?,?)',
                   (listing, snapshot, 'added', observed_at, _json({'cik': row['cik'], 'ticker': row['ticker'], 'exchange': row['exchange']})))
        return listing

    def import_listings(self, payload, source, complete=False):
        """Atomically import a validated SEC fields/data snapshot, retaining every venue.

        Absence retires listings only with explicit complete=True, and only for
        listings previously observed from this same URL. Repository seeds and
        other source scopes are never silently removed by a different source.
        An older snapshot is retained for audit without changing current state.
        """
        require(type(complete) is bool, 'complete must be an explicit boolean')
        rows = _listing_rows(payload)
        require(rows or not complete, 'an empty snapshot cannot establish complete listing coverage')
        now = self._now()
        evidence = _source(source, now)
        encoded, imported_at = _json(payload), _stamp(now)
        payload_sha, observed_at = _hash(encoded), evidence['retrieved_at']
        with self._connection(write=True) as db:
            old = db.execute('''SELECT summary_json FROM listing_snapshots WHERE source_url=? AND source_sha256=?
                AND retrieved_at=? AND complete=? AND is_seed=0 AND payload_sha256=?''',
                (evidence['url'], evidence['sha256'], observed_at, int(complete), payload_sha)).fetchone()
            if old:
                return {**json.loads(old['summary_json']), 'duplicate': True}
            latest = db.execute('SELECT MAX(retrieved_at) FROM listing_snapshots WHERE source_url=? AND is_seed=0 AND applied=1',
                                (evidence['url'],)).fetchone()[0]
            apply = not latest or observed_at >= latest
            snapshot = db.execute('''INSERT INTO listing_snapshots
                (source_url,source_sha256,retrieved_at,imported_at,complete,is_seed,applied,payload_sha256,payload_json,row_count,issuer_count)
                VALUES (?,?,?,?,?,0,?,?,?,?,?)''',
                (evidence['url'], evidence['sha256'], observed_at, imported_at, int(complete), int(apply), payload_sha,
                 encoded, len(rows), len({r['cik'] for r in rows}))).lastrowid
            summary = {'snapshot_id': snapshot, 'source_kind': 'import', 'complete': complete, 'applied': apply,
                       'rows': len(rows), 'issuers': len({r['cik'] for r in rows}), 'added_issuers': 0,
                       'added_listings': 0, 'reactivated_listings': 0, 'inactivated_listings': 0, 'duplicate': False,
                       'source': evidence}
            if not apply:
                summary['reason'] = 'older_snapshot_retained_for_audit'
                db.execute('UPDATE listing_snapshots SET summary_json=? WHERE id=?', (_json(summary), snapshot))
                return summary
            identities = {(r['cik'], r['ticker'], r['exchange']) for r in rows}
            if complete:
                current = db.execute('''SELECT l.* FROM listings l JOIN listing_snapshots s ON s.id=l.last_snapshot_id
                    WHERE l.status='active' AND s.source_url=? AND s.is_seed=0''', (evidence['url'],)).fetchall()
                for listing in current:
                    if (listing['cik'], listing['ticker'], listing['exchange']) not in identities:
                        db.execute("UPDATE listings SET status='inactive',inactivated_at=?,last_snapshot_id=? WHERE id=?",
                                   (observed_at, snapshot, listing['id']))
                        db.execute('INSERT INTO listing_events(listing_id,snapshot_id,event,observed_at,details_json) VALUES (?,?,?,?,?)',
                                   (listing['id'], snapshot, 'absent_from_complete_snapshot', observed_at,
                                    _json({'last_seen_at': listing['last_seen_at'], 'source_url': evidence['url']})))
                        summary['inactivated_listings'] += 1
            for row in rows:
                issuer = db.execute('SELECT cik FROM issuers WHERE cik=?', (row['cik'],)).fetchone()
                if not issuer:
                    db.execute('INSERT INTO issuers VALUES (?,?,?,?,?)', (row['cik'], row['company_name'], '{}', imported_at, imported_at))
                    summary['added_issuers'] += 1
                else:
                    db.execute('UPDATE issuers SET company_name=?,updated_at=? WHERE cik=?', (row['company_name'], imported_at, row['cik']))
                conflict = db.execute("SELECT cik FROM listings WHERE ticker=? AND exchange=? AND status='active' AND cik<>?",
                                      (row['ticker'], row['exchange'], row['cik'])).fetchone()
                require(not conflict, 'listing identity conflicts with another active issuer; a partial or different-source snapshot cannot resolve this')
                listing = db.execute('SELECT * FROM listings WHERE cik=? AND ticker=? AND exchange=?',
                                     (row['cik'], row['ticker'], row['exchange'])).fetchone()
                if not listing:
                    self._insert_listing(db, row, snapshot, observed_at)
                    summary['added_listings'] += 1
                else:
                    if listing['status'] == 'inactive':
                        db.execute('INSERT INTO listing_events(listing_id,snapshot_id,event,observed_at,details_json) VALUES (?,?,?,?,?)',
                                   (listing['id'], snapshot, 'reactivated', observed_at, '{}'))
                        summary['reactivated_listings'] += 1
                    db.execute("""UPDATE listings SET status='active',last_seen_at=?,inactivated_at=NULL,
                        last_snapshot_id=?,raw_exchange_json=? WHERE id=?""",
                        (observed_at, snapshot, _json(row['raw_exchange']), listing['id']))
            db.execute('UPDATE listing_snapshots SET summary_json=? WHERE id=?', (_json(summary), snapshot))
            return summary

    @staticmethod
    def _records(db, rows, preferred_ticker=None):
        if not rows:
            return []
        by_cik = {r['cik']: {'cik': r['cik'], 'company_id': 'company-cik-' + r['cik'], 'company_name': r['company_name'],
                            'created_at': r['created_at'], 'updated_at': r['updated_at'],
                            'metadata': json.loads(r['metadata_json']), 'listings': [], 'payloads': {}} for r in rows}
        placeholders = ','.join('?' for _ in by_cik)
        for row in db.execute(f'''SELECT l.*,s.source_url,s.source_sha256,s.retrieved_at,s.is_seed
            FROM listings l JOIN listing_snapshots s ON s.id=l.last_snapshot_id WHERE cik IN ({placeholders})
            ORDER BY CASE l.status WHEN 'active' THEN 0 ELSE 1 END,l.ticker,l.exchange''', list(by_cik)):
            by_cik[row['cik']]['listings'].append({'id': row['id'], 'ticker': row['ticker'], 'exchange': row['exchange'] or None,
                'status': row['status'], 'first_seen_at': row['first_seen_at'], 'last_seen_at': row['last_seen_at'],
                'inactivated_at': row['inactivated_at'], 'source_snapshot_id': row['last_snapshot_id'],
                'source_kind': 'repository_seed' if row['is_seed'] else 'import',
                'source': {'url': row['source_url'], 'sha256': row['source_sha256'], 'retrieved_at': row['retrieved_at']}})
        for row in db.execute(f'''SELECT p.cik,p.kind,p.version,p.sha256,p.stored_at,p.source_json
            FROM company_payloads p WHERE p.cik IN ({placeholders})
            AND p.version=(SELECT MAX(p2.version) FROM company_payloads p2 WHERE p2.cik=p.cik AND p2.kind=p.kind)''', list(by_cik)):
            by_cik[row['cik']]['payloads'][row['kind']] = {'version': row['version'], 'sha256': row['sha256'],
                'stored_at': row['stored_at'], 'source': json.loads(row['source_json']) if row['source_json'] else None}
        for record in by_cik.values():
            active = [l for l in record['listings'] if l['status'] == 'active']
            candidates = active or record['listings']
            preferred = next((l for l in candidates if l['ticker'] == preferred_ticker), None)
            primary = preferred or (candidates[0] if candidates else {})
            record.update(ticker=primary.get('ticker'), exchange=primary.get('exchange'), status='listed' if active else 'inactive')
        return list(by_cik.values())

    def list_companies(self, query='', limit=50, offset=0):
        require(isinstance(query, str) and len(query) <= 200, 'query must be at most 200 characters')
        require(type(limit) is int and 1 <= limit <= 500, 'limit must be 1..500')
        require(type(offset) is int and 0 <= offset <= 2_147_483_647, 'offset must be a nonnegative integer')
        query = query.strip()
        escaped = query.replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')
        pattern = '%' + escaped + '%'
        where = '''WHERE i.company_name LIKE ? ESCAPE '\\' OR i.cik LIKE ? ESCAPE '\\'
            OR EXISTS(SELECT 1 FROM listings l WHERE l.cik=i.cik AND l.ticker LIKE ? ESCAPE '\\')''' if query else ''
        args = [pattern] * 3 if query else []
        with self._connection() as db:
            total = db.execute('SELECT COUNT(*) FROM issuers i ' + where, args).fetchone()[0]
            rows = db.execute('SELECT i.* FROM issuers i ' + where + ' ORDER BY i.company_name COLLATE NOCASE,i.cik LIMIT ? OFFSET ?',
                              [*args, limit, offset]).fetchall()
            return {'items': self._records(db, rows), 'total': total, 'limit': limit, 'offset': offset}

    def company(self, cik_or_ticker):
        require(type(cik_or_ticker) in (str, int), 'company identity must be a CIK or ticker')
        identity = str(cik_or_ticker).strip()
        preferred = None
        with self._connection() as db:
            if re.fullmatch(r'\d{1,10}', identity, flags=re.ASCII):
                rows = db.execute('SELECT * FROM issuers WHERE cik=?', (normalize_cik(identity),)).fetchall()
            else:
                preferred = _ticker(identity)
                candidates = db.execute('SELECT cik,status FROM listings WHERE ticker=?', (preferred,)).fetchall()
                active = {r['cik'] for r in candidates if r['status'] == 'active'}
                identities = active or {r['cik'] for r in candidates}
                require(len(identities) <= 1, 'ticker is ambiguous; use the issuer CIK')
                rows = db.execute('SELECT * FROM issuers WHERE cik=?', (next(iter(identities)),)).fetchall() if identities else []
            return self._records(db, rows, preferred)[0] if rows else None

    def _prepare_payload(self, kind, value, source, now):
        _kind(kind)
        require(isinstance(value, dict), 'company payload must be a JSON object')
        encoded = _json(value)
        require(len(encoded.encode()) <= 64 * 1024 * 1024, 'company payload exceeds 64 MiB')
        evidence = _source(source, now) if source is not None else None
        return kind, encoded, _hash(encoded), evidence

    @staticmethod
    def _put_payload(db, cik, prepared, now):
        kind, encoded, sha, evidence = prepared
        source_json = _json(evidence) if evidence is not None else None
        old = db.execute('SELECT version,sha256,source_json FROM company_payloads WHERE cik=? AND kind=? ORDER BY version DESC LIMIT 1',
                         (cik, kind)).fetchone()
        if old and old['sha256'] == sha and old['source_json'] == source_json:
            return sha
        db.execute('''INSERT INTO company_payloads
            (cik,kind,version,sha256,value_json,stored_at,source_url,source_sha256,source_retrieved_at,source_json)
            VALUES (?,?,?,?,?,?,?,?,?,?)''',
            (cik, kind, old['version'] + 1 if old else 1, sha, encoded, now,
             evidence['url'] if evidence else None, evidence['sha256'] if evidence else None,
             evidence['retrieved_at'] if evidence else None, source_json))
        return sha

    def put_payload(self, cik, kind, value, source=None):
        cik, now = normalize_cik(cik), self._now()
        prepared = self._prepare_payload(kind, value, source, now)
        with self._connection(write=True) as db:
            self._issuer_exists(db, cik)
            return self._put_payload(db, cik, prepared, _stamp(now))

    def put_payload_if_current(self, cik, kind, value, expected_sha256, source=None, *, expected_version=None):
        """Publish only if the current payload still matches the caller's read.

        Return the new content hash on success, or None without any mutation on
        conflict. expected_sha256=None requires an absent payload. Always pass
        expected_version from get_payload_record when replacing an existing
        payload: source evidence can change while the content hash stays equal.
        """
        cik = normalize_cik(cik)
        require(expected_sha256 is None or isinstance(expected_sha256, str)
                and bool(re.fullmatch(r'[0-9a-fA-F]{64}', expected_sha256)),
                'expected_sha256 must be SHA-256 hex or None for an absent payload')
        require(expected_version is None or type(expected_version) is int and expected_version >= 1,
                'expected_version must be a positive integer or None')
        require(expected_sha256 is not None or expected_version is None,
                'an absent payload cannot have an expected version')
        expected_sha256 = expected_sha256.lower() if expected_sha256 is not None else None
        prepared = self._prepare_payload(kind, value, source, self._now())
        with self._connection(write=True) as db:
            self._issuer_exists(db, cik)
            current = db.execute('''SELECT sha256,version FROM company_payloads WHERE cik=? AND kind=?
                                    ORDER BY version DESC LIMIT 1''', (cik, kind)).fetchone()
            current_sha = current['sha256'] if current else None
            if current_sha != expected_sha256 or expected_version is not None and current['version'] != expected_version:
                return None
            return self._put_payload(db, cik, prepared, _stamp(self._now()))

    def get_payload_record(self, cik, kind):
        """Read one payload and its CAS metadata together from a single snapshot."""
        cik, kind = normalize_cik(cik), _kind(kind)
        with self._connection() as db:
            row = db.execute('''SELECT value_json,version,sha256,stored_at,source_json FROM company_payloads
                                WHERE cik=? AND kind=? ORDER BY version DESC LIMIT 1''', (cik, kind)).fetchone()
            if not row:
                return None
            return {'value': json.loads(row['value_json']),
                    'metadata': {'version': row['version'], 'sha256': row['sha256'], 'stored_at': row['stored_at'],
                                 'source': json.loads(row['source_json']) if row['source_json'] else None}}

    def get_payload(self, cik, kind):
        cik, kind = normalize_cik(cik), _kind(kind)
        with self._connection() as db:
            row = db.execute('SELECT value_json FROM company_payloads WHERE cik=? AND kind=? ORDER BY version DESC LIMIT 1', (cik, kind)).fetchone()
            return json.loads(row['value_json']) if row else None

    @staticmethod
    def _job(row):
        if not row:
            return None
        result = dict(row)
        result['job_id'] = result['id']
        result['result'] = json.loads(result.pop('result_json')) if result['result_json'] else None
        result.pop('result_json', None)
        return result

    @staticmethod
    def _event(db, job_id, event, now, worker_id=None, details=None):
        db.execute('INSERT INTO job_events(job_id,event,observed_at,worker_id,details_json) VALUES (?,?,?,?,?)',
                   (job_id, event, now, worker_id, _json(details or {})))

    def enqueue(self, cik, kind='refresh_company', available_at=None):
        cik, kind = normalize_cik(cik), _kind(kind)
        now = _stamp(self._now())
        available = _stamp(available_at) if available_at is not None else now
        with self._connection(write=True) as db:
            self._issuer_exists(db, cik)
            old = db.execute("SELECT * FROM jobs WHERE cik=? AND kind=? AND status IN ('queued','running','retry')", (cik, kind)).fetchone()
            if old:
                return self._job(old)
            job_id = db.execute('''INSERT INTO jobs(cik,kind,status,available_at,created_at,updated_at)
                                  VALUES (?,?,'queued',?,?,?)''', (cik, kind, available, now, now)).lastrowid
            self._event(db, job_id, 'enqueued', now)
            return self._job(db.execute('SELECT * FROM jobs WHERE id=?', (job_id,)).fetchone())

    def eligible_for_job(self, kind='refresh_company', limit=25, min_age_seconds=86_400):
        kind = _kind(kind)
        require(type(limit) is int and 1 <= limit <= 500, 'limit must be 1..500')
        require(type(min_age_seconds) is int and 0 <= min_age_seconds <= 366 * 86_400,
                'min_age_seconds must be 0..31622400')
        cutoff = _stamp(self._now() - timedelta(seconds=min_age_seconds))
        with self._connection() as db:
            rows = db.execute('''WITH candidates AS (SELECT i.*,
                (SELECT p.stored_at FROM company_payloads p WHERE p.cik=i.cik AND p.kind='collector_state' ORDER BY p.version DESC LIMIT 1) checked_at,
                (SELECT p.stored_at FROM company_payloads p WHERE p.cik=i.cik AND p.kind='history' ORDER BY p.version DESC LIMIT 1) history_at,
                (SELECT j.updated_at FROM jobs j WHERE j.cik=i.cik AND j.kind=? ORDER BY j.id DESC LIMIT 1) attempted_at
                FROM issuers i
                WHERE EXISTS(SELECT 1 FROM listings l WHERE l.cik=i.cik AND l.status='active')
                AND NOT EXISTS(SELECT 1 FROM jobs j WHERE j.cik=i.cik AND j.kind=? AND j.status IN ('queued','running','retry'))
                AND COALESCE((SELECT j.status FROM jobs j WHERE j.cik=i.cik AND j.kind=? ORDER BY j.id DESC LIMIT 1),'')<>'blocked')
                SELECT * FROM candidates
                WHERE MAX(COALESCE(checked_at,''),COALESCE(attempted_at,''))<=?
                ORDER BY CASE WHEN checked_at IS NULL THEN 0 ELSE 1 END,COALESCE(checked_at,history_at,attempted_at,''),cik
                LIMIT ?''', (kind, kind, kind, cutoff, limit)).fetchall()
            return self._records(db, rows)

    @staticmethod
    def _source_state(row, source, now):
        blocked_until = row['blocked_until'] if row else None
        next_request = row['next_request_at'] if row else None
        blocked = bool(blocked_until and _datetime(blocked_until) > now)
        return {'source': source, 'blocked': blocked, 'blocked_until': blocked_until,
                'reason': row['error'] if row else None, 'next_request_at': next_request,
                'interval_seconds': row['interval_seconds'] if row else 0.25,
                'wait_seconds': max(0.0, (_datetime(blocked_until) - now).total_seconds()) if blocked else 0.0,
                'updated_at': row['updated_at'] if row else None}

    def source_status(self, source='sec'):
        source = _kind(source)
        with self._connection() as db:
            return self._source_state(db.execute('SELECT * FROM source_limits WHERE source=?', (source,)).fetchone(), source, self._now())

    def reserve_source(self, source='sec', interval_seconds=0.25, now=None):
        """Reserve one shared request slot; cooldowns return their remaining wait.

        Callers must check source_status, wait only within their request budget,
        and recheck the cooldown immediately before each network attempt. This
        method makes no request and never sleeps. The shared floor is 4/sec.
        """
        source = _kind(source)
        require(type(interval_seconds) in (int, float) and 0.25 <= interval_seconds <= 60,
                'source request interval must be 0.25..60 seconds')
        with self._connection(write=True) as db:
            moment = _datetime(now) if now is not None else self._now()
            stamp = _stamp(moment)
            row = db.execute('SELECT * FROM source_limits WHERE source=?', (source,)).fetchone()
            state = self._source_state(row, source, moment)
            if state['blocked']:
                return state['wait_seconds']
            # A slower existing reservation policy cannot be weakened by a new worker.
            interval = max(interval_seconds, row['interval_seconds'] if row else 0.25)
            slot = max(moment, _datetime(row['next_request_at'])) if row and row['next_request_at'] else moment
            next_request = _stamp(slot + timedelta(seconds=interval))
            db.execute('''INSERT INTO source_limits(source,next_request_at,interval_seconds,updated_at) VALUES (?,?,?,?)
                ON CONFLICT(source) DO UPDATE SET next_request_at=excluded.next_request_at,
                interval_seconds=excluded.interval_seconds,updated_at=excluded.updated_at''', (source, next_request, interval, stamp))
            return max(0.0, (slot - moment).total_seconds())

    def pause_source(self, source, seconds, error=None, *, reason=None):
        source = _kind(source)
        require(type(seconds) in (int, float) and 0 < seconds <= 30 * 86_400,
                'source pause must be greater than zero and at most 30 days')
        error = _error(error if error is not None else reason or 'Source access paused')
        with self._connection(write=True) as db:
            moment = self._now()
            stamp, until = _stamp(moment), moment + timedelta(seconds=seconds)
            old = db.execute('SELECT * FROM source_limits WHERE source=?', (source,)).fetchone()
            if old and old['blocked_until'] and _datetime(old['blocked_until']) > until:
                until, error = _datetime(old['blocked_until']), old['error']
            db.execute('''INSERT INTO source_limits(source,blocked_until,error,updated_at) VALUES (?,?,?,?)
                ON CONFLICT(source) DO UPDATE SET blocked_until=excluded.blocked_until,error=excluded.error,
                updated_at=excluded.updated_at''', (source, _stamp(until), error, stamp))
            db.execute('INSERT INTO source_events(source,event,observed_at,details_json) VALUES (?,?,?,?)',
                       (source, 'paused', stamp, _json({'blocked_until': _stamp(until), 'error': error})))
            return self._source_state(db.execute('SELECT * FROM source_limits WHERE source=?', (source,)).fetchone(), source, moment)

    def claim(self, worker_id, now=None, lease_seconds=300):
        worker_id = _text(worker_id, 'worker ID', 200)
        require(type(lease_seconds) is int and 1 <= lease_seconds <= 86_400, 'lease_seconds must be 1..86400')
        with self._connection(write=True) as db:
            moment = _datetime(now) if now is not None else self._now()
            stamp, expires = _stamp(moment), _stamp(moment + timedelta(seconds=lease_seconds))
            while True:
                row = db.execute('''SELECT * FROM jobs WHERE
                    (status IN ('queued','retry') AND available_at<=?) OR (status='running' AND lease_expires_at<=?)
                    ORDER BY available_at,id LIMIT 1''', (stamp, stamp)).fetchone()
                if not row:
                    return None
                if row['attempts'] >= row['max_attempts']:
                    db.execute("""UPDATE jobs SET status='failed',error='Lease expired after maximum attempts',
                        updated_at=?,finished_at=?,lease_owner=NULL,lease_token=NULL,lease_expires_at=NULL WHERE id=?""",
                        (stamp, stamp, row['id']))
                    self._event(db, row['id'], 'attempts_exhausted', stamp)
                    continue
                token = uuid.uuid4().hex
                db.execute("""UPDATE jobs SET status='running',attempts=attempts+1,lease_owner=?,lease_token=?,
                    lease_expires_at=?,updated_at=?,finished_at=NULL WHERE id=?""", (worker_id, token, expires, stamp, row['id']))
                self._event(db, row['id'], 'lease_reclaimed' if row['status'] == 'running' else 'claimed', stamp, worker_id,
                            {'previous_worker': row['lease_owner'], 'attempt': row['attempts'] + 1})
                return self._job(db.execute('SELECT * FROM jobs WHERE id=?', (row['id'],)).fetchone())

    @staticmethod
    def _owned_job(db, job_id, worker_id, lease_token, now):
        require(type(job_id) is int and job_id > 0, 'job ID must be a positive integer')
        row = db.execute('SELECT * FROM jobs WHERE id=?', (job_id,)).fetchone()
        if not (row and row['status'] == 'running' and row['lease_owner'] == worker_id and row['lease_token'] == lease_token
                and row['lease_expires_at'] > now):
            raise LeaseLostError('job lease expired, was replaced, or does not belong to this worker')
        return row

    def _finish(self, db, row, worker_id, now, result):
        encoded = _json(result) if result is not None else None
        db.execute("""UPDATE jobs SET status='completed',updated_at=?,finished_at=?,error=NULL,result_json=?,
            lease_owner=NULL,lease_token=NULL,lease_expires_at=NULL WHERE id=?""", (now, now, encoded, row['id']))
        self._event(db, row['id'], 'completed', now, worker_id)
        return self._job(db.execute('SELECT * FROM jobs WHERE id=?', (row['id'],)).fetchone())

    def finish(self, job_id, worker_id, lease_token, result=None):
        with self._connection(write=True) as db:
            now = _stamp(self._now())
            row = self._owned_job(db, job_id, worker_id, lease_token, now)
            return self._finish(db, row, worker_id, now, result)

    def commit_job(self, job_id, worker_id, lease_token, payloads, result=None):
        """Publish staged company payloads and finish only under the live winning lease."""
        require(isinstance(payloads, dict), 'job payloads must map kinds to value/source objects')
        moment = self._now()
        prepared = []
        for kind, payload in payloads.items():
            require(isinstance(payload, dict) and 'value' in payload, 'job payload requires value')
            prepared.append(self._prepare_payload(kind, payload['value'], payload.get('source'), moment))
        _json(result) if result is not None else None
        with self._connection(write=True) as db:
            # Lock acquisition and serialization may outlast the lease.
            now = _stamp(self._now())
            row = self._owned_job(db, job_id, worker_id, lease_token, now)
            for payload in prepared:
                self._put_payload(db, row['cik'], payload, now)
            return self._finish(db, row, worker_id, now, result)

    def fail(self, job_id, worker_id, lease_token, error, retry_after_seconds=3600, max_attempts=5, blocked=False):
        error = _error(error)
        require(type(retry_after_seconds) is int and 0 <= retry_after_seconds <= MAX_RETRY_SECONDS,
                'retry_after_seconds must be 0..86400')
        require(type(max_attempts) is int and 1 <= max_attempts <= 100, 'max_attempts must be 1..100')
        require(type(blocked) is bool, 'blocked must be a boolean')
        with self._connection(write=True) as db:
            moment = self._now()
            now = _stamp(moment)
            row = self._owned_job(db, job_id, worker_id, lease_token, now)
            status = 'blocked' if blocked else ('failed' if row['attempts'] >= max_attempts else 'retry')
            delay = min(MAX_RETRY_SECONDS, retry_after_seconds * 2 ** min(max(row['attempts'] - 1, 0), 30))
            available = _stamp(moment + timedelta(seconds=delay))
            db.execute('''UPDATE jobs SET status=?,error=?,max_attempts=?,available_at=?,updated_at=?,finished_at=?,
                lease_owner=NULL,lease_token=NULL,lease_expires_at=NULL WHERE id=?''',
                (status, error, max_attempts, available, now, now if status in {'failed', 'blocked'} else None, row['id']))
            self._event(db, row['id'], status, now, worker_id, {'error': error, 'retry_after_seconds': delay if status == 'retry' else None})
            return self._job(db.execute('SELECT * FROM jobs WHERE id=?', (row['id'],)).fetchone())

    def stats(self):
        with self._connection() as db:
            statuses = {status: 0 for status in JOB_STATUSES}
            statuses.update({r['status']: r['count'] for r in db.execute('SELECT status,COUNT(*) count FROM jobs GROUP BY status')})
            latest = db.execute('SELECT summary_json FROM listing_snapshots WHERE is_seed=0 AND applied=1 ORDER BY retrieved_at DESC,id DESC LIMIT 1').fetchone()
            counts = {name: db.execute('SELECT COUNT(*) FROM ' + table).fetchone()[0]
                      for name, table in [('issuers', 'issuers'), ('listings', 'listings'), ('payloads', 'company_payloads'),
                                          ('listing_snapshots', 'listing_snapshots')]}
            counts.update({'schema_version': SCHEMA_VERSION, 'active_listings': db.execute("SELECT COUNT(*) FROM listings WHERE status='active'").fetchone()[0],
                           'inactive_listings': db.execute("SELECT COUNT(*) FROM listings WHERE status='inactive'").fetchone()[0],
                           'companies_with_payloads': db.execute('SELECT COUNT(DISTINCT cik) FROM company_payloads').fetchone()[0],
                           'jobs': statuses, 'last_listing_import': json.loads(latest['summary_json']) if latest else None,
                           'source_blocked': [dict(r) for r in db.execute("SELECT id,cik,kind,error,updated_at FROM jobs WHERE status='blocked' ORDER BY id DESC LIMIT 10")],
                           'sources': {r['source']: self._source_state(r, r['source'], self._now()) for r in db.execute('SELECT * FROM source_limits ORDER BY source')},
                           'scope': SCOPE})
            return counts
