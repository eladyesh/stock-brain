---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000002098
cik: 0000002098
company_name: ACME UNITED CORP
tickers:
- ACU
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 0fe1bd4b14b27b36b782428a47500971a40bd2c5
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
  - '3'
  - '4'
  - 4/A
  - '5'
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - NT 10-K
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000002098.json
    sha256: 98dc453533c3f93333a2cb3954621e925c538e0cf6f624fbbdd5feeae975ed9c
    retrieved_at: '2026-10-22T17:53:02.398600+00:00'
    archive:
      member: CIK0000002098.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000002098.json
    sha256: 30b961dff0b00b998cbe53ceef41a5012ba6e285f5cda6e02fd6e0a7fd8454be
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000002098.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-11-01T16:07:03.340031+00:00'
  sha256: ee0a872edece98430f3ba5a1ed6e9c683d7a1bb4b2980bdc9743c6995f264398
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000002098.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 30b961dff0b00b998cbe53ceef41a5012ba6e285f5cda6e02fd6e0a7fd8454be
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000002098.json
  published_at: null
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: 98dc453533c3f93333a2cb3954621e925c538e0cf6f624fbbdd5feeae975ed9c
- id: S04
  title: 10-K 0001193125-26-102079
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526102079/0001193125-26-102079-index.html
  published_at: '2026-03-11'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001193125-26-338211
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526338211/0001193125-26-338211-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001193125-26-209010
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526209010/0001193125-26-209010-index.html
  published_at: '2026-05-06'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S17
  title: SCHEDULE 13G/A 0001420506-26-002359
  url: https://www.sec.gov/Archives/edgar/data/2098/000142050626002359/0001420506-26-002359-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 4 0001193125-26-428985
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526428985/0001193125-26-428985-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: S-8 0001193125-26-412443
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526412443/0001193125-26-412443-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001193125-26-356980
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526356980/0001193125-26-356980-index.html
  published_at: '2026-08-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 144 0001959173-26-006130
  url: https://www.sec.gov/Archives/edgar/data/2098/000195917326006130/0001959173-26-006130-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S53
  title: 10-K 0001193125-26-102079
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526102079/0001193125-26-102079-index.html
  published_at: '2026-03-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S67
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526338211/acu-20260630.htm
  title: 10-Q 0001193125-26-338211
  published_at: '2026-08-06'
  retrieved_at: '2026-11-05T20:29:44.727768+00:00'
  sha256: 58be62751eeded0a97302968c627fe229d7278f1e26d6fe327a7246878f024df
- id: S69
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526129439/d57325ddef14a.htm
  title: DEF 14A 0001193125-26-129439
  published_at: '2026-03-27'
  retrieved_at: '2026-11-05T20:29:40.475997+00:00'
  sha256: 0b1f76d114e44389106bf3175ca368daad4b3fbaf3806bf47b7eb5fa40373e96
- id: S70
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526102079/acu-20251231.htm
  title: 10-K 0001193125-26-102079
  published_at: '2026-03-11'
  retrieved_at: '2026-11-05T20:29:38.626679+00:00'
  sha256: f41109956331b81588997c4640e93e94df11e147a7091ec672e15c373f243ef0
issuer_classification:
  cik: 0000002098
  classification_status: reported_sic
  entity_type: operating
  name: ACME UNITED CORP
  sic: '3420'
  sic_description: Cutlery, Handtools & General Hardware
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 30b961dff0b00b998cbe53ceef41a5012ba6e285f5cda6e02fd6e0a7fd8454be
  url: https://data.sec.gov/submissions/CIK0000002098.json
listings:
- ticker: ACU
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-102079
  filed: '2026-03-11'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526102079/0001193125-26-102079-index.html
- accession: 0001193125-26-338211
  filed: '2026-08-06'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526338211/0001193125-26-338211-index.html
- accession: 0001193125-26-129439
  filed: '2026-03-27'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526129439/0001193125-26-129439-index.html
- accession: 0001193125-26-313374
  filed: '2026-07-23'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/2098/000119312526313374/0001193125-26-313374-index.html
- accession: 0000950170-24-085000
  filed: '2024-07-22'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/2098/000095017024085000/0000950170-24-085000-index.html
- accession: 0001026608-14-000066
  filed: '2014-08-19'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/2098/000102660814000066/0001026608-14-000066-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 91946900f4b54b8f9f220e9a11e4e4627040704adb674e4aeb066061ce07d658
  last_attempt_at: '2026-11-05T20:27:49.643469+00:00'
  last_success_at: '2026-11-05T20:27:49.643469+00:00'
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
  derived_observations: 10
  model_draft: false
  reviewed: false
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '3420'
  sic_description: Cutlery, Handtools & General Hardware
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000002098.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/fd10ac7383bb02748d9125b578ec1ede86e3a21b/brain/companies/ACU/README.md
full_history_commit: fd10ac7383bb02748d9125b578ec1ede86e3a21b
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ACU — ACME UNITED CORP

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/fd10ac7383bb02748d9125b578ec1ede86e3a21b/brain/companies/ACU/README.md)

## Business overview

Reported issuer name: **ACME UNITED CORP**. Stable SEC CIK: **0000002098**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ACU | NYSE_AMERICAN | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-08-06, L6072:

> We have been actively diversifying our supply base for many years and source products and components in a number of countries. A significant portion of the products we sell (and components used in our products) are sourced from suppliers located in China. The United States government has imposed, and may continue to impose or adjust, significant tariffs on a range of Chinese goods. These tariffs have increased our costs of goods sold and could further escalate depending on changes in trade policy, negotiations, or retaliatory measures by China or by other countries similarly impacted. The indirect impact on demand for our products as a result of these developments has become more uncertain. The Company has taken and continues to take steps to mitigate the potential impact on our business and operations through strategic sourcing adjustments, price adjustments and supply chain diversification, but such efforts have not been able to fully mitigate the effects of the imposition of tariffs and related developments. Any further increases of existing tariffs, the imposition of new tariffs, the potential modifications to existing trade agreements, new restrictions on free trade and the responses by other governments to changes in trade policy by the United States may further adversely impact demand for our products, increase our costs, and disrupt our supply chain. These risks, in … [S67]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-08-06, L4037:

> The Company’s reportable business segments consist of: (1) United States; (2) Canada; and (3) Europe. As described below, the activities of the Company’s Asian operations are closely linked to those of the U.S. operations; accordingly, the Company’s CODM reviews the financial results of both on a consolidated basis, and the results of the Asian operations have been aggregated with the results of the United States operations to form one reportable segment called the “United States segment” or “U.S. segment”. Each reportable segment derives its revenue from the sales of i) first aid and medical products and ii) cutting and sharpening tools to school, home, office, hardware, sporting and industrial markets. [S67]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-Q, filed 2026-08-06, L5953:

> These risks and uncertainties include, without limitation, the following: (i) changes in the Company’s plans, strategies, objectives, expectations and intentions, which may be made at any time at the discretion of the Company; (ii) the impact of volatility in global economic conditions, including the impact on the Company’s suppliers and customers; (iii) international trade policies of the United States or foreign governments and their impact on demand for our products and our competitive position, including the imposition of new tariffs, changes in existing tariff rates or the threat of any such action; (iv) the continuing adverse impact of inflation, including product costs, transportation costs and interest rates; (v) currency fluctuations; (vi) potential adverse effects on the Company, its customers, and suppliers resulting from the wars in Ukraine and the Middle East; (vii) additional disruptions in the Company’s supply chains, whether caused by pandemics, natural disasters, including trucker shortages, port closures, port strikes or otherwise; (viii) labor related costs the Company has and may continue to incur, including costs of acquiring and training new employees and rising wages and benefits; (ix) changes in client needs and consumer spending habits; (x) the Company’s ability to effectively manage its inventory in a rapidly changing business environment; (xi) the … [S67]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-Q, filed 2026-08-06, L3500:

> A performance obligation is a promise in a contract to transfer a distinct good or service to the customer. A contract’s transaction price is allocated to each distinct performance obligation and recognized as revenue when, or as, the performance obligation is satisfied. Revenue is generated by the sale of the Company’s products to its customers. Sales contracts (purchase orders) generally have a single performance obligation that is satisfied at a point in time, upon shipment or delivery, depending on the terms of the underlying contract. Revenue is measured based on the consideration specified in the contract. The amount of consideration we receive and revenue we recognize is impacted by incentives ("customer rebates"), including sales rebates, which are generally tied to sales volume levels, in-store promotional allowances, shared media and customer catalog allowances and other cooperative advertising arrangements; freight allowance programs offered to our customers; and allowance for returns and discounts. We generally recognize customer rebate costs as a deduction to gross sales at the time that the associated revenue is recognized. [S67]

## Industry and value chain

SEC-reported SIC **3420**: Cutlery, Handtools & General Hardware. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 10-Q, filed 2026-08-06, L6072:

> We have been actively diversifying our supply base for many years and source products and components in a number of countries. A significant portion of the products we sell (and components used in our products) are sourced from suppliers located in China. The United States government has imposed, and may continue to impose or adjust, significant tariffs on a range of Chinese goods. These tariffs have increased our costs of goods sold and could further escalate depending on changes in trade policy, negotiations, or retaliatory measures by China or by other countries similarly impacted. The indirect impact on demand for our products as a result of these developments has become more uncertain. The Company has taken and continues to take steps to mitigate the potential impact on our business and operations through strategic sourcing adjustments, price adjustments and supply chain diversification, but such efforts have not been able to fully mitigate the effects of the imposition of tariffs and related developments. Any further increases of existing tariffs, the imposition of new tariffs, the potential modifications to existing trade agreements, new restrictions on free trade and the responses by other governments to changes in trade policy by the United States may further adversely impact demand for our products, increase our costs, and disrupt our supply chain. These risks, in … [S67]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-Q, filed 2026-08-06, L5953:

> These risks and uncertainties include, without limitation, the following: (i) changes in the Company’s plans, strategies, objectives, expectations and intentions, which may be made at any time at the discretion of the Company; (ii) the impact of volatility in global economic conditions, including the impact on the Company’s suppliers and customers; (iii) international trade policies of the United States or foreign governments and their impact on demand for our products and our competitive position, including the imposition of new tariffs, changes in existing tariff rates or the threat of any such action; (iv) the continuing adverse impact of inflation, including product costs, transportation costs and interest rates; (v) currency fluctuations; (vi) potential adverse effects on the Company, its customers, and suppliers resulting from the wars in Ukraine and the Middle East; (vii) additional disruptions in the Company’s supply chains, whether caused by pandemics, natural disasters, including trucker shortages, port closures, port strikes or otherwise; (viii) labor related costs the Company has and may continue to incur, including costs of acquiring and training new employees and rising wages and benefits; (ix) changes in client needs and consumer spending habits; (x) the Company’s ability to effectively manage its inventory in a rapidly changing business environment; (xi) the … [S67]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-K, filed 2026-03-11, L370:

> The Company owns many patents and trademarks that are important to its business. The Company’s success depends in part on its ability to maintain patent protection for its products, to preserve its proprietary technology and to operate without infringing upon the patents or proprietary rights of others. The Company generally files patent applications in the United States and foreign countries where patent protection for its technology is appropriate and available. [S70]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-K, filed 2026-03-11, L361:

> We continue to expand our catalog of craft items with patented new technologies, handle designs and construction that has driven Westcott to be a leader in fashionable and functional solutions for students and adults. In addition, Westcott continues to build on its cutting line with an expanded assortment of ceramic safety knives which include new features, allowing its customers to remain safer on the job. [S70]

## Financial performance

Derived observation: Operating margin was 7.49% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S53]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=14724514 USD (OperatingIncomeLoss), revenue=196541816 USD (Revenues).

Derived observation: Net margin was 5.18% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S53]
Formula: `net_income / revenue * 100`. Inputs: net_income=10184421 USD (NetIncomeLoss), revenue=196541816 USD (Revenues).

Derived observation: Free cash flow margin was 3.86% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S53]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=7577536 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=196541816 USD (Revenues).

Derived observation: Stock compensation / revenue was 1.01% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S53]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=1993758 USD (ShareBasedCompensation), revenue=196541816 USD (Revenues).

Derived observation: Annual revenue changed +1.05% from the year ended 2024-12-31 to 2025-12-31. [S53]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=196541816 USD (Revenues), revenue=194489991 USD (Revenues).

Derived observation: Annual operating income changed +4.13% from the year ended 2024-12-31 to 2025-12-31. [S53]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=14724514 USD (OperatingIncomeLoss), operating_income=14139942 USD (OperatingIncomeLoss).

Derived observation: Annual net income changed +1.62% from the year ended 2024-12-31 to 2025-12-31. [S53]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=10184421 USD (NetIncomeLoss), net_income=10022351 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed +52.23% from the year ended 2024-12-31 to 2025-12-31. [S53]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=18229449 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=11975240 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Annual free cash flow changed +57.00% from the year ended 2024-12-31 to 2025-12-31. [S53]
Formula: `(current / prior - 1) * 100`. Inputs: free_cash_flow=7577536 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), free_cash_flow=4826592 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment).

Derived observation: Operating cash flow / net income was 1.79x for the year ended 2025-12-31. Working capital and non-cash adjustments require separate filing analysis. [S53]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=18229449 USD (NetCashProvidedByUsedInOperatingActivities), net_income=10184421 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -10,651,913 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 119,131,968 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | 7,577,536 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 77,409,848 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 10,184,421 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 18,229,449 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 14,724,514 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 196,541,816 | USD | US GAAP / reported | Revenues | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 1,993,758 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -1,068,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| cost_of_revenue | 36,028,000 | USD | US GAAP / reported | CostOfGoodsAndServicesSold | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 12,052,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| gross_profit | 26,688,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | 5,051,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 13,120,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | 6,830,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 62,716,000 | USD | US GAAP / reported | Revenues | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 370,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; revision_requires_review | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review, revision_requires_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 5,041,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — DEF 14A, filed 2026-03-27, L64:

> On behalf of your Board of Directors and Management, I cordially invite you to attend the 2026 Annual Meeting of Shareholders of Acme United Corporation scheduled to be held on Monday, April 27, 2026, at 11:00 A.M., Eastern Time. The Annual Meeting will be held as a “virtual meeting”, i.e., solely by means of remote communication via the Internet at www.virtualshareholdermeeting.com/ACU2026. Shareholders will be able to participate virtually, vote on matters submitted to the shareholders and submit questions during the Annual Meeting electronically. All shareholders will have the same rights and opportunities to participate in this virtual Annual Meeting as they would have at an in-person annual meeting. The Meeting will be held for the following purposes: [S69]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-08-06, L5954:

> For a more detailed discussion of these and other factors affecting the Company, see the Risk Factors described in Item 1A included in the Company’s Annual Report on Form 10-K for the fiscal year ended December 31, 2025 and below under “Financial Condition”. All forward-looking statements in this report are based upon information available to the Company on the date of this report. The Company undertakes no obligation to publicly update or revise any forward-looking statement, whether as a result of new information, future events, or otherwise, except as required by law. [S67]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:27:06.145584+00:00.

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

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-22 | SCHEDULE 13G/A | 0001420506-26-002359 | — | [S17] |
| 2026-10-22 | 4 | 0001193125-26-428985 | — | [S18] |
| 2026-10-02 | S-8 | 0001193125-26-412443 | — | [S19] |
| 2026-08-19 | 4 | 0001193125-26-356980 | — | [S20] |
| 2026-08-17 | 144 | 0001959173-26-006130 | — | [S21] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000002098.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000002098.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-K 0001193125-26-102079](https://www.sec.gov/Archives/edgar/data/2098/000119312526102079/0001193125-26-102079-index.html) — published 2026-03-11; retrieved 2026-10-22T17:53:02.398600+00:00.

[S05] [10-Q 0001193125-26-338211](https://www.sec.gov/Archives/edgar/data/2098/000119312526338211/0001193125-26-338211-index.html) — published 2026-08-06; retrieved 2026-10-22T17:53:02.398600+00:00.

[S09] [10-Q 0001193125-26-209010](https://www.sec.gov/Archives/edgar/data/2098/000119312526209010/0001193125-26-209010-index.html) — published 2026-05-06; retrieved 2026-10-22T17:53:02.398600+00:00.

[S17] [SCHEDULE 13G/A 0001420506-26-002359](https://www.sec.gov/Archives/edgar/data/2098/000142050626002359/0001420506-26-002359-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [4 0001193125-26-428985](https://www.sec.gov/Archives/edgar/data/2098/000119312526428985/0001193125-26-428985-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [S-8 0001193125-26-412443](https://www.sec.gov/Archives/edgar/data/2098/000119312526412443/0001193125-26-412443-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001193125-26-356980](https://www.sec.gov/Archives/edgar/data/2098/000119312526356980/0001193125-26-356980-index.html) — published 2026-08-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [144 0001959173-26-006130](https://www.sec.gov/Archives/edgar/data/2098/000195917326006130/0001959173-26-006130-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S53] [10-K 0001193125-26-102079](https://www.sec.gov/Archives/edgar/data/2098/000119312526102079/0001193125-26-102079-index.html) — published 2026-03-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S67] [10-Q 0001193125-26-338211](https://www.sec.gov/Archives/edgar/data/2098/000119312526338211/acu-20260630.htm) — published 2026-08-06; retrieved 2026-11-05T20:29:44.727768+00:00.

[S69] [DEF 14A 0001193125-26-129439](https://www.sec.gov/Archives/edgar/data/2098/000119312526129439/d57325ddef14a.htm) — published 2026-03-27; retrieved 2026-11-05T20:29:40.475997+00:00.

[S70] [10-K 0001193125-26-102079](https://www.sec.gov/Archives/edgar/data/2098/000119312526102079/acu-20251231.htm) — published 2026-03-11; retrieved 2026-11-05T20:29:38.626679+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/fd10ac7383bb02748d9125b578ec1ede86e3a21b/brain/companies/ACU/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
