# CP-1 — Financial base: Caesars Entertainment, Inc. (czr)

## Request

- Issuer: Caesars Entertainment, Inc. (issuer id `czr`), as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD, all amounts in US$ millions as the filings print them (`(In millions)`). Current period Q3 2026; prior period FY2025 (context).
- Run: `czr-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Execution: host session; the host read the pinned page text and wrote this answer. No provider was called.
- Perimeter: Caesars Entertainment, Inc. and its consolidated subsidiaries, including the 50.0% variable interest in CVA Holdco, LLC that it consolidates. Debt, Adjusted EBITDA, interest and cash flow figures below are on that consolidated perimeter. The parent has no separate statements in the pack.
- Question: what is the reported financial base for the credit view, with debt, leases outside debt, liquidity, maturities, coverage and the covenant picture, for FY2025 and the first three quarters of 2026?
- Locators are `page:N` of the pinned `.jsonl` text of each source, not printed page numbers. Periods are labelled FY2025, Q1 2026, Q2 2026, Q3 2026, nine months 2026 (9M 2026), nine months 2025 (9M 2025) and LTM Q3 2026.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_czr-20251231.htm.jsonl | bc64a6b58a2e5481a0cfade7eea5b0ab2abc3801003c4d6cb677785a5aa59468 | Audited FY2025 statements, notes, Adjusted EBITDA reconciliation, debt and lease notes |
| 10-Q_2026-03-31_czr-20260331.htm.jsonl | 5678521031e1645ef46bac311c4cabf43977488c6d11dfa25cc00a4f23b2d8a8 | Unaudited Q1 2026 statements, debt note, liquidity table |
| 10-Q_2026-06-30_czr-20260630.htm.jsonl | c1584ea1247740f06c0dd4b0a8964b1753f8cc5c74266698804a67fd5a8dafb5 | Unaudited Q2 2026 and six-month statements, debt note, liquidity table |
| 10-Q_2026-09-30_czr-20260930.htm.jsonl | 020dbbd4c466f93db126b9e9ea0f09672470d3e5caa33fd667f739807400c48f | Unaudited Q3 2026 and nine-month statements, debt note, covenants, liquidity, merger note |
| EX-99.1_2026-04-28_ex991-2026q1ceiearningsrel.htm.jsonl | 7471385a5ad76519a93a6fc4a1f0048a88c7bfb7676d6a0b6e78c8e1a9e19c13 | Q1 2026 release; net debt table (supporting) |
| EX-99.1_2026-07-28_ex991-2026q2ceiearningsrel.htm.jsonl | 89cd5ad8c7a0d45cdf4a8f6462fc3964a9e7d04aae46811b1f50bebeb80c1762 | Q2 2026 release; net debt table (supporting) |
| EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm.jsonl | 72e92043d95db7701dbaee10509a03094dd97f5a7811f25a956ad12661393bcd | Q3 2026 release; net debt and liquidity table (supporting) |
| context | fb12b9963cea633059e88f881abb925ca379a0e095eca4255a6e391fb14bd7dc | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | c01a0b9e9e4166e7f52e7361ee900e87238ecbbd00650638eadf7c06ae6c64f6 | Source readiness: all selected consumers ready with limitations; carries the missing agreements, the lease note limit and the Fertitta naming gap |

Consistency with CP-0: this answer confirms CP-0 on every point it checked. CP-0 said the 10-Qs carry no lease note; that is confirmed (the 10-Qs show only the aggregate `Long-term financing obligations` line). No correction to CP-0 is needed.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported debt is 3.26x last-twelve-months Adjusted EBITDA, but lease financing obligations of 13,188 sit outside debt; including them leverage is 6.95x and cash interest cover is only 1.69x. | Medium | Adjusted EBITDA is a company non-GAAP measure and covenant ratio values are not printed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt fell from 11,905 at FY2025 to 11,659 at Q3 2026, with the revolver undrawn at quarter-end. | Modest deleveraging; debt-only leverage moved from 3.29x to 3.26x. | High |
| Lease rent interest of about 1,371 over the last twelve months is paid on top of 741 of cash interest on debt. | Fixed charges absorb most Adjusted EBITDA, leaving thin cover. | Medium |
| Net loss attributable to Caesars was (283) for nine months 2026 and Adjusted EBITDA fell to 2,672 from 2,723. | Earnings are shrinking while fixed charges are stable. | Medium |
| Liquidity was 2,947 on the company basis at Q3 2026, and maturities rise to 1,574 in 2029 and 3,962 in 2030. | Near-term liquidity is adequate; the 2029 and 2030 wall is the pressure point. | Medium |

### Financial base view

The reported base supports a debt-only view and a lease-inclusive view, and the two give very different pictures. On the company's own measures, debt is 11,659 at Q3 2026 (face value), net debt is 10,795, and last-twelve-months Adjusted EBITDA is 3,573, giving 3.26x and 3.02x. But Adjusted EBITDA is stated before the rent on the VICI and GLPI leases, which the company accounts for as financing obligations of 13,188 outside debt. Adding those obligations lifts leverage to 6.95x, and adding the roughly 1,371 of rent cash interest to the 741 of cash interest on debt gives cash interest cover of 1.69x. Both views use the same company Adjusted EBITDA, so neither is a covenant ratio. Earnings are drifting lower (Adjusted EBITDA 2,672 for 9M 2026 against 2,723 for 9M 2025, with Las Vegas down and Regional and Digital up) and net loss attributable to Caesars widened to (283) from (252). Liquidity is adequate in the near term and nothing in the debt table matures before 2028 beyond amortisation. The pending acquisition adds uncertainty about the debt, but the supplied sources do not say how existing debt is treated.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 3.29 | 3.04 | x | Face value of total debt 11,905 and company net debt 11,018 at December 31, 2025 over FY2025 Adjusted EBITDA 3,624. Excludes financing obligations. Adjusted EBITDA is a company non-GAAP measure. |
| LTM Q1 2026 | 3.29 | 3.05 | x | Debt 11,917 and net debt 11,050 at March 31, 2026 over LTM Adjusted EBITDA 3,627 (calculated). Excludes financing obligations. |
| LTM Q2 2026 | 3.29 | 3.02 | x | Debt 11,807 and net debt 10,842 at June 30, 2026 over LTM Adjusted EBITDA 3,592 (calculated). Excludes financing obligations. |
| LTM Q3 2026 | 3.26 | 3.02 | x | Debt 11,659 and net debt 10,795 at September 30, 2026 over LTM Adjusted EBITDA 3,573 (calculated). Excludes financing obligations; including the 13,188 of financing obligations, total debt plus obligations over EBITDA is 6.95x. Net debt deducts unrestricted cash only. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 1.68 | x | FY2025 Adjusted EBITDA 3,624 over cash interest paid for debt 813 plus cash interest paid for rent related to financing obligations 1,349. Debt-only cover is 4.46x. |
| LTM Q1 2026 | 1.67 | x | LTM Adjusted EBITDA 3,627 over LTM cash interest 815 on debt plus 1,359 rent (calculated from FY2025, Q1 2026 and Q1 2025). Debt-only cover is 4.45x. |
| LTM Q2 2026 | 1.68 | x | LTM Adjusted EBITDA 3,592 over LTM cash interest 776 on debt plus 1,368 rent (calculated). Debt-only cover is 4.63x. |
| LTM Q3 2026 | 1.69 | x | LTM Adjusted EBITDA 3,573 over LTM cash interest 741 on debt plus 1,371 rent (calculated). Debt-only cover is 4.82x. Rent includes the small other financing obligations line from 2026 interims. Not a covenant ratio. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 887 | 1946 | US$m | Cash and cash equivalents excluding restricted cash 85. Facilities are the company's revolver capacity net of 83 of letters of credit, 46 regulatory commitment and 40 reserves. Net of letters of credit only the figure is 2,032. |
| Q1 2026 | 867 | 1893 | US$m | Unrestricted cash excluding restricted cash 92. Company basis: CEI revolver net of 200 drawn, plus CVA 25, less 96 letters of credit, 40 reserves and 46 regulatory. Net of letters of credit only: 1,979. |
| Q2 2026 | 965 | 1963 | US$m | Unrestricted cash excluding restricted cash 96. Company basis: CEI revolver net of 120 drawn, plus CVA 25, less 96 letters of credit, 40 reserves and 56 regulatory. Net of letters of credit only: 2,059. |
| Q3 2026 | 864 | 2083 | US$m | Unrestricted cash excluding restricted cash 94. Company basis: CEI 2,250 undrawn plus CVA 25, less 96 letters of credit, 40 reserves and 56 regulatory (company total 2,947 with cash). Net of letters of credit only: 2,179. CEI revolver matures January 31, 2028. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q4 2026 | 28 | US$m | Remaining 2026 scheduled principal as of September 30, 2026 (Q3 10-Q page:16); face value, includes term loan amortisation. |
| FY2027 | 114 | US$m | Scheduled principal on term loans, the Special Improvement District Bonds and other borrowings (Q3 10-Q page:17); no instrument in the debt table has a 2027 final maturity. |
| FY2028 | 646 | US$m | CEI Term Loan A (609 at face value) matures January 31, 2028; the CEI revolver also matures that day and is undrawn at September 30, 2026. |
| FY2029 | 1574 | US$m | CEI Senior Notes due 2029 (1,200) and the CVA Delayed Draw Term Loan (371 at face value, April 26, 2029) account for 1,571 of the total. |
| FY2030 | 3962 | US$m | CEI Senior Secured Notes due 2030 (2,000) plus the CEI Term Loan B balloon (balance 2,012 at face value before earlier amortisation). |
| Thereafter | 5335 | US$m | 2031 onward: CEI Term Loan B-1, CEI notes due 2032 and the 2037 bonds. Total of all periods is 11,659. Excludes financing obligations. |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | 9M 2026 | 9M 2025 | LTM Q3 2026 | Basis and locators |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net revenues | 11,486 | 2,870 | 2,993 | 2,940 | 8,803 | 8,570 | 11,719 | Reported (10-K page:99; Q1 10-Q page:2; Q2 10-Q page:2; Q3 10-Q page:2). LTM calculated. |
| Operating income | 1,858 | 500 | 513 | 457 | 1,470 | 1,527 | 1,801 | Reported; FY2025 after 182 of impairment charges. LTM calculated. |
| Interest expense, net | 2,304 | 569 | 573 | 570 | 1,712 | 1,729 | 2,287 | Reported; includes interest on financing obligations. LTM calculated. |
| Net loss attributable to Caesars | (502) | (98) | (62) | (123) | (283) | (252) | (533) | Reported (10-K page:99; 10-Qs page:3). LTM calculated. |
| Depreciation and amortization | 1,417 | 347 | 355 | 366 | 1,068 | 1,073 | 1,412 | Reported. LTM calculated. |
| Adjusted EBITDA (company non-GAAP) | 3,624 | 887 | 920 | 865 | 2,672 | 2,723 | 3,573 | Reported (10-K page:78; Q1 10-Q page:29; Q2 10-Q page:34; Q3 10-Q page:34). LTM calculated. |
| Adjusted EBITDA margin (%) | 31.6 | 30.9 | 30.7 | 29.4 | 30.4 | 31.8 | 30.5 | Quarter and nine-month margins as reported (Q3 10-Q page:41); FY2025 and LTM calculated. |
| Net cash provided by operating activities | 1,302 | 204 | 471 | 267 | 942 | 998 | 1,246 | Reported for FY2025, Q1 2026, 9M columns; Q2 2026 and Q3 2026 derived by subtracting year-to-date reports. LTM calculated. |
| Purchase of property and equipment | 805 | 168 | 167 | 172 | 507 | 648 | 664 | Reported cash-flow line; Q2 2026 and Q3 2026 derived; Q3 equals the 172 segment capital expenditure (Q3 10-Q page:34). |
| Operating cash flow less purchase of property and equipment | 497 | 36 | 304 | 95 | 435 | 350 | 582 | Calculated; not a company-defined measure. |
| Cash interest paid for debt | 813 | 212 | 156 | 212 | 580 | 652 | 741 | Supplemental cash flow (10-K page:101; Q1 10-Q page:4; Q2 10-Q page:5; Q3 10-Q page:5); Q2 and Q3 derived. LTM calculated. |
| Cash interest paid for rent related to financing obligations | 1,349 | 346 | 345 | 346 | 1,037 | 1,015 | 1,371 | 2026 and 2025 interim figures add the GLPI and VICI line to the small other financing obligations line (9M 2026: 1,030 plus 7; 9M 2025: 1,009 plus 6). Q2 and Q3 derived. |
| Income taxes paid, net | 81 | 3 | 8 | 3 | 14 | 61 | 34 | Supplemental cash flow; Q2 and Q3 derived. LTM calculated. |
| Cash and cash equivalents (unrestricted) | 887 | 867 | 965 | 864 | n/a (instant) | n/a (instant) | n/a (instant) | Balance sheets (10-K page:99; 10-Qs page:2). |
| Total debt, face value | 11,905 | 11,917 | 11,807 | 11,659 | n/a (instant) | n/a (instant) | n/a (instant) | Debt notes (10-K page:122; Q1 10-Q page:12; Q2 10-Q page:16; Q3 10-Q page:16). |
| Net debt (company definition) | 11,018 | 11,050 | 10,842 | 10,795 | n/a (instant) | n/a (instant) | n/a (instant) | Releases page:2; equals total outstanding indebtedness less cash and cash equivalents. |
| Long-term financing obligations (carrying value) | 13,096 | 13,126 | 13,157 | 13,188 | n/a (instant) | n/a (instant) | n/a (instant) | Balance sheets; outside debt. |
| Revolver availability, company basis | 1,946 | 1,893 | 1,963 | 2,083 | n/a (instant) | n/a (instant) | n/a (instant) | Liquidity tables (10-K page:79; Q1 10-Q page:41; Q2 10-Q page:50; Q3 10-Q page:50), total less cash. |
| Total stockholders' equity | 3,686 | 3,597 | 3,552 | 3,446 | n/a (instant) | n/a (instant) | n/a (instant) | Equity statement (Q3 10-Q page:3 and page:4); includes noncontrolling interests. |
| Total debt / Adjusted EBITDA (x) | 3.29 | 3.29 | 3.29 | 3.26 | n/a (ratio) | n/a (ratio) | 3.26 | Calculated; LTM Adjusted EBITDA at each quarter-end. |
| Net debt / Adjusted EBITDA (x) | 3.04 | 3.05 | 3.02 | 3.02 | n/a (ratio) | n/a (ratio) | 3.02 | Calculated. |
| (Total debt + financing obligations) / Adjusted EBITDA (x) | 6.90 | 6.90 | 6.95 | 6.95 | n/a (ratio) | n/a (ratio) | 6.95 | Calculated; Adjusted EBITDA is stated before this rent, so the numerator and denominator are on the same basis. |
| Adjusted EBITDA / cash interest on debt (x) | 4.46 | 4.45 | 4.63 | 4.82 | n/a (ratio) | n/a (ratio) | 4.82 | Calculated on LTM cash interest paid for debt. |
| Adjusted EBITDA / (cash interest on debt + rent cash interest) (x) | 1.68 | 1.67 | 1.68 | 1.69 | n/a (ratio) | n/a (ratio) | 1.69 | Calculated. |
| (Operating cash flow less purchase of property and equipment) / total debt (%) | 4.17 | 4.51 | 5.17 | 4.99 | n/a (ratio) | n/a (ratio) | 4.99 | Calculated on LTM flows at each quarter-end. |

### Segment results

| Segment (US$m) | FY2025 revenue | FY2025 Adj. EBITDA | Q1 2026 revenue | Q1 2026 Adj. EBITDA | Q2 2026 revenue | Q2 2026 Adj. EBITDA | Q3 2026 revenue | Q3 2026 Adj. EBITDA | Q3 2025 revenue | Q3 2025 Adj. EBITDA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Las Vegas | 4,049 | 1,728 | 1,003 | 426 | 1,017 | 410 | 930 | 343 | 952 | 379 |
| Regional | 5,756 | 1,789 | 1,430 | 435 | 1,570 | 488 | 1,627 | 524 | 1,536 | 506 |
| Caesars Digital | 1,408 | 236 | 374 | 69 | 351 | 68 | 326 | 44 | 311 | 28 |
| Managed and Branded | 279 | 67 | 66 | 13 | 57 | 16 | 58 | 17 | 73 | 18 |
| Corporate and Other | (6) | (196) | (3) | (56) | (2) | (62) | (1) | (63) | (3) | (47) |
| Total | 11,486 | 3,624 | 2,870 | 887 | 2,993 | 920 | 2,940 | 865 | 2,869 | 884 |

Locators: 10-K page:148 to page:149; Q1 10-Q page:27; Q2 10-Q page:31; Q3 10-Q page:31 to page:32. The Q3 2026 Regional segment includes Caesars Windsor from March 3, 2026 (Q3 10-Q page:10). The filing states that Windsor management fees were previously in Managed and Branded and are in Regional from that date; the 2025 comparative columns carry no stated restatement.

### Debt by instrument

| Instrument | Security and guarantee | Final maturity | Rate | Face value, Q3 2026 | Book value, Q3 2026 | Face value, FY2025 |
| --- | --- | --- | --- | --- | --- | --- |
| CEI Revolving Credit Facility (2,250 commitment) | Senior secured; subsidiary guarantors | 2028 (January 31, 2028) | variable | 0 | 0 | 160 |
| CEI Term Loan A | Senior secured; subsidiary guarantors | 2028 | variable | 609 | 609 | 637 |
| CVA Revolving Credit Facility (25 commitment) | Secured by Caesars Virginia assets; no CEI guarantee | 2029 | variable | 0 | 0 | 0 |
| CVA Delayed Draw Term Loan | Secured by Caesars Virginia assets; no CEI guarantee | 2029 | variable | 371 | 367 | 386 |
| CEI Term Loan B | Senior secured; subsidiary guarantors | 2030 | variable | 2,012 | 1,988 | 2,031 |
| CEI Term Loan B-1 | Senior secured; subsidiary guarantors | 2031 | variable | 2,828 | 2,802 | 2,849 |
| CEI Senior Secured Notes due 2030 | Senior secured; subsidiary guarantors | 2030 | 7.00% | 2,000 | 1,988 | 2,000 |
| CEI Senior Secured Notes due 2032 | Senior secured; subsidiary guarantors | 2032 | 6.50% | 1,500 | 1,487 | 1,500 |
| CEI Senior Notes due 2029 | Senior unsecured; subsidiary guarantors | 2029 | 4.625% | 1,200 | 1,194 | 1,200 |
| CEI Senior Notes due 2032 | Senior unsecured; subsidiary guarantors | 2032 | 6.00% | 1,100 | 1,089 | 1,100 |
| Special Improvement District Bonds | Not stated | 2037 | 4.30% | 38 | 38 | 40 |
| Long-term notes and other payables | Not stated | Not stated | Not stated | 1 | 1 | 2 |
| Total debt | | | | 11,659 | 11,563 | 11,905 |

Locators: Q3 10-Q page:15 to page:16 (table), page:21 (guarantees and security), page:17 to page:20 (terms); 10-K page:122 (FY2025 column). The total row blank cells are not data. The CEI Senior Notes due 2027 were redeemed on July 8, 2025 (10-K page:80), so they are not outstanding at FY2025. Interest rate on the term loans: Term SOFR plus a margin of 2.25% (Q3 10-Q page:18 to page:19); weighted average rates were 6.12% on variable and 6.18% on fixed rate debt, with variable-rate borrowings of $5.8 billion, about 50% of debt (page:54).

### Leases and other claims outside debt

- Financing obligations: `Long-term financing obligations` were 13,188 at September 30, 2026, 13,157 at June 30, 2026, 13,126 at March 31, 2026 and 13,096 at December 31, 2025 (balance sheets, page:2). They arise from failed sale-leasebacks with VICI and GLPI. The 10-K splits them at December 31, 2025 as GLPI Leases 1,284 and VICI Leases 11,705 (10-K page:117), which total 12,989; the remaining 107 of the 13,096 balance is not itemised in the text read. The 10-Qs give no split.
- Why the balance grows: `cash payments are less than the interest expense recognized, which causes the failed-sale leaseback obligation to increase during the initial years of the lease term` (10-K page:118). The increase from December 31, 2025 to September 30, 2026 is 92 (calculated).
- Rent cash: cash interest paid for rent was 1,349 in FY2025 and 1,030 for GLPI and VICI in 9M 2026 (Q3 10-Q page:5). Management estimates `approximately $345 million` of lease payments to VICI and GLPI for the remainder of 2026 (Q3 10-Q page:51) and `approximately $1.4 billion` for 2026 (10-K page:80).
- Contractual terms: VICI leases have a 15-year initial term with four five-year renewals, CPI escalators with a 2% floor and a net revenue variable element; the next variable adjustment year begins in November 2027 (10-K page:116; Q3 10-Q page:51). The GLPI Master Lease runs through September 2038 with escalators (10-K page:117). The lease covenants require a minimum adjusted revenue to rent ratio of 1.20:1 for the GLPI Leases (Q3 10-Q page:52).
- Operating and finance leases: operating lease liability 742 and finance lease liabilities 147 at December 31, 2025 (10-K page:115 and page:116). The 10-Qs show no update beyond 203 of right-of-use assets obtained in exchange for lease liabilities in 9M 2026 (Q3 10-Q page:5); the filing does not state which lease it relates to. Separately, the Caesars Windsor lease has annual minimum rent of about 19 (Q3 10-Q page:10).
- Other commitments: sports sponsorship obligations 309 at September 30, 2026 (Q3 10-Q page:15); self-insurance liability 244 (page:15). Defined-benefit plans are small: the Tropicana Atlantic City plan had assets of 33 and obligations of 22, and the Scioto Downs plan about 1 each (10-K page:140). Multi-employer pension plan participation exists (10-K page:141); withdrawal liability amounts were not found. No factoring or supply-chain finance programme was found in the pack.
- Litigation and the data incident: the 10-K states the `Data Incident` has not had a material impact (10-K page:121); Q3 2026 litigation liabilities are `not material` (Q3 10-Q page:15). Merger-related suits have been threatened or filed (Q3 10-Q page:65), with no amount.

### Covenants and compliance

| Facility group | Test | Level | Reported figure | Headroom |
| --- | --- | --- | --- | --- |
| CEI Revolving Credit Facility and Term Loan A | Maximum net total leverage ratio | 6.50:1 | Not supplied: the 10-Q gives only a compliance statement | Not calculable: definition and covenant EBITDA not supplied |
| CEI Revolving Credit Facility and Term Loan A | Minimum fixed charge coverage ratio | 2.0:1 | Not supplied | Not calculable: fixed charges definition not supplied |
| CVA Revolving Credit Facility and Delayed Draw Term Loan | Maximum net total leverage ratio | 4:1 | Not supplied | Not calculable |
| CVA Revolving Credit Facility and Delayed Draw Term Loan | Minimum fixed charge coverage ratio | 1.05:1 | Not supplied | Not calculable |
| GLPI Leases | Minimum adjusted revenue to rent ratio | 1.20:1 | Not supplied | Not calculable |

Locators: Q3 10-Q page:20 to page:21 and page:52 to page:53. The company states it `was in compliance with all of the applicable financial covenants described above` at September 30, 2026. After repayment of Term Loan A, the revolver covenants are tested only when testing conditions are satisfied (page:20). The ratios computed in this answer use company Adjusted EBITDA and face debt; they are not covenant ratios, because the covenant definitions are not supplied and the company says its Adjusted EBITDA definition `may not be the same as the definitions used in any of our debt or lease agreements` (Q3 10-Q page:49). A reader must not compare 6.95x or 1.69x with 6.50:1 or 2.0:1.

### Events, comparability and subsequent events

- Pending merger: the Merger Agreement was signed May 27, 2026; consideration is `$31.00` per share in cash plus a ticking fee after June 26, 2027; stockholders approved on September 22, 2026; a termination fee of $200 million and a reverse termination fee of $450 million are described; the initial end date is May 27, 2027 (Q3 10-Q page:7 to page:9). The sources do not describe merger financing or the treatment of existing debt. Merger costs were 12 for Q3 2026 and 22 for 9M 2026 (page:10).
- Comparability: Caesars Windsor was consolidated into Regional from March 3, 2026 (purchased net assets included about 42 of furniture and equipment and 12 of net working capital); the Grand Bazaar interest was acquired on May 1, 2026 for about 66 including 10 deferred (Q3 10-Q page:10). The company states that the periods after these purchases are `not fully comparable` with earlier periods (Q3 10-Q page:11). Cash paid for asset acquisitions was 98 in 9M 2026.
- Financing events in 2026: the revolver was repaid from 160 to nil; 9M 2026 proceeds from long-term debt and revolving facilities were 1,335 and repayments 1,581 (Q3 10-Q page:4 to page:5). There was no share repurchase in 9M 2026 against 179 in 9M 2025; 221 of authorisation remains but `no share repurchases are expected` (page:53).
- Earlier: the 546 CEI Senior Notes due 2027 were redeemed on July 8, 2025 with revolver borrowings and note receivable proceeds (10-K page:80).
- Events after September 30, 2026 up to the cutoff: none stated in the Q3 10-Q; nothing is supplied after October 27, 2026.

### Interpretation: data to risk to credit implication

- Earnings: Adjusted EBITDA for 9M 2026 is 2,672 against 2,723, with Las Vegas 1,179 against 1,281 and Regional 1,447 against 1,385 (Q3 10-Q page:31 to page:32). The Las Vegas decline is attributed to fewer city-wide convention events and lower leisure visitation (Q3 10-Q page:46). Credit implication: the large Las Vegas segment, which carries the VICI Las Vegas lease, is the weak spot, and Regional growth includes the Windsor consolidation.
- Fixed charges: Adjusted EBITDA is before lease rent, so the lease cash interest of about 1,371 is a charge ahead of any debt service. Cash interest on debt is 741 and net loss attributable to Caesars is (533) over the last twelve months; interest expense, net of 2,287 exceeds operating income of 1,801 over the same period, and it includes lease interest. Credit implication: cover on all fixed charges is thin even though debt-only leverage looks moderate.
- Cash generation: 9M 2026 operating cash flow less purchase of property and equipment is 435 against 350, helped by lower capital expenditure (507 against 648) rather than higher operating cash (942 against 998). Credit implication: free cash flow depends on capital expenditure discipline; the 4.99% ratio to debt is low for the leverage.
- Liquidity and maturities: liquidity on the company basis is 2,947 including cash of 864, with the revolver undrawn. Debt maturing before 2029 is small (28 in remaining 2026, 114 in 2027, 646 in 2028), then 1,574 in 2029 and 3,962 in 2030. Credit implication: refinancing risk concentrates in 2029 and 2030, and the revolver and Term Loan A mature January 31, 2028, about fifteen months after the as-of date.
- Quality of the evidence: the quarterly statements are unaudited. The FY2025 statements are audited: the auditor states they `present fairly, in all material respects` the financial position and results (10-K page:96), in a report dated February 17, 2026 (10-K page:98). Adjusted EBITDA, net debt and the cash-interest lines are management or supplemental presentations; the 10-K labels Adjusted EBITDA as unaudited (10-K page:77).

## Calculations

All inputs are US$ millions from the cited pages. "LTM" means last twelve months and is calculated as FY2025 plus the year-to-date 2026 amount minus the year-to-date 2025 amount of the same length.

### LTM Adjusted EBITDA

- LTM Q1 2026: 3,624 + 887 - 884 = 3,627. Inputs: 10-K page:78; Q1 10-Q page:29 (887 and 884).
- LTM Q2 2026: 3,624 + 1,807 - 1,839 = 3,592. Inputs: Q2 10-Q page:34 (six months 1,807 and 1,839).
- LTM Q3 2026: 3,624 + 2,672 - 2,723 = 3,573. Inputs: Q3 10-Q page:34.
- Discrete quarters tie: 887 + 920 + 865 = 2,672.

### LTM and discrete cash flow and income lines

- Net revenues LTM: 11,486 + 8,803 - 8,570 = 11,719. Quarters: 2,870 + 2,993 + 2,940 = 8,803.
- Operating income LTM: 1,858 + 1,470 - 1,527 = 1,801. Quarters: 500 + 513 + 457 = 1,470.
- Interest expense, net LTM: 2,304 + 1,712 - 1,729 = 2,287. Quarters: 569 + 573 + 570 = 1,712.
- Net loss attributable LTM: -502 + -283 - -252 = -533. Quarters: -98 + -62 + -123 = -283.
- D&A LTM: 1,417 + 1,068 - 1,073 = 1,412.
- Operating cash flow: Q2 2026 = 675 - 204 = 471; Q3 2026 = 942 - 675 = 267; LTM = 1,302 + 942 - 998 = 1,246.
- Purchase of property and equipment: Q2 2026 = 335 - 168 = 167; Q3 2026 = 507 - 335 = 172; LTM = 805 + 507 - 648 = 664.
- Operating cash flow less purchase of property and equipment: FY2025 1,302 - 805 = 497; Q1 204 - 168 = 36; Q2 471 - 167 = 304; Q3 267 - 172 = 95; 9M 2026 942 - 507 = 435; 9M 2025 998 - 648 = 350; LTM 1,246 - 664 = 582.
- Cash interest on debt: Q2 2026 = 368 - 212 = 156; Q3 2026 = 580 - 368 = 212; LTM Q1 = 813 + 212 - 210 = 815; LTM Q2 = 813 + 368 - 405 = 776; LTM Q3 = 813 + 580 - 652 = 741.
- Rent cash interest: Q1 346; six months 2026 = 686 + 5 = 691, so Q2 = 691 - 346 = 345; nine months 2026 = 1,030 + 7 = 1,037, so Q3 = 1,037 - 691 = 346. 2025 comparatives: Q1 336; six months 672 + 0 = 672; nine months 1,009 + 6 = 1,015. LTM Q1 = 1,349 + 346 - 336 = 1,359; LTM Q2 = 1,349 + 691 - 672 = 1,368; LTM Q3 = 1,349 + 1,037 - 1,015 = 1,371.
- Income taxes paid: Q2 = 11 - 3 = 8; Q3 = 14 - 11 = 3; LTM = 81 + 14 - 61 = 34.
- LTM operating cash flow and purchases at Q1 and Q2: Q1 operating cash flow 1,302 + 204 - 218 = 1,288 and purchases 805 + 168 - 223 = 750; Q2 operating cash flow 1,302 + 675 - 680 = 1,297 and purchases 805 + 335 - 453 = 687.

### Leverage, cover and cash flow ratios

- Total debt / Adjusted EBITDA: FY2025 11,905 / 3,624 = 3.29x; Q1 11,917 / 3,627 = 3.29x; Q2 11,807 / 3,592 = 3.29x; Q3 11,659 / 3,573 = 3.26x.
- Net debt / Adjusted EBITDA: 11,018 / 3,624 = 3.04x; 11,050 / 3,627 = 3.05x; 10,842 / 3,592 = 3.02x; 10,795 / 3,573 = 3.02x. Net debt = face debt less cash and cash equivalents: 11,905 - 887 = 11,018; 11,917 - 867 = 11,050; 11,807 - 965 = 10,842; 11,659 - 864 = 10,795, all matching the releases.
- (Debt + financing obligations) / Adjusted EBITDA: (11,905 + 13,096) / 3,624 = 6.90x; (11,917 + 13,126) / 3,627 = 6.90x; (11,807 + 13,157) / 3,592 = 6.95x; (11,659 + 13,188) / 3,573 = 6.95x.
- Cash interest cover, debt only: 3,624 / 813 = 4.46x; 3,627 / 815 = 4.45x; 3,592 / 776 = 4.63x; 3,573 / 741 = 4.82x.
- Cash interest cover, all in: 3,624 / (813 + 1,349) = 3,624 / 2,162 = 1.68x; 3,627 / (815 + 1,359) = 3,627 / 2,174 = 1.67x; 3,592 / (776 + 1,368) = 3,592 / 2,144 = 1.68x; 3,573 / (741 + 1,371) = 3,573 / 2,112 = 1.69x.
- Free cash flow to debt: 497 / 11,905 = 4.17%; 538 / 11,917 = 4.51% (1,288 - 750 = 538); 610 / 11,807 = 5.17% (1,297 - 687 = 610); 582 / 11,659 = 4.99%.
- Adjusted EBITDA margin: FY2025 3,624 / 11,486 = 31.6%; LTM 3,573 / 11,719 = 30.5%.

### Liquidity

- FY2025: 887 + 2,075 - 83 - 46 = 2,833; availability 2,075 - 83 - 46 = 1,946. Net of letters of credit only: CEI 2,250 - 160 - 83 = 2,007 plus CVA 25 = 2,032.
- Q1 2026: 867 + 2,050 + 25 - 96 - 40 - 46 = 2,760; availability 1,893. Net of letters of credit only: 2,050 + 25 - 96 = 1,979.
- Q2 2026: 965 + 2,130 + 25 - 96 - 40 - 56 = 2,928; availability 1,963. Net of letters of credit only: 2,130 + 25 - 96 = 2,059.
- Q3 2026: 864 + 2,250 + 25 - 96 - 40 - 56 = 2,947 (matches release page:2); availability 2,083. Net of letters of credit only: 2,250 + 25 - 96 = 2,179.
- Letters of credit are reported against the CEI revolver (Q3 10-Q page:19); none is reported against the CVA revolver, which has a 10 letter of credit sub-facility.

### Tie-outs

- Q3 2026 total debt face: 609 + 371 + 2,012 + 2,828 + 2,000 + 1,500 + 1,200 + 1,100 + 38 + 1 = 11,659. Bank debt 609 + 371 + 2,012 + 2,828 = 5,820 and notes 2,000 + 1,500 + 1,200 + 1,100 = 5,800 match the release (page:2).
- Maturities: 28 + 114 + 646 + 1,574 + 3,962 + 5,335 = 11,659.
- Operating expenses to operating income, Q3 2026: 966 + 272 + 161 + 97 + 517 + 93 + 366 + 11 = 2,483; 2,940 - 2,483 = 457. 9M 2026: 2,823 + 827 + 480 + 287 + 1,542 + 275 + 1,068 + 31 = 7,333; 8,803 - 7,333 = 1,470. FY2025: 3,602 + 1,106 + 615 + 420 + 1,926 + 322 + 182 + 1,417 + 38 = 9,628; 11,486 - 9,628 = 1,858. No unresolved difference.
- Adjusted EBITDA reconciliation, 9M 2026: -283 + 52 - 10 - 1 + 0 + 1,712 + 1,068 + 64 + 70 = 2,672. Q3 2026: -123 + 16 - 10 + 4 + 0 + 570 + 366 + 19 + 23 = 865. FY2025: -502 + 65 - 11 - 2 + 4 + 2,304 + 182 + 1,417 + 72 + 95 = 3,624.
- Balance sheet, September 30, 2026: total liabilities 27,925 + total stockholders' equity 3,446 = 31,371 total assets.
- Financing obligations: 13,188 - 13,096 = 92; 13,096 - (1,284 + 11,705) = 107 not itemised.
- Debt change: 11,905 - 11,659 = 246; 9M 2026 repayments 1,581 less proceeds 1,335 = 246.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Covenant ratio values and covenant definitions not supplied; only levels and a compliance statement | High | CP-2, CP-5 | Obtain the CEI Credit Agreement and compliance certificates |
| Lease financing obligation split between VICI and GLPI only at December 31, 2025 (1,284 and 11,705); 107 of the 13,096 balance not itemised; nothing by landlord at later dates | Medium | CP-2 | Obtain the 10-K lease schedule update or the lease agreements |
| Merger financing and treatment of existing debt at closing not supplied | High | CP-1A, CP-2 | Obtain the Merger Agreement exhibits, proxy statement and financing commitments |
| Adjusted EBITDA is a company non-GAAP measure with add-backs (transaction costs and other net 64 for 9M 2026) and no reconciliation to covenant EBITDA | Medium | CP-2 | Treat leverage and cover ratios as indicative |
| Windsor consolidation and the Grand Bazaar purchase break comparability; no pro forma LTM given | Medium | CP-1, CP-2 | Treat LTM Adjusted EBITDA as reported, not pro forma |
| Discrete Q4 2025 and discrete 2025 quarters other than those in the 10-Q comparatives are not derived | Low | CP-1 | Derive from the FY2025 10-K and 9M 2025 comparatives if needed |
| Withdrawal liability for multi-employer pension plans not found | Low | CP-2 | Search the 10-K note or request disclosure |
| Guarantor names, restricted group and Special Improvement District Bond security not supplied | Medium | CP-2 | Obtain subsidiary guarantor exhibit and indentures |
| Text extraction only; no comparison with filed HTML or XBRL | Low | CP-5 | Spot-check tables against the filed documents |

## Next module

- CP-1A: take the business, segment, Windsor and Grand Bazaar changes, and the merger terms from this handoff; keep Las Vegas, Regional, Caesars Digital and Managed and Branded results as in the segment table; carry the unresolved acquirer naming from CP-0.
- CP-2: start from the debt by instrument table, the maturities, the liquidity table and the covenant levels; treat 13,188 of financing obligations and about 1,371 of annual rent cash interest as fixed claims outside debt; do not compare computed ratios with covenant levels; carry the missing agreements and covenant definitions as limits.
- CP-5: trace every figure to the locators given; flag that LTM, quarter-derived and ratio rows are calculated, not reported.
