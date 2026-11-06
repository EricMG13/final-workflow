## Request

Issuer: Wayfair Inc. (issuer id w; NYSE ticker W). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, stated in millions in every source. Current period: Q3 2026 (quarter ended 2026-09-30). Prior period named by the context: FY2025.

Question for this module: build the reported financial base for Wayfair Inc. to Q3 2026, with the debt schedule, liquidity, cash flow, leverage and coverage views that the later modules consume, and state which requirements the evidence supports. Perimeter: Wayfair Inc. and its wholly-owned subsidiaries, consolidated (Q3 10-Q page:6); there is no subsidiary-issuer or guarantor-group financial statement in the pack. Basis: US GAAP, with the company's non-GAAP measures labelled as management measures.

Short labels used for locators: 10-K is the FY2025 annual report; Q1 10-Q, Q2 10-Q and Q3 10-Q are the quarterly reports for 2026; Q1 rel, Q2 rel and Q3 rel are the three Exhibit 99.1 earnings releases. A locator `page:N` is the extraction chunk, not the printed page. The context file is not issuer evidence; its blank fields are Not supplied, never zero.

## Sources

### Issuer sources relied on

| Source name | sha256 | Short label | Entity, period and kind |
| --- | --- | --- | --- |
| 10-K_2025-12-31_w-20251231.htm.jsonl | 8ef4121e11689a0c5565962f85cfafc125f39e54e08df2c3b6c79eaf68e84e4d | 10-K | Wayfair Inc. consolidated; FY2025, FY2024 and FY2023; audited statements and notes; controlling for annual facts |
| 10-Q_2026-03-31_w-20260331.htm.jsonl | 79f74f0ba7972d92f75742a90568a879936b4ecf939af4026c967768203f5019 | Q1 10-Q | Same entity; quarter ended 2026-03-31; unaudited condensed |
| 10-Q_2026-06-30_w-20260630.htm.jsonl | e52476a4ad53b4396b19ba631702cd30b522eb54aecabc978fa654467e46935a | Q2 10-Q | Same entity; quarter and six months ended 2026-06-30; unaudited condensed |
| 10-Q_2026-09-30_w-20260930.htm.jsonl | 9224a05a14ec554aa7f19d7d2ae6869a07a996f1d60af972e32e1595aefdd8c3 | Q3 10-Q | Same entity; quarter and nine months ended 2026-09-30; unaudited condensed; controlling for 2026-09-30 facts |
| EX-99.1_2026-04-30_a2026-04x30ex991.htm.jsonl | a3debc23ce5c3027daa8862793a0e092539f933475881f34dd98f47a74a5cd40 | Q1 rel | Management earnings release for Q1 2026; supporting claims; repeats 10-Q statements |
| EX-99.1_2026-08-04_a2026-08x04ex991.htm.jsonl | bd4c1a88b49b8e4441931ccafc159f4e1f6d02b8d8bf7918ce20a28d44352f87 | Q2 rel | Management earnings release for Q2 2026; supporting claims |
| EX-99.1_2026-11-04_a2026-11x04ex991.htm.jsonl | 2907d0c055207f89b1a08967b4ff5b2fe5bb05c815f0f3ad4e1479f1b9a353cb | Q3 rel | Management earnings release for Q3 2026; supporting claims; source of the segment Adjusted EBITDA table |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | e3b6fe003758c2152693bc3785d916a8d51266f353efa91b71daa0110cb48520 | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | Use in this module |
| --- | --- | --- |
| CP-0 | 9ba2d9c1e2e60174eaacd93db71cc6938042323a45533114c80ae7273f5486a5 | Source readiness: all four consumers READY_WITH_LIMITATIONS; carried limits are no executed legal documents, no reported covenant ratio, unnamed guarantors, no Q4 2025 stand-alone quarter, and no ratings or market data |

The CP-0 handoff said not to build covenant headroom from Adjusted EBITDA. This module follows that: it shows one indicative secured-debt ratio, labelled as not a covenant test, and no headroom.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported figures support a complete financial base to the third quarter of 2026. On company-defined earnings, total debt is 3.28x and net debt 1.99x, with interest cover of 5.02x. Earnings quality and covenant headroom carry limits. | Medium | Earnings are company-adjusted and add back equity compensation; covenant definitions and market data are not supplied, so headroom and relative value cannot be measured. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Last-twelve-month Adjusted EBITDA is 853 million against 453 million in FY2024, while total debt fell from 3,118 million to 2,799 million. | Total debt to Adjusted EBITDA improved from 6.88x to 3.28x, driven more by earnings growth than by debt reduction. | High |
| Adjusted EBITDA adds back 293 million of equity compensation and related taxes in the last twelve months; operating income plus depreciation and amortization is 549 million. | On that unadjusted measure total debt is 5.10x, so leverage is sensitive to whether equity pay is treated as a cost. | Medium |
| Cash is 1,038 million and the undrawn revolver is 418 million after letters of credit, against 229 million of convertible notes due in 2027. | Cash exceeds the 2027 notes, but conversion settlement terms leave the cash need open. | Medium |
| Last-twelve-month free cash flow is 476 million, but 77 million of share-settlement tax and 60 million of buybacks sit in financing in nine months 2026. | Cash after dilution management is lower than free cash flow, and nine-month operating cash flow benefited from a working-capital inflow. | Medium |
| Interest cover is 5.02x on last-twelve-month cash interest, but stated coupons on debt outstanding at 30 September 2026 total about 195 million a year. | Cover on run-rate coupons is lower at 4.36x; the 2034 notes replaced lower-coupon convertibles, so cash interest is rising. | Medium |

### Financial base view

The reported base is complete for the requested use: audited FY2024 and FY2025 annual statements, three quarterly reports and three releases give statements of operations, balance sheets and cash flows for every period needed, in one currency, one perimeter and one accounting basis, with prior-year comparatives. On the company's own Adjusted EBITDA, last-twelve-month earnings to Q3 2026 are 853 million, up from 743 million in FY2025 and 453 million in FY2024, and total debt at carrying amount fell from 3,272 million at 2025-12-31 to 2,799 million at 2026-09-30. That moves total debt to Adjusted EBITDA from 4.40x to 3.28x and net debt to Adjusted EBITDA from 2.33x to 1.99x; the improvement since FY2024 is mainly earnings growth, since debt fell by 10.2% while Adjusted EBITDA rose by 88.3%. Cash and short-term investments are 1,098 million, the revolver is undrawn, and the capital structure is now all fixed-rate: 2,600 million of senior secured notes and 229 million of 2027 convertible notes, with no maturity before 2027.

Three qualifications bound the view. First, Adjusted EBITDA is a management measure that adds back equity compensation and related taxes (293 million over the last twelve months, 34.3% of the 853 million); on operating income plus depreciation and amortization, total debt is 5.10x. Second, net debt and free cash flow flatter cash available after dilution management: 77 million of tax on net share settlement and 60 million of buybacks sit in financing in nine months 2026, and nine-month operating cash flow includes a working-capital inflow of 64 million against an outflow of 76 million a year earlier. Third, the 2027 convertible notes are convertible in the quarter ending 2026-12-31 and were worth 141 million more on an if-converted basis than their principal, so settlement terms can add to the cash need. Covenant levels, guarantor lists and executed documents are not supplied, so no covenant headroom is shown.

### Source context

| Source | Entity and perimeter | Period | Statement kind | Unit and currency | Version relationship | Supports extraction |
| --- | --- | --- | --- | --- | --- | --- |
| 10-K | Wayfair Inc. and its wholly-owned subsidiaries, consolidated | FY2025, FY2024, FY2023; balance sheets 2025-12-31 and 2024-12-31 | Audited annual statements and notes (page:99-101, page:118-133); PwC opinion on FY2025 (page:96-98), Ernst & Young on earlier years (page:99) | USD millions | Original annual report; Q3 10-Q defers to it for policies (page:6) | Yes |
| Q1 10-Q | Same | Quarter ended 2026-03-31 with prior-year comparative | Unaudited condensed statements (page:2-5), debt note (page:9) | USD millions | Superseded by later quarters for balance sheet facts | Yes |
| Q2 10-Q | Same | Quarter and six months ended 2026-06-30 | Unaudited condensed (page:2-4), debt note (page:10-12) | USD millions | Superseded by Q3 10-Q for balance sheet facts | Yes |
| Q3 10-Q | Same | Quarter and nine months ended 2026-09-30; balance sheets 2026-09-30 and 2025-12-31 | Unaudited condensed (page:2-5), notes (page:6-25), MD&A and non-GAAP reconciliations (page:26-52) | USD millions | Latest filed report; controlling for current-period facts | Yes |
| Q1 rel, Q2 rel, Q3 rel | Same | Q1, Q2 and Q3 2026 | Release tables repeating 10-Q statements, plus segment Adjusted EBITDA and non-GAAP reconciliations (Q3 rel page:11-12) | USD millions | Management claims; the 10-Q controls where both print a figure | Yes; text only |

### Reported statements of operations

| Line (USD m) | FY2024 | FY2025 | 9M 2025 | 9M 2026 | Q3 2025 | Q3 2026 | Locators |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net revenue | 11,851 | 12,457 | 9,120 | 9,870 | 3,117 | 3,420 | 10-K page:100; Q3 10-Q page:3 |
| Cost of goods sold | 8,277 | 8,692 | 6,365 | 6,924 | 2,183 | 2,408 | 10-K page:100; Q3 10-Q page:3 |
| Gross profit | 3,574 | 3,765 | 2,755 | 2,946 | 934 | 1,012 | 10-K page:100; Q3 10-Q page:3 |
| Customer service and merchant fees | 470 | 471 | 346 | 369 | 118 | 127 | 10-K page:100; Q3 10-Q page:3 |
| Advertising | 1,472 | 1,425 | 1,046 | 1,059 | 330 | 338 | 10-K page:100; Q3 10-Q page:3 |
| Selling, operations, technology, general and administrative | 1,977 | 1,776 | 1,339 | 1,293 | 445 | 441 | 10-K page:100; Q3 10-Q page:3 |
| Impairment and other related net charges | 37 | 23 | 23 | 2 | Nil printed (dash) | Nil printed (dash) | 10-K page:100; Q3 10-Q page:3 |
| Restructuring and other charges, net | 79 | 53 | 68 | 24 | 3 | Nil printed (dash) | 10-K page:100; Q3 10-Q page:3 |
| Total operating expenses | 4,035 | 3,748 | 2,822 | 2,747 | 896 | 906 | 10-K page:100; Q3 10-Q page:3 |
| Income (loss) from operations | (461) | 17 | (67) | 199 | 38 | 106 | 10-K page:100; Q3 10-Q page:3 |
| Interest expense, net | (29) | (119) | (83) | (120) | (31) | (42) | 10-K page:100; Q3 10-Q page:3 |
| Other income (expense), net | (21) | 31 | 28 | (14) | (5) | 1 | 10-K page:100; Q3 10-Q page:3 |
| Gain (loss) on debt extinguishment, net | 29 | (233) | (68) | (102) | (99) | Nil printed (dash) | 10-K page:100; Q3 10-Q page:3 |
| Income (loss) before income taxes | (482) | (304) | (190) | (37) | (97) | 65 | 10-K page:100; Q3 10-Q page:3 |
| Provision for income taxes, net | 10 | 9 | 7 | 7 | 2 | 3 | 10-K page:100; Q3 10-Q page:3 |
| Net income (loss) | (492) | (313) | (197) | (44) | (99) | 62 | 10-K page:100; Q3 10-Q page:3 |

Discrete quarters (net revenue, gross profit, operating income, net income, Adjusted EBITDA, operating cash flow, free cash flow), USD m. Q1 to Q3 are printed; Q4 2025 is derived as FY2025 less nine months 2025 and is labelled as derived.

| Quarter | Net revenue | Gross profit | Income (loss) from operations | Net income (loss) | Adjusted EBITDA | Operating cash flow | Free cash flow | Locators |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q1 2025 | 2,730 | 837 | (122) | (113) | 106 | (96) | (139) | Q1 rel page:2 |
| Q2 2025 | 3,273 | 984 | 17 | 15 | 205 | 273 | 230 | Q2 rel page:2 |
| Q3 2025 | 3,117 | 934 | 38 | (99) | 208 | 155 | 93 | Q3 rel page:2 |
| Q4 2025 (derived) | 3,337 | 1,010 | 84 | (116) | 224 | 202 | 145 | Calculations |
| Q1 2026 | 2,931 | 880 | (11) | (105) | 151 | (52) | (106) | Q1 rel page:2 |
| Q2 2026 | 3,519 | 1,054 | 104 | (1) | 242 | 360 | 301 | Q2 rel page:2 |
| Q3 2026 | 3,420 | 1,012 | 106 | 62 | 236 | 198 | 136 | Q3 rel page:2 |

Operating cash flow is negative in both first quarters printed (Q1 2025 and Q1 2026) and positive in the other quarters printed, so any single-quarter cash figure must be read against that pattern.

### Reported balance sheets

| Line (USD m) | 2024-12-31 | 2025-12-31 | 2026-03-31 | 2026-06-30 | 2026-09-30 | Locators |
| --- | --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 1,316 | 1,476 | 1,004 | 1,065 | 1,038 | 10-K page:99; Q1 10-Q page:2; Q2 10-Q page:2; Q3 10-Q page:2 |
| Short-term investments | 56 | 66 | 58 | 78 | 60 | same |
| Accounts receivable, net | 155 | 132 | 158 | 184 | 165 | same |
| Inventories | 76 | 71 | 78 | 84 | 89 | same |
| Prepaid expenses and other current assets | 274 | 256 | 270 | 274 | 323 | same |
| Total current assets | 1,877 | 2,001 | 1,568 | 1,685 | 1,675 | same |
| Operating lease right-of-use assets | 925 | 862 | 741 | 722 | 881 | same |
| Property and equipment, net | 603 | 516 | 502 | 512 | 533 | same |
| Other non-current assets | 54 | 61 | 59 | 59 | 62 | same |
| Total assets | 3,459 | 3,440 | 2,870 | 2,978 | 3,151 | same |
| Accounts payable | 1,246 | 1,202 | 1,094 | 1,317 | 1,213 | same |
| Other current liabilities | 1,124 | 927 | 961 | 951 | 1,283 | same |
| Total current liabilities | 2,370 | 2,129 | 2,055 | 2,268 | 2,496 | same |
| Long-term debt | 2,882 | 3,233 | 2,931 | 2,797 | 2,572 | same |
| Operating lease liabilities, net of current | 929 | 835 | 704 | 680 | 864 | same |
| Other non-current liabilities | 33 | 25 | 22 | 21 | 23 | same |
| Total liabilities | 6,214 | 6,222 | 5,712 | 5,766 | 5,955 | same |
| Total stockholders' deficit | (2,755) | (2,782) | (2,842) | (2,788) | (2,804) | 10-K page:100; Q1 10-Q page:2; Q2 10-Q page:2; Q3 10-Q page:2 |

Short-term debt is inside other current liabilities: 236 at 2024-12-31 (10-K page:113), 39 at 2025-12-31 (10-K page:118), 39 at 2026-03-31 (Q1 10-Q page:9), 39 at 2026-06-30 (Q2 10-Q page:11) and 227 at 2026-09-30 (Q3 10-Q page:11). The Q3 10-Q does not break out the rest of other current liabilities (1,283 less 227 short-term debt is 1,056); the 10-K does at year end (page:113), including unearned revenue 265, current operating lease liabilities 190, advertising 84, sales tax payable 75, employee compensation 51 and sales return allowance 45. Contract liabilities are 296 at 2026-09-30 (Q3 10-Q page:7).

### Reported cash flows

| Line (USD m) | FY2024 | FY2025 | 9M 2025 | 9M 2026 | Locators |
| --- | --- | --- | --- | --- | --- |
| Net loss | (492) | (313) | (197) | (44) | 10-K page:101; Q3 10-Q page:4 |
| Depreciation and amortization | 387 | 305 | 234 | 195 | same |
| Equity-based compensation expense | 395 | 335 | 252 | 201 | same |
| Loss (gain) on debt extinguishment | (29) | 233 | 68 | 102 | same |
| Other non-cash items net (amortization of discount, impairment, lease gain, other) | 45 | 23 | 51 | (12) | same; see Calculations |
| Change in operating assets and liabilities | 11 | (49) | (76) | 64 | same; see Calculations |
| Net cash provided by operating activities | 317 | 534 | 332 | 506 | same |
| Purchase of property and equipment | (73) | (70) | (45) | (81) | same |
| Site and software development costs | (161) | (135) | (103) | (94) | same |
| Net cash used in investing activities | (262) | (219) | (150) | (168) | same |
| Proceeds from issuance of debt, net | 786 | 1,383 | 691 | 395 | same |
| Payment of principal upon maturity of debt | (117) | (157) | Nil printed (dash) | (39) | same |
| Payments to extinguish debt | (741) | (1,315) | (940) | (245) | same |
| Settlement of long-term debt | No such line | No such line | Nil printed (dash) | (696) | Q3 10-Q page:4 |
| Taxes paid on net share settlement of equity awards | No such line | (89) | (54) | (77) | 10-K page:101; Q3 10-Q page:4 |
| Repurchase of common stock | No such line | No such line | Nil printed (dash) | (60) | Q3 10-Q page:4 |
| Payments for purchase of equity instrument | No such line | No such line | Nil printed (dash) | (60) | Q3 10-Q page:4 |
| Net cash (used in) provided by financing activities | (69) | (129) | (303) | (782) | 10-K page:101; Q3 10-Q page:4 |
| Cash paid for interest on long-term debt | 63 | 139 | 98 | 129 | 10-K page:101; Q3 10-Q page:5 |

Cash taxes paid are printed for FY2025 only, as 4 of state income taxes net of refunds and 8 of foreign tax (10-K page:137); no interim cash tax figure is printed (Gaps). The FY2024 and FY2025 columns also include a 49 capped call unwind inflow in FY2025 and 3 in FY2024 (10-K page:101), which is not a debt flow.

### Adjusted EBITDA reconciliation and segments

| Line (USD m) | FY2024 | FY2025 | 9M 2025 | 9M 2026 | Q3 2025 | Q3 2026 | Locators |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net income (loss) | (492) | (313) | (197) | (44) | (99) | 62 | 10-K page:88; Q3 rel page:11 |
| Depreciation and amortization | 387 | 305 | 234 | 195 | 75 | 64 | same |
| Equity-based compensation and related taxes | 411 | 345 | 261 | 209 | 92 | 66 | same |
| Interest expense, net | 29 | 119 | 83 | 120 | 31 | 42 | same |
| Other (income) expense, net | 21 | (31) | (28) | 14 | 5 | (1) | same |
| Provision for income taxes, net | 10 | 9 | 7 | 7 | 2 | 3 | same |
| Impairment and other related net charges | 37 | 23 | 23 | 2 | Nil printed (dash) | Nil printed (dash) | same |
| Restructuring and other charges, net | 79 | 53 | 68 | 24 | 3 | Nil printed (dash) | same |
| Loss (gain) on debt extinguishment | (29) | 233 | 68 | 102 | 99 | Nil printed (dash) | same |
| Adjusted EBITDA | 453 | 743 | 519 | 629 | 208 | 236 | 10-K page:88; Q3 rel page:11 |
| Adjusted EBITDA margin (printed) | 3.8% | 6.0% | 5.7% | 6.4% | 6.7% | 6.9% | same |

| Segment (USD m) | FY2024 | FY2025 | 9M 2025 | 9M 2026 | Q3 2025 | Q3 2026 | Locators |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U.S. net revenue | 10,373 | 10,973 | 8,031 | 8,777 | 2,728 | 3,040 | 10-K page:143; Q3 rel page:6 |
| International net revenue | 1,478 | 1,484 | 1,089 | 1,093 | 389 | 380 | same |
| U.S. Adjusted EBITDA | 571 | 762 | 528 | 683 | 209 | 261 | 10-K page:143; Q3 rel page:11 |
| International Adjusted EBITDA | (118) | (19) | (9) | (54) | (1) | (25) | same |

International Adjusted EBITDA is a loss of 25 in Q3 2026 against a loss of 1 in Q3 2025, on revenue of 380 against 389, so the segment is a drag that U.S. earnings (261 against 209) more than cover.

### Operating metrics (management KPIs)

| Metric | Q3 2026 | Q3 2025 | Locator |
| --- | --- | --- | --- |
| Active customers (millions) | 22.2 | 21.2 | Q3 rel page:2 |
| LTM net revenue per active customer (USD) | 596 | 578 | Q3 rel page:2 |
| Orders delivered (millions) | 11.0 | 9.8 | Q3 rel page:2 |
| Average order value (USD) | 311 | 317 | Q3 rel page:2 |
| Repeat customer share of orders | 80.0% | 80.1% | Q3 rel page:2 |

The Q3 10-Q attributes the revenue increase to higher order volume partly offset by lower average order value (page:30), consistent with the two printed figures above. Gross margin was 29.6% in Q3 2026 against 30.0% in Q3 2025 (Q3 rel page:10), and the 10-Q says cost of goods sold rose as a share of revenue to 70.4% from 70.0% (page:31).

### Definition review

- Total debt: the debt note prints Total Debt at carrying amount, net of unamortized discount: 2,799 at 2026-09-30 (page:11). The principal is the sum of the series, 2,829, calculated here. Operating lease liabilities, the capped calls and letters of credit are outside both figures. This module uses the printed carrying total for ratios and says so in each basis cell.
- EBITDA, three definitions held apart. (1) The company prints no unadjusted EBITDA; operating income plus depreciation and amortization is calculated here as 549 for the last twelve months. (2) Company-defined Adjusted EBITDA is net income before depreciation and amortization, equity-based compensation and related taxes, interest, other income or expense, taxes, non-recurring items and other items "not indicative of our core operating performance" (Q3 rel page:8). The items in the reconciliation are those in the table above. (3) The covenant EBITDA in the revolver is "Consolidated EBITDA" as defined in the credit agreement (Q3 10-Q page:42), which is not supplied, so it may differ from both.
- Equity compensation: the reconciliation adds back "Equity-based compensation and related taxes" of 345 in FY2025, while the cash flow statement shows equity-based compensation expense of 335; the 10 difference is the related-taxes component implied by the two statements, and the pack does not define it.
- Free cash flow: net cash from operating activities less purchases of property and equipment and site and software development costs (Q3 rel page:9). It is before debt service principal, before tax paid on net share settlement and before buybacks, which are financing lines.
- Cash interest: "Cash paid for interest on long-term debt" in the cash flow supplemental information (Q3 10-Q page:5). It is gross of interest income, which is 30 for nine months 2026 (Q3 10-Q page:9).
- Liquidity: the 10-Q table is cash plus short-term investments and excludes the revolver (page:39); the releases state a larger "total liquidity" including revolver availability (Q3 rel page:1). Both are shown and labelled below.
- LTM: last twelve months equals the 10-K year plus the current year-to-date less the prior-year year-to-date, calculated here and labelled as derived.

### Debt schedule at 2026-09-30

| Instrument | Issuer and guarantors | Ranking and security | Coupon and effective rate | Maturity | Principal | Carrying amount | Fair value | Fair value as % of principal (calculated) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revolver (US$500 million commitment) | Borrower Wayfair LLC; Wayfair Inc. and certain subsidiaries guarantee (10-K page:119) | Senior secured, first-priority liens on substantially all assets (10-K page:119) | Variable; margin 1.25% over Term SOFR at 2025-12-31 (10-K page:120) | 2030-03-13 (Q3 10-Q page:11) | Nil drawn | Nil | Not applicable | Not applicable |
| 3.250% Convertible Senior Notes due 2027 | Wayfair Inc.; Wayfair LLC guarantees (10-K page:125) | Senior unsecured, structurally subordinated to subsidiary liabilities (10-K page:130) | 3.250%; 3.6% effective (Q3 10-Q page:11) | 2027-09-15 | 229 | 227 | 376 | 164.2% |
| 7.250% Senior Secured Notes due 2029 | Issuer Wayfair LLC; guarantors named in the indenture including Wayfair Inc. (10-K page:121) | Senior secured; first-priority liens pari passu with the revolver (10-K page:130) | 7.250%; 7.5% effective | 2029-10-31 | 800 | 791 | 812 | 101.5% |
| 7.750% Senior Secured Notes due 2030 | Same | Same | 7.750%; 7.9% effective | 2030-09-15 | 700 | 693 | 720 | 102.9% |
| 6.750% Senior Secured Notes due 2032 | Same | Same | 6.750%; 6.8% effective | 2032-11-15 | 700 | 693 | 692 | 98.9% |
| 7.125% Senior Secured Notes due 2034 | Issuer Wayfair LLC; guarantors named in the indenture including Wayfair Inc. (Q2 10-Q page:12) | Described as senior secured obligations of the Issuer (Q2 10-Q page:12); pari passu wording is printed for the earlier series only | 7.125%; 7.2% effective | 2034-05-31 | 400 | 395 | 398 | 99.5% |
| Total | | | | | 2,829 (calculated) | 2,799 (printed) | 2,998 (calculated) | |

Locators for the amounts: principal, carrying amount and coupons Q3 10-Q page:10-11; fair values Q3 10-Q page:15. The 2027 Notes convert at an initial price of $63.45 and become freely convertible from 2027-06-15 (Q3 10-Q page:12); the conditional conversion feature was triggered in the quarter ended 2026-09-30, so they are convertible in the quarter ending 2026-12-31 (page:13); the if-converted value exceeded principal by 141 (page:15). The 2027 capped calls have an initial cap price of $97.62 (page:16). No market share price at the cutoff is supplied.

Letters of credit of 82 reduce revolver availability (Q3 10-Q page:11). The senior secured notes total 2,600 of principal, 91.9% of the 2,829 total.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 6.88 | 3.85 | x | Total debt 3,118 (carrying, 10-K page:118) over company-defined Adjusted EBITDA 453; net debt deducts cash 1,316 and short-term investments 56; not a covenant definition |
| FY2025 | 4.40 | 2.33 | x | Total debt 3,272 over Adjusted EBITDA 743; net debt deducts cash 1,476 and short-term investments 66; excludes operating leases |
| LTM Q1 2026 | 3.77 | 2.42 | x | Total debt 2,970 (Q1 10-Q page:9) over derived LTM Adjusted EBITDA 788; net debt deducts 1,062 of cash and short-term investments; LTM is derived |
| LTM Q2 2026 | 3.44 | 2.05 | x | Total debt 2,836 (Q2 10-Q page:11) over derived LTM Adjusted EBITDA 825; net debt deducts 1,143; LTM is derived |
| LTM Q3 2026 | 3.28 | 1.99 | x | Total debt 2,799 (Q3 10-Q page:11) over derived LTM Adjusted EBITDA 853; net debt deducts 1,098; Adjusted EBITDA adds back equity compensation, so unadjusted leverage is higher (5.10x total debt on operating income plus D&A) |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 7.19 | x | Adjusted EBITDA 453 over cash paid for interest 63 (10-K page:101); Adjusted EBITDA is company-defined |
| FY2025 | 5.35 | x | Adjusted EBITDA 743 over cash paid for interest 139 |
| LTM Q1 2026 | 4.99 | x | Derived LTM Adjusted EBITDA 788 over derived LTM cash interest 158 (139 plus 35 less 16) |
| LTM Q2 2026 | 4.63 | x | Derived LTM Adjusted EBITDA 825 over derived LTM cash interest 178 (139 plus 98 less 59) |
| LTM Q3 2026 | 5.02 | x | Derived LTM Adjusted EBITDA 853 over derived LTM cash interest 170 (139 plus 129 less 98); cash interest is gross of interest income; cover on run-rate coupons of about 195 is 4.36x |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| 2024-12-31 | 1316 | Not supplied: revolver size and letters of credit at 2024-12-31 are not printed in the pack | US$m | Cash and cash equivalents only (10-K page:99); short-term investments of 56 are excluded from this column |
| 2025-12-31 | 1476 | 406 | US$m | Undrawn is the 500 revolver less 94 letters of credit, nothing drawn (10-K page:119); short-term investments of 66 excluded |
| 2026-03-31 | 1004 | 410 | US$m | 500 less 90 letters of credit (Q1 10-Q page:9); short-term investments of 58 excluded |
| 2026-06-30 | 1065 | 418 | US$m | 500 less 82 letters of credit (Q2 10-Q page:12); short-term investments of 78 excluded |
| 2026-09-30 | 1038 | 418 | US$m | 500 less 82 letters of credit (Q3 10-Q page:11); short-term investments of 60 excluded; availability is arithmetic and is not tested against covenants |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0 | US$m | No instrument in the debt table matures after 2026-09-30 in 2026; the 39 of 2026 Notes was paid on 2026-08-15 (Q3 10-Q page:13) |
| 2027 | 229 | US$m | 3.250% convertible notes due 2027-09-15; principal; settlement may be in cash, shares or a mix at the company's election (page:13) |
| 2028 | 0 | US$m | No 2028 Notes remain (page:15) |
| 2029 | 800 | US$m | 7.250% senior secured notes due 2029-10-31; principal |
| 2030 | 700 | US$m | 7.750% senior secured notes due 2030-09-15; principal; the undrawn 500 revolver also matures 2030-03-13, subject to a springing earlier maturity whose trigger is not described, and is not debt |
| 2031 | 0 | US$m | No instrument in the debt table matures in 2031 |
| 2032 | 700 | US$m | 6.750% senior secured notes due 2032-11-15; principal |
| 2033 | 0 | US$m | No instrument in the debt table matures in 2033 |
| 2034 | 400 | US$m | 7.125% senior secured notes due 2034-05-31; principal |

### Financials and credit metrics

| Metric (USD m unless stated) | FY2024 | FY2025 | 9M 2025 | 9M 2026 | LTM Q3 2026 | Basis |
| --- | --- | --- | --- | --- | --- | --- |
| Net revenue | 11,851 | 12,457 | 9,120 | 9,870 | 13,207 | LTM derived: 12,457 + 9,870 - 9,120 |
| Gross profit | 3,574 | 3,765 | 2,755 | 2,946 | 3,956 | LTM derived |
| Income (loss) from operations | (461) | 17 | (67) | 199 | 283 | LTM derived |
| Net income (loss) | (492) | (313) | (197) | (44) | (160) | LTM derived |
| Depreciation and amortization | 387 | 305 | 234 | 195 | 266 | LTM derived |
| EBITDA (operating income plus D&A), calculated | (74) | 322 | 167 | 394 | 549 | Calculated; not a company measure |
| Equity-based compensation and related taxes | 411 | 345 | 261 | 209 | 293 | LTM derived |
| Adjusted EBITDA (company-defined) | 453 | 743 | 519 | 629 | 853 | LTM derived |
| Adjusted EBITDA margin | 3.8% | 6.0% | 5.7% | 6.4% | 6.5% | Calculated from the rows above |
| Net cash from operating activities | 317 | 534 | 332 | 506 | 708 | LTM derived |
| Capital expenditure (property and equipment plus site and software) | 234 | 205 | 148 | 175 | 232 | Calculated; outflows shown as positive |
| Free cash flow | 83 | 329 | 184 | 331 | 476 | Printed for periods; LTM derived |
| Cash paid for interest | 63 | 139 | 98 | 129 | 170 | LTM derived |
| Total debt, carrying (period end) | 3,118 | 3,272 | Not supplied: the Q3 2025 balance sheet is not in the pack | 2,799 | 2,799 | Printed at period end |
| Cash and short-term investments (period end) | 1,372 | 1,542 | Not supplied: the Q3 2025 balance sheet is not in the pack | 1,098 | 1,098 | Calculated: cash plus short-term investments |
| Net debt (period end) | 1,746 | 1,730 | Not supplied: the Q3 2025 balance sheet is not in the pack | 1,701 | 1,701 | Calculated |
| Total debt / Adjusted EBITDA (x) | 6.88 | 4.40 | n/a: nine-month period | n/a: nine-month period | 3.28 | Calculated |
| Net debt / Adjusted EBITDA (x) | 3.85 | 2.33 | n/a: nine-month period | n/a: nine-month period | 1.99 | Calculated |
| Total debt / EBITDA, unadjusted (x) | Not meaningful: negative EBITDA | 10.16 | n/a: nine-month period | n/a: nine-month period | 5.10 | Calculated |
| Net debt / EBITDA, unadjusted (x) | Not meaningful: negative EBITDA | 5.37 | n/a: nine-month period | n/a: nine-month period | 3.10 | Calculated |
| Adjusted EBITDA / cash interest (x) | 7.19 | 5.35 | 5.30 | 4.88 | 5.02 | Calculated; the nine-month columns use nine-month cash interest |
| EBITDA (unadjusted) / cash interest (x) | Not meaningful: negative EBITDA | 2.32 | 1.70 | 3.05 | 3.23 | Calculated |
| Free cash flow / Adjusted EBITDA | 18.3% | 44.3% | 35.5% | 52.6% | 55.8% | Calculated |
| Secured notes principal / Adjusted EBITDA (x), indicative | 1.77 | 2.96 | n/a: nine-month period | n/a: nine-month period | 3.05 | Calculated on secured principal of 800 (2029 notes) at 2024-12-31, 2,200 (2029, 2030 and 2032 notes) at 2025-12-31 and 2,600 at 2026-09-30; not a covenant test and no headroom shown |

### Liquidity and cash flow reading

- Liquidity at 2026-09-30: cash 1,038 plus short-term investments 60 is 1,098 (Q3 10-Q page:39); with 418 of undrawn revolver after letters of credit, the arithmetic total is 1,516, consistent with the release wording of a total liquidity of 1.5 billion (Q3 rel page:1). Cash fell from 1,476 at 2025-12-31 by 438 over nine months while operating cash flow was 506, because financing used 782: 245 to extinguish debt, 696 of settlement of long-term debt, 39 at maturity, 77 for tax on net share settlement, 60 of buybacks and 60 for an equity instrument, against 395 of new debt proceeds (Q3 10-Q page:4).
- Debt activity in nine months 2026: net cash paid on debt principal and extinguishment was 585 (980 out less 395 in), and the principal outstanding fell from 3,308 to 2,829 as 39 of 2026 Notes, 251 of 2027 Notes and 589 of 2028 Notes were retired and 400 of 2034 Secured Notes were issued. Loss on debt extinguishment of 102 was charged (page:3); it is outside Adjusted EBITDA.
- Operating cash flow quality: nine-month operating cash flow rose from 332 to 506. The Q3 10-Q attributes 140 of the 174 increase to cash changes in operating assets and liabilities (page:44). Accounts payable of 1,213 against inventories of 89 (page:2) mean the working-capital line is large relative to inventory, and the 64 inflow in nine months 2026 may not repeat.
- Capital expenditure including site and software costs was 1.8% of net revenue in nine months 2026 (Q3 10-Q page:44), consistent with 175 over 9,870.
- Free cash flow was negative in Q1 2026 (106 outflow, Q1 rel page:1) and positive in Q2 2026 (301) and Q3 2026 (136). Free cash flow was also negative in Q1 2025 (139 outflow, Q1 rel page:2), so the first quarter is weak in both years printed.
- Interest: the 2034 Secured Notes at 7.125% replaced 2028 Notes at 3.50% (Q3 10-Q page:41, page:14), which is why the Q3 10-Q says interest expense, net rose by 11 to 42 in Q3 and to 120 from 83 in nine months (page:33, page:38). Stated coupons on the 2,829 of principal outstanding at 2026-09-30 total about 195 a year (calculated), above the 170 of last-twelve-month cash interest and before interest income, which was 30 for nine months (page:9).

### Earnings quality and definition risks

- Adjusted EBITDA bridge, last twelve months to Q3 2026: operating income 283 plus D&A 266 plus equity compensation and related taxes 293 plus impairment, restructuring and other charges 11 equals 853 (calculated). Equity compensation is therefore 34.3% of Adjusted EBITDA, against 46.4% in FY2025 (345 of 743). The fall reflects both lower equity compensation and higher Adjusted EBITDA.
- Non-cash versus cash: 77 of tax on net share settlement was paid in cash in nine months 2026 and 89 in FY2025, outside operating cash flow and free cash flow. Shares withheld for that purpose are a cash cost of equity pay that the Adjusted EBITDA add-back does not show.
- A one-time benefit is in the prior-year base: the Q3 10-Q says nine-month cost of goods sold rose partly because of "the absence of a one-time benefit of $38 million related to a resolution on the valuation of duties" in Q1 2025 (page:35). The prior-year nine-month Adjusted EBITDA therefore includes that benefit, and the reconciliation has no add-back for it; the last-twelve-month measure removes the nine-month 2025 period. FY2025 cost of goods sold also carries a 45 benefit from customs duty examinations (10-K page:133), which is likewise not adjusted out.
- Q3 2026 selling, operations, technology, general and administrative expense includes "costs associated with a legal settlement" (Q3 10-Q page:33), not quantified.
- Restructuring and impairment add-backs are 26 in nine months 2026 against 91 a year earlier, and none in Q3 2026 (page:3); the 24 in 2026 is a loss on termination of an operating lease for a logistics facility (page:8).
- Segment concentration: U.S. Adjusted EBITDA of 683 over nine months 2026 against a loss of 54 in International, so earnings quality depends on U.S. execution (Q3 rel page:11).

### Claims outside the debt figure

| Claim | Amount and date | Inside or outside total debt | Locator |
| --- | --- | --- | --- |
| Operating lease liabilities, non-current | 864 at 2026-09-30 | Outside | Q3 10-Q page:2 |
| Operating lease liabilities, total | 1,025 at 2025-12-31 (190 current plus 835 non-current) | Outside | 10-K page:113, page:118 |
| Operating lease commitments not yet commenced | 110 entered in nine months 2026 | Outside | Q3 10-Q page:8, page:45 |
| Future minimum operating lease payments | 1,391 at 2025-12-31 | Outside | 10-K page:83 |
| Purchase obligations (software licence and freight) | 649 at 2025-12-31 | Outside | 10-K page:84 |
| Letters of credit under the revolver | 82 at 2026-09-30 | Outside; reduce revolver availability | Q3 10-Q page:11 |
| Litigation accruals | Not quantified; "fully insured for a majority of these matters" | Outside | Q3 10-Q page:17 |
| Canada Border Services Agency review | Payments of about 19 and cost of about 14 in FY2025; further exposure not quantified | Outside | 10-K page:132-133 |
| Capped calls on 2027 Notes | Cap price $97.62; classified in equity | Outside | Q3 10-Q page:16-17 |
| Pension, factoring, supply-chain finance | None found in the pack | Not applicable | Search in Gaps |

### Events in the period and after

| Event | Date and amount | Effect and locator |
| --- | --- | --- |
| 2034 Secured Notes issued by Wayfair LLC | 2026-05-18; 400 at 7.125% due 2034 | Financed the redemption of the remaining 2028 Notes with cash on hand (Q3 10-Q page:41) |
| 2028 Notes retired | 56 repurchased Feb-Mar 2026, 89 repurchased Apr-May 2026, 444 redeemed 2026-06-29 (converted into cash of 444 and 4.5 million shares) | 589 retired in total; loss on extinguishment 102 (Q3 10-Q page:14-15) |
| 2027 Notes partly redeemed | 250 called 2026-03-23, settled in cash of 250 and 0.9 million shares | Principal 480 to 230 (Q3 10-Q page:14; Q1 10-Q page:9) |
| 2026 Notes matured | 2026-08-15; 39 paid in cash | None outstanding (Q3 10-Q page:13) |
| 2027 Notes conversion trigger | Quarter ended 2026-09-30 | Convertible in quarter ending 2026-12-31; if-converted excess 141 (Q3 10-Q page:13, page:15) |
| Share repurchase and equity instrument | 60 repurchased at an average $100.01; 60 equity instrument settled 2026-10-28 for 64 cash | Subsequent event dated before the cutoff (Q3 10-Q page:18, page:42) |
| Logistics lease termination | Obligations reduced by 138; charge of 24 | Q3 10-Q page:8 |
| Revolver | No revolving loans outstanding at March, June or September 2026; letters of credit 90, 82 and 82 at those dates | Q1 10-Q page:9; Q2 10-Q page:12; Q3 10-Q page:11 |

No event dated after the cutoff 2026-11-05 is used. The Q3 10-Q is signed 2026-11-04 (page:56).

### Requirement readiness for later modules

| Requirement | Status | Evidence and limit |
| --- | --- | --- |
| normalized_financials | sufficient | Statements of operations, balance sheets and cash flows for all periods above; Q3 2025 balance sheet not supplied |
| entity_scope | limited | Consolidated Wayfair Inc.; borrower, issuer and guarantor roles from filing text only; guarantor list not supplied |
| period_coverage | limited | Q1 to Q3 2026 and 2025 comparatives, FY2023 to FY2025; Q4 2025 stand-alone is derived only |
| kpi_dashboard | sufficient | Release KPIs and the metrics table above, each with a value |
| calculation_register | sufficient | Calculations section lists every derived figure with inputs |
| fcf_build | sufficient | Operating cash flow less capital expenditure for each period; financing-side dilution costs shown separately |
| cash_flow_metrics | sufficient | Operating cash flow, free cash flow and cash interest by period |
| liquidity_data | limited | Cash, short-term investments, revolver and letters of credit by date; 2024-12-31 undrawn facility not supplied |
| earnings_quality_metrics | limited | Adjusted EBITDA is company-defined; add-backs listed; no covenant EBITDA |
| debt_classification | sufficient | Series, issuer, security and guarantor roles in the debt schedule, from filing text |
| capital_structure | sufficient | Debt schedule plus balance sheet |
| debt_schedule | sufficient | Principal, carrying, fair value, coupon and maturity for every series |
| maturity_profile | sufficient | Maturity chart by year; revolver springing trigger not described |
| covenant_metrics | limited | Level 4.0x named; no reported ratio |
| ebitda_definitions | sufficient | Three definitions held apart in the definition review |
| covenant_compliance | limited | Compliance statement only (Q3 10-Q page:42); no tested ratio |

### Quality and lineage

| Claim | Lineage | Confidence | Reason |
| --- | --- | --- | --- |
| Reported statement lines, debt table, cash and letters of credit | Directly Sourced | High | Verbatim table values with locators; sums tie in Calculations |
| LTM figures, ratios, net debt, Q4 2025 | Calculated | High | Formulas and inputs shown; inputs share period and perimeter |
| Run-rate coupon of about 195 | Calculated | Medium | Stated coupons times principal; excludes revolver fees, interest income and any new financing |
| Adjusted EBITDA as a measure of earnings capacity | Directly Sourced as a management measure | Medium | Adds back equity compensation and related taxes; covenant definition unknown |
| Leverage improvement driven mainly by earnings growth | Analyst Inference | Medium | Debt fell 10.2%; Adjusted EBITDA rose 88.3%; comparison spans different period types |
| Interest cost rising because of the 2034 issuance | Analyst Inference | Medium | Supported by coupons and the Q3 10-Q interest explanation; not separately quantified |

## Calculations

All in USD millions unless stated. Inputs carry locators; derived figures are labelled.

| Calculation | Inputs and locators | Result |
| --- | --- | --- |
| LTM net revenue to Q3 2026 | FY2025 12,457 (10-K page:100) + 9M 2026 9,870 - 9M 2025 9,120 (Q3 10-Q page:3) | 13,207 |
| LTM gross profit | 3,765 + 2,946 - 2,755 | 3,956 |
| LTM income from operations | 17 + 199 - (-67) | 283 |
| LTM D&A | 305 + 195 - 234 (10-K page:101; Q3 10-Q page:4) | 266 |
| LTM EBITDA, operating income plus D&A | 283 + 266 | 549 |
| LTM equity compensation and related taxes | 345 + 209 - 261 (Q3 rel page:11) | 293 |
| LTM Adjusted EBITDA | 743 + 629 - 519 (10-K page:88; Q3 rel page:11) | 853; cross-check from discrete quarters: Q4 2025 224 (derived) + Q1 2026 151 + Q2 2026 242 + Q3 2026 236 = 853 |
| LTM Adjusted EBITDA at Q1 2026 | 743 + 151 - 106 (Q1 rel page:2) | 788 |
| LTM Adjusted EBITDA at Q2 2026 | 743 + 393 - 311 (Q2 rel page:12) | 825 |
| Adjusted EBITDA bridge, LTM | 549 + 293 + (23 + 53 impairment and restructuring in FY2025 + 2 + 24 in 9M 2026 - 23 - 68 in 9M 2025 = 11) | 853, equal |
| Q4 2025 derived quarter | FY2025 less 9M 2025: revenue 12,457 - 9,120; gross profit 3,765 - 2,755; operating income 17 - (-67); net income (313) - (197); Adjusted EBITDA 743 - 519; operating cash flow 534 - 332; free cash flow 329 - 184 | 3,337; 1,010; 84; (116); 224; 202; 145 |
| Quarterly sums tie to nine months | Revenue 2,931 + 3,519 + 3,420 = 9,870 and 2,730 + 3,273 + 3,117 = 9,120; Adjusted EBITDA 151 + 242 + 236 = 629 and 106 + 205 + 208 = 519; operating cash flow (52) + 360 + 198 = 506 and (96) + 273 + 155 = 332; free cash flow (106) + 301 + 136 = 331 and (139) + 230 + 93 = 184; net income (105) + (1) + 62 = (44) and (113) + 15 + (99) = (197) | All equal to the printed nine-month figures |
| Statement of operations foots | Gross profit less total operating expenses: 3,574 - 4,035; 3,765 - 3,748; 2,755 - 2,822; 2,946 - 2,747; 934 - 896; 1,012 - 906 | (461); 17; (67); 199; 38; 106, equal to printed |
| Net income foots | Income from operations + interest + other + debt extinguishment - tax: 106 - 42 + 1 + 0 - 3 and 199 - 120 - 14 - 102 - 7 | 62 and (44), equal |
| Adjusted EBITDA reconciliation foots | 9M 2026: -44 + 195 + 209 + 120 + 14 + 7 + 2 + 24 + 102; FY2025: -313 + 305 + 345 + 119 - 31 + 9 + 23 + 53 + 233 | 629 and 743, equal |
| Operating cash flow foots | 9M 2026: -44 + 195 + 201 + 6 + 2 + 102 - 20 + (-36 - 18 - 70 + 188) | 506, equal; the change in operating assets and liabilities is 64; 9M 2025: -197 + 234 + 252 + 7 + 23 + 68 + 21 + (33 + 7 + 18 - 134) = 332, with a change of (76) |
| Other non-cash items net (cash flow table) | 9M 2026: amortization 6 + impairment 2 + other (20); 9M 2025: 7 + 23 + 21; FY2025: 9 + 23 + (15) + 6; FY2024: 9 + 37 + (1) | (12); 51; 23; 45 |
| Free cash flow | OCF less capital expenditure: 506 - 81 - 94 and 198 - 30 - 32; FY2025 534 - 70 - 135 | 331; 136; 329, equal to printed |
| LTM operating cash flow and capital expenditure | 534 + 506 - 332; (70 + 135) + (81 + 94) - (45 + 103) | 708; 232; LTM free cash flow 708 - 232 = 476 |
| LTM cash interest | FY2025 139 + 9M 2026 129 - 9M 2025 98 (10-K page:101; Q3 10-Q page:5); at Q1: 139 + 35 - 16; at Q2: 139 + 98 - 59 (Q1 10-Q page:4; Q2 10-Q page:4) | 170; 158; 178 |
| Total debt, net debt | Carrying 2,799 less cash 1,038 less short-term investments 60 (Q3 10-Q page:2, page:11); prior dates from the balance sheet table | 1,701 at 2026-09-30; 1,730 at 2025-12-31; 1,746 at 2024-12-31; 1,908, 1,693 at March and June 2026 |
| Leverage ratios | 2,799 / 853; 1,701 / 853; 2,799 / 549; 1,701 / 549; and the other dates as in the chart | 3.28x; 1.99x; 5.10x; 3.10x |
| Interest cover | 853 / 170; 549 / 170; 743 / 139; 322 / 139 | 5.02x; 3.23x; 5.35x; 2.32x |
| Nine-month interest cover | 629 / 129; 519 / 98; 394 / 129; 167 / 98 | 4.88x; 5.30x; 3.05x; 1.70x |
| Change since FY2024 | Adjusted EBITDA 853 / 453 - 1; total debt 2,799 / 3,118 - 1 | +88.3%; -10.2% |
| Principal total and bridge | 229 + 800 + 700 + 700 + 400 = 2,829; 3,308 - 39 - 251 - 589 + 400 = 2,829 (Q3 10-Q page:10-11; 10-K page:118) | 2,829, equal |
| Carrying total ties | 227 + 791 + 693 + 693 + 395 = 2,799; 227 + 2,572 = 2,799 | Equal to printed |
| Secured notes share | 800 + 700 + 700 + 400 = 2,600; 2,600 / 2,829 | 91.9% |
| Indicative secured ratio, not a covenant test | 2,600 / 853; 2,200 / 743 (secured principal 800 + 700 + 700 at 2025-12-31); 800 / 453 (2029 notes at 2024-12-31, 10-K page:118) | 3.05x; 2.96x; 1.77x |
| Run-rate coupons | 229 x 3.250% + 800 x 7.250% + 700 x 7.750% + 700 x 6.750% + 400 x 7.125% = 7.44 + 58.00 + 54.25 + 47.25 + 28.50 | 195.44; Adjusted EBITDA 853 over 195.44 = 4.36x |
| Fair value over principal | 376 / 229; 812 / 800; 720 / 700; 692 / 700; 398 / 400 (Q3 10-Q page:15) | 164.2%; 101.5%; 102.9%; 98.9%; 99.5%; total fair value 2,998 |
| Revolver availability and liquidity | 500 - 0 - 82 = 418; 1,098 + 418 | 418; 1,516 |
| Financing outflows 9M 2026 | Debt: 39 + 245 + 696 - 395; equity-related: 77 + 60 + 60 | 585 net on debt; 197 on equity-related items |
| Equity compensation share of Adjusted EBITDA | 293 / 853; 345 / 743 | 34.3%; 46.4% |
| Free cash flow conversion | 476 / 853; 331 / 629; 184 / 519; 329 / 743; 83 / 453 | 55.8%; 52.6%; 35.5%; 44.3%; 18.3% |
| Segment margins, Q3 2026 and Q3 2025 | U.S. 261 / 3,040 and 209 / 2,728; International (25) / 380 and (1) / 389 | 8.6% and 7.7%; (6.6)% and (0.3)% |
| Balance sheet foots | 2026-09-30: 1,675 + 881 + 533 + 62 = 3,151; 2,496 + 2,572 + 864 + 23 = 5,955; 3,151 - 5,955 = (2,804) | Equal to printed |
| Interest tie | 9M 2026 contractual interest 143 + discount amortization 6 - interest income 30 (Q3 10-Q page:15, page:9) | 119 against 120 printed; within rounding |
| Cash flow line variances | (a) Settlement of long-term debt is 701 in the six-month column (Q2 10-Q page:4) and 696 in the nine-month column (Q3 10-Q page:4), a 5 decrease in a cumulative line that the text does not explain; (b) cash paid for 2028 Note repurchases is 99 + 148 = 247 in the notes (Q3 10-Q page:14) against 245 in payments to extinguish debt; (c) conversions settled in cash 250 + 444 = 694 against 696 | Small unexplained differences, carried as limitations |
| 2027 Notes principal | 480 - 250 = 230 (Q1 10-Q page:9); 229 at June and September (Q2 10-Q page:10; Q3 10-Q page:10) | 1 unexplained reduction in Q2 |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Reported covenant ratio and the credit agreement definition of Consolidated EBITDA are not supplied; the revolver test is no more than 4.0 to 1.0 (Q3 10-Q page:42). No covenant headroom is shown | High | CP-2 | Obtain the credit agreement and compliance certificate |
| Executed credit agreement, indentures and guarantor lists are not supplied; guarantor roles come from filing text | High | CP-2, CP-5 | Obtain the documents or their 8-K exhibits |
| Q3 2025 balance sheet is not in the pack, so period-end debt, cash and net debt at 2025-09-30 are Not supplied | Low | CP-1 | Not needed for LTM ratios at 2026-09-30 |
| Undrawn facility at 2024-12-31 is Not supplied: the revolver size and letters of credit at that date are not printed in the pack | Low | CP-2 | Use the FY2024 10-K if needed |
| Q4 2025 stand-alone figures are derived only | Low | CP-1 | Labelled as derived |
| Interim cash taxes paid are not printed in the three 10-Qs; FY2025 is 12 (10-K page:137) | Low | CP-1 | A search of the three 10-Qs for "cash paid for" returned interest and principal wording only |
| Current portion of operating lease liabilities at 2026-09-30 and the composition of other current liabilities (1,283) are not printed in the Q3 10-Q; the lease total at 2025-12-31 is 1,025 | Medium | CP-2 | Treat total leases as 1,025 at year end and the non-current 864 at 2026-09-30, labelled separately |
| Revolver springing maturity trigger and current margin are not printed after 2025-12-31 | Medium | CP-2 | Obtain the credit agreement |
| No management guidance is printed in the three releases (search for "outlook" and "guidance" returned nothing); no forecast is available for forward ratios | Medium | CP-2 | None in the pack |
| Ratings, market prices and peer data are not supplied (context blank); the if-converted value of the 2027 Notes is stated by the company only at 2026-09-30 | Medium | CP-2 | Supply dated market data |
| Pension, factoring and supply-chain finance: a search of all seven sources for each term returned no hit; the only retirement plan is a defined-contribution 401(k) plan (10-K page:133) | Low | CP-2 | None |
| Small cash flow line variances and the 1 reduction in 2027 Notes principal are unexplained (Calculations) | Low | CP-1 | Check against the indenture or the next report |
| Canada Border Services Agency matter is described in the 10-K only; its status after year end is unknown | Medium | CP-2 | Check later filings |
| Extraction is text from filings; no fidelity review of flattened tables; locators are page chunks | Low | CP-5 | Spot-check key tables against the original htm |

## Next module

Proceed to CP-1A, then CP-2 and CP-5, in the order CP-OS plans. Carry these instructions forward:

- Use the 10-K for audited FY2024 and FY2025 and the Q3 10-Q for 2026-09-30; treat the releases as supporting claims.
- Use the printed carrying total debt of 2,799 and say when principal (2,829) is meant. Keep leases, purchase obligations, letters of credit and the unquantified litigation and customs matters outside the debt figure.
- State leverage and cover on the company-defined Adjusted EBITDA of 853 and on operating income plus D&A of 549 side by side, and say that Adjusted EBITDA adds back 293 of equity compensation and related taxes.
- Keep the 2027 Notes conversion status, the if-converted excess of 141, the 64 cash settlement on 2026-10-28 and the run-rate coupons of about 195 as open cash and interest items.
- Do not state covenant compliance as tested: the pack gives a level and a compliance statement only.
- Quote the secured-notes ratio only as an indicative metric, never as covenant headroom.
