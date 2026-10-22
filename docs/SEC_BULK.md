# SEC access and bulk ingestion

## Verified source contract (October 22, 2026)

SEC public data APIs do not require an API key. A truthful declared User-Agent
with an operator contact and compliance with fair access are still required.
The SEC limit is 10 requests per second across the user's machines; the current
online collector uses a more conservative shared two-per-second reservation.
Identification does not guarantee access or override an existing denial.

Official documentation:

- https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data

The SEC publishes complete JSON ZIP archives nightly, approximately 03:00 Eastern:

| Archive | Official source | Purpose |
| --- | --- | --- |
| Submissions | https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip | Issuer identity, tickers, venues and filing metadata |
| Company Facts | https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip | Structured financial observations |

These cover SEC filers, not a guaranteed complete universe of currently tradable
stocks. Nasdaq Trader directories establish current exchange/symbol slots;
submissions match a slot to CIK only when ticker, venue and issuer name agree.
Ticker and exchange arrays are not presumed to have matching positions.

The existing Render origin received an SEC automated-access denial. Keep
`STOCK_BRAIN_SEC_ENABLED=0`. Do not move the same blocked acquisition to GitHub,
another host, a proxy or a browser, or disguise the client. Resume live SEC
acquisition only after legitimate access is resolved with the operator/provider
and a real contact is configured. No contact, credential or successful SEC
download was invented in this implementation.

## Implemented offline path

`scripts/sec_bulk.py` consumes archives already obtained through legitimate
access. It has **no network acquisition or network fallback**. The acquisition
manifest records actual retrieval time and hashes; those are evidence supplied
by the operator, not an SEC signature or proof that the bytes are authentic.

Create a local manifest with this shape, replacing every placeholder with the
actual file, timestamp and hash. Do not commit multi-gigabyte archives to Git.

```json
{
  "format": "stock-brain-sec-bulk-v1",
  "submissions": {
    "file": "submissions.zip",
    "url": "https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip",
    "retrieved_at": "ACTUAL_ISO_TIMESTAMP_WITH_TIMEZONE",
    "sha256": "ACTUAL_LOWERCASE_SHA256"
  },
  "companyfacts": {
    "file": "companyfacts.zip",
    "url": "https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip",
    "retrieved_at": "ACTUAL_ISO_TIMESTAMP_WITH_TIMEZONE",
    "sha256": "ACTUAL_LOWERCASE_SHA256"
  }
}
```

On an ingestion host with adequate disk/memory, inspect before import:

```bash
python scripts/sec_bulk.py inspect --manifest /data/sec/acquisition.json
python scripts/sec_bulk.py issuers --manifest /data/sec/acquisition.json --db /data/coverage.sqlite3 --limit 5000
python scripts/sec_bulk.py financials --manifest /data/sec/acquisition.json --db /data/coverage.sqlite3 --limit 100
```

Repeat issuer batches until `complete: true`, then financial batches until
complete. `cycle` combines these phases and resumes automatically. A complete
scan can still include quarantined failures; inspect `failed` and
`sec_bulk_errors`. Re-running an unchanged completed archive is a no-op.
New archive hashes, retrieval evidence or directory generations create a new
pass. A fresh directory (at most 36 hours old) is required for identity matching.

Each issuer checkpoint is durable. A crash between publication and checkpointing
can replay an issuer safely. Jobs claim their own ID and do not consume an online
collector's queue. Operate this as a **single writer**: do not run a live collector,
another bulk CLI or a release builder concurrently against the same database.
The public web replica is never an ingestion destination.

The release builder supports the same path after restoring the previous verified
database and refreshing directories:

```bash
python scripts/coverage_release.py build --tag coverage-YYYYMMDD-RUN-ATTEMPT --sec-bulk-manifest /data/sec/acquisition.json
```

It performs up to 5,000 identity scans and 100 financial jobs, includes progress
in the release manifest, and retains checkpoint/error tables in the backup.
Archive acquisition/staging on a scheduled host is not enabled in production.
The existing daily workflow therefore truthfully reports `not_configured` for
SEC bulk ingestion and continues its working directory refresh.

## Validation and boundaries

- Compressed archive limit: 8 GiB; expanded metadata total: 96 GiB; member limit:
  64 MiB; maximum 600,000 members. One issuer JSON is read at a time. ZIP traversal,
  symlinks, encryption, duplicates, unexpected names, excessive sizes/ratios,
  invalid hashes, duplicate JSON fields and CIK mismatches are rejected.
- ZIP members are never extracted. `inspect` validates the archive hash and
  inventory; member CRC, JSON and issuer identity are checked as members are read.
- Evidence carries both archive and member hashes plus original retrieval time.
  No nonexistent HTTP cache path is claimed for bulk-derived history.
- Financial history keeps the existing US GAAP, exact-period, unit, provenance and
  quality gates. New archives recheck Company Facts even when the latest accession
  is unchanged, so same-accession corrections are not silently skipped.
- Older source evidence cannot overwrite newer stored history. Failures retain
  the prior version. Automated drafts never approve canonical research.
- Recent filing metadata includes foreign forms. **20-F/40-F/6-K and IFRS financial
  normalization remain unsupported**, and are flagged rather than converted into
  invented US GAAP results. Older submission shards are inventoried, not ingested.
- Current public SQLite release bounds remain 512 MiB restored / 128 MiB
  compressed. This is not yet full-market financial storage. Implement a verified
  sharded/object-storage or database migration before a mass financial backfill;
  the builder fails closed at those limits and preserves the last good release.
- OTC stocks need an authoritative OTC master in addition to exchange directories.
  FINRA's public OTC Daily List describes changes, not a complete current master:
  https://developer.finra.org/docs (Equity / OTC Daily List).

## Alternative vendor investigation

The connected Financial Datasets company-facts and income-statement probes both
returned an account balance of $0.00 on October 22, 2026; neither returned data.
Connected-app access also does not provide a server API credential.

The provider's October 21 terms distinguish in-app redistribution from raw/bulk
exports. Even a Professional redistribution plan does not by itself authorize
publishing our full downloadable SQLite snapshot. See:
https://www.financial-datasets.ai/terms-of-use .

Both collection into this public-release pipeline and packaging retained vendor
observations now require `STOCK_BRAIN_FD_BULK_EXPORT_PERMISSION=1`, reflecting a
**separate written grant**. The existing display-license, credential, enablement
and budget gates also remain. Do not set these flags merely to make a job pass.
A future private-data backend can implement a separately licensed display path;
it must not leak raw vendor payloads through public release assets.
