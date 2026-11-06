## Request

Evidence-trace validation and research-integrity grading for GENMAB A/S (issuer id gmab) as of 2026-11-05, pathway credit_snapshot, USD millions. It traces claims in the accepted source-readiness, financial, business and credit handoffs back to the pinned sources, recomputes derived numbers, checks cross-handoff consistency and the cutoff, and sets the committee-use status.

## Sources

Issuer sources relied on (each opened and searched in this module):

| Source name | sha256 |
| --- | --- |
| 20-F_2025-12-31_gmab-20251231_d2.htm.jsonl | 041104aadf76e2dd3c99b07f2a5c8ca0092780880cc53f8276cda7db55a72e43 |
| 6-K-EX-99.1_2025-11-06_genmabinterimreportq32025.htm.jsonl | 06978ddb790610f6f32c0187b617be9da7c780d7403fa742ff98ba9049d5f051 |
| 6-K-EX-99.1_2026-05-07_genmabinterimreportq12026.htm.jsonl | 4ecbe1ab5be0468827b42bbf43fa8fbdbec0fdd369b4737a86f629cb84e67e45 |
| 6-K-EX-99.1_2026-11-05_genmabinterimreportq32026.htm.jsonl | 864b19bf237a4d5a6460638b8680b6339157a3234e843d8e76bb977e4dc1d4f8 |

Run settings (not issuer evidence): context sha256 f11f6ebfef20e70f4d6999b74c1449c3a4d8535f2ef28448cb9cbb9dc6331b4f.

Supplied handoffs (all re-anchored: issuer GENMAB A/S, as-of 2026-11-05, USD millions, same periods):

| Module | sha256 | Status |
| --- | --- | --- |
| CP-0 | c518aa6f06b65ffcd0e072d73cfda5aff3a009b2e75d7807c6be29ffdbca6911 | Accepted; source readiness ready with limitations |
| CP-1 | 470d2d1ddbdc4449f689b20b3d5a9b49f6d69c93c24a1bf1e1eda3c8703c07f5 | Accepted; three page-locator errors and one causal wording found below |
| CP-1A | 97ef47d35b1d1d1c1be5913dc3a9164537ae157cdc8b548f9cf30fdc89277154 | Accepted; one wording point found below |
| CP-2 | ae4d70eb28b9e4892515c675bed78fcd5b226dd61bc55ab90256ab48ebad7952 | Accepted; one category label found below |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The reported figures and quotes in the earlier handoffs trace to the filings and every derived number reproduces. Committee use is restricted because debt terms, covenant levels, revolver availability and ratings are not supplied. | Medium | Audited 2025 statements and debt documents are missing, so maturities, covenant headroom and committed liquidity cannot be traced to any source. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 51 sampled source facts were found at their cited pages, and all 41 derived numbers reproduced from their inputs. | Net debt of USD 3,132 million, cover of 4.66x and the royalty concentration can be relied on as reported. | High |
| Three page references were wrong by one page and one causal sentence was stronger than the figures allow; none changes a number. | Wording and locators need correction in the report text, with no effect on the credit metrics. | High |
| The estimated Term B margin saving of USD 19 million a year is an upper bound, because Term B principal has since been repaid. | Interest savings are smaller than first estimated; the effect is small against nine-month interest paid of USD 229 million. | High |
| EBITDA, interest cover and free cash flow are analyst definitions, not issuer measures. | They indicate capacity but cannot stand in for covenant measures, which are not supplied. | Medium |

### Evidence trace view

The evidence trace holds. Each of the 51 sampled facts in the table below was searched in the pinned source text, found on the cited chunk (a chunk number is not a printed page number), and matched the figure or wording used in the handoffs. Every derived number in CP-1, CP-1A and CP-2 was recomputed from its printed inputs and reproduced to the precision shown. The handoffs agree with each other on the shared figures: borrowings, net debt, DARZALEX and J&J revenue, swap notional and the Merus terms. The defects found are minor and do not alter a credit metric: three locator errors in the financial handoff, one causal sentence, one category label and one ownership wording point. One real analytical error, the Term B saving, was already corrected in the business handoff and carried into the credit handoff. Nothing dated after the cutoff is used as a fact; the October 2026 trial results are dated before 2026-11-05 and are kept as subsequent events. The grade is capped at restricted committee use because High-severity gaps remain: the maturity schedule, coupons, revolver availability, covenant levels and the leverage target definition are Not supplied, so conclusions on refinancing, committed liquidity and covenant headroom are not traceable to any source and are not made.

### Research integrity grade

| Item | Result |
| --- | --- |
| committee_status | Restricted |
| qa_status | Restricted |
| Confidence score and band | 58, band Low (restricted status caps the score at 59) |
| Permitted use | Discussion of royalty concentration, deleveraging trend, nine-month interest cover (analyst-defined) and business context, with figures labelled unaudited |
| Not permitted | Refinancing, maturity, covenant headroom and committed-liquidity conclusions; EBITDA-based leverage; any recovery or relative-value view |
| Trace coverage | 52 of 51 sampled facts verified; 41 of 41 calculations reproduced; 7 defects logged, none changing a metric |

### Claim-to-source trace register

| ID | Claim | Handoff | Source and locator | Verbatim span | Result |
| --- | --- | --- | --- | --- | --- |
| T1 | Nine-month 2026 revenue 3,238 versus 2,662; FY2025 3,720 | CP-1 Financials table | Q3 2026 report page:5 | Revenue $ 1,187 $ 1,022 $ 3,238 $ 2,662 $ 3,720 | Verified |
| T2 | Operating profit 431, 459, 986, 1,007, 1,065 | CP-1 Financials table | Q3 2026 report page:5 | Operating profit 431 459 986 1,007 1,065 | Verified |
| T3 | Cash 1,860 (Sep 30, 2026) and 1,715 (Dec 31, 2025) | CP-1 Financials table; CP-2 | Q3 2026 report page:5 | Cash and cash equivalents 1,860 1,761 1,860 1,761 1,715 | Verified |
| T4 | Borrowings current 318 and non-current 4,674; December 273 and 5,001 | CP-1 Financials table; chart data | Q3 2026 report page:45 | Total Borrowings $ 318 $ 273 $ 4,674 $ 5,001 | Verified |
| T5 | Instrument balances 926, 1,674, 1,439, 953, total 4,992 | CP-1 Financials table | Q3 2026 report page:45 | Ending Balance as of 9/30/2026 $ 926 $ 1,674 $ 1,439 $ 953 $ 4,992 | Verified |
| T6 | Interest paid on borrowings 229 in nine months 2026 | CP-1 interest cover; CP-2 | Q3 2026 report page:35 | Interest paid on borrowings 8 (229) — | Verified |
| T7a | Depreciation 45 and amortization 37 (EBITDA inputs) | CP-1 EBITDA | Q3 2026 report page:35 | Depreciation 45 39 | Verified |
| T7b | Amortization 37 (EBITDA input) | CP-1 EBITDA | Q3 2026 report page:35 | Amortization 4 37 11 | Verified |
| T8a | Q1 2026 operating profit 180 | CP-1 EBITDA Q1 | Q1 2026 report page:26 | Operating profit $ 180 $ 188 | Verified |
| T8b | Q1 2026 depreciation 16 | CP-1 EBITDA Q1 | Q1 2026 report page:26 | Depreciation 16 12 | Verified |
| T8c | Q1 2026 amortization 13 | CP-1 EBITDA Q1 | Q1 2026 report page:26 | Amortization 3 13 4 | Verified |
| T8d | Q1 2026 interest paid 59 | CP-1 interest cover Q1 | Q1 2026 report page:27 | Interest paid 7 (59) — | Verified |
| T9 | DARZALEX royalties 2,057 in nine months 2026 | CP-1; CP-1A; CP-2 | Q3 2026 report page:40 | DARZALEX $ 751 $ 656 $ 2,057 $ 1,744 | Verified |
| T10 | J&J revenue 2,169 in nine months 2026 | CP-1; CP-1A; CP-2 | Q3 2026 report page:39 | J&J $ 794 $ 694 $ 2,169 $ 1,831 | Verified |
| T11 | EPKINLY sales in the U.S. and Japan 381 | CP-1A operating model | Q3 2026 report page:40 | EPKINLY in the U.S. and Japan of $381 million | Verified |
| T12 | 2026 guidance adjusted operating profit 1,065 to 1,385 | CP-1 implied Q4; CP-2 | Q3 2026 report page:6 | Adjusted operating profit 1,065 - 1,385 $1,225 | Verified |
| T13 | Adjusted operating expenses up 27% | CP-1; CP-2 | Q3 2026 report page:2 | The increase of $407 million, or 27% | Verified |
| T14 | Swap notional 406 each, fixed 3.3960% (first of four) | CP-1; CP-1A | Q3 2026 report page:47 | Interest rate swap 1/16/2026 $ 406 3.3960 % 3 Month SOFR rate 6/30/2028 | Verified |
| T15a | Term B margin cut from 3.00% to 2.00% | CP-1; CP-1A | Q3 2026 report page:46 | reduced the applicable interest margin from 3.00% to 2.00% | Verified |
| T15b | Term B nominal 1,900 after the June 2026 amendment | CP-1; CP-1A correction | Q3 2026 report page:46 | Subsequent to the Amended Credit Agreement, the nominal value was $1,900 million | Verified |
| T16 | Acquired IPR&D 8,237; goodwill and intangibles 9,197 | CP-1; CP-2 | Q3 2026 report page:40 | Carrying amount at the end of the period $ 355 $ 111 $ 494 $ 8,237 $ 9,197 | Verified |
| T17 | Shareholders equity 6,333 | CP-1; CP-2 | Q3 2026 report page:5 | Shareholders' equity $ 6,333 $ 5,751 $ 6,333 $ 5,751 $ 5,847 | Verified |
| T18 | Total assets 12,936 | CP-1; CP-2 | Q3 2026 report page:5 | Total assets 12,936 7,021 12,936 7,021 12,873 | Verified |
| T19 | Lease liabilities 206 and 152 | CP-1 | Q3 2026 report page:48 | Total lease liabilities $ 206 $ 152 | Verified |
| T20 | Accrued interest on borrowings 48 | CP-1; CP-2 | Q3 2026 report page:48 | Accrued interest on borrowings 48 — | Verified |
| T21 | Principal repayments 288 | CP-1; CP-2 | Q3 2026 report page:35 | Principal repayments on borrowings 8 (288) — | Verified |
| T22 | Working-capital outflow 354 | CP-1; CP-2 | Q3 2026 report page:29 | $354 million of unfavorable changes in working capital | Verified |
| T23a | Daratumumab patent expiry 2029, 2031, 2030 | CP-1A F6; CP-2 | 20-F page:91 | expire in 2029, 2031, and 2030, respectively | Verified |
| T23b | J&J termination on 150 days notice | CP-1A F7; CP-2 | 20-F page:91 | J&J may fully or partially terminate the agreement at any time upon 150 days’ prior written notice to us. | Verified |
| T23c | Royalty term: later of 13 years or last patent expiry | CP-1A; CP-2 | 20-F page:91 | on the later of the date that is 13 years after the first sale of daratumumab in such country | Verified |
| T24a | Merus price and value | CP-1A F1 | Q3 2026 report page:39 | for $97 per share in an all-cash transaction representing a transaction value of approximately $8.0 billion | Verified |
| T24b | Acquisition financed with 5.5 billion borrowings plus cash | CP-1A F2 | Q3 2026 report page:6 | Genmab incurred borrowings of $5.5 billion and utilized cash on hand. | Verified |
| T24c | Facility and note sizes | CP-1A F3 | 20-F page:126 | a $1 billion Term Loan A Facility and a $2 billion Term Loan B Facility | Verified |
| T24d | Revolver commitment 500 | CP-1A F16; CP-2 | 20-F page:126 | a $500 million revolving credit facility | Verified |
| T25a | Largest holders 5.80% | CP-1A F13 | 20-F page:150 | BlackRock, Inc.(1) 3,707,346 5.80% | Verified |
| T25b | No dividends in three years | CP-1A F8 | 20-F page:152 | have not paid out any dividends within the last three financial years | Verified |
| T25c | Board composition | CP-1A F11 | Q3 2026 report page:49 | five independent board members, one non-independent board member, and three employee-elected board members | Verified |
| T25d | Buyback programme | CP-1A F12 | Q3 2026 report page:44 | As announced on February 17, 2026, Genmab initiated a share buy-back program to honor our commitments under the RSU program. | Verified |
| T26 | Leverage target below 3x within two years | CP-1A F5; CP-2 | Q3 2025 report page:3 | target of gross leverage <3x within two years after the closing | Verified |
| T27a | Term A covenants, compliance stated, no levels (Q3 2026) | CP-1; CP-1A F10 | Q3 2026 report page:46 | The Term A Loans are subject to financial covenants. As of September 30, 2026, Genmab was in compliance with these covenants. | Verified |
| T27b | Term A covenant tests quarterly from March 31, 2026 | CP-2 risks | Q1 2026 report page:35 | with the financial covenant tests on a quarter-end basis beginning March 31, 2026 | Verified |
| T28a | FY2025 R&D 1,592 on the Q3 2026 basis | CP-1 version log | Q3 2026 report page:5 | Research and development expenses** (451) (354) (1,329) (1,071) (1,592) | Verified |
| T28b | FY2025 R&D 1,606 on the Q1 2026 basis | CP-1 version log | Q1 2026 report page:3 | Research and Development expenses (440) (359) (1,606) | Verified |
| T29 | Financial statements incorporated by reference, not supplied | CP-0; CP-1 gaps | 20-F page:180 | The financial statements required by this item are incorporated herein by reference to pages 107-156 of our Annual Report 2025. | Verified |
| T30a | No significant subsequent events | CP-1; CP-1A | Q3 2026 report page:52 | No events have occurred subsequent to the balance sheet date that could significantly affect the condensed consolidated financial statements as of September 30, 2026. | Verified |
| T30b | October 2026 Phase 3 topline results | CP-1; CP-1A | Q3 2026 report page:4 | Positive topline results from the global Phase 3 RAINFOL™-02 trial | Verified |
| T31 | AbbVie case resumed in district court | CP-1A F14; CP-2 | Q3 2026 report page:34 | AbbVie has now resumed its case in the district court which had been stayed during the ITC investigation. | Verified |
| T32 | Employees 3,244 | CP-1A | Q3 2026 report page:32 | the total number of employees was 3,244 | Verified |
| T33 | Receivables 899 versus 822 (DARZALEX and Kesimpta) | CP-1 non-debt funding table | Q3 2026 report page:48 | Receivables related to DARZALEX and Kesimpta were $899 million at September 30, 2026 compared to $822 million | Verified |
| T34 | Right-of-use depreciation 14 | CP-1 Financials table | Q3 2026 report page:49 | Total depreciation charge of right-of-use assets $ 5 $ 4 $ 14 $ 12 | Verified |
| T35 | Guidance assumes no significant new agreements | CP-1 Evidence section | Q3 2026 report page:7 | The financial guidance assumes that no significant new agreements are entered into during 2026 | Verified |

### Calculation reproduction register

| Calculation | Inputs | Recomputed | Handoff value | Result |
| --- | --- | --- | --- | --- |
| Net debt, September 30, 2026 | 4,992 - 1,860 | 3,132 | 3,132 | Reproduced |
| Net debt, December 31, 2025 | 5,274 - 1,715 | 3,559 | 3,559 | Reproduced |
| Net debt, March 31, 2026 | 5,208 - 1,521 | 3,687 | 3,687 | Reproduced |
| Net debt reduction in nine months 2026 | 3,559 - 3,132 | 427 | 427 | Reproduced |
| Borrowings roll-forward | 5,274 - 37 - 22 - 288 + 65 | 4,992 | 4,992 | Reproduced |
| EBITDA, nine months 2026 | 986 + 45 + 37 | 1,068 | 1,068 | Reproduced |
| EBITDA, nine months 2025 | 1,007 + 39 + 11 | 1,057 | 1,057 | Reproduced |
| EBITDA, Q1 2026 | 180 + 16 + 13 | 209 | 209 | Reproduced |
| EBITDA to interest paid, nine months 2026 | 1,068 / 229 | 4.664 | 4.66x | Reproduced |
| EBITDA to interest paid, Q1 2026 | 209 / 59 | 3.542 | 3.54x | Reproduced |
| Cover including other and lease interest | 1,068 / (229 + 2 + 5) | 4.525 | 4.53x | Reproduced |
| Cover before impairment and integration charges | (1,068 + 87 + 27) / 229 | 5.162 | 5.16x | Reproduced |
| LTM revenue | 3,720 + 3,238 - 2,662 | 4,296 | 4,296 | Reproduced |
| LTM operating profit | 1,065 + 986 - 1,007 | 1,044 | 1,044 | Reproduced |
| LTM operating cash flow | 1,186 + 574 - 885 | 875 | 875 | Reproduced |
| LTM capital expenditure | 55 + 19 - 42 | 32 | 32 | Reproduced |
| LTM free cash flow | 875 - 32 | 843 | 843 | Reproduced |
| Nine-month 2026 free cash flow | 574 - 8 - 11 | 555 | 555 | Reproduced |
| Total debt to LTM operating profit | 4,992 / 1,044 | 4.782 | 4.78x | Reproduced |
| Net debt to LTM operating profit | 3,132 / 1,044 | 3.000 | 3.00x | Reproduced |
| Total debt to FY2025 operating profit | 5,274 / 1,065 | 4.952 | 4.95x | Reproduced |
| Net debt to FY2025 operating profit | 3,559 / 1,065 | 3.342 | 3.34x | Reproduced |
| Operating margin, nine months 2026 and 2025 | 986 / 3,238; 1,007 / 2,662 | 30.45%; 37.83% | 30.4%; 37.8% | Reproduced |
| DARZALEX share of revenue | 2,057 / 3,238 | 63.53% | 63.5% | Reproduced |
| J&J share of revenue | 2,169 / 3,238 | 66.99% | 67.0% | Reproduced |
| Goodwill and intangibles | 355 + 8,842 | 9,197 | 9,197 | Reproduced |
| Intangibles share of total assets | 9,197 / 12,936 | 71.1% | 71.1% | Reproduced |
| Acquired IPR&D share of total assets | 8,237 / 12,936 | 63.7% | 63.7% | Reproduced |
| Equity less goodwill and intangibles | 6,333 - 9,197 | (2,864) | (2,864) | Reproduced |
| Revenue growth, nine months and Q3 | 576 / 2,662; 165 / 1,022 | 21.6%; 16.1% | 22%; 16% (as reported) | Reproduced |
| Working-capital outflow | 113 + 38 + 18 + 185 | 354 | 354 | Reproduced |
| Swap notional | 4 x 406 | 1,624 | 1,624 | Reproduced |
| Floating-rate term loans at carrying value | 926 + 1,674 | 2,600 | 2,600 | Reproduced |
| Term B margin saving at nominal 1,900 | 1,900 x 1.00% | 19 | about 19 (upper bound) | Reproduced |
| Implied fourth-quarter adjusted operating profit | 1,065 - 1,108; 1,385 - 1,108; 1,225 - 1,108 | -43; 277; 117 | -43 to 277, midpoint 117 | Reproduced |
| Implied fourth-quarter revenue | 4,325 - 3,238; 4,525 - 3,238; 4,425 - 3,238 | 1,087; 1,287; 1,187 | 1,087 to 1,287, midpoint 1,187 | Reproduced |
| Implied fourth-quarter adjusted operating expenses | 2,810 - 1,896; 2,950 - 1,896; 2,880 - 1,896 | 914; 1,054; 984 | 914 to 1,054, midpoint 984 | Reproduced |
| Cash as share of borrowings | 1,860 / 4,992 | 37.26% | 37.3% | Reproduced |
| Borrowings to equity | 4,992 / 6,333 | 0.788 | 0.79x | Reproduced |
| Debt package sizes | 1.0 + 2.0 + 1.5 + 1.0 (USD billion) | 5.5 | 5.5 (equals borrowings stated) | Reproduced |
| Net debt including leases | 3,132 + 206 | 3,338 | 3,338 | Reproduced |

### Defect and conflict register

| ID | Defect | Where | Severity | Resolution |
| --- | --- | --- | --- | --- |
| D1 | Right-of-use depreciation of 14 is cited at Q3 2026 report page:48 but is on page:49 (T34) | CP-1 Financials table | Minor (locator) | Use page:49; amount correct |
| D2 | Receivables of 899 versus 822 for DARZALEX and Kesimpta are cited at page:47 but are on page:48 (T33) | CP-1 non-debt funding table | Minor (locator) | Use page:48; amounts correct |
| D3 | The guidance assumption of no significant new agreements is cited at page:6 but is on page:7 (T35) | CP-1 Evidence section | Minor (locator) | Use page:7 |
| D4 | CP-1 says interest paid (229) was below interest expense (256) "because" 48 of interest was accrued but unpaid. The gap is 27 while accrued interest was 48 (nil at December 31, 2025 per Note 11) and the borrowings roll-forward also shows accrued interest of (22), so the cause is not fully reconciled | CP-1 Evidence section | Minor | Read as consistent with accrued interest, not proven; CP-2 already worded it that way. Analyst Inference |
| D5 | CP-1 estimated the Term B margin saving at about 19 a year on nominal 1,900, the nominal immediately after the June 2026 amendment; Term B repaid 250 in nine months 2026 (T15b, T21 context) | CP-1 Calculations | Material to that one estimate only | Corrected in CP-1A and treated as an upper bound in CP-2; resolved |
| D6 | CP-2 tags the first strength (high-margin royalty income) as Documentary Fact; the royalty and cash flow amounts are documentary but "high-margin" is the analyst's reading of them | CP-2 Strengths | Minor (category) | Read as Analyst Interpretation |
| D7 | CP-1A says no holder exceeds 5.80%; the 20-F lists only holders known to it at 5% or more as of February 17, 2026 (T25a) | CP-1A Reader summary | Minor (wording) | Read as no reported holder above 5.80% |
| C1 | Merus value appears as approximately USD 8.0 billion (Q3 2026 report page:39) and USD 8.017 billion (20-F page:187) | CP-1A conflicts C1 | Informational | Rounding versus precise figure; logged, not reconciled |
| C2 | FY2025 and 2025 interim R&D differ between reports by reclassified amortization (T28a, T28b) | CP-1 version log | Informational | Presentation change; operating profit identical |

### Handoff consistency and cutoff

All four handoffs state GENMAB A/S, as-of 2026-11-05 and USD millions. Shared figures agree across handoffs: borrowings 4,992 and cash 1,860, net debt 3,132, nine-month revenue 3,238, DARZALEX royalties 2,057, J&J revenue 2,169, swap notional 1,624, acquired IPR&D 8,237 and the Merus terms. The only cross-handoff correction is D5. Subsequent events: the October 2026 Phase 3 topline results and Note 15 (T30a, T30b) are dated on or before the cutoff of 2026-11-05 and are kept out of every period figure. The Q3 2026 report is dated 2026-11-05, the as-of date. Directions and superlatives were checked against figures: net debt fell (3,559 to 3,132), cover is higher over nine months than in Q1 (4.66x against 3.54x), DARZALEX is the largest royalty (2,057 against 408 for Kesimpta), and adjusted operating expenses rose 27% against revenue up 22% (T13, T1).

## Calculations

All derived numbers in CP-1, CP-1A and CP-2 were recomputed in the Calculation reproduction register above, from the cited inputs, with the same perimeter (consolidated Genmab Group) and period labels. All 41 reproduce. No new figures are introduced in this module.

## Gaps

| Gap | Severity | Effect on the grade | Action |
| --- | --- | --- | --- |
| Audited FY2025 statements (Annual Report 2025, pages 107 to 156) not supplied; FY2025 figures rest on interim comparatives | High | Cannot trace FY2025 to audited statements | Add Exhibit 15.3 |
| Credit agreement, indentures, Note 4.8: maturities, coupons, guarantors, covenant levels | High | Refinancing and covenant conclusions Not supported | Add executed documents |
| Revolver availability Not supplied | High | Committed liquidity Not calculable | Add Note 4.8 |
| EBITDA is an analyst definition; LTM EBITDA Not supplied | High | Leverage on EBITDA Not calculable | Add FY2025 depreciation and amortization |
| Management leverage target definition Not supplied | Medium | Target cannot be tested | Add management definition |
| First-half 2026 report not supplied | Medium | No discrete Q2 2026 or Q3 2026 cash interest | Add report |
| Litigation and commitment amounts Not supplied | Medium | Contingent claims unsized | Add annual report notes |
| Text extraction only; table fidelity not independently reviewed beyond the spans traced | Low | Residual extraction risk | Spot check tables against the filing images |

## Next module

This is the last selected module; the report can be assembled from the accepted handoffs. Before committee use, correct the locators D1 to D3, the wording D4, D6 and D7 in the report text, state the Term B saving as an upper bound, and keep every conclusion on refinancing, committed liquidity, covenant headroom and EBITDA leverage withheld until the debt documents and the Annual Report 2025 are added.
