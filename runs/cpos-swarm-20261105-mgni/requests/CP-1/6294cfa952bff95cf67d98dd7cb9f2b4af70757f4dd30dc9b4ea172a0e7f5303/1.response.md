# Financial base: MAGNITE, INC. (mgni)

## Request

- Issuer: MAGNITE, INC. (issuer id mgni), as-of date 2026-11-05, information cutoff 2026-11-05. Reporting entity is the consolidated Magnite, Inc. and subsidiaries, which is also the credit-agreement borrower group described in the filings. Reporting currency USD. The statements print thousands of USD; the MD&A and releases print millions. Tables below say which unit they use.
- Scope: financial base for the credit snapshot: reported FY2024, FY2025, nine months 2026 and 2025, the discrete 2026 quarters, and LTM at September 30, 2026; leverage, cover, liquidity and maturity chart data; definition risks. Current period Q3 2026, prior period FY2025 (context).
- Execution: host session reading the pinned text files; no provider call. Locators `key pN` are the source chunk `page:N`; keys are in Sources. Quotes are exact substrings of the located chunk.
- Perimeter statement: all figures are consolidated Magnite, Inc. There is no subsidiary issuer, so no parent-versus-issuer split arises.

## Sources

| Key | Source (exact name) | sha256 (pinned file) | Used for |
| --- | --- | --- | --- |
| 10K | 10-K_2025-12-31_mgni-20251231.htm.jsonl | f96c3c8e001359e3762f2fdcdb5fec62dc8b34a692251ca50bc2b0320cbc2a0a | Audited FY2025 and FY2024 statements, debt note, Adjusted EBITDA reconciliation |
| Q1Q | 10-Q_2026-03-31_mgni-20260331.htm.jsonl | a236956e4f58c23dd0c7e9814923ff8c58122f0f2ffc4593ab7dcd2ac0165adf | Q1 2026 statements, debt table, revolver availability |
| Q2Q | 10-Q_2026-06-30_mgni-20260630.htm.jsonl | 796b488acb30e088707602178e4e306b131923e994381f8d88dd91dd9706c3bb | Q2 and six months 2026 statements, debt table |
| Q3Q | 10-Q_2026-09-30_mgni-20260930.htm.jsonl | c6922a9ebeac839059c55928b8190f39ac8376ff2e5306b6695aa910a9515bb4 | Q3 and nine months 2026 statements, debt, liquidity, subsequent event |
| ER1 | EX-99.1_2026-05-06_a991-earningsq12026.htm.jsonl | 1a65026a829ea6d3398cf84619845f6c5e542133314c7959aef5563816dda9a4 | Q1 2026 Adjusted EBITDA with Q1 2025 comparative |
| ER2 | EX-99.1_2026-08-05_a991-earningsq22026.htm.jsonl | 7a22ad7a167049f41876318b3adec058b3521559a35265d5009853f0eba7f49d | Q2 and six months Adjusted EBITDA with 2025 comparatives |
| ER3 | EX-99.1_2026-11-04_a991-earningsq32026.htm.jsonl | 9404d81beccd30783613c5d17e44e7f768a511dbf6b00a1825d39fa611f52e22 | Q3 and nine months Adjusted EBITDA reconciliation, guidance, measure definitions |
| context | context (run settings; not issuer evidence) | add9e4e5fe29cabeba543552138279256276897be557a9b8ceef018e156869fc | Dates, currency, periods |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 3b5491ad4792081e28ccae80a3f58279ef4978af29432bbcc0ff2472969d5e7a | Source readiness: all consumers READY_WITH_LIMITATIONS; credit agreement not supplied; Q4 2025 not separately reported; releases define operating cash flow differently from the cash flow statement. Carried into Gaps below. |

This answer does not correct the CP-0 handoff. It adds locators for the Q1 and Q2 2026 statements, which CP-0 assessed only at the register level.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Magnite is lightly levered on issuer-defined Adjusted EBITDA: gross debt of $357,730 thousand is 1.27x last-twelve-months EBITDA, and cash exceeds debt. Cash may be flattered by working-capital timing. | Medium | Adjusted EBITDA adds back stock compensation; the credit agreement and covenant definitions are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Only the term loan remains; the convertible notes were repaid in March 2026, cutting principal from $565,521 thousand to $359,546 thousand. | Refinancing risk is back-ended: most principal falls due after 2030. | High |
| Adjusted EBITDA rose from $232,131 thousand in FY2025 to $280,586 thousand over the last twelve months, while income from operations plus depreciation gives a lower base. | Leverage is 1.27x on the company measure and 1.81x after stock compensation. | Medium |
| Cash of $392,862 thousand sits beside payables of $1,738,299 thousand, and first-quarter operating cash flow was negative. | Net cash is not permanent excess liquidity; use it with the seasonal swing in mind. | Medium |
| The October 2026 repricing lowers the term loan margin to 2.50% and is a subsequent event not in September balances. | Interest cost falls modestly; the leverage covenant was not triggered at quarter end because the revolver was undrawn. | Medium |

### Financial base view

On the supplied filings, Magnite's financial base is strong and simple. Debt is a single secured term loan with principal of $357,730 thousand at September 30, 2026, an undrawn $175.0 million revolver and cash of $392,862 thousand. On the issuer's Adjusted EBITDA, which adds back stock-based compensation, gross leverage is 1.27x and net leverage is -0.13x on the last twelve months to September 30, 2026, down from 2.89x and 0.43x at FY2024, and cash-paid-interest cover is 10.98x. On a stricter base of income from operations plus depreciation and amortization (which carries stock compensation as an expense), gross leverage is 1.81x. Operating momentum is strong: Contribution ex-TAC for nine months 2026 is $551,127 thousand against $474,583 thousand, and CTV is the growth driver. The main qualifications are that cash is partly working-capital float (payables of $1,738,299 thousand against cash of $392,862 thousand) and swung from $553,362 thousand at FY2025 to $184,648 thousand at Q1 2026 before recovering, that FY2025 net income of $144,613 thousand includes a one-off income tax benefit of $73,986 thousand, and that covenant terms rest on the filings' description, not the credit agreement.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 2.89 | 0.43 | x | Debt principal 363,177 term loan plus 205,067 convertible notes (10K p148); cash 483,220 (10K p119); EBITDA is issuer Adjusted EBITDA 196,850 (10K p100). Adjusted EBITDA adds back stock compensation. |
| FY2025 | 2.44 | 0.05 | x | Principal 565,521 (10K p148); cash 553,362 (10K p119); Adjusted EBITDA 232,131 (10K p100). Convertible notes still outstanding at year end. |
| LTM Q1 2026 | 1.51 | 0.73 | x | Principal 359,546 (Q1Q p15); cash 184,648 (Q1Q p2); LTM Adjusted EBITDA 238,192 derived from FY2025 plus Q1 2026 less Q1 2025. Cash depressed by the March 2026 note repayment and seasonal working capital. |
| LTM Q2 2026 | 1.41 | 0.10 | x | Principal 358,638 (Q2Q p15); cash 332,615 (Q2Q p2); LTM Adjusted EBITDA 254,401 derived. |
| LTM Q3 2026 | 1.27 | -0.13 | x | Principal 357,730 (Q3Q p17); cash 392,862 (Q3Q p2); LTM Adjusted EBITDA 280,586 derived. Negative net leverage means cash exceeds debt. Debt excludes lease liabilities and uses principal, not carrying value. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 5.34 | x | Adjusted EBITDA 196,850 over cash paid for interest 36,863 (10K p122). |
| FY2025 | 8.24 | x | Adjusted EBITDA 232,131 over cash paid for interest 28,159 (10K p122). |
| LTM Q1 2026 | 8.58 | x | LTM Adjusted EBITDA 238,192 over LTM cash interest 27,768 (FY2025 plus Q1 2026 6,288 less Q1 2025 6,679; Q1Q p5). |
| LTM Q2 2026 | 9.56 | x | LTM Adjusted EBITDA 254,401 over LTM cash interest 26,615 (six-month cash interest 12,933 and 14,477; Q2Q p5). |
| LTM Q3 2026 | 10.98 | x | LTM Adjusted EBITDA 280,586 over LTM cash interest 25,549 (nine-month cash interest 19,064 and 21,674; Q3Q p6). Interest paid on the repaid convertible notes is small; the October 2026 repricing is not reflected. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 483.2 | 169.8 | US$m | Cash 483,220 thousand (10K p119). Undrawn is derived: $175.0 million revolver commitment less $5.2 million of office-lease letters of credit (10K p158); FY2024 availability is not printed in a supplied source. |
| FY2025 | 553.4 | 171.0 | US$m | Cash 553,362 thousand (10K p119); availability printed as $171.0 million net of $4.0 million letters of credit (10K p154). |
| Q1 2026 | 184.6 | 170.9 | US$m | Cash 184,648 thousand (Q1Q p2); availability $170.9 million (Q1Q p18). Cash is after repaying the convertible notes on March 15, 2026. |
| Q2 2026 | 332.6 | 170.9 | US$m | Cash 332,615 thousand (Q2Q p2); availability $170.9 million (Q2Q p18); a $60.0 million draw was made and repaid in the quarter. |
| Q3 2026 | 392.9 | 170.9 | US$m | Cash 392,862 thousand (Q3Q p2) including $78.1 million in foreign-currency accounts (Q3Q p50); availability $170.9 million net of $4.1 million letters of credit (Q3Q p20). Revolver matures February 2029; cash is partly customer-related working capital. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remaining 2026 | 0.908 | US$m | Principal of the 2024 Term Loan B at September 30, 2026 (Q3Q p17); scheduled amortization only. |
| 2027 | 3.632 | US$m | Scheduled 1% annual amortization (Q3Q p17, p20). Excess cash flow prepayment not required for the period (Q3Q p20). |
| 2028 | 3.632 | US$m | Same basis (Q3Q p17). |
| 2029 | 3.632 | US$m | Same basis; the undrawn revolver matures February 2029 (Q3Q p19) and is not in this schedule. |
| 2030 | 3.632 | US$m | Same basis (Q3Q p17). |
| Thereafter | 342.294 | US$m | Includes the February 2031 maturity of the term loan (Q3Q p19). Schedule totals 357.730, equal to principal outstanding. |

### Financials and credit metrics

| Metric (US$ thousands unless stated) | FY2024 | FY2025 | 9M 2025 | 9M 2026 | LTM Q3 2026 | Source and basis |
| --- | --- | --- | --- | --- | --- | --- |
| Revenue | 668,170 | 713,953 | 508,597 | 561,390 | 766,746 | 10K p120; Q3Q p3; LTM derived |
| Contribution ex-TAC (non-GAAP) | 606,942 | 669,633 | 474,583 | 551,127 | 746,177 | 10K p97; Q3Q p45; LTM derived |
| Gross profit | 409,332 | 447,334 | 311,489 | 374,928 | 510,773 | 10K p97; Q3Q p45; LTM derived |
| Income from operations | 51,087 | 97,601 | 45,636 | 89,481 | 141,446 | 10K p120; Q3Q p3; LTM derived |
| Depreciation and amortization | 58,510 | 53,674 | 40,119 | 42,866 | 56,421 | Cash flow statements 10K p121; Q3Q p5; LTM derived |
| Stock-based compensation | 76,519 | 76,648 | 58,811 | 55,805 | 73,642 | 10K p121; Q3Q p5; LTM derived |
| Adjusted EBITDA (issuer non-GAAP) | 196,850 | 232,131 | 148,362 | 196,817 | 280,586 | 10K p100; ER3 p13; LTM derived |
| Income from operations plus D&A | 109,597 | 151,275 | 85,755 | 132,347 | 197,867 | Derived; carries stock compensation as an expense |
| Net income | 22,786 | 144,613 | 21,563 | 57,786 | 180,836 | 10K p120; Q3Q p3; FY2025 includes tax benefit 73,986 |
| Interest expense, net | 27,032 | 18,923 | 14,916 | 15,689 | 19,696 | 10K p120; Q3Q p3; LTM derived |
| Cash paid for interest | 36,863 | 28,159 | 21,674 | 19,064 | 25,549 | 10K p122; Q3Q p6; LTM derived |
| Cash paid for income taxes | 3,870 | 3,760 | 2,836 | 5,409 | 6,333 | 10K p122; Q3Q p6; LTM derived |
| Net cash provided by operating activities | 235,201 | 236,168 | 107,711 | 168,752 | 297,209 | 10K p121; Q3Q p5; includes working-capital swings |
| Capex: property and equipment plus capitalized software | 47,070 | 84,303 | 55,279 | 44,101 | 73,125 | 10K p121; Q3Q p5; LTM derived |
| Operating cash flow less capex | 188,131 | 151,865 | 52,432 | 124,651 | 224,084 | Derived; not a company-defined free cash flow |
| Cash and cash equivalents (period end) | 483,220 | 553,362 | Not supplied: no September 30, 2025 balance sheet | 392,862 | 392,862 | 10K p119; Q3Q p2 |
| Debt principal (period end) | 568,244 | 565,521 | Not supplied: no September 30, 2025 balance sheet | 357,730 | 357,730 | 10K p148; Q3Q p17 |
| Net debt (principal less cash) | 85,024 | 12,159 | Not supplied: same reason | -35,132 | -35,132 | Derived |
| Total debt / Adjusted EBITDA (x) | 2.89 | 2.44 | Not calculable: nine-month flow | Not calculable: nine-month flow | 1.27 | Derived |
| Net debt / Adjusted EBITDA (x) | 0.43 | 0.05 | Not calculable: nine-month flow | Not calculable: nine-month flow | -0.13 | Derived |
| Total debt / (income from operations plus D&A) (x) | 5.18 | 3.74 | Not calculable: nine-month flow | Not calculable: nine-month flow | 1.81 | Derived |
| Adjusted EBITDA / cash paid for interest (x) | 5.34 | 8.24 | 6.85 | 10.32 | 10.98 | Derived |
| Adjusted EBITDA / Contribution ex-TAC | 32.4% | 34.7% | 31.3% | 35.7% | 37.6% | Derived; the issuer quotes its margin on this base (ER3 p2) |

### Reported facts by period

#### Discrete 2026 quarters (US$ thousands)

| Item | Q1 2026 | Q2 2026 | Q3 2026 | Source |
| --- | --- | --- | --- | --- |
| Revenue | 164,371 | 192,823 | 204,196 | Q1Q p3; Q2Q p3; Q3Q p3 |
| Income from operations | 7,719 | 31,222 | 50,540 | Q1Q p3; Q2Q p3; Q3Q p3 |
| Net income | 4,412 | 19,369 | 34,005 | Q1Q p3; Q2Q p3; Q3Q p3 |
| Adjusted EBITDA | 42,861 | 70,600 | 83,356 | ER1 p11; ER2 p12; ER3 p13 |
| Cash and cash equivalents at quarter end | 184,648 | 332,615 | 392,862 | Q1Q p2; Q2Q p2; Q3Q p2 |

Revenue of the three quarters sums to 561,390, equal to the printed nine-month revenue. Adjusted EBITDA of the three quarters sums to 196,817, equal to the printed nine-month figure.

#### Contribution ex-TAC by channel

CTV Contribution ex-TAC was "CTV $ 304,192 $ 260,159 $ 218,494" for FY2025, FY2024 and FY2023 (10K p98) and "CTV $ 105,368 $ 75,847 39 % $ 284,770 $ 210,615 35 %" for Q3 and nine months (Q3Q p45). CTV is 284,770 of the nine-month total of 551,127. Filings group channels as CTV, Mobile and Desktop; the releases group CTV and DV+ (ER3 p1). The company reports one segment: "operates as one operating segment and one reportable segment" (Q3Q p8).

#### Capital structure at September 30, 2026

- Term loan: "2024 Term Loan B Facility $ 357,730 $ 360,454" (Q3Q p20), secured by substantially all assets, maturing February 2031, contractual rate "6.90%" at September 30, 2026 (Q3Q p19). Carrying value net of discount and issuance costs 349,950 (Q3Q p17).
- Revolver: $175.0 million, undrawn, matures February 2029; "amounts available under the 2024 Revolving Credit Facility were $170.9 million, net of letters of credit outstanding in the amount of $4.1 million" (Q3Q p20).
- Convertible notes: "On March 15, 2026, the Convertible Senior Notes matured" and "No Convertible Senior Notes remained outstanding" (Q3Q p14). Principal repaid 205,067 (cash flow, Q3Q p5).
- Claims outside the debt figure: lease liabilities current 21,558 and non-current 40,436 (Q3Q p2); non-cancelable cloud, software and data center obligations "Total $ 115,219" (Q3Q p22). No pension, factoring or off-balance-sheet financing is described in the sections read; none was found in a search for those terms (see Gaps).
- Covenant: springing First Lien Net Leverage Ratio below 3.25 to 1.00, tested only if revolver utilization exceeds 35% of commitments; no revolver amount outstanding at September 30, 2026 and the Company "was in compliance with its debt covenants" (Q3Q p20). No reported ratio is supplied.

#### Subsequent event

Amendment No. 3 dated October 7, 2026 lowered the term loan margin to Term SOFR plus 2.50% from 3.00% and the revolver margin range from 3.50% to 4.00% to 2.50% to 3.00% (Q3Q p29, p30). It post-dates the September 30, 2026 balance sheet and is not applied to any figure above.

### Definition risks and quality of earnings

- Adjusted EBITDA is the issuer's measure: "Other companies may calculate Adjusted EBITDA differently than we do" (10K p100). It adds back stock-based compensation (76,648 in FY2025; 55,805 in nine months 2026), which is a real cost to equity holders but not cash.
- The FY2025 bridge from income from operations to Adjusted EBITDA ties exactly: 97,601 plus D&A 53,674 plus stock compensation 76,648 gives 227,923, and the remaining 4,208 equals merger costs 162, litigation expense 1,116, non-operational real estate and other 890, other income 1,073 and other debt refinancing expense 967. The nine-month 2026 and 2025 bridges also tie (8,665 and 3,796). Other income is included in Adjusted EBITDA because the reconciliation does not deduct it.
- The releases define "Operating cash flow is calculated as Adjusted EBITDA less capital expenditures" (ER3 p2) and free cash flow as that less net interest expense. These are not the cash flow statement's "Net cash provided by operating activities". This answer uses the statement figure for cash flow and labels operating cash flow less capex as a derived measure.
- FY2025 net income of 144,613 includes a tax benefit: "Provision (benefit) for income taxes (73,986)" (10K p120) and deferred taxes of (78,230) in the cash flow statement (10K p121); the auditor's critical audit matters include "Income Taxes — Valuation Allowance Release" (10K p118) and the filing states federal valuation allowances were released (10K p72). Net income is therefore not a run-rate measure; cash taxes paid were 3,760.
- Litigation: Magnite sued Google on September 16, 2025; litigation expense is added back (ER3 p13: "Litigation expense (1) 1,999 527 3,815 1,043"). No recovery or liability is recorded or quantified (Q3Q p24).
- Seasonality and float: "expect these measures to be higher in the fourth quarter than in other quarters" (10K p29); first-quarter 2026 operating cash flow was negative ("net cash used in operating activities was $120.8 million", Q1Q p47). Accounts payable and accrued expenses of 1,738,299 exceed accounts receivable of 1,432,233 (Q3Q p2) because the company collects from buyers and pays publishers. Reported cash and net debt are sensitive to the date within the cycle.
- Guidance (management, attributed): Q4 2026 total Contribution ex-TAC "between $227 million and $233 million" (ER3 p1). It is a management expectation, not used in any ratio.

## Calculations

All inputs are printed figures in US$ thousands from the cited chunks. "LTM" means last twelve months to the stated quarter end, computed as FY2025 plus the 2026 year-to-date figure less the 2025 year-to-date figure.

1. LTM Adjusted EBITDA, Q3 2026: 232,131 (10K p100) + 196,817 (ER3 p13) - 148,362 (ER3 p13) = 280,586. Q2 2026: 232,131 + 113,461 (ER2 p12) - 91,191 (ER2 p12) = 254,401. Q1 2026: 232,131 + 42,861 (ER1 p11) - 36,800 (ER1 p11) = 238,192.
2. LTM cash paid for interest, Q3: 28,159 + 19,064 - 21,674 = 25,549. Q2: 28,159 + 12,933 - 14,477 = 26,615. Q1: 28,159 + 6,288 - 6,679 = 27,768.
3. Debt principal: FY2024 363,177 + 205,067 = 568,244; FY2025 360,454 + 205,067 = 565,521 (10K p148); March 359,546, June 358,638, September 357,730 (Q1Q p15, Q2Q p15, Q3Q p17).
4. Net debt = principal - cash: FY2024 568,244 - 483,220 = 85,024; FY2025 565,521 - 553,362 = 12,159; Q1 359,546 - 184,648 = 174,898; Q2 358,638 - 332,615 = 26,023; Q3 357,730 - 392,862 = -35,132.
5. Total debt / LTM Adjusted EBITDA: FY2024 568,244 / 196,850 = 2.89; FY2025 565,521 / 232,131 = 2.44; Q1 359,546 / 238,192 = 1.51; Q2 358,638 / 254,401 = 1.41; Q3 357,730 / 280,586 = 1.27. Net: 85,024 / 196,850 = 0.43; 12,159 / 232,131 = 0.05; 174,898 / 238,192 = 0.73; 26,023 / 254,401 = 0.10; -35,132 / 280,586 = -0.13.
6. Cover: 196,850 / 36,863 = 5.34; 232,131 / 28,159 = 8.24; 238,192 / 27,768 = 8.58; 254,401 / 26,615 = 9.56; 280,586 / 25,549 = 10.98; nine months 2025 148,362 / 21,674 = 6.85; nine months 2026 196,817 / 19,064 = 10.32.
7. Stricter base: LTM income from operations 97,601 + 89,481 - 45,636 = 141,446; LTM D&A 53,674 + 42,866 - 40,119 = 56,421; sum 197,867; 357,730 / 197,867 = 1.81. FY2025 base 97,601 + 53,674 = 151,275; 565,521 / 151,275 = 3.74. FY2024 base 51,087 + 58,510 = 109,597; 568,244 / 109,597 = 5.18.
8. Capex: FY2025 70,535 + 13,768 = 84,303; nine months 2026 31,444 + 12,657 = 44,101; nine months 2025 45,131 + 10,148 = 55,279; FY2024 32,810 + 14,260 = 47,070; LTM 84,303 + 44,101 - 55,279 = 73,125. LTM operating cash flow 236,168 + 168,752 - 107,711 = 297,209; less capex 224,084.
9. Other LTM: revenue 713,953 + 561,390 - 508,597 = 766,746; Contribution ex-TAC 669,633 + 551,127 - 474,583 = 746,177; gross profit 447,334 + 374,928 - 311,489 = 510,773; stock compensation 76,648 + 55,805 - 58,811 = 73,642; net income 144,613 + 57,786 - 21,563 = 180,836; interest expense, net 18,923 + 15,689 - 14,916 = 19,696; cash taxes 3,760 + 5,409 - 2,836 = 6,333. Margin: 280,586 / 746,177 = 37.6%.
10. Undrawn FY2024 (derived): $175.0 million less $5.2 million = $169.8 million. Liquidity in the chart is cash plus undrawn facilities shown separately; it is not netted for the minimum cash needed to run the platform.
11. Illustrative effect of Amendment No. 3 (not a company figure): 357,730 x 0.50% = 1,789 per year on the September 30, 2026 principal, before changes in Term SOFR.

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Credit agreement, amendments and covenant definitions are Not supplied. The First Lien Net Leverage Ratio as defined, and any reported figure or headroom, are Not supplied. | Covenant headroom is Not calculable. The test applies only if revolver utilization exceeds 35%; none was drawn at September 30, 2026. | Retrieve the exhibits listed in the 10-K exhibit index (10K p179 to p182) if headroom matters. |
| Discrete Q4 2025 is not reported in a supplied source. | The Q4 2025 Adjusted EBITDA of 83,769 can be derived as 232,131 less 148,362, but no source states it. | Label as derived if used. |
| Balance sheet at September 30, 2025 and June or March 2025 are Not supplied. | Net debt and leverage for the 2025 nine-month column are Not calculable. | Use the LTM columns instead. |
| FY2024 revolver availability is not printed. | The FY2024 liquidity figure is derived from the commitment and the letters of credit. | Marked as derived. |
| Pension, factoring and supply-chain finance: no search hit for these terms in the debt and liquidity sections read; not an exhaustive search of every chunk. | Treated as none identified, not zero. | Confirm in downstream review. |
| Tables are flattened text; no XBRL. | Figures should be re-read against the cited chunk. | Done for figures used here. |
| Cash is not separated into operating cash and customer or publisher float; restricted cash is not shown separately on the face of the balance sheet. | Net cash overstates free cash in a seasonally weak quarter. | Treat liquidity as an upper bound. |
| Company free cash flow and guidance are management measures defined differently from the cash flow statement. | Not used in ratios. | Cross-check against the statement before use. |

## Next module

Proceed to CP-1A (business, structure and transactions), then CP-2 (capital structure, liquidity and covenants) and CP-5 (evidence review). Carry forward: the single-term-loan capital structure with principal of $357,730 thousand; the 1.27x and 1.81x leverage readings and their definitions; the cash-float and seasonality qualification; the one-off FY2025 tax benefit; the October 7, 2026 Amendment No. 3 as a subsequent event; and the absence of the credit agreement. CP-2 should recompute headroom only if the covenant definition is obtained.
