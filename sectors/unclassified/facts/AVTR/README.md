---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001722482
cik: 0001722482
company_name: Avantor, Inc.
tickers:
- AVTR
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 107777182f87f961989f84e51ee16bb872074fdf
financial_history_available: false
curated_research: null
financial_gap:
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-Q
  - '144'
  - 15-12B
  - 25-NSE
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B4
  - 424B5
  - 424B7
  - '5'
  - 8-A12B
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - CORRESP
  - D
  - DEF 14A
  - DEFA14A
  - DRS
  - EFFECT
  - FWP
  - POSASR
  - PRE 14A
  - S-1
  - S-1/A
  - S-1MEF
  - S-3ASR
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
    url: https://data.sec.gov/submissions/CIK0001722482.json
    sha256: a4200908d53e817f06c8b9aeb07279ff40ff2eeae6ada41d3c0753ce2cc3f516
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001722482.json
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
  url: https://data.sec.gov/submissions/CIK0001722482.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: a4200908d53e817f06c8b9aeb07279ff40ff2eeae6ada41d3c0753ce2cc3f516
- id: S03
  title: 4 0001628280-26-063227
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026063227/0001628280-26-063227-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 3 0001628280-26-063223
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026063223/0001628280-26-063223-index.html
  published_at: '2026-09-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 8-K 0000947871-26-000877
  url: https://www.sec.gov/Archives/edgar/data/1722482/000094787126000877/0000947871-26-000877-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 8-K 0000947871-26-000876
  url: https://www.sec.gov/Archives/edgar/data/1722482/000094787126000876/0000947871-26-000876-index.html
  published_at: '2026-09-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 8-K/A 0001628280-26-059273
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026059273/0001628280-26-059273-index.html
  published_at: '2026-08-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S55
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026050415/avtr-20260630.htm
  title: 10-Q 0001628280-26-050415
  published_at: '2026-07-29'
  retrieved_at: '2026-11-18T21:01:17.451216+00:00'
  sha256: 7996fef584424b699f1b7c90e1fa37c813e3d81b2c9652ff5c33006c62626070
- id: S56
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026021572/avtr-20260326.htm
  title: DEF 14A 0001628280-26-021572
  published_at: '2026-03-27'
  retrieved_at: '2026-11-18T21:01:15.810550+00:00'
  sha256: fb1b88814c8cdd403e94f8093186d30fe84e084b80e4d6c62ae3f9d9884fa639
- id: S59
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026007118/avtr-20251231.htm
  title: 10-K 0001628280-26-007118
  published_at: '2026-02-11'
  retrieved_at: '2026-11-18T21:01:11.118671+00:00'
  sha256: 24135c0ffdda22d17425ae7832dfbf9e6a9f87c9042d9d008f088aee1b3c024d
issuer_classification:
  cik: 0001722482
  classification_status: reported_sic
  entity_type: operating
  name: Avantor, Inc.
  sic: '3826'
  sic_description: Laboratory Analytical Instruments
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: a4200908d53e817f06c8b9aeb07279ff40ff2eeae6ada41d3c0753ce2cc3f516
  url: https://data.sec.gov/submissions/CIK0001722482.json
listings:
- ticker: AVTR
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-007118
  filed: '2026-02-11'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026007118/0001628280-26-007118-index.html
- accession: 0001628280-26-050415
  filed: '2026-07-29'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026050415/0001628280-26-050415-index.html
- accession: 0001628280-26-021572
  filed: '2026-03-27'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026021572/0001628280-26-021572-index.html
- accession: 0000947871-26-000877
  filed: '2026-09-21'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1722482/000094787126000877/0000947871-26-000877-index.html
- accession: 0001628280-26-059273
  filed: '2026-08-27'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026059273/0001628280-26-059273-index.html
- accession: 0001628280-26-011727
  filed: '2026-02-25'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026011727/0001628280-26-011727-index.html
- accession: 0001628280-26-011722
  filed: '2026-02-25'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1722482/000162828026011722/0001628280-26-011722-index.html
- accession: 0001722482-21-000220
  filed: '2021-08-18'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1722482/000172248221000220/0001722482-21-000220-index.html
- accession: 0001722482-21-000218
  filed: '2021-08-18'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1722482/000172248221000218/0001722482-21-000218-index.html
- accession: 0001722482-19-000036
  filed: '2019-11-05'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1722482/000172248219000036/0001722482-19-000036-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 66417c8dbf8a07067001db017fb75c237e74747d68f2735ee84c75d54da3546a
  last_attempt_at: '2026-11-18T21:00:27.361756+00:00'
  last_success_at: '2026-11-18T21:00:27.361756+00:00'
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
  sector: unclassified
  method: unresolved
  sic: '3826'
  sic_description: Laboratory Analytical Instruments
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/AVTR/README.md
full_history_commit: 0f49b319f95dcee8e757e592a38a028a04a7bc3c
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AVTR — Avantor, Inc.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/AVTR/README.md)

## Business overview

Reported issuer name: **Avantor, Inc.**. Stable SEC CIK: **0001722482**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AVTR | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-07-29, L175:

> •adverse impacts from currency exchange rates or currency controls imposed by any government in major areas where we operate or otherwise or from potential changes in trade restrictions, tariffs and exchange controls; [S55]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-07-29, L571:

> Effective January 1, 2026, we revised our internal operating model and reporting structure and now operate and report our results through two operating segments, which are also our reportable segments: Bioscience & Medtech Products and VWR Distribution & Services. This structure is consistent with how our Chief Executive Officer, who is our CODM, assesses performance and allocates resources. This segment change did not impact our consolidated operating results. Segment disclosures, including those for comparative periods presented, have been revised to conform to the current period presentation. [S55]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — DEF 14A, filed 2026-03-27, L951:

> is our channel business with the balance being our services offerings. This business builds on VWR’s nearly 175-year [S56]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — DEF 14A, filed 2026-03-27, L2152:

> Our success is built and sustained by the trust we have earned from our customers, suppliers, distributors, associates, [S56]

## Industry and value chain

SEC-reported SIC **3826**: Laboratory Analytical Instruments. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 10-Q, filed 2026-07-29, L872:

> Our business involves risk of product liability, patent infringement and other claims in the ordinary course of business arising from the products that we produce ourselves or obtain from our suppliers, as well as from the services we provide. Our exposure to such claims may increase to the extent that we expand our manufacturing operations or service offerings. [S55]

Navigation sector: **unclassified**. Method: `unresolved`. Missing, ambiguous or unmapped reported industry; company-specific review is required.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — DEF 14A, filed 2026-03-27, L7543:

> year period thereafter, he has also agreed not to solicit our employees or customers, compete with us, or interfere with our [S56]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-K, filed 2026-02-11, L393:

> We rely on intellectual property rights, nondisclosure and other contractual provisions and technical measures to protect our offerings, services and intangible assets. Much of our intellectual property is know-how and asset configurations that we treat as trade secrets. These proprietary rights are important to our ongoing operations. In some instances, we may license our technology to third parties or may elect to license intellectual property from others. We have applied in the United States and certain foreign [S59]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-Q, filed 2026-07-29, L872:

> Our business involves risk of product liability, patent infringement and other claims in the ordinary course of business arising from the products that we produce ourselves or obtain from our suppliers, as well as from the services we provide. Our exposure to such claims may increase to the extent that we expand our manufacturing operations or service offerings. [S55]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-07-29, L1678:

> In October 2025, our Board of Directors authorized the repurchase of up to $500.0 million of our common stock. Repurchases may be funded through available cash, borrowings under existing credit [S55]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-07-29, L158:

> You should understand that the following important factors, in addition to those discussed under Part I, Item 1A “Risk Factors” in our Annual Report, as such risk factors may be updated from time to time in our periodic filings with the SEC and in this report, could affect our future results and could cause those results or other outcomes to differ materially from those expressed or implied in our forward-looking statements: [S55]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-K, 10-Q, 144, 15-12B, 25-NSE, 3, 3/A, 4, 4/A, 424B4, 424B5, 424B7, 5, 8-A12B, 8-K, 8-K/A, ARS, CERT, CORRESP, D, DEF 14A, DEFA14A, DRS, EFFECT, FWP, POSASR, PRE 14A, S-1, S-1/A, S-1MEF, S-3ASR, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:35:16.556220+00:00.

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
| 2026-09-23 | 4 | 0001628280-26-063227 | — | [S03] |
| 2026-09-23 | 3 | 0001628280-26-063223 | — | [S04] |
| 2026-09-21 | 8-K | 0000947871-26-000877 | — | [S05] |
| 2026-09-21 | 8-K | 0000947871-26-000876 | — | [S06] |
| 2026-08-27 | 8-K/A | 0001628280-26-059273 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001722482.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0001628280-26-063227](https://www.sec.gov/Archives/edgar/data/1722482/000162828026063227/0001628280-26-063227-index.html) — published 2026-09-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [3 0001628280-26-063223](https://www.sec.gov/Archives/edgar/data/1722482/000162828026063223/0001628280-26-063223-index.html) — published 2026-09-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [8-K 0000947871-26-000877](https://www.sec.gov/Archives/edgar/data/1722482/000094787126000877/0000947871-26-000877-index.html) — published 2026-09-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [8-K 0000947871-26-000876](https://www.sec.gov/Archives/edgar/data/1722482/000094787126000876/0000947871-26-000876-index.html) — published 2026-09-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [8-K/A 0001628280-26-059273](https://www.sec.gov/Archives/edgar/data/1722482/000162828026059273/0001628280-26-059273-index.html) — published 2026-08-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S55] [10-Q 0001628280-26-050415](https://www.sec.gov/Archives/edgar/data/1722482/000162828026050415/avtr-20260630.htm) — published 2026-07-29; retrieved 2026-11-18T21:01:17.451216+00:00.

[S56] [DEF 14A 0001628280-26-021572](https://www.sec.gov/Archives/edgar/data/1722482/000162828026021572/avtr-20260326.htm) — published 2026-03-27; retrieved 2026-11-18T21:01:15.810550+00:00.

[S59] [10-K 0001628280-26-007118](https://www.sec.gov/Archives/edgar/data/1722482/000162828026007118/avtr-20251231.htm) — published 2026-02-11; retrieved 2026-11-18T21:01:11.118671+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/0f49b319f95dcee8e757e592a38a028a04a7bc3c/brain/companies/AVTR/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
