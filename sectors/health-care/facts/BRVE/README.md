---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002131524
cik: '0002131524'
company_name: Braveheart Bio, Inc.
tickers:
- BRVE
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
  - 10-Q
  - '3'
  - '4'
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
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002131524.json
    sha256: e71254074850b7192122b19bfbcd969567877eb1a8152becba6ac0f13c2af749
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0002131524.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002131524.json
    sha256: 2f49edf9979cd5efd651ccf69145da3a7fed98544d83b0a6d402ed46e09073da
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002131524.json
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
  url: https://data.sec.gov/submissions/CIK0002131524.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2f49edf9979cd5efd651ccf69145da3a7fed98544d83b0a6d402ed46e09073da
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002131524.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: e71254074850b7192122b19bfbcd969567877eb1a8152becba6ac0f13c2af749
- id: S04
  title: 10-Q 0001628280-26-060905
  url: https://www.sec.gov/Archives/edgar/data/2131524/000162828026060905/0001628280-26-060905-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: SCHEDULE 13D/A 0000947871-26-000860
  url: https://www.sec.gov/Archives/edgar/data/2131524/000094787126000860/0000947871-26-000860-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 10-Q 0001628280-26-060905
  url: https://www.sec.gov/Archives/edgar/data/2131524/000162828026060905/0001628280-26-060905-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 8-K 0001628280-26-060904
  url: https://www.sec.gov/Archives/edgar/data/2131524/000162828026060904/0001628280-26-060904-index.html
  published_at: '2026-09-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: SCHEDULE 13D 0000947871-26-000814
  url: https://www.sec.gov/Archives/edgar/data/2131524/000094787126000814/0000947871-26-000814-index.html
  published_at: '2026-08-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: 3 0002003663-26-000005
  url: https://www.sec.gov/Archives/edgar/data/2131524/000200366326000005/0002003663-26-000005-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0002131524'
  classification_status: reported_sic
  entity_type: operating
  name: Braveheart Bio, Inc.
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2f49edf9979cd5efd651ccf69145da3a7fed98544d83b0a6d402ed46e09073da
  url: https://data.sec.gov/submissions/CIK0002131524.json
listings:
- ticker: BRVE
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-060905
  filed: '2026-09-08'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/2131524/000162828026060905/0001628280-26-060905-index.html
- accession: 0001628280-26-060904
  filed: '2026-09-08'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/2131524/000162828026060904/0001628280-26-060904-index.html
research_progress:
  stage: pending
  input_sha256: ce687a720410a4e7be0e987e55a43ae5986f6760756c6fcfcca1eb7ef9e684e0
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
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
  source_url: https://data.sec.gov/submissions/CIK0002131524.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/BRVE/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BRVE — Braveheart Bio, Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/BRVE/README.md)

## Business overview

Reported issuer name: **Braveheart Bio, Inc.**. Stable SEC CIK: **0002131524**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BRVE | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| net_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLoss; missing_annual_anchor | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / reported / not model usable | NetIncomeLossAvailableToCommonStockholdersBasic; missing_annual_anchor | [S04] |
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / reported / not model usable | OperatingIncomeLoss; missing_annual_anchor | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
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
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |

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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-23T14:34:46.748933+00:00.

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
| 2026-09-10 | SCHEDULE 13D/A | 0000947871-26-000860 | — | [S05] |
| 2026-09-08 | 10-Q | 0001628280-26-060905 | — | [S06] |
| 2026-09-08 | 8-K | 0001628280-26-060904 | — | [S07] |
| 2026-08-18 | SCHEDULE 13D | 0000947871-26-000814 | — | [S08] |
| 2026-08-14 | 3 | 0002003663-26-000005 | — | [S09] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002131524.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002131524.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-Q 0001628280-26-060905](https://www.sec.gov/Archives/edgar/data/2131524/000162828026060905/0001628280-26-060905-index.html) — published 2026-09-08; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [SCHEDULE 13D/A 0000947871-26-000860](https://www.sec.gov/Archives/edgar/data/2131524/000094787126000860/0000947871-26-000860-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [10-Q 0001628280-26-060905](https://www.sec.gov/Archives/edgar/data/2131524/000162828026060905/0001628280-26-060905-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [8-K 0001628280-26-060904](https://www.sec.gov/Archives/edgar/data/2131524/000162828026060904/0001628280-26-060904-index.html) — published 2026-09-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [SCHEDULE 13D 0000947871-26-000814](https://www.sec.gov/Archives/edgar/data/2131524/000094787126000814/0000947871-26-000814-index.html) — published 2026-08-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [3 0002003663-26-000005](https://www.sec.gov/Archives/edgar/data/2131524/000200366326000005/0002003663-26-000005-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/BRVE/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
