# CP-1 — Financial statements and credit metrics: Element Solutions Inc (esi)

## Request

- Issuer: Element Solutions Inc (issuer id `esi`, NYSE: ESI), as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD; current period Q3 2026; prior period FY2025 (context). All amounts are USD millions as printed (one decimal), except per-share data and ratios.
- Run: `esi-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Feeds CP-1A, CP-2, CP-5 and the report section "Financials and credit metrics".
- Execution: host session. The host read the pinned page files and wrote this answer. No provider was called. Calculations were done separately from the extracted figures and are listed in `## Calculations`.
- Scope: audited FY2025, FY2024 and FY2023 statements; unaudited statements for Q1, Q2 and Q3 2026 (three-, six- and nine-month columns) with prior-year comparatives; last-twelve-months (LTM) figures built from them; debt, liquidity, issuer non-GAAP measures and the covenant text. No rating, forecast, valuation or pro forma.
- Periods are labelled throughout: Q1, Q2 and Q3 2026 are discrete quarters; nine months 2026 is January to September 2026; LTM is FY2025 plus nine months 2026 less nine months 2025 (and the analogous builds at Q1 and Q2); FY2025 is the audited year to December 31, 2025.

## Sources

| Source | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_esi-20251231.htm.jsonl | e419be4a34b86cf3946781c81c9cf5167d1ce55ea947acb2e97a22e3ec33fbdc | Audited FY2025, FY2024 and FY2023 statements, Note 12 debt, Note 22 segments and Adjusted EBITDA reconciliation (tag K25) |
| 10-Q_2026-03-31_esi-20260331.htm.jsonl | 71ffb0652af7e069b88fd66093decc7d627d9409b00bd185ac2a68db72c238da | Q1 2026 statements, debt, availability, Adjusted EBITDA (tag Q1-26) |
| 10-Q_2026-06-30_esi-20260630.htm.jsonl | 9e356702c38010063835ed61e96bcc033abb0f0a3a4b5a9a1845d764f0bcd2b7 | Q2 and six-month 2026 statements, debt, availability, Adjusted EBITDA (tag Q2-26) |
| 10-Q_2026-09-30_esi-20260930.htm.jsonl | 1efce58ae7d1707b81e096f97ecf01dbf0104d1e81a25b95db794dfd861b04fe | Q3 and nine-month 2026 statements, debt note, covenant, liquidity, segments (tag Q3-26) |
| EX-99.1_2026-04-28_aearningsreleaseex99120263.htm.jsonl | cb75b2ab3988a8e0ad3f68546b2df2a55172fd4900de7f7f14ec3436aa37dbbf | Q1 2026 capital structure and interest paid (tag R1) |
| EX-99.1_2026-07-27_aearningsreleaseex99120266.htm.jsonl | c0a4eea4343eb189f65a5cb896e49cd67b1e5c372bfce79bfb18a89241f92f7e | Q2 2026 capital structure and interest paid (tag R2) |
| EX-99.1_2026-10-21_aearningsreleaseex99120269.htm.jsonl | b36d51c2a20c56990c8361f520b238bac0611bf5a7dab66ba03c7922169d0001 | Q3 2026 capital structure, interest paid, discrete-quarter cash flows, free cash flow, guidance (tag R3) |
| context | 1920ec84f7b9710e00bbaac803890d2695813e40c10637e35f2e7d8eaaf0285a | Run settings: USD; current period q3-2026; prior period fy-2025 |

Supplied handoff consumed: CP-0 sha256 cdece14e2edef04df25761198b67e4d3c88f681db7a403c096bd0cf0d6bf17b7. Carried forward from CP-0: the 10-K and 10-Qs control statement facts; the releases are issuer non-GAAP presentations; debt carrying value and the release's debt table are different bases and CP-1 must state and reconcile the basis it uses (done in C10); revolver capacity and total availability across all lines are different figures; the 2026 acquisitions and their preliminary purchase price allocation limit comparability with FY2025; the Solstice merger was signed and terminated and its termination terms are not supplied; nothing after October 22, 2026 is supplied. CP-0 noted that the 10-K's EFC and Micromax prices are estimates later revised in the Q3 10-Q; this answer uses the Q3 10-Q figures.

Citation format: (tag pN: "exact substring") names the source tag and page chunk. Where a cell names only a tag and page, the figure is on that page.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Debt-funded 2026 acquisitions lifted total debt to Adjusted EBITDA to 3.09x on the last twelve months to Q3 2026, from 2.97x at FY2025. Cash interest cover stayed high at 7.85x. | Medium | Last-twelve-months EBITDA includes the acquired businesses only from their 2026 closing dates, and covenant definitions are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt rose to 2,082.1 from 1,625.9 to fund two acquisitions, while cash fell to 224.9 from 626.5. | Net debt to Adjusted EBITDA is 2.76x against 1.83x at FY2025. | High |
| Quarterly Adjusted EBITDA rose each quarter of 2026, to 191.0 in Q3 2026, with acquisitions and pass-through metals lifting reported sales. | Earnings growth supports deleveraging, but organic sales growth of 13% is well below reported growth of 52%. | Medium |
| Operating cash flow less capital expenditure was 108.8 for nine months 2026, as working capital absorbed cash. | That covers dividends and buybacks of 97.0 but not the 865.8 spent on acquisitions. | Medium |
| The 800.0 senior notes due in 2028 are the first large maturity; cash plus undrawn revolver is 702.9. | The notes depend on cash generation or refinancing before September 1, 2028. | Medium |
| The only financial covenant located is a springing first lien net leverage test of 5.0x, applying when the revolver is over 30% drawn. | It is not triggered at 15.0 drawn of 500; indicative first lien net leverage is 1.59x. | Medium |

### Financial base view

The reported base is clear and current to September 30, 2026. Element Solutions carries total debt of 3.09x LTM Adjusted EBITDA at Q3 2026, but 2026 changed its structure: it bought EFC for cash on hand and Micromax with new term loans, so debt rose by 456.2 and cash fell by 401.6 between December 31, 2025 and September 30, 2026. LTM leverage is therefore overstated relative to a full-year run rate of the acquired businesses, which contribute only from January 2 and February 2, 2026. Separately, Adjusted EBITDA adds back acquisition, integration and transaction costs of 52.6 for nine months 2026, so the ratio flatters cash earnings. Reported net sales growth of 52% in Q3 2026 includes acquisitions and higher pass-through metals prices; organic growth was 13%. Cash generation is thinner than EBITDA growth suggests: nine-month operating cash flow of 192.2 is below the 198.7 of nine months 2025 despite higher Adjusted EBITDA, because receivables and inventories absorbed cash. The 800.0 of senior notes in 2028 and 1,279.7 of term loans in 2030 are the only large maturities, and the revolver was 15.0 drawn at September 30, 2026. Every ratio below is the analyst's calculation on a labelled basis; none is a covenant ratio.

| Area | Position (Q3 2026 unless stated) | Basis |
| --- | --- | --- |
| Earnings | Adjusted EBITDA 673.1 LTM against 547.6 in FY2025 | Issuer non-GAAP, calculated (C1) |
| Leverage | Total debt / Adjusted EBITDA 3.09x; net 2.76x | Debt at carrying value (C4) |
| Coverage | Adjusted EBITDA / cash interest paid 7.85x | Cash interest from the releases and 10-K (C5) |
| Liquidity | Cash 224.9 plus undrawn revolver 478.0 equals 702.9 | Revolver net of letters of credit (C7) |
| Maturities | 800.0 in 2028; 1,279.7 in 2030; 15.0 revolver in 2031 | Face values, release table (C8) |

### Source context

| Source | Entity and perimeter | Periods | Statement kind | Units |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | Element Solutions Inc and subsidiaries, consolidated, with non-controlling interests | Years ended December 31, 2025, 2024 and 2023; balance sheets at December 31, 2025 and 2024 | Audited | "(dollars in millions, except per share amounts)" (K25 p82: "CONSOLIDATED STATEMENTS OF OPERATIONS (dollars in millions, except per share amounts)"); USD |
| 10-Q Q1 2026 | Same consolidated perimeter | Three months ended March 31, 2026 and 2025; balance sheet at March 31, 2026 and December 31, 2025 | Unaudited condensed | Dollars in millions; USD (Q1-26 p4: "(dollars in millions, except per share amounts)") |
| 10-Q Q2 2026 | Same consolidated perimeter | Three and six months ended June 30, 2026 and 2025 | Unaudited condensed | Dollars in millions; USD (Q2-26 p5: "Six Months Ended June 30") |
| 10-Q Q3 2026 | Same consolidated perimeter | Three and nine months ended September 30, 2026 and 2025; balance sheet at September 30, 2026 and December 31, 2025 | Unaudited condensed | Dollars in millions; USD (Q3-26 p5: "Nine Months Ended September 30") |
| Releases (R1, R2, R3) | Same perimeter, issuer presentation | Quarter and year-to-date | Unaudited, non-GAAP additions | Dollars in millions; USD |

### Financials and credit metrics

| Metric | LTM Q3 2026 | FY2025 | FY2024 | Basis and source |
| --- | --- | --- | --- | --- |
| Net sales (USD m) | 3,489.4 | 2,551.2 | 2,456.9 | LTM calculated, C1; FY reported, K25 p82 |
| Operating profit (USD m) | 408.7 | 342.2 | 343.9 | LTM calculated, C1; FY reported, K25 p82 |
| Net income (USD m) | 205.2 | 191.0 | 244.5 | LTM calculated, C1; FY reported, K25 p82; FY2024 includes 1.6 from discontinued operations |
| EBITDA, issuer-defined (USD m) | 564.8 | 470.2 | 501.6 | LTM calculated, C1; FY reported, K25 p124 |
| Adjusted EBITDA, issuer-defined (USD m) | 673.1 | 547.6 | 534.7 | LTM calculated, C1; FY reported, K25 p124 |
| Adjusted EBITDA / net sales (%) | 19.3 | 21.5 | 21.8 | Calculated, C9; the release's own margin uses net sales excluding pass-through metals (Q3 2026: 28.2%) |
| Interest expense, net (USD m) | 81.2 | 53.4 | 56.3 | LTM calculated, C1; FY reported, K25 p82 |
| Cash paid for interest (USD m) | 85.7 | 68.6 | 64.8 | LTM calculated, C3; FY reported, K25 p85 |
| Net cash flows from operating activities (USD m) | 283.3 | 289.8 | 362.0 | LTM calculated, C1; FY reported, K25 p84 |
| Capital expenditures (USD m) | 100.4 | 62.2 | 68.4 | LTM calculated, C1; FY reported, K25 p84 |
| Free cash flow, operating cash flow less capital expenditures (USD m) | 182.9 | 227.6 | 293.6 | Calculated, C6; not the issuer's free cash flow measure |
| Cash and cash equivalents (USD m) | 224.9 | 626.5 | 359.4 | Reported, Q3-26 p6; K25 p83 |
| Total debt, carrying value (USD m) | 2,082.1 | 1,625.9 | 1,824.0 | Reported, Q3-26 p15; K25 p112 |
| Net debt, carrying value less cash (USD m) | 1,857.2 | 999.4 | 1,464.6 | Calculated, C4 |
| Total debt / Adjusted EBITDA (x) | 3.09 | 2.97 | 3.41 | Calculated, C4 |
| Net debt / Adjusted EBITDA (x) | 2.76 | 1.83 | 2.74 | Calculated, C4 |
| Adjusted EBITDA / cash paid for interest (x) | 7.85 | 7.98 | 8.25 | Calculated, C5 |
| Adjusted EBITDA / interest expense, net (x) | 8.29 | 10.25 | 9.50 | Calculated, C5 |
| Total stockholders' equity (USD m) | 2,872.6 | 2,674.5 | 2,383.0 | Reported, Q3-26 p7; K25 p84 |
| Stockholders' equity less goodwill and intangible assets (USD m) | -663.4 | -224.6 | -481.0 | Calculated, C11 |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 3.41 | 2.74 | x | Debt at carrying value, 1,824.0 less cash 359.4; Adjusted EBITDA 534.7 (issuer non-GAAP); C4 |
| FY2025 | 2.97 | 1.83 | x | Debt 1,625.9, cash 626.5; Adjusted EBITDA 547.6; C4 |
| LTM Q1 2026 | 3.71 | 3.40 | x | Debt 2,156.6, cash 177.3; LTM Adjusted EBITDA 581.5; includes EFC and Micromax only from closing; C4 |
| LTM Q2 2026 | 3.37 | 3.07 | x | Debt 2,119.4, cash 189.6; LTM Adjusted EBITDA 629.0; same acquisition limitation; C4 |
| LTM Q3 2026 | 3.09 | 2.76 | x | Debt 2,082.1, cash 224.9; LTM Adjusted EBITDA 673.1; same limitation; on the release's debt table net debt 1,869.8 gives 2.78x; not a covenant ratio |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 8.25 | x | Adjusted EBITDA 534.7 over cash paid for interest 64.8 (K25 p85); C5 |
| FY2025 | 7.98 | x | Adjusted EBITDA 547.6 over cash paid for interest 68.6; C5 |
| LTM Q1 2026 | 8.04 | x | LTM Adjusted EBITDA 581.5 over LTM interest paid 72.3 (releases' "Interest paid"); C5 |
| LTM Q2 2026 | 7.91 | x | LTM Adjusted EBITDA 629.0 over LTM interest paid 79.5; C5 |
| LTM Q3 2026 | 7.85 | x | LTM Adjusted EBITDA 673.1 over LTM interest paid 85.7; interest paid is a cash measure and differs from accrual interest expense, net, of 81.2 LTM; C5 |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 359.4 | Not supplied: the revolver-only unused capacity at December 31, 2024 is not printed; total availability across all lines was approximately 390 | US$m | Cash K25 p83; availability K25 p114 |
| FY2025 | 626.5 | 368.0 | US$m | Revolving credit facility of 375 maturing in 2027, net of letters of credit (K25 p114) |
| Q1 2026 | 177.3 | 408.0 | US$m | Revolver of 500 maturing in 2031 with 85.0 drawn, net of letters of credit (Q1-26 p15) |
| Q2 2026 | 189.6 | 441.0 | US$m | Revolver with 50.0 drawn, net of letters of credit (Q2-26 p19); the printed figure is used as is |
| Q3 2026 | 224.9 | 478.0 | US$m | Revolver with 15.0 drawn, net of letters of credit of 7.0 (Q3-26 p18); of the cash, 176 is held by foreign subsidiaries; total availability across all lines is 506 |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 (remainder) | 0.0 | US$m | No tranche has its final maturity in 2026; face values at September 30, 2026 from the release table (R3 p9). Scheduled term loan installments are inside the 2030 amount; current installments of long-term debt and revolving credit facilities are 27.9, of which 15.0 is revolver borrowing |
| 2027 | 0.0 | US$m | No tranche has its final maturity in 2027; the FY2025 10-K showed a revolver maturing in 2027 that was replaced in February 2026 |
| 2028 | 800.0 | US$m | 3.875% USD Notes due September 1, 2028 (R3 p9; Q3-26 p18) |
| 2029 | 0.0 | US$m | No tranche has its final maturity in 2029; swaps on the term loans mature December 2028 and December 2029, which are not debt maturities |
| 2030 | 1279.7 | US$m | Term loans B-3 maturing December 18, 2030, face value (carrying value 1,270.2 after 9.5 of unamortized discounts and costs, Q3-26 p16) |
| 2031 | 15.0 | US$m | Borrowings under the revolving credit facility, maturing February 2, 2031 in the release's table; classed as current in the balance sheet |

### Reported statements of operations

| Line (as printed) | Q1 2026 | Q2 2026 | Q3 2026 | Nine months 2026 | Nine months 2025 | FY2025 | FY2024 | FY2023 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales | 840.0 | 977.9 | 995.3 | 2,813.2 | 1,875.0 | 2,551.2 | 2,456.9 | 2,333.2 |
| Gross profit | 322.7 | 334.0 | 342.4 | 999.1 | 793.9 | 1,070.5 | 1,035.7 | 918.5 |
| Operating profit | 111.4 | 113.7 | 113.9 | 339.0 | 272.5 | 342.2 | 343.9 | 173.6 |
| Interest expense, net | (21.5) | (24.0) | (22.8) | (68.3) | (40.5) | (53.4) | (56.3) | (49.3) |
| Income before income taxes and non-controlling interests | 82.7 | 107.1 | 93.3 | 283.1 | 234.6 | 265.6 | 287.7 | 129.1 |
| Income tax expense | (26.7) | (29.8) | (27.6) | (84.1) | (49.8) | (74.6) | (44.8) | (13.0) |
| Net income | 56.0 | 77.3 | 65.7 | 199.0 | 184.8 | 191.0 | 244.5 | 118.2 |

Sources: Q1-26 p4, Q2-26 p5 to p6, Q3-26 p5 to p6, K25 p82. Interest expense is printed in parentheses as a deduction and is kept signed. FY2023 operating profit is after an 80.0 goodwill impairment (K25 p82: "Goodwill impairment — — 80.0"). The nine-month 2025 column includes a 59.6 gain on divestitures (Q3-26 p5: "(Loss) gain on divestitures — (7.0) — 59.6"); the three quarters of 2026 add to the nine-month column (C8).

### Reported balance sheet (selected lines)

| Line (as printed) | Sep 30, 2026 | Jun 30, 2026 | Mar 31, 2026 | Dec 31, 2025 | Dec 31, 2024 |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 224.9 | 189.6 | 177.3 | 626.5 | 359.4 |
| Total current assets | 1,576.5 | 1,522.8 | Not extracted | 1,582.5 | 1,270.0 |
| Goodwill | 2,548.7 | 2,537.4 | Not extracted | 2,241.9 | 2,132.0 |
| Intangible assets, net | 987.3 | 1,004.9 | Not extracted | 657.2 | 732.0 |
| Total assets | 5,861.2 | 5,784.2 | 5,737.8 | 5,101.4 | 4,873.9 |
| Current installments of long-term debt and revolving credit facilities | 27.9 | 62.9 | 97.9 | — | 10.4 |
| Debt (long-term) | 2,054.2 | 2,056.5 | 2,058.7 | 1,625.9 | 1,813.6 |
| Pension and post-retirement benefits | 22.2 | 20.7 | Not extracted | 22.3 | 22.2 |
| Total liabilities | 2,974.1 | 2,956.9 | 2,988.0 | 2,412.0 | 2,475.5 |
| Total stockholders' equity | 2,872.6 | 2,812.7 | Not extracted | 2,674.5 | 2,383.0 |

Sources: Q3-26 p6 to p7, Q2-26 p6 to p7, Q1-26 p5, K25 p83 to p84. "Not extracted" means the line was not opened for this answer; it is not zero. Total liabilities at September 30, 2026 equal the printed components (C8).

### Reported cash flows (selected lines)

| Line (as printed) | Q1 2026 | Q2 2026 | Q3 2026 | Nine months 2026 | Nine months 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net cash flows provided by (used in) operating activities | (66.6) | 99.6 | 159.2 | 192.2 | 198.7 | 289.8 | 362.0 |
| Capital expenditures | (25.1) | (27.9) | (30.4) | (83.4) | (45.2) | (62.2) | (68.4) |
| Acquisitions, net of cash acquired | (864.2) | (1.6) | — | (865.8) | — | — | (3.9) |
| Debt proceeds, net of discount | 449.4 | — | — | 449.4 | — | — | 1,040.1 |
| Repayments of borrowings | — | (3.2) | (3.2) | (6.4) | (202.6) | (202.6) | (1,152.6) |
| Changes in lines of credit, net | 85.0 | (35.0) | (35.0) | 15.0 | — | not printed | not printed |
| Repurchases of common stock | — | — | (37.7) | (37.7) | (19.4) | (25.0) | — |
| Dividends | (20.2) | (19.6) | (19.5) | (59.3) | (58.4) | (77.8) | (78.2) |
| Cash paid for interest ("Interest paid" in the releases) | 29.1 | 16.0 | 31.1 | 76.2 | 59.1 | 68.6 | 64.8 |

Sources: the discrete-quarter 2026 columns are from the Q3 release's cash flow statement (R3 p8: "Capital expenditures (30.4) (27.9) (25.1)"); nine months from Q3-26 p7; FY from K25 p84 to p85; interest paid from R1 p9, R2 p11 and R3 p9. The 10-Qs print only year-to-date cash flows, so the discrete quarters are attributed to the release. They add to the nine-month column (C8).

### Debt register at September 30, 2026

| Instrument (as printed) | Final maturity | Rate | Carrying value | Face value |
| --- | --- | --- | --- | --- |
| Term Loans (term loans B-3) | 2030 (December 18, 2030) | SOFR plus 1.75% | 1,270.2 | 1,279.7 |
| Senior Notes - $800 million (3.875% USD Notes due 2028) | 2028 (September 1, 2028) | 3.875% | 796.9 | 800.0 |
| Borrowings under the Revolving Credit Facility ($500 million commitment) | 2031 | SOFR plus 1.50% | 15.0 | 15.0 |
| Total debt | — | — | 2,082.1 | 2,094.7 |
| Less: current installments of long-term debt and revolving credit facilities | — | — | 27.9 | — |
| Total long-term debt | — | — | 2,054.2 | — |

Sources: carrying values Q3-26 p15 ("Total debt 2,082.1 1,625.9"); face values and dates R3 p9. Security and guarantees: the Credit Agreement debt is secured on a first-priority basis and guaranteed by certain domestic subsidiaries (Q3-26 p16: "secured by a first-priority security interest in substantially all of their assets"); the senior notes are guaranteed on a senior unsecured basis by generally the same subsidiaries (Q3-26 p18). The term loans bear an effective rate of 4.4% including swaps and net investment hedges, and about 94% of debt is fixed (R3 p9: "approximately 94% of the Company's debt was fixed"). Other facilities: lines of credit and overdraft facilities of 15.0 outstanding at September 30, 2026 (Q3-26 p18: "totaled $15.0 million"); this equals the revolver borrowing figure and the 10-Q does not say whether it is the same 15.0; total debt contains one 15.0 (see gaps).

### Liquidity at September 30, 2026

| Component (as printed) | Amount (USD m) | Source |
| --- | --- | --- |
| Cash and cash equivalents | 224.9 | Q3-26 p6 |
| Revolving credit facility commitment | 500.0 | Q3-26 p16 |
| Less borrowings under the revolving credit facility | (15.0) | Q3-26 p15 |
| Less letters of credit | (7.0) | Q3-26 p46 |
| Unused revolver capacity, net of letters of credit | 478.0 | Q3-26 p18 |
| Cash plus unused revolver capacity | 702.9 | Calculated, C7 |
| Memo: availability across revolver, lines of credit and overdrafts | 506 | Q3-26 p46 |

The 506 includes facilities beyond the 500 committed revolver; this answer counts only the committed revolver as undrawn committed capacity. Management states that cash, operating cash flow and availability will cover "working capital needs, interest payments, capital expenditures" for at least twelve months (Q3-26 p44: "at least the next twelve months"). Full-year 2026 capital expenditure is expected to be approximately 110 (Q3-26 p44), up from the 75.0 expected in the 10-K (K25 p66: "approximately $75.0 million").

### Issuer non-GAAP measures

| Line (as printed) | Q1 2026 | Q2 2026 | Q3 2026 | Nine months 2026 | Nine months 2025 | FY2025 |
| --- | --- | --- | --- | --- | --- | --- |
| Net income | 56.0 | 77.3 | 65.7 | 199.0 | 184.8 | 191.0 |
| Income tax expense | 26.7 | 29.8 | 27.6 | 84.1 | 49.8 | 74.6 |
| Interest expense, net | 21.5 | 24.0 | 22.8 | 68.3 | 40.5 | 53.4 |
| Depreciation expense | 14.5 | 15.2 | 14.8 | 44.5 | 29.7 | 41.1 |
| Amortization expense | 28.0 | 29.5 | 30.3 | 87.8 | 84.3 | 110.1 |
| EBITDA | 146.7 | 175.8 | 161.2 | 483.7 | 389.1 | 470.2 |
| Acquisition, integration and transaction expenses | 20.1 | 10.6 | 21.9 | 52.6 | 22.6 | 34.9 |
| Unrealized (gains) losses on metals derivative contracts | (21.7) | (8.0) | 11.8 | (17.9) | 13.3 | 16.7 |
| Adjusted EBITDA | 162.3 | 183.5 | 191.0 | 536.8 | 411.3 | 547.6 |

Sources: Q1-26 p23, Q2-26 p27 to p28, Q3-26 p27, K25 p124. Only two of the adjustment lines are shown; the others (restructuring, inventory step-up, foreign exchange on intercompany loans, divestitures, debt financing costs, contingent consideration, other) are in the cited reconciliations and are included in the totals (C8). FY2025 also adds back 37.1 of "2025 executive share grants" (K25 p124: "2025 executive share grants 37.1"). Segment Adjusted EBITDA for Q3 2026 is Electronics 148.3 and Specialties 42.7; for nine months 2026, Electronics 408.9 and Specialties 127.9 (Q3-26 p27: "Adjusted EBITDA $ 148.3 $ 42.7 $ 191.0").

### Segments and sales drivers

| Item | Q3 2026 | Q3 2025 | Nine months 2026 | Nine months 2025 | Source |
| --- | --- | --- | --- | --- | --- |
| Electronics net sales | 779.6 | 465.2 | 2,180.1 | 1,298.9 | Q3-26 p26 |
| Specialties net sales | 215.7 | 190.9 | 633.1 | 576.1 | Q3-26 p26 |
| Micromax net sales (within Electronics) | 137.8 | — | 331.2 | — | Q3-26 p26 |
| EFC net sales (within Specialties) | 23.4 | — | 58.1 | — | Q3-26 p26 |
| Pass-through metals in Electronics net sales | 318.5 | 125.0 | 891.6 | 339.7 | R3 p8 |
| Electronics Adjusted EBITDA | 148.3 | 101.5 | 408.9 | 286.9 | Q3-26 p27 |
| Specialties Adjusted EBITDA | 42.7 | 45.4 | 127.9 | 124.4 | Q3-26 p27 |

The release reconciles reported to organic growth: total net sales growth of 52% in Q3 2026 comprises a change in pass-through metals pricing of (14)% and acquisitions of (25)%, leaving organic growth of 13% (R3 p11: "Total 52% 0% (14)% (25)% 13%"). Specialties Adjusted EBITDA fell in Q3 2026 against Q3 2025 even with the EFC acquisition contributing (R3 p4: "Specialties: Adjusted EBITDA was $43 million, a decrease of 6%").

### Claims outside debt

| Claim | Amount | Inside or outside the debt figure | Source |
| --- | --- | --- | --- |
| Operating lease liabilities (present value) | 86.0 at December 31, 2025 | Outside; not updated in the 10-Qs | K25 p121 |
| Pension and post-retirement benefits (balance sheet) | 22.2 at September 30, 2026 | Outside | Q3-26 p7 |
| EFC contingent consideration | 19.5 fair value, up to 30.0 cash or 1.16 million shares | Outside | Q3-26 p21 and p22 |
| Kuprion milestone payment, paid in Q4 2026 | 9.7 | Outside; subsequent to the balance sheet date | Q3-26 p15 |
| Environmental accruals | 13.4 | Outside | Q3-26 p24 |
| Mariposa Capital advisory fee | 2.0 per year to May 5, 2029 | Outside | Q3-26 p26 |
| Share repurchase authorization remaining | approximately 518 | Discretionary; outside | Q3-26 p22 |
| Interest rate and cross-currency swaps | Notional 1.17 billion; net swap liabilities and assets are in other liabilities and other assets | Outside; they convert term loan exposure to fixed euro | Q3-26 p20 |

No factoring, supply-chain finance or purchase-commitment table was located in the pages opened; Not supplied for the Q3 10-Q pages read. The 10-K refers to purchase commitments only in a risk factor (K25 p25).

### Covenants and financial terms

| Term | Description | Source |
| --- | --- | --- |
| Revolving credit facility maintenance test | "the Company's first lien net leverage ratio should not exceed 5.0 to 1.0, subject to a right to cure" when revolver borrowings exceed 30% of the commitment | Q3-26 p17 |
| Compliance | "At September 30, 2026, the Company was in compliance with the debt covenants contained in the Credit Agreement" | Q3-26 p18: "was in compliance with the debt covenants contained in the Credit Agreement" |
| Senior notes | Customary indenture covenants; compliance stated | Q3-26 p46: "we were in compliance with the debt covenants" |
| Negative covenants | Limits on additional indebtedness, dividends and distributions, restricted payments, liens, asset sales, among others | Q3-26 p16: "limitations on additional indebtedness, dividends, and other distributions" |
| Change of control | Event of default under the Credit Agreement | Q3-26 p18: "change of control provisions" |

Headroom against the covenant as defined is Not calculable: the Credit Agreement's definitions of first lien net leverage, EBITDA and net debt are not supplied, and no issuer-reported ratio is printed. Indicatively, first lien debt (revolver plus term loans, release table 1,294.7) less cash 224.9 over LTM Adjusted EBITDA 673.1 is 1.59x (C12); the test applies only above a revolver draw of 150.0, and 15.0 was drawn (C12). This indicative ratio is not the covenant ratio.

### Narrative review

- Leverage: total debt to LTM Adjusted EBITDA was 3.09x at Q3 2026, down from 3.71x at Q1 2026 and 3.37x at Q2 2026 but above 2.97x at FY2025. Mechanism: the add-on term loans of 449.4 (net of discount) and a revolver draw funded Micromax while EFC was paid from cash on hand, so debt rose and cash fell while LTM EBITDA includes the acquired businesses only partly. Implication: from Q1 2026 to Q3 2026 the ratio fell mainly because LTM Adjusted EBITDA rose from 581.5 to 673.1, helped by net revolver repayment of 70.0 across Q2 and Q3 2026 (R3 p8: "Changes in lines of credit, net (35.0) (35.0) 85.0"); term loan repayments were only 6.4 in nine months 2026.
- Coverage: Adjusted EBITDA covered cash interest paid 7.85x on the LTM basis, slightly below 7.98x at FY2025, as interest paid rose to 85.7 LTM. Accrual interest expense, net, rose 68.6% in nine months 2026 against nine months 2025. Interest cost is partly fixed through swaps (about 94% of debt fixed per the release), so a rise in SOFR has limited effect, but the euro-denominated swap legs add foreign exchange sensitivity.
- Cash flow quality: nine-month operating cash flow of 192.2 was 35.8% of Adjusted EBITDA of 536.8, against 48.3% in nine months 2025, because rising metals prices tied up working capital (receivables outflow 137.3, inventories 80.7). Q3 2026 alone was 159.2, after 99.6 in Q2 2026 and an outflow of 66.6 in Q1 2026. The 10-Q attributes the nine-month shortfall to "higher investment in working capital from rising metals prices" (Q3-26 p45). Implication: cash conversion is seasonal and metals-price dependent; it rebounded in Q3 2026.
- Liquidity: 702.9 of cash plus undrawn revolver against a first large maturity of 800.0 on September 1, 2028. Cash of 224.9 is mostly (176) held by foreign subsidiaries, so it is not all available to the U.S. borrowers without transfer cost.
- Earnings trend: Adjusted EBITDA rose each quarter in 2026 (162.3, 183.5, 191.0) and management raised 2026 guidance to approximately 720 (R3 p2, guidance, not a reported figure). Specialties Adjusted EBITDA fell year on year in Q3 2026.
- Data quality: the quarterly columns add to the nine-month columns; the Adjusted EBITDA reconciliations add exactly; carrying and face debt reconcile to the stated discounts and costs (C8, C10).
- Definition risks: issuer Adjusted EBITDA adds back acquisition, integration and transaction costs (52.6 for nine months 2026, 34.9 for FY2025), FY2025 executive share grants (37.1), restructuring and other items, and excludes unrealized metals derivative results. The Q3 2026 acquisition cost line may include costs of the terminated Solstice merger; the split is not supplied. Covenant EBITDA is defined in the Credit Agreement, not supplied.
- Key gaps: Credit Agreement and indenture; Termination Agreement; pro forma EBITDA for the acquisitions; covenant ratio; operating lease update after December 31, 2025.

### Readiness for downstream modules

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1A | Sufficient for business, segment and capital-structure description | Statements, segments, debt register and 2026 transactions above |
| CP-2 | Sufficient with limitations | Leverage, coverage and liquidity on labelled bases; covenant ratio Not calculable; LTM is not pro forma for acquisitions |
| CP-5 | Sufficient | Every figure has a source tag and page or a calculation ID |

### Quality review of claims

| Claim | Material | Lineage | Note |
| --- | --- | --- | --- |
| Total debt / LTM Adjusted EBITDA is 3.09x | Yes | Calculated | Debt at carrying value; LTM is not pro forma for the acquisitions |
| Net debt / LTM Adjusted EBITDA is 2.76x | Yes | Calculated | Release net debt 1,869.8 gives 2.78x on face-value debt |
| Adjusted EBITDA / cash interest paid is 7.85x | Yes | Calculated | Interest paid from releases; 10-K label "Cash paid for interest" assumed the same measure |
| Cash plus undrawn revolver is 702.9 | Yes | Calculated | Committed revolver only; 506 total availability is wider |
| In compliance with covenants | Yes | Directly Sourced | Management statement, Q3-26 p18 |
| Covenant headroom | Yes | Insufficient Information | Agreement definitions not supplied; indicative 1.59x is not the covenant ratio |

Open quality findings: one MATERIAL finding, LTM EBITDA is not pro forma for EFC and Micromax so LTM leverage is overstated relative to a full-year run rate; one MINOR finding, the 10-K and releases label cash interest differently ("Cash paid for interest" and "Interest paid").

## Calculations

All inputs are USD millions copied from the cited pages. Ratios are rounded half up to two decimals and percentages to one decimal. LTM Q3 2026 = FY2025 + nine months 2026 − nine months 2025.

| ID | Formula | Inputs and locators | Result |
| --- | --- | --- | --- |
| C1 | LTM = FY2025 + 9M 2026 − 9M 2025 | Net sales 2,551.2 + 2,813.2 − 1,875.0; operating profit 342.2 + 339.0 − 272.5; net income 191.0 + 199.0 − 184.8; interest expense, net 53.4 + 68.3 − 40.5; EBITDA 470.2 + 483.7 − 389.1; Adjusted EBITDA 547.6 + 536.8 − 411.3; operating cash flow 289.8 + 192.2 − 198.7; capital expenditures 62.2 + 83.4 − 45.2 (K25 p82, p84, p124; Q3-26 p5, p7, p27) | 3,489.4; 408.7; 205.2; 81.2; 564.8; 673.1; 283.3; 100.4 |
| C2 | LTM Adjusted EBITDA at Q1 and Q2 | Q1: 547.6 + 162.3 − 128.4. Q2: 547.6 + 345.8 − 264.4 (Q1-26 p23; Q2-26 p28) | 581.5; 629.0 |
| C3 | LTM cash interest paid | Q1: 68.6 + 29.1 − 25.4. Q2: 68.6 + 45.1 − 34.2. Q3: 68.6 + 76.2 − 59.1 (K25 p85; R1 p9; R2 p11; R3 p9) | 72.3; 79.5; 85.7 |
| C4 | Total debt / Adjusted EBITDA; (total debt − cash) / Adjusted EBITDA | FY2024: 1,824.0 / 534.7; (1,824.0 − 359.4) = 1,464.6 / 534.7. FY2025: 1,625.9 / 547.6; 999.4 / 547.6. Q1 2026: 2,156.6 / 581.5; 1,979.3 / 581.5. Q2 2026: 2,119.4 / 629.0; 1,929.8 / 629.0. Q3 2026: 2,082.1 / 673.1; 1,857.2 / 673.1. Debt: K25 p112; Q1-26 p13; Q2-26 p16; Q3-26 p15 | 3.41x, 2.74x; 2.97x, 1.83x; 3.71x, 3.40x; 3.37x, 3.07x; 3.09x, 2.76x |
| C5 | Adjusted EBITDA / cash interest paid; Adjusted EBITDA / interest expense, net | FY2024: 534.7 / 64.8; 534.7 / 56.3. FY2025: 547.6 / 68.6; 547.6 / 53.4. Q1: 581.5 / 72.3. Q2: 629.0 / 79.5. Q3: 673.1 / 85.7; 673.1 / 81.2 | 8.25x; 9.50x. 7.98x; 10.25x. 8.04x. 7.91x. 7.85x; 8.29x |
| C6 | Operating cash flow less capital expenditures | LTM 283.3 − 100.4; FY2025 289.8 − 62.2; FY2024 362.0 − 68.4; nine months 2026 192.2 − 83.4 | 182.9; 227.6; 293.6; 108.8 |
| C7 | Cash plus unused revolver capacity; revolver check | Q3 2026: 224.9 + 478.0. Q2: 189.6 + 441.0. Q1: 177.3 + 408.0. FY2025: 626.5 + 368.0. Revolver check at Q3: 500.0 − 15.0 − 7.0 | 702.9; 630.6; 585.3; 994.5; 478.0 |
| C8 | Internal consistency | Quarterly net sales 840.0 + 977.9 + 995.3; Adjusted EBITDA 162.3 + 183.5 + 191.0; operating cash flow −66.6 + 99.6 + 159.2; capex 25.1 + 27.9 + 30.4. Nine-month Adjusted EBITDA: 483.7 + 5.8 + 7.4 + 52.6 − 13.1 − 17.9 + 3.4 + 14.9 (Q3-26 p27). FY2025: 470.2 + 5.6 + 34.9 + 28.2 − 59.0 + 16.7 + 1.8 + 37.1 + 12.1 (K25 p124). Q3 2026 total liabilities 566.6 + 2,054.2 + 22.2 + 104.5 + 226.6 (Q3-26 p7). Face debt 15.0 + 1,279.7 + 800.0 (R3 p9) | 2,813.2; 536.8; 192.2; 83.4, each equal to the printed nine-month figure. 536.8 and 547.6, equal to printed. 2,974.1, equal to printed. 2,094.7, equal to printed total debt |
| C9 | Adjusted EBITDA / net sales | 673.1 / 3,489.4; 547.6 / 2,551.2; 534.7 / 2,456.9 | 19.3%; 21.5%; 21.8% |
| C10 | Debt basis bridge | Face 2,094.7 − carrying 2,082.1; the 10-Q states unamortized discounts and issuance costs of 12.6 (Q3-26 p46: "net of unamortized discounts and debt issuance costs of $12.6 million"). Net debt on face basis: 2,094.7 − 224.9; 1,869.8 / 673.1 | 12.6, equal to the stated 12.6; 1,869.8, equal to the release's net debt (R3 p9); 2.78x |
| C11 | Stockholders' equity less goodwill and intangible assets | Q3 2026: 2,872.6 − 2,548.7 − 987.3. FY2025: 2,674.5 − 2,241.9 − 657.2. FY2024: 2,383.0 − 2,132.0 − 732.0 (Q3-26 p6 to p7; K25 p83 to p84) | −663.4; −224.6; −481.0 |
| C12 | Indicative first lien net leverage and revolver trigger | (1,294.7 − 224.9) / 673.1. Utilization 15.0 / 500.0. Trigger 30% × 500.0 = 150.0; unused before trigger 150.0 − 15.0 (Q3-26 p17; R3 p9) | 1.59x; 3.0%; 150.0; 135.0 |
| C13 | Growth and conversion | Q3 net sales 995.3 / 656.1 − 1; nine-month Adjusted EBITDA 536.8 / 411.3 − 1; nine-month interest expense, net 68.3 / 40.5 − 1; operating cash flow / Adjusted EBITDA 192.2 / 536.8 and 198.7 / 411.3; change in debt 2,082.1 − 1,625.9; change in cash 626.5 − 224.9; 800.0 − 702.9; dividends plus buybacks 59.3 + 37.7 | 51.7%, consistent with the release's 52%; 30.5%; 68.6%; 35.8% and 48.3%; 456.2; 401.6; 97.1; 97.0 |

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| LTM Adjusted EBITDA is not pro forma for EFC (closed January 2, 2026) and Micromax (closed February 2, 2026); no pro forma EBITDA is printed | LTM leverage and cover are overstated or understated relative to a run rate; the 2026 guidance of approximately 720 is forward-looking and is not used | Treat ratios as reported-basis; request pro forma EBITDA from management or the credit agreement compliance certificate |
| Credit Agreement and indenture not supplied; first lien net leverage is not printed | Covenant headroom Not calculable; indicative 1.59x is not the covenant ratio | Supply the executed documents |
| Releases' "Interest paid" assumed to be the same measure as the 10-K "Cash paid for interest" | LTM cash interest may differ slightly | Treat the cover ratio as approximate |
| Discrete Q1, Q2 and Q3 2026 cash flows come from the Q3 release; the 10-Qs print year-to-date | Quarterly cash flow is attributed to an issuer presentation | Label; reconcile to the 10-Qs (done at nine months, C8) |
| Revolver-only unused capacity at December 31, 2024 not printed | FY2024 liquidity row is incomplete | Not required for the current view |
| Balance sheet lines for March 31, 2026 other than cash, total assets, debt and total liabilities not extracted | Q1 balance sheet detail incomplete | Open Q1-26 p5 if needed |
| No scheduled debt maturity table after the February 2026 add-on; term loan installments by year not printed | Annual maturity wall below the 2030 bullet is unsplit | Request the amortization schedule; current installments of term loans are 12.9 by difference of 27.9 and 15.0 |
| Operating lease and purchase commitment data are as of December 31, 2025 only | Claims outside debt not updated for acquired leases | Check the 10-K for 2026 update when filed |
| Solstice transaction costs and any termination payment not separable from acquisition, integration and transaction expenses | Quality of the add-back cannot be tested | Supply the Termination Agreement and cost breakdown |
| Pages not opened (risk factors, pension detail, tax, environmental, most business pages) | Residual undisclosed items are possible | Downstream modules open pages they need |

## Next module

- CP-1A: carry the 2026 acquisitions (EFC 366.6 cash, Micromax 494.3 cash, per Q3-26 p13), the segment table, the Solstice signing and termination, and the financing of Micromax with the add-on term loans into the transaction and profile sections.
- CP-2: read leverage on the carrying-value basis and the face-value basis (3.09x and about 3.11x total; 2.76x and 2.78x net), note that LTM EBITDA is not pro forma, carry the 800.0 notes due in 2028, the springing 5.0x first lien test and its 30% trigger, and the foreign-held cash.
- CP-5: trace every figure to its tag and page or calculation ID; keep the Adjusted EBITDA add-backs and the metals pass-through effect visible as definition risks.
