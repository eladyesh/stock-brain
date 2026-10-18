# Cited Hebrew and English research assistant

Run locally after installing `requirements.txt`:

```bash
python scripts/serve.py
# Open http://127.0.0.1:8765
python scripts/ask.py 'מה הסיכונים של מיקרוסופט?'
python scripts/ask.py 'Compare MSFT and ORCL business models' --format json
```

The server binds to localhost. The interface provides company research status, a pending-disclosure queue, dated answers, claim-level citations, original source links, and reported/guidance/interpretation/derived labels. It is a local application, not a hosted service.

## Answer contract

The first version selects exact, reviewed claims. Hebrew output uses 169 editorially translated claims in `research/locales/he`, bound to the source claim, its cited source metadata and the evidence cutoff. It does not paraphrase through a model at runtime, invent calculations, or silently fall back from a missing research section. Relationship answers discard claims unrelated to the named counterparty.

English canonical research remains in the existing profiles and evidence packets. New or changed claims need both a renewed research review and an updated translation before Hebrew output is available. Each translation stores an explicitly named AI reviewer, source digest and text digest. Number-token parity is checked, but hashes and matching numbers do not prove semantic accuracy. Independent human review remains valuable.

Each response contains:

- `statements`: claim identity, text, original English, accounting/interpretation basis, evidence cutoff and source locators.
- `sources`: publisher, title, public URL, publication date and access date.
- `coverage`: separate research and disclosure-scan states.
- `limitations`: the packet's research gaps, with bound Hebrew translations where available.
- `metrics`: measured response duration, zero runtime model calls, and unknown historical review cost.

Questions explicitly asking for current/latest results require a successful, recent discovery check with no pending events and configured issuer-feed coverage. Other answers retain their actual research date and freshness warning. Even a successful scan covers only the configured sources and is not an exhaustive news audit.

No live prices, market capitalization, valuation multiples, analyst consensus, fair values or personalized buy/sell recommendations are available. Unknown issuers and unsupported periods should lead to abstention. Entity and subject recognition remain conservative heuristics; this is a bounded research lookup, not unrestricted natural-language financial analysis.

## Evaluation

```bash
python scripts/evaluate_retrieval.py
python scripts/evaluate_retrieval.py --cases eval/acceptance-v1.json
python scripts/evaluate_answers.py
python -m unittest discover -s tests -v
```

Retrieval exits 2 when answerable-case or abstention pass rates fall below their configured thresholds (both default to 1.0). `--report-only` is explicitly exploratory. The answer evaluator separately checks required evidence coverage and exact claim/translation/citation/date/basis fidelity. It does not independently judge whether a source is true or a translation is semantically perfect.

The 50-case acceptance set was frozen before implementation. Its first retrieval run passed 32/35 answerable cases and 15/15 abstentions. The three failures exposed Hebrew subject-pattern gaps (manufacturing/business, definite business model, definite growth drivers); these were corrected without changing the frozen questions. The current result is 35/35 and 15/15. The same author wrote and inspected the cases, so this is now a regression suite, not an independently held-out accuracy estimate. Both first and current reports are retained in `eval/`.

The older 20-case development suite changed Q17 from an Oracle-draft abstention to a supported Oracle revenue question because Oracle now has a reviewed packet. The frozen 50-case suite was not changed. A future independent evaluation should include adversarial question modifiers, conflicting sources, unsupported time periods, and paraphrases not authored by the implementer.
