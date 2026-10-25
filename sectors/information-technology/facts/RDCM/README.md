---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001016838
cik: 0001016838
company_name: RADCOM LTD
tickers:
- RDCM
status: stub
canonical_reviewed: false
as_of: '2026-10-25'
updated_at: '2026-10-25T13:50:29.910841+00:00'
reviewed_at: null
coverage_release: coverage-20261025-40199010718-1
source_commit: d4303e1efab53027fe4e6e90633e2c69b11c599c
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
  - 424B3
  - 424B5
  - 6-K
  - CORRESP
  - CT ORDER
  - D
  - DEF 14A
  - EFFECT
  - F-3
  - F-3/A
  - F-3MEF
  - POS AM
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001016838.json
    sha256: afc55561bd1552e57798984b055b62af6bd0bdc85b1fc9b6c7e345e20ad6a54e
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001016838.json
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
  url: https://data.sec.gov/submissions/CIK0001016838.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: afc55561bd1552e57798984b055b62af6bd0bdc85b1fc9b6c7e345e20ad6a54e
- id: S03
  title: 6-K 0001213900-26-100745
  url: https://www.sec.gov/Archives/edgar/data/1016838/000121390026100745/0001213900-26-100745-index.html
  published_at: '2026-09-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-098384
  url: https://www.sec.gov/Archives/edgar/data/1016838/000121390026098384/0001213900-26-098384-index.html
  published_at: '2026-09-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: SCHEDULE 13D/A 0000921895-26-002520
  url: https://www.sec.gov/Archives/edgar/data/1016838/000092189526002520/0000921895-26-002520-index.html
  published_at: '2026-09-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-088035
  url: https://www.sec.gov/Archives/edgar/data/1016838/000121390026088035/0001213900-26-088035-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001213900-26-087495
  url: https://www.sec.gov/Archives/edgar/data/1016838/000121390026087495/0001213900-26-087495-index.html
  published_at: '2026-08-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001016838
  classification_status: reported_sic
  entity_type: other
  name: RADCOM LTD
  sic: '3577'
  sic_description: Computer Peripheral Equipment, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: afc55561bd1552e57798984b055b62af6bd0bdc85b1fc9b6c7e345e20ad6a54e
  url: https://data.sec.gov/submissions/CIK0001016838.json
listings:
- ticker: RDCM
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-036862
  filed: '2026-03-31'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1016838/000121390026036862/0001213900-26-036862-index.html
- accession: 0001178913-17-002701
  filed: '2017-09-19'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1016838/000117891317002701/0001178913-17-002701-index.html
- accession: 0001178913-16-005183
  filed: '2016-04-27'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1016838/000117891316005183/0001178913-16-005183-index.html
- accession: 0001178913-16-005164
  filed: '2016-04-25'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1016838/000117891316005164/0001178913-16-005164-index.html
- accession: 0001144204-10-056891
  filed: '2010-11-02'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1016838/000114420410056891/0001144204-10-056891-index.html
- accession: 0000922423-04-000686
  filed: '2004-05-13'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1016838/000092242304000686/0000922423-04-000686-index.html
- accession: 0001213900-26-100745
  filed: '2026-09-17'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1016838/000121390026100745/0001213900-26-100745-index.html
- accession: 0001144204-06-034331
  filed: '2006-08-17'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1016838/000114420406034331/0001144204-06-034331-index.html
research_progress:
  stage: pending
  input_sha256: b8a32dbc587cb818ead034d9557e718a24105ee231d535867e396df608e78002
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: information-technology
  method: project_sic_rule
  sic: '3577'
  sic_description: Computer Peripheral Equipment, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001016838.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/RDCM/README.md
full_history_commit: c6b3af0cefe967faceb0323aa590d422e87cbc29
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# RDCM — RADCOM LTD

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/RDCM/README.md)

## Business overview

Reported issuer name: **RADCOM LTD**. Stable SEC CIK: **0001016838**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| RDCM | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3577**: Computer Peripheral Equipment, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 144, 144/A, 20-F, 20-F/A, 3, 4, 424B3, 424B5, 6-K, CORRESP, CT ORDER, D, DEF 14A, EFFECT, F-3, F-3/A, F-3MEF, POS AM, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:30:51.568313+00:00.

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
| 2026-09-17 | 6-K | 0001213900-26-100745 | — | [S03] |
| 2026-09-09 | 6-K | 0001213900-26-098384 | — | [S04] |
| 2026-09-09 | SCHEDULE 13D/A | 0000921895-26-002520 | — | [S05] |
| 2026-08-12 | 6-K | 0001213900-26-088035 | — | [S06] |
| 2026-08-11 | 6-K | 0001213900-26-087495 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:47.626200+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001016838.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001213900-26-100745](https://www.sec.gov/Archives/edgar/data/1016838/000121390026100745/0001213900-26-100745-index.html) — published 2026-09-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001213900-26-098384](https://www.sec.gov/Archives/edgar/data/1016838/000121390026098384/0001213900-26-098384-index.html) — published 2026-09-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [SCHEDULE 13D/A 0000921895-26-002520](https://www.sec.gov/Archives/edgar/data/1016838/000092189526002520/0000921895-26-002520-index.html) — published 2026-09-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001213900-26-088035](https://www.sec.gov/Archives/edgar/data/1016838/000121390026088035/0001213900-26-088035-index.html) — published 2026-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001213900-26-087495](https://www.sec.gov/Archives/edgar/data/1016838/000121390026087495/0001213900-26-087495-index.html) — published 2026-08-11; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/RDCM/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
