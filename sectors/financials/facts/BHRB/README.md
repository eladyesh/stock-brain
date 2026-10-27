---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001964333
cik: 0001964333
company_name: Burke & Herbert Financial Services Corp.
tickers:
- BHRB
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 77264ce478c0c699392c0a049f464d4fda44c9f8
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-12B
  - 10-12B/A
  - 10-K
  - 10-K/A
  - 10-Q
  - '144'
  - '3'
  - 3/A
  - 305B2
  - '4'
  - 4/A
  - 424B3
  - 424B5
  - '425'
  - '5'
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - FWP
  - PRE 14A
  - S-3
  - S-3/A
  - S-4
  - S-4/A
  - S-4MEF
  - S-8
  - SC 13G
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SEC STAFF ACTION
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001964333.json
    sha256: 53517290e1189cc208333925980ad3851652440eb9b591d61db48a54fdf57dea
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0001964333.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001964333.json
    sha256: d9fabaedaca0e99b40e86b73f2748d14456492c29da9d49c10c1a0bbb3a9a659
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001964333.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-27T15:25:33.739265+00:00'
  sha256: 29c7cedde394d9fb806c731f8be32ec8c78cad2668852342db80ae28619465f0
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001964333.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d9fabaedaca0e99b40e86b73f2748d14456492c29da9d49c10c1a0bbb3a9a659
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001964333.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 53517290e1189cc208333925980ad3851652440eb9b591d61db48a54fdf57dea
- id: S04
  title: 10-K 0001964333-26-000016
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000016/0001964333-26-000016-index.html
  published_at: '2026-02-27'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001964333-26-000095
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000095/0001964333-26-000095-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S07
  title: 10-Q 0001964333-26-000068
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000068/0001964333-26-000068-index.html
  published_at: '2026-05-08'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S15
  title: 8-K/A 0001964333-26-000104
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000104/0001964333-26-000104-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S16
  title: 8-K 0001964333-26-000102
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000102/0001964333-26-000102-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S17
  title: 8-K 0001104659-26-112339
  url: https://www.sec.gov/Archives/edgar/data/1964333/000110465926112339/0001104659-26-112339-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S18
  title: 424B5 0001104659-26-112079
  url: https://www.sec.gov/Archives/edgar/data/1964333/000110465926112079/0001104659-26-112079-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S19
  title: 4 0002065589-26-000012
  url: https://www.sec.gov/Archives/edgar/data/1964333/000206558926000012/0002065589-26-000012-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S65
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000104/bhrb-20260618.htm
  title: 8-K/A 0001964333-26-000104
  published_at: '2026-10-23'
  retrieved_at: '2026-10-25T13:58:14.374687+00:00'
  sha256: a20b096bd23be04c237c41b4beffae3a14bee3700e45d1edb946f3c0d1dd4200
- id: S67
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000095/bhrb-20260630.htm
  title: 10-Q 0001964333-26-000095
  published_at: '2026-08-07'
  retrieved_at: '2026-10-25T13:58:10.912726+00:00'
  sha256: 4c0055bc3ed20b4be1dcc68919da9ce4699bed91750c4de40c7e99388dd280c8
- id: S70
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000016/bhrb-20251231.htm
  title: 10-K 0001964333-26-000016
  published_at: '2026-02-27'
  retrieved_at: '2026-10-25T13:58:05.601919+00:00'
  sha256: 72022526a0bf14f695d5b962d0c4576272f88e6845765426ba4d7be3dda23d52
issuer_classification:
  cik: 0001964333
  classification_status: reported_sic
  entity_type: operating
  name: Burke & Herbert Financial Services Corp.
  sic: '6021'
  sic_description: National Commercial Banks
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d9fabaedaca0e99b40e86b73f2748d14456492c29da9d49c10c1a0bbb3a9a659
  url: https://data.sec.gov/submissions/CIK0001964333.json
listings:
- ticker: BHRB
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001964333-26-000016
  filed: '2026-02-27'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000016/0001964333-26-000016-index.html
- accession: 0001964333-26-000095
  filed: '2026-08-07'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000095/0001964333-26-000095-index.html
- accession: 0001964333-26-000052
  filed: '2026-04-30'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000052/0001964333-26-000052-index.html
- accession: 0001964333-26-000102
  filed: '2026-10-22'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000102/0001964333-26-000102-index.html
- accession: 0001964333-26-000104
  filed: '2026-10-23'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000104/0001964333-26-000104-index.html
- accession: 0001964333-26-000084
  filed: '2026-07-17'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433326000084/0001964333-26-000084-index.html
- accession: 0001964333-25-000048
  filed: '2025-01-30'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433325000048/0001964333-25-000048-index.html
- accession: 0001964333-24-000294
  filed: '2024-07-11'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433324000294/0001964333-24-000294-index.html
- accession: 0001964333-24-000292
  filed: '2024-07-10'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433324000292/0001964333-24-000292-index.html
- accession: 0001964333-24-000216
  filed: '2024-05-09'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1964333/000196433324000216/0001964333-24-000216-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 6fb608b479fad7648f093142da2fd3ca454b0054b7d72e3936ce74ec2d1e9c9c
  last_attempt_at: '2026-10-25T13:56:40.792803+00:00'
  last_success_at: '2026-10-25T13:56:40.792803+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - competitive-landscape
  - customers-and-end-markets
  - growth-drivers
  - industry-and-value-chain
  - management-and-governance
  - moat-and-differentiation
  - products-and-services
  - recent-developments
  - revenue-model-and-segments
  - risks-and-thesis-breakers
  derived_observations: 4
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
  source_url: https://data.sec.gov/submissions/CIK0001964333.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/BHRB/README.md
full_history_commit: f974cdc6ffee05a6e0489d88d3e13c8eebf0b613
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BHRB — Burke & Herbert Financial Services Corp.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/BHRB/README.md)

## Business overview

Reported issuer name: **Burke & Herbert Financial Services Corp.**. Stable SEC CIK: **0001964333**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BHRB | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-08-07, L1731:

> competition; changes in consumer confidence and demand for financial services, including changes in consumer borrowing, repayment, investment, and deposit practices; changes in asset quality and credit risk; our ability to control costs and expenses; adverse developments in borrower industries or declines in real estate values; changes in and compliance with federal and state laws and regulations that pertain to our business and capital levels; our ability to raise capital as needed; the impact, extent and timing of technological changes; the effects of any cybersecurity breaches or events; the development and use of artificial intelligence (“AI”) in business processes, services, and products, including emerging external focus among regulators and other officials related to risks in connection with the development and use of AI; the potential adverse effects of unusual and infrequently occurring events, such as weather-related disasters, terrorist acts, geopolitical conflicts and tensions, or public health events (such as pandemics), and of governmental and societal responses thereto; and the other factors discussed in the “Risk Factors” and “Management's Discussion and Analysis of Financial Condition and Results of Operations” section of the Company's Annual Report on Form 10–K for the year ended December 31, 2025 and in Part I, Item 2. Management’s Discussion and Analysis of … [S67]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-08-07, L1721:

> The Company operates in one reportable segment, Community Banking. The Company's Chief Executive Officer has been identified as the chief operating decision maker (“CODM”). The CODM uses consolidated net income to evaluate the Company's overall operating performance and to allocate capital and other resources. While the CODM reviews information regarding the Company's products, services, revenue streams, and other operating activities, these activities are managed and evaluated on a consolidated basis. Information regarding individual business activities is reviewed for operational management purposes and not for the purpose of allocating resources among separate operating segments. Accordingly, the Company has concluded that it operates in a single reportable segment. [S67]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-K, filed 2026-02-27, L249:

> We continually review our product offerings, and based on these reviews, may selectively add additional products to provide further diversification of our revenue sources and to capture our customers’ full banking relationships. We believe that the following business strengths have been instrumental to the success of our core operations and will enable us to continue profitable growth and to maximize value to our shareholders, while remaining fundamentally sound. [S70]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-Q, filed 2026-08-07, L1878:

> •The effect of climate change on our business and performance, including indirectly through impacts on our customers; [S67]

## Industry and value chain

SEC-reported SIC **6021**: National Commercial Banks. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 10-Q, filed 2026-08-07, L1870:

> •Economic conditions, and volatility in markets, including the effects of pandemics, wars, political conflicts, political instability and uncertainty both in the U.S. and abroad, government spending policies, trade policies, including tariffs and tariff counter-measures, and other barriers to trade (including the threat of such actions), the availability of labor, supply chain volatility, and any actions taken to mitigate and manage such impacts; [S67]

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-Q, filed 2026-08-07, L1731:

> competition; changes in consumer confidence and demand for financial services, including changes in consumer borrowing, repayment, investment, and deposit practices; changes in asset quality and credit risk; our ability to control costs and expenses; adverse developments in borrower industries or declines in real estate values; changes in and compliance with federal and state laws and regulations that pertain to our business and capital levels; our ability to raise capital as needed; the impact, extent and timing of technological changes; the effects of any cybersecurity breaches or events; the development and use of artificial intelligence (“AI”) in business processes, services, and products, including emerging external focus among regulators and other officials related to risks in connection with the development and use of AI; the potential adverse effects of unusual and infrequently occurring events, such as weather-related disasters, terrorist acts, geopolitical conflicts and tensions, or public health events (such as pandemics), and of governmental and societal responses thereto; and the other factors discussed in the “Risk Factors” and “Management's Discussion and Analysis of Financial Condition and Results of Operations” section of the Company's Annual Report on Form 10–K for the year ended December 31, 2025 and in Part I, Item 2. Management’s Discussion and Analysis of … [S67]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-K, filed 2026-02-27, L304:

> We consider our employee base and our culture to be a competitive advantage. The variety in our employees’ backgrounds and experiences provides us the opportunity to serve our customers, communities, and each other in meaningful and impactful ways that result in long lasting relationships. Our overall human capital strategy focuses on attracting, engaging, and retaining qualified and innovative talent at all levels of the Company. We are a committed equal opportunity employer. We are also committed to maintaining a workforce committed to our core values to serve & lead, deliver more, elevate everyone, and always being invested in the long-term success of our customers, colleagues, and communities. [S70]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-Q, filed 2026-08-07, L1860:

> •Our ability to manage any material costs related to the execution of our strategic priorities, including increased employees, infrastructure, compliance, and other costs in a profitable manner over the long term, [S67]

## Financial performance

Derived observation: Annual net income changed +228.51% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=117306000 USD (NetIncomeLoss), net_income=35708000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +25.80% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=107933000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=85799000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed +18.46% from the year ended 2024-12-31 to 2025-12-31. [S04]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=96228000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=81232000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 0.92x for the year ended 2025-12-31. Working capital and non-cash adjustments require separate filing analysis. [S04]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=107933000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=117306000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -11,705,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 96,228,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 117,306,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | 116,406,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 107,933,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 4,777,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -2,191,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S07] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | -1,878,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S07] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 9,482,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | 9,257,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S05] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 313,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S07] |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 3,090,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S07] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

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
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | 450,000,000 | USD | US GAAP / reported | ShortTermBorrowings | [S05] |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | 525,000,000 | USD | US GAAP / reported | ShortTermBorrowings | [S05] |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 8-K/A, filed 2026-10-23, L76:

> This Current Report on Form 8-K/A (this “Amendment”) amends the Current Report on Form 8-K filed by Burke & Herbert Financial Services Corp. (the “Company”) with the U.S. Securities and Exchange Commission on June 18, 2026 (the “Original Form 8-K”). The Original Form 8-K was filed to report the results of the Company’s 2026 Annual Meeting of Shareholders held on June 18, 2026 (the “Annual Meeting”). The sole purpose of this Amendment is to disclose, in accordance with Item 5.07(d) of Form 8-K, the Company’s decision as to the frequency of future shareholder advisory votes regarding the compensation of the Company’s named executive officers. Except as set forth herein, no other changes have been made to the Original Form 8-K. [S65]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-08-07, L631:

> •Commercial real estate loans carry risk associated with either the net operating income generated from the lease of the real estate collateral or income generated from the sale of the collateral. Other risk factors include the credit-worthiness of the sponsor and the value of the collateral. [S67]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:36:27.526341+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (source excerpts available; assess the claim): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (source excerpts available; assess the claim): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (source excerpts available; assess the claim): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (source excerpts available; assess the claim): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
- **Growth drivers** (source excerpts available; assess the claim): Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.
- **Financial performance** (evidence or analysis still needed): Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.
- **Balance sheet and capital allocation** (evidence or analysis still needed): Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.
- **Management and governance** (source excerpts available; assess the claim): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
- **Valuation context** (evidence or analysis still needed): Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.
- **Catalysts** (evidence or analysis still needed): List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.
- **Risks and thesis breakers** (source excerpts available; assess the claim): Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.
- **Scenarios and open questions** (evidence or analysis still needed): Separate bull, base, and bear assumptions from facts. Record missing data, disputed evidence, and research questions without inventing answers.
- **Relationships and themes** (evidence or analysis still needed): Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.
- **Recent developments** (source excerpts available; assess the claim): Keep a dated, source-backed log of material changes. Distinguish the event date from the article date and explain what changed in the profile.

Calculation gaps: Operating margin: compatible positive revenue and usable inputs are required. Net margin: compatible positive revenue and usable inputs are required. Free cash flow margin: compatible positive revenue and usable inputs are required. Stock compensation / revenue: compatible positive revenue and usable inputs are required. revenue: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-23 | 8-K/A | 0001964333-26-000104 | — | [S15] |
| 2026-10-22 | 8-K | 0001964333-26-000102 | — | [S16] |
| 2026-09-30 | 8-K | 0001104659-26-112339 | — | [S17] |
| 2026-09-30 | 424B5 | 0001104659-26-112079 | — | [S18] |
| 2026-09-29 | 4 | 0002065589-26-000012 | — | [S19] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:33.739265+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001964333.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001964333.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001964333-26-000016](https://www.sec.gov/Archives/edgar/data/1964333/000196433326000016/0001964333-26-000016-index.html) — published 2026-02-27; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [10-Q 0001964333-26-000095](https://www.sec.gov/Archives/edgar/data/1964333/000196433326000095/0001964333-26-000095-index.html) — published 2026-08-07; retrieved 2026-10-22T17:39:41.848518+00:00.

[S07] [10-Q 0001964333-26-000068](https://www.sec.gov/Archives/edgar/data/1964333/000196433326000068/0001964333-26-000068-index.html) — published 2026-05-08; retrieved 2026-10-22T17:39:41.848518+00:00.

[S15] [8-K/A 0001964333-26-000104](https://www.sec.gov/Archives/edgar/data/1964333/000196433326000104/0001964333-26-000104-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S16] [8-K 0001964333-26-000102](https://www.sec.gov/Archives/edgar/data/1964333/000196433326000102/0001964333-26-000102-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S17] [8-K 0001104659-26-112339](https://www.sec.gov/Archives/edgar/data/1964333/000110465926112339/0001104659-26-112339-index.html) — published 2026-09-30; retrieved 2026-10-24T13:22:51.759433+00:00.

[S18] [424B5 0001104659-26-112079](https://www.sec.gov/Archives/edgar/data/1964333/000110465926112079/0001104659-26-112079-index.html) — published 2026-09-30; retrieved 2026-10-24T13:22:51.759433+00:00.

[S19] [4 0002065589-26-000012](https://www.sec.gov/Archives/edgar/data/1964333/000206558926000012/0002065589-26-000012-index.html) — published 2026-09-29; retrieved 2026-10-24T13:22:51.759433+00:00.

[S65] [8-K/A 0001964333-26-000104](https://www.sec.gov/Archives/edgar/data/1964333/000196433326000104/bhrb-20260618.htm) — published 2026-10-23; retrieved 2026-10-25T13:58:14.374687+00:00.

[S67] [10-Q 0001964333-26-000095](https://www.sec.gov/Archives/edgar/data/1964333/000196433326000095/bhrb-20260630.htm) — published 2026-08-07; retrieved 2026-10-25T13:58:10.912726+00:00.

[S70] [10-K 0001964333-26-000016](https://www.sec.gov/Archives/edgar/data/1964333/000196433326000016/bhrb-20251231.htm) — published 2026-02-27; retrieved 2026-10-25T13:58:05.601919+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/f974cdc6ffee05a6e0489d88d3e13c8eebf0b613/brain/companies/BHRB/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
