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
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: ef2ed016c2c344c23ee7fb991b25bf93660da77e
financial_history_available: true
curated_research:
  url: https://github.com/eladyesh/stock-brain/blob/ef2ed016c2c344c23ee7fb991b25bf93660da77e/sectors/information-technology/companies/MSFT/README.md
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
    sha256: 464cc12cc4796c90a6a0c709eb4920788aa7d4d5eee8b44f2d11d7d44804ae37
    retrieved_at: '2026-10-30T06:31:01.023895+00:00'
  submissions:
    url: https://data.sec.gov/submissions/CIK0000789019.json
    sha256: a9a65d8640cde1fe6fd7cf0219d5b948f431bf4f8b7954de4386d62f7eaa2523
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000789019.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:11.183681+00:00'
  sha256: 64301e84a89de015f12206ec26fa4a677c38e33277e47d0b3a6b91e370e8d274
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000789019.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: a9a65d8640cde1fe6fd7cf0219d5b948f431bf4f8b7954de4386d62f7eaa2523
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json
  published_at: null
  retrieved_at: '2026-10-30T06:31:01.023895+00:00'
  sha256: 464cc12cc4796c90a6a0c709eb4920788aa7d4d5eee8b44f2d11d7d44804ae37
- id: S04
  title: 10-K 0001193125-26-323660
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.html
  published_at: '2026-07-29'
  retrieved_at: '2026-10-30T06:31:01.023895+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001193125-26-436133
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.html
  published_at: '2026-10-28'
  retrieved_at: '2026-10-30T06:31:01.023895+00:00'
  sha256: null
- id: S17
  title: ARS 0001193125-26-427876
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526427876/0001193125-26-427876-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: DEFA14A 0001193125-26-427867
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526427867/0001193125-26-427867-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: DEF 14A 0001193125-26-427849
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526427849/0001193125-26-427849-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0000789019-26-000228
  url: https://www.sec.gov/Archives/edgar/data/789019/000078901926000228/0000789019-26-000228-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 4 0000789019-26-000226
  url: https://www.sec.gov/Archives/edgar/data/789019/000078901926000226/0000789019-26-000226-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000789019
  classification_status: reported_sic
  entity_type: operating
  name: MICROSOFT CORP
  sic: '7372'
  sic_description: Services-Prepackaged Software
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: a9a65d8640cde1fe6fd7cf0219d5b948f431bf4f8b7954de4386d62f7eaa2523
  url: https://data.sec.gov/submissions/CIK0000789019.json
listings:
- ticker: MSFT
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-323660
  filed: '2026-07-29'
  form: 10-K
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.html
- accession: 0001193125-26-191507
  filed: '2026-04-29'
  form: 10-Q
  period_end: '2026-03-31'
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/0001193125-26-191507-index.html
- accession: 0001193125-26-427849
  filed: '2026-10-21'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526427849/0001193125-26-427849-index.html
- accession: 0001193125-26-380280
  filed: '2026-09-02'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312526380280/0001193125-26-380280-index.html
- accession: 0001193125-24-062997
  filed: '2024-03-08'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/789019/000119312524062997/0001193125-24-062997-index.html
research_progress:
  stage: pending
  input_sha256: 2c36ed0777c186ef55e5211f880bcad6d133d49b4ba05465a1f6e35c3040e70b
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 10
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: curated_profile
  sic: '7372'
  sic_description: Services-Prepackaged Software
  rule_version: 1
  reason: Uses the dated curated profile assignment; automatic data does not renew
    its review.
  source_url: https://github.com/eladyesh/stock-brain/blob/ef2ed016c2c344c23ee7fb991b25bf93660da77e/sectors/information-technology/companies/MSFT/README.md
full_history_url: https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/MSFT/README.md
full_history_commit: 79888139fa1fe8ad3404e6bc04e318eee1474f73
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# MSFT — MICROSOFT CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/MSFT/README.md)

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

SEC-reported SIC **7372**: Services-Prepackaged Software. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `curated_profile`. Uses the dated curated profile assignment; automatic data does not renew its review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was 46.78% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S04]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=155237000000 USD (OperatingIncomeLoss), revenue=331839000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was 40.31% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=133749000000 USD (NetIncomeLoss), revenue=331839000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Free cash flow margin was 20.19% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S04]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=66987000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=331839000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Stock compensation / revenue was 3.74% for 2025-07-01 to 2026-06-30 (US GAAP inputs). [S04]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=12405000000 USD (ShareBasedCompensation), revenue=331839000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual revenue changed +17.79% from the year ended 2025-06-30 to 2026-06-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=331839000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax), revenue=281724000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual operating income changed +20.78% from the year ended 2025-06-30 to 2026-06-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=155237000000 USD (OperatingIncomeLoss), operating_income=128528000000 USD (OperatingIncomeLoss).

Derived observation: Annual net income changed +31.34% from the year ended 2025-06-30 to 2026-06-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=133749000000 USD (NetIncomeLoss), net_income=101832000000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +34.35% from the year ended 2025-06-30 to 2026-06-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=182935000000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=136162000000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed -6.46% from the year ended 2025-06-30 to 2026-06-30. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=66987000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=71611000000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 1.37x for the year ended 2026-06-30. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=182935000000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=133749000000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-30. Source retrieved: 2026-10-30T06:31:01.023895+00:00. [S03]

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


### quarterly: 2026-07-01 to 2026-09-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -39,367,000,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S05] |
| cost_of_revenue | 29,720,000,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 18,633,000,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S05] |
| gross_profit | 62,559,000,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | 36,629,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 58,000,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S05] |
| operating_income | 45,915,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 92,279,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 3,134,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S05] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-30. Source retrieved: 2026-10-30T06:31:01.023895+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-07-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 20,935,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 55,908,000,000 | USD | US GAAP / reported | ShortTermInvestments | [S05] |


### quarterly: 2026-07-01 to 2026-09-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 20,281,000,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | 44,228,000,000 | USD | US GAAP / reported | ShortTermInvestments | [S05] |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:29:09.982870+00:00.

Dated curated research is maintained separately: [profile at source commit](https://github.com/eladyesh/stock-brain/blob/ef2ed016c2c344c23ee7fb991b25bf93660da77e/sectors/information-technology/companies/MSFT/README.md) (status reviewed, as of 2026-10-18). Automatic facts never change its review date.

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

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:11.183681+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000789019.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json) — published not supplied; retrieved 2026-10-30T06:31:01.023895+00:00.

[S04] [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.html) — published 2026-07-29; retrieved 2026-10-30T06:31:01.023895+00:00.

[S05] [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.html) — published 2026-10-28; retrieved 2026-10-30T06:31:01.023895+00:00.

[S17] [ARS 0001193125-26-427876](https://www.sec.gov/Archives/edgar/data/789019/000119312526427876/0001193125-26-427876-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [DEFA14A 0001193125-26-427867](https://www.sec.gov/Archives/edgar/data/789019/000119312526427867/0001193125-26-427867-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [DEF 14A 0001193125-26-427849](https://www.sec.gov/Archives/edgar/data/789019/000119312526427849/0001193125-26-427849-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0000789019-26-000228](https://www.sec.gov/Archives/edgar/data/789019/000078901926000228/0000789019-26-000228-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [4 0000789019-26-000226](https://www.sec.gov/Archives/edgar/data/789019/000078901926000226/0000789019-26-000226-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/MSFT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
