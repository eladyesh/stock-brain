# Stock Brain development log

## 2026-10-22 — broad directory and daily data releases

Added strict import of both official Nasdaq Trader exchange directories, separate
listing-slot/issuer identities, explicit instrument classification, paginated
security search and per-dataset gaps. The real October 22 source files contained
13,293 rows: 13,256 non-test securities and 5,958 equity candidates under the
documented classifier. These are not 5,958 completed company research profiles.

Added a daily GitHub workflow, verified immutable compressed SQLite releases,
published-byte cold recovery and generation-based web replication. An optional
Financial Datasets adapter requires a server key, public-use license confirmation
and a daily request cap. Its durable reservation prevents failed-run retries from
resetting that daily cap. SEC remains disabled; no paid resource was provisioned.

The operating contract and remaining work are in
[Broad market operations](BROAD_MARKET_OPERATIONS.md). Production commit/run IDs
and verification results will be recorded in the release PR after deployment.

## 2026-10-22 — automated coverage foundation and research workbench

The user clarified that the main objective is code infrastructure for future
coverage of U.S.-listed companies. This release separates a broad issuer registry
and incremental collection pipeline from the small reviewed research corpus.

- Added stable CIK issuer identity, separate listing/share-class history, validated
  source imports, versioned per-company payloads and a leased transactional job
  queue. Registry reads are paginated and do not load financial payload bodies.
- Added a bounded SEC worker and explicit continuous cycle with shared request
  pacing/cooldowns, fair scheduling, resume after restart, incremental accession
  checks and unreviewed source-linked numerical change drafts. Startup uses CAS
  so seeding cannot overwrite a newer concurrent collection.
- Added read-only company APIs, a registry UI and consistent SQLite local
  backup/restore with an integrity/hash manifest. The broad store is separate from
  the existing four-file GitHub backup. No new hosting resource was provisioned.
- Added strict four-quarter TTM comparisons, MSFT/MU/NVDA FY2027–FY2030 illustrative
  models, source-bound before/after thesis comparisons, personal browser notes
  and saved assumptions, and queue grouping without changing document obligations.
- Updated RTX from its Q2 and Q3 official releases with evidence-bound AI review.
  The release is covered; the separate SEC 10-Q/8-K remain pending. Actual backup
  restoration into this release retained 216 queue items and re-triaged them to
  205 pending, including two P0 items. This rebuild is not a new source scan.
- Exact MSFT/MU/NVDA share/debt reviews made 84 more cells usable and resolved two
  NVDA split conflicts: 1,905 usable cells and 75 open QA flags. NVDA strict FCF
  remains unavailable; issuer-defined FCF stays separately labelled.
- Source health now distinguishes SEC from issuer checks and preserves the last
  successful timestamp across failures. Backup verification records workflow
  trigger type and a dated artifact; a manual run does not prove cron delivery.

Local validation passed: **249 Python tests**, **173 JavaScript/DOM tests**,
10-profile evidence/review audit, 172-chunk export, 20 retrieval baseline cases,
50 frozen bilingual retrieval cases and 50 answer-evidence cases. The JavaScript
suite includes 35 independently selected workbench questions. Coverage testing
includes a 50,000-synthetic-issuer paging fixture, independent concurrency
regressions, restart progression and local backup/restore. These are not real
market coverage or production throughput claims. A cloud-browser preview could
not be completed because its URL authority check rejected the tab; DOM behavior
and real WSGI/Node routes were tested locally.

### Production deployment and recovery proof

- PR #6 merged as `35c9169dc2fb8c1df5565f77724819bf2b985b61`; head and main CI passed.
  Render deployment `dep-dbcvfnt9fdbs73a1n7rg` became live at **11:48:45Z** on
  October 22, using the existing service, plan and instance count.
- The new registry, bounded company search/detail and source-linked TTM display
  were exercised against the live app and in the browser. This later production
  verification supersedes the local-preview browser limitation above. A follow-up
  presentation correction replaces internal thesis IDs with readable bilingual headings.
- Startup collection committed at **11:48:54Z**. All 216 existing event IDs,
  historical financial values and financial-source timestamps were preserved.
  Three new issuer disclosures increased the queue to **219 total / 208 pending**.
  Oracle's official RSS was successfully retrieved from Render at 11:48:43Z;
  the earlier local-runtime source error is not a claim of a continuing Render failure.
- [Backup/recovery run 39773645859](https://github.com/eladyesh/stock-brain/actions/runs/39773645859)
  succeeded, preserving data commit `8f3b2bd4a8cba4a00f6ec6485767bdc61036aebb`.
  Actual restoration into empty state at **11:51:01Z** reported 219 restored events,
  passing public answers and financial integrity, and 75 open QA flags.
  The dated verification artifact was uploaded. This was a manual dispatch;
  scheduled delivery is still not established by that result.
- SEC collection remains disabled and no broad worker or market-wide import was
  started. Ten issuer identities seed the new registry; this is not full-market
  coverage. The new SQLite store is still ephemeral on this deployment and is
  excluded from the pilot backup. Broad activation requires permitted SEC access,
  durable storage and verified off-host recovery. The remaining universe,
  accounting and capacity milestones are in [U.S. coverage infrastructure](US_COVERAGE.md).

## 2026-10-22 — reliable collection and server-side answers

### Authorized scope

1. Diagnose SEC collection failures on the existing Render service and implement a supported free-data solution where possible.
2. Strengthen financial-data validation and reconcile issues only when primary evidence supports the change.
3. Exercise collection, backup and cold restoration without ChatGPT as a runtime dependency.
4. Add a server-side `/api/ask` endpoint and expand supported, cited questions.
5. Keep this log and operational documentation current, including unresolved blockers.

Only `eladyesh/stock-brain` and Render service `srv-d8i2kla8qa3s73e10t50` are in scope. The `finlotus` repository and the other Render service are excluded. Keep the existing compute plan; no paid model API or new paid service.

### Baseline

- Main release: `b9524b5445ce9bab9c13e7a74c9664b72b84188f`.
- Public app: <https://finlotus-1.onrender.com/>.
- Backend: Python/Waitress, same-origin public APIs; Q&A currently executes in the browser.
- Daily collection: 08:30 Asia/Jerusalem. Backup workflow: twice hourly.
- Deployment `dep-dbcrqnd9fdbs73c5m19g` was live; initial backup workflow run `39742541119` succeeded and persisted data commit `3944d8a31b24138d2249ef069da6376c8e82c1e2`.
- First Render collection retained financial histories after SEC HTTP 403 errors; market collection succeeded and the pending disclosure queue reached 206.
- Existing financial-remediation documentation records 77 open QA flags. Flags are not resolved by suppressing them or by choosing the newest value without evidence.

### Implemented

- Added `POST /api/ask` on the Python backend using the shared JavaScript evidence engine. The worker has bounded concurrency, memory and duration, fixed file paths, no shell and no model/source requests. The browser calls it and labels fallback to its loaded snapshot on failure.
- Added Hebrew/English questions for the latest stored fiscal quarter/year, with exact period selection, citations and an explicit freshness limitation. Unsupported qualifiers and unverified cells still cause abstention.
- Strengthened financial validation: issuer identity, complete period/metric maps, status/value consistency, finite values, exact reported values versus provenance, calculation recomputation, derived-input eligibility and existing split-review bindings.
- Reject empty or truncated successful source downloads before replacing previous histories. Added a shared SEC 403 circuit breaker and an operator pause setting.
- Corrected a collector retry bug: a failed startup refresh now retries after one hour even if an earlier successful run was completed that same day. Partial source refreshes remain on the daily schedule.
- Extended each backup job with actual cold restoration and public answer checks. It checks queue/review preservation, exact financial/price equality, data integrity, a 36-hour collection-age limit and failed attempts. Failures fail the Actions job; partial source coverage remains visible.
- Added API documentation, operational instructions and a reproducible financial QA ledger. No research approvals or company facts were changed.

### Evidence and local verification

- Actual Render shell request on 2026-10-22 returned HTTP 403 with the SEC title “Your Request Originates from an Undeclared Automated Tool”. No alternate IP, proxy or browser impersonation was attempted. The deployed configuration pauses SEC requests while legitimate access is unresolved; issuer feeds and market refresh continue.
- Both repository histories and the downloaded live histories pass the stricter integrity checks. The generated `docs/FINANCIAL_QA_STATUS.json` records **77 open flags** across 10 issuers; integrity is not filing-level review.
- Actual cold restore from the GitHub data branch passed at `2026-10-22T08:28:40Z`: **216 queue records** restored, with review decisions, prices and financial histories preserved. Baseline pending-review count was 206, distinct from total queue size.
- Python test suite: **128 passed**. Browser/engine tests: **128 passed**. Regression coverage includes mutated numbers, derived arithmetic, blocked SEC sources, operator pause, empty/truncated downloads, real Node-worker answers, malformed/oversized requests, busy/timeout recovery, startup retry, latest-period scope guards and labelled offline fallback.
- Profile/index check, 10-profile evidence/review-binding audit, 172-chunk reviewed-only export, 20-case retrieval baseline, 50-case frozen bilingual retrieval acceptance and 50-case answer-evidence evaluation all passed. No paid model calls were made.

### Remaining blockers and release status

1. **SEC access:** confirmed external automated-access denial from Render. An approved contact identity and permitted source access are needed before re-enabling it. Existing dated data remains available; complete daily SEC refresh is not claimed.
2. **Financial reconciliation:** 77 existing flags still need issuer/filing-specific primary evidence (revision/definition, share-class/split scope, debt coverage, fiscal identity and missing coverage). The ledger and FINANCIAL_REMEDIATION.md identify the cases. No unsupported numbers were substituted.
3. **Schedules:** daily collection and twice-hourly GitHub backup are configured. The first manual backup succeeded; at the latest inspection, no scheduled run of the new backup workflow had appeared. GitHub cron delivery can be delayed, so scheduled execution is not yet proven.
4. **Code deployments:** the service's public-Git source has automatic code deploys disabled, so tested code releases require an explicit Render deployment. Runtime collection and GitHub backup do not require ChatGPT.

### Production release and recovery evidence

- [PR #5](https://github.com/eladyesh/stock-brain/pull/5) merged as `05e8222419e5d74e0f2743005e9bfe766f112d97`. Both head CI runs passed; the [main-branch validation run](https://github.com/eladyesh/stock-brain/actions/runs/39749126995) also passed. Uploaded blobs and the Git tree were checked against the locally tested content.
- Render deploy `dep-dbcsmovavr4c738mmolg` became **live at 2026-10-22T08:38:49Z** (11:38 Israel). It uses the existing starter instance, Python and Node; no new paid service was created. `STOCK_BRAIN_SEC_ENABLED=0` was merged into this service's existing configuration.
- Startup restored the existing backup, then completed its independent source collection at **08:39:01Z**. All 10 prices were available, all 10 financial histories matched the previous live histories exactly as parsed objects, and all prior disclosure IDs remained. The queue contains **216 total / 206 pending** records. Collection remains labelled **partial** because SEC collection is paused.
- Public `/healthz`, `/api/status`, and `/api/ask` were checked. Hebrew business and latest-stored-quarter questions returned cited answers; a buy recommendation question abstained. Browser verification visibly showed “answer from server”, the selected fiscal period, the dataset limitation and source links.
- [Backup and recovery run 39749692374](https://github.com/eladyesh/stock-brain/actions/runs/39749692374) completed successfully. Job `119726847963` persisted data commit `749b0e78c9e8369011765388d4b98cf8a71b2842`, and the branch ref was verified.
- The job's actual recovery check at **08:42:19Z** reported `cold_restore=pass`, `restored_queue_count=216`, `answer_api=pass`, `financial_integrity=pass`, `open_financial_flags=77`, `refresh_status=partial` and `sec_collection_enabled=false`.
- GitHub's workflow menu confirmed backup is enabled. Both observed backup runs were manually dispatched; scheduled delivery remains unobserved at this checkpoint. The next configured app collection is **2026-10-23 08:30 Asia/Jerusalem** (`05:30Z`). The old ChatGPT automation remains disabled; the legacy disclosure workflow was skipped on the main release.
- The separate `finlotus` Render service was read back unchanged (`updatedAt=2026-07-14T00:39:23.612689Z`) and still points to `eladyesh/finlotus`. No code or settings in that project were modified.

### Handoff / next actions

1. Resolve the SEC application's identifying-contact/access requirements with the source; only then re-enable SEC collection and verify an actual successful refresh. No private contact was published or used as a guessed identity.
2. Work through the issuer-specific cases in `FINANCIAL_REMEDIATION.md` and the generated QA ledger using primary filing evidence. Keep open flags and old source dates until each case is genuinely reconciled.
3. Observe the next scheduled backup and daily collection in GitHub Actions and `/api/status`. Automated recovery/API checks are now in the backup job; a passing manual run proves the pipeline, not delivery of a future cron event.
4. For broader natural-language chat, choose and benchmark an independently hosted model against available memory and evidence requirements before adding it. The deployed product is deterministic cited retrieval, with no paid model dependency.

This documentation update records the completed release; it changes no deployed application code.
