---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001135951
cik: 0001135951
company_name: DR REDDYS LABORATORIES LTD
tickers:
- RDY
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: 68485afc2c279cc446102d99a1310528fc8bf3ae
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
  - 6-K
  - CT ORDER
  - EFFECT
  - F-6
  - S-8
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SCHEDULE 13D/A
  - SCHEDULE 13G/A
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001135951.json
    sha256: c3be80af1b8558c68cd9e82665cbae3aae5901d7068dfc7d8e7e3a95fbbb9070
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0001135951.json
      sha256: 593fbbea6512ef5ec729a5e513c465fbedaac8a66602c0abe00d0ba5a4d18732
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
  url: https://data.sec.gov/submissions/CIK0001135951.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: c3be80af1b8558c68cd9e82665cbae3aae5901d7068dfc7d8e7e3a95fbbb9070
- id: S03
  title: 6-K 0001575872-26-000725
  url: https://www.sec.gov/Archives/edgar/data/1135951/000157587226000725/0001575872-26-000725-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001575872-26-000724
  url: https://www.sec.gov/Archives/edgar/data/1135951/000157587226000724/0001575872-26-000724-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001575872-26-000721
  url: https://www.sec.gov/Archives/edgar/data/1135951/000157587226000721/0001575872-26-000721-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001575872-26-000719
  url: https://www.sec.gov/Archives/edgar/data/1135951/000157587226000719/0001575872-26-000719-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 6-K 0001575872-26-000715
  url: https://www.sec.gov/Archives/edgar/data/1135951/000157587226000715/0001575872-26-000715-index.html
  published_at: '2026-10-21'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1135951/000157587226000381/rdy0899_20f.htm
  title: 20-F 0001575872-26-000381
  published_at: '2026-05-29'
  retrieved_at: '2026-10-31T15:37:06.598426+00:00'
  sha256: 5d53193f187fd50a7c7ee903dc6315918b1b98da05736557105f889bcf5e6853
issuer_classification:
  cik: 0001135951
  classification_status: reported_sic
  entity_type: other
  name: DR REDDYS LABORATORIES LTD
  sic: '2834'
  sic_description: Pharmaceutical Preparations
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: c3be80af1b8558c68cd9e82665cbae3aae5901d7068dfc7d8e7e3a95fbbb9070
  url: https://data.sec.gov/submissions/CIK0001135951.json
listings:
- ticker: RDY
  exchange: NYSE
  instrument_type: common_stock
research_filings:
- accession: 0001575872-26-000381
  filed: '2026-05-29'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1135951/000157587226000381/0001575872-26-000381-index.html
- accession: 0001575872-18-000142
  filed: '2018-07-12'
  form: 20-F/A
  url: https://www.sec.gov/Archives/edgar/data/1135951/000157587218000142/0001575872-18-000142-index.html
- accession: 0001575872-26-000725
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1135951/000157587226000725/0001575872-26-000725-index.html
research_progress:
  stage: evidence_collected
  input_sha256: b64c180a04bb587fc6c199db8e3ad5df3c17fa3019cadaead09b4b2877035cb6
  last_attempt_at: '2026-10-31T15:34:51.132722+00:00'
  last_success_at: '2026-10-31T15:34:51.132722+00:00'
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
  source_url: https://data.sec.gov/submissions/CIK0001135951.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/9a2d93421bf50e1b28d316e7c6a7d3bd950c2718/brain/companies/RDY/README.md
full_history_commit: 9a2d93421bf50e1b28d316e7c6a7d3bd950c2718
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# RDY — DR REDDYS LABORATORIES LTD

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/9a2d93421bf50e1b28d316e7c6a7d3bd950c2718/brain/companies/RDY/README.md)

## Business overview

Reported issuer name: **DR REDDYS LABORATORIES LTD**. Stable SEC CIK: **0001135951**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| RDY | NYSE | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-05-29, L172:

> our business and operations in general, including: our ability to develop and commercialize additional pharmaceutical products; manufacturing, safety or quality control problems, which may damage our reputation for quality production and require costly remediation; interruptions in our supply chain; disruptions of our or third party information technology systems or breaches of our data security or other cyber-attacks; the failure to recruit or retain key personnel; significant sales to a limited number of customers in our U.S. market; and our ability to successfully undertake licensing opportunities; [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-05-29, L550:

> Our products currently under development, if and when fully developed and tested, may not perform as we expect or meet our standards of safety and efficacy. Necessary regulatory approvals may not be obtained in a timely manner, if at all, and we may not be able to successfully and profitably produce and market such products. Our approved products may not achieve expected levels of market acceptance. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-05-29, L180:

> our generics medicines business, including: consolidation of our customer base and commercial alliances among our customers; the increase in the number of competitors targeting generic opportunities and seeking U.S. market exclusivity for generic versions of significant products; price erosion relating to our generic products, both from competing products and increased regulation; delays in launches of new generic products; efforts of pharmaceutical companies to limit the use of generics including through legislation and regulations; the difficulty and expense of obtaining licenses to proprietary technologies; and returns, allowances and chargebacks; [S54]

## Industry and value chain

SEC-reported SIC **2834**: Pharmaceutical Preparations. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-05-29, L172:

> our business and operations in general, including: our ability to develop and commercialize additional pharmaceutical products; manufacturing, safety or quality control problems, which may damage our reputation for quality production and require costly remediation; interruptions in our supply chain; disruptions of our or third party information technology systems or breaches of our data security or other cyber-attacks; the failure to recruit or retain key personnel; significant sales to a limited number of customers in our U.S. market; and our ability to successfully undertake licensing opportunities; [S54]

Navigation sector: **health-care**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-05-29, L569:

> The regulatory requirements are still evolving and are dynamic in many emerging markets where we sell or manufacture products, including our biologic drugs, and regulatory requirements may be unclear due to lack of precedents, among other reasons, which may lead to delays in product approvals, reapproval or re-licensure process, or other sanctions and, in turn, additional cost to operations. In the United States, the Biologics Price Competition and Innovation Act of 2009 (“BPCIA”) created a statutory pathway and abbreviated approval processes for the approval of biosimilar versions of branded biological products. Further, several legal challenges concerning the requirements of the abbreviated biosimilar pathway, patent exchange and other provisions of BPCIA have been adjudicated in U.S. courts, legal challenges concerning FTO, patent exchange and trade matters, among others, continue. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-05-29, L544:

> Additionally, if we fail to adequately protect critical proprietary or confidential information or associated intellectual property rights or fail to manage third party partners and contract research organizations that our business depends on, it might have a material adverse impact on our product development execution. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-05-29, L969:

> We entered into an agreement with Nestlé Health Science India to commercialize nutritional and wellness products in India. This partnership provides access to complementary capabilities and supports our strategy to expand in consumer‑oriented health and nutrition categories. Refer to Note 35.A to the Consolidated Financial Statements for additional details on this partnership. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-05-29, L129:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-05-29, L204:

> those discussed in the sections entitled “risk factors”, “business overview” and “operating and financial review and prospects” and elsewhere in this report. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 144, 20-F, 20-F/A, 3, 6-K, CT ORDER, EFFECT, F-6, S-8, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G/A
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:31:53.537701+00:00.

### Research work queue

Collection stage: **evidence_collected**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (source excerpts available; assess the claim): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
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
| 2026-10-23 | 6-K | 0001575872-26-000725 | — | [S03] |
| 2026-10-23 | 6-K | 0001575872-26-000724 | — | [S04] |
| 2026-10-23 | 6-K | 0001575872-26-000721 | — | [S05] |
| 2026-10-23 | 6-K | 0001575872-26-000719 | — | [S06] |
| 2026-10-21 | 6-K | 0001575872-26-000715 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001135951.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001575872-26-000725](https://www.sec.gov/Archives/edgar/data/1135951/000157587226000725/0001575872-26-000725-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001575872-26-000724](https://www.sec.gov/Archives/edgar/data/1135951/000157587226000724/0001575872-26-000724-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001575872-26-000721](https://www.sec.gov/Archives/edgar/data/1135951/000157587226000721/0001575872-26-000721-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001575872-26-000719](https://www.sec.gov/Archives/edgar/data/1135951/000157587226000719/0001575872-26-000719-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [6-K 0001575872-26-000715](https://www.sec.gov/Archives/edgar/data/1135951/000157587226000715/0001575872-26-000715-index.html) — published 2026-10-21; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001575872-26-000381](https://www.sec.gov/Archives/edgar/data/1135951/000157587226000381/rdy0899_20f.htm) — published 2026-05-29; retrieved 2026-10-31T15:37:06.598426+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/9a2d93421bf50e1b28d316e7c6a7d3bd950c2718/brain/companies/RDY/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
