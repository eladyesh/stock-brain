---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001826168
cik: 0001826168
company_name: TIM S.A.
tickers:
- TIMB
status: stub
canonical_reviewed: false
as_of: '2026-10-29'
updated_at: '2026-10-29T16:18:46.634043+00:00'
reviewed_at: null
coverage_release: coverage-20261029-40909364006-1
source_commit: aa19db75827ed3c73031b70e9a0a2e63baffc491
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
  - '4'
  - 6-K
  - 6-K/A
  - 8-K12B
  - EFFECT
  - F-6
  - IRANNOTICE
  - SC 13D/A
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001826168.json
    sha256: 0c70ed19db30cee2729c9c73b451c87193645116e1d2a2a0f7f4794bbd0bcba5
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001826168.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-29T16:14:13.951866+00:00'
  sha256: 2ac9bdaf5d770442eb34b0b33eb6a5240dbd11a3f2077f7b88051dbb82d4313b
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001826168.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 0c70ed19db30cee2729c9c73b451c87193645116e1d2a2a0f7f4794bbd0bcba5
- id: S03
  title: 6-K 0001292814-26-004896
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281426004896/0001292814-26-004896-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001292814-26-004848
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281426004848/0001292814-26-004848-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001292814-26-004720
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281426004720/0001292814-26-004720-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001292814-26-004718
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281426004718/0001292814-26-004718-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001292814-26-004601
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281426004601/0001292814-26-004601-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001826168
  classification_status: reported_sic
  entity_type: other
  name: TIM S.A.
  sic: '4813'
  sic_description: Telephone Communications (No Radiotelephone)
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 0c70ed19db30cee2729c9c73b451c87193645116e1d2a2a0f7f4794bbd0bcba5
  url: https://data.sec.gov/submissions/CIK0001826168.json
listings:
- ticker: TIMB
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001292814-26-001915
  filed: '2026-03-30'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281426001915/0001292814-26-001915-index.html
- accession: 0001292814-25-001285
  filed: '2025-04-01'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281425001285/0001292814-25-001285-index.html
- accession: 0001292814-26-004896
  filed: '2026-10-09'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281426004896/0001292814-26-004896-index.html
- accession: 0001292814-24-000733
  filed: '2024-03-11'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281424000733/0001292814-24-000733-index.html
- accession: 0001292814-24-000396
  filed: '2024-02-09'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281424000396/0001292814-24-000396-index.html
- accession: 0001292814-23-004473
  filed: '2023-11-07'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281423004473/0001292814-23-004473-index.html
- accession: 0001292814-23-004466
  filed: '2023-11-07'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281423004466/0001292814-23-004466-index.html
- accession: 0001292814-23-000538
  filed: '2023-02-21'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281423000538/0001292814-23-000538-index.html
- accession: 0001292814-22-002130
  filed: '2022-05-06'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281422002130/0001292814-22-002130-index.html
- accession: 0001292814-21-004269
  filed: '2021-11-08'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1826168/000129281421004269/0001292814-21-004269-index.html
research_progress:
  stage: pending
  input_sha256: 59ee509433bd64226a967360c3ec6915892023d31345138e2dbd06fb6017d429
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: communication-services
  method: project_sic_rule
  sic: '4813'
  sic_description: Telephone Communications (No Radiotelephone)
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001826168.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/TIMB/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# TIMB — TIM S.A.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/TIMB/README.md)

## Business overview

Reported issuer name: **TIM S.A.**. Stable SEC CIK: **0001826168**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| TIMB | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **4813**: Telephone Communications (No Radiotelephone). [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **communication-services**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 3, 4, 6-K, 6-K/A, 8-K12B, EFFECT, F-6, IRANNOTICE, SC 13D/A
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:55.696063+00:00.

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
| 2026-10-09 | 6-K | 0001292814-26-004896 | — | [S03] |
| 2026-10-05 | 6-K | 0001292814-26-004848 | — | [S04] |
| 2026-09-28 | 6-K | 0001292814-26-004720 | — | [S05] |
| 2026-09-28 | 6-K | 0001292814-26-004718 | — | [S06] |
| 2026-09-21 | 6-K | 0001292814-26-004601 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.951866+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001826168.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001292814-26-004896](https://www.sec.gov/Archives/edgar/data/1826168/000129281426004896/0001292814-26-004896-index.html) — published 2026-10-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001292814-26-004848](https://www.sec.gov/Archives/edgar/data/1826168/000129281426004848/0001292814-26-004848-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001292814-26-004720](https://www.sec.gov/Archives/edgar/data/1826168/000129281426004720/0001292814-26-004720-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001292814-26-004718](https://www.sec.gov/Archives/edgar/data/1826168/000129281426004718/0001292814-26-004718-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001292814-26-004601](https://www.sec.gov/Archives/edgar/data/1826168/000129281426004601/0001292814-26-004601-index.html) — published 2026-09-21; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/TIMB/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
