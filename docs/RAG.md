# RAG design

## Implemented boundary

Stock Brain currently provides a versioned Markdown corpus, metadata validation, navigation indexes, and a deterministic JSONL chunk export. It does not call an embedding API, install a vector database, retrieve results, or answer questions.

```bash
python scripts/stock_brain.py export --output build/chunks.jsonl
```

Only `reviewed` company profiles enter the corpus. Stubs, drafts, archives, templates, generated indexes, and sector planning prompts are excluded. Sections explicitly marked `Not available:` or `Not applicable:` are excluded. An empty corpus is a valid result and is reported as zero chunks.

## Chunk contract

| Field | Purpose |
| --- | --- |
| `id` | Company ID, section ID, and part number for upsert identity |
| `document_id` | Immutable company ID |
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

## Retrieval layer to add later

1. Pin an export to a Git commit and store that revision alongside ingestion metadata.
2. Resolve exact tickers, aliases, and company names before semantic retrieval.
3. Combine lexical retrieval with embeddings and metadata filters for company, sector, theme, date, and status.
4. Rank candidates and optionally fetch neighboring section chunks for context.
5. Answer only from retrieved evidence, citing the company file and original sources.
6. State missing coverage, conflicts, and stale evidence explicitly. Do not answer a current-price question with an old snapshot.

Example future questions include: "Which covered companies depend on data-center spending?", "How do these two companies make money?", and "Which risks could invalidate this growth thesis?" Sector folders alone cannot answer cross-sector questions; the tags and sourced relationship sections support them.

## Evaluation before deployment

Create a small set of source-backed questions with expected company IDs, sections, and evidence. Include cross-sector retrieval, ambiguous symbols, dated financial figures, contradictory sources, unavailable companies, and questions that cannot be answered. Measure retrieval coverage and citation support separately from answer fluency. A fluent unsupported answer is a failure.

The source files and retrieved passages are untrusted data. A future answerer must not execute instructions embedded in a company profile or a linked source. Keep system instructions separate from retrieved content.
