# Coverage gaps and next research tasks

[Company index](INDEX.md)

Data release: `coverage-20261023-39925380279-1`; source created 2026-10-23T08:47:59.341415+00:00.

These counts describe distinct mapped issuers. Foreign-form and fund-reporting signals are derived from retained filing metadata, not a verified domicile or final instrument classification. The universe may include funds awaiting instrument review. Financial coverage is separate from completed research.

| Financial collection state | Issuers | Next action |
| --- | ---: | --- |
| available | 4052 | Retain dated financial evidence and review blocked metrics before analytical use. |
| latest_filing_incomplete | 211 | Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit. |
| foreign_reporting_adapter | 1028 | Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization. |
| fund_reporting_review | 317 | Review the instrument against its N-CSR/N-CSRS reporting evidence before applying an operating-company model. This signal alone is not a final fund classification. |
| unsupported_reporting_inventory | 26 | Review primary filing evidence and identify the reporting regime; do not infer financial values from directory membership. |
| not_collected | 0 | Collect verified issuer submissions and source financial data before normalization. |

Unresolved stock listings: **604**. Verify their issuer identity before attaching any company financial data.

Generated research profiles remain stubs. Curated research links retain their original review dates; broad market prices, consensus, news and ownership still need separate source coverage.

## latest_filing_incomplete

Resolve the latest financial filing/CompanyFacts mismatch; any historical bootstrap must keep the latest-period gap explicit.

Examples (up to 20; each company file contains its source evidence and task):

- [ABBOTT LABORATORIES — 0000001800](companies/0000001800/README.md)
- [AMERICAN ELECTRIC POWER CO INC — 0000004904](companies/0000004904/README.md)
- [AZZ INC — 0000008947](companies/0000008947/README.md)
- [CANADIAN PACIFIC KANSAS CITY LTD/CN — 0000016875](companies/0000016875/README.md)
- [CLOROX CO /DE/ — 0000021076](companies/0000021076/README.md)
- [COCA COLA CO — 0000021344](companies/0000021344/README.md)
- [CTO Realty Growth, Inc. — 0000023795](companies/0000023795/README.md)
- [CTS CORP — 0000026058](companies/0000026058/README.md)
- [OMNICOM GROUP INC. — 0000029989](companies/0000029989/README.md)
- [EIDP, Inc. — 0000030554](companies/0000030554/README.md)
- [FEDERAL REALTY INVESTMENT TRUST — 0000034903](companies/0000034903/README.md)
- [FORD MOTOR CO — 0000037996](companies/0000037996/README.md)
- [FRANKLIN ELECTRIC CO INC — 0000038725](companies/0000038725/README.md)
- [GENERAL DYNAMICS CORP — 0000040533](companies/0000040533/README.md)
- [GREIF, INC — 0000043920](companies/0000043920/README.md)
- [HUBBELL INC — 0000048898](companies/0000048898/README.md)
- [HUMANA INC — 0000049071](companies/0000049071/README.md)
- [HUNTINGTON BANCSHARES INC /MD/ — 0000049196](companies/0000049196/README.md)
- [IMPERIAL OIL LTD — 0000049938](companies/0000049938/README.md)
- [MASCO CORP /DE/ — 0000062996](companies/0000062996/README.md)

## fund_reporting_review

Review the instrument against its N-CSR/N-CSRS reporting evidence before applying an operating-company model. This signal alone is not a final fund classification.

Examples (up to 20; each company file contains its source evidence and task):

- [ADAMS DIVERSIFIED EQUITY FUND, INC. — 0000002230](companies/0000002230/README.md)
- [Invesco Bond Fund — 0000005094](companies/0000005094/README.md)
- [BANCROFT FUND LTD — 0000009521](companies/0000009521/README.md)
- [CENTRAL SECURITIES CORP — 0000018748](companies/0000018748/README.md)
- [CORNERSTONE TOTAL RETURN FUND INC — 0000033934](companies/0000033934/README.md)
- [GENERAL AMERICAN INVESTORS CO INC — 0000040417](companies/0000040417/README.md)
- [MEXICO FUND INC — 0000065433](companies/0000065433/README.md)
- [Western Asset Investment Grade Income Fund Inc. — 0000075398](companies/0000075398/README.md)
- [TRI-CONTINENTAL Corp — 0000099614](companies/0000099614/README.md)
- [SRH Total Return Fund, Inc. — 0000102426](companies/0000102426/README.md)
- [ADAMS NATURAL RESOURCES FUND, INC. — 0000216851](companies/0000216851/README.md)
- [BARINGS CORPORATE INVESTORS — 0000275694](companies/0000275694/README.md)
- [KOREA FUND INC — 0000748691](companies/0000748691/README.md)
- [JOHN HANCOCK INVESTORS TRUST — 0000759828](companies/0000759828/README.md)
- [JOHN HANCOCK INCOME SECURITIES TRUST — 0000759866](companies/0000759866/README.md)
- [ABRDN AUSTRALIA EQUITY FUND, INC. — 0000779336](companies/0000779336/README.md)
- [LIBERTY ALL STAR GROWTH FUND INC. — 0000786035](companies/0000786035/README.md)
- [ABRDN ASIA-PACIFIC INCOME FUND, INC. — 0000790500](companies/0000790500/README.md)
- [ELLSWORTH GROWTH & INCOME FUND LTD — 0000793040](companies/0000793040/README.md)
- [GABELLI EQUITY TRUST INC — 0000794685](companies/0000794685/README.md)

## foreign_reporting_adapter

Add support for the observed 20-F, 40-F or 6-K reporting forms and verify the actual accounting taxonomy before normalization.

Examples (up to 20; each company file contains its source evidence and task):

- [AGNICO EAGLE MINES LTD — 0000002809](companies/0000002809/README.md)
- [Scully Royalty Ltd. — 0000016859](companies/0000016859/README.md)
- [CANADIAN NATIONAL RAILWAY CO — 0000016868](companies/0000016868/README.md)
- [MITSUBISHI UFJ FINANCIAL GROUP INC — 0000067088](companies/0000067088/README.md)
- [UNILEVER PLC — 0000217410](companies/0000217410/README.md)
- [SUNCOR ENERGY INC — 0000311337](companies/0000311337/README.md)
- [BARCLAYS PLC — 0000312069](companies/0000312069/README.md)
- [Sony Group Corp — 0000313838](companies/0000313838/README.md)
- [SASOL LTD — 0000314590](companies/0000314590/README.md)
- [AVINO SILVER & GOLD MINES LTD — 0000316888](companies/0000316888/README.md)
- [NOVO NORDISK A S — 0000353278](companies/0000353278/README.md)
- [KINROSS GOLD CORP — 0000701818](companies/0000701818/README.md)
- [HONDA MOTOR CO LTD — 0000715153](companies/0000715153/README.md)
- [BCE INC — 0000718940](companies/0000718940/README.md)
- [MAGNA INTERNATIONAL INC — 0000749098](companies/0000749098/README.md)
- [BARRICK MINING CORP — 0000756894](companies/0000756894/README.md)
- [Caledonia Mining Corp Plc — 0000766011](companies/0000766011/README.md)
- [PAN AMERICAN SILVER CORP — 0000771992](companies/0000771992/README.md)
- [WPP plc — 0000806968](companies/0000806968/README.md)
- [TAT TECHNOLOGIES LTD — 0000808439](companies/0000808439/README.md)

## unsupported_reporting_inventory

Review primary filing evidence and identify the reporting regime; do not infer financial values from directory membership.

Examples (up to 20; each company file contains its source evidence and task):

- [Preferred Bank — 0001492165](companies/0001492165/README.md)
- [Bank OZK — 0001569650](companies/0001569650/README.md)
- [ADARx Pharmaceuticals, Inc. — 0001802369](companies/0001802369/README.md)
- [Iambic Therapeutics, Inc. — 0001997038](companies/0001997038/README.md)
- [Retension Pharmaceuticals, Inc. — 0002002988](companies/0002002988/README.md)
- [ROZE AI INC. — 0002075335](companies/0002075335/README.md)
- [Ives Ultra AI Opportunities Inc. — 0002077345](companies/0002077345/README.md)
- [Electra Therapeutics, Inc. — 0002088082](companies/0002088082/README.md)
- [Evernorth Holdings Inc. — 0002092592](companies/0002092592/README.md)
- [West Coast Community Bancorp — 0002105965](companies/0002105965/README.md)
- [Xtend AI Robotics, Inc. — 0002111860](companies/0002111860/README.md)
- [Churchill Capital Corp XIII — 0002114229](companies/0002114229/README.md)
- [Pelican Acquisition II Corp — 0002122392](companies/0002122392/README.md)
- [Orion180 Insurance Group Inc. — 0002124472](companies/0002124472/README.md)
- [Three Lions Acquisition Corp. — 0002128462](companies/0002128462/README.md)
- [Vylor Inc. — 0002128626](companies/0002128626/README.md)
- [Lyntris Inc. — 0002132582](companies/0002132582/README.md)
- [NorthStrive Acquisition Corp I. — 0002133719](companies/0002133719/README.md)
- [Real REMAX Group Inc. — 0002136387](companies/0002136387/README.md)
- [TRex Bio, Inc. — 0002139097](companies/0002139097/README.md)
