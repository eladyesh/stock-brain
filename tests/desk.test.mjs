import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {ask,scenario} from '../site/engine.mjs';
const data=JSON.parse(fs.readFileSync(new URL('../data/desk.json',import.meta.url)));
const cases=JSON.parse(fs.readFileSync(new URL('../eval/acceptance-v1.json',import.meta.url))).cases;

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
  'What was MSFT revenue in Q1 FY2026?',
  'מה היו הכנסות מיקרוסופט ברבעון הראשון של 2026?',
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
  'What was MU revenue in fiscal Q1 2026?',
  'What was MSFT revenue in FY2024?',
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
  globalThis.fetch=async()=>({ok:true,json:async()=>structuredClone(data)});
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
    nav[1].click();
    assert(document.querySelectorAll('table tbody tr').length>=20);
    assert.equal(document.querySelectorAll('thead th').length,6);
    const quarter=Array.from(document.querySelectorAll('.segmented button')).find(b=>b.textContent==='רבעוני');
    quarter.click();assert.equal(document.querySelectorAll('thead th').length,13);
    nav[3].click();
    document.getElementById('scenario-eps').value='10';
    document.getElementById('scenario-price').value='200';
    document.getElementById('scenario-form').dispatchEvent(new window.Event('submit',{cancelable:true}));
    assert.equal(document.querySelectorAll('.scenario-card').length,3);
    assert(!document.getElementById('scenario-result').textContent.includes('NaN'));
    document.getElementById('question').value='מה עושה אורקל?';
    document.getElementById('question-form').dispatchEvent(new window.Event('submit',{cancelable:true}));
    assert(document.querySelectorAll('#answer .claim').length>0);
    document.getElementById('question').value='What was MSFT revenue in Q1 FY2026?';
    document.getElementById('question-form').dispatchEvent(new window.Event('submit',{cancelable:true}));
    assert.equal(document.querySelectorAll('#answer .claim').length,0);
    assert(document.querySelector('#answer .notice.amber'));
    for(const button of document.querySelectorAll('.company-button'))button.click();
    assert(document.querySelector('.company-button.active'));
    assert.equal(document.querySelectorAll('a[href="#"]').length,0,'No dead source links');
  }finally{globalThis.fetch=oldFetch;}
});

