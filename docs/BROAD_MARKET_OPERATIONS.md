# Broad market operations

## Goal and standing authorization

The user authorized continued autonomous implementation, verification, deployment
to the existing Stock Brain service and daily maintenance on October 22, 2026.
Continue concrete unblocked work without asking for routine confirmation. Keep
the reviewed research boundary, actual source evidence and access restrictions.
This authorization does not supply missing credentials, a data redistribution
license or a budget for new paid resources. Never invent those prerequisites.

Repository: `eladyesh/stock-brain`, branch `main`.
Existing Render service: `srv-d8i2kla8qa3s73e10t50` (NEW-finlotus), workspace
`tea-d58ndgmuk2gs73dodh90`, https://finlotus-1.onrender.com/ . Preserve its plan,
other environment variables and the unrelated finlotus service.

## What coverage means

The two official Nasdaq Trader directories contain exchange-listed securities,
including ETFs and other instruments. The October 22 files contained 13,293 rows,
13,256 non-test securities and 5,958 equity candidates under the explicit name
classifier. Candidates include 329 unresolved instrument types. These counts are
neither unique verified U.S. companies nor completed research profiles. The
directories include foreign issuers listed in the U.S. and do not cover OTC.

The expanded stock scope also includes preferred shares and common partnership
units, with separate filters; packaged SPAC units remain excluded. The earlier
counts above use the earlier classifier. `/api/coverage` reports the current
counts and `stock_scope` explicitly separates classified listings, unresolved
instruments and missing OTC coverage. These are name/flag classifications, not
verified issuer counts; closed-end funds still need independent identification.

The ten pilot issuers retain dated financial history, quotes and reviewed research.
Other securities initially have directory information only. Filings, financials,
prices, news, estimates and ownership are measured separately. Missing datasets
remain missing; a recent directory download never refreshes their dates.

`listing_key` identifies an exchange/symbol slot. Stable issuer identity is a
verified CIK. Name/type changes, reappearance after absence or loss/change of a
previous CIK mapping increment `identity_revision` and hide prior observations.
Absence means `not_in_latest_directory`, not proven delisting. Unresolved name,
venue, instrument and issuer mappings must not be silently guessed.

## Daily production path

1. `.github/workflows/coverage-daily.yml` runs at **06:23 UTC daily**, or by manual
   dispatch on main. Changing this workflow or directory importer on main also
   runs a bootstrap check.
   One concurrency group prevents simultaneous writers.
2. `coverage_release.py build` restores the last complete verified data release,
   validates the four-file pilot checkpoint, then merges both complete directories.
   Invalid schemas, stale/backwards files, a shrink above 10%, missing halves and
   conflicting listings abort the new generation. Existing releases remain usable.
3. Existing pilot quotes are copied with their original trade/retrieval dates and
   hashes. Optional vendor collection is disabled unless explicitly configured.
4. The job takes a SQLite online backup, verifies a local cold restore, and publishes
   `coverage.part-NNNN.sqlite3.gz` assets and `coverage-manifest.json` to an immutable
   prerelease tag. Each chunk has at most 32 MiB of raw data and its own raw and
   compressed hash. Legacy single-file releases remain readable.
5. It downloads the actual published bytes and cold-restores them into empty state.
   Only after success is `offhost-verification.json` uploaded. Incomplete releases
   are ineligible for consumers. This is off-host recovery evidence, not just a
   same-directory copy.
6. With `STOCK_BRAIN_COVERAGE_MIRROR=1`, Render checks every 15 minutes. It verifies
   bounds, hashes, SQLite integrity and schema, stages a separate database, then
   swaps readers under a lock. A failure keeps the last readable generation.

The existing daily pilot refresh and four-file checkpoint remain separate. The
broad database is never appended to `desk.json`. The broad builder is the sole
writer for this snapshot mode; do not run `coverage_cycle.py` against a web replica
and expect its local changes to become durable releases. HTTP searches do no
provider acquisition and return bounded pages. Client downloads do not include
the whole market database.

`/api/coverage` reports directory counts, per-dataset coverage, storage and mirror
state. `coverage_progress` distinguishes mapped listings from distinct verified
issuer IDs. Filing-check freshness uses the collector's source retrieval time;
new directory imports, storage migrations and deploys do not reset it. A 48-hour
check window indicates collection timeliness, not completeness of financial data.
`/api/securities?q=MSFT&limit=25` searches the broad directory;
`/api/securities/{listing_key}` gives identity, evidence and dataset availability.
Verified CIKs link to the existing `/api/companies/{cik}` detail API.

An observed manual run proves execution/recovery, not cron delivery. The manifest
records the actual workflow event and `scheduled_execution_observed`. Inspect the
first scheduled run separately; do not relabel a manual test as a scheduled run.

## Optional authorized vendor

The Financial Datasets adapter is an independent contracted source. It is not an
SEC access workaround. All five prerequisites must be supplied through GitHub
repository secrets/variables before network acquisition becomes enabled:

| Configuration | Location | Meaning |
| --- | --- | --- |
| `FINANCIAL_DATASETS_API_KEY` | Actions secret | Authorized server credential |
| `STOCK_BRAIN_FD_ENABLED=1` | Actions variable | Explicit enablement |
| `STOCK_BRAIN_FD_PUBLIC_DATA_LICENSE=1` | Actions variable | Operator confirms public display rights |
| `STOCK_BRAIN_FD_BULK_EXPORT_PERMISSION=1` | Actions variable | Separate written permission for raw/bulk public release exports |
| `STOCK_BRAIN_FD_MAX_DAILY_REQUESTS` | Actions variable | Explicit request allowance, 1–1,000 |

Never extract a connected app's credentials or assume its interactive access grants
server usage. Never print the key. No purchase, new service or key was made for
this release. The default makes zero vendor requests.

The October 21 provider terms prohibit raw/bulk redistribution even on standard
redistribution plans. A display license alone is insufficient for our public
SQLite assets. Packaging checks retained vendor data too. Two connected-provider
probes on October 22 returned a zero-balance error and no data. See
[SEC access and bulk ingestion](SEC_BULK.md) for source contracts and alternatives.

Before requests, a create-only daily reservation in `automation/vendor-budget`
consumes the entire daily allowance. It survives failed jobs and lost runners;
another run on the same UTC day skips calls. A transaction-backed counter also
caps in-run requests, including failures. Requests use fixed HTTPS endpoints,
bounded responses, one-second pacing and no credential-bearing redirects.
401/402/403 stop collection and persist a cooldown; 429 also stops the pass.
The allowance is a request limit, not an invented guarantee of monetary cost.

Profiles are due weekly; financials and prices daily. Fair queues eventually
rotate through eligible securities but do not promise daily full-market refresh
when the configured request allowance is smaller than the due workload. Non-profile
requests require a verified issuer mapping. Provider payloads remain unreviewed.
Vendor statements are not yet connected to GAAP/TTM comparisons or financial
screening: a dedicated accounting adapter with identity/unit/period/provenance
tests is required first. Directory search does not imply those features exist.

SEC access stays `STOCK_BRAIN_SEC_ENABLED=0` until the existing denial is resolved
through legitimate provider/operator access. Do not rotate hosts, IPs, proxies or
user agents to bypass it. Do not replace the actual contact with a fabricated one.

## Offline SEC bulk path

`sec_bulk.py` now supports bounded, resumable archive ingestion with CIK checks,
per-member provenance, isolated failures, exact job claims and existing financial
quality gates. `coverage_release.py build --sec-bulk-manifest PATH` integrates it
before snapshot publication. It reads already legitimately acquired local archives
and makes zero network requests. No production SEC archive has yet been acquired
or loaded; the daily release reports `sec_bulk_collection.status=not_configured`.
See [the operator commands and limits](SEC_BULK.md). This is not an alternate host
for a blocked SEC downloader. Foreign-form accounting, OTC and access resolution
remain separate work items. Online workers claim only their job kind; bulk workers
claim their exact job ID, so expired work is not stolen by the other queue.

## Capacity and next implementation priorities

This is a bounded single-writer batch system, not a claim of unlimited scale.
Schema 6 compresses and deduplicates large payloads while retaining every version.
Version-2 releases use independently verified 32 MiB raw chunks; restored databases
still stop at 512 MiB. Daily snapshots are retained off-host; web replicas retain
active and previous generations. Before approaching the remaining bound, implement
and verify the next storage migration. See [COVERAGE_STORAGE.md](COVERAGE_STORAGE.md)
for measured capacity, legacy migration and the recovery contract.
Never drop historical evidence silently to make a build pass. Larger universes,
intraday updates or concurrent collectors will require a costed durable database
and object-storage design before provisioning anything paid.

Continue in this order, completing and verifying each unblocked item:

Check actual storage headroom before every whole-market financial backfill. The
archive adapter makes collection possible once legitimate access is available;
compression and multipart publication do not remove the 512 MiB restored cap.
Prepare adapters from actual authorized source samples. Never count a synthetic
archive test as production coverage or a configured schedule as observed delivery.

1. Verify first cron-triggered release, its published-byte recovery proof and live
   generation; expose stale data, source failures, coverage percentages and update
   lag clearly. Verify that a host replacement recovers both stores.
2. Add provider-neutral validated observation/detail and screening APIs with
   strict as-of dates, units, null semantics, pagination and coverage requirements.
   Build accounting adapters using genuine source samples when authorized access
   exists. Use labelled synthetic fixtures only for tests, never production data.
3. Improve issuer/security reconciliation, changes of venue/symbol, share classes,
   corporate actions and delisting evidence without breaking permanent issuer IDs.
4. Add permitted filing/news feeds, earnings calendars, ownership/insider changes
   and estimates as independent dated datasets. Do not scrape through denials or
   treat a license for one dataset as permission for another.
5. Build incremental source-linked change summaries and opportunity screens on
   validated available data. Preserve the distinction between facts, guidance,
   estimates and interpretation; never automatically mark research reviewed.
6. Track completeness, freshness and source coverage by dataset and issuer; keep
   an actionable backlog and capacity/cost forecast. Full readiness requires
   measured sufficient coverage and observed scheduled runs, not just working code.

For continued daily engineering, inspect latest main, open work, CI, live APIs and
the latest release before choosing the next change. Respect `AGENTS.md`, keep PRs
small, run relevant tests/validators, merge only passing changes, deploy only the
intended service and verify actual behavior. Do not re-dispatch a healthy collector
merely because a monitoring task ran. Report meaningful completed changes or new
blockers briefly in Hebrew. Record deployment/run evidence in the implementation
PR, and keep this operating contract current.

## Validation

```bash
python scripts/stock_brain.py check
python -m unittest discover -s tests
npm run build
npm test
```

Targeted tests cover malformed/truncated directories, identity changes, missing
rows, pagination, corrupt snapshots, schema/bounds rejection, recovery and old-data
retention, zero-network disabled providers, durable budget reservation and payload
validation. Real-directory cold recovery is also verified before first deployment.

Source field definitions: https://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs
Vendor API contracts: https://docs.financialdatasets.ai/api/company/facts/ticker ,
https://docs.financialdatasets.ai/api/financials/all-financial-statements and
https://docs.financialdatasets.ai/api/prices/snapshot .

## First production evidence — October 22, 2026

PRs #8 and #9 passed CI and were merged. The first broad-market run
[39790049607](https://github.com/eladyesh/stock-brain/actions/runs/39790049607)
completed its source import, release publication and published-byte cold recovery.
Its newer 09:31 source files contain **13,260 non-test securities** and **5,960
equity candidates**. These supersede the earlier local-file counts above. Counts
are dated observations, not constants; consult the live API for the active release.

Release `coverage-20261022-39790049607-1` includes both data assets and a passing
off-host proof. Render deploy `dep-dbd18p1srm7s73b9od1g` became live at 13:50:37 UTC
from commit `bba9cf0f19bc5680bc8611362873bf74c271ae36` and loaded that verified
generation. Live checks passed for MSFT identity/detail, AAPL's explicit missing
data, ETF filtering, pagination bounds and health. Initial local verification
passed 271 Python and 173 JavaScript tests.

The pilot backup also passed after deployment in run
[39791215719](https://github.com/eladyesh/stock-brain/actions/runs/39791215719).
The earlier pilot backup run 39782948227 was genuinely schedule-triggered. The
new broad-market run was push-triggered; its first cron execution remains to be
observed. Daily autonomous continuation was enabled at 08:30 Asia/Jerusalem.

The live directory exposed packaged units whose names also mention warrants.
The importer now classifies the traded unit before its components, and avoids
treating an issuer named Unit Corporation as a unit. A subsequent run must
re-import the existing release to apply this refinement and prove continuity.
Its final run/deploy evidence is recorded in the follow-up PR.
