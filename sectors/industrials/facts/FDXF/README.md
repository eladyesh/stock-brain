---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002082247
cik: 0002082247
company_name: FedEx Freight Holding Company, Inc.
tickers:
- FDXF
status: stub
canonical_reviewed: false
as_of: '2026-10-25'
updated_at: '2026-10-25T13:50:29.910841+00:00'
reviewed_at: null
coverage_release: coverage-20261025-40199010718-1
source_commit: d4303e1efab53027fe4e6e90633e2c69b11c599c
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
  - '3'
  - '4'
  - 4/A
  - 8-K
  - CERT
  - DRS
  - DRS/A
  - S-8
  - SCHEDULE 13G
  - SEC STAFF ACTION
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002082247.json
    sha256: 2746dc975625de34f1e1fa6fcaea269ce6aff42db67da34966ab07c556bad688
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0002082247.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002082247.json
    sha256: 3674982c1fc48e11116008446c6785401d3cc17cdf5070b1d7ba093afcb4a58b
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002082247.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-25T13:45:48.334682+00:00'
  sha256: 94335ed3f4abc4bbd58a4415d105d453184f5484eaf6a2884d1bfb0120d850c9
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0002082247.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 3674982c1fc48e11116008446c6785401d3cc17cdf5070b1d7ba093afcb4a58b
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002082247.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 2746dc975625de34f1e1fa6fcaea269ce6aff42db67da34966ab07c556bad688
- id: S04
  title: 10-K 0001628280-26-053359
  url: https://www.sec.gov/Archives/edgar/data/2082247/000162828026053359/0001628280-26-053359-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 8-K 0001104659-26-113295
  url: https://www.sec.gov/Archives/edgar/data/2082247/000110465926113295/0001104659-26-113295-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 8-K 0001104659-26-104793
  url: https://www.sec.gov/Archives/edgar/data/2082247/000110465926104793/0001104659-26-104793-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001628280-26-055715
  url: https://www.sec.gov/Archives/edgar/data/2082247/000162828026055715/0001628280-26-055715-index.html
  published_at: '2026-08-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: SCHEDULE 13G 0001104659-26-092744
  url: https://www.sec.gov/Archives/edgar/data/2082247/000110465926092744/0001104659-26-092744-index.html
  published_at: '2026-08-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: 8-K 0001628280-26-054314
  url: https://www.sec.gov/Archives/edgar/data/2082247/000162828026054314/0001628280-26-054314-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S14
  title: 10-K 0001628280-26-053359
  url: https://www.sec.gov/Archives/edgar/data/2082247/000162828026053359/0001628280-26-053359-index.html
  published_at: '2026-08-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0002082247
  classification_status: reported_sic
  entity_type: operating
  name: FedEx Freight Holding Company, Inc.
  sic: '4513'
  sic_description: Air Courier Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 3674982c1fc48e11116008446c6785401d3cc17cdf5070b1d7ba093afcb4a58b
  url: https://data.sec.gov/submissions/CIK0002082247.json
listings:
- ticker: FDXF
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-053359
  filed: '2026-08-05'
  form: 10-K
  period_end: '2026-05-31'
  url: https://www.sec.gov/Archives/edgar/data/2082247/000162828026053359/0001628280-26-053359-index.html
- accession: 0001104659-26-113295
  filed: '2026-10-02'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/2082247/000110465926113295/0001104659-26-113295-index.html
research_progress:
  stage: pending
  input_sha256: 248385217aec7cbfe26c7783edb11cfad91711c062435794ba7abfa249fc8d90
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 4
  model_draft: false
  reviewed: false
sector_assignment:
  sector: industrials
  method: project_sic_rule
  sic: '4513'
  sic_description: Air Courier Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002082247.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/FDXF/README.md
full_history_commit: c6b3af0cefe967faceb0323aa590d422e87cbc29
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# FDXF — FedEx Freight Holding Company, Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/FDXF/README.md)

## Business overview

Reported issuer name: **FedEx Freight Holding Company, Inc.**. Stable SEC CIK: **0002082247**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| FDXF | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **4513**: Air Courier Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was 6.14% for 2025-06-01 to 2026-05-31 (US GAAP inputs). [S14]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=540000000 USD (OperatingIncomeLoss), revenue=8795000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Net margin was 7.45% for 2025-06-01 to 2026-05-31 (US GAAP inputs). [S14]
Formula: `net_income / revenue * 100`. Inputs: net_income=655000000 USD (NetIncomeLoss), revenue=8795000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Stock compensation / revenue was 0.15% for 2025-06-01 to 2026-05-31 (US GAAP inputs). [S14]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=13000000 USD (ShareBasedCompensation), revenue=8795000000 USD (RevenueFromContractWithCustomerExcludingAssessedTax).

Derived observation: Operating cash flow / net income was 0.25x for the year ended 2026-05-31. Working capital and non-cash adjustments require separate filing analysis. [S14]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=167000000 USD (NetCashProvidedByUsedInOperatingActivities), net_income=655000000 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-06-01 to 2026-05-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 655,000,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | 655,000,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| operating_cash_flow | 167,000,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 540,000,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | -379,000,000 | USD | US GAAP / reported | PaymentsToAcquireProductiveAssets; Cash outflow = negative of reported PaymentsToAcquireProductiveAssets; source value retained.; broader_than_property_plant_equipment_only | [S04] |
| revenue | 8,795,000,000 | USD | US GAAP / reported | RevenueFromContractWithCustomerExcludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 13,000,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |

## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### annual: 2025-06-01 to 2026-05-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligationsCurrent; debt_scope_requires_filing_review | [S04] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebtAndCapitalLeaseObligations; debt_scope_requires_filing_review | [S04] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; alternative_tag_scope_differs, debt_scope_requires_filing_review | [S04] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

Not available: reviewed debt maturity, acquisition, dividend and repurchase analysis.

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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:36:39.900991+00:00.

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

Calculation gaps: Free cash flow margin: compatible positive revenue and usable inputs are required. revenue: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. net_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-02 | 8-K | 0001104659-26-113295 | — | [S05] |
| 2026-09-02 | 8-K | 0001104659-26-104793 | — | [S06] |
| 2026-08-11 | 4 | 0001628280-26-055715 | — | [S07] |
| 2026-08-07 | SCHEDULE 13G | 0001104659-26-092744 | — | [S08] |
| 2026-08-06 | 8-K | 0001628280-26-054314 | — | [S09] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:48.334682+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002082247.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002082247.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001628280-26-053359](https://www.sec.gov/Archives/edgar/data/2082247/000162828026053359/0001628280-26-053359-index.html) — published 2026-08-05; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [8-K 0001104659-26-113295](https://www.sec.gov/Archives/edgar/data/2082247/000110465926113295/0001104659-26-113295-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [8-K 0001104659-26-104793](https://www.sec.gov/Archives/edgar/data/2082247/000110465926104793/0001104659-26-104793-index.html) — published 2026-09-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001628280-26-055715](https://www.sec.gov/Archives/edgar/data/2082247/000162828026055715/0001628280-26-055715-index.html) — published 2026-08-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [SCHEDULE 13G 0001104659-26-092744](https://www.sec.gov/Archives/edgar/data/2082247/000110465926092744/0001104659-26-092744-index.html) — published 2026-08-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [8-K 0001628280-26-054314](https://www.sec.gov/Archives/edgar/data/2082247/000162828026054314/0001628280-26-054314-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S14] [10-K 0001628280-26-053359](https://www.sec.gov/Archives/edgar/data/2082247/000162828026053359/0001628280-26-053359-index.html) — published 2026-08-05; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/FDXF/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
