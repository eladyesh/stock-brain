---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001023512
cik: '0001023512'
company_name: DRDGOLD LTD
tickers:
- DRD
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
  - 20-F
  - 20-F/A
  - '25'
  - '3'
  - '4'
  - 424B3
  - 6-K
  - 8-A12B
  - CB
  - CB/A
  - CERTNYS
  - CORRESP
  - EFFECT
  - F-3
  - F-3/A
  - F-4
  - F-6
  - F-6 POS
  - F-6EF
  - F-X
  - POS AM
  - RW
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-I
  - SC TO-I/A
  - SD
  - T-3
  - T-3/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001023512.json
    sha256: 24ac3e4fc0230f79286863e813b330c0d221a41b5edb0b83b2e7d16f1b1ccefd
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001023512.json
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
  url: https://data.sec.gov/submissions/CIK0001023512.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 24ac3e4fc0230f79286863e813b330c0d221a41b5edb0b83b2e7d16f1b1ccefd
- id: S03
  title: 6-K 0001628280-26-066821
  url: https://www.sec.gov/Archives/edgar/data/1023512/000162828026066821/0001628280-26-066821-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001628280-26-066589
  url: https://www.sec.gov/Archives/edgar/data/1023512/000162828026066589/0001628280-26-066589-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001628280-26-064357
  url: https://www.sec.gov/Archives/edgar/data/1023512/000162828026064357/0001628280-26-064357-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 20-F 0001628280-26-064355
  url: https://www.sec.gov/Archives/edgar/data/1023512/000162828026064355/0001628280-26-064355-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001628280-26-063927
  url: https://www.sec.gov/Archives/edgar/data/1023512/000162828026063927/0001628280-26-063927-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001023512'
  classification_status: reported_sic
  entity_type: other
  name: DRDGOLD LTD
  sic: '1040'
  sic_description: Gold and Silver Ores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 24ac3e4fc0230f79286863e813b330c0d221a41b5edb0b83b2e7d16f1b1ccefd
  url: https://data.sec.gov/submissions/CIK0001023512.json
listings:
- ticker: DRD
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001628280-26-064355
  filed: '2026-10-02'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1023512/000162828026064355/0001628280-26-064355-index.html
- accession: 0001023512-23-000062
  filed: '2023-10-31'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1023512/000102351223000062/0001023512-23-000062-index.html
- accession: 0001562762-23-000161
  filed: '2023-04-12'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1023512/000156276223000161/0001562762-23-000161-index.html
- accession: 0001562762-22-000446
  filed: '2022-11-08'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1023512/000156276222000446/0001562762-22-000446-index.html
- accession: 0001023512-19-000028
  filed: '2019-11-29'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1023512/000102351219000028/0001023512-19-000028-index.html
- accession: 0001023512-18-000010
  filed: '2018-12-03'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1023512/000102351218000010/0001023512-18-000010-index.html
- accession: 0001341004-18-000612
  filed: '2018-11-07'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1023512/000134100418000612/0001341004-18-000612-index.html
- accession: 0001205613-07-000164
  filed: '2007-12-13'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1023512/000120561307000164/0001205613-07-000164-index.html
- accession: 0001156973-05-000583
  filed: '2005-04-29'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1023512/000115697305000583/0001156973-05-000583-index.html
- accession: 0000950172-05-001034
  filed: '2005-04-01'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1023512/000095017205001034/0000950172-05-001034-index.html
- accession: 0000950123-04-014374
  filed: '2004-12-03'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1023512/000095012304014374/0000950123-04-014374-index.html
- accession: 0001047469-03-032067
  filed: '2003-09-30'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1023512/000104746903032067/0001047469-03-032067-index.html
research_progress:
  stage: pending
  input_sha256: f121ff00add206e87535e9f1a74ba479923ea09137f125908ec66b1e34e7314a
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: materials
  method: project_sic_rule
  sic: '1040'
  sic_description: Gold and Silver Ores
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001023512.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/DRD/README.md
full_history_commit: c6b3af0cefe967faceb0323aa590d422e87cbc29
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# DRD — DRDGOLD LTD

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/DRD/README.md)

## Business overview

Reported issuer name: **DRDGOLD LTD**. Stable SEC CIK: **0001023512**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| DRD | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1040**: Gold and Silver Ores. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **materials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 25, 3, 4, 424B3, 6-K, 8-A12B, CB, CB/A, CERTNYS, CORRESP, EFFECT, F-3, F-3/A, F-4, F-6, F-6 POS, F-6EF, F-X, POS AM, RW, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SC TO-I, SC TO-I/A, SD, T-3, T-3/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:30:56.182385+00:00.

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
| 2026-10-22 | 6-K | 0001628280-26-066821 | — | [S03] |
| 2026-10-21 | 6-K | 0001628280-26-066589 | — | [S04] |
| 2026-10-02 | 6-K | 0001628280-26-064357 | — | [S05] |
| 2026-10-02 | 20-F | 0001628280-26-064355 | — | [S06] |
| 2026-09-30 | 6-K | 0001628280-26-063927 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:48.334682+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001023512.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001628280-26-066821](https://www.sec.gov/Archives/edgar/data/1023512/000162828026066821/0001628280-26-066821-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001628280-26-066589](https://www.sec.gov/Archives/edgar/data/1023512/000162828026066589/0001628280-26-066589-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001628280-26-064357](https://www.sec.gov/Archives/edgar/data/1023512/000162828026064357/0001628280-26-064357-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [20-F 0001628280-26-064355](https://www.sec.gov/Archives/edgar/data/1023512/000162828026064355/0001628280-26-064355-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001628280-26-063927](https://www.sec.gov/Archives/edgar/data/1023512/000162828026063927/0001628280-26-063927-index.html) — published 2026-09-30; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c6b3af0cefe967faceb0323aa590d422e87cbc29/brain/companies/DRD/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
