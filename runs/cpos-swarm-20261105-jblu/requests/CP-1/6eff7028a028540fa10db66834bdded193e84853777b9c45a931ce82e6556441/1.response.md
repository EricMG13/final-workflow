# CP-1 — Financial base: JETBLUE AIRWAYS CORP (jblu)

## Request

- Issuer: JETBLUE AIRWAYS CORP (registrant "JETBLUE AIRWAYS CORPORATION", ticker JBLU). As-of date 2026-11-05; information cutoff 2026-11-05.
- Pathway `credit_snapshot`. Reporting currency USD; all amounts are US$ millions unless stated. Current period Q3 2026 (quarter ended September 30, 2026); prior period FY2025 (context).
- Scope: the issuer's own consolidated reported financials, debt, liquidity, claims outside debt, covenant disclosure and latest-quarter events, with computed credit metrics. This is a factual and computational base for later modules; it is not a rating view or an investment opinion.
- Perimeter: JetBlue Airways Corporation consolidated. The filings describe one reportable segment (10-K page:159). There is no parent in the sources. JetBlue Loyalty LP is a co-issuer of the TrueBlue financings and is inside the consolidated statements; no stand-alone figures for it are supplied.
- Execution: host session; the host read the pinned text and computed every derived figure shown in `## Calculations`. No provider was called.

## Sources

Hashes are the sha256 of the pinned text extractions named by CP-OS. A locator `page:N` is the extraction chunk number, not the printed page.

| Source | sha256 | Use in this handoff |
| --- | --- | --- |
| 10-K_2025-12-31_jblu-20251231.htm.jsonl | 5eaf617accf854e4d3e9a550a2ff2955ebfa71253742ee07dd6faac0b2e32a8c | Audited FY2025 and FY2024 statements, debt note and rates, maturities, cash interest, covenant text |
| 10-Q_2026-03-31_jblu-20260331.htm.jsonl | 23aa04d969e5d0170c0af37c935f385dfb36e65e5eefd81c73b6d9abfad792fa | Q1 2026 discrete quarter statement of operations |
| 10-Q_2026-06-30_jblu-20260630.htm.jsonl | 909f0d616195258039c6cade15d6ec9c2498b992386b681904fa4366c00d0fca | Q2 2026 discrete quarter and six-month statements, six-month cash flow |
| 10-Q_2026-09-30_jblu-20260930.htm.jsonl | acf402823b4f024901754bb305241f6c703d6a3c7b62a75b67703d555b0a8e99 | Q3 2026 and nine-month statements, balance sheet, debt note, liquidity, commitments, covenants |
| EX-99.1_2026-04-28_ex991-earningsreleaseq12026.htm.jsonl | d4d4219d15ba6a638e2373e8ae55aa1c8d909855e1454637cd8095dcf728854e | Tie-out of Q1 2026 statement of operations to the 10-Q |
| EX-99.1_2026-07-28_ex991-earningsreleaseq22026.htm.jsonl | 802f55be8bbdb2947fd6f1ea1be406ca4f8ca6aa8c3d778ecad7cf301e68ccf6 | Tie-out of Q2 2026 statement of operations to the 10-Q |
| EX-99.1_2026-10-26_ex991-earningsreleaseq32026.htm.jsonl | 698b07a0502ae526f90cdcc0cd39f907723cfed08c5317bc057549e3a8aec7de | Tie-out of Q3 2026 statement and total debt; attributed management liquidity and asset claims |
| context | 31c25d56081dda135cad8e796a84043b049461aaa2d0b6432dd4792f868c14f8 | Run settings (period labels, currency); not issuer evidence |

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | 5f1fd6d78bb06a0ae2ac09089d15d4162bd31f1324bf5098e03d0142b1a1dcc0 |

CP-0 reported READY_WITH_LIMITATIONS for this module: text extraction only, executed debt agreements not supplied, no numeric covenant levels, and two debt totals on different bases. This handoff carries each of those limits forward and does not correct CP-0.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| On a computed last-twelve-months basis to September 30, 2026, JetBlue carries 56.33x debt to EBITDA excluding special items, covers cash interest 0.30x, and holds 2,226 US$m of liquidity against 8,393 US$m of debt. | Medium | The issuer reports no EBITDA, so every leverage and cover ratio rests on our own definition. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Operating results weakened: the last-twelve-months operating loss is 609 US$m, against 368 US$m for FY2025, because fuel expense grew by a larger percentage than revenue. | Earnings do not support the debt load, so repayment relies on liquidity and refinancing. | High |
| Debt of 8,393 US$m is almost unchanged from year-end FY2025, while unrestricted cash and investments fell from 2,477 US$m to 1,626 US$m. | Net debt rose from 6,021 US$m to 6,767 US$m. | High |
| Maturities are modest until 2029, when 1,835 US$m falls due, and 4,691 US$m falls due after 2030. | Near-term refinancing need is modest against liquidity; the 2029 wall is the pressure point. | Medium |
| Management states covenant compliance but no covenant level or headroom is printed. | Covenant headroom cannot be measured from these filings. | Medium |

### Financial base view

The financial base is usable. Audited FY2024 and FY2025 statements and unaudited statements for Q1, Q2 and Q3 2026 are located and tie to the earnings releases. Revenue grew in every 2026 quarter, but fuel and labor costs grew faster, so the operating result deteriorated year on year: the nine-month 2026 operating loss was 509 against 268 in the prior-year nine months. The issuer prints no EBITDA, so EBITDA here is operating income plus depreciation and amortization, with the separately printed special items added back; the unadjusted figure is shown beside it. On that basis leverage and interest cover are weak and worsen from FY2025 to the last twelve months, and the ratios are very sensitive to a small EBITDA denominator. Liquidity is 2,226 on a computed basis (cash, cash equivalents and investment securities plus the undrawn 600 Citibank revolver), which matches management's stated 2.2 billion. Maturities before 2029 are small relative to liquidity. Limits: the issuer reports no covenant levels, executed agreements are not supplied, and amounts are rounded to millions.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 15.19 | 8.17 | x | Debt 8,539 (carrying value at December 31, 2024); EBITDA excluding special items 562 (operating loss plus D&A plus special items); net debt uses unrestricted cash, cash equivalents and investment securities 3,946. FY2024 special items of 591 include non-cash Spirit items and are added back. |
| FY2025 | 24.28 | 17.20 | x | Debt 8,498 (carrying value at December 31, 2025); EBITDA excluding special items 350; net debt uses 2,477 of unrestricted cash, cash equivalents and investment securities. Issuer reports no EBITDA; this is our computation. |
| LTM Q3 2026 | 56.33 | 45.42 | x | Debt 8,393 at September 30, 2026; LTM EBITDA excluding special items 149 (FY2025 plus nine months 2026 less nine months 2025); net debt uses 1,626. Unadjusted LTM EBITDA is 115, which would give higher ratios. Restricted cash of 264 is excluded. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 2.44 | x | EBITDA excluding special items 562 divided by cash interest paid, net 230; the FY2025 10-K describes this as net of interest income cash receipts. |
| FY2025 | 0.82 | x | EBITDA excluding special items 350 divided by cash interest paid, net 427, net of interest income cash receipts per the 10-K. |
| LTM Q3 2026 | 0.30 | x | LTM EBITDA excluding special items 149 divided by LTM cash interest paid, net 493 (427 plus 372 less 306). The nine-month cash flow line carries the same label but the interim filing does not repeat the net-of-interest-income wording. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (December 31, 2025) | 2477 | 600 | US$m | Cash is unrestricted cash and equivalents 1,946 plus current investment securities 213 plus non-current investment securities 318. Undrawn is the Citibank revolver of 600 with no balance outstanding. Excludes restricted cash of 349 and the Morgan Stanley line. |
| Q3 2026 (September 30, 2026) | 1626 | 600 | US$m | Cash is 1,258 plus current investment securities 251 plus non-current investment securities 117. Undrawn is the Citibank revolver of 600, no balance outstanding. The Morgan Stanley line of up to approximately 200 is excluded because availability varies with pledged securities. No letters of credit are drawn on the revolver; the letters of credit disclosed are cash-collateralised in restricted cash. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remainder of 2026 | 152 | US$m | Scheduled maturities of long-term debt and finance lease obligations at September 30, 2026, net of debt issuance costs. |
| 2027 | 477 | US$m | Same basis. |
| 2028 | 582 | US$m | Same basis. |
| 2029 | 1835 | US$m | Same basis; includes the 2.50% convertible senior notes and the TrueBlue term loan facility, both due 2029. |
| 2030 | 656 | US$m | Same basis. |
| Thereafter | 4691 | US$m | Same basis; the maturity table totals 8,393. |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2024 | FY2025 | Nine months 2025 | Nine months 2026 | LTM Q3 2026 |
| --- | --- | --- | --- | --- | --- |
| Total operating revenues | 9,279 | 9,062 | 6,818 | 7,749 | 9,993 |
| Operating loss | (684) | (368) | (268) | (509) | (609) |
| Depreciation and amortization | 655 | 688 | 512 | 548 | 724 |
| Special items (expense) | 591 | 30 | 29 | 33 | 34 |
| EBITDA, computed (operating loss plus D&A) | (29) | 320 | 244 | 39 | 115 |
| EBITDA excluding special items, computed | 562 | 350 | 273 | 72 | 149 |
| Interest expense | 365 | 588 | 441 | 440 | 587 |
| Cash interest paid, net | 230 | 427 | 306 | 372 | 493 |
| Net loss | (795) | (602) | (425) | (823) | (1,000) |
| Net cash (used in) provided by operating activities | 144 | (94) | (143) | (273) | (224) |
| Capital expenditures | 1,478 | 1,078 | 742 | 575 | 911 |
| Pre-delivery deposits for flight equipment | 141 | 44 | 35 | 49 | 58 |
| Free cash flow, computed (operating cash flow less capex less pre-delivery deposits) | (1,475) | (1,216) | (920) | (897) | (1,193) |
| Total debt, carrying value, period end | 8,539 | 8,498 | Not supplied | 8,393 | 8,393 |
| Unrestricted cash, equivalents and investment securities, period end | 3,946 | 2,477 | Not supplied | 1,626 | 1,626 |
| Net debt, computed | 4,593 | 6,021 | Not supplied | 6,767 | 6,767 |
| Total debt / EBITDA excluding special items (x) | 15.19 | 24.28 | Not supplied | Not calculable | 56.33 |
| Net debt / EBITDA excluding special items (x) | 8.17 | 17.20 | Not supplied | Not calculable | 45.42 |
| EBITDA excluding special items / cash interest paid (x) | 2.44 | 0.82 | 0.89 | 0.19 | 0.30 |

Reading of the table: the nine-month columns are year-to-date flows; period-end balances exist only for December 31, 2024, December 31, 2025 and September 30, 2026, so a September 30, 2025 balance and nine-month leverage are not supplied or not calculable (a nine-month EBITDA divided into a September balance is not an annual leverage ratio).

### Reported statements

#### Statement of operations by period (US$m, from the statements)

| Line | Q1 2026 | Q2 2026 | Q3 2026 | Nine months 2026 | Q3 2025 | Nine months 2025 | FY2025 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total operating revenues | 2,240 | 2,697 | 2,812 | 7,749 | 2,322 | 6,818 | 9,062 |
| Aircraft fuel | 573 | 911 | 868 | 2,352 | 539 | 1,554 | 2,057 |
| Salaries, wages and benefits | 896 | 875 | 946 | 2,717 | 865 | 2,579 | 3,453 |
| Depreciation and amortization | 179 | 183 | 186 | 548 | 173 | 512 | 688 |
| Special items | — (no amount printed) | — (no amount printed) | 33 | 33 | 5 | 29 | 30 |
| Total operating expenses | 2,464 | 2,838 | 2,956 | 8,258 | 2,422 | 7,086 | 9,430 |
| Operating loss | (224) | (141) | (144) | (509) | (100) | (268) | (368) |
| Interest expense | (144) | (147) | (149) | (440) | (146) | (441) | (588) |
| Net loss | (319) | (247) | (257) | (823) | (143) | (425) | (602) |

Locators: Q1 column Q1 10-Q page:6; Q2 column Q2 10-Q page:6; Q3 and nine-month columns Q3 10-Q page:6; FY2025 column 10-K page:113. The Q1 and Q2 columns are discrete three-month results printed in those reports.

#### Balance sheet (US$m)

| Line | September 30, 2026 | December 31, 2025 | December 31, 2024 |
| --- | --- | --- | --- |
| Cash and cash equivalents | 1,258 | 1,946 | 1,921 |
| Investment securities, current | 251 | 213 | 1,689 |
| Investment securities, non-current | 117 | 318 | 336 |
| Restricted cash and cash equivalents, current | 9 | 100 | — (no amount printed) |
| Restricted cash and cash equivalents, non-current | 255 | 249 | 227 |
| Total current assets | 2,793 | 3,238 | 4,258 |
| Total assets | 15,966 | 16,570 | 16,841 |
| Air traffic liability, current | 1,925 | 1,669 | 1,572 |
| Current maturities of long-term debt and finance lease obligations | 482 | 769 | 392 |
| Long-term debt and finance lease obligations | 7,911 | 7,729 | 8,147 |
| Current operating lease liabilities | 101 | 79 | 93 |
| Long-term operating lease liabilities | 852 | 839 | 510 |
| Air traffic liability, non-current | 771 | 704 | 653 |
| Total stockholders' equity | 1,337 | 2,120 | 2,641 |

Locators: Q3 10-Q page:5 and page:6; 10-K page:112 and page:113.

#### Cash flow items (US$m)

| Line | FY2024 | FY2025 | Nine months 2025 | Nine months 2026 |
| --- | --- | --- | --- | --- |
| Net cash (used in) provided by operating activities | 144 | (94) | (143) | (273) |
| Capital expenditures | (1,478) | (1,078) | (742) | (575) |
| Pre-delivery deposits for flight equipment | (141) | (44) | (35) | (49) |
| Proceeds from issuance of long-term debt, net of issuance costs | 3,793 | — (no amount printed) | — (no amount printed) | 495 |
| Repayment of long-term debt and finance lease obligations | (748) | (461) | (339) | (658) |
| Cash payments for interest, net | (230) | (427) | (306) | (372) |

Locators: 10-K page:114; Q3 10-Q page:7.

### Debt by instrument at September 30, 2026

| Instrument | September 30, 2026 | December 31, 2025 | Rate at December 31, 2025 (10-K) | Security |
| --- | --- | --- | --- | --- |
| Fixed rate special facility bonds, due through 2036 | 43 | 43 | 5.0 % | Secured |
| 2019-1 Series AA enhanced equipment notes, due through 2032 | 409 | 424 | 2.8 % | Secured by aircraft |
| 2019-1 Series A, due through 2028 | 128 | 132 | 3.0 % | Secured by aircraft |
| 2019-1 Series B, due through 2027 | 38 | 45 | 8.1 % | Secured by aircraft |
| 2020-1 Series A, due through 2032 | 407 | 428 | 4.1 % | Secured by aircraft |
| 2020-1 Series B, due through 2028 | 73 | 82 | 7.8 % | Secured by aircraft |
| Fixed rate equipment notes, due through 2036 | 573 | 127 | 4.0 % (10-K line, due through 2028); 2026 borrowings priced off U.S. Treasury rates plus a margin | Secured by aircraft |
| Floating rate equipment notes, due through 2036 | 619 | 673 | 6.7 % | Secured by aircraft |
| Aircraft failed sale-leaseback transactions, due through 2036 | 2,011 | 2,103 | 6.9 % | Secured by aircraft |
| TrueBlue senior secured notes, due through 2031 | 1,991 | 1,990 | 9.9 % (9.875% coupon) | Senior secured, first lien on loyalty collateral; co-issued by JetBlue and JetBlue Loyalty LP, guaranteed by the Guarantors |
| TrueBlue senior secured term loan facility, due through 2029 | 742 | 744 | 8.8 % | Senior secured pari passu with the notes; co-borrowers JetBlue and JetBlue Loyalty LP |
| Finance leases | 421 | 449 | 6.3 % | Secured by leased assets |
| Unsecured CARES Act Payroll Support Program loan, due through 2030 | 259 | 259 | 2.0 % | Unsecured, U.S. Treasury |
| Unsecured Payroll Support Program Extension loan, due through 2031 | 144 | 144 | 2.0 % | Unsecured, U.S. Treasury |
| Unsecured American Rescue Plan Act payroll support loan, due through 2031 | 132 | 132 | 2.0 % | Unsecured, U.S. Treasury |
| 0.50% convertible senior notes, due through 2026 | — (no amount printed) | 325 | 0.5 % | Unsecured; repaid in full April 1, 2026 |
| 2.50% convertible senior notes, due through 2029 | 460 | 460 | 2.5 % | Unsecured senior |
| Total debt and finance lease obligations (before issuance costs) | 8,450 | 8,560 | not applicable | not applicable |
| Less: debt issuance costs | (57) | (62) | not applicable | not applicable |
| Total debt, carrying value | 8,393 | 8,498 | not applicable | not applicable |

Locators: Q3 10-Q page:11 (September 30, 2026 and December 31, 2025 amounts), 10-K page:126 and page:127 (rates), 10-K page:129 to page:131 (TrueBlue terms), 10-K page:132 to page:135 (convertible notes). Rates for the instruments carried to September 30, 2026 are as of December 31, 2025; the Q3 10-Q prints no rate table.

### Claims outside the debt figure

| Claim | Amount | Inside or outside the debt figure | Locator and note |
| --- | --- | --- | --- |
| Failed sale-leasebacks | 2,011 | Inside (a line of the debt table) | Q3 10-Q page:11; the assets stay in property and equipment (10-K page:129) |
| Finance leases | 421 | Inside | Q3 10-Q page:11 |
| Operating lease liabilities | 953 (current 101 plus non-current 852) | Outside | Q3 10-Q page:6; undiscounted operating lease obligations 1,499 in the contractual obligations table, page:46 |
| Flight equipment purchase commitments | 5,372 | Outside | Q3 10-Q page:17; 77 aircraft deliveries committed |
| Other obligations (maintenance, infrastructure, information technology) | 1,673 | Outside | Q3 10-Q page:46 |
| Air traffic liability (current plus non-current) | 2,696 | Outside; a customer prepayment liability, not borrowed money | Q3 10-Q page:6 |
| Letters of credit | 58 for leases and 65 for JFK Millennium Partners | Outside; cash-collateralised in restricted cash | Q3 10-Q page:18 |
| Pensions and retiree medical | Not supplied | Not applicable | The only retirement plan described is a defined contribution 401(k) plan (Q3 10-Q page:17); no defined benefit obligation is printed. |
| Factoring and supply-chain finance | Not supplied | Not applicable | No mention in any of the seven sources |
| Litigation | Not estimable | Outside | Antitrust class action over the Northeast Alliance: "an estimate of the reasonably possible loss or range of loss, if any, cannot be made" (Q3 10-Q page:21). Q3 2026 special items include a litigation reserve adjustment of 33 (page:26). |

### Liquidity, covenants and ratings

- Liquidity at September 30, 2026: management states "$2.2 billion in liquidity, which includes $1.6 billion in unrestricted cash, cash equivalents, and investment securities and our $600 million undrawn Citibank line of credit" (Q3 10-Q page:44). Our computed total of 2,226 agrees. Management expects liquidity to be sufficient for at least the next 12 months (page:44).
- Facility expiry: the Citibank revolver of 600 matures October 21, 2029 (Q3 10-Q page:14); no facility used in liquidity expires within twelve months of the as-of date. The Morgan Stanley line is not committed to a fixed amount.
- Covenants: the Citibank revolver includes covenants requiring minimum balances of unrestricted cash, cash equivalents and unused commitments (10-K page:94). The TrueBlue notes and term loan carry "debt service coverage ratios and minimum liquidity requirements" and a cross-default to other material indebtedness (Q3 10-Q page:47). Management states "we were in compliance with the material covenants of our debt and lease agreements" (Q3 10-Q page:47). No level, step-down or reported ratio is printed, so headroom is Not calculable.
- Security: the net book value of pledged assets is $8.0 billion (Q3 10-Q page:11) and approximately 66% of owned property and equipment and intangibles are pledged or committed to be pledged (page:47). Management claims an unencumbered asset base of about $7 billion (Q3 release page:2); this is attributed to management and is not reconciled to the filing.
- Ratings: none supplied (context ratings field is blank).

### Latest quarter and subsequent events

- Q3 2026 against Q3 2025: total operating revenues 2,812 against 2,322; aircraft fuel 868 against 539; operating loss (144) against (100); net loss (257) against (143) (Q3 10-Q page:6). Management reports average fuel price per gallon of $3.91 against $2.49 (Q3 release page:8).
- Financing events in 2026: 0.50% convertible senior notes of 325 repaid April 1, 2026, partly from the 100 Citibank escrow (page:14); aircraft-secured financing of up to $500 million agreed April 14, 2026 and fully borrowed by September 30, 2026, maturities 2033 through 2036; a further $250 million is available and "Funding is expected in the fourth quarter of 2026" (page:14).
- Subsequent events up to the cutoff: acquisition of 22 LaGuardia slots from Spirit Airlines completed in October 2026 for an aggregate purchase price of $58.5 million (page:44); opposition to class certification filed October 9, 2026 (page:21). Nothing after October 26, 2026 is supplied.
- Other: supplemental agreements with IAE dated July 27, 2026 give credits up to $105 million against future purchases through December 31, 2027 (page:33).

### Definition review and interpretation

- EBITDA: no source prints the word EBITDA. EBITDA here is operating loss plus depreciation and amortization from the statements of operations, optionally plus the separately printed special items line. Aircraft rent (49 for nine months 2026) is not added back, so this is not EBITDAR. Capitalized interest is not adjusted.
- Special items: Q3 2026 special items are a litigation reserve remeasurement; FY2024 special items of 591 include a non-cash Spirit item of 450 per the FY2025 10-K cash flow statement (page:114). Adding special items back is a choice that raises EBITDA; the unadjusted measure is shown.
- Cash interest is "net" (net of interest income cash receipts per 10-K page:136), so it understates gross cash interest and the cover ratio is flattered by interest income. Interest income fell from 101 to 57 between the nine months of 2025 and 2026 (page:6).
- Debt basis: the debt table totals 8,450 before issuance costs; the carrying value, fair value table and release use 8,393. Credit metrics here use carrying value so that they tie to the release and the balance sheet (current 482 plus non-current 7,911 equals 8,393).
- Interpretation: fuel is the largest single driver of the deterioration. In Q3 2026 total operating expenses rose by 534 year on year, of which aircraft fuel accounts for 329 and salaries, wages and benefits for 81, against revenue growth of 490 (Q3 10-Q page:6). Operating cash flow was negative in both nine-month periods and free cash flow after capex and pre-delivery deposits was negative in every period shown, so capex and debt repayment in 2026 were met from the liquidity balance and from 495 of new secured borrowing: unrestricted cash and investments fell by 851 from December 31, 2025 to September 30, 2026 while 658 of debt and finance lease principal was repaid.

## Calculations

All amounts US$ millions. Inputs are cited above; recomputation checks follow.

### Tie-outs

- Quarters sum to nine months, revenue: 2,240 + 2,697 + 2,812 = 7,749, equal to the nine-month figure (Q1 10-Q page:6; Q2 10-Q page:6; Q3 10-Q page:6).
- Operating loss: (224) + (141) + (144) = (509), equal to the nine-month figure.
- D&A: 179 + 183 + 186 = 548, equal to the nine-month figure.
- Releases agree with the 10-Qs on revenue and operating loss for each quarter (Q1 release page:7 shows 2,240 and (224); Q2 release page:7 shows 2,697 and (141); Q3 release page:7 shows 2,812 and (144)).
- Maturity table: 152 + 477 + 582 + 1,835 + 656 + 4,691 = 8,393, equal to the carrying value (Q3 10-Q page:11 and page:12). December 31, 2025: 755 + 411 + 516 + 1,768 + 589 + 4,459 = 8,498 (10-K page:136).
- Balance sheet debt: 482 + 7,911 = 8,393. December 31, 2025: 769 + 7,729 = 8,498. December 31, 2024: 392 + 8,147 = 8,539.
- Debt table: sum of September 30, 2026 lines gives 8,450 before issuance costs; 8,450 less 57 equals 8,393. December 31, 2025: 8,560 less 62 equals 8,498.
- Debt movement, carrying value: 8,498 to 8,393 is a decrease of 105. Gross cash flow explains an increase of 495 raised less 658 repaid, plus 44 of flight equipment acquired under finance leases (Q3 10-Q page:7): 8,560 + 495 - 658 + 44 = 8,441 against the reported 8,450 before issuance costs; the residual of 9 is not itemized in the sources.

### EBITDA

- Computed EBITDA = operating income (loss) + depreciation and amortization.
- FY2024: (684) + 655 = (29); with special items 591: 562.
- FY2025: (368) + 688 = 320; with special items 30: 350.
- Nine months 2025: (268) + 512 = 244; with special items 29: 273.
- Nine months 2026: (509) + 548 = 39; with special items 33: 72.
- LTM Q3 2026 = FY2025 + nine months 2026 - nine months 2025. Operating loss: (368) + (509) - (268) = (609). D&A: 688 + 548 - 512 = 724. Special items: 30 + 33 - 29 = 34. EBITDA: (609) + 724 = 115; with special items: 115 + 34 = 149.
- Revenue LTM: 9,062 + 7,749 - 6,818 = 9,993. Net loss LTM: (602) + (823) - (425) = (1,000). Interest expense LTM: 588 + 440 - 441 = 587. Cash interest LTM: 427 + 372 - 306 = 493. Operating cash flow LTM: (94) + (273) - (143) = (224). Capex LTM: 1,078 + 575 - 742 = 911. Pre-delivery deposits LTM: 44 + 49 - 35 = 58.
- Discrete quarters, EBITDA excluding special items: Q1 2026 (224) + 179 = (45); Q2 2026 (141) + 183 = 42; Q3 2026 (144) + 186 + 33 = 75; sum 72, equal to nine months 2026. 2025: Q1 (174) + 168 = (6); Q2 6 + 171 + 24 = 201; Q3 (100) + 173 + 5 = 78; sum 273, equal to nine months 2025 (prior-year quarters from the comparative columns of the same 10-Qs).

### Free cash flow

- Operating cash flow less capital expenditures less pre-delivery deposits. FY2024: 144 - 1,478 - 141 = (1,475). FY2025: (94) - 1,078 - 44 = (1,216). Nine months 2025: (143) - 742 - 35 = (920). Nine months 2026: (273) - 575 - 49 = (897). LTM: (224) - 911 - 58 = (1,193), equal to (1,216) + (897) - (920).

### Net debt and liquidity

- Unrestricted cash, equivalents and investment securities. December 31, 2024: 1,921 + 1,689 + 336 = 3,946. December 31, 2025: 1,946 + 213 + 318 = 2,477. September 30, 2026: 1,258 + 251 + 117 = 1,626.
- Net debt = carrying debt less that sum. December 31, 2024: 8,539 - 3,946 = 4,593. December 31, 2025: 8,498 - 2,477 = 6,021. September 30, 2026: 8,393 - 1,626 = 6,767. Change in net debt, December 31, 2025 to September 30, 2026: 6,767 - 6,021 = 746.
- Liquidity = cash above plus undrawn Citibank revolver of 600. December 31, 2025: 2,477 + 600 = 3,077. September 30, 2026: 1,626 + 600 = 2,226. Change in unrestricted cash and investments: 1,626 - 2,477 = (851).
- Restricted cash at September 30, 2026: 9 + 255 = 264, equal to the 264 stated on page:18.

### Ratios (rounded to two decimals)

- Total debt / EBITDA excluding special items: FY2024 8,539 / 562 = 15.19; FY2025 8,498 / 350 = 24.28; LTM 8,393 / 149 = 56.33.
- Net debt / EBITDA excluding special items: FY2024 4,593 / 562 = 8.17; FY2025 6,021 / 350 = 17.20; LTM 6,767 / 149 = 45.42.
- EBITDA excluding special items / cash interest: FY2024 562 / 230 = 2.44; FY2025 350 / 427 = 0.82; nine months 2025 273 / 306 = 0.89; nine months 2026 72 / 372 = 0.19; LTM 149 / 493 = 0.30.
- Unadjusted LTM: 8,393 / 115 = 72.98 and 6,767 / 115 = 58.84; cover 115 / 493 = 0.23.
- Q3 2026 year-on-year changes: revenue 2,812 - 2,322 = 490; fuel 868 - 539 = 329; salaries 946 - 865 = 81; total operating expenses 2,956 - 2,422 = 534.
- Maturity shares of 8,393: 2029 1,835 is 21.9 percent; thereafter 4,691 is 55.9 percent; remainder of 2026 plus 2027 is 152 + 477 = 629.

## Gaps

| Gap | Severity | Affected | Remediation |
| --- | --- | --- | --- |
| The issuer reports no EBITDA; all leverage and cover ratios use a computed definition | Medium | Leverage and cover metrics | Compare with any lender or rating-agency EBITDA definition when supplied |
| Covenant levels, step-downs and reported ratios for the TrueBlue financings and Citibank revolver are not printed | High | Covenant headroom | Supply the credit agreements and compliance certificates |
| Executed debt agreements and guarantor identities not supplied | High | Debt terms, guarantor perimeter | Supply the TrueBlue indenture, term loan and Citibank agreement |
| Rates are as of December 31, 2025; the 2026 equipment notes are described only as Treasury plus a margin | Low | Cost of debt | Supply the April 14, 2026 financing documents |
| No balance sheet at September 30, 2025, so nine-month 2025 leverage is not supplied | Low | Prior-year comparison | Use the Q3 2025 10-Q if a quarterly series is needed |
| Cash interest is net of interest income; gross cash interest is not supplied | Medium | Interest cover | Supply a gross cash interest figure or derive from the debt schedule |
| Management's unencumbered asset claim of about $7 billion is not reconciled to the filing | Medium | Collateral and secondary liquidity | Obtain the asset appraisal basis |
| Extraction is text only; tables flattened; no XBRL | Low | All figures | Spot-check key figures against the filed HTML |
| Events from October 27, 2026 to 2026-11-05 not supplied | Medium | Subsequent events | Supply later filings or confirm none |

## Next module

CP-1A (company and transaction profile) follows, then CP-2 (credit analysis) and CP-5. CP-2 should treat covenant headroom, the 2029 maturity concentration and the secured-versus-unsecured claim structure as its first open items, and should keep the EBITDA definition used here or state its own.
