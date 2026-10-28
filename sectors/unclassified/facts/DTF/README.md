---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000879535
cik: 0000879535
company_name: DTF TAX-FREE INCOME 2028 TERM FUND INC
tickers:
- DTF
status: stub
canonical_reviewed: false
as_of: '2026-10-28'
updated_at: '2026-10-28T16:13:42.115634+00:00'
reviewed_at: null
coverage_release: coverage-20261028-40722802424-1
source_commit: 8a30d18f29f6ce6c61cbe955ca3f23f6f12ef180
financial_history_available: false
curated_research: null
financial_gap:
  reason: fund_reporting_review
  next_action: Review the instrument against its N-CSR/N-CSRS reporting evidence before
    applying an operating-company model. This signal alone is not a final fund classification.
  observed_forms:
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 40-17G
  - '5'
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DEFR14A
  - N-23C-2
  - N-23C-2/A
  - N-30D
  - N-CEN
  - N-CEN/A
  - N-CSR
  - N-CSR/A
  - N-CSRS
  - N-PX
  - N-PX/A
  - N-Q
  - NPORT-EX
  - NPORT-P
  - NPORT-P/A
  - NSAR-A
  - NSAR-B
  - NSAR-B/A
  - PRE 14A
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000879535.json
    sha256: 215dd2776e60f38e7c21b85398de56e0b107a04c2c837a611cfa3f65af5f27df
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000879535.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-28T16:09:02.154543+00:00'
  sha256: 9075fbed01d898a38c24f9b203cac1b6a4eed581edb2da888a321447f3bb55cc
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000879535.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 215dd2776e60f38e7c21b85398de56e0b107a04c2c837a611cfa3f65af5f27df
- id: S03
  title: NPORT-P 0000940400-26-038883
  url: https://www.sec.gov/Archives/edgar/data/879535/000094040026038883/0000940400-26-038883-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 40-17G 0001193125-26-395166
  url: https://www.sec.gov/Archives/edgar/data/879535/000119312526395166/0001193125-26-395166-index.html
  published_at: '2026-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: N-PX 0001193125-26-343953
  url: https://www.sec.gov/Archives/edgar/data/879535/000119312526343953/0001193125-26-343953-index.html
  published_at: '2026-08-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: N-CSRS 0001193125-26-292155
  url: https://www.sec.gov/Archives/edgar/data/879535/000119312526292155/0001193125-26-292155-index.html
  published_at: '2026-07-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: NPORT-P 0000940400-26-026149
  url: https://www.sec.gov/Archives/edgar/data/879535/000094040026026149/0000940400-26-026149-index.html
  published_at: '2026-06-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0000879535
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: DTF TAX-FREE INCOME 2028 TERM FUND INC
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 215dd2776e60f38e7c21b85398de56e0b107a04c2c837a611cfa3f65af5f27df
  url: https://data.sec.gov/submissions/CIK0000879535.json
listings:
- ticker: DTF
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-015150
  filed: '2026-01-16'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/879535/000119312526015150/0001193125-26-015150-index.html
research_progress:
  stage: pending
  input_sha256: dbfa444742091127b7ab5cc23ae5046fcfef0d085bfb1bf0c02c9a42157e3f66
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
  sic: null
  sic_description: ''
  rule_version: 1
  reason: Fund reporting signal requires instrument review before operating-sector
    classification.
full_history_url: https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/DTF/README.md
full_history_commit: 5da532c3abee5b40a5400c5864c6f3f4593276d7
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# DTF — DTF TAX-FREE INCOME 2028 TERM FUND INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/DTF/README.md)

## Business overview

Reported issuer name: **DTF TAX-FREE INCOME 2028 TERM FUND INC**. Stable SEC CIK: **0000879535**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| DTF | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

Not available: substantive research has not been completed. Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.

Navigation sector: **unclassified**. Method: `unresolved`. Fund reporting signal requires instrument review before operating-sector classification.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

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
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Review the instrument against its N-CSR/N-CSRS reporting evidence before applying an operating-company model. This signal alone is not a final fund classification.
- Forms observed in the retained filing inventory: 3, 3/A, 4, 4/A, 40-17G, 5, CORRESP, DEF 14A, DEFA14A, DEFR14A, N-23C-2, N-23C-2/A, N-30D, N-CEN, N-CEN/A, N-CSR, N-CSR/A, N-CSRS, N-PX, N-PX/A, N-Q, NPORT-EX, NPORT-P, NPORT-P/A, NSAR-A, NSAR-B, NSAR-B/A, PRE 14A, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SC TO-I, SC TO-I/A, SCHEDULE 13G, SCHEDULE 13G/A
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:29:53.896018+00:00.

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

Calculation gaps: Validated financial history is missing.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-29 | NPORT-P | 0000940400-26-038883 | — | [S03] |
| 2026-09-18 | 40-17G | 0001193125-26-395166 | — | [S04] |
| 2026-08-11 | N-PX | 0001193125-26-343953 | — | [S05] |
| 2026-07-01 | N-CSRS | 0001193125-26-292155 | — | [S06] |
| 2026-06-26 | NPORT-P | 0000940400-26-026149 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:02.154543+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000879535.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [NPORT-P 0000940400-26-038883](https://www.sec.gov/Archives/edgar/data/879535/000094040026038883/0000940400-26-038883-index.html) — published 2026-09-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [40-17G 0001193125-26-395166](https://www.sec.gov/Archives/edgar/data/879535/000119312526395166/0001193125-26-395166-index.html) — published 2026-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [N-PX 0001193125-26-343953](https://www.sec.gov/Archives/edgar/data/879535/000119312526343953/0001193125-26-343953-index.html) — published 2026-08-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [N-CSRS 0001193125-26-292155](https://www.sec.gov/Archives/edgar/data/879535/000119312526292155/0001193125-26-292155-index.html) — published 2026-07-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [NPORT-P 0000940400-26-026149](https://www.sec.gov/Archives/edgar/data/879535/000094040026026149/0000940400-26-026149-index.html) — published 2026-06-26; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261028-40722802424-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/5da532c3abee5b40a5400c5864c6f3f4593276d7/brain/companies/DTF/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
