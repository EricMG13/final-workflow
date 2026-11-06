## Request

Module: financial base for CACI INTERNATIONAL INC /DE/ (issuer id caci, ticker CACI), as of 2026-11-05, cutoff 2026-11-05, pathway credit snapshot. Reporting currency per the context: USD. Context periods: current period the fiscal first quarter of FY2027 (Q1 FY2027, quarter ended September 30, 2026); prior period FY2026 (year ended June 30, 2026). The fiscal year ends June 30 until the transition to a calendar year disclosed on October 20, 2026.

Scope: extract the reported financial base from the supplied filings and releases, calculate leverage, cover, liquidity and maturity measures from printed inputs, review definitions, and state what stays restricted. All amounts below are US$ millions unless marked, converted from US$ thousands as printed (divide by one thousand, no other change). Perimeter: CACI International Inc and its consolidated subsidiaries, US GAAP, as printed in the statements. The quarterly statements are unaudited. No input is taken from outside the pinned sources.

Upstream handoff used: CP-0 (source readiness). It found all seven sources usable, with no executed debt documents, no guarantor list, no covenant levels, and a fiscal-year change after the last quarter. This module carries each of those limits forward and does not correct CP-0, except that CP-0 stated no balance sheet at the end of Q1 FY2026 was supplied: that stands for the balance sheet, but cash (133.020) and equity (4,025.499) at that date are printed in the Q1 FY2027 quarterly cash flow and equity statements, and are used below.

## Sources

### Issuer sources relied on

Locators use the file name and the source chunk shown as page:N, which is not the printed page.

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2026-06-30_caci-20260630.htm.jsonl | f2d21cb22e8c5506b4bb126ec8c544c48dff7d613005574465264d0d51f72c87 |
| 10-Q_2025-12-31_caci-20251231.htm.jsonl | 6f56468069c0ca930d3949dd2a9dc046bc39d9a3ee2fbfe67786310e4a593a88 |
| 10-Q_2026-03-31_caci-20260331.htm.jsonl | 743998e742f09f0797de29d0f737948ca0facb537bfd7546eb293e55de92e220 |
| 10-Q_2026-09-30_caci-20260930.htm.jsonl | dea393e31122fa0362a795e376fb4e1b82a07df3fbc9a647679762ac053e54fc |
| EX-99.1_2026-04-22_fy26-q3caci20260422ex991.htm.jsonl | 3baba025aa721deb2088cd8c20105e1486e76edc2a788c07afcf9740e7703457 |
| EX-99.1_2026-08-05_fy26-q4caci20260805ex991.htm.jsonl | 365693dc6db2c9b512bcdf65c2cb01ffe29245082e9245fc25f8496d007e334e |
| EX-99.1_2026-10-21_fy27-q1caci20261021ex991.htm.jsonl | 5ac06623a6e500e9ed51b547855a7fd7b4c66f8019da3cafa8cd0fb6f8596399 |

User context (settings, not issuer evidence): context sha256 771458f144b8d7a95d0c8ef74d2f2b133b5846c23aea051905b07e94014f45fd.

### Handoffs supplied

| Module | sha256 |
| --- | --- |
| CP-0 | 762cecbf926d995975842c532bf62ee7e0ca710d78ac7cdd487a629157bb5aa2 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported leverage rose after the large acquisition but eased by the latest quarter, while cash interest cover stayed above five times and liquidity was ample on printed facilities. Covenant tests cannot be checked. | Medium | Management EBITDA is the only earnings measure; covenant levels, definitions and a pro forma acquisition view are not supplied, so leverage is not on a covenant or run-rate basis. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt over EBITDA moved from 3.04x at FY2025 to 4.20x at FY2026 and 3.94x on the twelve months to September 30, 2026. | Acquisition debt lifted leverage; modest deleveraging followed, but the ratio still sits above the prior year-end level. | Medium |
| Cash interest cover was 6.67x at FY2025, 5.49x at FY2026 and 5.60x on the latest twelve months. | Interest burden grew with acquisition debt; cover remains comfortable, but quarterly cash interest omits note coupons and the twelve-month figure holds part-year acquisition debt. | Medium |
| Cash plus undrawn revolver was 1,674.389 million at September 30, 2026; receivable-sale capacity is nearly fully used and expires December 18, 2026. | Liquidity is large against near-term maturities; the receivable sale program is not extra headroom. | High |
| The first heavy maturity wall is FY2031, at 1,706.750 million, with 2,959.250 million after that. | No large maturity falls inside the next four fiscal years; floating-rate exposure is partly hedged. | High |
| Covenant types are named but no level, definition or reported ratio is supplied. | Covenant headroom, definition gaps and default distance cannot be assessed from this pack. | High |

### Financial base view

The financial base is usable for statement-based credit work, with restrictions. The audited FY2026 and FY2025 statements, three quarterly filings and three releases give a consistent consolidated base in USD. On printed inputs, total debt (principal) over management EBITDA was 3.04x at FY2025, 4.20x at FY2026 and 3.94x on the twelve months to September 30, 2026, and net debt over EBITDA was 2.93x, 4.04x and 3.72x. EBITDA over cash interest paid was 6.67x, 5.49x and 5.60x. Leverage rose because the March 2026 acquisition was financed with new term debt and add-on notes while its earnings entered the base only from March 9, 2026; the latest twelve-month ratio therefore still carries a part-year earnings contribution against the full acquisition debt balance, and no pro forma figure is supplied. The restrictions are: EBITDA is management defined and unadjusted for stock compensation and acquisition costs; covenant definitions and levels are Not supplied, so no covenant ratio or headroom is computed; a fiscal-year change makes the next report a six-month transition period; and obligations outside the debt figure (operating leases, the receivable sale program, supplemental retirement obligations, contingent consideration) are listed but not added to leverage.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (June 30, 2025) | 3.04 | 2.93 | x | Principal debt 2,942.625 over management EBITDA 966.796; cash 106.181. Management EBITDA, not covenant EBITDA; operating leases and receivable sales excluded from debt. |
| FY2026 (June 30, 2026) | 4.20 | 4.04 | x | Principal debt 4,931.125 over management EBITDA 1,173.914; cash 191.756. EBITDA includes the acquired business only from March 9, 2026; debt includes its full financing; not pro forma. |
| LTM September 30, 2026 | 3.94 | 3.72 | x | Principal debt 4,864.438 over LTM EBITDA 1,234.129 (FY2026 plus Q1 FY2027 less Q1 FY2026); cash 279.389. Same part-year acquisition contribution; not pro forma; not a covenant ratio. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 6.67 | x | Management EBITDA 966.796 over cash paid for interest 145.040 (cash flow statement supplemental disclosure). Not a covenant interest coverage ratio. |
| FY2026 | 5.49 | x | Management EBITDA 1,173.914 over cash paid for interest 213.640. Acquisition debt outstanding only from March 2026, so cash interest does not yet show a full year of it. |
| LTM September 30, 2026 | 5.60 | x | LTM EBITDA 1,234.129 over LTM cash interest 220.491 (FY2026 plus Q1 FY2027 less Q1 FY2026). The senior notes pay semi-annually with first dates of December 15, 2025 and June 15, 2026 per the notes text, which implies (inference) no note coupon in the July to September quarter; LTM includes two coupon dates; not a covenant ratio. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| June 30, 2025 | 106.181 | Not supplied: revolving commitment at this date is not printed in the supplied filings | US$m | Cash from the FY2026 annual balance sheet comparative. Revolver drawn balance was 124.500 per the debt table. |
| December 31, 2025 | 422.976 | 2,000.0 | US$m | Cash from the balance sheet. Undrawn is the printed 2,000.0 revolving commitment with the printed statement of no outstanding revolver, swing line or standby letter of credit borrowings; derived by identity, not printed as undrawn. |
| March 31, 2026 | 157.996 | 1,072.0 | US$m | Undrawn capacity as printed in the Q3 FY2026 filing liquidity discussion. Revolver drawn 928.000 at that date. |
| June 30, 2026 | 191.756 | 1,340.0 | US$m | Undrawn capacity as printed in the annual report; revolver drawn 660.000; no standby letters of credit outstanding. |
| September 30, 2026 | 279.389 | 1,395.0 | US$m | Undrawn capacity as printed in the Q1 FY2027 filing; revolver drawn 605.000. Cash includes pound sterling and euro balances of 92.7 not immediately available to U.S. operations. Receivable sale capacity (maximum 350.0) is almost fully used and is excluded. Revolver matures November 2030. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2027 (year ending June 30, 2027) | 46.750 | US$m | Aggregate maturities as of June 30, 2026 from the annual debt note; scheduled term loan amortisation. Scheduled payments of 7.8, 1.9 and 2.0 were made in Q1 FY2027 on the Term Loan, Term Loan B and Term Loan B-2. |
| FY2028 | 62.375 | US$m | Scheduled amortisation, same table. |
| FY2029 | 78.000 | US$m | Scheduled amortisation, same table. |
| FY2030 | 78.000 | US$m | Scheduled amortisation, same table. |
| FY2031 | 1,706.750 | US$m | Holds the instruments due November 2030, within the fiscal year ending June 30, 2031: the revolver (660.000 drawn at June 30, 2026; 605.000 at September 30, 2026) and the Term Loan. |
| Thereafter | 2,959.250 | US$m | Term Loan B (October 2031), Term Loan B-2 (March 2033) and the 2033 Notes and add-on (June 2033), net of amortisation. Table total equals principal of 4,931.125 at June 30, 2026; a schedule at September 30, 2026 is not supplied. Fiscal-year labels may change with the calendar-year transition. |

### Financials and credit metrics

| Metric | FY2025 | FY2026 | Q1 FY2026 | Q1 FY2027 | LTM Sep 30, 2026 | Unit | Basis, locator and limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Revenues | 8,627.824 | 9,567.779 | 2,287.623 | 2,474.597 | 9,754.753 | US$m | Statements of operations: annual 10-K page:66; Q1 10-Q page:2. LTM calculated. |
| Income from operations | 764.185 | 919.815 | 212.275 | 247.528 | 955.068 | US$m | Same pages. LTM calculated. |
| Management EBITDA | 966.796 | 1,173.914 | 268.613 | 328.828 | 1,234.129 | US$m | Releases: Q4 FY2026 page:12; Q1 FY2027 page:10. Net income plus taxes, net interest and D&A including depreciation in direct costs; not adjusted for stock compensation or deal costs. LTM calculated. |
| EBITDA margin | 11.2 | 12.3 | 11.7 | 13.3 | 12.7 | % | Printed in releases for the first four columns; LTM calculated. |
| Net income | 499.830 | 535.808 | 124.810 | 130.367 | 541.365 | US$m | Statements of operations. LTM calculated. |
| Interest expense and other, net (income statement) | 158.844 | 215.454 | 46.173 | 73.240 | 242.521 | US$m | One combined line; interest income not separated. LTM calculated. |
| Cash paid for interest | 145.040 | 213.640 | 35.768 | 42.619 | 220.491 | US$m | Cash flow supplemental disclosure: 10-K page:67; Q1 10-Q page:4. LTM calculated. Q1 FY2027 is below the income statement charge of 73.240. |
| Cash paid for income taxes, net of refunds | 134.782 | 93.169 | 30.476 | 13.177 | 75.870 | US$m | Same pages. LTM calculated. |
| Net cash provided by operating activities | 547.009 | 886.710 | 171.065 | 161.314 | 876.959 | US$m | Cash flow statements. Includes receivable sale program flows. LTM calculated. |
| Capital expenditures | 65.603 | 106.653 | 17.014 | 11.359 | 100.998 | US$m | Cash flow statements. LTM calculated. |
| Operating cash flow less capital expenditures | 481.406 | 780.057 | 154.051 | 149.955 | 775.961 | US$m | Calculated; includes receivable sale program flows. |
| Free cash flow, management definition | 442.497 | 735.433 | 142.960 | 133.489 | 725.962 | US$m | Releases: excludes receivable sale program flows, less capex (Q4 FY2026 page:13; Q1 FY2027 page:11). Non-GAAP; LTM calculated from released figures. |
| Cash and cash equivalents | 106.181 | 191.756 | 133.020 | 279.389 | 279.389 | US$m | Balance sheets; Q1 FY2026 from the Q1 FY2027 cash flow statement end-of-period line (10-Q page:4). |
| Total debt, principal | 2,942.625 | 4,931.125 | Not supplied: debt table at September 30, 2025 not in the pack | 4,864.438 | 4,864.438 | US$m | Debt notes: 10-K page:86; Q1 10-Q page:9. Carrying value net of discount: 2,917.940, 4,901.509 and 4,836.063 at June 30, 2025, June 30, 2026 and September 30, 2026. |
| Net debt (principal less cash) | 2,836.444 | 4,739.369 | Not supplied: debt not available at this date | 4,585.049 | 4,585.049 | US$m | Calculated. |
| Total debt / EBITDA | 3.04 | 4.20 | Not calculable: quarterly EBITDA is not an annual base | Not calculable: quarterly EBITDA is not an annual base | 3.94 | x | Calculated; see Calculations. |
| Net debt / EBITDA | 2.93 | 4.04 | Not calculable: quarterly EBITDA is not an annual base | Not calculable: quarterly EBITDA is not an annual base | 3.72 | x | Calculated. |
| EBITDA / cash interest | 6.67 | 5.49 | 7.51 | 7.72 | 5.60 | x | Calculated. Quarterly cover is flattered because note coupons fall in December and June, not in July to September. |
| Total assets | 8,647.598 | 11,819.644 | Not supplied: balance sheet at this date not in the pack | 11,947.535 | 11,947.535 | US$m | Balance sheets. |
| Total shareholders' equity | 3,893.945 | 4,462.697 | 4,025.499 | 4,626.691 | 4,626.691 | US$m | Balance sheets; Q1 FY2026 from the equity statement. |
| Domestic Operations revenues | 8,370.361 | 9,260.288 | 2,210.044 | 2,398.161 | 9,448.405 | US$m | Segment notes: 10-K page:98; Q1 10-Q page:12. LTM calculated. |
| International Operations revenues | 257.463 | 307.491 | 77.579 | 76.436 | 306.348 | US$m | Same pages. LTM calculated. |
| Domestic Operations income from operations | 709.552 | 859.873 | 199.434 | 234.267 | 894.706 | US$m | Same pages. LTM calculated. |
| International Operations income from operations | 54.633 | 59.942 | 12.841 | 13.261 | 60.362 | US$m | Same pages. LTM calculated. |
| Contract awards | 9,642.184 | 10,245.039 | 4,998.684 | 4,828.329 | Not calculable: LTM awards not reported on a comparable basis | US$m | Releases: Q4 FY2026 page:10; Q1 FY2027 page:9. Management KPI. |
| Total backlog (period end) | 31,400 | 32,000 | 33,900 | 34,000 | 34,000 | US$m | Printed in billions: 10-K page:52; Q1 10-Q page:20. Includes unexercised options. Funded backlog 5,400 at June 30, 2026 and 6,200 at September 30, 2026. |
| Remaining sold receivables (receivable sale program, derecognised) | 192.518 | 223.406 | 164.816 | 189.280 | 189.280 | US$m | 10-K page:85; Q1 10-Q page:8. Outside the debt figure. |
| Operating lease liabilities, total | 417.089 | 483.024 | Not supplied: not reported in the quarter | Not supplied: only the non-current part (447.236) is on the balance sheet | Not supplied: total not printed at this date | US$m | 10-K page:86 (note on leases). Outside the debt figure. |

### Facility and instrument detail

Principal at September 30, 2026, as printed (Q1 FY2027 10-Q, page:9), with maturity, stated and effective rates. Guarantors and collateral wording are in Gaps.

| Instrument | Maturity | Stated rate | Effective rate | Principal US$m | Security and ranking as printed |
| --- | --- | --- | --- | --- | --- |
| Revolving Facility (commitment 2,000.0) | November 2030 | 4.99% | 4.99% | 605.000 | Senior secured credit facility; a majority of assets serve as collateral (10-K page:88) |
| Term Loan | November 2030 | 5.40% | 5.47% | 1,226.563 | Same credit facility; quarterly amortisation of 7.8 through December 31, 2027 and 15.6 after |
| Term Loan B | October 2031 | 5.65% | 5.89% | 736.875 | Senior secured term loan; quarterly amortisation of 1.9 |
| Term Loan B-2 | March 2033 | 5.65% | 5.85% | 796.000 | Senior secured term loan; same guarantees and collateral as Term Loan B; quarterly amortisation of 2.0 |
| 2033 Notes | June 2033 | 6.38% | 6.58% | 1,000.000 | Senior unsecured notes at 6.375%; text says subordinated to existing senior secured indebtedness |
| 2033 Notes-2 | June 2033 | 6.38% | 6.10% | 500.000 | Add-on of the same series as the 2033 Notes, issued at a premium |
| Principal total | | | | 4,864.438 | Less unamortised discount, premium and issuance costs 28.375; carrying value 4,836.063 |

### Definition review

- Management EBITDA: net income plus income taxes, net interest income and expense, and depreciation and amortisation including depreciation within direct costs (Q1 FY2027 release page:10). The four published reconciliations were re-added and tie to the printed totals (see Calculations). Stock-based compensation (79.514 in FY2026, cash flow statement) is not added back, and the Q3 FY2026 release states EBITDA "includes $17.4 million of ARKA-related transaction expenses" (Q3 release page:1). No adjusted EBITDA is reported; the company reports adjusted net income only.
- Interest: "Interest expense and other, net" is one line. Cash interest is the cash flow supplemental line. Neither is a covenant interest measure.
- Total debt here is principal of the six listed instruments. Operating leases, receivable sales, retirement obligations, contingent consideration and the swaps are outside it.
- Covenant definitions: the only text names "a maximum total net leverage ratio and a minimum interest coverage ratio" (10-Q ended December 31, 2025, page:12) and later filings state compliance. Levels, step-downs, definitions and the reported ratios are Not supplied. The metrics above are not the covenant metrics.

### Claims outside the debt figure

| Item | Amount | Inside or outside the debt figure | Locator |
| --- | --- | --- | --- |
| Operating leases (all leases are operating) | Total liabilities 483.024 at June 30, 2026 (current 51.255, non-current 431.769); undiscounted payments 607.532; further 32.2 of leases not yet commenced | Outside | 10-K page:86 |
| Receivable sale program with MUFG Bank, Ltd. | Sold balance 349.999 less cash collected not remitted 160.719 gives remaining sold receivables 189.280 at September 30, 2026; maximum 350.0; term extended to December 18, 2026 | Outside (derecognised); the unremitted cash is a liability in other accrued expenses | 10-Q Q1 FY2027 page:8; 10-K page:85 |
| Supplemental Retirement Savings Plan obligations (non-qualified, defined contribution) | 130.7 at June 30, 2026, of which the current part is in accrued compensation; 118.734 non-current on the September 30, 2026 balance sheet; funded by corporate owned life insurance assets of 103.874 | Outside | 10-K page:97; 10-Q page:3 |
| Accrued post-retirement obligations | 6.967 at June 30, 2026 | Outside | 10-K page:92 |
| Contingent acquisition consideration | 7.835 current and 0.551 non-current at September 30, 2026 | Outside | 10-Q page:10 |
| Al Shimari litigation | A 42 million jury judgment (November 2024) vacated by the District Court on October 21, 2026; plaintiffs may seek Supreme Court review; no amounts recognised | Outside; contingent | 10-Q page:13; 10-K page:99 |
| Interest rate swaps | Notional 1,400.0 at September 30, 2026, asset fair value 25.367 (1.978 current plus 23.389 non-current) | Outside | 10-Q page:9, page:10 |
| Standby letters of credit | Statement of no borrowings on the standby letter of credit sub-facility of 25.0; no amount drawn | Not applicable | 10-Q page:9 |
| Pension (defined benefit), purchase and capacity commitments, supply-chain finance | Not supplied: searched for defined benefit, purchase obligation, supply chain finance and supplier finance; only defined contribution plans and a bridge commitment (terminated) found | Not assessable | 10-K pages:81, 97 |

### Latest quarter and subsequent events

- Quarter ended September 30, 2026: revenues up 8.2% with organic growth of 2.1% (Q1 10-Q page:18); a 5.0 purchase-price refund reduced the ARKA consideration to 2,637.7 and moved the cash flow acquisitions line to a positive 5.0 (10-Q pages:3, 5).
- Subsequent to the balance sheet: the Board approved on October 20, 2026 a change to a calendar fiscal year with a six-month transition period to December 31, 2026 (10-Q page:13); the Court of Appeals issued the mandate on October 20 and the District Court vacated the judgment on October 21, 2026 (10-Q page:13); fiscal 2027 guidance was raised on October 21, 2026 (release page:4); the receivable sale program term ends December 18, 2026 (10-K page:85, after the cutoff and stated here as a contract term only).
- Financing events in FY2026: Credit Facility amended November 25, 2025 to extend maturity; Term Loan B-2 of 800.0 on March 9, 2026; 500.0 add-on notes on March 12, 2026 with 516.5 net proceeds; a 1,300.0 bridge commitment was undrawn and terminated March 9, 2026 (10-K pages:81, 88, 89). Swaps of 800.0 were added in May 2026 (10-K page:90).

### Interpretation: evidence, mechanism, credit implication

Leverage. Evidence: principal debt rose from 2,942.625 to 4,931.125 between June 30, 2025 and June 30, 2026 (10-K page:86) while management EBITDA rose from 966.796 to 1,173.914 (release page:12). Mechanism: the acquisition debt arrived in March 2026 and its earnings are in the base for under four months of FY2026 and for under seven months of the latest twelve months, so reported ratios carry a timing mismatch that may overstate run-rate leverage; the size of that effect is not supplied because no pro forma figure is given (the 10-K states pro forma results were not material, page:81). Implication: reported leverage of 3.94x on the latest twelve months may overstate run-rate leverage, and should be refined when later periods carry more of the acquired earnings or a pro forma figure is supplied.

Coverage and cash. Evidence: cash interest paid 213.640 in FY2026 and 42.619 in Q1 FY2027 against an income statement charge of 215.454 and 73.240. Mechanism: the quarterly cash number omits note coupons (semi-annual) and floating-rate timing; the income statement charge is the better guide to the current interest run-rate. Implication: do not annualise the Q1 FY2027 cash interest; the cover ratios in the charts are historical cash-basis cover.

Liquidity and refinancing. Evidence: cash 279.389 and undrawn revolver 1,395.0 at September 30, 2026 against 46.750 scheduled in FY2027 and no maturity above 78.000 until FY2031. Mechanism: the revolver matures November 2030 and carries a 605.000 drawn balance, so refinancing risk sits in FY2031 and beyond; the receivable sale program (sold balance at the 350.0 maximum) expires in December 2026 and is a short-dated source of working-capital cash outside the debt figure. Implication: near-term liquidity is not a constraint on printed inputs; renewal of the receivable program is the nearest dated funding event.

Interest rate exposure. Evidence: floating-rate instruments total 3,364.438 (revolver, Term Loan, Term Loan B, Term Loan B-2) against swaps of 1,400.0 notional, and management states a one percent move changes quarterly interest on variable debt by 5.1 (10-Q page:22). Mechanism: about 1,964.438 of floating debt is unhedged by the notional shown, and swaps mature through 2030. Implication: higher rates would raise cash interest and reduce cover.

## Calculations

All amounts in US$ millions, from printed inputs in US$ thousands divided by one thousand. LTM means last twelve months to September 30, 2026 = FY2026 plus Q1 FY2027 less Q1 FY2026 (same fiscal first quarter of the prior year).

### LTM bridge

| Item | FY2026 | plus Q1 FY2027 | less Q1 FY2026 | LTM |
| --- | --- | --- | --- | --- |
| Revenues | 9,567.779 | 2,474.597 | 2,287.623 | 9,754.753 |
| Management EBITDA | 1,173.914 | 328.828 | 268.613 | 1,234.129 |
| Income from operations | 919.815 | 247.528 | 212.275 | 955.068 |
| Net income | 535.808 | 130.367 | 124.810 | 541.365 |
| Interest expense and other, net | 215.454 | 73.240 | 46.173 | 242.521 |
| Cash paid for interest | 213.640 | 42.619 | 35.768 | 220.491 |
| Cash paid for income taxes | 93.169 | 13.177 | 30.476 | 75.870 |
| Operating cash flow | 886.710 | 161.314 | 171.065 | 876.959 |
| Capital expenditures | 106.653 | 11.359 | 17.014 | 100.998 |
| Free cash flow, management definition | 735.433 | 133.489 | 142.960 | 725.962 |
| Domestic Operations revenues | 9,260.288 | 2,398.161 | 2,210.044 | 9,448.405 |
| International Operations revenues | 307.491 | 76.436 | 77.579 | 306.348 |
| Domestic Operations income from operations | 859.873 | 234.267 | 199.434 | 894.706 |
| International Operations income from operations | 59.942 | 13.261 | 12.841 | 60.362 |

### Ratios

| Ratio | Formula and inputs | Result |
| --- | --- | --- |
| Total debt / EBITDA, FY2025 | 2,942.625 / 966.796 | 3.04x |
| Total debt / EBITDA, FY2026 | 4,931.125 / 1,173.914 | 4.20x |
| Total debt / EBITDA, LTM | 4,864.438 / 1,234.129 | 3.94x |
| Net debt, FY2025 | 2,942.625 less cash 106.181 | 2,836.444 |
| Net debt, FY2026 | 4,931.125 less cash 191.756 | 4,739.369 |
| Net debt, September 30, 2026 | 4,864.438 less cash 279.389 | 4,585.049 |
| Net debt / EBITDA, FY2025 | 2,836.444 / 966.796 | 2.93x |
| Net debt / EBITDA, FY2026 | 4,739.369 / 1,173.914 | 4.04x |
| Net debt / EBITDA, LTM | 4,585.049 / 1,234.129 | 3.72x |
| EBITDA / cash interest, FY2025 | 966.796 / 145.040 | 6.67x |
| EBITDA / cash interest, FY2026 | 1,173.914 / 213.640 | 5.49x |
| EBITDA / cash interest, LTM | 1,234.129 / 220.491 | 5.60x |
| EBITDA / cash interest, Q1 FY2026 | 268.613 / 35.768 | 7.51x |
| EBITDA / cash interest, Q1 FY2027 | 328.828 / 42.619 | 7.72x |
| EBITDA margin, LTM | 1,234.129 / 9,754.753 | 12.7% |
| Operating cash flow less capex, LTM | 876.959 less 100.998 | 775.961 |
| Liquidity, September 30, 2026 | Cash 279.389 plus undrawn revolver 1,395.0 | 1,674.389 |
| Liquidity, June 30, 2026 | Cash 191.756 plus undrawn revolver 1,340.0 | 1,531.756 |
| Undrawn revolver check, September 30, 2026 | Commitment 2,000.0 less drawn 605.000 | 1,395.000, equals printed 1,395.0 |
| Remaining sold receivables, September 30, 2026 | 349.999 less 160.719 | 189.280, equals printed |
| Floating-rate principal, September 30, 2026 | 605.000 plus 1,226.563 plus 736.875 plus 796.000 | 3,364.438 |
| Floating principal not covered by swap notional | 3,364.438 less 1,400.0 | 1,964.438 |
| Maturity schedule check | 46.750 plus 62.375 plus 78.000 plus 78.000 plus 1,706.750 plus 2,959.250 | 4,931.125, equals principal |
| Debt table check, September 30, 2026 | 605.000 plus 1,226.563 plus 736.875 plus 796.000 plus 1,000.000 plus 500.000 | 4,864.438, equals printed |

### EBITDA reconciliation re-addition

| Period | Net income plus taxes plus net interest plus D&A | Result | Printed EBITDA |
| --- | --- | --- | --- |
| FY2026 | 535.808 plus 168.553 plus 215.454 plus 254.099 | 1,173.914 | 1,173.914 |
| FY2025 | 499.830 plus 105.511 plus 158.844 plus 202.611 | 966.796 | 966.796 |
| Q1 FY2027 | 130.367 plus 43.921 plus 73.240 plus 81.300 | 328.828 | 328.828 |
| Q1 FY2026 | 124.810 plus 41.292 plus 46.173 plus 56.338 | 268.613 | 268.613 |

## Gaps

| Gap | Effect | Remediation |
| --- | --- | --- |
| Covenant levels, step-downs, definitions, reported ratios and headroom: Not supplied (credit agreement and indentures not in the pack) | Covenant compliance and headroom are Not calculable; leverage and cover shown are not covenant ratios | Add the executed credit agreement, term loan agreement and indentures |
| Guarantor group and collateral schedule: Not supplied; the indentures state "the guarantors named therein" and the credit facility text says "A majority of our assets" are collateral | Structural ranking and recovery by entity cannot be built | Add the subsidiaries exhibit and guarantor schedules |
| No pro forma EBITDA for the acquired business for the full twelve months | LTM leverage overstated against run-rate; size not quantified | Use the transition-period report when published (after the cutoff) or add acquirer pro forma data |
| Debt table, balance sheet and facility availability at September 30, 2025 and June 30, 2025 revolver commitment: Not supplied | Q1 FY2026 leverage and the June 30, 2025 liquidity point not calculable | Add the Q1 FY2026 10-Q and prior-year facility description |
| Discrete quarterly cash interest omits coupon timing | Quarterly cover not suitable for run-rate use | Use cash interest from a full coupon cycle or the income statement charge |
| Fiscal-year change: the next report covers six months; guidance basis in the October 21, 2026 release not reconciled to the change | Period labels and comparison bases will change | Read the transition report and updated guidance when available |
| Purchase price allocation for the acquisition still preliminary | Goodwill and intangibles may change | Track later filings |
| Defined benefit pension, purchase commitments, supply-chain finance: Not supplied after search | Other debt-like claims not assessable | None available in the pack |
| Operating lease total at September 30, 2026: Not supplied | Lease-adjusted leverage not computed | Quarterly lease note or reconstruct from the 10-K |
| Figures taken from text extraction, not independently re-keyed | Fidelity not independently reviewed | Spot-check against the filed documents |

## Next module

CP-1A (business and transaction context) follows, then CP-2 and CP-5. CP-1A should use this handoff's base for the acquisition and financing facts, state Not supplied for covenant levels, guarantors and pro forma earnings, label all figures by period (FY2025, FY2026, Q1 FY2027, LTM September 30, 2026), and prefer the later filing where the acquisition price or the litigation differs.
