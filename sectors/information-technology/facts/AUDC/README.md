---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001086434
cik: 0001086434
company_name: AUDIOCODES LTD
tickers:
- AUDC
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
  - 424B2
  - 424B3
  - 424B5
  - 6-K
  - 6-K/A
  - CORRESP
  - CT ORDER
  - EFFECT
  - F-3
  - F-3/A
  - F-3ASR
  - FWP
  - RW
  - S-8
  - S-8 POS
  - SC 13G
  - SC 13G/A
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001086434.json
    sha256: 886b265e602f7de6358fce52aa8254a1bdee8b2db3e5bbade17b286a488fe090
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001086434.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-27T15:25:33.739265+00:00'
  sha256: 29c7cedde394d9fb806c731f8be32ec8c78cad2668852342db80ae28619465f0
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001086434.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 886b265e602f7de6358fce52aa8254a1bdee8b2db3e5bbade17b286a488fe090
- id: S03
  title: 4 0001976408-26-000836
  url: https://www.sec.gov/Archives/edgar/data/1086434/000197640826000836/0001976408-26-000836-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001185185-26-003973
  url: https://www.sec.gov/Archives/edgar/data/1086434/000118518526003973/0001185185-26-003973-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001976408-26-000831
  url: https://www.sec.gov/Archives/edgar/data/1086434/000197640826000831/0001976408-26-000831-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001976408-26-000830
  url: https://www.sec.gov/Archives/edgar/data/1086434/000197640826000830/0001976408-26-000830-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001976408-26-000828
  url: https://www.sec.gov/Archives/edgar/data/1086434/000197640826000828/0001976408-26-000828-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001086434
  classification_status: reported_sic
  entity_type: other
  name: AUDIOCODES LTD
  sic: '3661'
  sic_description: Telephone & Telegraph Apparatus
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 886b265e602f7de6358fce52aa8254a1bdee8b2db3e5bbade17b286a488fe090
  url: https://data.sec.gov/submissions/CIK0001086434.json
listings:
- ticker: AUDC
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001185185-26-001124
  filed: '2026-03-30'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1086434/000118518526001124/0001185185-26-001124-index.html
- accession: 0001086434-04-000041
  filed: '2004-09-22'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1086434/000108643404000041/0001086434-04-000041-index.html
- accession: 0001185185-26-003973
  filed: '2026-09-14'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1086434/000118518526003973/0001185185-26-003973-index.html
- accession: 0001185185-25-000961
  filed: '2025-08-13'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1086434/000118518525000961/0001185185-25-000961-index.html
- accession: 0001144204-16-134543
  filed: '2016-11-15'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1086434/000114420416134543/0001144204-16-134543-index.html
research_progress:
  stage: pending
  input_sha256: b7683dd04a012927c74e73b403ee76bbba8c30cc6fc587fe4f291eda1a539b53
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
  sic: '3661'
  sic_description: Telephone & Telegraph Apparatus
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001086434.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/AUDC/README.md
full_history_commit: ea9dd09e5d047ff0620d4500849876915bb10e87
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AUDC — AUDIOCODES LTD

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/AUDC/README.md)

## Business overview

Reported issuer name: **AUDIOCODES LTD**. Stable SEC CIK: **0001086434**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AUDC | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **3661**: Telephone & Telegraph Apparatus. [S02]

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
- Forms observed in the retained filing inventory: 144, 144/A, 20-F, 20-F/A, 3, 4, 424B2, 424B3, 424B5, 6-K, 6-K/A, CORRESP, CT ORDER, EFFECT, F-3, F-3/A, F-3ASR, FWP, RW, S-8, S-8 POS, SC 13G, SC 13G/A, SC TO-I, SC TO-I/A, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:31:32.465335+00:00.

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
| 2026-09-14 | 4 | 0001976408-26-000836 | — | [S03] |
| 2026-09-14 | 6-K | 0001185185-26-003973 | — | [S04] |
| 2026-09-10 | 4 | 0001976408-26-000831 | — | [S05] |
| 2026-09-10 | 4 | 0001976408-26-000830 | — | [S06] |
| 2026-09-10 | 4 | 0001976408-26-000828 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:33.739265+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001086434.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0001976408-26-000836](https://www.sec.gov/Archives/edgar/data/1086434/000197640826000836/0001976408-26-000836-index.html) — published 2026-09-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001185185-26-003973](https://www.sec.gov/Archives/edgar/data/1086434/000118518526003973/0001185185-26-003973-index.html) — published 2026-09-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001976408-26-000831](https://www.sec.gov/Archives/edgar/data/1086434/000197640826000831/0001976408-26-000831-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001976408-26-000830](https://www.sec.gov/Archives/edgar/data/1086434/000197640826000830/0001976408-26-000830-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001976408-26-000828](https://www.sec.gov/Archives/edgar/data/1086434/000197640826000828/0001976408-26-000828-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/AUDC/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
