---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000100726
cik: '0000100726'
company_name: UNIFI INC
tickers:
- UFI
status: stub
canonical_reviewed: false
as_of: '2026-10-29'
updated_at: '2026-10-29T16:18:46.634043+00:00'
reviewed_at: null
coverage_release: coverage-20261029-40909364006-1
source_commit: 066173dd7c0933a11c2085b144bbb14099b44560
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
  - 3/A
  - '4'
  - 4/A
  - 424B3
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
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000100726.json
    sha256: 8f436e4863a0e158970ac22a66a91c5200e6da8687203955d2d5e794697d931c
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0000100726.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000100726.json
    sha256: e5371dc5c0a5107fe465cca2f1702d26701235cbfb2d82df93829860c419f20d
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000100726.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-29T16:14:13.951866+00:00'
  sha256: 2ac9bdaf5d770442eb34b0b33eb6a5240dbd11a3f2077f7b88051dbb82d4313b
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000100726.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e5371dc5c0a5107fe465cca2f1702d26701235cbfb2d82df93829860c419f20d
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000100726.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 8f436e4863a0e158970ac22a66a91c5200e6da8687203955d2d5e794697d931c
- id: S04
  title: 10-K 0000100726-26-000012
  url: https://www.sec.gov/Archives/edgar/data/100726/000010072626000012/0000100726-26-000012-index.html
  published_at: '2026-08-26'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S08
  title: 10-Q 0000100726-26-000004
  url: https://www.sec.gov/Archives/edgar/data/100726/000010072626000004/0000100726-26-000004-index.html
  published_at: '2026-05-06'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S17
  title: 4 0001213900-26-111354
  url: https://www.sec.gov/Archives/edgar/data/100726/000121390026111354/0001213900-26-111354-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: SCHEDULE 13G/A 0001104659-26-115448
  url: https://www.sec.gov/Archives/edgar/data/100726/000110465926115448/0001104659-26-115448-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: DEFA14A 0000100726-26-000016
  url: https://www.sec.gov/Archives/edgar/data/100726/000010072626000016/0000100726-26-000016-index.html
  published_at: '2026-09-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: DEF 14A 0000100726-26-000015
  url: https://www.sec.gov/Archives/edgar/data/100726/000010072626000015/0000100726-26-000015-index.html
  published_at: '2026-09-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 10-K 0000100726-26-000012
  url: https://www.sec.gov/Archives/edgar/data/100726/000010072626000012/0000100726-26-000012-index.html
  published_at: '2026-08-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0000100726'
  classification_status: reported_sic
  entity_type: operating
  name: UNIFI INC
  sic: '2200'
  sic_description: Textile Mill Products
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: e5371dc5c0a5107fe465cca2f1702d26701235cbfb2d82df93829860c419f20d
  url: https://data.sec.gov/submissions/CIK0000100726.json
listings:
- ticker: UFI
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0000100726-26-000012
  filed: '2026-08-26'
  form: 10-K
  period_end: '2026-06-28'
  url: https://www.sec.gov/Archives/edgar/data/100726/000010072626000012/0000100726-26-000012-index.html
- accession: 0000100726-26-000004
  filed: '2026-05-06'
  form: 10-Q
  period_end: '2026-03-29'
  url: https://www.sec.gov/Archives/edgar/data/100726/000010072626000004/0000100726-26-000004-index.html
- accession: 0000100726-26-000015
  filed: '2026-09-11'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/100726/000010072626000015/0000100726-26-000015-index.html
- accession: 0000100726-26-000010
  filed: '2026-08-19'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/100726/000010072626000010/0000100726-26-000010-index.html
- accession: 0000950170-24-011723
  filed: '2024-02-06'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/100726/000095017024011723/0000950170-24-011723-index.html
- accession: 0001564590-20-029340
  filed: '2020-06-15'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/100726/000156459020029340/0001564590-20-029340-index.html
- accession: 0001564590-20-028248
  filed: '2020-06-03'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/100726/000156459020028248/0001564590-20-028248-index.html
- accession: 0001193125-17-206082
  filed: '2017-06-16'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/100726/000119312517206082/0001193125-17-206082-index.html
- accession: 0001193125-17-176777
  filed: '2017-05-19'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/100726/000119312517176777/0001193125-17-176777-index.html
- accession: 0001437749-16-035552
  filed: '2016-07-22'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/100726/000143774916035552/0001437749-16-035552-index.html
- accession: 0001437749-16-035262
  filed: '2016-07-15'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/100726/000143774916035262/0001437749-16-035262-index.html
- accession: 0001437749-13-014391
  filed: '2013-11-12'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/100726/000143774913014391/0001437749-13-014391-index.html
research_progress:
  stage: pending
  input_sha256: 150065c8bbc3debc440eba27a02c639eaf5a59d29bc0e59828d923c374142284
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 4
  model_draft: false
  reviewed: false
sector_assignment:
  sector: consumer-discretionary
  method: project_sic_rule
  sic: '2200'
  sic_description: Textile Mill Products
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000100726.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/UFI/README.md
full_history_commit: 52b6569b626a07b359d4a15742ebb633a0e48007
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# UFI — UNIFI INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/UFI/README.md)

## Business overview

Reported issuer name: **UNIFI INC**. Stable SEC CIK: **0000100726**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| UFI | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2200**: Textile Mill Products. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **consumer-discretionary**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was -2.76% for 2025-06-30 to 2026-06-28 (US GAAP inputs). [S21]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=-14648000 USD (OperatingIncomeLoss), revenue=531303000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was -4.62% for 2025-06-30 to 2026-06-28 (US GAAP inputs). [S21]
Formula: `net_income / revenue * 100`. Inputs: net_income=-24562000 USD (NetIncomeLoss), revenue=531303000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Free cash flow margin was 4.05% for 2025-06-30 to 2026-06-28 (US GAAP inputs). [S21]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=21532000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=531303000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual revenue changed -7.01% from the year ended 2025-06-29 to 2026-06-28. [S21]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=531303000 USD (RevenueFromContractWithCustomerExcludingAssessedTax), revenue=571344000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-06-30 to 2026-06-28

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -5,002,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 500,847,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 21,532,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 30,456,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | -24,562,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | -24,562,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 26,534,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | -14,648,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 531,303,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-03-30 to 2026-06-28

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -1,130,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| cost_of_revenue | 129,883,000 | USD | US GAAP / derived | CostOfGoodsAndServicesSold; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 1,011,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| gross_profit | 14,341,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | -1,193,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | -1,193,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_cash_flow | 2,141,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| operating_income | 2,378,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S08] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 144,224,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-06-30 to 2026-06-28

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 25,072,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligationsCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | DebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S04] |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-03-30 to 2026-06-28

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 25,072,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligationsCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | DebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S04] |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:28:13.513369+00:00.

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

Calculation gaps: Stock compensation / revenue: compatible positive revenue and usable inputs are required. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. net_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-21 | 4 | 0001213900-26-111354 | — | [S17] |
| 2026-10-13 | SCHEDULE 13G/A | 0001104659-26-115448 | — | [S18] |
| 2026-09-11 | DEFA14A | 0000100726-26-000016 | — | [S19] |
| 2026-09-11 | DEF 14A | 0000100726-26-000015 | — | [S20] |
| 2026-08-26 | 10-K | 0000100726-26-000012 | — | [S21] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.951866+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000100726.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000100726.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0000100726-26-000012](https://www.sec.gov/Archives/edgar/data/100726/000010072626000012/0000100726-26-000012-index.html) — published 2026-08-26; retrieved 2026-10-22T17:39:41.848518+00:00.

[S08] [10-Q 0000100726-26-000004](https://www.sec.gov/Archives/edgar/data/100726/000010072626000004/0000100726-26-000004-index.html) — published 2026-05-06; retrieved 2026-10-22T17:39:41.848518+00:00.

[S17] [4 0001213900-26-111354](https://www.sec.gov/Archives/edgar/data/100726/000121390026111354/0001213900-26-111354-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [SCHEDULE 13G/A 0001104659-26-115448](https://www.sec.gov/Archives/edgar/data/100726/000110465926115448/0001104659-26-115448-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [DEFA14A 0000100726-26-000016](https://www.sec.gov/Archives/edgar/data/100726/000010072626000016/0000100726-26-000016-index.html) — published 2026-09-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [DEF 14A 0000100726-26-000015](https://www.sec.gov/Archives/edgar/data/100726/000010072626000015/0000100726-26-000015-index.html) — published 2026-09-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [10-K 0000100726-26-000012](https://www.sec.gov/Archives/edgar/data/100726/000010072626000012/0000100726-26-000012-index.html) — published 2026-08-26; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/52b6569b626a07b359d4a15742ebb633a0e48007/brain/companies/UFI/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
