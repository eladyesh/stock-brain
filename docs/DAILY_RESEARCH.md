# Daily research across the stock universe

The company directory is the universe, not a hand-maintained ten-company list.
Every mapped issuer gets a dated Markdown profile and an explicit research plan.
The public navigation uses stock symbols and company names. CIK is an immutable
internal issuer key: ticker changes, multiple share classes and sector changes
must not merge or reset company history.

## What is automated

1. The existing daily coverage workflow downloads official SEC bulk archives and
   publishes a verified data release. Its completion starts `Publish company Markdown`.
   A daily 12:53 UTC fallback also continues research using the latest verified
   release if the upstream refresh fails. Durable per-UTC-day request, company
   and model-attempt budgets prevent duplicate triggers from multiplying usage.
2. The Markdown workflow restores the verified release and the durable queue from
   the `research-data` branch. A source fingerprint uses filing accessions rather
   than daily export timestamps; unchanged documents do not cause new work.
3. Each active issuer is planned, including companies outside `config/universe.json`.
   The collector resolves primary documents from actual SEC filing-index tables.
   Annual, interim, governance and event filings are separate evidence sources.
   Foreign forms remain identified; a 6-K is not assumed to be a quarterly report.
4. A run processes up to 120 companies, 360 network attempts, and 20 minutes of
   collection. All remaining companies stay in the queue for later runs. SEC
   requests use an operator-provided contact and a maximum of two attempts per
   second. A 403 stops the SEC batch; failures receive bounded exponential backoff.
   Partial document progress is checkpointed; prior evidence is retained.
5. Exact dated excerpts identify business, segments, products, customers,
   competition, governance and risks where matching source text exists. These are
   explicitly source excerpts, not an assertion that the entire report was read,
   an investment thesis was reviewed, or each research topic is complete.
6. Financial observations calculate annual growth, margins and cash conversion
   only from usable, dated, compatible US GAAP cells. Every observation retains
   formula, inputs and filing links. Definition changes, negative prior growth
   denominators, irregular periods and source conflicts block the calculation.
7. All issuer profiles are enriched with current work status, evidence and next
   questions. The publisher writes full history to `brain-data`, and compact
   symbol-named profiles to `sectors/<sector>/facts/<SYMBOL>/README.md` on main.
   Full-history folders are also symbol-named at `brain/companies/<SYMBOL>/`;
   the publication manifest resolves immutable CIKs to their current paths.
8. Render reads the verified manifest periodically and exposes searchable company
   research and its actual Markdown sections through `/api/research`. A detail
   read is hash checked, pinned to a commit, bounded and cached. No collection or
   paid model call occurs on the public HTTP request path.

## Research states and review

`pending` → `evidence_collected` → optional `draft`. `retry` preserves the last
successful evidence and retry date; `source_missing` means the required filing
metadata needs work. Collection of all planned documents is distinct from topic
coverage. Every automatic profile remains `status: stub`,
`canonical_reviewed: false`, and excluded from reviewed retrieval.

Existing curated research remains in `sectors/*/companies/<SYMBOL>/README.md` and
is never overwritten by daily collection. Its review dates are not refreshed by
data updates. The existing evidence packet and review-attestation process remains
the route for promotion. Analyst/model conclusions cannot be auto-approved by
format tests or a successful download.

The curated `research_company.py` runner also resolves supported common shares
and ADRs from the verified broad manifest when they are absent from the initial
cohort. Unclassified issuers and unresolved instrument types need an explicit
classification decision before entering that stricter curated schema; their
daily evidence collection does not depend on that decision.

## Optional synthesis

No paid model request is enabled by default. The existing explicit Responses API
adapter can synthesize source-bound draft claims when all of these are configured
in GitHub Actions: secret `OPENAI_API_KEY`, variable `OPENAI_MODEL`, and variable
`STOCK_BRAIN_RESEARCH_MODEL_ENABLED=1`. The workflow limits synthesis to two model
attempts per UTC day. The model must return all 17 research topics, use exact excerpts
as evidence, and state unavailable topics. Invented source IDs, quotes, numeric
claims, issuer identities and review fields are rejected. Passing these checks is
not semantic review; generated conclusions remain labeled unreviewed drafts.

CLI operators may supply a different explicit JSON argv runner with
`research_queue.py run --runner <config> --model-limit <0..5>`. Filings cannot select
commands, models, credentials or destinations. `config/openai-runner.example.json`
contains the existing adapter configuration, with no credential value.

## Persistence, migration and limits

- `research_state.py restore/publish` checks the remote parent and each retained
  report digest, uses fast-forward Git updates, and refuses unexpected files.
- The fact manifest accepts old CIK paths while migrating to version 2 symbol
  paths. Install verifies every old file before removing only manifest-owned old
  paths. Multi-class aliases remain indexed; symbol collisions receive a CIK
  suffix. Renames keep `company_id=company-cik-<CIK>` and Git history.
- The compact tree is bounded to 256 MiB / 96 KiB per company; the full history
  tree to 768 MiB / 512 KiB per company. These file budgets accommodate added
  dated research evidence; the financial database's separate capacity guard is
  unchanged. Exceeding any bound fails publication, retaining the prior version.
- `state.json` records actual counts, request use, stop reason and model status.
  The Actions artifact retains this operational record for 30 days. Git retains
  successive source/research generations and superseded evidence.

## Remaining depth gaps

The infrastructure does not by itself establish all-company deep research.
Competitive interpretation, defensible moats, forecasts, current valuation,
customer concentration, governance judgments and thesis breakers still need
adequate dated evidence and review. SEC access failures, unsupported foreign
accounting, unmapped listings and provisional industry assignments remain
visible. Daily scheduling means a bounded batch is attempted daily; it does not
mean every company's full qualitative research is rewritten every day.

References: [SEC data APIs](https://www.sec.gov/edgar/sec-api-documentation),
[SEC fair access](https://www.sec.gov/filergroup/announcements-old/new-rate-control-limits).
