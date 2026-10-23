import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {ask,scenario} from '../site/engine.mjs';
const data=JSON.parse(fs.readFileSync(new URL('../data/desk.json',import.meta.url)));
const cases=JSON.parse(fs.readFileSync(new URL('../eval/acceptance-v1.json',import.meta.url))).cases;
const historicalCases=JSON.parse(fs.readFileSync(new URL('./historical-answer-cases.json',import.meta.url)));

const semanticCases=JSON.parse(fs.readFileSync(new URL('./semantic-holdout-cases.json',import.meta.url)));
for(const c of semanticCases)test('Independent semantic contract: '+c.question,()=>{
  const out=ask(c.question,data);assert.equal(out.abstain,c.abstain||false,JSON.stringify(out));
  if(out.abstain){assert.equal(out.reason_code,c.reason);assert.deepEqual(out.statements,[]);return;}
  assert.equal(out.statements.length,1);assert.equal(out.statements[0].metric,c.metric);assert.equal(out.statements[0].unit,c.unit);
});

for(const c of historicalCases)test('Exact historical answer: '+c.question,()=>{
  const out=ask(c.question,data);
  assert.equal(out.abstain,c.abstain||false,c.question+' '+out.reason_code);
  if(out.abstain){assert.deepEqual(out.statements,[]);if(c.reason)assert.equal(out.reason_code,c.reason);return;}
  assert.equal(out.mode,'financial_history');assert.equal(out.statements.length,1);
  const row=out.statements[0];
  assert.deepEqual([row.ticker,row.value,row.period_start,row.period_end],[c.ticker,c.value,c.start,c.end]);
  assert(row.sources.some(s=>s.url.startsWith('https://www.sec.gov/Archives/')&&s.locator.includes('us-gaap:')));
  assert(row.sources.every(s=>s.url.startsWith('https://')&&s.locator));
  if(c.review_source_id)assert(row.sources.some(s=>s.id===c.review_source_id),'Exact-period share review evidence must accompany newly eligible EPS');
});

test('Historical comparison returns every issuer or abstains',()=>{
  const q='Compare MSFT and PLTR revenue in FY2024';
  const result=ask(q,data);assert.equal(result.abstain,false);
  assert.deepEqual(new Set(result.statements.map(s=>s.ticker)),new Set(['MSFT','PLTR']));
  const missing=structuredClone(data);missing.companies.find(c=>c.ticker==='PLTR').historical_index=[];
  assert.equal(ask(q,missing).abstain,true);assert.deepEqual(ask(q,missing).statements,[]);
});

for(const c of cases)test('Browser evidence gate '+c.id,()=>{
  const out=ask(c.question,data);
  if(c.expected_behavior==='abstain'){assert.equal(out.abstain,true);assert.deepEqual(out.statements,[]);return;}
  assert.equal(out.abstain,false,c.question+' '+out.reason_code);
  for(const expected of c.evidence){
    assert(out.statements.some(s=>s.section===expected.section_id&&
      data.companies.find(x=>x.ticker===s.ticker)?.history?.company_id===expected.document_id&&
      expected.source_ids.every(id=>s.sources.some(source=>source.id===id))),c.id+' evidence missing');
  }
  for(const statement of out.statements){
    assert(statement.sources.length>0);
    assert(statement.sources.every(s=>s.url.startsWith('https://')&&s.locator));
  }
});
for(const q of [
  'What was MSFT revenue excluding Azure in FY2026?',
  'מה שיעור הרווח הגולמי של אנבידיה?',
  'What is NVDA gross margin?',
  'What is MSFT operating margin?',
  'What is MSFT free cash flow?',
  'What was MSFT inflation-adjusted revenue in FY2026?',
  'What was MSFT revenue per employee in FY2026?',
  'What was MSFT Azure revenue in FY2026?',
  'Compare NVDA and AMD revenue in 2027',
  'Compare MSFT and ORCL revenue in Q1 FY2027',
  'What was NVDA annual revenue in FY2027?',
  'What was MSFT FY2026 adjusted EPS?',
  'Compare MSFT GAAP and adjusted EPS in FY2026',
  'What are MSFT net income and ROIC?',
  'What was MSFT revenue in Q1 and Q2 FY2026?',
  'What was NVDA revenue in Q2 2027?',
])test('Browser numerical rejection: '+q,()=>assert.equal(ask(q,data).abstain,true));

for(const q of ['Was AVAV profitable on a GAAP basis in fiscal Q1 2027 despite positive adjusted EBITDA?','What was MSFT FY2026 GAAP revenue and net income?','What was ORCL GAAP revenue in FY2027 Q1?','Give MU fiscal Q4 2026 revenue and gross margin.','What was NVDA revenue in Q2 FY2027?'])
  test('Browser exact numerical support: '+q,()=>assert.equal(ask(q,data).abstain,false));

test('Scenario math is deterministic and rejects unsupported inputs',()=>{
  const s=scenario(10,.1,20,3,200);
  assert(Math.abs(s.terminalPrice-266.2)<1e-8);
  assert(Math.abs(s.annualized-.1)<1e-8);
  for(const v of [[0,.1,20,3,200],[10,-1,20,3,200],[10,.1,NaN,3,200],[10,.1,20,3,0]])assert.throws(()=>scenario(...v));
});

test('All UI views, question submission and scenario calculation render with real snapshot',async()=>{
  const {parseHTML}=await import('linkedom');
  const {document,window}=parseHTML(fs.readFileSync(new URL('../site/index.html',import.meta.url),'utf8'));
  globalThis.document=document;globalThis.Node=window.Node;
  const oldFetch=globalThis.fetch;
  globalThis.fetch=async(url,options)=>({ok:true,json:async()=>url==='./api/ask'?ask(JSON.parse(options.body).question,data):structuredClone(data)});
  try{
    await import('../site/app.mjs');
    await new Promise(resolve=>setTimeout(resolve,0));
    assert.equal(document.querySelectorAll('.company-button').length,10);
    const nav=Array.from(document.querySelectorAll('.nav-button'));
    for(const button of nav){
      button.click();
      assert(document.getElementById('content').textContent.trim().length>100);
      assert.equal(document.querySelectorAll('.nav-button[aria-current="page"]').length,1);
    }
    nav.find(button=>button.textContent.includes('היסטוריה פיננסית')).click();
    assert(document.querySelectorAll('table tbody tr').length>=20);
    assert.equal(document.querySelectorAll('thead th').length,6);
    const quarter=Array.from(document.querySelectorAll('.segmented button')).find(b=>b.textContent==='רבעוני');
    quarter.click();assert.equal(document.querySelectorAll('thead th').length,13);
    nav.find(button=>button.textContent.includes('תרחישי שווי')).click();
    document.getElementById('scenario-eps').value='10';
    document.getElementById('scenario-price').value='200';
    document.getElementById('scenario-form').dispatchEvent(new window.Event('submit',{cancelable:true}));
    assert.equal(document.querySelectorAll('.scenario-card').length,3);
    assert(!document.getElementById('scenario-result').textContent.includes('NaN'));
    document.getElementById('question').value='מה עושה אורקל?';
    document.getElementById('question-form').dispatchEvent(new window.Event('submit',{cancelable:true}));
    await new Promise(resolve=>setTimeout(resolve,0));
    assert(document.querySelectorAll('#answer .claim').length>0);
    document.getElementById('question').value='What was MSFT revenue in calendar year 2026?';
    document.getElementById('question-form').dispatchEvent(new window.Event('submit',{cancelable:true}));
    await new Promise(resolve=>setTimeout(resolve,0));
    assert.equal(document.querySelectorAll('#answer .claim').length,0);
    assert(document.querySelector('#answer .notice.amber'));
    document.getElementById('question').value='מה היו ההכנסות של מיקרוסופט בשנת הכספים 2024?';
    document.getElementById('question-form').dispatchEvent(new window.Event('submit',{cancelable:true}));
    await new Promise(resolve=>setTimeout(resolve,0));
    assert(document.getElementById('answer').textContent.includes('245,122,000,000'));
    assert(document.getElementById('answer').textContent.includes('2023-07-01'));
    assert(document.getElementById('answer').textContent.includes('שכבה נפרדת'));
    for(const button of document.querySelectorAll('.company-button'))button.click();
    assert(document.querySelector('.company-button.active'));
    assert.equal(document.querySelectorAll('a[href="#"]').length,0,'No dead source links');
  }finally{globalThis.fetch=oldFetch;}
});

test('Unavailable or incompatible remote data keeps a labelled usable snapshot',async()=>{
  const {parseHTML}=await import('linkedom');
  const {document,window}=parseHTML(fs.readFileSync(new URL('../site/index.html',import.meta.url),'utf8'));
  globalThis.document=document;globalThis.Node=window.Node;
  const oldFetch=globalThis.fetch;
  globalThis.fetch=async url=>url==='./snapshot.json'?{ok:true,json:async()=>structuredClone(data)}:{ok:false,status:404};
  try{
    await import('../site/app.mjs?offline-test');await new Promise(resolve=>setTimeout(resolve,0));
    assert(document.getElementById('data-status').textContent.includes('לא התקבל עדכון'));
    assert.equal(document.querySelectorAll('.company-button').length,data.companies.length);
    document.getElementById('question').value='How does Microsoft make money?';
    document.getElementById('question-form').dispatchEvent(new window.Event('submit',{cancelable:true}));
    await new Promise(resolve=>setTimeout(resolve,0));
    assert(document.getElementById('answer').textContent.includes('העותק שנטען בדפדפן'));
    assert(document.querySelectorAll('#answer .claim').length>0);
    const legacy=structuredClone(data);delete legacy.answer_contract_version;
    globalThis.fetch=async()=>({ok:true,json:async()=>legacy});
    document.getElementById('refresh').click();await new Promise(resolve=>setTimeout(resolve,0));
    assert(document.getElementById('data-status').textContent.includes('לא התקבל עדכון'));
    assert.equal(document.querySelectorAll('.company-button').length,data.companies.length);
  }finally{globalThis.fetch=oldFetch;}
});


for(const q of ['MSFT revenue in latest available fiscal year','MSFT revenue in latest available quarter','MSFT revenue in Latest Available Quarter','מה ההכנסות של מיקרוסופט ברבעון האחרון במאגר?'])
  test('Latest stored period is explicit and cited: '+q,()=>{
    const result=ask(q,data);assert.equal(result.abstain,false);assert(result.availability_note);assert(result.selected_period.end);assert(result.statements.every(s=>s.sources.length));
  });
for(const q of ['MSFT current revenue in latest available quarter','Compare MSFT and NVDA revenue in latest available year','MSFT revenue in latest available calendar year','MSFT revenue in latest available quarter FY2024','MSFT Azure revenue in latest available quarter','MSFT consensus revenue in latest available year'])
  test('Latest stored period cannot relax a scope guard: '+q,()=>assert.equal(ask(q,data).abstain,true));
test('Latest stored period never falls back to an older usable cell',()=>{
  const changed=structuredClone(data),company=changed.companies.find(c=>c.ticker==='MSFT');
  const end=company.history.periods.filter(p=>p.type==='annual').sort((a,b)=>b.end.localeCompare(a.end))[0].end;
  company.metric_index=[];
  company.historical_index.filter(r=>r.period_end===end&&r.metric_keys.includes('revenue')).forEach(r=>r.model_usable=false);
  assert.equal(ask('MSFT revenue in latest available year',changed).abstain,true);
});
