---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001486298
cik: 0001486298
company_name: Blackstone Senior Floating Rate 2027 Term Fund
tickers:
- BSL
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 79ea404d09f86d838fefd71cf88a566d57bc57a2
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
  - 40-APP
  - 40-APP/A
  - 424B3
  - '497'
  - '5'
  - 8-A12B
  - 8-K
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - IRANNOTICE
  - N-2
  - N-2/A
  - N-23C-2
  - N-2MEF
  - N-8A
  - N-CEN
  - N-CSR
  - N-CSRS
  - N-CSRS/A
  - N-PX
  - N-Q
  - NPORT-EX
  - NPORT-P
  - NSAR-A
  - NSAR-A/A
  - NSAR-B
  - POS EX
  - PRE 14A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001486298.json
    sha256: 2f1dd0a34353d7773ce8c49d7d297a165da94d8f3d145d120d85b130d44e8937
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001486298.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-27T15:25:35.250901+00:00'
  sha256: 3e845dbd702671bbfbbc700f50d314d4d4cb439640ee0fe6fbf22fc3344c7f42
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001486298.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2f1dd0a34353d7773ce8c49d7d297a165da94d8f3d145d120d85b130d44e8937
- id: S03
  title: 40-17G 0001398344-26-017290
  url: https://www.sec.gov/Archives/edgar/data/1486298/000139834426017290/0001398344-26-017290-index.html
  published_at: '2026-09-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: N-CSRS 0001398344-26-016702
  url: https://www.sec.gov/Archives/edgar/data/1486298/000139834426016702/0001398344-26-016702-index.html
  published_at: '2026-09-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: NPORT-P 0001049169-26-002105
  url: https://www.sec.gov/Archives/edgar/data/1486298/000104916926002105/0001049169-26-002105-index.html
  published_at: '2026-08-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: N-PX 0001398344-26-013256
  url: https://www.sec.gov/Archives/edgar/data/1486298/000139834426013256/0001398344-26-013256-index.html
  published_at: '2026-07-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: SCHEDULE 13G 0000897101-26-000298
  url: https://www.sec.gov/Archives/edgar/data/1486298/000089710126000298/0000897101-26-000298-index.html
  published_at: '2026-07-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001486298
  classification_status: missing_or_invalid_sic
  entity_type: other
  name: Blackstone Senior Floating Rate 2027 Term Fund
  sic: null
  sic_description: ''
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 2f1dd0a34353d7773ce8c49d7d297a165da94d8f3d145d120d85b130d44e8937
  url: https://data.sec.gov/submissions/CIK0001486298.json
listings:
- ticker: BSL
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001398344-26-003958
  filed: '2026-02-27'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1486298/000139834426003958/0001398344-26-003958-index.html
- accession: 0001193125-20-044343
  filed: '2020-02-21'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1486298/000119312520044343/0001193125-20-044343-index.html
research_progress:
  stage: pending
  input_sha256: 79e2bba2c9d03ac2394a923b4519e5e2cfb064ba86399f26b43d3f010ba05cb6
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/BSL/README.md
full_history_commit: ea9dd09e5d047ff0620d4500849876915bb10e87
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# BSL — Blackstone Senior Floating Rate 2027 Term Fund

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/BSL/README.md)

## Business overview

Reported issuer name: **Blackstone Senior Floating Rate 2027 Term Fund**. Stable SEC CIK: **0001486298**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BSL | NYSE | common_stock | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 3, 3/A, 4, 4/A, 40-17G, 40-APP, 40-APP/A, 424B3, 497, 5, 8-A12B, 8-K, CORRESP, DEF 14A, DEFA14A, EFFECT, IRANNOTICE, N-2, N-2/A, N-23C-2, N-2MEF, N-8A, N-CEN, N-CSR, N-CSRS, N-CSRS/A, N-PX, N-Q, NPORT-EX, NPORT-P, NSAR-A, NSAR-A/A, NSAR-B, POS EX, PRE 14A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:33:36.824344+00:00.

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
| 2026-09-22 | 40-17G | 0001398344-26-017290 | — | [S03] |
| 2026-09-04 | N-CSRS | 0001398344-26-016702 | — | [S04] |
| 2026-08-27 | NPORT-P | 0001049169-26-002105 | — | [S05] |
| 2026-07-31 | N-PX | 0001398344-26-013256 | — | [S06] |
| 2026-07-06 | SCHEDULE 13G | 0000897101-26-000298 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:35.250901+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001486298.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [40-17G 0001398344-26-017290](https://www.sec.gov/Archives/edgar/data/1486298/000139834426017290/0001398344-26-017290-index.html) — published 2026-09-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [N-CSRS 0001398344-26-016702](https://www.sec.gov/Archives/edgar/data/1486298/000139834426016702/0001398344-26-016702-index.html) — published 2026-09-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [NPORT-P 0001049169-26-002105](https://www.sec.gov/Archives/edgar/data/1486298/000104916926002105/0001049169-26-002105-index.html) — published 2026-08-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [N-PX 0001398344-26-013256](https://www.sec.gov/Archives/edgar/data/1486298/000139834426013256/0001398344-26-013256-index.html) — published 2026-07-31; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [SCHEDULE 13G 0000897101-26-000298](https://www.sec.gov/Archives/edgar/data/1486298/000089710126000298/0000897101-26-000298-index.html) — published 2026-07-06; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/BSL/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
