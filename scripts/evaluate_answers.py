#!/usr/bin/env python3
"""Check answer evidence coverage and fidelity separately from retrieval recall.

This is a reproducible acceptance test, not independent semantic fact-checking.
"""
import argparse
import hashlib
import json
from pathlib import Path
import statistics
import time

import answering
import evaluate_retrieval
import research_pipeline as pipeline
import stock_brain as kb


def evaluate(root, cases_path):
    cases = pipeline.read_json(cases_path)['cases']
    records = kb.export_records(root)
    evaluate_retrieval.validate_cases(cases, records)
    by_section = {(r['ticker'], r['section_id']): r for r in records if r.get('ticker')}
    results, latency = [], []
    for case in cases:
        started = time.monotonic()
        output = answering.answer(case['question'], root)
        latency.append(time.monotonic() - started)
        answering.validate_answer(output, root)
        covered = []
        for expected in case.get('evidence', []):
            covered.append(any(by_section[(s['ticker'], s['section_id'])]['document_id'] == expected['document_id']
                               and s['section_id'] == expected['section_id']
                               and set(expected['source_ids']) <= {r['id'].split(':', 1)[1] for r in s['citations']}
                               for s in output['statements']))
        passed = output['abstain'] if case['expected_behavior'] == 'abstain' else bool(covered) and all(covered) and not output['abstain']
        results.append({'id': case['id'], 'expected_behavior': case['expected_behavior'], 'passed': passed,
                        'abstain': output['abstain'], 'reason_code': output['reason_code'],
                        'claims': [s['ticker'] + ':' + s['claim_id'] for s in output['statements']],
                        'evidence_and_translation_integrity': True})
    positive = [r for r in results if r['expected_behavior'] == 'answer']
    negative = [r for r in results if r['expected_behavior'] == 'abstain']
    return {'cases': len(cases), 'cases_sha256': hashlib.sha256(cases_path.read_bytes()).hexdigest(),
            'answer_evidence_pass_rate': sum(r['passed'] for r in positive) / len(positive) if positive else None,
            'abstention_pass_rate': sum(r['passed'] for r in negative) / len(negative) if negative else None,
            'median_latency_seconds': round(statistics.median(latency), 4), 'model_api_calls': 0, 'model_cost_usd': 0,
            'research_review_cost_usd': None,
            'scope': 'Exact claim, translation-version, basis, date and citation fidelity; required evidence coverage. Not an independent assessment of factual truth or general language understanding.',
            'results': results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cases', type=Path, default=Path('eval/acceptance-v1.json'))
    parser.add_argument('--output', type=Path, default=Path('build/answers-evaluation.json'))
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    result = evaluate(root, args.cases if args.cases.is_absolute() else root / args.cases)
    pipeline.write_json(args.output if args.output.is_absolute() else root / args.output, result)
    print(json.dumps({k: v for k, v in result.items() if k != 'results'}, indent=2))
    return 0 if all(r['passed'] for r in result['results']) else 2


if __name__ == '__main__':
    raise SystemExit(main())
