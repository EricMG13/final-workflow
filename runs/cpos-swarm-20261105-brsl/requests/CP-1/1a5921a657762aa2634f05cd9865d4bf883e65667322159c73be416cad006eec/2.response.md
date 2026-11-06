## Request

Module: financial base (reported statements, debt, liquidity, maturities, leverage and cover metrics) for Brightstar Lottery PLC (issuer id brsl, NYSE: BRSL), pathway credit snapshot, as-of date 2026-11-05, evidence cutoff 2026-11-05. The context names USD as the reporting currency, current period q2-2026 and prior period fy-2025. All figures below are US$ millions unless stated, from continuing operations unless stated (the gaming and digital business sold on July 1, 2025 is discontinued), on the consolidated perimeter of Brightstar Lottery PLC (the "Parent") and its consolidated subsidiaries, US GAAP. Periods used: FY2024 and FY2025 (years ended December 31, audited), six months 2025 and six months 2026 (H1, unaudited), and LTM to June 30, 2026 (FY2025 plus H1 2026 less H1 2025). Part of the debt is euro-denominated and is shown in dollars as the filings translate it.

This module consumes the source-readiness handoff and carries its limits forward: no filing after the August 4, 2026 interim report is supplied, covenant levels and debt documents are not supplied, and Adjusted EBITDA, net debt and net debt leverage exist only in management slide decks. No credit conclusion beyond the financial base is drawn here.

Short names used in locators: 20-F is the FY2025 annual report; Q1 6-K and Q2 6-K are the interim reports for March 31, 2026 and June 30, 2026; Q4 deck, Q1 deck and Q2 deck are the earnings presentations. A locator reads (source page:N, "exact words").

## Sources

### Issuer sources relied on

| Short name | Source file (exact name) | sha256 | Use in this module |
| --- | --- | --- | --- |
| 20-F | 20-F_2025-12-31_igt-20251231.htm.jsonl | 1c18bf53e9995ce6c2aca12af6c18a64523551fba3492e8f989685fea08386fa | Audited FY2025 and FY2024 statements, debt note, leases, liquidity, cash requirements |
| Q3-25 6-K | 6-K_2025-09-30_brightstar-9302025xform6k.htm.jsonl | d46e904b239bdfcdf629b7154b5f837586e94b09f3d9adb6cf2a3a22cad2c307 | Read for context only; no figure in this module is taken from it |
| Q1 6-K | 6-K_2026-03-31_brightstar-3312026xform6k.htm.jsonl | bd68ab805934e86ab47882d408ef93ab3b6ce1b76f45e4a9303ec66c324fbd07 | March 31, 2026 balance sheet, debt, liquidity, cash interest |
| Q2 6-K | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 59ad2951e3fb4482f8541a5bd23eebbb988b008e57b642801a0675f3dc319de2 | June 30, 2026 balance sheet, H1 2026 statements, debt, liquidity, subsequent events |
| Q4 deck | 6-K-EX-99.2_2025-12-31_q425earningsslidedeck-fi.htm.jsonl | 52d9fd83276756c04d4933b539c2d599c1b0335f475eb7ae194b8d0285bb64ab | FY2025 and FY2024 Adjusted EBITDA (management non-GAAP) |
| Q1 deck | 6-K-EX-99.2_2026-03-31_q126earningsslidedeckfin.htm.jsonl | 904bf049bdca8cf2ecdea2a5b2e5271032b7a15662b32cecb7e8b6ac25de48c2 | Q1 2026 and Q1 2025 Adjusted EBITDA, management pro forma leverage |
| Q2 deck | 6-K-EX-99.2_2026-06-30_q226earningsslidedeck-fi.htm.jsonl | 2e4571f9e2637bd424291bf68428c53b010290fd8734caabd6c6df90116096fc | H1 2026 and H1 2025 Adjusted EBITDA, management net debt leverage, outlook |

Original authority: the 20-F, Q1 6-K and Q2 6-K are filed statements and control their facts. The decks are issuer presentations: their Adjusted EBITDA, net debt, leverage, free cash flow and outlook figures are management claims, labelled as such below.

### Run settings (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context | 5dec6fdc4bf237796c486a0095b8a59b71b216970050467cf9aed314b06e0f82 |

### Handoffs

| Module | Handoff | sha256 |
| --- | --- | --- |
| CP-0 | Source readiness for Brightstar Lottery PLC | 2272d9d74d9d7f19568da51f3a2c80f84dc9432a75a7be1a1d26161cd2bf1768 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported net debt leverage is 3.24x at June 30, 2026 after the final Italian Lotto license payment, up from 2.44x at December 31, 2025. Liquidity is $1,742 million and no debt matures before 2027. | Medium | Adjusted EBITDA is a management measure, covenant levels are not supplied, and nothing after August 4, 2026 is covered. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The $1,675 million final license payment in April 2026 drove six-month operating cash flow to a $1,174 million outflow. | Free cash flow is negative on a reported basis; the year-end leverage of 2.44x did not reflect the $1,680 million payable. | High |
| Total debt at June 30, 2026 is $4,383 million principal, of which $2,883 million is euro-denominated; maturities start with $228 million in 2027. | Currency moves change dollar debt, and each 2028 to 2030 maturity is at least $798 million. | High |
| Adjusted EBITDA of $1,170 million for the last twelve months adds back $323 million of license-fee amortization. | Without that add-back, net debt leverage would be 4.48x, so the add-back drives the reported leverage. | Medium |
| Interest cover on cash interest is 6.09x for the last twelve months, against 5.26x for FY2025. | Cover is adequate on the management measure, but non-controlling interests take $163 million of cash distributions a year. | Medium |
| Liquidity is $558 million cash plus $1,185 million undrawn revolver, down from $3,036 million at December 31, 2025. | The Lotto payment consumed most of the cash buffer; the revolver now carries $604 million drawn. | High |

### Financial base view

The financial base is complete enough for the downstream credit work, with three restrictions. First, the reported picture is a company that has just paid a very large one-off cash item: the final Italian Lotto license installment of $1,675 million in April 2026, which turned six-month operating cash flow to a $1,174 million outflow and lifted net debt from $2,732 million to $3,796 million between December 31, 2025 and June 30, 2026. Net debt leverage on management's definition moved from 2.44x to 3.24x, and the December 2025 figure sat beside a $1,680 million payable to the Italian regulator that was outside debt. Second, the leverage and cover ratios rest on Adjusted EBITDA, a management non-GAAP measure that adds back amortization of upfront license fees, and the filings supply no covenant thresholds against which to judge headroom. Third, the capital structure is mainly senior secured, mixed in currency, with about two thirds of principal in euros, and cash distributions to non-controlling interests are a recurring claim on consolidated cash flow. Liquidity of $1,742 million and a first maturity of $228 million in 2027 give near-term room, but the evidence ends at the August 4, 2026 interim report.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 (December 31, 2024) | 4.58 | 4.08 | x | Calculated: carrying debt 5,361 and net debt 4,777 (carrying debt less cash 584) over management Adjusted EBITDA 1,170; Adjusted EBITDA is a deck figure; the Q4 deck prints 4.1x |
| FY2025 (December 31, 2025) | 3.73 | 2.44 | x | Calculated: carrying debt 4,178 and net debt 2,732 over Adjusted EBITDA 1,121; excludes the 1,680 payable to the Italian regulator; the Q4 deck prints net debt 2,723 and 2.4x, a 9 difference to the filing-derived 2,732 |
| LTM March 31, 2026 | 3.46 | 2.38 | x | Calculated: carrying debt 4,008 and net debt 2,759 over LTM Adjusted EBITDA 1,158 (1,121 + 287 - 250); includes 1,644 payable to the Italian regulator outside debt; the Q1 deck prints 2.4x and about 3.5x pro forma |
| LTM June 30, 2026 | 3.72 | 3.24 | x | Calculated: carrying debt 4,354 and net debt 3,796 over LTM Adjusted EBITDA 1,170 (1,121 + 573 - 524); matches the Q2 deck figure of 3.24x; no covenant definition applied |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 5.29 | x | Calculated: Adjusted EBITDA 1,170 over cash interest paid 221 (continuing operations); management EBITDA, not covenant EBITDA |
| FY2025 | 5.26 | x | Calculated: Adjusted EBITDA 1,121 over cash interest paid 213 (continuing operations); management EBITDA, not covenant EBITDA |
| LTM March 31, 2026 | 6.09 | x | Calculated: LTM Adjusted EBITDA 1,158 over LTM cash interest 190 (213 + 49 - 72); management EBITDA |
| LTM June 30, 2026 | 6.09 | x | Calculated: LTM Adjusted EBITDA 1,170 over LTM cash interest 192 (213 + 68 - 89); management EBITDA; the revolver and term loan covenant uses net interest costs, whose definition is not supplied |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| December 31, 2024 | 584 | 1,364 | US$m | As printed in the 20-F liquidity table (total 1,948); excludes restricted cash 120; facilities were the earlier revolvers due July 2027 |
| December 31, 2025 | 1,446 | 1,590 | US$m | As printed (total 3,036); excludes restricted cash 54; the 1,680 payable to the Italian regulator was due in 2026; no letters of credit outstanding under the revolvers |
| March 31, 2026 | 1,249 | 1,570 | US$m | As printed in the Q1 6-K (total 2,818, components sum to 2,819 by rounding); excludes restricted cash 25; before the April 2026 Lotto payment |
| June 30, 2026 | 558 | 1,185 | US$m | As printed in the Q2 6-K (total 1,742, components sum to 1,743 by rounding); new revolvers due March 2031 with 604 drawn; letters of credit under the new revolvers are not stated; about 40 of cash sits in countries with transfer restrictions |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remainder of 2026 | 0 | US$m | Principal at June 30, 2026, printed as a dash (nil) in the Q2 6-K maturity table; euro debt translated at the June 30, 2026 rate |
| 2027 | 228 | US$m | Principal at June 30, 2026, all euro-denominated (term loan installment due September 2027) |
| 2028 | 798 | US$m | Principal at June 30, 2026, all euro-denominated (2.375% euro notes and term loan installment) |
| 2029 | 978 | US$m | Principal at June 30, 2026: 750 dollar notes and 228 euro term loan installment |
| 2030 | 1,025 | US$m | Principal at June 30, 2026, all euro-denominated (4.250% euro notes and final term loan installments) |
| 2031 and thereafter | 1,354 | US$m | Principal at June 30, 2026: 750 dollar notes due 2033 and 604 drawn on the revolver due March 2031; the revolver can be redrawn or repaid before maturity |

### Financials and credit metrics

| Metric | FY2024 | FY2025 | H1 2025 | H1 2026 | LTM June 30, 2026 | Basis |
| --- | --- | --- | --- | --- | --- | --- |
| Total revenue | 2,512 | 2,511 | 1,214 | 1,171 | 2,468 | Reported; LTM = FY2025 + H1 2026 - H1 2025; revenue is net of upfront license fee amortization |
| Income from continuing operations | 271 | 135 | (52) | 119 | 306 | Reported; LTM calculated; includes foreign exchange loss 124 in FY2025 and gain 16 in H1 2026 |
| Adjusted EBITDA (management non-GAAP) | 1,170 | 1,121 | 524 | 573 | 1,170 | Deck figures; LTM calculated; not in any filed statement |
| Adjusted EBITDA margin on revenue | 46.6% | 44.6% | 43.2% | 48.9% | 47.4% | Calculated from the two rows above |
| Of which add-back: amortization of upfront license fees | 198 | 223 | 101 | 201 | 323 | Reported in cash flow statements; LTM calculated |
| Interest expense, net | 206 | 172 | 94 | 92 | 170 | Reported; LTM calculated |
| Cash interest paid | 221 | 213 | 89 | 68 | 192 | Reported supplemental cash flow disclosure, continuing operations; LTM calculated |
| Cash income taxes paid | 241 | 220 | 32 | 16 | 204 | Reported; LTM calculated |
| Net cash from operating activities, continuing | 709 | (193) | 473 | (1,174) | (1,840) | Reported; LTM calculated |
| Of which Italian Lotto license payments | Nil | (926) | Nil | (1,675) | (2,601) | Reported as a separate operating line; nil is printed as a dash |
| Operating cash flow excluding Lotto license payments | 709 | 733 | 473 | 501 | 761 | Calculated; FY2025 733 and H1 2026 501 also appear in the 20-F and Q2 deck |
| Capital expenditures | (149) | (316) | (174) | (232) | (374) | Reported; LTM calculated |
| Free cash flow (operating cash flow less capex) | 560 | (509) | 299 | (1,406) | (2,214) | Calculated; FY2024, FY2025 and H1 2026 match the decks |
| Free cash flow excluding Lotto license payments | 560 | 417 | 299 | 269 | 387 | Calculated |
| Dividends paid to shareholders | (161) | (770) | (81) | (85) | (774) | Reported; FY2025 includes a 600 special dividend stated in the Q4 deck |
| Share repurchases | Nil | (271) | Nil | (45) | (316) | Reported; nil is printed as a dash |
| Dividends paid to non-controlling interests | (159) | (163) | (163) | (163) | (163) | Reported; LTM calculated |
| Capital increase from non-controlling interests | 2 | 386 | 178 | 650 | 858 | Reported; LTM calculated; partners funded part of the Lotto payment |
| Cash and cash equivalents (period end) | 584 | 1,446 | Not supplied | 558 | Not applicable | Balance sheet dates are December 31, 2024, December 31, 2025 and June 30, 2026; no June 30, 2025 balance sheet is in the pack |
| Restricted cash (period end) | 120 | 54 | Not supplied | 21 | Not applicable | Balance sheets; not included in liquidity |
| Total debt, carrying value | 5,361 | 4,178 | Not supplied | 4,354 | 4,354 | Debt notes; net of issuance costs |
| Total debt, principal | 5,396 | 4,203 | Not supplied | 4,383 | 4,383 | Debt notes; euro debt translated at period-end rates |
| Net debt (carrying debt less cash) | 4,777 | 2,732 | Not supplied | 3,796 | 3,796 | Calculated on management's definition |
| Total debt / Adjusted EBITDA | 4.58x | 3.73x | Not applicable | Not applicable | 3.72x | Calculated on carrying value |
| Net debt / Adjusted EBITDA | 4.08x | 2.44x | Not applicable | Not applicable | 3.24x | Calculated; decks print 4.1x, 2.4x and 3.24x |
| Adjusted EBITDA / cash interest | 5.29x | 5.26x | Not applicable | Not applicable | 6.09x | Calculated |
| Payable to the Italian regulator (outside debt) | Nil | 1,680 | Not supplied | Nil | Not applicable | Balance sheets; paid April 24, 2026 |
| Non-controlling interests (equity) | 409 | 715 | 481 | 1,173 | Not applicable | Equity statements; period-end balances |
| Covenant ratios as reported by the company | Not supplied | Not supplied | Not supplied | Not supplied | Not supplied | Covenant levels and definitions are not in the pack |

### Debt instruments and security

| Instrument | Issuer or borrower | Principal June 30, 2026 | Carrying June 30, 2026 | Principal December 31, 2025 | Maturity | Security and guarantee |
| --- | --- | --- | --- | --- | --- | --- |
| 2.375% Senior Secured Euro Notes | Parent | 570 | 568 | 588 | April 2028 | Secured; guaranteed by certain subsidiaries |
| 5.250% Senior Secured U.S. Dollar Notes | Parent | 750 | 747 | 750 | January 2029 | Secured; guaranteed by certain subsidiaries |
| 4.250% Senior Secured Euro Notes | Brightstar Lottery Holdings B.V. | 570 | 564 | 588 | March 2030 | Secured; guaranteed by the Parent and certain subsidiaries |
| 5.750% Senior Secured U.S. Dollar Notes | Parent and a co-issuer named in two spellings in the 20-F | 750 | 743 | 750 | January 2033 | Secured; guaranteed by the Parent and certain of its other subsidiaries per the 20-F table text |
| Euro Term Loan Facilities | Brightstar Lottery S.p.A. | 1,139 | 1,135 | 1,175 | September 2030 | Secured; guaranteed by the Parent and certain subsidiaries; installments from September 2027 |
| Euro Term Loan Facility due January 2027 | Brightstar Lottery Holdings B.V. | Nil | Nil | 353 | January 2027 | Fully repaid by April 2026 |
| Revolving Credit Facility B | Parent and subsidiaries | 604 | 597 | Nil | March 2031 | Senior secured, pari passu; drawn |
| Revolving Credit Facility A | Parent and subsidiaries | Nil | Nil | Nil | March 2031 | Senior secured, pari passu; undrawn |
| Total debt | | 4,383 | 4,354 | 4,203 | | |

By currency at June 30, 2026, principal is 1,500 dollar-denominated and 2,883 euro-denominated, together 4,383 (Q2 6-K page:14, "Total principal amounts 1,500 2,883 4,383"). The December 31, 2025 principal of the January 2027 term loan is 235 long-term plus 118 current. Notes are secured by "the shares of Brightstar Lottery S.p.A., certain intercompany loans with principal balances in excess of $10 million, and certain accounts receivable" (20-F page:169). The Q2 6-K says the revolver obligations are guaranteed "subject to agreed guarantor coverage thresholds based on consolidated assets and adjusted EBITDA" (Q2 6-K page:15); the guarantors are not named. Debt is described as all senior secured; no unsecured or subordinated debt, and no structurally separate unrestricted group, appears in the debt note.

### Claims outside the debt figure

| Claim | Amount and date | Inside or outside debt | Locator |
| --- | --- | --- | --- |
| Payable to the Italian regulator (final Lotto installment) | 1,680 at December 31, 2025; nil at June 30, 2026 after payment of 1,675 on April 24, 2026 | Outside debt and outside net debt; the Q1 6-K shows 1,644 at March 31, 2026 | 20-F page:137; Q2 6-K page:3, page:12 |
| Operating and finance lease liabilities | 121 at December 31, 2025 (97 operating, 24 finance); June 30, 2026 lease liabilities not located; finance lease right-of-use assets rose to 86 from 20 | Outside debt | 20-F page:165; Q2 6-K page:12 |
| Receivables factoring | 264 factored in H1 2026 and 440 in FY2025; 78 and 149 collected on behalf of banks held in other current liabilities | Outside debt; cash from factoring sits in operating cash flow | Q2 6-K page:12; 20-F page:162 |
| Unconditional purchase obligations | About 64 at December 31, 2025 | Outside debt | 20-F page:59 |
| Capital expenditure for contract obligations | 190 expected in the second half of 2026 | Outside debt | Q2 6-K page:27 |
| Guarantee of a lease of the sold gaming business | Maximum exposure 94, liability 10 at June 30, 2026, partly offset by a bank letter of credit | Outside debt | Q2 6-K page:18 |
| Letters of credit | 263 outstanding at December 31, 2025, none under the revolvers | Outside debt; no reduction of revolver availability then | 20-F page:60, page:176 |
| Non-controlling interests | 1,173 equity at June 30, 2026; 163 cash distributions in H1 2026 | Outside debt; a claim on consolidated cash flow | Q2 6-K page:4, page:5 |
| Restructuring liability | 46 at June 30, 2026 | Outside debt | Q2 6-K page:14 |
| Declared shareholder distributions | Dividend of about 42 declared July 30, 2026, payable September 1, 2026; 186 left on the repurchase program at June 30, 2026 | Outside debt | Q2 6-K page:18, page:19 |
| Pensions and retiree medical | Not located in the financial statement notes of the 20-F or the interim reports (searched for pension in the statements and notes) | Not supplied | 20-F pages:76, 82, 93, 106, 112 are non-financial text |

### Covenants and restrictions

The revolver agreement "contains a maximum net leverage ratio covenant and a minimum interest coverage ratio covenant" (Q2 6-K page:15) and the borrowers "were in compliance with such covenants" at June 30, 2026 (Q2 6-K page:27). No threshold, step-down, covenant EBITDA definition or reported covenant ratio is printed, so headroom is Not calculable. The term loan agreements at December 31, 2025 limited dividends and share repurchases to "$400 million if any two" ratings are below Ba1/BB+ and $550 million if two are at or above that level, with the cap removed if two ratings are at or above Baa3/BBB- (20-F page:171); the ratings at that date were BBB- (Fitch), Ba1 (Moody's) and BB+ (S&P) (20-F page:168). In March 2026 the company amended certain provisions of the 2030 term loans "to align such provisions under the RCF Agreement" (Q2 6-K page:15) and the amended text is not supplied, so the current distribution cap cannot be stated.

### Definition and sensitivity review

| Measure | FY2025 | LTM June 30, 2026 | Basis |
| --- | --- | --- | --- |
| Management Adjusted EBITDA | 1,121 | 1,170 | Adds back foreign exchange, restructuring, stock-based compensation, other expense and amortization of upfront license fees |
| Less license-fee amortization add-back | 898 | 847 | Calculated: 1,121 - 223 and 1,170 - 323 |
| Net debt / EBITDA after removing that add-back | 3.04x | 4.48x | Calculated: 2,732 / 898 and 3,796 / 847 |
| EBITDA after removing that add-back / cash interest | 4.22x | 4.41x | Calculated: 898 / 213 and 847 / 192 |
| Net debt including the Italian regulator payable / Adjusted EBITDA | 3.94x | Not applicable | Calculated: (2,732 + 1,680) / 1,121; the payable was settled in 2026 |
| Net debt including lease liabilities / Adjusted EBITDA | 2.55x | Not supplied | Calculated: (2,732 + 121) / 1,121; June 30, 2026 lease liabilities not located |
| Net debt / (Adjusted EBITDA less non-controlling interest distributions) | Not applicable | 3.77x | Calculated: 3,796 / (1,170 - 163) using H1 2026 distributions of 163 as the LTM figure; both sides are 100% consolidated |

These are analyst sensitivities, not reported metrics and not covenant calculations. Amortization of upfront license fees is a non-cash reduction of revenue that arises from fees already paid in cash (926 in FY2025 and 1,675 in H1 2026); adding it back is management's convention.

### Data quality and conflicts

- Net debt at December 31, 2025: the filing-derived figure is 2,732 (4,178 less 1,446); the Q4 deck prints "4,777 2,723 FY'24 FY'25" (Q4 deck page:6). The 9 difference does not change the printed 2.4x. The filing-derived figure is used.
- The final Lotto installment appears as 1,680 (payable at December 31, 2025), $1.68B (Q4 deck), $1.67B (Q1 deck and Q2 deck) and 1,675 (cash paid). The balance sheet and cash flow figures are each used for their own date; the filing does not state the translation bridge.
- The euro notes and term loans are translated at period-end rates that differ by date (the principal of the same euro term loans reads 1,175, 1,150 and 1,139 at December 31, 2025, March 31, 2026 and June 30, 2026), so dollar debt moves with the exchange rate without any repayment.
- Printed liquidity of 1,742 equals the revolver availability plus cash within rounding (1,743 summed). The printed 1,185 reconciles to $650 million plus the euro facility less 604 drawn only if the euro term loan principal of 1,139 is read as the dollar value of 1.0 billion euros; this is an inference from the 20-F repayment schedule of 200, 200, 200 and 400 million euros and is not stated in the Q2 6-K.
- The 20-F debt note names the 5.750% notes co-issuer "Brightstar Global Solutions Corporation" in its table and "Brightstar Lottery Global Solutions Corporation" in its text (20-F page:169); the debt table here carries both spellings.
- Where this module goes beyond the readiness handoff: the readiness handoff said period-end euro rates were not located; the implied rate for June 30, 2026 can be inferred from the euro term loan principal, as noted above. It also said whether letters of credit reduce the new revolver was unstated; that remains unstated, and the inferred reconciliation of 1,185 suggests no deduction but is not proof.

### Subsequent events and outlook

- After June 30, 2026 and before the August 4, 2026 report: a dividend of $0.23 per share, about 42 in total, declared July 30, 2026 and payable September 1, 2026 (Q2 6-K page:18); repurchases of 0.9 million shares for $10 million through July 31, 2026 (Q2 6-K page:19); payment of the Mexican tax settlement on July 10, 2026, amount not stated (Q2 6-K page:17).
- Management outlook for FY2026 (deck claims): revenue $2.50B to $2.55B, Adjusted EBITDA $1.16B to $1.19B, capex about $450M to $475M (Q2 deck page:7). These are forward-looking management statements, not evidence of results.
- Not supplied: any filing after August 4, 2026, including a third-quarter 2026 report; ratings after December 31, 2025.

## Calculations

All inputs are as printed in the cited sources; results are rounded to the stated precision from unrounded arithmetic.

| Calculation | Inputs and locators | Result |
| --- | --- | --- |
| LTM Adjusted EBITDA, June 30, 2026 | FY2025 1,121 (Q4 deck page:10); H1 2026 573 and H1 2025 524 (Q2 deck page:10): 1,121 + 573 - 524 | 1,170 |
| LTM Adjusted EBITDA, March 31, 2026 | FY2025 1,121; Q1 2026 287 and Q1 2025 250 (Q1 deck page:7): 1,121 + 287 - 250 | 1,158 |
| LTM cash interest, June 30, 2026 | FY2025 213 (20-F page:140); H1 2026 68 and H1 2025 89 (Q2 6-K page:6): 213 + 68 - 89 | 192 |
| LTM cash interest, March 31, 2026 | FY2025 213; Q1 2026 49 and Q1 2025 72 (Q1 6-K page:6): 213 + 49 - 72 | 190 |
| Net debt, June 30, 2026 | carrying debt 4,354 less cash 558 (Q2 6-K page:3, page:14) | 3,796 |
| Net debt, December 31, 2025 | carrying debt 4,178 less cash 1,446 (20-F page:137, page:168) | 2,732 |
| Net debt, December 31, 2024 | carrying debt 5,361 less cash 584 | 4,777 |
| Net debt, March 31, 2026 | carrying debt 4,008 less cash 1,249 (Q1 6-K page:3, page:12) | 2,759 |
| Net debt / EBITDA | 3,796 / 1,170; 2,732 / 1,121; 4,777 / 1,170; 2,759 / 1,158 | 3.24x; 2.44x; 4.08x; 2.38x |
| Total debt / EBITDA | 4,354 / 1,170; 4,178 / 1,121; 5,361 / 1,170; 4,008 / 1,158 | 3.72x; 3.73x; 4.58x; 3.46x |
| EBITDA / cash interest | 1,170 / 192; 1,121 / 213; 1,170 / 221; 1,158 / 190 | 6.09x; 5.26x; 5.29x; 6.09x |
| LTM revenue | 2,511 + 1,171 - 1,214 | 2,468 |
| LTM income from continuing operations | 135 + 119 - (-52) | 306 |
| LTM operating cash flow | -193 + -1,174 - 473 | -1,840 |
| LTM operating cash flow excluding Lotto payments | (-193 + 926) + (-1,174 + 1,675) - 473 = 733 + 501 - 473 | 761 |
| LTM capex | 316 + 232 - 174 | 374 |
| LTM free cash flow | -1,840 - 374; excluding Lotto: 761 - 374 | -2,214; 387 |
| LTM license-fee amortization add-back | 223 + 201 - 101 | 323 |
| Maturity table footing | 0 + 228 + 798 + 978 + 1,025 + 1,354 | 4,383, equal to printed total |
| Revolver reconciliation (inference) | 650 + 1,139 - 604 | 1,185, equal to printed availability |

## Gaps

| Gap | Severity | Effect and remedy |
| --- | --- | --- |
| Not supplied: any report after August 4, 2026, including third-quarter 2026 results | High | Balance sheet and leverage are as of June 30, 2026; obtain the latest report if filed on or before 2026-11-05 |
| Not supplied: covenant levels, step-downs and covenant EBITDA; headroom is Not calculable | High | Leverage and cover are management-basis only; obtain the revolver and term loan agreements |
| Adjusted EBITDA, net debt and leverage are deck figures, not filed statement lines | Medium | Labelled as management claims; filed statements support every other figure |
| Letters of credit under the new revolvers at June 30, 2026 are not stated | Medium | Liquidity of 1,185 is as printed; the reconciliation above suggests no deduction |
| June 30, 2026 lease liabilities and the finance lease increase are not located | Low | Lease-adjusted leverage computed only for December 31, 2025 |
| No June 30, 2025 balance sheet and no Q2 2025 or Q4 2025 interim reports in the pack | Low | LTM figures use the comparative columns of later reports; discrete Q4 2025 is not derived here |
| Pension and retiree medical obligations not located in the statement notes | Low | Treated as not supplied, not as nil |
| Guarantor list and the amended March 2026 term loan terms not supplied | Medium | Structure and distribution cap cannot be fully described |
| Ratings after December 31, 2025 not supplied | Medium | Rating-linked pricing and distribution limits cannot be assessed |
| Deck charts not inspected (text extraction only) | Low | The filed debt tables are used for all chart-like data |

## Next module

The business and transaction module (CP-1A) follows. Carry forward: the Italian Lotto license (final installment of 1,675 paid April 24, 2026, amortized over nine years from December 2025, which drives the 323 LTM add-back) is the central financing and earnings-quality item; the consortium partners fund part of it through non-controlling interest capital increases (650 in H1 2026) and took 163 of cash distributions in H1 2026 (the same amount as in FY2025 and H1 2025); the sale of the gaming business on July 1, 2025 is the perimeter change behind all continuing-operations comparatives; and the UK contract transition in August 2025 reduces service revenue. The fundamental credit synthesis should use the leverage range of 3.24x on management's definition and 4.48x without the license-fee add-back, treat covenant headroom as unknown, and keep the August 4, 2026 evidence cut-off in view. The evidence trace validator should check the deck-derived Adjusted EBITDA figures against their locators.
