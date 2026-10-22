# Standalone Stock Brain

The app runs ordinary Python and browser JavaScript, without ChatGPT, Sites, a connected-app session, or a paid model API. Anyone who can reach its public URL can use the desk without signing in. Cited retrieval and deterministic financial calculations power its answers. It is not a general language-model chat service and does not automatically read, judge, translate, or approve new research. New disclosures enter the review queue; review work remains separate. Public-source failures remain visible.

## Deployment

Use one Python web-service instance. Waitress binds to `0.0.0.0:$PORT`.

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

Replace only Render service `NEW-finlotus` (`srv-d8i2kla8qa3s73e10t50`), currently at `https://finlotus-1.onrender.com`. Keep its current plan, region and instance count. Do not change the other `finlotus` service or code in `eladyesh/finlotus`. Remove unrelated application secrets from the replaced service; Stock Brain needs none.

This setup adds no web service, database, disk, or cron service. Normal hosting/bandwidth/build limits still apply. Backup uses the public repository's standard GitHub Actions Linux runner and built-in `GITHUB_TOKEN`, with contents-write permission. Render does not store a personal GitHub token.

## Collection and persistence

1. On a cold start, resolve the GitHub data branch to one immutable commit and restore its four payloads. Failure to restore an expected checkpoint stops startup; it never silently resets the queue. An existing local checkpoint needs no GitHub connection.
2. Rebuild the desk against this release's hash-bound research, preserving financial/source timestamps.
3. Serve public reads. Collect SEC, issuer announcements and market data in a separate process at startup and daily at the configured local time. IANA timezone rules handle Israel daylight-saving changes.
4. Validate the complete result and publish all four files with one atomic checkpoint replacement. Partial source failures retain previous data and stay labelled. Unsafe refreshes retain the entire last checkpoint and record a failed attempt; failures retry after an hour. Visitors cannot trigger collection.
5. `.github/workflows/runtime-backup.yml` checks the public app twice hourly, validates new checkpoints, pushes without force and verifies the resulting ref. Older/unchanged data is skipped. The `STOCK_BRAIN_URL` repository variable can override the default app URL.

Render's ordinary filesystem is ephemeral. A restart recovers the **last successful GitHub backup**, not necessarily the last collection. GitHub schedules can be delayed or disabled; the actual data-branch commit determines the recovery point. Data collected between backups can be recollected. Research approvals are never made in this ephemeral runtime. A persistent disk is an optional improvement if tighter recovery guarantees are required.

## Public endpoints

| Route | Purpose |
| --- | --- |
| `/` | Hebrew research desk |
| `/api/snapshot` | Research, financial history, prices and queue |
| `/api/status` | Refresh history, errors, latest attempt and schedule |
| `/api/state` | Consistent four-file backup checkpoint |
| `/healthz` | Fast readiness check without external calls |

All routes accept only GET/HEAD. Assets are allowlisted. Repository files, environment variables and admin commands are not served. The browser connects only to its own origin. Q&A uses `site/engine.mjs` in the browser, so visitor questions do not create model charges or source requests.

## Operations

Run a manual collection from the service shell:

```bash
python scripts/runtime_data.py refresh --state-dir /tmp/stock-brain
```

For an immediate backup, use GitHub Actions **Back up standalone Stock Brain → Run workflow**. Do not resume the retired ChatGPT task or legacy disclosure collector alongside this writer. Inspect `/api/status`, Render logs and backup results before claiming reliability. A schedule is not proof of future success. Preserve known source limitations, including Oracle's announcement feed when it fails. Passing tests does not approve research or resolve existing financial QA flags.
