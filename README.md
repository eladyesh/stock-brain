# Stock Brain

A structured, source-backed knowledge base for U.S.-listed stocks, written in English and designed for a future retrieval-augmented generation (RAG) system.

The Markdown files are the source of truth. Every company uses the same sections. Sector indexes and the master index are generated from company metadata, so navigation stays consistent as coverage grows.

**Current state (2026-10-18):** ten sourced company profiles: MSFT, MU and AVAV are reviewed dated snapshots; ORCL, PLTR, NVDA, AMD, AVGO, LMT and RTX remain drafts. Two bounded sector guides are reviewed. The pipeline collects primary sources, prepares evidence requests, renders drafts, validates reviews, and proposes incremental updates. An English retrieval baseline has 20 development questions. This is not a live market-data feed or a deployed question-answering application. The pilot reviews were performed by Codex with a separate evidence-checking agent, not human sign-off.

## Start here

| Destination | Purpose |
| --- | --- |
| [Master index](INDEX.md) | Browse sectors, companies, and cross-sector themes |
| [Company template](templates/company/README.md) | See the shared research structure |
| [Sector template](templates/sector/README.md) | See the shared sector structure |
| [Research guide](docs/RESEARCH.md) | Source quality, review, and update rules |
| [Data contract](docs/DATA_CONTRACT.md) | Metadata, identifiers, and validation |
| [RAG design](docs/RAG.md) | Chunk export and the future retrieval layer |
| [Research pipeline](docs/PIPELINE.md) | Collect, draft, review, and update in small batches |
| [Pilot results](docs/PILOT.md) | Coverage, validation, collection timing, and limitations |
| [Evidence contract](docs/EVIDENCE_PACKET.md) | Claim locators, metric definitions, and review binding |
| [Contributing](CONTRIBUTING.md) | Add, research, validate, and update a company |

## Organization

| Path | Contents |
| --- | --- |
| `README.md` | Project overview |
| `INDEX.md` | Generated master index |
| `sectors/<sector>/README.md` | Uniform sector research guide |
| `sectors/<sector>/INDEX.md` | Generated company index for that sector |
| `sectors/<sector>/companies/<TICKER>/README.md` | One canonical company profile |
| `config/` | Sector taxonomy and ordered company sections |
| `templates/` | Canonical starting templates |
| `data/catalog.json` | Generated machine-readable company catalog |
| `scripts/stock_brain.py` | Add, validate, index, and export commands |
| `scripts/research_company.py` | Source collection and evidence/review workflow |
| `research/` | Evidence packets, review records, and compact source-state checkpoints |
| `eval/` | Source-backed development questions and retrieval results |
| `build/` | Local generated retrieval output; excluded from Git |

A company has one primary sector. Tags such as `ai`, `defense`, or `data-centers` connect companies across sectors without duplicating their research. The 11 top-level sector names follow the broad [GICS sector structure](https://www.msci.com/indexes/index-resources/gics); individual company classifications are research decisions, not a licensed GICS constituent dataset.

Initial scope means common stocks and ADRs listed on Nasdaq, NYSE, or NYSE American, including listed REIT common shares. U.S.-listed does not necessarily mean U.S.-domiciled. ETFs, funds, OTC securities, private companies, and non-U.S. listings are outside this initial scope. There is no implicit claim of complete market coverage.

## Quick start

Requires Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/stock_brain.py check
```

Inspect the populated pilot and validate its evidence:

```bash
python scripts/research_company.py audit
python scripts/evaluate_retrieval.py
```

After editing research, rebuild and validate:

```bash
python scripts/stock_brain.py build
python scripts/stock_brain.py check
python -m unittest discover -s tests -v
python scripts/stock_brain.py export --output build/chunks.jsonl
```

The exporter includes only `reviewed` company profiles and explicitly registered reviewed sector research. The pilot exports 59 chunks: 49 company chunks and 10 sector chunks. Templates, indexes, stubs, drafts, archived profiles, and sector planning prompts are excluded. See the pipeline guide to collect sources or use an explicitly configured model runner.

## What is implemented

- Eleven sector sections, each with a README and its own index.
- One 18-section company format, YAML metadata, source IDs, and review dates.
- Generated master and sector indexes, cross-sector tag navigation, and a JSON catalog.
- Validation of structure, metadata, source references, and review requirements.
- Section-aware JSONL export with company context, evidence, dates, content hashes, and stable section identifiers.
- A local test suite and GitHub Actions validation for changes.
- Ten source-backed evidence packets, three separately audited reference profiles, and two bounded sector guides.
- SEC submissions/company-facts collection, curated IR HTML/PDF sources, content-addressed caching, and disclosure-change detection.
- Provider-neutral model runner protocol, optional Responses API adapter, deterministic metric calculations, and hash-bound review records.
- Twenty retrieval/abstention development cases with a reproducible lexical baseline.

## Next stages

1. Independently review the seven drafts and close their recorded research gaps.
2. Expand in cohorts of three to five issuers while monitoring collection and review effort.
3. Add a held-out evaluation set, then compare embeddings/hybrid retrieval against the lexical baseline.
4. Build cited question answering and evaluate answer factuality separately from retrieval.

Local validation, collection and retrieval evaluation need no model API key. Automated model drafting is opt-in and requires explicit configuration; no scheduled job or paid request is enabled by default.
