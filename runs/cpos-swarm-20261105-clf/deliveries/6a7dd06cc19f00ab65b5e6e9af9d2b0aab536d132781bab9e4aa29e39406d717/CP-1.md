# CP-1 — Financial base: CLEVELAND-CLIFFS INC. (clf)

## Request

- Issuer: CLEVELAND-CLIFFS INC. (issuer id `clf`, NYSE: CLF), as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD; all amounts are US$ millions unless a row says otherwise. Current period Q3 2026; prior period FY2025 (context `run`).
- Run: `clf-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5. This is CP-1, the financial base.
- Execution: host session. The analyst read the pinned page files and wrote this answer. No provider was called.
- Question: what do the filed statements, notes and releases support as a financial base (reported figures, debt, liquidity, interest, covenant status and claims outside debt), and which calculations are safe?
- Perimeter: Cleveland-Cliffs Inc. and subsidiaries, consolidated, including the Stelco subsidiary and the SunCoke Middletown variable interest entity (10-Q Q3 page:3, page:7, page:23). Issuer of every senior note series and borrower under the ABL Facility is Cleveland-Cliffs Inc. (10-K page:131, page:132 footnote 2).
- Periods: FY2025 is the year ended December 31, 2025. Q1, Q2 and Q3 2026 are the three months ended March 31, June 30 and September 30, 2026. LTM (last twelve months) means the twelve months to September 30, 2026 unless a row names another quarter-end.
- Locators: `page:N` is the source chunk number in the pinned `.jsonl` file, not the printed page number. "10-Q Q3" is the 10-Q for the quarter ended September 30, 2026; "Release Q3" is the Exhibit 99.1 dated October 19, 2026.

## Sources

Issuer sources relied on (name and pinned sha256):

| Source | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_clf-20251231.htm.jsonl | 4c221bc0965bff2fddf7c4bff630fa79a69227de30709426ec9a8c89ce97e2df | FY2025 statements, debt note, leases, pensions, commitments, FY2025 Adjusted EBITDA and cash interest |
| 10-Q_2026-03-31_clf-20260331.htm.jsonl | cdb78421e299c29e406bbc729a020af9f5e9e2600a8725769f4fc9cce3f48238 | Q1 2026 and Q1 2025 statements, debt and ABL table, cash interest |
| 10-Q_2026-06-30_clf-20260630.htm.jsonl | e0ba1bee447b92cbe2b9ad67268169c4ba2e392089bcf206be2b86a11c01f94b | Q2 and six-month 2026 and 2025 statements, debt and ABL table, cash interest |
| 10-Q_2026-09-30_clf-20260930.htm.jsonl | c3188e1da0b49175580c8c9484ba8f4a1c413725f4f518851b880884f79957d1 | Q3 and nine-month 2026 and 2025 statements, debt note, ABL table, liquidity, commitments, Adjusted EBITDA |
| EX-99.1_2026-04-20_clf-202603318xkex991.htm.jsonl | b9c8fc8d9b4361337a220b73ac602738ac2f0a283bbd73c7b1429c171ac6000c | Q1 2026 release: reported liquidity, fourth quarter 2025 comparatives, management outlook |
| EX-99.1_2026-07-23_clf-202606308xkex991.htm.jsonl | 6e73622f8701012d98293b6d350054a601691c0c525be23eff4b4255d0c4ab32 | Q2 2026 release: discrete Q2 figures, leverage target wording |
| EX-99.1_2026-10-19_clf-202609308xkex991.htm.jsonl | e6cabc90a6962f04fc1da1253ad4fc1e70365df28408b401d69ed58092c0c0e1 | Q3 2026 release: discrete Q2 and Q3 columns, outlook, leverage target wording |
| context | 9824d18b9e3851ae3ee2ee1eb294b36a7465c031f02ec1e26c0d1341d4ae46e3 | Run settings only; not issuer evidence. Blank fields (ratings, quotes, market data) are not zero |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | a3ac66d14ed58e324a2e51f64f8df6ffab5558cd2acad9a6736446039b68520e | Source readiness: consumer status READY_WITH_LIMITATIONS for CP-1, CP-1A, CP-2 and CP-5; logged differences carried below |

CP-0 consistency: this answer agrees with CP-0 on its source register and its logged differences 1 to 7. It adds one difference CP-0 did not list (capital expenditure outlook horizons, see Conflicts) and it defines net debt, which CP-0 correctly noted no filing defines.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Cleveland-Cliffs is highly levered on a last-twelve-month basis, at 7.93x total debt to Adjusted EBITDA at September 30, 2026, but liquidity of $3,246 million and no senior note maturity before 2029 limit near-term refinancing pressure. | Medium | Leverage rests on management's Adjusted EBITDA, which was thin before the 2026 recovery. Covenant levels, indentures and the property sale behind expected debt reduction are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Last-twelve-month Adjusted EBITDA is $972 million against $37 million for FY2025, and quarterly Adjusted EBITDA rose from $95 million to $286 million to $612 million across 2026. | Leverage multiples are falling fast but remain very sensitive to a single strong quarter. Trough-period ratios are not meaningful. | High |
| Total debt principal is $7,712 million, of which the ABL Facility is $834 million due 2028. Nine senior note series are unsecured and none matures before 2029. | Refinancing pressure is back-ended. The secured ABL is the nearest maturity and the only drawn bank debt. | High |
| Interest cover is 1.84x on cash interest and 1.61x on net interest expense on a last-twelve-month basis. | Cover is thin, so the credit depends on the 2026 earnings run-rate holding. | Medium |
| Operating cash flow less capital expenditure was negative $332 million in the nine months ended September 30, 2026, but positive $72 million in Q3 2026. | Debt has fallen only modestly since March 2026. The expected large fourth-quarter reduction is management language and cannot be verified from the filings. | Medium |
| Finance leases of $402 million, pension and OPEB items and large purchase commitments sit outside the $7,712 million debt figure. | Fixed obligations beyond debt are material, so headline debt understates claims on cash flow. Lease and commitment data are only as of December 31, 2025. | Medium |

### Financial base view

The financial base is usable and the filed numbers tie out across the 10-K, the three 10-Qs and the three releases. Leverage is high but refinancing pressure is back-ended. At September 30, 2026 total debt principal was $7,712 million against cash of $77 million, and LTM Adjusted EBITDA of $972 million gives total debt to Adjusted EBITDA of 7.93x and net debt to Adjusted EBITDA of 7.85x. The multiple has fallen from 25.20x at March 31, 2026 and 15.45x at June 30, 2026 only because earnings recovered: Adjusted EBITDA was $95 million in Q1 2026, $286 million in Q2 2026 and $612 million in Q3 2026, while debt principal moved from $7,837 million to $7,773 million to $7,712 million. FY2025 Adjusted EBITDA of $37 million makes the FY2025 multiple not meaningful. Liquidity, defined as cash plus ABL borrowing capacity after borrowings and letters of credit, was $3,246 million, and the only covenant the sources describe, a springing fixed charge coverage ratio of 1.0 to 1.0, was not applicable because the ABL liquidity requirements were met. Three restrictions follow every ratio below: Adjusted EBITDA is management's non-GAAP measure and includes non-cash pension and OPEB credits; no indenture or credit agreement is supplied, so covenant headroom is Not calculable; and lease balances, pension funded status and purchase commitments are available only as of December 31, 2025.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (Dec 31, 2025) | Not supplied: FY2025 Adjusted EBITDA of 37 makes the multiple not meaningful | Not supplied: FY2025 Adjusted EBITDA of 37 makes the multiple not meaningful | x | Debt principal 7,330 and cash 57 (10-K page:131, page:109); Adjusted EBITDA 37 (10-K page:93). Arithmetic would give 198.11x and 196.57x |
| Q1 2026 (LTM to Mar 31, 2026) | 25.20 | 25.05 | x | Debt principal 7,837 (10-Q Q1 page:12), cash 45; LTM Adjusted EBITDA 311 = 37 + 95 - (-179). Total debt excludes leases; net debt is analyst-defined as debt principal less cash and equivalents |
| Q2 2026 (LTM to Jun 30, 2026) | 15.45 | 15.31 | x | Debt principal 7,773 (10-Q Q2 page:15), cash 70; LTM Adjusted EBITDA 503 = 37 + 381 - (-85). Same definitions |
| Q3 2026 (LTM to Sep 30, 2026) | 7.93 | 7.85 | x | Debt principal 7,712 (10-Q Q3 page:15), cash 77; LTM Adjusted EBITDA 972 = 37 + 993 - 58. Adjusted EBITDA is a management non-GAAP measure that includes non-service pension and OPEB credits; excluding them would raise the multiples (see Interpretation) |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 0.08 | x | Adjusted EBITDA 37 over interest paid on debt obligations net of capitalized interest 459 (10-K page:93, page:123). Not meaningful as a cover measure; earnings near zero |
| Q1 2026 (LTM to Mar 31, 2026) | 0.60 | x | LTM Adjusted EBITDA 311 over LTM cash interest 520 = 459 + 138 - 77 (10-Q Q1 page:8) |
| Q2 2026 (LTM to Jun 30, 2026) | 1.00 | x | LTM Adjusted EBITDA 503 over LTM cash interest 505 = 459 + 256 - 210 (10-Q Q2 page:9) |
| Q3 2026 (LTM to Sep 30, 2026) | 1.84 | x | LTM Adjusted EBITDA 972 over LTM cash interest 529 = 459 + 411 - 341 (10-Q Q3 page:9). Cash interest excludes finance lease interest and may differ from interest expense by timing of coupon dates; over net interest expense of 604 the cover is 1.61x |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2025 | 57 | 3213 | US$m | Cash and cash equivalents (10-K page:109). Undrawn = ABL borrowing capacity available: borrowing base 3,730 less borrowings 452 less letters of credit 65 (10-K page:140). Limited by the borrowing base, not by the 4,750 commitment |
| Mar 31, 2026 | 45 | 3096 | US$m | Cash (10-Q Q1 page:3). Borrowing base 4,103 less borrowings 959 less letters of credit 48 (10-Q Q1 page:13) |
| Jun 30, 2026 | 70 | 3014 | US$m | Cash (10-Q Q2 page:3). Borrowing base 3,969 less borrowings 895 less letters of credit 60 (10-Q Q2 page:15) |
| Sep 30, 2026 | 77 | 3169 | US$m | Cash (10-Q Q3 page:3). Borrowing base 4,060 less borrowings 834 less letters of credit 57 (10-Q Q3 page:15). Cash plus capacity is 3,246, stated by the issuer as "$3.2 billion in liquidity" (10-Q Q3 page:46) |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 (remainder) | 0 | US$m | Printed as a dash in the 10-Q Q3 maturity table (page:16); consistent with the redemption of all 2027 notes on October 3, 2025 (10-K page:140) |
| 2027 | 0 | US$m | Printed as a dash (10-Q Q3 page:16) |
| 2028 | 834 | US$m | ABL Facility borrowings; maturity is the earlier of June 9, 2028 or 91 days before the maturity of certain other material debt (10-K page:139). Secured |
| 2029 | 1268 | US$m | 4.625% 2029 notes 368 (due Mar 1, 2029) plus 6.875% 2029 notes 900 (due Nov 1, 2029); 10-Q Q3 page:15 and 10-K page:135 |
| 2030 | 750 | US$m | 6.750% 2030 notes due Apr 15, 2030 |
| 2031 | 1175 | US$m | 4.875% 2031 notes 325 (due Mar 1, 2031) plus 7.500% 2031 notes 850 (due Sep 15, 2031). The filing prints these inside "Thereafter 4,860"; the split is from the instrument table and maturity dates |
| 2032 | 1425 | US$m | 7.000% 2032 notes due Mar 15, 2032 (split from "Thereafter") |
| 2033 | 900 | US$m | 7.375% 2033 notes due May 1, 2033 (split from "Thereafter") |
| 2034 | 1125 | US$m | 7.625% 2034 notes due Jan 15, 2034 (split from "Thereafter") |
| 2040 | 235 | US$m | 6.250% 2040 notes due Oct 1, 2040, not guaranteed by subsidiaries (10-K page:136). Total of all rows is 7,712, equal to the printed total principal amount; carrying value after 67 of unamortized discounts and issuance costs is 7,645 |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2025 | Nine months 2025 | Nine months 2026 | LTM to Sep 30, 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- |
| Revenues | 18610 | 14297 | 15760 | 20073 | LTM = 18,610 + 15,760 - 14,297. 10-K page:109; 10-Q Q3 page:4. Q3 2026 alone: 5,612 |
| Operating income (loss) | -1579 | -1248 | 49 | -282 | LTM = -1,579 + 49 - (-1,248). Q3 2026 alone: 311 |
| Interest expense, net | 594 | 442 | 452 | 604 | LTM = 594 + 452 - 442. Q3 2026 alone: 148 |
| Net income (loss) | -1428 | -1193 | -198 | -433 | LTM = -1,428 + (-198) - (-1,193). Q3 2026 alone: 165 |
| Total EBITDA, as reported | -180 | -163 | 979 | 962 | Issuer reconciliation, 10-K page:93; 10-Q Q3 page:47. LTM = -180 + 979 - (-163) |
| Adjusted EBITDA, management non-GAAP | 37 | 58 | 993 | 972 | 10-K page:93; 10-Q Q3 page:47. Excludes EBITDA from noncontrolling interests, idled facilities, currency exchange, derivative fair value changes, disposals, severance and other. Q3 2026 alone: 612 |
| Depreciation, depletion and amortization | 1235 | 963 | 780 | 1052 | LTM = 1,235 + 780 - 963 |
| Net cash from operating activities | -462 | -449 | 129 | 116 | 10-K page:110; 10-Q Q3 page:5. LTM = -462 + 129 - (-449). Q3 2026 alone: 224 (Release Q3 page:8) |
| Purchase of property, plant and equipment | 561 | 421 | 461 | 601 | LTM = 561 + 461 - 421. Q3 2026 alone: 152 |
| Operating cash flow less capital expenditure | -1023 | -870 | -332 | -485 | Analyst calculation, not a printed subtotal. Q3 2026 alone: 72 |
| Interest paid on debt obligations, net of capitalized interest | 459 | 341 | 411 | 529 | 10-K page:123; 10-Q Q3 page:9. Q3 2026 alone: 155 = 411 - 256 |
| Total debt principal (period end) | 7330 | Not supplied: the Sep 30, 2025 debt table is not in the pack | 7712 | 7712 | FY2025 as of Dec 31, 2025; nine months 2026 and LTM as of Sep 30, 2026 (10-Q Q3 page:15) |
| Cash and cash equivalents (period end) | 57 | 66 | 77 | 77 | 10-K page:109; 10-Q Q3 page:3; Sep 30, 2025 cash from the nine-month cash flow statement, 10-Q Q3 page:5 |
| Net debt, analyst-defined (debt principal less cash) | 7273 | Not supplied: Sep 30, 2025 debt not in the pack | 7635 | 7635 | No filing defines net debt. Excludes leases and restricted cash (restricted cash is nil at Sep 30, 2026, 10-Q Q3 page:5) |
| Total debt / Adjusted EBITDA (x) | Not supplied: not meaningful, FY2025 Adjusted EBITDA is 37 | Not supplied: debt at Sep 30, 2025 not in the pack | Not supplied: nine-month EBITDA is not annualized | 7.93 | 7,712 / 972 |
| Net debt / Adjusted EBITDA (x) | Not supplied: not meaningful, FY2025 Adjusted EBITDA is 37 | Not supplied: see above | Not supplied: nine-month EBITDA is not annualized | 7.85 | 7,635 / 972 |
| Adjusted EBITDA / cash interest (x) | 0.08 | Not supplied: nine-month debt service is not annualized here | Not supplied: nine-month figure is not annualized here | 1.84 | 972 / 529 |
| Adjusted EBITDA / interest expense, net (x) | 0.06 | Not supplied: not annualized | Not supplied: not annualized | 1.61 | 972 / 604 |
| Liquidity (cash plus ABL capacity) | 3270 | Not supplied: Sep 30, 2025 ABL table not in the pack | 3246 | 3246 | Dec 31, 2025: 57 + 3,213. Sep 30, 2026: 77 + 3,169 |
| Covenant: springing fixed charge coverage minimum | 1.0 to 1.0, not applicable | Not supplied: not tested in the pack | 1.0 to 1.0, not applicable | 1.0 to 1.0, not applicable | Test applies only if ABL liquidity requirements are not met; trigger level and fixed charge definition are Not supplied. Headroom is Not calculable |

### Reported statement extracts

#### Statements of operations (US$m)

| Line | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | Nine months 2026 | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| Revenues | 18610 | 4922 | 5226 | 5612 | 15760 | 10-K page:109; 10-Q Q1 page:4; 10-Q Q2 page:4; 10-Q Q3 page:4 |
| Cost of goods sold | -19470 | -5004 | -5094 | -5147 | -15245 | same |
| Selling, general and administrative | -543 | -125 | -154 | -153 | -432 | same |
| Restructuring and other charges | -86 | 0 | -3 | -1 | -4 | Q1 2026 printed as a dash |
| Asset impairment | -39 | 0 | 0 | 0 | 0 | Printed as a dash in Q3 2026 and nine months 2026; no line in the Q1 and Q2 2026 statements, so 0 is used only for the sum check |
| Acquisition-related costs | -1 | 0 | 0 | 0 | 0 | Absent in 2026 statements |
| Miscellaneous, net | -50 | -6 | -24 | 0 | -30 | Q3 2026 printed as a dash |
| Total operating costs | -20189 | -5135 | -5275 | -5301 | -15711 | printed totals |
| Operating income (loss) | -1579 | -213 | -49 | 311 | 49 | printed |
| Interest expense, net | -594 | -148 | -156 | -148 | -452 | printed |
| Net periodic benefit credits other than service cost | 223 | 64 | 64 | 64 | 192 | printed |
| Net income (loss) | -1428 | -229 | -134 | 165 | -198 | printed |
| Net income (loss) attributable to Cliffs shareholders | -1478 | -237 | -145 | 152 | -230 | printed |

#### Balance sheet and cash flow items (US$m)

| Item | Dec 31, 2025 | Mar 31, 2026 | Jun 30, 2026 | Sep 30, 2026 | Locator |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 57 | 45 | 70 | 77 | 10-K page:109; 10-Q Q1 page:3; 10-Q Q2 page:3; 10-Q Q3 page:3 |
| Accounts receivable, net | 1442 | 1882 | 2044 | 2159 | same |
| Inventories | 4772 | 4591 | 4525 | 4694 | same |
| Accounts payable | 1893 | 2011 | 2159 | 2327 | same |
| Long-term debt (carrying) | 7253 | 7763 | 7703 | 7645 | debt notes |
| Total liabilities | 13689 | 14096 | 14297 | 14376 | statements |
| Total equity | 6323 | 6019 | 5818 | 5966 | statements of changes in equity |
| Noncontrolling interests | 207 | 197 | 214 | 279 | statements of changes in equity |
| Net cash from operating activities, year to date | -462 | -325 | -95 | 129 | cash flow statements |
| Purchase of property, plant and equipment, year to date | -561 | -152 | -309 | -461 | cash flow statements |

### Debt register

All senior notes are issued by Cleveland-Cliffs Inc. alone (no co-issuer); the 10-K issuer column reads "Cliffs" for every row (10-K page:131). Principal is as of September 30, 2026 and December 31, 2025 and is identical on both dates for every note series.

| Instrument | Principal (US$m) | Coupon | Effective rate | Maturity | Security | Guarantors | Locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4.625% 2029 Senior Notes | 368 | 4.625% | 4.625% | Mar 1, 2029 | Unsecured | Material direct and indirect wholly owned domestic subsidiaries | 10-Q Q3 page:15; 10-K page:135, page:136 |
| 6.875% 2029 Senior Notes | 900 | 6.875% | 6.875% | Nov 1, 2029 | Unsecured | same | same |
| 6.750% 2030 Senior Notes | 750 | 6.750% | 6.750% | Apr 15, 2030 | Unsecured | same | same |
| 4.875% 2031 Senior Notes | 325 | 4.875% | 4.875% | Mar 1, 2031 | Unsecured | same | same |
| 7.500% 2031 Senior Notes | 850 | 7.500% | 7.500% | Sep 15, 2031 | Unsecured | same | 10-K page:134 |
| 7.000% 2032 Senior Notes | 1425 | 7.000% | 7.054% | Mar 15, 2032 | Unsecured | same | 10-K page:135 |
| 7.375% 2033 Senior Notes | 900 | 7.375% | 7.375% | May 1, 2033 | Unsecured | same | 10-K page:135 |
| 7.625% 2034 Senior Notes | 1125 | 7.625% | 7.516% | Jan 15, 2034 | Unsecured | same | 10-K page:133 |
| 6.250% 2040 Senior Notes | 235 | 6.250% | 6.340% | Oct 1, 2040 | Unsecured | None: "There are no subsidiary guarantees" | 10-K page:136 |
| ABL Facility | 834 (452 at Dec 31, 2025) | Variable; 5.211% effective at Sep 30, 2026 | 5.211% | Earlier of Jun 9, 2028 or 91 days before certain other material debt | First lien on ABL collateral (receivables, inventory, certain mobile equipment); second lien on substantially all other assets | Certain U.S. subsidiaries; Cleveland-Cliffs Inc. is borrower under the U.S. tranche, certain Canadian subsidiaries under a 500 tranche | 10-Q Q3 page:15; 10-K page:139 |
| Total principal | 7712 (7330 at Dec 31, 2025) | | | | | | 10-Q Q3 page:15 |
| Unamortized discounts and issuance costs | -67 (-77) | | | | | | same |
| Total long-term debt (carrying) | 7645 (7253) | | | | | | same |

Other debt features: the notes carry change-of-control repurchase at 101% for the series that print it, optional redemption schedules, and "there are no financial covenants" in the series described (10-K page:133, page:134, page:138). Redemption price steps for the 7.375% 2033 notes are unverified (see Conflicts). Fair value of senior notes was 6,751 against carrying 6,811 at September 30, 2026, and 7,037 against 6,801 at December 31, 2025 (10-Q Q3 page:19). Debt principal moved this year as follows: ABL borrowings 452 at Dec 31, 2025, 959 at Mar 31, 2026, 895 at Jun 30, 2026 and 834 at Sep 30, 2026; no senior notes were issued in 2026 (10-Q Q3 page:45).

### Liquidity build and covenant status

| Facility or item | Dec 31, 2025 | Mar 31, 2026 | Jun 30, 2026 | Sep 30, 2026 | Locator |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 57 | 45 | 70 | 77 | balance sheets |
| ABL maximum borrowing base (commitments) | 4750 | 4750 | 4750 | 4750 | footnote to ABL table in each filing |
| Available borrowing base | 3730 | 4103 | 3969 | 4060 | ABL tables |
| Less borrowings | -452 | -959 | -895 | -834 | ABL tables |
| Less letters of credit issued under the ABL | -65 | -48 | -60 | -57 | ABL tables |
| Borrowing capacity available | 3213 | 3096 | 3014 | 3169 | ABL tables (printed) |
| Cash plus capacity | 3270 | 3141 | 3084 | 3246 | calculated; issuer states $3.1 billion, $3.1 billion and $3.2 billion for the three 2026 dates |

- Facilities: one committed facility, the ABL Facility. Its maturity (earlier of June 9, 2028 or 91 days before certain other material debt) is more than twelve months from September 30, 2026, so no committed facility expires within twelve months of that date. Availability is limited by the borrowing base (receivables, inventory and mobile equipment), not by the 4,750 commitment. A Canadian tranche of 500 sits inside the 4,750 (10-K page:139); availability by tranche is not printed.
- Letters of credit and surety: standby letters of credit under the ABL of 57 reduce availability. Separately, surety-backed letters of credit and surety bonds were 336 at September 30, 2026 against 278 at December 31, 2025 (10-Q Q3 page:25; 10-K page:161); the 10-K says surety instruments have "no impact on our liquidity" (10-K page:92).
- Covenant: the ABL has a springing minimum fixed charge coverage ratio of 1.0 to 1.0. At each quarter end in the pack the issuer reports it was in compliance with the ABL liquidity requirements, so the test was not applicable (10-Q Q3 page:15, page:46; 10-K page:139). The liquidity level that triggers the test, the definition of fixed charges and the issuer's computed ratio are not in the sources. Maintenance headroom is therefore Not calculable. The definition differs from the metrics computed here: the computed EBITDA / cash interest cover is not the covenant ratio.
- Secured capacity: management states "approximately $3 billion of secured note capacity" at September 30, 2026 (10-Q Q3 page:46), compared with approximately $3.2 billion at December 31, 2025 and March 31, 2026. Subject to the limits of the indentures and ABL, which are not supplied.

### Claims outside the debt figure

| Item | Amount (US$m) | Date | Inside or outside the 7,712 debt figure | Locator |
| --- | --- | --- | --- | --- |
| Finance lease liabilities | 402 (67 current, 335 non-current) | Dec 31, 2025 | Outside; carried in Other current and Other non-current liabilities | 10-K page:152, page:153 |
| Operating lease liabilities | 282 (48 current, 234 non-current) | Dec 31, 2025 | Outside | same |
| Pension funded status (surplus) | 215 | Dec 31, 2025 | Outside; surplus | 10-K page:141 |
| OPEB funded status (deficit) | -514 | Dec 31, 2025 | Outside | 10-K page:141 |
| Pension and OPEB assets / liabilities on the balance sheet | 589 / 593 | Sep 30, 2026 | Outside | 10-Q Q3 page:3 |
| Defined benefit pension contributions | 27 | Nine months 2026 | Cash outflow outside debt | 10-Q Q3 page:17 |
| Cash pension and OPEB payments and contributions | 116 | Nine months 2026 | Cash outflow outside debt; management guides about 125 for FY2026 | 10-Q Q3 page:5; Release Q2 page:3 |
| Unconditional purchase obligations (take-or-pay) | 13954 total: 2,911 (2026), 1,936 (2027), 1,520 (2028), 1,266 (2029), 1,191 (2030), 5,130 thereafter | Dec 31, 2025 | Outside; off balance sheet | 10-K page:160 |
| Supply chain finance programs | 19 short-term financing in Other current liabilities; 76 in Accounts payable | Sep 30, 2026 (28 and 73 at Dec 31, 2025) | Outside; 19 is classified as short-term financing but not included in Long-term debt | 10-Q Q3 page:9 |
| Surety bonds and surety-backed letters of credit | 336 | Sep 30, 2026 | Outside | 10-Q Q3 page:25 |
| Asset retirement and environmental obligations | 698 non-current balance sheet line; environmental obligations total 114 (14 current, 100 long-term) | Sep 30, 2026 | Outside | 10-Q Q3 page:3, page:19 |
| Accrued liabilities for indefinitely idled facilities | 40 | Sep 30, 2026 | Outside | 10-Q Q3 page:9 |
| Noncontrolling interests | 279 | Sep 30, 2026 | Outside. The SunCoke Middletown VIE table shows noncontrolling interests of 290, more than the consolidated 279, which implies other noncontrolling interests net to negative 11; not explained. Creditors of the VIE have no recourse to the Company | 10-Q Q3 page:3, page:23 |
| Factoring or receivables sale programs | Not supplied: the term "factoring" does not appear in any source | | Not applicable | search of all sources |
| Litigation or consent-decree funding | Not supplied: the notes say no pending claim is expected to have a material adverse effect; no amount is printed | Sep 30, 2026 | Outside | 10-Q Q3 page:25 |

The unconditional purchase obligations table is printed in the 10-K only. The 10-Q Q3 Note 18 heading "PURCHASE COMMITMENTS" is followed by narrative and no table in the extracted text (page:24); whether the filed 10-Q omits the table or the extraction dropped it cannot be determined from the pack.

### Latest quarter and events after

- Q3 2026 results: revenues 5,612, Adjusted EBITDA 612 against 143 in Q3 2025, net income 165 against a loss of 234. Management said Adjusted EBITDA was "above the $575 million guidance" given three months earlier (Release Q3 page:1; guidance in Release Q2 page:3).
- Q3 2026 financing: ABL net repayment of 61 (Release Q3 page:8); no senior notes issued; no share repurchases under the program (only 5,811 shares delivered for tax withholding; remaining authorization stated as $1,375,931,379, 10-Q Q3 page:61).
- Q3 2026 events with amounts: Department of Energy framework for the Middletown Works investment, rescoping the previously awarded 500 DOE grant; the project is a 1,000 total investment with funding shared equally between the Company and the DOE, expected to be completed in 2030 (10-Q Q3 page:38, page:39). Gains on disposal of assets of 14 in Q3 and 23 in nine months (10-Q Q3 page:47). Net contributions from noncontrolling interests of 52 in Q3 (10-Q Q3 page:5); the cause is not stated, and SunCoke Middletown VIE noncontrolling interests rose from 219 to 290 (page:23).
- Operating changes: the 10-Q says the Company decided "to indefinitely idle the finishing operations at our Hamilton Works facility" (page:37); the release speaks of "galvanizing lines at Stelco" (Release Q3 page:2). Carried as logged in CP-0.
- Management language, attributed and not verified: fourth quarter 2026 Adjusted EBITDA of "approximately $715 million" and 2027 Adjusted EBITDA expected to "exceed $4 billion" (Release Q3 page:3, page:2); "we expect a major debt reduction in the fourth quarter" from free cash flow and "property sale proceeds" (Release Q3 page:1); leverage target "under 2.5x net debt to EBITDA by the middle of next year" (Release Q3 page:1). No filing describes the property sale or defines the ratio.
- Subsequent events: the 10-Q Q3 Note 19 lists none (page:27). Nothing between October 20, 2026 and 2026-11-05 is supplied; events in that window are Not supplied, not absent.
- Shares outstanding: 570,584,966 as of October 20, 2026 (10-Q Q3 page:1).

### Definitions and perimeter

- Adjusted EBITDA (issuer definition, 10-Q Q3 page:2): "EBITDA, excluding certain items such as EBITDA from noncontrolling interests; idled facilities credits (charges); currency exchange; changes in fair value of derivatives, net; gain (loss) on disposal of assets, net; amortization of inventory step-up; severance; and other, net." It is attributable to Cliffs shareholders by construction (EBITDA of noncontrolling interests is removed: 19 in Q3 2026, 50 in nine months 2026, 61 in nine months 2025, 76 in FY2025), while debt is consolidated.
- Pension and OPEB credit: the non-service component (Q3 2026: 64; nine months 2026: 192; nine months 2025: 157; FY2025: 223) sits inside EBITDA and Adjusted EBITDA (it is a line of the segment reconciliation, 10-Q Q3 page:11). The matching cash flow statement line deducts "Pension and OPEB credits" of 166 in nine months 2026 as non-cash (page:5).
- Total debt: principal of the nine senior note series and the ABL Facility, excluding leases, supply chain finance and noncontrolling interests. Net debt: total debt principal less cash and equivalents; analyst-defined.
- Cash interest: "Interest paid on debt obligations net of capitalized interest" from the supplemental cash flow note. Finance lease interest (23 in FY2025) is reported separately inside operating cash flow (10-K page:153) and is not in the 459.
- Perimeter: the obligated group (issuer and guarantor subsidiaries) reports nine-month 2026 revenues of 14,074 and a net loss of 67, against consolidated revenues of 15,760 and net loss of 198 (10-Q Q3 page:49, page:4). Stelco and other foreign subsidiaries are consolidated; whether they guarantee is not stated. Net debt is not tested at the guarantor level.

### Conflicts and consistency

| # | Item | Locators | Treatment |
| --- | --- | --- | --- |
| 1 | Q1 10-Q MD&A calls $3.1 billion the "available borrowing base"; Note 7 prints borrowing base 4,103 and capacity 3,096 | 10-Q Q1 page:13, page:40 | Note 7 table used. The $3.1 billion equals capacity, not the borrowing base (carried from CP-0) |
| 2 | Leverage target worded "debt to EBITDA by this time next year" (Q2) and "net debt to EBITDA by the middle of next year" (Q3) | Release Q2 page:2; Release Q3 page:1 | Management language only; not used as a covenant |
| 3 | Segment revenue 5,492 (Steelmaking, gross of intersegment) and 5,447 (net) for Q3 2026 | 10-Q Q3 page:11, page:10 | Both bases stated; consolidated 5,612 is used here |
| 4 | Capital expenditure outlook: releases hold "Capital expenditures maintained at approximately $700 million" for full-year 2026 (Q1 and Q2); the Q3 10-Q says "We anticipate total cash used for capital expenditures during the next 12 months to be approximately $1.0 billion" | Release Q1 page:3; Release Q2 page:3; 10-Q Q3 page:44 | Different horizons (FY2026 versus next twelve months) and the Q3 release gives no capex line. Not reconciled; both carried as management statements. Nine months 2026 actual is 461 |
| 5 | Redemption schedule text for the 7.375% 2033 notes names "7.375% 2029 Senior Notes" and steps to 100% on November 1, 2028 | 10-K page:138 | Likely text error; indenture not supplied; redemption terms unverified |
| 6 | Stray "0" in the nine-month 2026 asset impairment column of Release Q3 | Release Q3 page:7; 10-Q Q3 page:4 | 10-Q controls; no figure changes |
| 7 | SunCoke Middletown VIE noncontrolling interests of 290 exceed consolidated noncontrolling interests of 279 at September 30, 2026 (219 against 207 at December 31, 2025) | 10-Q Q3 page:23, page:3; 10-K page:159, page:109 | Both are printed; the difference is not explained in the sources. Carried as an unexplained difference |

Source tie-outs found no numeric conflict between filings and releases on revenue, net income, cash, long-term debt, operating cash flow or Adjusted EBITDA for shared periods (see Calculations).

### Interpretation

- Earnings recovery drives the leverage change. Evidence: quarterly Adjusted EBITDA of 95, 286 and 612 in 2026 (10-Q Q1 page:41; 10-Q Q2 page:45; 10-Q Q3 page:47) against debt principal that moved only from 7,837 to 7,712. Mechanism: the LTM window still contains the 2025 quarters of weak or negative Adjusted EBITDA (nine months 2025: 58), so each additional strong quarter replaces a weak one and lowers the multiple mechanically. Implication: the 7.93x level is a transition value; if Q3 2026 earnings are annualized (an illustration, not a forecast) the multiple would be 3.15x, so the credit view turns on whether the Q3 run-rate is sustained into the 2027 contract resets management describes. This is an analyst illustration, not a reported or guided figure.
- Cash conversion is the weak point. Evidence: nine-month 2026 operating cash flow of 129 against capital expenditure of 461, and receivables up by 723 as steel prices rose (10-Q Q3 page:5, page:44). Mechanism: rising prices lift receivables before collections, so earnings growth absorbs working capital in the first half. Implication: debt reduction so far is limited; the sources show ABL borrowings falling by 61 in Q3, and the fourth-quarter reduction management expects is not verifiable.
- Quality of Adjusted EBITDA. Evidence: non-service pension and OPEB credits of 258 inside LTM Adjusted EBITDA (223 + 192 - 157) and cash pension and OPEB payments of 116 in nine months 2026 (10-K page:109; 10-Q Q3 page:4, page:5). Mechanism: the credit raises EBITDA without cash. Implication: excluding the credit, LTM Adjusted EBITDA would be 714 and total debt to that figure 10.80x. This sensitivity is analyst-defined and not an issuer measure.
- Interest burden. Evidence: the instrument table implies about 519 of annual coupon and ABL interest at current balances (475.7 notes plus 43.5 ABL) against LTM cash interest of 529 and LTM interest expense of 604 (10-Q Q3 page:15, page:9, page:4). Mechanism: expense exceeds the coupon run-rate because of amortization of issuance costs, finance lease interest, fees and other items not itemized. Implication: LTM Adjusted EBITDA covers cash interest 1.84x and interest expense 1.61x, which leaves little room for an earnings reversal.
- Maturity profile. Evidence: nothing but the ABL (834, 2028) matures before 2029, and 1,268 matures in 2029 (10-Q Q3 page:16). Mechanism: the secured ABL is a borrowing-base facility whose availability moves with receivables and inventory. Implication: near-term refinancing risk is low on the sources, but 2029 to 2034 carries 6,643 of unsecured notes (1,268 + 750 + 1,175 + 1,425 + 900 + 1,125) before the 2040 notes.
- Structural position. Evidence: note guarantors are described as "material direct and indirect wholly owned domestic subsidiaries" (10-K page:136) and Stelco is a Canadian corporation (10-Q Q3 page:3). Mechanism: if foreign subsidiaries are outside the guarantee group, which the sources imply but do not state, their cash flows and assets support the notes only through the parent. Implication: guarantor-level leverage cannot be computed from the sources; the obligated group summary (10-Q Q3 page:49) is the only guarantor-level data.

## Calculations

All inputs are from the cited sources in US$ millions. Results are rounded half-even to two decimals only for ratios.

### Last-twelve-month Adjusted EBITDA

| Quarter-end | Formula | Inputs | Result |
| --- | --- | --- | --- |
| Mar 31, 2026 | FY2025 + Q1 2026 - Q1 2025 | 37 + 95 - (-179) (10-K page:93; 10-Q Q1 page:41) | 311 |
| Jun 30, 2026 | FY2025 + six months 2026 - six months 2025 | 37 + 381 - (-85) (10-Q Q2 page:45) | 503 |
| Sep 30, 2026 | FY2025 + nine months 2026 - nine months 2025 | 37 + 993 - 58 (10-Q Q3 page:47) | 972 |

Cross-check: quarterly Adjusted EBITDA for 2025 implied by the sources: Q1 -179, Q2 94 (10-Q Q2 page:45), Q3 143, so Q4 2025 = 37 - (-179 + 94 + 143) = -21, which equals the fourth quarter 2025 figure in Release Q1 page:1 ("$21 million" loss).

### Leverage

| Period | Formula | Result |
| --- | --- | --- |
| Q1 2026 total | 7,837 / 311 | 25.20x |
| Q1 2026 net | (7,837 - 45) / 311 | 25.05x |
| Q2 2026 total | 7,773 / 503 | 15.45x |
| Q2 2026 net | (7,773 - 70) / 503 | 15.31x |
| Q3 2026 total | 7,712 / 972 | 7.93x |
| Q3 2026 net | (7,712 - 77) / 972 | 7.85x |
| FY2025 total, net | 7,330 / 37; (7,330 - 57) / 37 | 198.11x; 196.57x: not meaningful |
| Q3 2026 on Total EBITDA, unadjusted | 7,712 / 962 where 962 = -180 + 979 - (-163) | 8.02x |
| Q3 2026 ex pension credit (sensitivity) | 7,712 / 714 where 714 = 972 - 258 and 258 = 223 + 192 - 157; net 7,635 / 714 | 10.80x; 10.69x |
| Q3 2026 annualized Q3 (illustration) | 7,712 / (612 x 4) = 7,712 / 2,448; net 7,635 / 2,448 | 3.15x; 3.12x |

### Cash interest and cover

| Period | LTM cash interest | Cover |
| --- | --- | --- |
| FY2025 | 459 | 37 / 459 = 0.08x |
| Q1 2026 | 459 + 138 - 77 = 520 | 311 / 520 = 0.60x |
| Q2 2026 | 459 + 256 - 210 = 505 | 503 / 505 = 1.00x |
| Q3 2026 | 459 + 411 - 341 = 529 | 972 / 529 = 1.84x |
| Q3 2026 on interest expense, net | LTM 594 + 452 - 442 = 604 | 972 / 604 = 1.61x |
| FY2025 on interest expense, net | 594 | 37 / 594 = 0.06x |

Annual coupon run-rate at September 30, 2026: notes 368 x 4.625% + 900 x 6.875% + 750 x 6.750% + 325 x 4.875% + 850 x 7.500% + 1,425 x 7.000% + 900 x 7.375% + 1,125 x 7.625% + 235 x 6.250% = 475.71; ABL 834 x 5.211% = 43.46; total 519.17, a weighted average of 6.73% on 7,712. Excludes fees, issuance-cost amortization and finance lease interest.

### Liquidity

| Date | Formula | Result |
| --- | --- | --- |
| Dec 31, 2025 | 57 + (3,730 - 452 - 65) | 3,270 |
| Mar 31, 2026 | 45 + (4,103 - 959 - 48) | 3,141 |
| Jun 30, 2026 | 70 + (3,969 - 895 - 60) | 3,084 |
| Sep 30, 2026 | 77 + (4,060 - 834 - 57) | 3,246 |

### Other LTM and derived figures

| Figure | Formula | Result |
| --- | --- | --- |
| LTM revenues | 18,610 + 15,760 - 14,297 | 20,073 |
| LTM operating income (loss) | -1,579 + 49 - (-1,248) | -282 |
| LTM net income (loss) | -1,428 + (-198) - (-1,193) | -433 |
| LTM total EBITDA | -180 + 979 - (-163) | 962 |
| LTM D&A | 1,235 + 780 - 963 | 1,052 |
| LTM operating cash flow | -462 + 129 - (-449) | 116 |
| LTM capital expenditure | 561 + 461 - 421 | 601 |
| LTM operating cash flow less capital expenditure | 116 - 601 | -485 |
| Nine months 2026 operating cash flow less capital expenditure | 129 - 461 | -332 |
| Q3 2026 operating cash flow less capital expenditure | 224 - 152 | 72 |
| Q3 2026 cash interest | 411 - 256 | 155 |
| LTM EBITDA of noncontrolling interests (context) | 76 + 50 - 61 | 65 |
| Maturities 2029 to 2034 | 1,268 + 750 + 1,175 + 1,425 + 900 + 1,125 | 6,643 |
| Fair value of senior notes to principal, Sep 30, 2026 | 6,751 / 6,878 where 6,878 = 7,712 - 834 | 98.2% |

### Tie-outs and statement reconciliations

| Check | Computation | Result vs printed |
| --- | --- | --- |
| FY2025 operating cost block | 19,470 + 543 + 86 + 1 + 39 + 0 + 50 | 20,189, equals printed total; 18,610 - 20,189 = -1,579, equals printed |
| Nine months 2026 operating cost block | 15,245 + 432 + 4 + 0 + 30 | 15,711, equals printed; 15,760 - 15,711 = 49, equals printed |
| Nine months 2025 operating cost block | 14,951 + 400 + 92 + 39 + 63 | 15,545, equals printed; 14,297 - 15,545 = -1,248, equals printed |
| Q3 2026 operating cost block | 5,147 + 153 + 1 + 0 + 0 | 5,301, equals printed; 5,612 - 5,301 = 311, equals printed |
| Q3 2026 Total EBITDA | 165 + 148 + 46 + 259 | 618, equals printed |
| Q3 2026 Adjusted EBITDA | 618 - (19 - 4 - 4 - 15 + 14 - 2 - 2) = 618 - 6 | 612, equals printed |
| Nine months 2026 Adjusted EBITDA | 979 - (50 + 1 - 37 - 37 + 23 - 3 - 11) = 979 + 14 | 993, equals printed |
| FY2025 Adjusted EBITDA | -180 - (76 - 239 - 45 + 37 - 25 - 10 + 9 - 7 + 6 - 1 - 18) = -180 + 217 | 37, equals printed |
| Q3 2026 debt principal | 368 + 900 + 750 + 325 + 850 + 1,425 + 900 + 1,125 + 235 + 834 | 7,712, equals printed; less 67 is 7,645, equals printed |
| Q2 2026 operating cash flow | -95 - (-325) | 230, equals Release Q2 page:1 |
| Q3 2026 operating cash flow | 129 - (-95) | 224, equals Release Q3 page:8 |
| Q3 2026 ABL net repayment | 895 - 834 | 61, equals Release Q3 page:8 |
| Leases | 67 + 335 + 48 + 234 | 684, equals the 115 current plus 569 non-current in 10-K page:91 |
| Unconditional purchase obligations | 2,911 + 1,936 + 1,520 + 1,266 + 1,191 + 5,130 | 13,954 |

## Gaps

| Gap | Severity | Affected | Remediation |
| --- | --- | --- | --- |
| Indentures and ABL credit agreement not supplied; springing covenant trigger level and fixed charge definition not printed; covenant headroom Not calculable | High for covenant work | CP-2 | Supply executed documents. Until then, report only that the test was not applicable |
| No filing defines net debt or the management leverage ratio; the target wording differs between releases | Medium | CP-2 | Keep the analyst definition above and label management targets as management language |
| Adjusted EBITDA includes non-service pension and OPEB credits that are non-cash | Medium | CP-2 | Show both the reported and the ex-credit multiples |
| Property sale behind the expected fourth-quarter debt reduction not described in any filed source | Medium | CP-1A, CP-2 | Supply the relevant Form 8-K if one exists after October 20, 2026 |
| Lease balances and maturity table, pension funded status and unconditional purchase obligations are as of December 31, 2025 only; the 10-Q Q3 purchase commitment table is absent from the extracted text | Medium | CP-2 | Use the 10-K amounts and label them; check the filed 10-Q for the table |
| Sep 30, 2025 debt, cash and ABL balances not in the pack; prior-year quarter-end leverage not computable | Low | Chart data | Not needed for the selected views |
| ABL availability by U.S. and Canadian tranche not printed | Low | CP-2 | Supply borrowing base certificate or credit agreement |
| Capital expenditure outlook differs by horizon between releases and the Q3 10-Q | Low | CP-2 | Quote each statement separately |
| Events between October 20, 2026 and 2026-11-05 not supplied | Medium | CP-1A, CP-2 | Supply later 8-Ks or confirm none |
| Ratings, market capitalization, quotes: context fields blank | Low for this scope | CP-2 | Not supplied |

## Next module

- CP-1A: carry the business and transaction context from the 10-K and the 10-Q Q3 (POSCO Memorandum of Understanding subject to definitive agreements; Middletown Works DOE framework; Hamilton Works and Stelco idling wording as logged). Treat the property sale and the fourth-quarter debt reduction as management language, Not supplied in filings. Label events after October 20, 2026 Not supplied.
- CP-2: use the leverage and cover tables as LTM Adjusted EBITDA based, state that the multiple is a transition value, show the ex-pension-credit sensitivity beside it, and carry the covenant, indenture and lease-date limitations. Treat liquidity of 3,246 as ABL capacity plus cash, limited by the borrowing base.
- CP-5: check that every figure above resolves to a located statement line or a shown calculation, and that the quarterly Adjusted EBITDA series (95, 286, 612) matches across the 10-Qs and releases.
