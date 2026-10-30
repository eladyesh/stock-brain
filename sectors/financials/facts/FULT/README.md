---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000700564
cik: '0000700564'
company_name: FULTON FINANCIAL CORP
tickers:
- FULT
- FULTP
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: f9a34108789a82bf7c75f9d65a0e9552aa5552db
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-Q
  - 11-K
  - '144'
  - 144/A
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B2
  - 424B3
  - 424B5
  - '425'
  - '5'
  - 8-A12B
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - CORRESP
  - CT ORDER
  - DEF 14A
  - DEFA14A
  - EFFECT
  - FWP
  - NT 10-K
  - S-3ASR
  - S-4
  - S-4/A
  - S-8
  - S-8 POS
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000700564.json
    sha256: fee75e4055c9cd5a51f85d8a8a279109c8c0e7eef5365e014bcf80e0415f060e
    retrieved_at: '2026-10-22T18:10:35.452616+00:00'
    archive:
      member: CIK0000700564.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000700564.json
    sha256: 725dace3d30a39ffc38053731b1fd59cbeef74fd00b1e1add63a5ee251f9c63a
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000700564.json
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
  url: https://data.sec.gov/submissions/CIK0000700564.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 725dace3d30a39ffc38053731b1fd59cbeef74fd00b1e1add63a5ee251f9c63a
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000700564.json
  published_at: null
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: fee75e4055c9cd5a51f85d8a8a279109c8c0e7eef5365e014bcf80e0415f060e
- id: S04
  title: 10-K 0000700564-26-000006
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056426000006/0000700564-26-000006-index.html
  published_at: '2026-02-27'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S08
  title: 10-Q 0000700564-26-000033
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056426000033/0000700564-26-000033-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S09
  title: 10-Q 0000700564-26-000016
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056426000016/0000700564-26-000016-index.html
  published_at: '2026-05-08'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S16
  title: 8-K 0000700564-26-000036
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056426000036/0000700564-26-000036-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S17
  title: 4 0001592539-26-000002
  url: https://www.sec.gov/Archives/edgar/data/700564/000159253926000002/0001592539-26-000002-index.html
  published_at: '2026-09-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 3 0001592539-26-000001
  url: https://www.sec.gov/Archives/edgar/data/700564/000159253926000001/0001592539-26-000001-index.html
  published_at: '2026-09-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0002035688-26-000003
  url: https://www.sec.gov/Archives/edgar/data/700564/000203568826000003/0002035688-26-000003-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0002086746-26-000003
  url: https://www.sec.gov/Archives/edgar/data/700564/000208674626000003/0002086746-26-000003-index.html
  published_at: '2026-09-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0000700564'
  classification_status: reported_sic
  entity_type: operating
  name: FULTON FINANCIAL CORP
  sic: '6021'
  sic_description: National Commercial Banks
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 725dace3d30a39ffc38053731b1fd59cbeef74fd00b1e1add63a5ee251f9c63a
  url: https://data.sec.gov/submissions/CIK0000700564.json
listings:
- ticker: FULT
  exchange: NASDAQ
  instrument_type: common_stock
- ticker: FULTP
  exchange: NASDAQ
  instrument_type: preferred
research_filings:
- accession: 0000700564-26-000006
  filed: '2026-02-27'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056426000006/0000700564-26-000006-index.html
- accession: 0000700564-26-000033
  filed: '2026-08-07'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056426000033/0000700564-26-000033-index.html
- accession: 0001206774-26-000176
  filed: '2026-04-01'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/700564/000120677426000176/0001206774-26-000176-index.html
- accession: 0000700564-26-000036
  filed: '2026-10-21'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056426000036/0000700564-26-000036-index.html
- accession: 0000700564-25-000037
  filed: '2025-07-16'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056425000037/0000700564-25-000037-index.html
- accession: 0000700564-25-000013
  filed: '2025-02-28'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056425000013/0000700564-25-000013-index.html
- accession: 0000700564-23-000031
  filed: '2023-06-21'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056423000031/0000700564-23-000031-index.html
- accession: 0000700564-23-000006
  filed: '2023-01-18'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056423000006/0000700564-23-000006-index.html
- accession: 0000700564-20-000022
  filed: '2020-04-22'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056420000022/0000700564-20-000022-index.html
- accession: 0000700564-20-000009
  filed: '2020-02-12'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056420000009/0000700564-20-000009-index.html
- accession: 0000700564-18-000005
  filed: '2018-01-23'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/700564/000070056418000005/0000700564-18-000005-index.html
- accession: 0001193125-17-351442
  filed: '2017-11-24'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/700564/000119312517351442/0001193125-17-351442-index.html
research_progress:
  stage: pending
  input_sha256: 676a4985e59d15e8a880044439b99919bea06914496fb2e9c4030a0c52db33bb
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 5
  model_draft: false
  reviewed: false
sector_assignment:
  sector: financials
  method: project_sic_rule
  sic: '6021'
  sic_description: National Commercial Banks
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000700564.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/FULT/README.md
full_history_commit: 1b4771bc41dec553e210323f72d9bfc908288c04
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# FULT, FULTP — FULTON FINANCIAL CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/FULT/README.md)

## Business overview

Reported issuer name: **FULTON FINANCIAL CORP**. Stable SEC CIK: **0000700564**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| FULT | NASDAQ | common_stock | 1 | [S01] |
| FULTP | NASDAQ | preferred | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6021**: National Commercial Banks. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Net margin was 141.49% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S04]
Formula: `net_income / revenue * 100`. Inputs: net_income=391609000 USD (NetIncomeLoss), revenue=276768000 USD (RevenueFromContractWithCustomerIncludingAssessedTax).

Derived observation: Annual revenue changed -6.50% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=276768000 USD (RevenueFromContractWithCustomerIncludingAssessedTax), revenue=296014000 USD (RevenueFromContractWithCustomerIncludingAssessedTax).

Derived observation: Annual net income changed +35.63% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=391609000 USD (NetIncomeLoss), net_income=288743000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed -26.91% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=304483000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=416565000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Operating cash flow / net income was 0.78x for the year ended 2025-12-31. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=304483000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=391609000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 391,609,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | 381,361,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 304,483,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 276,768,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerIncludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S08] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S08] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 102,414,000 | USD | US GAAP / reported | NetIncomeLoss | [S08] |
| net_income_common | 99,852,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S08] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 99,702,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S08] [S09] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 79,306,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerIncludingAssessedTax | [S08] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S08] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S08] |
| stock_based_compensation | 3,951,000 | USD | US GAAP / reported | ShareBasedCompensation | [S08] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
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
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:28:35.964605+00:00.

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

Calculation gaps: Operating margin: compatible positive revenue and usable inputs are required. Free cash flow margin: compatible positive revenue and usable inputs are required. Stock compensation / revenue: compatible positive revenue and usable inputs are required. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-21 | 8-K | 0000700564-26-000036 | — | [S16] |
| 2026-09-16 | 4 | 0001592539-26-000002 | — | [S17] |
| 2026-09-16 | 3 | 0001592539-26-000001 | — | [S18] |
| 2026-09-08 | 4 | 0002035688-26-000003 | — | [S19] |
| 2026-09-03 | 4 | 0002086746-26-000003 | — | [S20] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:11.183681+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000700564.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000700564.json) — published not supplied; retrieved 2026-10-22T18:10:35.452616+00:00.

[S04] [10-K 0000700564-26-000006](https://www.sec.gov/Archives/edgar/data/700564/000070056426000006/0000700564-26-000006-index.html) — published 2026-02-27; retrieved 2026-10-22T18:10:35.452616+00:00.

[S08] [10-Q 0000700564-26-000033](https://www.sec.gov/Archives/edgar/data/700564/000070056426000033/0000700564-26-000033-index.html) — published 2026-08-07; retrieved 2026-10-22T18:10:35.452616+00:00.

[S09] [10-Q 0000700564-26-000016](https://www.sec.gov/Archives/edgar/data/700564/000070056426000016/0000700564-26-000016-index.html) — published 2026-05-08; retrieved 2026-10-22T18:10:35.452616+00:00.

[S16] [8-K 0000700564-26-000036](https://www.sec.gov/Archives/edgar/data/700564/000070056426000036/0000700564-26-000036-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S17] [4 0001592539-26-000002](https://www.sec.gov/Archives/edgar/data/700564/000159253926000002/0001592539-26-000002-index.html) — published 2026-09-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [3 0001592539-26-000001](https://www.sec.gov/Archives/edgar/data/700564/000159253926000001/0001592539-26-000001-index.html) — published 2026-09-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0002035688-26-000003](https://www.sec.gov/Archives/edgar/data/700564/000203568826000003/0002035688-26-000003-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0002086746-26-000003](https://www.sec.gov/Archives/edgar/data/700564/000208674626000003/0002086746-26-000003-index.html) — published 2026-09-03; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/FULT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
