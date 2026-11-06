## Request

Financial base for Primo Brands Corp (Primo Brands Corporation, NYSE: PRMB, issuer id prmb), as of 2026-11-05. Pathway credit_snapshot, reporting currency USD, current period Q3 2026, prior period FY2025. Evidence cutoff 2026-11-05. Amounts are USD millions, as the filings print them. The task is to set out the reported financial statements, the debt and liquidity position, the covenants, the claims outside debt and the latest-quarter events, to calculate leverage, cover and liquidity from printed inputs, and to say what the base can and cannot support.

The readiness review (supplied handoff) found one registrant, one reportable segment and USD throughout, and carried forward four limits: no executed financing documents, a debt table and maturity ladder that predate the March 2026 refinancing, three disclosed class actions without loss estimates beyond amounts accrued, and unreviewed text extraction. This module works inside those limits. One correction to that handoff is made under `### Correction to the earlier handoff`.

Periods used: FY2025 is the year ended December 31, 2025 (audited). Q3 2026 is the three months ended September 30, 2026 and nine months 2026 is the nine months ended that date (both unaudited). LTM Sep 30, 2026 is FY2025 less nine months 2025 plus nine months 2026, the same construction the company uses (Q3 release `page:14`). Every other period is labelled where it appears.

The run context holds no ratings, quotes, peers or deal terms; those are Not supplied, never zero.

## Sources

`page:N` is the chunk of the converted text file, not the printed page. The sha256 is the pinned file hash.

### Issuer sources relied on

| Source (exact name) | sha256 (pinned file) | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_prmb-20251231.htm.jsonl | 60d79b9ec8f05aed0d140a51b4d3f1d8eb015dd6743bb2699d0fee368bff051f | Audited FY2025 statements (`page:126` to `page:128`), debt note (`page:154` to `page:162`), contractual obligations (`page:104`, `page:105`), Adjusted EBITDA (`page:86`), leases (`page:153`) |
| 10-Q_2026-03-31_prmb-20260331.htm.jsonl | 99681433894a4d7b14141909d74698aff6d2383b60283b0706ad04024190b1b8 | Q1 2026 statements, liquidity text (`page:42`), letters of credit (`page:33`) |
| 10-Q_2026-06-30_prmb-20260630.htm.jsonl | f5f942b75f737f8af26039c159ca583ff2e512ee89a2478a6850a2d1b07a0f98 | Q2 2026 statements (`page:4` to `page:6`), liquidity text (`page:50`), letters of credit (`page:37`) |
| 10-Q_2026-09-30_prmb-20260930.htm.jsonl | 95354dd1e2fc79683928b45ccb08e03d8e76291367a9171fad5aa8f4c5954c6b | Q3 2026 statements (`page:4` to `page:7`), debt, covenants, contingencies, MD&A, ratings |
| EX-99.1_2026-05-07_ex991.htm.jsonl | 5b4e5356c8a7dd33fff4d2ec1d2357c63bb85628f6a6619799a77852ce483032 | Q1 2026 release: Adjusted EBITDA, net leverage build, outlook |
| EX-99.1_2026-08-05_ex991.htm.jsonl | 56ee46b7abb25637a63476c674a59659d13c2eddb920ccd958837f11cba5c01d | Q2 2026 release: Adjusted EBITDA, net leverage build, outlook |
| EX-99.1_2026-11-05_ex991.htm.jsonl | 6dd2c90be990eaffd514267a4b4a0363cc3e49d4529fedc16d1ed91c51d7cb2d | Q3 2026 release: non-GAAP reconciliations (`page:11` to `page:14`), outlook (`page:2`), subsequent events (`page:2`) |

The file `_retrieval.json` was ignored by CP-OS and is not evidence.

### Run context (not issuer evidence)

| Source | sha256 |
| --- | --- |
| context | 6c8ceb76224ccf7cca54dd0892bbd34fd084e5ce74d3140c5df58145b6c1160f |

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 9d41085fd45f5ff627591894684056b0d9ea68db270d4db90c628ad2a3f32ec9 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Sales and cash flow improved in 2026 while trailing Adjusted EBITDA is slightly below year-end, leaving leverage at 3.66 times gross and 3.32 times net. Liquidity is ample; the 2028 and 2029 notes are the next wall. | Medium | Leverage rests on management Adjusted EBITDA; covenant ratios, executed credit documents and a filed post-refinancing debt schedule are not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Nine-month 2026 net sales rose 2.6% to 5,243.3 million, but Adjusted EBITDA fell 1.0% to 1,102.0 million and the margin slipped to 21.0% from 21.8%. | Earnings growth lags revenue growth because freight and materials costs rose, so debt capacity is not widening yet. | High |
| Trailing Adjusted EBITDA is 1,436.1 million and debt is 5,249.7 million, giving 3.66 times gross and 3.32 times net; on unadjusted EBITDA the figures are 4.34 and 3.95 times. | Leverage looks moderate mainly because of 227.0 million of management add-backs, so add-back quality matters to the credit view. | High |
| The term loan was refinanced to March 2031, but derived figures put 532.3 million due in 2028 and 1,490.2 million in 2029. | The senior notes are the next refinancing test, and the company says operating cash will not repay all debt at maturity. | Medium |
| Liquidity is 1,063.8 million: cash of 477.2 million plus 586.6 million of revolver availability after letters of credit. | Liquidity covers scheduled debt service, but the undrawn status of the revolver is inferred, not printed. | Medium |
| Nine-month free cash flow was 319.6 million; dividends and buybacks took 201.3 million, and a new 300.0 million buyback was authorized after quarter end. | Shareholder returns compete with deleveraging, since net leverage fell only slightly this year. | Medium |

### Financial base view

Primo Brands Corporation reports as one registrant with one segment, so the base is a single consolidated set of statements rather than a segment mosaic. Through nine months 2026, net sales were 5,243.3, up 2.6% on 5,109.9, and Adjusted EBITDA was 1,102.0, down 1.0% from 1,112.7, because cost of sales grew faster than sales on freight and materials costs (Q3 10-Q `page:49`). Q3 2026 was better than the first half: net sales rose 3.1% to 1,821.0, Adjusted EBITDA rose 1.6% to 411.0 and the margin was 22.6% against 22.9% a year earlier. EBITDA before add-backs rose much faster than Adjusted EBITDA (396.9 against 313.1 in Q3) because lower integration costs (add-back of 23.7 against 88.2) and an unrealized gain of 26.1, both excluded from Adjusted EBITDA, flowed through, and the total add-backs shrank to 14.1 in Q3 2026 from 91.4 a year earlier. Trailing-twelve-month Adjusted EBITDA of 1,436.1 gives gross leverage of 3.66 times and net leverage of 3.32 times on the company's definition; on EBITDA before add-backs of 1,209.1 the ratios are 4.34 and 3.95 times. Cash paid for interest of 298.7 over the trailing twelve months is covered 4.81 times by Adjusted EBITDA. Operating cash flow was 625.3 for nine months against 477.2, with payables and accruals contributing 141.1 of the 148.1 improvement, partly offset by other working capital lines; a payables-driven gain can reverse. Liquidity of 1,063.8 is cash of 477.2 plus revolver commitments of 750.0 less 163.4 of letters of credit. The March 2026 refinancing moved the term loan to March 2031, so the nearest large maturities are the 3.875% notes in October 2028 and the 4.375% and 6.250% notes in April 2029. Four limits bind: Adjusted EBITDA is a management measure with large add-backs, covenant ratios are not printed, finance leases, other debt and the revolver balance are not itemized at September 30, 2026, and the maturity ladder after the refinancing is derived, not filed.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2025 (FY2025) | 3.63 | 3.37 | x | Debt of 5,249.1 US$m (10-K contractual maturities total 5,078.3 plus finance leases 170.8, `page:155`, `page:153`) and unrestricted cash of 376.7 US$m (`page:151`) over FY2025 Adjusted EBITDA of 1,446.8 US$m (`page:86`). Management definition; the company's own year-end ratio is not in the pack. On unadjusted EBITDA of 1,081.7 US$m the ratios are 4.85x and 4.50x. Not a covenant ratio |
| Mar 31, 2026 (LTM) | 3.72 | 3.52 | x | Q1 release `page:12`: debt excluding unamortized costs 5,255.1 US$m, unrestricted cash 287.9 US$m, LTM Adjusted EBITDA 1,411.3 US$m; net ratio as printed, gross ratio derived. Management definition |
| Jun 30, 2026 (LTM) | 3.67 | 3.42 | x | Q2 release `page:13`: debt excluding unamortized costs 5,250.0 US$m, unrestricted cash 366.5 US$m, TTM Adjusted EBITDA 1,429.6 US$m; net ratio as printed, gross ratio derived. Management definition |
| Sep 30, 2026 (LTM) | 3.66 | 3.32 | x | Q3 release `page:14`: debt excluding unamortized costs 5,249.7 US$m, unrestricted cash 477.2 US$m, TTM Adjusted EBITDA 1,436.1 US$m; net ratio as printed, gross ratio derived. On unadjusted LTM EBITDA of 1,209.1 US$m the ratios are 4.34x and 3.95x. Not a covenant ratio |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 4.77 | x | FY2025 Adjusted EBITDA of 1,446.8 US$m over cash paid for interest, net of interest capitalized, of 303.1 US$m (10-K `page:128`). On unadjusted EBITDA of 1,081.7 US$m the ratio is 3.57x. Not the covenant definition |
| LTM Sep 30, 2026 | 4.81 | x | LTM Adjusted EBITDA of 1,436.1 US$m over LTM cash interest of 298.7 US$m (303.1 less 204.8 plus 200.4, `page:7` of the Q3 10-Q and 10-K `page:128`). On unadjusted LTM EBITDA of 1,209.1 US$m the ratio is 4.05x. Not the covenant definition |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2025 | 376.7 | 612.6 | US$m | Unrestricted cash (10-K `page:151`). Revolver commitments of 750.0 less letters of credit of 137.4 (10-K `page:90`); revolver loans shown as nil in the debt table (10-K `page:154`) |
| Mar 31, 2026 | 287.9 | 586.1 | US$m | Unrestricted cash from the Q1 release `page:12` (288.2 less 0.3 restricted). Revolver 750.0 less letters of credit of 163.9 (Q1 10-Q `page:42`); revolver loans not itemized, assumed nil |
| Jun 30, 2026 | 366.5 | 586.6 | US$m | Unrestricted cash from the Q2 release `page:13` (366.8 less 0.3 restricted). Revolver 750.0 less letters of credit of 163.4 (Q2 10-Q `page:50`); revolver loans not itemized, assumed nil |
| Sep 30, 2026 | 477.2 | 586.6 | US$m | Unrestricted cash (477.4 less 0.2 restricted, `page:51`). Revolver 750.0 less letters of credit of 163.4 (`page:51`); revolver loans not itemized, assumed nil from the phrase "undrawn availability" (`page:50`). Revolver matures February 2030 with an undefined springing maturity; no facility expires within twelve months |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q4 2026 | 7.7 | US$m | Derived pro forma at Sep 30, 2026: term loan amortization of 1.00% a year on 3,090.0 in equal quarterly instalments (`page:16`). Excludes finance leases and other debt, which are not itemized at Sep 30, 2026 |
| 2027 | 30.9 | US$m | Derived: four instalments of 7.725 on the term loan |
| 2028 | 532.3 | US$m | Derived: term loan 30.9 plus 3.875% Senior Secured Notes due October 31, 2028 of EUR 441.9 million, converted at the 510.6 US$m per EUR 450.0 million rate stated at Sep 30, 2026 (`page:54`), giving 501.4 |
| 2029 | 1,490.2 | US$m | Derived: term loan 30.9 plus 6.250% Senior Notes due April 1, 2029 of 712.8 plus 4.375% Senior Secured Notes due April 30, 2029 of 746.5 (10-K `page:159`, `page:160`) |
| 2030 | 30.9 | US$m | Derived: term loan instalments only; the revolver matures February 2030 and is assumed undrawn |
| 2031 | 2,943.2 | US$m | Derived: term loan balance at the March 2031 maturity (3,074.5 less 7.7 less four years of 30.9). Total of the six rows is 5,035.2 against term loan 3,074.5 plus notes 1,247.9 |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2025 | Nine months 2025 | Nine months 2026 | Q3 2025 | Q3 2026 | LTM Sep 30, 2026 | Source and basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales | 6,664.0 | 5,109.9 | 5,243.3 | 1,766.1 | 1,821.0 | 6,797.4 | 10-K `page:126`; Q3 10-Q `page:5`; LTM derived |
| Gross profit | 2,020.2 | 1,590.1 | 1,567.5 | 528.2 | 553.9 | 1,997.6 | Same pages; LTM derived |
| Gross margin (%) | 30.3 | 31.1 | 29.9 | 29.9 | 30.4 | 29.4 | Derived to one decimal; Q3 10-Q `page:45`, `page:48` print the quarter and nine-month margins |
| Selling, general and administrative expenses | 1,390.4 | 1,049.4 | 998.5 | 343.0 | 316.3 | 1,339.5 | Same pages; LTM derived |
| Acquisition, integration and restructuring expenses (statement line) | 167.5 | 133.7 | 47.5 | 44.2 | 16.7 | 81.3 | Same pages; LTM derived. The Adjusted EBITDA add-back is larger because it includes integration costs in cost of sales |
| Operating income | 430.4 | 412.4 | 567.2 | 146.4 | 248.9 | 585.2 | Same pages; LTM derived |
| Interest and financing expense, net | 326.5 | 247.1 | 239.5 | 83.1 | 79.9 | 318.9 | Same pages; LTM derived |
| Net income from continuing operations | 80.4 | 105.7 | 221.0 | 40.5 | 124.5 | 195.7 | Same pages; LTM derived |
| Depreciation and amortization | 610.2 | 437.0 | 429.5 | 163.1 | 146.3 | 602.7 | Cash flow statements; LTM derived |
| EBITDA, company definition | 1,081.7 | 850.2 | 977.6 | 313.1 | 396.9 | 1,209.1 | 10-K `page:86`; Q3 release `page:11`; LTM derived |
| Adjusted EBITDA, company definition | 1,446.8 | 1,112.7 | 1,102.0 | 404.5 | 411.0 | 1,436.1 | 10-K `page:86`; Q3 release `page:11`; LTM as printed on `page:14` |
| Adjusted EBITDA margin (%) | 21.7 | 21.8 | 21.0 | 22.9 | 22.6 | 21.1 | Nine-month, Q3 margins as printed (Q3 release `page:11`); FY2025 and LTM derived |
| Add-backs (Adjusted EBITDA less EBITDA) | 365.1 | 262.5 | 124.4 | 91.4 | 14.1 | 227.0 | Derived |
| Net cash from operating activities, continuing | 680.3 | 477.2 | 625.3 | 283.4 | 293.6 | 828.4 | 10-K `page:127`; Q3 10-Q `page:6`; LTM derived |
| Purchases of property, plant and equipment | 377.4 | 231.6 | 268.7 | 115.7 | 78.7 | 414.5 | Same pages; LTM derived |
| Purchases of intangible assets | 57.0 | 42.2 | 37.0 | 17.0 | 4.3 | 51.8 | Same pages; LTM derived |
| Free cash flow (company definition) | 245.9 | 203.4 | 319.6 | 150.7 | 210.6 | 362.1 | Q3 release `page:12` for the 2025 and 2026 interim periods; FY2025 and LTM derived |
| Adjusted free cash flow (company definition) | Not supplied: FY2025 not in the pack | 535.5 | 602.9 | 311.1 | 274.2 | Not supplied: FY2025 base missing | Q3 release `page:12` |
| Cash paid for interest, net of interest capitalized | 303.1 | 204.8 | 200.4 | 51.8 | 52.1 | 298.7 | 10-K `page:128`; Q3 10-Q `page:7`; LTM derived |
| Cash paid for income taxes | 56.9 | 56.8 | 112.0 | 2.4 | 37.4 | 112.1 | Same pages; LTM derived |
| Dividends paid to common stockholders | 151.3 | 113.2 | 131.2 | 37.2 | 43.5 | 169.3 | Cash flow statements; LTM derived |
| Common stock repurchased and cancelled | 421.5 | 296.8 | 70.1 | 75.8 | 22.3 | 194.8 | Cash flow statements; LTM derived |
| Cash, cash equivalents and restricted cash, period end | 376.9 | 423.6 | 477.4 | 423.6 | 477.4 | 477.4 | Balance sheets and cash flow statements |
| Unrestricted cash, period end | 376.7 | Not supplied: Sep 30, 2025 balance sheet not in the pack | 477.2 | Not supplied: same reason | 477.2 | 477.2 | 10-K `page:151`; Q3 release `page:14` |
| Total debt, balance sheet (current plus long-term) | 5,157.9 | Not supplied: same reason | 5,162.1 | Not supplied: same reason | 5,162.1 | 5,162.1 | 10-K `page:155`; Q3 10-Q `page:4` |
| Debt before unamortized costs and discounts | 5,249.1 | Not supplied: same reason | 5,249.7 | Not supplied: same reason | 5,249.7 | 5,249.7 | FY2025 derived (see Calculations); Sep 30 as printed, Q3 release `page:14` |
| Net debt | 4,872.4 | Not supplied: same reason | 4,772.5 | Not supplied: same reason | 4,772.5 | 4,772.5 | FY2025 derived; Sep 30 as printed |
| Total debt / Adjusted EBITDA (x) | 3.63 | Not calculable: nine-month EBITDA is not annual | Not calculable: nine-month EBITDA is not annual | Not calculable: quarterly EBITDA is not annual | Not calculable: quarterly EBITDA is not annual | 3.66 | LTM or annual basis only |
| Net debt / Adjusted EBITDA (x) | 3.37 | Not calculable: nine-month EBITDA is not annual | Not calculable: nine-month EBITDA is not annual | Not calculable: quarterly EBITDA is not annual | Not calculable: quarterly EBITDA is not annual | 3.32 | LTM figure as printed in the Q3 release |
| Total debt / EBITDA (x) | 4.85 | Not calculable: nine-month EBITDA is not annual | Not calculable: nine-month EBITDA is not annual | Not calculable: quarterly EBITDA is not annual | Not calculable: quarterly EBITDA is not annual | 4.34 | Derived on EBITDA before add-backs |
| Net debt / EBITDA (x) | 4.50 | Not calculable: nine-month EBITDA is not annual | Not calculable: nine-month EBITDA is not annual | Not calculable: quarterly EBITDA is not annual | Not calculable: quarterly EBITDA is not annual | 3.95 | Derived on EBITDA before add-backs |
| Adjusted EBITDA / cash interest (x) | 4.77 | 5.43 | 5.50 | 7.81 | 7.89 | 4.81 | Derived; interim periods are not annualized |
| Adjusted EBITDA / interest and financing expense, net (x) | 4.43 | 4.50 | 4.60 | 4.87 | 5.14 | 4.50 | Derived; expense basis |
| Covenant first lien net leverage and interest coverage | Not supplied | Not supplied | Not supplied | Not supplied | Not supplied | Not supplied | Levels are printed (5.00 to 1.00 and 2.00 to 1.00, Q3 10-Q `page:17`); the reported ratios are not |

### Discrete quarters (US$m)

Q1 2026, Q2 2026 and Q3 2026 and their 2025 comparatives are printed in the quarterly reports and releases; Q4 2025 is derived as FY2025 less nine months 2025. The 2025 interim figures are on the continuing-operations basis the 2026 reports use.

| Quarter | Net sales | Adjusted EBITDA | Adjusted EBITDA margin (%) | Net income from continuing operations | Source |
| --- | --- | --- | --- | --- | --- |
| Q1 2025 | 1,613.7 | 341.5 | 21.2 | 34.7 | Q1 release `page:1`; Q1 10-Q `page:5` |
| Q2 2025 | 1,730.1 | 366.7 | 21.2 | 30.5 | Q2 release `page:1` |
| Q3 2025 | 1,766.1 | 404.5 | 22.9 | 40.5 | Q3 release `page:1` |
| Q4 2025 (derived) | 1,554.1 | 334.1 | 21.5 | -25.3 | FY2025 less nine months 2025; margin derived |
| Q1 2026 | 1,626.1 | 306.0 | 18.8 | 27.3 | Q1 release `page:1` |
| Q2 2026 | 1,796.2 | 385.0 | 21.4 | 69.2 | Q2 release `page:1` |
| Q3 2026 | 1,821.0 | 411.0 | 22.6 | 124.5 | Q3 release `page:1` |

The three 2026 quarters sum to nine-month net sales of 5,243.3 (1,626.1 plus 1,796.2 plus 1,821.0) and to nine-month Adjusted EBITDA of 1,102.0 (306.0 plus 385.0 plus 411.0), which agree with the nine-month figures in the Q3 release.

### Net sales by water type (US$m)

| Category | Q3 2026 | Q3 2025 | Nine months 2026 | Nine months 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- |
| Regional spring water | 911.5 | 885.6 | 2,623.7 | 2,554.8 | 3,319.9 | 3,234.5 |
| Purified water | 573.6 | 557.5 | 1,640.9 | 1,617.5 | 2,102.0 | 1,348.7 |
| Premium water | 122.1 | 98.2 | 341.8 | 259.6 | 349.9 | 94.8 |
| Other water | 31.8 | 33.0 | 94.1 | 103.0 | 128.8 | 140.7 |
| Other | 182.0 | 191.8 | 542.8 | 575.0 | 763.4 | 333.8 |
| Total net sales | 1,821.0 | 1,766.1 | 5,243.3 | 5,109.9 | 6,664.0 | 5,152.5 |

Source: Q3 10-Q `page:22` and `page:45`, `page:48`; 10-K `page:86`. FY2024 is not like-for-like with FY2025 because Primo Water is included only from November 9, 2024 (10-K `page:84`). The nine-month 2026 growth in premium water was 82.2 and in regional spring water 68.9, partly offset by a decline of 21.7 from the exited US office coffee services business (Q3 10-Q `page:49`). Sales in the United States were 98.6% of consolidated net sales for both the quarter and nine months 2026 (Q3 10-Q `page:22`). One customer made up about 21% of net sales and about 20% of trade receivables at December 31, 2025 (10-K `page:112`); that disclosure was not found restated in the Q3 10-Q.

### Balance sheet (US$m)

Source: Q3 10-Q `page:4` and `page:5` and 10-K `page:126`.

| Line | Sep 30, 2026 | Dec 31, 2025 |
| --- | --- | --- |
| Cash, cash equivalents and restricted cash | 477.4 | 376.9 |
| Trade receivables, net | 563.1 | 431.8 |
| Inventories | 264.9 | 223.5 |
| Prepaid expenses and other current assets | 197.4 | 148.9 |
| Current assets held for sale | 25.3 | 36.7 |
| Total current assets | 1,528.1 | 1,217.8 |
| Property, plant and equipment, net | 2,123.8 | 2,185.5 |
| Operating lease right-of-use assets, net | 584.7 | 539.3 |
| Goodwill | 3,612.0 | 3,581.9 |
| Intangible assets, net | 2,885.3 | 2,992.7 |
| Total assets | 10,828.0 | 10,602.8 |
| Current portion of long-term debt | 74.4 | 73.3 |
| Trade payables | 539.6 | 518.9 |
| Accruals and other current liabilities | 681.8 | 597.6 |
| Current portion of operating lease obligations | 83.6 | 92.9 |
| Total current liabilities | 1,379.4 | 1,282.7 |
| Long-term debt, less current portion | 5,087.7 | 5,084.6 |
| Operating lease obligations, less current portion | 528.5 | 474.4 |
| Deferred income taxes | 696.3 | 691.5 |
| Total liabilities | 7,779.3 | 7,610.2 |
| Total stockholders' equity | 3,048.7 | 2,992.6 |

Accumulated deficit was (1,992.4) against (2,014.5), so equity carries a deficit alongside 5,049.9 of additional paid-in capital. Goodwill and intangible assets together were 6,497.3 at September 30, 2026 (3,612.0 plus 2,885.3), which is 60.0% of total assets, so book equity of 3,048.7 rests on acquisition accounting from the 2024 combination.

### Debt, all instruments

The registrant is Primo Brands Corporation. Borrowers and issuers are subsidiaries, set out in the table. Amounts are carrying values in the Q3 10-Q fair-value table (`page:30`) unless a principal is stated; the notes lines in that table are net of unamortized discount, so the table total (5,017.5) is not a principal total.

| Instrument | Issuer or borrower | Amount | Rate | Maturity | Security and guarantors | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Term Loans (Refinancing Term Facility) | Primo Brands Corporation as parent borrower; Triton Water Holdings, Inc. and Primo Water Holdings Inc. as borrowers | 3,090.0 at March 31, 2026; carrying 3,074.5 at Sep 30, 2026 (fair value 3,090.0) | SOFR plus 2.75%, SOFR floor 0.50% | March 2031; 1.00% a year amortization in equal quarterly instalments | First lien; guarantors are the other guarantors party to the credit agreement; the term loans are secured by a first-priority lien on substantially all assets of the issuers and guarantors (10-K `page:95`) | Q3 10-Q `page:16`, `page:30` |
| Revolving Credit Facility | Borrowers under the same credit agreement | Commitments 750.0; letters of credit 163.4; loans not itemized at Sep 30, 2026; nil at Dec 31, 2025 | SOFR plus 1.50% to 2.25% by first lien net leverage; commitment fee 0.20% to 0.30% (10-K `page:157`, `page:158`; pre-Fifth Amendment text) | February 2030, subject to a springing maturity whose conditions are not stated | Same credit agreement; letters of credit sublimit 250.0 and swing line 150.0 (10-K `page:157`) | Q3 10-Q `page:17`, `page:51` |
| 3.875% Senior Secured Notes | Co-issued by Primo Water Holdings Inc. and Triton Water Holdings, Inc. | EUR 441.9 million (519.8 at Dec 31, 2025 rates); carrying 495.9 at Sep 30, 2026 | 3.875% | October 31, 2028 | Senior secured, first lien pari passu with the credit agreement (10-K `page:98`); guaranteed by the Company and substantially all wholly-owned domestic subsidiaries (10-K `page:160`) | Q3 10-Q `page:30`; 10-K `page:160` |
| 4.375% Senior Secured Notes | Co-issued by the same two issuers | 746.5 principal; carrying 721.4 at Sep 30, 2026 | 4.375% | April 30, 2029 | Senior secured, first lien pari passu (10-K `page:98`); guaranteed by the Guarantors | Q3 10-Q `page:30`; 10-K `page:160` |
| 6.250% Senior Notes | Co-issued by the same two issuers | 712.8 | 6.250% | April 1, 2029 | Senior unsecured (10-K `page:99`); guaranteed by the Company and certain subsidiaries (10-K `page:159`) | Q3 10-Q `page:30`; 10-K `page:159` |
| Non-tendered Original Senior Notes | Primo Water Holdings Inc. and Triton Water Holdings, Inc. (original issuers) | 12.9 carrying | As the original notes | Original maturities | Covenants largely removed and, for the original 3.875% and 4.375% notes, guarantees released by supplemental indentures (10-K `page:158`) | Q3 10-Q `page:30` |
| Finance leases | Company | Not itemized at Sep 30, 2026; 170.8 at Dec 31, 2025 (current 36.9, long-term 133.9) | Weighted-average discount rate 6.2% at Dec 31, 2025 | Weighted-average remaining term 9.4 years at Dec 31, 2025 | Lessor claims on leased assets | 10-K `page:153` |
| Other debt | Company | Not itemized at Sep 30, 2026; 31.7 at Dec 31, 2025, which includes the non-tendered original notes of 13.3 | Not stated | Through the 2030s: 11.5 falls after 2030 (10-K `page:155`) | Not stated | 10-K `page:155` |

Total debt on the balance sheet at September 30, 2026 is 5,162.1 (74.4 current plus 5,087.7 long-term), and the company's debt before unamortized costs and discounts of 87.6 is 5,249.7 (Q3 release `page:14`). The first lien claims that rank with the Revolving Credit Facility therefore include the term loan and the two secured note series. Hedges: forward contracts of EUR 450.0 million notional (510.6 at Sep 30, 2026 rates) maturing November 1, 2027 hedge the Euro Notes, so the hedge ends before the October 31, 2028 maturity; two float-to-fixed interest rate swaps of 250.0 each, maturing December 31, 2026 and December 31, 2027, hedge 500.0 of term loan principal (Q3 10-Q `page:54`). The ratings printed in the Q3 10-Q (`page:53`) are Corporate / Family "B1" and "BB-", Senior Secured "Ba3" and "BB", Senior Unsecured "B3" and "B", with "Outlook Positive Neutral"; they are company-reported statements, not independent rating documents.

### Maturity ladder as reported at December 31, 2025 (US$m)

Source: 10-K `page:104`, `page:105`, which agrees with the debt note ladder on `page:155`. It predates the March 2026 refinancing and excludes finance leases and unamortized costs.

| Instrument | 2026 | 2027 | 2028 | 2029 | 2030 | Thereafter | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Term Loans (matured March 31, 2028 at that date) | 31.0 | 31.0 | 3,005.7 | none | none | none | 3,067.7 |
| 3.875% Senior Notes | none | none | 519.7 | none | none | none | 519.7 |
| 4.375% Senior Notes | none | none | none | 746.5 | none | none | 746.5 |
| 6.250% Senior Notes | none | none | none | 712.8 | none | none | 712.8 |
| Other debt | 4.9 | 1.3 | 9.8 | 3.9 | 0.2 | 11.5 | 31.6 |
| Revolving Credit Facility | none | none | none | none | none | none | none |
| Total | 35.9 | 32.3 | 3,535.2 | 1,463.2 | 0.2 | 11.5 | 5,078.3 |

The table prints a dash where nothing is due; "none" here is that dash, not a zero carried into any calculation. The 2028 term loan balloon of 3,005.7 no longer exists at that date after the March 2026 refinancing to March 2031 (Q3 10-Q `page:16`), which is why the derived ladder in the chart data above is used for the current wall. The contractual obligations table also shows interest payments of 816.0 over all years, of which 320.9 in 2026, and finance lease payments of 229.8 (10-K `page:105`).

### Covenants

| Covenant | Level | Reported figure | Headroom | Source |
| --- | --- | --- | --- | --- |
| Revolving Credit Facility: first lien net leverage ratio | At most 5.00 to 1.00, with no step-downs and a 0.50 to 1.00 step-up for any four-quarter period in which a material acquisition is consummated | Not supplied | Not calculable on the credit agreement definition | Q3 10-Q `page:17`, `page:53` |
| Revolving Credit Facility: interest coverage ratio | At least 2.00 to 1.00 at the end of each fiscal quarter | Not supplied | Not calculable on the credit agreement definition | Q3 10-Q `page:17`, `page:53` |
| Term Loans and indentures | Negative covenants only (debt, liens, restricted payments, asset sales, affiliate transactions); covenants substantially similar across the note series and largely fall away under an investment grade rating | Not applicable | Not applicable | Q3 10-Q `page:17`, `page:18` |

The company states it "was in compliance with all covenants under the agreements governing its indebtedness as of September 30, 2026" (`page:18`). A management-basis proxy, labelled as such and not the credit agreement definition, is given in `## Calculations`: the proxy first lien net leverage is 2.68 times and the proxy interest coverage on the expense basis is 4.50 times. The covenant definition of EBITDA, the treatment of unrestricted cash and the debt included are not supplied, so the proxy shows direction only.

### Claims outside the debt figure

| Claim | Amount and period | Inside or outside the debt figure | Source |
| --- | --- | --- | --- |
| Operating lease obligations | 612.1 at Sep 30, 2026 (83.6 current plus 528.5 long-term); 567.3 at Dec 31, 2025; undiscounted payments 707.9 at Dec 31, 2025 | Outside; operating lease expense is already deducted in EBITDA | Q3 10-Q `page:4`; 10-K `page:153` |
| Finance leases | 170.8 at Dec 31, 2025; not itemized at Sep 30, 2026; cash principal payments of 29.6 in nine months 2026 | Inside the balance-sheet debt total and inside the company's net leverage numerator | 10-K `page:153`, `page:155`; Q3 10-Q `page:7` |
| Leases not yet commenced | 75.2 of minimum payments over 5 to 15 years for three leases entered in Q1 2026 (37.8 for five leases at Dec 31, 2025) | Outside | Q1 10-Q `page:33`; 10-K `page:153` |
| Purchase obligations | 187.1 at Dec 31, 2025 (92.1 in 2026); Q3 10-Q gives no amount | Outside | 10-K `page:105`, `page:106` |
| Postretirement benefits | 7.7 of undiscounted obligations at Dec 31, 2025; Note 16 describes defined contribution plans and split-dollar life insurance arrangements (10-K `page:175`) | Outside | 10-K `page:105` |
| Letters of credit | 163.4 outstanding at Sep 30, 2026 (137.4 at Dec 31, 2025) | Outside the debt total; reduces revolver availability | Q3 10-Q `page:38`, `page:51` |
| Property and casualty insurance reserves | 199.2 at Dec 31, 2025 within accruals; not itemized at Sep 30, 2026 | Outside | 10-K `page:154` |
| Securities class action (City of Miami Fire Fighters) | Damages not specified; motion to dismiss fully briefed and pending | Outside, unquantified | Q3 10-Q `page:35` |
| Consumer class action (Hamilton) | Seeks to represent potentially 600,000 customers; damages not specified; motions to compel arbitration and to dismiss pending | Outside, unquantified | Q3 10-Q `page:36`, `page:37` |
| Spring-water labelling class action (Patane) | Damages sought on a price-premium and statutory basis; mediation on September 3, 2026 did not settle it; second mediation scheduled for November 19, 2026 | Outside, unquantified | Q3 10-Q `page:37`, `page:38` |
| Factoring, supply chain finance, securitization, defined benefit pension plans, environmental remediation or consent decree funding | None identified; searches of the 10-K and the Q3 10-Q for these terms found no arrangement | Not applicable | Search of both filings |

The company states it is "unable to reasonably estimate the amount or range of possible loss, if any, in excess of the amounts accrued" (Q3 10-Q `page:34`). A warehouse tornado in Q2 2025 produced incremental costs of 19.8 and capital costs of 33.8 in the nine months 2025, against insurance proceeds of 10.0 in cost of sales and 20.0 in investing cash flow (Q3 10-Q `page:38`, `page:39`); the filing gives no 2026 amounts.

### Latest quarter and events to the cutoff

- Financing. The Fifth Amendment of March 31, 2026 refinanced term loans of 3,067.6 into 3,090.0 maturing March 2031, a net principal increase of 22.4, with a loss on modification and extinguishment of debt of 17.7 in nine months 2026 (Q3 10-Q `page:16`, `page:17`). No financing event on debt occurred in Q3 2026; term loan repayments were 7.8 (Q3 10-Q `page:7`).
- Equity. On August 7, 2026 the sponsor affiliate Triton Water Equity Holdings sold 20,000,000 shares at 24.37 a share in a secondary offering, and the company bought back 410,340 shares from it for about 10.0 funded from cash; the company received no offering proceeds (Q3 10-Q `page:19`, `page:61`).
- After quarter end. On November 3, 2026 the board declared a dividend of 0.12 a share payable December 4, 2026 and approved a new share repurchase program of up to 300.0, replacing the existing program that had 40.8 of authorization left at September 30, 2026 (Q3 10-Q `page:39`).
- Outlook. The Q3 release expects net sales at the midpoint of the previous 2% to 4% growth range and Adjusted EBITDA at the lower end of the previous 1,465 to 1,515 range, with base capital expenditure of 4% of net sales and Adjusted Free Cash Flow of 790 to 810 unchanged (Q3 release `page:2`). In May 2026 the Adjusted EBITDA range was widened from 1,485 to 1,515 to 1,465 to 1,515 (Q1 release `page:2`), and in August it was reaffirmed (Q2 release `page:2`). These are attributed management claims and are not reconciled to GAAP (Q3 release `page:6`).
- Restructuring. Management expected aggregate restructuring charges of about 75.0 to 100.0 in connection with the 2024 combination, and no further cash termination benefits are expected (Q3 10-Q `page:23`).

### Interpretation

#### Leverage

Net debt fell to 4,772.5 at September 30, 2026 from 4,872.4 at December 31, 2025, a decrease of 99.9, while trailing Adjusted EBITDA fell to 1,436.1 from 1,446.8. Net leverage on the company's definition was therefore 3.32 times against 3.37 times, a small improvement that comes from cash rising by 100.5 rather than from earnings growth; gross debt before unamortized costs was nearly unchanged at 5,249.7 against 5,249.1. Leverage was higher at the March and June 2026 test dates (3.52 and 3.42 times net) because unrestricted cash (287.9 and 366.5) and trailing Adjusted EBITDA (1,411.3 and 1,429.6) were both lower then. On unadjusted EBITDA, which includes integration costs and unrealized gains, trailing leverage is 4.34 times gross and 3.95 times net, so the difference between the two bases, 0.68 times gross and 0.63 times net, measures how much of the credit story rests on add-backs. The add-backs fell from 365.1 in FY2025 to 124.4 in nine months 2026, which supports management's view that integration costs are winding down (Q3 10-Q `page:49`), but the "other adjustments, net" line is still 11.5 in nine months 2026 against (5.0) in nine months 2025 (Q3 release `page:11`).

#### Coverage

Adjusted EBITDA covered cash interest 4.81 times over the trailing twelve months and covered interest and financing expense, net 4.50 times. Interest and financing expense, net for nine months 2026 was 239.5, 3.1% lower than 247.1 a year earlier (Q3 10-Q `page:50`), even though the term loan margin rose to 2.75% from 2.25% at the refinancing (Q3 10-Q `page:16`; 10-K `page:156`); the swaps fix the rate on 500.0 of the term loans and one of them ends December 31, 2026. Cash interest paid of 200.4 was below the expense of 239.5 for nine months; non-cash amortization of debt discount and issuance costs of 21.5 (Q3 10-Q `page:6`) explains part, and the timing of semi-annual coupons in April and October (10-K `page:159`, `page:160`) is a consistent but unstated explanation for the rest, which is an inference. These ratios are not the covenant measure.

#### Cash flow quality

Operating cash flow from continuing operations was 625.3 for nine months 2026, up 148.1. The company attributes this to improved earnings excluding non-cash charges of 80.1 and an increase in cash provided by trade payables and accruals of 141.1, partly offset by larger uses for prepaid assets, receivables and inventories (Q3 10-Q `page:58`). A payables-driven gain can reverse. Receivables absorbed 163.5 in nine months 2026 against 133.4, and cash paid for income taxes rose to 112.0 from 56.8. Free cash flow was 319.6 against 203.4. Dividends of 131.2 and buybacks of 70.1 took 201.3 of it, leaving 118.3, about 37% of free cash flow, while cash rose by 100.5. The adjusted free cash flow of 602.9 adds back 146.3 of acquisition, integration and restructuring cash costs and 101.8 of integration capital expenditure among other items (Q3 release `page:12`), so the gap between free cash flow and adjusted free cash flow of 283.3 is itself management-defined. Purchases of property, plant and equipment and intangibles were 305.7 for nine months 2026, 5.8% of net sales; the outlook's "Base CAPEX" of 4% of net sales is a separate management measure, so the two are not directly comparable.

#### Liquidity

Cash of 477.2 plus revolver availability of 586.6 gives 1,063.8, against current portion of long-term debt of 74.4 and nine-month cash interest of 200.4. The revolver matures February 2030, so no facility expires within twelve months, but the springing maturity condition is not stated and could shorten it. The company states that it does not expect to generate sufficient cash from operations to repay at maturity the entirety of its debt and so depends on refinancing (Q3 10-Q `page:51`). The revolver is assumed undrawn because the filing speaks of "undrawn availability" and no revolver borrowing line appears in the financing cash flows; that is an inference.

#### Earnings quality and definitions

Adjusted EBITDA is defined by management as net income from continuing operations before interest, taxes and depreciation and amortization, adjusted for acquisition, integration and restructuring expenses, stock-based compensation, unrealized gains and losses on foreign exchange and commodity forwards, loss on disposal of property, plant and equipment, debt modification losses, purchase accounting and other adjustments (Q3 10-Q `page:43`). Four points matter. First, the integration add-back of 91.2 for nine months 2026 is larger than the statement line of 47.5 because 43.7 of integration cost sits in cost of sales (Q3 release `page:11`, `page:12`). Second, Q3 2026 operating income of 248.9 includes other operating income of 28.0, of which 27.6 is unrealized gains on commodity forwards (Q3 10-Q `page:47`); Adjusted EBITDA removes 26.1 of unrealized gains, against unrealized gains of 27.6 in Q3 2026 and 1.8 in Q3 2025 in operating income, so part of the rise in operating income is a mark-to-market swing. Third, depreciation and amortization fell to 146.3 from 163.1 in Q3 2026, mainly because amortization of customer lists and definite-lived trade names fell to 30.1 from 56.1 (Q3 release `page:12`), which lifts net income without any cash effect. Fourth, FY2025 Adjusted EBITDA excluded insurance proceeds of 47.3 and added back an intangible asset impairment of 35.6 (10-K `page:86`). The effective tax rate was 28.4% for nine months 2026 against 36.4% (Q3 10-Q `page:50`).

#### Capital allocation

The company paid dividends of 0.12 a share each quarter in 2026 and authorized a new 300.0 repurchase program after quarter end; its sponsor affiliate sold 20,000,000 shares in August 2026 and the company bought back 410,340 shares from it. Management states a focus on generating cash flow and reducing net leverage (Q3 release `page:1`), and repurchases of 70.1 and dividends of 131.2 in nine months 2026 sit alongside it.

### Correction to the earlier handoff

The readiness review described the difference between the debt before unamortized costs in the Q3 release (5,249.7) and the fair-value table total (5,017.5), 232.2, as debt the Q3 report does not itemize. That wording is too strong. The notes lines of the fair-value table are carried net of unamortized discounts (the 10-K states discounts of 7.5 on the 3.875% notes and 31.7 on the 4.375% notes at December 31, 2025, `page:155`), while the term loan line is principal. The 232.2 therefore mixes finance leases, other debt not in the table and note discounts. It is still not decomposed in the Q3 10-Q, and the gap about finance leases, other debt and the revolver balance stands, but the 232.2 should not be read as unitemized debt.

## Calculations

All inputs are from the cited statements; derived values are labelled. USD millions. Ratios are to two decimals and percentages to one decimal unless a source prints more.

| Item | Formula and inputs | Result | Period and perimeter |
| --- | --- | --- | --- |
| LTM net sales | 6,664.0 - 5,109.9 + 5,243.3 | 6,797.4 | LTM Sep 30, 2026, consolidated |
| LTM gross profit | 2,020.2 - 1,590.1 + 1,567.5 | 1,997.6 | Same |
| LTM SG&A | 1,390.4 - 1,049.4 + 998.5 | 1,339.5 | Same |
| LTM acquisition, integration and restructuring expenses | 167.5 - 133.7 + 47.5 | 81.3 | Same |
| LTM operating income | 430.4 - 412.4 + 567.2 | 585.2 | Same |
| LTM interest and financing expense, net | 326.5 - 247.1 + 239.5 | 318.9 | Same |
| LTM net income from continuing operations | 80.4 - 105.7 + 221.0 | 195.7 | Same |
| LTM depreciation and amortization | 610.2 - 437.0 + 429.5 | 602.7 | Same |
| LTM provision for income taxes | 64.6 - 60.4 + 87.6 | 91.8 | Same |
| LTM EBITDA tie | 195.7 + 318.9 + 91.8 + 602.7 | 1,209.1, equal to 1,081.7 - 850.2 + 977.6 | Same |
| LTM Adjusted EBITDA | 1,446.8 - 1,112.7 + 1,102.0 | 1,436.1, equal to the Q3 release `page:14` | Same |
| LTM add-backs | 1,436.1 - 1,209.1 | 227.0, which is 18.8% of LTM EBITDA | Same |
| FY2025 add-backs | 1,446.8 - 1,081.7 | 365.1, which is 33.8% of FY2025 EBITDA | FY2025 |
| Nine-month 2026 add-backs | 1,102.0 - 977.6 | 124.4, which is 12.7% of EBITDA | Nine months 2026 |
| Nine-month 2025 add-backs | 1,112.7 - 850.2 | 262.5 | Nine months 2025 |
| Q3 add-backs | 411.0 - 396.9 and 404.5 - 313.1 | 14.1 (Q3 2026); 91.4 (Q3 2025) | Quarters |
| Integration add-back vs statement line | 47.5 + 43.7 (cost of sales); 16.7 + 7.0 | 91.2 and 23.7, equal to the release add-backs | Nine months and Q3 2026 |
| Net sales growth | 1,821.0 / 1,766.1 - 1; 5,243.3 / 5,109.9 - 1 | 3.1% (Q3); 2.6% (nine months) | Q3 and nine months 2026 |
| Adjusted EBITDA growth | 411.0 / 404.5 - 1; 1,102.0 / 1,112.7 - 1 | 1.6% (Q3); -1.0% (nine months) | Q3 and nine months 2026 |
| EBITDA growth | 396.9 / 313.1 - 1 | 26.8% | Q3 2026 |
| Gross margin | 1,997.6 / 6,797.4 (LTM); 2,020.2 / 6,664.0 (FY2025) | 29.4% (LTM); 30.3% (FY2025) | Derived |
| Adjusted EBITDA margin | 1,436.1 / 6,797.4; 1,446.8 / 6,664.0 | 21.1% (LTM); 21.7% (FY2025) | Derived |
| Q4 2025 net sales | 6,664.0 - 5,109.9 | 1,554.1 | Q4 2025, derived |
| Q4 2025 Adjusted EBITDA | 1,446.8 - 1,112.7 | 334.1; margin 334.1 / 1,554.1 = 21.5% | Q4 2025, derived |
| Q4 2025 net income from continuing operations | 80.4 - 105.7 | -25.3 | Q4 2025, derived |
| Quarter sums, 2026 | 1,626.1 + 1,796.2 + 1,821.0; 306.0 + 385.0 + 411.0 | 5,243.3; 1,102.0, equal to the nine-month figures | Nine months 2026 |
| Interest tie, 2026 | 78.3 + 81.3 + 79.9 | 239.5, equal to the nine-month figure | Nine months 2026 |
| Balance sheet debt | 74.4 + 5,087.7 | 5,162.1, equal to the release "Total debt" | Sep 30, 2026 |
| Debt before unamortized costs | 5,162.1 + 87.6 | 5,249.7, equal to the release | Sep 30, 2026 |
| Net debt | 5,249.7 - 477.2 | 4,772.5, equal to the release | Sep 30, 2026 |
| Gross leverage, Sep 30, 2026 | 5,249.7 / 1,436.1 | 3.66x | LTM Adjusted EBITDA basis |
| Net leverage, Sep 30, 2026 | 4,772.5 / 1,436.1 | 3.32x, equal to the release | LTM Adjusted EBITDA basis |
| Gross and net leverage on unadjusted EBITDA | 5,249.7 / 1,209.1; 4,772.5 / 1,209.1 | 4.34x; 3.95x | LTM EBITDA basis |
| Debt before unamortized costs, Dec 31, 2025 | 5,078.3 (ladder total, 10-K `page:155`) + 170.8 (finance leases) | 5,249.1; cross-check 5,157.9 + 52.0 + 7.5 + 31.7 = 5,249.1 (balance-sheet debt, unamortized costs, and discounts netted in the notes lines) | Dec 31, 2025 |
| Net debt, Dec 31, 2025 | 5,249.1 - 376.7 | 4,872.4 | Dec 31, 2025 |
| Gross and net leverage, Dec 31, 2025 | 5,249.1 / 1,446.8; 4,872.4 / 1,446.8 | 3.63x; 3.37x | FY2025 Adjusted EBITDA basis |
| Leverage on unadjusted FY2025 EBITDA | 5,249.1 / 1,081.7; 4,872.4 / 1,081.7 | 4.85x; 4.50x | FY2025 EBITDA basis |
| Gross leverage, Mar 31 and Jun 30, 2026 | 5,255.1 / 1,411.3; 5,250.0 / 1,429.6 | 3.72x; 3.67x (net 3.52x and 3.42x as printed) | LTM at each date, from the releases |
| Change in net debt | 4,772.5 - 4,872.4 | -99.9 | Dec 31, 2025 to Sep 30, 2026 |
| Cash increase | 477.2 - 376.7 | 100.5, equal to the cash flow statement increase of 100.5 | Nine months 2026 |
| Cash interest, LTM | 303.1 - 204.8 + 200.4 | 298.7 | LTM |
| Cover on cash interest | 1,436.1 / 298.7; 1,446.8 / 303.1; 1,209.1 / 298.7; 1,081.7 / 303.1 | 4.81x; 4.77x; 4.05x; 3.57x | LTM and FY2025 |
| Interim cover on cash interest | 1,102.0 / 200.4; 1,112.7 / 204.8; 411.0 / 52.1; 404.5 / 51.8 | 5.50x; 5.43x; 7.89x; 7.81x | Interim periods, not annualized |
| Cover on expense | 1,436.1 / 318.9; 1,446.8 / 326.5; 1,102.0 / 239.5; 1,112.7 / 247.1; 411.0 / 79.9; 404.5 / 83.1 | 4.50x; 4.43x; 4.60x; 4.50x; 5.14x; 4.87x | Expense basis |
| LTM cash flow items | CFO 680.3 - 477.2 + 625.3; PP&E 377.4 - 231.6 + 268.7; intangibles 57.0 - 42.2 + 37.0 | 828.4; 414.5; 51.8 | LTM |
| LTM free cash flow | 828.4 - 414.5 - 51.8 | 362.1 | LTM |
| FY2025 free cash flow | 680.3 - 377.4 - 57.0 | 245.9 | FY2025 |
| Shareholder returns | 131.2 + 70.1 | 201.3, which is 63% of free cash flow of 319.6; remainder 118.3 | Nine months 2026 |
| LTM dividends and buybacks | 151.3 - 113.2 + 131.2; 421.5 - 296.8 + 70.1 | 169.3; 194.8 | LTM |
| Working capital contribution | CFO increase 625.3 - 477.2 | 148.1, of which payables and accruals 135.3 - (-5.8) = 141.1, as the MD&A states | Nine months 2026 |
| Capital spending | 268.7 + 37.0 | 305.7, which is 5.8% of net sales of 5,243.3 | Nine months 2026 |
| Liquidity, Sep 30, 2026 | 477.2 + (750.0 - 163.4) | 1,063.8 | Revolver loans assumed nil |
| Liquidity at other dates | 376.7 + (750.0 - 137.4); 287.9 + (750.0 - 163.9); 366.5 + (750.0 - 163.4) | 989.3; 874.0; 953.1 | Dec 31, 2025; Mar 31, 2026; Jun 30, 2026 |
| Goodwill and intangibles share | (3,612.0 + 2,885.3) / 10,828.0 | 6,497.3, which is 60.0% of total assets | Sep 30, 2026 |
| Term loan principal roll | 3,090.0 less repayments of 7.7 (Q2 2026) and 7.8 (Q3 2026) | 3,074.5, equal to the carrying value on `page:30`; 1.00% on 3,090.0 is 7.725 a quarter | Sep 30, 2026 |
| Euro note conversion | 510.6 x 441.9 / 450.0 | 501.4 | Sep 30, 2026 rate implied by `page:54` |
| Derived ladder | Term loan: 7.725 (Q4 2026); 30.9 a year 2027 to 2030; 3,074.5 - 7.725 - 4 x 30.9 = 2,943.2 in 2031. Notes: 501.4 (2028); 712.8 + 746.5 (2029) | Q4 2026 7.7; 2027 30.9; 2028 532.3; 2029 1,490.2; 2030 30.9; 2031 2,943.2; total 5,035.2 = 3,074.5 + 501.4 + 712.8 + 746.5 | Pro forma, excludes finance leases and other debt |
| Management-basis first lien proxy | (3,074.5 + 501.4 + 746.5 - 477.2) / 1,436.1 | 2.68x; numerator 3,845.2; not the covenant definition | Sep 30, 2026 |
| Outlook arithmetic | 1,465 - 1,102.0; 1,515 - 1,102.0 | 363.0 to 413.0 implied for Q4 2026 Adjusted EBITDA; 790 - 602.9 and 810 - 602.9 = 187.1 to 207.1 implied for Q4 Adjusted Free Cash Flow; arithmetic on guidance, not a forecast | Q4 2026 |
| Indicative leverage on guidance | 5,249.7 / 1,465; 4,772.5 / 1,465 | 3.58x; 3.26x, at the lower end of the range | Mixed: dated debt, forecast EBITDA |

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Covenant first lien net leverage and interest coverage ratios, definitions and headroom are not printed (searched "first lien net leverage" and "interest coverage" in all seven sources); only levels and a compliance statement are printed | Headroom is not calculable; the proxy ratios in Calculations show direction only | Obtain the executed credit agreement with the Fifth Amendment and the quarterly compliance figures |
| Finance leases, other debt and the revolver balance are not itemized at September 30, 2026; the last itemized view is December 31, 2025 | The Sep 30 debt composition below the term loan and notes is a residual; the revolver is assumed undrawn | Use the December 31, 2025 table as the last itemized view; check the next filing |
| No filed maturity ladder after the March 2026 refinancing; the derived ladder uses an implied euro rate and ignores any excess cash flow prepayment (50% sweep, subject to leverage reductions, described pre-refinancing in the 10-K `page:94`) | The 2028 and 2029 wall figures are derived and could shift with FX and prepayments | Label as derived; confirm against the next filing |
| Springing maturity condition on the revolver is not stated | The effective revolver maturity could be earlier than February 2030 | Read the credit agreement |
| Executed credit agreement, Fifth Amendment, indentures and guarantor schedules are not in the pack; the revolver pricing in this handoff is from the pre-Fifth Amendment 10-K text | Security, guarantor perimeter and current revolver margin rest on filing summaries | Obtain the executed documents |
| The Q4 2025 release (the source of the company's year-end ratio) and FY2025 Adjusted Free Cash Flow are not in the pack | FY2025 company-basis leverage and adjusted free cash flow are derived or Not supplied | Rely on the derived FY2025 ratios, labelled |
| Q4 2025 is derived as FY2025 less nine months 2025 | Small risk if prior-period amounts were reclassified (Q3 10-Q `page:10`) | Labelled as derived |
| Sep 30, 2025 balance sheet is not in the pack | Year-ago net debt and leverage are not available | None needed for the base |
| Purchase obligations, property and casualty reserves and customer concentration are given only as of December 31, 2025 | Q3 values are Not supplied | Carry as FY2025 context |
| The three class actions have no estimate of possible loss beyond amounts accrued; the Patane second mediation (November 19, 2026) and the Hamilton scheduling conference (November 12, 2026) fall after the cutoff | Possible cash cost is unquantified | Carry as open contingent claims |
| Ratings are printed by the company in the 10-Q; the context leaves them blank | Ratings are an issuer-reported statement | Use only as such |
| Earnings presentations are not in the pack | No chart or slide content was read | None needed for the base |
| Adjusted EBITDA is a management measure with the add-backs shown above | Leverage on the adjusted basis is lower than on the unadjusted basis | Show both bases, as done |

## Next module

Proceed to CP-1A for the business and transaction context, with these carry-forwards: one registrant and one segment; leverage of 3.66 times gross and 3.32 times net on management Adjusted EBITDA and 4.34 and 3.95 times on unadjusted EBITDA; the March 2026 refinancing of the term loan to March 2031 and the derived 2028 and 2029 note wall; liquidity of 1,063.8 with an assumed undrawn revolver; the pending 300.0 buyback program and dividend declared after quarter end; the three class actions without loss estimates; and the covenant, guarantor and post-refinancing schedule gaps. CP-2 should keep the covenant headroom gap open, treat the 232.2 residual as mixed (see the correction above), and not cite the proxy ratios as reported covenant figures.
