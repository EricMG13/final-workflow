## Request

Module CP-1, financial base and credit metrics, for ADVANCE AUTO PARTS INC (issuer id aap, registrant Advance Auto Parts, Inc., consolidated with subsidiaries), pathway credit_snapshot, as-of date 2026-11-05, cutoff 2026-11-05, reporting currency USD in millions. The module extracts the reported financial base from the pinned filings and releases, calculates leverage, interest cover, liquidity and maturity data with every input shown, and carries the source-readiness limitations from the upstream handoff.

Period labelling follows the filings, not the context labels q2-2027 and fy-2026, which match no period in the pack (see the upstream handoff). The periods used are FY2025 (fifty-three weeks ended January 3, 2026), Q1 FY2026 (sixteen weeks ended April 25, 2026), Q2 FY2026 (twelve weeks ended July 18, 2026), Q3 FY2026 (twelve weeks ended October 10, 2026), forty weeks ended October 10, 2026 and October 4, 2025, and last-twelve-months (LTM) periods ending on each 2026 quarter end. Fiscal quarters are sixteen weeks for the first and twelve weeks for the others. The perimeter is the consolidated company; no separate issuer, borrower or guarantor statements exist in the sources.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2026-01-03_aap-20260103.htm.jsonl | 88f0e66024a1a4e436956477a1b2bdacaf04082e37a839a013e4cf7b08a76ecc | FY2025 statements, debt table and maturities, ABL terms, covenant description, leases, supplier finance |
| 10-Q_2026-04-25_aap-20260425.htm.jsonl | b2dda8d971a035721b55c0b12971db6aed3046b92a0ea3374bd34ecc4d16e660 | Sixteen weeks ended April 25, 2026 statements and ABL availability |
| 10-Q_2026-07-18_aap-20260718.htm.jsonl | d30e886360cdf677d2862f5aa362e3322f6a90f56e6bf5994651f2a56dce1ba0 | Twelve and twenty-eight weeks ended July 18, 2026 statements |
| 10-Q_2026-10-10_aap-20261010.htm.jsonl | 32c4d101ba1517004b623cd5dd9218257b19e48552a751844ca10c65f72b2dcf | Twelve and forty weeks ended October 10, 2026 statements, debt note, liquidity, MD&A |
| EX-99.1_2026-05-21_aap-ex99_1.htm.jsonl | 281142b5117a0fb7df01ee4cf7cccfd81f8a80502e2274192453a4d9bcd9063f | Management net leverage reconciliation, four quarters ended April 25, 2026 |
| EX-99.1_2026-08-20_aap-ex99_1.htm.jsonl | 6fa6d0f76f705af9a8078a4e1b4a20159ae0682aa896d374dffc425d834ff4a2 | Management net leverage reconciliation, four quarters ended July 18, 2026 |
| EX-99.1_2026-11-05_aap-ex99_1.htm.jsonl | de47b06e79c571c89947b08d25437b94293b8641bb8475120032ad32f61878b9 | Management net leverage reconciliation, free cash flow, guidance, subsequent dividend |

The context input (sha256 ffcc1267b075abb958b7ec70e65c9102a0d2613c38bcd4fb41ec20b2a4c808c3) holds the requester's settings and is not issuer evidence.

### Handoffs

| Module | sha256 | Used for |
| --- | --- | --- |
| CP-0 | 29209c406c3dbcb47beef8e7094c9acab8905f427370b8271dbe27c2816b6d03 | Source readiness, period-label mismatch, gaps G1 to G11. It was read in full and its limitations are carried below. |

### Short names

10-K FY2025, 10-Q Q1, 10-Q Q2, 10-Q Q3, Release Q1, Release Q2 and Release Q3 name the seven sources in table order. A locator `page:N` is the chunk number in the pinned file, not the printed page. This answer corrects nothing in the upstream handoff; where it adds detail (for example the maturity wall), it builds on gaps the handoff recorded.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Debt is fixed-rate unsecured notes with an undrawn secured revolver, and cash exceeds debt. Earnings are thin: last-twelve-month reported EBITDA of 508 gives gross leverage of 6.67x but net leverage of 0.60x. | Medium | EBITDA is a simple reported measure that includes restructuring charges, and no covenant ratio or headroom is reported. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Cash of 3,085 and revolver availability of 894 give liquidity of 3,979 against total debt of 3,388. | Near-term maturities, including 350 due in 2027, are covered several times by cash. | High |
| Interest paid over the last twelve months was 200, so reported EBITDA covers cash interest 2.54x. | Cover is modest because interest cost rose after the 2025 note issuance. | Medium |
| Confirmed supplier finance obligations are 2.6 billion, inside accounts payable and outside reported debt. | A pullback by banks would drain working capital and is a key liquidity sensitivity. | Medium |
| Before 2030 only 350 falls due in 2027 and 271 in 2028; 1,475 falls due in 2030. | Refinancing pressure sits beyond the next two years, but the 2027 notes become current. | High |

### Financial base view

The reported financial base is complete enough for the requested use, with limits. The three FY2026 quarters and FY2025 each have a full income statement, balance sheet and cash flow, and the debt note, revolver terms, leases and supplier finance programme are disclosed. The company is a high-cash, fixed-rate unsecured issuer whose cash balance exceeds its reported debt at every balance sheet date in the pack, but whose earnings base is still recovering from restructuring: FY2025 operating income was a loss and the last twelve months to October 10, 2026 show a modest positive result. Gross leverage is high on reported EBITDA and net leverage is low only because of a very large cash balance, of which a large part sits in qualified cash accounts that carry availability conditions under the revolver. Interest cover on a cash basis is thin. Limits that matter for use: EBITDA here is operating income plus depreciation and amortisation with no add-backs, covenant ratios and headroom are not reported, per-series principal at October 10, 2026 is derived, and no pension or finance lease obligation is evidenced either way. Quarterly derived figures differ from reported totals by rounding of one unit in places.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 14.90 | 1.26 | x | Balance sheet debt (carrying value, net of discounts) over reported EBITDA of 229 (operating loss plus D&A); fifty-three weeks; debt reflects the August 2025 issuance in full while the year's EBITDA and interest paid reflect only part-year coupons on it. |
| LTM April 25, 2026 | 8.25 | 1.11 | x | Derived LTM EBITDA of 414 from FY2025 plus sixteen weeks 2026 less sixteen weeks 2025; no add-backs; includes restructuring charges. |
| LTM July 18, 2026 | 6.88 | 0.54 | x | Derived LTM EBITDA of 492 from FY2025 plus twenty-eight weeks 2026 less twenty-eight weeks 2025; no add-backs. |
| LTM October 10, 2026 | 6.67 | 0.60 | x | Derived LTM EBITDA of 508 (fifty-three weeks); debt 3,388 and cash 3,085 at October 10, 2026; no add-backs. Net debt uses all cash, of which 2.3 billion is qualified cash subject to revolver availability conditions. Management's own lease-adjusted net leverage is 2.2x on adjusted EBITDAR and is not comparable. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 3.01 | x | Reported EBITDA of 229 over interest paid of 76; the August 2025 notes paid their first coupons only in the last months of the year, so this flatters cover. |
| LTM April 25, 2026 | 3.04 | x | LTM EBITDA of 414 over derived LTM interest paid of 136. |
| LTM July 18, 2026 | 3.62 | x | LTM EBITDA of 492 over derived LTM interest paid of 136. |
| LTM October 10, 2026 | 2.54 | x | LTM EBITDA of 508 over derived LTM interest paid of 200. Interest paid is gross and is not reduced by interest income, which sits in other income, net; coupons are semi-annual so quarterly interest paid is lumpy. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 3123 | 896 | US$m | Cash at January 3, 2026; revolver borrowing availability as reported with 104 of letters of credit outstanding and no borrowings. |
| Q1 FY2026 | 2956 | 896 | US$m | Cash at April 25, 2026; availability as reported. |
| Q2 FY2026 | 3120 | 894 | US$m | Cash at July 18, 2026; availability as reported with 106 of letters of credit outstanding. |
| Q3 FY2026 | 3085 | 894 | US$m | Cash at October 10, 2026; availability as reported. Of cash, 2.3 billion is qualified cash, described as unrestricted but subject to minimum availability and excess availability conditions and springing control on default. The uncommitted 500 accordion is excluded. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0 | US$m | Contractual maturity calendar year. The 2026 notes were redeemed in 2025; the FY2025 schedule prints no 2026 maturity. |
| 2027 | 350 | US$m | 1.75% notes due October 1, 2027; principal due within twelve months of October 10, 2026 as printed (0.1 repurchased in Q2 FY2026, so about 349.9). |
| 2028 | 271 | US$m | 5.95% notes due March 9, 2028; derived as 300 printed at January 3, 2026 less 29 repurchased in Q2 FY2026. |
| 2029 | 0 | US$m | No maturity printed for 2029 in the FY2025 schedule. |
| 2030 | 1475 | US$m | 3.90% notes due April 15, 2030 (500) and 7.00% notes due August 1, 2030 (975). |
| 2031 | 0 | US$m | No instrument in the FY2025 debt table matures in 2031. |
| 2032 | 350 | US$m | 3.50% notes due March 15, 2032. |
| 2033 | 975 | US$m | 7.375% notes due August 1, 2033. Revolver maturity is not printed (five-year facility put in place on August 12, 2025) and is excluded; principal by year is derived from the FY2025 table and the repurchase narrative, not tabulated by the company at October 10, 2026. |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2025 (53 weeks) | Q1 FY2026 (16 weeks) | Q2 FY2026 (12 weeks) | Q3 FY2026 (12 weeks) | Q3 FY2025 (12 weeks) | 40 weeks 2026 | 40 weeks 2025 | LTM Oct 10, 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales | 8,601 | 2,614 | 2,000 | 2,012 | 2,036 | 6,626 | 6,628 | 8,599 |
| Gross profit | 3,733 | 1,180 | 923 | 897 | 881 | 3,001 | 2,864 | 3,870 |
| Restructuring and related expenses | 204 | 32 | 10 | 42 | 33 | 84 | 180 | 108 |
| Operating income (loss) | (43) | 69 | 101 | 47 | 22 | 218 | (87) | 262 |
| Interest expense | (139) | (65) | (48) | (46) | (40) | (160) | (86) | (213) |
| Other income, net | 91 | 31 | 22 | 23 | 16 | 76 | 61 | 106 |
| Net income (loss) | 44 | 24 | 55 | 15 | (1) | 94 | 38 | 100 |
| Depreciation and amortisation (cash flow statement) | 272 | 74 | 56 | 58 | 68 | 188 | 214 | 246 |
| EBITDA (operating income plus D&A, derived) | 229 | 143 | 157 | 105 | 90 | 406 | 127 | 508 |
| Net cash from operating activities | (46) | (19) | 271 | 59 | (12) | 311 | (118) | 383 |
| Purchases of property and equipment | (252) | (56) | (76) | (70) | (64) | (202) | (159) | (295) |
| Interest paid | 76 | 99 | 1 | 89 | 25 | 189 | 65 | 200 |
| Cash and cash equivalents (period end) | 3,123 | 2,956 | 3,120 | 3,085 | n/a | 3,085 | 3,174 | 3,085 |
| Total debt, carrying value (period end) | 3,412 | 3,414 | 3,387 | 3,388 | n/a | 3,388 | Not supplied | 3,388 |
| Total debt / EBITDA (x) | 14.90 | n/a | n/a | n/a | n/a | n/a | n/a | 6.67 |
| Net debt / EBITDA (x) | 1.26 | n/a | n/a | n/a | n/a | n/a | n/a | 0.60 |
| EBITDA / interest paid (x) | 3.01 | n/a | n/a | n/a | n/a | n/a | n/a | 2.54 |

Notes to the table. FY2025 net income is 44 including a loss of 24 from discontinued operations; continuing operations earned 68. Q2 and Q3 quarter figures for D&A, cash flow, capex and interest paid are derived by subtracting year-to-date totals in consecutive 10-Qs; income statement quarters are as printed. Q1 to Q3 FY2026 operating income sums to 217 against 218 printed for forty weeks, and interest expense sums to 159 against 160, which are rounding differences. LTM columns are derived as FY2025 plus forty weeks 2026 less forty weeks 2025. Cash at 40 weeks 2025 is the October 4, 2025 balance from the cash flow statement. The LTM net income of 100 includes the 24 discontinued loss because it is taken from total net income; management's four-quarter figure of 124 excludes it. Where a cell reads n/a the ratio or balance was not computed for that column, which is a choice and not missing data, except where Not supplied is stated.

### Source locators for the table

| Item | Locator and quote |
| --- | --- |
| FY2025 income statement | 10-K FY2025 page:66 "Operating (loss) income" and "Net sales" row; 8,601 net sales and operating loss of 43 |
| FY2025 cash flow, D&A, capex | 10-K FY2025 page:67 "Depreciation and amortization" row 272; page:68 "Purchases of property and equipment" 252 |
| FY2025 interest paid | 10-K FY2025 page:68 "Interest paid" 76 |
| Q1 income statement and cash flow | 10-Q Q1 page:4 and page:5; interest paid on page:6 |
| Q2 income statement and cash flow | 10-Q Q2 page:4, page:5 and page:6 |
| Q3 income statement and cash flow | 10-Q Q3 page:4, page:5 and page:6; interest paid on page:7 |

### Debt and capital structure

| Instrument | Principal at January 3, 2026 | Terms and status | Locator |
| --- | --- | --- | --- |
| 1.75% Senior Unsecured Notes due October 1, 2027 | 350 | Unsecured; subsidiary guarantees under the 2010 indenture; reclassified to current in Q3 FY2026 | 10-K FY2025 page:87; 10-Q Q3 page:11 |
| 5.95% Senior Unsecured Notes due March 9, 2028 | 300 | 29 repurchased in Q2 FY2026 | 10-K FY2025 page:87; 10-Q Q3 page:11 |
| 3.90% Senior Unsecured Notes due April 15, 2030 (Exchange Notes) | 500 | 2020 indenture | 10-K FY2025 page:87, page:88 |
| 7.00% Senior Unsecured Notes due August 1, 2030 | 975 | Issued August 4, 2025 under a new indenture with Computershare as trustee | 10-K FY2025 page:87, page:88 |
| 3.50% Senior Unsecured Notes due March 15, 2032 | 350 | 2010 indenture | 10-K FY2025 page:87, page:88 |
| 7.375% Senior Unsecured Notes due August 1, 2033 | 975 | Issued August 4, 2025 | 10-K FY2025 page:87, page:88 |
| ABL Facility (senior secured first lien revolver, up to 1,000 with an uncommitted 500 accordion) | 0 drawn | No borrowings at January 3, 2026 or October 10, 2026; borrower is Advance Auto Parts, Inc.; first lien on receivables, inventory, cash and related assets | 10-K FY2025 page:90, page:91; 10-Q Q3 page:12 |
| Total principal | 3,450 (3,412 net of discounts and issuance costs) | The sum of the six note series, 350 + 300 + 500 + 975 + 350 + 975, agrees to the printed total | 10-K FY2025 page:87 |

The 5.90% notes due 2026 (300) were redeemed in full in August 2025 from the proceeds of the 2030 and 2033 issuance. Every note carries a fixed rate, so interest expense risk applies only to future revolver borrowings, while interest income on cash moves with rates (10-K FY2025 page:58 puts a 100 basis point change at about 31 a year). The notes rank behind the first lien revolver on the pledged current assets, and the revolver, notes and guarantees share the same guarantor group except for certain Canadian subsidiaries that guarantee only the revolver. The FY2025 maturity schedule prints 0 for 2026, 350 for 2027, 300 for 2028, 0 for 2029, 1,475 for 2030 and 1,325 thereafter, and these sum to 3,450.

### Claims outside reported debt

| Claim | Amount and period | Inside or outside the debt figure | Locator |
| --- | --- | --- | --- |
| Operating lease liabilities | 2,247 at January 3, 2026 (435 current, 1,812 non-current); management counts 2,189 at October 10, 2026 | Outside debt; included in management's adjusted net debt | 10-K FY2025 page:93; Release Q3 page:10 |
| Supplier finance (confirmed obligations to banks) | 2.6 billion at October 10, 2026; 2.5 billion at January 3, 2026 | Outside debt; recorded in accounts payable | 10-Q Q3 page:14; 10-K FY2025 page:103 |
| Guarantee of bank loans to independent Carquest stores | 57 at October 10, 2026; 69 at January 3, 2026, collateralised by inventory valued at 142 | Outside debt; liability recorded in other current liabilities | 10-Q Q3 page:13 |
| Letters of credit under the revolver | 106 at October 10, 2026; 104 at January 3, 2026 | Reduce revolver availability; undrawn | 10-Q Q3 page:12 |
| Operating lease commitments signed but not commenced | 78 at January 3, 2026 | Outside debt and lease liabilities | 10-K FY2025 page:94 |
| Purchase commitments | No material effect expected by management | Not quantified | 10-K FY2025 page:54 |
| Litigation | No material adverse effect expected by management | Not quantified | 10-Q Q3 page:14 |
| Pension and retiree medical; finance leases | Not supplied: a search of all sources found no such disclosure | Not calculable | Gap |

### Covenants and restrictions

| Test or restriction | Level | Reported figure and headroom | Locator |
| --- | --- | --- | --- |
| Springing fixed charge coverage ratio, ABL Facility | Minimum 1:1, four quarters trailing, defined as Consolidated Adjusted EBITDA less capital expenditures less taxes over Fixed Charges | Not supplied: no ratio, no trigger level and no headroom are printed. The company states it was in compliance with the ABL covenants in all periods presented. | 10-K FY2025 page:91; 10-Q Q3 page:12 |
| Minimum availability on qualified cash | Greater of 12.5% of the Line Cap and 125 | Line Cap not printed; Not calculable | 10-Q Q3 page:12 |
| Excess availability on qualified cash | At least 400 | Reported borrowing availability is 894, an indicative gap of 494, but excess availability is a defined term that may differ from reported availability; Not calculable as defined | 10-Q Q3 page:12 |
| Notes: cross-acceleration | 25 for the 2027, 2028, Exchange and 2032 notes; 125 for the 2030 and 2033 notes | Not applicable; no default reported | 10-K FY2025 page:89 |
| Notes: liens and sale-leaseback limits; change of control put at 101% | Per indentures | Indentures not supplied | 10-K FY2025 page:88, page:89 |

The metric computed here, operating income plus D&A, differs from the covenant measure. The covenant uses Consolidated Adjusted EBITDA, subtracts capital expenditures and taxes, and divides by Fixed Charges, all as defined in the ABL agreement, which is not in the pack. Management's net leverage ratio is a third definition (adjusted EBITDAR, lease-adjusted net debt) and is reported as an attributed claim only.

### Latest quarter and events to the cutoff

| Event | Amount and date | Locator |
| --- | --- | --- |
| Reclassification of the 2027 notes to current liabilities | 349 carrying; Q3 FY2026 | 10-Q Q3 page:11 |
| Repurchases of 2027 and 2028 notes under a 10b5-1 plan, completed in Q2 FY2026; no new plan in Q3 | 0.1 and 29 of principal | 10-Q Q3 page:11 |
| Non-cash impairment of right-of-use assets on closed locations | 33; Q3 FY2026 | 10-Q Q3 page:18 |
| Vendor bankruptcy converted to Chapter 7 liquidation | September 1, 2026; the charge on vendor receivables was recorded in Q3 FY2025 | 10-Q Q3 page:11 |
| IEEPA tariff refunds recognised | 26 in Q2 FY2026; immaterial since | 10-Q Q3 page:11 |
| Final Worldpac working-capital payment | 55 in the first half of FY2026, shown in discontinued investing cash flow | 10-Q Q3 page:24 |
| Regular dividend declared | 0.25 per share declared October 26, 2026, payable January 22, 2027 (subsequent to quarter end, before cutoff) | Release Q3 page:2 |
| Updated FY2026 guidance | Net sales about 8,500; free cash flow about 150 (previously about 100); capex about 300; interest expense about 210 and interest income about 105 | Release Q3 page:2, page:3 |
| Remaining restructuring charges | 5 to 10 through the end of FY2026; cumulative 1.1 billion to date | 10-Q Q3 page:19 |

No new debt, amendment, waiver or disaster is disclosed in Q3 FY2026 or after it in the pack. The revolver does not expire within twelve months of the cutoff on the evidence available, because it is a five-year facility put in place in August 2025, although its exact maturity date is not printed. The 2027 notes are the only debt maturing within twelve months of the cutoff.

### Interpretation: evidence, mechanism and credit implication

| Topic | Evidence | Risk mechanism | Credit implication | Classification |
| --- | --- | --- | --- | --- |
| Liquidity versus debt | Cash 3,085 and revolver availability 894 at October 10, 2026 against total debt 3,388 and 349 of current debt (10-Q Q3 page:4, page:12) | Cash exceeds all debt, so near-term repayment does not depend on market access; however 2.3 billion of the cash is qualified cash that becomes restricted on a default or covenant breach | Strong near-term repayment capacity; the 2027 notes can be repaid from cash several times over | Analyst Interpretation |
| Earnings base | LTM operating income of 262 and EBITDA of 508 after restructuring charges of 108, against operating loss of 43 in FY2025 | Thin earnings convert to high gross leverage and modest interest cover; the improvement is recent and sensitive to sales that were flat | Leverage on earnings is the weak point; cover of 2.54x gives limited room for a shock, offset by cash | Analyst Interpretation |
| Interest burden | Interest expense rose to 160 over forty weeks from 86 because of the 1,950 notes issued in August 2025 (10-Q Q3 page:23); guidance implies interest expense of about 210 against interest income of about 105 | Net carry on the cash pile is positive only while cash stays invested at current rates; cash interest is paid in lumps around coupon dates | Falling rates or using cash would raise net interest cost | Analyst Interpretation |
| Supplier finance | 2.6 billion confirmed obligations versus accounts payable of 3,065 and inventories of 3,789 (10-Q Q3 page:4, page:14); utilisation depends on bank participation and credit ratings (10-K FY2025 page:49) | Accounts payable fund most of the inventory; if banks pull back or ratings fall, payment terms shorten and working capital absorbs cash; the revolver borrowing base also carries reserves for it (10-K FY2025 page:91) | The key off-balance-sheet liquidity sensitivity, comparable in size to the debt stack | Analyst Interpretation |
| Cash flow quality | Operating cash flow of 311 over forty weeks against negative 118 a year earlier, helped by lower restructuring cash charges (10-Q Q3 page:25) | Part of the swing is working capital and non-recurring restructuring outflows rolling off, not run-rate earnings | Free cash flow of 109 over forty weeks (Release Q3 page:10) is positive but small relative to debt | Documentary Fact for the figures; Analyst Interpretation for the reading |
| Maturity wall | 1,475 in 2030 and 1,325 in 2032 to 2033 | Only 350 falls due in 2027 and 271 in 2028, then a concentrated maturity in 2030 | Refinancing risk is back-ended and manageable if cash is retained | Analyst Interpretation |

## Calculations

All inputs are reported figures in US$ millions with the locators in the sections above. Results are rounded as shown. Nothing in this section is a source-printed subtotal unless stated.

### Derived LTM inputs

LTM = FY2025 + forty weeks 2026 (or 16 or 28 weeks) less the same weeks of 2025.

| Measure | Formula and inputs | Result |
| --- | --- | --- |
| LTM operating income to October 10, 2026 | -43 + 218 - (-87) | 262 |
| LTM D&A to October 10, 2026 | 272 + 188 - 214 | 246 |
| LTM EBITDA to October 10, 2026 | 262 + 246 | 508 |
| LTM interest paid to October 10, 2026 | 76 + 189 - 65 | 200 |
| LTM operating income to April 25, 2026 | -43 + 69 - (-131) | 157 |
| LTM D&A to April 25, 2026 | 272 + 74 - 89 | 257 |
| LTM EBITDA to April 25, 2026 | 157 + 257 | 414 |
| LTM interest paid to April 25, 2026 | 76 + 99 - 39 | 136 |
| LTM operating income to July 18, 2026 | -43 + 170 - (-109) | 236 |
| LTM D&A to July 18, 2026 | 272 + 130 - 146 | 256 |
| LTM EBITDA to July 18, 2026 | 236 + 256 | 492 |
| LTM interest paid to July 18, 2026 | 76 + 100 - 40 | 136 |
| FY2025 EBITDA | -43 + 272 | 229 |

The LTM D&A figures of 246, 257 and 256 agree to the D&A shown in management's four-quarter reconciliations in the releases, and LTM interest expense of 212 printed there compares with 213 derived from the statements (139 + 160 - 86), a rounding difference. The LTM periods cover fifty-three weeks because FY2025 had fifty-three weeks and the two forty-week periods cancel; they are not strictly comparable to a fifty-two week year.

### Leverage and cover

| Ratio | Inputs | Result |
| --- | --- | --- |
| Net debt, October 10, 2026 | 3,388 - 3,085 | 303 |
| Total debt / EBITDA, LTM October 10, 2026 | 3,388 / 508 | 6.67x |
| Net debt / EBITDA, LTM October 10, 2026 | 303 / 508 | 0.60x |
| EBITDA / interest paid, LTM October 10, 2026 | 508 / 200 | 2.54x |
| Total debt / EBITDA, LTM July 18, 2026 | 3,387 / 492 | 6.88x |
| Net debt / EBITDA, LTM July 18, 2026 | (3,387 - 3,120) / 492 = 267 / 492 | 0.54x |
| EBITDA / interest paid, LTM July 18, 2026 | 492 / 136 | 3.62x |
| Total debt / EBITDA, LTM April 25, 2026 | 3,414 / 414 | 8.25x |
| Net debt / EBITDA, LTM April 25, 2026 | (3,414 - 2,956) / 414 = 458 / 414 | 1.11x |
| EBITDA / interest paid, LTM April 25, 2026 | 414 / 136 | 3.04x |
| Total debt / EBITDA, FY2025 | 3,412 / 229 | 14.90x |
| Net debt / EBITDA, FY2025 | (3,412 - 3,123) / 229 = 289 / 229 | 1.26x |
| EBITDA / interest paid, FY2025 | 229 / 76 | 3.01x |

Total debt at October 10, 2026 is the sum of the current portion of 349 and long-term debt of 3,039, which equals 3,388 and agrees to management's Total Debt (GAAP) of 3,388 in Release Q3. Management's lease-adjusted metric checks as 3,388 + 2,189 - 3,085 = 2,492 of adjusted net debt, and 2,492 / 1,157 = 2.15x, which rounds to the 2.2x printed. Its adjusted EBITDAR of 1,157 sums from 124 + 246 + 212 - 106 + 31 + 524 + 37 + 89, and uses rent of 524 and other add-backs that this module does not adopt.

### Liquidity

| Measure | Inputs | Result |
| --- | --- | --- |
| Liquidity, October 10, 2026 | Cash 3,085 + availability 894 | 3,979 |
| Liquidity, July 18, 2026 | 3,120 + 894 | 4,014 |
| Liquidity, April 25, 2026 | 2,956 + 896 | 3,852 |
| Liquidity, January 3, 2026 | 3,123 + 896 | 4,019 |
| Revolver cross-check | Facility 1,000 less drawn 0 less letters of credit 106 | 894, agrees to reported availability |
| Liquidity less current debt | 3,979 - 349 | 3,630 |

### Principal roll-forward at October 10, 2026

| Item | Inputs | Result |
| --- | --- | --- |
| Principal at January 3, 2026 | 350 + 300 + 500 + 975 + 350 + 975 | 3,450 |
| Less FY2026 repurchases | 0.1 + 29 | 29.1 |
| Derived principal at October 10, 2026 | 3,450 - 29.1 | 3,420.9 |
| Check to management text | Outstanding principal described as 3.4 billion | Consistent |
| 2028 maturity after repurchase | 300 - 29 | 271 |

### Other derived ratios

| Measure | Inputs | Result |
| --- | --- | --- |
| Supplier finance as share of accounts payable | 2.6 billion / 3,065 | about 85 percent |
| Accounts payable as share of inventories | 3,065 / 3,789 | about 81 percent |
| Discrete Q2 FY2026 cash from operations | 252 - (-19) | 271 |
| Discrete Q3 FY2026 cash from operations | 311 - 252 | 59 |
| Discrete Q2 FY2026 D&A | 130 - 74 | 56 |
| Discrete Q3 FY2026 D&A | 188 - 130 | 58 |
| Discrete Q2 FY2026 capex | 132 - 56 | 76 |
| Discrete Q3 FY2026 capex | 202 - 132 | 70 |
| Discrete Q3 FY2026 interest paid | 189 - 100 | 89 |
| Discrete Q2 FY2026 interest paid | 100 - 99 | 1 |
| LTM net sales | 8,601 + 6,626 - 6,628 | 8,599 |
| LTM gross profit | 3,733 + 3,001 - 2,864 | 3,870 |
| LTM restructuring and related | 204 + 84 - 180 | 108 |
| LTM other income, net | 91 + 76 - 61 | 106 |
| LTM net income | 44 + 94 - 38 | 100 |
| LTM operating cash flow | -46 + 311 - (-118) | 383 |
| LTM capex | 252 + 202 - 159 | 295 |

## Gaps

| ID | Gap | Affected use | Action |
| --- | --- | --- | --- |
| C1 | Per-series principal at October 10, 2026 is not tabulated by the company; it is derived from the FY2025 table and repurchase narrative (carried from the upstream source-readiness gap on the debt table). | Debt table, maturity chart | Label as derived; confirm if a later filing prints the table. |
| C2 | Covenant ratio, springing trigger and headroom are Not supplied; the ABL agreement and the Line Cap definition are not in the pack. | Covenant analysis | Do not substitute management's ratio. |
| C3 | EBITDA is operating income plus cash-flow D&A without add-backs; restructuring and impairment charges are inside it, and management supplies no adjusted EBITDA without rent. | All leverage and cover ratios | Present as reported EBITDA; compare with management's adjusted EBITDAR only as an attributed claim. |
| C4 | LTM periods cover fifty-three weeks and mix a sixteen-week quarter; no seasonal normalisation is made. | LTM ratios | Note in any use. |
| C5 | Interest cover uses gross interest paid; interest income is in other income, net and is not separately split in the statements, though management's guidance gives about 105 of interest income for FY2026. | Interest cover | Do not net unless a split is supplied. |
| C6 | Revolver maturity date and pricing tier in use are Not supplied. | Maturity chart | Excluded from the maturity table. |
| C7 | Pension, retiree medical and finance lease obligations are Not supplied (searched, no disclosure found); credit ratings and guarantor list are also absent. | Claims outside debt | Not zero; carry forward as gaps. |
| C8 | The 10-Qs print cash flows only year to date, so discrete Q2 and Q3 cash flow, capex, D&A and interest paid are derived by differencing. | Quarterly cash flow columns | Label as derived. |
| C9 | Qualified cash of 2.3 billion is described as unrestricted but subject to availability conditions; the extent to which it can be used for debt repayment or distributions is not quantified. | Net debt, liquidity | Show net debt with and without this cash if the use is a downside case. |
| C10 | Text extraction flattened tables; figures were read by cell order and checked against totals where possible (for example balance sheet and debt table sums agree). | All figures | Source fidelity not independently reviewed. |

## Next module

CP-1A should use this handoff for the business and transaction context: the Worldpac sale and use of proceeds, the August 2025 refinancing (notes issued, 2026 notes redeemed, the 2021 revolving credit agreement terminated and replaced by the asset-based revolver), the restructuring programme, management's investment grade goal, and the links between supplier finance, ratings and liquidity. It should carry gaps C1 to C10 together with the source-readiness gaps recorded earlier, and should not restate this module's leverage numbers beyond the cited figures.
