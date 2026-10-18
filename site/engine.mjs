// Portable evidence lookup. Numerical eligibility is exported from Python source.
export const normalize = text => text.normalize('NFKC').toLowerCase().replace(/[\u0591-\u05c7]/g, '').replaceAll('’', "'");
const escape = value => value.replace(/[.*+?^()|[\]\\{}$]/g, '\\$&');
const match = (text, name) => new RegExp('(?<![\\p{L}\\p{N}_])' + (/[א-ת]/.test(name) ? '[ובלמשכ]?' : '') + escape(normalize(name)) + '(?![\\p{L}\\p{N}_])','u').test(text);
export function parseQuestion(question, data) {
  const q=normalize(question); let remainder=q; const metrics=[];
  for(const [key,[pattern]] of data.metric_patterns) if(new RegExp(pattern,'iu').test(remainder)){metrics.push(key);remainder=remainder.replace(new RegExp(pattern,'giu'),' ');}
  if(/\bearnings\b/.test(remainder) && !/date|release|next results/.test(q))metrics.push('net_income');
  const quarters=new Set([...q.matchAll(/\bq([1-4])\b/g)].map(m=>+m[1]));
  const words=['first|1st|ראשון','second|2nd|שני','third|3rd|שלישי','fourth|4th|רביעי'];
  words.forEach((word,i)=>{if(new RegExp('(?:'+word+')[- ]quarter|quarter\\s*'+(i+1)+'|רבעון\\s+(?:ה)?(?:'+word+')|רבעון\\s*'+(i+1),'u').test(q))quarters.add(i+1);});
  const years=[...new Set([...q.matchAll(/(?<!\d)(?:19|20)\d{2}(?!\d)/g)].map(m=>+m[0]))];
  const non=/non[ -]?gaap|adjusted|מתואמ/.test(q), gaap=/(?<!non-)(?<!non )\bgaap\b/.test(q);
  let error=null;
  if(/\broic\b|\broe\b|\broa\b|ebit margin|return on (?:capital|equity|assets)|תשואה על (?:ההון|נכסים)/.test(q))error='unsupported_metric';
  if(/excluding|except for|without|ללא|בניכוי|למעט/.test(q))error='unsupported_qualifier';
  if(metrics.length && /per employee|per customer|per user|לעובד|ללקוח|למשתמש|inflation.adjusted|constant.currency|במטבע קבוע|בנטרול|azure|copilot|data cent(?:er|re)|aws|cloud revenue|revenue.*cloud|הכנסות.*ענן|הכנסות.*אזור|הכנסות.*(?:סין|ארה״ב)/.test(q))error='unsupported_qualifier';
  return {metrics,quarters:[...quarters],years,fiscal:/\bfy\s*\d{4}|fiscal|שנת כספים|שנה פיסקלית/.test(q),annual:years.length>0 && quarters.size===0,bothBases:gaap&&non,basis:gaap&&non?null:non?'non-GAAP':gaap?'GAAP':null,guidance:/guidance|outlook|forecast|תחזית|צפי/.test(q),comparison:/\bcompare|versus|\bvs\b|השוו|השוה|השוואה|לעומת/.test(q),error};
}
export function ask(question,data) {
  const he=/[א-ת]/.test(question),q=normalize(question),spec=parseQuestion(question,data);
  const fail=code=>({abstain:true,reason_code:code,reason:he?(data.he_reasons[code]||data.he_reasons.no_evidence):({unsupported_metric:'The requested metric or accounting basis is not available.',unsupported_period:'The requested financial period is not fully supported.',unsupported_qualifier:'The requested adjustment or breakdown is not supported.',incomplete_comparison:'Evidence is missing for part of this comparison.'}[code]||'No fully supported answer is available for this question.'),statements:[],companies:[]});
  if(!question.trim()||question.length>4000)return fail('invalid_question');
  const entities=Object.entries(data.config.issuer_aliases).filter(([ticker,names])=>[ticker,...names].some(n=>match(q,n))).map(([ticker])=>ticker);
  const unknown=[...question.matchAll(/\$([A-Za-z][A-Za-z0-9.-]*)\b/g)].some(m=>!Object.keys(data.config.issuer_aliases).includes(m[1].toUpperCase()));
  const basisComparison=/gaap|adjusted|non.?gaap|מתואם|מתואמ/.test(q);
  if(unknown || (spec.comparison&&entities.length<2&&!basisComparison))return fail('unknown_issuer');
  const acronyms=new Set([...Object.keys(data.config.issuer_aliases),...data.config.non_ticker_acronyms,'ROIC','ROE','ROA','FCF','OCF','SBC']);
  if((spec.comparison||!entities.length)&&[...question.matchAll(/\b[A-Z]{2,5}\b/g)].some(m=>!acronyms.has(m[0])))return fail('unknown_issuer');
  for(const rule of data.config.unsupported)if(new RegExp(rule.pattern,'i').test(q))return fail(rule.code);
  if(!entities.length)return fail('missing_scope');
  if(entities.length>2)return fail('too_many_issuers');
  const relation=/relationship|collaboration|partnership|supplier|customer|הקשר|קשר בין|שותפ|ספק של/.test(q);
  const companies=data.companies.filter(c=>entities.includes(c.ticker));
  if(companies.length!==entities.length && !relation)return fail('unreviewed_issuer');
  let hints=Object.entries(data.config.sections).filter(([,r])=>r.patterns.some(p=>new RegExp(p,'i').test(q))).map(([section])=>section);
  const descriptive=hints.some(h=>['business-overview','revenue-model-and-segments','products-and-services','growth-drivers','catalysts'].includes(h))&&!/how much|how many|what was|what were|כמה|מה היו|שיעור|\b(?:FY|Q[1-4])/i.test(question);
  const financial=Boolean(spec.metrics.length||spec.error||hints.some(h=>['financial-performance','balance-sheet-and-capital-allocation'].includes(h)));
  if(financial&&!descriptive&&spec.error)return fail(spec.error);
  const precise=financial&&!descriptive&&(spec.metrics.length||spec.years.length||spec.quarters.length||spec.basis);
  if(precise&&(spec.years.length>1||spec.quarters.length>1))return fail('unsupported_period');
  const statements=[];
  for(const company of companies){
    let allowed=null, sections=hints;
    if(precise){
      allowed=new Set();sections=[];
      for(const key of spec.metrics.length?spec.metrics:[null]){
        const eligible=company.metric_index.filter(m=>{
          const i=m.identity;
          return (!key||m.metric_keys.includes(key))&&(!spec.quarters.length||(i.type==='quarterly'&&spec.quarters.includes(i.quarter)))&&(!spec.years.length||spec.years.includes(i.year))&&(!spec.annual||i.type==='annual')&&(!spec.years.length||spec.fiscal||i.year===Number(m.period_end?.slice(0,4)))&&(!spec.basis||m.basis===spec.basis)&&((m.claim_kind==='management_guidance')===spec.guidance);
        });
        if(spec.bothBases&&spec.metrics.length===1&&(!eligible.some(m=>m.basis==='GAAP')||!eligible.some(m=>m.basis==='non-GAAP')))return fail('unsupported_metric');
        if(!eligible.length)return fail(spec.years.length||spec.quarters.length?'unsupported_period':'unsupported_metric');
        eligible.forEach(m=>{allowed.add(m.claim_id);if(!sections.includes(m.section_id))sections.push(m.section_id);});
      }
    }
    if(!sections.length)return fail('no_evidence');
    if(/\b(?:today|current|latest|right now)\b|היום|כרגע|עדכני|האחרון|האחרונה/i.test(question)){
      const fresh=company.freshness,age=fresh.checked_at?(Date.now()-Date.parse(fresh.checked_at))/3600000:Infinity;
      if(fresh.status!=='checked'||age>48)return fail('freshness_unverified');
    }
    for(const section of sections){
      for(const c of company.sections[section]||[]){
        if(allowed&&!allowed.has(c.id))continue;
        if(section==='relationships-and-themes'&&entities.length>1){
          const others=entities.filter(t=>t!==company.ticker).flatMap(t=>[t,...(data.config.issuer_aliases[t]||[])]);
          if(!others.some(n=>match(normalize(c.text),n)))continue;
        }
        if(he&&!c.text_he)return fail('translation_missing');
        statements.push({...c,ticker:company.ticker,section,text:he?c.text_he:c.text,sources:c.evidence.map(e=>({...company.sources.find(s=>s.id===e.source_id),locator:e.locator}))});
      }
    }
    if(allowed&&[...allowed].some(id=>!statements.some(s=>s.ticker===company.ticker&&s.id===id)))return fail('incomplete_answer');
  }
  if(!statements.length)return fail('no_evidence');
  if(spec.comparison&&entities.some(t=>!statements.some(s=>s.ticker===t)))return fail('incomplete_comparison');
  return {abstain:false,statements,companies,language:he?'he':'en'};
}
export function scenario(eps,growth,pe,years,price){
  if(![eps,growth,pe,years,price].every(Number.isFinite)||eps<=0||growth<=-1||growth>3||pe<=0||pe>200||years<1||years>10||price<=0)throw Error('Invalid scenario inputs');
  const terminalEPS=eps*(1+growth)**years,terminalPrice=terminalEPS*pe;
  return {terminalEPS,terminalPrice,change:terminalPrice/price-1,annualized:(terminalPrice/price)**(1/years)-1};
}
