# CP-1 Financial base for TripAdvisor, Inc. (trip), as of 2026-11-05

## Request

Issuer: TripAdvisor, Inc. (ticker TRIP), a single reporting entity whose consolidated statements are the only statements supplied. As-of date and evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, in millions unless a cell says otherwise; the 10-K prints whole millions and the 10-Qs and releases print one decimal. Current period: Q3 2026 (quarter ended September 30, 2026). Prior period: FY2025.

Scope of this handoff: the reported financial base a committee needs first, namely revenue and segment earnings, Adjusted EBITDA, cash flow, debt and liquidity, leverage and interest cover, with every figure labelled by period and perimeter, and with the report selector tables for leverage, interest cover, liquidity and debt maturities. It gives no ratings view, valuation or recommendation. Perimeter rule carried from the readiness handoff: figures are on the continuing-operations perimeter (TheFork discontinued) unless a cell says otherwise.

Locator convention: `Q3 10-Q page:N` means extraction chunk N of the Q3 2026 Form 10-Q (not the printed page); likewise `Q1 10-Q`, `Q2 10-Q`, `10-K`, and `Q1 PR`, `Q2 PR`, `Q3 PR` for the three Exhibit 99.1 earnings releases.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_trip-20251231.htm.jsonl | 8885b42791d5e90823a0c9c46491e45285d32d010f68b9715cb0b383be7e31bf | Audited FY2025 statements on the old perimeter (TheFork included), debt terms, covenant level, contractual obligations (whole USD millions) |
| 10-Q_2026-03-31_trip-20260331.htm.jsonl | 9289cc81c4291efc67a199ffd3d95096f8d91f0c627c0d49a15ca4c0525a91f8 | Q1 2026 balance sheet, cash interest, debt (old perimeter, TheFork included) |
| 10-Q_2026-06-30_trip-20260630.htm.jsonl | 358dea410a455694571e6fd8ed4ffb768fc6929fddacda37801383944ce9f7e1 | Q2 2026 and six-month continuing statements, balance sheet, cash interest, debt |
| 10-Q_2026-09-30_trip-20260930.htm.jsonl | 37e12b49f799525884b2d1c8f8223439d80dbaee990e3c8305474f0abf40c5c7 | Latest balance sheet, Q3 and nine-month continuing statements, cash flows, debt, liquidity, goodwill, subsequent events |
| EX-99.1_2026-05-07_trip-ex99_1.htm.jsonl | 986da54f4628e6ef7caa0f060a29736fbe7ef71884de15f953b1b79776621916 | Q1 release; read for context only, old perimeter |
| EX-99.1_2026-08-06_trip-ex99_1.htm.jsonl | 4b5f625f62e6af22d7ff5c0ad78ab3c67f22ed4bd26c03b70a227ec22f7f24b0 | Q2 release; read for perimeter change and Q2 continuing figures |
| EX-99.1_2026-11-05_trip-ex99_1.htm.jsonl | 08c99d197b1e28c92053c736e4c07c927f197a67f49f8aceaed0f5db801c0a1c | Quarterly continuing-operations series for 2025 and 2026 (page:12-16), the source of every Q4 2025 and FY2025 continuing figure and of the LTM build |

### Run context (not issuer evidence)

| Source | sha256 | Role |
| --- | --- | --- |
| context (1526520-tripadvisor-inc-trip.json) | 1fa2d7822828d80dbe527b9dde9239ab274e8339a7a989f9acc6255a06577c7a | Run dates, currency, pathway; contains no issuer figures |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 11450ae719794e17a2469c6eb5fd603263c2713efb400c29bf944a61ffe15423 | Source readiness: perimeter break, authority ranking, gap register. Opened and applied: every figure below carries its perimeter, the LTM build uses the Q3 release series at management-release authority as CP-0 directed, and the covenant ratio is not invented. |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Earnings fell sharply: LTM Adjusted EBITDA is 207.3, so gross leverage on the 833.9 term loan is 4.02x. Cash of 706.8 and an undrawn revolver give liquidity, though much cash is matched by operator payables. | Medium | Adjusted EBITDA is a management non-GAAP measure, the annual continuing base rests on a release, and neither the covenant ratio nor the credit agreement is supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Q3 2026 Adjusted EBITDA was 71.1 against 107.8 a year earlier, and LTM Adjusted EBITDA of 207.3 compares with 294.7 for FY2025. | Debt repayment only offset the earnings decline, leaving gross leverage unchanged from year end, so any further earnings decline raises leverage directly. | High |
| Hotels and Other produced 143.6 of the 207.3 LTM Adjusted EBITDA while its revenue fell, and it took a 369.5 goodwill impairment in Q3 2026. | Debt service leans on a shrinking segment while the growth segment earns little, so earnings quality is the central credit question. | Medium |
| Debt is one Term Loan B of 833.9 due 2031 plus an undrawn 500.0 revolver due 2028; the 345.0 convertible notes were repaid on April 1, 2026. | No maturity of size before 2031 and no financial covenant on the term loan, but the rate floats and the 10-K says it is unhedged. | High |
| Operating cash flow was -122.0 in Q3 2026 and LTM free cash flow is -17.5; cash of 706.8 sits beside 396.8 of deferred merchant payables. | Reported cash overstates freely usable cash, and seasonal outflows can absorb much of it in the second half. | Medium |
| The sale of TheFork closed after quarter end for about 741.0 of net cash, which no reported balance sheet includes. | Net debt could fall sharply, but only management intent, not a commitment, links the proceeds to debt reduction. | Medium |

### Financial base view

TripAdvisor, Inc. enters the fourth quarter of 2026 with a lower-earning but lower-debt capital structure than a year ago. On the continuing-operations perimeter, LTM Adjusted EBITDA is 207.3 against 294.7 for FY2025, driven by Hotels and Other, whose revenue fell 23% in Q3 2026, while Experiences revenue fell 3% in the same quarter after growing earlier in the year. Debt principal has fallen from 1,185 at December 31, 2025 to 833.9 at September 30, 2026 because the 345.0 convertible notes were repaid in cash on April 1, 2026, so gross debt to LTM Adjusted EBITDA is 4.02x, the same as at year end 2025 only because EBITDA and debt fell together. Net of 706.8 of cash the ratio is 0.61x, but 396.8 of deferred merchant payables, amounts owed to experience operators after travel, sit against that cash, and on a cash-less-float basis net leverage is 2.53x. Free cash flow is negative on an LTM basis, interest cover on cash interest is 3.50x LTM, and the term loan has no financial covenant while the revolver carries a leverage maximum whose reported level is not printed in the 2026 filings. The TheFork sale added about 741.0 of net cash on November 1, 2026, after the balance sheet date, so the reported figures understate the post-sale cash position. Every ratio below rests on management Adjusted EBITDA, which adds back stock-based compensation, so the ratios are better read as a ceiling on earnings capacity than as a covenant calculation.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 4.02 | 0.70 | x | Debt principal 1,185 at December 31, 2025 (10-K page:90) over continuing-operations Adjusted EBITDA of 294.7 for FY2025 (Q3 PR page:13); net debt uses continuing cash of 978.0 (Q3 10-Q page:3 comparative). Management non-GAAP EBITDA after stock-based compensation add-back; leases and deferred merchant payables excluded from debt. |
| LTM Q1 2026 | 4.47 | Not supplied: Q1 10-Q cash includes TheFork and continuing cash is not printed | x | Debt principal 1,183.1 at March 31, 2026 (Q1 10-Q page:43) over LTM Adjusted EBITDA of 264.8 built from Q2 2025 to Q1 2026 release quarters (Q3 PR page:13). Management non-GAAP basis, release authority for the quarters. |
| LTM Q2 2026 | 3.43 | -0.03 | x | Debt principal 836.0 at June 30, 2026 (Q2 10-Q page:55) over LTM Adjusted EBITDA of 244.0; net of continuing cash 843.2 (Q2 10-Q page:3). Same non-GAAP and release-authority limits; operator float sits against the cash. |
| LTM Q3 2026 | 4.02 | 0.61 | x | Debt principal 833.9 at September 30, 2026 (Q3 10-Q page:62) over LTM Adjusted EBITDA of 207.3 (Q4 2025 43.4 plus nine months 2026 163.9); net of continuing cash 706.8 (Q3 10-Q page:3). Sale proceeds received November 1, 2026 are excluded. Deferred merchant payables of 396.8 sit against the cash; net of that float the ratio is 2.53x. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 4.99 | x | Continuing Adjusted EBITDA 294.7 over cash paid for interest of 59 (10-K page:110, consolidated and in whole millions, so rounded). Perimeter mix: the cash interest line is not split for TheFork, which carries no debt in the held-for-sale detail. |
| LTM Q1 2026 | 4.22 | x | LTM Adjusted EBITDA 264.8 over LTM cash interest of 62.8 (FY2025 59 less Q1 2025 10.5 plus Q1 2026 14.3; Q1 10-Q page:5, 10-K page:110). Rounded FY input. |
| LTM Q2 2026 | 4.01 | x | LTM Adjusted EBITDA 244.0 over LTM cash interest of 60.8 (59 less six months 2025 26.8 plus six months 2026 28.6; Q2 10-Q page:6). Rounded FY input. |
| LTM Q3 2026 | 3.50 | x | LTM Adjusted EBITDA 207.3 over LTM cash interest of 59.2 (59 less nine months 2025 42.9 plus nine months 2026 43.1; Q3 10-Q page:7). Burdened by stock-based compensation add-back; after deducting LTM stock-based compensation of 70.2 the cover is 2.32x. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 978.0 | 496.4 | US$m | Continuing cash and cash equivalents at December 31, 2025 (Q3 10-Q page:3 comparative; consolidated cash incl. TheFork was 1,034.9). Revolver 500.0 less 3.6 of undrawn standby letters of credit (Q3 10-Q page:61). Deferred merchant payables owed to operators were 308.1. |
| Q1 2026 | 1,120.4 | 496.4 | US$m | Q1 10-Q page:3 cash on the old perimeter, so it includes TheFork cash that is not separately printed. Undrawn amount is 500.0 less 3.6 of letters of credit (Q1 10-Q page:43), derived not printed. Deferred merchant payables owed to operators were 405.7. |
| Q2 2026 | 843.2 | 496.4 | US$m | Continuing cash at June 30, 2026 (Q2 10-Q page:3). Undrawn amount is 500.0 less 3.6 of letters of credit (Q2 10-Q page:55), derived not printed. Deferred merchant payables owed to operators were 484.2. |
| Q3 2026 | 706.8 | 497.7 | US$m | Continuing cash at September 30, 2026 (Q3 10-Q page:3) and printed available borrowing capacity of 497.7 (Q3 10-Q page:61). Deferred merchant payables owed to operators were 396.8; 219.4 of cash is held outside the U.S. The roughly 741.0 sale proceeds arrived November 1, 2026 and are excluded. Revolver matures June 29, 2028. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q4 2026 | 2.1 | US$m | One quarterly Term Loan B installment of 0.25% of the original 850.0 (Q3 10-Q page:62 states the 1.00% annual schedule; 10-K page:163 states the original-principal basis). Derived, not a printed schedule. |
| 2027 | 8.5 | US$m | Four quarterly installments; the current portion of debt at September 30, 2026 is 8.5 (Q3 10-Q page:3). Derived. |
| 2028 | 8.5 | US$m | Term Loan B installments only. The 500.0 revolver matures June 29, 2028 but is undrawn, so no borrowings mature. Derived. |
| 2029 | 8.5 | US$m | Term Loan B installments only. Derived. |
| 2030 | 8.5 | US$m | Term Loan B installments only. Derived. |
| 2031 | 797.8 | US$m | Two installments of 2.1 plus the balance due July 8, 2031 (793.6); equals 833.9 principal less 36.1 of earlier installments. Consistent with the 10-K table at December 31, 2025 (9, 17, 17 and 797 over the periods shown, 10-K page:95). Excludes any voluntary prepayment from sale proceeds. |

### Financials and credit metrics

| Metric | Q3 2026 | Q3 2025 | 9M 2026 | 9M 2025 | LTM Q3 2026 | FY2025 | Unit | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue | 436.4 | 490.8 | 1,204.1 | 1,319.3 | 1,559.1 | 1,674.3 | US$m | Continuing. Q3 and 9M: Q3 10-Q page:2. FY2025 and Q4 2025 (355.0): Q3 PR page:14. LTM is Q4 2025 plus 9M 2026. |
| Experiences revenue | 284.8 | 294.3 | 731.3 | 720.6 | 935.0 | 924.4 | US$m | Q3 10-Q page:34 and page:47; FY2025 Q3 PR page:14. |
| Hotels and Other revenue | 151.6 | 196.5 | 472.8 | 598.7 | 624.1 | 749.9 | US$m | Q3 10-Q page:34; 9M 2025 is the sum of release quarters 196.7, 205.5 and 196.5 (Q3 PR page:14); FY2025 Q3 PR page:14. |
| Adjusted EBITDA (management, non-GAAP) | 71.1 | 107.8 | 163.9 | 251.3 | 207.3 | 294.7 | US$m | Continuing. Q3 10-Q page:47 and Q3 PR page:13 (quarterly series). Adds back stock-based compensation, restructuring, legal, transaction, impairment and non-recurring items. |
| Adjusted EBITDA margin | 16.3 | 22.0 | 13.6 | 19.0 | 13.3 | 17.6 | % | Calculated as Adjusted EBITDA over revenue; Q3 2026, Q3 2025 and FY2025 agree with the release margins (Q3 PR page:16). |
| Experiences Adjusted EBITDA | 38.2 | 52.4 | 49.4 | 75.8 | 63.7 | 90.2 | US$m | Q3 10-Q page:47; FY2025 Q3 PR page:16. Segment Adjusted EBITDA is after reallocated stranded costs (Q3 10-Q page:34). |
| Hotels and Other Adjusted EBITDA | 32.9 | 55.4 | 114.5 | 175.4 | 143.6 | 204.5 | US$m | Q3 10-Q page:34; 9M 2025 sums 60.6, 59.4 and 55.4 (Q3 PR page:16); FY2025 Q3 PR page:16. |
| Operating income (loss) | -336.7 | 63.1 | -321.6 | 115.7 | Not supplied: Q4 2025 continuing operating income not printed | Not supplied: FY2025 continuing operating income not printed | US$m | Q3 10-Q page:2. Q3 2026 includes the 369.5 goodwill impairment. The 10-K operating income of 80 includes TheFork and is not comparable. |
| Impairment of goodwill | 369.5 | — | 369.5 | — | 369.5 | — | US$m | Hotels and Other reporting unit, Q3 10-Q page:22. Nil in the other columns as printed. |
| Depreciation and amortization | 18.9 | 18.7 | 56.5 | 53.5 | 75.7 | 72.7 | US$m | Q3 10-Q page:2; FY2025 and Q4 2025 (19.2) Q3 PR page:12. |
| Stock-based compensation | 15.3 | 25.7 | 50.5 | 77.1 | 70.2 | 96.9 | US$m | Q3 10-Q page:2; FY2025 and Q4 2025 (19.7) Q3 PR page:12. |
| Interest expense | 15.3 | 17.5 | 46.1 | 46.5 | Not supplied: Q4 2025 continuing interest expense not printed | Not supplied: FY2025 continuing interest expense not printed | US$m | Q3 10-Q page:2. Mostly the Term Loan B (13.8 in Q3 2026 and 40.8 in 9M 2026, Q3 10-Q page:25). The 10-K shows 63 on the old perimeter. |
| Interest income | 5.8 | 10.3 | 18.8 | 30.3 | Not supplied: Q4 2025 continuing interest income not printed | Not supplied: FY2025 continuing interest income not printed | US$m | Q3 10-Q page:2; falls with lower rates and lower cash after the notes repayment (Q3 10-Q page:56). |
| Net income (loss) from continuing operations | -316.9 | 48.5 | -324.7 | 82.4 | -354.6 | 52.4 | US$m | Q3 10-Q page:2; FY2025 and Q4 2025 (-29.9) Q3 PR page:12. |
| Operating cash flow, continuing | -122.0 | 32.9 | 130.4 | 337.5 | 27.4 | 234.7 | US$m | 9M columns Q3 10-Q page:6; Q3 and FY2025 Q3 PR page:14; Q4 2025 is -103.0. The 9M 2025 release quarters sum to 337.7, 0.2 above the 10-Q. |
| Capital expenditures, continuing | 9.2 | 13.9 | 31.8 | 48.2 | 44.9 | 61.3 | US$m | Including capitalized website development. Q3 10-Q page:6 and Q3 PR page:14; Q4 2025 is 13.1. |
| Free cash flow, continuing (non-GAAP) | -131.2 | 19.0 | 98.6 | 289.3 | -17.5 | 173.4 | US$m | Operating cash flow less capital expenditures (Q3 PR page:14). 9M 2025 is calculated from the 10-Q figures 337.5 and 48.2; the release quarters sum to 289.5. |
| Cash paid for interest | 14.5 | 16.1 | 43.1 | 42.9 | 59.2 | 59 | US$m | Consolidated cash flow statement, not split for TheFork. Q3 10-Q page:7, Q2 10-Q page:6; FY2025 10-K page:110 in whole millions. Quarters are year-to-date differences. |
| Cash paid for income taxes, net | 4.3 | 4.8 | 8.7 | 20.3 | 17.4 | 29 | US$m | Consolidated. Q3 10-Q page:6, Q2 10-Q page:6; FY2025 10-K page:110 in whole millions. Quarters are year-to-date differences. |
| Total debt / LTM Adjusted EBITDA | — | — | — | — | 4.02 | 4.02 | x | Principal over Adjusted EBITDA; see the leverage table and Calculations. |
| Net debt / LTM Adjusted EBITDA | — | — | — | — | 0.61 | 0.70 | x | Net of continuing cash; 2.53x at September 30, 2026 net of deferred merchant payables. |
| Adjusted EBITDA / cash interest | 4.90 | 6.70 | 3.80 | 5.86 | 3.50 | 4.99 | x | Quarterly and nine-month columns are not annualized; Q3 columns use the year-to-date differences above. |

### Capital structure and claims outside debt

| Item | September 30, 2026 | December 31, 2025 | Treatment and locator |
| --- | --- | --- | --- |
| Term Loan B principal | 833.9 | 840.2 | Q3 10-Q page:20 and page:24. SOFR plus 2.75%, due July 8, 2031, 1.00% annual amortization, no financial covenants (Q3 10-Q page:62). Inside debt. |
| Term Loan B carrying value | 822.9 | 827.5 | Net of unamortized issuance costs of 11.0 and 12.7 (Q3 10-Q page:20). Balance sheet shows 8.5 current plus 814.4 long-term. Inside debt. |
| 0.25% Convertible 2026 Senior Notes | 0.0 | 345.0 | Repaid at maturity on April 1, 2026 for 345.4 including interest; capped calls expired unexercised (Q3 10-Q page:25-26). Inside debt at December 31, 2025. |
| Revolving Credit Facility drawn | 0.0 | 0.0 | 500.0 commitment, matures June 29, 2028, secured (Q3 10-Q page:62; 10-K page:161). Letters of credit issued under it: 2.3 and 3.6. |
| Finance lease obligations | 36.8 | 42.7 | Current 7.4 (Q3 10-Q page:23) plus 29.4 (page:3); December 7.1 plus 35.6. Headquarters lease in Needham to December 2030 (10-K page:96). Outside the debt figure. |
| Operating lease liabilities | 29.3 | 32.7 | Current 5.0 plus 24.3; December 5.3 plus 27.4 (Q3 10-Q page:3 and page:23). Outside the debt figure. |
| Deferred merchant payables | 396.8 | 308.1 | Amounts owed to experience operators; a working-capital liability that funds part of cash (Q3 10-Q page:3, page:64). Outside debt, but it reduces freely usable cash. |
| Purchase obligations | Not supplied: unchanged since the 10-K | 88 | 10-K page:95 shows 88 of which 43 within a year; the Q3 10-Q page:66 states no material changes. Outside debt. |
| Pensions, retiree medical, factoring, supply-chain finance | Not supplied: none found | Not supplied: none found | Searched the 10-K and Q3 10-Q for pension, retiree, factoring and supply chain finance; only a 401(k) plan and unrelated mentions were found. |
| Tax claims (HMRC and IRS) | Estimated 20.0 to 30.0 if HMRC prevails, excluding interest | 73 of unrecognized tax benefits including interest | Q3 10-Q page:27 and page:64; 10-K page:96 and page:171. Outside debt, a potential cash outflow. |
| Total stockholders' equity | 366.3 | 644.9 | Q3 10-Q page:4. Retained earnings turned to a deficit of 6.5 after the impairment. |
| Term Loan B fair value | 795.8 | 811.1 | Level 2 third-party pricing (Q3 10-Q page:20); the 10-K printed 821 for the same date (see conflicts). |

### Segment and earnings quality drivers

Hotels and Other revenue fell 23% in Q3 2026 and 21% over nine months, and its Adjusted EBITDA fell 41% in Q3 2026 against Q3 2025 (Q3 PR page:1 and page:14). Management attributes the decline to "the sustained acceleration of traffic acquisition headwinds negatively impacting this business due to the changes in the search landscape" (Q3 10-Q page:22), which reads as a structural rather than cyclical explanation (analyst reading). Experiences revenue fell 3% in Q3 2026 after growing 1% over nine months, with Adjusted EBITDA down 27% in Q3 2026; the 10-Q cites macro events, cancellations and search headwinds on the Tripadvisor point of sale (Q3 10-Q page:43 and page:49). Mechanism: the segment that supplies about 69% of LTM Adjusted EBITDA is the one in structural decline, and the growth segment's LTM margin is 6.8% against 23.0% for Hotels and Other, so group margin falls as mix shifts even before any further decline in Hotels and Other. Credit implication: debt capacity depends on how fast Hotels and Other earnings erode against how fast Experiences margin can expand; the November 4, 2026 restructuring plan (costs of approximately $15 million to $20 million, Q3 10-Q page:37) targets the cost base but management's claimed savings are a release-only statement (Q3 PR page:3) and are not carried here.

### Definition review

Adjusted EBITDA is defined in Q3 10-Q page:33 as net income from continuing operations plus taxes, other income and expense, depreciation and amortization, stock-based compensation, impairments, legal reserves and settlements, restructuring, transaction expenses and non-recurring items. Reported-basis bridge for nine months 2026, recomputed from printed lines: operating income of -321.6 plus depreciation and amortization of 56.5 plus the goodwill impairment of 369.5 gives 104.4; adding stock-based compensation 50.5, restructuring 7.8, legal reserves and other 1.9, transaction expenses 4.1 and deducting the 4.8 fraud recovery gives 163.9, which equals the reported figure (Q3 PR page:12-13; Q3 10-Q page:34-37). The Q3 2026 bridge is 51.7 plus 15.3, 0.9, 2.6 and 0.6 giving 71.1. Largest definitional sensitivity: stock-based compensation is an add-back of 70.2 over the LTM, so EBITDA after stock-based compensation is 137.1 and gross leverage on that basis is 6.08x. The Term Loan B has no financial covenant; the revolver covenant definition of total net leverage is not supplied, so none of the ratios here is the covenant ratio.

### Conflicts and unreconciled differences

| Item | Located values | Treatment |
| --- | --- | --- |
| Term Loan B fair value at December 31, 2025 | 821 in the 10-K (page:152, page:100) against 811.1 as the comparative in the Q3 10-Q (page:20). | Not reconciled. The later filing is used for the December 2025 comparative in the capital table; the difference does not enter any ratio. |
| Nine-month 2025 operating cash flow | 337.5 in the Q3 10-Q (page:6) against 337.7 as the sum of the three release quarters (Q3 PR page:14). | The 10-Q figure is used for the nine-month column and the release quarter for Q4 2025; the 0.2 difference flows into the LTM figure. |
| HMRC exposure range | 20.0 to 30.0 in the Q3 10-Q (page:27), described as intercompany financing deductions, against 25 to 35 in the 10-K (page:171), described as transfer pricing arrangements. | Latest filing used; the change in range and wording is unexplained in the pack. |
| Term loan interest rate at September 30, 2026 | 6.92% effective (Q3 10-Q page:25) against 6.65% (page:62), the latter not labelled. | Neither rate enters a ratio. |
| Perimeter of December 31, 2025 balance sheet | 10-K cash 1,035 and goodwill 844 against 978.0 and 724.2 in the Q3 10-Q recast comparative. | Continuing comparatives used throughout; 10-K figures cited only for debt, covenant and obligation tables. |

### Subsequent events

Per Q3 10-Q page:11, page:37 and Q3 PR page:2-3: the TheFork sale closed on November 1, 2026 with total net cash consideration of approximately 741.0 and an expected fourth-quarter gain of about 487.0, both subject to final adjustments; a Transition Services Agreement of up to 12 months began at closing; and a restructuring plan was started on November 4, 2026 with expected pre-tax costs of approximately $15 million to $20 million. Management "currently expects that the Company will prioritize reduction of its long-term debt" (Q3 10-Q page:65). None of these is in the September 30, 2026 balance sheet.

## Calculations

All inputs are printed in the cited locators. Amounts in USD millions. Results are rounded to the precision shown; ratios to two decimals.

### LTM Adjusted EBITDA, continuing operations

| Period | Formula and inputs | Result |
| --- | --- | --- |
| LTM Q3 2026 | Q4 2025 43.4 + Q1 2026 16.4 + Q2 2026 76.4 + Q3 2026 71.1 (equivalently FY2025 294.7 - 9M 2025 251.3 + 9M 2026 163.9) | 207.3 |
| LTM Q2 2026 | Q3 2025 107.8 + Q4 2025 43.4 + Q1 2026 16.4 + Q2 2026 76.4 | 244.0 |
| LTM Q1 2026 | Q2 2025 97.2 + Q3 2025 107.8 + Q4 2025 43.4 + Q1 2026 16.4 | 264.8 |
| FY2025 check | 46.3 + 97.2 + 107.8 + 43.4 | 294.7 |

Quarters from Q3 PR page:13. 9M 2026: 16.4 + 76.4 + 71.1 = 163.9, equal to Q3 10-Q page:47. 9M 2025: 46.3 + 97.2 + 107.8 = 251.3, equal to Q3 10-Q page:47.

### Debt, net debt and leverage

| Date | Debt principal | Cash | Net debt | Total debt / EBITDA | Net debt / EBITDA |
| --- | --- | --- | --- | --- | --- |
| December 31, 2025 | 1,185 (10-K page:90: 354 + 831; equals 345.0 + 840.2) | 978.0 | 207.0 | 1,185 / 294.7 = 4.02 | 207.0 / 294.7 = 0.70 |
| March 31, 2026 | 1,183.1 (353.5 + 829.6) | Not supplied | Not calculable | 1,183.1 / 264.8 = 4.47 | Not calculable |
| June 30, 2026 | 836.0 (8.5 + 827.5) | 843.2 | -7.2 | 836.0 / 244.0 = 3.43 | -7.2 / 244.0 = -0.03 |
| September 30, 2026 | 833.9 (8.5 + 825.4) | 706.8 | 127.1 | 833.9 / 207.3 = 4.02 | 127.1 / 207.3 = 0.61 |

Cash-less-float sensitivity at September 30, 2026: cash 706.8 less deferred merchant payables 396.8 = 310.0; net debt 833.9 - 310.0 = 523.9; 523.9 / 207.3 = 2.53x. At December 31, 2025: 978.0 - 308.1 = 669.9; 1,185 - 669.9 = 515.1; 515.1 / 294.7 = 1.75x. At June 30, 2026: 843.2 - 484.2 = 359.0; 836.0 - 359.0 = 477.0; 477.0 / 244.0 = 1.95x. Including finance leases (36.8) in debt at September 30, 2026: (833.9 + 36.8) / 207.3 = 4.20x. After stock-based compensation: LTM 207.3 - 70.2 = 137.1; 833.9 / 137.1 = 6.08x.

### Cash interest and cover

| Period | Cash interest formula | Result | EBITDA / cash interest |
| --- | --- | --- | --- |
| LTM Q3 2026 | FY2025 59 - 9M 2025 42.9 + 9M 2026 43.1 | 59.2 | 207.3 / 59.2 = 3.50 |
| LTM Q2 2026 | 59 - 6M 2025 26.8 + 6M 2026 28.6 | 60.8 | 244.0 / 60.8 = 4.01 |
| LTM Q1 2026 | 59 - Q1 2025 10.5 + Q1 2026 14.3 | 62.8 | 264.8 / 62.8 = 4.22 |
| FY2025 | printed 59 | 59 | 294.7 / 59 = 4.99 |
| Q3 2026 | 9M 2026 43.1 - 6M 2026 28.6 | 14.5 | 71.1 / 14.5 = 4.90 |
| Q3 2025 | 9M 2025 42.9 - 6M 2025 26.8 | 16.1 | 107.8 / 16.1 = 6.70 |
| 9M 2026 and 9M 2025 | 163.9 / 43.1; 251.3 / 42.9 | 3.80; 5.86 | not annualized |

After stock-based compensation, LTM: 137.1 / 59.2 = 2.32.

### Cash flow build

LTM operating cash flow: Q4 2025 -103.0 + 9M 2026 130.4 = 27.4. LTM capital expenditures: 13.1 + 31.8 = 44.9. LTM free cash flow: -116.1 + 98.6 = -17.5, equal to 27.4 - 44.9 = -17.5. FY2025 check: 234.7 - 61.3 = 173.4. 9M 2025 free cash flow: 337.5 - 48.2 = 289.3. LTM revenue: 355.0 + 1,204.1 = 1,559.1. LTM margin: 207.3 / 1,559.1 = 13.3%. LTM net income: -29.9 + -324.7 = -354.6. LTM depreciation and amortization: 19.2 + 56.5 = 75.7. LTM stock-based compensation: 19.7 + 50.5 = 70.2. LTM cash taxes: 29 - 20.3 + 8.7 = 17.4.

### Segment mix

LTM Hotels and Other Adjusted EBITDA: 29.1 + 114.5 = 143.6 of 207.3, which is 69.3%; Experiences 14.3 + 49.4 = 63.7, which is 30.7%. LTM segment margins: 143.6 / 624.1 = 23.0% (revenue 151.3 + 472.8 = 624.1); 63.7 / 935.0 = 6.8% (revenue 203.7 + 731.3 = 935.0). Year-on-year: Q3 2026 revenue 436.4 / 490.8 - 1 = -11.1%; Q3 Adjusted EBITDA 71.1 / 107.8 - 1 = -34.0%; nine-month revenue 1,204.1 / 1,319.3 - 1 = -8.7%; nine-month Adjusted EBITDA 163.9 / 251.3 - 1 = -34.8%.

### Liquidity and debt schedule

Liquidity at September 30, 2026: cash 706.8 + undrawn revolver 497.7 (500.0 - 2.3) = 1,204.5; less deferred merchant payables 396.8 = 807.7. At December 31, 2025: 978.0 + 496.4 = 1,474.4; less 308.1 = 1,166.3. Term Loan B at fair value: 795.8 / 833.9 = 95.4% of principal at September 30, 2026; 811.1 / 840.2 = 96.5% at December 31, 2025 (comparative as restated in the 10-Q). Maturity derivation: 833.9 principal; Q4 2026 installment 2.1; 2027 to 2030 installments 4 x 8.5 = 34.0; 2031 installments 4.2 before the July 8 balance; balance 833.9 - 2.1 - 34.0 - 4.2 = 793.6; 2031 total 4.2 + 793.6 = 797.8. Check: 2.1 + 34.0 + 797.8 = 833.9.

### Illustrative post-sale view (not a reported figure)

Principal 833.9 against cash of 706.8 plus net sale consideration of about 741.0 = 1,447.8 gives net cash of 613.9 (net debt -613.9; -613.9 / 207.3 = -2.96x). Net of operator float: 706.8 - 396.8 + 741.0 = 1,051.0; net debt -217.1. This ignores fourth-quarter seasonal operating cash outflow (Q4 2025 was -103.0), the $15 million to $20 million restructuring cost, any prepayment of debt and final purchase price adjustments, and is shown only to size the effect.

## Gaps

| Gap | Detail | Effect | Action |
| --- | --- | --- | --- |
| Covenant ratio and definition | Not supplied: the issuer's computed total net leverage ratio and the credit agreement definition. The 4.5 to 1.0 maximum appears in the 10-K (page:161) and applies solely to the revolver; the 2026 10-Qs state compliance only. Whether the test is springing is not stated in the pack. | Headroom is Not calculable. A proxy of 0.61x on Adjusted EBITDA is not the covenant ratio. | Obtain the Amended Credit Agreement. |
| Filed continuing base for FY2025 | Not supplied: FY2025 and Q4 2025 continuing operating income, interest expense and interest income, and a continuing cash flow statement. | LTM interest expense, LTM operating income and LTM interest cover on interest expense are Not calculable. Cash interest cover uses the consolidated cash paid figure. | Use cash interest as the denominator and label it consolidated. |
| Cash interest perimeter | The cash paid for interest line is consolidated and not split between continuing and discontinued operations. | The direction and size of any distortion are not known. | Note the label on every cover figure. |
| Continuing cash at March 31, 2026 | Q1 10-Q cash of 1,120.4 includes TheFork cash that is not printed. | Q1 net leverage is Not supplied. | None needed for the current view. |
| Seasonality of net debt | Second-half cash flows from experience bookings are typically negative (Q3 10-Q page:64) and Q4 2025 operating cash flow was -103.0. | Year-end net debt may differ from the September 30 figure. | Revisit with the next report. |
| Adjusted EBITDA quality | Stock-based compensation add-back of 70.2 (LTM) and a 4.8 fraud recovery deducted in Q1 2026 are management choices. | Ratios on Adjusted EBITDA overstate cash earnings capacity. | Show the after-stock-compensation sensitivity. |
| Post-sale position | Not supplied: any balance sheet after November 1, 2026, and any debt prepayment. | Net debt after the sale is illustrative only. | None until the next filing. |
| Ratings, market debt prices and guidance | Not supplied. Fair values of the term loan are Level 2 estimates, not quotes. | No market-implied or rating view. | None. |
| Extraction | Tables are flattened and were reopened by page for every figure; no fidelity review of the extraction itself. | Residual transcription risk. | CP-5 recomputes. |

## Next module

Proceed to CP-1A. Carry forward: the perimeter rule (continuing operations unless stated), the LTM Adjusted EBITDA of 207.3 and its non-GAAP and release-authority limits, Hotels and Other as the earnings core and the impaired reporting unit, the after-quarter-end sale and restructuring events as subsequent events, the single Term Loan B due 2031 with no financial covenant and the unsupplied revolver covenant ratio, and the differences logged above. CP-2 and CP-5 should treat the post-sale figures as illustrative, never as reported.
