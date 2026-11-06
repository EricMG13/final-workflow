## Request

Issuer: GENESIS ENERGY LP (registrant name in the filings: Genesis Energy, L.P.; issuer id gel; ticker GEL). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency per the run settings: USD. Current period Q3 2026 (quarter ended September 30, 2026); prior period FY2025.

Scope of this handoff: the financial base for the requested downstream modules. It extracts the statements, reviews definitions of EBITDA and covenant measures, builds the debt, liquidity and maturity registers, computes leverage and interest cover from printed components, reviews claims outside reported debt, and states what the evidence can and cannot support. It uses only the pinned sources and the accepted CP-0 handoff. Nothing is taken from outside the sources. Money is in US dollars. Tables of statement lines are in thousands of dollars as the filings print them; the four chart tables are in US$m or x as their headers say.

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 | Document family and period |
| --- | --- | --- |
| 10-K_2025-12-31_gel-20251231.htm.jsonl | ccb89bebbe1f6460b65cf41694753b9c46d6084fa3c93974775412b94a4649f8 | Form 10-K, fiscal year ended December 31, 2025 (audited) |
| 10-Q_2026-03-31_gel-20260331.htm.jsonl | 25844b5fb23f8fb7e6ed5e3ecd46a1d84117c9d80e65e2ca8d092544b9bdbfa5 | Form 10-Q, quarter ended March 31, 2026 (unaudited) |
| 10-Q_2026-06-30_gel-20260630.htm.jsonl | abd4ada77d59922e6f0bafe2fa139c2cc408c45768d2e839399c3eb81593724d | Form 10-Q, quarter ended June 30, 2026 (unaudited) |
| 10-Q_2026-09-30_gel-20260930.htm.jsonl | b8ecb63006d005d24876220dffec5b55d573a9ed4071631f5d65780aeca8bd64 | Form 10-Q, quarter ended September 30, 2026 (unaudited) |
| EX-99.1_2026-05-07_a90ex9918kearnings_q12026.htm.jsonl | dacbb1e9e5b2b770bd5cf7b317240e0ada11d6948f3a4f941eec0c98544a6e5d | Exhibit 99.1 earnings release, May 7, 2026 |
| EX-99.1_2026-08-06_a90ex9918kearnings_q22026.htm.jsonl | e543ee3e3398ce04f2a72be94919a9105edf4587f39625f574d75860af788168 | Exhibit 99.1 earnings release, August 6, 2026 |
| EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | c64ffa295db0861a2124c70f86ea927a2ba296a55d07643ed60b307a769d0d5c | Exhibit 99.1 earnings release, November 5, 2026 |

### Run settings (not issuer evidence)

| Item | sha256 | Use |
| --- | --- | --- |
| context (/workspace/secdata/data/2026-11-05/contexts/1022321-genesis-energy-lp-gel.json) | df9790453496c7c6915bcace0e2562d4cd49506ea6a01ef11c0fdc0b1c2fef47 | Dated settings only (as-of 2026-11-05, current period q3-2026, prior period fy-2025, USD). Market capitalization, net debt, EV, peers, ratings and deal terms are blank in the context; blank is not zero. |

### Supplied handoffs

| Module | sha256 | How it is used |
| --- | --- | --- |
| CP-0 | 4b65b01575675a608bc6fc6997ea8b40b64b585c6caafd62892d7c3a4a40acae | Source readiness. Its limitations are carried forward below: the credit agreement, note indentures and guarantor list are not supplied; cash and inventory-financing items differ between the Q3 10-Q and the Q3 release; the AR Facility sits inside balance sheet debt but outside the release's Adjusted Debt; the 10-K describes the superseded credit agreement; the 2025 comparatives separate the discontinued Alkali Business. |

CP-0 rated this module's source set READY_WITH_LIMITATIONS. This handoff confirms that reading and does not correct any CP-0 statement. In "page:N" the page is the extracted chunk, not the printed page.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Genesis carries about 5.18x total debt to EBITDA on a computed basis, with 2.36x EBITDA to cash interest, but has $41.477 million cash and $894.4 million of undrawn revolver and no maturity before 2029. | Medium | The covenant ratio and its inputs are management figures; the credit agreement is not supplied and FY2025 adjusted EBITDA is not printed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Funded debt principal rose to $3,249.5 million from $3,085.760 million at year end while preferred units were bought back with debt and asset-sale proceeds. | Senior claims grew while a more expensive but junior preferred claim shrank; deleveraging has not yet shown in the debt balance. | High |
| The reported covenant leverage ratio of 5.03x sits below the 5.75x maximum, and the release's own inputs imply an EBITDA cushion of about 12.5%. | Compliance headroom is real but modest, and it depends on definitions held in documents not supplied. | Medium |
| Operating cash flow of $340.898 million in nine months of 2026 includes a $58.619 million working capital inflow and a large receivables gross-up. | Cash generation is partly timing; the AR Facility is fully drawn against receivables. | Medium |
| Liquidity is revolver-based with the revolver subject to covenants, and notes mature from January 2029. | Near-term refinancing risk is low; revolver access depends on staying inside the leverage test. | Medium |

### Financial base view

The financial base is usable for the requested work, with limitations. Audited FY2025 statements, three unaudited 2026 interim statements and three releases give consistent continuing-operations figures for the consolidated partnership, and every figure in the tables below is printed in, or calculated from, those sources. On a computed basis (operating income plus depreciation and amortization plus equity in earnings, less the 2026 asset-sale gain) LTM Q3 2026 EBITDA is 626.898 US$m, total debt to EBITDA is 5.18x, net debt to EBITDA is 5.12x and EBITDA to cash interest paid is 2.36x. Management reports a covenant leverage ratio of 5.03x, which uses a different debt and EBITDA perimeter. The two bases must not be mixed: the computed basis is consolidated and gross of noncontrolling interests, while management's Adjusted EBITDA is net to Genesis' ownership. Funded debt is $3,150.000 million of senior unsecured notes plus a $99.500 million AR Facility, with no revolver borrowings at September 30, 2026. Liquidity at that date is $41.477 million of unrestricted cash plus $894.4 million of revolver availability, subject to covenant compliance. Limitations that restrict conclusions: the credit agreement and indentures are not supplied; FY2025 adjusted EBITDA and a covenant ratio at December 31, 2025 are not printed; FY2025 cash flows are consolidated and include the discontinued Alkali Business for January and February 2025; and the Q3 10-Q and the Q3 release disagree on two inputs to the management leverage ratio.

### Source context

All sources are for one entity and one perimeter. The four strings below apply word for word to every financial scope in this handoff.

| Item | Value |
| --- | --- |
| Entity perimeter | Genesis Energy, L.P. and its consolidated subsidiaries (continuing operations; the Alkali Business is shown separately as discontinued operations for 2025) |
| Accounting basis | US GAAP as filed (10-K audited; 10-Qs unaudited); management non-GAAP measures from the releases are labelled as such |
| Currency | USD |
| Unit | thousands of US dollars, except per-unit amounts and where a table header says US$m or x |

| Source | Statement kinds | Period and instant dates | Version relationship | Can support extraction |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31_gel-20251231.htm.jsonl | Balance sheet page:166; operations pages:166-167; cash flows pages:168-169; debt note page:191; segments pages:207-209; supplemental cash flow page:210 | FY2025, FY2024, FY2023; instants December 31, 2025 and 2024 | Audited; the Alkali Business is discontinued operations | Yes |
| 10-Q_2026-03-31_gel-20260331.htm.jsonl | Balance sheet page:2; operations page:3; debt note pages:12-14 | Quarter to March 31, 2026 and 2025; instant March 31, 2026 | Unaudited; successor to the 10-K | Yes |
| 10-Q_2026-06-30_gel-20260630.htm.jsonl | Balance sheet page:2; operations page:3; debt note pages:15-18 | Quarter and six months to June 30, 2026 and 2025; instant June 30, 2026 | Unaudited | Yes |
| 10-Q_2026-09-30_gel-20260930.htm.jsonl | Balance sheet page:2; operations page:3; cash flows pages:5-6; debt note pages:14-19; segments pages:25-27 | Quarter and nine months to September 30, 2026 and 2025; instant September 30, 2026 | Unaudited; latest filing | Yes |
| EX-99.1_2026-05-07_a90ex9918kearnings_q12026.htm.jsonl, EX-99.1_2026-08-06_a90ex9918kearnings_q22026.htm.jsonl, EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | Non-GAAP reconciliations, adjusted debt-to-adjusted consolidated EBITDA tables | Quarter, year-to-date and trailing twelve months at each quarter end | Management releases; filings control | Yes, as attributed management measures |

Extraction note: statement rows are flattened text. Every figure below was read from the cited page and cross-footed (cross-footing is shown in Calculations).

### Financials and credit metrics

| Metric | FY2025 | Q3 2026 | Q3 2025 | 9M 2026 | 9M 2025 | LTM Q3 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenues | 1,630,415 | 449,251 | 414,001 | 1,427,801 | 1,189,660 | 1,868,556 | Printed: 10-K_2025-12-31_gel-20251231.htm.jsonl page:166; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3. LTM calculated. |
| Operating income | 258,190 | 69,406 | 78,591 | 251,455 | 168,279 | 341,366 | Printed: 10-K_2025-12-31_gel-20251231.htm.jsonl page:166; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3. LTM calculated. |
| Depreciation and amortization | 232,072 | 60,958 | 57,068 | 183,000 | 169,144 | 245,928 | Printed: 10-K_2025-12-31_gel-20251231.htm.jsonl page:166; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3. LTM calculated. |
| Equity in earnings of equity investees | 47,629 | 12,556 | 10,845 | 45,078 | 35,667 | 57,040 | Printed: 10-K_2025-12-31_gel-20251231.htm.jsonl page:167; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3. LTM calculated. |
| Gain on sale of assets (in costs; negative reduces costs) | Not supplied: no such line in FY2025 | — (printed nil) | — (printed nil) | (17,436) | — (printed nil) | (17,436) | Printed: 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3 |
| EBITDA (computed: operating income + D&A + equity in earnings - gain on sale) | 537,891 | 142,920 | 146,504 | 462,097 | 373,090 | 626,898 | Calculated; see Calculations. Consolidated, before noncontrolling interests. |
| Interest expense, net | (264,729) | (67,275) | (66,407) | (202,207) | (197,199) | (269,737) | Printed: 10-K_2025-12-31_gel-20251231.htm.jsonl page:167; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3. LTM calculated. |
| Net income from continuing operations | 30,505 | 14,414 | 22,776 | 90,162 | (3,774) | 124,441 | Printed: 10-K_2025-12-31_gel-20251231.htm.jsonl page:167; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3. LTM calculated. |
| Net income (loss) attributable to Genesis Energy, L.P. | (440,403) | 2,415 | 9,207 | 52,072 | (460,274) | 71,943 | Printed: 10-K_2025-12-31_gel-20251231.htm.jsonl page:167; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3. FY2025 and 9M 2025 include the discontinued-operations loss. LTM mixes bases and is shown for completeness only. |
| Total Segment Margin (management measure) | 577,853 | 147,206 | 146,576 | 473,128 | 403,840 | 647,141 | Printed: 10-K_2025-12-31_gel-20251231.htm.jsonl page:208; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:26. LTM calculated. |
| Adjusted EBITDA (management measure, net to Genesis ownership) | Not supplied: the 10-K does not present Adjusted EBITDA | 130,502 | 131,957 | 442,897 | 386,535 | Not calculable: FY2025 Adjusted EBITDA is not printed | Printed: EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:10. |
| Cash flows from operating activities | 252,826 | 78,414 | 70,252 | 340,898 | 142,044 | 451,680 | Printed: 10-K_2025-12-31_gel-20251231.htm.jsonl page:168; EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:10. FY2025 and 9M 2025 include discontinued operations. |
| Payments to acquire fixed and intangible assets | (186,888) | Not supplied: quarterly capex not printed in the sources read | Not supplied: quarterly capex not printed in the sources read | (84,996) | (163,108) | (108,776) | Printed: 10-K_2025-12-31_gel-20251231.htm.jsonl page:168; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:5. |
| Payments of interest and commitment fees (US$m, as printed) | 282.4 | Not supplied: quarterly amount not printed | Not supplied: quarterly amount not printed | 190.0 | 206.3 | 266.1 | Printed: 10-K_2025-12-31_gel-20251231.htm.jsonl page:210; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:29. LTM calculated. |
| Total debt principal at period end (US$m) | 3,085.760 | 3,249.500 | Not supplied: prior-year instant not extracted | 3,249.500 | Not supplied: prior-year instant not extracted | 3,249.500 | Instants: 10-K_2025-12-31_gel-20251231.htm.jsonl page:191; 10-Q_2026-09-30_gel-20260930.htm.jsonl pages:14-15. Includes the 99.500 AR Facility in 2026. |
| Unrestricted cash at period end (US$m) | 6.437 | 41.477 | Not supplied: prior-year instant not extracted | 41.477 | Not supplied: prior-year instant not extracted | 41.477 | Instants: 10-K_2025-12-31_gel-20251231.htm.jsonl page:166; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:2. |
| Total debt / EBITDA (x, computed) | 5.74 | Not calculable: ratio needs an annual or LTM base | Not calculable: ratio needs an annual or LTM base | Not calculable: ratio needs an annual or LTM base | Not calculable: ratio needs an annual or LTM base | 5.18 | Calculated at December 31, 2025 and September 30, 2026. |
| Net debt / EBITDA (x, computed) | 5.72 | Not calculable: ratio needs an annual or LTM base | Not calculable: ratio needs an annual or LTM base | Not calculable: ratio needs an annual or LTM base | Not calculable: ratio needs an annual or LTM base | 5.12 | Calculated at December 31, 2025 and September 30, 2026. |
| EBITDA / cash interest (x, computed) | 1.90 | Not calculable: ratio needs an annual or LTM base | Not calculable: ratio needs an annual or LTM base | Not calculable: ratio needs an annual or LTM base | Not calculable: ratio needs an annual or LTM base | 2.36 | Calculated. |
| Covenant leverage ratio as reported by management (x) | Not supplied: first reported with the Q1 2026 release | 5.03 | Not supplied: not reported | Not calculable: point-in-time LTM measure | Not supplied: not reported | 5.03 | Printed: EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:1 and page:11. Management measure under the credit agreement. |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 5.74 | 5.72 | x | Debt principal of 3,085.760 US$m at December 31, 2025 over computed FY2025 EBITDA of 537.891 US$m; unrestricted cash of 6.437 US$m. Continuing operations; consolidated, gross of noncontrolling interests. |
| LTM Q1 2026 | 5.40 | 5.39 | x | Debt principal of 3,224.100 US$m (notes plus 74.100 revolver) over LTM EBITDA of 596.939 US$m; cash of 4.210 US$m. LTM equals FY2025 plus Q1 2026 less Q1 2025. |
| LTM Q2 2026 | 5.15 | 5.09 | x | Debt principal of 3,249.500 US$m (notes plus 99.500 AR Facility) over LTM EBITDA of 630.482 US$m; cash of 39.261 US$m. The 2026 gain on sale is excluded from EBITDA. |
| LTM Q3 2026 | 5.18 | 5.12 | x | Debt principal of 3,249.500 US$m over LTM EBITDA of 626.898 US$m; cash of 41.477 US$m (restricted cash of 4.975 US$m excluded). Management's covenant ratio is 5.03x on a different perimeter; not comparable. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 1.90 | x | Computed FY2025 EBITDA of 537.891 US$m over payments of interest and commitment fees of 282.4 US$m. The cash figure is consolidated and may include Alkali Business interest for January and February 2025 (the Alkali Business reported 4,179 thousand of interest expense in 9M 2025); the EBITDA is continuing operations only, so the ratio may be understated. |
| LTM Q1 2026 | 2.23 | x | LTM EBITDA of 596.939 US$m over LTM cash interest of 268.1 US$m (282.4 plus 59.0 less 73.3). |
| LTM Q2 2026 | 2.37 | x | LTM EBITDA of 630.482 US$m over LTM cash interest of 266.2 US$m (282.4 plus 135.9 less 152.1). |
| LTM Q3 2026 | 2.36 | x | LTM EBITDA of 626.898 US$m over LTM cash interest of 266.1 US$m (282.4 plus 190.0 less 206.3). The covenant interest coverage test uses credit-agreement definitions; the reported covenant figure is not supplied. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2025 | 6.437 | 788.6 | US$m | Revolver availability as printed (800 US$m facility less 6.4 borrowed and 5.0 letters of credit); subject to covenant compliance. No AR Facility existed. |
| Mar 31, 2026 | 4.210 | 819.1 | US$m | Revolver availability as printed (900 US$m facility less 74.1 borrowed and 6.8 letters of credit); subject to covenant compliance. |
| Jun 30, 2026 | 39.261 | 894.4 | US$m | Revolver availability as printed (900 US$m facility less 5.6 letters of credit, no borrowings); the 99.5 US$m AR Facility is fully drawn so adds no undrawn capacity; restricted cash of 4.975 US$m excluded. |
| Sep 30, 2026 | 41.477 | 894.4 | US$m | Revolver availability as printed (900 US$m facility less 5.6 letters of credit, no borrowings); the 99.5 US$m AR Facility is fully drawn; restricted cash of 4.975 US$m excluded. Revolver springing maturities and covenants apply. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remainder of 2026 | 0 | US$m | No instrument in the September 30, 2026 debt table matures in 2026. |
| 2027 | 0 | US$m | No instrument matures in 2027. |
| 2028 | 0 | US$m | No instrument matures in 2028; the revolver would mature on October 16, 2028 if more than 150 US$m of the 2029 notes remain outstanding then (springing, undrawn). |
| 2029 | 699.5 | US$m | 8.250% notes due January 15, 2029 (600.0) plus the AR Facility (99.5) that expires June 26, 2029. The AR Facility is classified as a current borrowing on the balance sheet; management states "nothing maturing until January 15, 2029". |
| 2030 | 500.0 | US$m | 8.875% notes due April 15, 2030. The revolver would mature January 14, 2030 if more than 150 US$m of these notes remain outstanding then (springing, undrawn). |
| 2031 | 0 | US$m | Revolver expires March 4, 2031 (900 US$m commitment, no borrowings); no drawn debt matures. |
| 2032 | 700.0 | US$m | 7.875% notes due May 15, 2032. |
| 2033 | 600.0 | US$m | 8.000% notes due May 15, 2033. |
| 2034 | 750.0 | US$m | 6.750% notes due March 15, 2034. Total across the rows is 3,249.5 US$m, equal to total debt principal. |

### Statement extraction: income statement (continuing operations)

Printed in thousands of dollars. Costs are shown as the statements show them. Locators: 10-K_2025-12-31_gel-20251231.htm.jsonl pages:166-167; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3.

| Line | FY2025 | 9M 2026 | 9M 2025 | Q3 2026 | Q3 2025 |
| --- | --- | --- | --- | --- | --- |
| Offshore pipeline transportation revenue | 531,898 | 446,060 | 377,563 | 138,632 | 143,306 |
| Marine transportation revenue | 319,498 | 251,052 | 237,319 | 90,064 | 77,058 |
| Onshore transportation and services revenue | 779,019 | 730,689 | 574,778 | 220,555 | 193,637 |
| Total revenues | 1,630,415 | 1,427,801 | 1,189,660 | 449,251 | 414,001 |
| General and administrative | 86,339 | 55,315 | 70,674 | 18,344 | 15,288 |
| Depreciation and amortization | 232,072 | 183,000 | 169,144 | 60,958 | 57,068 |
| Gain on sale of assets | Not supplied: no such line | (17,436) | — (printed nil) | — (printed nil) | — (printed nil) |
| Total costs and expenses | 1,372,225 | 1,176,346 | 1,021,381 | 379,845 | 335,410 |
| Operating income | 258,190 | 251,455 | 168,279 | 69,406 | 78,591 |
| Equity in earnings of equity investees | 47,629 | 45,078 | 35,667 | 12,556 | 10,845 |
| Interest expense, net | (264,729) | (202,207) | (197,199) | (67,275) | (66,407) |
| Other expense | (9,779) | (3,570) | (9,779) | — (printed nil) | — (printed nil) |
| Income (loss) from continuing operations before income taxes | 31,311 | 90,756 | (3,032) | 14,687 | 23,029 |
| Income tax expense | (806) | (594) | (742) | (273) | (253) |
| Net income (loss) from continuing operations | 30,505 | 90,162 | (3,774) | 14,414 | 22,776 |
| Net loss from discontinued operations, net of tax | (423,745) | — (printed nil) | (423,745) | — (printed nil) | — (printed nil) |
| Net income attributable to noncontrolling interests | (47,163) | (38,090) | (32,755) | (11,999) | (13,569) |
| Net income (loss) attributable to Genesis Energy, L.P. | (440,403) | 52,072 | (460,274) | 2,415 | 9,207 |

Expense block reconciliation. For this by-function-by-segment statement the block between revenue and operating income is the sum of segment operating costs, onshore product costs, general and administrative, depreciation and amortization and the 2026 gain. It foots to the printed total costs and expenses and to operating income in each period (see Calculations, cross-foot checks). No difference remains unresolved.

### Statement extraction: balance sheet

Printed in thousands of dollars; each column is an instant. Locators: 10-K_2025-12-31_gel-20251231.htm.jsonl page:166; 10-Q_2026-03-31_gel-20260331.htm.jsonl pages:2-3; 10-Q_2026-06-30_gel-20260630.htm.jsonl pages:2-3; 10-Q_2026-09-30_gel-20260930.htm.jsonl pages:2-3.

| Line | Dec 31, 2025 | Mar 31, 2026 | Jun 30, 2026 | Sep 30, 2026 |
| --- | --- | --- | --- | --- |
| Cash and cash equivalents | 6,437 | 4,210 | 39,261 | 41,477 |
| Restricted cash | — (printed nil) | Not supplied: no such line | 4,975 | 4,975 |
| Accounts receivable - trade, net | 608,221 | 628,603 | 1,189,516 | 1,053,898 |
| Inventories | 55,366 | 39,224 | 38,589 | 22,795 |
| Other current assets | 17,442 | 30,782 | 27,050 | 23,631 |
| Total current assets | 687,466 | 702,819 | 1,299,391 | 1,146,776 |
| Net fixed assets | 3,465,323 | 3,431,322 | 3,401,858 | 3,372,141 |
| Equity investees | 218,631 | 215,610 | 219,542 | 212,880 |
| Intangible assets, net | 75,606 | 73,323 | 70,975 | 68,659 |
| Goodwill | 301,959 | 301,959 | 301,959 | 301,959 |
| Right of use assets, net | 57,670 | 56,839 | 59,963 | 60,966 |
| Other assets, net | 54,048 | 54,842 | 59,069 | 65,172 |
| Total assets | 4,860,703 | 4,836,714 | 5,412,757 | 5,228,553 |
| Accounts payable - trade | 490,712 | 508,348 | 1,096,530 | 927,687 |
| Accrued liabilities | 208,980 | 212,355 | 203,003 | 225,832 |
| Accounts receivable securitization credit facility | — (printed nil) | Not supplied: no such line | 99,500 | 99,500 |
| Total current liabilities | 699,692 | 720,703 | 1,399,033 | 1,253,019 |
| Senior secured credit facility | 6,400 | 74,100 | — (printed nil) | — (printed nil) |
| Senior unsecured notes, net of costs and discount | 3,040,415 | 3,102,076 | 3,104,316 | 3,106,655 |
| Deferred tax liabilities | 17,405 | 17,217 | 17,126 | 17,099 |
| Other long-term liabilities | 388,707 | 387,112 | 439,456 | 433,015 |
| Total liabilities | 4,152,619 | 4,301,208 | 4,959,931 | 4,809,788 |
| Class A Convertible Preferred Units (mezzanine) | 552,523 | 411,547 | 325,146 | 325,146 |
| Common unitholders | (314,346) | (343,173) | (336,836) | (367,614) |
| Noncontrolling interests | 469,907 | 467,132 | 464,516 | 461,233 |
| Total partners' capital | 155,561 | 123,959 | 127,680 | 93,619 |

Instant treatment: balance sheet columns are instants with no start date. Lines the standard account list does not name (right of use assets, the AR Facility, mezzanine preferred units) are kept under their own labels. A dash printed in a filing is shown as printed nil; the words no such line mean the filing prints no row.

### Statement extraction: cash flows

Printed in thousands of dollars. Locators: 10-K_2025-12-31_gel-20251231.htm.jsonl pages:168-169; 10-Q_2026-09-30_gel-20260930.htm.jsonl pages:5-6.

| Line | FY2025 | 9M 2026 | 9M 2025 |
| --- | --- | --- | --- |
| Net cash provided by operating activities | 252,826 | 340,898 | 142,044 |
| Net changes in components of operating assets and liabilities | (89,185) | 58,619 | (90,379) |
| Payments to acquire fixed and intangible assets | (186,888) | (84,996) | (163,108) |
| Proceeds from disposal of discontinued operations, net of cash divested | 996,642 | — (printed nil) | 996,642 |
| Proceeds from asset sales | 1,039 | 10,199 | 970 |
| Net cash provided by (used in) investing activities | 832,294 | (68,861) | 851,851 |
| Borrowings on senior secured credit facility | 866,600 | 789,900 | 664,900 |
| Repayments on senior secured credit facility | (1,151,200) | (796,300) | (897,300) |
| Borrowings on accounts receivable securitization credit facility | Not supplied: no such line | 99,500 | — (printed nil) |
| Proceeds from issuance of senior unsecured notes | — (printed nil) | 750,000 | — (printed nil) |
| Repayment of senior unsecured notes | (414,370) | (679,933) | (414,370) |
| Redemption of Class A Convertible Preferred Units | (262,500) | (221,594) | (262,500) |
| Distributions to Class A Convertible Preferred unitholders | (71,572) | (38,946) | (56,704) |
| Distributions to common unitholders | (80,828) | (68,531) | (60,621) |
| Distributions to noncontrolling interests | (58,527) | (53,442) | (39,447) |
| Contributions from noncontrolling interests | 68,454 | 6,678 | 48,652 |
| Net cash used in financing activities | (1,108,235) | (232,022) | (1,018,532) |
| Cash, cash equivalents and restricted cash at end of period | 6,437 | 46,452 | 4,915 |

### Debt and facility register at September 30, 2026

| Instrument | Issuer and ranking | Principal (US$m) | Rate | Maturity | Security and guarantors | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| AR Facility | Genesis Energy, L.P. through Genesis AR LLC, a bankruptcy-remote consolidated special purpose entity | 99.500 | Term SOFR plus 1.375%; unused fee 0.35% | Expires June 26, 2029; classified current | Secured by eligible receivables sold to Genesis AR LLC; those receivables are not available to other creditors; Genesis AR LLC is a non-guarantor | 10-Q_2026-09-30_gel-20260930.htm.jsonl pages:15-16 |
| Senior secured revolving credit facility | Genesis Energy, L.P., borrower | 0.000 drawn on a 900 US$m commitment | Term SOFR plus 3.25% (alternate base rate plus 2.25%); commitment fee 0.50% | March 4, 2031, with springing earlier dates (October 16, 2028 and January 14, 2030) | Described as senior secured; collateral and guarantors are in documents not supplied | 10-Q_2026-09-30_gel-20260930.htm.jsonl pages:16-18 |
| 8.250% senior unsecured notes | Genesis Energy, L.P. and Genesis Energy Finance Corporation, co-issuers | 600.000 | 8.250% | January 15, 2029 | Guaranteed by 100% owned domestic subsidiaries, except Genesis AR LLC, Genesis AR Holdings LLC and certain immaterial subsidiaries | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:14 and page:18 |
| 8.875% senior unsecured notes | Same co-issuers | 500.000 | 8.875% | April 15, 2030 | Same guarantors | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:14 |
| 7.875% senior unsecured notes | Same co-issuers | 700.000 | 7.875% | May 15, 2032 | Same guarantors | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:15 |
| 8.000% senior unsecured notes | Same co-issuers | 600.000 | 8.000% | May 15, 2033 | Same guarantors | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:15 |
| 6.750% senior unsecured notes | Same co-issuers | 750.000 | 6.750% | March 15, 2034 | Same guarantors | 10-Q_2026-09-30_gel-20260930.htm.jsonl pages:15, 18 |

Retired in 2026: the 7.750% notes due 2028 (679.360 US$m at December 31, 2025) were purchased in a tender (416.1) and redeemed (263.3) in March 2026 using the 2034 notes. Redemption rights from the 10-K (10-K_2025-12-31_gel-20251231.htm.jsonl page:196): the 2029 notes from January 15, 2026, the 2030 notes from April 15, 2026, the 2032 notes from May 15, 2027 and the 2033 notes from May 15, 2028; call terms of the 2034 notes are not supplied.

### Claims outside reported debt

| Claim | Amount and period | Inside or outside the debt figure | Locator |
| --- | --- | --- | --- |
| Class A Convertible Preferred Units (mezzanine equity) | Carrying value 325,146 thousand at September 30, 2026; 9,236,530 units; distribution of 0.9473 per unit per quarter (3.7892 annualized) | Outside debt; senior to common units for distributions and liquidation; classified as temporary equity because of redemption provisions on a deemed liquidation event | 10-Q_2026-09-30_gel-20260930.htm.jsonl pages:2, 21; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:53 |
| Noncontrolling interests | Balance 461,233 thousand; 9M 2026 net income attributable 38,090 thousand; distributions 53,442 thousand against contributions 6,678 thousand | Outside debt; cash leaves the group to the noncontrolling holder | 10-Q_2026-09-30_gel-20260930.htm.jsonl pages:3, 5-6 |
| Asset retirement obligations | Total 256,656 thousand at September 30, 2026; 24.2 million current, remainder in other long-term liabilities | Outside debt | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:13 |
| Contract liabilities | Long-term 129,487 thousand at September 30, 2026 against 78,946 thousand at December 31, 2025 (contract liabilities; includes consideration received upfront for operation and maintenance services after the June 2026 divestiture) | Outside debt; settled by service performance, not cash | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:9; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:10 |
| Operating lease obligations | Undiscounted payments of 154.1 million and present value of 67,838 thousand at December 31, 2025 (latest printed) | Outside debt | 10-K_2025-12-31_gel-20251231.htm.jsonl page:187; 10-K_2025-12-31_gel-20251231.htm.jsonl page:118 |
| Equity investee debt (Poseidon revolver) | Amount not supplied; the facility is non-recourse to owners | Outside debt; not consolidated as debt | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:14 |
| Pension and retiree medical | Not supplied: no continuing obligation is shown; the benefit plan was held for discontinued operations and disposed | Not applicable to continuing balance sheet | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:5 |
| Purchase and capacity commitments, factoring | Not supplied as a separate amount in the sources read; receivables are sold only to Genesis AR LLC under the AR Facility, which is consolidated | AR Facility inside balance sheet debt | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:16 |
| Litigation | No material developments reported | Not applicable | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:64 |

Other long-term liabilities of 433,015 thousand at September 30, 2026 are not itemised in full. Itemised pieces: non-current asset retirement obligations (about 232,456 thousand, calculated as total less the 24.2 million current) and long-term contract liabilities (129,487 thousand). The remainder of about 71,072 thousand includes non-current lease liabilities and other items and cannot be split from the sources.

### Covenants and definitions review

| Test | Level and step-down | Reported figure | Headroom | Locator |
| --- | --- | --- | --- | --- |
| Maximum consolidated leverage ratio | 5.75x for fiscal quarters ending March 31, 2026 to December 31, 2027; 5.50x thereafter | 5.38x at Q1 2026, 5.00x at Q2 2026, 5.03x at Q3 2026 (management, from releases) | 0.72x at Q3 2026 against the printed ratio; with the release's own adjusted debt of 3,055.602 US$m the EBITDA floor at 5.75x is 531.409 US$m against 607.450 US$m, a cushion of 76.041 US$m or 12.5% | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:17; EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:1 and page:11 |
| Minimum consolidated interest coverage ratio | 2.00x to December 31, 2026; 2.15x in 2027; 2.25x thereafter | Not supplied: no reported figure in the sources | Not calculable against the covenant. Indicative only: 607.450 US$m Adjusted Consolidated EBITDA over LTM net interest expense of 269.737 US$m is 2.25x, on a different interest definition | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:17 |
| Maximum senior secured leverage ratio | 2.50x | Not supplied: no reported figure | Not calculable. The revolver is undrawn; whether the secured AR Facility counts is defined in documents not supplied | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:17 |

Cushion at earlier quarters on the same method: Q1 2026 cushion 38.244 US$m (6.5%); Q2 2026 cushion 79.997 US$m (13.1%).

Definition risks (the definition that differs from the metric computed here):

- Computed EBITDA here is consolidated and includes 100% of subsidiaries with noncontrolling holders. Management's Adjusted EBITDA is stated net to Genesis' ownership and adds distributable cash from equity investees in place of equity earnings (EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:9; EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:11).
- Management's Adjusted EBITDA adds back select items, including differences in timing of cash receipts for certain contractual arrangements; the nine-month 2026 amount was (16,200) thousand in the Segment Margin reconciliation (10-Q_2026-09-30_gel-20260930.htm.jsonl page:27).
- The covenant EBITDA (Adjusted Consolidated EBITDA per our senior secured credit facility, as the releases label it) includes adjustments of 11,405 thousand at Q3 2026 (33,473 at Q1 2026, 16,699 at Q2 2026) described in the Q1 release as a pro rata portion of projected annual EBITDA from contractual minimum cash commitments of in-service growth projects (EX-99.1_2026-05-07_a90ex9918kearnings_q12026.htm.jsonl page:11).
- Covenant debt (Adjusted Debt) excludes the AR Facility, deducts an inventory financing item and deducts only cash of restricted subsidiaries; see the conflicts carried from CP-0.
- Management's Q3 2026 Adjusted EBITDA of 130,502 thousand compares with 131,957 thousand in Q3 2025; the 2025 comparatives include the Alkali Business through February 28, 2025 in the 9M 2025 amount of 386,535 thousand, so nine-month growth is not like for like (the reconciliation starts from net income attributable including discontinued operations, EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:10).

### Segment and operating KPIs

| Segment Margin (thousands) | FY2025 | 9M 2026 | 9M 2025 | Q3 2026 | Q3 2025 |
| --- | --- | --- | --- | --- | --- |
| Offshore pipeline transportation | 385,694 | 320,508 | 265,485 | 97,795 | 101,343 |
| Marine transportation | 115,690 | 82,246 | 85,408 | 28,680 | 25,570 |
| Onshore transportation and services | 76,469 | 70,374 | 52,947 | 20,731 | 19,663 |
| Total Segment Margin | 577,853 | 473,128 | 403,840 | 147,206 | 146,576 |

Locators: 10-K_2025-12-31_gel-20251231.htm.jsonl page:208; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:26; EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:5. Management's quarterly Adjusted EBITDA in 2026: 140,862 (Q1), 171,533 (Q2) and 130,502 (Q3), which sum to the 442,897 nine-month figure (EX-99.1_2026-05-07_a90ex9918kearnings_q12026.htm.jsonl page:9; EX-99.1_2026-08-06_a90ex9918kearnings_q22026.htm.jsonl page:9; EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:10). Offshore volumes: total offshore crude oil pipelines averaged 671,007 barrels per day in Q3 2026 against 677,691 in Q3 2025 (EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:8). Inland barge utilization was 97.9% against 91.2% (EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:8).

### Credit narrative by dimension

Leverage. Evidence: debt principal is 3,249.500 US$m at September 30, 2026 against 3,085.760 US$m at December 31, 2025 (10-Q_2026-09-30_gel-20260930.htm.jsonl pages:14-15; 10-K_2025-12-31_gel-20251231.htm.jsonl page:191). Risk mechanic: the 2034 notes (750.0) replaced the 2028 notes (679.360), the AR Facility added 99.500 and the revolver balance of 6.400 was repaid, a net rise of 163.740 US$m, while 221.594 US$m was spent on preferred units that carried "an annual coupon rate of 11.24%" (10-Q_2026-09-30_gel-20260930.htm.jsonl page:48; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:6). That swaps a preferred claim ranking below debt for debt, lowering the cost of capital but raising senior claims. Credit implication: computed total debt to EBITDA of 5.18x leaves little room for an EBITDA shortfall; management has said Adjusted EBITDA for 2026 will likely be near or possibly below the low end of its original guidance (EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:4), which is an attributed management statement.

Coverage. Evidence: EBITDA to cash interest of 2.36x (LTM) and 1.90x for FY2025 on the basis shown. Mechanic: the notes carry a run-rate coupon of 247.625 US$m a year (calculated) and net interest expense was 202.207 US$m in nine months of 2026; offshore pipeline transportation produced 320,508 of the 473,128 thousand of nine-month 2026 Segment Margin (67.7%, calculated), so cover depends heavily on producer volumes. Implication: coverage above the 2.00x covenant level is indicative only (2.25x on an unlike definition), and the minimum rises to 2.15x in 2027.

Cash flow quality. Evidence: operating cash flow of 340.898 US$m in nine months of 2026 against 142.044 in 2025, with working capital contributing +58.619 against (90.379); receivables rose to 1,053.898 from 608.221 and payables to 927.687 from 490.712 (10-Q_2026-09-30_gel-20260930.htm.jsonl pages:2, 5). Mechanic: the 10-Q says "our accounts receivable and accounts payable generally move in tandem" (10-Q_2026-09-30_gel-20260930.htm.jsonl page:50), so the rise in both is consistent with higher crude marketing activity; the AR Facility of 99.500 is drawn against receivables. Operating cash flow excluding the working capital line is 282.279 (calculated). After capital payments of 84.996, common distributions of 68.531, preferred distributions of 38.946 and net noncontrolling distributions of 46.764, free cash is 101.661 US$m (calculated), before the 221.594 US$m preferred redemptions. Implication: reported cash generation is partly timing and the 2025 comparison includes the Alkali Business; underlying free cash after distributions is positive but small relative to debt.

Liquidity. Evidence: 41.477 US$m unrestricted cash and 894.4 US$m revolver availability (total 935.877, calculated), no revolver borrowings, letters of credit of 5.6 against a 50 allowance, AR Facility fully drawn at 99.5 limit. Mechanic: availability is "subject to compliance with covenants" and the revolver has springing maturities tied to the 2029 and 2030 notes. Implication: ample near-term liquidity, but access is conditional on the leverage test; no debt matures before January 15, 2029.

Data quality. The 10-K is audited; the 10-Qs are unaudited; the releases are management documents. The statement figures cross-foot (see Calculations). Differences between the Q3 10-Q and the Q3 release on cash and the inventory financing item are unresolved. FY2025 cash flows and the nine-month 2025 comparatives include the Alkali Business for part of the period.

Definition risks. See the definitions review above: the management leverage ratio is not reproducible from the filings alone.

Key gaps. See the Gaps section.

### Conflicts and unresolved differences

| Item | Source A | Source B | Treatment here |
| --- | --- | --- | --- |
| Cash for leverage | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:2: "Cash and cash equivalents $ 41,477 $ 6,437" | EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:11: "Less: Cash and cash equivalents (40,553)" | Filed balance sheet cash used for computed metrics; the release figure appears only in the management ratio. |
| Inventory financing item | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:17: "Our inventory financing sublimit as of September 30, 2026 was $10.5 million of the maximum allowed of $200 million." | EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:11: "Less: Outstanding inventory financing sublimit borrowings (10,500)" | Not netted in computed metrics. At December 31, 2025 the same sentence gave 28.1 million with only 6.4 million borrowed (10-K_2025-12-31_gel-20251231.htm.jsonl page:194), which suggests it is a sublimit size, but this is not confirmed. |

### Subsequent events and period labels

Events after September 30, 2026: the October 2026 declaration of a 0.20 per unit common distribution and 0.9473 per preferred unit, payable November 13, 2026 (10-Q_2026-09-30_gel-20260930.htm.jsonl page:53), and, in the release only, about four days of service disruption from Hurricane Isaias in early October (EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:4). Neither changes a September 30, 2026 figure. All period labels used: FY2025, Q1 2026 to Q3 2026, 9M 2026, 9M 2025, LTM at each 2026 quarter end.

### Readiness for downstream consumers

| Consumer | Requirement | Status | Evidence and action |
| --- | --- | --- | --- |
| CP-1A | Sufficiency of CP-1 evidence for business and transaction context | Limited | Debt register, 2026 financing events and preferred repurchases are located; transaction documents and the organization chart are not supplied. |
| CP-2 | Normalized financials, liquidity data, debt classification, maturity profile, covenant metrics | Limited | Statements, debt register, liquidity and maturities are complete; covenant ratio is management-reported and EBITDA definitions differ by basis. Action: label every ratio with its basis. |
| CP-5 | Traceability of each figure | Sufficient | Every printed figure has a page locator; every calculated figure is shown with inputs. |

### Evidence lineage

| Claim group | Lineage class | Reason |
| --- | --- | --- |
| Statement lines, debt table, covenant levels | Directly Sourced | Printed in filings with locator. |
| EBITDA, LTM figures, leverage, interest cover, liquidity totals, maturities | Calculated | Derived from printed components in Calculations. |
| Management covenant ratio and Adjusted EBITDA | Directly Sourced as management measure | Attributed to management; definitions held in documents not supplied. |
| Interpretation of the inventory financing item | Analyst Inference | Based on the December 31, 2025 comparison; unconfirmed. |

## Calculations

All inputs are printed figures with the locators given in the tables above. Thousands of dollars unless stated.

### EBITDA (computed)

Definition: operating income + depreciation and amortization + equity in earnings of equity investees - gain on sale of assets.

| Period | Operating income | D&A | Equity earnings | Gain on sale | EBITDA |
| --- | --- | --- | --- | --- | --- |
| FY2025 | 258,190 | 232,072 | 47,629 | 0 (no such line) | 537,891 |
| Q1 2026 | 76,613 | 58,909 | 14,162 | 0 (no such line) | 149,684 |
| Q1 2025 | 21,973 | 56,171 | 12,492 | 0 (no such line) | 90,636 |
| Six months 2026 | 182,049 | 122,042 | 32,522 | 17,436 | 319,177 |
| Six months 2025 | 89,688 | 112,076 | 24,822 | 0 (no such line) | 226,586 |
| 9M 2026 | 251,455 | 183,000 | 45,078 | 17,436 | 462,097 |
| 9M 2025 | 168,279 | 169,144 | 35,667 | 0 (no such line) | 373,090 |
| Q3 2026 | 69,406 | 60,958 | 12,556 | 0 (no such line) | 142,920 |
| Q3 2025 | 78,591 | 57,068 | 10,845 | 0 (no such line) | 146,504 |

Q1 locators: 10-Q_2026-03-31_gel-20260331.htm.jsonl page:3; six-month: 10-Q_2026-06-30_gel-20260630.htm.jsonl page:3.

### LTM EBITDA and cash interest

LTM = FY2025 + year-to-date 2026 - year-to-date 2025.

- LTM Q1 2026 EBITDA: 537,891 + 149,684 - 90,636 = 596,939.
- LTM Q2 2026 EBITDA: 537,891 + 319,177 - 226,586 = 630,482.
- LTM Q3 2026 EBITDA: 537,891 + 462,097 - 373,090 = 626,898.
- LTM Q1 2026 cash interest (US$m): 282.4 + 59.0 - 73.3 = 268.1 (10-Q_2026-03-31_gel-20260331.htm.jsonl page:24).
- LTM Q2 2026 cash interest: 282.4 + 135.9 - 152.1 = 266.2 (10-Q_2026-06-30_gel-20260630.htm.jsonl page:29).
- LTM Q3 2026 cash interest: 282.4 + 190.0 - 206.3 = 266.1 (10-Q_2026-09-30_gel-20260930.htm.jsonl page:29).

### Other LTM lines in the metrics table

- Revenue: 1,630,415 + 1,427,801 - 1,189,660 = 1,868,556.
- Operating income: 258,190 + 251,455 - 168,279 = 341,366.
- D&A: 232,072 + 183,000 - 169,144 = 245,928.
- Equity earnings: 47,629 + 45,078 - 35,667 = 57,040.
- Interest expense, net: 264,729 + 202,207 - 197,199 = 269,737.
- Net income from continuing operations: 30,505 + 90,162 - (-3,774) = 124,441.
- Net income attributable to Genesis Energy, L.P.: -440,403 + 52,072 - (-460,274) = 71,943.
- Segment Margin: 577,853 + 473,128 - 403,840 = 647,141.
- Operating cash flow: 252,826 + 340,898 - 142,044 = 451,680.
- Capital payments: 186,888 + 84,996 - 163,108 = 108,776.

### Leverage and cover

| Date | Debt principal (US$m) | Cash (US$m) | LTM EBITDA (US$m) | Total debt / EBITDA | Net debt / EBITDA | Cash interest (US$m) | EBITDA / cash interest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dec 31, 2025 | 3,085.760 | 6.437 | 537.891 | 5.7368 | 5.7248 | 282.4 | 1.9047 |
| Mar 31, 2026 | 3,224.100 | 4.210 | 596.939 | 5.4011 | 5.3940 | 268.1 | 2.2266 |
| Jun 30, 2026 | 3,249.500 | 39.261 | 630.482 | 5.1540 | 5.0917 | 266.2 | 2.3685 |
| Sep 30, 2026 | 3,249.500 | 41.477 | 626.898 | 5.1835 | 5.1173 | 266.1 | 2.3559 |

Debt principal: Dec 31, 2025 is 6,400 + 679,360 + 600,000 + 500,000 + 700,000 + 600,000 = 3,085,760; Mar 31, 2026 is 74,100 + 3,150,000 = 3,224,100; Jun 30 and Sep 30, 2026 are 3,150,000 + 99,500 = 3,249,500. Net debt = debt principal - unrestricted cash.

### Liquidity, maturities and debt movement

- Revolver availability: Dec 31, 2025: 800.0 - 6.4 - 5.0 = 788.6; Mar 31, 2026: 900.0 - 74.1 - 6.8 = 819.1; Jun 30 and Sep 30, 2026: 900.0 - 0 - 5.6 = 894.4 (US$m; matches the printed availability each time).
- Cash plus availability at Sep 30, 2026: 41.477 + 894.4 = 935.877 US$m.
- Maturity rows: 600.0 + 99.5 = 699.5 (2029); 699.5 + 500.0 + 700.0 + 600.0 + 750.0 = 3,249.5.
- Debt movement since Dec 31, 2025: 3,249,500 - 3,085,760 = 163,740; also -6,400 - 679,360 + 750,000 + 99,500 = 163,740.
- Run-rate note coupon (US$m): 600.0 x 8.250% + 500.0 x 8.875% + 700.0 x 7.875% + 600.0 x 8.000% + 750.0 x 6.750% = 49.500 + 44.375 + 55.125 + 48.000 + 50.625 = 247.625.

### Covenant cushion (management inputs)

| Quarter | Adjusted Debt | Adjusted Consolidated EBITDA | EBITDA floor at 5.75x (debt / 5.75) | Cushion | Cushion share |
| --- | --- | --- | --- | --- | --- |
| Q1 2026 | 3,155,230 | 586,980 | 548,736 | 38,244 | 6.5% |
| Q2 2026 | 3,048,295 | 610,135 | 530,138 | 79,997 | 13.1% |
| Q3 2026 | 3,055,602 | 607,450 | 531,409 | 76,041 | 12.5% |

Q3 2026 Adjusted Debt: 3,106,655 - 10,500 - 40,553 = 3,055,602. Ratio: 3,055,602 / 607,450 = 5.0302, printed as 5.03X. Turns of headroom at Q3: 5.75 - 5.03 = 0.72. Indicative interest coverage: 607,450 / 269,737 = 2.2520.

### Cash flow and other

- Operating cash flow before working capital, 9M 2026: 340,898 - 58,619 = 282,279.
- Free cash after distributions, 9M 2026: 340,898 - 84,996 - 68,531 - 38,946 - (53,442 - 6,678) = 101,661.
- Non-current ARO: 256,656 - 24,200 = 232,456; other long-term liabilities residual: 433,015 - 232,456 - 129,487 = 71,072.
- Receivables change: 1,053,898 - 608,221 = 445,677; payables change: 927,687 - 490,712 = 436,975.
- Management Adjusted EBITDA 2026 quarters: 140,862 + 171,533 + 130,502 = 442,897.

### Cross-foot checks

Balance sheet columns foot in every period: current assets sum to total current assets; total current assets plus non-current assets equal total assets; current liabilities sum to the total; total liabilities plus mezzanine units plus partners' capital equal total assets (checked for all four dates). Income statement: total revenues less total costs and expenses equals operating income in each column (1,630,415 - 1,372,225 = 258,190; 1,427,801 - 1,176,346 = 251,455; 1,189,660 - 1,021,381 = 168,279; 449,251 - 379,845 = 69,406; 414,001 - 335,410 = 78,591).

## Gaps

| Gap | Severity | Affected consumers | Action |
| --- | --- | --- | --- |
| Not supplied: FY2025 Adjusted EBITDA and a covenant ratio at December 31, 2025; the 10-K presents Available Cash before Reserves (149,121 thousand) but not Adjusted EBITDA | Medium | CP-2, CP-5 | Use the computed EBITDA basis for FY2025 and label it; do not compare with management's 2026 figures. |
| Not supplied: credit agreement and indentures, so covenant definitions, collateral and guarantor release terms are not verifiable | High | CP-2, CP-5 | Add the executed agreements before relying on headroom. |
| Unresolved: cash (41,477 vs 40,553) and inventory financing item (10.5 million) differ between the 10-Q and the release | Medium | CP-2, CP-5 | Carry both; do not net the item in computed metrics. |
| Not supplied: reported interest coverage and senior secured leverage figures | Medium | CP-2 | Treat the indicative 2.25x as not a covenant measure. |
| FY2025 cash flows are consolidated and cash interest may include Alkali Business interest for January and February 2025 | Low | CP-2 | Label FY2025 interest cover as possibly understated; prefer LTM Q3 2026. |
| Not supplied: separate fourth-quarter 2025 statements and quarterly capital payments | Low | CP-2 | Use LTM built from year-to-date differences. |
| Not supplied: Poseidon revolver balance, non-current lease liability at September 30, 2026, call terms of the 2034 notes | Low | CP-2 | Add from the 10-K or indenture if needed. |
| Not supplied: year-end call guidance range | Low | CP-2 | Quote guidance only as management language. |

## Next module

Run CP-1A next, then CP-2 and CP-5. Carry forward: (1) every ratio must name its basis, computed consolidated EBITDA or management Adjusted Consolidated EBITDA, and total debt including the AR Facility or the release's Adjusted Debt excluding it; (2) computed LTM Q3 2026 figures are total debt to EBITDA 5.18x, net debt to EBITDA 5.12x and EBITDA to cash interest 2.36x; (3) liquidity is 41.477 US$m cash plus 894.4 US$m revolver availability, conditional on covenants; (4) no maturity before January 15, 2029; (5) the credit agreement, indentures, guarantor list and organization chart remain unsupplied; (6) the 10-K credit agreement description is superseded. The next evidence action is to add the Eighth credit agreement and note indentures.
