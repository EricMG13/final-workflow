# CP-1 financial base: ESCO TECHNOLOGIES INC (ese)

## Request

- Issuer: ESCO TECHNOLOGIES INC (issuer id `ese`, NYSE: ESE), consolidated with its subsidiaries, as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run `ese-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. This is CP-1, the financial base. Its consumers are CP-1A, CP-2 and CP-5. CP-0 (source readiness) is the one upstream handoff.
- Execution: host session. The host read the pinned source text, recomputed every derived number and wrote this answer. No provider was called.
- Periods (context): current period `q3-2026`, prior period `fy-2025`. ESCO has a September fiscal year end, so Q3 2026 is the quarter ended June 30, 2026, "nine months 2026" (9M 2026) is October 1, 2025 to June 30, 2026, FY2025 is the year ended September 30, 2025 and FY2024 the year ended September 30, 2024. LTM means the twelve months ended June 30, 2026, built as FY2025 plus 9M 2026 minus 9M 2025.
- Currency and unit: USD. Statements are printed in thousands of USD; the chart tables below convert to US$m where their header says so. No other currency is the reporting currency.
- Perimeter: continuing operations of ESCO Technologies Inc. and subsidiaries. The VACCO business (sold July 18, 2025) is discontinued operations in every period presented. The balance sheets at September 30, 2025 and later show no discontinued-operations assets or liabilities; the September 30, 2024 balance sheet does (10-K page:58).
- Question answered: what financial base do the supplied filings give for leverage, coverage, cash flow and liquidity, and what limits it?
- This module carries the CP-0 restrictions forward: covenant levels, the May 29, 2026 credit agreement, Megger financials and anything after August 10, 2026 are Not supplied.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Use |
| --- | --- | --- |
| 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | fe80d5d10f35aaa7f1b7aa40e6d69aeaea7f501fabdde619947c03aa0fe69d71 | Audited FY2025 and FY2024 statements, debt note, segment note, VACCO |
| 10-Q_2025-12-31_ese-20251231x10q.htm.jsonl | 028e0b9aec25ecf720ca796f0beef13fd8b40ddc333348a8ba8153fe3b16e523 | Q1 2026 balance sheet, debt, cash flow, liquidity |
| 10-Q_2026-03-31_ese-20260331x10q.htm.jsonl | d207365eeea17e17e69c10625b481ddba582ee4861f7a9c60376e4bd5dffc806 | Q2 2026 balance sheet, debt, cash flow, liquidity |
| 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | 056428009193705ead08cb6828be9f20a62a9323946644ad69e280efbf618711 | Q3 2026 statements, notes, debt, leases, Megger, liquidity |
| EX-99.1_2026-01-30_tm264950d1_ex99-1.htm.jsonl | 73c00c863e8360707e7681c62537391b693f1632ac470f63ec94b54622dbc238 | Q1 2026 release: quarterly EBITDA reconciliation |
| EX-99.1_2026-05-07_tm2613615d1_ex99-1.htm.jsonl | 4483c93985a6b3ea98a959d8659fafa040f3230850186662a7c5bb7c5d2d8a1d | Q2 2026 release: quarterly and six-month EBITDA reconciliation |
| EX-99.1_2026-08-06_tm2621646d1_ex99-1.htm.jsonl | f683102e1a6a6e74cee756fd0639a64a1d810e0d5fd17fcb2dc502f25f716fb6 | Q3 2026 release: EBITDA and adjusted measures, backlog, guidance |

### Other inputs

| Input | sha256 | Use |
| --- | --- | --- |
| context (`contexts/866706-esco-technologies-inc-ese.json`) | da65696ce609dcf19999b44c58b8a10f43f7d7bc7cde7c4a3762d76affdde214 | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 7f46d3b1dbdad4b468a5bdd5db37f408dc8a1ce57aba77ff195a116822899d17 | Source readiness: READY_WITH_LIMITATIONS; gap list carried forward |

### Labels and locators

Locators are `page:N` of the pinned text files (the source chunk, not the printed page). "10-K" is the FY2025 10-K. "10-Q Q1", "10-Q Q2" and "10-Q Q3" are the 10-Qs for the quarters ended December 31, 2025, March 31, 2026 and June 30, 2026. "Release Q1", "Release Q2" and "Release Q3" are the EX-99.1 releases dated February 5, May 7 and August 6, 2026.

CP-0 consistency: this module follows CP-0's rulings that the 10-K and 10-Qs control and the releases are attributed management claims, that availability figures are on different bases across quarters, and that the contract-liability note and the balance sheet caption must stay separate. It does not correct CP-0. It adds one point CP-0 left open: the pension question. A full-text search of the 10-K again finds only the deferred tax line "Pension and other postretirement benefits" (10-K page:79), so pension is Not supplied.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| On reported figures ESCO has low leverage and strong cash conversion, with total debt of $85.0 million at June 30, 2026. That base excludes the Megger acquisition, which management expects to close in the first quarter of fiscal 2027. | Medium | Pro forma debt, covenant levels and Megger earnings are not supplied, so the reported base may not describe the post-closing company. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt fell from $186.0 million at September 30, 2025 to $85.0 million at June 30, 2026, and LTM EBITDA of $305.7 million gives total debt to EBITDA of 0.278x. | Reported leverage is very low and net debt is small, giving headroom before the acquisition financing. | High |
| Operating cash flow from continuing operations was $193.4 million for the nine months to June 30, 2026, against $88.3 million a year earlier, helped by contract liability growth. | Cash generation is strong but part reflects customer advances timing, so it may not repeat. | Medium |
| Liquidity at June 30, 2026 is $73.2 million of cash plus $442.3 million of undrawn revolver after letters of credit. | Near-term liquidity is ample and no maturity falls before August 30, 2028 except $20.0 million due within twelve months. | High |
| The $2.35 billion Megger purchase includes $0.9 billion in cash, and new facilities of $500 million each (revolver, term loan A, term loan B) are committed but not yet effective. | Debt is expected to rise materially at closing, so the current low leverage is temporary. | Medium |
| Nine-month cash flow from continuing operations excludes a discontinued-operations outflow of $59.3 million, alongside approximately $59 million of tax paid on the VACCO gain. | Free cash flow from continuing operations overstates cash available after that one-off tax. | Medium |

### Financial base view

On reported figures, ESCO enters the Megger transaction from a strong and lightly levered base. Total borrowings at June 30, 2026 were $85.0 million against LTM EBITDA of $305.677 million, and cash was $73.236 million, so net debt was $11.764 million. Over the same twelve months EBITDA covered cash interest paid about twenty times. Liquidity of $515.536 million is mostly an undrawn $500 million revolver. These are reported-basis ratios computed here, not covenant ratios, because the credit agreement definitions are not supplied.

In US$ millions, the headline figures are: total borrowings of $186.0 million at September 30, 2025 and $85.0 million at June 30, 2026; LTM EBITDA of $305.7 million; operating cash flow from continuing operations of $193.4 million for the nine months to June 30, 2026 against $88.3 million for the prior-year nine months; cash of $73.2 million and undrawn revolver of $442.3 million at June 30, 2026; a current portion of debt of $20.0 million; and a discontinued-operations operating outflow of $59.3 million.

Three features limit how far this base can be used. First, it is a pre-acquisition picture. The signed Megger purchase (approximately $2.35 billion, of which $0.9 billion is cash) is to be financed by a new $1.5 billion committed facility set that will replace the existing facility at closing, so the debt table at June 30, 2026 describes a structure management expects to retire. Second, the LTM period carries the Maritime acquisition (closed April 25, 2025) for all four quarters, but FY2025 and 9M 2025 carry it only from that date, so year-on-year growth includes acquired revenue, and the latest nine months include a large working capital inflow and a large discontinued-operations outflow, so LTM cash conversion is not a clean run rate. Third, the 10-Q Q3 prints nine-month cash flows only, so discrete Q3 cash flow is not available.

The statements are consistent with each other where checked: the 10-K and the 10-Q Q3 print the same September 30, 2025 total assets, and the release quarterly EBITDA figures sum to the nine-month figure (see Calculations). The status for downstream use is READY_WITH_LIMITATIONS: CP-1A and CP-2 can use the figures below; CP-2 must treat covenant headroom and post-closing leverage as Not supplied.

### Source assessment

| Source | Entity and perimeter | Period and basis | Unit | Version relationship |
| --- | --- | --- | --- | --- |
| 10-K | ESCO Technologies Inc. and subsidiaries, continuing operations, VACCO as discontinued | FY2025, FY2024, FY2023 audited, year ended September 30 | US$ thousands | Controls annual figures; comparatives recast for VACCO |
| 10-Q Q1 | Same | Quarter ended December 31, 2025, unaudited | US$ thousands | Separate active source |
| 10-Q Q2 | Same | Quarter and six months ended March 31, 2026, unaudited | US$ thousands | Separate active source |
| 10-Q Q3 | Same | Quarter and nine months ended June 30, 2026, unaudited | US$ thousands | Latest filing; controls over Release Q3 |
| Release Q1, Q2, Q3 | Same, management presentation | Quarter and year-to-date, unaudited, GAAP plus adjusted | US$ thousands | Statements duplicate the 10-Qs; adjusted measures are attributed claims |

Extraction covers all pages of each source; no page was found absent. The 10-K carries the audit report of Grant Thornton LLP (10-K page:55 "We have served as the Company’s auditor since 2021."). Interim statements are unaudited (10-Q Q3 page:2 "(Unaudited)").

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 (September 30, 2024) | 0.615 | 0.283 | x | Total borrowings 122,000 over EBITDA 198,355 (US$ thousands). EBITDA is EBT plus interest expense, net plus D&A, continuing operations, reported not adjusted. Excludes leases and letters of credit. |
| FY2025 (September 30, 2025) | 0.758 | 0.345 | x | Total borrowings 186,000 over EBITDA 245,376. FY2025 EBITDA includes Maritime from April 25, 2025 only, while year-end debt carries its full financing, so the ratio is overstated against a run rate. |
| LTM December 31, 2025 | 0.541 | 0.155 | x | Total borrowings 145,511 (including 511 of short-term foreign borrowings) over LTM EBITDA 269,202. Same definitions. |
| LTM March 31, 2026 | 0.496 | 0.180 | x | Total borrowings 145,000 over LTM EBITDA 292,617. Same definitions. |
| LTM June 30, 2026 | 0.278 | 0.038 | x | Total borrowings 85,000 over LTM EBITDA 305,677; net debt 11,764 after cash of 73,236. Pre-Megger; Megger debt and EBITDA are Not supplied. Not a covenant calculation. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 13.65 | x | EBITDA 198,355 over interest paid 14,535 (US$ thousands, cash flow supplemental). |
| FY2025 | 14.09 | x | EBITDA 245,376 over interest paid 17,421. Interest paid is the total printed, not split between continuing and discontinued operations. |
| LTM December 31, 2025 | 15.35 | x | LTM EBITDA 269,202 over LTM interest paid 17,543. |
| LTM March 31, 2026 | 21.58 | x | LTM EBITDA 292,617 over LTM interest paid 13,558. Six-month interest paid is 4,958 against 8,821 a year earlier, so the LTM denominator is lower. |
| LTM June 30, 2026 | 20.42 | x | LTM EBITDA 305,677 over LTM interest paid 14,970. The roughly 7 million of Megger debt financing costs in Q3 2026 interest expense is not cash interest paid in this measure and is not in the denominator. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| September 30, 2024 | 65.963 | Not supplied: the revolver commitment at that date is not stated in the supplied sources | US$m | Cash from the 10-K balance sheet. Drawn revolver 122.0 and letters of credit 5.0 are printed. |
| September 30, 2025 | 101.350 | 464.900 | US$m | Revolver commitment 500.0 less drawn 25.0 less letters of credit 10.1. Company states approximately 465. Excludes the undrawn part of the incremental delayed-draw facility, which the filings do not state. |
| December 31, 2025 | 103.824 | 468.789 | US$m | 500.0 less revolver and short-term borrowings 20.511 less letters of credit 10.7. Company states approximately 469 excluding the Incremental Facility. |
| March 31, 2026 | 92.252 | 440.500 | US$m | 500.0 less drawn 45.0 less letters of credit 14.5. Company states approximately 440. |
| June 30, 2026 | 73.236 | 442.300 | US$m | 500.0 less drawn 45.0 less letters of credit 12.7. Company states approximately 442. The 250.0 increase option needs lender consent and is excluded. The revolver matures August 30, 2028. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Within twelve months of June 30, 2026 | 20.000 | US$m | Current portion of long-term debt, term loan A. Classified as current because management intends to repay it under the Incremental Facility repayment terms; the schedule is not printed. |
| After twelve months, due by August 30, 2028 | 65.000 | US$m | Long-term debt of 65,000: revolver 45,000 plus term loan A 20,000. The split between fiscal 2027 and fiscal 2028 is Not supplied. The revolver and term loan A fall due on August 30, 2028. |
| After August 30, 2028 | Not supplied: no existing debt is shown beyond that date, and the replacement facility tenors apply only after closing | US$m | The New Credit Facility revolver and term loan A mature five years after its effective date and term loan B seven years after; amounts drawn at closing are Not supplied. |

### Financials and credit metrics

Figures are in US$ thousands unless a row says x or %. "calc" rows are computed in the Calculations section. 9M columns are not annualized, so ratios are shown for FY and LTM columns only.

| Metric | FY2024 | FY2025 | 9M 2025 | 9M 2026 | LTM June 30, 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- |
| Net sales | 919,127 | 1,095,388 | 742,714 | 938,027 | 1,290,701 | 10-K page:57; 10-Q Q3 page:2; LTM calc |
| SG&A expense | 208,203 | 234,638 | 171,305 | 195,039 | 258,372 | same pages; LTM calc |
| Amortization of intangible assets | 32,804 | 53,317 | 32,735 | 61,086 | 81,668 | same pages; LTM calc |
| Interest expense, net | 15,247 | 17,502 | 12,373 | 13,992 | 19,121 | same pages; includes about 7 million Megger financing costs in Q3 2026; LTM calc |
| Earnings before income taxes | 130,953 | 152,853 | 93,286 | 120,296 | 179,863 | same pages; LTM calc |
| Income tax expense | 28,325 | 36,554 | 21,841 | 25,314 | 40,027 | same pages; LTM calc |
| Earnings from continuing operations | 102,628 | 116,299 | 71,445 | 94,982 | 139,836 | same pages; LTM calc |
| EBIT (EBT plus interest expense, net) | 146,200 | 170,355 | 105,659 | 134,288 | 198,984 | calc; ties to 10-K page:85 and 10-Q Q3 page:23 |
| Depreciation and amortization | 52,155 | 75,021 | 48,401 | 80,073 | 106,693 | 10-K page:59; 10-Q Q3 page:3; LTM calc |
| EBITDA, reported basis | 198,355 | 245,376 | 154,060 | 214,361 | 305,677 | calc; 9M ties to Release Q3 page:7 |
| EBITDA margin | 21.6% | 22.4% | 20.7% | 22.9% | 23.7% | calc |
| Net cash from operations, continuing | 121,582 | 200,396 | 88,299 | 193,377 | 305,474 | 10-K page:59; 10-Q Q3 page:3; LTM calc |
| Capital expenditures | 28,275 | 36,322 | 24,210 | 24,560 | 36,672 | same pages; LTM calc |
| Additions to capitalized software and other | 11,903 | 15,844 | 13,018 | 7,874 | 10,700 | same pages; LTM calc |
| Free cash flow after capex and software (calc) | 81,404 | 148,230 | 51,071 | 160,943 | 258,102 | calc; continuing operations only |
| Interest paid | 14,535 | 17,421 | 16,038 | 13,587 | 14,970 | 10-K page:59; 10-Q Q3 page:4; LTM calc |
| Dividends paid | 8,246 | 8,262 | 6,196 | 6,216 | 8,282 | same pages; LTM calc |
| Acquisition of business, net of cash acquired | 56,383 | 472,006 | 472,006 | 10,232 | 10,232 | same pages; LTM calc |
| Total borrowings, period end | 122,000 | 186,000 | Not supplied: June 30, 2025 debt is not in the supplied sources | 85,000 | 85,000 | 10-K page:80; 10-Q Q3 page:10 |
| Cash and cash equivalents, period end | 65,963 | 101,350 | 78,816 | 73,236 | 73,236 | 10-K page:59; 10-Q Q3 page:4 |
| Net debt (calc) | 56,037 | 84,650 | Not supplied: June 30, 2025 debt is not in the supplied sources | 11,764 | 11,764 | calc |
| Total debt / EBITDA | 0.615x | 0.758x | not annualized | not annualized | 0.278x | calc |
| Net debt / EBITDA | 0.283x | 0.345x | not annualized | not annualized | 0.038x | calc |
| EBITDA / interest paid | 13.65x | 14.09x | not annualized | not annualized | 20.42x | calc |

### Debt instruments and facilities

| Instrument | Borrower and guarantors | Drawn at June 30, 2026 (US$ thousands) | Terms | Locator |
| --- | --- | --- | --- | --- |
| Revolving credit facility, Existing Credit Facility | ESCO Technologies Inc. and certain subsidiaries; guaranteed by material US subsidiaries with a pledge of equity of material foreign subsidiaries (10-K) | 45,000 | Commitment $500 million, plus $250 million increase option with lender consent; matures August 30, 2028; weighted average rate 4.98% for the three months | 10-Q Q3 pages:10 to 11; 10-K page:80 |
| Incremental facility (term loan A) | Same | 40,000, of which 20,000 current | Matures August 30, 2028; weighted average rate 5.25% for the three months; originally a delayed-draw facility of up to $375 million | 10-Q Q3 pages:10 to 11 |
| New Credit Facility (not effective) | ESCO and certain subsidiaries; foreign subsidiaries may also draw | None drawn; effective only with Megger closing | Senior secured revolver $500 million, term loan A $500 million, term loan B $500 million; revolver and term loan A five years, term loan B seven years from the effective date | 10-Q Q3 page:12 |

No notes, bonds or other tranches appear in the debt table (10-Q Q3 page:10). The security statement for the existing facility comes from the 10-K (page:80), and the 10-Q Q3 does not repeat it. The New Credit Facility's security, pricing and guarantors are Not supplied here beyond the label "senior secured".

### Claims outside debt

| Claim | Amount (US$ thousands) | Inside or outside the debt figure | Locator |
| --- | --- | --- | --- |
| Operating lease liabilities | 50,260 present value (6,153 current, 44,107 non-current) | Outside | 10-Q Q3 page:17 |
| Finance lease liabilities | 15,396 present value (1,647 current, 13,749 non-current) | Outside; in other liabilities and accrued other expenses | 10-Q Q3 pages:17 to 18 |
| Letters of credit under the Credit Facility | 12,700 | Outside; reduces revolver availability | 10-Q Q3 page:11 |
| Contract liabilities (customer advances) | 288,142 | Outside; working capital, not financing | 10-Q Q3 page:3 |
| Income tax payable, current | 5,754 (62,007 at September 30, 2025) | Outside | 10-Q Q3 page:3 |
| Megger cash consideration and equity | $0.9 billion cash and equity valued at about $1.4 billion | Outside; not yet closed | 10-Q Q3 page:19 |
| Pensions and retiree medical | Not supplied: no note in the extracted 10-K or 10-Qs | Not applicable | 10-K page:79 |
| Purchase commitments, factoring, supply chain finance | Not supplied: no such term found in the 10-K or 10-Q Q3 | Not applicable | search of both |
| Litigation, environmental | Management states exposure is not material (10-K page:86) | Outside | 10-K page:86; 10-Q Q3 page:26 |

The 10-K states "We had no off-balance-sheet arrangements outstanding at September 30, 2025." (page:40). Future operating lease cash payments total 62,732 undiscounted and finance lease 19,404 (10-Q Q3 page:17).

### Covenants and definitions

- Covenant types: a leverage ratio and an interest coverage ratio (10-K page:80 "The financial covenants of the Credit Facility include a leverage ratio and an interest coverage ratio.").
- Compliance: each 10-Q states compliance, latest 10-Q Q3 page:11 "As of June 30, 2026, the Company was in compliance with all covenants."
- Levels, step-downs, definitions and the issuer's reported ratios: Not supplied. The Amended and Restated Credit Agreement dated August 30, 2023 and Amendment No. 1 are exhibits incorporated by reference (10-Q Q3 page:30) and are not in the pack. Headroom is Not calculable.
- Pricing grid: spread 0.25% to 2.25% over the reference rate and a facility fee of 12.5 to 25 basis points, both varying with the leverage ratio (10-Q Q3 page:11).
- Definition difference: the ratios above use reported EBIT plus D&A and borrowings only. They differ from the agreement's undefined "Consolidated EBITDA" and leverage ratio, from the release's adjusted EBITDA (9M 2026 225,182 and 9M 2025 162,975, Release Q3 page:7) and from any lease-inclusive measure.

### Segment and operating drivers

| Item | Q3 2026 | Q3 2025 | 9M 2026 | 9M 2025 | Locator |
| --- | --- | --- | --- | --- | --- |
| A&D net sales | 168,202 | 136,324 | 462,341 | 307,819 | 10-Q Q3 pages:7 to 9 |
| USG net sales | 99,963 | 92,357 | 280,976 | 269,784 | same |
| Test net sales | 70,862 | 67,663 | 194,710 | 165,111 | same |
| A&D segment profit (EBIT) | 50,418 | 36,577 | 131,372 | 78,246 | same |
| USG segment profit (EBIT) | 21,983 | 21,540 | 63,998 | 62,808 | same |
| Test segment profit (EBIT) | 10,882 | 10,732 | 27,697 | 21,523 | same |
| Consolidated EBITDA, reported | 76,410 | 63,350 | 214,361 | 154,060 | Release Q3 page:7 |

- Growth: 10-Q Q3 page:20 states nine-month net sales "$195.3 million, or 26.3%, higher" and Maritime contributed "$121.1 million of revenue growth in the first nine months of 2026". The Maritime acquisition is a large part of the increase, so organic growth is lower than reported growth.
- Backlog: remaining performance obligations are "$1,540.5 million" at June 30, 2026 (10-Q Q3 page:16), against backlog of 1,133.6 million at September 30, 2025 (10-Q Q3 page:21). Release Q3 page:1 calls the June 30 backlog a "record".
- Weak spot: NRG (renewables) sales fell 5.3 million in Q3 2026 and 14.3 million in the nine months (10-Q Q3 page:20).

### Latest quarter, subsequent events and items after the period

- Megger: signed April 15, 2026, a "Subsequent Event" to the March 31, 2026 balance sheet (10-Q Q2 page:24). Total consideration approximately $2.35 billion; $0.9 billion cash from "existing cash on hand and incremental debt"; equity valued at approximately $1.4 billion; completion expected in the first quarter of fiscal 2027; Megger joins USG (10-Q Q3 page:19). Regulatory filings are underway (Release Q3 page:3).
- Financing: Credit Agreement dated May 29, 2026 with the New Credit Facility sized above, effective only on closing and replacing the Existing Credit Facility (10-Q Q3 page:12). Financing costs of approximately $7 million were expensed in Q3 2026 interest expense (10-Q Q3 page:23). The Release Q3 adjusted EPS excludes "$0.20 of debt financing" for the quarter (page:6).
- Dividend: $0.08 per share, $2.1 million, paid July 17, 2026, after the period (10-Q Q3 page:25). The next dividend of $0.08 per share is announced for October 15, 2026 (Release Q3 page:3).
- VACCO: sold July 18, 2025 for net proceeds of approximately $270 million, proceeds mainly used to pay down debt (10-K page:32). In Q2 2026 the Company paid approximately $59 million of cash taxes on the gain (10-Q Q3 page:25), shown in discontinued operations cash flow of (59,340) for the nine months (10-Q Q3 page:3).
- Guidance: Release Q3 page:3 raises FY2026 sales guidance to "$1.30 to $1.33 billion" and adjusted EPS to "$8.30 - $8.40". These are management expectations, not evidence of results.
- After August 10, 2026: nothing is supplied. Closing status, borrowings under the New Credit Facility and any equity issuance at the as-of date are Not supplied.

### Definition review

| Definition | Source | Treatment here |
| --- | --- | --- |
| EBIT | Release Q3 page:4 "The Company defines “EBIT” as earnings before interest and taxes" | Used as EBT plus interest expense, net; ties to 10-Q Q3 page:23 |
| EBITDA | Release Q3 page:4, earnings before interest, taxes, depreciation and amortization | EBIT plus D&A from the cash flow statement; matches the release quarterly "Consolidated EBITDA" for Q1, Q2, Q3 and the nine months |
| Adjusted EBITDA and Adjusted EBIT | Release Q3 page:4, excluding items in the reconciliation | Not used in ratios; adjusted EBIT excludes acquisition-related amortization, restructuring, Megger financing and acquisition costs; LTM adjusted EBITDA is Not calculable because the FY2025 adjusted figure is not supplied |
| Total debt | 10-Q Q3 page:10 "Total borrowings" | Revolver plus term loan A; excludes leases and letters of credit |
| Interest paid | Cash flow supplemental line | Used as cash interest; not split by continuing and discontinued operations |
| Covenant leverage and interest coverage | 10-K page:80 | Definitions Not supplied |

### Narrative review

#### Leverage

On the reported basis, leverage is low and falling: total debt to EBITDA of 0.758x at FY2025 compares with 0.278x for the LTM to June 30, 2026, with total borrowings down 101,000 (thousands) from 186,000 to 85,000 over nine months. The mechanism was operating cash flow from continuing operations of 193,377 funding net repayment of 101,000 (231,000 repaid less 130,000 borrowed), the 59,340 discontinued-operations outflow, capital spending and dividends (10-Q Q3 pages:3 and 4). The credit implication is limited headroom risk today, but the May 29, 2026 agreement and the equity-and-cash purchase price mean the position is expected to change. Illustrative sensitivity only: if the full $0.9 billion cash consideration were borrowed on top of current debt, total debt would be about 3.22x LTM ESCO-only EBITDA before Megger earnings, fees and any cash used. This is a bound on method, not a forecast, and Megger EBITDA is Not supplied.

#### Coverage

Cash interest cover is about twenty times on LTM figures. The 10-Q Q3 cites "lower average outstanding borrowings" and "lower average interest rates" as partial offsets to the higher interest expense (page:23), which is consistent with the low cash interest in the denominator. Cover on interest expense, net is lower because Q3 2026 includes about 7 million of financing costs; on that basis LTM EBITDA is 15.99 times the 19,121 charge (see Calculations). Post-closing interest on up to $1.5 billion of committed term and revolver capacity is Not supplied.

#### Cash flow quality

Continuing operations produced 193,377 of operating cash flow in nine months against 88,299, an increase that the 10-Q Q3 attributes to "lower working capital requirements and higher earnings" (page:24). Contract liabilities rose 71.5 million "due to timing of payments received from customers" (page:24), which is customer advance timing that can reverse. Discontinued operations used 59,340, largely VACCO gain tax, so total operating cash flow was 134,037. Free cash flow of 258,102 for the LTM period is therefore a continuing-operations figure before that one-time tax and before dividends; it should not be read as the cash available after all outflows.

#### Liquidity

Liquidity at June 30, 2026 is 515.536 (US$m): cash 73.236 and undrawn revolver 442.300 after 12.7 of letters of credit. The Existing Credit Facility runs to August 30, 2028 with no maturity in the next twelve months other than the 20.0 current portion. Cash fell from 101.350 at September 30, 2025 as debt was repaid. Liquidity after closing depends on the New Credit Facility, which is not effective and not supplied beyond its sizes.

#### Data quality

Statements are tied: segment profit reconciles to EBT (10-Q Q3 pages:8 and 9), the 10-K and 10-Q Q3 print the same September 30, 2025 total assets, and the release quarterly EBITDA sums to the nine-month figure. Open points are the contract-liabilities note against the balance sheet caption (10-Q Q3 page:16 "$293.4 million" against 288,142 on page:3, unexplained), Release Q3 printing "Interest expense" where the 10-Q prints "Interest expense, net" (same amount), and the release's single "Other current liabilities" line. No restatement notice appears in the supplied filings other than the VACCO recast.

#### Definition risks

The agreement's leverage and coverage definitions are Not supplied, so no reported ratio here is a covenant ratio. Release adjusted measures exclude acquisition amortization and deal costs, and adjusted EBITDA is not a lender definition. Net debt here excludes finance and operating leases. Including finance leases alone the LTM leverage is 0.328x, and including operating leases as well 0.493x (see Calculations).

#### Key gaps

Covenant levels and ratios; the New Credit Facility terms; Megger financials; pro forma debt and interest; the repayment schedule of term loan A; discrete Q3 cash flow; June 30, 2025 debt (needed for a 9M 2025 balance column); pension and retiree medical; and anything after August 10, 2026.

### Downstream readiness

| Consumer | Requirement | Status | Basis and action |
| --- | --- | --- | --- |
| CP-1A | Business and transaction facts | limited | Segments, VACCO, Maritime and Megger terms are in the 10-Q Q3; Megger agreements not supplied |
| CP-2 | Debt, liquidity, leverage, coverage | sufficient for reported basis; limited for covenants | Use the chart tables; mark covenant headroom and pro forma leverage Not supplied |
| CP-2 | Maturity profile | limited | Only 20.0 current and 65.0 by August 30, 2028; no schedule |
| CP-5 | Trace of figures | sufficient | Every figure here has a page locator and recomputation in Calculations |

### Quality review

| Claim | Material | Lineage | Note |
| --- | --- | --- | --- |
| Total borrowings of 85,000 at June 30, 2026 | Yes | Directly Sourced | 10-Q Q3 page:10 |
| LTM EBITDA of 305,677 | Yes | Calculated | Components all located; not a reported figure |
| Undrawn revolver of 442.300 | Yes | Calculated | Company states approximately 442 |
| Total debt to EBITDA of 0.278x | Yes | Calculated | Reported basis, not covenant |
| Covenant headroom | Yes | Insufficient Information | Levels not supplied |
| Illustrative 3.22x with full cash consideration borrowed | Yes | Analyst Inference | Assumption: all $0.9 billion borrowed, no cash used, Megger EBITDA omitted |

## Calculations

All inputs are US$ thousands as printed, with locators in the tables above. No input was replaced with zero.

### EBIT and EBITDA

- EBIT = earnings before income taxes + interest expense, net.
  - FY2024: 130,953 + 15,247 = 146,200. FY2025: 152,853 + 17,502 = 170,355. 9M 2025: 93,286 + 12,373 = 105,659. 9M 2026: 120,296 + 13,992 = 134,288. LTM: 179,863 + 19,121 = 198,984.
  - Checks: FY2024 and FY2025 equal segment profit after corporate on 10-K page:85 (146,200 and 170,355); 9M figures equal EBIT on 10-Q Q3 page:23.
- EBITDA = EBIT + D&A (cash flow statement; continuing operations because the same statement removes discontinued earnings before adding D&A).
  - FY2024: 146,200 + 52,155 = 198,355. FY2025: 170,355 + 75,021 = 245,376. 9M 2025: 105,659 + 48,401 = 154,060. 9M 2026: 134,288 + 80,073 = 214,361.
  - Checks against Release Q3 page:7: 214,361 and 154,060 match.
  - Quarterly sum check: Q1 2026 64,851 + Q2 2026 73,100 + Q3 2026 76,410 = 214,361. Q1 2025 41,025 + Q2 2025 49,685 + Q3 2025 63,350 = 154,060.
- LTM = FY2025 + 9M 2026 - 9M 2025, for every flow row.
  - EBITDA: 245,376 + 214,361 - 154,060 = 305,677. D&A: 75,021 + 80,073 - 48,401 = 106,693. Net sales: 1,095,388 + 938,027 - 742,714 = 1,290,701. EBT: 152,853 + 120,296 - 93,286 = 179,863. Interest expense, net: 17,502 + 13,992 - 12,373 = 19,121. SG&A: 234,638 + 195,039 - 171,305 = 258,372. Amortization: 53,317 + 61,086 - 32,735 = 81,668. Tax: 36,554 + 25,314 - 21,841 = 40,027. Earnings from continuing operations: 116,299 + 94,982 - 71,445 = 139,836.
  - Operating cash flow: 200,396 + 193,377 - 88,299 = 305,474. Capex: 36,322 + 24,560 - 24,210 = 36,672. Capitalized software: 15,844 + 7,874 - 13,018 = 10,700. Interest paid: 17,421 + 13,587 - 16,038 = 14,970. Dividends: 8,262 + 6,216 - 6,196 = 8,282. Acquisitions: 472,006 + 10,232 - 472,006 = 10,232.
- EBITDA margin = EBITDA / net sales: 198,355 / 919,127 = 21.6%; 245,376 / 1,095,388 = 22.4%; 154,060 / 742,714 = 20.7%; 214,361 / 938,027 = 22.9%; 305,677 / 1,290,701 = 23.7%.
- LTM at December 31, 2025: 245,376 + 64,851 - 41,025 = 269,202. LTM at March 31, 2026: 245,376 + 137,951 - 90,710 = 292,617 (six-month EBITDA from Release Q2 page:7 and its comparative; Q1 2026 EBITDA 64,851 and Q1 2025 EBITDA 41,025 from Release Q1 page:6).
- Interest paid LTM at December 31, 2025: 17,421 + 2,689 - 2,567 = 17,543. At March 31, 2026: 17,421 + 4,958 - 8,821 = 13,558.

### Free cash flow

- FCF = net cash from operating activities, continuing operations - capital expenditures - additions to capitalized software and other, before dividends and acquisitions.
  - FY2024: 121,582 - 28,275 - 11,903 = 81,404. FY2025: 200,396 - 36,322 - 15,844 = 148,230. 9M 2025: 88,299 - 24,210 - 13,018 = 51,071. 9M 2026: 193,377 - 24,560 - 7,874 = 160,943. LTM: 305,474 - 36,672 - 10,700 = 258,102.
- Total operating cash flow 9M 2026 = 193,377 + (59,340 outflow) = 134,037, which equals the printed figure (10-Q Q3 page:3).

### Leverage, net debt and cover

- Net debt = total borrowings - cash and cash equivalents. FY2024: 122,000 - 65,963 = 56,037. FY2025: 186,000 - 101,350 = 84,650. December 31, 2025: 145,511 - 103,824 = 41,687. March 31, 2026: 145,000 - 92,252 = 52,748. June 30, 2026: 85,000 - 73,236 = 11,764.
- Total debt / EBITDA: 122,000 / 198,355 = 0.615x; 186,000 / 245,376 = 0.758x; 145,511 / 269,202 = 0.541x; 145,000 / 292,617 = 0.496x; 85,000 / 305,677 = 0.278x.
- Net debt / EBITDA: 56,037 / 198,355 = 0.283x; 84,650 / 245,376 = 0.345x; 41,687 / 269,202 = 0.155x; 52,748 / 292,617 = 0.180x; 11,764 / 305,677 = 0.038x.
- EBITDA / interest paid: 198,355 / 14,535 = 13.65x; 245,376 / 17,421 = 14.09x; 269,202 / 17,543 = 15.35x; 292,617 / 13,558 = 21.58x; 305,677 / 14,970 = 20.42x.
- EBITDA / interest expense, net, LTM: 305,677 / 19,121 = 15.99x.
- Including leases at June 30, 2026: (85,000 + 15,396) / 305,677 = 0.328x; (85,000 + 15,396 + 50,260) / 305,677 = 0.493x.
- Illustrative sensitivity (not pro forma): (85,000 + 900,000) / 305,677 = 3.22x. Inputs: June 30, 2026 borrowings plus the $0.9 billion cash consideration from 10-Q Q3 page:19, assuming it is all borrowed, no cash is used, fees are nil and Megger EBITDA is zero. It overstates leverage by omitting Megger EBITDA and understates it by omitting fees and any other costs.

### Liquidity

- Undrawn revolver = commitment 500,000 - drawn - letters of credit. September 30, 2025: 500,000 - 25,000 - 10,100 = 464,900. December 31, 2025: 500,000 - 20,511 - 10,700 = 468,789 (the 20,511 is revolver plus short-term borrowings as printed). March 31, 2026: 500,000 - 45,000 - 14,500 = 440,500. June 30, 2026: 500,000 - 45,000 - 12,700 = 442,300.
- Liquidity at June 30, 2026 = 73,236 + 442,300 = 515,536. At September 30, 2025 = 101,350 + 464,900 = 566,250.
- Implied Q4 2025 (September 30, 2025 quarter) net sales = 1,095,388 - 742,714 = 352,674 and EBITDA = 245,376 - 154,060 = 91,316, shown only to explain the LTM bridge.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Covenant levels, definitions and reported ratios not supplied | High | CP-2, CP-5 | Supply the 2023 Amended and Restated Credit Agreement, Amendment No. 1 and any compliance certificate |
| New Credit Facility terms (pricing, covenants, conditions, guarantors) and amounts drawn at closing not supplied | High | CP-2 | Supply the May 29, 2026 Credit Agreement (Exhibit 10.3, Form 8-K filed June 3, 2026) |
| Megger financial statements and pro forma debt, interest and EBITDA not supplied | High | CP-1A, CP-2 | Supply Megger financials or pro forma information |
| No filing dated after August 10, 2026; Megger closing status unknown | High | All | Supply later 8-Ks or confirm none |
| Term loan A repayment schedule not printed; fiscal-year maturity split Not supplied | Medium | CP-2 | Supply the credit agreement or amortization schedule |
| Release adjusted EBITDA cannot be extended to an LTM figure because the FY2025 adjusted figure is not supplied | Medium | CP-2 | Supply the fiscal Q4 2025 release |
| Contract liabilities note totals differ from the balance sheet caption without explanation | Medium | CP-1 | Locate the explanation in the filed HTML |
| Nine-month cash flows only for Q3 2026; no discrete quarterly cash flow | Medium | CP-2 | Derive only if Q2 six-month and Q3 nine-month inputs are used, and label as derived |
| Interest paid not split between continuing and discontinued operations | Low | CP-2 | Check the filed notes |
| Undrawn portion of the incremental delayed-draw facility not stated | Low | CP-2 | Supply the credit agreement |
| Pension, retiree medical, purchase commitments, factoring: nothing found in the supplied text | Low | CP-2 | Treat as Not supplied |
| Debt at June 30, 2025 not supplied (needed for a 9M 2025 balance column) | Low | CP-1 | Supply the Q3 FY2025 10-Q |
| Revolver commitment at September 30, 2024 not stated, so FY2024 undrawn facilities are Not supplied | Low | CP-2 | Supply the FY2024 10-K |

## Next module

- CP-1A: carry the Megger transaction (signed April 15, 2026; approximately $2.35 billion; $0.9 billion cash and equity valued at about $1.4 billion; expected closing first quarter of fiscal 2027; New Credit Facility of $1.5 billion in three tranches, effective only at closing) and treat all terms beyond the 10-Q Q3 summary as Not supplied. Keep the VACCO and Maritime history on the continuing-operations perimeter.
- CP-2: use the chart tables as the reported base; build liquidity from the printed inputs; name the two covenant types and leave levels and headroom Not supplied; treat the 3.22x figure only as an illustrative bound; do not describe post-closing leverage or interest cover as known.
- CP-5: trace each figure by page locator; note that EBITDA, LTM, free cash flow, net debt, ratios and undrawn facilities are calculated, not printed, and that the covenant ratio is not computed.
