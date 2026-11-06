# CP-1 financial base: TENET HEALTHCARE CORP (thc)

## Request

- Issuer: TENET HEALTHCARE CORP (issuer id `thc`; registrant as filed: Tenet Healthcare Corporation, NYSE: THC), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run `thc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, reporting currency USD, in millions unless stated. Current period Q3 2026 (quarter and nine months ended September 30, 2026); prior period FY2025.
- Task: extract the reported financial base (income statement, balance sheet, cash flow, debt, liquidity, maturities, non-GAAP Adjusted EBITDA), calculate leverage, interest cover and liquidity from printed components, and state what the evidence supports.
- Execution: host session; no provider call. Locators are `page:N`, the chunk number in the pinned `.jsonl` text, not the printed page.
- Period labels used: FY2024, FY2025, nine months 2025 (9M 2025), nine months 2026 (9M 2026), LTM Q3 2026 (FY2025 plus 9M 2026 less 9M 2025), and balance-sheet instants at December 31, 2024, December 31, 2025, March 31, 2026, June 30, 2026 and September 30, 2026.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_thc-20251231.htm.jsonl | f11b8c51ccd0de901ead39554fe597e277a823a504d6f5879743322f2e033f67 | Audited FY2025 and FY2024 statements, debt note, leases, segment Adjusted EBITDA |
| 10-Q_2026-03-31_thc-20260331.htm.jsonl | ae2f3d08760ee554a01678cce38fd15c1f6dcfb4f1eb937aa8f7c46189f0123b | Unaudited Q1 2026 statements; March 31, 2026 cash and revolver availability |
| 10-Q_2026-06-30_thc-20260630.htm.jsonl | a8d86c65c6d20d928c4d4325b82f5d466ad3837698345b3d3bc00c8145f3cd72 | Unaudited H1 2026 statements; June 30, 2026 cash, debt and six-month Adjusted EBITDA |
| 10-Q_2026-09-30_thc-20260930.htm.jsonl | e79732f4107be2e25480e8b1b80ad38188b6eb8362209287bd06381751951a29 | Unaudited Q3 and 9M 2026 statements, debt note, liquidity, maturity table; controlling for September 30, 2026 |
| EX-99.1_2026-04-30_thc-20260331ex991earningsr.htm.jsonl | 5ea4e9008424f03304d19bf4ecd566569d118ac8a64e8cca9032f7ad6a5e6de8 | Q1 2026 release; management non-GAAP; read for context only |
| EX-99.1_2026-07-23_thc-20260630ex991earningsr.htm.jsonl | 03d054c86dcde38802e070349b77939f6a497570e6b4a7e4537e884b4aff9ae1 | Q2 2026 release; management non-GAAP; read for context only |
| EX-99.1_2026-10-29_thc-20260930ex991earningsr.htm.jsonl | de8966425c6d51c46fec7968d415d855247be5599cd3f04bbba535aedb3bc95d | Q3 2026 release: Adjusted EBITDA definition, reported net-debt ratio, outlook |
| context | 0ee21d145e164a59cd564e90c45b59adffc7b68df2c1b6fb4dcb72027505ffb5 | User run settings; not issuer evidence |

| Handoff module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 7380c434050643b1a54d0163daac1ad648692a43ba1556324f37ec4ffc476d9e | Source readiness: all four consumers READY_WITH_LIMITATIONS; statements are controlling over releases; carry the contract-termination revenue, Adjusted EBITDA and net-debt cautions; covenant text is dated December 31, 2025 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Leverage is moderate and falling: total debt is 2.65x last-twelve-month Adjusted EBITDA and net debt 2.11x, with cash interest cover of 6.03x and 4,574 of liquidity. Earnings are lifted by a transition benefit. | Medium | Adjusted EBITDA is a management measure before noncontrolling holders, and executed credit documents are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Net debt to Adjusted EBITDA of 2.11x reproduces from balance-sheet debt less cash and last-twelve-month Adjusted EBITDA. | The management ratio can be relied on as arithmetic, though its definition is still not printed. | Medium |
| September 2026 refinancing replaced 2027 secured notes and part of the 2028 unsecured notes with 2034 notes. | The nearest maturity wall moves to 2028 and 2030, with no revolver draw. | High |
| Consolidated Adjusted EBITDA includes earnings belonging to noncontrolling holders, who received 838 of cash distributions in the last twelve months. | Leverage on a basis net of those distributions is higher at 3.18x. | Medium |
| Third quarter 2026 Adjusted EBITDA includes a 147 favorable transition and timing effect, and operating cash flow includes 540 of contract-termination receipts. | Underlying earnings and free cash flow are lower than headline figures. | High |

### Financial base view

Tenet is a large, cash-generative hospital and ambulatory-surgery operator whose reported leverage has fallen across the periods supplied. On the carrying amount of long-term debt, total debt over Adjusted EBITDA is 3.30x at FY2024, 2.88x at FY2025 and 2.65x on an LTM Q3 2026 basis; net of cash it is 2.54x, 2.25x and 2.11x. Cash-paid interest cover rises from 4.69x to 5.28x to 6.03x. Liquidity at September 30, 2026 is 2,674 of cash plus 1,900 of undrawn revolver availability, 4,574 in total, with nothing drawn. Debt is predominantly fixed-rate notes, 8,300 first-lien secured and 4,362 unsecured at September 30, 2026, and no maturity exceeds 1,931 until 2030. The picture is credit-supportive on its face, but four limits keep confidence at Medium: Adjusted EBITDA is a management measure that includes the minority share of ambulatory earnings and, in Q3 2026, a 147 favorable transition effect; operating cash flow in 9M 2026 includes 540 received from the CommonSpirit agreements; redeemable noncontrolling interests of 2,179 and operating leases of 1,257 sit outside the debt figure; and the covenant text in the sources is dated December 31, 2025.

| Check | Result | Basis |
| --- | --- | --- |
| Total debt / LTM Adjusted EBITDA, September 30, 2026 | 2.65x | 13,243 over 5,004 |
| Net debt / LTM Adjusted EBITDA, September 30, 2026 | 2.11x | 10,569 over 5,004; equals management's reported 2.11x |
| Adjusted EBITDA / cash interest, LTM Q3 2026 | 6.03x | 5,004 over 830 |
| Liquidity, September 30, 2026 | 4,574 | cash 2,674 plus revolver availability 1,900 |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 3.30 | 2.54 | x | Total debt 13,173 and cash 3,019 at December 31, 2024 over FY2024 Adjusted EBITDA 3,995; company non-GAAP, consolidated before noncontrolling interests; carrying debt including finance leases |
| FY2025 | 2.88 | 2.25 | x | Total debt 13,171 and cash 2,883 at December 31, 2025 over FY2025 Adjusted EBITDA 4,566; net result equals management's reported 2.25x |
| LTM Q3 2026 | 2.65 | 2.11 | x | Total debt 13,243 and cash 2,674 at September 30, 2026 over LTM Adjusted EBITDA 5,004 (FY2025 4,566 plus 9M 2026 3,821 less 9M 2025 3,383); includes a 147 favorable Q3 2026 effect; net result equals management's reported 2.11x |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 4.69 | x | Adjusted EBITDA 3,995 over interest paid net of capitalized interest 851; company non-GAAP numerator |
| FY2025 | 5.28 | x | Adjusted EBITDA 4,566 over interest paid net of capitalized interest 865 |
| LTM Q3 2026 | 6.03 | x | LTM Adjusted EBITDA 5,004 over LTM cash interest 830 (FY2025 865 plus 9M 2026 464 less 9M 2025 499); coupon timing is semi-annual so LTM is used rather than a single quarter |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| December 31, 2025 | 2,883 | 1,900 | US$m | Balance-sheet cash; revolver availability 1,900 with no cash borrowings and less than 1 of standby letters of credit, which is not netted because the exact amount is not printed |
| March 31, 2026 | 2,967 | 1,900 | US$m | Same basis as December 31, 2025 |
| June 30, 2026 | 2,170 | 1,900 | US$m | Same basis as December 31, 2025 |
| September 30, 2026 | 2,674 | 1,900 | US$m | Same basis; the separate 200 letter-of-credit facility (105 of standby letters of credit outstanding) is letter-of-credit capacity only and is excluded; availability is borrowing-base driven and equals the 1,900 commitment |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 (remainder) | 27 | US$m | Fixed-rate long-term debt maturing in the year ending December 31, 2026 as printed at September 30, 2026; before unamortized discounts and issue costs |
| 2027 | 157 | US$m | As printed; the 5.125% secured notes due 2027 were redeemed in September 2026, so this is other debt only |
| 2028 | 1,931 | US$m | As printed; includes the 4.625% secured notes (600) and the 6.125% unsecured notes (1,250 after partial redemption) |
| 2029 | 1,464 | US$m | As printed; includes the 4.250% secured notes (1,400) |
| 2030 | 3,493 | US$m | As printed; includes the 4.375% (1,450) and 6.125% (2,000) secured notes |
| Thereafter | 6,269 | US$m | As printed; 2031 to 2034 notes. Table total 13,341 includes finance leases, mortgages and other notes of 679; revolver (undrawn) matures November 4, 2030 subject to a springing date |

### Financials and credit metrics

| Metric | FY2024 | FY2025 | 9M 2025 | 9M 2026 | LTM Q3 2026 | Source and basis |
| --- | --- | --- | --- | --- | --- | --- |
| Net operating revenues | 20,675 | 21,310 | 15,783 | 16,627 | 22,154 | 10-K page:118; Q3 10-Q page:2; excludes revenue from contract termination; LTM calculated |
| Revenue from contract termination | No line printed | No line printed | Printed as nil dash | 1,472 | Not calculable: no FY2025 line | Q3 10-Q page:2; separate statement line |
| Operating income | 5,956 | 3,508 | 2,655 | 4,547 | 5,400 | 10-K page:118; Q3 10-Q page:3; 9M 2026 includes termination revenue; FY2024 includes a 2,916 net gain on sales |
| Adjusted EBITDA (management non-GAAP) | 3,995 | 4,566 | 3,383 | 3,821 | 5,004 | 10-K page:174; Q3 10-Q page:24 and page:25; consolidated before noncontrolling interests; LTM calculated |
| Adjusted EBITDA margin | 19.3% | 21.4% | 21.4% | 23.0% | 22.6% | Calculated on net operating revenues above |
| Interest expense | 826 | 821 | 616 | 612 | 817 | 10-K page:118; Q3 10-Q page:3; LTM calculated |
| Interest paid, net of capitalized interest | 851 | 865 | 499 | 464 | 830 | 10-K page:121; Q3 10-Q page:4; shown as positive outflow |
| Net income available to common shareholders | 3,200 | 1,407 | 1,036 | 2,528 | 2,899 | 10-K page:119; Q3 10-Q page:3; LTM calculated |
| Net cash provided by operating activities | 2,047 | 3,540 | 2,809 | 3,507 | 4,238 | 10-K page:120; Q3 10-Q page:4; 9M 2026 includes 540 contract-termination receipts |
| Purchases of property and equipment | 931 | 1,010 | 646 | 546 | 910 | 10-K page:120; Q3 10-Q page:4 |
| Operating cash flow less capex | 1,116 | 2,530 | 2,163 | 2,961 | 3,328 | Calculated; 2,788 LTM excluding the 540 receipt |
| Distributions paid to noncontrolling interests | 681 | 809 | 585 | 614 | 838 | 10-K page:120; Q3 10-Q page:4; financing cash flow |
| Repurchases of common stock | 672 | 1,386 | 1,188 | 1,615 | 1,813 | 10-K page:120; Q3 10-Q page:4; cash-flow basis |
| Cash and cash equivalents (period end) | 3,019 | 2,883 | 2,975 | 2,674 | 2,674 | 10-K page:118; Q3 10-Q page:2 and page:4 |
| Total long-term debt, carrying (period end) | 13,173 | 13,171 | Not supplied: September 30, 2025 balance sheet is not in the pack | 13,243 | 13,243 | 10-K page:144; Q3 10-Q page:12; includes current portion and finance leases, net of discounts |
| Net debt (period end) | 10,154 | 10,288 | Not supplied: same reason | 10,569 | 10,569 | Calculated: carrying debt less cash |
| Total debt / Adjusted EBITDA | 3.30x | 2.88x | Not calculable | Not calculable | 2.65x | Calculated; annual and LTM only |
| Net debt / Adjusted EBITDA | 2.54x | 2.25x | Not calculable | Not calculable | 2.11x | Calculated; matches management's 2.25x and 2.11x |
| Adjusted EBITDA / cash interest | 4.69x | 5.28x | Not calculable | Not calculable | 6.03x | Calculated |
| Redeemable noncontrolling interests (period end) | 2,727 | 2,956 | Not supplied: same reason | 2,179 | 2,179 | 10-K page:118; Q3 10-Q page:2; outside debt |
| Noncontrolling interests in equity (period end) | 1,649 | 1,797 | Not supplied: same reason | 1,971 | 1,971 | 10-K page:118; Q3 10-Q page:2 |

### Debt structure at September 30, 2026

| Instrument | Amount | Ranking and note |
| --- | --- | --- |
| 6.125% senior unsecured notes due 2028 | 1,250 | Unsecured; 1,750 at December 31, 2025, 500 redeemed in September 2026 |
| 6.875% senior unsecured notes due 2031 | 362 | Unsecured; New York Stock Exchange listed as THC31 |
| 6.000% senior unsecured notes due 2033 | 750 | Unsecured |
| 6.250% senior unsecured notes due 2034 | 2,000 | Unsecured; issued September 2026; first coupon March 15, 2027 |
| 4.625% senior secured first lien notes due 2028 | 600 | First lien |
| 4.250% senior secured first lien notes due 2029 | 1,400 | First lien |
| 4.375% senior secured first lien notes due 2030 | 1,450 | First lien |
| 6.125% senior secured first lien notes due 2030 | 2,000 | First lien |
| 6.750% senior secured first lien notes due 2031 | 1,350 | First lien |
| 5.500% senior secured first lien notes due 2032 | 1,500 | First lien |
| Finance leases, mortgages and other notes | 679 | Classification by ranking not supplied |
| Unamortized issue costs and note discounts | (98) | Deduction |
| Total long-term debt | 13,243 | Current portion 164; long-term 13,079 |
| Senior secured revolving credit facility, 1,900 | 0 drawn | Asset-based; borrowing base of receivables, inventory and Medicaid supplemental payments |
| Letter of credit facility, 200 | 105 standby letters of credit outstanding | Not a source of cash liquidity |

### Latest quarter and after

- Refinancing, September 2026: Tenet issued 2,000 of 6.250% senior unsecured notes due September 2034 and used the proceeds with cash on hand to redeem all 1,500 of 5.125% senior secured first lien notes due November 2027 and 500 of the 1,750 of 6.125% senior unsecured notes due October 2028 (Q3 10-Q page:13). A loss from early extinguishment of debt of 5 was booked in Q3 2026 (Q3 10-Q page:3). The Forty-Third Supplemental Indenture is dated September 22, 2026 (Q3 10-Q page:53).
- Revolver: availability 1,900, no cash borrowings (Q3 10-Q page:13). No amendment to the revolver in 2026 is described in the located text.
- Conifer: the transition of certain revenue cycle services occurred in Q3 2026 and was to be substantially complete by October 30, 2026, with cumulative catch-up adjustments of 233 to revenue from contract termination and 97 to net operating revenues (release page:2); these are management statements dated October 29, 2026.
- Share count: 79,588 thousand shares outstanding at October 23, 2026 (Q3 10-Q page:1). Q3 2026 repurchases were 970 thousand shares for 255 (release page:2).
- Acquisitions: 201 of cash used for acquisition-related activity in 9M 2026 (Q3 10-Q page:23).
- Management outlook (not filed evidence): FY2026 Adjusted EBITDA 5,050 to 5,200, raised by 195 at the midpoint; interest expense 815 to 825; capital expenditures 700 to 800 (October release, page:1 for the raise and page:4 for the ranges).
- Subsequent events: the Q3 10-Q describes no event after September 30, 2026 other than the share count date. Events from October 30, 2026 to the cutoff are Not supplied.

### Claims outside the debt figure

- Operating lease liabilities: 1,257 at December 31, 2025 (current 214, long-term 1,043), inside other liabilities, not debt (10-K page:143). No September 30, 2026 balance is supplied.
- Finance lease liabilities of 452 at December 31, 2025 are already inside long-term debt (10-K page:143).
- Redeemable noncontrolling interests: 2,179 at September 30, 2026, of which Ambulatory Care 2,134 and Hospital Operations 45 (Q3 10-Q page:20). Put-right terms are not supplied in the located text.
- Professional and general liability reserves: 317 current and 979 long-term; defined benefit plan obligations 238 (Q3 10-Q page:2). Pension funded status is not supplied.
- CHI Note Receivable (an asset, not a liability): 434 current plus 828 long-term at carrying value, payable in annual installments of about 453 (Q3 10-Q page:10).
- Revenue and collection guarantees to physicians: maximum potential payments 328, liability recorded 290; guarantees of investee debt about 83 (Q3 10-Q page:13).
- Share repurchase authorization remaining: 1,875 at September 30, 2026 (Q3 10-Q page:53). The board added 2,000 of authorization in June 2026 (same page).

### Covenants and structure (dated December 31, 2025)

- Secured notes indentures limit secured debt by a secured debt ratio of 4.00 to 1.00 (10-K page:148, "the secured debt ratio (as defined in the indentures) to exceed 4.00 to"; the sentence continues on page:149). The indenture definition is not supplied, so reported headroom is Not calculable; first-lien notes of 8,300 over LTM Adjusted EBITDA of 5,004 is 1.66x on this report's own simple basis, not the indenture ratio.
- The letter of credit facility has an "effective maximum secured debt covenant of 4.25 to 1.00" (10-K page:148).
- The revolver has a minimum fixed charge coverage ratio "to be met if the designated excess availability under the revolving credit facility falls below $150 million" (10-K page:149). Availability is 1,900, so the test is not engaged on the printed figures.
- Cash dominion applies if unused availability falls below 200 for three consecutive business days (10-K page:149).
- The company states compliance with all applicable covenants at September 30, 2026 (Q3 10-Q page:51).
- Springing maturity: the revolver terminates on the earlier of November 4, 2030 or 45 business days before certain 2028 and 2027 to 2030 note maturities unless extended, repaid, refinanced or an excess availability condition is met (10-K page:147). The 6.125% unsecured notes due 2028 remain outstanding at 1,250, so the clause is relevant; its exact operation needs the executed agreement.
- Change of control: senior secured notes carry a 101% purchase right (10-K page:146).

### Correction to the earlier handoff

The source-readiness handoff stated that the reported net-debt ratio could not be rebuilt because no net-debt figure or definition is supplied. That remains true of the definition, but the ratio can be reproduced: carrying long-term debt less balance-sheet cash over LTM Adjusted EBITDA gives 2.25x at December 31, 2025, 2.33x at June 30, 2026 and 2.11x at September 30, 2026, equal to the three ratios in the release. This report therefore uses those inputs and labels the ratio as reproduced, not as defined by the issuer.

### Interpretation

- Deleveraging comes from both sides. Total debt is nearly flat between December 31, 2025 and September 30, 2026 (13,171 to 13,243) while LTM Adjusted EBITDA rose from 4,566 to 5,004, so the move in leverage is earnings-driven, not repayment-driven.
- Earnings quality: 9M 2026 operating income of 4,547 includes 1,472 of contract-termination revenue that management excludes from Adjusted EBITDA. Adjusted EBITDA for Q3 2026 of 1,355 includes a 147 favorable net impact attributed to revenue-cycle transition timing (release page:2). Excluding it, LTM Adjusted EBITDA would be 4,857 and leverage 2.73x total and 2.18x net, as a sensitivity and not a reported figure.
- Minority leakage: ambulatory surgery earnings are partly owned by physicians and partners. Cash distributions to noncontrolling holders of 838 over the LTM period are real cash leaving the group before debt service. On Adjusted EBITDA less those distributions (4,166), total debt is 3.18x and net debt 2.54x.
- Free cash flow: operating cash flow less capex of 3,328 for the LTM period includes the 540 CommonSpirit receipt, which was offset against a payment due to CommonSpirit that sits in financing cash flows. Excluding it, 2,788.
- Capital allocation: in 9M 2026 buybacks of 1,615, purchases of noncontrolling interests of 583 and distributions to noncontrolling interests of 614 total 2,812, against operating cash flow less capex of 2,961 that itself includes the 540 receipt. Cash fell from 2,883 to 2,674 over the period. The CommonSpirit agreement offset 540 owed to CommonSpirit against the amount it owed Tenet (Q3 10-Q page:5), so the receipt and the matching redemption payment inflate both operating inflows and financing outflows.
- Seasonality: Q3 2026 interest expense of 203 compares with Q3 cash interest of 99 (9M 2026 464 less H1 2026 365) because notes pay semi-annually; accrued interest payable rose from 81 to 213 (Q3 10-Q page:2). Any quarterly coverage ratio would mislead; the LTM basis is used.

## Calculations

All inputs are USD millions from the locators shown. LTM Q3 2026 = FY2025 + 9M 2026 - 9M 2025.

| Calculation | Inputs | Result |
| --- | --- | --- |
| LTM net operating revenues | 21,310 + 16,627 - 15,783 | 22,154 |
| LTM Adjusted EBITDA | 4,566 + 3,821 - 3,383 | 5,004 |
| FY2025 Adjusted EBITDA check | 21,310 + 264 - 8,705 - 3,780 - 4,523 | 4,566 (agrees to 10-K page:174) |
| LTM cash interest paid | 865 + 464 - 499 | 830 |
| LTM interest expense | 821 + 612 - 616 | 817 |
| LTM operating income | 3,508 + 4,547 - 2,655 | 5,400 |
| LTM operating cash flow | 3,540 + 3,507 - 2,809 | 4,238 |
| LTM capex | 1,010 + 546 - 646 | 910 |
| LTM operating cash flow less capex | 4,238 - 910 | 3,328 |
| LTM less contract-termination receipt | 3,328 - 540 | 2,788 |
| LTM noncontrolling distributions | 809 + 614 - 585 | 838 |
| LTM net income to common | 1,407 + 2,528 - 1,036 | 2,899 |
| LTM repurchases of common stock | 1,386 + 1,615 - 1,188 | 1,813 |
| Net debt, December 31, 2024 | 13,173 - 3,019 | 10,154 |
| Net debt, December 31, 2025 | 13,171 - 2,883 | 10,288 |
| Net debt, June 30, 2026 | 13,248 - 2,170 | 11,078 |
| Net debt, September 30, 2026 | 13,243 - 2,674 | 10,569 |
| Total debt / EBITDA, FY2024 | 13,173 / 3,995 | 3.2974, shown 3.30x |
| Total debt / EBITDA, FY2025 | 13,171 / 4,566 | 2.8846, shown 2.88x |
| Total debt / EBITDA, LTM Q3 2026 | 13,243 / 5,004 | 2.6465, shown 2.65x |
| Net debt / EBITDA, FY2024 | 10,154 / 3,995 | 2.5417, shown 2.54x |
| Net debt / EBITDA, FY2025 | 10,288 / 4,566 | 2.2532, shown 2.25x |
| Net debt / EBITDA, LTM Q3 2026 | 10,569 / 5,004 | 2.1121, shown 2.11x |
| LTM Adjusted EBITDA at June 30, 2026 (check of 2.33x) | 4,566 + 2,466 - 2,284 = 4,748; 11,078 / 4,748 | 2.3332, shown 2.33x |
| Cover FY2024 | 3,995 / 851 | 4.6945, shown 4.69x |
| Cover FY2025 | 4,566 / 865 | 5.2786, shown 5.28x |
| Cover LTM Q3 2026 | 5,004 / 830 | 6.0289, shown 6.03x |
| Adjusted EBITDA margin | 3,995 / 20,675; 4,566 / 21,310; 3,383 / 15,783; 3,821 / 16,627; 5,004 / 22,154 | 19.3%, 21.4%, 21.4%, 23.0%, 22.6% |
| Liquidity, September 30, 2026 | 2,674 + 1,900 | 4,574 |
| Liquidity, December 31, 2025 | 2,883 + 1,900 | 4,783 |
| Sensitivity: LTM Adjusted EBITDA less 147 | 5,004 - 147 = 4,857; 13,243 / 4,857; 10,569 / 4,857 | 2.7266 and 2.1760, shown 2.73x and 2.18x |
| Sensitivity: EBITDA less noncontrolling distributions | 5,004 - 838 = 4,166; 13,243 / 4,166; 10,569 / 4,166 | 3.1788 and 2.5370, shown 3.18x and 2.54x |
| Notes principal | 4,362 unsecured + 8,300 first lien | 12,662 (agrees to Q3 10-Q page:13 "$12.662 billion") |
| First-lien notes / LTM EBITDA | 8,300 / 5,004 | 1.6587, shown 1.66x |
| Debt table total | 12,662 + 679 - 98 | 13,243 (agrees to page:12) |
| Maturity table total | 27 + 157 + 1,931 + 1,464 + 3,493 + 6,269 | 13,341 (agrees to page:52); equals 13,243 plus discounts 98 |
| Q3 2026 discrete operating cash flow | 3,507 - 2,226 | 1,281 |
| Q3 2026 discrete cash interest | 464 - 365 | 99 |
| Q3 2026 discrete capex | 546 - 348 | 198 (agrees to segment note) |
| 9M 2026 financing uses cited above | 1,615 + 583 + 614 | 2,812 |
| 9M 2026 operating cash flow less capex | 3,507 - 546 | 2,961 |

## Gaps

| Gap | Severity | Effect | Action |
| --- | --- | --- | --- |
| Executed credit agreement, LC facility and indentures not supplied; covenant definitions and headroom not calculable | High for covenant work | Cannot compute secured debt ratio or fixed charge test | Supply executed documents |
| Covenant text is dated December 31, 2025; the Q3 2026 report only states compliance | Medium | Later amendments invisible | Supply amendments and the September 22, 2026 supplemental indenture |
| Net debt definition not printed by the issuer; ratio reproduced from carrying debt less cash | Medium | Definition risk (for example restricted cash, leases) | Supply supplemental disclosures |
| Q3 2025 10-Q not in pack; September 30, 2025 balance sheet other than cash not supplied | Low | No September 2025 leverage point | Not required for LTM at September 30, 2026 |
| Operating lease liabilities and pension funded status not updated after December 31, 2025 | Low to Medium | Lease-adjusted leverage dated | Use December 31, 2025 values labelled as such |
| Terms of put rights on redeemable noncontrolling interests of 2,179 not supplied | Medium | Possible cash call not sized | Supply put terms |
| Exact standby letters of credit under the revolver (printed only as less than $1 million) not printed | Low | Undrawn facility overstated by under 1 | None needed |
| Transition benefit of 147 is a management attribution without a filed split | Medium | Underlying Adjusted EBITDA is a sensitivity only | Supply the supplemental disclosures |
| No FY2025 contract-termination line; LTM of that line not calculable | Low | Not needed for Adjusted EBITDA, which excludes it | None |
| Text conversion only; no XBRL | Low | Table layout risk | Check against filed HTML |

## Next module

- CP-1A: carry the Conifer and CommonSpirit agreements, the CHI Note Receivable, the September 2026 refinancing, the Q3 2026 transition benefit and the rising buyback pace as the transaction and operating context. Keep noncontrolling interests in view when describing Ambulatory Care economics.
- CP-2: use the leverage, cover and liquidity rows above with the Medium confidence stated; treat 2.65x and 2.11x as headline, and 2.73x and 2.18x and 3.18x and 2.54x as sensitivities; carry covenant headroom as Not calculable.
- CP-5: trace every figure to the locators named; the net-debt ratio is reproduced here, not issuer-defined.
