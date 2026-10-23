import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {parseHTML} from 'linkedom';

test('Registry loads bounded pages and shows dated draft comparisons without research approval',async()=>{
  const snapshot=JSON.parse(fs.readFileSync(new URL('../data/desk.json',import.meta.url),'utf8'));
  const {document,window}=parseHTML(fs.readFileSync(new URL('../site/index.html',import.meta.url),'utf8'));
  globalThis.document=document;globalThis.Node=window.Node;
  const priorFetch=globalThis.fetch,requests=[];
  let warming=false;
  const issuer={cik:'0000000123',ticker:'SYNTH',company_name:'Synthetic Issuer',listings:[{ticker:'SYNTH'}],collection_status:'registry-only'};
  const security={listing_key:'a'.repeat(32),security_name:'Synthetic Issuer',ticker:'SYNTH',exchange:'NASDAQ',cik:issuer.cik,instrument_type:'common_stock',datasets:{},source:{url:'https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt'}};
  const brain={available:true,url:'https://github.com/eladyesh/stock-brain/blob/'+ 'a'.repeat(40)+'/brain/companies/0000000123/README.md',raw_url:'https://raw.githubusercontent.com/eladyesh/stock-brain/'+ 'a'.repeat(40)+'/brain/companies/0000000123/README.md',created_at:'2026-10-22T00:00:00Z',matches_current_data:false};
  const detail={company:issuer,brain,collection_status:'review-required',research:{as_of:null,canonical_reviewed:false},
    collected:{history:{source:{retrieved_at:'2026-10-22T10:00:00+00:00'},
      periods:[{id:'annual-fixture',type:'annual',start:'2025-01-01',end:'2025-12-31'}],
      financials:{'annual-fixture':{revenue:{value:100e6,unit:'USD',model_usable:false,provenance:[{url:'https://www.sec.gov/Archives/edgar/data/123/annual.htm'}]}}}},
      submissions:{recent_filing_inventory:[{form:'20-F',filed:'2026-04-01',url:'https://www.sec.gov/Archives/edgar/data/123/foreign.htm'}]},automatic_changes:{changes:[{
      metric:'revenue',previous_value:100e6,value:120e6,unit:'USD',delta:null,comparison:'blocked',
      previous_period_start:'2025-01-01',previous_period_end:'2025-12-31',period_start:'2026-01-01',period_end:'2026-09-30',
      source_urls:['https://www.sec.gov/Archives/edgar/data/123/fixture.htm'],
    }],limitations:[]}},ttm:null};
  globalThis.fetch=async url=>{
    requests.push(url);
    const value=url.startsWith('./api/securities?')?(warming?{items:[],total:0,directory:{status:'unavailable'}}:{items:[security],total:50000,limit:25,offset:0,brain:{available:true,sectors_url:'https://github.com/eladyesh/stock-brain/blob/main/sectors/README.md',company_profiles:1,unresolved_listings:2,created_at:brain.created_at,index_url:'https://github.com/eladyesh/stock-brain/blob/'+ 'a'.repeat(40)+'/brain/INDEX.md',download_url:'https://github.com/eladyesh/stock-brain/archive/'+ 'a'.repeat(40)+'.zip'},
      directory:{coverage_progress:{total_listings:50000,mapped_listings:2,unmapped_listings:49998,distinct_mapped_issuers:1,
        filing_checks:{recent:0,overdue:2,not_checked:49998}}}}):
      url==='./api/securities/'+security.listing_key?{security}:
      url==='./api/companies/0000000123'?detail:snapshot;
    return {ok:true,json:async()=>structuredClone(value)};
  };
  const settle=()=>new Promise(resolve=>setTimeout(resolve,0));
  try{
    await import('../site/app.mjs?coverage-ui');await settle();
    [...document.querySelectorAll('.nav-button')].find(x=>x.textContent.includes('מרשם החברות')).click();await settle();
    assert(requests.some(x=>x.includes('limit=25&offset=0')));
    assert.equal(document.querySelectorAll('.registry-row').length,1);
    assert(document.getElementById('content').textContent.includes('50000 ניירות תואמים'));
    assert(document.getElementById('content').textContent.includes('ממתינות לקישור: 49998'));
    assert(document.getElementById('content').textContent.includes('חברות מזוהות שונות: 1'));
    assert(document.getElementById('content').textContent.includes('בדיקה מתעכבת: 2'));
    assert(document.getElementById('content').textContent.includes('Brain: 1 קובצי חברות'));
    assert(document.querySelector('a[href="https://github.com/eladyesh/stock-brain/blob/main/sectors/README.md"]'));
    assert(document.getElementById('companies').hidden);
    assert(document.getElementById('reviewed-search').hidden);
    assert(document.getElementById('coverage-count').textContent.includes('50000'));
    document.querySelector('.registry-row button').click();await settle();
    assert(document.getElementById('content').textContent.includes('תחזיות אנליסטים'));
    assert(document.getElementById('content').textContent.includes('טרם נאסף'));
    [...document.querySelectorAll('button')].find(x=>x.textContent==='הצג נתונים פיננסיים ומחקר ←').click();await settle();
    const text=document.getElementById('content').textContent;
    assert(text.includes('מחקר שנבדק: טרם הושלם'));
    assert(document.querySelector('a[href="'+brain.url+'"]'));
    assert(document.querySelector('a[href="'+brain.raw_url+'"]'));
    assert(text.includes('הקובץ מבוסס על עדכון נתונים קודם'));
    assert(text.includes('הדוח השנתי האחרון במאגר'));
    assert(text.includes('דורש בדיקה לפני השוואה או חישוב'));
    assert(text.includes('דיווחים אחרונים ל־SEC'));
    assert(document.querySelector('a[href="https://www.sec.gov/Archives/edgar/data/123/foreign.htm"]'));
    assert(text.includes('השוואה חסומה'));
    assert(text.includes('2026-01-01 – 2026-09-30'));
    assert.equal(document.querySelectorAll('pre').length,0);
    assert(document.querySelector('a[href="https://www.sec.gov/Archives/edgar/data/123/fixture.htm"]'));
    assert(!text.includes('NaN'));
    [...document.querySelectorAll('button')].find(x=>x.textContent==='הבא').click();await settle();
    assert(requests.some(x=>x.includes('limit=25&offset=25')));
    warming=true;
    [...document.querySelectorAll('button')].find(x=>x.textContent==='הבא').click();await settle();
    assert(document.getElementById('content').textContent.includes('מאגר המניות נטען כעת'));
    assert(!document.getElementById('content').textContent.includes('0 ניירות תואמים'));
    [...document.querySelectorAll('.nav-button')].find(x=>x.textContent.includes('תמונת המחקר')).click();
    assert(!document.getElementById('companies').hidden);
  }finally{globalThis.fetch=priorFetch;}
});
