#!/usr/bin/env python3
"""Discover SEC filings and configured issuer feeds; never approve research."""
from datetime import date, datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET

import research_pipeline as pipeline
import stock_brain as kb

FORMS = {'10-K', '10-K/A', '10-Q', '10-Q/A', '20-F', '20-F/A', '40-F', '40-F/A',
         '8-K', '8-K/A', '6-K', '6-K/A', 'DEF 14A', 'DEFA14A'}


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def accession(url):
    match = re.search(r'/edgar/data/\d+/(\d{18})/', url)
    return match[1] if match else None


def event_id(ticker, url):
    return hashlib.sha256((ticker + '|' + url).encode()).hexdigest()[:24]


def parse_feed(raw, ticker, feed_url):
    kb.need(len(raw) <= 2_000_000, 'feed exceeds 2 MB')
    root = ET.fromstring(raw)
    result = []
    for node in list(root.findall('.//item')) + list(root.findall('{http://www.w3.org/2005/Atom}entry')):
        def field(name):
            child = node.find(name)
            if child is None:
                child = node.find('{http://www.w3.org/2005/Atom}' + name)
            return child
        title = field('title')
        link = field('link')
        if link is None:
            continue
        url = (link.get('href') or link.text or '').strip()
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme != 'https' or not parsed.hostname or parsed.username:
            continue
        stamp = next((field(n) for n in ('pubDate', 'published', 'updated') if field(n) is not None), None)
        published = None
        if stamp is not None and stamp.text:
            try:
                published = datetime.fromisoformat(stamp.text.replace('Z', '+00:00')).date().isoformat()
            except ValueError:
                try:
                    published = parsedate_to_datetime(stamp.text).date().isoformat()
                except (ValueError, TypeError):
                    pass
        result.append({'id': event_id(ticker, url), 'ticker': ticker, 'url': url,
                       'title': ''.join(title.itertext()).strip() if title is not None else 'Issuer disclosure',
                       'published_at': published, 'kind': 'issuer_feed', 'discovered_from': feed_url})
    return result


def discover_sec(company, packet, fetcher, cutoff, since=None):
    since = since or packet['as_of']
    url = f"https://data.sec.gov/submissions/CIK{company['cik']}.json"
    raw, _ = fetcher.fetch(url, refresh=True)
    data = json.loads(raw)
    kb.need(str(data.get('cik', '')).zfill(10) == company['cik'], 'SEC issuer identity mismatch')
    recent = data.get('filings', {}).get('recent')
    kb.need(isinstance(recent, dict) and isinstance(recent.get('form'), list), 'SEC recent filings structure is missing')
    kb.need(all(isinstance(recent.get(k), list) and len(recent[k]) == len(recent['form']) for k in ('filingDate', 'accessionNumber', 'primaryDocument')), 'SEC filing arrays are inconsistent')
    rows = pipeline.filing_rows(data)
    archives = [a for a in data.get('filings', {}).get('files', [])
                if a.get('filingTo', '9999') >= since and a.get('filingFrom', '0000') <= cutoff]
    kb.need(len(archives) <= 12, 'discovery history exceeds 12 archives; narrow the research cutoff after review')
    for item in archives:
        name = item['name']
        kb.need(bool(re.fullmatch(r'CIK\d+-submissions-\d+\.json', name)), 'unexpected SEC archive filename')
        raw, _ = fetcher.fetch('https://data.sec.gov/submissions/' + name)
        rows.extend(pipeline.filing_rows(json.loads(raw)))
    sources = {s['url'] for s in packet['sources']}
    known = {accession(s) for s in sources} - {None}
    events = []
    for row in rows:
        if row['form'] not in FORMS or not since <= row.get('filingDate', '') <= cutoff:
            continue
        acc = row['accessionNumber'].replace('-', '')
        kb.need(bool(re.fullmatch(r'\d{18}', acc)), 'invalid filing accession')
        if acc in known:
            continue
        doc = row['primaryDocument']
        kb.need(not doc.startswith('/') and '..' not in doc.split('/'), 'invalid SEC document path')
        link = f"https://www.sec.gov/Archives/edgar/data/{int(company['cik'])}/{acc}/{doc}"
        events.append({'id': event_id(company['ticker'], link), 'ticker': company['ticker'], 'url': link,
                       'title': f"{company['ticker']} {row['form']} filed {row['filingDate']}",
                       'published_at': row['filingDate'], 'kind': 'sec_filing', 'form': row['form'],
                       'accession': acc, 'items': row.get('items', ''), 'discovered_from': url})
    return events


def reconciled_queue(old, found, packets, reviewed, checked_at):
    # Merge; disappearing from a feed is not evidence that an event was reviewed.
    queue = {e['id']: dict(e) for e in old}
    for event in found:
        queue[event['id']] = {**queue.get(event['id'], {}), **event,
                             'first_seen_at': queue.get(event['id'], {}).get('first_seen_at', checked_at)}
    for event in queue.values():
        packet = packets[event['ticker']]
        urls = {s['url'] for s in packet['sources']}
        covered = event['url'] in urls or (event['kind'] == 'sec_filing' and event.get('accession') in
                                         {accession(url) for url in urls} - {None})
        approved = reviewed.get(event['ticker'])
        if covered and approved:
            event.update(status='reviewed', resolved_by_profile_sha256=approved,
                         resolution_basis='Source or SEC filing accession included in the hash-bound reviewed packet.')
        else:
            event['status'] = 'pending_review'
            event.pop('resolved_by_profile_sha256', None)
            event.pop('resolution_basis', None)
    return sorted(queue.values(), key=lambda e: (e.get('published_at') or '', e['ticker'], e['id']), reverse=True)


def run(root, user_agent, cutoff=None, previous=None):
    cutoff = cutoff or date.today().isoformat()
    kb.need(date.fromisoformat(cutoff) <= date.today(), 'discovery cutoff cannot be in the future')
    now = utc_now()
    fetcher = pipeline.Fetcher(root, user_agent)
    docs = kb.documents(root)
    from review_gates import check_managed_reviews
    check_managed_reviews(root, docs)
    packets, found, states, reviewed = {}, [], {}, {}
    config_path = root / 'config/discovery.json'
    config = pipeline.read_json(config_path) if config_path.exists() else {'issuer_feeds': {}}
    overlap = config.get('overlap_days', 90)
    kb.need(type(overlap) is int and 1 <= overlap <= 730, 'overlap_days must be 1..730')
    for company in pipeline.universe(root):
        ticker = company['ticker']
        packet_path = pipeline.managed_packet_path(root, ticker)
        if not packet_path.exists():
            continue
        packet = pipeline.read_json(packet_path)
        packets[ticker] = packet
        doc = next(d for d in docs if d.metadata['ticker'] == ticker)
        if doc.metadata['status'] == 'reviewed':
            reviewed[ticker] = pipeline.digest(doc.path.read_bytes())
        errors = []
        since = (date.fromisoformat(packet['as_of']) - timedelta(days=overlap)).isoformat()
        try:
            found.extend(discover_sec(company, packet, fetcher, cutoff, since))
        except (OSError, ValueError, KeyError) as error:
            errors.append({'source': 'SEC submissions', 'error': str(error)})
        feeds = config.get('issuer_feeds', {}).get(ticker, [])
        for feed in feeds:
            try:
                raw, _ = fetcher.fetch(feed, refresh=True)
                found.extend(e for e in parse_feed(raw, ticker, feed)
                             if e['published_at'] is None or since <= e['published_at'] <= cutoff)
            except (OSError, ValueError, ET.ParseError) as error:
                errors.append({'source': feed, 'error': str(error)})
        states[ticker] = {'checked_at': now, 'packet_sha256': pipeline.digest(packet_path.read_bytes()),
                          'status': 'error' if errors else ('checked' if feeds else 'partial'), 'errors': errors,
                          'scope': 'SEC filings and configured issuer feeds', 'issuer_feed_count': len(feeds), 'discovery_since': since,
                          'coverage_note': config.get('coverage_notes', {}).get(ticker),
                          'limits': ['Unfiled announcements are covered only when present in a configured issuer feed.',
                                     'Discovery identifies review candidates; it does not read or approve their claims.']}
    prior = [e for e in (previous or {}).get('queue', []) if e['ticker'] in packets]
    queue = reconciled_queue(prior, found, packets, reviewed, now)
    for ticker, state in states.items():
        count = sum(e['ticker'] == ticker and e['status'] == 'pending_review' for e in queue)
        state['pending_count'] = count
        if count and state['status'] in {'checked', 'partial'}:
            state['status'] = 'needs_review'
    return {'schema_version': 1, 'checked_at': now, 'cutoff': cutoff, 'companies': states, 'queue': queue,
            'research_changed': False, 'model_api_calls': 0,
            'preparations': (previous or {}).get('preparations', {})}


def freshness(root, ticker, report, now=None, max_age_hours=48):
    now = now or datetime.now(timezone.utc)
    state = (report or {}).get('companies', {}).get(ticker)
    if not state:
        return {'status': 'unknown', 'message': 'No discovery check is available.', 'pending_count': None}
    try:
        checked = datetime.fromisoformat(state['checked_at'])
        hours = (now - checked).total_seconds() / 3600
        packet = pipeline.managed_packet_path(root, ticker)
        if state.get('packet_sha256') != pipeline.digest(packet.read_bytes()):
            return {'status': 'unknown', 'message': 'Discovery was checked against another evidence version.', 'pending_count': state.get('pending_count')}
        if hours < -1 or hours > max_age_hours:
            return {'status': 'stale_check', 'message': 'The discovery check is expired.', 'pending_count': state.get('pending_count')}
    except (KeyError, ValueError, OSError, TypeError):
        return {'status': 'unknown', 'message': 'Discovery metadata is invalid.', 'pending_count': None}
    if (report or {}).get('cutoff') != checked.date().isoformat():
        return {'status': 'unknown', 'message': 'Historical discovery is not a current check.', 'pending_count': state.get('pending_count')}
    return {'status': state['status'], 'checked_at': state['checked_at'], 'pending_count': state.get('pending_count'),
            'scope': state.get('scope'), 'message': 'Dated research snapshot; discovery is not an exhaustive news review.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    parser.add_argument('--as-of', default=date.today().isoformat())
    parser.add_argument('--output', type=Path, default=Path('build/monitoring/latest.json'))
    parser.add_argument('--summary', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    try:
        seed = root / 'research/monitoring/latest.json'
        previous = pipeline.read_json(output) if output.exists() else (pipeline.read_json(seed) if seed.exists() else None)
        result = run(root, os.environ.get('SEC_USER_AGENT', ''), args.as_of, previous)
        pipeline.write_json(output, result)
        pending = [e for e in result['queue'] if e['status'] == 'pending_review']
        errors = [t for t, s in result['companies'].items() if s['status'] == 'error']
        print(json.dumps({'output': str(output), 'pending': len(pending), 'failed_issuers': errors, 'errors': {t: result['companies'][t]['errors'] for t in errors}}))
        if args.summary:
            lines = ['# Stock Brain disclosure review queue', '', f"Checked: {result['checked_at']}",
                     f'Pending disclosures: {len(pending)}. Failed issuer checks: {len(errors)}.', '',
                     'Discovery never changes research or review status.', '']
            for event in pending:
                title = event['title'].replace('\n', ' ').replace('[', '').replace(']', '').replace('<', '').replace('>', '')
                lines.append(f"- {event['ticker']} — {title} — {event['url']}")
            if errors:
                lines.append('\nFailed checks: ' + ', '.join(errors))
                for ticker in errors:
                    for error in result['companies'][ticker]['errors']:
                        detail = str(error['error']).replace('\n', ' ').replace('<', '').replace('>', '')
                        lines.append(f"- {ticker}: {error['source']} — {detail}")
            args.summary.write_text('\n'.join(lines) + '\n')
        return 1 if errors else 0
    except (OSError, ValueError, KeyError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
