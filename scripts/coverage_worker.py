#!/usr/bin/env python3
"""Bounded SEC collection jobs and neutral, unreviewed financial change drafts."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import hashlib
import json
import os
from pathlib import Path
import re
import time
import urllib.error
import urllib.parse

import financial_history as fh
import research_pipeline as p
import stock_brain as kb
from coverage_store import _datetime


def utc_now():
    return datetime.now(timezone.utc)


def encoded_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def issuer_metadata(submissions, cik):
    """Retain reported business classification; SIC is not a GICS assignment."""
    kb.need(str(submissions.get('cik', '')).zfill(10) == cik, 'submissions issuer mismatch')
    sic = submissions.get('sic')
    if type(sic) is int:
        sic = str(sic)
    valid = isinstance(sic, str) and re.fullmatch(r'[0-9]{1,4}', sic) and int(sic) > 0
    description = submissions.get('sicDescription')
    entity = submissions.get('entityType')
    return {'name': submissions.get('name'), 'cik': cik,
            'sic': sic.zfill(4) if valid else None,
            'sic_description': description if isinstance(description, str) and len(description) <= 500 else None,
            'entity_type': entity if isinstance(entity, str) and len(entity) <= 100 else None,
            'classification_status': 'reported_sic' if valid else 'missing_or_invalid_sic'}


def source_metadata(url, raw, meta):
    digest = p.digest(raw)
    kb.need(not meta.get('sha256') or meta['sha256'] == digest, 'provider response hash mismatch')
    retrieved = meta.get('fetched_at') or meta.get('retrieved_at')
    kb.need(bool(retrieved), 'provider response is missing its retrieval timestamp')
    return {'url': url, 'retrieved_at': retrieved, 'sha256': digest}


def financial_filings(submissions, cik, cutoff):
    """Use explicit SEC filing/report dates, including amendments; no calendar inference."""
    kb.need(str(submissions.get('cik', '')).zfill(10) == cik, 'submissions issuer mismatch')
    filing_data = submissions.get('filings', {})
    kb.need(isinstance(filing_data, dict), 'invalid SEC filings object')
    recent = filing_data.get('recent', {})
    kb.need(isinstance(recent, dict), 'invalid SEC recent filings')
    forms = recent.get('form', [])
    kb.need(isinstance(forms, list), 'invalid SEC forms')
    for key in ('accessionNumber', 'filingDate', 'reportDate'):
        kb.need(isinstance(recent.get(key), list) and len(recent[key]) == len(forms),
                'incomplete SEC recent filing columns')
    found = []
    for row in p.filing_rows(submissions):
        if row['form'] not in fh.FORMS:
            continue
        filed, end, accession = row['filingDate'], row['reportDate'], row['accessionNumber']
        kb.iso_date(filed, 'filing date', required=True)
        kb.iso_date(end, 'report date', required=True)
        kb.need(end <= filed and re.fullmatch(r'\d{10}-\d{2}-\d{6}', accession), 'invalid financial filing identity')
        if filed <= cutoff and end <= cutoff:
            found.append({'accession': accession, 'form': row['form'], 'filed': filed,
                          'period_end': end, 'url': fh.filing_url(cik, accession)})
    return sorted(found, key=lambda r: (r['filed'], r['accession']), reverse=True)


def has_accession(data, accession):
    facts = data.get('facts', {})
    kb.need(isinstance(facts, dict), 'invalid Company Facts concepts')
    found = False
    for taxonomy in facts.values():
        kb.need(isinstance(taxonomy, dict), 'invalid Company Facts taxonomy')
        for concept in taxonomy.values():
            kb.need(isinstance(concept, dict) and isinstance(concept.get('units'), dict),
                    'invalid Company Facts concept units')
            for rows in concept['units'].values():
                kb.need(isinstance(rows, list) and all(isinstance(row, dict) for row in rows),
                        'invalid Company Facts observations')
                found = found or any(row.get('accn') == accession for row in rows)
    return found


def recent_filing_inventory(submissions, cik, cutoff):
    """Keep filing metadata for foreign and non-financial forms without modeling it."""
    rows = []
    for row in p.filing_rows(submissions):
        accession, filed, form = row.get('accessionNumber'), row.get('filingDate'), row.get('form')
        kb.need(isinstance(form, str) and 0 < len(form) <= 40, 'invalid filing form')
        kb.iso_date(filed, 'filing date', required=True)
        kb.need(isinstance(accession, str) and re.fullmatch(r'\d{10}-\d{2}-\d{6}', accession), 'invalid filing accession')
        if filed <= cutoff:
            rows.append({'accession': accession, 'filed': filed, 'form': form, 'url': fh.filing_url(cik, accession)})
    return sorted(rows, key=lambda r: (r['filed'], r['accession']), reverse=True)[:1000]


def previous_accession(history):
    sources = [source for cells in (history or {}).get('financials', {}).values()
               for cell in cells.values() for source in cell.get('provenance', [])]
    return max(sources, key=lambda s: (s['filed'], s['accession']))['accession'] if sources else None


class SourceCooldown(ValueError):
    def __init__(self, message, retry_after_seconds=3600, blocked=False):
        super().__init__(message)
        self.retry_after_seconds = max(1, min(86400, int(retry_after_seconds)))
        self.blocked = blocked


def sec_request_guard(store, max_wait_seconds=5, sleep=time.sleep):
    """Reserve a database-wide slot before each attempt, including Fetcher retries."""
    def guard(url):
        host = urllib.parse.urlparse(url).hostname or ''
        if host != 'sec.gov' and not host.endswith('.sec.gov'):
            return
        if os.environ.get('STOCK_BRAIN_SEC_ENABLED', '1') != '1':
            raise SourceCooldown('SEC collection paused by operator')
        status = store.source_status('sec')
        if status['blocked']:
            raise SourceCooldown('SEC persisted cooldown: ' + (status.get('reason') or 'source access paused'), status['wait_seconds'])
        delay = store.reserve_source('sec', interval_seconds=0.5)
        if delay > max_wait_seconds:
            status = store.source_status('sec')
            raise SourceCooldown('SEC persisted cooldown: ' + (status.get('reason') or 'source access paused')
                                 if status['blocked'] else 'SEC rate slot deferred; retry after the reserved interval',
                                 delay + 1)
        if delay > 0:
            sleep(delay)
        status = store.source_status('sec')
        if status['blocked']:
            raise SourceCooldown('SEC persisted cooldown: ' + (status.get('reason') or 'source access paused'), status['wait_seconds'])
        if os.environ.get('STOCK_BRAIN_SEC_ENABLED', '1') != '1':
            raise SourceCooldown('SEC collection paused by operator')
    return guard


class SecFinancialProvider:
    """Small injectable adapter; the shared Fetcher owns identity, rate limits and access guards."""
    def __init__(self, root, user_agent=None, fetcher=None, store=None, sleep=time.sleep, clock=utc_now):
        self.root = Path(root)
        self.user_agent = os.environ.get('SEC_USER_AGENT', '') if user_agent is None else user_agent
        self.fetcher = fetcher
        self.store = store
        self.sleep = sleep
        self.clock = clock

    def readiness(self):
        enabled = os.environ.get('STOCK_BRAIN_SEC_ENABLED', '1') == '1'
        try:
            identified = p.validate_sec_user_agent(self.user_agent)
        except ValueError:
            identified = False
        status = self.store.source_status('sec') if self.store is not None else {'blocked': False}
        return {'provider': 'SEC EDGAR', 'enabled': enabled, 'identity_configured': identified,
                'ready': enabled and identified and not status['blocked'],
                'reason': ('SEC collection paused by operator' if not enabled else
                           'SEC_USER_AGENT must identify the application and its real contact' if not identified else
                           'SEC persisted cooldown: ' + (status.get('reason') or 'source access paused') if status['blocked'] else None),
                'cooldown': status,
                'supported_forms': sorted(fh.FORMS), 'network_checked': False}

    def fetch_json(self, url):
        ready = self.readiness()
        if not ready['enabled']:
            raise SourceCooldown(ready['reason'])
        if ready['cooldown']['blocked']:
            raise SourceCooldown(ready['reason'], ready['cooldown']['wait_seconds'])
        kb.need(ready['ready'], ready['reason'])
        if self.fetcher is None:
            self.fetcher = p.Fetcher(self.root, self.user_agent,
                                     before_request=sec_request_guard(self.store, sleep=self.sleep) if self.store is not None else None)
        elif self.store is not None:
            self.fetcher.before_request = sec_request_guard(self.store, sleep=self.sleep)
        raw, meta = self.fetcher.fetch(url, refresh=True)
        parsed = json.loads(raw)
        kb.need(isinstance(parsed, dict), 'SEC response must be an object')
        return parsed, source_metadata(url, raw, meta)

    def submissions(self, cik):
        return self.fetch_json(f'https://data.sec.gov/submissions/CIK{cik}.json')

    def companyfacts(self, cik):
        return self.fetch_json(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json')

    def failure_policy(self, error):
        text = str(error)
        response_error = error
        for _ in range(5):
            if getattr(response_error, 'code', None) is not None:
                break
            cause = response_error.__cause__ or response_error.__context__
            if cause is None:
                break
            response_error = cause
        code = getattr(response_error, 'code', None)
        if isinstance(error, SourceCooldown):
            return {'blocked': error.blocked, 'stop_batch': True, 'retry_after_seconds': error.retry_after_seconds}
        if 'paused by operator' in text or 'persisted cooldown' in text:
            # A global pause may begin after this job claims its lease. Only
            # an actual access denial makes this issuer require manual retry.
            status = self.store.source_status('sec') if self.store is not None else {}
            return {'blocked': False, 'stop_batch': True,
                    'retry_after_seconds': max(1, min(86400, int(status.get('wait_seconds') or 900)))}
        blocked = bool(getattr(self.fetcher, 'sec_block', None)) or code == 403
        backoff = blocked or code in {429, 500, 502, 503, 504} or 'longer backoff' in text
        pause_seconds = 86400 if blocked else 3600
        if backoff:
            retry_after = str((getattr(response_error, 'headers', None) or {}).get('Retry-After', ''))
            try:
                requested = int(retry_after) if retry_after.isdigit() else (
                    parsedate_to_datetime(retry_after).astimezone(timezone.utc) - self.clock().astimezone(timezone.utc)).total_seconds()
                pause_seconds = max(pause_seconds, min(30 * 86400, requested))
            except (ValueError, TypeError, OverflowError):
                pass
        if self.store is not None and (blocked or backoff):
            self.store.pause_source('sec', seconds=pause_seconds, reason=text[:1000])
        return {'blocked': blocked, 'stop_batch': backoff,
                'retry_after_seconds': min(86400, int(pause_seconds)) if backoff else 900}


def change_draft(previous, history, filing, checked_at, sources):
    """Compare explicit latest periods; gates suppress deltas, never source values."""
    changes = []
    for kind in ('annual', 'quarterly'):
        periods = [period for period in history['periods'] if period['type'] == kind]
        if not periods:
            continue
        current = max(periods, key=lambda period: period['end'])
        old_periods = [period for period in (previous or {}).get('periods', []) if period['type'] == kind]
        same = next((period for period in old_periods if period['id'] == current['id']), None)
        old_period = same or (max(old_periods, key=lambda period: period['end']) if old_periods else None)
        for metric in fh.METRICS:
            cell = history['financials'][current['id']][metric]
            old = previous['financials'][old_period['id']][metric] if old_period else None
            if cell['value'] is None and (not old or old['value'] is None):
                continue
            if same and old and all(cell.get(key) == old.get(key) for key in ('value', 'model_usable', 'flags')):
                continue
            flags = sorted(set(cell['flags']) | set((old or {}).get('flags', [])) |
                           set(current.get('flags', [])) | set((old_period or {}).get('flags', [])))
            compatible = bool(old and cell['model_usable'] and old['model_usable']
                              and not current.get('flags') and not old_period.get('flags')
                              and (not same or current['start'] == old_period['start'])
                              and cell['unit'] == old['unit'] and cell['basis'] == old['basis']
                              and cell.get('definition_tag') == old.get('definition_tag')
                              and cell.get('debt_scope') == old.get('debt_scope'))
            provenance = cell['provenance'] + (old or {}).get('provenance', [])
            changes.append({'metric': metric, 'period_type': kind, 'period_start': current['start'],
                            'period_end': current['end'], 'previous_period_start': (old_period or {}).get('start'),
                            'previous_period_end': (old_period or {}).get('end'), 'previous_value': (old or {}).get('value'),
                            'value': cell['value'], 'unit': cell['unit'],
                            'delta': cell['value'] - old['value'] if compatible else None,
                            'comparison': 'comparable' if compatible else 'blocked' if old else 'new_coverage',
                            'change_type': 'new_period' if old_period and not same else 'value_or_quality_changed' if old else 'first_observation',
                            'flags': flags, 'source_ids': sorted({s['source_id'] for s in provenance}),
                            'source_urls': sorted({s['url'] for s in provenance})})
    open_flags = [flag for flag in history['qa_flags'] if flag.get('status') == 'open']
    classification = 'quality_review_required' if open_flags or any(c['comparison'] == 'blocked' for c in changes) else 'data_collected'
    return {'schema_version': 1, 'cik': history['cik'], 'ticker': history['ticker'],
            'generated_at': checked_at, 'status': 'draft', 'review_status': 'unreviewed', 'canonical_reviewed': False,
            'classification': classification, 'latest_financial_filing': filing, 'history_as_of': history['as_of'],
            'changes': changes,
            'identity_changes': ([{'field': 'ticker', 'previous': previous['ticker'], 'value': history['ticker'],
                                   'identity_basis': 'same CIK in imported listing registry'}]
                                 if previous and previous['ticker'] != history['ticker'] else []),
            'qa': {'open_flag_count': len(open_flags),
                                      'open_flags_by_code': dict(Counter(flag['code'] for flag in open_flags))},
            'sources': sources,
            'limitations': ['Automatic collection and neutral numeric changes have not received research review.',
                            'Comparisons use the exact dates shown; quarterly changes are not automatically year-over-year.',
                            'Unverified definitions, share/debt scope, revisions and fiscal identities block calculated deltas.',
                            'No thesis, forecast, investment recommendation or canonical review status is generated.']}


class CoverageWorker:
    def __init__(self, store, provider, root=kb.ROOT, clock=utc_now):
        self.store, self.provider, self.root, self.clock = store, provider, Path(root), clock
        if isinstance(provider, SecFinancialProvider):
            provider.store = store
            provider.clock = clock

    def _canonical_reviews(self, company):
        path = self.root / 'research/financials' / (company['ticker'] + '.json')
        if not path.exists():
            return []
        history = fh.load_history(self.root, company['ticker'])
        kb.need(history['cik'] == company['cik'], 'canonical evidence belongs to another issuer')
        return history.get('normalization_reviews', [])

    def collect(self, job, *, filings_only=False):
        company = self.store.company(job['cik'])
        kb.need(company is not None and company['cik'] == job['cik'], 'unknown collection issuer')
        cik = company['cik']
        kb.need(bool(re.fullmatch(r'\d{10}', cik)), 'invalid collection CIK')
        checked_at = self.clock().astimezone(timezone.utc).isoformat()
        cutoff = min(checked_at[:10], getattr(self.provider, 'cutoff', checked_at[:10]))
        previous = self.store.get_payload(cik, 'history')
        if previous:
            fh.validate_history(previous)
            kb.need(previous['cik'] == cik, 'stored history belongs to another issuer')
            kb.need(previous['as_of'] <= cutoff, 'stored history exceeds the collection cutoff')
        state = self.store.get_payload(cik, 'collector_state') or {}
        submissions, sub_source = self.provider.submissions(cik)
        # Offline archives must not roll a newer live observation backwards.
        for kind, incoming in (('collector_state', sub_source), ('history', sub_source)):
            old = self.store.get_payload_record(cik, kind)
            if old and old['metadata'].get('source'):
                kb.need(_datetime(incoming['retrieved_at']) >= _datetime(old['metadata']['source']['retrieved_at']),
                        'older source cannot replace newer issuer evidence')
        filings = financial_filings(submissions, cik, cutoff)
        latest = filings[0] if filings else None
        submission_payload = {'schema_version': 1, 'cik': cik, 'ticker': company['ticker'],
                              'checked_at': checked_at, 'source': sub_source,
                              'issuer': issuer_metadata(submissions, cik),
                              'latest_financial_filing': latest, 'filings': filings[:100],
                              'recent_filing_inventory': recent_filing_inventory(submissions, cik, cutoff),
                              'scope': 'Recent filing metadata only; older submission shards and document bodies are not collected here'}
        old_submissions = self.store.get_payload(cik, 'submissions')
        def submission_content(value):
            return {k: v for k, v in (value or {}).items() if k not in ('checked_at', 'source')}
        unchanged_submissions = (old_submissions and
            old_submissions['source']['sha256'] == sub_source['sha256'] and
            submission_content(old_submissions) == submission_content(submission_payload))
        payloads = {} if unchanged_submissions else {'submissions': {'value': submission_payload, 'source': sub_source}}
        fact_source = None
        if filings_only:
            # A separately validated submissions response remains useful when
            # XBRL is delayed or its normalization fails. No financial value or
            # processed accession is advanced by this metadata-only commit.
            draft = {'schema_version': 1, 'cik': cik, 'ticker': company['ticker'], 'generated_at': checked_at,
                     'status': 'draft', 'review_status': 'unreviewed', 'canonical_reviewed': False,
                     'classification': 'quality_review_required', 'latest_financial_filing': latest,
                     'history_as_of': (previous or {}).get('as_of'), 'changes': [],
                     'qa': {'open_flag_count': 1, 'open_flags_by_code': {'financial_collection_incomplete': 1}},
                     'sources': [sub_source],
                     'limitations': ['Filing metadata was checked. Financial collection did not complete; any previous history retains its original source dates.']}
            payloads['automatic_changes'] = {'value': draft, 'source': sub_source}
            result = {'classification': 'quality_review_required', 'action': 'filings_only_financials_incomplete',
                      'facts_fetched': False, 'latest_financial_accession': state.get('latest_financial_accession'),
                      'history_sha256': state.get('history_sha256')}
        elif latest is None:
            draft = {'schema_version': 1, 'cik': cik, 'ticker': company['ticker'], 'generated_at': checked_at,
                     'status': 'draft', 'review_status': 'unreviewed', 'canonical_reviewed': False,
                     'classification': 'quality_review_required', 'latest_financial_filing': None,
                     'history_as_of': (previous or {}).get('as_of'), 'changes': [],
                     'qa': {'open_flag_count': 1, 'open_flags_by_code': {'unsupported_or_missing_financial_forms': 1}},
                     'sources': [sub_source], 'limitations': ['No supported 10-K/10-Q filing exists in the retrieved recent submissions; foreign forms and older submission shards require a separate source adapter. Prior history is retained.']}
            payloads['automatic_changes'] = {'value': draft, 'source': sub_source}
            result = {'classification': 'quality_review_required', 'action': 'no_supported_filing', 'facts_fetched': False}
        else:
            processed = state.get('latest_financial_accession') or previous_accession(previous)
            fetch_facts = previous is None or latest['accession'] != processed or getattr(self.provider, 'force_facts', False)
            history = previous
            sources = [sub_source]
            if fetch_facts:
                facts, fact_source = self.provider.companyfacts(cik)
                old = self.store.get_payload_record(cik, 'history')
                if old and old['metadata'].get('source'):
                    kb.need(_datetime(fact_source['retrieved_at']) >= _datetime(old['metadata']['source']['retrieved_at']),
                            'older Company Facts cannot replace newer history')
                kb.need(has_accession(facts, latest['accession']), 'latest filing is not yet available in Company Facts; prior history retained')
                reviews = list((previous or {}).get('normalization_reviews', []))
                by_id = {review['review_id']: review for review in reviews}
                for review in self._canonical_reviews(company):
                    kb.need(review['review_id'] not in by_id or by_id[review['review_id']] == review,
                            'canonical normalization review ID conflict')
                    by_id[review['review_id']] = review
                history = fh.normalize_companyfacts(facts, company, cutoff,
                    {'fetched_at': fact_source['retrieved_at'], 'sha256': fact_source['sha256']},
                    normalization_reviews=list(by_id.values()))
                if fact_source.get('acquisition') == 'operator_supplied_sec_bulk_archive':
                    history['source']['acquisition'] = fact_source['acquisition']
                    history['source']['archive'] = fact_source['archive']
                    history['source']['raw_cache'] = None
                expected_kind = 'annual' if latest['form'].startswith('10-K') else 'quarterly'
                current_periods = [period for period in history['periods']
                                   if period['end'] == latest['period_end'] and period['type'] == expected_kind]
                kb.need(current_periods and any(
                    source['accession'] == latest['accession']
                    for period in current_periods for metric in ('revenue', 'net_income', 'operating_income', 'operating_cash_flow')
                    for source in history['financials'][period['id']][metric]['provenance']),
                    'latest filing financial period is not yet normalized; prior history retained')
                # The registry's stable CIK owns identity across a ticker rename.
                # Align the alias only for the generic coverage validator; the
                # old payload version and its source observations remain intact.
                prior_identity = {**previous, 'ticker': history['ticker']} if previous else None
                fh.validate_refresh(prior_identity, history)
                sources.append(fact_source)
                def content(value):
                    return {**{k: v for k, v in value.items() if k not in ('as_of', 'source', 'source_index')},
                        'source_index': {key: {k: v for k, v in entry.items() if k != 'retrieved_at'}
                            for key, entry in value['source_index'].items()}}
                if (previous and previous['source']['sha256'] == fact_source['sha256']
                        and content(previous) == content(history)):
                    # Keep the original source observation and all prior versions.
                    # A tiny collector state records the new successful check.
                    history = previous
                else:
                    payloads['history'] = {'value': history, 'source': fact_source}
                    draft = change_draft(previous, history, latest, checked_at, sources)
                    payloads['automatic_changes'] = {'value': draft, 'source': fact_source}
            else:
                kb.need(history is not None, 'unchanged filing has no stored history')
                # New release evidence may be applied without claiming a new SEC download.
                reviewed = fh.apply_normalization_reviews(history, self._canonical_reviews(company))
                reviewed['ticker'] = company['ticker']
                reviewed['company_name'] = company['company_name']
                if reviewed != history:
                    source = {'url': history['source']['url'], 'retrieved_at': history['source']['retrieved_at'],
                              'sha256': history['source']['sha256']}
                    payloads['history'] = {'value': reviewed, 'source': source}
                    payloads['automatic_changes'] = {'value': change_draft(history, reviewed, latest, checked_at, sources), 'source': source}
                    history = reviewed
            classification = 'quality_review_required' if any(flag.get('status') == 'open' for flag in history['qa_flags']) else 'data_collected'
            result = {'classification': classification, 'action': 'new_financial_filing' if fetch_facts else 'filing_unchanged',
                      'facts_fetched': fetch_facts, 'latest_financial_accession': latest['accession'],
                      'history_sha256': encoded_digest(history)}
        payloads['collector_state'] = {'value': {'schema_version': 1, 'cik': cik, 'ticker': company['ticker'],
            'last_checked_at': checked_at, 'status': result['classification'],
            'latest_financial_accession': result.get('latest_financial_accession'),
            'history_sha256': result.get('history_sha256'), 'last_action': result['action'],
            'facts_checked_at': fact_source['retrieved_at'] if fact_source else state.get('facts_checked_at'),
            'facts_sha256': fact_source['sha256'] if fact_source else state.get('facts_sha256'),
            'canonical_reviewed': False}, 'source': sub_source}
        return payloads, result

    def run(self, worker_id, limit=10, dry_run=False):
        kb.need(isinstance(limit, int) and not isinstance(limit, bool) and 1 <= limit <= 100, 'worker limit must be 1..100')
        kb.need(bool(worker_id.strip()), 'worker ID is required')
        ready = self.provider.readiness()
        report = {'worker_id': worker_id, 'limit': limit, 'dry_run': dry_run, 'provider': ready,
                  'processed': 0, 'succeeded': 0, 'failed': 0, 'stopped_reason': None, 'jobs': []}
        if dry_run or not ready['ready']:
            report['stopped_reason'] = ready['reason'] if not ready['ready'] else None
            return report
        for _ in range(limit):
            ready = self.provider.readiness()
            if not ready['ready']:
                report['stopped_reason'] = ready['reason']
                break
            job = self.store.claim(worker_id, now=self.clock().astimezone(timezone.utc).isoformat(),
                                   lease_seconds=300, kind='refresh_company')
            if job is None:
                break
            job_id = job.get('job_id', job.get('id'))
            report['processed'] += 1
            try:
                kb.need(job['kind'] == 'refresh_company', 'unsupported collection job kind')
                payloads, result = self.collect(job)
                self.store.commit_job(job_id, worker_id, job['lease_token'], payloads, result=result)
                report['succeeded'] += 1
                report['jobs'].append({'job_id': job_id, 'cik': job['cik'], **result})
            except (ValueError, OSError, KeyError, TypeError, RuntimeError) as error:
                policy = self.provider.failure_policy(error)
                message = str(error)[:1000]
                try:
                    self.store.fail(job_id, worker_id, job['lease_token'], message,
                                    retry_after_seconds=policy['retry_after_seconds'], blocked=policy['blocked'])
                except (ValueError, RuntimeError):
                    # Another worker owns an expired lease; staged payloads were never committed.
                    message = 'Job lease lost; staged data discarded. ' + message
                report['failed'] += 1
                report['jobs'].append({'job_id': job_id, 'cik': job['cik'], 'error': message,
                                       'prior_payloads_retained': True, **policy})
                if policy['stop_batch']:
                    report['stopped_reason'] = message
                    break
        return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path)
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--worker-id', default='coverage-' + str(os.getpid()))
    parser.add_argument('--dry-run', action='store_true', help='Inspect configuration without claiming jobs or accessing the network.')
    parser.add_argument('--readiness', action='store_true', help='Alias for --dry-run; configuration status is not an access probe.')
    args = parser.parse_args()
    from coverage_store import CoverageStore
    try:
        store = CoverageStore(args.db)
        worker = CoverageWorker(store, SecFinancialProvider(args.root), root=args.root)
        report = worker.run(args.worker_id, args.limit, args.dry_run or args.readiness)
        print(json.dumps(report, ensure_ascii=False))
        return 1 if report['failed'] or (report['stopped_reason'] and not (args.dry_run or args.readiness)) else 0
    except (ValueError, OSError) as error:
        print(json.dumps({'error': str(error), 'network_success_claimed': False}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
