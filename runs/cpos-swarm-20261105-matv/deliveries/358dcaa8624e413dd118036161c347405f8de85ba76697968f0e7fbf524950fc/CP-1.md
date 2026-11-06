## Request

Module: financial base and credit metrics for Mativ Holdings, Inc. (ticker MATV, issuer id matv), pathway credit_snapshot, as-of date 2026-11-05 (cutoff 2026-11-05). Reporting currency USD, in millions (US$m) unless a line says otherwise. Current period Q3 2026 (three and nine months ended September 30, 2026); prior period FY2025 (year ended December 31, 2025). Perimeter: Mativ Holdings, Inc. and its consolidated subsidiaries, the registrant that files the statements; there is no separate borrower or parent reporting entity in the sources. Nothing dated after 2026-11-05 is used as fact.

The module extracts the statement lines the credit view needs, builds the debt, liquidity, covenant and off-debt claim registers, and computes leverage and cover on stated bases. It hands readiness, limits and gaps to the next modules. Abbreviations used in locators: 10-K is the FY2025 annual report; 10-Q Q1, Q2 and Q3 are the 2026 quarterly reports; Release Q1, Q2 and Q3 are the 2026 earnings release exhibits; `page:N` is the source chunk number, not the printed page.

## Sources

### Issuer sources relied on

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_matv-20251231.htm.jsonl | 0987bdd177918d1704e3f88d583ff72f6a39e66a94dd95882dba466d3888311c |
| 10-Q_2026-03-31_matv-20260331.htm.jsonl | be2515741fe2f13e179c4c2e30c15996c434ad9db582dc94e1ef7a9b4954e68d |
| 10-Q_2026-06-30_matv-20260630.htm.jsonl | 7184a20d311477dd5cb1dfc9b30dba5f1ea74b357d6c5b8b24327bc29eea17ff |
| 10-Q_2026-09-30_matv-20260930.htm.jsonl | cd05c1595b274a699b4cdcd913ff17f3c1b042cf31d245b0741f58eac17a20fb |
| EX-99.1_2026-05-06_ex991earningsrelease2026q1.htm.jsonl | 9f2d35ab42751d0b53917904e34ca17dd018903790ffb5f1f2e30283805e8933 |
| EX-99.1_2026-08-05_ex991earningsrelease2026q2.htm.jsonl | 6cdc4bf84d342bfc79bbfbfa3bbc0faf89dc1156b59bfb476359102520bc07e0 |
| EX-99.1_2026-11-04_ex991earningsrelease2026q3.htm.jsonl | 1d8a4657f455e3276abc49c4e3ccf64e82f7d0ab6a0f632c1c495bd5b53fcf53 |

### Run context (settings, not issuer evidence)

| Source name | sha256 |
| --- | --- |
| context (1000623-mativ-holdings-inc-matv.json) | 43cba5e2e4b206f93654450fc247b91671c4b4e4ab36f2ccb3891319991c5f21 |

### Handoffs relied on

| Handoff module | sha256 |
| --- | --- |
| CP-0 | 92a14b77ed2bb9def0944723f4f65aeedad508eab324c95320e6d76a3b3d4ee9 |

Authority: filed statements (10-K audited; 10-Qs unaudited) control; the earnings releases supply management measures (adjusted EBITDA, free cash flow, net debt, total liquidity) as attributed claims. Statement values were read from the page text and checked by tie-outs in Calculations; no image or chart content exists in the pack.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported leverage has fallen since the April 2026 refinancing, but on a reported earnings basis it is still above four times and interest cover is thin. Liquidity is adequate, though the revolver is smaller. | Medium | Management leverage uses an adjusted earnings definition and agreement text that are not in the sources, so covenant headroom cannot be tested. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The April 2026 refinancing pushed the bank maturities out and removed the 2027 wall, leaving the 8.000% notes due 2029 as the main bullet. | Near-term refinancing risk is low, but a 2029 refinancing of the notes is the key event. | Medium |
| Net debt fell and management reports net leverage of 3.8x against a 5.00x maximum that steps down toward 4.00x. | Headroom is comfortable today and thins at the final step-down, whose timing is not supplied. | Medium |
| On reported earnings the trailing interest cover is 2.62x on cash interest, and the quarter was hit by the July tornado. | Cover is modest, and most of the insured inventory loss is still a receivable rather than cash. | Medium |
| Cash flow is positive but leans on receivable sales, a tax refund and a working capital inflow. | Cash generation quality is weaker than the headline free cash flow suggests. | Medium |

### Financial base view

For Mativ Holdings, Inc. the financial base at September 30, 2026 is a company with USD 1,510.9 million of nine-month net sales (nine months 2026), gross profit up year on year for the nine months (though down in Q3), a thin operating margin and a net loss close to break-even for the nine months (net loss of 9.3 against a prior-year loss of 438.2 that carried an 411.9 goodwill impairment), financed by 976.4 of total debt (carrying value, net of 34.7 issuance costs; principal 1,011.1) against cash and cash equivalents of 97.3, so reported net debt of 879.1. The structure was reset on April 3, 2026 by the Ninth Amendment: a 305.0 revolver (20.0 drawn), an 89.9 Term Loan A, a 500.0 Term Loan B and the unchanged 400.0 of 8.000% senior unsecured notes due October 1, 2029. Management states net leverage of 3.8x at September 30, 2026 against a current maximum of 5.00x, down from 4.2x at December 31, 2025 and 4.1x at March 31, 2026.

The reported-basis measures built here are lower quality than management's: operating profit plus depreciation and amortization (with the 411.9 FY2025 goodwill impairment added back) gives trailing EBITDA of 210.0 at Q3 2026, so total debt to EBITDA is 4.65x and net debt to EBITDA is 4.19x, with EBITDA to cash interest of 2.62x. These are above management's 3.8x because the credit agreement and management adjusted EBITDA add back items such as stock compensation, restructuring, financing fees on the receivables program and purchase-accounting items; that definition is not supplied, so the two cannot be reconciled and neither is restated into the other. Evidence to risk to implication: a lender that sizes debt on the adjusted figure sees a levered but compliant credit; a lender that sizes it on reported earnings sees a leverage multiple that only recently dropped below five times, which makes the 2029 notes refinancing and the covenant step-downs the focus.

Liquidity is cash of 97.3 plus printed undrawn revolver capacity of 276.2, total 373.5, down from 498.5 at March 31, 2026 because the revolver was cut from 600.0 to 305.0. On the maturity table's reading nothing in the debt falls due before 2029 except 2.2 in the rest of 2026 and small amortization. Claims outside the debt figure are meaningful: a receivables sale program (837.3 sold in nine months 2026, balance outstanding not supplied), a foreign exchange contract liability of 27.6 in other liabilities (the euro cross-currency swap hedges are disclosed alongside), pension and other postretirement liabilities of 49.1, operating leases of 56.2, finance leases of 14.7 non-current, purchase obligations of 105.1 at year-end 2025, and open insurance recovery on the July 27, 2026 Menasha tornado (expense of 43.8 less recoveries received 5.0 and receivable 38.0, leaving a 0.8 net loss recorded). The view is restricted by the absence of the credit agreement, the indenture, the receivables agreement and any annual adjusted EBITDA.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (December 31, 2025) | 6.04 | 5.54 | x | Reported basis: FY2025 operating profit plus cash flow D&A plus the 411.9 goodwill impairment = 168.5 (10-K page:75, page:77). Total debt 1,018.2 and net debt 934.0 (10-K page:99; Release Q1 page:10). Management states net leverage of 4.2x on its definition (10-K page:63). Not an adjusted or covenant figure. |
| LTM Q1 2026 (March 31, 2026) | 5.34 | 4.91 | x | Reported basis, EBITDA 194.0 from FY2025 less Q1 2025 plus Q1 2026 (10-Q Q1 page:2, page:3). Total debt 1,035.8 and net debt 953.5 (10-Q Q1 page:10; Release Q1 page:10). Management states 4.1x (10-Q Q1 page:26). |
| LTM Q2 2026 (June 30, 2026) | 4.69 | 4.37 | x | Reported basis, EBITDA 207.7 from FY2025 less six months 2025 plus six months 2026 (10-Q Q2 page:2, page:4). Total debt 974.5 and net debt 908.2 (10-Q Q2 page:11; Release Q2 page:11). Management states 3.8x (10-Q Q2 page:27). |
| LTM Q3 2026 (September 30, 2026) | 4.65 | 4.19 | x | Reported basis, EBITDA 210.0 from FY2025 less nine months 2025 plus nine months 2026 (10-Q Q3 page:2, page:4; 10-K page:75, page:77). Total debt 976.4 and net debt 879.1 (10-Q Q3 page:12; Release Q3 page:11). Management states 3.8x (10-Q Q3 page:28). Adjusted LTM EBITDA Not calculable: no fourth quarter 2025 adjusted figure. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 (year ended December 31, 2025) | 2.04 | x | Reported-basis EBITDA 168.5 over cash paid for interest of 82.8 (10-K page:78). Cash interest is net of interest received. Covenant definition differs (not supplied). |
| LTM Q1 2026 | 2.41 | x | EBITDA 194.0 over LTM cash interest 80.5 (FY2025 82.8 less Q1 2025 13.2 plus Q1 2026 10.9; 10-Q Q1 page:4). |
| LTM Q2 2026 | 2.58 | x | EBITDA 207.7 over LTM cash interest 80.6 (82.8 less 42.4 plus 40.2; 10-Q Q2 page:5). |
| LTM Q3 2026 | 2.62 | x | EBITDA 210.0 over LTM cash interest 80.1 (82.8 less 55.2 plus 52.5; 10-Q Q3 page:5). On interest expense instead of cash interest the ratio is 2.92x (LTM expense 71.9). Management basis for nine months 2026 only: adjusted EBITDA 184.8 over cash interest 52.5 is 3.52x (not a trailing figure). |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| December 31, 2025 | 84.2 | 431.2 | US$m | Cash and cash equivalents excluding restricted cash of 5.6 (10-K page:76). Undrawn capacity as printed on the old 600.0 revolver (10-K page:63). |
| March 31, 2026 | 82.3 | 416.2 | US$m | Printed undrawn capacity on the old 600.0 revolver, before the April 3, 2026 amendment (10-Q Q1 page:26); restricted cash 5.0 excluded (10-Q Q1 page:2). |
| June 30, 2026 | 66.3 | 279.2 | US$m | Printed undrawn capacity on the 305.0 revolver (10-Q Q2 page:27); restricted cash 4.5 excluded. |
| September 30, 2026 | 97.3 | 276.2 | US$m | Printed undrawn capacity on the 305.0 revolver (10-Q Q3 page:28); restricted cash 4.2 excluded (UK pension scheme, 10-Q Q3 page:27). Of the cash, 72.7 is held by foreign subsidiaries (10-Q Q3 page:27). Printed capacity is 8.8 below commitment less drawings at every date; the cause (letters of credit or other usage) is not supplied. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 (October to December) | 2.2 | US$m | Expected maturities at September 30, 2026, principal before 34.7 of issuance costs (10-Q Q3 page:14). Table total 1,011.1. |
| 2027 | 6.6 | US$m | Same table (10-Q Q3 page:14). Amortization-sized amount only; the old May 2027 bank maturity wall was removed by the Ninth Amendment. |
| 2028 | 6.1 | US$m | Same table. |
| 2029 | 406.2 | US$m | Same table; the 400.0 8.000% notes due October 1, 2029 plus small amortization. Note 8 wording on the revolver and Term Loan A maturity (earlier of five years or 182 days before the notes' maturity) could place them in 2029 instead of later; the table does not (10-Q Q3 page:13, page:14). Unresolved. |
| 2030 | 6.2 | US$m | Same table. |
| Thereafter | 583.8 | US$m | Same table; Term Loan B and, on the table's reading, the revolver and Term Loan A. Release Q3 page:3 says debt matures on a staggered basis through 2033. |

### Financials and credit metrics

| Metric | Period | Value | Unit | Basis and locator |
| --- | --- | --- | --- | --- |
| Net sales | Q3 2026 | 499.5 | US$m | Three months ended Sep 30, 2026; 10-Q Q3 page:2 |
| Net sales | Q3 2025 | 513.7 | US$m | 10-Q Q3 page:2 |
| Net sales | 9M 2026 | 1510.9 | US$m | Nine months; 10-Q Q3 page:2 |
| Net sales | 9M 2025 | 1523.9 | US$m | 10-Q Q3 page:2 |
| Net sales | FY2025 | 1987.0 | US$m | 10-K page:75 |
| Net sales | LTM Q3 2026 | 1974.0 | US$m | Calculated: 1,987.0 - 1,523.9 + 1,510.9 |
| Gross profit | Q3 2026 | 97.7 | US$m | 10-Q Q3 page:2 |
| Gross profit | Q3 2025 | 99.4 | US$m | 10-Q Q3 page:2 |
| Gross profit | 9M 2026 | 295.9 | US$m | 10-Q Q3 page:2 |
| Gross profit | 9M 2025 | 275.7 | US$m | 10-Q Q3 page:2 |
| Gross profit | FY2025 | 362.9 | US$m | 10-K page:75 |
| Operating profit | Q3 2026 | 19.9 | US$m | 10-Q Q3 page:2 |
| Operating profit | Q3 2025 | 16.0 | US$m | 10-Q Q3 page:2 |
| Operating profit (loss) | 9M 2026 | 62.5 | US$m | 10-Q Q3 page:2 |
| Operating profit (loss) | 9M 2025 | -394.5 | US$m | After 411.9 goodwill impairment; 10-Q Q3 page:2 |
| Operating profit (loss) | FY2025 | -384.4 | US$m | After 411.9 goodwill impairment; 10-K page:75 |
| Interest expense | Q3 2026 | 18.1 | US$m | 10-Q Q3 page:2 |
| Interest expense | 9M 2026 | 54.9 | US$m | 10-Q Q3 page:2 |
| Interest expense | 9M 2025 | 54.1 | US$m | 10-Q Q3 page:2 |
| Interest expense | FY2025 | 71.1 | US$m | 10-K page:75 |
| Loss on debt extinguishment | 9M 2026 | 8.7 | US$m | Recorded in Q2 2026 on the refinancing; 10-Q Q3 page:2, page:13 |
| Net loss | Q3 2026 | -1.2 | US$m | 10-Q Q3 page:2 |
| Net loss | Q3 2025 | -3.2 | US$m | 10-Q Q3 page:2 |
| Net loss | 9M 2026 | -9.3 | US$m | 10-Q Q3 page:2 |
| Net loss | 9M 2025 | -438.2 | US$m | 10-Q Q3 page:2 |
| Net loss | FY2025 | -337.4 | US$m | Includes income tax benefit of 125.6; 10-K page:75 |
| Depreciation and amortization | 9M 2026 | 102.7 | US$m | Cash flow statement; 10-Q Q3 page:4 |
| Depreciation and amortization | 9M 2025 | 106.3 | US$m | 10-Q Q3 page:4 |
| Depreciation and amortization | FY2025 | 141.0 | US$m | 10-K page:77 |
| Adjusted EBITDA (management) | Q3 2026 | 62.3 | US$m | Non-GAAP, management measure; Release Q3 page:11 |
| Adjusted EBITDA (management) | Q3 2025 | 66.8 | US$m | Release Q3 page:11 |
| Adjusted EBITDA (management) | 9M 2026 | 184.8 | US$m | Release Q3 page:11 |
| Adjusted EBITDA (management) | 9M 2025 | 171.2 | US$m | Release Q3 page:11 |
| Adjusted EBITDA margin (management) | Q3 2026 | 12.5 | percent | Printed, Release Q3 page:10 |
| Adjusted EBITDA margin (management) | 9M 2026 | 12.2 | percent | Printed, Release Q3 page:10 |
| EBITDA, reported basis | LTM Q3 2026 | 210.0 | US$m | Calculated: operating profit 72.6 plus D&A 137.4; see Calculations |
| EBITDA, reported basis | FY2025 | 168.5 | US$m | Calculated: -384.4 + 141.0 + 411.9 |
| Cash and cash equivalents | Sep 30, 2026 | 97.3 | US$m | 10-Q Q3 page:2 |
| Cash and cash equivalents | Dec 31, 2025 | 84.2 | US$m | 10-Q Q3 page:2; 10-K page:76 |
| Restricted cash | Sep 30, 2026 | 4.2 | US$m | UK pension scheme contributions; 10-Q Q3 page:2, page:27 |
| Accounts receivable, net | Sep 30, 2026 | 250.3 | US$m | Includes the 38.0 tornado insurance receivable; 10-Q Q3 page:2, page:18 |
| Inventories, net | Sep 30, 2026 | 329.1 | US$m | Unchanged from Dec 31, 2025; 10-Q Q3 page:2 |
| Total assets | Sep 30, 2026 | 2030.5 | US$m | 10-Q Q3 page:3 |
| Total debt (carrying) | Sep 30, 2026 | 976.4 | US$m | Net of 34.7 issuance costs; 10-Q Q3 page:12 |
| Total debt (carrying) | Dec 31, 2025 | 1018.2 | US$m | 10-Q Q3 page:12; 10-K page:99 |
| Debt principal | Sep 30, 2026 | 1011.1 | US$m | Maturity table total; 10-Q Q3 page:14 |
| Current debt | Sep 30, 2026 | 3.8 | US$m | 10-Q Q3 page:3 |
| Net debt (management) | Sep 30, 2026 | 879.1 | US$m | Total debt less cash and cash equivalents; Release Q3 page:11 |
| Net debt (management) | Dec 31, 2025 | 934.0 | US$m | Release Q3 page:11 |
| Finance lease liabilities, noncurrent | Sep 30, 2026 | 14.7 | US$m | Outside the debt figure; current portion not shown separately in the 10-Q; 10-Q Q3 page:3 |
| Operating lease liabilities (current + noncurrent) | Sep 30, 2026 | 56.2 | US$m | 8.8 + 47.4; outside the debt figure; 10-Q Q3 page:3 |
| Pension and other postretirement benefits liability | Sep 30, 2026 | 49.1 | US$m | Outside the debt figure; 10-Q Q3 page:3 |
| Other liabilities | Sep 30, 2026 | 42.9 | US$m | Includes 27.6 of foreign exchange contract liability; 10-Q Q3 page:3, page:16 |
| Total stockholders' equity | Sep 30, 2026 | 467.1 | US$m | 10-Q Q3 page:3 |
| Total liquidity (management) | Sep 30, 2026 | 373.5 | US$m | 97.3 cash plus 276.2 revolver availability; Release Q3 page:3 |
| Net cash provided by operations | 9M 2026 | 117.4 | US$m | 10-Q Q3 page:4 |
| Net cash provided by operations | 9M 2025 | 114.5 | US$m | 10-Q Q3 page:4 |
| Net cash provided by operations | Q3 2026 | 48.5 | US$m | 10-Q Q3 page:24 |
| Net cash provided by operations | Q3 2025 | 72.8 | US$m | 10-Q Q3 page:24 |
| Capital spending | 9M 2026 | 26.9 | US$m | 10-Q Q3 page:4 |
| Capital spending | Q3 2026 | 11.0 | US$m | 10-Q Q3 page:24 |
| Free cash flow (management) | 9M 2026 | 90.5 | US$m | Operations less capital spending; Release Q3 page:11 |
| Free cash flow (management) | 9M 2025 | 85.8 | US$m | Release Q3 page:11 |
| Free cash flow (management) | Q3 2026 | 37.5 | US$m | Release Q3 page:11 |
| Free cash flow (management) | Q3 2025 | 66.7 | US$m | Release Q3 page:11 |
| Cash dividends paid | 9M 2026 | 17.0 | US$m | 10-Q Q3 page:4 |
| Cash paid for interest, net | 9M 2026 | 52.5 | US$m | 10-Q Q3 page:5 |
| Cash paid for interest, net | 9M 2025 | 55.2 | US$m | 10-Q Q3 page:5 |
| Cash paid (received) for taxes, net | 9M 2026 | -2.2 | US$m | Net refund received; 10-Q Q3 page:5 |
| Cash paid (received) for taxes, net | 9M 2025 | 9.4 | US$m | 10-Q Q3 page:5 |
| Net leverage under the credit agreement (management) | Sep 30, 2026 | 3.8 | x | Against a current maximum of 5.00x; 10-Q Q3 page:28 |
| Total debt to capital under the credit agreement | Sep 30, 2026 | 67.6 | percent | 10-Q Q3 page:29 |
| Total debt / EBITDA, reported basis | LTM Q3 2026 | 4.65 | x | Calculated: 976.4 / 210.0 |
| Net debt / EBITDA, reported basis | LTM Q3 2026 | 4.19 | x | Calculated: 879.1 / 210.0 |
| EBITDA / cash interest, reported basis | LTM Q3 2026 | 2.62 | x | Calculated: 210.0 / 80.1 |
| Free cash flow after dividends | 9M 2026 | 73.5 | US$m | Calculated: 90.5 - 17.0 |

### Debt register at September 30, 2026

| Instrument | Issuer or borrower | Amount (US$m) | Rate and terms | Maturity | Security and guarantors | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| Revolving Facility, commitment 305.0 (Euro and Sterling sub-facilities) | Mativ Holdings, Inc., Mativ Luxembourg and other loan parties are the named parties to the amendment (10-Q Q1 page:32); the borrower and guarantor split and the added U.S. borrowers are Not supplied | 20.0 drawn; 276.2 undrawn as printed | Margin 1.75% to 2.75% by net debt to EBITDA; commitment fee 0.15% to 0.35%, currently 0.30%; average rate 7.66% on outstanding | Earlier of five years from April 3, 2026 or 182 days before the notes' maturity | The 10-K (before the amendment) says secured by substantially all personal property of the company and guarantors and guaranteed by wholly-owned direct material domestic subsidiaries and Mativ Luxembourg; the 10-Q Q3 says one more subsidiary became a guarantor (name not supplied) | 10-Q Q3 page:12, page:13, page:14; 10-K page:100 |
| Term Loan A, commitment 89.9 | Same | 89.7 | Same margin grid as the revolver; average rate 6.40% | Same as revolver | Same | 10-Q Q3 page:12, page:13, page:14 |
| Term Loan B, commitment 500.0 | Same | 498.7 | Fixed margins 3.50% to 4.50% by benchmark; average rate 8.40% | Earlier of seven years from April 3, 2026 or 91 days before the notes' maturity | Same; the financial maintenance covenants apply to the Revolving Facility and Term Loan A | 10-Q Q3 page:12, page:13, page:14 |
| 8.000% senior unsecured notes due October 1, 2029 | Mativ Holdings, Inc. | 400.0 (fair value 398.9, Level 1) | 8.000% fixed, interest April 1 and October 1; redeemable from October 1, 2026 at indenture prices (not supplied) | October 1, 2029 | Senior unsecured; guaranteed by wholly-owned subsidiaries that borrow under or guarantee the senior secured facilities or certain other debt | 10-Q Q3 page:12, page:13, page:14 |
| Other loan agreements | Not supplied | 2.7 | Not supplied | Not supplied | Not supplied | 10-Q Q3 page:12 |
| Debt issuance costs | Not applicable | -34.7 | Not applicable | Not applicable | Not applicable | 10-Q Q3 page:12 |
| Total debt | Not applicable | 976.4 (principal 1,011.1) | Not applicable | Not applicable | Not applicable | 10-Q Q3 page:12, page:14 |

Changes since December 31, 2025 (10-K page:99): the old revolver (160.0 drawn), Term Loan A (83.3), Term Loan B (116.5) and delayed draw term loan (270.1) were replaced on April 3, 2026; debt proceeds in nine months 2026 were 705.7 and repayments 728.1, issuance costs paid 32.7, and 8.7 was lost on extinguishment (10-Q Q3 page:4, page:5, page:13). Interest rate swaps hedge 405.8 notional of floating debt (480.8 at year-end) and cross-currency swaps hedge a 450 million euro net investment (10-Q Q3 page:15).

### Claims outside the debt figure

| Claim | Amount (US$m) | Inside or outside total debt of 976.4 | Locator and comment |
| --- | --- | --- | --- |
| Receivables Sales Agreement (U.S. subsidiaries, via a bankruptcy-remote special purpose entity) | 837.3 sold in 9M 2026 for cash of 836.9; 28.6 receivables pledged | Outside (sales of financial assets, off balance sheet) | 10-Q Q3 page:6, page:27. Maximum commitment was 150.0 through November 5, 2026 (10-K page:93); extended to October 23, 2029 by an October 23, 2026 amendment, size after amendment Not supplied. Outstanding sold balance Not supplied. FY2025 fees on this and reverse receivables programs were 8.4 (10-K page:94) |
| Finance leases | 14.7 noncurrent at Sep 30, 2026; present value 17.9 at Dec 31, 2025 | Outside | 10-Q Q3 page:3; 10-K page:92. The 10-K total lease payments are 28.6 for finance leases |
| Operating leases | 56.2 (8.8 current plus 47.4 noncurrent) | Outside | 10-Q Q3 page:3 |
| Pension and other postretirement benefits | 49.1 liability at Sep 30, 2026 (53.8 at Dec 31, 2025) | Outside | 10-Q Q3 page:3. 10-K plan funded status at Dec 31, 2025: U.S. pensions +22.1, non-U.S. pensions -37.1, U.S. other postretirement -18.5, non-U.S. other postretirement -3.6; net pension assets of 25.0 sit in other assets (10-K page:112). Restricted cash 4.2 is UK scheme money (10-Q Q3 page:19) |
| Foreign exchange contract liability (the filing discloses 450 million euro of cross-currency swaps as net investment hedges) | 27.6 in other liabilities at Sep 30, 2026 (53.2 at Dec 31, 2025) | Outside | 10-Q Q3 page:15, page:16. The split between the swaps and other contracts is not stated; swap settlements are shown in investing cash flows |
| Purchase obligations | 105.1 at Dec 31, 2025 (84.3 within one year) | Outside | 10-K page:67; not updated in the 10-Qs |
| Interest on debt | 185.0 over five years at Dec 31, 2025 (73.6 in 2026) | Outside; before the April 2026 refinancing | 10-K page:67 |
| Engineered Papers divestiture indemnity | Capped at 10 | Outside | 10-Q Q3 page:17; no material claims pending |
| Tornado, uncovered or unrecognized recoveries | Open | Outside | 10-Q Q3 page:17, page:18 |
| Litigation and environmental | Not quantified; management does not expect material effect | Outside | 10-Q Q3 page:17, page:18, page:19 |

### Covenants

| Test | Level | Reported figure | Headroom |
| --- | --- | --- | --- |
| Maximum net debt to EBITDA (Revolving Facility and Term Loan A only) | 5.00x current maximum, ranging from 5.00x to 4.00x over time (step dates Not supplied; 10-Q Q3 page:14, page:28). Before the amendment: 5.50x through Dec 31, 2025 and 5.25x after (10-K page:100; 10-Q Q1 page:26) | 3.8x at Sep 30, 2026 (10-Q Q3 page:28); 4.2x at Dec 31, 2025; 4.1x at Mar 31, 2026; 3.8x at Jun 30, 2026 | 1.2x turns below the current maximum; EBITDA could fall about 24.0 percent at constant net debt before 5.00x. At the final 4.00x level the cushion shrinks to about 5.0 percent, on the rounded 3.8x. Timing Not supplied |
| Minimum interest coverage (same facilities) | 2.50x to 3.00x over time (10-Q Q3 page:14). Before the amendment: 2.50x through Dec 31, 2025 then 2.75x (10-K page:100) | Not supplied | Not calculable. The reported-basis ratios here are 2.62x on cash interest and 2.92x on interest expense; the covenant EBITDA and interest definitions are not supplied |
| Total debt to capital, as calculated under the agreement | No limit supplied | 67.6 percent at Sep 30, 2026 (67.1 percent at Dec 31, 2025) | Not calculable: whether it is a test is not stated |
| Indenture covenants | Incurrence-type limits on debt, restricted payments, liens, asset sales, mergers and affiliate transactions; terms not supplied | In compliance at Sep 30, 2026 | Not calculable (10-Q Q3 page:13) |

Compliance with the credit agreement and the indenture is stated at September 30, 2026 (10-Q Q3 page:13, page:14). Definitions that differ from the metric computed here: the covenant ratio uses the agreement's EBITDA and net debt, while the reported-basis EBITDA here is operating profit plus cash flow D&A with the FY2025 goodwill impairment added back and no other adjustments. A back-solve of the stated 3.8x on the release's net debt of 879.1 implies covenant EBITDA of roughly 231 (range 228 to 234 for ratios of 3.85x to 3.75x), about 21 above the reported-basis 210.0; this is an inference that assumes the covenant net debt equals the release net debt.

### Latest quarter and events to the cutoff

| Date | Event | Amount (US$m) | Locator |
| --- | --- | --- | --- |
| April 3, 2026 (Q2 2026) | Ninth Amendment refinanced the revolver, Term Loan A and Term Loan B and eliminated the delayed draw term loan; certain subsidiaries became additional U.S. borrowers | Facilities 894.9 in total; loss on extinguishment 8.7; issuance costs paid 32.7 | 10-Q Q3 page:13; 10-Q Q1 page:21 |
| July 27, 2026 (Q3 2026) | Severe tornado destroyed a third-party distribution facility in Menasha, Wisconsin | Inventory write-off 42.5, clean-up and other 1.3, total 43.8; recoveries received 5.0, receivable 38.0, net loss 0.8; business interruption recoveries not recognized | 10-Q Q3 page:17, page:18 |
| Q3 2026 | Restructuring and other impairment 2.7, including an impairment on long-lived assets at a North American facility to be removed from service in Q4 2026 and severance for a new service center | 2.7 | 10-Q Q3 page:11 |
| October 23, 2026 (subsequent) | Receivables Sales Agreement amended, term extended to October 23, 2029 | Size Not supplied | 10-Q Q3 page:6, page:22 |
| November 4, 2026 (subsequent) | Held-for-sale North American facility sold; fair value uplift recorded in Q3 | Proceeds Not supplied | 10-Q Q3 page:23 |
| November 4, 2026 (subsequent) | Quarterly dividend of 0.10 per share declared, payable December 18, 2026 to holders of record November 27, 2026 | Per share 0.10 | 10-Q Q3 page:28; Release Q3 page:3 |
| October 1, 2026 (subsequent) | Semi-annual coupon date on the 8.000% notes; notes become redeemable | Coupon 16.0 (400.0 x 8.000% / 2, calculated) | 10-Q Q3 page:12 |

### Segments and adjusted EBITDA

| Segment | Period | Net sales | Gross profit | Adjusted EBITDA (management) | Locator |
| --- | --- | --- | --- | --- | --- |
| Filtration & Advanced Materials | Q3 2026 | 218.5 | 51.5 | 39.6 (18.1 percent margin) | 10-Q Q3 page:22; Release Q3 page:1, page:10 |
| Filtration & Advanced Materials | Q3 2025 | 198.3 | 42.5 | 32.9 (16.6 percent) | same |
| Sustainable & Adhesive Solutions | Q3 2026 | 281.0 | 46.2 | 32.6 (11.6 percent) | same |
| Sustainable & Adhesive Solutions | Q3 2025 | 315.4 | 56.9 | 43.3 (13.7 percent) | same |
| Unallocated | Q3 2026 | Not applicable | Not applicable | -9.9 | Release Q3 page:10 |
| Filtration & Advanced Materials | 9M 2026 | 608.5 | 138.8 | 102.4 | 10-Q Q3 page:22; Release Q3 page:10 |
| Sustainable & Adhesive Solutions | 9M 2026 | 902.4 | 157.1 | 113.8 | same |

SAS net sales fell 10.9 percent in Q3 2026 (printed), which the filing attributes to lower volume and mix, mainly the Menasha tornado and the Healthcare business, partly offset by price (10-Q Q3 page:24); FAM grew 10.2 percent (printed). The release states the FAM growth is the segment's strongest ever (Release Q3 page:1), which is a management claim not tested here. Gross profit is the CODM segment measure from January 1, 2026 (10-Q Q3 page:21).

### Discrete quarters

| Item | Q1 2025 | Q2 2025 | Q3 2025 | Q4 2025 (derived) | Q1 2026 | Q2 2026 | Q3 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales | 484.8 | 525.4 | 513.7 | 463.1 | 479.6 | 531.8 | 499.5 |
| Gross profit | 72.6 | 103.7 | 99.4 | 87.2 | 84.9 | 113.3 | 97.7 |
| Operating profit (loss) | -430.6 | 20.1 | 16.0 | 10.1 | 7.3 | 35.3 | 19.9 |
| Net income (loss) | -425.5 | -9.5 | -3.2 | 100.8 | -11.7 | 3.6 | -1.2 |
| Adjusted EBITDA (management) | 37.2 | 67.2 | 66.8 | Not supplied | 47.5 | 75.0 | 62.3 |
| Net debt at quarter end (management) | Not supplied | Not supplied | Not supplied | 934.0 | 953.5 | 908.2 | 879.1 |

Locators: 10-Q Q1 page:2, 10-Q Q2 page:2, 10-Q Q3 page:2, 10-K page:75; adjusted EBITDA from Release Q1 page:9, Release Q2 page:10, Release Q3 page:10. Q4 2025 is the FY2025 amount less nine months 2025; it is derived, not printed. The Q4 2025 net income includes a large tax benefit (FY2025 benefit 125.6 against 14.6 for nine months 2025, 10-K page:75; 10-Q Q3 page:2), so it is not a run-rate.

### Cash flow quality and earnings quality

Nine-month 2026 operating cash flow of 117.4 rose 2.9 from 114.5 (10-Q Q3 page:28), but the mix is weaker than the headline: net working capital provided 11.9 against 35.3, cash taxes were a net refund of 2.2 against 9.4 paid, and Q3 operating cash flow was 48.5 against 72.8 in the prior-year quarter (10-Q Q3 page:4, page:5, page:24). Free cash flow for nine months (90.5) also benefits from lower capital spending of 26.9 against 28.7, while Q3 spending was 11.0 against 6.1. The company sold 837.3 of trade receivables in nine months 2026 for 836.9 of cash (10-Q Q3 page:6): the receivables facility is a recurring financing source that does not show in total debt. Adjusted EBITDA adds back financing fees on the Receivables Sales Agreement of 5.1 for nine months 2026 (Release Q3 page:10, page:11), stock compensation, restructuring and tornado costs, so management's measure treats the cost of selling receivables as interest. Accounts receivable of 250.3 includes the 38.0 insurance receivable, and accounts payable rose to 219.6 from 160.7 (10-Q Q3 page:2, page:3, page:18): working capital at the balance sheet date is inflated by both. Restructuring and other impairment expense fell to 4.7 for nine months from 18.2 (10-Q Q3 page:2).

### Consistency with the CP-0 handoff and corrections

No CP-0 figure is corrected. Two additions: the unexplained difference of 8.8 between commitment less drawings and printed undrawn capacity also exists at December 31, 2025 (600.0 less 160.0 is 440.0 against 431.2 printed; 10-K page:63, page:64, page:99) as well as at March 31, June 30 and September 30, 2026, so it is a constant item and likely a standing usage of the facility, but no source says what it is. CP-0 flagged the Note 8 maturity wording against the maturity table; this module carries that conflict in the maturity chart and does not resolve it. CP-0 listed the interest coverage covenant figure as Not supplied; it remains so, and the reported-basis cover here is not a substitute.

## Calculations

All amounts US$m. Inputs are cited above; the arithmetic is shown so each can be recomputed.

### Reported-basis EBITDA (operating profit plus cash flow D&A, goodwill impairment added back)

- FY2025: -384.4 + 141.0 + 411.9 = 168.5 (10-K page:75, page:77).
- LTM Q3 2026: operating profit = -384.4 - (-394.5) + 62.5 = 72.6; D&A = 141.0 - 106.3 + 102.7 = 137.4; goodwill impairment contributes nothing to the window (it was in Q1 2025, outside); EBITDA = 72.6 + 137.4 = 210.0.
- LTM Q2 2026: operating profit = -384.4 - (-410.5) + 42.6 = 68.7; D&A = 141.0 - 71.5 + 69.5 = 139.0; EBITDA = 207.7 (10-Q Q2 page:2, page:4).
- LTM Q1 2026: operating profit = -384.4 - (-430.6) + 7.3 = 53.5; D&A = 141.0 - 35.3 + 34.8 = 140.5; EBITDA = 194.0 (10-Q Q1 page:2, page:3).
- The earnings releases show D&A of 34.7 for Q1 2026 and 71.6 for six months 2025 against 34.8 and 71.5 in the 10-Qs; the 10-Q figures are used. This basis includes restructuring and other impairment charges (FY2025 19.9; nine months 2026 4.7) and excludes no other items.

### Leverage and cover

- Total debt / EBITDA: FY2025 1,018.2 / 168.5 = 6.04; Q1 1,035.8 / 194.0 = 5.34; Q2 974.5 / 207.7 = 4.69; Q3 976.4 / 210.0 = 4.65.
- Net debt / EBITDA: FY2025 934.0 / 168.5 = 5.54; Q1 953.5 / 194.0 = 4.91; Q2 908.2 / 207.7 = 4.37; Q3 879.1 / 210.0 = 4.19. Net debt is total debt less cash and cash equivalents, excluding restricted cash.
- LTM cash interest: Q3 82.8 - 55.2 + 52.5 = 80.1; Q2 82.8 - 42.4 + 40.2 = 80.6; Q1 82.8 - 13.2 + 10.9 = 80.5. LTM windows contain both semi-annual coupons on the notes.
- EBITDA / cash interest: FY2025 168.5 / 82.8 = 2.04; Q1 194.0 / 80.5 = 2.41; Q2 207.7 / 80.6 = 2.58; Q3 210.0 / 80.1 = 2.62.
- LTM interest expense at Q3 2026: 71.1 - 54.1 + 54.9 = 71.9; 210.0 / 71.9 = 2.92.
- Management nine-month basis: 184.8 / 52.5 = 3.52 (cash interest); 184.8 / 54.9 = 3.37 (interest expense). Not annualized and not a covenant figure.
- Implied covenant EBITDA from the stated 3.8x: 879.1 / 3.8 = 231.3; at 3.85x 228.3; at 3.75x 234.4. At Dec 31, 2025, 934.0 / 4.2 = 222.4 against reported-basis 168.5.
- EBITDA cushion at constant net debt: 1 - 3.8 / 5.00 = 24.0 percent; 1 - 3.8 / 4.00 = 5.0 percent.

### Liquidity build at September 30, 2026

- Cash and cash equivalents 97.3 (restricted cash of 4.2 excluded) plus printed undrawn revolver capacity 276.2 = 373.5, equal to the release (Release Q3 page:3).
- Commitment 305.0 less drawn 20.0 = 285.0; printed undrawn 276.2; difference 8.8 not explained by any printed item (searched for letters of credit, standby and LC across all sources; only fee terms found, 10-K page:99). The same 8.8 appears at June 30 (305.0 - 17.0 = 288.0 against 279.2), March 31 (600.0 - 175.0 = 425.0 against 416.2) and December 31, 2025 (600.0 - 160.0 = 440.0 against 431.2).
- Foreign-held cash: 72.7 / 97.3 = 74.7 percent of cash and cash equivalents (10-Q Q3 page:27); repatriation cost or restriction beyond the UK scheme cash is not stated.
- Facilities expiring within twelve months of September 30, 2026: none among the bank facilities (earliest maturity not before 2029 on either reading); the receivables program term was due November 5, 2026 (10-K page:93) and was extended on October 23, 2026 (10-Q Q3 page:6). Reverse receivables programs are uncommitted (10-K page:93).

### Tie-outs

- Debt principal: 20.0 + 89.7 + 498.7 + 400.0 + 2.7 = 1,011.1; less 34.7 = 976.4 (10-Q Q3 page:12, page:14). Maturity table: 2.2 + 6.6 + 6.1 + 406.2 + 6.2 + 583.8 = 1,011.1.
- Net debt: 976.4 - 97.3 = 879.1. Debt to capital: 976.4 / (976.4 + 467.1) = 67.6 percent; December 2025: 1,018.2 / (1,018.2 + 498.7) = 67.1 percent, both equal to the printed ratios.
- Quarterly tie to nine months: net sales 479.6 + 531.8 + 499.5 = 1,510.9; adjusted EBITDA 47.5 + 75.0 + 62.3 = 184.8 and 37.2 + 67.2 + 66.8 = 171.2; segment adjusted EBITDA nine months 2026: 102.4 + 113.8 - 31.4 = 184.8.
- Q4 2025 derived: net sales 1,987.0 - 1,523.9 = 463.1; gross profit 362.9 - 275.7 = 87.2; operating profit -384.4 - (-394.5) = 10.1; net income -337.4 - (-438.2) = 100.8.
- Free cash flow: 117.4 - 26.9 = 90.5; Q3 48.5 - 11.0 = 37.5; after dividends 90.5 - 17.0 = 73.5. LTM operating cash flow 133.8 - 114.5 + 117.4 = 136.7; LTM capital spending 40.0 - 28.7 + 26.9 = 38.2; LTM free cash flow 98.5.
- Tornado: 42.5 + 1.3 = 43.8; 43.8 - 5.0 - 38.0 = 0.8.
- Notes coupon check: 400.0 x 8.000% = 32.0 a year; 16.0 per semi-annual date.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreement as amended (Ninth Amendment), indenture and receivables purchase agreement not supplied: EBITDA and interest definitions, covenant step-down dates, baskets, guarantor and borrower names, security package after amendment are Not supplied | High | CP-2, CP-5 | Obtain the documents or an 8-K compliance disclosure |
| Annual and trailing adjusted EBITDA Not calculable: no fourth quarter 2025 adjusted figure and no adjusted EBITDA in the 10-K; management's 3.8x cannot be reproduced | High | CP-2 | Add the Q4 2025 release |
| Reported interest coverage ratio under the agreement Not supplied | Medium | CP-2 | Obtain compliance certificate |
| Letters of credit and other usage behind the 8.8 gap between commitment less drawings and printed undrawn capacity Not supplied | Medium | CP-2 | Agreement or compliance certificate |
| Revolver and Term Loan A maturity wording versus maturity table unresolved; if the springing wording operates, up to 109.7 of revolver and Term Loan A principal (20.0 + 89.7) would mature in 2029, ahead of the notes | Medium | CP-2 | Amended agreement |
| Receivables program: outstanding sold balance and post-amendment commitment Not supplied | Medium | CP-2 | October 2026 amendment filing |
| Interest rate: margins by facility given as ranges; benchmark currency of Term Loan A and Term Loan B borrowings not stated; other loan agreements (2.7) have no terms | Low | CP-2 | Agreement |
| Tornado insurance outcome open: 38.0 receivable not yet collected; business interruption not recognized | Medium | CP-2 | Q4 2025 and later filings after the cutoff |
| Post-quarter items without amounts: proceeds of the November 4, 2026 facility sale; Q4 2026 cash events | Low | CP-2 | Next filing |
| Purchase obligations and interest obligations are as of December 31, 2025, before the refinancing | Low | CP-2 | Next 10-K |
| Presentation changes in the December 31, 2025 balance sheet (lease lines condensed into property, plant and equipment and accrued expenses) carried from the 10-K to the 10-Q; totals unchanged | Low | CP-2 | None |
| Prior-year restructuring add-back differs between the two release reconciliations (9.7 and 10.6 for Q3 2025); the basis is not explained | Low | CP-5 | Carry as a presentation difference |
| No credit ratings, market quotes or peer data in the sources or context | Medium | CP-2 | Add if required |

Not supplied does not mean zero for any item above.

## Next module

Proceed to CP-1A with the business, operating model and transaction facts: Mativ's two segments, the April 3, 2026 refinancing, the 2029 notes, the July 27, 2026 tornado and its insurance position, the October 23, 2026 receivables amendment and the November 4, 2026 asset sale. Carry forward from this handoff the leverage on both bases (management 3.8x; reported-basis 4.65x total and 4.19x net), the liquidity of 373.5, the covenant levels and the unresolved items above, and treat the management claims (strongest FAM growth ever, record adjusted EBITDA, inventory losses fully recoverable) as Management Language, not fact. CP-2 should use the reported-basis and management bases side by side, never merged, and should restrict covenant conclusions to what Note 8 states.
