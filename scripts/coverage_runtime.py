"""Bridge the reviewed pilot into a separate per-issuer registry and job store.

The curated checkpoint remains a small reviewed corpus. Broad-market collection
is explicitly run through coverage_cli/coverage_worker against this database;
it is never appended to desk.json or the four-file GitHub runtime backup.
"""
from datetime import datetime
import logging
from pathlib import Path

import financial_history
import research_pipeline as p
from coverage_store import CoverageStore


def merge_history(store, cik, history):
    """Never replace a newer collection that wins a concurrent startup write."""
    financial_history.validate_history(history)
    for _ in range(5):
        record = store.get_payload_record(cik, 'history')
        previous = record['value'] if record else None
        metadata = record['metadata'] if record else {}
        if previous:
            old_time = datetime.fromisoformat(previous['source']['retrieved_at'].replace('Z', '+00:00'))
            new_time = datetime.fromisoformat(history['source']['retrieved_at'].replace('Z', '+00:00'))
            base, other = (previous, history) if old_time >= new_time else (history, previous)
            retained = financial_history.apply_normalization_reviews(base, other.get('normalization_reviews', []))
        else:
            retained = history
        committed = store.put_payload_if_current(cik, 'history', retained, metadata.get('sha256'),
                                                source=retained.get('source'), expected_version=metadata.get('version'))
        if committed is not None:
            return
    # A busy collector may keep winning. Preserve its data and retry on the next
    # startup rather than blocking the public app or overwriting a fresh result.
    logging.getLogger('stock-brain').warning('Pilot history merge deferred for CIK %s after concurrent writes', cik)


def initialize_coverage(root, snapshot, path):
    store = CoverageStore(path)
    store.seed_companies(p.universe(Path(root)))
    for company in snapshot['companies']:
        history = company.get('history')
        if not history:
            continue
        cik = history['cik']
        merge_history(store, cik, history)
        # build_desk already passed the canonical profile/packet review gate.
        # This dated narrative does not attest a newly collected financial period.
        store.put_payload(cik, 'reviewed_research', {
            'ticker': company['ticker'], 'cik': cik, 'as_of': company['as_of'],
            'review_type': 'ai', 'review_status': 'reviewed', 'canonical_reviewed': True,
            'sections': company['sections'], 'sources': company['sources'],
            'thesis': company.get('thesis'),
        })
    return store
