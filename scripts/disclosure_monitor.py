#!/usr/bin/env python3
"""Discover SEC filings and configured issuer feeds; never approve research."""
from datetime import date, datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
import argparse
import hashlib
import html
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


def public_url(url):
    parsed = urllib.parse.urlparse(url)
    return bool(parsed.scheme == 'https' and parsed.hostname and not parsed.username and not parsed.password)


def publication_date(value):
    if not isinstance(value, str) or not value.strip():
        return None
    value = value.strip()
    for parse in (lambda s: datetime.fromisoformat(s.replace('Z', '+00:00')),
                  parsedate_to_datetime,
                  lambda s: datetime.strptime(s, '%m/%d/%Y %H:%M:%S')):
        try:
            return parse(value).date().isoformat()
        except (ValueError, TypeError, AttributeError):
            continue
    return None


def parse_feed_details(raw, ticker, feed_url):
    """Reject HTTP-200 error pages; return warnings for incomplete real feeds."""
    kb.need(len(raw) <= 2_000_000, 'feed exceeds 2 MB')
    kb.need(b'<!DOCTYPE' not in raw.upper(), 'feed contains an unexpected document type')
    root = ET.fromstring(raw)
    if root.tag == 'rss':
        kb.need(root.find('channel') is not None, 'RSS channel is missing')
        nodes = root.findall('./channel/item')
    elif root.tag == '{http://www.w3.org/2005/Atom}feed':
        nodes = root.findall('{http://www.w3.org/2005/Atom}entry')
    else:
        raise ValueError('source is not an RSS or Atom feed (an HTML error page is not an empty feed)')
    result, skipped = [], 0
    for node in nodes:
        def field(name):
            child = node.find(name)
            if child is None:
                child = node.find('{http://www.w3.org/2005/Atom}' + name)
            return child
        title = field('title')
        link = field('link')
        if link is None:
            skipped += 1
            continue
        url = (link.get('href') or link.text or '').strip()
        if not public_url(url):
            skipped += 1
            continue
        stamp = next((field(n) for n in ('pubDate', 'published', 'updated') if field(n) is not None), None)
        published = publication_date(stamp.text if stamp is not None else None)
        result.append({'id': event_id(ticker, url), 'ticker': ticker, 'url': url,
                       'title': ''.join(title.itertext()).strip() if title is not None else 'Issuer disclosure',
                       'published_at': published, 'kind': 'issuer_feed', 'discovered_from': feed_url})
    warnings = []
    if not nodes:
        warnings.append('The feed contains no entries; issuer announcement coverage could not be confirmed.')
    if skipped:
        warnings.append(f'{skipped} feed entries had no usable public HTTPS link.')
    if any(e['published_at'] is None for e in result):
        warnings.append('Some entries have no usable publication date and remain review candidates.')
    return result, warnings


def parse_feed(raw, ticker, feed_url):
    return parse_feed_details(raw, ticker, feed_url)[0]


def parse_q4_news(raw, ticker, source_url):
    """Read the public JSON list used by the issuer's own news page."""
    kb.need(len(raw) <= 10_000_000, 'issuer news JSON exceeds 10 MB')
    payload = json.loads(raw)
    kb.need(isinstance(payload, dict) and isinstance(payload.get('GetPressReleaseListResult'), list),
            'issuer news JSON list is missing')
    rows = payload['GetPressReleaseListResult']
    events, warnings, skipped = [], [], 0
    for row in rows:
        kb.need(isinstance(row, dict), 'invalid issuer news entry')
        link = row.get('LinkToDetailPage')
        title = row.get('Headline')
        if not isinstance(link, str) or not link.strip() or not isinstance(title, str) or not title.strip():
            skipped += 1
            continue
        url = urllib.parse.urljoin(source_url, link)
        if not public_url(url):
            skipped += 1
            continue
        events.append({'id': event_id(ticker, url), 'ticker': ticker, 'url': url,
                       'title': html.unescape(title).strip(), 'published_at': publication_date(row.get('PressReleaseDate')),
                       'kind': 'issuer_announcement', 'discovered_from': source_url})
    if not rows:
        warnings.append('The issuer news list contains no entries; announcement coverage could not be confirmed.')
    if skipped:
        warnings.append(f'{skipped} issuer news entries were missing a valid title or public HTTPS link.')
    if any(e['published_at'] is None for e in events):
        warnings.append('Some issuer news entries have no usable publication date.')
    return events, warnings


def issuer_sources(config, ticker, since, cutoff):
    result = [{'kind': 'rss', 'url': url} for url in config.get('issuer_feeds', {}).get(ticker, [])]
    for adapter in config.get('issuer_adapters', {}).get(ticker, []):
        kb.need(adapter.get('kind') == 'q4_news', 'unsupported issuer announcement adapter')
        base = adapter['url']
        kb.need(public_url(base) and '{year}' in base, 'issuer news adapter requires an HTTPS year template')
        years = range(date.fromisoformat(since).year, date.fromisoformat(cutoff).year + 1)
        kb.need(len(years) <= 4, 'issuer news history exceeds four years')
        result.extend({'kind': 'q4_news', 'url': base.replace('{year}', str(year))} for year in years)
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


def reconciled_queue(old, found, packets, reviewed, checked_at, dispositions=None):
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
        # An explicit, hash-bound source review may close a nonmaterial disclosure.
        # Metadata triage, title similarity and preparation never resolve anything.
        decision = (dispositions or {}).get(event['id'])
        event.pop('resolved_by_triage_review', None)
        if event['status'] == 'pending_review' and decision:
            event.update(status='reviewed_disposition', resolved_by_triage_review=decision['record_id'],
                         resolution_basis=decision['disposition'] + ': ' + decision['reason'])
    return sorted(queue.values(), key=lambda e: (e.get('published_at') or '', e['ticker'], e['id']), reverse=True)


def run(root, user_agent, cutoff=None, previous=None, fetcher=None):
    cutoff = cutoff or date.today().isoformat()
    kb.need(date.fromisoformat(cutoff) <= date.today(), 'discovery cutoff cannot be in the future')
    now = utc_now()
    fetcher = fetcher or pipeline.Fetcher(root, user_agent)
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
        errors, checks = [], []
        since = (date.fromisoformat(packet['as_of']) - timedelta(days=overlap)).isoformat()
        try:
            sec_events = discover_sec(company, packet, fetcher, cutoff, since)
            found.extend(sec_events)
            checks.append({'source': 'SEC submissions', 'kind': 'sec', 'status': 'checked',
                           'candidate_count': len(sec_events)})
        except (OSError, ValueError, KeyError) as error:
            errors.append({'source': 'SEC submissions', 'error': str(error)})
            checks.append({'source': 'SEC submissions', 'kind': 'sec', 'status': 'error'})
        sources = issuer_sources(config, ticker, since, cutoff)
        for source in sources:
            url = source['url']
            try:
                raw, meta = fetcher.fetch(url, refresh=True)
                parser = parse_feed_details if source['kind'] == 'rss' else parse_q4_news
                events, warnings = parser(raw, ticker, url)
                selected = [e for e in events if e['published_at'] is None or since <= e['published_at'] <= cutoff]
                found.extend(selected)
                checks.append({'source': url, 'kind': source['kind'], 'status': 'partial' if warnings else 'checked',
                               'entry_count': len(events), 'candidate_count': len(selected), 'warnings': warnings,
                               'source_sha256': meta.get('sha256') or pipeline.digest(raw),
                               'latest_publication': max((e['published_at'] for e in events if e['published_at']), default=None)})
            except (OSError, ValueError, ET.ParseError) as error:
                errors.append({'source': url, 'error': str(error)})
                checks.append({'source': url, 'kind': source['kind'], 'status': 'error'})
        coverage = 'error' if errors else ('partial' if not sources or any(c['status'] == 'partial' for c in checks) else 'checked')
        states[ticker] = {'checked_at': now, 'packet_sha256': pipeline.digest(packet_path.read_bytes()),
                          'status': coverage, 'coverage_status': coverage, 'errors': errors, 'source_checks': checks,
                          'scope': 'SEC filings and configured public issuer announcement sources',
                          'issuer_feed_count': len(config.get('issuer_feeds', {}).get(ticker, [])),
                          'issuer_source_count': len(sources), 'discovery_since': since,
                          'coverage_note': config.get('coverage_notes', {}).get(ticker),
                          'limits': ['Unfiled announcements are covered only when present in a configured issuer source; rolling feeds may not cover the full overlap interval.',
                                     'Discovery identifies review candidates; it does not read or approve their claims.']}
    prior = [e for e in (previous or {}).get('queue', []) if e['ticker'] in packets]
    queue = reconciled_queue(prior, found, packets, reviewed, now)
    from triage_disclosures import active_dispositions
    dispositions = active_dispositions(root, queue, packets, reviewed)
    queue = reconciled_queue(queue, [], packets, reviewed, now, dispositions)
    for ticker, state in states.items():
        count = sum(e['ticker'] == ticker and e['status'] == 'pending_review' for e in queue)
        state['pending_count'] = count
        state['reviewed_disposition_count'] = sum(e['ticker'] == ticker and e['status'] == 'reviewed_disposition' for e in queue)
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
            'coverage_status': state.get('coverage_status', state['status']),
            'reviewed_disposition_count': state.get('reviewed_disposition_count', 0),
            'scope': state.get('scope'), 'message': 'Dated research snapshot; discovery and triage do not renew its research or review date.'}


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
        partial = [t for t, s in result['companies'].items() if s.get('coverage_status') == 'partial']
        print(json.dumps({'output': str(output), 'pending': len(pending), 'failed_issuers': errors,
                          'partial_issuers': partial, 'errors': {t: result['companies'][t]['errors'] for t in errors}}))
        if args.summary:
            lines = ['# Stock Brain disclosure review queue', '', f"Checked: {result['checked_at']}",
                     f'Pending disclosures: {len(pending)}. Failed issuer checks: {len(errors)}. Partial issuer checks: {len(partial)}.', '',
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
            if partial:
                lines.append('\nPartial announcement coverage: ' + ', '.join(partial))
            args.summary.write_text('\n'.join(lines) + '\n')
        return 1 if errors or partial else 0
    except (OSError, ValueError, KeyError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
