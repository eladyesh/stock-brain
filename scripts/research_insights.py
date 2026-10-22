"""Validate explicitly reviewed thesis comparisons before exporting them to the desk."""
from datetime import date
import json
from pathlib import Path
from urllib.parse import urlparse
import research_pipeline as pipeline
import stock_brain as kb


def load_thesis(root, ticker):
    path = Path(root) / 'research' / 'thesis' / (ticker + '.json')
    if not path.exists():
        return None
    value = json.loads(path.read_text(encoding='utf-8'))
    if value.get('schema_version') != 1 or value.get('ticker') != ticker:
        raise ValueError('Invalid thesis identity: ' + ticker)
    date.fromisoformat(value['as_of'])
    if value.get('packet_sha256'):
        if pipeline.digest(pipeline.managed_packet_path(Path(root), ticker).read_bytes()) != value['packet_sha256']:
            raise ValueError('Thesis packet binding is stale: ' + ticker)
    if value.get('profile_sha256'):
        profile = next((doc for doc in kb.documents(Path(root)) if doc.metadata.get('ticker') == ticker), None)
        if profile is None or pipeline.digest(profile.path.read_bytes()) != value['profile_sha256']:
            raise ValueError('Thesis profile binding is stale: ' + ticker)
    sources = {s['id']: s for s in value.get('sources', [])}
    if not sources or len(sources) != len(value['sources']):
        raise ValueError('Missing or duplicate thesis sources: ' + ticker)
    for source in sources.values():
        parsed = urlparse(source.get('url', ''))
        if parsed.scheme != 'https' or not parsed.netloc or not source.get('title'):
            raise ValueError('Invalid thesis source: ' + ticker)
        published = source.get('published_at') or source.get('published_date') or source.get('date')
        if published and str(published)[:10] > value['as_of']:
            raise ValueError('Thesis source after information cutoff: ' + ticker)
    changes = value.get('changes', [])
    ids = set()
    for change in changes:
        if not change.get('id') or change['id'] in ids:
            raise ValueError('Missing or duplicate thesis change ID: ' + ticker)
        ids.add(change['id'])
        for side in ('before', 'after'):
            item = change.get(side)
            if not isinstance(item, dict):
                raise ValueError('Thesis comparison needs both sides: ' + ticker)
            refs = item.get('source_ids') or ([item['source_id']] if item.get('source_id') else [])
            if not refs or any(ref not in sources for ref in refs):
                raise ValueError('Unbound thesis evidence: ' + ticker)
            if not (item.get('locator') or item.get('locators')):
                raise ValueError('Missing thesis evidence locator: ' + ticker)
            if not item.get('text_en') or not item.get('text_he'):
                raise ValueError('Missing bilingual thesis comparison: ' + ticker)
        if not change.get('interpretation_en') or not change.get('interpretation_he'):
            raise ValueError('Missing labelled thesis interpretation: ' + ticker)
    # These are AI-reviewed comparisons; this gate checks integrity, not independent factual truth.
    value['review_type'] = 'ai'
    value['comparison_count'] = len(changes)
    return value
