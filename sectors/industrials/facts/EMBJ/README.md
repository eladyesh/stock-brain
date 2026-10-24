---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001355444
cik: '0001355444'
company_name: EMBRAER S.A.
tickers:
- EMBJ
status: stub
canonical_reviewed: false
as_of: '2026-10-24'
updated_at: '2026-10-24T13:37:20.730682+00:00'
reviewed_at: null
coverage_release: coverage-20261024-40097864335-1
source_commit: 88540b30f4be3c56b6c7fa8ba3dede59893b9834
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 15-12B
  - 20-F
  - 20-F/A
  - '25'
  - '3'
  - '4'
  - 4/A
  - 424B2
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CERTNYS
  - CORRESP
  - EFFECT
  - F-3/A
  - F-3ASR
  - F-4
  - F-6 POS
  - FWP
  - POSASR
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001355444.json
    sha256: d34cabda5071029012e95f8777376ceacaa92cf84e53da3327368d25d5cd1fa0
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001355444.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-24T13:23:33.193038+00:00'
  sha256: 94335ed3f4abc4bbd58a4415d105d453184f5484eaf6a2884d1bfb0120d850c9
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001355444.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d34cabda5071029012e95f8777376ceacaa92cf84e53da3327368d25d5cd1fa0
- id: S03
  title: 6-K 0001292814-26-004988
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281426004988/0001292814-26-004988-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001292814-26-004832
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281426004832/0001292814-26-004832-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001292814-26-004774
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281426004774/0001292814-26-004774-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001292814-26-004766
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281426004766/0001292814-26-004766-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 3 0001292814-26-004534
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281426004534/0001292814-26-004534-index.html
  published_at: '2026-09-11'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
issuer_classification:
  cik: '0001355444'
  classification_status: reported_sic
  entity_type: other
  name: EMBRAER S.A.
  sic: '3721'
  sic_description: Aircraft
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d34cabda5071029012e95f8777376ceacaa92cf84e53da3327368d25d5cd1fa0
  url: https://data.sec.gov/submissions/CIK0001355444.json
listings:
- ticker: EMBJ
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-021824
  filed: '2026-03-30'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1355444/000162828026021824/0001628280-26-021824-index.html
- accession: 0001144204-07-064175
  filed: '2007-11-26'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1355444/000114420407064175/0001144204-07-064175-index.html
- accession: 0001292814-26-004988
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281426004988/0001292814-26-004988-index.html
- accession: 0001292814-26-002179
  filed: '2026-04-09'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281426002179/0001292814-26-002179-index.html
- accession: 0001292814-25-002891
  filed: '2025-08-06'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281425002891/0001292814-25-002891-index.html
- accession: 0001292814-24-003855
  filed: '2024-10-25'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281424003855/0001292814-24-003855-index.html
- accession: 0001292814-24-003817
  filed: '2024-10-22'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281424003817/0001292814-24-003817-index.html
- accession: 0001193125-17-028382
  filed: '2017-02-02'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1355444/000119312517028382/0001193125-17-028382-index.html
- accession: 0001292814-16-006373
  filed: '2016-10-24'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281416006373/0001292814-16-006373-index.html
- accession: 0001292814-16-005467
  filed: '2016-07-29'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1355444/000129281416005467/0001292814-16-005467-index.html
- accession: 0001193125-10-233750
  filed: '2010-10-21'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1355444/000119312510233750/0001193125-10-233750-index.html
research_progress:
  stage: pending
  input_sha256: 3f2dd74e4bb49c97a9024d9174e1c5e85aade0645006f9855e5e1f0b6cc7e49b
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
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
  source_url: https://data.sec.gov/submissions/CIK0001355444.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/EMBJ/README.md
full_history_commit: aad7b261e69b9f214b9c5e20228523ca644ed670
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# EMBJ — EMBRAER S.A.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/EMBJ/README.md)

## Business overview

Reported issuer name: **EMBRAER S.A.**. Stable SEC CIK: **0001355444**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| EMBJ | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3721**: Aircraft. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 15-12B, 20-F, 20-F/A, 25, 3, 4, 4/A, 424B2, 6-K, 6-K/A, 8-A12B, CERT, CERTNYS, CORRESP, EFFECT, F-3/A, F-3ASR, F-4, F-6 POS, FWP, POSASR, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:46.160476+00:00.

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
| 2026-10-23 | 6-K | 0001292814-26-004988 | — | [S03] |
| 2026-10-02 | 6-K | 0001292814-26-004832 | — | [S04] |
| 2026-10-01 | 6-K | 0001292814-26-004774 | — | [S05] |
| 2026-10-01 | 6-K | 0001292814-26-004766 | — | [S06] |
| 2026-09-11 | 3 | 0001292814-26-004534 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-24T13:23:33.193038+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001355444.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001292814-26-004988](https://www.sec.gov/Archives/edgar/data/1355444/000129281426004988/0001292814-26-004988-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001292814-26-004832](https://www.sec.gov/Archives/edgar/data/1355444/000129281426004832/0001292814-26-004832-index.html) — published 2026-10-02; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001292814-26-004774](https://www.sec.gov/Archives/edgar/data/1355444/000129281426004774/0001292814-26-004774-index.html) — published 2026-10-01; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001292814-26-004766](https://www.sec.gov/Archives/edgar/data/1355444/000129281426004766/0001292814-26-004766-index.html) — published 2026-10-01; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [3 0001292814-26-004534](https://www.sec.gov/Archives/edgar/data/1355444/000129281426004534/0001292814-26-004534-index.html) — published 2026-09-11; retrieved 2026-10-24T13:22:51.759433+00:00.

Source release: `coverage-20261024-40097864335-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/aad7b261e69b9f214b9c5e20228523ca644ed670/brain/companies/EMBJ/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
