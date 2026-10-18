"""Dated public market snapshots; optional adapter, no keys or paid requests.

Yahoo's chart endpoint is not an exchange SLA. Keep provider and trade timestamps,
retain old snapshots on errors, and never describe this as a live trading feed.
"""
import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import urllib.parse

import research_pipeline as p
import stock_brain as kb


def parse_quote(payload, ticker, retrieved_at=None):
    result = payload.get('chart', {}).get('result')
    kb.need(result and len(result) == 1, 'quote source returned no unique result')
    row = result[0]
    meta = row['meta']
    kb.need(meta.get('symbol', '').upper() == ticker.upper(), 'quote issuer mismatch')
    kb.need(meta.get('currency') == 'USD', 'only USD common-stock quotes are supported')
    price, stamp = meta.get('regularMarketPrice'), meta.get('regularMarketTime')
    kb.need(isinstance(price, (int, float)) and not isinstance(price, bool) and math.isfinite(price) and price > 0, 'invalid quote price')
    kb.need(isinstance(stamp, (int, float)) and stamp > 0, 'missing trade timestamp')
    now = datetime.fromisoformat(retrieved_at) if retrieved_at else datetime.now(timezone.utc)
    trade = datetime.fromtimestamp(stamp, timezone.utc)
    kb.need((trade-now).total_seconds() <= 300, 'future trade timestamp')
    splits = []
    for event in row.get('events', {}).get('splits', {}).values():
        numerator, denominator = event.get('numerator'), event.get('denominator')
        kb.need(isinstance(numerator, (int, float)) and isinstance(denominator, (int, float)) and numerator > 0 and denominator > 0, 'invalid split factor')
        splits.append({'effective_at': datetime.fromtimestamp(event['date'], timezone.utc).isoformat(), 'numerator': numerator, 'denominator': denominator})
    return {'schema_version': 1, 'ticker': ticker, 'price': price, 'currency': 'USD',
            'trade_at': trade.isoformat(), 'retrieved_at': now.isoformat(), 'exchange': meta.get('exchangeName'),
            'price_type': 'last_regular_session_trade', 'provider': 'Yahoo Finance',
            'source_url': 'https://finance.yahoo.com/quote/' + ticker + '/', 'split_events': splits,
            'status': 'stale' if (now-trade).total_seconds() > 4*86400 else 'available',
            'limitations': ['Provider snapshot; may be delayed. Not an exchange-certified real-time quote.',
                            'A current price does not make older financial statements current.']}


def collect(root, tickers=None):
    fetcher = p.Fetcher(root, 'StockBrain/1.0 (https://github.com/eladyesh/stock-brain)')
    requested = tickers or [c['ticker'] for c in p.universe(root)]
    results = []
    for ticker in requested:
        p.issuer(root, ticker)
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/' + urllib.parse.quote(ticker, safe='') + '?interval=1mo&range=5y&events=splits'
        try:
            raw, meta = fetcher.fetch(url, refresh=True)
            row = parse_quote(json.loads(raw), ticker, meta['fetched_at'])
            row['request_url'] = url
            row['source_sha256'] = meta['sha256']
            p.write_json(root / 'research/market' / (ticker + '.json'), row)
            results.append({'ticker': ticker, 'status': row['status'], 'trade_at': row['trade_at']})
        except (OSError, ValueError, KeyError, TypeError) as error:
            results.append({'ticker': ticker, 'status': 'error', 'error': str(error)})
    report = {'checked_at': datetime.now(timezone.utc).isoformat(), 'results': results}
    p.write_json(root / 'research/market/status.json', report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    parser.add_argument('--ticker', action='append')
    args = parser.parse_args()
    report = collect(args.root.resolve(), args.ticker)
    print(json.dumps(report, indent=2))
    return 1 if any(r['status'] == 'error' for r in report['results']) else 0


if __name__ == '__main__':
    raise SystemExit(main())
