## Request

Issuer: COLUMBUS MCKINNON CORP (issuer id cmco; reporting entity Columbus McKinnon Corporation, consolidated). As-of date and cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. The filings print amounts in US$ thousands and the earnings releases in US$ thousands or US$ millions; this handoff keeps US$ thousands in tables of reported figures and uses US$ millions only in the four chart tables where the selector requires it. Fiscal year ends March 31. Context periods: current period q2-2027 (quarter ended September 30, 2026, "Q2 FY2027") and prior period fy-2026 (year ended March 31, 2026, "FY2026"). Other labels used: H1 FY2027 (six months ended September 30, 2026), H1 FY2026 (six months ended September 30, 2025), Q1 FY2027 (quarter ended June 30, 2026), LTM (twelve months, always stated with its end date).

Task: CP-1 financial base. Build the reported financial base, capital structure, liquidity, covenant picture, claims outside debt and credit metrics, kept separate from calculations, with every period and perimeter labelled, and carry forward the limitations in the accepted source-readiness handoff. No credit rating, valuation or investment opinion is given here. Everything comes from the pinned sources below; nothing is taken from outside them and nothing is dated after 2026-11-05.

Perimeter note. The annual report FY2026 contains approximately two months of Kito Crosby (acquired February 3, 2026) and excludes approximately one month of the divested U.S. power chain hoist and chain operations (sold March 4, 2026). The H1 FY2027 figures contain Kito Crosby for the full six months and no divested business. All FY2025 and H1 FY2026 figures are pre-acquisition legacy results with the divested business included. Year-on-year changes therefore mix perimeters and are not like-for-like.

## Sources

### Issuer sources relied on

Locator key used in this handoff: "10-K" = annual report; "10-Q Dec25", "10-Q Jun26", "10-Q Sep26" = quarterly reports; "EX Jun04", "EX Jul30", "EX Nov03" = earnings releases (Exhibit 99.1). A locator `p:N` is the extraction page chunk, not the printed page.

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2026-03-31_cmco-20260331.htm.jsonl | 6c5bc84510574e2ec737bd05ee1fd8a3711e8a18e3afa84ac93b9ca09421f3b2 | Audited FY2026, FY2025 and FY2024 statements, debt, lease and pension notes (10-K) |
| 10-Q_2025-12-31_cmco-20251231.htm.jsonl | 768e09ab99d2d57b573c1d7e611dcf23d35114d9f599e779b33b981ef5e2e322 | Pre-acquisition facility and covenant description (10-Q Dec25) |
| 10-Q_2026-06-30_cmco-20260630.htm.jsonl | 848d4b1e6de7319613096e948145f873979b72374e1b0adf1266c7e707ed74ea | June 30, 2026 debt and cash flow data (10-Q Jun26) |
| 10-Q_2026-09-30_cmco-20260930.htm.jsonl | b3c5294b4e11dbda4ecee230ea30aa7939709362043cb1c68987937b3770044b | Current-period statements and notes (10-Q Sep26) |
| EX-99.1_2026-06-04_exhibit9913312026.htm.jsonl | 8fe0fb89665018b65928f2f5ad1f43cd441cafa6d1887e5ab7c1c193c08194ed | Q4 and FY2026 non-GAAP reconciliations (EX Jun04) |
| EX-99.1_2026-07-30_exhibit99107302026.htm.jsonl | 79d10e65644259bd7729bae3526568d114dc088282b163dea033ec227104fc0f | Q1 FY2027 non-GAAP reconciliations and Credit Agreement leverage at June 30, 2026 (EX Jul30) |
| EX-99.1_2026-11-03_exhibit9911132026.htm.jsonl | b37aa7a41882d117efc3cc33b70d5e18769d1bc6e6c1fb21bd10142444e39a78 | Q2 FY2027 non-GAAP reconciliations and guidance (EX Nov03) |

Run context (not issuer evidence): `context` sha256 6575122c1a10165e3e05cc3e66f366997e6fa4e2f6aa905298c07efcd7fba897. The context supplies the currency and period labels only; its blank fields (ratings, quotes, valuation, sponsor, parent) are not zero.

### Supplied handoffs

| Module | sha256 | File |
| --- | --- | --- |
| CP-0 | 71552fd03efd6c5e5b66da0cd6a9d8406b63ba87e5d16dbdb19f29c7ec519f40 | runs/cpos-swarm-20261105-cmco/requests/CP-0/0d6f93d72ccc111ac036b9e7997743de9c75735a5a8c69774628c402bf1d247a/1.response.md |

What was taken from the CP-0 handoff: its readiness view (READY_WITH_LIMITATIONS), conflicts C1 (revolver maturity), C2 (sponsor ownership percentage) and C4 (maturity table total), and gaps G1 (executed credit documents not supplied), G3 (discrete quarters), G4 (pre-close Kito Crosby statements) and G5 (no ratings or market data). Each is applied below at the figure it affects. This handoff resolves one open point left in CP-0, by arithmetic and not by any source statement: CP-0 left unexplained what the C4 maturity-table total includes; the instrument arithmetic below shows it.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Leverage is high after the Kito Crosby deal but easing on the lender-defined measure. Reported earnings still carry large deal costs, interest cover is thin, and liquidity is adequate with no large near-term maturities. | Medium | Covenant levels, trigger and the lender-defined earnings build rest on summaries and management adjustments, not executed documents. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt rose in the first half of fiscal 2027 even though the lender-defined net leverage ratio fell from 5.1x to 4.9x. | Deleveraging so far comes from the earnings base and pro forma adjustments, not debt repayment. | High |
| Cash interest paid for the first half of fiscal 2027 was 90,921 against adjusted EBITDA of 222,648. | Cover on a like-for-like six-month basis is thin; floating-rate exposure is partly hedged. | High |
| Liquidity was 531,980 at September 30, 2026, all revolver availability plus cash, with no receivables facility capacity left. | Adequate near-term runway, but the receivables facility needed a waiver and was amended again in late October 2026. | Medium |
| Lender-defined EBITDA of 467,796 includes a large pro forma and synergy add-back, and reported net loss remains large. | Reported leverage is more favourable than a reported-earnings basis, which is far higher. | High |
| Maturities are back-ended: the next 12 months involve about 150,000 of planned paydown, then the term loan and notes fall due in 2033. | No large maturity is scheduled before the receivables facility in 2028, but the revolver date is in conflict and the paydown plan depends on cash generation. | Medium |

### Financial base view

The financial base is usable but must be read in two layers. Reported (GAAP) layer: the business more than doubled in size on the Kito Crosby close (H1 FY2027 net sales 1,070,746 against 496,967 in H1 FY2026), but it is loss-making after amortization, interest and deal costs (H1 FY2027 net loss attributable to the Company 114,262; FY2026 net loss 229,535 including a 200,000 goodwill impairment), operating cash flow is small (H1 FY2027 21,065) and FY2026 operating cash flow was negative (146,211), reflecting acquisition and divestiture related cash payments. Lender-defined layer: the Credit Agreement Trailing Twelve Month Adjusted EBITDA of 467,796 at September 30, 2026 normalises a full year of Kito Crosby, the divestiture and cost synergies, and gives a Credit Agreement Net Leverage Ratio of 4.9x. The first layer is audited or filed; the second is a management reconciliation of a defined credit agreement term and is supporting evidence only. Debt is 2,412,308 (carrying value, including finance lease and the receivables facility) at September 30, 2026, up from 2,393,007 at March 31, 2026. About 1,551,465 of principal is floating rate against 965,000 of interest rate swap notional, so roughly 586,465 is unhedged on the figures supplied. Liquidity is 531,980 with the revolver commitment (500,000) the only meaningful undrawn source. The covenant package (first lien leverage test, maximum 7.75x stepping down) looks roomy against the 4.9x total net measure on an indicative reading, but trigger, step-down dates and exact definition are not supplied, so headroom is not calculable. Confidence in the base is Medium: the filed statements are internally consistent (debt carrying value ties to principal less unamortized costs; the lender-defined EBITDA reconciles line by line), while the credit documents, discrete Q4 FY2026 statements and any ratings are absent.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (March 31, 2025) | 3.00 | 2.66 | x | Total debt 470,975 (carrying, includes AR securitization and finance lease) over company-reported Adjusted EBITDA 156,751; net debt = total debt less cash 53,683. Legacy pre-acquisition perimeter; Credit Agreement EBITDA for this date is Not supplied. |
| FY2026 (March 31, 2026) | 5.43 | 5.21 | x | Total debt 2,393,007 over Credit Agreement TTM Adjusted EBITDA 441,030, which is pro forma for a full year of Kito Crosby, the divestiture and assumed synergies (management reconciliation). Net debt = total debt less cash 96,562. Company-reported Credit Agreement Net Leverage Ratio 5.1x uses a different net debt (adds letters of credit, deducts AR facility). |
| Q1 FY2027 (June 30, 2026) | 5.16 | 4.94 | x | Total debt 2,376,783 over Credit Agreement TTM Adjusted EBITDA 460,917 (pro forma, management reconciliation); net debt = total debt less cash 98,410. Company-reported ratio 4.9x. |
| Q2 FY2027 (September 30, 2026) | 5.16 | 4.92 | x | Total debt 2,412,308 over Credit Agreement TTM Adjusted EBITDA 467,796 (pro forma, management reconciliation); net debt = total debt less cash 110,900. Company-reported ratio 4.9x. On company-reported Adjusted EBITDA with no pro forma (LTM 331,193) the same total debt gives 7.28x and net 6.95x. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 5.22 | x | Company-reported Adjusted EBITDA 156,751 over interest paid 30,054 (cash-flow supplementary data). Legacy pre-acquisition structure. |
| FY2026 | 3.97 | x | Company-reported Adjusted EBITDA 181,373 over interest paid 45,630. Overstates the run rate: EBITDA includes approximately two months of Kito Crosby, but the new debt was outstanding only from late January and early February 2026 and the first notes coupon was paid August 1, 2026, so no notes coupon is in this figure. |
| H1 FY2026 | 4.52 | x | Six months to September 30, 2025: Adjusted EBITDA 72,828 over interest paid 16,114. Legacy pre-acquisition structure; comparable length to the next row. |
| H1 FY2027 | 2.45 | x | Six months to September 30, 2026: Adjusted EBITDA 222,648 over interest paid 90,921. Includes one semi-annual notes coupon (paid August 1, 2026); a full year has two, so annual cash interest is not simply twice this half. Company-reported Adjusted EBITDA, not pro forma. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| March 31, 2025 | 53.683 | 159.583 | US$m | Cash and cash equivalents (balance sheet; excludes 0.250 restricted cash). Undrawn = 2024 revolver availability net of standby letters of credit 15.417; availability of the AR securitization facility at this date is Not supplied in the pack. |
| March 31, 2026 | 96.562 | 464.654 | US$m | Undrawn = 2026 revolver availability 458.933 (commitment 500.000 less borrowings 25.000 less letters of credit 16.067) plus AR securitization availability 5.721. Matches company-stated liquidity of 561.216. |
| June 30, 2026 | 98.410 | 468.738 | US$m | Undrawn = revolver availability 468.738 (500.000 less borrowings 12.844 less letters of credit 18.418); AR facility availability nil per the Q1 release. Company-stated liquidity 567.1. |
| September 30, 2026 | 110.900 | 421.080 | US$m | Undrawn = revolver availability 421.080 (500.000 less borrowings 59.644 less letters of credit 19.276); no capacity under the AR securitization facility. Company-stated liquidity 531.980. Excludes unsecured uncommitted non-U.S. lines. Cash includes 108.440 held by foreign subsidiaries. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2027 (to March 31, 2027) | 17.981 | US$m | Principal payments scheduled as of March 31, 2026 in the 10-K table. Consistent with term loan amortization 12.375 plus other debt 5.606 maturing December 31, 2026 (derived). Excludes the voluntary paydown of about 160.000 the company planned for the following 12 months. |
| FY2028 | 16.500 | US$m | 10-K table; consistent with term loan amortization only. |
| FY2029 | 69.900 | US$m | 10-K table; consistent with term loan amortization 16.500 plus the AR securitization facility 53.400 due August 11, 2028 (derived). |
| FY2030 | 16.500 | US$m | 10-K table; term loan amortization only. |
| FY2031 and later | 2320.115 | US$m | 10-K table "Thereafter"; consistent with the remaining term loan, the 900.000 notes due February 1, 2033 and the 25.000 revolver borrowing (due 2031 or 2028 per conflicting dates) (derived). Whole table total 2440.996 excludes the finance lease of 11.549 and is at March 31, 2026 principal; September 30, 2026 principal by year is Not supplied. |

### Financials and credit metrics

Figures are US$ thousands unless the row says otherwise. "Adjusted EBITDA" is the company-reported non-GAAP measure (not pro forma). Balance rows are at the period end of the column (March 31, 2025; March 31, 2026; September 30, 2025; September 30, 2026). Derived cells are marked "(derived)" and shown in Calculations.

| Metric | FY2025 | FY2026 | H1 FY2026 | H1 FY2027 | Q2 FY2027 (three months) | Locators |
| --- | --- | --- | --- | --- | --- | --- |
| Net sales | 963,027 | 1,193,451 | 496,967 | 1,070,746 | 539,285 | 10-K p:75; 10-Q Sep26 p:5 |
| Gross profit | 325,680 | 359,431 | 167,382 | 334,178 | 187,909 | 10-K p:75; 10-Q Sep26 p:5 |
| Income (loss) from operations | 54,573 | (119,333) | 17,680 | 17,346 | 35,043 | 10-K p:75; 10-Q Sep26 p:5 |
| Interest and debt expense | 32,426 | 61,145 | 17,445 | 95,660 | 48,050 | 10-K p:75; 10-Q Sep26 p:5 |
| Net income (loss) attributable to the Company | (5,138) | (229,535) | 2,697 | (114,262) | (25,533) | 10-K p:75; 10-Q Sep26 p:5 |
| Adjusted EBITDA (company, not pro forma) | 156,751 | 181,373 | 72,828 | 222,648 | 111,205 | EX Jun04 p:14; EX Nov03 p:13 |
| Adjusted EBITDA margin | 16.3% | 15.2% | 14.7% | 20.8% | 20.6% | EX Jun04 p:14; EX Nov03 p:13 |
| Depreciation and amortization | 48,187 | 77,038 | 24,485 | 104,138 | Not supplied (discrete quarter) | 10-K p:77; 10-Q Sep26 p:7 |
| Net cash from operating activities | 45,612 | (146,211) | 248 | 21,065 | (4,559) | 10-K p:77; 10-Q Sep26 p:7; EX Nov03 p:13 |
| Capital expenditures | 21,411 | 17,859 | 6,523 | 16,464 | 10,796 | 10-K p:77; EX Nov03 p:13 |
| Free cash flow (operating cash flow less capex) | 24,201 | (164,070) | (6,275) | 4,601 | (15,355) | EX Jun04 p:14; EX Nov03 p:13 |
| Interest paid (cash) | 30,054 | 45,630 | 16,114 | 90,921 | 61,389 (derived) | 10-K p:78; 10-Q Sep26 p:8 |
| Income taxes paid, net | 20,520 | 45,850 | 12,143 | 25,589 | 11,681 (derived) | 10-K p:78; 10-Q Sep26 p:8; 10-Q Jun26 p:7 |
| Cash and cash equivalents | 53,683 | 96,562 | 28,039 (derived: 28,289 cash, cash equivalents and restricted cash less 250 restricted) | 110,900 | 110,900 | 10-K p:74; 10-Q Sep26 p:4, p:8 |
| Total debt (carrying; includes AR facility and finance lease) | 470,975 (derived) | 2,393,007 | Not supplied (September 30, 2025 debt balances not in pack) | 2,412,308 | 2,412,308 | 10-K p:74; EX Nov03 p:14; 10-Q Sep26 p:5 |
| Net debt (total debt less cash) | 417,292 (derived) | 2,296,445 (derived) | Not supplied (no debt balance) | 2,301,408 (derived) | 2,301,408 (derived) | Derived from rows above |
| Credit Agreement TTM Adjusted EBITDA (pro forma) | Not supplied | 441,030 | Not supplied | 467,796 | 467,796 | EX Nov03 p:14 |
| Credit Agreement Net Leverage Ratio (company) | Not supplied | 5.1x | Not supplied | 4.9x | 4.9x | EX Nov03 p:14 |
| Total debt / Credit Agreement EBITDA (derived) | Not supplied | 5.43x | Not supplied | 5.16x | 5.16x | Derived |
| Total shareholders' equity (includes preferred) | 882,095 | 1,448,629 | 914,588 | 1,337,922 | 1,337,922 | 10-K p:75; 10-Q Sep26 p:5, p:7 |

### Debt structure at September 30, 2026 (principal and terms as the notes print them)

All instruments are issued or borrowed by Columbus McKinnon Corporation as Borrower or issuer; Columbus McKinnon EMEA GmbH is a party to the First Amendment to the credit agreement alongside the Company and certain subsidiary guarantors ([10-Q Sep26 p:27]). Guarantor lists are Not supplied. Security: the notes are titled "senior secured" and the term loan is described as a "senior secured term loan credit facility" ([10-Q Sep26 p:28]); the collateral package and relative ranking of notes and term loan are Not supplied in the pack.

| Instrument | Principal / drawn (US$ thousands) | Rate | Maturity | Notes and locator |
| --- | --- | --- | --- | --- |
| 7.125% senior secured notes | 900,000 | 7.125% fixed, semi-annual (February 1, August 1) | February 1, 2033 | Issued January 30, 2026; first coupon paid August 1, 2026; callable from February 1, 2029 at stated prices, 101.0% change of control put [10-Q Sep26 p:27; 10-K p:110-111] |
| 2026 Term Loan B | 1,449,233 (1,406,577 net of 42,656 unamortized discount and costs) | Term SOFR plus 3.00% after the September 21, 2026 amendment (margin cut by 50 bps); 10-K stated a 0.50% SOFR floor | February 3, 2033 | Original 1,650,000; prepaid 193,010 with divestiture proceeds March 4, 2026; quarterly amortization 0.25%; obligation of 14,529 over the next 12 months plus excess cash flow [10-Q Sep26 p:28] |
| 2026 Revolving Credit Facility | 59,644 drawn (US$ 38,461 plus EUR 18,700) of 500,000; letters of credit 19,276 | Term SOFR plus 1.75% to 2.75% by Consolidated Total Leverage Ratio | February 3, 2031 per the latest filing; 2028 in two earlier statements (conflict C1) | Availability 421,080 [10-Q Sep26 p:29] |
| AR Securitization Facility | 42,588 | One-month SOFR plus 1.10% | August 11, 2028 | Maximum 60,000 subject to borrowing base; secured by U.S. receivables of 93,652; covenant waiver at September 30, 2026; amended again October 29, 2026 [10-Q Sep26 p:27, p:30] |
| Other debt | 5,183 | 2.7% | December 31, 2026 | Secured building loan assumed with Kito Crosby; fully current [10-Q Sep26 p:30] |
| Finance lease (Hartland, WI) | 11,132 | 4.51% weighted-average discount rate (March 31, 2026) | Terminates 2035 | 851 current [10-Q Sep26 p:30; 10-K p:148] |
| Non-U.S. unsecured uncommitted lines | 566 drawn of about 5,438 | Not supplied | Uncommitted | Not part of the tie below; bank guarantee lines of 22,694 with 18,757 used [10-Q Sep26 p:31] |

Tie to the balance sheet (derived): principal of the first six rows is 2,467,780; less unamortized discount and issuance costs of 55,472 (term loan 42,656, notes 12,642 net, AR facility 174) equals 2,412,308, which is the current portion 150,000 plus the long-term line 2,262,308 on the balance sheet [10-Q Sep26 p:5]. The same tie at March 31, 2026 gives 2,393,007.

Interest rate exposure: eleven interest rate swaps with aggregate notional 965,000, maturities March 31, 2027 to March 31, 2031 [10-Q Sep26 p:25]. Floating-rate principal (term loan, revolver and AR facility) is 1,551,465 (derived); unhedged floating exposure is therefore about 586,465, and the swaps' fixed rates are Not supplied. The swaps that mature in 2027 reduce the hedged amount before the debt does.

### Liquidity by facility

| Facility | Commitment | Drawn | Letters of credit | Undrawn | Expiry / note |
| --- | --- | --- | --- | --- | --- |
| 2026 Revolving Credit Facility, September 30, 2026 | 500,000 | 59,644 | 19,276 | 421,080 | 2031 (2028 conflict C1) [10-Q Sep26 p:29] |
| AR Securitization Facility, September 30, 2026 | 60,000 maximum, borrowing base limited | 42,588 | not applicable | 0 stated ("no additional capacity") | August 11, 2028 [10-Q Sep26 p:30, p:55] |
| Cash and cash equivalents, September 30, 2026 | not applicable | not applicable | not applicable | 110,900 | 108,440 held by foreign subsidiaries; management states no material restrictions on access [10-Q Sep26 p:56] |
| Total liquidity as stated by the company, September 30, 2026 | not applicable | not applicable | not applicable | 531,980 | 110,900 plus 421,080 [10-Q Sep26 p:55] |

No committed facility expires within twelve months of September 30, 2026. The only debt maturing inside twelve months is other debt of 5,183 (December 31, 2026) and the amortization and planned paydown in the current portion of 150,000. Revolver borrowings of 59,644 comprise 38,461 in US dollars and EUR 18,700 in euros, up from 25,000 at March 31, 2026; net borrowing in the six months was 15,443 ([10-Q Sep26 p:8]) while cash and cash equivalents rose by 14,338 (110,900 less 96,562, derived), so the cash build was funded by borrowing.

### Covenants and compliance

| Test or term | Level | Reported figure | Headroom |
| --- | --- | --- | --- |
| Consolidated First Lien Leverage Ratio, 2026 Credit Agreement (financial maintenance covenant) | Maximum 7.75 to 1.00 as of any date of determination, "with step-downs for the first three years to 7.25 to 1.00, 6.75 to 1.00 and 6.25 to 1.00" [10-K p:113] | Not supplied: the first lien ratio is not printed. Reported Credit Agreement Net Leverage Ratio is 4.9x at September 30, 2026 [EX Nov03 p:14], which counts all debt net of cash and so is a different, broader measure | Not calculable: step-down dates, whether the test applies at all times or only above a revolver-usage threshold, and the first lien definition are not supplied. The superseded facility's 30.0% usage trigger [10-Q Dec25 p:25] is not evidence for the 2026 revolver |
| Indenture covenants (liens, indebtedness, mergers, additional guarantors) | Incurrence-type; most suspended if rated investment grade by either agency [10-K p:113] | No ratio test printed | Not applicable; no maintenance test |
| AR Securitization Facility delinquency and default ratios | Levels Not supplied | "in compliance ... after receiving a waiver ... effective September 30, 2026"; amended again October 29, 2026 | Not calculable; the need for a waiver implies the ratios were at or beyond a trigger on that date, but the levels are not supplied |
| Compliance statement | Not applicable | "As of September 30, 2026, the Company was in compliance with its covenants under the 2026 Revolving Credit Facility and Senior Secured Notes." [10-Q Sep26 p:27] | Compliance is management-stated only |

The definition of Credit Agreement TTM Adjusted EBITDA differs from the company-reported Adjusted EBITDA: it is normalized to include a full year of Kito Crosby and the divestiture and assumes all cost synergies are achieved in fiscal 2026 ([EX Nov03 p:15] "EBITDA is normalized to include a full year of performance from Kito Crosby and Divestiture and assumes all cost synergies are achieved in fiscal 2026."). Credit Agreement Net Debt adds standby letters of credit and deducts cash and AR facility obligations ([EX Nov03 p:15]), so it also differs from the simple net debt in the chart tables.

### Claims outside the debt figure

| Claim | Amount | Inside the 2,412,308 debt figure? | Locator and limit |
| --- | --- | --- | --- |
| Operating lease liabilities | 95,718 at March 31, 2026 (31,523 current, 64,195 non-current); cash paid H1 FY2027 12,272 | No (finance lease 11,132 is inside) | [10-K p:148; 10-Q Sep26 p:47]; September 30, 2026 balance Not supplied |
| Pension plans, funded status | (78,251) at March 31, 2026 (obligation 201,021; assets 122,770); planned contribution 7,341 in fiscal 2027; a U.S. plan was settled after September 30, 2026 | No | [10-K p:119; 10-Q Sep26 p:31]; September 30, 2026 funded status and the settlement amount are Not supplied |
| Series A convertible participating preferred shares (CD&R Investor) | Carrying 818,403 within equity at September 30, 2026; 800,000 shares sold for an aggregate purchase price of $800,000,000; 7% payable in cash or in kind; conversion price $37.68; dividends in kind increased conversion value by 28,558 through September 30, 2026 | No (equity classified) | [10-Q Sep26 p:5, p:33]; redemption, ranking and liquidation preference terms are Not supplied; the annual report names "optional redemption rights" without terms [10-K p:50] |
| General and product liability reserves | 31,874 gross, less estimated insurance recoveries 19,735, net 12,139 at September 30, 2026 | No | [10-Q Sep26 p:34] |
| Asbestos liabilities (legacy Columbus McKinnon and Magnetek) | Estimated liability net of insurance recoveries approximates 4,924; a receivable of 5,821 for insurance cost sharing is recorded in other assets and offsets the reserve | No | [10-Q Sep26 p:35] |
| Final purchase price working capital payment | 10,000, accrued at September 30, 2026 and paid after the quarter | No | [10-Q Sep26 p:9]; a cash outflow in Q3 FY2027 |
| Letters of credit and bank guarantees | 19,276 standby letters of credit on the revolver (reduce availability); 18,757 bank guarantees used | Letters of credit are deducted from availability; guarantees are not debt | [10-Q Sep26 p:29, p:31] |
| Purchase commitments, factoring, supply-chain finance | Not supplied. Searches of all seven sources found no factoring or supply-chain finance programme and no quantified purchase commitment table (the annual report mentions non-cancellable purchase commitments only qualitatively [10-K p:28]) | Not applicable | Not supplied: no amount is printed |
| Litigation or consent-decree funding | No material pending proceedings stated beyond routine litigation; Magnetek indemnification matters (Italian tax, Monsanto, Fruit of the Loom environmental) described without quantified exposure in the pages read | No | [10-Q Sep26 p:33-43]; quantified exposure Not supplied |

### Earnings quality and definitions

The Credit Agreement TTM Adjusted EBITDA reconciliation at September 30, 2026 starts from a net loss of (345,759) and adds back, among other items, the annualization of Kito Crosby, the divestiture and synergies of 132,389, goodwill impairment of 200,000, acquisition inventory step-up of 99,441, transaction-related costs of 39,889, acquisition integration costs of 37,563, cost of debt repricing of 25,241, offset by a net gain on sale of business of (102,153) ([EX Nov03 p:14]). The components sum to 467,796 (checked in Calculations). The pro forma and synergy add-back is 28.3% of the lender-defined figure, and the four acquisition-related items together are 66.1% of it (derived). The difference between the lender-defined figure and company-reported LTM Adjusted EBITDA of 331,193 (derived) is 136,603, which management attributes to normalizing for a full year of Kito Crosby, the divestiture and synergies; it is a management estimate, not a reported result. Adjusted EBITDA also adds back stock-based compensation, which is a cost.

Company-reported Adjusted EBITDA for H1 FY2027 is 222,648 in the Q2 release. The Q1 release stated Q1 FY2027 Adjusted EBITDA of 111,464 ([EX Jul30 p:10]) and the Q2 release states Q2 FY2027 of 111,205 ([EX Nov03 p:13]), which sum to 222,669, 21 more than the H1 figure printed; the Q1 figure appears to have been revised by 21 in the later release, without a stated reason (Not supplied).

Reported gross margin (34.8% in Q2 FY2027 per [EX Nov03 p:3], 27.5% in Q1 FY2027 per [EX Jul30 p:2]) is depressed by inventory step-up amortization (acquisition inventory amortization 7,445 in Q2 and 62,643 for the six months, [10-Q Sep26 p:10]); the step-up is a non-cash, non-recurring accounting effect that unwinds as acquired inventory is sold, so gross margin should improve mechanically as it fades.

### Latest quarter and events after quarter end

- Q2 FY2027 (three months to September 30, 2026): net sales 539,285 versus 261,047 (up 106.6%), of which Kito Crosby 300,204 ([10-Q Sep26 p:10]); legacy net sales growth of 5.3% (management Legacy CMCO measure, [EX Nov03 p:13-14]); income from operations 35,043; interest and debt expense 48,050; cost of debt repricing 1,056; pre-tax loss (9,877) with income tax expense of 15,315; net loss attributable to the Company (25,533); acquisition integration and deal expenses 12,465 ([10-Q Sep26 p:5, p:10]). Operating cash flow was negative for the quarter at (4,559), with capital expenditures of 10,796 and free cash flow of (15,355) ([EX Nov03 p:13]).
- Financing events: First Amendment to the 2026 Credit Agreement on September 21, 2026 reduced the term loan and revolver margin by 50 bps; costs of 1,056 and a 279 lender fee ([10-Q Sep26 p:27, p:29]). AR securitization covenant waiver effective September 30, 2026 and amendment on October 29, 2026 (subsequent event, new ratio levels Not supplied).
- Other subsequent events: dividend of $0.07 per common share declared October 26, 2026 (about 2,030, payable November 16, 2026, [10-Q Sep26 p:33]); settlement of a U.S. pension plan after September 30, 2026 ([10-Q Sep26 p:31]); payment of the 10,000 working capital adjustment. Management raised FY2027 guidance on November 3, 2026 to net sales of $2.13 billion to $2.17 billion and Adjusted EBITDA of $425 million to $440 million, with interest expense of $185 million to $190 million and capital expenditures of $45 million to $55 million ([EX Nov03 p:3-4]); this is forward-looking management language.
- Nothing dated after the cutoff 2026-11-05 is used.

### Conflicts, corrections and unresolved differences

- C1 revolver maturity (from CP-0): the latest quarterly report and the second annual paragraph say February 3, 2031 ([10-Q Sep26 p:28]; [10-K p:112]); the first annual paragraph and the June 2026 quarterly report say February 3, 2028 ([10-K p:111]; [10-Q Jun26 p:24]). Both are logged; the 2031 date is used in the tables above because it is the only date in the latest report and appears in the operative revolver paragraph of each report, and the executed agreement is not supplied. The 10-K's own maturity table places no revolver amount in FY2028 (the FY2028 row of 16,500 equals term loan amortization), which fits 2031 (derived). If 2028 were correct the undrawn 421,080 would expire in about 15 months and the 59,644 drawn would fall due then; that would change the maturity wall and the liquidity runway.
- C2 sponsor ownership: approximately 42% in the December 2025 report and 43% in the 2026 reports; not a financial figure and not reconciled here.
- C4 maturity table (from CP-0, extended here): the 10-K table total of 2,440,996 equals the sum of the term loan 1,456,990, notes 900,000, AR facility 53,400, revolver borrowings 25,000 and other debt 5,606 (derived). The sentence introducing the table names three instruments; the arithmetic shows five are included. The finance lease (11,549) is excluded. This is an inference from exact arithmetic, not a source statement.
- Planned paydown versus balance sheet: the notes say about 150,000 of borrowings will be repaid within 12 months and that amount is recorded in current portion, while the balance sheet current portion line is also 150,000 and the same note also states 5,183 of other debt and 851 of finance lease as current. The pack does not show how these reconcile (Not supplied); the 150,000 current portion is used as printed.
- Q1 FY2027 Adjusted EBITDA revised by 21 in the Q2 release (above).
- The 10-K describes the superseded first lien facilities' 3.50x total leverage covenant with a usage trigger ([10-K p:118]); it is not a current covenant and is not used.

### Interpretation: evidence, risk mechanism, credit implication

- Leverage. Evidence: total debt 2,412,308 against Credit Agreement TTM Adjusted EBITDA of 467,796 (5.16x gross; 4.9x on the company's net definition); total debt at March 31, 2026 was 2,393,007. Mechanism: the measured improvement comes from the earnings base growing into the pro forma figure (441,030 to 467,796) and cash rising, not from repayment, and the earnings base includes assumed synergies. Implication: leverage is sensitive to synergy delivery; a shortfall of 10% in pro forma EBITDA would add roughly 0.6x to gross leverage. That sensitivity is derived and illustrative.
- Cover and floating-rate cost. Evidence: H1 FY2027 EBITDA over cash interest of 2.45x; interest and debt expense 95,660 for six months versus FY2027 guidance of 185 to 190 million. Mechanism: floating-rate debt of 1,551,465 with 965,000 hedged leaves about 586,465 exposed to base-rate moves, and the term loan margin was just cut by 50 bps. Implication: a 100 bps rise in base rates would add roughly 5,865 a year on the unhedged amount (derived, illustrative, ignoring the floor and hedge expiries), small against EBITDA but large against free cash flow of 4,601 in H1 FY2027.
- Cash generation. Evidence: H1 FY2027 operating cash flow 21,065 and free cash flow 4,601 after cash deal and integration costs of 24,300 (company-stated for the first half, [EX Nov03 p:3]); cash interest paid 90,921. Mechanism: deal and integration cash costs plus working capital outflows absorb EBITDA. Implication: the planned 150,000 paydown over the next 12 months is not funded by H1 free cash flow; it depends on the second half and on working capital release.
- Liquidity. Evidence: 531,980 at September 30, 2026, down from 561,216; AR facility capacity nil. Mechanism: higher revolver and letters of credit usage. Implication: sufficient on its face for the 12-month needs stated (150,000 paydown, capex guidance of 45 to 55 million), but it is concentrated in one revolver whose covenant trigger is not disclosed.

## Calculations

All inputs are US$ thousands as printed unless stated. Each derived figure shows its inputs; rounding is to the displayed digits.

1. Total debt at March 31, 2025 = current portion 50,739 + long-term line 420,236 = 470,975 [10-K p:74]. Net debt = 470,975 - cash 53,683 = 417,292.
2. Net debt (simple) = total debt less cash: March 31, 2026 2,393,007 - 96,562 = 2,296,445; June 30, 2026 2,376,783 - 98,410 = 2,278,373; September 30, 2026 2,412,308 - 110,900 = 2,301,408.
3. Total debt / EBITDA: FY2025 470,975 / 156,751 = 3.005, shown 3.00. March 2026 2,393,007 / 441,030 = 5.426, shown 5.43. June 2026 2,376,783 / 460,917 = 5.157, shown 5.16. September 2026 2,412,308 / 467,796 = 5.157, shown 5.16. Net: 417,292 / 156,751 = 2.662 (2.66); 2,296,445 / 441,030 = 5.207 (5.21); 2,278,373 / 460,917 = 4.943 (4.94); 2,301,408 / 467,796 = 4.920 (4.92).
4. Company Credit Agreement Net Debt check, September 30, 2026: total debt 2,412,308 + standby letters of credit 19,276 - cash 110,900 - AR facility obligations 42,762 = 2,277,922, equal to the printed figure; 2,277,922 / 467,796 = 4.87, printed as 4.9x. March 31, 2026: 2,393,007 + 16,067 - 96,562 - 53,127 = 2,259,385; / 441,030 = 5.12 (printed 5.1x). June 30, 2026: 2,376,783 + 18,418 - 98,410 - 51,391 = 2,245,400; / 460,917 = 4.87 (printed 4.9x).
5. Credit Agreement TTM Adjusted EBITDA reconciliation check, September 30, 2026: -345,759 + 132,389 + 60,475 + 139,360 + 25,241 + 156,691 + 12,565 + 39,889 + 37,563 + 99,441 + 3,370 + 274 + 392 + 200,000 + 3,049 - 102,153 - 914 - 735 + 6,658 = 467,796. The March 31, 2026 column sums to 441,030 and the June 30, 2026 column to 460,917 on the same method.
6. LTM company-reported Adjusted EBITDA to September 30, 2026 = FY2026 181,373 - H1 FY2026 72,828 + H1 FY2027 222,648 = 331,193. Total debt / 331,193 = 7.28; net 2,301,408 / 331,193 = 6.95. Difference to the lender-defined figure = 467,796 - 331,193 = 136,603.
7. Interest cover: FY2025 156,751 / 30,054 = 5.22; FY2026 181,373 / 45,630 = 3.97; H1 FY2026 72,828 / 16,114 = 4.52; H1 FY2027 222,648 / 90,921 = 2.45. Q2 FY2027 interest paid = 90,921 - Q1 29,532 [10-Q Jun26 p:7] = 61,389; Q2 EBITDA 111,205 / 61,389 = 1.81 (not charted because Q2 holds the first notes coupon, 900,000 x 7.125% / 2 = 32,063, and Q1 holds none). LTM cash interest to September 30, 2026 = 45,630 - 16,114 + 90,921 = 120,437 (mixed pre- and post-acquisition structure; not used).
8. Q2 FY2027 income taxes paid = H1 25,589 - Q1 13,908 = 11,681.
9. Add-back concentration: 132,389 / 467,796 = 28.3%; (132,389 + 99,441 + 39,889 + 37,563) = 309,282; 309,282 / 467,796 = 66.1%.
10. Liquidity: March 31, 2026 96,562 + 458,933 + 5,721 = 561,216 (matches stated); revolver 500,000 - 25,000 - 16,067 = 458,933. June 30, 2026 revolver 500,000 - 12,844 - 18,418 = 468,738; plus cash 98,410 = 567,148. September 30, 2026 revolver 500,000 - 59,644 - 19,276 = 421,080; plus cash 110,900 = 531,980.
11. Debt principal to carrying value, September 30, 2026: 1,449,233 + 900,000 + 42,588 + 59,644 + 5,183 + 11,132 = 2,467,780; discount and issuance costs 42,656 + (13,973 - 1,331) + (273 - 99) = 55,472; 2,467,780 - 55,472 = 2,412,308. March 31, 2026: 1,456,990 + 900,000 + 25,000 + 53,400 + 5,606 + 11,549 = 2,452,545; costs 45,678 + (13,973 - 333) + (273 - 53) = 59,538; 2,452,545 - 59,538 = 2,393,007.
12. Maturity table composition at March 31, 2026: 1,456,990 + 900,000 + 53,400 + 25,000 + 5,606 = 2,440,996 (printed total). FY2027: 12,375 + 5,606 = 17,981. FY2029: 16,500 + 53,400 = 69,900. Thereafter: 1,456,990 - 12,375 - 16,500 - 16,500 - 16,500 = 1,395,115, plus 900,000 plus 25,000 = 2,320,115. The current portion at March 31, 2026: 160,000 + 5,606 + 812 = 166,418.
13. Change in total debt, H1 FY2027: 2,412,308 - 2,393,007 = 19,301 increase. Change in Credit Agreement TTM Adjusted EBITDA: 467,796 - 441,030 = 26,766 increase.
14. Floating-rate principal = term loan 1,449,233 + revolver 59,644 + AR 42,588 = 1,551,465; less swap notional 965,000 = 586,465; 1% of 586,465 = 5,865.
15. Sensitivity: 10% lower pro forma EBITDA = 467,796 x 0.9 = 421,016; 2,412,308 / 421,016 = 5.73 versus 5.16, an increase of about 0.57.
16. Free cash flow: FY2026 -146,211 - 17,859 = -164,070; H1 FY2027 21,065 - 16,464 = 4,601; Q2 FY2027 -4,559 - 10,796 = -15,355.
17. Q3 FY2026 Adjusted EBITDA (not used) = 181,373 - 72,828 - 68,731 = 39,814.

## Gaps

| Gap | Detail | Effect |
| --- | --- | --- |
| Executed credit documents | 2026 Credit Agreement, indenture, AR facility agreement and amendments: Not supplied (CP-0 G1) | Covenant trigger, step-down dates, first lien definition, guarantors, collateral and ranking are not verifiable; headroom Not calculable |
| Credit Agreement EBITDA for FY2025 | Not supplied; company-reported Adjusted EBITDA used for FY2025 | FY2025 leverage is not like-for-like with later periods |
| Discrete Q4 FY2026 statements | No quarterly filing; the June 2026 release carries three-month figures (CP-0 G3) | FY2026 quarterly trend only partly available |
| September 30, 2025 balance sheet | Not supplied; only equity and cash are recoverable from the equity and cash-flow statements | H1 FY2026 debt and working-capital comparatives Not supplied |
| AR facility availability at March 31, 2025 | Not supplied | FY2025 undrawn figure excludes it |
| Maturity profile at September 30, 2026 by year | Not supplied beyond the next 12 months | Wall shown as of March 31, 2026 |
| Swap fixed rates and effective rates | Not supplied | Hedged cost of floating debt not computable |
| Preferred share terms | Redemption, ranking, liquidation preference and cash-pay conditions Not supplied | Claim ranking and cash drain from the 7% dividend cannot be assessed |
| Pension funded status and settlement amount after March 31, 2026 | Not supplied | Pension claim figure is as of March 31, 2026 |
| Operating lease liability at September 30, 2026 | Not supplied | Lease claim figure is as of March 31, 2026 |
| Quantified purchase commitments, factoring and supply-chain finance | Not supplied; none found | Possible off-debt claims cannot be quantified |
| Pre-close Kito Crosby statements | Not supplied beyond pro forma note (CP-0 G4) | Pre-deal comparisons not like-for-like |
| Ratings and market data | Not supplied (CP-0 G5) | No market-implied or rating-based view |
| Reconciliation of the 150,000 planned paydown to current portion | Not supplied | Current-portion composition unresolved |
| Revolver maturity (C1) | Unresolved conflict | Maturity wall and liquidity runway uncertain |

## Next module

CP-1A should take the business and transaction context from the same sources and carry forward: the perimeter changes (Kito Crosby from February 3, 2026, divestiture March 4, 2026); the preferred equity (CD&R Investor, conversion price, 7% in kind or cash, ownership percentage conflict C2); and the debt and covenant limits above. Any later module that uses leverage must name the EBITDA basis (company-reported or Credit Agreement pro forma) and the net debt definition, and must not treat the 4.9x lender measure as first lien covenant headroom. The Q1 FY2027 Adjusted EBITDA revision of 21 and the revolver maturity conflict should be cited, not resolved, until the executed documents are supplied.
