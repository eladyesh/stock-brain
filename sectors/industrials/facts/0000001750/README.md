---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000001750
cik: '0000001750'
company_name: AAR CORP
tickers:
- AIR
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T08:47:59.341415+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39925380279-1
source_commit: 78606fb159189686ce54eb7bc0fa1098e51dc3ab
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
  - '4'
  - 4/A
  - 424B5
  - 8-A12B
  - 8-A12B/A
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - CORRESP
  - DEF 14A
  - DEFA14A
  - S-3ASR
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
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000001750.json
    sha256: 68cd2263e381f8f1521377b94279b51791058f8c51721fd02a01639b781c1284
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0000001750.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000001750.json
    sha256: ca88d7b23004788ef286854a92c6821b2a7f8923136488d14ceb3e5e78b964ba
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000001750.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T08:33:49.304929+00:00'
  sha256: 6b752ea8975cd8cfe39564769459d8cea3289453fb9454cc2eb02663466ddb67
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000001750.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ca88d7b23004788ef286854a92c6821b2a7f8923136488d14ceb3e5e78b964ba
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000001750.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 68cd2263e381f8f1521377b94279b51791058f8c51721fd02a01639b781c1284
- id: S04
  title: 10-K 0001104659-26-085459
  url: https://www.sec.gov/Archives/edgar/data/1750/000110465926085459/0001104659-26-085459-index.html
  published_at: '2026-07-22'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001104659-26-111786
  url: https://www.sec.gov/Archives/edgar/data/1750/000110465926111786/0001104659-26-111786-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S17
  title: 4 0000001750-26-000104
  url: https://www.sec.gov/Archives/edgar/data/1750/000000175026000104/0000001750-26-000104-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 144 0001950047-26-010316
  url: https://www.sec.gov/Archives/edgar/data/1750/000195004726010316/0001950047-26-010316-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: S-8 0001104659-26-112722
  url: https://www.sec.gov/Archives/edgar/data/1750/000110465926112722/0001104659-26-112722-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 10-Q 0001104659-26-111786
  url: https://www.sec.gov/Archives/edgar/data/1750/000110465926111786/0001104659-26-111786-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 8-K 0001104659-26-111482
  url: https://www.sec.gov/Archives/edgar/data/1750/000110465926111482/0001104659-26-111482-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0000001750'
  classification_status: reported_sic
  entity_type: operating
  name: AAR CORP
  sic: '3720'
  sic_description: Aircraft & Parts
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ca88d7b23004788ef286854a92c6821b2a7f8923136488d14ceb3e5e78b964ba
  url: https://data.sec.gov/submissions/CIK0000001750.json
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '3720'
  sic_description: Aircraft & Parts
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000001750.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0000001750/README.md
full_history_commit: ffcaf17e05894e3d5a5cf6f414562c7c11a15184
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AAR CORP — AIR

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0000001750/README.md)

## Business overview

Reported issuer name: **AAR CORP**. Stable SEC CIK: **0000001750**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AIR | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3720**: Aircraft & Parts. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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

### annual: 2025-06-01 to 2026-05-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -36,600,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 2,686,000,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 62,100,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 622,000,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 187,700,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 187,700,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 98,700,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 3,308,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerIncludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 17,800,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-06-01 to 2026-08-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -11,800,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S05] |
| cost_of_revenue | 741,700,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 44,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S05] |
| gross_profit | 176,300,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | 40,100,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 40,100,000 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | 55,800,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S05] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 918,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerIncludingAssessedTax | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 7,800,000 | USD | US GAAP / reported | ShareBasedCompensation | [S05] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-06-01 to 2026-05-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 84,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-06-01 to 2026-08-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 104,500,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review, definition_changed_across_series | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T08:37:30.314138+00:00.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-22 | 4 | 0000001750-26-000104 | — | [S17] |
| 2026-10-20 | 144 | 0001950047-26-010316 | — | [S18] |
| 2026-10-01 | S-8 | 0001104659-26-112722 | — | [S19] |
| 2026-09-29 | 10-Q | 0001104659-26-111786 | — | [S20] |
| 2026-09-29 | 8-K | 0001104659-26-111482 | — | [S21] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-23T08:33:49.304929+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000001750.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000001750.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001104659-26-085459](https://www.sec.gov/Archives/edgar/data/1750/000110465926085459/0001104659-26-085459-index.html) — published 2026-07-22; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [10-Q 0001104659-26-111786](https://www.sec.gov/Archives/edgar/data/1750/000110465926111786/0001104659-26-111786-index.html) — published 2026-09-29; retrieved 2026-10-22T17:39:41.848518+00:00.

[S17] [4 0000001750-26-000104](https://www.sec.gov/Archives/edgar/data/1750/000000175026000104/0000001750-26-000104-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [144 0001950047-26-010316](https://www.sec.gov/Archives/edgar/data/1750/000195004726010316/0001950047-26-010316-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [S-8 0001104659-26-112722](https://www.sec.gov/Archives/edgar/data/1750/000110465926112722/0001104659-26-112722-index.html) — published 2026-10-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [10-Q 0001104659-26-111786](https://www.sec.gov/Archives/edgar/data/1750/000110465926111786/0001104659-26-111786-index.html) — published 2026-09-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [8-K 0001104659-26-111482](https://www.sec.gov/Archives/edgar/data/1750/000110465926111482/0001104659-26-111482-index.html) — published 2026-09-29; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39925380279-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ffcaf17e05894e3d5a5cf6f414562c7c11a15184/brain/companies/0000001750/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
