---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002096300
cik: 0002096300
company_name: AEVEX Corp.
tickers:
- AVEX
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 107777182f87f961989f84e51ee16bb872074fdf
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
  - 4/A
  - 424B4
  - 8-A12B
  - 8-K
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - EFFECT
  - S-1
  - S-1/A
  - S-8
  - SCHEDULE 13G
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002096300.json
    sha256: 903e1e607b363fe8569d767ea0f45fce4331d96abd1e079c59193dc47fa2366e
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0002096300.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002096300.json
    sha256: ecc56250be0efd3f9cab57460024c7c1715696b57661f10316dfc3ee58e06118
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002096300.json
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
  url: https://data.sec.gov/submissions/CIK0002096300.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ecc56250be0efd3f9cab57460024c7c1715696b57661f10316dfc3ee58e06118
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002096300.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 903e1e607b363fe8569d767ea0f45fce4331d96abd1e079c59193dc47fa2366e
- id: S04
  title: 10-Q 0002096300-26-000022
  url: https://www.sec.gov/Archives/edgar/data/2096300/000209630026000022/0002096300-26-000022-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: SCHEDULE 13G 0001894225-26-000005
  url: https://www.sec.gov/Archives/edgar/data/2096300/000189422526000005/0001894225-26-000005-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 3 0001231919-26-001181
  url: https://www.sec.gov/Archives/edgar/data/2096300/000123191926001181/0001231919-26-001181-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 8-K 0001193125-26-385301
  url: https://www.sec.gov/Archives/edgar/data/2096300/000119312526385301/0001193125-26-385301-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: SCHEDULE 13G 0001331875-26-000078
  url: https://www.sec.gov/Archives/edgar/data/2096300/000133187526000078/0001331875-26-000078-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: SCHEDULE 13G 0001193125-26-352759
  url: https://www.sec.gov/Archives/edgar/data/2096300/000119312526352759/0001193125-26-352759-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S56
  url: https://www.sec.gov/Archives/edgar/data/2096300/000209630026000022/avex-20260630.htm
  title: 10-Q 0002096300-26-000022
  published_at: '2026-08-12'
  retrieved_at: '2026-11-17T21:34:59.984629+00:00'
  sha256: f9a0d1c589eda2579cb16641f77f5a8870ecae842fe144b242b098c56b7da0b3
issuer_classification:
  cik: 0002096300
  classification_status: reported_sic
  entity_type: operating
  name: AEVEX Corp.
  sic: '3721'
  sic_description: Aircraft
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ecc56250be0efd3f9cab57460024c7c1715696b57661f10316dfc3ee58e06118
  url: https://data.sec.gov/submissions/CIK0002096300.json
listings:
- ticker: AVEX
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0002096300-26-000022
  filed: '2026-08-12'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/2096300/000209630026000022/0002096300-26-000022-index.html
- accession: 0001193125-26-385301
  filed: '2026-09-08'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/2096300/000119312526385301/0001193125-26-385301-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 421aa1355f985541bef3e14ea8ed071ea38f79fedb1267606f94880494da8be5
  last_attempt_at: '2026-11-17T21:29:10.535348+00:00'
  last_success_at: '2026-11-17T21:29:10.535348+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - customers-and-end-markets
  - growth-drivers
  - industry-and-value-chain
  - management-and-governance
  - products-and-services
  - recent-developments
  - revenue-model-and-segments
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '3721'
  sic_description: Aircraft
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002096300.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/AVEX/README.md
full_history_commit: 0f49b319f95dcee8e757e592a38a028a04a7bc3c
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AVEX — AEVEX Corp.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/AVEX/README.md)

## Business overview

Reported issuer name: **AEVEX Corp.**. Stable SEC CIK: **0002096300**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AVEX | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-08-12, L230:

> •pandemics, public health crises and other events that could disrupt our business, supply chain or customer demand; [S56]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-08-12, L740:

> Please refer to the condensed consolidated statements of operations for the disaggregation of revenue by products versus services and to Note 14, Segment Information, for disaggregation of revenue by reportable segment. [S56]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-Q, filed 2026-08-12, L218:

> •the markets into which we sell our products and services decline or do not grow as expected; [S56]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-Q, filed 2026-08-12, L231:

> •technological failures, cybersecurity breaches or unauthorized access to our, our customers’ or our suppliers’ information and systems; [S56]

## Industry and value chain

SEC-reported SIC **3721**: Aircraft. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 10-Q, filed 2026-08-12, L230:

> •pandemics, public health crises and other events that could disrupt our business, supply chain or customer demand; [S56]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-Q, filed 2026-08-12, L217:

> •increasing competitive pressures in our industry, including the risk that we are not able to expand our customer base, achieve broad market acceptance, or compete effectively against larger or better-resourced competitors; [S56]

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; missing_annual_anchor | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; missing_annual_anchor | [S04] |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; missing_annual_anchor | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / reported / not model usable | ProfitLoss; missing_annual_anchor | [S04] |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | OperatingIncomeLoss; missing_annual_anchor | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; missing_annual_anchor | [S04] |
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
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtCurrent; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtNoncurrent; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |

Not available: reviewed debt maturity, acquisition, dividend and repurchase analysis.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-08-12, L651:

> Subsequent to the Organizational Transactions and IPO, the Company granted Class A common stock restricted stock units ("RSUs") and performance-based restricted stock units (“PSUs”) to certain employees and non-employee directors. The Company accounts for stock compensation in accordance with Accounting Standards Codification (“ASC”) 718, Compensation — Stock Compensation (“ASC 718”). Share-based awards are measured at their grant-date fair value. For the RSUs and PSUs, fair value is determined based on the closing stock price of the Company’s Class A common stock on the grant date. The grant date is the date upon which the Company and a grantee have a mutual understanding of all key terms and conditions of an award, including all annual performance conditions determined by the Board of Directors. Stock compensation expense recognition starts on the grant date and occurs on a straight-line basis for awards with service-only vesting conditions (e.g., RSUs) over the vesting period, whereas awards with performance conditions (e.g., PSUs) expense recognition occurs using the accelerated attribution method over the implicit or explicit service period when a performance condition is deemed probable of achievement. Expense recorded for performance-based awards is reversed if the performance conditions are no longer deemed probable of achievement or ultimately are not achieved. The … [S56]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-08-12, L239:

> •other factors set forth under the “Risk Factors” section in our most recent filings with the Securities and Exchange Commission. [S56]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:36:41.346174+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (source excerpts available; assess the claim): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (source excerpts available; assess the claim): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (evidence or analysis still needed): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (evidence or analysis still needed): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
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
| 2026-09-15 | SCHEDULE 13G | 0001894225-26-000005 | — | [S05] |
| 2026-09-15 | 3 | 0001231919-26-001181 | — | [S06] |
| 2026-09-08 | 8-K | 0001193125-26-385301 | — | [S07] |
| 2026-08-14 | SCHEDULE 13G | 0001331875-26-000078 | — | [S08] |
| 2026-08-14 | SCHEDULE 13G | 0001193125-26-352759 | — | [S09] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002096300.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002096300.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-Q 0002096300-26-000022](https://www.sec.gov/Archives/edgar/data/2096300/000209630026000022/0002096300-26-000022-index.html) — published 2026-08-12; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [SCHEDULE 13G 0001894225-26-000005](https://www.sec.gov/Archives/edgar/data/2096300/000189422526000005/0001894225-26-000005-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [3 0001231919-26-001181](https://www.sec.gov/Archives/edgar/data/2096300/000123191926001181/0001231919-26-001181-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [8-K 0001193125-26-385301](https://www.sec.gov/Archives/edgar/data/2096300/000119312526385301/0001193125-26-385301-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [SCHEDULE 13G 0001331875-26-000078](https://www.sec.gov/Archives/edgar/data/2096300/000133187526000078/0001331875-26-000078-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [SCHEDULE 13G 0001193125-26-352759](https://www.sec.gov/Archives/edgar/data/2096300/000119312526352759/0001193125-26-352759-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S56] [10-Q 0002096300-26-000022](https://www.sec.gov/Archives/edgar/data/2096300/000209630026000022/avex-20260630.htm) — published 2026-08-12; retrieved 2026-11-17T21:34:59.984629+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/AVEX/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
