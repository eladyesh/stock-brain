#!/usr/bin/env python3
"""Prioritize disclosure metadata; retain explicit source-review decisions separately."""
from collections import Counter
from datetime import datetime, timezone
import argparse
import json
import os
from pathlib import Path
import re
import urllib.parse

import research_pipeline as pipeline
import stock_brain as kb

DISPOSITIONS = {'irrelevant', 'no_material_change', 'duplicate'}
EVENT_FIELDS = ('id', 'ticker', 'url', 'title', 'published_at', 'kind', 'form', 'accession', 'items')


def event_digest(event):
    return pipeline.digest(json.dumps({k: event.get(k) for k in EVENT_FIELDS}, sort_keys=True, ensure_ascii=False))


def canonical_url(url):
    parsed = urllib.parse.urlsplit(url)
    query = [(k, v) for k, v in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
             if not k.lower().startswith('utm_')]
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path,
                                   urllib.parse.urlencode(query), ''))


def priority(event):
    """A routing heuristic, not a conclusion about financial materiality."""
    form = event.get('form', '')
    items = {v.strip() for v in event.get('items', '').split(',')}
    title = event.get('title', '').lower()
    if form in {'10-K', '10-K/A', '10-Q', '10-Q/A', '20-F', '20-F/A', '40-F', '40-F/A'}:
        return 0, 'Annual or interim financial filing.'
    if '2.02' in items or re.search(r'\b(reports?|announces?)\b.*\b(results|dividend)\b', title):
        if not re.search(r'\b(date|to report|to release)\b', title):
            return 0, 'Results or capital-return disclosure indicated by filing items/headline.'
    if form or re.search(r'\b(acquir\w*|merger|contract|awarded|debt|financing|divest\w*|appoint\w*|president|ceo|cfo)\b', title):
        return 1, 'Filing, transaction, contract, financing or leadership review candidate.'
    if re.search(r'\b(earnings.*(date|webcast)|date.*earnings|to report|to release|conference|celebrat\w*|pop-up|merchandise|tutorial)\b', title):
        return 3, 'Scheduling, event or editorial headline; still pending a source-based review.'
    return 2, 'Product, partnership or other issuer announcement; materiality is undetermined.'


def record_digest(record):
    return pipeline.digest(json.dumps({k: v for k, v in record.items() if k != 'record_id'},
                                      sort_keys=True, ensure_ascii=False))[:24]


def validate_record(record, event, packet_hash, profile_hash, sections):
    kb.need(record.get('disposition') in DISPOSITIONS, 'unsupported reviewed disposition')
    kb.need(record.get('event_id') == event['id'] and record.get('event_sha256') == event_digest(event),
            'triage review refers to another event version')
    kb.need(profile_hash and record.get('profile_sha256') == profile_hash and record.get('packet_sha256') == packet_hash,
            'triage review requires the current hash-bound reviewed research')
    kb.need(record.get('reviewer_type') in {'human', 'ai'} and kb.scalar(record.get('reviewer')),
            'an explicit human or AI reviewer identity is required')
    kb.need(isinstance(record.get('reason'), str) and len(record['reason'].strip()) >= 30,
            'a substantive source-based disposition reason is required')
    checked = record.get('sections_checked')
    kb.need(isinstance(checked, list) and checked and set(checked) <= set(sections),
            'identify the current research sections checked against this disclosure')
    kb.need(record.get('source_read_in_full') is True, 'a full-source review attestation is required')
    stamp = datetime.fromisoformat(record.get('reviewed_at', ''))
    kb.need(stamp.tzinfo is not None and stamp <= datetime.now(timezone.utc), 'invalid or future triage review time')
    evidence = record.get('evidence')
    kb.need(isinstance(evidence, list) and evidence, 'source bindings are required')
    for source in evidence:
        parsed = urllib.parse.urlparse(source.get('url', ''))
        kb.need(parsed.scheme == 'https' and parsed.hostname and not parsed.username and not parsed.password,
                'triage evidence must use public HTTPS URLs')
        kb.need(bool(re.fullmatch(r'[0-9a-f]{64}', source.get('sha256', ''))) and
                isinstance(source.get('excerpt'), str) and len(source['excerpt'].strip()) >= 20,
                'a source hash and supporting excerpt are required')
        kb.need(source.get('verified_at') and source.get('content_type'), 'source retrieval verification is missing')
        if source.get('reviewed_sha256'):
            kb.need(bool(re.fullmatch(r'[0-9a-f]{64}', source['reviewed_sha256'])) and
                    bool(re.fullmatch(r'[0-9a-f]{64}', source.get('reviewed_text_sha256', ''))) and
                    source.get('verification') == 'unchanged_complete_html_text',
                    'changed HTML bytes require the original hash and complete-text binding')
    kb.need(any(canonical_url(s['url']) == canonical_url(event['url']) for s in evidence),
            'review evidence must include the original queued disclosure')
    if record['disposition'] == 'duplicate':
        kb.need(record.get('duplicate_of') and record['duplicate_of'] != event['id'], 'duplicate target is required')
    if 'record_id' in record:
        kb.need(record['record_id'] == record_digest(record), 'triage review audit checksum is invalid')


def active_dispositions(root, queue, packets, reviewed):
    path = root / 'research/monitoring/triage.json'
    data = pipeline.read_json(path) if path.exists() else {}
    decisions, by_id = {}, {e['id']: e for e in queue}
    # Invalid/stale decisions are ignored conservatively, never used to clear work.
    for record in data.get('reviews', []):
        event = by_id.get(record.get('event_id'))
        if not event:
            continue
        ticker = event['ticker']
        try:
            validate_record(record, event, pipeline.digest(pipeline.managed_packet_path(root, ticker).read_bytes()),
                            reviewed.get(ticker), packets[ticker].get('sections', {}))
            kb.need(record.get('record_id'), 'unrecorded review')
            if record['disposition'] == 'duplicate':
                target = by_id.get(record['duplicate_of'])
                kb.need(target and target['ticker'] == ticker, 'duplicate target is unavailable')
                kb.need(record.get('duplicate_of_event_sha256') == event_digest(target), 'duplicate target changed after review')
                kb.need(any(canonical_url(s['url']) == canonical_url(target['url']) for s in record['evidence']),
                        'duplicate target source was not reviewed')
                # The primary copy keeps its own review obligation.
            decisions[event['id']] = record
        except (OSError, ValueError, KeyError, TypeError):
            continue
    # Never close every copy through a duplicate cycle or a duplicate chain.
    return {event_id: record for event_id, record in decisions.items()
            if record['disposition'] != 'duplicate' or
            decisions.get(record['duplicate_of'], {}).get('disposition') != 'duplicate'}


def research_context(root):
    from review_gates import check_managed_reviews
    docs = kb.documents(root)
    check_managed_reviews(root, docs)
    packets, reviewed = {}, {}
    for doc in docs:
        ticker = doc.metadata['ticker']
        path = pipeline.managed_packet_path(root, ticker)
        if path.exists():
            packets[ticker] = pipeline.read_json(path)
            if doc.metadata['status'] == 'reviewed':
                reviewed[ticker] = pipeline.digest(doc.path.read_bytes())
    return packets, reviewed


def triage(root, report, prior=None):
    from disclosure_monitor import accession
    packets, reviewed = research_context(root)
    active = active_dispositions(root, report['queue'], packets, reviewed)
    grouped, entries = {}, []
    for event in report['queue']:
        key = (event['ticker'], event.get('accession') or canonical_url(event['url']))
        grouped.setdefault(key, []).append(event)
    for event in report['queue']:
        rank, why = priority(event)
        key = (event['ticker'], event.get('accession') or canonical_url(event['url']))
        siblings = sorted(e['id'] for e in grouped[key])
        record = active.get(event['id'])
        sources = {s['url'] for s in packets.get(event['ticker'], {}).get('sources', [])}
        covered = bool(reviewed.get(event['ticker'])) and (event['url'] in sources or
                  (event.get('kind') == 'sec_filing' and event.get('accession') in {accession(u) for u in sources} - {None}))
        effective_status = 'reviewed' if covered else 'reviewed_disposition' if record else 'pending_review'
        state = ('already_in_reviewed_evidence' if covered else
                 'reviewed_' + record['disposition'] if record else
                 'duplicate_needs_review' if siblings[0] != event['id'] else 'needs_review')
        entries.append({'event_id': event['id'], 'ticker': event['ticker'], 'title': event.get('title'),
                        'url': event['url'], 'published_at': event.get('published_at'),
                        'event_sha256': event_digest(event), 'priority': 'P' + str(rank),
                        'priority_reason': why, 'classification': state,
                        'duplicate_of': siblings[0] if siblings[0] != event['id'] else None,
                        'review_record_id': record['record_id'] if record else None,
                        'queue_status': effective_status})
    entries.sort(key=lambda e: (e['priority'], e['published_at'] or '', e['ticker'], e['event_id']))
    return {'schema_version': 1, 'generated_at': datetime.now(timezone.utc).isoformat(),
            'discovery_checked_at': report.get('checked_at'),
            'queue_sha256': pipeline.digest(json.dumps(report['queue'], sort_keys=True, ensure_ascii=False)),
            'policy': 'Priority and exact-URL/accession duplicate grouping use metadata only. No materiality finding or research approval is implied. All unresolved items remain pending.',
            'summary': {'total': len(entries), 'pending': sum(e['queue_status'] == 'pending_review' for e in entries),
                        'by_priority': dict(sorted(Counter(e['priority'] for e in entries if e['queue_status'] == 'pending_review').items())),
                        'by_classification': dict(sorted(Counter(e['classification'] for e in entries).items())),
                        'by_company_pending': dict(sorted(Counter(e['ticker'] for e in entries if e['queue_status'] == 'pending_review').items()))},
            'entries': entries, 'reviews': (prior or {}).get('reviews', [])}


def record_review(root, report, decision, fetcher):
    """Verify source bytes/excerpts before appending a reviewer-authored disposition."""
    packets, reviewed = research_context(root)
    event = next((e for e in report['queue'] if e['id'] == decision.get('event_id')), None)
    kb.need(event is not None, 'review event is absent from the durable queue')
    ticker = event['ticker']
    record = {**decision, 'evidence': [dict(s) for s in decision.get('evidence', [])]}
    kb.need('record_id' not in record, 'record IDs are assigned only after verification')
    for source in record['evidence']:
        raw, meta = fetcher.fetch(source['url'], refresh=True)
        text = pipeline.document_text(raw, meta['content_type'])
        current_hash = pipeline.digest(raw)
        if current_hash != source.get('sha256'):
            # Some issuer pages regenerate timestamps/analytics on every request.
            # This is opt-in: the reviewer must bind all extracted text, not just
            # the short excerpt, and the original and fresh byte hashes survive.
            kb.need('html' in meta['content_type'].lower() and
                    bool(re.fullmatch(r'[0-9a-f]{64}', source.get('sha256', ''))) and
                    source.get('reviewed_text_sha256') == pipeline.digest(text),
                    'source changed since the proposed review')
            source.update(reviewed_sha256=source['sha256'], sha256=current_hash,
                          verification='unchanged_complete_html_text')
        else:
            source['verification'] = 'exact_source_bytes'
        normalized = lambda value: ' '.join(value.split())
        kb.need(normalized(source.get('excerpt', '')) in normalized(text), 'review excerpt is not in the fetched source')
        source.update(verified_at=meta['fetched_at'], content_type=meta['content_type'])
    validate_record(record, event, pipeline.digest(pipeline.managed_packet_path(root, ticker).read_bytes()),
                    reviewed.get(ticker), packets[ticker].get('sections', {}))
    if record['disposition'] == 'duplicate':
        target = next((e for e in report['queue'] if e['id'] == record['duplicate_of'] and e['ticker'] == ticker), None)
        kb.need(target is not None,
                'duplicate target is absent from the same company queue')
        kb.need(record.get('duplicate_of_event_sha256') == event_digest(target), 'duplicate target hash is required')
        kb.need(any(canonical_url(s['url']) == canonical_url(target['url']) for s in record['evidence']),
                'duplicate target source must also be reviewed')
    record['recorded_at'] = datetime.now(timezone.utc).isoformat()
    record['record_id'] = record_digest(record)
    path = root / 'research/monitoring/triage.json'
    prior = pipeline.read_json(path) if path.exists() else {'reviews': []}
    prior.setdefault('reviews', []).append(record)
    pipeline.write_json(path, prior)
    pipeline.write_json(path, triage(root, report, prior))
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    parser.add_argument('--report', type=Path, default=Path('research/monitoring/latest.json'))
    parser.add_argument('--record-review', type=Path, help='Append an explicit reviewer-authored, source-bound JSON decision')
    args = parser.parse_args()
    root = args.root.resolve()
    report = pipeline.read_json(args.report if args.report.is_absolute() else root / args.report)
    path = root / 'research/monitoring/triage.json'
    if args.record_review:
        record_review(root, report, pipeline.read_json(args.record_review),
                      pipeline.Fetcher(root, os.environ.get('SEC_USER_AGENT', '')))
    else:
        prior = pipeline.read_json(path) if path.exists() else {}
        pipeline.write_json(path, triage(root, report, prior))
    print(json.dumps(pipeline.read_json(path)['summary'], indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
