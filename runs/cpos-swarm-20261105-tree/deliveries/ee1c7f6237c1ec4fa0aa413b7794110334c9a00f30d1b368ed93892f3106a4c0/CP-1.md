# CP-1 — Financial base: LendingTree, Inc. (tree)

## Request

- Issuer: LendingTree, Inc. (issuer id `tree`; Nasdaq: TREE), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run: `tree-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. This module builds the financial base from the pinned filings and releases and the CP-0 readiness handoff. Later modules CP-1A, CP-2 and CP-5 consume it.
- Context settings: reporting currency USD; current period q2-2026; prior period fy-2025. The statements report in US dollars, in thousands. Narrative and the releases use US dollars, in millions. The sources report no other currency.
- Periods used, each labelled where it appears: FY2024 and FY2025 (fiscal years ended December 31); Q2 2025 and Q2 2026 (three months ended June 30); H1 2025 and H1 2026 (six months ended June 30); LTM June 30, 2026 (FY2025 plus H1 2026 less H1 2025, calculated here). Balance-sheet dates are December 31, 2024, December 31, 2025 and June 30, 2026.
- Execution: host session. The host read the pinned files and wrote this answer. No provider was called.
- Scope: reported facts, separately labelled calculations, definitions, data-quality findings and gaps. No credit opinion on ratings or relative value.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_tree-20251231.htm.jsonl | 8cb6cb5e097dc2e8360d276758588e587f0ac910e30b439c9a6d5f22fdc532f1 | Audited FY2025, FY2024 and FY2023 statements; debt Note 13; Adjusted EBITDA reconciliation |
| 10-Q_2025-09-30_tree-20250930.htm.jsonl | 249304d8f29fc14b902a9aacbb2c6a074e549655cafbbfa182447cab0a8e6bd0 | Unaudited Q3 2025 and nine-month 2025; Q3 2025 discrete quarter |
| 10-Q_2026-03-31_tree-20260331.htm.jsonl | 9f7be701e3beaeb193c8f4c45fa295df34640347810fab7e7e1868937c8317f9 | Unaudited Q1 2026; used for discrete Q2 2026 cash-flow derivation |
| 10-Q_2026-06-30_tree-20260630.htm.jsonl | 4c93c158274dd2856277ea5350526f695a8bcd4a41e0bedcd9b748ac31b890ae | Unaudited Q2 2026 and H1 2026 with 2025 comparatives; current-period authority |
| EX-99.1_2026-03-02_tree-123125xer.htm.jsonl | 930047033d516e80ede0b1af19850b29c93444522e483a1dc8c6992d4283ee5d | Q4 2025 earnings release; discrete Q4 2025 non-GAAP figures and management leverage statement |
| EX-99.1_2026-04-30_tree-33126xer.htm.jsonl | 9b95e0c334507932b6d82bc72cf01d0a8f620ab6313637adea07e7f7ef2b4190 | Q1 2026 earnings release; context only |
| EX-99.1_2026-07-29_tree-63026xer.htm.jsonl | b737e26fe71071d22f2d669bce2532cab38eb1e5741e87f2852ff6a85cf82520 | Q2 2026 earnings release; Q1 2026 discrete non-GAAP comparatives and outlook |
| context | d200051bbc093266762c46db0da57fcc23aae21f45bdfa41362781dff2cb6e7d | User run settings; not issuer evidence |

| Handoff module | sha256 | Use |
| --- | --- | --- |
| CP-0 | c84ab10531b22ca79243cab80e778b189c7ae85ab40d1bc94cfa4d4426e74643 | Readiness verdict and gap list; its limitations are carried forward below |

Locators are `page:N`, the source chunk number in each pinned file, not the printed page. A locator names the file by its short form: 10-K (FY2025), 10-Q Q2 2026, 10-Q Q1 2026, 10-Q Q3 2025, release Q4 2025, release Q1 2026, release Q2 2026.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Total debt to Adjusted EBITDA fell from 4.56x at December 31, 2024 to 2.58x for the twelve months to June 30, 2026. Liquidity is US$110.8m cash plus an undrawn US$75.0m revolver. EBITDA quality is the main judgment. | Medium | Adjusted EBITDA is an issuer non-GAAP measure that adds back non-cash compensation; covenant definitions and letter of credit usage are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Twelve-month revenue to June 30, 2026 was US$1,268.2m and Adjusted EBITDA US$153.6m, up from US$132.9m in FY2025. | A larger earnings base supports debt service, but growth is concentrated in the Insurance segment, so mix matters. | High |
| Net debt to Adjusted EBITDA is 1.86x and total debt to Adjusted EBITDA is 2.58x, from 2.39x and 3.00x at FY2025. | Deleveraging is real but flattering if non-cash compensation is treated as a cost; that sensitivity gives 3.05x total debt. | Medium |
| Cash interest paid was US$34.7m over the last twelve months, covered 4.42x by Adjusted EBITDA; free cash flow was US$73.9m. | Debt service looks comfortable; only US$4.0m falls due within twelve months, so refinancing risk sits at the August 21, 2030 maturity. | Medium |
| Variable marketing spend was 70.8% of revenue in H1 2026, and one partner supplied 27% of FY2025 revenue. | Margins depend on advertising efficiency and one insurer, so earnings can fall quickly if either weakens. | Medium |
| FY2025 net income of US$151.3m includes a US$130.3m income tax benefit. | Net income overstates operating earning power; judge credit on operating income and Adjusted EBITDA. | High |

### Financial base view

Twelve-month revenue to June 30, 2026 was US$1,268.2m and Adjusted EBITDA US$153.6m, against US$132.9m in FY2025; cash interest paid over the same twelve months was US$34.7m; FY2025 net income was US$151.3m. The financial base is usable and shows a business that has grown quickly and cut leverage, with one facility, no maturity other than scheduled amortization before August 21, 2030 and a large undrawn revolver. On issuer-defined Adjusted EBITDA, total debt to EBITDA moved from 4.56x at December 31, 2024 to 3.00x at December 31, 2025 and 2.58x for the twelve months to June 30, 2026; net debt to EBITDA moved from 3.54x to 2.39x and 1.86x. Revenue grew 24.1% in FY2025 and 30.8% in H1 2026, and Adjusted EBITDA grew 36.8% in H1 2026, but only 10.6% in Q2 2026 and it fell 16.3% from Q1 2026 (calculation C2). Cash interest paid was covered 4.42x for the last twelve months. Free cash flow for that period was US$73.9m. The restrictions are definitional rather than about data volume. Adjusted EBITDA excludes non-cash compensation and litigation settlements, so the same debt on unadjusted EBITDA is 3.10x total debt to EBITDA for the twelve months to June 30, 2026. Second-quarter 2026 variable marketing margin and Adjusted EBITDA were both below the first quarter, and the business depends on variable advertising spend and one large insurance partner. All leverage figures here use the principal of the 2025 Term Loan, not the carrying value net of issuance costs.

### Source context

- 10-K (FY2025), audited by PricewaterhouseCoopers LLP (page:109). Entity perimeter: LendingTree, Inc. and subsidiaries, consolidated, USD, in thousands (page:109, page:110). Controls FY2025, FY2024 and FY2023 facts and the December 31, 2025 balance sheet.
- 10-Q Q2 2026 (page:2 to page:4): unaudited, same entity perimeter, USD, in thousands; carries the June 30, 2026 balance sheet and H1 2026 and H1 2025 flows. Note 1 states "Certain prior period amounts have been reclassified to conform to the current period presentation" (page:6).
- 10-Q Q1 2026 (page:2 to page:4) and 10-Q Q3 2025 (page:2, page:3): unaudited interim reports used for discrete quarters and for the Q2 2026 cash-flow derivation.
- Three releases: management-prepared, unaudited, same perimeter. They repeat filed figures and add discrete-quarter non-GAAP reconciliations and outlook. A filed report controls where they differ (see data-quality finding).
- Extraction: text only. Tables are flattened; no image or XBRL review was done.

### Reported income statement

US$ thousands, as printed. Sources: FY2024 and FY2025 10-K page:110; H1 and Q2 columns 10-Q Q2 2026 page:2 and page:3.

| Line | FY2024 | FY2025 | H1 2025 | H1 2026 | Q2 2025 | Q2 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| Revenue | 900,219 | 1,117,324 | 489,844 | 640,689 | 250,116 | 313,422 |
| Cost of revenue | 36,072 | 42,525 | 19,937 | 22,965 | 10,029 | 11,269 |
| Selling and marketing expense | 635,963 | 812,904 | 349,504 | 475,021 | 176,753 | 236,453 |
| General and administrative expense | 108,705 | 112,888 | 55,694 | 53,700 | 25,034 | 25,710 |
| Product development | 46,358 | 45,251 | 23,377 | 21,499 | 11,473 | 10,032 |
| Depreciation | 18,300 | 16,459 | 8,538 | 8,462 | 4,241 | 4,277 |
| Amortization of intangibles | 5,889 | 5,190 | 2,614 | 2,576 | 1,307 | 1,288 |
| Restructuring and severance | 508 | 1,633 | 1,155 | 2,778 | 357 | 1,839 |
| Litigation settlements and contingencies | 3,797 | 15,661 | 15,210 | 776 | (2) | 756 |
| Total costs and expenses | 855,592 | 1,052,511 | 476,029 | 587,777 | 229,192 | 291,624 |
| Operating income | 44,627 | 64,813 | 13,815 | 52,912 | 20,924 | 21,798 |
| Interest expense, net | (27,849) | (46,787) | (19,486) | (17,049) | (10,402) | (8,483) |
| Other income (expense) | (54,162) | 2,998 | 1,636 | 1,201 | 248 | 832 |
| Income (loss) before income taxes | (37,384) | 21,024 | (4,035) | 37,064 | 10,770 | 14,147 |
| Income tax benefit (expense) | (4,320) | 130,284 | 522 | (10,224) | (1,908) | (4,573) |
| Net income (loss) | (41,704) | 151,308 | (3,513) | 26,840 | 8,862 | 9,574 |

### Reported discrete quarters

US$ thousands. Revenue, Adjusted EBITDA, variable marketing margin and net income by quarter. Q2 2025 and Q2 2026: 10-Q Q2 2026 page:2, page:36, page:38. Q3 2025: 10-Q Q3 2025 page:2, page:3 and release Q4 2025 page:7, page:8 (reconciliations). Q4 2025: release Q4 2025 page:5, page:7, page:8. Q1 2026: 10-Q Q1 2026 page:2 and release Q2 2026 page:5, page:6.

| Quarter | Revenue | Variable marketing margin (non-GAAP) | Adjusted EBITDA (non-GAAP) | Net income | Operating income |
| --- | --- | --- | --- | --- | --- |
| Q2 2025 | 250,116 | 83,648 | 31,793 | 8,862 | 20,924 |
| Q3 2025 | 307,792 | 93,224 | 39,795 | 10,165 | 28,766 |
| Q4 2025 | 319,688 | 92,045 | 36,673 | 144,656 | 22,232 |
| Q1 2026 | 327,267 | 99,547 | 42,009 | 17,266 | 31,114 |
| Q2 2026 | 313,422 | 87,339 | 35,162 | 9,574 | 21,798 |

The four quarters Q1 2025 to Q4 2025 are not all shown, but the printed Q1 2025 revenue of 239,728 (10-Q Q1 2026 page:2) with the quarters above sums to the FY2025 revenue of 1,117,324 (calculation C14). The sum of the quarterly Adjusted EBITDA figures, including Q1 2025 of 24,626 (10-Q Q1 2026 page:33), equals FY2025 Adjusted EBITDA of 132,887.

### Reported segments

US$ thousands. FY columns 10-K page:152; H1 and Q2 columns 10-Q Q2 2026 page:21 and page:22. Segment profit is revenue less segment marketing expense, the issuer's primary segment measure (10-Q Q2 2026 page:33). "Other" is marketing revenue and expense not allocated to a segment.

| Line | FY2024 | FY2025 | H1 2025 | H1 2026 | Q2 2025 | Q2 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| Home revenue | 128,854 | 151,764 | 77,437 | 82,974 | 40,418 | 43,906 |
| Consumer revenue | 222,462 | 253,370 | 118,552 | 126,593 | 62,519 | 60,260 |
| Insurance revenue | 548,704 | 711,880 | 293,809 | 431,122 | 147,157 | 209,263 |
| Other revenue | 199 | 310 | 46 | — (printed as a dash) | 22 | (7) |
| Home segment profit | 39,896 | 48,343 | 26,202 | 21,240 | 13,056 | 11,278 |
| Consumer segment profit | 110,537 | 129,448 | 59,207 | 60,553 | 32,070 | 27,620 |
| Insurance segment profit | 159,230 | 174,417 | 78,706 | 107,929 | 39,996 | 49,997 |
| Other segment profit (loss) | (95) | (161) | (24) | (142) | (12) | (72) |
| Total segment profit | 309,568 | 352,047 | 164,091 | 189,580 | 85,110 | 88,823 |

### Reported balance sheet

US$ thousands. December 31, 2024 and December 31, 2025: 10-K page:110. June 30, 2026: 10-Q Q2 2026 page:2.

| Line | Dec 31, 2024 | Dec 31, 2025 | Jun 30, 2026 |
| --- | --- | --- | --- |
| Cash and cash equivalents | 106,594 | 81,073 | 110,766 |
| Accounts receivable, net | 97,790 | 110,582 | 149,287 |
| Total current assets | 238,462 | 229,708 | 299,804 |
| Goodwill | 381,539 | 381,539 | 381,539 |
| Intangible assets, net | 43,283 | 38,092 | 35,516 |
| Deferred income tax assets | — (printed as a dash) | 124,867 | 114,737 |
| Total assets | 767,674 | 855,692 | 911,631 |
| Current portion of long-term debt | 124,931 | 3,926 | 3,932 |
| Accounts payable, trade | 8,360 | 6,735 | 47,351 |
| Accrued expenses and other current liabilities | 107,185 | 126,803 | 111,086 |
| Total current liabilities | 240,476 | 137,464 | 162,369 |
| Long-term debt | 344,124 | 387,694 | 386,351 |
| Operating lease liabilities (non-current) | 69,238 | 43,597 | 41,996 |
| Total liabilities | 658,853 | 568,895 | 590,859 |
| Total shareholders' equity | 108,821 | 286,797 | 320,772 |

Accumulated deficit was (728,099) at December 31, 2025 and (701,259) at June 30, 2026 (10-Q Q2 2026 page:2). Goodwill of 381,539 is net of accumulated impairment losses of 521,688 (10-Q Q2 2026 page:11).

### Reported cash flow

US$ thousands. FY columns 10-K page:111, page:112; H1 columns 10-Q Q2 2026 page:4.

| Line | FY2024 | FY2025 | H1 2025 | H1 2026 |
| --- | --- | --- | --- | --- |
| Net cash provided by operating activities | 62,258 | 73,103 | 27,743 | 40,717 |
| Capital expenditures | (11,220) | (12,423) | (6,158) | (5,935) |
| Net cash used in investing activities | (11,218) | (9,926) | (6,158) | (5,883) |
| Proceeds from term loan | 125,000 | 450,000 | 50,000 | — (printed as a dash) |
| Repayment of term loan | (12,500) | (410,375) | (6,563) | (2,000) |
| Repayment and repurchase of 0.50% Convertible Senior Notes | (158,839) | (115,007) | (19,700) | — (printed as a dash) |
| Net cash used in financing activities | (56,502) | (88,698) | 20,952 | (5,141) |
| Interest paid (supplemental) | 38,203 | 37,203 | 18,494 | 16,031 |
| Income tax payments (supplemental) | 1,676 | 1,772 | Not supplied: the 10-Q supplemental lines show interest paid only | Not supplied: the 10-Q supplemental lines show interest paid only |

H1 2026 operating cash flow includes the second and final instalments of a US$19.0m litigation settlement (10-Q Q2 2026 page:20: "The settlement was payable in three equal installments"). Accrued contingencies fell from 13,001 to 863 between December 31, 2025 and June 30, 2026 (10-Q Q2 2026 page:12).

### Debt and claims outside debt

Facilities and principal, US$ thousands. Sources: 10-K page:144 to page:146, page:149; 10-Q Q2 2026 page:18, page:19, page:39.

| Instrument | Terms as printed | Gross principal | Net carrying value |
| --- | --- | --- | --- |
| 2025 Term Loan (first lien, secured by substantially all assets, guaranteed by material domestic subsidiaries; the borrower entity is not named in the pinned text) | US$400.0m facility, matures August 21, 2030; interest on Term SOFR plus 4.50% (4.25% after a Moody's corporate family rating of B2 (stable) or better, achieved January 2026) (10-K page:145) | Dec 31, 2025: 399,000; Jun 30, 2026: 397,000 | Dec 31, 2025: 391,620; Jun 30, 2026: 390,283 (calculation C4) |
| 2025 Revolving Facility | US$75.0m commitment, matures August 21, 2030; up to US$30.0m for letters of credit; no borrowings at December 31, 2025 or June 30, 2026 (10-K page:144; 10-Q Q2 2026 page:19) | 0 drawn (no borrowings outstanding) | Not applicable |
| 2021 Credit Facility term loan and revolver, 2024 Term Loan | Repaid or terminated August 21, 2025 (10-K page:148) | Dec 31, 2024: bank debt of 359,375 in aggregate (calculation C4) | Dec 31, 2024: part of 469,055 total carrying debt |
| 0.50% Convertible Senior Notes due July 15, 2025 | Repaid at maturity July 15, 2025 (10-K page:142) | Dec 31, 2024: 115,307 (10-K page:143) | Dec 31, 2024: 114,976 |

- Financial covenant: first lien net leverage ratio of 5.00 to 1.00, tested only if loans and certain other obligations under the revolver exceed US$20.0m at a quarter end; "The Company was in compliance with all covenants at June 30, 2026" (10-K page:145; 10-Q Q2 2026 page:19). The reported ratio and its definition are Not supplied.
- Incremental capacity: the greater of US$58.0m and 50% of consolidated EBITDA plus an unlimited amount if first lien net leverage does not exceed 3.10 to 1.00 (10-K page:145). The agreement's EBITDA definition is Not supplied.
- Interest: H1 2026 interest expense on the 2025 Credit Agreement was US$16.8m, of which US$15.9m on SOFR-based borrowings (10-Q Q2 2026 page:19). A 100 basis point move would change annual interest by US$4.0m (10-Q Q2 2026 page:40).
- Outside the debt figure: operating lease liabilities of 3,783 current plus 41,996 non-current at June 30, 2026 (10-Q Q2 2026 page:12, page:2), and lease payments of 8,186 due in 2026 per the December 31, 2025 maturity table (10-K page:131); surety bonds of 3,243 (10-K page:149); litigation accruals of US$0.9m at June 30, 2026 (10-Q Q2 2026 page:20). The sources show no pension, retiree medical, factoring, supply-chain finance, purchase commitment or consent-decree obligation (searched "pension", "factoring", "supply chain finance", "purchase obligation", "consent decree"); only a 401(k) plan with company matching of about US$2.6m in FY2025 (10-K page:151).

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 (Dec 31, 2024) | 4.56 | 3.54 | x | Gross principal 474,682 (convertible notes 115,307 plus bank debt 359,375) over issuer Adjusted EBITDA of 104,113; net of cash of 106,594. Issuer non-GAAP EBITDA; calculation C5. |
| FY2025 (Dec 31, 2025) | 3.00 | 2.39 | x | Gross principal 399,000 over Adjusted EBITDA of 132,887; net of cash of 81,073. Matches the management statement of net leverage of 2.4x (release Q4 2025 page:2). Calculation C5. |
| LTM Jun 30, 2026 | 2.58 | 1.86 | x | Gross principal 397,000 over LTM Adjusted EBITDA of 153,639 (FY2025 plus H1 2026 less H1 2025); net of cash of 110,766. Issuer non-GAAP EBITDA adds back non-cash compensation; on unadjusted EBITDA the ratios are 3.10 and 2.24 (calculation C5). |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 2.73 | x | Adjusted EBITDA of 104,113 over interest paid of 38,203 (10-K page:112). Cash interest includes the convertible notes and two term loans outstanding in 2024. Calculation C6. |
| FY2025 | 3.57 | x | Adjusted EBITDA of 132,887 over interest paid of 37,203 (10-K page:112). The August 21, 2025 refinancing changed the debt mix within the year. Calculation C6. |
| LTM Jun 30, 2026 | 4.42 | x | LTM Adjusted EBITDA of 153,639 over LTM interest paid of 34,740 (37,203 plus 16,031 less 18,494). Issuer non-GAAP EBITDA; calculation C6. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2024 | 106.6 | Not supplied: the 2021 revolver balance at December 31, 2024 is not stated in the pinned sources | US$m | Cash and cash equivalents of 106,594 (10-K page:110). The 2021 revolver was terminated on August 21, 2025 (10-K page:148). |
| Dec 31, 2025 | 81.1 | 75.0 | US$m | Cash of 81,073 (10-K page:110). Revolver commitment of 75,000 with no borrowings (10-K page:144). Letters of credit outstanding are Not supplied; the 10-K states US$75.0m "available for borrowing" at March 9, 2026 (10-K page:98). |
| Jun 30, 2026 | 110.8 | 75.0 | US$m | Cash of 110,766 (10-Q Q2 2026 page:2). Revolver commitment of 75,000 with no borrowings (10-Q Q2 2026 page:19); "$75.0 million available for borrowing" at July 30, 2026 (10-Q Q2 2026 page:39). The financial covenant is tested only above US$20.0m of revolver usage. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Due within 12 months of Dec 31, 2024 | 125.6 | US$m | Gross carrying amount: current portion 10,313 plus 2025 Notes 115,307 (10-K page:143, page:149). The notes were repaid on July 15, 2025. |
| Due after 12 months from Dec 31, 2024 | 349.1 | US$m | Long-term portion gross carrying amount 349,062 (10-K page:149). |
| Due within 12 months of Dec 31, 2025 | 4.0 | US$m | Current portion gross carrying amount 4,000 (10-K page:149). |
| Due after 12 months from Dec 31, 2025 | 395.0 | US$m | Long-term portion gross carrying amount 395,000; final maturity August 21, 2030 (10-K page:149, page:144). Annual split of the long-term portion is Not supplied. |
| Due within 12 months of Jun 30, 2026 | 4.0 | US$m | Current portion gross carrying amount 4,000 (10-Q Q2 2026 page:18). |
| Due after 12 months from Jun 30, 2026 | 393.0 | US$m | Long-term portion gross carrying amount 393,000; final maturity August 21, 2030 (10-Q Q2 2026 page:18). Revolver has no borrowings. Annual split Not supplied. |

### Financials and credit metrics

| Metric (US$ thousands unless stated) | FY2024 | FY2025 | H1 2025 | H1 2026 | Q2 2025 | Q2 2026 | LTM Jun 30, 2026 | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue | 900,219 | 1,117,324 | 489,844 | 640,689 | 250,116 | 313,422 | 1,268,169 | Reported; LTM calculated (C1) |
| Variable marketing margin (non-GAAP) | 304,311 | 346,644 | 161,375 | 186,886 | 83,648 | 87,339 | 372,155 | Issuer non-GAAP; LTM calculated (C1) |
| Adjusted EBITDA (non-GAAP) | 104,113 | 132,887 | 56,419 | 77,171 | 31,793 | 35,162 | 153,639 | Issuer non-GAAP; LTM calculated (C1) |
| Unadjusted EBITDA (net income plus interest, tax, depreciation, amortization) | 14,654 | 89,460 | 26,603 | 65,151 | 26,720 | 28,195 | 128,008 | Calculated (C3) |
| Operating income | 44,627 | 64,813 | 13,815 | 52,912 | 20,924 | 21,798 | 103,910 | Reported; LTM calculated (C1) |
| Net income | (41,704) | 151,308 | (3,513) | 26,840 | 8,862 | 9,574 | 181,661 | Reported; LTM calculated (C1); FY2025 and LTM include a US$130.3m tax benefit |
| Interest expense, net | 27,849 | 46,787 | 19,486 | 17,049 | 10,402 | 8,483 | 44,350 | Reported; FY2025 includes a loss on repayment of term loans of 7,861 (10-K page:111) |
| Cash interest paid | 38,203 | 37,203 | 18,494 | 16,031 | 9,666 | 8,013 | 34,740 | Reported; Q2 and LTM calculated (C6, C12) |
| Net cash provided by operating activities | 62,258 | 73,103 | 27,743 | 40,717 | 27,953 | 29,165 | 86,077 | Reported; Q2 and LTM calculated (C7, C12) |
| Capital expenditures | 11,220 | 12,423 | 6,158 | 5,935 | 2,744 | 3,165 | 12,200 | Reported; Q2 and LTM calculated (C7, C12) |
| Free cash flow (operating cash flow less capital expenditures) | 51,038 | 60,680 | 21,585 | 34,782 | 25,209 | 26,000 | 73,877 | Calculated (C7, C12) |
| Total debt, gross principal (period end) | 474,682 | 399,000 | Not supplied: the Jun 30, 2025 balance sheet is not in the pack | 397,000 | Not supplied: the Jun 30, 2025 balance sheet is not in the pack | 397,000 | 397,000 | Reported principal; FY2024 calculated (C4) |
| Cash and cash equivalents (period end) | 106,594 | 81,073 | Not supplied: the Jun 30, 2025 balance sheet is not in the pack | 110,766 | Not supplied: the Jun 30, 2025 balance sheet is not in the pack | 110,766 | 110,766 | Reported |
| Net debt (gross principal less cash) | 368,088 | 317,927 | Not supplied: the Jun 30, 2025 balance sheet is not in the pack | 286,234 | Not supplied: the Jun 30, 2025 balance sheet is not in the pack | 286,234 | 286,234 | Calculated (C4) |
| Total debt / Adjusted EBITDA (x) | 4.56 | 3.00 | Not calculable: no Jun 30, 2025 debt | Not calculable: half-year EBITDA is not annual | Not calculable: no Jun 30, 2025 debt | Not calculable: quarterly EBITDA is not annual | 2.58 | Calculated (C5) |
| Net debt / Adjusted EBITDA (x) | 3.54 | 2.39 | Not calculable: no Jun 30, 2025 debt | Not calculable: half-year EBITDA is not annual | Not calculable: no Jun 30, 2025 debt | Not calculable: quarterly EBITDA is not annual | 1.86 | Calculated (C5) |
| Total debt / unadjusted EBITDA (x) | 32.39 | 4.46 | Not calculable: no Jun 30, 2025 debt | Not calculable: half-year EBITDA is not annual | Not calculable: no Jun 30, 2025 debt | Not calculable: quarterly EBITDA is not annual | 3.10 | Calculated (C5); FY2024 is distorted by 54,162 of other expense |
| Adjusted EBITDA / cash interest paid (x) | 2.73 | 3.57 | 3.05 | 4.81 | 3.29 | 4.39 | 4.42 | Calculated (C6) |
| Adjusted EBITDA / interest expense, net (x) | 3.74 | 2.84 | 2.90 | 4.53 | 3.06 | 4.15 | 3.46 | Calculated (C6) |
| Adjusted EBITDA margin on revenue (%) | 11.6 | 11.9 | 11.5 | 12.0 | 12.7 | 11.2 | 12.1 | Calculated (C8) |
| Variable marketing margin on revenue (%) | 33.8 | 31.0 | 32.9 | 29.2 | 33.4 | 27.9 | 29.3 | Calculated (C8) |
| Cash income taxes paid | 1,676 | 1,772 | Not supplied: not printed in the 10-Q | Not supplied: not printed in the 10-Q | Not supplied: not printed in the 10-Q | Not supplied: not printed in the 10-Q | Not supplied: 2026 not printed | Reported (10-K page:112) |

### Definition review

- Adjusted EBITDA: net income excluding interest, income tax, amortization and depreciation, and further excluding non-cash compensation, non-cash impairment charges, gain or loss on disposals, gain or loss on investments, restructuring and severance, litigation settlements and contingencies, acquisition and disposition items, LendingTree Foundation contributions, dividend income, and one-time items (10-Q Q2 2026 page:37). "For the periods presented below, there are no adjustments for one-time items."
- Size of the add-backs. FY2025 non-cash compensation added back was 29,202, litigation 15,661, restructuring 1,633, loss on investments 1,225, and dividend income of (4,223) was deducted (10-K page:96). Non-cash compensation was about 22.0% of FY2025 Adjusted EBITDA and 12.0% of H1 2026 Adjusted EBITDA (calculation C9). The sensitivity that treats LTM non-cash compensation of 23,632 as a cost gives total debt to EBITDA of 3.05x and net debt to EBITDA of 2.20x (calculation C9).
- Variable marketing expense is defined as advertising and promotional expense and excludes overhead and personnel costs. The 10-Q states "advertising and promotional expenses are equivalent to the non-GAAP measure variable marketing expense" (10-Q Q2 2026 page:30). Variable marketing margin is revenue less that expense (10-Q Q2 2026 page:35).
- Net leverage as stated by management at December 31, 2025, 2.4x against 3.5x a year earlier, agrees with the computation here (release Q4 2025 page:2; calculation C5). The release does not print the formula, so agreement is observed, not confirmed by definition.
- The covenant's first lien net leverage ratio, its EBITDA definition and the cash netting rules are in the credit agreement, which is not supplied. No covenant headroom is computed.

### Leverage

Total debt to Adjusted EBITDA fell from 4.56x at December 31, 2024 to 3.00x at December 31, 2025 and 2.58x for the twelve months to June 30, 2026. Two things drove the FY2025 fall. Total principal fell by 75,682, because 115,307 of 2025 Notes were repaid in cash while bank debt rose by 39,625, from 359,375 to 399,000 (calculation C4). Adjusted EBITDA rose from 104,113 to 132,887. The LTM fall since December 31, 2025 comes from higher EBITDA (153,639 against 132,887) and a 2,000 term loan repayment. The covenant level of 5.00 to 1.00 first lien net leverage is above every Adjusted EBITDA-based ratio computed here, but its definition sits in an unsupplied agreement, so the two are not comparable. The unadjusted EBITDA view is 3.10x total debt to EBITDA at LTM June 30, 2026 against 4.46x at FY2025.

### Coverage

Adjusted EBITDA covered cash interest paid 2.73x in FY2024, 3.57x in FY2025 and 4.42x over the last twelve months. Net interest expense was 10,402 in Q2 2025 and 8,483 in Q2 2026. H1 2025 interest expense was split across three instruments (US$11.3m on the 2021 credit agreement, US$7.8m on the 2024 Term Loan and US$0.6m on the 2025 Notes), against US$16.8m on the single 2025 Credit Agreement in H1 2026 (10-Q Q2 2026 page:19). The sources give no further driver. FY2025 interest expense includes a loss on repayment of term loans of 7,861 that is not a cash interest cost. Interest paid in 2025 straddles two debt structures, so FY2025 cover is a mixed-basis figure.

### Cash flow quality

Free cash flow was 51,038 in FY2024, 60,680 in FY2025 and 73,877 over the last twelve months, which is about 48.1% of LTM Adjusted EBITDA (calculation C7). Three items qualify it. First, H1 2026 operating cash flow bore two of three equal instalments of a US$19.0m settlement. Second, working capital is large and seasonal: accounts receivable rose from 110,582 to 149,287 between December 31, 2025 and June 30, 2026 while accounts payable rose from 6,735 to 47,351, and the 10-Q cash flow shows a 39,186 receivables outflow in H1 2026 (10-Q Q2 2026 page:4). Third, FY2025 net income of 151,308 includes a 130,284 income tax benefit that is mostly deferred (deferred income taxes of (129,751) in the cash flow, 10-K page:111); cash taxes paid were only 1,772. The deferred tax asset was 124,867 at December 31, 2025 and 114,737 at June 30, 2026, and the 10-Q says certain option expiries could reverse part of it (10-Q Q2 2026 page:18).

### Liquidity

Liquidity at June 30, 2026 was cash of 110,766 plus an undrawn revolver of 75,000, or 185,766 before any letters of credit (calculation C10). At December 31, 2025 it was 156,073 on the same basis. Only 4,000 of debt falls due within twelve months of June 30, 2026. The revolver matures on August 21, 2030, the same date as the term loan, so there is no revolver maturity ahead of the term loan. The issuer states that it expects cash and operating cash flow "to be sufficient to fund our operating needs for the next twelve months and beyond" (10-Q Q2 2026 page:39).

### Data quality

- Conflict: release versus 10-K balance sheet. The Q4 2025 release shows December 31, 2025 "Prepaid and other current assets 49,053", "Total current assets 240,708" and "Other non-current assets 5,522" (release Q4 2025 page:5). The audited 10-K shows 38,053, 229,708 and 16,522, plus equity investments of 475 (10-K page:110). The 10-Q Q2 2026 comparative agrees with the 10-K (page:2). The difference is 11,000 moved between current and non-current assets; total assets of 855,692 agree. The 10-K controls. Affected value: current assets and any current ratio at December 31, 2025. Downstream effect: use 229,708.
- Reclassification: the Q2 10-Q states that "Certain prior period amounts have been reclassified" (page:6). The 10-Q shows December 31, 2025 other non-current assets of 16,997 against the 10-K split of 16,522 and 475 (equity investments). No reconciliation is printed.
- Rate label: the 10-Q says borrowings "bear interest based on the Secured Overnight Financing Rate ("SOFR") of 7.89%" (10-Q Q2 2026 page:19), 8.22% at December 31, 2025 (10-K page:144). The pricing is Term SOFR plus 4.50% or 4.25% (10-K page:145), so these appear to be all-in rates. Not confirmed by the sources.
- Cross-check: the sum of the quarterly figures reconciles to the FY2025 totals for revenue and Adjusted EBITDA (calculation C14). The sum of the term loan gross principal less issuance costs and discount equals the carrying value at June 30, 2026 (calculation C4).
- Extraction: text only; no image or XBRL fidelity review.

### Definition risks and key gaps

- Adjusted EBITDA is issuer-defined and drives every leverage and cover ratio in the chart tables. The unadjusted ratios are shown beside them for that reason.
- Covenant definitions, borrower and guarantor names and letters of credit under the revolver need the credit agreement, which is Not supplied (CP-0 gap, carried forward).
- Nothing after July 30, 2026 is supplied. The 2026 outlook (revenue of US$1.30 to US$1.32 billion, Adjusted EBITDA of US$145 to US$152 million) is an attributed management claim from the July 29, 2026 release (release Q2 2026 page:3) and is not used in any ratio.
- Concentration: one Network Partner, Progressive Casualty Insurance, was 27% of FY2025 revenue, all in Insurance (10-K page:12). The Insurance segment was 63.7% of FY2025 revenue and 66.8% of Q2 2026 revenue (calculation C11); the 2026 share for the partner is Not supplied.
- Variable marketing expense was 70.8% of H1 2026 revenue and 72.1% of Q2 2026 revenue (calculation C11). The 10-Q says the operating model is "highly sensitive to the amount and efficiency of variable marketing expenditures" (page:35) and expects "advertising costs to remain elevated for the remainder of 2026" (page:35).

## Calculations

All inputs are printed amounts in US$ thousands from the locators given above. Ratios are rounded to two decimals in the tables and to three decimals here.

**C1. LTM amounts (FY2025 plus H1 2026 less H1 2025).**
- Revenue: 1,117,324 + 640,689 − 489,844 = 1,268,169.
- Variable marketing margin: 346,644 + 186,886 − 161,375 = 372,155.
- Adjusted EBITDA: 132,887 + 77,171 − 56,419 = 153,639.
- Operating income: 64,813 + 52,912 − 13,815 = 103,910.
- Net income: 151,308 + 26,840 − (−3,513) = 181,661.
- Interest expense, net: 46,787 + 17,049 − 19,486 = 44,350.

**C2. Growth rates.**
- FY2025 revenue over FY2024 is 1,117,324 / 900,219 − 1 = 24.1%; H1 2026 over H1 2025 is 640,689 / 489,844 − 1 = 30.8%; H1 2026 Adjusted EBITDA over H1 2025 is 77,171 / 56,419 − 1 = 36.8%; Q2 2026 Adjusted EBITDA over Q2 2025 is 35,162 / 31,793 − 1 = 10.6%; Q2 2026 over Q1 2026 Adjusted EBITDA is 35,162 / 42,009 − 1 = −16.3%.

**C3. Unadjusted EBITDA = net income + interest expense, net + income tax expense (benefit) + depreciation + amortization of intangibles.**
- FY2024: −41,704 + 27,849 + 4,320 + 18,300 + 5,889 = 14,654.
- FY2025: 151,308 + 46,787 + (−130,284) + 16,459 + 5,190 = 89,460.
- H1 2025: −3,513 + 19,486 + (−522) + 8,538 + 2,614 = 26,603.
- H1 2026: 26,840 + 17,049 + 10,224 + 8,462 + 2,576 = 65,151.
- Q2 2025: 8,862 + 10,402 + 1,908 + 4,241 + 1,307 = 26,720.
- Q2 2026: 9,574 + 8,483 + 4,573 + 4,277 + 1,288 = 28,195.
- LTM: 89,460 + 65,151 − 26,603 = 128,008.

**C4. Debt and cash.**
- Gross principal FY2024: 2025 Notes 115,307 + current bank 10,313 + long-term bank 349,062 = 474,682 (bank debt 359,375).
- Gross principal FY2025: 4,000 + 395,000 = 399,000. June 30, 2026: 4,000 + 393,000 = 397,000.
- Carrying value June 30, 2026: 3,932 + 386,351 = 390,283. December 31, 2025: 3,926 + 387,694 = 391,620. December 31, 2024: 124,931 + 344,124 = 469,055.
- Tie-out, June 30, 2026: 397,000 − issuance costs (34 + 3,307) − discount (34 + 3,342) = 397,000 − 6,717 = 390,283, equal to the carrying value.
- Net debt = gross principal − cash: FY2024 474,682 − 106,594 = 368,088; FY2025 399,000 − 81,073 = 317,927; June 30, 2026 397,000 − 110,766 = 286,234.

**C5. Leverage ratios.**
- Total debt / Adjusted EBITDA: FY2024 474,682 / 104,113 = 4.559; FY2025 399,000 / 132,887 = 3.003; LTM 397,000 / 153,639 = 2.584.
- Net debt / Adjusted EBITDA: FY2024 368,088 / 104,113 = 3.536; FY2025 317,927 / 132,887 = 2.392; LTM 286,234 / 153,639 = 1.863.
- Total debt / unadjusted EBITDA: FY2024 474,682 / 14,654 = 32.393; FY2025 399,000 / 89,460 = 4.460; LTM 397,000 / 128,008 = 3.101.
- Net debt / unadjusted EBITDA: FY2024 368,088 / 14,654 = 25.119; FY2025 317,927 / 89,460 = 3.554; LTM 286,234 / 128,008 = 2.236.
- Management cross-check: release Q4 2025 states net leverage of 2.4x at year-end 2025 and 3.5x at year-end 2024; the computed 2.392 and 3.536 round to the same figures.

**C6. Coverage.**
- LTM interest paid: 37,203 + 16,031 − 18,494 = 34,740.
- Adjusted EBITDA / interest paid: FY2024 104,113 / 38,203 = 2.725; FY2025 132,887 / 37,203 = 3.572; H1 2025 56,419 / 18,494 = 3.051; H1 2026 77,171 / 16,031 = 4.814; Q2 2025 31,793 / 9,666 = 3.289; Q2 2026 35,162 / 8,013 = 4.388; LTM 153,639 / 34,740 = 4.422.
- Adjusted EBITDA / interest expense, net: FY2024 104,113 / 27,849 = 3.738; FY2025 132,887 / 46,787 = 2.840; H1 2025 56,419 / 19,486 = 2.895; H1 2026 77,171 / 17,049 = 4.527; Q2 2025 31,793 / 10,402 = 3.056; Q2 2026 35,162 / 8,483 = 4.145; LTM 153,639 / 44,350 = 3.464. Half-year and quarter ratios are period flows over period flows, not annualized.

**C7. Free cash flow and cash conversion.**
- FY2024: 62,258 − 11,220 = 51,038. FY2025: 73,103 − 12,423 = 60,680. H1 2025: 27,743 − 6,158 = 21,585. H1 2026: 40,717 − 5,935 = 34,782.
- LTM operating cash flow: 73,103 + 40,717 − 27,743 = 86,077. LTM capital expenditures: 12,423 + 5,935 − 6,158 = 12,200. LTM free cash flow: 86,077 − 12,200 = 73,877.
- LTM free cash flow / LTM Adjusted EBITDA: 73,877 / 153,639 = 48.1%.

**C8. Margins.** Adjusted EBITDA / revenue: FY2024 104,113 / 900,219 = 11.6%; FY2025 132,887 / 1,117,324 = 11.9%; H1 2025 56,419 / 489,844 = 11.5%; H1 2026 77,171 / 640,689 = 12.0%; Q2 2025 31,793 / 250,116 = 12.7%; Q2 2026 35,162 / 313,422 = 11.2%; LTM 153,639 / 1,268,169 = 12.1%. Variable marketing margin / revenue: FY2024 304,311 / 900,219 = 33.8%; FY2025 346,644 / 1,117,324 = 31.0%; H1 2025 161,375 / 489,844 = 32.9%; H1 2026 186,886 / 640,689 = 29.2%; Q2 2025 83,648 / 250,116 = 33.4%; Q2 2026 87,339 / 313,422 = 27.9%; LTM 372,155 / 1,268,169 = 29.3%.

**C9. Add-back sensitivity.**
- Non-cash compensation share of Adjusted EBITDA: FY2025 29,202 / 132,887 = 22.0%; H1 2026 9,264 / 77,171 = 12.0%.
- LTM non-cash compensation add-back: 29,202 + 9,264 − 14,834 = 23,632.
- Adjusted EBITDA less non-cash compensation: 153,639 − 23,632 = 130,007. Total debt / that figure: 397,000 / 130,007 = 3.054. Net debt / that figure: 286,234 / 130,007 = 2.202.

**C10. Liquidity.** June 30, 2026: 110,766 + 75,000 = 185,766. December 31, 2025: 81,073 + 75,000 = 156,073. Letters of credit are Not supplied and are not deducted.

**C11. Mix and spend ratios.**
- Insurance revenue share: FY2024 548,704 / 900,219 = 61.0%; FY2025 711,880 / 1,117,324 = 63.7%; Q2 2026 209,263 / 313,422 = 66.8%; H1 2026 431,122 / 640,689 = 67.3%.
- Insurance share of total segment profit: FY2025 174,417 / 352,047 = 49.5%; Q2 2026 49,997 / 88,823 = 56.3%.
- Variable marketing expense / revenue: H1 2026 453,803 / 640,689 = 70.8%; Q2 2026 226,083 / 313,422 = 72.1%; FY2025 770,680 / 1,117,324 = 69.0%.

**C12. Discrete Q2 derivations (H1 less Q1).**
- Operating cash flow: Q2 2026 40,717 − 11,552 = 29,165; Q2 2025 27,743 − (−210) = 27,953.
- Capital expenditures: Q2 2026 5,935 − 2,770 = 3,165; Q2 2025 6,158 − 3,414 = 2,744.
- Free cash flow: Q2 2026 29,165 − 3,165 = 26,000; Q2 2025 27,953 − 2,744 = 25,209.
- Interest paid: Q2 2026 16,031 − 8,018 = 8,013; Q2 2025 18,494 − 8,828 = 9,666.
- Inputs: Q1 2026 operating cash flow 11,552 and Q1 2025 (210) (10-Q Q1 2026 page:3); Q1 capital expenditures 2,770 and 3,414 and interest paid 8,018 and 8,828 (10-Q Q1 2026 page:4).

**C13. Working capital movement.** Accounts receivable June 30, 2026 less December 31, 2025: 149,287 − 110,582 = 38,705. Accounts payable: 47,351 − 6,735 = 40,616. Accrued contingencies: 13,001 − 863 = 12,138 reduction.

**C14. Quarter sums.**
- Revenue: Q1 2025 239,728 + Q2 250,116 + Q3 307,792 + Q4 319,688 = 1,117,324, equal to FY2025.
- Adjusted EBITDA: 24,626 + 31,793 + 39,795 + 36,673 = 132,887, equal to FY2025.
- Q4 2025 net income cross-check: 151,308 − (−3,513) − 10,165 = 144,656, equal to the release.

**C15. Balance sheet difference between release and 10-K.** 240,708 − 229,708 = 11,000 current assets; 16,522 + 475 − (5,522 + 475) = 11,000 non-current assets.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreement not supplied: covenant definitions, reported first lien net leverage, borrower and guarantor names, letters of credit under the revolver | High for covenant work; Medium for this module | CP-2 | Supply the August 21, 2025 Credit Agreement and compliance disclosure |
| Undrawn facility at December 31, 2024 not stated in the pinned sources (2021 revolver of 200,000, terminated August 21, 2025) | Low | CP-2 | Supply the FY2024 10-K |
| Annual maturity split of the 393,000 long-term portion not printed; only the 4,000 current portion and the August 21, 2030 final maturity are given | Low | CP-2 | Use current portion and final maturity only |
| Jun 30, 2025 balance sheet not in the pack; Q2 2025 and H1 2025 leverage not calculable | Low | CP-1A, CP-2 | Supply the Q2 2025 10-Q if needed |
| Cash income taxes paid for 2026 not printed in the 10-Qs | Low | CP-2 | Treat 2026 as Not supplied |
| Nothing after July 30, 2026, including any Q3 2026 results | Medium | CP-1A, CP-2 | Supply later filings |
| 2026 largest-customer concentration not located | Low | CP-1A | Supply later disclosure |
| Release versus 10-K balance sheet conflict (11,000 between current and non-current assets) | Low | CP-2 | Use 10-K and 10-Q Q2 2026 values |
| Rate label ambiguity (SOFR of 7.89% against Term SOFR plus 4.50% or 4.25%) | Low | CP-2 | Quote as printed |
| Text extraction only; no XBRL or image fidelity review | Low | CP-5 | Check flagged tables against the filed HTML |

## Next module

- CP-1A: use the segment table, the Insurance share of revenue and profit, the 27% partner concentration, the three segments and the Q2 2026 weakness in Consumer (revenue down 4% and segment profit down 14%, 10-Q Q2 2026 page:31) as inputs; label the July 29, 2026 outlook as a dated management claim.
- CP-2: take the leverage, cover and liquidity chart tables as issuer-EBITDA-based and carry the unadjusted ratios and the 3.05x non-cash-compensation sensitivity beside them; describe the 5.00 to 1.00 first lien net leverage covenant and the US$20.0m test trigger without computing headroom; carry the missing credit agreement, the letter of credit gap and the rate-label ambiguity as restrictions.
- CP-5: trace each figure to the cited `page:N`; the calculation labels C1 to C15 are the audit trail for derived amounts, and
