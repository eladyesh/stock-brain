"""Symbol-first, read-only research library with bounded verified Markdown reads."""
from collections import Counter, OrderedDict
import json
from pathlib import Path
import re
import threading
from urllib.parse import parse_qs, unquote
from urllib.request import Request, urlopen

import brain_markdown as brain
import stock_brain as kb
import sector_facts
from company_identity import primary_symbol
from coverage_store import require


def download(url, limit):
    with urlopen(Request(url, headers={'User-Agent': 'StockBrain/1.0 research-library'}), timeout=8) as response:
        raw = response.read(limit + 1)
    require(len(raw) <= limit, 'research resource exceeds bound')
    return raw


def validate_manifest(m):
    require(m.get('format') == sector_facts.FORMAT and m.get('version') in (1, 2), 'invalid research index')
    rows = m['companies']
    require(isinstance(rows, list) and 0 < len(rows) == m['company_profiles'] <= brain.MAX_PROFILES, 'invalid research inventory')
    require(len({r['cik'] for r in rows}) == len(rows), 'duplicate issuer in research index')
    for row in rows:
        match = sector_facts.PATH.fullmatch(row['path'])
        require(brain.CIK.fullmatch(row['cik']) and match and match[1] == row['sector'], 'invalid research path')
        require(brain.SHA256.fullmatch(row['sha256']) and 0 < row['size_bytes'] <= sector_facts.MAX_FILE, 'invalid research digest/size')
        primary_symbol(row['tickers'])
    require(dict(Counter(r['sector'] for r in rows)) == m['sector_counts'], 'research sector counts differ')
    return m


class ResearchLibrary:
    def __init__(self, root):
        self.root = Path(root)
        self.lock = threading.RLock()
        self.slots = threading.BoundedSemaphore(2)
        self.cache = OrderedDict()
        path = self.root / sector_facts.MANIFEST
        self.local = validate_manifest(json.loads(path.read_text())) if path.exists() else None
        self.local_rows = {r['cik']: r for r in (self.local or {}).get('companies', [])}
        self.manifest, self.commit, self.status = self.local, None, 'local' if self.local else 'waiting'

    def refresh(self):
        try:
            ref = json.loads(download(f'https://api.github.com/repos/{brain.REPO}/git/ref/heads/main', 10000))
            commit = ref['object']['sha']
            require(ref['ref'] == 'refs/heads/main' and ref['object']['type'] == 'commit' and brain.SHA.fullmatch(commit), 'invalid main ref')
            if commit == self.commit:
                self.status = 'ready'
                return
            m = validate_manifest(json.loads(download(f'https://raw.githubusercontent.com/{brain.REPO}/{commit}/{sector_facts.MANIFEST}', 16_000_000)))
            with self.lock:
                require(not self.manifest or m['created_at'] >= self.manifest['created_at'], 'older research generation')
                self.manifest, self.commit, self.status = m, commit, 'ready'
        except (OSError, ValueError, KeyError, TypeError):
            self.status = 'degraded'

    def list(self, query=''):
        q = parse_qs(query, keep_blank_values=True, strict_parsing=False)
        require(set(q) <= {'q', 'sector', 'stage', 'limit', 'offset'} and all(len(v) == 1 for v in q.values()), 'invalid research query')
        search = q.get('q', [''])[0].strip().upper()
        limit, offset = int(q.get('limit', ['25'])[0]), int(q.get('offset', ['0'])[0])
        require(len(search) <= 100 and 1 <= limit <= 100 and 0 <= offset <= brain.MAX_PROFILES, 'invalid query bounds')
        with self.lock:
            m = self.manifest
        if not m:
            return {'available': False, 'items': [], 'total': 0}
        sector, stage = q.get('sector', [''])[0], q.get('stage', [''])[0]
        require(not sector or sector in m['sector_counts'], 'unknown research sector')
        require(stage in {'', 'pending', 'retry', 'source_missing', 'evidence_collected', 'draft'}, 'unknown research stage')
        rows = [r for r in m['companies'] if (not sector or r['sector'] == sector)
                and (not stage or r.get('research', {}).get('stage', 'pending') == stage)
                and (not search or all(part in (' '.join(r['tickers']) + ' ' + r['company_name'] + ' ' + r['cik']).upper() for part in search.split()))]
        rows.sort(key=lambda r: (0 if search in r['tickers'] else 1, primary_symbol(r['tickers']), r['cik']))
        return {'available': True, 'items': [{k: r.get(k) for k in ('cik', 'company_name', 'tickers', 'symbol', 'sector', 'financial_history_available', 'research')} for r in rows[offset:offset + limit]],
                'total': len(rows), 'offset': offset, 'limit': limit, 'status': self.status,
                'source_created_at': m['created_at'], 'release_tag': m['release_tag'], 'company_profiles': m['company_profiles'],
                'financial_profiles': m['financial_profiles'], 'sector_counts': m['sector_counts'],
                'research_queue': m.get('research_queue'), 'reviewed_generated_profiles': 0}

    def detail(self, identifier):
        require(re.fullmatch(r'[A-Z0-9.\-^/$]{1,40}', identifier), 'invalid company symbol')
        with self.lock:
            m, commit = self.manifest, self.commit
        if not m:
            return None
        rows = [r for r in m['companies'] if identifier == r['cik'] or identifier in r['tickers']]
        if not rows:
            return None
        require(len(rows) == 1, 'ambiguous symbol; select a specific issuer')
        row = rows[0]
        key = row['sha256']
        with self.lock:
            cached = self.cache.get(key)
            if cached is not None:
                self.cache.move_to_end(key)
                return cached
        if self.local_rows.get(row['cik'], {}).get('sha256') == key:
            path = self.root / row['path']
            require(not any(p.is_symlink() for p in [path, *path.parents]), 'linked research file')
            raw = path.read_bytes()
        else:
            require(bool(commit), 'research generation not pinned')
            if not self.slots.acquire(blocking=False):
                raise OSError('research reads busy')
            try:
                raw = download(f'https://raw.githubusercontent.com/{brain.REPO}/{commit}/{row["path"]}', sector_facts.MAX_FILE)
            finally:
                self.slots.release()
        require(len(raw) == row['size_bytes'] and brain.digest(raw) == key, 'research file integrity mismatch')
        meta, body = brain.split_profile(raw.decode())
        require(meta['cik'] == row['cik'] and meta['tickers'] == row['tickers'] and meta['coverage_release'] == m['release_tag']
                and meta['status'] == 'stub' and meta['canonical_reviewed'] is False, 'research metadata differs')
        sections = kb.sections_from(body, kb.config(self.root)[1])
        require(set(kb.CITATION.findall(body)) <= {s['id'] for s in meta['sources']}, 'missing research citation')
        result = {'company': {k: row.get(k) for k in ('cik', 'company_name', 'tickers', 'sector')},
            'sections': sections, 'sources': meta['sources'], 'research': meta.get('research_progress', {}),
            'curated_research': meta.get('curated_research'), 'updated_at': meta['updated_at'],
            'release_tag': meta['coverage_release'], 'canonical_reviewed': False,
            'classification': meta['sector_assignment'], 'financial_gap': meta.get('financial_gap'),
            'markdown_url': f'https://github.com/{brain.REPO}/blob/{commit or "main"}/{row["path"]}',
            'full_history_url': meta['full_history_url']}
        with self.lock:
            self.cache[key] = result
            while len(self.cache) > 32:
                self.cache.popitem(last=False)
        return result

    def serve(self, path, query):
        try:
            if path == '/api/research':
                return '200 OK', self.list(query)
            require(not query, 'detail query is unsupported')
            result = self.detail(unquote(path.removeprefix('/api/research/')).upper())
            return ('200 OK', result) if result else ('404 Not Found', {'error': 'research_company_not_found'})
        except (ValueError, KeyError, TypeError):
            return '400 Bad Request', {'error': 'invalid_or_unverified_research'}
        except OSError:
            return '503 Service Unavailable', {'error': 'research_temporarily_unavailable'}
