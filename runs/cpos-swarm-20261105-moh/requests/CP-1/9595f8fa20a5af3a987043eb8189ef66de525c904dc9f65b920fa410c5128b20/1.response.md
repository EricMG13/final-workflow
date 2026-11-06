## Request

Issuer: MOLINA HEALTHCARE, INC. (ticker MOH; consolidated reporting entity; the senior notes are obligations of the parent corporation). As-of date and cutoff: 2026-11-05. Pathway: credit snapshot, public case. Reporting currency USD; all amounts are USD millions unless stated. Current period Q3 2026 (nine months ended September 30, 2026, and the balance sheet at September 30, 2026); prior period FY2025 (year ended December 31, 2025), with FY2024 as comparative.

Scope: extract the financial base (income statement, cash flow, balance sheet, debt, liquidity, covenants) from the pinned sources, calculate the leverage, coverage, liquidity and maturity metrics the report needs, and state what the evidence supports. This handoff is an intermediate artifact, not the final report. Period labels used throughout: FY2024, FY2025, nine months 2025 (9M 2025), nine months 2026 (9M 2026), and LTM, meaning the twelve months ended on the stated quarter-end, calculated as FY2025 plus the 2026 year-to-date amount less the 2025 year-to-date amount.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Use in this handoff |
| --- | --- | --- |
| 10-K_2025-12-31_moh-20251231.htm.jsonl | c9fc11483fb4b7c19a024a1eea5a26db7d569aa891c87974935ef7d58e311c73 | Audited FY2025 and FY2024 statements, debt note, covenants, ratings, parent liquidity |
| 10-Q_2026-03-31_moh-20260331.htm.jsonl | 13a11f49b2609a371d7feaaf1fc732c450976bf0759ca520903d8cae2d01480e | Q1 2026 statements, debt, parent liquidity |
| 10-Q_2026-06-30_moh-20260630.htm.jsonl | 2e116fbc160064a31ee8ffdf3cb7b87c5a30be87614aee212f07d7cf0a47d671 | Q2 2026 and six-month statements, debt, parent liquidity |
| 10-Q_2026-09-30_moh-20260930.htm.jsonl | 0eb181a17a96ec54e5242c30d2326e1cb431ceae3183b3fa8dd8bb665798cbdd | Q3 2026 and nine-month statements, debt, covenants, liquidity, legal |
| EX-99.1_2026-04-22_moh1q26_er.htm.jsonl | 209474d035cda2f89bcc2ac9abfc62e08120c0698a0cff7b05687b4b711891da | Q1 2026 release; cross-check and guidance |
| EX-99.1_2026-07-22_moh2q26_er.htm.jsonl | fd72c687dc87193147ac248ab3371c514003ac36c928d56dc905298dfee99d6d | Q2 2026 release; cross-check and guidance |
| EX-99.1_2026-10-21_moh3q26_er.htm.jsonl | f0ee0db37cb0340d37b34fde6c6107463ac060309062b86bfa3e7caa6f07a604 | Q3 2026 release; cross-check, cash flow narrative and guidance |

Context file sha256 038deefd3d0187dee809d7ec7eb3f32548cc8a768b8a64a8e4dfbffc4bec802f holds run settings only (no ratings, quotes or deal terms; all blank).

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 9a38b7e81c8a9d34c66cf8ba2d88f056039593cb8ea14bd1234abdea53036afb | Source readiness: adequate with limitations; carried forward as the gaps below |

Consistency with CP-0: every figure CP-0 tied (premium revenue 30,873, net income 112, interest expense 161, debt principal 3,800 and carrying value 3,771) is used here unchanged. This handoff corrects nothing in CP-0. It adds one finding CP-0 left out by design: the ratings sentence sits on page:94 of the annual report.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Calculated total debt to EBITDA rose from 1.54x in FY2024 to 11.32x for the twelve months to September 30, 2026 as earnings fell, while debt held near $3,771 million and the $1,250 million revolver stayed undrawn. | Medium | EBITDA is calculated, not reported, and cash interest and the covenant ratio are not available for the latest twelve months. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Operating income fell from $1,707 million in FY2024 to $781 million in FY2025 and to a calculated $172 million for the twelve months to September 30, 2026. | Debt service now rests on a thin earnings base, which raises refinancing and covenant sensitivity. | High |
| EBITDA over interest expense is a calculated 1.56x for the twelve months to September 30, 2026, against a covenant floor of 1.75 to 1.00 that is defined differently. | Headroom cannot be confirmed; the company states compliance but the covenant definition and reported ratio are not supplied. | Low |
| Parent cash and investments were $608 million at September 30, 2026, while consolidated cash of $4,479 million is subject to statutory capital rules at the regulated subsidiaries. | Debt service depends on the parent balance, subsidiary dividends and the undrawn revolver rather than consolidated cash. | Medium |
| No note principal falls due before the $800 million 4.375% notes in June 2028; the revolver matures in November 2030. | Near-term maturity pressure is limited, so the credit question is earnings recovery and covenant headroom. | High |
| Operating cash flow was an outflow of $535 million in FY2025 and an inflow of $629 million in 9M 2026, mainly on government settlement timing. | Cash generation is volatile and settlement-driven, so it is a weak guide to debt capacity. | Medium |

### Financial base view

The financial base is well supported for reported facts and weaker for derived credit metrics. Reported facts: Molina is a managed-care payer whose earnings compressed sharply as the medical care ratio (MCR, medical costs over premium revenue) rose from 89.1% in FY2024 to 91.7% in FY2025 and 92.1% in 9M 2026, so that operating income fell from 1,707 in FY2024 to 781 in FY2025 and to 334 in 9M 2026 against 943 in 9M 2025. Debt is five parent-level senior unsecured notes with 3,800 of principal and 3,771 of carrying value at September 30, 2026, no amount drawn on the 1,250 revolver, and no principal due before June 2028. Calculated metrics, not reported by the company: EBITDA (operating income plus depreciation and amortization) was 1,893 in FY2024, 976 in FY2025 and 333 for the LTM to September 30, 2026, which puts total debt to EBITDA at 1.54x, 3.86x and 11.32x. The mechanism is operating leverage on a fixed debt stack: debt did not fall while earnings did, and interest expense rose from 118 in FY2024 to 192 in FY2025 after the November 2024 and November 2025 note issuances and the 2025 term loan borrowings. Interest expense over the LTM to September 30, 2026 was 213, so EBITDA over interest expense is 1.56x on this simple basis, below the 1.75 to 1.00 covenant floor in force through December 31, 2026. That comparison is not a covenant test: the credit agreement defines the ratio and the sources do not print the definition or the reported ratio, the company states it is in compliance (10-Q Q3 page:15), and adding back the 93 non-cash impairment alone lifts the simple ratio to 2.00x. The consolidated balance sheet shows net cash (consolidated cash and equivalents of 4,479 exceed debt of 3,771), but most of that cash supports claims and statutory capital at the regulated health plans, so the parent view (608 of cash and investments) is the better liquidity guide for debt service. Near-term maturity pressure is limited because no principal falls due before June 2028, so the credit question is earnings recovery and covenant headroom rather than refinancing in the next year. What the evidence supports: the reported statements, debt table, maturities, revolver size and parent cash. What it restricts: any statement of covenant headroom, cash-interest coverage for the latest twelve months, or revolver availability net of letters of credit. The context holds no ratings, so the only rating evidence is the annual report sentence that each senior note is rated BB by S&P and Ba2 by Moody's (10-K page:94).

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 1.54 | 1.31 | x | Total debt = long-term debt carrying value 2,923; EBITDA = operating income 1,707 + D&A 186 = 1,893 (calculated); net debt deducts parent cash and investments 445. Consolidated cash is not deducted because most is held at regulated subsidiaries. |
| FY2025 | 3.86 | 3.63 | x | Debt 3,766; EBITDA = 781 + 195 = 976 (calculated); parent cash and investments 223. Finance leases of 209 are outside the debt figure (4.05x if the non-current 184 is added). |
| LTM Q1 2026 | 6.11 | 5.76 | x | Debt 3,767; LTM EBITDA 617 (calculated, includes the 93 impairment charge in operating income); parent cash and investments 213. |
| LTM Q2 2026 | 10.16 | 9.38 | x | Debt 3,769; LTM EBITDA 371 (calculated, includes the 93 impairment); parent cash and investments 290. |
| LTM Q3 2026 | 11.32 | 9.50 | x | Debt 3,771; LTM EBITDA 333 (calculated, includes the 93 impairment; 8.85x total debt if it is added back); parent cash and investments 608. On consolidated cash and equivalents of 4,479 net debt is negative. Covenant EBITDA is not supplied. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 15.64 | x | EBITDA 1,893 (calculated) over cash paid for interest of 121 (10-K page:107). Expense basis: 16.04x on interest expense of 118. |
| FY2025 | 5.39 | x | EBITDA 976 (calculated) over cash paid for interest of 181 (10-K page:107). Expense basis: 5.08x on interest expense of 192. |
| LTM Q1 2026 | Not supplied: cash interest paid is printed only in the 10-K, not in the quarterly reports or releases | x | Expense basis for reference: EBITDA 617 over LTM interest expense of 203 is 3.04x. |
| LTM Q2 2026 | Not supplied: cash interest paid is printed only in the 10-K, not in the quarterly reports or releases | x | Expense basis for reference: EBITDA 371 over LTM interest expense of 209 is 1.78x. |
| LTM Q3 2026 | Not supplied: cash interest paid is printed only in the 10-K, not in the quarterly reports or releases | x | Expense basis for reference: EBITDA 333 over LTM interest expense of 213 is 1.56x (2.00x with the 93 impairment added back). Not the covenant ratio; the covenant floor is 1.75 to 1.00 through December 31, 2026. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| December 31, 2024 | 4662 | Not supplied: capacity under the prior credit agreement at this date is not printed in the pinned sources | US$m | Consolidated cash and cash equivalents (10-K page:105). Parent cash and investments were 445 (10-K page:90). |
| December 31, 2025 | 4248 | 1250 | US$m | Consolidated cash and equivalents; 1,250 is the stated available borrowing capacity under the revolver (10-K page:96). Parent cash and investments 223. Letters of credit under the 100 sub-facility are not printed. |
| March 31, 2026 | 5314 | 1250 | US$m | Consolidated cash and equivalents (10-Q Q1 page:2); capacity per 10-Q Q1 page:36. Parent cash and investments 213. |
| June 30, 2026 | 4985 | 1250 | US$m | Consolidated cash and equivalents (10-Q Q2 page:2); capacity per 10-Q Q2 page:39. Parent cash and investments 290. |
| September 30, 2026 | 4479 | 1250 | US$m | Consolidated cash and equivalents (10-Q Q3 page:2); capacity per 10-Q Q3 page:40. Parent cash and investments 608. Consolidated cash is subject to statutory capital rules; investments of 4,100 are excluded from Cash. Revolver terminates November 20, 2030. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0 | US$m | No principal due; the 10-K maturity table prints a dash for 2026 (10-K page:130). |
| 2027 | 0 | US$m | No principal due; dash in the 10-K table. |
| 2028 | 800 | US$m | 4.375% Notes due June 15, 2028, senior unsecured, issued by the parent (10-Q Q3 page:14). |
| 2029 | 0 | US$m | No principal due; dash in the 10-K table. |
| 2030 | 650 | US$m | 3.875% Notes due November 15, 2030. The 1,250 revolver also terminates November 20, 2030, with nothing outstanding. |
| 2031 | 850 | US$m | 6.500% Notes due February 15, 2031 (issued November 20, 2025). |
| 2032 | 750 | US$m | 3.875% Notes due May 15, 2032. |
| 2033 | 750 | US$m | 6.250% Notes due January 15, 2033. Principal total 3,800; carrying value 3,771 after 29 of deferred issuance costs. |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2024 | FY2025 | 9M 2025 | 9M 2026 | LTM Q3 2026 | Basis and source |
| --- | --- | --- | --- | --- | --- | --- |
| Premium revenue | 38,627 | 43,052 | 32,337 | 30,873 | 41,588 | Reported; LTM calculated. 10-K page:105; 10-Q Q3 page:2 |
| Total revenue | 40,650 | 45,426 | 34,051 | 32,752 | 44,127 | Reported; LTM calculated |
| Medical care costs | 34,428 | 39,488 | 29,352 | 28,429 | 38,565 | Reported; LTM calculated |
| MCR (%) | 89.1 | 91.7 | 90.8 | 92.1 | 92.73 | Reported (10-K page:81; 10-Q Q3 page:24); LTM calculated |
| G&A expense | 2,743 | 3,009 | 2,214 | 2,213 | 3,008 | Reported; LTM calculated (6.82% of LTM total revenue) |
| Depreciation and amortization | 186 | 195 | 151 | 117 | 161 | Reported; LTM calculated |
| Impairment (intangible assets, MAPD exit) | No line reported | No line reported | 0 (printed as a dash) | 93 | 93 | Recognized in Q1 2026 (10-Q Q1 page:2; 10-Q Q3 page:2); the FY2024 and FY2025 income statements have no impairment line |
| Operating income | 1,707 | 781 | 943 | 334 | 172 | Reported; LTM calculated; includes investment income of 420 in FY2025 |
| EBITDA (operating income + D&A) | 1,893 | 976 | 1,094 | 451 | 333 | Calculated; not a company-reported measure |
| Interest expense | 118 | 192 | 140 | 161 | 213 | Reported; LTM calculated |
| Income before income tax | 1,589 | 589 | 803 | 173 | -41 | Reported; LTM calculated |
| Net income | 1,179 | 472 | 632 | 112 | -48 | Reported; LTM calculated |
| Net cash from operating activities | 644 | -535 | -237 | 629 | 331 | Reported; LTM calculated; settlement timing drives swings |
| Capital expenditure (property, equipment, software) | 100 | 101 | 102 | 94 | 93 | Reported; LTM calculated |
| Operating cash flow less capital expenditure | 544 | -636 | -339 | 535 | 238 | Calculated; before share repurchases (1,000 in FY2025, none in 9M 2026) |
| Cash and cash equivalents (period end) | 4,662 | 4,248 | Not supplied | 4,479 | 4,479 | Balance sheet at September 30, 2026; September 30, 2025 balance sheet not in pinned set |
| Investments (current) | 4,325 | 4,008 | Not supplied | 4,100 | 4,100 | Available-for-sale; mostly regulated-subsidiary assets |
| Parent cash and investments | 445 | 223 | Not supplied | 608 | 608 | MD&A liquidity text |
| Long-term debt, carrying value | 2,923 | 3,766 | Not supplied | 3,771 | 3,771 | Senior notes less deferred costs; no revolver drawn |
| Finance lease liabilities, non-current | 195 | 184 | Not supplied | 179 | 179 | Balance sheet line; current portion not shown at September 30, 2026 |
| Stockholders' equity | 4,496 | 4,069 | Not supplied | 4,155 | 4,155 | Balance sheet |
| Total debt / EBITDA (x) | 1.54 | 3.86 | Not calculable | Not calculable | 11.32 | Calculated; 9M columns are not annual so no multiple is shown |
| Net debt (parent cash basis) / EBITDA (x) | 1.31 | 3.63 | Not calculable | Not calculable | 9.50 | Calculated |
| EBITDA / interest expense (x) | 16.04 | 5.08 | Not calculable | Not calculable | 1.56 | Calculated; not the covenant ratio |
| EBITDA / cash interest paid (x) | 15.64 | 5.39 | Not supplied | Not supplied | Not supplied | Cash interest paid 121 and 181 in the 10-K only |

### Credit-relevant observations

- Earnings pressure is margin-driven, not revenue-driven at the premium line in 2025: premium revenue rose from 38,627 to 43,052 in FY2025 while medical margin fell from 4,199 to 3,564 (10-K page:81). In 2026 premium revenue also fell (30,873 in 9M 2026 against 32,337), mainly on lower Medicaid and Marketplace membership (Q3 release page:1), so both a lower revenue base and a higher MCR now weigh on earnings. Marketplace MCR was 90.6% in FY2025 against 75.4% in FY2024 (10-K page:85).
- The fourth quarter of 2025 was an operating loss on a derived basis: FY2025 operating income of 781 less 9M 2025 of 943 gives -162 (see Calculations). That quarter is what lifts the LTM interest-cover measure down to 1.56x.
- Leverage view by balance sheet: debt to capital on a simple basis (debt over debt plus equity) is 47.58% at September 30, 2026, against 48.07% at December 31, 2025 and 39.40% at December 31, 2024. The covenant maximum is 60% (65% for four quarters after a material acquisition), defined by the credit agreement; the simple ratio is indicative only.
- Claims outside debt: medical claims and benefits payable of 4,988 and amounts due government agencies of 1,141 at September 30, 2026 are operating liabilities outside the debt figure (10-Q Q3 page:2). Finance lease liabilities were 209 in total at December 31, 2025 (25 current, 184 non-current) and operating lease liabilities 71 (10-K page:127); both are outside the debt figure. Pensions, factoring and supply-chain finance: none found in the sources (searched).
- Liquidity depends on subsidiary dividends: regulated subsidiaries paid 985 in 2025 and 997 in 2024 to the parent (10-K page:90); for 9M 2026 the parent received 329 in dividends and return of capital and contributed 130 of capital (10-Q Q3 page:35). Dividends payable without regulatory approval were about 170 in aggregate at December 31, 2025, and the company expected a decline in such dividends for 2026 (10-K page:94). Minimum statutory capital and surplus was about 3.1 billion at December 31, 2025 (10-K page:93).
- Capital return and financing: 1,000 of common stock was purchased in FY2025 and none in 9M 2026; 500 remained authorized through December 31, 2026 as of October 16, 2026 (10-Q Q3 page:40). In FY2025 the company borrowed 1,100 under the credit facility and term loans and repaid 1,100, and issued the 850 6.500% notes in November 2025 with net proceeds of 838 (10-K page:107).
- Latest quarter and subsequent events to the cutoff: the Q3 release reaffirmed FY2026 guidance (premium revenue of approximately $42 billion; GAAP earnings of at least $2.38 per diluted share; adjusted earnings of at least $5.25), including a loss of $1.50 per share from implementing the new Florida Medicaid contract in Q4 2026 and $1.00 from traditional MAPD (Q3 release page:2). The securities class action was dismissed with prejudice on October 20, 2026 (10-Q Q3 page:18). The Q3 2026 debt note (10-Q Q3 pages 14-15) shows the same five notes as December 31, 2025 and no drawing on the revolver; no debt issuance or further amendment after February 4, 2026 appears in the pinned sources.
- Covenant facts: minimum interest coverage 3.0 to 1.0, reduced by the February 4, 2026 amendment to 1.75 to 1.00 for quarters ending March 31, 2026 to December 31, 2026, then 2.00 (March 2027), 2.50 (June 2027) and 2.75 (September 2027); maximum Consolidated Total Debt to Capital Ratio 60% (10-Q Q3 page:15). Compliance at September 30, 2026 is stated. The step-up of the floor in 2027 to 2.75 is a forward test; at the LTM September 2026 simple measure of 1.56x that is a material sensitivity if earnings do not recover.

## Calculations

All amounts USD millions. LTM = FY2025 + year-to-date 2026 - year-to-date 2025. Sources: 10-K pages 105-107; 10-Q Q1 page:2; 10-Q Q2 page:2; 10-Q Q3 pages 2-4.

| Item | Formula and inputs | Result |
| --- | --- | --- |
| EBITDA FY2024 | Operating income 1,707 + D&A 186 | 1,893 |
| EBITDA FY2025 | 781 + 195 | 976 |
| EBITDA 9M 2025 | 943 + 151 | 1,094 |
| EBITDA 9M 2026 | 334 + 117 | 451 |
| LTM Q3 2026 operating income | 781 + 334 - 943 | 172 |
| LTM Q3 2026 D&A | 195 + 117 - 151 | 161 |
| LTM Q3 2026 EBITDA | 172 + 161 | 333 |
| LTM Q2 2026 EBITDA | Operating income 781 + 228 - 806 = 203; D&A 195 + 79 - 106 = 168; 203 + 168 | 371 |
| LTM Q1 2026 EBITDA | Operating income 781 + 83 - 433 = 431; D&A 195 + 39 - 48 = 186; 431 + 186 | 617 |
| LTM interest expense | Q3: 192 + 161 - 140 = 213; Q2: 192 + 108 - 91 = 209; Q1: 192 + 54 - 43 = 203 | 213; 209; 203 |
| Total debt / EBITDA | FY2024 2,923 / 1,893; FY2025 3,766 / 976; Q1 3,767 / 617; Q2 3,769 / 371; Q3 3,771 / 333 | 1.54x; 3.86x; 6.11x; 10.16x; 11.32x |
| Net debt (parent cash basis) | Debt less parent cash and investments: FY2024 2,923 - 445 = 2,478; FY2025 3,766 - 223 = 3,543; Q1 3,767 - 213 = 3,554; Q2 3,769 - 290 = 3,479; Q3 3,771 - 608 = 3,163 | 2,478; 3,543; 3,554; 3,479; 3,163 |
| Net debt / EBITDA | 2,478 / 1,893; 3,543 / 976; 3,554 / 617; 3,479 / 371; 3,163 / 333 | 1.31x; 3.63x; 5.76x; 9.38x; 9.50x |
| Net debt, consolidated cash basis (reference) | 3,771 - 4,479 at September 30, 2026 | -708 (net cash); not used as the primary measure |
| Finance-lease-inclusive leverage FY2025 | (3,766 + 184) / 976 | 4.05x |
| Impairment sensitivity LTM Q3 2026 | EBITDA 333 + 93 = 426; 3,771 / 426; 426 / 213 | 8.85x; 2.00x |
| EBITDA / cash interest | FY2024 1,893 / 121; FY2025 976 / 181 | 15.64x; 5.39x |
| EBITDA / interest expense | FY2024 1,893 / 118; FY2025 976 / 192; LTM Q1 617 / 203; Q2 371 / 209; Q3 333 / 213 | 16.04x; 5.08x; 3.04x; 1.78x; 1.56x |
| LTM MCR | LTM medical costs 39,488 + 28,429 - 29,352 = 38,565; LTM premium 43,052 + 30,873 - 32,337 = 41,588; 38,565 / 41,588 | 92.73% |
| LTM total revenue, pre-tax, net income | Revenue 45,426 + 32,752 - 34,051; pre-tax 589 + 173 - 803; net income 472 + 112 - 632 | 44,127; -41; -48 |
| Free cash flow proxy | Operating cash flow less capex: FY2024 644 - 100; FY2025 -535 - 101; 9M 2025 -237 - 102; 9M 2026 629 - 94; LTM operating cash flow -535 + 629 + 237 = 331 less LTM capex 101 + 94 - 102 = 93 | 544; -636; -339; 535; 238 |
| Debt to capital (simple, indicative) | Debt / (debt + equity): 3,771 / (3,771 + 4,155); 3,766 / (3,766 + 4,069); 2,923 / (2,923 + 4,496) | 47.58%; 48.07%; 39.40% |
| Implied Q4 2025 | FY2025 less 9M 2025: operating income 781 - 943; pre-tax 589 - 803; net income 472 - 632; premium revenue 43,052 - 32,337; medical costs 39,488 - 29,352 (10,136); MCR 10,136 / 10,715 | -162; -214; -160; 10,715; 94.60% |
| Annual coupon on notes | 800 x 4.375% + 650 x 3.875% + 850 x 6.500% + 750 x 3.875% + 750 x 6.250% = 35.00 + 25.19 + 55.25 + 29.06 + 46.88 | 191.4 (5.04% of principal 3,800); LTM interest expense of 213 is higher by deferred cost amortization, commitment fees and lease interest the sources do not itemize |
| Implied Q4 2026 GAAP net income at the guidance floor | FY2026 GAAP net income guidance 122 (Q3 release page:9) less 9M 2026 net income 112 | 10 (a floor, from "at least"; management guidance, not a forecast of record) |
| Principal and carrying value | 800 + 650 + 850 + 750 + 750 = 3,800; less deferred issuance costs 29 | 3,771 (ties to the balance sheet) |

Checks: quarterly premium revenue 10,172 + 10,244 + 10,457 = 30,873; quarterly net income 14 + 60 + 38 = 112; the Q3 release and 10-Q Q3 agree on every figure used.

## Gaps

| Gap | Search performed | Effect | Action |
| --- | --- | --- | --- |
| Covenant ratio values (interest coverage, debt to capital) and definitions not supplied; executed credit agreement and first amendment not in pinned set | Searched all sources for Interest Coverage Ratio and Debt to Capital: thresholds and compliance statements only | Headroom cannot be measured; the 1.56x simple LTM measure must not be read as the covenant ratio | Add the credit agreement, first amendment and a compliance figure |
| Cash interest paid for LTM periods not printed (10-K only) | Searched cash paid and interest paid in all sources | LTM cash-interest cover is Not supplied; expense basis used for reference | Obtain quarterly supplemental cash flow data |
| Letters of credit outstanding under the 100 sub-facility not printed | Searched letter of credit, standby, surety, performance bond | Undrawn facility is the stated 1,250 available capacity, not a net-of-letters figure | Obtain facility utilization |
| Reported EBITDA and adjusted EBITDA not in the company's materials | Searched EBITDA; only adjusted net income and adjusted EPS appear, in the releases | Credit EBITDA is calculated as operating income + D&A, includes investment income and the 93 impairment | Label as calculated; obtain covenant EBITDA |
| September 30, 2025 balance sheet not supplied | Balance sheet comparatives are December 31, 2025 only | Balance rows for 9M 2025 are Not supplied | None needed for LTM |
| Current portion of finance leases and operating leases at September 30, 2026 not printed | Searched lease terms in the Q3 report | Lease obligations known at December 31, 2025 only (209 finance, 71 operating) | Use December 31, 2025 for lease sizing |
| Consolidated cash is largely at regulated subsidiaries; no split of unrestricted parent cash vs subsidiary cash beyond parent cash and investments | Reviewed liquidity text | Net debt shown on parent basis; consolidated basis is reference only | Keep parent view primary |
| Ratings only as of the annual report (BB, Ba2) | Searched Moody, S&P, rated | No later rating action in sources | Add agency reports if needed |
| Extraction fidelity of flattened tables not reviewed | Figures cross-checked between filings and releases | Low | Spot-check |

## Next module

Proceed to the business and transaction context module (CP-1A) with this handoff: the key financial facts it needs are the segment mix (Medicaid 24,175 of 30,873 premium revenue in 9M 2026), the margin deterioration, the Florida contract implementation cost in Q4 2026, the exit of the MAPD product for 2027, and the dismissal of the securities litigation. Carry forward: EBITDA is calculated; covenant headroom, cash-interest cover for LTM periods and letters of credit are not supplied; the simple LTM interest cover of 1.56x is below the 1.75 to 1.00 floor in force but is not the covenant measure.
