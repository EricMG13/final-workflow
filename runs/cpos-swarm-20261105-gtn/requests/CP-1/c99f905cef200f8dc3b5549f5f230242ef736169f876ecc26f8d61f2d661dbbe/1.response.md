# CP-1 financial statements and credit metrics: GRAY MEDIA, INC (gtn)

## Request

Issuer: GRAY MEDIA, INC (ticker GTN), consolidated Gray Media, Inc. and subsidiaries. As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit_snapshot. Reporting currency per the run context: USD; every amount below is USD millions as printed unless a ratio or percentage is stated. Current period per the context: q2-2026 (quarter and six months ended June 30, 2026). Prior period: fy-2025.

Scope: reported statements for FY2025, FY2024 and FY2023 (audited), the interim statements for Q3 2025, Q1 2026 and Q2 2026 (unaudited), discrete quarters Q3 2025 to Q2 2026, last-twelve-months (LTM) figures to June 30, 2026, debt by instrument, liquidity, issuer-defined Adjusted EBITDA and covenant ratios, and the claims that sit outside the debt principal. This handoff consumes the CP-0 source-readiness handoff and carries its limitations. No forecast, rating, valuation or pro forma is built. Execution is a host session with no provider call.

Feeds CP-1A, CP-2 and CP-5, and the report sections for financials and credit metrics, leverage, interest cover, liquidity and debt maturities.

## Sources

### Issuer sources relied on

Locators are `page:N` chunks of the pinned text files, not printed page numbers.

| Label | Exact source name | sha256 | Used for |
| --- | --- | --- | --- |
| S-10K | 10-K_2025-12-31_gtn20251231_10k.htm.jsonl | 88cd2be27d00e9908e881a07fffdbfb7e9fbcb182cd4daa7213df1b4b5f00737 | Audited FY2025, FY2024, FY2023 statements; debt note; leverage schedule; cash interest; commitments; pension; segments |
| S-Q3-25 | 10-Q_2025-09-30_gtn20250930_10q.htm.jsonl | b62445e5fe4a163fa362c47bf83e36bde2a987867496619de6fe27a40edfa171 | Q3 2025 discrete quarter |
| S-Q1-26 | 10-Q_2026-03-31_gtn20260331_10q.htm.jsonl | 3356f048b1cdb10c04c5b80b0d02babf79237e5dc24d851924643abb820dcebd | Q1 2026 debt table and leverage schedule |
| S-Q2-26 | 10-Q_2026-06-30_gtn20260630_10q.htm.jsonl | e96d90052b60b94fa2a12b7f9024364ed7aff9961690c651cc002284f695a02b | June 30, 2026 balance sheet, Q2 and six-month statements, cash flow, debt note, covenants, subsequent events |
| S-R-Feb | EX-99.1_2026-02-26_ex_924265.htm.jsonl | 178b7bc5710105291e494cc784bd65c8c9bce375e1552cc63408e1853ff6a993 | Q4 2025 and FY2025 Adjusted EBITDA, revenue mix |
| S-R-May | EX-99.1_2026-05-07_ex_956963.htm.jsonl | b04f43ebe7b79436fed34dc07bcf8f9f9fb0c9fac32a39299a3e02ac7ae325d8 | Q1 2026 Adjusted EBITDA and revenue mix |
| S-R-Aug | EX-99.1_2026-08-07_ex_998938.htm.jsonl | 1120ddd52748c4fbbc1c17f2a7297d8e7f38db5b861bb6f5b9064b68dbae4a0d | Q2 2026 and six-month Adjusted EBITDA, debt summary, guidance, Q3 2025 comparatives |

The run context (sha256 457b491e723cfaa80de6921ac6aa99b1d24251f7cfebd35fd33b60ef8d3cb70e) supplies the USD currency and the period labels only; it is not issuer evidence.

### Handoffs supplied

| Module | sha256 | Carried forward |
| --- | --- | --- |
| CP-0 | e77a699cb806587c5833b538af86a669d2f7b40e236fe396a25b387c082542af | Seven sources are sufficient with limitations. Adjusted EBITDA is release-only. No credit agreement, indentures or later-than-June 2026 balance sheet. Conflicts X1 to X5 and gaps G1 to G9 apply; the ones that bear on figures are restated in `## Gaps`. |

This handoff does not correct CP-0. It adds two details CP-0 did not need: the Q3 2025 Adjusted EBITDA is not printed anywhere in the pack and is derived here (C2), and the covenant schedule lists LRD and net debt but no maintenance-test headroom, which is derived here (C9).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Principal debt of 5,867 is 8.28 times last-twelve-months Adjusted EBITDA of 709, well above the 5.73 times the company reports on its covenant definition. Liquidity is 921 and no principal matures before 2028. | Medium | Adjusted EBITDA is release-only and last twelve months mixes an election-year half with an off-year half; credit agreement terms and post-June borrowing are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt over Adjusted EBITDA is 8.28 times on the last twelve months, against 4.90 times in FY2024, when political advertising and EBITDA were far higher. | Leverage on actual earnings is much higher than the covenant ratio; the covenant ratio depends on an eight-quarter average and acquisition add-backs. | Medium |
| Adjusted EBITDA covers cash interest 1.84 times on the last twelve months, down from 2.95 times in FY2024. | Thin cover leaves little room for an advertising or retransmission shortfall. | Medium |
| Cash is 176 and revolver availability 745; the receivables facility is fully drawn and there is no maturity before 2028. | No principal falls due before 2028, but July 2026 repurchases were partly funded by revolver borrowings of undisclosed size. | Medium |
| Operating cash flow less capital expenditure is 146 on the last twelve months, and dividends of 87 absorb more than half of it. | Little internally generated cash remains for debt reduction. | Medium |

### Financial base view

The financial base is a thinly covered, advertising-cyclical broadcaster that is usable for a snapshot only with its definitions kept apart. On issuer Adjusted EBITDA of 709 for the twelve months to June 30, 2026, principal debt of 5,867 is 8.28 times and debt net of cash is 8.03 times. The company's own covenant measure reads 5.73 times on net debt of 5,696 because its denominator is an eight-quarter average of 994 that includes the third and fourth quarters of the 2024 election year and acquisition, synergy and unrestricted-subsidiary adjustments. Both numbers are correct on their own basis; they must not be mixed, and neither is a maintenance test. The one maintenance covenant described is a first lien net leverage limit, which the issuer text ties to revolver borrowings or to more than 50 of uncollateralized letters of credit, with a stated cap of 4.25 times while revolver amounts are outstanding; the issuer reports 2.55 times at June 30, 2026.

Three features shape every ratio. First, 2026 is a political on-year: political advertising was 113 in the first half of 2026 against 22 a year earlier, so the last twelve months blend an off-year half with an on-year half and fourth-quarter 2026 will differ from the fourth-quarter 2025 base. Second, 2026 acquisitions add revenue and Adjusted EBITDA only from their closing dates, while the full acquisition cost and the July 2026 funding are already in debt or cash. Third, a 400 receivables securitization is fully drawn and sits outside reported debt principal, as does 600 of Series A perpetual preferred stock at liquidation value. Evidence ends with the August 7, 2026 release; the quarter ended September 30, 2026 is not in the pack.

### Source context

| Source | Entity and perimeter | Periods | Statement kind | Units |
| --- | --- | --- | --- | --- |
| S-10K | Gray Media, Inc. and consolidated subsidiaries; holding company with no material independent assets | Years ended December 31, 2025, 2024 and 2023; balance sheets at December 31, 2025 and 2024 | Audited | "(in millions)" (S-10K page:72); USD |
| S-Q3-25 | Same | Three and nine months ended September 30, 2025 | Unaudited condensed | "(in millions, except for per share data)" (S-Q3-25 page:3); USD |
| S-Q1-26 | Same | Three months ended March 31, 2026 | Unaudited condensed | USD millions |
| S-Q2-26 | Same | Three and six months ended June 30, 2026 and 2025; balance sheet at June 30, 2026 and December 31, 2025 | Unaudited condensed | "(in millions)" (S-Q2-26 page:2); USD |
| S-R-Feb, S-R-May, S-R-Aug | Same, issuer presentation | Q4 and FY2025; Q1 2026; Q2 and six months 2026 | Unaudited release; non-GAAP | USD millions |

Same four strings apply to every figure: perimeter consolidated Gray Media, Inc., basis US GAAP, currency USD, unit millions. Per-share data, share counts and percentages are separate quantities and are labelled.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 4.90 | 4.78 | x | Outstanding principal 5,690 and cash 135 at December 31, 2024 over issuer Adjusted EBITDA 1,162 for FY2024 (C4). 2024 was a political on-year. Excludes the receivables facility, letters of credit and preferred stock. |
| FY2025 | 8.67 | 8.12 | x | Principal 5,810 and cash 368 over Adjusted EBITDA 670 for FY2025 (C4). 2025 was a political off-year. Same exclusions. |
| Q2 2026 LTM | 8.28 | 8.03 | x | Principal 5,867 and cash 176 at June 30, 2026 over Adjusted EBITDA 709 for the twelve months to June 30, 2026 (C3, C4). Mixes an off-year half and an on-year half; acquisitions only from closing dates; after July 2026 repurchases the debt would differ (see gaps). Not the covenant ratio, which the issuer reports as 5.73 on a different denominator. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 2.95 | x | Adjusted EBITDA 1,162 over cash interest paid 394 (S-10K page:94); C5. |
| FY2025 | 1.70 | x | Adjusted EBITDA 670 over cash interest paid 393 (S-10K page:94); C5. |
| Q2 2026 LTM | 1.84 | x | Adjusted EBITDA 709 over cash interest paid 385, built as FY2025 plus six months 2026 less six months 2025 (C1, C5). Cash interest is timing-dependent because coupons are semiannual. Interest expense, not cash interest, gives 1.50 (C5). |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 135 | 674 | US$m | Cash at December 31, 2024 and revolver availability of 674 after 6 of undrawn letters of credit (S-10K page:92). |
| FY2025 | 368 | 745 | US$m | Cash at December 31, 2025 and revolver availability of 745 after 5 of letters of credit (S-10K page:92). |
| Q2 2026 | 176 | 745 | US$m | Cash at June 30, 2026 and revolver availability of 745 on a 750 commitment (S-Q2-26 page:15). Excludes the receivables facility, which is fully drawn at 400 and gives no availability. Before the July 2026 repurchases, which were funded partly by revolver borrowings of an undisclosed amount. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remainder of 2026 | 0 | US$m | Principal maturities printed as nil at June 30, 2026 (S-Q2-26 page:16). |
| 2027 | 0 | US$m | Printed as nil (S-Q2-26 page:16). |
| 2028 | 739 | US$m | 2028 1L Term Loan, matures December 1, 2028; the revolver commitment of 750 also terminates December 1, 2028 (S-10K page:92). Revolver is undrawn at June 30, 2026 and is not in the 739. |
| 2029 | 1,125 | US$m | 2029 1L Notes at 10.5%, matures July 15, 2029. 100 was repurchased on July 21, 2026, after the balance sheet date. |
| 2030 | 790 | US$m | 2030 Notes at 4.75%, matures October 15, 2030. |
| 2031 | 1,218 | US$m | 2031 Notes at 5.375%, matures November 15, 2031. 20 was repurchased on July 21, 2026. |
| Thereafter | 1,995 | US$m | 2032 2L Notes 1,150 and 2033 1L Notes 845 (S-Q2-26 page:16). The receivables facility of 400 matures March 31, 2028 and is not in these amounts. |

### Financials and credit metrics

| Metric | LTM to Jun 30, 2026 | FY2025 | FY2024 | Basis and source |
| --- | --- | --- | --- | --- |
| Total revenue (USD m) | 3,148 | 3,095 | 3,644 | LTM calculated C1; FY reported (S-10K page:73) |
| Political advertising revenue (USD m) | 133 | 42 | 497 | LTM calculated C1; FY from S-R-Feb page:2 |
| Adjusted EBITDA, issuer-defined (USD m) | 709 | 670 | 1,162 | LTM calculated C1; FY from S-R-Feb page:11; release-only measure |
| Adjusted EBITDA margin (%) | 22.5 | 21.6 | 31.9 | Calculated C6 |
| Operating income (USD m) | 435 | 392 | 851 | LTM calculated C1; FY reported (S-10K page:73) |
| Interest expense (USD m) | 473 | 474 | 485 | LTM calculated C1; FY reported (S-10K page:73) |
| Net income (loss) (USD m) | (26) | (85) | 375 | LTM calculated C1; FY reported (S-10K page:73) |
| Cash interest paid (USD m) | 385 | 393 | 394 | LTM calculated C1; FY reported (S-10K page:94) |
| Net cash provided by operating activities (USD m) | 250 | 289 | 751 | LTM calculated C1; FY reported (S-10K page:75) |
| Purchases of property and equipment (USD m) | 104 | 108 | 143 | LTM calculated C1; FY reported (S-10K page:75) |
| Operating cash flow less purchases of property and equipment (USD m) | 146 | 181 | 608 | Calculated C7 |
| Dividends paid, preferred and common (USD m) | 87 | 85 | 84 | LTM calculated C1; FY reported (S-10K page:75) |
| Cash (USD m) | 176 | 368 | 135 | Reported (S-Q2-26 page:2; S-10K page:72) |
| Outstanding principal of debt (USD m) | 5,867 | 5,810 | 5,690 | Reported (S-Q2-26 page:15; S-10K page:92) |
| Series A perpetual preferred, liquidation value (USD m) | 600 | 650 | 650 | Reported (S-Q2-26 page:3; S-10K page:73) |
| Receivables sold under the securitization facility (USD m) | 400 | 400 | 300 | Reported (S-Q2-26 page:8; S-10K page:79) |
| Total debt / Adjusted EBITDA (x) | 8.28 | 8.67 | 4.90 | Calculated C4 |
| Net debt / Adjusted EBITDA (x) | 8.03 | 8.12 | 4.78 | Calculated C4 |
| Debt plus preferred plus securitization / Adjusted EBITDA (x) | 9.69 | 10.24 | 5.71 | Calculated C4; sensitivity, not a reported measure |
| Adjusted EBITDA / cash interest (x) | 1.84 | 1.70 | 2.95 | Calculated C5 |
| Adjusted EBITDA / interest expense (x) | 1.50 | 1.41 | 2.40 | Calculated C5 |
| Covenant: Consolidated First Lien Net Leverage Ratio (x) | 2.55 | 2.43 | Not supplied: December 31, 2024 schedule is not in the pack | Reported by issuer (S-Q2-26 page:37; S-10K page:57); incurrence maximum 3.5 |
| Covenant: Consolidated Total Net Leverage Ratio (x) | 5.73 | 5.80 | Not supplied: December 31, 2024 schedule is not in the pack | Reported by issuer (S-Q2-26 page:37; S-10K page:57); incurrence maximum 7.00 |
| Leverage Ratio Denominator, eight-quarter average (USD m) | 994 | 939 | Not supplied: December 31, 2024 schedule is not in the pack | Reported by issuer (S-Q2-26 page:37; S-10K page:57) |

### Discrete quarters

| Line | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | Source |
| --- | --- | --- | --- | --- | --- |
| Total revenue | 749 | 792 | 768 | 839 | S-Q3-25 page:3; S-R-Feb page:2; S-R-May page:2; S-Q2-26 page:3 |
| Core advertising | 355 | 392 | 352 | 357 | S-R-Aug page:5; S-R-Feb page:2; S-R-May page:2; S-R-Aug page:3 |
| Political advertising | 8 | 12 | 30 | 83 | S-R-Aug page:5; S-R-Feb page:2; S-R-May page:2; S-R-Aug page:3 |
| Total broadcasting expense | 542 | 557 | 555 | 569 | S-Q3-25 page:3; S-R-Feb page:2; S-R-May page:2; S-Q2-26 page:3 |
| Net income (loss) | (10) | (10) | (20) | 14 | S-Q3-25 page:3; S-R-Feb page:2; S-R-May page:2; S-Q2-26 page:3 |
| Adjusted EBITDA | 162 | 179 | 154 | 214 | Q3 2025 derived C2 (not printed); S-R-Feb page:11; S-R-May page:2; S-R-Aug page:3 |

The four quarters sum to the LTM totals in C1 (revenue 3,148 and Adjusted EBITDA 709). Q2 and Q4 are seasonally strongest for advertising ([S-Q2-26 page:28] "Broadcast advertising revenue is generally highest in the second and fourth quarters each year.").

### Reported statements of operations

| Line (as printed) | Q2 2026 | Q2 2025 | 6M 2026 | 6M 2025 | FY2025 | FY2024 | FY2023 | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenue (less agency commissions) | 839 | 772 | 1,607 | 1,554 | 3,095 | 3,644 | 3,281 | S-Q2-26 page:3; S-10K page:73 |
| Broadcasting operating expenses | 569 | 563 | 1,124 | 1,140 | 2,239 | 2,317 | 2,268 | S-Q2-26 page:3; S-10K page:73 |
| Corporate and administrative | 37 | 25 | 76 | 57 | 113 | 104 | 112 | S-Q2-26 page:3; S-10K page:73 |
| Depreciation | 34 | 32 | 67 | 66 | 133 | 144 | 145 | S-Q2-26 page:3; S-10K page:73 |
| Amortization of intangible assets | 21 | 28 | 53 | 57 | 104 | 125 | 194 | S-Q2-26 page:3; S-10K page:73 |
| Operating income | 136 | 82 | 217 | 174 | 392 | 851 | 383 | S-Q2-26 page:3; S-10K page:73 |
| Interest expense | (117) | (117) | (234) | (235) | (474) | (485) | (440) | S-Q2-26 page:3; S-10K page:73 |
| Net income (loss) | 14 | (56) | (6) | (65) | (85) | 375 | (76) | S-Q2-26 page:3; S-10K page:73 |
| Preferred stock dividends | (13) | (13) | (26) | (26) | (52) | (52) | (52) | S-Q2-26 page:3; S-10K page:73 |

Interest expense is printed in parentheses and kept signed. FY2025 preferred dividends are printed as a positive 52 in the 10-K and are shown signed here for comparability with the interim statements. The six-month 2026 loss on disposal of 20 includes a 22 non-cash loss on the Scripps station swap ([S-Q2-26 page:33] "We recognized a loss on disposal of assets of $20 million in the 2026 six-month period").

### Revenue mix

| Line | Q2 2026 | Q2 2025 | 6M 2026 | 6M 2025 | FY2025 | FY2024 | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Core advertising | 357 | 361 | 709 | 705 | 1,452 | 1,490 | S-Q2-26 page:28; S-R-Feb page:2 |
| Political advertising | 83 | 9 | 113 | 22 | 42 | 497 | S-Q2-26 page:28; S-R-Feb page:2 |
| Retransmission consent | 359 | 369 | 698 | 748 | 1,429 | 1,482 | S-Q2-26 page:28; S-R-Feb page:2 |
| Production companies | 26 | 18 | 55 | 45 | 107 | 105 | S-Q2-26 page:28; S-R-Feb page:2 |
| Other | 14 | 15 | 32 | 34 | 65 | 70 | S-Q2-26 page:28; S-R-Feb page:2 |
| Net retransmission revenue (retransmission less network affiliation fees) | 150 | 136 | 292 | 281 | 547 | 550 | S-R-Aug page:3 and page:4; S-R-Feb page:2 |

Drivers stated by the issuer: [S-Q2-26 page:31] "Retransmission consent revenue decreased by $50 million or 7% due to the net effect of a decrease in subscriptions, the transition of one station to independent status, as well as a distribution dispute with a satellite television company removing our stations from its platform from March 2026 through May 1, 2026, offset, in part, by an increase in rates." The 2026 acquisitions contributed 41 of Q2 2026 revenue ([S-R-Aug page:2] "contributed $41 million in total revenue in the second quarter of 2026.").

### Reported balance sheet

| Line (as printed) | Jun 30, 2026 | Dec 31, 2025 | Dec 31, 2024 | Source |
| --- | --- | --- | --- | --- |
| Cash | 176 | 368 | 135 | S-Q2-26 page:2; S-10K page:72 |
| Accounts receivable, net | 193 | 205 | 337 | S-Q2-26 page:2; S-10K page:72 |
| Total current assets | 492 | 656 | 541 | S-Q2-26 page:2; S-10K page:72 |
| Property and equipment, net | 1,522 | 1,509 | 1,577 | S-Q2-26 page:2; S-10K page:72 |
| Broadcast licenses | 5,463 | 5,309 | 5,311 | S-Q2-26 page:2; S-10K page:72 |
| Goodwill | 2,693 | 2,642 | 2,642 | S-Q2-26 page:2; S-10K page:72 |
| Total assets | 10,437 | 10,440 | 10,542 | S-Q2-26 page:2; S-10K page:72 |
| Accrued interest | 150 | 151 | 112 | S-Q2-26 page:2; S-10K page:72 |
| Current portion of long-term debt | - | 2 | 20 | S-Q2-26 page:2; S-10K page:72 |
| Total current liabilities | 517 | 516 | 527 | S-Q2-26 page:2; S-10K page:72 |
| Long-term debt, less current portion and deferred financing costs | 5,808 | 5,742 | 5,601 | S-Q2-26 page:2; S-10K page:72 |
| Deferred income taxes | 1,299 | 1,300 | 1,347 | S-Q2-26 page:2; S-10K page:72 |
| Total liabilities | 7,709 | 7,635 | 7,609 | S-Q2-26 page:2; S-10K page:73 |
| Series A Perpetual Preferred Stock (liquidation value) | 600 | 650 | 650 | S-Q2-26 page:3; S-10K page:73 |
| Total stockholders' equity | 2,128 | 2,155 | 2,283 | S-Q2-26 page:3; S-10K page:73 |

Cash declined by 192 in the first half of 2026 ([S-Q2-26 page:5] "Net (decrease) increase in cash (192 ) 64"). Accrued interest of 150 shows how lumpy the semiannual coupon timing is: interest paid in the six months was 222 against interest expense of 234.

### Reported cash flows

| Line (as printed) | 6M 2026 | 6M 2025 | FY2025 | FY2024 | FY2023 | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Net cash provided by operating activities | 124 | 163 | 289 | 751 | 648 | S-Q2-26 page:5; S-10K page:75 |
| Purchases of property and equipment | (36) | (40) | (108) | (143) | (348) | S-Q2-26 page:5; S-10K page:75 |
| Acquisitions of businesses and licenses, net of cash acquired | (264) | - | - | (1) | (6) | S-Q2-26 page:5; S-10K page:75 |
| Net cash used in investing activities | (290) | (14) | (63) | (28) | (291) | S-Q2-26 page:5; S-10K page:75 |
| Proceeds from borrowings on long-term debt | 70 | 130 | 2,110 | 2,070 | 300 | S-Q2-26 page:5; S-10K page:75 |
| Repayments of borrowings on long-term debt | (13) | (168) | (1,987) | (2,544) | (610) | S-Q2-26 page:5; S-10K page:75 |
| Repurchase of Series A preferred stock | (30) | - | not printed as a separate line | not printed as a separate line | not printed as a separate line | S-Q2-26 page:5 |
| Payment of common stock dividends | (17) | (16) | (33) | (32) | (30) | S-Q2-26 page:5; S-10K page:75 |
| Payment of preferred stock dividends | (27) | (26) | (52) | (52) | (52) | S-Q2-26 page:5; S-10K page:75 |
| Net cash (used in) provided by financing activities | (26) | (85) | 7 | (609) | (397) | S-Q2-26 page:5; S-10K page:76 |
| Net (decrease) increase in cash | (192) | 64 | 233 | 114 | (40) | S-Q2-26 page:5; S-10K page:76 |
| Cash paid for interest | 222 | 230 | 393 | 394 | 419 | S-Q2-26 page:16; S-10K page:94 |

The 2025 operating cash flow of 289 compares with 751 in 2024, a fall the issuer attributes to the 460 decrease in net income and an 89 swing in working capital ([S-10K page:53] "The decrease in cash provided by operating activities was primarily due to the decrease in net income of $460 million; a decrease in cash provided by changes in working capital of $89 million"). The 2026 first half includes a non-cash station exchange of 70 and a 20 deemed contribution on the preferred repurchase, both disclosed as non-cash supplemental items on S-Q2-26 page:5.

### Issuer Adjusted EBITDA reconciliation

| Line (as printed) | Q2 2026 | Q2 2025 | 6M 2026 | 6M 2025 | FY2025 | FY2024 | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net income (loss) | 14 | (56) | (6) | (65) | (85) | 375 | S-R-Aug page:12; S-R-Feb page:11 |
| Depreciation | 34 | 32 | 67 | 66 | 133 | 144 | S-R-Aug page:12; S-R-Feb page:11 |
| Amortization of intangible assets | 21 | 28 | 53 | 57 | 104 | 125 | S-R-Aug page:12; S-R-Feb page:11 |
| Non-cash stock-based compensation | 3 | 5 | 11 | 12 | 22 | 22 | S-R-Aug page:12; S-R-Feb page:11 |
| Impairment of intangible assets / goodwill and other intangible assets | - | 28 | - | 28 | 30 | - | S-R-Aug page:12; S-R-Feb page:11 |
| Loss (gain) on disposal of long-lived assets, net | 20 | (6) | 20 | (8) | (11) | 20 | S-R-Aug page:12; S-R-Feb page:11 |
| Interest expense | 117 | 117 | 234 | 235 | 474 | 485 | S-R-Aug page:12; S-R-Feb page:11 |
| Income tax expense (benefit) | 5 | 21 | (3) | 6 | (28) | 117 | S-R-Aug page:12; S-R-Feb page:11 |
| Adjusted EBITDA | 214 | 169 | 368 | 329 | 670 | 1,162 | S-R-Aug page:12; S-R-Feb page:11 |

The table omits small reconciling lines that sit between the shown ones (miscellaneous income, impairment of investments, early extinguishment of debt); each reconciliation adds to its printed Adjusted EBITDA from the full printed lines (C8). Corporate expense includes transaction-related costs of 7 in Q2 2026 and 11 in the six months, which the issuer shows as a separate line inside operating expenses but does not add back to Adjusted EBITDA ([S-R-Aug page:3] "Transaction Related Expenses"). Adjusted EBITDA is a management measure that appears only in the three releases.

### Debt register at June 30, 2026

| Instrument (as printed) | Rate | Maturity | Security and ranking | Principal Jun 30, 2026 | Principal Dec 31, 2025 | Source |
| --- | --- | --- | --- | --- | --- | --- |
| 2028 1L Term Loan | Term SOFR plus 3.00%, 6.7% at June 30, 2026 | December 1, 2028 | First lien, under the 2019 Senior Credit Facility | 739 | 739 | S-Q2-26 page:15, page:16 |
| 2026 1L Term Loan (called "2024 Term Loan (1L)" in the 10-K) | Not supplied | Repaid April 2, 2026 (10-K: June 4, 2029) | First lien | - | 10 | S-Q2-26 page:15; S-Q1-26 page:12; S-10K page:91 |
| 2029 1L Notes | 10.5% | July 15, 2029 | Senior secured first lien | 1,125 | 1,125 | S-Q2-26 page:14, page:15 |
| 2033 1L Notes | 7.25% | August 15, 2033 | Senior secured first lien | 845 | 775 | S-Q2-26 page:14, page:15 |
| 2032 2L Notes | 9.625% | July 15, 2032 | Senior secured second lien | 1,150 | 1,150 | S-Q2-26 page:14, page:15 |
| 2026 Notes | 5.875% | July 15, 2026 | Senior unsecured | - | 2 | S-Q2-26 page:14, page:15 |
| 2030 Notes | 4.75% | October 15, 2030 | Senior unsecured | 790 | 790 | S-Q2-26 page:14, page:15 |
| 2031 Notes | 5.375% | November 15, 2031 | Senior unsecured | 1,218 | 1,219 | S-Q2-26 page:14, page:15 |
| Total outstanding principal, including current portion | | | | 5,867 | 5,810 | S-Q2-26 page:15 |
| Revolving credit facility, 750 commitment, undrawn | Term SOFR plus 1.75% to 2.75%; commitment fee 0.250% to 0.400% | December 1, 2028 | First lien | - | - | S-Q2-26 page:16; S-10K page:92 |
| Accounts receivable securitization facility, 400 sold | One-month SOFR plus 125 basis points | March 31, 2028 | SPV receivables; outside reported debt | 400 | 400 | S-Q2-26 page:8; S-10K page:61 |
| Series A Perpetual Preferred Stock, liquidation value | Cumulative dividend, 13 per quarter | Perpetual, redeemable | Equity-classified outside stockholders' equity | 600 | 650 | S-Q2-26 page:3, page:5 |

Carrying value: principal less unamortized deferred loan costs of 63 plus unamortized premium of 4 gives 5,808, equal to the printed long-term debt line (C10). Per-instrument carrying amounts are printed as deferred-cost lines, not per instrument, so a per-instrument book value is Not supplied. Guarantors and security are as in CP-0: substantially all subsidiaries guarantee, the first lien, second lien and 2029, 2033 and 2032 notes are secured by substantially all assets excluding real estate ([S-Q2-26 page:35] "are secured by substantially all of our consolidated assets, excluding real estate").

By ranking: principal secured by a first lien is 2,709 (term loan 739 plus 2029 1L 1,125 plus 2033 1L 845), secured by any lien 3,859 (adding the 2L Notes 1,150), and unsecured 2,008 (2030 Notes 790 plus 2031 Notes 1,218); these agree with the covenant schedule ([S-Q2-26 page:37] "Total outstanding principal secured by a first lien $ 2,709").

### Liquidity at June 30, 2026

| Component | June 30, 2026 | December 31, 2025 | Source |
| --- | --- | --- | --- |
| Cash | 176 | 368 | S-Q2-26 page:2 |
| Revolving credit facility commitment | 750 | 750 | S-Q2-26 page:15 |
| Undrawn outstanding letters of credit | (5) | (5) | S-Q2-26 page:15 |
| Borrowing availability under the revolving credit facility | 745 | 745 | S-Q2-26 page:15 |
| Cash plus revolver availability | 921 | 1,113 | Calculated C3 |
| Receivables securitization facility | 400 sold, fully drawn | 400 sold, fully drawn | S-Q2-26 page:8; S-R-Aug page:5 |

Forward uses the issuer states: estimated debt interest of about 465 over the twelve months after June 30, 2026 ([S-Q2-26 page:34] "we estimate that we will make approximately $465 million in debt interest payments over the twelve months immediately following June 30, 2026."), 2026 preferred dividends of 50 and common dividends of 33 and capital expenditures of 120 to 130 in the August guidance (S-R-Aug page:6), and income tax payments of 80 to 100 (S-R-Aug page:6). The interest estimate of 465 plus guided 2026 dividends of 83 is 548, or 77.3% of the 709 of LTM Adjusted EBITDA before any debt reduction (C12). The 745 revolver availability is stated by the issuer as "reflecting only certain outstanding undrawn letters of credit" ([S-R-Aug page:5]).

### Covenants as described by the issuer

| Test | Level | Reported at June 30, 2026 | Status in the sources | Source |
| --- | --- | --- | --- | --- |
| Consolidated First Lien Net Leverage Ratio, incurrence | maximum 3.5 | 2.55 | Reported; not a maintenance test | S-Q2-26 page:37 |
| First lien net leverage, maintenance test and cap | 4.25 while amounts are outstanding under the revolver | 2.55 | Two issuer passages read together (inference): the test applies if revolving loans are outstanding or more than 50 of letters of credit are uncollateralized at quarter end, and the schedule footnote caps the ratio at 4.25 while revolver amounts are outstanding. At June 30, 2026 the revolver is undrawn and letters of credit are 5, so the test is not triggered on the printed figures; a draw outstanding at September 30, 2026 would trigger it | S-Q2-26 page:35, page:37 |
| Consolidated Secured Net Leverage Ratio, incurrence | maximum 5.50; 4.5 for second lien incurrence | 3.71 | Reported; incurrence basket | S-Q2-26 page:37 |
| Consolidated Total Net Leverage Ratio, incurrence | maximum 7.00 | 5.73 | Reported; incurrence basket | S-Q2-26 page:37 |
| Compliance statement | all required covenants | In compliance | Management statement | S-Q2-26 page:16 |

Headroom against the stated levels is derived in C9. These rest on the issuer's Leverage Ratio Denominator of 994, which [S-Q2-26 page:36] describes as "an average amount for the preceding eight quarters then ended." Definitions differ from the Adjusted EBITDA used above, and the credit agreement (amended and restated March 31, 2026) is not supplied; the earlier 10-K worded the maintenance condition differently ([S-10K page:55] "maintenance of the First Lien Leverage Ratio while any amount is outstanding under the Revolving Credit Facility"), so the level and trigger are issuer-described only.

### Claims outside the debt principal

| Claim | Amount | Inside debt figure? | Source |
| --- | --- | --- | --- |
| Receivables securitization, amount sold and derecognized | 400 at June 30, 2026 and December 31, 2025 | No; excluded from reported principal and from net debt | S-Q2-26 page:8; S-R-Aug page:4 |
| Series A perpetual preferred stock, liquidation value | 600 at June 30, 2026 (650 at December 31, 2025) | No; 50 of liquidation value repurchased for 30 on June 30, 2026 | S-Q2-26 page:3, page:15 |
| Letters of credit under the revolver | 5 | Added in covenant total net debt, not in reported principal | S-Q2-26 page:37 |
| Operating lease liabilities | 79 (11 current plus 68 non-current) | No | S-Q2-26 page:2 |
| Programming and network affiliation commitments, minimum payments at December 31, 2025 | 1,724 in total, of which 832 in 2026, 628 in 2027 and 259 in 2028 | No | S-10K page:108 |
| Service and other agreements, minimum payments at December 31, 2025 | 119 | No | S-10K page:108 |
| Pension | Gray Pension Plan funded status: plan assets 73 over projected benefit obligation 57 at December 31, 2025, a net asset of 16; plan termination approved in 2026 with a settlement charge not yet quantified | No | S-10K page:106; S-Q2-26 page:26 |
| Litigation | In re Local TV Advertising Litigation; the consent decree carries no monetary penalty; no amount is accrued or quantified in the sources | No | S-10K page:109 |

Network affiliation agreements expire from mid-2027 through December 31, 2028 ([S-10K page:61] "Our network affiliation agreements expire at various dates from mid-2027 through December 31, 2028."), so the 2027 and 2028 renewal terms coincide with the 2028 debt maturities. The commitments table is as of December 31, 2025; no June 30, 2026 update is in the pack.

### Subsequent events and post-period items

- Acquisitions: first closings with American Spirit Media and WHPM on July 1, 2026, paying 40 and 3; second closings pending regulatory approval for 10 and 1 ([S-Q2-26 page:25] "Total consideration for the acquisition is anticipated to be $50 million.").
- Financing: on June 30, 2026 the company issued 70 of additional 2033 1L Notes at par to fund the 40 first closing and 30 of preferred repurchase ([S-Q2-26 page:15] "On June 30, 2026, we issued $70 million in additional 2033 1L Notes in a private placement transaction."). On July 21, 2026 it repurchased 100 of 2029 1L Notes and 20 of 2031 Notes at par plus accrued interest with cash and revolver borrowings (S-Q2-26 page:25). The revolver draw is not disclosed.
- On August 6, 2026 the board authorized repurchases of up to 250 of debt through December 31, 2027 (S-Q2-26 page:26).
- Guidance for the quarter ending September 30, 2026: revenue 935 to 965 and broadcasting expense 590 to 600, against Q3 2025 actuals of 749 and 542 (S-R-Aug page:5, page:6). This is management forecast, not result.

### Definition review

- Adjusted EBITDA: net income plus depreciation, amortization, non-cash stock compensation, impairments, loss or gain on disposals, interest, early-extinguishment and tax items (S-R-Aug page:12). It is not in any filing and does not add back the 7 and 11 of transaction expenses it reports inside corporate expense.
- Leverage Ratio Denominator: eight-quarter average, with acquisitions and divestitures treated as if completed on July 1, 2024, expected synergies, and unrestricted-subsidiary adjustments; some acquisition data is unaudited and un-reviewed (S-Q2-26 page:36). The June 30, 2026 schedule includes "Adjustments for stations acquired or divested, financings and expected synergies during the eight quarter period 144" (S-Q2-26 page:37).
- Net debt: the release uses principal less cash (5,691, excluding letters of credit); the covenant schedule adds 5 of letters of credit (5,696). Either excludes the securitization and preferred stock.
- LTM here is FY2025 plus six months 2026 less six months 2025; it is not a covenant or pro forma measure.

### Narrative review

- Leverage: on actual earnings, principal debt is 8.28 times Adjusted EBITDA on the last twelve months and 8.67 times in FY2025, against 4.90 times in FY2024. Mechanism: FY2024 carried 497 of political advertising and 1,162 of Adjusted EBITDA; FY2025 carried 42 and 670 while debt rose from 5,690 to 5,810. Implication: the credit is structurally much more levered in off-years than the covenant ratio shows. The covenant total net leverage of 5.73 times uses an eight-quarter average of 994 that still includes 2024 election-year quarters and 144 of acquisition and synergy adjustments, so on the actual LTM Adjusted EBITDA of 709 the same net debt of 5,696 would be 8.03 times (C9).
- Coverage: Adjusted EBITDA covers cash interest 1.84 times on the last twelve months and interest expense 1.50 times. Mechanism: interest expense is about 473 a year on a weighted coupon near the 7.6% average rate the issuer reports ([S-Q2-26 page:33] "Our average total interest rate was 7.6% and 7.4% during the 2026 and 2025 six-month periods, respectively."); a 10.5% first lien tranche and a 9.625% second lien tranche carry the highest coupons. Implication: little earnings cushion above fixed charges before dividends of 87 and capex of 104.
- Cash flow quality: operating cash flow less capex is 146 on the last twelve months, 181 in FY2025 and 608 in FY2024. After preferred and common dividends of 87 it is 59. Mechanism: retransmission consent revenue fell 50 in the first half of 2026 while network affiliation fees fell 61, so net retransmission revenue rose 11. Implication: little free cash for debt reduction without the election-year earnings.
- Liquidity: cash plus revolver availability is 921, down from 1,113 at December 31, 2025, after 264 of acquisition spending in the first half. No principal falls due before December 1, 2028, when 739 of term loan and the revolver mature, followed by 1,125 in 2029. The receivables facility of 400 matures March 31, 2028. Implication: the nearest wall is 2028 and refinancing risk concentrates in 2028 to 2031, which is 3,872 or 66.0% of principal.
- Data quality: audited annual and unaudited interim statements reconcile on the totals checked (C8, C10, C11). Table text is flattened by extraction; no layout error was found in the rows used. One small inconsistency affects the debt table labels (CP-0 X2 and X3).
- Definition risks: Adjusted EBITDA is release-only; the covenant denominator is unaudited in parts; the maintenance covenant text differs between the 10-K and the 10-Q; the credit agreement is not supplied.
- Key gaps: the quarter ended September 30, 2026; the revolver draw after July 21, 2026; credit agreement and indentures; the purchase agreements for pending closings; Q3 2025 Adjusted EBITDA is derived, not printed.

### Readiness for downstream modules

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1A | Sufficient with limitations | Debt register, liquidity, 2026 acquisitions and the political cycle are laid out; ownership detail and purchase agreements remain Not supplied |
| CP-2 | Sufficient with limitations | Leverage, cover and liquidity are on labelled bases; the covenant ratio and Adjusted EBITDA bases must not be mixed; post-June revolver position is Not calculable |
| CP-5 | Sufficient with limitations | Every figure carries a page locator or a calculation id; release-only and derived items are flagged |

### Quality review of claims

| Claim | Material | Lineage | Note |
| --- | --- | --- | --- |
| Debt to LTM Adjusted EBITDA is 8.28 times | Yes | Calculated | Mixes a filing balance with a release-only EBITDA; C3, C4 |
| Covenant total net leverage is 5.73 times | Yes | Directly Sourced | Issuer calculation (S-Q2-26 page:37) |
| Cash plus revolver availability is 921 | Yes | Calculated | Inputs reported; excludes the securitization and post-June borrowing |
| First lien maintenance test and 4.25 times cap read together from two issuer passages | Yes | Analyst Inference over issuer text | Executed credit agreement not supplied; the link between the page 35 trigger and the 4.25 footnote is inferred |
| Q3 2025 Adjusted EBITDA is 162 | No | Calculated | Not printed; derived C2 |
| Headroom to the 4.25 cap is 40.0% of the denominator | Yes | Calculated | Rests on the issuer denominator and an issuer-described level; C9 |

Open quality findings: one MATERIAL, the covenant and credit agreement text is not supplied and the 10-K and 10-Q describe the maintenance trigger differently; one MATERIAL, the post-July 21, 2026 revolver draw and the quarter ended September 30, 2026 are not in the pack; one MINOR, the term loan label differs between the 10-K and the first-quarter 10-Q.

## Calculations

All inputs are USD millions copied from the cited sources. Ratios are rounded half up to two decimals, percentages to one decimal.

| ID | Formula | Inputs and locators | Result |
| --- | --- | --- | --- |
| C1 | LTM = FY2025 + 6M 2026 − 6M 2025 | Revenue 3,095 + 1,607 − 1,554; Adjusted EBITDA 670 + 368 − 329; operating income 392 + 217 − 174; interest expense 474 + 234 − 235; net income −85 + (−6) − (−65); operating cash flow 289 + 124 − 163; purchases of P&E 108 + 36 − 40; cash interest 393 + 222 − 230; political revenue 42 + 113 − 22; dividends paid 52 + 33 + 27 + 17 − 26 − 16 (S-10K page:73, page:75, page:94; S-Q2-26 page:3, page:5, page:16; S-R-Feb page:2, page:11; S-R-Aug page:12) | 3,148; 709; 435; 473; −26; 250; 104; 385; 133; 87 |
| C2 | Q3 2025 Adjusted EBITDA = FY2025 − Q1 2025 − Q2 2025 − Q4 2025; four-quarter cross-check | 670 − 160 − 169 − 179 = 162. Q1 2025 160 and Q1 2026 154 from S-R-May page:2; Q2 2025 169 and Q2 2026 214 from S-R-Aug page:3; Q4 2025 179 from S-R-Feb page:11. Cross-check: 162 + 179 + 154 + 214 | 162; 709, equal to C1 |
| C3 | Liquidity = cash + revolver availability | 176 + 745; 368 + 745; 135 + 674 | 921; 1,113; 809 |
| C4 | Total debt / Adjusted EBITDA; (debt − cash) / Adjusted EBITDA; (debt + preferred + securitization) / Adjusted EBITDA | June 30, 2026: 5,867 / 709; (5,867 − 176) / 709; (5,867 + 600 + 400) / 709. FY2025: 5,810 / 670; (5,810 − 368) / 670; (5,810 + 650 + 400) / 670. FY2024: 5,690 / 1,162; (5,690 − 135) / 1,162; (5,690 + 650 + 300) / 1,162 | 8.28; 8.03; 9.69. 8.67; 8.12; 10.24. 4.90; 4.78; 5.71 |
| C5 | Adjusted EBITDA / cash interest; Adjusted EBITDA / interest expense | 709 / 385; 709 / 473. 670 / 393; 670 / 474. 1,162 / 394; 1,162 / 485 | 1.84; 1.50. 1.70; 1.41. 2.95; 2.40 |
| C6 | Adjusted EBITDA margin | 709 / 3,148; 670 / 3,095; 1,162 / 3,644 | 22.5%; 21.6%; 31.9% |
| C7 | Operating cash flow less purchases of P&E; after dividends | LTM 250 − 104 = 146, less dividends 87 = 59. FY2025 289 − 108 = 181. FY2024 751 − 143 = 608. 6M 2026 124 − 36 = 88 | 146 and 59; 181; 608; 88 |
| C8 | Adjusted EBITDA reconciliation adds to printed total | Q2 2026: 14 + 34 + 21 + 3 + 0 + 20 + 117 + 5 = 214. 6M 2026: −6 + 67 + 53 + 11 + 20 − 8 + 234 − 3 = 368. FY2025: −85 + 133 + 104 + 22 + 30 − 11 + 1 + 20 + 474 + 10 − 28 = 670. Q4 2025: −10 + 34 + 24 + 5 + 2 − 2 − 1 + 20 + 119 + 4 − 16 = 179 (S-R-Aug page:12; S-R-Feb page:11) | 214; 368; 670; 179, equal to printed values |
| C9 | Covenant sensitivity, issuer denominator 994 and net debt as printed | First lien: net debt 2,533 / 4.25 = 596.0 required denominator; (994 − 596.0) / 994 = 40.0%; 4.25 × 994 − 2,533 = 1,691.5 of additional first lien net debt. Headroom in turns: 4.25 − 2.55 = 1.70; 3.5 − 2.55 = 0.95; 5.50 − 3.71 = 1.79; 7.00 − 5.73 = 1.27. Total net debt 5,696 / 7.00 = 813.7, a 18.1% cushion on 994. Net debt 5,696 over LTM Adjusted EBITDA 709 (S-Q2-26 page:37) | 40.0%; 1,691.5; 1.70; 0.95; 1.79; 1.27; 18.1%; 8.03. Not a covenant test: the denominators differ by 285 (994 − 709) |
| C10 | Debt principal, carrying value and coupon check | Principal 739 + 1,125 + 845 + 1,150 + 790 + 1,218 = 5,867; less deferred loan costs 11 + 7 + 6 + 9 + 15 + 15 = 63; plus premium 4 = 5,808. December 31, 2025: 5,810 − (13 + 9 + 7 + 10 + 17 + 15 = 71) + 5 = 5,744, less current 2 = 5,742. Coupon arithmetic: 1,125 × 10.5% + 845 × 7.25% + 1,150 × 9.625% + 790 × 4.75% + 1,218 × 5.375% + 739 × 6.7% = 442.6, or 7.54% of 5,867 (S-Q2-26 page:14 to page:16) | 5,867; 5,808; 5,742; 442.6 and 7.54%. The coupon sum excludes the securitization interest, revolver fees and amortization; it is a check, not a forecast, against the 465 the issuer estimates for twelve months and the 7.6% average rate it reports |
| C11 | Maturity wall and statement checks | 2028 to 2031: 739 + 1,125 + 790 + 1,218 = 3,872, or 3,872 / 5,867 = 66.0%. First half cash roll: 124 − 290 − 26 = −192; 368 − 192 = 176. FY2025 cash roll: 289 − 63 + 7 = 233; 135 + 233 = 368. Quarter revenue: 749 + 792 + 768 + 839 = 3,148 | 3,872 and 66.0%; −192 and 176; 233 and 368; 3,148, all equal to printed or derived values |
| C12 | Interest and dividend load | Estimated twelve-month debt interest 465 (S-Q2-26 page:34) + guided 2026 preferred dividends 50 + common dividends 33 (S-R-Aug page:6) = 548; 548 / 709 | 548; 77.3% |

## Gaps

| Id | Gap | Effect | Action |
| --- | --- | --- | --- |
| G1 | Quarter ended September 30, 2026 not supplied | Leverage, cash and liquidity are as of June 30, 2026 at a November 5, 2026 as-of date | Add the Q3 2026 10-Q and release if filed by the cutoff; otherwise state the staleness |
| G2 | Revolver borrowings used on or after July 21, 2026 are not disclosed | Liquidity and debt after the repurchases of 100 and 20 are Not calculable | Obtain the September 30, 2026 balance sheet |
| G3 | Executed credit agreement, indentures and collateral documents not supplied | Maintenance covenant level and trigger rest on issuer wording; 10-K and 10-Q wording differ | Add the agreement as amended March 31, 2026 |
| G4 | Adjusted EBITDA exists only in releases; Q3 2025 value is derived | EBITDA-based ratios carry management-claim lineage | Label as release-sourced; keep filed GAAP lines alongside |
| G5 | LTM mixes an election off-year half and an on-year half; acquisitions enter only from closing dates | LTM leverage and cover are not a clean run rate | Show FY2024 and FY2025 alongside; do not annualize |
| G6 | Per-instrument carrying amounts, term loan 2026 label and its rate, and December 31, 2024 covenant schedule are not supplied | Facility-level book values and the 2024 covenant ratio cannot be shown | Mark Not supplied; map the term loan labels (CP-0 X2) |
| G7 | Commitments and pension data are at December 31, 2025; June 30, 2026 updates are not in the pack | Programming and affiliation commitments may have changed with the acquisitions | Add the Q3 2026 filing |

## Next module

- CP-1A should use this handoff's debt register, political-cycle and acquisition facts: the 2026 acquisitions and the 2028 to 2031 maturity concentration, the network affiliation expiries from mid-2027 through 2028, and the pending ASM and WHPM closings.
- CP-2 should keep three leverage bases separate: principal over Adjusted EBITDA (8.28 times LTM), the issuer covenant ratios (5.73 total, 2.55 first lien) and the sensitivity including preferred and the securitization (9.69 times).
- CP-5 should check the derived items C2 and C9 and the release-only Adjusted EBITDA against their locators.
