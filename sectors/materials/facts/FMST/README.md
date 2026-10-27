---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001935418
cik: 0001935418
company_name: Foremost Clean Energy Ltd.
tickers:
- FMST
status: stub
canonical_reviewed: false
as_of: '2026-10-27'
updated_at: '2026-10-27T15:30:18.641431+00:00'
reviewed_at: null
coverage_release: coverage-20261027-40530587641-1
source_commit: 79ea404d09f86d838fefd71cf88a566d57bc57a2
financial_history_available: false
curated_research: null
financial_gap:
  reason: foreign_reporting_adapter
  next_action: Add support for the observed 20-F, 40-F or 6-K reporting forms and
    verify the actual accounting taxonomy before normalization.
  observed_forms:
  - 20-F
  - 424B3
  - 424B4
  - 6-K
  - 6-K/A
  - 8-A12B
  - 8-A12B/A
  - CERT
  - CORRESP
  - D
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-1
  - F-1/A
  - F-3
  - POS AM
  - SC 13D
  - SC 13D/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001935418.json
    sha256: 913cc4b73291af091eee06b5239fb7a2a1a505b6c271f09ee41ff0f0a0d38c43
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001935418.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-27T15:25:33.739265+00:00'
  sha256: 29c7cedde394d9fb806c731f8be32ec8c78cad2668852342db80ae28619465f0
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001935418.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 913cc4b73291af091eee06b5239fb7a2a1a505b6c271f09ee41ff0f0a0d38c43
- id: S03
  title: 6-K 0001171843-26-006784
  url: https://www.sec.gov/Archives/edgar/data/1935418/000117184326006784/0001171843-26-006784-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: EFFECT 9999999995-26-002958
  url: https://www.sec.gov/Archives/edgar/data/1935418/999999999526002958/9999999995-26-002958-index.html
  published_at: '2026-09-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001171843-26-005787
  url: https://www.sec.gov/Archives/edgar/data/1935418/000117184326005787/0001171843-26-005787-index.html
  published_at: '2026-08-28'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001171843-26-005553
  url: https://www.sec.gov/Archives/edgar/data/1935418/000117184326005553/0001171843-26-005553-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: POS AM 0001171843-26-005552
  url: https://www.sec.gov/Archives/edgar/data/1935418/000117184326005552/0001171843-26-005552-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1935418/000117184326004369/fmst20260331_20f.htm
  title: 20-F 0001171843-26-004369
  published_at: '2026-06-30'
  retrieved_at: '2026-10-27T15:37:48.493106+00:00'
  sha256: ad8e770210a8a6c7ea2f09e9c54d568e97b2ab47b16f6ed732f692b5c1737f4a
issuer_classification:
  cik: 0001935418
  classification_status: reported_sic
  entity_type: other
  name: Foremost Clean Energy Ltd.
  sic: '1090'
  sic_description: Miscellaneous Metal Ores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: 913cc4b73291af091eee06b5239fb7a2a1a505b6c271f09ee41ff0f0a0d38c43
  url: https://data.sec.gov/submissions/CIK0001935418.json
listings:
- ticker: FMST
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001171843-26-004369
  filed: '2026-06-30'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1935418/000117184326004369/0001171843-26-004369-index.html
- accession: 0001171843-26-006784
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1935418/000117184326006784/0001171843-26-006784-index.html
- accession: 0001171843-23-005428
  filed: '2023-08-24'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/1935418/000117184323005428/0001171843-23-005428-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 7b41761f7e8aec624dc3cd0ed623eadbd14f3d07947010687372e68186f7207f
  last_attempt_at: '2026-10-27T15:36:38.956292+00:00'
  last_success_at: '2026-10-27T15:36:38.956292+00:00'
  next_retry_at: null
  source_set_current: true
  evidence_topics:
  - business-overview
  - competitive-landscape
  - growth-drivers
  - industry-and-value-chain
  - management-and-governance
  - moat-and-differentiation
  - recent-developments
  - risks-and-thesis-breakers
  derived_observations: 0
  model_draft: false
  reviewed: false
sector_assignment:
  sector: materials
  method: project_sic_rule
  sic: '1090'
  sic_description: Miscellaneous Metal Ores
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001935418.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/FMST/README.md
full_history_commit: ea9dd09e5d047ff0620d4500849876915bb10e87
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# FMST — Foremost Clean Energy Ltd.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/FMST/README.md)

## Business overview

Reported issuer name: **Foremost Clean Energy Ltd.**. Stable SEC CIK: **0001935418**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| FMST | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-06-30, L480:

> This Annual Report contains many statements that are “forward-looking” and uses forward-looking terminology such as “anticipate,” “believe,” “could,” “estimate,” “expect,” “future,” “intend,” “may,” “ought to,” “plan,” “possible,” “potentially,” “predicts,” “project,” “should,” “will,” “would,” negatives of such terms or other similar statements. You should not place undue reliance on any forward-looking statement due to its inherent risk and uncertainties, both general and specific. Although we believe the assumptions on which the forward-looking statements are based are reasonable and within the bounds of our knowledge of our business and operations as of the date of this Annual Report, any or all of those assumptions could prove to be inaccurate. As a result, the forward-looking statements based on those assumptions could also be incorrect. The forward-looking statements in this Annual Report include, without limitation, statements relating to: [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1090**: Miscellaneous Metal Ores. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-06-30, L674:

> Several governments or governmental bodies have introduced or are contemplating legislative and/or regulatory changes in response to concerns about the potential impact of climate change. New legislation and increased regulation regarding climate change could potentially impose significant costs on us, and on our suppliers, including costs related to increased energy requirements, capital equipment, environmental monitoring and reporting, and other costs necessary to comply with such regulations. Any adopted future climate change regulations could also negatively impact our ability to compete with companies situated in areas not subject to such limitations. Given the emotional and political significance and uncertainty surrounding the impact of climate change and how it should be dealt with, we cannot predict how legislation and regulation will ultimately affect our financial condition, operating performance, and ability to compete. Furthermore, even without such regulation, increased awareness, and any adverse publicity in the global marketplace about potential impacts on climate change by us or other companies in our industry could harm our reputation. The potential physical impacts of climate change on our operations are highly uncertain, could be particular to the geographic circumstances in areas in which we operate and may include changes in rainfall and storm patterns … [S54]

Navigation sector: **materials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-06-30, L674:

> Several governments or governmental bodies have introduced or are contemplating legislative and/or regulatory changes in response to concerns about the potential impact of climate change. New legislation and increased regulation regarding climate change could potentially impose significant costs on us, and on our suppliers, including costs related to increased energy requirements, capital equipment, environmental monitoring and reporting, and other costs necessary to comply with such regulations. Any adopted future climate change regulations could also negatively impact our ability to compete with companies situated in areas not subject to such limitations. Given the emotional and political significance and uncertainty surrounding the impact of climate change and how it should be dealt with, we cannot predict how legislation and regulation will ultimately affect our financial condition, operating performance, and ability to compete. Furthermore, even without such regulation, increased awareness, and any adverse publicity in the global marketplace about potential impacts on climate change by us or other companies in our industry could harm our reputation. The potential physical impacts of climate change on our operations are highly uncertain, could be particular to the geographic circumstances in areas in which we operate and may include changes in rainfall and storm patterns … [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-06-30, L12577:

> We have implemented and maintain various information security processes designed to identify, assess and manage material risks from cybersecurity threats to our critical computer networks, third party hosted services, communications systems, hardware and software, and our critical data, including intellectual property, confidential information that is proprietary, strategic or competitive in nature, and other data related to our ongoing research and development initiatives, which we refer to as Information Systems and Data. Our information technology function helps identify, assess and manage our cybersecurity threats and risks. Our information technology function identifies and assesses risks from cybersecurity threats by monitoring and evaluating our threat environment using various methods including, for example, automated vulnerability scanning tools of the network, third-party cybersecurity audits, and use of external intelligence feeds. Depending on the environment, we implement and maintain various technical, physical, and organizational measures, processes, standards and policies designed to manage and mitigate material risks from cybersecurity threats to our Information Systems and Data, including, for example, vulnerability management, disaster recovery and business continuity plan, incident response policy, system monitoring, data encryption and access controls. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-06-30, L729:

> We also expect that being a public company will make it more expensive for us to obtain director and officer liability insurance, and we may be required to accept reduced coverage or incur substantially higher costs to obtain coverage. These increased costs may require us to divert a significant amount of money that we could otherwise use to expand our business and achieve our strategic objectives. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-06-30, L91:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to § 240.10D-1(b). ​☐​ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-06-30, L542:

> The forward-looking statements included in this Annual Report are subject to known and unknown risks, uncertainties and assumptions about our business and business environments. These statements reflect our current views with respect to future events and are not a guarantee of future performance. Actual results of our operations may differ materially from information contained in the forward-looking statements as a result of risk factors, some of which are described under the headings “Risk Factors”, “Operating and Financial Review and Prospects,” “Information on our Company” and elsewhere in this Annual Report. Such described risks and uncertainties are not exhaustive. Other sections of this Annual Report include additional factors which could adversely impact our business and financial performance. The forward-looking statements contained in this Annual Report speak only as of the date of this Annual Report or, if obtained from third-party studies or reports, the date of the corresponding study or report, and are expressly qualified in their entirety by the cautionary statements in this Annual Report. Since we operate in an emerging and evolving environment and new risk factors and uncertainties emerge from time to time, you should not rely upon forward-looking statements as predictions of future events. Except as otherwise required by the securities laws of the United … [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 424B3, 424B4, 6-K, 6-K/A, 8-A12B, 8-A12B/A, CERT, CORRESP, D, DRS, DRS/A, DRSLTR, EFFECT, F-1, F-1/A, F-3, POS AM, SC 13D, SC 13D/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:36:23.915787+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (evidence or analysis still needed): Describe the main products, customer problems solved, distribution, and product dependencies.
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
| 2026-10-23 | 6-K | 0001171843-26-006784 | — | [S03] |
| 2026-09-14 | EFFECT | 9999999995-26-002958 | — | [S04] |
| 2026-08-28 | 6-K | 0001171843-26-005787 | — | [S05] |
| 2026-08-14 | 6-K | 0001171843-26-005553 | — | [S06] |
| 2026-08-14 | POS AM | 0001171843-26-005552 | — | [S07] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-27T15:25:33.739265+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001935418.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001171843-26-006784](https://www.sec.gov/Archives/edgar/data/1935418/000117184326006784/0001171843-26-006784-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [EFFECT 9999999995-26-002958](https://www.sec.gov/Archives/edgar/data/1935418/999999999526002958/9999999995-26-002958-index.html) — published 2026-09-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001171843-26-005787](https://www.sec.gov/Archives/edgar/data/1935418/000117184326005787/0001171843-26-005787-index.html) — published 2026-08-28; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001171843-26-005553](https://www.sec.gov/Archives/edgar/data/1935418/000117184326005553/0001171843-26-005553-index.html) — published 2026-08-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [POS AM 0001171843-26-005552](https://www.sec.gov/Archives/edgar/data/1935418/000117184326005552/0001171843-26-005552-index.html) — published 2026-08-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001171843-26-004369](https://www.sec.gov/Archives/edgar/data/1935418/000117184326004369/fmst20260331_20f.htm) — published 2026-06-30; retrieved 2026-10-27T15:37:48.493106+00:00.

Source release: `coverage-20261027-40530587641-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ea9dd09e5d047ff0620d4500849876915bb10e87/brain/companies/FMST/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
