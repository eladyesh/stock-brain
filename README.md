# Stock Brain

A structured, source-backed knowledge base for U.S.-listed stocks, written in English and designed for a future retrieval-augmented generation (RAG) system.

The Markdown files are the source of truth. Every company uses the same sections. Sector indexes and the master index are generated from company metadata, so navigation stays consistent as coverage grows.

**Current state:** the repository contains the knowledge structure and working maintenance tools. Company research has not been populated yet. Empty sectors and unresearched profiles are labeled explicitly. This is not a live market-data feed or a deployed question-answering application.

## Start here

| Destination | Purpose |
| --- | --- |
| [Master index](INDEX.md) | Browse sectors, companies, and cross-sector themes |
| [Company template](templates/company/README.md) | See the shared research structure |
| [Sector template](templates/sector/README.md) | See the shared sector structure |
| [Research guide](docs/RESEARCH.md) | Source quality, review, and update rules |
| [Data contract](docs/DATA_CONTRACT.md) | Metadata, identifiers, and validation |
| [RAG design](docs/RAG.md) | Chunk export and the future retrieval layer |
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

Create a company profile, for example:

```bash
python scripts/stock_brain.py add \
  --ticker MSFT \
  --name "Microsoft Corporation" \
  --sector information-technology \
  --exchange NASDAQ
```

This creates a **stub**, not researched company facts. Fill the profile using the research guide, update its metadata, and rebuild the indexes:

```bash
python scripts/stock_brain.py build
python scripts/stock_brain.py check
python -m unittest discover -s tests -v
python scripts/stock_brain.py export --output build/chunks.jsonl
```

The exporter includes only `reviewed` company profiles. With the initial empty knowledge base it produces zero chunks, successfully and explicitly. Templates, indexes, stubs, drafts, archived profiles, and sector planning prompts are never embedded as company research.

## What is implemented

- Eleven sector sections, each with a README and its own index.
- One 18-section company format, YAML metadata, source IDs, and review dates.
- Generated master and sector indexes, cross-sector tag navigation, and a JSON catalog.
- Validation of structure, metadata, source references, and review requirements.
- Section-aware JSONL export with company context, evidence, dates, content hashes, and stable section identifiers.
- A local test suite and GitHub Actions validation for changes.

## Next stages

1. Choose a coverage universe and research the first companies using primary sources.
2. Expand coverage while keeping unknowns, review status, and source dates explicit.
3. Select embeddings, lexical search, a vector store, and a retrieval evaluation set.
4. Build question answering that cites its evidence and states when information is missing or stale.

No API keys, scheduled scraping, external messaging, paid services, or embedding provider are required for this foundation.
