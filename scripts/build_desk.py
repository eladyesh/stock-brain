"""Build a portable, dated research desk from checked research and separate data layers."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil

import answering
import financial_history
import research_pipeline as p
import stock_brain as kb
import valuation
import query_contract


def build(root, output=None):
    kb.export_records(root)  # Reject stale review bindings before publishing any narrative.
    config = p.read_json(root / 'config/query_language.json')
    sections = p.read_json(root / 'config/sections.json')
    reports = [p.read_json(path) for path in [root / 'build/monitoring/latest.json', root / 'research/monitoring/latest.json'] if path.exists()]
    monitor = max(reports, key=lambda r: r.get('checked_at', ''), default=None)
    result = {'schema_version': 1, 'built_at': datetime.now(timezone.utc).isoformat(),
              'repository': 'https://github.com/eladyesh/stock-brain',
              'config': config, 'section_definitions': sections, 'companies': [],
              'metric_patterns': list(query_contract.METRICS.items()), 'he_reasons': answering.HE_REASONS,
              'queue': (monitor or {}).get('queue', []), 'scan_at': (monitor or {}).get('checked_at'),
              'source_health': (monitor or {}).get('companies', {}),
              'limits': ['Research approvals are AI reviews, not independent human sign-off.',
                         'SEC normalization and market snapshots are separate from reviewed narrative research.',
                         'Scenario outputs are sensitivity calculations from explicit assumptions, not forecasts.']}
    for company in p.universe(root):
        ticker = company['ticker']
        packet = p.read_json(p.managed_packet_path(root, ticker))
        history_path = root / 'research/financials' / (ticker + '.json')
        quote_path = root / 'research/market' / (ticker + '.json')
        history = financial_history.load_history(root, ticker) if history_path.exists() else None
        claims = {}
        for section, data in packet['sections'].items():
            claims[section] = [{**c, 'text_he': answering.translated_claim(root, packet, c)} for c in data.get('claims', [])]
        locale = p.read_json(root / 'research/locales/he' / (ticker + '.json'))
        gaps = []
        for index, gap in enumerate(packet['gaps']):
            candidate = locale.get('gaps', [])[index] if index < len(locale.get('gaps', [])) else {}
            text = candidate.get('text') if candidate.get('source_sha256') == p.digest(gap) and candidate.get('translated_text_sha256') == p.digest(candidate.get('text', '')) else None
            gaps.append({'en': gap, 'he': text})
        metric_index = []
        period_context = query_contract.period_context(packet)
        claim_map = {c['id']: (section, c) for section, values in packet['sections'].items() for c in values.get('claims', [])}
        for metric in packet.get('metrics', []):
            section, claim = claim_map[metric['claim_id']]
            metric_index.append({**metric, 'metric_keys': [key for key in query_contract.METRICS if query_contract.metric_matches(metric, key)],
                                 'identity': query_contract.period_identity(metric, claim, period_context), 'section_id': section, 'claim_kind': claim['kind']})
        item = {'ticker': ticker, 'name': company['company_name'], 'sector': company['sector'],
                'as_of': packet['as_of'], 'sections': claims, 'sources': packet['sources'], 'metrics': packet.get('metrics', []), 'metric_index': metric_index,
                'gaps': gaps, 'freshness': answering.disclosure_monitor.freshness(root, ticker, monitor),
                'quote': p.read_json(quote_path) if quote_path.exists() else None,
                'history': history, 'ratios': valuation.historical_ratios(history) if history else []}
        result['companies'].append(item)
    triage_path = root / 'research/monitoring/triage.json'
    if triage_path.exists(): result['triage'] = p.read_json(triage_path)
    for key, path in [('refresh_status', root / 'research/monitoring/refresh-status.json'), ('market_status', root / 'research/market/status.json')]:
        if path.exists(): result[key] = p.read_json(path)
    target = output or root / 'data/desk.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--dist', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    result = build(root, args.output)
    if args.dist:
        args.dist.mkdir(parents=True, exist_ok=True)
        for path in (root / 'site').iterdir():
            if path.is_file(): shutil.copyfile(path, args.dist / path.name)
        (args.dist / 'snapshot.json').write_text(json.dumps(result, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    print(json.dumps({'companies': len(result['companies']), 'built_at': result['built_at'], 'output': str(args.output or root/'data/desk.json')}))

if __name__ == '__main__': main()
