# Stock Brain

A structured, source-backed knowledge base for U.S.-listed stocks, with canonical English research and a cited Hebrew/English lookup interface.

The Markdown files are the source of truth. Every company uses the same sections. Sector indexes and the master index are generated from company metadata, so navigation stays consistent as coverage grows.

**Current state (2026-10-18):** all ten company profiles have hash-bound research reviews, with 169 claims and Hebrew translations. A local question-answering interface cites reviewed evidence and shows freshness. Daily disclosure discovery maintains a separate pending-review queue (unattended activation requires a permitted runner; the GitHub-hosted live probe returned HTTP 403); six issuer feeds supplement SEC coverage for all ten companies. Reviews include Codex AI checks, not independent human sign-off. Prices and valuation feeds are not connected. See [the maintenance guide](docs/MAINTENANCE.md) for activation and coverage limits.

## Start here

| Destination | Purpose |
| --- | --- |
| [Master index](INDEX.md) | Browse sectors, companies, and cross-sector themes |
| [Company template](templates/company/README.md) | See the shared research structure |
| [Sector template](templates/sector/README.md) | See the shared sector structure |
| [Research guide](docs/RESEARCH.md) | Source quality, review, and update rules |
| [Data contract](docs/DATA_CONTRACT.md) | Metadata, identifiers, and validation |
| [Research assistant](docs/ASSISTANT.md) | Local interface, Hebrew answers, citations and acceptance results |
| [Ongoing maintenance](docs/MAINTENANCE.md) | Daily discovery, durable queue, review cadence and scan health |
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

The exporter includes only `reviewed` company profiles and explicitly registered reviewed sector research. The reviewed corpus exports 172 chunks: 162 company chunks and 10 sector chunks. Templates, indexes, stubs, drafts, archived profiles, and sector planning prompts are excluded. See the pipeline guide to collect sources or use an explicitly configured model runner.

## What is implemented

- Eleven sector sections, each with a README and its own index.
- One 18-section company format, YAML metadata, source IDs, and review dates.
- Generated master and sector indexes, cross-sector tag navigation, and a JSON catalog.
- Validation of structure, metadata, source references, and review requirements.
- Section-aware JSONL export with company context, evidence, dates, content hashes, and stable section identifiers.
- A local test suite and GitHub Actions validation for changes.
- Ten source-backed evidence packets, ten reviewed profiles (three previous reference reviews and seven new AI source reviews), and two bounded sector guides.
- SEC submissions/company-facts collection, curated IR HTML/PDF sources, content-addressed caching, and disclosure-change detection.
- Provider-neutral model runner protocol, optional Responses API adapter, deterministic metric calculations, and hash-bound review records.
- Twenty development cases and 50 frozen bilingual acceptance cases, with failing retrieval and answer-integrity gates.
- Local Hebrew/English Q&A, exact claim citations, bound translations and freshness indicators.
- Daily SEC/RSS discovery, a persistent review queue and bounded incremental request preparation.

## Use the assistant

```bash
python scripts/serve.py
python scripts/ask.py 'מה עושה אורקל?'
python scripts/evaluate_retrieval.py --cases eval/acceptance-v1.json
python scripts/evaluate_answers.py
```

Open `http://127.0.0.1:8765`. No model API key is needed for lookup, discovery, or evaluation. Optional model drafting requires explicit configuration.

## Next priorities

Triage the initial discovery backlog, add the four missing issuer-feed adapters, and keep source/translation reviews current. Add independent evaluation questions before expanding beyond this bounded lookup interface. Introduce timestamped market data only as a separate, explicitly sourced layer.
