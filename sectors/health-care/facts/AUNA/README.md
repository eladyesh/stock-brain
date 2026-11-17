---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001799207
cik: 0001799207
company_name: AUNA S.A.
tickers:
- AUNA
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
  - 20-F
  - 20-F/A
  - '3'
  - 3/A
  - '4'
  - 424B1
  - 6-K
  - 6-K/A
  - 8-A12B
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - F-3/A
  - RW
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SEC STAFF LETTER
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001799207.json
    sha256: d5dd37b363fbed516433ae140cef7ae6cd6c51654240bf20029af93f86388af2
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001799207.json
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
  url: https://data.sec.gov/submissions/CIK0001799207.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d5dd37b363fbed516433ae140cef7ae6cd6c51654240bf20029af93f86388af2
- id: S03
  title: 6-K 0000950103-26-015991
  url: https://www.sec.gov/Archives/edgar/data/1799207/000095010326015991/0000950103-26-015991-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: SCHEDULE 13G/A 0001398344-26-018004
  url: https://www.sec.gov/Archives/edgar/data/1799207/000139834426018004/0001398344-26-018004-index.html
  published_at: '2026-10-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0000950103-26-012579
  url: https://www.sec.gov/Archives/edgar/data/1799207/000095010326012579/0000950103-26-012579-index.html
  published_at: '2026-08-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: SCHEDULE 13G/A 0000796848-26-000009
  url: https://www.sec.gov/Archives/edgar/data/1799207/000079684826000009/0000796848-26-000009-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0000950103-26-010680
  url: https://www.sec.gov/Archives/edgar/data/1799207/000095010326010680/0000950103-26-010680-index.html
  published_at: '2026-07-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1799207/000119312526168210/d108315d20f.htm
  title: 20-F 0001193125-26-168210
  published_at: '2026-04-22'
  retrieved_at: '2026-11-17T21:32:23.587612+00:00'
  sha256: 42fadc64d0bb1a99ea2a7037ac03de9a647efd132ae18bbf78e8d59f991c9a60
issuer_classification:
  cik: 0001799207
  classification_status: reported_sic
  entity_type: other
  name: AUNA S.A.
  sic: '8011'
  sic_description: Services-Offices & Clinics of  Doctors of  Medicine
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: d5dd37b363fbed516433ae140cef7ae6cd6c51654240bf20029af93f86388af2
  url: https://data.sec.gov/submissions/CIK0001799207.json
listings:
- ticker: AUNA
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-168210
  filed: '2026-04-22'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1799207/000119312526168210/0001193125-26-168210-index.html
- accession: 0001193125-25-114989
  filed: '2025-05-07'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1799207/000119312525114989/0001193125-25-114989-index.html
- accession: 0000950103-26-015991
  filed: '2026-10-22'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1799207/000095010326015991/0000950103-26-015991-index.html
- accession: 0001193125-25-252433
  filed: '2025-10-28'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1799207/000119312525252433/0001193125-25-252433-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 0fb0b2fca089747e3876009e68aa5b6efb6d380e249c2816eeab093ecf816d94
  last_attempt_at: '2026-11-17T21:29:10.535348+00:00'
  last_success_at: '2026-11-17T21:29:10.535348+00:00'
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
  sector: health-care
  method: project_sic_rule
  sic: '8011'
  sic_description: Services-Offices & Clinics of  Doctors of  Medicine
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001799207.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/4221fdf1cbfcbe1be4425ff7f3389bba890abacf/brain/companies/AUNA/README.md
full_history_commit: 4221fdf1cbfcbe1be4425ff7f3389bba890abacf
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AUNA — AUNA S.A.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/4221fdf1cbfcbe1be4425ff7f3389bba890abacf/brain/companies/AUNA/README.md)

## Business overview

Reported issuer name: **AUNA S.A.**. Stable SEC CIK: **0001799207**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AUNA | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-22, L778:

> We present EBITDA, Segment EBITDA, Adjusted EBITDA, EBITDA Margin, Adjusted EBITDA Margin, Adjusted Net Income, Adjusted Net Income Margin and Adjusted Leverage Ratio because we believe they assist investors and analysts in comparing our operating performance across reporting periods on a consistent basis by excluding items that we do not believe are indicative of our core operating performance. In addition, management and our board of directors use EBITDA, Segment EBITDA, Adjusted EBITDA, EBITDA Margin, Adjusted EBITDA Margin, Adjusted Net Income, Adjusted Net Income Margin and Adjusted Leverage Ratio to assess our financial performance and believe they are helpful in highlighting trends in our core operating performance, while other measures can differ significantly depending on long-term strategic decisions regarding the growth of our business. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-22, L4980:

> Operating segments are components of a company about which separate financial information is available that is regularly evaluated by the chief operating decision maker(s) in deciding how to allocate resources and assess performance. We have determined that our reportable segments are: (i) Oncosalud Peru, (ii) Healthcare Services in Peru, (iii) Healthcare Services in Colombia and (iv) Healthcare Services in Mexico. Our Oncosalud Peru segment consists of our prepaid healthcare plans and oncology services provided at our Oncosalud Peru segment facilities, including services provided under our prepaid plans and third-party healthcare plans and paid for out-of-pocket by our patients. Our Healthcare Services in Peru segment consists of healthcare services provided at any of our facilities in Peru other than those in the Oncosalud network. Oncosalud Peru is a payer to Healthcare Services in Peru, as are other third-party payers, for oncology and general healthcare services provided to it by our Healthcare Services in Peru segment, and the cost of such services are reflected as a cost to our Oncosalud Peru segment and a revenue to our Healthcare Services in Peru segment in our segment reporting. Our Healthcare Services in Colombia segment consists of healthcare services provided at any of our facilities in Colombia. Our Healthcare Services in Mexico segment consists of healthcare … [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-22, L1059:

> the cost of acquiring new equipment and technologies, or upgrading existing equipment and technologies, needed to provide our services; [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-22, L1104:

> A failure of our IT systems could also expose us to various security threats and vulnerabilities that may result in the theft, destruction, loss or misappropriation of protected health information or other data subject to privacy laws in Mexico, Peru or Colombia or loss of proprietary business information. Breaches of our security measures and the unauthorized dissemination of sensitive personal information, proprietary information or confidential information could expose us, our customers or other third parties to a risk of loss or misuse of this information, including exposing our customers to the risk of financial or medical identity theft, result in litigation and potential liability, such as regulatory penalties for us, damage our brand and reputation or otherwise harm our business. The failure of our IT systems, including the costs to eliminate or address security threats and vulnerabilities before or after a system failure, could have a material adverse effect on our business, financial condition and results of operations. [S54]

## Industry and value chain

SEC-reported SIC **8011**: Services-Offices & Clinics of  Doctors of  Medicine. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-22, L857:

> our ability to diversify our suppliers for medical equipment and supplies, as well as distressed supply chains, could increase our costs and create operational risks; [S54]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-22, L781:

> EBITDA, Segment EBITDA, Adjusted EBITDA, EBITDA Margin, Adjusted EBITDA Margin, Adjusted Net Income, Adjusted Net Income Margin and Adjusted Leverage Ratio are not measures of operating performance under IFRS Accounting Standards and have limitations as analytical tools. You should not consider such measures either in isolation or as substitutes for analyzing our results as reported under IFRS Accounting Standards. Additionally, our calculations of EBITDA, Segment EBITDA, Adjusted EBITDA, EBITDA Margin, Adjusted EBITDA Margin, Adjusted Net Income, Adjusted Net Income Margin and Adjusted Leverage Ratio may be different from the calculations used by other companies for similarly titled measures, including our competitors, and therefore may not be comparable to those of other companies. For reconciliations of EBITDA, Adjusted EBITDA, EBITDA Margin, Adjusted Net Income, Adjusted Net Income Margin, and Adjusted EBITDA Margin to profit (loss) for the period and Segment EBITDA to segment profit (loss) before tax for the period, in each case, the most directly comparable IFRS Accounting Standards measure, see “Item 5A. Operating and Financial Review and Prospects—Operating Results—Key Performance Indicators—Reconciliation of EBITDA, Segment EBITDA, Adjusted EBITDA, EBITDA Margin, Adjusted EBITDA Margin, Adjusted Net Income, Adjusted Net Income Margin and Adjusted Leverage Ratio.” [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-22, L1122:

> Our medical support staff, in particular our nurses and administrative personnel, are also critical to our success and competitive advantage. Our medical support staff is on the front lines of a patient’s experience at our hospitals and clinics, and we depend on their efforts, abilities and experience to maintain our reputation as a provider of healthcare services. In recruiting and retaining qualified hospital management, administrative personnel, nurses and other medical personnel, such as pharmacists and lab technicians, we compete with other healthcare providers, including government hospitals. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-22, L1078:

> Many of these factors are outside of our control. In addition, certain aspects of our growth strategy may also result in increased operating expenditures, such as opening new facilities or hiring additional personnel, which may not be offset by an increase in our revenue, resulting in diminished operating margins. We may also be unable to appropriately predict costs associated with the implementation of new healthcare plans, which may result in lower margins in connection with such products. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-22, L127:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-22, L792:

> By their very nature, forward-looking statements involve inherent risks and uncertainties, both general and specific, and risks exist that the predictions, forecasts, projections and other forward-looking statements will not be achieved. You should not place undue reliance on these forward-looking statements or projections. Although we believe that these forward-looking statements and projections are based on reasonable assumptions at the time they are made, you should be aware that many factors could affect our actual financial results or results of operations and could cause actual results to differ materially from those expressed in the forward-looking statements and projections. Factors that may materially affect such forward-looking statements and projections include, but are not limited to “Item 4. Key Information—D. Risk Factors” in this annual report. These risks and uncertainties include factors relating to: [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 3/A, 4, 424B1, 6-K, 6-K/A, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, F-3/A, RW, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, SEC STAFF LETTER, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:41.554644+00:00.

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
| 2026-10-22 | 6-K | 0000950103-26-015991 | — | [S03] |
| 2026-10-08 | SCHEDULE 13G/A | 0001398344-26-018004 | — | [S04] |
| 2026-08-18 | 6-K | 0000950103-26-012579 | — | [S05] |
| 2026-08-12 | SCHEDULE 13G/A | 0000796848-26-000009 | — | [S06] |
| 2026-07-15 | 6-K | 0000950103-26-010680 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001799207.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0000950103-26-015991](https://www.sec.gov/Archives/edgar/data/1799207/000095010326015991/0000950103-26-015991-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [SCHEDULE 13G/A 0001398344-26-018004](https://www.sec.gov/Archives/edgar/data/1799207/000139834426018004/0001398344-26-018004-index.html) — published 2026-10-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0000950103-26-012579](https://www.sec.gov/Archives/edgar/data/1799207/000095010326012579/0000950103-26-012579-index.html) — published 2026-08-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [SCHEDULE 13G/A 0000796848-26-000009](https://www.sec.gov/Archives/edgar/data/1799207/000079684826000009/0000796848-26-000009-index.html) — published 2026-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0000950103-26-010680](https://www.sec.gov/Archives/edgar/data/1799207/000095010326010680/0000950103-26-010680-index.html) — published 2026-07-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001193125-26-168210](https://www.sec.gov/Archives/edgar/data/1799207/000119312526168210/d108315d20f.htm) — published 2026-04-22; retrieved 2026-11-17T21:32:23.587612+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/4221fdf1cbfcbe1be4425ff7f3389bba890abacf/brain/companies/AUNA/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
