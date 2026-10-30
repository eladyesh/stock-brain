---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001538847
cik: 0001538847
company_name: GoldMining Inc.
tickers:
- GLDG
status: stub
canonical_reviewed: false
as_of: '2026-10-30'
updated_at: '2026-10-30T16:05:25.650854+00:00'
reviewed_at: null
coverage_release: coverage-20261030-41085569265-1
source_commit: f9a34108789a82bf7c75f9d65a0e9552aa5552db
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '3'
  - '4'
  - 4/A
  - 40-F
  - 40-F/A
  - 40FR12B
  - 6-K
  - 6-K/A
  - CERT
  - D
  - D/A
  - EFFECT
  - F-10
  - F-10/A
  - F-X
  - SC 13D
  - SC 13G
  - SC 13G/A
  - SEC STAFF ACTION
  - SUPPL
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001538847.json
    sha256: d6e9be656fa34aaae435851b8e2e5f9118e8da61ed164225873898caf5d3bd57
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001538847.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-30T16:00:12.358089+00:00'
  sha256: a960a0bfc5439fac9e467fe07ef1f44afe893ba2afc3297648321a80ce09971e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001538847.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d6e9be656fa34aaae435851b8e2e5f9118e8da61ed164225873898caf5d3bd57
- id: S03
  title: 6-K 0001437749-26-033327
  url: https://www.sec.gov/Archives/edgar/data/1538847/000143774926033327/0001437749-26-033327-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001437749-26-032624
  url: https://www.sec.gov/Archives/edgar/data/1538847/000143774926032624/0001437749-26-032624-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001437749-26-032599
  url: https://www.sec.gov/Archives/edgar/data/1538847/000143774926032599/0001437749-26-032599-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001437749-26-032098
  url: https://www.sec.gov/Archives/edgar/data/1538847/000143774926032098/0001437749-26-032098-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001437749-26-024036
  url: https://www.sec.gov/Archives/edgar/data/1538847/000143774926024036/0001437749-26-024036-index.html
  published_at: '2026-07-22'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1538847/000143774926006120/gldmn20251130_40f.htm
  title: 40-F 0001437749-26-006120
  published_at: '2026-02-27'
  retrieved_at: '2026-10-27T15:39:44.710654+00:00'
  sha256: 16ed07be8eaace8f3b7999f587aaf48e21a1472dec3412c2322b0dbaf5b6c5a1
issuer_classification:
  cik: 0001538847
  classification_status: reported_sic
  entity_type: other
  name: GoldMining Inc.
  sic: '1040'
  sic_description: Gold and Silver Ores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: d6e9be656fa34aaae435851b8e2e5f9118e8da61ed164225873898caf5d3bd57
  url: https://data.sec.gov/submissions/CIK0001538847.json
listings:
- ticker: GLDG
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0001437749-26-006120
  filed: '2026-02-27'
  form: 40-F
  url: https://www.sec.gov/Archives/edgar/data/1538847/000143774926006120/0001437749-26-006120-index.html
- accession: 0001437749-22-004908
  filed: '2022-03-01'
  form: 40-F/A
  url: https://www.sec.gov/Archives/edgar/data/1538847/000143774922004908/0001437749-22-004908-index.html
- accession: 0001437749-26-033327
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1538847/000143774926033327/0001437749-26-033327-index.html
- accession: 0001437749-24-014415
  filed: '2024-05-03'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1538847/000143774924014415/0001437749-24-014415-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 69eaa5014e3c65877a83cc15e1daf86b4cfa498d413b351a10cca77134c89bf3
  last_attempt_at: '2026-10-27T15:36:38.956292+00:00'
  last_success_at: '2026-10-27T15:36:38.956292+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - management-and-governance
  - recent-developments
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
  source_url: https://data.sec.gov/submissions/CIK0001538847.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/GLDG/README.md
full_history_commit: 1b4771bc41dec553e210323f72d9bfc908288c04
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# GLDG — GoldMining Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/GLDG/README.md)

## Business overview

Reported issuer name: **GoldMining Inc.**. Stable SEC CIK: **0001538847**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| GLDG | NYSE_AMERICAN | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 40-F, filed 2026-02-27, L131:

> Attestation report of the registered public accounting firm. In accordance with the United States Jumpstart Our Business Startup Act (the “JOBS Act”), the Company qualifies as an “emerging growth company” (an “EGC”), which entitles the Company to take advantage of certain exemptions from various reporting requirements. Specifically, the JOBS Act defers the requirement to have the Company’s independent auditor assess the Company’s internal controls over financial reporting under Section 404(b) of the Sarbanes-Oxley Act for so long as the Company remains an EGC. Accordingly, this Annual Report on Form 40-F does not include an attestation report of the Company’s registered public accounting firm due to the Company’s status as an EGC. [S54]

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

Source excerpt — 40-F, filed 2026-02-27, L79:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

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
- Forms observed in the retained filing inventory: 3, 4, 4/A, 40-F, 40-F/A, 40FR12B, 6-K, 6-K/A, CERT, D, D/A, EFFECT, F-10, F-10/A, F-X, SC 13D, SC 13G, SC 13G/A, SEC STAFF ACTION, SUPPL
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:34:02.197177+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (evidence or analysis still needed): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (evidence or analysis still needed): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (evidence or analysis still needed): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (evidence or analysis still needed): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
- **Growth drivers** (evidence or analysis still needed): Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.
- **Financial performance** (evidence or analysis still needed): Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.
- **Balance sheet and capital allocation** (evidence or analysis still needed): Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.
- **Management and governance** (source excerpts available; assess the claim): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
- **Valuation context** (evidence or analysis still needed): Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.
- **Catalysts** (evidence or analysis still needed): List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.
- **Risks and thesis breakers** (evidence or analysis still needed): Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.
- **Scenarios and open questions** (evidence or analysis still needed): Separate bull, base, and bear assumptions from facts. Record missing data, disputed evidence, and research questions without inventing answers.
- **Relationships and themes** (evidence or analysis still needed): Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.
- **Recent developments** (source excerpts available; assess the claim): Keep a dated, source-backed log of material changes. Distinguish the event date from the article date and explain what changed in the profile.

Calculation gaps: Validated financial history is missing.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest five available filing metadata records; document bodies have not been analyzed here.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-23 | 6-K | 0001437749-26-033327 | — | [S03] |
| 2026-10-14 | 6-K | 0001437749-26-032624 | — | [S04] |
| 2026-10-14 | 6-K | 0001437749-26-032599 | — | [S05] |
| 2026-10-06 | 6-K | 0001437749-26-032098 | — | [S06] |
| 2026-07-22 | 6-K | 0001437749-26-024036 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-30T16:00:12.358089+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001538847.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001437749-26-033327](https://www.sec.gov/Archives/edgar/data/1538847/000143774926033327/0001437749-26-033327-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001437749-26-032624](https://www.sec.gov/Archives/edgar/data/1538847/000143774926032624/0001437749-26-032624-index.html) — published 2026-10-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001437749-26-032599](https://www.sec.gov/Archives/edgar/data/1538847/000143774926032599/0001437749-26-032599-index.html) — published 2026-10-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001437749-26-032098](https://www.sec.gov/Archives/edgar/data/1538847/000143774926032098/0001437749-26-032098-index.html) — published 2026-10-06; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001437749-26-024036](https://www.sec.gov/Archives/edgar/data/1538847/000143774926024036/0001437749-26-024036-index.html) — published 2026-07-22; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [40-F 0001437749-26-006120](https://www.sec.gov/Archives/edgar/data/1538847/000143774926006120/gldmn20251130_40f.htm) — published 2026-02-27; retrieved 2026-10-27T15:39:44.710654+00:00.

Source release: `coverage-20261030-41085569265-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/1b4771bc41dec553e210323f72d9bfc908288c04/brain/companies/GLDG/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
