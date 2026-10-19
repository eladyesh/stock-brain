"""Exact, cited historical lookup; separate from editorially reviewed claims.

Only explicit periods and model-usable GAAP cells are eligible. The same
deterministic bilingual records are exported for the browser; no LLM or
calendarization, rolling-period calculation, or missing-to-zero fill is used.
"""
import hashlib
import json

import financial_history
import query_contract

METRICS = {
    'revenue': ('revenue', 'Revenue', 'הכנסות'),
    'gross_profit': ('gross_profit', 'Gross profit', 'רווח גולמי'),
    'operating_income': ('operating_income', 'Operating income', 'רווח תפעולי'),
    'net_income': ('net_income', 'Net income attributable to parent', 'רווח נקי מיוחס לחברה האם'),
    'eps': ('eps_diluted', 'Reported diluted EPS', 'רווח מדולל מדווח למניה'),
    'operating_cash_flow': ('operating_cash_flow', 'Operating cash flow', 'תזרים מפעילות שוטפת'),
    'capex': ('capex', 'Cash PP&E purchases (outflow negative)', 'רכישת רכוש קבוע במזומן (יציאה שלילית)'),
    'free_cash_flow': ('free_cash_flow', 'OCF less cash PP&E purchases', 'תזרים שוטף פחות רכישת רכוש קבוע'),
    'sbc': ('stock_based_compensation', 'Stock-based compensation', 'תגמול מבוסס מניות'),
    'cash': ('cash_and_equivalents', 'Cash and cash equivalents', 'מזומנים ושווי מזומנים'),
    'debt': ('debt_total', 'Total debt (defined scope)', 'חוב כולל לפי ההגדרה במקור'),
}


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def index(history):
    """Return inspectable source records; quality gates stay in the selector."""
    if not history:
        return []
    financial_history.validate_history(history)
    rows = []
    for period in history['periods']:
        for key, (metric, english, hebrew) in METRICS.items():
            cell = history['financials'][period['id']][metric]
            if cell['value'] is None:
                continue
            ticker = history['ticker']
            sources = []
            for source in cell['provenance']:
                locator = (source['taxonomy'] + ':' + source['tag'] + '; ' +
                           (source['start'] + ' – ' if source['start'] else 'as of ') + source['end'] +
                           '; ' + source['unit'] + '; filed ' + source['filed'])
                sources.append({'id': source['source_id'], 'ticker': ticker,
                                'title': ticker + ' ' + source['form'] + ' (' + source['filed'] + ')',
                                'publisher': ticker + ' / SEC EDGAR', 'url': source['url'],
                                'published_at': source['filed'],
                                'accessed_at': history['source']['retrieved_at'][:10], 'locator': locator})
            identifier = 'H:' + period['id'] + ':' + metric
            amount = format(cell['value'], ',.6f').rstrip('0').rstrip('.')
            unit_he = {'USD': 'דולר', 'USD/shares': 'דולר למניה', 'shares': 'מניות'}[cell['unit']]
            duration = period['start'] + ' – ' + period['end']
            instant = metric in financial_history.INSTANT
            period_label = ('as of ' + period['end']) if instant else duration
            kind = 'derived' if cell['status'] == 'derived' else 'reported'
            rows.append({'id': identifier, 'claim_id': identifier, 'ticker': ticker,
                         'section': 'financial-history', 'section_id': 'financial-history',
                         'metric_keys': [key], 'metric': metric, 'value': cell['value'], 'unit': cell['unit'],
                         'basis': 'GAAP', 'kind': kind, 'claim_kind': kind,
                         'identity': {'type': period['type'], 'year': period['fiscal_year'], 'quarter': period['fiscal_quarter']},
                         'period_start': period['start'], 'period_end': period['end'],
                         'period_label': period['label'], 'model_usable': cell['model_usable'],
                         'flags': cell['flags'], 'as_of': history['as_of'], 'sources': sources,
                         'source_sha256': digest({'cell': cell, 'period': period, 'snapshot': history['source']}),
                         'text': f"{ticker} — {period['label']} ({period_label}): {english}: {amount} {cell['unit']}. US GAAP; {kind}. Data snapshot: {history['as_of']}.",
                         'text_he': f"{ticker} — {period['label']} ({'ליום ' + period['end'] if instant else duration}): {hebrew}: {amount} {unit_he}. US GAAP · {'חישוב מנתונים מדווחים' if kind == 'derived' else 'נתון מדווח'}. תמונת נתונים ל־{history['as_of']}."})
    return rows


def eligible(request):
    return bool(request['metrics'] and len(request['years']) == 1 and len(request['quarters']) <= 1
                and not request.get('period_error') and not request['qualifier_error']
                and not request['guidance'] and request['basis'] != 'non-GAAP' and not request['both_bases'])


def select(indexes, request):
    """Require every metric for every issuer; never return a partial comparison."""
    if not eligible(request) or not indexes:
        return [], 'unsupported_period'
    selected = []
    for rows in indexes.values():
        for key in request['metrics']:
            matches = [row for row in rows if key in row['metric_keys'] and query_contract.match_identity(
                row['identity'], row['period_start'], row['period_end'], request)]
            if len(matches) != 1:
                return [], 'unsupported_period' if key in METRICS else 'unsupported_metric'
            if any(not row['model_usable'] for row in matches):
                return [], 'data_quality_unverified'
            selected.extend(matches)
    return list({(r['ticker'], r['id']): r for r in selected}.values()), None


def lookup(root, question, tickers, language):
    rows, error = select({t: index(financial_history.load_history(root, t)) for t in tickers}, query_contract.parse(question))
    if error:
        return [], [], error
    statements, sources = [], {}
    for row in rows:
        citations = []
        for source in row['sources']:
            identifier = row['ticker'] + ':' + source['id']
            citations.append({'id': identifier, 'locator': source['locator']})
            sources[identifier] = {k: v for k, v in source.items() if k != 'locator'} | {'id': identifier}
        statements.append({k: row[k] for k in ['ticker', 'claim_id', 'section_id', 'kind', 'as_of', 'source_sha256',
                                               'metric', 'value', 'unit', 'period_start', 'period_end', 'period_label']} |
                          {'text': row['text_he'] if language == 'he' else row['text'], 'original_text': row['text'],
                           'citations': citations})
    return statements, list(sources.values()), None
