---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001051627
cik: '0001051627'
company_name: AXT INC
tickers:
- AXTI
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: ddae9173dac59b8f117d07d566c062594b1014b4
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-K/A
  - 10-K405
  - 10-Q
  - 10-Q/A
  - '144'
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B5
  - '5'
  - 8-A12G
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - CT ORDER
  - DEF 14A
  - DEFA14A
  - DEFR14A
  - EFFECT
  - NT 10-K
  - NT 10-Q
  - POS AM
  - PRE 14A
  - S-3
  - S-3/A
  - S-3ASR
  - S-3MEF
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001051627.json
    sha256: 76220cf02b2c4e2067fa257d2096ea62192d03eae8641ef5a6dadf6ff5361216
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0001051627.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001051627.json
    sha256: 913137af69c34be4456837e1a8ba5436c76c79ab32e433b4d809817ff5b87101
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001051627.json
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
  url: https://data.sec.gov/submissions/CIK0001051627.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 913137af69c34be4456837e1a8ba5436c76c79ab32e433b4d809817ff5b87101
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001051627.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 76220cf02b2c4e2067fa257d2096ea62192d03eae8641ef5a6dadf6ff5361216
- id: S04
  title: 10-K 0001437749-26-008612
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774926008612/0001437749-26-008612-index.html
  published_at: '2026-03-17'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001437749-26-027677
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/0001437749-26-027677-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001437749-26-017054
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774926017054/0001437749-26-017054-index.html
  published_at: '2026-05-14'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S17
  title: SCHEDULE 13G/A 0002012383-26-003311
  url: https://www.sec.gov/Archives/edgar/data/1051627/000201238326003311/0002012383-26-003311-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 4 0001437749-26-028577
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774926028577/0001437749-26-028577-index.html
  published_at: '2026-08-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: 4 0001437749-26-028573
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774926028573/0001437749-26-028573-index.html
  published_at: '2026-08-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 144 0001965301-26-000127
  url: https://www.sec.gov/Archives/edgar/data/1051627/000196530126000127/0001965301-26-000127-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 10-Q 0001437749-26-027677
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/0001437749-26-027677-index.html
  published_at: '2026-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S67
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/axti20260630_10q.htm
  title: 10-Q 0001437749-26-027677
  published_at: '2026-08-13'
  retrieved_at: '2026-11-18T21:05:41.056030+00:00'
  sha256: da20d5227ecbfe0d5e732c9a038b3e9192a80d18f5ecd7915bf1edf3329d2b33
issuer_classification:
  cik: '0001051627'
  classification_status: reported_sic
  entity_type: operating
  name: AXT INC
  sic: '3674'
  sic_description: Semiconductors & Related Devices
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 913137af69c34be4456837e1a8ba5436c76c79ab32e433b4d809817ff5b87101
  url: https://data.sec.gov/submissions/CIK0001051627.json
listings:
- ticker: AXTI
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001437749-26-008612
  filed: '2026-03-17'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774926008612/0001437749-26-008612-index.html
- accession: 0001437749-26-027677
  filed: '2026-08-13'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/0001437749-26-027677-index.html
- accession: 0001437749-26-010661
  filed: '2026-03-31'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774926010661/0001437749-26-010661-index.html
- accession: 0001437749-26-025061
  filed: '2026-07-30'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774926025061/0001437749-26-025061-index.html
- accession: 0001437749-25-023431
  filed: '2025-07-24'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1051627/000143774925023431/0001437749-25-023431-index.html
- accession: 0001558370-22-013815
  filed: '2022-08-19'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1051627/000155837022013815/0001558370-22-013815-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 9af34b6d3fa8d0518b3d7d21ed88171b216ecf2d39f560401cf8f14983446a01
  last_attempt_at: '2026-11-18T21:00:27.361756+00:00'
  last_success_at: '2026-11-18T21:00:27.361756+00:00'
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
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '3674'
  sic_description: Semiconductors & Related Devices
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001051627.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AXTI/README.md
full_history_commit: b9d67ef2f16565081e0df464efbaff4348778881
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AXTI — AXT INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AXTI/README.md)

## Business overview

Reported issuer name: **AXT INC**. Stable SEC CIK: **0001051627**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AXTI | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-08-13, L1406:

> We operate in one segment for the design, development, manufacture and distribution of high-performance compound and single element semiconductor substrates and sale of raw materials integral to these substrates. In accordance with ASC Topic 280, Segment Reporting, our chief operating decision‑maker (“CODM”) has been identified as the Chief Executive Officer, who reviews operating results to make decisions about allocating resources and assessing performance for the Company. Since we operate in one segment, all financial segment and product line information can be found in the consolidated financial statements. The CODM regularly evaluates consolidated net income (loss) and functional expenses, including cost of revenue, selling, general and administrative and research and development, to manage Company operations. No additional disaggregated expense categories are presented beyond those already disclosed in the primary financial statements. [S67]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-Q, filed 2026-08-13, L1521:

> We provide warranties for our products for a specific period of time, generally twelve months, against material defects. We provide for the estimated future costs of warranty obligations in cost of sales when the related revenue is recognized. The accrued warranty costs represent the best estimate at the time of sale of the total costs that we expect to incur to repair or replace product parts that fail while still under warranty. The amount of accrued estimated warranty costs is primarily based on historical experience as to product failures as well as current information on repair costs. On a quarterly basis, we review the accrued balances and update the historical warranty cost trends. [S67]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-Q, filed 2026-08-13, L1514:

> We perform ongoing credit evaluations of our customers’ financial condition, and limit the amount of credit extended when deemed necessary, but generally do not require collateral. No customer accounted for more than 10% of our accounts receivable balance as of June 30, 2026 and one customer accounted for more than 10% of our accounts receivable balance December 31, 2025. [S67]

## Industry and value chain

SEC-reported SIC **3674**: Semiconductors & Related Devices. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 10-Q, filed 2026-08-13, L717:

> We have made strategic investments in private companies located in China in order to gain access at a competitive cost to raw materials that are critical to our substrate business (see Note 7). The investment balances for the non-consolidated companies are accounted for under the equity method, included in “Other assets” in the condensed consolidated balance sheets, totaled $14.1 million and $15.0 million as of June 30, 2026 and December 31, 2025, respectively. As of June 30, 2026, there were three companies accounted for under the equity method. There were no impairment charges for these investments during the three and six months ended June 30, 2026 and 2025. [S67]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-Q, filed 2026-08-13, L1798:

> Our forward-looking statements are based upon assumptions that are subject to uncertainties and factors relating to the Company’s operations and business environment, which could cause actual results to differ materially from those expressed or implied in the forward-looking statements contained in this Quarterly Report on Form 10-Q. These uncertainties and factors include, but are not limited to: the receipt of export permits to export indium phosphide wafers from China, as well as our other wafer products, and the timing of such export permit approvals, the withdrawal, cancellations or requests for redemptions by private equity funds in China of their investments in Tongmei, revenues from long-term supply agreements with customers, Tongmei's intended IPO application on the Hong Kong Stock Exchange, the administrative challenges in satisfying the requirements of various government agencies in China in connection with the investments in Tongmei and geopolitical tensions between China and the United States. Additional uncertainties and factors include, but are not limited to: the timing and receipt of significant orders; the cancellation of orders and return of product; emerging applications using chips or devices fabricated on our substrates; end-user acceptance of products containing chips or devices fabricated on our substrates; our ability to bring new products to market; … [S67]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-Q, filed 2026-08-13, L1562:

> We have established a wafer process production line in Dingxing, China. In addition to a land rights and building purchase agreement that we entered into with a private real estate development company to acquire our new manufacturing facility, we also entered into a cooperation agreement with the Dingxing local government. In addition to pledging its full support and cooperation, the Dingxing local government will issue certain credits or rebates to us as we achieve certain milestones. We, in turn, agreed to hire local workers over time, pay taxes when due and eventually demonstrate a total investment of approximately $90 million in value, assets and capital. The investment will include cash paid for the land and buildings, cash on deposit in our name at local banks, the gross value of new and used equipment (including future equipment that might be used for indium phosphide and germanium substrates production), the deemed value for our customer list or the end user of our substrates, for example, the end users of 3-D sensing VCSELs (vertical cavity surface emitting lasers), a deemed value for employment of local citizens, a deemed value for our proprietary process technology, other intellectual property, other intangibles and additional items of value. There is no timeline or deadline by which this must be accomplished, rather it is a good faith covenant entered into between … [S67]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-Q, filed 2026-08-13, L1797:

> This Quarterly Report on Form 10-Q of AXT, Inc., a Delaware corporation (“AXT”, “the Company”, “we,” “us,” and “our” refer to AXT, Inc. and its consolidated subsidiaries) contains forward-looking statements within the meaning of Section 27A of the Securities Act of 1933, as amended, and Section 21E of the Securities Exchange Act of 1934, as amended (the “Exchange Act”). Statements relating to our expectations regarding the receipt of export permits for our indium phosphide substrates, results of operations, market and customer demand for our products, our ability to expand our markets or increase sales, emerging applications using chips or devices fabricated on our substrates, including the use of InP wafer substrates in artificial intelligence (“AI”) applications, revenues from long-term supply agreements with customers, the development and adoption of new products, applications, enhancements or technologies, the life cycles of our products and applications, product yields and gross margins, expense levels, the impact of the adoption of certain accounting pronouncements, our investments in capital projects, ramping production at our new sites, potential severance costs with respect to any reduction in our work force, our ability to have new customers qualify substrates from our new manufacturing locations in China, our ability to utilize or increase our manufacturing … [S67]

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -5,995,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | 77,084,000 | USD | US GAAP / reported | CostOfRevenue | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | -18,778,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | 11,242,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | -21,260,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | -21,437,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | -23,202,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | -12,783,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | -21,976,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; definition_changed_across_series | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 3,292,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -7,226,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| cost_of_revenue | 26,223,000 | USD | US GAAP / reported | CostOfRevenue | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | 3,558,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| gross_profit | 21,366,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | 11,128,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | 11,084,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S05] |
| net_income_including_noncontrolling_interests | 13,030,000 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | 10,784,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | 10,423,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; definition_changed_across_series | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 762,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 120,266,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | DebtCurrent; alternative_tag_scope_differs, debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / reported / not model usable | ShortTermBorrowings; revision_requires_review | [S05] |
| short_term_investments | 0 | USD | US GAAP / reported | ShortTermInvestments | [S05] |


### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 412,167,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | DebtCurrent; alternative_tag_scope_differs, debt_scope_requires_filing_review, definition_changed_across_series | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | 79,000,000 | USD | US GAAP / reported | ShortTermBorrowings | [S05] |
| short_term_investments | 5,031,000 | USD | US GAAP / reported | ShortTermInvestments | [S05] |



## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-08-13, L845:

> Our Related Party Transactions Policy seeks to prohibit all conflicts of interest in transactions between related parties and us, unless they have been approved by our Board of Directors. This policy applies to all of our employees, directors, and our consolidated subsidiaries. Our executive officers retain board seats on the board of directors of the companies in which we have invested in our PRC joint ventures (see Note 7). [S67]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-08-13, L1566:

> From time to time we may be involved in judicial or administrative proceedings concerning matters arising in the ordinary course of business. We do not expect that any of these matters, individually or in the aggregate, will have a material adverse effect on our business, financial condition, cash flows or results of operations. [S67]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:31:15.090134+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
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

Calculation gaps: Operating margin: compatible positive revenue and usable inputs are required. Net margin: compatible positive revenue and usable inputs are required. Free cash flow margin: compatible positive revenue and usable inputs are required. Stock compensation / revenue: compatible positive revenue and usable inputs are required. revenue: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. net_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-05 | SCHEDULE 13G/A | 0002012383-26-003311 | — | [S17] |
| 2026-08-19 | 4 | 0001437749-26-028577 | — | [S18] |
| 2026-08-19 | 4 | 0001437749-26-028573 | — | [S19] |
| 2026-08-17 | 144 | 0001965301-26-000127 | — | [S20] |
| 2026-08-13 | 10-Q | 0001437749-26-027677 | — | [S21] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001051627.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001051627.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001437749-26-008612](https://www.sec.gov/Archives/edgar/data/1051627/000143774926008612/0001437749-26-008612-index.html) — published 2026-03-17; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [10-Q 0001437749-26-027677](https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/0001437749-26-027677-index.html) — published 2026-08-13; retrieved 2026-10-22T17:39:41.848518+00:00.

[S09] [10-Q 0001437749-26-017054](https://www.sec.gov/Archives/edgar/data/1051627/000143774926017054/0001437749-26-017054-index.html) — published 2026-05-14; retrieved 2026-10-22T17:39:41.848518+00:00.

[S17] [SCHEDULE 13G/A 0002012383-26-003311](https://www.sec.gov/Archives/edgar/data/1051627/000201238326003311/0002012383-26-003311-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [4 0001437749-26-028577](https://www.sec.gov/Archives/edgar/data/1051627/000143774926028577/0001437749-26-028577-index.html) — published 2026-08-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [4 0001437749-26-028573](https://www.sec.gov/Archives/edgar/data/1051627/000143774926028573/0001437749-26-028573-index.html) — published 2026-08-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [144 0001965301-26-000127](https://www.sec.gov/Archives/edgar/data/1051627/000196530126000127/0001965301-26-000127-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [10-Q 0001437749-26-027677](https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/0001437749-26-027677-index.html) — published 2026-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S67] [10-Q 0001437749-26-027677](https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/axti20260630_10q.htm) — published 2026-08-13; retrieved 2026-11-18T21:05:41.056030+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AXTI/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
