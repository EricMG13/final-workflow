## Request

Module: financial base for MAXLINEAR, INC (MaxLinear, Inc., Nasdaq: MXL, issuer id mxl), as of 2026-11-05, evidence cutoff 2026-11-05. Pathway: credit snapshot. Reporting currency USD; the filings report in thousands of USD and this handoff keeps that unit unless a label says US$m. Current period q3-2026 (quarter and nine months ended 2026-09-30); prior period fy-2025 (year ended 2025-12-31). Perimeter: MaxLinear, Inc. and its directly and indirectly wholly-owned subsidiaries, consolidated, as filed. No parent, sponsor or separate borrower entity is named in the context or sources.

Scope: reported statement facts, the calculations a credit analyst needs from them (EBITDA proxy, leverage, coverage, liquidity), the full debt and off-debt claims picture, covenants, the latest quarter and events to the cutoff, and the four chart tables the report needs. The upstream readiness handoff rated this module READY_WITH_LIMITATIONS; those limitations are carried below.

## Sources

### Issuer sources relied on

Locators are `page:N` chunks of the pinned extractions, not printed pages. Amounts are USD thousands unless stated.

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_mxl-20251231.htm.jsonl | 88c5a5c8ff6cf18541031ab4aef4feb9645b937db462a2943427cc48c137e1d9 |
| 10-Q_2026-03-31_mxl-20260331.htm.jsonl | 42848ffc444d8c47a09304ae1148778a878e57d84c54fa74dc1f2b0e6e5d0dd8 |
| 10-Q_2026-06-30_mxl-20260630.htm.jsonl | 01411c1534e3e0c0e916b41e14102517d827593ed353c6e2edbb7bcfabe4eb3d |
| 10-Q_2026-09-30_mxl-20260930.htm.jsonl | 75f4d013edbcd52763843513db2d44d0258392fcbcf7fab3f738307f7e5ec1a3 |
| EX-99.1_2026-04-22_a03312026exhibit991.htm.jsonl | 80656f36f632a9814cfc0d89b1465026471d15c2a52a4f467e504c7d5e0b776a |
| EX-99.1_2026-07-23_a06302026exhibit991.htm.jsonl | 513984500469e10cfb125419373d89d4b53d02f7f1ffe85723d32af0bb949f83 |
| EX-99.1_2026-10-22_a09302026exhibit991.htm.jsonl | 2f6d78692e5e0106407183ea23f9296509641c88888df05a93887a904e78fabf |

Run context (not issuer evidence): context, sha256 39695f94e05534dbaa55be69eaec116e2e3f550f0af980e236d8132f5e5386f2.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 5befe5c880ee0e3433b442e8789a41a9cded34b374570aca05a9aef7730f3cef | Source readiness, entity roles, covenant conflicts and gaps; opened and consumed below |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Earnings turned positive in Q3 2026 but operating cash flow did not, and debt rose to USD 165.0 million as the revolver funded working capital; on a GAAP EBITDA proxy leverage is 5.52x gross and 2.81x net. | Medium | The agreement's EBITDA definition is not supplied and the proxy rests on one profitable quarter, so covenant headroom is unverified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Revenue rose each quarter of 2026 to USD 218.1 million in Q3 2026, and operating income moved from a loss to a profit of USD 30.2 million. | The trailing EBITDA proxy is positive only in the latest window, so leverage ratios are new and unseasoned. | High |
| Operating cash flow was negative USD 17.7 million over nine months 2026 as receivables, inventory and prepayments grew. | Growth is financed by the revolver, USD 40.0 million drawn at 2026-09-30, rather than by internal cash. | High |
| All debt is secured bank debt maturing in 2028: a USD 125.0 million term loan and the USD 40.0 million revolver draw. | The whole structure faces one refinancing window in 2028. | High |
| Purchase obligations of USD 273.0 million and an unquantified Silicon Motion claim sit outside the debt figure. | Fixed cash calls and a contingent claim add to cash needs beyond debt service. | Medium |
| The liquidity covenant floor falls from USD 80.0 million to USD 60.0 million after 2026-10-16, with undrawn revolver of USD 90.0 million at quarter end. | Covenant liquidity looks ample, but letter of credit use and borrowing conditions are not supplied. | Medium |

### Financial base view

MaxLinear is a single-entity, fabless semiconductor credit whose reported earnings inflected in 2026 while its balance sheet absorbed the growth. Net revenue rose from 137,188 in Q1 2026 to 168,847 in Q2 2026 and 218,057 in Q3 2026 (first quarter 10-Q `page:2`-`page:3`; second quarter 10-Q `page:4`-`page:5`; third quarter 10-Q `page:4`-`page:5`). Income from operations moved from a loss of 17,209 in Q1 2026 to a profit of 30,227 in Q3 2026. On a GAAP EBITDA proxy that adds back depreciation and intangible amortization (not operating lease amortization, and not stock-based compensation), trailing twelve-month EBITDA to 2026-09-30 is 29,865, which gives total debt of 165,000 a ratio of 5.52x and net debt of 83,915 a ratio of 2.81x; trailing EBITDA coverage of cash interest is 3.51x. Those ratios exist only for the latest window: the proxy was negative for FY2024, FY2025 and the trailing windows to Q1 2026 and Q2 2026, and excluding Q3 2026 the trailing figure would be negative 9,215. The strongest contrary evidence is cash: net cash used in operating activities was 17,653 for nine months 2026 (about USD 17.7 million), against 9,213 provided in nine months 2025, because receivables, inventory and prepaid expenses absorbed cash (`page:6` of the third quarter 10-Q; management attributes it to wafer prepayments and inventory for data center demand, `page:62`). The revolver went from undrawn at 2026-06-30 to 40,000 drawn at 2026-09-30, and total debt principal rose from 125,000 to 165,000. Definition risks run both ways: the proxy is far below what the credit agreement's Consolidated EBITDA might show (stock-based compensation alone was 86,923 over the trailing twelve months), but that definition is not supplied, so covenant compliance, which the issuer states as met at 2026-09-30 (`page:24`), cannot be verified. In USD millions the headline figures are: Q3 2026 net revenue USD 218.1 million; Q3 2026 income from operations USD 30.2 million; nine-month 2026 operating cash flow negative USD 17.7 million; total debt principal USD 165.0 million, being the term loan of USD 125.0 million plus the revolver draw of USD 40.0 million; undrawn revolver USD 90.0 million at 2026-09-30; inventory purchase obligations USD 273.0 million; and a liquidity covenant floor of USD 80.0 million that the amendment of 2026-10-16 lowers to USD 60.0 million. Consequence for the credit view: operating momentum is real and the covenant package looks accommodating, but leverage depends on one quarter, cash conversion is negative, working-capital commitments are still growing, and all debt matures in 2028.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | Not supplied: EBITDA proxy negative, ratio not meaningful | Not supplied: EBITDA proxy negative, ratio not meaningful | x | Debt principal 125,000 and cash 118,575 at 2024-12-31 (10-K `page:164`, `page:136`); EBITDA proxy about negative 177,201 (operating loss 223,352 plus depreciation 23.0 million and intangible amortization 23,151, both from 10-K `page:163`, `page:160`) |
| FY2025 | Not supplied: EBITDA proxy negative, ratio not meaningful | Not supplied: EBITDA proxy negative, ratio not meaningful | x | Debt principal 125,000, cash 72,806 at 2025-12-31; EBITDA proxy about negative 90,377 (operating loss 126,890 plus 36,513 depreciation and intangible amortization) |
| LTM Q1 2026 | Not supplied: LTM EBITDA proxy negative, ratio not meaningful | Not supplied: LTM EBITDA proxy negative, ratio not meaningful | x | Debt principal 125,000, cash 61,077 at 2026-03-31; LTM EBITDA proxy about negative 61,626 |
| LTM Q2 2026 | Not supplied: LTM EBITDA proxy negative, ratio not meaningful | Not supplied: LTM EBITDA proxy negative, ratio not meaningful | x | Debt principal 125,000, cash 64,814 at 2026-06-30; LTM EBITDA proxy about negative 41,514 |
| LTM Q3 2026 | 5.52 | 2.81 | x | Debt principal 165,000 (term loan 125,000 plus revolver 40,000), cash and cash equivalents 81,085 (excluding 28,779 restricted cash), LTM EBITDA proxy about 29,865; GAAP operating income plus depreciation plus intangible amortization, no add-backs; excludes operating lease liabilities of 21,943; not the covenant definition, which is not supplied |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | Not supplied: EBITDA proxy negative, ratio not meaningful | x | Cash paid for interest 9,743 (10-K `page:138`) |
| FY2025 | Not supplied: EBITDA proxy negative, ratio not meaningful | x | Cash paid for interest 8,598 (10-K `page:138`) |
| LTM Q1 2026 | Not supplied: LTM EBITDA proxy negative, ratio not meaningful | x | LTM cash paid for interest 8,388 |
| LTM Q2 2026 | Not supplied: LTM EBITDA proxy negative, ratio not meaningful | x | LTM cash paid for interest 8,260 |
| LTM Q3 2026 | 3.51 | x | LTM EBITDA proxy about 29,865 over LTM cash paid for interest 8,508; the revolver draw of 40,000 was outstanding for only part of the window, so the denominator understates the run rate (indicative run-rate cover 2.59x, see Calculations) |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| 2025-12-31 | 72.806 | 100.000 | US$m | Cash and cash equivalents only (restricted cash 28.606 excluded); revolver commitment 100.0 undrawn (10-K `page:165`); facility was due 2026-06-23 (10-K `page:167`), within twelve months; letters of credit issued under it not supplied |
| 2026-03-31 | 61.077 | 100.000 | US$m | Revolver undrawn (first quarter 10-Q `page:17`); commitment 100.0 at quarter end, the 30.0 increase and extension to 2028-03-23 came on 2026-04-22 (`page:40`) |
| 2026-06-30 | 64.814 | 130.000 | US$m | No borrowings outstanding (second quarter 10-Q `page:23`); commitment 100.0 plus 30.0 incremental |
| 2026-09-30 | 81.085 | 90.000 | US$m | Commitment 130.0 (implied: 200 total after the 70 million increase of 2026-10-16, third quarter 10-Q `page:44`) less 40.000 drawn (`page:20`); letters of credit under the 10.0 sublimit not supplied |
| 2026-09-30 pro forma for 2026-10-16 amendment | 81.085 | 160.000 | US$m | Cash is the 2026-09-30 balance, not updated; commitments 200 less 40.000 drawn; illustrative only |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 (Q4) | 0 | US$m | No amortization remains; contractual obligations table shows nil due within one year (third quarter 10-Q `page:58`) |
| 2027 | 0 | US$m | No scheduled maturity; the 1-3 year bucket of 165,000 falls in 2028 by facility dates |
| 2028 | 165.000 | US$m | Revolver drawn 40.000 matures 2028-03-23; Initial Term Loan 125.000 matures 2028-06-23 (`page:20`, `page:23`); the 2026-10-16 amendment's effect on revolver maturity is not stated |
| 2029 | 0 | US$m | Nil in the 3-5 year bucket (`page:58`) |
| 2030 and later | 0 | US$m | Nil in the more-than-5-year bucket (`page:58`) |

### Financials and credit metrics

USD thousands unless stated. Quarter columns are discrete quarters (Q2 and Q3 derived from cumulative filings, see Calculations); balance rows are period-end; the 9M and LTM columns show the 2026-09-30 balance. Ratio rows use LTM EBITDA to each period end. A tilde marks a figure that rests on a rounded filing input.

| Metric | FY2024 | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | 9M 2026 | LTM Q3 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net revenue | 360,528 | 467,641 | 137,188 | 168,847 | 218,057 | 524,092 | 660,528 |
| Gross profit | 194,782 | 265,814 | 78,884 | 97,663 | 128,070 | 304,617 | 383,174 |
| Gross margin (%) | 54.0 | 56.8 | 57.5 | 57.8 | 58.7 | 58.1 | 58.0 |
| Income (loss) from operations | (223,352) | (126,890) | (17,209) | (4,185) | 30,227 | 8,833 | (6,059) |
| Depreciation and intangible amortization (excl. lease amortization) | ~46,151 | ~36,513 | 9,119 | 9,011 | 8,853 | 26,983 | ~35,924 |
| EBITDA proxy | ~(177,201) | ~(90,377) | (8,090) | 4,826 | 39,080 | 35,816 | ~29,865 |
| Stock-based compensation (cash flow statement) | 66,021 | 77,128 | 20,027 | 27,479 | 19,824 | 67,330 | 86,923 |
| Net income (loss) | (245,198) | (136,681) | (45,137) | 1,760 | 28,902 | (14,475) | (29,372) |
| Interest expense (income statement) | 10,874 | 10,056 | 2,197 | 2,269 | 2,692 | 7,158 | 9,549 |
| Cash paid for interest | 9,743 | 8,598 | 1,935 | 2,049 | 2,441 | 6,425 | 8,508 |
| Cash paid for income taxes, net of refunds | 8,194 | 5,792 | 1,992 | (4,108) | (1,914) | (4,030) | (2,602) |
| Net cash from (used in) operating activities | (45,295) | 19,619 | (8,872) | 4,809 | (13,590) | (17,653) | (7,247) |
| Purchases of property and equipment plus intangible assets | 23,446 | 19,795 | 2,239 | 3,148 | 9,648 | 15,035 | 18,721 |
| Free cash flow (operating cash flow less those purchases) | (68,741) | (176) | (11,111) | 1,661 | (23,238) | (32,688) | (25,968) |
| Cash and cash equivalents (period end) | 118,575 | 72,806 | 61,077 | 64,814 | 81,085 | 81,085 | 81,085 |
| Restricted cash, short and long term (period end) | 1,028 | 28,606 | 28,855 | 28,918 | 28,779 | 28,779 | 28,779 |
| Total debt principal (period end) | 125,000 | 125,000 | 125,000 | 125,000 | 165,000 | 165,000 | 165,000 |
| Net carrying amount of long-term debt (period end) | 122,996 | 123,618 | 123,773 | 123,926 | 164,062 | 164,062 | 164,062 |
| Net debt: principal less cash and cash equivalents | 6,425 | 52,194 | 63,923 | 60,186 | 83,915 | 83,915 | 83,915 |
| Accounts receivable, net (period end) | 85,464 | 46,122 | 40,855 | 51,037 | 73,381 | 73,381 | 73,381 |
| Inventory (period end) | 90,343 | 78,104 | 85,839 | 105,490 | 113,722 | 113,722 | 113,722 |
| Prepaid expenses and other current assets (period end) | 28,057 | 50,390 | 60,253 | 75,829 | 121,648 | 121,648 | 121,648 |
| Total stockholders' equity (period end) | 516,283 | 451,895 | 454,191 | 484,840 | 533,009 | 533,009 | 533,009 |
| Total debt / LTM EBITDA proxy (x) | Not meaningful | Not meaningful | Not meaningful | Not meaningful | 5.52 | Not applicable | 5.52 |
| Net debt / LTM EBITDA proxy (x) | Not meaningful | Not meaningful | Not meaningful | Not meaningful | 2.81 | Not applicable | 2.81 |
| LTM EBITDA proxy / LTM cash interest (x) | Not meaningful | Not meaningful | Not meaningful | Not meaningful | 3.51 | Not applicable | 3.51 |

### Debt schedule at 2026-09-30

The debt table in note 8 lists two instruments, both under the June 23, 2021 Credit Agreement (third quarter 10-Q `page:19`-`page:24`). There are no notes or bonds and no co-issuers.

| Instrument | Borrower | Principal | Rate | Maturity | Security and guarantors | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| Initial Term Loan (senior secured term B; original 350,000) | MaxLinear, Inc. | 125,000 | Adjusted Term SOFR (floor 0.50%) plus 2.25%, or base rate plus 1.25% | 2028-06-23; no scheduled amortization remains | Substantially all assets of the company and subsidiary guarantors; guaranteed by certain domestic subsidiaries meeting materiality thresholds (not named) | `page:20`-`page:23` |
| Revolving Facility | MaxLinear, Inc. | 40,000 drawn; commitments 130,000 at quarter end (implied), 200,000 after 2026-10-16 | Term SOFR plus 2.25%, or base rate plus 1.25%; commitment fee 0.25% | 2028-03-23 (extended from 2026-06-23 on 2026-04-22) | Same collateral and guarantee package; includes a 10,000 Letter of Credit Commitment | `page:20`, `page:22`-`page:23`, `page:44` |

Other facts: unamortized discount 226 and issuance costs 712 reduce 165,000 to a carrying amount of 164,062 (`page:19`); the weighted average effective interest rate on aggregate debt was about 7.0% at 2026-09-30 and 6.9% at 2025-12-31 (`page:19`); the term loan's fair value was 123.4 million against 125.0 million of principal (Level 2, `page:20`); a 1.00% soft call applied only during the six months after the April 2026 amendment (`page:23`). Maturity wall by year: 2026 nil, 2027 nil, 2028 165,000, 2029 and later nil. The incremental loan capacity is the greater of 175.0 million and 100% of consolidated EBITDA plus ratio-based amounts (`page:21`).

### Covenants

| Test | Level | Reported figure | Headroom |
| --- | --- | --- | --- |
| Total net leverage ratio | Not above 3.50 to 1.00, tested at each fiscal quarter end (`page:23`-`page:24`) | Not printed; the company states compliance at 2026-09-30 | Proxy only: net debt of 83,915 over LTM EBITDA proxy of about 29,865 is 2.81x, 0.69x below the level; the proxy EBITDA could fall about 5,889 (about 19.7%) before it reached 3.50x. The agreement's Consolidated EBITDA is not supplied and may be much higher (add-backs for stock-based compensation alone were 86,923 over the trailing twelve months) |
| Liquidity: unrestricted cash plus available undrawn revolver commitments | Not less than 80.0 million at 2026-09-30 (`page:24`); reduced to 60 million by the amendment of 2026-10-16 (`page:44`-`page:45`, `page:48`) | Not printed | Computed: 81,085 plus 90,000 equals 171,085, headroom 91,085 against 80,000, before any letters of credit; pro forma for the amendment 241,085 against 60,000 |
| Springing secured net leverage test (3.50 to 1.00, 3.75 after certain acquisitions, if revolver borrowings exceed 1% of commitments) | Described in the 10-K, first and second quarter 10-Qs; absent from the third quarter note | Not printed | Borrowings of 40,000 exceed 1% of 130,000 at 2026-09-30, so if the test survives the second amendment it would apply; whether it survives is unresolved (see the upstream readiness handoff) |

Definitions that differ from the metric computed here: the covenant ratio is a "total net leverage ratio" on the agreement's Consolidated EBITDA, whereas this handoff computes net debt over a GAAP EBITDA proxy with no add-backs; netting of cash and any cash cap, and treatment of leases, are unknown.

### Claims outside the debt figure

None of the following is inside the 165,000 of debt principal.

| Claim | Amount | Treatment and locator |
| --- | --- | --- |
| Inventory purchase obligations | 272,967 (88,690 in Q4 2026; 184,277 in 2027) | Off balance sheet; rose from 168,484 at 2025-12-31 (10-K `page:120`; third quarter 10-Q `page:37`, `page:58`) |
| Other obligations (mainly software licenses) | 74,589 | Off balance sheet (`page:37`, `page:58`) |
| Operating lease liabilities | 21,943 (long-term 13,776; short-term 8,167 inside accrued expenses); minimum payments 24,571 | On balance sheet, not in debt (`page:37`, `page:19`) |
| Contingent consideration | 2,600 | Current liability, Level 3 (`page:17`, `page:19`) |
| Sale arrangement for claims | 8,000 received, in other long-term liabilities; interest sold in claims for up to 10,000 | Derecognized on settlement of the claims; further contingent payments not estimable (`page:24`) |
| Jointly funded research and development | 15,000 received, repayable if conditions are not resolved | In other long-term liabilities (`page:38`) |
| Uncertain tax positions | 4,400 in other long-term liabilities | Timing uncertain (`page:59`) |
| Price protection and customer obligations | 30,367 accrued price protection; 14,428 price adjustments; 343 stock rotation | On balance sheet (`page:19`, `page:36`) |
| Pension and other defined benefit | Net unfunded status 315 at 2025-12-31 | Small (10-K `page:186`); not updated in the 10-Qs |
| Restricted cash held as collateral for letters of credit | 28,779 (1,359 short term, 27,420 long term) | The 10-K states restricted cash is collateral for letters of credit (`page:141`); issued letter of credit balances are not supplied |
| Silicon Motion arbitration and stockholder suits; Comcast, Dish, Cox, DIRECTV matters | No amount; no material loss accrued; unfavorable outcome reasonably possible, range not estimable | `page:38`-`page:43` |
| Share repurchase authorization | 55.0 million remaining; no repurchases in nine months 2026 | Discretionary (`page:44`) |

Factoring, supply-chain or supplier finance, capacity reservation arrangements and consent decrees: searched for in all seven sources by those terms; nothing found. Wafer prepayments are discussed as a use of cash (first quarter 10-Q `page:54`; third quarter 10-Q `page:62`) but no separate financing arrangement is described.

### Latest quarter and events to the cutoff

- Q3 2026 (quarter ended 2026-09-30): net revenue 218,057 against 126,459 in Q3 2025, up 72% as reported (release `page:1`); infrastructure revenue 124,907 against 40,343 and 57% of revenue, broadband 53,345 against 58,236 (third quarter 10-Q `page:34`-`page:35`, `page:50`-`page:51`). Gross margin 58.7%; operating income 30,227; net income 28,902 after an income tax benefit of 732 (`page:5`).
- Financing in Q3: revolver borrowings of 40,000 and no repayment (release `page:9`); 9M 2026 borrowings 60,000 and repayments 20,000 (`page:6`); the revolver was borrowed and repaid within Q2 2026 (20,000 each way).
- Q1 2026: the second amendment of 2026-04-22 extended the revolver to 2028-03-23, added 30 million of commitments, raised the margin to 2.25% (Term SOFR) and set the covenants above (first quarter 10-Q `page:40`).
- Subsequent event, 2026-10-16: third amendment adds 70 million of revolving commitments for a total of 200 million and lowers the liquidity floor from 80 million to 60 million (third quarter 10-Q `page:44`-`page:45`).
- Outlook (management, release of 2026-10-22, `page:2`): Q4 2026 revenue 240 to 260 million, GAAP gross margin 58.0% to 61.0%, GAAP operating expenses 96 to 101 million, interest and other expense 3.5 to 4.3 million. This is a management claim, not a filed figure.
- Management non-GAAP income from operations: 21,756 in Q1 2026, 37,608 in Q2 2026, 64,290 in Q3 2026 and 123,654 for nine months 2026 (releases; third quarter release `page:8`, second quarter release `page:9`). These add back stock-based compensation, performance-based equity, purchased intangible amortization, acquisition costs and restructuring, and are not used in the ratios above.
- Between 2026-10-22 and the cutoff no source is supplied.

### Evidence, risk mechanism and credit implication

1. Earnings recovery is steep but short. Evidence: operating income of negative 17,209, negative 4,185 and 30,227 in Q1, Q2 and Q3 2026; trailing EBITDA proxy turns from negative 41,514 at Q2 to 29,865 at Q3. Risk mechanism: leverage and coverage ratios are driven by a single quarter, so a demand pause or margin slip reverses them. Implication: gross leverage of 5.52x exceeds the 3.50x covenant level, but the covenant is on net leverage (2.81x on the proxy), so compliance depends on cash netting and on the agreement's unsupplied EBITDA definition.
2. Growth consumes cash. Evidence: the nine-month cash flow statement shows cash absorbed of 27,259 by receivables, 35,618 by inventory and 68,168 by prepaid expenses and other assets (`page:6`); purchase obligations rose to 272,967. Risk mechanism: wafer prepayments and committed purchases precede revenue, so each step-up in the outlook needs financing before cash returns. Implication: revolver reliance rises with growth; availability, not earnings, is the binding constraint.
3. Single-bank secured structure with a 2028 wall. Evidence: 165,000 of principal, all maturing in 2028, floating rate at about 7.0% effective. Risk mechanism: no staggered maturities and a springing-test ambiguity. Implication: refinancing risk is concentrated in the first half of 2028 and the covenant package should be confirmed from the executed agreement.
4. Contingent claims are unsized. Evidence: the arbitration seeks the termination fee plus additional damages and costs; no loss is accrued. Risk mechanism: an award or settlement would be a cash outflow that reduces the unrestricted cash counted in the liquidity covenant. Implication: headroom analysis must be stressed for an unsized claim.

### Consistency with the upstream readiness handoff

The upstream handoff rated this module READY_WITH_LIMITATIONS and flagged covenant wording conflicts, revolver size at quarter end, unsupplied letter of credit use and an unquantified Silicon Motion claim. All hold. Additions and one clarification found in this module: (1) the cash flow line "Amortization and depreciation" is on two different bases across filings. The 10-K (FY2025) and the first quarter 10-Q include operating lease right-of-use amortization in that line (no separate lease line exists and the statements still sum to operating cash flow), while the second and third quarter 10-Qs and releases show lease amortization separately (nine months 2026: 26,983 excluding 5,336 of lease amortization). The second quarter release restates Q1 2026 as 9,119 against 10,939 in the first quarter 10-Q (`page:10` of the second quarter release), a difference of 1,820 equal to the lease line shown there. This handoff uses the excluding-lease basis throughout. (2) The upstream handoff recorded issued letter of credit balances as not found; that still holds. This module adds that restricted cash of 28,779 is stated by the 10-K to be collateral for letters of credit, which may mean they are cash collateralised outside the revolver, but the sources do not say so.

## Calculations

All inputs are printed in the cited filings; derived values are marked.

### Expense block reconciliation to operating profit

Gross profit less research and development, selling, general and administrative and restructuring (and impairment losses where printed) equals income (loss) from operations; no unresolved difference.

| Period | Gross profit | Operating expense block | Result | Printed operating income (loss) | Difference |
| --- | --- | --- | --- | --- | --- |
| FY2025 | 265,814 | 208,599 + 159,580 + 24,525 = 392,704 | (126,890) | (126,890) | 0 |
| FY2024 | 194,782 | 225,189 + 138,329 + 1,237 + 53,379 = 418,134 | (223,352) | (223,352) | 0 |
| Q1 2026 | 78,884 | 53,162 + 42,457 + 474 = 96,093 | (17,209) | (17,209) | 0 |
| Q2 2026 | 97,663 | 56,033 + 45,751 + 64 = 101,848 | (4,185) | (4,185) | 0 |
| Q3 2026 | 128,070 | 60,642 + 36,947 + 254 = 97,843 | 30,227 | 30,227 | 0 |
| 9M 2026 | 304,617 | 169,837 + 125,155 + 792 = 295,784 | 8,833 | 8,833 | 0 |

### Discrete quarters from cumulative filings (derived)

| Item | Q1 2026 | Six months 2026 | Q2 2026 = six months less Q1 | Nine months 2026 | Q3 2026 = nine months less six months |
| --- | --- | --- | --- | --- | --- |
| Net cash from operating activities | (8,872) | (4,063) | 4,809 | (17,653) | (13,590) |
| Purchases of property and equipment | 1,384 | 3,722 | 2,338 | 9,662 | 5,940 |
| Purchases of intangible assets | 855 | 1,665 | 810 | 5,373 | 3,708 |
| Cash paid for interest | 1,935 | 3,984 | 2,049 | 6,425 | 2,441 |
| Cash paid for income taxes, net of refunds | 1,992 | (2,116) | (4,108) | (4,030) | (1,914) |

The derived Q2 and Q3 operating cash flow figures equal the second and third quarter release columns (4,809 and negative 13,590, third quarter release `page:9`). Capital purchases: Q1 2,239 (1,384 plus 855), Q2 3,148 (2,338 plus 810), Q3 9,648 (5,940 plus 3,708), nine months 15,035. Free cash flow equals operating cash flow less those purchases: Q1 negative 11,111, Q2 1,661, Q3 negative 23,238, nine months negative 32,688 (sum of the three quarters equals the nine-month figure).

### Depreciation and amortization basis

Basis used: depreciation plus intangible amortization, excluding operating lease right-of-use amortization (the basis of the cash flow line in the second and third quarter 10-Qs).

| Period | Cash flow "Amortization and depreciation" as filed | Basis | Adjustment | Used |
| --- | --- | --- | --- | --- |
| Nine months 2026 | 26,983 | Excludes lease amortization of 5,336 (`page:6`) | None | 26,983 |
| Nine months 2025 | 27,572 | Excludes lease amortization of 5,632 | None | 27,572 |
| Six months 2026 and 2025 | 18,130 and 18,582 | Excludes lease amortization of 3,615 and 3,784 | None | 18,130 and 18,582 |
| Q1 2026 | 10,939 (first quarter 10-Q `page:3`) | Includes lease amortization | Second quarter release shows 9,119 and lease amortization 1,820 (`page:10`) | 9,119 |
| Q1 2025 | 11,149 | Includes lease amortization | 18,582 less Q2 2025 of 9,329 (second quarter release `page:10`) | 9,253 |
| FY2025 | 43,992 (10-K `page:137`) | Includes lease amortization | Depreciation 23.2 million (rounded, `page:163`) plus intangible amortization 13,313 (`page:160`) | ~36,513 |
| FY2024 | 54,140 | Includes lease amortization | Depreciation 23.0 million (rounded) plus intangible amortization 23,151 | ~46,151 |

Cross-check of the basis: for nine months 2026, depreciation 16.8 million plus intangible amortization 10,219 (`page:18`, `page:16`) is about 27.0 million, which matches 26,983. The FY2025 and FY2024 figures carry the rounding of the printed depreciation (plus or minus 50), which moves the trailing ratios by about 0.01x. That the 10-K line includes lease amortization is inferred from the statement sums (the 10-K lines tie to operating cash flow of 19,619 with no separate lease line) and from the 43,992 less 36,513 difference of about 7,479, in line with the 5,632 recorded for the first nine months of 2025.

### Trailing twelve months (LTM = FY2025 + year to date 2026 - year to date 2025)

| Item | LTM Q1 2026 | LTM Q2 2026 | LTM Q3 2026 |
| --- | --- | --- | --- |
| Net revenue | 467,641 + 137,188 - 95,933 = 508,896 | 467,641 + 306,035 - 204,746 = 568,930 | 467,641 + 524,092 - 331,205 = 660,528 |
| Income (loss) from operations | (126,890) + (17,209) - (46,094) = (98,005) | (126,890) + (21,394) - (70,709) = (77,575) | (126,890) + 8,833 - (111,998) = (6,059) |
| Depreciation and intangible amortization | 36,513 + 9,119 - 9,253 = 36,379 | 36,513 + 18,130 - 18,582 = 36,061 | 36,513 + 26,983 - 27,572 = 35,924 |
| EBITDA proxy | (61,626) | (41,514) | 29,865 |
| Cash paid for interest | 8,598 + 1,935 - 2,145 = 8,388 | 8,598 + 3,984 - 4,322 = 8,260 | 8,598 + 6,425 - 6,515 = 8,508 |
| Stock-based compensation (cash flow) | 77,128 + 20,027 - 22,911 = 74,244 | 77,128 + 47,506 - 36,024 = 88,610 | 77,128 + 67,330 - 57,535 = 86,923 |

Other LTM Q3 2026 items: gross profit 265,814 + 304,617 - 187,257 = 383,174; net loss (136,681) + (14,475) - (121,784) = (29,372); interest expense 10,056 + 7,158 - 7,665 = 9,549; cash paid for income taxes 5,792 + (4,030) negative less 4,364 = (2,602); operating cash flow 19,619 + (17,653) - 9,213 = (7,247); capital purchases 19,795 + 15,035 - 16,109 = 18,721; free cash flow (25,968). LTM excluding Q3 2026 equals 29,865 less 39,080, which is (9,215).

### Leverage, coverage and covenant proxy at 2026-09-30

| Measure | Inputs | Result |
| --- | --- | --- |
| Total debt / EBITDA proxy | 165,000 / 29,865 | 5.52x |
| Net debt | 165,000 - 81,085 | 83,915 |
| Net debt / EBITDA proxy | 83,915 / 29,865 | 2.81x |
| EBITDA proxy / cash interest | 29,865 / 8,508 | 3.51x |
| Covenant level 3.50x less proxy net leverage | 3.50 - 2.81 | 0.69x (indicative) |
| EBITDA level at which net leverage equals 3.50x | 83,915 / 3.50 | 23,976; cushion 29,865 - 23,976 = 5,889, about 19.7% of the proxy |
| Liquidity covenant measure | 81,085 + (130,000 - 40,000) = 171,085 vs 80,000 | headroom 91,085 (before letters of credit) |
| Liquidity pro forma 2026-10-16 | 81,085 + (200,000 - 40,000) = 241,085 vs 60,000 | headroom 181,085 (illustrative; cash not updated) |
| Liquidity at 2026-06-30 | 64,814 + 130,000 = 194,814 | tested against the then 80,000 floor: 114,814 |

Sensitivities (analyst-defined, not the covenant definition): adding back trailing stock-based compensation of 86,923 gives an EBITDA of 116,788, so total debt / EBITDA 1.41x, net debt / EBITDA 0.72x and cover 13.73x; netting restricted cash of 28,779 as well as cash gives net debt of 55,136 and 1.85x on the unadjusted proxy. Indicative run-rate interest: 165,000 multiplied by the 7.0% weighted average effective rate is 11,550, and 29,865 / 11,550 gives 2.59x, against 3.51x on historical cash interest.

### Source integrity checks

- Cash reconciliation at 2026-09-30: 81,085 + 1,359 + 27,420 = 109,864, equal to cash, cash equivalents and restricted cash at end of period (`page:7`).
- Net change in cash, nine months 2026: (17,653) + (17,035) + 43,793 + (653) = 8,452, equal to the printed increase.
- Debt carrying amount: 165,000 - 226 - 712 = 164,062, equal to the balance sheet.
- Quarterly sum: depreciation and intangible amortization 9,119 + 9,011 + 8,853 = 26,983, equal to nine months; EBITDA proxy (8,090) + 4,826 + 39,080 = 35,816, equal to 8,833 + 26,983.
- Release and 10-Q agree on Q3 2026 net revenue 218,057, cash 81,085 and long-term debt 164,062.

## Gaps

| Gap | Severity | Effect | Action |
| --- | --- | --- | --- |
| Consolidated EBITDA as defined in the credit agreement and the reported total net leverage ratio are not supplied | High | Covenant headroom is a proxy only; the true cushion could differ widely either way | Obtain the executed agreement and the quarterly compliance certificate |
| Letters of credit issued under the revolver (10.0 million sublimit) and conditions to borrowing are not supplied | Medium | Undrawn availability of 90.0 million is gross of letters of credit | Obtain issued letter of credit balance and availability test |
| Revolver commitments at 2026-09-30 (130.0 million) are implied from the 200 million total and the 70 million increase, not printed as one figure | Medium | Quarter-end undrawn amount rests on an inference consistent with 100 plus 30 | Confirm from the amendment text |
| Whether the springing secured net leverage test survives the second amendment, and the second quarter 10-Q's wording that the liquidity floor is a percentage of EBITDA, are unresolved | High | Two covenant formulations; compliance statement covers "such covenants" only | Resolve against executed agreement |
| Depreciation basis differs between filings; FY2025 and FY2024 depreciation printed only to 0.1 million | Low | Trailing EBITDA proxy accurate to about 50; the lease-inclusive reading would add about 7.5 million | Request unrounded depreciation if precision is needed |
| No Q4 2025 release and no discrete Q4 2025; FY2025 minus nine months 2025 is the only route | Low | LTM figures depend on the 10-K and comparatives | Add the Q4 2025 release |
| Effect of the 2026-10-16 amendment on revolver maturity, margin and fees is not stated | Medium | The 2028 maturity wall is as of the earlier amendment | Obtain the 8-K exhibit |
| Silicon Motion exposure unquantified; arbitration confidential | High | Contingent claim cannot enter leverage or liquidity stress | Monitor; no source can size it |
| No ratings, market quotes, market capitalization or peer data in the context | Low | No market-implied view | Supply if needed |
| Pension obligation shown only at 2025-12-31 (net unfunded 315) | Low | Immaterial | None |
| No source dated after 2026-10-22 | Medium | Cash and revolver balances after 2026-09-30 are unobserved | Add filings through 2026-11-05 |

## Next module

Proceed to CP-1A (business and transaction context). It should take from this handoff: the single-registrant perimeter and 2028 secured bank structure; the terminated Silicon Motion merger and the open arbitration and stockholder suits as unquantified; the credit agreement amendments (2023 benchmark replacement, 2026-04-22 and 2026-10-16) as transactions with their stated terms; the sale arrangement for claims (8,000 received); the end-market revenue shift to infrastructure (57% of Q3 2026 revenue) and customer, supplier and geographic concentrations (`page:34`, `page:46`). Carry forward these limits: the EBITDA proxy is not the covenant definition; ratios exist only for the latest trailing window; liquidity and maturity figures are as of 2026-09-30 with the 2026-10-16 amendment shown separately; the depreciation basis difference is documented above. CP-2 and CP-5 should use the trailing ratios only with their stated basis and the gaps table.
