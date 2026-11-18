---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001214816
cik: 0001214816
company_name: AXIS CAPITAL HOLDINGS LTD
tickers:
- AXS
- AXS$E
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
  reason: latest_filing_incomplete
  next_action: Resolve the latest financial filing/CompanyFacts mismatch; any historical
    bootstrap must keep the latest-period gap explicit.
  observed_forms:
  - 10-K
  - 10-Q
  - 13F-HR
  - '144'
  - 25-NSE
  - '3'
  - '4'
  - 4/A
  - 424B2
  - 424B3
  - 424B5
  - '425'
  - 8-A12B
  - 8-K
  - 8-K/A
  - ARS
  - CERTNYS
  - CORRESP
  - DEF 14A
  - DEFA14A
  - EFFECT
  - FWP
  - IRANNOTICE
  - RW
  - S-3ASR
  - S-4
  - S-4/A
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
    url: https://data.sec.gov/submissions/CIK0001214816.json
    sha256: 24d7e693d908cb0f2057501ae6748e295d23095961489a93ea72feca8bfaa56a
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001214816.json
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
  url: https://data.sec.gov/submissions/CIK0001214816.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 24d7e693d908cb0f2057501ae6748e295d23095961489a93ea72feca8bfaa56a
- id: S03
  title: 13F-HR 0001214816-26-000205
  url: https://www.sec.gov/Archives/edgar/data/1214816/000121481626000205/0001214816-26-000205-index.html
  published_at: '2026-07-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: IRANNOTICE 0001214816-26-000204
  url: https://www.sec.gov/Archives/edgar/data/1214816/000121481626000204/0001214816-26-000204-index.html
  published_at: '2026-07-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001214816-26-000203
  url: https://www.sec.gov/Archives/edgar/data/1214816/000121481626000203/0001214816-26-000203-index.html
  published_at: '2026-07-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 8-K 0001214816-26-000201
  url: https://www.sec.gov/Archives/edgar/data/1214816/000121481626000201/0001214816-26-000201-index.html
  published_at: '2026-07-28'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: SCHEDULE 13G 0000354204-26-000772
  url: https://www.sec.gov/Archives/edgar/data/1214816/000035420426000772/0000354204-26-000772-index.html
  published_at: '2026-07-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1214816/000121481626000203/axs-20260630.htm
  title: 10-Q 0001214816-26-000203
  published_at: '2026-07-28'
  retrieved_at: '2026-11-18T21:05:08.148225+00:00'
  sha256: eba29bb6a0f7d0432ed6f1b78d7486c045c4bef0365969e47606fb260c3691e9
- id: S55
  url: https://www.sec.gov/Archives/edgar/data/1214816/000121481626000149/axs-20260401.htm
  title: DEF 14A 0001214816-26-000149
  published_at: '2026-04-02'
  retrieved_at: '2026-11-18T21:05:05.202594+00:00'
  sha256: fe0cb49fe3e2529647bbfe7e3679ebd66affe56e7644b3c7c3b1a060f9f00f26
issuer_classification:
  cik: 0001214816
  classification_status: reported_sic
  entity_type: operating
  name: AXIS CAPITAL HOLDINGS LTD
  sic: '6331'
  sic_description: Fire, Marine & Casualty Insurance
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 24d7e693d908cb0f2057501ae6748e295d23095961489a93ea72feca8bfaa56a
  url: https://data.sec.gov/submissions/CIK0001214816.json
listings:
- ticker: AXS
  exchange: NYSE
  instrument_type: common_stock
- ticker: AXS$E
  exchange: NYSE
  instrument_type: preferred
research_filings:
- accession: 0001214816-26-000097
  filed: '2026-02-27'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1214816/000121481626000097/0001214816-26-000097-index.html
- accession: 0001214816-26-000203
  filed: '2026-07-28'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1214816/000121481626000203/0001214816-26-000203-index.html
- accession: 0001214816-26-000149
  filed: '2026-04-02'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1214816/000121481626000149/0001214816-26-000149-index.html
- accession: 0001214816-26-000201
  filed: '2026-07-28'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1214816/000121481626000201/0001214816-26-000201-index.html
- accession: 0001104659-25-011171
  filed: '2025-02-11'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1214816/000110465925011171/0001104659-25-011171-index.html
- accession: 0001214816-23-000039
  filed: '2023-04-14'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1214816/000121481623000039/0001214816-23-000039-index.html
- accession: 0001104659-23-007556
  filed: '2023-01-27'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1214816/000110465923007556/0001104659-23-007556-index.html
- accession: 0001193125-22-128062
  filed: '2022-04-29'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1214816/000119312522128062/0001193125-22-128062-index.html
- accession: 0001193125-17-369532
  filed: '2017-12-14'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1214816/000119312517369532/0001193125-17-369532-index.html
research_progress:
  stage: evidence_collected
  input_sha256: db75302bedb7289d15aaaab79bb7fb2ee44c2f104681b2dee90c41680f7e8fae
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
  sic: '6331'
  sic_description: Fire, Marine & Casualty Insurance
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001214816.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AXS/README.md
full_history_commit: b9d67ef2f16565081e0df464efbaff4348778881
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AXS, AXS$E — AXIS CAPITAL HOLDINGS LTD

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AXS/README.md)

## Business overview

Reported issuer name: **AXIS CAPITAL HOLDINGS LTD**. Stable SEC CIK: **0001214816**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AXS | NYSE | common_stock | 1 | [S01] |
| AXS$E | NYSE | preferred | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 10-Q, filed 2026-07-28, L110:

> Forward-looking statements made in this report, such as those related to our performance, pricing, growth prospects, fee income, the outcome of our strategic initiatives, our expectations relating to our ability to successfully implement and manage technology initiatives – including artificial intelligence, our expectations about the current trade and geopolitical environment on our business, economic and market conditions, and other statements that are not historical facts, reflect our current views with respect to future events and financial performance and are made pursuant to the safe harbor provisions of the Private Securities Litigation Reform Act of 1995. [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

Source excerpt — 10-Q, filed 2026-07-28, L584:

> The Company's underwriting operations are organized around its global underwriting platforms, AXIS Insurance and AXIS Re. The Company has determined that it has two reportable segments, insurance and reinsurance. [S54]

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

Source excerpt — 10-Q, filed 2026-07-28, L2253:

> •leveraging our global platform to introduce our products and services to new regions including the continued expansion of our North America product capabilities; [S54]

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

Source excerpt — 10-Q, filed 2026-07-28, L2256:

> •investing in data and technology, together with AI capabilities and tools, to enhance productivity, empower our teammates and enhance the service that we provide to our customers; [S54]

## Industry and value chain

SEC-reported SIC **6331**: Fire, Marine & Casualty Insurance. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — DEF 14A, filed 2026-04-02, L1096:

> •Held executive leadership and management roles at Verizon over the course of his 33-year tenure in the areas of digital technology and platforms, cybersecurity, supply chain management, sales, marketing, and operations, including President of Verizon Global Wholesale Group, President of Verizon Digital Media Service, Area President of Verizon Midwest Region, and Senior Vice President of Verizon Enterprise Operations. [S55]

Navigation sector: **financials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 10-Q, filed 2026-07-28, L113:

> Strategic Risk: industry competition and consolidation; failure to keep the pace or manage technology developments, including artificial intelligence; general economic, capital, and credit market conditions, including market illiquidity, fluctuations in interest rates, credit spreads, equity securities' prices, foreign currency exchange rates, and evolving impacts of tariffs, sanctions, and international trade tensions; our ability to increase the use of data and analytics, and technology as part of our business strategy and adapt to new technologies; changes in the political environment of certain countries where we operate or underwrite business; loss of business provided to us by major brokers; rating agency actions; key personnel changes; potential strategic opportunities including acquisitions and our ability to achieve them; evolving expectations regarding environmental, social, and governance matters; and the effect of contagious diseases on our business. [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — DEF 14A, filed 2026-04-02, L3263:

> We provide our NEOs with benefits and severance payments if we terminate them without cause and if they terminate their employment for good reason. These benefits add a level of security to each NEO’s position. We believe these benefits are needed to attract and retain talented executives. These provisions encourage individuals to move from other firms and help attract individuals new to our industry, which is generally more volatile. In addition, we face significant competition within our industry for experienced leaders, and we believe these benefits are needed to remain competitive as an employer as it is a common feature in many of our competitors’ compensation programs. Furthermore, we provide these benefits in part so that we can obtain valuable agreements from the NEOs to assign to us certain intellectual property rights and maintain the confidentiality of our information, and not to compete with us or solicit our teammates or customers for a certain period of time after leaving. Moreover, providing payments upon termination allows us to obtain a release of claims from the NEO upon the NEO's departure from AXIS, which we consider a valuable benefit to us. [S55]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 10-Q, filed 2026-07-28, L2262:

> AXIS is executing with clarity and conviction in our strategy to be a leading global specialty underwriter, delivering durable, profitable growth across market cycles. Our differentiated market positioning – anchored by a diversified specialty portfolio, deep underwriting expertise, a global operating platform, strong claims and risk management capabilities, and global multivariate distribution model – provides a powerful foundation for continued value creation. This is reinforced by a conservative, high‑quality investment portfolio that enhances earnings resilience and capital flexibility. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 10-Q, filed 2026-07-28, L1993:

> On September 17, 2025, the Company's Board of Directors approved a new share repurchase program for up to $400 million of the Company's common shares. The new share repurchase program is open-ended, allowing the Company to repurchase its shares from time to time in the open market or privately negotiated transactions, depending on market conditions. At June 30, 2026, remaining authorization under this plan was exhausted. [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 10-Q, filed 2026-07-28, L119:

> Readers should carefully consider these risks alongside those detailed in Item 1A, 'Risk Factors' of our most recent Annual Report on Form 10-K filed with the Securities and Exchange Commission ("SEC"), and in subsequent filings available at www.sec.gov. [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.
- Forms observed in the retained filing inventory: 10-K, 10-Q, 13F-HR, 144, 25-NSE, 3, 4, 4/A, 424B2, 424B3, 424B5, 425, 8-A12B, 8-K, 8-K/A, ARS, CERTNYS, CORRESP, DEF 14A, DEFA14A, EFFECT, FWP, IRANNOTICE, RW, S-3ASR, S-4, S-4/A, S-8, SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D/A, SCHEDULE 13G, SCHEDULE 13G/A, UPLOAD
- Collector status: quality_review_required; last action: filings_only_financials_incomplete; last checked: 2026-10-24T13:32:10.780886+00:00.

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
| 2026-07-28 | 13F-HR | 0001214816-26-000205 | — | [S03] |
| 2026-07-28 | IRANNOTICE | 0001214816-26-000204 | — | [S04] |
| 2026-07-28 | 10-Q | 0001214816-26-000203 | — | [S05] |
| 2026-07-28 | 8-K | 0001214816-26-000201 | — | [S06] |
| 2026-07-14 | SCHEDULE 13G | 0000354204-26-000772 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001214816.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [13F-HR 0001214816-26-000205](https://www.sec.gov/Archives/edgar/data/1214816/000121481626000205/0001214816-26-000205-index.html) — published 2026-07-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [IRANNOTICE 0001214816-26-000204](https://www.sec.gov/Archives/edgar/data/1214816/000121481626000204/0001214816-26-000204-index.html) — published 2026-07-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [10-Q 0001214816-26-000203](https://www.sec.gov/Archives/edgar/data/1214816/000121481626000203/0001214816-26-000203-index.html) — published 2026-07-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [8-K 0001214816-26-000201](https://www.sec.gov/Archives/edgar/data/1214816/000121481626000201/0001214816-26-000201-index.html) — published 2026-07-28; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [SCHEDULE 13G 0000354204-26-000772](https://www.sec.gov/Archives/edgar/data/1214816/000035420426000772/0000354204-26-000772-index.html) — published 2026-07-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [10-Q 0001214816-26-000203](https://www.sec.gov/Archives/edgar/data/1214816/000121481626000203/axs-20260630.htm) — published 2026-07-28; retrieved 2026-11-18T21:05:08.148225+00:00.

[S55] [DEF 14A 0001214816-26-000149](https://www.sec.gov/Archives/edgar/data/1214816/000121481626000149/axs-20260401.htm) — published 2026-04-02; retrieved 2026-11-18T21:05:05.202594+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/b9d67ef2f16565081e0df464efbaff4348778881/brain/companies/AXS/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
