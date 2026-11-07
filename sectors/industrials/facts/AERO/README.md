---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001561861
cik: 0001561861
company_name: Grupo Aeromexico, S.A.B. de C.V.
tickers:
- AERO
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
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - '3'
  - '4'
  - 424B1
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - DRS
  - DRS/A
  - DRSLTR
  - F-1
  - F-1/A
  - FWP
  - S-8
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001561861.json
    sha256: 8a28daaee7c83fdfb7cd43d8f2d579715a188e5e1cf602bcd373320f25d63570
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001561861.json
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
  url: https://data.sec.gov/submissions/CIK0001561861.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 8a28daaee7c83fdfb7cd43d8f2d579715a188e5e1cf602bcd373320f25d63570
- id: S03
  title: 6-K 0001561861-26-000081
  url: https://www.sec.gov/Archives/edgar/data/1561861/000156186126000081/0001561861-26-000081-index.html
  published_at: '2026-10-20'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: 6-K 0001561861-26-000079
  url: https://www.sec.gov/Archives/edgar/data/1561861/000156186126000079/0001561861-26-000079-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 4 0001561861-26-000076
  url: https://www.sec.gov/Archives/edgar/data/1561861/000156186126000076/0001561861-26-000076-index.html
  published_at: '2026-10-16'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001561861-26-000072
  url: https://www.sec.gov/Archives/edgar/data/1561861/000156186126000072/0001561861-26-000072-index.html
  published_at: '2026-09-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001561861-26-000069
  url: https://www.sec.gov/Archives/edgar/data/1561861/000156186126000069/0001561861-26-000069-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1561861/000119312526197494/d101275d20f.htm
  title: 20-F 0001193125-26-197494
  published_at: '2026-04-30'
  retrieved_at: '2026-11-06T19:53:15.435431+00:00'
  sha256: 56651821f7a57fa110c04505c202ab2f29213072381229b3f3027b91b7a86c69
issuer_classification:
  cik: 0001561861
  classification_status: reported_sic
  entity_type: other
  name: Grupo Aeromexico, S.A.B. de C.V.
  sic: '4512'
  sic_description: Air Transportation, Scheduled
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 8a28daaee7c83fdfb7cd43d8f2d579715a188e5e1cf602bcd373320f25d63570
  url: https://data.sec.gov/submissions/CIK0001561861.json
listings:
- ticker: AERO
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001193125-26-197494
  filed: '2026-04-30'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1561861/000119312526197494/0001193125-26-197494-index.html
- accession: 0001561861-26-000081
  filed: '2026-10-20'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1561861/000156186126000081/0001561861-26-000081-index.html
research_progress:
  stage: evidence_collected
  input_sha256: c8b51034138e8d85fde1fa3c53e511bea93a674b0baa1c9c3eb172af1f0982be
  last_attempt_at: '2026-11-06T19:49:30.346586+00:00'
  last_success_at: '2026-11-06T19:49:30.346586+00:00'
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
  sector: industrials
  method: project_sic_rule
  sic: '4512'
  sic_description: Air Transportation, Scheduled
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001561861.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/9ce9ba7dde955e58421992481cd013c9475dbbdb/brain/companies/AERO/README.md
full_history_commit: 9ce9ba7dde955e58421992481cd013c9475dbbdb
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AERO — Grupo Aeromexico, S.A.B. de C.V.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/9ce9ba7dde955e58421992481cd013c9475dbbdb/brain/companies/AERO/README.md)

## Business overview

Reported issuer name: **Grupo Aeromexico, S.A.B. de C.V.**. Stable SEC CIK: **0001561861**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AERO | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-04-30, L1160:

> Due to rounding, numbers presented throughout this document may not add up precisely to the totals we provide, and percentages may not precisely reflect the absolute figures. The exchange rate of the peso against the U.S. dollar, as of December 31, 2025, was Ps. 17.9667 per $1.00, according to the Mexican Central Bank. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 20-F, filed 2026-04-30, L2329:

> We control PLM, our subsidiary that operates the Aeroméxico Rewards loyalty program, formerly known as Club Premier, the first frequent flyer program established in Latin America and Mexico’s largest loyalty program. Aeroméxico Rewards is designed to promote customer loyalty and customer satisfaction, which helps us retain and attract customers while generating high margin co-branded revenue streams. As of December 31, 2025, Aeroméxico Rewards had approximately 13.9 million members. Our Aeroméxico Rewards members are able to accumulate and redeem points through a diverse set of travel and shopping partners, as well as everyday credit card expenditure, which drives improved customer loyalty and profitability. Aeroméxico Rewards is the exclusive partner to Aeroméxico and is significantly larger than Mexico’s next largest airline loyalty program. In 2022, we acquired a controlling stake of PLM, the company that manages Aeroméxico Rewards, resulting in improved customer experience due to the full integration of Aeroméxico Rewards with our digital platforms. We intend to continue expanding Aeroméxico Rewards’ high margin co-branded revenue streams by promoting increased use of Aeroméxico Rewards credit cards. For further information about Aeroméxico Rewards, see “Item 4. Information on the Company—B. Business Overview—Aeroméxico Rewards Loyalty Program.” [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-04-30, L1119:

> “NPS” means Net Promoter Score. For clarification purposes, we calculate NPS through a bottom-up study, which consists of a personalized questionnaire to our customers about their experience in connection with our services, and a top-down study, which consists of a market analysis by an external consultant through blind and standardized surveys at MEX designed to identify our market position in relation to our competitors. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-04-30, L1119:

> “NPS” means Net Promoter Score. For clarification purposes, we calculate NPS through a bottom-up study, which consists of a personalized questionnaire to our customers about their experience in connection with our services, and a top-down study, which consists of a market analysis by an external consultant through blind and standardized surveys at MEX designed to identify our market position in relation to our competitors. [S54]

## Industry and value chain

SEC-reported SIC **4512**: Air Transportation, Scheduled. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-04-30, L1496:

> Steel and aluminum are key raw materials used in the manufacture and maintenance of commercial aircraft. Increases in tariffs on these and other aviation-related goods may result in higher costs for aircraft manufacturing, parts procurement, and maintenance services. These increased costs could affect our cost structure, particularly in connection with aircraft and spare parts sourced from international manufacturers such as Boeing and other U.S.-based suppliers. Supply chain disruptions, component shortages, and delivery delays – arising from elevated costs or retaliatory trade measures – may impair our ability to maintain, repair, or expand our fleet on a timely or cost-efficient basis. [S54]

Navigation sector: **industrials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-04-30, L1119:

> “NPS” means Net Promoter Score. For clarification purposes, we calculate NPS through a bottom-up study, which consists of a personalized questionnaire to our customers about their experience in connection with our services, and a top-down study, which consists of a market analysis by an external consultant through blind and standardized surveys at MEX designed to identify our market position in relation to our competitors. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-04-30, L1315:

> We have proprietary rights to trademarks used in this annual report that are important to our business, many of which are registered under applicable intellectual property laws. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-04-30, L1496:

> Steel and aluminum are key raw materials used in the manufacture and maintenance of commercial aircraft. Increases in tariffs on these and other aviation-related goods may result in higher costs for aircraft manufacturing, parts procurement, and maintenance services. These increased costs could affect our cost structure, particularly in connection with aircraft and spare parts sourced from international manufacturers such as Boeing and other U.S.-based suppliers. Supply chain disruptions, component shortages, and delivery delays – arising from elevated costs or retaliatory trade measures – may impair our ability to maintain, repair, or expand our fleet on a timely or cost-efficient basis. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-04-30, L146:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-04-30, L1313:

> In addition, projections, assumptions and estimates of the future performance of the markets in which we operate are necessarily subject to uncertainty and risk due to a variety of factors, including those described in “Item 3. Key Information—D. Risk Factors” and “Cautionary Note about Forward-Looking Statements and Risk Factor Summary.” These and other factors could cause results to differ materially from those expressed in the estimates made by third parties and by us. Accordingly, you are cautioned not to place undue reliance on such market and industry data or any other such estimates. We cannot guarantee the accuracy or completeness of this information; we have not independently verified any third-party information; and data from our internal research has not been verified by any independent source. The content of, or accessibility through, the sources and websites identified herein, except to the extent specifically described in this annual report, does not constitute a portion of this annual report and is not incorporated herein, and any websites are an inactive textual reference only. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 4, 424B1, 6-K, 8-A12B, CERT, CORRESP, DRS, DRS/A, DRSLTR, F-1, F-1/A, FWP, S-8, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:34:09.047625+00:00.

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
| 2026-10-20 | 6-K | 0001561861-26-000081 | — | [S03] |
| 2026-10-19 | 6-K | 0001561861-26-000079 | — | [S04] |
| 2026-10-16 | 4 | 0001561861-26-000076 | — | [S05] |
| 2026-09-22 | 6-K | 0001561861-26-000072 | — | [S06] |
| 2026-09-14 | 6-K | 0001561861-26-000069 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001561861.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001561861-26-000081](https://www.sec.gov/Archives/edgar/data/1561861/000156186126000081/0001561861-26-000081-index.html) — published 2026-10-20; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [6-K 0001561861-26-000079](https://www.sec.gov/Archives/edgar/data/1561861/000156186126000079/0001561861-26-000079-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [4 0001561861-26-000076](https://www.sec.gov/Archives/edgar/data/1561861/000156186126000076/0001561861-26-000076-index.html) — published 2026-10-16; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001561861-26-000072](https://www.sec.gov/Archives/edgar/data/1561861/000156186126000072/0001561861-26-000072-index.html) — published 2026-09-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001561861-26-000069](https://www.sec.gov/Archives/edgar/data/1561861/000156186126000069/0001561861-26-000069-index.html) — published 2026-09-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001193125-26-197494](https://www.sec.gov/Archives/edgar/data/1561861/000119312526197494/d101275d20f.htm) — published 2026-04-30; retrieved 2026-11-06T19:53:15.435431+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/9ce9ba7dde955e58421992481cd013c9475dbbdb/brain/companies/AERO/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
