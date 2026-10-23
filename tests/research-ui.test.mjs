import test from 'node:test';
import assert from 'node:assert/strict';
import {parseHTML} from 'linkedom';
import {researchView,markdownView} from '../site/research.mjs';

function setup(){
  const {document,window}=parseHTML('<html><body><main></main></body></html>');
  const h=(tag,attrs={},...children)=>{const el=document.createElement(tag);for(const [k,v] of Object.entries(attrs)){if(v===null||v===undefined)continue;if(k.startsWith('on'))el.addEventListener(k.slice(2).toLowerCase(),v);else if(k==='value'||k==='disabled')el[k]=v;else el.setAttribute(k,v);}for(const c of children.flat(Infinity))if(c!==null&&c!==undefined)el.append(c instanceof window.Node?c:document.createTextNode(String(c)));return el;};
  const ui={h,card:(title,body)=>h('section',{},h('h2',{},title),body),button:(text,fn,cls)=>h('button',{onClick:fn,class:cls},text),note:text=>h('p',{},text),link:(text,url)=>h('a',{href:url?.startsWith('https://')?url:'#'},text),date:x=>x||'לא זמין',option:(v,text,selected)=>h('option',{value:v,selected:selected?'':null},text),sections:{'business-overview':'איך העסק עובד','financial-performance':'ביצועים פיננסיים','sources-and-change-log':'מקורות'}};
  return {document,window,ui};
}

test('whole-market research searches symbols, renders evidence and preserves incomplete statuses',async()=>{
  const {document,window,ui}=setup(),requests=[],previous=globalThis.fetch;
  const row={cik:'0000000001',tickers:['SYNTH'],symbol:'SYNTH',company_name:'Synthetic Company',sector:'industrials',research:{stage:'evidence_collected'}};
  const page={available:true,items:[row],total:1,company_profiles:5634,financial_profiles:4052,sector_counts:{industrials:764},source_created_at:'2026-10-23',research_queue:{counts:{evidence_collected:1,pending:5633},stop_reason:null}};
  const item={company:row,sections:{'business-overview':'Source excerpt:\n\n> Synthetic source evidence. [S01]\n\n<script>alert(1)</script>','financial-performance':'Derived observation: 10%. [S01]\n\n| Metric | Value |\n| --- | ---: |\n| Revenue | 100 |','sources-and-change-log':'[S01]'},sources:[{id:'S01',title:'Synthetic report',url:'https://www.sec.gov/fixture'}],research:{stage:'evidence_collected',evidence_topics:['business-overview'],derived_observations:1},markdown_url:'https://github.com/eladyesh/stock-brain/blob/main/sectors/industrials/facts/SYNTH/README.md',full_history_url:'https://github.com/eladyesh/stock-brain',canonical_reviewed:false};
  globalThis.fetch=async url=>{requests.push(url);return {ok:true,json:async()=>structuredClone(url.startsWith('./api/research?')?page:item)};};
  const settle=()=>new Promise(resolve=>setTimeout(resolve,0));
  try{
    document.querySelector('main').append(...researchView(ui));await settle();
    assert(document.body.textContent.includes('5634'));
    assert(!document.body.textContent.includes('null'));
    assert(document.querySelector('.registry-row h3').textContent==='SYNTH');
    assert(!document.querySelector('.registry-row').textContent.includes(row.cik));
    document.querySelector('.registry-row button').click();await settle();
    assert(document.querySelector('.research-detail').textContent.includes('טרם נבדקו'));
    assert(document.querySelector('blockquote').textContent.includes('Synthetic source evidence'));
    assert(document.querySelector('a[href="https://www.sec.gov/fixture"]'));
    assert.equal(document.querySelectorAll('script').length,0);
    [...document.querySelectorAll('.research-topic')].find(b=>b.textContent==='ביצועים פיננסיים').click();
    assert.equal(document.querySelectorAll('table').length,1);
    assert(document.querySelector('table').textContent.includes('100'));
    document.querySelector('input').value='OTHER';
    document.querySelector('form').dispatchEvent(new window.Event('submit',{cancelable:true}));await settle();
    assert(requests.some(url=>url.includes('q=OTHER')));
    assert.equal(document.querySelector('.research-detail').textContent,'');
  }finally{globalThis.fetch=previous;}
});

test('source Markdown cannot inject HTML or executable links',()=>{
  const {document,ui}=setup();
  document.body.append(markdownView('[x](javascript:alert(1))\n\n<img src=x onerror=alert(1)>\n\n**Reported** value [S01]',[{id:'S01',url:'https://example.test/source'}],ui));
  assert.equal(document.querySelectorAll('img,script').length,0);
  assert.equal(document.querySelectorAll('a').length,1);
  assert.equal(document.querySelector('strong').textContent,'Reported');
});
