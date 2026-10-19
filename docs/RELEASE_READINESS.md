# Release readiness — 2026-10-19

Code changes are proposed in GitHub PR #3. The release is staged pending user
approval to merge the PR, publish the private Site and activate daily updates.

## Verified preparation

- Exact-period and historical-answer changes pass Python, browser-engine/DOM and
  frozen acceptance checks. GitHub Actions also passed for the implementation.
- SEC financial history and dated market data refreshed for all ten issuers on
  October 19. Oracle's announcement feed remains an explicit partial-refresh
  error. The 140 pending disclosure reviews remain open.
- The Site exists with owner-only access. The observed initial state had no saved
  version, live URL or linked task. The source and deployment package are prepared
  for saving without publication.
- The production data branch did not exist. Its initial payload is prepared from
  the completed refresh, including exact answer contract v2, without resetting
  the queue or approving research.

## Approval-dependent rollout

1. Recheck PR #3 head/base and CI, then merge the approved head into main.
2. Verify the candidate four-file data payload's manifest and publish it to
   `automation/research-data`. If that branch was created meanwhile, preserve and
   restore its state first; never overwrite it with the bootstrap snapshot.
3. Read back the persisted files and hashes through GitHub and verify the raw
   `desk.json` is accessible with `answer_contract_version: 2`.
4. Deploy the prepared archive-backed Site version, retaining owner-only access.
   Use the version's returned ID and the native private deployment operation.
5. Once publication succeeds, get the Site again. Reuse a matching linked task;
   create one only when the task list is available and contains no match.
6. Verify the saved task, publication URL and data readback. A saved schedule is
   not evidence that a future run has completed.

Proposed task: **Update Stock Brain**. Daily at **08:30 Asia/Jerusalem**, starting
at the next occurrence after activation. Run instructions:

> Refresh Stock Brain's financial history, market snapshots and company disclosures
> using the connected GitHub repository eladyesh/stock-brain and its main-branch
> docs/CLOUD_UPDATES.md runbook. Restore the existing research-data branch, preserve
> the disclosure queue and previous values on source failures, and publish only
> the validated four-file data payload. Read back the saved update. Keep research
> approvals separate and report a short Hebrew summary of the refresh, pending
> reviews, source failures and successful persistence. Routine data refreshes do
> not require Site republication or paid services.

Visual browser QA was unavailable. Real data, DOM interactions, numerical gates
and the offline/incompatible-snapshot fallback were checked.
