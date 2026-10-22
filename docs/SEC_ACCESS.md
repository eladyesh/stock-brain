# SEC access diagnosis and recovery

## Verified on 2026-10-22

- The actual Render service `NEW-finlotus` received HTTP 403 with the title
  "Your Request Originates from an Undeclared Automated Tool" in the earlier probe.
- Its Render environment has no `SEC_USER_AGENT`, and no linked environment group.
  `refresh_desk.py` therefore falls back to the app name and repository URL, without
  an operator email. This does not match SEC's documented declared-bot identity.
- `STOCK_BRAIN_SEC_ENABLED=0` is an intentional pause after that denial. Current
  skipped refreshes do not represent new failed SEC requests.
- The legacy shared fetcher previously accepted any nonempty identity, although
  the broad provider already required an application and contact. The shared
  network path now enforces the same check. Issuer sources and cached bytes remain
  available; financial refresh failures retain previous source-dated records.

The missing contact is confirmed. IP reputation, shared cloud egress and aggregate
traffic are possible additional factors, not established causes. No evidence
shows this application exceeded SEC's limit. No new SEC probe was made during
this diagnosis, and a changed header is not proof of restored access.

## Correct configuration, then resolve the denial

1. Obtain the operator's real contact email for Stock Brain. Store the application
   name and email privately as `SEC_USER_AGENT` in Render. Never substitute a
   sample address, another organization's contact, or a browser identity.
2. Inspect `/api/status.sec_configuration` after the applicable deploy. It reports
   `enabled`, `user_agent_configured`, `user_agent_format_valid`, `status` and
   `network_checked: false`, never the email. Passing format validation cannot
   verify mailbox ownership or SEC access. Keep the collection pause active while
   addressing the existing denial.
3. SEC's FAQ directs access-denial cases to **webmaster@sec.gov**, with the error
   text or screenshot and the originating public IP. Include the affected URL,
   UTC timestamp, truthful application identity, request rate and any response
   reference ID when available. The earlier title is preserved, but a reference
   ID and original egress IP were not retained; do not fabricate them. Prepare
   a support request if the denial is unresolved; sending it requires operator
   authorization. Do not rotate IPs, proxies or identities to evade the denial.
4. Once the denial is legitimately resolved, verify a small controlled request
   from the existing collector before resuming daily work. Retain evidence of
   successful JSON retrieval, then enable collection and verify its published
   source dates. An enabled flag alone is not an access check.

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
