---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001529192
cik: 0001529192
company_name: Vipshop Holdings Ltd
tickers:
- VIPS
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
  - '144'
  - 20-F
  - '3'
  - '4'
  - 424B3
  - 424B4
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERTNYS
  - CORRESP
  - EFFECT
  - F-1
  - F-1/A
  - F-1MEF
  - F-3ASR
  - F-6
  - F-6EF
  - FWP
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001529192.json
    sha256: d16def91142541d4c518d6545540faa837a85730a8c0948ef651baef0c4c995f
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001529192.json
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
  url: https://data.sec.gov/submissions/CIK0001529192.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d16def91142541d4c518d6545540faa837a85730a8c0948ef651baef0c4c995f
- id: S03
  title: 4 0002111248-26-000004
  url: https://www.sec.gov/Archives/edgar/data/1529192/000211124826000004/0002111248-26-000004-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 4 0001972323-26-000008
  url: https://www.sec.gov/Archives/edgar/data/1529192/000197232326000008/0001972323-26-000008-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0002114343-26-000002
  url: https://www.sec.gov/Archives/edgar/data/1529192/000211434326000002/0002114343-26-000002-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001501343-26-000004
  url: https://www.sec.gov/Archives/edgar/data/1529192/000150134326000004/0001501343-26-000004-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001104659-26-100484
  url: https://www.sec.gov/Archives/edgar/data/1529192/000110465926100484/0001104659-26-100484-index.html
  published_at: '2026-08-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001529192
  classification_status: reported_sic
  entity_type: other
  name: Vipshop Holdings Ltd
  sic: '5961'
  sic_description: Retail-Catalog & Mail-Order Houses
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d16def91142541d4c518d6545540faa837a85730a8c0948ef651baef0c4c995f
  url: https://data.sec.gov/submissions/CIK0001529192.json
listings:
- ticker: VIPS
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001104659-26-044015
  filed: '2026-04-16'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1529192/000110465926044015/0001104659-26-044015-index.html
- accession: 0001104659-26-100484
  filed: '2026-08-25'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1529192/000110465926100484/0001104659-26-100484-index.html
- accession: 0001193125-21-167325
  filed: '2021-05-20'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1529192/000119312521167325/0001193125-21-167325-index.html
research_progress:
  stage: pending
  input_sha256: b8d65cfb40eb254cc2a7a9d8add9925e532f25d05d5893b593419f54a9334960
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: consumer-discretionary
  method: project_sic_rule
  sic: '5961'
  sic_description: Retail-Catalog & Mail-Order Houses
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001529192.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/VIPS/README.md
full_history_commit: 71fcd4775048604503d616351f7f309068b23e1b
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# VIPS — Vipshop Holdings Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/VIPS/README.md)

## Business overview

Reported issuer name: **Vipshop Holdings Ltd**. Stable SEC CIK: **0001529192**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| VIPS | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **5961**: Retail-Catalog & Mail-Order Houses. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **consumer-discretionary**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

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
- Forms observed in the retained filing inventory: 144, 20-F, 3, 4, 424B3, 424B4, 424B5, 6-K, 6-K/A, 8-A12B, CERTNYS, CORRESP, EFFECT, F-1, F-1/A, F-1MEF, F-3ASR, F-6, F-6EF, FWP, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SC TO-I, SC TO-I/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:33:56.791460+00:00.

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
| 2026-10-15 | 4 | 0002111248-26-000004 | — | [S03] |
| 2026-10-15 | 4 | 0001972323-26-000008 | — | [S04] |
| 2026-09-10 | 4 | 0002114343-26-000002 | — | [S05] |
| 2026-09-10 | 4 | 0001501343-26-000004 | — | [S06] |
| 2026-08-25 | 6-K | 0001104659-26-100484 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:48.334682+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001529192.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0002111248-26-000004](https://www.sec.gov/Archives/edgar/data/1529192/000211124826000004/0002111248-26-000004-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [4 0001972323-26-000008](https://www.sec.gov/Archives/edgar/data/1529192/000197232326000008/0001972323-26-000008-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0002114343-26-000002](https://www.sec.gov/Archives/edgar/data/1529192/000211434326000002/0002114343-26-000002-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001501343-26-000004](https://www.sec.gov/Archives/edgar/data/1529192/000150134326000004/0001501343-26-000004-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001104659-26-100484](https://www.sec.gov/Archives/edgar/data/1529192/000110465926100484/0001104659-26-100484-index.html) — published 2026-08-25; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/71fcd4775048604503d616351f7f309068b23e1b/brain/companies/VIPS/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
