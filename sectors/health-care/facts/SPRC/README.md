---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001611746
cik: '0001611746'
company_name: SciSparc Ltd.
tickers:
- SPRC
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
  - '144'
  - 20-F
  - 20-F/A
  - 25-NSE
  - '3'
  - 3/A
  - '4'
  - 424B2
  - 424B3
  - 424B4
  - 424B5
  - '425'
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CERTNAS
  - CORRESP
  - CT ORDER
  - D
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-1MEF
  - F-3
  - F-3/A
  - F-4
  - F-4/A
  - F-6
  - F-6 POS
  - FWP
  - NT 20-F
  - POS AM
  - RW
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001611746.json
    sha256: 7fcbbaee964d1494f0d5716f9898fa0715b7f023da93b7dec5d35087e6f7df7d
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001611746.json
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
  url: https://data.sec.gov/submissions/CIK0001611746.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 7fcbbaee964d1494f0d5716f9898fa0715b7f023da93b7dec5d35087e6f7df7d
- id: S03
  title: 6-K 0001213900-26-109727
  url: https://www.sec.gov/Archives/edgar/data/1611746/000121390026109727/0001213900-26-109727-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-109675
  url: https://www.sec.gov/Archives/edgar/data/1611746/000121390026109675/0001213900-26-109675-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-107436
  url: https://www.sec.gov/Archives/edgar/data/1611746/000121390026107436/0001213900-26-107436-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-105319
  url: https://www.sec.gov/Archives/edgar/data/1611746/000121390026105319/0001213900-26-105319-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001213900-26-102810
  url: https://www.sec.gov/Archives/edgar/data/1611746/000121390026102810/0001213900-26-102810-index.html
  published_at: '2026-09-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: '0001611746'
  classification_status: reported_sic
  entity_type: other
  name: SciSparc Ltd.
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 7fcbbaee964d1494f0d5716f9898fa0715b7f023da93b7dec5d35087e6f7df7d
  url: https://data.sec.gov/submissions/CIK0001611746.json
listings:
- ticker: SPRC
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-049322
  filed: '2026-04-29'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1611746/000121390026049322/0001213900-26-049322-index.html
- accession: 0001213900-26-091427
  filed: '2026-08-19'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1611746/000121390026091427/0001213900-26-091427-index.html
- accession: 0001213900-24-038779
  filed: '2024-05-02'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1611746/000121390024038779/0001213900-24-038779-index.html
- accession: 0001213900-26-109727
  filed: '2026-10-15'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1611746/000121390026109727/0001213900-26-109727-index.html
- accession: 0001213900-21-045064
  filed: '2021-08-26'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1611746/000121390021045064/0001213900-21-045064-index.html
research_progress:
  stage: pending
  input_sha256: f730eb598fc5acc8b22f66eefff14a6294d0c272c88eba4b95cb4b2c9afd2123
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: health-care
  method: project_sic_rule
  sic: '2834'
  sic_description: Pharmaceutical Preparations
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001611746.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/SPRC/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SPRC — SciSparc Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/SPRC/README.md)

## Business overview

Reported issuer name: **SciSparc Ltd.**. Stable SEC CIK: **0001611746**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SPRC | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 25-NSE, 3, 3/A, 4, 424B2, 424B3, 424B4, 424B5, 425, 6-K, 6-K/A, 8-A12B, CERT, CERTNAS, CORRESP, CT ORDER, D, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-1MEF, F-3, F-3/A, F-4, F-4/A, F-6, F-6 POS, FWP, NT 20-F, POS AM, RW, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-23T14:31:45.779015+00:00.

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
| 2026-10-15 | 6-K | 0001213900-26-109727 | — | [S03] |
| 2026-10-15 | 6-K | 0001213900-26-109675 | — | [S04] |
| 2026-10-07 | 6-K | 0001213900-26-107436 | — | [S05] |
| 2026-09-30 | 6-K | 0001213900-26-105319 | — | [S06] |
| 2026-09-24 | 6-K | 0001213900-26-102810 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:54.530395+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001611746.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001213900-26-109727](https://www.sec.gov/Archives/edgar/data/1611746/000121390026109727/0001213900-26-109727-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001213900-26-109675](https://www.sec.gov/Archives/edgar/data/1611746/000121390026109675/0001213900-26-109675-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001213900-26-107436](https://www.sec.gov/Archives/edgar/data/1611746/000121390026107436/0001213900-26-107436-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001213900-26-105319](https://www.sec.gov/Archives/edgar/data/1611746/000121390026105319/0001213900-26-105319-index.html) — published 2026-09-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001213900-26-102810](https://www.sec.gov/Archives/edgar/data/1611746/000121390026102810/0001213900-26-102810-index.html) — published 2026-09-24; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/SPRC/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
