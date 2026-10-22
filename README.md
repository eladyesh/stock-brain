# Stock Brain

A structured, source-backed knowledge base for U.S.-listed stocks, with canonical English research and a cited Hebrew/English lookup interface.

The Markdown files are the source of truth. Every company uses the same sections. Sector indexes and the master index are generated from company metadata, so navigation stays consistent as coverage grows.

**Current state (2026-10-19):** ten hash-bound AI-reviewed company profiles with 179 claims and Hebrew translations; exact metric/period/basis gates; 170 source-backed financial periods (five years and twelve quarters per company); dated market snapshots; and a Hebrew research desk with history, comparisons, assumption-driven scenarios and disclosure triage. Reviews include AI checks, not independent human sign-off. Missing data and normalization conflicts remain explicit. Oracle announcement access remains blocked in this runtime.

**Standalone research app:** `site/` is served by the public Python application in `scripts/serve_public.py`. Collection runs on the server; GitHub Actions backs up validated checkpoints to `automation/research-data`. No ChatGPT account, Sites deployment, model API key, or paid data subscription is required. See [standalone deployment](docs/STANDALONE.md), [desk behavior](docs/DESK.md), and [financial definitions](docs/FINANCIAL_HISTORY.md). The ChatGPT daily task has been disabled. The legacy GitHub disclosure collector remains paused because of source-access failures.

## Start here

| Destination | Purpose |
| --- | --- |
| [Master index](INDEX.md) | Browse sectors, companies, and cross-sector themes |
| [Company template](templates/company/README.md) | See the shared research structure |
| [Sector template](templates/sector/README.md) | See the shared sector structure |
| [Research guide](docs/RESEARCH.md) | Source quality, review, and update rules |
| [Data contract](docs/DATA_CONTRACT.md) | Metadata, identifiers, and validation |
| [Research assistant](docs/ASSISTANT.md) | Local interface, Hebrew answers, citations and acceptance results |
| [Exact numerical answers](docs/EXACT_ANSWERS.md) | Calendar/fiscal period matching and sourced historical lookup |
| [Hosted research desk](docs/DESK.md) | Financial history, comparisons, scenario assumptions and build instructions |
| [Standalone application](docs/STANDALONE.md) | Public server, scheduled collection, backup and recovery |
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
- Daily SEC/RSS/public Q4 discovery, source diagnostics, a persistent review queue, source-bound triage decisions and bounded incremental request preparation.
- Exact-definition SEC history, source-bound growth/margin answers, verified NVDA/AVGO split bridges, explicit remaining comparability flags, public market snapshots and assumption-based valuation sensitivity.
- A public Hebrew web application, a server-side collector and a data-only backup branch; no runtime model API key is required.

## Run the public application

```bash
python -m pip install -r requirements-web.txt
python scripts/serve_public.py
```

Open `http://localhost:10000`. For the existing production checkpoint, set `STOCK_BRAIN_BOOTSTRAP_GITHUB=1` before the first start. See [deployment and recovery](docs/STANDALONE.md) for the full configuration.

## Use the assistant

```bash
python scripts/serve.py
python scripts/ask.py 'מה עושה אורקל?'
python scripts/evaluate_retrieval.py --cases eval/acceptance-v1.json
python scripts/evaluate_answers.py
```

Open `http://127.0.0.1:8765`. No model API key is needed for lookup, discovery, or evaluation. Optional model drafting requires explicit configuration.

## Next priorities

Both critical AMD/NVDA updates are integrated. Resolve the remaining substantive disclosure backlog and 77 financial QA flags before expanding the universe. See [financial remediation](docs/FINANCIAL_REMEDIATION.md) for exact source tasks. Deepen issuer-specific moat, customer concentration, management incentives and measurable thesis-breaker work. Add independent human review and holdout questions. Consensus, forward valuation and a general language-model assistant remain separate future capabilities; scenario calculations do not supply them.
