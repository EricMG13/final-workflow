## Request

Module: financial base, debt and liquidity extraction for Hilton Grand Vacations Inc. (ticker HGV), as of 2026-11-05, evidence cutoff 2026-11-05. Pathway: credit snapshot. Reporting currency: USD, USD millions unless a figure says otherwise. Current period: Q3 2026 (quarter and nine months ended September 30, 2026), with a trailing twelve months (LTM) view to September 30, 2026; prior period: FY2025 (year ended December 31, 2025). All figures are the consolidated registrant, US GAAP. No other currency or fiscal calendar is reported.

Perimeter used for leverage: corporate (recourse) debt of the consolidated group. Non-recourse timeshare receivable debt is reported separately in the filings and is shown separately here; it is not in the corporate debt figure unless a row says so. The issuer for this run is the listed parent Hilton Grand Vacations Inc.; the filings are not a combined filing of a parent and a separate subsidiary issuer, but the borrower and note issuers named in the exhibit index (for example Hilton Grand Vacations Borrower LLC) have no separate statements in the pack, so the parent's consolidated statements are the only perimeter available.

This module extracts and calculates; it gives no recommendation. The upstream handoff (source readiness) states which limitations apply and they are carried below.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Use in this module |
| --- | --- | --- |
| 10-K_2025-12-31_hgv-20251231.htm.jsonl | 17ffd5299d1ce58eaab3023314cb336b0628a563fbd9844c59917a6e453a02cf | FY2025 statements, debt note, cash interest, Adjusted EBITDA reconciliation |
| 10-Q_2026-03-31_hgv-20260331.htm.jsonl | 8a81895fada4586d8ccd4cb859be2d1886b42ac41a8aafdb19a05d432443584d | Q1 2026 comparison only; not used for a figure in the tables below |
| 10-Q_2026-06-30_hgv-20260630.htm.jsonl | a81efeb9cd748af0032df304e54e9f41941d57f53ef97a5d684972a6e7db8177 | Q2 2026 debt table and Term Loan B refinancing disclosure |
| 10-Q_2026-09-30_hgv-20260930.htm.jsonl | c993d04f6645ba40daf4556f4dc20114eff181da866b29f116f9cba49f88abad | Q3 2026 statements, debt and non-recourse notes, maturities, liquidity, commitments |
| EX-99.1_2026-04-30_hgvq12026earningsreleaseex.htm.jsonl | 92e4f803974e8b1d1fb782b7fa4c071295d1bcd965fc060f8d1edf8b3dca9f05 | Management leverage statement for Q1 2026 only |
| EX-99.1_2026-07-30_hgvq22026earningsreleaseex.htm.jsonl | 5535f4d3e680b0dd2b2a79102a2a9c458f84caa70b4ad3b4d26b8a0600e150b0 | Management leverage statement for Q2 2026 only |
| EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl | 53988e1805605a66d65d0b02e89b98e726349e8a8a53c9499714f31b0854d4d4 | Adjusted EBITDA reconciliations, construction deferral tables, management leverage, guidance |

Run context sha256 6edd9e91feb582497e031062a9d2821be0472a4f8a6020100729ec6b65f6bb35 (settings only, not evidence).

### Handoffs supplied

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 7f439ceea4fa01d10d2964db467b9c8db2afe1ab216f19ad970291bc172cd742 | Readiness status and limitations (no covenant text, management leverage undefined, Q3 construction recognition and allowance change, preliminary Elara accounting, revolver commitment not printed) |

The upstream handoff says the revolver total commitment is not printed. That remains true; this module derives it from printed components and labels the derivation (see Calculations). No other upstream statement is corrected.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported corporate leverage fell and interest cover improved, but the gain leans on a one-time third quarter construction recognition. Excluding it, leverage is materially higher, and liquidity is thinner than at year end. | Medium | Covenant levels and the management leverage definition are not in the sources, so headroom cannot be tested. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Reported LTM Adjusted EBITDA is flattered by a large third quarter construction recognition; excluding net construction effects, net leverage is close to the 3.9x management figure. | Reported leverage understates the debt burden on recurring earnings. | Medium |
| Corporate debt rose over the nine months, mainly through the revolver, while cash and revolver availability fell. | Liquidity is thinner than at year end. | High |
| Share repurchases over nine months exceeded free cash flow. | Buybacks were partly debt funded, which reduces deleveraging capacity. | Medium |
| Little corporate debt matures before 2028 and most falls due after 2030. | Near-term refinancing need is small; refinancing risk sits in the later years. | High |
| Non-recourse receivable debt and commitments sit outside the corporate debt figure. | Total claims are larger than the corporate leverage figures suggest. | High |

### Financial base view

On the reported basis, Hilton Grand Vacations carries corporate debt of 4,946 (gross) at September 30, 2026 against LTM Adjusted EBITDA of 1,434, giving total leverage of 3.45x and net leverage of 3.29x, down from 4.75x and 4.50x at FY2025. That improvement is not clean. Q3 2026 contains a net construction recognition of 296 that the company itself says lifted Adjusted EBITDA, and LTM includes net construction recognitions of 218 across the twelve months. Removing them, LTM Adjusted EBITDA is 1,216 and net leverage is 3.88x, which is close to the management figure of approximately 3.9x (a management statement whose definition is not in the pack, so the match is an observation and not a reconciliation). Corporate debt rose by 343 in nine months, of which 360 is revolver drawn (130 to 490); unrestricted cash fell from 239 to 227 and undrawn revolver capacity from 809 to 457, so corporate liquidity is 684 against 1,048 at year end. Nine-month free cash flow (273) was below share repurchases (410). Maturities are small through 2027, and the largest block falls due after 2030; the revolver matures January 2030. The credit read is therefore one of leverage that is moderate on the reported basis and elevated on a recurring basis, with liquidity adequate but declining and no covenant evidence to test headroom. Non-recourse receivable debt of 2,923 is excluded from these ratios; its inclusion would put total debt at 7,869 and is shown for information only.

### Source figures

Each figure used below, with its locator and exact quote.

| Item | Locator | Quote |
| --- | --- | --- |
| Adjusted EBITDA, FY2025 (969), EBITDA (760) | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:98` | "Adjusted EBITDA 969 1,094 1,005 (125) (11.4)" |
| EBITDA FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:97` | "EBITDA 760 735 842 25 3.4" |
| Total revenues FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:113` | "Total revenues 5,047 4,981 3,978" |
| Net income FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:113` | "Net income 99 60 313" |
| Interest expense FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:113` | "Interest expense (311) (329) (178)" |
| Operating cash flow FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:114` | "Net cash provided by operating activities 300 309 312" |
| Capital expenditure FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:114` | "Capital expenditures for property and equipment (excluding inventory) (70) (42) (31)" |
| Software capitalisation FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:114` | "Software capitalization costs (76) (84) (44)" |
| Share repurchases FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:114` | "Repurchase and retirement of common stock (600) (432) (368)" |
| Cash FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:112` | "Cash and cash equivalents $ 239 $ 328" |
| Restricted cash FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:112` | "Restricted cash 332 438" |
| Corporate debt gross FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:143` | "Total debt, gross 4,603 4,672" |
| Non-recourse debt gross FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:145` | "Total non-recourse debt, gross 2,751 2,350" |
| Revolver LCs FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:144` | "we had $61 million of letters of credit outstanding under the revolving credit facility" |
| Revolver capacity FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:144` | "we have $809 million remaining borrowing capacity under the revolver facility" |
| Revolver maturity | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:144` | "extend maturity to January 2030" |
| Timeshare Facility capacity FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:146` | "our Timeshare Facility has a remaining borrowing capacity of $235 million" |
| Cash interest, corporate, FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:163` | "Cash paid for interest on our corporate debt, net was $297 million, $354 million and $187 million" |
| Covenant description (affirmative leverage and ratio covenants, no levels) | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:61` | "contains affirmative covenants that will require us to be in compliance with certain leverage and financial ratios" |
| Total revenues Q3 and 9M 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:3` | "Total revenues 1,961 1,300 4,604 3,714" |
| Net income Q3 and 9M 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:3` | "Net income 297 30 380 46" |
| Interest expense 9M 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:3` | "Interest expense (78) (79) (221) (235)" |
| Operating cash flow 9M 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:4` | "Net cash provided by operating activities 349 133" |
| Capital expenditure 9M 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:4` | "Capital expenditures for property and equipment (excluding inventory) (23) (50)" |
| Software capitalisation 9M 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:4` | "Software capitalization costs (53) (54)" |
| Share repurchases 9M 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:4` | "Repurchase and retirement of common stock (410) (450)" |
| Cash and restricted cash at September 30, 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "Cash and cash equivalents $ 227 $ 239" |
| Restricted cash at September 30, 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "Restricted cash 275 332" |
| Timeshare financing receivables | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "Timeshare financing receivables, net 3,676 3,115" |
| Debt, net and non-recourse debt, net | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "Debt, net 4,885 4,545" |
| Non-recourse debt, net | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "Non-recourse debt, net 2,891 2,716" |
| Operating lease liabilities | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "Operating lease liabilities 106 89" |
| Total equity | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "Total equity 1,469 1,440" |
| Noncontrolling interest | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "Noncontrolling interest 162 151" |
| Term loan A | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:22` | "Term loan A due 2028 5.551 % $ 400 $ 400" |
| Term loan B due 2031 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:22` | "Term loan B due 2031 5.901 % 880 887" |
| Term loan B due 2033 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:22` | "Term loan B due 2033 5.901 % 850 851" |
| Revolver drawn | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:22` | "Revolver due 2030(2) 5.442 % 490 130" |
| Senior notes 2029 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:22` | "Senior notes due 2029 5.000 % 850 850" |
| Senior notes 2031 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:22` | "Senior notes due 2031 4.875 % 500 500" |
| Senior notes 2032 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:22` | "Senior notes due 2032 6.625 % 900 900" |
| Other debt | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:22` | "Other debt 76 85" |
| Corporate debt gross | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:22` | "Total debt, gross 4,946 4,603" |
| Weighted average rate | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:23` | "weighted-average interest rates were 5.751% and 5.691%" |
| Revolver LCs September 30, 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:23` | "we had $53 million of letters of credit outstanding under the revolving credit facility" |
| Revolver capacity September 30, 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:23` | "we have $457 million remaining borrowing capacity under the revolver facility" |
| Covenant compliance statement | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:23` | "We were in compliance with all applicable maintenance and financial covenants and ratios as of September 30, 2026" |
| Term Loan B refinancing | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:23` | "On July 17, 2026, we refinanced our Term Loan B due 2028 with an amended $850 million Term Loan B due 2033." |
| Interest rate swaps | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:23` | "the aggregate notional values of the interest rate swaps under our senior secured credit facility was $550 million" |
| Guarantors of the 2032 secured notes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:24` | "The Senior Notes due 2032 are guaranteed on a senior secured basis by certain of our subsidiaries." |
| Cash interest, corporate, 9M 2026 and 9M 2025 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:24` | "Cash paid for interest on our corporate debt, net was $207 million and $221 million for the nine months ended September 30, 2026 and 2025" |
| Non-recourse debt gross | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:24` | "Total non-recourse debt, gross 2,923 2,751" |
| Timeshare Facility capacity | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:25` | "our Timeshare Facility has a remaining borrowing capacity of $450 million" |
| Big Cedar Timeshare Facility capacity | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:25` | "the Big Cedar Timeshare Facility has a remaining borrowing capacity of $175 million" |
| Maturity row 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:26` | "2026 (remaining three months) $ 6 $ 156 $ 162" |
| Maturity row 2027 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:26` | "2027 22 541 563" |
| Maturity row 2028 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:26` | "2028 430 439 869" |
| Maturity row 2029 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:26` | "2029 878 923 1,801" |
| Maturity row 2030 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:26` | "2030 515 276 791" |
| Maturity row thereafter and total | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:26` | "Thereafter 3,095 588 3,683" |
| Maturity total | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:26` | "Total $ 4,946 $ 2,923 $ 7,869" |
| Cash interest on non-recourse debt, FY2025 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:142` | "Cash paid for interest associated with our non-recourse debt was $104 million, $90 million and $44 million" |
| Cash interest on non-recourse debt | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:21` | "Cash paid for interest associated with our non-recourse debt was $93 million and $76 million" |
| Inventory purchase commitments | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:35` | "we were committed to purchase approximately $304 million of inventory over a period of 12 years and $53 million of other commitments" |
| Commitment table total | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:35` | "Total $ 46 $ 58 $ 107 $ 96 $ 112 $ 195 $ 614" |
| Marketing and license fee commitments | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:35` | "Marketing and license fee agreements $ 9 $ 38 $ 38 $ 38 $ 39 $ 95 $ 257" |
| Litigation accrual | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:36` | "we accrued liabilities of approximately $19 million and $8 million, respectively, for all legal matters" |
| Surety commitments | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:36` | "We have commitments from surety providers in the amount of $346 million" |
| Total contractual obligations | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:59` | "we were committed to $10.1 billion in contractual obligations over 14 years" |
| Unconsolidated affiliate debt | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:21` | "This unconsolidated affiliate had an aggregated debt balance of $38 million as of September 30, 2026." |
| Adjusted EBITDA Q3 and 9M, 2026 and 2025 | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:18` | "Adjusted EBITDA 617 249 1,137 672" |
| EBITDA Q3 and 9M | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:18` | "EBITDA 562 191 944 511" |
| Adjusted EBITDA by quarter, 2025 | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:7` | "Adjusted EBITDA 185 238 249 297 969" |
| Net construction deferrals, 2025 | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:7` | "Net construction deferrals(2) $ (68) $ (45) $ (57) $ (32) $ (202)" |
| Net construction recognitions, 2026 | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:6` | "Net construction (deferrals) recognitions(2) $ (18) $ (28) $ 296 $ — $ 250" |
| Free cash flow, quarter and nine months | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:18` | "Free Cash Flow $ 52 $ (4) $ 273 $ 29" |
| Q3 construction recognition effect | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:2` | "Adjusted EBITDA attributable to stockholders was affected by a net construction recognition of $296 million." |
| Management leverage statement | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:6` | "total net leverage on a trailing 12-month basis was approximately 3.9x" |
| Guidance reduction | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:2` | "to a range of $1.165 billion to $1.180 billion, from the prior range of $1.225 billion to $1.265 billion" |
| Management leverage at Q2 2026 | `EX-99.1_2026-07-30_hgvq22026earningsreleaseex.htm.jsonl page:3` | "total net leverage on a trailing 12-month basis was approximately 3.8x" |
| Management leverage at Q1 2026 | `EX-99.1_2026-04-30_hgvq12026earningsreleaseex.htm.jsonl page:4` | "total net leverage on a trailing 12-month basis was approximately 3.9x" |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 4.75 | 4.50 | x | Corporate debt gross 4,603 and net of unrestricted cash 239, over Adjusted EBITDA 969 as reported (company-defined, consolidated before noncontrolling interest, includes a net construction deferral of 202). Excluding non-recourse debt 2,751 and restricted cash. Excluding the deferral: 3.93x total and 3.73x net. Not a covenant definition. |
| LTM Q3 2026 | 3.45 | 3.29 | x | Corporate debt gross 4,946 and net of unrestricted cash 227, over LTM Adjusted EBITDA 1,434 built as FY2025 less nine months 2025 plus nine months 2026 (company-defined, includes net construction recognitions of 218). Excluding non-recourse debt 2,923 and restricted cash. Excluding net construction: 4.07x total and 3.88x net. Management states approximately 3.9x on an undefined basis. Not a covenant definition. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 3.26 | x | Adjusted EBITDA 969 over cash paid for interest on corporate debt, net, 297. Excludes interest on non-recourse debt (104 cash paid in FY2025). Excluding the construction deferral: 3.94x. Not a covenant definition. |
| LTM Q3 2026 | 5.07 | x | LTM Adjusted EBITDA 1,434 over LTM cash interest on corporate debt 283 (297 less 221 plus 207). Excludes interest on non-recourse debt (93 cash paid in nine months 2026). Excluding net construction: 4.30x. Not a covenant definition. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 239 | 809 | US$m | Unrestricted cash at December 31, 2025. Undrawn is the remaining corporate revolver capacity as printed; drawn 130 plus letters of credit 61 plus 809 sums to 1,000, so the printed capacity appears net of letters of credit (derived, commitment not printed). Excludes restricted cash 332 and non-recourse Timeshare Facility capacity 235. |
| Q3 2026 | 227 | 457 | US$m | Unrestricted cash at September 30, 2026. Undrawn is the remaining corporate revolver capacity as printed; drawn 490 plus letters of credit 53 plus 457 sums to 1,000 (derived). The revolver matures January 2030; no facility expires within twelve months. Excludes restricted cash 275 and non-recourse capacity (Timeshare Facility 450, Big Cedar Timeshare Facility 175), which funds receivables only. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 (remaining three months) | 6 | US$m | Corporate debt contractual principal as of September 30, 2026. Non-recourse debt maturing in the period is 156 and is not included. |
| 2027 | 22 | US$m | Corporate debt principal. Non-recourse debt maturing is 541, not included. |
| 2028 | 430 | US$m | Corporate debt principal; includes the Term Loan A of 400. Non-recourse debt maturing is 439, not included. |
| 2029 | 878 | US$m | Corporate debt principal; includes the 5.000% senior notes of 850. Non-recourse debt maturing is 923, not included. |
| 2030 | 515 | US$m | Corporate debt principal; includes the revolver drawn 490. Non-recourse debt maturing is 276, not included. |
| Thereafter | 3,095 | US$m | Corporate debt principal; includes the term loans due 2031 and 2033 and the senior notes due 2031 and 2032. Non-recourse debt maturing is 588, not included. Total corporate 4,946 equals gross debt. |

### Financials and credit metrics

| Metric | FY2025 | 9M 2025 | 9M 2026 | LTM Q3 2026 | Basis |
| --- | --- | --- | --- | --- | --- |
| Total revenues | 5,047 | 3,714 | 4,604 | 5,937 | Reported; LTM calculated |
| Net income | 99 | 46 | 380 | 433 | Reported before noncontrolling interest; LTM calculated |
| EBITDA (company definition) | 760 | 511 | 944 | 1,193 | Reported; LTM calculated |
| Adjusted EBITDA (company definition) | 969 | 672 | 1,137 | 1,434 | Reported; LTM calculated; includes net construction effects |
| Net construction (deferrals) recognitions in Adjusted EBITDA | (202) | (170) | 250 | 218 | Reported by quarter; 9M 2025 is the sum of three quarters; LTM calculated |
| Adjusted EBITDA excluding net construction | 1,171 | 842 | 887 | 1,216 | Calculated; analyst construction of the company's own disclosure |
| Interest expense, income statement | 311 | 235 | 221 | 297 | Reported; LTM calculated |
| Cash interest paid, corporate debt | 297 | 221 | 207 | 283 | Reported; LTM calculated |
| Cash interest paid, non-recourse debt | 104 | 76 | 93 | 121 | Reported; LTM calculated |
| Operating cash flow | 300 | 133 | 349 | 516 | Reported; LTM calculated; includes receivable and deferred revenue movements |
| Capital expenditure and software capitalisation | 146 | 104 | 76 | 118 | Reported components summed; LTM calculated |
| Free cash flow (operating cash flow less both) | 154 | 29 | 273 | 398 | Calculated; matches the company's reported nine month free cash flow of 273 and 29 |
| Share repurchases | 600 | 450 | 410 | 560 | Reported; LTM calculated |
| Total debt / Adjusted EBITDA (x) | 4.75 | Not calculable | Not calculable | 3.45 | Corporate gross debt at period end; interim columns not calculated because 9M flows are not annual |
| Net debt / Adjusted EBITDA (x) | 4.50 | Not calculable | Not calculable | 3.29 | Corporate gross debt less unrestricted cash |
| Net debt / Adjusted EBITDA excluding net construction (x) | 3.73 | Not calculable | Not calculable | 3.88 | Calculated |
| Adjusted EBITDA / cash interest (x) | 3.26 | Not calculable | Not calculable | 5.07 | Corporate cash interest only |
| Free cash flow / corporate debt | 3.3% | Not calculable | Not calculable | 8.0% | Calculated; free cash flow over corporate gross debt at period end |

### Balance sheet and debt at the two balance dates

| Item | December 31, 2025 | September 30, 2026 | Note |
| --- | --- | --- | --- |
| Cash and cash equivalents | 239 | 227 | Unrestricted |
| Restricted cash | 332 | 275 | Escrow and non-recourse reserves |
| Term loan A due 2028 | 400 | 400 | Senior secured credit facility |
| Term loan B due 2031 | 887 | 880 | Senior secured credit facility |
| Term loan B due 2028, refinanced into the Term Loan B due 2033 on July 17, 2026 | 851 | 850 | The 10-K prints 851 for the loan due 2028; the Q3 table prints the same 851 as the comparative against the loan due 2033 |
| Revolver due 2030 (drawn) | 130 | 490 | Senior secured credit facility |
| Senior notes due 2029, 5.000% | 850 | 850 | Unsecured |
| Senior notes due 2031, 4.875% | 500 | 500 | Unsecured |
| Senior notes due 2032, 6.625% | 900 | 900 | Secured |
| Other debt | 85 | 76 | |
| Total corporate debt, gross | 4,603 | 4,946 | Net of deferred costs and discounts: 4,545 and 4,885 |
| Non-recourse debt, gross | 2,751 | 2,923 | Net: 2,716 and 2,891 |
| Total borrowings, gross | 7,354 | 7,869 | Calculated |
| Timeshare financing receivables, net | 3,115 | 3,676 | Collateral pool for non-recourse debt |
| Total equity | 1,440 | 1,469 | Includes noncontrolling interest of 151 and 162 |

### Instrument terms as printed

The Term Loan B pricing is stated as unchanged at SOFR plus 2.00 percent after the July 2026 refinancing, from the quote above. The 10-K states pricing for the term loans and revolver: Term Loan A at SOFR plus 1.65 percent and both Term Loan Bs at SOFR plus 2.00 percent (`10-K_2025-12-31_hgv-20251231.htm.jsonl page:144`: "The Term Loan B due 2031 was repriced to SOFR plus 2.00%"). Interest rate swaps with a notional of 550 convert part of the floating rate debt to an average fixed 1.55 percent through 2028. The 2032 notes are guaranteed on a senior secured basis and the 2029 and 2031 notes on a senior unsecured basis, each by certain unnamed subsidiaries (`10-Q_2026-09-30_hgv-20260930.htm.jsonl page:24`: "The Senior Unsecured Notes are guaranteed on a senior unsecured basis by certain of our subsidiaries."). Issuer and co-issuer of the notes are named only in the 10-K exhibit index (Hilton Grand Vacations Borrower LLC and Hilton Grand Vacations Borrower Inc.) (`10-K_2025-12-31_hgv-20251231.htm.jsonl page:167`: "Indenture, dated as of January 17, 2024, among Hilton Grand Vacations Borrower LLC, Hilton Grand Vacations Borrower Inc."). Guarantor identity, collateral package, call schedules and incurrence tests are Not supplied: the indentures and credit agreement are not in the pack.

### Claims outside the corporate debt figure

| Claim | Amount | Inside or outside corporate debt figure | Locator basis |
| --- | --- | --- | --- |
| Non-recourse debt, gross | 2,923 | Outside; payable from pledged receivables | Quoted above |
| Operating lease liabilities | 106 | Outside | Balance sheet row above; finance leases: no separate balance printed in the pages searched |
| Inventory purchase commitments | 304 over 12 years | Outside | Quoted above |
| Marketing and license fee commitments | 257 | Outside | Quoted above |
| Other commitments | 53 | Outside | Quoted above |
| Commitments table total | 614 | Outside | Quoted above |
| Contractual obligations including debt and interest (company statement) | 10.1 billion over 14 years | Overlaps debt | Quoted above |
| Surety bond commitments from providers | 346 | Outside; contingent capacity, not a liability | Quoted above |
| Legal accrual | 19 | Outside | Quoted above |
| Debt of unconsolidated affiliate 1776 Holding LLC, without recourse | 38 | Outside; not consolidated | Quoted above |
| Noncontrolling interest (Big Cedar joint venture) | 162 | Outside | Balance sheet row above |

A search of the 10-K and the Q3 10-Q found no pension or retiree medical obligation, no factoring or supply-chain finance arrangement and no consent decree.

### Events through the cutoff that affect the financial base

| Event | Locator | Quote |
| --- | --- | --- |
| Term Loan B refinanced July 17, 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:23` | "On July 17, 2026, we refinanced our Term Loan B due 2028 with an amended $850 million Term Loan B due 2033." |
| Timeshare Facility upsized and extended, May 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:25` | "increasing the facility size from $850 million to $1.0 billion" |
| Big Cedar warehouse facility, September 14, 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:25` | "Big Cedar entered into the Big Cedar Timeshare Facility, a $200 million revolving receivables warehouse facility" |
| NBA Receivables Facility terminated | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:26` | "During the third quarter of 2026, we terminated the NBA Receivables Facility." |
| Elara acquisition, April 29, 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:8` | "for a total cash consideration of $131 million" |
| New repurchase plan authorised August 12, 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:59` | "On August 12, 2026, our Board of Directors approved a share repurchase program authorizing us to repurchase up to an aggregate of $600 million" |
| Allowance method change, Q3 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:16` | "we recorded a $55 million decrease in the allowance for originated timeshare financing receivable" |
| FY2026 Adjusted EBITDA guidance reduced, October 29, 2026 | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:2` | "The Company is reducing its guidance for the full year 2026 Adjusted EBITDA, excluding deferrals and recognitions" |

The allowance change reduced the provision and raised Sales of VOIs, net, in Q3 2026 and so raised reported earnings in the quarter by an amount separate from the construction effect; the filings give the 55 decrease but do not state its Adjusted EBITDA effect separately, so the Adjusted EBITDA excluding net construction in this module still includes it. No subsequent-events note exists in the Q3 10-Q, and nothing after October 29, 2026 is in the pack.

### Covenants

Covenant compliance is Not supplied beyond the statement that the company was in compliance with all applicable maintenance and financial covenants and ratios as of September 30, 2026 (quoted above) and that the credit agreement carries leverage and financial ratio covenants (quoted above, 10-K). Test levels, step-downs, the issuer's reported ratio and the headroom are not printed. The management total net leverage figure of approximately 3.9x (Q1 2026 and Q3 2026) and 3.8x (Q2 2026) has no definition in the pack and differs in kind from the analyst figures in this module (which use gross corporate debt less unrestricted cash over company-defined Adjusted EBITDA); the net leverage excluding net construction (3.88x) is close to the management figure but this does not establish that the definitions match.

## Calculations

All inputs are quoted in Source figures. LTM means FY2025 less nine months 2025 plus nine months 2026. Rounded to two decimals in tables.

| Calculation | Inputs | Result |
| --- | --- | --- |
| LTM revenue | 5,047 - 3,714 + 4,604 | 5,937 |
| LTM net income | 99 - 46 + 380 | 433 |
| LTM EBITDA | 760 - 511 + 944 | 1,193 |
| LTM Adjusted EBITDA | 969 - 672 + 1,137 | 1,434 |
| Check: Q4 2025 Adjusted EBITDA | 969 - 672 | 297, equal to the printed fourth quarter 2025 value of 297 |
| 9M 2025 Adjusted EBITDA from quarters | 185 + 238 + 249 | 672, equal to the printed nine month value |
| 9M 2025 net construction | (68) + (45) + (57) | (170) |
| 9M 2026 net construction | (18) + (28) + 296 | 250, equal to the printed nine month value |
| LTM net construction | (202) - (170) + 250 | 218 |
| Adjusted EBITDA excluding net construction, FY2025 | 969 + 202 | 1,171 |
| Adjusted EBITDA excluding net construction, 9M 2025 | 672 + 170 | 842 |
| Adjusted EBITDA excluding net construction, 9M 2026 | 1,137 - 250 | 887 |
| Adjusted EBITDA excluding net construction, LTM | 1,434 - 218; also 1,171 - 842 + 887 | 1,216 |
| LTM interest expense | 311 - 235 + 221 | 297 |
| LTM cash interest, corporate | 297 - 221 + 207 | 283 |
| LTM cash interest, non-recourse | 104 - 76 + 93 | 121 |
| LTM operating cash flow | 300 - 133 + 349 | 516 |
| LTM capital expenditure and software | (70 + 76) - (50 + 54) + (23 + 53) = 146 - 104 + 76 | 118 |
| LTM free cash flow | 516 - 118 | 398 |
| Free cash flow checks | 9M 2026: 349 - 23 - 53; 9M 2025: 133 - 50 - 54 | 273 and 29, equal to the printed 273 and 29 |
| LTM share repurchases | 600 - 450 + 410 | 560 |
| Net corporate debt, FY2025 | 4,603 - 239 | 4,364 |
| Net corporate debt, Q3 2026 | 4,946 - 227 | 4,719 |
| Total debt / Adjusted EBITDA, FY2025 | 4,603 / 969 | 4.750x |
| Net debt / Adjusted EBITDA, FY2025 | 4,364 / 969 | 4.504x |
| Total debt / Adjusted EBITDA, LTM | 4,946 / 1,434 | 3.449x |
| Net debt / Adjusted EBITDA, LTM | 4,719 / 1,434 | 3.291x |
| Total debt / Adjusted EBITDA excluding construction, FY2025 | 4,603 / 1,171 | 3.931x |
| Net debt / Adjusted EBITDA excluding construction, FY2025 | 4,364 / 1,171 | 3.727x |
| Total debt / Adjusted EBITDA excluding construction, LTM | 4,946 / 1,216 | 4.067x |
| Net debt / Adjusted EBITDA excluding construction, LTM | 4,719 / 1,216 | 3.881x |
| Interest cover, FY2025 | 969 / 297 | 3.263x |
| Interest cover excluding construction, FY2025 | 1,171 / 297 | 3.943x |
| Interest cover, LTM | 1,434 / 283 | 5.067x |
| Interest cover excluding construction, LTM | 1,216 / 283 | 4.297x |
| Total borrowings including non-recourse, September 30, 2026 | 4,946 + 2,923 | 7,869, equal to the printed maturity table total |
| Total borrowings including non-recourse, December 31, 2025 | 4,603 + 2,751 | 7,354 |
| Total borrowings over LTM Adjusted EBITDA (information only) | 7,869 / 1,434 | 5.487x |
| Free cash flow / corporate debt, FY2025 and LTM | 154 / 4,603; 398 / 4,946 | 3.3% and 8.0% |
| Corporate liquidity | 227 + 457; 239 + 809 | 684 and 1,048 |
| Revolver commitment (derived, not printed) | 490 + 53 + 457; 130 + 61 + 809 | 1,000 at both dates |
| Corporate debt increase in nine months | 4,946 - 4,603; revolver 490 - 130 | 343; 360 |
| Maturity table check | 6 + 22 + 430 + 878 + 515 + 3,095; non-recourse 156 + 541 + 439 + 923 + 276 + 588 | 4,946 and 2,923, equal to the printed totals |
| Commitments table check | 304 + 257 + 53 | 614, equal to the printed total |

Period and perimeter checks: every ratio uses period-end corporate debt (recourse) with a twelve-month earnings figure on the same consolidated perimeter. The Elara acquisition (April 29, 2026) is included in the nine months 2026 from its acquisition date and no pro forma adjustment is made for the part of the LTM before it; this is a limitation, not a correction. Adjusted EBITDA is consolidated before noncontrolling interest; the LTM amount attributable to noncontrolling interest is 19 (19 - 14 + 14), so the amount attributable to stockholders is 1,415 (950 - 658 + 1,123). The ratios in this module use the consolidated amount.

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Covenant test levels, definitions, reported ratios and headroom: Not supplied (credit agreement, amendments and indentures not in pack) | Headroom Not calculable | Add the credit agreement and indentures; until then use the compliance statement only |
| Management net leverage of approximately 3.9x has no definition or inputs | Cannot be reconciled to the analyst figures | Treat as a management claim |
| Revolver commitment is not printed; 1,000 is derived from drawn, letters of credit and remaining capacity | Derived value | Confirm against the credit agreement |
| The allowance method change (55) raised Q3 2026 Sales of VOIs, net; the Adjusted EBITDA effect is not separately stated | LTM and ex-construction Adjusted EBITDA may be overstated by an amount not disclosed | Ask for the effect or treat as a limitation |
| LTM has no pro forma for the Elara acquisition and purchase accounting is preliminary | Minor for leverage; balances may change | Re-check at the next filing |
| Fiscal fourth quarter 2026 is not in the pack; guidance for FY2026 Adjusted EBITDA excluding deferrals and recognitions is a range (1.165 to 1.180 billion), reduced from 1.225 to 1.265 billion | No forward leverage calculation is made | Use guidance only as management context |
| The 9M and quarterly interim ratio cells are Not calculable because annualisation is not performed | None | None |
| Finance lease balances are not separately printed in the pages searched; operating lease liabilities are 106 | Minor | Check lease note |
| Extraction fidelity not reviewed; tables are flattened text | Low | Spot-check key rows against the filings |

## Next module

Proceed to CP-1A (business and transaction context). Carry forward: corporate and non-recourse debt kept separate; the construction recognition and allowance method change as comparability issues; the Term Loan B refinancing, Timeshare Facility renewal, Big Cedar facility and Elara acquisition as transaction events; covenant terms as Not supplied; the derived revolver commitment of 1,000 labelled as derived. CP-2 and CP-5 follow.
