## Request

Financial base view for GFL Environmental Inc. (issuer id gfl; consolidated group, parent-level registrant), as of 2026-11-05, pathway credit_snapshot, current period Q3 2026 (three months to September 30, 2026) against FY2025, reporting currency CAD (context file). All amounts are CAD millions under IFRS unless stated; USD instruments appear at their CAD carrying value, and the Q3 release states `All references to “$” in this press release are to Canadian dollars, unless otherwise noted.` (Q3PR page:10). Scope: extract and label the reported financial base (income statement, cash flow, balance sheet, debt, liquidity, covenants, claims outside debt, quality of the Adjusted EBITDA measure) and compute leverage, coverage and liquidity metrics from printed inputs only, with periods and perimeter labelled. No outside knowledge of the company is used and no source after the cutoff 2026-11-05 is used as fact. The reporting perimeter is GFL Environmental Inc. and its consolidated subsidiaries; no issuer-only, restricted-group or guarantor-only statements are in the pack, so none can be given. The upstream source-readiness handoff (CP-0) rated the pack READY_WITH_LIMITATIONS; its limitations are carried forward in Gaps.

## Sources

Issuer sources relied on (exact name and sha256 as supplied). Keys in brackets are used in locators as `(KEY page:N)`; a page is the retained chunk, not a printed page.

| Key | Source name | sha256 |
| --- | --- | --- |
| 40F | 40-F_2025-12-31_gfl-20251231x40f.htm.jsonl | b934765df3e7c34910af8387591b8fa09e1dab95cdcc8ca06bb6c968dd003ae6 |
| Q1FS | 6-K-EX-99.1_2026-03-31_tm2612685d3_ex99-1.htm.jsonl | cb537fb74c382c1d0201e410842d4660c8613b15a362445d11ff422e5b399f25 |
| Q1PR | 6-K-EX-99.1_2026-04-29_tm2612685d2_ex99-1.htm.jsonl | 3df073d71665ee940b9aad03ce71f25168457a8b67f443c14d9006bb7687f437 |
| Q2FS | 6-K-EX-99.1_2026-06-30_tm2619744d3_ex99-1.htm.jsonl | f263228fdadc42723c2dcd6496cb1b52232f1a5fd2b7778ad4e13cf2111721c2 |
| Q2PR | 6-K-EX-99.1_2026-07-29_tm2619744d2_ex99-1.htm.jsonl | 5fa07feeac05724810518cb847015c4db9d05aa3ab7046fa5917870573c8a1c3 |
| Q3PR | 6-K-EX-99.1_2026-10-28_tm2626649d2_ex99-1.htm.jsonl | ee28f5cf135f3ebbb50b3dfc34b1ac6447600e4aae341e5faea9d8d69de358cb |
| Q3FS | 6-K-EX-99.1_2026-10-30_tm2626649d1_ex99-1.htm.jsonl | 21de76c788e5b3fc408d84e05a80d6dd1586537f33922ada67131193bae391d4 |

Run context (settings, not issuer evidence): context, sha256 8fcb7a42287c8f6efb39cea12a8c3d3db65bfbc11e1653a358aafe84da574912.

Supplied handoff:

| Module | sha256 | Use in this module |
| --- | --- | --- |
| CP-0 | 5dd8c10116ab71166e18daa0c21c2809277112054bd8d1c10946b00be6546478 | Opened and used: source roles (Q3 statements control IFRS facts, Q3 release controls non-IFRS measures), the revised December 31, 2025 comparatives, the absence of FY2025 annual exhibits and of legal documents, and the tie-outs it recorded. |

Authority used here: the Q3 and earlier interim statements (FS keys) control reported IFRS facts; releases (PR keys) supply non-IFRS measures, Net Leverage and guidance as attributed management claims.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Debt rose sharply in the third quarter with the SECURE acquisition. On unadjusted trailing Adjusted EBITDA, leverage is above management's 3.8x run-rate figure and the 5.00x covenant level, so the covenant definition decides the headroom. | Medium | The credit agreement and full-year 2025 statements are not in the pack, so covenant headroom and full-year cash interest cannot be tested. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt rose to 11,696.4 from 7,426.7 at year-end 2025 while trailing Adjusted EBITDA includes only one month of SECURE. | Unadjusted leverage is 5.18x against management's run-rate 3.8x; the gap rests on 730.9 of management adjustments. | High |
| Cash interest paid was 371.7 for nine months 2026 against Adjusted EBITDA of 1,748.4. | Coverage of 4.70x on that basis; the lumpy semi-annual coupons make single quarters unreliable. | Medium |
| Liquidity cannot be stated exactly: revolver commitments, drawings and letters of credit are printed, but not the amount available. | Derived revolver availability is 809.7 if all non-EDC letters of credit sit on the revolver. | Medium |
| About 172.1 of nine-month 2026 cash costs are added back to Adjusted EBITDA, and the 2025 comparatives were revised. | Adjusted EBITDA is more generous than cash earnings; use the revised comparatives. | Medium |

### Financial base view

GFL's financial base at September 30, 2026 is a larger, more levered consolidated group than at year-end 2025, and the leverage figure depends entirely on which EBITDA and debt definition is used. Reported debt before deferred costs rose by 4,269.7 to 11,696.4 while cash rose by 210.9 to 296.5; the increase coincides with 2,569.8 of nine-month acquisition spend, the SECURE share-and-cash purchase that closed September 1, 2026, and a Term Loan B Facility entered on August 28, 2026; the sources do not bridge the debt movement line by line. Trailing-twelve-month Adjusted EBITDA of 2,257.1 captures SECURE for one month only, so total debt over that EBITDA is 5.18x and net 5.05x, whereas management's Net Leverage of 3.8x adds 730.9 of run-rate adjustments to reach 2,988.0. The revolver covenant is 5.00x for four quarters after a Material Acquisition and 4.50x otherwise, and management states compliance; the agreement definition is not in the pack, so headroom is not calculable here and the unadjusted 5.18x must not be read as a breach. Cash conversion improved at the management-defined Adjusted Free Cash Flow level (484.9 for nine months 2026 against 331.3), but operating cash flow is stated after 193.1 of working-capital outflow and the earnings measure adds back 172.1 of cash costs. All FY2025 figures other than the year-end balance sheet comparatives and management's trailing-twelve-month figures are unavailable, and the year-end 2025 balance sheet was revised after Q1.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2025 | 3.74 | 3.70 | x | Debt before deferred costs 7,426.7 and cash 85.6 over trailing-twelve-month Adjusted EBITDA 1,985.0 (Q3PR page:14), a management measure. Excludes leases. Management Net Leverage with run-rate EBITDA 2,157.6 is 3.4x. FY2025 audited statements not in pack |
| Mar 31, 2026 | 4.61 | 3.90 | x | Debt 9,384.2 and cash 1,436.2 over trailing Adjusted EBITDA 2,037.3 (Q1PR page:13). Excludes leases. Management Net Leverage is 3.6x |
| Jun 30, 2026 | 4.54 | 4.45 | x | Debt 9,604.2 and cash 192.1 over trailing Adjusted EBITDA 2,113.4 (Q2PR page:14). Excludes leases. Management Net Leverage is 4.0x |
| Sep 30, 2026 | 5.18 | 5.05 | x | Debt 11,696.4 and cash 296.5 over trailing Adjusted EBITDA 2,257.1 (Q3PR page:14). Excludes leases of 705.0. Includes SECURE debt in full but only one month of SECURE EBITDA, so overstated against a pro forma basis; management Net Leverage with run-rate EBITDA 2,988.0 is 3.8x. Not the revolver covenant ratio |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q1 2026 | 4.02 | x | Adjusted EBITDA 478.5 over interest paid in cash 118.9 for the three months; semi-annual coupon timing makes single quarters noisy |
| Q2 2026 | 7.36 | x | Adjusted EBITDA 591.2 over interest paid in cash 80.3; low cash interest reflects coupon timing, not a lower interest burden |
| Q3 2026 | 3.93 | x | Adjusted EBITDA 678.7 over interest paid in cash 172.5; includes one month of SECURE EBITDA and new debt |
| Nine months 2026 | 4.70 | x | Adjusted EBITDA 1,748.4 over interest paid in cash 371.7; best available proxy because trailing-twelve-month cash interest needs FY2025 cash flow, which is not in the pack |
| Q3 2025 | 4.53 | x | Adjusted EBITDA 535.1 over interest paid in cash 118.1; comparative as revised |
| Nine months 2025 | 3.98 | x | Adjusted EBITDA 1,476.3 over interest paid in cash 371.1; cash interest includes 68.9 paid on early termination of debt (Q3PR page:18) and the 2025 cash flow statement may include discontinued operations (the operating cash flow does include 69.6), so not like for like |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2025 | Not supplied: reported in CAD millions | Not supplied: reported in CAD millions | CAD millions | Cash 85.6 and revolver drawn 750.6; commitments at that date are described only in later interim statements, so availability is not calculable from the pack |
| Mar 31, 2026 | Not supplied: reported in CAD millions | Not supplied: reported in CAD millions | CAD millions | Cash 1,436.2; revolver commitments 2,025.0 less drawn 1,185.1 is 839.9 before letters of credit, 564.9 after the 275.0 of letters of credit outside the EDC facility |
| Jun 30, 2026 | Not supplied: reported in CAD millions | Not supplied: reported in CAD millions | CAD millions | Cash 192.1; commitments 2,025.0 less drawn 182.0 is 1,843.0 before letters of credit, 1,564.1 after 278.9 of non-EDC letters of credit |
| Sep 30, 2026 | Not supplied: reported in CAD millions | Not supplied: reported in CAD millions | CAD millions | Cash 296.5; commitments 2,025.0 less drawn 868.0 is 1,157.0 before letters of credit, 809.7 after 347.3 of non-EDC letters of credit. Excludes the 1,000.0 accordion and subsidiary facilities; allocation of letters of credit to the revolver is an assumption |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | Not supplied: reported in CAD millions | CAD millions | Current portion of long-term debt 14.2 at Sep 30, 2026 is due within twelve months; no instrument matures in calendar 2026 by the note's footnotes |
| 2027 | Not supplied: reported in CAD millions | CAD millions | No named instrument matures in 2027; amortisation of term loans inside Other is not printed |
| 2028 | Not supplied: reported in CAD millions | CAD millions | 3.500% 2028 Secured Notes 1,064.1 (Sep 1) and 4.000% 2028 Notes 1,064.1 (Aug 1) total 2,128.2, plus the subsidiary term loan and revolver maturing Aug 31, 2028 (amounts inside Other 528.0, split not printed) |
| 2029 | Not supplied: reported in CAD millions | CAD millions | 4.750% 2029 Notes 1,064.1 (Jun 15) and 4.375% 2029 Notes 780.3 (Aug 15) total 1,844.4 |
| 2030 | Not supplied: reported in CAD millions | CAD millions | Revolving credit facility drawn 868.0 (matures Apr 29, 2030) plus the subsidiary term loan and revolver maturing Sep 21, 2030 (inside Other) |
| 2031 | Not supplied: reported in CAD millions | CAD millions | 6.750% 2031 Secured Notes 1,418.8 (Jan 15), 5.625% 2031 Notes 1,064.1 (Jul 1) and the 4.375% Bonds 297.9 at their initial mandatory tender date of Oct 1, 2031, total 2,780.8 |
| 2032 | Not supplied: reported in CAD millions | CAD millions | 6.625% 2032 Notes 709.4 (Apr 1) |
| 2033 | Not supplied: reported in CAD millions | CAD millions | Term Loan B Facility 1,418.8 (Aug 28, 2033) |
| 2034 | Not supplied: reported in CAD millions | CAD millions | 5.500% 2034 Notes 1,418.8 (Feb 1) |

### Financials and credit metrics

| Metric | Q3 2026 | Q3 2025 | Nine months 2026 | Nine months 2025 | At Sep 30, 2026 | At Dec 31, 2025 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue | 2,155.3 | 1,694.2 | 5,746.9 | 4,929.5 | n/a | n/a | Reported, continuing operations (Q3FS page:1) |
| Adjusted EBITDA (management) | 678.7 | 535.1 | 1,748.4 | 1,476.3 | n/a | n/a | Non-IFRS (Q3FS page:15); excludes the share of results of associates |
| Adjusted EBITDA margin (printed) | 31.5% | 31.6% | 30.4% | 29.9% | n/a | n/a | Printed ratio (Q3PR page:14) |
| Net (loss) income from continuing operations | (28.0) | 90.4 | (409.8) | 123.5 | n/a | n/a | Reported (Q3FS page:1); 2025 comparatives revised |
| Interest and other finance costs | 179.4 | 129.2 | 482.9 | 460.7 | n/a | n/a | Reported; of which interest 148.5, 106.7, 402.1 and 345.5 (Q3FS page:13) |
| Interest paid in cash | 172.5 | 118.1 | 371.7 | 371.1 | n/a | n/a | Cash flow statement, operating section (Q3FS page:4) |
| Cash flows from operating activities | 365.0 | 391.1 | 950.1 | 870.7 | n/a | n/a | Reported (Q3FS page:4); nine months 2025 includes 69.6 from discontinued operations |
| Purchase of property and equipment | 239.0 | 289.5 | 912.8 | 893.1 | n/a | n/a | Reported (Q3FS page:4); the management free cash flow reconciliation shows 875.0 for nine months 2025 |
| Adjusted Free Cash Flow (management) | 272.5 | 180.5 | 484.9 | 331.3 | n/a | n/a | Non-IFRS (Q3PR page:18); adds back transaction, integration and CEO costs and incremental growth capex |
| Business acquisitions, net of cash acquired | 1,085.3 | 330.6 | 2,569.8 | 616.5 | n/a | n/a | Investing outflow (Q3FS page:4) |
| Issuance of long-term debt | 2,438.9 | 964.3 | 6,795.9 | 1,833.5 | n/a | n/a | Financing (Q3FS page:4) |
| Repayment of long-term debt | 1,320.3 | 475.0 | 3,823.9 | 4,294.0 | n/a | n/a | Financing (Q3FS page:4) |
| Repurchase of subordinate voting shares | nil | 346.3 | 71.0 | 2,758.5 | n/a | n/a | Financing (Q3FS page:4) |
| Cash | n/a | n/a | n/a | n/a | 296.5 | 85.6 | Balance sheet (Q3FS page:2) |
| Total long-term debt (carrying) | n/a | n/a | n/a | n/a | 11,671.4 | 7,422.6 | Current 14.2 plus non-current 11,657.2 (Q3FS page:11) |
| Debt before discount, derivative and deferred costs | n/a | n/a | n/a | n/a | 11,696.4 | 7,426.7 | Note 7 subtotal (Q3FS page:11); basis of leverage here |
| Lease obligations, current plus non-current | n/a | n/a | n/a | n/a | 705.0 | 510.5 | Outside Note 7 debt (Q3FS page:2) |
| Closure and post-closure obligations | n/a | n/a | n/a | n/a | 1,503.8 | 1,170.5 | Outside debt (Q3FS page:11) |
| Total shareholders' equity | n/a | n/a | n/a | n/a | 11,900.2 | 7,413.7 | December 2025 as revised (Q3FS page:2) |
| Trailing-twelve-month Adjusted EBITDA | n/a | n/a | n/a | n/a | 2,257.1 | 1,985.0 | Management (Q3PR page:14) |
| Run-Rate EBITDA (management) | n/a | n/a | n/a | n/a | 2,988.0 | 2,157.6 | Includes management adjustments of 730.9 and 172.6 (Q3PR page:14) |
| Net Leverage (management) | n/a | n/a | n/a | n/a | 3.8x | 3.4x | Printed (Q3PR page:14) |
| Total debt / trailing Adjusted EBITDA (computed) | n/a | n/a | n/a | n/a | 5.18x | 3.74x | See Calculations; excludes leases; not the covenant ratio |
| Net debt / trailing Adjusted EBITDA (computed) | n/a | n/a | n/a | n/a | 5.05x | 3.70x | See Calculations; not the covenant ratio |
| Adjusted EBITDA / interest paid in cash (computed) | 3.93x | 4.53x | 4.70x | 3.98x | n/a | n/a | See Calculations |
| Segment Canada: revenue and Adjusted EBITDA | 773.0 and 275.6 | 559.1 and 188.0 | 1,918.1 and 650.3 | 1,609.8 and 513.7 | n/a | n/a | Segment note (Q3FS page:15) |
| Segment USA: revenue and Adjusted EBITDA | 1,382.3 and 466.6 | 1,135.1 and 409.4 | 3,828.8 and 1,285.5 | 3,319.7 and 1,163.4 | n/a | n/a | Segment note (Q3FS page:15); corporate Adjusted EBITDA (63.5) for Q3 2026 |

### Debt instruments

All instruments are obligations of the consolidated group; the note does not name the issuer or co-issuer of any series, nor the guarantors of any series other than the bonds. Carrying values are CAD and move with the exchange rate; USD principal is printed only where stated. Source: Note 7 (Q3FS page:11) and its footnotes (Q3FS page:12).

| Instrument | Carrying value Sep 30, 2026 | Carrying value Dec 31, 2025 | Rate | Maturity | Security and guarantors as printed |
| --- | --- | --- | --- | --- | --- |
| Revolving credit facility | 868.0 | 750.6 | CORRA/SOFR plus 1.125% to 1.750% plus a credit spread adjustment, or Canadian/Prime plus 0.125% to 0.750% | Apr 29, 2030 | Secured by mortgages on certain properties, a general security agreement over all assets of GFL and certain material subsidiaries and a share pledge; commitments 2,000.0 plus 25.0 plus 1,000.0 accordion |
| Term Loan B Facility | 1,418.8 | nil | SOFR plus 2.000% | Aug 28, 2033 | Same security package as the revolver; entered Aug 28, 2026 |
| 3.500% USD senior secured notes | 1,064.1 | 1,028.0 | 3.500% | Sep 1, 2028 | Secured; collateral and guarantors not printed |
| 6.750% USD senior secured notes | 1,418.8 | 1,370.6 | 6.750% | Jan 15, 2031 | Collateral released under the indenture; `As a result, the notes are no longer secured.` (Q3FS page:12) |
| 4.000% USD senior notes | 1,064.1 | 1,028.0 | 4.000% | Aug 1, 2028 | US$500.0 million initial plus US$250.0 million additional; security not stated |
| 4.750% USD senior notes | 1,064.1 | 1,028.0 | 4.750% | Jun 15, 2029 | Security not stated |
| 4.375% USD senior notes | 780.3 | 753.8 | 4.375% | Aug 15, 2029 | Security not stated |
| 6.625% USD senior notes | 709.4 | 685.3 | 6.625% | Apr 1, 2032 | Security not stated |
| 5.500% USD senior notes | 1,418.8 | nil | 5.500% | Feb 1, 2034 | Security not stated; first coupon Aug 1, 2026 |
| 5.625% USD senior notes | 1,064.1 | nil | 5.625% | Jul 1, 2031 | Security not stated; first coupon Jan 1, 2027 |
| 4.375% USD Solid Waste Disposal Revenue Bonds | 297.9 | 287.8 | 4.375% | Initial mandatory tender Oct 1, 2031 | `The bonds are unsecured and guaranteed jointly and severally, fully and unconditionally by GFL and certain of its subsidiaries.` (Q3FS page:13); US$210.0 million issued Oct 8, 2024 |
| Other (subsidiary stand-alone facilities and other) | 528.0 | 494.6 | Subsidiary term loans and revolvers at base or SOFR plus 2.000% to 4.000% and 2.000% to 3.250% | Aug 31, 2028 and Sep 21, 2030 | Non-wholly-owned subsidiaries; details in Q3FS page:13 |

### Claims outside the debt figure

| Claim | Amount | Period | Inside or outside Note 7 debt | Locator |
| --- | --- | --- | --- | --- |
| Lease obligations, current 99.3 and non-current 605.7 | 705.0 | Sep 30, 2026 | Outside; separate balance sheet lines | Q3FS page:2 |
| Letters of credit outstanding, including 187.8 under the EDC Guaranteed LC Facility | 535.1 | Sep 30, 2026 | Outside; off balance sheet; some LCs may sit on the revolver | Q3FS page:18 |
| Performance bonds issued | 2,324.1 | Sep 30, 2026 | Outside; off balance sheet | Q3FS page:19 |
| Crude oil transportation commitments | 561.4 | Sep 30, 2026 | Outside; total payment if committed pipeline volumes are not delivered; nil at Dec 31, 2025 | Q3FS page:19 |
| Crude oil storage commitments recognized as onerous contracts | 51.0 | Sep 30, 2026 | Outside; recognized as onerous | Q3FS page:19 |
| Closure and post-closure obligations (balance sheet) | 1,503.8 | Sep 30, 2026 | Outside; legally restricted trust assets of 38.9 sit in other long-term assets | Q3FS page:11 |
| Accrued contingent consideration on acquisitions | 28.5 | Nine months 2026 additions | Outside; arose in the period | Q3FS page:6 |
| Pension and retiree medical, factoring or supply-chain finance, litigation or consent-decree funding | Not supplied | n/a | Searched all seven sources for pension, retirement, post-employment, factoring, supply chain, litigation and consent; hits were asset retirement obligations, restricted share units and the auditor consent exhibit, none of these claims | all sources |

### Liquidity and covenants

- Facilities. `GFL has access to a $2,000.0 million revolving credit facility (available in Canadian and US dollars), a $25.0 million revolving credit facility (available in US dollars) and an aggregate $1,000.0 million accordion feature` (Q3FS page:12), maturing April 29, 2030, so neither the revolver nor the Term Loan B Facility expires within twelve months (the EDC facility term is not stated). The EDC Guaranteed LC Facility gives `$250.0 million of letters of credit that are 100% guaranteed by Export Development Canada` (Q3FS page:18) against 187.8 used.
- Availability. The sources print commitments, drawings and letters of credit but no statement of the amount available. The derived revolver availability range is 809.7 to 1,157.0 at September 30, 2026 (Calculations). Cash is 296.5. The subsidiary facilities (a US$30.0 million revolver undrawn and a US$100.0 million revolver with US$43.0 million drawn) are USD and outside the parent's revolver; they are not added.
- Covenants. `The Revolving Credit Agreement contains a Total Net Funded Debt to Adjusted EBITDA and an Interest Coverage Ratio (each as defined in the Revolving Credit Agreement) financial maintenance covenant.` (Q3FS page:12). The leverage test is `equal to or less than 5.00 to 1.00 for a period of four complete fiscal quarters following completion of a Material Acquisition` (Q3FS page:13) and otherwise 4.50 to 1.00; the interest coverage test is at least 3.00 to 1.00; `GFL was in compliance with these covenants.` (Q3FS page:13). No step-down date is printed. The reported covenant figures are not printed, so headroom is Not calculable. The metric computed here differs from the covenant: it uses unadjusted trailing Adjusted EBITDA, debt before deferred costs and cash netting, while the agreement defines Total Net Funded Debt and Adjusted EBITDA itself, and the release says Run-Rate EBITDA is `calculated in accordance with the terms of our revolving credit agreement` (Q3PR page:10).

### Earnings quality and cash flow

- Add-backs. Nine months 2026 EBITDA of 1,203.4 becomes Adjusted EBITDA of 1,748.4 after 545.0 of add-backs (Q3PR page:15; Calculations). Of these, 172.1 are cash costs: transaction costs 70.6, acquisition, rebranding and integration costs 27.3 and Founder/CEO remuneration 74.2, which is `cash payment to the Founder and CEO, which payment had been previously satisfied through the issuance of restricted share units` (Q3FS page:16). Share-based payments of 87.0, foreign exchange and derivative losses of 192.6 and the Call Option charge of 45.0 are non-cash.
- Cash conversion. Operating cash flow of 950.1 for nine months 2026 is after 193.1 of working-capital outflow (Q3FS page:4) and 371.7 of cash interest. Adjusted Free Cash Flow of 484.9 adds back, among other items, 104.5 of cash transaction costs, 27.3 integration costs, 74.2 CEO remuneration and 182.4 of incremental growth investments (Q3PR page:18); management describes conversion as `improving Adjusted Free Cash Flow1 conversion toward the mid 40% range` (Q3PR page:1).
- Net loss drivers. Net loss from continuing operations of 409.8 for nine months 2026 follows interest and other finance costs of 482.9, a loss on foreign exchange of 196.7, a Call Option fair value charge of 45.0 and an equity-method loss of 48.0.

### Latest quarter and events to the cutoff

- Financing. The Term Loan B Facility was entered on August 28, 2026 and matures August 28, 2033 at SOFR plus 2.000%; the revolver was amended and restated through September 1, 2026; the 5.500% 2034 Notes and 5.625% 2031 Notes are on the June 30, 2026 balance sheet (1,421.0 and 1,065.8, Q2FS page:10). Cross-currency interest rate swaps were entered on the 5.625% 2031 Notes on June 25, 2026 (fixing 4.480%) and on the Term Loan B Facility on August 28, 2026 (fixing 5.009%) (Q3FS page:18). Q3 2026 debt issued was 2,438.9 and repaid 1,320.3.
- SECURE. `On September 1, 2026, GFL acquired 100% of the issued and outstanding common shares of SECURE for total consideration of approximately $5,414.1 million.` (Q3FS page:7): shares 4,334.8 and cash 1,079.3. Goodwill recognized was 4,968.1. The allocation is provisional. GFL also acquired 13 other businesses in nine months, each individually immaterial; total net assets acquired in nine months were 7,012.6 including SECURE, of which others 1,598.5.
- Guidance (management, not a fact). Full-year 2026 Adjusted EBITDA approximately 2,490 to 2,495, Adjusted Free Cash Flow approximately 1,020, cash interest approximately 455 and `Net Leverage2 is estimated to be in the mid 3s by the end of 2026` (Q3PR page:3). Guidance excludes acquisitions not yet completed.
- After quarter end. The Q3 statements contain no subsequent-events note. The release dated October 28, 2026 records a Special Committee reviewing take-private proposals with a deadline of November 9, 2026 for updated proposals, a date after the cutoff (Q3PR page:1). No proposal terms are supplied.
- Revised comparatives. The December 31, 2025 equity-method investment was 1,898.0 as first reported and 1,805.3 as revised (Q3FS page:9); this figure and the 2025 comparatives in this handoff are the revised ones, as in the Q3 statements.

## Calculations

All amounts are CAD millions. Inputs are the cited printed figures; results are computed here and rounded to two decimals for ratios.

| Calculation | Formula and inputs | Result |
| --- | --- | --- |
| Total debt / trailing Adjusted EBITDA, Sep 30, 2026 | 11,696.4 (Q3FS page:11) / 2,257.1 (Q3PR page:14) | 5.18x |
| Net debt, Sep 30, 2026 | 11,696.4 - 296.5 | 11,399.9 (equal to the figure printed in Q3PR page:14) |
| Net debt / trailing Adjusted EBITDA, Sep 30, 2026 | 11,399.9 / 2,257.1 | 5.05x |
| Net debt / Run-Rate EBITDA, Sep 30, 2026 | 11,399.9 / 2,988.0, where 2,988.0 = 2,257.1 + 730.9 | 3.82x, printed as 3.8x |
| Dec 31, 2025 | 7,426.7 / 1,985.0; (7,426.7 - 85.6 = 7,341.1) / 1,985.0 | 3.74x total; 3.70x net |
| Mar 31, 2026 | 9,384.2 / 2,037.3; (9,384.2 - 1,436.2 = 7,948.0) / 2,037.3 | 4.61x total; 3.90x net |
| Jun 30, 2026 | 9,604.2 / 2,113.4; (9,604.2 - 192.1 = 9,412.1) / 2,113.4 | 4.54x total; 4.45x net |
| Total debt plus leases / trailing Adjusted EBITDA, Sep 30, 2026 | (11,696.4 + 705.0) / 2,257.1 where leases = 99.3 + 605.7 | 5.49x; at Dec 31, 2025 (7,426.7 + 510.5) / 1,985.0 = 4.00x, leases 59.9 + 450.6 |
| Change in debt | 11,696.4 - 7,426.7 | 4,269.7 increase |
| Adjusted EBITDA / interest paid in cash | Q1 478.5 / 118.9; Q2 591.2 / 80.3; Q3 678.7 / 172.5; nine months 1,748.4 / 371.7; Q3 2025 535.1 / 118.1; nine months 2025 1,476.3 / 371.1 (cash interest by quarter 118.9 + 80.3 + 172.5 = 371.7) | 4.02x; 7.36x; 3.93x; 4.70x; 4.53x; 3.98x |
| Nine months 2025 ex early-termination interest (illustrative) | 1,476.3 / (371.1 - 68.9 = 302.2) | 4.89x; not used in the chart because the 68.9 is management-reported on a different basis |
| Revolver availability, Sep 30, 2026 | Commitments 2,000.0 + 25.0 = 2,025.0; less drawn 868.0 = 1,157.0; less non-EDC letters of credit (535.1 - 187.8 = 347.3) = 809.7 | 809.7 to 1,157.0; the lower figure assumes every letter of credit outside the EDC facility sits on the revolver, which the note does not say |
| Revolver availability, Mar 31, 2026 | 2,025.0 - 1,185.1 = 839.9; letters of credit 417.6 - 142.6 = 275.0; 839.9 - 275.0 | 564.9 to 839.9 |
| Revolver availability, Jun 30, 2026 | 2,025.0 - 182.0 = 1,843.0; letters of credit 424.3 - 145.4 = 278.9; 1,843.0 - 278.9 | 1,564.1 to 1,843.0 |
| Add-back bridge, nine months 2026 | 192.6 + (-14.2) + 45.0 + 60.4 + 87.0 + 70.6 + 27.3 + 74.2 + 2.1 | 545.0; 1,203.4 + 545.0 = 1,748.4, equal to the printed Adjusted EBITDA |
| Cash costs added back, nine months 2026 | 70.6 + 27.3 + 74.2 | 172.1, which is 9.84% of Adjusted EBITDA of 1,748.4; Q3 2026 transaction costs 46.5 plus integration 7.6 = 54.1, which is 7.97% of 678.7 |
| Adjusted EBITDA bridge, trailing | 1,985.0 + 1,748.4 - 1,476.3 | 2,257.1, equal to the printed trailing figure |
| Debt maturity grouping | 2028: 1,064.1 + 1,064.1 = 2,128.2; 2029: 1,064.1 + 780.3 = 1,844.4; 2030: 868.0; 2031: 1,418.8 + 1,064.1 + 297.9 = 2,780.8; 2032: 709.4; 2033: 1,418.8; 2034: 1,418.8; plus Other 528.0 | 11,696.4, equal to the Note 7 subtotal; the revolver (868.0) is placed in 2030 and Other is unallocated by year |
| Cash conversion | Operating cash flow 950.1 / Adjusted EBITDA 1,748.4; Adjusted Free Cash Flow 484.9 / 1,748.4; prior 331.3 / 1,476.3 | 54.34%; 27.73%; prior 22.44% |
| Margin check | Q3 2026 678.7 / 2,155.3 | 31.49%, printed as 31.5% |

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| FY2025 audited statements, annual MD&A and contractual obligations table are not in the pack (the 40-F only lists them as exhibits, 40F page:5). Not supplied: FY2025 income statement, cash flow, full-year cash interest and year-end debt note | Trailing-twelve-month cash interest and full-year coverage are Not calculable; FY2025 appears only as year-end comparatives and management's 1,985.0 | Obtain the 40-F exhibits |
| No credit agreement or indentures | Reported covenant ratios, headroom, definitions, guarantors and restricted-group perimeter are Not supplied | Obtain the revolving credit agreement and indentures |
| USD principal not printed for most notes | Principal at original currency cannot be shown; CAD carrying values include foreign exchange translation | Use the indentures or annual debt note |
| Maturity by year is derived from footnotes; Other (528.0) and the subsidiary term loan amortisation are not allocated by year | The maturity chart has no numeric cells (CAD reporting) and Other is unallocated | None available in the pack |
| Revolver availability is derived, not printed | Liquidity is a range; letters of credit allocation is an assumption | Management statement or credit agreement |
| Trailing Adjusted EBITDA includes SECURE for one month; provisional purchase accounting | Unadjusted leverage is overstated against a pro forma basis; run-rate adjustments are management estimates | Treat 5.18x and 3.8x as bounds and do not use either as the covenant ratio |
| Nine months 2025 cash flow includes discontinued operations; the management free cash flow reconciliation uses a different capex basis (875.0 against 893.1) | Prior-year coverage and conversion are not like for like | Use 2025 comparatives with the stated caveat |
| Year-end 2025 balance sheet revised after Q1 (Note 3, Q3FS page:9) | Earlier-quarter references to December 2025 differ for equity-method investments, deferred tax and equity | Use the Q3 version |
| Take-private review outcome unknown; no terms | Potential change in ownership, financing and covenants is unquantified | Monitor; not a fact in this handoff |
| No pension, factoring, litigation or consent-decree disclosure in interim statements | Absence in interim statements does not show absence in annual statements | Check annual exhibits |

## Next module

CP-1A should carry forward: the SECURE acquisition (completed September 1, 2026, total consideration 5,414.1, provisional accounting), the Term Loan B Facility, the Special Committee review with its November 9, 2026 deadline (after the cutoff, a future term), the Founder/CEO cash remuneration add-back and the related-party items; the missing annual information form means business description, ownership and control must be marked as not supplied. CP-2 should use the unadjusted leverage of 5.18x total and 5.05x net, management's 3.8x run-rate Net Leverage and the covenant levels together, state that covenant headroom is Not calculable, show liquidity as the 809.7 to 1,157.0 revolver range plus cash of 296.5, and label December 2025 figures as revised. CP-5 should check the quotes above against their pages, the 2025 comparative revision, and the capex basis difference (875.0 against 893.1).
