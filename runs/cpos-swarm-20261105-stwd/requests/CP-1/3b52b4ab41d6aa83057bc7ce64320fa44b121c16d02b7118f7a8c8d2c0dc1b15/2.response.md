## Request

Issuer: STARWOOD PROPERTY TRUST, INC. (issuer id stwd, NYSE: STWD). As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway credit_snapshot. Reporting currency USD; every statement amount below is in USD thousands unless a line says millions, billions or per share. Current period q2-2026 (quarter and six months ended June 30, 2026); prior period fy-2025 (year ended December 31, 2025).

Task: build the financial base for the issuer from the supplied filings and releases, as the first financial module after source readiness. It reports the statements as printed, builds labelled calculation bridges, interprets them from the evidence and lists gaps. It is an intermediate handoff for CP-OS, not the final report. The perimeter is the registrant, Starwood Property Trust, Inc., on its consolidated basis, which includes consolidated securitization variable interest entities (VIEs); where the management presentation excludes them, the text says so.

## Sources

Issuer sources relied on (file name and sha256 of the pinned file; page:N is the extraction chunk, not the printed page):

| Short name | Exact source name | sha256 | Used for |
| --- | --- | --- | --- |
| 10-K FY2025 | 10-K_2025-12-31_stwd-20251231.htm.jsonl | 5d034c0380b12617b5276d804970154e60e42e6a23c5bcee4ef0d6e26b8a55fd | audited FY2025, FY2024, FY2023 statements; Dec 31, 2025 and 2024 balance sheets |
| 10-Q Q3 2025 | 10-Q_2025-09-30_stwd-20250930.htm.jsonl | d42c4a9a27c9d73fda589e7dc56562d17c85018a2ea82a77ac4a395ea6aee3bc | Q3 2025 and nine months 2025; Sep 30, 2025 balance sheet |
| 10-Q Q1 2026 | 10-Q_2026-03-31_stwd-20260331.htm.jsonl | a981c1ff096bebb78573fc217060d2be7d932d6a1d88404218dd31da70ce8980 | Q1 2026; Mar 31, 2026 balance sheet |
| 10-Q Q2 2026 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | e8c4bcc3fcec859b834e7d77d0075c7162cba6647a0dd89e45052bfa9c8b4b3a | Q2 2026 and 6M 2026; Jun 30, 2026 balance sheet; debt notes; subsequent events |
| Release YE2025 | EX-99.1_2026-02-25_stwd_pressrelease-ye2025.htm.jsonl | 1f1cf65fe88590eb05e524e31bd92875cef8da770ee1cfa5cacc2e06538ebd9a | Q4 2025 statement and distributable earnings |
| Release Q1 2026 | EX-99.1_2026-05-08_stwd_pressrelease-q12026.htm.jsonl | 316bfad5efe7ce527d0308c8cc555686397e0897e2159e9321c558a9bbed50a7 | Q1 2026 distributable earnings |
| Release Q2 2026 | EX-99.1_2026-08-06_stwd_pressrelease-q22026.htm.jsonl | b1942a46f485117f96015975cca8555da21dd98692e7e25a0fc84b19a0efbf22 | Q2 2026 segment statements, ex-VIE balance sheet, distributable earnings |

Run-settings source `context` (bb1537683323815090e6da83a4ec1d608fc4d7c145051f90360ef72eab181e62) names the issuer, periods and currency only; it holds no financial data.

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 2dd5f2d188dcfd523c32c5571bb13634e5383866cc3b07a5a7ff8344297fbd4e | opened and used: source identities, the ex-VIE versus consolidated perimeter conflict, the missing covenant, guarantor and rating inputs, and the period-labelling cautions |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported earnings are thin against the distributable earnings measure and against the dividend, while debt has risen and equity has fallen. The financial base is usable for the credit view, with the perimeter stated on every figure. | Medium | Distributable earnings is a company measure and the consolidated balance sheet includes large securitization VIE balances. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Second quarter 2026 net income attributable to the registrant was 6,557 thousand against distributable earnings of 151,503 thousand. | GAAP earnings give little cushion in the quarter; the company measure is far higher and is not a filed GAAP figure. | High |
| Total debt on the balance sheet rose to 23,694,124 thousand at June 30, 2026 from 22,094,237 thousand at December 31, 2025, while stockholders’ equity fell. | Debt to stockholders’ equity moved to 3.65x from 3.25x, so leverage is higher and equity cushion thinner. | High |
| Dividends declared exceeded distributable earnings per share in the first half of 2026 and exceeded operating cash flow. | The payout draws on balance sheet capacity or asset sales rather than on retained cash earnings. | Medium |
| The consolidated balance sheet and the management ex-VIE presentation differ greatly in size. | Any asset, liability or leverage figure must say which perimeter it uses. | High |
| Unsecured note maturities changed after the quarter end through a repayment and a redemption funded by new notes. | The nearest unsecured maturity after July 2026 is the 2027 convertible notes. | Medium |

### Financial base view

The registrant’s financial base for the twelve months to June 30, 2026 shows a lender with higher revenue than a year earlier, rising funding cost and low GAAP earnings in the latest quarter. Revenue for the quarter was higher than a year earlier, interest expense was higher, and the credit loss line moved from a small reversal in the first quarter of 2026 to a provision in the second. Distributable earnings stayed between about 147 and 160 million dollars a quarter over the last four quarters on the company’s own definition, so the gap between GAAP and distributable earnings is the central reading issue. Debt grew over the six months while stockholders’ equity fell; the equity fall reflects dividends declared above net income. The evidence is sufficient to carry a financial base into the business, credit and evidence-trace work, with the limitations in the Gaps section: no filing after June 30, 2026, no covenant levels, an unaudited interim base, and two balance-sheet perimeters.

### Source and perimeter context

- Statements are the consolidated statements of Starwood Property Trust, Inc. and subsidiaries, in USD thousands (10-Q Q2 2026 page:3 "Condensed Consolidated Balance Sheets (Unaudited, amounts in thousands, except share data)"; 10-K FY2025 page:159 "Consolidated Balance Sheets (Amounts in thousands, except share data)"). The FY2025 statements carry an auditor’s report dated February 25, 2026 (10-K FY2025 pages 157 and 159); the 2026 and Q3 2025 reports are unaudited.
- The balance sheet consolidates securitization VIEs as separate lines: "Variable interest entity (“VIE”) assets, at fair value 30,868,147 34,493,164" and "VIE liabilities, at fair value 29,293,820 32,803,806" (10-Q Q2 2026 page:4). The balance-sheet note states that securitized financing issued by VIEs "do not have recourse to Starwood Property Trust, Inc." (10-Q Q2 2026 page:4).
- The release segment statements show a subtotal before a "Securitization VIEs" column; the Q2 2026 release headline total assets figure is that subtotal (Release Q2 2026 page:1 "Record Total Assets of $31.8 Billion"; page:7). The perimeter bridge in the Calculations section ties the two.
- Quarter, six-month, nine-month, full-year and LTM labels are kept distinct throughout. Q4 2025 comes from the year-end release (Release YE2025 pages 5 and 6) and ties to FY2025 less nine months 2025 (see Calculations).
- The registrant is externally managed (10-Q Q2 2026 page:11); management fees are a separate expense line and the company’s distributable earnings measure is used to compute the incentive fee (Release Q2 2026 page:4).

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Jun 30, 2026 | Not supplied: the issuer reports no EBITDA and the filings read here print none | Not supplied: the issuer reports no EBITDA and the filings read here print none | x | EBITDA is not a reported measure and is not meaningful for a lender whose interest expense is its main cost. The analyst ratio total debt to stockholders’ equity is 3.65x at this date, in the metrics table below. |
| Mar 31, 2026 | Not supplied: no reported EBITDA | Not supplied: no reported EBITDA | x | Same basis. Total debt to stockholders’ equity is 3.47x. |
| Dec 31, 2025 | Not supplied: no reported EBITDA | Not supplied: no reported EBITDA | x | Same basis. Total debt to stockholders’ equity is 3.25x. |
| Sep 30, 2025 | Not supplied: no reported EBITDA | Not supplied: no reported EBITDA | x | Same basis. Total debt to stockholders’ equity is 3.12x. |
| Dec 31, 2024 | Not supplied: no reported EBITDA | Not supplied: no reported EBITDA | x | Same basis. Total debt to stockholders’ equity is 2.69x. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| LTM Jun 2026 | Not supplied: no reported EBITDA | x | Cash paid for interest for the LTM is 1,236,745 USD thousands. The analyst GAAP interest cover (income before income taxes plus interest expense, over interest expense) is 1.22x; it is not EBITDA based and not a covenant ratio. |
| FY2025 | Not supplied: no reported EBITDA | x | Cash paid for interest is 1,188,901 USD thousands (10-K FY2025 page:164). No EBITDA is reported. |
| FY2024 | Not supplied: no reported EBITDA | x | Cash paid for interest is 1,294,131 USD thousands (10-K FY2025 page:164). No EBITDA is reported. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Jun 30, 2026 | 367.592 | Not supplied: the filings give lender-approved undrawn capacity, not committed facilities | US$m | Cash and cash equivalents, excluding restricted cash of 272.764 US$m (10-Q Q2 2026 page:3). Approved but undrawn capacity on secured borrowings is 1,399.046 US$m (10-Q Q2 2026 page:143); it depends on pledged collateral and is not stated to be committed, so it is not charted as committed. No company liquidity figure for this date was located. |
| Mar 31, 2026 | 290.285 | Not supplied: the filings give lender-approved undrawn capacity, not committed facilities | US$m | Cash and cash equivalents (10-Q Q1 2026 page:3); restricted cash of 375.777 US$m excluded. Approved but undrawn capacity was 1,028.798 US$m (10-Q Q1 2026 page:126). |
| Dec 31, 2025 | 499.480 | Not supplied: the filings give lender-approved undrawn capacity, not committed facilities | US$m | Cash and cash equivalents (10-K FY2025 page:159). Approved but undrawn capacity was 1,596.919 US$m (10-K FY2025 page:138). The year-end release headline states current liquidity of 1.4 billion dollars (Release YE2025 page:2) without a build, so it cannot be tied to these inputs. |
| Sep 30, 2025 | 301.135 | Not supplied: the filings give lender-approved undrawn capacity, not committed facilities | US$m | Cash and cash equivalents (10-Q Q3 2025 page:3). Approved but undrawn capacity was 1,511.811 US$m (10-Q Q3 2025 page:143). |
| Dec 31, 2024 | 377.831 | Not supplied: no undrawn capacity figure for this date is in the supplied sources | US$m | Cash and cash equivalents (10-K FY2025 page:159). The December 31, 2024 secured borrowings summary would be in the FY2024 annual report, which is not supplied. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 (remainder) | 1369.797 | US$m | Principal at Jun 30, 2026: secured and securitized financing 969.797 on the company’s fully extended or collateral-driven schedule (10-Q Q2 2026 page:55) plus 2026 Senior Notes 400.000 (page:56). Before the July 2026 repayment of those notes. |
| 2027 | 3619.529 | US$m | Secured and securitized 2738.779 plus 2027 Convertible Notes 380.750 and 2027 Senior Notes 500.000. The 500.000 notes were redeemed in July 2026 and replaced by notes due August 15, 2029 (10-Q Q2 2026 page:101), which this row does not reflect. |
| 2028 | 3827.998 | US$m | Secured and securitized 3327.998 plus 2028 Senior Notes 500.000. |
| 2029 | 2915.616 | US$m | Secured and securitized 2315.616 plus 2029 Senior Notes 600.000, before the new notes due August 15, 2029 of 500.000. |
| 2030 | 6704.331 | US$m | Secured and securitized 5304.331 plus April, July and October 2030 Senior Notes 1400.000. |
| Thereafter | 5425.840 | US$m | Secured and securitized 4275.840 plus January 2031 and June 2031 Senior Notes 1150.000. Total across all rows 23863.111 US$m. The secured schedule uses the earlier of facility or collateral maturity, so it is not a contractual facility maturity table. |

### Financials and credit metrics

| Metric | LTM Jun 2026 or Jun 30, 2026 | FY2025 or Dec 31, 2025 | Basis |
| --- | --- | --- | --- |
| Total revenues (USD thousands) | 2,007,950 | 1,844,289 | GAAP consolidated; LTM is calculated |
| Interest expense (USD thousands) | 1,342,180 | 1,276,987 | GAAP consolidated; LTM is calculated |
| Net income attributable to STWD (USD thousands) | 227,910 | 411,544 | GAAP; LTM is calculated |
| Distributable Earnings (USD thousands) | 606,926 | 615,534 | Company non-GAAP measure; LTM is calculated |
| Net cash provided by operating activities (USD thousands) | 1,090,565 | 977,852 | GAAP basis; LTM is calculated |
| Cash paid for interest (USD thousands) | 1,236,745 | 1,188,901 | Supplemental cash flow disclosure; LTM is calculated |
| Cash and cash equivalents (USD thousands) | 367,592 | 499,480 | Balance sheet instant |
| Total debt, carrying (USD thousands) | 23,694,124 | 22,094,237 | Secured, securitized and unsecured lines; calculated |
| Total STWD stockholders’ equity (USD thousands) | 6,498,963 | 6,795,516 | Balance sheet instant |
| Total debt / STWD stockholders’ equity | 3.65x | 3.25x | Analyst ratio on the GAAP consolidated perimeter |
| GAAP interest cover | 1.22x | 1.38x | Analyst ratio (income before income taxes plus interest expense, over interest expense: FY2025 is 479,812 plus 1,276,987 over 1,276,987); includes fair value and VIE items |
| Distributable earnings per share to declared dividend per share (6M 2026 in the first column, FY2025 in the second) | 0.81x | 0.88x | Calculated from per-share figures: 0.78 over 0.96, and 1.69 over 1.92 |

### Reported income statement, by quarter

| Line (USD thousands) | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | Locators |
| --- | --- | --- | --- | --- | --- | --- |
| Total revenues | 444,283 | 488,878 | 492,948 | 512,456 | 513,668 | 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:5; 10-Q Q3 2025 page:5; Release YE2025 page:5 |
| Interest income from loans | 385,219 | 395,446 | 383,921 | 373,811 | 398,415 | 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:4; 10-Q Q3 2025 page:5; Release YE2025 page:5 |
| Interest expense | 316,132 | 334,849 | 333,848 | 328,906 | 344,577 | 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:5; 10-Q Q3 2025 page:5; Release YE2025 page:5 |
| Credit loss provision (reversal), net | 5,666 | 28,359 | 10,344 | (377) | 30,164 | 10-Q Q1 2026 page:5; 10-Q Q2 2026 page:5; 10-Q Q3 2025 page:5; Release YE2025 page:5 |
| Income before income taxes | 135,367 | 93,273 | 131,305 | 53,477 | 21,229 | 10-Q Q1 2026 page:5; 10-Q Q2 2026 page:5; 10-Q Q3 2025 page:5; Release YE2025 page:6 |
| Net income | 134,696 | 79,930 | 112,366 | 57,422 | 15,005 | 10-Q Q1 2026 page:5; 10-Q Q2 2026 page:5; 10-Q Q3 2025 page:5; Release YE2025 page:6 |
| Net income attributable to STWD | 129,814 | 72,560 | 96,915 | 51,878 | 6,557 | 10-Q Q1 2026 page:5; 10-Q Q2 2026 page:5; 10-Q Q3 2025 page:5; Release YE2025 page:6 |

The Q2 2025 column is the comparative column of the Q2 2026 10-Q; the Q3 2025 column is the three-month column of the Q3 2025 10-Q; Q4 2025 is the Total column of the year-end release’s three-month statement. Diluted earnings per share as printed: Q2 2025 0.38, Q3 2025 0.19, Q1 2026 0.13, Q2 2026 0.01 (10-Q Q2 2026 page:5; 10-Q Q3 2025 page:5; 10-Q Q1 2026 page:5); the year-end release headline gives 0.26 for Q4 2025 (Release YE2025 page:2 "GAAP EPS of $0.26 for the Quarter").

### Reported income statement, six months and full years

| Line (USD thousands) | 6M 2026 | 6M 2025 | FY2025 | FY2024 | FY2023 | Locators |
| --- | --- | --- | --- | --- | --- | --- |
| Total revenues | 1,026,124 | 862,463 | 1,844,289 | 1,946,843 | 2,049,908 | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| Interest income from loans | 772,226 | 739,142 | 1,518,509 | 1,698,067 | 1,804,104 | 10-K FY2025 page:160; 10-Q Q2 2026 page:4 |
| Interest income from investment securities | 10,188 | 22,534 | 34,461 | 66,805 | 76,524 | 10-K FY2025 page:160; 10-Q Q2 2026 page:4 |
| Servicing fees | 64,687 | 31,540 | 86,543 | 55,199 | 33,121 | 10-K FY2025 page:160; 10-Q Q2 2026 page:4 |
| Rental income | 167,825 | 57,426 | 182,440 | 107,998 | 127,666 | 10-K FY2025 page:160; 10-Q Q2 2026 page:4 |
| Management fees | 66,739 | 71,596 | 137,265 | 145,177 | 141,543 | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| Interest expense | 673,483 | 608,290 | 1,276,987 | 1,348,693 | 1,436,107 | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| General and administrative | 115,027 | 99,219 | 208,809 | 199,236 | 180,212 | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| Depreciation and amortization | 68,986 | 21,855 | 78,981 | 41,306 | 49,141 | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| Credit loss provision (reversal), net | 29,787 | (19,333) | 19,370 | 197,400 | 243,728 | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| Total costs and expenses | 1,005,073 | 814,703 | 1,786,562 | 1,982,072 | 2,098,318 | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| Total other income | 53,655 | 207,474 | 422,085 | 441,238 | 465,885 | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| Income before income taxes | 74,706 | 255,234 | 479,812 | 406,009 | 417,475 | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| Net income | 72,427 | 250,797 | 443,093 | 380,577 | 418,157 | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| Net income attributable to STWD | 58,435 | 242,069 | 411,544 | 359,933 | 339,213 | 10-K FY2025 page:161; 10-Q Q2 2026 page:5 |

### Reported balance sheet

| Line (USD thousands) | Jun 30, 2026 | Mar 31, 2026 | Dec 31, 2025 | Sep 30, 2025 | Dec 31, 2024 | Locators |
| --- | --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 367,592 | 290,285 | 499,480 | 301,135 | 377,831 | 10-K FY2025 page:159; 10-Q Q1 2026 page:3; 10-Q Q2 2026 page:3; 10-Q Q3 2025 page:3 |
| Restricted cash | 272,764 | 375,777 | 175,167 | 237,972 | 176,164 | 10-K FY2025 page:159; 10-Q Q1 2026 page:3; 10-Q Q2 2026 page:3; 10-Q Q3 2025 page:3 |
| Loans held-for-investment, net | 19,816,968 | 19,281,560 | 18,862,712 | 18,318,757 | 15,437,013 | 10-K FY2025 page:159; 10-Q Q1 2026 page:3; 10-Q Q2 2026 page:3; 10-Q Q3 2025 page:3 |
| Loans held-for-sale, at fair value | 2,217,481 | 2,322,940 | 2,323,543 | 2,561,155 | 2,516,008 | 10-K FY2025 page:159; 10-Q Q1 2026 page:3; 10-Q Q2 2026 page:3; 10-Q Q3 2025 page:3 |
| Properties, net | 3,998,669 | 3,859,134 | 3,448,652 | 3,334,483 | 1,373,678 | 10-K FY2025 page:159; 10-Q Q1 2026 page:3; 10-Q Q2 2026 page:3; 10-Q Q3 2025 page:4 |
| Total assets | 61,046,276 | 62,087,328 | 63,183,357 | 62,433,975 | 62,556,497 | 10-K FY2025 page:159; 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:4; 10-Q Q3 2025 page:4 |
| Secured financing agreements, net | 13,999,891 | 13,769,576 | 12,678,948 | 14,663,218 | 11,151,557 | 10-K FY2025 page:159; 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:4; 10-Q Q3 2025 page:4 |
| Securitized financing, net | 4,811,511 | 5,081,897 | 5,131,453 | 3,522,488 | 3,196,426 | 10-K FY2025 page:159; 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:4; 10-Q Q3 2025 page:4 |
| Unsecured senior notes, net | 4,882,722 | 4,287,646 | 4,283,836 | 3,245,122 | 2,994,682 | 10-K FY2025 page:159; 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:4; 10-Q Q3 2025 page:4 |
| VIE liabilities, at fair value | 29,293,820 | 30,768,059 | 32,803,806 | 32,597,454 | 37,288,545 | 10-K FY2025 page:159; 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:4; 10-Q Q3 2025 page:4 |
| Total liabilities | 53,862,850 | 54,738,601 | 55,693,851 | 54,861,935 | 55,363,025 | 10-K FY2025 page:159; 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:4; 10-Q Q3 2025 page:4 |
| Redeemable non-controlling interests (temporary equity) | 356,377 | 357,487 | 364,118 | 385,853 | 426,695 | 10-K FY2025 page:159; 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:4; 10-Q Q3 2025 page:4 |
| Total STWD stockholders’ equity | 6,498,963 | 6,665,469 | 6,795,516 | 6,864,314 | 6,437,107 | 10-K FY2025 page:160; 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:4; 10-Q Q3 2025 page:4 |
| Total permanent equity | 6,827,049 | 6,991,240 | 7,125,388 | 7,186,187 | 6,766,777 | 10-K FY2025 page:160; 10-Q Q1 2026 page:4; 10-Q Q2 2026 page:4; 10-Q Q3 2025 page:4 |

Allowances: loans held-for-investment carry allowances of 419,156 at June 30, 2026 and 440,842 at December 31, 2025 (10-Q Q2 2026 page:3). Dec 31, 2025 and Dec 31, 2024 columns are from the audited 10-K FY2025; the Jun 30, 2026 column is from the 10-Q Q2 2026, which repeats the December 31, 2025 comparatives.

### Reported cash flow

| Line (USD thousands) | 6M 2026 | 6M 2025 | FY2025 | FY2024 | FY2023 | Locators |
| --- | --- | --- | --- | --- | --- | --- |
| Net cash provided by operating activities | 264,224 | 151,511 | 977,852 | 646,586 | 528,597 | 10-K FY2025 page:163; 10-Q Q2 2026 page:8 |
| Net cash (used in) provided by investing activities | (1,370,555) | (1,858,825) | (3,776,452) | 2,083,954 | 855,074 | 10-K FY2025 page:163; 10-Q Q2 2026 page:8 |
| Net cash provided by (used in) financing activities | 1,071,058 | 1,627,352 | 2,919,558 | (2,485,900) | (1,454,563) | 10-K FY2025 page:163; 10-Q Q2 2026 page:8 |
| Payment of dividends | (356,995) | (326,033) | (668,855) | (619,996) | (601,192) | 10-K FY2025 page:163; 10-Q Q2 2026 page:8 |
| Cash paid for interest | 609,792 | 561,948 | 1,188,901 | 1,294,131 | 1,351,533 | 10-K FY2025 page:164; 10-Q Q2 2026 page:9 |
| Income taxes paid | 5,202 | 154 | 696 | 4,010 | 1,670 | 10-K FY2025 page:164; 10-Q Q2 2026 page:9 |
| Cash, cash equivalents and restricted cash, end of period | 640,356 | 474,865 | 674,647 | 553,995 | 311,972 | 10-K FY2025 page:164; 10-Q Q2 2026 page:9 |

Financing and investing lines are on the GAAP basis that includes consolidated VIEs. The 10-Q Q2 2026 also presents cash flows "Excluding Securitization VIEs" (page:137): operating cash flow on that basis is 261,329 for 6M 2026 against 264,224 on the GAAP basis. Cash paid for interest and income taxes paid are from the supplemental disclosure.

### Distributable earnings (company non-GAAP measure)

| Measure | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | 6M 2026 | 6M 2025 | FY2025 | Locators |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Distributable Earnings (non-GAAP), USD thousands | 148,604 | 159,545 | 147,274 | 151,503 | 298,777 | 307,385 | 615,534 | 10-Q Q2 2026 page:129; 10-Q Q2 2026 page:130; 10-Q Q3 2025 page:125; Release Q1 2026 page:5; Release Q2 2026 page:5; Release YE2025 page:7; Release YE2025 page:9 |
| Distributable Earnings per diluted share, USD | 0.40 | 0.42 | 0.39 | 0.40 | 0.78 | 0.88 | 1.69 | same pages |

Definition (Release Q2 2026 page:4): "Distributable Earnings, a non-GAAP financial measure, is used to compute the Company’s incentive fees to its external manager". It is net income attributable to the registrant adjusted for non-cash and other items per the company’s reconciliation. It is a management-attributed measure and does not replace a GAAP figure.

### Segment view, Q2 2026 (management segment statements)

| Q2 2026, USD thousands | Commercial and Residential Lending | Infrastructure Lending | Property | Investing and Servicing | Corporate | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Net income (loss) attributable to STWD | 133,938 | 26,094 | (2,215) | 24,480 | (175,740) | 6,557 |
| Distributable Earnings (Loss) | 185,728 | 27,139 | 34,177 | 42,389 | (137,930) | 151,503 |
| Total assets at Jun 30, 2026 (before securitization VIE column) | 21,331,144 | 3,433,002 | 5,215,719 | 1,595,708 | 196,539 | 31,772,112 |

Locators: Release Q2 2026 pages 4, 5 and 7. In the Q2 2026 segment statement the Corporate column carries management fees of 30,392 and interest expense of 107,564 (Release Q2 2026 page:3), and the MD&A attributes the Corporate loss to interest on unsecured senior notes and secured term loans (10-Q Q2 2026 page:137). The Corporate figure is the largest negative figure in each of the two rows.

### Debt as reported

Unsecured senior notes at the registrant level:

| Instrument | Coupon | Maturity | Principal Jun 30, 2026 | Principal Dec 31, 2025 | Locator |
| --- | --- | --- | --- | --- | --- |
| 2027 Convertible Notes | 6.75% | 7/15/2027 | 380,750 | 380,750 | 10-Q Q2 2026 page:55 |
| 2026 Senior Notes | 3.63% | 7/15/2026 | 400,000 | 400,000 | 10-Q Q2 2026 page:55 |
| 2027 Senior Notes | 4.38% | 1/15/2027 | 500,000 | 500,000 | 10-Q Q2 2026 page:56 |
| 2028 Senior Notes | 5.25% | 10/15/2028 | 500,000 | 500,000 | 10-Q Q2 2026 page:56 |
| 2029 Senior Notes | 7.25% | 4/1/2029 | 600,000 | 600,000 | 10-Q Q2 2026 page:56 |
| April 2030 Senior Notes | 6.00% | 4/15/2030 | 400,000 | 400,000 | 10-Q Q2 2026 page:56 |
| July 2030 Senior Notes | 6.50% | 7/1/2030 | 500,000 | 500,000 | 10-Q Q2 2026 page:56 |
| October 2030 Senior Notes | 6.50% | 10/15/2030 | 500,000 | 500,000 | 10-Q Q2 2026 page:56 |
| January 2031 Senior Notes | 5.75% | 1/15/2031 | 550,000 | 550,000 | 10-Q Q2 2026 page:56 |
| June 2031 Senior Notes | 6.13% | 6/1/2031 | 600,000 | — | 10-Q Q2 2026 page:56 |
| Total principal amount | — | — | 4,930,750 | 4,330,750 | 10-Q Q2 2026 page:56 |

Secured and securitized financing (principal outstanding unless stated):

| Secured financing, outstanding (USD thousands) | Jun 30, 2026 | Dec 31, 2025 | Locator |
| --- | --- | --- | --- |
| Total repurchase agreements | 9,759,429 | 8,890,092 | 10-Q Q2 2026 page:49 |
| Total other secured financing | 4,333,787 | 3,890,701 | 10-Q Q2 2026 page:49 |
| Total secured financing agreements, principal | 14,093,216 | 12,780,793 | 10-Q Q2 2026 page:49 |
| Securitized financing, principal (CLOs, SASB, ABS) | 4,839,145 | 5,153,316 (derived: 17,934,109 less 12,780,793) | 10-Q Q2 2026 page:55; 10-K FY2025 page:138 |
| Secured plus securitized financing, principal outstanding | 18,932,361 | 17,934,109 | 10-Q Q2 2026 page:143; 10-K FY2025 page:138 |
| Approved but undrawn capacity, secured borrowings (total) | 1,399,046 | 1,596,919 | 10-Q Q2 2026 page:143; 10-K FY2025 page:138 |

Detail by facility (maximum size, outstanding, approved undrawn capacity, pledged asset carrying value) is in 10-Q Q2 2026 pages 49 and 143 and is carried to the credit module. The maturity schedule for secured and securitized financing on a fully extended or collateral-driven basis shows a total of 18,932,361 (10-Q Q2 2026 page:55 "Total $ 9,759,429 $ 4,333,787 $ 4,839,145 $ 18,932,361").

### Evidence-based interpretation

1. Earnings. Net income attributable to the registrant was 6,557 in Q2 2026 against 129,814 in Q2 2025 (quarterly table). The statement shows the sources: total other income was 32,329 against 121,563 a year earlier, the credit loss provision was 30,164 against 5,666, depreciation and amortization was 35,260 against 10,371, the income tax provision was (6,224) against (671) and income attributable to non-controlling interests was (8,448) against (4,882) (10-Q Q2 2026 pages 4 and 5). The prior-year quarter included a foreign currency gain of 83,761, offset in part by a derivative loss of (101,296). Revenue rose, 513,668 against 444,283, and so did interest expense, 344,577 against 316,132. Rental income, 87,854 against 28,243, is the revenue line with the largest increase; the registrant acquired Fundamental Income Properties, LLC on July 23, 2025 (10-K FY2025 page:9), which falls between the two quarters, so the rise is consistent with that acquisition, though the filings read here do not split it out in this table.
2. Distributable earnings versus GAAP. Distributable earnings in Q2 2026 was 151,503 against 148,604 in Q3 2025, 159,545 in Q4 2025 and 147,274 in Q1 2026. The segment table shows the Commercial and Residential Lending segment at 185,728 and Corporate at (137,930). The reconciliation adds back, among other items, the credit loss provision (30,164), depreciation and amortization (35,570) and non-cash equity compensation (13,313) (Release Q2 2026 pages 4 and 5). A creditor should read cash earnings power from distributable earnings with the understanding that, per the company’s reconciliation, it removes the credit loss provision and unrealized and other non-cash items that GAAP net income includes.
3. Leverage. Total debt over stockholders’ equity rose each date from Dec 31, 2024 (2.69x) to Jun 30, 2026 (3.65x), through 3.12x at Sep 30, 2025, 3.25x at Dec 31, 2025 and 3.47x at Mar 31, 2026. In 6M 2026, debt rose by 1,599,887 (23,694,124 less 22,094,237) and stockholders’ equity fell by 296,553 (6,795,516 less 6,498,963). Unsecured notes were 20.6% of total debt at Jun 30, 2026, from 19.4% at Dec 31, 2025.
4. Payout. The company declared 0.48 a share in Q2 2026 and in Q2 2025 and 0.96 in each six-month period (10-Q Q2 2026 page:6 and page:7); distributable earnings per share was 0.40 in Q2 2026 and 0.39 in Q1 2026, below that level, and 0.78 for 6M 2026 against 0.96 declared. The accumulated deficit increased by the amount by which dividends declared exceeded net income (Calculations). Operating cash flow of 264,224 in 6M 2026 was lower than dividends paid of 356,995; over the LTM, operating cash flow of 1,090,565 was higher than dividends paid of 699,817. Operating cash flow in a lender includes loan held-for-sale flows, so the two periods are not directly comparable.
5. Cash interest. Cash paid for interest of 609,792 in 6M 2026 compares with interest expense of 673,483; the LTM cash-to-expense ratio is 92.1%. Part of the gap is non-cash amortization of deferred financing costs (about 18.4 million dollars in 6M 2026 on secured financing agreements, 10-Q Q2 2026 page:50), but the filings read here do not itemise the whole difference.
6. Interest spread. LTM interest income of 1,573,708 exceeds LTM interest expense of 1,342,180 by 231,528. The ratio is 1.17x, and it excludes servicing, rental and fair value income and the VIE net change line.
7. Funding structure and maturities. Secured and securitized financing principal is 18,932,361 of which the earliest scheduled amounts are 969,797 for the remainder of 2026 and 2,738,779 for 2027 (10-Q Q2 2026 page:55). Unsecured notes were 4,930,750 at June 30, 2026 with 900,000 due within a year then; July 2026 events removed that near-term amount (pro forma in Calculations), leaving 380,750 of convertible notes due July 15, 2027 as the first unsecured maturity.
8. Credit quality links for the next modules. Nonaccrual loans, the allowance and funding commitments sit in the credit module’s scope (10-Q Q2 2026 pages 33 and 94); this module records the allowance on loans held-for-investment (419,156) and the provision line only.

## Calculations

### LTM bridge (twelve months to June 30, 2026)
Formula: FY2025 plus 6M 2026 less 6M 2025, USD thousands, each input from the period table above (10-K FY2025 pages 160 to 164; 10-Q Q2 2026 pages 4 to 9). Cross-check: the sum of Q3 2025, Q4 2025, Q1 2026 and Q2 2026 from the quarterly table.

| Measure | FY2025 | plus 6M 2026 | less 6M 2025 | LTM Jun 2026 | Sum of four quarters |
| --- | --- | --- | --- | --- | --- |
| Total revenues | 1,844,289 | 1,026,124 | 862,463 | 2,007,950 | 2,007,950 |
| Interest expense | 1,276,987 | 673,483 | 608,290 | 1,342,180 | 1,342,180 |
| Net income attributable to STWD | 411,544 | 58,435 | 242,069 | 227,910 | 227,910 |
| Income before income taxes | 479,812 | 74,706 | 255,234 | 299,284 | Not calculated (quarterly figure not in the table) |
| Interest income from loans | 1,518,509 | 772,226 | 739,142 | 1,551,593 | Not calculated (quarterly figure not in the table) |
| Interest income from investment securities | 34,461 | 10,188 | 22,534 | 22,115 | Not calculated (quarterly figure not in the table) |
| Net cash provided by operating activities | 977,852 | 264,224 | 151,511 | 1,090,565 | Not calculated (quarterly figure not in the table) |
| Payment of dividends (outflow shown positive) | 668,855 | 356,995 | 326,033 | 699,817 | Not calculated (quarterly figure not in the table) |
| Cash paid for interest | 1,188,901 | 609,792 | 561,948 | 1,236,745 | Not calculated (quarterly figure not in the table) |
| Credit loss provision (reversal), net | 19,370 | 29,787 | (19,333) | 68,490 | Not calculated (quarterly figure not in the table) |
| Distributable Earnings (non-GAAP) | 615,534 | 298,777 | 307,385 | 606,926 | 606,926 |

Tie-outs. Q1 2026 plus Q2 2026 revenue is 512,456 plus 513,668, which equals the 6M 2026 figure of 1,026,124; net income attributable is 51,878 plus 6,557, which equals 58,435. Q4 2025 in the year-end release equals FY2025 less nine months 2025 in the Q3 2025 report for revenue (1,844,289 less 1,351,341 is 492,948), interest expense (1,276,987 less 943,139 is 333,848) and net income attributable (411,544 less 314,629 is 96,915). Distributable earnings Q4 2025 equals FY2025 less 6M 2025 less Q3 2025 (615,534 less 307,385 less 148,604 is 159,545).

### Leverage and funding mix (carrying values, GAAP consolidated perimeter)
Formula: total debt is secured financing agreements, net plus securitized financing, net plus unsecured senior notes, net, as printed on each balance sheet. Equity is total Starwood Property Trust, Inc. stockholders’ equity. VIE liabilities at fair value are not debt in this measure. Ratios are total debt divided by equity, rounded to two decimals. The securitized-financing exclusion is shown because the balance-sheet note states that those VIE liabilities do not have recourse to the registrant.

| Date | Secured financing agreements | Securitized financing | Unsecured senior notes | Total debt (carrying) | STWD stockholders’ equity | Total debt / STWD equity | Debt excl. securitized financing / STWD equity | Unsecured notes / total debt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jun 30, 2026 | 13,999,891 | 4,811,511 | 4,882,722 | 23,694,124 | 6,498,963 | 3.65x | 2.91x | 20.6% |
| Mar 31, 2026 | 13,769,576 | 5,081,897 | 4,287,646 | 23,139,119 | 6,665,469 | 3.47x | 2.71x | 18.5% |
| Dec 31, 2025 | 12,678,948 | 5,131,453 | 4,283,836 | 22,094,237 | 6,795,516 | 3.25x | 2.50x | 19.4% |
| Sep 30, 2025 | 14,663,218 | 3,522,488 | 3,245,122 | 21,430,828 | 6,864,314 | 3.12x | 2.61x | 15.1% |
| Dec 31, 2024 | 11,151,557 | 3,196,426 | 2,994,682 | 17,342,665 | 6,437,107 | 2.69x | 2.20x | 17.3% |

Equity basis check at June 30, 2026: total permanent equity of 6,827,049 plus redeemable non-controlling interests of 356,377 is 7,183,426; total debt of 23,694,124 divided by that figure is 3.30x. At December 31, 2025 the same basis gives 7,489,506 and 2.95x.

### Earnings, coverage and payout measures (LTM and 6M 2026)
| Measure | Formula and inputs (USD thousands) | Result |
| --- | --- | --- |
| GAAP interest cover | (LTM income before income taxes 299,284 plus LTM interest expense 1,342,180) divided by LTM interest expense | 1.22x |
| Revenue to interest expense | LTM total revenues 2,007,950 divided by LTM interest expense 1,342,180 | 1.50x |
| Interest income to interest expense | LTM interest income from loans 1,551,593 plus from investment securities 22,115 is 1,573,708; divided by LTM interest expense 1,342,180 | 1.17x |
| Net of the two, USD thousands | 1,573,708 less 1,342,180 | 231,528 |
| Cash interest to interest expense, LTM | cash paid for interest 1,236,745 divided by interest expense 1,342,180 | 92.1% |
| Operating cash flow to dividends paid, LTM | 1,090,565 divided by 699,817 | 1.56x |
| Operating cash flow to dividends paid, 6M 2026 | 264,224 divided by 356,995 | 0.74x |
| Distributable earnings to dividends declared, 6M 2026 | 298,777 divided by 357,326 (dividends declared, 10-Q Q2 2026 page:7) | 0.84x |
| Distributable earnings per share to dividends declared per share, 6M 2026 | 0.78 divided by 0.96 | 0.81x |
| Same, Q2 2026 | 0.40 divided by 0.48 | 0.83x |
| Same, FY2025 | 1.69 divided by 1.92 (dividends declared per share for 2025, 10-K FY2025 page:162) | 0.88x |

These measures use GAAP income before income taxes, which includes the net change in consolidated VIEs, fair value changes, foreign currency and derivative gains and losses; they are analyst ratios, not covenant ratios and not company-defined.

Equity roll check, 6M 2026: accumulated deficit moved from (39,018) to (337,909), a change of (298,891); net income attributable to the registrant of 58,435 less dividends declared of 357,326 is (298,891), which matches.

### Perimeter bridge: GAAP consolidated versus management ex-VIE presentation, June 30, 2026
Inputs from the segment balance sheet (Release Q2 2026 page:7): total assets, subtotal before the securitization VIE column 31,772,112; secured financing agreements, net 14,019,547; securitized financing, net 4,811,511; unsecured senior notes, net 4,882,722. Debt on that perimeter is 23,713,780; divided by the subtotal assets the result is 74.6%. On the GAAP perimeter, total debt of 23,694,124 divided by total assets of 61,046,276 is 38.8%, and total liabilities of 53,862,850 divided by total assets is 88.2%. The two percentages answer different questions and must not be compared as a trend. The release subtotal is not simply total assets less the balance-sheet line for VIE assets (61,046,276 less 30,868,147 is 30,178,129); the difference of 1,593,983 equals the securities, intangibles and unconsolidated-entity amounts eliminated against VIE balances in the VIE column (1,540,884 plus 38,069 plus 15,030).

### Unsecured senior notes: June 30, 2026 table and July 2026 pro forma (labelled pro forma, USD thousands)
Principal at June 30, 2026 is 4,930,750 (10-Q Q2 2026 page:56). Subsequent events (10-Q Q2 2026 page:101): 500,000 of 5.875% Senior Notes due August 15, 2029 issued to redeem the 500,000 2027 Senior Notes; 400,000 of 2026 Senior Notes repaid at maturity. Pro forma principal is 4,930,750 less 400,000 (repaid) plus 500,000 (issued) less 500,000 (redeemed), which is 4,530,750. By year: 2027 380,750 (convertible notes due July 15, 2027); 2028 500,000; 2029 1,100,000 (600,000 due April 1, 2029 plus 500,000 due August 15, 2029); 2030 1,400,000 (400,000 plus 500,000 plus 500,000); 2031 1,150,000 (550,000 plus 600,000). These add to 4,530,750. This is arithmetic on disclosed terms, not a company-reported figure.

### Liquidity inputs (no company-defined June 30, 2026 liquidity figure was located)
Cash and cash equivalents 367,592 and restricted cash 272,764 (10-Q Q2 2026 page:3); the sum of the two matches the cash flow statement end balance of 640,356. Lender-approved but undrawn capacity on secured borrowings is 1,399,046 in total, of which 200,000 is under term loans and revolver (10-Q Q2 2026 page:143). Cash plus approved undrawn capacity is 367,592 plus 1,399,046, which is 1,766,638. This is an analyst construct, not the company’s liquidity definition: approved capacity depends on pledged collateral, the unallocated financing amount of 9,992,934 is not available capacity, and letters of credit drawn on facilities are not netted because no such deduction was located. The CP-2 liquidity work must rebuild this by facility.

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| No filing or release for any period after June 30, 2026 | All balance-sheet and covenant-relevant figures are as of June 30, 2026; events up to 2026-11-05 are unknown beyond the July 2026 subsequent events in the Q2 10-Q | Label every figure as of June 30, 2026; do not state that nothing happened afterwards |
| Interim 2026 and Q3 2025 statements are unaudited | The latest base is not audited | Use the FY2025 audited statements for year-end facts |
| Q4 2025 is taken from the year-end release; it ties to FY2025 less nine months 2025 for the revenue, interest expense, net income and distributable earnings lines checked | Management-attributed for the other Q4 lines | Use the tie-outs; flag lines not tied |
| Distributable earnings is a company non-GAAP measure, from releases and the 10-Q MD&A | It cannot replace GAAP earnings in a coverage test | Show both; label the source |
| Consolidated and ex-VIE perimeters differ; some ex-VIE figures exist only in releases and the MD&A | Leverage ratios depend on the perimeter | Name the perimeter on every ratio; the filing controls for GAAP facts |
| No company-defined liquidity figure for June 30, 2026 located; the bulleted list of liquidity sources is not in the extracted text, as noted in the readiness handoff | Liquidity inputs are an analyst construct | Rebuild by facility in the credit module; check the original HTML |
| Covenant levels, guarantor terms and ratings not supplied (readiness handoff) | No covenant headroom can be computed here | Mark Not calculable in the credit module unless documents are supplied |
| Quarterly figures for Q3 2025 and Q4 2025 for lines other than those shown (for example cash flow) were not extracted | No quarterly cash-flow trend | Use 6M and FY periods |

Correction or refinement of the readiness handoff: it listed Q4 2025 as available only in the release; this module confirms that revenue, interest expense, net income attributable and distributable earnings for Q4 2025 also follow from the FY2025 and nine-month 2025 filed figures. No other correction was needed.

## Next module

CP-1A (business and transaction view) should use this base for the segment structure, the Fundamental acquisition, the 2026 financing and securitization transactions and the July 2026 subsequent events, and should carry forward the perimeter labels, the LTM and quarter definitions, and the gaps above. CP-2 should rebuild liquidity and maturities by facility from 10-Q Q2 2026 pages 49, 55, 56 and 143, treat covenant headroom as Not calculable without the governing documents, and keep the June 30, 2026 table separate from the July 2026 pro forma.
