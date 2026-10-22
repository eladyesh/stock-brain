import test from 'node:test';
import assert from 'node:assert/strict';
import {personalStore,changesSinceVisit,groupQueue} from '../site/workbench.mjs';

test('Personal research survives reload without changing canonical data',()=>{
  const memory=new Map(),storage={getItem:k=>memory.get(k),setItem:(k,v)=>memory.set(k,v)};
  const first=personalStore(storage),data={companies:[{ticker:'MSFT',as_of:'2026-10-20'}],queue:[{id:'old'}]};
  const original=JSON.stringify(data);
  assert(first.saveNote('MSFT','<script>personal text</script>'));
  assert(first.saveScenario('MSFT','2026-10-22',{scenarioId:'base',revenueGrowth:.15}));
  assert(first.markVisit(data));
  const next=personalStore(storage);
  assert.equal(next.note('MSFT').text,'<script>personal text</script>');
  assert.equal(next.scenario('MSFT').overrides.revenueGrowth,.15);
  assert.equal(JSON.stringify(data),original);
  const changed=structuredClone(data);changed.built_at='2030-01-01';
  assert.deepEqual(changesSinceVisit(changed,next.previousVisit).companies,[]);
  changed.companies[0].thesis={as_of:'2026-10-22'};changed.queue.push({id:'new'});
  const delta=changesSinceVisit(changed,next.previousVisit);
  assert.deepEqual(delta.companies,['MSFT']);assert.deepEqual(delta.events,[{id:'new'}]);
});
test('Unavailable and corrupt local storage do not imply a successful save',()=>{
  for(const storage of [null,{getItem:()=>'{bad',setItem:()=>{throw Error('quota')}}]){
    const state=personalStore(storage);assert.equal(state.note('MSFT'),null);
    assert.equal(state.saveNote('MSFT','notes'),false);
  }
});
test('Related earnings documents retain individual review status and unrelated filings stay separate',()=>{
  const entries=[
    {event_id:'release',ticker:'RTX',published_at:'2026-10-20',title:'RTX Reports Q3 2026 Results',priority:'P0',queue_status:'reviewed'},
    {event_id:'8k',ticker:'RTX',published_at:'2026-10-20',title:'RTX 8-K',priority:'P0',queue_status:'pending_review'},
    {event_id:'10q',ticker:'RTX',published_at:'2026-10-20',title:'RTX 10-Q',url:'https://www.sec.gov/Archives/rtx-20260930.htm',priority:'P0',queue_status:'pending_review'},
    {event_id:'leadership',ticker:'RTX',published_at:'2026-10-20',title:'RTX 8-K',priority:'P1',queue_status:'pending_review'},
    {event_id:'other',ticker:'LMT',published_at:'2026-10-20',title:'LMT 8-K',priority:'P0',queue_status:'pending_review'},
  ];
  const events=[{id:'release',kind:'issuer_feed'},{id:'8k',kind:'sec_filing',form:'8-K',items:'2.02,9.01'},
    {id:'10q',kind:'sec_filing',form:'10-Q'},{id:'leadership',kind:'sec_filing',form:'8-K',items:'5.02'},
    {id:'other',kind:'sec_filing',form:'8-K',items:'2.02'}];
  const groups=groupQueue(entries,events),earnings=groups.find(g=>g.id.startsWith('earnings:'));
  assert.equal(groups.length,3);assert.equal(earnings.pending,2);assert.equal(earnings.entries.length,3);
  assert.equal(groups.flatMap(g=>g.entries).length,entries.length);
  assert.equal(entries[0].queue_status,'reviewed');
});
