---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001981662
cik: 0001981662
company_name: NewGenIvf Group Ltd
tickers:
- NIVF
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
  - 20-F/A
  - '3'
  - 3/A
  - '4'
  - 424B3
  - 424B4
  - '425'
  - 6-K
  - 6-K/A
  - 8-K12B
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-4
  - F-4/A
  - NT 20-F
  - RW
  - SC 13D
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001981662.json
    sha256: d08075ab75a13e9a15831c39d24e6a8cae7e3e434492bf8c7854458085b99b78
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001981662.json
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
  url: https://data.sec.gov/submissions/CIK0001981662.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d08075ab75a13e9a15831c39d24e6a8cae7e3e434492bf8c7854458085b99b78
- id: S03
  title: 6-K 0001213900-26-111191
  url: https://www.sec.gov/Archives/edgar/data/1981662/000121390026111191/0001213900-26-111191-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-107570
  url: https://www.sec.gov/Archives/edgar/data/1981662/000121390026107570/0001213900-26-107570-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-107372
  url: https://www.sec.gov/Archives/edgar/data/1981662/000121390026107372/0001213900-26-107372-index.html
  published_at: '2026-10-07'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: SCHEDULE 13D/A 0001213900-26-107054
  url: https://www.sec.gov/Archives/edgar/data/1981662/000121390026107054/0001213900-26-107054-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001213900-26-107053
  url: https://www.sec.gov/Archives/edgar/data/1981662/000121390026107053/0001213900-26-107053-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001981662
  classification_status: reported_sic
  entity_type: other
  name: NewGenIvf Group Ltd
  sic: '8090'
  sic_description: Services-Misc Health & Allied Services, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d08075ab75a13e9a15831c39d24e6a8cae7e3e434492bf8c7854458085b99b78
  url: https://data.sec.gov/submissions/CIK0001981662.json
listings:
- ticker: NIVF
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-037687
  filed: '2026-03-31'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1981662/000121390026037687/0001213900-26-037687-index.html
- accession: 0001213900-25-043940
  filed: '2025-05-15'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1981662/000121390025043940/0001213900-25-043940-index.html
- accession: 0001213900-26-111191
  filed: '2026-10-21'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1981662/000121390026111191/0001213900-26-111191-index.html
- accession: 0001213900-25-011296
  filed: '2025-02-07'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1981662/000121390025011296/0001213900-25-011296-index.html
research_progress:
  stage: pending
  input_sha256: 3a29d8eec374ff7e403fa5d9edc4e390cdcc633a482abb080e3aa29194322714
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
  sic: '8090'
  sic_description: Services-Misc Health & Allied Services, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001981662.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/NIVF/README.md
full_history_commit: 6ec0c5a139b27efe3be9111dc20cf938bd839c1e
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# NIVF — NewGenIvf Group Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/NIVF/README.md)

## Business overview

Reported issuer name: **NewGenIvf Group Ltd**. Stable SEC CIK: **0001981662**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| NIVF | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **8090**: Services-Misc Health & Allied Services, NEC. [S02]

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
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 3, 3/A, 4, 424B3, 424B4, 425, 6-K, 6-K/A, 8-K12B, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-4, F-4/A, NT 20-F, RW, SC 13D, SC 13G, SC 13G/A, SCHEDULE 13D/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:29.348125+00:00.

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
| 2026-10-21 | 6-K | 0001213900-26-111191 | — | [S03] |
| 2026-10-07 | 6-K | 0001213900-26-107570 | — | [S04] |
| 2026-10-07 | 6-K | 0001213900-26-107372 | — | [S05] |
| 2026-10-06 | SCHEDULE 13D/A | 0001213900-26-107054 | — | [S06] |
| 2026-10-06 | 4 | 0001213900-26-107053 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-26T16:11:31.228419+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001981662.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001213900-26-111191](https://www.sec.gov/Archives/edgar/data/1981662/000121390026111191/0001213900-26-111191-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001213900-26-107570](https://www.sec.gov/Archives/edgar/data/1981662/000121390026107570/0001213900-26-107570-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001213900-26-107372](https://www.sec.gov/Archives/edgar/data/1981662/000121390026107372/0001213900-26-107372-index.html) — published 2026-10-07; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [SCHEDULE 13D/A 0001213900-26-107054](https://www.sec.gov/Archives/edgar/data/1981662/000121390026107054/0001213900-26-107054-index.html) — published 2026-10-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001213900-26-107053](https://www.sec.gov/Archives/edgar/data/1981662/000121390026107053/0001213900-26-107053-index.html) — published 2026-10-06; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261026-40356450615-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6ec0c5a139b27efe3be9111dc20cf938bd839c1e/brain/companies/NIVF/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
