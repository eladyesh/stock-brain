---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001871983
cik: 0001871983
company_name: Anghami Inc
tickers:
- ANGH
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: da985d7cdd310eab261be4fd3662836a26873702
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
  - 424B3
  - '425'
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - D
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-4
  - F-4/A
  - NT 20-F
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001871983.json
    sha256: a42e1936783e885f7bc3fb3a5fbb955b3b3a64bfd401d466fe3d2088d96216e8
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001871983.json
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
  url: https://data.sec.gov/submissions/CIK0001871983.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: a42e1936783e885f7bc3fb3a5fbb955b3b3a64bfd401d466fe3d2088d96216e8
- id: S03
  title: SCHEDULE 13D/A 0001193125-26-418066
  url: https://www.sec.gov/Archives/edgar/data/1871983/000119312526418066/0001193125-26-418066-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: SCHEDULE 13D/A 0001193125-26-390634
  url: https://www.sec.gov/Archives/edgar/data/1871983/000119312526390634/0001193125-26-390634-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: SCHEDULE 13D/A 0001104659-26-107266
  url: https://www.sec.gov/Archives/edgar/data/1871983/000110465926107266/0001104659-26-107266-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001213900-26-089443
  url: https://www.sec.gov/Archives/edgar/data/1871983/000121390026089443/0001213900-26-089443-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 3 0001213900-26-077928
  url: https://www.sec.gov/Archives/edgar/data/1871983/000121390026077928/0001213900-26-077928-index.html
  published_at: '2026-07-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1871983/000121390026070187/ea0295256-20fa1_anghami.htm
  title: 20-F/A 0001213900-26-070187
  published_at: '2026-06-18'
  retrieved_at: '2026-11-12T20:36:32.756328+00:00'
  sha256: 36c3edd95c2d17bf00b7c991cca3f5c96d128b52db59a209c6316dde3a21f6fd
- id: S55
  url: https://www.sec.gov/Archives/edgar/data/1871983/000121390026050335/ea0287764-20f_anghami.htm
  title: 20-F 0001213900-26-050335
  published_at: '2026-04-30'
  retrieved_at: '2026-11-12T20:36:31.288073+00:00'
  sha256: d1a0e8f80391011523fc8fd4ba228ba7d63345c41eb9238f7eb4bc5be8ca491e
issuer_classification:
  cik: 0001871983
  classification_status: reported_sic
  entity_type: other
  name: Anghami Inc
  sic: '4899'
  sic_description: Communications Services, NEC
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: a42e1936783e885f7bc3fb3a5fbb955b3b3a64bfd401d466fe3d2088d96216e8
  url: https://data.sec.gov/submissions/CIK0001871983.json
listings:
- ticker: ANGH
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001213900-26-050335
  filed: '2026-04-30'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1871983/000121390026050335/0001213900-26-050335-index.html
- accession: 0001213900-26-070187
  filed: '2026-06-18'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1871983/000121390026070187/0001213900-26-070187-index.html
- accession: 0001213900-26-089443
  filed: '2026-08-14'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1871983/000121390026089443/0001213900-26-089443-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 41c7cd1938ade75af62369d536be4cb9d147e0a494fa0ed64cfe1fa6c0affa98
  last_attempt_at: '2026-11-12T20:35:06.924881+00:00'
  last_success_at: '2026-11-12T20:35:06.924881+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - competitive-landscape
  - customers-and-end-markets
  - growth-drivers
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
  sector: communication-services
  method: project_sic_rule
  sic: '4899'
  sic_description: Communications Services, NEC
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001871983.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/ANGH/README.md
full_history_commit: 6e1c8271c74cf7335265700a5a223e692b47544f
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ANGH — Anghami Inc

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/ANGH/README.md)

## Business overview

Reported issuer name: **Anghami Inc**. Stable SEC CIK: **0001871983**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ANGH | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-30, L352:

> concentration of voting power among our founders who have and will continue to have substantial control over our business; [S55]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-30, L1464:

> could cause us to lose subscribers and subscription revenue or suffer an increase in our costs without a corresponding increase in the [S55]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-30, L461:

> users, retain existing users, and effectively monetize our products and services are not successful, our growth prospects and revenue [S55]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-30, L1156:

> online platforms, hardware, and networks to reach our customers. These platforms range from desktop and mobile operating systems and application [S55]

## Industry and value chain

SEC-reported SIC **4899**: Communications Services, NEC. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **communication-services**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-30, L542:

> to improving average revenue per user and overall profitability. However, competition from global and regional streaming platforms, many [S55]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-30, L423:

> claims of intellectual property infringement or missing content/publishing licenses could materially harm our business, results, and [S55]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-30, L717:

> market. However, if we do decide to expand our business (with both Arabic and international music) in the U.S., and we do not grow in [S55]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F/A, filed 2026-06-18, L75:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☒ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-30, L364:

> additional risk factors that could adversely impact our business and financial performance. Moreover, we operate in an evolving environment. [S55]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 20-F/A, 3, 3/A, 424B3, 425, 6-K, 8-A12B, CERT, CORRESP, D, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-4, F-4/A, NT 20-F, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:15.569320+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (source excerpts available; assess the claim): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (evidence or analysis still needed): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
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
| 2026-10-08 | SCHEDULE 13D/A | 0001193125-26-418066 | — | [S03] |
| 2026-09-14 | SCHEDULE 13D/A | 0001193125-26-390634 | — | [S04] |
| 2026-09-14 | SCHEDULE 13D/A | 0001104659-26-107266 | — | [S05] |
| 2026-08-14 | 6-K | 0001213900-26-089443 | — | [S06] |
| 2026-07-14 | 3 | 0001213900-26-077928 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001871983.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SCHEDULE 13D/A 0001193125-26-418066](https://www.sec.gov/Archives/edgar/data/1871983/000119312526418066/0001193125-26-418066-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [SCHEDULE 13D/A 0001193125-26-390634](https://www.sec.gov/Archives/edgar/data/1871983/000119312526390634/0001193125-26-390634-index.html) — published 2026-09-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [SCHEDULE 13D/A 0001104659-26-107266](https://www.sec.gov/Archives/edgar/data/1871983/000110465926107266/0001104659-26-107266-index.html) — published 2026-09-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001213900-26-089443](https://www.sec.gov/Archives/edgar/data/1871983/000121390026089443/0001213900-26-089443-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [3 0001213900-26-077928](https://www.sec.gov/Archives/edgar/data/1871983/000121390026077928/0001213900-26-077928-index.html) — published 2026-07-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F/A 0001213900-26-070187](https://www.sec.gov/Archives/edgar/data/1871983/000121390026070187/ea0295256-20fa1_anghami.htm) — published 2026-06-18; retrieved 2026-11-12T20:36:32.756328+00:00.

[S55] [20-F 0001213900-26-050335](https://www.sec.gov/Archives/edgar/data/1871983/000121390026050335/ea0287764-20f_anghami.htm) — published 2026-04-30; retrieved 2026-11-12T20:36:31.288073+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/ANGH/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
