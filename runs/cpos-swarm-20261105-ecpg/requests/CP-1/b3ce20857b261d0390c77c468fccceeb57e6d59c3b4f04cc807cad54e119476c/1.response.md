## Request

Issuer: ENCORE CAPITAL GROUP INC (ticker ECPG, issuer id ecpg). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD; the filings print US$ in thousands, and this handoff keeps US$ thousands for statement amounts and states US$m where a chart table asks for it. Current period: Q3 2026 (quarter ended 2026-09-30); prior period: FY2025.

Task: extract and structure the financial base from the filed statements and releases (income, balance sheet, cash flow, Adjusted EBITDA, debt by instrument, liquidity, maturities), review definitions, and give the leverage, interest cover, liquidity and maturity series for the credit snapshot. Perimeter: Encore Capital Group, Inc. consolidated, which includes the consolidated securitisation vehicles (the Cabot securitisation vehicle and the U.S. financing subsidiary), and the restricted group of the Global Senior Facility and the Senior Secured Notes is a sub-perimeter whose own figures are not printed.

The upstream source-readiness handoff is relied on: it found the source set READY_WITH_LIMITATIONS for this module, with no reported covenant ratios, no letters of credit figure, no ratings, no executed agreements and no discrete fourth quarter or last-twelve-months figure printed. This handoff does not correct that handoff; it confirms those limits and adds the extraction below.

## Sources

### Issuer sources relied on

| Source name | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_ecpg-20251231.htm.jsonl | 34ff88efcf361fa9aeafcc136a26a65107894a6eccc6d81525528ab9ff5d0d5d | FY2025 and FY2024 statements, Adjusted EBITDA, borrowings note, contractual obligations, year-end 2025 liquidity |
| 10-Q_2026-03-31_ecpg-20260331.htm.jsonl | 78afd13c000763f54a4aba736b73215614c4d9f919d4b8b0b086fe99e4f165ec | Q1 2026 statements, Adjusted EBITDA, borrowings, capacity |
| 10-Q_2026-06-30_ecpg-20260630.htm.jsonl | b9101ef4153230b6bac0c232b19beeb72b0be52512669a3b5f826ec55ac35d2f | Q2 2026 and six month 2026 statements, Adjusted EBITDA, borrowings, capacity |
| 10-Q_2026-09-30_ecpg-20260930.htm.jsonl | 732e46e0fdf56804d0e4376f251fca05b1fb9b8a2542ea7489a917605ffcd2f2 | Q3 2026 and nine month 2026 statements, Adjusted EBITDA, borrowings by instrument, liquidity, commitments, hedging |
| EX-99.1_2026-05-06_exhibit991ecpgq12026earnin.htm.jsonl | 52e6f2f8497b4c376deb09345bbca84227e91bc87999210c914e4332ca310a30 | Q1 2026 collections and ERC (attributed management release) |
| EX-99.1_2026-08-05_exhibit991ecpgq22026earnin.htm.jsonl | c912421ecebbdeab115865e4c75e4397e60fc06977b32c09b5fe72e8026c1bc7 | Q2 2026 collections and ERC; refinancing cost statement |
| EX-99.1_2026-11-04_exhibit991ecpgq32026earnin.htm.jsonl | 55d38b7d96066eb32a5cc33bf9d08102e9a0e050298f0028532e13cfed8c82ea | Q3 2026 collections, ERC, Adjusted EBITDA agreement check, guidance |

The context file (sha256 fb9232dcd1631add7bbcdb6eec1a7bd4a0eec6466deb6a3148ebd7ee287099b7) holds run settings only and is not issuer evidence.

### Handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 5bceebdd4466b332506213f28eb141aebd7b80ad1c46615c0f3d948e9eb94d38 | Source readiness, gaps and limitations carried forward |

Locators are retained `page:N` spans of each source, not printed page numbers. Source labels used below: 10-K is the FY2025 annual report; Q1 10-Q, Q2 10-Q and Q3 10-Q are the quarterly reports; Q1, Q2 and Q3 release are the three earnings releases. Every page and quote below was opened in the retained text.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Debt rose over 2026 but earnings grew faster: total debt to Adjusted EBITDA fell from 5.96x at FY2025 to 5.13x at the last twelve months to Q3 2026, while revolver availability fell to 510.2 US$m. | Medium | The earnings measure is the company's own Adjusted EBITDA, and no covenant ratios or executed agreements are available. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Leverage and cash interest cover both improved through 2026, to 5.13x and 3.07x on a last twelve months basis. | Improving service capacity, but on a company-defined earnings measure. | Medium |
| Revolver availability fell sharply in Q3 2026 after the convertible notes were settled in cash from revolver drawings. | Less undrawn liquidity, with no debt maturing before 2028 in the notes tables. | High |
| Adjusted EBITDA includes forecast-driven revenue that is deducted as non-cash in operating cash flow, and portfolio purchases sit outside it. | Headline leverage overstates cash earnings capacity available for debt service. | High |
| Covenant tests are described but the issuer's reported ratios are not available. | Headroom cannot be measured; only a compliance statement exists. | Medium |

### Financial base view

For ENCORE CAPITAL GROUP INC the filed statements support a clear financial base through Q3 2026, with the limits stated here. On the company's own Adjusted EBITDA, last twelve months leverage on gross debt fell from 5.96x at FY2025 to 5.13x at Q3 2026 and net leverage from 5.73x to 4.94x, because last twelve months Adjusted EBITDA grew from 676,958 to 831,829 (US$ thousands) while principal debt rose from 4,033,394 to 4,267,981. Cash interest cover on the same basis rose from 2.61x to 3.07x. Liquidity narrowed: the issuer-stated availability under the Global Senior Facility moved from 814.3 US$m at FY2025 to 510.2 US$m at Q3 2026 as the revolver funded the settlement of the 2029 convertible notes, and the other two debt facilities are fully drawn. The maturity profile is long: the notes tables show no instrument maturing before 2028, and the largest single maturity year is 2029 (the revolver and the U.S. Facility). The measure itself carries definition risk: roughly two fifths of nine month 2026 Adjusted EBITDA is revenue from changes in recoveries that the cash flow statement deducts as non-cash, and the large purchases of receivable portfolios needed to sustain collections sit in investing cash flow, outside both Adjusted EBITDA and operating cash flow. Covenant headroom is not measurable because only limits and a compliance statement are printed. Overall this is a usable base for leverage, coverage and liquidity work, with Medium confidence on the headline ratios.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 11.14 | 10.54 | x | Principal debt 3,710,018 (10-K page:105 "4,033,394 3,710,018") less cash 199,865 (10-K page:86 "Cash and cash equivalents $ 156,784 $ 199,865"); Adjusted EBITDA 332,928 (10-K page:62 "Adjusted EBITDA $ 676,958 $ 332,928 $ 333,615"). US$ thousands as printed. FY2024 Adjusted EBITDA adds back goodwill impairment of 100,600 and asset impairment of 18,544 and carries negative changes in recoveries of (89,740), so it is not like for like with later periods. |
| FY2025 | 5.96 | 5.73 | x | Principal debt 4,033,394 (10-K page:105) less cash 156,784 (10-K page:86); Adjusted EBITDA 676,958 (10-K page:62). Company-defined Adjusted EBITDA, not covenant EBITDA. Principal includes consolidated non-recourse securitisation debt. |
| LTM Q1 2026 | 5.54 | 5.23 | x | Principal debt 4,063,717 (Q1 10-Q page:16 "4,063,717 4,033,394") less cash 227,204 (Q1 10-Q page:2 "Cash and cash equivalents $ 227,204 $ 156,784"); LTM Adjusted EBITDA 733,084 calculated as FY2025 plus Q1 2026 196,586 less Q1 2025 140,460 (Q1 10-Q page:39 "Adjusted EBITDA $ 196,586 $ 140,460"). LTM is a calculation, not a printed figure. |
| LTM Q2 2026 | 5.46 | 5.22 | x | Principal debt 4,213,379 (Q2 10-Q page:17 "4,213,379 4,033,394") less cash 182,932 (Q2 10-Q page:2 "Cash and cash equivalents $ 182,932 $ 156,784"); LTM Adjusted EBITDA 771,414 calculated as FY2025 plus six months 2026 399,149 less six months 2025 304,693 (Q2 10-Q page:46 "Adjusted EBITDA $ 202,563 $ 164,233 $ 399,149 $ 304,693"). Includes the 30,533 loss on extinguishment added back. |
| LTM Q3 2026 | 5.13 | 4.94 | x | Principal debt 4,267,981 (Q3 10-Q page:19 "4,267,981 4,033,394") less cash 158,425 (Q3 10-Q page:2 "Cash and cash equivalents $ 158,425 $ 156,784"); LTM Adjusted EBITDA 831,829 calculated as FY2025 plus nine months 2026 644,320 less nine months 2025 489,449 (Q3 10-Q page:51 "Adjusted EBITDA $ 245,171 $ 184,756 $ 644,320 $ 489,449"). Cash includes cash of consolidated securitisation vehicles and client cash, not separated; carrying borrowings are 4,237,800 after 30,181 of discount and costs. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 1.58 | x | Adjusted EBITDA 332,928 (10-K page:62) over cash paid for interest 210,580 (10-K page:89 "Cash paid for interest $ 259,812 $ 210,580 $ 163,815"). Same non-comparability of FY2024 Adjusted EBITDA as in the leverage table. |
| FY2025 | 2.61 | x | Adjusted EBITDA 676,958 (10-K page:62) over cash paid for interest 259,812 (10-K page:89). |
| LTM Q1 2026 | 2.87 | x | LTM Adjusted EBITDA 733,084 over LTM cash interest 255,852, calculated as FY2025 259,812 plus Q1 2026 37,343 less Q1 2025 41,303 (Q1 10-Q page:5 "Cash paid for interest $ 37,343 $ 41,303"). |
| LTM Q2 2026 | 2.81 | x | LTM Adjusted EBITDA 771,414 over LTM cash interest 274,701, calculated as FY2025 259,812 plus six months 2026 148,719 less six months 2025 133,830 (Q2 10-Q page:5 "Cash paid for interest $ 148,719 $ 133,830"). |
| LTM Q3 2026 | 3.07 | x | LTM Adjusted EBITDA 831,829 over LTM cash interest 270,515, calculated as FY2025 259,812 plus nine months 2026 183,459 less nine months 2025 172,756 (Q3 10-Q page:6 "Cash paid for interest $ 183,459 $ 172,756"). Cash interest is lumpy because coupons fall on semi-annual dates, so single quarters are not used. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (2025-12-31) | 156.8 | 814.3 | US$m | Cash 156,784 thousand (10-K page:86). Undrawn is the issuer-stated Global Senior Facility availability (10-K page:107 "was approximately $814.3 million as of December 31, 2025"), after covenants. Commitment less drawn would be 853.0 (1,485.0 less 632.0); the difference is unexplained in the sources. The Cabot facility is drawn to its commitment (10-K: outstanding £255.0 million of a £255.0 million commitment); the U.S. Facility is drawn to its 450.0 US$m commitment (10-K page:110 "to increase the committed amount from $300.0 million to $450.0 million" and outstanding of $450.0 million). |
| Q1 2026 (2026-03-31) | 227.2 | 791.3 | US$m | Cash 227,204 thousand (Q1 10-Q page:2). Issuer-stated availability (Q1 10-Q page:17 "was approximately $791.3 million as of March 31, 2026"). Commitment less drawn would be 803.7; difference unexplained. |
| Q2 2026 (2026-06-30) | 182.9 | 793.4 | US$m | Cash 182,932 thousand (Q2 10-Q page:2). Issuer-stated availability (Q2 10-Q page:18 "was approximately $793.4 million as of June 30, 2026"), equal to commitment less drawn. |
| Q3 2026 (2026-09-30) | 158.4 | 510.2 | US$m | Cash 158,425 thousand (Q3 10-Q page:2), of which 54.8 is held by U.S.-based entities and 103.6 by foreign entities (Q3 10-Q page:58). Issuer-stated availability (Q3 10-Q page:20 "was approximately $510.2 million as of September"), equal to commitment of 1,485.0 less drawn 974.8. Cash includes consolidated securitisation vehicle cash of 48,558 thousand and client cash of 10.4 US$m, not separated. No letters of credit figure is supplied. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Within 12 months of 2025-12-31 | 21.0 | US$m | 10-K page:71 "Principal payments on debt $ 4,032,798 $ 21,015 $ 4,011,783"; contractual obligations table at FY2025, principal only. |
| 2026 and 2027 (as at 2026-09-30) | Not supplied: no instrument in the Q3 10-Q borrowings tables matures in these years, but the Other borrowings line (54.7) and finance leases carry no stated maturity, so a near-term amount cannot be excluded | US$m | Q3 10-Q page:19 "Other 54,714 52,926". No Q3 10-Q contractual obligations table is supplied. |
| 2028 | 331.6 | US$m | Q3 10-Q page:21 "Encore 2028 Notes $ 331,615 $ 336,803 GBP Jun 1, 2028" (sterling notes at the period-end rate). Excludes any outstanding amount of the 69.5 US$m revolver tranche that terminates in September 2028 (Q3 10-Q page:20), because outstanding by tranche is not supplied. |
| 2029 | 1424.8 | US$m | Global Senior Facility outstanding 974.8 (Q3 10-Q page:20 "matures in September 2029") plus U.S. Facility 450.0 (Q3 10-Q page:25 "to extend its maturity from October 2028 to October 2029"). The revolver is a drawn revolving facility assigned to its main termination date. |
| 2030 | 500.0 | US$m | Q3 10-Q page:21 "Encore 2030 Notes 500,000 500,000 USD May 15, 2030". |
| 2031 | 838.2 | US$m | Encore 2031 Notes 500.0 (Q3 10-Q page:21 "Encore 2031 Notes 500,000 500,000 USD Apr 15, 2031") plus Cabot securitisation senior facility 338.2 (Q3 10-Q page:25 "The Cabot Securitisation Senior Facility matures in January 2031"). |
| 2032 | 750.0 | US$m | Q3 10-Q page:21 "Encore 2032 Notes 750,000 — USD Jun 1, 2032". |
| 2033 | 368.3 | US$m | Q3 10-Q page:21 "Encore 2033 Floating Rate Notes 368,263 — EUR Jul 15, 2033" (euro notes at the period-end rate). |
| No stated maturity (Other borrowings and finance leases, as at 2026-09-30) | 55.1 | US$m | Q3 10-Q page:19 "Other 54,714 52,926" and "Finance lease liabilities 379 596"; maturities not itemised in the sources read. |

### Financials and credit metrics

US$ thousands as printed unless stated. Columns FY2024 and FY2025 are full years; Q1 to Q3 2026 are discrete quarters; 9M 2026 is nine months; LTM Q3 2026 is FY2025 plus 9M 2026 less 9M 2025 (calculated). Cells marked (c) are calculated here from printed figures, shown in the calculations. Balance sheet rows are instants at the period end, so the 9M 2026 and LTM columns repeat the Q3 2026 date as "same as Q3".

| Metric | FY2024 | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | 9M 2026 | LTM Q3 2026 | Source locators |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenues | 1,316,361 | 1,768,802 | 475,411 | 491,872 | 544,541 | 1,511,824 | 1,985,376 (c) | 10-K page:86; Q1 10-Q page:3; Q2 10-Q page:3; Q3 10-Q page:3 |
| of which changes in recoveries | (89,740) | 208,771 | 62,740 | 71,115 | 111,043 | 244,898 | 312,970 (c) | same statements |
| Income from operations | 157,330 | 626,647 | 183,992 | 186,902 | 230,605 | 601,499 | 774,892 (c) | 10-K page:87; Q1 10-Q page:3; Q2 10-Q page:3; Q3 10-Q page:3 |
| Interest expense | 252,545 | 293,910 | 73,050 | 73,907 | 72,299 | 219,256 | 294,451 (c) | same statements |
| Net income (loss) | (139,244) | 256,834 | 86,243 | 63,999 | 124,013 | 274,255 | 350,912 (c) | same statements |
| Adjusted EBITDA (company-defined) | 332,928 | 676,958 | 196,586 | 202,563 | 245,171 | 644,320 | 831,829 (c) | 10-K page:62; Q1 10-Q page:39; Q2 10-Q page:46; Q3 10-Q page:51 |
| Cash paid for interest | 210,580 | 259,812 | 37,343 | 111,376 (c) | 34,740 (c) | 183,459 | 270,515 (c) | 10-K page:89; Q1 10-Q page:5; Q2 10-Q page:5; Q3 10-Q page:6 |
| Net cash provided by operating activities | 156,168 | 153,199 | 82,326 | (29,380) (c) | 106,684 (c) | 159,630 | 176,441 (c) | 10-K page:88; Q1 10-Q page:4; Q2 10-Q page:5; Q3 10-Q page:5 |
| Net cash used in investing activities | (440,430) | (242,586) | (27,407) | (103,243) (c) | (44,988) (c) | (175,638) | (202,675) (c) | same statements |
| Purchases of receivable portfolios, net of put-backs (cash flow) | 1,336,442 | 1,389,064 | 359,463 | 440,838 (c) | 386,771 (c) | 1,187,072 | 1,509,913 (c) | same statements |
| Collections applied to receivable portfolios (cash flow) | 859,911 | 1,136,991 | 328,395 | 336,622 (c) | 339,431 | 1,004,448 | 1,295,147 (c) | same statements; Q3 10-Q page:18 |
| Cash and cash equivalents | 199,865 | 156,784 | 227,204 | 182,932 | 158,425 | same as Q3 | same as Q3 | 10-K page:86; Q1 10-Q page:2; Q2 10-Q page:2; Q3 10-Q page:2 |
| Principal debt before discount and costs | 3,710,018 | 4,033,394 | 4,063,717 | 4,213,379 | 4,267,981 | same as Q3 | same as Q3 | 10-K page:105; Q1 10-Q page:16; Q2 10-Q page:17; Q3 10-Q page:19 |
| Borrowings, carrying amount | 3,672,762 | 4,001,293 | 4,033,301 | 4,179,515 | 4,237,800 | same as Q3 | same as Q3 | balance sheets, same pages as cash |
| Total stockholders' equity | 767,331 | 976,750 | 1,034,808 | 1,078,717 | 1,078,682 | same as Q3 | same as Q3 | 10-K page:86; Q1 10-Q page:3; Q2 10-Q page:3; Q3 10-Q page:3 |
| Receivable portfolios, net | 3,776,369 | 4,371,532 | 4,437,415 | 4,609,705 | 4,763,412 | same as Q3 | same as Q3 | balance sheets |
| Total estimated remaining collections (ERC) | Not supplied: not read for FY2024 in this extraction | 9,684,339 | 9,825,266 | 10,178,335 | 10,451,677 | same as Q3 | same as Q3 | 10-K page:65 "Total ERC"; Q3 10-Q page:54; releases page:2 |
| Principal debt / Adjusted EBITDA (x, LTM basis) | 11.14 (c) | 5.96 (c) | 5.54 (c) | 5.46 (c) | 5.13 (c) | not applicable | 5.13 (c) | see calculations |

### Debt by instrument at 2026-09-30

Principal amounts in US$ thousands; foreign currency instruments are translated by the issuer at period-end rates.

| Instrument | Obligor and ranking as printed | Amount | Rate | Maturity | Locator |
| --- | --- | --- | --- | --- | --- |
| Global Senior Facility (revolving, committed 1,485.0 US$m) | Encore as parent of the restricted group; guaranteed by material subsidiaries; secured on substantially all their assets; super senior to the notes on enforcement for shared collateral | 974,763 | Term SOFR plus 2.25% plus 0.10% adjustment spread; floor 0.00% | September 2029; a 69.5 US$m tranche terminates September 2028 | Q3 10-Q pages:19, 20 |
| Encore 2028 Notes (GBP) | Senior secured notes, same collateral, guarantees pari passu with the revolver | 331,615 | 4.250% | Jun 1, 2028 | Q3 10-Q page:21 |
| Encore 2030 Notes | same | 500,000 | 8.500% | May 15, 2030 | Q3 10-Q page:21 |
| Encore 2031 Notes | same | 500,000 | 6.625% | Apr 15, 2031 | Q3 10-Q page:21 |
| Encore 2032 Notes | same | 750,000 | 6.625% | Jun 1, 2032 | Q3 10-Q page:21 |
| Encore 2033 Floating Rate Notes (EUR) | same | 368,263 | three-month EURIBOR (0% floor) plus 3.250% | Jul 15, 2033 | Q3 10-Q page:21 |
| Cabot securitisation senior facility | Cabot Securitisation UK Ltd, indirect subsidiary and consolidated VIE; first ranking security over its assets | 338,247 | SONIA plus 3.00% | January 2031 | Q3 10-Q pages:19, 25 |
| U.S. facility | U.S. Financing Subsidiary, indirect subsidiary and consolidated VIE; first ranking security over its assets | 450,000 | Term SOFR plus 3.00% | October 2029 (extended in August 2026) | Q3 10-Q pages:19, 25 |
| Other borrowings | Not itemised in the sources read | 54,714 | Not supplied | Not supplied | Q3 10-Q page:19 |
| Finance lease liabilities | Not itemised | 379 | Not supplied | Not supplied | Q3 10-Q page:19 |
| Total principal | | 4,267,981 | | | Q3 10-Q page:19 |
| Convertible senior notes due 2029 | Redeemed 2026-09-24 | nil at 2026-09-30 (230,000 at 2025-12-31) | 4.000% | Mar 15, 2029 | Q3 10-Q pages:19, 24 |

### Definition review

- Adjusted EBITDA is defined by the company as net income before interest income and expense, taxes, depreciation and amortization, stock-based compensation, acquisition, integration and restructuring expenses and other non-recurring charges or gains (Q1 10-Q page:39, "Adjusted EBITDA. Management utilizes adjusted EBITDA (defined as net income before interest income and expense, taxes, depreciation and amortization"). It is a management measure, not a covenant measure; the covenant definitions are in executed agreements that are not supplied.
- Revenue inside Adjusted EBITDA includes changes in recoveries, which the cash flow statement removes as non-cash (Q3 10-Q page:3 "Changes in recoveries 111,043 63,636 244,898 140,699" and the cash flow adjustment on Q3 10-Q page:5). Nine month 2026 changes in recoveries of 244,898 are 38.0% of nine month Adjusted EBITDA of 644,320 (calculated). Forecast-driven revenue makes the measure more sensitive to collection forecast changes than a cash measure.
- Portfolio purchases are the core reinvestment of the business and are in investing cash flow, outside both Adjusted EBITDA and operating cash flow: nine month 2026 purchases of 1,187,072 compare with Adjusted EBITDA of 644,320 and operating cash flow of 159,630. Debt to Adjusted EBITDA therefore does not measure the cash left for debt service after reinvestment.
- Total debt here is principal before discount and costs, including finance leases, and includes consolidated securitisation debt of the Cabot vehicle and the U.S. subsidiary that is secured on its own assets; the balance sheet VIE table shows borrowings of 784,567 thousand (Q3 10-Q page:3). The restricted group perimeter's own debt, EBITDA and covenant ratios are not printed.
- Operating lease liabilities are not in total debt (operating lease right-of-use assets are in other assets, Q3 10-Q page:18). The undiscounted operating lease payments at FY2025 were 73,761 thousand (10-K page:71). Forward flow purchase commitments of 684.5 US$m minimum are outside debt (Q3 10-Q page:30).
- Foreign currency: sterling and euro instruments are translated at period-end rates (for example Q3 10-Q page:25, "approximately $338.2 million based on an exchange rate of $1.00 to £0.75"), so reported US$ debt moves with exchange rates. The EBITDA is in US$ after translation of European results.

### Cash flow and liquidity read

- Operating cash flow is small relative to Adjusted EBITDA and volatile by quarter. The sum of operating and investing cash flow was a deficit of 16,008 for nine months 2026 against a deficit of 79,161 for nine months 2025 (calculated), so the business consumed cash before financing in both periods while growing the portfolio balance.
- The revolver funded the 2026 refinancing and the convertible settlement. Drawings on the Global Senior Facility rose from 691,648 at Q2 2026 to 974,763 at Q3 2026, an increase of 283,115 (calculated), after the 2029 convertible notes were settled in cash for 367.9 US$m, partly offset by 31.8 US$m of capped call proceeds (Q3 10-Q page:24). Utilisation of the 1,485.0 US$m commitment was 65.6% at Q3 2026 against 42.6% at FY2025 (calculated); the loan to value covenant of 0.75 applies when utilisation exceeds 20% (Q3 10-Q page:20), so that covenant is live in every period shown.
- Fixed charge coverage covenant: at least 2.0 (Q3 10-Q page:20). The issuer's definition and reported ratio are not supplied, so headroom is Not calculable.
- Share repurchases are also financed from the revolver or cash: nine months 2026 repurchases were 73,993 in the cash flow statement (Q3 10-Q page:5 financing section), with remaining authority of 229.0 US$m (Q3 10-Q page:58).

### Refinancing events and subsequent events to the cutoff

- 2026-05-22: issued 750.0 US$m 6.625% Encore 2032 Notes at 100.000%, used to redeem the 500.0 US$m 9.250% Encore 2029 Notes; loss on extinguishment 28.0 US$m including a 23.1 US$m make-whole premium (Q3 10-Q page:22).
- 2026-05-28: issued 325.0 EUR m Encore 2033 Floating Rate Notes and redeemed the 415.0 EUR m Encore 2028 Floating Rate Notes using the proceeds and revolver drawings; loss on extinguishment 2.5 US$m (Q3 10-Q page:22). Total loss on extinguishment for nine months 2026 is 30,533 thousand (Q3 10-Q page:3), booked in Q2 2026.
- 2026-07-22 and 2026-09-24: called and settled the 2029 convertible notes in cash for 367.9 US$m; the 137.9 US$m excess over principal was charged to equity, not to the income statement (Q3 10-Q page:24).
- 2026-08-17: U.S. Facility amended, maturity extended from October 2028 to October 2029 and margin reduced from 3.50% to 3.00% (Q3 10-Q page:25).
- October 2026 (after the 2026-09-30 balance sheet date, before the cutoff): new interest rate swaps with 150.0 US$m notional replaced swaps that matured on 2026-10-27 (Q3 10-Q page:14).
- 2026-11-04: Q3 results and raised full-year 2026 guidance (Q3 release page:1), management forward-looking statement, not evidence of outcome.

### Evidence, risk mechanism and credit implication

- Evidence: Adjusted EBITDA last twelve months to Q3 2026 of 831,829 against principal debt of 4,267,981. Risk mechanism: the measure includes forecast-driven revenue and excludes the reinvestment spend that the model needs to replace runoff. Credit implication: the improvement in headline leverage is real on the filed numbers but overstates cash coverage; debt capacity should also be tested against collections and ERC.
- Evidence: revolver availability of 510.2 US$m at Q3 2026 against 814.3 US$m at FY2025, and all other facilities fully drawn. Risk mechanism: future portfolio purchases and refinancing are funded from the revolver, whose availability is covenant-limited and expires in 2029 (2028 for one tranche). Credit implication: liquidity headroom is thinner than a year ago, though no debt matures before 2028 in the notes tables.
- Evidence: a long list of senior secured instruments sharing collateral with a super senior revolver. Risk mechanism: enforcement proceeds on shared collateral go first to the revolver and super senior hedging. Credit implication: recovery for the senior secured notes depends on the revolver balance at default, which has risen.

## Calculations

All inputs are US$ thousands as printed unless stated; each result is computed from the figures cited above.

1. LTM Adjusted EBITDA = FY2025 + year to date 2026 − year to date 2025. Q1: 676,958 + 196,586 − 140,460 = 733,084. Q2: 676,958 + 399,149 − 304,693 = 771,414. Q3: 676,958 + 644,320 − 489,449 = 831,829. Quarterly check: 196,586 + 202,563 + 245,171 = 644,320, equal to the printed nine month figure.
2. LTM cash paid for interest: Q1: 259,812 + 37,343 − 41,303 = 255,852. Q2: 259,812 + 148,719 − 133,830 = 274,701. Q3: 259,812 + 183,459 − 172,756 = 270,515. Discrete quarters: Q2 = 148,719 − 37,343 = 111,376; Q3 = 183,459 − 148,719 = 34,740.
3. Net debt = principal debt − cash. FY2024: 3,710,018 − 199,865 = 3,510,153. FY2025: 4,033,394 − 156,784 = 3,876,610. Q1: 4,063,717 − 227,204 = 3,836,513. Q2: 4,213,379 − 182,932 = 4,030,447. Q3: 4,267,981 − 158,425 = 4,109,556.
4. Total debt / Adjusted EBITDA: FY2024 3,710,018 / 332,928 = 11.14x; FY2025 4,033,394 / 676,958 = 5.96x; Q1 4,063,717 / 733,084 = 5.54x; Q2 4,213,379 / 771,414 = 5.46x; Q3 4,267,981 / 831,829 = 5.13x. Net: 3,510,153 / 332,928 = 10.54x; 3,876,610 / 676,958 = 5.73x; 3,836,513 / 733,084 = 5.23x; 4,030,447 / 771,414 = 5.22x; 4,109,556 / 831,829 = 4.94x. On carrying borrowings of 4,237,800 the Q3 ratio is 5.09x.
5. EBITDA / cash interest: FY2024 332,928 / 210,580 = 1.58x; FY2025 676,958 / 259,812 = 2.61x; Q1 733,084 / 255,852 = 2.87x; Q2 771,414 / 274,701 = 2.81x; Q3 831,829 / 270,515 = 3.07x.
6. Other LTM Q3 2026 figures: revenue 1,768,802 + 1,511,824 − 1,295,250 = 1,985,376; changes in recoveries 208,771 + 244,898 − 140,699 = 312,970; income from operations 626,647 + 601,499 − 453,254 = 774,892; interest expense 293,910 + 219,256 − 218,715 = 294,451; net income 256,834 + 274,255 − 180,177 = 350,912; operating cash flow 153,199 + 159,630 − 136,388 = 176,441; investing cash flow (242,586) + (175,638) − (215,549) = (202,675); purchases 1,389,064 + 1,187,072 − 1,066,223 = 1,509,913; collections applied 1,136,991 + 1,004,448 − 846,292 = 1,295,147.
7. Discrete Q2 and Q3 cash flow items from year to date figures: operating Q2 = 52,946 − 82,326 = (29,380), Q3 = 159,630 − 52,946 = 106,684; investing Q2 = (130,650) − (27,407) = (103,243), Q3 = (175,638) − (130,650) = (44,988); purchases Q2 = 800,301 − 359,463 = 440,838, Q3 = 1,187,072 − 800,301 = 386,771; collections applied Q2 = 665,017 − 328,395 = 336,622 (Q3 printed 339,431, and 1,004,448 − 665,017 = 339,431).
8. Share of nine month Adjusted EBITDA from changes in recoveries: 244,898 / 644,320 = 38.0%.
9. Operating plus investing cash flow: nine months 2026 159,630 + (175,638) = (16,008); nine months 2025 136,388 + (215,549) = (79,161).
10. Revolver: commitment less drawn at Q3 2026: 1,485.0 − 974.763 = 510.237, agreeing with the stated 510.2 US$m. At Q2: 1,485.0 − 691.648 = 793.352 against stated 793.4. At Q1: 1,485.0 − 681.267 = 803.733 against stated 791.3 (difference 12.4). At FY2025: 1,485.0 − 631.998 = 853.002 against stated 814.3 (difference 38.7). Utilisation: 974.763 / 1,485.0 = 65.6% at Q3 2026; 631.998 / 1,485.0 = 42.6% at FY2025. Drawing increase Q2 to Q3: 974,763 − 691,648 = 283,115.
11. Maturities in US$m at 2026-09-30: 2029 = 974.763 + 450.000 = 1,424.763; 2031 = 500.000 + 338.247 = 838.247; undated = 54.714 + 0.379 = 55.093. Total check: 331.615 + 1,424.763 + 500.000 + 838.247 + 750.000 + 368.263 + 55.093 = 4,267.981, equal to the printed principal total of 4,267,981 thousand. Notes subtotal check: 331,615 + 500,000 + 500,000 + 750,000 + 368,263 = 2,449,878, equal to the printed total on Q3 10-Q page:21.
12. Consistency of year-end 2025 debt across filings: total principal 4,033,394 and carrying 4,001,293 are the same in the 10-K and in the Q1, Q2 and Q3 10-Q comparatives. Difference between principal and carrying at Q3: 4,267,981 − 4,237,800 = 30,181, equal to the printed discount and costs.

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Covenant ratios (loan to value, secured revolver loan to value, fixed charge coverage) are not reported, only limits and a material compliance statement. | Headroom Not calculable. | Obtain compliance certificate and agreement definitions. |
| Letters of credit or ancillary usage under the Global Senior Facility: not supplied after searching the sources. | The difference between commitment less drawn and stated availability at FY2025 (38.7) and Q1 2026 (12.4) is unexplained. | Ask the issuer for facility utilisation detail. |
| Restricted group perimeter: its debt, EBITDA and cash flow are not printed. | Leverage is for the consolidated perimeter, including non-recourse securitisation debt. | Obtain restricted group financials if the credit view is at that level. |
| Composition and maturity of Other borrowings (54.7 US$m) and finance leases. | Near-term maturities in 2026 and 2027 cannot be fully excluded. | Read the debt note detail in the filings or ask the issuer. |
| Outstanding amount of the revolver tranche terminating in September 2028. | 2028 and 2029 maturity split is approximate. | Obtain the facility schedule. |
| LTM and discrete fourth quarter figures are calculated, not printed. | The series rests on year to date subtraction. | State as calculation; already shown. |
| FY2024 total ERC not read in this extraction. | No FY2024 collections coverage comparison. | Read the FY2025 10-K comparative ERC if needed. |
| Cash is not split into unrestricted cash and cash of consolidated vehicles or client cash. | Net debt may understate net leverage on a free cash basis. | Separate in the credit synthesis if material. |
| Ratings, market debt prices, executed agreements: not supplied (carried from the readiness handoff). | No market-implied or legal ranking view. | Supply them if required. |

## Next module

Pass the following forward to the business and transaction fact pack and the credit synthesis. Use the Q3 2026 10-Q as the controlling source for current debt, liquidity and maturities, and the 10-K only for FY2025 and FY2024 comparatives. Treat the leverage, interest cover, liquidity and maturity tables above as the canonical series, each labelled by period and basis (LTM figures are calculations). Carry forward the definition risks (forecast-driven revenue inside Adjusted EBITDA, purchases outside it, consolidated securitisation debt inside it) and the gaps above, in particular covenant headroom Not calculable, the unexplained difference between commitment less drawn and stated availability at FY2025 and Q1 2026, and the 2026 refinancing sequence ending with the cash settlement of the 2029 convertible notes from revolver drawings. Next evidence action: obtain the compliance certificate and the Global Senior Facility agreement.
