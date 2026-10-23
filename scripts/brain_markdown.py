"""Publish source-backed Markdown for every mapped stock issuer, without review promotion.

The generated brain-data branch owns these factual stubs. Curated research on
main remains untouched and is linked at its exact source commit. No acquisition
of SEC data occurs here: the input is an already verified coverage release.
"""
from __future__ import annotations

import argparse
import base64
from collections import defaultdict
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import subprocess
import tempfile
from urllib.parse import urlparse

import yaml

import financial_history
import market_directory
import stock_brain as kb
import ttm
from coverage_store import CoverageStore, SCHEMA_VERSION, require
from company_identity import primary_symbol, symbol_paths


REPO = 'eladyesh/stock-brain'
BRANCH = 'brain-data'
ROOT = Path(__file__).resolve().parents[1]
MAX_FILE = 512 * 1024
MAX_TOTAL = 768 * 1024 * 1024
MAX_PROFILES = 50_000
FORMAT = 'stock-brain-markdown'
GAP_ACTIONS = {
    'available': 'Retain dated financial evidence and review blocked metrics before analytical use.',
    'latest_filing_incomplete': 'Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.',
    'foreign_reporting_adapter': 'Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.',
    'fund_reporting_review': 'Review the instrument against its N-CSR/N-CSRS reporting evidence before applying an operating-company model. This signal alone is not a final fund classification.',
    'unsupported_reporting_inventory': 'Review primary filing evidence and identify the reporting regime; do not infer financial values from directory membership.',
    'not_collected': 'Collect verified issuer submissions and source financial data before normalization.',
}
CIK = re.compile(r'[0-9]{10}\Z')
SHA = re.compile(r'[0-9a-f]{40}\Z')
SHA256 = re.compile(r'[0-9a-f]{64}\Z')


def company_path(manifest, cik):
    """Read legacy generations; new user-facing folders use current symbols."""
    path = (manifest.get('company_paths') or {}).get(cik, f'brain/companies/{cik}/README.md')
    require(re.fullmatch(r'brain/companies/[A-Z0-9][A-Z0-9._-]*/README\.md', path), 'invalid company path')
    return path


class ProfileLoader(getattr(yaml, 'CSafeLoader', yaml.SafeLoader)):
    """Keep duplicate-key rejection while streaming thousands of large profiles."""


ProfileLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, kb.unique_mapping)


def split_profile(raw):
    match = re.match(r'\A---\n(.*?)\n---\n(.*)\Z', raw, flags=re.S)
    require(match is not None, 'profile frontmatter missing')
    meta = yaml.load(match[1], Loader=ProfileLoader)
    require(isinstance(meta, dict), 'profile metadata must be a mapping')
    return meta, match[2]


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


class FrozenStore(CoverageStore):
    """A verified, quiescent snapshot must never be migrated or switched to WAL."""
    def __init__(self, path):
        self.path = Path(path).resolve()
        self.clock = lambda: datetime.now(timezone.utc)
        require(self.path.is_file() and not any(Path(str(self.path) + suffix).exists()
                for suffix in ('-wal', '-shm', '-journal')), 'a frozen snapshot without sidecars is required')
        with self._connection() as db:
            require(db.execute('PRAGMA user_version').fetchone()[0] == SCHEMA_VERSION, 'unsupported frozen database schema')

    @contextmanager
    def _connection(self, write=False):
        require(not write, 'Markdown input is read only')
        db = sqlite3.connect(self.path.as_uri() + '?mode=ro&immutable=1', uri=True)
        db.row_factory = sqlite3.Row
        db.execute('PRAGMA query_only=ON')
        db.execute('PRAGMA trusted_schema=OFF')
        try:
            yield db
        finally:
            db.close()


def text(value):
    return kb.cell(value).replace('\n', ' ').replace('\r', ' ').replace('`', '&#96;')


def url(value):
    require(isinstance(value, str) and len(value) <= 2048 and not re.search(r'[\s<>"()]', value), 'invalid source URL')
    parsed = urlparse(value)
    require(parsed.scheme == 'https' and parsed.hostname is not None and not parsed.username, 'invalid source URL')
    return value


def stock_rows(store):
    placeholders = ','.join('?' for _ in market_directory.EQUITY_TYPES)
    with store._connection() as db:
        return [dict(r) for r in db.execute(f'''SELECT * FROM market_securities
            WHERE directory_status='present' AND is_test=0 AND instrument_type IN ({placeholders})
            ORDER BY cik,exchange,ticker''', market_directory.EQUITY_TYPES)]


def financial_gap(history, submissions, state):
    inventory = (submissions or {}).get('recent_filing_inventory') or (submissions or {}).get('filings') or []
    forms = sorted({x['form'] for x in inventory if x.get('form')})
    if history:
        reason = 'available'
    elif (state or {}).get('last_action') == 'filings_only_financials_incomplete':
        reason = 'latest_filing_incomplete'
    elif any(x in forms for x in ('10-K', '10-Q', '10-K/A', '10-Q/A')):
        # A mixed filing history cannot be classified as a fund/foreign issuer
        # from the presence of one historical form alone.
        reason = 'unsupported_reporting_inventory'
    elif any(x in forms for x in ('20-F', '40-F', '6-K', '20-F/A', '40-F/A', '6-K/A')):
        reason = 'foreign_reporting_adapter'
    elif any(x in forms for x in ('N-CSR', 'N-CSRS', 'N-CSR/A', 'N-CSRS/A')):
        reason = 'fund_reporting_review'
    elif submissions:
        reason = 'unsupported_reporting_inventory'
    else:
        reason = 'not_collected'
    return {'reason': reason, 'next_action': GAP_ACTIONS[reason], 'observed_forms': forms}


def profile(store, cik, rows, definitions, release, curated=None):
    """One issuer in memory, deterministic bytes, explicit missing research sections."""
    require(CIK.fullmatch(cik) is not None and int(cik) > 0, 'invalid issuer identity')
    company = store.company(cik)
    require(company is not None and all(r['cik'] == cik for r in rows), 'issuer/listing mismatch')
    payloads = {kind: store.get_payload(cik, kind) for kind in ('history', 'submissions', 'collector_state')}
    for value in payloads.values():
        require(value is None or value.get('cik') == cik, 'payload issuer mismatch')
    history, submissions, state = (payloads[k] for k in ('history', 'submissions', 'collector_state'))
    if history:
        financial_history.validate_history(history)
    gap = financial_gap(history, submissions, state)
    sources, lookup = [], {}

    def source(link, title, accessed, *, published=None, sha256=None):
        link = url(link)
        key = (link, accessed, sha256)
        if key not in lookup:
            sid = f'S{len(sources) + 1:02d}'
            lookup[key] = sid
            sources.append({'id': sid, 'title': str(title), 'url': link,
                            'published_at': published, 'retrieved_at': accessed, 'sha256': sha256})
        return '[' + lookup[key] + ']'

    sections = {d['id']: 'Not available: substantive research has not been completed. ' + d['prompt'] for d in definitions}
    name = company['company_name']
    aliases = sorted({r['ticker'] for r in rows})
    identity_lines = [f'Reported issuer name: **{text(name)}**. Stable SEC CIK: **{cik}**.',
                      'The directory links the following current stock listings to this issuer. Classification is provisional where indicated.',
                      '| Symbol | Exchange | Instrument | Identity revision | Evidence |',
                      '| --- | --- | --- | ---: | --- |']
    for row in rows:
        evidence = json.loads(row['source_json'])
        cite = source(evidence['url'], row['source_name'], evidence['retrieved_at'], sha256=evidence['sha256'])
        identity_lines.append('| ' + ' | '.join(text(row[k]) for k in ('ticker', 'exchange', 'instrument_type', 'identity_revision')) + f' | {cite} |')
    if submissions:
        evidence = submissions['source']
        cite = source(evidence['url'], 'SEC issuer submissions', evidence['retrieved_at'], sha256=evidence.get('sha256'))
        identity_lines[0] += ' ' + cite
        issuer = submissions.get('issuer') or {}
        if issuer.get('sic'):
            sections['industry-and-value-chain'] = (f"SEC-reported SIC **{text(issuer['sic'])}**: {text(issuer.get('sic_description'))}. {cite}\n\n"
                'This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.')
    identity_lines += ['', 'Not available: a reviewed explanation of the business, products, customers and competitive position.']
    sections['business-overview'] = '\n\n'.join(identity_lines[:2]) + '\n\n' + '\n'.join(identity_lines[2:])

    if history:
        source_meta = history['source']
        origin = source(source_meta['url'], 'SEC CompanyFacts source', source_meta['retrieved_at'], sha256=source_meta.get('sha256'))
        intro = (f"Evidence cutoff: {history['as_of']}. Source retrieved: {source_meta['retrieved_at']}. {origin}\n\n"
                 'US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. '
                 'Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. '
                 'Instant balance-sheet values are as of the period end; flow values cover the displayed interval.\n\n')
        flow, balance = [intro], [intro]
        for period in history['periods']:
            heading = f"### {text(period['type'])}: {period['start']} to {period['end']}\n\n"
            for target, is_balance in ((flow, False), (balance, True)):
                target.append(heading + '| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |\n| --- | ---: | --- | --- | --- | --- |')
                for metric, cell in sorted(history['financials'][period['id']].items()):
                    if (metric in ttm.BALANCE_METRICS) != is_balance:
                        continue
                    refs = []
                    for p in cell.get('provenance', []):
                        ref = source(p['url'], p['form'] + ' ' + p['accession'], source_meta['retrieved_at'], published=p['filed'])
                        if ref not in refs:
                            refs.append(ref)
                    flags = sorted(set(cell.get('flags', []) + period.get('flags', [])))
                    usable = (cell.get('model_usable') is True and not cell.get('conflicts')
                              and not ttm.BLOCKING_FLAGS.intersection(flags) and not period.get('flags'))
                    value = format(cell['value'], ',.12g') if usable and cell.get('value') is not None else 'Unavailable / blocked'
                    definition = cell.get('definition_tag') or ''
                    if cell.get('normalization'):
                        definition += ('; ' if definition else '') + cell['normalization']
                    if flags:
                        definition += '; ' + ', '.join(flags)
                    status = f"{cell.get('basis', 'US GAAP')} / {cell['status']}" + ('' if usable else ' / not model usable')
                    target.append('| ' + ' | '.join((text(metric), value, text(cell.get('unit')), text(status), text(definition), ' '.join(refs) or 'No eligible evidence')) + ' |')
                target.append('')
        sections['financial-performance'] = '\n'.join(flow)
        sections['balance-sheet-and-capital-allocation'] = '\n'.join(balance) + '\nNot available: reviewed debt maturity, acquisition, dividend and repurchase analysis.\n'

    filing_list = (submissions or {}).get('recent_filing_inventory') or (submissions or {}).get('filings') or []
    if filing_list:
        lines = [f'Latest {min(50, len(filing_list))} filing metadata records of {len(filing_list)} retained records. '
                 'A filing link is evidence of submission, not evidence that the document was read or analyzed.',
                 '| Filed | Form | Accession | Period end | Filing |', '| --- | --- | --- | --- | --- |']
        for filing in filing_list[:50]:
            cite = source(filing['url'], filing['form'] + ' ' + filing['accession'], submissions['source']['retrieved_at'], published=filing['filed'])
            lines.append('| ' + ' | '.join(text(filing.get(k)) for k in ('filed', 'form', 'accession', 'period_end')) + f' | {cite} |')
        sections['recent-developments'] = '\n\n'.join(lines[:1]) + '\n\n' + '\n'.join(lines[1:])
    gaps = ["Research remains a stub; automation does not approve an investment thesis.",
            "Sector, industry and domicile remain unassigned unless a separate reviewed profile supplies them.",
            "Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence."]
    if not history:
        gaps.append('No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.')
        gaps.append('Next collection task: ' + gap['next_action'])
        gaps.append('Forms observed in the retained filing inventory: ' + ', '.join(gap['observed_forms']))
    if state:
        gaps.append(f"Collector status: {state.get('status')}; last action: {state.get('last_action')}; last checked: {state.get('last_checked_at')}.")
    sections['scenarios-and-open-questions'] = '\n'.join('- ' + text(g) for g in gaps)
    if curated:
        sections['scenarios-and-open-questions'] += '\n\nDated curated research is maintained separately: ' + f"[profile at source commit]({curated['url']}) (status {curated['status']}, as of {curated['as_of']}). Automatic facts never change its review date."
    sections['sources-and-change-log'] = '\n\n'.join(
        f"[{s['id']}] [{text(s['title'])}]({s['url']}) — published {s['published_at'] or 'not supplied'}; retrieved {s['retrieved_at']}; "
        + (f"source SHA-256 `{s['sha256']}`." if s['sha256'] else 'filing linked by accession.') for s in sources)
    sections['sources-and-change-log'] += f"\n\nGenerated from verified data release `{release['release_tag']}`. Exact changes are retained in the brain-data Git history."
    input_sources = {kind: {key: value['source'][key] for key in ('url', 'sha256', 'retrieved_at', 'archive', 'acquisition')
                            if key in value['source']}
                     for kind, value in (('history', history), ('submissions', submissions)) if value}
    import research_financials
    research_filings = []
    # Keep annual, interim, governance and material-event sources even when the
    # fifty newest submissions are mostly ownership filings.
    all_filings = {f['accession']: f for f in filing_list + (submissions or {}).get('filings', [])}
    for forms in ({'10-K', '20-F', '40-F'}, {'10-Q', '6-K'}, {'DEF 14A'}, {'8-K'}):
        candidates = sorted((f for f in all_filings.values() if f['form'] in forms), key=lambda f: (f['filed'], f['accession']), reverse=True)
        if candidates:
            base = candidates[0]
            research_filings.append(base)
            research_filings.extend(f for f in all_filings.values() if f['form'] == base['form'] + '/A' and f.get('period_end') == base.get('period_end'))
    metadata = {'schema_version': 1, 'document_type': 'company_facts', 'company_id': 'company-cik-' + cik,
                'cik': cik, 'company_name': name, 'tickers': aliases, 'status': 'stub', 'canonical_reviewed': False,
                'as_of': release['created_at'][:10], 'updated_at': release['created_at'], 'reviewed_at': None,
                'coverage_release': release['release_tag'], 'source_commit': release['source_commit'],
                'financial_history_available': bool(history), 'curated_research': curated,
                'financial_gap': gap, 'input_sources': input_sources, 'sources': sources,
                'issuer_classification': (submissions or {}).get('issuer'),
                'classification_source': (submissions or {}).get('source'),
                'listings': [{k: r[k] for k in ('ticker', 'exchange', 'instrument_type')} for r in rows],
                'research_filings': research_filings[:12], 'financial_analysis': research_financials.analyze(history)}
    body = f"# {text(', '.join(aliases))} — {text(name)}\n\n> Automatically maintained factual stub. Substantive company research is incomplete.\n\n[All companies](../../INDEX.md)\n\n"
    body += '\n\n'.join(f"## {d['title']}\n\n{sections[d['id']]}" for d in definitions) + '\n'
    return '---\n' + yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True) + '---\n' + body


def unresolved(row, release):
    evidence = json.loads(row['source_json'])
    metadata = {'schema_version': 1, 'document_type': 'unresolved_listing', 'listing_key': row['listing_key'],
                'identity_revision': row['identity_revision'], 'cik': None, 'status': 'stub', 'canonical_reviewed': False,
                'ticker': row['ticker'], 'exchange': row['exchange'], 'coverage_release': release['release_tag'],
                'source': evidence}
    body = f"# {text(row['ticker'])} — identity unresolved\n\n[All companies](../INDEX.md)\n\n"
    body += f"Directory name: {text(row['security_name'])}. Instrument: {text(row['instrument_type'])}.\n\n"
    body += f"[Nasdaq Trader source]({url(evidence['url'])}), retrieved {evidence['retrieved_at']}, SHA-256 `{evidence['sha256']}`.\n\n"
    body += 'No verified issuer CIK is attached to this listing revision. Do not infer company identity, financial data, research coverage or U.S. domicile from this record.\n'
    return '---\n' + yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True) + '---\n' + body


def export(store, output, release, *, root=ROOT):
    output = Path(output)
    require(not output.exists(), 'output must be a new directory')
    require(SHA.fullmatch(release.get('source_commit', '')) is not None, 'source commit must be pinned')
    require(SHA256.fullmatch(release.get('database_sha256', '')) is not None, 'database digest required')
    definitions = kb.config(root)[1]
    curated = {}
    for doc in kb.documents(root):
        m = doc.metadata
        if m['cik']:
            curated[m['cik']] = {'url': f"https://github.com/{REPO}/blob/{release['source_commit']}/{doc.path.relative_to(root).as_posix()}",
                                 'status': m['status'], 'as_of': m['as_of'], 'sector': m['sector']}
    grouped, missing = defaultdict(list), []
    for row in stock_rows(store):
        if row['cik']:
            grouped[row['cik']].append(row)
        else:
            missing.append(row)
    require(0 < len(grouped) <= MAX_PROFILES and len(missing) <= MAX_PROFILES, 'unexpected profile count')
    slugs = symbol_paths([{'cik': cik, 'tickers': [r['ticker'] for r in rows]} for cik, rows in grouped.items()])
    paths = {cik: f'brain/companies/{slug}/README.md' for cik, slug in slugs.items()}
    files, total, financials = {}, 0, 0
    gap_groups = defaultdict(list)

    def write(path, content):
        nonlocal total
        raw = content.encode()
        require(0 < len(raw) <= (5 * 1024 * 1024 if path.endswith('INDEX.md') else MAX_FILE), 'Markdown file exceeds bound')
        total += len(raw)
        require(total <= MAX_TOTAL, 'Markdown export exceeds capacity')
        target = output / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        files[path] = {'sha256': digest(raw), 'size_bytes': len(raw)}

    index = ['# Stock Brain — Company Markdown', '',
             f"Verified data release: `{release['release_tag']}`. Source created: {release['created_at']}.", '',
             f"**{len(grouped)} distinct mapped issuers**, **{sum(map(len, grouped.values()))} mapped stock listings**, "
             f"**{len(missing)} unresolved listings**. All generated profiles remain factual stubs; these counts do not measure completed research or OTC coverage.", '',
             '## Company pages — sorted by symbol', '', '| Page | First symbol | Last symbol |', '| --- | --- | --- |']
    company_index, missing_index = [], []
    for cik, rows in sorted(grouped.items()):
        content = profile(store, cik, rows, definitions, release, curated.get(cik))
        meta, body = split_profile(content)
        kb.sections_from(body, definitions)
        financials += int(meta['financial_history_available'])
        gap_groups[meta['financial_gap']['reason']].append((cik, meta['company_name']))
        write(paths[cik], content)
        company_index.append((primary_symbol(meta['tickers']), f"| [{text(', '.join(meta['tickers']))}](../companies/{slugs[cik]}/README.md) | {text(meta['company_name'])} | {'available, quality gates apply' if meta['financial_history_available'] else 'not available'} |"))
        if len(files) % 500 == 0:
            print(json.dumps({'markdown_profiles_written': len(files), 'bytes': total}), flush=True)
    company_index.sort()
    for offset in range(0, len(company_index), 100):
        page = company_index[offset:offset + 100]
        number = offset // 100 + 1
        filename = f'index/companies-{number:04d}.md'
        write('brain/' + filename, f'# Company page {number}\n\n[All pages](../INDEX.md)\n\n'
              + '| Symbols | Company | Financial history |\n| --- | --- | --- |\n'
              + '\n'.join(row for _, row in page) + '\n')
        index.append(f'| [{number}]({filename}) | {page[0][0]} | {page[-1][0]} |')
    index += ['', '## Unresolved listing pages', '', '| Page | Listings |', '| --- | ---: |']
    for row in missing:
        write(f"brain/unmapped/{row['listing_key']}.md", unresolved(row, release))
        missing_index.append(f"| [{text(row['ticker'])}](../unmapped/{row['listing_key']}.md) | {text(row['exchange'])} | {text(row['security_name'])} |")
    for offset in range(0, len(missing_index), 100):
        number = offset // 100 + 1
        page = missing_index[offset:offset + 100]
        filename = f'index/unresolved-{number:04d}.md'
        write('brain/' + filename, f'# Unresolved listing page {number}\n\n[All pages](../INDEX.md)\n\n'
              + '| Symbol | Exchange | Directory name |\n| --- | --- | --- |\n' + '\n'.join(page) + '\n')
        index.append(f'| [{number}]({filename}) | {len(page)} |')
    index += ['', '[Coverage gaps and next research tasks](GAPS.md)', '']
    write('brain/INDEX.md', '\n'.join(index) + '\n')
    gap_lines = ['# Coverage gaps and next research tasks', '', '[Company index](INDEX.md)', '',
                 f"Data release: `{release['release_tag']}`; source created {release['created_at']}.", '',
                 'These counts describe distinct mapped issuers. Foreign-form and fund-reporting signals are derived from retained filing metadata, not a verified domicile or final instrument classification. '
                 'The universe may include funds awaiting instrument review. Financial coverage is separate from completed research.', '',
                 '| Financial collection state | Issuers | Next action |', '| --- | ---: | --- |']
    for reason, action in GAP_ACTIONS.items():
        gap_lines.append(f'| {reason} | {len(gap_groups[reason])} | {action} |')
    gap_lines += ['', f'Unresolved stock listings: **{len(missing)}**. Verify their issuer identity before attaching any company financial data.', '',
                  'Generated research profiles remain stubs. Curated research links retain their original review dates; broad market prices, consensus, news and ownership still need separate source coverage.', '']
    for reason, issuers in gap_groups.items():
        if reason == 'available' or not issuers:
            continue
        gap_lines += ['## ' + reason, '', GAP_ACTIONS[reason], '', 'Examples (up to 20; each company file contains its source evidence and task):', '']
        gap_lines += [f'- [{text(slugs[cik])} — {text(name)}](companies/{slugs[cik]}/README.md)' for cik, name in issuers[:20]]
        gap_lines.append('')
    write('brain/GAPS.md', '\n'.join(gap_lines))
    write('README.md', '# Stock Brain — Daily Markdown\n\n[Browse every company and unresolved listing](brain/INDEX.md).\n\n'
          'This branch contains automatically generated factual stubs from verified public coverage data. '
          'Financial source dates and quality gates are retained. Stubs are excluded from reviewed retrieval exports.\n\n'
          '[Curated research and generator source](https://github.com/' + REPO + '/tree/main) remain on main. '
          'Edit research there. The publisher refuses to overwrite manually modified files in this generated branch. '
          'Company paths use current symbols; CIKs remain immutable metadata keys. Unresolved listing paths identify exchange/symbol slots, not issuers. '
          'Previous snapshots remain in Git history; disappearance is not proof of delisting.\n')
    manifest = {'format': FORMAT, 'version': 2, **release, 'company_profiles': len(grouped), 'company_paths': paths,
                'mapped_stock_listings': sum(map(len, grouped.values())), 'unresolved_listings': len(missing),
                'financial_profiles': financials, 'reviewed_generated_profiles': 0, 'bytes': total,
                'financial_gap_counts': {reason: len(gap_groups[reason]) for reason in GAP_ACTIONS},
                'company_ciks': sorted(grouped), 'unresolved_listing_keys': sorted(r['listing_key'] for r in missing)}
    write('brain/publication.json', json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    (output / 'brain/files.json').write_text(json.dumps(files, sort_keys=True, indent=2) + '\n')
    verify(output, definitions)
    return manifest


def verify(output, definitions=None):
    """Check every persisted file and identity; fail closed on edits or extra files."""
    output = Path(output)
    files = json.loads((output / 'brain/files.json').read_text())
    actual = {p.relative_to(output).as_posix() for p in output.rglob('*') if p.is_file() and '.git' not in p.relative_to(output).parts}
    require(actual == set(files) | {'brain/files.json'}, 'unexpected or missing files; preserve manual changes')
    manifest = json.loads((output / 'brain/publication.json').read_text())
    require(manifest.get('format') == FORMAT and manifest.get('version') in (1, 2), 'invalid publication format')
    if manifest['version'] == 2:
        require(set(manifest['company_paths']) == set(manifest['company_ciks'])
                and len(set(manifest['company_paths'].values())) == manifest['company_profiles'], 'ambiguous company paths')
    company_ciks, unresolved_keys, financials = [], [], 0
    identities = []
    gap_counts = {reason: 0 for reason in GAP_ACTIONS}
    total = 0
    definitions = definitions or kb.config(ROOT)[1]
    for name, entry in files.items():
        path = Path(name)
        require(not path.is_absolute() and '..' not in path.parts and not (output / path).is_symlink(), 'unsafe export path')
        raw = (output / path).read_bytes()
        require(len(raw) == entry['size_bytes'] and digest(raw) == entry['sha256'], 'file digest differs; preserve manual changes')
        total += len(raw)
        require(total <= MAX_TOTAL and len(raw) <= (5 * 1024 * 1024 if name.endswith('INDEX.md') else MAX_FILE), 'export exceeds capacity')
        if name.startswith('brain/companies/'):
            meta, body = split_profile(raw.decode())
            cik = meta['cik']
            require(CIK.fullmatch(cik) is not None and int(cik) > 0 and name == company_path(manifest, cik), 'invalid profile path')
            require(meta['document_type'] == 'company_facts' and meta['company_id'] == 'company-cik-' + cik, 'invalid profile identity')
            require(meta['status'] == 'stub' and meta['canonical_reviewed'] is False and meta['reviewed_at'] is None, 'automatic research promotion')
            require(meta['coverage_release'] == manifest['release_tag'] and meta['source_commit'] == manifest['source_commit'], 'profile publication mismatch')
            kb.sections_from(body, definitions)
            require(set(kb.CITATION.findall(body)) <= {s['id'] for s in meta['sources']}, 'unregistered citation')
            company_ciks.append(cik)
            identities.append({'cik': cik, 'tickers': meta['tickers']})
            financials += int(meta['financial_history_available'])
            if 'financial_gap_counts' in manifest:
                reason = meta['financial_gap']['reason']
                require(reason in gap_counts and (reason == 'available') == meta['financial_history_available'], 'financial gap differs from coverage')
                gap_counts[reason] += 1
        elif name.startswith('brain/unmapped/'):
            meta, _ = split_profile(raw.decode())
            require(meta['document_type'] == 'unresolved_listing' and meta['cik'] is None and meta['canonical_reviewed'] is False, 'unresolved issuer promoted')
            require(name == f"brain/unmapped/{meta['listing_key']}.md", 'unresolved path mismatch')
            unresolved_keys.append(meta['listing_key'])
    require(sorted(company_ciks) == manifest['company_ciks'] and len(company_ciks) == manifest['company_profiles'], 'profile inventory mismatch')
    if manifest['version'] == 2:
        require(manifest['company_paths'] == {cik: f'brain/companies/{slug}/README.md' for cik, slug in symbol_paths(identities).items()}, 'symbol folders differ from issuer inventory')
    require(sorted(unresolved_keys) == manifest['unresolved_listing_keys'] and len(unresolved_keys) == manifest['unresolved_listings'], 'unresolved inventory mismatch')
    require(financials == manifest['financial_profiles'] and manifest['reviewed_generated_profiles'] == 0, 'coverage counts differ')
    if 'financial_gap_counts' in manifest:
        require(gap_counts == manifest['financial_gap_counts'], 'financial gap counts differ')
    return manifest


def publish(output):
    """Fast-forward a generated-only branch; never store credentials or touch main."""
    manifest = verify(output)
    token = os.environ.get('GH_TOKEN')
    require(bool(token), 'GH_TOKEN is required for authorized publication')
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GIT_CONFIG_COUNT='1',
               GIT_CONFIG_KEY_0='http.https://github.com/.extraheader',
               GIT_CONFIG_VALUE_0='AUTHORIZATION: basic ' + base64.b64encode(('x-access-token:' + token).encode()).decode())
    with tempfile.TemporaryDirectory() as temporary:
        target = Path(temporary)

        def git(*args, allowed=(0,)):
            result = subprocess.run(['git', *args], cwd=target, env=env, capture_output=True, text=True, timeout=600)
            require(result.returncode in allowed, 'Git publication failed: ' + args[0])
            return result

        git('init', '-q')
        git('remote', 'add', 'origin', f'https://github.com/{REPO}.git')
        found = git('ls-remote', '--exit-code', '--heads', 'origin', BRANCH, allowed=(0, 2))
        if found.returncode == 0:
            git('fetch', '--depth=1', 'origin', BRANCH)
            git('checkout', '-q', '-b', BRANCH, 'FETCH_HEAD')
            previous = verify(target)
            require(manifest['created_at'] >= previous['created_at'], 'refuse a backwards data publication')
            shutil.rmtree(target / 'brain')
            (target / 'README.md').unlink()
        else:
            git('checkout', '--orphan', BRANCH)
        shutil.copytree(Path(output) / 'brain', target / 'brain')
        shutil.copy2(Path(output) / 'README.md', target / 'README.md')
        verify(target)
        git('add', '--', 'README.md', 'brain')
        changed = git('diff', '--cached', '--quiet', allowed=(0, 1))
        if changed.returncode:
            git('-c', 'user.name=github-actions[bot]', '-c', 'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                'commit', '-q', '-m', 'Refresh factual Markdown: ' + manifest['release_tag'])
            git('push', 'origin', 'HEAD:refs/heads/' + BRANCH)
        commit = git('rev-parse', 'HEAD').stdout.strip()
        remote = git('ls-remote', '--exit-code', '--heads', 'origin', BRANCH).stdout.split()[0]
        require(remote == commit, 'published branch did not match verified commit')
    return {'commit': commit, 'company_profiles': manifest['company_profiles'],
            'unresolved_listings': manifest['unresolved_listings'], 'release_tag': manifest['release_tag'],
            'url': f'https://github.com/{REPO}/blob/{commit}/brain/INDEX.md'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['export', 'verify', 'publish'])
    parser.add_argument('--output', type=Path, default=Path('build/brain-data'))
    parser.add_argument('--database', type=Path)
    parser.add_argument('--manifest', type=Path)
    parser.add_argument('--source-commit', default=os.environ.get('GITHUB_SHA'))
    parser.add_argument('--result-file', type=Path)
    args = parser.parse_args()
    if args.command == 'export':
        require(SHA.fullmatch(args.source_commit or '') is not None, 'source commit required')
        import coverage_release
        with tempfile.TemporaryDirectory() as temporary:
            database = args.database or Path(temporary) / 'coverage.sqlite3'
            if args.database:
                require(args.manifest is not None, 'local export requires verified coverage manifest')
                m = json.loads(args.manifest.read_text())
                require(file_digest(database) == m['database_manifest']['snapshot']['sha256'], 'database hash mismatch')
            else:
                latest = coverage_release.latest_release()
                require(latest is not None, 'no verified coverage release')
                m = coverage_release.download_release(latest, database)
            release = {'release_tag': m['release_tag'], 'created_at': m['created_at'],
                       'database_sha256': m['database_manifest']['snapshot']['sha256'], 'source_commit': args.source_commit}
            result = export(FrozenStore(database), args.output, release)
            require(file_digest(database) == release['database_sha256'], 'snapshot changed during Markdown export')
    elif args.command == 'verify':
        result = verify(args.output)
    else:
        result = publish(args.output)
    if args.result_file:
        args.result_file.write_text(json.dumps(result) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in {'company_ciks', 'unresolved_listing_keys', 'company_paths'}}, indent=2))


if __name__ == '__main__':
    main()
