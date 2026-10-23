# Coverage gaps and next research tasks

[Company index](INDEX.md)

Data release: `coverage-20261023-39968262770-1`; source created 2026-10-23T14:35:22.252685+00:00.

These counts describe distinct mapped issuers. Foreign-form and fund-reporting signals are derived from retained filing metadata, not a verified domicile or final instrument classification. The universe may include funds awaiting instrument review. Financial coverage is separate from completed research.

| Financial collection state | Issuers | Next action |
| --- | ---: | --- |
| available | 4052 | Retain dated financial evidence and review blocked metrics before analytical use. |
| latest_filing_incomplete | 211 | Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit. |
| foreign_reporting_adapter | 1028 | Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization. |
| fund_reporting_review | 317 | Review the instrument against its N-CSR/N-CSRS reporting evidence before applying an operating-company model. This signal alone is not a final fund classification. |
| unsupported_reporting_inventory | 26 | Review primary filing evidence and identify the reporting regime; do not infer financial values from directory membership. |
| not_collected | 0 | Collect verified issuer submissions and source financial data before normalization. |

Unresolved stock listings: **607**. Verify their issuer identity before attaching any company financial data.

Generated research profiles remain stubs. Curated research links retain their original review dates; broad market prices, consensus, news and ownership still need separate source coverage.

## latest_filing_incomplete

Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.

Examples (up to 20; each company file contains its source evidence and task):

- [ABT — ABBOTT LABORATORIES](companies/ABT/README.md)
- [AEP — AMERICAN ELECTRIC POWER CO INC](companies/AEP/README.md)
- [AZZ — AZZ INC](companies/AZZ/README.md)
- [CP — CANADIAN PACIFIC KANSAS CITY LTD/CN](companies/CP/README.md)
- [CLX — CLOROX CO /DE/](companies/CLX/README.md)
- [KO — COCA COLA CO](companies/KO/README.md)
- [CTO — CTO Realty Growth, Inc.](companies/CTO/README.md)
- [CTS — CTS CORP](companies/CTS/README.md)
- [OMC — OMNICOM GROUP INC.](companies/OMC/README.md)
- [CTA_24A — EIDP, Inc.](companies/CTA_24A/README.md)
- [FRT — FEDERAL REALTY INVESTMENT TRUST](companies/FRT/README.md)
- [F — FORD MOTOR CO](companies/F/README.md)
- [FELE — FRANKLIN ELECTRIC CO INC](companies/FELE/README.md)
- [GD — GENERAL DYNAMICS CORP](companies/GD/README.md)
- [GEF — GREIF, INC](companies/GEF/README.md)
- [HUBB — HUBBELL INC](companies/HUBB/README.md)
- [HUM — HUMANA INC](companies/HUM/README.md)
- [HBAN — HUNTINGTON BANCSHARES INC /MD/](companies/HBAN/README.md)
- [IMO — IMPERIAL OIL LTD](companies/IMO/README.md)
- [MAS — MASCO CORP /DE/](companies/MAS/README.md)

## fund_reporting_review

Review the instrument against its N-CSR/N-CSRS reporting evidence before applying an operating-company model. This signal alone is not a final fund classification.

Examples (up to 20; each company file contains its source evidence and task):

- [ADX — ADAMS DIVERSIFIED EQUITY FUND, INC.](companies/ADX/README.md)
- [VBF — Invesco Bond Fund](companies/VBF/README.md)
- [BCV — BANCROFT FUND LTD](companies/BCV/README.md)
- [CET — CENTRAL SECURITIES CORP](companies/CET/README.md)
- [CRF — CORNERSTONE TOTAL RETURN FUND INC](companies/CRF/README.md)
- [GAM — GENERAL AMERICAN INVESTORS CO INC](companies/GAM/README.md)
- [MXF — MEXICO FUND INC](companies/MXF/README.md)
- [PAI — Western Asset Investment Grade Income Fund Inc.](companies/PAI/README.md)
- [TY — TRI-CONTINENTAL Corp](companies/TY/README.md)
- [STEW — SRH Total Return Fund, Inc.](companies/STEW/README.md)
- [PEO — ADAMS NATURAL RESOURCES FUND, INC.](companies/PEO/README.md)
- [MCI — BARINGS CORPORATE INVESTORS](companies/MCI/README.md)
- [KF — KOREA FUND INC](companies/KF/README.md)
- [JHI — JOHN HANCOCK INVESTORS TRUST](companies/JHI/README.md)
- [JHS — JOHN HANCOCK INCOME SECURITIES TRUST](companies/JHS/README.md)
- [IAF — ABRDN AUSTRALIA EQUITY FUND, INC.](companies/IAF/README.md)
- [ASG — LIBERTY ALL STAR GROWTH FUND INC.](companies/ASG/README.md)
- [FAX — ABRDN ASIA-PACIFIC INCOME FUND, INC.](companies/FAX/README.md)
- [ECF — ELLSWORTH GROWTH & INCOME FUND LTD](companies/ECF/README.md)
- [GAB — GABELLI EQUITY TRUST INC](companies/GAB/README.md)

## foreign_reporting_adapter

Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.

Examples (up to 20; each company file contains its source evidence and task):

- [AEM — AGNICO EAGLE MINES LTD](companies/AEM/README.md)
- [SRL — Scully Royalty Ltd.](companies/SRL/README.md)
- [CNI — CANADIAN NATIONAL RAILWAY CO](companies/CNI/README.md)
- [MUFG — MITSUBISHI UFJ FINANCIAL GROUP INC](companies/MUFG/README.md)
- [UL — UNILEVER PLC](companies/UL/README.md)
- [SU — SUNCOR ENERGY INC](companies/SU/README.md)
- [BCS — BARCLAYS PLC](companies/BCS/README.md)
- [SONY — Sony Group Corp](companies/SONY/README.md)
- [SSL — SASOL LTD](companies/SSL/README.md)
- [ASM — AVINO SILVER & GOLD MINES LTD](companies/ASM/README.md)
- [NVO — NOVO NORDISK A S](companies/NVO/README.md)
- [KGC — KINROSS GOLD CORP](companies/KGC/README.md)
- [HMC — HONDA MOTOR CO LTD](companies/HMC/README.md)
- [BCE — BCE INC](companies/BCE/README.md)
- [MGA — MAGNA INTERNATIONAL INC](companies/MGA/README.md)
- [B — BARRICK MINING CORP](companies/B/README.md)
- [CMCL — Caledonia Mining Corp Plc](companies/CMCL/README.md)
- [PAAS — PAN AMERICAN SILVER CORP](companies/PAAS/README.md)
- [WPP — WPP plc](companies/WPP/README.md)
- [TATT — TAT TECHNOLOGIES LTD](companies/TATT/README.md)

## unsupported_reporting_inventory

Review primary filing evidence and identify the reporting regime; do not infer financial values from directory membership.

Examples (up to 20; each company file contains its source evidence and task):

- [PFBC — Preferred Bank](companies/PFBC/README.md)
- [OZK — Bank OZK](companies/OZK/README.md)
- [ADRX — ADARx Pharmaceuticals, Inc.](companies/ADRX/README.md)
- [IAM — Iambic Therapeutics, Inc.](companies/IAM/README.md)
- [RTSN — Retension Pharmaceuticals, Inc.](companies/RTSN/README.md)
- [RZAI — ROZE AI INC.](companies/RZAI/README.md)
- [IVAI — Ives Ultra AI Opportunities Inc.](companies/IVAI/README.md)
- [ETRA — Electra Therapeutics, Inc.](companies/ETRA/README.md)
- [XRPN — Evernorth Holdings Inc.](companies/XRPN/README.md)
- [WCCB — West Coast Community Bancorp](companies/WCCB/README.md)
- [XTND — Xtend AI Robotics, Inc.](companies/XTND/README.md)
- [XIII — Churchill Capital Corp XIII](companies/XIII/README.md)
- [PLCI — Pelican Acquisition II Corp](companies/PLCI/README.md)
- [OIG — Orion180 Insurance Group Inc.](companies/OIG/README.md)
- [TLAC — Three Lions Acquisition Corp.](companies/TLAC/README.md)
- [VYLR — Vylor Inc.](companies/VYLR/README.md)
- [LYNX — Lyntris Inc.](companies/LYNX/README.md)
- [NSAI — NorthStrive Acquisition Corp I.](companies/NSAI/README.md)
- [REAX — Real REMAX Group Inc.](companies/REAX/README.md)
- [TRXB — TRex Bio, Inc.](companies/TRXB/README.md)
