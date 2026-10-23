---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000789019
cik: 0000789019
company_name: MICROSOFT CORP
tickers:
- MSFT
status: stub
canonical_reviewed: false
as_of: '2026-10-22'
updated_at: '2026-10-22T18:45:53.881812+00:00'
reviewed_at: null
coverage_release: coverage-20261022-39831584719-1
source_commit: c640ba8ecaf78dc0ecb247c1e3ebadf4b6fa77ae
financial_history_available: true
curated_research:
  url: https://github.com/eladyesh/stock-brain/blob/c640ba8ecaf78dc0ecb247c1e3ebadf4b6fa77ae/sectors/information-technology/companies/MSFT/README.md
  status: reviewed
  as_of: '2026-10-18'
  sector: information-technology
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-Q
  - 11-K
  - '144'
  - 25-NSE
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B3
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - IRANNOTICE
  - PX14A6G
  - S-3ASR
  - S-4
  - S-4/A
  - S-8
  - S-8 POS
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json
    sha256: dd0308149a8e96497989ed7c690b5a49a00bef9ceafbb24638bda41e8ae938dd
    retrieved_at: '2026-10-22T17:54:54.576049+00:00'
  submissions:
    url: https://data.sec.gov/submissions/CIK0000789019.json
    sha256: a9a65d8640cde1fe6fd7cf0219d5b948f431bf4f8b7954de4386d62f7eaa2523
    retrieved_at: '2026-10-22T17:39:35.977490+00:00'
    archive: &id001
      member: CIK0000789019.json
      sha256: b6534bf3efaca6ea2a0a9509deb9eb4c612cb9aa12d4913fdb641a526cc4b033
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-22T18:30:07.617970+00:00'
  sha256: 484b32c59991d6364287abb8172f2106fc4eea58e5cb0256601a455a37cadda1
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000789019.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: a9a65d8640cde1fe6fd7cf0219d5b948f431bf4f8b7954de4386d62f7eaa2523
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json
  published_at: null
  retrieved_at: '2026-10-22T17:54:54.576049+00:00'
  sha256: dd0308149a8e96497989ed7c690b5a49a00bef9ceafbb24638bda41e8ae938dd
- id: S04
  title: 10-K 0001193125-26-323660
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.html
  published_at: '2026-07-29'
  retrieved_at: '2026-10-22T17:54:54.576049+00:00'
  sha256: null
- id: S08
  title: 10-Q 0001193125-26-191507
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/0001193125-26-191507-index.html
  published_at: '2026-04-29'
  retrieved_at: '2026-10-22T17:54:54.576049+00:00'
  sha256: null
- id: S17
  title: ARS 0001193125-26-427876
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526427876/0001193125-26-427876-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S18
  title: DEFA14A 0001193125-26-427867
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526427867/0001193125-26-427867-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S19
  title: DEF 14A 0001193125-26-427849
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526427849/0001193125-26-427849-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S20
  title: 4 0000789019-26-000228
  url: https://www.sec.gov/Archives/edgar/data/789019/000078901926000228/0000789019-26-000228-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S21
  title: 4 0000789019-26-000226
  url: https://www.sec.gov/Archives/edgar/data/789019/000078901926000226/0000789019-26-000226-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
issuer_classification:
  cik: 0000789019
  name: MICROSOFT CORP
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: a9a65d8640cde1fe6fd7cf0219d5b948f431bf4f8b7954de4386d62f7eaa2523
  url: https://data.sec.gov/submissions/CIK0000789019.json
sector_assignment:
  sector: information-technology
  method: curated_profile
  sic: null
  sic_description: null
  rule_version: 1
  reason: Uses the dated curated profile assignment; automatic data does not renew
    its review.
  source_url: https://github.com/eladyesh/stock-brain/blob/c640ba8ecaf78dc0ecb247c1e3ebadf4b6fa77ae/sectors/information-technology/companies/MSFT/README.md
full_history_url: https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000789019/README.md
full_history_commit: f1dea1c5fdf869d02b10266fe4da900fd3a13544
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# MICROSOFT CORP — MSFT

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000789019/README.md)

## Business overview

Reported issuer name: **MICROSOFT CORP**. Stable SEC CIK: **0000789019**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| MSFT | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

Not available: substantive research has not been completed. Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.

Navigation sector: **information-technology**. Method: `curated_profile`. Uses the dated curated profile assignment; automatic data does not renew its review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:54:54.576049+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -115,948,000,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 106,374,000,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | 18 | USD/shares | US GAAP / reported | EarningsPerShareBasic; filing_scope_verified | [S04] |
| eps_diluted | 17.95 | USD/shares | US GAAP / reported | EarningsPerShareDiluted; filing_scope_verified | [S04] |
| free_cash_flow | 66,987,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 225,465,000,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 133,749,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 182,935,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 155,237,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 331,839,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | 7,429,000,000 | shares | US GAAP / reported | WeightedAverageNumberOfSharesOutstandingBasic; filing_scope_verified | [S04] |
| shares_diluted | 7,453,000,000 | shares | US GAAP / reported | WeightedAverageNumberOfDilutedSharesOutstanding; filing_scope_verified | [S04] |
| stock_based_compensation | 12,405,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -35,802,000,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| cost_of_revenue | 29,525,000,000 | USD | US GAAP / derived | CostOfGoodsAndServicesSold; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | 19,639,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| gross_profit | 60,482,000,000 | USD | US GAAP / derived | GrossProfit; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income | 35,766,000,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 55,441,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_income | 40,603,000,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 90,007,000,000 | USD | US GAAP / derived | RevenueFromContractWithCustomerExcludingAssessedTax; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 3,122,000,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:54:54.576049+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 20,935,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | 9,227,000,000 | USD | US GAAP / reported | LongTermDebtCurrent; filing_scope_verified | [S04] |
| debt_noncurrent | 31,067,000,000 | USD | US GAAP / reported | LongTermDebtNoncurrent; filing_scope_verified | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | 40,294,000,000 | USD | US GAAP / reported | LongTermDebt; filing_scope_verified | [S04] |
| shares_outstanding | 7,427,000,000 | shares | US GAAP / reported | CommonStockSharesOutstanding; filing_scope_verified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 55,908,000,000 | USD | US GAAP / reported | ShortTermInvestments | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 20,935,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | 9,227,000,000 | USD | US GAAP / reported | LongTermDebtCurrent; filing_scope_verified | [S04] |
| debt_noncurrent | 31,067,000,000 | USD | US GAAP / reported | LongTermDebtNoncurrent; filing_scope_verified | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | 40,294,000,000 | USD | US GAAP / reported | LongTermDebt; filing_scope_verified | [S04] |
| shares_outstanding | 7,427,000,000 | shares | US GAAP / reported | CommonStockSharesOutstanding; filing_scope_verified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 55,908,000,000 | USD | US GAAP / reported | ShortTermInvestments | [S04] |



## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-22T18:36:27.121227+00:00.

Dated curated research is maintained separately: [profile at source commit](https://github.com/eladyesh/stock-brain/blob/c640ba8ecaf78dc0ecb247c1e3ebadf4b6fa77ae/sectors/information-technology/companies/MSFT/README.md) (status reviewed, as of 2026-10-18). Automatic facts never change its review date.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-21 | ARS | 0001193125-26-427876 | — | [S17] |
| 2026-10-21 | DEFA14A | 0001193125-26-427867 | — | [S18] |
| 2026-10-21 | DEF 14A | 0001193125-26-427849 | — | [S19] |
| 2026-10-15 | 4 | 0000789019-26-000228 | — | [S20] |
| 2026-10-14 | 4 | 0000789019-26-000226 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-22T18:30:07.617970+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000789019.json) — published not supplied; retrieved 2026-10-22T17:39:35.977490+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json) — published not supplied; retrieved 2026-10-22T17:54:54.576049+00:00.

[S04] [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.html) — published 2026-07-29; retrieved 2026-10-22T17:54:54.576049+00:00.

[S08] [10-Q 0001193125-26-191507](https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/0001193125-26-191507-index.html) — published 2026-04-29; retrieved 2026-10-22T17:54:54.576049+00:00.

[S17] [ARS 0001193125-26-427876](https://www.sec.gov/Archives/edgar/data/789019/000119312526427876/0001193125-26-427876-index.html) — published 2026-10-21; retrieved 2026-10-22T17:39:35.977490+00:00.

[S18] [DEFA14A 0001193125-26-427867](https://www.sec.gov/Archives/edgar/data/789019/000119312526427867/0001193125-26-427867-index.html) — published 2026-10-21; retrieved 2026-10-22T17:39:35.977490+00:00.

[S19] [DEF 14A 0001193125-26-427849](https://www.sec.gov/Archives/edgar/data/789019/000119312526427849/0001193125-26-427849-index.html) — published 2026-10-21; retrieved 2026-10-22T17:39:35.977490+00:00.

[S20] [4 0000789019-26-000228](https://www.sec.gov/Archives/edgar/data/789019/000078901926000228/0000789019-26-000228-index.html) — published 2026-10-15; retrieved 2026-10-22T17:39:35.977490+00:00.

[S21] [4 0000789019-26-000226](https://www.sec.gov/Archives/edgar/data/789019/000078901926000226/0000789019-26-000226-index.html) — published 2026-10-14; retrieved 2026-10-22T17:39:35.977490+00:00.

Source release: `coverage-20261022-39831584719-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000789019/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
