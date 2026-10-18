"""Conservative bilingual retrieval over reviewed, dated research.

This is a deterministic small-corpus retriever, not a general translator.
Entity coverage and unsupported requests are checked before ranking.
"""
from collections import Counter
from datetime import date
import json
import math
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
STOP = set('a an the is are was were of for in and to what which how does do its by as on with from s me give explain describe summarize tell about main reported report company companies corporation inc corp current latest has have versus vs compare'.split())


def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFKC', text).casefold()
                   if not '\u0591' <= c <= '\u05c7').replace('’', "'")


def tokens(text):
    return [w for w in re.findall(r'[a-z0-9]+|[\u05d0-\u05ea]+', normalize(text)) if w not in STOP]


def matched(text, phrase):
    # Hebrew prepositions may be attached to an issuer name.
    prefix = r'(?:[ובלמשכ])?' if re.search(r'[\u05d0-\u05ea]', phrase) else ''
    return re.search(r'(?<!\w)' + prefix + re.escape(normalize(phrase)) + r'(?!\w)', text) is not None


def settings(root=None):
    path = (root or ROOT) / 'config/query_language.json'
    return json.loads(path.read_text(encoding='utf-8'))


def resolve_entities(question, universe, records, config):
    q = normalize(question)
    aliases = {c['ticker']: {c['ticker'], c['company_name'],
               re.sub(r'\b(?:Corporation|Technologies|Technology|Inc|Corp)\.?', '', c['company_name']).strip(' ,.')}
               for c in universe}
    for r in records:
        if r.get('ticker') in aliases:
            aliases[r['ticker']].update(r.get('ticker_aliases', []))
    for ticker, names in config['issuer_aliases'].items():
        aliases.setdefault(ticker, {ticker}).update(names)
    mentions = {t for t, names in aliases.items() if any(n and matched(q, n) for n in names)}
    unknown = {s.upper() for s in re.findall(r'\$([A-Za-z][A-Za-z0-9.\-]{0,11})\b', question)} - set(aliases)
    acronyms = set(config['non_ticker_acronyms'])
    capitalized = set(re.findall(r'\b[A-Z]{2,5}\b', question)) - set(aliases) - acronyms
    comparison = bool(re.search(r'\b(?:compare|versus|vs)\b|השוו|השוה|השוואה|לעומת', q))
    # Program acronyms inside a single-issuer question are not extra issuers.
    if not mentions or comparison:
        unknown.update(capitalized)
    basis_comparison = bool(re.search(r'gaap|adjusted|non.?gaap|מתואם|מתואמ', q))
    if comparison and len(mentions) < 2 and not basis_comparison:
        unknown.add('unresolved comparison counterparty')
    return sorted(mentions), sorted(unknown)


def refuse(reason, code, entities=()):
    return {'abstain': True, 'reason': reason, 'reason_code': code,
            'chunk_ids': [], 'entities': list(entities), 'section_ids': []}


def retrieve(question, records, universe, top_k=6, root=None):
    if not isinstance(question, str) or not question.strip() or len(question) > 4000:
        return refuse('Provide a research question of 1–4000 characters.', 'invalid_question')
    if top_k < 1:
        raise ValueError('top_k must be positive')
    config = settings(root)
    q = normalize(question)
    entities, unknown = resolve_entities(question, universe, records, config)
    if unknown:
        return refuse('An issuer or comparison counterparty needs clarification.', 'unknown_issuer', entities)
    for rule in config['unsupported']:
        if re.search(rule['pattern'], q):
            return refuse(rule['reason'], rule['code'], entities)
    covered = {r.get('ticker') for r in records if r.get('document_type') == 'company'}
    relationship = bool(re.search(r'\b(?:relationship|collaboration|partnership|supplier|customer)\b|הקשר|קשר בין|שותפ|ספק של', q))
    missing = set(entities) - covered
    if missing and not (relationship and set(entities) & covered):
        return refuse('Requested issuer lacks reviewed coverage.', 'unreviewed_issuer', entities)
    hints = []
    expanded = []
    for section, rule in config['sections'].items():
        if any(re.search(pattern, q) for pattern in rule['patterns']):
            hints.append(section)
            expanded.extend(rule['search_terms'].split())
    if not entities:
        # Sector/theme searches require an explicit scope; do not silently guess an issuer.
        theme_terms = {tag for r in records for tag in r.get('tags', []) if matched(q, tag)}
        theme_terms.update(config['themes'][term] for term in config.get('themes', {}) if matched(q, term))
        if not theme_terms:
            return refuse('Specify a covered company, sector, or theme.', 'missing_scope')
        candidates = [r for r in records if theme_terms & set(r.get('tags', []))]
    else:
        candidates = [r for r in records if r.get('ticker') in entities]
    if not candidates:
        return refuse('No reviewed evidence exists for this scope.', 'no_evidence', entities)
    years = re.findall(r'\b(?:19|20)\d{2}\b', q)
    if years and 'financial-performance' in hints:
        candidates = [r for r in candidates if all(y in r['text'].split('\n\n', 1)[-1] for y in years)]
        if not candidates:
            return refuse('The requested financial period is not in the reviewed evidence.', 'unsupported_period', entities)
    # Ranking excludes metadata headers, so an issuer symbol alone cannot create a hit.
    docs = [tokens(r['text'].split('\n\n', 1)[-1]) for r in candidates]
    if not docs:
        return refuse('No eligible evidence.', 'no_evidence', entities)
    freq = Counter(w for doc in docs for w in set(doc))
    average = max(1, sum(map(len, docs)) / len(docs))
    issuer_terms = {w for c in universe for w in tokens(c['company_name'] + ' ' + c['ticker'])}
    query = [w for w in tokens(question) if w not in issuer_terms] + expanded
    scored = []
    for record, doc in zip(candidates, docs):
        counts = Counter(doc)
        score = 0.0
        for term in set(query):
            tf = counts[term]
            if tf:
                idf = math.log(1 + (len(docs) - freq[term] + .5) / (freq[term] + .5))
                score += idf * tf * 2.2 / (tf + 1.2 * (.25 + .75 * len(doc) / average))
        if record.get('section_id') in hints:
            score += 20
        if score > 0:
            scored.append((score, record))
    ranked = sorted(scored, key=lambda pair: (-pair[0], pair[1]['id']))
    chosen = []
    # Reserve evidence for each issuer in a comparison instead of crowding one out.
    for ticker in entities:
        first = next((r for _, r in ranked if r.get('ticker') == ticker), None)
        if first and first['id'] not in chosen:
            chosen.append(first['id'])
    if len(chosen) > top_k:
        return refuse('Increase the evidence limit or compare fewer companies.', 'too_many_issuers', entities)
    for _, record in ranked:
        if record['id'] not in chosen and len(chosen) < top_k:
            chosen.append(record['id'])
    if not chosen:
        return refuse('No matching reviewed evidence was found.', 'no_evidence', entities)
    return {'abstain': False, 'reason': None, 'reason_code': None, 'chunk_ids': chosen,
            'entities': entities, 'section_ids': hints}
