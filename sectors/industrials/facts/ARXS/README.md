---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002093536
cik: 0002093536
company_name: Arxis, Inc.
tickers:
- ARXS
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
  - 10-Q
  - '3'
  - '4'
  - 424B3
  - 424B4
  - 8-A12B
  - 8-K
  - CERT
  - DRS
  - DRS/A
  - EFFECT
  - S-1
  - S-1/A
  - S-1MEF
  - S-8
  - SCHEDULE 13G
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002093536.json
    sha256: 90ed2447379d85a8951c419f0133d89c6442f95926432fd90bebda3290b2df0d
    retrieved_at: '2026-10-22T18:10:35.452616+00:00'
    archive:
      member: CIK0002093536.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002093536.json
    sha256: 88a932103374b3edd497fe7bc738c1ee328a6708b3c4a66874e29c1e48fa797b
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0002093536.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
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
  url: https://data.sec.gov/submissions/CIK0002093536.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 88a932103374b3edd497fe7bc738c1ee328a6708b3c4a66874e29c1e48fa797b
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002093536.json
  published_at: null
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: 90ed2447379d85a8951c419f0133d89c6442f95926432fd90bebda3290b2df0d
- id: S04
  title: 10-Q 0001193125-26-325027
  url: https://www.sec.gov/Archives/edgar/data/2093536/000119312526325027/0001193125-26-325027-index.html
  published_at: '2026-07-30'
  retrieved_at: '2026-10-22T18:10:35.452616+00:00'
  sha256: null
- id: S06
  title: EFFECT 9999999995-26-003322
  url: https://www.sec.gov/Archives/edgar/data/2093536/999999999526003322/9999999995-26-003322-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 424B3 0001193125-26-428993
  url: https://www.sec.gov/Archives/edgar/data/2093536/000119312526428993/0001193125-26-428993-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S08
  title: S-1 0001193125-26-419718
  url: https://www.sec.gov/Archives/edgar/data/2093536/000119312526419718/0001193125-26-419718-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S09
  title: SCHEDULE 13G 0001096906-26-001396
  url: https://www.sec.gov/Archives/edgar/data/2093536/000109690626001396/0001096906-26-001396-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S10
  title: 4 0000950103-26-012767
  url: https://www.sec.gov/Archives/edgar/data/2093536/000095010326012767/0000950103-26-012767-index.html
  published_at: '2026-08-21'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/2093536/000119312526325027/arxs-20260630.htm
  title: 10-Q 0001193125-26-325027
  published_at: '2026-07-30'
  retrieved_at: '2026-11-14T18:46:34.212446+00:00'
  sha256: 0f1096581776dee4fca145d9c1a16efe1c8fa185ec38e114ac5672664bb78ae5
issuer_classification:
  cik: 0002093536
  classification_status: reported_sic
  entity_type: operating
  name: Arxis, Inc.
  sic: '3728'
  sic_description: Aircraft Parts & Auxiliary Equipment, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 88a932103374b3edd497fe7bc738c1ee328a6708b3c4a66874e29c1e48fa797b
  url: https://data.sec.gov/submissions/CIK0002093536.json
listings:
- ticker: ARXS
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-325027
  filed: '2026-07-30'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/2093536/000119312526325027/0001193125-26-325027-index.html
- accession: 0001193125-26-354774
  filed: '2026-08-18'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/2093536/000119312526354774/0001193125-26-354774-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 00d0d9e9103afac0cddefa8f221661d4499c615c5df145b397ae81e7f4016462
  last_attempt_at: '2026-11-14T18:39:40.176158+00:00'
  last_success_at: '2026-11-14T18:39:40.176158+00:00'
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
  - revenue-model-and-segments
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '3728'
  sic_description: Aircraft Parts & Auxiliary Equipment, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002093536.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ARXS/README.md
full_history_commit: 8c5afb0854b43beae818b88ec42b173c9411d269
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ARXS — Arxis, Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ARXS/README.md)

## Business overview

Reported issuer name: **Arxis, Inc.**. Stable SEC CIK: **0002093536**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ARXS | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-07-30, L5632:

> As of June 30, 2026 and December 31, 2025, $44,867 and $45,015, respectively, were accrued for these environmental investigation and remediation activities in Other long-term liabilities. The aggregate undiscounted amount has been accrued because it represents the Company’s best estimate of the cost, but the timing of payments is not considered to be fixed and reliably determinable. There can be no assurance that this matter would not have an adverse impact on our business, financial condition, results of operations and/or cash flows. [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-07-30, L3496:

> The Company has two reportable segments, Electronic Components and Mechanical Components. The Company’s segment reporting structure is consistent with how the Chief Operating Decision Maker ("CODM") reviews the business, makes investment and resource-allocation decisions, and assesses operating performance. [S53]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-Q, filed 2026-07-30, L5974:

> This Quarterly Report on Form 10-Q, including the exhibits being filed as part of this report, as well as other statements made by Arxis, Inc. (“Arxis,” the “Company,” “we,” “us” and “our”), contain forward-looking statements that reflect, when made, the Company’s current views with respect to current events, certain investments and acquisitions and financial performance. Such forward-looking statements are subject to many risks, uncertainties and factors relating to the Company’s operations and business environment, which may cause the actual results of the Company to be materially different from any future results, express or implied, by such forward-looking statements. All statements that address future operating, financial or business performance or the Company’s strategies or expectations are forward-looking statements. In some cases, you can identify these statements by forward-looking words such as “may,” “might,” “will,” “should,” “expects,” “plans,” “intends,” “anticipates,” “believes,” “estimates,” “predicts,” “projects,” “potential,” “outlook” or “continue,” and other comparable terminology. Factors that could cause actual results to differ materially from these forward-looking statements include, but are not limited to, the following: the concentration of our business on the aerospace and defense industries; the unique business risks of supplying products to … [S53]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-Q, filed 2026-07-30, L2926:

> Arxis designs, manufactures, and sells highly engineered electronic and mechanical components primarily used in mission-critical applications. The Company serves diverse end markets including defense and space, commercial aerospace, and industrial technology, and operates highly specialized manufacturing facilities globally, with a focus on domestic manufacturing. [S53]

## Industry and value chain

SEC-reported SIC **3728**: Aircraft Parts & Auxiliary Equipment, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 10-Q, filed 2026-07-30, L5974:

> This Quarterly Report on Form 10-Q, including the exhibits being filed as part of this report, as well as other statements made by Arxis, Inc. (“Arxis,” the “Company,” “we,” “us” and “our”), contain forward-looking statements that reflect, when made, the Company’s current views with respect to current events, certain investments and acquisitions and financial performance. Such forward-looking statements are subject to many risks, uncertainties and factors relating to the Company’s operations and business environment, which may cause the actual results of the Company to be materially different from any future results, express or implied, by such forward-looking statements. All statements that address future operating, financial or business performance or the Company’s strategies or expectations are forward-looking statements. In some cases, you can identify these statements by forward-looking words such as “may,” “might,” “will,” “should,” “expects,” “plans,” “intends,” “anticipates,” “believes,” “estimates,” “predicts,” “projects,” “potential,” “outlook” or “continue,” and other comparable terminology. Factors that could cause actual results to differ materially from these forward-looking statements include, but are not limited to, the following: the concentration of our business on the aerospace and defense industries; the unique business risks of supplying products to … [S53]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-Q, filed 2026-07-30, L5974:

> This Quarterly Report on Form 10-Q, including the exhibits being filed as part of this report, as well as other statements made by Arxis, Inc. (“Arxis,” the “Company,” “we,” “us” and “our”), contain forward-looking statements that reflect, when made, the Company’s current views with respect to current events, certain investments and acquisitions and financial performance. Such forward-looking statements are subject to many risks, uncertainties and factors relating to the Company’s operations and business environment, which may cause the actual results of the Company to be materially different from any future results, express or implied, by such forward-looking statements. All statements that address future operating, financial or business performance or the Company’s strategies or expectations are forward-looking statements. In some cases, you can identify these statements by forward-looking words such as “may,” “might,” “will,” “should,” “expects,” “plans,” “intends,” “anticipates,” “believes,” “estimates,” “predicts,” “projects,” “potential,” “outlook” or “continue,” and other comparable terminology. Factors that could cause actual results to differ materially from these forward-looking statements include, but are not limited to, the following: the concentration of our business on the aerospace and defense industries; the unique business risks of supplying products to … [S53]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-Q, filed 2026-07-30, L5974:

> This Quarterly Report on Form 10-Q, including the exhibits being filed as part of this report, as well as other statements made by Arxis, Inc. (“Arxis,” the “Company,” “we,” “us” and “our”), contain forward-looking statements that reflect, when made, the Company’s current views with respect to current events, certain investments and acquisitions and financial performance. Such forward-looking statements are subject to many risks, uncertainties and factors relating to the Company’s operations and business environment, which may cause the actual results of the Company to be materially different from any future results, express or implied, by such forward-looking statements. All statements that address future operating, financial or business performance or the Company’s strategies or expectations are forward-looking statements. In some cases, you can identify these statements by forward-looking words such as “may,” “might,” “will,” “should,” “expects,” “plans,” “intends,” “anticipates,” “believes,” “estimates,” “predicts,” “projects,” “potential,” “outlook” or “continue,” and other comparable terminology. Factors that could cause actual results to differ materially from these forward-looking statements include, but are not limited to, the following: the concentration of our business on the aerospace and defense industries; the unique business risks of supplying products to … [S53]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-Q, filed 2026-07-30, L7704:

> Historically, our primary sources of liquidity have been cash and cash equivalents, cash flows from our operating activities and borrowings under our credit agreements, including revolving credit facilities. In April 2026, the Company completed its IPO of shares of Class A common stock. Net proceeds from the IPO were $1,220.6 million, after deducting underwriting discounts, commissions and offering costs. A portion of the net proceeds was used to repay $946.0 million of outstanding indebtedness under the Company’s Term Loan Credit Facility, with the remainder to be used for working capital and general corporate purposes. Our principal historical liquidity requirements have been for acquisitions, capital expenditures, servicing indebtedness and working capital needs. As we continue to expand our business, we may require additional working capital in the future for increased costs, and although we believe that we will be able to fully fund our ongoing capital expenditures, working capital requirements and other capital needs for the foreseeable future through cash on hand and cash flows from our operating activities, we may choose to use borrowings under our credit facilities to finance our operating and investing activities. Based on our current outlook, we believe that net cash provided by operating activities and available borrowings under our credit agreements will be … [S53]

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfRevenue; missing_annual_anchor | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; missing_annual_anchor | [S04] |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; missing_annual_anchor | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLossAvailableToCommonStockholdersBasic; missing_annual_anchor | [S04] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | OperatingIncomeLoss; missing_annual_anchor | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; missing_annual_anchor | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T18:10:35.452616+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; missing_annual_anchor | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | DebtCurrent; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / derived / not model usable | DebtCurrent + LongTermDebtNoncurrent; debt_scope_requires_filing_review, derived_input_requires_review, missing_annual_anchor | [S04] |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |



## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-07-30, L5732:

> Prior to the Reorganization, Arcline Engineered Polymer Topco, L.P., Hawkeye TopCo, L.P., Connector TopCo, L.P., and Ovation TopCo, L.P. established Management Equity Plans (the “ME Plans”), Growth Participation Plans (“GPP”) and the Value Creation Bonus (“VCB”) Plan, under which the Board of Directors of each entity’s plan had the authority to grant Management Incentive Units (“MIUs”), Growth Participation Units (“GPUs”) and VCBs, respectively. [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-07-30, L5699:

> The Company is subject to commercial matters and legal proceedings and claims that arise in the normal course of business. While the outcome of these matters cannot be predicted with certainty, the Company does not have any knowledge of any such matters that would have a material adverse effect on the condensed consolidated financial statements, except as disclosed below. [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:36:41.148472+00:00.

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
- **Recent developments** (evidence or analysis still needed): Keep a dated, source-backed log of material changes. Distinguish the event date from the article date and explain what changed in the profile.

Calculation gaps: No annual period is available for comparison.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-22 | EFFECT | 9999999995-26-003322 | — | [S06] |
| 2026-10-22 | 424B3 | 0001193125-26-428993 | — | [S07] |
| 2026-10-13 | S-1 | 0001193125-26-419718 | — | [S08] |
| 2026-09-21 | SCHEDULE 13G | 0001096906-26-001396 | — | [S09] |
| 2026-08-21 | 4 | 0000950103-26-012767 | — | [S10] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002093536.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002093536.json) — published not supplied; retrieved 2026-10-22T18:10:35.452616+00:00.

[S04] [10-Q 0001193125-26-325027](https://www.sec.gov/Archives/edgar/data/2093536/000119312526325027/0001193125-26-325027-index.html) — published 2026-07-30; retrieved 2026-10-22T18:10:35.452616+00:00.

[S06] [EFFECT 9999999995-26-003322](https://www.sec.gov/Archives/edgar/data/2093536/999999999526003322/9999999995-26-003322-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [424B3 0001193125-26-428993](https://www.sec.gov/Archives/edgar/data/2093536/000119312526428993/0001193125-26-428993-index.html) — published 2026-10-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S08] [S-1 0001193125-26-419718](https://www.sec.gov/Archives/edgar/data/2093536/000119312526419718/0001193125-26-419718-index.html) — published 2026-10-13; retrieved 2026-10-24T13:22:51.759433+00:00.

[S09] [SCHEDULE 13G 0001096906-26-001396](https://www.sec.gov/Archives/edgar/data/2093536/000109690626001396/0001096906-26-001396-index.html) — published 2026-09-21; retrieved 2026-10-24T13:22:51.759433+00:00.

[S10] [4 0000950103-26-012767](https://www.sec.gov/Archives/edgar/data/2093536/000095010326012767/0000950103-26-012767-index.html) — published 2026-08-21; retrieved 2026-10-24T13:22:51.759433+00:00.

[S53] [10-Q 0001193125-26-325027](https://www.sec.gov/Archives/edgar/data/2093536/000119312526325027/arxs-20260630.htm) — published 2026-07-30; retrieved 2026-11-14T18:46:34.212446+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/8c5afb0854b43beae818b88ec42b173c9411d269/brain/companies/ARXS/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
