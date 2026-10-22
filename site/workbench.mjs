// Personal state stays in this browser. It never changes reviewed research.
const KEY = 'stock-brain-workbench-v1';
export function personalStore(storage) {
  if (storage === undefined) { try { storage = globalThis.localStorage; } catch { storage = null; } }
  let state = {version: 1, notes: {}, scenarios: {}, visit: null};
  try {
    const saved = JSON.parse(storage?.getItem(KEY) || 'null');
    if (saved?.version === 1 && saved.notes && saved.scenarios) state = saved;
  } catch { /* A corrupt or unavailable browser store must not block research. */ }
  const previousVisit = state.visit;
  const persist = () => { try { if (!storage) return false; storage.setItem(KEY, JSON.stringify(state)); return true; } catch { return false; } };
  return {
    previousVisit,
    note: ticker => typeof state.notes[ticker]?.text === 'string' ? state.notes[ticker] : null,
    saveNote(ticker, text) { state.notes[ticker] = {text: String(text).slice(0, 12000), saved_at: new Date().toISOString()}; return persist(); },
    scenario: ticker => state.scenarios[ticker] || null,
    saveScenario(ticker, modelDate, overrides) { state.scenarios[ticker] = {model_as_of: modelDate, overrides, saved_at: new Date().toISOString()}; return persist(); },
    markVisit(data) { state.visit = visitSnapshot(data); return persist(); },
  };
}
export function visitSnapshot(data) {
  return {at: new Date().toISOString(), companies: Object.fromEntries(data.companies.map(c => [c.ticker, {research: c.as_of, thesis: c.thesis?.as_of || null}])),
    events: (data.queue || []).map(e => e.id)};
}
export function changesSinceVisit(data, previous) {
  if (!previous?.companies || !Array.isArray(previous.events)) return {first: true, companies: [], events: []};
  const known = new Set(previous.events);
  return {first: false, since: previous.at,
    companies: data.companies.filter(c => previous.companies[c.ticker]?.research !== c.as_of || previous.companies[c.ticker]?.thesis !== (c.thesis?.as_of || null)).map(c => c.ticker),
    events: (data.queue || []).filter(e => !known.has(e.id))};
}
// Presentation groups only: every document retains its own review obligation.
export function groupQueue(entries, events = []) {
  const full = new Map(events.map(e => [e.id, e]));
  const rows = entries.map(e => ({...full.get(e.event_id), ...e}));
  const anchors = new Map();
  for (const e of rows) {
    const title = e.title || '';
    if (e.kind === 'sec_filing' || !/(?:reports|announces).*(?:results|earnings)/i.test(title)) continue;
    const quarter = title.match(/\bQ([1-4])\s+(20\d{2})\b/i);
    if (quarter) anchors.set(e.ticker + ':' + String(e.published_at).slice(0, 10), {id: e.event_id, title, quarter: +quarter[1], year: +quarter[2]});
  }
  const grouped = new Map();
  for (const e of rows) {
    const key = e.ticker + ':' + String(e.published_at).slice(0, 10), anchor = anchors.get(key);
    const form = e.form || '';
    const earnings8k = form === '8-K' && /(?:^|[,\s;])2\.02(?:$|[,\s;])/.test(String(e.items || ''));
    const filenameDate = (e.url || '').match(/-(20\d{2})(\d{2})(\d{2})\.htm(?:l)?(?:$|\?)/);
    const date = e.report_date || e.reportDate || (filenameDate ? filenameDate.slice(1).join('-') : '');
    const quarter10q = form === '10-Q' && anchor && date.startsWith(String(anchor.year)) && Math.ceil(Number(date.slice(5, 7)) / 3) === anchor.quarter;
    const groupKey = anchor && (e.event_id === anchor.id || earnings8k || quarter10q) ? 'earnings:' + key : 'document:' + e.event_id;
    if (!grouped.has(groupKey)) grouped.set(groupKey, {id: groupKey, title: groupKey.startsWith('earnings:') ? anchor.title : e.title, ticker: e.ticker, published_at: e.published_at, entries: []});
    grouped.get(groupKey).entries.push(e);
  }
  return [...grouped.values()].map(g => ({...g, priority: g.entries.map(e => e.priority).sort()[0], pending: g.entries.filter(e => e.queue_status === 'pending_review').length})).sort((a,b) => a.priority.localeCompare(b.priority) || String(b.published_at).localeCompare(String(a.published_at)));
}
