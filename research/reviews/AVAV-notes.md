# AVAV evidence review notes

Review performed on 2026-10-18 against the exact evidence packet in `research/pilot/AVAV.json`. This is a substantive source check, not a substitute for the pipeline's packet-hash and rendered-body-hash review record.

## Scope and method

The reviewer read the business, competition, risk and financial sections of the fiscal 2026 Form 10-K; the latest Form 10-Q's statements, acquisition and debt notes, management discussion, controls and litigation disclosures; the September earnings release and reconciliation; the executive-officer section of the 2026 proxy; and the September annual-meeting results filing. Source URLs and publication dates are embedded in the packet. Downloaded source documents and SHA-256 hashes are retained in the ignored defense research cache.

A second pass revisited each material claim against its source heading. The pass checked period boundaries from the quarterly filing's XBRL contexts, statement units, loss signs, accounting basis and attribution of forecasts. It also checked that source-backed competitor relationships were not converted into unsourced customer relationships.

| Claims | Source locations checked | Review outcome |
|---|---|---|
| C01 | S02 cover and Note 1 | Scope and latest reporting period supported. |
| C02 | S01 Item 7, Overview / Revenue | Segments and revenue mechanisms supported. |
| C03 | S01 Item 1, product groups | Examples supported; no performance comparison inferred. |
| C04 | S01 Item 1, Customers | Contracting buyer versus end user distinction preserved. |
| C05 | S01 manufacturing and seasonality | Delivery dependencies supported. |
| C06 | S01 Competition | Competitor names are attributed to management; no market shares assigned. |
| C07 | S01 intellectual property and competition | Clearly labelled interpretation; no proven-moat assertion. |
| C08 | S03 opening commentary | Management intention, not achieved capacity or independent forecast. |
| C09 | S02 Item 2, Revenue and SCDE Revenue | Adverse product and segment developments retained. |
| C10 | S03 statements; independent tie-out to S02 statements | Revenue, net loss and diluted loss verified. |
| C11 | S03 results narrative and reconciliations | Company-defined adjusted metrics separated from GAAP. |
| C12 | C10 inputs and S02 Revenue | Arithmetic recomputed; organic-growth limitation retained. |
| C13 | S02 balance sheet and Note 9 | Carrying value distinguished from face value; debt note locator corrected in this pass. |
| C14 | S02 cash-flow statement and liquidity discussion | Operating cash flow distinguished from free cash flow. |
| C15 | S05 Executive Officers; S03 conference-call details; S04 Item 5.07 | Roles and voting account supported at cited dates. |
| C16 | S03 results and reconciliation | Valuation method is interpretation; no market price or target supplied. |
| C17 | S03 outlook and S02 Note 1 | Monitoring trigger, not an invented earnings announcement date. |
| C18 | S01 risks; S02 controls and legal proceedings | Cancellation, reporting-control issues and litigation are treated distinctly. Allegations remain allegations. |
| C19 | S02 operations and controls | Scenario conditions are labelled; no probabilities or return forecasts. |
| C20 | S02 Note 15, acquisition subsections | Dates and ownership relationship supported. |
| C21 | S04 Item 5.07 | Event date versus filing date preserved. |

## Financial checks

All eleven metric entries were checked against their corresponding claim and source location. M01–M06 tie to the release, with GAAP amounts also checked against the quarterly filing. M07 is derived from M01 and M02, retains the source periods, and rounds consistently with C12. M08–M10 tie to the balance sheet and debt note. M11 ties to the cash-flow statement. Fiscal-quarter boundaries were verified from the underlying XBRL contexts rather than inferred from calendar quarter conventions.

## Limits and conclusion

This is a reviewed, bounded company profile, not a completed investment recommendation. Current valuation, consensus, complete customer economics, competitive market shares and an exhaustive subsequent announcement feed remain explicit gaps. Ongoing legal and control matters require fresh evidence; no resolution is inferred. The period covered by reported financials differs from the evidence cutoff, as disclosed in the packet.

The source checks support accepting this constrained reference profile. The main workflow must bind any `reviewed` status to the final packet hash and rendered draft-body hash after all edits. Changes to content invalidate that binding and need a fresh substantive review of the changed claims.
