# Standalone Stock Brain

The app runs ordinary Python and browser JavaScript, without ChatGPT, Sites, a connected-app session, or a paid model API. Anyone who can reach its public URL can use the desk without signing in. Cited retrieval and deterministic financial calculations power its answers. It is not a general language-model chat service and does not automatically read, judge, translate, or approve new research. New disclosures enter the review queue; review work remains separate. Public-source failures remain visible.

## Deployment

Use one Python web-service instance with Node.js 20+ available on PATH. Waitress binds to `0.0.0.0:$PORT`. Startup checks that Node is installed.

| Setting | Value |
| --- | --- |
| Repository | `https://github.com/eladyesh/stock-brain` |
| Branch | `main` |
| Root directory | empty |
| Build command | `pip install -r requirements-web.txt` |
| Start command | `python scripts/serve_public.py` |
| Health check | `/healthz` |
| `STOCK_BRAIN_STATE_DIR` | `/tmp/stock-brain` |
| `STOCK_BRAIN_BOOTSTRAP_GITHUB` | `1` |
| `STOCK_BRAIN_REFRESH_ENABLED` | `1` |
| `STOCK_BRAIN_REFRESH_ON_START` | `1` |
| `STOCK_BRAIN_TIMEZONE` | `Asia/Jerusalem` |
| `STOCK_BRAIN_REFRESH_TIME` | `08:30` |
| `STOCK_BRAIN_SEC_ENABLED` | `0` while the observed SEC access denial is unresolved |

Replace only Render service `NEW-finlotus` (`srv-d8i2kla8qa3s73e10t50`), currently at `https://finlotus-1.onrender.com`. Keep its current plan, region and instance count. Do not change the other `finlotus` service or code in `eladyesh/finlotus`. Remove unrelated application secrets from the replaced service; Stock Brain needs none.

This setup adds no web service, database, disk, or cron service. Normal hosting/bandwidth/build limits still apply. Backup uses the public repository's standard GitHub Actions Linux runner and built-in `GITHUB_TOKEN`, with contents-write permission. Render does not store a personal GitHub token.

## Collection and persistence

1. On a cold start, resolve the GitHub data branch to one immutable commit and restore its four payloads. Failure to restore an expected checkpoint stops startup; it never silently resets the queue. An existing local checkpoint needs no GitHub connection.
2. Rebuild the desk against this release's hash-bound research, preserving financial/source timestamps.
3. Serve public reads. Collect SEC, issuer announcements and market data in a separate process at startup and daily at the configured local time. IANA timezone rules handle Israel daylight-saving changes.
4. Validate the complete result and publish all four files with one atomic checkpoint replacement. Partial source failures retain previous data and stay labelled. Unsafe refreshes retain the entire last checkpoint and record a failed attempt; failures retry after an hour. Visitors cannot trigger collection.
5. `.github/workflows/runtime-backup.yml` checks the public app twice hourly, validates new checkpoints, pushes without force and verifies the resulting ref. Older/unchanged data is skipped. It then exercises public answers, rejects collection older than 36 hours, and restores the actual GitHub checkpoint into empty temporary state. Queue entries, review decisions, financial histories and prices are compared with the live app. Failures fail the Actions job; source-level partial refreshes and open QA flags remain explicit in the report. The `STOCK_BRAIN_URL` repository variable can override the default app URL.

Render's ordinary filesystem is ephemeral. A restart recovers the **last successful GitHub backup**, not necessarily the last collection. GitHub schedules can be delayed or disabled; the actual data-branch commit determines the recovery point. Data collected between backups can be recollected. Research approvals are never made in this ephemeral runtime. A persistent disk is an optional improvement if tighter recovery guarantees are required.

## Public endpoints

| Route | Purpose |
| --- | --- |
| `/` | Hebrew research desk |
| `/api/snapshot` | Research, financial history, prices and queue |
| `/api/status` | Refresh history, errors, latest attempt and schedule |
| `/api/state` | Consistent four-file backup checkpoint |
| `/healthz` | Fast readiness check without external calls |
| `POST /api/ask` | Cited evidence answers; see [API contract](API.md) |

All routes except `/api/ask` accept only GET/HEAD. Assets are allowlisted. Repository files, environment variables and admin commands are not served. The browser connects only to its own origin. Q&A uses `site/engine.mjs` on the server through one bounded Node worker at a time. Requests have an 8 KiB body limit, a 4,000-character question limit, an eight-second worker timeout and a 96 MiB V8 heap cap. Busy requests receive 503 with Retry-After. This protects process concurrency, not a complete per-user quota or DDoS service. Questions are not persisted or logged by application code and never create model charges or source requests. If the endpoint is unavailable, the browser uses its dated loaded snapshot and labels that fallback.

The engine supports reviewed business/risk/comparison questions, exact supported financial periods, and explicit latest-*stored* fiscal quarter/year questions in Hebrew and English. “Latest available” refers to the selected dataset period, not verified current reporting. Missing or unreviewed data still causes abstention; it never searches backward for an easier period.

## SEC access limitation

On 2026-10-22 the actual Render service received HTTP 403 with the SEC title “Your Request Originates from an Undeclared Automated Tool”. SEC requests are paused on this service via `STOCK_BRAIN_SEC_ENABLED=0`; issuer announcements and market collection continue. There is no proxy, browser impersonation, alternate-IP retry or paid replacement. Existing financial records keep their original collection dates. A shared collector circuit breaker also skips remaining SEC requests after the first 403 in a run.

Restoring SEC collection requires legitimate resolution of the source's access policy. Configure `SEC_USER_AGENT` with an approved identifying application/contact string privately in Render and obtain permitted access before setting `STOCK_BRAIN_SEC_ENABLED=1`. A changed header alone is not proof that access is restored. Check [SEC developer resources](https://www.sec.gov/about/developer-resources) and [SEC webmaster guidance](https://www.sec.gov/about/webmaster-frequently-asked-questions). No contact address was invented or published in the code.

Financial refresh validation rejects empty/truncated schedules, missing previously available source cells, mismatched reported numbers, invalid arithmetic, inconsistent issuer/period maps and unsafe model eligibility. The reproducible [QA ledger](FINANCIAL_QA_STATUS.json) records the existing 77 open source/comparability flags. Integrity checks do not resolve these flags or constitute a new review of filings.

## Operations

Run a manual collection from the service shell:

```bash
python scripts/runtime_data.py refresh --state-dir /tmp/stock-brain
```

For an immediate backup, use GitHub Actions **Back up standalone Stock Brain → Run workflow**. Do not resume the retired ChatGPT task or legacy disclosure collector alongside this writer. Inspect `/api/status`, Render logs and backup results before claiming reliability. A schedule is not proof of future success. Preserve known source limitations, including Oracle's announcement feed when it fails. Passing tests does not approve research or resolve existing financial QA flags.

The current Render service uses the public Git repository source and has automatic code deploys disabled. After merging a tested code release, trigger **Manual Deploy → Deploy latest commit** on this service and check `/healthz`, `/api/ask` and the backup workflow. Data collection and backup schedules run independently of code deployment and ChatGPT. The deployment history and remaining work are recorded in [DEVELOPMENT_LOG.md](DEVELOPMENT_LOG.md).
