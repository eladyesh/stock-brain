# Public answer API

`POST https://finlotus-1.onrender.com/api/ask` accepts UTF-8 JSON:

```json
{"question":"What was MSFT revenue in FY2024?"}
```

The object must contain only `question`, a non-empty string of at most 4,000 characters. The body must be at most 8,192 bytes. The endpoint reads the server's current atomic checkpoint, runs the same evidence engine as the browser, and never performs research collection or model calls.

A successful HTTP 200 response contains `abstain`, `statements`, `companies`, `built_at`, `generation` (checkpoint SHA-256), and `engine`. Statements include text, issuer, accounting/period metadata where relevant, and `sources` with URLs and source locators. Company objects contain only small identity/date fields. A valid question with insufficient evidence returns HTTP 200 with `abstain: true`, `reason_code`, `reason`, and no statements. It does not fabricate an answer.

Examples:

- `How does Microsoft make money?`
- `Compare AMD and NVDA risks`
- `What was MSFT revenue in FY2024?`
- `MSFT revenue in latest available quarter`
- `מה ההכנסות של מיקרוסופט ברבעון האחרון במאגר?`
- `מה היו ההכנסות של מיקרוסופט בשנת הכספים 2024?`

Latest-available requests return `selected_period` and `availability_note`. They select one issuer's latest stored annual/quarterly period and keep every existing numerical and evidence gate. Calendar periods, GAAP/non-GAAP, forecasts and missing source data are not silently substituted.

| HTTP status | Meaning |
| --- | --- |
| 400 | Invalid JSON/question shape |
| 405 | Use POST on this route |
| 413 | Missing/invalid body size or body exceeds 8 KiB |
| 415 | Content-Type must be application/json |
| 503 | Worker busy/unavailable; Retry-After: 1 |

Answers use `Cache-Control: no-store`. Application code does not save or log visitor questions. Hosting infrastructure can log ordinary request metadata. Requests execute without a shell, use a fixed checkpoint path and a bounded Node subprocess, and cannot trigger writes or arbitrary commands. The browser labels local snapshot fallback if the API is unavailable.

The API is public and requires no login or API key. It is an evidence lookup engine, not unrestricted generative chat. Source freshness, scope and open financial QA limitations remain visible in the data and status endpoints.

## Separate coverage registry

`GET /api/coverage` returns registry counts, job states and scope limitations. `GET /api/companies?q=MSFT&limit=25&offset=0` returns `{items,total,limit,offset}`; its bounded items include identity, listings and payload metadata, never complete histories. `limit` is 1–100. Search accepts a name, ticker or CIK. Tickers can be ambiguous; CIK is the stable detail identifier.

`GET /api/companies/0000789019` returns one issuer's collected history, submissions metadata, automatic change draft and validated TTM where available. `collection_status` distinguishes registry-only, data-collected and review-required. `research` separately reports its dated evidence-bound narrative; automatic collection never promotes it to reviewed. If collection changes while a detail response is being read, the route returns a retryable HTTP 503 rather than a mixed generation. Missing companies return 404; invalid queries return 400. GET/HEAD are supported; writes return 405. These routes never fetch external sources, enqueue jobs or expand `/api/snapshot` and `/api/state`.

The answer API continues to use the reviewed pilot and its validated numerical data. It does not silently answer qualitative questions about every newly registered issuer. See [coverage infrastructure](US_COVERAGE.md) for activation and remaining scope.
