## Request

Subject: Millicom International Cellular S.A. (issuer id tigo; "MIC S.A.", Luxembourg parent of the Tigo group, Nasdaq: TIGO). As-of date: 2026-11-05 (cutoff 2026-11-05). Module: CP-1, financials and credit metrics, pathway credit_snapshot, public case. Reporting currency USD; all amounts are USD millions unless a row says otherwise. Current period q3-2026 (quarter and nine months ended September 30, 2026); prior period fy-2025.

Scope: extract the reported financial statements, debt and liquidity facts and management credit metrics from the supplied filings; keep reported facts apart from calculations; state what the evidence supports for credit use and what stays restricted. No credit rating, price or valuation view is given.

Locator convention: "chunk N" is the `page` field of the named converted-text file (about 3,000 characters per chunk, not the printed page of the filing). Source labels used below: 20-F = 20-F_2025-12-31_tigo-20251231.htm.jsonl; Q1 6-K = 6-K_2026-05-12_dp246578_6k.htm.jsonl; Q2 6-K = 6-K_2026-08-06_dp251442_6k.htm.jsonl; Q3 6-K = 6-K_2026-11-05_dp256407_6k.htm.jsonl.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | What it is |
| --- | --- | --- |
| 20-F_2025-12-31_tigo-20251231.htm.jsonl | 13be2a8c900b103376e04c45e18282d28f2b1aac3516bfaed99fc02cc0e15f37 | Form 20-F for the year ended December 31, 2025, filed March 24, 2026; audited IFRS consolidated statements (USD millions); controls audited year-end 2025 facts |
| 6-K_2026-05-12_dp246578_6k.htm.jsonl | e31fa18185d3ceef7ba9e0133efc952dd4f43ccbd999e9a5f5b5af04d8dbf712 | Form 6-K with unaudited IAS 34 statements for the three months ended March 31, 2026 and the Q1 2026 earnings release; no review report |
| 6-K_2026-08-06_dp251442_6k.htm.jsonl | 76b47ade3b6a5a2f060db2592b816c6ed584aa9ed405d036c0be893943dc1c51 | Form 6-K with the half-year report for the six months ended June 30, 2026 (KPMG Audit S.à r.l. review conclusion, chunk 8) and the Q2 2026 earnings release |
| 6-K_2026-11-05_dp256407_6k.htm.jsonl | 6ab7c7e5e635829f16eb15a89301463e6131db3f5c0e68ee118ba6350801f894 | Form 6-K with unaudited IAS 34 statements for the nine months ended September 30, 2026 and the Q3 2026 earnings release dated November 5, 2026; no review report |

Run context (settings only, not issuer evidence): context, sha256 5b145622a49a1e38ec7885504ac944230be02601fefa1d2f3fb7d83ded83c956. It holds no ratings, quotes, deal terms or assumptions; blanks are not treated as zero.

### Supplied handoffs

| Module | sha256 | Use in this module |
| --- | --- | --- |
| CP-0 | 533a512a1f3bb7bc99ba007a510cec3fdee3aeab214040d4ea601266e7a3d9fd | Source readiness: CP-1 rated READY_WITH_LIMITATIONS. Its gaps G1 (covenant terms not supplied), G2 (no instrument-level debt table after December 31, 2025), G3 (revolving credit facility status), G5 (Q1 and Q3 unreviewed), G6 (restated and re-presented comparatives), G7 (provisional purchase accounting), G8 (perimeter break) and G9 (unreconciled figures) are carried into the Gaps section below. |

### Source versions and basis

- Entity and perimeter: Millicom International Cellular S.A. and subsidiaries, consolidated, IFRS (IAS 34 for interims), USD. The Honduras joint venture (66.67 percent, joint control) and the Chile associate (49 percent, from February 10, 2026) are equity-accounted and not consolidated (Q3 6-K chunks 11, 17; 20-F chunk 92).
- Perimeter change: Tigo Uruguay and Tigo Ecuador consolidated from October 2025; Coltel consolidated from February 6, 2026 (Q3 6-K chunk 1 footnote i). Quarters before those dates are not like-for-like with later quarters.
- 2025 interim comparatives are re-presented in the 6-Ks for the Paraguay mobile finance business moved to discontinued operations (Q3 6-K chunks 1, 12). The 20-F FY2025 income statement is not re-presented. The December 31, 2025 balance sheet is restated in the Q3 6-K for final Uruguay and updated Ecuador purchase accounting (Q3 6-K chunk 12), while the Q1 6-K, Q2 6-K and 20-F carry the original figures.
- Statement status: the 20-F is audited (KPMG LLP report, chunk 193). The Q2 6-K carries a review conclusion (chunk 8). The Q1 6-K and Q3 6-K are unaudited and carry no review report. Non-IFRS measures (Adjusted EBITDA, capex, OCF, equity free cash flow, net debt, leverage) are management measures from the earnings releases and are attributed supporting claims, not audited facts.

## Findings

### Financials and credit metrics

Reported facts only. Period-end items (cash, debt, equity, lease liabilities, KPIs) are balances at the end of the column period: FY2025 is December 31, 2025; Q1 2026 is March 31; Q2 2026 is June 30; Q3 2026 and 9M 2026 are September 30, 2026; 9M 2025 is September 30, 2025 or the nine months ended then. Flows in Q1 to Q3 2026 columns are the quarter, 9M 2026 is nine months, and where a discrete quarter is not printed the cell says Not supplied and shows the cumulative figure that is printed. "Not supplied" means the source set does not print the figure; it is never zero.

| Metric | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | 9M 2026 | 9M 2025 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue | 5,819 | 1,985 | 2,179 | 2,276 | 6,440 | 4,150 | IFRS income statements: 20-F chunk 194; Q1 6-K chunk 1; Q2 6-K chunk 8; Q3 6-K chunk 1. 9M 2025 re-presented |
| Service revenue (non-IFRS) | 5,451 | 1,857 | 2,043 | 2,145 | 6,045 | 3,888 | 20-F chunk 106; Q1 6-K chunk 26; Q2 6-K chunk 37; Q3 6-K chunk 34 |
| Adjusted EBITDA (non-IFRS, continuing) | 2,749 | 857 | 1,009 | 1,092 | 2,958 | 1,964 | FY2025 group total in 20-F segment note chunk 228; quarters in Q3 6-K chunk 41 reconciliation; 9M 2025 re-presented |
| Adjusted EBITDA margin (release) | Not supplied | 43.2% | 46.3% | 48.0% | 45.9% | 47.3% | Q1 6-K chunk 26; Q2 6-K chunk 37; Q3 6-K chunk 34. FY2025 margin is not printed |
| Operating profit | 1,639 | 416 | 462 | 600 | 1,478 | 1,163 | Income statements, same chunks as revenue |
| Interest and other financial expenses | (702) | (248) | (292) | (328) | (868) | (507) | Income statements; Q3 6-K note 11 prints (508) for 9M 2025 (chunk 25) |
| Interest and other financial income | 28 | 10 | 13 | 13 | 37 | 16 | Income statements, same chunks |
| Profit before taxes, continuing operations | 1,665 | 154 | 204 | 213 | 571 | 1,346 | FY2025 includes the Lati gain of 741; 9M 2025 includes 742 |
| Tax expense | (303) | (78) | (104) | (115) | (298) | (257) | Income statements |
| Net profit attributable to owners | 1,316 | 109 | 109 | 98 | 316 | 1,064 | Income statements; non-controlling interests are a loss of 41 for 9M 2026 (Q3 6-K chunk 1) |
| Net cash provided by operating activities | 1,734 | 590 | Not supplied (H1 2026: 1,301) | 727 | 2,028 | 1,257 | Cash flow statements: 20-F chunk 197; Q1 6-K chunk 3; Q2 6-K chunk 10; Q3 6-K chunk 4; Q3 quarter in Q3 6-K chunk 42 |
| Cash interest paid on debt and other financing | 409 | 138 | Not supplied (H1 2026: 279) | Not supplied (9M 2026: 463) | 463 | 313 | Cash flow statements |
| Cash interest paid on leases | 176 | 68 | Not supplied (H1 2026: 137) | Not supplied (9M 2026: 216) | 216 | 119 | Cash flow statements |
| Taxes paid | 335 | 53 | 146 | 106 | 306 | 236 | Cash flow statements; Q2 6-K chunk 34; Q3 6-K chunk 31 |
| Capex excluding spectrum (non-IFRS) | 719 | 193 | 234 | 243 | 669 | 447 | FY2025 from 20-F segment note chunk 228; Q1 6-K chunk 26; Q2 6-K chunk 37; Q3 6-K chunks 34, 42 |
| Spectrum and licenses paid | 73 | 99 | 41 | 67 | 207 | 62 | 20-F chunk 197; Q1 6-K chunk 23; Q2 6-K chunk 34; Q3 6-K chunk 31 |
| Operating cash flow (Adjusted EBITDA less capex, non-IFRS) | Not supplied | 664 | 775 | 849 | 2,289 | 1,516 | Releases: Q1 6-K chunk 26; Q2 6-K chunk 37; Q3 6-K chunk 34 |
| Equity free cash flow | 916 | 225 | 327 | 316 | 867 | 638 | FY2025 20-F chunk 106; Q1 6-K chunk 23; Q2 6-K chunk 34; Q3 6-K chunk 31 |
| Equity free cash flow excluding divestitures | 864 | 225 | 327 | 316 | 867 | 601 | Same chunks; divestiture proceeds removed are 52 for FY2025 and 37 for 9M 2025 |
| Dividends paid to owners | 754 | 125 | Not supplied (H1 2026: 461) | Not supplied (9M 2026: 587) | 587 | 420 | Cash flow statements |
| Acquisition of subsidiaries, net of cash acquired | 545 | 742 | Not supplied (H1 2026: 937) | Not supplied (9M 2026: 924) | 924 | — as printed | Cash flow statements; FY2025 and Q1 2026 captions also include joint ventures and associates |
| Cash and cash equivalents | 1,552 | 1,177 | 861 | 848 | 848 | 1,663 | Balance sheets; 9M 2025 from Q3 6-K cash flow statement (chunk 4); the release prints 1,664 for September 30, 2025 (Q3 6-K chunk 32) |
| Restricted cash | 50 | 40 | 30 | 31 | 31 | Not supplied | Balance sheets |
| Gross debt (release) | 6,886 | 8,624 | 8,742 | 8,648 | 8,648 | 6,260 | Debt tables: Q3 6-K chunk 32; Q2 6-K chunk 35; Q1 6-K chunks 24-25 |
| Debt and financing on balance sheet: current plus non-current | 329 plus 6,556 | 1,232 plus 7,393 | 1,095 plus 7,647 | 872 plus 7,777 | 872 plus 7,777 | Not supplied | 20-F chunk 196; Q1 6-K chunks 2-3; Q2 6-K chunk 10; Q3 6-K chunk 3 |
| Derivatives and vendor financing included in net debt | 23 | 162 | 194 | 183 | 183 | 30 | Release debt tables |
| Net debt (release, non-IFRS) | 5,357 | 7,609 | 8,075 | 7,983 | 7,983 | 4,627 | Release debt tables |
| Leverage (release, non-IFRS) | 2.17x | 2.76x | 2.73x | 2.53x | 2.53x | 2.09x | Release debt tables; definition in Q3 6-K chunk 40 |
| Lease liabilities (current plus non-current) | 2,587 (20-F); 2,563 restated | 3,098 | 3,159 | 3,190 | 3,190 | Not supplied | 20-F chunk 258; Q1 6-K chunks 2-3; Q2 6-K chunk 10; Q3 6-K chunks 3, 12 |
| Total equity | 3,621 | 3,169 | 2,493 | 2,278 | 2,278 | 3,310 | Balance sheets; 9M 2025 from Q3 6-K chunk 5 |
| Interest expense on bonds and bank financing | 407 | 135 | 164 | 173 | 472 | 296 | Financial expense notes: 20-F chunk 257; Q1 6-K chunk 18; Q2 6-K chunk 28; Q3 6-K chunk 25 |
| Interest expense on leases | 182 | 68 | 78 | 87 | 232 | 124 | Same notes |
| Average interest rate on debt (release) | Not supplied | 7.8% | 8.2% | 8.3% | 8.3% | Not supplied | Release debt discussions |
| Fixed-rate share of debt (release) | 70% | 57% | 56% | 56% | 56% | Not supplied | FY2025 value stated as the year-end 2025 comparison in Q3 6-K chunk 32 |
| Average debt maturity in years (release) | Not supplied | 3.6 | 3.5 | 3.5 | 3.5 | Not supplied | Release debt discussions |
| Debt held at operating entities (release) | 65% (4,470) | 71% | 70% | approximately 70% | approximately 70% | Not supplied | 20-F chunk 114; Q1 6-K chunk 24; Q2 6-K chunk 35; Q3 6-K chunk 32 |
| Mobile customers (thousands) | 49,311 | 57,335 | 55,779 | 55,845 | 55,845 | 42,158 | KPI table Q3 6-K chunk 33; FY2025 column is the Q4 2025 value; 9M 2025 column is the Q3 2025 value |
| Of which postpaid (thousands) | 10,919 | 16,543 | 16,805 | 17,194 | 17,194 | 8,896 | KPI table Q3 6-K chunk 33 |
| Mobile ARPU (USD per month, excludes Coltel) | 6.8 | 6.7 | 7.1 | 7.4 | 7.1 | 6.0 | KPI table Q3 6-K chunk 33; nine-month figures Q3 6-K chunk 42 |
| Home ARPU (USD per month, excludes Coltel) | 25.3 | 26.1 | 26.9 | 27.7 | 27.0 | 24.5 | Q3 6-K chunks 33, 42 |
| Customer relationships, fixed (thousands) | 4,604 | 6,141 | 6,066 | 5,966 | 5,966 | 4,576 | Q3 6-K chunk 33 |

### Debt maturity profile

Total debt and financing repayable (note 11B, carrying amounts), as printed in each package. The Q3 6-K prints the December 31, 2025 total as 6,887; the other packages and the 20-F print 6,886.

| Due within | December 31, 2025 | March 31, 2026 | June 30, 2026 | September 30, 2026 |
| --- | --- | --- | --- | --- |
| One year | 329 | 1,232 | 1,095 | 872 |
| One to two years | 697 | 916 | 1,008 | 986 |
| Two to three years | 1,047 | 1,583 | 1,858 | 1,947 |
| Three to four years | 1,025 | 948 | 929 | 1,601 |
| Four to five years | 1,014 | 1,129 | 1,800 | 1,147 |
| After five years | 2,773 | 2,818 | 2,052 | 2,094 |
| Total as printed | 6,886 | 8,624 | 8,742 | 8,648 |

Locators: Q1 6-K chunks 17-18; Q2 6-K chunk 28; Q3 6-K chunk 25 (Q3 table also prints December 31, 2025 as 6,887). Which instruments fall in each bucket is Not supplied.

### Debt structure and instruments

Latest instrument-level detail is December 31, 2025 (20-F chunks 245-246, 252-253). Carrying amounts, USD millions. The "Developments in 2026" column is taken from the 6-K financial obligations notes and cannot be rolled into a September 30, 2026 balance.

| Instrument | Obligor (location) | Maturity | Carrying at December 31, 2025 | Developments in 2026 |
| --- | --- | --- | --- | --- |
| SEK floating-rate notes, STIBOR plus 3.000%, swapped to USD | MIC S.A. (Luxembourg) | January 2027 | 244 | Hedged by currency swap (Q3 6-K chunk 25); falls inside the one-to-two-year window by the September 30, 2026 ladder |
| 7.375% Senior Notes | MIC S.A. | 2032 | 446 | Reopened April 14, 2026 for an additional 87.5 principal in a Regulation S private placement (Q3 6-K chunk 24) |
| 4.500% Senior Notes | MIC S.A. | 2031 | 755 | None stated |
| 6.250% Senior Notes | MIC S.A. | 2029 | 614 | None stated |
| 5.125% Senior Notes | MIC S.A. | 2028 | 359 | None stated |
| COP-USD linked private bond, fixed rate (IDB and Proparco) | MIC S.A. | 8 years from March 27, 2026 | Not applicable (issued 2026) | Issued for COP 370,000 million (Q3 6-K chunk 24) |
| 5.125% Senior Notes | Comunicaciones Celulares S.A. (Guatemala), guaranteed by Guatemalan subsidiaries | 2032 | 738 | None stated |
| 4.500% Senior Notes | Telecomunicaciones Digitales, S.A. (Panama) | 2030 | 550 | None stated |
| 5.875% Senior Notes | Telefonica Celular del Paraguay (Paraguay) | 2027 | 140 | Redeemed in full at par on April 29, 2026, about 139.7 principal (Q3 6-K chunk 25) |
| Other bonds: Paraguay PYG notes, Bolivia BOB notes, Colombia UNE bonds | Operating subsidiaries | 2026 to 2036 | 2025 total bonds 4,550 less the rows above | Paraguay bond redemption PYG 98 billion in September 2026; Bolivia 5% bond repaid August 2026; UNE Bond 3 tranche B repaid May 2026 (Q3 6-K chunks 23-25) |
| Bank and development finance institution loans | Operating subsidiaries and MIC S.A. | 2026 to 2033 | 2,335 | New 2026 loans in Colombia (Coltel and Tigo Colombia), Guatemala, Bolivia, Panama and others (Q3 6-K chunks 23-25); balances Not supplied |
| Revolving credit facility, 600 commitment, ESG-linked | MIC S.A. | October 15, 2027 | Undrawn; 20-F shows (1) of amortized costs | Status at September 30, 2026 Not supplied (20-F chunks 124, 255, 272) |
| Coltel debt on acquisition | Colombia Telecomunicaciones S.A. E.S.P. | Mixed | Not applicable | "Other debt and financing" of 1,424 at February 6, 2026 (Q3 6-K chunk 9); Q1 release says consolidation added 1,482 of gross debt and 1,513 of net debt (Q1 6-K chunk 24). A 500 bond issued in 2020 and a 70 bank loan raised in 2024 are hedged (Q3 6-K chunk 25); their maturities are Not supplied |

20-F debt by location at December 31, 2025: MIC S.A. 2,416; Guatemala 1,602; Colombia 620; Paraguay 705; Bolivia 128; Panama 734; Costa Rica 148; El Salvador 248; Uruguay 201; Ecuador 83; total 6,886 (20-F chunk 245). Honduras joint venture debt is 367 excluding leases and non-recourse to MIC S.A. (20-F chunk 114). Guarantees by MIC S.A. of subsidiary financings were 629 at December 31, 2025 (20-F chunk 258), including the Uruguay Santander loan and the El Salvador IDB Invest loan (20-F chunks 124, 256).

### Liquidity and cash flow

- Cash and cash equivalents were 848 at September 30, 2026, about 78 percent held in U.S. dollars, against 861 at June 30, 2026 (Q3 6-K chunk 32). At December 31, 2025, cash was 1,552, of which 1,166 was at holding level and 387 at operating subsidiaries (20-F chunk 110). The September 30, 2026 split between holding and operating level is Not supplied.
- Debt due within one year was 872 at September 30, 2026 (Q3 6-K chunk 25). Current liabilities were 5,032 against current assets of 2,759 (Q3 6-K chunk 3).
- The 600 revolving credit facility was undrawn at December 31, 2025 and extended to October 15, 2027 (20-F chunks 124, 272). No 6-K states its drawn or available amount at a 2026 date. The Tigo Chile associate has a 65 revolving facility expiring August 2027 with the full balance available at June 30, 2026 (Q2 6-K chunk 26); that facility is at an equity-accounted associate.
- Nine months to September 30, 2026: operating cash flow 2,028, purchase of property, plant and equipment 658, other intangibles 100, spectrum and licenses 207, acquisitions of subsidiaries 924, dividends paid 587, repayment of debt 999 against proceeds of 1,131 (Q3 6-K chunks 4-5). Net decrease in cash was 698.
- Equity free cash flow was 867 for the nine months and 316 for Q3 2026. Management maintains full-year 2026 equity free cash flow of around 1.1 billion and a year-end leverage target below 2.5x (Q3 6-K chunk 29); the target had been "at least $900 million" and "around 2.5x" in the Q1 6-K (chunk 21) and was raised in the Q2 6-K (chunk 32). These are management claims.
- Dividends: the AGM of May 20, 2026 approved 3.00 per share in four quarterly installments of 0.75 (July 2026, October 2026, January 2027, April 2027), and on August 5, 2026 the Board approved an interim dividend of 1.50 per share paid as 0.75 on January 15, 2027 and 0.75 on April 15, 2027 (Q3 6-K chunk 20). The balance sheet shows a dividend payable of 579 at September 30, 2026 (Q3 6-K chunk 3).
- Other debt-like and liquidity items: payables and accruals for capital expenditure of 1,644 non-current and 457 current at September 30, 2026 against 758 and 440 at December 31, 2025 (Q3 6-K chunk 3); a 163 supplier finance balance at December 31, 2025 (20-F chunk 117), not updated in the 6-Ks; amounts due to the Honduras joint venture of 184 (Q3 6-K chunk 21); capital commitments of 384, of which 367 within one year (Q3 6-K chunk 27); claims against the group of 217 with 91 provided, and tax exposure of 378 with 60 provided (Q3 6-K chunks 26-27).

### Covenants, restrictions and definitions

- Covenants: the 20-F states facilities are subject to covenants including net leverage ratio, debt service coverage ratios and debt-to-earnings ratios, that certain financings restrict sales of businesses or significant assets, and that at December 31, 2025 there were no covenant breaches and none were anticipated in the following twelve months (20-F chunk 258). Facilities at MIC S.A. level carry leverage covenants; operating-level facilities carry leverage and restricted payment covenants and in some cases debt service coverage and debt-to-earnings covenants (20-F chunk 116). Some operating subsidiaries and joint ventures have debt covenants that restrict upstreaming cash to MIC S.A. (20-F chunk 111). Covenant thresholds, definitions, test dates and headroom are Not supplied, and the 6-Ks do not restate a compliance statement.
- Cash repatriation to MIC S.A. was 1,102 in 2025 (subsidiaries 979, joint ventures 123) (20-F chunk 110). For 9M 2026, repatriation from joint ventures and associates in the equity free cash flow build is 79 (Q3 6-K chunk 31). Note 8 says the Honduras venture repatriated 79 in the three months to September 30, 2026 (Q3 6-K chunk 21), which conflicts with the 22 for Q3 in the cash flow build.
- Adjusted EBITDA definition differs between documents: the segment note defines it as operating profit excluding impairment losses, depreciation and amortization, share of profit in the Honduras joint venture and Chile associate, and gains or losses on disposal of fixed assets (Q3 6-K chunk 18); the release adds early termination of leases (Q3 6-K chunk 40). The reconciliation of Adjusted EBITDA to profit before tax (Q3 6-K chunk 41) shows other operating income (expense) and share of profit in the Honduras joint venture removed.
- Leverage as defined by management is net debt over last-twelve-month Adjusted EBITDA after subtracting depreciation of right-of-use assets and interest expense on leases, pro forma for acquisitions in the last twelve months (Q3 6-K chunk 40). It is not stated to be a covenant ratio. Net debt includes derivative assets and liabilities and "pledged and time deposits" (Q3 6-K chunk 40) and, in the release table, "Derivatives & Vendor Financing" of 183 (Q3 6-K chunk 32). Lease liabilities are excluded from gross debt and net debt.
- Items above Adjusted EBITDA flagged as one-off: Q3 2026 total (31), of which Colombia (20); nine months total (149), of which Colombia (116) (Q3 6-K chunk 41). Items below Adjusted EBITDA: a goodwill impairment of about 32 for the Costa Rica unit (Q3 6-K chunk 27) and the Guatemala settlement of former executives' claims with a 99 expense, of which 31 paid in the quarter and 68 outstanding over seven years (Q3 6-K chunk 26).

### Latest quarter (Q3 2026) changes

- Revenue 2,276 and Adjusted EBITDA 1,092 against 1,415 and 693 in Q3 2025; management gives organic growth of 4.8 percent for revenue and 7.7 percent for Adjusted EBITDA, with perimeter 32.9 percent and foreign exchange and other 17.1 percent of the EBITDA growth (Q3 6-K chunk 41).
- Operating profit 600, net financial expenses 314 (Q3 2025: 162), other non-operating expenses 71 driven by the Guatemala settlement, tax 115, net profit attributable to owners 98 (Q3 6-K chunks 29-31).
- Gross debt 8,648 against 8,742 at June 30, 2026; cash 848 against 861; net debt 7,983 against 8,075; leverage 2.53x against 2.73x; a dividend payment of 126 in the quarter; fixed-rate share of debt 56 percent; average interest rate 8.3 percent (Q3 6-K chunk 32).
- Financing: Tigo Panama repaid a 75 Scotiabank loan and took a new 6-year 75 loan from BAC; Coltel entered two 3-year loans (COP 245,000 million and COP 54,500 million) to repay a COP 272,000 million Scotiabank loan; Tigo Bolivia issued a new BOB bond and bank loans and repaid its 5% bond; Tigo Paraguay redeemed a PYG 98 billion bond (Q3 6-K chunks 23-25).
- Post-period (October 2026): Coltel took a COP 40,000 million loan from BTG Pactual and prepaid 12.5 of the Santander loan; an incentive plan of about 50 contingent on 2 billion of annual equity free cash flow was announced; Paraguay MFS regulatory approval was gathered in October 2026 and the Ecuador acquisition accounting measurement period ended October 30, 2026 (Q3 6-K chunks 12, 14, 28).

### Interpretation (evidence, risk mechanism, credit implication)

- Leverage. Evidence: net debt rose from 5,357 at December 31, 2025 to 7,983 at September 30, 2026 while management leverage moved from 2.17x to 2.53x, after a peak of 2.76x at March 31, 2026 (release tables). Mechanism: the debt increase came mainly from consolidating Coltel and paying for the Colombian stakes, offset by a larger EBITDA base and strong cash generation; the ratio is pro forma and net of lease costs. Implication: leverage has improved for two consecutive quarters, but the reported figure rests on a management denominator that is not reproducible from the supplied tables (Calculations 3 and 4), and covenant headroom cannot be assessed because covenant terms are not supplied.
- Coverage. Evidence: interest expense on bonds and bank financing was 472 for nine months against Adjusted EBITDA of 2,958, with lease interest of 232 on top. Mechanism: the average cost of debt was 8.3 percent and 44 percent of debt is floating (the fixed-rate share is 56 percent), so rate moves pass through to interest; local-currency borrowing of 61 percent of debt matches revenue currencies but carries higher coupons than the dollar book (5.7 percent on dollar debt). Implication: coverage is adequate on the reported period (Calculation 6) but the Coltel floating-rate debt raises sensitivity to rates; interest sensitivity is Not supplied.
- Cash flow quality. Evidence: Adjusted EBITDA of 2,958 converts to operating cash flow of 2,289 after capex and to equity free cash flow of 867 after spectrum, taxes, interest and lease payments; 9M dividends paid of 587 consumed most of it. Mechanism: lease payments (483 net for nine months) and spectrum (207) are large fixed claims; restructuring items above EBITDA of 149 depress EBITDA temporarily. Implication: free cash flow after dividends was about 280 for the nine months (Calculation 8) while acquisitions required 924, so the group funded the Colombian deals with cash, debt and equity buy-outs of minorities rather than with internally generated cash alone.
- Liquidity. Evidence: cash of 848 against debt due within one year of 872, and a 600 revolving facility that was undrawn at December 31, 2025 and due October 2027. Mechanism: the near-term ladder is dominated by operating-level bank loans that are routinely rolled (the Q3 notes show repeated refinancing), and the 2027 SEK note and revolving facility mature within about fourteen months. Implication: liquidity depends on continued market access and on facility availability that the 6-Ks do not confirm; the current-year dividend schedule adds a visible cash call (Calculation 7).
- Data quality. Evidence: Q1 and Q3 are unreviewed; the December 31, 2025 balance sheet was restated; purchase accounting for Coltel is provisional; the cash flow statement and the release disagree on 9M operating cash flow (2,028 against 2,019). Implication: figures are usable as reported with labels, but any single-period ratio mixing restated and original bases carries an unresolved difference.
- Definition risks. Evidence: management leverage and Adjusted EBITDA are non-IFRS and defined differently across the segment note and the release. Implication: do not equate the release leverage with a covenant ratio; do not compare it with ratios built from IFRS lines without stating the bridge.

## Calculations

All inputs are quoted from the sources above; results are calculated by this module, not printed by the issuer. Rounding is to the stated precision.

### Calculation 1: Discrete quarter cash flow from cumulative statements

- Q2 2026 operating cash flow = H1 2026 1,301 minus Q1 2026 590 = 711. Q3 2026 = 9M 2,028 minus H1 1,301 = 727, which equals the Q3 figure printed in the equity free cash flow reconciliation (727, Q3 6-K chunk 42), so the cash flow statement ties at quarter level.
- Q2 2026 cash interest paid on debt = H1 279 minus Q1 138 = 141; Q3 = 9M 463 minus H1 279 = 184.

### Calculation 2: Last-twelve-month Adjusted EBITDA as printed, not pro forma

- LTM to September 30, 2026 = Q4 2025 776 + Q1 2026 857 + Q2 2026 1,009 + Q3 2026 1,092 = 3,734 (quarterly series in Q3 6-K chunk 41). Basis limitation: Q4 2025 and Q1 2026 include only part of the Coltel, Uruguay and Ecuador contribution, so this is not a pro forma figure.
- Cross-check: the FY2025 20-F figure of 2,749 less re-presented 9M 2025 of 1,964 plus 9M 2026 of 2,958 would be 3,743; the nine-unit difference arises because the 20-F figure is not re-presented for discontinued operations.

### Calculation 3: Simple leverage ratios (calculated, unadjusted for pro forma or leases)

- Net debt 7,983 divided by LTM Adjusted EBITDA 3,734 = 2.14x.
- Gross debt 8,648 divided by 3,734 = 2.32x.
- Lease-inclusive: net debt 7,983 plus lease liabilities 3,190 (2,846 non-current plus 344 current) = 11,173; divided by 3,734 = 2.99x.
- Management leverage is 2.53x. Dividing net debt 7,983 by 2.53 implies a denominator of about 3,155, which is lower than 3,734 by about 579; management subtracts depreciation of right-of-use assets and lease interest and adds pro forma acquisition EBITDA, and neither the right-of-use depreciation by quarter nor the pro forma bridge is supplied. The management ratio is therefore Not calculable from the supplied tables.

### Calculation 4: Net debt and gross debt movements

- Gross debt 8,648 minus 6,886 at December 31, 2025 = 1,762. Net debt 7,983 minus 5,357 = 2,626. The Q1 release attributes 1,482 of the gross debt increase and 1,513 of the net debt increase in Q1 to consolidating Coltel and 773 of Q1 net debt to acquisition-related payments (Q1 6-K chunk 24); the remaining components are not summed here.
- Gearing as defined in the 20-F (net debt divided by equity attributable to owners plus net debt): December 31, 2025 = 5,357 / (3,640 + 5,357) = 0.60 (printed 0.60 in 20-F chunk 273); September 30, 2026 = 7,983 / (2,238 + 7,983) = 0.78.

### Calculation 5: Maturity concentration at September 30, 2026

- Due within one year 872 / 8,648 = 10.1 percent; within two years (872 + 986) = 1,858 / 8,648 = 21.5 percent; after five years 2,094 / 8,648 = 24.2 percent.
- Cash 848 / debt due within one year 872 = 0.97x.

### Calculation 6: Interest coverage, nine months to September 30, 2026

- Adjusted EBITDA 2,958 / interest expense on bonds and bank financing 472 = 6.27x.
- Adjusted EBITDA 2,958 / (472 + lease interest 232) = 4.20x.
- Adjusted EBITDA 2,958 / cash interest paid (463 on debt plus 216 on leases) = 4.36x.
- Basis: interest expense and Adjusted EBITDA both include Coltel from February 6, 2026 and Uruguay and Ecuador from October 2025, so the ratios are on a reported basis and not pro forma. The 44 percent floating share used in the interpretation is 100 percent minus the printed 56 percent fixed share.

### Calculation 7: Scheduled dividend cash calls after September 30, 2026

- Remaining declared installments: October 2026 0.75; January 2027 0.75 plus 0.75; April 2027 0.75 plus 0.75 = 3.75 per share. Multiply by 167.717 million weighted average shares for Q3 2026 (Q3 6-K chunk 20) = about 629. The balance sheet dividend payable is 579; the difference of about 50 is not explained in the sources (possibly the October installment timing or share count), so 629 is an approximation.

### Calculation 8: Cash generation and uses, nine months to September 30, 2026

- Equity free cash flow 867 minus dividends paid 587 = 280.
- Operating cash flow (Adjusted EBITDA less capex) 2,289 / Adjusted EBITDA 2,958 = 77.4 percent.
- Adjusted EBITDA excluding the 149 one-offs reported above EBITDA = 2,958 + 149 = 3,107; for Q3, 1,092 + 31 = 1,123. This adds back the issuer's own one-off classification; the one-offs are not independently verified.
- Implied fourth-quarter equity free cash flow if the around-1.1-billion guidance were met exactly = 1,100 minus 867 = 233 (management claim, approximate).
- LTM equity free cash flow excluding divestitures = FY2025 864 minus 9M 2025 601 plus 9M 2026 867 = 1,130; net debt 7,983 / 1,130 = 7.1x. Basis mix: FY2025 is not re-presented while 9M 2025 is, and the perimeter changed, so this ratio is indicative only.

### Calculation 9: FY2025 Adjusted EBITDA margin

- 2,749 / 5,819 = 47.2 percent (the 20-F does not print a margin).

## Gaps

| Id | Severity | Gap | Affects | Action |
| --- | --- | --- | --- | --- |
| G1 | High | Covenant thresholds, definitions, test dates and headroom are Not supplied; the only statement is the qualitative 20-F statement for December 31, 2025. No 6-K restates covenant compliance. Covenant ratios are therefore Not calculable. | Leverage and liquidity conclusions, CP-2 | Obtain credit agreements, indentures and compliance certificates |
| G2 | High | No instrument-level debt table after December 31, 2025; the September 30, 2026 ladder (total 8,648) cannot be allocated to instruments, currencies or obligors beyond the release percentages (61 percent local currency, 56 percent fixed, 70 percent operating entities). | Debt schedule, refinancing view | Obtain the Financial and Operational Data file or a debt schedule |
| G3 | High | Availability and maturity of the 600 MIC S.A. revolving credit facility at 2026 dates is Not supplied; the 20-F worded the extension two ways (565 versus the full 600 after a joinder, chunks 124, 255). | Liquidity | Confirm drawn amount and maturity |
| G4 | Medium | Management leverage of 2.53x cannot be reproduced; right-of-use depreciation and the pro forma EBITDA bridge are not supplied. Calculations 3 and 4 are simple ratios on reported lines. | Leverage | Request the management bridge |
| G5 | Medium | Unreconciled figures: 9M 2026 operating cash flow 2,028 in the cash flow statement versus 2,019 in the equity free cash flow reconciliation; Q3 6-K note 11 prints 9M 2025 financial expenses of 508 against 507 in the income statement; cash at September 30, 2025 is 1,663 in the cash flow statement and 1,664 in the release; Q1 6-K cash flow opens the year at 1,550 while the balance sheet shows 1,552; Q3 note 8 says joint venture repatriation was 79 in the three months while the cash flow build shows 22 for Q3 and 79 for nine months. Each is small in amount but unexplained. | Cash flow, CP-5 | Carry both values with locators; do not pick one |
| G6 | Medium | Comparative bases differ: the December 31, 2025 balance sheet is restated (for example lease liabilities 2,563 against 2,587), the 2025 interim income statements are re-presented, and the FY2025 income statement and Adjusted EBITDA from the 20-F are not. LTM and year-over-year ratios mix bases. | All trend metrics | State the basis for each ratio |
| G7 | Medium | Q1 and Q3 statements are unaudited and not reviewed; the 2025 comparative income-statement columns in the Q2 6-K are labelled "Not reviewed". | Data quality | Label figures accordingly |
| G8 | Medium | Perimeter break: no pro forma Adjusted EBITDA, cash flow or interest for Coltel, Uruguay and Ecuador. LTM Adjusted EBITDA of 3,734 includes pre-acquisition quarters only in part. Coltel, Ecuador and Chile purchase accounting remain provisional (Q3 6-K chunks 9-14). | Leverage, coverage, growth | Request pro forma figures |
| G9 | Medium | Debt-like items outside gross debt are only partly quantified: capex payables of 2,101 at September 30, 2026 (1,644 plus 457) against 1,198 at December 31, 2025; supplier finance of 163 at December 31, 2025 with no 2026 update; the Guatemala settlement payable of 68; the Celtel Chile earn-out liability of 110 is at an equity-accounted associate; guarantees of 629 at December 31, 2025 with no 2026 update. | Net financing obligations | Request a September 30, 2026 schedule of these items |
| G10 | Medium | Discrete Q2 and Q3 cash interest, dividends and acquisition payments are not printed; Calculation 1 derives quarterly operating cash flow and interest from cumulative figures. Quarterly balance sheets before 2026 and full Q4 2025 and Q2 2025 statements are not supplied. | Quarterly analysis | None possible from this pack |
| G11 | Medium | The cash effect of the Guatemala settlement (99 expense, 31 paid in the quarter, 68 payable over seven years) on operating cash flow or equity free cash flow is Not supplied; it sits below Adjusted EBITDA in other non-operating expenses. A one-time reversal of legal provisions benefited Q3 Guatemala Adjusted EBITDA by an amount that is Not supplied (Q3 6-K chunk 35). | Cash flow quality | Request the amounts |
| G12 | Low | Ratings at the as-of date are Not supplied (context is blank; the 20-F states Moody's Ba2 stable and Fitch BB+ at December 31, 2025, chunk 273). Interest rate sensitivity and the swap notional and maturity detail are Not supplied. | Credit context | Obtain current rating actions |
| G13 | Low | The Financial and Operational Data Excel file referenced in the releases and any presentation are not supplied; no workbook or image content was inspected. | Completeness | Treat as unsupplied |

## Next module

Proceed to CP-1A (business and transaction context), then CP-2 and CP-5 in the order CP-OS sets. CP-1A should use the Colombia (Coltel and EPM buy-out), Chile (Celtel with NJJ), Uruguay, Ecuador, Lati tower-sale and Paraguay mobile-finance disposal facts above, and should carry the covenant, debt-schedule and revolving-facility gaps. CP-2 should treat the management leverage and equity free cash flow guidance as attributed claims and should not describe covenant headroom.
