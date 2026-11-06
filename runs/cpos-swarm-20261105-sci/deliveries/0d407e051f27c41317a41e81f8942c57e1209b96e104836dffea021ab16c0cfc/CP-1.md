# CP-1 — Financial base: SERVICE CORP INTERNATIONAL (sci)

## Request

- Issuer: SERVICE CORP INTERNATIONAL (issuer id `sci`; the registrant is "SERVICE CORPORATION INTERNATIONAL", NYSE: SCI), as of 2026-11-05, information cutoff 2026-11-05.
- Current period Q3 2026 (three and nine months ended September 30, 2026); prior period FY2025 (year ended December 31, 2025); reporting currency USD (context). Statements are printed in USD thousands; the releases and MD&A also use USD millions. Both are labelled wherever used.
- Perimeter: the registrant's consolidated statements, which include consolidated merchandise, service and perpetual care trusts. SCI files alone; there is no separate parent, borrower or subsidiary-issuer statement in the sources, so no parent-versus-issuer split arises.
- Scope: reported financial statements, debt and liquidity, covenant as reported, cash flow, claims outside debt, and the latest quarter and events after it, for the credit snapshot. Reported facts are separated from calculations. Calculations are numbered C1 to C12 under `## Calculations`.
- Upstream: the CP-0 readiness handoff rated this module READY_WITH_LIMITATIONS. Its limits are carried forward here: no EBITDA in any source, no credit agreement or indentures, no guarantor detail, no ratings, a maturity-table basis conflict. Where this answer corrects CP-0 it says so under `### Reconciliation to the readiness handoff`.
- Execution: host session; no provider was called.

## Sources

Locators are `page:N` chunks of the pinned `.jsonl` text, not printed page numbers. "10-K" is the FY2025 annual report; "Q1 10-Q", "Q2 10-Q" and "Q3 10-Q" are the 2026 quarterly reports; "Q1 release", "Q2 release" and "Q3 release" are the Exhibit 99.1 earnings releases.

| Source | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_sci-20251231.htm.jsonl | 36f224c032003fbd2390907d9603b5b257c583b876df570b13d8b342fe4f5f00 | Audited FY2025 and FY2024 statements, debt note, leases, pension, covenant table, maturities |
| 10-Q_2026-03-31_sci-20260331.htm.jsonl | e6b5e437aefdd3d93a7df7ee4a72da856eb2c3e8d8864dff282c77ac49311d26 | Q1 2026 statements, debt, covenant, liquidity |
| 10-Q_2026-06-30_sci-20260630.htm.jsonl | 3f4554fa1a62f231e9dd455be55fe862d78b2b61391019d236799268dd70b592 | Q2 2026 and six-month statements, debt, covenant, liquidity |
| 10-Q_2026-09-30_sci-20260930.htm.jsonl | 236742c90fb88a0fc6e3b830a1a819da8579c8436891d794242d5625f7bae113 | Q3 2026 and nine-month statements, debt, covenant, liquidity, segments, subsequent events |
| EX-99.1_2026-04-29_exhibit991q126earningsrele.htm.jsonl | dc7d39675688d257986d7838f6da2271b0d5a328325d0081a47485a7f2412e53 | Q1 2026 release; management claims only |
| EX-99.1_2026-07-29_exhibit991q226earningsrele.htm.jsonl | 8ffbca4fd985e89d67fcf44643913b74684aa9a27e65aeca772948faf99925ff | Q2 2026 release; guidance before the Q3 revision |
| EX-99.1_2026-10-28_exhibit991q326earningsrele.htm.jsonl | d5fe76c2497f82e8e53c22501a405cf8fb7df74cae0b9bd5b7f0b933f384c2b3 | Q3 2026 release; discrete quarter operating cash flow and capital expenditure, cash taxes, revised outlook |
| context | 65d65475c254be68b493ea4436b1695cdda5a813079114b87a550c9ce00dd797 | Run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | a4424fa5ae507987bbabfc0ea081c1e6d0634859958366cc6d6a3e21db770495 | Source readiness; limits and conflicts carried forward and checked against the sources |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported results and liquidity are stable and covenant leverage is reported well inside its maximum. Our own leverage estimate is higher than the reported covenant figure because the covenant definition is not supplied. | Medium | No EBITDA is reported, so every EBITDA ratio is our own estimate and cannot be tied to the covenant. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Trailing leverage on our estimate is 4.15x gross and 4.01x net at September 30, 2026, against a reported covenant ratio of 3.69 and a maximum of 5.00. | Reported headroom is wide, but our estimate cannot be tested against the covenant. | Medium |
| Liquidity is cash plus undrawn revolver capacity of 1,513.7 million US dollars, with no revolver maturity before November 2030. | Near-term maturities are covered, including the April 2027 notes. | High |
| Operating cash flow after capital expenditure rose in the nine months of 2026, and shareholder returns used most of it. | Cash is going to buybacks and dividends rather than debt reduction. | Medium |
| Funeral gross profit fell in the nine months while cemetery gross profit rose, and the outlook for 2026 earnings was lowered after the quarter. | Margin pressure from selling and healthcare costs could slow the coverage gains. | Medium |
| The annual maturity table does not match its own caption, and a stated floating-rate average conflicts with the debt note. | Maturity and interest-sensitivity figures need a basis label before use. | Low |

### Financial base view

The reported financial base for SERVICE CORP INTERNATIONAL supports a stable consolidated credit view at September 30, 2026, with the leverage estimate and the covenant figure kept apart. Revenue for the nine months ended September 30, 2026 was 3,307,004 thousand against 3,197,707 thousand a year earlier, operating income rose to 728,292 thousand from 702,537 thousand, and operating cash flow was 869,288 thousand against 729,860 thousand. Total debt printed on the balance sheet was 5,172,948 thousand against 5,139,817 thousand at December 31, 2025, and cash fell to 172,653 thousand from 243,581 thousand, so net debt rose while the company bought back 318,942 thousand of stock and paid 145,421 thousand of dividends. No EBITDA appears in any source, so all EBITDA ratios below are analyst estimates built from printed operating income and printed depreciation and amortization lines (C1); they are not the covenant measure, which the credit agreement defines and the sources do not. The company reports a covenant leverage ratio of 3.69 against a 5.00 maximum at September 30, 2026. The stack is mostly unsecured senior notes plus a bank term loan and revolver due November 2030, with the revolver largely undrawn, and the one near-term maturity is the 7.500% notes due April 2027. Open items are the maturity-table basis conflict, a floating-rate average that does not match the debt note, and the absence of the credit agreement.

### Source context

| Source | Entity and perimeter | Periods | Statement kind | Units |
| --- | --- | --- | --- | --- |
| 10-K | SERVICE CORPORATION INTERNATIONAL and consolidated subsidiaries, including consolidated trusts | Years ended December 31, 2025, 2024 and 2023; balance sheets at December 31, 2025 and 2024 | Audited (PricewaterhouseCoopers LLP, opinion dated February 12, 2026, 10-K page:68, page:70) | "(In thousands, except per share amounts)", USD (10-K page:71) |
| Q1 10-Q | Same consolidated perimeter | Three months ended March 31, 2026 and 2025; balance sheet at March 31, 2026 and December 31, 2025 | Unaudited | USD thousands (Q1 10-Q page:6) |
| Q2 10-Q | Same | Three and six months ended June 30, 2026 and 2025; balance sheet at June 30, 2026 and December 31, 2025 | Unaudited | USD thousands (Q2 10-Q page:6) |
| Q3 10-Q | Same | Three and nine months ended September 30, 2026 and 2025; balance sheet at September 30, 2026 and December 31, 2025 | Unaudited | USD thousands (Q3 10-Q page:6) |
| Q1, Q2, Q3 releases | Same, issuer presentation | Quarter and year-to-date | Unaudited; GAAP and non-GAAP | USD millions in tables and text; statements in thousands (Q3 release page:3, page:10) |

The cash flow statements are year-to-date. A discrete Q3 2026 flow is the nine-month figure less the six-month figure (C2). The Q3 release prints discrete Q3 operating cash flow and capital expenditure, which agree with C2.

### Financials and credit metrics

| Metric (USD thousands unless stated) | FY2024 | FY2025 | 9M 2025 | 9M 2026 | Q3 2025 | Q3 2026 | LTM to Q3 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenue | 4,186,379 | 4,309,234 | 3,197,707 | 3,307,004 | 1,058,096 | 1,107,262 | 4,418,531 | Reported; 10-K page:71, Q3 10-Q page:6. Q3 2025 and Q3 2026 are the printed three-month columns. LTM is C2 |
| Gross profit | 1,090,657 | 1,140,074 | 828,398 | 832,225 | 265,543 | 272,273 | 1,143,901 | Reported; same pages. LTM is C2 |
| Corporate general and administrative expenses | 139,019 | 166,158 | 132,499 | 116,279 | 38,332 | 30,593 | 149,938 | Reported as costs (printed negative); same pages. LTM is C2 |
| Gains (losses) on divestitures and impairment charges, net | (12,488) | 6,151 | 8,618 | 12,346 | (415) | 11,210 | 9,879 | Reported; same pages. LTM is C2 |
| Operating income | 927,680 | 978,087 | 702,537 | 728,292 | 226,391 | 252,890 | 1,003,842 | Reported; same pages. LTM is C2 |
| Interest expense | 257,771 | 255,372 | 191,237 | 193,710 | 65,683 | 64,993 | 257,845 | Reported as expense (printed negative); same pages. LTM is C2 |
| Net income attributable to common stockholders | 518,648 | 542,614 | 383,218 | 401,909 | 117,473 | 141,276 | 561,305 | Reported; same pages. LTM is C2 |
| Depreciation and amortization | 208,211 | 219,654 | 163,462 | 172,429 | 55,205 | 58,348 | 228,621 | Cash flow line; 10-K page:72, Q3 10-Q page:8. Q3 columns are nine-month less six-month (C2) |
| Amortization of intangibles | 17,222 | 16,370 | 12,353 | 10,465 | 3,912 | 3,427 | 14,482 | Cash flow line; same pages; Q3 columns by C2 |
| EBITDA, analyst estimate (operating income + depreciation and amortization + amortization of intangibles) | 1,153,113 | 1,214,111 | 878,352 | 911,186 | 285,508 | 314,665 | 1,246,945 | Calculated, C1. Not issuer-defined and not the covenant measure; amortization of cemetery property is not added back |
| Net cash provided by operating activities | 944,912 | 942,798 | 729,860 | 869,288 | 252,280 | 296,849 | 1,082,226 | Reported; 10-K page:72, Q3 10-Q page:8. Q3 columns by C2; Q3 release page:3 prints 252.3 and 296.8 million |
| Capital expenditures | 373,659 | 388,553 | 262,818 | 275,047 | 101,617 | 99,454 | 400,782 | Reported as outflow (printed negative); same pages. Q3 columns by C2; Q3 release page:17 prints 101.6 and 99.5 million |
| Operating cash flow less capital expenditures | 571,253 | 554,245 | 467,042 | 594,241 | 150,663 | 197,395 | 681,444 | Calculated, C3. Before corporate headquarters spend, acquisitions and trust items |
| Corporate headquarters spend | 15,448 | 69,898 | 44,942 | 72,419 | 18,183 | 16,085 | 97,375 | Reported investing line; financed by a separate headquarters debt facility (10-K page:45, Q3 10-Q page:27). Q3 columns and LTM by C2 |
| Payments of dividends | 174,282 | 183,571 | 135,977 | 145,421 | 44,848 | 49,058 | 193,015 | Reported financing line; Q3 columns and LTM by C2 |
| Purchase of Company common stock (cash) | 253,733 | 461,015 | 402,093 | 318,942 | 78,070 | 52,565 | 377,864 | Reported financing line; Q3 columns and LTM by C2 |
| Cash interest paid | 241,673 | 252,901 | 159,500 | 162,900 | 33,900 | 34,900 | 256,301 | 10-K page:103; Q3 10-Q page:18 prints 162.9 and 159.5 million. Q3 columns are nine-month less six-month using 128.0 and 125.6 million (Q2 10-Q page:17), rounded to 0.1 million (C4) |
| Cash and cash equivalents (balance) | 218,766 | 243,581 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 172,653 | Reported; 10-K page:72, Q3 10-Q page:7. LTM column holds the September 30, 2026 balance. Part is encumbered (Q3 10-Q page:26) |
| Total debt, carrying value (balance) | 4,835,298 | 5,139,817 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 5,172,948 | Reported; 10-K page:100, Q3 10-Q page:18. Includes finance leases, net of unamortized issuance costs. Gross principal is 5,205,353 at September 30, 2026 (C5) |
| Net debt, analyst estimate (balance) | 4,616,532 | 4,896,236 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 5,000,295 | Calculated, C6: total debt less cash |
| Undrawn bank credit facility capacity (balance) | Not supplied | 1,448,000 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 1,513,700 | Reported in millions: 1,448.0 (10-K page:102) and 1,513.7 (Q3 10-Q page:18). December 31, 2024 capacity is not stated in the sources |
| Total equity (balance) | 1,678,669 | 1,638,841 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 1,575,281 | Reported; 10-K page:72, Q3 10-Q page:7 |
| Total debt / EBITDA (x) | 4.19 | 4.23 | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | 4.15 | Calculated, C7; analyst EBITDA; carrying-value debt |
| Net debt / EBITDA (x) | 4.00 | 4.03 | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | 4.01 | Calculated, C7 |
| EBITDA / cash interest paid (x) | 4.77 | 4.80 | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | 4.87 | Calculated, C8 |
| EBITDA / interest expense (x) | 4.47 | 4.75 | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | n/a (LTM basis) | 4.84 | Calculated, C8 |
| EBITDA margin (%) | 27.5 | 28.2 | 27.5 | 27.6 | 27.0 | 28.4 | 28.2 | Calculated, C9; analyst EBITDA over total revenue |
| Operating cash flow less capital expenditures / total debt (%) | n/a (flow) | 10.8 | n/a (flow) | n/a (flow) | n/a (flow) | n/a (flow) | 13.2 | Calculated, C3 and C10 |
| Covenant leverage ratio as reported (x), maximum 5.00 | Not supplied | 3.67 | n/a (balance) | n/a (balance) | n/a (balance) | n/a (balance) | 3.69 | Reported by the issuer; 10-K page:42, Q3 10-Q page:25. Definition not supplied; not comparable with the analyst ratios |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 4.19 | 4.00 | x | Analyst EBITDA (C1) and carrying-value debt at December 31, 2024; the covenant ratio for this date is not supplied |
| FY2025 | 4.23 | 4.03 | x | Analyst EBITDA and debt at December 31, 2025; the reported covenant ratio is 3.67 on its own definition |
| LTM Q1 2026 | 4.27 | 4.06 | x | FY2025 plus Q1 2026 less Q1 2025 (C2); debt at March 31, 2026; reported covenant ratio 3.68 |
| LTM Q2 2026 | 4.35 | 4.14 | x | FY2025 plus six months 2026 less six months 2025 (C2); debt at June 30, 2026; reported covenant ratio 3.77 |
| LTM Q3 2026 | 4.15 | 4.01 | x | FY2025 plus nine months 2026 less nine months 2025 (C2); debt at September 30, 2026; reported covenant ratio 3.69. Analyst estimate, not the covenant measure |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 4.77 | x | Analyst EBITDA over cash interest paid of 241,673 thousand (10-K page:103) |
| FY2025 | 4.80 | x | Analyst EBITDA over cash interest paid of 252,901 thousand |
| LTM Q1 2026 | 4.71 | x | Cash interest LTM from 32.9 and 29.2 million (Q1 10-Q page:17), rounded to 0.1 million (C4) |
| LTM Q2 2026 | 4.77 | x | Cash interest LTM from 128.0 and 125.6 million (Q2 10-Q page:17) (C4) |
| LTM Q3 2026 | 4.87 | x | Cash interest LTM from 162.9 and 159.5 million (Q3 10-Q page:18) (C4); analyst EBITDA |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| December 31, 2024 | 218.8 | Not supplied: the 2024 capacity is not stated in the supplied sources | US$m | Cash from 10-K page:72; the 10-K gives only letters of credit of 39.0 million for 2024 (page:102) |
| December 31, 2025 | 243.6 | 1448.0 | US$m | Cash 243,581 thousand (10-K page:72); capacity as printed net of 47.0 million letters of credit (10-K page:102) |
| March 31, 2026 | 258.0 | 1448.3 | US$m | Cash 257,959 thousand (Q1 10-Q page:7); capacity as printed (Q1 10-Q page:17) |
| June 30, 2026 | 260.4 | 1383.7 | US$m | Cash 260,411 thousand (Q2 10-Q page:7); capacity as printed (Q2 10-Q page:17) |
| September 30, 2026 | 172.7 | 1513.7 | US$m | Cash 172,653 thousand (Q3 10-Q page:7); capacity as printed net of 1.3 million letters of credit (Q3 10-Q page:18). Part of cash is encumbered (page:26) |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 (as of December 31, 2025) | 56.8 | US$m | 10-K page:101 as printed; basis conflict: the table is captioned as excluding issuance costs but totals the net carrying amount (C5) |
| 2027 (as of December 31, 2025) | 736.9 | US$m | As printed; includes the 7.500% notes due April 2027 and the 4.625% notes due December 2027 (10-K page:100) |
| 2028 (as of December 31, 2025) | 54.3 | US$m | As printed |
| 2029 (as of December 31, 2025) | 814.3 | US$m | As printed; includes the 5.125% notes due June 2029 |
| 2030 (as of December 31, 2025) | 1790.1 | US$m | As printed; includes the term loan, revolver, 3.375% notes due August 2030 |
| 2031 and thereafter (as of December 31, 2025) | 1687.4 | US$m | As printed; includes the 4.000% notes due May 2031, 5.750% notes due October 2032 and the headquarters facility due February 2037 |
| Next twelve months from September 30, 2026 | 195.1 | US$m | Current maturities of long-term debt 195,060 thousand (Q3 10-Q page:7, page:18); includes the 7.500% notes due April 2027, the term loan, mortgage notes, finance leases and a share of unamortized issuance costs. No full maturity table at September 30, 2026 is supplied |

### Reported balance sheet and debt

| Line (as printed, USD thousands) | December 31, 2024 | December 31, 2025 | March 31, 2026 | June 30, 2026 | September 30, 2026 |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 218,766 | 243,581 | 257,959 | 260,411 | 172,653 |
| Total current assets | 377,330 | 411,793 | 447,742 | 449,746 | 360,821 |
| Preneed receivables, net, and trust investments | 6,739,332 | 7,360,793 | 7,264,446 | 7,652,394 | 7,585,365 |
| Cemetery perpetual care trust investments | 2,154,032 | 2,398,613 | 2,365,441 | 2,520,779 | 2,465,566 |
| Goodwill | 2,081,015 | 2,169,055 | 2,173,354 | 2,174,837 | 2,188,137 |
| Total assets | 17,379,438 | 18,654,512 | 18,574,749 | 19,214,493 | 19,093,247 |
| Current maturities of long-term debt | 83,850 | 56,847 | 57,300 | 195,149 | 195,060 |
| Long-term debt | 4,751,448 | 5,082,970 | 5,105,516 | 5,108,016 | 4,977,888 |
| Deferred revenue, net | 1,755,170 | 1,779,266 | 1,799,576 | 1,823,627 | 1,820,555 |
| Deferred receipts held in trust | 5,162,525 | 5,784,398 | 5,709,204 | 6,116,618 | 6,050,706 |
| Care trusts’ corpus | 2,145,112 | 2,381,507 | 2,342,740 | 2,506,248 | 2,448,379 |
| Total equity | 1,678,669 | 1,638,841 | 1,584,949 | 1,537,760 | 1,575,281 |

Locators: 10-K page:72 (December 2024 and 2025); Q1 10-Q page:7; Q2 10-Q page:7; Q3 10-Q page:7. The December 31, 2025 comparative in the Q1 10-Q splits current "Other" into "Income tax receivable 4,999" and "Other 27,552"; their sum, 32,551, equals the 10-K line and the Q2 and Q3 10-Q presentation, so this is a presentation change, not a restatement.

### Debt register

| Instrument (as printed, USD thousands) | December 31, 2025 | March 31, 2026 | June 30, 2026 | September 30, 2026 | Rate or note |
| --- | --- | --- | --- | --- | --- |
| 7.500% Senior Notes due April 2027 | 136,924 | 136,924 | 136,924 | 136,924 | Fixed; current at June 30 and September 30, 2026 |
| 4.625% Senior Notes due December 2027 | 550,000 | 550,000 | 550,000 | 550,000 | Fixed |
| 5.125% Senior Notes due June 2029 | 750,000 | 750,000 | 750,000 | 750,000 | Fixed |
| 3.375% Senior Notes due August 2030 | 850,000 | 850,000 | 850,000 | 850,000 | Fixed |
| 4.000% Senior Notes due May 2031 | 800,000 | 800,000 | 800,000 | 800,000 | Fixed |
| 5.750% Senior Notes due October 2032 | 800,000 | 800,000 | 800,000 | 800,000 | Fixed; described as "unsecured" at issue (10-K page:102) |
| Term Loan due November 2030 | 750,000 | 745,313 | 740,625 | 735,938 | Floating; part of the 2.5 billion US dollar bank credit agreement; guaranteed by a majority of domestic subsidiaries |
| Bank Credit Facility due November 2030 (revolver) | 255,000 | 255,000 | 365,000 | 235,000 | Floating; 1.75 billion US dollar commitment with a 100.0 million sublimit for letters of credit (10-K page:102); bank credit agreement rate 5.65% at September 30, 2026 |
| Corporate Headquarters Debt Facility due February 2037 | 54,766 | 80,848 | 106,620 | 110,852 | Described as a separate construction loan facility for the new headquarters (10-K page:45); commitment size and rate not supplied |
| Obligations under finance leases | 151,061 | 152,981 | 160,112 | 160,547 | Inside total debt |
| Mortgage notes and other debt, maturities through 2050 | 80,142 | 77,957 | 78,200 | 76,092 | 74.3 million of assets pledged as collateral at December 31, 2025 (10-K page:103) |
| Unamortized debt issuance costs | (38,076) | (36,207) | (34,316) | (32,405) | Deducted in the printed total |
| Total debt (printed) | 5,139,817 | 5,162,816 | 5,303,165 | 5,172,948 | Carrying value |
| Weighted average interest rate, total debt | 4.85% | 4.83% | 4.84% | 4.88% | Fixed 4.67%; floating 5.54%, 5.44%, 5.43%, 5.68% in order of the columns |
| Fixed-rate share of total debt | 79% | 79% | 77% | 79% | "Approximately" as printed |
| Total fair value of debt instruments | 4,962,533 | 4,937,331 | 5,070,798 | 4,833,217 | 10-K page:104; Q1 10-Q page:18; Q2 10-Q page:18; Q3 10-Q page:19. Fixed-rate notes at Level 2 market prices; term loan, revolver, headquarters facility and mortgage notes at Level 3 (Q3 10-Q page:20) |

Locators: 10-K page:100; Q1 10-Q page:16 to page:17; Q2 10-Q page:16 to page:17; Q3 10-Q page:17 to page:18 (the first three notes sit on the earlier page of each pair). Senior-note guarantor and security status other than the 2032 notes is not stated; the executed indentures are not supplied.

### Liquidity and covenant

| Item | December 31, 2025 | March 31, 2026 | June 30, 2026 | September 30, 2026 |
| --- | --- | --- | --- | --- |
| Cash and cash equivalents (USD thousands) | 243,581 | 257,959 | 260,411 | 172,653 |
| Revolver commitment (USD millions) | 1,750.0 | 1,750.0 | 1,750.0 | 1,750.0 |
| Revolver drawn (USD millions, from the debt register) | 255.0 | 255.0 | 365.0 | 235.0 |
| Letters of credit issued under the facility (USD millions) | 47.0 | 46.7 | 1.3 | 1.3 |
| Borrowing capacity as printed (USD millions) | 1,448.0 | 1,448.3 | 1,383.7 | 1,513.7 |
| Covenant: leverage ratio, reported actual | 3.67 | 3.68 | 3.77 | 3.69 |
| Covenant: maximum per credit agreement | 5.00 | 5.00 | 5.00 | 5.00 |

Locators: 10-K page:42, page:102; Q1 10-Q page:17, page:24; Q2 10-Q page:17, page:24; Q3 10-Q page:18, page:25. The 1,750.0 commitment is printed in the 10-K (page:44, page:102); the 10-Qs do not restate it, and the printed capacity equals commitment less drawn less letters of credit at each date (C11). The revolver and term loan mature in November 2030, so no facility expires within twelve months of September 30, 2026. During the nine months ended September 30, 2026 the company closed 46.0 million US dollars of letters of credit tied to renewable energy tax credit investments that were fully funded (Q2 10-Q page:17, Q3 10-Q page:18). The unused commitment fee is 0.20%. The only financial covenant described is a maximum leverage ratio; there are "certain dividend and share repurchase restrictions" whose terms are not supplied (Q3 10-Q page:18). Management states a leverage target of 3.5x to 4.0x (Q3 10-Q page:25).

### Segment and operating drivers

| Item (USD thousands) | Q3 2026 | Q3 2025 | 9M 2026 | 9M 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- |
| Funeral revenue | 602,616 | 574,063 | 1,838,004 | 1,804,922 | 2,405,530 | 2,324,200 |
| Funeral gross profit | 104,921 | 99,599 | 349,185 | 369,554 | 495,767 | 465,262 |
| Cemetery revenue | 504,646 | 484,033 | 1,469,000 | 1,392,785 | 1,903,704 | 1,862,179 |
| Cemetery gross profit | 167,352 | 165,944 | 483,040 | 458,844 | 644,307 | 625,395 |
| Gross profit from reportable segments | 272,273 | 265,543 | 832,225 | 828,398 | 1,140,074 | 1,090,657 |

Locators: Q3 10-Q page:20 to page:21; 10-K page:115. Funeral gross profit for the nine months fell and cemetery gross profit rose (calculated growth rates in C12). The 10-Q attributes margin pressure to higher selling compensation, advertising and marketing for preneed sales, and health insurance expense, and lower funeral volume in the nine months (Q3 10-Q page:38, page:40, page:43). In the nine months, comparable funeral services performed fell by 2.7%, and comparable funeral average revenue per service rose (Q3 10-Q page:43). Corporate general and administrative expenses fell by 16.2 million US dollars in the nine months, 6.4 million of it from a prior-year legal settlement and the rest mainly from favorable self-insurance reserve adjustments (Q3 10-Q page:45).

### Claims outside the debt figure

| Claim | Amount | Inside or outside total debt | Locator |
| --- | --- | --- | --- |
| Finance lease obligations | 160,547 thousand at September 30, 2026 | Inside | Q3 10-Q page:18 |
| Operating lease liabilities | Present value 50,786 thousand and fixed payments 65,629 thousand at December 31, 2025; September 30, 2026 not supplied | Outside | 10-K page:105 to page:106 |
| Unfunded retirement plans (frozen) | Benefit obligation 12,284 thousand at December 31, 2025; no plan assets; September 30, 2026 not supplied | Outside | 10-K page:113 |
| Surety bonds | 498.3 million US dollars at September 30, 2026; the underlying obligations are recorded in deferred revenue | Outside (contingent) | Q3 10-Q page:28 |
| Letters of credit | 1.3 million US dollars at September 30, 2026 | Outside debt; reduces revolver capacity | Q3 10-Q page:18 |
| Preneed deferred revenue | 1,820,555 thousand | Outside; operating liability | Q3 10-Q page:7 |
| Deferred receipts held in trust and care trusts’ corpus | 6,050,706 and 2,448,379 thousand | Outside; matched by consolidated trust assets of 7,585,365 and 2,465,566 thousand | Q3 10-Q page:7 |
| Unfunded private equity commitments of the trusts | 532.6 million US dollars | Outside; "would be funded by the assets of the trusts" | Q3 10-Q page:15 |
| Self-insurance reserves | 113.5 million US dollars | Outside | Q3 10-Q page:22 |
| Unclaimed property audits, about forty states | Unquantified; "unable to reasonably estimate" the loss | Outside; contingent | Q3 10-Q page:22 |
| Tax credit equity investments | Unamortized 1.1 million US dollars at September 30, 2026; unfunded commitment 40.8 million US dollars at December 31, 2025; September 30, 2026 unfunded amount not stated | Outside | Q3 10-Q page:17 |
| Share repurchase authorization remaining | 498.8 million US dollars; discretionary | Outside | Q3 10-Q page:20 |

A search of all seven sources for factoring, supply-chain finance, securitization and consent-decree language found no hits. Purchase commitments other than the items above are not disclosed in the sources read.

### Latest quarter and after

- Q3 2026 revenue was 1,107,262 thousand against 1,058,096 thousand; operating income was 252,890 thousand against 226,391 thousand, including a divestiture and impairment gain of 11,210 thousand against a loss of 415 thousand (Q3 10-Q page:6). Operating income excluding that line rose by 6.6%, and the gross margin fell to 24.6% from 25.1% (C12).
- Financing in Q3: the revolver balance fell from 365,000 to 235,000 thousand, the term loan from 740,625 to 735,938 thousand, and the headquarters facility rose from 106,620 to 110,852 thousand (debt register). Nine-month debt issuance was 586.1 million US dollars and payments 570.7 million (Q3 10-Q page:19). The Q3 10-Q debt note lists no senior note issuance or redemption in the nine months of 2026.
- Shareholder returns: the company repurchased 658,460 shares in Q3 (Q3 10-Q page:52) and 4,009,333 shares for 317.6 million US dollars in the nine months (page:20). The quarterly dividend was 0.36 US dollars per share in Q3 (page:26). The release says 464 million US dollars was returned year to date (Q3 release page:3).
- After the quarter: "Subsequent to September 30, 2026, we repurchased 232,968 shares for $18.2 million" (Q3 10-Q page:20). Shares outstanding were 135,907,343 at October 29, 2026 (page:1).
- Outlook (issuer claim): on October 28, 2026 the company set fourth quarter adjusted earnings per share at 1.10 to 1.20 US dollars and full-year adjusted earnings per share at 3.94 to 4.04 US dollars, citing lower funeral volumes than anticipated and higher healthcare, selling and advertising costs (Q3 release page:4). The July 29, 2026 range was 4.10 to 4.30 US dollars (Q2 release page:4), so the full-year range was lowered. The operating cash flow outlook midpoint of 1,085 million US dollars and maintenance capital expenditure of 335 million were unchanged, implying adjusted free cash flow of about 750 million (Q3 release page:4 to page:5).
- Apart from the repurchases and the outlook, the sources report no acquisition, debt issuance, rating action, litigation outcome or disaster event dated after September 30, 2026. Nothing dated after October 29, 2026 is supplied, so events from October 30, 2026 to the cutoff are Not supplied.

### Reconciliation to the readiness handoff

- Agreed: no EBITDA in any source; the executed credit agreement, indentures, guarantor detail and ratings are not supplied; the maturity table (10-K page:101) totals 5,139,817 thousand, the net carrying amount, although captioned as excluding issuance costs. That conflict is carried into the maturity chart above.
- Corrected: the readiness handoff listed discrete Q2 and Q3 cash flows as not printed. The Q3 release prints discrete Q3 net cash provided by operating activities (296.8 and 252.3 million US dollars) and total capital expenditures (99.5 and 101.6 million) on page:3 and page:17. These agree with C2. Other discrete Q3 cash flow lines are not printed and are derived.
- New conflict: the Q3 10-Q says the floating-rate debt "carried a weighted average rate of 4.1%, which is over 230 basis points lower than the weighted average rate for our floating rate debt in the prior year" (page:46). The debt note shows a floating-rate weighted average of 5.68% at September 30, 2026 and 5.54% at December 31, 2025 (page:18), and the bank credit agreement rate of 5.65% (page:18). The two cannot both describe the same population on a period-end basis. The sources do not explain it and no derivative or hedge is disclosed. This answer uses the debt-note rates and treats the 4.1% as unresolved.
- Note: the December 31, 2025 liquidity reading in the readiness handoff matches the 10-K (1,448.0 million).

## Calculations

All inputs are printed figures cited above, in USD thousands unless stated. Results are rounded as shown.

- **C1, EBITDA estimate.** Operating income + Depreciation and amortization + Amortization of intangibles (the latter two from the cash flow statement; the segment note shows them as separate lines, 10-K page:116). FY2024: 927,680 + 208,211 + 17,222 = 1,153,113. FY2025: 978,087 + 219,654 + 16,370 = 1,214,111. 9M 2025: 702,537 + 163,462 + 12,353 = 878,352. 9M 2026: 728,292 + 172,429 + 10,465 = 911,186. Amortization of cemetery property (FY2025 104,262; 9M 2026 74,592) is a cost of cemetery sales and is not added back. No divestiture gains, impairments or restructuring are adjusted, so this is a reported-basis estimate and not issuer-defined.
- **C2, LTM and discrete quarters.** LTM Q3 2026 = FY2025 + 9M 2026 - 9M 2025. Revenue: 4,309,234 + 3,307,004 - 3,197,707 = 4,418,531. Gross profit: 1,140,074 + 832,225 - 828,398 = 1,143,901. Corporate G&A: 166,158 + 116,279 - 132,499 = 149,938. Divestiture gains: 6,151 + 12,346 - 8,618 = 9,879. Operating income: 978,087 + 728,292 - 702,537 = 1,003,842. Interest expense: 255,372 + 193,710 - 191,237 = 257,845. Net income attributable: 542,614 + 401,909 - 383,218 = 561,305. D&A: 219,654 + 172,429 - 163,462 = 228,621. Intangibles: 16,370 + 10,465 - 12,353 = 14,482. EBITDA: 1,214,111 + 911,186 - 878,352 = 1,246,945. Operating cash flow: 942,798 + 869,288 - 729,860 = 1,082,226. Capex: 388,553 + 275,047 - 262,818 = 400,782. HQ: 69,898 + 72,419 - 44,942 = 97,375. Dividends: 183,571 + 145,421 - 135,977 = 193,015. Buybacks: 461,015 + 318,942 - 402,093 = 377,864. Discrete Q3 = nine months less six months: D&A 172,429 - 114,081 = 58,348 and 163,462 - 108,257 = 55,205; intangibles 10,465 - 7,038 = 3,427 and 12,353 - 8,441 = 3,912; operating cash flow 869,288 - 572,439 = 296,849 and 729,860 - 477,580 = 252,280; capex 275,047 - 175,593 = 99,454 and 262,818 - 161,201 = 101,617; HQ 72,419 - 56,334 = 16,085 and 44,942 - 26,759 = 18,183; dividends 145,421 - 96,363 = 49,058 and 135,977 - 91,129 = 44,848; buybacks 318,942 - 266,377 = 52,565 and 402,093 - 324,023 = 78,070. Q3 EBITDA: 252,890 + 58,348 + 3,427 = 314,665 and 226,391 + 55,205 + 3,912 = 285,508. LTM Q1 and Q2 2026 use the same pattern with the Q1 and Q2 10-Q columns: LTM Q1 EBITDA 1,214,111 + (243,814 + 56,686 + 3,656) - (251,687 + 54,126 + 4,200) = 1,208,254; LTM Q2 EBITDA 1,214,111 + (475,402 + 114,081 + 7,038) - (476,146 + 108,257 + 8,441) = 1,217,788.
- **C3, operating cash flow less capex.** FY2024 944,912 - 373,659 = 571,253. FY2025 942,798 - 388,553 = 554,245. 9M 2025 729,860 - 262,818 = 467,042. 9M 2026 869,288 - 275,047 = 594,241. Q3 2025 252,280 - 101,617 = 150,663. Q3 2026 296,849 - 99,454 = 197,395. LTM 1,082,226 - 400,782 = 681,444. After the nine-month dividends and buybacks of 145,421 + 318,942 = 464,363, the 9M 2026 figure is 594,241 - 464,363 = 129,878, before the headquarters spend of 72,419 and acquisitions of 73,262.
- **C4, LTM cash interest** (USD millions as printed to one decimal): FY2025 252.901 + 9M 2026 162.9 - 9M 2025 159.5 = 256.301; LTM Q1 252.901 + 32.9 - 29.2 = 256.601; LTM Q2 252.901 + 128.0 - 125.6 = 255.301. Discrete Q3: 162.9 - 128.0 = 34.9 and 159.5 - 125.6 = 33.9.
- **C5, debt basis.** Sum of printed components at December 31, 2025 before issuance costs: 136,924 + 550,000 + 750,000 + 850,000 + 800,000 + 800,000 + 750,000 + 255,000 + 54,766 + 151,061 + 80,142 = 5,177,893. Less 38,076 = 5,139,817, equal to the printed total debt and to the maturity-table total. At September 30, 2026: 136,924 + 550,000 + 750,000 + 850,000 + 800,000 + 800,000 + 735,938 + 235,000 + 110,852 + 160,547 + 76,092 = 5,205,353; less 32,405 = 5,172,948. Maturity table sum: 56,847 + 736,928 + 54,264 + 814,320 + 1,790,101 + 1,687,357 = 5,139,817. The caption says it excludes issuance costs, so either the caption or the amounts are mislabelled; which buckets carry the 38,076 reduction is Not determinable.
- **C6, net debt.** Carrying total debt less cash: FY2024 4,835,298 - 218,766 = 4,616,532; FY2025 5,139,817 - 243,581 = 4,896,236; March 31, 2026 5,162,816 - 257,959 = 4,904,857; June 30, 2026 5,303,165 - 260,411 = 5,042,754; September 30, 2026 5,172,948 - 172,653 = 5,000,295. All cash is treated as available, which overstates it, because part is encumbered.
- **C7, leverage.** Total debt / EBITDA: FY2024 4,835,298 / 1,153,113 = 4.19; FY2025 5,139,817 / 1,214,111 = 4.23; LTM Q1 5,162,816 / 1,208,254 = 4.27; LTM Q2 5,303,165 / 1,217,788 = 4.35; LTM Q3 5,172,948 / 1,246,945 = 4.15. Net debt / EBITDA: 4,616,532 / 1,153,113 = 4.00; 4,896,236 / 1,214,111 = 4.03; 4,904,857 / 1,208,254 = 4.06; 5,042,754 / 1,217,788 = 4.14; 5,000,295 / 1,246,945 = 4.01. Using gross principal of 5,205,353 at September 30, 2026 gives 5,205,353 / 1,246,945 = 4.17. The reported covenant ratio (3.67 to 3.77) is lower than every analyst ratio here; the definitional cause is Not determinable.
- **C8, cover.** EBITDA / cash interest paid: 1,153,113 / 241,673 = 4.77; 1,214,111 / 252,901 = 4.80; 1,208,254 / 256,601 = 4.71; 1,217,788 / 255,301 = 4.77; 1,246,945 / 256,301 = 4.87. EBITDA / interest expense: 1,153,113 / 257,771 = 4.47; 1,214,111 / 255,372 = 4.75; 1,246,945 / 257,845 = 4.84.
- **C9, EBITDA margin.** FY2024 1,153,113 / 4,186,379 = 27.5%; FY2025 1,214,111 / 4,309,234 = 28.2%; 9M 2025 878,352 / 3,197,707 = 27.5%; 9M 2026 911,186 / 3,307,004 = 27.6%; Q3 2025 285,508 / 1,058,096 = 27.0%; Q3 2026 314,665 / 1,107,262 = 28.4%; LTM 1,246,945 / 4,418,531 = 28.2%.
- **C10, cash flow to debt.** 554,245 / 5,139,817 = 10.8%; 681,444 / 5,172,948 = 13.2%.
- **C11, liquidity check.** Commitment less drawn less letters of credit equals the printed capacity: December 31, 2025 1,750.0 - 255.0 - 47.0 = 1,448.0; March 31, 2026 1,750.0 - 255.0 - 46.7 = 1,448.3; June 30, 2026 1,750.0 - 365.0 - 1.3 = 1,383.7; September 30, 2026 1,750.0 - 235.0 - 1.3 = 1,513.7. Liquidity at September 30, 2026 is 172.7 + 1,513.7 = 1,686.4 million US dollars (cash 172,653 thousand, part of it encumbered). Floating-rate instruments (term loan, revolver, headquarters facility) at September 30, 2026: 735,938 + 235,000 + 110,852 = 1,081,790, or 20.8% of gross principal 5,205,353, consistent with the printed "approximately 79%" fixed; which instruments are floating is an inference from the Level 3 classification and rates, and the sources do not list them.
- **C12, growth rates and margins.** Revenue Q3 1,107,262 / 1,058,096 - 1 = 4.6%; 9M 3,307,004 / 3,197,707 - 1 = 3.4%. Operating income Q3 252,890 / 226,391 - 1 = 11.7%; 9M 728,292 / 702,537 - 1 = 3.7%. Operating income excluding divestiture and impairment line: Q3 2026 252,890 - 11,210 = 241,680 against 226,391 + 415 = 226,806, up 6.6%; 9M 2026 728,292 - 12,346 = 715,946 against 702,537 - 8,618 = 693,919, up 3.2%. Gross margin Q3 272,273 / 1,107,262 = 24.6% against 265,543 / 1,058,096 = 25.1%; 9M 832,225 / 3,307,004 = 25.2% against 828,398 / 3,197,707 = 25.9%. Funeral gross profit 9M 349,185 / 369,554 - 1 = -5.5%; cemetery 483,040 / 458,844 - 1 = 5.3%; Q3 funeral 104,921 / 99,599 - 1 = 5.3%; Q3 cemetery 167,352 / 165,944 - 1 = 0.8%. Operating cash flow 9M 869,288 / 729,860 - 1 = 19.1%.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No EBITDA or adjusted EBITDA in any source; ratios here use a reported-basis estimate (C1) | High | CP-2 | Supply the covenant compliance certificate or credit agreement definition; keep the reported 3.69 against 5.00 as an attributed figure |
| Credit agreement, indentures, guarantor list and security detail for the notes not supplied | High | CP-2 | Supply executed documents |
| Maturity-table basis conflicts with its caption (10-K page:100 and page:101); no maturity table at September 30, 2026 | Medium | CP-2 | Confirm the basis from the filed HTML or XBRL; label the ladder as printed |
| Floating-rate average of 4.1% conflicts with the debt note rate of 5.68% (Q3 10-Q page:46 against page:18) | Medium | CP-2 | Ask the issuer or check the filed HTML; use debt-note rates meanwhile |
| Headquarters debt facility commitment, rate and security not supplied | Low | CP-2 | Supply the facility terms; at September 30, 2026 110,852 thousand is drawn |
| December 31, 2024 revolver capacity, and September 30, 2026 operating lease and pension balances not supplied | Low | CP-1, CP-2 | Use the dates that are supplied; label the rest Not supplied |
| Part of cash is encumbered (Canada and minimum operating cash, Q3 10-Q page:26); the amount is not given | Medium | CP-2 | Treat net debt as a lower bound on leverage relief |
| Unclaimed property audits in about forty states are unquantified | Medium | CP-2 | Carry as a contingency |
| Cash taxes jumped in 2025 (income taxes paid 140,065 against 20,820 thousand in 2024, 10-K page:97) and 9M 2026 cash taxes were 65.3 against 114.3 million (Q3 release page:17); the tax timing makes single-period cash flow comparisons unreliable | Low | CP-1, CP-2 | Compare on an LTM basis only |
| Text extraction only; page chunks are not printed page numbers; no XBRL | Low | CP-5 | Check flagged tables against the filed HTML |

## Next module

- CP-1A: describe the business with the segment table above; carry the lowered 2026 earnings outlook and the cause stated by the issuer; label anything after October 29, 2026 as Not supplied.
- CP-2: use the debt register and the liquidity table as the starting capital structure; keep finance leases inside debt and operating leases, pensions, surety bonds and trust balances outside; use the reported covenant ratio only as attributed; state the maturity-table basis conflict wherever the wall is shown; flag the floating-rate conflict.
- CP-5: all figures above are traceable to `page:N` locators; the analyst EBITDA and every ratio built on it are calculations, not source facts.
