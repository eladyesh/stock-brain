---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000836157
cik: 0000836157
company_name: LINDSAY CORP
tickers:
- LNN
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
  - NT 10-K
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000836157.json
    sha256: e12e8c03017c46ccfcee1ae3dec10c7cd4bdb0feb5f5edf62b15d7871ef77f92
    retrieved_at: '2026-10-23T08:33:18.308731+00:00'
    archive:
      member: CIK0000836157.json
      sha256: 75d1cc8bca6d990b787653521a352ab25164869485705a9fb49551e8e65a9650
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000836157.json
    sha256: d0c13fc1f6f415aee9b6c065d0e8fb68d854017acb9006484aab4f5450c808df
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000836157.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T14:17:55.298415+00:00'
  sha256: be329650ef672c0314f0e16b2e41951f6af4ae314df9a04a32dc11ddb70b194e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000836157.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d0c13fc1f6f415aee9b6c065d0e8fb68d854017acb9006484aab4f5450c808df
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000836157.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:18.308731+00:00'
  sha256: e12e8c03017c46ccfcee1ae3dec10c7cd4bdb0feb5f5edf62b15d7871ef77f92
- id: S04
  title: 10-K 0001193125-26-428926
  url: https://www.sec.gov/Archives/edgar/data/836157/000119312526428926/0001193125-26-428926-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:18.308731+00:00'
  sha256: null
- id: S08
  title: 10-Q 0001193125-26-294516
  url: https://www.sec.gov/Archives/edgar/data/836157/000119312526294516/0001193125-26-294516-index.html
  published_at: '2026-07-02'
  retrieved_at: '2026-10-23T08:33:18.308731+00:00'
  sha256: null
- id: S14
  title: 10-K 0001193125-26-428926
  url: https://www.sec.gov/Archives/edgar/data/836157/000119312526428926/0001193125-26-428926-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S15
  title: 8-K 0001193125-26-428293
  url: https://www.sec.gov/Archives/edgar/data/836157/000119312526428293/0001193125-26-428293-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S16
  title: 8-K 0001193125-26-374348
  url: https://www.sec.gov/Archives/edgar/data/836157/000119312526374348/0001193125-26-374348-index.html
  published_at: '2026-08-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S17
  title: 8-K 0001193125-26-307817
  url: https://www.sec.gov/Archives/edgar/data/836157/000119312526307817/0001193125-26-307817-index.html
  published_at: '2026-07-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 10-Q 0001193125-26-294516
  url: https://www.sec.gov/Archives/edgar/data/836157/000119312526294516/0001193125-26-294516-index.html
  published_at: '2026-07-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000836157
  classification_status: reported_sic
  entity_type: operating
  name: LINDSAY CORP
  sic: '3523'
  sic_description: Farm Machinery & Equipment
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d0c13fc1f6f415aee9b6c065d0e8fb68d854017acb9006484aab4f5450c808df
  url: https://data.sec.gov/submissions/CIK0000836157.json
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '3523'
  sic_description: Farm Machinery & Equipment
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000836157.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000836157/README.md
full_history_commit: 8929b40d1af134561afb621de3adca71dd9577ba
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# LINDSAY CORP — LNN

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000836157/README.md)

## Business overview

Reported issuer name: **LINDSAY CORP**. Stable SEC CIK: **0000836157**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| LNN | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3523**: Farm Machinery & Equipment. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Evidence cutoff: 2026-10-23. Source retrieved: 2026-10-23T08:33:18.308731+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-09-01 to 2026-08-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -40,172,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfRevenue; gross_profit_tieout_failed | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 34,748,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; gross_profit_tieout_failed | [S04] |
| net_income | 55,653,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 55,653,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 74,920,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 66,925,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, gross_profit_tieout_failed | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 5,614,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-06-01 to 2026-08-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -4,658,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / derived / not model usable | CostOfRevenue; cross_filing_derivation, gross_profit_tieout_failed, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | 39,636,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| gross_profit | Unavailable / blocked | USD | US GAAP / derived / not model usable | GrossProfit; cross_filing_derivation, gross_profit_tieout_failed, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income | 11,264,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 11,264,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_cash_flow | 44,294,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_income | 15,793,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / derived / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; cross_filing_derivation, gross_profit_tieout_failed, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 724,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-23. Source retrieved: 2026-10-23T08:33:18.308731+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-09-01 to 2026-08-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 189,836,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S04] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-06-01 to 2026-08-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 189,836,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S04] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T14:25:22.636338+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-22 | 10-K | 0001193125-26-428926 | — | [S14] |
| 2026-10-22 | 8-K | 0001193125-26-428293 | — | [S15] |
| 2026-08-28 | 8-K | 0001193125-26-374348 | — | [S16] |
| 2026-07-17 | 8-K | 0001193125-26-307817 | — | [S17] |
| 2026-07-02 | 10-Q | 0001193125-26-294516 | — | [S18] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:55.298415+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000836157.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000836157.json) — published not supplied; retrieved 2026-10-23T08:33:18.308731+00:00.

[S04] [10-K 0001193125-26-428926](https://www.sec.gov/Archives/edgar/data/836157/000119312526428926/0001193125-26-428926-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:18.308731+00:00.

[S08] [10-Q 0001193125-26-294516](https://www.sec.gov/Archives/edgar/data/836157/000119312526294516/0001193125-26-294516-index.html) — published 2026-07-02; retrieved 2026-10-23T08:33:18.308731+00:00.

[S14] [10-K 0001193125-26-428926](https://www.sec.gov/Archives/edgar/data/836157/000119312526428926/0001193125-26-428926-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S15] [8-K 0001193125-26-428293](https://www.sec.gov/Archives/edgar/data/836157/000119312526428293/0001193125-26-428293-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S16] [8-K 0001193125-26-374348](https://www.sec.gov/Archives/edgar/data/836157/000119312526374348/0001193125-26-374348-index.html) — published 2026-08-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S17] [8-K 0001193125-26-307817](https://www.sec.gov/Archives/edgar/data/836157/000119312526307817/0001193125-26-307817-index.html) — published 2026-07-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [10-Q 0001193125-26-294516](https://www.sec.gov/Archives/edgar/data/836157/000119312526294516/0001193125-26-294516-index.html) — published 2026-07-02; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/8929b40d1af134561afb621de3adca71dd9577ba/brain/companies/0000836157/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
