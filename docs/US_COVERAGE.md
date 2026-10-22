# U.S. coverage infrastructure

The goal is automated coverage expansion across U.S.-listed companies. The code
now discovers issuer/listing associations, queues bounded work, collects and
normalizes filings incrementally, retains provenance and exposes individual
companies without shipping the entire market to each browser. The existing ten
reviewed profiles remain a separate, small research corpus.

This is a working collection foundation, not a claim of complete market research.
No market-wide source import or production worker was activated in this release.
The current service has SEC access paused and an ephemeral filesystem.

## Components and data boundaries

| Component | Responsibility |
| --- | --- |
| `coverage_store.py` | Versioned SQLite schema, stable padded CIKs, separate tickers/share classes/venues, listing evidence, versioned per-company payloads and job events |
| `coverage_cli.py` | Seed the pilot, validate/import official listing snapshots, explicitly queue batches and inspect state |
| `coverage_worker.py` | Check submissions, fetch Company Facts on a new supported filing, normalize financial history and stage a source-linked change draft |
| `coverage_cycle.py` | Repeatedly select eligible issuers, run bounded batches and optionally refresh listings every 24 hours |
| `coverage_api.py` | Paginated metadata search and per-company detail; no network acquisition on page views |
| `coverage_runtime.py` | Bootstrap pilot data with compare-and-swap protection against concurrent newer collections |
| `coverage_backup.py` | Consistent SQLite online backup, integrity/hash manifest and verified local restore |

CIK identifies an issuer; a ticker is not an immutable identity. Listing history
retains source dates, venue and inactive status. Only an explicit validated,
unfiltered complete snapshot may retire absent listings from that same source.
Older snapshots are audited without rolling the registry back. Recurring imports
are partial and never infer delisting from absence.

Collection and reviewed research have different states. Registration creates no
financial coverage. New financial observations are validated and stored with their
actual source URL, hash, retrieval time and filing identity. Automatic change
drafts contain explicit periods, values, gated deltas and citations. They are
unreviewed; they never approve a thesis, create an investment recommendation or
modify a reviewed Markdown profile. Review remains a separately evidence-bound
pipeline. The new registry UI shows these distinctions.

## One-host operation

Use a durable **local** filesystem and one shared SQLite database for the public
app and collection processes. SQLite WAL is appropriate for bounded same-host
workers; do not place it on a shared network filesystem or claim independent
multi-host scaling. Set `STOCK_BRAIN_COVERAGE_DB` to this database in both processes.
The worker's raw response cache under `build/research-cache/` also needs a capacity policy.

The commands below use `build/coverage.sqlite3` for a reproducible local pilot.
Replace that path with an actually provisioned durable path before production:

```bash
python scripts/coverage_cli.py --db build/coverage.sqlite3 seed
python scripts/coverage_cycle.py --db build/coverage.sqlite3 --readiness
python scripts/coverage_cli.py --db build/coverage.sqlite3 status --limit 10
```

The web app additionally copies the pilot's validated financial histories on
startup. CLI `seed` copies only reviewed research and registry identities. Neither
operation fetches the market or changes `config/universe.json`.

After legitimate SEC access is available, configure `SEC_USER_AGENT` privately
with the real application's name and real operator contact. Do not use an invented
email or impersonate a browser. `--readiness` validates configuration and reports
persisted cooldowns; `network_checked: false` means it is **not** proof of access.
Keep `STOCK_BRAIN_SEC_ENABLED=0` while the existing access denial remains unresolved.

Import an operator-supplied official snapshot without any network request:

```bash
python scripts/coverage_cli.py --db build/coverage.sqlite3 import-listings \
  --file /path/to/company_tickers_exchange.json \
  --source-url https://www.sec.gov/files/company_tickers_exchange.json \
  --retrieved-at ACTUAL_SOURCE_RETRIEVAL_ISO_TIMESTAMP
```

When access is permitted, a single explicit fetch is available with
`import-listings --fetch`. Actual raw bytes, source hash and retrieval time are
preserved. Input schema, duplicate/conflicting identities, truncated/empty files
and filtered complete snapshots are rejected before registry changes.

Run one bounded pass, inspect its JSON result, then run the same process under
the chosen host's supervisor for unattended operation:

```bash
python scripts/coverage_cycle.py --db build/coverage.sqlite3 --limit 10
python scripts/coverage_cycle.py --db build/coverage.sqlite3 \
  --continuous --limit 25 --interval-seconds 60 --refresh-listings
```

The second command explicitly opts into periodic official listing retrieval.
Without `--refresh-listings`, only the current registry is processed. One pass is
the default; no scheduler, external service or paid resource is created by these
commands. SIGTERM/SIGINT finish the in-flight bounded cycle and stop before the
next cycle. A host kill may interrupt a job; its lease expires and another worker
can retry it. Staged incomplete data is never published.

Eligible companies are selected by collection/attempt age, with a 24-hour minimum
age, rather than just the age of a changed financial history. An unchanged issuer
or one without supported forms therefore cannot monopolize each batch. Active
jobs deduplicate; completed state persists across restarts. Jobs use expiring
leases and bounded retries. Publication checks ownership and expiry inside the
write transaction; a stale worker cannot overwrite a winner's data.

The provider uses shared persistent request slots at **two requests per second**
for this database, including retries and listing imports. HTTP 403 pauses the
source and marks the affected job blocked. HTTP 429/temporary failures persist
cooldowns and retry safely. No identity rotation, alternate IP, proxy or paid
fallback is implemented. Independent pilot collection uses its existing guard;
before broad activation, avoid simultaneous SEC writers outside this shared store
or make them use the same rate coordinator. No distributed rate-limit claim is made.

Blocked jobs are excluded from automatic selection. After the source-access
problem is actually resolved and its cooldown has expired, an operator can queue
a specific affected company with `coverage_cli.py --db PATH enqueue --ticker MSFT`.
The blocked job remains in the audit history; the explicit new job does not clear
source cooldowns or change review status.

Submissions are checked first. Company Facts is fetched only for a new supported
accession or missing history. The checkpoint does not advance until the new
filing has usable reported observations in the returned data. A failed/truncated
refresh retains the last good history. Exact-definition, share/debt-scope and
period QA gates remain active for every issuer. Unsupported forms yield explicit
review-required coverage rather than fabricated financial data.

## Backup and recovery

The pilot's four-file GitHub backup excludes this database and raw cache. A local
backup on the same ephemeral host is **not durable recovery**. Use an already
approved off-host destination for the snapshot and manifest, and test restoring
them onto a fresh host before expanding production collection.

```bash
python scripts/coverage_backup.py backup build/coverage.sqlite3 build/coverage-backup.sqlite3
python scripts/coverage_backup.py status build/coverage-backup.sqlite3
python scripts/coverage_backup.py restore build/coverage-backup.sqlite3 \
  build/coverage-backup.sqlite3.manifest.json build/restored-coverage.sqlite3
```

Online backup captures a consistent database including committed WAL data, checks
integrity, records SHA-256 and publishes the manifest last. Interrupted two-file
publication is unverified until the matching manifest is present. Restore checks
both files and refuses unsafe overwrites or live WAL sidecars. Replacing an
existing destination additionally requires `--replace --quiesced`; stop every
reader/writer first. This tool neither uploads backups nor provisions storage.

## Scope and next engineering milestones

1. **Source and durability activation.** Resolve permitted SEC access, verify a
   durable database path and off-host recovery, then run a small real pilot and
   inspect source timestamps, failure rates, queue lag, disk and memory growth.
2. **Eligible universe reconciliation.** The SEC association file is a candidate
   pool, not a guaranteed complete security master. Reconcile Nasdaq/NYSE/NYSE
   American listing status and instrument type, including ADRs, common REIT
   shares, IPOs, ticker changes and delistings. Preserve unknown venues/types
   until identified. Registration currently retains OTC/unassigned rows unless
   explicitly excluded; these are not a claim that those securities belong to
   the product's intended coverage. U.S.-listed does not mean U.S.-domiciled.
3. **Accounting adapters.** Current automated normalization supports 10-K/10-Q
   and amendments using US-GAAP Company Facts. Foreign-issuer 20-F/6-K/IFRS,
   banks, insurers, REIT-specific measures and custom XBRL tags require dedicated
   mappings and evidence gates. Missing data must remain visible.
4. **Automated research drafting and review.** Connect new disclosure evidence to
   the existing provider-neutral draft/review protocol with a cost budget and
   exact source-bound review gates. Do not mark generated narrative as reviewed
   merely because ingestion succeeded. Qualitative answers still use the curated
   corpus; automatic change summaries are numerical drafts.
5. **Operational scale.** Establish retention/archival for payload versions,
   listing snapshots, job/source events and raw cache, with recovery tests before
   pruning. Measure real workloads before deciding on PostgreSQL/object storage
   and multiple hosts. The SQLite implementation is a single-host foundation;
   no retention job or multi-host deployment is included in this release.

Validation includes deterministic concurrency/lease tests, source-gate failure
tests, a 50,000-synthetic-issuer paging fixture, restart progression and real local
SQLite backup/restore. Synthetic fixtures verify behavior, not production
throughput, complete market discovery or source accessibility.

Official source contract: [SEC EDGAR data access](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data).
The SEC's published limit is ten requests per second; this implementation uses a
lower shared rate. The SEC also cautions about the accuracy and scope of its
ticker/CIK association files.
