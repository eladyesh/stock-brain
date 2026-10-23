---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001253986
cik: 0001253986
company_name: ARBOR REALTY TRUST INC
tickers:
- ABR
status: stub
canonical_reviewed: false
as_of: '2026-10-23'
updated_at: '2026-10-23T14:35:22.252685+00:00'
reviewed_at: null
coverage_release: coverage-20261023-39968262770-1
source_commit: 3f697433c3580d4ca83edbe44c66580ac926c8d7
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
  - 25-NSE
  - '3'
  - 3/A
  - 305B2
  - '4'
  - 4/A
  - 424B2
  - 424B3
  - 424B5
  - '5'
  - 8-A12B
  - 8-K
  - 8-K/A
  - ABS-15G
  - ARS
  - CERT
  - CERTNYS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - FWP
  - PRE 14A
  - PRER14A
  - S-3
  - S-3/A
  - S-3ASR
  - S-4
  - S-4/A
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001253986.json
    sha256: 54e13e9a3f2211e2012f276d27767957a2f2453555fa3d382a7f7f72024a2f5c
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001253986.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: otherlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt
  published_at: null
  retrieved_at: '2026-10-23T14:17:55.298415+00:00'
  sha256: be329650ef672c0314f0e16b2e41951f6af4ae314df9a04a32dc11ddb70b194e
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001253986.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 54e13e9a3f2211e2012f276d27767957a2f2453555fa3d382a7f7f72024a2f5c
- id: S03
  title: 4 0001104659-26-112894
  url: https://www.sec.gov/Archives/edgar/data/1253986/000110465926112894/0001104659-26-112894-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 4 0001104659-26-108577
  url: https://www.sec.gov/Archives/edgar/data/1253986/000110465926108577/0001104659-26-108577-index.html
  published_at: '2026-09-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001104659-26-104321
  url: https://www.sec.gov/Archives/edgar/data/1253986/000110465926104321/0001104659-26-104321-index.html
  published_at: '2026-09-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001104659-26-104317
  url: https://www.sec.gov/Archives/edgar/data/1253986/000110465926104317/0001104659-26-104317-index.html
  published_at: '2026-09-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001104659-26-104313
  url: https://www.sec.gov/Archives/edgar/data/1253986/000110465926104313/0001104659-26-104313-index.html
  published_at: '2026-09-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1253986/000125398626000048/abr-20260630.htm
  title: 10-Q 0001253986-26-000048
  published_at: '2026-07-31'
  retrieved_at: '2026-10-23T18:27:19.846909+00:00'
  sha256: 989bbd239d78fb6c0df07a7fdacc7ac606c0431396b83b2e4d558920d8b9c467
- id: S56
  url: https://www.sec.gov/Archives/edgar/data/1253986/000125398626000019/abr-20251231.htm
  title: 10-K 0001253986-26-000019
  published_at: '2026-02-27'
  retrieved_at: '2026-10-23T18:27:16.176214+00:00'
  sha256: 9d7de4af512cb72f5c273fe4f69de281f9541669af30f9bb5424705fb0e40d8c
issuer_classification:
  cik: 0001253986
  classification_status: reported_sic
  entity_type: operating
  name: ARBOR REALTY TRUST INC
  sic: '6798'
  sic_description: Real Estate Investment Trusts
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 54e13e9a3f2211e2012f276d27767957a2f2453555fa3d382a7f7f72024a2f5c
  url: https://data.sec.gov/submissions/CIK0001253986.json
listings:
- ticker: ABR
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001253986-26-000019
  filed: '2026-02-27'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1253986/000125398626000019/0001253986-26-000019-index.html
- accession: 0001253986-26-000048
  filed: '2026-07-31'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1253986/000125398626000048/0001253986-26-000048-index.html
- accession: 0001253986-26-000027
  filed: '2026-04-16'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1253986/000125398626000027/0001253986-26-000027-index.html
- accession: 0001253986-26-000053
  filed: '2026-08-11'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1253986/000125398626000053/0001253986-26-000053-index.html
- accession: 0001628280-23-033197
  filed: '2023-09-28'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1253986/000162828023033197/0001628280-23-033197-index.html
- accession: 0001104659-19-004798
  filed: '2019-01-31'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1253986/000110465919004798/0001104659-19-004798-index.html
- accession: 0001104659-17-049579
  filed: '2017-08-04'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1253986/000110465917049579/0001104659-17-049579-index.html
- accession: 0001047469-16-014726
  filed: '2016-08-05'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1253986/000104746916014726/0001047469-16-014726-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 0d2e4cc2437f010bd7301130207fa3b3ec1840ce80a9261613cc7963b90042ad
  last_attempt_at: '2026-10-23T18:20:50.371071+00:00'
  last_success_at: '2026-10-23T18:20:50.371071+00:00'
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
  sector: unclassified
  method: unresolved
  sic: '6798'
  sic_description: Real Estate Investment Trusts
  rule_version: 1
  reason: Missing, ambiguous or unmapped reported industry; company-specific review
    is required.
full_history_url: https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/ABR/README.md
full_history_commit: d523cff21b18141b9a37cddd98ad6af6e1a30fa5
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ABR — ARBOR REALTY TRUST INC

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/ABR/README.md)

## Business overview

Reported issuer name: **ARBOR REALTY TRUST INC**. Stable SEC CIK: **0001253986**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ABR | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-07-31, L124:

> The information contained in this quarterly report on Form 10-Q is not a complete description of our business or the risks associated with an investment in Arbor Realty Trust, Inc. We urge you to carefully review and consider the various disclosures in this report, as well as information in our annual report on Form 10-K for the year ended December 31, 2025 (the “2025 Annual Report”) filed with the Securities and Exchange Commission (“SEC”) on February 27, 2026 and in our other reports and filings with the SEC. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-07-31, L1801:

> (1) Includes income (loss) allocated to the noncontrolling interest holders not allocated to the two reportable segments. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-K, filed 2026-02-27, L236:

> The financing of multifamily, SFR and other diverse commercial real estate offers opportunities that demand customized financing solutions. We believe that providing both structured products and GSE/Agency loans through direct originations and in-house underwriting capabilities throughout our national network of sales offices and lending solutions through various GSE and HUD programs provides us with a competitive advantage, since this allows us to meet the multiple needs of borrowers through fully integrated, comprehensive product offerings. We employ the following investment strategies: [S56]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-K, filed 2026-02-27, L592:

> Cybersecurity incidents and cyberattacks, which include malicious software, ransomware or terrorists attacks, unauthorized attempts to gain access to sensitive, confidential or otherwise protected information related to us and our customers, have been occurring globally at a more frequent and severe level and are expected to continue to increase in frequency and severity in the future. In the course of our business, we gather, transmit and retain confidential information through our information systems and through the systems of various third-party vendors and service providers on whom we rely, including cloud-based technology providers, data processors, property managers, servicers and other counterparties. Although we endeavor to protect confidential information through the implementation of security technologies, processes and procedures, it is possible that an individual or group could penetrate our security systems or those of our third-party providers and access sensitive information about our business, borrowers and employees. Any misappropriation, loss or unauthorized disclosure of confidential information gathered, stored or used by us or by our third-party providers could have a material impact on the operation of our business, including damaging our reputation with our borrowers, employees, third parties and investors. We could also incur significant costs in … [S56]

## Industry and value chain

SEC-reported SIC **6798**: Real Estate Investment Trusts. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Navigation sector: **unclassified**. Method: `unresolved`. Missing, ambiguous or unmapped reported industry; company-specific review is required.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-Q, filed 2026-07-31, L125:

> This report contains certain “forward-looking statements” within the meaning of the Private Securities Litigation Reform Act of 1995. Such forward-looking statements relate to, among other things, the operating performance of our investments and financing needs. We use words such as “anticipate,” “expect,” “believe,” “intend,” “should,” “could,” “will,” “may” and similar expressions to identify forward-looking statements, although not all forward-looking statements include these words. Forward-looking statements are based on certain assumptions, discuss future expectations, describe future plans and strategies, contain projections of results of operations or of financial condition or state other forward-looking information. Our ability to predict results or the actual effect of future plans or strategies is inherently uncertain. These forward-looking statements involve risks, uncertainties and other factors that may cause our actual results in future periods to differ materially from forecasted results. Factors that could have a material adverse effect on our results of operations, financial condition and future prospects include, but are not limited to, economic, macroeconomic and geopolitical conditions; the real estate market; adverse changes in our status with government-sponsored enterprises affecting our ability to originate loans through such programs; changes in … [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-K, filed 2026-02-27, L236:

> The financing of multifamily, SFR and other diverse commercial real estate offers opportunities that demand customized financing solutions. We believe that providing both structured products and GSE/Agency loans through direct originations and in-house underwriting capabilities throughout our national network of sales offices and lending solutions through various GSE and HUD programs provides us with a competitive advantage, since this allows us to meet the multiple needs of borrowers through fully integrated, comprehensive product offerings. We employ the following investment strategies: [S56]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-K, filed 2026-02-27, L239:

> Manage Credit Quality. A critical component of our strategy is our ability to manage the real estate risks associated with our investment portfolio. We actively manage the credit quality of our portfolio by using the expertise of our asset management group, which has a proven track record of structuring and repositioning investments to improve credit quality and yield. [S56]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-07-31, L1473:

> On July 31, 2024, a purported shareholder filed a securities class action lawsuit against us and certain of our executive officers in the United States District Court for the Eastern District of New York (the “Court”), alleging violations of Sections 10(b) and 20(a) of the Exchange Act and Rule 10b-5 promulgated thereunder. The plaintiffs sought to represent a class of shareholders who purchased our shares of common stock between May 7, 2021 and July 11, 2024. [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-07-31, L125:

> This report contains certain “forward-looking statements” within the meaning of the Private Securities Litigation Reform Act of 1995. Such forward-looking statements relate to, among other things, the operating performance of our investments and financing needs. We use words such as “anticipate,” “expect,” “believe,” “intend,” “should,” “could,” “will,” “may” and similar expressions to identify forward-looking statements, although not all forward-looking statements include these words. Forward-looking statements are based on certain assumptions, discuss future expectations, describe future plans and strategies, contain projections of results of operations or of financial condition or state other forward-looking information. Our ability to predict results or the actual effect of future plans or strategies is inherently uncertain. These forward-looking statements involve risks, uncertainties and other factors that may cause our actual results in future periods to differ materially from forecasted results. Factors that could have a material adverse effect on our results of operations, financial condition and future prospects include, but are not limited to, economic, macroeconomic and geopolitical conditions; the real estate market; adverse changes in our status with government-sponsored enterprises affecting our ability to originate loans through such programs; changes in … [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-K, 10-Q, 144, 25-NSE, 3, 3/A, 305B2, 4, 4/A, 424B2, 424B3, 424B5, 5, 8-A12B, 8-K, 8-K/A, ABS-15G, ARS, CERT, CERTNYS, CORRESP, DEF 14A, DEFA14A, EFFECT, FWP, PRE 14A, PRER14A, S-3, S-3/A, S-3ASR, S-4, S-4/A, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-23T14:28:40.242000+00:00.

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
| 2026-10-01 | 4 | 0001104659-26-112894 | — | [S03] |
| 2026-09-17 | 4 | 0001104659-26-108577 | — | [S04] |
| 2026-09-01 | 4 | 0001104659-26-104321 | — | [S05] |
| 2026-09-01 | 4 | 0001104659-26-104317 | — | [S06] |
| 2026-09-01 | 4 | 0001104659-26-104313 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-10-23T14:17:55.298415+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001253986.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [4 0001104659-26-112894](https://www.sec.gov/Archives/edgar/data/1253986/000110465926112894/0001104659-26-112894-index.html) — published 2026-10-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [4 0001104659-26-108577](https://www.sec.gov/Archives/edgar/data/1253986/000110465926108577/0001104659-26-108577-index.html) — published 2026-09-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001104659-26-104321](https://www.sec.gov/Archives/edgar/data/1253986/000110465926104321/0001104659-26-104321-index.html) — published 2026-09-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001104659-26-104317](https://www.sec.gov/Archives/edgar/data/1253986/000110465926104317/0001104659-26-104317-index.html) — published 2026-09-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001104659-26-104313](https://www.sec.gov/Archives/edgar/data/1253986/000110465926104313/0001104659-26-104313-index.html) — published 2026-09-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [10-Q 0001253986-26-000048](https://www.sec.gov/Archives/edgar/data/1253986/000125398626000048/abr-20260630.htm) — published 2026-07-31; retrieved 2026-10-23T18:27:19.846909+00:00.

[S56] [10-K 0001253986-26-000019](https://www.sec.gov/Archives/edgar/data/1253986/000125398626000019/abr-20251231.htm) — published 2026-02-27; retrieved 2026-10-23T18:27:16.176214+00:00.

Source release: `coverage-20261023-39968262770-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/d523cff21b18141b9a37cddd98ad6af6e1a30fa5/brain/companies/ABR/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
