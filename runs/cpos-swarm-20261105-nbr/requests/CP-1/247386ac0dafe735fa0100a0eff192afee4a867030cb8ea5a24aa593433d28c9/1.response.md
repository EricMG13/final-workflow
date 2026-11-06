## Request

- Issuer: NABORS INDUSTRIES LTD (issuer id nbr, NYSE: NBR), the Bermuda registrant; figures are the consolidated Nabors Industries Ltd. and subsidiaries statements, which consolidate the SANAD joint venture and the special purpose acquisition company Nabors Energy Transition Corp. II as variable interest entities.
- As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Latest evidence: third-quarter 2026 Form 10-Q signed November 4, 2026 and the October 27, 2026 earnings release.
- Pathway: credit_snapshot. Reporting currency per context: USD. Current period: Q3 2026 (quarter ended September 30, 2026) and its LTM; prior period: FY2025 (year ended December 31, 2025). The filings report in US dollars, in thousands; charts below are in US$m. No other currency or scale is used by the sources.
- Task for this module: the canonical financial base for the credit snapshot: statements as reported, reported covenant and liquidity facts, debt by instrument, maturity profile, calculated leverage, coverage, liquidity and cash flow metrics with their inputs, definition risks and the gaps that limit them.
- Upstream handoff used: CP-0 (source readiness), listed in Sources. Its limitations G1 to G7 are carried forward here. This handoff corrects nothing in CP-0; it adds that the 10-K exhibit-index wording for the exchangeable notes ("due 2027") is outweighed by the debt note and the quarterly debt tables ("due June 2029"), as CP-0 G7 anticipated.
- Settings file `context` is not issuer evidence. It leaves ratings, quotes, valuation inputs, deal terms, guarantors, parent and sponsor blank; those are treated as not supplied, never as zero.
- Periods are labelled throughout: Q3 2026 (three months), nine months 2026 (9M 2026), nine months 2025 (9M 2025), FY2025, LTM to Q3 2026 (calculated as FY2025 plus 9M 2026 minus 9M 2025) and point-in-time balance dates. A page locator is the source chunk shown as `page:N`, not a printed page.

## Sources

### Issuer sources relied on

| Cite as | Source name | sha256 | Use in this handoff |
| --- | --- | --- | --- |
| 10-K | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | 427cc2fc64bcd723a27a6c2478a12093e219dc045e02d41b40eab49061568751 | Audited FY2025 statements, FY2025 cash interest and taxes, debt note, joint venture note, leases, covenant definitions, exhibit index |
| 10-Q Q1 | 10-Q_2026-03-31_nbr-20260331x10q.htm.jsonl | 11eb9a5886137a3201a1d5b34cd6e8ef50e247d641cd61ec9c9814adc458e187 | March 31, 2026 debt, covenant ratio, liquidity |
| 10-Q Q2 | 10-Q_2026-06-30_nbr-20260630x10q.htm.jsonl | 6c2a6d1bdbcbd71ad95906094386639f0ffd409dc513dcadc487db645242cb3b | June 30, 2026 debt, covenant ratio, receivables sold |
| 10-Q Q3 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | 7e240e48875d03a0d84a20d6f741fc0c9988f286076c7c4d265721b0e0793ce2 | Latest unaudited statements, debt note, credit agreement, covenants, liquidity, joint venture, receivables facility, commitments |
| ER Q1 | EX-99.1_2026-04-28_tm2612942d1_ex99-1.htm.jsonl | 811d6f2d82a109aad668cd621d65877dd4784a4f2a4d17ed4d8fd9b20e6f9b37 | Q4 2025 and Q1 2026 quarterly columns, Q1 2026 balance sheet, reconciliations |
| ER Q2 | EX-99.1_2026-07-28_tm2621313d2_ex99-1.htm.jsonl | 4fe99e5d4274f6274ec08f0c05beac58f1ab8c742acabe22ed57e9e2bd36a4e7 | Q2 2026 and Q2 2025 columns, Quail Tools carve-out |
| ER Q3 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | f9d4d37c25f2acc92f4bf176ff35ad6539e2f40b8c58a320a92c16c59d447e59 | Q3 2026 quarterly columns, reconciliations, net debt, adjusted free cash flow, guidance |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 2447d4a661e92334753a8e1c6e3f04df86843d3399afe1ed1f2ac26814412213 | Run settings only; not issuer evidence |

### Upstream handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 01371c96badec91a1c024971fd80be337cc1aa2bfcd663093f556e7185d90614 | Source readiness: perimeter map, gaps G1 to G12, source relationships |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Notes at face value fell to 2,050.0 US$m, paid from cash, so net leverage is flat at 1.76x and liquidity fell to 825.1 US$m. No notes mature before 2029; reported covenant interest cover is 5.20x against 2.75x. | Medium | Cash interest for 2026 is not reported in the quarterly filings, and covenant EBITDA is undefined in the pack, so coverage rests on interest expense and the reported ratio. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Notes at face value fell from 2,529.1 US$m to 2,050.0 US$m after the 2028 notes and 100.0 US$m of the 2030 notes were redeemed with cash. | Lower coupons help cover, but cash fell from 940.7 US$m to 475.1 US$m, so net debt of 1,574.9 US$m is little changed. | High |
| LTM adjusted EBITDA is 893.6 US$m against 912.7 US$m for FY2025, but FY2025 includes the Quail Tools business sold in August 2025. | Like-for-like earnings improved; leverage is 2.29x gross and 1.76x net on a face-value basis. | Medium |
| Cash of 475.1 US$m includes 180.6 US$m held in the half-owned Saudi joint venture, and EBITDA includes all of that venture. | Parent-level liquidity and leverage are weaker than consolidated figures suggest; the share creditors can reach is not disclosed. | Medium |
| Free cash flow after net capital spending was 74.5 US$m in Q3 2026 but only 38.6 US$m for nine months, with Saudi newbuild spending ongoing. | Debt reduction beyond bond redemptions depends on spending staying below plan and receivables collecting. | Medium |
| About 41% of receivables sit in Saudi Arabia, and 168.0 US$m of receivables were sold under a facility whose term may end on April 1, 2027. | A non-renewal would absorb cash within twelve months, and Saudi concentration ties collections to one customer group. | Medium |

### Financial base view

On the filed evidence, Nabors Industries Ltd entered 2026 with 2,529.1 US$m of notes at face value and ended Q3 2026 with 2,050.0, after redeeming the 7.50% notes due January 2028 and 100.0 US$m of the 9.125% notes due January 2030 with cash on hand. Because both redemptions were paid from cash, which fell from 940.7 to 475.1 US$m, net debt on a face-value basis moved only from 1,588.4 to 1,574.9 US$m, and net leverage on LTM adjusted EBITDA moved from 1.74x to 1.76x while gross leverage fell from 2.77x to 2.29x. Liquidity, cash plus the undrawn 350.0 US$m revolver, fell from 1,290.7 to 825.1 US$m, which remains sizeable against a first maturity in June 2029 but is a smaller cushion than at December 31, 2025. The reported covenant interest coverage ratio was 5.20x at September 30, 2026 against a minimum of 2.75x, and minimum guarantor value was 99.8% against 90%. Three features limit how far these figures can be pushed: consolidated cash, debt capacity and EBITDA include the 50%-owned SANAD venture; 2026 cash interest and the covenant EBITDA definition are not in the pack; and the FY2025 comparison includes Quail Tools. All figures below are issuer-reported or calculated from reported inputs, with the formula in Calculations.

### Source context

| Source | Entity and perimeter | Period and basis | Statement kind, unit and currency |
| --- | --- | --- | --- |
| 10-K | Nabors Industries Ltd. and subsidiaries, consolidated, including consolidated VIEs | FY2025 with FY2024 and FY2023 comparatives; audited under U.S. GAAP (auditor PricewaterhouseCoopers LLP) | Annual statements, notes and segment note; US$ thousands unless stated |
| 10-Q Q1, Q2, Q3 | Same perimeter | Quarter ends March 31, June 30 and September 30, 2026; unaudited, U.S. GAAP interim; cash flow is year-to-date | Interim statements and notes; US$ thousands |
| ER Q1, Q2, Q3 | Same perimeter | Three-month columns, year-to-date columns and Q4 2025 comparative; unaudited, with issuer non-GAAP measures | Press release statements and reconciliations; US$ thousands, headline text in US$ millions |

Version relationships: the three 10-Qs and three releases are successive and distinct. Where a release and a 10-Q state the same fact, the 10-Q is the controlling filed document. FY2025 comparatives inside 2026 documents were compared at the balance sheet date (the December 31, 2025 balance sheet totals agree across the 10-K, the Q1 release and the Q3 10-Q, so no restatement of that date was found).

### Reported statements

#### Income statement, US$ thousands as reported

| Line | Q4 2025 (ER Q1 page:6) | Q1 2026 (ER Q1 page:6) | Q2 2026 (ER Q3 page:5-6) | Q3 2026 (10-Q Q3 page:3) | 9M 2026 (10-Q Q3 page:3) | 9M 2025 (10-Q Q3 page:3) | FY2025 (10-K page:82) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Operating revenues | 797,529 | 783,548 | 814,795 | 872,194 | 2,470,537 | 2,387,164 | 3,184,693 |
| Investment income | 7,600 | 2,887 | 2,131 | 4,143 | 9,161 | 20,048 | 27,648 |
| Direct costs | 486,367 | 493,469 | 507,551 | 536,577 | 1,537,597 | 1,428,009 | 1,914,376 |
| General and administrative | 76,279 | 71,760 | 71,375 | 76,733 | 219,868 | 228,308 | 304,587 |
| Research and engineering | 13,328 | 13,506 | 14,209 | 13,341 | 41,056 | 39,735 | 53,063 |
| Depreciation and amortization | 159,188 | 156,186 | 160,549 | 159,744 | 476,479 | 490,046 | 649,234 |
| Interest expense | 50,625 | 43,761 | 42,678 | 42,087 | 128,526 | 164,741 | 215,366 |
| Gain on disposition of Quail Tools (a cost-side line; a gain is negative) | 1,595 | - | - | - | - | (415,557) | (413,962) |
| Gain on bargain purchase (a gain is negative) | 2,846 | - | - | - | - | (116,499) | (113,653) |
| Other, net | (9,532) | (13,393) | 5,682 | 11,428 | 3,717 | 75,334 | 65,802 |
| Income before income taxes | 24,433 | 21,146 | 14,882 | 36,427 | 72,455 | 513,095 | 537,528 |
| Income tax expense | 7,440 | 16,884 | 16,405 | 20,443 | 53,732 | 155,655 | 163,095 |
| Net income (loss) | 16,993 | 4,262 | (1,523) | 15,984 | 18,723 | 357,440 | 374,433 |
| Net (income) attributable to noncontrolling interest | (6,645) | (19,428) | (20,807) | (27,149) | (67,384) | (81,164) | (87,809) |
| Net income (loss) attributable to Nabors | 10,348 | (15,166) | (22,330) | (11,165) | (48,661) | 276,276 | 286,624 |
| Adjusted EBITDA (issuer definition, non-GAAP) | 221,555 | 204,813 | 221,660 | 245,543 | 672,016 | 691,112 | 912,667 (calculated, see Calculations; not printed in the 10-K) |
| Adjusted operating income (issuer definition) | 62,367 | 48,627 | 61,111 | 85,799 | 195,537 | 201,066 | 263,433 (calculated) |

Sign convention: costs are positive and gains negative, as the statement prints them; net (income) attributable to noncontrolling interest is shown as the statement prints it, so a negative number reduces income to Nabors. The 9M 2025 period includes Parker from March 12, 2025 and Quail Tools until its sale on August 20, 2025 (10-Q Q3 page:8).

#### Balance sheet, US$ thousands as reported

| Line | Dec 31, 2025 (10-K page:81) | Mar 31, 2026 (ER Q1 page:6) | Jun 30, 2026 (ER Q3 page:6) | Sep 30, 2026 (10-Q Q3 page:2) |
| --- | --- | --- | --- | --- |
| Cash and short-term investments | 940,738 | 500,853 | 509,833 | 475,145 |
| Accounts receivable, net | 391,705 | 417,717 | 443,417 | 511,663 |
| Total current assets | 1,551,573 | 1,152,601 | 1,197,179 | 1,205,114 |
| Property, plant and equipment, net | 2,920,019 | 2,914,886 | 2,908,061 | 2,884,274 |
| Total assets | 4,789,657 | 4,385,636 | 4,419,945 | 4,443,317 |
| Current portion of debt, net | 377,492 | - | - | - |
| Trade accounts payable | 300,467 | 322,837 | 365,472 | 370,483 |
| Total current liabilities | 993,001 | 585,215 | 633,639 | 679,993 |
| Long-term debt, net of deferred financing costs | 2,117,187 | 2,118,729 | 2,120,276 | 2,022,758 |
| Total liabilities | 3,352,014 | 2,944,107 | 2,978,067 | 2,948,049 |
| Redeemable noncontrolling interest in subsidiary (mezzanine) | 482,446 | 489,129 | 495,886 | 502,718 |
| Shareholders' equity | 590,727 | 568,942 | 544,128 | 565,912 |
| Noncontrolling interest | 364,470 | 383,458 | 401,864 | 426,638 |
| Total equity | 955,197 | 952,400 | 945,992 | 992,550 |
| Notes at face value (debt note total) | 2,529,146 | 2,150,000 | 2,150,000 | 2,050,000 |
| Deferred financing costs | 34,467 | 31,271 | 29,724 | 27,242 |

The face-value totals come from the debt notes (10-K page:103, 10-Q Q1 page:13, 10-Q Q2 page:13, 10-Q Q3 page:15) and the deferred financing costs are the amounts those notes deduct. Cash and short-term investments at September 30, 2026 are cash and cash equivalents of 475,072 plus short-term investments of 73 (10-Q Q3 page:2). Restricted cash of 2,379 at September 30, 2026 is outside this line (10-Q Q3 page:5).

#### Cash flow, US$ thousands as reported

| Line | 9M 2026 (10-Q Q3 page:4) | 9M 2025 (10-Q Q3 page:4) | FY2025 (10-K page:83) | Q3 2026 (ER Q3 page:12) |
| --- | --- | --- | --- | --- |
| Net cash provided by operating activities | 487,474 | 447,425 | 693,266 | 238,893 |
| Capital expenditures (cash flow statement line) | (460,803) | (553,886) | (715,948) | not printed as a gross quarterly figure |
| Proceeds from sales of assets and insurance claims | 11,975 | 50,609 | 98,628 | not printed separately |
| Capital expenditures net of proceeds from sales of assets (release measure) | (448,828) | (503,277) | not printed | (164,370) |
| Issuer free cash flow / adjusted free cash flow | 38,646 | (15,036) adjusted; (55,852) before the acquisition-cost add-back | not printed for the year | 74,523 |
| Reduction in debt (financing) | (484,013) | (343,036) | (902,676) | not printed |
| Distributions to noncontrolling interest | (4,776) | (1,625) | not extracted | not printed |
| Proceeds from disposition of Quail Tools | - | 371,319 | 622,856 | - |

The 9M 2025 cash taxes and interest are not extracted here; the only cash interest and cash tax figures in the pack are those for FY2025, FY2024 and FY2023 on 10-K page:121 (see Gaps).

#### Segment adjusted EBITDA, US$ thousands as reported (issuer definition)

| Segment | Q3 2026 (ER Q3 page:6) | Q3 2025 (ER Q3 page:6) | 9M 2026 (ER Q3 page:6) | 9M 2025 (ER Q3 page:6) |
| --- | --- | --- | --- | --- |
| U.S. Drilling | 99,391 | 94,161 | 281,537 | 288,693 |
| International Drilling | 145,718 | 127,551 | 397,532 | 360,695 |
| Drilling Solutions | 43,913 | 60,666 | 122,588 | 178,020 |
| Rig Technologies | 4,987 | 3,770 | 8,672 | 14,507 |
| Other reconciling items | (48,466) | (49,840) | (138,313) | (150,803) |
| Total adjusted EBITDA | 245,543 | 236,308 | 672,016 | 691,112 |

Drilling Solutions in Q3 2025 and 9M 2025 includes Quail Tools, whose Q3 2025 adjusted EBITDA was 20,305 (ER Q3 page:12) and whose Q2 2025 adjusted EBITDA was 37,012 (ER Q2 page:12).

### Debt by instrument at September 30, 2026

| Instrument | Face value 9/30/2026 (US$ thousands) | Face value 12/31/2025 | Fair value 9/30/2026 | Maturity | Issuer per 10-K exhibit index | Annual coupon on face value (calculated) |
| --- | --- | --- | --- | --- | --- | --- |
| 1.75% senior exchangeable notes | 250,000 | 250,000 | 230,313 | June 2029 | Nabors Industries, Inc., guaranteed by Nabors Industries Ltd. | 4,375 |
| 9.125% senior priority guaranteed notes | 550,000 | 650,000 | 570,906 | January 2030 | Nabors Industries, Inc., with guarantors | 50,188 (rounded from 50,187.5) |
| 8.875% senior guaranteed notes | 550,000 | 550,000 | 556,584 | August 2031 | Nabors Industries, Inc., with guarantors | 48,813 (rounded from 48,812.5) |
| 7.625% senior priority guaranteed notes | 700,000 | 700,000 | 700,196 | November 2032 | Nabors Industries, Inc. per the exhibit index; the debt note says "Nabors" | 53,375 |
| 7.50% senior guaranteed notes | - (redeemed) | 379,146 | - | January 2028 | Nabors Industries Ltd. (2020 indenture) | - |
| Total notes | 2,050,000 | 2,529,146 | 2,057,999 | Various | Various | 156,750 |

Sources: debt and fair value tables 10-Q Q3 page:15 and page:19; December 31, 2025 column 10-K page:103; issuers 10-K page:135 and page:136. The 7.625% notes are guaranteed by Nabors and "certain of Nabors' indirect wholly-owned subsidiaries" (10-K page:104) and the exchangeable notes by Nabors Industries Ltd.; for the other series the exhibit index says only "the guarantors party thereto", and no guarantor list is in the pack. The exchangeable notes have an exchange rate of 4.7056 common shares per 1,000 US$ principal, an exchange price of approximately 212.51 US$ per share (10-K page:104); the issuer may settle in cash, shares or a combination. The Q3 2026 10-Q shows these notes at a fair value below face (230,313 against 250,000).

Bank and other facilities at September 30, 2026:

| Facility | Commitment or limit | Drawn or used | Remaining | Terms and source |
| --- | --- | --- | --- | --- |
| 2024 Credit Agreement revolver (borrower Nabors Industries, Inc.; Nabors Industries Ltd. is Holdings) | 350,000 | No borrowings | 350,000 | First lien on contiguous U.S. land drilling rigs and related equipment (10-K page:30); matures the earlier of June 17, 2029 and, if 50% or more of the exchangeable notes remain outstanding, 90 days before their maturity (10-Q Q3 page:16); 200,000 uncommitted accordion (10-Q Q3 page:15) |
| 2024 Credit Agreement letter of credit tranche | 150,000 (after the April 7, 2026 joinder added 25,000) | 68,200 of letters of credit | 81,800 (calculated) | Letters of credit do not reduce revolving capacity (10-Q Q3 page:15 and page:16) |
| Seven bilateral letter-of-credit facilities | 270,333 credit available | 133,447 letters of credit outstanding, including financial and performance guarantees | 136,886 | 10-Q Q3 page:40 and page:41; letter-of-credit capacity only, not cash |
| Receivables sales facility (A/R Purchase Agreement) | 250,000 maximum purchase commitment | 168,000 sold and not yet collected | Fluctuates with eligible receivables | Sale accounting; term to the earliest of April 1, 2027 and 90 days before the 2024 Credit Agreement maturity (10-Q Q3 page:14, page:15 and page:41) |

### Covenants and reported compliance

| Test | Level | Reported figure | Date | Source |
| --- | --- | --- | --- | --- |
| Interest coverage ratio (EBITDA / interest expense, latest four fiscal quarters) | Not less than 2.75x | 4.16x | Dec 31, 2025 | 10-K page:63 |
| Interest coverage ratio, as above | Not less than 2.75x | 4.40x | Mar 31, 2026 | 10-Q Q1 page:33 |
| Interest coverage ratio, as above | Not less than 2.75x | 4.69x | Jun 30, 2026 | 10-Q Q2 page:37 |
| Interest coverage ratio, as above | Not less than 2.75x | 5.20x | Sep 30, 2026 | 10-Q Q3 page:40 |
| Minimum guarantor value (share of consolidated property, plant and equipment owned by non-parent guarantors and their subsidiaries) | Not less than 90% | 99.8% at each of the four dates | Dec 31, 2025 to Sep 30, 2026 | same pages as the interest coverage rows |
| Collateral coverage requirement (collateral rig fair value not below a threshold; independent appraisal every six months) | Threshold as defined in the agreement, not stated in the pack | Not supplied | Not dated | 10-Q Q3 page:16 |

The headroom on the interest coverage test is 2.45 turns at September 30, 2026 (5.20 less 2.75), a simple difference of reported figures. It cannot be converted into an EBITDA cushion, because the covenant definition of EBITDA is not in the pack. Management states compliance and an expectation to remain in compliance for twelve months (10-Q Q3 page:40), which is a management statement.

### Financials and credit metrics

| Metric | FY2025 or Dec 31, 2025 | LTM to Q3 2026 or Sep 30, 2026 | Q3 2026 (quarter) | Basis, inputs and locators |
| --- | --- | --- | --- | --- |
| Operating revenues, US$m | 3,184.7 | 3,268.1 | 872.2 | FY2025 10-K page:82; LTM calculated as FY2025 plus 9M 2026 less 9M 2025; Q3 10-Q Q3 page:3 |
| Adjusted EBITDA, US$m (issuer definition) | 912.7 | 893.6 | 245.5 | FY2025 calculated (see Calculations); LTM = Q4 2025 221.6 plus 9M 2026 672.0; Q3 ER Q3 page:1 |
| Adjusted EBITDA margin | 28.7% | 27.3% | 28.2% | Calculated: adjusted EBITDA / operating revenues |
| Interest expense, US$m | 215.4 | 179.2 | 42.1 | FY2025 10-K page:82; LTM calculated; Q3 10-Q Q3 page:3 |
| Cash paid for interest, net of capitalized interest, US$m | 209.2 | Not supplied: not printed in the 10-Qs | Not supplied | 10-K page:121 for FY2025 only |
| Adjusted EBITDA / interest expense | 4.24x | 4.99x | 5.83x | Calculated; differs from the covenant ratio because covenant EBITDA is defined in the credit agreement, not in the pack |
| Reported covenant interest coverage | 4.16x | 5.20x | not applicable | 10-K page:63; 10-Q Q3 page:40; minimum 2.75x |
| Net cash from operating activities, US$m | 693.3 | 733.3 | 238.9 | FY2025 10-K page:83; LTM calculated; Q3 ER Q3 page:12 |
| Capital expenditures net of sales proceeds, US$m | 617.3 | 562.9 | 164.4 | FY2025 calculated from 10-K page:83 (715.9 less 98.6); LTM calculated; Q3 ER Q3 page:12 |
| Operating cash flow less net capital expenditures, US$m | 75.9 | 170.4 | 74.5 | Calculated; Q3 equals the issuer's adjusted free cash flow |
| Notes at face value, US$m | 2,529.1 | 2,050.0 | not applicable | 10-K page:103; 10-Q Q3 page:15 |
| Total debt per issuer net debt table (net of deferred financing costs), US$m | 2,494.7 | 2,022.8 | not applicable | ER Q3 page:11 |
| Cash and short-term investments, US$m | 940.7 | 475.1 | not applicable | ER Q3 page:11 |
| Of which held in SANAD (cash and cash equivalents), US$m | 179.9 | 180.6 | not applicable | 10-K page:112; 10-Q Q3 page:13 |
| Net debt on face value, US$m | 1,588.4 | 1,574.9 | not applicable | Calculated: notes at face value less cash and short-term investments |
| Issuer-defined net debt (carrying value), US$m | 1,553.9 | 1,547.6 | not applicable | ER Q3 page:11 |
| Total debt / adjusted EBITDA (face value) | 2.77x | 2.29x | not applicable | Calculated |
| Net debt / adjusted EBITDA (face value) | 1.74x | 1.76x | not applicable | Calculated |
| Liquidity: cash plus undrawn revolver, US$m | 1,290.7 | 825.1 | not applicable | Calculated: cash and short-term investments plus 350.0 undrawn revolver; excludes letter-of-credit capacity |
| Annual coupon on notes outstanding, US$m | 194.3 | 156.8 | not applicable | Calculated from face values and coupons; Dec 31, 2025 includes the 7.50% notes redeemed January 15, 2026 |
| Redeemable noncontrolling interest, US$m | 482.4 | 502.7 | not applicable | 10-K page:81; 10-Q Q3 page:2 |
| Receivables sold and not yet collected, US$m | 137.0 | 168.0 | not applicable | 10-Q Q3 page:15 |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 2.77 | 1.74 | x | Notes at face value at December 31, 2025 over FY2025 adjusted EBITDA (calculated, issuer definition, includes Quail Tools until August 20, 2025); net of cash and short-term investments; excludes redeemable noncontrolling interest, leases and receivables sold |
| Q1 2026 | 2.36 | 1.81 | x | Face value 2,150.0 US$m at March 31, 2026 over LTM adjusted EBITDA 911.1 US$m (calculated); net of cash and short-term investments of 500.9 US$m |
| Q2 2026 | 2.43 | 1.85 | x | Face value 2,150.0 US$m at June 30, 2026 over LTM adjusted EBITDA 884.3 US$m (calculated); net of cash and short-term investments of 509.8 US$m |
| Q3 2026 | 2.29 | 1.76 | x | Face value 2,050.0 US$m at September 30, 2026 over LTM adjusted EBITDA 893.6 US$m (calculated); net of cash and short-term investments of 475.1 US$m, of which 180.6 US$m cash is held in SANAD; EBITDA includes 100% of SANAD |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 4.36 | x | Calculated: FY2025 adjusted EBITDA 912.7 US$m over cash paid for interest, net of capitalized interest, of 209.2 US$m (10-K page:121) |
| Q1 2026 | Not supplied: cash paid for interest is not printed in the quarterly reports | x | Interest expense based cover is in the Financials and credit metrics table; reported covenant ratio 4.40x |
| Q2 2026 | Not supplied: cash paid for interest is not printed in the quarterly reports | x | Interest expense based cover is in the Financials and credit metrics table; reported covenant ratio 4.69x |
| Q3 2026 | Not supplied: cash paid for interest is not printed in the quarterly reports | x | LTM adjusted EBITDA over LTM interest expense is 4.99x (not cash interest); reported covenant ratio 5.20x |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 940.7 | 350.0 | US$m | Cash and short-term investments at December 31, 2025 (includes 179.9 held in SANAD); undrawn revolver, no borrowings and the letter-of-credit tranche is separate (10-K page:106) |
| Q1 2026 | 500.9 | 350.0 | US$m | Cash and short-term investments at March 31, 2026; no borrowings (10-Q Q1 page:32); excludes letter-of-credit capacity and receivables facility |
| Q2 2026 | 509.8 | 350.0 | US$m | Cash and short-term investments at June 30, 2026; no borrowings (10-Q Q2 page:36); excludes letter-of-credit capacity and receivables facility |
| Q3 2026 | 475.1 | 350.0 | US$m | Cash and short-term investments at September 30, 2026, of which 180.6 is SANAD cash; no borrowings (10-Q Q3 page:16); the 68.2 of letters of credit under the credit agreement use the separate tranche; revolver term at the earliest June 2029 |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0.0 | US$m | No series in the September 30, 2026 debt table matures in 2026; the 2028 notes were redeemed in January 2026; revolver undrawn |
| 2027 | 0.0 | US$m | No series in the debt table matures in 2027; the receivables facility term may end April 1, 2027 but is a sale facility, not debt |
| 2028 | 0.0 | US$m | No series in the debt table matures in 2028 after the redemption of the 7.50% notes |
| 2029 | 250.0 | US$m | 1.75% exchangeable notes due June 2029 at face value; the revolver (undrawn) matures at the earliest June 17, 2029 or 90 days before these notes if 50% or more remain outstanding |
| 2030 | 550.0 | US$m | 9.125% senior priority guaranteed notes due January 2030 at face value after the 100.0 redemption |
| 2031 | 550.0 | US$m | 8.875% senior guaranteed notes due August 2031 at face value |
| 2032 | 700.0 | US$m | 7.625% senior priority guaranteed notes due November 2032 at face value |

The year-by-year table printed in the 10-K (page:103) is as of December 31, 2025 and still shows the 7.50% notes; the schedule above is rebuilt from the September 30, 2026 instrument list, not copied from it. Face value is used, not carrying value, and no call or put schedule is in the pack.

### Definition review

- Adjusted EBITDA and adjusted operating income are issuer non-GAAP measures that exclude investment income, interest, gains on the Quail Tools sale and bargain purchase, and Other, net, and the issuer states that they exclude "certain cash expenses that the Company is obligated to make" (ER Q3 page:7). In 9M 2026 Other, net included severance and reorganization costs of 6,203 and litigation items of (14,737), a net credit (10-Q Q3 page:24). The measure includes 100% of the consolidated SANAD venture although Saudi Aramco owns half; net income attributable to noncontrolling interest was 67,384 in 9M 2026 against consolidated net income of 18,723.
- The covenant EBITDA in the 2024 Credit Agreement is a defined term not reproduced in the pack. The reported covenant ratio (5.20x) is above this handoff's adjusted EBITDA over interest expense (4.99x); the difference cannot be explained from the pack.
- Net debt: the issuer deducts cash and short-term investments from total debt after deferred financing costs. This handoff uses face value for leverage and reports the issuer measure alongside it; the gap at September 30, 2026 equals the deferred financing costs of 27,242.
- Adjusted free cash flow: operating cash flow less capital expenditures net of proceeds from sales of assets, before acquisition-related costs (ER Q3 page:12). The cash flow statement shows capital expenditures and sales proceeds on separate lines.
- Restricted cash of 2,379 at September 30, 2026 is not in cash and short-term investments (10-Q Q3 page:5).
- Secured versus unsecured: the credit agreement is secured by a first lien on contiguous U.S. land drilling rigs (10-K page:30). The pack does not state the security or ranking of any note series beyond the names "senior priority guaranteed" and "senior guaranteed" and the existence of guarantees. No secured or unsecured split of notes is made.

### Funding, off-debt claims and commitments

- Redeemable noncontrolling interest, 502,718 at September 30, 2026: Saudi Aramco's share of SANAD redeemable ownership interests, which accrue interest annually, have a twenty-five year maturity and convert to authorized capital on specified events including accumulated losses (10-Q Q3 page:13). It is mezzanine equity, outside debt, and the accrued distribution of 20,272 for 9M 2026 reduced retained earnings (10-Q Q3 page:6).
- SANAD: balance sheet at September 30, 2026 shows cash of 180,635, total assets of 1,570,831 and total liabilities of 244,920 (10-Q Q3 page:13). The 10-K states that Nabors backstops its share of SANAD's obligations to purchase the first 25 drilling rigs if the venture lacks cash or third-party financing (10-K page:114); the Q3 10-Q does not repeat that sentence in the pages searched.
- Receivables sale: 168,000 sold and uncollected at September 30, 2026, against 138,000 at June 30, 2026 and 137,000 at December 31, 2025 (10-Q Q3 page:15; 10-Q Q2 page:13); outside reported debt under sale accounting; the originators, Nabors Industries, Inc., the special purpose entity and the Company give representations, covenants and an indemnification guarantee (10-Q Q3 page:41).
- Purchase commitments of about 296.4 US$m at September 30, 2026 (10-Q Q3 page:42). Financial standby letters of credit and surety instruments of 33,795 maximum (10-Q Q3 page:44).
- Leases: operating lease liabilities of 40,213 at December 31, 2025 (10-K page:127); the September 30, 2026 balance sheet shows current lease liabilities of 10,206 (10-Q Q3 page:2). No finance leases and no pension funded status were located.
- Related parties: revenues from related parties including Saudi Aramco were about 1.1 billion US$ in FY2025 (10-K page:114), and related party receivables were 211.5 US$m at September 30, 2026 against 121.0 at December 31, 2025 (10-Q Q3 page:3).
- Receivables concentration at September 30, 2026: about 41% Saudi Arabia, 13% U.S. and 9% Mexico, with a Mexican customer that has a history of late payment (10-Q Q3 page:41).

### Latest quarter and events after the quarter end

- Q3 2026 financing: 100.0 US$m of the 9.125% notes redeemed with cash (10-Q Q3 page:15; ER Q3 page:3); loss on debt buybacks of 5,525 in Q3 2026 (10-Q Q3 page:24). April 7, 2026: the letter of credit tranche was increased by 25.0 US$m (10-Q Q3 page:16). On August 26, 2026, Nabors issued about 0.4 million shares for about 5.4 million Series B-1 preferred shares of Quaise Energy, a noncash exchange valued by reference to 35.0 US$m (10-Q Q3 page:17).
- After September 30, 2026 and up to the cutoff: the October 27, 2026 release states that SANAD has suspended five rigs and gives fourth-quarter guidance (ER Q3 page:2 and page:3-4); management expects full-year 2026 adjusted EBITDA of about 930 US$m, adjusted free cash flow of 100 to 110 US$m and capital spending of 710 to 720 US$m, including 295 to 305 for SANAD newbuilds. These are management statements; the filed 10-Q does not give the rig suspension count. No debt issuance, redemption or amendment dated after September 30, 2026 appears in the pack.
- The Q3 10-Q also notes that, in the Middle East, certain operators have placed rigs on standby and issued additional suspension notices (10-Q Q3 page:33).

### Narrative findings

**Leverage.** Evidence: notes at face value fell from 2,529.1 to 2,050.0 US$m while LTM adjusted EBITDA is 893.6 US$m (Financials and credit metrics). Risk mechanism: the reduction was paid from cash, not from free cash flow, because operating cash flow less net capital expenditures was only 38.6 US$m in 9M 2026; net debt on face value is little changed, so the improvement in gross leverage does not add equal protection for creditors. Credit implication: gross leverage of 2.29x overstates the deleveraging; net leverage of 1.76x is the better reference and is flat to FY2025. Because FY2025 EBITDA includes at least 57.3 US$m from Quail Tools (Q2 2025 37.0 plus Q3 2025 20.3, calculated; Q1 2025 stub not supplied) which was sold in August 2025, the LTM figure is the cleaner earnings base.

**Coverage.** Evidence: interest expense fell from 215.4 to an LTM 179.2 US$m, and annual coupons on notes outstanding are 156.8 US$m against 194.3 US$m on the December 31, 2025 mix. Risk mechanism: coupons on the remaining notes are fixed, so interest expense should fall further toward the coupon run rate, while 2026 cash interest is not reported and the Q3 release says higher cash interest payments partly offset the sequential improvement in free cash flow (F15). Credit implication: cover on interest expense of 4.99x LTM is adequate and improving, and the reported covenant ratio of 5.20x is well above 2.75x, but the covenant definition cannot be tested from the pack.

**Cash flow quality.** Evidence: operating cash flow of 487.5 US$m in 9M 2026 against 448.8 US$m of net capital expenditures; working capital used 48.3 US$m (10-Q Q3 page:43); receivables rose to 511.7 US$m from 391.7 US$m, including related party receivables up to 211.5 US$m, a group that the 10-K says includes the joint venture partner Saudi Aramco (10-K page:114). Risk mechanism: growth in related party receivables and the Mexican late-payment history tie cash conversion to few counterparties, and the rise in receivables sold from 137.0 to 168.0 US$m, a calculated 31.0 US$m, supported operating cash flow in the nine months because sale proceeds are classified as operating (10-Q Q3 page:14). Credit implication: Q3 free cash flow of 74.5 US$m benefited from lower SANAD capital spending as milestones shifted to later periods (ER Q3 page:2 and page:3), so the full-year guidance of 100 to 110 US$m depends on Q4 delivery of 60 to 70 US$m.

**Liquidity.** Evidence: cash and short-term investments of 475.1 US$m and an undrawn 350.0 US$m revolver give 825.1 US$m, down from 1,290.7 US$m. Risk mechanism: 180.6 US$m of the cash sits in SANAD, whose assets can be used to settle the venture's own obligations or be made available to its owners through dividends, distributions or an exchange of redeemable interests upon mutual agreement of the owners (10-Q Q3 page:13), and the receivables facility term may end on April 1, 2027 at the earliest. Credit implication: liquidity outside SANAD is lower than the headline; with no maturity before June 2029 and no borrowings, the near-term refinancing risk is low, but the cushion for a receivables facility non-renewal or an extended Saudi slowdown is thinner than at FY2025.

**Data quality and definition risk.** Evidence: see Definition review. Risk mechanism: issuer-defined EBITDA excludes cash items and includes all of SANAD; the covenant EBITDA is undefined here. Credit implication: use LTM adjusted EBITDA as an issuer-defined base, not as a covenant-equivalent figure.

### Evidence register

| Ref | Source | Locator | Quote |
| --- | --- | --- | --- |
| F1 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:16 | The Company is required to maintain an interest coverage ratio (EBITDA/interest expense) of 2.75:1.00 |
| F2 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:40 | which were 5.20:1.00 and 99.8%, respectively, as of September 30, 2026 |
| F3 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:30 | The interest coverage ratio is defined to mean the ratio of (i) EBITDA for the latest four fiscal quarters |
| F4 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:15 | We also redeemed $100.0 million of the 9.125% senior priority guaranteed notes due January 2030 |
| F5 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:103 | A redemption notice for our 7.50% senior guaranteed notes due January 2028 was issued December 24, 2025 and such notes were redeemed on January 15, 2026. |
| F6 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:4 | Net debt is calculated as total debt minus the sum of cash, cash equivalents and short-term investments. |
| F7 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:7 | In addition, adjusted EBITDA excludes certain cash expenses that the Company is obligated to make. |
| F8 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:15 | approximately $168.0 million and $137.0 million had been sold to and as yet uncollected by the Purchasers |
| F9 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:14 | extended the term of the A/R Purchase Agreement to the earliest of (i) April 1, 2027 |
| F10 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:114 | the agreement requires us to backstop our share of the joint venture’s obligations to purchase the first 25 drilling rigs |
| F11 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:13 | The condensed balance sheet of SANAD, as included in our condensed consolidated balance sheet, is presented below. |
| F12 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:41 | Our largest customer in Mexico has a history of making late payments |
| F13 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:114 | Revenues from business transactions with these related parties totaled $1.1 billion, $0.9 billion and $0.8 billion |
| F14 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:104 | equivalent to an exchange price of approximately $212.51 per common share |
| F15 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:2 | partially offset by higher cash interest payments |
| F16 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:3 | We anticipate delivering full-year 2026 adjusted EBITDA of approximately $930 million |
| F17 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:2 | despite a lower SANAD rig count following the suspension of five rigs |
| F18 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:121 | Cash paid for interest, net of capitalized interest |
| F19 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:44 | The following table summarizes the total maximum amount of financial guarantees issued by Nabors: |
| F20 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:15 | Letters of credit issued do not affect revolving loan capacity and vice versa. |

## Calculations

All inputs are US$ thousands as reported unless stated; results are rounded for the tables. Sign convention: gains reduce the cost-side lines.

### Adjusted EBITDA bases

| Item | Formula and inputs | Result |
| --- | --- | --- |
| FY2025 adjusted operating income | Income before income taxes 537,528 + interest expense 215,366 - investment income 27,648 - gain on Quail Tools 413,962 - gain on bargain purchase 113,653 + Other, net 65,802 (10-K page:82, with the issuer's stated definition in ER Q3 page:11) | 263,433 |
| FY2025 adjusted EBITDA | 263,433 + depreciation and amortization 649,234 | 912,667 |
| Check on FY2025 adjusted EBITDA | 9M 2025 adjusted EBITDA 691,112 (ER Q3 page:6) + Q4 2025 adjusted EBITDA 221,555 (ER Q1 page:6) | 912,667, equal |
| LTM adjusted EBITDA to Q3 2026 | Q4 2025 221,555 + 9M 2026 672,016; equivalently FY2025 912,667 + 672,016 - 691,112 | 893,571 |
| LTM adjusted EBITDA to Q2 2026 | FY2025 912,667 + 6M 2026 426,473 - 6M 2025 454,804 (ER Q2 page:6) | 884,336 |
| LTM adjusted EBITDA to Q1 2026 | FY2025 912,667 + Q1 2026 204,813 - Q1 2025 206,345 (ER Q1 page:6) | 911,135 |
| Quail Tools contribution inside FY2025 adjusted EBITDA (at least) | Q2 2025 37,012 + Q3 2025 20,305; the Q1 2025 stub after March 11, 2025 is not supplied | at least 57,317 |
| LTM operating revenues | 3,184,693 + 2,470,537 - 2,387,164 | 3,268,066 |
| LTM interest expense | 215,366 + 128,526 - 164,741 (equal to Q4 2025 50,625 + 9M 2026 128,526) | 179,151 |
| Quarter tie-out 9M 2026 adjusted EBITDA | 204,813 + 221,660 + 245,543 | 672,016, equal to reported |

### Leverage

| Period | Debt at face value | Cash and short-term investments | Net debt at face value | EBITDA used | Total debt / EBITDA | Net debt / EBITDA |
| --- | --- | --- | --- | --- | --- | --- |
| FY2025 | 2,529,146 | 940,738 | 1,588,408 | 912,667 | 2,529,146 / 912,667 = 2.77x | 1,588,408 / 912,667 = 1.74x |
| Q1 2026 | 2,150,000 | 500,853 | 1,649,147 | 911,135 | 2.36x | 1.81x |
| Q2 2026 | 2,150,000 | 509,833 | 1,640,167 | 884,336 | 2.43x | 1.85x |
| Q3 2026 | 2,050,000 | 475,145 | 1,574,855 | 893,571 | 2,050,000 / 893,571 = 2.29x | 1,574,855 / 893,571 = 1.76x |

Carrying-value cross-check, using the issuer's own net debt table: total debt 2,022,758 / 893,571 = 2.26x and net debt 1,547,613 / 893,571 = 1.73x at September 30, 2026; 2,494,679 / 912,667 = 2.73x and 1,553,941 / 912,667 = 1.70x at December 31, 2025. Sensitivities, not headline figures: adding receivables sold of 168,000 to face-value debt gives (2,050,000 + 168,000) / 893,571 = 2.48x; excluding SANAD cash of 180,635 from cash gives net debt of 2,050,000 - (475,145 - 180,635) = 1,755,490, or 1.96x on the same EBITDA, which still includes 100% of SANAD and so is an overstatement of leverage on a proportionate view and an understatement on a ring-fenced view.

### Coverage

| Item | Formula | Result |
| --- | --- | --- |
| FY2025 EBITDA / cash interest | 912,667 / 209,167 | 4.36x |
| FY2025 EBITDA / interest expense | 912,667 / 215,366 | 4.24x |
| LTM EBITDA / interest expense | 893,571 / 179,151 | 4.99x |
| Q3 2026 EBITDA / interest expense | 245,543 / 42,087 | 5.83x |
| Coupon on notes at September 30, 2026 | 250,000 x 1.75% + 550,000 x 9.125% + 550,000 x 8.875% + 700,000 x 7.625% = 4,375 + 50,187.5 + 48,812.5 + 53,375 | 156,750 |
| Coupon on notes at December 31, 2025 | 379,146 x 7.50% + 250,000 x 1.75% + 650,000 x 9.125% + 550,000 x 8.875% + 700,000 x 7.625% = 28,436 + 4,375 + 59,312.5 + 48,812.5 + 53,375 | 194,311 |
| LTM EBITDA / coupon on notes outstanding | 893,571 / 156,750 | 5.70x |
| Covenant headroom, ratio points | 5.20 - 2.75 | 2.45 |

The 7.50% notes coupon uses 7.50% as printed in the instrument name; the pack does not give its payment dates. These coupon figures are annual run rates before the revolver, letter-of-credit fees, discount amortization and any capitalized interest.

### Liquidity

| Period | Formula | Result (US$ thousands) |
| --- | --- | --- |
| Dec 31, 2025 | 940,738 + 350,000 undrawn revolver | 1,290,738 |
| Mar 31, 2026 | 500,853 + 350,000 | 850,853 |
| Jun 30, 2026 | 509,833 + 350,000 | 859,833 |
| Sep 30, 2026 | 475,145 + 350,000 | 825,145 |
| Cash outside SANAD, Sep 30, 2026 | cash and cash equivalents 475,072 - SANAD cash 180,635 | 294,437 |
| Cash outside SANAD, Dec 31, 2025 | 940,707 - 179,907 | 760,800 |
| Letter-of-credit tranche remaining | 150,000 - 68,200 | 81,800 |
| Bilateral letter-of-credit facilities remaining | 270,333 - 133,447 | 136,886, equal to the printed remaining availability |

Letters of credit under the credit agreement are drawn against the separate tranche and do not reduce the revolver (10-Q Q3 page:15), so the revolver is shown undrawn at 350,000. It is not known from the pack whether the 133,447 of letters of credit under the seven bilateral facilities overlaps with the 68,200 under the credit agreement; the two are not added here. The revolver and letter-of-credit facilities run to June 2029 at the earliest, so none expires within twelve months; the receivables facility may end April 1, 2027, which is within twelve months of the cutoff.

### Cash flow

| Item | Formula | Result |
| --- | --- | --- |
| LTM operating cash flow | 693,266 + 487,474 - 447,425 | 733,315 |
| FY2025 net capital expenditures | 715,948 - 98,628 | 617,320 |
| 9M 2026 net capital expenditures | 460,803 - 11,975 | 448,828, equal to the release |
| 9M 2025 net capital expenditures | 553,886 - 50,609 | 503,277, equal to the release |
| LTM net capital expenditures | 617,320 + 448,828 - 503,277 | 562,871 |
| FY2025 operating cash flow less net capital expenditures | 693,266 - 617,320 | 75,946 |
| LTM operating cash flow less net capital expenditures | 733,315 - 562,871 | 170,444 |
| 9M 2026 operating cash flow less net capital expenditures | 487,474 - 448,828 | 38,646, equal to the release |
| Q3 2026 | 238,893 - 164,370 | 74,523, equal to the release |
| Quarter tie-out 9M 2026 operating cash flow | 113,339 + 135,242 + 238,893 | 487,474, equal to reported |
| Implied Q4 2026 adjusted EBITDA from guidance | about 930,000 (management) - 672,016 | about 257,984, a derived figure from an approximate guide |
| Indicative 9M 2026 cash interest, analyst inference | interest expense 128,526 - amortization of debt discount and deferred financing costs 5,292 (10-Q Q3 page:4) + decrease in interest payable (62,898 at Dec 31, 2025 less 34,760 at Sep 30, 2026, 10-Q Q3 page:23) 28,138 | about 151,372 |

The indicative cash interest figure is not a reported number: it ignores capitalized interest, accrued interest paid on redemptions, and any other timing, and it is not used in any chart or ratio. FY2025 free cash flow after net capital expenditures is before the Parker acquisition cost add-back that the issuer makes in its adjusted measure.

### Other ratios

| Item | Formula | Result |
| --- | --- | --- |
| FY2025 adjusted EBITDA margin | 912,667 / 3,184,693 | 28.7% |
| LTM adjusted EBITDA margin | 893,571 / 3,268,066 | 27.3% |
| Q3 2026 adjusted EBITDA margin | 245,543 / 872,194 | 28.2% |
| Related party share of FY2025 revenue (rounded input) | 1.1 billion / 3.184693 billion | about 34.5%, from a rounded numerator |
| Fair value as a share of face, notes at September 30, 2026 | 2,057,999 / 2,050,000 | 100.4% |
| Q3 2026 adjusted EBITDA growth against Q3 2025 excluding Quail Tools | (245,543 - (236,308 - 20,305)) / (236,308 - 20,305) = 29,540 / 216,003 | 13.7% |

## Gaps

| ID | Gap | Why it matters | Action |
| --- | --- | --- | --- |
| H1 | Not supplied: cash paid for interest and cash taxes for 2026 periods; the 10-Qs do not print them | Cash interest cover cannot be shown for Q1 to Q3 2026 or LTM; the indicative figure is an inference | Use FY2025 cash interest; ask for the supplemental cash flow data if cash cover is needed |
| H2 | Not supplied: the covenant definition of EBITDA and interest expense, the collateral coverage threshold and appraisal result | Headroom in EBITDA terms and collateral cushion cannot be computed | Add the 2024 Credit Agreement |
| H3 | Not supplied: guarantor lists, security and ranking of each note series, and call or put schedules | Structural subordination and recovery work cannot rely on filings alone | Add the indentures listed in the 10-K exhibit index |
| H4 | The year-by-year maturity table in the 10-K is as of December 31, 2025; a schedule for September 30, 2026 was rebuilt from the instrument list | Face-value schedule only; no amortization or call dates | Treat as the working schedule |
| H5 | SANAD: no income statement, EBITDA or debt capacity of the venture; cash availability to the parent is by distribution or exchange of redeemable interests only | Proportionate leverage and parent-only liquidity cannot be calculated | Request venture-level financial data; run a case that excludes the 180.6 US$m |
| H6 | The backstop of SANAD rig purchases appears in the 10-K but was not found in the Q3 10-Q | Contingent funding exposure after the first 25 rigs is unquantified | Confirm in a later filing |
| H7 | Management statements in the October release (rig suspensions, guidance, run rate) are not repeated in a filing | Not filed evidence; guidance cannot be reconciled by the issuer | Carry as management language |
| H8 | The 10-K does not print consolidated adjusted EBITDA; FY2025 is calculated and checked two ways | Small risk of definitional difference | Both methods agree at 912,667 |
| H9 | Receivables facility: availability, concentration limits and the effect on operating cash flow are not quantified | Non-renewal after April 1, 2027 would absorb cash | Monitor the term and the amount sold |
| H10 | No ratings, quotes, market capitalization or peer data in the pack | Market-based leverage and relative value are outside this base | Not supplied in context |
| H11 | Pension funded status and finance leases were not located; operating lease liability only as of December 31, 2025 | Small, but leases and pensions are outside the debt figure | Confirm in the 10-K notes if needed |
| H12 | Exhibit-index wording "due 2027" for the exchangeable notes conflicts with the debt note "due June 2029" | Maturity label only | The debt note and the quarterly tables control |

## Next module

Next is CP-1A (business and transaction context), which should use this handoff for the Parker acquisition and Quail Tools sale dates, the SANAD joint venture mechanics and the Saudi concentration, and carry H3, H5, H6 and H7. CP-2 should take the leverage, coverage, liquidity and cash flow figures above as calculated on the stated bases (face-value debt, issuer-defined LTM adjusted EBITDA) and state that 2026 cash interest and the covenant EBITDA definition are not available. CP-5 should treat the 10-Q as controlling over the release, check the three basis differences (face versus carrying debt, gross versus net capital expenditures, issuer versus covenant EBITDA) as definitional rather than errors, and verify the calculated figures against the inputs listed in Calculations.
