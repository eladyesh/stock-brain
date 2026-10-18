"""Cited, deterministic answers from reviewed claims and bound translations.

No runtime model request, numeric synthesis, or ungrounded completion is used.
Source review is editorial; hash and answer checks establish identity, not truth.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import time

import disclosure_monitor
import research_pipeline as pipeline
import retrieval
import stock_brain as kb

HE_REASONS = {
    'invalid_question': 'יש להזין שאלת מחקר באורך של עד 4,000 תווים.',
    'unknown_issuer': 'לא זוהתה בוודאות אחת החברות. יש לציין שם חברה או טיקר ולהבהיר את ההשוואה.',
    'unreviewed_issuer': 'לפחות אחת החברות המבוקשות אינה כלולה במחקר שנבדק.',
    'live_market_data': 'אין במאגר מקור עדכני למחיר מניה, לשווי שוק או למכפילים.',
    'unsourced_forecast': 'אין במאגר מקור לתחזית אנליסטים, למחיר יעד או לשווי הוגן.',
    'investment_action': 'הכלי מספק מחקר מבוסס מקורות; אין בו בסיס להמלצת קנייה או מכירה אישית.',
    'unsupported_period': 'התקופה הכספית המבוקשת אינה מופיעה בראיות שנבדקו.',
    'missing_scope': 'יש לציין חברה מכוסה או נושא מחקר מוגדר.',
    'no_evidence': 'לא נמצאה ראיה בדוקה שעונה על השאלה.',
    'translation_missing': 'אין תרגום בדוק ועדכני לראיה המתאימה. אפשר לשאול באנגלית.',
    'freshness_unverified': 'לא ניתן להציג את המידע כעדכני: קיימים פרסומים שטרם נבדקו או שחסרה בדיקת עדכניות תקפה.',
    'too_many_issuers': 'יש לצמצם את מספר החברות בהשוואה.',
}
HE_KINDS = {'reported': 'דיווח החברה', 'management_guidance': 'תחזית או צפי הנהלה',
            'interpretation': 'פרשנות מחקרית', 'derived': 'חישוב מנתונים מדווחים'}


def claim_hash(packet, claim):
    ids = {e['source_id'] for e in claim['evidence']}
    content = {'claim': claim, 'as_of': packet['as_of'],
               'sources': [s for s in packet['sources'] if s['id'] in ids]}
    return hashlib.sha256(json.dumps(content, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def numbers(text):
    return sorted(set(re.findall(r'\d+(?:[,\.]\d+)*(?:%?)', text)))


def translated_claim(root, packet, claim):
    path = root / 'research/locales/he' / (packet['ticker'] + '.json')
    if not path.exists():
        return None
    data = pipeline.read_json(path)
    row = data.get('claims', {}).get(claim['id'])
    if not row or row.get('source_sha256') != claim_hash(packet, claim):
        return None
    kb.need(kb.scalar(row.get('text')) and kb.scalar(data.get('reviewer')), 'translation needs text and reviewer')
    kb.need(numbers(row['text']) == numbers(claim['text']), f"{packet['ticker']} {claim['id']}: translation numeric tokens differ")
    kb.need(row.get('translated_text_sha256') == pipeline.digest(row['text']), 'translation changed after its recorded review')
    return row['text']


def answer(question, root=None, language='auto', monitor_report=None):
    root = Path(root or kb.ROOT).resolve()
    started = time.monotonic()
    kb.need(language in {'auto', 'he', 'en'}, 'language must be auto, he or en')
    language = ('he' if re.search(r'[\u05d0-\u05ea]', question) else 'en') if language == 'auto' else language
    records = kb.export_records(root)
    result = retrieval.retrieve(question, records, pipeline.universe(root), top_k=8, root=root)
    output = {'schema_version': 1, 'question': question, 'language': language, 'mode': 'reviewed_claims',
              'abstain': result['abstain'], 'reason_code': result['reason_code'], 'reason': result['reason'],
              'statements': [], 'sources': [], 'coverage': [], 'limitations': [], 'retrieval': result,
              'metrics': {'model_api_calls': 0, 'model_cost_usd': 0, 'research_review_cost_usd': None}}
    def finish(code=None, reason=None):
        if code:
            output.update(abstain=True, reason_code=code, reason=reason, statements=[], sources=[])
        if output['abstain'] and language == 'he':
            output['reason'] = HE_REASONS.get(output['reason_code'], HE_REASONS['no_evidence'])
        output['metrics']['elapsed_seconds'] = round(time.monotonic() - started, 4)
        return output
    if result['abstain']:
        return finish()
    by_id = {r['id']: r for r in records}
    candidates = [by_id[i] for i in result['chunk_ids'] if by_id[i].get('ticker')]
    if not candidates:
        return finish('no_evidence', 'No claim-level company evidence is available for this question.')
    if monitor_report is None:
        path = root / 'build/monitoring/latest.json'
        if not path.exists():
            path = root / 'research/monitoring/latest.json'
        monitor_report = pipeline.read_json(path) if path.exists() else None
    requested_current = bool(re.search(r'\b(?:today|current|latest|right now)\b|היום|כרגע|עדכני|האחרון|האחרונה', question, re.I))
    chosen = []
    tickers = list(dict.fromkeys(r['ticker'] for r in candidates))
    for ticker in tickers:
        ticker_records = [r for r in candidates if r['ticker'] == ticker]
        packet = pipeline.read_json(pipeline.managed_packet_path(root, ticker))
        # Editorial export gate already checked the packet/profile review binding.
        state = disclosure_monitor.freshness(root, ticker, monitor_report)
        output['coverage'].append({'ticker': ticker, 'as_of': packet['as_of'], 'freshness': state})
        locale_path = root / 'research/locales/he' / (ticker + '.json')
        gaps = pipeline.read_json(locale_path).get('gaps', []) if language == 'he' and locale_path.exists() else []
        for index, gap in enumerate(packet['gaps']):
            translated = gaps[index] if index < len(gaps) else {}
            if translated.get('source_sha256') == pipeline.digest(gap) and translated.get('translated_text_sha256') == pipeline.digest(translated.get('text', '')):
                gap = translated['text']
            output['limitations'].append({'ticker': ticker, 'text': gap})
        if requested_current and state['status'] != 'checked':
            return finish('freshness_unverified', 'Currentness cannot be established; request the dated snapshot or refresh research.')
        matching = [r for r in ticker_records if r['section_id'] in result['section_ids']]
        # A recognized subject must not silently fall back to another section.
        if result['section_ids'] and not matching:
            return finish('no_evidence', 'The requested research section is unavailable.')
        selection = matching[:2] if matching else ticker_records[:1]
        for record in selection:
            data = packet['sections'][record['section_id']]
            for claim in data.get('claims', []):
                if 'relationships-and-themes' in result['section_ids'] and len(result['entities']) > 1:
                    aliases = retrieval.settings(root)['issuer_aliases']
                    others = [name for t in result['entities'] if t != ticker for name in [t] + aliases.get(t, [])]
                    if not any(retrieval.matched(retrieval.normalize(claim['text']), name) for name in others):
                        continue
                text = claim['text'] if language == 'en' else translated_claim(root, packet, claim)
                if text is None:
                    return finish('translation_missing', 'The matched claim has no reviewed current translation.')
                sources = {s['id']: s for s in packet['sources']}
                refs = []
                for evidence in claim['evidence']:
                    source = sources[evidence['source_id']]
                    ref = ticker + ':' + source['id']
                    refs.append({'id': ref, 'locator': evidence['locator']})
                    if ref not in {s['id'] for s in output['sources']}:
                        output['sources'].append({**source, 'id': ref, 'ticker': ticker})
                chosen.append({'ticker': ticker, 'claim_id': claim['id'], 'section_id': record['section_id'],
                               'text': text, 'original_text': claim['text'], 'kind': claim['kind'],
                               'as_of': packet['as_of'], 'source_sha256': claim_hash(packet, claim), 'citations': refs})
    output['statements'] = list({(s['ticker'], s['claim_id']): s for s in chosen}.values())
    output['coverage'] = [c for c in output['coverage'] if any(s['ticker'] == c['ticker'] for s in output['statements'])]
    if not output['statements']:
        return finish('no_evidence', 'No claim supports the question.')
    validate_answer(output, root)
    return finish()


def validate_answer(output, root):
    """Reject injected statements, changed numbers, unknown claims and wrong citations."""
    if output['abstain']:
        kb.need(not output['statements'] and not output['sources'], 'abstention contains factual output')
        return
    kb.need(bool(output['statements']), 'answer has no evidence')
    supplied = {s['id']: s for s in output['sources']}
    for statement in output['statements']:
        packet = pipeline.read_json(pipeline.managed_packet_path(root, statement['ticker']))
        claim = next((c for c in packet['sections'][statement['section_id']].get('claims', []) if c['id'] == statement['claim_id']), None)
        kb.need(claim is not None, 'answer cites an unknown claim')
        expected = claim['text'] if output['language'] == 'en' else translated_claim(root, packet, claim)
        kb.need(expected is not None and statement['text'] == expected, 'answer differs from reviewed evidence')
        kb.need(statement['source_sha256'] == claim_hash(packet, claim) and statement['as_of'] == packet['as_of'], 'answer evidence version mismatch')
        kb.need(statement['kind'] == claim['kind'], 'answer changed reported/guidance/interpretation basis')
        expected_refs = [{'id': statement['ticker'] + ':' + e['source_id'], 'locator': e['locator']} for e in claim['evidence']]
        kb.need(statement['citations'] == expected_refs, 'answer citation mismatch')
        for source in packet['sources']:
            ref = statement['ticker'] + ':' + source['id']
            if ref in {r['id'] for r in expected_refs}:
                kb.need(supplied.get(ref) == {**source, 'id': ref, 'ticker': statement['ticker']}, 'answer altered source provenance')


def markdown(output):
    if output['abstain']:
        return output['reason'] + '\n'
    he = output['language'] == 'he'
    lines = []
    for coverage in output['coverage']:
        label = 'מחקר נכון ל־' if he else 'Research as of '
        lines.append(f"**{coverage['ticker']} — {label}{coverage['as_of']}**")
        state = coverage['freshness']
        if state['status'] != 'checked':
            lines.append('עדכניות מול פרסומים חדשים לא אושרה.' if he else 'Currentness against new disclosures is not confirmed.')
        for row in output['statements']:
            if row['ticker'] == coverage['ticker']:
                kind = HE_KINDS[row['kind']] if he else row['kind'].replace('_', ' ')
                refs = ' '.join('[' + c['id'] + ']' for c in row['citations'])
                lines += ['', f"- **{kind}:** {row['text']} {refs}"]
        lines.append('')
    lines += ['**מקורות**' if he else '**Sources**', '']
    for source in output['sources']:
        locators = sorted({c['locator'] for row in output['statements'] for c in row['citations'] if c['id'] == source['id']})
        lines.append(f"- [{source['id']}] [{source['title']}]({source['url']}) — {'; '.join(locators)}. {'פורסם' if he else 'Published'}: {source['published_at'] or ('לא ידוע' if he else 'unknown')}.")
    lines += ['', '**מידע חסר**' if he else '**Research gaps**', '']
    for gap in output['limitations']:
        lines.append(f"- {gap['ticker']}: {gap['text']}")
    return '\n'.join(lines) + '\n'
