---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002000230
cik: '0002000230'
company_name: BrilliA Inc
tickers:
- BRIA
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 77264ce478c0c699392c0a049f464d4fda44c9f8
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - '3'
  - 424B3
  - 424B4
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - FWP
  - SC 13D
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0002000230.json
    sha256: 4a9c9013d9ca209d713ed83a8576822b9bfb2c2c5c1bf5ca5fa679a598be7849
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002000230.json
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
  url: https://data.sec.gov/submissions/CIK0002000230.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 4a9c9013d9ca209d713ed83a8576822b9bfb2c2c5c1bf5ca5fa679a598be7849
- id: S03
  title: 6-K 0001213900-26-107369
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026107369/0001213900-26-107369-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-084111
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026084111/0001213900-26-084111-index.html
  published_at: '2026-07-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 20-F 0001213900-26-084106
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026084106/0001213900-26-084106-index.html
  published_at: '2026-07-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: SCHEDULE 13G 0001213900-26-043139
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026043139/0001213900-26-043139-index.html
  published_at: '2026-04-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 3 0001213900-26-042719
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026042719/0001213900-26-042719-index.html
  published_at: '2026-04-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: 3 0001213900-26-034326
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026034326/0001213900-26-034326-index.html
  published_at: '2026-03-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: 3 0001213900-26-033837
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026033837/0001213900-26-033837-index.html
  published_at: '2026-03-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S10
  title: 3 0001213900-26-033830
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026033830/0001213900-26-033830-index.html
  published_at: '2026-03-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S11
  title: 6-K 0001213900-26-033561
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026033561/0001213900-26-033561-index.html
  published_at: '2026-03-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S12
  title: 3 0001213900-26-032633
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026032633/0001213900-26-032633-index.html
  published_at: '2026-03-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S13
  title: 3 0001213900-26-032200
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026032200/0001213900-26-032200-index.html
  published_at: '2026-03-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S14
  title: SCHEDULE 13G/A 0001213900-25-086357
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025086357/0001213900-25-086357-index.html
  published_at: '2025-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S15
  title: 6-K 0001213900-25-084063
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025084063/0001213900-25-084063-index.html
  published_at: '2025-09-03'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S16
  title: 424B3 0001213900-25-080076
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025080076/0001213900-25-080076-index.html
  published_at: '2025-08-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S17
  title: EFFECT 9999999995-25-002707
  url: https://www.sec.gov/Archives/edgar/data/2000230/999999999525002707/9999999995-25-002707-index.html
  published_at: '2025-08-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: CORRESP 0001213900-25-078481
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025078481/0001213900-25-078481-index.html
  published_at: '2025-08-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: F-1/A 0001213900-25-077951
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025077951/0001213900-25-077951-index.html
  published_at: '2025-08-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: F-1 0001213900-25-076752
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025076752/0001213900-25-076752-index.html
  published_at: '2025-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: UPLOAD 0000000000-25-008429
  url: https://www.sec.gov/Archives/edgar/data/2000230/000000000025008429/0000000000-25-008429-index.html
  published_at: '2025-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S22
  title: 6-K/A 0001213900-25-070848
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025070848/0001213900-25-070848-index.html
  published_at: '2025-08-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S23
  title: DRS 0001213900-25-070639
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025070639/0001213900-25-070639-index.html
  published_at: '2025-08-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S24
  title: 6-K 0001213900-25-070616
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025070616/0001213900-25-070616-index.html
  published_at: '2025-08-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S25
  title: 6-K 0001213900-25-066326
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025066326/0001213900-25-066326-index.html
  published_at: '2025-07-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S26
  title: 20-F 0001213900-25-066324
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025066324/0001213900-25-066324-index.html
  published_at: '2025-07-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S27
  title: 6-K 0001213900-25-054268
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025054268/0001213900-25-054268-index.html
  published_at: '2025-06-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S28
  title: 6-K 0001213900-25-025736
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025025736/0001213900-25-025736-index.html
  published_at: '2025-03-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S29
  title: SCHEDULE 13G 0001213900-25-017237
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025017237/0001213900-25-017237-index.html
  published_at: '2025-02-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S30
  title: SCHEDULE 13G 0001213900-25-015027
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025015027/0001213900-25-015027-index.html
  published_at: '2025-02-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S31
  title: SC 13D 0001213900-24-109494
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024109494/0001213900-24-109494-index.html
  published_at: '2024-12-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S32
  title: SC 13D 0001213900-24-108589
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024108589/0001213900-24-108589-index.html
  published_at: '2024-12-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S33
  title: 6-K 0001213900-24-104084
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024104084/0001213900-24-104084-index.html
  published_at: '2024-11-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S34
  title: 424B4 0001213900-24-103340
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024103340/0001213900-24-103340-index.html
  published_at: '2024-11-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S35
  title: EFFECT 9999999995-24-003515
  url: https://www.sec.gov/Archives/edgar/data/2000230/999999999524003515/9999999995-24-003515-index.html
  published_at: '2024-11-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S36
  title: F-1/A 0001213900-24-099319
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024099319/0001213900-24-099319-index.html
  published_at: '2024-11-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S37
  title: CORRESP 0001213900-24-098996
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024098996/0001213900-24-098996-index.html
  published_at: '2024-11-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S38
  title: CORRESP 0001213900-24-098993
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024098993/0001213900-24-098993-index.html
  published_at: '2024-11-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S39
  title: 8-A12B 0001213900-24-098730
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024098730/0001213900-24-098730-index.html
  published_at: '2024-11-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S40
  title: CERT 0001143313-24-000113
  url: https://www.sec.gov/Archives/edgar/data/2000230/000114331324000113/0001143313-24-000113-index.html
  published_at: '2024-11-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S41
  title: F-1/A 0001213900-24-087852
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024087852/0001213900-24-087852-index.html
  published_at: '2024-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S42
  title: FWP 0001213900-24-082895
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024082895/0001213900-24-082895-index.html
  published_at: '2024-09-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S43
  title: CORRESP 0001213900-24-079745
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024079745/0001213900-24-079745-index.html
  published_at: '2024-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S44
  title: F-1/A 0001213900-24-079743
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024079743/0001213900-24-079743-index.html
  published_at: '2024-09-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S45
  title: UPLOAD 0000000000-24-010503
  url: https://www.sec.gov/Archives/edgar/data/2000230/000000000024010503/0000000000-24-010503-index.html
  published_at: '2024-09-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S46
  title: F-1 0001213900-24-078063
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024078063/0001213900-24-078063-index.html
  published_at: '2024-09-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S47
  title: DRSLTR 0001213900-24-071411
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024071411/0001213900-24-071411-index.html
  published_at: '2024-08-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S48
  title: DRS/A 0001213900-24-071410
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024071410/0001213900-24-071410-index.html
  published_at: '2024-08-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S49
  title: UPLOAD 0000000000-24-009511
  url: https://www.sec.gov/Archives/edgar/data/2000230/000000000024009511/0000000000-24-009511-index.html
  published_at: '2024-08-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S50
  title: DRSLTR 0001213900-24-068113
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024068113/0001213900-24-068113-index.html
  published_at: '2024-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S51
  title: DRS/A 0001213900-24-068109
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390024068109/0001213900-24-068109-index.html
  published_at: '2024-08-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S52
  title: UPLOAD 0000000000-24-006924
  url: https://www.sec.gov/Archives/edgar/data/2000230/000000000024006924/0000000000-24-006924-index.html
  published_at: '2024-06-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0002000230'
  classification_status: reported_sic
  entity_type: other
  name: BrilliA Inc
  sic: '2300'
  sic_description: Apparel & Other Finishd Prods of  Fabrics & Similar Matl
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 4a9c9013d9ca209d713ed83a8576822b9bfb2c2c5c1bf5ca5fa679a598be7849
  url: https://data.sec.gov/submissions/CIK0002000230.json
listings:
- ticker: BRIA
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-084106
  filed: '2026-07-31'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026084106/0001213900-26-084106-index.html
- accession: 0001213900-26-107369
  filed: '2026-10-07'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390026107369/0001213900-26-107369-index.html
- accession: 0001213900-25-070848
  filed: '2025-08-04'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/2000230/000121390025070848/0001213900-25-070848-index.html
research_progress:
  stage: pending
  input_sha256: 9c96b86c098b143daa812aafa1df82bbe2cc942331038ff11c92d4ff7d56aa62
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
---
# BRIA — BrilliA Inc

> Automatically maintained factual stub. Substantive company research is incomplete.

[All companies](../../INDEX.md)


## Business overview

Reported issuer name: **BrilliA Inc**. Stable SEC CIK: **0002000230**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| BRIA | NYSE_AMERICAN | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2300**: Apparel & Other Finishd Prods of  Fabrics & Similar Matl. [S02]

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
- Forms observed in the retained filing inventory: 20-F, 3, 424B3, 424B4, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, FWP, SC 13D, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:31.167959+00:00.

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

Latest 50 filing metadata records of 60 retained records. A filing link is evidence of submission, not evidence that the document was read or analyzed.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-07 | 6-K | 0001213900-26-107369 | — | [S03] |
| 2026-07-31 | 6-K | 0001213900-26-084111 | — | [S04] |
| 2026-07-31 | 20-F | 0001213900-26-084106 | — | [S05] |
| 2026-04-13 | SCHEDULE 13G | 0001213900-26-043139 | — | [S06] |
| 2026-04-13 | 3 | 0001213900-26-042719 | — | [S07] |
| 2026-03-26 | 3 | 0001213900-26-034326 | — | [S08] |
| 2026-03-25 | 3 | 0001213900-26-033837 | — | [S09] |
| 2026-03-25 | 3 | 0001213900-26-033830 | — | [S10] |
| 2026-03-24 | 6-K | 0001213900-26-033561 | — | [S11] |
| 2026-03-23 | 3 | 0001213900-26-032633 | — | [S12] |
| 2026-03-20 | 3 | 0001213900-26-032200 | — | [S13] |
| 2025-09-10 | SCHEDULE 13G/A | 0001213900-25-086357 | — | [S14] |
| 2025-09-03 | 6-K | 0001213900-25-084063 | — | [S15] |
| 2025-08-25 | 424B3 | 0001213900-25-080076 | — | [S16] |
| 2025-08-21 | EFFECT | 9999999995-25-002707 | — | [S17] |
| 2025-08-19 | CORRESP | 0001213900-25-078481 | — | [S18] |
| 2025-08-18 | F-1/A | 0001213900-25-077951 | — | [S19] |
| 2025-08-14 | F-1 | 0001213900-25-076752 | — | [S20] |
| 2025-08-12 | UPLOAD | 0000000000-25-008429 | — | [S21] |
| 2025-08-04 | 6-K/A | 0001213900-25-070848 | — | [S22] |
| 2025-08-01 | DRS | 0001213900-25-070639 | — | [S23] |
| 2025-08-01 | 6-K | 0001213900-25-070616 | — | [S24] |
| 2025-07-22 | 6-K | 0001213900-25-066326 | — | [S25] |
| 2025-07-22 | 20-F | 0001213900-25-066324 | — | [S26] |
| 2025-06-13 | 6-K | 0001213900-25-054268 | — | [S27] |
| 2025-03-21 | 6-K | 0001213900-25-025736 | — | [S28] |
| 2025-02-26 | SCHEDULE 13G | 0001213900-25-017237 | — | [S29] |
| 2025-02-19 | SCHEDULE 13G | 0001213900-25-015027 | — | [S30] |
| 2024-12-17 | SC 13D | 0001213900-24-109494 | — | [S31] |
| 2024-12-13 | SC 13D | 0001213900-24-108589 | — | [S32] |
| 2024-11-29 | 6-K | 0001213900-24-104084 | — | [S33] |
| 2024-11-27 | 424B4 | 0001213900-24-103340 | — | [S34] |
| 2024-11-19 | EFFECT | 9999999995-24-003515 | — | [S35] |
| 2024-11-18 | F-1/A | 0001213900-24-099319 | — | [S36] |
| 2024-11-15 | CORRESP | 0001213900-24-098996 | — | [S37] |
| 2024-11-15 | CORRESP | 0001213900-24-098993 | — | [S38] |
| 2024-11-15 | 8-A12B | 0001213900-24-098730 | — | [S39] |
| 2024-11-15 | CERT | 0001143313-24-000113 | — | [S40] |
| 2024-10-15 | F-1/A | 0001213900-24-087852 | — | [S41] |
| 2024-09-30 | FWP | 0001213900-24-082895 | — | [S42] |
| 2024-09-18 | CORRESP | 0001213900-24-079745 | — | [S43] |
| 2024-09-18 | F-1/A | 0001213900-24-079743 | — | [S44] |
| 2024-09-17 | UPLOAD | 0000000000-24-010503 | — | [S45] |
| 2024-09-12 | F-1 | 0001213900-24-078063 | — | [S46] |
| 2024-08-21 | DRSLTR | 0001213900-24-071411 | — | [S47] |
| 2024-08-21 | DRS/A | 0001213900-24-071410 | — | [S48] |
| 2024-08-20 | UPLOAD | 0000000000-24-009511 | — | [S49] |
| 2024-08-13 | DRSLTR | 0001213900-24-068113 | — | [S50] |
| 2024-08-13 | DRS/A | 0001213900-24-068109 | — | [S51] |
| 2024-06-17 | UPLOAD | 0000000000-24-006924 | — | [S52] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:35.250901+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002000230.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001213900-26-107369](https://www.sec.gov/Archives/edgar/data/2000230/000121390026107369/0001213900-26-107369-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001213900-26-084111](https://www.sec.gov/Archives/edgar/data/2000230/000121390026084111/0001213900-26-084111-index.html) — published 2026-07-31; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [20-F 0001213900-26-084106](https://www.sec.gov/Archives/edgar/data/2000230/000121390026084106/0001213900-26-084106-index.html) — published 2026-07-31; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [SCHEDULE 13G 0001213900-26-043139](https://www.sec.gov/Archives/edgar/data/2000230/000121390026043139/0001213900-26-043139-index.html) — published 2026-04-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [3 0001213900-26-042719](https://www.sec.gov/Archives/edgar/data/2000230/000121390026042719/0001213900-26-042719-index.html) — published 2026-04-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [3 0001213900-26-034326](https://www.sec.gov/Archives/edgar/data/2000230/000121390026034326/0001213900-26-034326-index.html) — published 2026-03-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [3 0001213900-26-033837](https://www.sec.gov/Archives/edgar/data/2000230/000121390026033837/0001213900-26-033837-index.html) — published 2026-03-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S10] [3 0001213900-26-033830](https://www.sec.gov/Archives/edgar/data/2000230/000121390026033830/0001213900-26-033830-index.html) — published 2026-03-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S11] [6-K 0001213900-26-033561](https://www.sec.gov/Archives/edgar/data/2000230/000121390026033561/0001213900-26-033561-index.html) — published 2026-03-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S12] [3 0001213900-26-032633](https://www.sec.gov/Archives/edgar/data/2000230/000121390026032633/0001213900-26-032633-index.html) — published 2026-03-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S13] [3 0001213900-26-032200](https://www.sec.gov/Archives/edgar/data/2000230/000121390026032200/0001213900-26-032200-index.html) — published 2026-03-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S14] [SCHEDULE 13G/A 0001213900-25-086357](https://www.sec.gov/Archives/edgar/data/2000230/000121390025086357/0001213900-25-086357-index.html) — published 2025-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S15] [6-K 0001213900-25-084063](https://www.sec.gov/Archives/edgar/data/2000230/000121390025084063/0001213900-25-084063-index.html) — published 2025-09-03; retrieved 2026-10-23T08:33:02.691743+00:00.

[S16] [424B3 0001213900-25-080076](https://www.sec.gov/Archives/edgar/data/2000230/000121390025080076/0001213900-25-080076-index.html) — published 2025-08-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S17] [EFFECT 9999999995-25-002707](https://www.sec.gov/Archives/edgar/data/2000230/999999999525002707/9999999995-25-002707-index.html) — published 2025-08-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [CORRESP 0001213900-25-078481](https://www.sec.gov/Archives/edgar/data/2000230/000121390025078481/0001213900-25-078481-index.html) — published 2025-08-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [F-1/A 0001213900-25-077951](https://www.sec.gov/Archives/edgar/data/2000230/000121390025077951/0001213900-25-077951-index.html) — published 2025-08-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [F-1 0001213900-25-076752](https://www.sec.gov/Archives/edgar/data/2000230/000121390025076752/0001213900-25-076752-index.html) — published 2025-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [UPLOAD 0000000000-25-008429](https://www.sec.gov/Archives/edgar/data/2000230/000000000025008429/0000000000-25-008429-index.html) — published 2025-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S22] [6-K/A 0001213900-25-070848](https://www.sec.gov/Archives/edgar/data/2000230/000121390025070848/0001213900-25-070848-index.html) — published 2025-08-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S23] [DRS 0001213900-25-070639](https://www.sec.gov/Archives/edgar/data/2000230/000121390025070639/0001213900-25-070639-index.html) — published 2025-08-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S24] [6-K 0001213900-25-070616](https://www.sec.gov/Archives/edgar/data/2000230/000121390025070616/0001213900-25-070616-index.html) — published 2025-08-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S25] [6-K 0001213900-25-066326](https://www.sec.gov/Archives/edgar/data/2000230/000121390025066326/0001213900-25-066326-index.html) — published 2025-07-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S26] [20-F 0001213900-25-066324](https://www.sec.gov/Archives/edgar/data/2000230/000121390025066324/0001213900-25-066324-index.html) — published 2025-07-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S27] [6-K 0001213900-25-054268](https://www.sec.gov/Archives/edgar/data/2000230/000121390025054268/0001213900-25-054268-index.html) — published 2025-06-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S28] [6-K 0001213900-25-025736](https://www.sec.gov/Archives/edgar/data/2000230/000121390025025736/0001213900-25-025736-index.html) — published 2025-03-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S29] [SCHEDULE 13G 0001213900-25-017237](https://www.sec.gov/Archives/edgar/data/2000230/000121390025017237/0001213900-25-017237-index.html) — published 2025-02-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S30] [SCHEDULE 13G 0001213900-25-015027](https://www.sec.gov/Archives/edgar/data/2000230/000121390025015027/0001213900-25-015027-index.html) — published 2025-02-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S31] [SC 13D 0001213900-24-109494](https://www.sec.gov/Archives/edgar/data/2000230/000121390024109494/0001213900-24-109494-index.html) — published 2024-12-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S32] [SC 13D 0001213900-24-108589](https://www.sec.gov/Archives/edgar/data/2000230/000121390024108589/0001213900-24-108589-index.html) — published 2024-12-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S33] [6-K 0001213900-24-104084](https://www.sec.gov/Archives/edgar/data/2000230/000121390024104084/0001213900-24-104084-index.html) — published 2024-11-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S34] [424B4 0001213900-24-103340](https://www.sec.gov/Archives/edgar/data/2000230/000121390024103340/0001213900-24-103340-index.html) — published 2024-11-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S35] [EFFECT 9999999995-24-003515](https://www.sec.gov/Archives/edgar/data/2000230/999999999524003515/9999999995-24-003515-index.html) — published 2024-11-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S36] [F-1/A 0001213900-24-099319](https://www.sec.gov/Archives/edgar/data/2000230/000121390024099319/0001213900-24-099319-index.html) — published 2024-11-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S37] [CORRESP 0001213900-24-098996](https://www.sec.gov/Archives/edgar/data/2000230/000121390024098996/0001213900-24-098996-index.html) — published 2024-11-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S38] [CORRESP 0001213900-24-098993](https://www.sec.gov/Archives/edgar/data/2000230/000121390024098993/0001213900-24-098993-index.html) — published 2024-11-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S39] [8-A12B 0001213900-24-098730](https://www.sec.gov/Archives/edgar/data/2000230/000121390024098730/0001213900-24-098730-index.html) — published 2024-11-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S40] [CERT 0001143313-24-000113](https://www.sec.gov/Archives/edgar/data/2000230/000114331324000113/0001143313-24-000113-index.html) — published 2024-11-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S41] [F-1/A 0001213900-24-087852](https://www.sec.gov/Archives/edgar/data/2000230/000121390024087852/0001213900-24-087852-index.html) — published 2024-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S42] [FWP 0001213900-24-082895](https://www.sec.gov/Archives/edgar/data/2000230/000121390024082895/0001213900-24-082895-index.html) — published 2024-09-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S43] [CORRESP 0001213900-24-079745](https://www.sec.gov/Archives/edgar/data/2000230/000121390024079745/0001213900-24-079745-index.html) — published 2024-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S44] [F-1/A 0001213900-24-079743](https://www.sec.gov/Archives/edgar/data/2000230/000121390024079743/0001213900-24-079743-index.html) — published 2024-09-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S45] [UPLOAD 0000000000-24-010503](https://www.sec.gov/Archives/edgar/data/2000230/000000000024010503/0000000000-24-010503-index.html) — published 2024-09-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S46] [F-1 0001213900-24-078063](https://www.sec.gov/Archives/edgar/data/2000230/000121390024078063/0001213900-24-078063-index.html) — published 2024-09-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S47] [DRSLTR 0001213900-24-071411](https://www.sec.gov/Archives/edgar/data/2000230/000121390024071411/0001213900-24-071411-index.html) — published 2024-08-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S48] [DRS/A 0001213900-24-071410](https://www.sec.gov/Archives/edgar/data/2000230/000121390024071410/0001213900-24-071410-index.html) — published 2024-08-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S49] [UPLOAD 0000000000-24-009511](https://www.sec.gov/Archives/edgar/data/2000230/000000000024009511/0000000000-24-009511-index.html) — published 2024-08-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S50] [DRSLTR 0001213900-24-068113](https://www.sec.gov/Archives/edgar/data/2000230/000121390024068113/0001213900-24-068113-index.html) — published 2024-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S51] [DRS/A 0001213900-24-068109](https://www.sec.gov/Archives/edgar/data/2000230/000121390024068109/0001213900-24-068109-index.html) — published 2024-08-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S52] [UPLOAD 0000000000-24-006924](https://www.sec.gov/Archives/edgar/data/2000230/000000000024006924/0000000000-24-006924-index.html) — published 2024-06-17; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. Dated research changes remain in Git history; review is never inferred from collection.
