import {ask,scenario} from './engine.mjs';
import {projectCompanyModel,requiredRevenueCagr} from './models.mjs';
import {personalStore,changesSinceVisit,groupQueue} from './workbench.mjs';

const $=id=>document.getElementById(id);
const NAV=[['overview','◫','תמונת המחקר'],['financials','▥','היסטוריה פיננסית'],['compare','⇄','השוואת חברות'],['scenarios','↗','תרחישי שווי'],['updates','◷','דיווחים ומעקב'],['coverage','⌕','מרשם החברות']];
const SECTIONS={'business-overview':'איך העסק עובד','revenue-model-and-segments':'מגזרים ומקורות הכנסה','products-and-services':'מוצרים ושירותים','customers-and-end-markets':'לקוחות ושווקים','industry-and-value-chain':'הענף ושרשרת הערך','competitive-landscape':'התחרות','moat-and-differentiation':'חפיר ובידול','growth-drivers':'מנועי צמיחה','financial-performance':'ביצועים פיננסיים','balance-sheet-and-capital-allocation':'מאזן והקצאת הון','management-and-governance':'הנהלה וממשל תאגידי','valuation-context':'הערכת שווי','catalysts':'זרזים ואבני דרך','risks-and-thesis-breakers':'סיכונים ושבירת התזה','scenarios-and-open-questions':'תרחישים ושאלות פתוחות','relationships-and-themes':'קשרים בין חברות','recent-developments':'התפתחויות אחרונות','sources-and-change-log':'מקורות והיסטוריית שינוי'};
const METRICS={revenue:'הכנסות',gross_profit:'רווח גולמי',cost_of_revenue:'עלות הכנסות',operating_income:'רווח תפעולי',net_income:'רווח נקי מיוחס לחברה אם',net_income_common:'רווח מיוחס למניות רגילות',net_income_including_noncontrolling_interests:'רווח כולל זכויות שאינן מקנות שליטה',eps_diluted:'רווח מדולל למניה',eps_basic:'רווח בסיסי למניה',operating_cash_flow:'תזרים מפעילות שוטפת',capex:'רכישת רכוש קבוע',free_cash_flow:'תזרים חופשי מחושב',purchases_of_productive_assets:'רכישת נכסים יצרניים, הגדרה רחבה',stock_based_compensation:'תגמול מבוסס מניות',cash_and_equivalents:'מזומנים ושווי מזומנים',short_term_investments:'השקעות קצרות טווח',debt_current:'חוב שוטף',debt_noncurrent:'חוב שאינו שוטף',long_term_debt_total:'סך חוב ארוך טווח',short_term_borrowings:'הלוואות קצרות טווח',debt_total:'חוב כולל מחושב',shares_basic:'ממוצע מניות, בסיסי',shares_diluted:'ממוצע מניות, מדולל',shares_outstanding:'מניות קיימות למועד המאזן'};
const KIND={reported:'נתון מדווח',derived:'חישוב',reported_fact:'נתון מדווח',management_guidance:'תחזית הנהלה',interpretation:'פרשנות',research_question:'שאלה למחקר'};
const state={tab:'overview',ticker:'MSFT',period:'annual',metric:'revenue',section:'business-overview',compare:new Set(['MSFT','NVDA']),comparePeriod:'ttm',queueTicker:'all',priority:'all',queueStatus:'pending'};
const personal=personalStore();
let visitRecorded=false;
let data=null,loadToken=0,answerToken=0,catalogToken=0;
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
function cell(c,p,key){return p?.type==='ttm'?(c.ttm?.financials?.[key]||c.ttm?.balance_sheet?.[key]):c.history?.financials?.[p?.id]?.[key];}
function latest(c,key){const p=periods(c,'annual')[0];return {period:p,cell:cell(c,p,key)};}
function note(text,kind=''){return h('div',{class:'notice '+kind},text);}
function option(value,label,selected){return h('option',{value,selected:selected?'':null},label);}
function button(text,handler,className='text-button'){return h('button',{type:'button',class:className,onClick:handler},text);}
function card(title,body,extra=null){return h('section',{class:'card'},h('div',{class:'card-head'},h('h2',{},title),extra),body);}
function sourceRefs(claim,c){
  const sources=claim.sources||(claim.evidence||[]).map(e=>({...c.sources.find(s=>s.id===e.source_id),locator:e.locator}));
  return sources.map((s,i)=>h('span',{},i?' · ':'',link(s.id+' ↗',s.url),h('span',{class:'sr-only'},s.title+' '+s.locator)));
}
function claimView(claim,c,answer=false){
  return h('article',{class:'claim'},answer?h('span',{class:'result-company',dir:'ltr'},c.ticker+' / '+(SECTIONS[claim.section]||'')):null,
    h('p',{dir:'auto'},claim.text_he||claim.text),
    h('div',{class:'claim-meta'},h('span',{class:'kind '+claim.kind},KIND[claim.kind]||claim.kind),
      sourceRefs(claim,c),h('span',{},(claim.source_kind==='financial_history'?'נתונים היסטוריים ל־':'מחקר ל־')+date(claim.as_of||c.as_of))));
}
function pendingCount(c){return data.triage?.summary?.by_company_pending?.[c.ticker]??c.freshness.pending_count??0;}
function companySummary(c){return h('div',{class:'company-summary'},h('div',{class:'company-avatar','aria-hidden':'true'},c.ticker.slice(0,1)),h('div',{},h('h2',{dir:'ltr'},c.name),h('p',{},c.ticker+' · '+({'information-technology':'טכנולוגיה','industrials':'תעשייה וביטחון'}[c.sector]||c.sector)+' · מחקר ל־'+date(c.as_of))),h('span',{class:'badge'},pendingCount(c)+' דיווחים ממתינים לסקירה'));}
function stat(label,value,description){return h('div',{class:'stat'},h('div',{class:'stat-label'},label),h('div',{class:'stat-value'},value),h('div',{class:'stat-note'},description));}
function thesisCard(c){
  const thesis=c.thesis;
  if(!thesis?.changes?.length)return card('מה השתנה בתזה?',note('עדיין אין השוואת תזה מאומתת בין שני דיווחים לחברה זו.'));
  const refs=side=>(side.source_ids||(side.source_id?[side.source_id]:[])).map(id=>thesis.sources.find(s=>s.id===id)).filter(Boolean);
  return card('מה השתנה בתזה?',h('div',{},h('p',{class:'caption'},'השוואת מקורות שנבדקה בידי AI · עד '+date(thesis.as_of)),...thesis.changes.map(change=>h('article',{class:'thesis-change'},
    h('h3',{},change.title_he||change.title||change.id),h('div',{class:'thesis-pair'},...['before','after'].map(side=>h('div',{},h('strong',{},side==='before'?'בדיווח הקודם':'בדיווח החדש'),h('p',{},change[side].text_he),h('details',{},h('summary',{},'מקור ומיקום'),...refs(change[side]).map(s=>h('p',{},link(s.title,s.url))),h('p',{class:'caption',dir:'auto'},change[side].locator||JSON.stringify(change[side].locators)))))),
    h('p',{class:'thesis-meaning'},h('strong',{},'משמעות לתזה · פרשנות: '),change.interpretation_he))),
    note('ההשוואה מתייחסת למקורות ולתאריכים המוצגים. דיווחים אחרים עשויים עדיין להמתין לסקירה.')));
}
function personalNotes(c){
  const saved=personal.note(c.ticker),area=h('textarea',{id:'research-note',rows:5,maxlength:12000,'aria-label':'הערות המחקר שלי',placeholder:'התזה שלי, מה לבדוק בדוח הבא, ומה ישנה את דעתי…'},saved?.text||'');
  const status=h('p',{class:'caption','aria-live':'polite'},saved?'נשמר ב־'+date(saved.saved_at):'');
  return card('הערות המחקר שלי',h('div',{},area,h('div',{class:'section-tools'},button('שמור הערות',()=>{status.textContent=personal.saveNote(c.ticker,area.value)?'ההערות נשמרו בדפדפן הזה.':'לא ניתן לשמור בדפדפן הזה. העתק את ההערה לפני יציאה.';},'primary')),status,h('p',{class:'caption'},'נשמר בדפדפן הזה בלבד. ההערות הן שלך ואינן חלק מהמחקר שנבדק.')));
}
function visitCard(){
  const delta=changesSinceVisit(data,personal.previousVisit);
  return card('מה השתנה מאז הביקור האחרון?',delta.first?note('זהו הביקור הראשון שנשמר בדפדפן הזה. מהביקור הבא יוצגו כאן מחקרים שהתעדכנו ודיווחים חדשים.'):h('div',{},h('p',{class:'caption'},'מאז '+date(delta.since)+' · לפי היסטוריית הדפדפן הזה'),h('p',{},delta.companies.length?'מחקר או השוואת תזה עודכנו: '+delta.companies.join(', '):'לא נוסף עדכון מחקר לחברות במעקב.'),h('p',{},delta.events.length+' דיווחים חדשים נוספו לתור.'),delta.events.length?button('פתח את תור הדיווחים ←',()=>navigate('updates')):null));
}
function dataDates(c){
  return h('div',{class:'data-dates'},h('span',{},'מחקר: '+date(c.as_of)),h('span',{},'שליפת נתונים פיננסיים: '+date(c.history?.source?.retrieved_at)),h('span',{},'עסקת המחיר: '+date(c.quote?.trade_at)));
}
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
  return [companySummary(c),dataDates(c),stats,h('div',{class:'grid-2'},h('div',{},thesisCard(c),main,performance,history),h('div',{},visitCard(),personalNotes(c),growth,risk,gaps))];
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
  const ttm=state.comparePeriod==='ttm',period=c=>ttm?c.ttm?.period:periods(c,'annual')[0];
  const periodControl=h('div',{class:'segmented'},...['ttm','annual'].map(key=>button(key==='ttm'?'ארבעת הרבעונים האחרונים · TTM':'שנה מדווחת אחרונה',()=>{state.comparePeriod=key;renderContent();},state.comparePeriod===key?'active':'')));
  const checkboxes=h('div',{class:'section-tools'},...data.companies.map(c=>h('label',{class:'check-company'},h('input',{type:'checkbox',checked:state.compare.has(c.ticker),onChange:e=>{if(e.target.checked)state.compare.add(c.ticker);else state.compare.delete(c.ticker);renderContent();}}),c.ticker)));
  const keys=['revenue','gross_profit','operating_income','net_income','operating_cash_flow','free_cash_flow','stock_based_compensation','cash_and_equivalents','debt_total'];
  const heads=selected.map(c=>{const p=period(c);return h('th',{scope:'col'},c.ticker,h('span',{class:'period-date'},p?(ttm?'TTM':p.label)+' · '+p.start+' – '+p.end:'אין תקופה תקפה'));});
  const rows=keys.map(key=>h('tr',{},h('td',{},METRICS[key],h('span',{class:'metric-unit'},'מיליוני דולר'+(['cash_and_equivalents','debt_total'].includes(key)?' · יתרה בסוף התקופה':''))),...selected.map(c=>h('td',{},cellView(c,period(c),key)))));
  for(const [key,label] of [['gross_margin','שיעור רווח גולמי'],['operating_margin','שיעור רווח תפעולי'],['net_margin','שיעור רווח נקי'],['fcf_margin','תזרים חופשי / הכנסות'],['sbc_to_revenue','תגמול מנייתי / הכנסות']]){
    const cells=selected.map(c=>{
      const p=period(c),ratio=ttm?c.ttm?.ratios?.[key]:c.ratios.find(r=>r.period.id===p?.id)?.ratios[key];
      const detail=ratio?h('details',{class:'cell-detail'},h('summary',{},'נוסחה ומקורות'),h('p',{dir:'ltr'},ratio.formula||'הנתונים הדרושים חסרים או אינם תואמים'),...(ratio.source_urls||[]).map(url=>h('p',{},link('דיווח SEC ↗',url)))):null;
      return h('td',{},h('span',{class:'metric-value'},pct(ratio?.value)),detail);
    });
    rows.push(h('tr',{},h('td',{},label,h('span',{class:'metric-unit'},'חישוב מנתונים תואמים')),...cells));
  }
  const table=h('table',{},h('thead',{},h('tr',{},h('th',{scope:'col'},'מדד'),...heads)),h('tbody',{},...rows));
  return [card(ttm?'השוואת TTM לפי הרבעונים האחרונים במאגר':'השוואה לפי השנה המדווחת האחרונה',h('div',{},periodControl,checkboxes,note('התקופות המדויקות מוצגות בכל עמודה, ועשויות להסתיים בתאריכים שונים. הטבלה אינה מדרגת תקופות שונות כאילו הן זהות. '+(ttm?'TTM מחבר רק ארבעה רבעונים רצופים עם הגדרות תואמות; יתרות מאזן מוצגות בנפרד למועד הסיום. EPS וממוצע מניות אינם מסוכמים.':''),'amber'),selected.length?h('div',{class:'table-wrap',tabindex:'0','aria-label':'השוואת חברות'},table):note('בחר לפחות חברה אחת.')))];
}
function companyModel(c){
  const model=c.model;
  if(!model)return card('מודל חברה ל־2027–2030',note('מודלים מפורטים זמינים כרגע ל־MSFT, MU ו־NVDA.'));
  if(!model.scenarios?.length||model.readiness?.status==='blocked')return card('מודל חברה ל־2027–2030',note('חסרים נתוני בסיס מאומתים להפעלת המודל. '+(model.readiness?.reasons||[]).join(', '),'amber'));
  const saved=personal.scenario(c.ticker),compatible=saved?.model_as_of===model.as_of;
  const initial=compatible?saved.overrides:{};
  const out=h('div',{'aria-live':'polite',class:'model-results'}),status=h('p',{class:'caption','aria-live':'polite'});
  const caseSelect=h('select',{'aria-label':'תרחיש במודל החברה'},...model.scenarios.map(s=>option(s.id,s.label_he||s.label,s.id===(initial.scenarioId||'base'))));
  const fields=[['revenueGrowth','צמיחת הכנסות שנתית (%)',-99.9,300],['netMargin','שיעור רווח נקי (%)',-100,100],['fcfMargin','שיעור תזרים חופשי (%)',-100,100],['shareChange','שינוי שנתי במניות (%)',-50,50],['exitPe','מכפיל רווח בסוף 2030',.01,100]];
  const inputs=Object.fromEntries(fields.map(([key,label,min,max])=>[key,h('input',{id:'model-'+key,type:'number',step:'any',min,max,value:initial[key]===undefined?'':initial[key]*(key==='exitPe'?1:100),placeholder:'לפי התרחיש','aria-label':label})]));
  const price=h('input',{type:'number',step:'any',min:'.0001',required:true,value:initial.referencePrice||c.quote?.price||'','aria-label':'מחיר ייחוס למודל'});
  const read=()=>Object.fromEntries([['scenarioId',caseSelect.value],['referencePrice',Number(price.value)],...fields.filter(([key])=>inputs[key].value!=='').map(([key])=>[key,Number(inputs[key].value)/(key==='exitPe'?1:100)])]);
  const draw=overrides=>{
    try{
      const result=projectCompanyModel(model,overrides);
      if(!result.scenarios?.length){out.replaceChildren(note('לא ניתן לחשב מהנתונים או ההנחות הנוכחיים. '+(result.reasons||[]).join(', '),'amber'));return;}
      const chosen=result.scenarios.find(s=>s.id===(overrides.scenarioId||'base'))||result.scenarios[0];
      const cards=h('div',{class:'model-cards'},...result.scenarios.map(s=>h('article',{class:'model-card '+(s.id===chosen.id?'selected':'')},h('h3',{},s.label_he||s.label),h('div',{class:'scenario-price'},s.terminal.price===null?'לא זמין':num(s.terminal.price)+' $'),h('p',{},'שינוי שנתי במחיר: '+pct(s.terminal.annualized_return)),h('p',{},'הכנסות 2030: '+compact(s.terminal.revenue)+' $'),h('p',{class:'caption'},s.rationale_he||s.rationale))));
      const columns=[['fiscal_year','שנת כספים',num],['revenue','הכנסות ($)',compact],['net_income','רווח נקי ($)',compact],['free_cash_flow','תזרים חופשי ($)',compact],['shares_diluted','מניות מדוללות',compact],['eps','רווח למניה ($)',num]];
      const table=h('div',{class:'table-wrap',tabindex:0},h('table',{},h('thead',{},h('tr',{},...columns.map(([,title])=>h('th',{},title)))),h('tbody',{},...chosen.rows.map(row=>h('tr',{},...columns.map(([key,,format])=>h('td',{},key==='fiscal_year'?String(row[key]):format(row[key]))))))));
      const reverse=requiredRevenueCagr(model,chosen.id,Number(overrides.referencePrice||c.quote?.price),0);
      const baseScenario=model.scenarios.find(s=>s.id===chosen.id);
      const assumptions=h('details',{},h('summary',{},'הנחות התרחיש המקורי לפי שנה'),h('p',{class:'caption'},'שדות החלופה שהזנת מחליפים את ההנחה המקבילה בכל ארבע השנים של התרחיש הנבחר.'),h('div',{class:'table-wrap'},h('table',{},h('thead',{},h('tr',{},...['שנה','צמיחת הכנסות','רווח נקי / הכנסות','תזרים חופשי / הכנסות','שינוי במניות'].map(t=>h('th',{},t)))),h('tbody',{},...baseScenario.years.map(y=>h('tr',{},h('td',{},String(y.fiscal_year)),...['revenue_growth','net_margin','fcf_margin','share_change'].map(k=>h('td',{},pct(y[k])))))))),h('p',{},'מכפיל יציאה מקורי: '+num(baseScenario.exit_pe)));
      out.replaceChildren(cards,h('h3',{},'מסלול '+(chosen.label_he||chosen.label)+' · הנחות וחישובים'),table,assumptions,
        note(reverse.status==='illustrative'?'בדיקת המחיר: בהנחות הרווחיות, המניות והמכפיל המקוריות של תרחיש '+(chosen.label_he||chosen.label)+', נדרשת צמיחת הכנסות שנתית של '+pct(reverse.required_revenue_cagr)+' מבסיס FY2026 כדי שמחיר סוף התקופה יהיה זהה למחיר הייחוס. זהו חישוב הפוך, ולא תחזית.':'החישוב ההפוך אינו זמין לבסיס הנתונים הנוכחי.'));
    }catch{out.replaceChildren(note('בדוק שההנחות והמחיר נמצאים בטווחים המותרים.','red'));}
  };
  const form=h('form',{id:'company-model-form',onSubmit:e=>{e.preventDefault();draw(read());}},h('div',{class:'section-tools'},h('label',{},'תרחיש לעריכה ',caseSelect),h('label',{},'מחיר ייחוס ($) ',price)),h('p',{class:'caption'},'חלופה אחידה לכל שנה בתרחיש הנבחר. השאר שדה ריק לשימוש במסלול המקורי.'),h('div',{class:'model-fields'},...fields.map(([key,label])=>h('label',{class:'field'},label,inputs[key]))),h('div',{class:'section-tools'},h('button',{class:'primary',type:'submit'},'חשב מחדש'),button('שמור את התרחיש שלי',()=>{if(!form.reportValidity())return;const values=read();draw(values);status.textContent=personal.saveScenario(c.ticker,model.as_of,values)?'התרחיש נשמר בדפדפן הזה.':'לא ניתן לשמור בדפדפן הזה.';}),button('חזור להנחות המקוריות',()=>{fields.forEach(([key])=>{inputs[key].value='';});draw(read());})),status);
  const sources=h('details',{},h('summary',{},'בסיס הנתונים, מקורות ומגבלות'),h('p',{},'בסיס: '+model.base.period.label+' · עד '+date(model.base.period.end)+' · הנחות מתוארכות ל־'+date(model.as_of)),h('p',{},'הכנסות: '+compact(model.base.revenue)+' $ · מניות מדוללות: '+compact(model.base.shares_diluted)),...model.sources.map(s=>h('p',{},link(s.title,s.url))),h('ul',{},...(model.limitations_he||model.limitations||[]).map(x=>h('li',{},typeof x==='string'?x:JSON.stringify(x)))));
  draw(initial);
  return card('מודל '+c.ticker+' · שנות הכספים 2027–2030',h('div',{},note('תרחישים להמחשה, המבוססים על הנחות מחקר מפורשות. הם אינם תחזית הנהלה, קונצנזוס אנליסטים או מחיר יעד. השינוי במחיר אינו כולל דיבידנדים, מס, עמלות ומט״ח.','amber'),saved&&!compatible?note('מודל הבסיס השתנה מאז השמירה. מוצגות ההנחות החדשות; התרחיש הקודם לא הוחל אוטומטית.'):null,h('p',{class:'caption'},'מחיר השוק במאגר: '+num(c.quote?.price)+' $ · עסקה מ־'+date(c.quote?.trade_at)+'. שמירה מקומית בדפדפן הזה בלבד.'),form,out,sources));
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
  return [companySummary(c),companyModel(c),card('מחשבון רגישות חופשי לפי EPS',h('details',{},h('summary',{},'פתח את המחשבון הכללי'),baseInfo,form,h('div',{id:'scenario-result','aria-live':'polite'}),h('p',{class:'caption',dir:'ltr'},'EPS × (1 + growth)^years × exit P/E'),h('p',{class:'caption'},'השינוי המוצג הוא במחיר בלבד, ללא דיבידנדים, מס, עמלות או מט״ח. המכפיל דורש EPS חיובי; אין תמיכה בתרחיש הפסד או בשינוי עתידי במספר המניות.')))];
}
function calculateScenario(rows){
  const out=$('scenario-result');
  try{
    const eps=Number($('scenario-eps').value),price=Number($('scenario-price').value),years=Number($('scenario-years').value);
    const cards=rows.map(([name],i)=>{const result=scenario(eps,Number($('growth-'+i).value)/100,Number($('pe-'+i).value),years,price);return h('article',{class:'scenario-card'},h('h3',{},'תרחיש '+name+' · '+years+' שנים'),h('div',{class:'scenario-price'},num(result.terminalPrice)+' $'),h('p',{},'שינוי במחיר: ',h('bdi',{class:result.change<0?'negative':''},pct(result.change))),h('p',{},'שינוי שנתי מחושב: ',h('bdi',{},pct(result.annualized))),h('p',{},'EPS סופי: ',h('bdi',{},num(result.terminalEPS)+' $')));});
    out.replaceChildren(h('div',{class:'scenario-output'},cards));
  }catch{out.replaceChildren(note('יש להזין EPS ומחיר חיוביים, צמיחה מעל ‎-100%, מכפיל עד 200 ואופק של שנה עד עשר שנים.','red'));}
}
function coverageCatalog(){
  const scope=note('מניות הנסחרות בבורסות בארה״ב, כולל מניות בכורה, תעודות פיקדון ויחידות שותפות. כיסוי OTC טרם נוסף. הסיווג מבוסס על רשימות המסחר ושמות הניירות; מועמדות עדיין דורשות בדיקה. רישום למסחר אינו מעיד שהמידע הפיננסי נאסף או שהמחקר הושלם.');
  const query=h('input',{type:'search',placeholder:'שם חברה, סימול או CIK','aria-label':'חיפוש במרשם החברות'});
  const instrument=h('select',{'aria-label':'סוג נייר'},option('equities','מניות ומועמדות',true),option('stocks','מניות שסווגו לפי הרשימה'),option('preferred','מניות בכורה'),option('partnership_unit','יחידות שותפות'),option('all','כל סוגי הניירות'),option('etf','קרנות ETF'),option('unknown','סיווג טעון בדיקה'));
  const types={common_stock:'מניה רגילה',depositary_receipt:'תעודת פיקדון',partnership_unit:'יחידת שותפות',equity_candidate:'מועמדת · סוג הנייר טרם אומת',etf:'ETF',preferred:'מניית בכורה',warrant:'כתב אופציה',unit:'יחידה',right:'זכות',debt:'חוב',managed_fund:'קרן מנוהלת'};
  const datasets={profile:'פרופיל חברה',financials:'דוחות כספיים',prices:'מחירי מסחר',filings:'דיווחים',news:'חדשות',estimates:'תחזיות אנליסטים',ownership:'בעלי מניות'};
  const results=h('div',{'aria-live':'polite'}),detail=h('div',{}),summary=h('p',{class:'caption'}),coverageInfo=h('p',{class:'caption'}),progressInfo=h('p',{class:'caption','aria-label':'התקדמות כיסוי המידע'});
  let offset=0,total=0;
  const load=async()=>{
    const token=++catalogToken;results.replaceChildren(note('טוען חברות…'));detail.replaceChildren();
    try{
      const response=await fetch('./api/securities?q='+encodeURIComponent(query.value)+'&instrument='+encodeURIComponent(instrument.value)+'&limit=25&offset='+offset,{signal:AbortSignal.timeout(15000)});
      if(!response.ok)throw Error('registry unavailable');
      const page=await response.json();if(!Array.isArray(page.items)||!Number.isInteger(page.total))throw Error('invalid registry');
      if(token!==catalogToken)return;
      total=page.total;summary.textContent=total+' ניירות תואמים · '+(total?offset+1:0)+'–'+Math.min(offset+25,total)+' מוצגים · רשימה נבדקה: '+date(page.directory?.imported_at)+(page.directory?.status==='stale'?' · העדכון היומי מתעכב':'');
      const counts=page.directory?.data_coverage||{};
      coverageInfo.textContent='כיסוי מידע בכל המרשם: דוחות כספיים '+(counts.financials||0)+' · מחירים '+(counts.prices||0)+' · מחקר שנבדק '+(counts.reviewed_research||0)+'. כל נתון נשמר עם תאריך המקור שלו.';
      const progress=page.directory?.coverage_progress,checks=progress?.filing_checks;
      progressInfo.textContent=progress?'מניות ומועמדות במאגר: '+progress.total_listings+' · קישור לזהות חברה: '+progress.mapped_listings+' · ממתינות לקישור: '+progress.unmapped_listings+' · חברות מזוהות שונות: '+progress.distinct_mapped_issuers+'. בדיקת דיווחים ב־48 השעות האחרונות: '+(checks?.recent||0)+' · בדיקה מתעכבת: '+(checks?.overdue||0)+' · טרם נבדקו: '+(checks?.not_checked||0)+'. עדכון רשימת המסחר אינו עדכון של דוחות החברה.':'';
      results.replaceChildren(...page.items.map(row=>h('article',{class:'registry-row'},h('div',{},h('h3',{dir:'auto'},row.security_name||row.ticker),h('p',{class:'caption',dir:'auto'},row.ticker+' · '+row.exchange+(row.cik?' · CIK '+row.cik:'')),h('p',{class:'caption'},types[row.instrument_type]||'סוג אחר', ' · ',row.datasets?.financials?.retrieved_at?'קיימים נתונים פיננסיים מתוארכים':'נתונים פיננסיים טרם נאספו')),button('פתח נייר ←',()=>openSecurity(row.listing_key),'text-button'))));
      if(!page.items.length)results.append(note('לא נמצאו חברות במסנן הזה.'));
      previous.disabled=offset===0;next.disabled=offset+25>=total;
    }catch{if(token===catalogToken)results.replaceChildren(note('מרשם החברות אינו זמין בחיבור הנוכחי. המחקר שנבדק עדיין זמין בלשוניות האחרות.','amber'));}
  };
  const openSecurity=async key=>{
    const token=++catalogToken;detail.replaceChildren(note('טוען את מצב הכיסוי…'));
    try{
      const response=await fetch('./api/securities/'+encodeURIComponent(key),{signal:AbortSignal.timeout(15000)});
      if(!response.ok)throw Error('security unavailable');
      const item=await response.json();if(token!==catalogToken)return;
      const security=item.security;if(!security)throw Error('invalid security');
      const rows=Object.entries(datasets).map(([key,label])=>{const value=security.datasets?.[key];return h('tr',{},h('td',{},label),h('td',{},value?.retrieved_at?'נאסף · '+date(value.retrieved_at):'טרם נאסף'));});
      detail.replaceChildren(card(security.security_name,h('div',{},h('p',{dir:'auto'},security.ticker+' · '+security.exchange+' · '+(types[security.instrument_type]||'סוג אחר')),
        note(security.cik?'זהות המנפיק מקושרת. כל תחום מידע מוצג לפי מועד האיסוף שלו.':'זהות המנפיק עדיין דורשת קישור מאומת. רישום נייר למסחר אינו מחקר על החברה.'),
        h('p',{class:'caption'},'בדיקת דיווחים אחרונה: '+date(security.filing_check?.last_checked_at)+(security.filing_check?.status==='overdue'?' · נדרשת בדיקה חדשה':security.filing_check?.status==='recent'?' · נבדק ב־48 השעות האחרונות':' · בדיקה עדכנית טרם הושלמה')),
        h('div',{class:'table-wrap'},h('table',{},h('tbody',{},...rows))),
        h('p',{class:'caption'},'רשימת המסחר נשלפה: '+date(security.source?.retrieved_at)+' · תאריך קובץ המקור: '+date(security.source?.file_created_at_local)),
        link('רשימת המסחר המקורית ↗',security.source?.url),
        security.cik?button('הצג נתונים פיננסיים ומחקר ←',()=>openCompany(security.cik)):null)));
    }catch{if(token===catalogToken)detail.replaceChildren(note('לא ניתן לטעון את הנייר כעת.','amber'));}
  };
  const openCompany=async cik=>{
    const token=++catalogToken;detail.replaceChildren(note('טוען את נתוני החברה…'));
    try{
      const response=await fetch('./api/companies/'+encodeURIComponent(cik),{signal:AbortSignal.timeout(15000)});
      if(!response.ok)throw Error('company unavailable');
      const item=await response.json();if(token!==catalogToken)return;
      const company=item.company,history=item.collected?.history,ttm=item.ttm;
      if(!company)throw Error('invalid company');
      const title=company.name||company.company_name||company.cik;
      const metrics=['revenue','operating_income','net_income','operating_cash_flow','free_cash_flow'];
      const rows=metrics.map(key=>h('tr',{},h('td',{},METRICS[key]),h('td',{},cellValue(ttm?.financials?.[key]))));
      const changes=item.collected?.automatic_changes;
      const changeRows=(changes?.changes||[]).map(change=>h('tr',{},h('td',{},METRICS[change.metric]||change.metric),
        h('td',{},cellValue({value:change.previous_value,unit:change.unit}),h('div',{class:'caption',dir:'ltr'},change.previous_period_start?change.previous_period_start+' – '+change.previous_period_end:'—')),
        h('td',{},cellValue(change),h('div',{class:'caption',dir:'ltr'},change.period_start+' – '+change.period_end)),
        h('td',{},change.comparison==='comparable'?cellValue({value:change.delta,unit:change.unit}):change.comparison==='new_coverage'?'כיסוי חדש':'השוואה חסומה'),
        h('td',{},...(change.source_urls||[]).map((url,i)=>link('מקור '+(i+1)+' ↗',url)))));
      detail.replaceChildren(card(title,h('div',{},note(item.collection_status==='registry-only'?'החברה נוספה למרשם; הנתונים הפיננסיים טרם נאספו.':'נתונים שנאספו אוטומטית. מדדים שאינם עומדים בבדיקות ההתאמה נשארים חסומים.'),
        h('p',{class:'caption'},'מקור פיננסי נשלף ב־'+date(history?.source?.retrieved_at)+' · מחקר שנבדק: '+(item.research?.as_of?date(item.research.as_of):'טרם הושלם')),
        ttm?.period?h('div',{},h('h3',{},'TTM · ארבעה רבעונים רצופים במאגר'),h('p',{class:'caption',dir:'ltr'},ttm.period.start+' – '+ttm.period.end+' · USD millions'),h('div',{class:'table-wrap'},h('table',{},h('tbody',{},...rows))),h('details',{},h('summary',{},'מקורות החישוב'),...(ttm.source_urls||[]).map(url=>h('p',{},link('דיווח מקור ↗',url))))):note('עדיין אין ארבעה רבעונים תקפים לחישוב TTM.'),
        changes?h('details',{},h('summary',{},'טיוטת השינויים האוטומטית'),h('p',{class:'caption'},'השוואת נתונים שטרם עברה סקירת מחקר · סכומים ומניות במיליונים, EPS בדולר למניה. שינוי בין תקופות מוצג רק כשההגדרות תואמות; זו אינה בהכרח השוואה שנתית.'),
          changeRows.length?h('div',{class:'table-wrap'},h('table',{},h('thead',{},h('tr',{},...['מדד','בתצפית הקודמת','בתצפית החדשה','הפרש','מקורות'].map(title=>h('th',{},title)))),h('tbody',{},...changeRows))):note('אין שינוי מספרי בר השוואה בטיוטה זו.'),
          ...(changes.limitations||[]).map(text=>h('p',{class:'caption',dir:'auto'},text))):null)));
    }catch{if(token===catalogToken)detail.replaceChildren(note('לא ניתן לטעון את החברה כעת.','amber'));}
  };
  const previous=button('הקודם',()=>{offset=Math.max(0,offset-25);load();}),next=button('הבא',()=>{offset+=25;load();});
  const form=h('form',{class:'section-tools',onSubmit:e=>{e.preventDefault();offset=0;load();}},query,instrument,h('button',{type:'submit',class:'primary'},'חפש'));
  const body=card('חיפוש מניות בארה״ב',h('div',{},scope,form,summary,coverageInfo,progressInfo,results,h('div',{class:'section-tools'},previous,next)));
  load();
  return [body,detail];
}
function updates(){
  const summary=data.triage?.summary,entries=data.triage?.entries||[];
  const errors=Object.entries(data.source_health||{}).flatMap(([ticker,health])=>(health.errors||[]).map(e=>h('p',{class:'caption'},ticker+' · '+e.error+' ',e.source?.startsWith('https://')?link('מקור',e.source):null)));
  const refreshErrors=(data.refresh_status?.financials||[]).concat(data.refresh_status?.market||[]).filter(r=>r.status==='error').map(e=>h('p',{class:'caption'},e.ticker+' · '+e.error));
  const coverage=h('div',{class:'coverage'},...data.companies.map(c=>h('div',{class:'coverage-item '+(c.freshness.coverage_status!=='checked'?'error':'')},h('strong',{},c.ticker),h('span',{},'SEC: '+(c.freshness.sec_coverage_status==='checked'?'נבדק בהצלחה':'כיסוי חסר או לא נבדק')),h('span',{},'אתר החברה: '+(c.freshness.issuer_coverage_status==='checked'?'נבדק בהצלחה':'כיסוי חלקי או לא נבדק')),h('span',{},pendingCount(c)+' ממתינים לסקירה'),h('details',{},h('summary',{},'זמני בדיקת המקורות'),...(c.freshness.source_checks||[]).map(s=>h('p',{class:'caption'},(s.kind||s.source_type||'מקור')+' · ניסיון: '+date(s.attempted_at)+' · הצלחה אחרונה: '+date(s.last_successful_check_at)))))));
  const controls=h('div',{class:'section-tools'},h('label',{for:'queue-company'},'חברה'),h('select',{id:'queue-company',onChange:e=>{state.queueTicker=e.target.value;renderContent();}},option('all','כל החברות',state.queueTicker==='all'),...data.companies.map(c=>option(c.ticker,c.ticker,state.queueTicker===c.ticker))),h('label',{for:'queue-priority'},'עדיפות'),h('select',{id:'queue-priority',onChange:e=>{state.priority=e.target.value;renderContent();}},option('all','כל העדיפויות',state.priority==='all'),...['P0','P1','P2','P3'].map(p=>option(p,p,state.priority===p))));
  controls.append(h('label',{for:'queue-status'},'מצב'),h('select',{id:'queue-status',onChange:e=>{state.queueStatus=e.target.value;renderContent();}},option('pending','ממתינים לסקירה',state.queueStatus==='pending'),option('all','כל הדיווחים',state.queueStatus==='all')));
  const filtered=groupQueue(entries,data.queue).filter(g=>(state.queueTicker==='all'||g.ticker===state.queueTicker)&&(state.priority==='all'||g.entries.some(e=>e.priority===state.priority))&&(state.queueStatus==='all'||g.pending>0));
  return [h('div',{class:'stats'},stat('דיווחים הממתינים לסקירה',summary?.pending??'—','הכותרות עדיין אינן מסקנות מחקר'),stat('עדיפות גבוהה · P0',summary?.by_priority?.P0??'—','תוצאות ודיווחים כספיים'),stat('תור להמשך בדיקה · P1',summary?.by_priority?.P1??'—','דיווחים, עסקאות ומינויים'),stat('סריקת המקורות',date(data.scan_at),'תאריך סריקה, לא תאריך אישור מחקר')),
    card('כיסוי המקורות',h('div',{},coverage,h('p',{class:'caption'},'מקורות עם בדיקה חלקית או שגיאה: '+(data.companies.filter(c=>c.freshness.coverage_status!=='checked').map(c=>c.ticker).join(', ')||'אין')+'. הצלחה בסריקה אינה מעידה שכל הדיווחים עברו סקירת תוכן.'),h('details',{},h('summary',{},'פרטי תקלות האיסוף'),errors,refreshErrors))),
    card('תור הדיווחים',h('div',{},h('p',{class:'caption'},link('סקירת הדיווחים הקריטיים והעדכונים המוצעים ↗',data.repository+'/blob/main/docs/P0_REVIEW.md')),note('העדיפות נקבעת לפי מטא־נתונים לצורך סדר העבודה. סגירת דיווח דורשת קריאת מקור והשוואה למחקר הקיים; הסריקה אינה מאשרת אוטומטית את המחקר.'),controls,
      h('p',{class:'caption'},filtered.length+' אירועים במסנן. דיווחים קשורים מקובצים לתצוגה לפי מטא־נתונים; כל מסמך שומר על מצב הסקירה שלו.'),
      filtered.length?h('div',{},...filtered.map(g=>h('article',{class:'queue-item'},h('span',{class:'priority '+g.priority},g.priority),h('div',{},h('h3',{},g.title),h('div',{class:'caption'},g.ticker+' · '+date(g.published_at)+' · '+g.entries.length+' מסמכים · '+g.pending+' ממתינים לסקירה'),...g.entries.map(e=>h('p',{class:'queue-document'},link(e.title||'מקור',e.url),' · ',e.queue_status==='pending_review'?'ממתין לסקירה':e.classification==='already_in_reviewed_evidence'?'מקושר למחקר שנבדק':'החלטת סקירה מתועדת')))))):note('אין דיווחים במסנן הנוכחי.')))];
}
function navigate(tab){state.tab=tab;renderNavigation();renderContent();}
function renderNavigation(){
  $('page-title').textContent=NAV.find(n=>n[0]===state.tab)[2];
  $('navigation').replaceChildren(...NAV.map(([id,icon,label])=>h('button',{type:'button',class:'nav-button '+(state.tab===id?'active':''),'aria-current':state.tab===id?'page':null,onClick:()=>navigate(id)},h('span',{class:'nav-icon','aria-hidden':'true'},icon),label)));
}
function renderCompanies(){
  $('selected-label').textContent=company().name;
  $('companies').replaceChildren(...data.companies.map(c=>h('button',{type:'button',class:'company-button '+(c.ticker===state.ticker?'active':''),'aria-pressed':c.ticker===state.ticker,onClick:()=>{state.ticker=c.ticker;renderCompanies();renderContent();}},h('strong',{dir:'ltr'},c.ticker),h('small',{},h('span',{class:'pending-dot','aria-hidden':'true'}),pendingCount(c)+' לבדיקה'))));
}
function renderContent(){
  const c=company();
  const pages={overview:()=>overview(c),financials:()=>financials(c),compare,scenarios:()=>scenarios(c),updates,coverage:coverageCatalog};
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
  out.replaceChildren(...[header,h('p',{class:'caption'},origin+' · תמונת נתונים מ־'+date(result.built_at||data.built_at)),result.availability_note?note(result.availability_note,'amber'):null,h('p',{class:'caption'},result.mode==='financial_history'?'תשובה מההיסטוריה הפיננסית של SEC. התקופה, ההגדרה והמקור מופיעים בכל נתון; זו שכבה נפרדת מסקירת המחקר.':'תשובה ממקורות המחקר שנבדקו, לפי תאריך כל חברה. דיווחים חדשים עשויים עדיין להמתין לסקירה.'),
    ...result.statements.map(s=>claimView({...s,text_he:s.text},data.companies.find(c=>c.ticker===s.ticker),true))].filter(Boolean));
}
$('question-form').addEventListener('submit',event=>{event.preventDefault();runQuestion($('question').value);});
$('examples').replaceChildren(...['איך מיקרוסופט מרוויחה כסף?','מה ההכנסות של מיקרוסופט ברבעון האחרון במאגר?','מה השתנה בתזה של מיקרון מאז הדוח הקודם?'].map(q=>button(q,()=>{$('question').value=q;runQuestion(q);},'example')));
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
  if(!visitRecorded){personal.markVisit(value);visitRecorded=true;}
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

