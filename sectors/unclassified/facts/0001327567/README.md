---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001327567
cik: '0001327567'
company_name: Palo Alto Networks Inc
tickers:
- PANW
status: stub
canonical_reviewed: false
as_of: '2026-10-22'
updated_at: '2026-10-22T18:45:53.881812+00:00'
reviewed_at: null
coverage_release: coverage-20261022-39831584719-1
source_commit: c640ba8ecaf78dc0ecb247c1e3ebadf4b6fa77ae
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-Q
  - '144'
  - 144/A
  - '25'
  - '3'
  - '4'
  - 4/A
  - 424B3
  - 424B7
  - '425'
  - '5'
  - 8-A12B
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - PX14A6G
  - S-3ASR
  - S-4
  - S-4/A
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001327567.json
    sha256: 0fce8129e237331262a97979fde517a19797896a44f4d4eeab2a0767aaa6029f
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0001327567.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001327567.json
    sha256: 54acd6c26e8bfcdf5e0f0dea30dabef27123525133df99729bb4ccd8f000c402
    retrieved_at: '2026-10-22T17:39:35.977490+00:00'
    archive: &id001
      member: CIK0001327567.json
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
  url: https://data.sec.gov/submissions/CIK0001327567.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 54acd6c26e8bfcdf5e0f0dea30dabef27123525133df99729bb4ccd8f000c402
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001327567.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 0fce8129e237331262a97979fde517a19797896a44f4d4eeab2a0767aaa6029f
- id: S04
  title: 10-K 0001327567-26-000023
  url: https://www.sec.gov/Archives/edgar/data/1327567/000132756726000023/0001327567-26-000023-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S08
  title: 10-Q 0001327567-26-000015
  url: https://www.sec.gov/Archives/edgar/data/1327567/000132756726000015/0001327567-26-000015-index.html
  published_at: '2026-06-03'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S17
  title: 4 0001493152-26-046991
  url: https://www.sec.gov/Archives/edgar/data/1327567/000149315226046991/0001493152-26-046991-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S18
  title: 144 0001193125-26-420726
  url: https://www.sec.gov/Archives/edgar/data/1327567/000119312526420726/0001193125-26-420726-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S19
  title: 144 0001968582-26-001051
  url: https://www.sec.gov/Archives/edgar/data/1327567/000196858226001051/0001968582-26-001051-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S20
  title: 4 0001682260-26-000008
  url: https://www.sec.gov/Archives/edgar/data/1327567/000168226026000008/0001682260-26-000008-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
- id: S21
  title: 4 0001193125-26-419277
  url: https://www.sec.gov/Archives/edgar/data/1327567/000119312526419277/0001193125-26-419277-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: null
issuer_classification:
  cik: '0001327567'
  name: Palo Alto Networks Inc
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-22T17:39:35.977490+00:00'
  sha256: 54acd6c26e8bfcdf5e0f0dea30dabef27123525133df99729bb4ccd8f000c402
  url: https://data.sec.gov/submissions/CIK0001327567.json
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: null
  sic_description: null
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0001327567/README.md
full_history_commit: f1dea1c5fdf869d02b10266fe4da900fd3a13544
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# Palo Alto Networks Inc — PANW

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0001327567/README.md)

## Business overview

Reported issuer name: **Palo Alto Networks Inc**. Stable SEC CIK: **0001327567**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| PANW | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

Not available: substantive research has not been completed. Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.

Navigation sector: **unclassified**. Method: `unresolved`. Missing, ambiguous or unmapped reported industry; company-specific review is required.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-08-01 to 2026-07-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | 3,403,000,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 8,077,000,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 307,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 4,553,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 695,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | -440,000,000 | USD | US GAAP / reported | PaymentsToAcquireProductiveAssets; Cash outflow = negative of reported PaymentsToAcquireProductiveAssets; source value retained.; broader_than_property_plant_equipment_only | [S04] |
| revenue | 11,480,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 1,774,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-05-01 to 2026-07-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | 1,106,000,000 | USD | US GAAP / derived | CostOfGoodsAndServicesSold; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 2,304,000,000 | USD | US GAAP / derived | GrossProfit; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income | -282,000,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 1,357,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_income | 172,000,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| purchases_of_productive_assets | -103,000,000 | USD | US GAAP / derived | PaymentsToAcquireProductiveAssets; broader_than_property_plant_equipment_only, cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| revenue | 3,410,000,000 | USD | US GAAP / derived | RevenueFromContractWithCustomerExcludingAssessedTax; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 460,000,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-08-01 to 2026-07-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 2,514,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 557,000,000 | USD | US GAAP / reported | ShortTermInvestments | [S04] |


### quarterly: 2026-05-01 to 2026-07-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 2,514,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 557,000,000 | USD | US GAAP / reported | ShortTermInvestments | [S04] |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-22T18:40:35.368769+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-14 | 4 | 0001493152-26-046991 | — | [S17] |
| 2026-10-13 | 144 | 0001193125-26-420726 | — | [S18] |
| 2026-10-09 | 144 | 0001968582-26-001051 | — | [S19] |
| 2026-10-09 | 4 | 0001682260-26-000008 | — | [S20] |
| 2026-10-09 | 4 | 0001193125-26-419277 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-22T18:30:07.617970+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001327567.json) — published not supplied; retrieved 2026-10-22T17:39:35.977490+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001327567.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001327567-26-000023](https://www.sec.gov/Archives/edgar/data/1327567/000132756726000023/0001327567-26-000023-index.html) — published 2026-09-10; retrieved 2026-10-22T17:39:41.848518+00:00.

[S08] [10-Q 0001327567-26-000015](https://www.sec.gov/Archives/edgar/data/1327567/000132756726000015/0001327567-26-000015-index.html) — published 2026-06-03; retrieved 2026-10-22T17:39:41.848518+00:00.

[S17] [4 0001493152-26-046991](https://www.sec.gov/Archives/edgar/data/1327567/000149315226046991/0001493152-26-046991-index.html) — published 2026-10-14; retrieved 2026-10-22T17:39:35.977490+00:00.

[S18] [144 0001193125-26-420726](https://www.sec.gov/Archives/edgar/data/1327567/000119312526420726/0001193125-26-420726-index.html) — published 2026-10-13; retrieved 2026-10-22T17:39:35.977490+00:00.

[S19] [144 0001968582-26-001051](https://www.sec.gov/Archives/edgar/data/1327567/000196858226001051/0001968582-26-001051-index.html) — published 2026-10-09; retrieved 2026-10-22T17:39:35.977490+00:00.

[S20] [4 0001682260-26-000008](https://www.sec.gov/Archives/edgar/data/1327567/000168226026000008/0001682260-26-000008-index.html) — published 2026-10-09; retrieved 2026-10-22T17:39:35.977490+00:00.

[S21] [4 0001193125-26-419277](https://www.sec.gov/Archives/edgar/data/1327567/000119312526419277/0001193125-26-419277-index.html) — published 2026-10-09; retrieved 2026-10-22T17:39:35.977490+00:00.

Source release: `coverage-20261022-39831584719-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0001327567/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
