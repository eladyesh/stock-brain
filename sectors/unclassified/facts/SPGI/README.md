---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000064040
cik: '0000064040'
company_name: S&P Global Inc.
tickers:
- SPGI
status: stub
canonical_reviewed: false
as_of: '2026-10-26'
updated_at: '2026-10-26T16:16:21.148680+00:00'
reviewed_at: null
coverage_release: coverage-20261026-40356450615-1
source_commit: ffd7836f4c177b9a174b16eab4288980decb7e24
financial_history_available: false
curated_research: null
financial_gap:
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-Q
  - 11-K
  - '144'
  - 15-12B
  - '3'
  - 3/A
  - '4'
  - 424B2
  - 424B3
  - 424B5
  - '425'
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - FWP
  - IRANNOTICE
  - POS AM
  - PRE 14A
  - PX14A6G
  - S-3ASR
  - S-4
  - S-4/A
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000064040.json
    sha256: 12197d15423e02c01481847fae9e9c7809b4c532afdf4270822502c4d68ce9c8
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0000064040.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-26T16:11:31.806354+00:00'
  sha256: 13932af456c860d259c16604472ab685dab69d880fb71eb6d5b53159497eb520
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0000064040.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 12197d15423e02c01481847fae9e9c7809b4c532afdf4270822502c4d68ce9c8
- id: S03
  title: S-3ASR 0001104659-26-118287
  url: https://www.sec.gov/Archives/edgar/data/64040/000110465926118287/0001104659-26-118287-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 8-K 0000064040-26-000049
  url: https://www.sec.gov/Archives/edgar/data/64040/000006404026000049/0000064040-26-000049-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 3 0001969228-26-000003
  url: https://www.sec.gov/Archives/edgar/data/64040/000196922826000003/0001969228-26-000003-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 4 0002043271-26-000008
  url: https://www.sec.gov/Archives/edgar/data/64040/000204327126000008/0002043271-26-000008-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 4 0002142367-26-000004
  url: https://www.sec.gov/Archives/edgar/data/64040/000214236726000004/0002142367-26-000004-index.html
  published_at: '2026-08-04'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
issuer_classification:
  cik: '0000064040'
  classification_status: reported_sic
  entity_type: operating
  name: S&P Global Inc.
  sic: '7320'
  sic_description: Services-Consumer Credit Reporting, Collection Agencies
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 12197d15423e02c01481847fae9e9c7809b4c532afdf4270822502c4d68ce9c8
  url: https://data.sec.gov/submissions/CIK0000064040.json
listings:
- ticker: SPGI
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0000064040-26-000013
  filed: '2026-02-11'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/64040/000006404026000013/0000064040-26-000013-index.html
- accession: 0000064040-26-000045
  filed: '2026-07-28'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/64040/000006404026000045/0000064040-26-000045-index.html
- accession: 0001104659-26-037380
  filed: '2026-03-31'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/64040/000110465926037380/0001104659-26-037380-index.html
- accession: 0000064040-26-000049
  filed: '2026-10-23'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/64040/000006404026000049/0000064040-26-000049-index.html
- accession: 0001104659-26-080571
  filed: '2026-07-06'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/64040/000110465926080571/0001104659-26-080571-index.html
- accession: 0000064040-26-000004
  filed: '2026-01-14'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/64040/000006404026000004/0000064040-26-000004-index.html
- accession: 0000064040-24-000067
  filed: '2024-02-08'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/64040/000006404024000067/0000064040-24-000067-index.html
- accession: 0000064040-22-000107
  filed: '2022-05-03'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/64040/000006404022000107/0000064040-22-000107-index.html
- accession: 0001193125-22-064702
  filed: '2022-03-04'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/64040/000119312522064702/0001193125-22-064702-index.html
- accession: 0001193125-22-023508
  filed: '2022-01-31'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/64040/000119312522023508/0001193125-22-023508-index.html
- accession: 0000950103-18-006512
  filed: '2018-05-24'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/64040/000095010318006512/0000950103-18-006512-index.html
research_progress:
  stage: pending
  input_sha256: 8f5fc534439e9520d1dcf6f07a5b88f527fbbd14a6afb615939adfdcfaa190d0
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
  sic: '7320'
  sic_description: Services-Consumer Credit Reporting, Collection Agencies
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/SPGI/README.md
full_history_commit: 6ec0c5a139b27efe3be9111dc20cf938bd839c1e
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SPGI — S&P Global Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/SPGI/README.md)

## Business overview

Reported issuer name: **S&P Global Inc.**. Stable SEC CIK: **0000064040**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SPGI | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7320**: Services-Consumer Credit Reporting, Collection Agencies. [S02]

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
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-K, 10-Q, 11-K, 144, 15-12B, 3, 3/A, 4, 424B2, 424B3, 424B5, 425, 8-K, 8-K/A, ARS, CORRESP, DEF 14A, DEFA14A, EFFECT, FWP, IRANNOTICE, POS AM, PRE 14A, PX14A6G, S-3ASR, S-4, S-4/A, S-8, S-8 POS, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:27:47.983542+00:00.

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
| 2026-10-23 | S-3ASR | 0001104659-26-118287 | — | [S03] |
| 2026-10-23 | 8-K | 0000064040-26-000049 | — | [S04] |
| 2026-10-19 | 3 | 0001969228-26-000003 | — | [S05] |
| 2026-10-05 | 4 | 0002043271-26-000008 | — | [S06] |
| 2026-08-04 | 4 | 0002142367-26-000004 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.806354+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000064040.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [S-3ASR 0001104659-26-118287](https://www.sec.gov/Archives/edgar/data/64040/000110465926118287/0001104659-26-118287-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [8-K 0000064040-26-000049](https://www.sec.gov/Archives/edgar/data/64040/000006404026000049/0000064040-26-000049-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [3 0001969228-26-000003](https://www.sec.gov/Archives/edgar/data/64040/000196922826000003/0001969228-26-000003-index.html) — published 2026-10-19; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [4 0002043271-26-000008](https://www.sec.gov/Archives/edgar/data/64040/000204327126000008/0002043271-26-000008-index.html) — published 2026-10-05; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [4 0002142367-26-000004](https://www.sec.gov/Archives/edgar/data/64040/000214236726000004/0002142367-26-000004-index.html) — published 2026-08-04; retrieved 2026-10-24T13:22:51.759433+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/SPGI/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
