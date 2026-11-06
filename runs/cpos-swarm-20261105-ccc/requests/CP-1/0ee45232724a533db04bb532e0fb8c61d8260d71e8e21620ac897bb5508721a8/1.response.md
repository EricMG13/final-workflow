## Request

Issuer: CCC Intelligent Solutions Holdings Inc. (ticker CCC; consolidated reporting entity; borrower under the 2021 Credit Agreement is its indirect wholly owned subsidiary CCC Intelligent Solutions Inc.). As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit_snapshot, host mode, no provider call.

Scope: financial statements and credit metrics for FY2024 and FY2025 (audited), Q1, Q2 and Q3 2026 (unaudited, three-month columns), nine months 2026 (9M 2026) and last-twelve-months to 2026-09-30 (LTM Q3 2026, built from reported columns). Reporting currency USD. Statement amounts are in USD thousands as printed; the liquidity and maturity chart tables are in US$m (thousands divided by 1,000, no rounding beyond the stated decimals). Leverage and cover are in x. Current period q3-2026; prior period fy-2025, per the run context. The context supplies no ratings, quotes, peers, deal terms or assumptions, and none is used.

This handoff feeds CP-1A, CP-2 and CP-5. It makes no covenant-compliance statement, no pro forma statement for the pending merger and no valuation statement.

## Sources

Issuer sources relied on (exact name and sha256 pinned by CP-OS). A locator `page:N` is the extracted chunk N of that source, not the printed page.

| Source | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_ccc-20251231.htm.jsonl | 59a1556351f7a7f353f0b9618ee7cf495b7ba17767f7cd6a5a0ded1621642fde | Audited FY2025, FY2024 and FY2023 statements; Note 15 debt; Adjusted EBITDA reconciliation; market risk; commitments |
| 10-Q_2026-03-31_ccc-20260331.htm.jsonl | 39b288dd8e81ee0fdda5870870b9bea592f01074d7af9763a85c294be03c88d4 | Q1 2026 and Q1 2025 statements, 2026-03-31 balance sheet, debt, Adjusted EBITDA |
| 10-Q_2026-06-30_ccc-20260630.htm.jsonl | eda11b6dbfa4719333004f220abf5cdc5bfe0e2df75fd21d1a6f0733cf5d331c | Q2 2026 and six-month statements, 2026-06-30 balance sheet, debt, Adjusted EBITDA |
| 10-Q_2026-09-30_ccc-20260930.htm.jsonl | 0c88b8b197fab954d1c3ff71345c0e05e9f10d1f3510025ad9548d8138ae8407 | Q3 2026 and nine-month statements, 2026-09-30 balance sheet, Notes 14 to 16, 25, MD&A liquidity and non-GAAP measures, KPIs |
| EX-99.1_2026-04-30_ccc-ex99_1.htm.jsonl | ae3848deb91163ab500fd7932cb28c39aab5b44b52f0fa623f872d5f723093a6 | Q1 2026 release: free cash flow, total debt statement (attributed management) |
| EX-99.1_2026-07-30_ccc-ex99_1.htm.jsonl | a2b1e7ba00fedac3bf32b37f93a1dd3c6ccb1a88c16f25d3354731a4f4c2fb7c | Q2 2026 release: free cash flow, total debt statement |
| EX-99.1_2026-10-29_ccc-ex99_1.htm.jsonl | 6ea0ae7480d6fb5cada60e78aef6508a9d3b3ddbb6b2caecfdee6ff746b5c13f | Q3 2026 release: free cash flow, merger summary, guidance suspended |

Run context: `context`, sha256 b5d08a6a26eac33af88a5d18c45e48ca178e243a383ecb998014ab0c163dd60f (settings only, not issuer evidence).

Supplied handoff consumed: CP-0, sha256 6b0d66d9bd08d88f5e3acbbee3edf3515d663baf1c742e23d09d59c87c891429.

Carried forward from CP-0: the filings control over the releases; FY2025 is audited and the 2026 periods are unaudited; the 2021 Credit Agreement and its amendments and the merger agreement are not in the pack, so covenant definitions and post-deal financing are Not supplied; Q4 2025 is not reported as a discrete quarter; debt must be taken from the 10-K and 10-Q debt tables, not from release headlines; the guarantor name and covenant wording differ between filings and are quoted as printed. Corrections to CP-0 found while building this module are listed in `### Corrections to CP-0`.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Gross leverage is 2.64x and net leverage 2.22x on LTM Adjusted EBITDA of USD 484,946 thousand, with cash of USD 202,926 thousand and an undrawn revolver. After deducting share-based pay, gross leverage is 3.58x. | Medium | Adjusted EBITDA adds back share-based pay, covenant definitions are not in the pack, and the pending take-private leaves the post-deal debt unknown. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Net debt fell from 1,179,798 at FY2025 to 1,078,290 at Q3 2026 as cash rose to 202,926 and 9,774 of principal was repaid. | Deleveraging so far comes mostly from cash build, with debt reduced only by scheduled amortisation. | High |
| Adjusted EBITDA adds back 126,687 of share-based pay and related payroll tax over the LTM period; leverage after that deduction is 3.58x gross and 3.01x net. | Headline leverage depends on the add-back, and the definition lenders use is not supplied. | Medium |
| Adjusted EBITDA covers cash interest 6.69x over the LTM period, and free cash flow is 311,375. | Debt service is well covered, and swaps fix 750.0 million of the term loan at about 3.94% through 2027-07-31. | Medium |
| Scheduled amortisation is 13,033 a year until a balloon of 1,212,792 in 2032, and the 250.0 million revolver is undrawn with 249.0 million available. | There is no near-term maturity wall, but the pending merger may change the debt. | Medium |

### Financial base view

View: the financial base is sufficient and consistent for a bounded credit snapshot, with the restrictions listed below. Every statement figure used here is taken from a filed statement or note; the three discrete 2026 quarters are the reported three-month columns, FY2025 and FY2024 are audited, and LTM Q3 2026 is calculated as FY2025 plus nine months 2026 less nine months 2025 (calculation C1). The reported statements reconcile: revenue, operating cash flow, free cash flow and Adjusted EBITDA for the quarters add to the nine-month columns within a difference of at most 2 thousand (C9), and the term loan carrying amount ties to its components. The capital structure is one senior secured term loan with 1,281,216 principal at 2026-09-30 and an undrawn 250.0 million revolver; the only other funded obligation is a 27,562 promissory note issued by CCC Cayman, the parent of the China subsidiaries, without recourse to the registrant. The strongest contrary points are these. First, headline leverage is built on Adjusted EBITDA, which adds back share-based compensation and related payroll tax of 126,687 over the LTM period; on the lower base gross leverage is 3.58x, not 2.64x. Second, the lender covenant is a springing leverage test that applies only when revolver borrowings reach the 35% threshold (the filings word it as "a minimum of 35.0%" in 10-K page:81 and as exceeding 35% of commitments in 10-K page:161), and its ratio definition is not in the pack, so headroom is Not calculable. Third, the merger agreed on 2026-10-14 is a subsequent event; the existing term loan may be repaid or kept at closing, and the pack does not say which, so any forward leverage is Not calculable. What can proceed: reported-fact summaries, LTM and discrete-quarter metrics, liquidity and maturity profile, and the leverage and cover ratios as issuer-basis measures. What is restricted: covenant compliance or headroom, pro forma capital structure, and any Q4 2025 discrete figure not derived by difference.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 1.95 | 0.95 | x | Term Loan principal 776,000 at 2024-12-31 over issuer Adjusted EBITDA 397,377 (C3); net of cash and cash equivalents 398,983; audited; issuer-defined EBITDA, not covenant EBITDA |
| FY2025 | 2.96 | 2.71 | x | Principal 1,290,990 over Adjusted EBITDA 436,043 (C3); net of cash 111,192; year-end debt includes the 300,000 incremental term loan of 2025-12-12, so this ratio is year-end debt over full-year earnings |
| LTM Q1 2026 | 2.82 | 2.74 | x | Principal 1,287,732 over LTM Adjusted EBITDA 457,164 (C2, C3); net of cash 36,900; LTM built from reported columns |
| LTM Q2 2026 | 2.77 | 2.52 | x | Principal 1,284,474 over LTM Adjusted EBITDA 464,527 (C2, C3); net of cash 115,857 |
| LTM Q3 2026 | 2.64 | 2.22 | x | Principal 1,281,216 over LTM Adjusted EBITDA 484,946 (C1, C3); net of cash 202,926; excludes the 27,562 non-recourse subsidiary note; on Adjusted EBITDA less share-based pay and related payroll tax the ratios are 3.58x and 3.01x (C5); not a covenant ratio and no pro forma for the merger |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 6.32 | x | Adjusted EBITDA 397,377 over cash paid for interest 62,898 (C4); cash interest excludes swap settlements, which are recorded in other income |
| FY2025 | 6.54 | x | Adjusted EBITDA 436,043 over cash paid for interest 66,704 (C4) |
| LTM Q1 2026 | 6.59 | x | LTM Adjusted EBITDA 457,164 over LTM cash interest 69,354 (C2, C4) |
| LTM Q2 2026 | 6.53 | x | LTM Adjusted EBITDA 464,527 over LTM cash interest 71,168 (C2, C4) |
| LTM Q3 2026 | 6.69 | x | LTM Adjusted EBITDA 484,946 over LTM cash interest 72,448 (C1, C4); on Adjusted EBITDA less share-based pay and related payroll tax the ratio is 4.95x (C5); swap settlements paid of 1.5 million for 9M 2026 are in other income and not in cash interest |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 398.983 | 249.3 | US$m | Cash and cash equivalents at 2024-12-31 (10-K page:129); revolver 250.0 commitment less a 0.7 standby letter of credit, available 249.3 (10-K page:160); no restricted cash line is printed |
| FY2025 | 111.192 | 248.9 | US$m | Cash at 2025-12-31 (10-K page:129); 250.0 commitment less a 1.1 standby letter of credit (10-K page:160) |
| Q1 2026 | 36.900 | 249.0 | US$m | Cash at 2026-03-31 (10-Q Q1 page:4); availability 249.0 after letters of credit of 1.0 (10-Q Q1 page:20) |
| Q2 2026 | 115.857 | 249.0 | US$m | Cash at 2026-06-30 (10-Q Q2 page:4); availability 249.0 (10-Q Q2 page:17) |
| Q3 2026 | 202.926 | 249.0 | US$m | Cash at 2026-09-30 (10-Q Q3 page:4); revolver undrawn, 250.0 commitment less 1.0 of standby letters of credit; total of cash and availability 451.926 (C7); the revolver matures 2029-09-23 with a springing maturity of 2028-06-22 if more than 234.0 of term loan remains; borrowing is subject to the merger agreement's debt incurrence limits (10-Q Q3 pages:45, 52) |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q4 2026 | 3.259 | US$m | Remaining 2026 scheduled term loan amortisation at 2026-09-30: current portion 13,033 less 9,774 paid in 9M 2026 (C6) |
| 2027 | 13.033 | US$m | Scheduled quarterly amortisation, 10-Q Q3 page:18 and current portion 13,033 (10-Q Q3 page:19) (C6) |
| 2028 | 13.033 | US$m | Scheduled amortisation (C6); revolver springing maturity 2028-06-22 applies only if more than 234.0 of term loan remains, and the revolver is undrawn |
| 2029 | 13.033 | US$m | Scheduled amortisation (C6); the undrawn 250.0 revolver expires 2029-09-23 and is not debt maturing |
| 2030 | 13.033 | US$m | Scheduled amortisation (C6) |
| 2031 | 13.033 | US$m | Scheduled amortisation through 2031-12-31 (C6) |
| 2032 | 1,212.792 | US$m | Balloon due 2032-01-23 (10-Q Q3 page:18), calculated as principal 1,281.216 less the preceding payments (C6); the 10-K table at 2025-12-31 prints a single 2030 bucket of 1,238.858, which equals 2030 and 2031 amortisation plus this balloon (C6) |
| Undated | Not supplied: maturity is contingent on funds being available to redeem the Series A preferred stock, not a calendar date | US$m | The 27.562 promissory note at CCC Cayman (10-Q Q3 page:20) is non-recourse to the registrant, accrues 12.0% per annum paid in kind and is not in the funded debt total |

### Financials and credit metrics

| Metric | Q3 2026 | 9M 2026 | LTM Q3 2026 | FY2025 | FY2024 | Basis and source |
| --- | --- | --- | --- | --- | --- | --- |
| Revenue (USD thousands) | 294,093 | 861,298 | 1,139,163 | 1,057,001 | 944,800 | Reported (10-Q Q3 page:5; 10-K page:129); LTM calculated, C1 |
| Revenue growth versus prior-year period (%) | 10.1 | 10.5 | Not calculable: needs LTM to 2025-09-30 | 11.9 | 9.1 | Calculated, C10; FY2024 over FY2023 revenue 866,378 (10-K page:129) |
| Operating income (USD thousands) | 57,387 | 153,837 | 203,933 | 93,842 | 80,105 | Reported (10-Q Q3 page:5; 10-K page:130); LTM calculated, C1 |
| Adjusted EBITDA, issuer-defined (USD thousands) | 130,539 | 366,217 | 484,946 | 436,043 | 397,377 | Reported (10-Q Q3 page:43; 10-K page:111); LTM calculated, C1 |
| Adjusted EBITDA margin (%) | 44.4 | 42.5 | 42.6 | 41.3 | 42.1 | Calculated, C10 |
| Share-based compensation and related payroll tax added back (USD thousands) | 31,758 | 97,359 | 126,687 | 181,285 | 177,808 | Reported (10-Q Q3 page:43; 10-K page:111); LTM calculated, C1 |
| Adjusted EBITDA less that add-back (USD thousands) | 98,781 | 268,858 | 358,259 | 254,758 | 219,569 | Calculated, C5; analyst measure, not issuer-defined |
| Interest expense (USD thousands) | 20,900 | 61,559 | 79,700 | 71,007 | 64,608 | Reported (10-Q Q3 page:5; 10-K page:130); LTM calculated, C1 |
| Cash paid for interest (USD thousands) | 19,557 | 57,637 | 72,448 | 66,704 | 62,898 | Reported 9M, FY (10-Q Q3 page:8; 10-K page:132); Q3 derived, C8; LTM calculated, C1 |
| Cash paid for income taxes, net (USD thousands) | 7,318 | 9,142 | 11,538 | 28,595 | 50,742 | Reported 9M, FY (10-Q Q3 page:8; 10-K page:132); Q3 derived, C8; LTM calculated, C1 |
| Net income including non-controlling interest (USD thousands) | 30,231 | 66,435 | 74,555 | 1,688 | 31,240 | Reported (10-Q Q3 page:5; 10-K page:130); LTM calculated, C1 |
| Net cash provided by operating activities (USD thousands) | 100,429 | 259,464 | 378,628 | 315,479 | 283,886 | Reported 9M, FY (10-Q Q3 page:8; 10-K page:132); Q3 per release 2026-10-29 page:12 and C8; LTM calculated, C1 |
| Purchases of software, equipment and property (USD thousands) | 17,964 | 52,966 | 67,253 | 60,971 | 53,012 | Reported 9M, FY; Q3 per release page:12; LTM calculated, C1 |
| Free cash flow, operating cash flow less those purchases (USD thousands) | 82,465 | 206,498 | 311,375 | 254,508 | 230,874 | Issuer-defined, reported (release 2026-10-29 page:12; 10-K page:112); LTM calculated, C1 |
| Cash and cash equivalents at period end (USD thousands) | 202,926 | Same date as Q3 2026 | 202,926 | 111,192 | 398,983 | Reported (10-Q Q3 page:4; 10-K page:129) |
| Term Loan principal at period end (USD thousands) | 1,281,216 | Same date as Q3 2026 | 1,281,216 | 1,290,990 | 776,000 | Reported (10-Q Q3 page:19; 10-K page:161; 10-K page:114) |
| Net debt: principal less cash (USD thousands) | 1,078,290 | Same date as Q3 2026 | 1,078,290 | 1,179,798 | 377,017 | Calculated, C3 |
| Total debt / Adjusted EBITDA (x) | Not applicable: LTM basis | Not applicable: LTM basis | 2.64 | 2.96 | 1.95 | Calculated, C3 |
| Net debt / Adjusted EBITDA (x) | Not applicable: LTM basis | Not applicable: LTM basis | 2.22 | 2.71 | 0.95 | Calculated, C3 |
| Total debt / (Adjusted EBITDA less add-back) (x) | Not applicable: LTM basis | Not applicable: LTM basis | 3.58 | 5.07 | 3.53 | Calculated, C5 |
| Net debt / (Adjusted EBITDA less add-back) (x) | Not applicable: LTM basis | Not applicable: LTM basis | 3.01 | 4.63 | 1.72 | Calculated, C5 |
| Adjusted EBITDA / cash interest (x) | 6.67 | 6.35 | 6.69 | 6.54 | 6.32 | Calculated, C4 |
| Adjusted EBITDA less add-back / cash interest (x) | 5.05 | 4.66 | 4.95 | 3.82 | 3.49 | Calculated, C5 |
| Free cash flow / Adjusted EBITDA (%) | 63.2 | 56.4 | 64.2 | 58.4 | 58.1 | Calculated, C10 |
| Term Loan weighted-average interest rate (%) | 5.8 | 5.8 | Not supplied: only quarter, nine-month and full-year rates are printed | 6.2 | 7.6 | Reported (10-Q Q3 page:18; 10-K page:115) |
| Total stockholders' equity (USD thousands) | 1,841,885 | Same date as Q3 2026 | 1,841,885 | 1,787,010 | 1,997,823 | Reported (10-Q Q3 page:5; 10-K page:129) |

Reading the leverage rows: Adjusted EBITDA is the issuer's measure and it adds back share-based compensation and related payroll tax (10-Q Q3 page:43). The reported figure is the base for the headline ratios above; the rows after the add-back are an analyst sensitivity. The interest cover ratios use cash paid for interest, as the method asks; interest expense is higher (79,700 LTM) because it includes non-cash items (C4).

### Source context

| Source | Entity and perimeter | Periods | Statement kind | Units |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | CCC Intelligent Solutions Holdings Inc. and subsidiaries, consolidated; includes the CCC Cayman subsidiary and its non-controlling interest until reclassified | Years ended 2025-12-31, 2024-12-31 and 2023-12-31; balance sheets at 2025-12-31 and 2024-12-31 | Audited consolidated statements (10-K page:125) | "(In thousands, except share data)" (10-K page:129); USD |
| 10-Q Q1 2026 | Same consolidated perimeter | Three months ended 2026-03-31 and 2025-03-31; balance sheet 2026-03-31 and 2025-12-31 | Unaudited condensed | "(In thousands, except share data)" (10-Q Q1 page:4); USD |
| 10-Q Q2 2026 | Same | Three and six months ended 2026-06-30 and 2025-06-30; balance sheet 2026-06-30 | Unaudited condensed | "(In thousands, except share data)" (10-Q Q2 page:4); USD |
| 10-Q Q3 2026 | Same | Three and nine months ended 2026-09-30 and 2025-09-30; balance sheet 2026-09-30 | Unaudited condensed | "(In thousands, except share data)" (10-Q Q3 page:4); USD |
| Releases (3) | Same, issuer presentation with non-GAAP measures | Q1, Q2 and Q3 2026 and the comparable periods | Unaudited, furnished, attributed to management | Thousands in tables, millions in text; USD |

### Reported statements of operations

| Line (as printed) | Q1 2026 | Q2 2026 | Q3 2026 | 9M 2026 | 9M 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Revenues | 281,274 | 285,931 | 294,093 | 861,298 | 779,136 | 1,057,001 | 944,800 |
| Gross profit | 208,879 | 210,637 | 218,006 | 637,522 | 571,981 | 776,808 | 713,803 |
| Total operating expenses | 160,062 | 163,004 | 160,619 | 483,685 | 528,235 | 682,966 | 633,698 |
| Operating income | 48,817 | 47,633 | 57,387 | 153,837 | 43,746 | 93,842 | 80,105 |
| Interest expense | (20,300) | (20,359) | (20,900) | (61,559) | (52,866) | (71,007) | (64,608) |
| Interest income | 942 | 743 | 1,365 | 3,050 | 4,233 | 4,882 | 12,203 |
| Pretax income (loss) | 33,425 | 30,584 | 39,934 | 103,943 | (11,575) | 21,529 | 44,314 |
| Income tax (provision) benefit | (18,008) | (9,797) | (9,703) | (37,508) | 5,143 | (19,841) | (13,074) |
| Net income (loss) including non-controlling interest | 15,417 | 20,787 | 30,231 | 66,435 | (6,432) | 1,688 | 31,240 |

Sources: 10-Q Q1 page:5; 10-Q Q2 page:5; 10-Q Q3 pages:5-6; 10-K pages:129-130. Expense and outflow lines are shown signed as printed in parentheses. Stock-based compensation fell from 146,216 in 9M 2025 to 93,794 in 9M 2026 (10-Q Q3 page:8), a fall of 52,422 that is larger than the 44,550 fall in total operating expenses; share-based compensation by function for Q3 is on 10-Q Q3 page:36.

### Reported balance sheet (selected lines)

| Line (as printed) | 2024-12-31 | 2025-12-31 | 2026-03-31 | 2026-06-30 | 2026-09-30 |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 398,983 | 111,192 | 36,900 | 115,857 | 202,926 |
| Total current assets | 564,650 | 335,098 | 250,896 | 330,620 | 426,513 |
| Goodwill | 1,417,724 | 1,955,551 | 1,955,551 | 1,955,551 | 1,955,551 |
| Intangible assets, net | 934,278 | 1,010,658 | 987,778 | 964,898 | 942,018 |
| Total assets | 3,183,218 | 3,573,432 | 3,470,788 | 3,531,928 | 3,602,061 |
| Current portion of long-term debt | 8,000 | 13,033 | 13,033 | 13,033 | 13,033 |
| Note payable to minority investor | — | 25,197 | 25,953 | 26,741 | 27,562 |
| Total current liabilities | 154,846 | 234,125 | 200,281 | 212,180 | 208,437 |
| Long-term debt, net | 761,053 | 1,264,941 | 1,262,138 | 1,259,345 | 1,256,563 |
| Operating lease liabilities (current plus non-current) | 54,893 | 59,252 | 58,386 | 57,359 | 56,086 |
| Long-term licensing agreement (current plus non-current) | 27,692 | 24,434 | 23,589 | 22,729 | 21,855 |
| Total liabilities | 1,163,716 | 1,786,422 | 1,749,638 | 1,759,380 | 1,760,176 |
| Redeemable non-controlling interest (mezzanine) | 21,679 | — | — | — | — |
| Total stockholders' equity | 1,997,823 | 1,787,010 | 1,721,150 | 1,772,548 | 1,841,885 |

Sources: 10-K page:129; 10-Q Q1 page:4; 10-Q Q2 pages:4-5; 10-Q Q3 pages:4-5. The lease and licensing rows are sums of the printed current and non-current lines (C11). Total assets equal total liabilities plus equity at 2026-09-30 (C9).

### Reported cash flows (selected lines)

| Line (as printed) | Q1 2026 | Q2 2026 | Q3 2026 | 9M 2026 | 9M 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net cash provided by operating activities | 57,461 | 101,574 | 100,429 | 259,464 | 196,315 | 315,479 | 283,886 |
| Purchases of software, equipment, and property | (15,876) | (19,126) | (17,964) | (52,966) | (46,684) | (60,971) | (53,012) |
| Acquisition of EvolutionIQ, net of cash acquired | — | — | — | — | (410,412) | (410,412) | — |
| Proceeds from issuance of long-term debt | — | — | — | — | 225,000 | 525,000 | — |
| Principal payments on long-term debt | (3,258) | (3,259) | (3,257) | (9,774) | (7,508) | (10,010) | (8,000) |
| Repurchase of common stock | (100,166) | — | — | (100,166) | (212,485) | (600,567) | — |
| Stock-based compensation (non-cash add-back) | 31,871 | 30,387 | 31,536 | 93,794 | 146,216 | 175,394 | 171,038 |
| Cash paid for interest | 19,008 | 19,072 | 19,557 | 57,637 | 51,893 | 66,704 | 62,898 |

Sources: 10-Q Q1 pages:6-7; 10-Q Q2 pages:7-8; 10-Q Q3 page:8; 10-K pages:131-132. Q2 and Q3 values are differences of cumulative columns for operating cash flow, purchases, principal payments and cash interest (C8); the share-based compensation quarters are the equity-statement amounts (10-Q Q3 pages:6-7). The Q3 principal payment of 3,257 is 9,774 less the Q1 and Q2 payments; Q2 3,259 is the difference of the six-month 6,517 and Q1 3,258 (C8). The Q1 2026 repurchase of 100,166 is the cash paid for 16,565,982 shares under the 2025 Share Repurchase Program (10-Q Q3 page:22); the 9,606,474 shares delivered on 2026-02-27 settled the accelerated share repurchase prepaid on 2025-12-12 (10-Q Q3 page:23).

### Debt register and terms at 2026-09-30

| Instrument (as printed) | Amount (USD thousands) | Maturity | Rate and security | Source |
| --- | --- | --- | --- | --- |
| Term Loan, principal | 1,281,216 | 2032-01-23; quarterly principal payments of about 3.3 million through 2031-12-31 | Term SOFR plus 2.00% (1.00% for base rate loans), with 0.25% reduction if first lien debt ratings reach BB-/Ba3 or better; senior secured, first-priority liens on the equity of CCC Intelligent Solutions Inc. and substantially all of its assets | 10-Q Q3 pages:18-19 |
| Term Loan, discount | (912) | Not applicable | Contra-debt item | 10-Q Q3 page:19 |
| Term Loan, deferred financing fees | (10,708) | Not applicable | Contra-debt item | 10-Q Q3 page:19 |
| Term Loan, net of discount and fees | 1,269,596 | Not applicable | Of which current 13,033 and long-term 1,256,563 | 10-Q Q3 page:19 |
| 2021 Revolving Credit Facility | 0 drawn of 250,000 commitment | 2029-09-23; springing 2028-06-22 if more than 234.0 million of term loan remains | Letters of credit 1.0 million; availability 249.0 million; commitment fee up to 0.50% on unused amount; letters of credit sublimit 75.0 million (10-K page:158) | 10-Q Q3 page:18 |
| Note payable to minority investor (CCC Cayman) | 27,562 | Date funds are available to redeem the Series A preferred stock | 12.0% per annum compounded daily, paid in kind; without recourse to the registrant | 10-Q Q3 pages:19-20 |

Fair value: the term loan carrying amount is 1,280,303 and its estimated fair value is 1,276,411 at 2026-09-30, against 1,289,968 and 1,294,220 at 2025-12-31 (10-Q Q3 page:14); the estimate is 99.6% of principal at 2026-09-30 and was above principal at 2025-12-31 (C12). Interest rate swaps fix 750.0 million notional of the term loan at about 3.94% through 2027-07-31, fair value an asset of 2.6 million at 2026-09-30, not designated as hedges (10-Q Q3 page:19). The 10-K states that a 100-basis point rise in rates would raise annual interest expense by 12.9 million at 2025-12-31 (10-K page:125); that figure equals 1.00% of the full 1,290,990 principal, so it appears not to reflect the swaps, though the filing does not say so.

Guarantors and security: guaranteed by an intermediate holding company named "Cypress Holdings Intermediate Holdings II, LLC." in the 10-K and in the Q1 10-Q, and "Cypress Intermediate Holdings II, LLC" in the Q2 and Q3 10-Qs, and by certain other US subsidiaries (10-K page:160; 10-Q Q1 page:20; 10-Q Q2 page:18; 10-Q Q3 page:18).

Covenants as described (the agreement itself is Not supplied): a financial covenant applies at each quarter end only if revolver borrowings exceed 35% of commitments, in which case the leverage ratio of the borrower and certain subsidiaries cannot exceed 6.25 to 1.00 (10-K page:161; 10-Q Q3 page:18); the filings say the test did not apply at 2025-12-31 and 2026-09-30 and that the company was in compliance (10-K page:161; 10-Q Q3 page:18). The term loan requires mandatory prepayment from certain events and up to 50% of annual excess cash flow if the leverage ratio exceeds 3.5, which it did not at 2025-12-31 (10-K page:114). The wording of the ratio varies: leverage ratio (10-K page:161), first lien leverage test (10-K page:81) and first lien net leverage ratio test (10-Q Q3 page:46).

### Other claims outside the funded debt figure

| Claim | Amount at 2026-09-30 (USD thousands) | Inside or outside the debt figure | Source |
| --- | --- | --- | --- |
| Note payable to minority investor, CCC Cayman, without recourse to the registrant | 27,562 | Outside (shown separately) | 10-Q Q3 page:5, page:20 |
| Operating lease liabilities, current plus non-current | 56,086 (6,072 + 50,014) | Outside | 10-Q Q3 page:5 |
| Long-term licensing agreement, current plus non-current | 21,855 (3,632 + 18,223) | Outside | 10-Q Q3 page:5 |
| Purchase obligations for data licences, data centre, disaster recovery and SaaS | 164,515 at 2025-12-31 (2026: 51,632; 2027: 69,284; 2028: 13,899; 2029, 2030 and thereafter: 9,900 each); 10-Q Q3 reports no material change | Outside | 10-K page:174; 10-Q Q3 page:25 |
| Merger termination fee payable by the company in certain cases | 149,520 (149.52 million) | Contingent, outside | 10-Q Q3 page:51 |
| Finance leases | None: the 10-K states "The Company does not have any finance leases" | Not applicable | 10-K page:154 |
| Pensions | No defined benefit obligation: the company sponsors defined contribution 401(k) plans, with expense of 10.5 million in FY2025 | Not applicable | 10-K pages:168-169 |
| Retiree medical, factoring and supply-chain finance | Not supplied: the terms were searched in all seven sources and are not mentioned | Not applicable | All sources |
| Litigation or consent decrees | No amount stated: Note 20 of the 10-Q says pending or threatened matters are not expected to have a material adverse effect; merger-related stockholder complaints are a risk factor with no amount | Not applicable | 10-Q Q3 page:25, page:53 |

Debt plus the minority-investor note over LTM Adjusted EBITDA is 2.70x, and adding the lease and licensing liabilities 2.86x (C11). These are analyst sensitivities.

### Adjusted EBITDA definition and reconciliation

Issuer definition: net income adjusted for interest, taxes, amortisation, depreciation, stock-based compensation expense and related employer payroll tax, M&A and integration costs, litigation proceeds and costs, equity transaction costs, change in fair value of derivative instruments, income from derivative instruments and debt refinancing costs (10-Q Q3 page:43; 10-K page:110). Q3 2026 reconciliation (10-Q Q3 page:43): net income 30,231; interest expense 20,900; interest income (1,365); income tax provision 9,703; amortisation of intangible assets 18,511; amortisation of acquired technologies 4,368; depreciation and amortisation 2,048 and 12,763; stock-based compensation and payroll tax 31,758; M&A and integration costs 3,657; change in fair value of derivative instruments (2,514); expense from derivative instruments 479; Adjusted EBITDA 130,539. M&A and integration costs added back were 3,657 in Q3 2026 against 234 in Q3 2025 (10-Q Q3 page:43); the filing does not itemise what they comprise. Adjusted EBITDA margin is 44% for Q3 2026 and 41% for Q3 2025 as printed (10-Q Q3 page:43). Quarterly Adjusted EBITDA: Q1 2026 120,198 (10-Q Q1 page:41); Q2 2026 115,478 (10-Q Q2 page:41); Q3 2026 130,539.

### KPIs

| KPI | Definition source | Q1 2026 | Q2 2026 | Q3 2026 | Q1 2025 | Q2 2025 | Q3 2025 | Q4 2025 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Software net dollar retention (%) | 10-Q Q3 page:34 | 107 | 107 | 108 | 107 | 107 | 105 | 106 |
| Software gross dollar retention (%) | 10-Q Q3 page:35 | 98 | 98 | 98 | 99 | 99 | 99 | 99 |

Software subscription revenue was 281.5 million, 96% of total revenue, in Q3 2026 against 256.7 million in Q3 2025 (10-Q Q3 page:36). Revenue growth in Q3 2026 came about 8% from existing customers and about 2% from new customers (10-Q Q3 page:36). An AI-related annualised run-rate of about 130 million is a management claim in the release, not a filed figure (release 2026-10-29 page:2).

### Subsequent event with financial relevance

On 2026-10-14 the company entered into an Agreement and Plan of Merger with Mozart Parent, LLC and Mozart Merger Sub (DE), Inc.; each share converts into $7.75 in cash, no financing condition, expected close in the first quarter of 2027 (10-Q Q3 pages:29-30). The release states an enterprise value of approximately $6.1 billion and a consortium led by GTCR including Elliott Investment Management, and says guidance is suspended (release 2026-10-29 page:2). The agreement restricts, without Parent consent, incurring certain debt, dividends and share repurchases (10-Q Q3 pages:22, 45, 52). The fate of the existing term loan at closing and the merger financing are Not supplied. Nothing in this handoff is pro forma.

### Corrections to CP-0

CP-0 was accepted and cannot be edited; where it differs from the sources, this module governs.

| CP-0 statement | Correction | Locator |
| --- | --- | --- |
| Reader summary says "The only debt is one senior secured term loan and an undrawn revolver" | There is also a 27,562 promissory note at CCC Cayman, non-recourse to the registrant, outside the funded debt figure and shown in the debt register | 10-Q Q3 pages:19-20 |
| Cash 202,926 cited to 10-Q Q3 page:5 (Calculations) and statements cited as pages:5-8 | The 2026-09-30 balance sheet assets, including cash, are on 10-Q Q3 page:4; the liability and equity side continues on page:5 | 10-Q Q3 pages:4-5 |
| Tie-out of the 10-Q to the 2026-10-29 release cited at release pages:2, 9 and 12 | Cash 202,926 is in the release balance sheet on release page:8 (and as 202.9 million on page:2); revenue 294,093 is on page:9; free cash flow on page:12 | Release 2026-10-29 pages:8, 9, 12 |
| Guarantor name compared between the 10-K and the Q2 and Q3 10-Qs | The Q1 10-Q uses the 10-K spelling; only the Q2 and Q3 10-Qs use "Cypress Intermediate Holdings II, LLC" | 10-Q Q1 page:20 |
| 10-K maturity table "should be checked" for the 2030 bucket | The 2030 bucket of 1,238,858 equals 13,033 for 2030, 13,033 for 2031 and the balloon of 1,212,792 due in 2032, so it is a lumped last bucket and not a conflicting maturity (C6) | 10-K page:161 |

## Calculations

All amounts in USD thousands unless stated. LTM Q3 2026 = FY2025 + 9M 2026 − 9M 2025. LTM Q2 2026 = FY2025 + six months 2026 − six months 2025. LTM Q1 2026 = FY2025 + Q1 2026 − Q1 2025.

### C1 LTM Q3 2026 builds

| Item | FY2025 | + 9M 2026 | − 9M 2025 | = LTM Q3 2026 |
| --- | --- | --- | --- | --- |
| Revenue | 1,057,001 | 861,298 | 779,136 | 1,139,163 |
| Operating income | 93,842 | 153,837 | 43,746 | 203,933 |
| Adjusted EBITDA | 436,043 | 366,217 | 317,314 | 484,946 |
| Stock-based compensation and related payroll tax | 181,285 | 97,359 | 151,957 | 126,687 |
| Interest expense | 71,007 | 61,559 | 52,866 | 79,700 |
| Cash paid for interest | 66,704 | 57,637 | 51,893 | 72,448 |
| Cash paid for income taxes, net | 28,595 | 9,142 | 26,199 | 11,538 |
| Net income including non-controlling interest | 1,688 | 66,435 | (6,432) | 74,555 |
| Net cash provided by operating activities | 315,479 | 259,464 | 196,315 | 378,628 |
| Purchases of software, equipment and property | 60,971 | 52,966 | 46,684 | 67,253 |
| Free cash flow | 254,508 | 206,498 | 149,631 | 311,375 |

Inputs: FY2025 from 10-K pages:111, 112, 130, 132; 9M 2026 and 9M 2025 from 10-Q Q3 pages:5, 8, 43 and release 2026-10-29 page:12. Check: 378,628 − 67,253 = 311,375.

### C2 LTM Q1 2026 and LTM Q2 2026 builds

| Item | FY2025 | + Q1 2026 | − Q1 2025 | = LTM Q1 2026 | + six months 2026 | − six months 2025 | = LTM Q2 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Adjusted EBITDA | 436,043 | 120,198 | 99,077 | 457,164 | 235,678 | 207,194 | 464,527 |
| Cash paid for interest | 66,704 | 19,008 | 16,358 | 69,354 | 38,080 | 33,616 | 71,168 |
| Interest expense | 71,007 | 20,300 | 16,926 | 74,381 | 40,659 | 34,763 | 76,903 |

Inputs: 10-Q Q1 pages:5, 7, 41; 10-Q Q2 pages:5, 8, 41; 10-K pages:111, 130, 132. Six-month Adjusted EBITDA is the reported cumulative figure, not the sum of the quarters.

### C3 Leverage (principal basis)

Net debt = Term Loan principal − cash and cash equivalents. Revolver undrawn at every date (0 drawn).

| Date | Principal | Cash | Net debt | EBITDA used | Total debt / EBITDA | Net debt / EBITDA |
| --- | --- | --- | --- | --- | --- | --- |
| 2024-12-31 | 776,000 | 398,983 | 377,017 | 397,377 | 776,000 / 397,377 = 1.95x | 377,017 / 397,377 = 0.95x |
| 2025-12-31 | 1,290,990 | 111,192 | 1,179,798 | 436,043 | 1,290,990 / 436,043 = 2.96x | 1,179,798 / 436,043 = 2.71x |
| 2026-03-31 | 1,287,732 | 36,900 | 1,250,832 | 457,164 | 1,287,732 / 457,164 = 2.82x | 1,250,832 / 457,164 = 2.74x |
| 2026-06-30 | 1,284,474 | 115,857 | 1,168,617 | 464,527 | 1,284,474 / 464,527 = 2.77x | 1,168,617 / 464,527 = 2.52x |
| 2026-09-30 | 1,281,216 | 202,926 | 1,078,290 | 484,946 | 1,281,216 / 484,946 = 2.64x | 1,078,290 / 484,946 = 2.22x |

Inputs: principal from 10-K pages:114, 161 and the 10-Q debt tables (10-Q Q1 page:20; 10-Q Q2 page:18; 10-Q Q3 page:19); cash from the balance sheets. Principal change FY2025 to Q3 2026: 1,290,990 − 1,281,216 = 9,774, equal to principal payments in 9M 2026. Net debt change: 1,078,290 − 1,179,798 = −101,508.

### C4 Interest cover (cash paid for interest basis)

| Period | EBITDA | Cash interest | EBITDA / cash interest | Interest expense | EBITDA / interest expense |
| --- | --- | --- | --- | --- | --- |
| FY2024 | 397,377 | 62,898 | 6.32x | 64,608 | 6.15x |
| FY2025 | 436,043 | 66,704 | 6.54x | 71,007 | 6.14x |
| LTM Q1 2026 | 457,164 | 69,354 | 6.59x | 74,381 | 6.15x |
| LTM Q2 2026 | 464,527 | 71,168 | 6.53x | 76,903 | 6.04x |
| LTM Q3 2026 | 484,946 | 72,448 | 6.69x | 79,700 | 6.08x |
| Q3 2026 | 130,539 | 19,557 | 6.67x | 20,900 | 6.25x |
| 9M 2026 | 366,217 | 57,637 | 6.35x | 61,559 | 5.95x |

Inputs: Adjusted EBITDA from C1 and C2; cash interest and interest expense from C1, C2 and C8; the Q3 2026 and 9M 2026 rows use the discrete-quarter and nine-month figures.

### C5 Sensitivity after share-based pay

Adjusted EBITDA less add-back = Adjusted EBITDA − stock-based compensation and related payroll tax.

| Period | Adjusted EBITDA | Add-back | Result | Principal | Net debt | Total debt / result | Net debt / result | Cash interest | Result / cash interest |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FY2024 | 397,377 | 177,808 | 219,569 | 776,000 | 377,017 | 3.53x | 1.72x | 62,898 | 3.49x |
| FY2025 | 436,043 | 181,285 | 254,758 | 1,290,990 | 1,179,798 | 5.07x | 4.63x | 66,704 | 3.82x |
| LTM Q3 2026 | 484,946 | 126,687 | 358,259 | 1,281,216 | 1,078,290 | 3.58x | 3.01x | 72,448 | 4.95x |
| Q3 2026 | 130,539 | 31,758 | 98,781 | not applicable | not applicable | not applicable | not applicable | 19,557 | 5.05x |
| 9M 2026 | 366,217 | 97,359 | 268,858 | not applicable | not applicable | not applicable | not applicable | 57,637 | 4.66x |

Inputs: 10-K page:111; 10-Q Q3 page:43. The FY2025 ratio uses year-end debt including the 300,000 incremental term loan of 2025-12-12 against full-year earnings.

### C6 Debt maturity derivation (US$m in the chart table; thousands here)

Stated terms: quarterly principal payments of about 3.3 million until 2031-12-31, remainder due 2032-01-23 (10-Q Q3 page:18); current portion 13,033 (10-Q Q3 page:19); 9M 2026 principal payments 9,774 (10-Q Q3 page:8).

- Q4 2026: 13,033 − 9,774 = 3,259.
- 2027 to 2031: 13,033 each, five years, total 65,165.
- 2032 balloon: 1,281,216 − 3,259 − 65,165 = 1,212,792.
- Check against the 10-K table at 2025-12-31: 13,033 for each of 2026 to 2029 and 1,238,858 for 2030 sum to 52,132 + 1,238,858 = 1,290,990; and 1,238,858 = 13,033 + 13,033 + 1,212,792 = 1,238,858.

### C7 Liquidity

2026-09-30: cash 202,926 + revolver availability 249,000 (commitment 250,000 less 1,000 of standby letters of credit) = 451,926. Inputs: 10-Q Q3 pages:4, 18.

### C8 Discrete quarter derivations

- Cash paid for interest: Q2 2026 = 38,080 (six months) − 19,008 (Q1) = 19,072; Q3 2026 = 57,637 − 38,080 = 19,557.
- Cash paid for income taxes, net: six months 2026 = 1,824 (10-Q Q2 page:8); Q3 2026 = 9,142 − 1,824 = 7,318; Q1 2026 was a net receipt of 2,109 (10-Q Q1 page:7).
- Operating cash flow: Q2 2026 = 159,035 − 57,461 = 101,574; Q3 2026 = 259,464 − 159,035 = 100,429 (release 2026-10-29 page:12 prints 100,429).
- Principal payments: Q2 = 6,517 − 3,258 = 3,259; Q3 = 9,774 − 6,517 = 3,257.

### C9 Tie-outs

| Check | Inputs | Result |
| --- | --- | --- |
| Quarterly revenue to nine months | 281,274 + 285,931 + 294,093 | 861,298, equal to the reported 9M 2026 |
| Quarterly operating cash flow to nine months | 57,461 + 101,574 + 100,429 | 259,464, equal to the reported 9M 2026 |
| Quarterly free cash flow to nine months | 41,585 + 82,448 + 82,465 (releases: Q1 page:10, Q2 page:10, Q3 page:12) | 206,498, equal to the reported 9M 2026 |
| Quarterly purchases of software, equipment and property to nine months | 15,876 + 19,126 + 17,964 | 52,966, equal to the reported 9M 2026 |
| Adjusted EBITDA quarters to nine months | 120,198 + 115,478 + 130,539 | 366,215 against the reported 366,217: difference 2 |
| Term loan carrying amount | 1,281,216 − 912 − 10,708 | 1,269,596; 13,033 + 1,256,563 = 1,269,596 |
| Balance sheet 2026-09-30 | Total liabilities 1,760,176 + equity 1,841,885 | 3,602,061, equal to total assets |
| Cash change 9M 2026 | 202,926 − 111,192 | 91,734, equal to the reported net change |
| Principal change 9M 2026 | 1,290,990 − 1,281,216 | 9,774, equal to principal payments |

### C10 Margins, growth and conversion

- Adjusted EBITDA margin: Q3 2026 130,539 / 294,093 = 44.4%; 9M 2026 366,217 / 861,298 = 42.5%; LTM 484,946 / 1,139,163 = 42.6%; FY2025 436,043 / 1,057,001 = 41.3%; FY2024 397,377 / 944,800 = 42.1%.
- Revenue growth: Q3 2026 294,093 / 267,120 − 1 = 10.1%; 9M 2026 861,298 / 779,136 − 1 = 10.5%; FY2025 1,057,001 / 944,800 − 1 = 11.9%; FY2024 944,800 / 866,378 − 1 = 9.1%.
- Free cash flow / Adjusted EBITDA: Q3 2026 82,465 / 130,539 = 63.2%; 9M 2026 206,498 / 366,217 = 56.4%; LTM 311,375 / 484,946 = 64.2%; FY2025 254,508 / 436,043 = 58.4%; FY2024 230,874 / 397,377 = 58.1%.

### C11 Other claims

- Debt plus note: 1,281,216 + 27,562 = 1,308,778; / 484,946 = 2.70x.
- Plus operating leases 56,086 and licensing 21,855: 1,308,778 + 56,086 + 21,855 = 1,386,719; / 484,946 = 2.86x.
- Operating lease liabilities: 2026-09-30 6,072 + 50,014 = 56,086; 2025-12-31 7,785 + 51,467 = 59,252; 2024-12-31 7,658 + 47,235 = 54,893; 2026-03-31 6,760 + 51,626 = 58,386; 2026-06-30 6,411 + 50,948 = 57,359.
- Licensing: 2026-09-30 3,632 + 18,223 = 21,855; 2025-12-31 3,466 + 20,968 = 24,434; 2024-12-31 3,257 + 24,435 = 27,692; 2026-03-31 3,521 + 20,068 = 23,589; 2026-06-30 3,576 + 19,153 = 22,729.

### C12 Fair value ratio

1,276,411 / 1,281,216 = 99.6% at 2026-09-30; 1,294,220 / 1,290,990 = 100.3% at 2025-12-31.

### C13 Metrics table cover rows for Q3 and 9M

Q3 2026 Adjusted EBITDA / cash interest = 130,539 / 19,557 = 6.67x; 9M 2026 = 366,217 / 57,637 = 6.35x. Q3 2026 after add-back = 98,781 / 19,557 = 5.05x; 9M 2026 = 268,858 / 57,637 = 4.66x.

## Gaps

| Gap | Severity | Affected | Action |
| --- | --- | --- | --- |
| 2021 Credit Agreement and Amendments 1 to 5 not supplied: the leverage ratio definition, covenant EBITDA, any add-back cap and the change-of-control terms are Not supplied; covenant headroom is Not calculable | High | CP-2, CP-5 | Add the executed agreement and amendments |
| Merger agreement and financing not supplied: whether the term loan is repaid or rolled, new debt amounts and pro forma leverage are Not supplied and Not calculable | High | CP-1A, CP-2 | Add the 8-K of 2026-10-15 with exhibit 2.1 and any later financing disclosure |
| Q4 2025 discrete quarter not reported in the pack; no quarterly series is built for it | Low | CP-2 | LTM figures use cumulative columns instead |
| Revolver availability is stated only to one decimal place in millions (249.0); exact thousands of the letters of credit are not printed | Low | CP-1 | The chart uses the printed amounts |
| The 10-K 100-basis point sensitivity of 12.9 million does not state whether the 750.0 million swaps are reflected | Low | CP-2 | Do not use it as a net exposure figure |
| Restricted cash, finance leases, pensions and retiree medical: no balance sheet line found; reported as Not supplied rather than zero | Low | CP-2 | None unless a later source prints them |
| Differences carried from CP-0: guarantor name spelling, covenant wording, release headline total debt basis, depreciation in the segment note (42,065 against 42,120 in the cash flow statement for 9M 2026) | Low | CP-1A, CP-5 | Quote as printed; use cash flow and reconciliation amounts for add-backs |
| Extraction fidelity not reviewed against the original HTML; tables were read from flattened text | Low | CP-5 | Spot check key tables against the HTML |

## Next module

Proceed to CP-1A (business and transaction context) with these financial inputs: funded debt is the term loan of 1,281,216 principal plus an undrawn 250.0 million revolver; LTM Adjusted EBITDA 484,946 and leverage 2.64x gross and 2.22x net, 3.58x and 3.01x after share-based pay; cash interest cover 6.69x; liquidity of 451.926 US$m; scheduled amortisation of 13,033 a year and a 1,212,792 balloon in 2032. Carry forward the restrictions: covenant definitions, merger financing and the treatment of the existing debt at closing are Not supplied, and nothing here is pro forma. State that CP-0 is corrected as listed above where they differ.
