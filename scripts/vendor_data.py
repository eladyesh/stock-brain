"""Optional, budgeted vendor ingestion. Disabled until operator configuration.

Financial Datasets is a separate contracted source, not a way around an SEC
access denial. Public release publication requires a separate written bulk-export
grant; a display/redistribution plan alone is insufficient under the vendor terms.
Vendor financials remain provider-normalized data, outside the reviewed/GAAP and
TTM answer pipeline until a dedicated accounting adapter passes its evidence gates.
"""
from datetime import date, datetime, timedelta, timezone
import base64
import hashlib
import json
import math
import os
import re
import time
from urllib.error import HTTPError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, HTTPRedirectHandler, build_opener

from coverage_store import _datetime, _stamp, _json, normalize_cik, require
import market_directory as directory

PROVIDER = 'financial_datasets'
API = 'https://api.financialdatasets.ai'
CADENCE = {'profile': 7 * 24, 'financials': 24, 'prices': 24}
ENDPOINTS = {'profile': '/company/facts', 'financials': '/financials', 'prices': '/prices/snapshot'}
MAX_RESPONSE = 4_000_000
REPOSITORY = 'eladyesh/stock-brain'


def reserve_daily_run(environ, *, opener=None):
    """Reserve the entire day's request allowance before any billable request.

    The create-only Contents API write survives failed builds and lost ephemeral
    runners. A second run that day skips vendor calls, even if the first failed.
    Credentials are only sent to the fixed GitHub API; bodies are not logged.
    """
    require(environ.get('GITHUB_ACTIONS') == 'true' and environ.get('GH_TOKEN'), 'durable_vendor_budget_ledger_required')
    opener = opener or build_opener(NoRedirect()).open
    branch = 'automation/vendor-budget'
    api = 'https://api.github.com/repos/' + REPOSITORY
    headers = {'Authorization': 'Bearer ' + environ['GH_TOKEN'], 'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28', 'Content-Type': 'application/json'}
    def request(path, method='GET', value=None):
        try:
            with opener(Request(api + path, headers=headers, method=method,
                        data=json.dumps(value).encode() if value is not None else None), timeout=30) as response:
                return json.loads(response.read(1_000_000))
        except HTTPError as error:
            return {'http_error': error.code}
    ref = request('/git/ref/heads/' + branch)
    if ref.get('http_error') == 404:
        result = request('/git/refs', 'POST', {'ref': 'refs/heads/' + branch, 'sha': environ['GITHUB_SHA']})
        require(not result.get('http_error') or result['http_error'] == 422, 'cannot_create_budget_ledger')
    elif ref.get('http_error'):
        raise ProviderStop('cannot_read_budget_ledger')
    day = datetime.now(timezone.utc).date().isoformat()
    path = '/contents/reservations/financial-datasets-' + day + '.json'
    value = {'day': day, 'reserved_requests': int(environ['STOCK_BRAIN_FD_MAX_DAILY_REQUESTS']),
             'run_id': environ.get('GITHUB_RUN_ID'), 'run_attempt': environ.get('GITHUB_RUN_ATTEMPT')}
    result = request(path, 'PUT', {'message': 'Reserve vendor request allowance for ' + day, 'branch': branch,
                                 'content': base64.b64encode(json.dumps(value).encode()).decode()})
    if result.get('http_error') in {409, 422}: return False
    require(not result.get('http_error') and result.get('content', {}).get('sha'), 'cannot_reserve_vendor_budget')
    return True


class ProviderStop(ValueError):
    pass


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None  # Never forward API credentials to a redirect target.


class FinancialDatasets:
    def __init__(self, store, *, environ=None, opener=None, sleep=time.sleep):
        self.store, self.environ = store, os.environ if environ is None else environ
        self.opener, self.sleep = opener or build_opener(NoRedirect()).open, sleep

    def readiness(self):
        env = self.environ
        raw_budget = env.get('STOCK_BRAIN_FD_MAX_DAILY_REQUESTS', '0')
        budget = int(raw_budget) if re.fullmatch(r'\d{1,5}', raw_budget) else 0
        budget = budget if 0 <= budget <= 1000 else 0
        reason = ('disabled' if env.get('STOCK_BRAIN_FD_ENABLED') != '1' else
                  'api_key_missing' if not env.get('FINANCIAL_DATASETS_API_KEY') else
                  'public_data_license_not_confirmed' if env.get('STOCK_BRAIN_FD_PUBLIC_DATA_LICENSE') != '1' else
                  'written_bulk_export_permission_missing' if env.get('STOCK_BRAIN_FD_BULK_EXPORT_PERMISSION') != '1' else
                  'daily_request_budget_missing' if not budget else
                  'source_cooldown' if self.store.source_status(PROVIDER)['blocked'] else None)
        return {'provider': PROVIDER, 'ready': reason is None, 'reason': reason, 'daily_request_budget': budget,
                'datasets': list(CADENCE), 'network_checked': False}

    def request(self, security, dataset):
        ready = self.readiness()
        if not ready['ready']: raise ProviderStop(ready['reason'])
        now = self.store._now()
        # In-run counter complements the durable, create-only daily reservation.
        with self.store._connection(write=True) as db:
            day = now.date().isoformat()
            db.execute('INSERT OR IGNORE INTO provider_daily_usage VALUES (?,?,0)', (PROVIDER, day))
            used = db.execute('SELECT request_count FROM provider_daily_usage WHERE provider=? AND day=?', (PROVIDER, day)).fetchone()[0]
            if used >= ready['daily_request_budget']: raise ProviderStop('daily_budget_exhausted')
            db.execute('UPDATE provider_daily_usage SET request_count=request_count+1 WHERE provider=? AND day=?', (PROVIDER, day))
        delay = self.store.reserve_source(PROVIDER, interval_seconds=1)
        if delay > 5: raise ProviderStop('source_rate_deferred')
        if delay: self.sleep(delay)
        if self.store.source_status(PROVIDER)['blocked']: raise ProviderStop('source_cooldown')
        params = {'ticker': security['ticker']}
        if dataset == 'financials': params.update(period='quarterly', limit=8)
        url = API + ENDPOINTS[dataset] + '?' + urlencode(params)
        try:
            with self.opener(Request(url, headers={'X-API-KEY': self.environ['FINANCIAL_DATASETS_API_KEY'],
                        'User-Agent': 'StockBrain/1.0 authorized-data-client'}), timeout=30) as response:
                require(response.geturl() == url, 'unexpected vendor redirect')
                raw = response.read(MAX_RESPONSE + 1)
        except HTTPError as error:
            code = 'http_' + str(error.code)
            if error.code in {401, 402, 403, 429}:
                self.store.pause_source(PROVIDER, 86400 if error.code != 429 else 3600, error=code)
                raise ProviderStop(code) from None
            raise ValueError(code) from None
        require(len(raw) <= MAX_RESPONSE, 'vendor_response_too_large')
        value = json.loads(raw, parse_constant=lambda _: (_ for _ in ()).throw(ValueError('non_finite_json')))
        source = {'url': url, 'sha256': hashlib.sha256(raw).hexdigest(), 'retrieved_at': _stamp(self.store._now())}
        return value, source


def validate_payload(security, dataset, value, source, now):
    """Validate identities/units/periods; never manufacture a reviewed research claim."""
    retrieved = _datetime(source['retrieved_at'])
    require(retrieved <= now + timedelta(minutes=5), 'future_vendor_retrieval')
    require(re.fullmatch('[0-9a-f]{64}', source['sha256']) is not None, 'invalid_source_hash')
    parsed = urlsplit(source['url'])
    require(parsed.scheme == 'https' and parsed.hostname == 'api.financialdatasets.ai' and not parsed.username
            and not parsed.password and 'key' not in parsed.query.lower() and 'token' not in parsed.query.lower(), 'unsafe_source_url')
    require(isinstance(value, dict), 'invalid_vendor_response')
    _json(value)  # Reject NaN/Infinity in nested financial values.
    if dataset == 'profile':
        record = value.get('company_facts')
        require(isinstance(record, dict) and record.get('ticker') == security['ticker'], 'vendor_ticker_mismatch')
        require(directory._name_matches(security['security_name'], record.get('name') or '\x00'), 'vendor_name_mismatch')
        exchange = str(record.get('exchange', '')).upper()
        require(exchange == security['exchange'] or (security['exchange'] == 'NASDAQ' and exchange in {'NASDAQGS', 'NASDAQGM', 'NASDAQCM'}), 'vendor_exchange_mismatch')
        require(record.get('is_active') is True, 'vendor_inactive_security')
        cik = normalize_cik(record.get('cik'))
        require(not security.get('cik') or security['cik'] == cik, 'vendor_cik_mismatch')
        return {'as_of': _stamp(retrieved), 'as_of_basis': 'retrieval_only', 'cik': cik}
    if dataset == 'prices':
        record = value.get('snapshot')
        require(isinstance(record, dict) and record.get('ticker') == security['ticker'], 'vendor_ticker_mismatch')
        price = record.get('price')
        require(type(price) in (int, float) and math.isfinite(price) and price > 0, 'invalid_price')
        stamp = _datetime(record['time'])
        require(stamp <= now + timedelta(minutes=5), 'future_trade_time')
        return {'as_of': _stamp(stamp), 'as_of_basis': 'vendor_trade_time', 'currency': record.get('currency')}
    require(dataset == 'financials' and security.get('cik'), 'verified_issuer_required')
    statements = value.get('financials')
    require(isinstance(statements, dict), 'missing_financial_statements')
    ends = []
    for kind in ('income_statements', 'balance_sheets', 'cash_flow_statements'):
        records = statements.get(kind)
        require(isinstance(records, list) and 0 < len(records) <= 100, 'incomplete_financial_statements')
        for record in records:
            require(isinstance(record, dict) and record.get('ticker') == security['ticker'], 'vendor_ticker_mismatch')
            require(record.get('period') == 'quarterly' and re.fullmatch('[A-Z]{3}', record.get('currency', '')), 'financial_period_or_currency_missing')
            end = date.fromisoformat(record['report_period'])
            require(end <= now.date(), 'future_financial_period')
            require(re.fullmatch(r'\d{10}-\d{2}-\d{6}', record.get('accession_number', '')), 'financial_filing_identity_missing')
            filing = urlsplit(record.get('filing_url', ''))
            require(filing.scheme == 'https' and filing.hostname and not filing.username and not filing.password, 'financial_source_missing')
            ends.append(end.isoformat())
    return {'as_of': max(ends), 'as_of_basis': 'latest_reported_period', 'accounting_status': 'vendor_normalized_unreviewed'}


def save_observation(store, security, dataset, value, source):
    validated = validate_payload(security, dataset, value, source, store._now())
    payload = {'data': value, 'validation': validated, 'review_status': 'unreviewed'}
    encoded = _json(payload)
    digest = hashlib.sha256((encoded + _json(source)).encode()).hexdigest()
    with store._connection(write=True) as db:
        current = db.execute('SELECT * FROM market_securities WHERE listing_key=?', (security['listing_key'],)).fetchone()
        require(current is not None and current['identity_revision'] == security['identity_revision']
                and current['directory_status'] == 'present', 'listing_identity_changed')
        db.execute('''INSERT OR IGNORE INTO market_observations(listing_key,identity_revision,dataset,provider,
                      retrieved_at,as_of,source_json,payload_json,sha256) VALUES (?,?,?,?,?,?,?,?,?)''',
                   (security['listing_key'], security['identity_revision'], dataset, PROVIDER,
                    source['retrieved_at'], validated['as_of'], _json(source), encoded, digest))
    return validated


def due_tasks(store, *, limit=1000):
    """Fair ordering by prior attempts; unsupported/unlinked datasets stay explicit."""
    now = store._now()
    queues = {}
    with store._connection() as db:
        for dataset, hours in CADENCE.items():
            rows = db.execute('''SELECT s.*, a.attempted_at FROM market_securities s
                LEFT JOIN market_dataset_attempts a ON a.listing_key=s.listing_key AND a.dataset=?
                WHERE s.directory_status='present' AND s.is_test=0
                AND s.instrument_type IN (''' + ','.join('?' for _ in directory.EQUITY_TYPES) + ''')
                AND (?='profile' OR s.cik IS NOT NULL)
                AND (a.attempted_at IS NULL OR a.attempted_at<=?)
                ORDER BY coalesce(a.attempted_at,''),s.ticker LIMIT ?''',
                (dataset, *directory.EQUITY_TYPES, dataset, _stamp(now - timedelta(hours=hours)), limit)).fetchall()
            queues[dataset] = [dict(row) for row in rows if dataset == 'profile' or row['cik']]
    result = []
    while any(queues.values()) and len(result) < limit:
        for dataset in ('financials', 'prices', 'profile'):
            if queues[dataset] and len(result) < limit:
                result.append((dataset, queues[dataset].pop(0)))
    return result


def collect(store, provider=None, *, timeout_seconds=900, reserve=reserve_daily_run):
    provider = provider or FinancialDatasets(store)
    ready = provider.readiness()
    report = {'provider': ready, 'attempted': 0, 'stored': 0, 'failed': 0, 'stopped_reason': ready['reason']}
    if not ready['ready']: return report
    if not reserve(provider.environ):
        report['stopped_reason'] = 'daily_allowance_already_reserved'
        return report
    deadline = time.monotonic() + timeout_seconds
    for dataset, security in due_tasks(store, limit=ready['daily_request_budget']):
        if time.monotonic() >= deadline:
            report['stopped_reason'] = 'runtime_budget_exhausted'; break
        status, code = 'success', None
        try:
            report['attempted'] += 1
            value, source = provider.request(security, dataset)
            validated = save_observation(store, security, dataset, value, source)
            if dataset == 'profile':
                profile = value['company_facts']
                store.import_listings({'fields': ['cik', 'name', 'ticker', 'exchange'], 'data':
                    [[validated['cik'], profile['name'], security['ticker'], security['exchange']]]}, source, complete=False)
                with store._connection(write=True) as db:
                    db.execute('''UPDATE market_securities SET cik=?,mapping_basis=? WHERE listing_key=? AND identity_revision=?''',
                               (validated['cik'], 'vendor profile matched to exchange/ticker/name', security['listing_key'], security['identity_revision']))
            report['stored'] += 1
        except ProviderStop as error:
            report['stopped_reason'] = str(error); break
        except (ValueError, KeyError, TypeError, OSError):
            status, code = 'failed', 'provider_validation_or_transport_error'
            report['failed'] += 1
        with store._connection(write=True) as db:
            db.execute('INSERT OR REPLACE INTO market_dataset_attempts VALUES (?,?,?,?,?)',
                       (security['listing_key'], dataset, _stamp(store._now()), status, code))
    return report
