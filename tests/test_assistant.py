import copy
from datetime import datetime, timedelta, timezone
from functools import partial
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import answering as a
import disclosure_monitor as m
import research_pipeline as p
import retrieval
import prepare_updates
import serve
import stock_brain as kb


class AssistantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = kb.ROOT
        cls.records = kb.export_records(cls.root)
        cls.universe = p.universe(cls.root)

    def retrieve(self, q):
        return retrieval.retrieve(q, self.records, self.universe, root=self.root)

    def test_hebrew_casefold_and_unknown_comparison(self):
        for q in ['מה עושה אורקל?', 'what does orcl do?', 'מהו המודל העסקי של אורקל?']:
            r = self.retrieve(q)
            self.assertFalse(r['abstain'], q)
            self.assertEqual(r['entities'], ['ORCL'])
        for q in ['Compare Microsoft and WidgetCo', 'Compare MSFT and AAPL business', 'מה המחיר של אורקל?', 'What will MSFT revenue be in 2035?']:
            self.assertTrue(self.retrieve(q)['abstain'], q)

    def test_both_comparison_issuers_and_relationship_relevance(self):
        out=a.answer('השווה את המודל העסקי של מיקרוסופט ואורקל.',self.root)
        self.assertEqual({s['ticker'] for s in out['statements']},{'MSFT','ORCL'})
        out=a.answer('מה הקשר בין מיקרון לאנבידיה?',self.root)
        self.assertFalse(out['abstain'])
        self.assertTrue(all('Hugging Face' not in s['text'] for s in out['statements']))

    def test_all_bound_translations_and_numeric_parity(self):
        count=0
        for c in self.universe:
            packet=p.read_json(p.managed_packet_path(self.root,c['ticker']))
            for section in packet['sections'].values():
                for claim in section.get('claims',[]):
                    text=a.translated_claim(self.root,packet,claim)
                    self.assertIsNotNone(text)
                    self.assertEqual(a.numbers(text),a.numbers(claim['text']))
                    count+=1
        self.assertGreaterEqual(count,160)

    def test_reject_changed_number_citation_basis_and_source(self):
        original=a.answer('What are ORCL GAAP earnings?',self.root,language='en')
        self.assertFalse(original['abstain'])
        for mutation in [lambda o:o['statements'][0].update(text='Revenue was USD 1 million.'),
                         lambda o:o['statements'][0].update(citations=[]),
                         lambda o:o['statements'][0].update(kind='derived'),
                         lambda o:o['sources'][0].update(url='https://example.com/wrong')]:
            out=copy.deepcopy(original);mutation(out)
            with self.assertRaises(ValueError):a.validate_answer(out,self.root)

    def test_changed_translation_fails_closed(self):
        packet=p.read_json(p.managed_packet_path(self.root,'ORCL'))
        claim=packet['sections']['business-overview']['claims'][0]
        locale=p.read_json(self.root/'research/locales/he/ORCL.json')
        locale['claims'][claim['id']]['text']+=' שינוי'
        with patch.object(p,'read_json',return_value=locale):
            with self.assertRaises(ValueError):a.translated_claim(self.root,packet,claim)
        locale['claims'][claim['id']]['source_sha256']='old'
        with patch.object(p,'read_json',return_value=locale):self.assertIsNone(a.translated_claim(self.root,packet,claim))

    def test_latest_question_blocks_unknown_or_pending_freshness(self):
        for report in [None, {'companies':{}}]:
            out=a.answer('What are the latest MSFT financial results?',self.root,monitor_report=report)
            self.assertTrue(out['abstain'])
            self.assertEqual(out['reason_code'],'freshness_unverified')
        out=a.answer('What are MSFT FY2026 financial results?',self.root,monitor_report={})
        self.assertFalse(out['abstain'])

    def test_bad_predictions_make_cli_fail(self):
        cases=p.read_json(self.root/'eval/acceptance-v1.json')['cases']
        predictions={c['id']:{'abstain':c['expected_behavior']=='answer','chunk_ids':[]} for c in cases}
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/'wrong.json';p.write_json(path,predictions)
            run=subprocess.run([sys.executable,str(self.root/'scripts/evaluate_retrieval.py'),'--cases','eval/acceptance-v1.json','--predictions',str(path),'--output',str(Path(temp)/'report.json')],capture_output=True,text=True)
            self.assertEqual(run.returncode,2,run.stdout+run.stderr)

    def test_feed_dates_and_https_validation(self):
        raw=b'<rss><channel><item><title>A &amp; B</title><link>https://example.com/a</link><pubDate>Sun, 18 Oct 2026 08:00:00 GMT</pubDate></item><item><link>https://example.com/b</link></item><item><link>javascript:bad()</link></item></channel></rss>'
        events=m.parse_feed(raw,'MSFT','https://example.com/feed')
        self.assertEqual(len(events),2)
        self.assertEqual(events[0]['published_at'],'2026-10-18')
        self.assertIsNone(events[1]['published_at'])
        atom=b'<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>New</title><link href="https://example.com/c"/><updated>2026-10-18T08:00:00Z</updated></entry></feed>'
        self.assertEqual(m.parse_feed(atom,'MSFT','https://example.com/feed')[0]['published_at'],'2026-10-18')

    def test_queue_never_disappears_or_self_approves(self):
        event={'id':'a','ticker':'MSFT','url':'https://example.com/a','kind':'issuer_feed','published_at':None}
        packets={'MSFT':{'sources':[]}}
        q=m.reconciled_queue([], [event], packets, {}, 'now')
        self.assertEqual(q[0]['status'],'pending_review')
        q=m.reconciled_queue(q, [], packets, {}, 'later')
        self.assertEqual(q[0]['status'],'pending_review')
        packets['MSFT']['sources']=[{'url':event['url']}]
        self.assertEqual(m.reconciled_queue(q, [], packets, {}, 'later')[0]['status'],'pending_review')
        q=m.reconciled_queue(q, [], packets, {'MSFT':'approved-hash'}, 'later')
        self.assertEqual(q[0]['resolved_by_profile_sha256'],'approved-hash')
        self.assertEqual(m.reconciled_queue(q, [], packets, {}, 'later')[0]['status'],'pending_review')

    def test_failed_discovery_preserves_pending_and_does_not_change_research(self):
        before=p.digest(p.managed_packet_path(self.root,'MSFT').read_bytes())
        previous={'queue':[{'id':'keep','ticker':'MSFT','url':'https://example.com/pending','title':'Pending','kind':'issuer_feed','published_at':None}]}
        with patch.object(m.pipeline.Fetcher,'fetch',side_effect=OSError('test unavailable')):
            report=m.run(self.root,'Test contact',previous=previous)
        self.assertEqual(report['companies']['MSFT']['status'],'error')
        self.assertEqual(report['queue'][0]['id'],'keep')
        self.assertEqual(before,p.digest(p.managed_packet_path(self.root,'MSFT').read_bytes()))

    def test_freshness_expiry_historical_cutoff_and_changed_packet(self):
        now=datetime.now(timezone.utc)
        state={'status':'checked','checked_at':now.isoformat(),'packet_sha256':p.digest(p.managed_packet_path(self.root,'MSFT').read_bytes()),'pending_count':0}
        report={'cutoff':now.date().isoformat(),'companies':{'MSFT':state}}
        self.assertEqual(m.freshness(self.root,'MSFT',report,now)['status'],'checked')
        self.assertEqual(m.freshness(self.root,'MSFT',report,now+timedelta(days=3))['status'],'stale_check')
        report['cutoff']='2020-01-01'
        self.assertEqual(m.freshness(self.root,'MSFT',report,now)['status'],'unknown')
        state['packet_sha256']='changed'
        self.assertEqual(m.freshness(self.root,'MSFT',report,now)['status'],'unknown')

    def test_overlap_discovers_missed_pre_cutoff_filing(self):
        company=p.issuer(self.root,'MSFT')
        data={'cik':company['cik'],'filings':{'recent':{'form':['8-K'],'accessionNumber':['0000789019-26-999999'],'filingDate':['2026-10-01'],'primaryDocument':['event.htm']}}}
        class Fake:
            def fetch(self,*args,**kwargs):return json.dumps(data).encode(),{}
        events=m.discover_sec(company,{'as_of':'2026-10-18','sources':[]},Fake(),'2026-10-18','2026-07-20')
        self.assertEqual(len(events),1)

    def test_preparation_is_bounded_persistent_and_does_not_approve(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            packet=root/'research/pilot/MSFT.json';p.write_json(packet,{'ticker':'MSFT'})
            report_path=root/'latest.json'
            events=[{'id':str(i),'ticker':'MSFT','status':'pending_review','url':f'https://example.com/{i}',
                     'title':'New event','published_at':'2026-10-18','kind':'issuer_feed'} for i in range(12)]
            p.write_json(report_path,{'cutoff':'2026-10-18','queue':events})
            company={'ticker':'MSFT','company_name':'Microsoft','extra_sources':[]}
            with patch.object(p,'issuer',return_value=company), patch.object(p,'collect',return_value={'errors':[]}), patch.object(p,'prepare_request',return_value={}) as request:
                first=prepare_updates.prepare(root,report_path,1)
                self.assertEqual(first['jobs'][0]['selected_count'],10)
                second=prepare_updates.prepare(root,report_path,1)
                self.assertEqual(second['jobs'][0]['selected_count'],2)
                third=prepare_updates.prepare(root,report_path,1)
                self.assertEqual(third['jobs'],[])
                self.assertEqual(request.call_count,2)
            self.assertTrue(all(e['status']=='pending_review' for e in p.read_json(report_path)['queue']))

    def test_local_http_api_and_static_content(self):
        server=ThreadingHTTPServer(('127.0.0.1',0),partial(serve.Handler,root=self.root))
        thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        url='http://127.0.0.1:'+str(server.server_port)
        try:
            with urllib.request.urlopen(url) as response:
                self.assertIn("script-src 'self'",response.headers['Content-Security-Policy'])
                self.assertIn('Stock Brain',response.read().decode())
            req=urllib.request.Request(url+'/api/ask',json.dumps({'question':'מה עושה אורקל?'}).encode(),{'Content-Type':'application/json'})
            with urllib.request.urlopen(req) as response:
                result=json.load(response);self.assertFalse(result['abstain']);self.assertEqual(result['language'],'he')
            req=urllib.request.Request(url+'/api/ask',b'{}',{'Content-Type':'application/json','Origin':'https://other.example'})
            with self.assertRaises(urllib.error.HTTPError) as error:urllib.request.urlopen(req)
            self.assertEqual(error.exception.code,403)
        finally:server.shutdown();server.server_close();thread.join()


if __name__=='__main__':unittest.main()
