---
schema_version: 1
document_type: company_facts
company_id: company-cik-0000904851
cik: 0000904851
company_name: YPF SOCIEDAD ANONIMA
tickers:
- YPF
status: stub
canonical_reviewed: false
as_of: '2026-11-01'
updated_at: '2026-11-01T16:11:48.803754+00:00'
reviewed_at: null
coverage_release: coverage-20261101-41324509967-1
source_commit: b7d564f6a774e716acb58b68cc3c1e8b1400a1e5
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
  - 6-K
  - 6-K/A
  - CORRESP
  - NT 20-F
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SD
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0000904851.json
    sha256: ae0cb29ecfd038015954baba80f26f881988f4f0f276ba3082ec6471f19d1cc9
    retrieved_at: '2026-10-24T13:22:51.759433+00:00'
    archive: &id001
      member: CIK0000904851.json
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
  url: https://data.sec.gov/submissions/CIK0000904851.json
  published_at: null
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: ae0cb29ecfd038015954baba80f26f881988f4f0f276ba3082ec6471f19d1cc9
- id: S03
  title: 6-K 0001554855-26-002169
  url: https://www.sec.gov/Archives/edgar/data/904851/000155485526002169/0001554855-26-002169-index.html
  published_at: '2026-10-23'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S04
  title: 6-K 0001554855-26-002124
  url: https://www.sec.gov/Archives/edgar/data/904851/000155485526002124/0001554855-26-002124-index.html
  published_at: '2026-10-14'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S05
  title: 6-K 0001554855-26-002090
  url: https://www.sec.gov/Archives/edgar/data/904851/000155485526002090/0001554855-26-002090-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S06
  title: 6-K 0001554855-26-002088
  url: https://www.sec.gov/Archives/edgar/data/904851/000155485526002088/0001554855-26-002088-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S07
  title: 4 0001292814-26-004900
  url: https://www.sec.gov/Archives/edgar/data/904851/000129281426004900/0001292814-26-004900-index.html
  published_at: '2026-10-09'
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/904851/000119312526126363/d95578d20f.htm
  title: 20-F 0001193125-26-126363
  published_at: '2026-03-26'
  retrieved_at: '2026-11-02T22:08:05.644053+00:00'
  sha256: 787633e90ee8ce6739cd4a5b3f1b325f9f071a336fd6da44fb4d9af6a65b3b08
issuer_classification:
  cik: 0000904851
  classification_status: reported_sic
  entity_type: other
  name: YPF SOCIEDAD ANONIMA
  sic: '2911'
  sic_description: Petroleum Refining
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-24T13:22:51.759433+00:00'
  sha256: ae0cb29ecfd038015954baba80f26f881988f4f0f276ba3082ec6471f19d1cc9
  url: https://data.sec.gov/submissions/CIK0000904851.json
listings:
- ticker: YPF
  exchange: NYSE
  instrument_type: depositary_receipt
research_filings:
- accession: 0001193125-26-126363
  filed: '2026-03-26'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/904851/000119312526126363/0001193125-26-126363-index.html
- accession: 0001554855-26-002169
  filed: '2026-10-23'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/904851/000155485526002169/0001554855-26-002169-index.html
- accession: 0001193125-22-282329
  filed: '2022-11-10'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/904851/000119312522282329/0001193125-22-282329-index.html
- accession: 0001193125-16-768725
  filed: '2016-11-15'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/904851/000119312516768725/0001193125-16-768725-index.html
- accession: 0001193125-16-767555
  filed: '2016-11-14'
  form: 6-K/A
  url: https://www.sec.gov/Archives/edgar/data/904851/000119312516767555/0001193125-16-767555-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 2e83eac4a68a61d9677562790a42e9d6565864c288841bd89d265e7b7c572187
  last_attempt_at: '2026-11-02T22:04:14.646377+00:00'
  last_success_at: '2026-11-02T22:04:14.646377+00:00'
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
  sector: energy
  method: project_sic_rule
  sic: '2911'
  sic_description: Petroleum Refining
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0000904851.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/ef36a46d682e789d5949ebe61d4ec5a6bea5f3de/brain/companies/YPF/README.md
full_history_commit: ef36a46d682e789d5949ebe61d4ec5a6bea5f3de
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# YPF — YPF SOCIEDAD ANONIMA

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/ef36a46d682e789d5949ebe61d4ec5a6bea5f3de/brain/companies/YPF/README.md)

## Business overview

Reported issuer name: **YPF SOCIEDAD ANONIMA**. Stable SEC CIK: **0000904851**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| YPF | NYSE | depositary_receipt | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-03-26, L525:

> This annual report, including any documents incorporated by reference, contains statements that we believe constitute forward-looking statements within the meaning of the Private Securities Litigation Reform Act of 1995. These forward-looking statements may include statements regarding the intent, belief or current expectations of us and our management, including statements with respect to trends affecting our financial condition, financial ratios, results of operations, business, strategy, geographic concentration, oil and gas reserves, future hydrocarbon production volumes and our ability to satisfy our long-term sales commitments from future supplies available to us, our ability to pay dividends in the future and to service our outstanding debt, dates or periods in which production is scheduled or expected to come on-stream, as well as our plans with respect to capital expenditures, business, strategy, geographic concentration, cost savings, discount rates, investments and dividends payout policies. These statements are not a guarantee of future performance and are subject to material risks, uncertainties, changes and other factors which may be beyond our control or may be difficult to predict. Accordingly, our future financial condition, prices, financial ratios, results of operations, business, strategy, geographic concentration, hydrocarbon production volumes, oil and … [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 20-F, filed 2026-03-26, L764:

> We cannot predict whether, and to what extent, the value of the Argentine peso may depreciate or appreciate against the U.S. dollar or other hard foreign currencies, nor the way in which we will be able to pass-through those variations to the prices of our products and how any such fluctuations could affect the demand for the products we offer, thus affecting our business. [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 20-F, filed 2026-03-26, L880:

> Although we have adopted, and continue to adopt, what we believe are the appropriate measures to ensure the proper functioning of our digital technologies and operating systems, as well as to ensure that the information of our customers, suppliers and employees is protected, no assurance can be given that we will not be subject to any cyberattacks or system failures, which can adversely affect our business and results of operations. Additionally, certain cybersecurity incidents, such as surveillance, may remain undetected for an extended period. In addition, during 2025, we have registered an increase in attempted attacks and, like other companies in the industry, were exposed to malware infections, which did not result in a material negative impact on our operations. [S54]

## Industry and value chain

SEC-reported SIC **2911**: Petroleum Refining. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-03-26, L879:

> As dependence on digital technologies is expanding, cybersecurity incidents, including deliberate attacks or unintentional events, have been increasing worldwide. We rely on digital technologies to estimate quantities of oil and gas reserves, analyze seismic and drilling information, process and store financial and operating data, as well as to support our internal communications and interactions with our third-party business partners. Cyber-attacks could compromise our digital systems, information systems and related infrastructure, or those of our business partners, and result in additional costs and disruptions to our business operations or the loss of our data and negatively impact our operations in a variety of ways and, therefore, our business, financial condition and results of operations, including but not limited to: unauthorized access to strategic and sensitive information potentially impacting on our ability to compete for oil and gas resources; data corruption or operational disruption of production-related infrastructure that could result in a loss of production, or accidental discharge; disruption of our operations, communications, or processing of transactions or the loss of, or damage to, sensitive information, facilities, infrastructure and systems; cyber-attacks on a service provider that could result in supply chain disruptions, which could delay or halt … [S54]

Navigation sector: **energy**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-03-26, L781:

> Our pricing policy for fuels takes into account several factors such as international and local crude oil prices, international prices of refined products, processing and distribution costs, biofuel prices, exchange rate volatility, local demand and supply, competition, inventories, export duties, local taxation, domestic margins for our products, among others. Our expectation is to align, over time, our local prices with those of international markets, while seeking to maintain a reasonable relationship between local prices of crude oil and fuels, without considering short-term fluctuations; however, we cannot assure you that other critical factors that are also considered in our pricing policy (including, but not limited to, changes in the exchange rate, or in international prices or potential legal or regulatory limitations, or other limitations that affect the ability of markets to deal with price changes), will not have an adverse impact on our ability to maintain such relation, while volatility and uncertainty in the international prices of crude oil and its derivatives, fluctuations in the value of the Argentine peso, will likely persist as they remain strongly influenced by conditions and expectations of world supply, demand and geopolitical tensions, among other factors, also potentially having an adverse effect on our export revenues. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-03-26, L8046:

> In 2025, 89% of our production of natural gas came from the Neuquina basin. We believe that natural gas from this basin offers a competitive advantage in terms of cost-competitive reserves and resources compared to natural gas from other regions. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-03-26, L847:

> The oil and gas industry is competitive and our ability to achieve our strategic objectives and expand our business depends on our ability to successfully compete in the market and react to competitive forces [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-03-26, L161:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-03-26, L525:

> This annual report, including any documents incorporated by reference, contains statements that we believe constitute forward-looking statements within the meaning of the Private Securities Litigation Reform Act of 1995. These forward-looking statements may include statements regarding the intent, belief or current expectations of us and our management, including statements with respect to trends affecting our financial condition, financial ratios, results of operations, business, strategy, geographic concentration, oil and gas reserves, future hydrocarbon production volumes and our ability to satisfy our long-term sales commitments from future supplies available to us, our ability to pay dividends in the future and to service our outstanding debt, dates or periods in which production is scheduled or expected to come on-stream, as well as our plans with respect to capital expenditures, business, strategy, geographic concentration, cost savings, discount rates, investments and dividends payout policies. These statements are not a guarantee of future performance and are subject to material risks, uncertainties, changes and other factors which may be beyond our control or may be difficult to predict. Accordingly, our future financial condition, prices, financial ratios, results of operations, business, strategy, geographic concentration, hydrocarbon production volumes, oil and … [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 3, 4, 6-K, 6-K/A, CORRESP, NT 20-F, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SD, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:30:15.069259+00:00.

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
| 2026-10-23 | 6-K | 0001554855-26-002169 | — | [S03] |
| 2026-10-14 | 6-K | 0001554855-26-002124 | — | [S04] |
| 2026-10-09 | 6-K | 0001554855-26-002090 | — | [S05] |
| 2026-10-09 | 6-K | 0001554855-26-002088 | — | [S06] |
| 2026-10-09 | 4 | 0001292814-26-004900 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0000904851.json) — published not supplied; retrieved 2026-10-24T13:22:51.759433+00:00.

[S03] [6-K 0001554855-26-002169](https://www.sec.gov/Archives/edgar/data/904851/000155485526002169/0001554855-26-002169-index.html) — published 2026-10-23; retrieved 2026-10-24T13:22:51.759433+00:00.

[S04] [6-K 0001554855-26-002124](https://www.sec.gov/Archives/edgar/data/904851/000155485526002124/0001554855-26-002124-index.html) — published 2026-10-14; retrieved 2026-10-24T13:22:51.759433+00:00.

[S05] [6-K 0001554855-26-002090](https://www.sec.gov/Archives/edgar/data/904851/000155485526002090/0001554855-26-002090-index.html) — published 2026-10-09; retrieved 2026-10-24T13:22:51.759433+00:00.

[S06] [6-K 0001554855-26-002088](https://www.sec.gov/Archives/edgar/data/904851/000155485526002088/0001554855-26-002088-index.html) — published 2026-10-09; retrieved 2026-10-24T13:22:51.759433+00:00.

[S07] [4 0001292814-26-004900](https://www.sec.gov/Archives/edgar/data/904851/000129281426004900/0001292814-26-004900-index.html) — published 2026-10-09; retrieved 2026-10-24T13:22:51.759433+00:00.

[S54] [20-F 0001193125-26-126363](https://www.sec.gov/Archives/edgar/data/904851/000119312526126363/d95578d20f.htm) — published 2026-03-26; retrieved 2026-11-02T22:08:05.644053+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/ef36a46d682e789d5949ebe61d4ec5a6bea5f3de/brain/companies/YPF/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
