---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001993097
cik: 0001993097
company_name: 3 E Network Technology Group Ltd
tickers:
- MASK
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
  - '3'
  - 424B4
  - 6-K
  - 8-A12B
  - AW
  - CERT
  - CORRESP
  - D
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-1MEF
  - NT 20-F
  - POS AM
  - S-8
  - SCHEDULE 13D
  - SCHEDULE 13G
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001993097.json
    sha256: 3b2ec2fb74cfd886e759d689bcea783842e56eae646a5b4561619a01afb0f4be
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001993097.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
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
  url: https://data.sec.gov/submissions/CIK0001993097.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 3b2ec2fb74cfd886e759d689bcea783842e56eae646a5b4561619a01afb0f4be
- id: S03
  title: 6-K 0001185185-26-004971
  url: https://www.sec.gov/Archives/edgar/data/1993097/000118518526004971/0001185185-26-004971-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001185185-26-004968
  url: https://www.sec.gov/Archives/edgar/data/1993097/000118518526004968/0001185185-26-004968-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: D 0001993097-26-000001
  url: https://www.sec.gov/Archives/edgar/data/1993097/000199309726000001/0001993097-26-000001-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: SCHEDULE 13D 0001185185-26-004439
  url: https://www.sec.gov/Archives/edgar/data/1993097/000118518526004439/0001185185-26-004439-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001185185-26-004334
  url: https://www.sec.gov/Archives/edgar/data/1993097/000118518526004334/0001185185-26-004334-index.html
  published_at: '2026-09-25'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1993097/000118518525001717/mask20f110325.htm
  title: 20-F 0001185185-25-001717
  published_at: '2025-11-14'
  retrieved_at: '2026-10-29T16:27:43.606022+00:00'
  sha256: 6ba776ef6587bcc95e585f9742b84ca7ddf53cf2865e51fa3e0751b39d20b37f
issuer_classification:
  cik: 0001993097
  classification_status: reported_sic
  entity_type: other
  name: 3 E Network Technology Group Ltd
  sic: '7371'
  sic_description: Services-Computer Programming Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 3b2ec2fb74cfd886e759d689bcea783842e56eae646a5b4561619a01afb0f4be
  url: https://data.sec.gov/submissions/CIK0001993097.json
listings:
- ticker: MASK
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001185185-25-001717
  filed: '2025-11-14'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1993097/000118518525001717/0001185185-25-001717-index.html
- accession: 0001185185-26-004971
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1993097/000118518526004971/0001185185-26-004971-index.html
research_progress:
  stage: evidence_collected
  input_sha256: e333cdb762804ab618c713ed177dda701eaa96ae4bb8c8caf8cae2f765fde717
  last_attempt_at: '2026-10-29T16:24:48.518388+00:00'
  last_success_at: '2026-10-29T16:24:48.518388+00:00'
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
  sector: information-technology
  method: project_sic_rule
  sic: '7371'
  sic_description: Services-Computer Programming Services
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001993097.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/MASK/README.md
full_history_commit: c26f59bc72c00102d2490e95b07449f8cd848491
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# MASK — 3 E Network Technology Group Ltd

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/MASK/README.md)

## Business overview

Reported issuer name: **3 E Network Technology Group Ltd**. Stable SEC CIK: **0001993097**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| MASK | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2025-11-14, L551:

> information in such sources may not be consistent with other information compiled in or outside China. The industry in which we operate [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2025-11-14, L5269:

> real estate, exhibition & conferencing, and clean energy utilities. Our revenue streams include software development services, [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2025-11-14, L1085:

> Business and Industry—We may be forced to reduce the prices of our services due to increased competition and reduced bargaining [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2025-11-14, L796:

> information system and confidentiality of our customers’ personal information, including, but not limited to the followings: [S54]

## Industry and value chain

SEC-reported SIC **7371**: Services-Computer Programming Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2025-11-14, L1688:

> conflicts, may result in economic instability, market volatility, and regulatory changes, which could impact our supply chain, operations, [S54]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2025-11-14, L575:

> success of operating initiatives, including advertising and promotional efforts and new solution development by us and our competitors; [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2025-11-14, L1361:

> in wages for professionals in China could prevent us from sustaining our competitive advantage and could reduce our profit margins. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2025-11-14, L942:

> which could materially and adversely affect our liquidity and our ability to fund and expand our business.”; “— We [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2025-11-14, L124:

> received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2025-11-14, L552:

> is subject to a high degree of uncertainty and risk due to variety of factors, including those described in the “Risk Factors” [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 424B4, 6-K, 8-A12B, AW, CERT, CORRESP, D, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-1MEF, NT 20-F, POS AM, S-8, SCHEDULE 13D, SCHEDULE 13G, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:30.413648+00:00.

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
| 2026-10-23 | 6-K | 0001185185-26-004971 | — | [S03] |
| 2026-10-23 | 6-K | 0001185185-26-004968 | — | [S04] |
| 2026-10-08 | D | 0001993097-26-000001 | — | [S05] |
| 2026-09-30 | SCHEDULE 13D | 0001185185-26-004439 | — | [S06] |
| 2026-09-25 | 6-K | 0001185185-26-004334 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-29T16:14:13.115716+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001993097.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001185185-26-004971](https://www.sec.gov/Archives/edgar/data/1993097/000118518526004971/0001185185-26-004971-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001185185-26-004968](https://www.sec.gov/Archives/edgar/data/1993097/000118518526004968/0001185185-26-004968-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [D 0001993097-26-000001](https://www.sec.gov/Archives/edgar/data/1993097/000199309726000001/0001993097-26-000001-index.html) — published 2026-10-08; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [SCHEDULE 13D 0001185185-26-004439](https://www.sec.gov/Archives/edgar/data/1993097/000118518526004439/0001185185-26-004439-index.html) — published 2026-09-30; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001185185-26-004334](https://www.sec.gov/Archives/edgar/data/1993097/000118518526004334/0001185185-26-004334-index.html) — published 2026-09-25; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001185185-25-001717](https://www.sec.gov/Archives/edgar/data/1993097/000118518525001717/mask20f110325.htm) — published 2025-11-14; retrieved 2026-10-29T16:27:43.606022+00:00.

Source release: `coverage-20261029-40909364006-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/c26f59bc72c00102d2490e95b07449f8cd848491/brain/companies/MASK/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
