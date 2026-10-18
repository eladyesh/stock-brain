from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import valuation

class ValuationTests(unittest.TestCase):
    def test_price_only_math(self):
        result = valuation.scenario(10, .1, 20, 3, 200)
        self.assertAlmostEqual(result['terminal_eps'], 13.31)
        self.assertAlmostEqual(result['terminal_price'], 266.2)
        self.assertAlmostEqual(result['annualized_price_change'], .1)

    def test_negative_or_invalid_earnings_are_not_given_a_multiple(self):
        for inputs in [(-1,.1,20,3,100), (0,.1,20,3,100), (1,-1,20,3,100), (1,.1,20,0,100), (1,.1,20,3,0), (float('nan'),.1,20,3,100)]:
            with self.assertRaises(ValueError): valuation.scenario(*inputs)

if __name__ == '__main__': unittest.main()
