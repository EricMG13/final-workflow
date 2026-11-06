## Request

Issuer: TPG RE Finance Trust, Inc. (issuer id trtx; NYSE ticker TRTX). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. The statements are in thousands of US dollars; the chart tables below are in US$m as their headers require. Current period named by the context: Q3 2026 (quarter ended 2026-09-30). Prior period named by the context: FY2025.

Task for this module: build the financial base for the downstream modules from the pinned filings: reported statements, funding structure, liquidity, covenants, earnings measures and the credit-quality indicators that a commercial real estate lender needs. Entity perimeter: TPG RE Finance Trust, Inc. and its consolidated subsidiaries, including consolidated variable interest entities (the CRE CLO issuers). No other perimeter is used. The company is externally managed, reports one segment, and has no EBITDA line in any supplied source.

Periods are labelled throughout: Q1 2026, Q2 2026 and Q3 2026 are the discrete three-month periods in each 10-Q; nine months 2026 (9M 2026) is the year-to-date period to 2026-09-30; LTM is the twelve months to 2026-09-30, derived as FY2025 plus 9M 2026 minus 9M 2025; balance sheet items are at the period end date.

## Sources

Locators are `page:N` chunks of the named file, not printed pages. The sha256 is the pinned file hash.

### Issuer sources relied on

| Source name | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_trtx-20251231.htm.jsonl | 7b7b804dc956c7ba20b8c615f59942074ed4837f19257133ae8d92323027d7ec | Audited FY2025 statements and notes, FY2024 and FY2023 comparatives, liquidity at 2025-12-31 |
| 10-Q_2026-03-31_trtx-20260331.htm.jsonl | 41f66a4a0f2f9734dca4554ee0dc2ef549772c06941cdfec976d06a5c1955d4c | Q1 2026 unaudited statements, funding, liquidity and covenants |
| 10-Q_2026-06-30_trtx-20260630.htm.jsonl | 8f3da972b3575ac6703be3527817c87d3dc87cac2d5c8e1d4e7f81f5f78727e9 | Q2 2026 and six-month statements; Term Loan B and Revolver closing |
| 10-Q_2026-09-30_trtx-20260930.htm.jsonl | 4884d7a3b9e5f3a0f552349b7976aff0931070e9957fb8740966840f61145adc | Q3 2026 and nine-month statements; controlling source for the latest balance sheet, funding, covenants and liquidity |
| EX-99.1_2026-04-28_trtx-20260428exhibit991.htm.jsonl | 1e95941ab9e70def087e8a13656b49994337a0e1c905b17c9ac6471bddea9d88 | Q1 2026 earnings release; supporting management claims and Distributable Earnings reconciliation |
| EX-99.1_2026-07-28_trtx-20260728exhibit991.htm.jsonl | 85e111cdb3f106d12964e884db844b225d24404d7815e760f617225c97335579 | Q2 2026 earnings release; same role |
| EX-99.1_2026-10-26_trtx-20261026exhibit991.htm.jsonl | 262caea8fdb587a93bfd4ce5d18d486a64c133d5eee9d2c7316a1e31375c2fe8 | Q3 2026 earnings release; same role |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | ef96ebbdf5dd00ebb7411d32513edde7f00e3900728e79b850efc1744349d270 | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | f67c880ae13bd9b442ec32f542cac48afaa8a23c51c32c03c025a6a9e94e025f | Source readiness: all four consumers READY_WITH_LIMITATIONS; carried limits are no executed agreements, no covenant test values, no later filings and no presentations |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Funding and leverage grew sharply in 2026 while earnings softened in the third quarter. Liquidity is adequate but thin against promised loan fundings, and EBITDA-based metrics do not exist for this lender, so leverage rests on debt-to-equity. | Medium | No EBITDA is reported and covenant test values and executed agreements are not supplied, so coverage and covenant headroom cannot be measured. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt principal rose from 3,309,462 thousand at 2025-12-31 to 4,198,054 thousand at 2026-09-30 while equity fell, lifting total leverage from 3.02x to 4.03x. | Less equity supports each dollar of debt, and the new Term Loan B adds a fully recourse corporate claim. | High |
| Net income was 9,366 thousand in Q3 2026 against 21,993 thousand a year earlier; Distributable Earnings were 5,118 thousand after a 13,006 thousand realized loss. | Earnings only roughly matched the common dividend before realized losses and fell short after them, so equity is being drawn down. | High |
| Near-term liquidity was 291,634 thousand at 2026-09-30, of which 52.6 million of cash is held for liquidity covenants, against unfunded loan commitments of 236,552 thousand. | Usable liquidity is thinner than the headline and close to the loan funding the company has promised. | Medium |
| The largest maturity year is 2028 at 1,130,841 thousand; 45.7% of debt is non-recourse CLO debt and 78.8% is not subject to market-value margin calls. | Refinancing is clustered in 2028, while CLO and non-mark-to-market funding limit margin-call risk. | Medium |
| No EBITDA is reported anywhere in the pack, and covenant test values are printed only as levels plus a compliance statement. | EBITDA leverage and cover cannot be shown and covenant headroom cannot be measured, so downstream work must use debt-to-equity and interest income cover. | High |

### Financial base view

The financial base is sufficient to support a credit snapshot of TRTX on a reported basis, with the limits stated here. TRTX is a floating-rate commercial real estate lender: 99.7% of loan commitments are floating rate (10-Q Q3 page:31), and loans held for investment of 4,916,375 thousand at amortized cost make up most of total assets of 5,242,861 thousand (page:6-7). There is no EBITDA, so the chart selectors for EBITDA leverage and cover are recorded as Not supplied and the leverage and cover analysis is built on the company's own debt-to-equity and total leverage ratios, on debt principal against equity, and on interest income against interest expense.

The main story is balance sheet growth funded with debt. Total debt principal grew from 3,309,462 thousand at 2025-12-31 to 4,198,054 thousand at 2026-09-30 (10-Q Q3 page:89), an increase of 888,592 thousand, while total stockholders' equity fell from 1,068,023 thousand to 1,024,126 thousand (page:7). The company's own total leverage ratio, debt including the Term Loan B less cash over equity, rose from 3.02x to 4.03x (page:104-105). Most of the increase came in Q3 2026: the same ratio was 3.10x at 2026-03-31 and 3.32x at 2026-06-30 (10-Q Q1 page:93; 10-Q Q2 page:102). Funding changed in kind as well as in size: the 2022 CLO was redeemed in May 2026 (page:43), and funding moved to larger secured credit agreements with Wells Fargo, Citi and Goldman Sachs, a secured revolver drawn to 264,963 thousand, and a new 400,000 thousand Term Loan B that is fully recourse (page:56, page:89). The share of debt that is non-recourse CLO debt fell from 78.4% at 2025-12-31 to 45.7% at 2026-09-30 (page:77, page:89).

Earnings are lower and thinner than in 2025. Net interest income was 76,067 thousand in 9M 2026 against 78,334 thousand in 9M 2025, because interest expense grew by 17,019 thousand while interest income grew by 14,752 thousand (page:7-8, page:102). Credit loss expense was 11,850 thousand in 9M 2026 against 2,594 thousand in 9M 2025. Net income was 41,437 thousand against 56,343 thousand. Q3 2026 was the weakest quarter: net income 9,366 thousand against 21,993 thousand in Q3 2025, credit loss expense 8,573 thousand, and Distributable Earnings of 5,118 thousand after a 13,006 thousand realized loss on a Plano multifamily foreclosure (page:39, page:81). Distributable Earnings before realized losses were 18,124 thousand against a common dividend declared of 18,508 thousand (release 2026-10-26 page:8). Loan credit metrics are otherwise stable on the face of the filing: weighted average risk rating 3.0 unchanged, no loan on non-accrual at 2026-09-30 compared with one of 41.0 million at 2025-12-31, and an allowance of 147 basis points of total commitments (page:34, page:37, page:88). The quality of the book changed in one respect worth carrying forward: office exposure was 4.3% of commitments at 2026-06-30 and 7.9% at 2026-09-30 after a 212.0 million San Francisco office loan was originated on 2026-09-24 (10-Q Q2 page:71; 10-Q Q3 page:72, page:116). The Q1 2026 release had said office exposure was below 5% (release 2026-04-28 page:2); that was a management statement about a point in time and does not describe 2026-09-30.

Liquidity is adequate on the headline and thin on a usable basis. Near-term liquidity of 291,634 thousand at 2026-09-30 includes 70,826 thousand of cash of which 52.6 million is held to satisfy liquidity covenants (page:28, page:77, page:105). Unfunded loan commitments are 236,552 thousand (page:71). The covenant package changed when the Term Loan B and Revolver closed (page:55): the investment-portfolio debt-to-equity covenant of 4.25x is shown as not applicable currently, a total debt to total assets maximum of 83.333% applies, and the interest coverage minimum fell from 1.4x to 1.3x. The company states it was in compliance with all financial covenants (page:55, page:57), but the actual test values are not printed, so no headroom is reported as a company figure; an indicative balance sheet debt to assets ratio is set out in Calculations with its caveats.

Every figure below is a reported or derived USD figure on the TRTX consolidated perimeter. Statements are unaudited for the 2026 periods and audited for FY2025 (10-K page:175-177).

### Financials and credit metrics

| Line (USD thousands unless stated) | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | 9M 2026 | 9M 2025 | LTM Q3 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Interest income | 290237 | 74179 | 74053 | 82339 | 230571 | 215819 | 304989 | Flows; LTM derived. 10-K page:178; 10-Q Q1 page:7-8; Q2 page:7-8; Q3 page:7-8 |
| Interest expense | (186460) | (48462) | (50387) | (55655) | (154504) | (137485) | (203479) | Flows; LTM derived. Same pages |
| Net interest income | 103777 | 25717 | 23666 | 26684 | 76067 | 78334 | 101510 | Printed; LTM derived |
| Revenue from real estate owned operations | 34259 | 8288 | 9081 | 8078 | 25447 | 26466 | 33240 | Printed; LTM derived |
| Credit loss (expense) benefit, net | (13871) | 286 | (3563) | (8573) | (11850) | (2594) | (23127) | Printed; LTM derived |
| Net income | 60319 | 18939 | 13132 | 9366 | 41437 | 56343 | 45413 | Printed; LTM derived |
| Net income attributable to common stockholders | 45479 | 15166 | 9354 | 5820 | 30340 | 45290 | 30529 | Printed; LTM derived |
| Distributable earnings (issuer non-GAAP, after realized losses) | 76778 | 19513 | 17619 | 5118 | 42250 | n/a not printed for 9M 2025 | 60713 | 10-K page:124; releases page:8; 9M 2026 and LTM derived as sums of printed quarters and Q4 2025 |
| Distributable earnings before realized losses (issuer non-GAAP) | 76778 | 19513 | 17619 | 18124 | 55256 | n/a not printed for 9M 2025 | 73719 | Same basis |
| Cash and cash equivalents (at period end) | 87613 | 91985 | 65577 | 70826 | 70826 | n/a balance at date | n/a balance at date | Balances: 10-K page:177-178; 10-Q Q1 page:6; Q2 page:6; Q3 page:6 |
| Loans held for investment, amortized cost (at period end) | 4103022 | 4129958 | 4321538 | 4916375 | 4916375 | n/a balance at date | n/a balance at date | Same pages |
| Allowance for credit losses on loans (at period end) | (74503) | (74033) | (77750) | (73955) | (73955) | n/a balance at date | n/a balance at date | Excludes the unfunded-commitment reserve |
| Total assets (at period end) | 4406230 | 4472255 | 4596932 | 5242861 | 5242861 | n/a balance at date | n/a balance at date | Printed |
| Total debt principal (at period end) | 3309462 | 3382090 | 3531816 | 4198054 | 4198054 | n/a balance at date | n/a balance at date | Principal, all borrowings incl. Term Loan B: 10-K page:225-226; 10-Q Q1 page:50; Q2 page:56; Q3 page:57 |
| Total stockholders' equity (at period end) | 1068023 | 1062134 | 1044494 | 1024126 | 1024126 | n/a balance at date | n/a balance at date | Printed; includes preferred liquidation preference of 201,250 |
| Debt-to-equity ratio as printed (x) | 3.02 | 3.10 | 2.94 | 3.64 | 3.64 | n/a balance at date | n/a balance at date | Issuer definition: secured financing arrangements less cash over equity, excl. Term Loan B and Revolver: 10-K page:146; Q1 page:93; Q2 page:102; Q3 page:104 |
| Total leverage ratio as printed (x) | 3.02 | 3.10 | 3.32 | 4.03 | 4.03 | n/a balance at date | n/a balance at date | Issuer definition including Term Loan B and Revolver |
| Near-term liquidity as printed | 143022 | 172849 | 488181 | 291634 | 291634 | n/a balance at date | n/a balance at date | Issuer table: 10-K page:147; Q1 page:93-94; Q2 page:103; Q3 page:105 |
| Interest income to interest expense (x, derived) | 1.56 | 1.53 | 1.47 | 1.48 | 1.49 | 1.57 | 1.50 | Derived; not a covenant measure; see Calculations |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | Not supplied: the issuer reports no EBITDA in any supplied source and is a mortgage REIT | Not supplied: no EBITDA | x | Search of all seven sources for EBITDA returned no hits. The issuer's own debt-to-equity of 3.02x and net-of-cash leverage are in the financials table |
| Q1 2026 | Not supplied: no EBITDA | Not supplied: no EBITDA | x | As above; issuer total leverage ratio 3.10x at 2026-03-31 (10-Q Q1 page:93) |
| Q2 2026 | Not supplied: no EBITDA | Not supplied: no EBITDA | x | As above; issuer total leverage ratio 3.32x at 2026-06-30 (10-Q Q2 page:102) |
| Q3 2026 | Not supplied: no EBITDA | Not supplied: no EBITDA | x | As above; issuer total leverage ratio 4.03x at 2026-09-30 (10-Q Q3 page:104-105); definition is issuer-specific |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | Not supplied: no EBITDA reported | x | Cash interest paid was 179,722 thousand (10-K page:181). Interest income to interest expense was 1.56x on a derived basis, not EBITDA cover |
| Q1 2026 | Not supplied: no EBITDA reported | x | Cash interest paid 46,301 thousand (10-Q Q1 page:9), year to date; derived ratio 1.53x |
| Q2 2026 | Not supplied: no EBITDA reported | x | Cash interest paid 96,092 thousand for six months (10-Q Q2 page:10); derived quarterly ratio 1.47x |
| Q3 2026 | Not supplied: no EBITDA reported | x | Cash interest paid 148,023 thousand for nine months (10-Q Q3 page:10); derived quarterly ratio 1.48x; covenant minimum is 1.3 to 1.0 on an undisclosed definition |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 87.613 | 51.433 | US$m | Cash and cash equivalents at 2025-12-31. Undrawn is the issuer's secured credit agreement 21.433 plus secured revolving facility 30.000 (10-K page:147); not contractual commitment less drawn |
| Q1 2026 | 91.985 | 39.694 | US$m | 2026-03-31; secured credit agreement capacity of 39.694 and nil on the secured revolver (10-Q Q1 page:94) |
| Q2 2026 | 65.577 | 417.397 | US$m | 2026-06-30; secured credit agreements 297.397, secured revolver 20.000, Revolver 100.000 (10-Q Q2 page:103). The jump reflects the Citi facility closed 2026-06-30 and the new Revolver |
| Q3 2026 | 70.826 | 209.317 | US$m | 2026-09-30; secured credit agreements 87.317, secured revolver 22.000, Revolver 100.000 (10-Q Q3 page:105). Cash includes 52.6 held for liquidity covenants. Excludes 11.491 CLO reinvestment proceeds at the trustee. Contractual availability under the secured credit agreements is larger at 777.844 but depends on lender-approved collateral (page:47, page:91) |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 remainder | 1.000 | US$m | Principal at 2026-09-30 (10-Q Q3 page:57). Term Loan B amortization only |
| 2027 | 24.467 | US$m | CLO 20.467 plus Term Loan B 4.000 |
| 2028 | 1130.841 | US$m | Secured credit agreements 792.580, secured revolver 264.963, mortgage loans 31.200, CLO 38.098, Term Loan B 4.000. Secured credit agreement dates are extended maturities where at the company's option |
| 2029 | 452.580 | US$m | CLO 274.079, secured credit agreement 145.391, mortgage loan 29.110, Term Loan B 4.000 |
| 2030 | 1100.931 | US$m | CLO 1065.806, asset-specific financing 31.125, Term Loan B 4.000 |
| Thereafter | 1488.235 | US$m | CLO 521.050, secured credit agreements 584.185, Term Loan B 383.000. CLO maturities use fully extended collateral maturity, so actual CLO paydown follows loan repayments |

### Reported statements

#### Income statement (USD thousands)

| Line | FY2025 | FY2024 | Q1 2026 | Q2 2026 | Q3 2026 | Q3 2025 | 9M 2026 | 9M 2025 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Interest income | 290237 | 307146 | 74179 | 74053 | 82339 | 77106 | 230571 | 215819 |
| Interest expense | (186460) | (198854) | (48462) | (50387) | (55655) | (48818) | (154504) | (137485) |
| Net interest income | 103777 | 108292 | 25717 | 23666 | 26684 | 28288 | 76067 | 78334 |
| Other income, net | 8079 | 14123 | 3303 | 1261 | 1162 | 1597 | 5726 | 6272 |
| Revenue from real estate owned operations | 34259 | 30700 | 8288 | 9081 | 8078 | 7956 | 25447 | 26466 |
| Total other revenue | 42338 | 44823 | 11591 | 10342 | 9240 | 9553 | 31173 | 32738 |
| Management fee | (20858) | (20249) | (5315) | (5342) | (5326) | (5237) | (15983) | (15584) |
| Expenses from real estate owned operations | (35935) | (35626) | (8269) | (7266) | (8509) | (8293) | (24044) | (28899) |
| Total other expenses | (78517) | (74234) | (18543) | (17212) | (17881) | (18347) | (53636) | (58812) |
| Gain on sale of real estate owned, net | 6970 | none printed | none printed | none printed | none printed | none printed | none printed | 6970 |
| Credit loss (expense) benefit, net | (13871) | (4147) | 286 | (3563) | (8573) | 2608 | (11850) | (2594) |
| Income before income taxes | 60697 | 74734 | 19051 | 13233 | 9470 | 22102 | 41754 | 56636 |
| Income tax expense, net | (378) | (399) | (112) | (101) | (104) | (109) | (317) | (293) |
| Net income | 60319 | 74335 | 18939 | 13132 | 9366 | 21993 | 41437 | 56343 |
| Preferred dividends and participating securities | (14840) | (14669) | (3773) | (3778) | (3546) | (3544) | (11097) | (11053) |
| Net income attributable to common stockholders | 45479 | 59666 | 15166 | 9354 | 5820 | 18449 | 30340 | 45290 |
| Diluted earnings per common share (USD) | 0.57 | 0.75 | 0.19 | 0.12 | 0.08 | 0.23 | 0.39 | 0.56 |

Locators: 10-K page:178-179; 10-Q Q1 page:7-8; 10-Q Q2 page:7-8; 10-Q Q3 page:7-8. FY2024 values are the 10-K comparative. A printed dash is shown as none printed, not as zero.

#### Balance sheet (USD thousands, at date)

| Line | 2024-12-31 | 2025-12-31 | 2026-03-31 | 2026-06-30 | 2026-09-30 |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 190160 | 87613 | 91985 | 65577 | 70826 |
| Restricted cash | 323 | 654 | 472 | 633 | 265 |
| CLO proceeds held at trustee | none printed | 3976 | none printed | 5207 | 11491 |
| Loans held for investment, amortized cost | 3278588 | 4103022 | 4129958 | 4321538 | 4916375 |
| Allowance for credit losses | (61558) | (74503) | (74033) | (77750) | (73955) |
| Loans held for investment, net | 3217030 | 4028519 | 4055925 | 4243788 | 4842420 |
| Real estate owned, net | 256404 | 224386 | 223652 | 224779 | 255213 |
| Total assets | 3731429 | 4406230 | 4472255 | 4596932 | 5242861 |
| Collateralized loan obligations, net | 1681660 | 2579920 | 2534104 | 1905790 | 1907145 |
| Secured financing agreements, net | 670727 | 618470 | 738578 | 1115666 | 1782403 |
| Asset-specific financings, net | 185741 | 59780 | 59727 | 59781 | 30743 |
| Mortgage loans payable, net | 30695 | 30838 | 30874 | 30910 | 59950 |
| Term Loan B, net | none printed | none printed | none printed | 392973 | 393268 |
| Accrued interest payable | 6655 | 6751 | 7102 | 5244 | 6441 |
| Accrued expenses and other liabilities | 15077 | 15884 | 13860 | 16449 | 13692 |
| Payable to affiliates | 5111 | 5274 | 5315 | 5342 | 5326 |
| Deferred revenue | 1744 | 1940 | 1318 | 1363 | 1255 |
| Dividends payable | 19978 | 19350 | 19243 | 18920 | 18512 |
| Total liabilities | 2617388 | 3338207 | 3410121 | 3552438 | 4218735 |
| Total stockholders' equity | 1114041 | 1068023 | 1062134 | 1044494 | 1024126 |

Locators: 10-K page:177-178; 10-Q Q1 page:6-7; 10-Q Q2 page:6-7; 10-Q Q3 page:6-7. Receivables and other assets lines are not shown; accounts receivable from servicer or trustee, accrued interest and fees receivable and other assets complete total assets (Calculations).

#### Cash flow (USD thousands, year to date as reported)

| Line | FY2025 | FY2024 | 3M 2026 | 6M 2026 | 9M 2026 | 9M 2025 |
| --- | --- | --- | --- | --- | --- | --- |
| Net cash provided by operating activities | 90361 | 112131 | 24574 | 46135 | 60528 | 65704 |
| Origination and acquisition of loans | (1764973) | (494995) | (134063) | (583391) | (1266682) | (928227) |
| Advances on loans | (41932) | (40697) | (14460) | (29123) | (100068) | (30191) |
| Principal repayments of loans | 983895 | 887145 | 84386 | 396824 | 510134 | 493308 |
| Net cash used in investing activities | (789708) | 440510 | (66238) | (220658) | (863520) | (428259) |
| Proceeds from CLOs | 1917094 | none printed | none printed | none printed | none printed | 960094 |
| Payments on CLOs | (1006472) | (237502) | (46875) | (675816) | (675816) | (415306) |
| Proceeds from secured financing agreements | 1993614 | 442748 | 267254 | 839576 | 1753258 | 810411 |
| Payments on secured financing agreements | (2042570) | (594381) | (147751) | (341406) | (588850) | (901191) |
| Proceeds from Term Loan B | none printed | none printed | none printed | 399000 | 399000 | none printed |
| Dividends paid on common stock | (78496) | (77849) | (19350) | (38589) | (57509) | (59377) |
| Dividends paid on preferred stock | (12592) | (12588) | (3144) | (6296) | (9440) | (9440) |
| Payments to retire common stock | (25349) | (37) | (4197) | (15082) | (24613) | (24962) |
| Net cash provided by (used in) financing activities | 597131 | (569176) | 45854 | 152466 | 785816 | 266531 |
| Net change in cash, equivalents and restricted cash | (102216) | (16535) | 4190 | (22057) | (17176) | (96024) |
| Interest paid | 179722 | 194437 | 46301 | 96092 | 148023 | 133499 |
| Taxes paid | 290 | 260 | 287 | 366 | 369 | 271 |

Locators: 10-K page:180-181; 10-Q Q1 page:8-9; 10-Q Q2 page:9-10; 10-Q Q3 page:9-10. Cash flows are year to date only; discrete Q2 and Q3 amounts are derived in Calculations.

### Funding structure and recourse

The table sets out every borrowing instrument at 2026-09-30 as the Q3 10-Q prints it (page:46-58, page:77-78, page:89-91).

| Instrument | Borrower or issuer perimeter | Principal (USD thousands) | Carrying value | Pricing | Maturity | Recourse to TRTX or Holdco | Margin calls |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TRTX 2025-FL6 CRE CLO | Consolidated VIE issuer; Sub-REIT | 962500 | 956171 | Term SOFR, weighted spread 1.83% | Rated final distribution about 15.9 years; reinvestment 30 months from 2025-03-28 | Non-recourse; liabilities satisfied only from VIE assets | None |
| TRTX 2025-FL7 CRE CLO | Consolidated VIE issuer; Sub-REIT | 957000 | 950974 | Term SOFR, weighted spread 1.67% | About 16.7 years; reinvestment 30 months from 2025-11-17 | Non-recourse | None |
| Secured credit agreements (Goldman Sachs, Wells Fargo, Citi, Bank of America) | Special purpose subsidiaries; Holdco guarantee | 1522156 | 1519157 | Term SOFR plus weighted spread 1.61% | Extended maturities from 2028-05-12 to 2031-11-17 | 25% recourse to Holdco, capped but with bad-boy carve-outs | Credit marks only; no margin calls on the Wells Fargo agreement for one year from 2026-05-12 (page:48) |
| Secured revolving credit facility (375.0 million commitment, seven lenders) | Company and Holdco | 264963 | 263246 | Term SOFR plus 2.00% | 2028-02-13 | 100% recourse to Holdco | None |
| Asset-specific financing: HSBC | Single-asset financing | 31125 | 30743 | Term SOFR plus about 1.9% | Matched to collateral, about 3.9 years | 20% recourse | None |
| Asset-specific financing: BMO (200.0 million commitment) | Single-asset financing | none printed (undrawn) | none printed | not applicable | not applicable | 25% recourse | None |
| Mortgage loans payable (two REO loans) | Special purpose subsidiaries | 60310 | 59950 | 31.2 million fixed 7.7%; 29.1 million Term SOFR plus 2.0% | 2028-07-06 and 2029-08-15 | First is non-recourse; second has a 25% recourse guarantee | None |
| Term Loan B | Company, guaranteed by certain subsidiaries; first-priority lien on substantially all assets of the Company and certain subsidiaries | 400000 | 393268 | Term SOFR plus 2.75%; issued at 99.75 | May 2033; 0.25% quarterly amortization from December 2026 | 100% | None |
| Revolver (100.0 million) | Company and Holdco | none printed (undrawn) | not applicable | Term SOFR plus 2.00%; unused fee 15 or 25 basis points | May 2031 | 100% | None |

Sources: CLO table 10-Q Q3 page:45; secured credit agreements page:47-48 and page:89-91; secured revolver page:52; asset-specific page:53; mortgage loans page:54; Term Loan B page:56; Revolver page:57; recourse percentages page:89. Principal total 4,198,054 thousand (page:89). Non-mark-to-market borrowings were 78.8% of total (page:89).

The recourse layer matters more than any single ratio. Applying the printed recourse percentages to principal gives nominal recourse exposure of 1,051,727 thousand at 2026-09-30 (Calculations), made up of 664,963 thousand of fully recourse debt and 386,764 thousand of partial recourse. Five percent of that, 52,586 thousand, is consistent with the 52.6 million of cash the company reports holding for the liquidity covenant (page:28). The same test is consistent with the 39.5 million held at 2026-06-30 (release 2026-07-28 page:3) and gives a requirement below the 15.0 million floor at 2025-12-31 (page:28) and 2026-03-31 (release 2026-04-28 page:3), when 15.0 million was held. This suggests the company holds cash at the covenant minimum and that required cash rises with each draw on recourse debt. The filing does not define "recourse indebtedness" and the match holds only on the basis chosen in Calculations, so it is an inference.

### Liquidity

Near-term liquidity at 2026-09-30 is 291,634 thousand as the issuer defines it (page:105). It excludes contractual availability that depends on lender-approved collateral. Three points qualify the headline. First, 52.6 million of the 70,826 thousand cash is held for liquidity covenants (page:28), leaving 18.2 million available for investment (page:77). Second, the 87,317 thousand of secured credit agreement capacity is defined as available without pledging additional collateral (page:77), while maximum current availability is 777,844 thousand (page:47). Third, the 22,000 thousand secured revolver figure compares with an undrawn commitment of 110.0 million (375.0 million less 265.0 million drawn, page:77); collateral eligibility limits the difference. Against these, the company has unfunded loan commitments of 236,552 thousand (page:71), of which 26,740 thousand fall due within a year (page:108), and unencumbered loans of 187.2 million that can be pledged (page:106). Contractual obligations due in less than one year are 3,000 thousand of Term Loan B principal and 26,740 thousand of unfunded commitments, plus estimated interest, for a printed total of 272,285 thousand (page:108). The secured credit agreement and secured revolver maturities used in the schedule fall in 2028 or later (page:57), so no facility is shown expiring within twelve months of the as-of date.

### Covenants

The Q3 10-Q prints levels for the following tests (page:54-57):

| Covenant (borrower) | Level | Previous level | Reported figure | Headroom |
| --- | --- | --- | --- | --- |
| Cash liquidity (investment-portfolio facilities, Holdco; corporate facilities, Company and Holdco) | Greater of 15.0 million and 5.0% of recourse indebtedness | Same | Cash held for the covenant 52.6 million (page:28) | Not supplied: recourse indebtedness as defined is not printed; see inference above |
| Tangible net worth (investment-portfolio facilities) | 1.0 billion plus 75% of subsequent equity issuances less 75% of redeemed or repurchased preferred or redeemable equity or stock; 0.8 billion for the secured revolver | Same | Not supplied | Not calculable: the adjustments are not printed; unadjusted stockholders' equity is 1,024,126 thousand against the 1.0 billion base |
| Debt-to-equity (investment-portfolio facilities) | Not applicable now | 4.25 to 1.0 | Issuer total leverage ratio 4.03x is not the covenant measure | Not applicable |
| Total debt to total assets | Maximum 83.333% (Holdco and subsidiaries for investment-portfolio facilities; Company and subsidiaries for corporate facilities; includes Term Loan B and Revolver) | Not applicable | Not supplied | Not calculable as defined; indicative ratio in Calculations |
| Interest coverage | Minimum 1.3 to 1.0 | 1.4 to 1.0 | Not supplied | Not calculable: the definition is not printed |

Definitions that differ from the metrics computed in this handoff: the covenant total debt may use credit-agreement definitions of debt and assets that differ from consolidated GAAP principal and total assets; the interest coverage covenant's definition and numerator are not printed; the issuer's printed debt-to-equity and total leverage ratios use principal less cash over total equity (page:104-105). The company states compliance with all financial covenants for its financing arrangements to the extent of outstanding balances (page:55, page:57). The change that took effect when the Term Loan B and Revolver closed (page:55) replaced a 4.25x debt-to-equity limit with an 83.333% debt-to-assets limit; the issuer's total leverage ratio of 4.03x is below the former 4.25x limit, but the covenant definition is not supplied, so no inference about the reason for the change is drawn.

### Earnings measures and definitions

Distributable Earnings is an issuer non-GAAP measure: GAAP net income attributable to common stockholders, adding back non-cash stock compensation, depreciation and amortization on REO and credit loss expense, then deducting realized losses from loan write-offs (release 2026-10-26 page:7-8; 10-Q Q3 page:80-81). Q3 2026 adds back 1,254 thousand, 2,477 thousand and 8,573 thousand to net income attributable to common stockholders of 5,820 thousand to reach 18,124 thousand before a 13,006 thousand realized loss, giving 5,118 thousand. The realized loss is the write-off on the Plano multifamily loan converted to REO on 2026-09-01 (page:39). Book value per common share was 10.85 at 2026-09-30 against 11.07 at 2025-12-31 (page:81). Dividends declared were 0.24 per common share in each quarter of 2026: 19,239, 18,920 and 18,508 thousand (page:8-9).

### Credit quality of the loan book

Total loan commitments were 5,168,717 thousand and unpaid principal balance 4,934,450 thousand at 2026-09-30, against 4,290,603 and 4,118,050 thousand at 2025-12-31 (page:31, page:72). Risk ratings by amortized cost: rated 2 is 173,354 thousand, rated 3 is 4,622,896 thousand and rated 4 is 120,125 thousand, with none rated 1 or 5 (page:34). The two rated 4 loans are the mixed-use loan (76,548 thousand) and a Honolulu office loan (43.6 million) (page:86, page:118). The allowance for credit losses was 76,143 thousand including 2,188 thousand on unfunded commitments, or 147 basis points of commitments, all general reserve with no specific reserve (page:35, page:88). Seven REO properties are held, with an aggregate carrying value of 266.7 million (page:82); two are financed (page:106). The portfolio's weighted average loan-to-value is 65.9%, calculated at origination or acquisition on the as-is appraised value at that time, not marked to current value (page:118-119). The loan modification disclosed was a multifamily extension to 2027-07-09 with a lower spread on 33.1 million (page:38).

### Latest quarter and subsequent events

Q3 2026 activity (page:77): originations and one acquisition of 772.7 million commitments at a weighted spread of Term SOFR plus 3.02%; fundings of 71.8 million under existing loans; repayments of 119.6 million; one foreclosure with a 13,006 thousand realized loss; repurchase of 1,163,018 shares for 9,332 thousand (page:8). Subsequent events to the 10-Q (page:74): repayments of 72.2 million including one loan of 61.5 million; TRTX 2026-FL8, a 1.0 billion managed CRE CLO closed on 2026-10-02 with about 820.0 million of investment grade notes placed; and a new 50.0 million share repurchase program approved on 2026-10-26. The new CLO would add non-recourse debt and is not in the 2026-09-30 balance sheet; its use of proceeds, any redemption of other debt and any retained interests are not supplied. A dividend of 0.24 per share was declared on 2026-09-17 and paid on 2026-10-23 (release 2026-10-26 page:2).

### Consistency with the earlier handoff

This handoff builds on the CP-0 handoff and refines it in two small respects. CP-0 named the 25% recourse of the BMO facility and the secured credit agreements but not the other recourse terms; this handoff adds that the HSBC facility is 20% recourse and the secured revolver and Term Loan B are 100% recourse (10-Q Q3 page:52-53, page:89). CP-0's book value per share tie-out deducted only the Series C liquidation preference; the filing also deducts the 125 thousand Series A preference, giving 822,751 thousand of common equity and the same 10.85 (page:81). No CP-0 conclusion changes.

## Calculations

All figures are in USD thousands unless stated. Inputs carry their locators; every result was recomputed from the cited figures.

### LTM to 2026-09-30 (FY2025 + 9M 2026 - 9M 2025)

| Item | FY2025 | 9M 2026 | 9M 2025 | LTM |
| --- | --- | --- | --- | --- |
| Interest income | 290237 | 230571 | 215819 | 304989 |
| Interest expense | 186460 | 154504 | 137485 | 203479 |
| Net interest income | 103777 | 76067 | 78334 | 101510 |
| Revenue from real estate owned operations | 34259 | 25447 | 26466 | 33240 |
| Credit loss expense, net | 13871 | 11850 | 2594 | 23127 |
| Net income | 60319 | 41437 | 56343 | 45413 |
| Net income attributable to common | 45479 | 30340 | 45290 | 30529 |
| Interest paid | 179722 | 148023 | 133499 | 194246 |
| Net cash from operating activities | 90361 | 60528 | 65704 | 85185 |

Net interest income LTM: 304,989 - 203,479 = 101,510, equal to 103,777 + 76,067 - 78,334. LTM Distributable Earnings: Q4 2025 18,463 (10-K page:124) + Q1 19,513 + Q2 17,619 + Q3 5,118 = 60,713; before realized losses 18,463 + 19,513 + 17,619 + 18,124 = 73,719. The 9M 2025 Distributable Earnings is not printed in the pack; FY2025 76,778 less Q4 2025 18,463 would give 58,315 but is not used as a table value.

### Discrete quarters from year-to-date cash flows

| Item | Calculation | Result |
| --- | --- | --- |
| Operating cash flow Q2 2026 | 46,135 - 24,574 (10-Q Q2 page:9; Q1 page:9) | 21,561 |
| Operating cash flow Q3 2026 | 60,528 - 46,135 (10-Q Q3 page:10) | 14,393 |
| Interest paid Q2 2026 | 96,092 - 46,301 | 49,791 |
| Interest paid Q3 2026 | 148,023 - 96,092 | 51,931 |

### Cover and leverage measures (non-EBITDA)

| Measure | Inputs | Result |
| --- | --- | --- |
| Interest income to interest expense, Q3 2026 | 82,339 / 55,655 | 1.48x |
| Interest income to interest expense, 9M 2026 | 230,571 / 154,504 | 1.49x |
| Interest income to interest expense, LTM | 304,989 / 203,479 | 1.50x |
| Interest income to interest expense, FY2025 and 9M 2025 | 290,237 / 186,460 and 215,819 / 137,485 | 1.56x and 1.57x |
| Interest income to interest expense, Q1 and Q2 2026 | 74,179 / 48,462 and 74,053 / 50,387 | 1.53x and 1.47x |
| Operating cash flow before interest paid to interest paid, LTM | (85,185 + 194,246) / 194,246 | 1.44x |
| Operating cash flow before interest paid to interest paid, 9M 2026 | (60,528 + 148,023) / 148,023 | 1.41x |
| Net debt (principal less cash) at 2026-09-30 | 4,198,054 - 70,826 | 4,127,228 |
| Net debt over equity at 2026-09-30 | 4,127,228 / 1,024,126 | 4.03x, equal to printed total leverage ratio |
| Printed debt-to-equity ratio reproduced | (1,919,500 + 1,522,156 + 264,963 + 31,125 + 60,310 - 70,826) / 1,024,126 = 3,727,228 / 1,024,126 | 3.64x, equal to printed |
| Net debt over equity at 2026-06-30 | (3,531,816 - 65,577) / 1,044,494 | 3.32x, equal to printed |
| Net debt over equity at 2026-03-31 | (3,382,090 - 91,985) / 1,062,134 | 3.10x, equal to printed |
| Net debt over equity at 2025-12-31 | (3,309,462 - 87,613) / 1,068,023 | 3.02x, equal to printed |
| Debt principal growth since 2025-12-31 | 4,198,054 - 3,309,462 | 888,592 (26.9%) |
| Equity change since 2025-12-31 | 1,024,126 - 1,068,023 | -43,897 (-4.1%) |
| Indicative debt principal over total assets, 2026-09-30 | 4,198,054 / 5,242,861 | 80.07% against a 83.333% maximum; not the covenant measure because the credit-agreement definitions are not supplied. Indicative cushion 83.333% less 80.07% is about 3.3 percentage points; the GAAP total liabilities over total assets is 4,218,735 / 5,242,861 = 80.47% |
| Same ratio at earlier dates | 3,309,462 / 4,406,230; 3,382,090 / 4,472,255; 3,531,816 / 4,596,932 | 75.11%; 75.62%; 76.83% |

### Recourse and the cash covenant

| Component at 2026-09-30 | Calculation | Result |
| --- | --- | --- |
| Fully recourse debt | Secured revolver 264,963 + Term Loan B 400,000 + Revolver 0 | 664,963 |
| Secured credit agreements at 25% | 0.25 x 1,522,156 | 380,539 |
| HSBC facility at 20% | 0.20 x 31,125 | 6,225 |
| Nominal recourse exposure | 664,963 + 380,539 + 6,225 | 1,051,727 |
| 5.0% of that exposure | 0.05 x 1,051,727 | 52,586, consistent with 52.6 million held (10-Q Q3 page:28) |
| Same test at 2026-06-30 | 0.05 x (0.25 x 991,978 + 128,903 + 0.20 x 31,125 + 0.25 x 29,110 + 400,000) = 0.05 x 790,400 | 39,520, consistent with 39.5 million held (release 2026-07-28 page:3) |
| Same test at 2025-12-31 | 0.05 x (0.25 x 591,245 + 31,466 + 0.20 x 31,125 + 0.25 x 29,110) = 0.05 x 192,780 | 9,639, below the 15,000 floor, consistent with 15.0 million held (10-Q Q3 page:28) |
| Same test at 2026-03-31 | 0.05 x (0.25 x 742,214 + 0.20 x 31,125 + 0.25 x 29,110) = 0.05 x 199,056 | 9,953, below the floor, consistent with 15.0 million held (release 2026-04-28 page:3) |

The test excludes the 25% guarantee on the 29,110 thousand mortgage loan created in September 2026. Including it (0.25 x 29,110 = 7,278) would raise the 2026-09-30 exposure to 1,059,005 and 5% of it to 52,950, which rounds to 53.0 million rather than 52.6 million. The match therefore holds only on the basis used above, and the filing does not say which basis the covenant uses. It is an inference, not a company statement.

### Liquidity and maturities

| Item | Calculation | Result |
| --- | --- | --- |
| Near-term liquidity table adds, 2026-09-30 | 70,826 + 87,317 + 22,000 + 0 + 11,491 + 100,000 | 291,634, equal to printed |
| Near-term liquidity, 2026-06-30 | 65,577 + 297,397 + 20,000 + 0 + 5,207 + 100,000 | 488,181, equal to printed |
| Near-term liquidity, 2026-03-31 | 91,985 + 39,694 + 41,170 | 172,849, equal to printed |
| Near-term liquidity, 2025-12-31 | 87,613 + 21,433 + 30,000 + 3,976 | 143,022, equal to printed |
| Cash available for investment | 70.8 - 52.6 | 18.2 million, equal to printed |
| Liquidity less covenant cash | 291.634 - 52.6 | 239.0 million, approximate because 52.6 is rounded |
| Liquidity over unfunded commitments | 291,634 / 236,552 | 1.23x |
| Maximum current availability, secured credit agreements | 2,300,000 - 1,522,156 | 777,844, equal to printed (page:47) |
| Maturity schedule adds | 1,000 + 24,467 + 1,130,841 + 452,580 + 1,100,931 + 1,488,235 | 4,198,054, equal to printed and to the instrument sum |
| 2028 maturities | 38,098 + 792,580 + 264,963 + 31,200 + 4,000 | 1,130,841, equal to printed |
| 2026 to 2028 share of principal | (1,000 + 24,467 + 1,130,841) / 4,198,054 | 27.5%; 2028 alone 26.9% |
| Share of debt in CLOs | 1,919,500 / 4,198,054 and 2,595,316 / 3,309,462 | 45.7%, equal to printed, against 78.4% at 2025-12-31 |
| Non-mark-to-market share | 3,309,648 / 4,198,054 | 78.8%, equal to printed |
| Marked share | 888,406 / 4,198,054 | 21.2%, equal to printed |

### Earnings and credit tie-outs

| Item | Calculation | Result |
| --- | --- | --- |
| Net interest income Q3 2026 | 82,339 - 55,655 | 26,684, equal to printed |
| Quarterly sums to nine months (net income) | 18,939 + 13,132 + 9,366 | 41,437, equal to printed |
| Quarterly sums to nine months (credit loss) | 286 - 3,563 - 8,573 | -11,850, equal to printed |
| Quarterly sums to nine months (interest income) | 74,179 + 74,053 + 82,339 | 230,571, equal to printed |
| Q3 2026 pre-tax income | 26,684 + 9,240 - 17,881 - 8,573 | 9,470, equal to printed |
| Distributable earnings reconciliation Q3 2026 | 5,820 + 1,254 + 2,477 + 8,573 - 13,006 | 5,118, equal to printed |
| 9M 2026 Distributable earnings | 19,513 + 17,619 + 5,118 | 42,250; before realized losses 19,513 + 17,619 + 18,124 = 55,256 |
| Common dividends declared 9M 2026 | 19,239 + 18,920 + 18,508 | 56,667 (56.7 million printed) |
| Cover of declared common dividends | 55,256 / 56,667 and 42,250 / 56,667 | 0.98x before and 0.75x after realized losses |
| Q3 2026 dividend cover | 18,124 / 18,508 and 5,118 / 18,508 | 0.98x before and 0.28x after realized losses |
| Total allowance | 73,955 + 2,188 | 76,143, equal to printed; 76,143 / 5,168,717 = 147 basis points |
| Rated 4 loans | 76.5 million mixed-use loan (loan 24) + 43.6 million Honolulu office loan (loan 49), page:118 | 120.1 million, consistent with the printed 120,125 thousand; 120,125 / 4,916,375 = 2.4% of amortized cost |
| Office share of commitments | 195,360 / 4,508,434 and 407,360 / 5,168,717 | 4.3% and 7.9%, equal to printed; the increase 407,360 - 195,360 = 212,000 equals the San Francisco loan commitment of 212.0 million |
| REO aggregate carrying value | 255,213 + 8,913 + 1,368 + 2,536 - 1,345 | 266,685, consistent with 266.7 million (page:40, page:82) |
| Book value per common share | (1,024,126 - 201,250 - 125) / 75,826.954 | 10.85, equal to printed |
| Balance sheet foots, 2026-09-30 | 6,441 + 13,692 + 1,907,145 + 1,782,403 + 30,743 + 59,950 + 393,268 + 5,326 + 1,255 + 18,512 | 4,218,735, equal to printed; plus 1,024,126 equals 5,242,861 |
| Balance sheet foots, other dates | Liabilities listed in the table for 2025-12-31, 2026-03-31 and 2026-06-30 | 3,338,207; 3,410,121; 3,552,438, equal to printed |
| Assets foot, 2026-09-30 | 70,826 + 265 + 11,491 + 2,275 + 31,149 + 4,842,420 + 255,213 + 29,222 | 5,242,861, equal to printed |
| Secured financing carrying value | 1,519,157 + 263,246 | 1,782,403, equal to the balance sheet line |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No EBITDA in any supplied source; EBITDA leverage and EBITDA cover are Not supplied | High for the chart selectors; Low for credit view | CP-2, CP-5 | Use debt-to-equity, debt over assets and interest income cover; do not impute an EBITDA |
| Covenant test values and definitions (tangible net worth, total debt to total assets, interest coverage, recourse indebtedness) not printed | High for headroom | CP-2 | Obtain compliance certificates or the credit agreements; treat the indicative ratios here as unverified |
| Executed Term Loan B and Revolver agreements and secured credit agreements not supplied; guarantor list for the Term Loan B not named | Medium | CP-1A, CP-2 | Obtain the 2026-05-14 credit agreement and subsidiary guarantor list |
| Discrete-quarter cash flows not printed; derived Q2 and Q3 amounts depend on year-to-date columns | Low | CP-2 | Use derived amounts with the label |
| Distributable Earnings for 9M 2025 not printed in the pack; comparatives to prior year limited to Q3 2025 and Q4 2025 | Low | CP-2 | Obtain the Q1 and Q2 2025 releases if needed |
| Use of proceeds and effects of the 2026-10-02 CLO (TRTX 2026-FL8) and any debt redeemed are not supplied; the 2026-09-30 balance sheet excludes it | Medium | CP-1A, CP-2 | Obtain the 8-K of 2026-10-06 and the Q4 2026 filing |
| Nothing dated after 2026-10-26 up to 2026-11-05 supplied | Medium | CP-1A, CP-2 | Treat as Not supplied |
| Rating agency, market price and peer data not supplied; context empty | Medium for relative value | CP-2 | Not needed for this module |
| Undrawn committed facilities in the liquidity chart follow the issuer's availability definition, not commitment less drawn | Medium | CP-2 | Read with contractual availability of 777.844 million under the secured credit agreements |
| Unreconciled reading of the Q1 2026 release statement that office exposure was below 5% against 7.9% at 2026-09-30 | Low | CP-5 | Treat as a point-in-time management claim, superseded by the filed 10-Q table |

## Next module

- CP-1A: carry the external manager relationship with TPG, the one-segment business, the Term Loan B and Revolver of May 2026, the redemption of TRTX 2022-FL5 on 2026-05-15, the 2026-10-02 TRTX 2026-FL8 closing and the 2026-10-26 repurchase program. Label anything after 2026-10-26 as Not supplied.
- CP-2: use debt-to-equity and total leverage as the leverage measures, the recourse layering, the cash covenant inference, the 2028 maturity cluster and liquidity net of covenant cash. Carry the missing covenant values and the absent EBITDA as restrictions; do not equate undrawn commitments with usable liquidity.
- CP-5: trace every figure to the `page:N` locators above; the LTM, discrete-quarter, recourse and ratio figures are derived and appear only in Calculations.
