# Release readiness — 2026-10-19

The user authorized merging PR #3, publishing the existing owner-private Site
and activating daily updates. This file records implementation and the rollout
procedure; native GitHub/Sites receipts establish completed publication.

## Verified implementation

- 114 Python tests and 117 browser-engine/DOM tests pass.
- Both retrieval suites (20 development and 50 frozen bilingual cases) and all
  50 frozen answer-integrity cases pass; the frozen questions were not changed.
- Sixteen additional semantic cases cover growth versus absolute amounts,
  unsupported per-share requests, currency conversions and date qualifiers.
- Gross/operating/net margins and YoY revenue growth carry their inputs, formulas
  and source locators. Comparisons still require complete compatible evidence.
- AMD and NVIDIA critical filings are incorporated into source-bound English
  profiles and Hebrew evidence. Review is explicitly by AI.
- NVDA/AVGO split reconciliation resolves 32 flags and verifies 112 share/EPS
  cells. 77 financial QA flags remain; no global gate was waived.
- Refresh tests verify that normalization evidence survives the daily writer and
  does not approve newly filed, unreviewed observations.

## Live update verification

The October 19 refresh retrieved financial histories and dated market snapshots
for all ten issuers and discovered one additional PLTR item. The queue contains
148 events, 138 pending, zero P0 and 24 P1. Oracle announcement access is the only
source error, so the run is explicitly partial. All 77 QA flags and the verified
split reviews survived the refresh. Persistence and publication are checked in
the authorized rollout below.

## Authorized rollout

1. Run the live cloud refresher from current source, preserving review decisions
   and previous values if a source fails. Oracle announcement HTML failures must
   remain visible as partial coverage.
2. Recheck PR #3 head/base and CI, then merge the tested head.
3. Verify the four-file manifest and persist `desk.json`, `latest.json`,
   `triage.json` and `run-status.json` to `automation/research-data`. Read back
   exact Git blob hashes and the raw answer-contract-v2 snapshot.
4. Push the exact Site source, build/package it and publish its saved version
   with owner-only access unchanged.
5. After publication, read linked tasks and create the daily task only if no
   equivalent one exists. Record the saved task and its timezone.

Task: **Update Stock Brain**, daily **08:30 Asia/Jerusalem**, starting at the next
occurrence after activation. Each run follows [CLOUD_UPDATES.md](CLOUD_UPDATES.md),
restores the existing state branch, retains queues, validates the export,
publishes only the four data payloads and verifies persistence. Research approval
is separate from data refresh. No paid data/model service or external messaging
is required.

A saved schedule does not prove a future run occurred. `run-status.json` retains
actual dated outcomes. Three successful daily runs remain an observation gate.

## Remaining scope

The unresolved disclosure queue, issuer-specific debt/revision reconciliation,
Oracle announcement access and independent human review remain open. Coverage is
ten companies in two populated sectors. A general language-model assistant, live
analyst consensus and issuer-specific forward valuation are not supplied by this
release; the scenario tool remains an explicit sensitivity calculator.

Visual browser QA was unavailable in this runtime. Real data, all DOM views,
source links, numerical gates and offline/incompatible-snapshot fallback passed.
