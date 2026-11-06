## Request

Issuer: Block, Inc. (issuer id xyz, ticker XYZ), consolidated, as the registrant of the filings in the pack. As-of date and evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency USD; the filings report in thousands and this handoff converts to US$ millions (US$m) with one decimal, which is a unit conversion, not a restatement. Current period: Q3 2026 (quarter ended September 30, 2026), nine months 2026 and LTM to September 30, 2026; prior period FY2025.

Task: extract the financial base for the credit snapshot (income statement, cash flow, balance sheet debt and liquidity), compute leverage, interest cover, liquidity and maturity data, and state what the evidence supports. The upstream readiness handoff (CP-0) rated the source set READY_WITH_LIMITATIONS and carried forward: the leverage covenant level, guarantors and executed documents are open gaps; revenue comparatives were reclassified in the latest report; adjusted measures are management claims. This handoff follows those limits. No ratings, quotes, market data or deal terms are in the context; blank context fields are not treated as zero.

## Sources

### Issuer sources relied on

| Source | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_xyz-20251231.htm.jsonl | 6d2723637c4e4692665dfc17c25cdb747bc058fa0efdacc637270724a986bc79 | FY2025 statements (pages 140 to 143), Adjusted EBITDA reconciliation (page:125), liquidity table (page:127), debt note (pages 184 to 198), cash interest (page:211) |
| 10-Q_2026-03-31_xyz-20260331.htm.jsonl | fb16696ee2c760f5f516dd4d7d776ad2e1413e975d581b22e43bf743c804dffb | Read for period coverage only; not cited for any figure below |
| 10-Q_2026-06-30_xyz-20260630.htm.jsonl | 298a453eb61f62c2eadccf751942418cba8c13261b222b26c193276f0204df4e | Read for period coverage only; not cited for any figure below |
| 10-Q_2026-09-30_xyz-20260930.htm.jsonl | c3685fce2b8084b3b1277e2ff24d3b8912d57dba3d48bc4c00ef1cdf864ed3ba | Q3 2026 and nine months 2026 statements (pages 4 to 10), Note 12 debt (pages 26 to 30), Note 16 contingencies (pages 34 to 37), Note 18 cash interest (page:40), liquidity (pages 55 to 58) |
| EX-99.1_2026-05-07_d132441dex991.htm.jsonl | d34a2a9e1d7a5617f1c2e6fc60dfac8b09244c4670a9cb13c493e5c88cddf1a8 | Not cited for any figure below |
| EX-99.1_2026-08-05_d91486dex991.htm.jsonl | 804a5c312efc62e6ddd1ec8bbc4d12bb902bba131422b7373caf3f4ebbc3e21e | Not cited for any figure below |
| EX-99.1_2026-11-03_q32026shareholderletter.htm.jsonl | a2c931043c84d33fdc40710a24c2e84aa25d66394cc76e294f6f9e8221b76b85 | Quarterly series for operating income and Adjusted EBITDA (pages 14, 17, 32), Adjusted EBITDA definition (page:22), guidance (page:13) |

### Handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | fde3c57d263f194f36b012cf6dac47111bd001036fc4309d336b4e5a15f1d35b | Source readiness view and gap list, carried forward in this handoff |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Block's notes and secured warehouse borrowings sit below its reported cash, with leverage on filed earnings of 4.67x at the latest quarter and 1.69x on management's adjusted earnings. Large unpaid legal accruals weaken the picture. | Medium | The covenant level is not printed, and adjusted earnings add back large legal charges and share-based pay. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt at the latest quarter is the notes plus warehouse borrowings, and the 2026 notes were paid in cash. | No bond maturity falls before 2027, and near-term refinancing risk is limited to the warehouse lines and short certificates of deposit. | High |
| Leverage on filed operating income plus depreciation rose from 4.19x at FY2025 to 4.67x at the latest quarter, while net of cash it moved from 1.04x to below zero. | Net leverage depends on cash that may partly fund customer balances, so the negative net figure may overstate surplus cash. | Medium |
| Operating income fell on large legal and restructuring charges, and an agreed Department of Justice resolution is accrued but not yet paid. | Cash outflows for the settlement are still ahead, so reported operating cash flow overstates what is free. | Medium |
| Interest cover on filed earnings fell from 8.44x to 3.99x. | The decline reflects higher cash interest and lower filed earnings over the latest twelve months. | Medium |
| Stated liquidity of 10,064.0 includes restricted cash and securities, and the revolver is undrawn. | Liquidity is large against near-term maturities, but not all of it is freely available corporate cash. | Medium |

### Financial base view

Block, Inc. reports a platform business with two reportable segments and a revenue base that grew in 2026 on payments volume and consumer lending. Its debt at September 30, 2026 consists of five note series (four senior unsecured series and one convertible series) with 5,775.0 of principal, secured warehouse borrowings of 1,543.5 held in special purpose entities whose assets are not available to the issuer's creditors, and an undrawn 900.0 revolver. Cash and cash equivalents of 7,859.3 exceed total debt of 7,318.5, so net debt is negative on that measure. On the filed basis (operating income plus depreciation and amortization, no add-backs) LTM EBITDA is 1,567.0, giving total debt to EBITDA of 4.67x, up from 4.19x at FY2025, and EBITDA to cash interest of 3.99x, down from 8.44x. On management's Adjusted EBITDA of 4,336.4 the same ratios are 1.69x and 11.03x. The gap between the two bases is mostly share-based compensation (about 1.2 billion a year) and "contingencies, restructuring and other charges", which were 1,542.9 for nine months 2026 (742.8 + 365.1 + 435.0). Separately, accrued legal contingencies on the balance sheet rose to 980.6 at the latest quarter from 173.0 at FY2025, and include 764 for a Department of Justice resolution agreed in principle in October 2026 and accrued at September 30, 2026. That payment is a cash claim outside the debt figure. The reported cash flow is flattered by the unpaid accrual. The view is therefore moderate gross leverage with ample stated liquidity, a bond maturity profile with nothing due until November 2027, and meaningful non-debt claims and definition risk that the covenant (a maximum total net leverage ratio, level not printed) cannot be tested against from the pack.

### Statement and debt extraction

All amounts US$m unless stated; converted from thousands as printed.

| Item | FY2025 (Dec 31, 2025) | Sep 30, 2026 | Locator |
| --- | --- | --- | --- |
| Cash and cash equivalents | 6,564.1 | 7,859.3 | 10-K page:140; 10-Q Q3 page:4 |
| Investments in debt securities (short plus long term) | 706.7 (517.8 + 188.9) | 583.7 (385.2 + 198.4) | 10-K page:127; 10-Q Q3 page:55 |
| Short-term plus long-term restricted cash | 1,145.4 (1,071.6 + 73.8) | 721.1 (650.4 + 70.6) | 10-K page:127; 10-Q Q3 page:55 |
| Customer funds (held for customers, excluded from liquidity) | 4,771.8 | 5,356.9 | balance sheets |
| Customers payable | 6,805.4 | 7,700.1 | balance sheets |
| Senior and convertible notes, principal | 7,350.0 | 5,775.0 | 10-Q Q3 page:27 |
| Notes, net carrying value | 7,289.0 | 5,723.0 | 10-Q Q3 page:27 |
| Warehouse Facilities drawn (current plus non-current) | 1,364.9 (466.9 + 897.9) | 1,543.5 (447.4 + 1,096.1) | balance sheets; 10-Q Q3 page:30 |
| Revolving credit facility commitment, drawn nil | 775.0 | 900.0 | 10-K page:196; 10-Q Q3 page:28 |
| Warehouse capacity available to be drawn | 323.9 | 809.3 | 10-K page:198; 10-Q Q3 page:29 |
| Accrued legal contingencies | 173.0 | 980.6 | 10-Q Q3 page:22 |
| Brokered certificates of deposit, par (maturity twelve months or less) | none | 381.4 | 10-Q Q3 page:56 |
| Total stockholders' equity | 22,169.9 | 22,870.2 | balance sheets |

Note series at September 30, 2026 (10-Q Q3 page:27; coupons and maturities 10-K pages 186 to 190, 10-Q Q3 pages 27 and 57): 2027 Convertible Notes 575.0, 0.25%, due November 1, 2027; 2030 Senior Notes 1,200.0, 5.625%, due August 15, 2030; 2031 Senior Notes 1,000.0, 3.50%, due June 1, 2031; 2032 Senior Notes 2,000.0, 6.50%, due May 15, 2032; 2033 Senior Notes 1,000.0, 6.000%, due August 15, 2033. The senior series are described as senior unsecured notes and the 2027 notes as convertible senior notes; whether the convertible notes are unsecured, and who guarantees any series, is not stated in the pages read. The 2026 Senior Notes (1,000.0) and 2026 Convertible Notes (575.0) were paid in cash on June 1, 2026 and May 1, 2026 (10-Q Q3 page:27).

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 4.19 | 1.04 | x | Total debt is note principal 7,350.0 plus Warehouse Facilities 1,364.9 (8,714.9); EBITDA is operating income 1,708.4 plus depreciation and amortization 369.5 (2,077.9), no add-backs; net debt deducts cash and cash equivalents 6,564.1 only, excluding restricted cash, securities and customer funds. Cash partly backs customer balances. |
| LTM Q3 2026 | 4.67 | -0.35 | x | Total debt is note principal 5,775.0 plus Warehouse Facilities 1,543.5 (7,318.5); EBITDA is LTM operating income 1,188.7 plus depreciation and amortization 378.2 (1,567.0), no add-backs; net debt deducts cash and cash equivalents 7,859.3 only (-540.8). Warehouse debt is secured on SPE assets; on notes alone the ratio is 3.69x. Covenant definition differs and is not printed. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 8.44 | x | EBITDA 2,077.9 (operating income plus depreciation and amortization) over cash paid for interest 246.3 (10-K page:211). On Adjusted EBITDA 3,466.6 the ratio is 14.07x. |
| LTM Q3 2026 | 3.99 | x | EBITDA 1,567.0 over LTM cash paid for interest 393.1 (FY2025 246.3 less nine months 2025 124.2 plus nine months 2026 270.9). Cash paid for interest is a consolidated figure not split between notes, warehouse and deposits; warehouse interest expense is booked in general and administrative expense (10-Q Q3 page:30). On Adjusted EBITDA 4,336.4 the ratio is 11.03x. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 6,564.1 | 775.0 | US$m | Cash and cash equivalents (10-K page:140); revolver undrawn with no letters of credit issued (10-K page:196). Excludes 1,145.4 restricted cash, 706.7 debt securities and 323.9 warehouse availability. Revolver was later amended to 900.0 on January 14, 2026. |
| Q3 2026 | 7,859.3 | 900.0 | US$m | Cash and cash equivalents (10-Q Q3 page:4); revolver undrawn, no letters of credit issued (10-Q Q3 page:28). Company-stated total liquidity is 10,064.0 including restricted cash and securities; warehouse availability of 809.3 is excluded. Cash is not net of obligations to customers (customers payable exceeds customer funds). |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remainder of FY2026 | 0.0 | US$m | No note or warehouse principal is scheduled in the remainder of 2026 per the tables read; 381.4 of brokered certificates of deposit (maturity twelve months or less) are deposit liabilities, not included. |
| FY2027 | 1,090.0 | US$m | 2027 Convertible Notes 575.0 (November 1, 2027) plus Warehouse Facilities by final maturity 515.0, of which 447.4 is classified current at September 30, 2026. |
| FY2028 | 549.4 | US$m | Warehouse Facilities by final maturity; revolving, secured on consumer receivables. |
| FY2029 | 479.1 | US$m | Warehouse Facilities by final maturity (final maturities through July 2029). |
| FY2030 | 1,200.0 | US$m | 2030 Senior Notes, due August 15, 2030. |
| FY2031 | 1,000.0 | US$m | 2031 Senior Notes, due June 1, 2031. The 900.0 revolver, undrawn, matures January 2031 subject to a springing earlier date. |
| FY2032 | 2,000.0 | US$m | 2032 Senior Notes, due May 15, 2032. |
| FY2033 | 1,000.0 | US$m | 2033 Senior Notes, due August 15, 2033. |

The rows sum to 7,318.5 (notes principal 5,775.0 plus warehouse 1,543.5) at September 30, 2026.

### Financials and credit metrics

| Metric (US$m) | FY2025 | Nine months 2025 | Nine months 2026 | Q3 2025 | Q3 2026 | LTM Q3 2026 | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total net revenue | 24,193.7 | 17,941.2 | 19,393.9 | 6,115.0 | 6,719.4 | 25,646.4 | 10-K page:141; 10-Q Q3 page:5 |
| Gross profit | 10,359.9 | 7,487.7 | 9,310.6 | 2,661.6 | 3,235.3 | 12,182.8 | same |
| Operating income | 1,708.4 | 1,223.0 | 703.4 | 409.4 | 428.5 | 1,188.7 | same |
| Depreciation and amortization | 369.5 | 273.5 | 282.1 | 92.1 | 91.1 | 378.2 | 10-K page:143; 10-Q Q3 page:7; letter page:32 |
| EBITDA, filed basis (operating income plus D&A) | 2,077.9 | 1,496.5 | 985.5 | 501.6 | 519.6 | 1,567.0 | calculated |
| Adjusted EBITDA, management | 3,466.6 | 2,536.9 | 3,406.7 | 832.7 | 1,227.9 | 4,336.4 | 10-K page:125; 10-Q Q3 page:51 |
| Interest expense, net | 129.4 | 75.6 | 157.0 | 34.7 | 48.1 | 210.8 | statements of operations |
| Cash paid for interest | 246.3 | 124.2 | 270.9 | not supplied | not supplied | 393.1 | 10-K page:211; 10-Q Q3 page:40 |
| Net income | 1,304.2 | 1,188.7 | 342.6 | 461.6 | 564.1 | 458.2 | statements of operations |
| Net cash provided by operating activities | 2,579.7 | 1,958.7 | 3,001.6 | 1,451 (rounded) | 1,016 (rounded) | 3,622.6 | cash flow statements; letter page:17 |
| Purchases of property and equipment | 155.0 | 113.8 | 128.0 | 51 (rounded) | 44 (rounded) | 169.2 | same |
| Operating cash flow less capex | 2,424.7 | 1,844.9 | 2,873.6 | 1,400 (rounded) | 972 (rounded) | 3,453.4 | calculated |
| Total debt / EBITDA, filed basis (x) | 4.19 | n/a | n/a | n/a | n/a | 4.67 | calculated |
| Net debt / EBITDA, filed basis (x) | 1.04 | n/a | n/a | n/a | n/a | -0.35 | calculated |
| Total debt / Adjusted EBITDA (x) | 2.51 | n/a | n/a | n/a | n/a | 1.69 | calculated |
| EBITDA / cash interest, filed basis (x) | 8.44 | n/a | n/a | n/a | n/a | 3.99 | calculated |
| Adjusted EBITDA / cash interest (x) | 14.07 | n/a | n/a | n/a | n/a | 11.03 | calculated |

### Quality and definition review

Adjusted EBITDA is defined as net income excluding share-based compensation, restructuring share-based compensation, depreciation and amortization, "contingencies, restructuring, and other charges", interest, bitcoin remeasurement, other income and expense, taxes, disposals and acquired deferred revenue adjustments (letter page:22). Quarterly add-backs for contingencies, restructuring and other charges were 54.1 (Q4 2025), 742.8 (Q1 2026), 365.1 (Q2 2026) and 435.0 (Q3 2026) (letter page:32). The filings tie the increase in general and administrative expense to accrued legal contingencies (letter page:16) and the Workforce Plan cost 495.0 in nine months 2026 (10-Q Q3 page:40); the pages read do not itemise how much of the add-back is the Department of Justice matter, for which "The Company has accrued $764 million for this matter as of September 30, 2026" (10-Q Q3 page:34). Because the accrual is unpaid, nine-month 2026 operating cash flow of 3,001.6 includes a positive swing from accrued legal contingencies (10-Q Q3 page:59: "primarily due to an increase in accrued legal contingencies"); accrued legal contingencies rose by 807.6. The financial covenant is "a maximum total net leverage ratio" tested quarterly (10-Q Q3 page:28), with the issuer stating compliance; its definition, addbacks and threshold are not printed, so neither basis above is the covenant measure.

Lending flows affect comparability: loans held for investment are classified in investing activities (purchases and originations 33,272.9 and repayments 31,325.9 for nine months 2026, 10-Q Q3 page:8), while loans originally held for sale run through operating activities. Operating cash flow less capex therefore does not net lending growth, and the company's own non-GAAP cash flow after those items is 1,697 LTM (letter page:17), a management figure.

## Calculations

All inputs in US$m from the cited pages; thousands converted by dividing by 1,000.

1. LTM Q3 2026 for a flow item = FY2025 less nine months 2025 plus nine months 2026. Revenue: 24,193.683 - 17,941.205 + 19,393.893 = 25,646.371. Gross profit: 10,359.929 - 7,487.703 + 9,310.593 = 12,182.819. Operating income: 1,708.406 - 1,223.035 + 703.371 = 1,188.742 (cross-check by quarters Q4 2025 485.371 + Q1 2026 (171.990) + Q2 2026 446.870 + Q3 2026 428.491 = 1,188.742). D&A: 369.529 - 273.464 + 282.148 = 378.213 (quarters 96.065 + 95.977 + 95.051 + 91.120 = 378.213). Adjusted EBITDA: 3,466.568 - 2,536.878 + 3,406.739 = 4,336.429 (quarters 929.690 + 1,010.221 + 1,168.597 + 1,227.921 = 4,336.429). Interest expense, net: 129.363 - 75.582 + 157.044 = 210.825. Cash interest: 246.331 - 124.220 + 270.946 = 393.057. Net income: 1,304.210 - 1,188.654 + 342.615 = 458.171. Operating cash flow: 2,579.714 - 1,958.714 + 3,001.581 = 3,622.581. Capex: 155.038 - 113.838 + 127.996 = 169.196.
2. EBITDA, filed basis = operating income + depreciation and amortization. FY2025: 1,708.406 + 369.529 = 2,077.935. Nine months 2025: 1,223.035 + 273.464 = 1,496.499. Nine months 2026: 703.371 + 282.148 = 985.519. Q3 2025: 409.440 + 92.119 = 501.559. Q3 2026: 428.491 + 91.120 = 519.611. LTM: 1,188.742 + 378.213 = 1,566.955.
3. Total debt (note principal plus Warehouse Facilities drawn). FY2025: 7,350.000 + (466.942 + 897.941) = 8,714.883. Q3 2026: 5,775.000 + (447.437 + 1,096.103) = 7,318.540. Warehouse total agrees to the scheduled principal table: 515.039 + 549.437 + 479.064 = 1,543.540.
4. Net debt = total debt less cash and cash equivalents. FY2025: 8,714.883 - 6,564.092 = 2,150.791. Q3 2026: 7,318.540 - 7,859.314 = -540.774.
5. Ratios. Total debt / EBITDA: FY2025 8,714.883 / 2,077.935 = 4.194; Q3 2026 7,318.540 / 1,566.955 = 4.671. Net debt / EBITDA: 2,150.791 / 2,077.935 = 1.035; -540.774 / 1,566.955 = -0.345. Notes only / EBITDA at Q3 2026: 5,775.000 / 1,566.955 = 3.686. Total debt / Adjusted EBITDA: 8,714.883 / 3,466.568 = 2.514; 7,318.540 / 4,336.429 = 1.688. Cover: 2,077.935 / 246.331 = 8.436; 1,566.955 / 393.057 = 3.987; Adjusted: 3,466.568 / 246.331 = 14.073; 4,336.429 / 393.057 = 11.033.
6. Operating cash flow less capex: FY2025 2,579.714 - 155.038 = 2,424.676; nine months 2025 1,958.714 - 113.838 = 1,844.876; nine months 2026 3,001.581 - 127.996 = 2,873.585; LTM 3,622.581 - 169.196 = 3,453.385.
7. Run-rate coupon on notes at September 30, 2026 = 1,200 x 5.625% + 1,000 x 3.50% + 2,000 x 6.50% + 1,000 x 6.000% + 575 x 0.25% = 67.5 + 35.0 + 130.0 + 60.0 + 1.4375 = 293.9375. This is a calculated annual contractual coupon, not a filed figure; nine months 2026 contractual interest on the notes was 231.370 (10-Q Q3 page:27), consistent with this rate plus five months on the repaid 2.75% 2026 Senior Notes (1,000 x 2.75% x 5/12 = 11.46; 293.94 x 9/12 = 220.45; sum 231.9).
8. Customers payable versus customer funds at September 30, 2026: 7,700.091 - 5,356.911 = 2,343.180 excess of customers payable over customer funds; less settlements receivable 1,454.211 leaves 888.969. This is an analytical indicator that some corporate cash may fund customer obligations; the filing does not state the amount (10-Q Q3 page:59 explains customers payable can exceed settlements receivable and includes Cash App stored funds).
9. Change in accrued legal contingencies: 980.592 - 172.959 = 807.633.
10. Maturity wall check: 575.000 + 515.039 + 549.437 + 479.064 + 1,200.000 + 1,000.000 + 2,000.000 + 1,000.000 = 7,318.540, equal to total debt at September 30, 2026.

## Gaps

| Gap | Detail | Effect |
| --- | --- | --- |
| Covenant level and reported ratio | Searched all seven sources for the numeric limit of the maximum total net leverage ratio and for the issuer's computed ratio; neither is printed. Not calculable. | Covenant headroom cannot be computed; both EBITDA bases above differ from the covenant definition. |
| Guarantors and obligor roles | Not stated in the pages read; context blank. | Structural subordination relative to subsidiaries and the Warehouse SPEs is not assessable beyond the SPE description. |
| Executed indentures and credit agreement | Not supplied. | Terms such as change of control, redemption and covenants rest on issuer summaries. |
| Quarterly cash interest | Cash paid for interest is printed for FY2025 and nine months 2025 and 2026 only; Q3 2025 and Q3 2026 discrete cash interest is not supplied. | Interest cover is shown for FY2025 and LTM only. |
| Rounded quarterly operating cash flow and capex | Q3 2025 and Q3 2026 operating cash flow and capex come from the shareholder letter in US$m rounded; not recomputed from filed three-month statements because the 10-Q cash flow is nine-month only. | Marked rounded in the table. |
| Customer cash | The share of cash and cash equivalents that is economically owed to customers is not stated. | Net debt of -540.8 may overstate surplus cash. |
| DOJ resolution | Agreement in principle, subject to final agreement and court approval; the filing says terms could exceed the amount accrued (10-Q Q3 pages 34 and 35). The cash timing is not stated. | Cash outflow of about 764 net is not in debt or in the leverage ratios; the derivative-case insurance receipt of 150 is also uncertain (page:36). |
| Other non-debt claims | Purchase commitments total 2,201.3 (10-Q Q3 page:37); operating leases, pensions and retiree medical, factoring and supply-chain finance were not examined in this module beyond that; interest-bearing deposits and brokered certificates of deposit of 381.4 are bank-funding liabilities outside the debt figure. | Left for CP-2. |
| Ratings | The context supplies none; the 10-Q mentions agency ratings in management discussion (page:58) only as issuer statements. | Not verified against agency reports. |
| Perimeter | Figures are consolidated Block, Inc. including Square Financial Services and the Warehouse SPEs; the filings do not give restricted and unrestricted subsidiary splits. | Whole-group metrics, not issuer-only. |

## Next module

CP-1A should reuse the LTM bridge above (quarter sums agree to FY2025 less nine months 2025 plus nine months 2026) and test the Adjusted EBITDA add-backs, especially contingencies, restructuring and other charges and share-based compensation, as the main definition risk. CP-2 should take the maturity table, the note coupons, the Warehouse Facilities terms and the non-debt claims listed in the gaps (DOJ accrual of 764, accrued legal contingencies of 980.6, purchase commitments of 2,201.3, brokered certificates of deposit of 381.4), and request the indentures and credit agreement if covenant analysis is required. Carry forward that the leverage ratios above are on a filed-earnings basis with no covenant adjustments.
