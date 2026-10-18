import copy
from datetime import datetime, timezone
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import market_data

class MarketDataTests(unittest.TestCase):
    def payload(self):
        return {'chart': {'result': [{'meta': {'symbol': 'MSFT', 'currency': 'USD', 'regularMarketPrice': 123.5, 'regularMarketTime': 1792180800, 'exchangeName': 'NMS'}}]}}

    def test_trade_time_and_provider_are_preserved(self):
        row = market_data.parse_quote(self.payload(), 'MSFT', '2026-10-18T12:00:00+00:00')
        self.assertEqual(row['trade_at'], '2026-10-16T20:00:00+00:00')
        self.assertEqual(row['status'], 'available')
        self.assertEqual(row['provider'], 'Yahoo Finance')

    def test_invalid_or_mismatched_quotes_are_rejected(self):
        for field, value in [('symbol', 'AAPL'), ('currency', 'EUR'), ('regularMarketPrice', -2), ('regularMarketPrice', float('nan')), ('regularMarketTime', None)]:
            row = self.payload(); row['chart']['result'][0]['meta'][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                market_data.parse_quote(row, 'MSFT', '2026-10-18T12:00:00+00:00')

    def test_old_quotes_remain_explicitly_stale(self):
        row = market_data.parse_quote(self.payload(), 'MSFT', '2026-10-24T12:00:00+00:00')
        self.assertEqual(row['status'], 'stale')

    def test_splits_have_dates_and_factors(self):
        payload = self.payload()
        payload['chart']['result'][0]['events'] = {'splits': {'one': {'date': 1780000000, 'numerator': 10, 'denominator': 1}}}
        row = market_data.parse_quote(payload, 'MSFT', '2026-10-18T12:00:00+00:00')
        self.assertEqual(row['split_events'][0]['numerator'], 10)
        self.assertIn('effective_at', row['split_events'][0])

if __name__ == '__main__': unittest.main()
