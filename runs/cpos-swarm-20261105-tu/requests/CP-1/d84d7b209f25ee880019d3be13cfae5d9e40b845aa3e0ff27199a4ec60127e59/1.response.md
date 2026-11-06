# CP-1 financial base: TELUS CORP (tu)

## Request

- Issuer: TELUS CORP (issuer id `tu`; registrant "TELUS Corporation"), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run: `tu-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, module CP-1 (financial statements, debt, liquidity, covenants, cash flow and credit metrics). Execution: host session; no provider call.
- Periods (context): current period `q2-2026`, prior period `fy-2025`. This handoff labels every figure as one of: Q2 2026 (three months ended June 30, 2026), Q1 2026, Q4 2025, Q3 2025, FY2025 (assembled from four quarters, see Calculations), LTM to June 30, 2026 (four quarters Q3 2025 to Q2 2026), or a balance sheet date.
- Currency and units: the sources report in Canadian dollars, in millions (C$m) unless a row says otherwise. This matches the context's reporting currency CAD. The chart tables below ask for US$m in monetary cells. TELUS does not report in US$, so those monetary cells read `Not supplied: reported in C$ millions` and the C$ amounts are given in each row's basis column. Ratio cells in x are currency-neutral and are filled.
- Upstream handoff: the CP-0 source readiness handoff. Its limits are carried here: audited FY2025 statements (Exhibit 99.4 to the Form 40-F) not supplied; June 30, 2026 interim notes not supplied; debt-by-series table and maturity schedule only at March 31, 2026; credit agreements, indentures and named ratings not supplied; segment and perimeter changes across vintages.
- Scope limit: no credit conclusion beyond what the figures show, no legal interpretation and no valuation. Management claims are labelled as such.

## Sources

Locators are `page:N`, the chunk number in the pinned text file, not a printed page number. Short labels are used in citations as `[LABEL page:N "quote"]`.

| Label | Source (exact name) | sha256 | Role in this handoff |
| --- | --- | --- | --- |
| F40 | 40-F_2025-12-31_tu-20251231x40f.htm.jsonl | b0f2582e02ab1590b79f57963d19432006a5c182a75869a932135c754b75fcd3 | Form 40-F cover document; shows the audited statements are an exhibit outside the pack |
| Q3FS | 6-K-EX-99.1_2025-09-30_tm2525674d1_ex99-1.htm.jsonl | 436bedaf1f4dce1c7e6eb59881bfd06b2eda28c728cd8f139c3e87e5b19f9141 | Unaudited condensed interim statements and notes, September 30, 2025 |
| REL4Q25 | 6-K-EX-99.1_2026-02-12_tm261121d3_ex99-1.htm.jsonl | 86a3aab6322382ed8099639d74b8a5a665cd61822ab77656954f6c33682e6312 | Unaudited news release, fourth quarter 2025 (February 12, 2026) |
| Q1FS | 6-K-EX-99.1_2026-03-31_tm2610993d1_ex99-1.htm.jsonl | 786ff091c72b6c68ad509f7615fb77cb4d9d97ec151a629884165ec7501f67f6 | Unaudited condensed interim statements and notes, March 31, 2026 |
| REL1Q26 | 6-K-EX-99.1_2026-05-08_tm2610993d2_ex99-1.htm.jsonl | 4a46a2ffd615b6354baf9f5fba0823218c2071cb4a3fa919c80e6fdbc83658f3 | Unaudited news release, first quarter 2026 (May 8, 2026) |
| REL2Q26 | 6-K-EX-99.1_2026-07-31_tm2615221d2_ex99-1.htm.jsonl | 159e10207755e982fc8e0761482d512b4d2a82246d4508c8eb2d2f1f129bbd5c | Unaudited news release, second quarter 2026 (July 31, 2026) |
| MDA2Q26 | 6-K-EX-99.2_2026-06-30_tu-20260630xex99d2.htm.jsonl | df34bf40fbe3d3b13f773ae380315ed0a4e21b523c7736a3fcf69277289ecba4 | Management's discussion and analysis, second quarter 2026 (July 31, 2026) |
| context | context | 444f0b1a3ec6fedd71ff422ee4a294e2ddb38e2b78bcbad2de66f2441a8d4efa | User run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 544c6cab38ea7d4384375d826af7a24e93016625e263a47b8911621b1695f02d | Source readiness; its gaps are carried into this handoff |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| At June 30, 2026 TELUS reports net debt to EBITDA of 3.5 times, above its own objective and below the 4.25 covenant. Gross debt to EBITDA is 4.30 times and cash interest cover has fallen to 4.62 times. | Medium | Audited 2025 statements and second-quarter notes are not supplied, so 2025 totals are assembled from quarters and debt detail is dated March 31, 2026. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Reported net debt to EBITDA is 3.5 times, but the issuer gives the junior subordinated notes half equity credit; gross debt to EBITDA is higher at 4.30 times. | Leverage depends on the definition used; the covenant headroom of 0.70 times rests on the issuer's own definition. | Medium |
| Cash interest cover on EBITDA excluding restructuring fell from 5.09 times at March 31, 2026 to 4.62 times at June 30, 2026. | Less earnings cushion over cash interest, which includes a prepayment premium and lease interest. | Medium |
| Cash was 1,387 and revolver availability 657 at June 30, 2026; the issuer states over 2.7 billion of liquidity including the securitization. | Current maturities of 3,802 include commercial paper that the revolver backstops, so refinancing relies on rollover and new issuance. | Medium |
| A 2,135 impairment drove a net loss of 1,830 in the second quarter of 2026; the dividend was cut and 2026 guidance lowered. | Earnings and free cash flow are weaker; management cites the dividend reset as a deleveraging lever. | Medium |
| The last debt-by-series table and maturity schedule are at March 31, 2026, before further redemptions and commercial paper growth. | Refinancing needs at June 30, 2026 cannot be checked series by series. | High |

### Financial base view

TELUS is a large, investment-grade-rated Canadian telecommunications issuer whose reported leverage is 3.5 times net debt to EBITDA excluding restructuring and other costs at June 30, 2026, above both its previous and its newly set objective ranges, but below the covenant limit of 4.25 times. The financial base can be built from the pinned sources for the latest quarter and for four consecutive balance sheet dates, with limits. Reported leverage depends on a definition that gives half equity credit to the junior subordinated notes and adjusts for hedging items, so a gross view is also shown: total debt, including lease liabilities and short-term borrowings, is 4.30 times LTM EBITDA excluding restructuring and other costs. Cash interest cover on the same EBITDA is 4.62 times, down from 5.09 times a quarter earlier, partly because cash interest paid in Q2 2026 included a prepayment premium. Liquidity at June 30, 2026 is cash and temporary investments of 1,387, revolver availability of 657 after a 2,093 commercial paper backstop, securitization availability of 680 and a further 344 on a non-revolving bank facility due June 2027. Current maturities of long-term debt are 3,802. The second quarter brought a 2,135 impairment relating to TELUS Digital, a net loss of 1,830, a dividend reset and lower guidance. The view is restricted by missing audited FY2025 statements, missing second-quarter notes and missing agreements, so FY2025 flows are assembled from quarters and the debt register is dated March 31, 2026. All figures below are C$ millions unless stated.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Jun 30, 2026 | 4.30 | 3.55 | x | Total debt is calculated: long-term debt including current maturities and lease liabilities 30,231 plus short-term borrowings 1,225 = 31,456, over LTM EBITDA excluding restructuring and other costs 7,315. Net debt is the issuer figure 25,963 over 7,315, which gives 3.55 unrounded; the issuer reports 3.5. Issuer net debt deducts half equity credit for junior subordinated notes. |
| Mar 31, 2026 | 4.22 | 3.52 | x | Total debt 30,131 plus 920 = 31,051 over LTM EBITDA excluding restructuring and other costs 7,350. Net debt is the issuer figure 25,889 over 7,350; the issuer reports 3.5. Equity credit deducted was 3,661. |
| Dec 31, 2025 | 4.28 | Not supplied: net debt at December 31, 2025 is not printed in the pinned sources | x | Total debt 30,539 plus 920 = 31,459 over FY2025 EBITDA excluding restructuring and other costs 7,354. Management's release states a leverage ratio of 3.4-times at year-end 2025 (attributed claim, not a computed figure). The audited annual statements that would carry the net debt table are not supplied. |
| Sep 30, 2025 | 4.07 | 3.49 | x | Total debt 28,989 plus 922 = 29,911 over LTM EBITDA excluding restructuring and other costs 7,353. Net debt is the issuer figure 25,663 over 7,353; the issuer reports 3.5. Equity credit deducted was 2,232; the Series C, D, CAT and CAU junior subordinated notes were issued in December 2025 (Q1FS page:45), after this date. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| LTM to Jun 30, 2026 | 4.62 | x | EBITDA excluding restructuring and other costs 7,315 over cash interest paid 1,585 (Q3 2025 399, Q4 2025 306, Q1 2026 430, Q2 2026 450). Cash interest paid includes the interest component of lease payments and, in Q2 2026, a prepayment premium on a promissory note; it is gross of interest received. The issuer's own measure, EBITDA over net interest cost, is 4.9. |
| LTM to Mar 31, 2026 | 5.09 | x | EBITDA 7,350 over cash interest paid 1,443 (Q2 2025 308, Q3 2025 399, Q4 2025 306, Q1 2026 430). The issuer's own measure is 5.1. |
| FY2025 (LTM to Dec 31, 2025) | 5.31 | x | EBITDA 7,354 over cash interest paid 1,384 (Q1 2025 371, Q2 2025 308, Q3 2025 399, Q4 2025 306). The issuer's own measure at this date is Not supplied in the pinned sources. |
| LTM to Sep 30, 2025 | 5.26 | x | EBITDA 7,353 over cash interest paid 1,397 (Q4 2024 319, Q1 2025 371, Q2 2025 308, Q3 2025 399); the 1,397 matches the twelve-month figure printed in the September 2025 statements. The issuer's own measure is 5.2. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Jun 30, 2026 | Not supplied: reported in C$ millions | Not supplied: reported in C$ millions | US$m | Cash and temporary investments, net 1,387. Revolver availability 657 (2,750 size, nil drawn, nil letters of credit, 2,093 commercial paper backstop). Also stated: securitization availability 680 and non-revolving bank facility availability 344. The issuer's total is over 2.7 billion of liquidity (1,387 + 657 + 680). The 344 is stated separately and the issuer's total wording does not say whether it is included. |
| Mar 31, 2026 | Not supplied: reported in C$ millions | Not supplied: reported in C$ millions | US$m | Cash and temporary investments, net 1,302. Revolver net available 1,107 after a 1,643 commercial paper backstop. Securitization availability and any non-revolving facility availability are not printed at this date. |
| Dec 31, 2025 | Not supplied: reported in C$ millions | Not supplied: reported in C$ millions | US$m | Cash and temporary investments, net 2,621. Revolver net available 1,798 after a 952 commercial paper backstop. Securitization availability not printed at this date. |
| Sep 30, 2025 | Not supplied: reported in C$ millions | Not supplied: reported in C$ millions | US$m | Cash and temporary investments, net 1,827. Revolver net available 1,710 after a 1,040 commercial paper backstop. Securitization availability not printed at this date. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 (remainder of year) | Not supplied: reported in C$ millions | US$m | 3,148 composite principal repayments as at March 31, 2026, including lease principal of 333 (261 + 44 + 28). Commercial paper (1,643 at March 31, 2026) is classified as current because the revolver supports it [Q1FS page:43 "we classify it as a current portion of long-term debt"]; its allocation to this bucket is not itemized. Includes the 800 Series CZ notes due July 2026, of which 500 was redeemed on May 8, 2026 and 300 paid at maturity after June 30, 2026. Dated one quarter before the latest balance sheet. |
| 2027 | Not supplied: reported in C$ millions | US$m | 1,928, including the two U.S. dollar note series due in 2027 and lease principal. Dated March 31, 2026. |
| 2028 | Not supplied: reported in C$ millions | US$m | 2,319. Dated March 31, 2026. |
| 2029 | Not supplied: reported in C$ millions | US$m | 1,697. Dated March 31, 2026. |
| 2030 | Not supplied: reported in C$ millions | US$m | 1,869. Junior subordinated notes are shown at their first rate reset date, not their legal maturity. Dated March 31, 2026. |
| 2031 to 2035 | Not supplied: reported in C$ millions | US$m | 6,879, five years combined. Junior subordinated notes are shown at their first rate reset date. Dated March 31, 2026. |
| Thereafter | Not supplied: reported in C$ millions | US$m | 11,833. Dated March 31, 2026. The total across all buckets is 29,673 of principal, not reconciled to the 30,131 carrying amount of long-term debt. |

### Financials and credit metrics

| Metric | Unit | Q2 2026 / Jun 30, 2026 | Q1 2026 / Mar 31, 2026 | Q4 2025 / Dec 31, 2025 | Q3 2025 / Sep 30, 2025 | FY2025 | LTM to Jun 30, 2026 | Source and basis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Operating revenues and other income | C$m | 4,929 | 5,013 | 5,261 | 5,106 | 20,506 (calculated) | 20,309 (calculated) | MDA2Q26 eight-quarter table, page:29 |
| Net income (loss) | C$m | (1,830) | 144 | 290 | 431 | 777 (calculated) | (965) | MDA2Q26 page:29; LTM printed at page:59 |
| Impairment of intangible assets and goodwill | C$m | 2,135 | nil as printed | nil as printed | nil as printed | 500 (Q2 2025) | 2,135 | MDA2Q26 page:29; goodwill impairment of 500 in Q2 2025 per Q3FS page:3 |
| EBITDA | C$m | 1,588 | 1,522 | 1,746 | 1,753 | 6,922 | 6,609 (calculated) | MDA2Q26 page:29; FY2025 printed at Q1FS page:8 |
| Restructuring and other costs | C$m | 189 | 315 | 93 | 109 | 432 | 706 (calculated) | MDA2Q26 page:29; FY2025 printed at Q1FS page:8 |
| Adjusted EBITDA (equals EBITDA excluding restructuring and other costs) | C$m | 1,777 | 1,837 | 1,839 | 1,862 | 7,354 | 7,315 | MDA2Q26 page:29; LTM printed at page:59 |
| Cash provided by operating activities | C$m | 1,342 | 1,050 | 1,130 | 1,493 | 4,866 (calculated) | 5,015 (calculated) | MDA2Q26 page:29 |
| Free cash flow (issuer definition) | C$m | 545 | 583 | 574 | 611 | 2,208 (calculated) | 2,313 (calculated) | MDA2Q26 page:29; non-GAAP, excludes working capital and other items |
| Cash interest paid | C$m | 450 | 430 | 306 | 399 | 1,384 (calculated) | 1,585 (calculated) | MDA2Q26 page:52; Q1FS page:3; REL4Q25 page:29; Q3FS page:3 |
| Cash and temporary investments, net | C$m | 1,387 | 1,302 | 2,621 | 1,827 | as at Dec 31, 2025 | as at Jun 30, 2026 | MDA2Q26 page:50; Q1FS page:1; Q3FS page:1 |
| Short-term borrowings | C$m | 1,225 | 920 | 920 | 922 | as at Dec 31, 2025 | as at Jun 30, 2026 | MDA2Q26 page:50; Q1FS page:1; Q3FS page:2 |
| Current maturities of long-term debt | C$m | 3,802 | 4,092 | 3,102 | 3,200 | as at Dec 31, 2025 | as at Jun 30, 2026 | MDA2Q26 page:50; Q1FS page:2; Q3FS page:2 |
| Long-term debt, non-current | C$m | 26,429 | 26,039 | 27,437 | 25,789 | as at Dec 31, 2025 | as at Jun 30, 2026 | MDA2Q26 page:51; Q1FS page:2; Q3FS page:2 |
| Long-term debt including current maturities and lease liabilities | C$m | 30,231 | 30,131 | 30,539 | 28,989 | as at Dec 31, 2025 | as at Jun 30, 2026 | MDA2Q26 page:59; Q1FS page:39; Q3FS page:11 |
| Total debt (long-term debt plus short-term borrowings) | C$m | 31,456 (calculated) | 31,051 (calculated) | 31,459 (calculated) | 29,911 (calculated) | as at Dec 31, 2025 | as at Jun 30, 2026 | Sum of the two rows above |
| Net debt (issuer definition) | C$m | 25,963 | 25,889 | Not supplied: not printed in the pinned sources | 25,663 | Not supplied | 25,963 | MDA2Q26 page:59; Q1FS page:7; Q3FS page:11 |
| Junior subordinated notes equity credit deducted in net debt | C$m | Not supplied: not printed in the pinned sources | 3,661 | Not supplied: not printed in the pinned sources | 2,232 | Not supplied | Not supplied | Q1FS page:7; Q3FS page:11 |
| Net debt to EBITDA excluding restructuring and other costs, issuer reported | x | 3.5 | 3.5 | 3.4 (release claim) | 3.5 | 3.4 (release claim) | 3.5 | MDA2Q26 page:59; Q1FS page:7; REL4Q25 page:5; Q3FS page:11 |
| Total debt / EBITDA excluding restructuring and other costs | x | 4.30 (calculated) | 4.22 (calculated) | 4.28 (calculated) | 4.07 (calculated) | 4.28 (calculated) | 4.30 (calculated) | Calculated here; not an issuer measure |
| Total debt less cash / EBITDA excluding restructuring and other costs | x | 4.11 (calculated) | 4.05 (calculated) | 3.92 (calculated) | 3.82 (calculated) | 3.92 (calculated) | 4.11 (calculated) | Calculated here; no equity credit and no hedge adjustments |
| EBITDA / cash interest paid | x | 4.62 (calculated) | 5.09 (calculated) | 5.31 (calculated) | 5.26 (calculated) | 5.31 (calculated) | 4.62 (calculated) | Calculated here; each column is the twelve months to that date |
| EBITDA excluding restructuring and other costs interest coverage, issuer reported | x | 4.9 | 5.1 | Not supplied: not printed in the pinned sources | 5.2 | Not supplied | 4.9 | MDA2Q26 page:59; Q1FS page:7; Q3FS page:11; denominator is net interest cost |
| Common equity | C$m | 13,281 | 15,560 | 15,775 | 15,873 | as at Dec 31, 2025 | as at Jun 30, 2026 | MDA2Q26 page:51; Q1FS page:2; Q3FS page:2 |
| Non-controlling interests | C$m | 808 | 807 | 804 | 1,649 | as at Dec 31, 2025 | as at Jun 30, 2026 | MDA2Q26 page:51; Q1FS page:2; Q3FS page:2 |
| Total assets | C$m | Not supplied: totals not printed in the MD&A financial position table | 58,854 | 59,613 | 58,863 | as at Dec 31, 2025 | Not supplied | Q1FS page:1; Q3FS page:2 |
| Dividends declared per common share | C$ | 0.4184 | 0.4184 | 0.4184 | 0.4163 | Not supplied: four quarters not summed here | Not supplied | MDA2Q26 page:29; reset to 0.1875 per quarter declared July 30, 2026 |

### Segment and KPI view

Segment reporting was restated from January 1, 2026 (see Data quality and conflicts). The Q2 2026 reconciliation below carries the restated 2025 comparatives as printed.

| Segment, three months ended June 30 | Operating revenues and other income 2026 | 2025 (restated) | Adjusted EBITDA 2026 | 2025 (restated) | Source |
| --- | --- | --- | --- | --- | --- |
| TELUS technology solutions (TTech) | 3,746 | 3,842 | 1,639 | 1,640 | REL2Q26 page:20 and page:21 |
| TELUS Health | 536 | 519 | 99 | 98 | REL2Q26 page:20 and page:21 |
| TELUS Digital | 774 | 827 | 72 | 89 | REL2Q26 page:20 and page:21 |
| Eliminations | Not supplied: not printed in the appendix extract used | Not supplied | (33) | (15) | REL2Q26 page:20 |
| Consolidated | 4,929 | 5,082 | 1,777 | 1,812 | MDA2Q26 page:29; REL2Q26 page:20 |

Operating KPIs stated by management in the Q2 2026 release (attributed, non-GAAP or operating indicators): mobile phone net additions 17,000, internet net additions 20,000, connected device net additions 187,000, mobile phone ARPU $56.36, blended mobile phone churn 1.08 per cent [REL2Q26 page:1 "ARPU of $56.36"].

### Debt register at March 31, 2026 (latest series-level table)

Long-term debt composition (Q1FS Note 26(a)):

| Component | Mar 31, 2026 | Dec 31, 2025 | Ranking and security |
| --- | --- | --- | --- |
| TELUS Corporation senior notes | 17,664 | 18,191 | Senior unsecured |
| TELUS Corporation commercial paper | 1,643 | 952 | Senior unsecured, backstopped by the revolver |
| Other (unsecured) | 299 | 295 | Senior unsecured; includes a U.S. dollar promissory note repaid after March 31, 2026 |
| TELUS Corporation junior subordinated notes | 7,322 | 7,250 | Junior unsecured; subordinated to senior indebtedness |
| Other (secured) | 489 | 537 | Secured by AWS-4 spectrum licences; last period ending March 31, 2035 |
| Subtotal | 27,417 | 27,225 | Calculated sum equals the printed subtotal |
| Lease liabilities | 2,714 | 3,314 | Amortizing |
| Long-term debt | 30,131 | 30,539 | Current 4,092 and 3,102; non-current 26,039 and 27,437 |

Senior notes outstanding at March 31, 2026, face amounts in the currency shown (C$ unless marked US$). All are senior unsecured obligations of TELUS Corporation:

| Series | Maturity | Outstanding |
| --- | --- | --- |
| 3.75% Notes, Series CV | March 2026 | nil (redeemed January 16, 2026) |
| 2.75% Notes, Series CZ | July 2026 | 800 (500 redeemed May 8, 2026; 300 paid after June 30, 2026) |
| 2.80% U.S. Dollar Notes | February 2027 | US$600 |
| 3.70% U.S. Dollar Notes | September 2027 | US$500 |
| 2.35% Notes, Series CAC | January 2028 | 600 |
| 3.625% Notes, Series CX | March 2028 | 600 |
| 4.80% Notes, Series CAO | December 2028 | 700 |
| 3.30% Notes, Series CY | May 2029 | 1,000 |
| 5.00% Notes, Series CAI | September 2029 | 350 |
| 3.15% Notes, Series CAA | February 2030 | 600 |
| 5.60% Notes, Series CAM | September 2030 | 500 |
| 2.05% Notes, Series CAD | October 2030 | 500 |
| 4.95% Notes, Series CAP | February 2031 | 600 |
| 4.65% Notes, Series CAQ | August 2031 | 700 |
| 2.85% Sustainability-Linked Notes, Series CAF | November 2031 | 750 |
| 3.40% U.S. Dollar Sustainability-Linked Notes | May 2032 | US$900 |
| 5.25% Sustainability-Linked Notes, Series CAG | November 2032 | 1,100 |
| 4.95% Sustainability-Linked Notes, Series CAJ | March 2033 | 500 |
| 5.75% Sustainability-Linked Notes, Series CAK | September 2033 | 850 |
| 5.10% Sustainability-Linked Notes, Series CAN | February 2034 | 500 |
| 4.40% Notes, Series CL | April 2043 | 129 |
| 5.15% Notes, Series CN | November 2043 | 400 |
| 4.85% Notes, Series CP | April 2044 | 900 |
| 4.75% Notes, Series CR | January 2045 | 400 |
| 4.40% Notes, Series CU | January 2046 | 60 |
| 4.70% Notes, Series CW | March 2048 | 89 |
| 4.60% U.S. Dollar Notes | November 2048 | US$561 |
| 4.30% U.S. Dollar Notes | June 2049 | US$371 |
| 3.95% Notes, Series CAB | February 2050 | 73 |
| 4.10% Notes, Series CAE | April 2051 | 49 |
| 5.65% Notes, Series CAH | September 2052 | 550 |
| 5.95% Notes, Series CAL | September 2053 | 400 |

Junior subordinated notes outstanding at March 31, 2026 (fixed-to-fixed rate, unsecured, subordinated to senior indebtedness): Series CAR 6.25%, 1,500, due July 2055, no-call to July 21, 2030; Series CAS 6.75%, 925, due July 2055, no-call to July 21, 2035; U.S. dollar Series A 6.625%, US$700, due October 2055, no-call to October 15, 2030; Series B 7.000%, US$800, due October 2055, no-call to October 15, 2035; Series C 6.375%, US$800, due June 2056, no-call to June 9, 2031; Series D 6.625%, US$700, due June 2056, no-call to June 9, 2036; Series CAT 5.375%, 400, due June 2056, no-call to June 9, 2031; Series CAU 5.875%, 400, due June 2056, no-call to June 9, 2036. The face amounts and dates are as printed in Q1FS Note 26(f). Upon a rating event, as defined in the supplemental indenture, TELUS must offer to repurchase at 102 per cent [Q1FS page:45 "we must offer to repurchase the notes at a price equal to 102% of their principal amount"]. Senior notes carry a change-of-control put at 101 per cent [Q1FS page:39 "at a price equal to 101% of their principal amount"].

Other debt-like claims and facilities:

- Revolving credit facility: unsecured, 2,750, expiring August 21, 2030, shared by the commercial paper program [MDA2Q26 page:60 "expiring August 21, 2030"].
- Non-revolving bank facility: unsecured, 650 (or U.S. dollar equivalent), maturing June 2027, availability 344 at June 30, 2026 [MDA2Q26 page:62].
- Securitization: up to 1,600 of borrowings secured by trade receivables and unbilled customer finance receivables, term to May 22, 2027, minimum cash advances of approximately 920 [MDA2Q26 page:62].
- Letters of credit: 61 outstanding under uncommitted facilities at June 30, 2026, with 124 available [MDA2Q26 page:62].
- Guarantees: none of the instruments above is stated to be guaranteed by a subsidiary. The notes are described as effectively subordinated to obligations of, or guaranteed by, subsidiaries. Guarantor structure is Not supplied.

### Definitions review

- EBITDA is operating revenues and other income less goods and services purchased and employee benefits expense [MDA2Q26 page:81 "EBITDA as calculated by TELUS is equivalent to Operating revenues and other income less the total of Goods and services purchased expense and Employee benefits expense"]. It includes restructuring and other costs; impairment is added back in the segment reconciliation, so EBITDA is stated before impairment [REL2Q26 page:20].
- EBITDA excluding restructuring and other costs is the leverage and coverage numerator. In Q2 2026 and every quarter in the eight-quarter table it equals Adjusted EBITDA [REL2Q26 page:20 "EBITDA – excluding restructuring and other costs and Adjusted EBITDA 1,639"]. Adjusted EBITDA excludes items the issuer considers unusual [MDA2Q26 page:81].
- Net debt is long-term debt less the junior subordinated notes equity credit, plus debt issuance costs, less hedging derivative and accumulated other comprehensive income items, less cash, plus short-term borrowings [Q1FS page:7 "TELUS Corporation junior subordinated notes equity credit deducted in calculating net debt"]. For the equity credit, "only one-half of the principal of our junior subordinated notes is included as debt" [MDA2Q26 page:57]. The net debt components at June 30, 2026 are not printed in the pinned sources because they sit in the unsupplied Note 3.
- Net interest cost is financing costs adjusted for pension net interest, capitalized interest, debt-purchase gains and virtual power purchase agreement items [MDA2Q26 page:85]. It is an accrual measure, not cash interest.
- Covenants: leverage must not exceed 4.25 to 1.00 and coverage must not be less than 2.00 to 1.00 at each quarter-end; the reported ratios at June 30, 2026 are 3.5 and 4.9, and "There are certain minor differences in the calculation" against the management measures [MDA2Q26 page:61]. The Q1FS describes the second test as an operating cash flow to interest expense ratio [Q1FS page:43 "our operating cash flow to interest expense ratio must not be less than 2.00:1.00"]. The credit agreement definitions are not supplied.
- Objective range changed. In Q1FS the objective range is 2.2 to 2.7 times [Q1FS page:8 "Our long-term objective range for this ratio is 2.2 – 2.7 times"]. The June 2026 MD&A shows 2.5 to 3.0 times, with an objective of about 3.0 times in 2028 [MDA2Q26 page:27 "Net debt to EBITDA – excluding restructuring and other costs ratio of 2.5 to 3.0 times"]. Comparisons to the objective must name the vintage.
- Free cash flow is the issuer's non-GAAP measure and excludes certain working capital changes, proceeds from divested assets and other items [MDA2Q26 page:83 "Free cash flow: We report this measure"]. It is not a covenant measure.

### Covenant and liquidity position at June 30, 2026

- Leverage covenant: reported ratio 3.5 against a 4.25 limit [MDA2Q26 page:61 "As at June 30, 2026, our consolidated leverage ratio was 3.5 to 1.00 and our consolidated coverage ratio was 4.9 to 1.00"]. Using the unrounded issuer net debt over EBITDA, headroom is 0.70 times, or an EBITDA cushion of 1,206 (16.5 per cent) before the 4.25 limit is reached at constant net debt (see Calculations). This uses the management ratio, not the covenant definition.
- Coverage covenant: reported 4.9 against a 2.00 floor, a difference of 2.9 times.
- Continued access to the credit facilities is not contingent on a specific credit rating [MDA2Q26 page:61 "Continued access to our credit facilities is not contingent on maintaining a specific credit rating"]. Access to the U.S. commercial paper market depends on ratings.
- Ratings: "investment-grade" wording only [MDA2Q26 page:62]. Agency names and grades are Not supplied.
- Liquidity: the issuer's total of over 2.7 billion reproduces from cash 1,387, revolver 657 and securitization 680 (2,724, see Calculations). Management's stated objective is generally at least 1 billion of available liquidity [MDA2Q26 page:63 "generally maintaining at least $1 billion of available liquidity"].
- Commercial paper outstanding was 2.1 billion (US$1.5 billion) at June 30, 2026, up from 1.0 billion (US$0.7 billion) at December 31, 2025, and is fully backstopped by the revolver [MDA2Q26 page:56]. The facility table shows a 2,093 commercial paper backstop against the 2,750 revolver, which leaves the 657 of availability.
- Shelf prospectus: unlimited in Canada and 1.9 billion in the United States until January 2029 [MDA2Q26 page:63].

### Non-debt claims and funding review

| Claim | Amount | Inside or outside the debt figure | Source |
| --- | --- | --- | --- |
| Lease liabilities | 2,714 at Mar 31, 2026; 3,314 at Dec 31, 2025 | Inside long-term debt | Q1FS page:39 |
| Pension benefit liabilities | 452 at Mar 31, 2026; 453 at Dec 31, 2025 | Outside debt (other long-term liabilities) | Q1FS page:47 |
| Other post-employment benefit liabilities | 95 at Mar 31, 2026; 98 at Dec 31, 2025 | Outside debt | Q1FS page:47 |
| Written put options and contingent consideration provisions | 240 at Mar 31, 2026 (current 174, non-current 66) | Outside debt; part reclassified to current in Q2 2026 | Q1FS page:37; MDA2Q26 page:50 |
| Total provisions | 965 at Mar 31, 2026 | Outside debt | Q1FS page:37 |
| Property, plant and equipment contractual commitments | 219 at Mar 31, 2026 | Outside debt | Q1FS page:31 |
| Intangible asset contractual commitments | 44 at Mar 31, 2026 | Outside debt | Q1FS page:33 |
| Supply chain financing | 29 of trade payables within the program at Mar 31, 2026 | Outside debt (accounts payable) | Q1FS page:36 |
| Dividends payable | 659 at Jun 30, 2026 | Outside debt; paid in July 2026 | MDA2Q26 page:50 |
| Non-controlling interests, including Terrion | 808 at Jun 30, 2026 | Outside debt | MDA2Q26 page:51 |
| Claims and lawsuits | No amount provided | Outside debt; management says liability unlikely to be material beyond Note 29 items | MDA2Q26 page:64; Q1FS page:50 |
| Millimetre wave spectrum auction | Amount Not supplied; auction set for October 2027 | Future cash call, outside debt | MDA2Q26 page:66 |
| Stated annual contractual obligations table | Not supplied: in Exhibit 99.4 of the Form 40-F, not in the pack | n/a | F40 page:6 |

### Subsequent events and guidance

- After June 30, 2026 the remaining 300 of the 2.75% Series CZ notes was paid at maturity [MDA2Q26 page:56 "Subsequent to June 30, 2026, the remaining $300 million was paid upon maturity in the normal course"].
- July 31, 2026: dividend reset to 0.1875 per quarter (0.75 annualized from 1.6736), expected to produce cumulative cash savings of approximately 2.7 billion through 2028; the dividend reinvestment plan discount ends October 1, 2026 [REL2Q26 page:4 "representing a reset of 55 per cent to an annualized amount of $0.75 per share"].
- Guidance (management claims): previous and updated 2026 targets, per the release table: service revenue growth 2% to 4% moved to flat to (2%); Adjusted EBITDA growth 2% to 4% moved to (2%) to (4%); capital expenditures approximately 2.3 billion moved to approximately 2.6 billion; free cash flow approximately 2.45 billion moved to approximately 1.8 billion [REL2Q26 page:10 "Free cash flow Approximately $2.45 billion Approximately $1.8 billion"].
- Management states net debt to Adjusted EBITDA of 3.5-times and a target of about 3.0-times or lower by year-end 2028, aided by the dividend reset and asset monetization processes underway (TELUS Health non-core assets and non-core real estate); no proceeds or buyers are quantified [REL2Q26 page:4 "the company remains active in the market on TELUS Health-related non-core assets"].
- Nothing after July 31, 2026 is supplied.

### Data quality and conflicts

- No audited FY2025 financial statements: FY2025 totals are sums of four quarters; EBITDA, restructuring and Adjusted EBITDA for FY2025 tie to the Q1FS printed table (6,922, 432, 7,354).
- Cross-source ties that agree: LTM net loss of (965) printed in MDA2Q26 page:59 equals the four-quarter sum; LTM EBITDA excluding restructuring and other costs of 7,315 equals the sum of Adjusted EBITDA over four quarters; the 12-month cash interest of 1,397 at September 30, 2025 printed in Q3FS page:14 equals the sum of its quarters; long-term debt at June 30, 2026 of 30,231 equals current maturities 3,802 plus non-current 26,429; Dec 31, 2025 balances in Q1FS and MDA2Q26 agree (cash 2,621, current maturities 3,102, long-term debt 27,437).
- Name conflict (not a figure conflict): the July release calls the leverage measure "Net debt to Adjusted EBITDA" and the MD&A "Net debt to EBITDA – excluding restructuring and other costs". Both read 3.5 and the two EBITDA measures are equal in the reconciliation, so no figure conflict arises.
- Superseded guidance: the May 8, 2026 release stated free cash flow of approximately 2.45 billion and leverage targets of 3.3-times or lower by year-end 2026 [REL1Q26 page:1 "3.3-times or lower by year-end 2026 and 3.0-times or better by year-end 2027"]. The July 31, 2026 release supersedes them.
- Segment restatement: the 2026 filings restate 2025 segment results for the TELUS Digital privatization (MDA2Q26 page:9). The Q3FS and REL4Q25 use the earlier structure. Segment figures are only compared within one vintage.
- Perimeter: TELUS Digital was consolidated with a non-controlling interest until October 31, 2025; Terrion has had a non-controlling interest since July 2025. Terrion-related equity of 1,261 was issued to the non-controlling interest in Q3 2025 and appears in financing cash flows [Q3FS page:3 "Equity of subsidiary issued to non-controlling interest (Note 28(b)) 1,261"].
- Cash interest paid includes the interest component of lease payments [Q3FS page:46 "the interest component of lease payments is included in Interest paid"]. It also includes a Q2 2026 prepayment premium described in MDA2Q26 page:52.
- Text extraction: flattened tables; footnote markers attach to labels such as "Net debt1".

### Interpretation: evidence, mechanism, implication

- Leverage is definition-dependent. Evidence: net debt of 25,963 uses half equity credit for junior subordinated notes and EBITDA of 7,315. Mechanism: the notes are subordinated and carry a rating-event repurchase at 102 per cent, so the equity credit depends on agency treatment; if lost, reported leverage rises toward the gross figure. Implication: senior creditors should monitor the gross ratio of 4.30 times as well as the covenant ratio, because covenant headroom is 0.70 times on the issuer's own definition.
- Cash interest cover is moving down. Evidence: EBITDA over cash interest paid fell from 5.31 at FY2025 to 4.62 at June 30, 2026. Mechanism: interest paid rose by 142 in Q2 2026 and 201 in H1 2026 on 2025 junior subordinated issuance, the promissory note and the prepayment premium, while LTM EBITDA excluding restructuring and other costs fell from 7,354 to 7,315. Implication: cash cover has less margin, although part of the Q2 2026 rise is one-off.
- Refinancing and liquidity. Evidence: current maturities of long-term debt of 3,802, commercial paper of 2.1 billion fully backstopped by a revolver with 657 availability. Mechanism: commercial paper is classified as current but is supported by the revolver, so it consumes revolver capacity one for one and the availability of 657 is what remains after that backstop. The other current maturities, including the US$600 million 2.80% notes reclassified to current and the Series CZ balance paid in July 2026, rely on cash of 1,387, securitization availability of 680, non-revolving availability of 344 or new issuance. Implication: near-term maturities depend on commercial paper rollover and market access; the investment-grade wording supports access but ratings are not supplied and not tested here.
- Earnings quality. Evidence: Q2 2026 Adjusted EBITDA of 1,777 versus 1,812 and a 2,135 non-cash impairment; Digital Adjusted EBITDA 72 versus 89. Mechanism: the impairment does not affect EBITDA or covenants, which are not impacted by revaluation of goodwill [MDA2Q26 page:61 "The covenants are not impacted by revaluation"], but signals lower recoverable value in the TELUS Digital unit. Implication: covenant headroom is unaffected by the impairment, while the lower guidance affects forward leverage.
- Dividend reset. Evidence: dividends paid 864 in H1 2026 against free cash flow of 1,128 in the same half. Mechanism: the quarterly dividend falls from 0.4184 to 0.1875 per share. Implication: management cites this as a deleveraging lever; the 2.7 billion saving through 2028 is a management estimate.

## Calculations

All inputs are C$ millions from the cited sources. Calculated cells are labelled in the tables above.

1. FY2025 flows (sum of four quarters, MDA2Q26 page:29):
   - Operating revenues and other income: 5,057 + 5,082 + 5,106 + 5,261 = 20,506.
   - Net income: 301 + (245) + 431 + 290 = 777.
   - EBITDA: 1,744 + 1,679 + 1,753 + 1,746 = 6,922; ties to Q1FS page:8.
   - Restructuring and other costs: 97 + 133 + 109 + 93 = 432; ties to Q1FS page:8.
   - Adjusted EBITDA: 1,841 + 1,812 + 1,862 + 1,839 = 7,354; ties to Q1FS page:8.
   - Cash provided by operating activities: 1,077 + 1,166 + 1,493 + 1,130 = 4,866.
   - Free cash flow: 488 + 535 + 611 + 574 = 2,208.
2. LTM to June 30, 2026 (Q3 2025, Q4 2025, Q1 2026, Q2 2026):
   - Operating revenues and other income: 5,106 + 5,261 + 5,013 + 4,929 = 20,309.
   - Net income: 431 + 290 + 144 + (1,830) = (965); ties to MDA2Q26 page:59.
   - EBITDA: 1,753 + 1,746 + 1,522 + 1,588 = 6,609.
   - Restructuring and other costs: 109 + 93 + 315 + 189 = 706. EBITDA excluding restructuring and other costs: 6,609 + 706 = 7,315; ties to MDA2Q26 page:59.
   - Cash provided by operating activities: 1,493 + 1,130 + 1,050 + 1,342 = 5,015.
   - Free cash flow: 611 + 574 + 583 + 545 = 2,313.
3. Cash interest paid, twelve months:
   - Jun 30, 2026: 399 + 306 + 430 + 450 = 1,585.
   - Mar 31, 2026: 308 + 399 + 306 + 430 = 1,443. Dec 31, 2025: 371 + 308 + 399 + 306 = 1,384. Sep 30, 2025: 319 + 371 + 308 + 399 = 1,397; ties to Q3FS page:14.
   - Quarter inputs: Q1 2025 371 (Q1FS page:3), Q2 2025 308 (MDA2Q26 page:52), Q3 2025 399 (Q3FS page:3; also nine months 1,078 less H1 679), Q4 2025 306 and Q4 2024 319 (REL4Q25 page:29), Q1 2026 430 (Q1FS page:3), Q2 2026 450 (MDA2Q26 page:52).
4. Total debt = long-term debt including current maturities and lease liabilities plus short-term borrowings:
   - Jun 30, 2026: 30,231 + 1,225 = 31,456. Mar 31, 2026: 30,131 + 920 = 31,051. Dec 31, 2025: 30,539 + 920 = 31,459. Sep 30, 2025: 28,989 + 922 = 29,911.
5. Total debt / EBITDA excluding restructuring and other costs: 31,456 / 7,315 = 4.30; 31,051 / 7,350 = 4.22; 31,459 / 7,354 = 4.28; 29,911 / 7,353 = 4.07.
6. Issuer net debt / EBITDA: 25,963 / 7,315 = 3.549; 25,889 / 7,350 = 3.522; 25,663 / 7,353 = 3.490. Dec 31, 2025: Not calculable, net debt not printed.
7. Total debt less cash / EBITDA: (31,456 − 1,387) / 7,315 = 4.11; (31,051 − 1,302) / 7,350 = 4.05; (31,459 − 2,621) / 7,354 = 3.92; (29,911 − 1,827) / 7,353 = 3.82.
8. EBITDA / cash interest: 7,315 / 1,585 = 4.62; 7,350 / 1,443 = 5.09; 7,354 / 1,384 = 5.31; 7,353 / 1,397 = 5.26.
9. Covenant headroom at June 30, 2026, on the management measure: leverage 4.25 − 3.549 = 0.70 times. Net debt at the limit: EBITDA needed is 25,963 / 4.25 = 6,109; cushion 7,315 − 6,109 = 1,206, which is 16.5 per cent of 7,315. Coverage: 4.9 − 2.00 = 2.9 times.
10. Net debt before equity credit (illustrative, not an issuer measure): Mar 31, 2026: 25,889 + 3,661 = 29,550, over 7,350 = 4.02; Sep 30, 2025: 25,663 + 2,232 = 27,895, over 7,353 = 3.79. June 30, 2026: Not calculable, the equity credit is not printed.
11. Liquidity reproduction: 1,387 + 657 + 680 = 2,724, consistent with the issuer's "over $2.7 billion". Including the non-revolving availability: 2,724 + 344 = 3,068, not an issuer figure. Cash plus revolver: 1,387 + 657 = 2,044.
12. Maturity schedule check: 3,148 + 1,928 + 2,319 + 1,697 + 1,869 + 6,879 + 11,833 = 29,673; ties to the printed total. Difference from carrying long-term debt 30,131 − 29,673 = 458, not reconciled.
13. Lease principal, 2026 remainder: 261 + 28 + 44 = 333 (Canadian dollar, U.S. dollar and other currency lease columns).

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Audited FY2025 statements and annual MD&A not supplied; FY2025 flows assembled from quarters; no FY2025 net debt table | High | CP-2, CP-5 | Supply Exhibit 99.4 of the Form 40-F |
| June 30, 2026 interim statements and notes not supplied: net debt components, debt by series, lease liabilities, provisions detail and covenant text at that date | High | CP-2, CP-5 | Supply the interim statements that accompany the MD&A |
| Series-level debt register and maturity schedule dated March 31, 2026 | Medium | CP-2 | Label the date; supply June 30, 2026 Note 26 |
| Credit agreement covenant definitions and guarantor structure not supplied; reported ratios use management definitions | Medium | CP-2, CP-5 | Supply the credit agreements and indentures |
| Net debt and issuer coverage at December 31, 2025 not printed | Medium | CP-2 | Supply Exhibit 99.4 |
| Junior subordinated equity credit at June 30, 2026 not printed | Medium | CP-2 | Supply June 30, 2026 Note 3 |
| Named ratings and outlooks not supplied | Medium | CP-2 | Supply agency reports |
| Securitization and non-revolving facility availability not printed before June 30, 2026, so liquidity history is revolver and cash only | Low | CP-2 | Supply earlier availability disclosures |
| Segment restatement and perimeter changes limit period comparisons | Medium | CP-1A, CP-2 | Compare within one vintage only |
| Pension, provision and commitment detail at June 30, 2026 not printed | Low | CP-2 | Supply June 30, 2026 notes |
| Nothing after July 31, 2026 supplied | Medium | CP-2, CP-5 | Supply later filings |
| Text extraction only; flattened tables | Low | CP-5 | Use filed HTML or XBRL if layout matters |

## Next module

CP-1A (business and transaction context) is next, then CP-2 and CP-5. CP-1A should use this handoff for the privatization of TELUS Digital, the Terrion minority equity, the impairment and the dividend reset. CP-2 should carry the definition dependence of leverage (3.5 reported, 4.30 gross), the covenant headroom of 0.70 times on the management measure, the March 31, 2026 date of the debt register and maturity wall, the securitization and non-revolving sources that sit outside the revolver, and the missing agreements and ratings. CP-5 should treat FY2025 figures as assembled, not audited.
