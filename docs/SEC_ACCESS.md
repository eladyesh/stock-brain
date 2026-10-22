# SEC access diagnosis and recovery

## Verified recovery on 2026-10-22

The earlier Render HTTP 403 identified an undeclared automated tool. Its fallback
User-Agent lacked an operator contact. The operator subsequently supplied a
contact, which is now stored privately in Render and as the GitHub Actions
`SEC_USER_AGENT` secret. The contact is never committed or returned by public APIs.

A single controlled request from the same Render service at 16:50:19 UTC returned
HTTP 200 and valid Microsoft Company Facts (4,888,108 bytes; SHA-256
`dd0308149a8e96497989ed7c690b5a49a00bef9ceafbb24638bda41e8ae938dd`). After enabling
`STOCK_BRAIN_SEC_ENABLED=1`, the production refresh at 16:52:35 UTC succeeded for
all ten pilot submissions and financial histories. Oracle's separate issuer RSS
403 still makes the pilot refresh partial; it is not an SEC failure.

Subsequent HEAD requests from the same existing Render service returned HTTP 200
for both official archives: submissions 1,570,500,398 bytes and Company Facts
1,411,028,297 bytes. These are access/size checks, not completed archive ingestion.
No IP rotation, proxy, identity impersonation, redirect or denial retry was used.
The prior pause descriptions in historical development entries are superseded.

## Operational contract

- Keep the real application/contact identity private. The public configuration
  endpoint reports booleans and `network_checked: false`; it is not an access test.
- `scripts/sec_acquire.py` uses the official fixed ZIP URLs, streams to bounded
  disk files, verifies length and ZIP signature, records retrieval evidence and
  SHA-256, and stops on the first denial. No automatic retry or fallback exists.
- The daily GitHub release builder is the broad collection writer. Render uses a
  verified, immutable data generation and retains the last good generation if a
  collection or restore fails. See [SEC_BULK.md](SEC_BULK.md).
- If a new denial occurs, retain prior data and investigate the declared identity
  and source response. SEC's FAQ provides webmaster@sec.gov as its support route.
  Sending a support message requires operator authorization. Do not change hosts,
  IPs or identities to evade a source denial.

Reading public EDGAR APIs requires neither authentication nor an API key. These
are different from APIs for submitting filings. The documented ceiling is ten
requests/second across machines; this collector uses two per second, and multiple
independent collectors must share an overall budget.

## Broad coverage after access works

Use the official nightly `companyfacts.zip` and `submissions.zip` archives for
backfill, then incrementally process changed companies. SEC describes bulk ZIPs
as its most efficient option for large downloads and republishes them around
03:00 Eastern. The existing [bulk importer](SEC_BULK.md) accepts legitimately
obtained files. An importer is not proof that those archives are accessible.

## Official references

- [Declared identity and fair access](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data)
- [Undeclared-tool and access-denied FAQ](https://www.sec.gov/about/webmaster-frequently-asked-questions)
- [Public APIs, authentication and bulk archives](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
