# CP-1 - Financial base: Clear Channel Outdoor Holdings, Inc. (cco)

## Request

- Issuer: Clear Channel Outdoor Holdings, Inc. (issuer id `cco`), consolidated, as of 2026-11-05 (information cutoff 2026-11-05). Pathway `credit_snapshot`, module CP-1 (financial base). Reporting currency USD (context).
- Periods used: FY2025 and FY2024 (years ended December 31); the three and six months ended June 30, 2026 (Q2 2026, H1 2026) with 2025 comparatives; and the twelve months ended June 30, 2026 (LTM), built in `## Calculations` as FY2025 plus H1 2026 less H1 2025. Context names current period q2-2026 and prior period fy-2025; both are matched. Balance-sheet dates: December 31, 2024, December 31, 2025, March 31, 2026 and June 30, 2026. No source for the quarter ended September 30, 2026 is supplied (CP-0), so June 30, 2026 is the latest balance sheet.
- Units: the reported-statement tables are in USD thousands exactly as printed. The chart tables and the metrics table are in US$m (USD millions) with one decimal, converted from printed thousands; ratios are in x. Percent figures are in percent.
- Locator convention: "S4 page:3" is the retained text chunk numbered 3 of source S4, not a printed page number. Quotes are exact substrings of the named chunk.
- Scope: reported facts first, then labelled calculations. The perimeter is the continuing operations of the consolidated group. The Spain business is a discontinued operation held for sale at June 30, 2026 and sold on August 4, 2026 (S4 page:9). Statements of cash flows include discontinued operations (S4 page:7, page:8), which is flagged wherever a cash-flow figure is used.
- Inherited from the CP-0 handoff: nothing after August 5, 2026 is supplied; the merger and the related debt amendments are pending at the latest filing; executed debt documents and the guarantor list are not supplied; the covenant ratio is not printed because the springing test was not in effect.

## Sources

### Issuer sources relied on

| Label | Exact source name | sha256 | Use in this handoff |
| --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_cco-20251231.htm.jsonl | 571124584b3bbe99a4fbff8adfaba5f0fb8933c5a0003d1ef35708c36c286d39 | Audited FY2025 and FY2024 statements, debt, lease and commitment notes, covenants |
| S2 | 10-Q_2025-09-30_cco-20250930.htm.jsonl | 607e09a97951d1ad4c47649541e08f4b1e6c417cc3bd1376061667bd020f7126 | Third quarter 2025 revenue |
| S3 | 10-Q_2026-03-31_cco-20260331.htm.jsonl | a3ad502aa08b83254f97c12e4f79050207a26c6003570b7bd60e33a1124d566c | March 31, 2026 balance sheet, first quarter 2026 revenue, facility availability |
| S4 | 10-Q_2026-06-30_cco-20260630.htm.jsonl | fc57da6e0f4d7240050e6201742116917e571f4d11e190fcdcea84112429a51c | Latest balance sheet and H1 2026 and Q2 2026 statements, debt, liquidity, covenant text |
| S5 | EX-99.1_2026-02-26_exhibit991-ccohearningsrel.htm.jsonl | 5cc1d0e97fcf82997c8a6a84c737a99df944d52765b5ff540d0441e7f806a5a6 | Fourth quarter and FY2025 Adjusted EBITDA, segments, AFFO (issuer non-GAAP) |
| S6 | EX-99.1_2026-05-06_exhibit991-ccohearningsrel.htm.jsonl | d85dec563195c10f63eb072d829bbf7b6a81552ec09b651fb1bdefa50ffbbbd6 | First quarter 2026 Adjusted EBITDA (issuer non-GAAP) |
| S7 | EX-99.1_2026-08-05_exhibit991-ccohearningsrel.htm.jsonl | 86540d4f0d27c129f16354d25b76c67a8e72d707aa0c050724d976a7c4c17aa5 | Q2 2026 and H1 2026 Adjusted EBITDA, Adjusted Corporate expenses, AFFO, net debt (issuer non-GAAP) |

### Supplied handoffs

| Module | sha256 | Use in this handoff |
| --- | --- | --- |
| CP-0 | c71e4b6220652757facb8cbe1e745147a9ea4d59240f1f57156457c376ee1b60 | Source readiness: period map, perimeter, pending-event boundary at August 5, 2026, missing legal documents and guarantor list |

### Run settings (not issuer evidence)

Context file sha256 de960bbc410d3388b8cf7496a6e161733b9fd5ffc09b25a54e06ffd5d05f0294. It names the issuer, the as-of date, USD and the periods q2-2026 and fy-2025. Ratings, quotes, deal terms and peers are blank, and blank is not zero.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| On twelve-month Adjusted EBITDA of 544.3, debt principal of 5,148.8 is 9.46x, and EBITDA covers cash interest 1.40x. Cash is 192.1 and undrawn facilities 205.5. The next large maturities fall in 2028. | Medium | Adjusted EBITDA is the issuer's own measure, and balances are at June 30, 2026 with the merger still pending. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Leverage on Adjusted EBITDA eased from 10.20x at FY2025 to 9.46x on the twelve months to June 30, 2026, because EBITDA rose while debt principal stayed flat. | Improvement comes from earnings, not debt reduction, so it depends on advertising demand holding. | Medium |
| Adjusted EBITDA covers cash interest 1.40x on the trailing basis, against 1.28x for FY2025. | Thin cover leaves little room for an earnings setback before cash flow after interest tightens. | Medium |
| Free cash flow, operating cash flow less capital expenditures, is 84.3 on the trailing basis, against 32.0 for FY2025. | Positive but small next to 5,148.8 of debt; the Spain sale proceeds are the stated source for debt reduction, subject to the merger. | Medium |
| No borrowings are drawn on either facility; availability is 205.5 against 192.1 of cash at June 30, 2026. | Backstop liquidity exists, but the receivables facility is limited by a borrowing base. | Medium |
| Operating lease liabilities of 1,361.9 sit outside the debt figure. | Fixed lease obligations rank alongside debt service and are not captured in the debt ratios. | High |

### Financial base view

Clear Channel Outdoor Holdings, Inc. is a highly leveraged, now almost entirely U.S. out-of-home advertiser whose reported earnings are improving while its debt stack is unchanged. On the issuer's own Adjusted EBITDA of 544.3 for the twelve months to June 30, 2026 (FY2025 of 504.8 plus H1 2026 of 247.3 less H1 2025 of 207.8), debt principal including finance leases of 5,148.8 is 9.46x and, net of 192.1 of continuing cash, 9.11x, down from 10.20x and 9.82x at FY2025. Adjusted EBITDA covers cash interest paid of 390.1 only 1.40x, against 1.28x for FY2025 and 1.09x for FY2024. Revenue for the twelve months is 1,679.1 against 1,604.1 for FY2025, and the Adjusted EBITDA margin is 32.4%. Free cash flow, defined here as operating cash flow of 160.4 less capital expenditures of 76.1, is 84.3; both inputs include discontinued operations. Debt principal barely changed between December 31, 2025 and June 30, 2026: every note and term-loan balance is identical, and only finance leases moved, down 0.1. So the leverage improvement is earnings-led. The structure is 3,340.0 of first-priority secured debt (a 425.0 term loan and 2,915.0 of senior secured notes), 1,805.3 of senior unsecured notes due 2028 and 2029, and undrawn facilities; the secured share of principal is high, and the unsecured notes are effectively subordinated to it. Liquidity is 192.1 of cash and 205.5 of excess availability under a 100.0 revolving facility and a 200.0 receivables-based facility, both maturing June 12, 2030. The next significant maturities are in 2028, when 899.3 of 7.750% senior notes and the 425.0 term loan fall due, and the company has issued conditional redemption notices for the 2028 and 2029 unsecured notes, with conditions that include the merger closing. Operating lease liabilities of 1,361.9 and 877.6 of non-lease non-cancelable contracts at December 31, 2025 sit outside debt. Three qualifications bound this view. First, Adjusted EBITDA is the issuer's non-GAAP measure and is stated after site lease expense; the covenant EBITDA is not supplied. Second, cash-flow figures include the Spain business that was held for sale and the 2025 cash flows of businesses sold in 2025. Third, nothing after August 5, 2026 is supplied, so the merger, the redemption notices and the use of Spain sale proceeds, which are described as pending, cannot be reflected.

### Source context

| Source | Entity and perimeter | Periods | Statement kind | Units |
| --- | --- | --- | --- | --- |
| S1 | Clear Channel Outdoor Holdings, Inc. and subsidiaries, consolidated; continuing operations with the Spain business presented as discontinued operations | Years ended December 31, 2025, 2024 and 2023; balance sheets at December 31, 2025 and 2024 | Audited statements; MD&A unaudited | "(In thousands, except per share data)" (S1 page:78); USD |
| S2 | Same consolidated perimeter | Three and nine months ended September 30, 2025 and 2024 | Unaudited condensed | USD thousands (S2 page:3) |
| S3 | Same consolidated perimeter | Three months ended March 31, 2026 and 2025; balance sheet at March 31, 2026 | Unaudited condensed | USD thousands |
| S4 | Same consolidated perimeter | Three and six months ended June 30, 2026 and 2025; balance sheet at June 30, 2026 | Unaudited condensed | "(In thousands, except share and per share data)" (S4 page:2); USD |
| S5, S6, S7 | Same perimeter, management presentation | Q4 and FY2025; Q1 2026; Q2 and H1 2026 | Unaudited, includes non-GAAP | USD thousands in tables (S7 page:1) |

Each of the seven sources is extractable text, and CP-0 judged them sufficient with limits. Extraction is not a fidelity review. The statement figures below were read from the statement chunks and tied out in `## Calculations`.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 11.99 | 11.76 | x | Principal 5,704.0 (S1 page:100, page:101) over FY2024 Adjusted EBITDA 475.8 (S5 page:9); net of continuing cash 109.7 (S1 page:77). Calculated, C3. The principal still includes the 375.0 CCIBV term loan of businesses later sold, while EBITDA is continuing operations only; excluding it the ratios are 11.20 and 10.97 (C3) |
| FY2025 | 10.20 | 9.82 | x | Principal 5,148.9 (S1 page:100, page:101, page:117) over FY2025 Adjusted EBITDA 504.8 (S5 page:9); net of continuing cash 190.0 (S1 page:77). Calculated, C3. Debt is principal including finance leases, before original issue discount and fees |
| LTM Jun 30, 2026 | 9.46 | 9.11 | x | Principal 5,148.8 (S4 page:15) over LTM Adjusted EBITDA 544.3 (C1); net of continuing cash 192.1 (S4 page:2). Calculated, C3. Adjusted EBITDA is issuer non-GAAP; operating leases excluded; Spain sale proceeds not reflected |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 1.09 | x | Adjusted EBITDA 475.8 (S5 page:9) over cash paid for interest 434.5 (S1 page:80). Calculated, C4. Cash interest includes discontinued operations (the CCIBV term loan carried interest of 28.4 in discontinued operations, S1 page:96) while EBITDA is continuing only |
| FY2025 | 1.28 | x | Adjusted EBITDA 504.8 over cash paid for interest 394.4 (S1 page:80). Calculated, C4. Includes about 11.9 of accrued CCIBV interest paid when the loan was prepaid on March 31, 2025 (S1 page:102) |
| LTM Jun 30, 2026 | 1.40 | x | LTM Adjusted EBITDA 544.3 over LTM cash paid for interest 390.1 (C2). Calculated, C4. The prepayment interest falls in both FY2025 and H1 2025 and so nets out of the LTM figure; cash interest still comes from a statement that includes discontinued operations |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Dec 31, 2024 | 109.7 | Not supplied: the FY2025 annual report prints excess availability only at December 31, 2025, and states that no borrowings were outstanding in 2024 | US$m | Cash and cash equivalents of continuing operations (S1 page:77); a further 54.6 was held in discontinued operations (S1 page:95) and is excluded |
| Dec 31, 2025 | 190.0 | 205.8 | US$m | Cash of continuing operations (S1 page:77); 21.1 held in discontinued operations excluded (S1 page:95). Availability: revolving facility 93.1 plus receivables-based facility 112.7, after letters of credit of 6.9 and 87.3 (S1 page:68) |
| Mar 31, 2026 | 182.4 | 204.5 | US$m | Cash of continuing operations (S3 page:2). Availability: 93.0 plus 111.5 after letters of credit of 7.0 and 88.5 (S3 page:30) |
| Jun 30, 2026 | 192.1 | 205.5 | US$m | Cash of continuing operations (S4 page:2); 10.1 held in discontinued operations excluded (S4 page:10). Availability as printed in total (S4 page:33); the two facility figures of 93.0 and 112.4 sum to 205.4 and the filing attributes the difference to rounding (S4 page:34). The revolver letter of credit of 7.0 related to Spain and was cancelled on August 4, 2026 (S4 page:34) |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0.3 | US$m | Schedule at December 31, 2025 as printed, thousands 312 (S1 page:117); finance lease obligations only. The June 30, 2026 current portion of long-term debt is 0.3 (S4 page:2) |
| 2027 | 0.3 | US$m | As printed, thousands 297 (S1 page:117); finance lease obligations only; no note or loan matures |
| 2028 | 1,324.6 | US$m | As printed (S1 page:117): 7.750% Senior Notes 899.3 and the term loan 425.0 (S4 page:15) plus finance leases of 0.3 (C5). Term loan maturity carries a springing date if certain secured notes remain outstanding (S1 page:108). Conditional redemption notice issued for the notes, subject to the merger (S4 page:17) |
| 2029 | 906.3 | US$m | As printed (S1 page:117): 7.500% Senior Notes 906.0 due June 2029 (S4 page:15) plus finance leases of 0.4 (C5). Conditional redemption notice issued, subject to the merger (S4 page:17) |
| 2030 | 865.3 | US$m | As printed (S1 page:117): 7.875% Senior Secured Notes 865.0 due April 2030 plus finance leases of 0.3 (C5); revolver and receivables-based facility mature June 2030 and are undrawn (S4 page:15) |
| 2031 and later | 2,052.1 | US$m | Printed as "Thereafter" (S1 page:117): 7.125% Senior Secured Notes 1,150.0 due February 2031 and 7.500% Senior Secured Notes 900.0 due March 2033 plus finance leases of 2.1 (C5). The schedule is at December 31, 2025; June 30, 2026 principal of every note and loan is unchanged (S4 page:15). Excludes original issue discount and fees |

### Financials and credit metrics

| Metric | LTM Jun 30, 2026 | FY2025 | FY2024 | Basis and source |
| --- | --- | --- | --- | --- |
| Revenue, continuing operations (US$m) | 1,679.1 | 1,604.1 | 1,505.2 | LTM calculated, C1; FY reported, S1 page:78 |
| Operating income (US$m) | 316.7 | 310.6 | 279.2 | LTM calculated, C1; FY reported, S1 page:78 |
| Adjusted EBITDA, issuer non-GAAP (US$m) | 544.3 | 504.8 | 475.8 | LTM calculated, C1; FY reported, S5 page:9; stated after site lease expense and before share-based compensation |
| Adjusted EBITDA margin (%) | 32.4 | 31.5 | 31.6 | Calculated, C6 |
| Total Segment Adjusted EBITDA (US$m) | 640.9 | 595.1 | 574.7 | LTM calculated, C1; FY reported, S1 page:99 |
| Adjusted Corporate expenses (US$m) | 96.6 | 90.3 | 99.0 | LTM calculated, C1; FY reported, S5 page:10 |
| Interest expense, net, continuing (US$m) | 397.8 | 395.6 | 401.5 | LTM calculated, C1; FY reported, S1 page:78 |
| Cash paid for interest (US$m) | 390.1 | 394.4 | 434.5 | LTM calculated, C2; FY reported, S1 page:80; includes discontinued operations |
| Loss from continuing operations (US$m) | (114.2) | (103.7) | (123.8) | LTM calculated, C1; FY reported, S1 page:78 |
| Net cash provided by operating activities, consolidated (US$m) | 160.4 | 114.9 | 79.7 | LTM calculated, C1; FY reported, S1 page:80; includes discontinued operations |
| Capital expenditures, consolidated (US$m) | (76.1) | (82.9) | (142.4) | LTM calculated, C1; FY reported, S1 page:80; includes discontinued operations (21.1 in FY2025, S1 page:97) |
| Free cash flow, operating cash flow less capital expenditures (US$m) | 84.3 | 32.0 | (62.6) | Calculated, C7; issuer does not define this measure |
| Adjusted Funds From Operations, issuer non-GAAP (US$m) | 141.8 | 95.3 | 58.6 | LTM calculated, C1; FY reported, S5 page:10; H1, S7 page:9 |
| Cash and cash equivalents, continuing (US$m) | 192.1 | 190.0 | 109.7 | Reported, S4 page:2; S1 page:77 |
| Total debt, principal including finance leases (US$m) | 5,148.8 | 5,148.9 | 5,704.0 | Calculated from printed principal, C3; matches the printed maturity total for FY2025, S1 page:117 |
| Net debt, principal less continuing cash (US$m) | 4,956.6 | 4,958.9 | 5,594.3 | Calculated, C3; the issuer's own net debt on carrying value is 4,915.5 at June 30, 2026 (S7 page:6) |
| Total debt, carrying value as printed (US$m) | 5,107.6 | 5,103.0 | 5,660.3 | Reported, S4 page:15; S1 page:101; net of original issue discount and fees |
| Secured debt principal (US$m) | 3,340.0 | 3,340.0 | 3,665.0 | Calculated, C3; term loan plus senior secured notes (FY2024 includes the 375.0 CCIBV term loan); revolver and receivables-based facility undrawn |
| Total debt / Adjusted EBITDA (x) | 9.46 | 10.20 | 11.99 | Calculated, C3 |
| Net debt / Adjusted EBITDA (x) | 9.11 | 9.82 | 11.76 | Calculated, C3 |
| Secured debt / Adjusted EBITDA (x) | 6.14 | 6.62 | 7.70 | Calculated, C3; an indicator of secured leverage, not the covenant ratio |
| Adjusted EBITDA / cash interest paid (x) | 1.40 | 1.28 | 1.09 | Calculated, C4 |
| Adjusted EBITDA / interest expense, net (x) | 1.37 | 1.28 | 1.18 | Calculated, C4 |
| Operating lease liabilities, current and non-current (US$m) | 1,361.9 | 1,367.7 | 1,362.2 | Reported, S4 page:2; S1 page:77; outside debt |
| Debt plus operating lease liabilities / (Adjusted EBITDA plus operating lease expense) (x) | Not supplied: operating lease expense is not printed for the interim periods | 8.37 | 9.72 | Calculated, C8; issuer does not define this measure; indicative only |
| Total stockholders' deficit (US$m) | (3,457.1) | (3,394.4) | (3,639.8) | Reported, S4 page:3; S1 page:78 |

Which leverage basis to read: Adjusted EBITDA is stated after site lease expense, so operating lease liabilities of 1,361.9 are a fixed claim that total debt over Adjusted EBITDA leaves out. None of the ratios here is a covenant ratio; the only maintenance test is a springing first lien net leverage test that was not in effect (see Covenants).

### Reported statements of operations (USD thousands)

| Line (as printed) | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- |
| Revenue | 438,040 | 402,808 | 811,904 | 736,988 | 1,604,140 | 1,505,230 |
| Direct operating expenses | 196,178 | 185,530 | 376,280 | 354,059 | 748,023 | 680,578 |
| Selling, general and administrative expenses | 69,968 | 65,711 | 136,560 | 129,373 | 262,383 | 252,907 |
| Corporate expenses | 36,581 | 31,123 | 67,399 | 50,903 | 110,925 | 126,904 |
| Depreciation and amortization | 41,246 | 43,335 | 82,769 | 86,339 | 174,952 | 173,998 |
| Other operating expense (income), net | 5,011 | (315) | 20,357 | (6,100) | (2,749) | (8,340) |
| Operating income | 89,056 | 77,424 | 128,539 | 122,414 | 310,606 | 279,183 |
| Interest expense, net | (99,027) | (96,026) | (197,525) | (195,387) | (395,649) | (401,541) |
| Gain (loss) on extinguishment of debt | — | 28,796 | — | 28,796 | (14,956) | (2,393) |
| Other income (expense), net | 268 | 663 | 1,009 | 912 | 1,199 | (8,378) |
| Income (loss) from continuing operations before income taxes | (9,703) | 10,857 | (67,977) | (43,265) | (98,800) | (133,129) |
| Income tax benefit (expense) | (299) | (4,526) | 8,528 | (5,706) | (4,947) | 9,365 |
| Income (loss) from continuing operations | (10,002) | 6,331 | (59,449) | (48,971) | (103,747) | (123,764) |
| Income (loss) from discontinued operations | 5,038 | 4,318 | 6,491 | 122,833 | 128,486 | (52,114) |
| Consolidated net income (loss) | (4,964) | 10,649 | (52,958) | 73,862 | 24,739 | (175,878) |

Sources: S4 page:3 (Q2 and H1); S1 page:78 (FY). The operating cost block ties to operating income in each column (C9). The row "—" for gain on extinguishment means the statement prints a dash; it is not an inferred zero. The H1 2025 net income includes a 132.0 gain on sold and held-for-sale businesses within discontinued operations (S4 page:11), which makes the trailing net income unrepresentative; the trailing metrics use continuing operations.

### Segment and quarterly series (USD thousands)

| Line | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- |
| America revenue | 324,316 | 303,111 | 602,803 | 557,304 | 1,196,824 | 1,143,510 |
| Airports revenue | 113,601 | 99,685 | 208,827 | 179,668 | 407,127 | 361,488 |
| Other revenue (Singapore) | 123 | 12 | 274 | 16 | 189 | 232 |
| America Segment Adjusted EBITDA | 142,377 | 127,601 | 247,079 | 215,472 | 501,038 | 487,990 |
| Airports Segment Adjusted EBITDA | 29,890 | 24,347 | 52,816 | 38,660 | 95,219 | 87,860 |
| Other Segment Adjusted EBITDA | (278) | (381) | (559) | (571) | (1,137) | (1,142) |
| Total Segment Adjusted EBITDA | 171,989 | 151,567 | 299,336 | 253,561 | 595,120 | 574,708 |
| Adjusted Corporate expenses (non-GAAP) | 28,557 | 23,009 | 52,057 | 45,746 | 90,330 | 98,950 |
| Adjusted EBITDA (non-GAAP) | 143,432 | 128,558 | 247,279 | 207,815 | 504,790 | 475,758 |
| Digital revenue | 195,426 | 177,308 | 353,776 | 316,189 | 707,695 | 622,251 |

Sources: S4 page:12, page:13, page:24 (Q2 and H1 segments and digital revenue); S1 page:99 and page:57 (FY segments and digital revenue); S7 page:3 and page:8 (Adjusted Corporate expenses and Adjusted EBITDA); S5 page:2, page:9 and page:10 (FY2025 and FY2024). Segment Adjusted EBITDA less Adjusted Corporate expenses equals Adjusted EBITDA in every column (C9). Segment Adjusted EBITDA is a GAAP segment measure; Adjusted EBITDA and Adjusted Corporate expenses are non-GAAP.

Discrete quarters, USD thousands, current continuing-operations basis:

| Line | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 |
| --- | --- | --- | --- | --- |
| Revenue | 405,637 | 461,515 | 373,864 | 438,040 |
| Adjusted EBITDA (non-GAAP) | 132,515 | 164,460 | 103,847 | 143,432 |

Sources: S2 page:3 (Q3 2025 revenue); S5 page:1 (Q4 2025); S3 page:3 and S6 page:8 (Q1 2026); S4 page:3 and S7 page:8 (Q2 2026). The Q3 2025 Adjusted EBITDA is derived, not printed in the supplied set: FY2025 less Q4 2025 less H1 2025 (C1). The four revenue quarters add to the LTM revenue (C9).

### Adjusted EBITDA reconciliation (USD thousands)

| Line (as printed) | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- | --- | --- |
| Income (loss) from continuing operations | (10,002) | 6,331 | (59,449) | (48,971) | (103,747) | (123,764) |
| Income tax expense (benefit) | 299 | 4,526 | (8,528) | 5,706 | 4,947 | (9,365) |
| Other income, net | (268) | (663) | (1,009) | (912) | (1,199) | 8,378 |
| Loss (gain) on extinguishment of debt | — | (28,796) | — | (28,796) | 14,956 | 2,393 |
| Interest expense, net | 99,027 | 96,026 | 197,525 | 195,387 | 395,649 | 401,541 |
| Other operating expense (income), net | 5,011 | (315) | 20,357 | (6,100) | (2,749) | (8,340) |
| Depreciation and amortization | 41,246 | 43,335 | 82,769 | 86,339 | 174,952 | 173,998 |
| Share-based compensation | 7,942 | 7,359 | 13,788 | 12,783 | 25,474 | 23,076 |
| Restructuring and other costs (reversals), net | 177 | 755 | 1,826 | (7,621) | (3,493) | 7,841 |
| Adjusted EBITDA | 143,432 | 128,558 | 247,279 | 207,815 | 504,790 | 475,758 |

Sources: S7 page:8 and page:9 (Q2 and H1); S5 page:9 (FY). The columns add to the printed totals (C9). Add-backs that bear on quality: other operating expense, net of 20,357 in H1 2026, which the 10-Q attributes mainly to merger transaction costs of 20.2 million (S4 page:21); and a 10.1 million insurance recovery in H1 2025 and FY2025 reported within restructuring and other costs (S7 page:9). The definition is the same in the February and August 2026 releases (S5 page:8, S7 page:7).

### Reported balance sheet, selected lines (USD thousands)

| Line (as printed) | Jun 30, 2026 | Dec 31, 2025 | Dec 31, 2024 |
| --- | --- | --- | --- |
| Cash and cash equivalents | 192,138 | 190,022 | 109,707 |
| Accounts receivable, net | 367,992 | 371,377 | 344,096 |
| Current assets of discontinued operations | 187,273 | 202,709 | 1,176,036 |
| Total current assets | 772,520 | 793,194 | 1,659,044 |
| Operating lease right-of-use assets | 1,318,530 | 1,313,912 | 1,315,529 |
| Goodwill | 507,819 | 507,819 | 507,819 |
| Total assets | 3,763,081 | 3,828,875 | 4,804,263 |
| Current operating lease liabilities | 134,384 | 142,139 | 132,877 |
| Accrued interest | 88,910 | 99,095 | 90,945 |
| Deferred revenue | 102,730 | 75,437 | 70,214 |
| Current portion of long-term debt | 314 | 312 | 348 |
| Current liabilities of discontinued operations | 90,348 | 99,309 | 775,210 |
| Total current liabilities | 615,887 | 618,094 | 1,271,978 |
| Long-term debt | 5,107,315 | 5,102,681 | 5,659,957 |
| Non-current operating lease liabilities | 1,227,530 | 1,225,567 | 1,229,345 |
| Total liabilities | 7,220,200 | 7,223,243 | 8,444,046 |
| Total stockholders' deficit | (3,457,119) | (3,394,368) | (3,639,783) |

Sources: S4 page:2 and page:3; S1 page:77 and page:78. Total assets less total liabilities equals the stockholders' deficit at each date (C9). The Spain business is within the discontinued-operation lines at June 30, 2026 and December 31, 2025 (S4 page:10); at December 31, 2024 those lines also held the former Europe-North and Latin American businesses (S1 page:96).

### Reported cash flows, selected lines (USD thousands)

| Line (as printed) | H1 2026 | H1 2025 | FY2025 | FY2024 |
| --- | --- | --- | --- | --- |
| Net cash provided by operating activities | 47,840 | 2,326 | 114,860 | 79,746 |
| Capital expenditures | (35,323) | (42,080) | (82,879) | (142,395) |
| Proceeds from sales of businesses and/or assets, net | 1,288 | 599,292 | 607,807 | 13,712 |
| Proceeds from long-term debt | — | — | 2,050,000 | 1,657,000 |
| Payments on long-term debt | (145) | (574,673) | (2,610,918) | (1,635,562) |
| Net cash provided by (used for) financing activities | (20,989) | (585,281) | (598,295) | (8,176) |
| Cash paid for interest | 205,848 | 210,220 | 394,429 | 434,520 |
| Cash paid for income taxes, net of refunds | 997 | 6,737 | 7,391 | 16,150 |
| Decrease in operating lease liabilities (cash payments, net of interest) | (105,949) | (124,080) | (207,736) | (280,025) |
| Non-cash operating lease expense, net of interest | 94,143 | 113,219 | 207,105 | 270,492 |

Sources: S4 page:5 and page:6 (H1); S1 page:80 (FY). The H1 columns show a dash for proceeds from long-term debt because the H1 statement prints no such line; that is an absent line, not a stated zero. Capital expenditures of continuing operations were 29,735 in H1 2026 and 26,058 in H1 2025 (S4 page:13) and 61,784 and 80,717 in FY2025 and FY2024 (S1 page:99); the balance is discontinued operations (S4 page:11; S1 page:97). Merger transaction costs paid of 12.2 million in H1 2026 are inside operating cash flow (S4 page:33).

### Debt register at June 30, 2026

| Instrument (as printed, Note 5) | Principal (USD thousands) | Rate and maturity | Issuer and security | Source |
| --- | --- | --- | --- | --- |
| Receivables-Based Credit Facility | — (undrawn) | June 2030; commitment 200,000 limited by a borrowing base of 85% of eligible receivables | Company and certain subsidiaries as borrowers; first lien on receivables collateral, second lien on other collateral | S4 page:15, page:33; S1 page:104, page:106 |
| Revolving Credit Facility | — (undrawn) | June 2030; commitment 100,000 | Company as borrower; first-priority lien pari passu with the term loan and secured notes | S4 page:15, page:33; S1 page:107, page:108 |
| Term Loan Facility | 425,000 | August 2028 (springing earlier date if certain secured notes remain outstanding); floating rate, Term SOFR plus an Applicable Rate that is not printed | Company as borrower; guaranteed by certain domestic subsidiaries; first-priority | S4 page:15; S1 page:107, page:108 |
| 7.875% Senior Secured Notes | 865,000 | April 1, 2030; semi-annual interest | Company; guaranteed by certain wholly-owned domestic subsidiaries; first-priority on the notes collateral | S4 page:15; S1 page:110 |
| 7.125% Senior Secured Notes | 1,150,000 | February 15, 2031; interest February 15 and August 15 | As above | S4 page:15; S1 page:112 |
| 7.500% Senior Secured Notes | 900,000 | March 15, 2033; interest March 15 and September 15 | As above | S4 page:15; S1 page:112, page:113 |
| 7.750% Senior Notes | 899,311 | April 15, 2028; interest April 15 and October 15 | Company; senior unsecured guarantees from certain domestic subsidiaries; effectively subordinated to secured debt and structurally subordinated to non-guarantors | S4 page:15; S1 page:114 |
| 7.500% Senior Notes | 905,950 | June 1, 2029; interest June 1 and December 1 | As for the 7.750% Senior Notes | S4 page:15; S1 page:115, page:116 |
| Finance leases | 3,489 | Not applicable | Not applicable | S4 page:15 |
| Original issue discount | (2,967) | Not applicable | Not applicable | S4 page:15 |
| Long-term debt fees | (38,154) | Not applicable | Not applicable | S4 page:15 |
| Total debt (carrying) | 5,107,629 | Not applicable | Not applicable | S4 page:15 |

The principal amounts of the six notes and term loan, and the finance leases, add to 5,148,750 (C3), and the carrying total ties after discount and fees (C9). Notes repurchased in 2025 (95.7 million of the 7.750% notes and 134.1 million of the 7.500% notes) are held by the company and not cancelled; the table shows balances net of them (S1 page:102). About 8% of debt was variable rate at December 31, 2025 (S1 page:73) and the weighted average cost of debt was 7.6% (S1 page:73). Amendments and conditional redemption notices tied to the pending merger are described under Subsequent events and pending items.

### Liquidity

| Component | Amount (US$m) | Source |
| --- | --- | --- |
| Cash and cash equivalents, continuing operations, June 30, 2026 | 192.1 | S4 page:2 |
| Cash held by discontinued operations in Spain (excluded) | 10.1 | S4 page:10 |
| Revolving facility: limit 100.0, letters of credit 7.0, excess availability | 93.0 | S4 page:33 |
| Receivables-based facility: limit 200.0, letters of credit 87.6, excess availability | 112.4 | S4 page:33 |
| Total excess availability as printed | 205.5 | S4 page:33 |
| Borrowings outstanding on either facility | None drawn (printed as a dash) | S4 page:33 |

Of the 192.1 of continuing cash, 5.5 is held by continuing subsidiaries outside the U.S. (S4 page:32). The company states "We believe our sources of liquidity will be sufficient to meet our cash requirements for at least the next 12 months" (S4 page:29). Both facilities mature June 12, 2030 (S4 page:33), so no facility expires within twelve months. The receivables-based availability depends on a borrowing base that fluctuates with receivables (S4 page:34), and its fixed charge coverage test applies only in a Covenant Trigger Period (S1 page:106). Surety bonds of 42.6 and bank guarantees of 10.9 were outstanding at June 30, 2026, partly supported by 2.7 of cash collateral (S4 page:16). The company expects cash interest of about 197 million in the second half of 2026 and about 394 million in 2027 on June 30, 2026 debt (S4 page:32). Net proceeds of the Spain sale are not in the balance sheet and are subject to adjustments and fees (S4 page:9).

### Claims outside the debt figure

| Claim | Amount | Inside or outside debt | Source |
| --- | --- | --- | --- |
| Operating lease liabilities, current and non-current, June 30, 2026 | 1,361.9 US$m (134.4 current) | Outside; at December 31, 2025 undiscounted lease payments were 2,218.6 and the weighted-average discount rate 7.88% | S4 page:2; S1 page:117 |
| Non-lease non-cancelable contracts, December 31, 2025 | 877.6 US$m | Outside; payments by year printed | S1 page:118 |
| Capital expenditure commitments, December 31, 2025 | 152.7 US$m | Outside | S1 page:118 |
| Finance lease obligations | 3.5 US$m | Inside the principal figure used here | S4 page:15 |
| Surety bonds and bank guarantees, June 30, 2026 | 42.6 and 10.9 US$m | Off balance sheet; a portion relates to Spain | S4 page:16 |
| Asset retirement obligations, December 31, 2025 | 24.6 US$m | Inside other liabilities | S1 page:125 |
| Pension and retiree medical | Not found in the supplied sources for continuing operations | Not supplied | S1 page:78 (pension appears only as a reclassification on sold businesses) |
| Factoring and supply-chain finance | Not found in the supplied sources | Not supplied | Keyword search of all seven sources |
| Litigation | Ordinary-course claims, accrued where probable; no amount printed | Not quantified | S4 page:17 |
| Merger termination fee payable by the company in specified circumstances | 39.8 US$m | Contingent | S4 page:8 |

### Covenants

- Springing financial covenant (Senior Secured Credit Agreement): a first lien net leverage ratio of less than 7.10 to 1.00, applying only if the revolver has an outstanding balance or undrawn letters of credit under it exceed 10 million; "these conditions were not met and the covenant was not in effect" at June 30, 2026 (S4 page:34), with further carve-outs described at S1 page:109. The reported ratio is therefore not printed, and headroom is Not calculable from the sources.
- Receivables-based facility: a fixed charge coverage ratio of no less than 1.00 to 1.00 applies only in a Covenant Trigger Period; it did not apply for the four quarters ended December 31, 2025 (S1 page:106). A June 30, 2026 statement of its status is Not supplied.
- Compliance: the company states it "was in compliance with all covenants contained in its debt agreements" at June 30, 2026 (S4 page:16).
- Indenture covenants limit debt, liens, restricted payments, investments, asset sales and affiliate transactions (S1 page:111). Definitions and baskets are in executed documents that are not supplied.
- The secured-debt ratio in the metrics table is first-priority principal over Adjusted EBITDA. It is not the covenant measure, whose EBITDA and net debt definitions are not supplied.

### Subsequent events and pending items

- Spain sale: completed August 4, 2026 for approximately 132.3 million; net proceeds subject to adjustments and fees; intended to reduce debt "subject to the outcome of the Merger" (S4 page:22). Not in the June 30, 2026 balance sheet. Illustrative sensitivity: if the full price reduced debt principal, total debt over LTM Adjusted EBITDA would be 9.22x (C10); the net amount and its application are not supplied.
- Pending merger: Madison Parent Inc. to acquire the company at 2.43 per share in cash; closing expected by the end of the third quarter of 2026; stockholders approved on May 12, 2026 (S4 page:8). No source says whether it closed.
- Debt amendments: supplemental indentures and credit-agreement amendments provide that the merger is not a change of control; those for the secured notes and the Senior Secured Credit Agreement are effective but operative only on closing; the receivables-based amendment would extend its maturity to five years from closing and raise commitments from 200.0 to 250.0 (S4 page:16, page:17).
- Conditional redemption notices were issued for the 7.750% and 7.500% Senior Notes, conditional on the merger closing (S4 page:17). If effected, 1,805.3 of unsecured principal would be redeemed (C3), but the funding source is not supplied.
- The 10-K recorded the August 2025 refinancing of 2,000.0 of 5.125% and 9.000% secured notes into 7.125% and 7.500% secured notes, with a 43.8 loss on extinguishment (S1 page:102).

### Definition and basis risks

1. Adjusted EBITDA is the issuer's non-GAAP measure: loss from continuing operations plus tax, non-operating items, other operating expense, depreciation and amortization, share-based compensation, and restructuring and other costs (S7 page:7). It is after site lease expense, which sits in direct operating expenses (S4 page:24) and includes minimum guaranteed payments and revenue-sharing rent (S4 page:13). Covenant EBITDA is not supplied.
2. Total debt used here is principal including finance leases before discount and fees. The issuer's printed total and net debt are on carrying value (S7 page:6); the difference at June 30, 2026 is 41.1 (C3).
3. The FY2024 debt includes the CCIBV term loan, which belonged to businesses later sold; FY2024 leverage is shown with a sensitivity excluding it (C3).
4. Cash flow figures include discontinued operations (S4 page:7, page:8), while Adjusted EBITDA is continuing operations only. Trailing operating cash flow and capital expenditures include Spain in all periods and businesses sold in 2025 in FY2025 and H1 2025.
5. The Q3 2025 Adjusted EBITDA is derived from three printed figures and not printed in the supplied set.
6. The revenue mix between contracts with customers and leases changed sharply year over year because of changed contract terms (S4 page:15); that does not change total revenue.
7. Net income and cash flow for H1 2025 include large one-time items from the 2025 disposals (S4 page:11), so the trailing figures rely on continuing operations.
8. All balances are at June 30, 2026, before the Spain sale and the pending merger-related actions.

## Calculations

All inputs are printed figures cited above, in USD thousands unless stated. Results are shown in US$m to one decimal (ratios to two decimals), rounded half up.

C1. LTM to June 30, 2026 equals FY2025 plus H1 2026 less H1 2025.
- Revenue: 1,604,140 + 811,904 - 736,988 = 1,679,056.
- Operating income: 310,606 + 128,539 - 122,414 = 316,731.
- Adjusted EBITDA: 504,790 + 247,279 - 207,815 = 544,254.
- Total Segment Adjusted EBITDA: 595,120 + 299,336 - 253,561 = 640,895.
- Adjusted Corporate expenses: 90,330 + 52,057 - 45,746 = 96,641.
- Interest expense, net: 395,649 + 197,525 - 195,387 = 397,787.
- Loss from continuing operations: (103,747) + (59,449) - (48,971) = (114,225).
- Operating cash flow: 114,860 + 47,840 - 2,326 = 160,374.
- Capital expenditures: 82,879 + 35,323 - 42,080 = 76,122.
- AFFO: 95,286 + 51,479 - 4,954 = 141,811.
- Q3 2025 Adjusted EBITDA: 504,790 - 164,460 - 207,815 = 132,515; also 544,254 - 164,460 - 103,847 - 143,432 = 132,515.

C2. LTM cash paid for interest: 394,429 + 205,848 - 210,220 = 390,057.

C3. Leverage. Principal including finance leases equals the sum of the term loan, the five notes and finance leases.
- June 30, 2026: 425,000 + 865,000 + 1,150,000 + 900,000 + 899,311 + 905,950 + 3,489 = 5,148,750. Net of cash 192,138: 4,956,612. 5,148,750 / 544,254 = 9.46; 4,956,612 / 544,254 = 9.11.
- December 31, 2025: 5,145,261 + 3,636 = 5,148,897, equal to the printed maturity total (S1 page:117). Net of cash 190,022: 4,958,875. 5,148,897 / 504,790 = 10.20; 4,958,875 / 504,790 = 9.82.
- December 31, 2024: 425,000 + 1,250,000 + 750,000 + 865,000 + 995,000 + 1,040,000 + 375,000 + 3,974 = 5,703,974. Net of cash 109,707: 5,594,267. 5,703,974 / 475,758 = 11.99; 5,594,267 / 475,758 = 11.76. Excluding the CCIBV term loan of 375,000: 5,328,974 / 475,758 = 11.20; (5,328,974 - 109,707) / 475,758 = 10.97.
- Secured principal (term loan plus senior secured notes): June 30, 2026 and December 31, 2025 425,000 + 865,000 + 1,150,000 + 900,000 = 3,340,000; 3,340,000 / 544,254 = 6.14; 3,340,000 / 504,790 = 6.62. December 31, 2024: 425,000 + 1,250,000 + 750,000 + 865,000 + 375,000 = 3,665,000; 3,665,000 / 475,758 = 7.70.
- Unsecured notes: 899,311 + 905,950 = 1,805,261.
- Carrying versus principal at June 30, 2026: 5,148,750 - 5,107,629 = 41,121, equal to discount 2,967 plus fees 38,154.

C4. Cover.
- Adjusted EBITDA / cash interest: FY2024 475,758 / 434,520 = 1.09; FY2025 504,790 / 394,429 = 1.28; LTM 544,254 / 390,057 = 1.40.
- Adjusted EBITDA / interest expense, net: FY2024 475,758 / 401,541 = 1.18; FY2025 504,790 / 395,649 = 1.28; LTM 544,254 / 397,787 = 1.37.
- Coupon cross-check: 865,000 x 7.875% + 1,150,000 x 7.125% + 900,000 x 7.5% + 899,311 x 7.75% + 905,950 x 7.5% = 68,118.75 + 81,937.5 + 67,500 + 69,696.5 + 67,946.25 = 355,199.0, of the issuer's expected 2027 cash interest of about 394,000 (S4 page:32). The remainder of about 38,801 covers the floating term loan, fees and facility costs; the term-loan margin is not printed, so this is an upper-bound residual, not a rate.

C5. Maturity schedule composition. 2028: 1,324,631 - (899,311 + 425,000) = 320 of finance leases. 2029: 906,301 - 905,950 = 351. 2030: 865,251 - 865,000 = 251. Thereafter: 2,052,105 - (1,150,000 + 900,000) = 2,105. The scheduled amounts 312 + 297 + 1,324,631 + 906,301 + 865,251 + 2,052,105 = 5,148,897, equal to the printed total.

C6. Adjusted EBITDA margin: LTM 544,254 / 1,679,056 = 32.4%; FY2025 504,790 / 1,604,140 = 31.5%; FY2024 475,758 / 1,505,230 = 31.6%.

C7. Free cash flow equals operating cash flow less capital expenditures: LTM 160,374 - 76,122 = 84,252; FY2025 114,860 - 82,879 = 31,981; FY2024 79,746 - 142,395 = -62,649; H1 2026 47,840 - 35,323 = 12,517; H1 2025 2,326 - 42,080 = -39,754. Both inputs include discontinued operations.

C8. Lease-adjusted leverage, indicative. FY2025: (5,148,897 + 1,367,706) / (504,790 + 273,448) = 6,516,603 / 778,238 = 8.37, where 273,448 is operating lease expense of continuing operations (S1 page:117). FY2024: (5,703,974 + 1,362,222) / (475,758 + 251,229) = 7,066,196 / 726,987 = 9.72. The LTM value is Not supplied because interim operating lease expense is not printed.

C9. Tie-outs, all equal to printed totals.
- Statement of operations: revenue less direct operating, SG&A, corporate, depreciation and amortization and other operating expense (income) equals operating income. FY2025: 1,604,140 - 748,023 - 262,383 - 110,925 - 174,952 + 2,749 = 310,606. FY2024: 1,505,230 - 680,578 - 252,907 - 126,904 - 173,998 + 8,340 = 279,183. H1 2026: 811,904 - 376,280 - 136,560 - 67,399 - 82,769 - 20,357 = 128,539. H1 2025: 736,988 - 354,059 - 129,373 - 50,903 - 86,339 + 6,100 = 122,414. Q2 2026: 438,040 - 196,178 - 69,968 - 36,581 - 41,246 - 5,011 = 89,056. Q2 2025: 402,808 - 185,530 - 65,711 - 31,123 - 43,335 + 315 = 77,424.
- Below operating income: FY2025 310,606 - 395,649 - 14,956 + 1,199 = -98,800; less tax 4,947 = -103,747; plus discontinued operations 128,486 = 24,739. H1 2026 128,539 - 197,525 + 1,009 = -67,977; plus tax benefit 8,528 = -59,449; plus 6,491 = -52,958.
- Segment revenue: 602,803 + 208,827 + 274 = 811,904; 324,316 + 113,601 + 123 = 438,040. Segment Adjusted EBITDA less Adjusted Corporate expenses: FY2025 595,120 - 90,330 = 504,790; FY2024 574,708 - 98,950 = 475,758; H1 2026 299,336 - 52,057 = 247,279; H1 2025 253,561 - 45,746 = 207,815; Q2 2026 171,989 - 28,557 = 143,432; Q2 2025 151,567 - 23,009 = 128,558.
- Adjusted EBITDA reconciliation: H1 2026 -59,449 - 8,528 - 1,009 + 197,525 + 20,357 + 82,769 + 13,788 + 1,826 = 247,279; Q2 2026 -10,002 + 299 - 268 + 99,027 + 5,011 + 41,246 + 7,942 + 177 = 143,432; H1 2025 -48,971 + 5,706 - 912 - 28,796 + 195,387 - 6,100 + 86,339 + 12,783 - 7,621 = 207,815; Q2 2025 6,331 + 4,526 - 663 - 28,796 + 96,026 - 315 + 43,335 + 7,359 + 755 = 128,558; FY2025 -103,747 + 4,947 - 1,199 + 14,956 + 395,649 - 2,749 + 174,952 + 25,474 - 3,493 = 504,790; FY2024 -123,764 - 9,365 + 8,378 + 2,393 + 401,541 - 8,340 + 173,998 + 23,076 + 7,841 = 475,758.
- Debt carrying total, June 30, 2026: 5,148,750 - 2,967 - 38,154 = 5,107,629. December 31, 2024: 5,703,974 - 7,313 - 36,356 = 5,660,305.
- Balance sheet: June 30, 2026 total liabilities 615,887 + 5,107,315 + 1,227,530 + 212,688 + 56,780 = 7,220,200, and 3,763,081 - 7,220,200 = -3,457,119. December 31, 2025: 3,828,875 - 7,223,243 = -3,394,368. December 31, 2024: 4,804,263 - 8,444,046 = -3,639,783. Operating lease liabilities December 31, 2025: 142,139 + 1,225,567 = 1,367,706, equal to the lease note total (S1 page:117).
- Operating cash flow H1 2026: -52,958 + 94,143 + 82,769 - 250 + 13,832 + 4,968 + 3,352 - 8,927 - 784 + 3,897 + 4,730 - 9,909 - 105,949 - 10,185 + 27,373 + 1,738 = 47,840.
- Capital expenditures: FY2025 continuing 61,784 + discontinued 21,095 = 82,879; H1 2026 29,735 + 5,588 = 35,323.
- Quarterly revenue: 405,637 + 461,515 + 373,864 + 438,040 = 1,679,056, equal to the LTM revenue in C1. Quarterly Adjusted EBITDA: 132,515 + 164,460 + 103,847 + 143,432 = 544,254, equal to the LTM figure; and 103,847 + 143,432 = 247,279.

C10. Spain sensitivity (illustrative): (5,148,750 - 132,300) / 544,254 = 9.22. It uses the gross price of approximately 132.3 million, ignores adjustments, fees and cash that leaves with the business, and assumes full application to debt, which the company ties to the merger outcome.

C11. Direction checks. Leverage 10.20 at FY2025 and 9.46 at LTM: lower (C3). Debt principal 5,148,897 at December 31, 2025 and 5,148,750 at June 30, 2026: essentially unchanged, down 147 (finance leases 3,636 to 3,489). Adjusted EBITDA rose from 504,790 (FY2025) to 544,254 (LTM). Cash interest cover rose from 1.28 to 1.40 (C4). Cash rose from 190,022 to 192,138.

## Gaps

- Undrawn facilities at December 31, 2024: Not supplied. The FY2025 annual report prints excess availability only at December 31, 2025; the liquidity chart carries Not supplied for that row.
- Covenant levels and headroom: the springing ratio was not in effect and is not printed; covenant EBITDA and net debt definitions are in executed documents that are not supplied. Headroom is Not calculable.
- Operating lease expense for interim periods: not printed in the 10-Qs, so a trailing lease-adjusted leverage is Not supplied.
- Term loan margin: the Applicable Rate is not printed, so floating interest cannot be rebuilt from coupons; the coupon cross-check leaves an unexplained residual (C4).
- Adjusted EBITDA is issuer-defined and non-GAAP; no covenant or lender-defined EBITDA is supplied. Q3 2025 Adjusted EBITDA is derived, not printed.
- Cash-flow and cash-interest figures include discontinued operations; the continuing-operations split of operating cash flow and cash interest is Not supplied. Capital expenditures of continuing operations are printed and shown separately.
- FY2024 debt includes the CCIBV term loan of sold businesses; a continuing-only FY2024 debt figure is shown by sensitivity only.
- Guarantor and non-guarantor financial information is Not supplied (CP-0); structural subordination of the unsecured notes cannot be quantified.
- Everything after August 5, 2026 is Not supplied, including the merger outcome, redemption of the unsecured notes, effect of the amendments, the net Spain proceeds and their use, and a September 30, 2026 balance sheet.
- Pension, retiree medical, factoring and supply-chain finance programs: not found in the supplied text; treated as Not supplied rather than zero.
- Ratings, market quotes, peers and valuation inputs are blank in the context; no market value of debt beyond the printed approximation of 5.3 billion at June 30, 2026 (S4 page:16).

## Next module

CP-1A should take the business and transaction facts from the pending-merger items above (merger at 2.43 per share, closing expected by the end of the third quarter of 2026 but not confirmed in the supplied set, termination fees of 39.8 and 92.9, amendments operative only on closing, conditional redemption notices), the Spain sale completed on August 4, 2026, the 2025 disposals and refinancing history, the segment revenue and Segment Adjusted EBITDA table, and the digital revenue share. CP-2 should read leverage as 9.46x total debt and 9.11x net debt on trailing issuer-defined Adjusted EBITDA, cash interest cover of 1.40x, first-priority secured leverage of 6.14x, and 5,148.8 of principal that did not change in 2026, together with the operating leases outside debt, the absence of a printed covenant ratio, the pending merger, the exposure of the unsecured notes to structural subordination, and the stale-date restriction. CP-5 should trace each calculated figure to the printed inputs in `## Calculations`, check that no trailing metric uses a figure dated after August 5, 2026, and flag that Adjusted EBITDA, Adjusted Corporate expenses, AFFO and net debt come from releases or issuer non-GAAP presentations, while statement figures come from the filings.
