"""Read a bounded, commit-pinned index of persisted Markdown, off the HTTP path."""
import json
import re
from datetime import datetime, timezone
from urllib.request import Request, urlopen

from coverage_store import require

REPO = 'eladyesh/stock-brain'
SHA = re.compile(r'[0-9a-f]{40}\Z')
TAG = re.compile(r'coverage-\d{8}-[0-9]+-[0-9]+\Z')


def read_json(url, limit):
    with urlopen(Request(url, headers={'User-Agent': 'StockBrain/1.0 markdown-index'}), timeout=30) as response:
        raw = response.read(limit + 1)
    require(len(raw) <= limit, 'Markdown index exceeds capacity')
    return json.loads(raw)


class BrainPublication:
    def __init__(self):
        self.publication = None
        self.status = 'waiting'
        self.last_success_at = None

    def refresh(self):
        try:
            ref = read_json(f'https://api.github.com/repos/{REPO}/git/ref/heads/brain-data', 10_000)
            commit = ref['object']['sha']
            require(ref['ref'] == 'refs/heads/brain-data' and ref['object']['type'] == 'commit' and SHA.fullmatch(commit), 'invalid publication ref')
            if self.publication and self.publication['commit'] == commit:
                self.status = 'ready'
                self.last_success_at = datetime.now(timezone.utc).isoformat()
                return
            m = read_json(f'https://raw.githubusercontent.com/{REPO}/{commit}/brain/publication.json', 2_000_000)
            require(m.get('format') == 'stock-brain-markdown' and m.get('version') == 1, 'invalid Markdown index')
            require(TAG.fullmatch(m.get('release_tag', '')) and SHA.fullmatch(m.get('source_commit', '')), 'invalid source generation')
            created = datetime.fromisoformat(m['created_at'].replace('Z', '+00:00'))
            require(created.tzinfo is not None and created <= datetime.now(timezone.utc), 'invalid publication date')
            for key, count, pattern in (('company_ciks', 'company_profiles', r'[0-9]{10}'),
                                         ('unresolved_listing_keys', 'unresolved_listings', r'[0-9a-f]{32}')):
                values = m[key]
                require(isinstance(values, list) and 0 <= len(values) <= 50_000 and len(values) == m[count], 'invalid inventory count')
                require(all(isinstance(x, str) and re.fullmatch(pattern, x) for x in values), 'invalid inventory identity')
                require(values == sorted(set(values)), 'ambiguous inventory')
            require(0 <= m['financial_profiles'] <= m['company_profiles'] and m['reviewed_generated_profiles'] == 0, 'invalid review boundary')
            self.publication = {**m, 'commit': commit, 'company_ciks': frozenset(m['company_ciks']),
                                'unresolved_listing_keys': frozenset(m['unresolved_listing_keys'])}
            self.status = 'ready'
            self.last_success_at = datetime.now(timezone.utc).isoformat()
        except Exception:
            self.status = 'degraded'

    def summary(self):
        m = self.publication
        result = {'status': self.status, 'last_success_at': self.last_success_at, 'available': m is not None}
        if m:
            result.update({k: m[k] for k in ('commit', 'release_tag', 'created_at', 'company_profiles',
                                           'financial_profiles', 'unresolved_listings', 'reviewed_generated_profiles')})
            result['index_url'] = f"https://github.com/{REPO}/blob/{m['commit']}/brain/INDEX.md"
            result['download_url'] = f"https://github.com/{REPO}/archive/{m['commit']}.zip"
        return result

    def document(self, *, cik=None, listing_key=None, release_tag=None):
        m = self.publication
        if not m:
            return {'available': False}
        if cik in m['company_ciks']:
            path = f'brain/companies/{cik}/README.md'
        elif listing_key in m['unresolved_listing_keys']:
            path = f'brain/unmapped/{listing_key}.md'
        else:
            return {'available': False}
        return {'available': True, 'status': 'stub', 'canonical_reviewed': False,
                'created_at': m['created_at'], 'release_tag': m['release_tag'],
                'matches_current_data': m['release_tag'] == release_tag,
                'url': f"https://github.com/{REPO}/blob/{m['commit']}/{path}",
                'raw_url': f"https://raw.githubusercontent.com/{REPO}/{m['commit']}/{path}"}
