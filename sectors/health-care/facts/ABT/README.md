---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000001800
cik: 0000001800
company_name: ABBOTT LABORATORIES
tickers:
- ABT
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 897a5ec8e06dcb4c9844b83dea2f5d822553ed72
financial_history_available: false
curated_research: null
financial_gap:
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-Q
  - 11-K
  - '144'
  - '3'
  - 3/A
  - '4'
  - 424B3
  - 424B5
  - 8-K
  - 8-K/A
  - ARS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - FWP
  - PRE 14A
  - PX14A6G
  - S-3ASR
  - S-8
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000001800.json
    sha256: eb70623e7defeb4dcc52b6797104ebf42e45be796040189eed318e65ce99e3a9
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0000001800.json
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
  url: https://data.sec.gov/submissions/CIK0000001800.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: eb70623e7defeb4dcc52b6797104ebf42e45be796040189eed318e65ce99e3a9
- id: S03
  title: 8-K 0001628280-26-066601
  url: https://www.sec.gov/Archives/edgar/data/1800/000162828026066601/0001628280-26-066601-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 8-K 0001104659-26-117587
  url: https://www.sec.gov/Archives/edgar/data/1800/000110465926117587/0001104659-26-117587-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001104659-26-113291
  url: https://www.sec.gov/Archives/edgar/data/1800/000110465926113291/0001104659-26-113291-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 4 0001104659-26-113287
  url: https://www.sec.gov/Archives/edgar/data/1800/000110465926113287/0001104659-26-113287-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 4 0001104659-26-113286
  url: https://www.sec.gov/Archives/edgar/data/1800/000110465926113286/0001104659-26-113286-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1800/000162828026050134/abt-20260630.htm
  title: 10-Q 0001628280-26-050134
  published_at: '2026-07-28'
  retrieved_at: '2026-11-02T22:08:47.025275+00:00'
  sha256: ec840d02ba4c08e681a2164ad651c3847558e0dde4910dc7b0059b3a456de1c7
- id: S55
  url: https://www.sec.gov/Archives/edgar/data/1800/000130817926000064/abt-20260311.htm
  title: DEF 14A 0001308179-26-000064
  published_at: '2026-03-13'
  retrieved_at: '2026-11-02T22:08:45.180028+00:00'
  sha256: 15cd7a336e90e1d7dea16ca83aadcc83af69b5cbb7575a8cc98cb67a579d0ba9
- id: S56
  url: https://www.sec.gov/Archives/edgar/data/1800/000162828026010185/abt-20251231.htm
  title: 10-K 0001628280-26-010185
  published_at: '2026-02-20'
  retrieved_at: '2026-11-02T22:08:43.197233+00:00'
  sha256: d55632b106942d12eb71d0621fc819f6c6ebcf009a04feb3f34950bd6781ebbf
issuer_classification:
  cik: 0000001800
  classification_status: reported_sic
  entity_type: operating
  name: ABBOTT LABORATORIES
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: eb70623e7defeb4dcc52b6797104ebf42e45be796040189eed318e65ce99e3a9
  url: https://data.sec.gov/submissions/CIK0000001800.json
listings:
- ticker: ABT
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001628280-26-010185
  filed: '2026-02-20'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1800/000162828026010185/0001628280-26-010185-index.html
- accession: 0001628280-26-050134
  filed: '2026-07-28'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1800/000162828026050134/0001628280-26-050134-index.html
- accession: 0001308179-26-000064
  filed: '2026-03-13'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1800/000130817926000064/0001308179-26-000064-index.html
- accession: 0001628280-26-066601
  filed: '2026-10-21'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1800/000162828026066601/0001628280-26-066601-index.html
- accession: 0001104659-23-097759
  filed: '2023-09-01'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1800/000110465923097759/0001104659-23-097759-index.html
- accession: 0001104659-23-069894
  filed: '2023-06-09'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1800/000110465923069894/0001104659-23-069894-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 271d283b5d2a0f23a4ab333ae098c334530a8aa4aa924c035429c021356d0aab
  last_attempt_at: '2026-11-02T22:04:14.646377+00:00'
  last_success_at: '2026-11-02T22:04:14.646377+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - competitive-landscape
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
  sic: '2834'
  sic_description: Pharmaceutical Preparations
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000001800.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/9ce9ba7dde955e58421992481cd013c9475dbbdb/brain/companies/ABT/README.md
full_history_commit: 9ce9ba7dde955e58421992481cd013c9475dbbdb
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# ABT — ABBOTT LABORATORIES

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/9ce9ba7dde955e58421992481cd013c9475dbbdb/brain/companies/ABT/README.md)

## Business overview

Reported issuer name: **ABBOTT LABORATORIES**. Stable SEC CIK: **0000001800**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| ABT | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — DEF 14A, filed 2026-03-13, L671:

> To impact the most lives, we must get our innovative healthcare solutions to people who need them and ensure our business is resilient and prepared for the future, working to protect the environment, ensure a responsible supply chain, build the workforce of tomorrow and responsibly connect technology and care. [S55]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-07-28, L447:

> Abbott’s revenues are derived primarily from the sale of a broad portfolio of healthcare products under short-term receivable arrangements. Abbott has four reportable segments: Established Pharmaceutical Products, Nutritional Products, Diagnostic Products, and Medical Devices. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — DEF 14A, filed 2026-03-13, L665:

> At Abbott, sustainability means managing our company to deliver long-term impact for the people we serve — shaping the future of healthcare and helping the greatest number of people live better and healthier lives. Our products and services touched the lives of approximately 2 billion people in 2024 and our goal is to reach 3 billion people a year by 2030. [S55]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — DEF 14A, filed 2026-03-13, L595:

> Five new independent directors have been elected in the last five years to supplement the Board’s skills and provide fresh perspective, including in the areas of finance, supply chain and infrastructure management, technology, medical science, and healthcare delivery [S55]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-Q, filed 2026-07-28, L958:

> Abbott’s revenues are derived primarily from the sale of a broad portfolio of healthcare products under short-term receivable arrangements. Patent protection and licenses, technological and performance features, and inclusion of Abbott’s products under a contract most significantly impact which products are sold; price controls, competition, and rebates most significantly impact the net selling prices of products; and foreign currency translation impacts the measurement of net sales and costs. Abbott’s primary products are medical devices, diagnostic testing products, nutritional products, and branded generic pharmaceuticals. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 10-K, filed 2026-02-20, L303:

> Abbott is aware of the desirability for patent and trademark protection for its products. Accordingly, where possible, patents and trademarks are sought and obtained for Abbott’s products in the United States and countries of interest to Abbott. Abbott owns or has licenses under a substantial number of patents and patent applications. Principal trademarks and the products they cover are discussed in the Narrative Description of Business on pages 1 through 4. These, and various patents that expire during the period from 2026 to 2046, in the aggregate, are believed to be of material importance in the operation of Abbott’s business. Abbott believes that no single patent, license, or trademark is material in relation to Abbott’s business as a whole. [S56]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — DEF 14A, filed 2026-03-13, L774:

> •Aligned to drive Abbott’s strategic priorities, reflects strong sustainable performance resulting in total shareholder return (TSR) above the peer median on a one-year, three-year, and five-year basis. [S55]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-07-28, L1087:

> In the first six months of 2026, Abbott repurchased approximately 11.6 million of its common shares for $1.0 billion. As of June 30, 2026, $5.6 billion remains available for repurchase under the share repurchase program authorized by the board of directors in October 2024. [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-07-28, L560:

> The allowance for doubtful accounts reflects the current estimate of credit losses expected to be incurred over the life of the accounts receivable. Abbott considers various factors in establishing, monitoring, and adjusting its allowance for doubtful accounts, including the aging of the accounts and aging trends, the historical level of charge-offs, and specific exposures related to particular customers. Abbott also monitors other risk factors and forward-looking information, such as country risk, when determining credit limits for customers and establishing adequate allowances. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-K, 10-Q, 11-K, 144, 3, 3/A, 4, 424B3, 424B5, 8-K, 8-K/A, ARS, CORRESP, DEF 14A, DEFA14A, FWP, PRE 14A, PX14A6G, S-3ASR, S-8, SC 13G, SC 13G/A, SCHEDULE 13G, SCHEDULE 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:27:06.119681+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (source excerpts available; assess the claim): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (source excerpts available; assess the claim): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
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
| 2026-10-21 | 8-K | 0001628280-26-066601 | — | [S03] |
| 2026-10-21 | 8-K | 0001104659-26-117587 | — | [S04] |
| 2026-10-02 | 4 | 0001104659-26-113291 | — | [S05] |
| 2026-10-02 | 4 | 0001104659-26-113287 | — | [S06] |
| 2026-10-02 | 4 | 0001104659-26-113286 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000001800.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [8-K 0001628280-26-066601](https://www.sec.gov/Archives/edgar/data/1800/000162828026066601/0001628280-26-066601-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [8-K 0001104659-26-117587](https://www.sec.gov/Archives/edgar/data/1800/000110465926117587/0001104659-26-117587-index.html) — published 2026-10-21; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001104659-26-113291](https://www.sec.gov/Archives/edgar/data/1800/000110465926113291/0001104659-26-113291-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [4 0001104659-26-113287](https://www.sec.gov/Archives/edgar/data/1800/000110465926113287/0001104659-26-113287-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [4 0001104659-26-113286](https://www.sec.gov/Archives/edgar/data/1800/000110465926113286/0001104659-26-113286-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [10-Q 0001628280-26-050134](https://www.sec.gov/Archives/edgar/data/1800/000162828026050134/abt-20260630.htm) — published 2026-07-28; retrieved 2026-11-02T22:08:47.025275+00:00.

[S55] [DEF 14A 0001308179-26-000064](https://www.sec.gov/Archives/edgar/data/1800/000130817926000064/abt-20260311.htm) — published 2026-03-13; retrieved 2026-11-02T22:08:45.180028+00:00.

[S56] [10-K 0001628280-26-010185](https://www.sec.gov/Archives/edgar/data/1800/000162828026010185/abt-20251231.htm) — published 2026-02-20; retrieved 2026-11-02T22:08:43.197233+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/9ce9ba7dde955e58421992481cd013c9475dbbdb/brain/companies/ABT/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
