"""Dated, reproducible research observations from validated financial cells.

These are calculations, not a reviewed investment thesis. Missing/negative
denominators and non-comparable definitions produce gaps, never invented ratios.
"""
from datetime import date
import math
import ttm


def analyze(history):
    if not history:
        return {'observations': [], 'gaps': ['Validated financial history is missing.']}
    observations, gaps = [], []
    annual = sorted((p for p in history['periods'] if p['type'] == 'annual'), key=lambda p: p['end'], reverse=True)
    if not annual:
        return {'observations': [], 'gaps': ['No annual period is available for comparison.']}
    latest = annual[0]

    def cell(period, metric):
        value = history['financials'][period['id']].get(metric, {})
        if (period.get('flags') or value.get('model_usable') is not True or value.get('conflicts')
                or value.get('comparison_status') != 'comparable'
                or ttm.BLOCKING_FLAGS.intersection(value.get('flags', []))
                or type(value.get('value')) not in (int, float) or not math.isfinite(value['value'])
                or value.get('basis') != 'US GAAP' or value.get('unit') != 'USD'
                or not value.get('definition_tag') or not value.get('provenance')):
            return None
        return value

    def add(key, section, description, value, unit, formula, inputs, periods):
        if not math.isfinite(value):
            return
        observations.append({'id': key, 'kind': 'derived', 'section': section, 'text': description,
            'value': round(value, 6), 'unit': unit, 'formula': formula,
            'periods': [{k: p[k] for k in ('type', 'start', 'end')} for p in periods],
            'inputs': [{'metric': metric, 'value': c['value'], 'unit': c['unit'], 'basis': c['basis'],
                        'definition_tag': c['definition_tag']} for metric, c in inputs],
            'source_urls': sorted({p['url'] for _, c in inputs for p in c['provenance']}),
            'evidence_cutoff': history['as_of']})

    revenue = cell(latest, 'revenue')
    for name, metric in [('Operating margin', 'operating_income'), ('Net margin', 'net_income'),
                         ('Free cash flow margin', 'free_cash_flow'), ('Stock compensation / revenue', 'stock_based_compensation')]:
        numerator = cell(latest, metric)
        if revenue and numerator and revenue['value'] > 0:
            result = numerator['value'] / revenue['value'] * 100
            add(metric + '_to_revenue', 'financial-performance',
                f"{name} was {result:.2f}% for {latest['start']} to {latest['end']} (US GAAP inputs).",
                result, '%', metric + ' / revenue * 100', [(metric, numerator), ('revenue', revenue)], [latest])
        else:
            gaps.append(name + ': compatible positive revenue and usable inputs are required.')
    previous = annual[1] if len(annual) > 1 else None
    duration = lambda p: (date.fromisoformat(p['end']) - date.fromisoformat(p['start'])).days + 1
    comparable_periods = (previous and 330 <= duration(latest) <= 400 and 330 <= duration(previous) <= 400
                          and abs(duration(latest) - duration(previous)) <= 7
                          and 350 <= (date.fromisoformat(latest['end']) - date.fromisoformat(previous['end'])).days <= 380
                          and (date.fromisoformat(latest['start']) - date.fromisoformat(previous['end'])).days == 1)
    for metric in ('revenue', 'operating_income', 'net_income', 'operating_cash_flow', 'free_cash_flow'):
        current, prior = cell(latest, metric), cell(previous, metric) if comparable_periods else None
        if (current and prior and prior['value'] > 0 and current['definition_tag'] == prior['definition_tag']
                and current.get('normalization') == prior.get('normalization')):
            result = (current['value'] / prior['value'] - 1) * 100
            add(metric + '_annual_growth', 'financial-performance',
                f"Annual {metric.replace('_', ' ')} changed {result:+.2f}% from the year ended {previous['end']} to {latest['end']}.",
                result, '%', '(current / prior - 1) * 100', [(metric, current), (metric, prior)], [latest, previous])
        else:
            gaps.append(metric + ': annual growth withheld because periods, definitions or a positive prior denominator are not verified.')
    net, cash = cell(latest, 'net_income'), cell(latest, 'operating_cash_flow')
    if net and cash and net['value'] > 0:
        result = cash['value'] / net['value']
        add('cash_conversion', 'financial-performance',
            f"Operating cash flow / net income was {result:.2f}x for the year ended {latest['end']}. Working capital and non-cash adjustments require separate filing analysis.",
            result, 'x', 'operating_cash_flow / net_income', [('operating_cash_flow', cash), ('net_income', net)], [latest])
    return {'observations': observations, 'gaps': gaps}
