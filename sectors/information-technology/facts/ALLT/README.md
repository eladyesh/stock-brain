---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001365767
cik: '0001365767'
company_name: Allot Ltd.
tickers:
- ALLT
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
  - '144'
  - 20-F
  - 20-F/A
  - '3'
  - '4'
  - 424B1
  - 424B3
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERTNAS
  - CORRESP
  - CT ORDER
  - EFFECT
  - F-1
  - F-3
  - F-3/A
  - FWP
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001365767.json
    sha256: 0b215c2e41b1d8477becf79f4596acdf6ac8341378a2f80bcfc0fa40d94141cd
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001365767.json
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
  url: https://data.sec.gov/submissions/CIK0001365767.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 0b215c2e41b1d8477becf79f4596acdf6ac8341378a2f80bcfc0fa40d94141cd
- id: S03
  title: 6-K 0001178913-26-004814
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891326004814/0001178913-26-004814-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001178913-26-004505
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891326004505/0001178913-26-004505-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001178913-26-004492
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891326004492/0001178913-26-004492-index.html
  published_at: '2026-09-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001178913-26-004464
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891326004464/0001178913-26-004464-index.html
  published_at: '2026-09-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001976408-26-000790
  url: https://www.sec.gov/Archives/edgar/data/1365767/000197640826000790/0001976408-26-000790-index.html
  published_at: '2026-08-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891326001946/zk2635004.htm
  title: 20-F/A 0001178913-26-001946
  published_at: '2026-03-31'
  retrieved_at: '2026-11-09T22:57:16.271174+00:00'
  sha256: 3a8df767fb070b19491938690d2c5b832ff868f49fc5e36b69ca5539e96be09f
- id: S55
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891326001755/zk2634876.htm
  title: 20-F 0001178913-26-001755
  published_at: '2026-03-26'
  retrieved_at: '2026-11-09T22:57:14.239383+00:00'
  sha256: 95e83d5a539111dc54651bc4fb81b46c1876dd6363f04deb298933aff65108ec
issuer_classification:
  cik: '0001365767'
  classification_status: reported_sic
  entity_type: other
  name: Allot Ltd.
  sic: '3576'
  sic_description: Computer Communications Equipment
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 0b215c2e41b1d8477becf79f4596acdf6ac8341378a2f80bcfc0fa40d94141cd
  url: https://data.sec.gov/submissions/CIK0001365767.json
listings:
- ticker: ALLT
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001178913-26-001755
  filed: '2026-03-26'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891326001755/0001178913-26-001755-index.html
- accession: 0001178913-26-001946
  filed: '2026-03-31'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891326001946/0001178913-26-001946-index.html
- accession: 0001178913-20-001927
  filed: '2020-07-01'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891320001927/0001178913-20-001927-index.html
- accession: 0001178913-09-003095
  filed: '2009-12-18'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891309003095/0001178913-09-003095-index.html
- accession: 0001178913-26-004814
  filed: '2026-10-22'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891326004814/0001178913-26-004814-index.html
- accession: 0001178913-12-001551
  filed: '2012-05-21'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1365767/000117891312001551/0001178913-12-001551-index.html
research_progress:
  stage: evidence_collected
  input_sha256: b3bbb1daf558bc938fe06e48dc32a834dd9955d7bbdb98650a8e6cb57d727297
  last_attempt_at: '2026-11-09T22:51:05.851006+00:00'
  last_success_at: '2026-11-09T22:51:05.851006+00:00'
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
  sic: '3576'
  sic_description: Computer Communications Equipment
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001365767.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/ALLT/README.md
full_history_commit: 6e1c8271c74cf7335265700a5a223e692b47544f
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ALLT — Allot Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/ALLT/README.md)

## Business overview

Reported issuer name: **Allot Ltd.**. Stable SEC CIK: **0001365767**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ALLT | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-03-26, L430:

> occur, our business, financial condition and results of operations would suffer. In this case, the trading price of our ordinary shares [S55]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F/A, filed 2026-03-31, L8016:

> Allot operates in a single reportable segment. Revenues are based on the location of the Company's channel partners which are considered as end customers, as well as direct customers of the Company: [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-03-26, L476:

> sales disruptions or costs arising from a loss of rights to use the third-party solutions we integrate with our products; [S55]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-03-26, L472:

> the ability of our suppliers to provide, or refusal of our customers to implement, the single or limited sources from which certain [S55]

## Industry and value chain

SEC-reported SIC **3576**: Computer Communications Equipment. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-03-26, L472:

> the ability of our suppliers to provide, or refusal of our customers to implement, the single or limited sources from which certain [S55]

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-03-26, L348:

> and the effects of competition. Forward-looking statements include all statements that are not historical facts and can be identified [S55]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-03-26, L492:

> risks related to our proprietary rights and information, including our ability to protect the intellectual property embodied in our [S55]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-03-26, L371:

> statements regarding our ability to develop technologies to meet our customer demands and expand our product and service offerings, [S55]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F/A, filed 2026-03-31, L98:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive- based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-03-26, L406:

> these forward-looking statements due to various factors, including all the risks discussed in “ITEM 3: Key Information-Risk Factors” [S55]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 4, 424B1, 424B3, 424B5, 6-K, 6-K/A, 8-A12B, CERTNAS, CORRESP, CT ORDER, EFFECT, F-1, F-3, F-3/A, FWP, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:32:50.796193+00:00.

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
| 2026-10-22 | 6-K | 0001178913-26-004814 | — | [S03] |
| 2026-09-15 | 6-K | 0001178913-26-004505 | — | [S04] |
| 2026-09-10 | 6-K | 0001178913-26-004492 | — | [S05] |
| 2026-09-09 | 6-K | 0001178913-26-004464 | — | [S06] |
| 2026-08-31 | 4 | 0001976408-26-000790 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001365767.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001178913-26-004814](https://www.sec.gov/Archives/edgar/data/1365767/000117891326004814/0001178913-26-004814-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001178913-26-004505](https://www.sec.gov/Archives/edgar/data/1365767/000117891326004505/0001178913-26-004505-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001178913-26-004492](https://www.sec.gov/Archives/edgar/data/1365767/000117891326004492/0001178913-26-004492-index.html) — published 2026-09-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001178913-26-004464](https://www.sec.gov/Archives/edgar/data/1365767/000117891326004464/0001178913-26-004464-index.html) — published 2026-09-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001976408-26-000790](https://www.sec.gov/Archives/edgar/data/1365767/000197640826000790/0001976408-26-000790-index.html) — published 2026-08-31; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F/A 0001178913-26-001946](https://www.sec.gov/Archives/edgar/data/1365767/000117891326001946/zk2635004.htm) — published 2026-03-31; retrieved 2026-11-09T22:57:16.271174+00:00.

[S55] [20-F 0001178913-26-001755](https://www.sec.gov/Archives/edgar/data/1365767/000117891326001755/zk2634876.htm) — published 2026-03-26; retrieved 2026-11-09T22:57:14.239383+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/6e1c8271c74cf7335265700a5a223e692b47544f/brain/companies/ALLT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
