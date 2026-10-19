# Sourced financial history

`research/financials/{TICKER}.json` contains a selected historical financial-metric schedule for each of the ten configured issuers. The initial collection cutoff is **2026-10-18**; refreshed schedules carry their own `as_of` and source retrieval timestamps. Each schedule contains five annual periods and twelve standalone fiscal quarters, including sourced-boundary Q4 calculations where supported. All data comes from SEC Company Facts; there are no paid-provider inputs, market prices, consensus estimates, forecasts, or human-review claims.

The [October 19 source reconciliation](FINANCIAL_REMEDIATION.md) reduces open QA flags from 109 to 77 and verifies 112 share/EPS cells for NVIDIA and Broadcom. The baseline below is preserved for comparison.

These schedules are **partial research inputs**, not complete financial statements or a valuation-ready model. Source revisions, profit attribution, debt scope, share basis, and missing concepts remain visible. Canonical Markdown profiles and their research review states are unchanged.

## Refresh and access

Set `SEC_USER_AGENT` to an identifying application/contact string, then run:

```sh
python scripts/financial_history.py --as-of 2026-10-18
python scripts/financial_history.py --as-of 2026-10-18 --ticker MSFT --refresh
python -m unittest discover -s tests -p 'test_financial_history.py' -v
```

The default is the configured universe, five annual periods, and twelve quarters. The collector uses `research_pipeline.Fetcher` and its maximum of two requests per second, retry policy, SHA-256 integrity checks, and content-addressed raw cache under ignored `build/research-cache/http`. Each schedule preserves the snapshot URL, hash and retrieval timestamp. Failed downloads or normalization leave an existing schedule intact and produce a nonzero exit status. Do not interpret a failed refresh as current data.

```python
from pathlib import Path
from financial_history import load_history, get_metric

history = load_history(Path('.'), 'MSFT')
latest_annual_eps = get_metric(history, 'eps_diluted')
exact_quarter = get_metric(
    history, 'revenue', period_type='quarterly',
    period_start='2026-01-01', period_end='2026-03-31',
)
```

`load_history` returns `None` when the schedule does not exist and raises for corrupt data or an issuer mismatch. `get_metric` returns the metric cell plus `period`, `ticker`, `metric` and `as_of`. It returns `None` when the requested period is absent. A present period with an unavailable metric returns an explicit `missing_required_source` cell with `value: null`. Omitted date/fiscal filters select the latest stored period of the requested type. Explicit requests never fall back to a different period. Supported filters include `fiscal_year` and `fiscal_quarter`; an unverified fiscal year cannot match a year-specific request.

## Data contract

- `periods`: exact start/end, period type, fiscal year/quarter when verified, source accession(s) establishing period identity, label and identity caveats. IDs are `annual:YYYY-MM-DD` or `quarterly:YYYY-MM-DD`.
- `financials[period_id][metric]`: `value`, `unit`, `status`, `basis`, `evidence_label`, `confidence`, `model_usable`, `comparison_status`, source `definition_tag`, `provenance`, `conflicts`, `flags` and formulas/notes where relevant.
- `source_index`: accession-level filing sources and original filing URLs; `source_concepts` retains SEC concept labels, descriptions and available units.
- `provenance`: exact source value, tag, taxonomy, unit, period start/end, filing date, accession, filing fiscal focus, calendar frame and source URL. Calendar frames are audit metadata, never fiscal labels.
- `qa_flags`, `validation_checks`, `comparability_bridge`, `coverage` and `limitations`: downstream readiness, performed controls and unresolved gaps.

| Metrics | Definition and normalization |
| --- | --- |
| `revenue`, `operating_income`, `gross_profit`, `cost_of_revenue` | Accepted US-GAAP concepts; exact tag retained. Different reported definitions are not automatically recast. Gross profit may be revenue less cost only with compatible source accessions. |
| `net_income` | `NetIncomeLoss`: net income attributable to the parent. |
| `net_income_common` | `NetIncomeLossAvailableToCommonStockholdersBasic`; kept separate from parent net income. |
| `net_income_including_noncontrolling_interests` | `ProfitLoss`; kept separate from income attributable to parent/common holders. |
| `eps_basic`, `eps_diluted` | Reported USD/share, never calculated as a difference of cumulative EPS. |
| `shares_basic`, `shares_diluted` | Reported weighted-average shares; never substituted for current shares or derived by subtraction. |
| `shares_outstanding` | Exact period-end `CommonStockSharesOutstanding`. A nearby cover-page date or missing class breakdown does not substitute for it. |
| `operating_cash_flow`, `stock_based_compensation` | Exact consolidated operating cash flow and the reported share-based compensation concept. |
| `capex` | Cash PP&E purchases only; normalized to negative cash outflow with the source sign preserved in provenance. |
| `purchases_of_productive_assets` | Broader reported productive-asset investment, potentially including intangibles. Negative cash outflow, kept separate from strict PP&E capex. |
| `free_cash_flow` | OCF plus negative PP&E capex for the exact same normalized period. This is a defined calculation, not necessarily company-defined FCF; noncash additions and finance leases are not included. |
| `cash_and_equivalents`, `short_term_investments` | Separate exact period-end balances. Missing investments are not zero and cash is not silently combined with securities. |
| `debt_current`, `debt_noncurrent`, `long_term_debt_total`, `short_term_borrowings`, `debt_total` | Exact reported source scope retained. A missing short-term balance is not zero. Current notes, current long-term maturities, broad current debt, lease-inclusive debt and carrying/principal values are distinguished. Derived totals require compatible source accessions and remain subject to debt-scope review. |

Values remain in native units (`USD`, `shares`, `USD/shares`), with no scaling or FX conversion. `status` is `reported`, `derived`, `missing_required_source` or `conflicted`. A reported value can remain useful for source inspection while `model_usable` is false because an unresolved comparability issue prevents modeling.

## Fiscal periods, quarters and revisions

1. The latest core statement duration in each filing establishes its primary reporting period. A prior-period comparative inherits its actual boundaries, not that later filing's `fy` or `fp`.
2. Annual duration windows accommodate 52/53-week years. A standalone quarter must be 60–110 days and originate from the filing's current quarter context, or have Q4 boundaries established by a sourced Q3 end and annual end.
3. Quarter cash flows may be calculated as current cumulative minus previous cumulative only when fiscal start, tag and unit match exactly. Both inputs and accessions remain visible. Cross-filing derivation is flagged. A known cumulative revision blocks the subtraction pending reconciliation.
4. EPS and weighted-average share counts are nonadditive. If the standalone fact is missing, the quarter remains missing.
5. Select the latest filed accepted tag for the exact period/unit. Preferred tag order resolves overlaps on that filing date. Keep prior differing values and alternative definitions. Same-date conflicts return `null` rather than choose one number.
6. Share-count and per-share comparability remains unverified until corporate actions are reviewed. A changed historical EPS does not prove a particular split adjustment automatically.
7. Scope/tag changes receive a line-item comparability bridge. They do not turn unrelated series into recast data.

The SEC documents that Company Facts includes non-custom, entity-wide concepts, and that frames align to calendar periods which may differ from issuer reporting periods. The filing fiscal year/period focus describes the submission rather than every comparative fact contained in it:

- [SEC EDGAR API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- [SEC Financial Statement Data Sets documentation, fiscal-focus fields](https://www.sec.gov/files/fsds.pdf)

## Original collection baseline (before October 19 remediation)

All ten Company Facts sources were retrieved successfully. There are 170 period records and 24 separately defined metric slots per period: **2,303 reported cells, 561 derived cells and 1,216 explicit missing cells**. The denominator includes intentionally separate alternative definitions, such as parent/common/consolidated net income and PP&E/productive-asset investment. Their absence is not a claim that the issuer failed to publish financial results.

| Ticker | Annual / quarter periods | Latest period end | Latest source filed | Reported / derived / missing |
| --- | --- | --- | --- | --- |
| AMD | 5 / 12 | 2026-06-27 | 2026-08-05 | 246 / 59 / 103 |
| AVAV | 5 / 12 | 2026-08-01 | 2026-09-10 | 242 / 52 / 114 |
| AVGO | 5 / 12 | 2026-08-02 | 2026-09-10 | 232 / 68 / 108 |
| LMT | 5 / 12 | 2026-06-28 | 2026-07-23 | 217 / 42 / 149 |
| MSFT | 5 / 12 | 2026-06-30 | 2026-07-29 | 270 / 41 / 97 |
| MU | 5 / 12 | 2026-09-03 | 2026-10-09 | 251 / 59 / 98 |
| NVDA | 5 / 12 | 2026-07-26 | 2026-08-26 | 224 / 57 / 127 |
| ORCL | 5 / 12 | 2026-08-31 | 2026-09-11 | 200 / 49 / 159 |
| PLTR | 5 / 12 | 2026-06-30 | 2026-08-04 | 201 / 62 / 145 |
| RTX | 5 / 12 | 2026-06-30 | 2026-07-23 | 220 / 72 / 116 |

Latest annual revenue and reported diluted EPS exist for all ten issuers. Current precision does not establish historical split comparability or endorse an EPS growth forecast. Strict PP&E capex and FCF remain missing for NVDA and LMT; their broader productive-asset spending is available separately. Complete debt totals are frequently unavailable without filing-level scope reconciliation. Some companies' gross-profit components and share-class details use concepts outside this mapping.

The collection preserves **316 passed validation checks** across the ten JSON files: period-duration controls, gross-profit tie-outs when all selected inputs are available, and schedule-level schema/provenance/unit/cutoff/period controls. No performed check failed. These controls do not prove overall financial completeness; **109 open QA flags** remain for historical revisions, definition changes, share/debt basis, missing source coverage and fiscal identity. Full balance-sheet and cash-flow-statement reconciliations were not performed because this is a selected metric schedule.

Eighteen focused unit tests cover non-calendar fiscal labels, comparative filing focus, 53-week years, standalone versus YTD periods, nonadditive EPS/shares, mismatched cumulative starts, source revisions, same-date conflicts, future filings, currency/accounting scope, share/debt limitations, latest-tag selection, profit attribution, productive-asset definitions, FCF signs, failed financial tie-outs, and persisted-source integrity.

## Verified exceptions requiring source review

| Issuer / period | Observed source issue | Current treatment |
| --- | --- | --- |
| ORCL quarter ended 2026-08-31 | Its `10-Q` facts report `fy=2026`, following the annual FY2026 period ended 2026-05-31. | Exact quarter boundaries and Q1 retained; fiscal-year label is unknown with a conflict flag. No calendar-year guess. |
| NVDA year ended 2024-01-28 | Diluted EPS is 11.93 in accession `0001045810-24-000029` and 1.19 in `0001045810-26-000021`. | Latest 1.19 shown with both versions retained; share-basis reconciliation required. |
| AVGO year ended 2023-10-29 | Diluted EPS is 32.98 in `0001730168-23-000096` and 3.30 in `0001730168-25-000121`. | Latest 3.30 shown; no automatic historical split adjustment. |
| AVAV year ended 2025-04-30 | PP&E cash payments are 22.816m in `0001558370-25-008838` and 19.547m in `0001104659-26-078906`. | Both values retained; affected FCF and standalone-quarter calculations are not model-ready. |
| AVAV quarter ended 2026-01-31 | Operating loss changes from 179.038m in `0001104659-26-025979` to 268.440m in `0001104659-26-076141`. | Latest source value shown with a revision flag. The associated Q4 operating-income subtraction is blocked because cumulative inputs need reconciliation. |
| RTX year ended 2022-12-31 | Operating income is 5.414bn in `0000101829-23-000009` and 5.504bn in `0000101829-25-000005`. | Latest value and prior alternatives retained; presentation/revision review required. |

Review these source differences in their original filings before using them as a comparable model history. Next normalization work is targeted: resolve each revision/split bridge, reconcile complete debt and share-class scope, and add issuer-specific sourced concepts with explicit definition tests. New inputs must not silently change canonical research review status.
