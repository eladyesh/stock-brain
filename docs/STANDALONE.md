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
| `STOCK_BRAIN_SEC_ENABLED` | `1` after the verified 2026-10-22 identity/access recovery |

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
| `/api/coverage` | Separate registry and collection-queue counts |
| `/api/companies?q=&limit=25&offset=0` | Search/paginate registry metadata, maximum 100 issuers |
| `/api/companies/{CIK-or-ticker}` | One issuer's collected data and distinct dated research |
| `/healthz` | Fast readiness check without external calls |
| `POST /api/ask` | Cited evidence answers; see [API contract](API.md) |

All routes except `/api/ask` accept only GET/HEAD. Assets are allowlisted. Repository files, environment variables and admin commands are not served. The browser connects only to its own origin. Q&A uses `site/engine.mjs` on the server through one bounded Node worker at a time. Requests have an 8 KiB body limit, a 4,000-character question limit, an eight-second worker timeout and a 96 MiB V8 heap cap. Busy requests receive 503 with Retry-After. This protects process concurrency, not a complete per-user quota or DDoS service. Questions are not persisted or logged by application code and never create model charges or source requests. If the endpoint is unavailable, the browser uses its dated loaded snapshot and labels that fallback.

The engine supports reviewed business/risk/comparison questions, exact supported financial periods, and explicit latest-*stored* fiscal quarter/year questions in Hebrew and English. “Latest available” refers to the selected dataset period, not verified current reporting. Missing or unreviewed data still causes abstention; it never searches backward for an easier period.

## SEC access and broad collection

The earlier undeclared-tool denial was resolved on October 22 with the operator's
private application/contact identity. The Render pilot now has SEC collection
enabled and its verified refresh collected all ten financial histories. The
separate Oracle RSS denial remains visible as partial issuer-source coverage.
See [SEC_ACCESS.md](SEC_ACCESS.md) for timestamps and request evidence.

The GitHub daily broad pipeline downloads official SEC archives, matches current
US exchange stock listings to issuer CIKs, and publishes only a verified data
generation. Render restores that generation without writing into its live mirror.
See [SEC_BULK.md](SEC_BULK.md) for schedule, checkpoints and explicit coverage gaps.


## Expanding beyond the pilot

The web app seeds a separate SQLite coverage registry from the ten reviewed pilot companies. It does not start a market-wide collector. The production service now uses `STOCK_BRAIN_COVERAGE_MIRROR=1` to load a verified, independently backed-up broad directory from daily GitHub data releases; see [broad market operations](BROAD_MARKET_OPERATIONS.md). The four-file pilot backup **does not include** this database. Its durability comes from the separate verified release and cold-restore path.

For the alternative same-host worker mode, configure `STOCK_BRAIN_COVERAGE_DB` on a durable path shared with the opt-in `coverage_cycle.py` process. Do not run that collector against a release-mirror replica: local writes will not become authoritative releases. Without either durable mode, broad collection remains ephemeral and cannot be restored from the pilot's four-file backup. See [coverage operation and activation](US_COVERAGE.md) before running continuous collection.

## Operations

Run a manual collection from the service shell:

```bash
python scripts/runtime_data.py refresh --state-dir /tmp/stock-brain
```

For an immediate backup, use GitHub Actions **Back up standalone Stock Brain → Run workflow**. Do not resume the retired ChatGPT task or legacy disclosure collector alongside this writer. Inspect `/api/status`, Render logs and backup results before claiming reliability. A schedule is not proof of future success. Preserve known source limitations, including Oracle's announcement feed when it fails. Passing tests does not approve research or resolve existing financial QA flags.

The current Render service uses the public Git repository source and has automatic code deploys disabled. After merging a tested code release, trigger **Manual Deploy → Deploy latest commit** on this service and check `/healthz`, `/api/ask` and the backup workflow. Data collection and backup schedules run independently of code deployment and ChatGPT. The deployment history and remaining work are recorded in [DEVELOPMENT_LOG.md](DEVELOPMENT_LOG.md).
