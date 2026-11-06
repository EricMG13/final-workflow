## Request

NEWELL BRANDS INC. (issuer id nwl, ticker NWL, Nasdaq-listed registrant, Delaware, Commission File Number 1-9608), as of 2026-11-05, pathway credit_snapshot, public case. Reporting currency USD; the sources print amounts in USD millions. Current period Q3 2026 (quarter ended 2026-09-30); prior period FY2025 (year ended 2025-12-31). Evidence cutoff 2026-11-05.

This module answers one question: can the pinned source set support the selected downstream work (the financial base, business and transaction view, credit synthesis and evidence trace), and what remains blocked. It gives no credit conclusion, legal interpretation or investment opinion, and it does not normalize, reconcile or calculate financial figures. Sufficiency of sources is separate from completion of downstream analysis.

No supplied handoff exists for this module (it is first in the run).

## Sources

### Issuer sources relied on (pinned name and sha256 of the retained text)

| Source name | sha256 | Pages retained |
| --- | --- | --- |
| 10-K_2025-12-31_nwl-20251231.htm.jsonl | dcc793cfdb2b8cc449076ad729ebed59fbf0fa17a270e35dd5b40e5638fe6453 | 150 |
| 10-Q_2026-03-31_nwl-20260331.htm.jsonl | e491b436993330fb987ef524b9f78ce96b1802f1285b9af80a913a9adee3f88d | 38 |
| 10-Q_2026-06-30_nwl-20260630.htm.jsonl | b3b449c8e355a64543631b4a3e69f0acef91c01cc896e4386758050640b5804b | 46 |
| 10-Q_2026-09-30_nwl-20260930.htm.jsonl | 8b58e3ae589a883e4dd1d132d51cbe5455a5976aebd62f8367be4b91ce06fe29 | 54 |
| EX-99.1_2026-05-01_exhibit991_q1xmarchx2026.htm.jsonl | 944b1e0aff94a38b463c337c910588c7aa29def150477cd6c4593c7400267ccd | 16 |
| EX-99.1_2026-07-31_exhibit991_q2xjunex2026.htm.jsonl | 5357537cee17090bbc993249463e8c84756e595916b24485d6cd92a469d185c7 | 18 |
| EX-99.1_2026-10-30_exhibit991_q3xseptemberx20.htm.jsonl | f28d7c981e9628280882affba403a5eab9c05f0b6a106f3147b334e29e9ba0d3 | 19 |

### Run context (not issuer evidence)

| Source name | sha256 | Use |
| --- | --- | --- |
| context (814453-newell-brands-inc-nwl.json) | 6bed67ca32030e1461ea08189ab22687642083ba91fdd1b6bdf65186613803b0 | Dated settings only: as-of 2026-11-05, USD, current period q3-2026, prior period fy-2025. Ratings, quotes, deal terms, peers and research questions are blank; blank is not zero. |

### Supplied handoffs

| Module | sha256 | Note |
| --- | --- | --- |
| None | Not applicable | CP-0 is the first module; no upstream handoff exists. |

The pack also holds a retrieval index (_retrieval.json) that CP-OS ignored as a non-source; it was not used as evidence. A page is the retained text chunk shown as `page:N`, not a printed page. The 10-K, the three 10-Q and the three EX-99.1 files are text conversions of the filed HTML; no image, chart or table-as-image content was inspected.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed documents are adequate for the financial base, business view, credit synthesis and evidence trace, with limits. All four downstream tasks can run, none is blocked. | Medium | Executed debt agreements, interim cash interest and tax paid, covenant levels and a current maturity ladder are not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Filings cover the annual report and three consecutive 2026 quarters, so discrete quarters are available. | Supports a quarter-by-quarter view of leverage and earnings. | High |
| The debt stack changed in the third quarter: new asset-based facility, new senior notes, earlier notes redeemed. | The annual report ladder is stale and must be rebuilt from the latest quarterly debt table. | High |
| Covenant terms are described but covenant levels and reported ratios are not printed. | Headroom cannot be sized from these sources. | Medium |
| Receivables factoring and a financing amendment after quarter end are disclosed. | Liquidity and debt-like claims need care when read from the release. | Medium |

### Readiness view

The effective source set supports the requested work with bounded limitations; none of the four selected consumers is blocked. The pack combines the audited annual report for the year ended 2025-12-31, three unaudited quarterly reports for 2026 and three management earnings releases, all for the single registrant NEWELL BRANDS INC., so identity, perimeter (consolidated, USD millions) and period labels are consistent. The strongest limiting evidence is that the annual report debt ladder and covenant description describe a financing structure that the third-quarter report shows was replaced, that executed indentures and credit agreements are absent, and that the interim reports do not print cash paid for interest or taxes. The next evidence action is to take debt, availability and covenant facts from the latest quarterly report, and to treat the missing items as explicit gaps downstream.

### Source-by-source assessment

| Source | Document family and authority | Entity and perimeter | Period and basis | Version relationship and role |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31 | Audited annual report (Form 10-K), filed statements control | NEWELL BRANDS INC. and subsidiaries, consolidated | Year ended 2025-12-31, with 2024 and 2023 comparatives | Base annual source. Its debt table and maturity ladder are as of 2025-12-31 and are partly superseded by the Q3 2026 report. |
| 10-Q_2026-03-31 | Unaudited quarterly report (Form 10-Q), filed | Consolidated | Three months ended 2026-03-31 | Discrete Q1 2026; describes the earlier Credit Revolver. |
| 10-Q_2026-06-30 | Unaudited quarterly report, filed | Consolidated | Three and six months ended 2026-06-30 | Discrete Q2 2026 and half-year; describes the Credit Revolver in the past tense and the new ABL as a subsequent event. |
| 10-Q_2026-09-30 | Unaudited quarterly report, filed | Consolidated | Three and nine months ended 2026-09-30 | Latest filed period and controlling source for debt at 2026-09-30. |
| EX-99.1_2026-05-01 | Earnings release exhibit, management claims | Consolidated | Q1 2026 | Supporting, attributed narrative and non-GAAP; does not override the filing. |
| EX-99.1_2026-07-31 | Earnings release exhibit, management claims | Consolidated | Q2 2026 | Same role. Discloses tariff recoveries inside reported and normalized results. |
| EX-99.1_2026-10-30 | Earnings release exhibit, management claims | Consolidated | Q3 2026, nine months, trailing twelve months | Same role. Holds the only net debt and trailing-twelve-month normalized EBITDA reconciliation in the pack, and the outlook. |

No source is a base agreement, amendment, waiver or supplement; the sources are not duplicates of one another, and no hash identity between files was relied on. The release and the quarterly report for the same quarter overlap in content, and the filed report controls where they differ; no numerical conflict was tested here because CP-0 does not reconcile. No draft or unsigned document is in the pack.

### Located evidence (exact substrings)

| Topic | Source and locator | Exact quote |
| --- | --- | --- |
| Registrant identity and latest period | 10-Q_2026-09-30 page:1 | "FORM 10-Q ☒ Quarterly Report Pursuant to Section 13 or 15(d) of the Securities Exchange Act of 1934 For the Quarterly Period Ended September 30, 2026" |
| Registrant identity, annual | 10-K_2025-12-31 page:1 | "NEWELL BRANDS INC. (EXACT NAME OF REGISTRANT AS SPECIFIED IN ITS CHARTER)" |
| Latest quarter and nine-month income statement | 10-Q_2026-09-30 page:2 | "Net sales $ 1,873 $ 1,806 $ 5,416 $ 5,307" |
| Annual income statement | 10-K_2025-12-31 page:80 | "Net sales $ 7,204 $ 7,582 $ 8,133" |
| Q2 2026 discrete and six months | 10-Q_2026-06-30 page:2 | "Net sales $ 1,994 $ 1,935 $ 3,543 $ 3,501" |
| Q1 2026 discrete | 10-Q_2026-03-31 page:2 | "Net sales $ 1,549 $ 1,566" |
| Cash flow statement, nine months | 10-Q_2026-09-30 page:3 | "Net cash provided by operating activities 93 103" |
| Facility-level debt table at latest date | 10-Q_2026-09-30 page:17 | "Asset-based revolving credit facility maturing 2031 (a) 215 —" |
| Total debt at latest date | 10-Q_2026-09-30 page:17 | "Total debt 4,841 4,673" |
| Debt at 2025-12-31 with the revolver | 10-K_2025-12-31 page:105 | "Revolving credit facility (a) (b) 130 40" |
| New senior notes | 10-Q_2026-09-30 page:18 | "completed the offering and sale of $600 million of 6.250% senior notes due 2031" |
| New asset-based facility size | 10-Q_2026-09-30 page:19 | "The ABL Credit Agreement provides for the ABL Credit Facility in the amount of up to $800 million" |
| Springing covenant under the new facility | 10-Q_2026-09-30 page:19 | "requires the Company to satisfy a Consolidated Fixed Charge Coverage Ratio (as defined in the ABL Credit Agreement) if borrowings exceed certain levels relative to capacity" |
| Availability and letters of credit on the facility | 10-Q_2026-09-30 page:20 | "resulting in a net availability of approximately $480 million" |
| Weighted average interest rate | 10-Q_2026-09-30 page:21 | "Total debt 6.7 % 6.6 % 6.8 % 6.3 %" |
| Covenant compliance statement | 10-Q_2026-09-30 page:50 | "The Company was in compliance with all of its debt covenants at September 30, 2026." |
| Prior facility maintenance covenants | 10-K_2025-12-31 page:106 | "requires the Company to satisfy financial covenants testing the Company’s Collateral Coverage Ratio and Total Net Leverage Ratio" |
| Step-down of the prior leverage covenant | 10-K_2025-12-31 page:57 | "the Total Net Leverage Ratio covenant, is scheduled to decrease as of the last day of the fiscal quarter ending September 30, 2026" |
| Prior facility in Q2 report | 10-Q_2026-06-30 page:14 | "Revolving credit facility (a) 470 130" |
| Annual maturity ladder (as of 2025-12-31) | 10-K_2025-12-31 page:107 | "$130 $500 $1,252 $500 $750 $1,586 $4,718" |
| Annual cash interest | 10-K_2025-12-31 page:82 | "Cash paid for interest 354 319 298" |
| Segment results, quarter | 10-Q_2026-09-30 page:27 | "Segment operating income (loss) $ 86 $ (37) $ 137 $ (14) $ 156 $ 40 $ 124 $ (8)" |
| Segment results, nine months | 10-Q_2026-09-30 page:28 | "Segment operating income (loss) $ 545 $ 9 $ 553 $ (17) $ 481 $ 62 $ 424 $ (5)" |
| Receivables factoring, first program | 10-Q_2026-09-30 page:9 | "Outstanding receivables sold under the Customer Receivables Purchase Agreement at September 30, 2026 and December 31, 2025 were approximately $300 million and $270 million, respectively." |
| Receivables factoring, second program | 10-Q_2026-09-30 page:10 | "Outstanding receivables sold under the Receivables Facility at September 30, 2026 and December 31, 2025 were approximately $135 million and $125 million, respectively." |
| Subsequent event | 10-Q_2026-09-30 page:34 | "the facility limit on factored receivables outstanding was amended to $75 million" |
| Standby letters of credit outside the facility | 10-Q_2026-09-30 page:34 | "At September 30, 2026, the Company had approximately $64 million in standby letters of credit" |
| Normalized EBITDA, Q1 2026 release | EX-99.1_2026-05-01 page:1 | "Normalized EBITDA was $135 million compared with $136 million in the prior year period" |
| Tariff recoveries inside Q2 2026 results | EX-99.1_2026-07-31 page:2 | "Second quarter reported and normalized results included approximately $100 million pretax" |
| Net debt reconciliation | EX-99.1_2026-10-30 page:17 | "Net debt [1] $ 4,592 $ 4,470 $ 4,548" |
| Trailing-twelve-month normalized EBITDA | EX-99.1_2026-10-30 page:18 | "Normalized EBITDA $ 1,030 $ 882 $ 857" |
| Outlook and operating cash flow revision | EX-99.1_2026-10-30 page:4 | "The Company revised its full-year 2026 operating cash flow outlook primarily due to two one-time non-operating items" |

### Consumer assessments

| Consumer | Status | Evidence located | Limitations carried |
| --- | --- | --- | --- |
| CP-1 financial base | READY_WITH_LIMITATIONS | Annual and three consecutive 2026 quarterly statements, segment note with segment operating income, depreciation and amortization and capital expenditures, facility-level debt tables at 2025-12-31, 2026-03-31, 2026-06-30 and 2026-09-30, annual cash paid for interest and taxes, non-GAAP reconciliations in the releases. | Cash paid for interest and taxes is annual only. Q4 2025 as a discrete quarter is not printed as such. Normalized figures are management claims. Source sufficiency only; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED and no quarter normalization or reconciliation is asserted. |
| CP-1A business and transaction | READY_WITH_LIMITATIONS | Business description and three segments in the latest quarterly report and the annual report; the 2026 notes offering, redemption, new asset-based facility and receivables amendments are described in the latest quarterly report. | Executed indenture, credit agreement and receivables agreements are not supplied; only the filer's descriptions are available. No sponsor, guarantor financials or restricted and unrestricted entity split. |
| CP-2 credit synthesis | READY_WITH_LIMITATIONS | Debt, availability, letters of credit, weighted average rates, compliance statement, trailing-twelve-month net debt and normalized EBITDA in the release, outlook. | No printed covenant level or reported covenant ratio under the new facility; no current maturity ladder; ratings and market quotes blank in context. |
| CP-5 evidence trace | READY_WITH_LIMITATIONS | All claims above are locatable by page in retained text. | Text extraction only; no fidelity review against rendered documents; charts and images not inspected. |

Command sheet status: RUN for CP-1, CP-1A, CP-2 and CP-5. None is DO NOT RUN.

## Calculations

None. CP-0 does not normalize, reconcile or calculate financial figures. The only counts are coverage counts of retained pages: 150 pages (annual report), 38 (Q1 report), 46 (Q2 report), 54 (Q3 report), 16 (Q1 release), 18 (Q2 release) and 19 (Q3 release), which sum to 341 retained pages (150 + 38 + 46 + 54 + 16 + 18 + 19 = 341). No source-count or page-count figure is offered as proof of readiness. Every financial figure above is a quoted source value, not a derived one.

## Gaps

| Gap | Severity | Affected consumers | Remediation | Evidence of absence |
| --- | --- | --- | --- | --- |
| Executed indentures, ABL credit agreement, Credit Revolver amendments and receivables agreements are not in the pack; only descriptions in filings are available. | Medium | CP-1A, CP-2, CP-5 | Treat filing descriptions as the authority; do not interpret legal terms beyond them. | The pack lists only the seven filed documents; the contract terms are cited from the 10-K and 10-Qs. |
| Covenant levels and reported ratio values are not printed for the Collateral Coverage Ratio and Total Net Leverage Ratio of the former Credit Revolver or for the Fixed Charge Coverage Ratio of the new ABL facility; the 10-K says only that the net leverage covenant steps down from the quarter ending 2026-09-30. Searches for leverage ratio, Fixed Charge, compliance and covenant across all seven sources found descriptions and a compliance statement, no levels. | Medium | CP-2, CP-5 | Report headroom as Not calculable and name the missing level. | Pages cited in the evidence table. |
| The only maturity ladder is as of 2025-12-31 (before the 2026 redemption of the notes due 2027 and the issue of notes due 2031 and the new facility). The Q3 report prints no ladder. | Medium | CP-1, CP-2 | Rebuild the wall from the Q3 2026 facility-level debt table and stated maturities; do not use the annual ladder as current. | 10-K page:107 versus 10-Q Q3 page:17 and page:18. |
| Cash paid for interest and taxes is printed for FY2025 only; the 2026 quarterly reports and releases do not print them. Searches for cash paid, interest paid and taxes paid across the 10-Qs and releases found no such line. | Medium | CP-1, CP-2 | Mark interim cash interest and tax as Not supplied; use annual cash paid for interest only for FY2025 and do not annualize. | 10-K page:82 only. |
| Q4 2025 is not printed as a discrete quarter; only the full year and the comparative quarters inside the 2026 reports are supplied. | Low | CP-1 | Derive downstream only if needed and label it derived. | 10-K page:80 is annual only. |
| Tension to track, not resolved here: the Q3 report shows receivables sold under the second factoring program at 2026-09-30, and a subsequent amendment effective 2026-10-02 reduced its facility limit. The Q3 release also describes a reduced reliance on factoring. How the limit and the outstanding balance relate is not stated. | Low | CP-2, CP-5 | Present factoring as a separate claim outside the debt table and cite both programs. | 10-Q Q3 page:10, page:34, page:48; Q3 release page:4. |
| Ratings, market quotes, peers, deal terms and research questions are blank in context; the filings mention past rating actions only. Blank is not zero. | Low | CP-2 | Do not state a current rating from the context. | Context file sha256 listed in Sources. |
| Non-GAAP measures (normalized EBITDA, normalized earnings, net debt) are management definitions in releases; the filings do not print a normalized EBITDA. Q2 2026 reported and normalized results include tariff recoveries, which affects quarter comparability. | Medium | CP-1, CP-2 | Keep management claims attributed and separate from filed statements. | EX-99.1 pages cited above. |
| No presentation decks, workbooks or scanned images are in the pack; the releases stand in for presentations. Text extraction does not establish chart, image or table-as-image fidelity. | Low | CP-5 | Do not claim inspection of rendered content. | File list in Sources. |
| Guarantor identity and any guarantor or restricted-entity financial information for the notes and the new facility are not separately supplied; the new facility names a subsidiary borrower and guarantors without listing them. | Low | CP-1A, CP-2 | Treat the issuer as the consolidated registrant; flag structural subordination as an open item. | 10-Q Q3 page:19. |

Source-conflict log: no conflict between sources was established in CP-0. The annual-report statements about the former Credit Revolver and its covenants are superseded as of 2026-07-30 by the new facility described in the Q2 and Q3 reports; this is a version relationship, not a conflict.

## Next module

Proceed to CP-1 (financial base) with the Q3 2026 report as the controlling source for balances at 2026-09-30, the Q1 and Q2 reports for the other discrete quarters, and the annual report for FY2025. Carry forward these limits: facility-level debt must come from the Q3 table; annual maturity ladder and annual cash interest are as of FY2025 only; covenant levels and interim cash taxes are Not supplied; non-GAAP figures are attributed management claims; this is source sufficiency only and the Model input contract is not evaluated. CP-1A, CP-2 and CP-5 follow in that order.
