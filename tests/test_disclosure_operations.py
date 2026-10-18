import json
from datetime import datetime, timezone
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import disclosure_monitor as monitor
import prepare_updates
import research_pipeline as pipeline
import triage_disclosures as triage


class DiscoveryParsingTests(unittest.TestCase):
    def test_html_success_response_is_not_an_empty_feed(self):
        for body in (b'<html><body>Site Unavailable</body></html>',
                     b'<html><item><link>https://issuer.example/news</link></item></html>',
                     b'<rss/>'):
            with self.subTest(body=body), self.assertRaises(ValueError):
                monitor.parse_feed(body, 'MU', 'https://issuer.example/feed')

    def test_empty_feed_and_partial_entries_have_visible_warnings(self):
        events, warnings = monitor.parse_feed_details(b'<rss><channel/></rss>', 'MU', 'https://issuer.example/feed')
        self.assertEqual(events, [])
        self.assertTrue(warnings)
        events, warnings = monitor.parse_feed_details(
            b'<rss><channel><item><link>https://issuer.example/a</link></item><item><link>javascript:bad()</link></item></channel></rss>',
            'MU', 'https://issuer.example/feed')
        self.assertEqual(len(events), 1)
        self.assertIsNone(events[0]['published_at'])
        self.assertEqual(len(warnings), 2)

    def test_empty_feed_does_not_make_an_issuer_checked(self):
        with patch.object(monitor, 'discover_sec', return_value=[]), patch.object(pipeline.Fetcher, 'fetch',
                return_value=(b'<rss><channel/></rss>', {})):
            report = monitor.run(ROOT, 'Stock Brain test contact')
        self.assertEqual(report['companies']['MSFT']['status'], 'partial')
        self.assertEqual(report['companies']['MSFT']['coverage_status'], 'partial')
        self.assertEqual(report['companies']['MSFT']['source_checks'][1]['status'], 'partial')

    def test_q4_official_date_shape_relative_url_and_no_body_execution(self):
        payload = {'GetPressReleaseListResult': [{'Headline': 'Results &amp; guidance',
                    'LinkToDetailPage': '/news/release.aspx', 'PressReleaseDate': '09/30/2026 16:01:00',
                    'Body': '<script>ignored()</script>'}]}
        events, warnings = monitor.parse_q4_news(json.dumps(payload).encode(), 'MU', 'https://investors.micron.com/feed/news')
        self.assertEqual(events[0]['published_at'], '2026-09-30')
        self.assertEqual(events[0]['url'], 'https://investors.micron.com/news/release.aspx')
        self.assertEqual(events[0]['title'], 'Results & guidance')
        self.assertEqual(warnings, [])
        self.assertNotIn('Body', events[0])

    def test_q4_missing_structure_errors_empty_list_is_partial(self):
        with self.assertRaises(ValueError):
            monitor.parse_q4_news(b'{"error":"unavailable"}', 'PLTR', 'https://issuer.example/news')
        events, warnings = monitor.parse_q4_news(b'{"GetPressReleaseListResult":[]}', 'PLTR', 'https://issuer.example/news')
        self.assertEqual(events, [])
        self.assertTrue(warnings)

    def test_adapters_cover_the_overlap_across_calendar_years(self):
        config = {'issuer_adapters': {'MU': [{'kind': 'q4_news', 'url': 'https://issuer.example/news?year={year}'}]}}
        self.assertEqual([s['url'] for s in monitor.issuer_sources(config, 'MU', '2025-10-01', '2026-01-01')],
                         ['https://issuer.example/news?year=2025', 'https://issuer.example/news?year=2026'])

    def test_four_missing_issuers_have_explicit_configured_sources(self):
        config = pipeline.read_json(ROOT / 'config/discovery.json')
        for ticker in ('MU', 'PLTR', 'AVAV', 'ORCL'):
            self.assertTrue(monitor.issuer_sources(config, ticker, '2026-07-01', '2026-10-18'))


class TriageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.packet = {'sections': {'business-overview': {'claims': []}}, 'sources': []}
        self.packet_path = self.root / 'research/pilot/MSFT.json'
        pipeline.write_json(self.packet_path, self.packet)
        self.packets = {'MSFT': self.packet}
        self.reviewed = {'MSFT': 'a' * 64}
        self.event = {'id': 'event-one', 'ticker': 'MSFT', 'title': 'Upcoming investor conference',
                      'url': 'https://issuer.example/news', 'published_at': '2026-10-01',
                      'kind': 'issuer_feed', 'status': 'pending_review'}
        self.report = {'queue': [self.event], 'checked_at': '2026-10-18T00:00:00+00:00'}
        self.body = b'This release announces only the previously published conference date.'
        self.decision = {'event_id': self.event['id'], 'event_sha256': triage.event_digest(self.event),
                         'packet_sha256': pipeline.digest(self.packet_path.read_bytes()),
                         'profile_sha256': self.reviewed['MSFT'], 'reviewer': 'Test reviewer', 'reviewer_type': 'human',
                         'reviewed_at': datetime.now(timezone.utc).isoformat(), 'disposition': 'no_material_change',
                         'reason': 'The original release contains only a conference date and does not amend the reviewed business description.',
                         'source_read_in_full': True, 'sections_checked': ['business-overview'],
                         'evidence': [{'url': self.event['url'], 'sha256': pipeline.digest(self.body),
                                       'excerpt': self.body.decode()}]}

    def tearDown(self):
        self.temp.cleanup()

    def fake_fetcher(self):
        body = self.body
        class Fake:
            def fetch(self, *args, **kwargs):
                return body, {'content_type': 'text/plain', 'fetched_at': datetime.now(timezone.utc).isoformat()}
        return Fake()

    def record(self, decision=None):
        with patch.object(triage, 'research_context', return_value=(self.packets, self.reviewed)):
            return triage.record_review(self.root, self.report, decision or self.decision, self.fake_fetcher())

    def test_priority_routes_material_headlines_ahead_of_calendar_items(self):
        self.assertEqual(prepare_updates.priority({'form': '10-Q'}), 0)
        self.assertEqual(prepare_updates.priority({'title': 'Issuer Reports Third Quarter Results'}), 0)
        self.assertEqual(prepare_updates.priority({'title': 'Issuer awarded $1 billion contract'}), 1)
        self.assertEqual(prepare_updates.priority({'title': 'Issuer Announces Date of Earnings Webcast'}), 3)

    def test_metadata_triage_preserves_pending_and_does_not_approve(self):
        other = {**self.event, 'id': 'event-two', 'url': self.event['url'] + '?utm_source=feed'}
        report = {'queue': [self.event, other]}
        with patch.object(triage, 'research_context', return_value=(self.packets, self.reviewed)):
            out = triage.triage(self.root, report)
        self.assertEqual(out['summary']['pending'], 2)
        self.assertEqual(out['summary']['by_classification'], {'duplicate_needs_review': 1, 'needs_review': 1})
        self.assertEqual(out['reviews'], [])
        self.assertTrue(all(e['status'] == 'pending_review' for e in report['queue']))

    def test_explicit_verified_review_resolves_only_exact_event_version(self):
        record = self.record()
        active = triage.active_dispositions(self.root, [self.event], self.packets, self.reviewed)
        queue = monitor.reconciled_queue([self.event], [], self.packets, self.reviewed, 'now', active)
        self.assertEqual(queue[0]['status'], 'reviewed_disposition')
        self.assertEqual(queue[0]['resolved_by_triage_review'], record['record_id'])
        changed = {**self.event, 'title': 'Changed disclosure with financial information'}
        self.assertEqual(triage.active_dispositions(self.root, [changed], self.packets, self.reviewed), {})
        self.assertEqual(triage.active_dispositions(self.root, [self.event], self.packets, {}), {})

    def test_changed_packet_reopens_review_and_preserves_audit(self):
        self.record()
        pipeline.write_json(self.packet_path, {**self.packet, 'as_of': '2026-10-18'})
        self.assertEqual(triage.active_dispositions(self.root, [self.event], self.packets, self.reviewed), {})
        self.assertEqual(len(pipeline.read_json(self.root / 'research/monitoring/triage.json')['reviews']), 1)

    def test_wrong_source_hash_or_excerpt_cannot_close_item(self):
        for evidence in ({**self.decision['evidence'][0], 'sha256': '0' * 64},
                         {**self.decision['evidence'][0], 'excerpt': 'A fabricated financial conclusion that does not occur in the source.'}):
            with self.subTest(evidence=evidence), self.assertRaises(ValueError):
                self.record({**self.decision, 'evidence': [evidence]})
        self.assertFalse((self.root / 'research/monitoring/triage.json').exists())

    def test_missing_full_review_attestation_is_rejected(self):
        with self.assertRaises(ValueError):
            self.record({**self.decision, 'source_read_in_full': False})

    def test_dynamic_html_requires_complete_text_and_retains_both_byte_hashes(self):
        original = b'<html><meta name="timestamp" content="1"><body>Previously reviewed release text in full.</body></html>'
        fresh = original.replace(b'content="1"', b'content="2"')
        evidence = {**self.decision['evidence'][0], 'sha256': pipeline.digest(original),
                    'excerpt': 'Previously reviewed release text in full.',
                    'reviewed_text_sha256': pipeline.digest(pipeline.document_text(original, 'text/html'))}
        fetcher = self.fake_fetcher()
        fetcher.fetch = lambda *a, **kw: (fresh, {'content_type': 'text/html',
                                      'fetched_at': datetime.now(timezone.utc).isoformat()})
        with patch.object(triage, 'research_context', return_value=(self.packets, self.reviewed)):
            record = triage.record_review(self.root, self.report, {**self.decision, 'evidence': [evidence]}, fetcher)
            bound = record['evidence'][0]
            self.assertEqual(bound['sha256'], pipeline.digest(fresh))
            self.assertEqual(bound['reviewed_sha256'], pipeline.digest(original))
            self.assertEqual(bound['verification'], 'unchanged_complete_html_text')
            # The excerpt is unchanged, but new material elsewhere must reopen review.
            fresh = fresh.replace(b'</body>', b' New financing was announced.</body>')
            with self.assertRaises(ValueError):
                triage.record_review(self.root, self.report, {**self.decision, 'evidence': [evidence]}, fetcher)

    def test_duplicate_cycles_cannot_resolve_all_copies(self):
        other = {**self.event, 'id': 'event-two'}
        first = {**self.decision, 'disposition': 'duplicate', 'duplicate_of': 'event-two',
                 'duplicate_of_event_sha256': triage.event_digest(other)}
        self.report['queue'].append(other)
        self.record(first)
        second = {**first, 'event_id': other['id'], 'event_sha256': triage.event_digest(other),
                  'duplicate_of': self.event['id'], 'duplicate_of_event_sha256': triage.event_digest(self.event)}
        self.record(second)
        self.assertEqual(triage.active_dispositions(self.root, self.report['queue'], self.packets, self.reviewed), {})

    def test_stale_report_review_status_is_not_trusted_without_current_evidence(self):
        report = {'queue': [{**self.event, 'status': 'reviewed'}]}
        with patch.object(triage, 'research_context', return_value=(self.packets, self.reviewed)):
            out = triage.triage(self.root, report)
        self.assertEqual(out['summary']['pending'], 1)
        self.assertEqual(out['entries'][0]['classification'], 'needs_review')


if __name__ == '__main__':
    unittest.main()
