---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001095435
cik: 0001095435
company_name: Alpha Compute Corp
tickers:
- ALP
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: ce343a6d2661d5e53e8ca52f8b7b829df31d97c0
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
  - '3'
  - '4'
  - 4/A
  - 424B2
  - 424B3
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - AW
  - CERT
  - CORRESP
  - D
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - F-3DPOS
  - NT 20-F
  - POS AM
  - RW
  - S-8
  - S-8 POS
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SUPPL
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001095435.json
    sha256: edfa19e5dd9c99519719bef7c32082c02160d20b1d7a288864f0e0081d1e7dca
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001095435.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-11-01T16:07:03.070084+00:00'
  sha256: b160a2f2814e5df68d7e414fba70f808f7ad3d20cbbdd167a8a2e38a10044168
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001095435.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: edfa19e5dd9c99519719bef7c32082c02160d20b1d7a288864f0e0081d1e7dca
- id: S03
  title: 4 0001171843-26-006594
  url: https://www.sec.gov/Archives/edgar/data/1095435/000117184326006594/0001171843-26-006594-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001171843-26-006446
  url: https://www.sec.gov/Archives/edgar/data/1095435/000117184326006446/0001171843-26-006446-index.html
  published_at: '2026-10-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001171843-26-006419
  url: https://www.sec.gov/Archives/edgar/data/1095435/000117184326006419/0001171843-26-006419-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 3 0001171843-26-006418
  url: https://www.sec.gov/Archives/edgar/data/1095435/000117184326006418/0001171843-26-006418-index.html
  published_at: '2026-10-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001171843-26-006237
  url: https://www.sec.gov/Archives/edgar/data/1095435/000117184326006237/0001171843-26-006237-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1095435/000117184326005284/f20fa_072626.htm
  title: 20-F/A 0001171843-26-005284
  published_at: '2026-08-06'
  retrieved_at: '2026-11-10T20:13:21.607056+00:00'
  sha256: aa74ccf2a59a584a567fc0202e185fb55352cde9195ce7ad0e06835718c8809f
issuer_classification:
  cik: 0001095435
  classification_status: reported_sic
  entity_type: other
  name: Alpha Compute Corp
  sic: '6199'
  sic_description: Finance Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: edfa19e5dd9c99519719bef7c32082c02160d20b1d7a288864f0e0081d1e7dca
  url: https://data.sec.gov/submissions/CIK0001095435.json
listings:
- ticker: ALP
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001171843-26-004704
  filed: '2026-07-16'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1095435/000117184326004704/0001171843-26-004704-index.html
- accession: 0001171843-26-005284
  filed: '2026-08-06'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1095435/000117184326005284/0001171843-26-005284-index.html
- accession: 0001171843-26-004784
  filed: '2026-07-21'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1095435/000117184326004784/0001171843-26-004784-index.html
- accession: 0001171843-22-001628
  filed: '2022-03-04'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1095435/000117184322001628/0001171843-22-001628-index.html
- accession: 0001062993-21-003012
  filed: '2021-03-26'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1095435/000106299321003012/0001062993-21-003012-index.html
- accession: 0001393905-17-000342
  filed: '2017-11-09'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1095435/000139390517000342/0001393905-17-000342-index.html
- accession: 0001095435-13-000002
  filed: '2013-01-11'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1095435/000109543513000002/0001095435-13-000002-index.html
- accession: 0001095435-11-000055
  filed: '2011-08-23'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1095435/000109543511000055/0001095435-11-000055-index.html
- accession: 0001095435-07-000011
  filed: '2007-02-05'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1095435/000109543507000011/0001095435-07-000011-index.html
- accession: 0001095435-05-000065
  filed: '2005-11-29'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1095435/000109543505000065/0001095435-05-000065-index.html
- accession: 0001095435-05-000064
  filed: '2005-11-29'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1095435/000109543505000064/0001095435-05-000064-index.html
- accession: 0001095435-05-000046
  filed: '2005-09-29'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1095435/000109543505000046/0001095435-05-000046-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 6d28c87c541a4436b4b62b6fb3b43753710249914c1fdc2e08d4e7b78f4166a6
  last_attempt_at: '2026-11-10T20:10:56.246440+00:00'
  last_success_at: '2026-11-10T20:10:56.246440+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - competitive-landscape
  - customers-and-end-markets
  - growth-drivers
  - industry-and-value-chain
  - management-and-governance
  - moat-and-differentiation
  - products-and-services
  - recent-developments
  - revenue-model-and-segments
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: financials
  method: project_sic_rule
  sic: '6199'
  sic_description: Finance Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001095435.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/da8cd95563ea061c99219f658cc12f18850f2a59/brain/companies/ALP/README.md
full_history_commit: da8cd95563ea061c99219f658cc12f18850f2a59
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ALP — Alpha Compute Corp

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/da8cd95563ea061c99219f658cc12f18850f2a59/brain/companies/ALP/README.md)

## Business overview

Reported issuer name: **Alpha Compute Corp**. Stable SEC CIK: **0001095435**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ALP | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F/A, filed 2026-08-06, L256:

> regarding our business strategy, plans and objectives of management for future operations. Forward-looking statements are generally identified [S53]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F/A, filed 2026-08-06, L13577:

> of investment in Compedica was reclassified from the Digital & Compute reportable segment to the Immuno-Oncology reportable segment. [S53]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F/A, filed 2026-08-06, L992:

> for AI compute does not grow at the rate we anticipate, or if customers reduce their consumption of our services, our revenue, utilization [S53]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F/A, filed 2026-08-06, L1114:

> be our customers, suppliers, or partners, creating complex commercial relationships and potential conflicts of interest. Hyperscalers [S53]

## Industry and value chain

SEC-reported SIC **6199**: Finance Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F/A, filed 2026-08-06, L1081:

> a limited number of suppliers. The global semiconductor supply chain is subject to capacity constraints, extended lead times, geopolitical [S53]

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F/A, filed 2026-08-06, L963:

> in compute infrastructure, AI/ML systems, and digital assets. Competition for such personnel is intense, and we compete with larger, more [S53]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F/A, filed 2026-08-06, L2782:

> for Cancer Research Ltd. (“LICR”), which covers certain technology, intellectual property and know-how and development with [S53]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F/A, filed 2026-08-06, L1262:

> capital to fund our operations, investments and growth strategy, and we may seek to raise additional capital through the issuance of equity [S53]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F/A, filed 2026-08-06, L86:

> a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery [S53]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F/A, filed 2026-08-06, L315:

> \| the other risks and uncertainties described under “Item 3. Key Information—Risk Factors” and elsewhere in this Annual [S53]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 4, 4/A, 424B2, 424B3, 424B5, 6-K, 6-K/A, 8-A12B, AW, CERT, CORRESP, D, EFFECT, F-1, F-1/A, F-3, F-3/A, F-3DPOS, NT 20-F, POS AM, RW, S-8, S-8 POS, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, SUPPL, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:31:36.668201+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (source excerpts available; assess the claim): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (source excerpts available; assess the claim): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (source excerpts available; assess the claim): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (source excerpts available; assess the claim): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
- **Growth drivers** (source excerpts available; assess the claim): Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.
- **Financial performance** (evidence or analysis still needed): Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.
- **Balance sheet and capital allocation** (evidence or analysis still needed): Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.
- **Management and governance** (source excerpts available; assess the claim): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
- **Valuation context** (evidence or analysis still needed): Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.
- **Catalysts** (evidence or analysis still needed): List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.
- **Risks and thesis breakers** (source excerpts available; assess the claim): Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.
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
| 2026-10-13 | 4 | 0001171843-26-006594 | — | [S03] |
| 2026-10-06 | 6-K | 0001171843-26-006446 | — | [S04] |
| 2026-10-05 | 4 | 0001171843-26-006419 | — | [S05] |
| 2026-10-05 | 3 | 0001171843-26-006418 | — | [S06] |
| 2026-09-25 | 6-K | 0001171843-26-006237 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001095435.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0001171843-26-006594](https://www.sec.gov/Archives/edgar/data/1095435/000117184326006594/0001171843-26-006594-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001171843-26-006446](https://www.sec.gov/Archives/edgar/data/1095435/000117184326006446/0001171843-26-006446-index.html) — published 2026-10-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001171843-26-006419](https://www.sec.gov/Archives/edgar/data/1095435/000117184326006419/0001171843-26-006419-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [3 0001171843-26-006418](https://www.sec.gov/Archives/edgar/data/1095435/000117184326006418/0001171843-26-006418-index.html) — published 2026-10-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001171843-26-006237](https://www.sec.gov/Archives/edgar/data/1095435/000117184326006237/0001171843-26-006237-index.html) — published 2026-09-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S53] [20-F/A 0001171843-26-005284](https://www.sec.gov/Archives/edgar/data/1095435/000117184326005284/f20fa_072626.htm) — published 2026-08-06; retrieved 2026-11-10T20:13:21.607056+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/da8cd95563ea061c99219f658cc12f18850f2a59/brain/companies/ALP/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
