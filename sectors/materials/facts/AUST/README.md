---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001817740
cik: 0001817740
company_name: Austin Gold Corp.
tickers:
- AUST
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
  - 20-F
  - 424B3
  - 424B4
  - 6-K
  - 8-A12B
  - CERT
  - CORRESP
  - D
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - F-3
  - S-1
  - S-1/A
  - S-8
  - SC 13D
  - SCHEDULE 13D/A
  - UPLOAD
input_sources:
  submissions:
    url: https://data.sec.gov/submissions/CIK0001817740.json
    sha256: ac29b3088740739a2afb5e38c07f7b0423d7c427a5ffb1138ca364b599aa07d0
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001817740.json
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
  url: https://data.sec.gov/submissions/CIK0001817740.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ac29b3088740739a2afb5e38c07f7b0423d7c427a5ffb1138ca364b599aa07d0
- id: S03
  title: 6-K 0001104659-26-091322
  url: https://www.sec.gov/Archives/edgar/data/1817740/000110465926091322/0001104659-26-091322-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S04
  title: EFFECT 9999999995-26-002223
  url: https://www.sec.gov/Archives/edgar/data/1817740/999999999526002223/9999999995-26-002223-index.html
  published_at: '2026-07-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S05
  title: F-3 0001104659-26-076502
  url: https://www.sec.gov/Archives/edgar/data/1817740/000110465926076502/0001104659-26-076502-index.html
  published_at: '2026-06-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S06
  title: 6-K 0001062993-26-003170
  url: https://www.sec.gov/Archives/edgar/data/1817740/000106299326003170/0001062993-26-003170-index.html
  published_at: '2026-06-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S07
  title: 6-K 0001062993-26-002969
  url: https://www.sec.gov/Archives/edgar/data/1817740/000106299326002969/0001062993-26-002969-index.html
  published_at: '2026-06-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  url: https://www.sec.gov/Archives/edgar/data/1817740/000110465926035225/aust-20251231x20f.htm
  title: 20-F 0001104659-26-035225
  published_at: '2026-03-26'
  retrieved_at: '2026-11-17T21:33:08.519990+00:00'
  sha256: 59e45266f9931af44fb94bc499d500daf0d6064cd7969ea2e5c99fed03cc4a06
issuer_classification:
  cik: 0001817740
  classification_status: reported_sic
  entity_type: other
  name: Austin Gold Corp.
  sic: '1040'
  sic_description: Gold and Silver Ores
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: ac29b3088740739a2afb5e38c07f7b0423d7c427a5ffb1138ca364b599aa07d0
  url: https://data.sec.gov/submissions/CIK0001817740.json
listings:
- ticker: AUST
  exchange: NYSE_AMERICAN
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-035225
  filed: '2026-03-26'
  form: 20-F
  url: https://www.sec.gov/Archives/edgar/data/1817740/000110465926035225/0001104659-26-035225-index.html
- accession: 0001104659-26-091322
  filed: '2026-08-06'
  form: 6-K
  url: https://www.sec.gov/Archives/edgar/data/1817740/000110465926091322/0001104659-26-091322-index.html
research_progress:
  stage: evidence_collected
  input_sha256: 234608bcde3aa3ad59179322d850670d33ad3cbf8fabc1a98fc83c2ad501abb7
  last_attempt_at: '2026-11-17T21:29:10.535348+00:00'
  last_success_at: '2026-11-17T21:29:10.535348+00:00'
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
  sic: '1040'
  sic_description: Gold and Silver Ores
  rule_version: 1
  reason: Project navigation rules based on reported SEC SIC. These are provisional
    broad sector groupings, not licensed or official GICS classifications. Unlisted,
    mixed-activity, blank-check, investment-fund and ambiguous REIT codes require
    company-specific review.
  source_url: https://data.sec.gov/submissions/CIK0001817740.json
full_history_url: https://github.com/eladyesh/stock-brain/blob/4221fdf1cbfcbe1be4425ff7f3389bba890abacf/brain/companies/AUST/README.md
full_history_commit: 4221fdf1cbfcbe1be4425ff7f3389bba890abacf
view: latest_available_annual_quarterly_ttm_and_five_filings
---
# AUST — Austin Gold Corp.

> Automatically maintained factual profile. Research status: stub. Missing research is explicit.

[Sector index](../../INDEX.md) · [All sectors](../../../README.md) · [Full financial history](https://github.com/eladyesh/stock-brain/blob/4221fdf1cbfcbe1be4425ff7f3389bba890abacf/brain/companies/AUST/README.md)

## Business overview

Reported issuer name: **Austin Gold Corp.**. Stable SEC CIK: **0001817740**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| AUST | NYSE_AMERICAN | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

Source excerpt — 20-F, filed 2026-03-26, L616:

> We and our business are subject to material risks, which could cause actual results, performance and achievements to differ materially from those anticipated. Refer to the risk factors set forth in the section entitled “Risk Factors” in this Annual Report. These risks can be summarized as follows: [S54]

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1040**: Gold and Silver Ores. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

Source excerpt — 20-F, filed 2026-03-26, L865:

> Regulations and pending legislation governing issues involving climate change could result in increased operating costs, which could have a material adverse effect on our business. A number of governments or governmental bodies have introduced or are contemplating regulatory changes in response to climate and its potential impacts. Legislation and increased regulation regarding climate change could impose significant costs on us, our venture partners and our suppliers, including costs related to increased energy requirements, capital equipment, environmental monitoring and reporting and other costs to comply with such regulations. Any adopted climate change regulations could also negatively impact our ability to compete with companies situated in areas not subject to such regulations. Given the emotion, political significance and uncertainty around the impact of climate change and how it should be dealt with, we cannot predict how legislation and regulation will affect our financial condition, operating performance and ability to compete. Furthermore, even without such regulation, increased awareness and any adverse publicity in the global marketplace about potential impacts on climate change by us or other companies in the natural resources industry could harm our reputation. [S54]

Navigation sector: **materials**. Method: `project_sic_rule`. Project navigation rules based on reported SEC SIC. These are provisional broad sector groupings, not licensed or official GICS classifications. Unlisted, mixed-activity, blank-check, investment-fund and ambiguous REIT codes require company-specific review.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

Source excerpt — 20-F, filed 2026-03-26, L611:

> Shareholders, potential shareholders and other prospective investors should be aware that these statements are subject to known and unknown risks, uncertainties and other factors that could cause actual results to differ materially from those suggested by the forward - looking statements. Such factors include, but are not limited to: risks relating to estimates of mineral reserves proving to be inaccurate, fluctuations in the gold price, risks and hazards associated with the business of mineral exploration, development and mining (including environmental hazards, industrial accidents, unusual or unexpected geological or structural formations, pressures, power outages, explosions, landslides, cave - ins and flooding), risks relating to the credit worthiness or financial condition of suppliers, refiners and other parties with whom the Company does business; inadequate insurance, or inability to obtain insurance, to cover these risks and hazards, employee relations; relationships with and claims by local communities and indigenous populations; political risk; risks related to natural disasters, terrorism, civil unrest, public health concerns (including health epidemics or outbreaks of communicable diseases such as the coronavirus); availability and increasing costs associated with mining inputs and labor; the speculative nature of mineral exploration and development, including … [S54]

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

Source excerpt — 20-F, filed 2026-03-26, L911:

> AI systems may produce inaccurate, biased, or otherwise unreliable outputs and may present privacy, cybersecurity, intellectual property, and human rights risks. Our reliance on third-party AI providers may limit our visibility into training data, model design, and risk controls. Failure to manage these risks effectively, or to provide appropriate disclosure regarding our use of AI, could result in legal liability, reputational harm, regulatory investigations, or adverse impacts on our business, financial condition, and results of operations. [S54]

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

Source excerpt — 20-F, filed 2026-03-26, L685:

> We may be subject to currency rate risk. Our reporting currency is the USD, which is exposed to fluctuations against other currencies. Our properties are located in the USA with corporate operations in Canada. Should we expand our operations into other countries, our expenditures and obligations may be incurred in foreign currencies. As such, our results of operations may become subject to foreign currency fluctuation risks and such fluctuations may adversely affect the financial position and our operating results. At this time, we have not implemented measures to mitigate transactional volatility in the CAD. We may, however, enter into foreign currency forward contracts in order to match or partially offset existing currency exposures. [S54]

## Financial performance

Not available: substantive research has not been completed. Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.

## Balance sheet and capital allocation

Not available: substantive research has not been completed. Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

Source excerpt — 20-F, filed 2026-03-26, L119:

> Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ [S54]

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

Source excerpt — 20-F, filed 2026-03-26, L616:

> We and our business are subject to material risks, which could cause actual results, performance and achievements to differ materially from those anticipated. Refer to the risk factors set forth in the section entitled “Risk Factors” in this Annual Report. These risks can be summarized as follows: [S54]

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- The navigation assignment below does not establish domicile, a verified GICS sector or completed qualitative research.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- No validated normalized financial history is available. Foreign forms, missing CompanyFacts accessions and quality failures require separate work; this is not zero revenue.
- Next collection task: Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.
- Forms observed in the retained filing inventory: 20-F, 424B3, 424B4, 6-K, 8-A12B, CERT, CORRESP, D, DRS, DRS/A, DRSLTR, EFFECT, F-3, S-1, S-1/A, S-8, SC 13D, SCHEDULE 13D/A, UPLOAD
- Collector status: quality_review_required; last action: no_supported_filing; last checked: 2026-10-24T13:35:48.699166+00:00.

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
| 2026-08-06 | 6-K | 0001104659-26-091322 | — | [S03] |
| 2026-07-08 | EFFECT | 9999999995-26-002223 | — | [S04] |
| 2026-06-23 | F-3 | 0001104659-26-076502 | — | [S05] |
| 2026-06-12 | 6-K | 0001062993-26-003170 | — | [S06] |
| 2026-06-02 | 6-K | 0001062993-26-002969 | — | [S07] |

## Sources and change log

[S01] [otherlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt) — published not supplied; retrieved 2026-11-01T16:07:03.340031+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001817740.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [6-K 0001104659-26-091322](https://www.sec.gov/Archives/edgar/data/1817740/000110465926091322/0001104659-26-091322-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S04] [EFFECT 9999999995-26-002223](https://www.sec.gov/Archives/edgar/data/1817740/999999999526002223/9999999995-26-002223-index.html) — published 2026-07-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S05] [F-3 0001104659-26-076502](https://www.sec.gov/Archives/edgar/data/1817740/000110465926076502/0001104659-26-076502-index.html) — published 2026-06-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S06] [6-K 0001062993-26-003170](https://www.sec.gov/Archives/edgar/data/1817740/000106299326003170/0001062993-26-003170-index.html) — published 2026-06-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S07] [6-K 0001062993-26-002969](https://www.sec.gov/Archives/edgar/data/1817740/000106299326002969/0001062993-26-002969-index.html) — published 2026-06-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [20-F 0001104659-26-035225](https://www.sec.gov/Archives/edgar/data/1817740/000110465926035225/aust-20251231x20f.htm) — published 2026-03-26; retrieved 2026-11-17T21:33:08.519990+00:00.

Source release: `coverage-20261101-41324509967-1`. [Complete financial history and original evidence hashes](https://github.com/eladyesh/stock-brain/blob/4221fdf1cbfcbe1be4425ff7f3389bba890abacf/brain/companies/AUST/README.md).

Changes remain in main Git history. This generated factual profile does not promote or replace curated research.
