---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001926792
cik: 0001926792
company_name: SAMFINE CREATION HOLDINGS GROUP Ltd
tickers:
- SFHG
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
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - '3'
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
  - S-8
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001926792.json
    sha256: 556e3337dcea46c396f594074d65bb76a0d06efe823edb698dc4dd905d5c0c49
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001926792.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-26T16:11:31.228419+00:00'
  sha256: 74146fcda2f9b3b43b06280df0ad9584dffa78b2237460917eda3c2892e7a706
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001926792.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 556e3337dcea46c396f594074d65bb76a0d06efe823edb698dc4dd905d5c0c49
- id: S03
  title: 6-K 0001213900-26-104636
  url: https://www.sec.gov/Archives/edgar/data/1926792/000121390026104636/0001213900-26-104636-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: F-1/A 0001213900-26-073604
  url: https://www.sec.gov/Archives/edgar/data/1926792/000121390026073604/0001213900-26-073604-index.html
  published_at: '2026-06-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: F-1 0001213900-26-067533
  url: https://www.sec.gov/Archives/edgar/data/1926792/000121390026067533/0001213900-26-067533-index.html
  published_at: '2026-06-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: DRS 0001213900-26-057971
  url: https://www.sec.gov/Archives/edgar/data/1926792/000121390026057971/0001213900-26-057971-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 3 0001213900-26-042058
  url: https://www.sec.gov/Archives/edgar/data/1926792/000121390026042058/0001213900-26-042058-index.html
  published_at: '2026-04-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001926792
  classification_status: reported_sic
  entity_type: other
  name: SAMFINE CREATION HOLDINGS GROUP Ltd
  sic: '2750'
  sic_description: Commercial Printing
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 556e3337dcea46c396f594074d65bb76a0d06efe823edb698dc4dd905d5c0c49
  url: https://data.sec.gov/submissions/CIK0001926792.json
listings:
- ticker: SFHG
  exchange: NASDAQ
  instrument_type: equity_candidate
research_filings:
- accession: 0001213900-26-035532
  filed: '2026-03-27'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1926792/000121390026035532/0001213900-26-035532-index.html
- accession: 0001213900-26-104636
  filed: '2026-09-29'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1926792/000121390026104636/0001213900-26-104636-index.html
- accession: 0001213900-25-035233
  filed: '2025-04-25'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1926792/000121390025035233/0001213900-25-035233-index.html
research_progress:
  stage: pending
  input_sha256: 27214aa4ebf29c2467798026ebb781b40746fc8d34b9635124fe0fbb796b0c17
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
  sic: '2750'
  sic_description: Commercial Printing
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001926792.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/SFHG/README.md
full_history_commit: 6ec0c5a139b27efe3be9111dc20cf938bd839c1e
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# SFHG — SAMFINE CREATION HOLDINGS GROUP Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/SFHG/README.md)

## Business overview

Reported issuer name: **SAMFINE CREATION HOLDINGS GROUP Ltd**. Stable SEC CIK: **0001926792**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| SFHG | NASDAQ | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2750**: Commercial Printing. [S02]

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
- Forms observed in the retained filing inventory: 20-F, 3, 424B4, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, FWP, S-8, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:23.160746+00:00.

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
| 2026-09-29 | 6-K | 0001213900-26-104636 | — | [S03] |
| 2026-06-30 | F-1/A | 0001213900-26-073604 | — | [S04] |
| 2026-06-11 | F-1 | 0001213900-26-067533 | — | [S05] |
| 2026-05-15 | DRS | 0001213900-26-057971 | — | [S06] |
| 2026-04-09 | 3 | 0001213900-26-042058 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.228419+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001926792.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001213900-26-104636](https://www.sec.gov/Archives/edgar/data/1926792/000121390026104636/0001213900-26-104636-index.html) — published 2026-09-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [F-1/A 0001213900-26-073604](https://www.sec.gov/Archives/edgar/data/1926792/000121390026073604/0001213900-26-073604-index.html) — published 2026-06-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [F-1 0001213900-26-067533](https://www.sec.gov/Archives/edgar/data/1926792/000121390026067533/0001213900-26-067533-index.html) — published 2026-06-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [DRS 0001213900-26-057971](https://www.sec.gov/Archives/edgar/data/1926792/000121390026057971/0001213900-26-057971-index.html) — published 2026-05-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [3 0001213900-26-042058](https://www.sec.gov/Archives/edgar/data/1926792/000121390026042058/0001213900-26-042058-index.html) — published 2026-04-09; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/SFHG/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
