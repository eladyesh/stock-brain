const SECTORS={'communication-services':'תקשורת','consumer-discretionary':'צריכה מחזורית','consumer-staples':'צריכה בסיסית',energy:'אנרגיה',financials:'פיננסים','health-care':'בריאות',industrials:'תעשייה','information-technology':'טכנולוגיה',materials:'חומרי גלם','real-estate':'נדל״ן',utilities:'תשתיות ושירותים',unclassified:'ממתין לסיווג'};
const STAGES={pending:'ממתין לאיסוף מקורות',retry:'נדרש ניסיון איסוף נוסף',source_missing:'נדרש איתור דוח מקור',evidence_collected:'קטעי מקור נאספו · טרם נבדקו',draft:'טיוטת מחקר · טרם נבדקה'};

// Render only text and our own elements. Source Markdown never becomes HTML.
export function markdownView(text,sources,{h,link}){
  const refs=new Map(sources.map(s=>[s.id,s]));
  const inline=value=>{
    const parts=[],pattern=/(\[(S\d+)\]|\[([^\]]+)\]\((https:\/\/[^\s)]+)\)|\*\*([^*]+)\*\*|`([^`]+)`)/g;
    let last=0;
    for(const match of value.matchAll(pattern)){
      parts.push(value.slice(last,match.index));
      if(match[2])parts.push(refs.has(match[2])?link(match[2]+' ↗',refs.get(match[2]).url):match[0]);
      else if(match[3])parts.push(link(match[3],match[4]));
      else if(match[5])parts.push(h('strong',{},match[5]));
      else parts.push(h('code',{},match[6]));
      last=match.index+match[0].length;
    }
    parts.push(value.slice(last));return parts;
  };
  const lines=String(text||'').split('\n'),out=[];
  for(let i=0;i<lines.length;i++){
    const line=lines[i].trim();if(!line)continue;
    if(line.startsWith('|')){
      const rows=[];while(i<lines.length&&lines[i].trim().startsWith('|')){const cells=lines[i].trim().split('|').slice(1,-1).map(x=>x.trim());if(!cells.every(x=>/^:?-+:?$/.test(x)))rows.push(cells);i++;}i--;
      out.push(h('div',{class:'table-wrap'},h('table',{},h('thead',{},h('tr',{},...(rows.shift()||[]).map(c=>h('th',{},inline(c))))),h('tbody',{},...rows.map(r=>h('tr',{},...r.map(c=>h('td',{},inline(c)))))))));continue;
    }
    if(line.startsWith('### ')){out.push(h('h3',{},inline(line.slice(4))));continue;}
    if(line.startsWith('- ')){const items=[];while(i<lines.length&&lines[i].startsWith('- ')){items.push(h('li',{},inline(lines[i].slice(2))));i++;}i--;out.push(h('ul',{},items));continue;}
    if(line.startsWith('> ')){out.push(h('blockquote',{},inline(line.slice(2))));continue;}
    const paragraph=[line];while(i+1<lines.length&&lines[i+1].trim()&&!/^(?:\||### |\- |\> )/.test(lines[i+1]))paragraph.push(lines[++i]);
    out.push(h('p',{},inline(paragraph.join('\n'))));
  }
  return h('div',{class:'research-document',dir:'ltr'},out);
}

export function researchView(ui,initialSymbol=''){
  const {h,card,button,note,link,date,option,sections,onCount,onSelect}=ui;
  const query=h('input',{type:'search',placeholder:'AAPL, JPM, שם חברה…','aria-label':'חיפוש מחקר לפי סימול או חברה',value:initialSymbol});
  const sector=h('select',{'aria-label':'סינון מחקר לפי סקטור'},option('','כל הסקטורים',true));
  const stage=h('select',{'aria-label':'שלב מחקר'},option('','כל שלבי המחקר',true),...Object.entries(STAGES).map(([k,v])=>option(k,v,false)));
  const results=h('div',{class:'research-results','aria-live':'polite'}),detail=h('div',{class:'research-detail'}),summary=h('p',{class:'caption'}),stats=h('div',{class:'stats'}),status=h('div');
  let offset=0,listToken=0,detailToken=0,first=true;
  const fetchJSON=async url=>{const r=await fetch(url,{signal:AbortSignal.timeout(15000)});if(!r.ok)throw Error('research unavailable');return r.json();};
  async function open(identifier){
    const token=++detailToken;detail.replaceChildren(note('טוען את תיק המחקר…'));
    try{
      const item=await fetchJSON('./api/research/'+encodeURIComponent(identifier));if(token!==detailToken)return;
      if(!item.company||!item.sections||!Array.isArray(item.sources))throw Error('invalid research');
      onSelect?.(item.company.tickers[0]);
      let current='business-overview';const content=h('div',{}),coverage=h('div',{class:'research-topics'});
      const draw=()=>{
        const evidence=new Set(item.research?.evidence_topics||[]);
        coverage.replaceChildren(...Object.entries(sections).map(([key,label])=>button(label+(evidence.has(key)?' · מקור':'') ,()=>{current=key;draw();},'research-topic '+(current===key?'active':''))));
        content.replaceChildren(h('h3',{},sections[current]),markdownView(item.sections[current],item.sources,ui));
      };
      draw();
      const progress=item.research||{};
      detail.replaceChildren(card(item.company.tickers.join(' / ')+' · '+item.company.company_name,h('div',{},
        h('p',{class:'caption'},(SECTORS[item.company.sector]||item.company.sector)+' · נתונים ל־'+date(item.updated_at)),
        note(STAGES[progress.stage]||'פרופיל עובדתי · המחקר המעמיק עדיין חסר'),
        h('p',{class:'caption'},'הנתונים הכספיים, קטעי המקור וטיוטות המחקר מוצגים בנפרד. איסוף אוטומטי אינו סקירה מאושרת.'),
        h('div',{class:'research-progress'},h('span',{},(progress.derived_observations||0)+' חישובים מבוססי דוחות'),h('span',{},(progress.evidence_topics?.length||0)+' תחומים עם קטעי מקור'),h('span',{},'איסוף מקורות מוצלח: '+date(progress.last_success_at))),
        item.curated_research?h('p',{},link('המחקר שנבדק בנפרד · '+date(item.curated_research.as_of)+' ↗',item.curated_research.url)):null,
        h('p',{},link('קובץ החברה ב־Brain ↗',item.markdown_url),' · ',link('ההיסטוריה הפיננסית המלאה ↗',item.full_history_url)),
        coverage,content,
        h('details',{},h('summary',{},'מקורות, תאריכים ושיטת הסיווג'),h('p',{class:'caption',dir:'auto'},item.classification?.reason||''),...item.sources.map(s=>h('p',{class:'caption',dir:'auto'},link(s.id+' · '+s.title+' ↗',s.url),' · פורסם: '+date(s.published_at)+' · נאסף: '+date(s.retrieved_at)))))));
      detail.scrollIntoView?.({behavior:'smooth',block:'start'});
    }catch{if(token===detailToken)detail.replaceChildren(note('תיק המחקר אינו זמין כרגע. אפשר לבחור שוב חברה מהרשימה.','amber'));}
  }
  async function load(){
    const token=++listToken;++detailToken;detail.replaceChildren();results.replaceChildren(note('טוען את ספריית החברות…'));
    try{
      const page=await fetchJSON('./api/research?q='+encodeURIComponent(query.value)+'&sector='+encodeURIComponent(sector.value||'')+'&stage='+encodeURIComponent(stage.value||'')+'&limit=25&offset='+offset);
      if(token!==listToken)return;
      if(!page.available||!Array.isArray(page.items))throw Error('research initializing');
      onCount?.(page.company_profiles+' חברות בספרייה');
      const counts=page.research_queue?.counts||{};
      stats.replaceChildren(...[['חברות בספרייה',page.company_profiles],['עם היסטוריה פיננסית',page.financial_profiles],['עם קטעי מקור שנאספו',(counts.evidence_collected||0)+(counts.draft||0)],['טיוטות מחקר',counts.draft||0]].map(([label,value])=>h('div',{class:'stat'},h('div',{class:'stat-label'},label),h('div',{class:'stat-value'},value))));
      status.replaceChildren(...[h('p',{class:'caption'},'עדכון הנתונים: '+date(page.source_created_at)+' · המחקר מתעדכן בהדרגה לאחר איסוף ובדיקת מקורות.'),
        page.research_queue?.stop_reason==='sec_access_blocked'?note('איסוף תוכן הדוחות נעצר בגלל חסימת גישה של SEC. הנתונים והמחקר הקודמים נשמרו; ניסיון נוסף מתוכנן בריצה היומית.','amber'):null].filter(Boolean));
      const selected=sector.value;
      sector.replaceChildren(option('','כל הסקטורים',!selected),...Object.entries(page.sector_counts||{}).map(([key,n])=>option(key,(SECTORS[key]||key)+' · '+n,key===selected)));
      summary.textContent=page.total+' חברות תואמות · '+(page.total?offset+1:0)+'–'+Math.min(offset+25,page.total)+' · מיון לפי סימול';
      results.replaceChildren(...page.items.map(row=>h('article',{class:'registry-row'},h('div',{},h('h3',{dir:'ltr'},row.tickers.join(' / ')),h('p',{dir:'auto'},row.company_name),h('p',{class:'caption'},(SECTORS[row.sector]||row.sector)+' · '+(STAGES[row.research?.stage]||STAGES.pending))),button('פתח מחקר ←',()=>open(row.cik),'primary'))));
      if(!page.items.length)results.append(note('לא נמצאו חברות במסנן הזה.'));
      previous.disabled=offset===0;next.disabled=offset+25>=page.total;
      if(first&&initialSymbol){first=false;await open(initialSymbol);}else first=false;
    }catch{if(token===listToken)results.replaceChildren(note('ספריית המחקר אינה זמינה כרגע. המחקר שנבדק זמין בלשוניות האחרות.','amber'));}
  }
  const previous=button('הקודם',()=>{offset=Math.max(0,offset-25);load();}),next=button('הבא',()=>{offset+=25;load();});
  const form=h('form',{class:'section-tools',onSubmit:e=>{e.preventDefault();offset=0;load();}},query,sector,stage,h('button',{type:'submit',class:'primary'},'חפש חברה'));
  sector.addEventListener('change',()=>{offset=0;load();});stage.addEventListener('change',()=>{offset=0;load();});
  load();
  return [card('ספריית המחקר · כל החברות',h('div',{},h('p',{},'מצא חברה לפי סימול, עבור בין הסקטורים ופתח את הנתונים, מקורות המחקר והשאלות שעוד צריך להשלים.'),stats,status,form,summary,results,h('div',{class:'section-tools'},previous,next))),detail];
}
