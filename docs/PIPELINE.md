# Source-first research pipeline

The working unit is one issuer evidence packet, then a canonical Markdown draft, then a source review. Start with cohorts of three to five issuers. Existing pilot coverage and measured limits are in [PILOT.md](PILOT.md).

## 1. Configure the universe and collect

`config/universe.json` records verified ticker, SEC CIK, listing, sector, tags and cohort. `extra_sources` contains curated primary-source URLs such as the actual earnings exhibit, call remarks, proxy or product announcement. Entries can list affected section IDs; unknown event scope triggers broad review. Set `mutable: true` for pages that can change at the same URL. Add newly published IR documents when identified; the collector does not discover arbitrary new press releases automatically.

```bash
export SEC_USER_AGENT='Your research app your-contact@example.com'
python scripts/research_company.py collect --ticker MU --as-of 2026-10-18
python scripts/research_company.py prepare --ticker MU
python scripts/research_company.py batch --group semiconductors --limit 4 --as-of 2026-10-18
```

The SEC collector selects the most recent eligible annual and interim filing, corresponding amendments, and up to three recent event reports by default. `collect --max-events 10` expands that event sample. The cutoff filters by filing/publication date, not fiscal period alone. Foreign-issuer interim disclosures and 6-K contents need manual inspection. Event cover pages do not substitute for earnings exhibits: the manifest flags this explicitly. The pilot universe includes curated earnings sources for all ten issuers.

Downloads use an identifying User-Agent, two requests per second per process, bounded retries and a local content-addressed cache. Run one collector process at a time when scaling; do not multiply workers without a shared rate limiter. SEC submissions/company-facts and mutable IR pages refresh; immutable filing bytes reuse the cache. HTML extraction preserves table-cell boundaries. PDF extraction includes page markers; scanned/image-only PDFs require manual extraction/OCR and are rejected. Extracted financial tables still require source inspection.

Outputs under ignored `build/` include source manifests, raw/text hashes, company-facts JSON, fetch errors, coverage gaps, an update plan, and a budgeted model request. Full copyrighted documents are never committed. A failed required source is reported and prevents the `run` command from calling a model. Prefer a verified SEC exhibit when an IR webpage is unreadable; record the actual alternative URL.

Primary technical references: [SEC data APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [SEC access guidance](https://www.sec.gov/about/developer-resources), [pypdf extraction limits](https://pypdf.readthedocs.io/en/stable/user/extract-text.html).

## 2. Extract an evidence packet

Read [EVIDENCE_PACKET.md](EVIDENCE_PACKET.md). Each material claim has a source and locator. Explicitly distinguish reported results, management guidance, derived values and interpretation. Every financial metric has a fiscal period, unit, currency, basis and source. Unresearched sections remain explicitly unavailable. The collector's excerpts are budgeted, incomplete evidence; use full documents where needed, and never imply that an excerpt covers the whole filing.

A manually researched packet can be rendered without a paid service:

```bash
python scripts/research_company.py draft --packet research/pilot/MU.json
```

This writes only `build/proposals/MU.md`. Add `--apply` after checking the proposal to write the canonical profile as **draft** and persist its packet. Applying new evidence to a reviewed company always demotes it; review is a separate action. Existing immutable company IDs are preserved.

For exact reported XBRL facts:

```bash
python scripts/financial_facts.py build/research/MU/companyfacts.json \
  --concept Revenues --unit USD --start 2025-08-29 --end 2026-09-03 --as-of 2026-10-18
```

A concept may differ by issuer; inspect the company-facts taxonomy first. Missing data fails explicitly. Selection honors the exact period, unit and information cutoff, retains amendment provenance, and rejects conflicting latest values. It does not silently convert YTD into a quarter. Growth and margin formulas are evaluated in Python from compatible inputs, not supplied as model-calculated values. SEC company-facts coverage is not a replacement for segment/custom/non-GAAP tables.

## 3. Optional model drafting

`run` collects and prepares by default. A model is called only with an explicit runner configuration:

```bash
python scripts/research_company.py run --ticker MU --as-of 2026-10-18
# Set OPENAI_API_KEY securely in your environment and select a model you can access.
export OPENAI_MODEL='your-selected-model'
python scripts/research_company.py run --ticker MU --as-of 2026-10-18 \
  --runner config/openai-runner.example.json --force
```

The example invokes `scripts/openai_runner.py`, using the [Responses API](https://platform.openai.com/docs/api-reference/responses/create), JSON output mode and local evidence validation. It has no default model, key, price assumption or automatic paid retry. It rejects refusals and incomplete output. Add `--apply` to save a successful result as a canonical draft; otherwise it stays a proposal. `--force` deliberately prepares/runs even with no disclosure changes. It never bypasses validation or review.

Other providers or local models can use a JSON runner config: `{"argv":["python","your_runner.py"],"timeout_seconds":300}`. The trusted local program reads the request from stdin and writes either a packet or `{"packet":{...},"usage":{"input_tokens":123,"output_tokens":456}}` to stdout. No shell is used. Source content cannot select the program. Invented source URLs or altered provenance, changed unaffected sections and reused citation IDs pointing to different sources are rejected.

`run-metrics.json` records elapsed time, token usage if reported, and cost only when explicit `usd_per_million_tokens` input/output rates are supplied in the runner config. Unknown usage/cost stays null. Rate estimates are not invoices and do not account for provider-specific caching discounts. Model quality and source support still require review.

## 4. Review the actual draft

The reviewer reads the supporting source passages, checks dates/bases/units/calculations and conflicts, and records unresolved gaps. Format validation alone cannot do this. Create an attestation outside canonical research, then run:

```bash
python scripts/research_company.py review \
  --packet research/pilot/MU.json --attestation build/review/MU.json
```

Required attestation shape:

```json
{
  "ticker": "MU",
  "packet_sha256": "SHA-256 of the exact applied packet bytes",
  "draft_sha256": "SHA-256 of the exact canonical draft bytes",
  "reviewer": "Actual reviewer identity and whether AI or human",
  "reviewed_at": "2026-10-18",
  "notes": "Scope, source checking, conflicts and limitations actually reviewed",
  "claim_checks": [{"id":"C01","result":"supported","note":"Specific evidence checked; repeat for every claim"}],
  "gaps_acknowledged": ["Copy each current packet gap exactly"]
}
```

Every claim requires a supported check and a substantive note. The command verifies hashes, dates and completeness, promotes the draft, and writes a durable review record binding the resulting profile bytes. Subsequent packet/profile edits invalidate that binding. Hashes prove version identity, not truth; the editorial evidence review is essential. Pilot review notes state the actual separate-agent source checks and corrections.

## 5. Update only what changed

The collector compares current document hashes with `research/state/<TICKER>.json`, the source snapshot consumed by the last applied packet. Repeated inspection-only collection cannot consume an unapplied change. Checkpoints are bound to packet bytes and require readable coverage of its source URLs. A missing or mismatched checkpoint forces broad reconsideration.

Annual filings and unclassified events trigger broad review. Quarterly results target financials, capital allocation, segments, growth, catalysts, valuation, risks and scenarios; executive-change items target governance and risks. Any section citing a changed/removed source is added. These dependencies are proposals: inspect them for indirect implications. Rebuilt caches preserve packet citation IDs by URL.

With unchanged inputs and an existing applied profile, `run` skips model generation and preserves research/review dates. Collection alone does not demote or promote a profile. A known new material event should be triaged promptly; until its update is applied, the existing snapshot retains its explicitly dated research status. No background scheduler is installed.

## 6. Validate and evaluate

```bash
python scripts/stock_brain.py build
python scripts/stock_brain.py check
python scripts/research_company.py audit
python -m unittest discover -s tests -v
python scripts/stock_brain.py export --output build/chunks.jsonl
python scripts/evaluate_retrieval.py
```

Only reviewed company evidence and hash-bound reviewed sector guides enter export. Sector sources/dates and exact guide hashes are maintained in `config/sector_research.json`; index/navigation sections remain excluded. See [RAG.md](RAG.md) for the retrieval baseline and its limits. Commit concise evidence, reviews, checkpoints and generated indexes, not raw filings, credentials or generated embeddings.
