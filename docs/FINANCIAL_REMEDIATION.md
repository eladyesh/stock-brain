# Financial normalization remediation

Reviewed on **2026-10-22**. This pass makes the annual model inputs for Microsoft, Micron and NVIDIA reviewable and usable where exact issuer evidence supports them. All ten financial histories remain `readiness: partial`. This is not approval of complete financial statements, company research or an enterprise-value model.

## Result

Open QA flags decreased from **77 to 75**. Model-usable cells increased from **1,819 to 1,905**, comprising **84 exact filing-scope approvals** and **two NVIDIA period-end split reconciliations**. A cell is a metric/period view, so annual and Q4 views can reference the same underlying balance-sheet observation.

No existing numeric value, cell status, original observation, raw Company Facts hash, retrieval timestamp or information cutoff changed. The histories retain the original **2026-10-19** cutoff and retrieval metadata; new issuer-document retrieval dates are recorded separately. Source facts were not refreshed by this review. The unchanged SEC collection pause must not be presented as a successful refresh.

| Company | Open flags before | Open flags after | Model-usable cells before | Model-usable cells after | Newly scoped cells |
| --- | ---: | ---: | ---: | ---: | ---: |
| MSFT | 3 | 3 | 187 | 217 | 30 |
| MU | 3 | 3 | 171 | 201 | 30 |
| NVDA | 5 | 3 | 209 | 235 | 24 |
| AVGO | 26 | 26 | 235 | 235 | 0 |
| AVAV | 16 | 16 | 159 | 159 | 0 |
| RTX | 9 | 9 | 166 | 166 | 0 |
| ORCL | 6 | 6 | 150 | 150 | 0 |
| AMD | 3 | 3 | 200 | 200 | 0 |
| LMT | 3 | 3 | 153 | 153 | 0 |
| PLTR | 3 | 3 | 189 | 189 | 0 |
| **Total** | **77** | **75** | **1,819** | **1,905** | **84** |

The earlier 2026-10-19 pass reduced flags from 109 to 77 by reconciling 32 NVIDIA/Broadcom EPS and weighted-share revision flags. Its original split reviews, hashes, source observations and eight explicitly derived split-normalized cells remain intact.

## Annual model inputs now verified

Amounts below are reported FY2026 annual values, not TTM results, estimates or current market data. Dollars and shares are in millions except EPS.

| Issuer / fiscal end | Revenue | Net income | Diluted weighted shares | Diluted EPS | Strict cash FCF |
| --- | ---: | ---: | ---: | ---: | ---: |
| MSFT / 2026-06-30 | 331,839 | 133,749 | 7,453 | 17.95 | 66,987 |
| MU / 2026-09-03 | 133,188 | 84,969 | 1,143 | 74.33 | 58,963 |
| NVDA / 2026-01-25 | 215,938 | 120,067 | 24,514 | 4.90 | **Missing** |

Microsoft Note 2 and Micron Note 19 verify annual basic/diluted common EPS and weighted-average share denominators for FY2024–FY2026. Those exact observations now pass the share gate. NVIDIA's annual EPS and diluted denominator already had a verified split basis. Rounding can prevent net income divided by rounded shares from exactly reproducing reported EPS; the source-reported EPS is preserved.

Microsoft FCF is 182,935 operating cash flow less 115,948 cash PP&E purchases. Micron FCF is 89,675 less 30,712 gross cash PP&E purchases. Micron's calculation does not net government incentives against capex. NVIDIA reports broader productive-asset spending that includes intangibles; it is not relabeled as strict PP&E capex or used to fill the missing strict FCF cell.

Period-end outstanding common shares are separately reviewed for MSFT FY2024–FY2026, MU FY2025–FY2026 and NVDA FY2025–FY2026. These counts are neither annual diluted weighted-average denominators nor current quote-date outstanding shares. No missing Q4 EPS/share value is obtained by subtracting YTD data.

## Debt definitions and split reconciliation

- **Microsoft:** FY2026 long-term borrowing carrying value is 40,294 = 9,227 current + 31,067 noncurrent. FY2025 is 43,151 = 2,999 + 40,152. Note 10 distinguishes principal and carrying amounts; finance leases are separately reported in Note 13. The approved cells exclude finance leases. Missing short-term borrowings remain missing, and `debt_total` remains missing.
- **Micron:** FY2026 debt carrying value is 5,179 = 491 current + 4,688 noncurrent, including 2,387 of finance leases. FY2025 is 14,577 = 560 + 14,017, including 3,044 of finance leases. FY2026 notes payable are separately 2,792 carrying value, excluding leases; principal is 2,808 before 16 of discounts. These scopes are retained explicitly.
- **NVIDIA:** Borrowing carrying values are 8,463 at FY2025, 8,468 at FY2026 and 33,366 at Q2 FY2027 (2026-07-26), excluding lease liabilities. Current/noncurrent components and derived totals are bound to exact reviewed observations. The debt notes explicitly report no commercial paper outstanding; no missing metric has been filled with zero. Borrowing balances with this scope are not a lease-inclusive EV bridge.
- **NVIDIA FY2024 outstanding shares:** The original FY2024 filing reports 2,464 million shares before the ten-for-one split; FY2025 presents 24,643 million after the split. The scaled rounding interval of the former (24,635–24,645 million) overlaps the latter (24,642.5–24,643.5 million). Both original observations remain stored; the two annual/Q4 conflict flags are resolved with the split review ID. Neither reported number is overwritten.

## Primary evidence

Every new review retains the exact accession, concept, unit, period, value, publication date, source URL, document hash, document locator and scope rationale. The original SEC fact identity remains separate from corroborating issuer-hosted evidence.

| Evidence | Filing date | SHA-256 |
| --- | --- | --- |
| [Microsoft FY2026 annual financial statements, Notes 2, 10, 13 and 15](https://www.microsoft.com/investor/reports/ar26/index.html) | 2026-07-29 | `c80ec67fe527d2f974bf84a89661b23a22c752cc2ba0f107370c7df377b25f1b` |
| [Micron FY2026 Form 10-K, balance sheets and Notes 9/19](https://d18rn0p25nwr6d.cloudfront.net/CIK-0000723125/5dafce68-38e8-4cad-a8f3-ab56d04d73fd.pdf) | 2026-10-09 | `aa227d7af0003b3ead47c7b6bb628b98668c8065d14a917d734b2638185b48b3` |
| [NVIDIA FY2024 Form 10-K, balance sheets](https://s201.q4cdn.com/141608511/files/doc_financials/2024/q4/1cbe8fe7-e08a-46e3-8dcc-b429fc06c1a4.pdf) | 2024-02-21 | `536f66d7f1c3413abbf643e0a02bd0aab65639116fe630225f3f93529244658b` |
| [NVIDIA FY2025 Form 10-K, balance sheets and split disclosure](https://s201.q4cdn.com/141608511/files/doc_financials/2025/q4/177440d5-3b32-4185-8cc8-95500a9dc783.pdf) | 2025-02-26 | `b67bd67a64488a54886de001c788bc5059a965fc6ef5b4d8b71624951e13df8e` |
| [NVIDIA FY2026 Form 10-K, balance sheets and Note 11](https://s201.q4cdn.com/141608511/files/doc_financials/2026/q4/10K-NVDA.pdf) | 2026-02-25 | `a056b59e4170c0123217a8e861a39af4a4a48d2df0d27b641017a618a280a396` |
| [NVIDIA Q2 FY2027 Form 10-Q, Note 9](https://s201.q4cdn.com/141608511/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf) | 2026-08-26 | `6b5a8dc1ed21e8b2b960fd0de97103af6a2f32ccc8dd91b363f06ea192ecfebd` |

The PDFs present share counts in millions, establishing the rounding precision used for the new outstanding-share split bridge. The original weighted-share split reviews retain their inline-XBRL precision evidence.

## Remaining work

| Open issue category | Before | After | Required evidence / treatment |
| --- | ---: | ---: | --- |
| Source revisions or definition conflicts | 31 | 29 | Issuer-specific reconciliation of every selected and conflicting observation. |
| Definition changes across a series | 13 | 13 | Line-item bridges, especially AVGO debt and AVAV revenue definitions. |
| Share basis / outstanding-share coverage | 10 | 10 | Review unapproved earlier/quarterly observations. Group flags remain even when some model inputs are verified. |
| Debt scope | 10 | 10 | Extend the exact reviews to remaining periods and establish complete compatible EV scope. |
| Missing selected-metric coverage | 10 | 10 | Obtain exact missing concepts and periods; absence is not zero. |
| Fiscal identity conflicts | 3 | 3 | Review AVAV 2023-10-28 and 2024-01-27 and ORCL 2026-08-31 original contexts. |
| **Total** | **77** | **75** | |

The 29 remaining revision flags comprise **AVGO 18**, **AVAV 9** and **RTX 2**. Broadcom has 16 debt-related flags plus two outstanding-share flags at 2023-10-29. Its FY2024 issuer PDF confirms the split and the later share amount, but the conflict includes three earlier filings; complete fresh document evidence was not obtained for all alternatives, so both flags remain. Its FY2023 direct issuer download returned HTTP 503. AeroVironment's revised FY2025 PP&E/cash flow, quarterly operating income, consolidated profit and EPS remain unresolved; Q4 differences from unreconciled cumulative inputs stay blocked. RTX's historical operating-income presentation changes require their own reconciliation.

For the priority issuers, remaining unverified share/debt cells are MSFT **55/39**, MU **57/52** and NVDA **2/44**. These cell counts are distinct from the grouped QA flag count. NVIDIA and Lockheed Martin still lack strict PP&E capex and the corresponding FCF. No complete balance-sheet or cash-flow tie-out has been performed.

## Refresh and verification

`normalize_companyfacts(..., normalization_reviews=...)` applies only exact eligible observations. New `filing_scope` reviews verify a metric definition without clearing unrelated revisions or series-comparability gates. Share scope, borrowing scope and source evidence are validated; simply deleting a blocking flag cannot make a share/debt cell model-usable.

`apply_normalization_reviews(history, canonical_reviews)` returns a validated deep copy for checkpoint restoration. It merges immutable review IDs, reapplies only matching source observations, recounts QA/coverage and preserves source facts and fetch metadata. If no new eligible review is added, it preserves the existing payload without changing coverage fields. Changed facts/accessions remain gated. Conflicting contents for the same review ID are rejected. Evidence published after the history cutoff is excluded. Split conflict resolutions must reproduce the reviewed source-rounding reconciliation.

Verification: **34 focused financial tests pass**, including exported issuer evidence and bilingual lease-scope disclosure; all ten stored histories pass the reproducible integrity audit; semantic comparison confirms no numeric/status/provenance or original-source metadata change in MSFT/MU/NVDA. `git diff --check` and `python scripts/stock_brain.py check` pass after index regeneration. The machine-readable report is regenerated with:

```sh
python scripts/audit_financials.py --output docs/FINANCIAL_QA_STATUS.json
```

The audit reports internal integrity separately from research approval and includes exact latest-annual input gates, scope-review counts and open cell gates. It does not imply that all underlying reports were independently re-audited.
