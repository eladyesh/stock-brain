---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000918965
cik: 0000918965
company_name: SCANSOURCE, INC.
tickers:
- SCSC
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: c5f247f1f77b31a20ec1a66533503255600926f7
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-K/A
  - 10-Q
  - 10-Q/A
  - '144'
  - 144/A
  - '3'
  - '4'
  - 4/A
  - '5'
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - CT ORDER
  - DEF 14A
  - DEFA14A
  - PRE 14A
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SEC STAFF LETTER
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000918965.json
    sha256: a3788afc630c0802859b6d88740b106ba6364cf66f433b9b12a688f6d9b5891e
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0000918965.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000918965.json
    sha256: 63b2e761a725925ab4b4a1f1c67591cf85bce8c333754fedfb0d54ebfa8eeb11
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000918965.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T14:17:54.530395+00:00'
  sha256: a31379ea4791bd232005b22547c9cfa517e0cb9e9f14ff7091be845f143d5c71
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000918965.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 63b2e761a725925ab4b4a1f1c67591cf85bce8c333754fedfb0d54ebfa8eeb11
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000918965.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: a3788afc630c0802859b6d88740b106ba6364cf66f433b9b12a688f6d9b5891e
- id: S04
  title: 10-K 0000918965-26-000044
  url: https://www.sec.gov/Archives/edgar/data/918965/000091896526000044/0000918965-26-000044-index.html
  published_at: '2026-08-20'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S08
  title: 10-Q 0000918965-26-000028
  url: https://www.sec.gov/Archives/edgar/data/918965/000091896526000028/0000918965-26-000028-index.html
  published_at: '2026-05-07'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S17
  title: SCHEDULE 13G/A 0001027796-26-000063
  url: https://www.sec.gov/Archives/edgar/data/918965/000102779626000063/0001027796-26-000063-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: SCHEDULE 13G/A 0000814133-26-000129
  url: https://www.sec.gov/Archives/edgar/data/918965/000081413326000129/0000814133-26-000129-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 144/A 0001964306-26-000442
  url: https://www.sec.gov/Archives/edgar/data/918965/000196430626000442/0001964306-26-000442-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 144/A 0001964306-26-000441
  url: https://www.sec.gov/Archives/edgar/data/918965/000196430626000441/0001964306-26-000441-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 4 0001193125-26-390649
  url: https://www.sec.gov/Archives/edgar/data/918965/000119312526390649/0001193125-26-390649-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000918965
  classification_status: reported_sic
  entity_type: operating
  name: SCANSOURCE, INC.
  sic: '5045'
  sic_description: Wholesale-Computers & Peripheral Equipment & Software
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 63b2e761a725925ab4b4a1f1c67591cf85bce8c333754fedfb0d54ebfa8eeb11
  url: https://data.sec.gov/submissions/CIK0000918965.json
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '5045'
  sic_description: Wholesale-Computers & Peripheral Equipment & Software
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000918965.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000918965/README.md
full_history_commit: 8929b40d1af134561afb621de3adca71dd9577ba
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SCANSOURCE, INC. — SCSC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000918965/README.md)

## Business overview

Reported issuer name: **SCANSOURCE, INC.**. Stable SEC CIK: **0000918965**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SCSC | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **5045**: Wholesale-Computers & Peripheral Equipment & Software. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | 2,788,707,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 437,355,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 78,873,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 123,131,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 98,627,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | -9,286,000 | USD | US GAAP / reported | PaymentsToAcquireProductiveAssets; Cash outflow = negative of reported PaymentsToAcquireProductiveAssets; source value retained.; broader_than_property_plant_equipment_only | [S04] |
| revenue | 3,226,062,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 14,063,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | 833,261,000 | USD | US GAAP / derived | CostOfGoodsAndServicesSold; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 119,848,000 | USD | US GAAP / derived | GrossProfit; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income | 25,618,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | -2,272,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_income | 31,736,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| purchases_of_productive_assets | -2,517,000 | USD | US GAAP / derived | PaymentsToAcquireProductiveAssets; broader_than_property_plant_equipment_only, cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| revenue | 953,109,000 | USD | US GAAP / derived | RevenueFromContractWithCustomerExcludingAssessedTax; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 3,572,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 88,374,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 88,374,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T14:26:27.486108+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-20 | SCHEDULE 13G/A | 0001027796-26-000063 | — | [S17] |
| 2026-10-09 | SCHEDULE 13G/A | 0000814133-26-000129 | — | [S18] |
| 2026-09-15 | 144/A | 0001964306-26-000442 | — | [S19] |
| 2026-09-15 | 144/A | 0001964306-26-000441 | — | [S20] |
| 2026-09-14 | 4 | 0001193125-26-390649 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000918965.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000918965.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0000918965-26-000044](https://www.sec.gov/Archives/edgar/data/918965/000091896526000044/0000918965-26-000044-index.html) — published 2026-08-20; retrieved 2026-10-22T17:39:41.848518+00:00.

[S08] [10-Q 0000918965-26-000028](https://www.sec.gov/Archives/edgar/data/918965/000091896526000028/0000918965-26-000028-index.html) — published 2026-05-07; retrieved 2026-10-22T17:39:41.848518+00:00.

[S17] [SCHEDULE 13G/A 0001027796-26-000063](https://www.sec.gov/Archives/edgar/data/918965/000102779626000063/0001027796-26-000063-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [SCHEDULE 13G/A 0000814133-26-000129](https://www.sec.gov/Archives/edgar/data/918965/000081413326000129/0000814133-26-000129-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [144/A 0001964306-26-000442](https://www.sec.gov/Archives/edgar/data/918965/000196430626000442/0001964306-26-000442-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [144/A 0001964306-26-000441](https://www.sec.gov/Archives/edgar/data/918965/000196430626000441/0001964306-26-000441-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [4 0001193125-26-390649](https://www.sec.gov/Archives/edgar/data/918965/000119312526390649/0001193125-26-390649-index.html) — published 2026-09-14; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000918965/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
