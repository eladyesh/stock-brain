---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000096021
cik: 0000096021
company_name: SYSCO CORP
tickers:
- SYY
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
  - 25-NSE
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B2
  - 424B3
  - 424B5
  - '425'
  - 8-A12B
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - CORRESP
  - DEF 14A
  - DEFA14A
  - FWP
  - PX14A6G
  - S-3ASR
  - S-8
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000096021.json
    sha256: 7e1f5a09cbf7f2b6fdcae2845429574fa6b4f60ae7a5a955403b37a55d23dcf5
    retrieved_at: '2026-10-22T17:53:02.398600+00:00'
    archive:
      member: CIK0000096021.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000096021.json
    sha256: 5eadfc8b182aa6a245ab22ab2b920fd6b753b777b153a6825e26d9f5820aa707
    retrieved_at: '2026-10-22T17:52:50.185860+00:00'
    archive: &id001
      member: CIK0000096021.json
      sha256: b6534bf3efaca6ea2a0a9509deb9eb4c612cb9aa12d4913fdb641a526cc4b033
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-22T18:30:08.162126+00:00'
  sha256: 0be94d79fa8280e4e5fed634f305f620ea01ab67dda25960ecd76d3206dc969d
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000096021.json
  published_at: null
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: 5eadfc8b182aa6a245ab22ab2b920fd6b753b777b153a6825e26d9f5820aa707
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000096021.json
  published_at: null
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: 7e1f5a09cbf7f2b6fdcae2845429574fa6b4f60ae7a5a955403b37a55d23dcf5
- id: S04
  title: 10-K 0000096021-26-000033
  url: https://www.sec.gov/Archives/edgar/data/96021/000009602126000033/0000096021-26-000033-index.html
  published_at: '2026-08-21'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S08
  title: 10-Q 0000096021-26-000022
  url: https://www.sec.gov/Archives/edgar/data/96021/000009602126000022/0000096021-26-000022-index.html
  published_at: '2026-04-29'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S17
  title: CERT 0000876661-26-000821
  url: https://www.sec.gov/Archives/edgar/data/96021/000087666126000821/0000876661-26-000821-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: null
- id: S18
  title: 8-A12B 0001104659-26-114102
  url: https://www.sec.gov/Archives/edgar/data/96021/000110465926114102/0001104659-26-114102-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: null
- id: S19
  title: 8-K 0001104659-26-114079
  url: https://www.sec.gov/Archives/edgar/data/96021/000110465926114079/0001104659-26-114079-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: null
- id: S20
  title: 4 0001903968-26-000007
  url: https://www.sec.gov/Archives/edgar/data/96021/000190396826000007/0001903968-26-000007-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: null
- id: S21
  title: 4 0001837149-26-000008
  url: https://www.sec.gov/Archives/edgar/data/96021/000183714926000008/0001837149-26-000008-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: null
issuer_classification:
  cik: 0000096021
  name: SYSCO CORP
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-22T17:52:50.185860+00:00'
  sha256: 5eadfc8b182aa6a245ab22ab2b920fd6b753b777b153a6825e26d9f5820aa707
  url: https://data.sec.gov/submissions/CIK0000096021.json
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: null
  sic_description: null
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000096021/README.md
full_history_commit: f1dea1c5fdf869d02b10266fe4da900fd3a13544
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SYSCO CORP — SYY

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000096021/README.md)

## Business overview

Reported issuer name: **SYSCO CORP**. Stable SEC CIK: **0000096021**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SYY | NYSE | common_stock | 1 | [S01] |

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

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-06-29 to 2026-06-27

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | 68,914,000,000 | USD | US GAAP / reported | CostOfRevenue | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 15,639,000,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 1,757,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 2,638,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 3,095,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | -700,000,000 | USD | US GAAP / reported | PaymentsToAcquireProductiveAssets; Cash outflow = negative of reported PaymentsToAcquireProductiveAssets; source value retained.; broader_than_property_plant_equipment_only | [S04] |
| revenue | 84,553,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 118,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-03-29 to 2026-06-27

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | 17,990,000,000 | USD | US GAAP / derived | CostOfRevenue; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 4,134,000,000 | USD | US GAAP / derived | GrossProfit; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income | 551,000,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 1,175,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_income | 983,000,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| purchases_of_productive_assets | -239,000,000 | USD | US GAAP / derived | PaymentsToAcquireProductiveAssets; broader_than_property_plant_equipment_only, cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| revenue | 22,124,000,000 | USD | US GAAP / derived | RevenueFromContractWithCustomerExcludingAssessedTax; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 23,000,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-06-29 to 2026-06-27

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 1,786,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligationsCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | DebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S04] |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-03-29 to 2026-06-27

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 1,786,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligationsCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | DebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S04] |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-22T18:35:14.619891+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-09 | CERT | 0000876661-26-000821 | — | [S17] |
| 2026-10-06 | 8-A12B | 0001104659-26-114102 | — | [S18] |
| 2026-10-06 | 8-K | 0001104659-26-114079 | — | [S19] |
| 2026-10-02 | 4 | 0001903968-26-000007 | — | [S20] |
| 2026-10-02 | 4 | 0001837149-26-000008 | — | [S21] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-22T18:30:08.162126+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000096021.json) — published not supplied; retrieved 2026-10-22T17:52:50.185860+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000096021.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-K 0000096021-26-000033](https://www.sec.gov/Archives/edgar/data/96021/000009602126000033/0000096021-26-000033-index.html) — published 2026-08-21; retrieved 2026-10-22T17:53:02.398600+00:00.

[S08] [10-Q 0000096021-26-000022](https://www.sec.gov/Archives/edgar/data/96021/000009602126000022/0000096021-26-000022-index.html) — published 2026-04-29; retrieved 2026-10-22T17:53:02.398600+00:00.

[S17] [CERT 0000876661-26-000821](https://www.sec.gov/Archives/edgar/data/96021/000087666126000821/0000876661-26-000821-index.html) — published 2026-10-09; retrieved 2026-10-22T17:52:50.185860+00:00.

[S18] [8-A12B 0001104659-26-114102](https://www.sec.gov/Archives/edgar/data/96021/000110465926114102/0001104659-26-114102-index.html) — published 2026-10-06; retrieved 2026-10-22T17:52:50.185860+00:00.

[S19] [8-K 0001104659-26-114079](https://www.sec.gov/Archives/edgar/data/96021/000110465926114079/0001104659-26-114079-index.html) — published 2026-10-06; retrieved 2026-10-22T17:52:50.185860+00:00.

[S20] [4 0001903968-26-000007](https://www.sec.gov/Archives/edgar/data/96021/000190396826000007/0001903968-26-000007-index.html) — published 2026-10-02; retrieved 2026-10-22T17:52:50.185860+00:00.

[S21] [4 0001837149-26-000008](https://www.sec.gov/Archives/edgar/data/96021/000183714926000008/0001837149-26-000008-index.html) — published 2026-10-02; retrieved 2026-10-22T17:52:50.185860+00:00.

Source release: `coverage-20261022-39831584719-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f1dea1c5fdf869d02b10266fe4da900fd3a13544/brain/companies/0000096021/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
