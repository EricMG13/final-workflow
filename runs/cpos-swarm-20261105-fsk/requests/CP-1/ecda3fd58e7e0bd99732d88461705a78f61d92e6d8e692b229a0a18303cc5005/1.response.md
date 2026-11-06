## Request

Module CP-1 (canonical data foundation) for FS KKR Capital Corp (issuer id fsk, NYSE: FSK), credit_snapshot pathway, as of 2026-11-05 (cutoff 2026-11-05). Reporting currency USD, amounts in USD millions as the filings print them unless a cell says otherwise. Current period Q3 2026 (quarter ended 2026-09-30); prior period FY2025 (year ended 2025-12-31). The perimeter is the registrant's own consolidated statements, which include its wholly-owned special-purpose financing subsidiaries; the unconsolidated joint venture Credit Opportunities Partners JV, LLC is outside it. The issuer is a business development company, so EBITDA, capex and segment figures do not exist; the metric set is investment income, net investment income, net assets, debt, asset coverage and liquidity. Periods are labelled Q1 2026, Q2 2026, Q3 2026, nine months 2026 (cumulative to 2026-09-30) and FY2025; point-in-time balances carry their date.

## Sources

### Issuer sources relied on

`page:N` is the extraction chunk of the pinned file, not the printed page.

| Source (exact name) | sha256 (pinned file) | What it supplies |
| --- | --- | --- |
| 10-K_2025-12-31_fsk-20251231.htm.jsonl | be99ced2da7392c013fd879201dbe6646929f936ebb77ecc5d0444caab275d72 | FY2025 audited statements, Note 9 financing arrangements and covenant descriptions, liquidity and commitments |
| 10-Q_2026-03-31_fsk-20260331.htm.jsonl | c1848df2f7f8ae50873fb96d813147e929f68a7d9fd036caac9a50ef11030183 | Q1 2026 unaudited statements, Note 9, subsequent event of 2026-05-08 (credit agreement amendment) |
| 10-Q_2026-06-30_fsk-20260630.htm.jsonl | 5179e6b96937e772046c13be81daafa87748d7253056dcfc343a0e0d70e10e37 | Q2 2026 and six months statements, Note 9, amendment text, 7.500% Notes due 2031 |
| 10-Q_2026-09-30_fsk-20260930.htm.jsonl | 9fd3638380d8a2268f17361ef6fc29d66f22c0391f57eb0cb6b68acb61776e4e | Q3 2026 and nine months statements, Note 9, liquidity, asset coverage, joint venture, subsequent events |
| EX-99.1_2026-05-10_tm2614112d1_ex99-1.htm.jsonl | 7e0c1f798df446f884320f02fed73d08f87b229f9d7b33f04d81f5473d6602e3 | Q1 2026 release (text dated May 11, 2026): strategic actions, net debt reconciliation |
| EX-99.1_2026-08-06_tm2622260d1_ex99-1.htm.jsonl | 24d1ea2d36b2f64d8b77676a71ecd16bea780f8870e6b7238b28ee023281ffd9 | Q2 2026 release: leverage, liquidity, debt principal reconciliation |
| EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | 9570b8d0d4b7076e0359f3122075bc5e24c85c74b9723e31fa99d14ae3f3839b | Q3 2026 release: leverage, liquidity, debt principal reconciliation, subsequent events |

Run settings (dates, currency and scope only, not issuer evidence): context sha256 378a6255aee6dac53a389f9bf4cbce2419e6f8121d5d4932c50d57d1600eb13a.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 6fa09daba39205fb415654f095188714149fb623a5ac6f52a41f3d1dba8bb321 | Readiness, entity perimeter, definitional cautions; corrected in two places below |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Leverage eased slightly as the portfolio shrank and net assets eroded: principal debt is 6,337 against common equity of 4,999, with asset coverage of 179% on debt versus a 150% minimum and 3,197 of availability. | Medium | No EBITDA exists; covenant definitions and borrowing base values are not supplied, so headroom rests on the reported equity figure and asset coverage ratios only. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Net asset value per share fell from 20.89 to 18.28 over nine months 2026 while debt principal fell from 7,620 to 6,337. | Deleveraging came from asset sales and repayments, not earnings growth; the equity cushion under the debt is thinner. | High |
| The main bank covenant is a minimum shareholders' equity floor, reset on May 8, 2026 to 3,750.0 from about 5,048.6. | Common equity of 4,999 clears the new floor by about 1,249 but is below the old floor, so the reset mattered. | Medium |
| Nine-month net investment income of 366 did not cover common distributions of 373, and the Q3 figure relied on a 12 fee waiver. | Distribution policy competes with debt reduction for cash; the waiver is temporary. | Medium |
| Liquidity of 3,308 (cash 111 plus availability 3,197) compares with 900 of notes maturing in 2027 and unfunded commitments of 1,545.4. | Near-term refinancing looks covered if the borrowing base holds; availability is secured and base-limited. | Medium |
| Unsecured notes of 4,650 sit alongside 1,687 of secured borrowings; five stockholder suits filed since May 2026 carry no loss estimate. | Unsecured creditors rank behind secured lenders (the 7.500% notes say so); the suits are an unquantified contingent claim alleging misstatements on valuations. | Medium |

### Financial base view

The financial base is usable for a credit snapshot, with the issuer-specific metric set stated plainly. FS KKR Capital Corp is a business development company whose statements report investment income, net investment income, net assets and a statutory asset coverage test rather than EBITDA, so the leverage and interest cover chart fields are Not supplied and are replaced by debt to common equity, asset coverage and a net investment income based cover proxy, all labelled as calculations. Over nine months 2026 total investment income fell to 888 from 1,171, net assets fell by 850 to 4,999 as unrealised and realised losses of 766 and distributions of 375 outran net investment income of 366, and debt principal fell to 6,337 from 7,620 through asset sales and repayments. Liquidity at 2026-09-30 is 111 of cash and foreign currency plus 3,197 of borrowings available, subject to borrowing base and other limits. The largest near-term claims are 900 of unsecured notes maturing in January and July 2027, and the main covenant is the revolver's minimum shareholders' equity floor of 3,750.0 after the May 8, 2026 amendment. Limits that matter: the credit agreement's definitions are not supplied, the borrowing base is not printed, and the cash and debt figures appear on several bases that this handoff labels one by one.

### Corrections to the CP-0 handoff

The earlier handoff cannot be edited, so the corrections are stated here and govern downstream use.

- **Covenant levels are partly printed.** CP-0 said numeric financial covenant thresholds other than the 150% asset coverage test are not printed and that "minimum stockholders’ equity" has no level. The sources do print the revolver floor: Amendment No. 1 of May 8, 2026 provides for "a reset of the minimum Shareholders’ Equity floor to $3,750.0 from approximately $5,048.6" and a reduction of total commitments "to approximately $4,051.7 from $4,700.0" (10-Q Q1 2026 page:107; 10-Q Q2 2026 page:108). The 10-K lists the two financial covenants of the revolver: a minimum shareholders' equity measured at each fiscal quarter end and "a 150% asset coverage ratio" (10-K page:273). Still not supplied: the credit agreement's definition of shareholders' equity, the compliance certificate figures, and covenant levels for the Callowhill facility, the CLO notes and the note indentures beyond the asset coverage covenant.
- **Cash basis refinement.** CP-0 said restricted cash was included in earlier net debt and excluded in the latest. The labels did change, but restricted cash was nil at June 30, 2026 (the Q2 cash flow footnote lists only cash of 107 and foreign currency of 2, 10-Q Q2 2026 page:5), so the Q2 and Q3 net debt cash figures (109 and 111) are on the same effective basis. The difference is that 4 of restricted cash sat inside the Q1 figure of 133 (10-Q Q1 2026 page:5) and 61 of restricted cash is outside the Q3 figure of 111 (10-Q Q3 2026 page:2).
- **Guarantors.** CP-0 said no guarantor is named. The 10-K states that the revolver obligations "are guaranteed by certain of the Company’s subsidiaries" and secured "by a first priority security interest in substantially all of the assets of the Company and certain of the Company’s subsidiaries" (10-K page:273); the guarantors are not named.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (2025-12-31) | Not supplied: business development company reports no EBITDA | Not supplied: business development company reports no EBITDA | x | Substitute measures in the Financials table: debt principal to common equity (calculated) and asset coverage (reported). No EBITDA is derived because investment income is not operating earnings. |
| Q1 2026 (2026-03-31) | Not supplied: business development company reports no EBITDA | Not supplied: business development company reports no EBITDA | x | Same basis as FY2025; the release prints debt to equity of 138% and net debt to equity of 131%. |
| Q2 2026 (2026-06-30) | Not supplied: business development company reports no EBITDA | Not supplied: business development company reports no EBITDA | x | Same basis; the release prints debt to equity of 127% and net debt to equity of 122%. |
| Q3 2026 (2026-09-30) | Not supplied: business development company reports no EBITDA | Not supplied: business development company reports no EBITDA | x | Same basis; the release prints debt to equity of 127% and net debt to equity of 125%, with cash of 111 excluding 61 of restricted cash. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 (2025-12-31) | Not supplied: no EBITDA reported | x | Proxy only, not EBITDA cover: net investment income plus interest expense over interest expense is 2.41x (calculated); cash interest paid was 471. |
| Q1 2026 (2026-03-31) | Not supplied: no EBITDA reported | x | Proxy 2.11x (calculated); interest paid in the quarter was 121. |
| Q2 2026 (2026-06-30) | Not supplied: no EBITDA reported | x | Proxy 2.21x (calculated); interest paid in the quarter was 92 (calculated from the six-month and Q1 figures). |
| Q3 2026 (2026-09-30) | Not supplied: no EBITDA reported | x | Proxy 2.28x (calculated); interest paid in the quarter was 100 (calculated); nine months proxy 2.20x. Net investment income is after management and incentive fees and after a 12 incentive fee waiver in Q3. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (2025-12-31) | 208 | 3,268 | US$m | Cash is cash and cash equivalents of 181 plus foreign currency of 27, no restricted cash reported. Availability is the printed amount available under financing arrangements, net of standby letters of credit on the revolver, subject to borrowing base and other limitations. |
| Q1 2026 (2026-03-31) | 129 | 2,602 | US$m | Cash of 124 plus foreign currency of 5, excluding 4 of restricted cash (management prints 133 including it). Availability as printed. |
| Q2 2026 (2026-06-30) | 109 | 3,052 | US$m | Cash of 107 plus foreign currency of 2; no restricted cash reported. Availability as printed. |
| Q3 2026 (2026-09-30) | 111 | 3,197 | US$m | Cash of 102 plus foreign currency of 9, excluding 61 of restricted cash that collateralises derivatives. Availability is Callowhill 63 plus revolver 3,134, the revolver being net of 50 of standby letters of credit. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0 | US$m | Principal outstanding at 2026-09-30 by contractual maturity year from the Note 9 table; no arrangement is listed with a 2026 maturity (the 3.400% Notes due 2026 of 1,000 were outstanding at 2025-12-31 and are gone). |
| 2027 | 900 | US$m | 2.625% Notes due January 15, 2027 (400) and 3.250% Notes due July 15, 2027 (500). |
| 2028 | 750 | US$m | 3.125% Notes due October 12, 2028. |
| 2029 | 1,000 | US$m | 7.875% Notes due January 15, 2029 (400) and 6.875% Notes due August 15, 2029 (600). Revolver availability ends July 16, 2029 per the 10-K, ahead of its 2030 loan maturity. |
| 2030 | 1,644 | US$m | Callowhill facility 337 (June 2, 2030), Senior Secured Revolving Credit Facility 607 (July 16, 2030) and 6.125% Notes due January 15, 2030 (700). |
| 2031 | 1,300 | US$m | 6.125% Notes due January 15, 2031 (400) and 7.500% Notes due August 1, 2031 (900). |
| 2037 | 380 | US$m | CLO-2 notes, scheduled maturity April 15, 2037; legal final, repayment follows collateral cash flows. |
| 2038 | 363 | US$m | CLO-3 notes, scheduled maturity January 15, 2038; same limitation. Total of all rows is 6,337, equal to the release's debt principal; the 150 convertible preferred has no maturity and is excluded. |

### Financials and credit metrics

| Metric (USD millions unless stated) | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | Nine months 2026 | Source and basis |
| --- | --- | --- | --- | --- | --- | --- |
| Total investment income | 1,519 | 304 | 290 | 294 | 888 | 10-K page:165; 10-Q Q1 page:3; 10-Q Q2 page:3; 10-Q Q3 page:3 |
| Interest expense | 464 | 105 | 101 | 99 | 305 | same pages; includes amortisation of financing costs |
| Subordinated income incentive fee waiver | None (waiver starts Q2 2026) | None (waiver starts Q2 2026) | 11 | 12 | 23 | 10-Q Q2 page:3; 10-Q Q3 page:3 |
| Net investment income | 654 | 117 | 122 | 127 | 366 | same pages; after excise taxes where printed |
| Net investment income per share ($) | 2.34 | 0.42 | 0.44 | 0.46 | 1.31 | 10-K page:142; releases page:1; 10-Q Q3 page:138 |
| Total net realized and unrealized gain (loss) | (624) | (558) | (154) | (54) | (766) | statements of operations, pages as above |
| Net increase (decrease) in net assets from operations | 11 | (441) | (34) | 73 | (402) | statements of operations, pages as above |
| Distributions to common stockholders | (784) | (134) | (118) | (121) | (373) | statements of changes in net assets: 10-K page:166; 10-Q Q1 page:4; 10-Q Q2 page:4; 10-Q Q3 page:4 |
| Repurchases of common stock | — (nil as printed) | — (nil as printed) | (4) | (69) | (73) | statements of changes in net assets |
| Net cash from operating activities | 592 | 245 | 776 (calculated) | 404 (calculated) | 1,425 | cash flow statements: 10-K page:167; 10-Q Q1 page:5; 10-Q Q2 page:5 (six months 1,021); 10-Q Q3 page:5 |
| Purchases of investments | (5,107) | (505) | (591) (calculated) | (335) (calculated) | (1,431) | cash flow statements, pages as above |
| Proceeds from sales and repayments of investments | 5,343 | 760 | 1,287 (calculated) | 646 (calculated) | 2,693 | cash flow statements, pages as above |
| Interest paid | 471 | 121 | 92 (calculated) | 100 (calculated) | 313 | cash flow statements, supplemental information |
| Total investments at fair value (period end) | 13,009 | 12,269 | 11,418 | 11,306 | Same as Q3 2026 (balance at 2026-09-30) | balance sheets: 10-K page:164; 10-Q Q1 page:2; 10-Q Q2 page:2; 10-Q Q3 page:2 |
| Total assets (period end) | 13,729 | 12,825 | 11,994 | 11,695 | Same as Q3 2026 (balance at 2026-09-30) | balance sheets, pages as above |
| Debt, carrying value net of financing costs and discount (period end) | 7,634 | 7,271 | 6,471 | 6,231 | Same as Q3 2026 (balance at 2026-09-30) | balance sheets; includes hedge accounting adjustments |
| Debt principal outstanding excluding preferred (period end) | 7,620 | 7,290 | 6,491 | 6,337 | Same as Q3 2026 (balance at 2026-09-30) | Note 9 totals: 10-K page:259; 10-Q Q1 page:93; 10-Q Q2 page:102 (6,641 less 150 preferred; release page:10 prints 6,491); 10-Q Q3 page:110 (6,487 less 150; release page:9 prints 6,337) |
| Convertible preferred stock (period end) | None issued | None issued | 150 | 150 | Same as Q3 2026 (balance at 2026-09-30) | balance sheets; temporary equity, counted in asset coverage |
| Common stockholders' equity (period end) | 5,849 | 5,274 | 5,118 | 4,999 | Same as Q3 2026 (balance at 2026-09-30) | balance sheets |
| Net asset value per share ($, period end) | 20.89 | 18.83 | 18.30 | 18.28 | Same as Q3 2026 (balance at 2026-09-30) | balance sheets |
| Debt to equity per release (%) | Not supplied: no Q4 2025 release in the pack (calculated 130.3) | 138 | 127 | 127 | Same as Q3 2026 (balance at 2026-09-30) | Q2 release page:1 prints 138 for 2026-03-31 and 127 for 2026-06-30; Q3 release page:1 prints 127; the Q1 release prints the net ratio only |
| Net debt to equity per release (%) | 122 | 131 | 122 | 125 | Same as Q3 2026 (balance at 2026-09-30) | releases: Q1 page:1, Q2 page:1, Q3 page:1; cash basis noted in the definition review |
| Asset coverage (150% minimum) | 177% (single figure) | 172% (single figure) | 179% on debt; 177% on stock | 179% on debt; 177% on stock | Same as Q3 2026 (balance at 2026-09-30) | 10-K page:259; 10-Q Q1 page:93; 10-Q Q2 page:101; 10-Q Q3 page:109 |
| Cash, cash equivalents and foreign currency excluding restricted cash (period end) | 208 | 129 | 109 | 111 | Same as Q3 2026 (balance at 2026-09-30) | balance sheets, summed (calculated) |
| Restricted cash (period end) | None reported | 4 | None reported | 61 | Same as Q3 2026 (balance at 2026-09-30) | balance sheets and cash flow footnotes: 10-Q Q1 page:5; 10-Q Q2 page:5; 10-Q Q3 page:5 |
| Borrowings available under financing arrangements (period end) | 3,268 | 2,602 | 3,052 | 3,197 | Same as Q3 2026 (balance at 2026-09-30) | liquidity discussion: 10-K page:144; 10-Q Q1 page:128; 10-Q Q2 page:135; 10-Q Q3 page:141 |
| Unfunded debt investment commitments (period end) | 1,447.4 | 1,326.0 | 1,110.5 | 1,041.1 | Same as Q3 2026 (balance at 2026-09-30) | same liquidity pages |
| Unfunded equity and other commitments (period end) | 87.5 | 87.2 | 70.7 | 70.3 | Same as Q3 2026 (balance at 2026-09-30) | same liquidity pages |
| Unfunded commitments to the joint venture (period end) | 245.0 | 434.0 | 434.0 | 434.0 | Same as Q3 2026 (balance at 2026-09-30) | same liquidity pages |
| Investments on non-accrual, share of fair value (%) | 3.4 | 4.2 | 3.8 | 3.4 | Same as Q3 2026 (balance at 2026-09-30) | 10-K page:134; Q1 release page:4; Q2 release page:3; Q3 release page:3 |
| Investments on non-accrual, share of amortised cost (%) | 5.5 | 8.1 | 7.1 | 6.4 | Same as Q3 2026 (balance at 2026-09-30) | Q1 release page:4 (Dec 2025 and Mar 2026); Q2 release page:3; Q3 release page:3 |
| Weighted average yield on accruing debt investments (%) | 10.1 | 9.9 | 9.8 | 10.0 | Same as Q3 2026 (balance at 2026-09-30) | 10-K page:134; Q1 release page:4; Q2 release pages:2 and 3; Q3 release page:2 |
| Investments rated 3 or 4 on the adviser's scale, fair value (period end) | 1,023 (calculated) | 1,242 (calculated) | 1,109 (calculated) | 1,121 (calculated) | Same as Q3 2026 (balance at 2026-09-30) | MD&A rating tables: 10-Q Q1 page:125; 10-Q Q2 page:130; 10-Q Q3 page:135 (adviser's internal scale, not an external rating) |
| Debt principal to common equity (%, calculated) | 130.3 | 138.2 | 126.8 | 126.8 | Same as Q3 2026 (balance at 2026-09-30) | principal debt over common stockholders' equity, both rows above |
| Net investment income plus interest expense, over interest expense (x, calculated proxy) | 2.41 | 2.11 | 2.21 | 2.28 | 2.20 | not EBITDA cover; see Calculations |

### Debt schedule at 2026-09-30

Source: Note 9, 10-Q Q3 2026 pages 109 to 111, and the 10-K narrative (pages 266 to 278). Issuer is FS KKR Capital Corp unless the vehicle is named. Amounts are principal outstanding in USD millions.

| Instrument | Issuer / borrower | Outstanding | Available | Rate | Maturity | Security and guarantors |
| --- | --- | --- | --- | --- | --- | --- |
| Senior Secured Revolving Credit Facility | FS KKR Capital Corp (sole borrower); JPMorgan agent, ING collateral agent | 607 (euro, sterling and Australian dollar borrowings translated) | 3,134 net of 50 of standby letters of credit | SOFR + 1.78% to 1.90% plus credit spread adjustment 0.10% | Availability ends July 16, 2029; loans mature July 16, 2030 (10-K page:271, before the 2026 amendment) | Secured by substantially all assets of the Company and certain subsidiaries; guaranteed by certain subsidiaries (not named); covenants in the covenant table below |
| Callowhill Credit Facility | Callowhill Street Funding LLC, wholly-owned special-purpose subsidiary; CIBC agent | 337 | 63 | SOFR + 1.75% | June 2, 2030 per Note 9 (the 10-K narrative says June 3, 2030); revolving period ends June 2, 2028 | Portfolio securities held in the subsidiary are pledged as collateral to the facility (10-Q Q3 page:30); recourse wording not read |
| 2.625% Notes due 2027 | FS KKR Capital Corp | 400 | none | 2.63% | January 15, 2027 | Unsecured; no guarantor named |
| 3.250% Notes due 2027 | FS KKR Capital Corp | 500 | none | 3.25% | July 15, 2027 | Unsecured; no guarantor named |
| 3.125% Notes due 2028 | FS KKR Capital Corp | 750 | none | 3.13% | October 12, 2028 | Unsecured; no guarantor named |
| 7.875% Notes due 2029 | FS KKR Capital Corp | 400 | none | 7.88% | January 15, 2029 | Unsecured; no guarantor named |
| 6.875% Notes due 2029 | FS KKR Capital Corp | 600 | none | 6.88% | August 15, 2029 | Unsecured; swapped to floating (notional equals principal), carrying value reduced 12 by hedge accounting |
| 6.125% Notes due 2030 | FS KKR Capital Corp | 700 | none | 6.13% | January 15, 2030 | Unsecured; hedged, carrying value reduced 10 |
| 6.125% Notes due 2031 | FS KKR Capital Corp | 400 | none | 6.13% | January 15, 2031 | Unsecured; hedged, carrying value reduced 19 |
| 7.500% Notes due 2031 | FS KKR Capital Corp; issued June 8, 2026 under the Sixteenth Supplemental Indenture, U.S. Bank Trust Company trustee | 900 | none | 7.50% | August 1, 2031 | Unsecured; "rank structurally junior to all existing and future indebtedness" of subsidiaries; hedged, carrying value reduced 19 |
| CLO-2 Notes | KKR - FSK CLO 2 LLC, consolidated special-purpose subsidiary | 380 | none | SOFR + 1.48% to 2.15% | April 15, 2037 | Secured by the CLO issuer's loan portfolio |
| CLO-3 Notes | KKR - FSK CLO 3 LLC, consolidated special-purpose subsidiary | 363 | none | SOFR + 1.47% to 2.10% | January 15, 2038 | Secured by the CLO issuer's loan portfolio; the 10-K also describes Class D notes of 26.1 that the Note 9 outstanding table does not list (presumably held by the Company; not confirmed) |
| Cumulative Convertible Perpetual Preferred Stock, Series A | FS KKR Capital Corp; 6,000,000 shares at 25.00 issued June 29, 2026 to KKR Alternative Assets L.P. | 150 | none | 5.00% cash or 7.00% payment in kind, rising 1.00% annually from the 5.5-year anniversary | Perpetual; holder redemption after six years | Equity in GAAP (temporary equity); senior security for the 1940 Act asset coverage test |
| Total | | 6,487 including preferred; 6,337 debt | 3,197 | | | 27% secured and 73% unsecured of the debt (release page:3) |

No longer listed at 2026-09-30 (10-Q Q3 pages 109 and 111): the 3.400% Notes due 2026 (1,000 at 2025-12-31, maturity January 15, 2026), the Meadowbrook Run facility (265 outstanding at 2025-12-31; Meadowbrook Run terminated the committed facility on June 29, 2026, 10-Q Q2 page:109) and the CCT Tokyo Funding facility (45 outstanding at 2025-12-31, listed maturity June 2, 2026).

### Claims outside the debt figure

- **Unfunded commitments.** 1,041.1 to debt investments, 70.3 to equity and other, and 434.0 to the joint venture at 2026-09-30, total 1,545.4 (calculated); outside balance sheet debt, funded from liquidity (10-Q Q3 page:141).
- **Joint venture debt.** Credit Opportunities Partners JV, LLC carries its own debt of 2,330.9 against total assets of 4,538.9 (selected data, 10-Q Q3 page:94). It is not the issuer's borrowing and is not in the 6,337; the issuer's investment in it is 1,634 at fair value (14.4% of the portfolio) and it holds 79% of the venture.
- **Preferred stock.** 150 of convertible preferred sits outside debt but inside asset coverage, with cash dividends of 0.3125 per share declared for the fourth quarter (10-Q Q3 page:123).
- **Distributions.** A declared fourth quarter distribution of 0.44 per share and a special distribution of 0.20 per share (10-Q Q3 page:123); stockholder distributions payable were 121 at 2026-09-30.
- **Litigation.** Five stockholder matters are pending at 2026-09-30 and the Company states it "is unable to reasonably estimate any possible loss or range of loss" (10-Q Q3 pages 114 and 115): a putative securities class action filed May 4, 2026 (Stuart v. FS KKR Capital Corp., E.D. Pa.; amended complaint September 28, 2026) and derivative complaints filed May 12, June 29, July 15 and August 21, 2026, two of them against the Adviser under Section 36(b) of the 1940 Act on fee levels. The 10-K (page:279) reported no material proceedings at FY2025. No provision or accrual is shown.
- **Leases, pensions, factoring.** None found: the sources read describe no lease financing, pension, retiree medical or supply-chain finance obligation for this issuer.
- **Derivatives.** Interest rate swaps of 2,600 notional hedge the fixed-rate notes (10-Q Q3 pages 28 and 29); restricted cash of 61 is collateral posted on derivative contracts.

### Covenants and headroom

| Test | Level | Reported figure | Headroom | Definition and limitation |
| --- | --- | --- | --- | --- |
| Revolver minimum shareholders' equity, each fiscal quarter end | 3,750.0 after Amendment No. 1 of May 8, 2026; about 5,048.6 before | Not supplied: compliance certificate figure; common stockholders' equity is 4,999 at 2026-09-30 (proxy) | About 1,249 (25.0% of equity) on the proxy, calculated | Credit agreement definition of shareholders' equity not supplied; using balance sheet equity is an assumption. Against the former floor the same proxy would be 49.6 below, so the amendment was decisive. |
| Revolver 150% asset coverage, at all times (or statutory if greater) | 150% | 179% on debt, 177% including preferred (10-Q Q3 page:109) | 29 and 27 points; about 15% fall in coverage base reaches 150% (calculated) | Statutory definition; rounded ratios |
| Statutory 150% asset coverage for distributions and repurchases | 150% | 179% and 177% | As above | Failing it restricts distributions and share repurchases (10-Q Q3 page:142) |
| Notes indentures | Asset coverage compliance covenant of Section 18(a)(1)(A) | Compliance statement only | Not calculable beyond the asset coverage ratio | 7.500% Notes indenture text read (10-Q Q2 page:108); other indentures summarised only in the 10-K |
| Borrowing base pricing step at 1.60x | Margin steps up when the gross borrowing base is below 1.60 times the Combined Debt Amount | Not supplied: borrowing base value | Not calculable | A pricing grid, not a default test |
| All financing arrangements | Customary | "The Company was in compliance with all covenants required by its financing arrangements as of September 30, 2026 and December 31, 2025" (10-Q Q3 page:113) | Not calculable | Management statement; no figures |

### Liquidity

Liquidity at 2026-09-30 is cash and foreign currency of 111 plus availability of 3,197, being Callowhill 63 and the revolver 3,134 after 50 of standby letters of credit; the total is 3,308 (calculated), with 61 of restricted cash excluded. Availability is "subject to borrowing base and other limitations" (10-Q Q3 page:141), the borrowing base is not printed, and the revolver is secured on substantially all assets. No committed facility expires inside twelve months of the as-of date; the Callowhill revolving period ends June 2, 2028 and revolver availability ends July 16, 2029 (10-K pages 266 and 271). Notes of 900 mature by July 15, 2027. The nine-month operating cash inflow of 1,425 is not recurring earnings power: it comes from proceeds of 2,693 exceeding purchases of 1,431, which is portfolio liquidation.

### Earnings and income quality

- Total investment income fell to 294 in Q3 2026 from 373 in Q3 2025 and to 888 over nine months from 1,171, attributed to a smaller portfolio and non-accrual assets (10-Q Q3 page:136).
- Paid-in-kind interest was 46 of Q3 income (15.6%) and non-cash income including accretion was 51 of 294; dividend and other income of 84 (28.6%) came wholly from affiliated and controlled investments in Q3 (the unaffiliated line is nil), including the joint venture (10-Q Q3 pages 3 and 135).
- Net investment income of 127 in Q3 2026 was after a 12 incentive fee waiver; the adviser waives 50% of the subordinated income incentive fee during the waiver period of four quarters starting Q2 2026 (Q1 release page:3; 10-Q Q3 page:167).
- Nine-month net investment income of 366 (1.31 per share) compares with distributions to common stockholders of 373 and, per the releases, 1.34 per share paid. FY2025 net investment income of 654 compared with distributions of 784.
- Interest rate sensitivity over twelve months at 2026-09-30: up 100 basis points raises net interest income by 27 (6.2%), down 100 lowers it by 27 (10-Q Q3 page:155).

### Latest quarter and subsequent events

- Q3 2026: the amended securities class action complaint was filed September 28, 2026 (litigation above); repurchased about six million shares for about 69 (Q3 release page:1); repayments of 442 against purchases of 335 (Q3 release page:1); non-accrual share fell to 3.4% of fair value from 3.8%.
- Q2 2026 events: preferred issue of 150 closed June 29, 2026; the 7.500% Notes due 2031 of 900 were issued June 8, 2026; the KKR subsidiary tender offer of 150 completed; the 300 repurchase program began (Q2 release page:2; 10-Q Q3 page:74).
- May 8, 2026: Amendment No. 1 to the revolver (commitments, pricing and equity floor), recorded as a Q1 subsequent event.
- After the quarter to 2026-10-30: 1,546,162 shares repurchased for 17 at an average 10.88; fourth quarter distribution 0.44 and special distribution 0.20 declared October 7, 2026; preferred dividend 0.3125 declared October 28, 2026 (10-Q Q3 page:123; Q3 release pages 1 and 2). The last reported share price was 11.03 on October 30, 2026 against net asset value of 18.28 (10-Q Q3 page:164).

### Definition review and conflicts

- **Debt bases.** Carrying value 6,231, principal 6,337 and 6,487 including preferred are three bases for the same capital; hedge accounting adjustments reduce the carrying value of four notes (10-Q Q3 page:110, footnote 7). Always label the basis.
- **Net debt.** The release's net debt of 6,271 is principal debt plus preferred, less cash and foreign currency of 111 and net receivable for investments sold of 105 (Q3 release page:9). It excludes 61 of restricted cash; with it included the ratio would be lower (calculated 124%).
- **Cash basis by quarter.** Q1 management cash of 133 included 4 restricted; Q2 109 had none; Q3 111 excludes 61. This handoff's liquidity chart uses one basis (excluding restricted cash) in all four periods.
- **Letters of credit conflict in the 10-K.** Note 9 narrative says "As of December 31, 2025, $21 of such letters of credit have been issued" (10-K page:271) while the Note 9 table footnote says 50 (10-K pages 146, 261 and 282; repeated in 10-Q Q3 page:112). Availability of 3,117 plus outstanding 1,533 against commitments of 4,700 is consistent with 50, so 50 is used; the 21 matches the 2024 figure and looks stale.
- **Interest rate bases.** 5.57% stated (Q3 release page:3), 5.49% effective at 2026-06-30 (10-Q Q2 page:107), 5.72% average for nine months (10-Q Q3 page:113) are different measures.
- **Realised proceeds.** The cash flow proceeds of 646 for Q3 differ from the release's 442 of sales and repayments because the receivable for investments sold fell from 310 to 106; see Calculations.

## Calculations

All inputs are the printed figures cited above; results are rounded as shown.

| Calculation | Inputs | Result |
| --- | --- | --- |
| Debt principal to common equity, 2025-12-31 | 7,620 / 5,849 | 130.3% |
| Debt principal to common equity, 2026-03-31 | 7,290 / 5,274 | 138.2% (release prints 138%) |
| Debt principal to common equity, 2026-06-30 | 6,491 / 5,118 | 126.8% (release prints 127%) |
| Debt principal to common equity, 2026-09-30 | 6,337 / 4,999 | 126.8% (release prints 127%) |
| Net debt to equity, 2026-09-30, recomputed | (6,337 + 150 - 111 - 105) / 4,999 = 6,271 / 4,999 | 125.4% (release prints 125%) |
| Same with restricted cash of 61 netted | (6,271 - 61) / 4,999 | 124.2% |
| Debt plus preferred over common equity, 2026-09-30 | 6,487 / 4,999 | 129.8% |
| Change in net assets, nine months 2026 | 4,999 - 5,849; check: (402) - 375 - 73 | (850), equal to the statement of changes in net assets |
| Net asset value per share change | 18.28 - 20.89 = (2.61); 2.61 / 20.89 | down 12.5% over nine months 2026; 18.30 to 18.28 in Q3 |
| Debt principal reduction | 7,620 - 6,337 = 1,283; 1,283 / 7,620 | 16.8% |
| Total investment income decline, nine months | (1,171 - 888) / 1,171 | 24.2% |
| Q3 investment income decline | (373 - 294) / 373 | 21.2% |
| Interest expense decline, nine months | (354 - 305) / 354 | 13.8% |
| Interest cover proxy FY2025 | (654 + 464) / 464 | 2.41x |
| Interest cover proxy Q1 2026 | (117 + 105) / 105 | 2.11x |
| Interest cover proxy Q2 2026 | (122 + 101) / 101 | 2.21x |
| Interest cover proxy Q3 2026 | (127 + 99) / 99 | 2.28x |
| Interest cover proxy nine months 2026 | (366 + 305) / 305 | 2.20x |
| Quarterly operating cash flow, Q2 | 1,021 (six months) - 245 (Q1) | 776 |
| Quarterly operating cash flow, Q3 | 1,425 (nine months) - 1,021 | 404 |
| Quarterly interest paid, Q2 and Q3 | 213 - 121; 313 - 213 | 92; 100 |
| Quarterly purchases, Q2 and Q3 | 1,096 - 505; 1,431 - 1,096 | 591; 335 (release prints 335) |
| Quarterly proceeds, Q2 and Q3 | 2,047 - 760; 2,693 - 2,047 | 1,287; 646 |
| Q3 proceeds reconciliation | 442 sales and repayments + (310 - 106) fall in receivable | 646 |
| Liquidity, 2026-09-30 | 111 + 3,197 (63 + 3,134) | 3,308 |
| Unfunded commitments, 2026-09-30 | 1,041.1 + 70.3 + 434.0 | 1,545.4; liquidity covers them 2.14 times (3,308 / 1,545.4) |
| Maturities by year, sum | 0 + 900 + 750 + 1,000 + 1,644 + 1,300 + 380 + 363 | 6,337 |
| Secured and unsecured split | secured 607 + 337 + 380 + 363 = 1,687; unsecured notes 400 + 500 + 750 + 400 + 600 + 700 + 400 + 900 = 4,650; each over 6,337 | 26.6% and 73.4% (release prints 27% and 73%) |
| Equity floor headroom | 4,999 - 3,750.0 | 1,249.0, which is 25.0% of 4,999 |
| Against the former floor | 4,999 - 5,048.6 | (49.6) |
| Asset coverage fall to 150% | 1 - 1.50 / 1.77; 1 - 1.50 / 1.79 | about 15.3% (including preferred) and 16.2% (debt only); rounded ratios, so about 15% |
| Cash basis, 2026-03-31 | 124 + 5 | 129 (133 less 4 restricted) |
| Distribution per share paid, nine months | 0.48 + 0.42 + 0.44 | 1.34 against net investment income per share of 1.31 |
| Q3 net investment income without the waiver | 127 - 12 = 115; 115 / 121 distributions | 95.0% |
| Non-cash share of Q3 income | 51 / 294 | 17.3% |
| Investments rated 3 or 4 | 2026-09-30: 859 + 262; 2025-12-31: 760 + 263; 2026-03-31: 826 + 416; 2026-06-30: 888 + 221 | 1,121; 1,023; 1,242; 1,109 |
| Share price to net asset value | 11.03 / 18.28 - 1 | a 39.7% discount on October 30, 2026 |

## Gaps

| Gap | Severity | Consumers | Action |
| --- | --- | --- | --- |
| EBITDA, cash interest cover and net debt to EBITDA do not exist for a business development company | Structural | CP-2, CP-5 | Report Not supplied; use debt to equity, asset coverage and the labelled net investment income proxy |
| Revolver equity floor definition and compliance certificate figures not supplied; headroom is on a balance sheet equity proxy | Medium | CP-2 | State the proxy plainly; do not claim certified headroom |
| Covenant levels for Callowhill, the CLO notes and note indentures beyond asset coverage not supplied | Medium | CP-2 | Treat as Not supplied |
| Borrowing base value and the 1.60x ratio not printed | Medium | CP-2 | Availability of 3,197 is as printed and base-limited |
| No Q4 2025 release in the pack, so the FY2025 gross debt to equity ratio is calculated only | Low | CP-5 | Label the figure as calculated |
| Guarantor names for the revolver not given | Low | CP-2 | Report that certain subsidiaries guarantee |
| CLO-3 Class D notes of 26.1 described in the 10-K but absent from the outstanding table | Low | CP-5 | Do not add to debt; flag as unconfirmed |
| Letters of credit text conflict in the 10-K (21 versus 50) | Low | CP-5 | Use 50, which reconciles to availability |
| Joint venture full statements and look-through exposure not supplied | Low | CP-2 | Use selected data only |
| Loss from the five pending stockholder suits cannot be estimated by the Company; no accrual shown | Medium | CP-2, CP-5 | Report as an unquantified contingent claim; do not assign an amount |
| No ratings or market debt quotes in the pack | Medium | CP-2 | Not supplied |

## Next module

CP-1A (business and transaction context) follows. It should take from this handoff: the issuer is an externally managed business development company with a KKR affiliated adviser; the 2026 capital actions (150 convertible preferred from a KKR subsidiary, 150 tender offer, 300 repurchase program, 50% incentive fee waiver for four quarters); the May 8, 2026 revolver amendment; the 900 of 7.500% Notes issued June 8, 2026; and the joint venture exposure of 1,634. It must carry the corrections to CP-0 stated above, the covenant proxy limits, the three debt bases and the absence of EBITDA. CP-2 and CP-5 then rely on this handoff for every figure and must keep the calculated rows labelled as calculated.
