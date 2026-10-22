import {ask,scenario} from './engine.mjs';

const $=id=>document.getElementById(id);
const NAV=[['overview','◫','תמונת המחקר'],['financials','▥','היסטוריה פיננסית'],['compare','⇄','השוואת חברות'],['scenarios','↗','תרחישי שווי'],['updates','◷','דיווחים ומעקב']];
const SECTIONS={'business-overview':'איך העסק עובד','revenue-model-and-segments':'מגזרים ומקורות הכנסה','products-and-services':'מוצרים ושירותים','customers-and-end-markets':'לקוחות ושווקים','industry-and-value-chain':'הענף ושרשרת הערך','competitive-landscape':'התחרות','moat-and-differentiation':'חפיר ובידול','growth-drivers':'מנועי צמיחה','financial-performance':'ביצועים פיננסיים','balance-sheet-and-capital-allocation':'מאזן והקצאת הון','management-and-governance':'הנהלה וממשל תאגידי','valuation-context':'הערכת שווי','catalysts':'זרזים ואבני דרך','risks-and-thesis-breakers':'סיכונים ושבירת התזה','scenarios-and-open-questions':'תרחישים ושאלות פתוחות','relationships-and-themes':'קשרים בין חברות','recent-developments':'התפתחויות אחרונות','sources-and-change-log':'מקורות והיסטוריית שינוי'};
const METRICS={revenue:'הכנסות',gross_profit:'רווח גולמי',cost_of_revenue:'עלות הכנסות',operating_income:'רווח תפעולי',net_income:'רווח נקי מיוחס לחברה אם',net_income_common:'רווח מיוחס למניות רגילות',net_income_including_noncontrolling_interests:'רווח כולל זכויות שאינן מקנות שליטה',eps_diluted:'רווח מדולל למניה',eps_basic:'רווח בסיסי למניה',operating_cash_flow:'תזרים מפעילות שוטפת',capex:'רכישת רכוש קבוע',free_cash_flow:'תזרים חופשי מחושב',purchases_of_productive_assets:'רכישת נכסים יצרניים, הגדרה רחבה',stock_based_compensation:'תגמול מבוסס מניות',cash_and_equivalents:'מזומנים ושווי מזומנים',short_term_investments:'השקעות קצרות טווח',debt_current:'חוב שוטף',debt_noncurrent:'חוב שאינו שוטף',long_term_debt_total:'סך חוב ארוך טווח',short_term_borrowings:'הלוואות קצרות טווח',debt_total:'חוב כולל מחושב',shares_basic:'ממוצע מניות, בסיסי',shares_diluted:'ממוצע מניות, מדולל',shares_outstanding:'מניות קיימות למועד המאזן'};
const KIND={reported:'נתון מדווח',derived:'חישוב',reported_fact:'נתון מדווח',management_guidance:'תחזית הנהלה',interpretation:'פרשנות',research_question:'שאלה למחקר'};
const state={tab:'overview',ticker:'MSFT',period:'annual',metric:'revenue',section:'business-overview',compare:new Set(['MSFT','NVDA']),queueTicker:'all',priority:'all'};
let data=null,loadToken=0,answerToken=0;
function h(tag,attrs={},...children){
  const node=document.createElement(tag);
  for(const [key,value] of Object.entries(attrs)){
    if(value===null||value===undefined)continue;
    if(key==='class')node.className=value;
    else if(key.startsWith('on'))node.addEventListener(key.slice(2).toLowerCase(),value);
    else if(key==='value'||key==='checked'||key==='disabled'||key==='hidden')node[key]=value;
    else node.setAttribute(key,String(value));
  }
  for(const child of children.flat(Infinity))if(child!==null&&child!==undefined)node.append(child instanceof Node?child:document.createTextNode(String(child)));
  return node;
}
function safeURL(url){try{const u=new URL(url);return u.protocol==='https:'?u.href:'#';}catch{return '#';}}
function link(text,url){return h('a',{href:safeURL(url),target:'_blank',rel:'noopener noreferrer'},text);}
function date(value){if(!value)return 'לא זמין';const d=new Date(value);return Number.isNaN(+d)?value:new Intl.DateTimeFormat('he-IL',{day:'2-digit',month:'2-digit',year:'numeric',timeZone:'Asia/Jerusalem'}).format(d);}
function num(v,digits=2){return typeof v==='number'&&Number.isFinite(v)?v.toLocaleString('en-US',{maximumFractionDigits:digits}):'—';}
function compact(v){return typeof v==='number'&&Number.isFinite(v)?new Intl.NumberFormat('en-US',{notation:'compact',maximumFractionDigits:2}).format(v):'—';}
function pct(v){return typeof v==='number'&&Number.isFinite(v)?num(100*v,1)+'%':'—';}
function unit(cell){return cell?.unit==='USD/shares'?'דולר למניה':cell?.unit==='shares'?'מיליוני מניות':'מיליוני דולר';}
function cellValue(cell){if(typeof cell?.value!=='number')return '—';return num(cell.unit==='USD/shares'?cell.value:cell.value/1e6,cell.unit==='USD/shares'?2:1);}
function company(){return data.companies.find(c=>c.ticker===state.ticker)||data.companies[0];}
function periods(c,type=state.period){return (c.history?.periods||[]).filter(p=>p.type===type).sort((a,b)=>b.end.localeCompare(a.end));}
function cell(c,p,key){return c.history?.financials?.[p?.id]?.[key];}
function latest(c,key){const p=periods(c,'annual')[0];return {period:p,cell:cell(c,p,key)};}
function note(text,kind=''){return h('div',{class:'notice '+kind},text);}
function option(value,label,selected){return h('option',{value,selected:selected?'':null},label);}
function button(text,handler,className='text-button'){return h('button',{type:'button',class:className,onClick:handler},text);}
function card(title,body,extra=null){return h('section',{class:'card'},h('div',{class:'card-head'},h('h2',{},title),extra),body);}
function sourceRefs(claim,c){
  const sources=claim.sources||claim.evidence.map(e=>({...c.sources.find(s=>s.id===e.source_id),locator:e.locator}));
  return sources.map((s,i)=>h('span',{},i?' · ':'',link(s.id+' ↗',s.url),h('span',{class:'sr-only'},s.title+' '+s.locator)));
}
function claimView(claim,c,answer=false){
  return h('article',{class:'claim'},answer?h('span',{class:'result-company',dir:'ltr'},c.ticker+' / '+(SECTIONS[claim.section]||'')):null,
    h('p',{dir:'auto'},claim.text_he||claim.text),
    h('div',{class:'claim-meta'},h('span',{class:'kind '+claim.kind},KIND[claim.kind]||claim.kind),
      sourceRefs(claim,c),h('span',{},(claim.source_kind==='financial_history'?'נתונים היסטוריים ל־':'מחקר ל־')+date(claim.as_of||c.as_of))));
}
function companySummary(c){return h('div',{class:'company-summary'},h('div',{class:'company-avatar','aria-hidden':'true'},c.ticker.slice(0,1)),h('div',{},h('h2',{dir:'ltr'},c.name),h('p',{},c.ticker+' · '+({'information-technology':'טכנולוגיה','industrials':'תעשייה וביטחון'}[c.sector]||c.sector)+' · מחקר ל־'+date(c.as_of))),h('span',{class:'badge'},(c.freshness.pending_count||0)+' דיווחים ממתינים לסקירה'));}
function stat(label,value,description){return h('div',{class:'stat'},h('div',{class:'stat-label'},label),h('div',{class:'stat-value'},value),h('div',{class:'stat-note'},description));}
function chart(c,key,type='annual'){
  const rows=periods(c,type).slice().reverse().map(p=>({period:p,cell:cell(c,p,key)}));
  if(!rows.some(r=>typeof r.cell?.value==='number'))return h('div',{class:'chart-empty'},'אין נתונים לפי ההגדרה המדויקת של המדד.');
  const node=document.createElementNS('http://www.w3.org/2000/svg','svg');
  node.setAttribute('viewBox','0 0 690 235');node.setAttribute('class','chart');node.setAttribute('role','img');node.setAttribute('aria-label',METRICS[key]+' לפי תקופה. הנתונים זמינים גם בטבלה.');
  const add=(tag,attrs,text)=>{const n=document.createElementNS(node.namespaceURI,tag);for(const [k,v] of Object.entries(attrs))n.setAttribute(k,v);if(text!==undefined)n.textContent=text;node.append(n);return n;};
  const values=rows.filter(r=>typeof r.cell?.value==='number').map(r=>r.cell.value),lo=Math.min(0,...values),hi=Math.max(0,...values),range=hi-lo||1,top=22,bottom=194,height=bottom-top;
  const y=v=>bottom-(v-lo)/range*height;
  for(let i=0;i<=3;i++){const v=lo+(hi-lo)*i/3;add('line',{x1:52,x2:680,y1:y(v),y2:y(v),class:'chart-grid'});add('text',{x:42,y:y(v)+4,'text-anchor':'end',class:'chart-label'},compact(v));}
  const step=620/rows.length,bw=Math.min(step*.58,64);
  rows.forEach((r,i)=>{const x=54+i*step+step/2,v=r.cell?.value;
    if(typeof v==='number'){const bar=add('rect',{x:x-bw/2,y:Math.min(y(v),y(0)),width:bw,height:Math.max(1,Math.abs(y(v)-y(0))),rx:3,class:'chart-bar '+(i===rows.length-1?'latest ':'')+(!r.cell.model_usable?'flagged':'')});
      const t=document.createElementNS(node.namespaceURI,'title');t.textContent=r.period.label+' · '+r.period.start+' – '+r.period.end+' · '+num(v)+' '+r.cell.unit;bar.append(t);add('text',{x,y:v>=0?y(v)-7:y(v)+13,'text-anchor':'middle',class:'chart-value'},compact(v));
    }else add('text',{x,y:y(0)-8,'text-anchor':'middle',class:'chart-label'},'—');
    add('text',{x,y:216,'text-anchor':'middle',class:'chart-label'},r.period.label.replace('FY',''));
  });
  return node;
}
function overview(c){
  const revenue=latest(c,'revenue'),profit=latest(c,'net_income'),fcf=latest(c,'free_cash_flow'),q=c.quote;
  const stale=q&&(Date.now()-Date.parse(q.trade_at)>4*86400000||q.status!=='available');
  const stats=h('div',{class:'stats'},
    stat('הכנסות שנתיות',compact(revenue.cell?.value)+' $',(revenue.period?.label||'')+' · עד '+date(revenue.period?.end)),
    stat('רווח נקי, חברה אם',typeof profit.cell?.value==='number'?compact(profit.cell.value)+' $':'לא זמין',(profit.period?.label||'')+' · US GAAP'),
    stat('תזרים חופשי מחושב',typeof fcf.cell?.value==='number'?compact(fcf.cell.value)+' $':'לא זמין','תזרים שוטף פחות רכישת רכוש קבוע'),
    stat('מחיר בעסקה האחרונה',q?num(q.price)+' $':'לא זמין',(q?date(q.trade_at)+' · Yahoo Finance':'אין מקור מחיר')+(stale?' · נתון ישן':'')));
  const researchSelect=h('select',{'aria-label':'פרק מחקר',onChange:e=>{state.section=e.target.value;renderContent();}},...Object.entries(SECTIONS).filter(([key])=>c.sections[key]?.length).map(([key,label])=>option(key,label,key===state.section)));
  const main=card('המחקר של '+c.ticker,h('div',{},h('div',{class:'section-tools'},researchSelect),...(c.sections[state.section]||[]).map(x=>claimView(x,c)),h('p',{class:'caption'},'התוכן נבדק בידי AI ומוצג לפי תאריך המחקר. הנתונים ההיסטוריים עשויים לכלול דיווחים מאוחרים יותר.')));
  const risk=card('מה יכול לשבור את התזה?',h('div',{},...(c.sections['risks-and-thesis-breakers']||[]).map(x=>claimView(x,c))));
  const growth=card('מנועי צמיחה',h('div',{},...(c.sections['growth-drivers']||[]).map(x=>claimView(x,c))));
  const history=card('הכנסות לאורך זמן',h('div',{},h('p',{class:'caption'},'דולר · שנים פיסקליות · SEC Company Facts'),chart(c,'revenue'),h('p',{class:'caption'},'הגדרת המדד והמקורות המדויקים מופיעים בהיסטוריה הפיננסית.')),button('הנתונים המלאים ←',()=>navigate('financials')));
  const calculated=(c.historical_index||[]).filter(r=>r.id.startsWith('D:')&&r.period_label===revenue.period?.label);
  const performance=card('צמיחה ורווחיות',calculated.length?h('div',{},h('p',{class:'caption'},revenue.period.label+' · חישובים מנתוני SEC תואמים'),...calculated.map(r=>h('details',{class:'cell-detail'},h('summary',{},({'revenue_growth':'צמיחה שנתית בהכנסות','gross_margin':'שיעור רווח גולמי','operating_margin':'שיעור רווח תפעולי','net_margin':'שיעור רווח נקי'}[r.metric]||r.metric)+' · '+num(r.value,2)+'%'),claimView({...r,source_kind:"financial_history"},c)))):note('אין מספיק נתונים תואמים לחישוב בתקופה האחרונה.'));
  const gaps=card('מה עדיין צריך לבדוק',h('ul',{class:'gap-list'},...c.gaps.map(g=>h('li',{},g.he||g.en))));
  return [companySummary(c),stats,h('div',{class:'grid-2'},h('div',{},main,performance,history),h('div',{},growth,risk,gaps))];
}
function cellView(c,p,key){
  const m=cell(c,p,key);if(!m||m.value===null)return h('span',{class:'missing',title:m?.flags?.join(', ')||'הנתון חסר במקור'},'—');
  const warnings=m.flags||[],conflicts=m.conflicts||[];
  const detail=h('details',{class:'cell-detail'},h('summary',{},m.model_usable?'מקור ופרטים':'⚑ בדיקת התאמה נדרשת'),h('p',{},m.basis+' · '+(m.status==='derived'?'חישוב':'דיווח')+' · '+num(m.value)+' '+m.unit),
    m.formula?h('p',{dir:'ltr'},String(typeof m.formula==='string'?m.formula:JSON.stringify(m.formula))):null,
    ...Array.from(new Map((m.provenance||[]).map(s=>[s.url,s])).values()).map(s=>h('p',{},link((s.form||'SEC')+' · '+date(s.filed),s.url),h('span',{class:'period-date'},s.tag))),
    m.share_basis?h('p',{},'בסיס מניות מאומת לאחר פיצול מ־'+date(m.share_basis.effective_date)+' · '+m.share_basis.new_shares_per_old_share+' מניות לכל מניה קודמת',...m.share_basis.evidence_source_ids.map(id=>{const source=c.history.source_index[id];return h('span',{},' · ',link('אסמכתת הפיצול ↗',source.url));})):null,
    warnings.length?h('ul',{},...warnings.map(f=>h('li',{dir:'ltr'},f))):null,
    conflicts.length?h('p',{},conflicts.length+' ערכים/גרסאות חלופיים נשמרו. ',link('לנתונים המלאים',data.repository+'/blob/main/research/financials/'+c.ticker+'.json')):null);
  return h('div',{},h('span',{class:'metric-value'},cellValue(m)),detail);
}
function financials(c){
  const ps=periods(c);
  const controls=h('div',{class:'section-tools'},h('div',{class:'segmented'},...['annual','quarterly'].map(type=>button(type==='annual'?'שנתי':'רבעוני',()=>{state.period=type;renderContent();},state.period===type?'active':''))),h('label',{for:'chart-metric'},'מדד בגרף'),h('select',{id:'chart-metric',onChange:e=>{state.metric=e.target.value;renderContent();}},...Object.entries(METRICS).map(([key,label])=>option(key,label,key===state.metric))));
  const table=h('table',{},h('thead',{},h('tr',{},h('th',{scope:'col'},'מדד / תקופה'),...ps.map(p=>h('th',{scope:'col'},p.label,h('span',{class:'period-date'},p.start+' – '+p.end))))),h('tbody',{},...Object.entries(METRICS).map(([key,label])=>h('tr',{},h('td',{},label,h('span',{class:'metric-unit'},unit(cell(c,ps[0],key)))),...ps.map(p=>h('td',{},cellView(c,p,key)))))));
  return [companySummary(c),note('נתוני SEC מנורמלים לפי תקופות והגדרות מדויקות. יתרות מאזניות הן ליום סיום התקופה. מקף מציין חוסר בנתון. לחיצה על „מקור ופרטים” פותחת את הדיווח. סימון ⚑ מצביע על סתירה, שינוי בהגדרה או בסיס מניות שטרם אומת.','amber'),
    card('היסטוריה פיננסית',h('div',{},controls,chart(c,state.metric,state.period),h('p',{class:'caption'},'נתונים נשלפו ב־'+date(c.history?.source?.retrieved_at)+' · '+METRICS[state.metric]+'. התאמה לפיצולים מוצגת בפרטי כל נתון רק כאשר אומתה; נתונים אחרים נשארים מסומנים לבדיקה.'),
      h('div',{class:'table-wrap',tabindex:'0','aria-label':'טבלת נתונים פיננסיים, ניתן לגלול לרוחב'},table))),
    note('תזרים חופשי מחושב רק כאשר קיימים תזרים שוטף ורכישת רכוש קבוע לפי אותה תקופה. „רכישת נכסים יצרניים” נשמרת בנפרד. תקופה רבעונית שנגזרה ממצטבר מסומנת כחישוב.'),
    h('p',{class:'caption'},link('קובץ הנתונים, ההגדרות וכל החריגים ↗',data.repository+'/blob/main/research/financials/'+c.ticker+'.json'))];
}
function compare(){
  const selected=data.companies.filter(c=>state.compare.has(c.ticker));
  const checkboxes=h('div',{class:'section-tools'},...data.companies.map(c=>h('label',{class:'check-company'},h('input',{type:'checkbox',checked:state.compare.has(c.ticker),onChange:e=>{if(e.target.checked)state.compare.add(c.ticker);else state.compare.delete(c.ticker);renderContent();}}),c.ticker)));
  const keys=['revenue','gross_profit','operating_income','net_income','operating_cash_flow','free_cash_flow','stock_based_compensation','cash_and_equivalents','debt_total'];
  const heads=selected.map(c=>{const p=periods(c,'annual')[0];return h('th',{scope:'col'},c.ticker,h('span',{class:'period-date'},p?.label+' · '+p?.end));});
  const rows=keys.map(key=>h('tr',{},h('td',{},METRICS[key],h('span',{class:'metric-unit'},'מיליוני דולר')),...selected.map(c=>h('td',{},cellView(c,periods(c,'annual')[0],key)))));
  for(const [key,label] of [['gross_margin','שיעור רווח גולמי'],['operating_margin','שיעור רווח תפעולי'],['net_margin','שיעור רווח נקי'],['fcf_margin','תזרים חופשי / הכנסות'],['sbc_to_revenue','תגמול מנייתי / הכנסות']]){
    const cells=selected.map(c=>{
      const p=periods(c,'annual')[0],ratio=c.ratios.find(r=>r.period.id===p?.id)?.ratios[key];
      const detail=ratio?h('details',{class:'cell-detail'},h('summary',{},'נוסחה ומקורות'),h('p',{dir:'ltr'},ratio.formula),...ratio.source_urls.map(url=>h('p',{},link('דיווח SEC ↗',url)))):null;
      return h('td',{},h('span',{class:'metric-value'},pct(ratio?.value)),detail);
    });
    rows.push(h('tr',{},h('td',{},label,h('span',{class:'metric-unit'},'חישוב מנתונים תואמים')),...cells));
  }
  const table=h('table',{},h('thead',{},h('tr',{},h('th',{scope:'col'},'מדד'),...heads)),h('tbody',{},...rows));
  return [card('השוואה לפי השנה המדווחת האחרונה',h('div',{},checkboxes,note('שנות הכספים של החברות מסתיימות במועדים שונים. תאריכי הסיום מוצגים בכל עמודה; הטבלה אינה מניחה שתקופות אלה זהות. גם הגדרות רווח וחוב עשויות להגביל השוואה.','amber'),selected.length?h('div',{class:'table-wrap',tabindex:'0','aria-label':'השוואת חברות'},table):note('בחר לפחות חברה אחת.')))];
}
function scenarios(c){
  const eps=latest(c,'eps_diluted'),q=c.quote;
  const fields=h('div',{class:'scenario-form'},
    h('label',{class:'field'},'EPS בסיס שהנחת ($ למניה)',h('input',{id:'scenario-eps',type:'number',min:'.0001',step:'any',required:true,placeholder:'הזן בסיס חיובי'})),
    h('label',{class:'field'},'מחיר ייחוס ($ למניה)',h('input',{id:'scenario-price',type:'number',min:'.0001',step:'any',required:true,value:q?.price||''})),
    h('label',{class:'field'},'אופק התרחיש (שנים)',h('input',{id:'scenario-years',type:'number',min:1,max:10,step:1,required:true,value:3})));
  const rows=[['שלילי',-10,15],['אמצע',5,25],['חיובי',15,35]];
  const form=h('form',{id:'scenario-form',onSubmit:e=>{e.preventDefault();calculateScenario(rows);}},fields,h('div',{class:'table-wrap'},h('table',{class:'assumptions'},h('thead',{},h('tr',{},h('th',{},'תרחיש'),h('th',{},'צמיחת EPS שנתית (%)'),h('th',{},'מכפיל רווח בסוף התקופה'))),h('tbody',{},...rows.map(([name,growth,pe],i)=>h('tr',{},h('td',{},name),h('td',{},h('input',{id:'growth-'+i,type:'number',min:-99.99,max:300,step:'any',required:true,value:growth,'aria-label':'צמיחת EPS בתרחיש '+name})),h('td',{},h('input',{id:'pe-'+i,type:'number',min:'.01',max:200,step:'any',required:true,value:pe,'aria-label':'מכפיל בתרחיש '+name}))))))),h('p',{class:'caption'},'ערכי הצמיחה והמכפילים ההתחלתיים הם דוגמה כללית לכל החברות. שנה אותם לפי ההנחות שלך.'),h('button',{type:'submit',class:'primary'},'חשב את התרחישים ←'));
  const baseInfo=h('div',{},note('זהו מחשבון רגישות לפי הנחותיך. הוא אינו תחזית של החברה, קונצנזוס אנליסטים או מחיר יעד. EPS מדווח אינו בהכרח בסיס מתאים לרווח מנורמל.','amber'),
    h('p',{class:'caption'},'EPS מדולל היסטורי: '+(typeof eps.cell?.value==='number'?num(eps.cell.value)+' $':'לא זמין')+' · '+(eps.period?.label||'')+' · עד '+date(eps.period?.end)+(eps.cell?.share_basis?' · בסיס מניות מאומת לאחר הפיצול מ־'+date(eps.cell.share_basis.effective_date)+'. ':'. בסיס המניות והפיצולים עדיין דורש בדיקה. '),
      eps.cell?.provenance?.[0]?link('מקור ↗',eps.cell.provenance[0].url):null),
    h('p',{class:'caption'},'מחיר הייחוס שנשלף: '+(q?num(q.price)+' $ · עסקה מ־'+date(q.trade_at)+' · Yahoo Finance':'אין מחיר זמין')+'. ניתן לשנותו.'));
  return [companySummary(c),card('מה קורה לשווי כשההנחות משתנות?',h('div',{},baseInfo,form,h('div',{id:'scenario-result','aria-live':'polite'}),h('p',{class:'caption',dir:'ltr'},'EPS × (1 + growth)^years × exit P/E'),h('p',{class:'caption'},'השינוי המוצג הוא במחיר בלבד, ללא דיבידנדים, מס, עמלות או מט״ח. המכפיל דורש EPS חיובי; אין תמיכה בתרחיש הפסד או בשינוי עתידי במספר המניות.')))];
}
function calculateScenario(rows){
  const out=$('scenario-result');
  try{
    const eps=Number($('scenario-eps').value),price=Number($('scenario-price').value),years=Number($('scenario-years').value);
    const cards=rows.map(([name],i)=>{const result=scenario(eps,Number($('growth-'+i).value)/100,Number($('pe-'+i).value),years,price);return h('article',{class:'scenario-card'},h('h3',{},'תרחיש '+name+' · '+years+' שנים'),h('div',{class:'scenario-price'},num(result.terminalPrice)+' $'),h('p',{},'שינוי במחיר: ',h('bdi',{class:result.change<0?'negative':''},pct(result.change))),h('p',{},'שינוי שנתי מחושב: ',h('bdi',{},pct(result.annualized))),h('p',{},'EPS סופי: ',h('bdi',{},num(result.terminalEPS)+' $')));});
    out.replaceChildren(h('div',{class:'scenario-output'},cards));
  }catch{out.replaceChildren(note('יש להזין EPS ומחיר חיוביים, צמיחה מעל ‎-100%, מכפיל עד 200 ואופק של שנה עד עשר שנים.','red'));}
}
function updates(){
  const summary=data.triage?.summary,entries=data.triage?.entries||[];
  const errors=Object.entries(data.source_health||{}).flatMap(([ticker,health])=>(health.errors||[]).map(e=>h('p',{class:'caption'},ticker+' · '+e.error+' ',e.source?.startsWith('https://')?link('מקור',e.source):null)));
  const refreshErrors=(data.refresh_status?.financials||[]).concat(data.refresh_status?.market||[]).filter(r=>r.status==='error').map(e=>h('p',{class:'caption'},e.ticker+' · '+e.error));
  const coverage=h('div',{class:'coverage'},...data.companies.map(c=>h('div',{class:'coverage-item '+(c.freshness.coverage_status!=='checked'?'error':'')},h('strong',{},c.ticker),h('span',{},c.freshness.coverage_status==='checked'?'סריקת מקורות הצליחה':'כיסוי מקורות חלקי'),h('span',{},(c.freshness.pending_count||0)+' ממתינים לסקירה'))));
  const controls=h('div',{class:'section-tools'},h('label',{for:'queue-company'},'חברה'),h('select',{id:'queue-company',onChange:e=>{state.queueTicker=e.target.value;renderContent();}},option('all','כל החברות',state.queueTicker==='all'),...data.companies.map(c=>option(c.ticker,c.ticker,state.queueTicker===c.ticker))),h('label',{for:'queue-priority'},'עדיפות'),h('select',{id:'queue-priority',onChange:e=>{state.priority=e.target.value;renderContent();}},option('all','כל העדיפויות',state.priority==='all'),...['P0','P1','P2','P3'].map(p=>option(p,p,state.priority===p))));
  const filtered=entries.filter(e=>(state.queueTicker==='all'||e.ticker===state.queueTicker)&&(state.priority==='all'||e.priority===state.priority));
  return [h('div',{class:'stats'},stat('דיווחים הממתינים לסקירה',summary?.pending??'—','הכותרות עדיין אינן מסקנות מחקר'),stat('עדיפות גבוהה · P0',summary?.by_priority?.P0??'—','תוצאות ודיווחים כספיים'),stat('תור להמשך בדיקה · P1',summary?.by_priority?.P1??'—','דיווחים, עסקאות ומינויים'),stat('סריקת המקורות',date(data.scan_at),'תאריך סריקה, לא תאריך אישור מחקר')),
    card('כיסוי המקורות',h('div',{},coverage,h('p',{class:'caption'},'מקורות עם בדיקה חלקית או שגיאה: '+(data.companies.filter(c=>c.freshness.coverage_status!=='checked').map(c=>c.ticker).join(', ')||'אין')+'. הצלחה בסריקה אינה מעידה שכל הדיווחים עברו סקירת תוכן.'),errors,refreshErrors)),
    card('תור הדיווחים',h('div',{},h('p',{class:'caption'},link('סקירת הדיווחים הקריטיים והעדכונים המוצעים ↗',data.repository+'/blob/main/docs/P0_REVIEW.md')),note('העדיפות נקבעת לפי מטא־נתונים לצורך סדר העבודה. סגירת דיווח דורשת קריאת מקור והשוואה למחקר הקיים; הסריקה אינה מאשרת אוטומטית את המחקר.'),controls,
      filtered.length?h('div',{},...filtered.map(e=>h('article',{class:'queue-item'},h('span',{class:'priority '+e.priority},e.priority),h('div',{},h('h3',{},e.title),h('div',{class:'caption'},e.ticker+' · '+date(e.published_at)+' · '+(e.classification==='already_in_reviewed_evidence'?'מקושר למחקר שנבדק':e.classification==='needs_review'?'ממתין לסקירה':'החלטת סקירה מתועדת'))),link('מקור ↗',e.url)))):note('אין דיווחים במסנן הנוכחי.')))];
}
function navigate(tab){state.tab=tab;renderNavigation();renderContent();}
function renderNavigation(){
  $('page-title').textContent=NAV.find(n=>n[0]===state.tab)[2];
  $('navigation').replaceChildren(...NAV.map(([id,icon,label])=>h('button',{type:'button',class:'nav-button '+(state.tab===id?'active':''),'aria-current':state.tab===id?'page':null,onClick:()=>navigate(id)},h('span',{class:'nav-icon','aria-hidden':'true'},icon),label)));
}
function renderCompanies(){
  $('selected-label').textContent=company().name;
  $('companies').replaceChildren(...data.companies.map(c=>h('button',{type:'button',class:'company-button '+(c.ticker===state.ticker?'active':''),'aria-pressed':c.ticker===state.ticker,onClick:()=>{state.ticker=c.ticker;renderCompanies();renderContent();}},h('strong',{dir:'ltr'},c.ticker),h('small',{},h('span',{class:'pending-dot','aria-hidden':'true'}),c.freshness.pending_count+' לבדיקה'))));
}
function renderContent(){
  const c=company();
  const pages={overview:()=>overview(c),financials:()=>financials(c),compare,scenarios:()=>scenarios(c),updates};
  const warning=data.refresh_status?.status==='partial'?note('עדכון הנתונים האחרון היה חלקי. שגיאות המקור מוצגות במעקב; נתונים קודמים נשמרו עם תאריכיהם.','amber'):null;
  $('content').replaceChildren(...(warning?[warning]:[]),...pages[state.tab]());
}
async function runQuestion(question){
  if(!data)return;
  const token=++answerToken,out=$('answer');out.hidden=false;
  out.replaceChildren(note('מחפש תשובה עם מקורות…'));
  let result,origin='תשובה מהשרת';
  try{
    const response=await fetch('./api/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question}),signal:AbortSignal.timeout(10000)});
    if(!response.ok)throw Error('Answer API unavailable');
    result=await response.json();
    if(typeof result.abstain!=='boolean'||!Array.isArray(result.statements))throw Error('Invalid answer');
  }catch{
    result=ask(question,data);
    origin='השרת לא זמין למענה; תשובה מהעותק שנטען בדפדפן';
  }
  if(token!==answerToken)return;
  const header=h('div',{class:'answer-title'},result.abstain?'אין תשובה נתמכת לשאלה המדויקת':'תשובה מתוך המחקר',button('סגור',()=>{out.hidden=true;}));
  if(result.abstain){out.replaceChildren(header,h('p',{class:'caption'},origin),note(result.reason+' נתונים היסטוריים נוספים זמינים בלשונית ההיסטוריה הפיננסית.','amber'));return;}
  out.replaceChildren(header,h('p',{class:'caption'},origin+' · תמונת נתונים מ־'+date(result.built_at||data.built_at)),result.availability_note?note(result.availability_note,'amber'):null,h('p',{class:'caption'},result.mode==='financial_history'?'תשובה מההיסטוריה הפיננסית של SEC. התקופה, ההגדרה והמקור מופיעים בכל נתון; זו שכבה נפרדת מסקירת המחקר.':'תשובה ממקורות המחקר שנבדקו, לפי תאריך כל חברה. דיווחים חדשים עשויים עדיין להמתין לסקירה.'),
    ...result.statements.map(s=>claimView({...s,text_he:s.text},data.companies.find(c=>c.ticker===s.ticker),true)));
}
$('question-form').addEventListener('submit',event=>{event.preventDefault();runQuestion($('question').value);});
$('examples').replaceChildren(...['איך מיקרוסופט מרוויחה כסף?','מה ההכנסות של מיקרוסופט ברבעון האחרון במאגר?','Compare AMD and NVDA risks'].map(q=>button(q,()=>{$('question').value=q;runQuestion(q);},'example')));
function validateData(value){
  if(value?.schema_version!==1||value.answer_contract_version!==2||!Array.isArray(value.companies)||!value.companies.length||new Set(value.companies.map(c=>c.ticker)).size!==value.companies.length||value.companies.some(c=>!Array.isArray(c.historical_index))||!value.config||!value.metric_patterns||!Number.isFinite(Date.parse(value.built_at)))throw Error('Invalid or incompatible research snapshot');
  return value;
}
async function fetchData(url){
  const response=await fetch(url,{cache:'no-store',signal:AbortSignal.timeout(15000)});
  if(!response.ok)throw Error('Snapshot request failed');
  return validateData(await response.json());
}
function display(value,origin){
  data=value;
  $('coverage-count').textContent=value.companies.length+' חברות במעקב';
  $('data-status').textContent=origin+' · נבנה ב־'+date(value.built_at);
  renderNavigation();renderCompanies();renderContent();
}
async function refresh(){
  const token=++loadToken;$('refresh').disabled=true;
  try{
    try{
      const remote=await fetchData('./api/snapshot');
      if(token!==loadToken)return;
      display(remote,'נתונים מהשרת');
      try{
        const response=await fetch('./api/status',{cache:'no-store',signal:AbortSignal.timeout(5000)});
        const status=response.ok?await response.json():null;
        if(token===loadToken&&status?.last_attempt?.status==='failed')$('data-status').textContent+=' · העדכון האחרון נכשל; מוצגים הנתונים שנשמרו';
      }catch{/* The dated snapshot remains usable when status is unavailable. */}
    }catch{
      if(token!==loadToken)return;
      if(!data)display(await fetchData('./snapshot.json'),'עותק מצורף');
      if(token===loadToken)$('data-status').textContent='עותק שמור מ־'+date(data.built_at)+' · לא התקבל עדכון מהשרת';
    }
  }catch{
    $('data-status').textContent='הנתונים אינם זמינים';
    $('content').replaceChildren(note('לא ניתן לטעון את הנתונים. נסה לרענן או פתח את המאגר ב־GitHub.','red'));
  }finally{if(token===loadToken)$('refresh').disabled=false;}
}
$('refresh').addEventListener('click',refresh);
refresh();

