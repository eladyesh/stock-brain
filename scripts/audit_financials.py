"""Reproducible integrity audit; passing does not approve open financial QA."""
import argparse
from collections import Counter
import json
from pathlib import Path

import financial_history as financials
import research_pipeline as p
import stock_brain as kb


def audit(histories):
    companies = []
    for history in histories:
        financials.validate_history(history)
        counts = Counter(cell['status'] for cells in history['financials'].values() for cell in cells.values())
        gates = Counter(flag for cells in history['financials'].values() for cell in cells.values() for flag in cell['flags']
                        if flag in {'share_split_and_corporate_action_basis_unverified', 'debt_scope_requires_filing_review',
                                    'definition_changed_across_series', 'revision_requires_review'})
        latest_inputs = {}
        for metric in ('revenue', 'net_income', 'eps_diluted', 'shares_diluted', 'shares_outstanding', 'free_cash_flow', 'debt_total'):
            cell = financials.get_metric(history, metric)
            if cell:
                latest_inputs[metric] = {'period_end': cell['period']['end'], 'value': cell['value'], 'unit': cell['unit'],
                                         'model_usable': cell['model_usable'], 'flags': cell['flags'],
                                         'reviewed_scope': cell.get('scope_review', {}).get('scope'),
                                         'review_id': cell.get('scope_review', cell.get('share_basis', {})).get('review_id')}
        companies.append({'ticker': history['ticker'], 'as_of': history['as_of'],
                          'retrieved_at': history['source'].get('retrieved_at'),
                          'periods': len(history['periods']), 'cells': dict(counts),
                          'model_usable_cells': sum(cell['model_usable'] for cells in history['financials'].values() for cell in cells.values()),
                          'filing_scope_verified_cells': sum(bool(cell.get('scope_review')) for cells in history['financials'].values() for cell in cells.values()),
                          'open_cell_gates': dict(gates), 'latest_annual_model_inputs': latest_inputs,
                          'open_flags': [f for f in history['qa_flags'] if f.get('status') == 'open']})
    return {'schema_version': 1, 'integrity': 'pass', 'research_approved': False,
            'checks': ['issuer identity', 'complete period/metric maps', 'status and finite values',
                       'exact-period reported numbers against provenance', 'derived arithmetic and inputs',
                       'split and filing-scope review bindings', 'source units/cutoffs', 'model eligibility gates'],
            'limitation': 'Checks internal source-linked consistency, not a new filing-level review or independent verification of raw source documents.',
            'open_flag_count': sum(len(c['open_flags']) for c in companies),
            'open_flags_by_code': dict(Counter(f['code'] for c in companies for f in c['open_flags'])),
            'model_usable_cells': sum(c['model_usable_cells'] for c in companies),
            'filing_scope_verified_cells': sum(c['filing_scope_verified_cells'] for c in companies),
            'companies': companies}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    histories = ([c['history'] for c in p.read_json(args.state)['files']['desk.json']['companies']]
                 if args.state else [financials.load_history(kb.ROOT, c['ticker']) for c in p.universe(kb.ROOT)])
    report = audit(histories)
    p.write_json(args.output, report)
    print(json.dumps({'integrity': report['integrity'], 'open_flags': report['open_flag_count'], 'output': str(args.output)}))
