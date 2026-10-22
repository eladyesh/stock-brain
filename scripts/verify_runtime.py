"""Exercise public APIs and a real cold restore after a GitHub backup."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile
import urllib.request
from urllib.parse import urlsplit

import audit_financials
import runtime_data as data


def age_hours(stamp, now):
    try:
        parsed = datetime.fromisoformat(stamp.replace('Z', '+00:00'))
        if parsed.tzinfo is None:
            return None
        return round((now - parsed).total_seconds() / 3600, 2)
    except (AttributeError, TypeError, ValueError):
        return None


def source_health(files, now=None, max_age_hours=36):
    """Report source retrieval independently of a completed partial collector run."""
    now = now or datetime.now(timezone.utc)
    run = files['run-status.json']
    financial_runs = {r['ticker']: r for r in run.get('financials', [])}
    market_runs = {r['ticker']: r for r in run.get('market', [])}
    financials, market, discovery = [], [], []
    for company in files['desk.json']['companies']:
        ticker = company['ticker']
        history, quote = company.get('history') or {}, company.get('quote') or {}
        for rows, value, result, success in [(financials, history.get('source', {}), financial_runs.get(ticker, {}), 'collected'),
                                              (market, quote, market_runs.get(ticker, {}), 'available')]:
            age = age_hours(value.get('retrieved_at'), now)
            recent = age is not None and -5 / 60 <= age <= max_age_hours
            collected = result.get('status') == success
            rows.append({'ticker': ticker, 'collection_status': result.get('status', 'unknown'),
                         'retrieved_at': value.get('retrieved_at'), 'retrieval_age_hours': age,
                         'fresh_retrieval': collected and recent,
                         'status': 'fresh_retrieval' if collected and recent else
                                   ('retained' if value and not collected else ('stale' if value else 'missing'))})
        financials[-1]['latest_period_end'] = max((p['end'] for p in history.get('periods', []) if p.get('end')), default=None)
        market[-1].update(trade_at=quote.get('trade_at'), trade_age_hours=age_hours(quote.get('trade_at'), now))
        state = files['latest.json'].get('companies', {}).get(ticker, {})
        discovery.append({'ticker': ticker, 'checked_at': state.get('checked_at'),
                          'coverage_status': state.get('coverage_status', 'unknown'),
                          'sec_coverage_status': state.get('sec_coverage_status', 'unknown'),
                          'issuer_coverage_status': state.get('issuer_coverage_status', 'unknown'),
                          'source_checks': state.get('source_checks', [])})
    return {'max_retrieval_age_hours': max_age_hours,
            'financials': {'fresh_count': sum(r['fresh_retrieval'] for r in financials),
                           'company_count': len(financials), 'companies': financials},
            'market': {'fresh_count': sum(r['fresh_retrieval'] for r in market),
                       'company_count': len(market), 'companies': market},
            'discovery': discovery,
            'limits': ['Fresh retrieval is not proof that the latest report has been reviewed or that all filings are covered.',
                       'Quote retrieval time and last trade time are separate; prices may be delayed and exchanges close.']}


def execution_context(environ=None):
    environ = os.environ if environ is None else environ
    event = environ.get('GITHUB_EVENT_NAME', 'local')
    return {'event': event, 'run_id': environ.get('GITHUB_RUN_ID'),
            'run_attempt': environ.get('GITHUB_RUN_ATTEMPT'),
            'scheduled_execution_observed': event == 'schedule'}


def write_report(root, result):
    data.p.write_json(root / 'build/runtime-verification.json', result)
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY')
    if not summary_path:
        return
    rows = [('Verification', result['verification_status']),
            ('Workflow event', result['execution']['event']),
            ('Scheduled execution observed in this run', str(result['execution']['scheduled_execution_observed'])),
            ('Cold restore and backup equality', result.get('cold_restore', 'not_proven')),
            ('Collector checkpoint', result.get('refresh_status', 'not_proven'))]
    if result.get('sources'):
        for name in ('financials', 'market'):
            group = result['sources'][name]
            rows.append((name.capitalize() + ' fresh source retrievals', f"{group['fresh_count']}/{group['company_count']}"))
    if result.get('error'):
        rows.append(('Verification error', result['error']))
    safe = lambda value: str(value).replace('|', '\\|').replace('\n', ' ').replace('<', '&lt;').replace('>', '&gt;')
    lines = ['## Stock Brain runtime verification', '', '| Check | Evidence |', '| --- | --- |']
    lines.extend('| ' + safe(key) + ' | ' + safe(value) + ' |' for key, value in rows)
    lines.extend(['', 'A successful backup preserves the dated data. It does not make retained financials current or prove full disclosure coverage.', ''])
    with Path(summary_path).open('a') as stream:
        stream.write('\n'.join(lines))


def verify(root, url, check_answers=True):
    parsed = urlsplit(url)
    data.kb.need(parsed.scheme == 'https' and parsed.hostname and not parsed.username and not parsed.password,
                 'public HTTPS app URL required')
    url = url.rstrip('/')
    data.kb.need(data.fetch_json(url + '/healthz').get('status') == 'ok', 'service not healthy')
    status = data.fetch_json(url + '/api/status')
    live = data.validate_bundle(data.fetch_json(url + '/api/state'))
    age = (datetime.now(timezone.utc) - datetime.fromisoformat(live['files']['run-status.json']['completed_at'])).total_seconds()
    data.kb.need(-300 <= age <= 36 * 3600, 'collection checkpoint is older than 36 hours or future-dated')
    data.kb.need(status['scheduler']['enabled'], 'daily collector is disabled')
    data.kb.need((status.get('last_attempt') or {}).get('status') != 'failed', 'last collection failed')
    with tempfile.TemporaryDirectory(prefix='stock-brain-restore-proof-') as directory:
        store = data.StateStore(directory)
        data.kb.need(not store.path.exists(), 'restore test requires empty state')
        data.initialize(root, store, bootstrap=True)  # Actual immutable GitHub checkpoint, no mock.
        restored = store.read()['files']
        live_files = live['files']
        data.kb.need({e['id'] for e in live_files['latest.json']['queue']} <= {e['id'] for e in restored['latest.json']['queue']},
                     'backup is missing live disclosure events')
        data.kb.need({e['record_id'] for e in live_files['triage.json']['reviews']} <= {e['record_id'] for e in restored['triage.json']['reviews']},
                     'backup is missing review decisions')
        restored_by_ticker = {c['ticker']: c for c in restored['desk.json']['companies']}
        for company in live_files['desk.json']['companies']:
            saved = restored_by_ticker[company['ticker']]
            for key in ('history', 'quote'):
                data.kb.need(saved[key] == company[key], 'backup ' + key + ' differs from live ' + company['ticker'])
        audit = audit_financials.audit([c['history'] for c in restored_by_ticker.values()])
        queue_count = len(restored['latest.json']['queue'])
    if check_answers:
        for question, abstain in [('How does Microsoft make money?', False), ('Should I buy MSFT?', True)]:
            request = urllib.request.Request(url + '/api/ask', data=data.encode({'question': question}),
                headers={'Content-Type': 'application/json'}, method='POST')
            with urllib.request.urlopen(request, timeout=15) as response:
                answer = json.load(response)
            data.kb.need(answer.get('abstain') is abstain, 'unexpected answer eligibility')
            if not abstain:
                data.kb.need(bool(answer['statements']) and all(s['sources'] for s in answer['statements']), 'answer lacks citations')
    return {'service': 'stock-brain', 'verified_at': datetime.now(timezone.utc).isoformat(),
            'verification_status': 'pass', 'execution': execution_context(),
            'cold_restore': 'pass', 'restored_queue_count': queue_count, 'answer_api': 'pass' if check_answers else 'not_checked',
            'refresh_status': live['files']['run-status.json']['status'], 'financial_integrity': audit['integrity'],
            'open_financial_flags': audit['open_flag_count'], 'sec_collection_enabled': status.get('sec_collection_enabled'),
            'collector': {'checkpoint_completed_at': live['files']['run-status.json']['completed_at'],
                          'checkpoint_age_hours': round(age / 3600, 2), 'scheduler_enabled': status['scheduler']['enabled'],
                          'last_attempt_status': (status.get('last_attempt') or {}).get('status'),
                          'daily_schedule_delivery': 'not_established_by_this_check'},
            'sources': source_health(live['files'])}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', default=os.environ.get('STOCK_BRAIN_URL', 'https://finlotus-1.onrender.com'))
    parser.add_argument('--skip-answers', action='store_true', help='Migration diagnostic only; scheduled verification checks answers.')
    args = parser.parse_args()
    try:
        result = verify(data.kb.ROOT, args.url, not args.skip_answers)
    except (OSError, ValueError, KeyError, TypeError) as error:
        result = {'service': 'stock-brain', 'verified_at': datetime.now(timezone.utc).isoformat(),
                  'verification_status': 'failed', 'execution': execution_context(), 'error': str(error)}
        write_report(data.kb.ROOT, result)
        print(json.dumps(result))
        raise SystemExit(1)
    write_report(data.kb.ROOT, result)
    print(json.dumps(result))
