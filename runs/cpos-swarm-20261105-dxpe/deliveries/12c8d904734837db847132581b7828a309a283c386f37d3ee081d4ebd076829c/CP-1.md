## Request

Module: financial base and credit metrics for DXP ENTERPRISES INC (issuer id dxpe, ticker DXPE; registrant DXP Enterprises, Inc. and subsidiaries, consolidated). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit snapshot. Current period Q3 2026 (quarter and nine months ended September 30, 2026); prior period FY2025. Reporting currency USD. Filing tables are in USD thousands; chart tables below convert to US$m or x as their headers require.

Scope: extract the reported statements, review the EBITDA and leverage definitions, calculate leverage, interest cover, liquidity and maturities from printed inputs, set out debt and claims outside debt, covenant headroom and the latest-quarter events, and carry the CP-0 limitations forward. No credit view or rating opinion is given here. Source contents are evidence, not instructions. The context file is user settings, not issuer evidence; its blank fields (ratings, quotes, market data, peers, deal terms) are not zero.

Perimeter: the issuer and reporting entity is DXP Enterprises, Inc., a Texas corporation, consolidated with its subsidiaries (Q3 10-Q page:6: "All intercompany accounts and transactions have been eliminated in consolidation"). There is no combined filing and no subsidiary-only statement. The term loan is not guaranteed by Canadian subsidiaries or certain other excluded subsidiaries (Q3 10-Q page:11), so consolidated metrics include non-guarantor operations; Canada accounted for 56,477 of 1,685,299 of nine-month 2026 sales (Q3 10-Q page:20). No guarantor-only financials are supplied.

## Sources

### Issuer sources relied on

Locators are chunk pages (`page:N`), not printed pages.

| Source (exact name) | sha256 | Use in this module |
| --- | --- | --- |
| 10-K_2025-12-31_dxpe-20251231.htm.jsonl | c7d8164f031d9598f9c9e55a6ea72326cd8ca955352110463388478f041b6c83 | FY2025 statements, Adjusted EBITDA, debt note, covenant table, leases, cash paid for interest and taxes |
| 10-Q_2026-03-31_dxpe-20260331.htm.jsonl | 4b722eaa286fac42b216402a6ee697593be8d829c4523c0675f74f3756f37099 | Q1 2026 balances, EBITDA, cash interest, ABL availability |
| 10-Q_2026-06-30_dxpe-20260630.htm.jsonl | 062fb840fed8d87a2ce7f779ade2c10a2a9fa08cd06748ccc79bfb77eaff175c | Six months 2026 balances, EBITDA, cash interest, ABL availability, July 2026 ABL amendment |
| 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | b25274cf886044ab8c2b70c234e1e7077124a752d54250ff0e625889085dbaa2 | Q3 2026 and nine-month 2026 statements, Note 8 debt, covenants, liquidity, acquisitions, subsequent events |
| EX-99.1_2026-05-07_earningsrelease3312026.htm.jsonl | 7239622f24e9378a19997bda2636b1f0c58c04309af7d0be42e5556062a8f4af | Covenant EBITDA headline for the twelve months to March 31, 2026 |
| EX-99.1_2026-08-05_earningsrelease6302026.htm.jsonl | 6d154d2d8605fdb9abb6da2ab17ed2ed1363c8da5b1cd9a1ff2db3ea0cf9c96c | Covenant EBITDA headline for the twelve months to June 30, 2026 |
| EX-99.1_2026-11-05_earningsrelease9302026.htm.jsonl | 7fc5ad335ae78b4ce865ab4ec5f61033f2b042958c1ba4a250444be1733b49a2 | Covenant EBITDA headline for the twelve months to September 30, 2026, Q3 reconciliations |
| context (1020710-dxp-enterprises-inc-dxpe.json) | be741ade5f3ce71fa0fd12e85135207822d5c3bd4725f3f29649b4083fde9ae2 | Settings only: dates, currency, pathway |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 1c28b410d01884432fc8e019b3403e1cf46fbc87c18718dda8f14d0e897e7ee0 | Source readiness: READY_WITH_LIMITATIONS; conflicts, gaps and version relationships carried forward below |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Gross leverage on company Adjusted EBITDA fell from 3.76x at FY2025 to 3.30x at Q3 2026, with net leverage of 2.44x. Liquidity was 411.0 US$m and interest cover on cash interest was 4.33x. | Medium | Leverage uses company-defined Adjusted EBITDA; the covenant EBITDA bridge and the covenant level for two quarter-ends are unresolved. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt is one floating-rate term loan of 839.525 US$m with no hedges disclosed at FY2025; 811.965 US$m falls due in 2030. | The wall is far out, but interest cost moves with rates and cash is the main buffer. | High |
| The revolving facility was undrawn and enlarged to 225.0 US$m in July 2026, leaving 192.2 US$m available after letters of credit. | Availability rose while cash fell over nine months 2026 after net acquisition spending. | High |
| Reported secured leverage of 2.30 to 1.00 sits well inside either covenant level the filings give for September 30, 2026. | The headroom is large, but the applicable level and the covenant EBITDA bridge are not documented. | Medium |
| Nine-month 2026 operating cash flow rose while cash taxes paid fell sharply against nine-month 2025. | Part of the cash flow improvement is tax timing, so last-twelve-month free cash flow may overstate a steady state. | Medium |

### Financial base view

The reported financial base is clean and internally consistent, and the requested metrics can be calculated from printed inputs with stated limitations. For the last twelve months to Q3 2026, built as FY2025 plus nine months 2026 less nine months 2025, sales were 2,212,689 and company-defined Adjusted EBITDA was 254,413 (USD thousands), a margin of 11.50 percent against 11.17 percent for FY2025. Total debt at September 30, 2026 was 839,525 of principal, entirely the Senior Secured Term Loan B; the revolving facility had nothing drawn and the promissory note was repaid. Cash was 218,834. On that Adjusted EBITDA, gross leverage is 3.30x and net leverage 2.44x, against 3.76x and 2.41x at FY2025. Net leverage was higher at the two intervening quarter-ends (2.74x and 2.53x) when cash was lower after acquisition spending (126,234 net cash paid for acquisitions in nine months 2026, Q3 10-Q page:3). Interest cover is 4.33x on last-twelve-month cash interest and 3.83x on interest expense. Liquidity of 411,005 is cash plus 192,171 of revolver availability after 32,829 of letters of credit.

Three limits shape how these numbers can be used. First, EBITDA is the company's own Adjusted EBITDA, which adds back stock compensation and non-recurring items and is not pro forma for acquisitions; the covenant EBITDA headline in the Q3 release is higher at 270,000 and no bridge is printed. Second, the term loan covenant level for the June 30, 2026 and September 30, 2026 tests differs between the 10-K and the 10-Qs (CP-0 conflict), so headroom is shown at both levels. Third, the last-twelve-month figures splice an audited year with unaudited interim periods. No restatement of FY2025 comparatives was found in the 2026 filings; the Q3 10-Q states that reclassifications "do not have a material effect" (page:6).

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 3.76 | 2.41 | x | Total debt 846,785 principal (Term Loan B 845,885 plus promissory note 900) at December 31, 2025, 10-K page:83; cash 303,783, 10-K page:68; Adjusted EBITDA 225,302, 10-K page:52. Company-defined EBITDA, excludes leases. |
| Q1 2026 LTM | 3.66 | 2.74 | x | Debt 844,665 and cash 213,381 at March 31, 2026 (Q1 10-Q pages 2 and 9). LTM Adjusted EBITDA 230,595 = 225,302 + 57,812 - 52,519. Not pro forma for acquisitions. |
| Q2 2026 LTM | 3.46 | 2.53 | x | Debt 842,545 and cash 226,618 at June 30, 2026 (Q2 10-Q pages 2 and 10). LTM Adjusted EBITDA 243,658 = 225,302 + 128,188 - 109,832. Not pro forma. |
| Q3 2026 LTM | 3.30 | 2.44 | x | Debt 839,525 and cash 218,834 at September 30, 2026 (Q3 10-Q pages 2 and 11). LTM Adjusted EBITDA 254,413 = 225,302 + 195,444 - 166,333. Not pro forma; covenant EBITDA headline is 270,000 (Q3 release page:2). |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 4.20 | x | Adjusted EBITDA 225,302 over cash paid for interest 53,698 (10-K page:92). |
| Q1 2026 LTM | 4.20 | x | LTM Adjusted EBITDA 230,595 over LTM cash interest 54,953 = 53,698 + 14,950 - 13,695 (Q1 10-Q page:16). |
| Q2 2026 LTM | 4.27 | x | 243,658 over 57,097 = 53,698 + 30,097 - 26,698 (Q2 10-Q page:18). |
| Q3 2026 LTM | 4.33 | x | 254,413 over 58,803 = 53,698 + 45,330 - 40,225 (Q3 10-Q page:19). On interest expense (66,455 LTM) the ratio is 3.83x. Cash interest is a year-to-date disclosure only, so LTM is spliced from three filings. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (December 31, 2025) | 303.8 | 153.5 | US$m | Cash 303,783; ABL capacity 185,000 less nil drawn less letters of credit 31,472 = 153,528 (10-K page:54). Rounded to 0.1. |
| Q1 2026 (March 31, 2026) | 213.4 | 153.3 | US$m | Cash 213,381; capacity 185,000 less letters of credit 31,731 = 153,269 (Q1 10-Q page:27). |
| Q2 2026 (June 30, 2026) | 226.6 | 147.9 | US$m | Cash 226,618; capacity 185,000 (before the July 2, 2026 increase) less letters of credit 37,117 = 147,883 (Q2 10-Q page:32). |
| Q3 2026 (September 30, 2026) | 218.8 | 192.2 | US$m | Cash 218,834; capacity 225,000 less letters of credit 32,829 = 192,171 (Q3 10-Q page:33); company states liquidity of 411.0 US$m, equal to the sum. Availability is printed as capacity less letters of credit; the borrowing base is not printed. No facility expires within twelve months. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q4 2026 (remainder of 2026) | 2.120 | US$m | Term Loan B scheduled amortisation at September 30, 2026, Q3 10-Q page:14. |
| FY2027 | 8.480 | US$m | Same table; 0.25 percent quarterly amortisation (Q3 10-Q page:11). |
| FY2028 | 8.480 | US$m | Same table. |
| FY2029 | 8.480 | US$m | Same table. The 10-K showed 9,080 for 2029 because it included the promissory note, now repaid. |
| FY2030 | 811.965 | US$m | Balloon on October 13, 2030 (Q3 10-Q page:11). Five-year total 839.525 equals total debt, so nothing falls due after 2030; the ABL (matures July 2, 2031) is undrawn. Excludes any excess cash flow sweep and lease payments. |

### Financials and credit metrics

| Metric (USD thousands) | FY2025 | Q3 2025 | Q3 2026 | 9M 2025 | 9M 2026 | LTM to Q3 2026 | Source and basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sales | 2,016,365 | 513,724 | 587,180 | 1,488,975 | 1,685,299 | 2,212,689 | Statements of operations: 10-K page:68; Q3 10-Q page:2. LTM calculated. |
| Gross profit | 635,928 | 161,259 | 180,508 | 469,337 | 532,181 | 698,772 | Same. LTM calculated. |
| SG&A | 459,058 | 117,561 | 128,046 | 339,138 | 381,752 | 501,672 | Same. Includes intangible amortisation. LTM calculated. |
| Income from operations | 176,870 | 43,698 | 52,462 | 130,199 | 150,429 | 197,100 | Gross profit less SG&A; checked. |
| Interest expense | 60,530 | 14,894 | 16,949 | 44,298 | 50,223 | 66,455 | Includes debt cost amortisation of 3,388 in 9M 2026 (Q3 10-Q page:3). |
| Income before income taxes | 119,222 | 29,452 | 36,463 | 88,221 | 102,809 | 133,810 | Reported; LTM calculated. |
| Net income | 88,677 | 21,631 | 26,870 | 65,832 | 75,556 | 98,401 | Reported; LTM calculated. |
| EBITDA (company) | 218,602 | 54,266 | 65,767 | 161,063 | 189,641 | 247,180 | 10-K page:52; Q3 10-Q page:31. |
| Adjusted EBITDA (company) | 225,302 | 56,501 | 67,256 | 166,333 | 195,444 | 254,413 | Adds stock compensation and non-recurring items. |
| Adjusted EBITDA margin | 11.2% | 11.0% | 11.5% | 11.2% | 11.6% | 11.5% | Reported except LTM, calculated at 11.50%. |
| Net cash from operating activities | 94,264 | 34,886 | 18,686 | 56,505 | 80,641 | 118,400 | Cash flow statements: 10-K page:70; Q3 release page:9; Q3 10-Q page:3. |
| Purchases of property and equipment | 40,286 | 6,740 | 4,238 | 37,000 | 10,153 | 13,439 | Same; shown as positive outflow. |
| Free cash flow (company definition) | 53,978 | 28,146 | 14,448 | 19,505 | 70,488 | 104,961 | Operating cash flow less purchases of property and equipment; before acquisitions (nine months 2026: 126,234). |
| Cash paid for interest | 53,698 | Not supplied: quarterly figure not printed | Not supplied: quarterly figure not printed | 40,225 | 45,330 | 58,803 | Year-to-date notes only: 10-K page:92; Q3 10-Q page:19. |
| Cash paid for income taxes | 36,399 | Not supplied: quarterly figure not printed | Not supplied: quarterly figure not printed | 35,095 | 6,579 | 7,883 | Same. Provision for income taxes was 27,253 in 9M 2026 (Q3 10-Q page:2). |

### Balance sheet and capital structure

| Item (USD thousands) | December 31, 2025 | March 31, 2026 | June 30, 2026 | September 30, 2026 | Source |
| --- | --- | --- | --- | --- | --- |
| Cash (no restricted cash reported) | 303,783 | 213,381 | 226,618 | 218,834 | 10-K page:68; Q1 10-Q page:2; Q2 10-Q page:2; Q3 10-Q page:2 |
| ABL Revolver drawn | nil | nil | nil | nil | Debt notes: 10-K page:83; Q1 page:9; Q2 page:10; Q3 page:10 |
| Senior Secured Term Loan B principal | 845,885 | 843,765 | 841,645 | 839,525 | Same |
| Promissory note | 900 | 900 | 900 | nil (repaid) | Calculated as total debt less Term Loan B for Q1 and Q2; Q3 10-Q page:14 |
| Total debt (principal) | 846,785 | 844,665 | 842,545 | 839,525 | Same |
| Unamortized discount and issuance costs | 19,729 | 18,725 | 17,600 | 16,309 | Same |
| Debt on balance sheet (current plus long-term, net) | 827,056 | 825,940 | 824,945 | 823,216 | Calculated: current maturities 8,580 / 8,580 / 8,580 / 8,480 plus long-term debt 818,476 / 817,360 / 816,365 / 814,736 |
| Operating lease liabilities (short plus long-term) | 76,547 | 76,073 | 74,056 | 74,724 | 10-K page:78; Q1 10-Q pages 2 and 3 (19,398 plus 56,675); Q2 10-Q page:3 (19,522 plus 54,534); Q3 10-Q page:3 (20,042 plus 54,682) |
| Finance lease liabilities | 20,883 | Not supplied | Not supplied | Not supplied: no lease note in the 10-Qs | 10-K page:78 (current 7,660 in other current liabilities; non-current 13,223 in other long-term liabilities) |
| Contingent consideration (acquisitions) | 13,775 | 29.1 million (rounded) | 29,826 | 30,711 | Q1 10-Q page:6 ("$29.1 million"); Q2 10-Q page:7; Q3 10-Q page:8 (current 13.4 and long-term 17.3 in millions) |
| Total shareholders' equity | 498,439 | 512,197 | 540,741 | 570,414 | Statements of equity: Q3 10-Q page:4 |

### Segment base

| Segment (USD thousands) | Q3 2025 sales | Q3 2026 sales | Q3 2025 operating income | Q3 2026 operating income | 9M 2026 sales | 9M 2026 operating income |
| --- | --- | --- | --- | --- | --- | --- |
| Service Centers | 350,179 | 376,637 | 51,346 | 55,614 | 1,082,511 | 159,454 |
| Innovative Pumping Solutions | 100,551 | 144,115 | 18,399 | 23,444 | 405,514 | 71,777 |
| Supply Chain Services | 62,994 | 66,428 | 5,304 | 5,998 | 197,274 | 18,896 |
| Total segments | 513,724 | 587,180 | 75,049 | 85,056 | 1,685,299 | 250,127 |

Source: Q3 10-Q pages 16 and 17. Segment income is before intangible amortisation (6,899 in Q3 2026) and corporate expenses (25,695 in Q3 2026), per the Q3 release reconciliation (page:7). Acquisition sales were 48,832 of Q3 2026 sales, all in IPS (Q3 10-Q page:20); organic sales were 538,348.

### Statement bridges and definition review

EBITDA definition. The company defines EBITDA as net income attributable to DXP plus interest, taxes, depreciation and amortization, and Adjusted EBITDA as EBITDA plus stock-based compensation and all other non-cash charges, adjustments and non-recurring items (Q3 10-Q page:31). Depreciation and amortization in the reconciliation is depreciation plus amortization of intangibles and finance lease assets: 8,992 plus 27,617 equals 36,609 for nine months 2026 (cash flow statement, Q3 10-Q page:3), and 10,372 plus 28,478 equals 38,850 for FY2025 (10-K page:69). Operating lease cost stays in operating expenses, so Adjusted EBITDA is after rent. Debt issuance cost amortization sits in interest expense and is added back through interest.

Reconciliation checks (all agree to the printed totals):

| Check | Inputs | Result | Printed |
| --- | --- | --- | --- |
| Q3 2026 EBITDA | 36,463 + 16,949 + 12,355 | 65,767 | 65,767 (Q3 10-Q page:31; release page:8) |
| Q3 2026 Adjusted EBITDA | 65,767 + 1,489 + 0 | 67,256 | 67,256 |
| 9M 2026 EBITDA | 102,809 + 50,223 + 36,609 | 189,641 | 189,641 |
| 9M 2026 Adjusted EBITDA | 189,641 + 4,757 + 1,046 | 195,444 | 195,444 |
| FY2025 EBITDA | 88,677 + 60,530 + 30,545 + 38,850 | 218,602 | 218,602 (10-K page:52) |
| FY2025 Adjusted EBITDA | 218,602 + 5,708 + 992 | 225,302 | 225,302 |
| 9M 2026 operating income | 532,181 - 381,752 | 150,429 | 150,429 |
| 9M 2026 segment bridge | 250,127 - 20,714 - 78,984 | 150,429 | 150,429 (release page:7) |

The non-recurring add-back is described differently in the Q3 release ("non-recurring costs not related to continuing business operations", page:8) and the Q3 10-Q ("unique acquisition integration costs and other non-cash, non-recurring costs", page:31); the 10-Q controls (CP-0 conflict). The add-back was 1,046 in nine months 2026 and nil in Q3 2026.

Expense block. For this issuer the by-function income statement runs sales, cost of sales, gross profit, then one SG&A line, then income from operations. Intangible amortization (20,714 in nine months 2026) is inside SG&A, as the segment note shows corporate "Other" containing SG&A of 75.5 million and intangible amortization of 20.7 million (Q3 10-Q page:17). There is no separate amortization line to reconcile, and no unresolved difference.

Covenant EBITDA. The term loan defines covenant EBITDA as net income plus tax, franchise tax, interest, depreciation and amortization, all non-cash charges and adjustments, and non-recurring cash expenses related to the term loan, with pro forma effect for acquisitions and disposals (10-K page:85). That definition differs from company Adjusted EBITDA, and its pro forma treatment of acquisitions is a possible reason why the headline covenant EBITDA of 270,000 exceeds LTM Adjusted EBITDA of 254,413, but no source says so. The 15,587 difference is not bridged in any source.

### Debt and claims outside debt

| Claim | Terms and amount | Inside the debt figure? | Source |
| --- | --- | --- | --- |
| Senior Secured Term Loan B | 839,525 at September 30, 2026; borrower DXP Enterprises, Inc.; agent Goldman Sachs Bank USA; Term SOFR (floor 1.00 percent) plus 3.25 percent, 7.15 percent at September 30, 2026; 0.25 percent quarterly amortisation; matures October 13, 2030; guaranteed by material wholly owned direct and indirect subsidiaries other than Canadian and certain excluded subsidiaries; incremental capacity up to 100 million; fair value 846.9 US$m (level 2) | Yes | Q3 10-Q pages 10-12 |
| ABL Revolver | 225,000 commitment under the July 2, 2026 Second Amended and Restated Loan and Security Agreement (Bank of America, N.A. as agent, Q3 10-Q page:36), nil drawn, matures July 2, 2031, Term SOFR or Term CORRA plus 1.25 to 1.75 percent, unused fee 0.375 percent, first-priority lien on U.S. and Canadian receivables and inventory ranking ahead of the term loan on that collateral; guarantors: DXP Enterprises, Inc. and material wholly owned U.S. subsidiaries, plus Canadian subsidiaries for the Canadian borrowers; may increase by up to 50 million | Nil drawn | Q3 10-Q pages 12 and 13 |
| Letters of credit under the ABL | 32,829 | No: reduces availability, not debt | Q3 10-Q page:33 |
| Promissory note due November 1, 2029 | Nil at September 30, 2026 (900 at December 31, 2025), 5 percent | Repaid | Q3 10-Q page:14 |
| Finance leases | 20,883 at December 31, 2025; interest about 1.6 million in nine months 2026; principal payments 6,877 in nine months 2026 | No: in other liabilities | 10-K page:78; Q3 10-Q pages 4 and 14 |
| Operating leases | 74,724 at September 30, 2026 | No | Q3 10-Q page:3 |
| Related-party leases | Lease expense of about 2.3 million in FY2025 to entities controlled by the CEO and family | No | 10-K page:100 |
| Acquisition contingent consideration | 30,711 at September 30, 2026; maximum payable 34.0 US$m over three years; discount rate 8.6 percent | No | Q3 10-Q page:8 |
| Pensions and retiree medical, purchase commitments, factoring and supply-chain finance | Not found by text search in the pack. A 401(k) plan with company matching is mentioned (10-K page:15). Litigation is described as ordinary course with no material effect expected (Q3 10-Q page:15) | Not applicable | Not supplied |
| Preferred stock | Series A and Series B preferred carried at 1 and 15 (USD thousands); Series B convertible into 840,000 common shares; dividends 68 for nine months 2026 | No: equity | Q3 10-Q pages 2 and 15 |

The wall is one tranche. Floating-rate exposure is unhedged as of FY2025 (10-K page:64: "As of December 31, 2025, we had no interest rate hedges in place"); no later hedge disclosure was found. The 10-K's own sensitivity was an 8.5 million pre-tax change in interest expense for a 100 basis point move on the FY2025 base (page:64). Excess cash flow sweep: 50 percent, reducing to 25 percent if the Total Leverage Ratio is at or below 3.00 to 1.00, and none at or below 2.50 to 1.00 (Q3 10-Q page:12). The Total Leverage Ratio definition is not printed, so whether a sweep applies for FY2026 cannot be computed.

### Covenants

| Test | Level | Reported | Headroom | Notes |
| --- | --- | --- | --- | --- |
| Term loan Secured Leverage Ratio, September 30, 2026 | 5.50:1.00 per the 10-K step-down table (page:84); less than 5.75 to 1.00 per the Q3 10-Q (page:12) | 2.30 to 1.00 (Q3 10-Q page:12) | 3.20 turns to the 5.50 level; 3.45 turns to the 5.75 level | Calculated. Applicable level unresolved (CP-0 conflict). Later steps: 5.25 from March 31, 2027, 5.00 from December 31, 2027, 4.75 from June 30, 2028 (10-K page:84). |
| Same, as EBITDA cushion | Secured net debt 620,691 = 839,525 - 218,834 (cash below the 330 million netting cap) | Covenant EBITDA 270,000 | EBITDA could fall to 112,853 at 5.50 (58.2 percent below 270,000) or 107,946 at 5.75 (60.0 percent below) | Calculated; assumes all debt is secured and no other secured debt counts. Check: 620,691 / 270,000 = 2.30, matching the reported ratio. |
| ABL Fixed Charge Coverage Ratio | Not less than 1.00 to 1.00, tested only during a compliance period triggered when availability falls below a threshold that is not printed | 2.98 to 1.00 (Q3 10-Q page:13) | 1.98 turns above the minimum | Calculated difference. Availability of 192.2 US$m; the threshold is not supplied. |

Covenant EBITDA headlines by test date: 243.9 US$m (twelve months to March 31, 2026), 267.3 (June 30, 2026), 270.0 (September 30, 2026), from the three releases (page:2 of each). Reported secured leverage was 2.25 at December 31, 2025 (10-K page:84), 2.59 at March 31, 2026, 2.30 at June 30, 2026 and 2.30 at September 30, 2026. The company states it was in compliance with all financial covenants at September 30, 2026 (Q3 10-Q page:13).

### Latest quarter and subsequent events

| Date | Event | Amount and source |
| --- | --- | --- |
| July 2, 2026 | Second Amended and Restated ABL: commitment raised from 185.0 to 225.0 US$m, maturity moved from July 19, 2027 to July 2, 2031 | Q2 10-Q page:20; Q3 10-Q page:12; 10-K page:85 |
| July 20, 2026 | S&P upgraded issuer credit and issue-level rating from B to B+ (issuer statement; no rating report supplied) | Q3 10-Q page:33 |
| August 1, 2026 | Acquisition of Mequipco Ltd. (Canadian water and wastewater) for cash and 9,456 shares | Q2 10-Q page:20; Q3 10-Q page:35 |
| Q3 2026 | One acquisition in the quarter: cash 13,399, stock 1,485, contingent 3,190, total consideration 18,074, goodwill 12,637. Five acquisitions in nine months 2026: total consideration 153,633, cash 130,121 | Q3 10-Q page:18 |
| August 2026 | The 85.0 million share repurchase program completed; no shares repurchased in nine months 2026 | Q3 10-Q page:19 |
| October 28, 2026 (subsequent) | New repurchase program of up to 150.0 million or 1.0 million shares over 24 months | Q3 10-Q page:21 |
| November 1, 2026 (subsequent) | Agreement to acquire MDS of Michigan, LLC, funded from balance sheet cash; amount not given | Q3 10-Q page:21 |

Nine-month 2026 cash flow: operating 80,641, investing (135,755), financing (28,151), foreign currency (1,684), net change (84,949) (Q3 10-Q page:4). Management attributes the improvement in operating cash flow to higher net income and lower tax payments (page:32). Management's statement that Q3 set "a new sales high watermark" (release page:2) is management language and is not tested here against all prior quarters.

### Consistency with the CP-0 handoff

This module relies on CP-0 and corrects nothing in it. It adds locators CP-0 did not need: debt maturities at Q3 10-Q page:14, covenant detail at Q3 10-Q pages 12 and 13. The CP-0 conflicts on the covenant level and on the ABL terms are applied as stated.

## Calculations

All figures are USD thousands unless stated. LTM means last twelve months and is built as FY2025 + nine months 2026 - nine months 2025; for the Q1 and Q2 columns the year-to-date amounts of the matching 2026 and 2025 quarters are used.

LTM Adjusted EBITDA
- Q1 2026: 225,302 + 57,812 - 52,519 = 230,595 (10-K page:52; Q1 10-Q page:25)
- Q2 2026: 225,302 + 128,188 - 109,832 = 243,658 (Q2 10-Q page:30)
- Q3 2026: 225,302 + 195,444 - 166,333 = 254,413 (Q3 10-Q page:31)

Leverage (total debt principal, net debt = principal less cash)
- FY2025: 846,785 / 225,302 = 3.758x; (846,785 - 303,783) / 225,302 = 543,002 / 225,302 = 2.410x
- Q1 2026: 844,665 / 230,595 = 3.663x; (844,665 - 213,381) = 631,284; 631,284 / 230,595 = 2.738x
- Q2 2026: 842,545 / 243,658 = 3.458x; (842,545 - 226,618) = 615,927; 615,927 / 243,658 = 2.528x
- Q3 2026: 839,525 / 254,413 = 3.300x; (839,525 - 218,834) = 620,691; 620,691 / 254,413 = 2.440x
- On the covenant EBITDA headline: 620,691 / 270,000 = 2.299x, against 2.30x reported.

LTM cash interest and cover
- Q1 2026: 53,698 + 14,950 - 13,695 = 54,953; 230,595 / 54,953 = 4.196x
- Q2 2026: 53,698 + 30,097 - 26,698 = 57,097; 243,658 / 57,097 = 4.267x
- Q3 2026: 53,698 + 45,330 - 40,225 = 58,803; 254,413 / 58,803 = 4.327x
- FY2025: 225,302 / 53,698 = 4.196x
- On interest expense: LTM 60,530 + 50,223 - 44,298 = 66,455; 254,413 / 66,455 = 3.828x

LTM operating items (Q3 2026): sales 2,016,365 + 1,685,299 - 1,488,975 = 2,212,689; gross profit 635,928 + 532,181 - 469,337 = 698,772; SG&A 459,058 + 381,752 - 339,138 = 501,672; income from operations 176,870 + 150,429 - 130,199 = 197,100; income before taxes 119,222 + 102,809 - 88,221 = 133,810; net income 88,677 + 75,556 - 65,832 = 98,401; EBITDA 218,602 + 189,641 - 161,063 = 247,180; operating cash flow 94,264 + 80,641 - 56,505 = 118,400; capital expenditure 40,286 + 10,153 - 37,000 = 13,439; free cash flow 118,400 - 13,439 = 104,961; cash taxes 36,399 + 6,579 - 35,095 = 7,883; Adjusted EBITDA margin 254,413 / 2,212,689 = 11.50 percent.

Liquidity: Q3 2026 218,834 + (225,000 - 0 - 32,829) = 218,834 + 192,171 = 411,005. Q2 2026 226,618 + (185,000 - 37,117) = 374,501. Q1 2026 213,381 + 153,269 = 366,650. FY2025 303,783 + 153,528 = 457,311.

Maturities: 2,120 + 8,480 + 8,480 + 8,480 + 811,965 = 839,525, equal to total debt.

Balance sheet debt: FY2025 8,580 + 818,476 = 827,056; Q3 2026 8,480 + 814,736 = 823,216; principal less unamortized discount and costs: 839,525 - 16,309 = 823,216 (agrees).

Covenant headroom: 5.50 - 2.30 = 3.20; 5.75 - 2.30 = 3.45; EBITDA floor 620,691 / 5.50 = 112,853 (1 - 112,853 / 270,000 = 58.2 percent); 620,691 / 5.75 = 107,946 (60.0 percent); FCCR 2.98 - 1.00 = 1.98. Difference between covenant EBITDA and LTM Adjusted EBITDA: 270,000 - 254,413 = 15,587.

Lease and other: operating lease liabilities at September 30, 2026: 20,042 + 54,682 = 74,724; at December 31, 2025: 19,038 + 57,509 = 76,547. Finance lease liabilities at December 31, 2025: 7,660 + 13,223 = 20,883 (agrees to the lease table, 10-K page:79).

Limitations of the calculations: LTM Adjusted EBITDA is not pro forma for acquisitions, which depresses leverage comparability with the covenant basis; lease liabilities are excluded from every leverage ratio; net debt nets all cash with no trapped-cash adjustment because none is disclosed (the foreign share of cash is not supplied); cash interest is year-to-date only.

## Gaps

| Gap | Affected metric or consumer | Severity | Remediation |
| --- | --- | --- | --- |
| Covenant level conflict for June 30, 2026 and September 30, 2026 (10-K table 5.50 versus 10-Q less than 5.75) | Covenant headroom; CP-2, CP-5 | Medium | Obtain the Term Loan Amendment dated December 16, 2025 and any later amendment; until then show both levels |
| No bridge from company Adjusted EBITDA to covenant EBITDA (15,587 difference at Q3 2026) | Covenant leverage; CP-2 | Medium | Obtain compliance certificate or label covenant EBITDA as management-attributed |
| Leverage is not pro forma for acquisitions | Leverage trend, CP-2 | Low | Pro forma sales and net income exist (Q3 10-Q page:19) but no pro forma EBITDA; do not infer one |
| Cash interest and cash taxes are year-to-date only; discrete Q3 figures not printed | Interest cover, tax quality | Low | LTM is spliced from year-to-date disclosures |
| Finance lease liabilities at September 30, 2026 not supplied; Q1 and Q2 lease balances not read | Lease-adjusted debt | Low | Use December 31, 2025 balance, labelled |
| ABL borrowing base and compliance-period availability threshold not printed | Usable liquidity; FCCR relevance | Low | Obtain borrowing base certificate and credit agreement |
| Total Leverage Ratio definition for the excess cash flow sweep not printed | FY2026 mandatory prepayment | Low | Obtain term loan agreement |
| Geographic split of cash (Canadian subsidiaries are non-guarantors) not supplied | Net debt | Low | None in the pack |
| Cash taxes in nine months 2026 well below the provision, with deferred taxes of 11,087 and an income taxes working-capital inflow of 7,303 (Q3 10-Q page:3) | Free cash flow durability | Medium | Treat LTM free cash flow with caution; cash taxes in FY2025 were 36,399 |
| No hedge disclosure after December 31, 2025 (Q3 10-Q refers to the 10-K for market risk, page:34) | Interest rate exposure | Low | Assume unchanged unless stated |
| Rating: issuer statement only | CP-2 | Low | CP-0 gap carried forward |

## Next module

CP-1A should run next, using this handoff's debt, liquidity and covenant tables and the CP-0 source register. It should treat the acquisition programme (five deals in nine months 2026, funded mainly by cash on hand), the ABL replacement and the repurchase authorisation as the key business and capital-allocation facts, keep Adjusted EBITDA and covenant EBITDA labelled separately, and carry the covenant level conflict forward unresolved.
