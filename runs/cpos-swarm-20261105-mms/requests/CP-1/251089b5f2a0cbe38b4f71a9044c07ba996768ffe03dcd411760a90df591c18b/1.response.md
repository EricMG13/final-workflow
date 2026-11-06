# CP-1 — Financial base: MAXIMUS, INC. (mms)

## Request

- Issuer: MAXIMUS, INC. (issuer id `mms`; the registrant is "Maximus, Inc.", NYSE: MMS), as of 2026-11-05, information cutoff 2026-11-05.
- Periods. Maximus has a fiscal year ending September 30. The context labels are read as: current period `q3-2026` = fiscal Q3 2026, the three months ended June 30, 2026 (the nine months ended June 30, 2026 are also shown); prior period `fy-2025` = the fiscal year ended September 30, 2025. FY2024 is the fiscal year ended September 30, 2024. LTM means the twelve months ended on the stated quarter-end, built as the last fiscal year plus the year-to-date less the prior-year year-to-date (calculation C1). The quarter ended September 30, 2026 is fiscal Q4 2026 and is not supplied.
- Reporting currency USD (context). Statements are printed in USD thousands; MD&A text and the releases also use USD millions and billions. Units are labelled wherever used.
- Perimeter: the registrant's consolidated statements. Maximus files alone; no parent is named, and there is no separate borrower or subsidiary-issuer statement in the sources, so no parent-versus-issuer split arises.
- Scope: reported financial statements, debt and liquidity, covenants as reported, cash flow, claims outside the debt figure, and the latest quarter and events after it, for the credit snapshot. Reported facts are separated from calculations. Calculations are numbered C1 to C16 under `## Calculations`.
- Upstream: the CP-0 readiness handoff rated this module READY_WITH_LIMITATIONS. Its limits are carried forward here: Credit Agreement text and EBITDA definition not supplied, guarantors not named, no ratings, nothing after August 6, 2026, letters of credit and non-US facilities not quantified at June 30, 2026. Where this answer extends or corrects CP-0 it says so under `### Reconciliation to the readiness handoff`.
- Execution: host session; no provider was called.

## Sources

Locators are `page:N` chunks of the pinned `.jsonl` text, not printed page numbers. "10-K" is the fiscal 2025 annual report; "Q1 10-Q", "Q2 10-Q" and "Q3 10-Q" are the quarterly reports for the quarters ended December 31, 2025, March 31, 2026 and June 30, 2026; "Q1 release", "Q2 release" and "Q3 release" are the Exhibit 99.1 earnings releases dated February 5, May 7 and August 6, 2026.

| Source | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-09-30_mms-20250930.htm.jsonl | 962786100737da7c8a25bf2c0b0d8b7bba5fc8fe85f1a63dc4a22607d3101fd0 | Audited FY2025 and FY2024 statements, debt note, covenants, adjusted EBITDA, leases, receivable sales, litigation |
| 10-Q_2025-12-31_mms-20251231.htm.jsonl | 1ece10b3b4a1f72edf52da31ebe99ab2543998f22e423edd0be2ded3496f545d | Q1 FY2026 statements, debt, covenant tables, adjusted EBITDA, interest payments |
| 10-Q_2026-03-31_mms-20260331.htm.jsonl | 72c28dae66fdf3271ecd55284a1e9ffd02e932cd689052dff69253e7614fe8a8 | Q2 FY2026 statements, debt, covenant tables, adjusted EBITDA, interest payments |
| 10-Q_2026-06-30_mms-20260630.htm.jsonl | e0ee49037a76362fa1359adeb6f1d6ec0af3bf048fce3d62f4b088d4d2e2d60b | Q3 FY2026 statements, debt, swaps, liquidity, covenants, segments, subsequent events |
| EX-99.1_2026-02-05_mms-2025x12x31x8kxex991.htm.jsonl | ff62eabdd3d1037513edc754533c1c20140d9d029aa9713e0d89283ab79659d9 | Q1 release: leverage statement, guidance (attributed) |
| EX-99.1_2026-05-07_mms-2026x03x31x8kxex991.htm.jsonl | 3cc2b6ddbaacd127b88b399aaed54a4ba71be05c3b12c29939da2343ffcad4ec | Q2 release: leverage statement, guidance (attributed) |
| EX-99.1_2026-08-06_mms-2026x06x30x8kxex991.htm.jsonl | 78b1fb3302628c3c36cbd9a44260145bf92a755c30565ab852ed03fa9e5e9aa0 | Q3 release: discrete quarter cash flow, guidance, adjusted EBITDA, pipeline (attributed) |
| context | 427dc9f0877ed950bde305fcdd6af025bde473794c90eea607afca11f0c6cd79 | User run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | b2c3bb0b1f4af634e0abd5fcab811ad35e641a5d0e7ca14dd9cdc832dae5d76e | Source readiness, identity and period conventions, limitations carried forward |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Net debt to issuer-adjusted EBITDA rose from 1.60x to 2.25x in nine months, and the reported covenant ratio is 2.00 against a 4.00 maximum. Cash flow is seasonal and full-year guidance rests on fourth-quarter collections. | Medium | Credit Agreement definitions and letter of credit usage are not supplied, and nothing after August 6, 2026 is covered, including fiscal fourth quarter results. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt principal rose by 306,673 thousand US dollars between September 30, 2025 and June 30, 2026 while unrestricted cash fell to 56,953 thousand. | Leverage is still moderate, but the reported covenant ratio of 2.00 now sits at the bottom of management's stated range of 2x to 3x. | High |
| Nine-month operating cash flow was an outflow of 179,863 thousand and buybacks plus dividends took 256,356 thousand. | Shareholder returns were funded by borrowing, so deleveraging depends on the fourth-quarter collections management expects. | High |
| Liquidity at June 30, 2026 was 786,953 thousand: 56,953 of cash and about 730,000 of revolver capacity. | Near-term obligations are covered, but cash is thin and the revolver is the buffer; letters of credit are not netted. | Medium |
| Reported covenant leverage is 2.00 against a 4.00 maximum, and interest cover is 8.72 against a 3.00 minimum. | Headroom is wide: covenant EBITDA could fall 50.0% before the leverage test binds, subject to the unsupplied definition. | Medium |
| August 2026 guidance lowered adjusted EPS, adjusted EBITDA margin and free cash flow after a customer-directed contract modification effective July 1, 2026. | Earnings are lower through December 31, 2026, when the modification ends, extending the pressure into fiscal 2027. | Medium |

### Financial base view

The reported financial base for MAXIMUS, INC. supports a moderately levered, covenant-compliant credit view at June 30, 2026, with the issuer-adjusted measures and the Credit Agreement measures kept apart. Revenue for the nine months ended June 30, 2026 was 3,929,984 thousand against 4,112,861 thousand a year earlier, operating income rose to 456,125 thousand from 405,427 thousand, and issuer-adjusted EBITDA was 550,768 thousand against 541,313 thousand; the operating income gain is largely explained by a 39,343 thousand divestiture charge in the prior-year figure, which the adjusted measure adds back. Net cash used in operating activities was 179,863 thousand against 220,000 thousand, which reflects the seasonal receivables build and, in the current year, delayed payments from a large federal contract, after 1.28 billion US dollars of receivables were sold to a bank. Total debt principal was 1,653,548 thousand against 1,346,875 thousand at September 30, 2025, and unrestricted cash fell to 56,953 thousand from 222,351 thousand, so net debt of 1,596,595 thousand is 2.25 times LTM issuer-adjusted EBITDA of 711,009 thousand (C5), up from 1.60 times. The issuer reports a Credit Agreement ratio of 2.00 against a 4.00 maximum, on its own EBITDA definition that adds 52,278 thousand of pro forma and other adjustments (C9). The stack is a single bank Credit Agreement: Term Loan A, Term Loan B and a 750,000 thousand revolver with 20,000 thousand drawn, secured by substantially all assets (10-K page:84); no bonds or indentures appear in the supplied sources. The nearest large maturity is 690,184 thousand in the year ending September 30, 2029. Open items are the Credit Agreement text and amendment terms, the receivable-sale balance outstanding, letters of credit, and the fiscal fourth quarter, which carries the collections that full-year free cash flow guidance requires (C13).

### Source context

| Source | Entity and perimeter | Periods | Statement kind | Units |
| --- | --- | --- | --- | --- |
| 10-K | Maximus, Inc. and consolidated subsidiaries | Years ended September 30, 2025, 2024 and 2023; balance sheets at September 30, 2025 and 2024 | Audited (KPMG LLP, report dated November 20, 2025, 10-K page:63; fiscal 2024 comparatives carry an Ernst & Young LLP report, page:64) | "(in thousands, except per share amounts)", USD (10-K page:64) |
| Q1 10-Q | Same consolidated perimeter | Three months ended December 31, 2025 and 2024; balance sheet at December 31, 2025 and September 30, 2025 | Unaudited | USD thousands (Q1 10-Q page:4) |
| Q2 10-Q | Same | Three and six months ended March 31, 2026 and 2025; balance sheet at March 31, 2026 and September 30, 2025 | Unaudited | USD thousands (Q2 10-Q page:4) |
| Q3 10-Q | Same | Three and nine months ended June 30, 2026 and 2025; balance sheet at June 30, 2026 and September 30, 2025 | Unaudited | USD thousands (Q3 10-Q page:4) |
| Q1, Q2, Q3 releases | Same, issuer presentation | Quarter and year-to-date | Unaudited; GAAP and non-GAAP | USD thousands in statements; millions and billions in text (Q3 release pages:2, 6) |

The 10-Q cash flow statements are year-to-date. The Q3 release prints a discrete three-month cash flow column (Q3 release page:7), which is used for Q3 FY2026 and Q3 FY2025 operating cash flow, capital expenditure and dividends. Discrete Q3 cash interest paid is the nine-month less six-month figure (C2).

### Financials and credit metrics

| Metric (USD thousands unless stated) | FY2024 | FY2025 | Q3 FY2025 | Q3 FY2026 | 9M FY2025 | 9M FY2026 | LTM Jun 30, 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue | 5,306,197 | 5,431,276 | 1,348,400 | 1,278,971 | 4,112,861 | 3,929,984 | 5,248,399 | Reported; 10-K page:64, Q3 10-Q page:4. LTM is C1 |
| Gross profit | 1,251,652 | 1,333,443 | 359,513 | 348,803 | 999,891 | 1,009,737 | 1,343,289 | Reported; same pages. LTM is C1 |
| Operating income | 488,499 | 528,289 | 165,672 | 161,428 | 405,427 | 456,125 | 578,987 | Reported; same pages. LTM is C1 |
| Interest expense | 82,440 | 84,080 | 22,657 | 23,878 | 61,648 | 66,805 | 89,237 | Reported; same pages. LTM equals the 89,237 in the Credit Agreement reconciliation (Q3 10-Q page:33) |
| Net income | 306,914 | 319,034 | 105,981 | 103,593 | 243,746 | 295,599 | 370,887 | Reported; same pages. LTM equals the printed 370,887 (Q3 10-Q page:33) |
| Depreciation and amortization of property, equipment and capitalized software | 33,957 | 41,669 | 9,607 | 11,874 | 27,502 | 37,091 | 51,258 | Cash flow line; 10-K page:65, Q3 release page:7. LTM equals the printed 51,258 (Q3 10-Q page:33) |
| Amortization of intangible assets | 91,570 | 92,047 | 23,010 | 20,187 | 69,041 | 60,785 | 83,791 | Reported; same pages. LTM equals the printed 83,791 |
| Adjusted EBITDA, issuer non-GAAP | 615,044 | 701,554 | 198,289 | 192,327 | 541,313 | 550,768 | 711,009 | Reported by the issuer (10-K page:59; Q3 10-Q page:36; Q3 release page:9). Adds back divestiture-related items, capitalized software impairment, intangibles amortization and depreciation; does not add back stock compensation. LTM is C1 |
| Consolidated EBITDA as defined by the Credit Agreement | 725,783 | 793,995 | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | 798,419 | Reported trailing twelve months at each fiscal year end and at June 30, 2026 (10-K page:54; Q3 10-Q page:33). Includes stock compensation, pro forma and other adjustments; not comparable with the issuer-adjusted measure (C9) |
| Net cash (used in) provided by operating activities | 515,258 | 429,372 | (182,718) | (124,987) | (220,000) | (179,863) | 469,509 | Reported; 10-K page:65, Q3 release page:7. Seasonal: the first nine months are outflows. LTM is C1 |
| Purchases of property, equipment and capitalized software | 114,190 | 63,213 | 15,488 | 11,980 | 55,686 | 28,752 | 36,279 | Reported as outflows (printed negative); same pages. LTM is C1 |
| Free cash flow (operating cash flow less purchases), issuer non-GAAP | 401,068 | 366,159 | (198,206) | (136,967) | (275,686) | (208,615) | 433,230 | Reported for FY2025, FY2024 (10-K page:51), Q3 and nine months (Q3 10-Q page:34; Q3 release page:9). LTM is C3 |
| Cash dividends paid | 72,901 | 68,710 | 16,904 | 17,278 | 51,865 | 51,437 | 68,282 | Reported financing line; 10-K page:65, Q3 release page:7. LTM is C1 |
| Purchases of Maximus common stock (cash) | 73,069 | 447,482 | — (nil as printed) | 49,917 | 306,443 | 204,919 | 345,958 | Reported financing line; 10-K page:66, Q3 release page:7. The Q3 FY2025 cell prints a dash, which is nil for that quarter; nine-month FY2025 purchases fell in the first half. LTM is C1 |
| Cash interest paid | 78,955 | 82,562 | 22,042 | 23,131 | 60,809 | 64,526 | 86,279 | "Interest payments" (10-K page:93; Q3 10-Q page:19). Q3 columns are nine-month less six-month (Q2 10-Q page:17), C2. LTM is C1 |
| Cash and cash equivalents, unrestricted (balance) | 183,123 | 222,351 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 56,953 | Reported; 10-K page:64, Q3 10-Q page:5. LTM column holds the June 30, 2026 balance |
| Restricted cash (balance) | 52,640 | 38,108 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 96,296 | 10-K page:93; Q3 10-Q page:19. Held on behalf of customers; excluded from liquidity |
| Total debt principal (balance) | 1,145,819 | 1,346,875 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 1,653,548 | 10-K page:83, Q3 10-Q page:15. Term loans and revolver; equals the Credit Agreement "Funded Debt" (Q3 10-Q page:33) |
| Total debt, carrying value (balance) | 1,132,093 | 1,334,273 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 1,636,935 | Principal less unamortized issuance costs and discounts; same pages |
| Net debt, principal less unrestricted cash (balance) | 962,696 | 1,124,524 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 1,596,595 | Calculated, C4 |
| Revolver capacity not drawn, US$ millions (balance) | Not supplied | 747.0 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 730.0 | 750.0 less 3.0 of letters of credit at September 30, 2025 (10-K pages:83, 84); "approximately $730.0 million" at June 30, 2026 (Q3 10-Q page:32), letters of credit not stated. September 30, 2024 revolver size not stated |
| Total shareholders' equity (balance) | 1,842,815 | 1,674,035 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 1,740,551 | Reported; 10-K page:65, Q3 10-Q page:6 |
| Total debt / issuer-adjusted EBITDA (x) | 1.86 | 1.92 | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | 2.33 | Calculated, C5; principal over LTM adjusted EBITDA |
| Net debt / issuer-adjusted EBITDA (x) | 1.57 | 1.60 | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | 2.25 | Calculated, C5; net of all unrestricted cash |
| Issuer-adjusted EBITDA / cash interest paid (x) | 7.79 | 8.50 | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | 8.24 | Calculated, C6 |
| Issuer-adjusted EBITDA margin (%) | 11.6 | 12.9 | 14.7 | 15.0 | 13.2 | 14.0 | 13.5 | FY and quarter margins as printed by the issuer; LTM calculated, C7 |
| Operating cash flow / issuer-adjusted EBITDA (%) | 83.8 | 61.2 | n/a (seasonal flow) | n/a (seasonal flow) | n/a (seasonal flow) | n/a (seasonal flow) | 66.0 | Calculated, C8 |
| Covenant net total leverage ratio as reported (x), maximum 4.00 | 1.37 | 1.51 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 2.00 | Reported (10-K page:54; Q3 10-Q page:33); Credit Agreement definition, cash offset capped at 150,000 |
| Covenant net interest coverage ratio as reported (x), minimum 3.00 | 8.54 | 9.25 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 8.72 | Reported (same pages); Credit Agreement definition |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 (September 30, 2024) | 1.86 | 1.57 | x | Debt principal 1,145,819 and unrestricted cash 183,123 over issuer-adjusted EBITDA 615,044 (C5); the Credit Agreement ratio at this date is 1.37 on its own definition |
| FY2025 (September 30, 2025) | 1.92 | 1.60 | x | Principal 1,346,875, cash 222,351, adjusted EBITDA 701,554; Credit Agreement ratio 1.51 |
| LTM Q1 FY2026 (December 31, 2025) | 2.21 | 2.02 | x | Principal 1,579,375, cash 137,594, LTM adjusted EBITDA 715,350 (C2); Credit Agreement ratio 1.79 |
| LTM Q2 FY2026 (March 31, 2026) | 2.16 | 1.94 | x | Principal 1,546,875, cash 157,452, LTM adjusted EBITDA 716,971 (C2); Credit Agreement ratio 1.75, which caps the cash offset at 150,000 |
| LTM Q3 FY2026 (June 30, 2026) | 2.33 | 2.25 | x | Principal 1,653,548, cash 56,953, LTM adjusted EBITDA 711,009 (C1); Credit Agreement ratio 2.00. Issuer-adjusted EBITDA, not the covenant measure; the seasonal fourth-quarter collections (fiscal Q4 2025 free cash flow was 641,845, C13) have not yet occurred |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 (September 30, 2024) | 7.79 | x | Issuer-adjusted EBITDA 615,044 over interest payments 78,955 (10-K page:93) |
| FY2025 (September 30, 2025) | 8.50 | x | Adjusted EBITDA 701,554 over interest payments 82,562 |
| LTM Q1 FY2026 (December 31, 2025) | 8.37 | x | LTM adjusted EBITDA 715,350 over LTM interest payments 85,448 (C2); Credit Agreement coverage 9.01 |
| LTM Q2 FY2026 (March 31, 2026) | 8.42 | x | LTM adjusted EBITDA 716,971 over LTM interest payments 85,190 (C2); Credit Agreement coverage 8.84 |
| LTM Q3 FY2026 (June 30, 2026) | 8.24 | x | LTM adjusted EBITDA 711,009 over LTM interest payments 86,279 (C1); Credit Agreement coverage 8.72. The 325 million added to Term Loan B on May 27, 2026 bore interest for only part of the quarter, so LTM cash interest understates the run-rate |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| September 30, 2024 | 183.1 | Not supplied: the revolver size and balance at this date are not stated in the supplied sources | US$m | Unrestricted cash 183,123 thousand (10-K page:64); the debt table shows no revolver balance (10-K page:83) |
| September 30, 2025 | 222.4 | 747.0 | US$m | Unrestricted cash 222,351 thousand (10-K page:64); revolver 750.0 undrawn per "access to an additional $750.0 million" (page:52) less letters of credit of 3.0 (page:84). The filing does not say letters of credit reduce availability; they are netted here as the conservative reading |
| December 31, 2025 | 137.6 | 505.0 | US$m | Cash 137,594 thousand (Q1 10-Q page:5); "approximately $505.0 million" (Q1 10-Q page:27); letters of credit not stated, so capacity may be overstated |
| March 31, 2026 | 157.5 | 525.0 | US$m | Cash 157,452 thousand (Q2 10-Q page:5); "approximately $525.0 million" (Q2 10-Q page:29); letters of credit not stated |
| June 30, 2026 | 57.0 | 730.0 | US$m | Cash 56,953 thousand (Q3 10-Q page:5); "approximately $730.0 million" (Q3 10-Q page:32), equal to 750.0 less the 20.0 drawn; letters of credit not stated. Excludes 96.3 of restricted cash and the receivable-sale facility |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| July 1 to September 30, 2026 (as of June 30, 2026) | 19.0 | US$m | Future minimum principal payments, 18,952 thousand (Q3 10-Q page:15) |
| Year ending September 30, 2027 | 75.8 | US$m | 75,809 thousand; scheduled term loan amortization |
| Year ending September 30, 2028 | 81.4 | US$m | 81,434 thousand |
| Year ending September 30, 2029 | 690.2 | US$m | 690,184 thousand; the Term Loan A matures May 30, 2029 (10-K page:83); the table does not itemize the bucket |
| Year ending September 30, 2030 | 8.3 | US$m | 8,309 thousand |
| Years ending September 30, 2031 and thereafter | 778.9 | US$m | 778,860 thousand; the Term Loan B was due May 30, 2031 before the May 27, 2026 amendment (10-K page:83) and the amendment's maturity is not stated. Total 1,653.5 equals principal |

### Reported balance sheet and debt

| Item (USD thousands) | September 30, 2024 | September 30, 2025 | December 31, 2025 | March 31, 2026 | June 30, 2026 |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 183,123 | 222,351 | 137,594 | 157,452 | 56,953 |
| Accounts receivable, net | 879,514 | 898,095 | 1,147,740 | 1,114,960 | 1,382,014 |
| Goodwill | 1,782,871 | 1,782,095 | 1,781,156 | 1,780,507 | 1,780,543 |
| Intangible assets, net | 630,569 | 538,266 | 517,916 | 497,342 | 477,031 |
| Total assets | 4,131,508 | 4,069,639 | 4,208,300 | 4,239,174 | 4,366,779 |
| Total liabilities | 2,288,693 | 2,395,604 | 2,488,488 | 2,542,213 | 2,626,228 |
| Total shareholders' equity | 1,842,815 | 1,674,035 | 1,719,812 | 1,696,961 | 1,740,551 |
| Long-term debt, current portion | 40,139 | 52,680 | 58,305 | 63,930 | 71,599 |
| Long-term debt, non-current portion | 1,091,954 | 1,281,593 | 1,509,205 | 1,471,816 | 1,565,336 |
| Operating lease liabilities, current plus non-current | 144,877 | 109,894 | 102,752 | 92,040 | 94,883 |

Locators: 10-K pages:64 to 65; Q1 10-Q page:5; Q2 10-Q page:5; Q3 10-Q pages:5 to 6. Operating lease liabilities are the sum of the two printed lines (C14); at March 31, 2026 they are 35,400 + 56,640 (Q2 10-Q page:5).

### Debt register

| Instrument (as printed, USD thousands) | September 30, 2024 | September 30, 2025 | December 31, 2025 | March 31, 2026 | June 30, 2026 | Rate and terms |
| --- | --- | --- | --- | --- | --- | --- |
| Term Loan A (TLA) | 641,875 | 853,125 | 841,875 | 830,625 | 819,375 | Floating: SOFR plus a margin of 1.0% to 2.0% by leverage, 1.375% at June 30, 2026; matures May 30, 2029 (10-K page:83; Q3 10-Q page:30) |
| Term Loan B (TLB) | 498,750 | 493,750 | 492,500 | 491,250 | 814,173 | Floating: SOFR with a 0.5% floor plus a fixed 2.0% margin; was due May 30, 2031 before the May 27, 2026 amendment that "increased our TLB by $325 million" (10-K page:83; Q3 10-Q page:15) |
| Revolver | Not listed | None printed ("—" in the Q3 10-Q comparative) | 245,000 | 225,000 | 20,000 | Up to 750,000; SOFR-based, commitment fee 0.125% to 0.30% on unused funds (10-K page:83); Credit Agreement ends May 2031 (Q3 10-Q page:32) |
| Subsidiary loan agreements | 5,194 | None printed ("—") | Not listed | Not listed | Not listed | Extinguished with the Australia divestiture (10-K page:84) |
| Total debt principal | 1,145,819 | 1,346,875 | 1,579,375 | 1,546,875 | 1,653,548 | Sum of the lines above (C15) |
| Unamortized debt-issuance costs and discounts | (13,726) | (12,602) | (11,865) | (11,129) | (16,613) | Deducted in the printed total |
| Total debt, carrying value | 1,132,093 | 1,334,273 | 1,567,510 | 1,535,746 | 1,636,935 | Printed |
| Effective interest rate, including issuance costs | 5.52% | 5.37% | 5.1% | 5.0% | 5.6% | 10-K pages:35, 53; Q1 10-Q page:25; Q2 10-Q page:27; Q3 10-Q page:17 |

Locators: 10-K pages:83 to 84; Q1 10-Q page:13; Q2 10-Q page:14; Q3 10-Q page:15. The Credit Agreement is "secured by substantially all of our assets and all of the assets of our wholly owned material domestic subsidiaries, and guaranteed by each of our wholly owned material domestic subsidiaries" (10-K page:84); the guarantor entities are not named. There are no senior notes, bonds or indentures in any supplied source; the whole debt stack is one bank facility with JPMorgan Chase Bank, N.A. as the named counterparty (10-K page:52). The 10-K also notes revolving credit facilities in Canada and the United Kingdom without size or balance (page:83).

Interest rate swaps at June 30, 2026 (Q3 10-Q page:16): Term Loan B 75,000 at 3.72% to September 2026, 75,000 at 3.62% to September 2027, 75,000 at 4.04% to September 2028 and 50,000 at 4.06% to September 2029; Term Loan A 150,000 at 3.14% to September 2027, 200,000 at 3.47% to September 2028 and 50,000 at 4.05% to May 2029. Notional 675,000 of 1,653,548 principal, 40.8% (C12). The remaining 978,548 pays SOFR plus margin. The swap on 75,000 of Term Loan B expires in September 2026, after the balance sheet date. Fair value at June 30, 2026: asset 3.9 million, liability 0.8 million (Q3 10-Q page:17).

Maturity profile as of June 30, 2026 (Q3 10-Q page:15), USD thousands: July 1 to September 30, 2026: 18,952; year ending September 30, 2027: 75,809; 2028: 81,434; 2029: 690,184; 2030: 8,309; thereafter: 778,860; total 1,653,548. The comparable table at September 30, 2025 shows 55,625, 72,500, 78,125, 666,875, 5,000 and 468,750 (10-K page:84). The table at December 31, 2025 shows 911,875 for the year ending September 30, 2029 (Q1 10-Q page:13), when the revolver stood at 245,000. The revolver's own maturity is not itemized.

### Liquidity and covenant

| Item | September 30, 2025 | December 31, 2025 | March 31, 2026 | June 30, 2026 |
| --- | --- | --- | --- | --- |
| Unrestricted cash (USD thousands) | 222,351 | 137,594 | 157,452 | 56,953 |
| Revolver commitment (USD millions) | 750.0 | 750 ("our $750 million revolving credit facility") | 750 (same wording) | 750 (same wording) |
| Revolver drawn (USD thousands) | None printed | 245,000 | 225,000 | 20,000 |
| Letters of credit under the Credit Agreement (USD millions) | 3.0 | Not stated | Not stated | Not stated |
| Revolver access as printed (USD millions) | 750.0 | 505.0 | 525.0 | 730.0 |
| Covenant: net total leverage ratio, reported | 1.51 | 1.79 | 1.75 | 2.00 |
| Covenant: maximum | 4.00, step-up to 4.50 under certain circumstances | Same | Same | Same |
| Covenant: net interest coverage ratio, reported | 9.25 | 9.01 | 8.84 | 8.72 |
| Covenant: minimum | 3.00 | 3.00 | 3.00 | 3.00 |

Locators: 10-K pages:52 to 54, 84; Q1 10-Q pages:25, 27 to 29; Q2 10-Q pages:27, 29 to 31; Q3 10-Q pages:29, 32 to 33. The leverage test is on "any twelve-month period" at the end of each quarter, with cash offset capped at 150 million US dollars; the same ratio sets the TLA margin and the unused-line fee (Q3 10-Q page:32). The release states a target net leverage ratio of 2x to 3x (Q3 release page:4). No facility is stated to expire within twelve months of June 30, 2026: the Credit Agreement runs to May 2031, and the Canada and United Kingdom facilities are not sized, so their expiry is Not supplied. After the balance sheet date "we have received $245 million of cash due from this customer" (Q3 10-Q page:31). The receivable-sale agreement with Wells Fargo Bank N.A. allows sales of up to 350.0 million US dollars at any time (Q3 10-Q page:20); it is a liquidity source recorded as sales, not as debt, and its drawn balance is not printed.

### Segment and operating drivers

| Item (USD thousands) | Q3 FY2026 | Q3 FY2025 | 9M FY2026 | 9M FY2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- |
| U.S. Federal Services revenue | 720,991 | 761,174 | 2,260,735 | 2,319,756 | 3,067,691 | 2,737,244 |
| U.S. Federal Services segment operating income | 134,040 | 137,862 | 396,477 | 355,944 | 469,155 | 333,622 |
| U.S. Services revenue | 418,227 | 439,818 | 1,249,229 | 1,334,418 | 1,763,691 | 1,911,813 |
| U.S. Services segment operating income | 45,189 | 44,957 | 113,065 | 139,610 | 171,264 | 246,982 |
| Outside the U.S. revenue | 139,753 | 147,408 | 420,020 | 458,687 | 599,894 | 657,140 |
| Outside the U.S. segment operating income/(loss) | 1,206 | 5,940 | (3,259) | 18,856 | 22,391 | 7,705 |
| Total segment operating income | 180,435 | 188,759 | 506,283 | 514,410 | 662,810 | 588,309 |

Locators: Q3 release pages:8 to 9 and Q3 10-Q pages:10 to 11 for quarter and nine months; 10-K pages:78 to 79 for the fiscal years. Segment operating income is before amortization of intangibles, divestiture-related items and unallocated "Other". Revenue from U.S. federal government agencies, across segments, was 55.2% of FY2025 revenue (10-K page:80, 2,995,821). Backlog was 15,327 million US dollars at September 30, 2025 against 16,167 million a year earlier (10-K page:49); no later backlog figure is supplied, so backlog at June 30, 2026 is Not supplied. The Q3 release prints segment operating margins of 18.6%, 10.8% and 0.9% for the quarter (page:3).

### Claims outside the debt figure

| Item | Amount | Date | Inside or outside the debt figure | Locator |
| --- | --- | --- | --- | --- |
| Operating lease liabilities (no finance leases are shown) | 94,883 thousand (38,280 current plus 56,603 non-current) | June 30, 2026 | Outside; the debt figure is term loans and revolver only | Q3 10-Q page:5; 10-K page:89 shows 109,894 at September 30, 2025 |
| Receivables sold under the Wells Fargo Receivables Purchase Agreement | Receivables transferred 1.28 billion, cash received 1.27 billion, in the nine months; capacity 350.0 million (250.0 million at September 30, 2025 and December 31, 2025) | Nine months ended June 30, 2026 | Outside; accounted for as sales with "no recourse", loss on sale in SG&A, cash in operating cash flow | Q3 10-Q page:20; 10-K page:94; Q1 10-Q page:17; Q2 10-Q page:18 |
| Performance bond commitments | 33.2 million | September 30, 2025 | Outside; liability only on default on performance, probability believed "remote" | 10-K page:98 |
| Indemnification liability to the buyer of the Australia and Korea businesses | 8,767 thousand, level 3 fair value | June 30, 2026 | Outside the debt figure; recorded in liabilities | Q3 10-Q page:17 |
| Contingent consideration receivable from that sale | Up to 5.0 million; none recorded | June 30, 2026 | An unrecorded asset, not a claim | Q3 10-Q page:15 |
| Deferred compensation plan liabilities, non-current | 66,468 thousand, with Rabbi Trust assets of 46,375 thousand at fair value | June 30, 2026 | Outside; the trust is available to general creditors in bankruptcy and "sufficient to meet 92% of the liabilities" at September 30, 2025 | Q3 10-Q pages:5, 17; 10-K page:99 |
| Restricted cash held for customers | 96,296 thousand, offset by a current liability | June 30, 2026 | Outside; not available liquidity | Q3 10-Q pages:19, 32 |
| MOVEit cybersecurity incident litigation | Accrual "within a range of possible outcomes"; amount not printed | June 30, 2026 | Outside; unquantified | Q3 10-Q pages:21 to 22; 10-K pages:96 to 97 |
| Pensions and retiree medical | None described: the sources describe 401(k) and non-US defined contribution plans only; a search of the 10-K for "defined benefit" and "pension plan" found nothing | September 30, 2025 | Not applicable | 10-K page:99 |
| Purchase and capacity commitments, consent decrees | Not found in the sources; a search of the 10-K for "purchase obligation", "purchase commitment", "unconditional", "consent decree" and "consent order" found nothing | September 30, 2025 | Not supplied | 10-K searched |

### Latest quarter and after

- Fiscal Q3 2026 (three months ended June 30, 2026): revenue 1,278,971 thousand against 1,348,400 thousand, a decline of 5.1% (C7); adjusted EBITDA 192,327 against 198,289 (margin 15.0% against 14.7% as printed); operating income 161,428 against 165,672; net income 103,593 against 105,981 (Q3 10-Q page:4; Q3 release pages:2, 6, 9). All three segments reported lower revenue; the release attributes the prior-year quarter to "elevated natural disaster support activity as well as temporary clinical volume surges" (Q3 release page:3).
- Financing event: on May 27, 2026 the Credit Agreement was amended and Term Loan B increased by 325 million US dollars (Q3 10-Q page:15). Term Loan B principal rose from 491,250 at March 31, 2026 to 814,173 at June 30, 2026 and the revolver fell from 225,000 to 20,000, so the quarter's borrowings of 703,675 and repayments of 600,935 are consistent with refinancing revolver borrowings (Q3 release page:7; C16). The amendment's pricing, maturity and other terms are Not supplied. Debt financing costs paid in the quarter were 2,393 thousand. New interest rate swaps took effect on June 1, 2026 (Q3 10-Q page:16).
- Capital returns: the board increased the repurchase authorization in May 2026 to up to 400 million US dollars, with about 400.0 million still available at June 30, 2026 (Q3 10-Q page:19). In the nine months the company purchased about 2.6 million shares at a cost of 192.4 million including excise tax, against 204,919 thousand of cash purchases in the cash flow statement; the sources do not reconcile the two. Quarterly dividend 0.33 per share (Q3 10-Q page:5).
- Operations and cash: days sales outstanding were 98 days at June 30, 2026 against 62 days at September 30, 2025, or 123 days against 73 days excluding the receivable-sale effect, because of "administrative delays on payments from one of our large contracts with the U.S. federal government" (Q3 10-Q page:31). Accounts receivable, net rose from 898,095 to 1,382,014 thousand (C14). Restricted cash rose from 38,108 to 96,296 thousand on one customer's contract (Q3 10-Q page:32).
- Subsequent events (after June 30, 2026, before the August 6, 2026 filing date): 245 million US dollars collected from the delayed federal customer, with more expected "through the fourth quarter of fiscal year 2026" (Q3 10-Q page:31); a dividend of 0.33 per share declared July 6, 2026, payable August 31, 2026, about 17.3 million US dollars (page:22). The release says collections "accelerated during July" and expects days sales outstanding to finish fiscal 2026 "below 70 days" (Q3 release page:4).
- Customer-directed modification: a major customer's temporary contractual modification is effective July 1, 2026 through December 31, 2026 and is expected to reduce diluted EPS by about 0.35 per quarter through the remainder of fiscal 2026 and the first quarter of fiscal 2027 (Q3 10-Q page:27). The Federal Services operating margin guidance for fiscal 2026 is 16.5% to 17.0% and the Outside the U.S. segment is expected to break even (Q3 release page:3).
- Guidance changes (attributed management claims): adjusted diluted EPS 7.90 to 8.20 in August 2026 against 8.25 to 8.55 in May 2026; adjusted EBITDA margin about 13.7% against about 14.2%; free cash flow 425 million to 475 million against 450 million to 500 million; revenue unchanged at 5.2 billion to 5.35 billion; adjusted EBITDA 712 million to 734 million (Q3 release pages:2, 5 to 6; Q2 release pages:2, 4). Implied fourth-quarter figures are in C13.
- Nothing dated after August 6, 2026 is supplied. The fiscal 2025 10-K reports its own subsequent events: a dividend of 0.30 per share declared October 6, 2025 and 0.4 million shares bought for 30.7 million US dollars after year end (10-K pages:93, 99).

### Reconciliation to the readiness handoff

- CP-0 found no trailing twelve month adjusted EBITDA and listed it as a gap. This answer derives it (C1, C2) from printed quarterly and annual adjusted EBITDA, and labels it as calculated.
- CP-0 said the 10-Qs do not mention letters of credit and that availability net of letters of credit is not determinable. That holds: the capacity figures here are as printed, with 3.0 million netted only at September 30, 2025, where the 10-K prints it.
- CP-0 recorded the receivable-sale limit change from 250.0 million to 350.0 million between December 31, 2025 and March 31, 2026. It is carried forward unchanged; the date and terms remain Not supplied.
- CP-0 listed Term Loan A, Term Loan B, the Revolver and the receivable-sale agreement as the instruments. This answer confirms there are no notes or other instruments in the debt tables and adds the Canada and United Kingdom revolving facilities that the 10-K mentions. Nothing in CP-0 is corrected.

## Calculations

All amounts are in thousands of USD unless stated. Inputs are the printed figures at the cited locators.

- C1. LTM to June 30, 2026 = FY2025 + 9M FY2026 − 9M FY2025. Revenue: 5,431,276 + 3,929,984 − 4,112,861 = 5,248,399. Gross profit: 1,333,443 + 1,009,737 − 999,891 = 1,343,289. Operating income: 528,289 + 456,125 − 405,427 = 578,987. Interest expense: 84,080 + 66,805 − 61,648 = 89,237. Net income: 319,034 + 295,599 − 243,746 = 370,887. Depreciation and amortization: 41,669 + 37,091 − 27,502 = 51,258. Amortization of intangibles: 92,047 + 60,785 − 69,041 = 83,791. Adjusted EBITDA: 701,554 + 550,768 − 541,313 = 711,009. Operating cash flow: 429,372 + (−179,863) − (−220,000) = 469,509. Purchases of property, equipment and software: 63,213 + 28,752 − 55,686 = 36,279. Dividends: 68,710 + 51,437 − 51,865 = 68,282. Share purchases: 447,482 + 204,919 − 306,443 = 345,958. Cash interest: 82,562 + 64,526 − 60,809 = 86,279. The interest expense, net income, depreciation and amortization and intangibles LTM figures equal the trailing twelve month figures printed in the Credit Agreement reconciliation (Q3 10-Q page:33).
- C2. Earlier LTM series. Adjusted EBITDA to December 31, 2025: 701,554 + 170,414 − 156,618 = 715,350 (Q1 10-Q page:31). To March 31, 2026: 701,554 + 358,441 − 343,024 = 716,971 (Q2 10-Q page:33). Cash interest to December 31, 2025: 82,562 + 20,445 − 17,559 = 85,448 (Q1 10-Q page:16); to March 31, 2026: 82,562 + 41,395 − 38,767 = 85,190 (Q2 10-Q page:17). Interest expense to December 31, 2025: 84,080 + 20,816 − 17,522 = 87,374, equal to the printed 87,374 (Q1 10-Q page:28); to March 31, 2026: 84,080 + 42,927 − 38,991 = 88,016, equal to the printed figure (Q2 10-Q page:30). Discrete Q3 cash interest: 64,526 − 41,395 = 23,131 for FY2026 and 60,809 − 38,767 = 22,042 for FY2025.
- C3. Free cash flow = operating cash flow − purchases of property, equipment and software. LTM: 469,509 − 36,279 = 433,230. FY2025: 429,372 − 63,213 = 366,159 and FY2024: 515,258 − 114,190 = 401,068, both equal to the printed figures. Nine months FY2026: −179,863 − 28,752 = −208,615, equal to the printed figure.
- C4. Net debt = debt principal − unrestricted cash, with restricted cash excluded and no cap on the cash offset. June 30, 2026: 1,653,548 − 56,953 = 1,596,595. September 30, 2025: 1,346,875 − 222,351 = 1,124,524. September 30, 2024: 1,145,819 − 183,123 = 962,696. December 31, 2025: 1,579,375 − 137,594 = 1,441,781. March 31, 2026: 1,546,875 − 157,452 = 1,389,423.
- C5. Leverage = debt principal (or net debt) / LTM issuer-adjusted EBITDA. June 30, 2026: 1,653,548 / 711,009 = 2.33; 1,596,595 / 711,009 = 2.25. September 30, 2025: 1,346,875 / 701,554 = 1.92; 1,124,524 / 701,554 = 1.60. September 30, 2024: 1,145,819 / 615,044 = 1.86; 962,696 / 615,044 = 1.57. December 31, 2025: 1,579,375 / 715,350 = 2.21; 1,441,781 / 715,350 = 2.02. March 31, 2026: 1,546,875 / 716,971 = 2.16; 1,389,423 / 716,971 = 1.94.
- C6. Cover = LTM issuer-adjusted EBITDA / LTM cash interest paid. June 30, 2026: 711,009 / 86,279 = 8.24. September 30, 2025: 701,554 / 82,562 = 8.50. September 30, 2024: 615,044 / 78,955 = 7.79. December 31, 2025: 715,350 / 85,448 = 8.37. March 31, 2026: 716,971 / 85,190 = 8.42.
- C7. Margins and growth. LTM adjusted EBITDA margin: 711,009 / 5,248,399 = 13.5%. FY2025 revenue growth: 5,431,276 / 5,306,197 − 1 = 2.4%. Q3 revenue change: 1,278,971 / 1,348,400 − 1 = −5.1%. Nine-month revenue change: 3,929,984 / 4,112,861 − 1 = −4.4%. Q3 adjusted EBITDA change: 192,327 / 198,289 − 1 = −3.0%.
- C8. Operating cash flow / adjusted EBITDA: LTM 469,509 / 711,009 = 66.0%; FY2025 429,372 / 701,554 = 61.2%; FY2024 515,258 / 615,044 = 83.8%.
- C9. Covenant arithmetic on the Credit Agreement basis (Q3 10-Q page:33). Net total leverage: (1,653,548 − 56,953) = 1,596,595; 1,596,595 / 798,419 = 2.00. EBITDA at which the 4.00 maximum binds: 1,596,595 / 4.00 = 399,149; cushion 798,419 − 399,149 = 399,270, which is 50.0% of 798,419. Additional net debt capacity at 4.00 with EBITDA unchanged: 4.00 × 798,419 − 1,596,595 = 1,597,081. Interest coverage: 798,419 / 91,588 = 8.72; EBITDA at which the 3.00 minimum binds: 3.00 × 91,588 = 274,764; cushion 798,419 − 274,764 = 523,655, which is 65.6%. The 4.50 step-up applies "under certain circumstances" that are not defined in the sources and is not used. The Credit Agreement EBITDA exceeds LTM issuer-adjusted EBITDA by 798,419 − 711,009 = 87,410; the reconciliation shows stock compensation 35,132 and pro forma and other adjustments 52,278, and 35,132 + 52,278 = 87,410.
- C10. Liquidity at June 30, 2026 = unrestricted cash + printed revolver access: 56,953 + 730,000 = 786,953. Other dates: September 30, 2025: 222,351 + 747,000 = 969,351; December 31, 2025: 137,594 + 505,000 = 642,594; March 31, 2026: 157,452 + 525,000 = 682,452. Revolver access at June 30, 2026 = 750,000 − 20,000 = 730,000, with letters of credit not stated and the receivable-sale facility excluded.
- C11. Movement in debt and net debt from September 30, 2025 to June 30, 2026: principal 1,653,548 − 1,346,875 = 306,673; net debt 1,596,595 − 1,124,524 = 472,071. Nine-month capital returns: share purchases 204,919 + dividends 51,437 = 256,356; net borrowing in the nine months: proceeds 1,368,675 − repayments 1,065,935 = 302,740. Term Loan B principal rose 814,173 − 491,250 = 322,923 in the quarter from March 31, 2026.
- C12. Hedge coverage: notional 75,000 + 75,000 + 150,000 + 200,000 + 75,000 + 50,000 + 50,000 = 675,000; 675,000 / 1,653,548 = 40.8%. Unhedged: 419,375 + 539,173 + 20,000 = 978,548 = 1,653,548 − 675,000.
- C13. Guidance-implied fourth quarter (attributed guidance less nine-month actuals, USD thousands). Revenue 5,200,000 to 5,350,000 less 3,929,984 = 1,270,016 to 1,420,016. Adjusted EBITDA 712,000 to 734,000 less 550,768 = 161,232 to 183,232. Operating cash flow 465,000 to 515,000 less (−179,863) = 644,863 to 694,863. Free cash flow 425,000 to 475,000 less (−208,615) = 633,615 to 683,615. Comparator: fiscal Q4 2025 free cash flow was 366,159 − (−275,686) = 641,845, and operating cash flow 429,372 − (−220,000) = 649,372. Interest and other expense guidance of 88,000 less the nine-month 66,805 − 1,639 = 65,166 implies 22,834 for the fourth quarter.
- C14. Balance sheet items. Operating lease liabilities: 38,280 + 56,603 = 94,883 at June 30, 2026; 38,605 + 71,289 = 109,894 at September 30, 2025; 47,656 + 97,221 = 144,877 at September 30, 2024; 37,484 + 65,268 = 102,752 at December 31, 2025. Accounts receivable, net: 1,382,014 − 898,095 = 483,919. Goodwill plus intangibles at June 30, 2026: 1,780,543 + 477,031 = 2,257,574, which exceeds equity of 1,740,551 by 517,023; at September 30, 2025 the excess is 1,782,095 + 538,266 − 1,674,035 = 646,326.
- C15. Debt tie-outs. June 30, 2026: 819,375 + 814,173 + 20,000 = 1,653,548; less 16,613 = 1,636,935; current 71,599 + non-current 1,565,336 = 1,636,935. December 31, 2025: 841,875 + 492,500 + 245,000 = 1,579,375. March 31, 2026: 830,625 + 491,250 + 225,000 = 1,546,875. September 30, 2025: 853,125 + 493,750 = 1,346,875. September 30, 2024: 641,875 + 498,750 + 5,194 = 1,145,819. Maturity tables foot to the principal totals at each date (see CP-0 for June 30, 2026 and September 30, 2025; December 31, 2025: 43,125 + 72,500 + 78,125 + 911,875 + 5,000 + 468,750 = 1,579,375).
- C16. Quarter financing flows (Q3 release page:7): proceeds from borrowings 703,675 − principal payments 600,935 = net borrowing 102,740. Debt principal rose 1,653,548 − 1,546,875 = 106,673 over the quarter, which exceeds net borrowing by 3,933; the nine-month figures in C11 differ by the same 3,933 (306,673 against 302,740), and the first two quarters tie exactly (232,500 and 200,000 in Q1 and the first half). The unamortized issuance costs and discounts rose from 11,129 to 16,613, and 11,129 + 2,393 (debt financing costs paid) + 3,933 − 842 (amortization of debt issuance costs and discount in the quarter) = 16,613. That roll-forward is consistent with a 3,933 discount netted from the quarter's proceeds, but the sources do not say so, so it is an inference and not a reported fact.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit Agreement text, the May 27, 2026 amendment terms (pricing, maturity, baskets, step-up conditions) and the Consolidated EBITDA definition are not supplied | High | CP-2, CP-5 | Supply the executed agreement and amendment; keep the reported 2.00 and 8.72 as attributed figures |
| Fiscal Q4 and full-year fiscal 2026 results and all events from August 7, 2026 to the cutoff are not supplied; full-year guidance depends on fourth-quarter collections of 633,615 to 683,615 thousand free cash flow (C13) | High | CP-1A, CP-2 | Supply the fiscal 2026 10-K, any release and any 8-K |
| Letters of credit under the revolver are quantified only at September 30, 2025 (3.0 million); revolver access at later dates is as printed and may be overstated | Medium | CP-2 | Request later disclosure; do not net unsupported amounts |
| Outstanding balance of receivables sold to Wells Fargo at each balance sheet date is not printed; the loss on sale for the nine months is not separable (transfers 1.28 billion and cash 1.27 billion are rounded) | Medium | CP-2 | Supply the agreement and period-end balances |
| Revolver size at September 30, 2024, and the size, balance and expiry of the Canada and United Kingdom revolving facilities, are not supplied | Low | CP-2 | Supply the facility terms |
| Guarantor entities and the restricted or unrestricted split are not stated, and cash held in foreign locations is not quantified | High | CP-2 | Supply the guarantor schedule; "no requirement to remit funds from our foreign locations" is stated (Q3 10-Q page:33) |
| Backlog at June 30, 2026 and book-to-bill are not supplied (10-K gives 15,327 million at September 30, 2025 only) | Medium | CP-1A | Supply later backlog disclosure |
| MOVEit litigation accrual amount and insurance recovery are not printed | Medium | CP-2 | Carry as an unquantified contingency |
| Issuer-adjusted and Credit Agreement EBITDA differ by stock compensation and pro forma adjustments (C9); no single normalized EBITDA is established here | Medium | CP-2, CP-5 | Label the measure used in every ratio |
| Releases are attributed management claims; earnings presentations and the non-GAAP calculation details are not supplied | Low | CP-1A | Supply the decks if needed |
| Text extraction only: original HTML, XBRL and images are not supplied; page chunks are not printed page numbers | Low | CP-5 | Check flagged tables against the filed HTML when available |
| Debt principal moved 3,933 thousand more than net borrowing in the quarter and nine months (C16); the sources do not state why, and a discount netted from proceeds is only an inference | Low | CP-5 | Confirm against the Credit Agreement amendment or the filed tables |

## Next module

- CP-1A: describe the business from the 10-K and the Q3 10-Q using the segment and customer tables here. Carry the customer-directed modification effective July 1, 2026 through December 31, 2026, the child support divestiture of December 2025 and the Australia and Korea divestiture of December 2024. Attribute the releases. Label anything after August 6, 2026 as Not supplied.
- CP-2: use the debt register, liquidity, covenant and claims-outside-debt tables. Quote covenant levels and reported ratios as attributed, keep issuer-adjusted and Credit Agreement EBITDA apart, and carry the missing Credit Agreement, amendment terms, guarantors, letters of credit and receivable-sale balances as restrictions. Treat the fourth-quarter collections required by guidance (C13) as the central liquidity and leverage sensitivity.
- CP-5: every figure here is traceable to a located page; the calculations C1 to C16 show their inputs. Keep the extraction-only limit, the release-versus-filing distinction and the 3,933 difference between debt movement and net borrowing (C16) visible.
