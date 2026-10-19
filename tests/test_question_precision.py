"""Independent regression cases from observed failures and adversarial modifiers."""
import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import answering
import query_contract


class QuestionPrecisionTests(unittest.TestCase):
    def test_unsupported_questions_never_substitute_nearby_facts(self):
        questions = [
            'What was MSFT revenue excluding Azure in FY2026?',
            'מה שיעור הרווח הגולמי של אנבידיה?',
            'What is NVDA gross margin?',
            'What is MSFT operating margin?',
            'What is MSFT free cash flow?',
            'What was MSFT inflation-adjusted revenue in FY2026?',
            'What was MSFT revenue per employee in FY2026?',
            'What was MSFT Azure revenue in FY2026?',
            'Compare NVDA and AMD revenue in 2027',
            'Compare MSFT and ORCL revenue in Q1 FY2027',
            'What was NVDA annual revenue in FY2027?',
            'What was MSFT FY2026 adjusted EPS?',
            'Compare MSFT GAAP and adjusted EPS in FY2026',
            'What are MSFT net income and ROIC?',
            'What was MSFT revenue in Q1 and Q2 FY2026?',
        ]
        for question in questions:
            with self.subTest(question=question):
                out = answering.answer(question)
                self.assertTrue(out['abstain'])
                self.assertEqual(out['statements'], [])
                self.assertEqual(out['sources'], [])

    def test_exact_supported_periods_remain_available(self):
        for question, ticker in [
            ('What was MSFT FY2026 GAAP revenue and net income?', 'MSFT'),
            ('What was ORCL GAAP revenue in FY2027 Q1?', 'ORCL'),
            ('Give MU fiscal Q4 2026 revenue and gross margin.', 'MU'),
            ('Was AVAV profitable on a GAAP basis in fiscal Q1 2027 despite positive adjusted EBITDA?', 'AVAV'),
            ('What was NVDA revenue in Q2 FY2027?', 'NVDA'),
            ('מה ההכנסות של מיקרוסופט?', 'MSFT'),
            ('What was MSFT revenue in Q1 FY2026?', 'MSFT'),
            ('מה היו הכנסות מיקרוסופט ברבעון הראשון של 2026?', 'MSFT'),
            ('What was MU revenue in fiscal Q1 2026?', 'MU'),
            ('What was MSFT revenue in FY2024?', 'MSFT'),
        ]:
            with self.subTest(question=question):
                out = answering.answer(question)
                self.assertFalse(out['abstain'], out)
                self.assertEqual({s['ticker'] for s in out['statements']}, {ticker})
                answering.validate_answer(out, Path(__file__).resolve().parents[1])

    def test_comparison_returns_both_companies_or_abstains(self):
        for question in ['Compare MSFT and ORCL business models', 'Compare AMD and NVDA risks']:
            out = answering.answer(question)
            self.assertFalse(out['abstain'])
            self.assertEqual(len({s['ticker'] for s in out['statements']}), 2)

    def test_fiscal_and_calendar_years_are_not_interchangeable(self):
        self.assertFalse(answering.answer('What was NVDA revenue in Q2 FY2027?')['abstain'])
        self.assertTrue(answering.answer('What was NVDA revenue in Q2 2027?')['abstain'])

    def test_quarter_numbers_are_not_calendar_month_inferences(self):
        metric = {'period_start': '2026-04-27', 'period_end': '2026-07-26', 'name': 'Revenue', 'locator': 'Three months ended July 26'}
        identity = query_contract.period_identity(metric, {'text': 'Reported revenue for the three months ended July 26, 2026.'})
        self.assertIsNone(identity['quarter'])


if __name__ == '__main__':
    unittest.main()
