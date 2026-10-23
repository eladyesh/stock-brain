"""Maintain bounded, source-backed company Markdown inside main/sectors.

Full financial history stays in brain-data. Main contains a useful recent-period
view for each issuer, never a link-only placeholder or an approved research claim.
"""
from collections import Counter
import argparse
import base64
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

import yaml
import brain_markdown as brain
import stock_brain as kb
from coverage_store import require

MANIFEST = 'data/sector-facts.json'
FORMAT = 'stock-brain-sector-facts'
MAX_TOTAL = 128 * 1024 * 1024
MAX_FILE = 96 * 1024
PATH = re.compile(r'sectors/([a-z-]+)/facts/([0-9]{10})/README\.md\Z')


def rules(root):
    config = json.loads((root / 'config/sector_sic_rules.json').read_text())
    known = {s['id'] for s in kb.config(root)[0]}
    mapping = {}
    require(config['version'] == 1 and set(config['sectors']) == known, 'invalid sector rules')
    for sector, codes in config['sectors'].items():
        for code in codes.split():
            require(re.fullmatch(r'[0-9]{4}', code) and code not in mapping, 'invalid or duplicate SIC rule')
            mapping[code] = sector
    return config, mapping


def classify(meta, root=brain.ROOT):
    config, mapping = rules(root)
    issuer = meta.get('issuer_classification') or {}
    curated = meta.get('curated_research') or {}
    result = {'sector': 'unclassified', 'method': 'unresolved', 'sic': issuer.get('sic'),
              'sic_description': issuer.get('sic_description'), 'rule_version': config['version'],
              'reason': 'Missing, ambiguous or unmapped reported industry; company-specific review is required.'}
    if curated.get('sector') in config['sectors']:
        result.update(sector=curated['sector'], method='curated_profile',
                      reason='Uses the dated curated profile assignment; automatic data does not renew its review.', source_url=curated['url'])
    elif (meta.get('financial_gap', {}).get('reason') == 'fund_reporting_review'
          or any(f in {'N-CSR', 'N-CSRS', 'N-CSR/A', 'N-CSRS/A'} for f in meta.get('financial_gap', {}).get('observed_forms', []))):
        result['reason'] = 'Fund reporting signal requires instrument review before operating-sector classification.'
    elif issuer.get('sic') in mapping and meta.get('classification_source'):
        result.update(sector=mapping[issuer['sic']], method='project_sic_rule',
                      reason=config['policy'], source_url=meta['classification_source']['url'])
    return result


def recent_periods(content):
    """Copy source-rendered cells unchanged; choose the newest annual/quarter/TTM."""
    parts = re.split(r'(?m)(?=^### )', content)
    selected = {}
    for part in parts[1:]:
        match = re.match(r'### (annual|quarterly|ttm): ([0-9-]{10}) to ([0-9-]{10})\n', part)
        require(match is not None, 'unrecognized financial period heading')
        kind, end = match[1], match[3]
        if kind not in selected or end > selected[kind][0]:
            selected[kind] = (end, part)
    if not selected:
        return content
    return parts[0] + 'This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.\n\n' + '\n'.join(selected[k][1] for k in ('annual', 'quarterly', 'ttm') if k in selected)


def render(meta, body, definitions, assignment, publication_commit):
    sections = kb.sections_from(body, definitions)
    for key in ('financial-performance', 'balance-sheet-and-capital-allocation'):
        sections[key] = recent_periods(sections[key])
    recent = sections['recent-developments']
    if '| Filed | Form |' in recent:
        lines = recent.splitlines()
        rows = [line for line in lines if line.startswith('|')]
        sections['recent-developments'] = ('Latest five available filing metadata records; document bodies have not been analyzed here.\n\n'
                                           + '\n'.join(rows[:7]))
    sections['scenarios-and-open-questions'] = sections['scenarios-and-open-questions'].replace(
        'Sector, industry and domicile remain unassigned unless a separate reviewed profile supplies them.',
        'The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.')
    classification_text = ('\n\nNavigation sector: **' + assignment['sector'] + '**. Method: `' + assignment['method']
                           + '`. ' + assignment['reason'])
    sections['industry-and-value-chain'] += classification_text
    sections.pop('sources-and-change-log')
    used = set(kb.CITATION.findall('\n'.join(sections.values())))
    sources = [s for s in meta['sources'] if s['id'] in used]
    require(used == {s['id'] for s in sources}, 'compact profile lost source evidence')
    full_url = f"https://github.com/{brain.REPO}/blob/{publication_commit}/brain/companies/{meta['cik']}/README.md"
    sections['sources-and-change-log'] = '\n\n'.join(
        f"[{s['id']}] [{brain.text(s['title'])}]({brain.url(s['url'])}) — published {s['published_at'] or 'not supplied'}; retrieved {s['retrieved_at']}."
        for s in sources) + f"\n\nSource release: `{meta['coverage_release']}`. [Complete financial history and original evidence hashes]({full_url}).\n\nChanges remain in main Git history. This generated factual profile does not promote or replace curated research."
    metadata = {**meta, 'sources': sources, 'sector_assignment': assignment,
                'full_history_url': full_url, 'full_history_commit': publication_commit,
                'view': 'latest_available_annual_quarterly_ttm_and_five_filings'}
    title = f"# {brain.text(meta['company_name'])} — {brain.text(', '.join(meta['tickers']))}\n\n"
    title += ('> Automatically maintained factual profile. Research status: stub. Missing research is explicit.\n\n'
              '[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · '
              f'[Full financial history]({full_url})\n\n')
    return '---\n' + yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True) + '---\n' + title + '\n\n'.join(
        f"## {d['title']}\n\n{sections[d['id']]}" for d in definitions) + '\n'


def export(publication, output, commit, *, root=brain.ROOT):
    require(brain.SHA.fullmatch(commit or ''), 'published brain-data commit required')
    source = brain.verify(publication)
    output = Path(output)
    require(not output.exists(), 'output must be a new directory')
    definitions = kb.config(root)[1]
    records, total = [], 0
    for cik in source['company_ciks']:
        meta, body = brain.split_profile((Path(publication) / f'brain/companies/{cik}/README.md').read_text())
        assignment = classify(meta, root)
        name = f"sectors/{assignment['sector']}/facts/{cik}/README.md"
        raw = render(meta, body, definitions, assignment, commit).encode()
        total += len(raw)
        require(0 < len(raw) <= MAX_FILE and total <= MAX_TOTAL, 'sector facts exceed capacity')
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        records.append({'cik': cik, 'company_name': meta['company_name'], 'tickers': meta['tickers'],
                        'sector': assignment['sector'], 'classification_method': assignment['method'],
                        'financial_history_available': meta['financial_history_available'], 'path': name,
                        'sha256': brain.digest(raw), 'size_bytes': len(raw)})
    manifest = {'format': FORMAT, 'version': 1, 'release_tag': source['release_tag'], 'created_at': source['created_at'],
                'brain_commit': commit, 'source_commit': source['source_commit'], 'database_sha256': source['database_sha256'],
                'company_profiles': len(records), 'financial_profiles': source['financial_profiles'],
                'unresolved_listings': source['unresolved_listings'], 'bytes': total,
                'sector_counts': dict(sorted(Counter(r['sector'] for r in records).items())), 'companies': records}
    (output / 'data').mkdir()
    (output / MANIFEST).write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    verify(output, root=root, current_rules=True)
    return manifest


def verify(target, *, root=brain.ROOT, allow_absent=False, current_rules=False):
    target = Path(target)
    path = target / MANIFEST
    actual = {p.relative_to(target).as_posix() for p in (target / 'sectors').glob('*/facts/**/*') if p.is_file()}
    if not path.exists():
        require(allow_absent and not actual, 'missing sector facts manifest; preserve manual changes')
        return None
    require(path.stat().st_size <= 32 * 1024 * 1024, 'sector manifest exceeds bound')
    m = json.loads(path.read_text())
    require(m['format'] == FORMAT and m['version'] == 1, 'unsupported sector facts')
    require(brain.SHA.fullmatch(m['brain_commit']) and brain.SHA.fullmatch(m['source_commit']), 'invalid source commits')
    definitions = kb.config(root)[1]
    seen, total, financials = set(), 0, 0
    for row in m['companies']:
        match = PATH.fullmatch(row['path'])
        require(match and match[1] == row['sector'] and match[2] == row['cik'] and row['cik'] not in seen, 'ambiguous sector identity')
        seen.add(row['cik'])
        p = target / row['path']
        require(not any(parent.is_symlink() for parent in [p, *p.parents]) and p.is_file(), 'missing or linked sector file')
        raw = p.read_bytes()
        require(len(raw) == row['size_bytes'] <= MAX_FILE and brain.digest(raw) == row['sha256'], 'sector file changed; preserve manual changes')
        total += len(raw)
        require(total <= MAX_TOTAL, 'sector facts exceed capacity')
        meta, body = brain.split_profile(raw.decode())
        require(meta['cik'] == row['cik'] and meta['company_id'] == 'company-cik-' + row['cik'], 'sector profile identity mismatch')
        require(meta['document_type'] == 'company_facts' and meta['status'] == 'stub' and meta['canonical_reviewed'] is False and meta['reviewed_at'] is None, 'automatic research promotion')
        require(meta['coverage_release'] == m['release_tag'] and meta['full_history_commit'] == m['brain_commit'], 'sector publication mismatch')
        assignment = meta['sector_assignment']
        require(assignment['sector'] == row['sector'] and assignment['method'] == row['classification_method']
                and assignment['sector'] in {s['id'] for s in kb.config(root)[0]} | {'unclassified'}
                and assignment['method'] in {'unresolved', 'curated_profile', 'project_sic_rule'}, 'sector evidence differs')
        if current_rules:
            require(assignment == classify(meta, root), 'sector evidence differs from current rules')
        require(meta['company_name'] == row['company_name'] and meta['tickers'] == row['tickers'] and meta['financial_history_available'] == row['financial_history_available'], 'sector index differs')
        financials += int(meta['financial_history_available'])
        kb.sections_from(body, definitions)
        require(set(kb.CITATION.findall(body)) <= {s['id'] for s in meta['sources']}, 'missing sector citation')
    require(actual == {r['path'] for r in m['companies']}, 'unexpected sector file; preserve manual changes')
    require(len(seen) == m['company_profiles'] and financials == m['financial_profiles'] and total == m['bytes'], 'sector counts differ')
    require(dict(Counter(r['sector'] for r in m['companies'])) == m['sector_counts'], 'sector totals differ')
    return m


def install(output, target, *, root=brain.ROOT):
    """Only manifest-owned facts are replaced; manual research never enters scope."""
    incoming = verify(output, root=root, current_rules=True)
    previous = verify(target, root=root, allow_absent=True)
    if previous:
        require(incoming['created_at'] >= previous['created_at'], 'refuse backwards sector facts')
    old = {r['path'] for r in (previous or {}).get('companies', [])}
    new = {r['path'] for r in incoming['companies']}
    for name in old - new:
        (Path(target) / name).unlink()
    for name in new | {MANIFEST}:
        path = Path(target) / name
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(Path(output) / name, path)
    verify(target, root=root)


def publish(output):
    incoming = verify(output, current_rules=True)
    token = os.environ.get('GH_TOKEN')
    require(bool(token), 'GH_TOKEN is required for authorized sector publication')
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GIT_CONFIG_COUNT='1', GIT_CONFIG_KEY_0='http.https://github.com/.extraheader',
               GIT_CONFIG_VALUE_0='AUTHORIZATION: basic ' + base64.b64encode(('x-access-token:' + token).encode()).decode())
    with tempfile.TemporaryDirectory() as temporary:
        target = Path(temporary)
        def git(*args, allowed=(0,)):
            r = subprocess.run(['git', *args], cwd=target, env=env, capture_output=True, text=True, timeout=600)
            require(r.returncode in allowed, 'sector Git publication failed: ' + args[0])
            return r
        git('init', '-q')
        git('remote', 'add', 'origin', f'https://github.com/{brain.REPO}.git')
        git('fetch', '--depth=1', 'origin', 'main')
        git('checkout', '-q', '-b', 'main', 'FETCH_HEAD')
        current = git('rev-parse', 'HEAD').stdout.strip()
        if verify(target, root=target, allow_absent=True) == incoming:
            kb.build(target, check=True)
            return {'commit': current, 'company_profiles': incoming['company_profiles'], 'sector_counts': incoming['sector_counts']}
        require(current == incoming['source_commit'], 'main moved; regenerate from its current source before publication')
        install(output, target, root=target)
        kb.build(target)
        kb.build(target, check=True)
        git('add', '--', 'sectors', MANIFEST, 'INDEX.md', 'data/catalog.json')
        changed = git('diff', '--cached', '--name-only').stdout.splitlines()
        allowed = {r['path'] for r in incoming['companies']} | {MANIFEST, 'INDEX.md', 'data/catalog.json', 'sectors/README.md'}
        for name in changed:
            require(name in allowed or PATH.fullmatch(name) or re.fullmatch(r'sectors/[a-z-]+/INDEX\.md', name), 'publication tried to modify curated research')
        if changed:
            git('-c', 'user.name=github-actions[bot]', '-c', 'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                'commit', '-q', '-m', 'Refresh sector factual profiles: ' + incoming['release_tag'])
            git('push', 'origin', 'HEAD:refs/heads/main')
        commit = git('rev-parse', 'HEAD').stdout.strip()
        require(git('ls-remote', '--exit-code', '--heads', 'origin', 'main').stdout.split()[0] == commit, 'sector publication ref differs')
    return {'commit': commit, 'company_profiles': incoming['company_profiles'], 'sector_counts': incoming['sector_counts']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['export', 'verify', 'install', 'publish'])
    parser.add_argument('--publication', type=Path, default=Path('build/brain-data'))
    parser.add_argument('--output', type=Path, default=Path('build/sector-facts'))
    parser.add_argument('--target', type=Path, default=brain.ROOT)
    parser.add_argument('--commit')
    args = parser.parse_args()
    if args.command == 'export':
        result = export(args.publication, args.output, args.commit)
    elif args.command == 'verify':
        result = verify(args.target)
    elif args.command == 'install':
        install(args.output, args.target)
        result = verify(args.target)
    else:
        result = publish(args.output)
    print(json.dumps({k: v for k, v in result.items() if k != 'companies'}, indent=2))


if __name__ == '__main__':
    main()
