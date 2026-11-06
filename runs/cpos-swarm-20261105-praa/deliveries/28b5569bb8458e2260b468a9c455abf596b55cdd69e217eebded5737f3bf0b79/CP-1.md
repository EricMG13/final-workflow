# CP-1 — Financial base: PRA GROUP INC (praa)

## Request

- Issuer: PRA GROUP INC (issuer id `praa`, ticker PRAA), as-of date 2026-11-05, information cutoff 2026-11-05 (context).
- Run `praa-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Current period q2-2026, prior period fy-2025, reporting currency USD (context settings).
- Task: build the reported financial base for the credit view: statement facts, debt by instrument, liquidity, maturities, the issuer's EBITDA definition, and clearly labelled calculations, from the pinned filings and releases only.
- Perimeter: PRA Group, Inc. and its subsidiaries, consolidated, including noncontrolling interests. USD. Statements are in thousands of USD; chart tables are converted to US$m (thousands divided by 1,000, no rounding of the source).
- Execution: host session. No provider was called. Nothing dated after the cutoff is used; the latest source is the Q2 2026 10-Q signed August 7, 2026.
- Upstream: the CP-0 readiness handoff, which rated CP-1 READY_WITH_LIMITATIONS and carries these limits forward: tables are flattened text; segment basis changed in Q4 2025; the amended European credit agreement, other credit agreements and indentures are not supplied; covenant ratio levels are not printed.

## Sources

Locators are `page:N` of the pinned text files (source chunks, not printed page numbers). sha256 values are those CP-OS pins.

### Issuer sources relied on

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_praa-20251231.htm.jsonl | acaea144d244584c3474f86549753d209ff125e0c5d293c88092a8b3609d005e | Audited FY2025 and FY2024 statements, borrowings note, covenants, Adjusted EBITDA reconciliation, ERC, segments |
| 10-Q_2025-09-30_praa-20250930.htm.jsonl | 929f20928dbfde158b90287ecb3f34f89e93248de03667dc981595cbc1f16f43 | September 30, 2025 debt, cash, availability, nine-month cash interest, last-twelve-months Adjusted EBITDA |
| 10-Q_2026-03-31_praa-20260331.htm.jsonl | 5b8ee1fe62f8b0079ea63a2a1c4f92f69a59ebc645588dbcce6f190c45211b32 | March 31, 2026 balance sheet, debt, availability, Q1 2026 results and cash interest, ERC |
| 10-Q_2026-06-30_praa-20260630.htm.jsonl | d7a354d31f5af038cbd610321c408a92f38ffbe0be4451883080ac13fa2cd5a8 | June 30, 2026 statements, borrowings, availability, segments, ERC, Adjusted EBITDA, subsequent event |
| EX-99.1_2026-05-07_q12026earningsrelease.htm.jsonl | 0cafa2dd16d8fe170df8f95a181353ea848b2d370eaa0bad903e81ca9ab40ac1 | Adjusted EBITDA reconciliation for the last twelve months to March 31, 2026 |
| EX-99.1_2026-08-06_q22026earningsrelease.htm.jsonl | 90c4b9dc1bbbec8846231ce65b511117fe19795284263ee0dc2f0a68914940d4 | Quarterly cash collections by source, Adjusted EBITDA reconciliation to June 30, 2026, management commentary |
| EX-99.1_2026-02-26_q42025earningsrelease.htm.jsonl | ac28ac408106b5058aef5a7017ad24c9c2f1059768c1e80795f1a5ba0705218f | Cross-check only: FY2025 and FY2024 Adjusted EBITDA agree with the 10-K (page:11) |

### Run settings (not issuer evidence)

| Source | sha256 | Role |
| --- | --- | --- |
| context (1185348-pra-group-inc-praa.json) | fb395d626a32c7d3e686eb338c55b901d79ab38a3782a023f0c732503b0056b3 | Dated user settings. Blank fields are unknown, not zero. |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | ad930b06ca8dfafbd7d05aa59918ec9f5ec7345e1f274cfd0ac40c5b9907cbbd | Source readiness, source register, limitations carried forward. |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Debt principal of $3,771.3 million at June 30, 2026 is 2.78x issuer-defined Adjusted EBITDA of $1,358.9 million for the last twelve months, 2.68x net of cash. Reported earnings lean on estimate revisions rather than cash. | Medium | Adjusted EBITDA is an issuer non-GAAP measure, not the covenant definition, so these ratios are not covenant headroom. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Gross debt over Adjusted EBITDA eased from 2.93x for FY2024 to 2.78x for the last twelve months to June 30, 2026, as EBITDA grew faster than debt. | Leverage is moderate on the issuer's own measure, but that measure adds back collections applied to principal, so peer comparison needs care. | Medium |
| Adjusted EBITDA covered cash interest paid 5.36x for the last twelve months to June 30, 2026, against 5.08x for FY2025. | Interest is well covered by cash earnings before portfolio purchases, which absorb the surplus. | Medium |
| Portfolio purchases exceeded Adjusted EBITDA after cash interest and cash taxes in both FY2025 and FY2024, and borrowings rose in both years. | Leverage depends on purchasing discipline; growth in the portfolio has been debt funded. | Medium |
| Changes in expected recoveries were $96.9 million of Q2 2026 income from operations of $153.3 million, after the European forecast review. | Reported profit is more estimate driven than cash collections of $558.5 million suggest, so cash measures deserve more weight. | Medium |
| Credit facility availability was $998.5 million at June 30, 2026, of which $733.1 million is based on current ERC, against cash of $132.4 million. | Liquidity rests on ERC-based borrowing capacity and covenant compliance rather than on cash on hand. | Medium |

### Financial base view

The reported base is complete for the audited year ended December 31, 2025, the comparative year 2024 and the interim periods to June 30, 2026. On the issuer's own Adjusted EBITDA, gross debt (credit facilities plus senior notes, at principal) was $3,771.3 million at June 30, 2026 against last-twelve-months Adjusted EBITDA of $1,358.9 million, which is 2.78x gross and 2.68x after deducting cash and cash equivalents of $132.4 million. Adjusted EBITDA covered cash interest paid 5.36x. Total availability under the credit facilities was $998.5 million, of which $733.1 million is based on current ERC and $265.4 million is subject to borrowing base and advance rates. Quarterly cash collections were $558.5 million in Q2 2026. Three features limit how far these numbers can be pushed. First, PRA's Adjusted EBITDA adds back recoveries collected and applied to finance receivables less changes in expected recoveries, so it is a cash-collections measure and is not comparable with a conventional EBITDA; it is also not the EBITDA defined in the credit agreements, which is not supplied. Second, net cash used in operating activities is negative in every year shown because collections applied to principal are classified in investing activities, so operating cash flow and a free cash flow built from it are not meaningful here. Third, Q2 2026 earnings include a European forecast revision: changes in expected recoveries were $96.9 million of income from operations of $153.3 million. The base does not support a covenant headroom conclusion: compliance is stated but no covenant ratio is printed.

### Source basis and period map

| Source | Entity and perimeter | Period and basis | Statement kind | Units and currency | Role in this handoff |
| --- | --- | --- | --- | --- | --- |
| 10-K FY2025 | PRA Group, Inc. consolidated | Years ended December 31, 2025, 2024, 2023; audited (Ernst & Young LLP, page:68) | Balance sheet page:68, income statement page:69, cash flows page:70 and page:71, notes | Thousands, USD | Controlling for FY2025 and FY2024 |
| 10-Q Q3 2025 | PRA Group, Inc. consolidated | Three and nine months ended September 30, 2025; unaudited | Statements page:2 to page:6, Note 5 page:12 | Thousands, USD | September 30, 2025 balances and nine-month cash interest |
| 10-Q Q1 2026 | PRA Group, Inc. consolidated | Three months ended March 31, 2026 and 2025; unaudited | Statements page:2 to page:5, Note 5 page:8 | Thousands, USD | March 31, 2026 balances; Q1 2026 and Q1 2025 flows |
| 10-Q Q2 2026 | PRA Group, Inc. consolidated | Three and six months ended June 30, 2026 and 2025; unaudited | Statements page:2 to page:5, Note 5 page:11 | Thousands, USD | Controlling for June 30, 2026 balances and H1 2026 flows |
| Releases (Q1 2026, Q2 2026, Q4 2025) | PRA Group, Inc. consolidated, management presentation | Last twelve months to March 31, 2026 and June 30, 2026; fiscal 2025 | Non-GAAP reconciliations and cash collections by source | Thousands, USD | Supporting; filings control where both print a figure |

### Debt by instrument

Principal amounts as printed in the borrowings notes (Q2 10-Q Note 5, page:11; 10-K Note 7, page:86; Q1 10-Q Note 5, page:8; Q3 10-Q Note 5, page:12). Terms from the 10-K (page:87 to page:92) except where the Q2 10-Q is cited.

| Instrument | Dec 31, 2025 | Jun 30, 2026 | Maturity | Pricing or coupon | Security and obligors |
| --- | --- | --- | --- | --- | --- |
| North American revolving credit facility (limit 1,075,000: 950,000 domestic and 125,000 Canadian) | 520,736 | 565,092 | October 28, 2029 | Margin 2.25%, or 2.00% if consolidated senior secured leverage is at most 1.60x; unused fee 0.35% or 0.30% | First priority lien on substantially all assets; guaranteed by U.S. and Canadian subsidiaries |
| North American term loan | 460,111 | 455,111 | October 28, 2029; 2,500 quarterly principal payments | Same margin as the North American facility | Same as the North American revolving facility |
| United Kingdom revolving credit facility (limit 725,000) | 499,848 | 491,946 | October 30, 2029 | Margin 2.75%, or 2.50% if senior secured leverage is at most 1.60x; commitment fee 0.30% or 0.35% | Secured by substantially all assets of PRA Group UK Limited and related equity interests |
| European revolving credit facility (about EUR 730,000 limit; committed 873,733 at June 30, 2026) | 577,335 | 618,227 | November 23, 2027 at the 10-K date; April 30, 2031 after the April 30, 2026 amendment | Interbank rate plus 2.80% to 3.80% by ERC ratio at the 10-K date; funding costs unchanged by the amendment per Q1 10-Q page:17 | Guaranteed by the Company; secured by equity in operating subsidiaries of the borrowers |
| Colombian revolving credit facility | 2,611 | 245 | Not stated in the supplied text | Not stated | Not stated |
| 2028 senior notes | 398,000 | 398,000 | February 1, 2028 | 8.375%; original issue 400,000 | Senior unsecured; guaranteed by domestic restricted subsidiaries |
| 2029 senior notes | 350,000 | 350,000 | October 1, 2029 | 5.00% | Senior unsecured; guaranteed by domestic restricted subsidiaries |
| 2030 senior notes | 550,000 | 550,000 | January 31, 2030 | 8.875%; 400,000 issued May 20, 2024 plus 150,000 issued November 25, 2024 | Senior unsecured; guaranteed by domestic restricted subsidiaries |
| 2032 senior notes (EUR 300,000 principal) | 352,350 | 342,630 | September 30, 2032 | 6.250% | Issued by PRA Group Europe Holding II S.à r.l.; guaranteed by the Company and domestic restricted subsidiaries |
| Credit facility borrowings | 2,060,641 | 2,130,621 | n/a | n/a | Sum as printed |
| Senior notes | 1,650,350 | 1,640,630 | n/a | n/a | Sum as printed |
| Credit facility borrowings and senior notes (principal) | 3,710,991 | 3,771,251 | n/a | n/a | As printed |
| Unamortized debt premium and issuance costs, net | (13,653) | (11,898) | n/a | n/a | As printed |
| Total borrowings (balance sheet carrying value) | 3,697,338 | 3,759,353 | n/a | n/a | As printed |

Other claims outside the debt figure: interest-bearing deposits of 100,460 at June 30, 2026 (106,148 at December 31, 2025), taken by the banking subsidiary AK Nordic AB (Q2 10-Q page:2, page:41 and page:43; 10-K page:89); lease liabilities of 30,681 at June 30, 2026, of which 6.6 million is due within 12 months (page:2 and page:43); interest rate swaps with notional of 723.1 million and foreign exchange forwards with notional of 443.7 million (page:12), with derivative liabilities at fair value of 7,987 (page:12). The estimated minimum contractual purchase obligation under forward flow agreements was "not significant" (page:17); estimated forward flow purchases over the next 12 months are 218.7 million, which is not a contractual minimum (page:42). Letters of credit drawn against the North American facility are Not supplied: the only mention is a 25.0 million sub-limit (10-K page:87).

### Covenant terms as printed (levels only; no reported ratios)

| Facility | Test as printed in the 10-K (page:87 to page:89) | Reported level | Note |
| --- | --- | --- | --- |
| North American | Consolidated total leverage at most 3.50x; senior secured leverage at most 2.50x; fixed charge coverage at least 2.00x; dividends and distributions at most 50.0 million per fiscal year; borrowing base 35% of eligible Core ERC and 55% of Insolvency ERC | Not supplied: compliance stated only (Q2 10-Q page:11) | Definitions not supplied |
| United Kingdom | Same three ratio tests; borrowing base of up to 35% and 55% of PRA UK eligible ERC less reserves | Not supplied | Definitions not supplied |
| European | Same three ratio tests; ERC ratio at most 45% at the 10-K date, 40% after April 30, 2026; interest-bearing deposits in AK Nordic AB at most SEK 2.2 billion; cash collection thresholds | Not supplied | The amended agreement is not supplied |

### Liquidity and availability by facility

| Facility (June 30, 2026) | Committed | Outstanding | Total availability | Based on current ERC | Additional availability |
| --- | --- | --- | --- | --- | --- |
| North American revolving | 1,075,000 | 565,092 | 509,908 | 318,207 | 191,701 |
| European revolving | 873,733 | 618,227 | 255,506 | 255,506 | 0 printed as a dash |
| UK revolving | 725,000 | 491,946 | 233,054 | 159,383 | 73,671 |
| Total of the three revolving facilities | 2,673,733 | 1,675,265 | 998,468 | 733,096 | 265,372 |

Totals follow Q2 10-Q page:40 and page:41 (committed total 4,769,719 including the term loan, senior notes and the Colombian facility). The "additional availability" is stated to be "subject to borrowing base and debt covenants, including advance rates" (page:41). Availability at other dates is in the liquidity chart data.

### Adjusted EBITDA as printed by the issuer

Source: 10-K page:45 and page:46 (FY2024 and FY2025), Q1 release page:10 and Q1 10-Q page:27 (last twelve months to March 31, 2026), Q2 release page:11 and Q2 10-Q page:35 (last twelve months to June 30, 2026). Thousands of USD.

| Line | FY2024 | FY2025 | LTM Mar 31, 2026 | LTM Jun 30, 2026 |
| --- | --- | --- | --- | --- |
| Net income/(loss) attributable to PRA Group, Inc. | 70,601 | (305,142) | (280,591) | (265,048) |
| Income tax expense | 21,032 | 46,735 | 51,187 | 65,157 |
| Foreign exchange (gain)/loss | 9 | (755) | (1,860) | (1,309) |
| Interest expense, net | 229,267 | 251,788 | 254,336 | 256,338 |
| Other expense | 851 | 336 | 410 | 427 |
| Depreciation and amortization | 10,792 | 9,035 | 7,805 | 7,188 |
| Impairment of real estate | — | 1,404 | 573 | 3,411 |
| Goodwill impairment | — | 412,611 | 412,611 | 412,611 |
| Net income attributable to noncontrolling interests | 17,972 | 15,168 | 13,325 | 11,010 |
| Gain on sale of equity method investment | — | (38,403) | (38,403) | — |
| Recoveries collected and applied to finance receivables, net less changes in expected recoveries | 787,028 | 922,697 | 929,206 | 869,128 |
| Adjusted EBITDA | 1,137,552 | 1,315,474 | 1,348,599 | 1,358,913 |

The Q3 2025 10-Q prints last-twelve-months Adjusted EBITDA to September 30, 2025 of 1,265,490 (page:25 and page:35). The Q2 10-Q key metrics table prints the prior-year comparative, last twelve months to June 30, 2025, of 1,240,092, with a stated increase of 9.6% (page:25).

### Segment and geographic facts

Thousands of USD. Segments were created in Q4 2025 and prior periods are recast (10-K page:103 and page:104). Q2 10-Q page:18 and page:19; 10-K page:104 and page:105.

| Item | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- |
| U.S. revenues from external customers | 150,476 | 137,448 | 307,271 | 273,829 | 611,252 | 593,928 |
| Europe revenues from external customers | 216,613 | 119,447 | 342,245 | 219,597 | 461,365 | 394,963 |
| U.S. adjusted segment operating income (FY: segment operating income) | 17,315 | 17,511 | 47,504 | 34,890 | 120,630 | 127,573 |
| Europe adjusted segment operating income (FY: segment operating income) | 168,146 | 70,723 | 244,366 | 127,350 | 269,828 | 217,708 |
| U.S. interest expense, net | 35,186 | 38,610 | 76,292 | 76,549 | 144,304 | 139,594 |
| Europe interest expense, net | 30,756 | 25,095 | 54,349 | 48,862 | 111,516 | 90,537 |

Segment revenues exclude South America, Canada and Australia ("All other"), which contribute the difference to consolidated revenues (Q2 10-Q page:18).

### ERC by geography

Thousands of USD; ERC is the issuer's estimate of future collections on its portfolios.

| Date | U.S. | Europe | Other markets | Total | Source |
| --- | --- | --- | --- | --- | --- |
| December 31, 2024 | Not supplied by segment | Not supplied by segment | Not supplied by segment | 7,460,626 | 10-K page:39 |
| December 31, 2025 | 3,658,300 | 4,386,331 | 564,234 | 8,608,865 | 10-K page:50 |
| March 31, 2026 | 3,647,093 | 4,336,770 | 564,685 | 8,548,548 | Q1 10-Q page:28 |
| June 30, 2025 | Not supplied by segment | Not supplied by segment | Not supplied by segment | 8,294,310 | Q2 10-Q page:25 |
| June 30, 2026 | 3,592,821 | 4,806,182 | 495,512 | 8,894,515 | Q2 10-Q page:37 |

The Q2 10-Q reports that the European forecast update raised European ERC by 348.5 million (page:24) and, within changes in expected future recoveries, a positive adjustment of approximately 105 million (page:9). The 2026 10-Q ERC tables start their year rows at 2027 and print no 2026 row, although the rows sum to the printed total; what period the first row covers is not stated in the pages read.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 2.93 | 2.84 | x | Debt principal 3,337,541 (10-K page:86) over issuer Adjusted EBITDA 1,137,552; net of cash and cash equivalents 105,938. Issuer non-GAAP EBITDA, not the covenant definition. |
| LTM Q3 2025 | 2.86 | 2.78 | x | Debt principal 3,621,300 (Q3 10-Q page:12) over last-twelve-months Adjusted EBITDA 1,265,490; net of cash 107,454. Same limitation. |
| FY2025 | 2.82 | 2.74 | x | Debt principal 3,710,991 (10-K page:86) over Adjusted EBITDA 1,315,474, which includes a goodwill impairment add-back; net of cash 104,409. Same limitation. |
| LTM Q1 2026 | 2.81 | 2.72 | x | Debt principal 3,791,905 (Q1 10-Q page:8) over last-twelve-months Adjusted EBITDA 1,348,599; net of cash 124,778. Same limitation. |
| LTM Q2 2026 | 2.78 | 2.68 | x | Debt principal 3,771,251 (Q2 10-Q page:11) over last-twelve-months Adjusted EBITDA 1,358,913; net of cash 132,431. Interest-bearing deposits of 100,460 and investments of 145,473 are excluded. Same limitation. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 5.08 | x | Issuer Adjusted EBITDA 1,137,552 over cash paid for interest 224,099 (10-K page:71). Issuer non-GAAP EBITDA. |
| LTM Q3 2025 | 4.84 | x | Adjusted EBITDA 1,265,490 over derived last-twelve-months cash interest 261,450 (FY2024 less nine months 2024 plus nine months 2025; Q3 10-Q page:6). |
| FY2025 | 5.08 | x | Adjusted EBITDA 1,315,474 over cash paid for interest 259,061 (10-K page:71). |
| LTM Q1 2026 | 5.27 | x | Adjusted EBITDA 1,348,599 over derived cash interest 256,029 (FY2025 less Q1 2025 plus Q1 2026; Q1 10-Q page:4). |
| LTM Q2 2026 | 5.36 | x | Adjusted EBITDA 1,358,913 over derived cash interest 253,430 (FY2025 less H1 2025 plus H1 2026; Q2 10-Q page:5). Cash interest paid is the cash flow supplemental figure and its composition (for example deposit interest and swap settlements) is not itemized. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2024 | 105.938 | 1026.339 | US$m | Cash and cash equivalents (10-K page:68); total availability (10-K page:40). Availability is after the borrowing base and advance rates; letters of credit drawn are Not supplied. |
| Jun 30, 2025 | 131.592 | 840.670 | US$m | Cash and cash equivalents (Q2 10-Q page:5, comparative); total availability (Q2 10-Q page:25, comparative). Same limitation. |
| Sep 30, 2025 | 107.454 | 1190.275 | US$m | Cash (Q3 10-Q page:2); total availability (Q3 10-Q page:26). Same limitation. |
| Dec 31, 2025 | 104.409 | 1099.466 | US$m | Cash (10-K page:68); total availability (10-K page:54). Same limitation. |
| Mar 31, 2026 | 124.778 | 995.995 | US$m | Cash (Q1 10-Q page:2); total availability (Q1 10-Q page:32). Same limitation. |
| Jun 30, 2026 | 132.431 | 998.468 | US$m | Cash (Q2 10-Q page:2); total availability (Q2 10-Q page:40). 733.096 is based on current ERC and 265.372 is additional availability subject to borrowing base and advance rates. Cash excludes investments of 145.473 held for the banking subsidiary and restricted cash of 3.248. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| H2 2026 | 5.000 | US$m | North American term loan quarterly principal payments of 2.5 million for two quarters (Q2 10-Q page:42). Derived schedule as of June 30, 2026; the filing prints no maturity table for that date. |
| 2027 | 10.000 | US$m | North American term loan payments only. The European facility, shown in 2027 in the 10-K table (page:86), now matures in 2031. |
| 2028 | 408.245 | US$m | 2028 senior notes 398.000 (February 1, 2028), term loan payments 10.000 and the Colombian facility 0.245, placed here because the 10-K totals are consistent with 2028 and the Q2 10-Q puts the earliest non-term-loan principal in February 2028 (page:42). Colombian maturity is not stated. |
| 2029 | 1837.149 | US$m | North American revolving 565.092 and UK revolving 491.946 (October 2029), 2029 senior notes 350.000, and the term loan balance due at maturity 430.111 after 2026 to 2028 payments of 25.000. |
| 2030 | 550.000 | US$m | 2030 senior notes (January 31, 2030). |
| 2031 | 618.227 | US$m | European revolving facility drawn balance at the amended April 30, 2031 maturity. Revolver balances are shown in full at final maturity; they may be repaid and redrawn earlier. |
| 2032 | 342.630 | US$m | 2032 senior notes, EUR 300.0 million translated at the June 30, 2026 balance sheet rate as printed. Foreign exchange moves this figure. |

### Financials and credit metrics

| Metric (thousands of USD unless stated) | FY2024 | FY2025 | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Portfolio income | 857,188 | 1,013,271 | 250,934 | 267,799 | 491,892 | 537,378 | Income statements: 10-K page:69; Q2 10-Q page:3 |
| Changes in expected recoveries | 240,868 | 176,451 | 33,292 | 96,924 | 61,214 | 140,810 | Same |
| Total revenues | 1,114,524 | 1,201,837 | 287,688 | 372,174 | 557,307 | 686,707 | Same |
| Total operating expenses | 774,792 | 1,232,110 | 202,577 | 218,892 | 397,619 | 430,171 | FY2025 includes goodwill impairment 412,611 |
| Income/(loss) from operations | 339,732 | (30,273) | 85,111 | 153,282 | 159,688 | 256,536 | Same |
| Interest expense, net | 229,267 | 251,788 | 62,361 | 64,363 | 123,331 | 127,881 | Shown as a positive expense |
| Income/(loss) before income taxes | 109,605 | (243,239) | 61,128 | 88,326 | 74,504 | 128,862 | FY2025, Q2 2025 and H1 2025 include the 38,403 gain on sale of equity method investment |
| Net income/(loss) attributable to PRA Group, Inc. | 70,601 | (305,142) | 42,374 | 57,917 | 46,033 | 86,127 | Same |
| Net income attributable to noncontrolling interests | 17,972 | 15,168 | 3,339 | 1,024 | 8,744 | 4,586 | Same |
| Cash collections | 1,868,576 | 2,107,626 | 536,288 | 558,545 | 1,033,724 | 1,110,473 | 10-K page:39; Q2 10-Q page:25 |
| Portfolio purchases (total, as defined by issuer) | 1,407,834 | 1,208,500 | 346,505 | 296,571 | 638,207 | 517,421 | Same |
| Net cash used in operating activities | (94,594) | (85,541) | Not printed: year-to-date statement only | Not printed: year-to-date statement only | (65,490) | (11,344) | 10-K page:70; Q2 10-Q page:5 |
| Purchases of nonperforming loan portfolios (cash flow) | (1,407,067) | (1,203,740) | Not printed: year-to-date statement only | Not printed: year-to-date statement only | (633,308) | (521,713) | Investing activities; 10-K page:70; Q2 10-Q page:5 |
| Recoveries collected and applied to finance receivables, net | 1,027,896 | 1,099,148 | Not printed: year-to-date statement only | Not printed: year-to-date statement only | 554,715 | 580,742 | Investing activities; same |
| Cash paid for interest | 224,099 | 259,061 | Not printed: year-to-date statement only | Not printed: year-to-date statement only | 132,590 | 126,959 | Supplemental cash flow information |
| Cash paid for income taxes | 5,222 | 38,528 | Not printed: year-to-date statement only | Not printed: year-to-date statement only | 19,551 | 8,264 | Same |
| Adjusted EBITDA (issuer non-GAAP) | 1,137,552 | 1,315,474 | Not printed: last twelve months only | 1,358,913 for the last twelve months to Jun 30, 2026 | Not printed: last twelve months only | Not printed: last twelve months only | Last twelve months to Jun 30, 2025 was 1,240,092 (Q2 10-Q page:25) |
| Cash and cash equivalents (period end) | 105,938 | 104,409 | 131,592 | 132,431 | Same date as Q2 2025 | Same date as Q2 2026 | Balance sheets; Q2 2025 from the cash flow reconciliation (Q2 10-Q page:5) |
| Finance receivables, net (period end) | 4,140,742 | 4,688,024 | 4,562,576 | 4,717,204 | Same date as Q2 2025 | Same date as Q2 2026 | 10-K page:68; Q2 10-Q page:2 and page:25 |
| Total borrowings, carrying value (period end) | 3,326,621 | 3,697,338 | 3,614,208 | 3,759,353 | Same date as Q2 2025 | Same date as Q2 2026 | Same |
| Debt principal, facilities plus senior notes (period end) | 3,337,541 | 3,710,991 | Not supplied: principal table for June 30, 2025 not in the pack | 3,771,251 | Same date as Q2 2025 | Same date as Q2 2026 | 10-K page:86; Q2 10-Q page:11 |
| Total stockholders' equity, PRA Group, Inc. (period end) | 1,135,032 | 979,851 | 1,336,925 | 1,045,469 | Same date as Q2 2025 | Same date as Q2 2026 | 10-K page:68; Q2 10-Q page:2 and page:25 |
| Total assets (period end) | 4,931,155 | 5,103,322 | Not supplied: balance sheet for June 30, 2025 not in the pack | 5,238,767 | Same date as Q2 2025 | Same date as Q2 2026 | Same |
| ERC (period end) | 7,460,626 | 8,608,865 | 8,294,310 | 8,894,515 | Same date as Q2 2025 | Same date as Q2 2026 | 10-K page:39; Q2 10-Q page:25 |
| Total availability under credit facilities (period end) | 1,026,339 | 1,099,466 | 840,670 | 998,468 | Same date as Q2 2025 | Same date as Q2 2026 | Same |

### Definition and data-quality review

- Adjusted EBITDA definition. The issuer adds net income attributable to noncontrolling interests, so the measure is before the minority share; distributions to noncontrolling interests were 25,132 in FY2025 and 1,522 in H1 2026 (10-K page:71; Q2 10-Q page:5). It replaces changes in expected recoveries with "recoveries collected and applied to Finance receivables, net", which moves the measure from an accrual revenue basis to a cash basis (10-K page:45). It is not the covenant EBITDA; covenant definitions are Not supplied. Do not compare the computed ratios to the 3.50x total leverage or 2.50x senior secured leverage tests.
- Nearest cash cross-check. The issuer's cash receipts less Adjusted operating expenses for FY2025 was 1,298,123 (10-K page:46); Adjusted EBITDA is 1,315,474, a difference of 17,351 whose components are not itemized in the filing.
- Operating cash flow. Net cash used in operating activities is negative in FY2024 and FY2025 and for H1 2025 and H1 2026 because collections applied to principal (1,099,148 in FY2025) sit in investing activities (Q2 10-Q page:44). Free cash flow from operating cash flow is Not calculable on a meaningful basis; the bridge below uses the issuer's cash measure instead.
- Debt perimeter. Total debt here is principal of credit facilities and senior notes. It excludes interest-bearing deposits (100,460), lease liabilities (30,681) and derivative liabilities. A sensitivity including deposits is in Calculations.
- Cash perimeter. Cash and cash equivalents of 132,431 includes 119.1 million held by international operations with indefinitely reinvested earnings (Q2 10-Q page:40). Investments of 145,473 are held "to meet liquidity requirements for our banking subsidiary" (page:43) and are excluded from net debt.
- Foreign currency. The 2032 notes, the European facility and the UK facility are non-USD or multi-currency; principal moves with exchange rates (for example the 2032 notes at 352,350 and 342,630).
- Segment basis. Single-segment before Q4 2025 (Q3 10-Q page:20); two reportable segments from Q4 2025 with recast comparatives (10-K page:103 and page:104).
- Goodwill. 412,611 impaired in Q3 2025 (Q3 10-Q page:3 and page:12), leaving 26,871. FY2025 and the last twelve months to March 31, 2026 and June 30, 2026 net loss therefore reflect a non-cash charge that Adjusted EBITDA adds back.
- Subsequent events. April 30, 2026 amendment of the European facility (Q1 10-Q page:17); August 3, 2026 approval of a new share repurchase program of up to 150 million (Q2 10-Q page:21). Neither changes a balance in the statements reported here.

### Credit read-through

- Leverage trend. Gross debt over Adjusted EBITDA is 2.93x at FY2024, 2.82x at FY2025 and 2.78x for the last twelve months to June 30, 2026. Debt principal rose 13.0% from FY2024 to June 30, 2026 while Adjusted EBITDA rose 19.5%, so the ratio fell. The mechanism is higher collections on recently purchased portfolios (cash collections of 2,107,626 in FY2025 against 1,868,576 in FY2024) and a larger ERC (8,894,515 at June 30, 2026), financed with debt.
- Funding gap. Adjusted EBITDA after cash interest and cash taxes was less than cash spent on portfolio purchases and capital expenditure in FY2025 and FY2024 (bridge in Calculations). Borrowings at carrying value rose from 2,914,270 at December 31, 2023 to 3,326,621 and then 3,697,338 (10-K page:39) and net debt cash flows were positive in both years (C8), so leverage is a function of purchase volume. Management states it can slow purchases "without significantly impacting current year collections" (10-K page:55); that is a management statement, not evidenced by the supplied tables.
- Earnings quality. In Q2 2026 changes in expected recoveries were 96,924 of income from operations of 153,282, driven by the European forecast revision. These are estimates of future collections recognised in income now; Portfolio income, which the filing calls the more predictable yield component, was 267,799 (Q2 10-Q page:29). Cash collections of 558,545 are the stronger measure of performance in the quarter.
- Liquidity. Cash is 132,431 against total availability of 998,468, of which 733,096 is based on current ERC. Availability moved from 1,099,466 at December 31, 2025 to 998,468 at June 30, 2026 as revolver drawings rose; the supplied text does not give letters of credit drawn.
- Maturities. After the April 2026 extension no principal other than the term loan's quarterly payments falls due before February 2028 (Q2 10-Q page:42). The 2029 concentration is the largest, with both revolvers, the 2029 notes and the term loan balance maturing in October 2029.
- Interest. Interest expense, net was 251,788 in FY2025 (cash interest paid 259,061) and 127,881 in H1 2026. Interest expense, net rose 3.2% year on year in Q2 2026, which the filing attributes primarily to higher average debt balances (Q2 10-Q page:32).

## Calculations

All inputs are in thousands of USD unless stated. Results are calculated here and are not issuer-printed unless said.

### C1 and C2: gross and net debt over Adjusted EBITDA

Gross = debt principal / Adjusted EBITDA. Net = (debt principal − cash and cash equivalents) / Adjusted EBITDA.

| Period | Debt principal | Cash | Adjusted EBITDA | Gross (x) | Net debt | Net (x) |
| --- | --- | --- | --- | --- | --- | --- |
| FY2024 | 3,337,541 | 105,938 | 1,137,552 | 2.934 | 3,231,603 | 2.841 |
| LTM Q3 2025 | 3,621,300 | 107,454 | 1,265,490 | 2.862 | 3,513,846 | 2.777 |
| FY2025 | 3,710,991 | 104,409 | 1,315,474 | 2.821 | 3,606,582 | 2.742 |
| LTM Q1 2026 | 3,791,905 | 124,778 | 1,348,599 | 2.812 | 3,667,127 | 2.719 |
| LTM Q2 2026 | 3,771,251 | 132,431 | 1,358,913 | 2.775 | 3,638,820 | 2.678 |

Sensitivity including interest-bearing deposits in debt: (3,771,251 + 100,460 − 132,431) / 1,358,913 = 2.752x at June 30, 2026; (3,710,991 + 106,148 − 104,409) / 1,315,474 = 2.822x at FY2025; (3,337,541 + 163,406 − 105,938) / 1,137,552 = 2.984x at FY2024.

### C3 and C4: derived cash interest and interest cover

Last-twelve-months cash interest = FY2025 cash paid for interest − prior-year-to-date + current-year-to-date.

- LTM Q3 2025: 224,099 − 176,537 + 213,888 = 261,450 (FY2024 less nine months 2024 plus nine months 2025).
- LTM Q1 2026: 259,061 − 86,878 + 83,846 = 256,029.
- LTM Q2 2026: 259,061 − 132,590 + 126,959 = 253,430.

Cover = Adjusted EBITDA / cash interest: FY2024 1,137,552 / 224,099 = 5.076x; LTM Q3 2025 1,265,490 / 261,450 = 4.840x; FY2025 1,315,474 / 259,061 = 5.078x; LTM Q1 2026 1,348,599 / 256,029 = 5.267x; LTM Q2 2026 1,358,913 / 253,430 = 5.362x.

### C5: tie-outs of printed totals

- Adjusted EBITDA reconciliation columns sum to the printed totals: FY2024 1,137,552; FY2025 1,315,474; LTM Mar 31, 2026 1,348,599; LTM Jun 30, 2026 1,358,913 (components in the table above).
- Last-twelve-months net loss to June 30, 2026: (305,142) − 46,033 + 86,127 = (265,048), which equals the printed figure (Q2 10-Q page:25 and page:36).
- Growth in last-twelve-months Adjusted EBITDA: 1,358,913 / 1,240,092 − 1 = 9.58%, which matches the printed 9.6% (page:25).
- Availability at June 30, 2026 equals committed less outstanding for each revolving facility (1,075,000 − 565,092 = 509,908; 873,733 − 618,227 = 255,506; 725,000 − 491,946 = 233,054) and the sum 998,468 equals the printed total. The ERC-based parts sum to 733,096 and the additional parts to 265,372. The same holds at March 31, 2026 (995,995) and December 31, 2025 (1,099,466).
- Principal of credit facilities and senior notes at June 30, 2026: 2,130,621 + 1,640,630 = 3,771,251; less 11,898 gives 3,759,353, the balance sheet figure.

### C6: liquidity

| Date | Cash | Total availability | Cash plus availability |
| --- | --- | --- | --- |
| Dec 31, 2024 | 105,938 | 1,026,339 | 1,132,277 |
| Jun 30, 2025 | 131,592 | 840,670 | 972,262 |
| Sep 30, 2025 | 107,454 | 1,190,275 | 1,297,729 |
| Dec 31, 2025 | 104,409 | 1,099,466 | 1,203,875 |
| Mar 31, 2026 | 124,778 | 995,995 | 1,120,773 |
| Jun 30, 2026 | 132,431 | 998,468 | 1,130,899 |

Letters of credit drawn are Not supplied, so no deduction is made. No facility is described as expiring within twelve months of June 30, 2026 in the supplied text; the earliest revolver maturity is October 2029 (Q2 10-Q page:11).

### C7: derived maturity schedule at June 30, 2026

Inputs from Q2 10-Q page:11 and page:42 and 10-K page:87 to page:92. Term loan balance 455,111 less 2.5 million quarterly payments: H2 2026 = 2 × 2,500 = 5,000; 2027 = 4 × 2,500 = 10,000; 2028 = 10,000; remainder at October 28, 2029 = 455,111 − 5,000 − 10,000 − 10,000 = 430,111.

- 2026 (H2): 5,000.
- 2027: 10,000.
- 2028: 398,000 + 10,000 + 245 = 408,245.
- 2029: 565,092 + 491,946 + 350,000 + 430,111 = 1,837,149.
- 2030: 550,000.
- 2031: 618,227.
- 2032: 342,630.
- Sum: 5,000 + 10,000 + 408,245 + 1,837,149 + 550,000 + 618,227 + 342,630 = 3,771,251, equal to the printed principal.

Cross-check against the 10-K schedule at December 31, 2025 (page:86): 2028 = 398,000 + 10,000 + 2,611 = 410,611, which equals the printed 410,611; 2029 = 520,736 + 499,848 + 350,000 + 430,111 = 1,800,695, which equals the printed figure. The 10-K 2027 figure of 587,335 included the European facility 577,335 plus 10,000 and is superseded for that facility by the extension to April 30, 2031.

### C8: illustrative cash bridge (not an issuer measure)

Adjusted EBITDA − cash paid for interest − cash paid for income taxes − purchases of nonperforming loan portfolios − purchases of property and equipment.

- FY2025: 1,315,474 − 259,061 − 38,528 − 1,203,740 − 4,821 = (190,676).
- FY2024: 1,137,552 − 224,099 − 5,222 − 1,407,067 − 4,045 = (502,881).

Net debt cash flows, from the cash flow statement (10-K page:71): FY2025 1,203,549 − 1,291,725 − 10,000 + 351,990 = 253,814 (lines of credit proceeds less payments, less long-term debt payments, plus senior notes proceeds); FY2024 1,901,645 − 1,720,836 + 472,611 − 445,000 + 555,438 − 298,000 = 465,858. FY2024 also had a 59,848 net increase in interest-bearing deposits and FY2025 an 88,193 net decrease. Adjusted EBITDA includes the noncontrolling interests' share and the bridge excludes distributions to noncontrolling interests (25,132 in FY2025), share repurchases (20,000 in FY2025) and fees, so the shortfall to be financed is larger than shown.

### C9: other ratios

- ERC to debt principal: 8,894,515 / 3,771,251 = 2.36x at June 30, 2026; 8,608,865 / 3,710,991 = 2.32x at December 31, 2025; 7,460,626 / 3,337,541 = 2.24x at December 31, 2024.
- Change in debt principal from December 31, 2024 to June 30, 2026: 3,771,251 − 3,337,541 = 433,710, which is 13.0% of 3,337,541. Change in Adjusted EBITDA from FY2024 to the last twelve months to June 30, 2026: 1,358,913 / 1,137,552 − 1 = 19.5%.
- Share of income from operations: changes in expected recoveries 96,924 / 153,282 = 63.2% in Q2 2026; 140,810 / 256,536 = 54.9% in H1 2026.
- Adjusted EBITDA less cash receipts less Adjusted operating expenses, FY2025: 1,315,474 − 1,298,123 = 17,351.

## Gaps

| Gap | Severity | Affected use | Action |
| --- | --- | --- | --- |
| Covenant ratio levels and the covenant definition of EBITDA are not supplied; compliance is stated only | High | Covenant headroom, CP-2 | Supply executed credit agreements and any compliance certificates; keep Not supplied |
| Amended European credit agreement (Exhibit 10.1 to the Q2 10-Q) not supplied | High | European facility terms after April 30, 2026 | Supply the agreement |
| Letters of credit drawn on the North American facility not supplied (only a 25.0 million sub-limit is stated) | Medium | Liquidity net of letters of credit | Supply facility usage detail |
| Colombian revolving credit facility maturity and terms not stated | Low | Maturity placement of 245 | Supply if material |
| Interest-bearing deposits (100,460) maturity and the AK Nordic AB funding terms not supplied | Medium | Debt perimeter, liquidity | Supply deposit maturity and funding detail |
| Discrete Q2 2026 and Q2 2025 cash flows not printed (year-to-date statements only); derivable from Q1 and H1 statements but not done here | Low | Quarterly cash flow analysis | Derive in a later step if needed |
| Quarterly Adjusted EBITDA not printed (last twelve months only) | Medium | Discrete quarter leverage and cover | Keep last twelve months basis |
| June 30, 2025 debt principal table and balance sheet not in the pack | Low | June 30, 2025 leverage | Not calculable beyond the carrying borrowings of 3,614,208 printed in the Q2 10-Q |
| ERC year rows in the 2026 10-Q tables begin at 2027 with no 2026 row; period covered by the first row not stated | Medium | ERC timing and borrowing base reading | Resolve from the 10-K convention or the issuer; do not assume |
| Components of the 17,351 difference between Adjusted EBITDA and cash receipts less Adjusted operating expenses for FY2025 not itemized | Low | EBITDA definition risk | Treat the two measures as distinct |
| Events after August 7, 2026, including any report for the quarter ended September 30, 2026, not supplied | Medium | Current leverage and liquidity at the as-of date | Supply later filings or confirm none |
| Ratings, market prices and valuation inputs not supplied | Low | Relative value | Not required for this module |

## Next module

- CP-1A: carry the April 30, 2026 European facility amendment, the Q4 2025 segment reorganization and the August 3, 2026 repurchase authorization as dated events; carry the European forecast review (348.5 million increase in European ERC; approximately 105 million positive adjustment in changes in expected future recoveries) as a business-context fact, not as earnings.
- CP-2: use the leverage, cover, liquidity and maturity tables here with their definition limits; do not compare the Adjusted EBITDA based ratios with the covenant limits; carry the missing covenant ratios, the unsupplied European amendment and the unsupplied letters of credit data as restrictions; use the Q2 10-Q for the maturity profile and not the 10-K principal payment table.
- CP-5: trace each figure to the cited page; the derived values are in Calculations C1 to C9.
