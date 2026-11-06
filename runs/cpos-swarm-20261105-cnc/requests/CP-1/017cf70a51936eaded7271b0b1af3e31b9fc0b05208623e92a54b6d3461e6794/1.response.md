# CP-1 Financial statements and credit metrics: CENTENE CORP (cnc)

## Request

- Issuer: CENTENE CORP (issuer id `cnc`), registrant "CENTENE CORPORATION", as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD; every amount below is USD millions unless a row says otherwise.
- Run `cnc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. This handoff feeds CP-1A, CP-2, CP-5 and the report section "Financials and credit metrics". Current period q3-2026, prior period fy-2025 (context).
- Execution: host session; no provider call. Every derived number is listed in `## Calculations` with its inputs.
- Scope: reported FY2024 and FY2025 annual figures (FY2023 is printed in the 10-K but not tabulated), the 2026 interim statements for Q1, Q2 and Q3 with 2025 comparatives, last-twelve-months (LTM) figures to September 30, 2026 built from them, debt, liquidity, covenants as disclosed, and events up to the cutoff. No rating, forecast, valuation or pro forma.
- Locators are `page:N` chunk numbers of the pinned extracts, not printed page numbers. Short names are defined in `## Sources`.

## Sources

### Issuer sources relied on

| Short name | Exact source name | sha256 (pinned file) | Used for |
| --- | --- | --- | --- |
| 10-K FY2025 | 10-K_2025-12-31_cnc-20251231.htm.jsonl | 097062d4e055a3b7fe83b7f7a6e69a627cdfc677e170580a5543c61781d7f32c | Audited FY2025, FY2024 and FY2023 statements (FY2024 and FY2025 tabulated), debt note, maturities, segment note |
| Q1 10-Q | 10-Q_2026-03-31_cnc-20260331.htm.jsonl | 6fdb16147461b8c90a892872b86f94619262dc29b1649522f12be59d50d43010 | March 31, 2026 statements, three-month columns |
| Q2 10-Q | 10-Q_2026-06-30_cnc-20260630.htm.jsonl | 2be254120598acb867bfc89cb539dc675621975d5b2820213b11fde2ab54d522 | June 30, 2026 statements, six-month columns |
| Q3 10-Q | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | cfb19f79c82250660e2e3f3fc4242fe18840a50e06dfa54c4c173df9081f0994 | September 30, 2026 statements, debt, liquidity, covenant, subsequent events |
| Q1 release | EX-99.1_2026-04-28_a20260428ex991pressrelease.htm.jsonl | 85e525be3f7df9445c1acc49590c58f56053e97a34531af048cb7fd64ca5f94b | Issuer cash available for general corporate use at March 31, 2026 |
| Q2 release | EX-99.1_2026-07-28_a20260728ex991pressrelease.htm.jsonl | ef848078ad02a5ade77bb7226070a38945f9e917a1e3e86d5abb0edd73e6d395 | Issuer cash available for general corporate use at June 30, 2026 |
| Q3 release | EX-99.1_2026-10-27_a20261027ex991pressrelease.htm.jsonl | 916ad849ec4d38de97614bebc7921009e1fad702ea222f32804d2cf10f3a8c80 | Adjusted EPS, guidance, debt to capitalization, regulated and unregulated split |

### Run settings

| Item | sha256 | Role |
| --- | --- | --- |
| context | 513a568e8f913d85d10b3279b6da71f4942d77c29169f956b5f35a2740b22b67 | USD; as-of and cutoff 2026-11-05; current period q3-2026; prior period fy-2025. Not issuer evidence. Blank fields (ratings, quotes, market data, guarantors) are not zero. |

### Supplied handoffs

| Module | sha256 | Consumed for |
| --- | --- | --- |
| CP-0 | 891bc08ab57345267c7df4471f2151a6318cc16f4e53da139e0a73bb24e6659d | Source readiness: statements are controlling, releases are secondary, executed agreements are not supplied, nothing after October 27, 2026 is supplied |

Carried forward from CP-0 and applied here: (1) the 10-K FY2025 and the 10-Qs control statement facts and the releases are not independent corroboration; (2) cash flow statements are cumulative only; (3) 2025 comparatives were reclassified in the 2026 filings; (4) the 10-K maturity schedule total does not equal its debt table lines; (5) covenant definitions, guarantors and the receivable purchase agreement are not supplied.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Calculated leverage improved sharply from FY2025 as senior notes were repurchased and earnings recovered, but earnings are front-loaded and headline cash is mostly regulated. Parent liquidity rests on a small cash balance and the undrawn revolver. | Medium | The issuer reports no EBITDA, so every leverage and cover ratio uses an analyst definition; covenant definitions and executed agreements are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Calculated leverage on LTM EBITDA is 3.62x, down from 6.86x in FY2025, while total debt fell to 15,542. | Deleveraging is real, but third quarter EBITDA was far below the first two quarters, so the LTM figure flatters the run rate. | Medium |
| Consolidated cash of 20,700 sits mostly in regulated subsidiaries; cash available for general corporate use was 175. | Parent debt service relies on subsidiary dividends and the undrawn 4,000 revolver rather than headline cash. | High |
| Operating cash flow includes state pass-through timing and a 970 net receivable sale in the first quarter. | Reported free cash flow overstates recurring cash generation, and quarterly cash flow is volatile. | Medium |
| Issuer debt-to-capital is 41.1% against a 0.60 maximum, and the 2027 notes were fully redeemed in October 2026. | The nearest maturity is cleared and the stated covenant has wide room, though its definition is unverified. | Medium |

### Financial base view

CENTENE CORP has a usable financial base for downstream work, with stated limits. Audited FY2025 statements and unaudited Q1, Q2 and Q3 2026 statements with 2025 comparatives are located and their totals recompute. On the analyst-calculated EBITDA used throughout (the issuer reports none), LTM leverage to September 30, 2026 is 3.62x and LTM cover of cash interest is 6.85x, against 6.86x and 3.92x for FY2025, when the health benefits ratio rose to 91.9% from 88.3% in FY2024. Total debt fell from 17,401 at December 31, 2025 to 15,542 at September 30, 2026 as senior notes were repurchased, and the remaining 2027 notes were redeemed in October 2026. Three cautions control the read. Earnings are front-loaded, so the LTM ratios are better than the third quarter run rate. Consolidated cash is mainly held by regulated subsidiaries, so net debt on that cash would mislead. Operating cash flow is distorted by pass-through timing and the receivable sale.

### Source context

| Source | Entity and perimeter | Periods | Statement kind | Units |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | Centene Corporation and subsidiaries, consolidated; parent-only schedule also supplied | Years ended December 31, 2025, 2024 and 2023; balance sheets at December 31, 2025 and 2024 | Audited, KPMG LLP | USD millions except shares in thousands and per share data (10-K FY2025 page:129) |
| Q1 10-Q | Same consolidated perimeter | Three months ended March 31, 2026 and 2025; balance sheet at March 31, 2026 and December 31, 2025 | Unaudited | USD millions (Q1 10-Q page:7) |
| Q2 10-Q | Same consolidated perimeter | Three and six months ended June 30, 2026 and 2025; balance sheet at June 30, 2026 and December 31, 2025 | Unaudited | USD millions (Q2 10-Q page:7) |
| Q3 10-Q | Same consolidated perimeter | Three and nine months ended September 30, 2026 and 2025; balance sheet at September 30, 2026 and December 31, 2025 | Unaudited | USD millions (Q3 10-Q page:8) |
| Q1, Q2 and Q3 releases | Same perimeter, issuer presentation | Quarter and year to date | Unaudited, management-prepared, partly non-GAAP | USD millions |

### Financials and credit metrics

| Metric | FY2024 | FY2025 | 9M 2026 | LTM to Sep 30, 2026 | Basis and source |
| --- | --- | --- | --- | --- | --- |
| Total revenues | 163,071 | 194,777 | 154,170 | 203,895 | Reported (10-K FY2025 page:130; Q3 10-Q page:9); LTM calculated, C1 |
| Premium and service revenues | 145,505 | 174,581 | 134,135 | 178,862 | Reported; LTM calculated, C1 |
| Medical costs | 125,707 | 157,702 | 118,460 | 159,949 | Reported; LTM calculated, C1 |
| Health benefits ratio, issuer-defined (%) | 88.3 | 91.9 | 89.9 | Not supplied | Reported (10-K FY2025 page:107; Q3 10-Q page:42); no LTM ratio is printed |
| Earnings (loss) from operations | 3,175 | (7,623) | 2,752 | 1,007 | Reported; LTM calculated, C1 |
| Investment and other income | 1,784 | 1,572 | 1,175 | 1,544 | Reported; LTM calculated, C1 |
| Impairment | 13 | 7,311 | — | 513 | Reported as printed; the dash for 9M 2026 is a printed nil; LTM calculated, C1 |
| EBITDA, analyst-calculated, primary (before impairment, includes investment and other income) | 6,213 | 2,535 | 4,826 | 4,292 | Calculated, C2. The issuer prints no EBITDA |
| EBITDA excluding investment and other income | 4,429 | 963 | 3,651 | 2,748 | Calculated, C2 |
| Interest expense | 702 | 678 | 466 | 634 | Reported; LTM calculated, C1 |
| Interest paid (cash) | 688 | 647 | 438 | 627 | Reported (10-K FY2025 page:132; Q3 10-Q page:11); LTM calculated, C1 |
| Net earnings (loss) | 3,294 | (6,677) | 2,561 | 1,461 | Reported; LTM calculated, C1 |
| Net cash provided by operating activities | 154 | 5,088 | 4,287 | 4,724 | Reported; LTM calculated, C1. Includes timing items, see cash flow section |
| Capital expenditures | 644 | 767 | 568 | 781 | Reported; LTM calculated, C1 |
| Operating cash flow less capital expenditures | (490) | 4,321 | 3,719 | 3,943 | Calculated, C3 |
| Cash and cash equivalents (period end) | 14,063 | 17,888 | 20,700 | 20,700 | Reported (balance at September 30, 2026) |
| Unregulated cash and cash equivalents (period end) | 248 | 553 | 376 | 376 | Reported (10-K FY2025 page:110; Q3 10-Q page:46) |
| Total debt, carrying (period end) | 18,533 | 17,401 | 15,542 | 15,542 | Reported (10-K FY2025 page:158; Q3 10-Q page:20) |
| Total stockholders' equity (period end) | 26,500 | 20,033 | 22,283 | 22,283 | Reported (10-K FY2025 page:129; Q3 10-Q page:8) |
| Total debt / EBITDA (x) | 2.98 | 6.86 | Not applicable: balance over a nine-month flow | 3.62 | Calculated, C4 |
| Net debt / EBITDA (x), net of unregulated cash and equivalents | 2.94 | 6.65 | Not applicable: balance over a nine-month flow | 3.53 | Calculated, C4 |
| Total debt / EBITDA excluding investment and other income (x) | 4.18 | 18.07 | Not applicable: balance over a nine-month flow | 5.66 | Calculated, C4 |
| EBITDA / interest paid (x) | 9.03 | 3.92 | 11.02 | 6.85 | Calculated, C4 |
| EBITDA / interest expense (x) | 8.85 | 3.74 | 10.36 | 6.77 | Calculated, C4 |
| Debt to capital, issuer-defined (%) | 41.2 | 46.5 | 41.1 | 41.1 | Reported (10-K FY2025 page:112; Q3 10-Q page:47); recomputed, C5 |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 2.98 | 2.94 | x | Carrying total debt at December 31, 2024 over analyst EBITDA; net debt deducts unregulated cash and equivalents of 248. C4 |
| FY2025 | 6.86 | 6.65 | x | EBITDA adds back the 7,311 impairment (C2); the ratio is high because underlying earnings were low. Net debt deducts 553. C4 |
| LTM Q1 2026 | 5.70 | 5.49 | x | LTM to March 31, 2026 built from FY2025 and the first quarters. Net debt deducts 593. C4 |
| LTM Q2 2026 | 3.56 | 3.37 | x | LTM to June 30, 2026. Net debt deducts 885. C4 |
| LTM Q3 2026 | 3.62 | 3.53 | x | LTM to September 30, 2026; the issuer prints no EBITDA, so this is an analyst definition. Net debt deducts 376; consolidated cash is not used because it is mostly regulated. C4 |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 9.03 | x | Analyst EBITDA over interest paid of 688 (supplemental cash flow disclosure). C4 |
| FY2025 | 3.92 | x | Interest paid of 647. EBITDA is depressed by lower earnings. C4 |
| LTM Q1 2026 | 4.33 | x | Interest paid LTM of 664. C4 |
| LTM Q2 2026 | 7.19 | x | Interest paid LTM of 629. C4 |
| LTM Q3 2026 | 6.85 | x | Interest paid LTM of 627. Interest paid is total cash interest; no split by instrument is printed. C4 |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2024 | 14,063 | Not supplied: the prior revolving facility size is not stated in the supplied pages; only a drawn balance of 950 is printed | US$m | Cash is consolidated cash and cash equivalents, mostly held by regulated subsidiaries. Unregulated cash was 248 |
| Dec 31, 2025 | 17,888 | 4,000 | US$m | Revolver of 4,000 with no borrowings; letters of credit of 120 are not part of the revolver. Unregulated cash 553, of which 400 available for general corporate use |
| Mar 31, 2026 | 21,264 | 4,000 | US$m | No revolver borrowings; letters of credit of 113 are outside the revolver. Unregulated cash 593, of which 437 available |
| Jun 30, 2026 | 24,151 | 4,000 | US$m | No revolver borrowings; letters of credit of 113 are outside the revolver. Unregulated cash 885, of which 715 available. Cash includes state pass-through payments of about 4,500 |
| Sep 30, 2026 | 20,700 | 4,000 | US$m | No revolver borrowings (Q3 10-Q page:47). Unregulated cash 376, of which 175 available for general corporate use. Revolver matures March 5, 2030 |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 50 | US$m | Aggregate maturities as printed at December 31, 2025 (10-K FY2025 page:160), before 2026 repurchases |
| 2027 | 2,316 | US$m | As printed at December 31, 2025. The 2027 notes were repurchased by 1,647 par in the nine months and the remaining 569 par was redeemed in October 2026 (Q3 10-Q page:21) |
| 2028 | 2,400 | US$m | As printed at December 31, 2025; 200 par of the 2028 notes was repurchased in 2026 |
| 2029 | 3,377 | US$m | As printed at December 31, 2025 |
| 2030 | 5,850 | US$m | As printed at December 31, 2025; the two 2030 note series are 2,000 and 2,200 and the remainder is not itemized, consistent with the Term Loan Facility maturing with the credit agreement on March 5, 2030 |
| Thereafter | 3,500 | US$m | As printed at December 31, 2025 (the 2031 notes). The printed total of 17,493 is not identical to the sum of the debt table lines, see gaps |

### Reported statements of operations

| Line (as printed) | Q1 2026 | Q2 2026 | Q3 2026 | Q3 2025 | 9M 2026 | 9M 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Premium | 43,887 | 43,582 | 44,370 | 44,126 | 131,839 | 127,578 | 171,556 | 142,303 |
| Service | 768 | 793 | 735 | 772 | 2,296 | 2,276 | 3,025 | 3,202 |
| Premium and service revenues | 44,655 | 44,375 | 45,105 | 44,898 | 134,135 | 129,854 | 174,581 | 145,505 |
| Premium tax | 5,289 | 9,204 | 5,542 | 4,792 | 20,035 | 15,198 | 20,196 | 17,566 |
| Total revenues | 49,944 | 53,579 | 50,647 | 49,690 | 154,170 | 145,052 | 194,777 | 163,071 |
| Medical costs | 38,303 | 39,029 | 41,128 | 40,902 | 118,460 | 116,213 | 157,702 | 125,707 |
| Cost of services | 702 | 729 | 675 | 651 | 2,106 | 1,990 | 2,670 | 2,729 |
| Selling, general and administrative expenses | 3,397 | 3,103 | 3,235 | 3,145 | 9,735 | 9,534 | 12,904 | 12,400 |
| Depreciation expense | 134 | 139 | 138 | 147 | 411 | 430 | 590 | 549 |
| Amortization of acquired intangible assets | 166 | 161 | 161 | 170 | 488 | 516 | 685 | 692 |
| Premium tax expense | 5,381 | 9,220 | 5,617 | 4,886 | 20,218 | 15,449 | 20,538 | 17,806 |
| Impairment | — | — | — | 6,743 | — | 6,798 | 7,311 | 13 |
| Earnings (loss) from operations | 1,861 | 1,198 | (307) | (6,954) | 2,752 | (5,878) | (7,623) | 3,175 |
| Investment and other income | 407 | 435 | 333 | 450 | 1,175 | 1,203 | 1,572 | 1,784 |
| Gain (loss) on debt extinguishment | (5) | 6 | 1 | — | 2 | — | 1 | — |
| Interest expense | (164) | (153) | (149) | (170) | (466) | (510) | (678) | (702) |
| Earnings (loss) before income tax | 2,099 | 1,486 | (122) | (6,674) | 3,463 | (5,185) | (6,728) | 4,257 |
| Income tax expense (benefit) | 560 | 399 | (57) | (42) | 902 | 392 | (51) | 963 |
| Net earnings (loss) | 1,539 | 1,087 | (65) | (6,632) | 2,561 | (5,577) | (6,677) | 3,294 |

Sources: Q1 10-Q page:7; Q2 10-Q page:8; Q3 10-Q page:9; 10-K FY2025 page:129 and page:130. Interest expense is printed in parentheses as a deduction and kept signed. The Q1 statement prints no impairment row; its totals recompute without one (C6). The Q3 2025 impairment of 6,743 and the FY2025 impairment of 7,311 include a goodwill impairment; the 10-K FY2025 non-GAAP note cites "goodwill impairment of $6,723 million" (10-K FY2025 page:11).

### Reported balance sheet and capital structure items

| Line (as printed) | Dec 31, 2024 | Dec 31, 2025 | Mar 31, 2026 | Jun 30, 2026 | Sep 30, 2026 |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 14,063 | 17,888 | 21,264 | 24,151 | 20,700 |
| Short-term investments | 2,622 | 2,432 | 2,477 | 2,906 | 2,886 |
| Long-term investments | 17,429 | 17,035 | 16,599 | 16,302 | 14,794 |
| Restricted deposits | 1,390 | 1,412 | 1,432 | 1,487 | 1,470 |
| Total assets | 82,445 | 76,747 | 81,175 | 83,012 | 79,280 |
| Medical claims liability | 18,308 | 20,544 | 20,627 | 20,262 | 21,495 |
| Current portion of long-term debt | 110 | 50 | 63 | 75 | 88 |
| Long-term debt | 18,423 | 17,351 | 16,308 | 16,030 | 15,454 |
| Total liabilities | 55,935 | 56,691 | 59,648 | 60,355 | 56,973 |
| Total stockholders' equity | 26,500 | 20,033 | 21,502 | 22,634 | 22,283 |
| Issuer debt to capitalization (%) | 41.2 | 46.5 | 43.2 | 41.6 | 41.1 |

Sources: 10-K FY2025 page:129; Q1 10-Q page:7; Q2 10-Q page:7; Q3 10-Q page:8; ratios from 10-K FY2025 page:112, Q1 10-Q page:36, Q2 10-Q page:44 and Q3 10-Q page:47. Total debt at each date is the sum of the current portion and long-term debt and equals the printed debt-note total (C5). The December 31, 2025 comparative in the 2026 10-Qs shows accounts payable and accrued expenses of 13,796, total current liabilities of 36,718 and other long-term liabilities of 1,789, where the 10-K FY2025 prints 13,774, 36,696 and 1,811 (Q3 10-Q page:8; 10-K FY2025 page:129); total liabilities are unchanged at 56,691. This is the reclassification CP-0 flagged.

### Reported cash flows

| Line (as printed) | Q1 2026 | 6M 2026 | 9M 2026 | 9M 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- |
| Net earnings (loss) | 1,539 | 2,626 | 2,561 | (5,577) | (6,677) | 3,294 |
| Depreciation and amortization | 300 | 600 | 899 | 946 | 1,275 | 1,241 |
| Net cash provided by operating activities | 4,366 | 7,956 | 4,287 | 4,651 | 5,088 | 154 |
| Capital expenditures | (200) | (374) | (568) | (554) | (767) | (644) |
| Proceeds from long-term debt | — | — | — | 750 | 750 | 1,300 |
| Payments and repurchases of long-term debt | (1,046) | (1,304) | (1,872) | (1,708) | (1,895) | (622) |
| Common stock repurchases | (29) | (33) | (57) | (473) | (475) | (3,124) |
| Net cash (used in) financing activities | (1,063) | (1,322) | (1,906) | (1,434) | (1,621) | (2,406) |
| Interest paid | 146 | 302 | 438 | 458 | 647 | 688 |
| Income taxes paid, net | (19) | (225) | 15 | 540 | 448 | 1,002 |

Sources: Q1 10-Q page:9; Q2 10-Q page:10; Q3 10-Q page:11; 10-K FY2025 page:131 and page:132. All cash flow columns are cumulative. Discrete quarterly figures are derived in C7. The Q3 10-Q states "the quarter-to-date operating cash flow use of $3,669 million" (Q3 10-Q page:12), which equals the derivation. Income taxes are printed as net refunds for Q1 and six months 2026 and shown here as negative.

### Segment information

| Line | Q3 2026 | Q3 2025 | 9M 2026 | 9M 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- |
| Medicaid premium and service revenues | 24,039 | 23,171 | 70,401 | 67,193 | 90,238 | 83,851 |
| Medicare premium and service revenues | 11,263 | 9,391 | 32,646 | 27,600 | 37,210 | 23,032 |
| Commercial premium and service revenues | 8,700 | 10,992 | 27,612 | 31,211 | 42,003 | 33,702 |
| Other and eliminations premium and service revenues | 1,103 | 1,344 | 3,476 | 3,850 | 5,130 | 4,920 |
| Medicaid segment gross margin | 1,528 | 1,532 | 4,534 | 4,081 | 5,690 | 6,246 |
| Medicare segment gross margin | 699 | 538 | 3,418 | 2,605 | 2,983 | 2,595 |
| Commercial segment gross margin | 958 | 1,116 | 5,263 | 4,604 | 5,101 | 7,663 |
| Other and eliminations segment gross margin | 117 | 159 | 354 | 361 | 435 | 565 |
| Consolidated segment gross margin | 3,302 | 3,345 | 13,569 | 11,651 | 14,209 | 17,069 |

Sources: Q3 10-Q page:23 and page:24; 10-K FY2025 page:169 and page:170. Segment gross margin is defined as "premium and service revenues less medical costs and cost of services" (Q3 10-Q page:23). The segment columns add to the consolidated totals (C6).

### Debt register at September 30, 2026

| Instrument (as printed) | Maturity | Coupon | Carrying Sep 30, 2026 | Carrying Dec 31, 2025 |
| --- | --- | --- | --- | --- |
| $2,500 million Senior Notes | December 15, 2027 | 4.25% | 568 | 2,211 |
| $2,300 million Senior Notes | July 15, 2028 | 2.45% | 2,101 | 2,302 |
| $3,500 million Senior Notes | December 15, 2029 | 4.625% | 3,277 | 3,277 |
| $2,000 million Senior Notes | February 15, 2030 | 3.375% | 2,000 | 2,000 |
| $2,200 million Senior Notes | October 15, 2030 | 3.00% | 2,200 | 2,200 |
| $2,200 million Senior Notes | March 1, 2031 | 2.50% | 2,200 | 2,200 |
| $1,300 million Senior Notes | August 1, 2031 | 2.625% | 1,300 | 1,300 |
| Total senior notes | — | — | 13,646 | 15,490 |
| Term Loan Facility | March 5, 2030 | Floating, benchmark plus margin | 1,963 | 2,000 |
| Revolving Credit Facility, 4,000 commitment | March 5, 2030 | Floating | 0 | 0 |
| Debt issuance costs | — | — | (67) | (89) |
| Total debt | — | — | 15,542 | 17,401 |
| Less: current portion | — | — | (88) | (50) |
| Long-term debt | — | — | 15,454 | 17,351 |

Sources: Q3 10-Q page:20; 10-K FY2025 page:158 and page:159. The revolver rows reflect "no borrowings outstanding under our Revolving Credit Facility" (Q3 10-Q page:47). The notes are described as senior unsecured notes in the fair value note (10-K FY2025 page:136); the security and guarantors of the credit facilities are Not supplied. The issuer of all instruments is Centene Corporation (10-K FY2025 page:158). Senior notes carrying amounts are shown net of any unamortized discount or premium as printed; face amounts at Sep 30, 2026 are not separately printed.

Repurchases and redemptions during 2026 (Q3 10-Q page:21): par value Senior Notes due 2027 repurchased 1,647 in the nine months (500 in the third quarter); par value Senior Notes due 2028 repurchased 200 for 190 in the nine months; "In October 2026, the Company redeemed in full at par the remaining $569 million of its par value Senior Notes due 2027 through the debt repurchase program" (Q3 10-Q page:21). The repurchase program authorization was raised by 1,000 in February 2026, 750 in May 2026 and 2,000 in October 2026, leaving 426 available at September 30, 2026 and 1,857 at October 27, 2026. The Q3 release states that debt was "reduced by $1.1 billion since June 30, 2026" (Q3 release page:1); this agrees with the filed figures (C8).

### Claims and obligations outside the debt figure

| Item | Amount | Inside or outside total debt | Source and period |
| --- | --- | --- | --- |
| Letters of credit not part of the revolver | 113 | Outside | Q3 10-Q page:47, September 30, 2026 |
| Surety bonds | 750 | Outside | Q3 10-Q page:47, September 30, 2026 |
| Operating lease liabilities | 761 | Outside | 10-K FY2025 page:160, December 31, 2025; no later figure printed in the supplied 10-Qs |
| Part D receivable sale: maximum outstanding purchase amount | 4,250 | Outside, off-balance-sheet for receivables sold | Q3 10-Q page:14 |
| Part D receivable sale: remaining purchase amount permitted | 3,250 | Outside | Q3 10-Q page:15, September 30, 2026 |
| 2025 plan year Part D receivables still recognized and eligible | 2,668 | On balance sheet as receivables | Q3 10-Q page:15 |
| Participating interest sold in March 2026 | 1,000 | Derecognized from receivables | Q3 10-Q page:15; net proceeds 970 |
| State pass-through payments in accounts payable and accrued expenses | 1,635 | Outside, operating liability | Q3 10-Q page:12, September 30, 2026 (about 4,500 at June 30, 2026) |
| Medical claims liability | 21,495 | Outside, operating liability | Q3 10-Q page:8 |
| Liabilities held for sale (Magellan Health) | 312 | Outside, within accounts payable and accrued expenses | Q3 10-Q page:13 |
| Pensions and retiree medical | Not supplied | Not applicable | A search of the supplied sources found no defined benefit pension or retiree medical disclosure, only a 401(k) plan mention (10-K FY2025 page:40); the absence is not evidence of zero |
| Securities class action and derivative suits | Not supplied: no loss estimate | Outside | Q3 10-Q page:26 states "amounts accrued for legal proceedings and regulatory matters were not material" |

### Liquidity at September 30, 2026

| Component (as printed or derived) | Amount | Source |
| --- | --- | --- |
| Consolidated cash and cash equivalents | 20,700 | Q3 10-Q page:8; mostly held by regulated subsidiaries |
| Unregulated cash and cash equivalents | 376 | Q3 10-Q page:46 |
| Of which available for general corporate use | 175 | Q3 10-Q page:46 |
| Revolving Credit Facility commitment | 4,000 | Q3 10-Q page:47 |
| Revolving Credit Facility borrowings | 0 | Q3 10-Q page:47 ("no borrowings outstanding") |
| Letters of credit that reduce revolver availability | 0 | Letters of credit "were not part of our Revolving Credit Facility" (Q3 10-Q page:47) |
| Undrawn committed facility | 4,000 | Calculated, C9 |
| Parent-level liquidity: cash available for general corporate use plus undrawn revolver | 4,175 | Calculated, C9 |
| Dividends received from regulated subsidiaries, nine months | 1,700 | Q3 10-Q page:49 ("$1.7 billion") |
| Capital contributions to regulated subsidiaries, nine months | 623 | Q3 10-Q page:49 |
| Short-term and long-term investments and restricted deposits | 19,150 | Calculated, C9 (2,886 + 14,794 + 1,470) |

Unregulated cash available for general corporate use was 400 at December 31, 2025, 437 at March 31, 2026, 715 at June 30, 2026 and 175 at September 30, 2026 (10-K FY2025 page:110; Q1 10-Q page:35; Q2 10-Q page:42; Q3 10-Q page:46). The revolver matures with the credit agreement on March 5, 2030, outside twelve months. No credit facility expires within twelve months of September 30, 2026; the term of the receivable purchase agreement is Not supplied. The current portion of long-term debt is 88.

### Covenants as disclosed

| Test | Level | Reported figure | Headroom |
| --- | --- | --- | --- |
| Maximum debt-to-capital ratio under the credit agreement, tested quarterly | "may not exceed 0.60 to 1.00" (Q3 10-Q page:47); a step-up to 0.65 to 1.00 upon election after a material acquisition (10-K FY2025 page:159) | 41.1% at September 30, 2026, defined by the issuer as total debt divided by the sum of total debt and total equity (Q3 10-Q page:47) | Indicative only: 60.0 less 41.1 is 18.9 percentage points on the issuer's own ratio definition (C5). The agreement's definition is not supplied, so covenant headroom is Not calculable |
| Indenture covenants of the senior notes | "restrictive covenants of Centene Corporation" (10-K FY2025 page:158) | In compliance (10-K FY2025 page:158, December 31, 2025) | Terms are Not supplied |
| Compliance statement | "we were in compliance with all covenants" (Q3 10-Q page:47) | September 30, 2026 | Management statement |

### Non-GAAP and definitions

The issuer reports no EBITDA or Adjusted EBITDA in any supplied source (a text search of all seven sources for "EBITDA" returns nothing). The issuer reports adjusted diluted EPS: Q3 2026 0.58 against 0.50 in Q3 2025, and 6.45 for the nine months against 3.26 (Q3 release page:6), with 2026 guidance of greater than 5.20 (Q3 release page:4). GAAP diluted EPS was a loss of 0.14 in Q3 2026 and earnings of 5.15 for nine months (Q3 10-Q page:9). Adjusted EPS excludes severance and enterprise optimization costs. The Q3 10-Q states severance and third-party vendor costs of 297 in the quarter and 358 in nine months included in selling, general and administrative expenses (Q3 10-Q page:26). Interest expense guidance for 2026 is "$600 million to $620 million" (Q3 release page:4), a management forward-looking statement.

### Narrative review

- Leverage: total debt fell from 17,401 to 15,542 between December 31, 2025 and September 30, 2026, and the analyst-calculated LTM ratio is 3.62x against 6.86x for FY2025. Mechanism: the FY2025 ratio was inflated by lower earnings, since the health benefits ratio rose to 91.9% from 88.3% in FY2024 (EBITDA already adds back the impairment), while 2026 repurchases of 1,847 par of the 2027 and 2028 notes reduced the numerator. Implication: leverage has returned toward the FY2024 level of 2.98x but is not yet there, and it rests on an earnings recovery that is not evenly spread across the year.
- Earnings shape: calculated EBITDA was 2,568 in Q1 2026, 1,933 in Q2 and 325 in Q3, against 556 in Q3 2025 (C7). The health benefits ratio rose through the year from 87.3% in Q1 to 89.6% in Q2 and 92.7% in Q3 (Q1 10-Q page:32; Q2 10-Q page:37; Q3 10-Q page:40). Implication: the LTM ratio overstates the run rate that the second half implies; the creditor should watch fourth quarter results before treating 3.62x as stable.
- Coverage: LTM EBITDA over interest paid is 6.85x against 3.92x for FY2025 and 9.03x for FY2024. Implication: coverage is adequate and improving, helped by lower interest expense (634 LTM against 678 in FY2025). Interest guidance for 2026 of 600 to 620 implies a fourth quarter of 134 to 154 against 466 in nine months (C10).
- Cash flow quality: nine-month operating cash flow of 4,287 includes net proceeds of 970 from the March 2026 sale of Part D receivables, which the filing records as operating cash flow ("The cash proceeds and associated loss on sale of receivables are recorded as operating cash flows", Q3 10-Q page:14), and the third quarter shows an operating cash outflow of 3,669 as state pass-through payments of about 4,500 held at June 30, 2026 were paid through. Implication: LTM operating cash flow less capital expenditures of 3,943 is not a recurring free cash flow measure; excluding the 970 gives 2,973 (C11).
- Liquidity: consolidated cash is 20,700 but unregulated cash is 376 and the part available for general corporate use is 175. The undrawn revolver of 4,000 has no letters of credit against it. Implication: parent liquidity is 4,175 on the derived measure and depends on the revolver and on subsidiary dividends (1.7 billion in nine months), not on headline cash. The 2027 notes are cleared; the next maturity in the debt register is the 2028 notes of 2,101.
- Perimeter and claims: Magellan Health assets and liabilities of 312 each are held for sale (Q3 10-Q page:13), and the Part D receivable program of up to 4,250 is a financing source that sits outside debt. Implication: perimeter and funding-source changes make period comparisons less clean.
- Data quality: every recomputed total ties (C5, C6). Known inconsistencies are the 2025 comparative reclassification and the 10-K maturity total (gaps). Source quality is high for filed statements; releases add no independent facts.
- Definition risks: EBITDA, net debt and parent liquidity are analyst constructs; the issuer's debt-to-capital ratio is the only leverage metric the issuer prints; the covenant definition is unknown; HBR is issuer-defined.
- Key gaps: executed credit agreement and indentures; guarantors; receivable purchase agreement; discrete quarterly cash flow statements; undrawn facility size at December 31, 2024.

### Readiness for downstream modules

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1A | Sufficient with limitations | Statements, segments, debt register, receivable sale, held-for-sale perimeter and subsequent events above |
| CP-2 | Sufficient with limitations | Credit metrics on stated bases with calculation IDs; covenant headroom and parent liquidity are indicative |
| CP-5 | Sufficient | Every figure has a locator or a calculation ID |

### Quality review of claims

| Claim | Material | Lineage | Note |
| --- | --- | --- | --- |
| Total debt was 15,542 at September 30, 2026 | Yes | Directly Sourced | Q3 10-Q page:20 and page:8 |
| LTM total debt / EBITDA is 3.62x | Yes | Calculated | EBITDA is analyst-defined, C2 and C4 |
| Cash available for general corporate use was 175 | Yes | Directly Sourced | Q3 10-Q page:46 |
| Parent-level liquidity is 4,175 | Yes | Calculated | Combines two sourced figures, C9 |
| Debt to capital is 41.1% against a 0.60 maximum | Yes | Directly Sourced | Covenant definition not supplied |
| Covenant headroom | Yes | Insufficient Information | Agreement not supplied |

Open quality findings: one MATERIAL finding, covenant definitions and executed agreements are not supplied. Two MINOR findings: the 10-K maturity total differs from its debt table lines; 2025 comparatives were reclassified in the 2026 filings.

## Calculations

All inputs are USD millions copied from the cited chunks. Ratios are rounded half up to two decimals and percentages to one decimal.

| ID | Formula | Inputs and locators | Result |
| --- | --- | --- | --- |
| C1 | LTM to Sep 30, 2026 = FY2025 + 9M 2026 - 9M 2025 | Total revenues 194,777 + 154,170 - 145,052; premium and service revenues 174,581 + 134,135 - 129,854; medical costs 157,702 + 118,460 - 116,213; earnings from operations -7,623 + 2,752 - (-5,878); investment and other income 1,572 + 1,175 - 1,203; impairment 7,311 + nil (printed dash) - 6,798; interest expense 678 + 466 - 510; interest paid 647 + 438 - 458; net earnings -6,677 + 2,561 - (-5,577); operating cash flow 5,088 + 4,287 - 4,651; capital expenditures 767 + 568 - 554 (10-K FY2025 page:130 to page:132; Q3 10-Q page:9, page:11) | 203,895; 178,862; 159,949; 1,007; 1,544; 513; 634; 627; 1,461; 4,724; 781. The LTM impairment of 513 equals the pending divestiture impairment of 513 recorded in December 2025 (Q3 10-Q page:14) |
| C2 | EBITDA = earnings (loss) from operations + investment and other income + depreciation expense + amortization of acquired intangible assets + impairment; the secondary basis omits investment and other income | FY2024: 3,175 + 1,784 + 549 + 692 + 13; FY2025: -7,623 + 1,572 + 590 + 685 + 7,311; 9M 2026: 2,752 + 1,175 + 411 + 488 + 0; LTM Q3 2026: 1,007 + 1,544 + 571 + 657 + 513, where LTM depreciation 590 + 411 - 430 = 571 and amortization 685 + 488 - 516 = 657; LTM Q1 2026 = FY2025 EBITDA + Q1 2026 EBITDA - Q1 2025 EBITDA, with Q1 2025 1,534 + 382 + 142 + 173 + 0 = 2,231, so 2,535 + 2,568 - 2,231; LTM Q2 2026 = 2,535 + 4,501 - 2,513, where six-month EBITDA is 3,059 + 842 + 273 + 327 + 0 = 4,501 (2026) and 1,076 + 753 + 283 + 346 + 55 = 2,513 (2025) | Primary: 6,213; 2,535; 4,826; 4,292; LTM Q1 2,872; LTM Q2 4,523. Secondary: 4,429; 963; 3,651; 2,748. Debt extinguishment gains and losses are excluded |
| C3 | Operating cash flow less capital expenditures | FY2024 154 - 644; FY2025 5,088 - 767; 9M 2026 4,287 - 568; LTM 4,724 - 781 | -490; 4,321; 3,719; 3,943 |
| C4 | Total debt / EBITDA; (total debt - unregulated cash and equivalents) / EBITDA; EBITDA / interest paid; EBITDA / interest expense | Dec 31, 2024: 18,533 and 248 over 6,213; interest paid 688; interest expense 702. Dec 31, 2025: 17,401 and 553 over 2,535; 647; 678. Mar 31, 2026: 16,371 and 593 over 2,872; interest paid LTM 647 + 146 - 129 = 664. Jun 30, 2026: 16,105 and 885 over 4,523; interest paid LTM 647 + 302 - 320 = 629. Sep 30, 2026: 15,542 and 376 over 4,292; 627; 634. Secondary basis: 18,533 / 4,429; 17,401 / 963; 15,542 / 2,748. 9M 2026: 4,826 / 438; 4,826 / 466 | Total debt / EBITDA: 2.98; 6.86; 5.70; 3.56; 3.62. Net: 2.94; 6.65; 5.49; 3.37; 3.53. Secondary: 4.18; 18.07; 5.66. EBITDA / interest paid: 9.03; 3.92; 4.33; 7.19; 6.85; 9M 2026 11.02. EBITDA / interest expense: 8.85; 3.74; 6.77 (LTM Q3); 9M 2026 10.36. Dec 31, 2024 interest expense input is 702 |
| C5 | Debt to capital = total debt / (total debt + total equity); total debt = current portion + long-term debt | Sep 30, 2026: (88 + 15,454) = 15,542; 15,542 / (15,542 + 22,283). Dec 31, 2024: 18,533 / (18,533 + 26,500). Dec 31, 2025: 17,401 / (17,401 + 20,033). Indicative headroom: 60.0 - 41.1. Debt-note totals 17,401 (Dec 2025), 16,371 (Mar 2026), 16,105 (Jun 2026), 15,542 (Sep 2026) equal current plus long-term debt on each balance sheet | 41.1%; 41.2%; 46.5%, all equal to the issuer's printed ratios; 18.9 percentage points |
| C6 | Statement totals from components | For each of Q1, Q2, Q3 2026, Q3 2025, 9M 2026, 9M 2025, FY2025, FY2024 and 6M 2026: premium + service + premium tax = total revenues; medical costs + cost of services + SG&A + depreciation + amortization + premium tax expense + impairment = total operating expenses; total revenues - total operating expenses = earnings from operations; plus investment and other income, debt extinguishment and interest expense = pretax; less tax = net earnings. Q3 2026 balance sheet: 45,461 + 14,794 + 1,470 + 2,109 + 10,835 + 4,042 + 569 = 79,280; 39,068 + 15,454 + 719 + 1,732 = 56,973; 56,973 + 24 + 22,283 = 79,280. Segment columns: Q3 2026 24,039 + 11,263 + 8,700 + 1,103 = 45,105; gross margin 1,528 + 699 + 958 + 117 = 3,302; the same additions hold for the other segment periods. Quarterly sums: operating earnings 1,861 + 1,198 - 307 = 2,752; pretax 2,099 + 1,486 - 122 = 3,463; net earnings 1,539 + 1,087 - 65 = 2,561 | All equal the printed figures |
| C7 | Discrete quarters from cumulative figures | EBITDA Q1 2026 1,861 + 407 + 134 + 166 + 0; Q2 2026 1,198 + 435 + 139 + 161 + 0; Q3 2026 -307 + 333 + 138 + 161 + 0; Q3 2025 -6,954 + 450 + 147 + 170 + 6,743. Operating cash flow Q2 7,956 - 4,366; Q3 4,287 - 7,956. Interest paid Q2 302 - 146; Q3 438 - 302 | EBITDA 2,568; 1,933; 325 (sum 4,826 equals the nine-month figure); 556. Operating cash flow Q2 3,590; Q3 -3,669 (equals the printed 3,669 use, sum 4,366 + 3,590 - 3,669 = 4,287). Interest paid 156; 136 |
| C8 | Check of management claim of debt reduction since June 30, 2026 | (16,105 - 15,542) + 569 redeemed in October | 1,132, consistent with "$1.1 billion" |
| C9 | Liquidity derivations | Undrawn revolver 4,000 - 0 borrowings - 0 letters of credit under the revolver; parent-level liquidity 175 + 4,000; investments and restricted deposits 2,886 + 14,794 + 1,470. The total with cash 20,700 is 39,850, equal to the Q3 release total of 39,850 (Q3 release page:14) | 4,000; 4,175; 19,150 |
| C10 | Implied fourth quarter interest expense from guidance | 600 - 466; 620 - 466 | 134 to 154 |
| C11 | Operating cash flow excluding the net receivable sale proceeds | LTM 4,724 - 970; nine months 4,287 - 970; LTM less capital expenditures 3,754 - 781 | 3,754; 3,317; 2,973 |
| C12 | Maturity schedule against debt table, December 31, 2025 | Total senior notes 15,490 + Term Loan Facility 2,000 = 17,490 against printed schedule total 17,493 (10-K FY2025 page:158, page:160); 17,490 - 89 = 17,401 | 3 difference, unreconciled; carried to gaps |

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Executed credit agreement and indentures not supplied; covenant definitions and guarantors unknown | Covenant headroom is Not calculable and guarantor structure unknown | Supply the executed Credit Agreement dated March 5, 2025 and the indentures |
| Issuer prints no EBITDA | All leverage and cover ratios use an analyst definition, C2 | Treat ratios as analyst-defined; compare with any issuer or agency definition if supplied |
| Cash flow statements are cumulative only; discrete quarters derived | Quarterly cash flow rests on subtraction (C7) | Check against quarterly filings when available |
| Receivable purchase agreement not supplied | Purchaser appetite, discount spread and recourse are known only from notes | Supply Exhibits 2.1 and 2.2 to the 10-K |
| Undrawn facility size at December 31, 2024 not supplied | Liquidity chart cell for that date is Not supplied | Supply the prior credit agreement terms or 2024 10-K |
| 10-K maturity schedule total 17,493 differs from its debt table lines (C12) | The 3 difference is unexplained | Confirm with issuer or treat as presentation difference |
| 2025 comparatives reclassified in the 2026 filings | Dec 31, 2025 comparatives differ by line from the 10-K | Use the 10-K for annual analysis, the 10-Qs for interim comparatives, and label the choice |
| Pension and retiree medical disclosure not located | Cannot confirm whether any such claim exists | Confirm in the full 10-K note set if needed |
| Face amount of notes at September 30, 2026 not separately printed | Carrying amounts are used for the register | Use the October 2026 redemption and repurchase notes for par movements |
| Events after October 27, 2026 not supplied | Debt and liquidity at the as-of date may differ | Supply later filings |

## Next module

- CP-1A: carry the Part D receivable sale, the Magellan held-for-sale perimeter, the segment shifts (Medicare revenue up, Commercial revenue down) and the October 2026 note redemption as dated facts; label anything after October 27, 2026 as Not supplied.
- CP-2: read leverage on the analyst-defined EBITDA with the front-loaded earnings caution; treat parent liquidity (4,175) and covenant headroom as indicative; carry the covenant-definition and guarantor gaps.
- CP-5: trace each figure to its locator or calculation ID; treat the releases as duplicative of the filings.
