# CP-1 — Financial base: DAVITA INC. (dva)

## Request

- Issuer: DAVITA INC. (issuer id `dva`, ticker DVA), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026; prior period FY2025 (context).
- Run: `dva-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Execution: host session; the host read the pinned page text and wrote this answer. No provider was called.
- Perimeter: DaVita Inc. and its consolidated subsidiaries, including partnerships in which third parties hold noncontrolling interests. Debt, EBITDA, interest and cash flow figures below are on that consolidated perimeter. The parent has no separate statements in the pack.
- Units: the filings print statements in US$ thousands; the earnings releases print supplemental tables in US$ millions. Everything below is in US$ millions. Figures taken from the statements are shown to one decimal (thousands divided by 1,000, so rounding can leave 0.1 differences in sums); figures the company prints in millions are shown as printed.
- Question: what is the reported financial base for the credit view, with debt, claims outside debt, liquidity, maturities, coverage and the covenant picture, for FY2025 and the first three quarters of 2026?
- Locators are `page:N` of the pinned `.jsonl` text of each source, not printed page numbers. Tags: [10-K] annual report, [Q1 10-Q], [Q2 10-Q], [Q3 10-Q] quarterly reports, [Q1 ER], [Q2 ER], [Q3 ER] earnings releases. Quotes are exact substrings of the cited page. Periods: FY2025, Q1 2026, Q2 2026, Q3 2026, nine months 2026 (9M 2026), nine months 2025 (9M 2025) and LTM (last twelve months) at each quarter-end.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_dva-20251231.htm.jsonl | e8c363b79225d32d92e8856c1234363883b84595e0f356cf12128301c572a94b | Audited FY2025 statements, debt, lease and segment notes, contractual obligations |
| 10-Q_2026-03-31_dva-20260331.htm.jsonl | 7063ac673c62a3a12d361c8ab9f216c83e6406eb95937f85ad2f6c47a221fe01 | Unaudited Q1 2026 statements, debt note, liquidity |
| 10-Q_2026-06-30_dva-20260630.htm.jsonl | 5aed5931f3b50f8efc4d5398264cb7a317623aeb269a49968c33246ed0273365 | Unaudited Q2 2026 and six-month statements, debt note with maturities, liquidity |
| 10-Q_2026-09-30_dva-20260930.htm.jsonl | 99b4bb0c8f87c03db2290c95cfd812d4622509e8fdbcdce46d84afcedef79236 | Unaudited Q3 2026 and nine-month statements, debt note, maturities, liquidity, segments |
| EX-99.1_2026-05-05_dva33126ex991.htm.jsonl | c5727d9383becddd69bf1cd80efadc8ee72012f8313405a8b1414b2f74143fa7 | Q1 2026 release; leverage ratio calculation (supporting, non-GAAP) |
| EX-99.1_2026-08-04_dva63026ex991.htm.jsonl | e55a9fe053fe9f69274156863d81212ffe989a931913bc64dfc65b70fd8151a2 | Q2 2026 release; leverage ratio calculation (supporting, non-GAAP) |
| EX-99.1_2026-10-29_dva93026ex991.htm.jsonl | b062a4dfa0aa9b3cce4ee385c1a8aad8546180810a3acbc585a968f93eadfc64 | Q3 2026 release; leverage ratio, guidance, segment data (supporting, non-GAAP) |
| context | 888318ae2603a71d9f443112e6d0298861b2ea95d8c8a8118da68f80c88bfe70 | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 3ecf1492bb810c2e90133183ed7699bad1c56c1780a9f8736f0e2c4391db50f2 | Source readiness: all selected consumers ready with limitations; carries the missing credit agreement and indentures, the missing guarantor list, the unit mix and the issuer-computed leverage ratio |

Consistency with CP-0: this answer confirms CP-0 on the points it checked (the covenant summary is only in the 10-K, the 10-Qs carry no leverage text, the Q1 10-Q debt note has no maturity schedule, the unit mix). It adds one fact CP-0 left open: the Berkshire repurchase obligation described in the Q3 10-Q was settled on October 27, 2026 (see Events). No correction to CP-0 is needed.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Covenant-basis net leverage is 3.38x, up from 3.26x at FY2025, against a 5.00x maximum. Earnings are growing, but buybacks and a heavy 2030 and 2031 maturity wall absorb cash flow. | Medium | The EBITDA is company-computed and cannot be checked to the credit agreement; cash interest is printed only for FY2025. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt rose to 10,832.2 at Q3 2026 from 10,344.6 at FY2025, while cash fell to 495.6 from 676.4. | Net leverage drifted up and the cash buffer shrank. | High |
| Revenue of 10,547.8 and operating income of 1,560.1 for 9M 2026 were each about 5.2% above 9M 2025. | Earnings growth is the main support for deleveraging capacity. | High |
| Share repurchases of 870.2 in 9M 2026 nearly matched operating cash flow less capital expenditure of 898.4, and net debt issuance was 490. | Free cash flow is going to buybacks rather than debt paydown. | Medium |
| Debt maturing in 2030 is 4,570.3 and in 2031 is 3,765.1, about 77% of the total. | Refinancing risk concentrates in 2030 and 2031. | High |
| Reported leverage of 3.38x compares with a 5.00x maximum, leaving 1.62x of headroom on company figures. | The cushion looks wide but rests on definitions that are not supplied. | Low |

### Financial base view

The reported base shows a large, steady-earning dialysis business that has been adding debt while it returns cash to shareholders. At September 30, 2026 total debt principal is 10,832.2 (including 151.6 of finance leases and before 63.1 of unamortised discount and financing costs); cash and cash equivalents are 495.6, so net debt on the company's own definition is 10,337. Against the company's credit-agreement EBITDA of 3,042 (last twelve months, issuer non-GAAP), total debt is 3.56x and the covenant-basis net leverage is 3.38x, up from 3.26x at December 31, 2025. The statements themselves print no EBITDA: operating income plus depreciation and amortization plus the Q3 2026 impairment is 2,880.9 for the last twelve months, which gives 3.76x on total debt, a stricter reading that is shown as a sensitivity. Operating lease liabilities of 2,623.3 and noncontrolling interests subject to put provisions of 1,484.3 sit outside the debt figure. The business grew in 9M 2026 (revenue and operating income each about 5.2% above 9M 2025), but operating cash flow was 1.2% lower, free cash flow on the company definition was 672 against 716, and 870.2 went to share repurchases. Liquidity is cash of 495.6 plus 1,420.0 of undrawn revolver, down from 2,176.4 at FY2025. About 77% of debt matures in 2030 and 2031. The only financial maintenance test summarised in the filings is a maximum leverage ratio of 5.00:1.00; the company reports 3.38x, but the agreement and the definition of Consolidated EBITDA are not supplied, so headroom is a company-basis figure.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 3.49 | 3.26 | x | Total debt principal 10,344.6 (incl. 185.1 finance leases, before discount) and company Consolidated EBITDA 2,960 at December 31, 2025. Net debt is the company Consolidated net debt 9,648 (funded debt less unrestricted cash and short-term investments), which gives the reported leverage ratio of 3.26x. Consolidated EBITDA is an issuer non-GAAP measure under the credit agreement. |
| LTM Q1 2026 | 3.56 | 3.34 | x | Total debt 10,694.3 and Consolidated EBITDA 3,008 at March 31, 2026; Consolidated net debt 10,031. Same basis and limits. |
| LTM Q2 2026 | 3.59 | 3.37 | x | Total debt 10,847.5 and Consolidated EBITDA 3,018 at June 30, 2026; Consolidated net debt 10,162. Same basis and limits. |
| LTM Q3 2026 | 3.56 | 3.38 | x | Total debt 10,832.2 and Consolidated EBITDA 3,042 at September 30, 2026; Consolidated net debt 10,269. Excludes operating lease liabilities of 2,623.3 and puttable noncontrolling interests of 1,484.3. On operating income plus D&A plus impairment (2,880.9) total debt is 3.76x. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 5.74 | x | Consolidated EBITDA 2,960 over cash paid for interest, net of 515.5 ([10-K] page:213). Company non-GAAP EBITDA. On debt expense of 579.9 instead, cover is 5.10x. |
| LTM Q1 2026 | Not supplied: interim cash interest paid is not printed | x | No cash-flow supplemental disclosure in the 10-Qs or releases. On LTM debt expense of 590.0 (calculated) cover is 5.10x; this is an expense basis, not cash. |
| LTM Q2 2026 | Not supplied: interim cash interest paid is not printed | x | As above. On LTM debt expense of 594.2 (calculated) cover is 5.08x; expense basis. |
| LTM Q3 2026 | Not supplied: interim cash interest paid is not printed | x | As above. On LTM debt expense of 593.7 (calculated) cover is 5.12x; expense basis. Operating income over LTM debt expense is 3.57x. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 676.4 | 1500.0 | US$m | Cash and cash equivalents excluding restricted cash of 81.3 and short-term investments of 24.3. Revolver of 1,500.0 undrawn; no letters of credit reduce it. Separate bilateral secured letter of credit facility has about 195 of letters of credit outstanding (capacity not stated). |
| Q1 2026 | 644.2 | 1125.0 | US$m | Excludes restricted cash of 82.2 and short-term investments of 22.3. Revolver 375.0 drawn. Separate bilateral facility letters of credit about 207. |
| Q2 2026 | 669.0 | 1435.0 | US$m | Excludes restricted cash of 82.9 and short-term investments of 19.9. Revolver 65.0 drawn. Separate bilateral facility letters of credit about 188. |
| Q3 2026 | 495.6 | 1420.0 | US$m | Excludes restricted cash of 83.6 and short-term investments of 70.7. Revolver 80.0 drawn; revolver matures November 24, 2030 (earlier, March 2, 2030, if the 4.625% senior notes remain outstanding 91 days before their maturity). Separate bilateral facility letters of credit about 185 (184.8 in the note). |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q4 2026 | 31.4 | US$m | Remainder of 2026 scheduled principal at September 30, 2026 ([Q3 10-Q] page:12); principal outstanding including financing lease obligations. |
| FY2027 | 113.0 | US$m | Scheduled principal ([Q3 10-Q] page:12); no tranche in the debt table has a 2027 final maturity. |
| FY2028 | 160.4 | US$m | Scheduled amortisation of Term Loan A-2 and Term Loan B-2 and other debt; no final maturity in 2028. |
| FY2029 | 146.9 | US$m | Scheduled amortisation and other debt; no final maturity in 2029. |
| FY2030 | 4570.3 | US$m | Includes the 4.625% Senior Notes (2,750.0, due June 1, 2030) and Term Loan A-2 and revolver balances (due November 24, 2030, but March 2, 2030 if the 4.625% notes remain outstanding 91 days before maturity). |
| FY2031 | 3765.1 | US$m | Includes the 3.75% Senior Notes (1,500.0, due February 15, 2031) and the Term Loan B-2 balance due May 9, 2031. |
| Thereafter | 2045.1 | US$m | 2032 onward: 6.875% Senior Notes (1,000.0, 2032), 6.75% Senior Notes (1,000.0, 2033) and later instalments. The seven rows total 10,832.2, equal to total principal. |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | 9M 2026 | 9M 2025 | LTM Q3 2026 | Basis and locators |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenues | 13,643.1 | 3,415.5 | 3,554.1 | 3,578.1 | 10,547.8 | 10,023.3 | 14,167.5 | Reported ([10-K] page:153; [Q1 10-Q] page:2; [Q2 10-Q] page:2; [Q3 10-Q] page:2). LTM calculated. |
| Operating income | 2,043.6 | 481.9 | 579.0 | 499.3 | 1,560.1 | 1,482.5 | 2,121.2 | Reported; Q3 2026 after 62.2 of goodwill and other asset impairment. LTM calculated. |
| Operating margin (%) | 15.0 | 14.1 | 16.3 | 14.0 | 14.8 | 14.8 | 15.0 | Calculated from the two rows above. |
| Adjusted operating income (company non-GAAP) | 2,094 | 482 | 579 | 561 | 1,622 | 1,508 | 2,208 | Reported in millions ([10-K] page:133; [Q1 ER] page:1; [Q3 ER] page:1). LTM calculated. |
| Depreciation and amortization | 715.3 | 177.8 | 167.8 | 165.2 | 510.8 | 528.6 | 697.5 | Reported. LTM calculated. |
| Debt expense | 579.9 | 145.1 | 150.3 | 150.0 | 445.4 | 431.7 | 593.7 | Reported income statement line; includes amortisation of discount, financing costs and caps. LTM calculated. |
| Net income from continuing operations attributable to DaVita Inc. | 721.8 | 197.5 | 265.4 | 222.9 | 685.9 | 512.6 | 895.1 | Reported ([10-K] page:154 gives 721.8; FY2025 net income attributable of 746.8 includes 25.0 from discontinued operations). LTM calculated. |
| Net income attributable to noncontrolling interests | 331.9 | 77.5 | 77.8 | 46.5 | 201.8 | 235.1 | 298.6 | Reported; deducted from consolidated net income, not from operating income or Consolidated EBITDA. |
| Net cash provided by operating activities | 1,886.5 | 320.8 | 490.1 | 518.8 | 1,329.7 | 1,345.8 | 1,870.5 | Reported for FY2025, Q1 2026 and 9M columns ([10-K] page:155; [Q1 10-Q] page:4; [Q3 10-Q] page:4); Q2 2026 and Q3 2026 derived from year-to-date reports ([Q2 10-Q] page:4). LTM calculated. |
| Additions of property and equipment | 575.9 | 102.0 | 169.8 | 159.5 | 431.3 | 430.4 | 576.8 | Reported cash-flow line; Q2 and Q3 derived. LTM calculated. |
| Operating cash flow less additions of property and equipment | 1,310.6 | 218.8 | 320.3 | 359.3 | 898.4 | 915.3 | 1,293.7 | Calculated; not a company-defined measure. |
| Free cash flow (company non-GAAP) | 1,024 | 140 | 256 | 276 | 672 | 716 | 980 | Reported in millions ([10-K] page:135; [Q1 ER] page:13; [Q2 ER] page:13; [Q3 ER] page:13 and [Q3 10-Q] page:44). After distributions to noncontrolling interests, net of contributions. LTM as reported and recomputed. |
| Cash paid for share repurchases | 1,793.0 | 396.3 | 364.3 | 109.5 | 870.2 | 1,464.2 | 1,199.0 | Sum of purchases of treasury stock from related party and other purchases of treasury stock (cash-flow statements); Q2 and Q3 derived. LTM calculated. |
| Distributions to noncontrolling interests | 324.3 | 85.4 | 64.5 | 93.9 | 243.8 | 232.7 | 335.3 | Cash-flow statements; Q2 and Q3 derived. LTM calculated. |
| Cash paid for interest, net | 515.5 | Not supplied | Not supplied | Not supplied | Not supplied | Not supplied | Not supplied | Supplemental cash flow note, FY2025 only ([10-K] page:213). |
| Cash and cash equivalents | 676.4 | 644.2 | 669.0 | 495.6 | n/a (instant) | n/a (instant) | n/a (instant) | Balance sheets ([10-K] page:154; [Q1 10-Q] page:2; [Q2 10-Q] page:3; [Q3 10-Q] page:3). Excludes restricted cash and short-term investments. |
| Total debt principal (incl. finance leases) | 10,344.6 | 10,694.3 | 10,847.5 | 10,832.2 | n/a (instant) | n/a (instant) | n/a (instant) | Debt notes ([10-K] page:179; [Q1 10-Q] page:9; [Q2 10-Q] page:10; [Q3 10-Q] page:11). Before discount, premium and financing costs. |
| Total debt carrying value | 10,273.2 | 10,626.3 | 10,781.0 | 10,769.1 | n/a (instant) | n/a (instant) | n/a (instant) | Same notes; current plus long-term portions on the balance sheet. |
| Net debt (company: total debt less cash and cash equivalents) | 9,668 | 10,050 | 10,179 | 10,337 | n/a (instant) | n/a (instant) | n/a (instant) | Reported in millions ([Q1 ER] page:13; [Q2 ER] page:13; [Q3 ER] page:13). |
| Consolidated net debt (covenant basis) | 9,648 | 10,031 | 10,162 | 10,269 | n/a (instant) | n/a (instant) | n/a (instant) | Reported ([Q1 ER] page:16; [Q2 ER] page:15; [Q3 ER] page:15); deducts cash and short-term investments, excluding non-qualified deferred compensation amounts. |
| Consolidated EBITDA, LTM (company non-GAAP) | 2,960 | 3,008 | 3,018 | 3,042 | n/a (LTM) | n/a (LTM) | 3,042 | Reported credit-agreement construction ([Q1 ER] page:15; [Q2 ER] page:15; [Q3 ER] page:15). |
| Operating lease liabilities (current plus long-term) | 2,601.1 | 2,594.6 | 2,625.5 | 2,623.3 | n/a (instant) | n/a (instant) | n/a (instant) | Balance sheets; outside the debt figure. |
| Noncontrolling interests subject to put provisions | 1,532.2 | 1,524.5 | 1,561.4 | 1,484.3 | n/a (instant) | n/a (instant) | n/a (instant) | Balance sheets; temporary equity, outside debt. |
| Total equity (deficit) | (373.7) | (476.3) | (482.0) | (358.5) | n/a (instant) | n/a (instant) | n/a (instant) | Balance sheets; includes noncontrolling interests not subject to put provisions. |
| Total debt / Consolidated EBITDA (x) | 3.49 | 3.56 | 3.59 | 3.56 | n/a (ratio) | n/a (ratio) | 3.56 | Calculated. |
| Net debt (cash only) / Consolidated EBITDA (x) | 3.27 | 3.34 | 3.37 | 3.40 | n/a (ratio) | n/a (ratio) | 3.40 | Calculated on the company net debt row. |
| Reported leverage ratio (x) | 3.26 | 3.34 | 3.37 | 3.38 | n/a (ratio) | n/a (ratio) | 3.38 | As reported; recomputed from Consolidated net debt. Maximum 5.00x. |
| Total debt / (operating income + D&A + impairment, LTM) (x) | 3.75 | 3.81 | 3.82 | 3.76 | n/a (ratio) | n/a (ratio) | 3.76 | Calculated sensitivity; no add-backs; includes noncontrolling interests' share of earnings. |
| Operating income / LTM debt expense (x) | 3.52 | 3.54 | 3.58 | 3.57 | n/a (ratio) | n/a (ratio) | 3.57 | Calculated on LTM operating income and LTM debt expense at each quarter-end; expense basis, not cash interest. |
| (Operating cash flow less additions) / total debt (%) | 12.7 | 14.0 | 14.8 | 11.9 | n/a (ratio) | n/a (ratio) | 11.9 | Calculated on LTM flows at each quarter-end; FY2025 on 1,310.6. |

### Segment results

| Segment (US$m) | FY2025 | Q3 2026 | Q3 2025 | 9M 2026 | 9M 2025 | Basis and locators |
| --- | --- | --- | --- | --- | --- | --- |
| U.S. dialysis total revenues | 11,792.9 | 3,050.5 | 2,980.0 | 9,004.0 | 8,716.6 | Includes intersegment revenue ([10-K] page:212; [Q3 10-Q] page:23). |
| Other - Ancillary services total revenues | 1,922.3 | 551.8 | 454.9 | 1,606.1 | 1,355.4 | Integrated kidney care, other U.S. ancillary and international. |
| Elimination of intersegment revenues | (72.2) | (24.1) | (14.7) | (62.3) | (48.7) | |
| Consolidated revenues | 13,643.1 | 3,578.1 | 3,420.2 | 10,547.8 | 10,023.3 | Ties to the income statement. |
| U.S. dialysis segment operating margin | 2,084.2 | 544.2 | 530.1 | 1,588.1 | 1,528.7 | Segment margin after patient care costs, G&A and D&A. |
| Other - Ancillary services segment operating margin | 92.4 | (18.6) | 1.2 | 44.2 | 55.1 | Q3 2026 includes the China impairment. |
| Corporate administrative support | (133.0) | (26.3) | (25.6) | (72.2) | (101.3) | |
| Consolidated operating income | 2,043.6 | 499.3 | 505.8 | 1,560.1 | 1,482.5 | Ties to the income statement ([10-K] page:212; [Q3 10-Q] page:24). |

Operating metrics ([Q3 ER] page:1 to page:3, page:13): U.S. dialysis treatments were 7,329,644 in Q3 2026; revenue per treatment was 415.25 in Q3 2026 and 416.22 for 9M 2026 against 405.15 for 9M 2025; patient care costs per treatment were 279.24 against 271.23. Normalized non-acquired treatment growth in the third quarter of 2026 compared to the third quarter of 2025 was 0.4%. As of September 30, 2026 the company served approximately 298,100 patients at 3,269 outpatient dialysis centers, and had approximately 80,800 patients in risk-based integrated care arrangements.

### Debt by instrument

| Instrument | Security and ranking | Final maturity | Rate | Principal, Q3 2026 | Principal, FY2025 |
| --- | --- | --- | --- | --- | --- |
| Term Loan A-2 | Senior secured, guaranteed by domestic subsidiaries | November 24, 2030 (March 2, 2030 if 4.625% notes remain) | SOFR + 1.50% | 1,962.5 | 2,000.0 |
| Term Loan B-2 | Senior secured, same package | May 9, 2031 | SOFR + 1.75% | 2,352.0 | 1,868.6 |
| Revolving line of credit (1,500.0 commitment) | Senior secured, same package | November 24, 2030 (March 2, 2030 if 4.625% notes remain) | SOFR + 1.50% | 80.0 | 0.0 |
| 4.625% Senior Notes | Senior unsecured | June 1, 2030 | 4.625% | 2,750.0 | 2,750.0 |
| 3.75% Senior Notes | Senior unsecured | February 15, 2031 | 3.75% | 1,500.0 | 1,500.0 |
| 6.875% Senior Notes | Senior unsecured | September 1, 2032 | 6.875% | 1,000.0 | 1,000.0 |
| 6.75% Senior Notes | Senior unsecured, guaranteed by the domestic subsidiaries that guarantee the credit facilities | July 15, 2033 | 6.75% | 1,000.0 | 1,000.0 |
| Acquisition obligations and other notes payable | Not stated | 2026 to 2038 | 5.16% (weighted average) | 36.2 | 40.9 |
| Financing lease obligations | Lease obligations | 2027 to 2039 | 4.26% (weighted average) | 151.6 | 185.1 |
| Total debt principal outstanding | | | | 10,832.2 | 10,344.6 |
| Discount, premium and deferred financing costs | | | | (63.1) | (71.4) |
| Carrying value (current portion 112.5 and 10,656.6 long-term) | | | | 10,769.1 | 10,273.2 |

Locators: [Q3 10-Q] page:11 (table) and page:14 (revolver, weighted average rate); [10-K] page:179 (FY2025 column), page:181 to page:184 (facility terms, security, amortisation, notes). The blank cells in the total rows are not data. Weighted average effective interest rate on all debt including caps was 5.54% at September 30, 2026 against 5.51% at December 31, 2025 ([Q3 10-Q] page:14; [10-K] page:187). Term Loan A-2 amortises 12.5 per quarter through December 31, 2027 and 25.0 per quarter from March 31, 2028 ([10-K] page:181). Term Loan B-2 amortises 0.25% of the principal outstanding on the amendment date each quarter ([Q3 10-Q] page:12). The senior notes are described as unsecured obligations that rank equally ([10-K] page:184); the guarantor text is explicit only for the 6.75% Senior Notes.

Interest rate exposure ([Q3 10-Q] page:12 to page:13): cap agreements cover total notional of 3,500.0 through December 31, 2026, 2027 and 2028, 3,000.0 through 2029 and 500.0 through 2030, at weighted average strike rates of 4.32%, 4.46%, 4.43%, 4.75% and 5.25% respectively. The filing states that 894.5 of floating debt (814.5 of Term Loan A-2 and 80.0 of the revolver) is subject to SOFR-based interest rate volatility.

### Leases and other claims outside debt

- Operating leases: current and long-term operating lease liabilities total 2,623.3 at September 30, 2026 ([Q3 10-Q] page:3) and 2,601.1 at December 31, 2025, with undiscounted future minimum payments of 3,001.1 ([10-K] page:188). They are outside total debt principal. The Consolidated EBITDA reconciliation shows no add-back of lease cost, so the EBITDA figures above are after operating lease cost (fixed lease expense 570.3 and variable 131.9 in FY2025, [10-K] page:187 to page:188), and adding the liabilities to debt without adding rent back would mix bases; lease-adjusted leverage is therefore not calculated (Q3 2026 LTM operating lease cost is not printed in the 10-Qs).
- Finance leases: 151.6 at September 30, 2026, already inside total debt ([Q3 10-Q] page:11).
- Puttable noncontrolling interests: 1,484.3 on the balance sheet at September 30, 2026 ([Q3 10-Q] page:3). The 10-K contractual obligations table puts 1,408 of the 1,532 recorded at December 31, 2025 in its 2026 column, plus 66 of off-balance-sheet put provisions ([10-K] page:135). Distributions to noncontrolling interests were 243.8 in 9M 2026 and 324.3 in FY2025.
- Berkshire repurchase obligation: 54.7 recorded as due to related party at September 30, 2026; settled on October 27, 2026 for 69.0 ([Q3 10-Q] page:19).
- Letters of credit: about 184.8 outstanding under a separate bilateral secured letter of credit facility at September 30, 2026 ([Q3 10-Q] page:14); these do not reduce the revolver.
- Purchase and other commitments: remaining minimum commitments under supplier purchase agreements of about 961.1, 956.2, 752.6, 577.3 and 445.9 for 2026 to 2030 at December 31, 2025, with working capital funding commitments of about 8.2 and potential investments of 13.0 ([10-K] page:195). The Elara Caring minority investment of 200.0 closed effective July 20, 2026 ([Q3 10-Q] page:10).
- Pensions and retiree medical: no pension or retiree medical liability is shown on the balance sheet. The only defined benefit reference is an immaterial other comprehensive income line ((46) thousand in FY2025, [10-K] page:154); no obligation is quantified.
- Factoring and supply-chain finance: none found. The sources were searched for "supply chain" and "factoring".
- Litigation and incidents: recorded accruals for legal proceedings and regulatory matters were immaterial at September 30, 2026 and December 31, 2025 ([Q3 10-Q] page:14). FY2025 adjusted operating income excludes 25 of cybersecurity incident-related charges and a 25 accrual for potential third-party judgment costs ([10-K] page:133). Open matters include a False Claims Act action (U.S. ex rel. Bayne), a California Department of Insurance investigation, a District of Columbia antitrust CID, Federal Trade Commission CIDs and a putative employee antitrust class action ([Q3 10-Q] page:15 to page:17). No amount is estimated.

### Covenants and compliance

| Facility group | Test | Level | Reported figure | Headroom |
| --- | --- | --- | --- | --- |
| Credit Agreement (senior secured credit facilities) | Maximum leverage ratio, tested quarterly | 5.00:1.00 through December 31, 2028; 4.50:1.00 thereafter, rising to 5.00:1.00 for four quarters after a material acquisition | 3.38x at September 30, 2026 (company, [Q3 ER] page:15 to page:16) | 1.62x on company figures; at constant Consolidated net debt of 10,269, Consolidated EBITDA could fall to 2,053.8 (a cushion of 988.2 or 32.5%) before reaching 5.00x. Not verified to the agreement |
| Credit Agreement | Threshold below which many restrictions on investments, share repurchases, dividends and other indebtedness do not apply | 4.00:1.00 | 3.38x | 0.62x below the threshold; not verified to the agreement |
| Credit Agreement | Interest margin grid on Term Loan A-2 and revolver | 0.00% to 1.75% based on a leverage ratio grid; the debt table shows SOFR + 1.50% | 3.38x | Not applicable |
| Senior Notes | Restrictive covenants on liens, sale/leaseback and mergers | Not a financial maintenance test ([10-K] page:184) | Not applicable | Not applicable |

Locators: [10-K] page:183; [Q3 ER] page:15 to page:16. No statement that the company was in compliance with its covenants was found in the sources (searched for compliance wording in the 10-K, the Q3 10-Q and the Q3 ER); the only compliance evidence is the reported ratio against the printed maximum. The ratios computed in this answer on total debt and on net debt differ from the covenant ratio: the covenant uses funded debt less unrestricted cash and short-term investments over Consolidated EBITDA, whose pro forma adjustments, expected cost savings and "Other" add-backs (84 in the last twelve months at Q3 2026) are set by the agreement. The Q1 release notes that the prior facilities limited the cash deduction to 750 ([Q1 ER] page:15); the amended definition as printed has no such limit. A reader must not equate the 3.56x or 3.76x above with the covenant ratio.

### Events, comparability and subsequent events

- Debt amendments: the Eighth Amendment of November 24, 2025 refinanced the revolver and Term Loan A-1 into a new revolver and Term Loan A-2 ([10-K] page:181). The Ninth Amendment of June 8, 2026 added an incremental 500.0 to Term Loan B-2, with proceeds used to repay part of the revolver, and cost 2.0 of debt extinguishment and modification costs in Q2 2026 ([Q3 10-Q] page:12). Revolver draws were 375.0 at March 31, 2026, 65.0 at June 30, 2026 and 80.0 at September 30, 2026.
- Impairment: Q3 2026 included a 62.2 goodwill and other asset impairment for the China reporting unit, with goodwill of 42.9 remaining and carrying amount coverage shown as nil ([Q3 10-Q] page:10 to page:11; [Q3 ER] page:2). It reduced operating income but is added back in Consolidated EBITDA and adjusted operating income.
- Acquisitions and investments: the 200.0 Elara Caring minority investment closed July 20, 2026 and is equity method ([Q3 10-Q] page:10); cash paid for acquisitions was 41.7 in 9M 2026 against 118.3 in 9M 2025.
- Capital returns: 9M 2026 repurchases were 5.8 million shares for 870.2 of cash; the company repurchased a further 0.5 million shares for 87 between October 1 and October 27, 2026, and had approximately 1,212 available under current authorizations ([Q3 ER] page:2; [Q3 10-Q] page:19). These are subsequent events relative to September 30, 2026.
- Guidance (issuer, [Q3 ER] page:3): adjusted operating income 2,175 to 2,250 (prior 2,150 to 2,250), adjusted diluted EPS 14.30 to 15.20 (prior 14.10 to 15.20) and free cash flow 1,000 to 1,250 (unchanged). Guidance is management's forward-looking statement, not evidence of results.
- Comparability: the FY2025 income statement includes 25.0 of income from discontinued operations in net income; this answer uses continuing operations for earnings rows. FY2025 included the 2025 cybersecurity incident charges. Cash paid for interest is available for FY2025 only.
- Events after September 30, 2026 up to the cutoff: share repurchases and the Berkshire settlement above, both stated as of October 27, 2026. Nothing is supplied after October 29, 2026.

### Interpretation: data to risk to credit implication

- Leverage: the company's covenant-basis leverage rose from 3.26x at FY2025 to 3.38x at Q3 2026 while Consolidated EBITDA rose from 2,960 to 3,042; net debt grew faster than EBITDA because total debt principal rose 487.7 while cash fell 180.8. Credit implication: leverage is moving toward the top of the 3.0x to 3.5x range the 10-K says it held throughout 2025 ([10-K] page:114; the sources print no 2026 target), and it remains 1.62x inside the maximum on company figures.
- Earnings: 9M 2026 revenue and operating income were each about 5.2% higher than 9M 2025, and adjusted operating income was about 7.6% higher (1,622 against 1,508). Q3 2026 operating income of 499.3 was below Q3 2025's 505.8 because of the 62.2 impairment; adjusted operating income was 561 against 579 in Q2 2026. The release attributes year-to-date cost growth to compensation, medical supplies, insurance and health benefits ([Q3 ER] page:2). Credit implication: the earnings base is growing but cost pressure is visible per treatment (patient care costs per treatment 279.24 against 271.23).
- Cash conversion and capital allocation: operating cash flow for 9M 2026 was 1,329.7 against 1,345.8, and company free cash flow was 672 against 716. Cash share repurchases of 870.2 equalled about 97% of operating cash flow less additions of 898.4 and were accompanied by net debt issuance of 490 ([Q3 10-Q] page:44). Credit implication: free cash flow is directed to equity holders and the balance sheet absorbs the difference, so deleveraging depends on a change in policy. The 2026 guidance of 1,000 to 1,250 of free cash flow implies 328 to 578 for Q4 2026 (calculated).
- Noncontrolling interests: the company consolidates partnerships; noncontrolling interests earned 201.8 in 9M 2026 and received distributions of 243.8, and Consolidated EBITDA adds this income back. Credit implication: part of consolidated EBITDA is cash that leaves to minority partners, so debt-to-EBITDA may understate leverage on the parent's attributable cash flow; this is not quantified here.
- Liquidity and maturities: cash plus undrawn revolver was 1,915.6 at September 30, 2026 against 2,176.4 at December 31, 2025 (calculated); the revolver is nearly undrawn. Maturities before 2030 are small (31.4, 113.0, 160.4 and 146.9 in Q4 2026 to 2029), then 4,570.3 in 2030 and 3,765.1 in 2031. The Term Loan A-2 and revolver (2,042.5 drawn) fall due March 2, 2030 if the 4.625% notes are not refinanced by then. Credit implication: refinancing risk is back-ended but large and clustered, and the springing date pulls secured bank maturities forward.
- Rate risk: 894.5 of floating debt is unhedged by the printed caps, whose strikes step up to 4.75% and 5.25% in later years. Credit implication: a SOFR rise has a bounded effect today but the protection is thinner after 2028.
- Quality of the evidence: FY2025 statements are audited, with an unqualified opinion dated February 11, 2026 ([10-K] page:148). The quarterly statements are unaudited. Consolidated EBITDA, adjusted operating income, free cash flow and net debt are management non-GAAP presentations. The statements print no cash interest for interim periods.

## Calculations

All inputs are US$ thousands from the cited statements, shown in millions; sums use the unrounded thousands, so a sum of rounded components can differ by 0.1. "LTM" is FY2025 plus the 2026 year-to-date amount minus the 2025 year-to-date amount of the same length.

### LTM and discrete-quarter amounts

- LTM Q3 2026 revenue: 13,643.1 + 10,547.8 - 10,023.3 = 14,167.5. Operating income: 2,043.6 + 1,560.1 - 1,482.5 = 2,121.2. D&A: 715.3 + 510.8 - 528.6 = 697.5. Debt expense: 579.9 + 445.4 - 431.7 = 593.7. Net income from continuing operations attributable to DaVita Inc.: 721.8 + 685.9 - 512.6 = 895.1. Noncontrolling interests: 331.9 + 201.8 - 235.1 = 298.6.
- Quarters tie to nine months: revenue 3,415.5 + 3,554.1 + 3,578.1 = 10,547.8; operating income 481.9 + 579.0 + 499.3 = 1,560.1; D&A 177.8 + 167.8 + 165.2 = 510.8; debt expense 145.1 + 150.3 + 150.0 = 445.4; net income attributable 197.5 + 265.4 + 222.9 = 685.9.
- Operating cash flow: Q2 2026 = six months 810.9 - Q1 320.8 = 490.1; Q3 2026 = nine months 1,329.7 - six months 810.9 = 518.8; LTM = 1,886.5 + 1,329.7 - 1,345.8 = 1,870.5, which agrees with the 1,870 the Q3 release prints ([Q3 ER] page:2).
- Additions of property and equipment: Q2 = 271.8 - 102.0 = 169.8; Q3 = 431.3 - 271.8 = 159.5; LTM = 575.9 + 431.3 - 430.4 = 576.8.
- Operating cash flow less additions: FY2025 1,886.5 - 575.9 = 1,310.6; Q1 320.8 - 102.0 = 218.8; Q2 490.1 - 169.8 = 320.3; Q3 518.8 - 159.5 = 359.3; 9M 2026 1,329.7 - 431.3 = 898.4; 9M 2025 1,345.8 - 430.4 = 915.3; LTM 1,870.5 - 576.8 = 1,293.7.
- Share repurchase cash: FY2025 484.6 + 1,308.4 = 1,793.0; Q1 199.9 + 196.4 = 396.3; six months 382.8 + 377.9 = 760.7, so Q2 = 760.7 - 396.3 = 364.3 (rounded from unrounded 364.346); nine months 419.3 + 450.9 = 870.2, so Q3 = 870.2 - 760.7 = 109.5; 9M 2025 430.3 + 1,033.9 = 1,464.2; LTM = 1,793.0 + 870.2 - 1,464.2 = 1,199.0.
- Distributions to noncontrolling interests: Q2 = 149.9 - 85.4 = 64.5; Q3 = 243.8 - 149.9 = 93.9; LTM = 324.3 + 243.8 - 232.7 = 335.3.
- Adjusted operating income (millions): LTM = 2,094 + 1,622 - 1,508 = 2,208; quarters 482 + 579 + 561 = 1,622. Free cash flow: LTM = 1,024 + 672 - 716 = 980 (agrees with the 980 printed in [Q3 ER] page:2); quarters 140 + 256 + 276 = 672.

### Leverage and coverage

- Total debt / Consolidated EBITDA: FY2025 10,344.6 / 2,960 = 3.49; Q1 10,694.3 / 3,008 = 3.56; Q2 10,847.5 / 3,018 = 3.59; Q3 10,832.2 / 3,042 = 3.56.
- Net debt (cash only) / Consolidated EBITDA: company net debt equals total debt less cash and cash equivalents: FY2025 10,344.6 - 676.4 = 9,668.1; Q3 10,832.2 - 495.6 = 10,336.6 (company prints 10,337). Ratios: 9,668 / 2,960 = 3.27; 10,050 / 3,008 = 3.34; 10,179 / 3,018 = 3.37; 10,337 / 3,042 = 3.40.
- Covenant-basis net leverage recomputed: 9,648 / 2,960 = 3.26; 10,031 / 3,008 = 3.34; 10,162 / 3,018 = 3.37; 10,269 / 3,042 = 3.38. All agree with the printed ratios.
- Sensitivity EBITDA (operating income + D&A + impairment, LTM): FY2025 2,043.6 + 715.3 = 2,759.0; LTM Q1 2,086.6 + 716.7 = 2,803.3; LTM Q2 2,127.7 + 709.8 = 2,837.6; LTM Q3 2,121.2 + 697.5 + 62.2 = 2,880.9. Total debt over it: 10,344.6 / 2,759.0 = 3.75; 10,694.3 / 2,803.3 = 3.81; 10,847.5 / 2,837.6 = 3.82; 10,832.2 / 2,880.9 = 3.76. LTM Q1 operating income is 2,043.6 + 481.9 - 438.9 = 2,086.6 and D&A is 715.3 + 177.8 - 176.5 = 716.7; LTM Q2 operating income is 2,043.6 + 1,060.9 - 976.8 = 2,127.7 and D&A is 715.3 + 345.6 - 351.2 = 709.8 (inputs from [Q1 10-Q] page:2 and [Q2 10-Q] page:2).
- Cover: FY2025 2,960 / 515.5 = 5.74; expense basis: 2,960 / 579.9 = 5.10; LTM Q1 debt expense 579.9 + 145.1 - 135.1 = 590.0, 3,008 / 590.0 = 5.10; LTM Q2 579.9 + 295.4 - 281.1 = 594.2, 3,018 / 594.2 = 5.08; LTM Q3 3,042 / 593.7 = 5.12; operating income over debt expense 2,121.2 / 593.7 = 3.57.
- Cash-flow ratios: 1,293.7 / 10,832.2 = 11.9%; FY2025 1,310.6 / 10,344.6 = 12.7%; LTM Q1 (1,886.5 + 320.8 - 180.0 - (575.9 + 102.0 - 143.3)) = 1,492.7, over 10,694.3 = 14.0%; LTM Q2 (1,886.5 + 810.9 - 504.2 - (575.9 + 271.8 - 264.3)) = 1,609.8, over 10,847.5 = 14.8% (inputs from [Q1 10-Q] page:4 and [Q2 10-Q] page:4).

### Growth, shares and other derived figures

- Growth 9M 2026 over 9M 2025: revenue 10,547.8 / 10,023.3 - 1 = 5.2%; operating income 1,560.1 / 1,482.5 - 1 = 5.2%; adjusted operating income 1,622 / 1,508 - 1 = 7.6%; operating cash flow 1,329.7 / 1,345.8 - 1 = -1.2%; company free cash flow 672 / 716 - 1 = -6.1%.
- Share repurchases relative to cash generation: 870.2 / 898.4 = 97% of operating cash flow less additions (9M 2026). Net debt issuance: borrowings 3,511.3 less payments on long-term debt 3,021.0 = 490.3 ([Q3 10-Q] page:4; printed as 490 in [Q3 10-Q] page:44).
- Debt change from FY2025 to Q3 2026: 10,832.2 - 10,344.6 = 487.7 (rounded from 487.660). Cash change: 495.6 - 676.4 = -180.8.
- Maturity concentration: (4,570.3 + 3,765.1) / 10,832.2 = 76.9%, shown as about 77%. Seven maturity rows: 31.4 + 113.0 + 160.4 + 146.9 + 4,570.3 + 3,765.1 + 2,045.1 = 10,832.2.
- Springing maturity exposure: Term Loan A-2 1,962.5 + revolver 80.0 = 2,042.5.
- Unhedged floating debt: Term Loan A-2 balance subject to rate volatility 814.5 + revolver 80.0 = 894.5 (as stated in the filing).
- Liquidity: Q3 2026 cash 495.6 + undrawn revolver 1,420.0 = 1,915.6; FY2025 676.4 + 1,500.0 = 2,176.4; change -260.8. Including short-term investments: 1,986.3 at Q3 2026.
- Covenant headroom: 5.00 - 3.38 = 1.62x; EBITDA floor at constant net debt 10,269 / 5.00 = 2,053.8; cushion 3,042 - 2,053.8 = 988.2, which is 32.5% of 3,042; 4.00 - 3.38 = 0.62x.
- Guidance-implied Q4 free cash flow: 1,000 - 672 = 328 and 1,250 - 672 = 578.
- Noncontrolling share of 9M 2026 consolidated net income: 201.8 / 887.6 = 22.7%.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit Agreement and amendments not supplied; Consolidated EBITDA definition and covenant tests unverifiable; no compliance statement found | High | CP-2 | Supply the Credit Agreement and Ninth Amendment ([10-K] page:214 lists the base agreement) |
| Interim cash interest paid not printed (FY2025 only), so cash interest cover is Not supplied for 2026 | Medium | CP-1, CP-2 | Use expense-basis cover, labelled; supply cash-flow supplemental data if available |
| Consolidated EBITDA "Interest expense" (543 LTM at Q3 2026) differs from income-statement debt expense (593.7); the difference is not reconciled in the sources read | Low | CP-1, CP-2 | Treat as a definition difference; do not reconcile |
| Guarantor list and guarantor financial information not supplied | Medium | CP-2 | Supply Exhibit 21.1 and guarantor disclosure |
| Operating lease cost for LTM Q3 2026 not printed in the 10-Qs; lease-adjusted leverage not calculated | Medium | CP-2 | Use FY2025 lease cost for context only |
| Pension and retiree medical obligations not quantified (no balance sheet line; only an immaterial OCI item) | Low | CP-2 | None needed unless the 10-K note is requested |
| Events and filings dated after October 29, 2026 not supplied | Medium | CP-1A, CP-2 | Supply later 8-Ks or confirm none |
| Ratings, market prices and peer data not supplied | Low for this scope | CP-2 | Not required for CP-1 |
| Unit mix (thousands and millions) and issuer non-GAAP measures | Low | CP-1, CP-2 | Keep US$ millions with stated precision; label non-GAAP |

## Next module

- CP-1A: carry the segment split, the China impairment, the Elara Caring investment (closed July 20, 2026), the Berkshire settlement (October 27, 2026) and the guidance as events; label anything after October 29, 2026 as Not supplied.
- CP-2: use total debt of 10,832.2, Consolidated net debt of 10,269 and Consolidated EBITDA of 3,042 with their labels; keep the covenant at 5.00:1.00 (4.50:1.00 after December 31, 2028), the 4.00:1.00 relief threshold and the unverified definitions; classify operating leases, noncontrolling interest puts, letters of credit and the unhedged floating debt explicitly; carry the 2030 and 2031 maturity wall and the March 2, 2030 springing date.
- CP-5: trace each figure above to its `page:N` locator; the derived rows (LTM, quarters, ratios) are calculations, not source facts.
