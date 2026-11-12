---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000046129
cik: 0000046129
company_name: ALLIENT INC
tickers:
- ALNT
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 131b0b6ed0d2bea3ed29b4a8ed7a56210d933ab8
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-K/A
  - 10-KT
  - 10-Q
  - 10-Q/A
  - '144'
  - '3'
  - '4'
  - 4/A
  - '425'
  - '5'
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEFM14A
  - EFFECT
  - PRE 14A
  - PREM14A
  - S-3
  - S-3ASR
  - S-4
  - S-4/A
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000046129.json
    sha256: bb1cb61827ece7fe06d9be734b061b92aa136049e8234d5d7ee4d4e9dddf4eeb
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0000046129.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000046129.json
    sha256: 649c15be3772a6da018b03948a27b4de88b6f5ec04ba748302daedf403ec7de5
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000046129.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-11-01T16:07:03.070084+00:00'
  sha256: b160a2f2814e5df68d7e414fba70f808f7ad3d20cbbdd167a8a2e38a10044168
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000046129.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 649c15be3772a6da018b03948a27b4de88b6f5ec04ba748302daedf403ec7de5
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000046129.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: bb1cb61827ece7fe06d9be734b061b92aa136049e8234d5d7ee4d4e9dddf4eeb
- id: S04
  title: 10-K 0001104659-26-024123
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465926024123/0001104659-26-024123-index.html
  published_at: '2026-03-05'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001104659-26-091098
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465926091098/0001104659-26-091098-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001104659-26-056256
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465926056256/0001104659-26-056256-index.html
  published_at: '2026-05-06'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S17
  title: 4 0001239944-26-000080
  url: https://www.sec.gov/Archives/edgar/data/46129/000123994426000080/0001239944-26-000080-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: SCHEDULE 13D/A 0001214659-26-010111
  url: https://www.sec.gov/Archives/edgar/data/46129/000121465926010111/0001214659-26-010111-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0001239944-26-000078
  url: https://www.sec.gov/Archives/edgar/data/46129/000123994426000078/0001239944-26-000078-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 144 0001959173-26-005856
  url: https://www.sec.gov/Archives/edgar/data/46129/000195917326005856/0001959173-26-005856-index.html
  published_at: '2026-08-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 4 0001239944-26-000074
  url: https://www.sec.gov/Archives/edgar/data/46129/000123994426000074/0001239944-26-000074-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S66
  title: 10-K 0001104659-26-024123
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465926024123/0001104659-26-024123-index.html
  published_at: '2026-03-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S67
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465926091098/alnt-20260630x10q.htm
  title: 10-Q 0001104659-26-091098
  published_at: '2026-08-05'
  retrieved_at: '2026-11-10T20:12:25.185529+00:00'
  sha256: 7336da8e04a022f0aa526b6d70c79ec6233f771d0918e7d4a5e81de8291b6f58
- id: S69
  url: https://www.sec.gov/Archives/edgar/data/46129/000114036126011362/ny20061041x1_def14a.htm
  title: DEF 14A 0001140361-26-011362
  published_at: '2026-03-26'
  retrieved_at: '2026-11-10T20:12:21.442797+00:00'
  sha256: 794a74dc4550be5ddcb4a5f200025b70eb6125b38659e69ca03eb9e694a528aa
- id: S70
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465926024123/alnt-20251231x10k.htm
  title: 10-K 0001104659-26-024123
  published_at: '2026-03-05'
  retrieved_at: '2026-11-10T20:12:19.499836+00:00'
  sha256: 7982051c6c5c066e4fdbc5fdad51bb08ee82159210c5b4ccdc4f4845c55dfba0
issuer_classification:
  cik: 0000046129
  classification_status: reported_sic
  entity_type: operating
  name: ALLIENT INC
  sic: '3825'
  sic_description: Instruments For Meas & Testing of  Electricity & Elec Signals
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 649c15be3772a6da018b03948a27b4de88b6f5ec04ba748302daedf403ec7de5
  url: https://data.sec.gov/submissions/CIK0000046129.json
listings:
- ticker: ALNT
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-024123
  filed: '2026-03-05'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465926024123/0001104659-26-024123-index.html
- accession: 0001104659-26-091098
  filed: '2026-08-05'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465926091098/0001104659-26-091098-index.html
- accession: 0001140361-26-011362
  filed: '2026-03-26'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/46129/000114036126011362/0001140361-26-011362-index.html
- accession: 0001104659-26-058659
  filed: '2026-05-11'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465926058659/0001104659-26-058659-index.html
- accession: 0001104659-19-008955
  filed: '2019-02-15'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465919008955/0001104659-19-008955-index.html
- accession: 0001104659-14-000389
  filed: '2014-01-03'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465914000389/0001104659-14-000389-index.html
- accession: 0001104659-11-021938
  filed: '2011-04-22'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465911021938/0001104659-11-021938-index.html
- accession: 0001104659-07-060156
  filed: '2007-08-08'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/46129/000110465907060156/0001104659-07-060156-index.html
- accession: 0001047469-03-018774
  filed: '2003-05-15'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/46129/000104746903018774/0001047469-03-018774-index.html
research_progress:
  stage: evidence_collected
  input_sha256: f80accb0cf7c424ef92ec58d4e53fce53b9da9d0bff710634d25699cf5934836
  last_attempt_at: '2026-11-10T20:10:56.246440+00:00'
  last_success_at: '2026-11-10T20:10:56.246440+00:00'
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
  derived_observations: 7
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '3825'
  sic_description: Instruments For Meas & Testing of  Electricity & Elec Signals
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000046129.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/bba0a6d83003768658985dd56dce0e9f590a48b8/brain/companies/ALNT/README.md
full_history_commit: bba0a6d83003768658985dd56dce0e9f590a48b8
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ALNT — ALLIENT INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/bba0a6d83003768658985dd56dce0e9f590a48b8/brain/companies/ALNT/README.md)

## Business overview

Reported issuer name: **ALLIENT INC**. Stable SEC CIK: **0000046129**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ALNT | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-08-05, L8888:

> Throughout 2025 and through the first two quarters of 2026, we continue to refine our strategy to expand our vertical market focus to accelerate our growth. Throughout its history, the Company has expanded our capabilities to be a leading global provider of motion solutions. More recently, we have been building our controls and power technologies, both organically and through acquisitions. The evolution of these additional pillars of our business enhances our overall value proposition, expands our addressable markets and is aligned with mega technology trends. These advancements required us to refine our strategy to leverage the value opportunity that exists in three technology pillars – Motion, Controls, and Power. [S67]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-08-05, L3839:

> The Company disaggregates revenue from contracts with customers into geographical regions and target markets. The Company determines that disaggregating revenue into these categories achieves the disclosure objective to depict how the nature, amount, timing, and uncertainty of revenue and cash flows are affected by economic factors. As noted below in Note 17, Segment Information, the Company’s business consists of one reportable segment. Revenue by geographic region is based on point of shipment origin. [S67]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-Q, filed 2026-08-05, L8885:

> We are a global company that is engaged in the business of designing, manufacturing, and selling precision motion, control, power, and structural composites to provide integrated system solutions as well as individual products, to a broad spectrum of customers throughout the world primarily for the industrial, vehicle, medical, and aerospace and defense markets. We are headquartered in Williamsville, NY, and have operations in the United States, Canada, Mexico, Europe, and Asia-Pacific. We are known worldwide for our expertise in electro-magnetic, mechanical, and electronic motion technology. We sell component and integrated controlled motion solutions to end customers and OEMs through our own direct sales force and authorized manufacturers’ representatives and distributors. Our products include nano precision positioning systems, servo control systems, motion controllers, digital servo amplifiers and drives, brushless servo, torque, and coreless motors, brush motors, integrated motor-drives, gear motors, gearing, incremental and absolute optical encoders, active (electronic) and passive (magnetic) filters for power quality and harmonic issues, Industrial safety rated input/output Modules, Universal Industrial Communications Gateways, light-weighting technologies, transformers, and other controlled motion-related products. [S67]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — DEF 14A, filed 2026-03-26, L897:

> been committed to responsible and sustainable business practices that considered the best interest of our customers, employees, suppliers, communities, and other stakeholders. [S69]

## Industry and value chain

SEC-reported SIC **3825**: Instruments For Meas & Testing of  Electricity & Elec Signals. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 10-Q, filed 2026-08-05, L8897:

> The current geopolitical conflicts are creating higher levels of economic uncertainty and increased volatility with respect to energy prices, interest rates, our supply chain (in particular, with respect to changes and proposed changes to tariffs and trade policies), and certain customer ordering patterns. We are closely monitoring the developments and continue to adjust our production platform to react to changing customer ordering patterns. The impact of the conflicts on our operational and financial performance will depend on future developments that cannot be predicted. [S67]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-K, filed 2026-03-05, L378:

> Our products and solutions are sold into the global market with a large and diverse group of competitors that vary by product, geography, industry and application. The controlled motion market is highly fragmented with many competitors, some of which are substantially larger and have greater resources than Allient. We believe our competitive advantages include our electro-magnetic, mechanical and electronic controlled motion expertise, the breadth of our motor technologies and our ability to integrate these technologies with our encoders, gearing, power electronics, digital control technologies and network/feedback communications capabilities, as well as our global presence. Unlike many of our competitors, we are unique in our ability to provide custom-engineered controlled motion solutions that integrate the products we manufacture such as embedded or external electrical control solutions with our motors. We compete on [S70]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-K, filed 2026-03-05, L321:

> All statements contained herein that are not statements of historical fact constitute “forward-looking statements” within the meaning of the Private Securities Litigation Reform Act of 1995. Forward-looking statements include, without limitation, any statement that may predict, forecast, indicate, or imply future results, performance, or achievements, and may contain the word “believe,” “anticipate,” “expect,” “project,” “intend,” “will continue,” “will likely result,” “should” or words or phrases of similar meaning. Forward-looking statements involve known and unknown risks and uncertainties that may cause actual results to differ materially from the expected results described in the forward-looking statements. The risks and uncertainties include those associated with: the domestic and foreign general business and economic conditions in the markets we serve, including political and currency risks and adverse changes in local legal and regulatory environments; the severity, magnitude and duration of weather, natural disaster, or pandemic-related events, including impacts of businesses’ and governments’ responses to such events on our operations and personnel, and on commercial activity and demand across our and our customers’ businesses, and on global supply chains; the ability to protect the Company’s intellectual property; our ability to sustain, manage or forecast our … [S70]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-Q, filed 2026-08-05, L8888:

> Throughout 2025 and through the first two quarters of 2026, we continue to refine our strategy to expand our vertical market focus to accelerate our growth. Throughout its history, the Company has expanded our capabilities to be a leading global provider of motion solutions. More recently, we have been building our controls and power technologies, both organically and through acquisitions. The evolution of these additional pillars of our business enhances our overall value proposition, expands our addressable markets and is aligned with mega technology trends. These advancements required us to refine our strategy to leverage the value opportunity that exists in three technology pillars – Motion, Controls, and Power. [S67]

## Financial performance

Derived observation: Operating margin was 7.93% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S66]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=43985000 USD (OperatingIncomeLoss), revenue=554478000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Free cash flow margin was 8.96% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S66]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=49686000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=554478000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Stock compensation / revenue was 0.62% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S66]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=3430000 USD (ShareBasedCompensation), revenue=554478000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual revenue changed +4.62% from the year ended 2024-12-31 to 2025-12-31. [S66]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=554478000 USD (RevenueFromContractWithCustomerExcludingAssessedTax), revenue=529968000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual operating income changed +46.43% from the year ended 2024-12-31 to 2025-12-31. [S66]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=43985000 USD (OperatingIncomeLoss), operating_income=30038000 USD (OperatingIncomeLoss).

Derived observation: Annual operating cash flow changed +35.42% from the year ended 2024-12-31 to 2025-12-31. [S66]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=56675000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=41850000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed +54.46% from the year ended 2024-12-31 to 2025-12-31. [S66]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=49686000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=32167000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -6,989,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 372,769,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 49,686,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 181,709,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_common | 22,034,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | 22,034,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 56,675,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 43,985,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 554,478,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 3,430,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -4,902,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| cost_of_revenue | 100,178,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 9,052,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| gross_profit | 53,592,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_common | 10,391,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S05] |
| net_income_including_noncontrolling_interests | 10,391,000 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | 13,954,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | 15,610,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 153,770,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 997,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 40,705,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 42,088,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-08-05, L10263:

> Management uses Adjusted net income and Adjusted diluted earnings per share to assess the Company’s consolidated financial and operating performance. Adjusted net income and Adjusted diluted earnings per share are provided for informational purposes only and are not a measure of financial performance under GAAP. These measures help management make decisions that are expected to facilitate meeting current financial goals as well as achieving optimal financial performance. Adjusted net income provides management with a measure of financial performance of the Company based on operational factors as it removes the impact of certain non-routine items from the Company’s operating results. Adjusted diluted earnings per share provides management with an indication of how Adjusted net income would be reflected on a per share basis for comparison to the GAAP diluted earnings per share measure. Adjusted net income is a key metric used by senior management and the Company’s board of directors to review the consolidated financial performance of the business. This measure adjusts net income determined in accordance with GAAP to reflect changes in financial results associated with the highlighted expense and income items. [S67]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-08-05, L8883:

> New risk factors emerge from time to time, and it is not possible for management to predict all such risk factors, nor can it assess the impact of all such risk factors on its business or the extent to which any factor, or combination of factors, may cause actual results to differ materially from those contained in any forward-looking statements. The Company’s expectations, beliefs and projections are believed to have a reasonable basis; however, the Company makes no assurance that expectations, beliefs, or projections will be achieved. [S67]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:27:37.399508+00:00.

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

Calculation gaps: Net margin: compatible positive revenue and usable inputs are required. net_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-23 | 4 | 0001239944-26-000080 | — | [S17] |
| 2026-08-13 | SCHEDULE 13D/A | 0001214659-26-010111 | — | [S18] |
| 2026-08-12 | 4 | 0001239944-26-000078 | — | [S19] |
| 2026-08-10 | 144 | 0001959173-26-005856 | — | [S20] |
| 2026-08-06 | 4 | 0001239944-26-000074 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000046129.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000046129.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001104659-26-024123](https://www.sec.gov/Archives/edgar/data/46129/000110465926024123/0001104659-26-024123-index.html) — published 2026-03-05; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [10-Q 0001104659-26-091098](https://www.sec.gov/Archives/edgar/data/46129/000110465926091098/0001104659-26-091098-index.html) — published 2026-08-05; retrieved 2026-10-22T17:39:41.848518+00:00.

[S09] [10-Q 0001104659-26-056256](https://www.sec.gov/Archives/edgar/data/46129/000110465926056256/0001104659-26-056256-index.html) — published 2026-05-06; retrieved 2026-10-22T17:39:41.848518+00:00.

[S17] [4 0001239944-26-000080](https://www.sec.gov/Archives/edgar/data/46129/000123994426000080/0001239944-26-000080-index.html) — published 2026-09-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [SCHEDULE 13D/A 0001214659-26-010111](https://www.sec.gov/Archives/edgar/data/46129/000121465926010111/0001214659-26-010111-index.html) — published 2026-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0001239944-26-000078](https://www.sec.gov/Archives/edgar/data/46129/000123994426000078/0001239944-26-000078-index.html) — published 2026-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [144 0001959173-26-005856](https://www.sec.gov/Archives/edgar/data/46129/000195917326005856/0001959173-26-005856-index.html) — published 2026-08-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [4 0001239944-26-000074](https://www.sec.gov/Archives/edgar/data/46129/000123994426000074/0001239944-26-000074-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S66] [10-K 0001104659-26-024123](https://www.sec.gov/Archives/edgar/data/46129/000110465926024123/0001104659-26-024123-index.html) — published 2026-03-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S67] [10-Q 0001104659-26-091098](https://www.sec.gov/Archives/edgar/data/46129/000110465926091098/alnt-20260630x10q.htm) — published 2026-08-05; retrieved 2026-11-10T20:12:25.185529+00:00.

[S69] [DEF 14A 0001140361-26-011362](https://www.sec.gov/Archives/edgar/data/46129/000114036126011362/ny20061041x1_def14a.htm) — published 2026-03-26; retrieved 2026-11-10T20:12:21.442797+00:00.

[S70] [10-K 0001104659-26-024123](https://www.sec.gov/Archives/edgar/data/46129/000110465926024123/alnt-20251231x10k.htm) — published 2026-03-05; retrieved 2026-11-10T20:12:19.499836+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/bba0a6d83003768658985dd56dce0e9f590a48b8/brain/companies/ALNT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
