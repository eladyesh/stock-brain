---
schema_version: 1
document_type: company_facts
company_id: company-cik-0002079999
cik: 0002079999
company_name: Cardinal Infrastructure Group Inc.
tickers:
- CDNL
status: stub
canonical_reviewed: false
as_of: '2026-10-25'
updated_at: '2026-10-25T13:50:29.910841+00:00'
reviewed_at: null
coverage_release: coverage-20261025-40199010718-1
source_commit: d4303e1efab53027fe4e6e90633e2c69b11c599c
financial_history_available: true
curated_research: null
financial_gap:
  reason: available
  next_action: Retain dated financial evidence and review blocked metrics before analytical
    use.
  observed_forms:
  - 10-K
  - 10-Q
  - '3'
  - '4'
  - 424B4
  - 8-A12B
  - 8-K
  - 8-K/A
  - ARS
  - CERT
  - CORRESP
  - DEF 14A
  - DEFA14A
  - DRS
  - DRS/A
  - DRSLTR
  - EFFECT
  - S-1
  - S-1/A
  - S-1MEF
  - S-8
  - SCHEDULE 13G
  - SCHEDULE 13G/A
  - UPLOAD
input_sources:
  history:
    url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002079999.json
    sha256: 164c9cbd16e840e1dec9d4e473cd5d93853a15e434558153ba8eda33cc511a02
    retrieved_at: '2026-10-22T17:39:41.848518+00:00'
    archive:
      member: CIK0002079999.json
      sha256: 7457a528288f1e3425cba6ffd7370c6c205845aba12761763aa5ae3683c0fdc2
      url: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
    acquisition: operator_supplied_sec_bulk_archive
  submissions:
    url: https://data.sec.gov/submissions/CIK0002079999.json
    sha256: df3af9429d6bb530d3f0d187ed6218572dd968eeff7d5d9944feef15f928f9ce
    retrieved_at: '2026-10-23T08:33:02.691743+00:00'
    archive: &id001
      member: CIK0002079999.json
      sha256: 48514c6807353ac62b2eb8274cfd29e968eeec01123651eedda4c9584b680789
      url: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
    acquisition: operator_supplied_sec_bulk_archive
sources:
- id: S01
  title: nasdaqlisted.txt
  url: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
  published_at: null
  retrieved_at: '2026-10-25T13:45:47.626200+00:00'
  sha256: 59ac9b74ff663c6de40f5c93a54d5e12eb3fbef74f82e8a7cfc1456ad9f969ec
- id: S02
  title: SEC issuer submissions
  url: https://data.sec.gov/submissions/CIK0002079999.json
  published_at: null
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: df3af9429d6bb530d3f0d187ed6218572dd968eeff7d5d9944feef15f928f9ce
- id: S03
  title: SEC CompanyFacts source
  url: https://data.sec.gov/api/xbrl/companyfacts/CIK0002079999.json
  published_at: null
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: 164c9cbd16e840e1dec9d4e473cd5d93853a15e434558153ba8eda33cc511a02
- id: S04
  title: 10-K 0001193125-26-120014
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526120014/0001193125-26-120014-index.html
  published_at: '2026-03-23'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S05
  title: 10-Q 0001193125-26-345109
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526345109/0001193125-26-345109-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S06
  title: 10-Q 0001193125-26-221771
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526221771/0001193125-26-221771-index.html
  published_at: '2026-05-13'
  retrieved_at: '2026-10-22T17:39:41.848518+00:00'
  sha256: null
- id: S07
  title: 8-K 0001193125-26-424737
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526424737/0001193125-26-424737-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S08
  title: SCHEDULE 13G 0000895345-26-000469
  url: https://www.sec.gov/Archives/edgar/data/2079999/000089534526000469/0000895345-26-000469-index.html
  published_at: '2026-10-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S09
  title: 8-K 0001193125-26-410735
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526410735/0001193125-26-410735-index.html
  published_at: '2026-10-01'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S10
  title: 8-K 0001193125-26-389363
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526389363/0001193125-26-389363-index.html
  published_at: '2026-09-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S11
  title: 4 0001213900-26-091325
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026091325/0001213900-26-091325-index.html
  published_at: '2026-08-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S12
  title: 4 0001213900-26-090858
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026090858/0001213900-26-090858-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S13
  title: 4 0001213900-26-090856
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026090856/0001213900-26-090856-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S14
  title: 4 0001213900-26-090855
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026090855/0001213900-26-090855-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S15
  title: 4 0001213900-26-090854
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026090854/0001213900-26-090854-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S16
  title: 4 0001213900-26-090852
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026090852/0001213900-26-090852-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S17
  title: 4 0001213900-26-090850
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026090850/0001213900-26-090850-index.html
  published_at: '2026-08-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S18
  title: SCHEDULE 13G/A 0001109448-26-000244
  url: https://www.sec.gov/Archives/edgar/data/2079999/000110944826000244/0001109448-26-000244-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S19
  title: SCHEDULE 13G 0000938206-26-000043
  url: https://www.sec.gov/Archives/edgar/data/2079999/000093820626000043/0000938206-26-000043-index.html
  published_at: '2026-08-14'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S20
  title: 10-Q 0001193125-26-345109
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526345109/0001193125-26-345109-index.html
  published_at: '2026-08-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S21
  title: 8-K 0001193125-26-343397
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526343397/0001193125-26-343397-index.html
  published_at: '2026-08-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S22
  title: SCHEDULE 13G/A 0000315066-26-001969
  url: https://www.sec.gov/Archives/edgar/data/2079999/000031506626001969/0000315066-26-001969-index.html
  published_at: '2026-08-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S23
  title: SCHEDULE 13G 0002012383-26-002223
  url: https://www.sec.gov/Archives/edgar/data/2079999/000201238326002223/0002012383-26-002223-index.html
  published_at: '2026-07-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S24
  title: 424B4 0001213900-26-072043
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026072043/0001213900-26-072043-index.html
  published_at: '2026-06-25'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S25
  title: EFFECT 9999999995-26-002118
  url: https://www.sec.gov/Archives/edgar/data/2079999/999999999526002118/9999999995-26-002118-index.html
  published_at: '2026-06-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S26
  title: S-1MEF 0001213900-26-071682
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026071682/0001213900-26-071682-index.html
  published_at: '2026-06-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S27
  title: S-1 0001213900-26-070633
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026070633/0001213900-26-070633-index.html
  published_at: '2026-06-22'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S28
  title: DRS 0001213900-26-067407
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026067407/0001213900-26-067407-index.html
  published_at: '2026-06-10'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S29
  title: 4 0001213900-26-066857
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026066857/0001213900-26-066857-index.html
  published_at: '2026-06-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S30
  title: 4 0001213900-26-066856
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026066856/0001213900-26-066856-index.html
  published_at: '2026-06-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S31
  title: 4 0001213900-26-066855
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026066855/0001213900-26-066855-index.html
  published_at: '2026-06-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S32
  title: 4 0001213900-26-066854
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026066854/0001213900-26-066854-index.html
  published_at: '2026-06-09'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S33
  title: 8-K 0001193125-26-259493
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526259493/0001193125-26-259493-index.html
  published_at: '2026-06-05'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S34
  title: 4 0001213900-26-062942
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026062942/0001213900-26-062942-index.html
  published_at: '2026-05-29'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S35
  title: SCHEDULE 13G/A 0001109448-26-000167
  url: https://www.sec.gov/Archives/edgar/data/2079999/000110944826000167/0001109448-26-000167-index.html
  published_at: '2026-05-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S36
  title: SCHEDULE 13G/A 0001193805-26-000633
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119380526000633/0001193805-26-000633-index.html
  published_at: '2026-05-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S37
  title: 10-Q 0001193125-26-221771
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526221771/0001193125-26-221771-index.html
  published_at: '2026-05-13'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S38
  title: 8-K 0001193125-26-218102
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526218102/0001193125-26-218102-index.html
  published_at: '2026-05-12'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S39
  title: 4 0001213900-26-054547
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026054547/0001213900-26-054547-index.html
  published_at: '2026-05-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S40
  title: 4 0001213900-26-054546
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026054546/0001213900-26-054546-index.html
  published_at: '2026-05-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S41
  title: 4 0001213900-26-054545
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026054545/0001213900-26-054545-index.html
  published_at: '2026-05-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S42
  title: 4 0001213900-26-054544
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026054544/0001213900-26-054544-index.html
  published_at: '2026-05-11'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S43
  title: 8-K/A 0001193125-26-209128
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526209128/0001193125-26-209128-index.html
  published_at: '2026-05-06'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S44
  title: ARS 0001193125-26-177474
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526177474/0001193125-26-177474-index.html
  published_at: '2026-04-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S45
  title: DEFA14A 0001193125-26-177422
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526177422/0001193125-26-177422-index.html
  published_at: '2026-04-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S46
  title: DEF 14A 0001193125-26-177393
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526177393/0001193125-26-177393-index.html
  published_at: '2026-04-24'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S47
  title: SCHEDULE 13G/A 0000814133-26-000064
  url: https://www.sec.gov/Archives/edgar/data/2079999/000081413326000064/0000814133-26-000064-index.html
  published_at: '2026-04-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S48
  title: 3 0001213900-26-044210
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026044210/0001213900-26-044210-index.html
  published_at: '2026-04-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S49
  title: 3 0001213900-26-044209
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026044209/0001213900-26-044209-index.html
  published_at: '2026-04-15'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S50
  title: 4 0001213900-26-035634
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026035634/0001213900-26-035634-index.html
  published_at: '2026-03-27'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S51
  title: 10-K 0001193125-26-120014
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526120014/0001193125-26-120014-index.html
  published_at: '2026-03-23'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S52
  title: 8-K 0001193125-26-115080
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526115080/0001193125-26-115080-index.html
  published_at: '2026-03-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S53
  title: 8-K 0001193125-26-114334
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526114334/0001193125-26-114334-index.html
  published_at: '2026-03-18'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S54
  title: 8-K 0001213900-26-018087
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026018087/0001213900-26-018087-index.html
  published_at: '2026-02-19'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S55
  title: SCHEDULE 13G 0001213900-26-017486
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026017486/0001213900-26-017486-index.html
  published_at: '2026-02-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
- id: S56
  title: SCHEDULE 13G 0001213900-26-017484
  url: https://www.sec.gov/Archives/edgar/data/2079999/000121390026017484/0001213900-26-017484-index.html
  published_at: '2026-02-17'
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: null
issuer_classification:
  cik: 0002079999
  classification_status: reported_sic
  entity_type: operating
  name: Cardinal Infrastructure Group Inc.
  sic: '1600'
  sic_description: Heavy Construction Other Than Bldg Const - Contractors
classification_source:
  acquisition: operator_supplied_sec_bulk_archive
  archive: *id001
  retrieved_at: '2026-10-23T08:33:02.691743+00:00'
  sha256: df3af9429d6bb530d3f0d187ed6218572dd968eeff7d5d9944feef15f928f9ce
  url: https://data.sec.gov/submissions/CIK0002079999.json
listings:
- ticker: CDNL
  exchange: NASDAQ
  instrument_type: common_stock
research_filings:
- accession: 0001193125-26-120014
  filed: '2026-03-23'
  form: 10-K
  period_end: '2025-12-31'
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526120014/0001193125-26-120014-index.html
- accession: 0001193125-26-345109
  filed: '2026-08-12'
  form: 10-Q
  period_end: '2026-06-30'
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526345109/0001193125-26-345109-index.html
- accession: 0001193125-26-177393
  filed: '2026-04-24'
  form: DEF 14A
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526177393/0001193125-26-177393-index.html
- accession: 0001193125-26-424737
  filed: '2026-10-19'
  form: 8-K
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526424737/0001193125-26-424737-index.html
- accession: 0001193125-26-209128
  filed: '2026-05-06'
  form: 8-K/A
  url: https://www.sec.gov/Archives/edgar/data/2079999/000119312526209128/0001193125-26-209128-index.html
research_progress:
  stage: pending
  input_sha256: 94a162606c94bb9d2d7a74375ee5c84fe175d76226477d18bab022751c37b83a
  last_attempt_at: null
  last_success_at: null
  next_retry_at: null
  source_set_current: false
  evidence_topics: []
  derived_observations: 5
  model_draft: false
  reviewed: false
---
# CDNL — Cardinal Infrastructure Group Inc.

> Automatically maintained factual stub. Substantive company research is incomplete.

[All companies](../../INDEX.md)


## Business overview

Reported issuer name: **Cardinal Infrastructure Group Inc.**. Stable SEC CIK: **0002079999**. [S02]

The directory links the following current stock listings to this issuer. Classification is provisional where indicated.

| Symbol | Exchange | Instrument | Identity revision | Evidence |
| --- | --- | --- | ---: | --- |
| CDNL | NASDAQ | common_stock | 1 | [S01] |

Not available: a reviewed explanation of the business, products, customers and competitive position.

## Revenue model and segments

Not available: substantive research has not been completed. Describe revenue streams, segments, geographic exposure, pricing, and recurring versus transactional revenue. Date every mix figure.

## Products and services

Not available: substantive research has not been completed. Describe the main products, customer problems solved, distribution, and product dependencies.

## Customers and end markets

Not available: substantive research has not been completed. Describe buyers, use cases, concentration, contract duration, and end-market exposure. Do not infer undisclosed customer names.

## Industry and value chain

SEC-reported SIC **1600**: Heavy Construction Other Than Bldg Const - Contractors. [S02]

This is reported industry metadata, not an official GICS assignment or a completed analysis of the value chain. Suppliers, competitors and customers still require separate evidence.

## Competitive landscape

Not available: substantive research has not been completed. Identify direct competitors and alternatives. Compare specific products or business segments, with sources.

## Moat and differentiation

Not available: substantive research has not been completed. Separate evidence from interpretation when assessing switching costs, cost advantages, intellectual property, scale, or network effects.

## Growth drivers

Not available: substantive research has not been completed. Explain the mechanisms behind possible growth, their dependencies, and what would disprove them. Label forecasts and assumptions.

## Financial performance

Derived observation: Operating margin was 8.86% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S51]
Formula: `operating_income / revenue * 100`. Inputs: operating_income=40404407 USD (OperatingIncomeLoss), revenue=456045369 USD (RevenueFromContractWithCustomerIncludingAssessedTax).

Derived observation: Net margin was 4.97% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S51]
Formula: `net_income / revenue * 100`. Inputs: net_income=22686057 USD (NetIncomeLoss), revenue=456045369 USD (RevenueFromContractWithCustomerIncludingAssessedTax).

Derived observation: Free cash flow margin was -1.30% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S51]
Formula: `free_cash_flow / revenue * 100`. Inputs: free_cash_flow=-5914341 USD (NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment), revenue=456045369 USD (RevenueFromContractWithCustomerIncludingAssessedTax).

Derived observation: Stock compensation / revenue was 1.29% for 2025-01-01 to 2025-12-31 (US GAAP inputs). [S51]
Formula: `stock_based_compensation / revenue * 100`. Inputs: stock_based_compensation=5868592 USD (ShareBasedCompensation), revenue=456045369 USD (RevenueFromContractWithCustomerIncludingAssessedTax).

Derived observation: Operating cash flow / net income was 1.67x for the year ended 2025-12-31. Working capital and non-cash adjustments require separate filing analysis. [S51]
Formula: `operating_cash_flow / net_income`. Inputs: operating_cash_flow=37900887 USD (NetCashProvidedByUsedInOperatingActivities), net_income=22686057 USD (NetIncomeLoss).

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -43,815,228 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S04] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| free_cash_flow | -5,914,341 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S04] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 22,686,057 | USD | US GAAP / reported | NetIncomeLoss | [S04] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 31,093,483 | USD | US GAAP / reported | ProfitLoss | [S04] |
| operating_cash_flow | 37,900,887 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S04] |
| operating_income | 40,404,407 | USD | US GAAP / reported | OperatingIncomeLoss | [S04] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 456,045,369 | USD | US GAAP / reported | RevenueFromContractWithCustomerIncludingAssessedTax | [S04] |
| shares_basic | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_diluted | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| stock_based_compensation | 5,868,592 | USD | US GAAP / reported | ShareBasedCompensation | [S04] |

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -24,667,076 | USD | US GAAP / derived | PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S06] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S05] |
| free_cash_flow | -11,988,671 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S06] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 4,675,367 | USD | US GAAP / reported | NetIncomeLoss | [S05] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 11,148,306 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | 12,678,405 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S06] |
| operating_income | 15,478,448 | USD | US GAAP / reported | OperatingIncomeLoss | [S05] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 226,934,438 | USD | US GAAP / reported | RevenueFromContractWithCustomerIncludingAssessedTax | [S05] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S05] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S05] |
| stock_based_compensation | 269,665 | USD | US GAAP / derived | ShareBasedCompensation; cross_filing_derivation, standalone_quarter_from_cumulative_difference | [S05] [S06] |

### quarterly: 2026-01-01 to 2026-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| capex | -9,317,980 | USD | US GAAP / reported | PaymentsToAcquirePropertyPlantAndEquipment; Cash outflow = negative of reported PaymentsToAcquirePropertyPlantAndEquipment; source value retained. | [S06] |
| cost_of_revenue | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| eps_basic | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareBasic; share_split_and_corporate_action_basis_unverified | [S06] |
| eps_diluted | Unavailable / blocked | USD/shares | US GAAP / reported / not model usable | EarningsPerShareDiluted; share_split_and_corporate_action_basis_unverified | [S06] |
| free_cash_flow | -961 | USD | US GAAP / derived | NetCashProvidedByUsedInOperatingActivities + PaymentsToAcquirePropertyPlantAndEquipment | [S06] |
| gross_profit | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income | 3,418,438 | USD | US GAAP / reported | NetIncomeLoss | [S06] |
| net_income_common | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| net_income_including_noncontrolling_interests | 11,481,036 | USD | US GAAP / reported | ProfitLoss | [S05] |
| operating_cash_flow | 9,317,019 | USD | US GAAP / reported | NetCashProvidedByUsedInOperatingActivities | [S06] |
| operating_income | 14,780,141 | USD | US GAAP / reported | OperatingIncomeLoss | [S06] |
| purchases_of_productive_assets | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| revenue | 167,508,716 | USD | US GAAP / reported | RevenueFromContractWithCustomerIncludingAssessedTax | [S06] |
| shares_basic | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfSharesOutstandingBasic; share_split_and_corporate_action_basis_unverified | [S06] |
| shares_diluted | Unavailable / blocked | shares | US GAAP / reported / not model usable | WeightedAverageNumberOfDilutedSharesOutstanding; share_split_and_corporate_action_basis_unverified | [S06] |
| stock_based_compensation | 191,852 | USD | US GAAP / reported | ShareBasedCompensation | [S06] |

## Balance sheet and capital allocation

Evidence cutoff: 2026-10-22. Source retrieved: 2026-10-22T17:39:41.848518+00:00. [S03]

US GAAP facts and explicitly identified derivations. Values use the units shown, without scaling. Unavailable, conflicted or unverified cells remain blocked. No forecasts, prices, valuation multiples or research approval are inferred. Instant balance-sheet values are as of the period end; flow values cover the displayed interval.


### annual: 2025-01-01 to 2025-12-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | NotesPayableCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermNotesPayable; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2026-04-01 to 2026-06-30

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | NotesPayableCurrent; debt_scope_requires_filing_review | [S05] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermNotesPayable; debt_scope_requires_filing_review | [S05] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_borrowings | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| short_term_investments | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |

### quarterly: 2026-01-01 to 2026-03-31

| Metric | Value | Unit | Basis / status | Definition / quality | Filing evidence |
| --- | ---: | --- | --- | --- | --- |
| cash_and_equivalents | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| debt_current | Unavailable / blocked | USD | US GAAP / reported / not model usable | NotesPayableCurrent; debt_scope_requires_filing_review | [S06] |
| debt_noncurrent | Unavailable / blocked | USD | US GAAP / reported / not model usable | LongTermNotesPayable; debt_scope_requires_filing_review | [S06] |
| debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| long_term_debt_total | Unavailable / blocked | USD | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
| shares_outstanding | Unavailable / blocked | shares | US GAAP / missing_required_source / not model usable |  | No eligible evidence |
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
- Collector status: quality_review_required; last action: new_financial_filing; last checked: 2026-10-24T13:36:39.562200+00:00.

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

Calculation gaps: revenue: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. net_income: annual growth withheld because periods, definitions or a positive prior denominator are not verified. operating_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified. free_cash_flow: annual growth withheld because periods, definitions or a positive prior denominator are not verified.

## Relationships and themes

Not available: substantive research has not been completed. Link relevant companies and cross-sector themes. State the relationship type and supporting source; never imply all theme members are competitors.

## Recent developments

Latest 50 filing metadata records of 99 retained records. A filing link is evidence of submission, not evidence that the document was read or analyzed.

| Filed | Form | Accession | Period end | Filing |
| --- | --- | --- | --- | --- |
| 2026-10-19 | 8-K | 0001193125-26-424737 | — | [S07] |
| 2026-10-19 | SCHEDULE 13G | 0000895345-26-000469 | — | [S08] |
| 2026-10-01 | 8-K | 0001193125-26-410735 | — | [S09] |
| 2026-09-11 | 8-K | 0001193125-26-389363 | — | [S10] |
| 2026-08-18 | 4 | 0001213900-26-091325 | — | [S11] |
| 2026-08-17 | 4 | 0001213900-26-090858 | — | [S12] |
| 2026-08-17 | 4 | 0001213900-26-090856 | — | [S13] |
| 2026-08-17 | 4 | 0001213900-26-090855 | — | [S14] |
| 2026-08-17 | 4 | 0001213900-26-090854 | — | [S15] |
| 2026-08-17 | 4 | 0001213900-26-090852 | — | [S16] |
| 2026-08-17 | 4 | 0001213900-26-090850 | — | [S17] |
| 2026-08-14 | SCHEDULE 13G/A | 0001109448-26-000244 | — | [S18] |
| 2026-08-14 | SCHEDULE 13G | 0000938206-26-000043 | — | [S19] |
| 2026-08-12 | 10-Q | 0001193125-26-345109 | — | [S20] |
| 2026-08-11 | 8-K | 0001193125-26-343397 | — | [S21] |
| 2026-08-06 | SCHEDULE 13G/A | 0000315066-26-001969 | — | [S22] |
| 2026-07-27 | SCHEDULE 13G | 0002012383-26-002223 | — | [S23] |
| 2026-06-25 | 424B4 | 0001213900-26-072043 | — | [S24] |
| 2026-06-24 | EFFECT | 9999999995-26-002118 | — | [S25] |
| 2026-06-24 | S-1MEF | 0001213900-26-071682 | — | [S26] |
| 2026-06-22 | S-1 | 0001213900-26-070633 | — | [S27] |
| 2026-06-10 | DRS | 0001213900-26-067407 | — | [S28] |
| 2026-06-09 | 4 | 0001213900-26-066857 | — | [S29] |
| 2026-06-09 | 4 | 0001213900-26-066856 | — | [S30] |
| 2026-06-09 | 4 | 0001213900-26-066855 | — | [S31] |
| 2026-06-09 | 4 | 0001213900-26-066854 | — | [S32] |
| 2026-06-05 | 8-K | 0001193125-26-259493 | — | [S33] |
| 2026-05-29 | 4 | 0001213900-26-062942 | — | [S34] |
| 2026-05-18 | SCHEDULE 13G/A | 0001109448-26-000167 | — | [S35] |
| 2026-05-15 | SCHEDULE 13G/A | 0001193805-26-000633 | — | [S36] |
| 2026-05-13 | 10-Q | 0001193125-26-221771 | — | [S37] |
| 2026-05-12 | 8-K | 0001193125-26-218102 | — | [S38] |
| 2026-05-11 | 4 | 0001213900-26-054547 | — | [S39] |
| 2026-05-11 | 4 | 0001213900-26-054546 | — | [S40] |
| 2026-05-11 | 4 | 0001213900-26-054545 | — | [S41] |
| 2026-05-11 | 4 | 0001213900-26-054544 | — | [S42] |
| 2026-05-06 | 8-K/A | 0001193125-26-209128 | — | [S43] |
| 2026-04-24 | ARS | 0001193125-26-177474 | — | [S44] |
| 2026-04-24 | DEFA14A | 0001193125-26-177422 | — | [S45] |
| 2026-04-24 | DEF 14A | 0001193125-26-177393 | — | [S46] |
| 2026-04-23 | SCHEDULE 13G/A | 0000814133-26-000064 | — | [S47] |
| 2026-04-15 | 3 | 0001213900-26-044210 | — | [S48] |
| 2026-04-15 | 3 | 0001213900-26-044209 | — | [S49] |
| 2026-03-27 | 4 | 0001213900-26-035634 | — | [S50] |
| 2026-03-23 | 10-K | 0001193125-26-120014 | — | [S51] |
| 2026-03-19 | 8-K | 0001193125-26-115080 | — | [S52] |
| 2026-03-18 | 8-K | 0001193125-26-114334 | — | [S53] |
| 2026-02-19 | 8-K | 0001213900-26-018087 | — | [S54] |
| 2026-02-17 | SCHEDULE 13G | 0001213900-26-017486 | — | [S55] |
| 2026-02-17 | SCHEDULE 13G | 0001213900-26-017484 | — | [S56] |

## Sources and change log

[S01] [nasdaqlisted.txt](https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt) — published not supplied; retrieved 2026-10-25T13:45:47.626200+00:00.

[S02] [SEC issuer submissions](https://data.sec.gov/submissions/CIK0002079999.json) — published not supplied; retrieved 2026-10-23T08:33:02.691743+00:00.

[S03] [SEC CompanyFacts source](https://data.sec.gov/api/xbrl/companyfacts/CIK0002079999.json) — published not supplied; retrieved 2026-10-22T17:39:41.848518+00:00.

[S04] [10-K 0001193125-26-120014](https://www.sec.gov/Archives/edgar/data/2079999/000119312526120014/0001193125-26-120014-index.html) — published 2026-03-23; retrieved 2026-10-22T17:39:41.848518+00:00.

[S05] [10-Q 0001193125-26-345109](https://www.sec.gov/Archives/edgar/data/2079999/000119312526345109/0001193125-26-345109-index.html) — published 2026-08-12; retrieved 2026-10-22T17:39:41.848518+00:00.

[S06] [10-Q 0001193125-26-221771](https://www.sec.gov/Archives/edgar/data/2079999/000119312526221771/0001193125-26-221771-index.html) — published 2026-05-13; retrieved 2026-10-22T17:39:41.848518+00:00.

[S07] [8-K 0001193125-26-424737](https://www.sec.gov/Archives/edgar/data/2079999/000119312526424737/0001193125-26-424737-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S08] [SCHEDULE 13G 0000895345-26-000469](https://www.sec.gov/Archives/edgar/data/2079999/000089534526000469/0000895345-26-000469-index.html) — published 2026-10-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S09] [8-K 0001193125-26-410735](https://www.sec.gov/Archives/edgar/data/2079999/000119312526410735/0001193125-26-410735-index.html) — published 2026-10-01; retrieved 2026-10-23T08:33:02.691743+00:00.

[S10] [8-K 0001193125-26-389363](https://www.sec.gov/Archives/edgar/data/2079999/000119312526389363/0001193125-26-389363-index.html) — published 2026-09-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S11] [4 0001213900-26-091325](https://www.sec.gov/Archives/edgar/data/2079999/000121390026091325/0001213900-26-091325-index.html) — published 2026-08-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S12] [4 0001213900-26-090858](https://www.sec.gov/Archives/edgar/data/2079999/000121390026090858/0001213900-26-090858-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S13] [4 0001213900-26-090856](https://www.sec.gov/Archives/edgar/data/2079999/000121390026090856/0001213900-26-090856-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S14] [4 0001213900-26-090855](https://www.sec.gov/Archives/edgar/data/2079999/000121390026090855/0001213900-26-090855-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S15] [4 0001213900-26-090854](https://www.sec.gov/Archives/edgar/data/2079999/000121390026090854/0001213900-26-090854-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S16] [4 0001213900-26-090852](https://www.sec.gov/Archives/edgar/data/2079999/000121390026090852/0001213900-26-090852-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S17] [4 0001213900-26-090850](https://www.sec.gov/Archives/edgar/data/2079999/000121390026090850/0001213900-26-090850-index.html) — published 2026-08-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S18] [SCHEDULE 13G/A 0001109448-26-000244](https://www.sec.gov/Archives/edgar/data/2079999/000110944826000244/0001109448-26-000244-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S19] [SCHEDULE 13G 0000938206-26-000043](https://www.sec.gov/Archives/edgar/data/2079999/000093820626000043/0000938206-26-000043-index.html) — published 2026-08-14; retrieved 2026-10-23T08:33:02.691743+00:00.

[S20] [10-Q 0001193125-26-345109](https://www.sec.gov/Archives/edgar/data/2079999/000119312526345109/0001193125-26-345109-index.html) — published 2026-08-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S21] [8-K 0001193125-26-343397](https://www.sec.gov/Archives/edgar/data/2079999/000119312526343397/0001193125-26-343397-index.html) — published 2026-08-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S22] [SCHEDULE 13G/A 0000315066-26-001969](https://www.sec.gov/Archives/edgar/data/2079999/000031506626001969/0000315066-26-001969-index.html) — published 2026-08-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S23] [SCHEDULE 13G 0002012383-26-002223](https://www.sec.gov/Archives/edgar/data/2079999/000201238326002223/0002012383-26-002223-index.html) — published 2026-07-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S24] [424B4 0001213900-26-072043](https://www.sec.gov/Archives/edgar/data/2079999/000121390026072043/0001213900-26-072043-index.html) — published 2026-06-25; retrieved 2026-10-23T08:33:02.691743+00:00.

[S25] [EFFECT 9999999995-26-002118](https://www.sec.gov/Archives/edgar/data/2079999/999999999526002118/9999999995-26-002118-index.html) — published 2026-06-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S26] [S-1MEF 0001213900-26-071682](https://www.sec.gov/Archives/edgar/data/2079999/000121390026071682/0001213900-26-071682-index.html) — published 2026-06-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S27] [S-1 0001213900-26-070633](https://www.sec.gov/Archives/edgar/data/2079999/000121390026070633/0001213900-26-070633-index.html) — published 2026-06-22; retrieved 2026-10-23T08:33:02.691743+00:00.

[S28] [DRS 0001213900-26-067407](https://www.sec.gov/Archives/edgar/data/2079999/000121390026067407/0001213900-26-067407-index.html) — published 2026-06-10; retrieved 2026-10-23T08:33:02.691743+00:00.

[S29] [4 0001213900-26-066857](https://www.sec.gov/Archives/edgar/data/2079999/000121390026066857/0001213900-26-066857-index.html) — published 2026-06-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S30] [4 0001213900-26-066856](https://www.sec.gov/Archives/edgar/data/2079999/000121390026066856/0001213900-26-066856-index.html) — published 2026-06-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S31] [4 0001213900-26-066855](https://www.sec.gov/Archives/edgar/data/2079999/000121390026066855/0001213900-26-066855-index.html) — published 2026-06-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S32] [4 0001213900-26-066854](https://www.sec.gov/Archives/edgar/data/2079999/000121390026066854/0001213900-26-066854-index.html) — published 2026-06-09; retrieved 2026-10-23T08:33:02.691743+00:00.

[S33] [8-K 0001193125-26-259493](https://www.sec.gov/Archives/edgar/data/2079999/000119312526259493/0001193125-26-259493-index.html) — published 2026-06-05; retrieved 2026-10-23T08:33:02.691743+00:00.

[S34] [4 0001213900-26-062942](https://www.sec.gov/Archives/edgar/data/2079999/000121390026062942/0001213900-26-062942-index.html) — published 2026-05-29; retrieved 2026-10-23T08:33:02.691743+00:00.

[S35] [SCHEDULE 13G/A 0001109448-26-000167](https://www.sec.gov/Archives/edgar/data/2079999/000110944826000167/0001109448-26-000167-index.html) — published 2026-05-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S36] [SCHEDULE 13G/A 0001193805-26-000633](https://www.sec.gov/Archives/edgar/data/2079999/000119380526000633/0001193805-26-000633-index.html) — published 2026-05-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S37] [10-Q 0001193125-26-221771](https://www.sec.gov/Archives/edgar/data/2079999/000119312526221771/0001193125-26-221771-index.html) — published 2026-05-13; retrieved 2026-10-23T08:33:02.691743+00:00.

[S38] [8-K 0001193125-26-218102](https://www.sec.gov/Archives/edgar/data/2079999/000119312526218102/0001193125-26-218102-index.html) — published 2026-05-12; retrieved 2026-10-23T08:33:02.691743+00:00.

[S39] [4 0001213900-26-054547](https://www.sec.gov/Archives/edgar/data/2079999/000121390026054547/0001213900-26-054547-index.html) — published 2026-05-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S40] [4 0001213900-26-054546](https://www.sec.gov/Archives/edgar/data/2079999/000121390026054546/0001213900-26-054546-index.html) — published 2026-05-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S41] [4 0001213900-26-054545](https://www.sec.gov/Archives/edgar/data/2079999/000121390026054545/0001213900-26-054545-index.html) — published 2026-05-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S42] [4 0001213900-26-054544](https://www.sec.gov/Archives/edgar/data/2079999/000121390026054544/0001213900-26-054544-index.html) — published 2026-05-11; retrieved 2026-10-23T08:33:02.691743+00:00.

[S43] [8-K/A 0001193125-26-209128](https://www.sec.gov/Archives/edgar/data/2079999/000119312526209128/0001193125-26-209128-index.html) — published 2026-05-06; retrieved 2026-10-23T08:33:02.691743+00:00.

[S44] [ARS 0001193125-26-177474](https://www.sec.gov/Archives/edgar/data/2079999/000119312526177474/0001193125-26-177474-index.html) — published 2026-04-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S45] [DEFA14A 0001193125-26-177422](https://www.sec.gov/Archives/edgar/data/2079999/000119312526177422/0001193125-26-177422-index.html) — published 2026-04-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S46] [DEF 14A 0001193125-26-177393](https://www.sec.gov/Archives/edgar/data/2079999/000119312526177393/0001193125-26-177393-index.html) — published 2026-04-24; retrieved 2026-10-23T08:33:02.691743+00:00.

[S47] [SCHEDULE 13G/A 0000814133-26-000064](https://www.sec.gov/Archives/edgar/data/2079999/000081413326000064/0000814133-26-000064-index.html) — published 2026-04-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S48] [3 0001213900-26-044210](https://www.sec.gov/Archives/edgar/data/2079999/000121390026044210/0001213900-26-044210-index.html) — published 2026-04-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S49] [3 0001213900-26-044209](https://www.sec.gov/Archives/edgar/data/2079999/000121390026044209/0001213900-26-044209-index.html) — published 2026-04-15; retrieved 2026-10-23T08:33:02.691743+00:00.

[S50] [4 0001213900-26-035634](https://www.sec.gov/Archives/edgar/data/2079999/000121390026035634/0001213900-26-035634-index.html) — published 2026-03-27; retrieved 2026-10-23T08:33:02.691743+00:00.

[S51] [10-K 0001193125-26-120014](https://www.sec.gov/Archives/edgar/data/2079999/000119312526120014/0001193125-26-120014-index.html) — published 2026-03-23; retrieved 2026-10-23T08:33:02.691743+00:00.

[S52] [8-K 0001193125-26-115080](https://www.sec.gov/Archives/edgar/data/2079999/000119312526115080/0001193125-26-115080-index.html) — published 2026-03-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S53] [8-K 0001193125-26-114334](https://www.sec.gov/Archives/edgar/data/2079999/000119312526114334/0001193125-26-114334-index.html) — published 2026-03-18; retrieved 2026-10-23T08:33:02.691743+00:00.

[S54] [8-K 0001213900-26-018087](https://www.sec.gov/Archives/edgar/data/2079999/000121390026018087/0001213900-26-018087-index.html) — published 2026-02-19; retrieved 2026-10-23T08:33:02.691743+00:00.

[S55] [SCHEDULE 13G 0001213900-26-017486](https://www.sec.gov/Archives/edgar/data/2079999/000121390026017486/0001213900-26-017486-index.html) — published 2026-02-17; retrieved 2026-10-23T08:33:02.691743+00:00.

[S56] [SCHEDULE 13G 0001213900-26-017484](https://www.sec.gov/Archives/edgar/data/2079999/000121390026017484/0001213900-26-017484-index.html) — published 2026-02-17; retrieved 2026-10-23T08:33:02.691743+00:00.

Source release: `coverage-20261025-40199010718-1`. Dated research changes remain in Git history; review is never inferred from collection.
