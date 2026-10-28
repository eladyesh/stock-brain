---
schema_version: 1
document_type: company_facts
company_id: company-cik-0001610853
cik: 0001610853
company_name: Solana Co
tickers:
- HSDT
status: stub
canonical_reviewed: false
as_of: '2026-10-28'
updated_at: '2026-10-28T16:13:42.115634+00:00'
reviewed_at: null
coverage_release: coverage-20261028-40722802424-1
source_commit: 48056b79cf1dc5f5270bd576defc5c9bc49d62cf
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-12G
  - 10-12G/A
  - 10-K
  - 10-K/A
  - 10-KT
  - 10-Q
  - 10-Q/A
  - '3'
  - 3/A
  - '4'
  - 4/A
  - 424B3
  - 424B4
  - 424B5
  - 424B7
  - 8-A12B
  - 8-A12G
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - CORRESP
  - CT ORDER
  - D
  - DEF 14A
  - DEFA14A
  - DRS
  - DRSLTR
  - EFFECT
  - NT 10-K
  - NT 10-Q
  - POS AM
  - POSASR
  - PRE 14A
  - RW
  - S-1
  - S-1/A
  - S-1MEF
  - S-3
  - S-3/A
  - S-3ASR
  - S-8
  - SC 13D
  - SC 13D/A
  - SC 13G
  - SC 13G/A
  - SC TO-I
  - SC TO-I/A
  - SCHEDULE 13D
  - SCHEDULE 13D/A
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - SD
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001610853.json
    sha256: 46e6493c39e56936f374142a3d190afea4f84f6b840054f34dcd648e07a75d55
    retrieved_at: '2026-10-22T17:53:02.398600+00:00'
    archive:
      member: CIK0001610853.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0001610853.json
    sha256: 558e4bac3569f3d7b0aa7c208da5b3fd97912542d048edbf08073ef88c037bf2
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0001610853.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-28T16:09:01.738588+00:00'
  sha256: b555e192b928396dc88877226e82c2c8e9470c389cf2def559495683c673510d
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0001610853.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 558e4bac3569f3d7b0aa7c208da5b3fd97912542d048edbf08073ef88c037bf2
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0001610853.json
  published_at: null
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: 46e6493c39e56936f374142a3d190afea4f84f6b840054f34dcd648e07a75d55
- id: S04
  title: 10-K 0001104659-26-037194
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926037194/0001104659-26-037194-index.html
  published_at: '2026-03-31'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001610853-26-000007
  url: https://www.sec.gov/Archives/edgar/data/1610853/000161085326000007/0001610853-26-000007-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S06
  title: 10-K 0001558370-25-003619
  url: https://www.sec.gov/Archives/edgar/data/1610853/000155837025003619/0001558370-25-003619-index.html
  published_at: '2025-03-25'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S07
  title: 10-K 0001558370-24-004260
  url: https://www.sec.gov/Archives/edgar/data/1610853/000155837024004260/0001558370-24-004260-index.html
  published_at: '2024-03-28'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S08
  title: 10-K 0001558370-23-003338
  url: https://www.sec.gov/Archives/edgar/data/1610853/000155837023003338/0001558370-23-003338-index.html
  published_at: '2023-03-09'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S09
  title: 10-Q 0001104659-26-062611
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926062611/0001104659-26-062611-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S10
  title: 10-Q 0001104659-25-113714
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465925113714/0001104659-25-113714-index.html
  published_at: '2025-11-18'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S11
  title: 10-Q 0001558370-25-011568
  url: https://www.sec.gov/Archives/edgar/data/1610853/000155837025011568/0001558370-25-011568-index.html
  published_at: '2025-08-14'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S12
  title: 10-Q 0001558370-25-006120
  url: https://www.sec.gov/Archives/edgar/data/1610853/000155837025006120/0001558370-25-006120-index.html
  published_at: '2025-05-01'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S13
  title: 10-Q 0001558370-24-015344
  url: https://www.sec.gov/Archives/edgar/data/1610853/000155837024015344/0001558370-24-015344-index.html
  published_at: '2024-11-12'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S14
  title: 10-Q 0001558370-24-011905
  url: https://www.sec.gov/Archives/edgar/data/1610853/000155837024011905/0001558370-24-011905-index.html
  published_at: '2024-08-12'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S15
  title: 10-Q 0001558370-24-007971
  url: https://www.sec.gov/Archives/edgar/data/1610853/000155837024007971/0001558370-24-007971-index.html
  published_at: '2024-05-13'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S16
  title: 10-Q 0001558370-23-018605
  url: https://www.sec.gov/Archives/edgar/data/1610853/000155837023018605/0001558370-23-018605-index.html
  published_at: '2023-11-09'
  retrieved_at: '2026-10-22T17:53:02.398600+00:00'
  sha256: null
- id: S17
  title: 424B5 0001610853-26-000010
  url: https://www.sec.gov/Archives/edgar/data/1610853/000161085326000010/0001610853-26-000010-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: 8-K 0001610853-26-000008
  url: https://www.sec.gov/Archives/edgar/data/1610853/000161085326000008/0001610853-26-000008-index.html
  published_at: '2026-09-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: SCHEDULE 13D/A 0001213900-26-100250
  url: https://www.sec.gov/Archives/edgar/data/1610853/000121390026100250/0001213900-26-100250-index.html
  published_at: '2026-09-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 4 0002127311-26-000006
  url: https://www.sec.gov/Archives/edgar/data/1610853/000212731126000006/0002127311-26-000006-index.html
  published_at: '2026-08-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: SCHEDULE 13G/A 0001104659-26-100294
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926100294/0001104659-26-100294-index.html
  published_at: '2026-08-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S22
  title: 10-Q 0001610853-26-000007
  url: https://www.sec.gov/Archives/edgar/data/1610853/000161085326000007/0001610853-26-000007-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S23
  title: 8-K 0001610853-26-000005
  url: https://www.sec.gov/Archives/edgar/data/1610853/000161085326000005/0001610853-26-000005-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S24
  title: 4 0002086036-26-000006
  url: https://www.sec.gov/Archives/edgar/data/1610853/000208603626000006/0002086036-26-000006-index.html
  published_at: '2026-08-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S25
  title: 4 0001104659-26-082801
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926082801/0001104659-26-082801-index.html
  published_at: '2026-07-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S26
  title: 3 0001104659-26-082791
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926082791/0001104659-26-082791-index.html
  published_at: '2026-07-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S27
  title: 4 0002086128-26-000005
  url: https://www.sec.gov/Archives/edgar/data/1610853/000208612826000005/0002086128-26-000005-index.html
  published_at: '2026-06-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S28
  title: 4 0002086128-26-000003
  url: https://www.sec.gov/Archives/edgar/data/1610853/000208612826000003/0002086128-26-000003-index.html
  published_at: '2026-06-04'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S29
  title: 8-K 0001104659-26-068370
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926068370/0001104659-26-068370-index.html
  published_at: '2026-05-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S30
  title: 424B5 0001104659-26-068348
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926068348/0001104659-26-068348-index.html
  published_at: '2026-05-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S31
  title: SD 0001104659-26-068243
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926068243/0001104659-26-068243-index.html
  published_at: '2026-05-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S32
  title: 4 0002131577-26-000005
  url: https://www.sec.gov/Archives/edgar/data/1610853/000213157726000005/0002131577-26-000005-index.html
  published_at: '2026-05-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S33
  title: 4 0002130655-26-000005
  url: https://www.sec.gov/Archives/edgar/data/1610853/000213065526000005/0002130655-26-000005-index.html
  published_at: '2026-05-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S34
  title: 4 0001340555-26-000007
  url: https://www.sec.gov/Archives/edgar/data/1610853/000134055526000007/0001340555-26-000007-index.html
  published_at: '2026-05-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S35
  title: 4/A 0001340555-26-000005
  url: https://www.sec.gov/Archives/edgar/data/1610853/000134055526000005/0001340555-26-000005-index.html
  published_at: '2026-05-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S36
  title: SCHEDULE 13D/A 0001213900-26-061030
  url: https://www.sec.gov/Archives/edgar/data/1610853/000121390026061030/0001213900-26-061030-index.html
  published_at: '2026-05-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S37
  title: 4 0001075380-26-000006
  url: https://www.sec.gov/Archives/edgar/data/1610853/000107538026000006/0001075380-26-000006-index.html
  published_at: '2026-05-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S38
  title: 4/A 0001075380-26-000004
  url: https://www.sec.gov/Archives/edgar/data/1610853/000107538026000004/0001075380-26-000004-index.html
  published_at: '2026-05-26'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S39
  title: 8-K 0001104659-26-065815
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926065815/0001104659-26-065815-index.html
  published_at: '2026-05-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S40
  title: 4 0001104659-26-065600
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926065600/0001104659-26-065600-index.html
  published_at: '2026-05-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S41
  title: 3 0001104659-26-065598
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926065598/0001104659-26-065598-index.html
  published_at: '2026-05-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S42
  title: DEFA14A 0001104659-26-062844
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926062844/0001104659-26-062844-index.html
  published_at: '2026-05-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S43
  title: SCHEDULE 13G/A 0002048251-26-003782
  url: https://www.sec.gov/Archives/edgar/data/1610853/000204825126003782/0002048251-26-003782-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S44
  title: 10-Q 0001104659-26-062611
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926062611/0001104659-26-062611-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S45
  title: 8-K 0001104659-26-062534
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926062534/0001104659-26-062534-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S46
  title: SCHEDULE 13D/A 0002087954-26-000002
  url: https://www.sec.gov/Archives/edgar/data/1610853/000208795426000002/0002087954-26-000002-index.html
  published_at: '2026-05-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S47
  title: 4 0002086036-26-000002
  url: https://www.sec.gov/Archives/edgar/data/1610853/000208603626000002/0002086036-26-000002-index.html
  published_at: '2026-05-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S48
  title: SCHEDULE 13G/A 0001104659-26-057882
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926057882/0001104659-26-057882-index.html
  published_at: '2026-05-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S49
  title: DEFA14A 0001104659-26-054183
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926054183/0001104659-26-054183-index.html
  published_at: '2026-05-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S50
  title: 3 0002131577-26-000003
  url: https://www.sec.gov/Archives/edgar/data/1610853/000213157726000003/0002131577-26-000003-index.html
  published_at: '2026-04-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S51
  title: 3/A 0002130655-26-000003
  url: https://www.sec.gov/Archives/edgar/data/1610853/000213065526000003/0002130655-26-000003-index.html
  published_at: '2026-04-30'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S52
  title: 424B5 0001104659-26-049074
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926049074/0001104659-26-049074-index.html
  published_at: '2026-04-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S53
  title: 8-K 0001104659-26-049070
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926049070/0001104659-26-049070-index.html
  published_at: '2026-04-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  title: 8-K 0001104659-26-048625
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926048625/0001104659-26-048625-index.html
  published_at: '2026-04-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S55
  title: ARS 0001104659-26-042868
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926042868/0001104659-26-042868-index.html
  published_at: '2026-04-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S56
  title: 8-K 0001104659-26-042666
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926042666/0001104659-26-042666-index.html
  published_at: '2026-04-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S57
  title: DEF 14A 0001104659-26-041970
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926041970/0001104659-26-041970-index.html
  published_at: '2026-04-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S58
  title: 8-K 0001104659-26-041571
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926041571/0001104659-26-041571-index.html
  published_at: '2026-04-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S59
  title: EFFECT 9999999995-26-001114
  url: https://www.sec.gov/Archives/edgar/data/1610853/999999999526001114/9999999995-26-001114-index.html
  published_at: '2026-04-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S60
  title: EFFECT 9999999995-26-001113
  url: https://www.sec.gov/Archives/edgar/data/1610853/999999999526001113/9999999995-26-001113-index.html
  published_at: '2026-04-08'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S61
  title: 3 0002127311-26-000002
  url: https://www.sec.gov/Archives/edgar/data/1610853/000212731126000002/0002127311-26-000002-index.html
  published_at: '2026-04-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S62
  title: 4 0001537711-26-000002
  url: https://www.sec.gov/Archives/edgar/data/1610853/000153771126000002/0001537711-26-000002-index.html
  published_at: '2026-04-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S63
  title: 4 0001340555-26-000002
  url: https://www.sec.gov/Archives/edgar/data/1610853/000134055526000002/0001340555-26-000002-index.html
  published_at: '2026-04-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S64
  title: 4 0001215243-26-000003
  url: https://www.sec.gov/Archives/edgar/data/1610853/000121524326000003/0001215243-26-000003-index.html
  published_at: '2026-04-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S65
  title: 4 0001075380-26-000002
  url: https://www.sec.gov/Archives/edgar/data/1610853/000107538026000002/0001075380-26-000002-index.html
  published_at: '2026-04-02'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S66
  title: S-8 0001104659-26-037423
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926037423/0001104659-26-037423-index.html
  published_at: '2026-03-31'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0001610853
  classification_status: reported_sic
  entity_type: operating
  name: Solana Co
  sic: '6199'
  sic_description: Finance Services
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: 558e4bac3569f3d7b0aa7c208da5b3fd97912542d048edbf08073ef88c037bf2
  url: https://data.sec.gov/submissions/CIK0001610853.json
listings:
- ticker: HSDT
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001104659-26-037194
  filed: '2026-03-31'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926037194/0001104659-26-037194-index.html
- accession: 0001610853-26-000007
  filed: '2026-08-14'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/1610853/000161085326000007/0001610853-26-000007-index.html
- accession: 0001104659-26-041970
  filed: '2026-04-10'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/1610853/000110465926041970/0001104659-26-041970-index.html
- accession: 0001610853-26-000008
  filed: '2026-09-30'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/1610853/000161085326000008/0001610853-26-000008-index.html
- accession: 0001564590-21-019403
  filed: '2021-04-19'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610853/000156459021019403/0001564590-21-019403-index.html
- accession: 0001193125-20-186797
  filed: '2020-07-02'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610853/000119312520186797/0001193125-20-186797-index.html
- accession: 0001062993-16-010621
  filed: '2016-07-20'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610853/000106299316010621/0001062993-16-010621-index.html
- accession: 0001062993-16-009103
  filed: '2016-04-20'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610853/000106299316009103/0001062993-16-009103-index.html
- accession: 0001062993-15-005783
  filed: '2015-11-04'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/1610853/000106299315005783/0001062993-15-005783-index.html
research_progress:
  stage: pending
  input_sha256: 4384e1878a10d20ec0e0e97a1656296936d7e3516a90a49f643b4acbffef1de8
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 0
  model_draft: false
  reviewed: false
---
# HSDT — Solana Co

> Automatically maintained factual stub. Substantive company research is incomplete.

[All companies](../../INDEX.md)


## Business overview

Reported issuer name: **Solana Co**. Stable SEC CIK: **0001610853**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| HSDT | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **6199**: Finance Services. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfRevenue; definition_changed_across_series, gross_profit_tieout_failed | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; gross_profit_tieout_failed | [S04] |
| net_income | -40,890,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | -40,890,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | -40,890,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | -16,514,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | -243,840,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, gross_profit_tieout_failed | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 9,250,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |

### annual: 2024-01-01 to 2024-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -5,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfRevenue; definition_changed_across_series | [S04] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S04] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S04] |
| free_cash_flow | -11,046,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | -62,000 | USD | US GAAP / reported | GrossProfit | [S04] |
| net_income | -11,742,000 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | -11,742,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S04] |
| net_income_including_noncontrolling_interests | -11,742,000 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | -11,041,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | -13,903,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; revision_requires_review | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S04] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S04] |
| stock_based_compensation | 2,522,000 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |

### annual: 2023-01-01 to 2023-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -29,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S06] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; definition_changed_across_series, gross_profit_tieout_failed | [S06] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S06] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S06] |
| free_cash_flow | -10,445,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S06] |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; gross_profit_tieout_failed | [S06] |
| net_income | -8,850,000 | USD | US GAAP / reported | NetIncomeLoss | [S06] |
| net_income_common | -8,850,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S06] |
| net_income_including_noncontrolling_interests | -8,850,000 | USD | US GAAP / reported | ProfitLoss | [S06] |
| operating_cash_flow | -10,416,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S06] |
| operating_income | -12,428,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S06] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, gross_profit_tieout_failed | [S06] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S06] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S06] |
| stock_based_compensation | 1,629,000 | USD | US GAAP / reported | ShareBasedCompensation | [S06] |

### annual: 2022-01-01 to 2022-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -17,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S07] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; definition_changed_across_series, gross_profit_tieout_failed | [S07] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S07] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S07] |
| free_cash_flow | -14,327,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S07] |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; gross_profit_tieout_failed | [S07] |
| net_income | -14,072,000 | USD | US GAAP / reported | NetIncomeLoss | [S07] |
| net_income_common | -14,072,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S07] |
| net_income_including_noncontrolling_interests | -14,072,000 | USD | US GAAP / reported | ProfitLoss | [S07] |
| operating_cash_flow | -14,310,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S07] |
| operating_income | -15,516,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S07] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, gross_profit_tieout_failed | [S07] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S07] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S07] |
| stock_based_compensation | 2,254,000 | USD | US GAAP / reported | ShareBasedCompensation | [S07] |

### annual: 2021-01-01 to 2021-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -54,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S08] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; definition_changed_across_series, gross_profit_tieout_failed | [S08] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S08] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S08] |
| free_cash_flow | -13,442,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S08] |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; gross_profit_tieout_failed | [S08] |
| net_income | -18,132,000 | USD | US GAAP / reported | NetIncomeLoss | [S08] |
| net_income_common | -18,132,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S08] |
| net_income_including_noncontrolling_interests | -18,132,000 | USD | US GAAP / reported | ProfitLoss | [S08] |
| operating_cash_flow | -13,388,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S08] |
| operating_income | -18,142,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S08] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, gross_profit_tieout_failed, revision_requires_review | [S08] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S08] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S08] |
| stock_based_compensation | 4,252,000 | USD | US GAAP / reported | ShareBasedCompensation | [S08] |

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfRevenue; definition_changed_across_series | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 2,449,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | -30,256,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | -30,256,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S05] |
| net_income_including_noncontrolling_interests | -30,256,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_cash_flow | -11,892,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | -32,673,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | Revenues; definition_changed_across_series | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 63,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |

### quarterly: 2026-01-01 to 2026-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfRevenue; definition_changed_across_series | [S09] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S09] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S09] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 3,441,000 | USD | US GAAP / reported | GrossProfit | [S09] |
| net_income | -99,799,000 | USD | US GAAP / reported | NetIncomeLoss | [S09] |
| net_income_common | -99,799,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S09] |
| net_income_including_noncontrolling_interests | -99,799,000 | USD | US GAAP / reported | ProfitLoss | [S09] |
| operating_cash_flow | -4,831,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S09] |
| operating_income | -99,618,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S09] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | Revenues; definition_changed_across_series | [S09] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S09] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S09] |
| stock_based_compensation | 90,000 | USD | US GAAP / reported | ShareBasedCompensation | [S09] |

### quarterly: 2025-10-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 5,048,000 | USD | US GAAP / derived | GrossProfit; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| net_income | 325,551,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| net_income_common | 325,551,000 | USD | US GAAP / derived | NetIncomeLossAvailableToCommonStockholdersBasic; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| net_income_including_noncontrolling_interests | 325,551,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| operating_cash_flow | -6,177,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| operating_income | -201,055,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / derived / not model usable | Revenues; cross_filing_derivation, definition_changed_across_series, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 7,746,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |

### quarterly: 2025-07-01 to 2025-09-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; definition_changed_across_series | [S10] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S10] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S10] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | 594,000 | USD | US GAAP / reported | GrossProfit | [S10] |
| net_income | -352,768,000 | USD | US GAAP / reported | NetIncomeLoss | [S10] |
| net_income_common | -352,768,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S10] |
| net_income_including_noncontrolling_interests | -352,770,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S10] [S05] |
| operating_cash_flow | -4,044,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S10] [S05] |
| operating_income | -35,450,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S10] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | Revenues; definition_changed_across_series | [S10] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S10] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S10] |
| stock_based_compensation | 473,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S10] [S05] |

### quarterly: 2025-04-01 to 2025-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfRevenue; definition_changed_across_series | [S05] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | -53,000 | USD | US GAAP / reported | GrossProfit | [S05] |
| net_income | -9,833,000 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | -9,833,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S05] |
| net_income_including_noncontrolling_interests | -9,833,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_cash_flow | -2,757,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |
| operating_income | -3,322,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | Revenues; alternative_tag_scope_differs, definition_changed_across_series | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 409,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S09] |

### quarterly: 2025-01-01 to 2025-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfRevenue; definition_changed_across_series | [S09] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S09] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S09] |
| free_cash_flow | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| gross_profit | -72,000 | USD | US GAAP / reported | GrossProfit | [S09] |
| net_income | -3,838,000 | USD | US GAAP / reported | NetIncomeLoss | [S09] |
| net_income_common | -3,838,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S09] |
| net_income_including_noncontrolling_interests | -3,838,000 | USD | US GAAP / reported | ProfitLoss | [S09] |
| operating_cash_flow | -3,536,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S09] |
| operating_income | -4,011,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S09] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | Revenues; alternative_tag_scope_differs, definition_changed_across_series | [S09] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S09] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S09] |
| stock_based_compensation | 622,000 | USD | US GAAP / reported | ShareBasedCompensation | [S09] |

### quarterly: 2024-10-01 to 2024-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | 0 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / derived / not model usable | CostOfGoodsAndServicesSold; cross_filing_derivation, definition_changed_across_series, standalone_quarter_from_cumulative_difference | [S06] [S10] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | -2,378,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| gross_profit | -2,000 | USD | US GAAP / derived | GrossProfit; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| net_income | -3,928,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| net_income_common | -3,928,000 | USD | US GAAP / derived | NetIncomeLossAvailableToCommonStockholdersBasic; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| net_income_including_noncontrolling_interests | -3,928,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| operating_cash_flow | -2,378,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| operating_income | -3,147,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable | ; unreconciled_cumulative_revision | [S04] [S13] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 428,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S04] [S10] |

### quarterly: 2024-07-01 to 2024-09-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | 0 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S10] [S11] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; definition_changed_across_series | [S10] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S10] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S10] |
| free_cash_flow | -2,771,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S10] [S11] |
| gross_profit | -136,000 | USD | US GAAP / reported | GrossProfit | [S10] |
| net_income | -3,686,000 | USD | US GAAP / reported | NetIncomeLoss | [S10] |
| net_income_common | -3,686,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S10] |
| net_income_including_noncontrolling_interests | -3,686,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S10] [S11] |
| operating_cash_flow | -2,771,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S10] [S11] |
| operating_income | -4,070,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S10] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | Revenues; alternative_tag_scope_differs, definition_changed_across_series | [S10] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S10] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S10] |
| stock_based_compensation | 1,327,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S10] [S11] |

### quarterly: 2024-04-01 to 2024-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | 0 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S11] [S12] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; definition_changed_across_series, gross_profit_tieout_failed | [S11] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S11] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S11] |
| free_cash_flow | -2,891,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S11] [S12] |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; gross_profit_tieout_failed | [S11] |
| net_income | -1,612,000 | USD | US GAAP / reported | NetIncomeLoss | [S11] |
| net_income_common | -1,612,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S11] |
| net_income_including_noncontrolling_interests | -1,612,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S11] [S12] |
| operating_cash_flow | -2,891,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S11] [S12] |
| operating_income | -3,270,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S11] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, definition_changed_across_series, gross_profit_tieout_failed | [S11] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S11] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S11] |
| stock_based_compensation | 366,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S11] [S12] |

### quarterly: 2024-01-01 to 2024-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -5,000 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S12] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; definition_changed_across_series, gross_profit_tieout_failed | [S12] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S12] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S12] |
| free_cash_flow | -3,006,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S12] |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; gross_profit_tieout_failed | [S12] |
| net_income | -2,516,000 | USD | US GAAP / reported | NetIncomeLoss | [S12] |
| net_income_common | -2,516,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S12] |
| net_income_including_noncontrolling_interests | -2,516,000 | USD | US GAAP / reported | ProfitLoss | [S12] |
| operating_cash_flow | -3,001,000 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S12] |
| operating_income | -3,416,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S12] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, definition_changed_across_series, gross_profit_tieout_failed | [S12] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S12] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S12] |
| stock_based_compensation | 401,000 | USD | US GAAP / reported | ShareBasedCompensation | [S12] |

### quarterly: 2023-10-01 to 2023-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -3,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S06] [S13] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / derived / not model usable | CostOfGoodsAndServicesSold; cross_filing_derivation, definition_changed_across_series, gross_profit_tieout_failed, standalone_quarter_from_cumulative_difference | [S06] [S13] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | -2,037,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S06] [S13] |
| gross_profit | Unavailable / blocked | USD | US GAAP / derived / not model usable | GrossProfit; cross_filing_derivation, gross_profit_tieout_failed, standalone_quarter_from_cumulative_difference | [S06] [S13] |
| net_income | -1,045,000 | USD | US GAAP / derived | NetIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S06] [S13] |
| net_income_common | -1,045,000 | USD | US GAAP / derived | NetIncomeLossAvailableToCommonStockholdersBasic; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S06] [S13] |
| net_income_including_noncontrolling_interests | -1,045,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S06] [S13] |
| operating_cash_flow | -2,034,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S06] [S13] |
| operating_income | -2,246,000 | USD | US GAAP / derived | OperatingIncomeLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S06] [S13] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / derived / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; cross_filing_derivation, definition_changed_across_series, gross_profit_tieout_failed, standalone_quarter_from_cumulative_difference | [S06] [S13] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 401,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S06] [S13] |

### quarterly: 2023-07-01 to 2023-09-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -6,000 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S13] [S14] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | CostOfGoodsAndServicesSold; definition_changed_across_series, gross_profit_tieout_failed | [S13] |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S13] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S13] |
| free_cash_flow | -2,458,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S13] [S14] |
| gross_profit | Unavailable / blocked | USD | US GAAP / reported / not model usable | GrossProfit; gross_profit_tieout_failed | [S13] |
| net_income | -3,663,000 | USD | US GAAP / reported | NetIncomeLoss | [S13] |
| net_income_common | -3,663,000 | USD | US GAAP / reported | NetIncomeLossAvailableToCommonStockholdersBasic | [S13] |
| net_income_including_noncontrolling_interests | -3,663,000 | USD | US GAAP / derived | ProfitLoss; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S13] [S14] |
| operating_cash_flow | -2,452,000 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S13] [S14] |
| operating_income | -3,153,000 | USD | US GAAP / reported | OperatingIncomeLoss | [S13] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | Unavailable / blocked | USD | US GAAP / reported / not model usable | RevenueFromContractWithCustomerExcludingAssessedTax; alternative_tag_scope_differs, definition_changed_across_series, gross_profit_tieout_failed | [S13] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S13] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S13] |
| stock_based_compensation | 403,000 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S13] [S14] |

## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:53:02.398600+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 7,282,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### annual: 2024-01-01 to 2024-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 1,088,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### annual: 2023-01-01 to 2023-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 5,182,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S06] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S06] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### annual: 2022-01-01 to 2022-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 14,549,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S07] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S07] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### annual: 2021-01-01 to 2021-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 11,005,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S08] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S08] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 3,647,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2026-01-01 to 2026-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 4,395,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S09] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S09] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2025-10-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 7,282,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S05] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2025-07-01 to 2025-09-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 124,051,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S10] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S10] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2025-04-01 to 2025-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 6,078,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S11] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S11] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2025-01-01 to 2025-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 1,109,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S12] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S12] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2024-10-01 to 2024-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 1,088,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S04] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; revision_requires_review, share_split_and_corporate_action_basis_unverified | [S04] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2024-07-01 to 2024-09-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 3,468,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S13] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S13] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2024-04-01 to 2024-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 6,387,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S14] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S14] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2024-01-01 to 2024-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 3,638,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S15] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S15] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2023-10-01 to 2023-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 5,182,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S06] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S06] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2023-07-01 to 2023-09-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | 6,596,000 | USD | US GAAP / reported | CashAndCashEquivalentsAtCarryingValue | [S16] |
| debt_current | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / reported / not model usable | CommonStockSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S16] |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

Not available: reviewed debt maturity, acquisition, dividend and repurchase analysis.

## Management and governance

Not available: substantive research has not been completed. Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.

## Valuation context

Not available: substantive research has not been completed. Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.

## Catalysts

Not available: substantive research has not been completed. List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.

## Risks and thesis breakers

Not available: substantive research has not been completed. Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.

## Scenarios and open questions

- Research remains a stub; automation does not approve an investment thesis.
- Sector, industry and domicile remain unassigned unless a separate reviewed profile supplies them.
- Prices, news, consensus, ownership, valuation and company relationships require separately dated evidence.
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:34:32.140893+00:00.

### Research work queue

Collection stage: **pending**. Extracted evidence is not a reviewed conclusion. Daily collection resumes from durable state; unchanged accessions are reused.

- **Business overview** (evidence or analysis still needed): Explain what the company does, who pays it, and why the business exists. Cite primary sources.
- **Revenue model and segments** (evidence or analysis still needed): Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.
- **Products and services** (evidence or analysis still needed): Describe the main products, customer problems solved, distribution, and product dependencies.
- **Customers and end markets** (evidence or analysis still needed): Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.
- **Industry and value chain** (evidence or analysis still needed): Place the company among suppliers, distribution channels, customers, and substitutes. Explain cyclicality and supply constraints.
- **Competitive landscape** (evidence or analysis still needed): Identify direct competitors and alternatives. Compare specific products or business segments, with sources.
- **Moat and differentiation** (evidence or analysis still needed): Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.
- **Growth drivers** (evidence or analysis still needed): Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.
- **Financial performance** (evidence or analysis still needed): Record revenue, margins, earnings, cash flow, and relevant sector metrics. Every number needs period, units, currency, accounting basis, and source. Separate reported results, guidance, consensus, and estimates.
- **Balance sheet and capital allocation** (evidence or analysis still needed): Describe cash, debt, maturities, dilution, stock compensation, investment, acquisitions, dividends, and repurchases with dates and sources.
- **Management and governance** (evidence or analysis still needed): Describe leadership, ownership, incentives, governance, and execution history. Verify current roles and date the evidence.
- **Valuation context** (evidence or analysis still needed): Explain suitable valuation metrics and assumptions. Timestamp prices, share counts, net debt, and multiples; distinguish historical, current, and forward figures. Do not present an undated fair value.
- **Catalysts** (evidence or analysis still needed): List dated events, the mechanism by which they matter, uncertainty, and the next evidence to monitor. A scheduled event is not a guaranteed outcome.
- **Risks and thesis breakers** (evidence or analysis still needed): Describe operational, financial, regulatory, and competitive risks and measurable conditions that would invalidate an interpretation.
- **Scenarios and open questions** (evidence or analysis still needed): Separate bull, base, and bear assumptions from facts. Record missing data, disputed evidence, and research questions without inventing answers.
- **Relationships and themes** (evidence or analysis still needed): Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.
- **Recent developments** (evidence or analysis still needed): Keep a dated, source-backed log of material changes. Distinguish the event date from the article date and explain what changed in the profile.

Calculation gaps: Operating margin: compatible positive revenue and usable inputs are required. Net margin: compatible positive revenue and usable inputs are required. Free cash flow margin: compatible positive revenue and usable inputs are required. Stock compensation / revenue: compatible positive revenue and usable inputs are required. revenue: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. net_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest 50 filing metadata records of 729 retained records. A filing link is evidence of submission, not evidence that the document was read or analyzed.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-09-30 | 424B5 | 0001610853-26-000010 | — | [S17] |
| 2026-09-30 | 8-K | 0001610853-26-000008 | — | [S18] |
| 2026-09-15 | SCHEDULE 13D/A | 0001213900-26-100250 | — | [S19] |
| 2026-08-24 | 4 | 0002127311-26-000006 | — | [S20] |
| 2026-08-24 | SCHEDULE 13G/A | 0001104659-26-100294 | — | [S21] |
| 2026-08-14 | 10-Q | 0001610853-26-000007 | — | [S22] |
| 2026-08-14 | 8-K | 0001610853-26-000005 | — | [S23] |
| 2026-08-04 | 4 | 0002086036-26-000006 | — | [S24] |
| 2026-07-13 | 4 | 0001104659-26-082801 | — | [S25] |
| 2026-07-13 | 3 | 0001104659-26-082791 | — | [S26] |
| 2026-06-04 | 4 | 0002086128-26-000005 | — | [S27] |
| 2026-06-04 | 4 | 0002086128-26-000003 | — | [S28] |
| 2026-05-29 | 8-K | 0001104659-26-068370 | — | [S29] |
| 2026-05-29 | 424B5 | 0001104659-26-068348 | — | [S30] |
| 2026-05-29 | SD | 0001104659-26-068243 | — | [S31] |
| 2026-05-26 | 4 | 0002131577-26-000005 | — | [S32] |
| 2026-05-26 | 4 | 0002130655-26-000005 | — | [S33] |
| 2026-05-26 | 4 | 0001340555-26-000007 | — | [S34] |
| 2026-05-26 | 4/A | 0001340555-26-000005 | — | [S35] |
| 2026-05-26 | SCHEDULE 13D/A | 0001213900-26-061030 | — | [S36] |
| 2026-05-26 | 4 | 0001075380-26-000006 | — | [S37] |
| 2026-05-26 | 4/A | 0001075380-26-000004 | — | [S38] |
| 2026-05-22 | 8-K | 0001104659-26-065815 | — | [S39] |
| 2026-05-22 | 4 | 0001104659-26-065600 | — | [S40] |
| 2026-05-22 | 3 | 0001104659-26-065598 | — | [S41] |
| 2026-05-18 | DEFA14A | 0001104659-26-062844 | — | [S42] |
| 2026-05-15 | SCHEDULE 13G/A | 0002048251-26-003782 | — | [S43] |
| 2026-05-15 | 10-Q | 0001104659-26-062611 | — | [S44] |
| 2026-05-15 | 8-K | 0001104659-26-062534 | — | [S45] |
| 2026-05-13 | SCHEDULE 13D/A | 0002087954-26-000002 | — | [S46] |
| 2026-05-13 | 4 | 0002086036-26-000002 | — | [S47] |
| 2026-05-08 | SCHEDULE 13G/A | 0001104659-26-057882 | — | [S48] |
| 2026-05-01 | DEFA14A | 0001104659-26-054183 | — | [S49] |
| 2026-04-30 | 3 | 0002131577-26-000003 | — | [S50] |
| 2026-04-30 | 3/A | 0002130655-26-000003 | — | [S51] |
| 2026-04-27 | 424B5 | 0001104659-26-049074 | — | [S52] |
| 2026-04-27 | 8-K | 0001104659-26-049070 | — | [S53] |
| 2026-04-24 | 8-K | 0001104659-26-048625 | — | [S54] |
| 2026-04-14 | ARS | 0001104659-26-042868 | — | [S55] |
| 2026-04-13 | 8-K | 0001104659-26-042666 | — | [S56] |
| 2026-04-10 | DEF 14A | 0001104659-26-041970 | — | [S57] |
| 2026-04-09 | 8-K | 0001104659-26-041571 | — | [S58] |
| 2026-04-08 | EFFECT | 9999999995-26-001114 | — | [S59] |
| 2026-04-08 | EFFECT | 9999999995-26-001113 | — | [S60] |
| 2026-04-06 | 3 | 0002127311-26-000002 | — | [S61] |
| 2026-04-02 | 4 | 0001537711-26-000002 | — | [S62] |
| 2026-04-02 | 4 | 0001340555-26-000002 | — | [S63] |
| 2026-04-02 | 4 | 0001215243-26-000003 | — | [S64] |
| 2026-04-02 | 4 | 0001075380-26-000002 | — | [S65] |
| 2026-03-31 | S-8 | 0001104659-26-037423 | — | [S66] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-28T16:09:01.738588+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0001610853.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0001610853.json) — published not supplied; retrieved 2026-10-22T17:53:02.398600+00:00.

[S04] [10-K 0001104659-26-037194](https://www.sec.gov/Archives/edgar/data/1610853/000110465926037194/0001104659-26-037194-index.html) — published 2026-03-31; retrieved 2026-10-22T17:53:02.398600+00:00.

[S05] [10-Q 0001610853-26-000007](https://www.sec.gov/Archives/edgar/data/1610853/000161085326000007/0001610853-26-000007-index.html) — published 2026-08-14; retrieved 2026-10-22T17:53:02.398600+00:00.

[S06] [10-K 0001558370-25-003619](https://www.sec.gov/Archives/edgar/data/1610853/000155837025003619/0001558370-25-003619-index.html) — published 2025-03-25; retrieved 2026-10-22T17:53:02.398600+00:00.

[S07] [10-K 0001558370-24-004260](https://www.sec.gov/Archives/edgar/data/1610853/000155837024004260/0001558370-24-004260-index.html) — published 2024-03-28; retrieved 2026-10-22T17:53:02.398600+00:00.

[S08] [10-K 0001558370-23-003338](https://www.sec.gov/Archives/edgar/data/1610853/000155837023003338/0001558370-23-003338-index.html) — published 2023-03-09; retrieved 2026-10-22T17:53:02.398600+00:00.

[S09] [10-Q 0001104659-26-062611](https://www.sec.gov/Archives/edgar/data/1610853/000110465926062611/0001104659-26-062611-index.html) — published 2026-05-15; retrieved 2026-10-22T17:53:02.398600+00:00.

[S10] [10-Q 0001104659-25-113714](https://www.sec.gov/Archives/edgar/data/1610853/000110465925113714/0001104659-25-113714-index.html) — published 2025-11-18; retrieved 2026-10-22T17:53:02.398600+00:00.

[S11] [10-Q 0001558370-25-011568](https://www.sec.gov/Archives/edgar/data/1610853/000155837025011568/0001558370-25-011568-index.html) — published 2025-08-14; retrieved 2026-10-22T17:53:02.398600+00:00.

[S12] [10-Q 0001558370-25-006120](https://www.sec.gov/Archives/edgar/data/1610853/000155837025006120/0001558370-25-006120-index.html) — published 2025-05-01; retrieved 2026-10-22T17:53:02.398600+00:00.

[S13] [10-Q 0001558370-24-015344](https://www.sec.gov/Archives/edgar/data/1610853/000155837024015344/0001558370-24-015344-index.html) — published 2024-11-12; retrieved 2026-10-22T17:53:02.398600+00:00.

[S14] [10-Q 0001558370-24-011905](https://www.sec.gov/Archives/edgar/data/1610853/000155837024011905/0001558370-24-011905-index.html) — published 2024-08-12; retrieved 2026-10-22T17:53:02.398600+00:00.

[S15] [10-Q 0001558370-24-007971](https://www.sec.gov/Archives/edgar/data/1610853/000155837024007971/0001558370-24-007971-index.html) — published 2024-05-13; retrieved 2026-10-22T17:53:02.398600+00:00.

[S16] [10-Q 0001558370-23-018605](https://www.sec.gov/Archives/edgar/data/1610853/000155837023018605/0001558370-23-018605-index.html) — published 2023-11-09; retrieved 2026-10-22T17:53:02.398600+00:00.

[S17] [424B5 0001610853-26-000010](https://www.sec.gov/Archives/edgar/data/1610853/000161085326000010/0001610853-26-000010-index.html) — published 2026-09-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [8-K 0001610853-26-000008](https://www.sec.gov/Archives/edgar/data/1610853/000161085326000008/0001610853-26-000008-index.html) — published 2026-09-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [SCHEDULE 13D/A 0001213900-26-100250](https://www.sec.gov/Archives/edgar/data/1610853/000121390026100250/0001213900-26-100250-index.html) — published 2026-09-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [4 0002127311-26-000006](https://www.sec.gov/Archives/edgar/data/1610853/000212731126000006/0002127311-26-000006-index.html) — published 2026-08-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [SCHEDULE 13G/A 0001104659-26-100294](https://www.sec.gov/Archives/edgar/data/1610853/000110465926100294/0001104659-26-100294-index.html) — published 2026-08-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S22] [10-Q 0001610853-26-000007](https://www.sec.gov/Archives/edgar/data/1610853/000161085326000007/0001610853-26-000007-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S23] [8-K 0001610853-26-000005](https://www.sec.gov/Archives/edgar/data/1610853/000161085326000005/0001610853-26-000005-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S24] [4 0002086036-26-000006](https://www.sec.gov/Archives/edgar/data/1610853/000208603626000006/0002086036-26-000006-index.html) — published 2026-08-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S25] [4 0001104659-26-082801](https://www.sec.gov/Archives/edgar/data/1610853/000110465926082801/0001104659-26-082801-index.html) — published 2026-07-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S26] [3 0001104659-26-082791](https://www.sec.gov/Archives/edgar/data/1610853/000110465926082791/0001104659-26-082791-index.html) — published 2026-07-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S27] [4 0002086128-26-000005](https://www.sec.gov/Archives/edgar/data/1610853/000208612826000005/0002086128-26-000005-index.html) — published 2026-06-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S28] [4 0002086128-26-000003](https://www.sec.gov/Archives/edgar/data/1610853/000208612826000003/0002086128-26-000003-index.html) — published 2026-06-04; retrieved 2026-10-23T08:33:02.691743+00:00.

[S29] [8-K 0001104659-26-068370](https://www.sec.gov/Archives/edgar/data/1610853/000110465926068370/0001104659-26-068370-index.html) — published 2026-05-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S30] [424B5 0001104659-26-068348](https://www.sec.gov/Archives/edgar/data/1610853/000110465926068348/0001104659-26-068348-index.html) — published 2026-05-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S31] [SD 0001104659-26-068243](https://www.sec.gov/Archives/edgar/data/1610853/000110465926068243/0001104659-26-068243-index.html) — published 2026-05-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S32] [4 0002131577-26-000005](https://www.sec.gov/Archives/edgar/data/1610853/000213157726000005/0002131577-26-000005-index.html) — published 2026-05-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S33] [4 0002130655-26-000005](https://www.sec.gov/Archives/edgar/data/1610853/000213065526000005/0002130655-26-000005-index.html) — published 2026-05-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S34] [4 0001340555-26-000007](https://www.sec.gov/Archives/edgar/data/1610853/000134055526000007/0001340555-26-000007-index.html) — published 2026-05-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S35] [4/A 0001340555-26-000005](https://www.sec.gov/Archives/edgar/data/1610853/000134055526000005/0001340555-26-000005-index.html) — published 2026-05-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S36] [SCHEDULE 13D/A 0001213900-26-061030](https://www.sec.gov/Archives/edgar/data/1610853/000121390026061030/0001213900-26-061030-index.html) — published 2026-05-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S37] [4 0001075380-26-000006](https://www.sec.gov/Archives/edgar/data/1610853/000107538026000006/0001075380-26-000006-index.html) — published 2026-05-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S38] [4/A 0001075380-26-000004](https://www.sec.gov/Archives/edgar/data/1610853/000107538026000004/0001075380-26-000004-index.html) — published 2026-05-26; retrieved 2026-10-23T08:33:02.691743+00:00.

[S39] [8-K 0001104659-26-065815](https://www.sec.gov/Archives/edgar/data/1610853/000110465926065815/0001104659-26-065815-index.html) — published 2026-05-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S40] [4 0001104659-26-065600](https://www.sec.gov/Archives/edgar/data/1610853/000110465926065600/0001104659-26-065600-index.html) — published 2026-05-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S41] [3 0001104659-26-065598](https://www.sec.gov/Archives/edgar/data/1610853/000110465926065598/0001104659-26-065598-index.html) — published 2026-05-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S42] [DEFA14A 0001104659-26-062844](https://www.sec.gov/Archives/edgar/data/1610853/000110465926062844/0001104659-26-062844-index.html) — published 2026-05-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S43] [SCHEDULE 13G/A 0002048251-26-003782](https://www.sec.gov/Archives/edgar/data/1610853/000204825126003782/0002048251-26-003782-index.html) — published 2026-05-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S44] [10-Q 0001104659-26-062611](https://www.sec.gov/Archives/edgar/data/1610853/000110465926062611/0001104659-26-062611-index.html) — published 2026-05-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S45] [8-K 0001104659-26-062534](https://www.sec.gov/Archives/edgar/data/1610853/000110465926062534/0001104659-26-062534-index.html) — published 2026-05-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S46] [SCHEDULE 13D/A 0002087954-26-000002](https://www.sec.gov/Archives/edgar/data/1610853/000208795426000002/0002087954-26-000002-index.html) — published 2026-05-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S47] [4 0002086036-26-000002](https://www.sec.gov/Archives/edgar/data/1610853/000208603626000002/0002086036-26-000002-index.html) — published 2026-05-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S48] [SCHEDULE 13G/A 0001104659-26-057882](https://www.sec.gov/Archives/edgar/data/1610853/000110465926057882/0001104659-26-057882-index.html) — published 2026-05-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S49] [DEFA14A 0001104659-26-054183](https://www.sec.gov/Archives/edgar/data/1610853/000110465926054183/0001104659-26-054183-index.html) — published 2026-05-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S50] [3 0002131577-26-000003](https://www.sec.gov/Archives/edgar/data/1610853/000213157726000003/0002131577-26-000003-index.html) — published 2026-04-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S51] [3/A 0002130655-26-000003](https://www.sec.gov/Archives/edgar/data/1610853/000213065526000003/0002130655-26-000003-index.html) — published 2026-04-30; retrieved 2026-10-23T08:33:02.691743+00:00.

[S52] [424B5 0001104659-26-049074](https://www.sec.gov/Archives/edgar/data/1610853/000110465926049074/0001104659-26-049074-index.html) — published 2026-04-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S53] [8-K 0001104659-26-049070](https://www.sec.gov/Archives/edgar/data/1610853/000110465926049070/0001104659-26-049070-index.html) — published 2026-04-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [8-K 0001104659-26-048625](https://www.sec.gov/Archives/edgar/data/1610853/000110465926048625/0001104659-26-048625-index.html) — published 2026-04-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S55] [ARS 0001104659-26-042868](https://www.sec.gov/Archives/edgar/data/1610853/000110465926042868/0001104659-26-042868-index.html) — published 2026-04-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S56] [8-K 0001104659-26-042666](https://www.sec.gov/Archives/edgar/data/1610853/000110465926042666/0001104659-26-042666-index.html) — published 2026-04-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S57] [DEF 14A 0001104659-26-041970](https://www.sec.gov/Archives/edgar/data/1610853/000110465926041970/0001104659-26-041970-index.html) — published 2026-04-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S58] [8-K 0001104659-26-041571](https://www.sec.gov/Archives/edgar/data/1610853/000110465926041571/0001104659-26-041571-index.html) — published 2026-04-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S59] [EFFECT 9999999995-26-001114](https://www.sec.gov/Archives/edgar/data/1610853/999999999526001114/9999999995-26-001114-index.html) — published 2026-04-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S60] [EFFECT 9999999995-26-001113](https://www.sec.gov/Archives/edgar/data/1610853/999999999526001113/9999999995-26-001113-index.html) — published 2026-04-08; retrieved 2026-10-23T08:33:02.691743+00:00.

[S61] [3 0002127311-26-000002](https://www.sec.gov/Archives/edgar/data/1610853/000212731126000002/0002127311-26-000002-index.html) — published 2026-04-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S62] [4 0001537711-26-000002](https://www.sec.gov/Archives/edgar/data/1610853/000153771126000002/0001537711-26-000002-index.html) — published 2026-04-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S63] [4 0001340555-26-000002](https://www.sec.gov/Archives/edgar/data/1610853/000134055526000002/0001340555-26-000002-index.html) — published 2026-04-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S64] [4 0001215243-26-000003](https://www.sec.gov/Archives/edgar/data/1610853/000121524326000003/0001215243-26-000003-index.html) — published 2026-04-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S65] [4 0001075380-26-000002](https://www.sec.gov/Archives/edgar/data/1610853/000107538026000002/0001075380-26-000002-index.html) — published 2026-04-02; retrieved 2026-10-23T08:33:02.691743+00:00.

[S66] [S-8 0001104659-26-037423](https://www.sec.gov/Archives/edgar/data/1610853/000110465926037423/0001104659-26-037423-index.html) — published 2026-03-31; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261028-40722802424-1`. Dated research changes remain in Git history; review is never inferred from collection.
