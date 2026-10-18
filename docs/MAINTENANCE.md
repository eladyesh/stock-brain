# Keeping Stock Brain current

The unit of maintenance is a changed disclosure and the claims it affects. Discovery, drafting and approval have separate state. Opening or downloading a document never approves research.

## Daily operation

`.github/workflows/disclosures.yml` runs daily at 05:23 UTC, supports manual runs, and runs when its implementation changes on main or the initial implementation branch. Scheduled runs become active only after the workflow reaches the default branch and GitHub Actions is enabled. GitHub scheduling is best-effort, not a real-time delivery guarantee.

The job:

1. Restores the durable queue from `automation/disclosure-state`, initially seeded from `research/monitoring/latest.json`.
2. Checks SEC submissions for all ten companies and six verified issuer RSS feeds. The configured 90-day overlap before each packet's cutoff catches missed disclosures; overlapping results are deduplicated.
3. Keeps unreviewed events pending, even when they disappear from a feed or a later fetch fails. New annual/quarterly filings, amendments, event filings and proxies are candidates. The monitor follows overlapping SEC submission archive files, subject to an explicit bound.
4. Prepares review requests for at most two companies, at most ten new queue items per company. Annual/quarterly filings take priority, then other SEC events, then issuer news. Already prepared event IDs are tracked against the exact research packet, avoiding repeated preparation of unchanged work. Preparation does not remove review obligations.
5. Saves discovery/preparation state to the separate state branch; canonical research is untouched. Failed fetches remain errors. Run summaries and request artifacts are retained for 30 days.

The state branch stores JSON only. Updates are fast-forward and serialized; they do not overwrite `main`. Failure to restore an existing queue stops the run. A branch test does not write production state. No email, chat messages, paid model calls, issue creation or automatic research approval is configured.

The repository variable `SEC_USER_AGENT` can supply your identifying application/contact string. The default identifies Stock Brain and its repository URL. The shared fetcher limits itself to two requests/second and honors bounded retry/backoff. SEC's published ceiling is ten requests/second across clients: [EDGAR access guidance](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data).

## Coverage and freshness

| Layer | Current handling |
| --- | --- |
| Company filings | SEC discovery for all ten covered issuers |
| Issuer announcements | Microsoft, NVIDIA, AMD, Broadcom, Lockheed Martin and RTX RSS |
| Missing issuer-feed adapters | Micron, AeroVironment, Oracle and Palantir remain explicitly partial |
| Prices, multiples and consensus | No live feed; the assistant abstains |
| Review status | Exact packet/profile approval hashes; actual reviewer identity retained |
| Scan health | Errors, missing state, changed evidence version and scans older than 48 hours are visible |

Research cutoff, latest financial period, publication date, review date and last scan time are different concepts. A recent scan does not renew an old research date. A source marked “checked” does not imply exhaustive knowledge of all news. A company without issuer-feed coverage cannot satisfy an explicit current/latest question.

The first live scan on 2026-10-18 completed for all ten issuers without fetch errors and discovered 112 pending candidates. This is an initial overlap backlog, not 112 confirmed material developments. The checked-in report is a dated bootstrap snapshot, not a perpetual freshness badge.

## Review cadence

Review high-priority financial and material-event filings promptly. Batch ordinary announcements by company. Reserve a weekly pass for the oldest pending items, missing sources, feed health, and stale companies. A larger universe needs a review budget: expand coverage only when the pending backlog stays manageable. The current workflow prepares evidence automatically; it does not promise fully autonomous financial judgment.

For each selected company:

```bash
export SEC_USER_AGENT='Your application name and contact'
python scripts/disclosure_monitor.py --summary build/monitoring/summary.md
python scripts/prepare_updates.py --limit 2
# Inspect build/research/TICKER/request.json and update-plan.json.
# Use the existing optional runner explicitly, or author a corrected packet.
python scripts/research_company.py draft --packet path/to/proposal.json --apply
python scripts/research_company.py review --packet research/pilot/TICKER.json --attestation path/to/review.json
python scripts/stock_brain.py build
python scripts/stock_brain.py check
```

Read the relevant original exhibits before asserting financial results. The request carries the prior packet and the change plan; update only affected sections where the plan permits. Preserve facts unaffected by the new disclosure, distinguish reported results from guidance, and document remaining gaps. Rebind translations and rerun the quality gates. Approval invalidates old translations for changed claims. Queue items resolve only after their URL or SEC filing accession is present in a hash-bound reviewed packet; mentioning an event in a draft is insufficient.

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
