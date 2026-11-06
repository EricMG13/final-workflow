## Request

Issuer: ENTEGRIS INC (Entegris, Inc. and subsidiaries, consolidated; NASDAQ: ENTG; issuer id entg). As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit snapshot. Reporting currency: USD; all filed amounts are in USD millions except per-share data. Current period: Q3 2026 (quarter ended September 26, 2026) and the last twelve months to that date (LTM Q3 2026); prior period: FY2025 (year ended December 31, 2025), with FY2024 as the earlier year.

Task: extract the financial base for the credit snapshot from the supplied filings and releases: statements, debt and maturity profile, liquidity, leverage, interest cover and cash flow, with the definition review and the gaps that restrict use. Source abbreviations used in locators: `10-K` (annual report FY2025), `Q1 10-Q`, `Q2 10-Q`, `Q3 10-Q` (quarterly reports for the quarters ended March 28, June 27 and September 26, 2026), `Q1 release`, `Q2 release`, `Q3 release` (earnings releases, Exhibit 99.1, dated April 30, August 4 and October 29, 2026). `page:N` is the chunk number of the pinned extraction, not the printed page.

Perimeter and basis. The issuer is the registrant itself, so the consolidated statements are the issuer's own statements and no parent or subsidiary substitution applies. Accounting basis: US GAAP; Adjusted EBITDA is the company's own non-GAAP measure (defined in the Definition review). "LTM Q3 2026" means FY2025 plus nine months 2026 less nine months 2025, with each input shown in Calculations. Debt in leverage ratios is principal (par) outstanding unless stated; carrying value is shown separately.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Relied on for |
| --- | --- | --- |
| `10-K_2025-12-31_entg-20251231.htm.jsonl` | `260dc4cc98d7ad114dcfe1b4d9e49beac9ed9f7c97f27f59e6df3a75c0628528` | FY2025 and FY2024 statements, Adjusted EBITDA reconciliation, debt note, leases, commitments, cash requirements |
| `10-Q_2026-03-28_entg-20260328.htm.jsonl` | `3b83d32b0eaaaa1280f7799359a8f16448b715b610a83c1edceec0d49387802a` | March 28, 2026 cash, revolver commitment, Q1 2026 flows |
| `10-Q_2026-06-27_entg-20260627.htm.jsonl` | `5d06fd99ce42692b479a85d0b3d96bd08dbc1bdd295141cd5adf69b1988058ed` | June 27, 2026 debt, revolver, covenant statement, six-month flows and interest paid |
| `10-Q_2026-09-26_entg-20260926.htm.jsonl` | `7b5685a1d8fe745548fe7c65968e18c36857c1e4dd7f2b8045f8166b689f4db9` | September 26, 2026 statements, debt note, maturities, liquidity, covenant, nine-month flows, non-GAAP reconciliation |
| `EX-99.1_2026-04-30_entgq12026ex991.htm.jsonl` | `0e10b62e7e542aab19ae90b6d94252e94c7183b272237a1b5ecd040e7a3bb9d7` | Discrete quarter ended December 31, 2025 and Q1 2026 figures |
| `EX-99.1_2026-08-04_entgq22026ex991.htm.jsonl` | `729b6288fa7f91f06fa1d1330da9031db0436138ba5a59730b16535055ac78c0` | Discrete Q2 2026 and Q2 2025 Adjusted EBITDA |
| `EX-99.1_2026-10-29_entgq32026ex991.htm.jsonl` | `e35116403bbcb30c3a986093aa969493d265b238a073d77c0b1aa4aec9296a99` | Discrete Q3 2026 figures and the fourth-quarter outlook |

Run settings (not issuer evidence): `context`, sha256 `a75dcef49bab6da60dc1054c04d1bf4409ccb60667119c9ab2f0bfc98a4c262f`.

### Upstream handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | `69484fc1896f94421c30f81bc1a11d139a430313a621007d9d0706850a8bf3c8` | Readiness view READY_WITH_LIMITATIONS; carries the unit-caption conflict, the covenant, letter-of-credit and guarantor gaps, and the useful-life and tariff-refund comparability flags |

Consistency with the upstream handoff. All of its limitations are carried forward below. Two corrections to CP-0. First, its gap G8 said the fourth quarter of 2025 is not presented on its own. The Q1 release does print a discrete column for the quarter ended December 31, 2025 (net sales $823.9, Adjusted EBITDA $228.1; `Q1 release page:5`, `page:7`), and it agrees with the figure derived from the annual and nine-month numbers (see Calculations, C1). Second, CP-0 cited the first-quarter statement of covenant compliance at `page:27` of the Q1 10-Q; it is at `page:28`.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Leverage on par debt over company-defined Adjusted EBITDA fell from 4.34x at FY2024 to 3.27x on an LTM Q3 2026 basis, helped by the term loan repayment and higher earnings. Liquidity and cash flow are strong. | Medium | Covenant EBITDA, revolver letters of credit and the covenant test threshold are not supplied, so covenant headroom and net revolver availability cannot be calculated. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Par debt fell to $3,295.0 million at September 26, 2026 from $3,745.0 million at December 31, 2025 as the term loan was repaid; the remaining debt is fixed-rate notes. | Floating-rate exposure is gone, and 2029 holds $2,000.0 million of maturities, the largest wall. | High |
| LTM Q3 2026 Adjusted EBITDA is $1,008.2 million against $886.2 million for FY2025; net debt over Adjusted EBITDA is 2.91x against 3.82x. | Deleveraging came from higher earnings and lower debt; Adjusted EBITDA is a company-defined measure. | Medium |
| Cash is $356.5 million and the undrawn revolver commitment is $750.0 million, but only $58.3 million of the cash is held in the U.S. | Liquidity looks ample before letters of credit, which are not supplied; U.S. cash is small beside the revolver. | Medium |
| LTM cash interest paid is $181.1 million, giving cover of 5.57x against 4.78x for FY2025; the remaining notes carry about $161.3 million of annual coupons. | Cash interest burden is falling as floating-rate debt is repaid, which supports debt service. | Medium |
| Free cash flow after capital spending was $616.0 million LTM Q3 2026, as capital spending fell. | Cash generation covers debt reduction and dividends, but the capital spending decline may reverse. | Medium |

### Financial base view

The financial base is usable for a credit snapshot, with the limits stated below. Everything rests on filed, consolidated statements of Entegris, Inc. and subsidiaries in USD millions, supplemented by the company's own non-GAAP Adjusted EBITDA, which the filings reconcile to GAAP. On that basis, principal debt fell from $4,045.0 at FY2024 to $3,745.0 at FY2025 and $3,295.0 at September 26, 2026, while LTM Adjusted EBITDA rose from $886.2 (FY2025) to $1,008.2, so total debt over Adjusted EBITDA moved from 4.34x to 4.23x to 3.27x. The nine-month 2026 debt reduction is entirely term loan B repayment of $450.0; every remaining instrument is a fixed-rate note, the revolver is undrawn, and maturities start in 2028. Interest cover on cash interest paid is 5.57x LTM. Three things restrict the view. First, Adjusted EBITDA is management-defined and the covenant definition is not supplied, so covenant headroom is not calculable; the filing states compliance and a 5.20 to 1.00 first lien net leverage maximum that is tested only above a revolver utilisation threshold that is not printed. Second, letters of credit under the revolver are not supplied, so undrawn availability is shown before them. Third, 2026 operating income and margin are not like-for-like with 2025 because of the January 2026 change in useful lives, while Adjusted EBITDA adds depreciation back and is unaffected by it. The annual report's thousands captions on millions amounts are a known unit-label conflict, resolved by the Q3 10-Q statement that amounts are in millions (`10-K page:120`, `Q3 10-Q page:9`).

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 4.34 | 3.99 | x | Par debt 4045.0 and cash 329.2 at December 31, 2024 over company Adjusted EBITDA 931.1. Excludes leases. Adjusted EBITDA is non-GAAP and management-defined; covenant EBITDA not supplied. |
| FY2025 | 4.23 | 3.82 | x | Par debt 3745.0 and cash 360.4 at December 31, 2025 over Adjusted EBITDA 886.2. Excludes leases of 114.4. Same definition limits. |
| LTM Q2 2026 | 3.78 | 3.39 | x | Par debt 3495.0 and cash 353.6 at June 27, 2026 over LTM Adjusted EBITDA 925.6 (FY2025 plus six months 2026 less six months 2025). Same definition limits. |
| LTM Q3 2026 | 3.27 | 2.91 | x | Par debt 3295.0 and cash 356.5 at September 26, 2026 over LTM Adjusted EBITDA 1008.2. Cash includes 298.2 held outside the U.S. Excludes leases; same definition limits. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 4.67 | x | Adjusted EBITDA 931.1 over interest paid net of capitalized interest 199.2. Cash interest paid is lumpy (4.6 in Q1 2026, 89.3 over six months, 90.4 over nine months); Adjusted EBITDA is management-defined. |
| FY2025 | 4.78 | x | Adjusted EBITDA 886.2 over interest paid 185.4. Same limits. |
| LTM Q2 2026 | 4.88 | x | LTM Adjusted EBITDA 925.6 over LTM interest paid 189.7 (185.4 plus 89.3 less 85.0). Same limits. |
| LTM Q3 2026 | 5.57 | x | LTM Adjusted EBITDA 1008.2 over LTM interest paid 181.1 (185.4 plus 90.4 less 94.7). On LTM interest expense of 191.4 the same ratio is 5.27x. Same limits. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 329.2 | Not supplied: the revolver commitment at December 31, 2024 is not dated in the pack (borrowings were nil) | US$m | Cash and cash equivalents per balance sheet. Letters of credit not supplied. |
| FY2025 | 360.4 | 575.0 | US$m | Commitments 575.0 less borrowings nil at December 31, 2025. Shown before letters of credit, which are not supplied, so availability may be lower. Revolver due 2027, 575.0 commitments. |
| Q1 2026 | 442.7 | 575.0 | US$m | At March 28, 2026: commitments 575.0, no borrowings. Before letters of credit (not supplied). The April 29, 2026 amendment came after this date. |
| Q2 2026 | 353.6 | 750.0 | US$m | At June 27, 2026: commitments 750.0 after the April 29, 2026 amendment, no borrowings. Before letters of credit (not supplied). |
| Q3 2026 | 356.5 | 750.0 | US$m | At September 26, 2026: commitments 750.0, maturity April 29, 2031, no borrowings. Before letters of credit (not supplied). 298.2 of cash is outside the U.S. A yen line of about 6.3 is excluded because its committed status is not stated. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remaining 2026 | 0.0 | US$m | Printed as a dash in the Q3 10-Q maturity table; the row sums to the printed total of 3295.0, so nil. Par value at September 26, 2026. |
| 2027 | 0.0 | US$m | Printed as a dash; same basis. The prior revolver maturity of July 2027 was extended. |
| 2028 | 400.0 | US$m | Senior unsecured notes 4.375%. |
| 2029 | 2000.0 | US$m | Senior secured notes 4.75% of 1600.0 plus senior unsecured notes 3.625% of 400.0; the term loans B due 2029 are repaid. |
| 2030 | 895.0 | US$m | Senior unsecured notes 5.95%. |
| Thereafter | 0.0 | US$m | Printed as a dash. The undrawn 750.0 revolver matures April 29, 2031 and carries no balance. |

### Financials and credit metrics

| Metric (USD millions unless stated) | FY2024 | FY2025 | 9M 2025 | 9M 2026 | LTM Q3 2026 | Source and basis |
| --- | --- | --- | --- | --- | --- | --- |
| Net sales | 3,241.2 | 3,196.6 | 2,372.7 | 2,700.8 | 3,524.7 | `10-K page:106`; `Q3 10-Q page:5`; LTM derived (C2) |
| Gross profit | 1,486.7 | 1,419.9 | 1,059.3 | 1,301.0 | 1,661.6 | Same; LTM derived |
| Operating income (GAAP) | 533.9 | 455.9 | 351.0 | 536.8 | 641.7 | Same; 2026 benefits from lower depreciation (useful-life change, conflict C6 in CP-0) |
| Depreciation | 188.1 | 205.3 | 151.6 | 102.4 | 156.1 | `10-K page:107`; `Q3 10-Q page:7`; LTM derived |
| Amortization of intangibles | 190.1 | 184.4 | 138.1 | 138.0 | 184.3 | `10-K page:106`; `Q3 10-Q page:5`; LTM derived |
| EBITDA, unadjusted (operating income + depreciation + amortization) | 912.1 | 845.6 | 640.7 | 777.2 | 982.1 | Calculated (C3); before restructuring, impairment, disposal and refund items |
| Adjusted EBITDA (company, non-GAAP) | 931.1 | 886.2 | 658.1 | 780.1 | 1,008.2 | `10-K page:85`; `Q3 10-Q page:38`; LTM derived (C1) |
| Adjusted EBITDA margin (%) | 28.7 | 27.7 | 27.7 | 28.9 | 28.6 | As printed for years and periods (`10-K page:85`, `Q3 10-Q page:29`); LTM calculated (C2) |
| Net income | 292.8 | 235.6 | 186.2 | 343.4 | 392.8 | `10-K page:106`; `Q3 10-Q page:5`; LTM derived |
| Interest expense (gross) | 215.2 | 199.8 | 151.3 | 142.9 | 191.4 | `10-K page:106`; `Q3 10-Q page:5`; LTM derived |
| Interest paid, net of capitalized interest | 199.2 | 185.4 | 94.7 | 90.4 | 181.1 | `10-K page:108`; `Q3 10-Q page:7`; LTM derived |
| Income taxes paid, net | 103.8 | 113.0 | 108.6 | 90.3 | 94.7 | Same; LTM derived |
| Net cash from operating activities | 631.7 | 695.4 | 503.4 | 606.0 | 798.0 | `10-K page:108`; `Q3 10-Q page:7`; LTM derived |
| Acquisition of property, plant and equipment (capex) | 315.6 | 299.2 | 241.2 | 124.0 | 182.0 | Same; shown as a positive outflow |
| Free cash flow (operating cash flow less capex) | 316.1 | 396.2 | 262.2 | 482.0 | 616.0 | Calculated (C4); company does not print this measure |
| Dividends paid | 60.6 | 60.8 | 45.7 | 46.2 | 61.3 | `10-K page:108`; `Q3 10-Q page:7`; LTM derived |
| Cash and cash equivalents (period end) | 329.2 | 360.4 | n/a (flow period) | 356.5 | 356.5 | `10-K page:105`; `Q3 10-Q page:4` |
| Principal debt (par, period end) | 4,045.0 | 3,745.0 | n/a (flow period) | 3,295.0 | 3,295.0 | `10-K page:120`; `Q3 10-Q page:11` |
| Debt, carrying value net of discount and costs | 3,981.1 | 3,697.6 | n/a (flow period) | 3,260.6 | 3,260.6 | Same; 34.4 of discount and costs at September 26, 2026 |
| Net debt (par less cash) | 3,715.8 | 3,384.6 | n/a (flow period) | 2,938.5 | 2,938.5 | Calculated (C5) |
| Total debt / Adjusted EBITDA (x) | 4.34 | 4.23 | n/a (flow period) | n/a (flow period) | 3.27 | Calculated (C5) |
| Net debt / Adjusted EBITDA (x) | 3.99 | 3.82 | n/a (flow period) | n/a (flow period) | 2.91 | Calculated (C5) |
| Total debt / unadjusted EBITDA (x) | 4.43 | 4.43 | n/a (flow period) | n/a (flow period) | 3.36 | Calculated (C3); shows sensitivity to the Adjusted EBITDA definition |
| Adjusted EBITDA / interest paid (x) | 4.67 | 4.78 | n/a (flow period) | n/a (flow period) | 5.57 | Calculated (C5) |
| Adjusted EBITDA / gross interest expense (x) | 4.33 | 4.44 | n/a (flow period) | n/a (flow period) | 5.27 | Calculated (C5) |
| Free cash flow / par debt (%) | 7.8 | 10.6 | n/a (flow period) | n/a (flow period) | 18.7 | Calculated (C4); FY2024 and FY2025 use the same-year par debt |

### Discrete quarters

| Quarter | Net sales | Operating income | Net income | Adjusted EBITDA | Adjusted EBITDA margin (%) | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 2025 (Mar 29, 2025) | 773.2 | 122.3 | 62.9 | 220.7 | 28.5 | `Q1 release page:5`, `page:7` |
| Q2 2025 (Jun 28, 2025) | 792.4 | 106.1 | 52.8 | 216.7 | 27.3 | `Q2 10-Q page:5`; `Q2 release page:8` |
| Q3 2025 (Sep 27, 2025) | 807.1 | 122.6 | 70.5 | 220.7 | 27.3 | `Q3 10-Q page:5`; `Q3 release page:5`, `page:8` |
| Q4 2025 (Dec 31, 2025) | 823.9 | 104.9 | 49.4 | 228.1 | 27.7 | `Q1 release page:5`, `page:7` |
| Q1 2026 (Mar 28, 2026) | 811.9 | 141.6 | 92.0 | 226.1 | 27.8 | `Q1 10-Q page:5`; `Q1 release page:5`, `page:7` |
| Q2 2026 (Jun 27, 2026) | 883.2 | 164.6 | 93.6 | 250.7 | 28.4 | `Q2 10-Q page:5`; `Q3 release page:5`, `page:8` |
| Q3 2026 (Sep 26, 2026) | 1,005.7 | 230.6 | 157.8 | 303.3 | 30.2 | `Q3 10-Q page:5`, `page:38`; `Q3 release page:5`, `page:8` |

Net sales in Q3 2026 are the highest of the seven quarters shown, and Adjusted EBITDA margin rose in each 2026 quarter shown (27.8%, 28.4%, 30.2%). Management calls the quarter "record revenue" (`Q3 release page:1`); that is attributed management language and is not tested against quarters outside the pack. Year on year, Q3 net sales rose 24.6% from 807.1 to 1,005.7, which the 10-Q attributes primarily to volume of 205.8 (`Q3 10-Q page:23`).

### Segments

| Segment | FY2024 net sales | FY2025 net sales | 9M 2025 net sales | 9M 2026 net sales | FY2025 segment profit | 9M 2025 segment profit | 9M 2026 segment profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Materials Solutions | 1,400.1 | 1,406.7 | 1,044.9 | 1,126.5 | 276.6 | 212.7 | 237.9 |
| Advanced Purity Solutions | 1,850.2 | 1,799.1 | 1,334.6 | 1,583.1 | 426.4 | 322.2 | 497.2 |
| Inter-segment elimination | not shown here | not shown here | (6.8) | (8.8) | not applicable | not applicable | not applicable |

Sources: `10-K page:77`; `Q3 10-Q page:15`, `page:29`. FY2024 segment profit was 286.2 for Materials Solutions and 496.1 for Advanced Purity Solutions (`10-K page:77`). Unallocated general and administrative expense was 62.7 in FY2025 and 60.3 in nine months 2026 (`10-K page:77`; `Q3 10-Q page:15`). Advanced Purity Solutions segment profit rose from 322.2 to 497.2 over nine months, against sales growth from 1,334.6 to 1,583.1; the 10-Q attributes the profit increase to higher gross profit on higher sales, lower depreciation from the useful-life change and tariff refunds, partly offset by variable compensation (`Q3 10-Q page:31`).

### Capital structure and debt schedule

| Instrument | Par at Sep 26, 2026 | Par at Dec 31, 2025 | Rate | Maturity | Security and role |
| --- | --- | --- | --- | --- | --- |
| Senior secured notes due 2029 | 1,600.0 | 1,600.0 | 4.75% fixed | 2029 (month not printed in the pack) | Secured; issuer Entegris, Inc.; guarantee by "certain subsidiaries" per exhibit list only (`10-K page:96`-`page:97`) |
| Senior notes due 2030 | 895.0 | 895.0 | 5.95% fixed | 2030 | Senior unsecured per the annual report label (`10-K page:120`) |
| Senior notes due 2029 | 400.0 | 400.0 | 3.625% fixed (printed 3.63% in the Q3 10-Q) | 2029 | Senior unsecured |
| Senior notes due 2028 | 400.0 | 400.0 | 4.375% fixed (printed 4.38% in the Q3 10-Q) | 2028 | Senior unsecured |
| Term loans B due 2029 | 0.0 | 450.0 | 4.88% at Dec 31, 2025; 5.43% at Mar 28, 2026; 5.40% at Jun 27, 2026 (SOFR plus margin) | 2029 | Senior secured; repaid in full: 50.0 in Q1, 200.0 in Q2 and 200.0 in Q3 2026 |
| Revolving credit facility due 2031 | 0.0 drawn of 750.0 | 0.0 drawn of 575.0 | SOFR plus 1.25% (margin tier at Sep 26, 2026) | April 29, 2031 | Senior secured revolver; amended April 29, 2026 from 575.0 and July 6, 2027 |
| Total par | 3,295.0 | 3,745.0 | | | Q3 10-Q page:11; 10-K page:120 |

Sources for the quarterly term loan repayments: `Q1 10-Q page:11`, `Q2 10-Q page:12`, `Q3 10-Q page:12`. Carrying value is 3,260.6 against par 3,295.0 (discount and costs 34.4); fair value is 3,176.1 (`Q3 10-Q page:13`). The sources print no co-issuers, no guarantor amounts and no month of maturity for the notes; the equal priority intercreditor agreement among the credit facility and notes collateral agents is listed as an exhibit (`10-K page:97`), which indicates equal-priority liens but is not a term the pack documents.

### Maturity wall

Principal due by year at September 26, 2026 is nil to 2027, 400.0 in 2028, 2,000.0 in 2029 and 895.0 in 2030 (`Q3 10-Q page:11`). The 2029 maturity is 60.7% of par debt (C7). Nothing falls due within twelve months of the as-of date, and the revolver is undrawn, so refinancing risk sits in 2028 to 2030.

### Liquidity and claims outside the debt figure

| Item | Amount | Inside the par debt figure? | Source |
| --- | --- | --- | --- |
| Cash and cash equivalents, September 26, 2026 | 356.5 (U.S. 58.3; non-U.S. 298.2) | Not applicable | `Q3 10-Q page:4`, `page:34` |
| Undrawn revolver commitment | 750.0 before letters of credit | Not applicable | `Q3 10-Q page:12`, `page:34` |
| Liquidity as cash plus undrawn commitment | 1,106.5 (C6); before letters of credit | Not applicable | Calculated |
| Facilities expiring within twelve months | None: revolver April 29, 2031; yen line (about 6.3, undrawn) has no stated expiry | Not applicable | `Q3 10-Q page:12`, `page:34` |
| Lease liabilities at December 31, 2025 | 114.4 (operating 95.4, finance 19.0) | Outside; latest dated detail | `10-K page:124`; Q3 10-Q shows long-term lease liabilities of 100.4 (`page:4`) |
| Capital purchase obligations at December 31, 2025 | 60.0 (42.5 within one year) | Outside | `10-K page:81` |
| Supply purchase obligations at December 31, 2025 | 150.5 (88.1 within one year) | Outside | `10-K page:81` |
| Interest payments on long-term debt at December 31, 2025 | 655.3 (184.5 within one year) | Outside | `10-K page:81` |
| Income tax liabilities at December 31, 2025 | 123.2, of which uncertain positions 33.7 | Outside | `10-K page:81`-`page:82` |
| Asset retirement obligations at December 31, 2025 | 32.5 | Outside | `10-K page:124` |
| Pension: net amount recognized, December 31, 2025 | 7.6 shortfall (table captioned in thousands, values consistent with millions) | Outside | `10-K page:135` |
| Pension benefit obligations and other liabilities, September 26, 2026 | 80.0 (combined line) | Outside | `Q3 10-Q page:4` |
| Accrued interest payable, September 26, 2026 | 64.9, against 24.3 at December 31, 2025 | Outside par debt | `Q3 10-Q page:4` |
| Litigation | None expected to be material | Not applicable | `10-K page:139`; `Q3 10-Q page:40` |
| Factoring, supply chain finance, lease financing of the issuer | Searched all sources: none found | Not applicable | Not supplied |

Capital expenditure was guided to about 250.0 for 2026 in the annual report (`10-K page:82`); nine-month 2026 capex was 124.0 (`Q3 10-Q page:7`), so the annual guide in the pack is not a measure of the fourth-quarter run rate and no updated capex guidance is printed.

### Covenants

The credit agreement for the revolver and term loan (the "Amended Credit Agreement") contains a maximum first lien net leverage ratio of 5.20 to 1.00, tested only when utilisation of the revolver exceeds a specified threshold; the company states compliance through September 26, 2026 (`Q3 10-Q page:34`; same wording in `Q2 10-Q page:31`; `Q1 10-Q page:28` states compliance without a level). The threshold is not printed, the reported ratio is not printed, and no step-down is described. The revolver margin tiers depend on the same first lien net leverage ratio, and the margin fell from 1.50% (SOFR) at June 27, 2026 to 1.25% at September 26, 2026 (`Q2 10-Q page:12`; `Q3 10-Q page:12`), which is consistent with improving first lien leverage but does not give the ratio. An illustrative figure only: if the 1,600.0 secured notes are first lien debt and cash is fully netted, first lien net debt over LTM Adjusted EBITDA is 1.23x (C8); the covenant definition of debt, cash netting and EBITDA are not supplied, so this is not covenant headroom and no headroom is stated. Other restrictions are summarised in the annual report risk factors: restrictions on debt, dividends, investments, liens and asset sales, and incremental capacity up to the greater of $1.1 billion or 100% of EBITDA plus amounts subject to a secured net leverage test (`10-K page:54`); the indentures carry limited covenants on secured debt, sale-leasebacks and restricted subsidiary debt (`10-K page:56`).

### Latest quarter and subsequent events

- Debt: the remaining 200.0 of term loans B was repaid in Q3 2026, including a voluntary 25 payment made on July 31, 2026 (`Q2 10-Q page:17`; `Q3 10-Q page:12`); the 25 payment was disclosed as a subsequent event in the Q2 10-Q, and the loss on extinguishment was 1.7 in the quarter and 3.9 over nine months (`Q3 10-Q page:12`).
- Revolver: amended April 29, 2026, with commitments raised to 750.0 from 575.0, maturity extended to April 29, 2031 from July 6, 2027, and revised margins, commitment fees and certain negative covenants (`Q3 10-Q page:12`, `page:22`).
- Operating items: an equity investment impairment of 6.7 (first nine months, recorded in the second quarter per `Q3 release page:9`); restructuring of 11.2 over nine months, including the planned wind-down of Life Sciences Fluid Management (`Q3 10-Q page:16`); 8.3 of IEEPA tariff refunds in Q3 recognised in cost of sales and excluded from non-GAAP results (`Q3 10-Q page:38`).
- Subsequent events: a dividend of $0.10 per share declared October 14, 2026, payable November 18, 2026 (`Q3 10-Q page:17`); no other subsequent event is disclosed.
- Outlook (management expectation, not fact): fourth-quarter 2026 sales of 1,025 to 1,055 and Adjusted EBITDA of 315 to 329 (`Q3 release page:10`); a Capital Markets Day on November 9, 2026 is after the as-of date (`Q3 release page:1`).

### Definition review

- Adjusted EBITDA is defined as net income adjusted to exclude equity in net loss of affiliates, income tax expense, interest expense, interest income, other expense net, depreciation and Special Items (`10-K page:83`). It does not list share-based compensation as an adjustment, and the reconciliations show none (`Q3 10-Q page:38`: 54.8 of share-based compensation over nine months stays in Adjusted EBITDA).
- The 2026 nine-month add-backs are restructuring of 11.2 and an IEEPA refund deduction of (8.3), plus amortization of 138.0 and depreciation of 102.4 (`Q3 10-Q page:38`). FY2025 add-backs were restructuring of 29.7 and a loss on business sale of 10.9 (`10-K page:85`).
- The difference between Adjusted EBITDA and unadjusted EBITDA (operating income plus depreciation and amortization) is 40.6 for FY2025 (886.2 less 845.6, equal to restructuring of 29.7 plus the loss on business sale of 10.9), 19.0 for FY2024, 17.4 for nine months 2025 and 2.9 for nine months 2026 (C3), so management adjustments are small and shrinking in 2026.
- The January 2026 useful-life change cut depreciation by 55.6 over nine months 2026 (`Q3 10-Q page:9`); it lifts GAAP operating income and net income but not Adjusted EBITDA, which adds depreciation back.
- The releases net interest income against interest expense ("Interest expense, net" of 43.9 in Q3 2026 in `Q3 release page:5`); this module uses the gross filed lines (45.4 and 1.5 income, `Q3 10-Q page:5`).
- Covenant EBITDA, first lien net debt and the utilisation threshold are not supplied; any comparison with the 5.20 to 1.00 maximum is therefore Not calculable here.

### Cash flow quality

Operating cash flow was 606.0 in nine months 2026 against 503.4 in nine months 2025, helped by a 266.7 inflow from accounts payable and accrued liabilities that offset outflows of 167.5 in receivables and 153.2 in inventories (`Q3 10-Q page:7`); the working-capital inflow is partly timing of vendor payments and incentive accrual (`Q3 10-Q page:33`), so LTM free cash flow of 616.0 may include timing support. Cash interest paid (90.4 over nine months) is far below gross interest expense (142.9) because accrued interest payable rose to 64.9 from 24.3 (`Q3 10-Q page:4`); the 52.5 gap is mostly that accrual build of 40.6 (C11) plus 9.6 of non-cash amortization of debt costs (`Q3 10-Q page:7`). Net cash used in financing was 486.8, of which 450.0 was term loan repayment and 46.2 dividends (`Q3 10-Q page:7`).

## Calculations

Every input is a filed figure with the locator shown in the tables above. Results are rounded to the precision shown.

| Ref | Calculation | Inputs | Result |
| --- | --- | --- | --- |
| C1 | LTM Adjusted EBITDA, Q3 2026 | FY2025 886.2 + nine months 2026 780.1 − nine months 2025 658.1 | 1,008.2. Cross-check by quarters: 228.1 + 226.1 + 250.7 + 303.3 = 1,008.2 |
| C1a | LTM Adjusted EBITDA, Q2 2026 | FY2025 886.2 + six months 2026 476.8 − six months 2025 437.4 (`Q2 10-Q page:27`) | 925.6 |
| C1b | Q4 2025 Adjusted EBITDA implied | FY2025 886.2 − nine months 2025 658.1 | 228.1, equal to the printed discrete column in the Q1 release |
| C2 | LTM flows | Net sales 3,196.6 + 2,700.8 − 2,372.7; gross profit 1,419.9 + 1,301.0 − 1,059.3; operating income 455.9 + 536.8 − 351.0; net income 235.6 + 343.4 − 186.2; interest expense 199.8 + 142.9 − 151.3; operating cash flow 695.4 + 606.0 − 503.4; capex 299.2 + 124.0 − 241.2; dividends 60.8 + 46.2 − 45.7; taxes paid 113.0 + 90.3 − 108.6; depreciation 205.3 + 102.4 − 151.6; amortization 184.4 + 138.0 − 138.1 | 3,524.7; 1,661.6; 641.7; 392.8; 191.4; 798.0; 182.0; 61.3; 94.7; 156.1; 184.3. LTM margin 1,008.2 / 3,524.7 = 28.6%. Net sales cross-check by quarters: 823.9 + 811.9 + 883.2 + 1,005.7 = 3,524.7 |
| C3 | Unadjusted EBITDA (operating income + depreciation + amortization) | FY2024 533.9 + 188.1 + 190.1; FY2025 455.9 + 205.3 + 184.4; nine months 2025 351.0 + 151.6 + 138.1; nine months 2026 536.8 + 102.4 + 138.0 | 912.1; 845.6; 640.7; 777.2. LTM 845.6 + 777.2 − 640.7 = 982.1. Total debt / unadjusted EBITDA: 4,045.0 / 912.1 = 4.43x; 3,745.0 / 845.6 = 4.43x; 3,295.0 / 982.1 = 3.36x |
| C4 | Free cash flow = operating cash flow less acquisition of property, plant and equipment | FY2024 631.7 − 315.6; FY2025 695.4 − 299.2; nine months 2025 503.4 − 241.2; nine months 2026 606.0 − 124.0; LTM 798.0 − 182.0 | 316.1; 396.2; 262.2; 482.0; 616.0. FCF / par debt: 316.1 / 4,045.0 = 7.8%; 396.2 / 3,745.0 = 10.6%; 616.0 / 3,295.0 = 18.7%. After LTM dividends of 61.3: 554.7 |
| C5 | Leverage and cover | Par debt less cash: 4,045.0 − 329.2 = 3,715.8; 3,745.0 − 360.4 = 3,384.6; 3,495.0 − 353.6 = 3,141.4; 3,295.0 − 356.5 = 2,938.5. Total debt / Adjusted EBITDA: 4,045.0 / 931.1 = 4.34x; 3,745.0 / 886.2 = 4.23x; 3,495.0 / 925.6 = 3.78x; 3,295.0 / 1,008.2 = 3.27x. Net: 3,715.8 / 931.1 = 3.99x; 3,384.6 / 886.2 = 3.82x; 3,141.4 / 925.6 = 3.39x; 2,938.5 / 1,008.2 = 2.91x | Cover on cash interest: 931.1 / 199.2 = 4.67x; 886.2 / 185.4 = 4.78x; 925.6 / 189.7 = 4.88x (LTM interest paid 185.4 + 89.3 − 85.0 = 189.7); 1,008.2 / 181.1 = 5.57x (181.1 = 185.4 + 90.4 − 94.7). On gross interest expense: 931.1 / 215.2 = 4.33x; 886.2 / 199.8 = 4.44x; 1,008.2 / 191.4 = 5.27x |
| C6 | Liquidity at September 26, 2026 | Cash 356.5 + undrawn commitment 750.0 (750.0 − 0.0 borrowed) | 1,106.5 before letters of credit (Not supplied) |
| C7 | 2029 share of par debt | (1,600.0 + 400.0) / 3,295.0 | 60.7% |
| C8 | Illustrative first lien net leverage (not covenant) | (secured notes 1,600.0 + revolver 0.0 − cash 356.5) / 1,008.2 | 1.23x; gross 1,600.0 / 1,008.2 = 1.59x |
| C9 | Annual coupon on remaining notes | 1,600.0 × 4.75% + 895.0 × 5.95% + 400.0 × 3.625% + 400.0 × 4.375% = 76.0 + 53.3 + 14.5 + 17.5 | 161.3 (about 4.89% of par); LTM Adjusted EBITDA 1,008.2 / 161.3 = 6.25x, illustrative and excluding revolver fees |
| C10 | Debt change and fair value ratio | Par 3,745.0 − 3,295.0 = 450.0 repaid; fair value 3,176.1 / par 3,295.0 | 450.0 (term loans B); 96.4% |
| C11 | Accrued interest build | 64.9 − 24.3 | 40.6 |

## Gaps

| Ref | Gap | Effect | Action |
| --- | --- | --- | --- |
| F1 | Covenant EBITDA, first lien net debt definition, the revolver utilisation threshold and the reported covenant ratio are not supplied (searched all sources; only the 5.20 to 1.00 level and a compliance statement are printed). | Covenant headroom is Not calculable. | Obtain the credit agreement and compliance certificate. |
| F2 | Letters of credit under the revolver are not supplied. | Undrawn availability is shown before letters of credit and may be overstated; liquidity of 1,106.5 is an upper bound. | Obtain the letter-of-credit balance. |
| F3 | Guarantors, co-issuers, collateral package and notes maturity months are not supplied in text. | Structural priority and recovery analysis cannot be built beyond instrument labels. | Add the indentures and subsidiary list if needed. |
| F4 | Lease, pension, purchase obligation and tax detail is as of December 31, 2025 only; the interim reports have no such notes. | Those claims are stale by nine months; the Q3 10-Q states no material change in cash requirements outside the term loan repayment (`page:35`). | Label as of December 31, 2025. |
| F5 | The unit-caption conflict in the annual report remains (thousands captions on millions amounts). | Handled by treating all amounts as millions; the pension table has the same caption. | Carry as a stated limitation. |
| F6 | Adjusted EBITDA is management-defined and adds back restructuring and other items; no covenant or lender definition is available. | Leverage and cover are on the company's own definition; unadjusted EBITDA gives 3.36x total leverage LTM Q3 2026. | Show both, as in the metrics table. |
| F7 | The FY2024 revolver commitment at December 31, 2024 is not dated in the pack. | The FY2024 undrawn facility is Not supplied. | None needed for the current view. |
| F8 | Interest paid is lumpy by coupon date and a dash for the first quarter of 2025 appears in the Q1 10-Q, so no LTM Q1 2026 cover ratio is given. | Cover is shown for FY2024, FY2025, LTM Q2 2026 and LTM Q3 2026 only. | None needed. |
| F9 | 2026 operating income and net income are flattered by the useful-life change and tariff refunds; the fourth-quarter outlook is management expectation. | Margin comparison with 2025 is not like-for-like at operating income level. | Use Adjusted EBITDA for trend and flag the change. |

## Next module

Pass to the business and transaction context module with: the readiness limits from CP-0 and this handoff, the leverage path (4.34x FY2024, 4.23x FY2025, 3.27x LTM Q3 2026 on par debt over Adjusted EBITDA), the debt schedule and 2028 to 2030 maturity wall, liquidity of 1,106.5 before letters of credit, and the open gaps F1 to F3 (covenant, letters of credit, guarantor structure). The business module should treat Adjusted EBITDA as management language, use the segment table above for mix (Advanced Purity Solutions profit growth is the main driver), and not describe any sponsor, parent or deal terms, since none are supplied. The synthesis module must not state covenant headroom or net revolver availability, and should flag the useful-life change and the unit-caption conflict wherever 2026 margins or the annual report notes are cited.
