---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001859690
cik: 0001859690
company_name: Arqit Quantum Inc.
tickers:
- ARQQ
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 19d922c3a340e07ae75733aff6f0ed5f91038456
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
  - 25-NSE
  - '3'
  - '4'
  - 424B3
  - 424B5
  - '425'
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - F-4
  - F-4/A
  - POS AM
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001859690.json
    sha256: f76417990cf577afafdee5e0dcb94eaf537b6a8dba9e57b165f1f4af13cee2df
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001859690.json
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
  url: https://data.sec.gov/submissions/CIK0001859690.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: f76417990cf577afafdee5e0dcb94eaf537b6a8dba9e57b165f1f4af13cee2df
- id: S03
  title: 4 0001859690-26-000196
  url: https://www.sec.gov/Archives/edgar/data/1859690/000185969026000196/0001859690-26-000196-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 4 0001859690-26-000195
  url: https://www.sec.gov/Archives/edgar/data/1859690/000185969026000195/0001859690-26-000195-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001859690-26-000194
  url: https://www.sec.gov/Archives/edgar/data/1859690/000185969026000194/0001859690-26-000194-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001859690-26-000193
  url: https://www.sec.gov/Archives/edgar/data/1859690/000185969026000193/0001859690-26-000193-index.html
  published_at: '2026-10-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 144 0001959173-26-007353
  url: https://www.sec.gov/Archives/edgar/data/1859690/000195917326007353/0001959173-26-007353-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1859690/000110465925119500/arqq-20250930x20f.htm
  title: 20-F 0001104659-25-119500
  published_at: '2025-12-09'
  retrieved_at: '2026-11-14T18:44:20.150871+00:00'
  sha256: 0b0c4f12d291a88f656d26a5ef7fbe8a083b5ab37b4a45dbff6763c33ed4c3b4
issuer_classification:
  cik: 0001859690
  classification_status: reported_sic
  entity_type: other
  name: Arqit Quantum Inc.
  sic: '7372'
  sic_description: Services-Prepackaged Software
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: f76417990cf577afafdee5e0dcb94eaf537b6a8dba9e57b165f1f4af13cee2df
  url: https://data.sec.gov/submissions/CIK0001859690.json
listings:
- ticker: ARQQ
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001104659-25-119500
  filed: '2025-12-09'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1859690/000110465925119500/0001104659-25-119500-index.html
- accession: 0001104659-26-114690
  filed: '2026-10-08'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1859690/000110465926114690/0001104659-26-114690-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 7a2f637db8d94bfd7d06e8dbc9aa37bf4aa50b02807db1ac2e42c979984b70f1
  last_attempt_at: '2026-11-14T18:39:40.176158+00:00'
  last_success_at: '2026-11-14T18:39:40.176158+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - competitive-landscape
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
  sector: information-technology
  method: project_sic_rule
  sic: '7372'
  sic_description: Services-Prepackaged Software
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001859690.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/2f077c0023bcb685dbbb970d68a962dd99ff31fe/brain/companies/ARQQ/README.md
full_history_commit: 2f077c0023bcb685dbbb970d68a962dd99ff31fe
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ARQQ — Arqit Quantum Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/2f077c0023bcb685dbbb970d68a962dd99ff31fe/brain/companies/ARQQ/README.md)

## Business overview

Reported issuer name: **Arqit Quantum Inc.**. Stable SEC CIK: **0001859690**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ARQQ | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2025-12-09, L732:

> You should carefully consider the risks described below, together with all of the other information included in this Annual Report, in evaluating us and our shares. Our business, financial condition or results of operations could be materially and adversely affected by any of these risks. The trading price and value of our ordinary shares could decline due to any of these risks, and you may lose all or part of your investment. This Annual Report also contains forward-looking statements that involve risks and uncertainties. Our actual results could differ materially from those anticipated in these forward-looking statements as a result of certain factors, including the risks faced by us described below and elsewhere in this Annual Report. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2025-12-09, L7220:

> \| \| ● \| IFRIC Agenda Decision - Disclosure of Revenues and Expenses for Reportable Segments (IFRS 8) [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2025-12-09, L776:

> While Arqit has invested substantial resources in technological development, and believes that its product is a unique innovation, continuing technological changes in quantum technology and changes in the markets for its products could adversely affect adoption of its products, either generally or for particular applications. Arqit’s future success will depend upon its ability to develop and introduce a variety of new capabilities and innovations to its product offerings, as well as to introduce a variety of new product offerings, to address the changing needs of the markets in which Arqit offers its products. Delays in delivering new products that meet customer requirements could damage its relationships with customers and lead them to seek alternative sources of supply. Delays in introducing products and innovations, the failure to choose correctly among technical alternatives or the failure to offer innovative products or configurations at competitive prices may cause existing and potential customers to purchase its competitors’ products or turn to alternative technology. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **7372**: Services-Prepackaged Software. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **information-technology**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2025-12-09, L759:

> Participants in Arqit’s industry typically protect their technology, especially embedded software, through copyrights and trade secrets in addition to patents. As a result, there is frequent litigation based on allegations of infringement, misappropriation or other violations of intellectual property rights. Arqit may in the future receive inquiries from other intellectual property holders and may become subject to claims that it infringes their intellectual property rights, particularly as Arqit expands its presence in the market, expands to new use cases and faces increasing competition. In addition, parties may claim that the names and branding of Arqit’s products infringe their trademark rights in certain countries or territories. If such a claim were to prevail, Arqit may have to change the names and branding of its products in the affected territories and could incur other costs. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2025-12-09, L701:

> \| \| ● \| The Company may not be able to adequately protect or enforce its intellectual property rights or prevent unauthorized parties from copying or reverse engineering its products or technology. Its efforts to protect and enforce its intellectual property rights and prevent third parties from violating its rights may be costly. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2025-12-09, L886:

> If Arqit fails to develop and maintain effective internal controls and procedures and disclosure procedures and controls, it may be unable to provide financial information and required SEC reports that a U.S. publicly traded company is required to provide in a timely and reliable fashion. Any such delays or deficiencies could penalize Arqit, including by limiting its ability to obtain financing, either in the public capital markets or from private sources and hurt its reputation and could thereby impede its ability to implement its growth strategy. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2025-12-09, L120:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2025-12-09, L630:

> Industry publications, research, studies and forecasts generally state that the information they contain has been obtained from sources believed to be reliable, but that the accuracy and completeness of such information is not guaranteed. Forecasts and other forward-looking information obtained from these sources are subject to the same qualifications and uncertainties as the other forward-looking statements in this Annual Report. These forecasts and forward-looking information are subject to uncertainty and risk due to a variety of factors, including those described under “Risk Factors.” These and other factors could cause results to differ materially from those expressed in any forecasts or estimates. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 144/A, 20-F, 25-NSE, 3, 4, 424B3, 424B5, 425, 6-K, 8-A12B, CERT, CORRESP, EFFECT, F-1, F-1/A, F-3, F-3/A, F-4, F-4/A, POS AM, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:11.826425+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
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
| 2026-10-20 | 4 | 0001859690-26-000196 | — | [S03] |
| 2026-10-20 | 4 | 0001859690-26-000195 | — | [S04] |
| 2026-10-20 | 4 | 0001859690-26-000194 | — | [S05] |
| 2026-10-15 | 4 | 0001859690-26-000193 | — | [S06] |
| 2026-10-13 | 144 | 0001959173-26-007353 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001859690.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0001859690-26-000196](https://www.sec.gov/Archives/edgar/data/1859690/000185969026000196/0001859690-26-000196-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [4 0001859690-26-000195](https://www.sec.gov/Archives/edgar/data/1859690/000185969026000195/0001859690-26-000195-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001859690-26-000194](https://www.sec.gov/Archives/edgar/data/1859690/000185969026000194/0001859690-26-000194-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001859690-26-000193](https://www.sec.gov/Archives/edgar/data/1859690/000185969026000193/0001859690-26-000193-index.html) — published 2026-10-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [144 0001959173-26-007353](https://www.sec.gov/Archives/edgar/data/1859690/000195917326007353/0001959173-26-007353-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001104659-25-119500](https://www.sec.gov/Archives/edgar/data/1859690/000110465925119500/arqq-20250930x20f.htm) — published 2025-12-09; retrieved 2026-11-14T18:44:20.150871+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/2f077c0023bcb685dbbb970d68a962dd99ff31fe/brain/companies/ARQQ/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
