# Stock Brain development log

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

- Actual Render shell request on 2026-10-22 returned HTTP 403 with the SEC title “Your Request Originates from an Undeclared Automated Tool”. No alternate IP, proxy or browser impersonation was attempted. The release configuration will pause SEC requests while legitimate access is unresolved; issuer feeds and market refresh continue.
- Both repository histories and the downloaded live histories pass the stricter integrity checks. The generated `docs/FINANCIAL_QA_STATUS.json` records **77 open flags** across 10 issuers; integrity is not filing-level review.
- Actual cold restore from the GitHub data branch passed at `2026-10-22T08:28:40Z`: **216 queue records** restored, with review decisions, prices and financial histories preserved. Baseline pending-review count was 206, distinct from total queue size.
- Python test suite: **128 passed**. Browser/engine tests: **128 passed**. Regression coverage includes mutated numbers, derived arithmetic, blocked SEC sources, operator pause, empty/truncated downloads, real Node-worker answers, malformed/oversized requests, busy/timeout recovery, startup retry, latest-period scope guards and labelled offline fallback.
- Profile/index check, 10-profile evidence/review-binding audit, 172-chunk reviewed-only export, 20-case retrieval baseline, 50-case frozen bilingual retrieval acceptance and 50-case answer-evidence evaluation all passed. No paid model calls were made.

### Remaining blockers and release status

1. **SEC access:** confirmed external automated-access denial from Render. An approved contact identity and permitted source access are needed before re-enabling it. Existing dated data remains available; complete daily SEC refresh is not claimed.
2. **Financial reconciliation:** 77 existing flags still need issuer/filing-specific primary evidence (revision/definition, share-class/split scope, debt coverage, fiscal identity and missing coverage). The ledger and FINANCIAL_REMEDIATION.md identify the cases. No unsupported numbers were substituted.
3. **Schedules:** daily collection and twice-hourly GitHub backup are configured. The first manual backup succeeded; at the latest inspection, no scheduled run of the new backup workflow had appeared. GitHub cron delivery can be delayed, so scheduled execution is not yet proven.
4. **Deployment:** local work is complete; GitHub CI and the live release verification are pending below. The service's public-Git source has automatic code deploys disabled, so code releases are triggered explicitly.
