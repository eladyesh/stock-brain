# Independent reference-packet evidence audit

Audit date and evidence cutoff: **2026-10-18**. Reviewer: independent reference-evidence audit agent. Scope: the three intended reference packets, [MSFT](../pilot/MSFT.json), [MU](../pilot/MU.json), and [AVAV](../pilot/AVAV.json). This is a dated research-content audit, not an audit opinion on the issuers' financial statements or an investment recommendation.

The reviewer read `AGENTS.md` and `docs/EVIDENCE_PACKET.md`, every claim and metric in the three packets, and the supporting primary-source passages. This review is independent of the packet authors' notes and structural validation. Most source reading used the actual documents downloaded in this session under ignored `build/research-cache/software/`, `semiconductors/`, and `defense/`; collection manifests map those files to the packets' SEC/issuer URLs. The Microsoft investor-relations homepage was also opened directly on the audit date to verify its upcoming-earnings date.

## Disposition and corrections

| Packet | Content disposition | Covered financial period | Limit on the conclusion |
| --- | --- | --- | --- |
| MSFT | Suitable as a reviewed dated research snapshot after the two confirmed wording corrections below. | FY2026 ended June 30, 2026, with September segment/dividend developments and an October earnings-calendar check. | Does not provide current valuation, full segment-recast history, or an exhaustive intervening-event review. |
| MU | Suitable as a reviewed dated research snapshot after the confirmed C03 correction below. | Fiscal Q4 and FY2026 ended September 3, 2026; 10-K filed October 9. | Unusually strong results are reported results, not normalized earnings or evidence that cyclicality has ended. |
| AVAV | Suitable as a reviewed dated research snapshot; no required material content correction found. | Fiscal Q1 2027 ended August 1, 2026, with September meeting disclosures. | Filings-first coverage; valuation, exhaustive contract announcements, and an organic-growth reconciliation remain outside scope. |

Corrections raised directly with the packet authors:

1. **MU C03, resolved and reread:** the March announcement explicitly says HBM4 volume shipments, while SOCAMM2 and the 9650 SSD are described as being in high-volume production. The original sentence called all three shipments. The revised sentence preserves the production/shipment distinction. No numerical metric changed.
2. **MSFT C03, resolved and reread:** replaced the broad description of Devices and Consumer as containing the consumer-facing businesses with its explicit Windows, Xbox, and search/advertising components. S04 also places Microsoft 365 consumer cloud/products in Agents and Infra, so an all-consumer interpretation would be wrong.
3. **MSFT C08, resolved and reread:** now specifies **Microsoft 365 Commercial cloud** when attributing growth to premium offerings and paid-seat additions. The July call's relevant paragraph concerns M365, while the broader Microsoft Cloud metric also includes Azure.

All other material claims were either supported by the read primary sources, explicitly identified as management outlook, or presented as bounded interpretation. Unsupported current prices, consensus forecasts, price targets, or market-share rankings have not been filled in. The review does not establish that missing information is unavailable in general; it establishes that it has not been researched for these packets.

## Microsoft: claim and source checks

Source IDs below are those in the MSFT packet. Read S01 (FY2026 10-K), S02 (July 29 earnings release), S03 (July 29 earnings call), S04 (September segment presentation), S05 (September 15 dividend announcement), S07 (August 2024 Palantir announcement), and S08 (September 2 8-K) from their cached primary documents. S06 is the issuer's live investor-relations homepage, read on October 18; its upcoming-earnings panel and next-release answer both gave October 28, 2026.

| Claims | Checks performed and result |
| --- | --- |
| C01 | S01 cover and Item 1 confirm MSFT/Nasdaq, software/services, devices, gaming, advertising, and cloud. Its business and distribution descriptions support the subscription, consumption, license, hardware, and service revenue summary. |
| C02–C03 | S04 explicitly transitions the three FY2026 segments to Agents and Infra and Devices and Consumer starting FY2027; S08 confirms the effective reporting year. S04 places Microsoft 365 and GitHub with Azure and narrows Azure's consumption-based definition. Historical financials and metrics are recast in the presentation. C03's consumer-scope wording correction is recorded above. |
| C04 | S01 Item 1, Distribution, Sales, and Marketing explicitly describes direct enterprise/public-sector sales, partners, OEM preinstallation, and online purchasing/marketplaces. Operating-segment descriptions support the distinct end-market exposures. |
| C05 | S03 Nadella's infrastructure remarks describe Maia and Cobalt alongside NVIDIA and AMD. The same remarks discuss new capacity and faster deployment; Hood says demand exceeds capacity and incremental capacity was quickly monetized. The capacity/utilization conclusion is appropriately interpretive. |
| C06 | S01's Competition paragraphs distinguish Office's established/AI-first competitors, Dynamics' cloud/on-premises competitors, and Azure's competing services. No unverified ranking or share was inferred. |
| C07 | S04's integrated applications/agents/infrastructure description and S01's identity/security portfolio and distribution support the proposed integration/switching-cost mechanism. The packet labels this as interpretation and limits the claim about durable pricing power. |
| C08 | S03's M365 results paragraph attributes ARPU growth to premium offerings and describes paid-seat expansion; the Azure paragraph separately addresses capacity and consumption. The M365-specific wording correction is recorded above. Continued adoption/capacity requirements are interpretation. |
| C09 | Read the S02 twelve-month income-statement columns and the GAAP/OpenAI reconciliation. All reported annual figures match; the packet uses GAAP net income/EPS rather than the lower OpenAI-adjusted amounts. |
| C10 | Read S02 balance sheet and twelve-month cash-flow columns. Cash and short-term investments are a combined total; cash additions to PP&E are a cash-outflow magnitude. S03 separately discusses finance leases and cash PP&E spending, supporting the caution that cash capex alone omits noncash lease additions. |
| C11 | S05 names Nadella as chairman/CEO, Hood as CFO, and Peterson as lead independent director. The board-oversight statement is interpretation; a full compensation review is explicitly outstanding. |
| C12 | S06 directly confirms October 28, 2026 for FY27 Q1 earnings. S08 and S04 confirm FY27 reporting under the new structure. The expected analytical test is interpretation, not a prediction of the result. |
| C13–C14 | S01 Item 1A discusses competition, cyberattacks, infrastructure/capacity, regulation, AI investment and monetization risks. S03 discusses capex, leases, cash flows, and FY27 assumptions. The bull/base/bear text has no unsupported probabilities or valuation targets. |
| C15 | S07 confirms the August 8, 2024 Microsoft/Palantir integration across Azure government/classified environments and Palantir platforms. It conditions availability on authorization/accreditation. The packet retains that condition and makes no exclusivity assertion. |
| C16 | S08 confirms the September 2 announcement. S05 confirms the September 15 dividend declaration, December 10 payment date and November 19 record date. The future payment is correctly labeled declared, not paid. |

| Metrics | Independently checked value and basis |
| --- | --- |
| M01–M05 | FY2026 GAAP revenue **USD 331,839m**, operating income **155,237m**, net income **133,749m**, diluted EPS **USD 17.95**; FY2025 revenue **USD 281,724m**. Annual periods July 1–June 30, as stated in the packet, align with the release columns. |
| M06 | June 30, 2026 cash/equivalents/short-term investments **USD 76,843m**; balance-sheet point-in-time metric. |
| M07–M08 | FY2026 operating cash flow **USD 182,935m**; cash PP&E additions **USD 115,948m** outflow magnitude. Not total capex including leases. |
| M09 | **USD 0.98/share**, declared September 15 for payment December 10, 2026. `kind: declared` prevents treating the future payment date as an actual cash payment. |

The September recast was read but its full numeric history is not entered into the packet. July segment-specific guidance should not be used as unchanged, current-comparable guidance after that recast. The packet explicitly records this limitation.

## Micron: claim and source checks

Read S01 (FY2026 10-K filed October 9), S02 (September 30 release), S03 (September 30 prepared remarks PDF text), and S04 (March 16 product release). The unusually large annual results were compared between the release and the filed 10-K rather than rejected or normalized based on prior expectations.

| Claims | Checks performed and result |
| --- | --- |
| C01 | S01 Item 1, Overview and Product Technologies, confirms DRAM, NAND, NOR, owned manufacturing, components/integrated solutions, and the described end markets. |
| C02 | S01 Products by Business Unit and Market confirms the four units. Cloud Memory includes hyperscaler memory and all data-center HBM; Core Data Center includes all data-center storage plus specified memory markets. |
| C03 | S04 directly supports HBM4 volume shipments and SOCAMM2/9650 high-volume production. The reviewed correction preserves the difference. Product descriptions support accelerator bandwidth, CPU memory and storage-access distinctions. Footnotes show issuer/internal test bases; the packet asserts no independent benchmark win. |
| C04 | S01 Marketing and Customers states short-term contracts and multi-year take-or-pay commitments, fixed/periodically negotiated prices and price bands, with payments generally shortly after delivery. The packet does not treat all contracts as having price floors. |
| C05 | S03 Manufacturing expansions and Market outlook describe cleanroom requirements, gradual ramps and supply constraints expected through calendar 2028. This is correctly categorized as management guidance. |
| C06 | S01 Competitive Conditions names Samsung, SK hynix, Kioxia, Sandisk, CXMT and YMTC, and discusses pricing, technology, capacity and supply competition. |
| C07 | S04 describes joint engineering with NVIDIA and integration into specified platforms. The switching/substitution mechanism is interpretation and does not assert permanent exclusivity or superior margins. |
| C08 | S03 Data center connects model size, context length and concurrency to memory/storage requirements and discusses SSDs for KV-cache offload. The claim preserves management attribution and execution dependence. |
| C09 | Read S02's separate quarterly and annual GAAP tables and dates. Cross-checked annual revenue/net income with S01's audited annual statement. S01 Definitions confirms that FY2026 contains 53 weeks. |
| C10 | S02 balance-sheet amounts agree with S01. S01 Note 1 and Note 16 explain customer deposits/contract liabilities and recognition conditions. Cash/equivalents are not mislabeled as cash plus investments. |
| C11 | S01 Information About Our Executive Officers explicitly dates the information October 9 and identifies Mehrotra as chairman/CEO, Murphy as CFO and Bhatia as president/COO. The packet does not substitute an old executive title or claim a completed proxy review. |
| C12 | S03 Manufacturing expansions states Singapore HBM advanced-packaging initial output in early calendar 2027 and Idaho ID1 wafer output in mid-calendar 2027. It also states new production takes time to ramp. The packet treats these as changeable targets, not completed output/full capacity. |
| C13–C14 | S01 Competition/Risk Factors supports pricing, supply, trade and qualification risks. S03 supports the demand/capacity mechanisms used in clearly labeled scenarios. No scenario is presented as a sourced earnings forecast. |
| C15 | S04 identifies HBM4 and SOCAMM2 designed for Vera Rubin and the 9650 optimized for BlueField-4 STX. This supports a platform/supply-chain relationship; no GPU-competition or exclusive-supplier inference is made. |
| C16–C17 | S02 Product Highlights reports server-RDIMM sampling/qualification and SSD uses. The distinction between product milestones and recognized sales is appropriate; it does not negate the separately reported shipments in the source. |

| Metrics | Independently checked value and basis |
| --- | --- |
| M01–M03 | FQ4 ended September 3, 2026: GAAP revenue **USD 54,229m**, net income **USD 37,701m**, gross margin **86.8%**. The source's non-GAAP gross margin is different and was not substituted. |
| M04–M05 | FY2026: GAAP revenue **USD 133,188m**, net income **USD 84,969m**; both match the filed annual statement. |
| M06–M08 | September 3 balance sheet: cash/equivalents **USD 38,364m**, current debt **USD 491m**, long-term debt **USD 4,688m**. All match both S02 and S01. |

Quarterly start May 29 follows the preceding May 28 quarter-end; annual start August 29, 2025 follows the prior August 28 fiscal year-end. The 53-week year has not been silently treated as a standard calendar year. The cash-deposit and high-margin context warrants normalization work later, but does not invalidate the sourced reported amounts.

## AeroVironment: claim and source checks

Read S01 (FY2026 10-K), S02 (August 1 quarter's 10-Q), S03 (September 9 release), S04 (September 30 voting-results 8-K), and S05 (August 14 proxy). Dollar statements in thousands were converted to millions without dropping the loss signs.

| Claims | Checks performed and result |
| --- | --- |
| C01–C02 | S02 Note 1 describes autonomous systems, precision strike, counter-UAS, space, directed energy and cyber/electronic warfare. S01 Item 7 and S02 Note 1 confirm AxS/SCDE and the hardware, support/development/mission-service contract model. |
| C03 | S01 Item 1 identifies Puma/JUMP UAS, Switchblade loitering munitions, Titan counter-UAS systems and LOCUST laser systems. The packet does not treat their capabilities as interchangeable or independently establish performance leadership. |
| C04 | S01 Customers names military services, intelligence agencies, allied buyers and subcontractors; it explicitly explains Army contracting on behalf of other DoD organizations. The buyer/end-user distinction is supported. |
| C05 | S01 Manufacturing and Operations describes design, suppliers, assembly, integration, testing and field support. Seasonality discusses awards, funding, manufacturing lead times and acceptance; adjacent supplier disclosures discuss component constraints. |
| C06 | S01 Competition names Lockheed Martin/RTX in LMS and counter-UAS and Anduril/Elbit in precision-strike competition. This supports disclosed competitive overlaps, not market-share rankings. |
| C07 | S01 Technology/IP describes relevant capabilities and government rights to use or authorize others to use certain IP; Competition discusses rapid change. The potential repeat-procurement mechanism is explicitly interpretation. |
| C08 | S03 opening management remarks prioritize manufacturing capacity and supply-chain expansion. The packet labels this management guidance and does not turn the comment into an independent demand forecast. |
| C09 | S02 Item 2 attributes lower Switchblade revenue to order delays and lower SCDE revenue to the terminated SCAR program and reduced Cyber and Mission Solutions contract scope. Consolidated growth is not generalized to every business. |
| C10–C12 | Read S03 quarterly statements and non-GAAP reconciliation. GAAP loss, adjusted EBITDA and adjusted EPS remain distinct. Independently calculated revenue growth from the two reported revenue figures; the result rounds to 5.68%. S02 supports acquisition contributions and uneven product trends. |
| C13–C14 | S02 balance sheet, Note 9 and cash-flow statement confirm cash, short-term investments, debt carrying value and operating cash flow. Working-capital rows show cash uses from inventory and unbilled-receivable increases. Positive operating cash flow is not equated with free cash flow. |
| C15 | S05 Executive Officers gives information as of August 14 and names Nawabi and Woodward in the stated roles. S03 September call-host paragraph confirms them. S04 confirms September 24 director elections and advisory compensation approval. |
| C16 | S03 describes substantial acquisition-related amortization/purchase-accounting expense and reconciles adjusted results. The valuation paragraph is interpretive and supplies no unsourced market valuation. |
| C17 | S03 states that the company continues its FY2027 outlook. S02 Fiscal Periods specifies April 30, 2027 year-end. The packet does not invent a next-release date or treat the outlook as actual results. |
| C18 | S01 Item 1A/goodwill discussion explicitly states the SCAR agreement's March 2026 termination for convenience. S02 Item 4 describes continuing BlueHalo IT-control and goodwill-review material weaknesses and ongoing remediation. Part II Item 1 details securities/derivative allegations; the packet makes no liability finding. |
| C19 | S02 results and control disclosures support the monitoring questions about deliveries, organic growth, cash conversion and remediation. These are assumptions/questions rather than issuer forecasts. |
| C20 | S02 Note 15 confirms BlueHalo closed May 1, 2025 and ESAero March 16, 2026. These are acquisitions/ownership relations; shared themes alone are not commercial relationships. |
| C21 | S04's September 30 filing describes the September 24 meeting. The packet keeps event date distinct from filing date and discloses non-exhaustive news coverage. |

| Metrics | Independently checked value and basis |
| --- | --- |
| M01–M04 | May 1–August 1, 2026 GAAP revenue **USD 480.490m**, prior fiscal Q1 revenue **USD 454.676m** for the quarter ended August 2, 2025, net loss **USD 5.066m**, diluted loss **USD 0.10/share**. Negative signs are retained in numeric fields. |
| M05–M06 | Same current quarter: company-defined non-GAAP adjusted EBITDA **USD 53.4m**, adjusted diluted EPS **USD 0.59**. Not GAAP profit or operating cash flow. |
| M07 | `(480.490 / 454.676 - 1) * 100 = 5.6774494365%`, matching narrative **5.68%**. Numeric inputs share units/currency/basis and use comparable fiscal-quarter endpoints. |
| M08–M10 | August 1, 2026: cash/equivalents **USD 278.390m**, short-term investments **USD 301.837m**, long-term debt carrying value **USD 730.057m**. Not face value or a complete enterprise-value bridge. |
| M11 | Current fiscal Q1 GAAP operating cash inflow **USD 13.496m**, directly from S02. |

## Scope limits and review binding

- The cached SEC submissions inventories were inspected for the recent core filings. They show MSFT's July 29 10-K and September 2 segment 8-K; MU's September 30 results 8-K and October 9 10-K; and AVAV's September 9 results, September 10 10-Q and September 30 meeting 8-K. This inventory check does not establish exhaustive news, legal, insider-trading or contract-award coverage.
- An issuer source substantiates what the issuer reported; it does not independently validate issuer product superiority, future capacity, customer demand or management forecasts. These distinctions are preserved in the packets.
- Current market valuations, normalized-cycle forecasts, detailed debt schedules, independent product benchmarks, comprehensive compensation analysis and detailed customer concentration remain limited as expressly disclosed in the packets. Their absence should not be converted into an invented zero or an unqualified conclusion.
- The three reference packets are short research snapshots, not complete company models. A later earnings release, revised segment presentation, acquisition, control-remediation disclosure or other material event requires a fresh review of affected claims.
- Final packet hashes and correction status are recorded below. The pipeline's per-company review record must separately bind the exact packet and rendered draft-body hashes; this Markdown audit alone must not override that gate.

All three requested precision corrections are resolved and were reread on disk. No unresolved material claim-support failure was found in the reviewed versions. Final packet SHA-256 values:

| Packet | SHA-256 |
| --- | --- |
| MSFT | `3ee790a4ccf36d6279e7c5775a8374c0178c046a6994ca195478fac71c1291a5` |
| MU | `80b9a14ba35d45c630613670f1c468fc00e571e93ea5fa540e0d5ea31a33aa2d` |
| AVAV | `2b78bc9f35d9e416c4328036bd589f972354a5ccc53190c3bbd3d371cb5af7d1` |

Any subsequent packet edit invalidates this version binding and requires the affected evidence checks to be refreshed. The audit covered **54 claims and 28 metrics** across the three packets.
