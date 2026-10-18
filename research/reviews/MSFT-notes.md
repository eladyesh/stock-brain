# MSFT pilot evidence review

Reviewed on 2026-10-18 by the AI research reviewer. This was a separate second pass after drafting, performed against downloaded primary-source text and issuer pages. It is an evidence review of this bounded pilot profile, not a claim of exhaustive investment diligence or human approval. The publishing pipeline must bind its machine review record to the exact rendered draft body and packet.

Packet SHA-256 at completion: `3ee790a4ccf36d6279e7c5775a8374c0178c046a6994ca195478fac71c1291a5`.

## Coverage and source handling

The SEC submissions index identifies Microsoft Corporation, CIK 0000789019, common-stock ticker MSFT on Nasdaq. The latest annual report available by the cutoff is the FY2026 Form 10-K filed July 29, 2026, covering the year ended June 30. The latest substantive 8-K in the reviewed index is September 2 and concerns segment reporting. Also read: July 29 earnings release and conference-call transcript; September segment presentation; September 15 dividend announcement; current issuer IR page listing October 28 earnings; and the historical Microsoft-Palantir joint announcement. Sources are dated individually in the packet. Full downloads and integrity hashes remain under ignored build/research-cache/software/.

The quarterly figures and guidance on the July call are older evidence than the September reporting redesign. The profile deliberately does not carry forward the old segment-specific guidance. It makes no claim that selected issuer news checks constitute a complete news/legal scan.

## Claim checks

| Claims | Evidence checked | Outcome |
| --- | --- | --- |
| C01 | FY2026 10-K cover; Item 1 General, products and distribution | Business lines, payment models and Nasdaq ticker supported. |
| C02–C03 | September 2 Exhibit 99.1, updated reporting and Segment Structure; corresponding 8-K Item 7.01 | Supported. Three segments describe FY2026; FY2027 uses Agents and Infra / Devices and Consumer. Azure is more narrowly consumption-based in the revised presentation. C03 specifies Windows, Xbox, and search/advertising to avoid implying that all consumer offerings are in Devices and Consumer. |
| C04 | 10-K Distribution, Sales, and Marketing; segment descriptions | Direct/partner/OEM/digital distribution supported. Demand exposures are descriptive, not market-size claims. |
| C05 | July call, Nadella infrastructure/silicon remarks | Maia, Cobalt, NVIDIA and AMD all present. Capacity-to-revenue relationship is explicitly interpretation, not a quantified forecast. |
| C06 | 10-K Competition subsections for Office, Dynamics and Azure | Supported at competitor-category level. No market shares or unsupported named competitor rankings. |
| C07 | September presentation and 10-K identity/security portfolio and distribution | Integration and switching-cost mechanism is explicitly interpretation. Added the annual-report reference on second pass because the September presentation does not itself mention identity. |
| C08 | July call, Hood commercial-cloud and Azure discussion | Premium products, paid-seat additions, usage and capacity discussion support the growth mechanism. C08 scopes the premium-product and seat attribution specifically to Microsoft 365 Commercial cloud. No forecast represented as actual revenue. |
| C09 | Earnings-release annual income statement cross-checked against the 10-K income statement | All five numerical entries agree; fiscal-year dates, USD millions and diluted per-share basis are correct. |
| C10 | Earnings-release balance sheet and cash-flow statement cross-checked against the 10-K; July call finance-lease discussion | Cash/investment balance, operating cash flow and cash PPE additions agree. PPE amount is presented as positive spending magnitude, not positive investing cash flow. |
| C11 | September 15 issuer announcement, named annual-meeting hosts | Nadella chair/CEO, Hood CFO, Peterson lead independent director supported as of that source date. Oversight statement is interpretation. Compensation/ownership review remains a gap. |
| C12 | Current issuer IR page and September 8-K | October 28 earnings date verified. FY2027 reporting change supports the expected first-quarter reporting context; no favorable result assumed. |
| C13–C14 | 10-K Item 1A and July call capex, margin/cash-flow and outlook discussion | Risk mechanisms supported; scenario statements remain explicitly assumptions without probabilities or price targets. |
| C15 | August 8, 2024 joint announcement | Partnership scope, classified environments and authorization condition supported. No exclusivity or completed-deployment claim. Historical NYSE reference in this source is not reused for current PLTR identity. |
| C16 | September 2 8-K and September 15 dividend announcement | Event dates, declaration, payment/record dates and per-share amount supported. Future payment is explicitly declared, not reported as paid. |

## Financial reconciliation

M01–M05: FY2026 revenue 331,839; operating income 155,237; net income 133,749; diluted EPS 17.95; FY2025 revenue 281,724. Monetary totals are USD millions; EPS is USD per share. These agree in both the SEC annual statement and earnings release.

M06–M08: June 30 cash/equivalents/short-term investments 76,843; FY2026 operating cash flow 182,935; FY2026 cash PPE additions 115,948, all USD millions. The last is the magnitude of a cash outflow and does not include all noncash leased-asset additions.

M09: USD 0.98 quarterly dividend declared September 15; scheduled payment December 10 and record date November 19. Metric kind is `declared`, and the forward payment date is not evidence that payment has occurred.

GAAP/non-GAAP distinction: the earnings release excludes OpenAI investment effects in its particular non-GAAP reconciliation; it does not describe a comprehensive normalization of all investment gains and restructuring items. The packet retains GAAP reported earnings and makes only that limited reconciliation statement. No analyst consensus, market price, forward multiple, or computed fair value was inserted.

## Conflicts resolved and remaining gaps

The main stale-data hazard was the obsolete three-segment reporting structure. It is now explicitly dated FY2026 and superseded for FY2027 by the September filing. A full numerical recast is still missing, so the profile cannot support segment time-series comparisons by itself.

The identity reference in C07 was expanded after checking the original cited presentation. No unresolved factual contradiction remains in the included claims. Competition is category-level; market shares, detailed debt maturities, ownership and incentives, customer concentration, current valuation, and a comprehensive intervening-news review remain open. The missing valuation section is intentional and honest.

Result: the included claims and metrics support an evidence-reviewed pilot profile with the stated gaps. Any subsequent body or packet change requires hash-bound review renewal; the prose notes alone must not automatically set repository status.
