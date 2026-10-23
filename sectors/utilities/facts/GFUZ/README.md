---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002074850
cik: 0002074850
company_name: General Fusion Group Ltd.
tickers:
- GFUZ
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: 3f697433c3580d4ca83edbe44c66580ac926c8d7
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-Q
  - 10-Q/A
  - 20-F
  - 25-NSE
  - '3'
  - '4'
  - 424B3
  - '425'
  - 6-K
  - 8-A12B
  - 8-K
  - CERT
  - CORRESP
  - DRS
  - EFFECT
  - F-1
  - F-4
  - F-4/A
  - S-1
  - S-1/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002074850.json
    sha256: 12ef434e41feed899713cd606268a93e172b4e2c2fc465eb71572bf6a2fb4e53
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0002074850.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002074850.json
    sha256: 90e5075c69093fb3f3e2e670b024399ad3558ecd02e4f059f12041e2ef0f1ce2
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002074850.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T14:17:54.530395+00:00'
  sha256: a31379ea4791bd232005b22547c9cfa517e0cb9e9f14ff7091be845f143d5c71
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0002074850.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 90e5075c69093fb3f3e2e670b024399ad3558ecd02e4f059f12041e2ef0f1ce2
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002074850.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 12ef434e41feed899713cd606268a93e172b4e2c2fc465eb71572bf6a2fb4e53
- id: S04
  title: 10-Q/A 0001104659-26-105499
  url: https://www.sec.gov/Archives/edgar/data/2074850/000110465926105499/0001104659-26-105499-index.html
  published_at: '2026-09-04'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S07
  title: 424B3 0001104659-26-114558
  url: https://www.sec.gov/Archives/edgar/data/2074850/000110465926114558/0001104659-26-114558-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: 6-K 0001104659-26-114557
  url: https://www.sec.gov/Archives/edgar/data/2074850/000110465926114557/0001104659-26-114557-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: EFFECT 9999999995-26-003157
  url: https://www.sec.gov/Archives/edgar/data/2074850/999999999526003157/9999999995-26-003157-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S10
  title: 424B3 0001104659-26-114061
  url: https://www.sec.gov/Archives/edgar/data/2074850/000110465926114061/0001104659-26-114061-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S11
  title: 6-K 0001104659-26-109354
  url: https://www.sec.gov/Archives/edgar/data/2074850/000110465926109354/0001104659-26-109354-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0002074850
  classification_status: reported_sic
  entity_type: operating
  name: General Fusion Group Ltd.
  sic: '4911'
  sic_description: Electric Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 90e5075c69093fb3f3e2e670b024399ad3558ecd02e4f059f12041e2ef0f1ce2
  url: https://data.sec.gov/submissions/CIK0002074850.json
listings:
- ticker: GFUZ
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-084015
  filed: '2026-07-16'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/2074850/000110465926084015/0001104659-26-084015-index.html
- accession: 0001104659-26-114557
  filed: '2026-10-08'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/2074850/000110465926114557/0001104659-26-114557-index.html
- accession: 0001104659-26-080739
  filed: '2026-07-06'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/2074850/000110465926080739/0001104659-26-080739-index.html
research_progress:
  stage: pending
  input_sha256: b02c29c50b994a14b5e8acc151c29ab2e346c00310d211ac2a4ac4fe1a409671
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: utilities
  method: project_sic_rule
  sic: '4911'
  sic_description: Electric Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0002074850.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/GFUZ/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# GFUZ — General Fusion Group Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/GFUZ/README.md)

## Business overview

Reported issuer name: **General Fusion Group Ltd.**. Stable SEC CIK: **0002074850**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| GFUZ | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **4911**: Electric Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **utilities**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-01-01 to 2026-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; fiscal_start_mismatch, missing_annual_anchor, revision_requires_review | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / reported / not model usable | ProfitLoss; fiscal_start_mismatch, missing_annual_anchor, revision_requires_review | [S04] |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetCashProvidedByUsedInOperatingActivities; fiscal_start_mismatch, missing_annual_anchor | [S04] |
| operating_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | OperatingIncomeLoss; fiscal_start_mismatch, missing_annual_anchor | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| stock_based_compensation | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |



## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


This view retains the latest available annual, quarterly and TTM periods. Full retained history is linked above.

### quarterly: 2026-01-01 to 2026-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / reported / not model usable | CashAndCashEquivalentsAtCarryingValue; fiscal_start_mismatch, missing_annual_anchor | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; fiscal_start_mismatch, missing_annual_anchor | No eligible evidence |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T14:34:39.908191+00:00.

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

Calculation gaps: No annual period is available for comparison.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-08 | 424B3 | 0001104659-26-114558 | — | [S07] |
| 2026-10-08 | 6-K | 0001104659-26-114557 | — | [S08] |
| 2026-10-06 | EFFECT | 9999999995-26-003157 | — | [S09] |
| 2026-10-06 | 424B3 | 0001104659-26-114061 | — | [S10] |
| 2026-09-21 | 6-K | 0001104659-26-109354 | — | [S11] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002074850.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002074850.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-Q/A 0001104659-26-105499](https://www.sec.gov/Archives/edgar/data/2074850/000110465926105499/0001104659-26-105499-index.html) — published 2026-09-04; retrieved 2026-10-22T17:39:41.848518+00:00.

[S07] [424B3 0001104659-26-114558](https://www.sec.gov/Archives/edgar/data/2074850/000110465926114558/0001104659-26-114558-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [6-K 0001104659-26-114557](https://www.sec.gov/Archives/edgar/data/2074850/000110465926114557/0001104659-26-114557-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [EFFECT 9999999995-26-003157](https://www.sec.gov/Archives/edgar/data/2074850/999999999526003157/9999999995-26-003157-index.html) — published 2026-10-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S10] [424B3 0001104659-26-114061](https://www.sec.gov/Archives/edgar/data/2074850/000110465926114061/0001104659-26-114061-index.html) — published 2026-10-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S11] [6-K 0001104659-26-109354](https://www.sec.gov/Archives/edgar/data/2074850/000110465926109354/0001104659-26-109354-index.html) — published 2026-09-21; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/GFUZ/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
