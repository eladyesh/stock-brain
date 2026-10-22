"""Nasdaq's two public symbol directories, without invented issuer identities.

A listing_key identifies an exchange/symbol slot, NOT a permanent issuer.
Name changes increase identity_revision and clear attached dataset coverage.
Missing rows mean not observed in the current directory, never proven delisting.
"""
from datetime import datetime, timedelta, timezone
import csv
import hashlib
import io
import json
import re
from urllib.request import Request, urlopen

from coverage_store import _datetime, _stamp, _json, require

BASE = 'https://www.nasdaqtrader.com/dynamic/symdir/'
FILES = ('nasdaqlisted.txt', 'otherlisted.txt')
EXCHANGES = {'A': 'NYSE_AMERICAN', 'N': 'NYSE', 'P': 'NYSE_ARCA',
             'Z': 'CBOE_BZX', 'V': 'IEX', 'M': 'NYSE_TEXAS'}
MAX_BYTES = 5_000_000
DATASETS = ('profile', 'financials', 'prices', 'filings', 'news', 'estimates', 'ownership')
STOCK_TYPES = ('common_stock', 'depositary_receipt', 'partnership_unit', 'preferred')
EQUITY_TYPES = (*STOCK_TYPES, 'equity_candidate')


def classify(row):
    """Explicit flags first; ambiguous names remain candidates, not confirmed stocks."""
    if row['ETF'] == 'Y':
        return 'etf', 'directory ETF flag'
    if row.get('NextShares') == 'Y':
        return 'managed_fund', 'directory NextShares flag'
    name = row['Security Name'].lower()
    rules = (
        # Packaged units often mention their warrant/right components. The
        # traded instrument is still the unit, not one of those components.
        ('unit', r'\bunits?\b.*\b(?:each\s+(?:consisting|comprised)|consisting of)\b'),
        ('preferred', r'\b(preferred|preference|depositary shares.*(?:interest|preferred))\b'),
        ('warrant', r'\bwarrants?\b'),
        ('right', r'\brights\b'),
        ('debt', r'\b(notes|debentures|bonds)\b'),
        ('partnership_unit', r'\b(?:common units|(?:limited|operating) partnership units|representing limited partner(?:ship)? interests)\b'),
        ('unit', r'\bunits\b'),
        ('unit', r'\bunit\s*$'),
        ('depositary_receipt', r'\b(american depositary|american depository|ads|adrs?)\b'),
        ('common_stock', r'\b(common stock|common shares|ordinary shares|ordinary stock|shares of beneficial interest)\b'),
    )
    for kind, pattern in rules:
        if re.search(pattern, name):
            return kind, 'security-name classification; issuer/security-type review may refine it'
    return 'equity_candidate', 'not an ETF; instrument type not established by directory fields'


def parse_directory(raw, filename, *, retrieved_at, now=None, minimum_rows=1):
    require(filename in FILES and isinstance(raw, bytes), 'unsupported symbol directory')
    require(0 < len(raw) <= MAX_BYTES, 'symbol directory exceeds size limit')
    now = _datetime(now or datetime.now(timezone.utc))
    retrieved = _datetime(retrieved_at)
    require(retrieved <= now + timedelta(minutes=5), 'retrieval time is in the future')
    lines = raw.decode('utf-8-sig', errors='strict').splitlines()
    require(len(lines) >= 3, 'truncated directory')
    footer = re.fullmatch(r'File Creation Time: (\d{8}\d{2}:\d{2})\|*', lines[-1].strip())
    require(footer is not None, 'directory has no complete timestamp footer')
    # Nasdaq documents a file creation timestamp, but not a timezone in this
    # field definition. Preserve the literal value; compare calendar dates only.
    created = datetime.strptime(footer[1], '%m%d%Y%H:%M')
    age = (retrieved.date() - created.date()).days
    require(-1 <= age <= 7, 'directory creation date is stale or in the future')
    reader = csv.DictReader(io.StringIO('\n'.join(lines[:-1])), delimiter='|')
    required = {'Security Name', 'Test Issue', 'ETF'} | (
        {'Symbol', 'Market Category'} if filename == FILES[0] else {'ACT Symbol', 'Exchange', 'CQS Symbol', 'NASDAQ Symbol'})
    require(reader.fieldnames is not None and len(set(reader.fieldnames)) == len(reader.fieldnames)
            and required <= set(reader.fieldnames), 'directory schema does not match')
    rows, seen = [], set()
    for row in reader:
        require(None not in row and all(v is not None for v in row.values()), 'malformed directory row')
        require(all(len(v) <= 2000 and not any(ord(c) < 32 for c in v) for v in row.values()), 'invalid directory field')
        require(row['ETF'] in ('Y', 'N') and row['Test Issue'] in ('Y', 'N'), 'unknown directory flag')
        ticker = row.get('Symbol') or row['ACT Symbol']
        require(bool(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9.\-^/+= $]{0,31}', ticker)), 'invalid directory symbol')
        require(bool(row['Security Name'].strip()), 'missing security name')
        exchange = 'NASDAQ' if filename == FILES[0] else EXCHANGES.get(row['Exchange'], 'UNKNOWN_' + row['Exchange'])
        key = hashlib.sha256((exchange + '\n' + ticker).encode()).hexdigest()[:32]
        require(key not in seen, 'duplicate exchange/symbol slot')
        seen.add(key)
        kind, basis = classify(row)
        rows.append({'listing_key': key, 'ticker': ticker, 'exchange': exchange,
                     'security_name': row['Security Name'].strip(), 'instrument_type': kind,
                     'classification_basis': basis, 'is_test': int(row['Test Issue'] == 'Y'), 'raw': row})
    require(minimum_rows <= len(rows) <= 100_000, 'directory row count outside expected bounds')
    source = {'url': BASE + filename, 'sha256': hashlib.sha256(raw).hexdigest(),
              'retrieved_at': _stamp(retrieved), 'file_created_at_local': created.isoformat(),
              'file_timezone': 'not supplied in the source field definition', 'row_count': len(rows)}
    return {'filename': filename, 'source': source, 'rows': rows}


def fetch_directories(*, opener=urlopen):
    result = []
    for name in FILES:
        # One attempt, truthful client identifier, no fingerprint/IP rotation.
        with opener(Request(BASE + name, headers={'User-Agent': 'StockBrain/1.0 listing-directory research'}), timeout=45) as response:
            require(response.geturl() == BASE + name, 'unexpected directory redirect')
            raw = response.read(MAX_BYTES + 1)
        result.append(parse_directory(raw, name, retrieved_at=datetime.now(timezone.utc), minimum_rows=1000))
    return result


def _name_matches(directory_name, issuer_name):
    """Equivalent legal spelling, followed only by a legal/security suffix.

    This is not fuzzy matching: Holdings, Group and other business-name words
    remain significant. SEC jurisdiction suffixes such as /DE/ are metadata.
    Exact ticker/venue evidence is still required by every caller.
    """
    legal = {'inc', 'corp', 'co', 'ltd', 'plc', 'llc', 'lp', 'sa', 'nv', 'na'}
    synonyms = {'incorporated': 'inc', 'corporation': 'corp', 'company': 'co', 'limited': 'ltd'}
    def words(value):
        value = value.casefold()
        # Observed jurisdiction/type annotations, never arbitrary parentheticals
        # or country/business words appearing as part of the issuer's name.
        annotation = r'(?:de|delaware|ma|nj|ca|cayman|reit)'
        value = re.sub(r'\(' + annotation + r'\)', ' ', value)
        value = re.sub(r'[/\\]\s*' + annotation + r'/?\s*$', '', value)
        value = re.sub(r'/[a-z]{2}/?\s*$', '', value)
        for dotted, plain in (('s.a.', 'sa'), ('n.v.', 'nv'), ('n.a.', 'na'),
                              ('l.l.c.', 'llc'), ('l.p.', 'lp')):
            value = re.sub(r'\b' + re.escape(dotted), plain, value)
        value = value.replace('&', ' and ').replace('+', ' and ').replace("'", '').replace('’', '')
        result = [synonyms.get(w, w) for w in re.sub(r'[^a-z0-9]+', ' ', value).split()]
        if result and result[0] == 'the': result = result[1:]
        return result
    issuer, listing = words(issuer_name), words(directory_name)
    while issuer and issuer[-1] in legal | {'the'}: issuer.pop()
    if not issuer:
        return False
    for boundary in range(1, len(listing) + 1):
        core, remainder = listing[:boundary], listing[boundary:]
        while core and core[-1] in legal | {'the'}: core.pop()
        # Whitespace/punctuation differences (JP Morgan vs JPMorgan) preserve
        # every business-name character and its order. No edit-distance match.
        if ''.join(core) != ''.join(issuer):
            continue
        while remainder and remainder[0] in legal | {'the'}: remainder = remainder[1:]
        if len(remainder) >= 2 and remainder[0] == 'new' and remainder[1] in {'common', 'ordinary'}:
            remainder = remainder[1:]
        if not remainder or remainder[0] in {'common', 'ordinary', 'class', 'series', 'american',
                'depositary', 'depository', 'preferred', 'preference', 'shares', 'units', 'rights', 'warrants'}:
            return True
    return False


def sec_symbol(row):
    """SEC class/preferred separators; the original directory slot is preserved."""
    ticker = row['ticker']
    if row['instrument_type'] == 'preferred':
        ticker = re.sub(r'^([A-Z0-9]+)\$([A-Z0-9]+)$', r'\1-P\2', ticker)
    return re.sub(r'^([A-Z0-9]+)\.([A-Z])$', r'\1-\2', ticker)


def sec_venue_matches(exchange, sec_venues):
    # SEC identifies NYSE-family listings as NYSE. Nasdaq's directory retains
    # the specific primary venue; this does not change the listing's exchange.
    return exchange in sec_venues or ('NYSE' in sec_venues and
        exchange in {'NYSE_AMERICAN', 'NYSE_ARCA', 'NYSE_TEXAS'})


def import_directories(store, directories):
    require(len(directories) == 2 and {d['filename'] for d in directories} == set(FILES), 'both complete directories are required')
    now = _stamp(store._now())
    rows = [r for d in directories for r in d['rows']]
    require(len({r['listing_key'] for r in rows}) == len(rows), 'conflicting cross-directory listing')
    sources = {d['filename']: d['source'] for d in directories}
    summary = {'rows': len(rows), 'added': 0, 'changed': 0, 'not_in_latest_directory': 0}
    with store._connection(write=True) as db:
        last = db.execute('SELECT * FROM market_directory_runs ORDER BY id DESC LIMIT 1').fetchone()
        if last:
            previous_sources = json.loads(last['sources_json'])
            for d in directories:
                previous = previous_sources[d['filename']]
                require(d['source']['file_created_at_local'] >= previous['file_created_at_local'], 'older directory cannot replace current state')
                require(len(d['rows']) >= previous['row_count'] * 0.90, 'directory shrank by over 10%; manual reconciliation required')
        run_id = db.execute('INSERT INTO market_directory_runs(imported_at,sources_json,row_count,summary_json) VALUES (?,?,?,?)',
                            (now, _json(sources), len(rows), '{}')).lastrowid
        for directory in directories:
            source = _json(directory['source'])
            for row in directory['rows']:
                old = db.execute('SELECT * FROM market_securities WHERE listing_key=?', (row['listing_key'],)).fetchone()
                candidates = db.execute('''SELECT l.cik,i.company_name FROM listings l JOIN issuers i USING(cik)
                    WHERE l.ticker=? AND l.exchange=? AND l.status='active' ''', (row['ticker'], row['exchange'])).fetchall()
                match = candidates[0] if len(candidates) == 1 and _name_matches(row['security_name'], candidates[0]['company_name']) else None
                cik, mapping = (match['cik'], 'registered issuer, exact exchange/ticker and compatible name') if match else (None, None)
                if row['is_test'] or row['instrument_type'] not in EQUITY_TYPES:
                    cik, mapping = None, None
                changed = bool(old and (old['security_name'] != row['security_name']
                    or old['instrument_type'] != row['instrument_type']
                    or old['directory_status'] != 'present'
                    or (old['cik'] is not None and old['cik'] != cik)))
                revision = (old['identity_revision'] if old else 1) + int(changed)
                first = old['first_seen_at'] if old else now
                values = (row['listing_key'], row['ticker'], row['exchange'], row['security_name'], row['instrument_type'],
                          row['classification_basis'], row['is_test'], 'present', revision, cik, mapping, directory['filename'],
                          source, _json(row['raw']), first, now, run_id)
                db.execute('''INSERT INTO market_securities VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    ON CONFLICT(listing_key) DO UPDATE SET security_name=excluded.security_name,
                    instrument_type=excluded.instrument_type,classification_basis=excluded.classification_basis,
                    is_test=excluded.is_test,directory_status=excluded.directory_status,identity_revision=excluded.identity_revision,
                    cik=excluded.cik,mapping_basis=excluded.mapping_basis,source_name=excluded.source_name,
                    source_json=excluded.source_json,raw_json=excluded.raw_json,last_seen_at=excluded.last_seen_at,last_run_id=excluded.last_run_id''', values)
                event = 'new_listing_slot' if old is None else 'reappeared' if old['directory_status'] != 'present' else 'identity_evidence_changed' if changed else None
                if event:
                    db.execute('INSERT INTO market_directory_events(listing_key,run_id,event,observed_at,details_json) VALUES (?,?,?,?,?)',
                               (row['listing_key'], run_id, event, now, _json({'previous_name': old['security_name'] if old else None,
                                                                          'current_name': row['security_name'], 'identity_revision': revision})))
                if changed:
                    db.execute('DELETE FROM market_dataset_attempts WHERE listing_key=?', (row['listing_key'],))
                summary['added'] += int(old is None)
                summary['changed'] += int(changed)
        missing = db.execute("SELECT listing_key FROM market_securities WHERE last_run_id!=? AND directory_status='present'", (run_id,)).fetchall()
        for item in missing:
            db.execute('INSERT INTO market_directory_events(listing_key,run_id,event,observed_at,details_json) VALUES (?,?,?,?,?)',
                       (item['listing_key'], run_id, 'not_observed', now, '{}'))
        db.execute("UPDATE market_securities SET directory_status='not_in_latest_directory' WHERE last_run_id!=?", (run_id,))
        summary['not_in_latest_directory'] = len(missing)
        db.execute('UPDATE market_directory_runs SET summary_json=? WHERE id=?', (_json(summary), run_id))
    return {**summary, 'run_id': run_id}


def directory_status(store):
    with store._connection() as db:
        last = db.execute('SELECT * FROM market_directory_runs ORDER BY id DESC LIMIT 1').fetchone()
        groups = db.execute("SELECT instrument_type,count(*) AS n FROM market_securities WHERE directory_status='present' AND is_test=0 GROUP BY instrument_type").fetchall()
        linked = db.execute("SELECT count(*) FROM market_securities WHERE directory_status='present' AND is_test=0 AND cik IS NOT NULL").fetchone()[0]
        checks = db.execute('''SELECT s.cik,p.source_retrieved_at FROM market_securities s
            LEFT JOIN company_payloads p ON p.id=(SELECT p2.id FROM company_payloads p2
                WHERE p2.cik=s.cik AND p2.kind='collector_state' ORDER BY p2.version DESC LIMIT 1)
            WHERE s.directory_status='present' AND s.is_test=0 AND s.instrument_type IN ('''
            + ','.join('?' for _ in EQUITY_TYPES) + ')', EQUITY_TYPES).fetchall()
        dataset_rows = db.execute('''SELECT dataset,count(DISTINCT listing_key) AS n FROM (
            SELECT s.listing_key,o.dataset FROM market_securities s JOIN market_observations o
              ON o.listing_key=s.listing_key AND o.identity_revision=s.identity_revision
              WHERE s.directory_status='present' AND s.is_test=0
            UNION SELECT s.listing_key,CASE p.kind WHEN 'history' THEN 'financials'
              WHEN 'sec_bulk_identity' THEN 'profile' WHEN 'submissions' THEN 'filings' ELSE p.kind END
              FROM market_securities s JOIN company_payloads p ON p.cik=s.cik
              WHERE s.directory_status='present' AND s.is_test=0 AND p.kind IN ('history','reviewed_research','sec_bulk_identity','submissions')
            ) GROUP BY dataset''').fetchall()
    sources = json.loads(last['sources_json']) if last else {}
    oldest = min((_datetime(s['retrieved_at']) for s in sources.values()), default=None)
    age_hours = max(0, (store._now() - oldest).total_seconds() / 3600) if oldest else None
    counts = {r['instrument_type']: r['n'] for r in groups}
    check_counts = {key: 0 for key in ('recent', 'overdue', 'not_checked', 'invalid_timestamp')}
    for row in checks:
        check_counts[_collection_check(row['source_retrieved_at'], store._now())['status']] += 1
    return {'status': 'unavailable' if not last else 'stale' if age_hours > 36 else 'checked',
            'imported_at': last['imported_at'] if last else None, 'age_hours': round(age_hours, 2) if age_hours is not None else None,
            'sources': sources, 'listed_securities': sum(counts.values()), 'equity_candidates': sum(counts.get(k, 0) for k in EQUITY_TYPES),
            'instrument_counts': counts, 'linked_issuer_count': linked,
            'coverage_progress': {'scope': 'stock candidates including unresolved instruments; counts are listing counts unless stated',
                'total_listings': len(checks), 'mapped_listings': sum(r['cik'] is not None for r in checks),
                'unmapped_listings': sum(r['cik'] is None for r in checks),
                'distinct_mapped_issuers': len({r['cik'] for r in checks if r['cik']}),
                'filing_checks': {**check_counts, 'freshness_hours': 48,
                    'basis': 'Latest collector-state source retrieval, not directory import or payload storage time'}},
            'stock_scope': {'classified_stock_listings': sum(counts.get(k, 0) for k in STOCK_TYPES),
                           'unresolved_instruments': counts.get('equity_candidate', 0),
                           'included_types': list(STOCK_TYPES), 'otc': 'not_collected',
                           'domicile': 'US trading venue, not US incorporation',
                           'classification': 'Directory flags and names; fund/issuer review still required'},
            'data_coverage': {**{k: 0 for k in (*DATASETS, 'reviewed_research')}, **{r['dataset']: r['n'] for r in dataset_rows}},
            'scope': 'Two Nasdaq Trader directories; non-test listings. Candidates are not a verified count of operating companies. No OTC coverage.'}


def list_securities(store, *, query='', limit=50, offset=0, instrument='equities', exchange='', status='present'):
    require(1 <= limit <= 100 and 0 <= offset <= 1_000_000, 'invalid pagination')
    require(instrument in ('equities', 'stocks', 'all', 'etf', 'unknown', 'preferred', 'partnership_unit'), 'invalid instrument filter')
    require(status in ('present', 'all', 'not_in_latest_directory'), 'invalid listing status')
    clauses, params = ['s.is_test=0'], []
    if status != 'all': clauses.append('s.directory_status=?'); params.append(status)
    if instrument in ('equities', 'stocks'):
        kinds = EQUITY_TYPES if instrument == 'equities' else STOCK_TYPES
        clauses.append('s.instrument_type IN (' + ','.join('?' for _ in kinds) + ')'); params.extend(kinds)
    elif instrument != 'all': clauses.append('s.instrument_type=?'); params.append('equity_candidate' if instrument == 'unknown' else instrument)
    if exchange: clauses.append('s.exchange=?'); params.append(exchange)
    if query:
        escaped = query.replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')
        clauses.append("(s.ticker LIKE ? ESCAPE '\\' OR s.security_name LIKE ? ESCAPE '\\' OR s.cik=?)")
        params.extend(['%' + escaped + '%', '%' + escaped + '%', query.zfill(10) if query.isdigit() else query])
    where = ' AND '.join(clauses)
    with store._connection() as db:
        total = db.execute('SELECT count(*) FROM market_securities s WHERE ' + where, params).fetchone()[0]
        rows = db.execute('SELECT s.* FROM market_securities s WHERE ' + where +
                          ' ORDER BY CASE WHEN s.ticker=? COLLATE NOCASE THEN 0 ELSE 1 END,s.ticker,s.exchange LIMIT ? OFFSET ?',
                          [*params, query, limit, offset]).fetchall()
        result = [_public_record(db, row, store._now()) for row in rows]
    return {'items': result, 'total': total, 'limit': limit, 'offset': offset}


def _collection_check(retrieved_at, now):
    state = 'not_checked'
    if retrieved_at:
        try:
            age = (now - _datetime(retrieved_at)).total_seconds() / 3600
            state = 'invalid_timestamp' if age < -5 / 60 else 'recent' if age <= 48 else 'overdue'
        except (ValueError, TypeError):
            state = 'invalid_timestamp'
    return {'status': state, 'last_checked_at': retrieved_at, 'freshness_hours': 48,
            'basis': 'issuer filing source retrieval; directory updates do not refresh this timestamp'}


def _public_record(db, row, now):
    result = {k: row[k] for k in ('listing_key', 'ticker', 'exchange', 'security_name', 'instrument_type',
                                'classification_basis', 'directory_status', 'identity_revision', 'cik', 'mapping_basis',
                                'first_seen_at', 'last_seen_at')}
    result['source'] = json.loads(row['source_json'])
    payloads = {r['kind']: r['source_retrieved_at'] for r in db.execute('''SELECT p.kind,p.source_retrieved_at
        FROM company_payloads p WHERE p.cik=? AND p.version=(SELECT max(p2.version) FROM company_payloads p2
            WHERE p2.cik=p.cik AND p2.kind=p.kind)''', (row['cik'],))} if row['cik'] else {}
    result['filing_check'] = _collection_check(payloads.get('collector_state'), now)
    observations = {r['dataset']: r['retrieved_at'] for r in db.execute('''SELECT dataset,max(retrieved_at) AS retrieved_at
        FROM market_observations WHERE listing_key=? AND identity_revision=? GROUP BY dataset''', (row['listing_key'], row['identity_revision']))}
    result['datasets'] = {kind: {'status': 'available' if kind in observations else 'not_collected', 'retrieved_at': observations.get(kind)} for kind in DATASETS}
    if 'history' in payloads and 'financials' not in observations:
        result['datasets']['financials'] = {'status': 'retained', 'retrieved_at': payloads['history']}
    for kind, payload, scope in (('profile', 'sec_bulk_identity', 'issuer_identity_only'),
                                 ('filings', 'submissions', 'recent_metadata_only')):
        if payload in payloads and kind not in observations:
            result['datasets'][kind] = {'status': 'retained', 'retrieved_at': payloads[payload], 'scope': scope}
    result['research_status'] = 'dated_review_available' if 'reviewed_research' in payloads else 'not_reviewed'
    return result


def security_detail(store, listing_key):
    require(bool(re.fullmatch(r'[0-9a-f]{32}', listing_key)), 'invalid listing key')
    with store._connection() as db:
        row = db.execute('SELECT * FROM market_securities WHERE listing_key=?', (listing_key,)).fetchone()
        if row is None: return None
        result = _public_record(db, row, store._now())
        result['raw_directory_fields'] = json.loads(row['raw_json'])
    return result
