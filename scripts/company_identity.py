"""Readable symbol paths, with immutable issuer identity kept in metadata."""
from collections import Counter
import re


def primary_symbol(tickers):
    values = sorted(set(tickers), key=lambda value: (len(value), value))
    if not values or any(not isinstance(v, str) or not re.fullmatch(r'[A-Z0-9][A-Z0-9.\-^/$]{0,31}', v) or '..' in v for v in values):
        raise ValueError('A verified current symbol is required')
    return values[0]


def symbol_slug(symbol):
    # A slash or preferred-share suffix must never become a path separator.
    return ''.join(c if c.isascii() and (c.isalnum() or c in '.-') else '_' + format(ord(c), '02X') for c in symbol)


def symbol_paths(companies):
    """Deterministic collision handling; never merge different CIKs by ticker."""
    symbols = {c['cik']: primary_symbol(c['tickers']) for c in companies}
    slugs = {cik: symbol_slug(symbol) for cik, symbol in symbols.items()}
    counts = Counter(slugs.values())
    return {cik: (slug if counts[slug] == 1 else slug + '--' + cik) for cik, slug in slugs.items()}
