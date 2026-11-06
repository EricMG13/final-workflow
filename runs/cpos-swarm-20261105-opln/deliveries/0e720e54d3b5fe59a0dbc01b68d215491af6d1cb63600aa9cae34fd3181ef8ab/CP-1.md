## Request

Module CP-1, financial and credit data base, for OPENLANE, Inc. (issuer id opln, NYSE: OPLN), pathway credit_snapshot, as-of date 2026-11-05, evidence cutoff 2026-11-05, reporting currency USD. The module builds the reported-fact base, the debt, liquidity, covenant and cash-flow picture, and the four chart tables, from the pinned filings and slide decks. Periods follow the context (current q3-2026, prior fy-2025) and are labelled as the filings print them: Q3 2026, nine months 2026 (9M 2026), LTM Q3 2026 (twelve months ended September 30, 2026), FY2025 and FY2024. All amounts are USD millions unless a line says otherwise; the Canadian dollar and euro appear only as facility sizes. The perimeter is OPENLANE, Inc. consolidated, which includes the Finance segment (AFC) and its consolidated securitization vehicles.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Use |
| --- | --- | --- |
| 10-K_2025-12-31_opln-20251231.htm.jsonl | 26a1eb6e044eb7884447c1771579bc95b55527d93c8454714335cfb05faebcc7 | Audited FY2025 and FY2024 statements, debt, contractual obligations, quarterly 2025 EBITDA reconciliation |
| 10-Q_2026-03-31_opln-20260331.htm.jsonl | c46e877ea2548ae22544a835acae1b3618984f266ca5c5f8d9f1ce170a2f3661 | Q1 2026 balance sheet, debt, liquidity, covenant ratio, LTM reconciliation |
| 10-Q_2026-06-30_opln-20260630.htm.jsonl | 47753528b639818941177074a5796fb5ee4c271e3e7cb89f9ddc4bf548a73b8f | Q2 2026 balance sheet, debt, liquidity, covenant ratio, LTM reconciliation |
| 10-Q_2026-09-30_opln-20260930.htm.jsonl | 9682e191d9ec651d5722722ac8ff03e1ea87ff7ece0722d12fcb449d04d13357 | Q3 2026 and 9M 2026 statements, debt, securitization, liquidity, covenant, LTM reconciliation, subsequent event |
| EX-99.3_2026-05-05_q12026openlaneearningssl.htm.jsonl | 2fc56068f78381bd02bfbe329da47d9ab40d86ee26db869d39406949616dc5f0 | Q1 2026 slides (read for dates and Q1 reconciliation only) |
| EX-99.3_2026-08-04_q22026openlaneearningssl.htm.jsonl | 458d3c1fac99aaeefe126a46b683e88ca11580e6032ddf67da49e980bf2bff5d | Q2 2026 slides (read for dates and Q2 reconciliation only) |
| EX-99.3_2026-11-04_q32026openlaneearningssl.htm.jsonl | bc88d193632549ac9eb968d3349190fc1ffa3b0842d97894dce16151e37cfd9a | Q3 2026 slides: segment Adjusted EBITDA by quarter, revised 2026 guidance |

### Other pinned input

| Input | sha256 | Use |
| --- | --- | --- |
| context | 2fd2835b16fcd6e36fa06485261ee15d20c3a0b3f6cb56cfce407e6993d9ef70 | Run settings only; not issuer evidence. Ratings, market data, deal terms and peers are blank, and blank is not zero. |

### Handoffs

| Module | sha256 | Note |
| --- | --- | --- |
| CP-0 | 822af9f32f30d6c0feeb6f1f36ee177a40b0f0ee61b0286bf38226d8998cb018 | Source readiness. Opened and used: its view for this module is READY_WITH_LIMITATIONS; limitations G1 (executed agreements not supplied), G3 (deck charts not extracted), G4 (December 31, 2025 collateral figure corrected) and G6 (flattened tables) are carried into this module's Gaps. |

Short names: 10-K FY2025, 10-Q Q1, 10-Q Q2, 10-Q Q3, Deck Q1, Deck Q2, Deck Q3, in the order of the source table. A locator `page:N` is the source chunk number in the pinned file, not the printed page. Quotes are exact substrings of the cited chunk. Where a figure is described as calculated, the formula and inputs are in Calculations.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Corporate debt is one term loan with undrawn revolvers, and leverage on company Adjusted EBITDA is 1.43x at LTM Q3 2026. The larger funding is the securitization of finance receivables, which sits outside that debt figure. | Medium | The credit agreement and securitization agreements are not supplied, so covenant definitions and undrawn securitization capacity cannot be tested. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt to Adjusted EBITDA is 1.43x at LTM Q3 2026, against 1.65x at FY2025. Net of cash it is 0.79x. | Corporate leverage is low, but it rests on a company EBITDA measure that already deducts securitization interest. | Medium |
| Securitization obligations are 2,084.4 gross at September 30, 2026, against term debt of 545.9. | Most funding is secured on finance receivables, so a reader using only term debt understates funded obligations. | High |
| Cash plus undrawn revolver availability is 650.2 at September 30, 2026, up from 551.4 at December 31, 2025. | Corporate liquidity is ample against 5.5 of annual term-loan amortization and no revolver borrowings. | High |
| Nine-month free cash flow is 268.8, but receivable growth absorbed 367.6 of investing cash. | Cash generation depends on securitization funding growth in the receivable book. | Medium |
| Corporate interest, net of interest income, is 37.3 for LTM Q3 2026 against 14.9 for FY2025. | The October 2025 term loan raised the interest burden, so FY2025 cover understates the current run-rate. | High |

### Financial base view

The reported base is complete enough for credit work on OPENLANE, Inc.: audited FY2025 and FY2024 statements, three unaudited 2026 interim filings through September 30, 2026, and a company-printed LTM reconciliation at each 2026 quarter-end that matches the sum of quarters. The base separates three claims that a single leverage number would blur. First, corporate debt: one term loan of 545.9 and revolvers with no borrowings. Second, securitization obligations of 2,084.4 gross that fund the Finance segment's floorplan receivables and are accounted for as secured borrowings. Third, equity-like claims, namely the Series A preferred that was fully converted in May 2026. Company Adjusted EBITDA deducts securitization interest, so ratios on it use corporate debt only; ratios on unadjusted EBITDA use total cash interest. Both bases are shown and not mixed. All ratios below are the analyst's calculations from printed inputs and differ from the covenant ratio the company reports, whose definition rests on an agreement that is not supplied. Restrictions carried forward: covenant definitions, securitization capacity and the Third Amendment to the Credit Agreement cannot be verified from the pack.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 0.79 | 0.30 | x | Total debt 230.7 at December 31, 2024 over FY2024 company Adjusted EBITDA 293.4; net of cash and cash equivalents 143.0, restricted cash excluded. Excludes obligations collateralized by finance receivables. Calculated. |
| FY2025 | 1.65 | 1.23 | x | Total debt 550.0 over FY2025 Adjusted EBITDA 332.6; cash and cash equivalents 141.5. Same basis. The 550.0 term loan was drawn in October 2025. Calculated. |
| LTM Q1 2026 (twelve months ended March 31, 2026) | 1.64 | 1.12 | x | Total debt 568.0 (term loan plus European lines drawn) over LTM Adjusted EBITDA 346.5; cash and cash equivalents 180.1. Calculated. |
| LTM Q2 2026 (twelve months ended June 30, 2026) | 1.51 | 0.98 | x | Total debt 547.2 over LTM Adjusted EBITDA 363.0; cash and cash equivalents 189.7. Calculated. |
| LTM Q3 2026 (twelve months ended September 30, 2026) | 1.43 | 0.79 | x | Total debt 545.9 over LTM Adjusted EBITDA 382.7; cash and cash equivalents 244.9. The company reports a covenant ratio of 0.9 on its own definition. Securitization obligations of 2,084.4 gross are excluded because Adjusted EBITDA already deducts securitization interest. Calculated. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 2.82 | x | Company EBITDA 396.8 over cash paid for interest 140.7. Cash interest covers corporate and securitization interest; the filings do not split it. Calculated. |
| FY2025 | 3.54 | x | Company EBITDA 408.7 over cash paid for interest 115.4. The term loan carried interest for only the last quarter. Calculated. |
| LTM Q1 2026 | 3.46 | x | LTM EBITDA 425.0 over LTM cash interest 122.7 (FY2025 less Q1 2025 plus Q1 2026). Calculated. |
| LTM Q2 2026 | 3.55 | x | LTM EBITDA 440.2 over LTM cash interest 123.9. Calculated. |
| LTM Q3 2026 | 3.42 | x | LTM EBITDA 451.5 over LTM cash interest 132.1. EBITDA here is before the securitization-interest deduction that Adjusted EBITDA makes, which matches cash interest that includes securitization interest. On Adjusted EBITDA the ratio is 2.90. Calculated. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| December 31, 2025 | 141.5 | 409.9 | US$m | Cash and cash equivalents, restricted cash of 43.9 excluded. Undrawn is the Revolving Credit Facilities availability, net of 42.6 of letters of credit. As printed. |
| March 31, 2026 | 180.1 | 408.2 | US$m | Same basis. Letters of credit 42.6. As printed. |
| June 30, 2026 | 189.7 | 405.7 | US$m | Same basis. Letters of credit 42.6. As printed. |
| September 30, 2026 | 244.9 | 405.3 | US$m | Same basis; restricted cash of 34.7 excluded. Excludes the securitization committed capacity (US$2.0 billion and C$500 million), whose undrawn amount is Not calculable from the pack, and the European lines of 45.3, which the filing does not call committed. Both revolvers mature June 23, 2028. As printed. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q4 2026 | 1.4 | US$m | Analyst schedule: one quarterly installment of 0.25% of the original 550.0 term loan (1.375). Assumes installments on each quarter-end from March 31, 2026 and no prepayment. The filings do not print a maturity table at September 30, 2026. |
| 2027 | 5.5 | US$m | Four installments of 1.375. Same assumption. |
| 2028 | 5.5 | US$m | Four installments. Revolvers (325 and C$175 million) mature June 23, 2028 with no borrowings. |
| 2029 | 5.5 | US$m | Four installments. |
| 2030 | 5.5 | US$m | Four installments. The U.S. and Canadian securitization facilities expire January 31, 2030; they are revolving, and their gross balance of 2,084.4 is not scheduled. |
| 2031 | 5.5 | US$m | Four installments. |
| 2032 | 517.0 | US$m | Three installments of 1.375 (4.125) plus the balance of 512.875 due October 8, 2032. Sum of the schedule is 545.9, the term loan at September 30, 2026. |

### Financials and credit metrics

| Metric (USD millions unless stated) | FY2025 | Q3 2025 | Q3 2026 | 9M 2025 | 9M 2026 | LTM Q3 2026 | Source and basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total operating revenues | 1,934.5 | 498.4 | 561.2 | 1,440.2 | 1,643.7 | 2,138.0 | 10-K FY2025 page:91; 10-Q Q3 page:2; LTM calculated (FY2025 less 9M 2025 plus 9M 2026) |
| Operating profit | 196.6 | 55.0 | 70.4 | 154.1 | 211.7 | 254.2 | Same pages; LTM calculated |
| Finance interest expense (within operating expenses) | 109.9 | 28.1 | 28.2 | 82.6 | 78.7 | 106.0 | Same pages; LTM printed at 10-Q Q3 page:59 |
| Interest expense (corporate, below operating profit) | 18.1 | 1.1 | 10.0 | 8.2 | 30.1 | 40.0 | Same pages; LTM calculated |
| Net income | 177.7 | 47.9 | 44.7 | 118.2 | 137.9 | 197.4 | Same pages; LTM calculated and equal to the printed 197.4 at 10-Q Q3 page:59 |
| EBITDA (company definition) | 408.7 | 107.5 | 118.8 | 316.8 | 359.6 | 451.5 | 10-K FY2025 page:79; 10-Q Q3 page:58 to page:59; LTM printed |
| Adjusted EBITDA (company, after securitization interest) | 332.6 | 87.1 | 106.8 | 256.6 | 306.7 | 382.7 | Same pages; LTM printed |
| Net cash provided by operating activities | 391.9 | 72.2 | 97.1 | 266.4 | 309.5 | 435.0 | 10-K FY2025 page:93; 10-Q Q3 page:4; quarters from Deck Q3 page:8; LTM calculated |
| Purchases of property, equipment and computer software | 55.4 | 14.6 | 13.8 | 40.7 | 40.7 | 55.4 | Same; LTM calculated |
| Free cash flow (operating cash flow less capital purchases) | 336.5 | 57.6 | 83.3 | 225.7 | 268.8 | 379.6 | Calculated; Q3 amounts equal the company free cash flow at Deck Q3 page:8 |
| Cash paid for interest | 115.4 | 27.5 | 35.7 | 85.6 | 102.3 | 132.1 | 10-K FY2025 page:94; 10-Q Q3 page:5; 10-Q Q2 page:5; quarters and LTM calculated |
| Total debt / Adjusted EBITDA (x) | 1.65 | n/a | n/a | n/a | n/a | 1.43 | Point-in-time debt over LTM; see leverage table |
| Net debt / Adjusted EBITDA (x) | 1.23 | n/a | n/a | n/a | n/a | 0.79 | Same |
| EBITDA / cash interest (x) | 3.54 | n/a | n/a | n/a | n/a | 3.42 | See interest cover table |
| Adjusted EBITDA / interest expense net of interest income (x) | 22.32 | n/a | n/a | n/a | n/a | 10.26 | Corporate accrual cover: 332.6 over 14.9 and 382.7 over 37.3 |
| Reported Consolidated Senior Secured Net Leverage Ratio (x) | 1.3 | n/a | n/a | n/a | n/a | 0.9 | Company-reported at December 31, 2025 and September 30, 2026; covenant maximum 3.5 |

### Balance sheet and funding table

| Item | December 31, 2025 | September 30, 2026 | Locator and note |
| --- | --- | --- | --- |
| Cash and cash equivalents | 141.5 | 244.9 | 10-K FY2025 page:92; 10-Q Q3 page:2 |
| Restricted cash | 43.9 | 34.7 | Same. The restricted cash is the minimum reserve that AFC Funding Corporation must hold as security for the securitization (10-K FY2025 page:98) |
| Finance receivables, net | 2,425.4 | 2,763.8 | 10-K FY2025 page:92; 10-Q Q3 page:3 |
| Total assets | 4,724.3 | 5,229.2 | Same |
| Obligations collateralized by finance receivables (carrying) | 1,758.3 | 2,064.1 | Same; gross 1,771.7 and 2,084.4 (10-Q Q3 page:16) |
| Current maturities of long-term debt | 5.5 | 5.5 | Same |
| Long-term debt (carrying) | 530.1 | 528.7 | Same |
| Total debt, principal (debt table) | 550.0 | 545.9 | 10-K FY2025 page:122; 10-Q Q3 page:17 |
| Operating lease liabilities, non-current | 53.0 | 49.0 | Same balance sheet pages. The current portion is 9.7 at December 31, 2025 (10-K FY2025 page:131) and Not supplied at September 30, 2026 |
| Series A convertible preferred stock (temporary equity) | 289.8 | nil | Converted May 2026 (10-Q Q3 page:22 and page:23) |
| Total stockholders' equity | 1,240.7 | 1,576.8 | 10-K FY2025 page:92; 10-Q Q3 page:3 |

### Debt stack: every instrument

| Instrument | Obligor | Outstanding at September 30, 2026 | Rate | Maturity | Security and guarantee | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| 2025 Incremental Term Loans | OPENLANE, Inc. | 545.9 (550.0 at December 31, 2025) | Adjusted Term SOFR + 2.50% | October 8, 2032 | Secured by substantially all assets of the company and the Subsidiary Guarantors; guaranteed by certain domestic subsidiaries | 10-Q Q3 page:17 and page:18 |
| Revolving Credit Facility ($325 million) | OPENLANE, Inc. | No borrowings; 42.6 of letters of credit use the facility | Adjusted Term SOFR + 2.25% | June 23, 2028 | Same as term loans | 10-Q Q3 page:17, page:18 and page:20 |
| Canadian Revolving Credit Facility (C$175 million) | ADESA Auctions Canada Corporation (Canadian Borrower) | No borrowings | Adjusted Term CORRA + 2.50% | June 23, 2028 | Guaranteed by the Canadian Revolving Credit Facility Subsidiary Guarantors, which guarantee only the Canadian Secured Obligations | 10-Q Q3 page:17 and page:20 |
| European lines of credit (euro 40 million, 45.3 in USD) | OPENLANE Europe subsidiaries | No borrowings | Euribor + 1.25% | Repayable upon demand | Secured by certain inventory and receivables at OPENLANE Europe subsidiaries | 10-Q Q3 page:17 and page:21 |
| U.S. securitization facility | AFC Funding Corporation (consolidated, bankruptcy remote) | Gross obligations 2,084.4 for the U.S. and Canadian facilities together | Rate level Not supplied; the average rate fell about 0.6% in Q3 2026 (10-Q Q3 page:41) | Committed liquidity of 2.0 billion; expires January 31, 2030 | Secured borrowing against finance receivables; the facilities are not secured by the general assets of OPENLANE (10-K FY2025 page:82) | 10-Q Q3 page:15, page:16 and page:57 |
| Canadian securitization facility | AFCI (Automotive Finance Canada Inc.) | Included in the 2,084.4 above; split Not supplied | Rate level Not supplied | C$500 million committed; expires January 31, 2030 | Separate third-party conduit | 10-Q Q3 page:15 and page:56 |
| 5.125% senior notes due June 1, 2025 | OPENLANE, Inc. | Repaid at maturity in 2025 (210.0 outstanding at December 31, 2024) | 5.125% | June 1, 2025 | Guaranteed by the Subsidiary Guarantors | 10-K FY2025 page:75, page:76 and page:122 |

The debt table has four rows at September 30, 2026 (term loans, two revolvers and the European lines), and the filing prints a total of 545.9 for them. Securitization obligations are a separate balance-sheet line outside that total.

### Claims outside the debt table

| Claim | Amount | Inside or outside the debt figure | Locator |
| --- | --- | --- | --- |
| Obligations collateralized by finance receivables | 2,084.4 gross at September 30, 2026; 1,771.7 at December 31, 2025 | Outside; on balance sheet as a separate liability line | 10-Q Q3 page:16 |
| Operating lease liabilities | 62.7 at December 31, 2025 (9.7 current, 53.0 non-current); 49.0 non-current at September 30, 2026 | Outside | 10-K FY2025 page:131; 10-Q Q3 page:3 |
| Series A convertible preferred stock | Nil at September 30, 2026; 289.8 temporary equity at December 31, 2025 | Outside; converted to common stock in May 2026 | 10-Q Q3 page:22 and page:23 |
| Letters of credit under the revolver | 42.6 | Not debt; they reduce revolver availability | 10-Q Q3 page:20 |
| Pensions and retiree medical | Not supplied: no such obligation is described in the pinned text. The terms pension, postretirement, retiree and defined benefit were searched in the 10-K and the Q3 10-Q | Not applicable | 10-K FY2025; 10-Q Q3 |
| Purchase commitments, factoring and supply-chain finance | Not supplied: none described; the 10-K contractual obligations table lists only term debt, interest and operating leases | Not applicable | 10-K FY2025 page:82 |
| Litigation and consent decrees | No material accrual or funding obligation described; ordinary-course litigation only | Not applicable | 10-Q Q3 page:24 |
| Interest on long-term debt | 237.5 total over the life, of which 41.7 within one year, at December 31, 2025 | Outside the principal; a future cash cost | 10-K FY2025 page:82 |

### Securitization and funding of the Finance segment

AFC sells most U.S. dollar receivables on a revolving basis, without recourse, to AFC Funding Corporation. The sales are accounted for as secured borrowings (10-Q Q3 page:15 "The receivables sold pursuant to both the U.S. and Canadian securitization agreements are accounted for as secured borrowings"). Receivables serving as security were 2,786.7 at September 30, 2026 against gross obligations of 2,084.4, and a cash reserve of 1 or 3 percent of the obligations is also held (10-Q Q3 page:16). The 10-K gave 2,803.5 for December 31, 2025 collateral (10-K FY2025 page:77); the 2026 10-Qs state a corrected 2,448.2 for the same date. This module uses 2,448.2 for December 31, 2025 and treats 2,803.5 as superseded for that single line.

The filing states that approximately 70% to 75% of the receivable portfolio is funded through the securitization facilities, the remainder from cash on hand and working capital (10-Q Q3 page:60 "approximately 70% to 75% of AFC’s finance receivables portfolio is funded through its securitization facilities"). The calculated share at September 30, 2026 is 75.4% (2,084.4 over total receivables managed of 2,763.5), and 73.1% at December 31, 2025. The September 2026 amendments extended both facilities from January 31, 2028 to January 31, 2030 and yielded about 58 of incremental borrowing (10-Q Q3 page:57). AFC and the securitization vehicles must meet covenants on debt incurrence, minimum tangible net worth and portfolio performance, and the agreements incorporate the Credit Agreement financial covenants; the tangible net worth level is Not supplied, and tangible parent equity was 526.7 at September 30, 2026 against 534.4 at December 31, 2025 (10-Q Q3 page:42).

### Covenants

| Test | Level | Reported figure | Headroom | Locator and limitation |
| --- | --- | --- | --- | --- |
| Maximum Consolidated Senior Secured Net Leverage Ratio, Credit Agreement | 3.5, tested at each quarter-end on which any loans under the Revolving Credit Facilities are outstanding; no step-down is described | 0.9 at September 30, 2026; 1.0 at June 30, 2026; 1.2 at March 31, 2026; 1.3 at December 31, 2025 | 2.6 on the reported 0.9 (calculated as 3.5 less 0.9) | 10-Q Q3 page:54; 10-Q Q2 page:51; 10-Q Q1 page:41; 10-K FY2025 page:75. The filings report no revolver borrowings (10-Q Q3 page:20), so the test is described as springing on drawings; the legal reading is not made here |
| AFC and AFCI covenants under the securitization agreements | Limits on debt AFC and AFCI can incur, minimum tangible net worth, portfolio performance tests; levels Not supplied | In compliance at September 30, 2026 | Not calculable: levels are not printed | 10-Q Q3 page:57 |
| Credit Agreement negative covenants | Limits on dividends and distributions, acquisitions, investments, liens, asset sales and indebtedness; baskets Not supplied | In compliance at September 30, 2026 | Not calculable | 10-Q Q3 page:54 and page:55 |

The calculated net debt over Adjusted EBITDA (0.79 at LTM Q3 2026) is below the reported 0.9 at the same date. The difference is a definition difference, not an error: the covenant uses Consolidated Total Debt and Consolidated EBITDA as defined in the Credit Agreement, with Unrestricted Cash as defined there, and the company Adjusted EBITDA is its own non-GAAP measure. The covenant EBITDA adds back items such as stock-based compensation and restructuring-type costs (10-Q Q3 page:54) and the pack does not reconcile the two measures.

### Earnings quality: the bridge from EBITDA to Adjusted EBITDA

For LTM Q3 2026, EBITDA of 451.5 is reduced by net deductions of 68.8 to reach Adjusted EBITDA of 382.7 (10-Q Q3 page:59). The largest single item is the deduction for securitization interest of 95.9. That deduction is partly offset by non-cash stock-based compensation of 30.8. The first quarter of 2026 also carries a deduction of 15.9 for the Impact of Canadian DST related to prior years (10-Q Q3 page:59), which removes a one-time benefit from Adjusted EBITDA. New add-back lines appear in Q3 2026: transaction-related costs of 1.7 and a loss on extinguishment of debt of 0.7 (10-Q Q3 page:58). Because Adjusted EBITDA is stated after securitization interest, it is a corporate-level measure for leverage. It is not comparable with unadjusted EBITDA, and the interest-cover table keeps the two bases apart.

### Segment view: Adjusted EBITDA by segment

| Quarter | Marketplace | Finance | Consolidated | Locator |
| --- | --- | --- | --- | --- |
| Q4 2025 | 31.6 | 44.4 | 76.0 | Deck Q3 page:7 |
| Q1 2026 | 51.6 | 45.1 | 96.7 | Deck Q3 page:7 |
| Q2 2026 | 56.7 | 46.5 | 103.2 | Deck Q3 page:6 |
| Q3 2026 | 57.8 | 49.0 | 106.8 | Deck Q3 page:6 |
| LTM Q3 2026 (calculated) | 197.7 | 185.0 | 382.7 | Sum of the four quarters; Finance is 48.3% of the total |

The Finance segment's Adjusted EBITDA is after its securitization interest. Finance revenue was 114.7 in Q3 2026 against 109.0 in Q3 2025 (10-Q Q3 page:40), the annualized provision for credit losses was 1.1% of average receivables managed against 1.6%, and delinquent receivables were 0.6% of total receivables managed against 0.3% (10-Q Q3 page:40).

### Cash flow quality

Operating cash flow was 309.5 for 9M 2026 against 266.4 for 9M 2025, and free cash flow, after capital purchases of 40.7 in each period, was 268.8 against 225.7. The finance receivables book is funded outside operating cash flow: receivables growth is in investing activities (367.6 for 9M 2026) and the matching increase in securitization obligations is in financing activities (322.9). The calculated free cash flow after both changes is 224.1 for 9M 2026 and 175.4 for 9M 2025. Common stock repurchases including excise taxes were 91.5 for 9M 2026 against 35.8 for 9M 2025 (10-Q Q3 page:5). The October 2025 Series A repurchase of approximately 559.3 was funded primarily with the 550.0 of term loans (10-K FY2025 page:122; 10-Q Q3 page:22). Q3 2026 buybacks were 1,237,828 shares at an average of 35.23 including 727,590 shares bought from the underwriter of an Apax secondary offering in August 2026 (10-Q Q3 page:66).

### Latest quarter and events to the cutoff

- September 2026: AFC and AFC Funding Corporation signed the 2026 Second Amendment and AFCI signed Amendment No. 4, extending both facilities to January 31, 2030. Capitalized costs were about 10.7 and 1.8, a loss on extinguishment of debt of 0.7 was recorded, and the amendments yielded about 58 of incremental borrowing (10-Q Q3 page:15 and page:57).
- June 30, 2026: a Third Amendment to the Credit Agreement is listed in the exhibit index (10-Q Q3 page:68). Its terms are not described in the debt note and are Not supplied.
- May 2026: the remaining Series A preferred stock (300,277 shares) converted into 17,103,116 shares of common stock, a non-cash transaction (10-Q Q3 page:22).
- October 2026 (subsequent event): the board raised the share repurchase program from 250 to 400 and extended it to December 31, 2027; 306,334 shares were repurchased for 11.1 in October 2026 (10-Q Q3 page:27).
- November 4, 2026 guidance: Adjusted EBITDA of 390 to 400 and capital expenditures of 55 to 60 for 2026, a management claim (Deck Q3 page:5).
- The Q3 2026 10-Q describes no corporate debt issuance or repayment beyond the scheduled term-loan installments, and the word waiver does not appear in it. Nothing after November 4, 2026 is supplied.

### Interpretation for credit

1. Corporate leverage is low on the company measure. Debt of 545.9 is covered 1.43 times by LTM Adjusted EBITDA of 382.7, down from 1.65 at FY2025 because LTM Adjusted EBITDA is higher (382.7 against 332.6) while principal debt is about the same (545.9 against 550.0). At FY2024 the figure was 0.79, before the October 2025 term loan funded the preferred repurchase.
2. The all-in funded picture is much larger. Securitization obligations of 2,084.4 gross are not secured by the general assets of the company and are carried against 2,763.5 of receivables managed. Their risk is the quality and growth of floorplan receivables, not corporate leverage; delinquent receivables were 0.6% of receivables managed against 0.3% a year earlier.
3. Interest burden has stepped up. Corporate interest, net of interest income, is 37.3 for LTM Q3 2026 against 14.9 for FY2025 and 21.2 at LTM Q1 2026, as the term loan took effect in the fourth quarter of 2025 (10-Q Q3 page:35). Run-rate cover on Adjusted EBITDA is therefore better read as 10.26 than as the 22.32 for FY2025.
4. Liquidity is adequate. Cash of 244.9 and undrawn revolver availability of 405.3 total 650.2 against annual term-loan amortization of 5.5 and no maturity before June 23, 2028. The securitization facilities are committed to January 31, 2030.
5. Share repurchases are rising and compete with deleveraging. The buyback program was enlarged to 400 in October 2026, and 9M 2026 repurchases were 91.5. The Credit Agreement limits dividends and distributions, but baskets are Not supplied.

## Calculations

All inputs are printed figures cited above; results are the analyst's calculations rounded as shown.

### LTM bridges (flows)

| Item | Formula | Inputs | Result |
| --- | --- | --- | --- |
| LTM revenue Q3 2026 | FY2025 less 9M 2025 plus 9M 2026 | 1,934.5; 1,440.2; 1,643.7 | 2,138.0; quarter sum 494.3 + 527.9 + 554.6 + 561.2 = 2,138.0 |
| LTM operating profit | same | 196.6; 154.1; 211.7 | 254.2 |
| LTM net income | same | 177.7; 118.2; 137.9 | 197.4; equals printed 197.4 |
| LTM interest expense (corporate) | same | 18.1; 8.2; 30.1 | 40.0 |
| LTM operating cash flow | same | 391.9; 266.4; 309.5 | 435.0; quarter sum 125.5 + 159.6 + 52.8 + 97.1 = 435.0 |
| LTM capital purchases | same | 55.4; 40.7; 40.7 | 55.4 |
| LTM free cash flow | LTM operating cash flow less LTM capital purchases | 435.0; 55.4 | 379.6 |
| LTM Adjusted EBITDA at Q1, Q2 and Q3 2026 | sum of last four quarters | 86.7 + 87.1 + 76.0 + 96.7; 87.1 + 76.0 + 96.7 + 103.2; 76.0 + 96.7 + 103.2 + 106.8 | 346.5; 363.0; 382.7; each equals the company-printed LTM (10-Q Q1 page:44, 10-Q Q2 page:56, 10-Q Q3 page:59) |
| LTM EBITDA at Q1, Q2 and Q3 2026 | same | 102.9 + 107.5 + 91.9 + 122.7; 107.5 + 91.9 + 122.7 + 118.1; 91.9 + 122.7 + 118.1 + 118.8 | 425.0; 440.2; 451.5; each equals the printed LTM |
| LTM cash paid for interest | FY2025 less prior-year YTD plus current YTD | Q1: 115.4 - 26.1 + 33.4; Q2: 115.4 - 58.1 + 66.6; Q3: 115.4 - 85.6 + 102.3 | 122.7; 123.9; 132.1 |
| Stand-alone Q3 cash interest | 9M less 6M | 2026: 102.3 - 66.6; 2025: 85.6 - 58.1 | 35.7; 27.5 |
| FCF by period | operating cash flow less capital purchases | FY2025 391.9 - 55.4; Q3 2025 72.2 - 14.6; Q3 2026 97.1 - 13.8; 9M 2025 266.4 - 40.7; 9M 2026 309.5 - 40.7 | 336.5; 57.6; 83.3; 225.7; 268.8 |

### Leverage and cover

| Period | Total debt | Cash | Net debt | Adjusted EBITDA | Total debt / | Net debt / | EBITDA | Cash interest | EBITDA / cash int. | Adj. EBITDA / cash int. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FY2024 | 230.7 | 143.0 | 87.7 | 293.4 | 0.786 | 0.299 | 396.8 | 140.7 | 2.820 | 2.085 |
| FY2025 | 550.0 | 141.5 | 408.5 | 332.6 | 1.654 | 1.228 | 408.7 | 115.4 | 3.542 | 2.882 |
| LTM Q1 2026 | 568.0 | 180.1 | 387.9 | 346.5 | 1.639 | 1.119 | 425.0 | 122.7 | 3.464 | 2.824 |
| LTM Q2 2026 | 547.2 | 189.7 | 357.5 | 363.0 | 1.507 | 0.985 | 440.2 | 123.9 | 3.553 | 2.930 |
| LTM Q3 2026 | 545.9 | 244.9 | 301.0 | 382.7 | 1.426 | 0.787 | 451.5 | 132.1 | 3.418 | 2.897 |

Formulas: net debt = total debt less cash and cash equivalents; ratios are the quotient of the stated columns. Locators: debt at 10-K FY2025 page:122, 10-Q Q1 page:15, 10-Q Q2 page:17, 10-Q Q3 page:17; cash at 10-K FY2025 page:92, 10-Q Q1 page:2, 10-Q Q2 page:2, 10-Q Q3 page:2; Adjusted EBITDA and EBITDA at 10-K FY2025 page:79 and the LTM tables above; cash interest at 10-K FY2025 page:94 (FY2024 140.7) and the 10-Q cash-flow supplements. The FY2024 EBITDA 396.8 and Adjusted EBITDA 293.4 are at 10-K FY2025 page:79.

### Accrual interest cover and other ratios

| Item | Formula | Inputs | Result |
| --- | --- | --- | --- |
| Corporate accrual cover | Adjusted EBITDA over interest expense net of interest income | FY2025 332.6 over 14.9; LTM Q1 346.5 over 21.2; LTM Q2 363.0 over 28.9; LTM Q3 382.7 over 37.3 | 22.32; 16.34; 12.56; 10.26 |
| Liquidity | cash plus undrawn revolver availability | 141.5 + 409.9; 180.1 + 408.2; 189.7 + 405.7; 244.9 + 405.3 | 551.4; 588.3; 595.4; 650.2 |
| Securitization funding share | gross obligations over total receivables managed | 2,084.4 over 2,763.5; 1,771.7 over 2,423.5 | 75.4%; 73.1% |
| Collateral coverage | receivables serving as security over gross obligations | 2,786.7 over 2,084.4; 2,448.2 over 1,771.7 | 1.34; 1.38 |
| Free cash flow after receivable funding, 9M 2026 | FCF less increase in finance receivables plus increase in obligations | 268.8 - 367.6 + 322.9 | 224.1 |
| Free cash flow after receivable funding, 9M 2025 | same | 225.7 - 196.1 + 145.8 | 175.4 |
| Share of receivable growth funded by securitization, 9M 2026 | increase in obligations over increase in receivables | 322.9 over 367.6 | 87.8% |
| EBITDA to Adjusted EBITDA, LTM Q3 2026 | EBITDA less net deductions | 451.5 - 68.8 | 382.7; securitization interest 95.9 and stock-based compensation 30.8 are the two largest lines |
| Finance share of Adjusted EBITDA | Finance LTM over consolidated LTM | 44.4 + 45.1 + 46.5 + 49.0 = 185.0 over 382.7 | 48.3% |

### Debt maturity schedule check

| Item | Formula | Inputs | Result |
| --- | --- | --- | --- |
| Quarterly installment | 0.25% of the original principal | 0.0025 x 550.0 | 1.375 (10-Q Q3 page:18 "payable in quarterly installments equal to 0.25% of the original aggregate principal amount") |
| Principal after three installments | original less three installments | 550.0 - 4.125 | 545.875, printed as 545.9; payments on long-term debt of 4.1 for 9M 2026 (10-Q Q3 page:5) |
| Current and non-current split | principal less current maturities | 545.9 - 5.5 | 540.4; equals non-current carrying 528.7 plus unamortized discounts and costs 11.7 (10-Q Q3 page:20) |
| Carrying value | principal less unamortized discounts and costs | 545.9 - 11.7 | 534.2; equals 5.5 + 528.7 on the balance sheet |
| Filed split at December 31, 2025 | 10-K contractual obligations | 5.5 within one year; 544.5 after | 550.0 (10-K FY2025 page:82) |
| Schedule from September 30, 2026 | installments after the balance sheet date | Q4 2026 1.375; 2027 to 2031 5.5 each (27.5); 2032 three installments 4.125 plus balloon 512.875 | 1.375 + 27.5 + 4.125 + 512.875 = 545.875 |

## Gaps

| ID | Gap | Severity | Affected | Action |
| --- | --- | --- | --- | --- |
| G1 | Credit Agreement, its three amendments and the securitization agreements are not supplied. The Third Amendment dated June 30, 2026 is listed in the exhibit index but not described in the debt note. Covenant definitions, baskets and the securitization tangible net worth level are Not supplied. | High for covenant work | Covenant headroom, restricted payments | Supply the executed agreements |
| G2 | The cash paid for interest is a single figure that includes securitization interest; the corporate share is Not calculable. Cover on cash interest therefore mixes corporate and securitization interest. | Medium | Interest cover | Use accrual corporate cover as the cross-check |
| G3 | The undrawn securitization capacity is Not calculable: the 2,084.4 gross balance is not split between the U.S. facility and the C$500 million Canadian facility, and borrowing-base limits are not stated. | Medium | Liquidity | Obtain the monthly servicer or facility reports |
| G4 | The December 31, 2025 collateral figure of 2,803.5 in the 10-K is corrected to 2,448.2 in the 2026 10-Qs; the 10-K is not restated. This module uses 2,448.2. | Medium | Collateral coverage | Cite both |
| G5 | No maturity table is printed at September 30, 2026; the schedule is the analyst's, on an installment assumption, and ignores any excess-cash-flow or voluntary prepayment. | Low | Debt maturities | Confirm against the Credit Agreement |
| G6 | The current portion of operating lease liabilities at September 30, 2026 is Not supplied in the 10-Q; the term lease was searched in the 10-Q text. | Low | Claims outside debt | Use 9.7 at December 31, 2025 as the latest printed |
| G7 | The European lines (euro 40 million) are not described as committed, so they are excluded from undrawn committed facilities. | Low | Liquidity | Confirm facility terms |
| G8 | Deck charts (marketplace volumes, yield, finance metrics) are not in the extracted text; no chart data is used in this module. | Low | Operating metrics | Use the 10-Q tables |
| G9 | Guarantor names and the subsidiary list are Not supplied (CP-0 G2). | Medium | Structural analysis | Supply Exhibit 21.1 |
| G10 | Management guidance and Adjusted EBITDA are non-GAAP claims by the issuer; the covenant EBITDA is not reconciled to them. | Medium | Covenant headroom | Reconcile when the agreement is supplied |

## Next module

- CP-1A: carry the two-segment structure (Marketplace and Finance), the October 2025 term loan used to repurchase Series A preferred, the May 2026 conversion, the September 2026 securitization extensions and the October 2026 buyback increase. Keep the Third Amendment (June 30, 2026) as an event with Not supplied terms.
- CP-2: use corporate leverage of 1.43 total and 0.79 net on Adjusted EBITDA as the base, keep securitization obligations of 2,084.4 gross as a separate funded claim, and carry G1 to G3 and G10 as limits on covenant and liquidity conclusions. Use 2,448.2, not 2,803.5, for December 31, 2025 collateral.
- CP-5: trace the printed LTM tables (10-Q Q1 page:44, 10-Q Q2 page:56, 10-Q Q3 page:59), which agree with the sums of quarters, and label every ratio in this handoff as calculated.
