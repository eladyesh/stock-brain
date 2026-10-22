#!/usr/bin/env python3
"""Run bounded, restartable coverage cycles without an interactive chat session.

One pass is the default. --continuous explicitly enables repeated work. This
process shares one durable SQLite file with the web app and other local workers;
it is not started by web requests or the small pilot's daily refresh supervisor.
"""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import signal
import sqlite3
import threading
from types import SimpleNamespace
import uuid

import coverage_cli
from coverage_store import CoverageStore
from coverage_worker import CoverageWorker, SecFinancialProvider, utc_now
import stock_brain as kb


def listing_refresh_due(store, now):
    latest = store.stats().get('last_listing_import') or {}
    stamp = (latest.get('source') or {}).get('retrieved_at')
    if not stamp:
        return True
    retrieved = datetime.fromisoformat(stamp.replace('Z', '+00:00'))
    return (now.astimezone(timezone.utc) - retrieved).total_seconds() >= 86400


def run_cycle(store, provider, *, root=kb.ROOT, limit=25, worker_id='coverage-cycle',
              refresh_listings=False, now=None, listing_loader=coverage_cli.load_import):
    if type(limit) is not int or not 1 <= limit <= 100:
        raise ValueError('cycle limit must be 1..100')
    now = now or utc_now()
    worker = CoverageWorker(store, provider, root=root)
    ready = provider.readiness()
    report = {'started_at': now.isoformat(), 'provider': ready, 'queued': 0,
              'listing_import': None, 'worker': None, 'stopped_reason': ready.get('reason')}
    if not ready['ready']:
        return report
    if refresh_listings and listing_refresh_due(store, now):
        args = SimpleNamespace(fetch=True, root=Path(root), source_url=None, retrieved_at=None,
                               complete_snapshot=False, exclude_otc=False, exclude_unassigned_exchange=False)
        try:
            payload, source, _ = listing_loader(args, store=store)
            # Absence-based retirement requires a separate explicit complete import.
            report['listing_import'] = store.import_listings(payload, source, complete=False)
        except (ValueError, OSError, KeyError) as error:
            report['stopped_reason'] = 'Listing refresh failed; existing registry retained: ' + str(error)[:1000]
            return report
    ready = provider.readiness()
    if not ready['ready']:
        report['stopped_reason'] = ready['reason']
        return report
    report['queued'] = coverage_cli.enqueue(store, limit=limit)['selected']
    report['worker'] = worker.run(worker_id, limit=limit)
    report['stopped_reason'] = report['worker']['stopped_reason']
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=os.environ.get('STOCK_BRAIN_COVERAGE_DB'),
                        help='Shared database on durable local storage; required here or in STOCK_BRAIN_COVERAGE_DB')
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    parser.add_argument('--limit', type=int, default=25)
    parser.add_argument('--worker-id', default='cycle-' + uuid.uuid4().hex[:12])
    parser.add_argument('--continuous', action='store_true')
    parser.add_argument('--interval-seconds', type=int, default=60,
                        help='Delay after each cycle, at least 60 seconds')
    parser.add_argument('--refresh-listings', action='store_true',
                        help='Explicitly fetch the official SEC association file at most once per successful 24-hour interval')
    parser.add_argument('--readiness', action='store_true', help='Configuration only; no enqueue, claim or network request')
    args = parser.parse_args(argv)
    if not args.db:
        parser.error('--db or STOCK_BRAIN_COVERAGE_DB is required')
    if not 1 <= args.limit <= 100 or not 60 <= args.interval_seconds <= 86400:
        parser.error('--limit must be 1..100 and --interval-seconds must be 60..86400')
    stopped = threading.Event()
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda *_: stopped.set())
    try:
        store = CoverageStore(args.db)
        provider = SecFinancialProvider(args.root, store=store)
        if args.readiness:
            print(json.dumps({'provider': provider.readiness(), 'registry': store.stats(),
                              'network_checked': False}, ensure_ascii=False), flush=True)
            return 0
        while not stopped.is_set():
            report = run_cycle(store, provider, root=args.root, limit=args.limit, worker_id=args.worker_id,
                               refresh_listings=args.refresh_listings)
            print(json.dumps(report, ensure_ascii=False, allow_nan=False), flush=True)
            if not args.continuous:
                return 1 if report['stopped_reason'] or (report['worker'] or {}).get('failed') else 0
            stopped.wait(args.interval_seconds)
        return 0
    except (ValueError, OSError, KeyError, sqlite3.Error) as error:
        print(json.dumps({'error': str(error), 'previous_payloads_retained': True}), flush=True)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
