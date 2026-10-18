# RAG design

## Implemented boundary

Stock Brain provides a versioned Markdown corpus, metadata validation, deterministic JSONL chunk export, and bilingual entity-scoped lexical retrieval. A deterministic answer layer selects reviewed claims with source locators and bound Hebrew translations. It does not call an embedding API or install a vector database. See [assistant behavior and evaluation](ASSISTANT.md).

```bash
python scripts/stock_brain.py export --output build/chunks.jsonl
```

Only `reviewed` company profiles and opt-in reviewed sector guides enter the corpus. Managed company reviews bind exact packet/profile hashes; sector entries in `config/sector_research.json` bind exact guide hashes. Stubs, drafts, archives, templates, indexes, and sector planning prompts are excluded. Sections marked `Not available:` or `Not applicable:` are excluded. An empty corpus is valid.

## Chunk contract

| Field | Purpose |
| --- | --- |
| `id` | Company ID, section ID, and part number for upsert identity |
| `document_type`, `document_id` | Company ID or sector ID; sector chunks have no ticker |
| `section_id`, `section_title`, `part` | Section identity and split location |
| `text` | Company/ticker context, section title, research date, and section text |
| `content_sha256` | Detect a content or metadata change before embedding |
| `source_path` | Canonical Markdown path for traceability |
| `ticker`, `ticker_aliases`, `company_name` | Entity lookup and disambiguation |
| `sector`, `industry`, `tags`, `exchange`, `security_type`, `domicile_country`, `cik` | Retrieval filters |
| `as_of`, `updated_at`, `reviewed_at`, `status` | Research freshness and eligibility |
| `sources` | Source records cited anywhere in this section |

The chunk ID is stable for an unchanged section position, and `document_id` remains stable across ticker or sector changes. Paragraph edits can change split boundaries and part counts. On each ingestion, reconcile the complete set of IDs with the new export and delete missing IDs; this also removes companies returned to draft or archived. Never append exports blindly.

The content hash covers the chunk payload, including provenance and filters. The splitter keeps paragraphs together where possible and splits oversized blocks on line or word boundaries. Markdown tables are repeated with their header when split. The default target is 3,000 body characters, not tokens; an indivisible table row with its header may exceed that target, and the contextual prefix adds overhead. Choose and evaluate a tokenizer-specific limit when an embedding model is selected. There is no overlap in this first exporter; neighboring chunks can be fetched by document and section when necessary.

## Retrieval and answer gates

`python scripts/evaluate_retrieval.py` runs the development suite; `--cases eval/acceptance-v1.json` runs the frozen bilingual suite. Failed score thresholds now return nonzero. Use `--report-only` explicitly for exploratory comparisons. External predictions and gold evidence are checked for valid IDs and source references.

`config/query_language.json` defines Hebrew/English issuer aliases, known uncovered issuers, subject patterns and unsupported-query guards. Ranking is scoped to resolved companies, with comparison coverage reserved for each company. Unknown comparison partners, absent evidence, unsupported periods and live-market requests abstain. These are heuristics, not a general entity resolver.

The answer layer in `scripts/answering.py` selects exact packet claims behind the reviewed export, preserves their dates/basis, and validates citations. Missing or outdated translations fail closed. Independent factual truth and semantic entailment remain editorial responsibilities. [The assistant guide](ASSISTANT.md) documents the first-run failures, subsequent fixes, and honest scope of the acceptance reports.

For future hybrid retrieval, pin each export to a Git commit, reconcile deleted IDs, preserve issuer/date/status filters, and compare on newly held-out questions. Retrieved source text is untrusted data; never execute instructions embedded in a profile, filing or feed.
