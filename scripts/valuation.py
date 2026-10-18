"""Explicit sensitivity calculations, not forecasts, consensus or price targets."""
import math


def scenario(eps, annual_growth, exit_pe, years, reference_price):
    for value in [eps, annual_growth, exit_pe, years, reference_price]:
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError('All scenario inputs must be finite numbers.')
    if not (eps > 0 and -1 < annual_growth <= 3 and 0 < exit_pe <= 200 and 1 <= years <= 10 and reference_price > 0):
        raise ValueError('Positive EPS and price, growth above -100%, P/E 0–200 and 1–10 years are required.')
    terminal_eps = eps * (1 + annual_growth) ** years
    terminal_price = terminal_eps * exit_pe
    return {'terminal_eps': terminal_eps, 'terminal_price': terminal_price,
            'price_change': terminal_price/reference_price-1,
            'annualized_price_change': (terminal_price/reference_price)**(1/years)-1,
            'formula': 'EPS * (1 + assumed EPS growth)^years * assumed exit P/E',
            'basis': 'Illustrative user assumptions; price-only result excludes dividends, taxes, fees and FX.'}


def historical_ratios(history):
    import financial_history as f
    result = []
    for period in history['periods']:
        revenue = f.get_metric(history, 'revenue', period['type'], period['end'], period_start=period['start'])
        row = {'period': period, 'ratios': {}}
        for key, label in [('net_income', 'net_margin'), ('operating_income', 'operating_margin'), ('gross_profit', 'gross_margin'), ('free_cash_flow', 'fcf_margin'), ('stock_based_compensation', 'sbc_to_revenue')]:
            cell = f.get_metric(history, key, period['type'], period['end'], period_start=period['start'])
            if cell and revenue and cell.get('model_usable') and revenue.get('model_usable') and revenue.get('value', 0) > 0:
                row['ratios'][label] = {'value': cell['value']/revenue['value'], 'basis': 'derived_calculation',
                                      'formula': key + ' / revenue', 'source_metric': key,
                                      'source_urls': sorted({p['url'] for c in [cell, revenue] for p in c.get('provenance', []) if p.get('url')})}
        result.append(row)
    return result
