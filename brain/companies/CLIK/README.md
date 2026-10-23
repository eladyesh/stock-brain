---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002020027
cik: '0002020027'
company_name: Click Holdings Ltd.
tickers:
- CLIK
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: 3f697433c3580d4ca83edbe44c66580ac926c8d7
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - '3'
  - '4'
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - S-8
  - SCHEDULE 13D
  - SCHEDULE 13G
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0002020027.json
    sha256: 864d139c083cadd15c0cbee17f41630a4319e66c21f3b640a431950df0522765
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002020027.json
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
  url: https://data.sec.gov/submissions/CIK0002020027.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 864d139c083cadd15c0cbee17f41630a4319e66c21f3b640a431950df0522765
- id: S03
  title: 6-K 0001493152-26-048037
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226048037/0001493152-26-048037-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 20-F 0001493152-26-048036
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226048036/0001493152-26-048036-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001493152-26-046280
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226046280/0001493152-26-046280-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001493152-26-046092
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226046092/0001493152-26-046092-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001493152-26-042774
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226042774/0001493152-26-042774-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: 6-K 0001493152-26-042303
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226042303/0001493152-26-042303-index.html
  published_at: '2026-09-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: 4 0001493152-26-042298
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226042298/0001493152-26-042298-index.html
  published_at: '2026-09-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S10
  title: EFFECT 9999999995-26-002934
  url: https://www.sec.gov/Archives/edgar/data/2020027/999999999526002934/9999999995-26-002934-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S11
  title: F-3/A 0001493152-26-041311
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226041311/0001493152-26-041311-index.html
  published_at: '2026-09-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S12
  title: 6-K 0001493152-26-040942
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226040942/0001493152-26-040942-index.html
  published_at: '2026-09-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S13
  title: F-3 0001493152-26-040048
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226040048/0001493152-26-040048-index.html
  published_at: '2026-08-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S14
  title: 6-K 0001493152-26-040002
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226040002/0001493152-26-040002-index.html
  published_at: '2026-08-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S15
  title: 424B3 0001493152-26-034010
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226034010/0001493152-26-034010-index.html
  published_at: '2026-07-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S16
  title: 6-K 0001493152-26-034006
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226034006/0001493152-26-034006-index.html
  published_at: '2026-07-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S17
  title: EFFECT 9999999995-26-002368
  url: https://www.sec.gov/Archives/edgar/data/2020027/999999999526002368/9999999995-26-002368-index.html
  published_at: '2026-07-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 6-K 0001493152-26-033655
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226033655/0001493152-26-033655-index.html
  published_at: '2026-07-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: F-1 0001493152-26-033136
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226033136/0001493152-26-033136-index.html
  published_at: '2026-07-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 6-K 0001493152-26-031236
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226031236/0001493152-26-031236-index.html
  published_at: '2026-06-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: DRS 0001493152-26-031186
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226031186/0001493152-26-031186-index.html
  published_at: '2026-06-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S22
  title: 4 0001493152-26-029696
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226029696/0001493152-26-029696-index.html
  published_at: '2026-06-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S23
  title: 4 0001493152-26-028368
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226028368/0001493152-26-028368-index.html
  published_at: '2026-06-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S24
  title: 4 0001493152-26-027629
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226027629/0001493152-26-027629-index.html
  published_at: '2026-06-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S25
  title: 6-K 0001493152-26-027628
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226027628/0001493152-26-027628-index.html
  published_at: '2026-06-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S26
  title: 6-K 0001493152-26-027195
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226027195/0001493152-26-027195-index.html
  published_at: '2026-06-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S27
  title: 6-K 0001493152-26-027189
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226027189/0001493152-26-027189-index.html
  published_at: '2026-06-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S28
  title: 6-K 0001493152-26-025715
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226025715/0001493152-26-025715-index.html
  published_at: '2026-05-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S29
  title: 6-K 0001493152-26-022109
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226022109/0001493152-26-022109-index.html
  published_at: '2026-05-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S30
  title: 6-K 0001493152-26-019252
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226019252/0001493152-26-019252-index.html
  published_at: '2026-04-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S31
  title: 6-K 0001493152-26-018180
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226018180/0001493152-26-018180-index.html
  published_at: '2026-04-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S32
  title: 3 0001493152-26-011510
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226011510/0001493152-26-011510-index.html
  published_at: '2026-03-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S33
  title: 3 0001493152-26-011082
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226011082/0001493152-26-011082-index.html
  published_at: '2026-03-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S34
  title: 3 0001493152-26-011080
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226011080/0001493152-26-011080-index.html
  published_at: '2026-03-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S35
  title: 3 0001493152-26-011077
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226011077/0001493152-26-011077-index.html
  published_at: '2026-03-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S36
  title: 3 0001493152-26-011075
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226011075/0001493152-26-011075-index.html
  published_at: '2026-03-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S37
  title: 6-K 0001493152-26-009994
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226009994/0001493152-26-009994-index.html
  published_at: '2026-03-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S38
  title: SCHEDULE 13D 0001493152-26-000743
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226000743/0001493152-26-000743-index.html
  published_at: '2026-01-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S39
  title: SCHEDULE 13D 0001493152-26-000741
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226000741/0001493152-26-000741-index.html
  published_at: '2026-01-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S40
  title: SCHEDULE 13G 0001493152-26-000739
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226000739/0001493152-26-000739-index.html
  published_at: '2026-01-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S41
  title: 424B3 0001493152-25-028640
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315225028640/0001493152-25-028640-index.html
  published_at: '2025-12-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S42
  title: EFFECT 9999999995-25-003873
  url: https://www.sec.gov/Archives/edgar/data/2020027/999999999525003873/9999999995-25-003873-index.html
  published_at: '2025-12-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S43
  title: CORRESP 0001493152-25-028081
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315225028081/0001493152-25-028081-index.html
  published_at: '2025-12-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S44
  title: F-1 0001493152-25-027671
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315225027671/0001493152-25-027671-index.html
  published_at: '2025-12-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S45
  title: DRS 0001493152-25-026114
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315225026114/0001493152-25-026114-index.html
  published_at: '2025-12-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S46
  title: 6-K 0001493152-25-023844
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315225023844/0001493152-25-023844-index.html
  published_at: '2025-11-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S47
  title: 6-K 0001493152-25-019288
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315225019288/0001493152-25-019288-index.html
  published_at: '2025-10-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S48
  title: 20-F 0001493152-25-019286
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315225019286/0001493152-25-019286-index.html
  published_at: '2025-10-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S49
  title: 6-K 0001493152-25-017945
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315225017945/0001493152-25-017945-index.html
  published_at: '2025-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S50
  title: 6-K 0001493152-25-017191
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315225017191/0001493152-25-017191-index.html
  published_at: '2025-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S51
  title: 6-K 0001213900-25-065886
  url: https://www.sec.gov/Archives/edgar/data/2020027/000121390025065886/0001213900-25-065886-index.html
  published_at: '2025-07-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S52
  title: 6-K 0001213900-25-063981
  url: https://www.sec.gov/Archives/edgar/data/2020027/000121390025063981/0001213900-25-063981-index.html
  published_at: '2025-07-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0002020027'
  classification_status: reported_sic
  entity_type: other
  name: Click Holdings Ltd.
  sic: '7361'
  sic_description: Services-Employment Agencies
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 864d139c083cadd15c0cbee17f41630a4319e66c21f3b640a431950df0522765
  url: https://data.sec.gov/submissions/CIK0002020027.json
listings:
- ticker: CLIK
  exchange: NASDAQ
  instrument_type: equity_candidate
research_filings:
- accession: 0001493152-26-048036
  filed: '2026-10-22'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226048036/0001493152-26-048036-index.html
- accession: 0001493152-26-048037
  filed: '2026-10-22'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/2020027/000149315226048037/0001493152-26-048037-index.html
research_progress:
  stage: pending
  input_sha256: 3068fe5ea47dbb4dadab893a136dfefeffe7f854cacdeab92011b5656c8b7ac7
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
---
# CLIK — Click Holdings Ltd.

> Automatically maintained factual stub. Substantive company research is incomplete.

[All companies](../../INDEX.md)


## Business overview

Reported issuer name: **Click Holdings Ltd.**. Stable SEC CIK: **0002020027**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| CLIK | NASDAQ | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7361**: Services-Employment Agencies. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

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
- Sector, industry and domicile remain unassigned unless a separate reviewed profile supplies them.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 4, 424B3, 424B4, 424B5, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, F-3/A, S-8, SCHEDULE 13D, SCHEDULE 13G, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-23T14:34:33.456664+00:00.

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

Latest 50 filing metadata records of 95 retained records. A filing link is evidence of submission, not evidence that the document was read or analyzed.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-22 | 6-K | 0001493152-26-048037 | — | [S03] |
| 2026-10-22 | 20-F | 0001493152-26-048036 | — | [S04] |
| 2026-10-08 | 6-K | 0001493152-26-046280 | — | [S05] |
| 2026-10-07 | 6-K | 0001493152-26-046092 | — | [S06] |
| 2026-09-15 | 6-K | 0001493152-26-042774 | — | [S07] |
| 2026-09-11 | 6-K | 0001493152-26-042303 | — | [S08] |
| 2026-09-11 | 4 | 0001493152-26-042298 | — | [S09] |
| 2026-09-10 | EFFECT | 9999999995-26-002934 | — | [S10] |
| 2026-09-03 | F-3/A | 0001493152-26-041311 | — | [S11] |
| 2026-09-01 | 6-K | 0001493152-26-040942 | — | [S12] |
| 2026-08-25 | F-3 | 0001493152-26-040048 | — | [S13] |
| 2026-08-25 | 6-K | 0001493152-26-040002 | — | [S14] |
| 2026-07-21 | 424B3 | 0001493152-26-034010 | — | [S15] |
| 2026-07-21 | 6-K | 0001493152-26-034006 | — | [S16] |
| 2026-07-20 | EFFECT | 9999999995-26-002368 | — | [S17] |
| 2026-07-17 | 6-K | 0001493152-26-033655 | — | [S18] |
| 2026-07-14 | F-1 | 0001493152-26-033136 | — | [S19] |
| 2026-06-30 | 6-K | 0001493152-26-031236 | — | [S20] |
| 2026-06-30 | DRS | 0001493152-26-031186 | — | [S21] |
| 2026-06-23 | 4 | 0001493152-26-029696 | — | [S22] |
| 2026-06-12 | 4 | 0001493152-26-028368 | — | [S23] |
| 2026-06-08 | 4 | 0001493152-26-027629 | — | [S24] |
| 2026-06-08 | 6-K | 0001493152-26-027628 | — | [S25] |
| 2026-06-04 | 6-K | 0001493152-26-027195 | — | [S26] |
| 2026-06-04 | 6-K | 0001493152-26-027189 | — | [S27] |
| 2026-05-29 | 6-K | 0001493152-26-025715 | — | [S28] |
| 2026-05-11 | 6-K | 0001493152-26-022109 | — | [S29] |
| 2026-04-28 | 6-K | 0001493152-26-019252 | — | [S30] |
| 2026-04-21 | 6-K | 0001493152-26-018180 | — | [S31] |
| 2026-03-19 | 3 | 0001493152-26-011510 | — | [S32] |
| 2026-03-18 | 3 | 0001493152-26-011082 | — | [S33] |
| 2026-03-18 | 3 | 0001493152-26-011080 | — | [S34] |
| 2026-03-18 | 3 | 0001493152-26-011077 | — | [S35] |
| 2026-03-18 | 3 | 0001493152-26-011075 | — | [S36] |
| 2026-03-13 | 6-K | 0001493152-26-009994 | — | [S37] |
| 2026-01-07 | SCHEDULE 13D | 0001493152-26-000743 | — | [S38] |
| 2026-01-07 | SCHEDULE 13D | 0001493152-26-000741 | — | [S39] |
| 2026-01-07 | SCHEDULE 13G | 0001493152-26-000739 | — | [S40] |
| 2025-12-22 | 424B3 | 0001493152-25-028640 | — | [S41] |
| 2025-12-19 | EFFECT | 9999999995-25-003873 | — | [S42] |
| 2025-12-17 | CORRESP | 0001493152-25-028081 | — | [S43] |
| 2025-12-15 | F-1 | 0001493152-25-027671 | — | [S44] |
| 2025-12-04 | DRS | 0001493152-25-026114 | — | [S45] |
| 2025-11-17 | 6-K | 0001493152-25-023844 | — | [S46] |
| 2025-10-24 | 6-K | 0001493152-25-019288 | — | [S47] |
| 2025-10-24 | 20-F | 0001493152-25-019286 | — | [S48] |
| 2025-10-14 | 6-K | 0001493152-25-017945 | — | [S49] |
| 2025-10-07 | 6-K | 0001493152-25-017191 | — | [S50] |
| 2025-07-21 | 6-K | 0001213900-25-065886 | — | [S51] |
| 2025-07-15 | 6-K | 0001213900-25-063981 | — | [S52] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002020027.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001493152-26-048037](https://www.sec.gov/Archives/edgar/data/2020027/000149315226048037/0001493152-26-048037-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [20-F 0001493152-26-048036](https://www.sec.gov/Archives/edgar/data/2020027/000149315226048036/0001493152-26-048036-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001493152-26-046280](https://www.sec.gov/Archives/edgar/data/2020027/000149315226046280/0001493152-26-046280-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001493152-26-046092](https://www.sec.gov/Archives/edgar/data/2020027/000149315226046092/0001493152-26-046092-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001493152-26-042774](https://www.sec.gov/Archives/edgar/data/2020027/000149315226042774/0001493152-26-042774-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [6-K 0001493152-26-042303](https://www.sec.gov/Archives/edgar/data/2020027/000149315226042303/0001493152-26-042303-index.html) — published 2026-09-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [4 0001493152-26-042298](https://www.sec.gov/Archives/edgar/data/2020027/000149315226042298/0001493152-26-042298-index.html) — published 2026-09-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S10] [EFFECT 9999999995-26-002934](https://www.sec.gov/Archives/edgar/data/2020027/999999999526002934/9999999995-26-002934-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S11] [F-3/A 0001493152-26-041311](https://www.sec.gov/Archives/edgar/data/2020027/000149315226041311/0001493152-26-041311-index.html) — published 2026-09-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S12] [6-K 0001493152-26-040942](https://www.sec.gov/Archives/edgar/data/2020027/000149315226040942/0001493152-26-040942-index.html) — published 2026-09-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S13] [F-3 0001493152-26-040048](https://www.sec.gov/Archives/edgar/data/2020027/000149315226040048/0001493152-26-040048-index.html) — published 2026-08-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S14] [6-K 0001493152-26-040002](https://www.sec.gov/Archives/edgar/data/2020027/000149315226040002/0001493152-26-040002-index.html) — published 2026-08-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S15] [424B3 0001493152-26-034010](https://www.sec.gov/Archives/edgar/data/2020027/000149315226034010/0001493152-26-034010-index.html) — published 2026-07-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S16] [6-K 0001493152-26-034006](https://www.sec.gov/Archives/edgar/data/2020027/000149315226034006/0001493152-26-034006-index.html) — published 2026-07-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S17] [EFFECT 9999999995-26-002368](https://www.sec.gov/Archives/edgar/data/2020027/999999999526002368/9999999995-26-002368-index.html) — published 2026-07-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [6-K 0001493152-26-033655](https://www.sec.gov/Archives/edgar/data/2020027/000149315226033655/0001493152-26-033655-index.html) — published 2026-07-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [F-1 0001493152-26-033136](https://www.sec.gov/Archives/edgar/data/2020027/000149315226033136/0001493152-26-033136-index.html) — published 2026-07-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [6-K 0001493152-26-031236](https://www.sec.gov/Archives/edgar/data/2020027/000149315226031236/0001493152-26-031236-index.html) — published 2026-06-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [DRS 0001493152-26-031186](https://www.sec.gov/Archives/edgar/data/2020027/000149315226031186/0001493152-26-031186-index.html) — published 2026-06-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S22] [4 0001493152-26-029696](https://www.sec.gov/Archives/edgar/data/2020027/000149315226029696/0001493152-26-029696-index.html) — published 2026-06-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S23] [4 0001493152-26-028368](https://www.sec.gov/Archives/edgar/data/2020027/000149315226028368/0001493152-26-028368-index.html) — published 2026-06-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S24] [4 0001493152-26-027629](https://www.sec.gov/Archives/edgar/data/2020027/000149315226027629/0001493152-26-027629-index.html) — published 2026-06-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S25] [6-K 0001493152-26-027628](https://www.sec.gov/Archives/edgar/data/2020027/000149315226027628/0001493152-26-027628-index.html) — published 2026-06-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S26] [6-K 0001493152-26-027195](https://www.sec.gov/Archives/edgar/data/2020027/000149315226027195/0001493152-26-027195-index.html) — published 2026-06-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S27] [6-K 0001493152-26-027189](https://www.sec.gov/Archives/edgar/data/2020027/000149315226027189/0001493152-26-027189-index.html) — published 2026-06-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S28] [6-K 0001493152-26-025715](https://www.sec.gov/Archives/edgar/data/2020027/000149315226025715/0001493152-26-025715-index.html) — published 2026-05-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S29] [6-K 0001493152-26-022109](https://www.sec.gov/Archives/edgar/data/2020027/000149315226022109/0001493152-26-022109-index.html) — published 2026-05-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S30] [6-K 0001493152-26-019252](https://www.sec.gov/Archives/edgar/data/2020027/000149315226019252/0001493152-26-019252-index.html) — published 2026-04-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S31] [6-K 0001493152-26-018180](https://www.sec.gov/Archives/edgar/data/2020027/000149315226018180/0001493152-26-018180-index.html) — published 2026-04-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S32] [3 0001493152-26-011510](https://www.sec.gov/Archives/edgar/data/2020027/000149315226011510/0001493152-26-011510-index.html) — published 2026-03-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S33] [3 0001493152-26-011082](https://www.sec.gov/Archives/edgar/data/2020027/000149315226011082/0001493152-26-011082-index.html) — published 2026-03-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S34] [3 0001493152-26-011080](https://www.sec.gov/Archives/edgar/data/2020027/000149315226011080/0001493152-26-011080-index.html) — published 2026-03-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S35] [3 0001493152-26-011077](https://www.sec.gov/Archives/edgar/data/2020027/000149315226011077/0001493152-26-011077-index.html) — published 2026-03-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S36] [3 0001493152-26-011075](https://www.sec.gov/Archives/edgar/data/2020027/000149315226011075/0001493152-26-011075-index.html) — published 2026-03-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S37] [6-K 0001493152-26-009994](https://www.sec.gov/Archives/edgar/data/2020027/000149315226009994/0001493152-26-009994-index.html) — published 2026-03-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S38] [SCHEDULE 13D 0001493152-26-000743](https://www.sec.gov/Archives/edgar/data/2020027/000149315226000743/0001493152-26-000743-index.html) — published 2026-01-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S39] [SCHEDULE 13D 0001493152-26-000741](https://www.sec.gov/Archives/edgar/data/2020027/000149315226000741/0001493152-26-000741-index.html) — published 2026-01-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S40] [SCHEDULE 13G 0001493152-26-000739](https://www.sec.gov/Archives/edgar/data/2020027/000149315226000739/0001493152-26-000739-index.html) — published 2026-01-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S41] [424B3 0001493152-25-028640](https://www.sec.gov/Archives/edgar/data/2020027/000149315225028640/0001493152-25-028640-index.html) — published 2025-12-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S42] [EFFECT 9999999995-25-003873](https://www.sec.gov/Archives/edgar/data/2020027/999999999525003873/9999999995-25-003873-index.html) — published 2025-12-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S43] [CORRESP 0001493152-25-028081](https://www.sec.gov/Archives/edgar/data/2020027/000149315225028081/0001493152-25-028081-index.html) — published 2025-12-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S44] [F-1 0001493152-25-027671](https://www.sec.gov/Archives/edgar/data/2020027/000149315225027671/0001493152-25-027671-index.html) — published 2025-12-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S45] [DRS 0001493152-25-026114](https://www.sec.gov/Archives/edgar/data/2020027/000149315225026114/0001493152-25-026114-index.html) — published 2025-12-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S46] [6-K 0001493152-25-023844](https://www.sec.gov/Archives/edgar/data/2020027/000149315225023844/0001493152-25-023844-index.html) — published 2025-11-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S47] [6-K 0001493152-25-019288](https://www.sec.gov/Archives/edgar/data/2020027/000149315225019288/0001493152-25-019288-index.html) — published 2025-10-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S48] [20-F 0001493152-25-019286](https://www.sec.gov/Archives/edgar/data/2020027/000149315225019286/0001493152-25-019286-index.html) — published 2025-10-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S49] [6-K 0001493152-25-017945](https://www.sec.gov/Archives/edgar/data/2020027/000149315225017945/0001493152-25-017945-index.html) — published 2025-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S50] [6-K 0001493152-25-017191](https://www.sec.gov/Archives/edgar/data/2020027/000149315225017191/0001493152-25-017191-index.html) — published 2025-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S51] [6-K 0001213900-25-065886](https://www.sec.gov/Archives/edgar/data/2020027/000121390025065886/0001213900-25-065886-index.html) — published 2025-07-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S52] [6-K 0001213900-25-063981](https://www.sec.gov/Archives/edgar/data/2020027/000121390025063981/0001213900-25-063981-index.html) — published 2025-07-15; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. Dated research changes remain in Git history; review is never inferred from collection.
