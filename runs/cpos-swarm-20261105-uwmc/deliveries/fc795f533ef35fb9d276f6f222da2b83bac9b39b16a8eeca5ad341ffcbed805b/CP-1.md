# CP-1 — Financial base: UWM Holdings Corp (uwmc)

## Request

- Issuer: UWM Holdings Corp (UWM Holdings Corporation, NYSE "UWMC"), as of 2026-11-05, information cutoff 2026-11-05, pathway credit_snapshot. Reporting currency USD. Current period Q2 2026 (quarter ended June 30, 2026); prior period FY2025 (context).
- Execution: host session; the host read the pinned page text and wrote this answer. No provider was called.
- Question: what is the reported financial base for the credit view, covering earnings, cash flow, funding and non-funding debt, liquidity, maturities, coverage and the covenant picture, for FY2025 and the first six months of 2026?
- Perimeter: UWM Holdings Corporation and its consolidated subsidiaries (Up-C structure; the statements effectively represent Holdings LLC and its subsidiaries, Q2 10-Q `page:22`). No parent-only, issuer-only or restricted-group statements are supplied.
- Units: US$ thousands as the statements print them. The four chart tables use US$ millions as their selectors require. Prose uses US$ millions with one decimal.
- Periods: FY2025; Q1 2026 (three months ended March 31, 2026); Q2 2026; H1 2026 (six months ended June 30, 2026); H1 2025; LTM Q2 2026 (calculated as FY2025 plus H1 2026 less H1 2025); LTM Q1 2026 (FY2025 plus Q1 2026 less Q1 2025).
- Locators are `page:N` of the pinned `.jsonl` text of each source, not printed page numbers. "Q2 10-Q" is the Form 10-Q for June 30, 2026; "Q1 10-Q" for March 31, 2026; "Q2 release" and "Q1 release" are the Exhibit 99.1 press releases of August 5 and May 6, 2026.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_uwmc-20251231.htm.jsonl | 6df0e879c343753ce405aeb907aabeaeac058e835b89efb10be5b5f6ef447e2d | Audited FY2025, FY2024 and FY2023 statements, Adjusted EBITDA reconciliation, debt, lease and liquidity text |
| 10-Q_2025-09-30_uwmc-20250930.htm.jsonl | 84f53b3c261a44ff2b63ce2fd8da76aab14001838b1a0e3a2f304e513f9c0145 | Q3 2025 Adjusted EBITDA (quarter) used to cross-check the Q3 2025 and Q4 2025 split |
| 10-Q_2026-03-31_uwmc-20260331.htm.jsonl | eb1fccb72198e8bd32b24af480098c49a4e103fa66da8e8b43ba0a46fdd7b8e3 | Unaudited Q1 2026 and Q1 2025 statements, Q1 cash flow, MSR facility balances |
| 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | cea2518652546d9284379186814d587a8012203f70fc41bfc3b1a399bf834746 | Unaudited Q2 2026 and H1 2026 statements, debt notes, liquidity, covenants, subsequent events |
| EX-99.1_2026-02-26_irdeck4q25andfy2025-fina.htm.jsonl | 80372136ddaf727708bb7d020bd60e922c0bc6f80a8ff31bd92d35cba8e5b9c2 | FY2025 appendix on non-funding debt and Adjusted EBITDA (supporting; management presentation) |
| EX-99.1_2026-05-06_q12026ex-991pressrelease.htm.jsonl | 3516810c7f76bb754add7c9c09ef459031d4e398744e48f97ba6a9a478ed6c73 | Q1 2026 release: Adjusted EBITDA for Q1 2026, Q4 2025 and Q1 2025; non-funding debt (supporting) |
| EX-99.1_2026-08-05_q22026ex-991pressrelease.htm.jsonl | fce3d1caab58675ec9b80c128baca52e2510780e5b4d2dc29c8a0ea2b81bebde | Q2 2026 release: five-quarter balance sheet and operations addendum; non-funding debt; liquidity claim (supporting) |
| context | 9e4b4c779a926897468f1dfd198d157aa081551eb0aa185c7568e6564f764c9f | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 2571b7e9360f6c0ea273bba21e1fe841a47b3e684ddd02e1c3fe019c258d1214 | Source readiness: every consumer READY_WITH_LIMITATIONS; carries the missing agreements, the August 5, 2026 post-period transaction, two conflicts and the absence of filings after August 7, 2026 |

Consistency with CP-0: this answer confirms CP-0's conflict on the Conventional servicing-rights facility covenant set (Q2 10-Q `page:16` against `page:54`) and its statement that the June 30, 2026 balance sheet shows no preferred stock (`page:2`). It adds three points CP-0 did not list: the Q1 10-Q's restricted-cash comparative differs from the 10-K and Q2 10-Q; the limits of the two servicing-rights facilities rose between March 31 and June 30, 2026 without an amendment being described in the Q2 10-Q; and the February 2026 presentation differs by 2 from the 10-K in one FY2024 Adjusted EBITDA figure. None corrects CP-0.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Non-funding debt of 6,040.4 million is 7.64x last-twelve-months Adjusted EBITDA of 790.6 million, against 6.16x at FY2025. The second-quarter net loss of 451.9 million was driven by derivative losses that Adjusted EBITDA excludes. | Medium | Adjusted EBITDA is company-defined, the June 2026 figures are unaudited, and the August 2026 preferred raise is not in the statements. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Non-funding debt rose 1,747.5 million in six months, driven by 1,750.0 million of added servicing-rights borrowings. | Secured borrowing now funds the servicing-rights build; non-funding debt to equity reached 6.13x. | High |
| Last-twelve-months net loss was 105.0 million, while Adjusted EBITDA excludes a combined 526.8 million net loss from servicing-rights valuation and derivatives. | Earnings that reach equity are far weaker than Adjusted EBITDA suggests. | Medium |
| Operating cash flow was negative 1,885.8 million for six months 2026, and negative 1,084.8 million after adding servicing-rights sale proceeds. | Operations did not fund themselves; borrowings covered the gap. | High |
| Liquidity was 1,277.4 million: 477.4 million unrestricted cash plus 800.0 million of undrawn lines, of which 300.0 million is uncommitted. | Headroom relies on lender discretion and collateral values. | Medium |
| Warehouse lines with 5,090.8 million advanced expire by May 2027, and 2,375.0 million of non-funding debt falls due in 2027. | Renewal and refinancing needs concentrate in 2027. | Medium |

### Financial base view

UWM Holdings Corp is a wholesale mortgage originator whose reported debt has two parts that must be read separately: warehouse lines of 8,600.1 million that finance mortgage loans for days or weeks, and non-funding debt of 6,040.4 million (senior notes, servicing-rights facilities, borrowings against investment securities and finance leases) that finances the corporate balance sheet and the 5,311.5 million servicing-rights asset. The company's own leverage measure is non-funding debt to total equity, which was 6.13x at June 30, 2026 against 2.69x at December 31, 2025, because debt rose by 1,747.5 million while total equity fell by 608.3 million to 985.3 million. On Adjusted EBITDA, which already deducts warehouse interest but not interest on non-funding debt, non-funding debt was 7.64x the last twelve months at June 30, 2026 (790.6 million), against 6.16x at FY2025 (697.3 million). Earnings quality is the central issue: Adjusted EBITDA for Q2 2026 was 185.9 million while the net loss was 451.9 million, because the company adds back a 603.2 million loss on other interest rate derivatives and removes a 65.1 million servicing-rights valuation gain. For the last twelve months those two excluded items net to a 526.8 million loss, and net loss was 105.0 million. Operating cash flow was negative 1,885.8 million for H1 2026, with servicing-rights sale proceeds of 801.0 million in investing activities, and the gap was funded by 1,750.0 million of net borrowing on the servicing-rights lines. Liquidity on the company's basis is about 1.3 billion (1,298.4 million with restricted cash), but 300.0 million of the undrawn lines is uncommitted and the 500.0 million revolver is provided by SFS Corp., an entity controlled by the CEO. Cash of 321.8 million was paid to equity holders in H1 2026 through dividends and member distributions. Warehouse lines with 5,090.8 million advanced expire on or before May 14, 2027, and 2,375.0 million of non-funding debt (the 2027 notes and the Conventional servicing-rights facility) falls due in 2027. All figures are unaudited for 2026 and exclude the August 5, 2026 preferred stock and warrant transaction, which closed after the period.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 6.16 | 5.46 | x | Total debt is the company's non-funding debt (4,292.9 at December 31, 2025: carrying value of senior notes, secured lines, borrowings against investment securities and finance leases) over FY2025 Adjusted EBITDA of 697.3. Net debt deducts unrestricted cash of 482.4 (cash 503.4 less restricted 21.0, rounded as the filing prints it). Excludes warehouse lines of 8,912.5. Adjusted EBITDA is a company non-GAAP measure. |
| LTM Q1 2026 | 6.36 | 5.86 | x | Non-funding debt 5,092.8 at March 31, 2026 over LTM Adjusted EBITDA of 800.4 (calculated). Net debt deducts unrestricted cash of 403.0. Excludes warehouse lines of 9,900.3. |
| LTM Q2 2026 | 7.64 | 7.04 | x | Non-funding debt 6,040.4 at June 30, 2026 over LTM Adjusted EBITDA of 790.6 (calculated). Net debt deducts unrestricted cash of 477.4. Excludes warehouse lines of 8,600.1, which are secured by mortgage loans and whose interest is already deducted in Adjusted EBITDA. Senior notes are at carrying value (principal 3,000.0). Not an indenture or covenant ratio. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 3.25 | x | Not a cash-interest ratio. Cash interest on non-funding debt is not reported separately, so this is FY2025 Adjusted EBITDA of 697.3 over interest expense on non-funding debt of 214.5 (accrual, from the Adjusted EBITDA reconciliation). Total cash paid for interest of 496.2 includes warehouse interest already deducted in Adjusted EBITDA. |
| LTM Q1 2026 | 3.40 | x | Not a cash-interest ratio. LTM Adjusted EBITDA of 800.4 over LTM interest expense on non-funding debt of 235.2 (calculated, accrual). Total cash paid for interest for the last twelve months was 557.4. |
| LTM Q2 2026 | 2.92 | x | Not a cash-interest ratio. LTM Adjusted EBITDA of 790.6 over LTM interest expense on non-funding debt of 271.2 (calculated, accrual). Total cash paid for interest for the last twelve months was 551.7, of which the non-funding part is not reported. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Q4 2025 (December 31, 2025) | 482.4 | 1300.0 | US$m | Unrestricted cash is 503.4 less restricted 21.0. Undrawn lines are limit less drawn: Conventional servicing-rights facility 1,500.0 less 900.0, Ginnie Mae servicing-rights facility 500.0 less 300.0, and the 500.0 SFS Corp. revolver undrawn. The two servicing-rights facilities are described as uncommitted, and the filing does not say whether the revolver is committed, so the word committed in the column header does not fit these lines. Warehouse lines excluded. |
| Q1 2026 (March 31, 2026) | 403.0 | 900.0 | US$m | Unrestricted cash is 424.0 less restricted 21.0. Conventional facility 1,500.0 less 1,425.0 (derived as secured lines of 2,000.0 less Ginnie Mae 575.0; the filing rounds it to 1.4 billion), Ginnie Mae facility 900.0 less 575.0, revolver 500.0 undrawn. Uncommitted servicing-rights lines as above. Company text: about 1.3 billion including 424.0 of cash. |
| Q2 2026 (June 30, 2026) | 477.4 | 800.0 | US$m | Unrestricted cash is 498.4 less restricted 21.0. Conventional facility 2,000.0 less 1,875.0 = 125.0; Ginnie Mae facility 1,250.0 less 1,075.0 = 175.0; revolver 500.0 undrawn. The 2,000.0 Conventional limit is the combined limit shared with a warehouse counterparty and fully allocated to the servicing-rights facility. Available borrowing depends on advance rates against collateral value, so headroom is a ceiling. Company text: about 1.3 billion including 498.4 of cash. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| H2 2026 | 83.7 | US$m | Borrowings against investment securities, remaining terms one to three months at June 30, 2026 (Q2 10-Q `page:57`); the company intends to renew them. Warehouse lines of 8,600.1 are excluded and listed separately in the facility table. |
| FY2027 | 2375.0 | US$m | 2027 senior notes of 500.0 (June 15, 2027) plus the Conventional servicing-rights facility balance of 1,875.0 (maturity July 15, 2027). Principal amounts. |
| FY2028 | 0.0 | US$m | No instrument in the senior note table or the servicing-rights facility disclosure matures in 2028. The Ginnie Mae facility draw period ends March 20, 2028 but its maturity is 2029. |
| FY2029 | 1775.0 | US$m | 2029 senior notes of 700.0 (April 15, 2029) plus the Ginnie Mae servicing-rights facility balance of 1,075.0 (March 20, 2029). |
| FY2030 | 800.0 | US$m | 2030 senior notes of 800.0 (February 1, 2030); issuer Holdings LLC, guaranteed by UWM. |
| FY2031 | 1000.0 | US$m | 2031 senior notes of 1,000.0 (March 15, 2031); issuer Holdings LLC, guaranteed by UWM. |
| Unscheduled | 22.4 | US$m | Finance lease liability at carrying value, remaining terms about three to ten years (Q2 10-Q `page:57`). Principal total of all rows is 6,056.1 (senior notes at principal 3,000.0); carrying-value non-funding debt is 6,040.4. Maturities assume no prepayment or extension. |

### Financials and credit metrics

| Metric (US$ thousands unless stated) | FY2025 | Q1 2026 | Q2 2026 | H1 2026 | H1 2025 | LTM Q2 2026 | Basis and locators |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Loan origination volume | 163,446,463 | 44,944,156 | 39,702,264 | 84,646,420 | 72,096,290 | 175,996,593 | Reported (10-K `page:92`; Q2 release `page:2`; Q2 10-Q `page:40`). LTM calculated. |
| Total gain margin (%) | 1.16 | 1.23 | 1.33 | 1.28 | 1.04 | 1.27 | Reported except LTM, calculated as LTM loan production income over LTM volume. |
| Loan production income | 1,898,141 | 554,572 | 527,217 | 1,081,789 | 752,633 | 2,227,297 | Reported (10-K `page:127`; Q2 10-Q `page:3`). LTM calculated. |
| Loan servicing income | 724,741 | 213,379 | 220,503 | 433,882 | 369,330 | 789,293 | Reported. LTM calculated. |
| Interest income | 537,687 | 133,476 | 140,283 | 273,759 | 250,107 | 561,339 | Reported. LTM calculated. |
| Total revenue | 3,160,569 | 901,427 | 888,003 | 1,789,430 | 1,372,070 | 3,577,929 | Reported. LTM calculated. |
| Change in fair value of mortgage servicing rights | (1,055,448) | (10,335) | (122,683) | (133,018) | (500,006) | (688,460) | Reported, within other gains (losses). LTM calculated. |
| Gain (loss) on other interest rate derivatives | 298,126 | (138,198) | (603,191) | (741,389) | 208,904 | (652,167) | Reported, within other gains (losses). LTM calculated. |
| Total expenses | 2,152,351 | 575,394 | 635,050 | 1,210,444 | 1,012,366 | 2,350,429 | Reported. LTM calculated. |
| Interest expense, total | 530,794 | 140,765 | 158,939 | 299,704 | 253,877 | 576,621 | Reported. LTM calculated. |
| of which interest expense on non-funding debt | 214,513 | 70,727 | 86,810 | 157,537 | 100,855 | 271,195 | Adjusted EBITDA reconciliation (10-K `page:90`; Q1 release `page:5`; Q2 10-Q `page:38`). LTM calculated. |
| of which interest expense on funding facilities | 316,281 | 70,038 | 72,129 | 142,167 | 153,022 | 305,426 | Total less non-funding. FY2025, Q1 2026 and LTM calculated; Q2 2026, H1 2026 and H1 2025 as printed (Q2 10-Q `page:43`). |
| Earnings (loss) before income taxes | 250,896 | 177,500 | (472,921) | (295,421) | 68,602 | (113,127) | Reported. LTM calculated. |
| Net income (loss) | 244,023 | 170,374 | (451,902) | (281,528) | 67,451 | (104,956) | Reported. LTM calculated. |
| Net income (loss) attributable to UWMC | 27,380 | 25,301 | (80,594) | (55,293) | 9,230 | (37,143) | Reported. LTM calculated. The rest is attributable to non-controlling interest held by SFS Corp. |
| Adjusted EBITDA (company non-GAAP) | 697,336 | 160,909 | 185,879 | 346,787 | 253,485 | 790,638 | Reported (10-K `page:90`; Q1 release `page:5`; Q2 release `page:5`; Q2 10-Q `page:38`). LTM calculated; the sum of the last four quarters is 790,639 (rounding of 1). |
| Net cash (used in) provided by operating activities | (2,647,557) | (2,229,879) | 344,037 | (1,885,842) | 328,022 | (4,861,421) | Reported for FY2025, Q1 2026, H1 2026, H1 2025 (10-K `page:129`; Q1 10-Q `page:4`; Q2 10-Q `page:4`); Q2 2026 derived as H1 less Q1. LTM calculated. |
| Capitalization of mortgage servicing rights (non-cash, deducted in operating cash flow) | (3,647,451) | (1,101,017) | (1,041,838) | (2,142,855) | (1,636,842) | (4,153,464) | Reported (Q2 10-Q `page:4` and `page:12`). LTM calculated. |
| Net proceeds from sale of mortgage servicing rights (investing) | 2,423,711 | 542,626 | 258,387 | 801,013 | 1,591,780 | 1,632,944 | Reported (10-K `page:129`; Q1 10-Q `page:4`; Q2 10-Q `page:5`); Q2 2026 derived. LTM calculated. |
| Operating cash flow plus net MSR sale proceeds | (223,846) | (1,687,253) | 602,424 | (1,084,829) | 1,919,802 | (3,228,477) | Calculated; not a company-defined measure. |
| Purchases of premises and equipment and internal-use software | (74,048) | (19,063) | (9,462) | (28,525) | (41,955) | (60,618) | Reported (the FY2025 caption omits internal-use software); Q2 2026 derived. LTM calculated. |
| Dividends paid to Class A stockholders | (78,596) | (26,842) | (33,025) | (59,867) | (34,569) | (103,894) | Reported; Q2 2026 derived. LTM calculated. |
| Member distributions paid to SFS Corp. | (637,999) | (133,148) | (128,748) | (261,896) | (343,589) | (556,306) | Reported; Q2 2026 derived. LTM calculated. |
| Cash paid for interest (all interest) | 496,248 | 145,972 | 142,999 | 288,971 | 233,534 | 551,685 | Supplemental cash flow (10-K `page:129`; Q1 10-Q `page:5`; Q2 10-Q `page:5`); Q2 2026 derived. LTM calculated. |
| Cash paid for taxes | 914 | 39 | 60 | 99 | 161 | 852 | Supplemental cash flow; Q2 2026 derived. LTM calculated. |
| Non-funding debt (period end, carrying value) | 4,292,940 | 5,092,831 | 6,040,429 | n/a (instant) | n/a (instant) | n/a (instant) | Q1 release `page:6`; Q2 release `page:5` to `page:6`; deck `page:12`. |
| Total equity (period end) | 1,593,629 | 1,600,901 | 985,308 | n/a (instant) | n/a (instant) | n/a (instant) | Balance sheets (10-K `page:127`; Q2 10-Q `page:3`). |
| Non-funding debt / total equity (x) | 2.69 | 3.18 | 6.13 | n/a (ratio) | n/a (ratio) | n/a (ratio) | Company non-GAAP; recomputed (4,292,940 / 1,593,629; 5,092,831 / 1,600,901; 6,040,429 / 985,308) and equal to the printed ratios. |
| Non-funding debt / LTM Adjusted EBITDA (x) | 6.16 | 6.36 | 7.64 | n/a (ratio) | n/a (ratio) | 7.64 | Calculated; Q1 2026 uses LTM Q1 2026 Adjusted EBITDA of 800,442. |
| Adjusted EBITDA / interest expense on non-funding debt (x) | 3.25 | n/a | n/a | n/a | n/a | 2.92 | Calculated; accrual basis, not cash interest. |

### Balance sheet and capital structure

| Line (US$ thousands) | December 31, 2025 | March 31, 2026 | June 30, 2026 | Locator |
| --- | --- | --- | --- | --- |
| Cash and cash equivalents (includes restricted cash of about 21,000) | 503,364 | 423,996 | 498,407 | 10-K `page:126`; Q2 release `page:10`; Q2 10-Q `page:2` |
| Mortgage loans at fair value | 9,932,729 | 10,991,101 | 9,619,076 | same |
| Mortgage servicing rights | 4,073,781 | 4,591,855 | 5,311,465 | same |
| Accounts receivable, net | 526,694 | 1,271,014 | 531,790 | same |
| Loans eligible for repurchase from Ginnie Mae (asset and equal liability) | 1,133,359 | 1,124,020 | 1,141,719 | same |
| Total assets | 16,928,676 | 19,266,244 | 17,940,542 | same |
| Warehouse lines of credit | 8,912,496 | 9,900,303 | 8,600,078 | same |
| Secured lines of credit (servicing-rights facilities) | 1,200,000 | 2,000,000 | 2,950,000 | same |
| Senior notes (carrying value) | 2,981,975 | 2,983,152 | 2,984,328 | same |
| Borrowings against investment securities | 87,497 | 86,724 | 83,660 | same |
| Finance lease liability | 23,468 | 22,955 | 22,441 | same |
| Operating lease liability (outside non-funding debt) | 100,596 | 98,811 | 97,034 | same |
| Derivative liabilities | 26,574 | 337,817 | 33,566 | same |
| Accounts payable, accrued expenses and other | 707,790 | 949,788 | 881,997 | same |
| Accrued distributions and dividends payable | 161,292 | 161,773 | 160,411 | same |
| Total liabilities | 15,335,047 | 17,665,343 | 16,955,234 | same |
| Non-controlling interest (SFS Corp.) | 1,394,112 | 1,371,380 | 851,470 | same |
| Total equity | 1,593,629 | 1,600,901 | 985,308 | same |
| Equity excluding non-controlling interest (calculated) | 199,517 | 229,521 | 133,838 | Sum of Class A, Class D, paid-in capital and retained earnings |

The June 30, 2026 balance sheet shows no preferred stock issued or outstanding (Q2 10-Q `page:2`); the August 5, 2026 preferred stock is a subsequent event (Q2 10-Q `page:32` to `page:33`).

### Debt and funding facilities at June 30, 2026

| Instrument | Issuer / borrower | Amount (US$ thousands) | Rate | Maturity | Security and guarantors | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| 2027 senior notes | UWM | 499,170 carrying; 500,000 principal | 5.750% | June 15, 2027 | Unsecured; guarantors not stated | Q2 10-Q `page:17` |
| 2029 senior notes | UWM | 697,558 carrying; 700,000 principal | 5.500% | April 15, 2029 | Unsecured; guarantors not stated | Q2 10-Q `page:17` |
| 2030 senior notes | Holdings LLC | 795,019 carrying; 800,000 principal | 6.625% | February 1, 2030 | Unsecured; guaranteed by UWM | Q2 10-Q `page:17` to `page:18` |
| 2031 senior notes | Holdings LLC | 992,581 carrying; 1,000,000 principal | 6.250% | March 15, 2031 | Unsecured; guaranteed by UWM | Q2 10-Q `page:17` to `page:18` |
| Conventional MSR facility (Citibank) | UWM | 1,875,000 drawn; limit 2,000,000, uncommitted | SOFR plus margin | July 15, 2027 | Secured by Fannie Mae and Freddie Mac MSRs | Q2 10-Q `page:15` to `page:16` |
| Ginnie Mae MSR facility (Goldman Sachs Bank USA) | UWM | 1,075,000 drawn; limit 1,250,000, uncommitted | SOFR plus margin | Draw period to March 20, 2028; maturity March 20, 2029 | Secured by Ginnie Mae MSRs | Q2 10-Q `page:16` |
| Borrowings against investment securities | UWM (master repurchase agreement) | 83,660 | SOFR plus spread | One to three months remaining | Retained securitization interests (94.3 million pledged), about 75% advance | Q2 10-Q `page:22` and `page:57` |
| Finance lease liability | Company | 22,441 (22.0 million related party) | not stated | Three to ten years remaining | Leased assets | Q2 10-Q `page:57` |
| Revolving Credit Facility | UWM, lender SFS Corp. | 0 drawn; 500,000 facility | Applicable Prime Rate | Annual automatic renewal | Unsecured; subordinated to senior notes by Amendment No. 1 (September 2025) | Q2 10-Q `page:19` |
| Warehouse lines (11 master repurchase agreements and two early-funding programs) | UWM | 8,600,078 advanced; 900,000 of line amounts committed | SOFR plus 1.00% to 1.75% | Expiries September 29, 2026 to November 26, 2027; early funding has no expiry | Secured by pledged mortgage loans | Q2 10-Q `page:14` to `page:15` |

Memoranda: weighted average rate on servicing-rights facilities was 6.14% for Q2 2026 and 6.16% for H1 2026 (`page:16`). The weighted average effective rate on senior notes was 6.25% (`page:17`). Estimated fair value of the four senior notes was 2,783,429 against carrying value 2,984,328 (Level 2; `page:26`); by note 495,595, 651,112, 745,112 and 891,610 against principal of 500,000, 700,000, 800,000 and 1,000,000. At December 31, 2025 the total fair value was 3,005,945 (`page:26`), so it fell by 222,516. The count of senior note series is four, taken from the table (`page:17`); the 2025 notes of 800,000 were repaid at maturity in November 2025 (10-K `page:104`).

Warehouse lines by expiry (advanced, US$ thousands, Q2 10-Q `page:14`): 990,038 (limit 2.0 billion, September 29, 2026); 153,287 (750 million, October 8, 2026); 256,929 (325 million, December 17, 2026); 963,193 (1.5 billion, February 5, 2027); 506,673 (1.0 billion, February 9, 2027); 1,314,608 (3.0 billion, February 17, 2027); 661,696 (1.0 billion, February 19, 2027); 244,332 (500 million, May 14, 2027); nil (June 15, 2027, shared limit reallocated to the Conventional MSR facility); 1,056,961 (2.0 billion, August 3, 2027); 2,207,548 (3.5 billion, November 26, 2027); early funding 244,813 with no expiry. Lines with 5,090,756 advanced expire on or before May 14, 2027. Two of them, with 1,143,325 advanced, had expiry dates (September 29 and October 8, 2026) before the as-of date; their renewal is not in the supplied sources.

### Claims outside non-funding debt

| Claim | Amount at June 30, 2026 (US$ thousands) | Inside or outside non-funding debt | Locator |
| --- | --- | --- | --- |
| Warehouse lines of credit | 8,600,078 | Outside the company's non-funding debt definition; funding of mortgage loans | Q2 10-Q `page:2`; Q2 release `page:4` to `page:5` |
| Operating lease liability | 97,034 (96.4 million with related parties) | Outside; 10-K maturities show total payments of 144,988 at December 31, 2025 | Q2 10-Q `page:2`; 10-K `page:146` |
| Finance lease liability | 22,441 | Inside | Q2 release `page:5` to `page:6` |
| Tax Receivable Agreement liability to SFS Corp. | 279,995 (196,923 at December 31, 2025) | Outside; 85% of realized tax savings; rose 83,072 including 80.6 million from exchange transactions | Q2 10-Q `page:21`, `page:8`, `page:28` |
| Representations and warranties reserve | 104,475 | Outside | Q2 10-Q `page:20` |
| Accrued distributions and dividends payable | 160,411 (34.2 million dividend and 126.2 million member distribution paid July 9, 2026) | Outside | Q2 10-Q `page:2`, `page:59` |
| Loans eligible for repurchase from Ginnie Mae | 1,141,719 (liability, offset by an equal asset) | Outside; gross-up | Q2 10-Q `page:2`, `page:7` |
| Derivative liabilities | 33,566 | Outside | Q2 10-Q `page:11` |
| Commitments to originate loans | About 20.8 billion | Off balance sheet; many expected to expire undrawn | Q2 10-Q `page:21` |
| Related-party naming rights and sponsorship agreement | About 115 million over ten years, terminable by either party for any reason after two years | Outside | Q2 10-Q `page:27` |
| Litigation | No accrual or estimate printed; company does not expect a material adverse effect | Outside | Q2 10-Q `page:21`, `page:68` to `page:71` |
| Pensions, retiree medical, factoring and supply-chain finance | None found in the sources (searched for pension, retiree, postretirement, factoring, supply chain, purchase commitment); the 10-K describes a defined contribution 401(k) plan only | Not applicable | 10-K `page:158` |

### Covenants and regulatory minimums

| Test | Level | Reported figure | Headroom | Locator |
| --- | --- | --- | --- | --- |
| Warehouse and MSR facility financial covenants: minimum tangible net worth, minimum liquidity, maximum debt to net worth (or total liabilities to tangible net worth) and net income or profitability, as defined in each agreement | Not supplied: levels are not printed | In compliance as of June 30, 2026 | Not calculable: levels and definitions are not supplied | Q2 10-Q `page:15`, `page:16`, `page:52`, `page:54`, `page:55` |
| Senior note incurrence test: additional non-funding debt needs a Fixed Charge Coverage Ratio of at least 3.0 to 1.0 or a Debt-to-Equity Ratio not above 2.0 to 1.0 (defined terms in the indentures) | 3.0 to 1.0 or 2.0 to 1.0 | In compliance with the indentures as of June 30, 2026 | Not calculable: indenture definitions are not supplied; the company's non-funding debt to equity of 6.13 and the 2.92 accrual cover in this handoff are different constructs | Q2 10-Q `page:54` |
| Agency minimums (most restrictive of USDA, HUD, Ginnie Mae, Freddie Mac, Fannie Mae) | Net worth 743,600; liquidity 343,900; capital and risk-based capital ratios 6% (US$ thousands) | UWM in compliance; UWM's own net worth and liquidity are not printed | Not calculable: UWM-level figures are not supplied; consolidated total equity is 985,308 | Q2 10-Q `page:23` |
| Cross-default and cross-acceleration across warehouse, secured and unsecured lines | n/a | No default reported | n/a | Q2 10-Q `page:52` |

The covenant set of the Conventional servicing-rights facility is stated differently in two places (Q2 10-Q `page:16` includes maximum debt to net worth; `page:54` omits it). Neither reading is adopted.

### Adjusted EBITDA definition and reconciliation review

| Reconciling item (US$ thousands) | Q2 2026 | H1 2026 | FY2025 | Locator |
| --- | --- | --- | --- | --- |
| Net income (loss) | (451,902) | (281,528) | 244,023 | Q2 10-Q `page:38`; 10-K `page:90` |
| Interest expense on non-funding debt | 86,810 | 157,537 | 214,513 | same |
| Provision (benefit) for income taxes | (21,019) | (13,893) | 6,873 | same |
| Depreciation and amortization | 14,655 | 29,040 | 50,044 | same |
| Stock-based compensation expense | 12,494 | 25,656 | 50,363 | same |
| Change in fair value of MSRs due to valuation inputs or assumptions, net | (65,056) | (312,953) | 435,267 | same |
| (Gain) loss on other interest rate derivatives | 603,191 | 741,389 | (298,126) | same |
| Deferred compensation, net | 2,100 | 4,350 | (6,195) | same |
| Change in fair value of Public and Private Warrants | 0 | 0 | (2,743) | same; the warrants expired January 21, 2026 |
| Change in Tax Receivable Agreement liability | 612 | 2,515 | 3,144 | same |
| Change in fair value of investment securities | 558 | 861 | (4,793) | same |
| Acquisition-related expenses (net of recoveries) | 3,436 | (6,187) | 4,966 | same; the Two Harbors termination fee received in Q1 2026 is netted in H1 2026 |
| Adjusted EBITDA | 185,879 | 346,787 | 697,336 | same |

The definition excludes interest on non-funding debt but keeps interest on funding facilities as an operating cost (Q2 10-Q `page:38`). It adds back the change in servicing-rights fair value due to inputs and the full result on other interest rate derivatives. It does not add back the servicing-rights decay ("due to collection/realization of cash flows and other", 395,128 negative in H1 2026, Q2 10-Q `page:12`), so recurring runoff of the servicing asset reduces Adjusted EBITDA. The H1 2026 figure of 346,787 recomputes from the listed items. Adjusted EBITDA is not audited and is not a covenant measure.

Annual history (US$ thousands, 10-K `page:90` and `page:127`): Adjusted EBITDA 478,270 (FY2023), 459,975 (FY2024), 697,336 (FY2025); net income (loss) (69,782), 329,375, 244,023; total revenue 2,165,475, 2,674,126, 3,160,569; loan origination volume 108,275,883, 139,433,406, 163,446,463.

### Earnings, cash flow and servicing drivers

- Revenue: Q2 2026 total revenue of 888,003 was 17.0% above Q2 2025 (758,700) and 1.5% below Q1 2026 (901,427). H1 2026 revenue of 1,789,430 was 30.4% above H1 2025. Volume was flat year on year in Q2 (39.7 billion against 39.7 billion) and up 17.4% for the half (84.6 billion against 72.1 billion; Q2 10-Q `page:37`); the revenue gain came from gain margin (1.33% in Q2 2026 against 1.13% in Q2 2025) and servicing income (220,503 against 178,813).
- Expenses: H1 2026 total expenses of 1,210,444 rose 19.6% from 1,012,366; Q2 2026 general and administrative expense of 89,748 rose from 59,999, which the filing attributes to software licensing, legal fees and costs of the terminated Two Harbors merger (`page:46`).
- Net loss: the Q2 2026 net loss of 451,902 compares with net income of 314,479 in Q2 2025, a swing of 766,381, with other gains (losses), net moving from a gain of 97,483 to a loss of 725,874 (`page:3`, `page:47`).
- Servicing-rights asset: fair value rose from 4,073,781 to 5,311,465 over six months (up 1,237,684) on capitalization of 2,142,855, sales of 822,996, valuation-input gains of 312,953 and decay of 395,128 (`page:12`). Fair value is 2.14% of the 247,648,881 unpaid principal balance serviced, against 1.69% at December 31, 2025. Weighted average discount rate fell to 8.9% from 9.4% and weighted average prepayment speed to 8.6% from 10.3% (`page:13`). A 10% adverse change in discount rate lowers value by 207,202 and in prepayment speed by 200,467 (`page:13` to `page:14`). Loan servicing delinquency (60+ days) was 1.38% against 1.62% (`page:42`).
- Interest-rate sensitivity (company, hypothetical, June 30, 2026): a 25 basis point parallel fall lowers servicing rights by 313,118 and raises mortgage loans, interest rate lock commitments and other derivatives; a rise adds 234,587 to servicing rights and lowers the others (`page:66`). Other interest rate derivatives had a notional of 12,805,000 and fair value of 42,077 (`page:11`), and the company states it exited a significant number of positions entered at the end of Q1 2026 and in Q2 2026 (`page:60`).
- Cash flow quality: operating cash flow is distorted by origination and servicing mechanics. In H1 2026 the largest items were the non-cash capitalization of servicing rights (2,142,855 deducted), a decrease in mortgage loans at fair value (313,653 added) and the net loss (281,528). Servicing-rights sale proceeds of 801,013 sit in investing activities (`page:4` to `page:5`). The filing does not break out cash settled on derivative positions.
- Funding of the gap: financing activities provided 1,106,791 in H1 2026, including 3,650,000 borrowed and 1,900,000 repaid on secured lines (net 1,750,000) and net repayments of 312,417 on warehouse lines, after 59,867 of dividends and 261,896 of member distributions (`page:5`).
- Capital return: Class A dividends declared for H1 2026 were 65,589 and member distributions declared were 255,922 (`page:4`); the quarterly dividend was suspended after June 30, 2026 (Q2 release `page:3`). The release does not say whether the proportional distribution to SFS Corp. is also suspended; tax distributions remain required (`page:48`).

### Source context and version relationships

| Source | Entity and perimeter | Period and status | Statement kind and units | Version relationship |
| --- | --- | --- | --- | --- |
| 10-K | UWM Holdings Corporation, consolidated | FY2025, FY2024, FY2023; audited (Deloitte & Touche LLP opinion dated February 25, 2026, `page:125`) | Statements and notes; US$ thousands | Controls annual facts |
| Q3 2025 10-Q | Same | Q3 2025 and nine months 2025; unaudited | Interim statements; US$ thousands | Supports Q3 2025 only |
| Q1 2026 10-Q | Same | Q1 2026; unaudited | Interim statements; US$ thousands | Controls Q1 2026 |
| Q2 2026 10-Q | Same | Q2 and H1 2026; unaudited | Interim statements and notes; US$ thousands | Controls Q2 and H1 2026 |
| Q1 and Q2 2026 releases, February 2026 presentation | Same, management presentation | Q1 2026, Q2 2026, FY2025 | Non-GAAP reconciliations and addendum; US$ thousands | Supporting only; filings control |

All sources report in US dollars, matching the context's reporting currency. The balance sheet date June 30, 2026 is an instant; flows cover the stated periods. Within the Q2 2026 statements all periods carry the same perimeter and accounting basis (US GAAP, unaudited).

### Subsequent events and cutoff

On August 5, 2026 the company closed a preferred stock and warrant transaction with Oaktree and entities affiliated with the CEO: gross proceeds of 1.65 billion (1.5 billion Series A-1 and 150.0 million Series A-2, at an original issue price of 1,000 per share, 10.0% cash or 13.0% non-cash cumulative dividends) plus a planned 400 million rights offering "if needed" that expires on November 12, 2026, after the cutoff (Q2 10-Q `page:32` to `page:33`). The statements do not reflect it. Use of proceeds, fees and balance sheet classification are not supplied, so no pro forma ratio is calculated. The Q2 release headline of 2.05 billion combines the 1.65 billion and the 400 million. The quarterly dividend was suspended after June 30, 2026 (Q2 release `page:3`). Nothing dated after August 7, 2026 is used.

## Calculations

All inputs are US$ thousands from the cited locators; results are rounded as shown.

### LTM Adjusted EBITDA

| Measure | Formula | Inputs | Result |
| --- | --- | --- | --- |
| LTM Q2 2026 Adjusted EBITDA | FY2025 + H1 2026 - H1 2025 | 697,336 + 346,787 - 253,485 | 790,638 (790.6 million) |
| LTM Q1 2026 Adjusted EBITDA | FY2025 + Q1 2026 - Q1 2025 | 697,336 + 160,909 - 57,803 | 800,442 (800.4 million) |
| Cross-check, last four quarters | Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026 | 211,073 + 232,778 + 160,909 + 185,879 | 790,639; differs by 1 from the formula (rounding in the filings; H1 2025 of 253,485 against 57,803 + 195,683 = 253,486) |

### Leverage (non-funding debt basis)

| Measure | Formula | Inputs | Result |
| --- | --- | --- | --- |
| Non-funding debt / LTM Adjusted EBITDA, FY2025 | 4,292,940 / 697,336 | | 6.16x |
| Same, LTM Q1 2026 | 5,092,831 / 800,442 | | 6.36x |
| Same, LTM Q2 2026 | 6,040,429 / 790,638 | | 7.64x (7.64 rounded from 7.640) |
| Unrestricted cash | cash - restricted cash | 503,364 - 21,000; 423,996 - 21,000; 498,407 - 21,000 | 482,364; 402,996; 477,407 |
| Net non-funding debt / LTM Adjusted EBITDA | (non-funding debt - unrestricted cash) / EBITDA | (4,292,940 - 482,364) / 697,336; (5,092,831 - 402,996) / 800,442; (6,040,429 - 477,407) / 790,638 | 5.46x; 5.86x; 7.04x |
| Non-funding debt / total equity, June 30, 2026 | 6,040,429 / 985,308 | | 6.13x, equal to the printed 6.13 |
| Change in non-funding debt since December 31, 2025 | 6,040,429 - 4,292,940 | | 1,747,489 (1,747.5 million): secured lines +1,750,000, senior notes +2,353, investment securities borrowings -3,837, finance leases -1,027 |
| Non-funding debt check, June 30, 2026 | 2,984,328 + 2,950,000 + 83,660 + 22,441 | | 6,040,429 (equals the printed total) |
| Principal basis | 3,000,000 + 2,950,000 + 83,660 + 22,441 | | 6,056,101 |
| Not used: warehouse plus non-funding debt over LTM Adjusted EBITDA | (8,600,078 + 6,040,429) / 790,638 | | 18.5x; shown only to size the funding stack, since warehouse lines are secured by mortgage loans of 9,619,076 and their interest is already in Adjusted EBITDA |

### Coverage

| Measure | Formula | Inputs | Result |
| --- | --- | --- | --- |
| Interest expense on non-funding debt, LTM Q2 2026 | 214,513 + 157,537 - 100,855 | | 271,195 |
| Same, LTM Q1 2026 | 214,513 + 70,727 - 50,081 | | 235,159 |
| Adjusted EBITDA / interest expense on non-funding debt | | 697,336 / 214,513; 800,442 / 235,159; 790,638 / 271,195 | 3.25x; 3.40x; 2.92x |
| Cash paid for interest, LTM Q2 2026 | 496,248 + 288,971 - 233,534 | | 551,685 |
| Cash paid for interest, LTM Q1 2026 | 496,248 + 145,972 - 84,784 | | 557,436 |

### Earnings quality

| Measure | Formula | Inputs | Result |
| --- | --- | --- | --- |
| LTM net income (loss) | 244,023 + (-281,528) - 67,451 | | (104,956) (105.0 million) |
| MSR valuation change and derivative result excluded from Adjusted EBITDA, H1 2026 | MSR input-driven gain + derivative loss | 312,953 - 741,389 | (428,436) |
| Same, Q2 2026 | 65,056 - 603,191 | | (538,135) |
| Same, FY2025 | -435,267 + 298,126 | | (137,141) |
| Same, H1 2025 | -247,667 + 208,904 | | (38,763) |
| Same, LTM Q2 2026 | FY2025 + H1 2026 - H1 2025 | (137,141) + (428,436) - (38,763) | (526,814) (526.8 million) |
| Q2 2026 net loss less Adjusted EBITDA | 185,879 - (-451,902) | | 637,781 |
| Share of that gap that is the derivative loss added back | | 603,191 of 637,781 | 603,191 |

### Cash flow

| Measure | Formula | Inputs | Result |
| --- | --- | --- | --- |
| Operating cash flow plus net MSR sale proceeds, H1 2026 | -1,885,842 + 801,013 | | (1,084,829) (1,084.8 million) |
| Same, H1 2025 | 328,022 + 1,591,780 | | 1,919,802 |
| Same, FY2025 | -2,647,557 + 2,423,711 | | (223,846) |
| Same, Q1 2026 | -2,229,879 + 542,626 | | (1,687,253) |
| Same, Q2 2026 | 344,037 + 258,387 | | 602,424 |
| Same, LTM Q2 2026 | (-223,846) + (-1,084,829) - 1,919,802 | | (3,228,477) |
| Operating cash flow, Q2 2026 | H1 less Q1: -1,885,842 - (-2,229,879) | | 344,037 |
| Cash returned to equity holders, H1 2026 | 59,867 + 261,896 | | 321,763 (321.8 million) |
| Cash returned to equity holders, H1 2025 | 34,569 + 343,589 | | 378,158 |
| Bridge of H1 2026 operating cash flow | -281,528 + 13,017 - 2,142,855 + 133,018 + 29,842 + 25,656 + 861 + 313,653 - 46,034 - 19,858 + 6,992 + 81,394 | | (1,885,842), equal to the statement |

### Liquidity at June 30, 2026

| Component | Formula | Inputs | Result |
| --- | --- | --- | --- |
| Unrestricted cash | 498,407 - 21,000 | | 477,407 |
| Conventional MSR facility undrawn | 2,000,000 - 1,875,000 | | 125,000 |
| Ginnie Mae MSR facility undrawn | 1,250,000 - 1,075,000 | | 175,000 |
| Revolving Credit Facility undrawn | 500,000 - 0 | | 500,000 |
| Total on this basis | 477,407 + 125,000 + 175,000 + 500,000 | | 1,277,407 (1,277.4 million) |
| Company basis (cash including restricted) | 498,407 + 800,000 | | 1,298,407 (1,298.4 million), consistent with the printed "approximately $1.3 billion" |
| Letters of credit drawn on these facilities | | No letters of credit found in the sources (searched for letters of credit and standby) | Not applicable; nothing deducted |
| Facilities expiring within twelve months of June 30, 2026 | 2027 senior notes June 15, 2027 | 500,000 of principal | Within twelve months; the Conventional MSR facility (July 15, 2027) falls just outside; the revolver renews annually; warehouse lines expiring by June 15, 2027 carry 5,090,756 advanced |

### Other

| Measure | Formula | Inputs | Result |
| --- | --- | --- | --- |
| Servicing-rights fair value over UPB serviced | 5,311,465 / 247,648,881; 4,073,781 / 240,813,979 | | 2.14%; 1.69% |
| Secured lines over servicing-rights fair value | 2,950,000 / 5,311,465 | | 55.5% (all servicing rights, not only pledged collateral) |
| Total equity change | 985,308 - 1,593,629 | | (608,321), equal to net loss (281,528), dividends declared (65,589), member distributions declared (255,922), stock compensation 27,086 and re-measurement (32,368) |
| Warehouse lines expiring on or before May 14, 2027 | 990,038 + 153,287 + 256,929 + 963,193 + 506,673 + 1,314,608 + 661,696 + 244,332 | | 5,090,756 (59.2% of 8,600,078) |
| Senior note fair value change | 2,783,429 - 3,005,945 | | (222,516) |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Covenant levels, definitions and the headroom for the warehouse and servicing-rights facilities are Not supplied; only compliance statements are printed | High | CP-2 | Supply the facility agreements and any compliance certificates |
| Indenture definitions of Fixed Charge Coverage Ratio and Debt-to-Equity Ratio are Not supplied, so the incurrence tests cannot be computed | High | CP-2 | Supply the four indentures |
| The August 5, 2026 preferred stock and warrant transaction is not in the statements; use of proceeds, fees, classification and any pro forma leverage are Not calculable | High | CP-1A, CP-2 | Supply the 8-K and Certificate of Designation, and the third quarter 2026 report if filed |
| Cash interest on non-funding debt is not reported separately; coverage is on an accrual basis | Medium | CP-2 | Treat the cover figures as proxies |
| Adjusted EBITDA is company-defined, unaudited for 2026 and adds back large derivative and valuation items | Medium | CP-2, CP-5 | Use alongside net income and cash flow |
| Availability under the servicing-rights facilities depends on advance rates and collateral value and the facilities are uncommitted; the revolver's commitment status is not stated | Medium | CP-2 | Supply the agreements |
| Warehouse line renewals after expiry dates of September 29 and October 8, 2026 are Not supplied | Medium | CP-2 | Supply later filings |
| Facility limits rose from 1.5 billion to 2.0 billion (Conventional, by reallocating a shared limit) and from 900.0 million to 1.25 billion (Ginnie Mae) between March 31 and June 30, 2026 without a described amendment | Low | CP-2 | Supply the amendments |
| Q1 10-Q prints restricted cash of 16.0 million for December 31, 2025, while the 10-K and Q2 10-Q print 21.0 million; 21.0 million is used throughout and restricted cash is rounded to 0.1 million | Low | CP-1 | None needed beyond this note |
| February 2026 presentation shows FY2024 Adjusted EBITDA of 459,973 and interest on non-funding debt of 148,619 against 459,975 and 148,620 in the 10-K; the 10-K controls | Low | CP-1, CP-5 | None needed |
| Two Harbors termination fee amount and date are Not supplied; its effect is netted inside Q1 2026 acquisition-related expenses (9,622 credit) | Low | CP-1A | Supply the termination 8-K |
| Quarterly Q3 2025 and Q4 2025 cash flows are not built; only statements and Adjusted EBITDA are quarterly | Low | CP-1 | Derive from the Q3 2025 10-Q if a quarterly cash view is needed |
| Q3 2026 and later results are Not supplied | Medium | CP-1, CP-2 | Supply the Form 10-Q for September 30, 2026 if filed |

## Next module

CP-1A, then CP-2 and CP-5. Carry forward: the two-part debt stack (warehouse lines of 8,600.1 million separate from non-funding debt of 6,040.4 million); leverage of 7.64x on LTM Adjusted EBITDA of 790.6 million and 6.13x on equity; the gap between Adjusted EBITDA and net loss caused by derivative and servicing-rights valuation items; negative operating cash flow funded by servicing-rights borrowing; 800.0 million of undrawn lines of which 300.0 million is uncommitted; the 2027 maturities and warehouse expiries; and the unreflected August 5, 2026 preferred transaction.
