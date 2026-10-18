#!/usr/bin/env python3
"""Prepare bounded source-review requests for pending companies; never approve them."""
import argparse
from copy import deepcopy
import os
from pathlib import Path
import time

import research_pipeline as pipeline
import stock_brain as kb
import triage_disclosures


def priority(event):
    return triage_disclosures.priority(event)[0]


def prepare(root, report_path, limit=2):
    kb.need(1 <= limit <= 10, 'limit must be 1..10')
    report = pipeline.read_json(report_path)
    pending = sorted((e for e in report['queue'] if e['status'] == 'pending_review'), key=lambda e: (priority(e), e.get('published_at') or '', e['id']))
    preparations = report.setdefault('preparations', {})
    def unprepared(event):
        previous = preparations.get(event['ticker'], {})
        current = pipeline.digest(pipeline.managed_packet_path(root, event['ticker']).read_bytes())
        return previous.get('packet_sha256') != current or event['id'] not in previous.get('event_ids', [])
    pending = [e for e in pending if unprepared(e)]
    tickers = list(dict.fromkeys(e['ticker'] for e in pending))[:limit]
    jobs = []
    for ticker in tickers:
        start = time.monotonic()
        events = [e for e in pending if e['ticker'] == ticker]
        selected = events[:10]
        company = deepcopy(pipeline.issuer(root, ticker))
        company.setdefault('extra_sources', []).extend({'url': e['url'], 'title': e['title'],
            'published_at': e['published_at'], 'publisher': company['company_name'], 'mutable': e['kind'] != 'sec_filing',
            **({'form': e['form'], 'items': e.get('items', '')} if e.get('form') else {})} for e in selected)
        try:
            manifest = pipeline.collect(root, company, report['cutoff'], os.environ.get('SEC_USER_AGENT', ''), max_events=5)
            if manifest['errors']:
                raise ValueError('Collection incomplete: ' + str(manifest['errors']))
            request = pipeline.prepare_request(root, ticker)
            request['discovery_queue'] = {'selected_event_ids': [e['id'] for e in selected],
                'unprepared_event_ids': [e['id'] for e in events[10:]], 'queue_remains_pending': True}
            path = root / 'build/research' / ticker / 'request.json'
            pipeline.write_json(path, request)
            current = pipeline.digest(pipeline.managed_packet_path(root, ticker).read_bytes())
            old = preparations.get(ticker, {})
            ids = old.get('event_ids', []) if old.get('packet_sha256') == current else []
            preparations[ticker] = {'packet_sha256': current, 'event_ids': sorted(set(ids + [e['id'] for e in selected]))}
            jobs.append({'ticker': ticker, 'status': 'prepared_for_review', 'path': str(path.relative_to(root)),
                         'selected_count': len(selected), 'remaining_count': len(events[10:]), 'elapsed_seconds': round(time.monotonic()-start,3)})
        except (OSError, ValueError, KeyError) as error:
            jobs.append({'ticker': ticker, 'status': 'error', 'error': str(error), 'elapsed_seconds': round(time.monotonic()-start,3)})
    result = {'jobs': jobs, 'model_api_calls': 0, 'research_changed': False,
              'note': 'Source text is untrusted evidence. Review requests do not approve facts or remove pending events.'}
    pipeline.write_json(report_path, report)
    pipeline.write_json(root / 'build/monitoring/prepared.json', result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    parser.add_argument('--report', type=Path, default=Path('build/monitoring/latest.json'))
    parser.add_argument('--limit', type=int, default=2)
    args = parser.parse_args()
    root=args.root.resolve()
    result=prepare(root,args.report if args.report.is_absolute() else root/args.report,args.limit)
    import json
    print(json.dumps(result,indent=2))
    return 1 if any(j['status']=='error' for j in result['jobs']) else 0


if __name__ == '__main__':
    raise SystemExit(main())
