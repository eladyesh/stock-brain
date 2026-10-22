import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {ask} from '../site/engine.mjs';

// The questions and numerical oracle were authored independently before the
// implementation was inspected. This runner was added afterwards. Source-content
// and financial-interpretation review remains a separate independent AI check.
const frozenBytes=fs.readFileSync(new URL('./workbench-questions.json',import.meta.url));
const suite=JSON.parse(frozenBytes);
const data=JSON.parse(fs.readFileSync(new URL('../data/desk.json',import.meta.url)));
assert.equal(createHash('sha256').update(frozenBytes).digest('hex'),
  '132cbd83497a1819befe461df0412911ac5ce88fce95be72395829ae1866b28e',
  'Do not weaken frozen questions to accommodate an implementation failure.');
assert.equal(suite.cases.length,35);

function assertRefusal(result){
  assert.equal(result.abstain,true);
  assert.deepEqual(result.statements,[],'A refusal must not retain a partial answer.');
  assert.equal(typeof result.reason_code,'string');
  assert(result.reason?.trim(),'An unsupported request needs an explicit explanation.');
}

function assertAnsweredScope(result,c){
  assert.equal(result.abstain,false,`${c.id}: ${result.reason_code}: ${result.reason}`);
  assert(result.statements.length>0,'An answer needs evidence-bearing statements.');
  assert.deepEqual([...new Set(result.statements.map(s=>s.ticker))].sort(),[...c.tickers].sort(),
    'The answer must retain every requested issuer.');
  assert.equal(result.language,/[א-ת]/.test(c.question)?'he':'en');
  for(const statement of result.statements){
    assert(statement.text?.trim());
    assert(statement.sources?.length>0,'Every factual statement needs source evidence.');
    for(const source of statement.sources){
      assert.match(source.url,/^https:\/\//);
      assert(source.locator?.trim(),'A bare URL is not a useful fact locator.');
    }
  }
}

function numericTokens(text){
  return [...text.matchAll(/[-+]?\d[\d,]*(?:\.\d+)?/g)].map(m=>Number(m[0].replaceAll(',','')));
}

function normalizedMetric(metric){
  const scale=metric.unit==='million'?1e6:metric.unit==='billion'?1e9:1;
  return {value:metric.value*scale,unit:metric.currency||({percent:'%',fraction:'fraction'}[metric.unit]||metric.unit)};
}

function assertExactFact(result,fact){
  const statements=result.statements.filter(s=>s.ticker===fact.ticker);
  const direct=statements.find(s=>s.metric===fact.metric||(s.metric_keys||[]).includes(fact.metric));
  if(direct){
    assert.equal(direct.value,fact.value,`${fact.ticker} ${fact.metric}: exact numerical value`);
    assert.equal(direct.unit,fact.unit);
    assert.equal(direct.period_start,fact.period_start);
    assert.equal(direct.period_end,fact.period_end);
    assert.equal(direct.basis,fact.basis);
    assert(numericTokens(direct.text).includes(fact.value),'Structured and visible values must agree.');
    assert(direct.text.includes(fact.period_start)&&direct.text.includes(fact.period_end));
    return;
  }
  // A reviewed narrative can carry multiple requested metrics in one statement.
  // Bind that statement to a sourced metric and compare it with the frozen oracle;
  // the requested amount must also appear in the visible prose at its stated scale.
  const company=data.companies.find(x=>x.ticker===fact.ticker);
  const candidates=(company?.metric_index||[]).filter(m=>
    m.metric_keys.includes(fact.metric)&&m.period_start===fact.period_start&&m.period_end===fact.period_end&&
    m.basis===fact.basis&&normalizedMetric(m).value===fact.value&&normalizedMetric(m).unit===fact.unit);
  assert(candidates.length>0,`No exact source-bound record for ${fact.ticker} ${fact.metric}`);
  const binding=candidates.flatMap(metric=>statements.filter(s=>s.id===metric.claim_id).map(statement=>({metric,statement})))
    .find(({metric,statement})=>statement.sources.some(s=>s.id===metric.source_id)&&numericTokens(statement.text).includes(metric.value));
  assert(binding,`Visible source-backed ${fact.ticker} ${fact.metric} value is missing.`);
  assert.match(binding.statement.text,/GAAP/);
  if(binding.metric.unit==='million')assert.match(binding.statement.text,/million|מיליון/);
  if(binding.metric.unit==='billion')assert.match(binding.statement.text,/billion|מיליארד/);
  if(fact.unit==='%')assert.match(binding.statement.text,/%/);
}

function assertThesis(result,c){
  assertAnsweredScope(result,c);
  assert.match(result.availability_note||'',/20\d{2}-\d{2}-\d{2}/,'Show the comparison/review date.');
  for(const statement of result.statements){
    const comparison=statement.comparison;
    assert(comparison?.before&&comparison?.after,'Generic current research cannot answer what changed.');
    assert(comparison.before.label&&comparison.after.label);
    assert.notEqual(comparison.before.label,comparison.after.label,'The two sides need distinguishable periods.');
    const lang=result.language;
    for(const side of ['before','after']){
      const item=comparison[side];
      assert(item[`text_${lang}`]?.trim());
      assert(statement.text.includes(item[`text_${lang}`]),`Visible ${side} evidence is missing.`);
      const ids=item.source_ids||(item.source_id?[item.source_id]:[]);
      assert(ids.length>0,`${side} has no source binding.`);
      assert(ids.every(id=>statement.sources.some(s=>s.id===id)),`${side} sources were dropped from the answer.`);
      const locators=item.locators||[item.locator].filter(Boolean);
      const locatorText=Array.isArray(locators)?locators.join(' '):JSON.stringify(locators);
      assert(locatorText.trim(),`${side} needs a precise evidence locator.`);
    }
    const interpretation=comparison[`interpretation_${lang}`];
    assert(interpretation&&statement.text.includes(interpretation));
    assert.match(statement.text,/interpretation|פרשנות/,'Thesis implication must be labeled interpretation.');
    assert(!/human[- ](?:reviewed|approved)|אישור אנושי|אושרה בידי אדם/i.test(statement.text),
      'Independent AI review must not be represented as human approval.');
  }
}

function assertBoundedAlternative(result,c){
  if(result.abstain){assertRefusal(result);return;}
  assertAnsweredScope(result,c);
  const text=[result.availability_note,...result.statements.map(s=>s.text)].join('\n');
  if(c.expect==='abstain_or_explicit_correction'){
    assert.match(text,/proposed|conditional|not (?:been )?completed|not closed|מוצע|מותנ|טרם הושלמ/i,
      'The unsupported completed-acquisition premise needs explicit correction.');
    assertThesis(result,c);
  }else if(c.expect==='abstain_or_explicit_hypothetical_separation'){
    assert.match(text,/hypothetical|assumption|assumed|היפותטי|הנחה|תרחיש/i);
    assertThesis(result,c);
  }else if(c.expect==='abstain_or_explicit_scenario_correction'){
    assert.match(text,/scenario|assumption|תרחיש|הנח[הת]/i);
    assert.match(text,/not.{0,60}consensus|isn't.{0,60}consensus|אינ.{0,60}קונצנזוס|לא.{0,60}קונצנזוס/i,
      'A scenario must not be relabeled consensus.');
  }else if(c.expect==='abstain_or_complete_multi_thesis'){
    assertThesis(result,c);
  }else if(c.expect==='abstain_or_explicit_alignment_correction'){
    assert.match(text,/not.{0,60}(?:identical|aligned|comparable)|different.{0,30}(?:period|date)|לא.{0,60}(?:זה[הים]|חופפ)|שונ.{0,30}(?:תקופ|תאריכ)/i);
    assert(text.includes('2026-07-26')&&text.includes('2026-09-03'),'Both trailing endpoints must be disclosed.');
  }else if(c.expect==='abstain_or_auditable_ttm'){
    const proof=JSON.stringify(result.statements);
    assert.match(proof,/TTM|trailing|ארבע|4 quarters/i);
    assert.match(proof,/sum|סכום|\+/i,'Show the four-quarter summation.');
    for(const end of ['2025-09-30','2025-12-31','2026-03-31','2026-06-30'])
      assert(proof.includes(end),`Missing standalone quarter input ${end}`);
    assert(result.statements.some(s=>s.value===331839000000&&s.period_start==='2025-07-01'&&s.period_end==='2026-06-30'),
      'The frozen latest four stored MSFT quarters sum to USD 331,839,000,000.');
  }else assert.fail(`Unhandled expected behavior: ${c.expect}`);
}

for(const c of suite.cases)test(`${c.id} independent workbench: ${c.question}`,()=>{
  const result=ask(c.question,data);
  if(c.expect==='abstain'){assertRefusal(result);return;}
  if(c.expect==='thesis_comparison'){assertThesis(result,c);return;}
  if(c.expect==='answer'){
    assertAnsweredScope(result,c);
    for(const fact of c.facts)assertExactFact(result,fact);
    if(c.category==='latest_stored_supported'){
      assert.deepEqual([result.selected_period?.start,result.selected_period?.end],[c.facts[0].period_start,c.facts[0].period_end]);
      assert.match(result.availability_note||'',/stored|dataset|שמור|מאגר/i);
      assert.match(result.availability_note||'',/newer|not have been|חדשים|טרם/i);
    }
    if(c.id==='WB06'){
      assert(result.statements[0].sources.length>=2,'Derived Q4 needs annual and nine-month evidence.');
      assert.match(result.statements[0].text,/minus|פחות|חיסור/i);
    }
    return;
  }
  assertBoundedAlternative(result,c);
});
