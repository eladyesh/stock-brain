---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001576789
cik: 0001576789
company_name: Wix.com Ltd.
tickers:
- WIX
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
  - '144'
  - 144/A
  - 20-F
  - '3'
  - '4'
  - 424B4
  - 6-K
  - 8-A12B
  - CB
  - CERTNAS
  - CORRESP
  - CT ORDER
  - DRS
  - DRS/A
  - EFFECT
  - F-1
  - F-1/A
  - F-X
  - RW
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001576789.json
    sha256: bba9a4e627ff4b81656acc01dab75713c7ff483718c31824dc5d29afd1bb692e
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001576789.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-29T16:14:13.115716+00:00'
  sha256: 0695ffec283534755d4efe90771a9cacee840d7affb7ba717f62899195a301c6
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001576789.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: bba9a4e627ff4b81656acc01dab75713c7ff483718c31824dc5d29afd1bb692e
- id: S03
  title: 144 0001976408-26-000795
  url: https://www.sec.gov/Archives/edgar/data/1576789/000197640826000795/0001976408-26-000795-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 144 0001976408-26-000794
  url: https://www.sec.gov/Archives/edgar/data/1576789/000197640826000794/0001976408-26-000794-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001628280-26-059988
  url: https://www.sec.gov/Archives/edgar/data/1576789/000162828026059988/0001628280-26-059988-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001628280-26-059986
  url: https://www.sec.gov/Archives/edgar/data/1576789/000162828026059986/0001628280-26-059986-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001628280-26-059984
  url: https://www.sec.gov/Archives/edgar/data/1576789/000162828026059984/0001628280-26-059984-index.html
  published_at: '2026-09-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001576789
  classification_status: reported_sic
  entity_type: other
  name: Wix.com Ltd.
  sic: '7370'
  sic_description: Services-Computer Programming, Data Processing, Etc.
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: bba9a4e627ff4b81656acc01dab75713c7ff483718c31824dc5d29afd1bb692e
  url: https://data.sec.gov/submissions/CIK0001576789.json
listings:
- ticker: WIX
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-015222
  filed: '2026-03-05'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1576789/000162828026015222/0001628280-26-015222-index.html
- accession: 0001628280-26-052108
  filed: '2026-08-04'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1576789/000162828026052108/0001628280-26-052108-index.html
research_progress:
  stage: pending
  input_sha256: 237a5aeaa0006353a53f864e00060799cfb072ada3034a045136aaeeece44be1
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
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/WIX/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# WIX — Wix.com Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/WIX/README.md)

## Business overview

Reported issuer name: **Wix.com Ltd.**. Stable SEC CIK: **0001576789**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| WIX | NASDAQ | common_stock | 1 | [S01] |

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
- Forms observed in the retained filing inventory: 144, 144/A, 20-F, 3, 4, 424B4, 6-K, 8-A12B, CB, CERTNAS, CORRESP, CT ORDER, DRS, DRS/A, EFFECT, F-1, F-1/A, F-X, RW, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SC TO-I, SC TO-I/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:34:15.374162+00:00.

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
| 2026-09-02 | 144 | 0001976408-26-000795 | — | [S03] |
| 2026-09-02 | 144 | 0001976408-26-000794 | — | [S04] |
| 2026-09-02 | 4 | 0001628280-26-059988 | — | [S05] |
| 2026-09-02 | 4 | 0001628280-26-059986 | — | [S06] |
| 2026-09-02 | 4 | 0001628280-26-059984 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.115716+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001576789.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [144 0001976408-26-000795](https://www.sec.gov/Archives/edgar/data/1576789/000197640826000795/0001976408-26-000795-index.html) — published 2026-09-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [144 0001976408-26-000794](https://www.sec.gov/Archives/edgar/data/1576789/000197640826000794/0001976408-26-000794-index.html) — published 2026-09-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001628280-26-059988](https://www.sec.gov/Archives/edgar/data/1576789/000162828026059988/0001628280-26-059988-index.html) — published 2026-09-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001628280-26-059986](https://www.sec.gov/Archives/edgar/data/1576789/000162828026059986/0001628280-26-059986-index.html) — published 2026-09-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001628280-26-059984](https://www.sec.gov/Archives/edgar/data/1576789/000162828026059984/0001628280-26-059984-index.html) — published 2026-09-02; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/WIX/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
