---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000899715
cik: 0000899715
company_name: TANGER INC.
tickers:
- SKT
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: f9a34108789a82bf7c75f9d65a0e9552aa5552db
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
  - 10-Q/A
  - '144'
  - 144/A
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B5
  - 424B7
  - '5'
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - FWP
  - S-3ASR
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000899715.json
    sha256: 07d1b37c4ef7072f7602898f27fbdb23b7807841989c9dc5606a6e3bb77d0c2a
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0000899715.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0000899715.json
    sha256: 2982097d8420c3fe8eebec72c79ae942462dc85ae9bdf822280a4242bcb76156
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000899715.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:12.358089+00:00'
  sha256: a960a0bfc5439fac9e467fe07ef1f44afe893ba2afc3297648321a80ce09971e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000899715.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2982097d8420c3fe8eebec72c79ae942462dc85ae9bdf822280a4242bcb76156
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0000899715.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 07d1b37c4ef7072f7602898f27fbdb23b7807841989c9dc5606a6e3bb77d0c2a
- id: S04
  title: 10-Q 0001628280-26-053864
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026053864/0001628280-26-053864-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S16
  title: 4 0001628280-26-065147
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026065147/0001628280-26-065147-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S17
  title: 4 0001628280-26-057367
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026057367/0001628280-26-057367-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 10-Q 0001628280-26-053864
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026053864/0001628280-26-053864-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: SCHEDULE 13G/A 0000315066-26-002147
  url: https://www.sec.gov/Archives/edgar/data/899715/000031506626002147/0000315066-26-002147-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 8-K 0001628280-26-052544
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026052544/0001628280-26-052544-index.html
  published_at: '2026-08-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000899715
  classification_status: reported_sic
  entity_type: operating
  name: TANGER INC.
  sic: '6798'
  sic_description: Real Estate Investment Trusts
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2982097d8420c3fe8eebec72c79ae942462dc85ae9bdf822280a4242bcb76156
  url: https://data.sec.gov/submissions/CIK0000899715.json
listings:
- ticker: SKT
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-012252
  filed: '2026-02-26'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026012252/0001628280-26-012252-index.html
- accession: 0001628280-26-053864
  filed: '2026-08-06'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026053864/0001628280-26-053864-index.html
- accession: 0001628280-26-021249
  filed: '2026-03-26'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026021249/0001628280-26-021249-index.html
- accession: 0001628280-26-052544
  filed: '2026-08-04'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/899715/000162828026052544/0001628280-26-052544-index.html
- accession: 0000899715-21-000176
  filed: '2021-09-10'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/899715/000089971521000176/0000899715-21-000176-index.html
- accession: 0000899715-21-000124
  filed: '2021-04-06'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/899715/000089971521000124/0000899715-21-000124-index.html
- accession: 0000899715-18-000066
  filed: '2018-02-21'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/899715/000089971518000066/0000899715-18-000066-index.html
- accession: 0000899715-18-000024
  filed: '2018-02-14'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/899715/000089971518000024/0000899715-18-000024-index.html
- accession: 0000899715-17-000132
  filed: '2017-09-29'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/899715/000089971517000132/0000899715-17-000132-index.html
- accession: 0000899715-16-000282
  filed: '2016-03-02'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/899715/000089971516000282/0000899715-16-000282-index.html
- accession: 0000899715-16-000271
  filed: '2016-02-29'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/899715/000089971516000271/0000899715-16-000271-index.html
- accession: 0000899715-13-000134
  filed: '2013-11-12'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/899715/000089971513000134/0000899715-13-000134-index.html
research_progress:
  stage: pending
  input_sha256: 9936c831fb9f12bc5f037960fa8516d33a4e8724b42a66d4a236be551650e809
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: unclassified
  method: unresolved
  sic: '6798'
  sic_description: Real Estate Investment Trusts
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/SKT/README.md
full_history_commit: 1b4771bc41dec553e210323f72d9bfc908288c04
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SKT — TANGER INC.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/SKT/README.md)

## Business overview

Reported issuer name: **TANGER INC.**. Stable SEC CIK: **0000899715**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SKT | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6798**: Real Estate Investment Trusts. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **unclassified**. Method: `unresolved`. Missing, ambiguous or unmapped reported industry; company-specific review is required.

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
| net_income_including_noncontrolling_interests | Unavailable / blocked | USD | US GAAP / reported / not model usable | ProfitLoss; missing_annual_anchor | [S04] |
| operating_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| operating_income | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, definition_changed_across_series, missing_annual_anchor | [S04] |
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
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermDebt; debt_scope_requires_filing_review, missing_annual_anchor | [S04] |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; missing_annual_anchor, share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; missing_annual_anchor | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / reported / not model usable | ShortTermInvestments; missing_annual_anchor | [S04] |



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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:30:13.455194+00:00.

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
| 2026-10-05 | 4 | 0001628280-26-065147 | — | [S16] |
| 2026-08-17 | 4 | 0001628280-26-057367 | — | [S17] |
| 2026-08-06 | 10-Q | 0001628280-26-053864 | — | [S18] |
| 2026-08-06 | SCHEDULE 13G/A | 0000315066-26-002147 | — | [S19] |
| 2026-08-04 | 8-K | 0001628280-26-052544 | — | [S20] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000899715.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0000899715.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-Q 0001628280-26-053864](https://www.sec.gov/Archives/edgar/data/899715/000162828026053864/0001628280-26-053864-index.html) — published 2026-08-06; retrieved 2026-10-22T17:39:41.848518+00:00.

[S16] [4 0001628280-26-065147](https://www.sec.gov/Archives/edgar/data/899715/000162828026065147/0001628280-26-065147-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S17] [4 0001628280-26-057367](https://www.sec.gov/Archives/edgar/data/899715/000162828026057367/0001628280-26-057367-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [10-Q 0001628280-26-053864](https://www.sec.gov/Archives/edgar/data/899715/000162828026053864/0001628280-26-053864-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [SCHEDULE 13G/A 0000315066-26-002147](https://www.sec.gov/Archives/edgar/data/899715/000031506626002147/0000315066-26-002147-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [8-K 0001628280-26-052544](https://www.sec.gov/Archives/edgar/data/899715/000162828026052544/0001628280-26-052544-index.html) — published 2026-08-04; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/SKT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
