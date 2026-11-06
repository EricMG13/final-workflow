## Request

Module CP-1, financial base and credit metrics, for Service Properties Trust (SVC, issuer id svc), as of 2026-11-05 (cutoff 2026-11-05), pathway credit_snapshot, reporting currency USD. The module extracts the reported financial base from the pinned filings, calculates leverage, interest cover, liquidity and maturity data with every input shown, and carries the source-readiness limitations from the upstream handoff.

Perimeter: the registrant, Service Properties Trust, and its consolidated subsidiaries, including consolidated taxable REIT subsidiaries. No separate borrower, parent or guarantor statements exist in the sources. The issuer of the senior notes is the Trust itself; the net lease mortgage notes are issued by bankruptcy-remote subsidiaries that are consolidated.

Units and periods: the filings print dollars in thousands. Statement tables below are in USD thousands as printed. The four chart tables convert to US$m by dividing by 1,000, which is a change of scale only. Periods follow the filings: FY2024 and FY2025 (years ended December 31), Q1 2026, Q2 2026 and Q3 2026 (three months ended March 31, June 30 and September 30, 2026), nine months 2026 and nine months 2025 (ended September 30), and last twelve months (LTM) periods derived as FY2025 plus the 2026 year-to-date period less the 2025 year-to-date period. The context labels q3-2026 and fy-2025 match these periods.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_svc-20251231.htm.jsonl | 15b3016df80eabdf6701b53b9a448339a1d5ae915a5566d3f751538a9f1cf080 | Audited FY2025 and FY2024 statements, debt note, maturities, revolver terms and amendment, indenture tests at December 31, 2025, operating leases |
| 10-Q_2026-03-31_svc-20260331.htm.jsonl | ddc1e35889e90bee1694334ce247e9f387726f16b7ce89bd8b9a51b4f4bc89df | Q1 2026 statements, debt note, revolver availability, indenture tests |
| 10-Q_2026-06-30_svc-20260630.htm.jsonl | da660527db0f1353ac545e91f43f35b2233d5df64df735bb0e6f23f04bc598ba | Q2 2026 and six-month statements, debt note, revolver draw, indenture tests |
| 10-Q_2026-09-30_svc-20260930.htm.jsonl | f0504ddf51d9be829b263ff0aec5ab5ea7aa542d5518e107dbff10e9d9d5c34a | Q3 2026 and nine-month statements, debt note, maturity table, fixed-rate debt table, liquidity, indenture tests, subsequent events |
| EX-99.1_2026-05-06_svc_033126xexhibitx991.htm.jsonl | 2f1a4993f8cd70e48576dc6e794111c2977d7a50e2e8b2ecb75d059468ae6628 | Read: announcement only, no financial figures used |
| EX-99.1_2026-08-05_svc_063026xexhibitx991.htm.jsonl | fb76ab0c1c7105cbf6ef323f85f2c808f256d901d8e982c18e3c61667221ab25 | Read: announcement only, no financial figures used |
| EX-99.1_2026-11-04_svc_093026xexhibitx991.htm.jsonl | 865a9819dca5454c3d53aca165a47efc28c6cf0685e35747e559ffc2c9cf026d | Read: announcement only; portfolio counts agree with the Q3 10-Q |

The context input (sha256 a72cf33ce12be07f9ed0051d7ed4f82ab1f3905d4d81ff0fe1a5919c08327fd3) holds the requester's settings and is not issuer evidence. It leaves ratings, market data and deal terms blank.

### Handoffs

| Module | sha256 | Used for |
| --- | --- | --- |
| CP-0 | 0fbb7ad07aadbbd8b3c01b679bc383a79e711cd00b11da3f74ea1f9d0cbdcdab | Source readiness view READY_WITH_LIMITATIONS, split-adjustment limitation, gaps on credit agreement and indentures. Read in full and carried below. |

### Short names and locators

10-K FY2025, 10-Q Q1, 10-Q Q2 and 10-Q Q3 name the four filings. A locator `page:N` is the chunk number in the pinned extraction file, not the printed page.

### Correction to the upstream handoff

CP-0 listed the revolver covenant levels as not supplied and said the credit agreement terms are described only in general terms. The 10-K FY2025 does print two revolver covenant terms: "reduce the minimum fixed charge coverage ratio covenant from 1.50x to 1.30x effective with respect to the fourth quarter of 2024" and "change the required collateral property debt yield to 10%" (10-K FY2025, page:195). What remains unsupplied is the issuer's reported figure for either test at any date, and the credit agreement itself, so revolver headroom is still Not calculable. The CP-0 statement was right for the 10-Q filings and incomplete for the 10-K. CP-0 cannot be edited, so this answer is the correction.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Debt fell from 5,504,809 to 4,652,322 through 2026, but leverage on a calculated last-twelve-month core EBITDA of 475,642 is still 9.78x gross and 9.70x net, and cash interest cover is 1.41x. | Medium | The company reports no EBITDA, and the credit agreement ratios and headroom are not supplied. Core EBITDA is our own definition and includes sold hotels. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Liquidity at September 30, 2026 is cash of 40,118 plus an undrawn revolver of 650,000, but the revolver matures June 29, 2027 and an extension or refinancing is being explored. | Almost all liquidity is one secured facility that expires within nine months, so the refinancing outcome drives near-term risk. | High |
| Fixed-rate debt maturities are 584,150 in 2027 and 1,002,775 in 2028, against cash of 40,118. | Repayment depends on asset sales, new secured debt or equity, which the company has used heavily in 2026. | High |
| The senior notes tests at September 30, 2026 are 53.9% total debt to adjusted assets against a 60% maximum, and 1.83x debt service cover against a 1.50x minimum. | Headroom improved from December 31, 2025 (58.7% and 1.59x) after debt repayment and equity issuance, but debt service cover is the tighter test. | High |
| Nine-month 2026 net loss was 462,956, including impairments of 270,883, and hotel revenue fell with hotel sales. | Earnings quality is weak and the hotel base keeps shrinking, so past EBITDA overstates what the retained portfolio earns. | Medium |

### Financial base view

The reported financial base is complete enough for the requested use, with limits. Four filings give full statements, a debt note by class, a maturity table, the senior notes indenture tests, revolver availability and subsequent events through November 2, 2026. The company prints no EBITDA, so the leverage and cover charts use a core EBITDA defined and calculated here from statement lines: total revenues less hotel operating expenses, net lease operating expenses, general and administrative expenses and transaction related costs. It excludes depreciation, impairments, gains and losses on sales, early extinguishment losses and equity in losses of an investee. It is not an issuer figure and not a covenant measure.

On that basis the trust is highly levered and thinly covered but de-risked by a year of debt reduction. Principal debt fell by 852,487 from December 31, 2025 to September 30, 2026, funded by net equity proceeds of 541,798, new net lease mortgage notes, asset sales and cash on hand. Gross leverage on LTM core EBITDA moved from 10.77x at FY2025 to 9.78x at the third quarter of 2026, and cash interest cover from 1.35x to 1.41x. Both are weak, and the LTM EBITDA still includes earnings of hotels that have since been sold, so forward leverage on the retained portfolio is likely worse than the LTM figure shows; that last point is analyst inference, not a reported number. Liquidity is thin in cash and rests on a single undrawn secured revolver that matures within nine months. The balance sheet is secured-heavy: secured principal of 2,927,322 is 63% of principal debt, a share calculated in the Calculations section.

Limits on this view: no issuer EBITDA, no credit agreement ratios or headroom, share data that mixes split-adjusted and unadjusted bases across filings, unaudited interim statements, and hotel operating data that the company states it has not verified.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 10.77 | 10.09 | x | Principal debt of 5,504,809 thousand at December 31, 2025 (includes the 45,000 variable funding note) over calculated core EBITDA of 511,334 thousand; net of unrestricted cash of 346,813 thousand. Core EBITDA is our definition, not reported, and includes hotels since sold. |
| LTM Q1 2026 | 10.49 | 10.45 | x | Principal debt of 5,249,319 thousand over derived LTM core EBITDA of 500,352 thousand; unrestricted cash of 19,294 thousand. Derived as FY2025 plus Q1 2026 less Q1 2025. |
| LTM Q2 2026 | 9.81 | 9.80 | x | Principal debt of 4,723,321 thousand (includes 25,000 revolver draw) over derived LTM core EBITDA of 481,549 thousand; unrestricted cash of 5,511 thousand. Derived as FY2025 plus six months 2026 less six months 2025. |
| LTM Q3 2026 | 9.78 | 9.70 | x | Principal debt of 4,652,322 thousand over derived LTM core EBITDA of 475,642 thousand; unrestricted cash of 40,118 thousand (restricted cash of 22,374 thousand excluded). Derived as FY2025 plus nine months 2026 less nine months 2025; includes earnings of hotels sold during the period. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 1.35 | x | Core EBITDA of 511,334 thousand over cash paid for interest of 379,566 thousand (10-K FY2025 supplemental cash flow). |
| LTM Q1 2026 | 1.30 | x | Core EBITDA of 500,352 thousand over derived LTM cash interest of 383,820 thousand (FY2025 plus Q1 2026 of 51,049 less Q1 2025 of 46,795). |
| LTM Q2 2026 | 1.36 | x | Core EBITDA of 481,549 thousand over derived LTM cash interest of 352,906 thousand (six months 2026 of 158,873 less six months 2025 of 185,533 added to FY2025). |
| LTM Q3 2026 | 1.41 | x | Core EBITDA of 475,642 thousand over derived LTM cash interest of 336,491 thousand. Cash interest excludes accretion on the zero coupon 2027 secured notes, which is non-cash until maturity, and is gross of interest income. Coupons are semi-annual so interim periods are lumpy. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 346.813 | 650 | US$m | Unrestricted cash at December 31, 2025 (restricted cash of 25.275 excluded). Revolver undrawn at 650; the 45 variable funding note was fully drawn so adds no undrawn capacity. Revolver availability is subject to collateral performance, value and covenant conditions. No letters of credit were found in any source. |
| Q1 2026 | 19.294 | 650 | US$m | Unrestricted cash at March 31, 2026; revolver undrawn at 650 at March 31 and May 4, 2026; variable funding note fully drawn. |
| Q2 2026 | 5.511 | 625 | US$m | Unrestricted cash at June 30, 2026; 25 drawn on the revolver leaving 625 available; variable funding note fully drawn. The 25 draw was repaid by August 3, 2026, when the filing reports no revolver borrowings. |
| Q3 2026 | 40.118 | 650 | US$m | Unrestricted cash at September 30, 2026; revolver undrawn at 650 at September 30 and November 2, 2026; variable funding note repaid and terminated in September 2026. The revolver matures June 29, 2027, within twelve months, with two six-month extension options subject to a fee and conditions. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0.999 | US$m | Remaining 2026 amortisation of net lease mortgage notes, as printed at September 30, 2026. |
| 2027 | 584.150 | US$m | Includes the zero coupon senior secured notes due 2027 at 580.155 principal at maturity (carrying value 533.897); the month of maturity is not printed in the pages read. A one-time one-year extension option exists, subject to conditions and a fee. The remainder is mortgage note amortisation. The undrawn 650 revolver also matures on June 29, 2027 and is not in this table. |
| 2028 | 1002.775 | US$m | 3.95% senior unsecured notes of 400 plus the Series 2023-1 net lease mortgage note balloon due February 2028 and mortgage note amortisation. |
| 2029 | 427.038 | US$m | 4.95% senior unsecured notes of 425 plus mortgage note amortisation. |
| 2030 | 402.038 | US$m | 4.375% senior unsecured notes of 400 plus mortgage note amortisation. |
| 2031 and later | 2235.322 | US$m | Printed as Thereafter: 8.625% senior secured notes of 1000 due 2031, Series 2026-1 net lease mortgage notes due March 2031, and 8.875% senior guaranteed unsecured notes of 500 due 2032. Total fixed rate debt 4652.322. |

### Financials and credit metrics

| Metric (USD thousands unless stated) | FY2024 | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | Nine months 2026 | Nine months 2025 | LTM Q3 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hotel operating revenues | 1,496,705 | 1,413,403 | 264,575 | 320,071 | 298,379 | 883,025 | 1,116,944 | 1,179,484 |
| Rental income | 400,223 | 401,435 | 99,876 | 100,903 | 101,141 | 301,920 | 300,441 | 402,914 |
| Total revenues | 1,896,928 | 1,814,838 | 364,451 | 420,974 | 399,520 | 1,184,945 | 1,417,385 | 1,582,398 |
| Hotel operating expenses | 1,274,153 | 1,226,542 | 242,644 | 264,654 | 255,780 | 763,078 | 963,111 | 1,026,509 |
| Net lease operating expenses | 19,817 | 21,597 | 7,440 | 6,046 | 6,389 | 19,875 | 16,303 | 25,169 |
| General and administrative | 40,239 | 40,667 | 8,796 | 11,093 | 9,965 | 29,854 | 30,831 | 39,690 |
| Transaction related costs | 6,894 | 14,698 | 2,509 | 463 | 1,857 | 4,829 | 4,139 | 15,388 |
| Core EBITDA (calculated, not reported) | 555,825 | 511,334 | 103,062 | 138,718 | 125,529 | 367,309 | 403,001 | 475,642 |
| Depreciation and amortization | 371,786 | 314,963 | 75,843 | 77,083 | 72,152 | 225,078 | 238,583 | 301,458 |
| Loss on asset impairment | 56,212 | 81,889 | 28,095 | 189,097 | 53,691 | 270,883 | 81,788 | 270,984 |
| Interest expense (includes non-cash amortization) | 383,792 | 413,614 | 96,547 | 87,655 | 85,932 | 270,134 | 311,972 | 371,776 |
| Net loss | (275,526) | (202,321) | (151,178) | (223,838) | (87,940) | (462,956) | (201,539) | (463,738) |
| Net cash provided by operating activities | 139,391 | 117,808 | 35,578 | Not supplied: only six-month total printed (43,842) | Not supplied: not printed for the quarter | 132,226 | 136,305 | 113,729 |
| Real estate improvements (cash) | (303,600) | (224,833) | (49,893) | Not supplied: only six-month total printed (76,863) | Not supplied: not printed for the quarter | (110,062) | (148,154) | (186,741) |
| Cash paid for interest | 366,194 | 379,566 | 51,049 | Not supplied: only six-month total printed (158,873) | Not supplied: not printed for the quarter | 196,080 | 239,155 | 336,491 |
| Net proceeds from sale of real estate | 102,382 | 853,046 | Not supplied: only year-to-date totals are printed | Not supplied: only year-to-date totals are printed | Not supplied: only year-to-date totals are printed | 84,500 | 331,202 | 606,344 |
| Normalized FFO (company measure) | 176,402 | 129,884 | 7,445 | 55,024 | 43,839 | 106,308 | 102,349 | 133,843 |
| Cash and cash equivalents (period end) | 143,482 | 346,813 | 19,294 | 5,511 | 40,118 | 40,118 | 417,415 | 40,118 |
| Debt, carrying value (secured plus unsecured, period end) | 5,710,703 | 5,334,428 | 5,086,769 | 4,579,037 | 4,525,438 | 4,525,438 | Not supplied: the September 30, 2025 balance sheet is not in the pack | 4,525,438 |
| Debt, principal (period end) | Not supplied: not printed in the FY2025 10-K | 5,504,809 | 5,249,319 | 4,723,321 | 4,652,322 | 4,652,322 | Not supplied: the September 30, 2025 debt note is not in the pack | 4,652,322 |
| Total assets (period end) | 7,119,558 | 6,491,580 | 6,081,625 | 5,838,485 | 5,720,456 | 5,720,456 | Not supplied: the September 30, 2025 balance sheet is not in the pack | 5,720,456 |
| Total shareholders' equity (period end) | 851,873 | 646,124 | 493,736 | 806,455 | 712,749 | 712,749 | 647,908 | 712,749 |
| Principal debt / core EBITDA (x) | Not supplied: principal not printed | 10.77 | 10.49 (LTM) | 9.81 (LTM) | 9.78 (LTM) | n/a | n/a | 9.78 |
| Net principal debt / core EBITDA (x) | Not supplied: principal not printed | 10.09 | 10.45 (LTM) | 9.80 (LTM) | 9.70 (LTM) | n/a | n/a | 9.70 |
| Core EBITDA / cash interest (x) | 1.52 | 1.35 | 1.30 (LTM) | 1.36 (LTM) | 1.41 (LTM) | n/a | n/a | 1.41 |

Notes to the table. All amounts are as printed except rows marked calculated, derived or LTM. The Q1, Q2 and Q3 2026 columns are three-month periods; Q3 2026 plus Q2 and Q1 sums to the nine-month figure for each income statement line shown (for example core EBITDA 103,062 plus 138,718 plus 125,529 equals 367,309). The LTM column is FY2025 plus nine months 2026 less nine months 2025. The LTM net proceeds from sales is 853,046 plus 84,500 less 331,202, and LTM Normalized FFO is 129,884 plus 106,308 less 102,349. The total shareholders' equity cell for nine months 2025 is the September 30, 2025 balance. Cash for nine months 2025 is the September 30, 2025 balance from the cash flow reconciliation. Per-share data are excluded because the 10-K and the Q1 10-Q are not adjusted for the 1-for-5 reverse share split and the Q2 and Q3 10-Qs are.

### Source locators for the table

| Item | Locator and quote |
| --- | --- |
| FY2025 and FY2024 income statement | 10-K FY2025 page:172 "Total revenues 1,814,838 1,896,928 1,873,863" |
| FY2025 and FY2024 balance sheet | 10-K FY2025 page:171 "Cash and cash equivalents 346,813 143,482" |
| FY2025 and FY2024 cash flow | 10-K FY2025 page:173 "Net cash provided by operating activities 117,808 139,391 485,549" |
| FY2025 cash paid for interest | 10-K FY2025 page:174 "Cash paid for interest $ 379,566 $ 366,194 $ 314,323" |
| Q1 2026 income statement and cash flow | 10-Q Q1 page:3 "Total revenues 364,451 435,179"; page:4 "Cash paid for interest $ 51,049 $ 46,795" |
| Q2 2026 income statement | 10-Q Q2 page:3 "Total revenues 420,974 503,436 785,425 938,615" |
| Q2 2026 six-month cash flow | 10-Q Q2 page:5 "Cash paid for interest $ 158,873 $ 185,533" |
| Q3 2026 income statement | 10-Q Q3 page:3 "Total revenues 399,520 478,770 1,184,945 1,417,385" |
| Q3 2026 balance sheet | 10-Q Q3 page:2 "Total assets $ 5,720,456 $ 6,491,580" |
| Q3 2026 cash flow | 10-Q Q3 page:5 "Net cash provided by operating activities 132,226 136,305"; "Cash paid for interest $ 196,080 $ 239,155" |
| Normalized FFO | 10-Q Q3 page:62 "Normalized FFO $ 43,839 $ 33,910 $ 106,308 $ 102,349"; 10-Q Q2 page:60 "Normalized FFO $ 55,024 $ 57,603 $ 62,469 $ 68,439"; 10-Q Q1 page:50 "Normalized FFO $ 7,445 $ 10,836"; 10-K FY2025 page:152 "Normalized FFO $ 129,884 $ 176,402" |

### Debt and capital structure at September 30, 2026

Principal debt is 4,652,322 thousand: "(1) $1,725,000 aggregate outstanding principal amount of senior unsecured notes; (2) $1,580,155 aggregate outstanding principal amount of senior secured notes; and (3) $1,347,167 aggregate outstanding principal amount of net lease mortgage notes" (10-Q Q3 page:20). The revolver is undrawn: "we had no amounts outstanding under our revolving credit facility and $650,000 available for borrowing" (10-Q Q3 page:20). Every instrument is fixed rate at September 30, 2026 except the revolver, which is undrawn and priced at SOFR plus 2.50%.

| Instrument | Principal (USD thousands) | Coupon | Maturity | Security and obligors |
| --- | --- | --- | --- | --- |
| Senior secured notes, zero coupon | 580,155 at maturity | 0%, accreting at 7.50% per annum | 2027 | Secured by first-priority liens on equity of subsidiaries that own 36 travel centers (10-K FY2025 page:196); guaranteed by the TA Landlord Subsidiaries and the senior unsecured note guarantors |
| 3.95% senior unsecured notes | 400,000 | 3.95% | 2028 | Issued by the Trust; not guaranteed ("Our $1,225,000 of senior unsecured notes do not have the benefit of any guarantees", 10-Q Q3 page:53) |
| Net lease mortgage notes, Series 2023-1 | 603,186 | 5.60% weighted average | February 2028 | Non-recourse; issuer is SVC ABS LLC; secured by the 471-property collateral pool |
| 4.95% senior unsecured notes | 425,000 | 4.95% | 2029 | Issued by the Trust; not guaranteed |
| 4.375% senior unsecured notes | 400,000 | 4.375% | 2030 | Issued by the Trust; not guaranteed |
| Net lease mortgage notes, Series 2026-1 | 743,981 | 5.96% weighted average | March 2031 | Non-recourse; issuers are SVC ABS LLC, SVC 2026 ABS LLC and SVC 2026 TA ABS LLC; same 471-property pool |
| 8.625% senior secured notes | 1,000,000 | 8.625% | 2031 | Issued by the Trust; secured, with the collateral and guarantors not detailed in the pages read |
| 8.875% senior guaranteed unsecured notes | 500,000 | 8.875% | 2032 | Guaranteed by all subsidiaries except excluded subsidiaries ("fully and unconditionally guaranteed", 10-Q Q3 page:53) |
| Revolving credit facility | 0 drawn of 650,000 | SOFR plus 2.50% | June 29, 2027 | Secured by 55 properties with undepreciated book value of 874,751 (10-Q Q3 page:20) |

The fixed-rate debt table gives annual interest of 263,082 on 4,652,322 of principal (10-Q Q3 page:62). The mortgage note classes amortise monthly on the Class A and Class B notes at 0.50% and 0.25% annualised. The 2026 changes: all 4.95% notes due 2027 (400,000), all 8.375% guaranteed notes due 2029 (700,000) and all 5.50% guaranteed notes due 2027 (450,000) were redeemed for make whole premiums of 1,785, 37,128 and 7,191, the 745,000 Series 2026-1 notes were issued on March 6, 2026, and the 45,000 variable funding note was repaid and terminated in September 2026 (10-Q Q3 pages:21 to 23).

Cross-default: "Our indentures and their supplements contain cross default provisions to any other debt of $50,000 or more" (10-Q Q3 page:53). The credit agreement has cross default to recourse debt of 25,000 or more and non-recourse debt of 75,000 or more. A change of control under the credit agreement includes The RMR Group LLC ceasing to act as business manager (10-Q Q3 page:21).

### Claims outside reported debt

| Claim | Amount and date | Inside or outside the debt figure | Source |
| --- | --- | --- | --- |
| Operating lease liabilities (ground leases and hotel operating leases) | 147,198 at December 31, 2025; the September 30, 2026 amount was not found | Outside principal debt; included in accounts payable and other liabilities | 10-K FY2025 page:191 |
| Minimum lease payments under those operating leases | 262,150 undiscounted at December 31, 2025 | Outside | 10-K FY2025 page:191 |
| Unspent leasing-related obligations to net lease tenants | 10,264 at September 30, 2026 | Outside | 10-Q Q3 page:45 |
| Expected hotel and property capital improvements | 25,000 to 40,000 expected in the last three months of 2026, to be funded from cash on hand | Outside | 10-Q Q3 page:45 |
| Owed to Sonesta for capital expenditure and other reimbursements | 4,196 at September 30, 2026 (39,509 at December 31, 2025) | Outside; in due to related persons | 10-Q Q3 page:16 |
| Guarantees of obligations of taxable REIT subsidiaries | Amount not printed; liabilities of the TRSs were 65,669 at September 30, 2026 | Outside | 10-Q Q3 page:8 |
| Sonesta termination fee waived against a contract extension | 11,035, recorded as an impairment loss in Q3 2026 | Outside; non-cash | 10-Q Q3 page:16 |
| Pensions, retiree medical, factoring, supply-chain finance and litigation funding | None found after searching the 10-K and the Q3 10-Q for these terms. The 10-K states the Trust is "currently not a party to any litigation which we expect to have a material adverse effect" (10-K FY2025 page:121) | Not applicable | 10-K FY2025 page:121 |

Net lease tenant concentration affects the cover on these claims: TravelCenters of America is 68.2% of annualized minimum rent of 395,492 (10-Q Q3 page:56), with a BP Corporation North America guaranty of 2,782,917 over the master leases (10-Q Q3 page:57).

### Covenants and restrictions

| Test | Requirement | Reported at September 30, 2026 | Reported at June 30, 2026 | Reported at December 31, 2025 | Headroom at September 30, 2026 (calculated) |
| --- | --- | --- | --- | --- | --- |
| Total debt / adjusted total assets (indentures) | Maximum 60% | 53.9% | 53.7% | 58.7% | 6.1 percentage points |
| Secured debt / adjusted total assets (indentures) | Maximum 40% | 33.9% | 34.1% | 33.2% | 6.1 percentage points |
| Consolidated income available for debt service / debt service (indentures) | Minimum 1.50x | 1.83x | 1.74x | 1.59x | 0.33x |
| Total unencumbered assets / unsecured debt (indentures) | Minimum 150% | 273.2% | 281.5% | 218.7% | 123.2 percentage points |
| Unencumbered assets in guarantor subsidiaries / senior guaranteed unsecured debt (indentures) | Minimum 2.20x | 8.79x | 9.08x | 4.92x | 6.59x |
| Fixed charge coverage ratio (revolver) | Minimum 1.30x; 1.50x to use the first extension option | Not supplied: reported figure not printed in any source | Not supplied | Not supplied | Not calculable |
| Collateral property debt yield (revolver) | 10% | Not supplied: reported figure not printed in any source | Not supplied | Not supplied | Not calculable |

Locators: indenture tests at September 30, 2026 are in 10-Q Q3 page:51, at June 30, 2026 in 10-Q Q2 page:49, at December 31, 2025 in 10-K FY2025 page:138; the revolver terms are in 10-K FY2025 page:195. The company states it was in compliance with all covenants at September 30, 2026 (10-Q Q3 page:51). Definitions differ from the metrics calculated here: "Consolidated income available for debt service" and "adjusted total assets" are indenture-defined (adjusted total assets 8,631,686 at September 30, 2026), so the 1.83x reported test is not comparable with the 1.41x core EBITDA to cash interest cover calculated here. Availability under the revolver is conditioned on collateral minimum performance and market values (10-Q Q3 page:20).

### Latest quarter and events to the cutoff

- Q3 2026 (three months to September 30, 2026): total revenues 399,520 against 478,770 a year earlier; net loss 87,940 against 46,945; loss on asset impairment 53,691 against 27,067 (10-Q Q3 page:3). The hotel revenue decline is attributed mainly to hotel sales since July 1, 2025: "sales of certain hotels since July 1, 2025 ($94,624)" (10-Q Q3 page:38).
- Financing in 2026: Series 2026-1 net lease mortgage notes of 745,000 issued March 6, 2026; equity offering on April 2, 2026 with net proceeds of 541,798 (10-Q Q3 page:48); redemptions of 400,000, 700,000 and 450,000 of notes; variable funding note of 45,000 repaid in September 2026. The 1-for-5 reverse share split took effect after the close of trading on July 6, 2026.
- Revolver: no draw at September 30, 2026; the company says "We are currently exploring our options to extend or refinance our secured revolving credit facility" (10-Q Q3 page:47).
- Dispositions: 32 properties sold in the nine months for 88,159; six hotels sold in Q3 for 66,100 (10-Q Q3 page:10). Held for sale at September 30, 2026: nine hotels with 1,809 keys and six net lease properties (10-Q Q3 page:10).
- Subsequent events through November 2, 2026 (stated in the Q3 10-Q, dated before the cutoff): sale of eight hotels with 1,509 keys for 50,600 and one net lease property for 295; acquisition of four net lease properties for 8,314; a pending sale of one net lease property for 655 that is subject to conditions (10-Q Q3 pages:11 and 46). A regular distribution of $0.05 per share, about 6,491, was declared October 8, 2026 and is to be paid on or about November 12, 2026 (10-Q Q3 page:47).
- The announcement dated November 4, 2026 reports 87 hotels and 740 net lease properties at September 30, 2026 and refers to results and a presentation on the company website that are not in the pack.

### Interpretation: evidence, mechanism and credit implication

Leverage. Evidence: principal debt of 4,652,322 and calculated LTM core EBITDA of 475,642 give 9.78x, down from 10.77x at FY2025. Mechanism: the improvement comes mostly from the numerator, as 852,487 of debt was retired using equity and sale proceeds, while LTM EBITDA fell from 511,334 as hotels were sold and hotel revenue dropped. Implication: deleveraging is real but asset-sale driven, so each further hotel sale lowers both debt and EBITDA and the ratio improves only if proceeds retire debt at a higher multiple than the EBITDA sold. The hotel segment lost 272,673 in the nine months of 2026 after impairments (10-Q Q3 page:31), so the retained hotels are not yet self-supporting after impairment.

Coverage. Evidence: LTM cash interest of 336,491 against core EBITDA of 475,642 gives 1.41x, and the fixed-rate table shows annual interest of 263,082 on the current debt (10-Q Q3 page:62). Mechanism: LTM cash interest still includes interest on notes repaid during 2026, while LTM EBITDA includes earnings of sold hotels. Implication: cover on the current debt is likely above 1.41x on a run-rate basis only if EBITDA holds, which the hotel sales make uncertain. The 2027 zero coupon notes add no cash interest but accrete at 7.50% per annum, so the cash coverage metric understates the claim growing until maturity.

Liquidity and refinancing. Evidence: cash of 40,118, an undrawn 650,000 revolver maturing June 29, 2027, maturities of 584,150 in 2027 and 1,002,775 in 2028, and the stated search for a revolver extension or refinancing. Mechanism: the revolver is secured on 55 properties and its availability depends on collateral performance, value and covenants, including a fixed charge coverage minimum of 1.30x that the pack does not report against. Implication: the 2027 wall (revolver expiry and the zero coupon notes) is the near-term pressure point. The two six-month extension options require a fee and a 1.50x fixed charge coverage ratio for the first extension, a test the pack gives no figure for.

Structure. Evidence: secured principal (senior secured notes plus mortgage notes) of 2,927,322 against unsecured notes of 1,725,000, of which 1,225,000 is not guaranteed. Mechanism: unsecured and unguaranteed creditors sit behind secured claims on the best assets and behind subsidiary-level claims. Implication: recovery for the 1,225,000 of unguaranteed unsecured notes depends on residual value after secured claims; the indenture test of unencumbered assets to unsecured debt at 273.2% shows asset cover on the company's definition but is not a recovery estimate.

## Calculations

All inputs are in USD thousands as printed and locators are page chunks. Rounding is to two decimals for ratios.

### Core EBITDA

Definition: total revenues less hotel operating expenses, less net lease operating expenses, less general and administrative, less transaction related costs. Equivalent to net loss plus income tax plus interest expense plus depreciation and amortization less interest income plus impairment plus loss on sales plus early extinguishment loss plus equity in losses of an investee. The company reports no EBITDA, so this is an analyst-defined proxy.

| Period | Revenues | Hotel opex | Net lease opex | G&A | Transaction costs | Core EBITDA |
| --- | --- | --- | --- | --- | --- | --- |
| FY2025 (10-K FY2025 page:172) | 1,814,838 | 1,226,542 | 21,597 | 40,667 | 14,698 | 1,814,838 - 1,226,542 - 21,597 - 40,667 - 14,698 = 511,334 |
| FY2024 (10-K FY2025 page:172) | 1,896,928 | 1,274,153 | 19,817 | 40,239 | 6,894 | 555,825 |
| Q1 2026 (10-Q Q1 page:3) | 364,451 | 242,644 | 7,440 | 8,796 | 2,509 | 103,062 |
| Q1 2025 (10-Q Q1 page:3) | 435,179 | 305,840 | 5,628 | 9,556 | 111 | 114,044 |
| Six months 2026 (10-Q Q2 page:3) | 785,425 | 507,298 | 13,486 | 19,889 | 2,972 | 241,780 |
| Six months 2025 (10-Q Q2 page:3) | 938,615 | 634,753 | 11,067 | 19,774 | 1,456 | 271,565 |
| Q2 2026 (10-Q Q2 page:3) | 420,974 | 264,654 | 6,046 | 11,093 | 463 | 138,718 |
| Q3 2026 (10-Q Q3 page:3) | 399,520 | 255,780 | 6,389 | 9,965 | 1,857 | 125,529 |
| Nine months 2026 (10-Q Q3 page:3) | 1,184,945 | 763,078 | 19,875 | 29,854 | 4,829 | 367,309 |
| Nine months 2025 (10-Q Q3 page:3) | 1,417,385 | 963,111 | 16,303 | 30,831 | 4,139 | 403,001 |

LTM core EBITDA:

- LTM Q1 2026 = 511,334 + 103,062 - 114,044 = 500,352.
- LTM Q2 2026 = 511,334 + 241,780 - 271,565 = 481,549.
- LTM Q3 2026 = 511,334 + 367,309 - 403,001 = 475,642.

Cross-check: the three 2026 quarters sum to 103,062 + 138,718 + 125,529 = 367,309, which equals the nine-month figure.

### LTM cash interest

- FY2025 = 379,566 (10-K FY2025 page:174).
- LTM Q1 2026 = 379,566 + 51,049 - 46,795 = 383,820 (10-Q Q1 page:4).
- LTM Q2 2026 = 379,566 + 158,873 - 185,533 = 352,906 (10-Q Q2 page:5).
- LTM Q3 2026 = 379,566 + 196,080 - 239,155 = 336,491 (10-Q Q3 page:5).

### Principal debt, net debt and leverage

| Date | Components (USD thousands) | Principal debt | Unrestricted cash | Net debt |
| --- | --- | --- | --- | --- |
| December 31, 2025 | 3,275,000 + 1,580,155 + 604,654 + 45,000 (variable funding note) (10-K FY2025 page:194 and page:197) | 5,504,809 | 346,813 | 5,157,996 |
| March 31, 2026 | 2,275,000 + 1,580,155 + 1,349,164 + 45,000 (10-Q Q1 page:16) | 5,249,319 | 19,294 | 5,230,025 |
| June 30, 2026 | 25,000 + 1,725,000 + 1,580,155 + 1,348,166 + 45,000 (10-Q Q2 page:19) | 4,723,321 | 5,511 | 4,717,810 |
| September 30, 2026 | 1,725,000 + 1,580,155 + 1,347,167 (10-Q Q3 page:20) | 4,652,322 | 40,118 | 4,612,204 |

The December 31, 2025 total agrees with the printed maturity table total of 5,504,809 (10-K FY2025 page:198), and the September 30, 2026 total with the printed 4,652,322 (10-Q Q3 page:49).

Leverage ratios:

- FY2025: 5,504,809 / 511,334 = 10.77x; 5,157,996 / 511,334 = 10.09x.
- LTM Q1 2026: 5,249,319 / 500,352 = 10.49x; 5,230,025 / 500,352 = 10.45x.
- LTM Q2 2026: 4,723,321 / 481,549 = 9.81x; 4,717,810 / 481,549 = 9.80x.
- LTM Q3 2026: 4,652,322 / 475,642 = 9.78x; 4,612,204 / 475,642 = 9.70x.

Interest cover: 511,334 / 379,566 = 1.35x; 500,352 / 383,820 = 1.30x; 481,549 / 352,906 = 1.36x; 475,642 / 336,491 = 1.41x. FY2024: 555,825 / 366,194 = 1.52x.

Secured share of principal debt at September 30, 2026: (1,580,155 + 1,347,167) = 2,927,322; 2,927,322 / 4,652,322 = 62.9%, stated as 63%. This counts the net lease mortgage notes as secured and excludes the undrawn revolver.

Debt reduction: 5,504,809 - 4,652,322 = 852,487.

Fixed-rate run-rate interest: 263,082 / 4,652,322 = 5.65% average annual cash coupon (excludes zero coupon accretion and amortization of costs).

Check of the indenture ratio from printed components: 4,652,322 / 8,631,686 = 53.9%, which agrees with the reported 53.9% (adjusted total assets from 10-Q Q3 page:51). Unencumbered assets 4,093,665 + 456,711 + 162,366 = 4,712,742; 4,712,742 / 1,725,000 = 273.2%, which agrees with the reported 273.2%.

### Liquidity

- September 30, 2026: unrestricted cash 40,118 + undrawn revolver 650,000 = 690,118. No letters of credit or other deductions were found in the sources. The variable funding note was terminated so adds none.
- December 31, 2025: 346,813 + 650,000 = 996,813.
- March 31, 2026: 19,294 + 650,000 = 669,294.
- June 30, 2026: 5,511 + 625,000 = 630,511. Revolver availability is 650,000 less 25,000 drawn (10-Q Q2 page:19).
- Near-term uses (not netted in the liquidity figure): distribution of about 6,491 due about November 12, 2026; expected capital spending of 25,000 to 40,000 in the last quarter of 2026; 2027 maturities of 584,150. Sum of the 2027 maturities and cash on hand: 584,150 - 40,118 = 544,032 to be funded by other sources, before the revolver's own June 29, 2027 expiry.

### Cash flow and LTM operating lines

- LTM net cash from operations = 117,808 + 132,226 - 136,305 = 113,729.
- LTM real estate improvements = 224,833 + 110,062 - 148,154 = 186,741. LTM operating cash flow less real estate improvements = 113,729 - 186,741 = -73,012.
- LTM total revenues = 1,814,838 + 1,184,945 - 1,417,385 = 1,582,398.
- LTM hotel revenue = 1,413,403 + 883,025 - 1,116,944 = 1,179,484.
- LTM rental income = 401,435 + 301,920 - 300,441 = 402,914.
- LTM net loss = 202,321 + 462,956 - 201,539 = 463,738 (a loss).
- LTM interest expense = 413,614 + 270,134 - 311,972 = 371,776.
- LTM impairment = 81,889 + 270,883 - 81,788 = 270,984.
- LTM depreciation and amortization = 314,963 + 225,078 - 238,583 = 301,458.
- LTM net proceeds from sales = 853,046 + 84,500 - 331,202 = 606,344.

### Covenant headroom

- Total debt to adjusted total assets: 60% - 53.9% = 6.1 points.
- Secured debt to adjusted total assets: 40% - 33.9% = 6.1 points.
- Income available for debt service to debt service: 1.83x - 1.50x = 0.33x.
- Unencumbered assets to unsecured debt: 273.2% - 150% = 123.2 points.
- Guarantor unencumbered assets to guaranteed unsecured debt: 8.79x - 2.20x = 6.59x.
- Revolver fixed charge coverage and debt yield: Not calculable, because the reported figures are not printed.

## Gaps

| Gap | Severity | Consumer and effect | Remediation |
| --- | --- | --- | --- |
| The company reports no EBITDA; core EBITDA is calculated here and includes earnings of hotels since sold and the straight line rent adjustment. | High | Leverage and cover charts; forward leverage on the retained portfolio is not shown | Obtain a pro forma EBITDA for retained assets if the company publishes one; otherwise carry the limitation |
| Revolver fixed charge coverage and collateral debt yield: terms are printed in the 10-K only and no reported ratio exists in any source. | High | Headroom on the only liquidity facility is Not calculable | Obtain the credit agreement and compliance certificates |
| Revolver matures June 29, 2027, within twelve months of the as-of date; extension or refinancing is being explored and not agreed. | High | Liquidity chart; treat availability as time-limited | Monitor for an amendment or replacement facility |
| Maturity month of the zero coupon senior secured notes due 2027 and the collateral and guarantors of the 8.625% secured notes due 2031 were not found after searching. | Medium | Maturity timing within 2027 and recovery waterfall | Obtain the indentures |
| September 30, 2026 operating lease liability and principal debt at December 31, 2024 were not found. | Low | Claims outside debt; FY2024 leverage not calculated | Use December 31, 2025 lease figure as an indication only |
| Discrete Q2 and Q3 2026 cash flow lines are not printed; only six-month and nine-month totals. | Low | Quarterly cash flow rows show Not supplied | Derive by difference downstream if needed |
| Interim statements are unaudited, and hotel operating statistics are provided by managers and not independently verified by the company. | Medium | Hotel KPIs and interim figures | Cross-check to audited year-end |
| Share counts mix split-adjusted (Q2, Q3) and unadjusted (10-K, Q1) bases; per-share figures were not used. | Low | Per-share metrics | Use the Q3 10-Q adjusted figures |
| No letters of credit, pensions, factoring or supply-chain finance were found; these absences rest on text search, not on a statement that none exist. | Low | Claims outside debt | None required |
| The Trust's ratings and market values are blank in the context. | Low | Relative value and market-based leverage | Supply ratings and market data if wanted |

## Next module

Proceed to CP-1A (business and transaction context) and then CP-2. CP-1A should take the portfolio mix, TravelCenters of America concentration (68.2% of annualized minimum rent), the Sonesta hotel management arrangements and RMR management and change-of-control terms from the Q3 10-Q and 10-K, and use the debt table above for the transaction summary. CP-2 should carry forward the limits stated here: core EBITDA is an analyst proxy that includes sold hotels, the revolver matures June 29, 2027 with unreported covenant headroom, and the correction to the upstream readiness handoff on revolver covenant terms.
