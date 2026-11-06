# CP-1 - Financial base: FAIR ISAAC CORP (fico)

## Request

- Issuer: FAIR ISAAC CORP (Fair Isaac Corporation, NYSE "FICO", issuer id `fico`), as of 2026-11-05, information cutoff 2026-11-05.
- Scope: financial base view for the credit snapshot: reported statements, debt, liquidity, maturities, cash flow, and analyst-constructed leverage and cover, each with its basis. No credit rating view or recommendation.
- Currency and periods: USD, as the filings report. Statements are in US$ thousands as printed; chart tables are in US$m. The context names current period q3-2026 and prior period fy-2025. FICO's fiscal year ends September 30: fiscal Q3 2026 is the quarter ended June 30, 2026; FY2025 is the year ended September 30, 2025; "9M" is the nine months to June 30; "LTM Q3 FY2026" is the twelve months to June 30, 2026. No other currency or period is reported.
- Handoff consumed: CP-0 readiness (limitations carried forward below). CP-0 recorded no company-defined EBITDA, no stated revolver availability and second and third quarter cash flows given year to date only. This answer builds EBITDA and undrawn capacity as labelled analyst constructions from filed lines, which narrows two of those gaps without removing them. It does not contradict CP-0.
- Execution: host session, no provider call. Every figure comes from the pinned sources; locators are `page:N` chunks of the named jsonl file.

## Sources

| Source (exact name) | sha256 | Use |
| --- | --- | --- |
| 10-K_2025-09-30_fico-20250930.htm.jsonl | 2cd0fc2b16386652e87f31c986fda43ca1da2a923ef1840b57f765a69322682e | Audited FY2025 and FY2024 statements, debt note, contractual obligations, leases |
| 10-Q_2025-12-31_fico-20251231.htm.jsonl | 905bfc6e05d39d56e0eed3225e1079b7eb97528806ef0d9d2d8efa0e76893510 | Q1 FY2026 statements and comparatives (three months to December 31, 2025) |
| 10-Q_2026-03-31_fico-20260331.htm.jsonl | 1d56011f469dd7f9f01c0afabb2cc5e52bf600c9b61e1e02a22c20a1382a76cb | Q2 FY2026 statements, six-month cash flow |
| 10-Q_2026-06-30_fico-20260630.htm.jsonl | 9928c89c8cd74e2a4ae5180bf504e58edee7d7a0cfbf531e71dc30f830e9f9a7 | Q3 FY2026 statements, nine-month cash flow, debt, covenant text, liquidity |
| EX-99.1_2026-01-28_exhibit991erq12026.htm.jsonl | 7ff326f8e766ed76e0e346c09be22d1a6689de853a63261725535c212fd1ea11 | Q1 FY2026 release; not relied on for figures beyond the 10-Q |
| EX-99.1_2026-04-28_exhibit991erq22026.htm.jsonl | 98fcf8141dae7e420bccc2579f8ef67af179818384ed4fb3d51d12d1c6831d98 | Q2 FY2026 release; guidance history only |
| EX-99.1_2026-07-29_exhibit991erq32026.htm.jsonl | 4bcf15097cd5d352a02b7a02cc65369e0e3cdadccda74b9b84b0c06bd098be52 | Q3 FY2026 release: discrete quarter operating cash flow, free cash flow, guidance |
| context | 67fd10ada0c60e1a58280c6938025b16a97aebcc1d2e25ac2914a3e17b05c7a0 | User run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | bf1dc2c14187a6208c7ecc4cc4dcd1ace42a402c8c8aa295e5e74d0134c7d3d4 | Source readiness, located pages and gaps (no executed financing documents, no EBITDA measure, no evidence after July 29, 2026) |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Operating results are strong, but debt rose to US$5,582.4m at June 30, 2026 as buybacks were debt funded. Analyst leverage reached 4.46x, close to the stated covenant ceiling. | Medium | No company EBITDA or covenant ratio is reported, and the credit agreement definitions are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt rose by US$2,526.7m in nine months while nine-month buybacks were US$3,046.0m against free cash flow of US$750.0m. | Shareholder returns, not operations, drove the higher debt and the stockholders' deficit. | High |
| Analyst total debt to EBITDA rose from 3.25x at FY2025 to 4.46x; the stated covenant maximum is 4.5x until December 30, 2026, then 4.0x. | Headroom is thin on the analyst measure; the covenant definition may differ. | Medium |
| Interest paid in the last twelve months was US$164.9m, but annualised contractual interest on June 30, 2026 balances is US$316.5m. | Reported cover of 7.60x overstates the run-rate, which is about 3.96x. | Medium |
| Cash is US$248.4m and the undrawn revolver is US$290.0m before any letters of credit; US$300.0m of term loan falls due within twelve months. | Liquidity covers the near-term term loan amortisation, with little surplus. | Medium |
| Revenue growth is concentrated in Scores, driven by mortgage origination score pricing. | Cash generation depends on one segment and one pricing action. | Medium |

### Financial base view

FICO's operations generate strong, growing cash flow, but the June 30, 2026 balance sheet is a different credit from the one at FY2025. In nine months, with total debt rising by US$2,526.7m, the company drew a new US$1,500.0m term loan, issued US$1,000.0m of 2034 notes, repaid the US$400.0m 2018 notes and borrowed further on the revolver, taking total debt from US$3,055.7m to US$5,582.4m. The proceeds funded US$3,046.0m of share repurchases, including a US$1,500.0m accelerated share repurchase, far above free cash flow. On an analyst EBITDA of operating income plus depreciation and amortisation, total debt to EBITDA moved from 3.25x to 4.46x, and cash interest cover from 9.07x to 7.60x on a lagging cash-paid basis. Interest on the new debt is only partly in the last twelve months, so the run-rate burden is materially higher than reported cash interest. The main limits are the absence of a company-defined EBITDA or covenant ratio, the absence of the credit agreement, and the absence of anything after the July 29, 2026 filings. Of the term loan, US$300.0m falls due within twelve months. The base is sufficient to run the downstream modules with these limits stated.

| Dimension | Base view (figures from the Financials table below) | Limitation |
| --- | --- | --- |
| Earnings | LTM Q3 FY2026 revenue US$2,393.6m and analyst EBITDA US$1,252.4m | EBITDA is operating income plus cash flow statement D&A; no add-backs; not a company measure |
| Leverage | Total debt to EBITDA 4.46x; net 4.26x at June 30, 2026 | Carrying value of debt; covenant definition not supplied |
| Coverage | EBITDA to cash interest paid 7.60x LTM; 3.96x on annualised contractual interest | Cash interest lags new borrowings; run-rate excludes fees and floating-rate resets |
| Liquidity | Cash US$248.4m plus undrawn revolver US$290.0m | Letters of credit not disclosed; US$139.8m of cash is held by foreign subsidiaries |
| Maturities | US$75.0m in FY2026, US$337.5m in FY2027, US$1,987.5m in FY2028 | Derived from stated term loan amortisation; credit agreement not supplied |
| Cash flow | 9M FY2026 operating cash flow US$777.9m, free cash flow US$750.0m | Free cash flow after capitalised software; buybacks exceed it |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 2.96 | 2.75 | x | Debt at carrying value at September 30, 2024 (10-K page:103); EBITDA is operating income plus cash flow D&A for FY2024 (10-K page:89, page:90); analyst construction, no add-backs |
| FY2025 | 3.25 | 3.11 | x | Debt at September 30, 2025 (10-K page:103); EBITDA FY2025 (10-K page:89, page:90); analyst construction |
| LTM Q1 FY2026 | 3.21 | 3.05 | x | Debt at December 31, 2025 (10-Q page:9); LTM to December 31, 2025 built from FY2025 plus three months FY2026 less three months FY2025; analyst construction |
| LTM Q2 FY2026 | 3.16 | 2.97 | x | Debt at March 31, 2026 (10-Q page:10); LTM to March 31, 2026 from six-month figures; analyst construction |
| LTM Q3 FY2026 | 4.46 | 4.26 | x | Debt at June 30, 2026 (10-Q page:10); LTM to June 30, 2026 from nine-month figures; EBITDA includes no pro forma credit for the June 2026 term loan; not the covenant ratio, whose definition is not supplied |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 7.03 | x | Analyst EBITDA over cash paid for interest, US$106.4m (10-K page:90); cash interest is gross of interest income |
| FY2025 | 9.07 | x | Analyst EBITDA over cash paid for interest, US$103.6m (10-K page:90) |
| LTM Q1 FY2026 | 7.17 | x | Cash interest LTM built from FY2025 plus three months FY2026 less three months FY2025 (Q1 FY2026 10-Q page:4); semi-annual coupon timing makes quarters uneven |
| LTM Q2 FY2026 | 8.48 | x | Cash interest LTM from six-month figures (10-Q Q2 page:5) |
| LTM Q3 FY2026 | 7.60 | x | Cash interest LTM US$164.9m (10-Q page:5); lags the new debt; annualised contractual interest is US$316.5m, which gives 3.96x (see Calculations) |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 150.7 | 390.0 | US$m | Cash from 10-K page:88; undrawn is the US$600m revolver commitment before the May 2025 increase (10-K page:74) less US$210.0m drawn (10-K page:103); derived; letters of credit not disclosed |
| FY2025 | 134.1 | 725.0 | US$m | Cash 10-K page:88; undrawn is the US$1.0bn revolver less US$275.0m drawn (10-K page:74, page:103); derived; letters of credit not disclosed |
| Q1 FY2026 (Dec 31, 2025) | 162.0 | 585.0 | US$m | Cash 10-Q page:2; undrawn is the US$1.0bn revolver less US$415.0m drawn (10-Q page:9, page:10); derived |
| Q2 FY2026 (Mar 31, 2026) | 219.4 | 735.0 | US$m | Cash 10-Q page:2; undrawn is the US$1.0bn revolver less US$265.0m drawn (10-Q page:10, page:11); derived |
| Q3 FY2026 (Jun 30, 2026) | 248.4 | 290.0 | US$m | Cash 10-Q page:2, of which US$139.8m held by foreign subsidiaries (10-Q page:33); undrawn is the US$1.0bn revolver less US$710.0m drawn (10-Q page:10, page:11); the term loan was borrowed in full so adds no undrawn amount; derived; letters of credit not disclosed |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2026 | 75.0 | US$m | Term loan instalment due September 30, 2026 (10-Q page:11); position at June 30, 2026; events after the 10-Q are Not supplied |
| FY2027 | 337.5 | US$m | Term loan instalments of US$75.0m on three dates to June 30, 2027 and US$112.5m on September 30, 2027 (10-Q page:11); derived schedule |
| FY2028 | 1987.5 | US$m | Term loan: two instalments of US$112.5m plus balance of US$862.5m at the May 15, 2028 maturity, US$1,087.5m; plus 2019 and 2021 Senior Notes of US$900.0m due June 15, 2028 (10-Q page:11, page:12); derived |
| FY2029 | 0 | US$m | No instrument in the June 30, 2026 debt note matures in this fiscal year (10-Q page:10 to page:12) |
| FY2030 | 710.0 | US$m | Revolving line of credit drawn balance, maturing May 13, 2030 (10-Q page:11); a revolver can be repaid or redrawn earlier |
| FY2031 | 0 | US$m | No instrument in the June 30, 2026 debt note matures in this fiscal year |
| FY2032 | 0 | US$m | No instrument in the June 30, 2026 debt note matures in this fiscal year |
| FY2033 | 1500.0 | US$m | 2025 Senior Notes, 6.00%, due May 15, 2033 (10-Q page:12) |
| FY2034 | 1000.0 | US$m | 2026 Senior Notes, 6.25%, due September 15, 2034 (10-Q page:12) |

Total of the rows is US$5,610.0m face value, against US$5,582.4m carrying value after US$27.6m of unamortised issuance costs (10-Q page:10).

### Financials and credit metrics

Amounts are US$ thousands as printed unless the unit column says otherwise. Balance items are at the period end (September 30 for FY columns; June 30, 2026 for the 9M FY2026 and LTM columns). LTM Q3 FY2026 = FY2025 + 9M FY2026 - 9M FY2025.

| Metric | Unit | FY2024 | FY2025 | 9M FY2025 | 9M FY2026 | LTM Q3 FY2026 | Basis and source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenues | US$ thousands | 1,717,526 | 1,990,869 | 1,475,118 | 1,877,824 | 2,393,575 | Reported (10-K page:89; 10-Q page:2) |
| Scores segment revenues | US$ thousands | 919,650 | 1,168,575 | 857,023 | 1,238,404 | 1,549,956 | Reported (10-K page:89; 10-Q page:2) |
| Software segment revenues | US$ thousands | 797,876 | 822,294 | 618,095 | 639,420 | 843,619 | Software plus professional services lines, equal to the segment total (10-K page:89; 10-Q page:19) |
| Operating income | US$ thousands | 733,629 | 924,850 | 687,694 | 999,142 | 1,236,298 | Reported (10-K page:89; 10-Q page:2, page:3) |
| Depreciation and amortization | US$ thousands | 13,827 | 14,952 | 10,931 | 12,123 | 16,144 | Cash flow statement (10-K page:90; 10-Q page:4) |
| EBITDA (analyst) | US$ thousands | 747,456 | 939,802 | 698,625 | 1,011,265 | 1,252,442 | Operating income plus D&A; calculated; not a company measure |
| Share-based compensation | US$ thousands | 149,439 | 156,667 | 124,288 | 141,910 | 174,289 | Cash flow statement (10-K page:90; 10-Q page:4) |
| EBITDA plus share-based compensation (alternative) | US$ thousands | 896,895 | 1,096,469 | 822,913 | 1,153,175 | 1,426,731 | Calculated sensitivity; add-back is an analyst choice |
| Interest expense, net | US$ thousands | 105,638 | 133,647 | 93,765 | 146,462 | 186,344 | Reported (10-K page:89; 10-Q page:3) |
| Cash paid for interest | US$ thousands | 106,388 | 103,564 | 101,112 | 162,420 | 164,872 | Supplemental cash flow (10-K page:90; 10-Q page:5) |
| Cash paid for income taxes, net | US$ thousands | 133,716 | 162,089 | 129,078 | 162,882 | 195,893 | Supplemental cash flow (10-K page:90; 10-Q page:5) |
| Net income | US$ thousands | 512,811 | 651,946 | 496,932 | 660,003 | 815,017 | Reported (10-K page:89; 10-Q page:3) |
| Net cash provided by operating activities | US$ thousands | 632,964 | 778,807 | 555,138 | 777,880 | 1,001,549 | Reported (10-K page:90; 10-Q page:4) |
| Capital expenditure (property plus capitalised software) | US$ thousands | 25,551 | 39,407 | 26,582 | 27,846 | 40,671 | Sum of two cash flow lines (10-K page:90; 10-Q page:4) |
| Free cash flow | US$ thousands | 607,413 | 739,400 | 528,556 | 750,034 | 960,878 | Operating cash flow less the capex above; calculated |
| Repurchases of common stock (cash) | US$ thousands | 821,702 | 1,414,502 | 866,520 | 3,045,992 | 3,593,974 | Financing cash flow (10-K page:90; 10-Q page:4) |
| Cash and cash equivalents | US$ thousands | 150,667 | 134,136 | Not supplied | 248,444 | 248,444 | Balance sheet (10-K page:88; 10-Q page:2); June 30, 2025 balance sheet not in the pack |
| Total debt (carrying value) | US$ thousands | 2,209,021 | 3,055,691 | Not supplied | 5,582,389 | 5,582,389 | Debt note (10-K page:103; 10-Q page:10) |
| Net debt | US$ thousands | 2,058,354 | 2,921,555 | Not supplied | 5,333,945 | 5,333,945 | Total debt less cash; calculated |
| Total stockholders' deficit | US$ thousands | (962,679) | (1,745,784) | Not supplied | (4,097,135) | (4,097,135) | Balance sheet (10-K page:89; 10-Q page:2) |
| Total debt / EBITDA | x | 2.96 | 3.25 | Not applicable (LTM measure) | Not applicable (LTM measure) | 4.46 | Calculated; analyst EBITDA |
| Net debt / EBITDA | x | 2.75 | 3.11 | Not applicable (LTM measure) | Not applicable (LTM measure) | 4.26 | Calculated; analyst EBITDA |
| EBITDA / cash interest paid | x | 7.03 | 9.07 | Not applicable (LTM measure) | Not applicable (LTM measure) | 7.60 | Calculated |
| Total debt / (EBITDA plus share-based compensation) | x | 2.46 | 2.79 | Not applicable (LTM measure) | Not applicable (LTM measure) | 3.91 | Calculated sensitivity |
| Covenant maximum consolidated leverage ratio | x | Not supplied | 3.5 | Not supplied | 4.5 | 4.5 | Stated maximum (10-K page:75; 10-Q page:11); 4.0 from December 31, 2026 and 3.5 from December 31, 2027; reported ratio and definition Not supplied |

### Reported debt at June 30, 2026

| Instrument | Face value (US$ thousands) | Rate | Maturity | Security | Source |
| --- | --- | --- | --- | --- | --- |
| Revolving line of credit (US$1.0bn commitment) | 710,000 | 5.643% weighted average | May 13, 2030 | Unsecured | 10-Q page:10, page:11, page:12 |
| Term loan (borrowed June 5, 2026) | 1,500,000 | 5.863% | May 15, 2028, with quarterly amortisation | Unsecured | 10-Q page:10, page:11, page:12 |
| 2019 Senior Notes and 2021 Senior Notes (one class) | 900,000 | 4.00% | June 15, 2028 | Described as typical of unsecured obligations | 10-Q page:12 |
| 2025 Senior Notes | 1,500,000 | 6.00% | May 15, 2033 | As above | 10-Q page:12 |
| 2026 Senior Notes (issued March 20, 2026) | 1,000,000 | 6.25% | September 15, 2034 | As above | 10-Q page:12 |
| Less unamortised debt issuance costs | (27,611) | not applicable | not applicable | not applicable | 10-Q page:10 |
| Total debt, carrying value | 5,582,389 | not applicable | not applicable | not applicable | 10-Q page:10 |

The 2018 Senior Notes of US$400.0m were repaid in full on March 26, 2026 (10-Q page:12). Fair value of the Senior Notes at June 30, 2026 was US$3,333.5m against face value of US$3,400.0m (10-Q page:12). Issuer and borrower are the registrant; guarantors are Not supplied (no source mentions a guarantor).

### Claims outside reported debt

| Claim | Amount | Inside or outside the debt figure | Source |
| --- | --- | --- | --- |
| Finance leases at September 30, 2025 | US$7,207 thousand (current 3,266 plus non-current 3,941) | Outside; in other accrued liabilities and other liabilities | 10-K page:124 |
| Operating leases at September 30, 2025 | US$28,802 thousand | Outside | 10-K page:124 |
| Non-cancellable purchase obligations at September 30, 2025 | US$99,248 thousand | Outside | 10-K page:125 |
| Unrecognised tax benefits at June 30, 2026 | US$23.2m | Outside | 10-Q page:17 |
| Pension and retiree medical | Not supplied | A search of every source for pension, retiree and postretirement returned no match | Not applicable |
| Accelerated share repurchase prepayment | US$300.0m equity-linked contract, settlement expected in fiscal Q4 2026 | Outside debt; equity | 10-Q page:13 |
| Litigation | Putative class action alleging antitrust claims; no accrual or amount stated | Outside | 10-Q page:43; 10-Q page:20 |

Lease balances after September 30, 2025 are not itemised in the 10-Q read for this module; the June 30, 2026 balance sheet shows operating lease liabilities of US$15.6m non-current (10-Q page:2).

### Quarter and post-quarter events

- Fiscal Q3 2026 financing: on "June 5, 2026, we amended our credit agreement to provide for the issuance of a $1.5 billion unsecured term loan" (10-Q page:11), and the same date an accelerated share repurchase of US$1.5bn with Wells Fargo Securities, with US$300.0m prepaid and settlement "expected to occur during the fourth quarter of fiscal 2026" (10-Q page:13).
- Fiscal Q3 2026 discrete results from the release: revenues US$674.2m, operating cash flow US$380.4m, free cash flow US$370.3m (release page:1, page:5). Interest expense, net was US$59,877 thousand against US$32,899 thousand a year earlier (10-Q page:3).
- Earlier in FY2026: US$1,000.0m of 2026 Senior Notes on March 20, 2026 and repayment of the 2018 notes on March 26, 2026 (10-Q page:12).
- Guidance (management, forward-looking): updated fiscal 2026 revenues of US$2.53 billion, GAAP net income US$850 million (release page:2).
- Subsequent events: none are listed in any source; nothing dated after July 29, 2026 is supplied, so the September 30, 2026 term loan instalment, the ASR settlement and fiscal Q4 results are Not supplied.

### Interpretation: evidence, mechanism, implication

#### Debt-funded capital return

- Evidence: total debt carrying value rose from US$3,055,691 thousand to US$5,582,389 thousand (10-K page:103; 10-Q page:10), while cash repurchases were US$3,045,992 thousand in nine months (10-Q page:4) and "Repurchases of common stock (1,706) (17) (300,000) (1,978,927)" appears in the fiscal Q3 equity statement (10-Q page:3).
- Mechanism: buybacks run at a multiple of free cash flow, so each repurchase round is financed by borrowing; the term loan was drawn for the ASR (10-Q page:22: "the proceeds of which were used to fund an accelerated share repurchase agreement").
- Credit implication: leverage is a management choice that can be reversed only by slowing repurchases or by EBITDA growth; the stockholders' deficit of US$4,097,135 thousand carries no equity cushion. Management language that the credit agreement permits repurchases (10-Q page:11) is a permission, not a commitment to deleverage.

#### Leverage against covenant

- Evidence: analyst total debt to EBITDA 4.46x at June 30, 2026 against a stated maximum "of 4.5 to 1.0 through December 30, 2026, 4.0 to 1.0 during December 31, 2026 through December 30, 2027" (10-Q page:11); "we were in compliance with all financial covenants" (10-Q page:12).
- Mechanism: the step down to 4.0x on December 31, 2026 and 3.5x on December 31, 2027 shrinks permitted leverage unless EBITDA grows or debt is repaid; the term loan amortises US$75.0m a quarter. The covenant definition is not supplied, so the analyst ratio is context, not a test.
- Credit implication: on a measure that adds back share-based compensation the ratio is 3.91x; on the plain measure it is 4.46x. Headroom is Not calculable until the credit agreement definition is obtained; the range indicates headroom is thin to moderate before the first step down.

#### Interest burden

- Evidence: last twelve months cash interest US$164,872 thousand; contractual annualised interest on June 30, 2026 balances is US$316,510 thousand (Calculations). Interest expense, net for nine months rose to US$146,462 thousand from US$93,765 thousand (10-Q page:3).
- Mechanism: the term loan was drawn on June 5, 2026 and the 2026 notes on March 20, 2026, so only weeks to months of their interest are in the twelve-month figures; the term loan and revolver float over SOFR (10-Q page:41).
- Credit implication: forward cover is closer to 3.96x than 7.60x on unchanged EBITDA; floating-rate exposure applies to US$2,210.0m of borrowings (revolver plus term loan).

#### Revenue concentration in Scores

- Evidence: Scores revenue was US$458,897 thousand of US$674,188 thousand in fiscal Q3 2026 (10-Q page:2), and "The increase in business-to-business scores revenue was primarily attributable to a higher mortgage origination scores unit price" (10-Q page:26). Software revenue rose 2% in the quarter (10-Q page:25).
- Mechanism: earnings growth rests on pricing in one product line sold through credit reporting agencies and exposed to mortgage volumes and the antitrust claim (10-Q page:43).
- Credit implication: cash flow quality is high today but price-dependent; a pricing reversal would hit EBITDA and the covenant ratio at once.

## Calculations

All inputs are US$ thousands as printed unless marked.

### LTM construction

LTM Q3 FY2026 = FY2025 + 9M FY2026 - 9M FY2025.

| Item | FY2025 | 9M FY2026 | 9M FY2025 | LTM Q3 FY2026 |
| --- | --- | --- | --- | --- |
| Revenue | 1,990,869 | 1,877,824 | 1,475,118 | 1,990,869 + 1,877,824 - 1,475,118 = 2,393,575 |
| Operating income | 924,850 | 999,142 | 687,694 | 1,236,298 |
| D&A | 14,952 | 12,123 | 10,931 | 16,144 |
| Share-based compensation | 156,667 | 141,910 | 124,288 | 174,289 |
| Cash paid for interest | 103,564 | 162,420 | 101,112 | 164,872 |
| Operating cash flow | 778,807 | 777,880 | 555,138 | 1,001,549 |

The December 31, 2025 and March 31, 2026 LTM columns use the same method with three-month and six-month figures: operating income 234,049 and 179,528 (Q1 FY2026 and Q1 FY2025, 10-Q Q1 page:2), 636,514 and 425,176 (six months, 10-Q Q2 page:3); D&A 4,017 and 3,535 (Q1 page:3), 7,905 and 6,950 (Q2 page:4); cash interest 78,812 and 43,714 (Q1 page:4), 93,172 and 60,939 (Q2 page:5).

| Item | LTM Q1 FY2026 | LTM Q2 FY2026 |
| --- | --- | --- |
| Operating income | 924,850 + 234,049 - 179,528 = 979,371 | 924,850 + 636,514 - 425,176 = 1,136,188 |
| D&A | 14,952 + 4,017 - 3,535 = 15,434 | 14,952 + 7,905 - 6,950 = 15,907 |
| EBITDA | 994,805 | 1,152,095 |
| Cash interest | 103,564 + 78,812 - 43,714 = 138,662 | 103,564 + 93,172 - 60,939 = 135,797 |
| Total debt (balance sheet) | 3,196,829 | 3,639,063 |
| Cash | 162,034 | 219,419 |

### EBITDA, leverage and cover

- EBITDA = operating income + D&A. FY2024: 733,629 + 13,827 = 747,456. FY2025: 924,850 + 14,952 = 939,802. 9M FY2025: 687,694 + 10,931 = 698,625. 9M FY2026: 999,142 + 12,123 = 1,011,265. LTM Q3 FY2026: 1,236,298 + 16,144 = 1,252,442.
- Total debt / EBITDA: FY2024 2,209,021 / 747,456 = 2.96x; FY2025 3,055,691 / 939,802 = 3.25x; LTM Q1 3,196,829 / 994,805 = 3.21x; LTM Q2 3,639,063 / 1,152,095 = 3.16x; LTM Q3 5,582,389 / 1,252,442 = 4.46x.
- Net debt: FY2024 2,209,021 - 150,667 = 2,058,354; FY2025 3,055,691 - 134,136 = 2,921,555; Q1 3,196,829 - 162,034 = 3,034,795; Q2 3,639,063 - 219,419 = 3,419,644; Q3 5,582,389 - 248,444 = 5,333,945. Net debt / EBITDA: 2.75x, 3.11x, 3.05x, 2.97x, 4.26x.
- Cover = EBITDA / cash paid for interest: FY2024 747,456 / 106,388 = 7.03x; FY2025 939,802 / 103,564 = 9.07x; LTM Q1 994,805 / 138,662 = 7.17x; LTM Q2 1,152,095 / 135,797 = 8.48x; LTM Q3 1,252,442 / 164,872 = 7.60x.
- Sensitivity with share-based compensation added back: LTM Q3 1,252,442 + 174,289 = 1,426,731; 5,582,389 / 1,426,731 = 3.91x; FY2025 939,802 + 156,667 = 1,096,469; 3,055,691 / 1,096,469 = 2.79x.
- Face-value basis: the face total at June 30, 2026 is 710,000 + 1,500,000 + 3,400,000 = 5,610,000; 5,610,000 / 1,252,442 = 4.48x. The carrying basis is used in the charts.

### Annualised contractual interest at June 30, 2026

| Instrument | Balance | Rate | Annual interest |
| --- | --- | --- | --- |
| 2019 and 2021 Senior Notes | 900,000 | 4.00% | 36,000 |
| 2025 Senior Notes | 1,500,000 | 6.00% | 90,000 |
| 2026 Senior Notes | 1,000,000 | 6.25% | 62,500 |
| Revolver | 710,000 | 5.643% | 40,065 |
| Term loan | 1,500,000 | 5.863% | 87,945 |
| Total | 5,610,000 | not applicable | 316,510 |

EBITDA / annualised interest = 1,252,442 / 316,510 = 3.96x. Excludes credit agreement fees, issuance cost amortisation and interest income; rates are the weighted or stated June 30, 2026 rates and float.

### Liquidity and maturities

- Undrawn revolver: 1,000,000 - 710,000 = 290,000 at June 30, 2026; 1,000,000 - 415,000 = 585,000 at December 31, 2025; 1,000,000 - 265,000 = 735,000 at March 31, 2026; 1,000,000 - 275,000 = 725,000 at September 30, 2025; 600,000 - 210,000 = 390,000 at September 30, 2024. Cash plus undrawn at June 30, 2026: 248,444 + 290,000 = 538,444.
- Term loan schedule: instalments of 75,000 on September 30, 2026, December 31, 2026, March 31, 2027 and June 30, 2027 (300,000, matching "$300.0 million principal payments due on our term loan over the next 12 months", 10-Q page:33) then 112,500 on September 30, 2027, December 31, 2027 and March 31, 2028 (337,500), leaving 1,500,000 - 300,000 - 337,500 = 862,500 at May 15, 2028. By fiscal year: FY2026 75,000; FY2027 225,000 + 112,500 = 337,500; FY2028 225,000 + 862,500 = 1,087,500 plus notes 900,000 = 1,987,500. Sum of all rows: 75,000 + 337,500 + 1,987,500 + 710,000 + 1,500,000 + 1,000,000 = 5,610,000.
- Debt change: 5,582,389 - 3,055,691 = 2,526,698 over nine months; 5,582,389 - 3,639,063 = 1,943,326 in the quarter ended June 30, 2026.
- Buybacks less free cash flow, nine months FY2026: 3,045,992 - 750,034 = 2,295,958.

### Free cash flow and reconciliations

- Free cash flow = operating cash flow - (purchases of property and equipment + capitalised internal-use software). 9M FY2026: 777,880 - (1,355 + 26,491) = 750,034, against 750,035 printed by the release (release page:5), a rounding difference of 1. 9M FY2025: 555,138 - (4,751 + 21,831) = 528,556, equal to the release. FY2025: 778,807 - (8,922 + 30,485) = 739,400. FY2024: 632,964 - (8,884 + 16,667) = 607,413.
- Income statement block, 9M FY2026: revenues 1,877,824 - total operating expenses 878,682 = 999,142 operating income (10-Q page:2, page:3); FY2025: 1,990,869 - 1,066,019 = 924,850 (10-K page:89). Debt table: 300,000 + 5,282,389 = 5,582,389.
- Release and filing agree: "Total revenues 674,188 536,415 1,877,824 1,475,118" in both the 10-Q and the release.

## Gaps

| Gap | Severity | Affected | Action |
| --- | --- | --- | --- |
| No company-defined EBITDA, adjusted EBITDA or reported consolidated leverage ratio; covenant definition Not supplied | Medium | Leverage and covenant headroom | Headroom is Not calculable; obtain the credit agreement and any compliance certificate disclosure |
| Letters of credit drawn on the revolver are not disclosed; undrawn amount is derived from commitment less borrowings | Medium | Liquidity | Treat US$290.0m as an upper bound at June 30, 2026 |
| Credit agreement, First Amendment of June 5, 2026 and note indentures not supplied; the term loan schedule and guarantor position rest on 10-Q summary text | Medium | Maturities, security, guarantees | Obtain executed documents; guarantors Not supplied |
| Nothing after the July 29, 2026 filings: the September 30, 2026 instalment, ASR settlement, fiscal Q4 results and any later financing are Not supplied | Medium | All | Add fiscal Q4 release and 10-K when published |
| Jun 30, 2025 balance sheet is not in the pack, so 9M FY2025 balance items are Not supplied | Low | Trend | Use the FY2025 balance as comparator |
| Cash interest is lumpy by coupon date and lags new debt; interest burden is shown also on contractual run-rate | Low | Coverage | Interpret LTM cover with the run-rate |
| Lease balances after September 30, 2025 are not itemised; pension and retiree medical not found | Low | Claims outside debt | Not supplied |
| Antitrust litigation: no loss estimate or accrual is stated | Low | Contingent claims | Monitor; the 10-Q states no material exposure for reasonably possible losses (10-Q page:20) |
| Text extraction flattens tables; free cash flow, non-GAAP and guidance are management measures | Low | Reliability | 10-Q controls statement facts |

## Next module

Run CP-1A next on the business and transaction context, then CP-2 and CP-5. Carry forward: debt-funded buybacks and the 2026 financing events, analyst leverage of 4.46x on a plain EBITDA basis against a covenant maximum of 4.5x stepping down to 4.0x on December 31, 2026, run-rate interest of US$316.5m against LTM cash interest of US$164.9m, derived undrawn revolver of US$290.0m before letters of credit, and the absence of company EBITDA, executed financing documents and any evidence after July 29, 2026.
