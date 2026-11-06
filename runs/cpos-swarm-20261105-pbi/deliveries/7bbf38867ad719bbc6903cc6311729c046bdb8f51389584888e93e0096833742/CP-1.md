## Request

Issuer: PITNEY BOWES INC /DE/ (Pitney Bowes Inc., Delaware, NYSE: PBI, issuer id pbi). As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. The filings print thousands of US dollars; this handoff converts to US$ millions with one decimal (ratios to two decimals) and keeps the printed thousands in Calculations. Current period: Q3 2026 (three months and nine months ended 2026-09-30); prior period: FY2025.

Scope: the financial base for the credit snapshot. It extracts the reported statement lines, the debt and liquidity position, the maturity profile, the claims outside debt and the covenant evidence, then calculates leverage, interest cover and liquidity on stated bases and judges what the evidence supports. It gives no credit conclusion beyond the financial base and no rating view.

Perimeter: Pitney Bowes Inc. and its wholly owned subsidiaries, consolidated (10-K page:69). The notes name no borrower other than the Company and no guarantor, and no guarantor or Pitney Bowes Bank stand-alone financial data is supplied, so every figure below is consolidated. The consolidated statements include the Pitney Bowes Bank, whose customer deposits sit outside the debt table.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_pbi-20251231.htm.jsonl | 4f5deb57a07fe1eea64b3f9a9468185d34382c2ac8c5a94646c45747e0b2326e | FY2025 and FY2024 statements (pages 64-67), segment reconciliation (page:84), debt Note 13 (pages 97-101), leases (page:116), pensions (pages 102 and 110), future cash requirements (page:44), cash interest paid (page:96) |
| 10-Q_2026-03-31_pbi-20260331.htm.jsonl | 624a80b6cca522410fd3993e4d3c4a11f7096c24a4986d50fced927a53e82f28 | Position at 2026-03-31 (pages 2-4), debt table (page:18), cash interest (page:24) |
| 10-Q_2026-06-30_pbi-20260630.htm.jsonl | 1df859f2a36df1a95ab3c12f91757b26486c9d8b234afc186a635a7369a5958d | Position at 2026-06-30 (pages 2-4), debt table and revolver capacity (pages 19-20), cash interest (page:26) |
| 10-Q_2026-09-30_pbi-20260930.htm.jsonl | 9ac96ecd84cbfc34b739239b40a8f155d4a7193f9d71c03e1504313a41bfda22 | Primary source: statements (pages 2-4), segments (pages 9-10), debt Note 10 (pages 19-22), pensions (page:23), contingencies (page:24), liquidity and covenants (pages 34 and 36) |
| EX-99.1_2026-05-05_q12026earningspressrelea.htm.jsonl | 429691f75b3fe167dac89bd697b030c14535bbbb0b53e2afaf1e37a0eeb21619 | Q1 2026 Adjusted EBITDA and free cash flow reconciliation (page:7), attributed |
| EX-99.1_2026-07-29_q22026earningspressrelea.htm.jsonl | 0a144327096e38bc9546ab64951475ad37b63f71db5dc4f751be723ca256bc40 | Q2 and six-month Adjusted EBITDA and free cash flow reconciliation (page:9), attributed |
| EX-99.1_2026-10-28_ex991q32026earningspress.htm.jsonl | 42e81ba5c9c8e886a22fe22bd69da5cf53cfc84b55897aeb23cc53c06bbc9f1b | Q3 and nine-month Adjusted EBITDA and free cash flow reconciliation (page:9), segment tables (page:8), guidance (pages 2-3), attributed |

The run context (sha256 c37c14ec550e9841f87339ac47485b30200b39c05673baeb478fd6400a5b7677) supplies dates and currency only and is not issuer evidence.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 (source readiness) | cad86cb0a3fd98500e899a766aea0470956626c6150c1885edf57ff710f357b9 | Source map, gap register, version and maturity conflicts, covenant and letters-of-credit limits; read in full and carried forward |

### Corrections and refinements to the supplied handoff

The source-readiness handoff cannot be edited, so its points are checked here. No statement in it is found wrong. Two are refined. First, it logged the unitemized 23 million difference between the 450 million facility and the 427 million capacity as unexplained; the Q2 10-Q prints capacity of 330 million at 2026-06-30 against 96.7 million drawn (page:20 and page:19), which leaves the same gap of about 23.3 million, so the gap is stable across two quarters, consistent with letters of credit but still not stated as such. Second, it logged the 5 million tender gain in the Q3 10-Q text against the (3,155) table amount as an unexplained difference; the principal roll-forward in Calculations shows cash principal payments of 402,032 against 407,778 of observed principal reductions, an implied 5,746 discount to par, which is consistent with the narrative "gain of $5 million" and with a smaller net table gain after other items. The sources do not state this reconciliation, so it remains an inference.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| On the company basis, total debt principal of 1,918.4 at 2026-09-30 is 3.24x LTM Adjusted EBITDA of 591.5, or 2.79x net of cash, down from 3.54x and 3.04x at FY2025. | Medium | Adjusted EBITDA is calculated for FY2025 and LTM, adds back terminated-plan pension expense in 2026 only, and covenant headroom cannot be calculated without the credit agreement. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt principal fell 107.8 in nine months to 1,918.4, and no instrument has a final maturity before March 2029, when 476.0 of notes fall due. | Near-term refinancing need is low, but springing provisions tie the term loan and revolver to the 2029 notes and the 2030 convertible. | High |
| Liquidity at 2026-09-30 was cash of 268.5 plus 427.0 of printed revolver capacity, or 695.5. | The buffer is modest against springing tests whose liquidity definition is not supplied. | Medium |
| Cash interest cover was 4.34x on LTM Adjusted EBITDA against 4.03x at FY2025. | Coverage is comfortable on this basis, but the covenant coverage ratio uses defined terms that are not supplied. | Medium |
| Nine-month Adjusted EBITDA rose 18.6 to 432.4, yet a 23.1 pension add-back applies to 2026 only; excluding it gives 409.3 against 413.8. | Underlying earnings are flat to slightly lower, so leverage improvement rests on debt paydown rather than earnings growth. | Medium |
| Nine-month operating cash flow was 348.2 against 161.6, including 87.5 from finance receivable run-off, while buybacks and dividends took 246.3. | Cash generation is strong but partly liquidates the finance book, and shareholder returns exceed debt reduction. | Medium |

### Financial base view

The financial base is adequate for a leverage, interest-cover, liquidity and maturity review to 2026-09-30, on the stated bases and with named restrictions. No consolidated Adjusted EBITDA is printed for FY2025 or for any period in the 10-Qs; the releases print it for Q1 to Q3 of 2026 and of 2025, so leverage is built on Adjusted EBITDA as the Q1, Q2 and Q3 2026 releases print it, with FY2025 calculated from the filed segment reconciliation and tied to the release method. The reading is that debt principal has fallen from 2,026.2 to 1,918.4 since December 2025 while LTM Adjusted EBITDA is 591.5 on the company basis, so gross leverage is 3.24x and net leverage 2.79x. Two bases must be shown together: the company basis, and a sensitivity that removes the 23.1 of terminated-plan pension expense added back in 2026 only, which gives 3.38x gross and 2.90x net. Cash interest cover is 4.34x. Covenant ratios, headroom and the springing liquidity tests are Not calculable because the credit agreement definitions are not in the pack. Liquidity is cash of 268.5 plus the printed revolver capacity of 427.0.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | Not supplied: FY2024 Adjusted EBITDA is not printed and no FY2024 release is in the pack | Not supplied: same reason | x | Debt principal 1,955.5 and cash 469.7 at 2024-12-31 are printed (10-K page:98, page:65) but 2024 segments include Other operations and the ecommerce business was deconsolidated, so no EBITDA comparable with later periods is built. |
| FY2025 | 3.54 | 3.04 | x | Debt principal 2,026.2 and cash 284.9 at 2025-12-31 (10-K page:98, page:65) over FY2025 Adjusted EBITDA of 572.9, calculated as total adjusted segment EBIT 577.5 less corporate expenses 116.2 plus depreciation and amortization 111.6 (10-K page:84). Not printed; derived on the release method, which ties for the nine months of both years. |
| LTM Q1 2026 | 3.74 | 3.22 | x | Debt principal 2,172.7 and cash 302.9 at 2026-03-31 (Q1 10-Q page:18, page:2) over LTM Adjusted EBITDA of 580.9: FY2025 572.9 plus Q1 2026 156.0 less Q1 2025 148.0 (Q1 release page:7). Company basis; 2026 adds back terminated-plan pension expense, 2025 does not. |
| LTM Q2 2026 | 3.51 | 3.05 | x | Debt principal 2,066.8 and cash 266.8 at 2026-06-30 (Q2 10-Q page:19, page:3) over LTM Adjusted EBITDA of 589.6: 572.9 plus six months 2026 295.8 less six months 2025 279.1 (Q2 release page:9). Same pension basis caveat. |
| LTM Q3 2026 | 3.24 | 2.79 | x | Debt principal 1,918.4 and cash 268.5 at 2026-09-30 (Q3 10-Q page:19, page:3) over LTM Adjusted EBITDA of 591.5: 572.9 plus nine months 2026 432.4 less nine months 2025 413.8 (Q3 release page:9). On the 2025 definition (removing the 23.1 add-back) the ratios are 3.38 and 2.90. Cash excludes short-term investments of 12.7. Not the covenant ratio. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | Not supplied: FY2024 Adjusted EBITDA is not printed | x | Cash interest paid of 167.9 is printed (10-K page:96) but there is no comparable EBITDA. |
| FY2025 | 4.03 | x | Calculated Adjusted EBITDA 572.9 over cash interest paid 142.1 (10-K page:96). Cash interest covers the whole group including the financing business. |
| LTM Q1 2026 | 4.18 | x | 580.9 over LTM cash interest 138.9: FY2025 142.1 plus Q1 2026 46.0 less Q1 2025 49.3 (Q1 10-Q page:24). |
| LTM Q2 2026 | 4.14 | x | 589.6 over LTM cash interest 142.4: 142.1 plus six months 2026 72.2 less six months 2025 71.9 (Q2 10-Q page:26). |
| LTM Q3 2026 | 4.34 | x | 591.5 over LTM cash interest 136.3: 142.1 plus nine months 2026 114.0 less nine months 2025 119.9 (Q3 10-Q page:26). On the 2025 definition the cover is 4.17. Cash interest timing is uneven across quarters because coupons are semi-annual, so only LTM and annual figures are shown. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| 2024-12-31 | 469.7 | Not supplied: revolver availability at 2024-12-31 is not printed in the pack | US$m | Cash and cash equivalents (10-K page:65). The facility in force then was replaced in February 2025 and its terms are not in the pack. |
| 2025-12-31 | 284.9 | 373.0 | US$m | Calculated: 400.0 revolver, with no outstanding borrowings (10-K page:42, page:43), less approximately 27 of letters of credit that reduce borrowing capacity (10-K page:45). Capacity itself is not printed at this date. |
| 2026-03-31 | 302.9 | Not supplied: remaining borrowing capacity is not printed at 2026-03-31 | US$m | The 450.0 facility had no outstanding borrowings (Q1 10-Q page:19); the letters-of-credit amount at that date is not printed. Cash includes 42 held at foreign subsidiaries (Q1 10-Q page:30). |
| 2026-06-30 | 266.8 | 330.0 | US$m | Remaining borrowing capacity as printed (Q2 10-Q page:20), with 96.7 drawn at that date and repaid by July 30, 2026. |
| 2026-09-30 | 268.5 | 427.0 | US$m | Remaining borrowing capacity as printed (Q3 10-Q page:20); nothing drawn. Cash includes 64 held at foreign subsidiaries (Q3 10-Q page:34); short-term investments of 12.7 are excluded. The credit-agreement definition of liquidity is not supplied. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q4 2026 | Not supplied: scheduled term-loan amortization is not itemized by year at 2026-09-30 | US$m | No instrument has a final maturity in 2026. The current portion of long-term debt is 24.7 for the twelve months to 2027-09-30 (Q3 10-Q page:3); it sits inside the term loan balances shown below. |
| 2027 | Not supplied: scheduled term-loan amortization is not itemized by year | US$m | No final maturity in 2027: the 6.875% notes due March 2027 were repaid in Q2 2026 (Q3 10-Q page:20). |
| 2028 | Not supplied: scheduled term-loan amortization is not itemized by year | US$m | No final maturity in 2028. The 10-K schedule at 2025-12-31 (134.2 for 2028) pre-dates the 2026 refinancing and is not used (10-K page:101). |
| 2029 | 476.0 | US$m | 7.25% notes due March 2029 at 2026-09-30 (Q3 10-Q page:19). Springing provision applies to the term loan and revolver if not redeemed and liquidity is thin before December 14, 2028 (page:20). |
| 2030 | 230.0 | US$m | 1.50% convertible notes due August 2030 (page:19); conversion price 14.19; cash settlement up to principal. Springing provision before May 16, 2030 (page:20). |
| 2031 | 294.5 | US$m | Term loan at SOFR plus 2.10%, labelled due May 2031 in the Q3 10-Q (page:19) and March 2031 in the Q2 10-Q (page:19); the later label is used. Includes amortization due earlier. The 450.0 revolver, undrawn, is also stated to mature May 2031 (page:20). |
| 2032 | 584.0 | US$m | Term loan due March 2032 at SOFR plus 3.00% after a 0.75% repricing in Q3 2026 (page:19, page:20). Includes amortization due earlier. |
| 2033 and later | 334.0 | US$m | Notes due January 2037 (25.4) and March 2043 (308.5) (page:19). Rows sum to 1,918.5 against principal of 1,918.4 because of rounding. |

### Financials and credit metrics

| Metric (US$m) | FY2024 | FY2025 | Q3 2025 | Q3 2026 | 9M 2025 | 9M 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenue | 2,026.6 | 1,892.6 | 459.7 | 456.2 | 1,415.0 | 1,385.1 | 10-K page:64; Q3 10-Q page:2 |
| Gross profit (calculated: revenue less the three cost-of-revenue lines) | 1,062.3 | 1,023.9 | 244.3 | 247.3 | 760.9 | 749.4 | Same pages; the filing prints no gross profit |
| Selling, general and administrative | 717.9 | 621.6 | 144.2 | 139.2 | 480.6 | 401.3 | 10-K page:65; Q3 10-Q page:2 |
| Restructuring charges | 76.9 | 58.7 | 1.8 | 1.5 | 17.0 | 10.0 | Same pages |
| Interest expense, net (income statement) | 110.1 | 101.5 | 26.1 | 26.0 | 75.3 | 80.6 | Same pages |
| Total interest expense including allocated financing interest | 173.7 | 149.2 | 37.3 | 34.5 | 112.7 | 107.6 | 10-K page:84; Q3 10-Q page:10 |
| Income (loss) before taxes, continuing | (52.3) | 192.5 | 68.1 | 70.1 | 154.1 | 216.1 | 10-K page:65; Q3 10-Q page:2 |
| Net income (loss) | (203.6) | 144.7 | 52.0 | 52.7 | 117.4 | 160.7 | Same pages; FY2024 includes a discontinued-operations loss of 306.1 |
| Total adjusted segment EBIT | 550.5 | 577.5 | 133.7 | 146.9 | 422.7 | 442.3 | 10-K page:84; Q3 10-Q page:10 |
| Corporate expenses | 152.5 | 116.2 | 26.4 | 33.0 | 93.4 | 81.9 | Same pages |
| Adjusted EBIT (company basis) | Not supplied: not built for FY2024 | 461.3 | 107.3 | 113.9 | 329.3 | 360.3 | FY2025 calculated; others printed in Q3 release page:9 |
| Depreciation and amortization | 114.5 | 111.6 | 27.4 | 22.7 | 84.5 | 72.1 | 10-K page:84; Q3 release page:9; Q3 10-Q page:3 |
| Adjusted EBITDA (company basis) | Not supplied: not built for FY2024 | 572.9 | 134.8 | 136.7 | 413.8 | 432.4 | FY2025 calculated; others printed in Q3 release page:9. 2026 adds back terminated-plan pension expense; 2025 does not |
| Pension expense of plans to be terminated, added back | Not applicable before 2026 | Not applicable before 2026 | 0.0 | 7.1 | 0.0 | 23.1 | Q3 10-Q page:10 (2025 shows a dash) |
| Net cash from operating activities | 229.2 | 383.3 | 66.8 | 151.1 | 161.6 | 348.2 | 10-K page:67; Q3 10-Q page:4; Q3 release page:9 |
| Finance receivables, cash flow effect included above | 60.3 | 107.2 | 23.5 | 15.8 | 94.7 | 87.5 | 10-K page:67; Q3 10-Q page:4; Q3 values are nine months less six months |
| Capital expenditures | (72.4) | (66.3) | (15.8) | (10.7) | (46.0) | (45.0) | Same pages |
| Restructuring payments added back in free cash flow | 86.0 | 41.3 | 9.3 | 6.7 | 30.8 | 35.6 | 10-K page:66; Q3 release page:9 |
| Adjusted free cash flow | Not supplied: not built for FY2024 | 358.3 | 60.4 | 147.1 | 146.4 | 338.8 | FY2025 calculated on the release method; others printed in Q3 release page:9 |
| Dividends paid | (36.0) | (51.1) | (13.3) | (13.7) | (36.9) | (40.6) | 10-K page:67; Q3 10-Q pages 4 and 24-25 |
| Common stock repurchases | 0.0 | (378.4) | (161.5) | (17.3) | (251.8) | (205.7) | 10-K page:67; Q3 10-Q page:4, pages 24-25 |
| Cash interest paid | 167.9 | 142.1 | 47.9 | 41.8 | 119.9 | 114.0 | 10-K page:96; Q3 10-Q page:26; Q3 values are nine months less six months (Q2 10-Q page:26) |
| Adjusted EBITDA / total interest expense including financing interest (calculated, x) | Not supplied | 3.84 | 3.61 | 3.97 | 3.67 | 4.02 | Company-basis Adjusted EBITDA over total interest line above |

### Balance sheet, debt and leverage inputs

| Item (US$m) | 2024-12-31 | 2025-12-31 | 2026-03-31 | 2026-06-30 | 2026-09-30 | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 469.7 | 284.9 | 302.9 | 266.8 | 268.5 | 10-K page:65; Q1 10-Q page:2; Q2 10-Q page:3; Q3 10-Q page:3 |
| Short-term investments | 16.4 | 12.2 | 11.1 | 11.9 | 12.7 | Same pages |
| Debt principal | 1,955.5 | 2,026.2 | 2,172.7 | 2,066.8 | 1,918.4 | 10-K page:98; Q1 10-Q page:18; Q2 10-Q page:19; Q3 10-Q page:19 |
| Unamortized costs, net | 35.8 | 33.2 | 34.5 | 32.9 | 31.0 | Same pages |
| Total debt (carrying) | 1,919.7 | 1,993.0 | 2,138.2 | 2,033.9 | 1,887.4 | Same pages |
| Of which current portion | 53.3 | 17.2 | 364.0 | 23.1 | 24.7 | Same pages |
| Net debt (principal less cash and equivalents, calculated) | 1,485.8 | 1,741.3 | 1,869.8 | 1,800.0 | 1,649.9 | Calculated |
| Net finance receivables, short and long term | 1,145.9 | 1,101.6 | 1,052.7 | 1,019.3 | 995.1 | 10-K pages 65-66; Q1 10-Q pages 2-3; Q2 10-Q page:3; Q3 10-Q page:3 and page:11 |
| Customer deposits at Pitney Bowes Bank, current and noncurrent | 703.8 | 653.6 | 645.3 | 617.5 | 647.9 | 10-K page:66; Q1 10-Q page:3; Q2 10-Q page:3; Q3 10-Q page:3 |
| Operating lease liabilities, current and noncurrent | 127.7 | 128.2 | 130.0 | 123.8 | 117.3 | Same pages |
| Total assets | 3,397.5 | 3,169.0 | 3,147.3 | 3,019.6 | 2,992.3 | Same pages |
| Total liabilities | 3,975.9 | 3,971.3 | 4,040.9 | 3,882.9 | 3,829.0 | Same pages |
| Stockholders' deficit | (578.4) | (802.4) | (893.6) | (863.3) | (836.7) | Same pages |

### Debt schedule at 2026-09-30

| Instrument | Principal 2026-09-30 | Principal 2025-12-31 | Terms as printed | Ranking and support |
| --- | --- | --- | --- | --- |
| 6.875% notes due March 2027 | 0.0 | 346.7 | Repaid in Q2 2026 from the additional term loan (Q3 10-Q page:20) | Senior Notes under a 2021 indenture with guarantors (10-K page:56); secured status not stated in the pages read |
| 7.25% notes due March 2029 | 476.0 | 326.0 | Further 150.0 issued in Q1 2026 with identical terms; First Supplemental Indenture dated March 2, 2026 (Q3 10-Q pages 20 and 39) | Senior Notes with guarantors (10-K page:56); secured status not stated |
| 1.50% convertible notes due August 2030 | 230.0 | 230.0 | Conversion rate 70.4648 shares per 1,000 principal, or 14.19 per share; not redeemable before August 21, 2028; capped call with cap price 22.26 (Q3 10-Q pages 21-22) | Senior unsecured; guaranteed jointly and severally by wholly owned U.S. subsidiaries that guarantee the credit agreement, existing senior notes or other capital market debt above 150 (page:22) |
| Term loan, SOFR plus 2.10%, due May 2031 (March 2031 in Q2; March 2028 before the Q2 extension) | 294.5 | 154.0 | Additional 150.0 borrowed in Q2 2026 and maturity extended (Q3 10-Q page:20) | Credit agreement borrowings are secured by assets of the Company (page:20); guarantors not named |
| Term loan, SOFR plus 3.00%, due March 2032 | 584.0 | 588.6 | Margin reduced by 0.75% in Q3 2026; the Q3 release calls it a 585 million Term Loan B (Q3 release page:1) | Same security statement |
| 5.25% notes due January 2037 | 25.4 | 31.7 | Reduced by the Q3 tender and earlier purchases | Medium-term note under the 2005 Senior Debt Indenture (10-K page:56) |
| 6.70% notes due March 2043 | 308.5 | 349.3 | Reduced by the Q3 tender; listed as PBI.PRB (Q3 10-Q page:1) | Officer's Certificate and specimen notes of March 2013 (10-K page:56) |
| Revolving credit facility, 450.0 commitment, matures May 2031 (March 2031 in Q2 10-Q) | 0.0 drawn | 0.0 drawn | Increased from 400.0 in Q1 2026; 176.7 borrowed and repaid in 2026, of which 80 in Q3; capacity 427.0; commitment amount and letters of credit not itemized (Q3 10-Q page:20; cash flow page:4) | Secured by assets of the Company |
| Total principal | 1,918.4 | 2,026.2 | Unamortized costs 31.0 and 33.2; carrying 1,887.4 and 1,993.0; fair value of debt 1,912.0 and 1,954.3 (Q3 10-Q page:18) | Not applicable: total row |

### Claims outside the debt figure

| Item | Amount | Inside or outside total debt principal | Locator and note |
| --- | --- | --- | --- |
| Operating lease liabilities | 29.7 current and 87.6 noncurrent, total 117.3 at 2026-09-30 | Outside | Q3 10-Q page:3 |
| Finance lease liabilities | 36.9 at 2025-12-31 (10.6 within accounts payable and accrued liabilities, 26.4 within other noncurrent liabilities); not printed at 2026-09-30 | Outside the debt table | 10-K page:116; Q3 10-Q page:26 prints 9.1 of capital assets obtained under capital lease obligations in nine months 2026 |
| Customer deposits at Pitney Bowes Bank | 576.9 current and 71.0 noncurrent, total 647.9 | Outside | Q3 10-Q page:3; funds the financing business |
| Pension plans, funded status at 2025-12-31 | United States (50.2) and foreign (40.3); no Q3 2026 funded status is printed | Outside | 10-K page:102 |
| Postretirement medical, 2025-12-31 | (76.2) funded status; retiree medical payments of 71 over the years in the cash requirements table | Outside | 10-K pages 110 and 44 |
| Pension lump sums and buy-out | Lump sums of 66 million paid from plan assets in October 2026; intent to buy out the U.S. plan before year end | Outside; subsequent event | Q3 10-Q page:23 |
| Purchase obligations | 95 at 2025-12-31, all due in 2026 | Outside | 10-K page:44 |
| Letters of credit | Approximately 27 at 2025-12-31; about 23 implied at 2026-09-30, not printed | Reduce revolver capacity | 10-K page:45; Q3 10-Q page:20 |
| Vendor litigation (former ecommerce vendor) | More than 100 sought in lease payments, interest, fees and damages; no accrual amount printed | Outside | Q3 10-Q page:24 |
| Ecommerce Restructuring and DIP Facility | Remaining DIP balance fully reserved; the Company remains exposed to economic risks and continued costs of the ecommerce debtors | Outside | 10-K page:85 |
| Restructuring reserve | 5.8 at 2026-09-30 | Outside | Q3 10-Q page:18 |

### Definitions and covenant evidence

| Term | Definition as printed | Difference from the metric calculated here |
| --- | --- | --- |
| Adjusted EBIT and Adjusted EBITDA | Exclude restructuring, foreign currency gains and losses on intercompany loans, ecommerce restructuring costs, gains and losses on debt redemptions and other unusual items, and for 2026 also pension expense of the U.S. and Canada plans being terminated (Q3 release page:3) | Used on the release basis; FY2025 is calculated, not printed |
| Adjusted free cash flow | Cash from operations adjusted for capital expenditures, restructuring payments and other special items; renamed from Free Cash Flow in Q2 2026 with no change of method (Q3 release pages 3-4) | FY2025 is calculated with capital expenditures and restructuring payments only |
| Interest coverage covenant | Consolidated Interest Coverage Ratio of not less than 2.00 to 1.00, tested quarterly (Q3 10-Q page:20) | Defined in the credit agreement, not supplied; the 4.34x above is not that ratio |
| Secured leverage covenant | Consolidated Secured Net Leverage Ratio of no greater than 3.00 to 1.00 | Not reproduced; no secured debt split of the notes is given |
| Total leverage covenant | Consolidated Total Net Leverage Ratio of no greater than 4.75 to 1.00 for each quarter in 2026, 4.50 in 2027, 4.25 in 2028 and 4.00 thereafter | Not reproduced; 2.79x above is on a different definition |
| Springing maturity | If before December 14, 2028 the 2029 notes are not redeemed in full and liquidity is below the redemption amount plus 100 million, the term loan and revolver borrowings become due; a parallel test applies before May 16, 2030 for the convertible (Q3 10-Q page:20) | Liquidity is a defined term not supplied; compared with printed inputs only, 476.0 plus 100 is 576.0 and 230.0 plus 100 is 330.0 against cash plus capacity of 695.5; this is not a test result |

Covenant compliance is reported only in words: "At September 30, 2026, we were in compliance with these financial covenants." (Q3 10-Q page:20). The reported ratios, the credit-agreement EBITDA and net debt definitions and the headroom are Not calculable from the pack.

### Expense block reconciliation

The income statement is by function and prints no gross profit. The block from gross profit (calculated) to income before taxes reconciles in thousands for each period shown.

| Line (thousands) | FY2025 | 9M 2026 | Q3 2026 |
| --- | --- | --- | --- |
| Gross profit (calculated) | 1,023,862 | 749,367 | 247,308 |
| Selling, general and administrative | (621,567) | (401,324) | (139,201) |
| Research and development | (15,278) | (10,560) | (3,383) |
| Restructuring charges | (58,660) | (9,978) | (1,529) |
| Interest expense, net | (101,460) | (80,556) | (25,984) |
| Other components of net pension and postretirement cost | (7,543) | (33,564) | (10,274) |
| Other (expense) income | (26,830) | 2,672 | 3,155 |
| Income before taxes, as printed | 192,524 | 216,057 | 70,092 |

### Interpretation: evidence, mechanism, implication

- **Leverage is lower and moving down through debt paydown.** Evidence: debt principal fell from 2,026.2 to 1,918.4 while calculated LTM Adjusted EBITDA moved from 572.9 to 591.5. Mechanism: the 2026 refinancing replaced the 346.7 notes due March 2027 with an extra 150.0 of 7.25% notes due March 2029 and 150.0 of term loan, and a Q3 tender retired 46.5 of 2037 and 2043 notes at a discount (Calculations). Implication: gross leverage of 3.24x is below the 3.54x at FY2025, but the earnings contribution is smaller than it looks, as the next point shows.
- **Adjusted EBITDA growth is pension-basis driven.** Evidence: nine-month Adjusted EBITDA rose from 413.8 to 432.4, an increase of 18.6, and 2026 adds back 23.1 of terminated-plan pension expense that 2025 does not ("Prior periods were not recast", Q3 10-Q page:9). Mechanism: the add-back is larger than the increase; excluding it gives 409.3 against 413.8, and lower depreciation and amortization of 72.1 against 84.5 lifts Adjusted EBIT more than Adjusted EBITDA. Implication: on the 2025 definition LTM Adjusted EBITDA is 568.3 and leverage is 3.38x gross and 2.90x net. This is a sensitivity that assumes the 2025 base carried its pension cost, as the filings imply.
- **Segment mix is moving.** Evidence: nine-month adjusted segment EBIT was 351.2 in SendTech Solutions against 299.3 and 91.0 in Presort Services against 123.3 (Q3 10-Q page:10). Mechanism: SendTech cost reductions and mix offset revenue erosion, while Presort carries higher transportation and fuel costs, with a 15 million fuel and freight increase in the nine months (Q3 10-Q page:32). Implication: earnings rest increasingly on the SendTech base, whose revenue is in secular decline.
- **Cash flow is flattered by working capital and the finance book.** Evidence: nine-month cash from operations was 348.2 against 161.6, and the finance receivables line contributed 87.5 (Q3 10-Q page:4). Mechanism: net finance receivables fell from 1,101.6 to 995.1 as the leasing portfolio runs off ("a decline in our leasing portfolio", Q3 10-Q page:30), and management cites prepayments from new Presort customers after a competitor exited (Q3 release page:2). Implication: part of the cash generation is liquidation of an asset base, and prepayments may reverse; the guidance of 380 to 420 for the year implies fourth-quarter adjusted free cash flow of 41.2 to 81.2 against a derived 211.9 a year earlier.
- **Shareholder returns compete with debt reduction.** Evidence: nine-month buybacks of 205.7 and dividends of 40.6 total 246.3, against debt reduction of 107.8. Mechanism: the repurchase authorization was raised to 750 million in February 2026 with 165.9 remaining at September 30, 2026 (Q3 10-Q pages 38-39). Implication: further buybacks reduce the cash available to retire the 2029 notes; the stockholders' deficit is (836.7).
- **Funding of the financing business.** Evidence: net finance receivables of 995.1 and Bank customer deposits of 647.9 sit beside debt principal of 1,918.4 (Q3 10-Q page:3). Mechanism: allocated financing interest of 27.1 for nine months moves cost from interest expense, net into cost of financing (Q3 10-Q page:33). Implication: consolidated leverage mixes industrial and financing debt; no separate financing-segment debt is supplied.

## Calculations

All amounts are in thousands of US dollars as the filings print them unless a row says millions. Inputs are cited; results are calculated, not printed, unless stated.

### Adjusted EBITDA, FY2025 and last twelve months

Method: the releases define Adjusted EBIT as total adjusted segment EBIT less corporate expenses and Adjusted EBITDA as Adjusted EBIT plus depreciation and amortization (Q3 release pages 8-9). This ties for the nine months of 2026 (442,288 less 81,942 is 360,346; plus 72,062 is 432,408) and of 2025 (422,686 less 93,369 is 329,317; plus 84,503 is 413,820), so the same method is applied to FY2025 from the 10-K.

| Step | Inputs (locator) | Result |
| --- | --- | --- |
| FY2025 Adjusted EBIT | Total adjusted segment EBIT 577,466 less corporate expenses 116,173 (10-K page:84) | 461,293 |
| FY2025 Adjusted EBITDA | 461,293 plus total depreciation and amortization 111,575 (10-K page:84) | 572,868 |
| Check: FY2025 reconciles to pre-tax income | 577,466 - 116,173 - 149,156 - 58,392 - 268 - 14,072 - 21,944 - 12,758 - 12,179 (10-K page:84) | 192,524, equals income from continuing operations before taxes (10-K page:65) |
| Implied Q4 2025 Adjusted EBITDA | 572,868 less nine months 2025 413,820 | 159,048 (derived; no Q4 release is in the pack) |
| LTM Q1 2026 | 572,868 plus Q1 2026 156,018 less Q1 2025 148,013 (Q1 release page:7) | 580,873 |
| LTM Q2 2026 | 572,868 plus six months 2026 295,758 less six months 2025 279,068 (Q2 release page:9) | 589,558 |
| LTM Q3 2026 | 572,868 plus nine months 2026 432,408 less nine months 2025 413,820 (Q3 release page:9) | 591,456 |
| Quarterly tie, 2026 | 156,018 + 139,740 + 136,650 (Q1 release page:7, Q2 release page:9, Q3 release page:9) | 432,408, equals the nine-month figure |
| Quarterly tie, 2025 | 148,013 + 131,055 + 134,753 | 413,821, differs from 413,820 by 1 (rounding in the releases) |
| LTM Q3 2026 on the 2025 definition | 591,456 less 2026 pension add-backs 7,554 + 8,422 + 7,149 = 23,125 (Q1 release page:7, Q2 release page:9, Q3 release page:9) | 568,331 |
| Nine months 2026 on the 2025 definition | 432,408 less 23,125 | 409,283, against 413,820 in nine months 2025 |

### Leverage

Total debt / EBITDA is debt principal over Adjusted EBITDA; net debt is principal less cash and cash equivalents (short-term investments excluded).

| Period | Debt principal | Cash | Net debt | EBITDA | Total / EBITDA | Net / EBITDA |
| --- | --- | --- | --- | --- | --- | --- |
| FY2025 | 2,026,212 | 284,887 | 1,741,325 | 572,868 | 3.54x | 3.04x |
| LTM Q1 2026 | 2,172,675 | 302,876 | 1,869,799 | 580,873 | 3.74x | 3.22x |
| LTM Q2 2026 | 2,066,839 | 266,833 | 1,800,006 | 589,558 | 3.51x | 3.05x |
| LTM Q3 2026 | 1,918,434 | 268,514 | 1,649,920 | 591,456 | 3.24x | 2.79x |
| LTM Q3 2026, 2025 definition | 1,918,434 | 268,514 | 1,649,920 | 568,331 | 3.38x | 2.90x |

Carrying-value basis at 2026-09-30: 1,887,421 over 591,456 is 3.19x. Debt principal less net finance receivables of 995,101 is 923,333; this is an analyst-defined figure, not a company measure.

### Interest cover

| Period | EBITDA | Cash interest paid | Result |
| --- | --- | --- | --- |
| FY2025 | 572,868 | 142,107 (10-K page:96) | 4.03x |
| LTM Q1 2026 | 580,873 | 142,107 + 46,021 - 49,273 = 138,855 (Q1 10-Q page:24) | 4.18x |
| LTM Q2 2026 | 589,558 | 142,107 + 72,188 - 71,923 = 142,372 (Q2 10-Q page:26) | 4.14x |
| LTM Q3 2026 | 591,456 | 142,107 + 114,025 - 119,863 = 136,269 (Q3 10-Q page:26) | 4.34x |
| LTM Q3 2026, 2025 definition | 568,331 | 136,269 | 4.17x |

Total interest expense including financing interest: FY2025 149,156 (10-K page:84); LTM Q3 2026 equals 149,156 + 107,633 - 112,671, giving 144,118 (Q3 10-Q page:33); 572,868 over 149,156 is 3.84x and 591,456 over 144,118 is 4.10x. Q3 2026 alone: 136,650 over 34,450 is 3.97x; nine months 2026: 432,408 over 107,633 is 4.02x; Q3 2025: 134,753 over 37,287 is 3.61x; nine months 2025: 413,820 over 112,671 is 3.67x. Discrete cash interest: Q3 2026 is 114,025 less 72,188, or 41,837; Q3 2025 is 119,863 less 71,923, or 47,940.

### Liquidity

| Date | Cash | Undrawn committed | Total | Basis |
| --- | --- | --- | --- | --- |
| 2025-12-31 | 284,887 | 400,000 less about 27,000 letters of credit = 373,000 | 657,887 | Capacity not printed; calculated |
| 2026-06-30 | 266,833 | 330,000 | 596,833 | Capacity printed; 450,000 less 96,700 drawn less 330,000 leaves 23,300 unexplained |
| 2026-09-30 | 268,514 | 427,000 | 695,514 | Capacity printed; 450,000 less 427,000 leaves 23,000 unexplained |

Springing-test arithmetic on printed inputs only: 476,000 + 100,000 = 576,000 and 230,000 + 100,000 = 330,000, against 695,514. These are not test results because the liquidity definition is not supplied.

### Debt principal roll-forward, nine months 2026

| Step | Amount | Locator |
| --- | --- | --- |
| Opening principal 2025-12-31 | 2,026,212 | Q3 10-Q page:19 |
| Add: 7.25% notes issued (Q1) | 150,000 | Q3 10-Q page:20 |
| Add: additional term loan (Q2) | 150,000 | Q3 10-Q page:20; cash flow proceeds of issuance 300,000 (page:4) |
| Less: 6.875% notes due March 2027 repaid | (346,700) | Q3 10-Q page:19 |
| Less: term loan amortization, 154,000 + 150,000 - 294,450 | (9,550) | Q3 10-Q page:19 |
| Less: term loan due 2032 amortization, 588,567 - 584,029 | (4,538) | Q3 10-Q page:19 |
| Less: 2037 notes, 31,666 - 25,441 | (6,225) | Q3 10-Q page:19 |
| Less: 2043 notes, 349,279 - 308,514 | (40,765) | Q3 10-Q page:19 |
| Closing principal 2026-09-30 | 1,918,434 | Equals the printed principal. Ties |
| Observed principal reductions | 407,778 | 346,700 + 9,550 + 4,538 + 6,225 + 40,765 |
| Cash principal payments of debt | 402,032 | Q3 10-Q page:4 |
| Implied discount to par on repurchased notes | 5,746 | 407,778 less 402,032; inferred, not stated |
| Debt reduction in nine months | 107,778 | 2,026,212 less 1,918,434; Q3 release page:1 prints 108 million |
| Q3 2026 tender, 2037 and 2043 notes | 46,467 | (31,143 - 25,441) + (349,279 - 308,514), using the Q2 10-Q balances (page:19); release and 10-Q say 46 million |

### Other tie-outs

- Debt principal at 2026-09-30: 476,000 + 230,000 + 294,450 + 584,029 + 25,441 + 308,514 = 1,918,434; less unamortized costs 31,013 is 1,887,421, equal to 24,730 + 1,862,691 (Q3 10-Q page:3).
- Adjusted free cash flow, nine months 2026: 348,212 - 45,041 + 35,592 = 338,763; Q3 2026: 151,140 - 10,710 + 6,694 = 147,124 (Q3 release page:9). FY2025 on the same method: 383,257 - 66,278 + 41,338 = 358,317 (10-K pages 66-67); implied Q4 2025: 358,317 - 146,373 = 211,944.
- Guidance of 380 to 420 million for adjusted free cash flow (Q3 release page:3) less nine months of 338,763 implies 41.2 to 81.2 million for Q4 2026; this is an implication, not guidance.
- Cash returned to shareholders: nine months 2026 is 205,725 + 40,599 = 246,324; FY2025 is 378,361 + 51,059 = 429,420.
- Finance receivables: 461,910 + 533,191 = 995,101 equals the Note 6 total (Q3 10-Q page:11). Customer deposits: 576,949 + 71,000 = 647,949. Operating lease liabilities: 29,725 + 87,595 = 117,320.
- Pension and retiree medical at 2025-12-31: 50,225 + 40,341 = 90,566; with postretirement medical of 76,199 the total unfunded is 166,765 (10-K pages 102 and 110).
- Allocated financing interest, FY2025: 149,156 (10-K page:84) less interest expense, net 101,460 (10-K page:65) is 47,696; the 10-K confirms that a portion of total interest is allocated to cost of financing and other (page:34) but prints no amount, so the split is inferred.
- Segment concentration: SendTech adjusted segment EBIT of 351,243 is 79 percent of the total of 442,288 for nine months 2026.

## Gaps

| # | Gap or limitation | Affected output | Locator and detail | Action |
| --- | --- | --- | --- | --- |
| 1 | Credit agreement and amendments are not supplied; covenant ratios, headroom, definitions of liquidity, EBITDA and secured net debt, and the springing tests cannot be computed. A Second Amendment is implied by the numbering but is named in no source. | Covenant view, springing-test comparison | Q3 10-Q pages 20 and 39; Q2 10-Q page:40; 10-K page:59 | Write Not calculable; obtain the Credit Agreement and all amendments |
| 2 | FY2025 Adjusted EBITDA is not printed in the 10-K or in any release in the pack; it is calculated. The Q4 2025 implied figure of 159,048 is derived, not reported. | FY2025 and all LTM ratios | 10-K page:84; Q3 release page:9 | Label as calculated; confirm against the Q4 2025 release, which is not in the pack |
| 3 | Pension basis: 2026 adds back 23,125 of terminated-plan pension expense for nine months and prior periods were not recast; 2025 segment results were also revised for a cross-border contract from April 1, 2025. | Year-over-year Adjusted EBITDA and EBIT, leverage trend | Q3 10-Q page:9; Q1 10-Q page:5 | Show both bases; the sensitivity assumes the 2025 base carried the equivalent cost |
| 4 | Maturity labels differ between filings: the term loan and revolver are March 2031 in the Q2 10-Q and May 2031 in the Q3 10-Q; the term loan was March 2028 earlier in 2026. | Maturity chart, 2031 row | Q2 10-Q pages 19-20; Q3 10-Q pages 19-20 | Use May 2031 as latest filed; the Fifth Amendment of September 29, 2026 is not supplied |
| 5 | Revolver capacity at 2025-12-31 and 2026-03-31 is not printed, and letters of credit are printed only at 2025-12-31 (about 27). The 23 gap at Q2 and Q3 is not itemized. | Liquidity chart rows | 10-K page:45; Q2 10-Q page:20; Q3 10-Q page:20 | 2025-12-31 is calculated; 2026-03-31 is Not supplied |
| 6 | Scheduled amortization by year of the two term loans after 2026-09-30 is not printed; only the current portion of 24,730 is. The 10-K maturity table at 2025-12-31 pre-dates the refinancing. | Maturity chart rows for Q4 2026 to 2028 | Q3 10-Q pages 3 and 19; 10-K page:101 | Not supplied; request the amortization schedule |
| 7 | FY2024 comparable EBITDA, FY2024 free cash flow and FY2024 restructuring payments are not built: no FY2024 release is in the pack and 2024 includes Other operations and discontinued ecommerce items. | FY2024 columns and chart rows | 10-K pages 65-67 and 84 | Not supplied |
| 8 | Guarantors, collateral and the secured or unsecured status of the 2029, 2037 and 2043 notes are not stated in the pages read; indentures are not supplied. | Debt schedule ranking column, secured leverage | Q3 10-Q pages 20 and 22; 10-K pages 56-57 | Obtain the indentures and guarantor list |
| 9 | Pension funded status and finance lease liabilities are printed at 2025-12-31 only; none is printed at 2026-09-30. Pension lump sums of 66 million were paid in October 2026. | Claims outside debt | 10-K pages 102, 110, 116; Q3 10-Q page:23 | Show as of 2025-12-31 and flag the subsequent event |
| 10 | The Form 10-K/A cited by the 10-Qs is not in the pack; FY2025 figures here come from the Form 10-K and agree with the 2025-12-31 comparatives in the 2026 filings on the lines tested. | FY2025 column | Q3 10-Q page:5 | Label FY2025 as per the Form 10-K |
| 11 | The 5 million tender gain in the Q3 10-Q text versus the (3,155) table amount remains unreconciled in the sources; an implied discount of 5,746 is inferred. | Debt activity narrative | Q3 10-Q pages 20 and 26 | Use the table for statement lines |
| 12 | Management items (guidance, prepayment benefit, fuel-price attribution) are attributed statements, not filed facts. | Interpretation only | Q3 release pages 2-3; Q3 10-Q page:34 | Attribute to management |
| 13 | Consolidated leverage includes the financing business and the Pitney Bowes Bank; no separate financing or Bank statements are supplied. | Leverage interpretation | Q3 10-Q pages 3 and 33 | State on consolidated basis only |

## Next module

Run the business and transaction context module (CP-1A) next. It should carry forward from this handoff: the 2029 notes and 2030 convertible as the first final maturities, with the springing provisions that tie the term loan and revolver to them; the Q3 2026 repricing of the 2032 term loan by 0.75%; the Fifth Amendment of September 29, 2026 and its unsupplied terms; the ecommerce restructuring exposure and the vendor litigation claim of more than 100 million; the pension lump sums and intended buy-out; and the shift of earnings toward SendTech Solutions as Presort Services margins fall. The credit synthesis (CP-2) must use the leverage rows on the company basis with the 2025-definition sensitivity beside them, label FY2025 Adjusted EBITDA as calculated, treat covenant headroom and the springing liquidity tests as Not calculable, and keep management guidance attributed.
