# RAG design

## Implemented boundary

Stock Brain provides a versioned Markdown corpus, metadata validation, deterministic JSONL chunk export, and a small English lexical retrieval/evaluation baseline. It does not call an embedding API, install a vector database, or generate answers.

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

## Baseline and retrieval layer to extend

Run `python scripts/evaluate_retrieval.py` to evaluate `eval/questions.json`, writing `build/evaluation.json`. Supply `--predictions path.json` to evaluate another retriever's mapping from case ID to `{"abstain":false,"chunk_ids":["exported-id"]}`. Unknown or duplicate chunk IDs are rejected. Gold evidence must exist in the reviewed corpus. The command reports failures but does not enforce a score threshold; CI validates the corpus and evaluation structure.

The baseline uses BM25-style English tokens and exact issuer-name/ticker hints, with guards for missing reviewed coverage, unresolved symbols, live prices and consensus. A question about a relationship can retrieve evidence from one reviewed counterparty without implying full coverage of the other. Program acronyms within an identified issuer question are not automatically treated as tickers. These are heuristics, not a production entity resolver. Broader multilingual retrieval, ambiguity resolution and answer generation remain open work.

1. Pin an export to a Git commit and store that revision alongside ingestion metadata.
2. Resolve exact tickers, aliases, and company names before semantic retrieval.
3. Combine lexical retrieval with embeddings and metadata filters for company, sector, theme, date, and status.
4. Rank candidates and optionally fetch neighboring section chunks for context.
5. Answer only from retrieved evidence, citing the company file and original sources.
6. State missing coverage, conflicts, and stale evidence explicitly. Do not answer a current-price question with an old snapshot.

Example future questions include: "Which covered companies depend on data-center spending?", "How do these two companies make money?", and "Which risks could invalidate this growth thesis?" Sector folders alone cannot answer cross-sector questions; the tags and sourced relationship sections support them.

## Evaluation before deployment

The committed development set has 15 answerable cases and five abstention cases, including cross-sector comparisons, a supply-chain relationship, dated figures, GAAP versus adjusted results, uncovered/draft companies and unsourced live data. Gold expectations identify company IDs, sections and sources. The current 20/20 result is a small development-set result, not a held-out accuracy estimate. The retriever was developed with these cases visible. Add genuinely held-out questions, conflicting-source cases, sector queries and Hebrew queries before choosing a production retrieval stack. Measure generated-answer and citation accuracy separately; this implementation evaluates neither.

The source files and retrieved passages are untrusted data. A future answerer must not execute instructions embedded in a company profile or a linked source. Keep system instructions separate from retrieved content.
