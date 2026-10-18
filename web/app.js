'use strict';
const el = (tag, text, parent, cls) => { const n = document.createElement(tag); if(text != null) n.textContent = text; if(cls) n.className = cls; if(parent) parent.append(n); return n; };
const labels = {reported:'דיווח החברה',management_guidance:'תחזית הנהלה',interpretation:'פרשנות מחקרית',derived:'חישוב',unknown:'טרם נסרק',checked:'הסריקה הושלמה',stale_check:'נדרשת סריקה',needs_review:'ממתין לבדיקה',error:'שגיאת סריקה',partial:'כיסוי מקורות חלקי'};
function link(parent, title, url) { const n = el('a', title, parent); if (/^https:\/\//i.test(url)) { n.href=url; n.target='_blank'; n.rel='noopener noreferrer'; } return n; }
function render(data) {
 const box=document.querySelector('#answer'); box.replaceChildren();
 if(data.abstain) { el('p',data.reason,box,'notice'); return; }
 el('h2','הראיות שנמצאו',box);
 for(const company of data.coverage) {
  const card=el('article',null,box,'card'); el('h3',`${company.ticker} · מחקר ל־${company.as_of}`,card);
  el('p',`${labels[company.freshness.status] || company.freshness.status}${company.freshness.checked_at ? ' · '+company.freshness.checked_at.slice(0,16).replace('T',' ')+' UTC' : ''}`,card,'freshness');
  for(const row of data.statements.filter(s=>s.ticker===company.ticker)) {
   const p=el('p',null,card); el('span',labels[row.kind] || row.kind,p,'badge'); el('span',' '+row.text,p);
   const refs=el('small',null,card);
   for(const citation of row.citations) { const source=data.sources.find(s=>s.id===citation.id); link(refs,`[${citation.id}] ${citation.locator} `,source.url); }
  }
 }
 const sources=el('details',null,box); el('summary','מקורות ותאריכים',sources);
 for(const s of data.sources) {const p=el('p',null,sources);link(p,s.title,s.url);el('small',` · פורסם: ${s.published_at || 'לא ידוע'} · נבדק: ${s.accessed_at}`,p);}
 const gaps=el('details',null,box);el('summary','פערים ומגבלות במחקר',gaps);
 for(const gap of data.limitations) el('p',`${gap.ticker}: ${gap.text}`,gaps);
 el('small',`זמן תשובה: ${data.metrics.elapsed_seconds} שניות · קריאות למודל: ${data.metrics.model_api_calls}`,box);
}
document.querySelector('#ask').addEventListener('submit',async e=>{
 e.preventDefault();const button=document.querySelector('#submit');button.disabled=true;document.querySelector('#answer').textContent='בודק את הראיות…';
 try {const r=await fetch('/api/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question:document.querySelector('#question').value})});const data=await r.json();if(!r.ok)throw Error(data.error);render(data);}catch(e){document.querySelector('#answer').textContent='לא ניתן להשלים את הבדיקה: '+e.message;}finally{button.disabled=false;}
});
for(const button of document.querySelectorAll('[data-question]'))button.addEventListener('click',()=>{document.querySelector('#question').value=button.dataset.question;document.querySelector('#ask').requestSubmit();});
fetch('/api/status').then(r=>r.ok?r.json():Promise.reject(Error('status'))).then(data=>{
 for(const c of data.companies)el('span',`${c.ticker} · ${labels[c.freshness.status] || c.freshness.status}`,document.querySelector('#companies'),'company');
 document.querySelector('#queue-label').textContent=`${data.queue.length} עדכונים ממתינים לבדיקה`;
 for(const e of data.queue){const li=el('li',null,document.querySelector('#queue'));link(li,`${e.ticker}: ${e.title}`,e.url);el('small',' · '+(e.published_at || 'תאריך לא ידוע'),li);}
}).catch(()=>{document.querySelector('#companies').textContent='מצב הסריקה אינו זמין.';});
