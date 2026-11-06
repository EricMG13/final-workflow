# CP-1 — Financial base: Flutter Entertainment plc (flut)

## Request

- Issuer: Flutter Entertainment plc (issuer id `flut`), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026 (quarter and nine months ended September 30, 2026); prior period FY2025 (context). All amounts are US dollars in millions unless a ratio, percentage or per-unit figure is stated.
- Run: `flut-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, module CP-1. Execution: host session; the host read the pinned page text and wrote this answer. No provider was called.
- Question: what is the reported and derived financial base (statements, Adjusted EBITDA, leverage, cover, liquidity, maturities, cash flow) of the consolidated Flutter group at Q3 2026, and what limits it?
- Perimeter: Flutter Entertainment plc and its subsidiaries ("the Group"), consolidated, US GAAP, unaudited for 2026 interim periods and audited for FY2025, FY2024 and FY2023. No debt issuer is reported on a standalone basis.
- Locators are `page:N` of the pinned `.jsonl` text of each source, not printed page numbers. Source short names: 10-K = FY2025 annual report; Q1, Q2, Q3 10-Q = the 2026 quarterly reports; release = the Exhibit 99.1 earnings release for that quarter.
- Periods used: FY2024, FY2025, nine months ended September 30, 2025 (9M 2025) and 2026 (9M 2026), and last twelve months to September 30, 2026 (LTM Q3 2026 = FY2025 − 9M 2025 + 9M 2026). Interim LTM points use the same method. Derived values are labelled "calculated" and are shown in `## Calculations`.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_flut-20251231.htm.jsonl | b88acc6499b34409bd63bcc7ad6ada664ea0aaf382ca0ec0d2118e7c35eb580e | Audited FY2025, FY2024 and FY2023 statements, notes, segment note, debt note |
| 10-Q_2026-03-31_flut-20260331.htm.jsonl | 350d396101c8e01e25e223f0670d3e0363c6d230399db566cd885841329d1dbe | Q1 2026 statements, debt note, Adjusted EBITDA reconciliation |
| 10-Q_2026-06-30_flut-20260630.htm.jsonl | a6a0f970aa3d51a04b3c201b89aaae4625c229c4c7864888e69ca9462e615826 | Q2 2026 statements, debt note, Adjusted EBITDA reconciliation |
| 10-Q_2026-09-30_flut-20260930.htm.jsonl | cf209bd21d7ac9131f97943f724a2ebaf7232a79180602605a6b0908ae9a79a1 | Q3 2026 statements, debt note, segment note, MD&A, subsequent events |
| EX-99.1_2026-05-06_d46069dex991.htm.jsonl | 5416128bf3b9f4328a754a5eff0673c01006c996c64b406795c193ccb390bdfa | Q1 2026 release: net debt and leverage ratio statements |
| EX-99.1_2026-08-05_d127369dex991.htm.jsonl | 548ad754549966d85d0bb747ddc76468d7bd9635705b387877e25f59264aa63f | Q2 2026 release: net debt and leverage ratio statements |
| EX-99.1_2026-11-04_d141532dex991.htm.jsonl | ec2552a07ebcbae61da4247ec9d467815436158552ee8c98ff284c26331c74c1 | Q3 2026 release: net debt reconciliation, leverage ratio, guidance |
| context | c092a23c8bebb5c5ed118bc16d3658aa4f2c0513c724b7304133213e545208aa | User run settings; not issuer evidence |

| Handoff | Module | sha256 |
| --- | --- | --- |
| Source readiness | CP-0 | 6f50887cad81d339bbf86e29e4ef6f91bcf17a0cb9e2b4e94873f1133c5fcfda |

The CP-0 handoff was opened and used. It reports all four selected modules ready with limitations. This answer carries its limits forward: no executed credit documents, no covenant ratio values, the release leverage ratio and the covenant ratio use different definitions, and segment comparatives may not be recast. Where this answer settles a CP-0 question it says so under "Consistency with CP-0".

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Last-twelve-month Adjusted EBITDA of 2,331 against total debt of 12,313 gives total leverage of 5.28x and net leverage of 4.55x at Q3 2026, up from 4.31x and 3.67x at FY2025. | Medium | Adjusted EBITDA is the company's own measure, not the covenant definition, and the last-twelve-month figure is calculated from filed annual and interim data. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Adjusted EBITDA for nine months 2026 was 1,499 against 2,013 a year earlier, with the US segment falling most. | Debt is almost unchanged, so lower earnings drive the rise in leverage. | High |
| Cash interest cover on last-twelve-month Adjusted EBITDA is 3.67x, against 5.36x for FY2025. | Cash interest paid rose to 636 as the 2025 acquisition debt carried a full year of interest. | Medium |
| Free cash flow is positive at 515 for the last twelve months, but 319 once player deposit movements are removed. | Share repurchases of 543 exceeded free cash flow before the programme was paused. | Medium |
| Liquidity at September 30, 2026 was cash of 1,708 plus undrawn revolver commitments of 782, down from 1,828 and 929 at FY2025. | Headroom narrowed before the October 2026 amendment enlarged the revolver. | High |
| Add-backs for legal provisions, restructuring and Brazil impairment sit outside Adjusted EBITDA, and covenant EBITDA is defined separately. | Covenant headroom cannot be measured from these sources. | Low |

### Financial base view

The consolidated financial base is complete enough to use: audited FY2025 and FY2024 statements, three unaudited 2026 interim sets, a segment note, an Adjusted EBITDA reconciliation in every period and a debt note at each quarter end are all located. The picture they give is of a group whose total debt rose by 5,530 in 2025 (6,736 to 12,266, C13), with the proceeds of the 2025 term loan and note issues used to repay the bridge loans for the Snai acquisition and the Boyd transaction (10-K `page:126`), and whose earnings have since weakened. Adjusted EBITDA for nine months 2026 is 1,499 against 2,013 for nine months 2025, driven by the US segment (241 against 612) and a higher UK gaming duty in International, while total debt is almost flat (12,313 at September 30, 2026 against 12,266 at December 31, 2025). Calculated total debt to Adjusted EBITDA therefore rises from 4.31x at FY2025 to 5.28x on a last-twelve-month basis, and the company's own net leverage ratio moves from 3.7x to 4.6x. Cash interest cover on the same basis falls from 5.36x to 3.67x.

Three features limit the view. First, the headline measure is the company's Adjusted EBITDA, which excludes share-based compensation, restructuring, legal loss contingencies, transaction costs and impairment; the 10-Q says its definition `may not be the same as the definitions used in any of our debt agreements`. Second, the last-twelve-month figures are calculated from annual and year-to-date data, and the segment comparatives for 2025 appear not to be recast for the 2026 customer transfers between regions. Third, cash flow from operations moves with player deposit balances, which are not the Group's own cash. The figures should be read as a documented reported base with calculated overlays, not as covenant tests.

### Financials and credit metrics

| Metric (US$m unless stated) | FY2024 | FY2025 | 9M 2025 | 9M 2026 | LTM Q3 2026 | Source, basis and limitation |
| --- | --- | --- | --- | --- | --- | --- |
| Revenue | 14,048 | 16,383 | 11,646 | 12,504 | 17,241 | Reported: 10-K `page:146`; Q3 10-Q `page:6`. LTM calculated (C1). |
| Gross profit | 6,702 | 7,404 | 5,294 | 5,068 | 7,178 | Reported: 10-K `page:146`; Q3 10-Q `page:6`. LTM calculated. |
| Operating profit (loss) | 869 | 36 | (222) | (1,256) | (998) | Reported: 10-K `page:146`; Q3 10-Q `page:6`; after impairment. LTM calculated. |
| Impairment charges | Nil | 561 | 559 | 873 | 875 | FY2024 printed as a dash (nil) in the 10-K segment reconciliation (`page:168`); FY2025 `page:168`; 9M `page:14` of Q3 10-Q. LTM calculated. |
| Net income (loss) | 162 | (407) | (417) | (1,235) | (1,225) | Reported: 10-K `page:146`; Q3 10-Q `page:6`. LTM calculated. |
| Adjusted EBITDA (company definition) | 2,357 | 2,845 | 2,013 | 1,499 | 2,331 | Reported: 10-K `page:107`; Q3 10-Q `page:72`. Non-GAAP, not the covenant definition. LTM calculated (C1). |
| Adjusted EBITDA margin (%) | 16.8 | 17.4 | 17.3 | 12.0 | 13.5 | Reported for the first four columns (10-K `page:107`; Q3 10-Q `page:72`); LTM calculated as 2,331 divided by 17,241. |
| US segment Adjusted EBITDA | 507 | 922 | 612 | 241 | 551 | Reported: 10-K `page:168`; Q3 10-Q `page:14`. LTM calculated (C2). Comparatives not recast. |
| International segment Adjusted EBITDA | 2,065 | 2,202 | 1,614 | 1,498 | 2,086 | Reported: 10-K `page:168`; Q3 10-Q `page:14`. LTM calculated (C2). |
| Unallocated corporate overhead | (215) | (279) | (213) | (240) | (306) | Reported: 10-K `page:168`; Q3 10-Q `page:14`. LTM calculated (C2). |
| Depreciation and amortization | 1,097 | 1,517 | 1,082 | 1,220 | 1,655 | Reported: 10-K `page:148`; Q3 10-Q `page:9`. LTM calculated. |
| Interest expense, net | 419 | 515 | 347 | 477 | 645 | Reported: 10-K `page:146`; Q3 10-Q `page:6`. LTM calculated. |
| Cash interest paid | 462 | 531 | 321 | 426 | 636 | Reported supplemental cash flow: 10-K `page:149`; Q3 10-Q `page:10`. LTM calculated (C3). |
| Income tax paid, net of refunds | 255 | 445 | 326 | 293 | 412 | Reported: 10-K `page:149`; Q3 10-Q `page:10`. LTM calculated. |
| Net cash provided by operating activities | 1,602 | 1,184 | 756 | 904 | 1,332 | Reported: 10-K `page:148`; Q3 10-Q `page:9`. LTM calculated. Includes player deposit movements. |
| Player deposit movements within operating cash flow | 245 | (107) | (127) | 176 | 196 | Calculated (C4) from the two "Player deposits - investments" and "Player deposit liability" lines. |
| Operating cash flow excluding player deposit movements | 1,357 | 1,291 | 883 | 728 | 1,136 | Calculated (C4). |
| Capital expenditure (property, intangibles, capitalized software) | 661 | 777 | 487 | 527 | 817 | Calculated (C5) from three reported investing lines. Excludes intangible purchases with extended payment terms classified in financing (44 in 9M 2026; none printed for 9M 2025). |
| Free cash flow (operating cash flow less capital expenditure) | 941 | 407 | 269 | 377 | 515 | Calculated (C5); same definition as the release's free cash flow (Q3 release `page:27`). |
| Free cash flow excluding player deposit movements | 696 | 514 | 396 | 201 | 319 | Calculated (C5). |
| Repurchase of ordinary shares and taxes withheld on awards | 219 | 1,123 | 844 | 264 | 543 | Reported financing line: 10-K `page:149`; Q3 10-Q `page:9`. LTM calculated. |
| Total debt (carrying value, period end) | 6,736 | 12,266 | Not supplied: the September 30, 2025 balance sheet is not in the pack | 12,313 | 12,313 | Reported: 10-K `page:187`; Q3 10-Q `page:26`. Net of unamortized issuance costs. |
| Cash and cash equivalents (unrestricted, period end) | 1,531 | 1,828 | 1,727 | 1,708 | 1,708 | Reported: 10-K `page:145`; Q3 10-Q `page:5` and `page:10`. Excludes restricted cash and player deposits. |
| Net debt (carrying total debt less unrestricted cash) | 5,205 | 10,438 | Not supplied: no September 30, 2025 total debt | 10,605 | 10,605 | Calculated (C6). Differs from the release's net debt (10,656 at Q3 2026). |
| Total debt / Adjusted EBITDA (x) | 2.86 | 4.31 | Not calculable: nine-month flow, no period-end debt | Not calculable: nine-month flow, not annualised | 5.28 | Calculated (C7). |
| Net debt / Adjusted EBITDA (x) | 2.21 | 3.67 | Not calculable: nine-month flow, no period-end debt | Not calculable: nine-month flow, not annualised | 4.55 | Calculated (C7). Release ratio: 3.7x at December 31, 2025 and 4.6x at Q3 2026. |
| Adjusted EBITDA / cash interest paid (x) | 5.10 | 5.36 | Not calculable: nine-month flow | Not calculable: nine-month flow | 3.67 | Calculated (C7). |
| Adjusted EBITDA / interest expense, net (x) | 5.63 | 5.52 | Not calculable: nine-month flow | Not calculable: nine-month flow | 3.61 | Calculated (C7). |
| (Adjusted EBITDA less capital expenditure) / cash interest paid (x) | 3.67 | 3.89 | Not calculable: nine-month flow | Not calculable: nine-month flow | 2.38 | Calculated (C7). |
| Operating lease liabilities (current plus non-current, period end) | 547 | 606 | Not supplied: no September 30, 2025 balance sheet | 559 | 559 | Reported: 10-K `page:146`; Q3 10-Q `page:6`. Outside the debt figure and outside Adjusted EBITDA add-backs. |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 2.86 | 2.21 | x | Carrying total debt (6,736) and unrestricted cash (1,531) at December 31, 2024 over FY2024 company-defined Adjusted EBITDA (2,357). Calculated. Not a covenant test. |
| FY2025 | 4.31 | 3.67 | x | Total debt (12,266) and cash (1,828) at December 31, 2025 over FY2025 Adjusted EBITDA (2,845). Calculated. The release reports 3.7x on its own net debt definition. |
| LTM Q1 2026 | 4.18 | 3.65 | x | Total debt (11,965) and cash (1,512) at March 31, 2026 over LTM Adjusted EBITDA (2,860). Calculated. The Q1 release reports 3.7x. |
| LTM Q2 2026 | 4.89 | 4.25 | x | Total debt (11,978) and cash (1,563) at June 30, 2026 over LTM Adjusted EBITDA (2,449). Calculated. The Q2 release reports 4.3x. |
| LTM Q3 2026 | 5.28 | 4.55 | x | Total debt (12,313) and cash (1,708) at September 30, 2026 over LTM Adjusted EBITDA (2,331). Calculated. The Q3 release reports 4.6x on net debt of 10,656. Pre-amendment; the covenant uses a different EBITDA and net borrowings definition. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 5.10 | x | FY2024 Adjusted EBITDA (2,357) over cash interest paid (462). Calculated. |
| FY2025 | 5.36 | x | FY2025 Adjusted EBITDA (2,845) over cash interest paid (531). The 2025 acquisition debt carried interest for part of the year only, so the ratio flatters run-rate cover. |
| LTM Q1 2026 | 5.33 | x | LTM Adjusted EBITDA (2,860) over LTM cash interest paid (537). Calculated from year-to-date cash flow data. |
| LTM Q2 2026 | 3.83 | x | LTM Adjusted EBITDA (2,449) over LTM cash interest paid (639). Calculated. |
| LTM Q3 2026 | 3.67 | x | LTM Adjusted EBITDA (2,331) over LTM cash interest paid (636). Calculated. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| December 31, 2024 | 1,531 | Not supplied: the FY2024 annual report is not in the pack and the FY2025 report prints the undrawn revolver only at December 31, 2025 | US$m | Unrestricted cash and cash equivalents (10-K `page:145`). Excludes restricted cash and player deposits. |
| December 31, 2025 | 1,828 | 929 | US$m | Cash (10-K `page:145`); undrawn revolver `$929 million (£690 million)` (10-K `page:188`), of which 13 is reserved for guarantees. |
| March 31, 2026 | 1,512 | 1,185 | US$m | Cash (Q1 10-Q `page:4`); undrawn commitment `$1,185 million (£895 million)` (Q1 10-Q `page:20`), including 13 reserved for guarantees. |
| June 30, 2026 | 1,563 | 1,081 | US$m | Cash (Q2 10-Q `page:5`); undrawn commitment `$1,081 million (£815 million)` (Q2 10-Q `page:23`), including 13 reserved for guarantees. |
| September 30, 2026 | 1,708 | 782 | US$m | Cash (Q3 10-Q `page:5`); undrawn commitment `$782 million (£590 million)` (Q3 10-Q `page:27`), including 13 reserved for guarantees. Before the October 30, 2026 amendment, which lifts the commitment to `$1.86 billion` (`page:75`); the undrawn amount after the amendment is not supplied. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remainder of 2026 | 13 | US$m | Contractual principal repayments excluding accrued interest, as of September 30, 2026 (Q3 10-Q `page:26`). Pre-amendment schedule. |
| 2027 | 52 | US$m | Same table. Scheduled amortization. |
| 2028 | 2,681 | US$m | Same table. Includes the Term Loan A facilities and the revolver, which the October 30, 2026 amendment extends to May 3, 2032 (`page:42`). The pro forma split is Not calculable: the table does not itemise amounts by facility. |
| 2029 | 1,143 | US$m | Same table. |
| 2030 | 3,692 | US$m | Same table. |
| Thereafter | 4,696 | US$m | Same table; the sources print no year split for this bucket. Total of the table is 12,277, against 12,390 of principal including accrued interest in the debt note; the difference is not itemised. |

### Discrete quarters

| Quarter | Revenue | Adjusted EBITDA | Net income (loss) | Source and basis |
| --- | --- | --- | --- | --- |
| Q1 2025 | 3,665 | 616 | 335 | Q1 10-Q `page:53` comparatives. |
| Q2 2025 | 4,187 | 919 | 37 | Q2 10-Q `page:66` comparatives. |
| Q3 2025 | 3,794 | 478 | (789) | Q3 10-Q `page:72` and `page:6` comparatives. |
| Q4 2025 | 4,737 | 832 | 10 | Calculated (C8): FY2025 less 9M 2025. Not separately reported in the pack. |
| Q1 2026 | 4,304 | 631 | 209 | Q1 10-Q `page:53`. |
| Q2 2026 | 4,326 | 508 | (296) | Q2 10-Q `page:66`. |
| Q3 2026 | 3,874 | 360 | (1,148) | Q3 10-Q `page:72` and `page:6`. |

The three 2026 quarters sum to the nine-month figures printed in the Q3 10-Q (Adjusted EBITDA 1,499; net loss 1,235), and the three 2025 quarters sum to 2,013 and a net loss of 417 (C8). Q3 2026 net loss includes a Brazil impairment of 873 and a legal loss contingency add-back of 105 (Q3 10-Q `page:72` and `page:73`).

### Definition review

- Adjusted EBITDA is defined in the Q3 10-Q as `income (loss) before income taxes; other (expense) income, net; interest expense, net; depreciation and amortization; transaction fees and associated costs; restructuring and integration costs; legal (settlements) loss contingencies; gaming tax disputes; impairment of property and equipment, intangible assets, right-of-use assets and goodwill; and share-based compensation charge` (`page:70`). The 10-K notes that `Beginning January 1, 2024, the Group revised its definition of Adjusted EBITDA` (`page:99`); FY2024 and FY2023 figures in the 10-K are on the revised basis, and no earlier basis is supplied.
- Items excluded in the nine months to September 30, 2026 (Q3 10-Q `page:72`): share-based compensation 176, transaction fees 32, restructuring and integration costs 254, legal loss contingencies 200 and impairment 873. The restructuring programmes `are expected to run until 2029` (`page:73`), so the restructuring add-back is recurring in practice. Cash cost of the UKI restructuring, `$80 million to $90 million` pre-tax, is announced after quarter end (`page:42`) and is not in any period shown.
- Operating lease cost is inside Adjusted EBITDA (it is an operating expense), and operating lease liabilities sit outside debt. No finance lease balance is printed; the 10-K says `Substantially all leases are long-term operating leases` (`page:186`).
- Leverage definitions: the release defines `Leverage ratio is defined as net debt divided by last twelve months adjusted EBITDA` (Q3 release `page:21`). Its net debt adds back unamortized costs and removes unrealized foreign exchange on hedged debt (Q3 release `page:26`). This answer uses carrying total debt less unrestricted cash, so its net debt (10,605) is lower than the release's (10,656) by 51. The covenant ratio is `consolidated net borrowings to consolidated EBITDA as defined therein` with a limit of `5.20:1` before the October 30, 2026 amendment (10-K `page:128`) and a net first lien leverage level of `5.70:1.00` afterwards (Q3 10-Q `page:42`). No covenant ratio value is printed, so headroom is Not calculable.
- Cash interest paid is the supplemental cash flow line. It is not net of interest income (36 for 9M 2026 and 58 for 9M 2025 in the Q3 10-Q `page:19`), so interest cover on cash interest is stated before that income.
- Free cash flow follows the release definition (`Free cash flow is defined as net cash provided by (used in) operating activities less payments for property and equipment, intangible assets and capitalized software`, Q3 release `page:21`). Operating cash flow includes movements in player deposit liabilities and investments, which belong to players; the "excluding player deposit movements" rows remove them (C4).

### Reconciliations performed

- Segment to Group Adjusted EBITDA: FY2025 3,124 less overhead 279 equals 2,845 (10-K `page:168`); 9M 2026 1,739 less 240 equals 1,499; 9M 2025 2,226 less 213 equals 2,013 (Q3 10-Q `page:14`). Each equals the Group figure in the MD&A reconciliation (Q3 10-Q `page:72`).
- Quarterly sums: 631 + 508 + 360 = 1,499; 616 + 919 + 478 = 2,013 (C8).
- Reconciliation to net loss: the 9M 2026 add-backs listed on Q3 10-Q `page:72` take net loss of 1,235 to Adjusted EBITDA of 1,499 (C9).
- Debt: the Q3 debt note total (12,313) equals 170 current plus 12,143 non-current on the balance sheet (Q3 10-Q `page:6`, `page:26`); the eleven instrument rows sum to 12,390 of principal including accrued interest (C10).
- Release net debt: 12,313 + 77 − 26 − 1,708 = 10,656, matching Q3 release `page:26` (C10).
- Cash: opening 3,832, net movement 137 and foreign exchange (49) give 3,920, equal to unrestricted cash 1,708, restricted cash 95 and player deposit cash 2,117 (Q3 10-Q `page:9` and `page:10`). The caption on the movement line says "decrease" over a positive amount; the balances, not the caption, are used.
- Release leverage ratios: net debt on the release basis divided by calculated LTM Adjusted EBITDA gives 3.70x (Q1), 4.28x (Q2) and 4.57x (Q3), which round to the 3.7x, 4.3x and 4.6x the releases print (C11). This supports the LTM Adjusted EBITDA built here.

### Evidence assessment

- **Leverage.** Evidence: total debt 12,313 at September 30, 2026 against 12,266 at December 31, 2025 (`Total debt 12,313 12,266`, Q3 10-Q `page:26`), while LTM Adjusted EBITDA is 2,331 against 2,845. Mechanism: the 2025 acquisition debt is in place for the full period, and earnings fell in the US segment (241 against 612 for nine months) and from the UK gaming duty in International (Q3 10-Q `page:70`: `an increase of remote gaming tax in UK`). Consequence: calculated total leverage rose by about one turn between FY2025 and Q3 2026, and the company itself targets `2.0 - 2.5x` (Q3 release `page:12`).
- **Cover.** Evidence: cash interest paid 636 over the last twelve months against 531 in FY2025. Mechanism: a full year of interest on the notes due 2031 and Term Loan B due 2032 issued in 2025 (Q3 10-Q `page:53`: `a full quarter of interest on the Senior Secured Notes due 2031 and the USD First Lien Term Loan B due 2032 issued in August 2025`). Consequence: cover on cash interest fell from 5.36x to 3.67x, and the next twelve months carry `$696 million payable within 12 months net of hedging` of scheduled interest (Q3 10-Q `page:74`).
- **Cash flow.** Evidence: free cash flow of 377 for 9M 2026 against 269 for 9M 2025, but 201 against 396 once player deposit movements are removed. Mechanism: nine-month 2026 operating cash flow was lifted by player funds (176) and higher accrued legal and gaming duty liabilities (Q3 10-Q `page:76`). Consequence: the improvement in reported free cash flow is not evidence of stronger underlying cash generation; share repurchases of 543 over the last twelve months exceeded free cash flow of 515, and the programme is now paused (Q3 10-Q `page:75`).
- **Liquidity.** Evidence: cash 1,708 and undrawn revolver commitments 782 at September 30, 2026. Mechanism: the revolver was drawn to fund operations and repayments (`drew £1,208 million ($1,621 million)`, Q3 10-Q `page:27`). Consequence: the sterling revolver headroom fell from 1,185 at March 31, 2026 to 782; the post-amendment commitment is larger, but its undrawn amount is not supplied.
- **Earnings quality.** Evidence: Adjusted EBITDA of 1,499 for 9M 2026 against an operating loss of 1,256 and net loss of 1,235. Mechanism: impairment of 873 on Brazil, legal loss contingencies of 200 and restructuring of 254 are excluded. Consequence: cash costs among those items (legal settlements, restructuring severance) will reduce free cash flow in later periods even though they do not reduce Adjusted EBITDA.
- **Guidance context (management claim).** The Q3 release gives 2026 guidance midpoints of revenue `$17.61bn` and Adjusted EBITDA `$2.495bn` (`page:12`). Subtracting the nine-month figures implies fourth-quarter Adjusted EBITDA of about 996 and revenue of about 5,106 (C12). This is management's guidance, not a forecast built here, and it assumes the nine-month figures in this answer.

### Consistency with CP-0

- CP-0 asked whether FY2025 segment figures were recast for 2026 customer transfers. The Q3 10-Q MD&A describes `the migration of PokerStars North America to the U.S. segment` as an element of the period-over-period change (`page:69`), which indicates 2025 comparatives are as originally reported. Segment trends here therefore mix organic change with the transfers, and the effect is not quantified in the sources.
- CP-0 noted year-to-date cash flows only in the 10-Qs. This answer uses year-to-date data for LTM building and shows the release-derived quarter only for Q3 2026 free cash flow (35, Q3 release `page:27`).
- No CP-0 statement is corrected.

## Calculations

All inputs are reported values at the locators shown. LTM means FY2025 minus the 2025 comparative period plus the 2026 period.

| ID | Quantity | Formula and inputs | Result |
| --- | --- | --- | --- |
| C1 | LTM Adjusted EBITDA | Q3: 2,845 (10-K `page:107`) − 2,013 + 1,499 (Q3 10-Q `page:72`); Q2: 2,845 − 1,535 + 1,139 (Q2 10-Q `page:66`); Q1: 2,845 − 616 + 631 (Q1 10-Q `page:53`) | 2,331; 2,449; 2,860 |
| C2 | LTM segment lines (Q3) | US 922 − 612 + 241; International 2,202 − 1,614 + 1,498; overhead −279 − (−213) + (−240); US revenue 6,967 − 4,825 + 4,901; International revenue 9,416 − 6,821 + 7,603 | US 551; International 2,086; overhead (306); sum 2,331; revenue 7,043 and 10,198 |
| C3 | LTM cash interest paid | Q3: 531 − 321 + 426; Q2: 531 − 217 + 325 (Q2 10-Q `page:8`); Q1: 531 − 91 + 97 (Q1 10-Q `page:7`) | 636; 639; 537 |
| C4 | Player deposit movements and operating cash flow excluding them | Movement = "Player deposits - investments" line + "Player deposit liability" line, cash flow signs: FY2024 33 + 212; FY2025 120 + (−227); 9M 2025 117 + (−244); 9M 2026 18 + 158; LTM −107 − (−127) + 176. Operating cash flow less movement: 1,602 − 245; 1,184 − (−107); 756 − (−127); 904 − 176; LTM 1,291 − 883 + 728 | Movements 245; −107; −127; 176; 196. Excluding: 1,357; 1,291; 883; 728; 1,136 |
| C5 | Capital expenditure, free cash flow | Capex = property + intangibles + capitalized software: FY2024 144 + 136 + 381; FY2025 105 + 162 + 510; 9M 2025 69 + 105 + 313; 9M 2026 59 + 71 + 397; LTM 777 − 487 + 527. FCF = operating cash flow − capex: 1,602 − 661; 1,184 − 777; 756 − 487; 904 − 527; LTM 1,332 − 817. FCF excluding player funds: 1,357 − 661; 1,291 − 777; 883 − 487; 728 − 527; LTM 1,136 − 817 | Capex 661; 777; 487; 527; 817. FCF 941; 407; 269; 377; 515. FCF excluding player funds 696; 514; 396; 201; 319 |
| C6 | Net debt (carrying) | Total debt − unrestricted cash: Dec 2024 6,736 − 1,531; Dec 2025 12,266 − 1,828; Mar 2026 11,965 − 1,512; Jun 2026 11,978 − 1,563; Sep 2026 12,313 − 1,708 | 5,205; 10,438; 10,453; 10,415; 10,605 |
| C7 | Ratios | Total debt / EBITDA: 6,736 / 2,357; 12,266 / 2,845; 11,965 / 2,860; 11,978 / 2,449; 12,313 / 2,331. Net debt / EBITDA: 5,205 / 2,357; 10,438 / 2,845; 10,453 / 2,860; 10,415 / 2,449; 10,605 / 2,331. EBITDA / cash interest: 2,357 / 462; 2,845 / 531; 2,860 / 537; 2,449 / 639; 2,331 / 636. EBITDA / net interest expense: 2,357 / 419; 2,845 / 515; 2,331 / 645. (EBITDA − capex) / cash interest: (2,357 − 661) / 462; (2,845 − 777) / 531; (2,331 − 817) / 636 | Total 2.86x, 4.31x, 4.18x, 4.89x, 5.28x. Net 2.21x, 3.67x, 3.65x, 4.25x, 4.55x. Cover 5.10x, 5.36x, 5.33x, 3.83x, 3.67x. Net interest cover 5.63x, 5.52x, 3.61x. After capex 3.67x, 3.89x, 2.38x |
| C8 | Q4 2025 and quarter sums | Revenue 16,383 − 11,646; Adjusted EBITDA 2,845 − 2,013; net income −407 − (−417). Sums: 631 + 508 + 360; 616 + 919 + 478; 209 − 296 − 1,148; 335 + 37 − 789 | 4,737; 832; 10. Sums 1,499; 2,013; −1,235; −417 |
| C9 | Net loss to Adjusted EBITDA, 9M 2026 | −1,235 + (−73) income tax benefit + (−425) other income + 477 interest + 1,220 D&A + 176 SBC + 32 + 254 + 200 + 873 | 1,499 |
| C10 | Debt checks | Instrument rows 1,370 + 431 + 166 + 663 + 3,808 + 1,234 + 579 + 540 + 981 + 1,664 + 954; maturities 13 + 52 + 2,681 + 1,143 + 3,692 + 4,696; release net debt 12,313 + 77 − 26 − 1,708; difference 12,390 − 12,277; carrying vs release net debt 10,656 − 10,605 | 12,390; 12,277; 10,656; 113; 51 |
| C11 | Release-basis leverage | 10,575 / 2,860; 10,480 / 2,449; 10,656 / 2,331 | 3.70x; 4.28x; 4.57x |
| C12 | Guidance-implied Q4 2026 | Adjusted EBITDA 2,495 − 1,499; revenue 17,610 − 12,504 | 996; 5,106 |
| C13 | Change in total debt in 2025 | 12,266 − 6,736 (10-K `page:187`) | 5,530 |

Sign convention in C4 is the cash flow statement's: positive is a cash inflow within operating activities.

## Gaps

| Gap | Severity | Affected use | Action |
| --- | --- | --- | --- |
| Covenant ratio values and definitions are not printed; headroom is Not calculable. Pre-amendment net total leverage limit 5.20:1 and post-amendment net first lien leverage level 5.70:1.00 are the only terms. | Medium | Leverage, covenant work | Obtain the credit agreement definitions and compliance certificate. |
| LTM figures are calculated from annual and year-to-date data, not reported. Q4 2025 is derived. | Low | All LTM ratios | Treat as calculated; the release leverage ratios reproduce within rounding. |
| Segment comparatives appear not to be recast for the 2026 customer transfers (PokerStars North America to the US; Southern Europe to SEA). | Medium | Segment trends | Obtain the recast comparatives or restrict segment conclusions to total Group. |
| No September 30, 2025 balance sheet; total debt, cash (beyond the cash flow note) and lease balances for that date are Not supplied. | Low | Nine-month 2025 balance ratios | Not required for LTM Q3 2026; leave blank. |
| Undrawn revolver at December 31, 2024 is Not supplied. | Low | Liquidity history | Obtain the FY2024 annual report if a full history is needed. |
| Post-amendment undrawn revolver, pro forma maturity schedule and margin are Not supplied beyond the stated commitment and margin range. | Medium | Liquidity, maturities | Obtain the amended agreement and the November 3, 2026 position. |
| Cash interest paid is not netted for interest income or hedge settlements; no separate cash hedge line is used. | Low | Interest cover | Present cover before interest income, as here. |
| Player deposit movements inside operating cash flow are not Group cash. The treatment here removes them from operating cash flow; the release's own "excluding player funds" measure is given for Q3 2026 only (`(91)` against `(117)` for the quarter, Q3 release `page:27`) and also deducts extended-payment intangible purchases. | Medium | Free cash flow | Use the excluding-player-funds rows; do not mix with the release measure. |
| Adjusted EBITDA differs from covenant EBITDA and excludes recurring-style restructuring and legal items; no covenant EBITDA bridge is supplied. | Medium | Leverage, earnings quality | Obtain the covenant EBITDA definition; show the add-backs. |
| Legal, tax and contingent claims (Fast Code class action, Indian GST demand, IRS notices, Austrian and German player claims) and the Fox option are outside this financial base. | Medium | Claims outside debt | Cover in the debt and claims module. |
| Text extraction only; no comparison to filed HTML or XBRL. | Low | All figures | Spot-check key lines in verification. |

## Next module

CP-1A runs next on the business description and the same sources, and CP-2 follows with the debt structure, claims outside debt and the October 30, 2026 amendment. Both should take from this answer the calculated LTM Adjusted EBITDA of 2,331, total debt of 12,313, cash of 1,708, the pre-amendment liquidity and maturity profile, the distinction between company-defined and covenant leverage, and the open segment-recast question. CP-5 should verify the calculations in `## Calculations` against the cited pages.
