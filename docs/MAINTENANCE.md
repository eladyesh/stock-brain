# Keeping Stock Brain current

The unit of maintenance is a changed disclosure and the claims it affects. Discovery, drafting and approval have separate state. Opening or downloading a document never approves research.

## Current desk updater

The hosted desk uses the separate automation/research-data branch. scripts/refresh_desk.py refreshes SEC histories, dated quotes and the durable disclosure queue, then exports a publication manifest. The linked Site task follows [CLOUD_UPDATES.md](CLOUD_UPDATES.md). Routine data updates do not require Site deployment. Partial failures are persisted visibly; neither discovery nor normalization approves narrative research. Verify the linked schedule and actual run history before claiming unattended reliability.

The workflow below remains available as a separately gated GitHub/local option.

## Legacy disclosure-only operation

`.github/workflows/disclosures.yml` runs daily at 05:23 UTC, supports manual runs, and runs when its implementation changes on main or the initial implementation branch. Unattended runs require the workflow on the default branch, GitHub Actions enabled, and `STOCK_BRAIN_RUNNER_LABELS` configured. They are deliberately paused until a permitted execution host is selected. GitHub scheduling is best-effort, not a real-time delivery guarantee.

## Activation requirement found during live testing

The first GitHub-hosted run returned HTTP 403 for SEC submissions for all ten issuers and for the Broadcom/RTX feeds. The same requests succeeded in the development environment. This is an access/deployment blocker, not a passed automation test. The failed run retained all 112 pending events and surfaced errors correctly.

For this public repository, prefer the local scheduler described below on a stable machine with permitted source access and an identifying `SEC_USER_AGENT`. If using GitHub orchestration, use a dedicated isolated machine restricted to trusted workflows. Configure it as a repository self-hosted runner, then set the repository variable `STOCK_BRAIN_RUNNER_LABELS` to its labels, for example `["self-hosted", "linux", "stock-brain"]`. Run the workflow manually and verify source access before relying on the schedule. GitHub's [self-hosted runner setup](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners) covers registration. No runner, credential, paid server, or hosting account was provisioned by this PR. A manual dispatch without that variable can diagnose the hosted environment; ordinary push/scheduled runs remain paused.

Alternatively, run `scripts/refresh_research.sh` daily from an existing authorized host's scheduler, with `PYTHON_BIN` pointing to this checkout's virtual-environment Python and `SEC_USER_AGENT` set. Keep its working directory persistent and inspect nonzero exits. The local workflow stores pending state in `build/monitoring/latest.json`.

The job:

1. Restores the durable queue from `automation/disclosure-state`, initially seeded from `research/monitoring/latest.json`.
2. Checks SEC submissions for all ten companies, eight configured issuer RSS sources and the public Q4 JSON news lists used by Micron and Palantir's own websites. Oracle's officially documented RSS is configured but currently returns an unavailable HTML page from this environment; this is an error, not successful coverage. The configured 90-day overlap before each packet's cutoff catches missed disclosures; overlapping results are deduplicated. Rolling RSS lists do not guarantee a complete 90-day archive.
3. Keeps unreviewed events pending, even when they disappear from a feed or a later fetch fails. New annual/quarterly filings, amendments, event filings and proxies are candidates. The monitor follows overlapping SEC submission archive files, subject to an explicit bound.
4. Prepares review requests for at most two companies, at most ten new queue items per company. Financial filings and results come first, then other filings, transactions, contracts and leadership changes, then other announcements, then calendar/editorial headlines. This is a metadata routing rule, not a materiality determination. Already prepared event IDs are tracked against the exact research packet, avoiding repeated preparation of unchanged work. Preparation does not remove review obligations.
5. Saves discovery/preparation state to the separate state branch; canonical research is untouched. Failed fetches remain errors. Run summaries and request artifacts are retained for 30 days.

The state branch stores JSON only. Updates are fast-forward and serialized; they do not overwrite `main`. Failure to restore an existing queue stops the run. A branch test does not write production state. No email, chat messages, paid model calls, issue creation or automatic research approval is configured.

Set the repository secret `SEC_USER_AGENT` to the actual application name and operator contact email; the existing repository-variable form remains supported. The repository-URL fallback is only suitable for non-SEC sources and now fails locally before any SEC request. The disclosure workflow defaults `STOCK_BRAIN_SEC_ENABLED` to `0`; set its repository variable to `1` only after the observed access denial is legitimately resolved. The shared fetcher limits each instance to two requests/second and honors bounded retry/backoff; the broad worker additionally coordinates through its persisted source gate. SEC's ceiling is ten requests/second across all clients, so independent collectors must not multiply that budget. See [SEC access diagnosis and recovery](SEC_ACCESS.md) and the [official guidance](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data).

## Coverage and freshness

| Layer | Current handling |
| --- | --- |
| Company filings | SEC discovery for all ten covered issuers |
| Issuer announcements | Microsoft, NVIDIA, AMD, Broadcom, Lockheed Martin, RTX and AeroVironment RSS; Micron and Palantir public Q4 JSON lists |
| Oracle announcement access | Official corporate RSS configured; local HTTP-200 response contains `Site Unavailable`, so its check fails visibly |
| Empty or changed source formats | HTML app shells/error pages are rejected; empty real lists, malformed entries and missing dates produce partial coverage |
| Prices, multiples and consensus | Separate dated Yahoo price snapshots; no exchange real-time SLA, consensus or sourced forward multiples. Narrative lookup abstains on live valuation questions. |
| Review status | Exact packet/profile approval hashes; actual reviewer identity retained |
| Scan health | Errors, missing state, changed evidence version and scans older than 48 hours are visible |

Research cutoff, latest financial period, publication date, review date and last scan time are different concepts. A recent scan does not renew an old research date. A source marked “checked” does not imply exhaustive knowledge of all news. A company without verified issuer-announcement coverage cannot satisfy an explicit current/latest question.

Each company now exposes `source_checks` (endpoint, parser kind, response hash, entry count, latest publication and warnings), `issuer_source_count`, and a separate `coverage_status`. The review queue can be nonempty while coverage is partial; `needs_review` must not hide that coverage limitation. A successful SEC response with zero new filings is normal. An empty issuer feed/list cannot confirm working announcement coverage and is partial. A failure in one source preserves candidates from successful sources and all previously pending IDs.

The adapters were verified against the actual official sources on 2026-10-18:

| Issuer | Adapter and provenance | Verification |
| --- | --- | --- |
| AVAV | [Official RSS](https://investor.avinc.com/rss/news-releases.xml) | Returned RSS with dated announcements locally |
| MU | [News page](https://investors.micron.com/news/default.aspx), using the public `/feed/PressRelease.svc/GetPressReleaseList` endpoint specified in its [published Q4 JavaScript](https://investors.micron.com/js/module/widgets/dist/latest/evergreen.q4Api.min.js) | Valid JSON with 39 entries for 2026; old Drupal RSS returns 404 |
| PLTR | [News page](https://investors.palantir.com/news), using the public endpoint specified in its [published JavaScript](https://investors.palantir.com/bundle.js) | Valid JSON with 49 entries for 2026; HTML app shells are not parsed as news |
| ORCL | [Corporate RSS](https://www.oracle.com/corporate/press/rss/rss-pr.xml), linked from [Oracle's RSS directory](https://www.oracle.com/corporate/rss/) | Web retrieval sees current announcements; both this URL and the official IR RSS return unavailable HTML locally. Requires permitted source access before operation can be called healthy |

Q4 requests are bounded to the calendar years touched by the research overlap (maximum four), and the original publication date is retained. These are public website interfaces, so a future schema change fails explicitly and needs adapter maintenance. No private API, authentication, access-control bypass or new hosting service is used.

The first live scan on 2026-10-18 completed for all ten issuers without fetch errors and discovered 112 pending candidates. This is an initial overlap backlog, not 112 confirmed material developments. The checked-in report is a dated bootstrap snapshot, not a perpetual freshness badge.

The subsequent adapter verification scan retained all 114 prior records (112 pending, two already represented in reviewed evidence) and added 33 candidates: 15 PLTR, ten AVAV and eight MU. The saved snapshot has 145 pending items, routed as seven P0, 25 P1, 104 P2 and nine P3. All ten SEC checks and nine issuer-announcement checks succeeded; Oracle's announcement check failed and the command returned nonzero. No candidate was dismissed or newly approved. `triage.json` reports no exact-URL/accession duplicate candidates in this snapshot. Both error and partial-coverage scans return nonzero while preserving the durable queue.

## Review cadence

Review high-priority financial and material-event filings promptly. Batch ordinary announcements by company. Reserve a weekly pass for the oldest pending items, missing sources, feed health, and stale companies. A larger universe needs a review budget: expand coverage only when the pending backlog stays manageable. The current workflow prepares evidence automatically; it does not promise fully autonomous financial judgment.

For each selected company:

```bash
export SEC_USER_AGENT='Your application name and contact'
python scripts/disclosure_monitor.py --summary build/monitoring/summary.md
python scripts/triage_disclosures.py --report build/monitoring/latest.json
python scripts/prepare_updates.py --limit 2
# Inspect build/research/TICKER/request.json and update-plan.json.
# Use the existing optional runner explicitly, or author a corrected packet.
python scripts/research_company.py draft --packet path/to/proposal.json --apply
python scripts/research_company.py review --packet research/pilot/TICKER.json --attestation path/to/review.json
python scripts/stock_brain.py build
python scripts/stock_brain.py check
```

Read the relevant original exhibits before asserting financial results. The request carries the prior packet and the change plan; update only affected sections where the plan permits. Preserve facts unaffected by the new disclosure, distinguish reported results from guidance, and document remaining gaps. Rebind translations and rerun the quality gates. Approval invalidates old translations for changed claims. Material queue items resolve after their URL or SEC filing accession is present in a hash-bound reviewed packet; mentioning an event in a draft is insufficient. An explicit reviewer may instead record a verified nonmaterial/irrelevant/duplicate disposition as described below.

## Queue triage and review audit

`research/monitoring/triage.json` preserves every queued event and shows P0–P3 priority, the routing reason, exact-URL/accession duplicates, and whether it is already represented in reviewed evidence or still needs review. Headline similarity alone does not establish a duplicate. Tracking-parameter/fragment differences may identify duplicate candidates, but grouping never closes either copy. The original 112 pending disclosures are retained and prioritized; the three newly working announcement adapters may reveal additional backlog.

The `reviews` array is a separate append-only audit trail. The initial generated triage contains no new review decisions. To close an irrelevant disclosure, one with no material change to the current research, or an actual duplicate, read the whole original disclosure and write an explicit decision with:

- `event_id` and `event_sha256` from the triage entry;
- the exact `packet_sha256` and approved `profile_sha256`;
- `reviewer`, `reviewer_type` (`human` or `ai`), timezone-aware `reviewed_at`, `source_read_in_full: true`, the current `sections_checked`, and a substantive source-based `reason`;
- `disposition` (`irrelevant`, `no_material_change`, or `duplicate`; the last also needs `duplicate_of`, `duplicate_of_event_sha256`, and evidence for both originals);
- `evidence`: public source `url`, actual byte `sha256`, and an exact supporting `excerpt`. The original queued URL must be included.

Then run:

```bash
python scripts/triage_disclosures.py --report build/monitoring/latest.json --record-review path/to/decision.json
python scripts/disclosure_monitor.py --summary build/monitoring/summary.md
```

Recording refetches the supplied original source, validates the byte hash and excerpt, appends retrieval metadata and an audit checksum, and keeps prior review records. Only a valid explicit record can produce `reviewed_disposition`. Changing the event, packet or approved profile invalidates it and reopens the obligation; an unavailable source cannot produce a new record. Duplicate chains/cycles cannot resolve every copy. AI review remains labeled as AI review. A disposition does not change a claim, research cutoff, profile approval, missing-source status or expired-scan status. It is not a substitute for updating research after a material development.

For an HTML release whose non-content markup changes on every request, the reviewer may additionally supply `reviewed_text_sha256`, computed from the complete `research_pipeline.document_text` output of the source actually read. A changed byte hash is accepted only when that complete-text hash still matches. The record retains the original `reviewed_sha256`, fresh `sha256`, and `verification: unchanged_complete_html_text`; even a change outside the supporting excerpt fails. Use this option only after inspecting the markup changes and confirming that the reviewed disclosure is fully represented by the extracted text. Exact source bytes remain the default. The first substantive P0 review and its two open update requests are documented in [P0_REVIEW.md](P0_REVIEW.md).

An operator should inspect P0 first, batch P1 and P2 by affected research section, and reserve a weekly pass for P3 and the oldest pending events. Retain the triage audit file in Git when accepting reviewer-authored dispositions; scheduled discovery reads it but never invents reviewer records.

The existing model runner is optional and requires an explicitly supplied model/key/configuration. It may draft a proposal but does not bypass review. Runtime answers and scheduled discovery incur no model API calls. Hosting/Actions usage and research labor are separate costs. This session's review time and cost were not measured per company and are unknown, not zero.

## Operating checks

Check the Actions run and summary when a scheduled scan fails. GitHub's own account notification settings determine whether you receive workflow-failure notifications. The UI also expires a scan after 48 hours, including a scheduler that stopped running. GitHub may disable schedules in inactive public repositories, and schedules can be delayed: [scheduled workflow behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

To use the newest scheduled state locally:

```bash
git fetch origin automation/disclosure-state
mkdir -p build/monitoring
git show FETCH_HEAD:latest.json > build/monitoring/latest.json
python scripts/serve.py
```

If an artifact expires, the durable pending queue still exists. Regenerate that company's request with the existing `research_company.py run --ticker SYMBOL --force` command; it does not approve the packet. If the state branch is deleted, recover it from a retained run artifact before resuming rather than treating the bootstrap snapshot as complete history.
