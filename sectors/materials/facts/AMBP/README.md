---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001845097
cik: 0001845097
company_name: Ardagh Metal Packaging S.A.
tickers:
- AMBP
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 6dea3be4625120db9da80155a96f14ed62690190
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 25-NSE
  - '3'
  - '4'
  - 424B3
  - '425'
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - DRS
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-4
  - F-4/A
  - POS AM
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001845097.json
    sha256: ae464d7f8e0b08a5767578a2cf0a53a2db357b2b7a695347842cd2394ac6ec0d
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001845097.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-11-01T16:07:03.340031+00:00'
  sha256: ee0a872edece98430f3ba5a1ed6e9c683d7a1bb4b2980bdc9743c6995f264398
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001845097.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ae464d7f8e0b08a5767578a2cf0a53a2db357b2b7a695347842cd2394ac6ec0d
- id: S03
  title: 6-K 0001104659-26-118034
  url: https://www.sec.gov/Archives/edgar/data/1845097/000110465926118034/0001104659-26-118034-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001104659-26-118033
  url: https://www.sec.gov/Archives/edgar/data/1845097/000110465926118033/0001104659-26-118033-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001104659-26-118031
  url: https://www.sec.gov/Archives/edgar/data/1845097/000110465926118031/0001104659-26-118031-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001104659-26-116016
  url: https://www.sec.gov/Archives/edgar/data/1845097/000110465926116016/0001104659-26-116016-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001104659-26-108085
  url: https://www.sec.gov/Archives/edgar/data/1845097/000110465926108085/0001104659-26-108085-index.html
  published_at: '2026-09-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1845097/000110465926024068/ambp-20251231x20f.htm
  title: 20-F 0001104659-26-024068
  published_at: '2026-03-05'
  retrieved_at: '2026-11-10T20:16:58.297898+00:00'
  sha256: 4dcb67027bff48f9eded776f98d2358fabd48e46cb5600b55aca901b0ab8f010
issuer_classification:
  cik: 0001845097
  classification_status: reported_sic
  entity_type: other
  name: Ardagh Metal Packaging S.A.
  sic: '3411'
  sic_description: Metal Cans
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ae464d7f8e0b08a5767578a2cf0a53a2db357b2b7a695347842cd2394ac6ec0d
  url: https://data.sec.gov/submissions/CIK0001845097.json
listings:
- ticker: AMBP
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-024068
  filed: '2026-03-05'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1845097/000110465926024068/0001104659-26-024068-index.html
- accession: 0001104659-26-118034
  filed: '2026-10-22'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1845097/000110465926118034/0001104659-26-118034-index.html
research_progress:
  stage: evidence_collected
  input_sha256: b1faacb9ba90093b12af37b98f8f4bbf4b3505b18205b065f326d69f4b1d693b
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
  sector: materials
  method: project_sic_rule
  sic: '3411'
  sic_description: Metal Cans
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001845097.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/876d144f6387664050d096ed943ae2c26137a2cb/brain/companies/AMBP/README.md
full_history_commit: 876d144f6387664050d096ed943ae2c26137a2cb
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AMBP — Ardagh Metal Packaging S.A.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/876d144f6387664050d096ed943ae2c26137a2cb/brain/companies/AMBP/README.md)

## Business overview

Reported issuer name: **Ardagh Metal Packaging S.A.**. Stable SEC CIK: **0001845097**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AMBP | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-03-05, L460:

> \| \| ● \| changes in the economic, political, credit, and/or financial environment in which we operate, which could have a material adverse effect on our business, such as reducing demand for our products; [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-03-05, L922:

> Total revenue of our two operating and reportable segments, Europe and Americas, for the year ended December 31, 2025 was $2,307 million and $3,190 million, respectively. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-03-05, L460:

> \| \| ● \| changes in the economic, political, credit, and/or financial environment in which we operate, which could have a material adverse effect on our business, such as reducing demand for our products; [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-03-05, L452:

> \| \| ● \| concentration of our customers or changes in our customers’ strategic choices, such as whether to prioritize price or volume requirements; [S54]

## Industry and value chain

SEC-reported SIC **3411**: Metal Cans. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-03-05, L457:

> \| \| ● \| availability and any increase in the costs of raw materials, including as a result of changes in tariffs and duties and our inability to fully pass through input costs; [S54]

Navigation sector: **materials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-03-05, L513:

> \| \| ● \| risks relating to competition from other metal packaging producers and alternative forms of packaging; [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-03-05, L675:

> Ineffective AI governance or insufficient usage controls may result in the unauthorized deployment of AI technologies, unintended exposure of sensitive data, generation of inaccurate or misleading outputs, breaches of regulatory or contractual compliance, failures to meet privacy obligations, and reputational harm. As AI capabilities evolve, the complexity and potential impact of these risks may increase, particularly in relation to data protection, intellectual property, and ethical standards. Failure to implement robust AI governance frameworks, usage policies, and monitoring mechanisms could expose us to regulatory investigations, legal claims, operational disruptions, and loss of stakeholder trust, any of which could materially adversely affect our business, results of operations, financial condition, cash flows or prospects. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-03-05, L951:

> \| \| ● \| Emphasize operational excellence and optimize manufacturing base. In managing our businesses, we seek to improve our efficiency, control our costs and preserve and expand our margins. We aim to consistently reduce total costs through implementing operational efficiencies and promoting continuous improvement. We will continue to take actions to enhance efficiency through continuous improvement, best practice sharing and investment, enabling us to serve our existing and new customers’ exacting requirements for sustainable packaging. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-03-05, L81:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to § 240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-03-05, L460:

> \| \| ● \| changes in the economic, political, credit, and/or financial environment in which we operate, which could have a material adverse effect on our business, such as reducing demand for our products; [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 25-NSE, 3, 4, 424B3, 425, 6-K, 8-A12B, CERT, CORRESP, DRS, EFFECT, F-1, F-1/A, F-3, F-4, F-4/A, POS AM, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:05.986131+00:00.

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
| 2026-10-22 | 6-K | 0001104659-26-118034 | — | [S03] |
| 2026-10-22 | 6-K | 0001104659-26-118033 | — | [S04] |
| 2026-10-22 | 6-K | 0001104659-26-118031 | — | [S05] |
| 2026-10-15 | 6-K | 0001104659-26-116016 | — | [S06] |
| 2026-09-16 | 6-K | 0001104659-26-108085 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001845097.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001104659-26-118034](https://www.sec.gov/Archives/edgar/data/1845097/000110465926118034/0001104659-26-118034-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001104659-26-118033](https://www.sec.gov/Archives/edgar/data/1845097/000110465926118033/0001104659-26-118033-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001104659-26-118031](https://www.sec.gov/Archives/edgar/data/1845097/000110465926118031/0001104659-26-118031-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001104659-26-116016](https://www.sec.gov/Archives/edgar/data/1845097/000110465926116016/0001104659-26-116016-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001104659-26-108085](https://www.sec.gov/Archives/edgar/data/1845097/000110465926108085/0001104659-26-108085-index.html) — published 2026-09-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001104659-26-024068](https://www.sec.gov/Archives/edgar/data/1845097/000110465926024068/ambp-20251231x20f.htm) — published 2026-03-05; retrieved 2026-11-10T20:16:58.297898+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/876d144f6387664050d096ed943ae2c26137a2cb/brain/companies/AMBP/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
