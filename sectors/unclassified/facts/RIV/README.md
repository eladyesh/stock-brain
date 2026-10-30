---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001501072
cik: '0001501072'
company_name: RIVERNORTH OPPORTUNITIES FUND, INC.
tickers:
- RIV
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: ef2ed016c2c344c23ee7fb991b25bf93660da77e
financial_history_available: false
curated_research: null
financial_gap:
  reason: fund_reporting_review
  next_action: Review the instrument against its N-CSR/N-CSRS reporting evidence before
    applying an operating-company model. This signal alone is not a final fund classification.
  observed_forms:
  - '144'
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 40-17G
  - 40-APP
  - 40-APP/A
  - 424B2
  - 424B3
  - 424B5
  - '497'
  - 497AD
  - '5'
  - 8-A12B
  - 8-K
  - CERT
  - CORRESP
  - D
  - DEF 14A
  - DEFA14A
  - EFFECT
  - FWP
  - N-2
  - N-2/A
  - N-8A
  - N-CEN
  - N-CSR
  - N-CSRS
  - N-PX
  - N-Q
  - NPORT-EX
  - NPORT-P
  - NSAR-A
  - NSAR-B
  - POS 8C
  - POS EX
  - PRE 14A
  - SC 13D
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001501072.json
    sha256: 73c96538281b82cbe27b5633212bf2a4d10a25957e155abe20dca8112e87e847
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001501072.json
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
  url: https://data.sec.gov/submissions/CIK0001501072.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 73c96538281b82cbe27b5633212bf2a4d10a25957e155abe20dca8112e87e847
- id: S03
  title: SCHEDULE 13G 0001333986-26-000050
  url: https://www.sec.gov/Archives/edgar/data/1501072/000133398626000050/0001333986-26-000050-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: SCHEDULE 13G 0001109448-26-000284
  url: https://www.sec.gov/Archives/edgar/data/1501072/000110944826000284/0001109448-26-000284-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001398344-26-017885
  url: https://www.sec.gov/Archives/edgar/data/1501072/000139834426017885/0001398344-26-017885-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001398344-26-017874
  url: https://www.sec.gov/Archives/edgar/data/1501072/000139834426017874/0001398344-26-017874-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001398344-26-017872
  url: https://www.sec.gov/Archives/edgar/data/1501072/000139834426017872/0001398344-26-017872-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001501072'
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: RIVERNORTH OPPORTUNITIES FUND, INC.
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 73c96538281b82cbe27b5633212bf2a4d10a25957e155abe20dca8112e87e847
  url: https://data.sec.gov/submissions/CIK0001501072.json
listings:
- ticker: RIV
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001398344-26-015282
  filed: '2026-08-21'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1501072/000139834426015282/0001398344-26-015282-index.html
- accession: 0001398344-26-017220
  filed: '2026-09-18'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1501072/000139834426017220/0001398344-26-017220-index.html
research_progress:
  stage: pending
  input_sha256: dd3eda9c3f9ce19258f69e57f09e8b534b2c1f522d44c3b6b2be3e721f583fd3
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/RIV/README.md
full_history_commit: 79888139fa1fe8ad3404e6bc04e318eee1474f73
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# RIV — RIVERNORTH OPPORTUNITIES FUND, INC.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/RIV/README.md)

## Business overview

Reported issuer name: **RIVERNORTH OPPORTUNITIES FUND, INC.**. Stable SEC CIK: **0001501072**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| RIV | NYSE | common_stock | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 144, 3, 3/A, 4, 4/A, 40-17G, 40-APP, 40-APP/A, 424B2, 424B3, 424B5, 497, 497AD, 5, 8-A12B, 8-K, CERT, CORRESP, D, DEF 14A, DEFA14A, EFFECT, FWP, N-2, N-2/A, N-8A, N-CEN, N-CSR, N-CSRS, N-PX, N-Q, NPORT-EX, NPORT-P, NSAR-A, NSAR-B, POS 8C, POS EX, PRE 14A, SC 13D, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:33:43.188532+00:00.

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
| 2026-10-09 | SCHEDULE 13G | 0001333986-26-000050 | — | [S03] |
| 2026-10-09 | SCHEDULE 13G | 0001109448-26-000284 | — | [S04] |
| 2026-10-05 | 4 | 0001398344-26-017885 | — | [S05] |
| 2026-10-05 | 4 | 0001398344-26-017874 | — | [S06] |
| 2026-10-05 | 4 | 0001398344-26-017872 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001501072.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SCHEDULE 13G 0001333986-26-000050](https://www.sec.gov/Archives/edgar/data/1501072/000133398626000050/0001333986-26-000050-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [SCHEDULE 13G 0001109448-26-000284](https://www.sec.gov/Archives/edgar/data/1501072/000110944826000284/0001109448-26-000284-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001398344-26-017885](https://www.sec.gov/Archives/edgar/data/1501072/000139834426017885/0001398344-26-017885-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001398344-26-017874](https://www.sec.gov/Archives/edgar/data/1501072/000139834426017874/0001398344-26-017874-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001398344-26-017872](https://www.sec.gov/Archives/edgar/data/1501072/000139834426017872/0001398344-26-017872-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/79888139fa1fe8ad3404e6bc04e318eee1474f73/brain/companies/RIV/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
