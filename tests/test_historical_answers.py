import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import answering
import financial_answers
import financial_history
import query_contract
import stock_brain as kb


class HistoricalAnswerTests(unittest.TestCase):
    def test_exact_values_boundaries_and_refusals(self):
        cases = json.loads((kb.ROOT / 'tests/historical-answer-cases.json').read_text())
        for case in cases:
            with self.subTest(question=case['question']):
                result = answering.answer(case['question'])
                self.assertEqual(result['abstain'], case.get('abstain', False), result)
                answering.validate_answer(result, kb.ROOT)
                if result['abstain']:
                    self.assertEqual(result['statements'], [])
                    if case.get('reason'):
                        self.assertEqual(result['reason_code'], case['reason'])
                    continue
                self.assertEqual(result['mode'], 'financial_history')
                self.assertEqual(len(result['statements']), 1)
                row = result['statements'][0]
                self.assertEqual((row['ticker'], row['value'], row['period_start'], row['period_end']),
                                 (case['ticker'], case['value'], case['start'], case['end']))
                self.assertTrue(all(s['url'].startswith('https://www.sec.gov/Archives/') for s in result['sources']))
                self.assertIn('us-gaap:', row['citations'][0]['locator'])

    def test_history_answer_rejects_mutated_value_period_text_and_source(self):
        original = answering.answer('What was MSFT revenue in FY2024?')
        for mutate in [lambda o: o['statements'][0].update(value=1),
                       lambda o: o['statements'][0].update(period_start='2024-01-01'),
                       lambda o: o['statements'][0].update(text='Unverified claim'),
                       lambda o: o['sources'][0].update(url='https://example.com')]:
            output = copy.deepcopy(original)
            mutate(output)
            with self.assertRaises(ValueError):
                answering.validate_answer(output, kb.ROOT)

    def test_comparison_is_complete_or_empty(self):
        histories = {t: financial_answers.index(financial_history.load_history(kb.ROOT, t)) for t in ['MSFT', 'PLTR']}
        request = query_contract.parse('Compare MSFT and PLTR revenue in FY2024')
        rows, error = financial_answers.select(histories, request)
        self.assertIsNone(error)
        self.assertEqual({r['ticker'] for r in rows}, {'MSFT', 'PLTR'})
        histories['PLTR'] = []
        rows, error = financial_answers.select(histories, request)
        self.assertTrue(error)
        self.assertEqual(rows, [])

    def test_invalid_financial_history_is_not_exported(self):
        history = financial_history.load_history(kb.ROOT, 'MSFT')
        history['financials']['annual:2024-06-30']['revenue']['provenance'] = []
        with self.assertRaises(ValueError):
            financial_answers.index(history)


if __name__ == '__main__':
    unittest.main()
