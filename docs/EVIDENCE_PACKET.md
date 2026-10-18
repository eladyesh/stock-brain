# Evidence packet contract

Research packets are intermediate, auditable inputs. The company Markdown remains the canonical published research. Store pilot packets in `research/pilot/<TICKER>.json`; keep downloaded full documents under ignored `build/research-cache/`.

Version 1 packets have these keys:

```json
{
  "schema_version": 1,
  "ticker": "EXAMPLE",
  "as_of": "2026-10-18",
  "sources": [{"id":"S01","title":"Actual document title","publisher":"Actual issuer","url":"https://example.com/document","published_at":null,"accessed_at":"2026-10-18"}],
  "sections": {
    "business-overview": {"claims":[{"id":"C01","kind":"reported","text":"A self-contained original summary.","evidence":[{"source_id":"S01","locator":"Business / exact heading or page"}]}]},
    "valuation-context": {"unavailable":"Current market price and comparable estimates have not been sourced."}
  },
  "gaps": ["Specific unresolved question"],
  "metrics": []
}
```

Include all 17 research section IDs from `config/sections.json`, excluding `sources-and-change-log`. Each section must contain either a nonempty `claims` list or an honest nonempty `unavailable` reason. Claim IDs are unique across the packet. Claim kinds: `reported`, `management_guidance`, `interpretation`, `derived`. Each claim needs evidence references and meaningful source locators. Avoid embedding citation markers in claim text; the renderer adds them. All actual facts must come from read primary sources; a source URL or search snippet alone is insufficient. Number every material financial metric in `metrics` using the form below. Narrative numeric facts must also retain their period/basis in the prose.

```json
{"id":"M01","claim_id":"C09","name":"Revenue","value":1234,"unit":"million","currency":"USD","period_start":"2026-01-01","period_end":"2026-03-31","basis":"GAAP","source_id":"S01","locator":"Condensed statements of operations / Revenue"}
```

For balance-sheet values use `period_start: null`. For percent metrics use `unit: percent` and `currency: null`. For per-share values use `unit: per_share`. `value` must be a finite JSON number, never a missing-value zero. Derived metrics instead supply `calculation: {"operation":"growth_pct" or "margin_pct", "inputs":["M01","M02"]}`; omit their `value` so code computes it. Inputs must have compatible units/currency/basis and suitable periods. Narrative calculations must match the computed results. Do not add consensus or price targets without the corresponding evidence.

Metrics default to `kind: reported`; their period cannot follow the evidence cutoff. Use explicit `kind: management_guidance` for forward guidance and `kind: declared` for an announced future payment, retaining the announcement citation. Those kinds can have future periods and must not be mixed with actuals in calculations. A dividend's future payment date is not evidence that payment already occurred.

`as_of` states the evidence cutoff actually covered, not the date a file was touched. Explicitly disclose historical or incomplete refreshes in the profile. Additional URLs, full document hashes, fetch outcomes, and elapsed collection time belong in collection manifests, outside canonical company frontmatter.

Review logs live at `research/reviews/<TICKER>.json`. A reviewer checks the material claims against the cited source locations, records gaps and conflicts, and binds the review to the exact packet hash and draft body hash. Formatting validation alone must never set `reviewed`. See [the pipeline guide](PIPELINE.md) for commands.
