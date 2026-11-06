## Request

Issuer: Rithm Capital Corp. (issuer id ritm; NYSE: RITM), reporting entity "Rithm Capital Corp. and subsidiaries", consolidated. As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency per the context: USD. Current period: Q3 2026 (quarter ended September 30, 2026; nine months 2026 where stated); prior period: FY2025 (year ended December 31, 2025).

Task: CP-1, the financial base. Extract the reported financial statements, debt, liquidity, covenant and maturity facts from the pinned filings; label every figure with its period and perimeter; show every derived number; and keep conflicts, gaps and limitations explicit. This module gives no credit conclusion beyond what the figures support and no valuation view.

Units: filing tables are in US$ thousands unless a locator says billions or millions. The four chart-data tables are in US$m (thousands divided by 1,000; shown to three decimals so no digit is lost). Locators use `page:N`, the retained text chunk number, not the printed page.

Perimeter note: the issuer is the registrant Rithm Capital Corp., and every statement used here is consolidated. Much of the debt sits in consolidated subsidiaries and securitization or fund entities. The filings split contractual maturities into "Non-recourse" and "Recourse" columns, and state that creditors of the consolidated VIEs "do not have recourse to Rithm Capital Corp." (10-Q Q3 page:56). No parent-only statements exist in the pack. The consolidated figures are therefore group figures, not parent-creditor figures.

## Sources

### Issuer sources relied on (pack files, sha256 of the pinned text file)

| Source name | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_nrz-20251231.htm.jsonl | 1c6dc6fc4ac22ec0f983aa2d74b8236f15d06cb3d694e11e9adbcc9895b8a598 | FY2025 statements, FY2025 debt table, maturities, capacity, cash paid for interest |
| 10-Q_2026-03-31_nrz-20260331.htm.jsonl | 767e2e953064f6127dd3b7225c6f0b5f7530f4df6d8ed091932733330f9a34a9 | Opened for identity and period only; Q1 2026 figures are not carried into the tables |
| 10-Q_2026-06-30_nrz-20260630.htm.jsonl | 6daf210aa16182f6824c848a97ad4428da4dc1534373b7320d814299eab6f84f | Opened for identity and period only; Q2 2026 figures are not carried into the tables |
| 10-Q_2026-09-30_nrz-20260930.htm.jsonl | fe67ca59ff02f150e9ee570dc94fbca4e7146def420f7701280eb0487eeda6c4 | Primary source: Q3 2026 and nine months 2026 statements, Note 17 debt, maturities, capacity, covenants, MD&A liquidity, commitments |
| EX-99.1_2026-04-28_ritm-2026331x8xkxexhibit991.htm.jsonl | 7f51477fb7c8b90bc73114496ecaaec4ef4c755e9b5be36834e7ff89e1e4f463 | Not relied on for figures in this module |
| EX-99.1_2026-07-28_ritm-2026630x8xkxexhibit991.htm.jsonl | 67986b436cacab7f9ff46416cb7f57062e1228ff3e0789e90880132c1b737079 | Earnings available for distribution, Q2 2026 (supporting) |
| EX-99.1_2026-10-23_ritm-2026930x8xkxexhibit991.htm.jsonl | 7701308b9bdf89d27236cd23ca8f47f1dead7d427d8e354df0b2502bcac258f6 | Q3 2026 highlights, non-GAAP measure, management narrative (supporting, attributed) |

Context file (user settings, not issuer evidence): 73b514b2c18312238fd1fbb7bdc629559e11381beb8e9b95dfc9d7b54bcabe9d.

### Supplied handoffs

| Module | sha256 | How used |
| --- | --- | --- |
| CP-0 | 48c6d7ae503045da1cae2c5c7a86ddde9f062574551bdb4f6c2d47743f9e2c09 | Source-readiness view. Its gaps (no indentures, facility agreements, ratings or decks) and its listed conflicts are carried forward; one of its conflict entries is refined in Findings and Calculations below. |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Rithm is a large, mostly secured and heavily short-dated funder of mortgage and real estate assets. Debt is about half recourse, near-term maturities are heavy, unrestricted cash is modest against them, and no EBITDA is reported. | Medium | Committed undrawn capacity, covenant levels and the unencumbered-asset figure are not printed, so liquidity headroom and covenant headroom cannot be calculated. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Contractual maturities through the end of 2027 are a large share of total debt, with a big part recourse to the parent. | Refinancing and rollover of secured lines is the central credit risk for parent creditors. | High |
| Available financing under secured lines is described as uncommitted and collateral-dependent. | Stated capacity is not committed liquidity, so true headroom is lower than the capacity figure suggests. | High |
| Leverage on equity is high on a total basis and meaningfully lower on a recourse basis. | The senior unsecured notes sit behind secured and structurally senior non-recourse debt. | Medium |
| Earnings are volatile because of mortgage servicing rights fair value changes, and nine-month 2026 earnings are below the prior year. | Coverage of funding costs depends on market-sensitive items, not stable cash earnings. | Medium |
| The filings print compliance statements but no covenant levels or headroom. | Covenant risk cannot be measured from the pack; only compliance is evidenced. | Medium |

### Financial base view

The financial base is usable but must be read as a specialty-finance balance sheet rather than an operating-company credit. The group funds a mortgage, servicing, transitional-lending, asset-management and commercial real estate book mainly with secured repurchase and warehouse lines, secured notes and bonds, and consolidated securitization and fund debt, with a small layer of parent senior unsecured notes. Total contractual debt at September 30, 2026 was US$37,877.221m on the maturity-table basis, of which US$19,680.259m is classed as recourse and US$18,196.962m as non-recourse (10-Q Q3 page:57). The filings report no EBITDA, so the leverage and cover charts carry "Not supplied" and the credit read rests on debt to equity, the recourse split, the maturity profile, unrestricted cash and earnings cover of interest, all derived in Calculations. The strongest contrary evidence to a benign view is the maturity wall: US$7,546.015m falls due October 1 to December 31, 2026 and US$10,619.584m in 2027, and available financing is stated to be uncommitted. Earnings are market-sensitive: the change in fair value of MSRs net of economic hedges was a gain of 121,277 in Q3 2026 against a loss of 264,351 in Q3 2025, and a loss of 475,827 in nine months 2026 against a loss of 752,734 in nine months 2025 (US$ thousands, 10-Q Q3 page:8), and nine-month 2026 net income of 438,665 is below 627,514 in nine months 2025. Earnings available for distribution, a non-GAAP measure, were US$315.3m in Q3 2026 against US$338.9m in Q2 2026 (release Q3 page:1). The senior unsecured notes are unsecured and, at issuance, not guaranteed by any subsidiary, so they rank behind secured lenders on pledged collateral and behind subsidiary-level debt in the structure (10-Q Q3 page:59). The strongest supportive evidence is the filed statement that Rithm was in compliance with all debt covenants at September 30, 2026 and that about US$1.1 billion of liquidity held in the servicers exceeds regulatory requirements. Neither can be tested further without the facility agreements and indentures.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | Not supplied: the 10-K reports no EBITDA or adjusted EBITDA | Not supplied: the 10-K reports no EBITDA or adjusted EBITDA | x | Interest on warehouse and repurchase funding is an operating cost of this business, and no source defines an EBITDA. A constructed measure would mix non-recourse and recourse debt; see Calculations for the debt to equity measures used instead. Source: 10-K page:229. |
| Q3 2026 | Not supplied: the 10-Q and release report no EBITDA or adjusted EBITDA | Not supplied: the 10-Q and release report no EBITDA or adjusted EBITDA | x | The only adjusted earnings measure is earnings available for distribution, a non-GAAP per-share measure that is not EBITDA (release Q3 page:3). Same limitation as FY2025. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | Not supplied: no EBITDA is reported | x | Cash paid for interest is printed (US$1,765,292 thousand, 10-K page:233) but the numerator is not. An earnings cover of interest using pre-tax income is shown in Calculations and is not EBITDA. |
| Q3 2026 | Not supplied: no EBITDA is reported | x | Nine-month 2026 cash paid for interest and warehouse line fees is printed (US$1,406,118 thousand, 10-Q Q3 page:13); no quarterly cash interest figure is printed. Same numerator limitation. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2025 (FY2025) | 1847.626 | Not supplied: borrowing capacity is stated to be uncommitted and no committed undrawn amount is printed | US$m | Cash and cash equivalents excluding restricted cash of US$809.312m (10-Q Q3 page:44). Available financing of US$7,727.531m at December 31, 2025 is uncommitted (10-K page:314 to page:315). |
| Sep 30, 2026 (Q3 2026) | 1708.750 | Not supplied: borrowing capacity is stated to be uncommitted and no committed undrawn amount is printed | US$m | Cash and cash equivalents excluding restricted cash of US$740.572m and restricted cash of consolidated entities of US$101.715m (10-Q Q3 page:44). Available financing of US$10,785.284m is uncommitted and collateral-dependent (10-Q Q3 page:57); it is not counted as undrawn committed facilities. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q4 2026 (Oct 1 to Dec 31, 2026) | 7546.015 | US$m | Contractual maturities as of Sep 30, 2026, recourse plus non-recourse (10-Q Q3 page:57). Includes secured financing, secured notes and bonds, senior unsecured notes net and consolidated-entity notes. Recourse part: US$6,230.073m. |
| 2027 | 10619.584 | US$m | Same basis. Recourse part: US$6,736.955m. |
| 2028 | 3255.192 | US$m | Same basis. Recourse part: US$1,735.576m. |
| 2029 | 4375.281 | US$m | Same basis. Recourse part: US$2,430.775m; the 8.000% senior notes due April 1, 2029 are in this year. |
| 2030 | 1621.974 | US$m | Same basis. Recourse part: US$560.860m; the 8.000% senior notes due July 15, 2030 are in this year. |
| 2031 and thereafter | 10459.175 | US$m | Same basis. Recourse part: US$1,986.020m; the 8.500% senior notes due June 1, 2031 are in this bucket. |

### Financials and credit metrics

| Metric | FY2025 | Nine months 2025 | Nine months 2026 | Q3 2025 | Q3 2026 | Unit, basis and locator |
| --- | --- | --- | --- | --- | --- | --- |
| Total revenues | 4,590,228 | 3,307,056 | 4,423,413 | 1,108,214 | 1,756,422 | US$ thousands, flows. 10-K page:228 to page:229; 10-Q Q3 page:8 |
| Interest expense and warehouse line fees | 1,662,433 | 1,239,612 | 1,395,011 | 402,690 | 480,834 | US$ thousands, flows. 10-K page:229; 10-Q Q3 page:8 |
| Depreciation and amortization | 107,477 | 71,492 | 278,619 | 23,130 | 92,428 | US$ thousands, flows. FY2025 from the general and administrative breakdown (10-K page:199) because the FY2025 income statement shows no separate line; other columns from 10-Q Q3 page:8 and page:12 |
| Total expenses | 3,992,876 | 2,818,772 | 3,789,695 | 938,855 | 1,276,490 | US$ thousands, flows. 10-K page:229; 10-Q Q3 page:8 |
| Income before income taxes | 806,383 | 600,058 | 760,219 | 236,870 | 519,093 | US$ thousands, flows. 10-K page:229; 10-Q Q3 page:8 |
| Income tax expense (benefit) | 88,291 | (27,456) | 321,554 | 8,072 | 257,819 | US$ thousands, flows. 10-K page:229; 10-Q Q3 page:8 |
| Net income | 718,092 | 627,514 | 438,665 | 228,798 | 261,274 | US$ thousands, flows. 10-K page:229; 10-Q Q3 page:8 |
| Net income attributable to common stockholders | 567,200 | 514,084 | 305,150 | 193,662 | 217,126 | US$ thousands, flows, after preferred dividends. 10-K page:229; 10-Q Q3 page:8 |
| Preferred dividends | 114,246 | 82,371 | 107,104 | 27,876 | 36,159 | US$ thousands, flows. 10-K page:229; 10-Q Q3 page:8 |
| Net cash used in operating activities | (1,292,051) | (1,177,470) | (1,313,851) | Not supplied: quarterly cash flow not printed | Not supplied: quarterly cash flow not printed | US$ thousands, flows. Operating cash flow includes mortgage loans originated for sale. 10-K page:232; 10-Q Q3 page:12 |
| Net cash provided by (used in) investing activities | 2,671,482 | 1,222,360 | (2,521,808) | Not supplied: quarterly cash flow not printed | Not supplied: quarterly cash flow not printed | US$ thousands, flows. 10-K page:232; 10-Q Q3 page:12 |
| Net cash provided by (used in) financing activities | (507,827) | 283,075 | 3,597,283 | Not supplied: quarterly cash flow not printed | Not supplied: quarterly cash flow not printed | US$ thousands, flows. 10-K page:233; 10-Q Q3 page:13 |
| Cash paid for interest (and warehouse line fees in 2026 and nine months 2025) | 1,765,292 | 1,319,811 | 1,406,118 | Not supplied: quarterly cash interest not printed | Not supplied: quarterly cash interest not printed | US$ thousands, flows. 10-K page:233 (caption "interest"); 10-Q Q3 page:13 |
| Cash paid for income taxes, net of refunds | 15,797 | 22,743 | 11,398 | Not supplied: quarterly cash taxes not printed | Not supplied: quarterly cash taxes not printed | US$ thousands, flows. 10-K page:233; 10-Q Q3 page:13 |
| Dividends paid on common and preferred stock | 643,195 | 476,770 | 525,047 | Not supplied: quarterly cash flow not printed | Not supplied: quarterly cash flow not printed | US$ thousands, flows. 10-K page:233; 10-Q Q3 page:13 |
| Total assets | 53,063,126 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 56,661,330 | US$ thousands, instants at Dec 31, 2025 (FY2025 column) and Sep 30, 2026 (Q3 2026 column). 10-Q Q3 page:7 |
| Total liabilities | 43,808,416 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 47,124,374 | US$ thousands, instants. 10-Q Q3 page:7 |
| Stockholders' equity in Rithm Capital Corp. (includes preferred stock) | 8,430,487 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 8,620,062 | US$ thousands, instants. 10-Q Q3 page:7 |
| Total stockholders' equity (includes non-controlling interests) | 8,940,407 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 9,141,357 | US$ thousands, instants. 10-Q Q3 page:7 |
| Cash and cash equivalents (unrestricted) | 1,847,626 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 1,708,750 | US$ thousands, instants. 10-Q Q3 page:44 |
| Restricted cash (excluding consolidated entities) | 809,312 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 740,572 | US$ thousands, instants. 10-Q Q3 page:44 |
| Secured financing agreements (carrying) | 13,763,802 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 14,235,647 | US$ thousands, instants. 10-Q Q3 page:7 |
| Secured notes and bonds payable (carrying) | 15,203,770 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 14,011,438 | US$ thousands, instants. 10-Q Q3 page:7 |
| Notes payable and secured financing of consolidated entities (carrying) | 4,897,802 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 7,399,680 | US$ thousands, instants. Inside "Liabilities of Consolidated Entities", not a separate balance sheet line. 10-Q Q3 page:54 |
| Senior unsecured notes, net | 1,258,271 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 1,755,476 | US$ thousands, instants. 10-Q Q3 page:57 to page:58 |
| Tax receivable agreement liability | 162,817 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 151,677 | US$ thousands, instants. Presented in unsecured notes, net, but not a note. 10-Q Q3 page:58 |
| Contractual debt maturities, total (recourse plus non-recourse) | 35,443,392 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 37,877,221 | US$ thousands, instants, principal basis. 10-K page:314; 10-Q Q3 page:57 |
| Of which recourse | 19,496,781 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 19,680,259 | US$ thousands, instants. Same locators |
| Of which non-recourse | 15,946,611 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 18,196,962 | US$ thousands, instants. Same locators |
| Total debt, carrying, incl. senior notes (derived) | 35,123,645 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 37,402,241 | US$ thousands, derived in Calculations, excludes the tax receivable agreement |
| Total debt / equity in Rithm Capital Corp., principal basis (derived), in x | 4.20 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 4.39 | x, derived in Calculations |
| Recourse debt / equity in Rithm Capital Corp., principal basis (derived), in x | 2.31 | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | Not supplied: balance sheet date not presented | 2.28 | x, derived in Calculations |
| Pre-tax income plus interest expense, divided by interest expense (derived), in x | 1.49 | 1.48 | 1.54 | Not supplied: not computed for the quarter | Not supplied: not computed for the quarter | x, derived in Calculations; not EBITDA cover |

### Debt instruments, as of September 30, 2026

Issuer of the senior notes: Rithm Capital Corp. (the registrant). The secured lines are borrowed by Rithm Capital Corp. and by its consolidated subsidiaries (including Newrez, NRM, Genesis and consolidated funds and securitization entities); the filing does not name the borrower of each line, and it states that "Certain of the debt obligations included above are obligations of Rithm Capital’s consolidated subsidiaries, which own the related collateral" (10-Q Q3 page:56). Co-issuers are not stated for any line. Source for the table: 10-Q Q3 page:53 to page:54; US$ thousands.

| Instrument or collateral class | Face amount | Carrying value | Final stated maturity | Weighted average funding cost | Carrying value Dec 31, 2025 |
| --- | --- | --- | --- | --- | --- |
| Warehouse credit facilities, residential mortgage loans | 4,231,284 | 4,231,284 | Oct-26 to Apr-28 | 5.3 % | 5,091,525 |
| Warehouse credit facilities, RTLs | 3,276,190 | 3,276,190 | Nov-26 to Jun-28 | 5.9 % | 2,019,808 |
| Secured financing: government and government-backed securities | 4,722,683 | 4,722,683 | Oct-26 to Feb-27 | 4.0 % | 5,130,519 |
| Secured financing: non-Agency securities | 1,072,546 | 1,072,546 | Oct-26 to Oct-27 | 5.3 % | 936,424 |
| Credit Risk Transfer LLC | 110,688 | 110,688 | Dec-26 | 6.5 % | 110,688 |
| Excess MSRs financing | 202,000 | 202,000 | Sep-28 | 6.0 % | 201,660 |
| CLOs (secured financing) | 280,531 | 278,912 | Apr-34 to Oct-39 | 5.2 % | 257,796 |
| Real estate (secured financing) | 341,344 | 341,344 | Mar-28 to Feb-29 | 6.1 % | 15,382 |
| Total secured financing agreements | 14,237,266 | 14,235,647 | n/a | 5.1 % | 13,763,802 |
| Secured notes and bonds: MSRs | 7,241,721 | 7,229,602 | Oct-26 to Nov-31 | 6.9 % | 6,785,138 |
| Secured notes and bonds: servicer advance investments | 206,598 | 206,598 | Oct-27 | 6.2 % | 229,069 |
| Secured notes and bonds: servicer advances | 2,259,139 | 2,258,416 | Dec-26 to Jun-29 | 6.3 % | 2,528,896 |
| Secured notes and bonds: consumer loans | 715,700 | 698,137 | Oct-26 to Sep-37 | 4.7 % | 660,565 |
| Secured notes and bonds: real estate | 3,688,584 | 3,549,482 | Dec-26 to May-31 | 4.6 % | 4,755,270 |
| Secured notes and bonds: RTLs | Not supplied: printed as a dash, no balance | Not supplied: printed as a dash, no balance | N/A | N/A | 200,000 |
| Secured notes and bonds: other investments | 69,203 | 69,203 | Feb-30 to Jul-30 | 6.0 % | 44,832 |
| Total secured notes and bonds payable | 14,180,945 | 14,011,438 | n/a | 6.1 % | 15,203,770 |
| Consolidated entities: consolidated funds | 970,748 | 951,443 | Aug-27 to Jan-38 | 5.7 % | 1,209,739 |
| Consolidated entities: residential mortgage loan securitizations | 5,140,675 | 4,879,187 | Sep-48 to Jul-56 | 5.1 % | 2,820,922 |
| Consolidated entities: RTL securitizations | 1,058,756 | 1,055,132 | Sep-32 to Sep-39 | 6.2 % | 867,141 |
| Consolidated entities: consumer loan securitizations | 513,831 | 513,918 | Mar-37 to May-37 | 5.3 % | Not supplied: no December 31, 2025 balance printed |
| Total notes payable and secured financing of consolidated entities | 7,684,010 | 7,399,680 | n/a | 5.3 % | 4,897,802 |
| Total, Note 17 | 36,102,221 | 35,646,765 | n/a | 5.5 % | 33,865,374 |

Secured lines: the filing states that Rithm Capital "has margin exposure on $14.2 billion of secured financing agreements" and that a fall in collateral value below the margin trigger "could significantly impact its liquidity" (10-Q Q3 page:56). Of the MSR notes, US$6.2 billion floats at SOFR plus 2.5% to 3.0% and US$1.1 billion is fixed at 3.5% to 7.4% (10-Q Q3 page:55 note H). Collateral of the consolidated securitization entities is "not available to other creditors of Rithm Capital Corp." (10-Q Q3 page:56).

Parent senior unsecured notes (principal amounts from Note 17 and the MD&A; all issued by Rithm Capital Corp.; senior unsecured; not guaranteed by any subsidiary at issuance, with no obligation to add guarantors except in limited specified circumstances; trustee for the 2031 notes is U.S. Bank Trust Company, National Association):

| Notes | Principal | Rate | Issued | Maturity | Redemption | Covenant text |
| --- | --- | --- | --- | --- | --- | --- |
| 8.000% senior notes due 2029 | 775,000 | 8.000%, semi-annual April 1 and October 1 | March 19, 2024, issue price 98.981% | April 1, 2029 | Callable from April 1, 2026 at 104.000, 102.000 in 2027, 100.000 from 2028 | Total Unencumbered Assets not less than 120% of outstanding unsecured debt; change of control and Mortgage Business Triggering Event put at 101% |
| 8.000% senior notes due 2030 | 500,000 | 8.000%, semi-annual January 15 and July 15 | June 20, 2025 | July 15, 2030 | Callable from July 15, 2027 | Same 120% test and 101% put |
| 8.500% senior notes due 2031 | 500,000 | 8.500%, semi-annual June 1 and December 1 from December 1, 2026 | May 14, 2026, net proceeds approximately US$493.7 million | June 1, 2031 | Callable from June 1, 2028 at 104.250, 102.125 in 2029, 100.000 from 2030; to 40% at 108.500 before June 1, 2028 with equity proceeds; make-whole before then | Same 120% test |

Principal sources: 10-Q Q3 page:58 to page:63 and page:168. The 2025 senior notes were fully redeemed in the second quarter of 2025 (10-Q Q3 page:63). The tax receivable agreement liability (US$151,677 thousand) sits in the same balance sheet line but is not a note (10-Q Q3 page:58).

### Claims outside the debt figure

Stated at September 30, 2026 unless noted; none of these is inside the US$37,877.221m maturity-table debt.

| Claim | Amount | Inside or outside debt | Locator |
| --- | --- | --- | --- |
| Residential mortgage loan repurchase liability (Ginnie Mae buyout right, offset by an equal asset) | 4,594,747 | Outside debt; balance sheet liability | 10-Q Q3 page:7 |
| Interest sensitive insurance contract liabilities | 1,206,009 | Outside debt | 10-Q Q3 page:7 |
| Dividends payable | 190,451 | Outside debt | 10-Q Q3 page:7 |
| Preferred stock, aggregate liquidation preference (carrying value 1,632,915) | 1,689,104 | Equity; outside debt | 10-Q Q3 page:7; page:112 |
| Redeemable non-controlling interests | 395,599 | Mezzanine; outside debt | 10-Q Q3 page:7 |
| Operating lease liabilities, discounted | 157,921 | Outside debt (inside accrued expenses and other liabilities) | 10-Q Q3 page:49 |
| Finance lease liabilities, discounted | 914 | Outside debt | 10-Q Q3 page:49 |
| Unfunded capital commitments to funds, guaranteed by the Company if executive managing directors fail to fund | 483.7 million (US$) | Contingent; outside debt | 10-Q Q3 page:119 |
| Genesis commitments to fund additional advances on existing loans | 2.2 billion (US$) | Commitment; outside debt | 10-Q Q3 page:118 |
| Unfunded commitments on CRE loans | 66.3 million (US$) | Commitment; outside debt | 10-Q Q3 page:118 |
| Estimated liability for representations and warranties | 41.9 million (US$) | Reserve; outside debt | 10-Q Q3 page:117 |
| 60 Wall Street completion guarantee, liability recorded | 12.0 million (US$), with an equal indemnification asset | Contingent; outside debt | 10-Q Q3 page:120 |
| Non-recourse carve-out, completion, environmental and carry guarantees on two CRE projects | Not supplied: "subject to significant uncertainty" | Contingent; outside debt | 10-Q Q3 page:119 |

Pensions and retiree medical: no defined benefit pension or retiree medical obligation was found in the 10-Q Q3 or 10-K text searched. Purchase commitments: a fixed price construction contract for 171 single-family rental properties had US$2.9 million of the purchase price outstanding (10-Q Q3 page:118); no other purchase or capacity commitment was found. Factoring and supply-chain finance: none found in the text searched. Letters of credit and standby facilities: none found in the text searched. Litigation and consent decrees: the 10-Q Q3 says "Rithm Capital is, from time to time, subject to inquiries by government entities" and does not believe any would be material (10-Q Q3 page:186); no litigation reserve or consent decree amount is printed.

### Liquidity

Unrestricted cash and cash equivalents at September 30, 2026 were US$1,708.750m (10-Q Q3 page:44), against US$1,847.626m at December 31, 2025. The MD&A says "approximately $1.7 billion of available liquidity was held at NRM and Newrez, of which $1.1 billion was in excess of the regulatory liquidity requirements" (10-Q Q3 page:165); the filing does not say how this overlaps with consolidated cash, so it is not added to it. Available financing under secured lines was US$10,785.284m of US$29,121.824m capacity at September 30, 2026 (10-Q Q3 page:57), by facility: residential mortgage loans, RTLs, Credit Risk Transfer LLC and real estate 3,021,445; loan originations 3,918,467; CLOs 459,656; Excess MSRs 148,000; MSR notes 402,000; servicer advances 2,704,263; real estate 59,722; consolidated funds 71,731 (US$ thousands). The filing states "Although available financing is uncommitted" (10-Q Q3 page:57), so none of it is counted as undrawn committed facilities; servicer advance facilities are described as "non-recourse committed facilities" (10-Q Q3 page:137) but no committed undrawn amount is split out. No letters of credit drawn on facilities are disclosed in the text searched. Facilities with stated maturities within twelve months of September 30, 2026 are numerous: warehouse lines (Oct-26 onward), the government securities and non-Agency repurchase lines (Oct-26 to Feb-27 and Oct-26 to Oct-27), and Credit Risk Transfer LLC (Dec-26). Management says it expects cash on hand, operating cash flow and "our ability to extend or refinance our secured financing agreements and servicer advance financings" to satisfy needs for the next 12 months and that "Our ability to extend or refinance short-term borrowings is critical to our liquidity outlook" (10-Q Q3 page:172).

### Covenants

| Test | Level | Reported figure | Headroom | Note |
| --- | --- | --- | --- | --- |
| Senior notes (2029, 2030, 2031): Total Unencumbered Assets not less than 120% of aggregate principal amount of outstanding unsecured debt of the Company | 120% | Not supplied: the filings give compliance only | Not calculable: Total Unencumbered Assets and its indenture definition are not in the pack | The indenture definition differs from any asset or debt measure computed here |
| Corporate secured facilities: event of default on specified declines in equity, or failure to maintain tangible net worth, liquidity or indebtedness to tangible net worth ratio | Not supplied: no level printed | Not supplied | Not calculable | Compliance stated at September 30, 2026 (10-Q Q3 page:57) |
| FHFA and Ginnie Mae servicer standards: minimum tangible net worth, tangible net worth to tangible assets of 6% or greater, base liquidity, additional origination liquidity of 50 bps | 6% and bps formulas as printed | Not supplied: compliance stated, no ratio | Not calculable | 10-Q Q3 page:166; Ginnie Mae risk based capital ratio of at least 6% also required |

### Latest quarter and subsequent events

Q3 2026 (quarter ended September 30, 2026): net income attributable to common stockholders of US$217,126 thousand against US$20,193 thousand in Q2 2026 (release Q3 page:4), with income tax expense of US$257,819 thousand on pre-tax income of US$519,093 thousand (10-Q Q3 page:8). Elecor sold a 49% interest in a CRE joint venture, deconsolidated it and recognised a gain of US$26.8 million (10-Q Q3 page:38); the Note 17 roll-forward shows a US$900,000 thousand deconsolidation of secured notes on real estate in the nine months (10-Q Q3 page:56). Management states (release Q3 page:2, attributed, not independently verified) a US$515 million refinancing of 31 West 52nd Street, an inaugural US$375 million RTL securitization, two NQM securitizations totalling US$975 million of UPB and a US$306 million home improvement loan securitization. The Upgrade forward flow agreement was amended to extend the expiry from October 31, 2026 to August 21, 2027 and add US$1.2 billion of purchase commitments (10-Q Q3 page:35). Earlier in the nine months: the US$500.0 million 8.500% notes due 2031 on May 14, 2026 and Series F preferred stock on January 13, 2026 for net proceeds of approximately US$242.1 million (10-Q Q3 page:58; page:111).

Subsequent events: the Q3 10-Q is signed October 30, 2026, and its Note 27 reports no subsequent events requiring recognition or additional disclosure (10-Q Q3 page:125). The cover shows 558,407,031 shares outstanding as of October 28, 2026 (10-Q Q3 page:2). A purchase of Agency RMBS of US$535,039 thousand was "settled after quarter-end" (10-Q Q3 page:13). Future-dated terms, labelled as such: the Series D preferred dividend rate resets on November 15, 2026 to the five-year Treasury rate plus 6.223% (10-Q Q3 page:174); the first interest payment on the 2031 notes is December 1, 2026. Nothing dated after the cutoff of 2026-11-05 is used as fact.

### Conflicts, corrections and carried-forward limitations

1. Total debt, refining the CP-0 entry. CP-0 listed the MD&A total of "$38.1 billion", the Note 17 face total and the maturity-table total as three unreconciled figures. The first two can now be bridged: the maturity-table total of US$37,877.221m equals the Note 17 face total of US$36,102.221m plus the US$1,775.000m principal of the three senior notes (calculation below); the same bridge holds at December 31, 2025 (US$34,168.392m plus US$1,275.000m equals US$35,443.392m). The MD&A figure of US$38.1 billion remains unreconciled: it is US$222.779m above the maturity-table total, more than rounding to one decimal of a billion can explain. This module uses the maturity-table total for maturities and recourse split, and the Note 17 carrying total plus senior notes for carrying debt, and names the basis each time.
2. Cash scopes, as CP-0 recorded. Cash and cash equivalents US$1,708.750m; plus restricted cash US$740.572m and restricted cash of consolidated entities US$101.715m gives US$2,551.037m, the cash flow statement total (10-Q Q3 page:44), while the balance sheet line "Cash, cash equivalents and restricted cash" of US$2,449.322m excludes the restricted cash of consolidated entities (10-Q Q3 page:7, page:44). This reconciles US$2,551.037m to US$2,449.322m by US$101.715m (calculation below).
3. Senior notes issuance proceeds, as CP-0 recorded. The nine-month 2026 cash flow line "Proceeds from issuance of unsecured senior notes" is 495,000 in both 2026 and 2025 (10-Q Q3 page:13), while the 2031 notes of May 14, 2026 raised approximately US$493.7 million net (10-Q Q3 page:58) and the only other issue, the 2030 notes of June 20, 2025, raised approximately US$495.0 million (10-K page:315). The 2026 line is not explained in the retained text. Note 17 amounts control for the notes.
4. Presentation change. The FY2025 income statement shows interest, general and administrative, and compensation as the only expense lines, with depreciation and amortization of 107,477 inside general and administrative (10-K page:199); the 10-Q presents it as a separate line and reclassifies prior periods (10-Q Q3 page:17, page:8). The new commercial real estate segment contributes revenue of US$547,428 thousand in nine months 2026 and none in nine months 2025 (10-Q Q3 page:8), so nine-month 2026 against 2025 is not like-for-like.
5. Release comparatives. The Q3 release compares the balance sheet with June 30, 2026, the 10-Q with December 31, 2025. Figures here are taken from the 10-Q.

## Calculations

All inputs are in US$ thousands unless stated. Locators are those listed above.

1. Debt bridge, face to maturity table. Sep 30, 2026: 36,102,221 (Note 17 total face, page:54) + 775,000 + 500,000 + 500,000 (senior notes principal, page:168) = 37,877,221, equal to the maturity-table total (page:57). Dec 31, 2025: 34,168,392 (10-K page:311) + 775,000 + 500,000 = 35,443,392, equal to the maturity-table total (10-K page:314). The MD&A figure: 38,100,000 less 37,877,221 = 222,779 (using the printed US$38.1 billion).
2. Carrying total of Note 17: 14,235,647 + 14,011,438 + 7,399,680 = 35,646,765, equal to the printed total (page:54). Including senior notes, net: 35,646,765 + 1,755,476 = 37,402,241 (Sep 30, 2026); 33,865,374 + 1,258,271 = 35,123,645 (Dec 31, 2025). Net of unrestricted cash for Sep 30, 2026: 37,402,241 - 1,708,750 = 35,693,491 (arithmetic only; not a leverage metric because no EBITDA exists).
3. Recourse share of maturity-table debt at Sep 30, 2026: 19,680,259 / 37,877,221 = 0.5196 (51.96%); non-recourse 18,196,962 / 37,877,221 = 0.4804. Dec 31, 2025 recourse: 19,496,781 / 35,443,392 = 0.5501.
4. Near-term maturities: Oct 1 to Dec 31, 2026 and 2027 together = 7,546,015 + 10,619,584 = 18,165,599 (a 15-month window to December 31, 2027, not twelve months), of which recourse 6,230,073 + 6,736,955 = 12,967,028. Share of total: 18,165,599 / 37,877,221 = 0.4796; recourse share of the window: 12,967,028 / 18,165,599 = 0.7138. Unrestricted cash 1,708,750 against the Q4 2026 recourse bucket of 6,230,073: 0.2743.
5. Available financing check: 3,021,445 + 3,918,467 + 459,656 + 148,000 + 402,000 + 2,704,263 + 59,722 + 71,731 = 10,785,284, equal to the printed total (page:57); capacity 29,121,824 less outstanding 18,336,540 = 10,785,284.
6. Debt to equity (principal basis, equity in Rithm Capital Corp. including preferred stock): Sep 30, 2026: 37,877,221 / 8,620,062 = 4.394x (4.39x); Dec 31, 2025: 35,443,392 / 8,430,487 = 4.204x (4.20x). Recourse: 19,680,259 / 8,620,062 = 2.283x (2.28x); 19,496,781 / 8,430,487 = 2.313x (2.31x). The recourse column includes secured repurchase and warehouse borrowings made by the Company against collateral, not only unsecured debt, and equity includes the preferred stock carrying value of 1,632,915 (Sep 30, 2026) and 1,390,790 (Dec 31, 2025); neither ratio is a covenant measure.
7. Earnings cover of interest, (pre-tax income + interest expense and warehouse line fees) / interest expense and warehouse line fees: FY2025 (806,383 + 1,662,433) / 1,662,433 = 1.485x; nine months 2025 (600,058 + 1,239,612) / 1,239,612 = 1.484x; nine months 2026 (760,219 + 1,395,011) / 1,395,011 = 1.545x. Pre-tax income includes MSR fair value changes and other non-cash items, and interest on warehouse funding is a cost of revenue for this issuer, so this is a rough indicator, not EBITDA cover and not a cash measure. Cash paid for interest and warehouse line fees for nine months 2026 was 1,406,118 against expense of 1,395,011, a difference of 11,107.
8. Cash scope reconciliation (10-Q Q3 page:44): 1,708,750 + 740,572 + 101,715 = 2,551,037; 2,551,037 - 101,715 = 2,449,322, the balance sheet line (page:7). The US$1.7 billion MD&A figure matches 1,708,750 rounded.
9. Unit conversion for the chart tables: thousands divided by 1,000, for example 7,546,015 gives 7,546.015 US$m.
10. Not computed: net debt to EBITDA, EBITDA cover and any committed liquidity figure, because the numerators are not supplied (see Gaps). No LTM figure is used in any table.

## Gaps

| Gap | Severity | Effect | Remediation |
| --- | --- | --- | --- |
| Not supplied: EBITDA or adjusted EBITDA; no definition is printed in the filings or releases. | High | Total debt / EBITDA, net debt / EBITDA and EBITDA / cash interest cannot be reported. | Use the debt to equity and recourse measures; obtain a management bridge only if an EBITDA basis is wanted, labelled as external. |
| Not supplied: committed undrawn facilities. Available financing is stated to be uncommitted. | High | Liquidity headroom beyond unrestricted cash cannot be measured. | Obtain the facility agreements and committed amounts by lender. |
| Not supplied: Total Unencumbered Assets and the indenture definition; no covenant level for corporate secured facilities. | Medium | Covenant headroom cannot be calculated. | Obtain the indentures dated March 19, 2024, June 20, 2025 and May 14, 2026 and the facility agreements. |
| Not supplied: letters of credit drawn on facilities; the terms letters of credit, standby, factoring and supply chain finance were searched in the 10-Q Q3 and 10-K and nothing relevant was found. | Low | No amount to deduct from capacity. | Confirm in the facility agreements. |
| Not supplied: cash flow, cash interest and cash taxes for the single quarter Q3 2026; only nine-month totals are printed. | Medium | Quarterly cash cover cannot be shown. | Derive from Q2 10-Q nine-month totals if a quarterly view is required; not done here. |
| Unreconciled: MD&A total debt of US$38.1 billion versus the maturity-table total, and the senior notes proceeds line in the cash flow statement. | Medium | Totals depend on stated basis. | Name the basis whenever a total is cited. |
| Not supplied: parent-only statements, guarantor information and ratings. | Medium | Parent-creditor claims cannot be isolated beyond the recourse and non-recourse split. | Obtain ratings and any condensed parent information from external sources, labelled as external. |
| Not carried: Q1 2026 and Q2 2026 figures, and a Q3 2025 balance sheet (the pack holds no Q3 2025 report); only FY2025, nine months and Q3 are presented. | Low | Trend within 2026 is not shown beyond Q3 against Q2 net income. | Add from the Q1 and Q2 10-Qs if a quarterly series is needed. |
| Limitation: the nine-month 2026 and 2025 comparison is not like-for-like because of the Elecor and Crestline acquisitions (December 2025) and the CRE joint venture deconsolidation. | Medium | Growth rates overstate organic change. | Use segment tables for like-for-like work. |
| Limitation: management items in the Q3 release (securitizations, refinancing, ROE) are attributed claims, not filing facts. | Low | Not used in any figure. | None. |

Currency and period: all figures are US dollars, matching the context; no foreign currency presentation. Periods follow the context (Q3 2026 and FY2025), with nine months shown where the filings give no quarterly figure.

## Next module

Proceed to CP-1A with these financial facts: a group with a mostly secured and short-dated funding stack where about half of contractual debt is recourse, a recourse maturity wall in the next five quarters, uncommitted lines and no EBITDA metric. CP-1A should explain the business and acquisition changes (Crestline in December 2025, Elecor, the new commercial real estate and asset management segments, the wind-down of the single-family rental business referred to in the 10-Q) that drive the figures, and should carry forward the conflicts and gaps listed above, in particular the unreconciled total-debt figures, the absent EBITDA and covenant levels, and the non-like-for-like nine-month comparison.
