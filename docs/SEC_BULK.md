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

The earlier undeclared-identity denial was resolved using the operator-supplied
contact on the same Render origin. Pilot Company Facts retrievals and both archive
HEAD checks returned HTTP 200 on October 22. See [SEC_ACCESS.md](SEC_ACCESS.md)
for the actual evidence; access checks alone do not prove broad coverage.

## Scheduled acquisition and publication

The existing `coverage-daily.yml` workflow runs at **09:23 UTC daily**, after the
normal nightly SEC publication window. It reads a private `SEC_USER_AGENT` secret,
streams each official archive once, and stops on any denial or invalid response.
No new paid service or source credential is needed. The archive downloader rejects
redirects and bounds each file at 8 GiB with disk headroom and download deadlines.

The release builder opens both archives once and drains bounded identity and
financial batches, instead of stopping after the first 5,000/100 records. It has
a 90-minute import budget and preserves storage headroom within the existing
512 MiB release cap. Progress, explicit stopping reason, per-issuer errors and
source hashes are included in the verified data generation. A time/storage stop
is partial coverage, not a successful all-market completion.

Unchanged Company Facts bytes and unchanged normalized content keep their existing
history version and original observation date. The new collection check is stored
separately. Same-accession corrections and changed review evidence still create
versions. Identical recent filing metadata and identity payloads are not copied
again merely because a new archive was downloaded.

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

Matched-issuer and error checkpoints are durable; skipped private filers checkpoint every 100 records. A crash between publication and checkpointing
can replay an issuer safely. Bulk jobs claim their own ID; online collectors claim
only `refresh_company`, including when reclaiming expired leases. Neither consumes
the other queue. Operate this as a **single writer**: do not run a live collector,
another bulk CLI or a release builder concurrently against the same database.
The public web replica is never an ingestion destination.

The release builder supports the same path after restoring the previous verified
database and refreshing directories:

```bash
python scripts/coverage_release.py build --tag coverage-YYYYMMDD-RUN-ATTEMPT --sec-bulk-manifest /data/sec/acquisition.json
```

It completes successive batches and includes progress in the release manifest,
retaining checkpoint/error tables in the backup. Publication occurs only after
local restore verification; the web mirror additionally waits for verification
of the actual uploaded assets restored into an empty database.

## Validation and boundaries

- Compressed archive limit: 8 GiB; expanded metadata total: 96 GiB; member limit:
  64 MiB; maximum 1,200,000 members. The actual 2026-10-22 submissions ZIP has
  995,360 entries and an 87,678,109-byte central directory, measured via its ZIP64
  trailer. The previous 600,000-entry cap correctly rejected it; the bound now
  allows measured current size with modest growth headroom. Archive processing
  runs on the Actions runner, not the web service. One issuer JSON is read at a time. ZIP traversal,
  symlinks, encryption, duplicates, unexpected names, excessive sizes/ratios,
  invalid hashes, duplicate JSON fields and CIK mismatches are rejected.
- The real submissions ZIP also contains `placeholder.txt`. Only that exact
  non-issuer marker is allowed, at most 1 KiB, with link/encryption/duplicate and
  CRC checks; it is never parsed as a company. A full central-directory inventory
  found no other exceptional names. Observed expanded totals: submissions
  5,760,756,934 bytes; Company Facts 19,327,197,919 bytes across 20,488 entries.
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
- Schema 6 stores large JSON payloads as compressed, content-addressed objects
  while preserving every version and original source date. Version-2 releases
  distribute independently hashed 32 MiB raw chunks. The restored database still
  has a **512 MiB** safety cap; check measured capacity before each large backfill.
  See [COVERAGE_STORAGE.md](COVERAGE_STORAGE.md) for migration, verification and
  growth boundaries. A capacity failure preserves the last good public release.
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
