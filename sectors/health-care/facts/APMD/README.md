---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001745648
cik: 0001745648
company_name: Apnimed, Inc.
tickers:
- APMD
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: da985d7cdd310eab261be4fd3662836a26873702
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
  - 424B4
  - 8-A12B
  - 8-K
  - CERT
  - D
  - D/A
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
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001745648.json
    sha256: 979b02698bdc3d93327645e89c50c0dc3c8c07913c09bc8f3a85a8e249f0535b
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0001745648.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001745648.json
    sha256: 0df866cf65adebfc2464620791e44d18cbce9c4593a3c5220e87e0f568f5b249
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001745648.json
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
  url: https://data.sec.gov/submissions/CIK0001745648.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 0df866cf65adebfc2464620791e44d18cbce9c4593a3c5220e87e0f568f5b249
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001745648.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 979b02698bdc3d93327645e89c50c0dc3c8c07913c09bc8f3a85a8e249f0535b
- id: S04
  title: 10-Q 0001193125-26-385356
  url: https://www.sec.gov/Archives/edgar/data/1745648/000119312526385356/0001193125-26-385356-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: S-8 0001193125-26-385357
  url: https://www.sec.gov/Archives/edgar/data/1745648/000119312526385357/0001193125-26-385357-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 10-Q 0001193125-26-385356
  url: https://www.sec.gov/Archives/edgar/data/1745648/000119312526385356/0001193125-26-385356-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 8-K 0001193125-26-385355
  url: https://www.sec.gov/Archives/edgar/data/1745648/000119312526385355/0001193125-26-385355-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: SCHEDULE 13G 0001193125-26-340067
  url: https://www.sec.gov/Archives/edgar/data/1745648/000119312526340067/0001193125-26-340067-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: SCHEDULE 13G 0001104659-26-092032
  url: https://www.sec.gov/Archives/edgar/data/1745648/000110465926092032/0001104659-26-092032-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S56
  url: https://www.sec.gov/Archives/edgar/data/1745648/000119312526385356/apmd-20260630.htm
  title: 10-Q 0001193125-26-385356
  published_at: '2026-09-08'
  retrieved_at: '2026-11-13T20:13:25.468667+00:00'
  sha256: 9a90269a9551f5c7668d294140e4a840ff293b115b41b9785b9a3a253d0cf147
issuer_classification:
  cik: 0001745648
  classification_status: reported_sic
  entity_type: operating
  name: Apnimed, Inc.
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 0df866cf65adebfc2464620791e44d18cbce9c4593a3c5220e87e0f568f5b249
  url: https://data.sec.gov/submissions/CIK0001745648.json
listings:
- ticker: APMD
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-385356
  filed: '2026-09-08'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1745648/000119312526385356/0001193125-26-385356-index.html
- accession: 0001193125-26-385355
  filed: '2026-09-08'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1745648/000119312526385355/0001193125-26-385355-index.html
research_progress:
  stage: evidence_collected
  input_sha256: e0a2b9d435afbcbcae93b27d8725c28bd008be97ee852617c054b971904c6771
  last_attempt_at: '2026-11-13T20:12:14.550899+00:00'
  last_success_at: '2026-11-13T20:12:14.550899+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - competitive-landscape
  - growth-drivers
  - industry-and-value-chain
  - management-and-governance
  - moat-and-differentiation
  - products-and-services
  - recent-developments
  - revenue-model-and-segments
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: health-care
  method: project_sic_rule
  sic: '2834'
  sic_description: Pharmaceutical Preparations
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001745648.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/APMD/README.md
full_history_commit: 6e1c8271c74cf7335265700a5a223e692b47544f
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# APMD — Apnimed, Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/APMD/README.md)

## Business overview

Reported issuer name: **Apnimed, Inc.**. Stable SEC CIK: **0001745648**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| APMD | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-09-08, L255:

> We have based these forward-looking statements largely on our current expectations and estimates about future events and financial and other trends that we believe may affect our business, financial condition and results of operations. These forward-looking statements speak only as of the date of this Quarterly Report and are subject to a number of risks, uncertainties and assumptions described under the sections titled “Risk Factors” and “Management’s Discussion and Analysis of Financial Condition and Results of Operations” and elsewhere in this Quarterly Report. Because forward-looking statements are inherently subject to risks and uncertainties, some of which cannot be predicted or quantified and some of which are beyond our control, you should not rely on these forward-looking statements as predictions of future events. The events and circumstances reflected in our forward-looking statements may not be achieved or occur and actual results could differ materially from those estimated in the forward-looking statements. Moreover, we operate in an evolving environment. New risk factors and uncertainties may emerge from time to time, and it is not possible for management to predict all risk factors and uncertainties. The forward-looking statements contained in this Quarterly Report are made as of the date of this Quarterly Report, and we do not assume any obligation to update … [S56]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-09-08, L6152:

> The Company defines its segments on the basis of the way in which internally reported financial information is regularly reviewed by the chief operating decision maker ("CODM"), to analyze financial performance, make decisions, and allocate resources. The Company’s CODM is its Chief Executive Officer. The Company manages its operations as a single operating and reportable segment dedicated to the discovery, development and commercialization of novel oral therapies that address the neurobiology of sleep-related breathing diseases. The CODM uses net loss to monitor budget versus actual results and to analyze cash flows in assessing performance of the segment and allocating resources. All business activities are managed on a consolidated basis. As discussed further in Note 10, all revenue - related party recognized during the period has been generated from the SASS joint venture with Shionogi, which includes a combined performance obligation including the exclusive license under the Company's license agreement with SASS, which the Company entered in November 2023, and services to be performed under the MSA in accordance with SASS's research and development plan. The internal reporting of significant segment expenses is based on functional classification. The measure of the operating segment assets is reported on the consolidated balance sheet as total assets. All tangible assets … [S56]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-Q, filed 2026-09-08, L279:

> The marketing approval process is expensive, time-consuming and uncertain and may prevent us from obtaining approval for the commercialization of Oxnimbi. Furthermore, if there are delays in obtaining regulatory approvals, we may not be able to commercialize our products, may lose competitive lead time and our ability to generate revenues will be materially impaired. [S56]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 10-Q, filed 2026-09-08, L6728:

> establish and expand manufacturing capabilities and supply chain capacity for Oxnimbi or any future product candidates; [S56]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-Q, filed 2026-09-08, L253:

> This Quarterly Report on Form 10-Q (“Quarterly Report”) contains forward-looking statements about us and our industry. We intend such forward-looking statements to be covered by the safe harbor provisions for forward-looking statements contained in Section 27A of the Securities Act of 1933, as amended (the “Securities Act”), and Section 21E of the Securities Exchange Act of 1934, as amended (the “Exchange Act”). All statements other than statements of historical facts contained in this Quarterly Report are forward-looking statements, including statements regarding the timing of any submission of filings for regulatory approval of, and our ability to obtain and maintain regulatory approvals for, AD109 ("Oxnimbi") or any future product candidates; our planned commercialization activities, and our ability to successfully commercialize Oxnimbi, if approved; the effects of competition with respect to Oxnimbi or any future product candidates; the rate and degree of market acceptance, as well as the pricing and reimbursement of Oxnimbi, if approved; the scope, progress, results and costs of developing Oxnimbi or any future product candidates and conducting preclinical studies and clinical trials; our ability to maintain relationships with collaborators and licensors and identify and enter into future license agreements and collaborations; our ability to maintain and enforce our … [S56]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-Q, filed 2026-09-08, L253:

> This Quarterly Report on Form 10-Q (“Quarterly Report”) contains forward-looking statements about us and our industry. We intend such forward-looking statements to be covered by the safe harbor provisions for forward-looking statements contained in Section 27A of the Securities Act of 1933, as amended (the “Securities Act”), and Section 21E of the Securities Exchange Act of 1934, as amended (the “Exchange Act”). All statements other than statements of historical facts contained in this Quarterly Report are forward-looking statements, including statements regarding the timing of any submission of filings for regulatory approval of, and our ability to obtain and maintain regulatory approvals for, AD109 ("Oxnimbi") or any future product candidates; our planned commercialization activities, and our ability to successfully commercialize Oxnimbi, if approved; the effects of competition with respect to Oxnimbi or any future product candidates; the rate and degree of market acceptance, as well as the pricing and reimbursement of Oxnimbi, if approved; the scope, progress, results and costs of developing Oxnimbi or any future product candidates and conducting preclinical studies and clinical trials; our ability to maintain relationships with collaborators and licensors and identify and enter into future license agreements and collaborations; our ability to maintain and enforce our … [S56]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-Q, filed 2026-09-08, L6747:

> In addition, if we obtain regulatory approval for Oxnimbi or any future product candidates and do not enter into a third-party commercialization partnership, we expect to incur significant expenses related to developing our commercialization capability to support product sales, marketing, manufacturing and distribution activities. If Oxnimbi is approved, the earliest we would expect to generate revenue from product sales is 2027. As a result, we will need substantial additional funding to support our continuing operations and pursue our growth strategy. [S56]

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; missing_annual_anchor | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLossAvailableToCommonStockholdersBasic; missing_annual_anchor | [S04] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | OperatingIncomeLoss; missing_annual_anchor | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | Revenues; missing_annual_anchor | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |

## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; missing_annual_anchor | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |

Not available: reviewed debt maturity, acquisition, dividend and repurchase analysis.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-09-08, L5599:

> Dividends—The holders of Preferred Stock are entitled to receive non-cumulative and non-accruing dividends on an equal priority, in an amount at least equal to 8% of each Series’ original issue price. Dividends are payable only when, as, and if declared by the Board of Directors of the Company. There have been no dividends declared or paid. [S56]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-09-08, L255:

> We have based these forward-looking statements largely on our current expectations and estimates about future events and financial and other trends that we believe may affect our business, financial condition and results of operations. These forward-looking statements speak only as of the date of this Quarterly Report and are subject to a number of risks, uncertainties and assumptions described under the sections titled “Risk Factors” and “Management’s Discussion and Analysis of Financial Condition and Results of Operations” and elsewhere in this Quarterly Report. Because forward-looking statements are inherently subject to risks and uncertainties, some of which cannot be predicted or quantified and some of which are beyond our control, you should not rely on these forward-looking statements as predictions of future events. The events and circumstances reflected in our forward-looking statements may not be achieved or occur and actual results could differ materially from those estimated in the forward-looking statements. Moreover, we operate in an evolving environment. New risk factors and uncertainties may emerge from time to time, and it is not possible for management to predict all risk factors and uncertainties. The forward-looking statements contained in this Quarterly Report are made as of the date of this Quarterly Report, and we do not assume any obligation to update … [S56]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:35:23.208551+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
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

Calculation gaps: No annual period is available for comparison.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-08 | S-8 | 0001193125-26-385357 | — | [S05] |
| 2026-09-08 | 10-Q | 0001193125-26-385356 | — | [S06] |
| 2026-09-08 | 8-K | 0001193125-26-385355 | — | [S07] |
| 2026-08-07 | SCHEDULE 13G | 0001193125-26-340067 | — | [S08] |
| 2026-08-06 | SCHEDULE 13G | 0001104659-26-092032 | — | [S09] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001745648.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001745648.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-Q 0001193125-26-385356](https://www.sec.gov/Archives/edgar/data/1745648/000119312526385356/0001193125-26-385356-index.html) — published 2026-09-08; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [S-8 0001193125-26-385357](https://www.sec.gov/Archives/edgar/data/1745648/000119312526385357/0001193125-26-385357-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [10-Q 0001193125-26-385356](https://www.sec.gov/Archives/edgar/data/1745648/000119312526385356/0001193125-26-385356-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [8-K 0001193125-26-385355](https://www.sec.gov/Archives/edgar/data/1745648/000119312526385355/0001193125-26-385355-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [SCHEDULE 13G 0001193125-26-340067](https://www.sec.gov/Archives/edgar/data/1745648/000119312526340067/0001193125-26-340067-index.html) — published 2026-08-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [SCHEDULE 13G 0001104659-26-092032](https://www.sec.gov/Archives/edgar/data/1745648/000110465926092032/0001104659-26-092032-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S56] [10-Q 0001193125-26-385356](https://www.sec.gov/Archives/edgar/data/1745648/000119312526385356/apmd-20260630.htm) — published 2026-09-08; retrieved 2026-11-13T20:13:25.468667+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/APMD/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
