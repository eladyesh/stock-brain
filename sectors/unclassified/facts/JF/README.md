---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001716338
cik: 0001716338
company_name: J & Friends Holdings Ltd
tickers:
- JF
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
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 20-F/A
  - '3'
  - 424B4
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - CT ORDER
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - NT 20-F
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001716338.json
    sha256: 7935689e7040996c9f7dbc41461358483953f3402b8a53e2e9279d5c180e7330
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001716338.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-25T13:45:47.626200+00:00'
  sha256: 59ac9b74ff663c6de40f5c93a54d5e12eb3fbef74f82e8a7cfc1456ad9f969ec
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001716338.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 7935689e7040996c9f7dbc41461358483953f3402b8a53e2e9279d5c180e7330
- id: S03
  title: EFFECT 9999999995-26-001560
  url: https://www.sec.gov/Archives/edgar/data/1716338/999999999526001560/9999999995-26-001560-index.html
  published_at: '2026-05-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001104659-26-056677
  url: https://www.sec.gov/Archives/edgar/data/1716338/000110465926056677/0001104659-26-056677-index.html
  published_at: '2026-05-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: CORRESP 0001104659-26-055865
  url: https://www.sec.gov/Archives/edgar/data/1716338/000110465926055865/0001104659-26-055865-index.html
  published_at: '2026-05-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: UPLOAD 0000000000-26-004504
  url: https://www.sec.gov/Archives/edgar/data/1716338/000000000026004504/0000000000-26-004504-index.html
  published_at: '2026-05-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: F-3 0001104659-26-048978
  url: https://www.sec.gov/Archives/edgar/data/1716338/000110465926048978/0001104659-26-048978-index.html
  published_at: '2026-04-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001716338
  classification_status: reported_sic
  entity_type: other
  name: J & Friends Holdings Ltd
  sic: '7370'
  sic_description: Services-Computer Programming, Data Processing, Etc.
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 7935689e7040996c9f7dbc41461358483953f3402b8a53e2e9279d5c180e7330
  url: https://data.sec.gov/submissions/CIK0001716338.json
listings:
- ticker: JF
  exchange: NASDAQ
  instrument_type: depositary_receipt
research_filings:
- accession: 0001104659-26-048056
  filed: '2026-04-24'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1716338/000110465926048056/0001104659-26-048056-index.html
- accession: 0001104659-19-044414
  filed: '2019-08-07'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1716338/000110465919044414/0001104659-19-044414-index.html
- accession: 0001104659-26-056677
  filed: '2026-05-07'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1716338/000110465926056677/0001104659-26-056677-index.html
- accession: 0001213900-24-037909
  filed: '2024-04-30'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1716338/000121390024037909/0001213900-24-037909-index.html
research_progress:
  stage: pending
  input_sha256: 763e71ef2257d8eed23b350cb32ca3a0a8dcbb1486fced0206e08e2891fe226b
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
  sic: '7370'
  sic_description: Services-Computer Programming, Data Processing, Etc.
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/JF/README.md
full_history_commit: 71fcd4775048604503d616351f7f309068b23e1b
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# JF — J & Friends Holdings Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/JF/README.md)

## Business overview

Reported issuer name: **J & Friends Holdings Ltd**. Stable SEC CIK: **0001716338**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| JF | NASDAQ | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7370**: Services-Computer Programming, Data Processing, Etc.. [S02]

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
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 3, 424B4, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, CT ORDER, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, NT 20-F, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:14.521327+00:00.

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
| 2026-05-08 | EFFECT | 9999999995-26-001560 | — | [S03] |
| 2026-05-07 | 6-K | 0001104659-26-056677 | — | [S04] |
| 2026-05-06 | CORRESP | 0001104659-26-055865 | — | [S05] |
| 2026-05-04 | UPLOAD | 0000000000-26-004504 | — | [S06] |
| 2026-04-27 | F-3 | 0001104659-26-048978 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:47.626200+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001716338.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [EFFECT 9999999995-26-001560](https://www.sec.gov/Archives/edgar/data/1716338/999999999526001560/9999999995-26-001560-index.html) — published 2026-05-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001104659-26-056677](https://www.sec.gov/Archives/edgar/data/1716338/000110465926056677/0001104659-26-056677-index.html) — published 2026-05-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [CORRESP 0001104659-26-055865](https://www.sec.gov/Archives/edgar/data/1716338/000110465926055865/0001104659-26-055865-index.html) — published 2026-05-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [UPLOAD 0000000000-26-004504](https://www.sec.gov/Archives/edgar/data/1716338/000000000026004504/0000000000-26-004504-index.html) — published 2026-05-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [F-3 0001104659-26-048978](https://www.sec.gov/Archives/edgar/data/1716338/000110465926048978/0001104659-26-048978-index.html) — published 2026-04-27; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/JF/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
