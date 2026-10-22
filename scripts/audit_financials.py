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
        companies.append({'ticker': history['ticker'], 'as_of': history['as_of'],
                          'retrieved_at': history['source'].get('retrieved_at'),
                          'periods': len(history['periods']), 'cells': dict(counts),
                          'model_usable_cells': sum(cell['model_usable'] for cells in history['financials'].values() for cell in cells.values()),
                          'open_flags': [f for f in history['qa_flags'] if f.get('status') == 'open']})
    return {'schema_version': 1, 'integrity': 'pass', 'research_approved': False,
            'checks': ['issuer identity', 'complete period/metric maps', 'status and finite values',
                       'exact-period reported numbers against provenance', 'derived arithmetic and inputs',
                       'split review bindings', 'source units/cutoffs', 'model eligibility gates'],
            'limitation': 'Checks internal source-linked consistency, not a new filing-level review or independent verification of raw source documents.',
            'open_flag_count': sum(len(c['open_flags']) for c in companies), 'companies': companies}


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
