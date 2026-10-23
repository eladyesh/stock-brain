from copy import deepcopy
import json
from pathlib import Path
import shutil
import os
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import brain_markdown as brain
import research_queue as queue
import research_financials as financials
import research_api
import research_state
import research_pipeline
import sector_facts
import stock_brain as kb
import test_brain_markdown
from company_identity import primary_symbol, symbol_paths


class ResearchQueueTests(unittest.TestCase):
    def setUp(self):
        test_brain_markdown.MarkdownTests.setUp(self)
        self.state = self.root / 'state'
        self.accession = '0000789019-26-000001'
        self.index_url = 'https://www.sec.gov/Archives/edgar/data/789019/000078901926000001/' + self.accession + '-index.html'
        self.doc_url = self.index_url.rsplit('/', 1)[0] + '/synthetic.htm'
        self.store.put_payload('0000789019', 'submissions', {'cik': '0000789019', 'source': {
            'url': 'https://data.sec.gov/submissions/CIK0000789019.json', 'retrieved_at': self.release['created_at']},
            'filings': [{'accession': self.accession, 'form': '10-K', 'filed': '2026-09-01', 'period_end': '2026-06-30', 'url': self.index_url}]})
        brain.export(self.store, self.output, self.release)

    def fetcher(self, fail_document=False):
        parent = self
        class Fetcher:
            sec_block = None
            def __init__(self): self.calls = []
            def fetch(self, url):
                self.calls.append(url)
                if url == parent.index_url:
                    return b'<table><tr><td>1</td><td>Annual</td><td><a href="synthetic.htm">Document</a></td><td>10-K</td></tr></table>', {}
                parent.assertEqual(url, parent.doc_url)
                if fail_document:
                    self.sec_block = 'blocked'
                    raise ValueError('SEC unavailable')
                # Synthetic fixture, not assertions about Microsoft.
                text = ('Our business provides synthetic testing instruments to test laboratories. Our customers use these fictional products only in test fixtures.\n'
                        'Our competitors offer synthetic substitutes and the competition described here is fictional and intended only to test source attribution.\n'
                        'Risk factors include hypothetical testing failures that could materially adversely affect this completely fictional business.\n') * 5
                return text.encode(), {'content_type': 'text/plain', 'fetched_at': parent.release['created_at']}
        return Fetcher()

    def test_collect_every_issuer_plan_reuses_unchanged_accessions_and_keeps_review_boundary(self):
        f = self.fetcher()
        state = queue.run(self.output, self.state, root=self.root, fetcher=f)
        self.assertEqual(state['last_run']['issuers'], 1)
        self.assertEqual(state['last_run']['completed'], 1)
        self.assertEqual(len(f.calls), 2)
        again = queue.run(self.output, self.state, root=self.root, fetcher=f)
        self.assertEqual(again['last_run']['attempted'], 0)
        self.assertEqual(len(f.calls), 2)
        report = queue.report_read(self.state, state, '0000789019')
        self.assertFalse(report['canonical_reviewed'])
        self.assertIn('business-overview', report['documents'][0]['topics'])

    def test_block_stops_batch_keeps_prior_data_and_sets_retry(self):
        f = self.fetcher(fail_document=True)
        state = queue.run(self.output, self.state, root=self.root, fetcher=f)
        self.assertEqual(state['last_run']['stop_reason'], 'sec_access_blocked')
        job = state['jobs']['0000789019']
        self.assertEqual(job['status'], 'retry')
        self.assertIsNotNone(job['next_retry_at'])
        self.assertFalse(state['last_run']['model_enabled'])
        again = queue.run(self.output, self.state, root=self.root, fetcher=f)
        self.assertEqual(again['last_run']['attempted'], 0)

    def test_durable_git_state_restores_reports_and_rejects_a_stale_writer(self):
        remote = self.root / 'state.git'
        subprocess.run(['git', 'init', '--bare', '-q', str(remote)], check=True)
        tree = subprocess.run(['git', '--git-dir', str(remote), 'mktree'], input='', capture_output=True, text=True, check=True).stdout.strip()
        legacy = subprocess.run(['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.test', '--git-dir', str(remote), 'commit-tree', tree],
                                input='Unrelated branch\n', capture_output=True, text=True, check=True).stdout.strip()
        subprocess.run(['git', '--git-dir', str(remote), 'update-ref', 'refs/heads/automation/research-data', legacy], check=True)
        real_run = subprocess.run
        def local_remote(args, **kwargs):
            args = [str(remote) if a == 'https://github.com/' + brain.REPO + '.git' else a for a in args]
            return real_run(args, **kwargs)
        with patch.dict(os.environ, {'GH_TOKEN': 'synthetic-test-token'}), patch.object(research_state.subprocess, 'run', side_effect=local_remote):
            self.assertEqual(research_state.sync(self.state), '')
            queue.run(self.output, self.state, fetcher=self.fetcher())
            first = research_state.sync(self.state, publish=True)
            replica, stale = self.root / 'replica', self.root / 'stale'
            self.assertEqual(research_state.sync(replica), first)
            research_state.sync(stale)
            self.assertEqual(queue.load_state(replica), queue.load_state(self.state))
            queue.run(self.output, replica, fetcher=self.fetcher(), now='2026-10-24T00:00:00+00:00')
            research_state.sync(replica, publish=True)
            with self.assertRaisesRegex(ValueError, 'branch changed'):
                research_state.sync(stale, publish=True)
        preserved = subprocess.run(['git', '--git-dir', str(remote), 'rev-parse', 'refs/heads/automation/research-data'],
                                   capture_output=True, text=True, check=True).stdout.strip()
        self.assertEqual(preserved, legacy)

    def test_enriched_markdown_keeps_financial_observations_and_actual_evidence_in_compact_view(self):
        queue.run(self.output, self.state, fetcher=self.fetcher())
        before = len(kb.export_records(ROOT))
        queue.enrich(self.output, self.state)
        compact = self.root / 'compact'
        manifest = sector_facts.export(self.output, compact, 'c' * 40)
        row = manifest['companies'][0]
        self.assertEqual(row['path'], 'sectors/information-technology/facts/MSFT/README.md')
        meta, body = brain.split_profile((compact / row['path']).read_text())
        self.assertIn('Source excerpt', body)
        self.assertIn('synthetic testing instruments', body)
        self.assertIn('Research work queue', body)
        self.assertEqual(meta['research_progress']['stage'], 'evidence_collected')
        self.assertFalse(meta['canonical_reviewed'])
        self.assertEqual(len(kb.export_records(ROOT)), before)
        self.assertIn('Derived observation:', body)
        self.assertEqual(len(kb.sections_from(body, kb.config(ROOT)[1])), 18)
        with self.assertRaisesRegex(ValueError, 'already applied'):
            queue.enrich(self.output, self.state)

    def test_hash_tampering_and_filing_path_escape_are_rejected(self):
        state = queue.run(self.output, self.state, fetcher=self.fetcher())
        report = self.state / 'reports/0000789019.json'
        report.write_text(report.read_text() + ' ')
        with self.assertRaisesRegex(ValueError, 'preserve manual'):
            queue.load_state(self.state)
        for url in ('https://evil.invalid/file.htm', self.doc_url.replace('/789019/', '/123/'), self.doc_url + '?token=x', self.doc_url.replace('synthetic.htm', '../secret')):
            with self.assertRaises(ValueError): queue.safe_filing_url(url, '0000789019', self.accession)

    def test_daily_request_budget_survives_separate_runs(self):
        f = self.fetcher()
        original = f.fetch
        def factory(root, user_agent, before_request):
            def counted(url):
                before_request(url)
                return original(url)
            f.fetch = counted
            return f
        with patch.object(queue.pipeline, 'Fetcher', side_effect=factory):
            first = queue.run(self.output, self.state, max_requests=1)
            second = queue.run(self.output, self.state, max_requests=1)
        self.assertEqual(first['last_run']['stop_reason'], 'request_budget')
        self.assertEqual(first['daily_usage']['requests'], 1)
        self.assertEqual(second['daily_usage']['requests'], 1)
        self.assertEqual(len(f.calls), 1)

    def test_partially_completed_job_checkpoints_documents_before_later_failure(self):
        state = queue.load_state(self.state)
        queue.plan(self.output, state)
        job = state['jobs']['0000789019']
        job['filings'].append({**job['filings'][0], 'accession': '0000789019-26-000002', 'url': self.index_url.replace('000001', '000002')})
        f = self.fetcher()
        original = f.fetch
        def fail_next(url):
            if '000002' in url: raise OSError('temporary failure')
            return original(url)
        f.fetch = fail_next
        with self.assertRaises(OSError):
            queue.collect_job(job, f, checkpoint=lambda r: queue.save_report(self.state, state, r))
        self.assertEqual(len(queue.report_read(self.state, state, job['cik'])['documents']), 1)

    def test_interruption_keeps_reserved_budget_before_external_request(self):
        def factory(root, user_agent, before_request):
            class Interrupted:
                sec_block = None
                def fetch(self, url):
                    before_request(url)
                    raise KeyboardInterrupt()
            return Interrupted()
        with patch.object(queue.pipeline, 'Fetcher', side_effect=factory):
            with self.assertRaises(KeyboardInterrupt):
                queue.run(self.output, self.state, max_requests=1)
        saved = queue.load_state(self.state)
        self.assertEqual(saved['daily_usage']['requests'], 1)
        self.assertEqual(saved['daily_usage']['companies'], 1)
        again = queue.run(self.output, self.state, fetcher=self.fetcher(), max_requests=1)
        self.assertEqual(again['last_run']['attempted'], 0)

    def test_synthesis_rejects_invented_quotes_numbers_identity_and_review_fields(self):
        state = queue.run(self.output, self.state, fetcher=self.fetcher())
        job = state['jobs']['0000789019']
        report = queue.report_read(self.state, state, job['cik'])
        request = queue.synthesis_request(job, report, ROOT)
        packet = {'cik': job['cik'], 'sections': {s['id']: {'unavailable': 'No supporting evidence.'} for s in request['sections']}}
        e = report['documents'][0]['topics']['business-overview'][0]
        packet['sections']['business-overview'] = {'claims': [{'kind': 'reported', 'text': 'A synthetic instrument supplier.', 'evidence': [{'excerpt_id': e['id'], 'quote': e['text']}]}]}
        queue.validate_synthesis(packet, request)
        for mutation in ('quote', 'number', 'cik'):
            bad = deepcopy(packet)
            if mutation == 'quote': bad['sections']['business-overview']['claims'][0]['evidence'][0]['quote'] = 'This quote does not occur in the supplied source.'
            if mutation == 'number': bad['sections']['business-overview']['claims'][0]['text'] = 'Revenue was 999 billion.'
            if mutation == 'cik': bad['cik'] = '0000000001'
            with self.assertRaises(ValueError): queue.validate_synthesis(bad, request)

    def test_public_research_api_searches_aliases_and_uses_verified_file_bytes(self):
        queue.run(self.output, self.state, fetcher=self.fetcher())
        queue.enrich(self.output, self.state)
        compact = self.root / 'compact'
        sector_facts.export(self.output, compact, 'c' * 40)
        shutil.copytree(ROOT / 'config', compact / 'config')
        library = research_api.ResearchLibrary(compact)
        listing = library.list('q=MSFT&limit=25')
        self.assertEqual(listing['total'], 1)
        self.assertEqual(listing['items'][0]['symbol'], 'MSFT')
        page = library.detail('MSFT')
        self.assertEqual(len(page['sections']), 18)
        self.assertFalse(page['canonical_reviewed'])
        self.assertIn('/facts/MSFT/README.md', page['markdown_url'])
        self.assertEqual(library.detail('0000789019'), page)
        self.assertEqual(library.serve('/api/research/NOTFOUND', '')[0], '404 Not Found')
        for q in ('limit=50000', 'q=x&q=y', 'offset=-1', 'sector=../../etc', 'stage=reviewed'):
            self.assertEqual(library.serve('/api/research', q)[0], '400 Bad Request')
        library.cache.clear()
        path = compact / listing['items'][0].get('path', 'sectors/information-technology/facts/MSFT/README.md')
        path.write_text(path.read_text() + 'tampered')
        self.assertEqual(library.serve('/api/research/MSFT', '')[0], '400 Bad Request')

    def test_curated_runner_can_resolve_a_company_outside_the_small_cohort(self):
        compact = self.root / 'compact'
        sector_facts.export(self.output, compact, 'c' * 40)
        shutil.copytree(ROOT / 'config', compact / 'config')
        (compact / 'config/universe.json').write_text(json.dumps({'schema_version': 1, 'companies': []}))
        company = research_pipeline.issuer(compact, 'MSFT')
        self.assertEqual(company['cik'], '0000789019')
        self.assertEqual(company['group'], 'broad-market')
        self.assertEqual(company['exchange'], 'NASDAQ')


class FinancialResearchTests(unittest.TestCase):
    def setUp(self):
        self.history = json.loads((ROOT / 'research/financials/MSFT.json').read_text())

    def test_no_comparison_when_definitions_periods_or_denominators_are_incompatible(self):
        self.assertTrue(financials.analyze(self.history)['observations'])
        annual = sorted([p for p in self.history['periods'] if p['type'] == 'annual'], key=lambda p: p['end'], reverse=True)
        latest = self.history['financials'][annual[0]['id']]
        prior = self.history['financials'][annual[1]['id']]
        latest['revenue']['model_usable'] = False
        prior['operating_income']['value'] = -10
        latest['net_income']['definition_tag'] = 'DifferentDefinition'
        ids = {o['id'] for o in financials.analyze(self.history)['observations']}
        self.assertNotIn('revenue_annual_growth', ids)
        self.assertNotIn('operating_income_annual_growth', ids)
        self.assertNotIn('net_income_annual_growth', ids)
        self.assertNotIn('net_income_to_revenue', ids)
        for o in financials.analyze(self.history)['observations']:
            self.assertTrue(o['source_urls'])
            self.assertTrue(o['inputs'])

    def test_ticker_collision_and_rename_preserve_issuer_identity(self):
        rows = [{'cik': '0000000001', 'tickers': ['AAA']}, {'cik': '0000000002', 'tickers': ['AAA']}]
        paths = symbol_paths(rows)
        self.assertEqual(paths['0000000001'], 'AAA--0000000001')
        rows[0]['tickers'] = ['NEW']
        self.assertEqual(symbol_paths(rows)['0000000001'], 'NEW')
        self.assertEqual(primary_symbol(['BRK.B', 'BRK.A']), 'BRK.A')
        with self.assertRaises(ValueError): symbol_paths([{'cik': '1', 'tickers': ['../../escape']}])


if __name__ == '__main__':
    unittest.main()
