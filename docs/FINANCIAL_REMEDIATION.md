# Financial normalization remediation

Reviewed on **2026-10-19**, preserving the existing **2026-10-18 information cutoff**. This is a bounded source-reconciliation pass on the selected historical metric schedules. It does not mark company research as human-reviewed or turn the schedules into complete financial statements.

## Result

Open QA flags fell from **109 to 77** after resolving **32 share/EPS revision flags** for NVIDIA and Broadcom. **112 existing cells** now have verified, comparable share bases. Eight of those cells required explicit split calculations; the other 104 keep their reported numeric values. Every company remains `readiness: partial`.

Only `research/financials/NVDA.json` and `research/financials/AVGO.json` were regenerated. The other eight schedules were left intact. No non-share numeric value changed. The ten-company collection now contains **2,295 reported, 569 derived and 1,216 missing cells**. The eight-cell shift from reported to derived is the oldest-period split normalization, not new source coverage.

| Company | Open flags before | Open flags after | Model-usable cells before | Model-usable cells after | Readiness before / after |
| --- | ---: | ---: | ---: | ---: | --- |
| AMD | 3 | 3 | 200 | 200 | partial / partial |
| AVAV | 16 | 16 | 159 | 159 | partial / partial |
| AVGO | 42 | 26 | 179 | 235 | partial / partial |
| LMT | 3 | 3 | 153 | 153 | partial / partial |
| MSFT | 3 | 3 | 187 | 187 | partial / partial |
| MU | 3 | 3 | 171 | 171 | partial / partial |
| NVDA | 21 | 5 | 153 | 209 | partial / partial |
| ORCL | 6 | 6 | 150 | 150 | partial / partial |
| PLTR | 3 | 3 | 189 | 189 | partial / partial |
| RTX | 9 | 9 | 166 | 166 | partial / partial |
| **Total** | **109** | **77** | **1,707** | **1,819** | **partial / partial** |

Model usability is assessed per cell and definition. It is not permission to mix currencies, profit attribution, reporting periods or debt scopes, and does not establish valuation readiness.

## Verified source basis

The financial statements disclose two ten-for-one common-stock splits and retrospective presentation of share/per-share data:

| Company | Effective date | Primary evidence | Source publication date | Document SHA-256 |
| --- | --- | --- | --- | --- |
| NVDA | 2024-06-07 | [FY2025 Form 10-K, Note 1 and stock split disclosure](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm) | 2025-02-26 | `1493a74bd587701ed8039d680eb91aafc9ea747eef6a325ee189953dd4dce517` |
| AVGO | 2024-07-12 | [FY2024 Form 10-K, Note 1 and Note 11](https://www.sec.gov/Archives/edgar/data/1730168/000173016824000139/avgo-20241103.htm) | 2024-12-20 | `bf1e56c85495b8a2433c3ca9d7fa776ab75075dca8feadac122d4f4b77d4ad78` |

**152 exact observations across 24 original SEC filings were independently matched** to their non-dimensional inline-XBRL facts: accession, concept, unit, exact start/end, numeric value and source `decimals`. This includes the selected EPS/basic/diluted weighted-share facts and every older alternative implicated in their revisions. There are 76 verified observations from 12 filings for each issuer. Raw documents and their checksum-addressed cache remain in ignored `build/`; each persisted review retains document URLs, hashes and retrieval timestamps.

The four reviewed metrics are `eps_basic`, `eps_diluted`, `shares_basic` and `shares_diluted`. Each issuer has 14 available periods for these metrics, or 56 verified cells. The remaining three Q4 periods still have missing EPS/share facts; EPS and weighted-average shares are never obtained by subtracting YTD amounts.

The verified filing accessions are retained with each observation in the schedule's `normalization_reviews`. This is an explicit approval of those exact observations, not a blanket issuer rule. A future refresh that selects a different accession or changes the value, dates, unit or concept must obtain new source evidence before that cell becomes model-usable.

## Numerical reconciliation

NVIDIA FY2024 diluted EPS of 11.93 and its later presentation of 1.19 are consistent with the disclosed split and source rounding. Broadcom FY2023 diluted EPS of 32.98 and 3.30 reconcile on the same basis. Both old and selected versions remain in the saved schedule; reconciled alternatives move from `conflicts` into `resolved_conflicts` with a resolution and review ID.

Shares reported in millions require a precision-aware bridge. Broadcom's 427 million diluted weighted-average shares for FY2023 and its later 4,272 million are not exactly ten times apart. Both filings report shares to the nearest million. The pre-split rounding interval scaled by ten overlaps the post-split rounding interval, supporting the reconciliation. The implementation uses each observed inline-XBRL `decimals` value rather than an arbitrary percentage tolerance. It does not reconcile differing values already on the same split basis.

The oldest annual periods had no later, split-restated selected fact. Their values are now explicit derived calculations:

| Issuer / fiscal period | Metric | Original reported value | Comparable post-split value | Treatment |
| --- | --- | ---: | ---: | --- |
| NVDA FY2022, ended 2022-01-30 | Basic EPS | 3.91 | 0.391 | Divide by 10 |
| NVDA FY2022 | Diluted EPS | 3.85 | 0.385 | Divide by 10 |
| NVDA FY2022 | Basic weighted shares | 2,496,000,000 | 24,960,000,000 | Multiply by 10 |
| NVDA FY2022 | Diluted weighted shares | 2,535,000,000 | 25,350,000,000 | Multiply by 10 |
| AVGO FY2021, ended 2021-10-31 | Basic EPS | 15.70 | 1.570 | Divide by 10 |
| AVGO FY2021 | Diluted EPS | 15.00 | 1.500 | Divide by 10 |
| AVGO FY2021 | Basic weighted shares | 410,000,000 | 4,100,000,000 | Multiply by 10 |
| AVGO FY2021 | Diluted weighted shares | 429,000,000 | 4,290,000,000 | Multiply by 10 |

The calculations preserve the precision of the original rounded input after applying the split factor. For example, 0.385 is a calculation from reported 3.85, not a newly reported three-decimal EPS. Original numeric facts remain untouched in `provenance`; adjusted cells have `status: derived`, `evidence_label: derived_calculation`, a formula and a source-basis record. Later reported, already-adjusted values keep `status: reported`.

The action evidence is separately bound through `share_basis.evidence_source_ids` into `source_index`. Answers using a split-derived number should cite both the original numeric filing and the split evidence.

## Remaining blockers

| Open issue category | Before | After | Required next evidence / treatment |
| --- | ---: | ---: | --- |
| Source revisions or definition conflicts | 63 | 31 | Reconcile the remaining issuer-specific filing differences below; no automatic acceptance of the latest number. |
| Definition changes across a series | 13 | 13 | Build line-item bridges, especially debt scope and AVAV revenue definitions. |
| Share basis / outstanding-share class coverage | 10 | 10 | NVDA and AVGO now flag only `shares_outstanding`; the other issuers still require corporate-action and share-class review. |
| Debt scope | 10 | 10 | Reconcile current/noncurrent, borrowings, leases, principal and carrying amounts before enterprise-value calculations. |
| Missing selected-metric coverage | 10 | 10 | Source exact missing concepts and periods; no missing-to-zero conversion. |
| Fiscal identity conflicts | 3 | 3 | Review AVAV quarters ended 2023-10-28 and 2024-01-27 and ORCL quarter ended 2026-08-31 against the original submissions. |
| **Total** | **109** | **77** | |

The 31 remaining revision flags are cell-level issues, including derived and duplicate annual/quarter views of an underlying source difference:

- **NVDA: 2.** Period-end shares outstanding at 2024-01-28 remain unreconciled. The weighted-share review does not establish period-end share-class completeness.
- **AVGO: 18.** Sixteen concern current/noncurrent/derived debt definitions or values; two concern period-end shares outstanding at 2023-10-29. These are outside the approved EPS/weighted-share split bridge.
- **AVAV: 9.** FY2025 PP&E payments and related FCF/quarter differences, revised quarterly operating income and consolidated profit, and revised EPS require the specific amended/revised filings and explanations. The Q4 subtraction of unreconciled cumulative facts remains blocked.
- **RTX: 2.** FY2021 and FY2022 operating-income presentation changes remain unresolved. They are not stock-split effects.

Strict PP&E capex and the corresponding defined FCF are still missing for NVDA and LMT. Broader productive-asset spending is kept separate. Outstanding shares remain a distinct period-end measure; verified weighted-average shares do not substitute for current market-cap share counts.

## Refresh and verification

`financial_history.py` preserves the embedded `normalization_reviews` on a normal refresh and reapplies them only to matching source observations. Direct callers can pass the existing schedule's reviews using the `normalization_reviews` keyword argument. Calling the normalizer without a review intentionally retains the original conservative share gates.

Evidence and observations published after `as_of` are excluded. A known split cannot be applied in a historical snapshot using a proof filing that had not yet been published. The review date itself documents when the work was performed and does not change the source-information cutoff.

Verification completed:

- All 26 financial-history tests pass, including source precision, unexplained revisions, unreviewed new observations, same-day and same-basis conflicts, historical-cutoff leakage, source identity and derived-value integrity.
- All ten persisted histories pass schema, provenance, units, cutoff, period and normalization checks.
- Semantic comparison against the prior schedules confirms exactly the eight numeric/status changes listed above and no non-share numeric changes.
- The repository-wide validator was attempted during concurrent research edits and reported a stale generated sector index; the integration step must rebuild indexes and rerun that validator.

This work does not change canonical company profiles, review status, forecasts, debt totals or valuation assumptions.
