#!/usr/bin/env python3
"""Refresh dated data and durable disclosure state without approving research.

Exit 1 means a partial refresh was safely exported; inspect run-status.json.
Exit 2 means publication is unsafe and no payload should be published.
"""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess

import build_desk
import disclosure_monitor as monitor
import financial_history as financials
import market_data
import research_pipeline as p
import stock_brain as kb
import triage_disclosures as triage

USER_AGENT = 'StockBrain/1.0 (https://github.com/eladyesh/stock-brain)'


def merge_reports(canonical, saved):
    """Keep both queues. Discovery will re-evaluate every status against research."""
    result = dict(saved)
    events = {e['id']: e for e in canonical.get('queue', [])}
    events.update({e['id']: e for e in saved.get('queue', [])})
    result['queue'] = list(events.values())
    return result


def merge_reviews(canonical, saved):
    reviews = {r['record_id']: r for r in canonical.get('reviews', [])}
    reviews.update({r['record_id']: r for r in saved.get('reviews', [])})
    return {**saved, 'reviews': list(reviews.values())}


def read_state_ref(root, ref, path):
    kb.need(bool(re.fullmatch(r'[A-Za-z0-9/_-]+', ref)), 'invalid state ref')
    command = subprocess.run(['git', 'show', ref + ':' + path], cwd=root, text=True, capture_output=True)
    kb.need(command.returncode == 0, 'Cannot restore ' + path + '; refusing to reset durable state.')
    return json.loads(command.stdout)


def restore_state(root, ref):
    snapshot = read_state_ref(root, ref, 'desk.json')
    report = read_state_ref(root, ref, 'latest.json')
    saved_triage = read_state_ref(root, ref, 'triage.json')
    previous_run = read_state_ref(root, ref, 'run-status.json')
    universe = {c['ticker']: c for c in p.universe(root)}
    kb.need(snapshot.get('schema_version') == 1 and
            {c['ticker'] for c in snapshot['companies']} == set(universe),
            'saved snapshot universe mismatch')
    kb.need(isinstance(report.get('queue'), list), 'saved queue is invalid')
    # Parse and validate all required payloads before changing local state.
    for company in snapshot['companies']:
        ticker = company['ticker']
        if company.get('history'):
            kb.need(company['history']['company_id'] == 'company-cik-' + universe[ticker]['cik'], 'saved history issuer mismatch')
            financials.validate_history(company['history'])
        if company.get('quote'):
            kb.need(company['quote']['ticker'] == ticker, 'saved price issuer mismatch')
    for company in snapshot['companies']:
        ticker = company['ticker']
        for folder, key, timestamp in [('financials', 'history', 'source'), ('market', 'quote', 'retrieved_at')]:
            value = company.get(key)
            if not value:
                continue
            path = root / 'research' / folder / (ticker + '.json')
            old = p.read_json(path) if path.exists() else None
            stamp = lambda row: (row.get('source', {}).get('retrieved_at', '') if timestamp == 'source' else row.get(timestamp, ''))
            if not old or stamp(value) >= stamp(old):
                p.write_json(path, value)
    report_path = root / 'research/monitoring/latest.json'
    canonical = p.read_json(report_path) if report_path.exists() else {}
    p.write_json(report_path, merge_reports(canonical, report))
    triage_path = root / 'research/monitoring/triage.json'
    canonical_triage = p.read_json(triage_path) if triage_path.exists() else {}
    p.write_json(triage_path, merge_reviews(canonical_triage, saved_triage))
    return previous_run


def collect_financials(root, cutoff):
    fetcher = p.Fetcher(root, os.environ.get('SEC_USER_AGENT') or USER_AGENT)
    results = []
    for company in p.universe(root):
        try:
            raw, meta = fetcher.fetch('https://data.sec.gov/api/xbrl/companyfacts/CIK' + company['cik'] + '.json', refresh=True)
            history = financials.normalize_companyfacts(json.loads(raw), company, cutoff, meta, 5, 12)
            p.write_json(root / 'research/financials' / (company['ticker'] + '.json'), history)
            results.append({'ticker': company['ticker'], 'status': 'collected',
                            'as_of': cutoff, 'qa_flags': len(history['qa_flags'])})
        except (ValueError, OSError, KeyError, TypeError) as error:
            results.append({'ticker': company['ticker'], 'status': 'error', 'error': str(error),
                            'previous_data_retained': True})
    return results


def refresh(root, output, previous_run=None):
    kb.export_records(root)  # Review bindings must remain valid before any publication.
    now = datetime.now(timezone.utc)
    cutoff = now.date().isoformat()
    previous_run = previous_run or {}
    run = {'schema_version': 1, 'started_at': now.isoformat(), 'cutoff': cutoff,
           'research_changed': False, 'research_automatically_approved': False, 'model_api_calls': 0}
    report_path = root / 'research/monitoring/latest.json'
    previous = p.read_json(report_path)
    # A broken top-level discovery read must not replace the durable queue.
    try:
        report = monitor.run(root, os.environ.get('SEC_USER_AGENT') or USER_AGENT, cutoff, previous)
        p.write_json(report_path, report)
        run['discovery'] = {ticker: {'status': state['status'], 'coverage_status': state.get('coverage_status'),
                                     'errors': state.get('errors', [])}
                            for ticker, state in report['companies'].items()}
    except (OSError, ValueError, KeyError, TypeError) as error:
        report = previous
        run['discovery'] = {'error': str(error), 'previous_data_retained': True}
    # Keep the local assistant and export on the same queue version.
    p.write_json(root / 'build/monitoring/latest.json', report)
    triage_path = root / 'research/monitoring/triage.json'
    prior_triage = p.read_json(triage_path) if triage_path.exists() else {}
    p.write_json(triage_path, triage.triage(root, report, prior_triage))
    run['financials'] = collect_financials(root, cutoff)
    run['market'] = market_data.collect(root)['results']
    failed = ('error' in run['discovery'] or
              any(s.get('coverage_status') != 'checked' for s in run['discovery'].values() if isinstance(s, dict)) or
              any(s['status'] == 'error' for s in run['financials'] + run['market']))
    run['status'] = 'partial' if failed else 'complete'
    run['completed_at'] = datetime.now(timezone.utc).isoformat()
    run['pending_count'] = p.read_json(triage_path)['summary']['pending']
    prior_days = {r['cutoff']: r for r in previous_run.get('run_history', [])}
    prior_days[cutoff] = {k: run[k] for k in ['cutoff', 'completed_at', 'status', 'pending_count']}
    run['run_history'] = sorted(prior_days.values(), key=lambda r: r['cutoff'])[-30:]
    p.write_json(root / 'research/monitoring/refresh-status.json', run)
    output.mkdir(parents=True, exist_ok=True)
    snapshot = build_desk.build(root, output / 'desk.json')
    for name, value in [('latest.json', report), ('triage.json', p.read_json(triage_path)), ('run-status.json', run)]:
        p.write_json(output / name, value)
    # One payload manifest supports either authenticated Git or the connected GitHub API.
    payloads = [output / name for name in ['desk.json', 'latest.json', 'triage.json', 'run-status.json']]
    kb.need(all(path.is_file() and path.stat().st_size > 0 for path in payloads), 'incomplete publication payload')
    manifest = [{'path': path.name, 'local_path': str(path.resolve()), 'sha256': p.digest(path.read_bytes()),
                 'bytes': path.stat().st_size} for path in payloads]
    p.write_json(output / 'publish-manifest.json', {'target_branch': 'automation/research-data',
                 'built_at': snapshot['built_at'], 'files': manifest,
                 'publication_safe': True, 'refresh_status': run['status']})
    return run


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    parser.add_argument('--output', type=Path, default=Path('build/publish'))
    parser.add_argument('--restore-ref', help='Previously fetched automation/research-data Git ref; required on subsequent runs.')
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    try:
        previous = restore_state(root, args.restore_ref) if args.restore_ref else None
        run = refresh(root, output, previous)
        print(json.dumps({'status': run['status'], 'pending_count': run['pending_count'],
                          'publish_manifest': str(output / 'publish-manifest.json'),
                          'research_changed': False}))
        return 0 if run['status'] == 'complete' else 1
    except (ValueError, OSError, KeyError, TypeError) as error:
        # Remove the publish signal so a previous successful payload cannot be mistaken for this run.
        (output / 'publish-manifest.json').unlink(missing_ok=True)
        print(json.dumps({'publication_safe': False, 'error': str(error)}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())

