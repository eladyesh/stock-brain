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
            'cold_restore': 'pass', 'restored_queue_count': queue_count, 'answer_api': 'pass' if check_answers else 'not_checked',
            'refresh_status': live['files']['run-status.json']['status'], 'financial_integrity': audit['integrity'],
            'open_financial_flags': audit['open_flag_count'], 'sec_collection_enabled': status.get('sec_collection_enabled')}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', default=os.environ.get('STOCK_BRAIN_URL', 'https://finlotus-1.onrender.com'))
    parser.add_argument('--skip-answers', action='store_true', help='Migration diagnostic only; scheduled verification checks answers.')
    args = parser.parse_args()
    result = verify(data.kb.ROOT, args.url, not args.skip_answers)
    data.p.write_json(data.kb.ROOT / 'build/runtime-verification.json', result)
    print(json.dumps(result))
