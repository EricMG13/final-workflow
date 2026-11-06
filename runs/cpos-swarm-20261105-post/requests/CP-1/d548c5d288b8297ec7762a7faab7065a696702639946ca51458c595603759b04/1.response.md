## Request

Issuer: Post Holdings, Inc. (POST), a single consolidated reporting entity, borrower of the credit agreement and issuer of all senior notes. As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, in millions as the filings print them.

Scope of this module: extract and organise the financial base for the later modules: statements, the adjusted EBITDA definition, debt by instrument, liquidity, covenant, cash flow, claims outside debt and subsequent events, with leverage, interest cover, liquidity and maturity chart data. Periods follow Post's fiscal year, which ends September 30: FY2025 is the year ended September 30, 2025 (context prior period `fy-2025`); the current period `q3-2026` is the fiscal third quarter ended June 30, 2026, with nine months (9M) fiscal 2026 and the twelve months (LTM) ended June 30, 2026. Quarters are labelled by fiscal quarter, so Q1 FY2026 ended December 31, 2025 and Q2 FY2026 ended March 31, 2026. Sources and context agree on currency and periods, so there is no mismatch to report.

Correction to the earlier source-readiness handoff (CP-0, which cannot be edited): it said the reported total net leverage "uses principal debt less cash and a different numerator". Stated precisely, the release defines that ratio as principal debt less cash and cash equivalents over credit-agreement-adjusted Adjusted EBITDA for the last twelve months (EX-99.1 August 2026, page:17 and page:22), and the covenant ratio is a secured net leverage ratio whose numerator definition is not supplied. Nothing else in that handoff is changed.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-09-30_post-20250930.htm.jsonl | d988e0426964cfec01029656ef227ac10adca18ba413287c184f18404a876a74 |
| 10-Q_2025-12-31_post-20251231.htm.jsonl | e9cc6f62805c1b1bab9b7edb1afd055ae5b09d286a5f5385add48be2adcd1950 |
| 10-Q_2026-03-31_post-20260331.htm.jsonl | 6ed320d389c86598b7ad5f845098fe00ce2f7584e166c2976b8679a029b0c42b |
| 10-Q_2026-06-30_post-20260630.htm.jsonl | 5c5310f7f925e1ac072ebdb2eef5ec580787271894d731c4b0f244a823ad7595 |
| EX-99.1_2026-02-03_ex99-1q12026er.htm.jsonl | 38e17081ebfa3fafaf0505f1bd57fb738f074e8b7b4014662d7731549585d17b |
| EX-99.1_2026-05-05_ex99-1q22026er.htm.jsonl | c699bde5529dd39cf184dac3c7c6fd8e1af3530dddd1b671a659bdd669e9f846 |
| EX-99.1_2026-08-06_ex99-1q32026er.htm.jsonl | fa25c942bbdfd0499284c17eaea7c77be614d163d4c3ae3f0600195efb353a9c |
| context (settings, not issuer evidence) | 42de786351216298f80706a9245ba3397a337baef9248bdb3ddc19ef12ef23d8 |

Pages are the source chunks shown as `page:N`. In locators below, "10-K" is the FY2025 annual report, "Q1 10-Q", "Q2 10-Q" and "Q3 10-Q" are the quarterly reports for December 31, 2025, March 31, 2026 and June 30, 2026, and "Q1 release", "Q2 release" and "Q3 release" are the matching EX-99.1 earnings releases.

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 0207225cf916a688a599956fca0dbd3a4cedfd539e02ef72ef73b2252d375b67 |

CP-0 rated the source set READY_WITH_LIMITATIONS for this module. Its limits are carried here: no executed financing documents, no secured net leverage figure, no cash interest paid for interim periods in the 10-Qs (searched here, see Gaps), no balance sheet after June 30, 2026, and no ratings or market data. The release file dates for Q1 and Q2 differ from the dates printed in the releases (February 5 and May 7, 2026); neither affects any figure.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Leverage is high and has barely improved: net debt is about 4.6 times adjusted EBITDA, interest cost is rising faster than earnings, and shareholder buybacks absorbed more cash than free cash flow. Liquidity is ample. | Medium | Adjusted EBITDA is management's measure, cash interest is only available for FY2025, and the covenant metric is not reported. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt was 7,676.0 and net debt 7,410.4 at June 30, 2026, against twelve-month adjusted EBITDA of 1,615.9. | Net leverage of 4.59x on this basis, and total leverage of 4.75x, leave limited room for earnings shortfalls. | Medium |
| Interest expense, net rose 22% in both Q3 and the nine months while Q3 adjusted EBITDA fell 5.0%. | Reported interest coverage under the credit agreement fell from 4.1x to 3.8x between March and June 2026. | High |
| Cash plus undrawn revolver was 1,242.4 at June 30, 2026; the revolver of 1,000.0 matures in February 2029 and is undrawn. | Near-term liquidity is strong; the 575.0 convertible notes due August 2027 are the first maturity. | High |
| Nine-month buybacks of 916.1 exceeded free cash flow of 401.5; debt rose 223.8 despite 424.2 of disposal proceeds. | Leverage reduction is being deprioritised in favour of share repurchases. | High |
| The only maintenance covenant found is a springing secured leverage test, not applied while revolver usage stays below 30% of commitments. | Covenant protection is thin, and headroom cannot be measured from the pack. | Medium |

### Financial base view

The financial base is usable and internally consistent. The audited FY2025 statements, three quarterly statements and three earnings releases tie: the September 30, 2025 cash, total assets and long-term debt agree across the 10-K and the 10-Q comparatives, release figures for net earnings, interest and depreciation agree with the filed statements, and the twelve-month figures in the Q3 release reproduce from filed numbers (calculation 1). On the company's own adjusted EBITDA, leverage was 4.84x total and 4.73x net at September 30, 2025, dipped to 4.69x and 4.53x at March 31, 2026, and rose again to 4.75x and 4.59x at June 30, 2026 as Q3 adjusted EBITDA fell 5.0% against Q3 FY2025 while debt stayed at 7,676.0. Adjusted EBITDA is generous: it adds back 232.9 of items over the twelve months (14.4% of the total), including 83.0 of stock-based compensation and 43.3 of losses on held-for-sale assets, and unadjusted operating profit plus depreciation and amortization is 1,378.4, which puts total debt at 5.57x (calculation 5). The company reports 4.6x net leverage under its credit agreement definition and 3.8x interest coverage. Debt is almost entirely fixed-rate notes at a weighted average of 5.5%, of which 1,000.0 is secured, liquidity is 1,242.4, and the first maturity is the 575.0 convertible in August 2027. The main credit-relevant pattern is capital allocation: 916.1 of cash buybacks in nine months against 401.5 of free cash flow was funded by 424.2 of disposal proceeds and a net 223.8 of new debt. Full FY2026 guidance implies a weaker fourth quarter than a year earlier (calculation 8). The base does not support covenant headroom, guarantor-level, legal-term or post-June 30, 2026 conclusions.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (Sep 30, 2025) | 4.84 | 4.73 | x | Principal debt 7,452.2 (Q3 10-Q page:17 comparative; 10-K page:132) over FY2025 Adjusted EBITDA 1,538.8 (Q3 release page:22). Cash 176.7 excludes restricted cash. Adjusted EBITDA is management's measure; calculated here. |
| Q1 FY2026 (Dec 31, 2025) | 4.73 | 4.55 | x | Principal debt 7,507.2 (Q1 10-Q page:15) over LTM Adjusted EBITDA 1,587.1 calculated from 1,538.8 + 418.2 - 369.9 (Q3 release page:22; Q1 release page:18). Not a company-reported ratio: the Q1 release has no leverage reconciliation. |
| Q2 FY2026 (Mar 31, 2026) | 4.69 | 4.53 | x | Principal debt 7,676.0 (Q2 10-Q page:17) over LTM Adjusted EBITDA 1,635.6 (Q2 release page:23). Company-reported credit agreement ratio was 4.5x on credit-agreement-adjusted EBITDA of 1,646.9 (page:24). |
| Q3 FY2026 (Jun 30, 2026) | 4.75 | 4.59 | x | Principal debt 7,676.0 (Q3 10-Q page:17) over LTM Adjusted EBITDA 1,615.9 (Q3 release page:22). Company-reported credit agreement ratio was 4.6x on adjusted EBITDA of 1,597.3 (page:22). Leases, pensions and purchase commitments are excluded. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 (Sep 30, 2025) | 4.16 | x | Adjusted EBITDA 1,538.8 over interest paid 370.1 (10-K page:128, supplemental cash flow information). Interest expense, net of 361.4 gives 4.26x. |
| Q1 FY2026 (Dec 31, 2025) | Not supplied: cash interest paid is not printed in the Q1 10-Q or release | x | Searched "interest paid", "cash paid" and "interest payments" in all sources; only FY2025 prints the amount. No coverage ratio is reported for this date either. |
| Q2 FY2026 (Mar 31, 2026) | Not supplied: cash interest paid is not printed in the Q2 10-Q or release | x | Company-reported consolidated interest coverage ratio under the credit agreement was 4.1x, on interest expense, net of 399.4 (Q2 release page:24); that is not cash interest. |
| Q3 FY2026 (Jun 30, 2026) | Not supplied: cash interest paid is not printed in the Q3 10-Q or release | x | Company-reported consolidated interest coverage ratio was 3.8x, on interest expense, net of 419.1 (Q3 release page:22); the Q3 10-Q says only that interest payments were 11.8 higher in nine months (page:40). |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (Sep 30, 2025) | 176.7 | 537.7 | US$m | Revolver commitment 1,000.0 less borrowings 440.0 less letters of credit 22.3 (10-K page:139). Unrestricted cash only; restricted cash of 6.1 excluded. |
| Q1 FY2026 (Dec 31, 2025) | 279.3 | 545.9 | US$m | Revolver 1,000.0 less borrowings 430.0 less letters of credit 24.1 (Q1 10-Q page:19; balance sheet page:3). Restricted cash of 5.4 excluded. |
| Q2 FY2026 (Mar 31, 2026) | 269.4 | 976.2 | US$m | No borrowings, letters of credit 23.8 (Q2 10-Q page:21; balance sheet page:3). Restricted cash of 2.0 excluded. |
| Q3 FY2026 (Jun 30, 2026) | 265.6 | 976.8 | US$m | No borrowings, letters of credit 23.2 (Q3 10-Q page:21; balance sheet page:3). Restricted cash of 6.9 excluded. The facility is the only committed facility found and matures February 20, 2029, so none expires within twelve months. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2026 remainder (Jul-Sep 2026) | 0.0 | US$m | No instrument in the June 30, 2026 debt table matures before March 2027; the current portion of 1.3 is the municipal bond installment due March 1 (Q3 10-Q page:17; 10-K page:140). Derived from the table. |
| FY2027 | 576.3 | US$m | 2.50% convertible notes due August 15, 2027, 575.0, plus municipal bond installment 1.3. Holders may convert from May 15, 2027 (Q3 10-Q page:18). |
| FY2028 | 0.5 | US$m | Municipal bond final installment, March 1, 2028 (10-K page:140); equals the 10-K schedule of 0.5 for fiscal 2028 (page:141). |
| FY2029 | 0.0 | US$m | Revolver of 1,000.0 matures February 20, 2029 and is undrawn at June 30, 2026 (Q3 10-Q page:20). The 5.50% notes due December 2029 were redeemed in full. |
| FY2030 | 1,385.4 | US$m | 4.625% senior notes due April 2030 (Q3 10-Q page:17). |
| FY2031 | 980.6 | US$m | 4.50% senior notes due September 2031. |
| FY2032 | 1,000.0 | US$m | 6.25% senior secured notes due February 2032. |
| FY2033 | 1,200.0 | US$m | 6.375% senior notes due March 2033. |
| FY2034 | 0.0 | US$m | No instrument matures. |
| FY2035 | 1,200.0 | US$m | 6.250% senior notes due October 2034, which falls in fiscal 2035 because the fiscal year ends September 30; includes the 600.0 add-on of March 2026. |
| FY2036 | 1,300.0 | US$m | 6.50% senior notes due March 2036. |
| FY2040 | 33.2 | US$m | Leaseback financial liabilities; the lease term runs through fiscal 2040 but the principal schedule is not printed, so the balance is shown at term end only so that the rows total 7,676.0 (10-K page:140). |

### Financials and credit metrics

| Metric | FY2025 (year to Sep 30, 2025) | 9M FY2025 (to Jun 30, 2025) | 9M FY2026 (to Jun 30, 2026) | LTM to Jun 30, 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- |
| Net sales | 8,158.1 | 5,911.1 | 6,165.5 | 8,412.5 | Statements of operations (10-K page:94; Q3 10-Q page:2). LTM = FY2025 + 9M FY2026 - 9M FY2025. |
| Gross profit | 2,339.4 | 1,737.3 | 1,822.4 | 2,424.5 | Same pages. LTM calculated. |
| Operating profit | 799.3 | 630.9 | 639.6 | 808.0 | Same pages. FY2025 is after a goodwill impairment of 29.8. LTM calculated. |
| Depreciation and amortization | 524.3 | 378.1 | 424.2 | 570.4 | Cash flow statements (10-K page:96; Q3 10-Q page:3). LTM 570.4 also printed in Q3 release page:22. |
| Operating profit plus D&A (unadjusted) | 1,323.6 | 1,009.0 | 1,063.8 | 1,378.4 | Calculated; no add-backs. |
| Adjusted EBITDA (management) | 1,538.8 | 1,113.4 | 1,190.5 | 1,615.9 | Q3 release page:19 and page:22. Non-GAAP; not in any filing. |
| Interest expense, net | 361.4 | 259.6 | 317.3 | 419.1 | Statements of operations; LTM printed in Q3 release page:22. |
| Net earnings | 335.7 | 284.7 | 242.1 | 293.1 | Attributable to Post; LTM printed in Q3 release page:22. |
| Net cash provided by operating activities | 998.3 | 697.0 | 691.3 | 992.6 | Cash flow statements; LTM calculated. |
| Capital expenditures (additions to property) | 510.2 | 360.5 | 289.8 | 439.5 | Same pages; LTM calculated. |
| Free cash flow (operating cash flow less capital expenditures) | 488.1 | 336.5 | 401.5 | 553.1 | Company definition (Q3 release page:21); FY2025 and LTM calculated. |
| Purchases of treasury stock (cash) | 709.0 | 434.3 | 916.1 | 1,190.8 | Cash flow statements; LTM calculated. |
| Cash and cash equivalents (at period end) | 176.7 | Not supplied: Q3 FY2025 balance sheet is not in the pack | 265.6 | 265.6 | Balance sheets (10-K page:95; Q3 10-Q page:3). Excludes restricted cash of 6.1 and 6.9. |
| Principal debt (at period end) | 7,452.2 | Not supplied: Q3 FY2025 balance sheet is not in the pack | 7,676.0 | 7,676.0 | Debt note (Q3 10-Q page:17); Q3 release page:22 shows 7,676.0 as total principal debt. |
| Net debt (principal debt less cash) | 7,275.5 | Not supplied: as above | 7,410.4 | 7,410.4 | June 30, 2026 value printed in Q3 release page:22; FY2025 calculated. |
| Total debt / Adjusted EBITDA | 4.84x | Not supplied: as above | 4.75x | 4.75x | Calculated on LTM Adjusted EBITDA. |
| Net debt / Adjusted EBITDA | 4.73x | Not supplied: as above | 4.59x | 4.59x | Calculated. The company reports 4.6x on credit-agreement-adjusted EBITDA of 1,597.3. |
| Total debt / unadjusted EBITDA | 5.63x | Not supplied: as above | 5.57x | 5.57x | Calculated on operating profit plus D&A (calculation 5). |
| Total assets (at period end) | 13,528.4 | Not supplied: as above | 12,852.7 | 12,852.7 | Balance sheets. |
| Total shareholders' equity (at period end) | 3,763.8 | Not supplied: as above | 3,089.2 | 3,089.2 | Balance sheets; down because treasury stock rose to 4,663.5. |

### Adjusted EBITDA definition review

Adjusted EBITDA is built in the releases from net earnings (Q3 release page:19 and page:22). The twelve-month reconciliation printed there starts at net earnings of 293.1 and adds interest expense, net 419.1, income tax 100.4 and depreciation and amortization 570.4 to reach 1,383.0 (calculation 4), then adds the following items, shown as the LTM column prints them:

| Add-back (LTM to Jun 30, 2026) | Amount | Credit reading |
| --- | --- | --- |
| Stock-based compensation | 83.0 | Non-cash, but a recurring cost of staff remuneration |
| Loss on amounts held for sale | 43.3 | Crystal Farms write-down; non-recurring by nature |
| Impairment of goodwill | 29.8 | FY2025 Cheese and Dairy impairment (10-K page:131); non-cash |
| Integration costs | 27.6 | Recurs across acquisitions (8th Avenue, Weetabix East Africa and others) |
| Inventory revaluation adjustment on acquired businesses | 22.0 | Purchase accounting effect |
| Loss on extinguishment of debt, net | 17.5 | Premium and fees on the 5.50% notes redemption |
| Asset disposal costs, transaction costs, restructuring | 12.0, 9.0, 9.2 | Recurring in nature across periods |
| Other net items (hedge and equity mark-to-market, swaps, sale gain, legal, other) | (20.5) | Net negative: gains removed |

The other net items are the sum of mark-to-market on commodity and foreign exchange hedges (7.3), mark-to-market on equity securities (5.5), income on swaps (6.5), gain on sale of business (2.7), provision for legal settlements 2.7, costs expected to be indemnified (1.0), advisory income (0.1), equity method adjustment 0.4 and noncontrolling interest adjustment (0.5), where parentheses are negative (calculation 4). The credit agreement then adjusts LTM Adjusted EBITDA by a further (18.6) to 1,597.3 (Q3 release page:22); the nature of those adjustments is not stated beyond "certain items as provided in Post’s credit agreement" (page:17), so credit agreement EBITDA cannot be rebuilt.

### Debt by instrument at June 30, 2026

Issuer for every instrument is Post Holdings, Inc.; no co-issuer is named. Guarantors are not individually named in any source (see Gaps).

| Instrument | Principal | Rate | Maturity | Security and guarantors (as the notes print them) |
| --- | --- | --- | --- | --- |
| 2.50% convertible senior notes | 575.0 | 2.50% fixed | Aug 15, 2027 | Senior unsecured; guaranteed by domestic subsidiaries that guarantee other senior notes. Conversion price about $106.10; settled in cash, shares or both at Post's election (Q3 10-Q page:18 and page:39) |
| 4.625% senior notes | 1,385.4 | 4.625% fixed | Apr 2030 | Senior unsecured; guaranteed by existing and future domestic subsidiaries other than immaterial, excluded and unrestricted ones |
| 4.50% senior notes | 980.6 | 4.50% fixed | Sep 2031 | Same |
| 6.25% senior secured notes | 1,000.0 | 6.25% fixed | Feb 2032 | Senior secured; guaranteed on a secured basis by domestic subsidiaries that guarantee the Credit Agreement or certain other debt (Q3 10-Q page:39) |
| 6.375% senior notes | 1,200.0 | 6.375% fixed | Mar 2033 | Senior unsecured; guaranteed by wholly-owned domestic subsidiaries that guarantee the Credit Agreement or certain other debt (10-K page:136) |
| 6.250% senior notes | 1,200.0 | 6.250% fixed | Oct 2034 | Same; 600.0 issued October 2024 at par and 600.0 added March 13, 2026 at 100.75% (Q3 10-Q page:20) |
| 6.50% senior notes | 1,300.0 | 6.50% fixed | Mar 2036 | Senior unsecured; issued December 15, 2025 at par (Q3 10-Q page:19, page:20) |
| Revolving Credit Facility | 0.0 drawn | SOFR plus 1.50% to 2.00%, by secured net leverage | Feb 20, 2029 | 1,000.0 commitment, letters of credit up to 75.0, drawn letters of credit 23.2; secured by substantially all assets other than real property and guaranteed by subsidiaries (Q3 10-Q page:20, page:21, page:39) |
| Leaseback financial liabilities | 33.2 | 9.29% calculated rate (10-K) | Lease term through fiscal 2040 | Nut butter facilities in Fitzgerald, Georgia, assumed with 8th Avenue (10-K page:140) |
| Municipal bond | 1.8 | Not fixed-rate: total principal 7,676.0 less fixed-rate 7,674.2 | Mar 1, 2028 | Chaska, Minnesota filtration project (10-K page:140) |
| Total principal | 7,676.0 | 7,674.2 fixed at a weighted average 5.5% | | Q3 10-Q page:17 and page:45 |

Carrying value of long-term debt is 7,631.3 after current portion 1.3, debt issuance costs 56.0 and unamortized premium 12.6 (Q3 10-Q page:17). Fair value of the notes (excluding revolver, leasebacks and the municipal bond) was 7,526.2 at June 30, 2026 against 6,999.6 at September 30, 2025 (page:46).

### Covenants and definitions

The only maintenance test is a secured net leverage ratio not to exceed 4.25:1.00, measured at fiscal quarter end only if revolving loans, swing line loans and letter of credit obligations exceed 30% of revolving commitments (Q3 10-Q page:23; Q3 10-Q page:41). Post states compliance at June 30, 2026 and does not expect non-compliance. At June 30, 2026 usage was 23.2 of letters of credit and no borrowings, against a trigger of 300.0 (calculation 6), so the test was not engaged. The reported figure is total net leverage of 4.6x on credit agreement EBITDA of 1,597.3, which is a different measure from the covenant. Event-of-default cross default and judgment thresholds are 125.0 (page:21). Headroom to the 4.25:1.00 test is Not calculable: the secured net debt numerator and the credit agreement EBITDA definition are not supplied (CP-0 limitation confirmed). An indicative secured-only calculation is in calculation 7 and must not be read as covenant headroom.

### Cash flow and capital allocation, nine months FY2026

Operating cash flow was 691.3 against 697.0 a year earlier and capital expenditures 289.8 against 360.5, giving free cash flow of 401.5 against 336.5 (Q3 release page:21). Investing inflows of 424.2 came from the sale of the Pasta Business (378.5 at closing) and Crystal Farms (45.7 at closing) (Q3 10-Q page:10, page:12, page:40), plus 32.4 of property sales. Financing: proceeds from debt 2,265.0 (6.50% notes 1,300.0, 6.250% add-on 600.0, revolver borrowings 365.0), repayments 2,041.2 (5.50% notes 1,235.0, revolver 805.0, municipal bond 1.2), premiums paid 22.6, issuance costs 19.4 and treasury stock purchases 916.1 (Q3 10-Q page:4, page:22, page:41). Net debt issuance was 223.8 (calculation 3). Repurchases in the quarter were 2.1 million shares for 198.9, and 0.4 million shares for 39.3 after quarter end through August 5, 2026, leaving 490.7 of authorisation (Q3 release page:6).

### Claims outside the debt figure

| Item | Amount | Inside or outside debt | Locator |
| --- | --- | --- | --- |
| Leaseback financial liabilities | 33.2 | Inside principal debt | Q3 10-Q page:17 |
| Operating lease liabilities (September 30, 2025) | 277.9 | Outside | 10-K page:131; the 10-Qs print no lease balance (searched "lease liabilit" and "operating lease") |
| Leases signed but not commenced (September 30, 2025) | 138.3 minimum payments | Outside | 10-K page:131 |
| Purchase obligations (September 30, 2025) | 7,382.7, of which 2,497.3 in fiscal 2026 | Outside; mainly egg contracts, purchase orders and accrued capital expenditures | 10-K page:80 |
| Pension and retiree plans (September 30, 2025) | Funded status +17.0 North America, +123.8 other international; retiree health (49.9) | Outside; net surplus on pensions | 10-K page:144, page:148 |
| Bob Evans lease guarantees | Annual rent 13.5 on 129 properties; fair value stated immaterial | Outside; contingent | 10-K page:142 |
| Letters of credit under the revolver | 23.2 | Reduce undrawn capacity, not in debt | Q3 10-Q page:21 |
| Noncontrolling interest | 11.2 | Equity, outside debt | Q3 10-Q page:3 |
| Litigation | Not material per management; legal settlement provision 2.7 in LTM add-backs | Outside | Q3 10-Q page:23; Q3 release page:22 |

Searches of every source for factoring, supply chain finance and receivables sales found nothing, so none is reported.

### Segments, nine months and Q3 FY2026

Segment Adjusted EBITDA (management measure, Q3 release page:19 to page:21):

| Segment | Q3 FY2026 | Q3 FY2025 | 9M FY2026 | 9M FY2025 |
| --- | --- | --- | --- | --- |
| Post Consumer Brands | 197.3 | 177.5 | 600.8 | 586.1 |
| Foodservice | 140.8 | 159.0 | 435.2 | 371.8 |
| Refrigerated Retail | 26.6 | 45.3 | 117.5 | 121.6 |
| Weetabix | 37.3 | 32.8 | 102.7 | 91.1 |
| Corporate and other | (24.7) | (17.6) | (65.7) | (57.2) |
| Total Adjusted EBITDA | 377.3 | 397.0 | 1,190.5 | 1,113.4 |

Foodservice Q3 declines reflect the lapping of avian influenza pricing in the prior-year quarter (Q3 release page:4); management says FY2026 includes about $60 million of Foodservice earnings above its $500 million normalised run rate and about $20 million from divestitures, implying about $1.48 billion of comparable entry EBITDA for FY2027 (Q3 release page:7). That is management language, not a figure verified here.

### Subsequent events and latest-quarter events

After June 30, 2026 the pack shows only the 0.4 million share repurchase for 39.3 through August 5, 2026 and the narrowed FY2026 Adjusted EBITDA guidance of 1,560 to 1,570, down from a range of 1,550 to 1,580 (Q3 release page:6). Events inside the quarter: repayment of 45.0 of revolver borrowings, the sale of Crystal Farms (May 1, 2026), the sale of the Sparks Facility (gain of 21.6) and a loss on amounts held for sale of 15.0 (Q3 10-Q page:12). Nothing in the pack is dated after the cutoff.

## Calculations

1. LTM to June 30, 2026 = FY2025 + 9M FY2026 - 9M FY2025. Net sales 8,158.1 + 6,165.5 - 5,911.1 = 8,412.5. Gross profit 2,339.4 + 1,822.4 - 1,737.3 = 2,424.5. Operating profit 799.3 + 639.6 - 630.9 = 808.0. D&A 524.3 + 424.2 - 378.1 = 570.4 (equals Q3 release page:22). Interest 361.4 + 317.3 - 259.6 = 419.1 (equals printed). Net earnings 335.7 + 242.1 - 284.7 = 293.1 (equals printed). Operating cash flow 998.3 + 691.3 - 697.0 = 992.6. Capital expenditures 510.2 + 289.8 - 360.5 = 439.5. Free cash flow 992.6 - 439.5 = 553.1. Treasury stock purchases 709.0 + 916.1 - 434.3 = 1,190.8. Adjusted EBITDA 1,538.8 + 1,190.5 - 1,113.4 = 1,615.9 (equals printed).
2. Leverage by date. Net debt = principal debt - cash. Sep 30, 2025: 7,452.2 - 176.7 = 7,275.5; 7,452.2 / 1,538.8 = 4.84; 7,275.5 / 1,538.8 = 4.73. Dec 31, 2025: LTM Adjusted EBITDA 1,538.8 + 418.2 - 369.9 = 1,587.1; net debt 7,507.2 - 279.3 = 7,227.9; 7,507.2 / 1,587.1 = 4.73; 7,227.9 / 1,587.1 = 4.55. Mar 31, 2026: net debt 7,676.0 - 269.4 = 7,406.6 (equals Q2 release page:24); 7,676.0 / 1,635.6 = 4.69; 7,406.6 / 1,635.6 = 4.53. Jun 30, 2026: 7,676.0 / 1,615.9 = 4.75; 7,410.4 / 1,615.9 = 4.59. As a check, 7,410.4 / 1,597.3 = 4.64, which rounds to the reported 4.6x; March 7,406.6 / 1,646.9 = 4.50, reported 4.5x.
3. Net debt issuance 9M FY2026 = 2,265.0 - 2,041.2 = 223.8, and principal debt moved 7,452.2 to 7,676.0, a change of 223.8. Buybacks less free cash flow = 916.1 - 401.5 = 514.6.
4. Adjusted EBITDA build, LTM: 293.1 + 419.1 + 100.4 + 570.4 = 1,383.0; add-backs 1,615.9 - 1,383.0 = 232.9; 232.9 / 1,615.9 = 14.4%. Listed add-backs: 83.0 + 43.3 + 29.8 + 27.6 + 22.0 + 17.5 + 12.0 + 9.0 + 9.2 = 253.4; other net items (7.3) + (5.5) + (6.5) + (2.7) + 2.7 + (1.0) + (0.1) + 0.4 + (0.5) = (20.5); 253.4 - 20.5 = 232.9.
5. Unadjusted EBITDA = operating profit + D&A. FY2025: 799.3 + 524.3 = 1,323.6. LTM: 808.0 + 570.4 = 1,378.4. 9M FY2026: 639.6 + 424.2 = 1,063.8. 9M FY2025: 630.9 + 378.1 = 1,009.0. Leverage: 7,676.0 / 1,378.4 = 5.57; 7,452.2 / 1,323.6 = 5.63. Difference to Adjusted EBITDA: 1,615.9 - 1,378.4 = 237.5, being add-backs 232.9 plus 4.6 of non-operating items between net earnings-based and operating-profit-based totals (1,383.0 - 1,378.4).
6. Covenant trigger: 30% x 1,000.0 = 300.0; usage at Jun 30, 2026 = 0.0 borrowings + 23.2 letters of credit = 23.2 (letters of credit may be partly excepted under the credit agreement; not stated).
7. Indicative secured leverage, not the covenant: secured principal 1,000.0 (6.25% senior secured notes; revolver undrawn) less cash 265.6 = 734.4; 734.4 / 1,597.3 = 0.46x. Whether leaseback liabilities are secured and how cash is netted are not supplied.
8. Guidance read-through: FY2026 guidance 1,560 to 1,570 less 9M FY2026 1,190.5 implies Q4 FY2026 of 369.5 to 379.5. Q4 FY2025 = 1,538.8 - 1,113.4 = 425.4, so the implied Q4 is lower by 45.9 to 55.9.
9. Coupon run-rate on the notes at June 30, 2026: 575.0 x 2.50% + 1,385.4 x 4.625% + 980.6 x 4.50% + 1,000.0 x 6.25% + 1,200.0 x 6.375% + 1,200.0 x 6.250% + 1,300.0 x 6.50% = 14.4 + 64.1 + 44.1 + 62.5 + 76.5 + 75.0 + 84.5 = 421.1 (rounded). LTM Adjusted EBITDA 1,615.9 / 421.1 = 3.84x. This excludes the leaseback (about 3.1 at 9.29%), revolver commitment fees, amortisation and interest income, so it is an approximation of cash coupon only.
10. Liquidity: Jun 30, 2026 265.6 + 976.8 = 1,242.4; Sep 30, 2025 176.7 + 537.7 = 714.4; Dec 31, 2025 279.3 + 545.9 = 825.2; Mar 31, 2026 269.4 + 976.2 = 1,245.6. Maturity rows total 576.3 + 0.5 + 1,385.4 + 980.6 + 1,000.0 + 1,200.0 + 1,200.0 + 1,300.0 + 33.2 = 7,676.0.
11. Interest cover FY2025: 1,538.8 / 370.1 = 4.16; 1,538.8 / 361.4 = 4.26. Company coverage: 1,597.3 / 419.1 = 3.81 (reported 3.8x); 1,646.9 / 399.4 = 4.12 (reported 4.1x). Q3 interest expense, net of 108.2 against 88.5 is +19.7, or 22%; Q3 Adjusted EBITDA 377.3 against 397.0 is -19.7, or -5.0%.

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Cash interest paid is printed only for FY2025 (10-K page:128); the 10-Qs and releases do not print it | Interest cover on a cash basis is available for one date only; interim columns use no cash proxy | Use company-reported coverage on interest expense, net and label it so |
| Secured net leverage ratio and credit agreement EBITDA definition not supplied; headroom Not calculable | Covenant conclusion limited to compliance statement and non-trigger | Obtain compliance certificate and credit agreement |
| Executed financing documents not supplied | Guarantor names, release mechanics, call schedules and baskets, including restricted payment capacity, unverified | Obtain indentures and credit agreement before legal or restricted-payment conclusions |
| Principal repayment schedule for the leaseback financial liabilities not printed | Maturity row for FY2040 is a placement, not a schedule | Treat as 33.2 with unknown timing |
| June 30, 2025 balance sheet and Q3 FY2025 cash flow not in the pack | Leverage trend is shown from September 30, 2025 only; no prior-year same-date comparison; quarterly cash flow for Q3 alone not shown | Use year-to-date figures |
| Operating lease balance after September 30, 2025 not printed in the 10-Qs (searched) | Lease claim shown at the year-end date only | Label as September 30, 2025 |
| No data after June 30, 2026 except buybacks through August 5, 2026 | Position at the as-of date unknown | Label figures as of June 30, 2026 |
| Adjusted EBITDA is a non-GAAP issuer measure; credit agreement adjustment of (18.6) unexplained | Leverage on this basis understates leverage on unadjusted earnings | Show both bases, as above |
| Perimeter changes: 8th Avenue acquired July 1, 2025; Pasta Business sold December 1, 2025; Crystal Farms sold May 1, 2026 | LTM figures mix perimeters; no pro forma LTM for the divestitures | Flag in every comparison |

## Next module

Proceed to CP-1A (business and transaction context), then CP-2 and CP-5. Carry forward: all leverage figures are on management's LTM Adjusted EBITDA with an unadjusted sensitivity (5.57x total at June 30, 2026); cash interest is available for FY2025 only; the covenant is a springing secured test not engaged at June 30, 2026 with headroom not calculable; liquidity is 1,242.4 with the revolver maturing February 2029 and the convertible notes due August 2027 as the first maturity; buybacks exceed free cash flow; and the CP-0 wording about the covenant numerator is corrected above. CP-5 should open the locators for the calculations above, in particular the release reconciliation (Q3 release page:22) and the debt table (Q3 10-Q page:17).
