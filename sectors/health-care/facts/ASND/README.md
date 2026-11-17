---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001612042
cik: '0001612042'
company_name: Ascendis Pharma A/S
tickers:
- ASND
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 00ea836101d6c3061ba4aa1d3cd9c1b6b5393f11
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
  - 3/A
  - '4'
  - 424B4
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-A12B/A
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
  - F-3ASR
  - F-3MEF
  - F-6
  - FWP
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001612042.json
    sha256: c495d82ca7dda70d4da8be5da2727a85c22343b051d8757749c9f185577bf90f
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001612042.json
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
  url: https://data.sec.gov/submissions/CIK0001612042.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: c495d82ca7dda70d4da8be5da2727a85c22343b051d8757749c9f185577bf90f
- id: S03
  title: 6-K 0001193125-26-423938
  url: https://www.sec.gov/Archives/edgar/data/1612042/000119312526423938/0001193125-26-423938-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001193125-26-421789
  url: https://www.sec.gov/Archives/edgar/data/1612042/000119312526421789/0001193125-26-421789-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001193125-26-407293
  url: https://www.sec.gov/Archives/edgar/data/1612042/000119312526407293/0001193125-26-407293-index.html
  published_at: '2026-09-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001610717-26-000423
  url: https://www.sec.gov/Archives/edgar/data/1612042/000161071726000423/0001610717-26-000423-index.html
  published_at: '2026-09-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001193125-26-390877
  url: https://www.sec.gov/Archives/edgar/data/1612042/000119312526390877/0001193125-26-390877-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S53
  url: https://www.sec.gov/Archives/edgar/data/1612042/000119312526423938/d167361d6k.htm
  title: 6-K 0001193125-26-423938
  published_at: '2026-10-16'
  retrieved_at: '2026-11-15T19:17:18.879042+00:00'
  sha256: c982db3171c679c1f8b37a5b379ab3ca3264ae33033ade19842cb9a1596ee7c5
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1612042/000119312526046590/asnd-20251231.htm
  title: 20-F 0001193125-26-046590
  published_at: '2026-02-11'
  retrieved_at: '2026-11-15T19:17:17.182990+00:00'
  sha256: 7b628cf0943078b8a7dacf8a8bf701692ee87d87a1a2fdc7824b50503a5bb2e2
issuer_classification:
  cik: '0001612042'
  classification_status: reported_sic
  entity_type: other
  name: Ascendis Pharma A/S
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: c495d82ca7dda70d4da8be5da2727a85c22343b051d8757749c9f185577bf90f
  url: https://data.sec.gov/submissions/CIK0001612042.json
listings:
- ticker: ASND
  exchange: NASDAQ
  instrument_type: equity_candidate
research_filings:
- accession: 0001193125-26-046590
  filed: '2026-02-11'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1612042/000119312526046590/0001193125-26-046590-index.html
- accession: 0001193125-26-423938
  filed: '2026-10-16'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1612042/000119312526423938/0001193125-26-423938-index.html
- accession: 0001193125-15-112091
  filed: '2015-03-30'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1612042/000119312515112091/0001193125-15-112091-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 1bb6c00df026c9134e60bcb14d2a1131a77bd0d30c09b1e9b59ffbfe35d6d43b
  last_attempt_at: '2026-11-15T19:14:21.222490+00:00'
  last_success_at: '2026-11-15T19:14:21.222490+00:00'
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
  - risks-and-thesis-breakers
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
  source_url: https://data.sec.gov/submissions/CIK0001612042.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/4221fdf1cbfcbe1be4425ff7f3389bba890abacf/brain/companies/ASND/README.md
full_history_commit: 4221fdf1cbfcbe1be4425ff7f3389bba890abacf
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ASND — Ascendis Pharma A/S

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/4221fdf1cbfcbe1be4425ff7f3389bba890abacf/brain/companies/ASND/README.md)

## Business overview

Reported issuer name: **Ascendis Pharma A/S**. Stable SEC CIK: **0001612042**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ASND | NASDAQ | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-02-11, L346:

> This annual report contains forward-looking statements concerning our business, operations and financial performance and condition, as well as our plans, objectives and expectations for our business operations and financial performance and condition. Any statements contained herein that are not statements of historical facts may be deemed to be forward-looking statements. In some cases, you can identify forward-looking statements by terminology such as “aim,” “anticipate,” “assume,” “believe,” “contemplate,” “continue,” “could,” “due,” “estimate,” “expect,” “goal,” “intend,” “may,” “objective,” “plan,” “predict,” “potential,” “positioned,” “seek,” “should,” “target,” “will,” “would,” and other similar expressions that are predictions or indicate future events and future trends, or the negative of these terms or other comparable terminology. These forward-looking statements include, but are not limited to, statements about: [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-02-11, L362:

> our expectations regarding the potential market opportunities and patient populations for our products and product candidates, if approved for commercial use; [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-02-11, L1025:

> Similarly, global climate change could result in certain types of natural disasters occurring more frequently or with more intense effects. Some of our corporate and operational functions are located in California, which has experienced severe earthquakes, droughts, fires and other natural disasters in the past. We do not have multiple-site capacity for all of our operations in the event of a business disruption. Furthermore, parties in our supply chain and our customers are similarly vulnerable to these global or regional economic, political, health, climate and other conditions and events. Global or regional economic, political, health, climate and other conditions and events could result in a variety of risks to our business, including our ability to raise capital when needed on acceptable terms, if at all. Any of the foregoing could harm our business and we cannot anticipate all of the ways in which such conditions and events could adversely impact our business. [S54]

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 6-K, filed 2026-10-16, L49:

> programs or on-market products; manufacturing, supply chain, quality, or logistics issues that could delay development or commercialization; unforeseen expenses related to commercialization of any approved Ascendis products; unforeseen research and [S53]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-02-11, L423:

> Competition in the biotechnology and pharmaceutical industries is intense and our competitors may discover, develop or commercialize products faster or more successfully than us. If we are unable to compete effectively, our business, results of operations and prospects will suffer. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 6-K, filed 2026-10-16, L52:

> challenges, including payer coverage decisions and health technology assessments; competitive developments, including new or improved therapies; intellectual property protection, freedom-to-operate, and litigation risks; Ascendis’ ability to [S53]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-02-11, L496:

> In cases where we are successful in obtaining regulatory approvals to market one or more of our product candidates (such as the approvals we have obtained for YORVIPATH and SKYTROFA), our revenue will be dependent, in part, upon the size of the markets in the territories for which regulatory approval is granted, the accepted price for the product, the availability of competing products, the ability to get reimbursement for our products at any price and the extent of our royalty rights for that territory. If the number of patients suitable for our products or product candidates is not as significant as we estimate, the indication approved by regulatory authorities is narrower than we expect or the reasonably accepted population for treatment is narrowed by competition, physician choice, treatment guidelines or third-party payor restrictions, we may not generate significant revenue from the sale of such products or product candidates, even if approved. Limitations on our ability to generate revenue from commercial product sales or pursuant to up-front or milestone payments and royalties from collaboration partners would likely depress our market value and could impair our ability to raise capital, expand our business, discover or develop other products and product candidates or continue our operations. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-02-11, L82:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-02-11, L404:

> These forward-looking statements are based on senior management’s current expectations, estimates, forecasts and projections about our business and the industry in which we operate and involve known and unknown risks, uncertainties and other factors that are in some cases beyond our control. As a result, any or all of our forward-looking statements in this annual report may turn out to be inaccurate. Factors that may cause actual results to differ materially from current expectations include, among other things, those listed under the section of this annual report titled “Item 3.D—Key Information—Risk Factors” and elsewhere in this annual report. You are urged to consider these factors carefully in evaluating the forward-looking statements. These forward-looking statements speak only as of the date of this annual report. Except as required by law, we assume no obligation to update or revise these forward-looking statements for any reason, even if new information becomes available in the future. Given these risks and uncertainties, you are cautioned not to rely on such forward-looking statements as predictions of future events. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 144/A, 20-F, 3, 3/A, 4, 424B4, 424B5, 6-K, 6-K/A, 8-A12B, 8-A12B/A, CERTNAS, CORRESP, CT ORDER, D, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-1MEF, F-3, F-3ASR, F-3MEF, F-6, FWP, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:34:32.676328+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
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
| 2026-10-16 | 6-K | 0001193125-26-423938 | — | [S03] |
| 2026-10-14 | 6-K | 0001193125-26-421789 | — | [S04] |
| 2026-09-29 | 6-K | 0001193125-26-407293 | — | [S05] |
| 2026-09-28 | 4 | 0001610717-26-000423 | — | [S06] |
| 2026-09-15 | 6-K | 0001193125-26-390877 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001612042.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001193125-26-423938](https://www.sec.gov/Archives/edgar/data/1612042/000119312526423938/0001193125-26-423938-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001193125-26-421789](https://www.sec.gov/Archives/edgar/data/1612042/000119312526421789/0001193125-26-421789-index.html) — published 2026-10-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001193125-26-407293](https://www.sec.gov/Archives/edgar/data/1612042/000119312526407293/0001193125-26-407293-index.html) — published 2026-09-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001610717-26-000423](https://www.sec.gov/Archives/edgar/data/1612042/000161071726000423/0001610717-26-000423-index.html) — published 2026-09-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001193125-26-390877](https://www.sec.gov/Archives/edgar/data/1612042/000119312526390877/0001193125-26-390877-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S53] [6-K 0001193125-26-423938](https://www.sec.gov/Archives/edgar/data/1612042/000119312526423938/d167361d6k.htm) — published 2026-10-16; retrieved 2026-11-15T19:17:18.879042+00:00.

[S54] [20-F 0001193125-26-046590](https://www.sec.gov/Archives/edgar/data/1612042/000119312526046590/asnd-20251231.htm) — published 2026-02-11; retrieved 2026-11-15T19:17:17.182990+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/4221fdf1cbfcbe1be4425ff7f3389bba890abacf/brain/companies/ASND/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
