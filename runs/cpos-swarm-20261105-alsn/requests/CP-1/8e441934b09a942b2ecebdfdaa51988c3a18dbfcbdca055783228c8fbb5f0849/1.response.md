## Request

Issuer: Allison Transmission Holdings Inc (issuer id alsn, NYSE: ALSN), as of 2026-11-05, evidence cutoff 2026-11-05. Pathway credit_snapshot. Reporting currency USD; all amounts are US$ millions as printed in the filings unless a ratio (x) or percentage is stated. Current period q3-2026 (quarter and nine months ended 2026-09-30); prior period fy-2025 (year ended 2025-12-31).

Task: build the financial base for the credit snapshot from the pinned filings and earnings releases: reported statements, debt by instrument, liquidity, covenant, cash flow, claims outside debt, the latest quarter, and the chart data for leverage, interest cover, liquidity and debt maturities. Reported facts and calculations are kept apart; every calculation is shown in `## Calculations`.

Perimeter: the reporting entity is Allison Transmission Holdings, Inc. (the registrant, consolidated). Allison Transmission, Inc. (ATI), its wholly-owned subsidiary, is the issuer of the senior notes and the borrower under the credit facility (S4 page:19, S1 page:102). There is no combined filing with a separate parent, so the consolidated statements are the issuer's own statements. The Dana off-highway business was acquired on 2026-01-01 and is inside all 2026 periods and outside all 2025 periods (S4 page:5); this is the most important period label in the document.

Locator convention: S1 to S7 are the sources listed below; `page:N` is the chunk number of the extracted text, not the printed page. Quotes are exact substrings of the page text with line breaks collapsed.

## Sources

### Issuer sources relied on

| Id | Exact name | sha256 | Use in this handoff |
| --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_alsn-20251231.htm.jsonl | 4759ff666c33cf9b4aa9fc9af406b5ff948ca8c7e8b83ef1d1b8c3371ee474c1 | Audited FY2025 statements, FY2025 debt note, FY2025 Adjusted EBITDA bridge, cash interest, pension status |
| S2 | 10-Q_2026-03-31_alsn-20260331.htm.jsonl | be0a328aec24e49cdf0300569cba1bccab7cce3c7f95d5658c5db76418cb7b3d | Q1 2026 balances, debt table, revolver, covenant ratio, Q1 2025 and Q1 2026 Adjusted EBITDA |
| S3 | 10-Q_2026-06-30_alsn-20260630.htm.jsonl | 0d35855e179d244457d2146b580b35b12b14abea216ea0bdfab3dfa942713609 | Q2 2026 balances, debt table, revolver, covenant ratio, six-month Adjusted EBITDA and interest paid |
| S4 | 10-Q_2026-09-30_alsn-20260930.htm.jsonl | 45fe422f6a742d85a38f1278f190cb497541b353ed938208d565068e9ab989b0 | Primary source: Q3 2026 statements, debt note, liquidity, covenant, non-GAAP reconciliations, leases |
| S5 | EX-99.1_2026-05-04_d138525dex991.htm.jsonl | fe207b266e861065ca33402f15b822e8bf63e3f1f6c76c7ba33719a7889867e5 | Q1 2026 release: management debt and net debt figures |
| S6 | EX-99.1_2026-08-03_d95413dex991.htm.jsonl | 351a085e364488314b64d2b881181e5b5b95879fe010b71d75af6ac7e45fdd04 | Q2 2026 release: management debt and net debt figures, guidance |
| S7 | EX-99.1_2026-11-02_d187329dex991.htm.jsonl | b8087f0341293bcafb0ca28c8fc71ee181a5c666b45fe74a0ca9cfe109b0ba65 | Q3 2026 release: quarterly cash interest, segment Adjusted EBITDA, debt and net debt, guidance |

Run settings, not issuer evidence: context file 1411207-allison-transmission-holdings-inc-alsn.json, sha256 f65312705cd8bb204fde9755509326ba975099b166b8d246c949fcd0ea955b5a.

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 944a1fdb32b0e105bdb98bcce7fe9920a9ab8a1870c238bf911cb1860242755e |

The source-readiness handoff rates the source set READY_WITH_LIMITATIONS for this module. This answer carries its limitations forward: no executed legal documents, no pro forma or pre-acquisition financials for the acquired business, no year-by-year maturity schedule after the January 2026 amendment, and an unresolved guarantor roster. It also carries the debt-measure point (note total versus release total) and the purchase price difference, which the earlier handoff recorded and this answer uses as stated there.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Leverage rose sharply after the January 2026 acquisition and has since fallen: 2.82x total and 2.47x net on a reported trailing basis at 30 September 2026. Liquidity is large and the only maintenance covenant has very wide headroom. | Medium | Trailing earnings include the acquired business for only three of four quarters and no pro forma figure exists, so the ratios are overstated relative to a full-year view. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt rose from 2,909 to 4,037 and cash fell from 1,495 to 497 between year-end 2025 and 30 September 2026, funding the acquisition. | Net debt more than doubled, so the credit now carries acquisition leverage that deleveraging must work down. | High |
| Cash interest paid covered by trailing Adjusted EBITDA is 7.73x at the third quarter of 2026 versus 9.42x for FY2025. | Coverage is lower but still comfortable; the full cost of the new debt may not yet be in the trailing figure. | Medium |
| Liquidity is 497 of cash plus 996 undrawn on the revolver, and nothing on the revolver is drawn. | Near-term refinancing pressure is limited; the first maturity is 300 of notes due October 2027. | High |
| The reported first lien net leverage ratio is 0.84x against a 5.50x maximum, and it can be reproduced from the filings. | Maintenance covenant risk is remote; the unsecured notes sit behind 1,699 of secured term loans. | Medium |
| Adjusted EBITDA includes 200 of add-backs for the nine months, 17.2% of the reported figure, many tied to the acquisition. | Adjusted earnings sit well above plain accounting earnings, so the definition must be used with care. | Medium |

### Financial base view

On the filed numbers the credit is a lightly levered industrial that took on acquisition debt in the first quarter of 2026 and has been paying it down. Total debt at 2026-09-30 was 4,037 against 2,909 at 2025-12-31; cash fell from 1,495 to 497; net debt on the same debt measure therefore rose from 1,414 to 3,540. On trailing reported Adjusted EBITDA of 1,431 that is 2.82x gross and 2.47x net, down from a first-quarter peak of 3.59x and 3.33x and above the 2.57x and 1.25x at FY2025. Cash interest paid is covered 7.73x on a trailing basis. Liquidity at the quarter end is 1,493 (cash 497 plus 996 available under the 1,000 revolving facility, net of 4 of letters of credit), with no loans drawn on the revolver. The only financial maintenance covenant described is a maximum first lien net leverage ratio of 5.50x, reported at 0.84x, and the arithmetic of the filings reproduces that figure from term loans, cash and trailing Adjusted EBITDA. The weaknesses are perimeter and definition: trailing earnings contain the acquired business for only the 2026 quarters, so the leverage ratios overstate leverage against a full combined year and the interest cover may be flattered because only part of a year of the new interest cost is in the trailing cash figure; Adjusted EBITDA is a company and credit-agreement measure with material add-backs; the legal documents are not supplied; and purchase accounting is preliminary. Confidence is Medium overall and High for the reported balances.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (2025-12-31) | 2.57 | 1.25 | x | Total debt 2,909 (S1 page:101) less cash 1,495 (S1 page:81) for net; EBITDA is company-defined Adjusted EBITDA 1,130 for FY2025 (S1 page:117); acquired business excluded |
| Q1 2026 (2026-03-31) | 3.59 | 3.33 | x | Total debt 4,295 including 150 drawn on the revolver (S2 page:15); cash 311; trailing Adjusted EBITDA 1,196 built from FY2025, Q1 2025 and Q1 2026 (calculation C1); acquired business in one quarter only, so ratios are overstated against a pro forma view |
| Q2 2026 (2026-06-30) | 3.22 | 2.91 | x | Total debt 4,140 (S3 page:17); cash 399; trailing Adjusted EBITDA 1,287 (calculation C1); acquired business in two quarters only; ratios overstated against a pro forma view |
| Q3 2026 (2026-09-30) | 2.82 | 2.47 | x | Total debt 4,037 including 38 of finance leases, before 25 of deferred financing costs (S4 page:19); cash 497 (S4 page:2); trailing Adjusted EBITDA 1,431 (calculation C1); acquired business in three quarters only; management's release shows total debt 4,012 and net debt 3,515 (S7 page:3), which are 25 lower |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 (2025-12-31) | 9.42 | x | Adjusted EBITDA 1,130 over interest paid 120 (S1 page:81); interest received from swaps of 6 is not netted |
| Q1 2026 (2026-03-31) | 8.93 | x | Trailing Adjusted EBITDA 1,196 over trailing interest paid 134 (calculations C1 and C2); inputs S2 page:3 and S1 page:81 |
| Q2 2026 (2026-06-30) | 7.71 | x | Trailing Adjusted EBITDA 1,287 over trailing interest paid 167 (calculations C1 and C2); inputs S3 page:3 |
| Q3 2026 (2026-09-30) | 7.73 | x | Trailing Adjusted EBITDA 1,431 over trailing interest paid 185 (calculations C1 and C2); inputs S4 page:3; trailing cash interest holds only part of a year of acquisition debt and coupon timing on the notes makes quarterly cash paid uneven |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (2025-12-31) | 1,495 | 745 | US$m | Cash S1 page:81; revolver commitment 750 less 5 of letters of credit, no loans outstanding (S1 page:103) |
| Q1 2026 (2026-03-31) | 311 | 845 | US$m | Cash S2 page:3; revolver availability 845 after 150 of revolving loans outstanding and 5 of letters of credit (S2 page:18) |
| Q2 2026 (2026-06-30) | 399 | 995 | US$m | Cash S3 page:3; revolver availability 995 net of 5 of letters of credit (S3 page:19) |
| Q3 2026 (2026-09-30) | 497 | 996 | US$m | Cash S4 page:2, of which 361 is held by foreign subsidiaries (S4 page:44); revolver 1,000 less 4 of letters of credit (S4 page:21); revolver matures January 2031 |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0 | US$m | Constructed from the 2026-09-30 debt note (S4 page:19) by final maturity year; no instrument matures in 2026, but minimum amortization of 1 per quarter on the term loan and 3 per quarter on the incremental term loan is paid in every year and is counted in the final-maturity year; current portion of long-term debt is 20 (S4 page:2) |
| 2027 | 300 | US$m | 4.75% senior notes due October 2027 after the 100 redemption in September 2026 (S4 page:22); unsecured |
| 2028 | 0 | US$m | No instrument final maturity in 2028; amortization as noted for 2026 |
| 2029 | 500 | US$m | 5.875% senior notes due June 2029; unsecured |
| 2030 | 0 | US$m | No instrument final maturity in 2030; amortization as noted for 2026 |
| 2031 | 1,505 | US$m | 3.75% senior notes due January 2031, 1,000, plus term loan due March 2031, 505 (S4 page:19); the 1,000 revolver is undrawn and also matures January 2031 (S4 page:21) |
| 2032 | 0 | US$m | No instrument final maturity in 2032; amortization as noted for 2026 |
| 2033 | 1,694 | US$m | Incremental term loan due January 2033, 1,194, plus 5.875% senior notes due December 2033, 500; the incremental loan has a springing maturity to the term loan maturity if that falls earlier (S4 page:20) |
| Finance leases, no dated schedule | 38 | US$m | Present value of finance lease liabilities (S4 page:25), within total long-term debt; undiscounted payments by year are in the lease note |

### Financials and credit metrics

| Metric | Q3 2026 or 2026-09-30 | Q3 2025 | 9M 2026 | 9M 2025 | FY2025 or 2025-12-31 | Basis, unit and locator |
| --- | --- | --- | --- | --- | --- | --- |
| Net sales | 1,534 | 693 | 4,506 | 2,273 | 3,010 | US$m, reported; S4 page:2, S1 page:80; 2026 includes the acquired business, 2025 does not |
| Gross profit | 505 | 330 | 1,426 | 1,111 | 1,463 | US$m, reported; S4 page:2, S1 page:80 |
| Operating income | 304 | 204 | 790 | 709 | 880 | US$m, reported; S4 page:2, S1 page:80 |
| Interest expense, net | 51 | 24 | 166 | 67 | 92 | US$m, reported; S4 page:2, S1 page:80 |
| Net income | 191 | 137 | 484 | 524 | 623 | US$m, reported; S4 page:2, S1 page:80 |
| Adjusted EBITDA, company-defined | 400 | 256 | 1,166 | 865 | 1,130 | US$m, non-GAAP as reported; S4 page:41, S1 page:117; definition follows the credit agreement, which is not supplied |
| Adjusted EBITDA margin | 26.1% | 36.9% | 25.9% | 38.1% | 37.5% | Percent, as printed in the reconciliations; S4 page:41, S1 page:60 |
| Net cash provided by operating activities | 343 | 228 | 811 | 593 | 836 | US$m, reported; S4 page:41 and page:3, S1 page:60 |
| Additions of long-lived assets | 65 | 44 | 149 | 101 | 175 | US$m outflow shown as a positive magnitude; S4 page:41, S1 page:60 |
| Adjusted free cash flow | 278 | 184 | 662 | 492 | 661 | US$m, non-GAAP as reported: operating cash flow less additions of long-lived assets; S4 page:41, S1 page:60 |
| Interest paid, cash | 45 | 27 | 152 | 87 | 120 | US$m outflow shown as a positive magnitude; quarter from S7 page:9, others S4 page:3 and S1 page:81 |
| Cash and cash equivalents | 497 | Not applicable: balance at a date | Not applicable: balance at a date | Not applicable: balance at a date | 1,495 | US$m, reported; S4 page:2 |
| Total long-term debt, principal and finance leases | 4,037 | Not applicable: balance at a date | Not applicable: balance at a date | Not applicable: balance at a date | 2,909 | US$m, reported before deferred financing costs of 25 and 19; S4 page:19 |
| Net debt on the same measure | 3,540 | Not applicable: calculated at a date | Not applicable: calculated at a date | Not applicable: calculated at a date | 1,414 | US$m, calculated (C3); management's release shows 3,515 on its own measure (S7 page:3) |
| Revolver availability, net of letters of credit | 996 | Not applicable: balance at a date | Not applicable: balance at a date | Not applicable: balance at a date | 745 | US$m, reported; S4 page:21, S1 page:103 |
| Trailing Adjusted EBITDA | 1,431 | Not applicable: trailing at a date | Not applicable: trailing at a date | Not applicable: trailing at a date | 1,130 | US$m, calculated (C1); not pro forma for the acquired business |
| Total debt / trailing Adjusted EBITDA | 2.82x | Not applicable: ratio at a date | Not applicable: ratio at a date | Not applicable: ratio at a date | 2.57x | Calculated (C4) |
| Net debt / trailing Adjusted EBITDA | 2.47x | Not applicable: ratio at a date | Not applicable: ratio at a date | Not applicable: ratio at a date | 1.25x | Calculated (C4) |
| Trailing Adjusted EBITDA / trailing interest paid | 7.73x | Not applicable: ratio at a date | Not applicable: ratio at a date | Not applicable: ratio at a date | 9.42x | Calculated (C2 and C5) |
| First lien net leverage ratio, reported | 0.84x | Not applicable: ratio at a date | Not applicable: ratio at a date | Not applicable: ratio at a date | (0.87x) | As reported under the credit agreement definition, maximum 5.50x; S4 page:22, S1 page:103 |

### Debt structure

| Instrument | Issuer or borrower | Amount at 2026-09-30 | Rate | Maturity | Security and guarantee as printed | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| Revolving credit facility, 1,000 commitments | ATI | 0 drawn; 4 of letters of credit | Margin by first lien net leverage grid; commitment fee 0.25% | January 2031 | Secured by lien on substantially all assets of Holdings, ATI and certain guarantors | S4 page:20 and page:21 |
| Term loan | ATI | 505 | Term SOFR plus 1.50%, all-in 5.29% | March 2031 | Same secured package | S4 page:19 and page:20 |
| Incremental term loan | ATI | 1,194 | Term SOFR plus 1.75%, all-in 5.54% | January 2033, springing to the term loan maturity if earlier | Same secured package | S4 page:19 and page:20 |
| 4.75% senior notes | ATI | 300 | 4.75% fixed | October 2027 | Unsecured; guarantor roster unresolved | S4 page:19 and page:22 |
| 5.875% senior notes | ATI | 500 | 5.875% fixed | June 2029 | Unsecured; guarantor roster unresolved | S4 page:19 |
| 3.75% senior notes | ATI | 1,000 | 3.75% fixed | January 2031 | Unsecured; guarantor roster unresolved | S4 page:19 |
| 5.875% senior notes | ATI | 500 | 5.875% fixed | December 2033 | Unsecured; guarantor roster unresolved | S4 page:19 |
| Finance lease liabilities | Entity not stated in the note | 38 | Weighted average discount rate 3.28% | Weighted average remaining term 16.1 years | Lease assets | S4 page:25 |
| Total | | 4,037 | | | Secured term loans 1,699; notes 2,300; leases 38 | S4 page:19 |

### Leverage and coverage

Total debt rose from 2,909 at 2025-12-31 (S1 page:101) to 4,295 at 2026-03-31 (S2 page:15), then fell to 4,140 at 2026-06-30 (S3 page:17) and 4,037 at 2026-09-30 (S4 page:19). The first-quarter peak includes 150 drawn on the revolver (S2 page:15). From the first-quarter peak of 4,295 to 4,037, a fall of 258, the 150 revolver balance was repaid, 100 of the 4.75% notes were redeemed in September 2026 (S4 page:22) and the two term loans amortized by 9, while finance leases rose by 1 (calculation C16). Management states year-to-date debt repayment of over 400 (S7 page:1); the cash flow statement shows 300 of revolver repayments and 110 of payments on long-term debt, a total of 410 (calculation C7).

Trailing leverage on the plain reported measure is 2.82x gross and 2.47x net at the third quarter, falling from 3.59x and 3.33x at the first quarter. Direction check: after the first-quarter peak the gross ratio fell in each of the next two quarters (3.59x, 3.22x, 2.82x), and net debt fell from 3,984 to 3,741 to 3,540 (calculation C3). The trailing figure is a mixed perimeter. It adds FY2025 (no acquired business) to the 2026 quarters (with it), so it understates the earnings that the debt now supports. The acquired segment's Adjusted EBITDA is 285 for nine months and 83 for the third quarter (S7 page:10), and no filing in the pack gives its 2025 results, so a pro forma combined trailing EBITDA is Not calculable here.

The acquired segment earns a much lower margin than the legacy business: segment Adjusted EBITDA margin of 12.7% for the third quarter against 37.8% for Allison Transmission (S7 page:10). The consolidated Adjusted EBITDA margin has therefore fallen from 36.9% in the third quarter of 2025 to 26.1% (S4 page:41). This is a mix effect that leverage on a trailing basis cannot show.

Interest cover on cash paid is 7.73x trailing at the third quarter against 9.42x for FY2025. Interest expense, net for nine months is 166 against 67 (S4 page:2), driven by 49 on the incremental term loan, 22 on the 2033 notes and 17 of lower interest income (S4 page:38). The first quarter of 2026 is the first with the new debt, so the trailing cash figure holds three or fewer quarters of the new interest; cover on a run-rate basis would be lower than reported, but a run-rate is Not calculable from the filings without assuming a rate path for the floating loans.

### Liquidity

Liquidity at 2026-09-30 is 497 of cash plus 996 of undrawn revolver, a total of 1,493 (calculation C6), compared with 2,240 at 2025-12-31. Of the cash, 361 sits with foreign subsidiaries, mostly in Switzerland, China and India (S4 page:44); management says local restrictions are not expected to prevent funding of initiatives. The revolver of 1,000 carries a letters of credit allowance of up to 75 and 4 of letters of credit are outstanding (S4 page:21). No facility expires within twelve months of the cutoff. The nearest maturity is 300 of 4.75% notes due October 2027, which falls inside twelve months of the 2026-11-05 cutoff and about twelve months after the balance sheet date. Scheduled amortization is 4 per quarter in total. Management states that operating cash flow, cash and revolver capacity are sufficient for the next twelve months (S4 page:47); that is its assertion.

Uses of cash year to date (nine months 2026): business acquisition net of cash acquired 2,529, capital additions 149, dividends 72 and share repurchases 123 (S4 page:3). Remaining repurchase authorization is 1,068 (S4 page:47). Distributions to shareholders are therefore a discretionary use that can compete with debt reduction; the nine-month cash dividends and repurchases total 195 (calculation C8) against adjusted free cash flow of 662.

### Covenants

The credit facility requires a maximum first lien net leverage ratio of 5.50x when revolving loan commitments remain outstanding at a quarter end; the reported ratio is 0.84x at 2026-09-30 (S4 page:22). Reported ratios were 1.29x at 2026-03-31 (S2 page:18), 1.01x at 2026-06-30 (S3 page:20) and (0.87x) at 2025-12-31 (S1 page:103), where a negative value means cash exceeded first lien debt. Headroom against the maximum is 4.66x ratio points at the third quarter (calculation C9). A ratio at or below 4.00x also removes excess cash flow payments (S4 page:22).

Definition check: the reported ratio can be reproduced at all four dates as term loans and any drawn revolver, less all cash, over trailing Adjusted EBITDA as reported, without any pro forma adjustment for the acquisition (calculation C10). That is an inference from matching numbers; the credit agreement is not supplied, so the covenant definition itself is Not supplied. The ratio is a first lien measure and excludes the 2,300 of unsecured notes; it is not comparable with the total leverage figures above. Indenture covenants are negative covenants only, and the company states compliance with all covenants at 2026-09-30 (S4 page:22).

### Cash flow quality

Nine-month operating cash flow is 811 against 593 a year earlier, helped by higher gross profit and lower cash incentive compensation and reduced by higher cash interest and taxes and by working capital funding (S4 page:47). Operating cash flow includes 46 of payments for acquisition expenses against 30 a year earlier (S4 page:41). Working capital items in the cash flow statement are receivables (200) outflow, inventories 15 inflow, payables 207 inflow and other 12 inflow, a net inflow of 34 (calculation C11, S4 page:3). Cash taxes paid of 143 compare with income tax expense of 114 (S4 page:3 and page:2), and interest paid of 152 compares with interest expense, net of 166. Adjusted free cash flow is 662 for nine months against 492, and for the third quarter 278 against 184 (S4 page:41). Management guides full-year 2026 operating cash flow of 1,110 to 1,140 and adjusted free cash flow of 850 to 900 (S7 page:4); guidance is a forward-looking management statement and is not used in any ratio here.

### Adjusted EBITDA definition risk

Adjusted EBITDA of 1,166 for nine months is net income of 484 plus interest 166, depreciation 136, taxes 114, amortization 66 and a further 200 of adjustments (calculation C12, S4 page:41). Those adjustments are 64 of inventory step-up, 41 of depreciation on stepped-up assets, 30 of acquisition-related expenses, 25 of stock compensation, 17 of restructuring, 11 of unrealized loss on marketable securities, 3 of unrealized loss on foreign exchange, 2 of impairment and 7 of other items defined by the credit agreement. The adjustments equal 17.2% of the reported figure (calculation C12). The FY2025 bridge has 110 of other adjustments against 1,130 (S1 page:117). Acquisition-related expenses are cash costs that recur in 2026 and the footnote to operating cash flow shows 46 of cash payments for them in nine months (S4 page:41). The definition follows the credit agreement (S4 page:39) and the agreement is not in the pack, so the add-back baskets and any cap are Not supplied.

### Claims outside the debt figure

| Claim | Amount | Inside or outside the 4,037 debt figure | Locator |
| --- | --- | --- | --- |
| Operating lease liabilities, present value | 79 | Outside; total undiscounted payments 107 | S4 page:25 |
| Finance lease liabilities | 38 | Inside | S4 page:19 and page:25 |
| Defined benefit pension unfunded status at 2025-12-31 | 4 | Outside; not updated at 2026-09-30 in the pack | S1 page:50 |
| Retiree medical (OPEB) unfunded status at 2025-12-31 | 66 | Outside; not updated at 2026-09-30 in the pack | S1 page:50 |
| Product warranty liability, current 61 and non-current 66 | 127 | Outside | S4 page:23 |
| Deferred revenue, current 74 and non-current 105 | 179 | Outside | S4 page:23 |
| Vendor buyback obligation | 21 | Outside; within other current liabilities | S4 page:25 |
| Cross-currency swaps hedging euro net investment | Notional 1,000; fair value assets 12 and liabilities 11 | Outside | S4 page:17 and page:18 |

A search of S1 and S4 for factoring, supply chain finance, supplier finance, purchase commitments and take-or-pay terms found no disclosure of any of them. Litigation and consent-decree funding: Note Q states ordinary-course claims and says the company believes the ultimate liability, if any, will not be material (S4 page:27); no separate funding obligation is described. These are search results over the text, not a representation by the company.

### Latest quarter and events to the cutoff

During the third quarter of 2026 the company redeemed 100 of the 4.75% senior notes (S4 page:22), paid a quarterly dividend of 23 and repurchased 57 of stock (S7 page:1), recorded 17 of restructuring charges for off-highway footprint optimization (S4 page:41), and recorded acquisition-related expenses of 4. In the second quarter, Amendment No. 6 lowered the term loan margin by 0.25% (S4 page:20). Management raised its full-year 2026 guidance on 2026-11-02 to net sales of 5,975 to 6,075, adjusted EBITDA of 1,530 to 1,580 and adjusted free cash flow of 850 to 900 (S7 page:4); guidance is management's, not a filed fact. Purchase accounting is preliminary and was adjusted in the quarter with a 7 net increase to goodwill (S4 page:8). The latest dated content in the pack is the 10-Q signature date of 2026-11-04 (S4 page:54); a text search of the 10-Q found no subsequent events note, and nothing is dated after the 2026-11-05 cutoff.

### Data quality and conflicts carried forward

The purchase price is 2,732 in the annual report (preliminary) and 2,628 in the quarterly reports; the later figure is used for the transaction (S1 page:118, S4 page:7). Total debt is 4,037 in the debt note and 4,012 in management's release; this handoff uses 4,037 for every ratio and labels the other where it appears. The FY2025 annual statements have one segment; 2025 quarterly segments are recast in the 2026 quarterly reports (S4 page:29, page:30). The release debt and net debt figures were tied to the filings in the earlier handoff. Figures that depend on text extraction of flattened tables were read from the page text and tied to printed totals (calculations C3 and C12).

### Key evidence quotes

| Id | Locator | Exact quote |
| --- | --- | --- |
| Q1 | S4 page:19 | "Total long-term debt $ 4,037 $ 2,909" |
| Q2 | S4 page:21 | "As of September 30, 2026, the Company had $996 million available under the Revolving Credit Facility, net of $4 million in letters of credit." |
| Q3 | S4 page:22 | "specified maximum first lien net leverage ratio of 5.50x" |
| Q4 | S4 page:22 | "achieving a 0.84x ratio" |
| Q5 | S4 page:41 | "Adjusted EBITDA (Non-GAAP) $ 400 $ 256 $ 1,166 $ 865" |
| Q6 | S1 page:117 | "Adjusted EBITDA $ 1,130 $ 1,165 $ 1,108" |
| Q7 | S4 page:22 | "In September 2026, the Company made a $100 million redemption payment on the 4.75% Senior Notes." |
| Q8 | S7 page:3 | "total debt of $4,012 million and net debt of $3,515 million" |
| Q9 | S4 page:3 | "Interest paid $ (152 ) $ (87 )" |
| Q10 | S1 page:81 | "Interest paid $ (120 ) $ (124 ) $ (131 )" |
| Q11 | S2 page:3 | "Interest paid $ (41 ) $ (27 )" |
| Q12 | S3 page:3 | "Interest paid $ (107 ) $ (60 )" |
| Q13 | S2 page:18 | "achieving a 1.29x ratio" |
| Q14 | S3 page:20 | "achieving a 1.01x ratio" |
| Q15 | S1 page:103 | "achieving a (0.87x) ratio" |
| Q16 | S2 page:18 | "As of March 31, 2026, the Company had $845 million available under the Revolving Credit Facility, net of $150 million of revolving loans outstanding and $5 million in letters of credit." |
| Q17 | S3 page:19 | "As of June 30, 2026, the Company had $995 million available under the Revolving Credit Facility, net of $5 million in letters of credit." |
| Q18 | S1 page:103 | "As of December 31, 2025, the Company had $745 million available under the Revolving Credit Facility, net of $5 million in letters of credit." |

## Calculations

All inputs are printed figures in US$ millions with the locators given. Ratios are rounded to two decimals only at the end.

| Id | Calculation | Inputs and locators | Result |
| --- | --- | --- | --- |
| C1 | Trailing Adjusted EBITDA = FY2025 less prior-year year-to-date plus current year-to-date | FY2025 1,130 (S1 page:117). Q1: 1,130 less Q1 2025 296 plus Q1 2026 362 (S2 page:33 reconciliation). Q2: 1,130 less six months 2025 609 plus six months 2026 766 (S3 page:38). Q3: 1,130 less nine months 2025 865 plus nine months 2026 1,166 (S4 page:41) | Q1 1,196; Q2 1,287; Q3 1,431; FY2025 1,130 |
| C2 | Trailing interest paid = FY2025 less prior-year year-to-date plus current year-to-date | FY2025 120 (S1 page:81). Q1: 120 less 27 plus 41 (S2 page:3). Q2: 120 less 60 plus 107 (S3 page:3). Q3: 120 less 87 plus 152 (S4 page:3) | Q1 134; Q2 167; Q3 185; FY2025 120 |
| C3 | Net debt = total long-term debt less cash | FY2025 2,909 less 1,495; Q1 4,295 less 311; Q2 4,140 less 399; Q3 4,037 less 497 (debt S1 page:101, S2 page:15, S3 page:17, S4 page:19; cash S1 page:81, S2 page:3, S3 page:3, S4 page:2) | FY2025 1,414; Q1 3,984; Q2 3,741; Q3 3,540 |
| C4 | Leverage = debt or net debt over trailing Adjusted EBITDA | Total: 2,909 / 1,130 = 2.574; 4,295 / 1,196 = 3.591; 4,140 / 1,287 = 3.217; 4,037 / 1,431 = 2.821. Net: 1,414 / 1,130 = 1.251; 3,984 / 1,196 = 3.331; 3,741 / 1,287 = 2.907; 3,540 / 1,431 = 2.474 | Total 2.57x, 3.59x, 3.22x, 2.82x; net 1.25x, 3.33x, 2.91x, 2.47x |
| C5 | Cover = trailing Adjusted EBITDA over trailing interest paid | 1,130 / 120 = 9.417; 1,196 / 134 = 8.925; 1,287 / 167 = 7.707; 1,431 / 185 = 7.735 | 9.42x, 8.93x, 7.71x, 7.73x |
| C6 | Liquidity = cash plus undrawn revolver | FY2025 1,495 + 745; Q1 311 + 845; Q2 399 + 995; Q3 497 + 996 | 2,240; 1,156; 1,394; 1,493 |
| C7 | Year-to-date debt repayment check | Payments on revolving credit facility 300 and payments on long-term debt 110 (S4 page:3); the 110 is the 100 note redemption (S4 page:22) plus 10 of term loan amortization (S4 page:45) | 300 + 110 = 410, consistent with management's statement of over 400 in S7 page:1 |
| C8 | Nine-month shareholder cash distributions | Dividend payments 72 plus repurchases of common stock 123 (S4 page:3) | 195 |
| C9 | Covenant headroom in ratio points | Maximum 5.50x less reported 0.84x (S4 page:22) | 4.66x |
| C10 | Covenant ratio reproduction | Q3: (505 + 1,194 less 497) / 1,431 = 1,202 / 1,431 = 0.840. FY2025: (509 less 1,495) / 1,130 = negative 986 / 1,130 = negative 0.873. Q1: (508 + 1,200 + 150 less 311) / 1,196 = 1,547 / 1,196 = 1.293. Q2: (506 + 1,197 less 399) / 1,287 = 1,304 / 1,287 = 1.013 | 0.84x, (0.87x), 1.29x, 1.01x, each equal to the printed ratio |
| C11 | Nine-month working capital cash effect | Accounts receivable (200), inventories 15, accounts payable 207, other assets and liabilities 12 (S4 page:3) | 34 net inflow |
| C12 | Adjustments in nine-month Adjusted EBITDA | Net income 484 + interest 166 + depreciation 136 + taxes 114 + amortization 66 = 966; Adjusted EBITDA 1,166 less 966 = 200, equal to the sum 64 + 41 + 30 + 25 + 17 + 11 + 3 + 2 + 7 (S4 page:41); 200 / 1,166 = 0.1715 | 200, 17.2% of Adjusted EBITDA |
| C13 | Debt table maturity tie | 300 + 500 + 1,505 + 1,694 + 38 (maturity chart rows) | 4,037, equal to total long-term debt in S4 page:19 |
| C14 | Debt by security | Term loan 505 + incremental term loan 1,194 = 1,699 secured; notes 300 + 500 + 1,000 + 500 = 2,300 | 1,699 secured, 2,300 unsecured, 38 leases |
| C16 | Debt change from Q1 2026 to Q3 2026 | Total long-term debt 4,295 (S2 page:15) less 4,037 (S4 page:19) = 258. Components: revolver 150 to 0; 4.75% notes 400 to 300; term loan 508 to 505; incremental term loan 1,200 to 1,194; finance leases 37 to 38 | 150 + 100 + 3 + 6 less 1 = 258, equal to the change |
| C15 | Segment Adjusted EBITDA tie | Allison Transmission 333 + Allison Off-Highway 83 less central group function 16 for Q3; 927 + 285 less 46 for nine months (S7 page:10) | 400 and 1,166, equal to the consolidated figures |

## Gaps

| Gap | Severity | Effect and remediation |
| --- | --- | --- |
| Pro forma or pre-acquisition earnings for the acquired business are Not supplied; no filing in the pack gives its 2025 results | High | Trailing EBITDA mixes perimeters, so leverage is overstated and cover is flattered; a combined trailing figure is Not calculable. Obtain pro forma disclosure or the acquired business's historical statements |
| Credit agreement, amendments and indentures are Not supplied | Medium | The Adjusted EBITDA add-back baskets, covenant definition and restricted payment capacity cannot be checked; the covenant reproduction in C10 is an inference |
| Guarantor roster is unresolved between S4 page:20 and page:22 | Medium | Structural subordination of the notes cannot be stated beyond the secured and unsecured split |
| No year-by-year maturity schedule after the January 2026 amendment | Low | The maturity chart is constructed from instrument dates; scheduled amortization is counted in the final-maturity year |
| Pension and retiree medical balances are at 2025-12-31 only; no 2026-09-30 funded status in the pack | Low | The claims table uses the year-end figures and labels them |
| Cash interest in the trailing figure holds only part of a year of acquisition debt | Medium | Cover is flattered; a run-rate cover is Not calculable without a rate assumption |
| Purchase accounting is preliminary and may change | Medium | Goodwill, intangibles and acquired balances are provisional (S4 page:8) |
| Text extraction only; tables were read from flattened text and tied to printed totals | Low | Totals were checked in the calculations; no fidelity review against the original HTML |

## Next module

CP-1A, business and transaction context. Carry forward: the acquisition closed 2026-01-01 at a final purchase price of 2,628 (earlier preliminary 2,732); it was funded by 1,200 incremental term loan, 500 of 2033 notes, 300 revolver draw and cash; the acquired segment earns a lower margin (12.7% Adjusted EBITDA margin in Q3 2026 versus 37.8% for Allison Transmission); the secured package is 1,699 of term loans and 2,300 of unsecured notes sit behind it; and the guarantor roster and legal documents remain open.
