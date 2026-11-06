## Request

Issuer: Vestis Corp (ticker VSTS, issuer id vsts), registrant Vestis Corporation, consolidated. As-of date and evidence cutoff: 2026-11-05. Pathway: credit snapshot. Reporting currency: USD. Statements are printed in US$ thousands and narrative amounts in US$ millions; chart tables below are in the unit they state.

Task: extract and calculate the financial base for the credit view from the pinned sources: income statement, cash flow, balance sheet, debt and lease structure, liquidity, covenants, segments and quality of earnings and cash flow, and prepare the leverage, interest cover, liquidity and debt maturity chart data.

Period conventions used throughout. Fiscal 2025 ended October 3, 2025 and was a 53-week year (10-K page:65). Fiscal 2026 quarters end January 2, 2026 (Q1), April 3, 2026 (Q2) and July 3, 2026 (Q3). The context names current period q2-2026 and prior period fy-2025; the latest filed period in the pack is Q3 FY2026 (three and nine months ended July 3, 2026), so this handoff reports Q3 FY2026 as latest and shows the Q2 FY2026 position in the period-end tables. Nothing dated after the cutoff is used. The latest evidence is dated August 11, 2026.

Correction to the readiness handoff: that handoff reported no conflict between filings and releases on the figures it checked. That remains true for the filing-to-release comparison, but this module found two inconsistencies inside the company's own releases, set out under Definition risks and conflicts (fiscal 2025 Adjusted EBITDA, and a small free cash flow difference).

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-10-03_vsts-20251003.htm.jsonl | 69acf45c43af00eb0ad3afdad499957974d6855c0a4c69b858d3f2f1a0defa4d | Fiscal 2025 statements, debt note, maturities, covenants, leases, segments, cash interest paid |
| 10-Q_2026-01-02_vsts-20260102.htm.jsonl | 637925692f36f8779f60ebbc11d3252e4fe1f1a5077b706d2e2b4b1b4f6edc05 | Q1 FY2026 balance sheet, debt note, cash interest, receivables facility balance |
| 10-Q_2026-04-03_vsts-20260403.htm.jsonl | ba2978bcc5b4cdc3b18b43c2c9ae31ce0a31d87a366091d84bc271a3c594f858 | Q2 FY2026 balance sheet, debt note, six-month cash interest, receivables facility balance |
| 10-Q_2026-07-03_vsts-20260703.htm.jsonl | 7db2f115581c382fda3a1a642c3240840cc03e0b4154737c2546ddd28c46a9af | Q3 FY2026 statements, debt, leases, segments, MD&A, covenants, receivables facility |
| EX-99.1_2026-02-10_vstsq1fy26earningsrelease-.htm.jsonl | 73cf4915cc22c7c9a6d41b209e21e1301c8d95ee51da8c8656b7c37a3072aacd | Q1 FY2026 liquidity, net debt and net leverage table |
| EX-99.1_2026-05-12_vstsq2fy26earningsrelease-.htm.jsonl | e70477c8d46036f4ef7bd70b6551daa75ee805b6eb9bc6e0504e90f227edd1d1 | Q2 FY2026 liquidity, net debt, net leverage, outlook |
| EX-99.1_2026-08-11_vstsq3fy26earningsrelease-.htm.jsonl | d2693610d697f7e33edfd6b5f9d57dc6906301a18a12d6a3feec8645e5a3af14 | Q3 FY2026 non-GAAP reconciliations, trailing twelve month figures, net debt, liquidity, outlook |

Run context (settings only, not issuer evidence): context, sha256 c28ff4b5be1db183138bacbfdcd7f4640157e3a21bdc54358648d894f8fed07c.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | fb64725ea4a061e1ccbb327ea1648238e8928972fee966ac507aa72bbbb573c2 | Source readiness: its limitations are carried (executed credit documents not supplied, context period earlier than latest filing, receivables facility definition difference, non-GAAP measures management-defined) |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Vestis has cut principal debt and improved earnings through fiscal 2026: company-reported net leverage is 4.10x against a 5.00x maximum, with liquidity of $351.8 million. Headroom is real but narrower at the coming step-downs. | Medium | Covenant terms are company summaries and the receivables facility treatment in the ratio is unresolved. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Reported net leverage fell from 4.72x at fiscal 2025 year end to 4.10x at July 3, 2026 as principal debt fell and trailing earnings rose. | Maintenance test headroom widened, but the maximum steps down to 4.75x and then 4.50x. | Medium |
| Term loan and revolver maturities fall only in fiscal 2028 and fiscal 2031, with no revolver borrowings at July 3, 2026. | No bank debt wall before fiscal 2028, but the receivables facility is scheduled to end August 2, 2027. | Medium |
| Nine month operating cash flow rose sharply, helped by working capital and higher receivables facility sales. | Part of the improvement may not repeat, so cash flow quality needs care. | Medium |
| Two company figures for fiscal 2025 Adjusted EBITDA differ, and interest cover depends on the definition used. | Leverage and cover for fiscal 2025 carry definition risk. | Low |

### Financial base view

Vestis Corp entered fiscal 2026 with company-reported net leverage of 4.72x against a 5.25x maximum, and has since de-levered through earnings recovery and debt paydown rather than growth. Revenue is still falling: nine month revenue was $1,984.5 million, down 1.9% on the prior year, with net volumes down 2.0% and the decline attributed in part to a deliberate exit of unprofitable volume under the transformation plan (Q3 10-Q page:46). Earnings are recovering from cost action: nine month operating income rose from 46,790 to 80,605 (US$ thousands), while nine month SG&A fell 44.0 million, of which a 15 million bad debt charge in Q2 fiscal 2025 explains part (Q3 10-Q page:46). Company Adjusted EBITDA on a trailing twelve month basis rose from 257,425 at fiscal 2025 year end to 290,437 at July 3, 2026 (US$ thousands, release page:14).

Debt is entirely secured bank debt plus finance leases: term loan A-2 of 436,000 due September 2028 and term loan B-1 of 661,500 due February 2031 (US$ thousands), with the 300 million revolver undrawn. Principal debt fell by 71.0 million from fiscal 2025 year end to July 3, 2026 (calculated below). Cash interest paid on principal debt was 55.7 million for nine months against 64.7 million a year earlier (Q3 10-Q page:16), consistent with lower borrowings and a lower weighted-average rate of 6.23% against 6.80% (Q3 10-Q page:21).

On the metrics used for the charts below (company Adjusted EBITDA, principal debt plus finance leases), total debt over trailing EBITDA moved from 5.19x to 4.33x and net debt over trailing EBITDA from 5.07x to 4.13x between fiscal 2025 year end and July 3, 2026. The company's own covenant ratio, which uses covenant Adjusted EBITDA and adds letters of credit, moved from 4.72x to 4.10x against a maximum of 5.25x stepping to 5.00x (release page:16, Q3 10-Q page:20). Liquidity at July 3, 2026 was 351.8 million, made of 294.2 million of revolver availability and 57.7 million of cash.

Three issues keep the view at medium confidence. First, the executed credit agreement is not in the pack, so the covenant definition is read from summaries, and those summaries define covenant indebtedness to include advances under any receivables facility (Q3 10-Q page:52) while the company's net debt table has no such line (release page:16); the sold receivables balance was 212.3 million at July 3, 2026. Second, the maximum leverage ratio steps down to 4.75x for the quarter ending October 2, 2026 and 4.50x from the first quarter of fiscal 2027 (Q3 10-Q page:20), so today's headroom is not permanent. Third, the receivables facility is scheduled to terminate on August 2, 2027 (Q3 10-Q page:50); because the sold balance is off balance sheet, its end would draw on liquidity. The credit read-through is a deleveraging credit with adequate near-term liquidity and no bank maturity before fiscal 2028, but with a covenant test that tightens, definition risk around receivables, a shrinking top line and an earnings recovery driven by cost reductions and pricing while revenue and volume still decline.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (October 3, 2025) | 5.19 | 5.07 | x | Calculated. Total debt is principal debt plus finance lease obligations; net debt deducts cash. EBITDA is company trailing twelve month Adjusted EBITDA, a management non-GAAP measure. Fiscal 2025 had 53 weeks. Excludes letters of credit, operating leases and receivables facility sales. A second company FY2025 Adjusted EBITDA figure exists (see definition risks). |
| Q1 FY2026 (January 2, 2026) | 5.37 | 5.20 | x | Calculated on the same basis, trailing twelve months to January 2, 2026. Company-reported covenant ratio is lower because it uses covenant Adjusted EBITDA. |
| Q2 FY2026 (April 3, 2026) | 4.72 | 4.54 | x | Calculated on the same basis, trailing twelve months to April 3, 2026. |
| Q3 FY2026 (July 3, 2026) | 4.33 | 4.13 | x | Calculated on the same basis, trailing twelve months to July 3, 2026. Company-reported net leverage under its own definition is 4.10x; the two differ in EBITDA and in letters of credit. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 (October 3, 2025) | 2.75 | x | Calculated. Company trailing twelve month Adjusted EBITDA over cash interest paid on principal debt of 93.6 million (rounded, printed in millions). Excludes finance lease interest and receivables facility fees. |
| Q1 FY2026 (January 2, 2026) | 2.72 | x | Calculated. Trailing cash interest is fiscal 2025 plus Q1 FY2026 less Q1 FY2025, using printed millions rounded to one decimal, so the ratio is accurate to about one hundredth. |
| Q2 FY2026 (April 3, 2026) | 3.11 | x | Calculated on the same basis using six month cash interest figures. |
| Q3 FY2026 (July 3, 2026) | 3.43 | x | Calculated on the same basis using nine month cash interest figures. The covenant uses interest expense rather than cash interest; see the calculations. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (October 3, 2025) | 29.7 | 268.2 | US$m | Cash as printed. Undrawn is the 300 million revolver less 26.0 drawn and 5.8 letters of credit, as printed in the debt note. Receivables facility availability not supplied. |
| Q1 FY2026 (January 2, 2026) | 41.5 | 275.2 | US$m | Revolver less 19.0 drawn and 5.8 letters of credit. Receivables facility availability not supplied. |
| Q2 FY2026 (April 3, 2026) | 50.3 | 294.2 | US$m | Revolver undrawn less 5.8 letters of credit. Receivables facility availability not supplied. |
| Q3 FY2026 (July 3, 2026) | 57.7 | 294.2 | US$m | Revolver undrawn less 5.8 letters of credit; company total liquidity 351.8. Revolver matures September 29, 2028; the receivables facility is scheduled to end August 2, 2027 and is not counted. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2026 | 0.0 | US$m | Principal at July 3, 2026 by contractual maturity date from the debt note; the 10-Q prints no schedule. The 10-K says prior prepayments satisfied quarterly principal obligations through maturity. No receivables facility amounts included. |
| FY2027 | 0.0 | US$m | Same basis. The receivables facility (212.3 sold) is scheduled to terminate August 2, 2027, in fiscal 2027, and is not debt maturing here. |
| FY2028 | 436.0 | US$m | Term loan A-2 due September 2028. The 300 million revolver (undrawn) also matures September 29, 2028. At October 3, 2025 the 10-K printed 503.5 for 2028, which included 26.0 of revolver borrowings. |
| FY2029 | 0.0 | US$m | Same basis. |
| FY2030 | 0.0 | US$m | Same basis. |
| FY2031 | 661.5 | US$m | Term loan B-1 due February 2031; the 10-K prints this tranche as thereafter. Total of the rows equals principal debt of 1,097.5. |

### Financials and credit metrics

| Line (US$ thousands unless stated) | Q3 FY2026 (3 months to Jul 3, 2026) | Q3 FY2025 (3 months to Jun 27, 2025) | 9M FY2026 (to Jul 3, 2026) | 9M FY2025 (to Jun 27, 2025) | FY2025 (53 weeks to Oct 3, 2025) | LTM to Jul 3, 2026 | Source and basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue | 661,663 | 673,799 | 1,984,488 | 2,022,828 | 2,734,839 | 2,696,499 | Release page:12 and page:14; 10-K page:89; LTM as printed |
| Cost of services (excl. D&A) | 476,269 | 491,681 | 1,454,238 | 1,476,932 | 2,010,082 | Not printed | Release page:12; 10-K page:89; LTM not printed |
| Depreciation and amortization | 33,272 | 34,856 | 102,181 | 107,674 | 143,017 | 137,524 | Release page:12 and page:14 |
| SG&A | 114,874 | 122,301 | 347,464 | 391,432 | 517,309 | Not printed | Release page:12; 10-K page:89 |
| Operating income | 37,248 | 24,961 | 80,605 | 46,790 | 64,431 | Not printed | Release page:12; 10-K page:89 |
| Interest expense, net | 20,118 | 22,495 | 63,374 | 67,921 | 92,264 | 87,717 | Release page:12 and page:14 |
| Other expense, net (mainly receivables facility fees) | 2,786 | 3,215 | 8,935 | 10,120 | 13,689 | Not printed | Release page:12; Q3 10-Q page:44 |
| Pre-tax income (loss) | 14,344 | (749) | 8,296 | (33,401) | (44,306) | Not printed | Release page:12; 10-K page:89 |
| Income tax provision (benefit) | 3,298 | (73) | 1,045 | (5,727) | (4,083) | 2,689 | Release page:12 and page:14 |
| Net income (loss) | 11,046 | (676) | 7,251 | (27,674) | (40,223) | (5,298) | Release page:12 and page:14 |
| EBITDA unadjusted (net income + tax + interest + D&A), calculated | 67,734 | 56,602 | 173,851 | 142,194 | 190,975 | 222,632 | Calculated; see Calculations |
| Adjusted EBITDA (company, non-GAAP) | 80,851 | 64,007 | 225,781 | 192,769 | 257,425 | 290,437 | Release page:14; management add-backs |
| Covenant Adjusted EBITDA (company, non-GAAP) | 80,851 | 65,807 | 225,781 | 209,569 | 277,825 | 294,037 | Release page:14; adds covenant-only items |
| Adjusted EBITDA margin (company, %) | 12.2 | 9.5 | 11.4 | 9.5 | 9.4 | 10.8 | Release page:14 |
| Net cash provided by operating activities | 64,935 | 22,864 | 160,873 | 33,302 | 64,229 | 191,800 | Release page:13; 10-K page:91; LTM calculated |
| Purchases of property and equipment and other | (17,955) | (14,860) | (40,031) | (43,102) | (58,460) | (55,389) | Release page:13; 10-K page:91; LTM calculated |
| Free cash flow (operating cash flow less purchases), calculated | 46,980 | 8,004 | 120,842 | (9,800) | 5,769 | 136,411 | Calculated; company prints 46,980, 8,004, 120,842 and (9,800) for the first four columns (release page:16) |
| Payments of financing lease obligations | (9,519) | (8,808) | (28,220) | (25,630) | (34,496) | Not calculated | Release page:13 and page:14; 10-K page:92 |
| Dividend payments | 0 | 0 | 0 | (13,822) | (13,822) | Not calculated | Release page:14; 10-K page:92; the cash flow shows a dash for the nine months of fiscal 2026 |
| Cash interest paid on principal debt (US$ millions) | 17.5 | 20.9 | 55.7 | 64.7 | 93.6 | 84.6 | Q3 10-Q page:16; 10-K page:113; LTM calculated |

## Calculations

All calculations use figures printed in the sources. Money is US$ thousands unless stated. Rounding follows the stated precision.

### Period-end debt, liquidity and covenant position (printed and calculated)

| Item | FY2025 (Oct 3, 2025) | Q1 FY2026 (Jan 2, 2026) | Q2 FY2026 (Apr 3, 2026) | Q3 FY2026 (Jul 3, 2026) | Source |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 29,748 | 41,547 | 50,340 | 57,659 | Release page:16; Q3 10-Q page:6 |
| Term loan A-2 due September 2028 | 477,500 | 477,500 | 466,000 | 436,000 | Q1 10-Q page:17; Q2 10-Q page:19; Q3 10-Q page:19 |
| Term loan B-1 due February 2031 | 665,000 | 665,000 | 661,500 | 661,500 | same |
| Revolver drawn (US$300 million commitment) | 26,000 | 19,000 | 0 | 0 | same |
| Total principal debt | 1,168,500 | 1,161,500 | 1,127,500 | 1,097,500 | same; release page:16 |
| Unamortized debt issuance costs and discounts | (13,357) | (12,707) | (12,043) | (11,366) | Sum of the two printed lines on each date |
| Long-term borrowings, net (balance sheet) | 1,155,143 | 1,148,793 | 1,115,457 | 1,086,134 | same |
| Letters of credit outstanding | 5,818 | 5,818 | 5,818 | 5,818 | Release page:16 |
| Finance lease obligations | 166,305 | 162,738 | 164,717 | 159,723 | Release page:16 |
| Operating lease liabilities | 97,221 | 96,116 | 97,424 | 92,984 | 10-K page:121; sum of current and noncurrent on each 10-Q balance sheet |
| Receivables sold and derecognized (US$ millions) | 202.5 | 217.2 | 211.3 | 212.3 | 10-K page:147; 10-Q MD&A liquidity sections |
| Total equity | 865,644 | 864,428 | 867,202 | 877,671 | Balance sheets |
| Company Net Debt (principal + letters of credit + finance leases - cash) | 1,310,875 | 1,288,509 | 1,247,695 | 1,205,382 | Release page:16 |
| TTM Covenant Adjusted EBITDA | 277,825 | 267,006 | 278,992 | 294,037 | Release page:16 |
| Company Net Leverage Ratio (x) | 4.72 | 4.83 | 4.47 | 4.10 | Release page:16 |
| Maximum net leverage covenant (x) | 5.25 | 5.25 | 5.25 | 5.00 | 10-K page:115; Q3 10-Q page:20 |
| Headroom to maximum, calculated (x) | 0.53 | 0.42 | 0.78 | 0.90 | Maximum less reported ratio, using unrounded ratio |
| EBITDA cushion before breach, calculated | 28,135 | 21,576 | 41,336 | 52,961 | Covenant EBITDA less (company Net Debt / maximum) |
| EBITDA cushion as share of covenant EBITDA, calculated (%) | 10.1 | 8.1 | 14.8 | 18.0 | Cushion / covenant EBITDA |

### Calculation steps

- Principal debt reduction: 1,168,500 less 1,097,500 equals 71,000 (US$ thousands) between October 3, 2025 and July 3, 2026.
- Total debt for the leverage chart: principal debt plus finance lease obligations. FY2025: 1,168,500 + 166,305 = 1,334,805. Q1: 1,161,500 + 162,738 = 1,324,238. Q2: 1,127,500 + 164,717 = 1,292,217. Q3: 1,097,500 + 159,723 = 1,257,223.
- Net debt for the chart: total debt less cash. FY2025: 1,334,805 - 29,748 = 1,305,057. Q1: 1,324,238 - 41,547 = 1,282,691. Q2: 1,292,217 - 50,340 = 1,241,877. Q3: 1,257,223 - 57,659 = 1,199,564.
- Trailing twelve month Adjusted EBITDA (company): 257,425; 246,606; 273,592; 290,437 (release page:16). Total debt / EBITDA: 1,334,805 / 257,425 = 5.185 (5.19); 1,324,238 / 246,606 = 5.370 (5.37); 1,292,217 / 273,592 = 4.723 (4.72); 1,257,223 / 290,437 = 4.329 (4.33). Net debt / EBITDA: 1,305,057 / 257,425 = 5.070 (5.07); 1,282,691 / 246,606 = 5.201 (5.20); 1,241,877 / 273,592 = 4.539 (4.54); 1,199,564 / 290,437 = 4.130 (4.13).
- Trailing cash interest paid on principal debt (US$ millions, printed to one decimal): FY2025 93.6. Q1: 93.6 + 20.1 - 23.2 = 90.5 (Q1 10-Q page:15). Q2: 93.6 + 38.3 - 43.8 = 88.1 (Q2 10-Q page:16). Q3: 93.6 + 55.7 - 64.7 = 84.6 (Q3 10-Q page:16).
- Interest cover: 257.425 / 93.6 = 2.750; 246.606 / 90.5 = 2.725; 273.592 / 88.1 = 3.105; 290.437 / 84.6 = 3.433.
- Covenant-style interest cover, indicative only: the covenant is Adjusted EBITDA over consolidated interest expense, minimum 2.00x (Q3 10-Q page:52). The company does not print the ratio. Covenant Adjusted EBITDA over interest expense, net: Q3 LTM 294,037 / 87,717 = 3.352 (3.35x); FY2025 277,825 / 92,264 = 3.011 (3.01x). The agreement's definition of consolidated interest expense is not supplied, so these are not compliance figures.
- Cover including receivables facility fees, mixed basis: securitization fees LTM 12,163 (release page:14). LTM Adjusted EBITDA adds these fees back, so charging them as a financing cost: 290.437 / (84.6 + 12.163) = 3.002 (3.00x). Cash interest is on a paid basis and the fees are on an expense basis.
- EBITDA unadjusted: Q3 FY2026 11,046 + 3,298 + 20,118 + 33,272 = 67,734. Q3 FY2025: -676 + -73 + 22,495 + 34,856 = 56,602. 9M FY2026: 7,251 + 1,045 + 63,374 + 102,181 = 173,851. 9M FY2025: -27,674 + -5,727 + 67,921 + 107,674 = 142,194. FY2025: -40,223 + -4,083 + 92,264 + 143,017 = 190,975. LTM: -5,298 + 2,689 + 87,717 + 137,524 = 222,632.
- Free cash flow: Q3 FY2026 64,935 - 17,955 = 46,980. Q3 FY2025 22,864 - 14,860 = 8,004. 9M FY2026 160,873 - 40,031 = 120,842. 9M FY2025 33,302 - 43,102 = -9,800. FY2025 64,229 - 58,460 = 5,769. LTM operating cash flow 64,229 + 160,873 - 33,302 = 191,800; LTM purchases 58,460 + 40,031 - 43,102 = 55,389; LTM free cash flow 191,800 - 55,389 = 136,411. LTM free cash flow over LTM Adjusted EBITDA: 136,411 / 290,437 = 0.470 (47.0%).
- Operating cash flow change, nine months: 160,873 - 33,302 = 127,571. The 10-Q attributes 79.0 million (US$ millions) to changes in operating assets and liabilities (Q3 10-Q page:50). Receivables sold rose 212.3 - 202.5 = 9.8 million between October 3, 2025 and July 3, 2026. Cash paid for transformation costs and severance within nine month operating cash flow: 23,427 + 10,829 = 34,256 (release page:16).
- Static covenant sensitivity at July 3, 2026 balances (not a forecast): company Net Debt 1,205,382 divided by the next maxima. At 4.75x, EBITDA must be at least 1,205,382 / 4.75 = 253,765, a cushion of 294,037 - 253,765 = 40,272 (13.7%). At 4.50x, 1,205,382 / 4.50 = 267,863, a cushion of 26,174 (8.9%). The first applies to the quarter ending October 2, 2026 and the second from the first quarter of fiscal 2027 (Q3 10-Q page:20).
- Receivables facility sensitivity, illustrative: adding the 212.3 million sold balance to company Net Debt at July 3, 2026 gives (1,205,382 + 212,300) / 294,037 = 4.82x, against the 5.00x maximum. The same exercise for October 3, 2025 gives (1,310,875 + 202,500) / 277,825 = 5.45x, above the 5.25x maximum although the company reported compliance (10-K page:116). The covenant therefore evidently does not treat the whole sold balance as indebtedness, or its EBITDA differs; the executed definition is needed. These figures are not covenant measures.
- Liquidity: July 3, 2026 revolver availability 300,000 - 0 - 5,818 = 294,182; plus cash 57,659 = 351,841, equal to the company figure (release page:16). October 3, 2025: 300,000 - 26,000 - 5,818 = 268,182 (10-K prints 268.2); plus cash 29,748 = 297,930.
- Maturities: 436,000 + 661,500 = 1,097,500, equal to principal debt at July 3, 2026.

### Debt, lease and other claims inventory at July 3, 2026

| Claim | Amount | Inside or outside the debt figure | Source |
| --- | --- | --- | --- |
| Term loan A-2, SOFR + 10 bp credit spread adjustment + margin 1.50% to 2.50% (2.50% in Q3), due September 2028 | 436,000 | Inside principal debt | Q3 10-Q page:19 and page:21 |
| Term loan B-1, SOFR + margin 2.0% to 2.25% (2.25% in Q3), due February 2031 | 661,500 | Inside | Q3 10-Q page:19 and page:21 |
| Revolving credit facility, US$300 million commitment, matures September 29, 2028; letters of credit 5,818 | Drawn 0; available 294,182 | Inside when drawn; letters of credit outside debt | Q3 10-Q page:20 |
| Secured status and guarantors | All obligations guaranteed by the company and substantially all wholly-owned domestic material subsidiaries; secured by pledges of 100% of domestic and 65% of foreign direct subsidiary capital stock and by a security interest and mortgages on substantially all tangible assets | Not a figure | 10-K page:116 |
| Finance lease obligations (vehicles mainly) | 159,723 | Outside principal debt; inside covenant indebtedness and company Net Debt | Q3 10-Q page:25; page:52 |
| Operating lease liabilities | 92,984 | Outside debt | Q3 10-Q page:25 |
| Receivables securitization facility, US$250 million, terminates August 2, 2027 | 212.3 million sold and derecognized | Outside balance sheet debt; covenant treatment unresolved | Q3 10-Q page:50 |
| Environmental accruals | 7.7 million current plus 24.2 million noncurrent | Outside debt | Q3 10-Q page:28 |
| Asset retirement obligations | 12.5 million noncurrent | Outside debt | Q3 10-Q page:28 |
| Purchase commitments at October 3, 2025 | 6.2 million | Outside debt | 10-K page:124 |
| Multiemployer defined benefit pension plans | Withdrawal liability exists as a risk; no amount extracted | Outside debt | 10-K page:122 |
| Securities class and derivative litigation | Unspecified damages; no accrual amount extracted | Outside debt | Q3 10-Q pages 28 to 33 |

## Gaps

### Definition risks and conflicts

- Fiscal 2025 Adjusted EBITDA: the outlook tables in the Q2 and Q3 releases show fiscal 2025 actual Adjusted EBITDA of $272.6 million (Q3 release page:4), while the reconciliation shows 257,425 for the twelve months ended October 3, 2025 (release page:14). The difference, 272.6 less 257.425, is 15.175 million. No reconciliation of the two is in the text. This handoff uses 257,425 because it is reconciled to net income; the chart values for FY2025 would be lower in leverage terms if 272.6 were right (total debt / EBITDA 1,334.805 / 272.6 = 4.90x).
- Fiscal 2025 free cash flow: the same outlook table prints $5.9 million while operating cash flow less purchases is 5,769 (US$ thousands). Immaterial, unexplained.
- Covenant indebtedness includes advances under any receivables facility (Q3 10-Q page:52) but the company Net Debt table has no such line (release page:16). Unresolved; see the sensitivity above.
- The company ratio and the chart ratio differ in EBITDA (covenant versus Adjusted) and in letters of credit; neither is a verified covenant calculation because the executed agreement is not supplied.
- Fiscal 2025 had 53 weeks (10-K page:65); fiscal 2025 columns and the 12-month periods are not like-for-like.
- Plan cost estimate rose from 25 to 30 million (10-K page:147) to 35 to 40 million (Q3 10-Q page:42); cost recognised in nine months was 23.2 million consulting and 8.0 million severance.

### Items not supplied or not calculated

- Executed credit agreement, amendments and receivables facility documents: Not supplied (carried from the readiness handoff).
- Covenant interest coverage ratio actually reported by the company: Not supplied; the indicative figure above is calculated.
- Receivables facility availability or undrawn capacity: Not supplied; only the sold balance is stated. The facility is excluded from the liquidity chart.
- Quarterly LTM cost of services, SG&A, operating income and pre-tax income: Not printed; the cells say so rather than calculating from mismatched periods.
- Fiscal 2026 year-end (the fiscal quarter ending October 2, 2026) and anything after August 11, 2026: Not supplied.
- Pension withdrawal liability amount and litigation exposure: no amounts extracted.
- Segment detail (United States and Canada) was reviewed but is not tabulated in the required financial table; nine month reportable segment operating income was 141,525 for the United States and 6,457 for Canada on revenue of 1,802,551 and 181,937 (Q3 10-Q page:34).
- Pounds processed and revenue per pound are management estimates and are not in the filings (release page:12).

### Subsequent events

The pack holds no event after August 11, 2026. Within the fiscal third quarter, the company executed a long-term outsourcing arrangement for transactional support functions (Q3 10-Q page:42) and entered amended offer letters with its interim chief financial officer on June 12, 2026 (Q3 10-Q page:56). The release says the outsourcing is expected to generate approximately 10 million of annual SG&A savings from fiscal 2027 (release page:2).

## Next module

Proceed to the business and transaction context (CP-1A) with these carried limitations: covenant figures are company-reported and unverified against executed documents; the receivables facility treatment and its August 2, 2027 termination date; the maximum leverage steps (4.75x, then 4.50x); the dividend and buyback restriction until the earlier of a compliant quarter ending after October 2, 2026 or two consecutive quarters at or below 4.50x (Q3 10-Q page:20); the conflict between two fiscal 2025 Adjusted EBITDA figures; and the 53-week fiscal 2025. Later modules should cite figures from this handoff by period label and should state that Q3 FY2026 is the latest period although the context names Q2 FY2026.
