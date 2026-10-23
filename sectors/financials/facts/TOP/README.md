---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001848275
cik: 0001848275
company_name: TOP Financial Group Ltd
tickers:
- TOP
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: 3f697433c3580d4ca83edbe44c66580ac926c8d7
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-Q
  - 20-F
  - '3'
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-K
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - NT 10-K
  - NT 10-Q
  - NT 20-F
  - POS AM
  - SC 13G
  - SCHEDULE 13D
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001848275.json
    sha256: 4045d8c36af04e14a79208f806de5f8447a054c4d6818c583ff9beb4ba6eafc8
    retrieved_at: '2026-10-22T17:53:02.398600+00:00'
    archive:
      member: CIK0001848275.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001848275.json
    sha256: dd5e1c6315de0a7e07664431320db7eb0185a7699bff7131d0f818a8fbdc2d66
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001848275.json
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
  url: https://data.sec.gov/submissions/CIK0001848275.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: dd5e1c6315de0a7e07664431320db7eb0185a7699bff7131d0f818a8fbdc2d66
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001848275.json
  published_at: null
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: 4045d8c36af04e14a79208f806de5f8447a054c4d6818c583ff9beb4ba6eafc8
- id: S04
  title: 10-K 0001213900-26-075954
  url: https://www.sec.gov/Archives/edgar/data/1848275/000121390026075954/0001213900-26-075954-index.html
  published_at: '2026-07-07'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001213900-26-090479
  url: https://www.sec.gov/Archives/edgar/data/1848275/000121390026090479/0001213900-26-090479-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S06
  title: 8-K 0001213900-26-110029
  url: https://www.sec.gov/Archives/edgar/data/1848275/000121390026110029/0001213900-26-110029-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 8-K 0001213900-26-109242
  url: https://www.sec.gov/Archives/edgar/data/1848275/000121390026109242/0001213900-26-109242-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: 3 0002159927-26-000001
  url: https://www.sec.gov/Archives/edgar/data/1848275/000215992726000001/0002159927-26-000001-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: 8-K 0001213900-26-108497
  url: https://www.sec.gov/Archives/edgar/data/1848275/000121390026108497/0001213900-26-108497-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S10
  title: EFFECT 9999999995-26-003193
  url: https://www.sec.gov/Archives/edgar/data/1848275/999999999526003193/9999999995-26-003193-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001848275
  classification_status: reported_sic
  entity_type: operating
  name: TOP Financial Group Ltd
  sic: '6200'
  sic_description: Security & Commodity Brokers, Dealers, Exchanges & Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: dd5e1c6315de0a7e07664431320db7eb0185a7699bff7131d0f818a8fbdc2d66
  url: https://data.sec.gov/submissions/CIK0001848275.json
listings:
- ticker: TOP
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-075954
  filed: '2026-07-07'
  form: 10-K
  period_end: '2026-03-31'
  url: https://www.sec.gov/Archives/edgar/data/1848275/000121390026075954/0001213900-26-075954-index.html
- accession: 0001213900-26-090479
  filed: '2026-08-17'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1848275/000121390026090479/0001213900-26-090479-index.html
- accession: 0001213900-26-110029
  filed: '2026-10-16'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1848275/000121390026110029/0001213900-26-110029-index.html
research_progress:
  stage: pending
  input_sha256: 29f7f13ac2380f708d23e81bd3b69ffd43ac86eda943091df492b620e7d67b95
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: financials
  method: project_sic_rule
  sic: '6200'
  sic_description: Security & Commodity Brokers, Dealers, Exchanges & Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001848275.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/TOP/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# TOP — TOP Financial Group Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/TOP/README.md)

## Business overview

Reported issuer name: **TOP Financial Group Ltd**. Stable SEC CIK: **0001848275**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| TOP | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6200**: Security & Commodity Brokers, Dealers, Exchanges & Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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

### annual: 2025-04-01 to 2026-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -899,500 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 13,122,296 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | -1,170,823 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | -1,175,539 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 14,021,796 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | -1,177,320 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | Revenues; alternative_tag_scope_differs | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 60,194 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -3,112 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S05] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 6,031,674 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S05] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | -113,433 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | -113,725 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | 6,034,786 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S05] |
| operating_income | -386,954 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | Revenues; alternative_tag_scope_differs | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-04-01 to 2026-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 12,989,922 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 10,407,367 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

Not available: reviewed debt maturity, acquisition, dividend and repurchase analysis.

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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T14:33:54.796111+00:00.

### Research work queue

Collection stage: **pending**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (evidence or analysis still needed): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (evidence or analysis still needed): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (evidence or analysis still needed): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (evidence or analysis still needed): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (evidence or analysis still needed): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
- **Growth drivers** (evidence or analysis still needed): Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.
- **Financial performance** (evidence or analysis still needed): Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.
- **Balance sheet and capital allocation** (evidence or analysis still needed): Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.
- **Management and governance** (evidence or analysis still needed): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
- **Valuation context** (evidence or analysis still needed): Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.
- **Catalysts** (evidence or analysis still needed): List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.
- **Risks and thesis breakers** (evidence or analysis still needed): Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.
- **Scenarios and open questions** (evidence or analysis still needed): Separate bull, base, and bear assumptions from facts. Record missing data, disputed evidence, and research questions without inventing answers.
- **Relationships and themes** (evidence or analysis still needed): Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.
- **Recent developments** (evidence or analysis still needed): Keep a dated, source-backed log of material changes. Distinguish the event date from the article date and explain what changed in the profile.

Calculation gaps: Operating margin: compatible positive revenue and usable inputs are required. Net margin: compatible positive revenue and usable inputs are required. Free cash flow margin: compatible positive revenue and usable inputs are required. Stock compensation / revenue: compatible positive revenue and usable inputs are required. revenue: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. net_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-16 | 8-K | 0001213900-26-110029 | — | [S06] |
| 2026-10-14 | 8-K | 0001213900-26-109242 | — | [S07] |
| 2026-10-13 | 3 | 0002159927-26-000001 | — | [S08] |
| 2026-10-09 | 8-K | 0001213900-26-108497 | — | [S09] |
| 2026-10-08 | EFFECT | 9999999995-26-003193 | — | [S10] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001848275.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001848275.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-K 0001213900-26-075954](https://www.sec.gov/Archives/edgar/data/1848275/000121390026075954/0001213900-26-075954-index.html) — published 2026-07-07; retrieved 2026-10-22T17:53:02.398600+00:00.

[S05] [10-Q 0001213900-26-090479](https://www.sec.gov/Archives/edgar/data/1848275/000121390026090479/0001213900-26-090479-index.html) — published 2026-08-17; retrieved 2026-10-22T17:53:02.398600+00:00.

[S06] [8-K 0001213900-26-110029](https://www.sec.gov/Archives/edgar/data/1848275/000121390026110029/0001213900-26-110029-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [8-K 0001213900-26-109242](https://www.sec.gov/Archives/edgar/data/1848275/000121390026109242/0001213900-26-109242-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [3 0002159927-26-000001](https://www.sec.gov/Archives/edgar/data/1848275/000215992726000001/0002159927-26-000001-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [8-K 0001213900-26-108497](https://www.sec.gov/Archives/edgar/data/1848275/000121390026108497/0001213900-26-108497-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S10] [EFFECT 9999999995-26-003193](https://www.sec.gov/Archives/edgar/data/1848275/999999999526003193/9999999995-26-003193-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/TOP/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
