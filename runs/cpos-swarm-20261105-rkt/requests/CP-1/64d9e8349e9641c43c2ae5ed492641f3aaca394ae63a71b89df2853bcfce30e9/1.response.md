## Request

Module CP-1 (financial base view) for Rocket Companies, Inc. (issuer id rkt, NYSE: RKT), as of 2026-11-05, pathway credit_snapshot, case kind public. The context sets the cutoff at 2026-11-05, the current period at q3-2026 (quarter ended 2026-09-30), the prior period at fy-2025 (fiscal year ended 2025-12-31) and the reporting currency at USD. All amounts are US dollars in millions unless a cell says otherwise. The sources report in US dollars and in millions (Q3 10-Q page:5; Q3 release page:1), so no currency or scale conversion is needed. Periods are the company's calendar periods: FY2025, the quarters of 2026, nine months 2026 and nine months 2025. The context file lists no borrower, parent, guarantors, ratings, quotes or peers, and its blank fields are not read as zero.

The module builds the financial base view a credit committee reads first: reported statements, the debt stack, liquidity, maturities, leverage, interest cover and the definitions behind them. It does not give a rating view, relative value or a recommendation. It uses the CP-0 readiness handoff, which rated every requested consumer READY_WITH_LIMITATIONS and listed the limitations carried here. This module does not correct any CP-0 statement; where it adds precision (the revenue captions are not comparable across FY2025 and 2026, see Findings), that is a new limitation and not a correction.

Locator convention: `<source alias> page:N`, where N is the extracted chunk number of the pinned text file, not the printed page. Aliases are defined in the first table under Sources.

## Sources

### Issuer sources relied on

| Alias | Exact source name | sha256 | Document family and period |
| --- | --- | --- | --- |
| 10-K | 10-K_2025-12-31_rkt-20251231.htm.jsonl | 3f00d23a5a4d987299ba3ee372766fbda78de035096653b1d865a69d888922ae | Annual report, fiscal year ended December 31, 2025, audited, signed March 2, 2026 |
| Q1 10-Q | 10-Q_2026-03-31_rkt-20260331.htm.jsonl | 0a828436cfdb4cb6430873bcdf676f4a2758eb6f8aaf83bcd5c4c1bd9959be37 | Quarterly report, quarter ended March 31, 2026, unaudited |
| Q2 10-Q | 10-Q_2026-06-30_rkt-20260630.htm.jsonl | 4ca13e8689778101de80b67ba6d799666890bfd97332aef7adca82c2e094e90b | Quarterly report, quarter ended June 30, 2026, unaudited |
| Q3 10-Q | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | 59c56634da7bee8e5debdbfce480876851737d0b5ddf01b6f700d4f40ecd6bce | Quarterly report, quarter ended September 30, 2026, unaudited, signed October 30, 2026 |
| Q1 release | EX-99.1_2026-05-07_rkt-earningsrelease3312026.htm.jsonl | 7d218dea46aff3c8af9298dca5b852af49f0e5f073ef0f93c5f3b622d0854392 | Earnings release exhibit, first quarter 2026, dated May 7, 2026 |
| Q2 release | EX-99.1_2026-08-06_rkt-063020268xkex991earnin.htm.jsonl | 6542f2db604c3ffa41383bd56c69d56492031f4ee91e3c42b828c315d7979477 | Earnings release exhibit, second quarter 2026, dated August 6, 2026 |
| Q3 release | EX-99.1_2026-10-29_rkt-093020268xkex991earnin.htm.jsonl | 51281ba557de6ffcbe69b458cb58d0ccec82e27e457e960477651f50df28d346 | Earnings release exhibit, third quarter 2026, dated October 29, 2026 |

The first line of each pinned text file quotes a different sha256: that is the hash of the original HTML document, not of the pinned text file. The hashes above are the pinned text-file hashes supplied by CP-OS.

### Run context

| Source | sha256 | Role |
| --- | --- | --- |
| context | 2c3b1fbba94f4a511900e452ab48c8c288b5d2472b9c175cb66b98c0de72d2ac | The user's dated settings for this run. Not issuer evidence. |

### Handoffs supplied

| Module | sha256 | Use in this module |
| --- | --- | --- |
| CP-0 | b5fd40886eeedd24c855cc4c21dd662543a58c822d0fb2b19a168fce8c895924 | Source readiness: effective source set, perimeter and presentation changes, and gaps (no covenant levels, no guarantor names, no ratings, no interim cash interest, no discrete fourth quarter 2025). All carried into this module. |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| On last-twelve-month adjusted EBITDA of $2,843 million, unsecured senior notes of $10,743 million equal 3.78x gross and 2.83x net of cash, but earnings are rate-sensitive and fourth-quarter guidance points lower. | Medium | Cash interest, covenant levels, guarantors and undrawn secured availability are not printed, and the earnings base includes both acquisitions fully only from the fourth quarter of 2025. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Unsecured senior notes total $10,743 million with no maturity before April 2027, then $1,500 million due in 2029 and $2,076 million due in 2030. | Corporate refinancing needs are back-ended; the $503 million convertible due in 2027 is the first maturity. | High |
| Secured financing of $14,187 million exceeds the $7,400 million committed secured line amount and mostly sits on lines maturing in 2027 and 2028. | Warehouse renewals are the recurring rollover risk, and cross-default terms mean a facility default could reach other facilities. | Medium |
| Company-stated liquidity is $11.4 billion, but only the $2,699 million of cash and the $2,500 million undrawn revolver tie to the filings. | Usable liquidity may be lower than stated until the basis of the $6.2 billion of secured availability is confirmed. | Medium |
| Adjusted EBITDA excludes bond interest but deducts funding interest, and accrual bond interest cover is 4.94x for the last twelve months. | Cash interest cover cannot be read for 2026, so debt service capacity rests on an accrual proxy. | Medium |
| Leverage ratios of 8.16x for FY2025 and 5.65x for March 31, 2026 rest on earnings that did not yet include Mr. Cooper for a full year. | Only the September 30, 2026 ratio uses a full post-acquisition earnings base; the earlier ratios overstate leverage. | Medium |

### Financial base view

Rocket Companies, Inc. is a Delaware holding company (Q3 10-Q page:1) whose subsidiaries originate and service US residential mortgages and run real estate and personal finance businesses (Q3 10-Q page:8). Its funded debt has two layers that must not be mixed. The first is unsecured corporate debt: senior notes with principal of 10,743 at September 30, 2026 and a revolving credit facility of 2,500 that is undrawn (Q3 10-Q page:30). The second is secured financing of 14,187: repurchase agreements, early funding facilities, MSR lines, advance facilities and personal loan lines, collateralized by loans held for sale, MSRs and advance receivables (Q3 10-Q page:27 to page:29). The company's adjusted EBITDA is stated after the interest on secured financing and before bond interest on the senior notes (Q3 release page:10), so the consistent leverage numerator is the unsecured debt. On that basis, unsecured debt of 10,743 over last-twelve-month adjusted EBITDA of 2,843 gives 3.78x, and 2.83x net of cash of 2,699. Both are computed here from printed components; no net debt or debt to EBITDA ratio is printed in any of the seven sources.

The direction of travel is favourable but the base is thin. The ratio on FY2025 earnings is 8.16x and on March 31, 2026 last-twelve-month earnings 5.65x, because debt already included the notes assumed from Mr. Cooper while earnings held only part of a year of that business (Mr. Cooper was acquired on October 1, 2025; Q3 10-Q page:8). Unsecured principal rose from 10,455 at December 31, 2025 to 10,743 at September 30, 2026 (Q3 10-Q page:30), so the improvement comes from earnings, not from debt reduction. The September 30, 2026 last-twelve-month period is the first made only of quarters that include both acquisitions.

Earnings are cyclical and rate-sensitive. Adjusted revenue was 2,822 in Q1 2026, 2,761 in Q2 2026 and 2,574 in Q3 2026, and the company guides fourth-quarter 2026 adjusted revenue to between 2.1 billion and 2.3 billion (Q3 release page:3), below each of the three 2026 quarters. The Q3 10-Q ties the quarter to a rise in the 30-year mortgage rate from 6.43% in early July to 7.28% at the end of September and a smaller mortgage market than in the second quarter (Q3 10-Q page:49). GAAP net income of 709 in Q3 2026 includes a valuation gain on MSRs that the company removes from adjusted measures (710 in the adjusted revenue reconciliation, Q3 release page:6), so GAAP and adjusted earnings tell different stories and the committee should anchor on the adjusted measures with that caveat. Last-twelve-month adjusted EBITDA includes three quarters of higher adjusted revenue than the guided fourth quarter, which means the 3.78x ratio is not a forward run-rate.

Liquidity is stated by the company at 11.4 billion at September 30, 2026, made of cash of 2.7 billion, undrawn lines of credit of 2.5 billion and undrawn available MSR and advance lines of 6.2 billion (Q3 10-Q page:67). Cash of 2,699 and the undrawn revolver of 2,500 tie to the filings. The 6.2 billion does not tie to the secured financing table, which prints line amount, committed amount and outstanding balance but no availability (see Calculations). Most secured funding sits on uncommitted capacity: secured outstanding of 14,187 exceeds the committed secured line amount of 7,400 (Q3 10-Q page:29), and the 10-K flags the larger uncommitted portion of its loan funding facilities as a risk (10-K page:47). Covenants are described by type with compliance stated, and no level or headroom is printed (Q3 10-Q page:27), so covenant headroom is Not calculable.

Interest cover on a cash basis is available only for FY2025 and is mixed in basis; the quarterly reports do not print cash paid for interest. An accrual proxy, adjusted EBITDA over bond interest expense, is 4.94x for the last twelve months to September 30, 2026. The confidence in this base view is Medium: statements, debt and liquidity are well sourced, while the covenant, guarantor, rating, cash-interest and secured-availability inputs that a lender would normally use to size headroom and recovery are absent from the pack.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (December 31, 2025) | 8.16 | 6.06 | x | Total debt is unsecured senior notes principal of 10,455 (revolver undrawn); net debt deducts cash of 2,696; EBITDA is FY2025 adjusted EBITDA of 1,281 (company-defined, after secured-financing interest, before bond interest). Earnings hold only the fourth quarter of Mr. Cooper while debt holds the assumed notes, so leverage is overstated. Secured financing of 17,936 excluded. |
| Q1 2026 (LTM to March 31, 2026) | 5.65 | 4.20 | x | Total debt 10,455; cash 2,687; LTM adjusted EBITDA 1,850 (FY2025 1,281 plus Q1 2026 738 less Q1 2025 169). The LTM holds Q2 and Q3 2025 before Mr. Cooper, so leverage is overstated. Cash includes buy-down funds and margin cash not quantified. |
| Q2 2026 (LTM to June 30, 2026) | 4.42 | 3.15 | x | Total debt 10,805 after the June 2026 issuance; cash 3,103; LTM adjusted EBITDA 2,443 (1,281 plus 1,504 less 342). The LTM holds Q3 2025 before Mr. Cooper, so leverage is overstated. Quarters sum to 2,444 against 2,443 because of printed rounding. |
| Q3 2026 (LTM to September 30, 2026) | 3.78 | 2.83 | x | Total debt 10,743; cash 2,699; LTM adjusted EBITDA 2,843 (1,281 plus 2,252 less 690). First LTM made only of quarters that include both acquisitions. Company-defined EBITDA; earnings are rate-sensitive and Q4 2026 adjusted revenue is guided below Q3; secured financing of 14,187 excluded; no company-printed ratio exists to compare. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 2.15 | x | FY2025 adjusted EBITDA of 1,281 over cash paid for interest of 596 (10-K page:138). Basis is mixed: adjusted EBITDA is already after secured-financing interest, while cash paid for interest is a single figure not split between funding-facility interest and bond interest, so the ratio understates cover on a bond-only basis. |
| Q1 2026 | Not supplied: cash paid for interest is not printed in the Q1 10-Q | x | Accrual proxy of adjusted EBITDA over bond interest expense is shown in the financials table, not here. |
| Q2 2026 | Not supplied: cash paid for interest is not printed in the Q2 10-Q | x | Accrual proxy of adjusted EBITDA over bond interest expense is shown in the financials table, not here. |
| Q3 2026 | Not supplied: cash paid for interest is not printed in the Q3 10-Q | x | The nine-month cash flow statement ends with non-cash investing items and prints no interest paid (Q3 10-Q page:7 to page:8). Accrual proxy for the LTM is 4.94x (see financials table and Calculations). |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| December 31, 2025 | 2,696 | 2,300 | US$m | Cash and cash equivalents (10-K page:135); undrawn is the revolving credit facility, committed 2,300 and outstanding nil (10-K page:179). Company-stated total liquidity of 10.1 billion also counts 0.1 billion of corporate cash used to self-fund loans and 5.0 billion of undrawn MSR lines (10-K page:121); secured availability is not derivable. |
| March 31, 2026 | 2,687 | 2,300 | US$m | Cash (Q1 10-Q page:3); revolver 2,300 undrawn (Q1 10-Q page:27). Company-stated total 9.4 billion includes 4.4 billion of undrawn available MSR and advance lines (Q1 10-Q page:59), not tied to the note. |
| June 30, 2026 | 3,103 | 2,300 | US$m | Cash (Q2 10-Q page:4); revolver 2,300 undrawn at quarter end and later increased to 2,500 and extended (Q2 10-Q page:28). Company-stated total 11.2 billion includes 5.8 billion of secured availability (Q2 10-Q page:64), not tied to the note. |
| September 30, 2026 | 2,699 | 2,500 | US$m | Cash (Q3 10-Q page:4); revolver committed 2,500, outstanding nil, maturing July 16, 2029 (Q3 10-Q page:30). Company-stated total 11.4 billion includes 6.2 billion of undrawn available MSR and advance lines (Q3 10-Q page:67), which cannot be reproduced from the note. Cash includes buy-down funds and margin cash held for counterparties, which are not quantified. Restricted cash of 240 is excluded (Q3 10-Q page:11). |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 (remainder) | 0 | US$m | Unsecured senior notes principal at September 30, 2026 by stated maturity year (Q3 10-Q page:30). The 2.875% notes due October 15, 2026 were redeemed in the period, so nothing remains. Secured financing is excluded; see the secured maturity table below. |
| 2027 | 503 | US$m | The 0.500% convertible senior notes due April 1, 2027 (Q3 10-Q page:30), convertible to cash, shares or a combination at the company's election, with a free conversion date of January 1, 2027 (10-K page:181). |
| 2028 | 0 | US$m | The 5.250% notes due January 15, 2028 were redeemed in the period (Q3 10-Q page:30 to page:31). The 2,500 revolver matures in 2029, not 2028. |
| 2029 | 1,500 | US$m | 750 of 3.625% notes due March 1, 2029 plus 12 and 738 of 6.500% notes due August 1, 2029. The undrawn revolver matures July 16, 2029. |
| 2030 | 2,076 | US$m | 2,000 of 6.125% notes due August 1, 2030 plus 76 of 5.125% notes due December 15, 2030. |
| 2031 | 2,214 | US$m | 1,250 of 3.875% notes due March 1, 2031, 900 of 6.125% notes due August 1, 2031 and 64 of 5.750% notes due November 15, 2031. |
| 2032 | 1,000 | US$m | 45 plus 955 of 7.125% notes due February 1, 2032. |
| 2033 | 2,850 | US$m | 2,000 of 6.375% notes due August 1, 2033 and 850 of 4.000% notes due October 15, 2033. |
| 2034 | 600 | US$m | 6.500% notes due June 15, 2034, issued in June 2026. Rows sum to 10,743, the printed principal total; premium of 39 and issuance costs of 66 are excluded. |

### Financials and credit metrics

| Metric | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | Nine months 2026 | Nine months 2025 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenue, net | 6,695 | 2,941 | 2,784 | 3,284 | 9,009 | 4,248 | GAAP. FY2025 is on the pre-2026 captions (net of funding-facility interest of 376); 2026 and nine months 2025 are on the 2026 captions. Not comparable across that line (10-K page:136; Q1 10-Q page:4; Q2 10-Q page:5; Q3 10-Q page:5) |
| Adjusted revenue | 6,859 | 2,822 | 2,761 | 2,574 | 8,157 | 4,665 | Total revenue less change in MSR fair value from valuation assumptions (net of hedges); same caption caveat for FY2025 (10-K page:101; Q1 release page:1; Q2 release page:1; Q3 release page:1) |
| Total expenses | 6,909 | 2,541 | 2,503 | 2,326 | 7,370 | 4,631 | GAAP; same caption caveat for FY2025 (10-K page:136; Q3 10-Q page:5) |
| Net income (loss) | (234) | 297 | 229 | 709 | 1,235 | (302) | GAAP; not affected by the interest reclassification (Q3 10-Q page:10) |
| Adjusted net income | 628 | 422 | 441 | 419 | 1,282 | 313 | Company non-GAAP (10-K page:102; Q3 release page:7) |
| Adjusted EBITDA | 1,281 | 738 | 766 | 748 | 2,252 | 690 | Company non-GAAP; after secured-financing interest, before bond interest (10-K page:104; Q1 release page:8; Q2 release page:9; Q3 release page:8) |
| Bond interest expense (add-back) | 335 | 139 | 142 | 154 | 435 | 195 | Interest on the senior notes; FY2025 caption is interest and amortization on non-funding debt (10-K page:103; Q3 release page:8) |
| Interest expense, income statement | Not supplied: FY2025 is not printed on the 2026 caption | 349 | 374 | 359 | 1,082 | 499 | 2026 caption includes funding-facility interest and bond interest. The 10-K prints non-funding debt interest of 438 and funding interest of 376 netted in revenue (Q3 10-Q page:5; 10-K page:136) |
| Depreciation and amortization | 290 | 146 | 145 | 147 | 438 | 133 | GAAP, includes amortization of acquired intangibles (10-K page:136; Q3 10-Q page:5) |
| Net cash from operating activities | (3,927) | 1,857 | (1,212) | 1,905 | 2,550 | (2,697) | Dominated by loans held for sale flows; Q2 and Q3 are derived from year-to-date amounts of 645 and 2,550 (10-K page:138; Q1 10-Q page:6; Q2 10-Q page:6; Q3 10-Q page:7) |
| Closed loan origination volume (US$bn) | 130.4 | 44.7 | 49.1 | 43.6 | 137.4 | 83.1 | Operating KPI (10-K page:105; Q1 release page:1; Q2 release page:2; Q3 release page:2; Q3 10-Q page:50) |
| Gain on sale margin (percent) | 2.83 | 2.74 | 2.48 | 2.54 | 2.59 | 2.83 | Total gain on sale margin as printed; the correspondent channel appears only after the Mr. Cooper acquisition (10-K page:105; Q1 release page:1; Q2 release page:2; Q3 10-Q page:57) |
| Cash and cash equivalents | 2,696 | 2,687 | 3,103 | 2,699 | Not applicable: balance at the Q3 2026 date | Not applicable: balance sheet instant not in this table | Period-end; excludes restricted cash (10-K page:135; Q1 10-Q page:3; Q2 10-Q page:4; Q3 10-Q page:4) |
| Secured financing | 17,936 | 15,882 | 16,639 | 14,187 | Not applicable: balance at the Q3 2026 date | Not applicable: balance sheet instant not in this table | Carrying; FY2025 is funding facilities 14,155 plus MSR and advance facilities 3,781 (10-K page:135; Q1 10-Q page:4; Q2 10-Q page:4; Q3 10-Q page:4) |
| Unsecured financing, net | 10,423 | 10,430 | 10,772 | 10,716 | Not applicable: balance at the Q3 2026 date | Not applicable: balance sheet instant not in this table | Carrying value of senior notes, net of premium and issuance costs; revolver undrawn (Q3 10-Q page:30) |
| Senior notes principal | 10,455 | 10,455 | 10,805 | 10,743 | Not applicable: balance at the Q3 2026 date | Not applicable: balance sheet instant not in this table | Principal before premium and issuance costs (10-K page:180; Q1 10-Q page:27; Q2 10-Q page:29; Q3 10-Q page:30) |
| Total equity | 22,898 | 23,230 | 23,546 | 24,311 | Not applicable: balance at the Q3 2026 date | Not applicable: balance sheet instant not in this table | Includes all-stock acquisition consideration (10-K page:136; Q1 10-Q page:4; Q2 10-Q page:4; Q3 10-Q page:4) |
| Equity less goodwill and intangibles | 10,063 | 10,510 | 10,940 | 11,745 | Not applicable: balance at the Q3 2026 date | Not applicable: balance sheet instant not in this table | Derived: not the covenant tangible net worth, whose definition and level are not printed |
| Mortgage servicing rights at fair value | 19,442 | 19,377 | 18,905 | 20,257 | Not applicable: balance at the Q3 2026 date | Not applicable: balance sheet instant not in this table | Fair value; sensitive to rates and prepayment assumptions (10-K page:135; Q1 10-Q page:4; Q2 10-Q page:4; Q3 10-Q page:25) |
| Total debt / LTM adjusted EBITDA (x) | 8.16 | 5.65 | 4.42 | 3.78 | Not applicable: LTM measure | Not applicable: LTM measure | Unsecured senior notes principal over LTM adjusted EBITDA; derived (Calculations) |
| Net debt / LTM adjusted EBITDA (x) | 6.06 | 4.20 | 3.15 | 2.83 | Not applicable: LTM measure | Not applicable: LTM measure | Adds cash deduction; derived (Calculations) |
| LTM adjusted EBITDA / LTM bond interest, accrual (x) | 3.82 | 4.24 | 4.59 | 4.94 | Not applicable: LTM measure | Not applicable: LTM measure | Accrual proxy, not cash interest; derived (Calculations) |
| All balance sheet financing / LTM adjusted EBITDA (x) | 22.14 | 14.22 | 11.22 | 8.76 | Not applicable: LTM measure | Not applicable: LTM measure | Secured plus unsecured carrying over LTM adjusted EBITDA; not like-for-like because adjusted EBITDA is already after secured-financing interest and secured debt is collateralized by loans and MSRs; reference only (Calculations) |

### Debt stack at September 30, 2026

| Class | Line amount | Committed | Outstanding | Terms and locator |
| --- | --- | --- | --- | --- |
| Revolving credit facility, unsecured | 2,500 | 2,500 | 0 | Matures July 16, 2029; borrower Rocket Companies, Inc. with guarantors, per the exhibit listing (Q3 10-Q page:30, page:71) |
| Senior notes, unsecured, 14 lines | Not applicable: notes have principal only | Not applicable: notes have principal only | 10,743 | Rates 0.500% to 7.125%; weighted average interest rate 5.43% at September 30, 2026 against 5.03% at December 31, 2025; covenants restrict mergers, asset sales and liens; fair value 10,258 against carrying 10,716 (Q3 10-Q page:23, page:30 to page:31) |
| Mortgage loan funding, 20 lines (two terminated) | 27,750 | 2,250 | 12,042 | Master repurchase agreements and two evergreen early funding facilities; collateral is mortgage loans held for sale (Q3 10-Q page:27 to page:28) |
| MSR and advance facilities, 13 lines (two terminated) | 8,825 | 4,475 | 1,801 | MSR lines and servicing advance facilities (Q3 10-Q page:28) |
| Personal loan funding, 5 lines | 950 | 675 | 344 | Collateral is personal loans held for sale; one line is in its amortization period (Q3 10-Q page:28 to page:29) |
| Total secured financing | 37,525 | 7,400 | 14,187 | Spread over base rate from 0.75% to 3.25% in the nine months (Q3 10-Q page:29) |

### Secured financing by stated line maturity at September 30, 2026

| Stated maturity of line | Outstanding balance | Lines | Locator and limitation |
| --- | --- | --- | --- |
| 2026 | 9 | 5 | Lines dated October 22, November 18, November 27, December 21 and December 23, 2026; the October 22, 2026 line matured after the quarter (Q3 10-Q page:28 to page:29) |
| 2027 | 10,295 | 19 | Lines dated within 2027; after the quarter, three lines were extended, one of them (294 outstanding) from September 3, 2027 to September 1, 2028 and two within 2027 (Q3 10-Q page:28 to page:29) |
| 2028 | 3,462 | 8 | Lines dated within 2028 (Q3 10-Q page:28 to page:29) |
| Evergreen, no stated maturity | 421 | 2 | Two early funding facilities, terminable by either party on notice, one reviewed every 90 days (Q3 10-Q page:28 to page:29) |
| Total | 14,187 | 34 | Foots to Total Secured Financing; four terminated lines show no balance (Q3 10-Q page:29) |

### Liquidity, covenants and regulatory requirements

- Company-stated total liquidity: 10.1 billion at December 31, 2025, 9.4 billion at March 31, 2026, 11.2 billion at June 30, 2026 and 11.4 billion at September 30, 2026 (10-K page:121; Q1 10-Q page:59; Q2 10-Q page:64; Q3 10-Q page:67). The figures rose from 9.4 billion to 11.4 billion over the three 2026 quarters. The December 2025 figure also counts 0.1 billion of corporate cash used to self-fund loans, which later figures do not list.
- Cash is not all free. Buy-down funds sit in cash and can be withdrawn unless a margin call has been made or a default has occurred (Q3 10-Q page:27), and margin cash held for counterparties is included in cash with an offsetting liability (Q3 10-Q page:67). Neither amount is printed. Restricted cash of 240 is outside cash (Q3 10-Q page:11).
- Covenant types: minimum tangible net worth, minimum liquidity, maximum total debt or liabilities to net worth, pretax net income requirements and other customary covenants, with cross default or cross acceleration provisions in most facilities, and compliance stated at September 30, 2026 and December 31, 2025 (Q3 10-Q page:27). Litigation judgment thresholds are also a covenant type (10-K page:47). A money judgment above specified thresholds that is not paid, bonded or stayed could be a default under loan funding facilities (Q3 10-Q page:41). Levels, step-downs and headroom: Not supplied; the agreements are not in the pack.
- Regulatory minimums at September 30, 2026: the most restrictive require net worth of approximately 3,500, liquidity of approximately 1,500 and a 6% capital ratio, with compliance stated (Q3 10-Q page:42). These apply to Rocket Mortgage (Q3 10-Q page:42). Entity-level net worth and liquidity are not printed, so headroom against them is Not calculable; consolidated equity of 24,311 is not that measure.
- Fair value of the senior notes at September 30, 2026 was 10,258 against carrying value of 10,716, calculated from observable bond prices (Q3 10-Q page:23). At December 31, 2025 fair value was 10,502 against carrying value of 10,423. Fair value fell below carrying value over the nine months while it had been above it at year end.

### Earnings quality and definition review

- Adjusted EBITDA is net income before bond interest expense, income taxes, depreciation and amortization, share-based compensation, the change in MSR fair value from valuation assumptions (net of hedges), acquisition-related expenses, amortization of acquired intangibles, litigation accrual and other adjustments (Q3 release page:10). It includes interest on secured financing, which the company treats as a cost driven by origination volume, and excludes bond interest because it is a function of capital structure (Q3 release page:10). The Q3 10-Q states that adjusted EBITDA does not reflect interest expense or the cash needed to service debt (Q3 10-Q page:53).
- Adjustments in the nine months 2026: share-based compensation 262, MSR valuation change (852) (a gain removed), acquisition-related expenses 291, amortization of acquired intangibles 338, litigation accrual 28 and other 11 (Q3 release page:8). Acquisition-related expenses of 291 recur across 2025 and 2026 (158 in nine months 2025), so the add-back is not a one-quarter item.
- GAAP versus adjusted: nine months 2026 GAAP net income of 1,235 against adjusted EBITDA of 2,252. The adjusted figure removes a valuation gain on MSRs of 852 and adds back bond interest of 435, intangible amortization of 338 and acquisition costs of 291 (Q3 release page:8).
- Fair value exposure: MSRs of 20,257 at fair value are the largest asset line on the balance sheet (Q3 10-Q page:4), and change in fair value of MSRs, net was a charge of 945 in the nine months 2026 against 1,128 in nine months 2025 (Q3 10-Q page:5). Sensitivity to rates and prepayment assumptions is disclosed in the fair value note (Q3 10-Q page:25 to page:26).
- Servicing credit quality: delinquent loans (60-plus days past due) were 1.52% of the servicing portfolio at September 30, 2026 and 1.50% at December 31, 2025 (Q3 10-Q page:25).
- Cash flow: operating cash flow is dominated by loans held for sale. Nine months 2026 disbursements of mortgage loans held for sale were (136,882) and proceeds 139,626 (Q3 10-Q page:7). Net proceeds from sales of MSRs were 1,750 in the nine months 2026 against 315 in nine months 2025 (Q3 10-Q page:7), so investing inflows from MSR sales supported liquidity. Senior note borrowings were 1,500 and repayments (1,212) in the nine months 2026 (Q3 10-Q page:7). Free cash flow is Not calculable on a meaningful basis for an originator that funds loans through operating cash flow.

### Claims outside funded debt

- Operating leases: total lease liabilities of 334 at December 31, 2025, weighted average term 4.4 years (10-K page:184); not updated in the Q3 10-Q. Related party lease expense was 56 in the nine months 2026 (Q3 10-Q page:31). Lease liabilities are outside the debt figures used here.
- Purchase commitments: 914 in aggregate at December 31, 2025, primarily over 2027 through 2030 (10-K page:122). Outside debt.
- Tax receivable agreement: 90% of realized cash tax savings payable to RHI II, LLC and Mr. Gilbert; the liability was 590 at December 31, 2025 (10-K page:191). The Q3 10-Q does not print the liability amount (Q3 10-Q page:33). Outside debt.
- Legal reserves: 216 at September 30, 2026 against 74 at December 31, 2025 (Q3 10-Q page:41). A new trial verdict of 175 in damages against Rocket Close was returned on March 6, 2026 and judgment has not been entered; the plaintiff filed Chapter 11 on September 22, 2026 (Q3 10-Q page:38). The Mr. Cooper data breach class action is in class certification briefing (Q3 10-Q page:40). Acquisition accounting added 100 of litigation and regulatory accruals in the third quarter of 2026 (Q3 10-Q page:18). Whether the 175 verdict is within the 216 reserve is not stated.
- Investor reserves for representations and warranties: 112 at September 30, 2026 (Q3 10-Q page:36). The maximum exposure is the outstanding principal and premium on all loans ever sold less listed exclusions, and is not quantified.
- Non-recourse MSR-related liabilities: 325 at September 30, 2026 (Q3 10-Q page:25). Loans subject to repurchase right from Ginnie Mae of 5,476 appear on both sides of the balance sheet (Q3 10-Q page:4).
- Asset-backed financing entities: holders of debt issued by these entities have limited to no recourse to the company (Q3 10-Q page:15).

### Perimeter, comparability and presentation

- Acquisitions: Redfin from July 1, 2025 (consideration 1,742) and Mr. Cooper from October 1, 2025 (consideration 16,973) (Q3 10-Q page:16 to page:17). Nine months 2025 comparatives hold one quarter of Redfin and no Mr. Cooper. Year-on-year growth in the nine months, such as adjusted EBITDA of 2,252 against 690, therefore mixes organic change with acquired earnings. Unaudited pro forma revenue and net income for the third quarter and nine months of 2025 are printed (Q3 10-Q page:19) but no pro forma EBITDA.
- Interest captions: the 2026 income statement includes funding-facility interest in Interest expense, whereas FY2025 netted it against Interest income. For nine months 2025 the reclassification moved 246 of funding interest, 386 of deposit income and 21 of other interest (Q3 10-Q page:10). The company states that net income is unaffected; adjusted EBITDA includes secured-financing interest under its definition either way, so it should not move, but the company does not say so. Revenue, expenses and interest expense are not comparable between FY2025 as printed in the 10-K and 2026, and discrete fourth quarter 2025 revenue cannot be derived from FY2025 less nine months 2025.
- Segments: one reportable segment, Mortgage, from Q2 2026 with prior periods recast; the 10-K and Q1 10-Q use Direct to Consumer and Partner Network (Q3 10-Q page:42; 10-K page:206). Mortgage segment contribution margin was 3,572 in nine months 2026 against 1,479 in nine months 2025 (Q3 release page:4). No fiscal 2025 segment figures on the new basis are printed.
- Derived fourth quarter 2025: adjusted EBITDA of 591 (FY2025 1,281 less nine months 2025 690) and net income of 68 (FY2025 loss of 234 less nine months 2025 loss of 302). These are derived, rely on FY2025 as printed and the nine-month 2025 comparative as recast, and rest on net income being unaffected by the interest reclassification (Q3 10-Q page:10), and on adjusted EBITDA not moving, which the company does not state.

## Calculations

Amounts are USD millions unless stated. Ratios are rounded to two decimals; the rounded figures are the ones used in the chart tables.

| Calculation | Inputs (locator) | Result |
| --- | --- | --- |
| LTM adjusted EBITDA to December 31, 2025 | FY2025 1,281 (10-K page:104) | 1,281 |
| LTM adjusted EBITDA to March 31, 2026 | 1,281 + 738 (Q1 release page:8) - 169 (Q1 release page:8) | 1,850 |
| LTM adjusted EBITDA to June 30, 2026 | 1,281 + 1,504 - 342 (Q2 release page:9) | 2,443 (quarter sum 2,444; printed rounding of 1) |
| LTM adjusted EBITDA to September 30, 2026 | 1,281 + 2,252 - 690 (Q3 release page:8) | 2,843 |
| Derived Q4 2025 adjusted EBITDA | 1,281 - 690 | 591 |
| Net debt, December 31, 2025 | Senior notes principal 10,455 (10-K page:180) less cash 2,696 (10-K page:135) | 7,759 |
| Net debt, March 31, 2026 | 10,455 (Q1 10-Q page:27) less 2,687 (Q1 10-Q page:3) | 7,768 |
| Net debt, June 30, 2026 | 10,805 (Q2 10-Q page:29) less 3,103 (Q2 10-Q page:4) | 7,702 |
| Net debt, September 30, 2026 | 10,743 (Q3 10-Q page:30) less 2,699 (Q3 10-Q page:4) | 8,044 |
| Total debt / LTM EBITDA | 10,455 / 1,281; 10,455 / 1,850; 10,805 / 2,443; 10,743 / 2,843 | 8.16x; 5.65x; 4.42x; 3.78x |
| Net debt / LTM EBITDA | 7,759 / 1,281; 7,768 / 1,850; 7,702 / 2,443; 8,044 / 2,843 | 6.06x; 4.20x; 3.15x; 2.83x |
| LTM bond interest to September 30, 2026 | 335 (10-K page:103) + 435 - 195 (Q3 release page:8) | 575 |
| LTM bond interest to March 31, 2026 | 335 + 139 - 38 (Q1 release page:8) | 436 |
| LTM bond interest to June 30, 2026 | 335 + 281 - 84 (Q2 release page:9) | 532 |
| Accrual bond interest cover | 1,281 / 335; 1,850 / 436; 2,443 / 532; 2,843 / 575 | 3.82x; 4.24x; 4.59x; 4.94x |
| FY2025 EBITDA / cash interest | 1,281 / 596 (10-K page:138) | 2.15x, mixed basis |
| All balance sheet financing | Secured 14,187 + unsecured net 10,716 (Q3 10-Q page:4) | 24,903; over LTM EBITDA 2,843 = 8.76x |
| All balance sheet financing, other dates | 17,936 + 10,423 = 28,359 over 1,281; 15,882 + 10,430 = 26,312 over 1,850; 16,639 + 10,772 = 27,411 over 2,443 | 22.14x; 14.22x; 11.22x |
| Equity less goodwill and intangibles | Dec 2025: 22,898 - 10,611 - 2,224; Mar 2026: 23,230 - 10,611 - 2,109; Jun 2026: 23,546 - 10,611 - 1,995; Sep 2026: 24,311 - 10,686 - 1,880 | 10,063; 10,510; 10,940; 11,745 |
| Senior notes foot, September 30, 2026 | 503 + 750 + 12 + 738 + 2,000 + 76 + 1,250 + 900 + 64 + 45 + 955 + 2,000 + 850 + 600 (Q3 10-Q page:30) | 10,743 |
| Maturity rows foot | 0 + 503 + 0 + 1,500 + 2,076 + 2,214 + 1,000 + 2,850 + 600 | 10,743 |
| Carrying value | 10,743 + 39 - 66 | 10,716 |
| Secured foots | 12,042 + 1,801 + 344 (Q3 10-Q page:28 to page:29) | 14,187 |
| Secured by maturity year foots | 9 + 10,295 + 3,462 + 421 | 14,187 |
| Committed secured against outstanding | Committed 7,400 and outstanding 14,187 (Q3 10-Q page:29) | Outstanding exceeds committed by 6,787 |
| Undrawn available MSR and advance lines, attempted tie | Line 8,825 less outstanding 1,801; committed 4,475 less outstanding 1,801 (Q3 10-Q page:28) | 7,024 and 2,674; the printed 6.2 billion matches neither |
| Liquidity as stated | 2.7 + 2.5 + 6.2 billion (Q3 10-Q page:67) | 11.4 billion |
| Quarterly operating cash flow | Q2: 645 - 1,857; Q3: 2,550 - 645 (Q2 10-Q page:6; Q3 10-Q page:7) | (1,212); 1,905 |
| Bond interest quarters foot | 139 + 142 + 154 | 435 |


## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Covenant levels, step-downs and the issuer's reported covenant figures are Not supplied; only covenant types and compliance statements are printed (Q3 10-Q page:27; 10-K page:121). Headroom is Not calculable. | Medium | CP-2, CP-5 | Obtain the revolving credit agreement and key repurchase agreements; until then cite compliance statements and regulatory minimums only. |
| Cash paid for interest is Not supplied for Q1, Q2 and Q3 2026 and the nine months; FY2025 is 596 in a single figure not split between funding and bond interest (10-K page:138). The cash interest cover row is therefore filled for FY2025 only, on a mixed basis. | Medium | CP-2, CP-5 | Use the accrual bond interest cover as a labelled proxy; request cash interest paid by type from the company. |
| Named guarantors, the issuer of each senior note line and the assets pledged to each secured facility are Not supplied (Q3 10-Q page:30; 10-K page:177). Asset coverage and structural ranking of the unsecured notes are Not calculable. | Medium | CP-1A, CP-2 | Obtain the indentures, guarantor exhibit and collateral detail before any recovery or ranking statement. |
| The basis of the 6.2 billion undrawn available MSR and advance lines is not stated and cannot be reproduced from the secured financing table; buy-down funds and margin cash inside the 2,699 of cash are not quantified. | Medium | CP-2, CP-5 | Present stated liquidity as attributed management data; request the availability calculation and the cash composition. |
| Revenue, expense and interest captions for FY2025 are on the pre-2026 basis; discrete fourth quarter 2025 revenue and expenses cannot be derived; FY2025 segment results on the Mortgage basis are Not supplied. | Medium | CP-2, CP-5 | Use net income and adjusted EBITDA for cross-period work; restrict revenue and segment comparisons to 2025 quarters recast and 2026 quarters. |
| Adjusted EBITDA is company-defined. Whether FY2025 adjusted EBITDA of 1,281 is on exactly the same basis as the 2026 reconciliations is not stated; no pro forma EBITDA exists for the acquisitions. LTM figures to March and June 2026 hold quarters before Mr. Cooper. | Medium | CP-2, CP-5 | Treat the September 30, 2026 LTM ratios as the primary read; flag earlier ratios as overstated by perimeter. |
| Earnings are rate-sensitive and the fourth quarter 2026 adjusted revenue outlook (2.1 billion to 2.3 billion) is below the third quarter; the LTM ratios are not forward run-rates. No forecast is supplied. | Medium | CP-2 | Add a forward sensitivity in a later module if the committee needs one; no inputs are supplied here. |
| The tax receivable agreement liability at September 30, 2026, lease liabilities and purchase commitments after December 31, 2025 are Not supplied (10-K page:184, page:122, page:191; Q3 10-Q page:33). | Low | CP-2 | Use December 31, 2025 values labelled as stale, or obtain the current amounts. |
| Whether the 175 HouseCanary verdict is within the 216 legal reserve is not stated, and the investor representation and warranty exposure is not quantified (Q3 10-Q page:36, page:38, page:41). | Medium | CP-1A, CP-2 | Track the judgment entry and the bankruptcy stay; ask for reserve allocation. |
| Entity-level regulatory net worth and liquidity for Rocket Mortgage are Not supplied; the equity less goodwill and intangibles row is a consolidated proxy only (Q3 10-Q page:42). | Low | CP-2 | Request entity-level figures if headroom is needed. |
| No source is dated after October 30, 2026 although the cutoff is 2026-11-05; post-quarter facility extensions and a matured line are known only from table footnotes (Q3 10-Q page:29). | Medium | CP-1A, CP-2, CP-5 | Obtain the filing list for October 30 to November 5, 2026. |
| No credit ratings, no tranche-level bond prices (only aggregate fair value of senior notes, 10,258) and no market data are supplied; context ratings and quotes are blank, not zero. | Medium | CP-2 | Obtain agency publications and bond quotes dated on or before 2026-11-05. |
| Free cash flow and cash conversion are Not calculable on a meaningful basis because loans held for sale flow through operating cash flow (Q3 10-Q page:7). | Low | CP-2 | Use adjusted EBITDA, interest cover proxies and liquidity instead. |

## Next module

Proceed to CP-1A (business and transaction context). It should carry from this module: one unsecured corporate layer of senior notes with principal of 10,743 and an undrawn 2,500 revolver, a separate secured financing layer of 14,187 that is mostly uncommitted, the Redfin and Mr. Cooper perimeter dates, the segment recast, the legal matters and reserves, the control by Mr. Gilbert, and the limitations above (no guarantor names, covenant levels, ratings or cash interest). CP-2 and CP-5 follow. CP-2 should use the September 30, 2026 LTM ratios of 3.78x gross and 2.83x net as the leverage anchor, label the earlier ratios as overstated by perimeter, and treat stated liquidity of 11.4 billion as management data with only the cash and revolver tied to the filings.
