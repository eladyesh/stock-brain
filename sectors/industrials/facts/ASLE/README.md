---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001754170
cik: '0001754170'
company_name: AerSale Corp
tickers:
- ASLE
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 234e59eb75b5e3b9e02d4dd8de10d83fc60c027c
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
  - '144'
  - 25-NSE
  - 25-NSE/A
  - '3'
  - '4'
  - 4/A
  - 424B3
  - 424B4
  - 424B7
  - '425'
  - 8-A12B
  - 8-K
  - 8-K12B
  - ARS
  - CERT
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEL AM
  - DRS
  - EFFECT
  - POS AM
  - PRE 14A
  - PRER14A
  - S-1
  - S-1/A
  - S-3
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001754170.json
    sha256: aab4bf290a9a8c3f15beaf79588e69c3a26eb664ab6afa15d2cc03d68749f686
    retrieved_at: '2026-10-22T17:53:02.398600+00:00'
    archive:
      member: CIK0001754170.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001754170.json
    sha256: acc1153e2ebe8786cfb8e992e1e5f95a673e162382f77683ed939b89380839b1
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001754170.json
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
  url: https://data.sec.gov/submissions/CIK0001754170.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: acc1153e2ebe8786cfb8e992e1e5f95a673e162382f77683ed939b89380839b1
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001754170.json
  published_at: null
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: aab4bf290a9a8c3f15beaf79588e69c3a26eb664ab6afa15d2cc03d68749f686
- id: S04
  title: 10-K 0001104659-26-025574
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926025574/0001104659-26-025574-index.html
  published_at: '2026-03-10'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001104659-26-092710
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926092710/0001104659-26-092710-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001104659-26-057983
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926057983/0001104659-26-057983-index.html
  published_at: '2026-05-08'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S17
  title: 8-K 0001104659-26-111023
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926111023/0001104659-26-111023-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 4 0001104659-26-105051
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926105051/0001104659-26-105051-index.html
  published_at: '2026-09-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 144 0001959173-26-006598
  url: https://www.sec.gov/Archives/edgar/data/1754170/000195917326006598/0001959173-26-006598-index.html
  published_at: '2026-09-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0001104659-26-099748
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926099748/0001104659-26-099748-index.html
  published_at: '2026-08-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 4 0001104659-26-099747
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926099747/0001104659-26-099747-index.html
  published_at: '2026-08-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S64
  title: 10-K 0001104659-26-025574
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926025574/0001104659-26-025574-index.html
  published_at: '2026-03-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S68
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926092710/asle-20260630x10q.htm
  title: 10-Q 0001104659-26-092710
  published_at: '2026-08-07'
  retrieved_at: '2026-11-15T19:16:36.991791+00:00'
  sha256: e89166f11c54dbc98f961102291d4cd750130f2ba36d84f2eac85b16c2e9be3c
- id: S69
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926050451/asle-20260611xdef14a.htm
  title: DEF 14A 0001104659-26-050451
  published_at: '2026-04-28'
  retrieved_at: '2026-11-15T19:16:35.282245+00:00'
  sha256: c81efb490101c4bb5af8cb7b46e2a923b4183daa8b35207e37495531f36b35dd
- id: S70
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926025574/asle-20251231x10k.htm
  title: 10-K 0001104659-26-025574
  published_at: '2026-03-10'
  retrieved_at: '2026-11-15T19:16:33.404603+00:00'
  sha256: 243cecf9490de77801fcab8b991ca449bd541f30e52373ac3fe310020a6e0274
issuer_classification:
  cik: '0001754170'
  classification_status: reported_sic
  entity_type: operating
  name: AerSale Corp
  sic: '5080'
  sic_description: Wholesale-Machinery, Equipment & Supplies
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: acc1153e2ebe8786cfb8e992e1e5f95a673e162382f77683ed939b89380839b1
  url: https://data.sec.gov/submissions/CIK0001754170.json
listings:
- ticker: ASLE
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-025574
  filed: '2026-03-10'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926025574/0001104659-26-025574-index.html
- accession: 0001104659-26-092710
  filed: '2026-08-07'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926092710/0001104659-26-092710-index.html
- accession: 0001104659-26-050451
  filed: '2026-04-28'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926050451/0001104659-26-050451-index.html
- accession: 0001104659-26-111023
  filed: '2026-09-25'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1754170/000110465926111023/0001104659-26-111023-index.html
research_progress:
  stage: evidence_collected
  input_sha256: adad22adc5eee1cb46b145e4ff0e57ba82aa5656014d907e1a5f4255095b5f41
  last_attempt_at: '2026-11-15T19:14:21.222490+00:00'
  last_success_at: '2026-11-15T19:14:21.222490+00:00'
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
  derived_observations: 9
  model_draft: false
  reviewed: false
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '5080'
  sic_description: Wholesale-Machinery, Equipment & Supplies
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001754170.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ASLE/README.md
full_history_commit: 8c5afb0854b43beae818b88ec42b173c9411d269
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ASLE — AerSale Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ASLE/README.md)

## Business overview

Reported issuer name: **AerSale Corp**. Stable SEC CIK: **0001754170**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ASLE | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-08-07, L270:

> Moreover, we operate in an evolving environment. New risk factors and uncertainties may emerge from time to time, and it is not possible for management to predict all risk factors and uncertainties. [S68]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-08-07, L6575:

> The Chairman and Chief Executive Officer is our Chief Operating Decision Maker (“CODM”). We report operational data to our CODM at the segment level, which the CODM uses to evaluate performance and allocate resources based on gross profit and income (loss) from operations by segment. The CODM utilizes segment gross profit when making strategic decisions which include considerations of pursuing additional capacity and technical capabilities or acquiring additional Flight Equipment. Additionally, the CODM utilizes segment income (loss) from operations when comparing actual results to budgets and making decisions regarding personnel and capital allocations. While the Company believes there are synergies between the two business segments, they are managed separately because they have different risks and opportunities. The two reportable segments are: [S68]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-Q, filed 2026-08-07, L268:

> This Quarterly Report on Form 10-Q for the quarterly period ended June 30, 2026 (this “Quarterly Report”) contains forward-looking statements. We intend such forward-looking statements to be covered by the safe harbor provisions for forward-looking statements contained in Section 27A of the Securities Act of 1933, as amended (the “Securities Act”), and Section 21E of the Securities Exchange Act of 1934, as amended (the “Exchange Act”). All statements other than statements of historical facts contained in this Quarterly Report may constitute forward-looking statements, and may include, but are not limited to, changes in the market for our services; changes in applicable laws or regulations; the ability to launch new services and products or to profitably expand into new markets; the sufficiency of our liquidity; our recovery of insurance proceeds for casualty losses; and expectations of other economic, business and/or competitive factors. These statements involve known and unknown risks, uncertainties and other important factors that may cause our actual results, performance or achievements to be materially different from any future results, performance or achievements expressed or implied by the forward-looking statements. [S68]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-Q, filed 2026-08-07, L3552:

> For most service contracts, our performance obligations are satisfied over time as work progresses or at a point in time based on transfer of control of products and services to our customers. We receive payments from our customers based on billing schedules or other terms as written in our contracts. [S68]

## Industry and value chain

SEC-reported SIC **5080**: Wholesale-Machinery, Equipment & Supplies. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — DEF 14A, filed 2026-04-28, L620:

> Lt. General Fedder has served on our Board since July 2022. At the time of her retirement after nearly 35 years of active duty Air Force service, Lt. General Fedder served as Deputy Chief of Staff for Logistics, Installations and Mission Support, Headquarters U.S. Air Force, Washington, D.C. In that role, she was responsible to the Air Force Chief of Staff for leadership, management and integration of Air Force logistics readiness, aircraft, munitions, and missile maintenance, with emphasis on combat readiness and weapon system availability. Her portfolio also included setting policy and preparing budget estimates for Air Force civil engineering and security forces functions. Following her military career, Lt. General Fedder was a Senior Director at The Boeing Company for Global Sales and Marketing, Integrated Logistics, Boeing Defense. In that role, she secured capture of after-market services for military fighter and helicopter platforms and supply chain. She is currently a Senior Advisor at the Boston Consulting Group. [S69]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — DEF 14A, filed 2026-04-28, L3005:

> The Company’s compensation program generally consisting of base salary, annual performance based compensation and long term equity based primarily on performance with a retention element is within the median range consistent with competition in the industry. [S69]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-K, filed 2026-03-10, L368:

> \| \| ● \| lack of ownership of certain intellectual property and tooling that is important to our business; [S70]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — DEF 14A, filed 2026-04-28, L2462:

> Our recruitment programs involve partnerships with college programs, such as Embry-Riddle Aeronautical School, to provide internships and jobs. We are currently continuing to develop a scholarship program to focus on underrepresented graduates. Our program also includes summer internships for high school students who have demonstrated academic achievement and are pursuing careers in aviation and business. It is our intent to continue with these programs and partnerships in order to continue to expand our outreach. As we have expanded our workforce in our heavy MRO facilities we have partnered with a recruiting agency specialized in placing veterans in the civilian workforce. [S69]

## Financial performance

Derived observation: Operating margin was 4.71% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S64]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=15790000 USD (OperatingIncomeLoss), revenue=335286000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was 2.56% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S64]
Formula: `net_income / revenue * 100`. Inputs: net_income=8575000 USD (NetIncomeLoss), revenue=335286000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Free cash flow margin was -8.66% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S64]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=-29050000 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=335286000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Stock compensation / revenue was 1.46% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S64]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=4887000 USD (ShareBasedCompensation), revenue=335286000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual revenue changed -2.83% from the year ended 2024-12-31 to 2025-12-31. [S64]
Formula: `(current / prior - 1) * 100`. Inputs: revenue=335286000 USD (RevenueFromContractWithCustomerExcludingAssessedTax), revenue=345066000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Annual operating income changed +62.05% from the year ended 2024-12-31 to 2025-12-31. [S64]
Formula: `(current / prior - 1) * 100`. Inputs: operating_income=15790000 USD (OperatingIncomeLoss), operating_income=9744000 USD (OperatingIncomeLoss).

Derived observation: Annual net income changed +46.56% from the year ended 2024-12-31 to 2025-12-31. [S64]
Formula: `(current / prior - 1) * 100`. Inputs: net_income=8575000 USD (NetIncomeLoss), net_income=5851000 USD (NetIncomeLoss).

Derived observation: Annual operating cash flow changed -305.37% from the year ended 2024-12-31 to 2025-12-31. [S64]
Formula: `(current / prior - 1) * 100`. Inputs: operating_cash_flow=-22969000 USD (NetCashProvidedByUsedInOperatingActivities), operating_cash_flow=11184000 USD (NetCashProvidedByUsedInOperatingActivities).

Derived observation: Operating cash flow / net income was -2.68x for the year ended 2025-12-31. Working capital and non-cash adjustments require separate filing analysis. [S64]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=-22969000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=8575000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -6,081,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 229,512,000 | USD | US GAAP / reported | CostOfRevenue | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | -29,050,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 105,774,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | 8,575,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | 8,575,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | 8,575,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | -22,969,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 15,790,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 335,286,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 4,887,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -744,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| cost_of_revenue | 54,658,000 | USD | US GAAP / reported | CostOfRevenue | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | -7,558,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| gross_profit | 16,274,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | -5,570,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | -5,570,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_cash_flow | -6,814,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | -4,750,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 70,932,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 1,318,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 4,379,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 2,201,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review | [S05] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |



## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-08-07, L5940:

> The Company maintains a 2020 Equity Incentive Plan (the “2020 Plan”) and has 10,200,000 shares of common stock issuable under the 2020 Plan. The 2020 Plan authorizes discretionary grants of incentive stock options to employees of the Company and its qualifying subsidiaries. The 2020 Plan also authorizes discretionary grants of non-qualified stock options, stock appreciation rights, restricted stock, restricted stock units, dividend equivalents or other equity or cash-based awards to employees and consultants of the Company and its subsidiaries and to members of the Board of Directors (the [S68]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-08-07, L270:

> Moreover, we operate in an evolving environment. New risk factors and uncertainties may emerge from time to time, and it is not possible for management to predict all risk factors and uncertainties. [S68]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:35:26.187784+00:00.

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

Calculation gaps: free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-25 | 8-K | 0001104659-26-111023 | — | [S17] |
| 2026-09-03 | 4 | 0001104659-26-105051 | — | [S18] |
| 2026-09-01 | 144 | 0001959173-26-006598 | — | [S19] |
| 2026-08-21 | 4 | 0001104659-26-099748 | — | [S20] |
| 2026-08-21 | 4 | 0001104659-26-099747 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001754170.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001754170.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-K 0001104659-26-025574](https://www.sec.gov/Archives/edgar/data/1754170/000110465926025574/0001104659-26-025574-index.html) — published 2026-03-10; retrieved 2026-10-22T17:53:02.398600+00:00.

[S05] [10-Q 0001104659-26-092710](https://www.sec.gov/Archives/edgar/data/1754170/000110465926092710/0001104659-26-092710-index.html) — published 2026-08-07; retrieved 2026-10-22T17:53:02.398600+00:00.

[S09] [10-Q 0001104659-26-057983](https://www.sec.gov/Archives/edgar/data/1754170/000110465926057983/0001104659-26-057983-index.html) — published 2026-05-08; retrieved 2026-10-22T17:53:02.398600+00:00.

[S17] [8-K 0001104659-26-111023](https://www.sec.gov/Archives/edgar/data/1754170/000110465926111023/0001104659-26-111023-index.html) — published 2026-09-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [4 0001104659-26-105051](https://www.sec.gov/Archives/edgar/data/1754170/000110465926105051/0001104659-26-105051-index.html) — published 2026-09-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [144 0001959173-26-006598](https://www.sec.gov/Archives/edgar/data/1754170/000195917326006598/0001959173-26-006598-index.html) — published 2026-09-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0001104659-26-099748](https://www.sec.gov/Archives/edgar/data/1754170/000110465926099748/0001104659-26-099748-index.html) — published 2026-08-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [4 0001104659-26-099747](https://www.sec.gov/Archives/edgar/data/1754170/000110465926099747/0001104659-26-099747-index.html) — published 2026-08-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S64] [10-K 0001104659-26-025574](https://www.sec.gov/Archives/edgar/data/1754170/000110465926025574/0001104659-26-025574-index.html) — published 2026-03-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S68] [10-Q 0001104659-26-092710](https://www.sec.gov/Archives/edgar/data/1754170/000110465926092710/asle-20260630x10q.htm) — published 2026-08-07; retrieved 2026-11-15T19:16:36.991791+00:00.

[S69] [DEF 14A 0001104659-26-050451](https://www.sec.gov/Archives/edgar/data/1754170/000110465926050451/asle-20260611xdef14a.htm) — published 2026-04-28; retrieved 2026-11-15T19:16:35.282245+00:00.

[S70] [10-K 0001104659-26-025574](https://www.sec.gov/Archives/edgar/data/1754170/000110465926025574/asle-20251231x10k.htm) — published 2026-03-10; retrieved 2026-11-15T19:16:33.404603+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ASLE/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
