## Request

Issuer: AMC Global Media Inc. (issuer id amcx; Nasdaq: AMCX; formerly AMC Networks Inc.). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. Current period: Q2 2026 (quarter and six months ended June 30, 2026); prior period: FY2025 (year ended December 31, 2025).

Module task: extract the financial base from the supplied filings (income statement, balance sheet, cash flow, debt, liquidity, maturities, segments), define each measure, compute leverage, interest cover, liquidity and maturities for the report chart selectors, and carry the limitations from the source-readiness handoff. Perimeter: consolidated AMC Global Media Inc. and subsidiaries, as the filings present it; consolidated entities that are not wholly owned are included at 100% (July 2026 release, page:11). Units: the filings print thousands of US dollars; this handoff keeps thousands in the main table and states US$m or x where the chart selectors require it. Nothing dated after the cutoff is used; the latest source is dated July 30, 2026.

Source abbreviations used in locators: 10-K = annual report for FY2025; 10-Q Q3-25, 10-Q Q1-26, 10-Q Q2-26 = the interim reports; Rel Feb, Rel May, Rel Jul = the three Exhibit 99.1 earnings releases (filed 2026-02-11, 2026-05-08, 2026-07-30). A locator `page:N` is the extraction chunk, not the printed page.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_amcx-20251231.htm.jsonl | 2eac087a9c91970955c65f61340e91bd48ad2f9f3f6c57f58dc32a71147af2c1 | FY2025 statements (page:133, 134, 136, 137), debt note and covenant text (page:110-111, 167-176), commitments (page:186) |
| 10-Q_2025-09-30_amcx-20250930.htm.jsonl | 36dd5126a4c9060458356b29d3eb4aa03633caa5f0871dc91ad5f4dc8adcd0a9 | Read for covenant context only; no figure in the tables below comes from it |
| 10-Q_2026-03-31_amcx-20260331.htm.jsonl | 938a57939d24ffa99772ad28c4268837c8cd2e9d6c83313cdce5d4f6457a019b | March 31, 2026 balance sheet cash (page:2), debt note (page:14), cash interest paid (page:23) |
| 10-Q_2026-06-30_amcx-20260630.htm.jsonl | 709e51b6dc542ca6e875192527a94179627534ebb9b979b24ab34c983b10c21a | Q2 2026 and six-month statements (page:2, 3, 5, 6), notes (page:10, 16, 17, 19, 24, 27, 28-30), MD&A (page:42-47, 55-57, 60, 64, 68) |
| EX-99.1_2026-02-11_amcx-21126xex991.htm.jsonl | d86abe17fb554149efdc3f1d1068cea9305b7eb4d0b53b4922cda0c2c6548e87 | FY2025 capitalization, adjusted operating income, credit-facility ratios (page:11) |
| EX-99.1_2026-05-08_amcx-50826ex991.htm.jsonl | baaebb0b7ed064d963f5f351d5426dc6837acb54bc54b02caebdf8169997d96e | March 31, 2026 capitalization, twelve-month adjusted operating income, credit-facility ratios (page:9, 10) |
| EX-99.1_2026-07-30_amcx-73026ex991.htm.jsonl | 2c28473b42400a7535aa74f85a20a041b1e3d1cc8d274b85c2e5db3c449c0a4b | June 30, 2026 capitalization, twelve-month adjusted operating income, free cash flow (page:1, 4, 10, 11) |

### Settings input (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context (run settings, 2026-11-05) | 95e365e5dede6bf5d3238dc431d8121ca3ba426646f866c4518f2a27b51f7e19 |

### Handoffs supplied

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 35f530dc59f7820bbe868f2a577800a555c15b2a5fcc5f7bfcb4e80bdce10420 | Source readiness (READY_WITH_LIMITATIONS). Limitations L1 to L11 are carried below; L1 (no period after June 30, 2026), L2 and L3 (no executed debt documents, credit-agreement covenants ended), L5 (consolidated perimeter), L8 (text-only extraction) and L10 (period labels) bear most on this module. This handoff corrects none of CP-0's statements. |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Earnings fell while net debt was flat, so leverage rose: net debt to adjusted operating income went from 3.10x to 4.06x. The revolver is gone, so liquidity is cash only, and no debt falls due before 2029. | Medium | Latest figures are to June 30, 2026, and the notes' covenant tests are not printed in the sources. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Twelve-month adjusted operating income fell from 411,874 (FY2025) to 313,045 (to June 30, 2026) on lower revenue, especially content licensing. | Cover of cash interest fell from 2.63x to 2.07x; gross leverage rose from 4.32x to 5.54x. | High |
| Net debt was almost unchanged: 1,275,872 at December 31, 2025 and 1,271,558 at June 30, 2026. | Leverage moved because earnings fell, not because debt rose. | High |
| The revolving facility and Term Loan A were ended in May 2026; cash was 463,996 at June 30, 2026. | No committed back-up line remains; liquidity depends on cash, of which some is held abroad. | High |
| Nothing matures until February 2029 (420,456), then 1,315,098 of 10.50% secured notes in July 2032. | Refinancing risk is deferred but concentrated; the company says it cannot repay all debt from cash flow. | High |
| A Netflix licence announced July 30, 2026 is expected to bring cash of about 25 million in 2026 and about 100 million a year in 2027 to 2030. | Supportive of cash flow, but expected not received, and the contract is not supplied. | Medium |

### Financial base view

The financial base is a consolidated, USD, filed-statement base from the 10-K and the June 30, 2026 10-Q, with company releases used only as attributed support. On the company's adjusted operating income (AOI, a non-GAAP measure that adds back share-based compensation, depreciation and amortization, restructuring, impairment and cloud computing amortization and adds the proportionate AOI of majority-owned equity investees) the twelve months to June 30, 2026 produced 313,045 against 411,874 for FY2025. Total debt principal fell from 1,778,251 to 1,735,554 and cash from 502,379 to 463,996, so net debt was 1,275,872 and then 1,271,558. The result is gross debt to AOI of 5.54x and net debt to AOI of 4.06x at June 30, 2026, against 4.32x and 3.10x at FY2025, with AOI to cash interest paid of 2.07x against 2.63x. These ratios use the AOI definition and are not the credit-agreement ratios, which were last reported at March 31, 2026 (net leverage 5.11x against a 5.75x maximum that applied through March 31, 2026 and steps down to 5.50x after; interest coverage 1.85x against a 1.50x minimum) and ended with the facility on May 12, 2026. Using reported operating income plus depreciation and amortization, with no add-backs, the same debt gives much higher multiples because the twelve-month windows include a non-cash impairment charge of 97,784 recorded in Q4 2025; both bases are shown in the calculations and the chart rows use the AOI basis. The base supports the report's leverage, cover, liquidity and maturity charts for three period ends, with the limits listed under Gaps.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (31 Dec 2025) | 4.32 | 3.10 | x | EBITDA is the company's AOI for FY2025, 411,874 thousand. Total debt is principal, 1,778,251 thousand; cash 502,379 thousand. Calculated (C3). AOI is a non-GAAP measure, not EBITDA; the company's own 3.1x also includes finance leases. |
| LTM Q1 2026 (31 Mar 2026) | 4.86 | 3.39 | x | AOI for the twelve months to March 31, 2026, 376,363 thousand, as printed in Rel May page:9. Debt principal 1,829,284 thousand; cash 552,137 thousand. Calculated (C3). Same AOI limitation. |
| LTM Q2 2026 (30 Jun 2026) | 5.54 | 4.06 | x | AOI for the twelve months to June 30, 2026, 313,045 thousand, printed in Rel Jul page:11 and recomputed (C1). Debt principal 1,735,554 thousand; cash 463,996 thousand. Calculated (C3). Same AOI limitation; no credit-agreement ratio exists for this date. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 (31 Dec 2025) | 2.63 | x | AOI 411,874 thousand over cash interest paid 156,563 thousand (10-K page:196). Calculated (C4). Cash interest paid is gross of interest income. |
| LTM Q1 2026 (31 Mar 2026) | 2.38 | x | AOI 376,363 thousand over twelve-month cash interest paid 157,810 thousand, built from FY2025, Q1 2026 and Q1 2025 amounts (C2). Calculated (C4). |
| LTM Q2 2026 (30 Jun 2026) | 2.07 | x | AOI 313,045 thousand over twelve-month cash interest paid 151,153 thousand (C2). Calculated (C4). Quarterly cash interest paid is uneven (Q1 2026 77,983 against 78,984 for the six months, 10-Q Q1-26 page:23 and 10-Q Q2-26 page:27); the twelve-month window smooths this. The 10.50% secured notes carry a higher rate than the debt they replaced, so run-rate cash interest differs (C8). |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| 31 Dec 2025 | 502.379 | 175.0 | US$m | Cash from the balance sheet (10-K page:133). Undrawn $175.0 million revolving credit facility (10-K page:110); no letters of credit drawn on it are printed in the sources. |
| 31 Mar 2026 | 552.137 | 175.0 | US$m | Cash from 10-Q Q1-26 page:2. The $175.0 million revolver was still undrawn (10-Q Q1-26 page:14) but notice of termination was given on May 6, 2026. |
| 30 Jun 2026 | 463.996 | 0 | US$m | Cash from 10-Q Q2-26 page:2. The revolving credit facility was terminated on May 12, 2026 (10-Q Q2-26 page:17), so no committed facility remains in the sources. Cash includes about $136.5 million held by foreign subsidiaries (page:55). An unused receivables sale program with a $125.0 million limit (page:10) is excluded because it is not a committed facility. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0 | US$m | Principal at June 30, 2026 by stated final maturity (10-Q Q2-26 page:16); the Term Loan A and the 10.25% notes were repaid or redeemed before that date. Finance leases and program rights obligations are excluded. |
| 2027 | 0 | US$m | No instrument in the June 30, 2026 debt table matures in 2027. |
| 2028 | 0 | US$m | The Term Loan A due April 2028 (10-Q Q1-26 page:14) was repaid on May 12, 2026 (10-Q Q2-26 page:17). |
| 2029 | 420.456 | US$m | 4.25% Senior Notes due February 2029, 276.706, plus 4.25% Convertible Senior Notes due February 2029, 143.750 (page:16). The convertible notes are convertible into shares at the holder's option under conditions (10-K page:176); principal shown. |
| 2030 | 0 | US$m | No instrument in the June 30, 2026 debt table matures in 2030. |
| 2031 | 0 | US$m | No instrument in the June 30, 2026 debt table matures in 2031. |
| 2032 | 1315.098 | US$m | 10.50% Senior Secured Notes due July 2032 (page:16), principal including notes issued in the March 2026 exchange; carrying value is lower after a discount of 68,832 thousand across all debt. The maturity is read from the instrument labels; no maturity schedule table is printed in the 10-Q. |

### Financials and credit metrics

Amounts in USD thousands unless the Unit column says x. "Reported" rows are printed in the cited page; "Calculated" rows refer to the item in Calculations. Periods: Q2 = three months ended June 30; 6M = six months ended June 30; LTM = twelve months to June 30, 2026; balance items are at the date shown.

| Line | Period | Amount | Unit | Type | Locator |
| --- | --- | --- | --- | --- | --- |
| Revenues, net | FY2025 | 2,311,801 | USD thousands | Reported | 10-K page:134 |
| Revenues, net | 6M 2025 | 1,155,257 | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Revenues, net | 6M 2026 | 1,089,622 | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Revenues, net | Q2 2025 | 600,024 | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Revenues, net | Q2 2026 | 547,495 | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Revenues, net | LTM Jun 2026 | 2,246,166 | USD thousands | Calculated (C1) | FY2025 plus 6M 2026 less 6M 2025 |
| Subscription revenue | Q2 2026 | 352,514 | USD thousands | Reported | 10-Q Q2-26 page:28 |
| Subscription revenue | Q2 2025 | 367,428 | USD thousands | Reported | 10-Q Q2-26 page:29 |
| Advertising revenue | Q2 2026 | 138,212 | USD thousands | Reported | 10-Q Q2-26 page:28 |
| Advertising revenue | Q2 2025 | 148,609 | USD thousands | Reported | 10-Q Q2-26 page:29 |
| Content licensing and other revenue | Q2 2026 | 56,769 | USD thousands | Reported | 10-Q Q2-26 page:28 |
| Content licensing and other revenue | Q2 2025 | 83,987 | USD thousands | Reported | 10-Q Q2-26 page:29 |
| Operating income | FY2025 | 133,322 | USD thousands | Reported | 10-K page:134 |
| Operating income | 6M 2025 | 128,666 | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Operating income | 6M 2026 | 47,115 | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Operating income | Q2 2025 | 64,469 | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Operating income | Q2 2026 | 15,854 | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Operating income | LTM Jun 2026 | 51,771 | USD thousands | Reported and recomputed (C1) | Rel Jul page:11 |
| Depreciation and amortization | FY2025 | 94,425 | USD thousands | Reported | 10-K page:134 |
| Depreciation and amortization | LTM Jun 2026 | 85,296 | USD thousands | Reported and recomputed (C1) | Rel Jul page:11 |
| Impairment and other charges (non-cash) | FY2025 | 97,784 | USD thousands | Reported | 10-K page:134 |
| Adjusted operating income (AOI, non-GAAP) | FY2025 | 411,874 | USD thousands | Reported | Rel Feb page:11 |
| Adjusted operating income (AOI, non-GAAP) | 6M 2025 | 213,871 | USD thousands | Reported | Rel Jul page:11 |
| Adjusted operating income (AOI, non-GAAP) | 6M 2026 | 115,042 | USD thousands | Reported | Rel Jul page:11 |
| Adjusted operating income (AOI, non-GAAP) | Q2 2025 | 109,386 | USD thousands | Reported | Rel Jul page:11 |
| Adjusted operating income (AOI, non-GAAP) | Q2 2026 | 46,068 | USD thousands | Reported | Rel Jul page:11 |
| Adjusted operating income (AOI, non-GAAP) | LTM Mar 2026 | 376,363 | USD thousands | Reported and recomputed (C1) | Rel May page:9 |
| Adjusted operating income (AOI, non-GAAP) | LTM Jun 2026 | 313,045 | USD thousands | Reported and recomputed (C1) | Rel Jul page:11 |
| Segment adjusted operating income, Domestic Operations | Q2 2026 | 60,972 | USD thousands | Reported | 10-Q Q2-26 page:28 |
| Segment adjusted operating income, Domestic Operations | Q2 2025 | 126,339 | USD thousands | Reported | 10-Q Q2-26 page:29 |
| Segment adjusted operating income, International | Q2 2026 | 14,359 | USD thousands | Reported | 10-Q Q2-26 page:28 |
| Segment adjusted operating income, International | Q2 2025 | 14,737 | USD thousands | Reported | 10-Q Q2-26 page:29 |
| Interest expense | FY2025 | 172,353 | USD thousands | Reported | 10-K page:134 |
| Interest expense | 6M 2026 | 84,012 | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Interest expense | 6M 2025 | 85,852 | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Interest expense | LTM Jun 2026 | 170,513 | USD thousands | Calculated (C1) | FY2025 plus 6M 2026 less 6M 2025 |
| Cash interest paid | FY2025 | 156,563 | USD thousands | Reported | 10-K page:196 |
| Cash interest paid | 6M 2026 | 78,984 | USD thousands | Reported | 10-Q Q2-26 page:27 |
| Cash interest paid | 6M 2025 | 84,394 | USD thousands | Reported | 10-Q Q2-26 page:27 |
| Cash interest paid | LTM Jun 2026 | 151,153 | USD thousands | Calculated (C2) | FY2025 plus 6M 2026 less 6M 2025 |
| Net income (loss) including noncontrolling interests | FY2025 | 101,772 | USD thousands | Reported | 10-K page:134 |
| Net income (loss) including noncontrolling interests | 6M 2026 | (36,929) | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Net income (loss) including noncontrolling interests | 6M 2025 | 74,859 | USD thousands | Reported | 10-Q Q2-26 page:3 |
| Net cash provided by operating activities | FY2025 | 305,670 | USD thousands | Reported | 10-K page:136 |
| Net cash provided by operating activities | 6M 2026 | 124,659 | USD thousands | Reported | 10-Q Q2-26 page:5 |
| Net cash provided by operating activities | 6M 2025 | 211,596 | USD thousands | Reported | 10-Q Q2-26 page:5 |
| Net cash provided by operating activities | LTM Jun 2026 | 218,733 | USD thousands | Calculated (C5) | FY2025 plus 6M 2026 less 6M 2025 |
| Capital expenditures | FY2025 | 33,303 | USD thousands | Reported (outflow) | 10-K page:136 |
| Capital expenditures | 6M 2026 | 16,577 | USD thousands | Reported (outflow) | 10-Q Q2-26 page:5 |
| Capital expenditures | 6M 2025 | 21,670 | USD thousands | Reported (outflow) | 10-Q Q2-26 page:5 |
| Capital expenditures | LTM Jun 2026 | 28,210 | USD thousands | Calculated (C5) | FY2025 plus 6M 2026 less 6M 2025 |
| Free cash flow (operating cash flow less capital expenditures) | FY2025 | 272,367 | USD thousands | Calculated (C5) | 10-K page:136 |
| Free cash flow (operating cash flow less capital expenditures) | 6M 2026 | 108,082 | USD thousands | Reported | 10-Q Q2-26 page:64 |
| Free cash flow (operating cash flow less capital expenditures) | 6M 2025 | 189,926 | USD thousands | Reported | 10-Q Q2-26 page:64 |
| Free cash flow (operating cash flow less capital expenditures) | LTM Jun 2026 | 190,523 | USD thousands | Calculated (C5) | FY2025 plus 6M 2026 less 6M 2025 |
| Purchase of treasury stock | FY2025 | 17,969 | USD thousands | Reported (outflow) | 10-K page:136 |
| Purchase of treasury stock | 6M 2026 | 30,000 | USD thousands | Reported (outflow) | 10-Q Q2-26 page:6 |
| Cash and cash equivalents | 31 Dec 2025 | 502,379 | USD thousands | Reported | 10-K page:133 |
| Cash and cash equivalents | 31 Mar 2026 | 552,137 | USD thousands | Reported | 10-Q Q1-26 page:2 |
| Cash and cash equivalents | 30 Jun 2026 | 463,996 | USD thousands | Reported | 10-Q Q2-26 page:2 |
| Total debt, principal | 31 Dec 2025 | 1,778,251 | USD thousands | Reported | 10-Q Q2-26 page:16 |
| Total debt, principal | 31 Mar 2026 | 1,829,284 | USD thousands | Reported | 10-Q Q1-26 page:14 |
| Total debt, principal | 30 Jun 2026 | 1,735,554 | USD thousands | Reported | 10-Q Q2-26 page:16 |
| Unamortized discount | 30 Jun 2026 | (68,832) | USD thousands | Reported | 10-Q Q2-26 page:16 |
| Unamortized deferred financing costs | 30 Jun 2026 | (5,696) | USD thousands | Reported | 10-Q Q2-26 page:16 |
| Long-term debt, net (balance sheet) | 31 Dec 2025 | 1,752,293 | USD thousands | Reported (current 11,068 plus noncurrent 1,741,225) | 10-Q Q2-26 page:16 |
| Long-term debt, net (balance sheet) | 30 Jun 2026 | 1,661,026 | USD thousands | Reported (all noncurrent) | 10-Q Q2-26 page:2 |
| 10.50% Senior Secured Notes due July 2032 | 30 Jun 2026 | 1,315,098 | USD thousands | Reported | 10-Q Q2-26 page:16 |
| 4.25% Senior Notes due February 2029 | 30 Jun 2026 | 276,706 | USD thousands | Reported | 10-Q Q2-26 page:16 |
| 4.25% Convertible Senior Notes due February 2029 | 30 Jun 2026 | 143,750 | USD thousands | Reported | 10-Q Q2-26 page:16 |
| 10.25% Senior Secured Notes due January 2029 | 31 Dec 2025 | 875,000 | USD thousands | Reported | 10-Q Q2-26 page:16 |
| Term Loan A Facility | 31 Dec 2025 | 82,795 | USD thousands | Reported | 10-Q Q2-26 page:16 |
| Net debt (total debt principal less cash) | 31 Dec 2025 | 1,275,872 | USD thousands | Reported and recomputed (C3) | Rel Feb page:11 |
| Net debt (total debt principal less cash) | 30 Jun 2026 | 1,271,558 | USD thousands | Reported and recomputed (C3) | Rel Jul page:11 |
| Lease liabilities (operating plus finance, total) | 31 Dec 2025 | 99,906 | USD thousands | Reported | 10-Q Q2-26 page:19 |
| Lease liabilities (operating plus finance, total) | 30 Jun 2026 | 88,600 | USD thousands | Reported | 10-Q Q2-26 page:19 |
| Program rights obligations, current plus noncurrent | 31 Dec 2025 | 440,025 | USD thousands | Calculated (C6) | 10-Q Q2-26 page:2 |
| Program rights obligations, current plus noncurrent | 30 Jun 2026 | 381,698 | USD thousands | Calculated (C6) | 10-Q Q2-26 page:2 |
| Accrued interest | 30 Jun 2026 | 69,429 | USD thousands | Reported | 10-Q Q2-26 page:16 |
| Total stockholders' equity | 30 Jun 2026 | 946,376 | USD thousands | Reported | 10-Q Q2-26 page:2 |
| Contractual obligations not on the balance sheet | 30 Jun 2026 | 590,300 | USD thousands | Reported as $590.3 million | 10-Q Q2-26 page:24 |
| Purchase obligations | 31 Dec 2025 | 498,951 | USD thousands | Reported | 10-K page:186 |
| Total debt / AOI | FY2025 | 4.32 | x | Calculated (C3) | See C3 |
| Net debt / AOI | FY2025 | 3.10 | x | Calculated (C3) | See C3 |
| AOI / cash interest paid | FY2025 | 2.63 | x | Calculated (C4) | See C4 |
| Total debt / AOI | LTM Mar 2026 | 4.86 | x | Calculated (C3) | See C3 |
| Net debt / AOI | LTM Mar 2026 | 3.39 | x | Calculated (C3) | See C3 |
| AOI / cash interest paid | LTM Mar 2026 | 2.38 | x | Calculated (C4) | See C4 |
| Total debt / AOI | LTM Jun 2026 | 5.54 | x | Calculated (C3) | See C3 |
| Net debt / AOI | LTM Jun 2026 | 4.06 | x | Calculated (C3) | See C3 |
| AOI / cash interest paid | LTM Jun 2026 | 2.07 | x | Calculated (C4) | See C4 |
| Credit-agreement net leverage ratio (company-reported, maximum 5.75x) | 31 Dec 2025 | 4.41 | x | Reported | Rel Feb page:11 |
| Credit-agreement interest coverage ratio (company-reported, minimum 1.50x) | 31 Dec 2025 | 2.01 | x | Reported | Rel Feb page:11 |
| Credit-agreement net leverage ratio (company-reported, maximum 5.75x through March 31, 2026, then 5.50x) | 31 Mar 2026 | 5.11 | x | Reported | Rel May page:10 |
| Credit-agreement interest coverage ratio (company-reported, minimum 1.50x) | 31 Mar 2026 | 1.85 | x | Reported | Rel May page:10 |

### Definitions and comparability

- **AOI.** Defined in the segment note as operating income before depreciation and amortization, cloud computing amortization, share-based compensation, impairment and other charges, restructuring and other related charges, and including the proportionate share of adjusted operating income of majority-owned equity method investees (10-Q Q2-26 page:28). It is a segment measure and a non-GAAP total; it is not EBITDA. Three consequences: it excludes restructuring cash costs (cash paid for restructuring initiatives was 19,729 in 6M 2026 against 7,920 in 6M 2025, Rel Jul page:11), it adds back equity-classified and some other share-based compensation, and it adds investee AOI that is not consolidated cash flow (6,762 in 6M 2026).
- **EBITDA on a reported basis.** Operating income plus depreciation and amortization, with no add-backs. The twelve-month windows to March 31 and June 30, 2026 include the Q4 2025 non-cash impairment and other charges of 97,784 (10-K page:134; Q4 2025 timing per 10-Q Q2-26 page:16), so this basis understates run-rate earnings; it is shown in C7 for transparency, not charted.
- **Net debt.** Principal of debt less cash and cash equivalents, no restricted cash adjustment (none is printed), no lease adjustment. The company's own leverage ratio (3.1x at FY2025, 3.4x at March 31, 2026, 4.1x at June 30, 2026) divides net debt and finance leases by AOI (Rel Feb page:11, Rel May page:9, Rel Jul page:11); the difference from C3 is the finance lease liability (13,882 at June 30, 2026, Rel Jul page:11).
- **Credit-agreement ratios.** Company-reported at December 31, 2025 and March 31, 2026 only; they follow credit-agreement definitions that differ from AOI and ended with the facility on May 12, 2026 (10-Q Q2-26 page:17). The remaining notes' covenants are not printed.

### Earnings and operating drivers

- Revenue fell to 547,495 in Q2 2026 from 600,024 in Q2 2025 (10-Q Q2-26 page:3). Subscription revenue fell from 367,428 to 352,514, advertising from 148,609 to 138,212 and content licensing and other from 83,987 to 56,769 (page:28-29). Management attributes the licensing decline mainly to delivery timing and to a music catalog sale and Silo production revenue in Q2 2025, and says it expects licensing revenue to vary through 2026 (page:44). It expects linear subscriber declines to continue and advertising to continue to decline (page:43-44).
- Operating income fell from 64,469 to 15,854 (page:3); the filing attributes this mainly to the 52.5 million revenue decrease (page:47). Domestic segment AOI fell from 126,339 to 60,972 while International was stable at 14,359 against 14,737 (page:28-29).
- Cost lines did not fall with revenue: technical and operating expenses rose from 283,876 to 288,781 and selling, general and administrative expenses from 221,704 to 224,698 (page:3).
- FY2025 earnings were helped by a gain on extinguishment of debt of 129,800 (10-K page:134) and hurt by the impairment of 97,784; Q2 2026 includes a loss on extinguishment of debt of 3,784 (page:3). Net income including noncontrolling interests was a loss of 36,929 in 6M 2026 against a profit of 74,859 in 6M 2025.

### Leverage, cover and cash flow

- On the AOI basis total debt to AOI rose from 4.32x at FY2025 to 5.54x at June 30, 2026 and net debt to AOI from 3.10x to 4.06x, driven by the denominator: net debt moved from 1,275,872 to 1,271,558 while twelve-month AOI fell from 411,874 to 313,045.
- Cash interest paid over the twelve months was 151,153 against AOI of 313,045, 2.07x. Interest expense in 6M 2026 was 84,012 against 85,852 a year earlier, even though the 10.50% notes now cover 1,315,098 of principal; the lower balance of the 4.25% notes and the Term Loan A offset the higher coupon (10-Q Q2-26 page:48). The full-year effect of the post-exchange structure is shown in C8.
- Operating cash flow was 124,659 in 6M 2026 against 211,596 in 6M 2025; free cash flow after capital expenditures was 108,082 against 189,926 (page:5, 64). Management states that free cash flow includes restructuring cash costs and other items that affect comparability (Rel Jul page:11). The twelve-month free cash flow of 190,523 (C5) compares with cash interest paid of 151,153.
- Uses of cash in 6M 2026 outside debt service included 30,000 for treasury stock (page:6). A further accelerated share repurchase of $30 million with final settlement expected in the fourth quarter of 2026 and $87 million of authorization remaining at June 30, 2026 are management statements (Rel Jul page:4).

### Liquidity and refinancing

- Liquidity at June 30, 2026 is cash of 463,996 (about $136.5 million held by foreign subsidiaries, of which about $22.5 million is expected to be repatriated; 10-Q Q2-26 page:55). The $175.0 million revolver and the Term Loan A were repaid or terminated on May 12, 2026 (page:17), so no committed facility remains in the sources. Management points to cash, operating cash flow, the receivables monetization program and new debt as sources (page:55); the program had no receivables sold and a limit of $125.0 million (page:10).
- Management states that it does not expect to generate enough cash from operations, with cash on hand, to repay all debt at maturity and will depend on capital markets access (page:55-56).
- In the 2026 exchange, about $830.6 million of 10.25% notes were tendered early and about $30.7 million at expiry (about $861.3 million together, sum of the printed amounts) for new 10.50% notes due 2032 of about $884 million and about $31.1 million (about $915.1 million together) (page:18); the remaining 13.7 million was redeemed April 6, 2026 at 105.125% (page:19). The extra principal of $53.8 million over the exchanged amount is a non-cash discount; third-party fees of $16.7 million were expensed in Miscellaneous, net (page:18).
- Off-balance sheet contractual obligations rose by $91.3 million to $590.3 million at June 30, 2026, mainly marketing and third-party service contracts (page:24).
- A customer filed for Chapter 11 on June 30, 2026; the filing does not name the customer or state the exposure (page:57).

### Subsequent events (after June 30, 2026, to the cutoff)

- July 30, 2026: Netflix licence agreement for co-exclusive global streaming rights to the Walking Dead Universe. Aggregate licence fee $500 million in quarterly cash installments over five years from each title's start date; expected cash of about $25 million in 2026 and about $100 million in each of 2027, 2028, 2029 and 2030, with the remainder in 2031; expected present-value revenue about $445 million; expected revenue recognition of $200 million to $225 million in each of 2026 and 2027 (10-Q Q2-26 page:10, 68; Rel Jul page:4). These are management expectations; the contract is not supplied.
- Trial in the MFN Litigation was scheduled for October 27, 2026 with plaintiffs claiming damages in excess of $200 million (10-Q Q2-26 page:24). No later source reports an outcome, and none is assumed.
- No source dated after July 30, 2026 is supplied.

### Data quality and definition risks

- Text-only extraction: the figures above were read from page text. Tables were checked against totals where the filing prints one: the June 30, 2026 debt lines add to the printed total of 1,735,554, and the twelve-month AOI rebuilds to the printed figures (C1).
- The 10-K guarantee wording ("on an unsecured basis", page:112) and the first-priority lien description for the 2032 notes (page:171) are not reconciled by the sources; this handoff makes no statement on ranking.
- Leverage is shown on the AOI basis only because it is the one non-GAAP earnings measure for which the company prints a reconciliation; it adds back items that are real cash costs (restructuring, share-based awards settled in cash for directors).

## Calculations

All amounts are USD thousands unless stated.

**C1. Twelve-month (LTM) build to June 30, 2026 = FY2025 + 6M 2026 - 6M 2025.**
- Revenue: 2,311,801 + 1,089,622 - 1,155,257 = 2,246,166.
- Operating income: 133,322 + 47,115 - 128,666 = 51,771 (equals Rel Jul page:11).
- Depreciation and amortization: 94,425 + 38,243 - 47,372 = 85,296 (equals Rel Jul page:11).
- Interest expense: 172,353 + 84,012 - 85,852 = 170,513.
- AOI: 411,874 + 115,042 - 213,871 = 313,045 (equals Rel Jul page:11). For March 31, 2026: 411,874 + 68,974 - 104,485 = 376,363 (equals Rel May page:9), where 68,974 and 104,485 are the printed Q1 2026 and Q1 2025 AOI (Rel May page:10).

**C2. Twelve-month cash interest paid.**
- To June 30, 2026: 156,563 (FY2025) + 78,984 (6M 2026) - 84,394 (6M 2025) = 151,153.
- To March 31, 2026: 156,563 + 77,983 (Q1 2026, 10-Q Q1-26 page:23) - 76,736 (Q1 2025, same page) = 157,810.

**C3. Leverage on the AOI basis.**
- Net debt = total debt principal less cash. FY2025: 1,778,251 - 502,379 = 1,275,872. March 31, 2026: 1,829,284 - 552,137 = 1,277,147 (equals Rel May page:9). June 30, 2026: 1,735,554 - 463,996 = 1,271,558.
- Total debt / AOI: FY2025 1,778,251 / 411,874 = 4.32x; March 2026 1,829,284 / 376,363 = 4.86x; June 2026 1,735,554 / 313,045 = 5.54x.
- Net debt / AOI: 1,275,872 / 411,874 = 3.10x; 1,277,147 / 376,363 = 3.39x; 1,271,558 / 313,045 = 4.06x.
- Company-style check including finance leases: June 30, 2026 net debt and finance leases 1,285,440 / 313,045 = 4.11x, which the company prints as 4.1x (Rel Jul page:11).

**C4. AOI / cash interest paid.** FY2025 411,874 / 156,563 = 2.63x; LTM March 2026 376,363 / 157,810 = 2.38x; LTM June 2026 313,045 / 151,153 = 2.07x.

**C5. Cash flow.** LTM operating cash flow = 305,670 + 124,659 - 211,596 = 218,733. LTM capital expenditures = 33,303 + 16,577 - 21,670 = 28,210. LTM free cash flow = 218,733 - 28,210 = 190,523. FY2025 free cash flow = 305,670 - 33,303 = 272,367. The 6M free cash flows are printed (10-Q Q2-26 page:64).

**C6. Program rights obligations.** December 31, 2025: 258,252 (current) + 181,773 (noncurrent) = 440,025. June 30, 2026: 226,312 + 155,386 = 381,698 (10-Q Q2-26 page:2). Not included in debt, net debt or the leverage ratios.

**C7. Reported-basis EBITDA (operating income plus depreciation and amortization, no add-backs) and ratios.** FY2025: 133,322 + 94,425 = 227,747; debt 7.81x, net debt 5.60x, cover 1.45x on cash interest paid of 156,563. LTM March 2026: 100,386 + 94,922 = 195,308 (Rel May page:9); 9.37x, 6.54x, 1.24x on 157,810. LTM June 2026: 51,771 + 85,296 = 137,067; 12.66x, 9.28x, 0.91x on 151,153. These windows include the 97,784 impairment, so the multiples are shown to expose the gap between reported and adjusted earnings, not as run-rate leverage.

**C8. Run-rate contractual coupon on notes outstanding at June 30, 2026 (assumes principal at June 30, 2026 for a full year, excludes discount amortization and interest income).** 1,315,098 x 10.50% = 138,085; 276,706 x 4.25% = 11,760; 143,750 x 4.25% = 6,109; total 155,955. LTM AOI 313,045 / 155,955 = 2.01x. Coupon rates are from the instrument labels and the 10-K debt note (page:171, 175-176).

**C9. Covenant-style headroom at March 31, 2026 (last reported, facility since ended).** Net leverage: the maximum was 5.75x through March 31, 2026 (10-Q Q1-26 page:14), so 5.75x less 5.11x reported = 0.64x; the step-down to 5.50x applied after that date and would have left 0.39x on the same ratio. Interest coverage 1.85x reported less 1.50x minimum = 0.35x. No headroom is computed for June 30, 2026: Not calculable, because the credit agreement ended on May 12, 2026 and the notes' covenants are not printed.

**C10. Netflix cash timing (management expectation).** Aggregate $500 million; about $25 million in 2026 plus four years at about $100 million equals about $425 million; the remainder due in 2031 is therefore about $75 million, derived by subtraction, not printed.

**C11. Debt maturity grouping.** 2029: 276,706 + 143,750 = 420,456. 2032: 1,315,098. Total 1,735,554, equal to the printed total debt at June 30, 2026.

## Gaps

- Not supplied: any report or filing after July 30, 2026 (CP-0 L1). Q3 2026 results are not in the sources; figures here run to June 30, 2026.
- Not supplied: executed credit agreement, indentures and supplemental indentures (CP-0 L2). Covenants of the surviving notes, security package and guarantee ranking are not printed; the credit-agreement ratios cannot be extended past March 31, 2026 (CP-0 L3). Covenant headroom at June 30, 2026 is Not calculable.
- Not supplied: letters of credit drawn on the revolver before its termination; none is printed in the sources after a search for "letters of credit", "LC", "L/C", "standby" and "surety". The $175.0 million undrawn figure is therefore shown gross.
- Not supplied: a debt maturity table in the 10-Q; maturities are read from the instrument labels (final maturity month and year), and the exact day of the 4.25% Senior Notes maturity was not read.
- Not supplied: quarterly cash interest paid for Q2 2026 and Q2 2025 as printed; they can be derived from six-month less three-month amounts but are not charted.
- Not supplied: AOI for FY2024 and earlier in this handoff; not needed for the requested periods.
- Not supplied: ratings, market prices, peers, and the identity and exposure of the customer in Chapter 11 (CP-0 L7).
- Perimeter: consolidated, including non-wholly-owned entities at 100%; restricted and unrestricted subsidiary splits are Not supplied (CP-0 L5). Majority-owned equity investees AOI is included in AOI.
- Net debt excludes lease liabilities (88,600 at June 30, 2026), program rights obligations (381,698) and the 590.3 million of off-balance sheet obligations; these are shown separately and are not in any ratio.
- Extraction is text only; table alignment was checked against printed totals where available (CP-0 L8).

## Next module

Pass to CP-1A with the following carried forward: leverage and cover are on the AOI basis; the credit-agreement ratios and revolver ended on May 12, 2026; liquidity at June 30, 2026 is cash of 463,996 with no committed facility; maturities are 420,456 in February 2029 and 1,315,098 in July 2032; the Netflix licence and the October 27, 2026 trial are subsequent events with no outcome supplied. CP-2 and CP-5 should treat the C-numbered calculations here as the source of every derived figure and the CP-0 limitations L1 to L11 as still in force.
