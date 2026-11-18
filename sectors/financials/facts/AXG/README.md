---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001959224
cik: 0001959224
company_name: Solowin Holdings, Ltd.
tickers:
- AXG
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: ddae9173dac59b8f117d07d566c062594b1014b4
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - '144'
  - 20-F
  - '3'
  - 424B4
  - 424B5
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-A12B/A
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
  - FWP
  - NT 20-F
  - RW
  - S-8
  - S-8 POS
  - SC 13G
  - SCHEDULE 13D
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001959224.json
    sha256: 26a54a155761a8e56a868d4c4f267501b903b52931d13cc1997e42497240ac48
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001959224.json
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
  url: https://data.sec.gov/submissions/CIK0001959224.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 26a54a155761a8e56a868d4c4f267501b903b52931d13cc1997e42497240ac48
- id: S03
  title: 424B5 0001213900-26-111765
  url: https://www.sec.gov/Archives/edgar/data/1959224/000121390026111765/0001213900-26-111765-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001213900-26-111760
  url: https://www.sec.gov/Archives/edgar/data/1959224/000121390026111760/0001213900-26-111760-index.html
  published_at: '2026-10-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 6-K 0001213900-26-110714
  url: https://www.sec.gov/Archives/edgar/data/1959224/000121390026110714/0001213900-26-110714-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: SCHEDULE 13G 0001851416-26-000032
  url: https://www.sec.gov/Archives/edgar/data/1959224/000185141626000032/0001851416-26-000032-index.html
  published_at: '2026-10-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001213900-26-106393
  url: https://www.sec.gov/Archives/edgar/data/1959224/000121390026106393/0001213900-26-106393-index.html
  published_at: '2026-10-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1959224/000121390026084178/ea0298409-20f_solowin.htm
  title: 20-F 0001213900-26-084178
  published_at: '2026-08-03'
  retrieved_at: '2026-11-18T21:03:43.808997+00:00'
  sha256: 2c94f1907bbb8934582891412d1bf5f5099cf2f0b8b0b5404fe6274cd02dea5b
issuer_classification:
  cik: 0001959224
  classification_status: reported_sic
  entity_type: other
  name: Solowin Holdings, Ltd.
  sic: '6211'
  sic_description: Security Brokers, Dealers & Flotation Companies
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 26a54a155761a8e56a868d4c4f267501b903b52931d13cc1997e42497240ac48
  url: https://data.sec.gov/submissions/CIK0001959224.json
listings:
- ticker: AXG
  exchange: NASDAQ
  instrument_type: equity_candidate
research_filings:
- accession: 0001213900-26-084178
  filed: '2026-08-03'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1959224/000121390026084178/0001213900-26-084178-index.html
- accession: 0001213900-26-111760
  filed: '2026-10-22'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1959224/000121390026111760/0001213900-26-111760-index.html
- accession: 0001213900-25-093117
  filed: '2025-09-29'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1959224/000121390025093117/0001213900-25-093117-index.html
- accession: 0001213900-25-077673
  filed: '2025-08-18'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1959224/000121390025077673/0001213900-25-077673-index.html
research_progress:
  stage: evidence_collected
  input_sha256: d7b5d88ac07a60c787e5509a2f323c7299907255ef672c2d7d513f047f2aed77
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
  sector: financials
  method: project_sic_rule
  sic: '6211'
  sic_description: Security Brokers, Dealers & Flotation Companies
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001959224.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AXG/README.md
full_history_commit: b9d67ef2f16565081e0df464efbaff4348778881
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AXG — Solowin Holdings, Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AXG/README.md)

## Business overview

Reported issuer name: **Solowin Holdings, Ltd.**. Stable SEC CIK: **0001959224**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AXG | NASDAQ | equity_candidate | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-08-03, L632:

> in this report that are important to our business. Solely for convenience, the trademarks, service marks and trade names referred to [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-08-03, L5365:

> fees and enterprise solution integration fees represent our fast-growing revenue streams. Our revenue growth relies entirely on continuous [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-08-03, L1327:

> may require us to modify our products, restrict the use of certain AI models or data sets, disclose or validate model functionality, [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-08-03, L2307:

> personal data from our customers in connection with our business and operations and we are subject to various regulatory requirements [S54]

## Industry and value chain

SEC-reported SIC **6211**: Security Brokers, Dealers & Flotation Companies. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-08-03, L8829:

> We maintain a technology and cybersecurity program, which includes information security, as part of our overall risk management process with the aim that our information systems, including those of our suppliers and other third-parties, will be resilient, effective and capable of safeguarding against emerging risks and cybersecurity threats. We endeavor to assure our program is appropriately resourced and to attract and retain expert talent to execute it. [S54]

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-08-03, L1619:

> with limited notice. Competition for specialized AI and blockchain technical talent is intense, and our ability to retain key personnel, [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-08-03, L1325:

> transparency, explainability, data privacy, intellectual property, cybersecurity, consumer protection and use of AI in regulated financial [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-08-03, L1397:

> income, or the pace of institutional adoption of digital assets and AI technologies. Our efforts to attract new clients and expand our [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-08-03, L85:

> received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-08-03, L655:

> limited to, those that we discussed or referred to in Item 3 “Key information—D. Risk Factors” and elsewhere in this [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 3, 424B4, 424B5, 6-K, 6-K/A, 8-A12B, 8-A12B/A, CERT, CORRESP, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, F-3/A, FWP, NT 20-F, RW, S-8, S-8 POS, SC 13G, SCHEDULE 13D, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:27.129684+00:00.

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
| 2026-10-22 | 424B5 | 0001213900-26-111765 | — | [S03] |
| 2026-10-22 | 6-K | 0001213900-26-111760 | — | [S04] |
| 2026-10-19 | 6-K | 0001213900-26-110714 | — | [S05] |
| 2026-10-13 | SCHEDULE 13G | 0001851416-26-000032 | — | [S06] |
| 2026-10-02 | 6-K | 0001213900-26-106393 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.070084+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001959224.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [424B5 0001213900-26-111765](https://www.sec.gov/Archives/edgar/data/1959224/000121390026111765/0001213900-26-111765-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001213900-26-111760](https://www.sec.gov/Archives/edgar/data/1959224/000121390026111760/0001213900-26-111760-index.html) — published 2026-10-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [6-K 0001213900-26-110714](https://www.sec.gov/Archives/edgar/data/1959224/000121390026110714/0001213900-26-110714-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [SCHEDULE 13G 0001851416-26-000032](https://www.sec.gov/Archives/edgar/data/1959224/000185141626000032/0001851416-26-000032-index.html) — published 2026-10-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001213900-26-106393](https://www.sec.gov/Archives/edgar/data/1959224/000121390026106393/0001213900-26-106393-index.html) — published 2026-10-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001213900-26-084178](https://www.sec.gov/Archives/edgar/data/1959224/000121390026084178/ea0298409-20f_solowin.htm) — published 2026-08-03; retrieved 2026-11-18T21:03:43.808997+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AXG/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
