---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001224450
cik: '0001224450'
company_name: COHEN & STEERS REIT & PREFERRED & INCOME FUND INC
tickers:
- RNP
status: stub
canonical_reviewed: false
as_of: '2026-10-25'
updated_at: '2026-10-25T13:50:29.910841+00:00'
reviewed_at: null
coverage_release: coverage-20261025-40199010718-1
source_commit: f5f88011907841550f3cf7652c3822295b45cb57
financial_history_available: false
curated_research: null
financial_gap:
  reason: fund_reporting_review
  next_action: Review the instrument against its N-CSR/N-CSRS reporting evidence before
    applying an operating-company model. This signal alone is not a final fund classification.
  observed_forms:
  - '3'
  - '4'
  - 4/A
  - 40-17G
  - 40-6C
  - 40-6C/A
  - 40-APP
  - 40-APP/A
  - '497'
  - '5'
  - 8-A12B
  - 8-K
  - CERTNYS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - N-2
  - N-2/A
  - N-23C-2
  - N-23C-2/A
  - N-30B-2
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
  - NSAR-B/A
  - NT-NSAR
  - POS EX
  - PRE 14A
  - SC 13G
  - SC 13G/A
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001224450.json
    sha256: 89be865cc6a1f7f240c85c5565d3262e9643049d56f977988a99b0cc30150cb1
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001224450.json
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
  url: https://data.sec.gov/submissions/CIK0001224450.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 89be865cc6a1f7f240c85c5565d3262e9643049d56f977988a99b0cc30150cb1
- id: S03
  title: N-CSRS 0001193125-26-383116
  url: https://www.sec.gov/Archives/edgar/data/1224450/000119312526383116/0001193125-26-383116-index.html
  published_at: '2026-09-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: N-PX 0001193125-26-376006
  url: https://www.sec.gov/Archives/edgar/data/1224450/000119312526376006/0001193125-26-376006-index.html
  published_at: '2026-08-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: NPORT-P 0001410368-26-088058
  url: https://www.sec.gov/Archives/edgar/data/1224450/000141036826088058/0001410368-26-088058-index.html
  published_at: '2026-08-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 3 0001193125-26-341642
  url: https://www.sec.gov/Archives/edgar/data/1224450/000119312526341642/0001193125-26-341642-index.html
  published_at: '2026-08-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: NPORT-P 0001410368-26-056224
  url: https://www.sec.gov/Archives/edgar/data/1224450/000141036826056224/0001410368-26-056224-index.html
  published_at: '2026-05-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001224450'
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: COHEN & STEERS REIT & PREFERRED & INCOME FUND INC
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 89be865cc6a1f7f240c85c5565d3262e9643049d56f977988a99b0cc30150cb1
  url: https://data.sec.gov/submissions/CIK0001224450.json
listings:
- ticker: RNP
  exchange: NYSE
  instrument_type: preferred
research_filings:
- accession: 0001193125-26-090317
  filed: '2026-03-04'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1224450/000119312526090317/0001193125-26-090317-index.html
- accession: 0001193125-23-075486
  filed: '2023-03-21'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1224450/000119312523075486/0001193125-23-075486-index.html
research_progress:
  stage: pending
  input_sha256: 87627cd5e1d44f516350f4abbe567580ec66e32666d38c7c131127604919d77c
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/RNP/README.md
full_history_commit: 71fcd4775048604503d616351f7f309068b23e1b
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# RNP — COHEN & STEERS REIT & PREFERRED & INCOME FUND INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/RNP/README.md)

## Business overview

Reported issuer name: **COHEN & STEERS REIT & PREFERRED & INCOME FUND INC**. Stable SEC CIK: **0001224450**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| RNP | NYSE | preferred | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 3, 4, 4/A, 40-17G, 40-6C, 40-6C/A, 40-APP, 40-APP/A, 497, 5, 8-A12B, 8-K, CERTNYS, CORRESP, DEF 14A, DEFA14A, N-2, N-2/A, N-23C-2, N-23C-2/A, N-30B-2, N-8A, N-CEN, N-CSR, N-CSRS, N-PX, N-Q, NPORT-EX, NPORT-P, NSAR-A, NSAR-B, NSAR-B/A, NT-NSAR, POS EX, PRE 14A, SC 13G, SC 13G/A
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:11.538783+00:00.

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
| 2026-09-04 | N-CSRS | 0001193125-26-383116 | — | [S03] |
| 2026-08-31 | N-PX | 0001193125-26-376006 | — | [S04] |
| 2026-08-28 | NPORT-P | 0001410368-26-088058 | — | [S05] |
| 2026-08-10 | 3 | 0001193125-26-341642 | — | [S06] |
| 2026-05-29 | NPORT-P | 0001410368-26-056224 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:48.334682+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001224450.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [N-CSRS 0001193125-26-383116](https://www.sec.gov/Archives/edgar/data/1224450/000119312526383116/0001193125-26-383116-index.html) — published 2026-09-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [N-PX 0001193125-26-376006](https://www.sec.gov/Archives/edgar/data/1224450/000119312526376006/0001193125-26-376006-index.html) — published 2026-08-31; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [NPORT-P 0001410368-26-088058](https://www.sec.gov/Archives/edgar/data/1224450/000141036826088058/0001410368-26-088058-index.html) — published 2026-08-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [3 0001193125-26-341642](https://www.sec.gov/Archives/edgar/data/1224450/000119312526341642/0001193125-26-341642-index.html) — published 2026-08-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [NPORT-P 0001410368-26-056224](https://www.sec.gov/Archives/edgar/data/1224450/000141036826056224/0001410368-26-056224-index.html) — published 2026-05-29; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/RNP/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
