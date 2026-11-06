# CP-1 — Financial statements and credit metrics: TransDigm Group Incorporated (tdg)

## Request

- Issuer: TransDigm Group Incorporated (issuer id `tdg`), as of 2024-09-30.
- Run: `tdg-2024-09-30-credit_snapshot-host`, pathway `credit_snapshot`. This module feeds CP-1A and the report section "Financials and credit metrics".
- Execution: host session. The host read the pinned filings and wrote this answer. No provider was called. Calculations were done separately from the extracted figures and are shown in `## Calculations`.
- Scope: reported FY2024, FY2023 and FY2022 consolidated statements of TD Group, the FY2024 debt register, the issuer's EBITDA and EBITDA As Defined, FY2024 quarterly net sales, and bounded credit metrics. No rating, recovery, covenant compliance test or forecast.

## Sources

| Source | sha256 | Used for |
| --- | --- | --- |
| TDG_2024-09-30_10-K_0001260221-24-000083_tdg-20240930.htm.jsonl | d75c469fdb1966dd895c0f6faa6d5179b380d3ed95aa00aca99aa258059edab6 | Controlling source: audited statements, debt note, liquidity, non-GAAP reconciliation |
| TDG_2024-03-30_10-Q_0001260221-24-000046_tdg-20240330.htm.jsonl | fcec3566cfda08c82a8aaed7289c6440cc05d12976f237cd72a32cf9fbfb2ed6 | Second fiscal quarter FY2024 and 26-week net sales |
| TDG_2024-06-29_10-Q_0001260221-24-000069_tdg-20240629.htm.jsonl | ce1b0541d5e8222dc536d748942a3cb51236d7ff62d8613b002460bd8b41dcf2 | Third fiscal quarter FY2024 and 39-week net sales |
| TDG_2024-12-28_10-Q_0001260221-25-000014_tdg-20241228.htm.jsonl | ec98b47e6ebad9663286dc04b35dade04d11e7d12c3642ddaa6ef549a33d671f | Comparative column only: quarter ended December 30, 2023 (filed after the as-of date) |
| TDG_FY2024_annual-report_SEC-PDF_0001260221-25-000008_a841225transdigmgroupbookm.pdf | dc6a8ea6249e4e919d190a4bbb459d9bf4eded005b7d5680ae911b32d44d44af | Not used for figures: duplicate presentation of the same 10-K (CP-0) |
| context | f7b95e1ff471b47547a3ac86cb68e7e7144a06231f6e94de0eee48e0c6828449 | Run settings: currency USD, current period fy-2024, prior period fy-2023 |

Supplied handoff consumed: CP-0 sha256 bf1d2cc15a7725607055c4773e4b852c698185e8c28692b2df7b63d6967e0a7e. Carried forward from CP-0: the HTML 10-K controls; the PDF is a duplicate and is not counted as corroboration; no 10-Q for the first fiscal quarter of FY2024; no executed debt documents; October 2024 subsequent events.

Locators: `10-K page N` and `10-Q page N` are extracted-text pages of the pinned `.jsonl` sources.

## Findings

### Source context

| Source | Entity and perimeter | Periods | Statement kind | Units and currency |
| --- | --- | --- | --- | --- |
| 10-K FY2024 | TransDigm Group Incorporated and subsidiaries, consolidated | Fiscal years ended September 30, 2024, 2023 and 2022; balance sheets at September 30, 2024 and 2023 | Audited consolidated statements (Ernst & Young LLP opinion dated November 7, 2024, 10-K page 120) | "Amounts in millions, except per share amounts" (10-K page 121); USD |
| 10-Q for March 30, 2024 | Same consolidated perimeter | Thirteen and twenty-six weeks ended March 30, 2024 | Unaudited condensed | Millions; USD |
| 10-Q for June 29, 2024 | Same consolidated perimeter | Thirteen and thirty-nine weeks ended June 29, 2024 | Unaudited condensed | Millions; USD |
| 10-Q for December 28, 2024 | Same consolidated perimeter | Thirteen weeks ended December 28, 2024, with comparative thirteen weeks ended December 30, 2023 | Unaudited condensed; filed after the as-of date | Millions; USD |

All annual figures below are TD Group consolidated, U.S. GAAP, USD millions, unless a row says otherwise. Balance-sheet values are instants at September 30. Income-statement and cash-flow values are fiscal-year flows from October 1 to September 30.

### Financials and credit metrics

| Metric | FY2024 | FY2023 | Basis and source |
| --- | --- | --- | --- |
| Net sales (USD m) | 7,940 | 6,585 | Reported, 10-K page 121 |
| Gross profit (USD m) | 4,672 | 3,842 | Reported, 10-K page 121 |
| Income from operations (USD m) | 3,531 | 2,923 | Reported, 10-K page 121 |
| Net income (USD m) | 1,715 | 1,299 | Reported, 10-K page 121 |
| EBITDA, issuer-defined (USD m) | 3,813 | 3,148 | Reported non-GAAP, 10-K page 71 |
| EBITDA As Defined, issuer-defined (USD m) | 4,173 | 3,395 | Reported non-GAAP, 10-K page 71 |
| Interest expense—net (USD m) | 1,286 | 1,164 | Reported, 10-K page 121 |
| Cash paid for interest, net (USD m) | 1,158 | 1,160 | Reported, 10-K page 123 |
| Net cash provided by operating activities (USD m) | 2,045 | 1,375 | Reported, 10-K page 123 |
| Capital expenditures (USD m) | (165) | (139) | Reported, 10-K page 123 |
| Free cash flow, CFO less capex (USD m) | 1,880 | 1,236 | Calculated, C1 |
| Cash and cash equivalents (USD m) | 6,261 | 3,472 | Reported, 10-K page 120 |
| Total debt, carrying amount incl. securitization (USD m) | 24,880 | 19,750 | Reported, 10-K page 52, footnote: "Includes debt issuance costs and original issue discount and premiums" |
| Net debt, carrying (USD m) | 18,619 | 16,278 | Calculated, C2 |
| Total debt / EBITDA As Defined (x) | 5.96 | 5.82 | Calculated, C3 |
| Total debt / EBITDA (x) | 6.53 | 6.27 | Calculated, C3 |
| Net debt / EBITDA As Defined (x) | 4.46 | 4.79 | Calculated, C3 |
| EBITDA As Defined / interest expense—net (x) | 3.24 | 2.92 | Calculated, C4 |
| EBITDA / interest expense—net (x) | 2.97 | 2.70 | Calculated, C4 |
| EBITDA As Defined margin (%) | 52.6 | 51.6 | Calculated, C5 |
| Total stockholders' deficit (USD m) | (6,283) | (1,978) | Reported, 10-K page 120 |

Pro forma for the October 2024 special dividend payment, net debt on a carrying basis would be 22,967 and net debt / EBITDA As Defined 5.50x (C6). This is a labelled sensitivity, not a reported figure.

### Reported income statement

| Line (as printed) | FY2024 | FY2023 | FY2022 |
| --- | --- | --- | --- |
| NET SALES | 7,940 | 6,585 | 5,429 |
| COST OF SALES | 3,268 | 2,743 | 2,330 |
| GROSS PROFIT | 4,672 | 3,842 | 3,099 |
| SELLING AND ADMINISTRATIVE EXPENSES | 980 | 780 | 748 |
| AMORTIZATION OF INTANGIBLE ASSETS | 161 | 139 | 136 |
| INCOME FROM OPERATIONS | 3,531 | 2,923 | 2,215 |
| INTEREST EXPENSE—NET | 1,286 | 1,164 | 1,076 |
| REFINANCING COSTS | 58 | 56 | 1 |
| OTHER (INCOME) EXPENSE | (28) | (13) | 11 |
| INCOME FROM CONTINUING OPERATIONS BEFORE INCOME TAXES | 2,215 | 1,716 | 1,127 |
| INCOME TAX PROVISION | 500 | 417 | 261 |
| INCOME FROM CONTINUING OPERATIONS | 1,715 | 1,299 | 866 |
| INCOME FROM DISCONTINUED OPERATIONS, NET OF TAX | — | — | 1 |
| NET INCOME | 1,715 | 1,299 | 867 |
| NET INCOME ATTRIBUTABLE TO TD GROUP | 1,714 | 1,298 | 866 |
| Earnings per share (USD per share) | 25.62 | 22.03 | 13.40 |
| Cash dividends declared per common share (USD per share) | 110.00 | — | 18.50 |

Source: 10-K page 121. Expenses are printed as positive magnitudes and are kept in that presentation; "(28)" under other (income) expense is printed income. "—" is the printed dash, not a missing value. Per-share rows are USD per share, not USD millions.

The expense block between gross profit and income from operations is selling and administrative expenses plus amortization of intangible assets, and it reconciles exactly in each year (C7). Total depreciation and amortization of 312 (10-K page 71) is a different, wider measure and is not the income-statement amortization line.

### Reported balance sheet

| Line (as printed) | September 30, 2024 | September 30, 2023 |
| --- | --- | --- |
| Cash and cash equivalents | 6,261 | 3,472 |
| Trade accounts receivable—Net | 1,381 | 1,230 |
| Inventories—Net | 1,876 | 1,616 |
| Prepaid expenses and other | 511 | 420 |
| Total current assets | 10,029 | 6,738 |
| PROPERTY, PLANT AND EQUIPMENT—NET | 1,488 | 1,255 |
| GOODWILL | 10,419 | 8,988 |
| OTHER INTANGIBLE ASSETS—NET | 3,446 | 2,747 |
| OTHER NON-CURRENT ASSETS | 204 | 242 |
| TOTAL ASSETS | 25,586 | 19,970 |
| Current portion of long-term debt | 98 | 71 |
| Short-term borrowings—trade receivable securitization facility | 486 | 349 |
| Accounts payable | 323 | 305 |
| Dividends payable | 4,216 | — |
| Accrued and other current liabilities | 1,216 | 854 |
| Total current liabilities | 6,339 | 1,579 |
| LONG-TERM DEBT | 24,296 | 19,330 |
| DEFERRED INCOME TAXES | 766 | 627 |
| OTHER NON-CURRENT LIABILITIES | 468 | 412 |
| Total liabilities | 31,869 | 21,948 |
| Total TD Group stockholders’ deficit | (6,290) | (1,984) |
| NONCONTROLLING INTERESTS | 7 | 6 |
| Total stockholders’ deficit | (6,283) | (1,978) |
| TOTAL LIABILITIES AND STOCKHOLDERS’ DEFICIT | 25,586 | 19,970 |

Source: 10-K page 120. Totals were checked against their printed components (C8). Goodwill and other intangible assets together exceed total current assets; tangible equity is not calculated here.

### Reported cash flows (selected lines)

| Line (as printed) | FY2024 | FY2023 | FY2022 |
| --- | --- | --- | --- |
| Net cash provided by operating activities | 2,045 | 1,375 | 948 |
| Capital expenditures | (165) | (139) | (119) |
| Acquisition of businesses, net of cash acquired | (2,347) | (762) | (437) |
| Net cash used in investing activities | (2,441) | (900) | (553) |
| Dividends and dividend equivalent payments | (2,038) | (38) | (1,091) |
| Repurchases of common stock | — | — | (912) |
| Proceeds from issuance of senior secured notes, net | 7,373 | 3,504 | — |
| Repayments of senior secured notes | (4,400) | (1,122) | — |
| Repayments of senior subordinated notes, net | (550) | (1,459) | — |
| Proceeds from term loans, net | 6,815 | 6,238 | — |
| Repayment on term loans | (4,403) | (7,334) | (75) |
| Net cash provided by (used in) financing activities | 3,171 | (16) | (2,148) |
| NET INCREASE (DECREASE) IN CASH AND CASH EQUIVALENTS | 2,789 | 471 | (1,786) |
| Cash paid during the period for interest, net | 1,158 | 1,160 | 1,057 |
| Cash paid during the period for income taxes, net of refunds | 539 | 260 | 220 |

Source: 10-K page 123. Outflows are printed in parentheses and kept signed. The cash roll-forward reconciles to the closing balance (C9).

### Debt register at September 30, 2024

| Instrument (as printed) | Gross amount | Debt issuance costs | Original issue (discount) premium | Net amount |
| --- | --- | --- | --- | --- |
| Short-term borrowings—trade receivable securitization facility | 487 | (1) | — | 486 |
| Term loans | 8,702 | (25) | (35) | 8,642 |
| 5.50% senior subordinated notes due 2027 | 2,650 | (9) | — | 2,641 |
| 6.75% secured notes due 2028 | 2,100 | (15) | (8) | 2,077 |
| 4.625% senior subordinated notes due 2029 | 1,200 | (6) | — | 1,194 |
| 6.375% secured notes due 2029 | 2,750 | (22) | (1) | 2,727 |
| 4.875% senior subordinated notes due 2029 | 750 | (4) | — | 746 |
| 6.875% secured notes due 2030 | 1,450 | (12) | — | 1,438 |
| 7.125% secured notes due 2031 | 1,000 | (9) | (7) | 984 |
| 6.625% secured notes due 2032 | 2,200 | (20) | — | 2,180 |
| 6.00% secured notes due 2033 | 1,500 | (14) | — | 1,486 |
| Government refundable advances | 17 | — | — | 17 |
| Finance lease obligations | 262 | — | — | 262 |
| Printed subtotal, excluding the securitization row | 24,581 | (136) | (51) | 24,394 |

Source: 10-K pages 144 to 145. The printed subtotal of 24,581 excludes the securitization row; the printed components add to it exactly (C10). Gross principal including securitization is 25,068 (C10, calculated). The MD&A "Total debt" of 24,880 is the net carrying amount including securitization (C11). The term loans are described as "$8,702 million in fully drawn term loans" with "an $910 million revolving credit facility" (10-K page 59). The 10-K states: "There is no maturity on any tranche of term loans or notes until November 2027 (fiscal 2028)" (10-K page 56).

Secured and subordinated classes are identified by instrument name only. Ranking, guarantees and collateral come from the 10-K description (CP-0), not from executed documents.

### Liquidity at September 30, 2024

| Component (as printed) | Amount (USD m) | Source |
| --- | --- | --- |
| Cash and cash equivalents | 6,261 | 10-K page 55 |
| Availability on revolving credit facility | 843 | 10-K page 55 |
| Availability on Securitization Facility | 163 | 10-K page 55 |
| Cash liquidity | 7,267 | 10-K page 55 |
| Pro forma cash liquidity after the October 2024 special dividend payment | 2,919 | 10-K page 56, footnote (1) to the page 55 table |

The 10-K footnote states: "When considering the impact of the $4,348 million payment in special dividends and dividend equivalents in October 2024, the pro forma cash liquidity as of September 30, 2024 is $2,919 million." Revolver availability is after "$67 million in letters of credit outstanding" (10-K page 59). The securitization availability was drawn after the year end: "The Company drew the remaining $162.5 million available under the Securitization Facility in October 2024" (10-K page 152).

### Issuer non-GAAP measures and definition review

| Line (as printed) | FY2024 | FY2023 |
| --- | --- | --- |
| Net Income | 1,715 | 1,299 |
| Depreciation and amortization expense | 312 | 268 |
| Interest expense-net | 1,286 | 1,164 |
| Income tax provision | 500 | 417 |
| EBITDA | 3,813 | 3,148 |
| Acquisition transaction and integration-related expenses | 70 | 18 |
| Non-cash stock and deferred compensation expense | 217 | 157 |
| Refinancing costs | 58 | 56 |
| Other, net | 15 | 16 |
| EBITDA As Defined | 4,173 | 3,395 |

Source: 10-K page 71. Both reconciliations (from net income and from operating cash flow) reach the same EBITDA and EBITDA As Defined, and the net-income bridge adds exactly (C12).

- Definition: EBITDA As Defined is issuer-defined. The 10-K says neither measure "is a measurement of financial performance under U.S. GAAP" (10-K page 71). Its add-backs include non-cash stock compensation and integration costs. The issuer itself notes that EBITDA As Defined "excludes the cash expense we have incurred to integrate acquired businesses" (10-K page 70).
- Covenant alignment: the issuer uses the name "As Defined", but the executed Credit Agreement is not supplied (CP-0). This handoff does not claim that EBITDA As Defined equals any covenant EBITDA.
- Depreciation and amortization of 312 equals depreciation of 149 plus "Amortization of intangible assets and product certification costs" of 163 from the cash-flow statement (10-K page 122). It is wider than the income-statement amortization line of 161.

### FY2024 quarterly net sales

| Period | Net sales (USD m) | Basis and source |
| --- | --- | --- |
| Thirteen weeks ended December 30, 2023 | 1,789 | Reported as the comparative column of the 10-Q for December 28, 2024, page 3 (filed after the as-of date) |
| Thirteen weeks ended March 30, 2024 | 1,919 | Reported, 10-Q for March 30, 2024, page 3 |
| Thirteen weeks ended June 29, 2024 | 2,046 | Reported, 10-Q for June 29, 2024, page 3 |
| Fourth fiscal quarter of FY2024 | 2,186 | Calculated, C13: fiscal year less 39 weeks; not reported |
| Twenty-six weeks ended March 30, 2024 | 3,708 | Reported, 10-Q for March 30, 2024, page 3 |
| Thirty-nine weeks ended June 29, 2024 | 5,754 | Reported, 10-Q for June 29, 2024, page 3 |

The two reported quarters and the comparative first quarter add exactly to the printed year-to-date figures (C13). The fourth-quarter figure is derived and must stay labelled as calculated.

### Narrative review

- Leverage: total debt on a carrying basis rose from 19,750 to 24,880 while EBITDA As Defined rose from 3,395 to 4,173. Gross leverage on EBITDA As Defined moved from 5.82x to 5.96x; on reported EBITDA it is 6.53x. Mechanism: new term loans and secured notes funded acquisitions and special dividends (cash-flow lines above). Credit implication: leverage is high and rose slightly despite strong earnings growth. Net leverage at the year end is flattered by cash that was paid out as a dividend in October 2024; the labelled pro forma figure is 5.50x.
- Coverage: EBITDA As Defined covers net interest expense 3.24x in FY2024, up from 2.92x. Cash interest paid of 1,158 is lower than the expense of 1,286; the 10-K footnote shows interest in the operating-cash reconciliation excludes amortization of issuance costs and discount (10-K page 71). About 77% of gross debt was fixed rate (10-K page 55), so coverage is partly protected from rate moves; the hedge detail is not analysed here.
- Cash flow quality: operating cash flow rose from 1,375 to 2,045 and free cash flow (CFO less capex) from 1,236 to 1,880. Capex is small relative to sales. Working-capital lines absorbed cash in FY2024 (receivables and inventories printed as outflows, 10-K page 123). The gap between EBITDA As Defined and operating cash flow is mainly cash interest and cash taxes.
- Liquidity: reported cash liquidity of 7,267 at the year end falls to a pro forma 2,919 after the October 2024 dividend payment, as stated by the issuer. No debt matures until November 2027. The securitization facility was fully drawn in October 2024.
- Data quality: the annual statements are audited and internally consistent; all checked totals reconcile (C7 to C13). Interim figures are unaudited. The first FY2024 quarter comes from a later filing's comparative column.
- Definition risks: EBITDA As Defined is issuer-defined with material add-backs (stock compensation 217 in FY2024). Covenant EBITDA cannot be confirmed without the Credit Agreement.
- Key gaps: executed debt documents; first-quarter FY2024 10-Q; obligor-group statements beyond the 10-K summary; no forecast, rating or market data in scope.

### Readiness for CP-1A

| Requirement | Status | Basis |
| --- | --- | --- |
| Consolidated statements and credit metrics for the business and capital-structure description | Sufficient | Audited FY2024 statements and debt register above |
| Debt instrument list for the transaction summary | Limited | Instrument names, amounts and the no-maturity-before-November-2027 statement are located; executed terms are not supplied |
| Subsequent events at the as-of boundary | Sufficient | October 2024 dividend payment and securitization draw are located and dated |
| Segment financials | Not extracted here | CP-1A reads segments from the 10-K directly (CP-0 located the segment note) |

### Quality review of claims

| Claim | Material | Lineage | Note |
| --- | --- | --- | --- |
| Gross leverage on EBITDA As Defined is 5.96x in FY2024 | Yes | Calculated | From reported total debt and issuer EBITDA As Defined; the denominator is issuer-defined |
| Pro forma net leverage is 5.50x | Yes | Calculated | Uses the issuer's stated October 2024 payment; other October cash flows ignored |
| Interest coverage is 3.24x | Yes | Calculated | Net interest expense basis, not cash interest |
| No maturity before November 2027 | Yes | Directly Sourced | 10-K page 56 |
| Fourth-quarter FY2024 net sales of 2,186 | No | Calculated | Derived, not reported |
| Covenant headroom | Yes | Insufficient Information | Credit Agreement not supplied |

Open quality findings: one MATERIAL finding, covenant definitions not verifiable (no executed Credit Agreement). One MINOR finding, the first FY2024 quarter is sourced from a later filing's comparative column.

## Calculations

All inputs are USD millions copied from the cited pages. Results are rounded half up to two decimals for ratios and one decimal for percentages.

| ID | Formula | Inputs and locators | Result |
| --- | --- | --- | --- |
| C1 | Operating cash flow less capital expenditures | FY2024: 2,045 less 165; FY2023: 1,375 less 139 (10-K page 123) | 1,880; 1,236 |
| C2 | Total debt less cash and cash equivalents | FY2024: 24,880 less 6,261; FY2023: 19,750 less 3,472 (10-K pages 52, 120) | 18,619; 16,278 |
| C3 | Total debt divided by EBITDA As Defined; total debt divided by EBITDA; net debt divided by EBITDA As Defined | FY2024: 24,880 / 4,173; 24,880 / 3,813; 18,619 / 4,173. FY2023: 19,750 / 3,395; 19,750 / 3,148; 16,278 / 3,395 (10-K pages 52, 71) | FY2024: 5.96x; 6.53x; 4.46x. FY2023: 5.82x; 6.27x; 4.79x |
| C4 | EBITDA As Defined divided by interest expense—net; EBITDA divided by interest expense—net | FY2024: 4,173 / 1,286; 3,813 / 1,286. FY2023: 3,395 / 1,164; 3,148 / 1,164 (10-K pages 71, 121) | FY2024: 3.24x; 2.97x. FY2023: 2.92x; 2.70x |
| C5 | EBITDA As Defined divided by net sales | FY2024: 4,173 / 7,940; FY2023: 3,395 / 6,585 | 52.6%; 51.6% |
| C6 | Total debt less (cash less the October 2024 payment of 4,348), then divided by EBITDA As Defined | 24,880 less (6,261 less 4,348) = 22,967; 22,967 / 4,173 (10-K pages 52, 56, 120) | 22,967; 5.50x |
| C7 | Gross profit less selling and administrative expenses less amortization of intangible assets | FY2024: 4,672 less 980 less 161; FY2023: 3,842 less 780 less 139 (10-K page 121) | 3,531; 2,923, equal to printed income from operations |
| C8 | Balance-sheet totals from printed components | Total current assets 6,261 + 1,381 + 1,876 + 511; total assets 10,029 + 1,488 + 10,419 + 3,446 + 204; total current liabilities 98 + 486 + 323 + 4,216 + 1,216; total liabilities 6,339 + 24,296 + 766 + 468; liabilities plus deficit 31,869 less 6,283 (10-K page 120) | 10,029; 25,586; 6,339; 31,869; 25,586, all equal to printed totals |
| C9 | Cash roll-forward | 2,045 less 2,441 plus 3,171 plus 14 = 2,789; 3,472 plus 2,789 (10-K page 123) | 2,789; 6,261, equal to printed values |
| C10 | Debt register subtotal and gross principal | 8,702 + 2,650 + 2,100 + 1,200 + 2,750 + 750 + 1,450 + 1,000 + 2,200 + 1,500 + 17 + 262; then plus securitization 487 (10-K pages 144 to 145) | 24,581, equal to the printed subtotal; 25,068 gross including securitization |
| C11 | Net carrying debt including securitization | 24,394 plus 486 (10-K pages 144 to 145) | 24,880, equal to MD&A total debt |
| C12 | EBITDA and EBITDA As Defined bridges | 1,715 + 312 + 1,286 + 500 = 3,813; 3,813 + 70 + 217 + 58 + 15 = 4,173; depreciation 149 + amortization 163 = 312 (10-K pages 71, 122) | Equal to printed values |
| C13 | Quarterly net sales | 1,789 + 1,919 = 3,708; 3,708 + 2,046 = 5,754; 7,940 less 5,754 (10-Q pages 3; 10-K page 121) | 3,708 and 5,754 equal to printed year-to-date; fourth quarter 2,186 derived |
| C14 | Net sales growth | 7,940 / 6,585 less one | 20.6%, equal to the MD&A figure of "20.6 %" (10-K page 45) |

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Executed Credit Agreement and indentures not supplied | Covenant EBITDA, baskets and headroom cannot be checked; ranking and guarantees rest on the 10-K description | Supply executed documents before any covenant or legal module |
| No 10-Q for the quarter ended December 30, 2023 | The first FY2024 quarter comes from a later filing's comparative column | Supply the filing if discrete quarters are relied on |
| Obligor-group financials only summarized | Issuer-level (TransDigm Inc. and guarantors) leverage is not calculated | Use the 10-K summarized table if a structural view is needed |
| Pro forma figures after October 2024 | Only the dividend payment is reflected; other October cash flows are Not supplied | Use the FY2025 first-quarter 10-Q for an actual later balance sheet, labelled as subsequent |
| No forecasts, ratings or market data | Forward credit metrics are Not calculable | Out of scope for this run |

## Next module

- CP-1A: use the debt register, the October 2024 subsequent events and the liquidity table for the transaction summary. Keep "as printed" amounts, the carrying-versus-gross distinction (24,880 carrying including securitization; 25,068 gross including securitization) and the statement that executed terms are not supplied.
- Report section "Financials and credit metrics": the first table under that heading is the selected presentation. Calculated rows are labelled with their calculation ID.
