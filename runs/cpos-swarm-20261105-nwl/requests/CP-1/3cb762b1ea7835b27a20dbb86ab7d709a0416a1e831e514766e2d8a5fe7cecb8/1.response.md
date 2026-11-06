## Request

NEWELL BRANDS INC. (issuer id nwl, ticker NWL; the consolidated registrant, Newell Brands Inc. and subsidiaries), as of 2026-11-05, pathway credit_snapshot, public case. Module scope: the financial base for the credit snapshot, in USD millions as printed by the sources. Current period Q3 2026 (quarter ended 2026-09-30); prior period FY2025 (year ended 2025-12-31). Evidence cutoff 2026-11-05; nothing dated later is used.

Perimeter: the issuer is the parent registrant that files one consolidated set of statements; no subsidiary-level or guarantor-level statements are in the pack, so all debt, earnings, leverage and coverage here are consolidated. Period labels used: FY2025, Q1 2026, Q2 2026 and Q3 2026 (discrete quarters), 9M 2026 and 9M 2025 (nine months), and LTM Q3 2026 (twelve months to 2026-09-30, derived as FY2025 plus 9M 2026 less 9M 2025 unless the source prints it). The upstream readiness handoff is carried forward in `## Gaps`.

## Sources

### Issuer sources relied on (pinned name and sha256 of the retained text)

| Source name | sha256 | Use in this module |
| --- | --- | --- |
| 10-K_2025-12-31_nwl-20251231.htm.jsonl | dcc793cfdb2b8cc449076ad729ebed59fbf0fa17a270e35dd5b40e5638fe6453 | Audited FY2025 statements, debt note, maturity ladder, cash paid for interest and taxes, segment note |
| 10-Q_2026-03-31_nwl-20260331.htm.jsonl | e491b436993330fb987ef524b9f78ce96b1802f1285b9af80a913a9adee3f88d | Q1 2026 statements, debt table, Credit Revolver availability |
| 10-Q_2026-06-30_nwl-20260630.htm.jsonl | b3b449c8e355a64543631b4a3e69f0acef91c01cc896e4386758050640b5804b | Q2 2026 and six-month statements, debt table, Credit Revolver availability |
| 10-Q_2026-09-30_nwl-20260930.htm.jsonl | 8b58e3ae589a883e4dd1d132d51cbe5455a5976aebd62f8367be4b91ce06fe29 | Latest filed period: statements, facility-level debt, ABL terms, factoring, subsequent event |
| EX-99.1_2026-05-01_exhibit991_q1xmarchx2026.htm.jsonl | 944b1e0aff94a38b463c337c910588c7aa29def150477cd6c4593c7400267ccd | Management Q1 2026 net debt and trailing-twelve-month normalized EBITDA |
| EX-99.1_2026-07-31_exhibit991_q2xjunex2026.htm.jsonl | 5357537cee17090bbc993249463e8c84756e595916b24485d6cd92a469d185c7 | Management Q2 2026 net debt, trailing-twelve-month normalized EBITDA, tariff recoveries |
| EX-99.1_2026-10-30_exhibit991_q3xseptemberx20.htm.jsonl | f28d7c981e9628280882affba403a5eab9c05f0b6a106f3147b334e29e9ba0d3 | Management Q3 2026 net debt, trailing-twelve-month normalized EBITDA, outlook |

### Run context (not issuer evidence)

| Source name | sha256 | Use |
| --- | --- | --- |
| context (814453-newell-brands-inc-nwl.json) | 6bed67ca32030e1461ea08189ab22687642083ba91fdd1b6bdf65186613803b0 | Dated settings only: as-of 2026-11-05, USD, current period q3-2026, prior period fy-2025. Ratings, quotes and deal terms are blank; blank is not zero. |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 76b36ebebc3da26e35258cfc1d5238c4f31ac02f26874a5c908da1046b4e7b0c | Readiness handoff: all four consumers READY_WITH_LIMITATIONS. Its limits are carried here: covenant levels, interim cash interest and tax, a current maturity ladder and executed agreements are not supplied; non-GAAP figures are management claims; the annual debt ladder is stale after the third-quarter refinancing. Nothing in it is corrected by this module. |

A page is the retained text chunk shown as `page:N`, not a printed page. Management figures from the EX-99.1 releases are attributed claims; where they differ in kind from filed statements the filed statement controls.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Net debt to management's normalized EBITDA improved to 4.46x at Q3 2026 from 5.07x at FY2025, all through higher EBITDA. Cash conversion and interest cover stay thin, and the GAAP result is a loss. | Medium | EBITDA is a management measure that includes tariff recoveries; interim cash interest and covenant headroom are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Net debt was higher at Q3 2026 than at FY2025, so the lower leverage ratio comes from earnings, not repayment. | Deleveraging depends on sustaining earnings, which include one-off tariff recoveries in Q2 2026. | Medium |
| Operating cash flow less capital expenditure was small over the last twelve months against dividends paid. | Little internally generated cash is left after dividends to repay debt. | Medium |
| The nearest large maturity is the senior notes due 2028; the notes due 2027 were redeemed in the third quarter. | The 2028 notes are the next refinancing test, and the new asset-based facility may mature earlier if they remain outstanding. | Medium |
| Liquidity at Q3 2026 is cash plus net availability under a borrowing-base facility. | Availability moves with receivables and inventory and is lower than the facility size. | High |
| Receivables factoring sits outside reported debt and is being reduced. | Debt-like funding is larger than the debt table shows. | Medium |

### Financial base view

NEWELL BRANDS INC. entered the third quarter of 2026 with higher earnings but unchanged leverage in dollar terms. Net debt, as management defines it, was 4,592 at 2026-09-30 against 4,470 at 2025-12-31, so the improvement in net debt to normalized EBITDA from 5.07x to 4.46x came entirely from trailing-twelve-month normalized EBITDA rising from 882 to 1,030, not from paying debt down. That EBITDA is a management measure that adds back impairments, restructuring and share-based compensation, and it includes pre-tax tariff recoveries recorded in Q2 2026; on GAAP the issuer lost 323 over the twelve months to Q3 2026 after non-cash impairments, and Q3 2026 itself was a net loss of 81 after a 101 tradename impairment. Cash generation is thin: operating cash flow less capital expenditure was 53 over the twelve months to Q3 2026 while cash dividends paid were 127, and FY2025 interest paid in cash of 354 covered by normalized EBITDA only 2.49x. The refinancing in the third quarter replaced the 2027 note maturity and the secured revolver with a 2031 note and a new borrowing-base facility, which removes the near-term wall but leaves the 2028 notes (1,252 on the 2025-12-31 ladder) as the next large maturity, and the new facility can mature ahead of 2031 if material debt is still outstanding 91 days before its maturity. Liquidity at 2026-09-30 is cash of 249 plus net ABL availability of about 480, before factoring, which the issuer says it intends to reduce. The base is usable for a credit snapshot with the limits listed in `## Gaps`.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 5.30 | 5.07 | x | Gross debt 4,673 and net debt 4,470 over management Normalized EBITDA 882 (twelve months to 2025-12-31); debt at carrying value, cash excludes restricted cash; calculated, EBITDA is a management non-GAAP claim. |
| Q1 2026 | 5.64 | 5.41 | x | Gross debt 4,965 and net debt 4,764 over trailing-twelve-month Normalized EBITDA 881 to 2026-03-31; calculated, management claim. |
| Q2 2026 | 4.97 | 4.76 | x | Gross debt 5,006 and net debt 4,797 over trailing-twelve-month Normalized EBITDA 1,007 to 2026-06-30; EBITDA includes tariff recoveries recorded in Q2 2026; calculated, management claim. |
| Q3 2026 | 4.70 | 4.46 | x | Gross debt 4,841 and net debt 4,592 over trailing-twelve-month Normalized EBITDA 1,030 to 2026-09-30; includes the same Q2 2026 tariff recoveries; on a filing-based EBITDA before impairment the ratios are 5.81x and 5.51x (see Calculations); calculated, management claim. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 2.49 | x | Management Normalized EBITDA 882 over cash paid for interest 354 (10-K cash flow supplemental line); calculated; on net interest expense of 321 the ratio is 2.75x. |
| Q1 2026 | Not supplied: cash paid for interest is not printed in the 10-Q or release | x | Net interest expense for the trailing twelve months to 2026-03-31 is 333 in the release, which would give 2.65x on 881, but that is an expense basis and not the requested cash basis. |
| Q2 2026 | Not supplied: cash paid for interest is not printed in the 10-Q or release | x | Net interest expense for the trailing twelve months to 2026-06-30 is 338, which would give 2.98x on 1,007, an expense basis only. |
| Q3 2026 | Not supplied: cash paid for interest is not printed in the 10-Q or release | x | Net interest expense for the trailing twelve months to 2026-09-30 is 341, which would give 3.02x on 1,030, an expense basis only; cash interest may differ from expense. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 203 | 685 | US$m | Cash and cash equivalents at 2025-12-31 excluding restricted cash of 17; net availability under the 1,000 Credit Revolver as printed: 852 availability less 130 drawn less 37 standby letters of credit; limited by pledged collateral value, not the full commitment. |
| Q1 2026 | 201 | 327 | US$m | Cash at 2026-03-31; Credit Revolver net availability as printed: 789 availability less 425 drawn less 37 letters of credit; collateral-limited. |
| Q2 2026 | 209 | 451 | US$m | Cash at 2026-06-30; Credit Revolver net availability as printed: 969 availability less 470 drawn less 48 letters of credit; collateral-limited; the facility was replaced on 2026-07-30. |
| Q3 2026 | 249 | 480 | US$m | Cash at 2026-09-30, of which about 174 is held by non-US subsidiaries; ABL net availability as printed: 741 borrowing-base availability less 215 drawn less 46 letters of credit, under an 800 commitment; borrowing-base limited; not a committed amount; receivables factoring is not counted as liquidity. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 remaining | 0 | US$m | Derived roll-forward at 2026-09-30: no short-term debt or current portion is shown on the balance sheet; the 2025-12-31 ladder showed 130 for 2026 (the revolver, repaid). |
| 2027 | 0 | US$m | Derived: the 500 of notes due 2027 on the 2025-12-31 ladder were redeemed in August 2026; the small other debt of 2 is not dated and sits in the 2028 bucket as the 10-K ladder shows. |
| 2028 | 1,252 | US$m | As printed on the 2025-12-31 ladder (8.500% notes of 1,250 plus other debt); the date within 2028 is not printed in the pages read. |
| 2029 | 500 | US$m | As printed on the 2025-12-31 ladder; carrying value at 2026-09-30 is 475 because of fair value hedge accounting. |
| 2030 | 750 | US$m | As printed on the 2025-12-31 ladder. |
| 2031 | 815 | US$m | Derived: new 6.250% notes of 600 (principal) plus 215 drawn on the ABL, whose stated maturity is 2031-07-30 but can spring earlier (see Gaps). |
| 2032 and later | 1,586 | US$m | As printed under Thereafter on the 2025-12-31 ladder (notes due 2032, 2036 and 2046); the split between those years is not printed in the pages read. |

### Financials and credit metrics

| Metric (USD m unless stated) | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | 9M 2026 | 9M 2025 | LTM Q3 2026 | Basis and source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales | 7,204 | 1,549 | 1,994 | 1,873 | 5,416 | 5,307 | 7,313 | Reported; LTM calculated |
| Gross profit | 2,432 | 513 | 812 | 649 | 1,974 | 1,804 | 2,602 | Reported; LTM calculated |
| SG&A | 1,985 | 472 | 519 | 508 | 1,499 | 1,471 | 2,013 | Reported; LTM calculated |
| Restructuring costs, net | 62 | 7 | 10 | 13 | 30 | 22 | 70 | Reported; LTM calculated |
| Impairment of goodwill, intangibles and other assets | 346 | none printed | none printed | 101 | 101 | none printed | 447 | Reported; no impairment line is printed in the Q1 or Q2 statements |
| Operating income | 39 | 34 | 283 | 27 | 344 | 311 | 72 | Reported; LTM calculated |
| Interest expense, net | 321 | 84 | 87 | 86 | 257 | 237 | 341 | Reported; LTM matches release |
| Net income (loss) | (285) | (33) | 106 | (81) | (8) | 30 | (323) | Reported; LTM matches release |
| Depreciation and amortization | 311 | 79 | 78 | 77 | 234 | 231 | 314 | Cash flow statement; Q2 calculated as six months less Q1 |
| Normalized EBITDA (management) | 882 | 135 | 406 | 248 | 789 | 641 | 1,030 | Management non-GAAP, release reconciliation |
| Operating cash flow | 264 | (233) | 29 | 297 | 93 | 103 | 254 | Cash flow statements; Q2 and Q3 calculated from cumulative amounts |
| Capital expenditures | 247 | 37 | 47 | 47 | 131 | 177 | 201 | Cash flow statements; Q2 calculated |
| Operating cash flow less capital expenditures | 17 | (270) | (18) | 250 | (38) | (74) | 53 | Calculated |
| Cash dividends paid | 120 | 36 | 30 | 31 | 97 | 90 | 127 | Cash flow statements; Q2 and Q3 calculated |
| Cash paid for interest | 354 | Not supplied | Not supplied | Not supplied | Not supplied | Not supplied | Not supplied | 10-K supplemental line only |
| Cash paid for income taxes, net of refunds | 137 | Not supplied | Not supplied | Not supplied | Not supplied | Not supplied | Not supplied | 10-K supplemental line only |
| Cash and cash equivalents (period end) | 203 | 201 | 209 | 249 | 249 | 229 | 249 | Balance sheet; 9M 2025 from release |
| Gross debt (carrying value) | 4,673 | 4,965 | 5,006 | 4,841 | 4,841 | 4,777 | 4,841 | Balance sheet / release net debt table |
| Net debt (management definition) | 4,470 | 4,764 | 4,797 | 4,592 | 4,592 | 4,548 | 4,592 | Release net debt table |
| Total stockholders' equity | 2,391 | 2,342 | 2,451 | 2,364 | 2,364 | 2,697 | 2,364 | Balance sheet / equity statement |
| Gross debt / Normalized EBITDA (x, trailing twelve months at period end) | 5.30 | 5.64 | 4.97 | 4.70 | n/a | n/a | 4.70 | Calculated |
| Net debt / Normalized EBITDA (x, trailing twelve months at period end) | 5.07 | 5.41 | 4.76 | 4.46 | n/a | n/a | 4.46 | Calculated |
| Normalized EBITDA / net interest expense (x) | 2.75 | n/a | n/a | n/a | n/a | n/a | 3.02 | Calculated; expense basis |
| Normalized EBITDA / cash interest paid (x) | 2.49 | Not supplied | Not supplied | Not supplied | Not supplied | Not supplied | Not supplied | Calculated; FY2025 only |
| EBITDA before impairment, filing basis (operating income plus D&A plus impairment) | 696 | n/a | n/a | n/a | n/a | n/a | 833 | Calculated from filed lines; no add-backs other than impairment |
| Net debt / filing-basis EBITDA before impairment (x) | 6.42 | n/a | n/a | n/a | n/a | n/a | 5.51 | Calculated |

### Segment base

| Segment (USD m) | FY2025 net sales | FY2025 segment operating income | Q3 2026 net sales | Q3 2026 segment operating income | 9M 2026 net sales | 9M 2026 segment operating income |
| --- | --- | --- | --- | --- | --- | --- |
| Home and Commercial Solutions | 3,772 | (138) | 1,012 | (37) | 2,695 | 9 |
| Learning and Development | 2,691 | 464 | 692 | 137 | 2,137 | 553 |
| Outdoor and Recreation | 741 | (25) | 169 | (14) | 584 | (17) |
| Corporate expenses | n/a | (262) | n/a | (59) | n/a | (201) |
| Consolidated operating income | 7,204 | 39 | 1,873 | 27 | 5,416 | 344 |

Segment operating income is the filer's measure (net sales less cost of products sold, segment SG&A and other segment costs); the Q3 2026 Home and Commercial Solutions loss includes the 101 impairment within other segment costs of 104. Learning and Development's 9M 2026 segment operating income of 553 exceeds the 545 segment total, with Home and Commercial Solutions at 9 and Outdoor and Recreation at a loss of 17.

### Debt instruments at 2026-09-30

| Instrument | Issuer and co-issuer | Carrying value 2026-09-30 | Carrying value 2025-12-31 | Rate | Maturity | Security and guarantors as printed |
| --- | --- | --- | --- | --- | --- | --- |
| Senior notes | Newell Brands Inc.; no co-issuer printed | 1,242 | 1,239 | 8.500% | 2028 | Senior unsecured obligations of the Company (principal 1,250); guarantors not printed |
| Senior notes | Newell Brands Inc.; no co-issuer printed | 475 | 492 | 6.625% | 2029 | Security and guarantors not printed in pages read; 500 of floating-rate swaps designated as fair value hedge |
| Senior notes | Newell Brands Inc.; no co-issuer printed | 744 | 743 | 6.375% | 2030 | Security and guarantors not printed in pages read; indenture has additional covenants |
| Asset-based revolving credit facility | Newell Brands Inc. with Newell Brands Ireland Services DAC as subsidiary borrower | 215 | not applicable | SOFR plus 1.50% to 2.00%, or alternate base rate plus 0.50% to 1.00% | 2031-07-30, can spring earlier | Secured by a lien on deposit accounts, receivables, inventory, equipment and intellectual property in Eligible Jurisdictions; guaranteed by certain domestic and foreign subsidiary guarantors (not named); commitment up to 800 |
| Senior notes | Newell Brands Inc.; no co-issuer printed | 592 | not applicable | 6.250% | 2031 | Senior unsecured obligations of the Company (principal 600); guarantors not printed |
| Senior notes | Newell Brands Inc.; no co-issuer printed | 495 | 495 | 6.625% | 2032 | Security and guarantors not printed in pages read; indenture has additional covenants |
| Senior notes | Newell Brands Inc.; no co-issuer printed | 418 | 417 | 5.375% | 2036 | Security and guarantors not printed in pages read |
| Senior notes | Newell Brands Inc.; no co-issuer printed | 658 | 658 | 5.500% | 2046 | Security and guarantors not printed in pages read |
| Revolving credit facility (Credit Revolver, replaced 2026-07-30) | Newell Brands Inc. | 0 | 130 | Not printed in pages read | August 2027 | Secured, with guarantors; replaced by the ABL facility |
| Senior notes due 2027 (redeemed) | Newell Brands Inc. | 0 | 497 | 6.375% | 2027 | Redeemed in August 2026 |
| Other debt | Not printed | 2 | 2 | Not printed | Not printed | Not printed |
| Total debt | not applicable | 4,841 | 4,673 | 6.7% weighted average, Q3 2026 | not applicable | not applicable |

Coupon step-ups: about 1,080 of notes (the Coupon-Step Notes) had their rates raised by 50 bp in total after the 2025 downgrades and the maximum adjustment has been reached.

### Claims outside the debt figure

| Claim | Amount and period | Inside the debt figure? | Source note |
| --- | --- | --- | --- |
| Receivables factoring, Customer Receivables Purchase Agreement | 300 outstanding at 2026-09-30 (270 at 2025-12-31); limit cut from 700 to 625 effective 2026-09-14 | No | 10-Q Q3 page:9 |
| Receivables factoring, Receivables Facility | 135 outstanding at 2026-09-30 (125 at 2025-12-31); limit 75 from 2026-10-02 | No | 10-Q Q3 page:10, page:34 |
| Operating lease liabilities | 411 noncurrent plus 113 in other accrued liabilities at 2026-09-30 | No | 10-Q Q3 page:2, page:17 |
| Standby letters of credit | 64 primarily for self-insurance programs, and 46 against the ABL facility, at 2026-09-30 | No (the 46 reduces ABL availability) | 10-Q Q3 page:20, page:34 |
| Pension, retiree medical and supplemental plans | Not supplied in this module: the funded status table is in 10-K Footnote 10 and was not extracted; termination of nonqualified plans is expected to produce a net cash benefit of about 60 | No | 10-K page:111 onward; release page:4 |
| Litigation and indemnities | USPC sale indemnification claim and U.S. Tax Court proceedings; no amount is quantified in the pages read | No | 10-Q Q3 page:34 |

### Covenants and definition differences

The former Credit Revolver required financial covenants testing a Collateral Coverage Ratio and a Total Net Leverage Ratio, with the leverage test scheduled to step down at the quarter ending 2026-09-30; neither level nor the reported ratio is printed in the pack, so headroom is Not calculable. That facility was replaced on 2026-07-30 by the ABL facility, whose only printed financial test is a Consolidated Fixed Charge Coverage Ratio that applies if borrowings exceed levels relative to capacity during compliance testing periods; the level and the trigger are not printed. The issuer states compliance with all debt covenants at 2026-09-30. The Total Net Leverage Ratio is defined in the Credit Revolver, which is not supplied; the leverage ratios in this handoff use management's net debt (carrying value less unrestricted cash) over management's Normalized EBITDA and should not be read as the covenant measure.

### Latest quarter and subsequent events

| Date | Event | Amount | Source |
| --- | --- | --- | --- |
| 2026-07-30 | New five-year ABL facility replaces the Credit Revolver; 490 drawn on closing to repay it; uncommitted accordion up to 500 | Up to 800 | 10-Q Q3 page:19 |
| 2026-08 | Issued 6.250% senior notes due 2031 and redeemed the 6.375% notes due 2027 at 101.530% | 600 issued, proceeds 592; about 508 paid to redeem | 10-Q Q3 page:18 |
| Q3 2026 | Loss on extinguishment of debt | 16 (13 on the notes plus 3 of revolver costs) | 10-Q Q3 page:2, page:18, page:19 |
| Q3 2026 | Non-cash impairment of an indefinite-lived tradename in Home and Commercial Solutions | 101 | Release page:2 |
| 2026-09-14 | Customer Receivables Purchase Agreement limit cut to 625 and a first-priority lien granted over certain receivables not sold | 625 | 10-Q Q3 page:9 |
| 2026-10-02 | Receivables Facility renewed to 2027-10-01 with the limit on factored receivables outstanding cut to 75 | 75 | 10-Q Q3 page:34 |
| 2026-10-30 | Outlook: full-year operating cash flow about 150; the issuer anticipates reducing total debt and factoring by a couple of hundred million dollars in 2026 | about 150 | Release page:1, page:4 |

### Reported facts and locators (exact substrings)

| Topic | Source and locator | Exact quote |
| --- | --- | --- |
| Q3 and nine-month operating income | 10-Q_2026-09-30 page:2 | "Operating income 27 119 344 311" |
| Q3 impairment | 10-Q_2026-09-30 page:2 | "Impairment of goodwill, intangibles and other assets 101 — 101 —" |
| FY2025 operating income | 10-K_2025-12-31 page:81 | "Operating income (loss) 39 67 (85)" |
| FY2025 net loss | 10-K_2025-12-31 page:81 | "Net loss $ (285) $ (216) $ (388)" |
| FY2025 operating cash flow | 10-K_2025-12-31 page:82 | "Net cash provided by operating activities 264 496 930" |
| FY2025 capital expenditures | 10-K_2025-12-31 page:82 | "Capital expenditures (247) (259) (284)" |
| FY2025 cash dividends | 10-K_2025-12-31 page:82 | "Cash dividends (120) (118) (184)" |
| FY2025 cash interest | 10-K_2025-12-31 page:82 | "Cash paid for interest 354 319 298" |
| FY2025 cash taxes | 10-K_2025-12-31 page:82 | "Cash paid for income taxes, net of refunds (Footnote 11) 137 173 103" |
| 9M 2026 operating cash flow | 10-Q_2026-09-30 page:3 | "Net cash provided by operating activities 93 103" |
| Q1 2026 operating cash flow | 10-Q_2026-03-31 page:3 | "Net cash used in operating activities (233) (213)" |
| Six-month 2026 operating cash flow | 10-Q_2026-06-30 page:3 | "Net cash used in operating activities (204) (271)" |
| 9M 2026 capital expenditures | 10-Q_2026-09-30 page:3 | "Capital expenditures (131) (177)" |
| 9M 2026 dividends | 10-Q_2026-09-30 page:3 | "Cash dividends (97) (90)" |
| Q1 2026 capital expenditures | 10-Q_2026-03-31 page:3 | "Capital expenditures (37) (59)" |
| Six-month 2026 capital expenditures | 10-Q_2026-06-30 page:3 | "Capital expenditures (84) (118)" |
| Q1 2026 cash dividends | 10-Q_2026-03-31 page:3 | "Cash dividends (36) (31)" |
| Six-month 2026 cash dividends | 10-Q_2026-06-30 page:3 | "Cash dividends (66) (60)" |
| Net debt, Q3 2026 | EX-99.1_2026-10-30 page:17 | "Net debt [1] $ 4,592 $ 4,470 $ 4,548" |
| LTM normalized EBITDA, Q3 2026 | EX-99.1_2026-10-30 page:18 | "Normalized EBITDA $ 1,030 $ 882 $ 857" |
| LTM interest, Q3 2026 | EX-99.1_2026-10-30 page:18 | "Interest expense, net 341 321 309" |
| Net debt, Q2 2026 | EX-99.1_2026-07-31 page:17 | "Net debt [1] $ 4,797 $ 4,470 $ 4,858" |
| LTM normalized EBITDA, Q2 2026 | EX-99.1_2026-07-31 page:17 | "Normalized EBITDA $ 1,007 $ 882 $ 882" |
| Net debt, Q1 2026 | EX-99.1_2026-05-01 page:15 | "Net debt [1] $ 4,764 $ 4,470 $ 4,687" |
| LTM normalized EBITDA, Q1 2026 | EX-99.1_2026-05-01 page:15 | "Normalized EBITDA $ 881 $ 882 $ 884" |
| Debt table, Q3 2026 | 10-Q_2026-09-30 page:17 | "Total debt 4,841 4,673" |
| Debt table, Q1 2026 | 10-Q_2026-03-31 page:12 | "Total debt 4,965 4,673" |
| Debt table, Q2 2026 | 10-Q_2026-06-30 page:14 | "Total debt 5,006 4,673" |
| Maturity ladder | 10-K_2025-12-31 page:107 | "$130 $500 $1,252 $500 $750 $1,586 $4,718" |
| Redemption price | 10-Q_2026-09-30 page:18 | "at a redemption price equal to 101.530% of the outstanding aggregate principal amount of the notes" |
| ABL pricing | 10-Q_2026-09-30 page:20 | "ranging from 1.50% to 2.00% for SOFR-based loans" |
| ABL springing maturity | 10-Q_2026-09-30 page:20 | "solely to the extent that any indebtedness in an aggregate principal amount of $125 million or more" |
| ABL availability | 10-Q_2026-09-30 page:20 | "there was $741 million of availability under the ABL Credit Facility" |
| ABL letters of credit | 10-Q_2026-09-30 page:20 | "approximately $46 million of outstanding standby letters of credit issued against the ABL Credit Facility" |
| ABL net availability | 10-Q_2026-09-30 page:20 | "resulting in a net availability of approximately $480 million" |
| Cash held abroad | 10-Q_2026-09-30 page:48 | "of which approximately $174 million was held by the Company’s non-U.S. subsidiaries" |
| Credit Revolver net availability, FY2025 | 10-K_2025-12-31 page:106 | "resulting in a net availability of approximately $685 million" |
| Credit Revolver net availability, Q1 2026 | 10-Q_2026-03-31 page:13 | "resulting in a net availability of approximately $327 million" |
| Credit Revolver net availability, Q2 2026 | 10-Q_2026-06-30 page:14 | "resulting in a net availability of approximately $451 million" |
| Weighted average rate | 10-Q_2026-09-30 page:21 | "Total debt 6.7 % 6.6 % 6.8 % 6.3 %" |
| Fair value hedge on 2029 notes | 10-Q_2026-09-30 page:22 | "$500 million notional amount of interest rate swaps due September 2029" |
| Coupon-step notes | 10-K_2025-12-31 page:107 | "aggregating to approximately $1.08 billion (the “Coupon-Step Notes”)" |
| Factoring, first program | 10-Q_2026-09-30 page:9 | "Outstanding receivables sold under the Customer Receivables Purchase Agreement at September 30, 2026 and December 31, 2025 were approximately $300 million and $270 million, respectively." |
| Factoring, second program | 10-Q_2026-09-30 page:10 | "Outstanding receivables sold under the Receivables Facility at September 30, 2026 and December 31, 2025 were approximately $135 million and $125 million, respectively." |
| Subsequent event | 10-Q_2026-09-30 page:34 | "the facility limit on factored receivables outstanding was amended to $75 million" |
| Self-insurance letters of credit | 10-Q_2026-09-30 page:34 | "At September 30, 2026, the Company had approximately $64 million in standby letters of credit" |
| Operating lease liabilities | 10-Q_2026-09-30 page:2 | "Operating lease liabilities 411 433" |
| Current operating lease liabilities | 10-Q_2026-09-30 page:17 | "Operating lease liabilities 113 113" |
| Covenant compliance | 10-Q_2026-09-30 page:50 | "The Company was in compliance with all of its debt covenants at September 30, 2026." |
| Prior covenant tests | 10-K_2025-12-31 page:106 | "requires the Company to satisfy financial covenants testing the Company’s Collateral Coverage Ratio and Total Net Leverage Ratio" |
| New covenant | 10-Q_2026-09-30 page:19 | "requires the Company to satisfy a Consolidated Fixed Charge Coverage Ratio (as defined in the ABL Credit Agreement) if borrowings exceed certain levels relative to capacity" |
| Tariff recoveries in Q2 2026 | EX-99.1_2026-07-31 page:2 | "Second quarter reported and normalized results included approximately $100 million pretax" |
| Additional tariff recoveries in Q2 2026 | EX-99.1_2026-07-31 page:2 | "In addition, second quarter normalized results included approximately $26 million pretax" |
| Tradename impairment | EX-99.1_2026-10-30 page:2 | "The current period included a non-cash impairment charge of $101 million related to an indefinite-lived tradename." |
| Deleveraging intent | EX-99.1_2026-10-30 page:1 | "we anticipate reducing total debt and factoring by a couple hundred million dollars this year" |
| Operating cash flow outlook | EX-99.1_2026-10-30 page:4 | "Based on these two items the Company has revised its full-year operating cash flow guidance to approximately $150 million." |
| Segment results, Q3 2026 | 10-Q_2026-09-30 page:27 | "Segment operating income (loss) $ 86 $ (37) $ 137 $ (14) $ 156 $ 40 $ 124 $ (8)" |
| Segment results, 9M 2026 | 10-Q_2026-09-30 page:28 | "Segment operating income (loss) $ 545 $ 9 $ 553 $ (17) $ 481 $ 62 $ 424 $ (5)" |
| Segment results, FY2025 | 10-K_2025-12-31 page:131 | "Segment operating income (loss) $ 301 $ (138) $ 464 $ (25)" |

## Calculations

All inputs are quoted in `### Reported facts and locators`. USD millions; ratios in x rounded to two decimals; the calculation is the only place a derived value is created.

### LTM Q3 2026 income and cash flow (FY2025 + 9M 2026 - 9M 2025)

| Item | Formula | Result |
| --- | --- | --- |
| Net sales | 7,204 + 5,416 - 5,307 | 7,313 |
| Gross profit | 2,432 + 1,974 - 1,804 | 2,602 |
| SG&A | 1,985 + 1,499 - 1,471 | 2,013 |
| Restructuring costs, net | 62 + 30 - 22 | 70 |
| Impairment | 346 + 101 - 0 | 447 |
| Operating income | 39 + 344 - 311 | 72 |
| Interest expense, net | 321 + 257 - 237 | 341 |
| Net loss | -285 + -8 - 30 | -323 |
| Depreciation and amortization | 311 + 234 - 231 | 314 |
| Operating cash flow | 264 + 93 - 103 | 254 |
| Capital expenditures | 247 + 131 - 177 | 201 |
| Cash dividends | 120 + 97 - 90 | 127 |
| Operating cash flow less capital expenditures | 254 - 201 | 53 |
| Operating cash flow less capital expenditures less dividends | 53 - 127 | -74 |

### Discrete quarters from cumulative cash flow amounts

| Item | Formula | Result |
| --- | --- | --- |
| Q2 2026 operating cash flow | six months (-204) less Q1 (-233) | 29 |
| Q3 2026 operating cash flow | nine months 93 less six months (-204) | 297 |
| Q2 2026 capital expenditures | 84 - 37 | 47 |
| Q3 2026 capital expenditures | 131 - 84 | 47 |
| Q2 2026 dividends | 66 - 36 | 30 |
| Q3 2026 dividends | 97 - 66 | 31 |
| Q2 2026 depreciation and amortization | 157 - 79 | 78 |
| Operating cash flow less capex: Q1, Q2, Q3, 9M 2026, 9M 2025, FY2025 | -233-37; 29-47; 297-47; 93-131; 103-177; 264-247 | -270; -18; 250; -38; -74; 17 |

### Leverage

| Period | Gross debt / EBITDA | Net debt / EBITDA |
| --- | --- | --- |
| FY2025 | 4,673 / 882 = 5.30 | 4,470 / 882 = 5.07 |
| Q1 2026 | 4,965 / 881 = 5.64 | 4,764 / 881 = 5.41 |
| Q2 2026 | 5,006 / 1,007 = 4.97 | 4,797 / 1,007 = 4.76 |
| Q3 2026 | 4,841 / 1,030 = 4.70 | 4,592 / 1,030 = 4.46 |
| FY2025 on filing-basis EBITDA before impairment (39 + 311 + 346 = 696) | 4,673 / 696 = 6.71 | 4,470 / 696 = 6.42 |
| Q3 2026 on filing-basis EBITDA before impairment (72 + 314 + 447 = 833) | 4,841 / 833 = 5.81 | 4,592 / 833 = 5.51 |

Net debt check: 4,841 - 249 = 4,592 and 4,673 - 203 = 4,470, equal to the release. Change in net debt from FY2025 to Q3 2026: 4,592 - 4,470 = 122 (an increase). Change in trailing-twelve-month Normalized EBITDA: 1,030 - 882 = 148. Quarterly Normalized EBITDA 135 + 406 + 248 = 789 equals the printed 9M 2026 figure.

Sensitivity to tariff recoveries (illustrative, one-sided): removing the 100 and 26 of pre-tax recoveries named for Q2 2026 from trailing-twelve-month Normalized EBITDA gives 1,030 - 126 = 904; net debt / 904 = 5.08 and gross debt / 904 = 5.36. This ignores the tariff costs the recoveries relate to, some of which sit in the same twelve-month window, so it is a bound for sensitivity, not an estimate.

### Interest cover

| Basis | Formula | Result |
| --- | --- | --- |
| FY2025 cash basis | 882 / 354 | 2.49 |
| FY2025 expense basis | 882 / 321 | 2.75 |
| LTM Q3 2026 expense basis | 1,030 / 341 | 3.02 |
| LTM Q1 2026 expense basis | 881 / 333 | 2.65 |
| LTM Q2 2026 expense basis | 1,007 / 338 | 2.98 |

### Liquidity

| Date | Formula | Result |
| --- | --- | --- |
| 2025-12-31 availability check | 852 - 130 - 37 | 685, equal to the printed figure |
| 2026-03-31 availability check | 789 - 425 - 37 | 327, equal to the printed figure |
| 2026-06-30 availability check | 969 - 470 - 48 | 451, equal to the printed figure |
| 2026-09-30 availability check | 741 - 215 - 46 | 480, equal to the printed figure |
| Total liquidity before factoring: FY2025, Q1, Q2, Q3 2026 | 203 + 685; 201 + 327; 209 + 451; 249 + 480 | 888; 528; 660; 729 |

### Maturity roll-forward (derived, not printed)

2025-12-31 printed ladder total: 130 + 500 + 1,252 + 500 + 750 + 1,586 = 4,718. Roll-forward to 2026-09-30: remove 130 (revolver repaid) and 500 (notes due 2027 redeemed), add 600 (notes due 2031) and 215 (ABL drawn): 4,718 - 130 - 500 + 600 + 215 = 4,903, equal to the sum of the rows in the maturity chart (1,252 + 500 + 750 + 815 + 1,586 = 4,903). This assumes no other principal changed; carrying value 4,841 is net of unamortized costs and hedge adjustments, so the principal-based total exceeds it. Carrying value composition check: 1,242 + 475 + 744 + 215 + 592 + 495 + 418 + 658 + 2 = 4,841.

### Claims outside debt

Factoring outstanding: 300 + 135 = 435 at 2026-09-30; 270 + 125 = 395 at 2025-12-31. Operating lease liabilities: 411 + 113 = 524 at 2026-09-30.

## Gaps

| Gap | Effect on this module | Action |
| --- | --- | --- |
| Covenant levels and reported covenant ratios are not supplied for the former Collateral Coverage Ratio and Total Net Leverage Ratio, or for the ABL Consolidated Fixed Charge Coverage Ratio. | Covenant headroom is Not calculable; leverage ratios here are not covenant measures. | Take levels from the credit agreements if obtained; otherwise leave headroom unassessed. |
| Cash paid for interest and for taxes is printed for FY2025 only. | Cash interest cover for the 2026 periods is Not supplied; expense-based cover is shown as context only. | Do not annualize or infer 2026 cash interest. |
| The only printed maturity ladder is at 2025-12-31. The roll-forward to 2026-09-30 is derived, and the 2028 notes' maturity date, the principal split of the 2032, 2036 and 2046 notes and the guarantor list are not printed in the pages read. | Maturity chart rows for 2026, 2027 and 2031 are derived; the springing date of the ABL maturity cannot be dated. | Treat the chart as derived; confirm the principal amounts and 2028 maturity date from the indentures if obtained. |
| Normalized EBITDA is a management non-GAAP measure with its own add-backs (share-based compensation, restructuring, impairment of acquired intangibles and other items) and, for Q2 2026 onward, tariff recoveries. | Leverage on the chart is management-basis; the filing-basis ratios are shown for contrast. | Keep attributed to management; do not substitute it for a covenant EBITDA. |
| Debt is at carrying value (net of unamortized costs, with hedge adjustments), not principal. | Gross debt and net debt ratios are slightly lower than on a principal basis (4,903 derived principal against 4,841 carrying). | State the basis wherever a leverage figure is quoted. |
| Pension and retiree medical funded status, litigation reserves and the nonqualified plan termination are not extracted. | Debt-like claims outside the debt table are incomplete. | Extract 10-K Footnote 10 and Footnote 17 in the next module if needed. |
| Restricted cash (26 at 2026-09-30) is excluded from cash in the chart; cash of about 174 is held by non-US subsidiaries, with no repatriation cost stated in the pages read. | Usable group liquidity may be lower than the headline cash. | Treat non-US cash as potentially trapped until evidence says otherwise. |
| Q4 2025 is not printed as a discrete quarter. | Discrete Q4 2025 leverage and EBITDA are not shown. | Not needed for the charts; derive only if required. |
| Ratings, market quotes and peers are blank in the context. | No market-implied or ratings view is possible here. | None for this module. |

## Next module

Proceed to CP-1A (business and transaction view) using the Q3 2026 report and release for the refinancing, the asset-based facility, the receivables amendments and the tradename impairment. Carry forward: leverage uses management Normalized EBITDA with tariff recoveries in Q2 2026; net debt rose while the ratio fell; cash interest, covenant levels and executed agreements are Not supplied; the maturity chart rows for 2026, 2027 and 2031 are a derived roll-forward; factoring of 435 at 2026-09-30 sits outside the debt table. CP-2 and CP-5 follow.
