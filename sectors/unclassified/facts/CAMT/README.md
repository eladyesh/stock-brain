---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001109138
cik: 0001109138
company_name: CAMTEK LTD
tickers:
- CAMT
status: stub
canonical_reviewed: false
as_of: '2026-10-24'
updated_at: '2026-10-24T13:37:20.730682+00:00'
reviewed_at: null
coverage_release: coverage-20261024-40097864335-1
source_commit: 3e64e295ca76808fce5a42e3e525d15ea101c1a7
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '144'
  - 144/A
  - 20-F
  - 20-F/A
  - '3'
  - '4'
  - 424B1
  - 424B3
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12G
  - CORRESP
  - D
  - DEF 14A
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - POS AM
  - RW
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001109138.json
    sha256: d8d48f2eff3ecd8ae8a3e58cd86c46753bbcc9b36ea2eab7bddf72ba9737463d
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001109138.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-24T13:23:32.568444+00:00'
  sha256: 59ac9b74ff663c6de40f5c93a54d5e12eb3fbef74f82e8a7cfc1456ad9f969ec
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001109138.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d8d48f2eff3ecd8ae8a3e58cd86c46753bbcc9b36ea2eab7bddf72ba9737463d
- id: S03
  title: SCHEDULE 13G/A 0001178913-26-004806
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891326004806/0001178913-26-004806-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: SCHEDULE 13G/A 0001178913-26-004788
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891326004788/0001178913-26-004788-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: SCHEDULE 13G 0001178913-26-004782
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891326004782/0001178913-26-004782-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001178913-26-004769
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891326004769/0001178913-26-004769-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001178913-26-004767
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891326004767/0001178913-26-004767-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001109138
  classification_status: reported_sic
  entity_type: other
  name: CAMTEK LTD
  sic: '3827'
  sic_description: Optical Instruments & Lenses
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d8d48f2eff3ecd8ae8a3e58cd86c46753bbcc9b36ea2eab7bddf72ba9737463d
  url: https://data.sec.gov/submissions/CIK0001109138.json
listings:
- ticker: CAMT
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001178913-26-001561
  filed: '2026-03-19'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891326001561/0001178913-26-001561-index.html
- accession: 0001178913-17-000815
  filed: '2017-03-20'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891317000815/0001178913-17-000815-index.html
- accession: 0001178913-09-002657
  filed: '2009-11-09'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891309002657/0001178913-09-002657-index.html
- accession: 0001178913-09-002655
  filed: '2009-11-09'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891309002655/0001178913-09-002655-index.html
- accession: 0001178913-09-001926
  filed: '2009-08-13'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891309001926/0001178913-09-001926-index.html
- accession: 0001178913-26-004769
  filed: '2026-10-14'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891326004769/0001178913-26-004769-index.html
- accession: 0001178913-19-001525
  filed: '2019-05-16'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891319001525/0001178913-19-001525-index.html
- accession: 0001178913-18-002508
  filed: '2018-09-10'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891318002508/0001178913-18-002508-index.html
- accession: 0001178913-18-001840
  filed: '2018-06-04'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891318001840/0001178913-18-001840-index.html
- accession: 0001178913-18-001753
  filed: '2018-05-24'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891318001753/0001178913-18-001753-index.html
- accession: 0001178913-18-001723
  filed: '2018-05-22'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891318001723/0001178913-18-001723-index.html
- accession: 0001178913-18-001451
  filed: '2018-05-04'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1109138/000117891318001451/0001178913-18-001451-index.html
research_progress:
  stage: pending
  input_sha256: f2dea4f3c26a1347cfcf7f6779485d7a9d0b0040e3c0f79061a9f763c596c5be
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
  sic: '3827'
  sic_description: Optical Instruments & Lenses
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/2290c5ee6e95b7aeba999ae4c943952901c7c78d/brain/companies/CAMT/README.md
full_history_commit: 2290c5ee6e95b7aeba999ae4c943952901c7c78d
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# CAMT — CAMTEK LTD

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/2290c5ee6e95b7aeba999ae4c943952901c7c78d/brain/companies/CAMT/README.md)

## Business overview

Reported issuer name: **CAMTEK LTD**. Stable SEC CIK: **0001109138**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| CAMT | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3827**: Optical Instruments & Lenses. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **unclassified**. Method: `unresolved`. Missing, ambiguous or unmapped reported industry; company-specific review is required.

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
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 144/A, 20-F, 20-F/A, 3, 4, 424B1, 424B3, 424B5, 6-K, 6-K/A, 8-A12G, CORRESP, D, DEF 14A, EFFECT, F-1, F-1/A, F-3, F-3/A, POS AM, RW, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:31:42.845307+00:00.

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
| 2026-10-20 | SCHEDULE 13G/A | 0001178913-26-004806 | — | [S03] |
| 2026-10-19 | SCHEDULE 13G/A | 0001178913-26-004788 | — | [S04] |
| 2026-10-19 | SCHEDULE 13G | 0001178913-26-004782 | — | [S05] |
| 2026-10-14 | 6-K | 0001178913-26-004769 | — | [S06] |
| 2026-10-14 | 6-K | 0001178913-26-004767 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-24T13:23:32.568444+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001109138.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SCHEDULE 13G/A 0001178913-26-004806](https://www.sec.gov/Archives/edgar/data/1109138/000117891326004806/0001178913-26-004806-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [SCHEDULE 13G/A 0001178913-26-004788](https://www.sec.gov/Archives/edgar/data/1109138/000117891326004788/0001178913-26-004788-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [SCHEDULE 13G 0001178913-26-004782](https://www.sec.gov/Archives/edgar/data/1109138/000117891326004782/0001178913-26-004782-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001178913-26-004769](https://www.sec.gov/Archives/edgar/data/1109138/000117891326004769/0001178913-26-004769-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001178913-26-004767](https://www.sec.gov/Archives/edgar/data/1109138/000117891326004767/0001178913-26-004767-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261024-40097864335-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/2290c5ee6e95b7aeba999ae4c943952901c7c78d/brain/companies/CAMT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
