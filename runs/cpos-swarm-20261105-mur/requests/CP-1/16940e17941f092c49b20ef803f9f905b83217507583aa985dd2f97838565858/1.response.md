## Request

Issuer: MURPHY OIL CORP (issuer id mur; ticker MUR; registrant "Murphy Oil Corporation and consolidated subsidiaries"). As-of date and cutoff: 2026-11-05. Pathway: credit_snapshot. Current period q3-2026 (three months and nine months ended September 30, 2026); prior period fy-2025 (year ended December 31, 2025). Reporting currency: USD; the filings state thousands of US dollars and the narrative and non-GAAP tables state millions. All figures in this handoff are US dollars. Nothing dated after 2026-11-05 is used as fact.

Task: the financial base for the credit snapshot. It sets out the reported statement lines, the separately labelled calculation bridges (EBITDA, last-twelve-months, leverage, interest cover, liquidity, maturities), the debt stack and claims outside debt, the covenant position as far as the sources allow, the latest quarter and subsequent events, and the gaps. It is an intermediate handoff for the next modules, not the final report.

Perimeter and periods, applied to every figure below:

- Perimeter: Murphy Oil Corporation consolidated, which includes 100 percent of MP Gulf of Mexico, LLC (MP GOM) with a 20 percent noncontrolling interest (NCI) (EX-99.1 2026-11-04 page:6). The filings and the calculations in this handoff are consolidated, including NCI. The earnings releases state headline and non-GAAP measures excluding NCI; where a release figure is used it is labelled ex-NCI. Debt and cash are consolidated; the release states that its cash is inclusive of NCI (EX-99.1 2026-11-04 page:2).
- Periods: Q1 2026, Q2 2026 and Q3 2026 are the three-month periods ended March 31, June 30 and September 30, 2026; 9M 2026 and 9M 2025 are the nine months ended September 30; FY2025 and FY2024 are calendar years; LTM Q3 2026 is the twelve months ended September 30, 2026, calculated as FY2025 less 9M 2025 plus 9M 2026. A fourth quarter 2025 is not printed and appears only inside the LTM calculation.
- Carried from the CP-0 handoff: no indentures or credit agreement, no ratings, no earnings presentation, an unresolved coupon label on the 2042 notes, the NCI perimeter split, no discrete fourth quarter 2025 and no interim cash taxes. This handoff re-tests each against the sources before relying on it.

## Sources

All sources are public SEC filings and releases; locators use `page:N`, the chunk number of the retained text extraction, not the printed page.

### Issuer sources relied on

| Source (exact name) | sha256 | Use in this handoff |
| --- | --- | --- |
| 10-K_2025-12-31_mur-20251231.htm.jsonl | c16d5d2420f4bb44dfe1750a952efb626f89571137858e2ac70733c2eb2e689d | Audited FY2025 and FY2024 statements, year-end debt, covenants of the previous facility, contractual obligations, pensions, cash taxes |
| 10-Q_2026-03-31_mur-20260331.htm.jsonl | d566f6d07ea8b1f603a66a35f7401d96364d9e6eb05d9a099bfb89d283abc3ab | Q1 2026 statements, liquidity at March 31, 2026 |
| 10-Q_2026-06-30_mur-20260630.htm.jsonl | fce04c2bd9f3b4a6b7e478f16ad61267a81b35840396e9479017f47656dba038 | Six-month cash interest, liquidity at June 30, 2026 |
| 10-Q_2026-09-30_mur-20260930.htm.jsonl | b147365971e4aae7d6b9ba5fb1957e3afe56838663b5e3650eda237bbf2505f6 | Q3 2026 and 9M 2026 statements, debt note, leases, liquidity, segments |
| EX-99.1_2026-05-06_mur-2026q1xex991.htm.jsonl | e744f241b72a8349b639a4aa3e30a129b2d6c215dc449c6dde3de97f6a877f8e | Q1 2026 management non-GAAP measures, ex-NCI production |
| EX-99.1_2026-08-05_mur-2026q2xex991.htm.jsonl | e539fda8d909d906b9600fb569bd69a3204d1238c76ef5932e4e80c62a82c36d | Q2 2026 three-month statements and non-GAAP measures |
| EX-99.1_2026-11-04_mur-2026q3xex991.htm.jsonl | 74bcf894de6bb55cd6cce5e2656dafd86d31eac8462cf1bb5793b8acd23b2fdd | Q3 2026 non-GAAP reconciliations, net debt, guidance, production |

The run `context` file is not issuer evidence and supplies only the as-of date, periods and currency; its ratings, quotes, deal terms and valuation inputs are blank, and blanks are not treated as zero.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 403edb4227a4b11394670d0864302fb8b9a59504dd78e89f0fe1d69a345893bb | Source readiness: source set, locators, conflict on the 2042 notes coupon, perimeter split, gap list |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Leverage is low and liquidity is ample: total debt is 0.89x calculated EBITDA for the twelve months to September 30, 2026, with 2,499.9 million dollars of cash and undrawn revolver. Heavy exploration and development spending keeps free cash flow modest. | Medium | EBITDA is our own calculation including the noncontrolling interest; covenant definitions, indentures and ratings are not in the sources, so headroom and instrument terms are unverified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt rose to 1,634.4 million dollars from 1,385.1 million dollars at year-end 2025, after a new notes issue and a new finance lease. | Leverage still fell because calculated EBITDA rose faster, and no note matures before May 2029. | High |
| Operating cash flow of 1,517.6 million dollars for nine months 2026 was largely absorbed by 1,333.0 million dollars of property additions and dry hole costs. | Free cash flow after dividends of 150.5 million dollars is thin, so distributions and exploration depend on commodity prices. | Medium |
| Liquidity is cash of 500.3 million dollars plus 1,999.6 million dollars undrawn on a revolver that matures in January 2031. | Near-term refinancing risk is low; revolver covenants are known only from the previous facility's description. | Medium |
| Interest cover is 21.29x on interest paid for the twelve months to September 30, 2026, against 15.82x for FY2025. | Cash interest of 86.3 million dollars is below interest expense of 100.9 million dollars; cover on expense is 18.22x. | Medium |
| The 2042 notes show a 5.875% coupon in the annual report and 6.375% in the third quarter report, and filings include the 20 percent noncontrolling interest while releases exclude it. | Match perimeter before comparing figures; the coupon on 339.8 million dollars of notes needs the indenture. | Medium |

### Financial base view

The financial base is sufficient for a credit snapshot of MURPHY OIL CORP, with stated restrictions. Evidence: the audited FY2025 statements and the unaudited Q1 to Q3 2026 statements are complete and tie to the debt note (total debt 1,634.4 million dollars at September 30, 2026 equals current maturities of 11.229 plus long-term debt of 1,623.123 million dollars). Calculated EBITDA (operating income plus DD&A plus impairment, consolidated) is 1,837.5 million dollars for the twelve months to September 30, 2026 against 1,394.0 million dollars for FY2025, so total debt over EBITDA is 0.89x against 0.99x and net debt over EBITDA is 0.62x against 0.72x even though debt rose by 249.3 million dollars. Mechanism: revenue from production rose in the nine months (2,507.9 against 2,076.8 million dollars) on higher realized prices while ex-NCI volumes fell (176,620 against 182,585 BOEPD), and lease operating expenses fell from 605.0 to 436.4 million dollars; the 2025 comparison also carries a 115.0 million dollar impairment that the calculation adds back. Management's own ex-NCI adjusted EBITDA gives a close cross-check: 1,784.8 million dollars for the same twelve months, or 0.92x total debt. Source risk and consequence: the strength of the leverage and cover ratios rests on a high price period and a calculated, NCI-inclusive EBITDA; the free cash flow cushion is small because property additions and dry hole costs of 1,333.0 million dollars absorb most of the 1,517.6 million dollars of operating cash flow, and the balance sheet carries claims outside the debt figure (operating leases, asset retirement obligations, pension and retiree medical, commitments). The metrics therefore support a view of low financial leverage with good near-term liquidity and no note maturity until May 2029, but not a view of covenant headroom, instrument seniority or guarantor coverage, which the sources cannot verify.

### Financials and credit metrics

Reported lines are as printed in the statements and the releases; lines labelled calculated are derived in the Calculations section from reported components. Perimeter: consolidated including NCI, except the last two rows, which are ex-NCI as printed in the releases. Negative values are in parentheses.

| Line (US$m unless stated) | Q1 2026 | Q2 2026 | Q3 2026 | Q3 2025 | 9M 2026 | 9M 2025 | FY2025 | FY2024 | LTM Q3 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue from production | 732.4 | 926.3 | 849.2 | 721.0 | 2,507.9 | 2,076.8 | 2,689.8 | 3,014.9 | 3,120.9 |
| Total revenues and other income | 733.6 | 928.3 | 855.0 | 733.0 | 2,516.8 | 2,094.3 | 2,718.8 | 3,028.5 | 3,141.4 |
| Operating income from continuing operations | 138.3 | 354.7 | 256.5 | 5.8 | 749.4 | 241.9 | 301.2 | 602.6 | 808.8 |
| Depreciation, depletion and amortization | 254.4 | 262.1 | 271.4 | 283.5 | 787.9 | 736.9 | 977.8 | 865.8 | 1,028.7 |
| Impairment of assets (0.0 where no impairment line or a dash is printed) | 0.0 | 0.0 | 0.0 | 115.0 | 0.0 | 115.0 | 115.0 | 62.9 | 0.0 |
| EBITDA, calculated (operating income + DD&A + impairment) | 392.6 | 616.8 | 527.9 | 404.3 | 1,537.3 | 1,093.8 | 1,394.0 | 1,531.3 | 1,837.5 |
| Exploration expenses, including undeveloped lease amortization | 82.8 | 39.3 | 33.1 | 32.5 | 155.2 | 57.4 | 111.7 | 133.5 | 209.5 |
| EBITDAX, calculated (EBITDA + exploration expenses) | 475.5 | 656.1 | 561.0 | 436.8 | 1,692.6 | 1,151.2 | 1,505.7 | 1,664.8 | 2,047.0 |
| Interest expense, net | 29.0 | 24.9 | 24.2 | 24.7 | 78.1 | 73.3 | 96.1 | 105.9 | 100.9 |
| Income (loss) from continuing operations before income taxes | 119.1 | 341.0 | 235.1 | (3.7) | 695.3 | 154.0 | 182.9 | 567.6 | 724.2 |
| Income tax expense | 49.9 | 77.0 | 39.4 | 4.2 | 166.3 | 37.9 | 44.6 | 78.3 | 173.0 |
| Net income (loss) including noncontrolling interest | 68.7 | 263.5 | 195.5 | (8.3) | 527.7 | 116.2 | 138.8 | 486.5 | 550.3 |
| Net income (loss) attributable to Murphy | 53.0 | 232.2 | 171.1 | (3.0) | 456.3 | 92.3 | 104.2 | 407.2 | 468.2 |
| Net cash provided by continuing operations activities | 321.2 | 656.0 | 540.5 | 339.4 | 1,517.6 | 998.2 | 1,247.8 | 1,729.0 | 1,767.3 |
| Property additions and dry hole costs | 387.8 | 478.4 | 466.9 | 149.0 | 1,333.0 | 827.0 | 1,020.6 | 900.1 | 1,526.6 |
| Free cash flow, calculated (operating cash flow less property additions and dry hole costs) | (66.7) | 177.6 | 73.6 | 190.5 | 184.6 | 171.2 | 227.2 | 828.9 | 240.6 |
| Cash dividends paid | 50.2 | 50.2 | 50.2 | 46.4 | 150.5 | 139.8 | 186.2 | 180.0 | 196.9 |
| Repurchase of common stock, including excise tax | 0.8 | 0.0 | 0.0 | 0.0 | 0.8 | 102.6 | 102.6 | 301.4 | 0.8 |
| Interest paid, net of amounts capitalized | 4.9 | 30.5 | 15.2 | 7.8 | 50.6 | 52.4 | 88.1 | 78.8 | 86.3 |
| Cash and cash equivalents (period end) | 378.8 | 483.9 | 500.3 | 426.0 | 500.3 | 426.0 | 377.2 | 423.6 | 500.3 |
| Total debt including finance leases and revolver (period end) | 1,550.7 | 1,550.4 | 1,634.4 | Not supplied: Sep 30, 2025 balance sheet not in pack | 1,634.4 | Not supplied: Sep 30, 2025 balance sheet not in pack | 1,385.1 | 1,275.4 | 1,634.4 |
| Net debt, calculated (period end) | 1,171.9 | 1,066.6 | 1,134.1 | Not supplied: needs Sep 30, 2025 debt | 1,134.1 | Not supplied: needs Sep 30, 2025 debt | 1,007.9 | 851.8 | 1,134.1 |
| Total debt / EBITDA (x) | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | 0.99 | 0.83 | 0.89 |
| Net debt / EBITDA (x) | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | 0.72 | 0.56 | 0.62 |
| EBITDA / interest paid (x) | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | Not calculated: annual or LTM basis only | 15.82 | 19.43 | 21.29 |
| Net production excluding NCI (BOEPD, release) | 174,236 | 168,995 | 186,495 | 200,383 | 176,620 | 182,585 | Not supplied: no ex-NCI figure | Not supplied: no ex-NCI figure | Not supplied: no ex-NCI figure |
| Adjusted EBITDA attributable to Murphy, management non-GAAP (US$m) | 382.9 | 592.7 | 510.9 | 390.6 | 1,486.5 | 1,064.1 | 1,362.4 | 1,519.5 | 1,784.8 (calculated: 1,362.4 - 1,064.1 + 1,486.5) |

### Debt stack at September 30, 2026

Source: 10-Q Q3 2026 page:13-15 unless stated. Amounts in US$ thousands as printed. Issuer for every note line is Murphy Oil Corporation per the indenture exhibit list (10-K page:83-84); security, guarantors, ranking and covenants of the notes are not printed in the notes read (see Gaps).

| Instrument | Principal or carrying amount | Rate | Maturity | Security and guarantors as printed | Locator |
| --- | --- | --- | --- | --- | --- |
| Notes due May 2029 | 117,582 | 7.050% | May 2029 | Not printed; indenture is a 1999 supplemental indenture with SunTrust Bank as trustee (10-K page:83) | 10-Q Q3 page:13 |
| Notes due October 2032 | 600,000 | 6.000% | October 1, 2032; interest April 1 and October 1 | Not printed | 10-Q Q3 page:13; 10-K page:114 |
| Notes due February 2034 | 500,000 | 6.500% | February 15, 2034; interest February 15 and August 15 from August 15, 2026; issued January 23, 2026 with 8.3 million dollars of costs | Not printed; described as senior notes | 10-Q Q3 page:13, page:15; 10-K page:114 |
| Notes due December 2042 | 339,761 | 6.375% in 10-Q Q3; 5.875% in 10-K; footnote says the coupon can move 25 basis points on rating changes | December 2042 | Not printed | 10-Q Q3 page:13-14; 10-K page:112-113 |
| Total notes payable | 1,557,343 | | | | 10-Q Q3 page:13 |
| Unamortized debt issuance cost and discount | (17,712) | | | Not allocated by note | 10-Q Q3 page:13 |
| Total notes payable, net | 1,539,631 | | | | 10-Q Q3 page:13 |
| Finance lease obligations | 94,721, of which 83.9 million dollars is for the Vietnam floating storage and offloading vessel | Weighted average discount rate 7.1% | Due through October 2039 | Lease; not applicable | 10-Q Q3 page:14, page:32-33 |
| Total debt including current maturities | 1,634,352 (current 11,229; long-term 1,623,123) | | | | 10-Q Q3 page:14 |
| Amended revolving credit facility, 2.0 billion dollars | Drawn nil; 0.4 million dollars of letters of credit | 6.16% in effect on borrowings | January 2, 2031 | Senior unsecured, guaranteed; borrowers Murphy Oil Corporation, Murphy Exploration & Production Company - International and Murphy Oil Company Ltd.; guarantors Murphy Exploration & Production Company and Murphy Exploration & Production Company - USA (named in the Second Amendment exhibit, 10-K page:85) | 10-Q Q3 page:14; 10-K page:85 |

Redeemed in Q1 2026: the remaining 78.9 million dollars of 5.875% notes due 2027 and 148.6 million dollars of 6.375% notes due 2028, 227.5 million dollars in aggregate, for a total extinguishment cost of 3.5 million dollars (2.5 cash, 1.0 non-cash) (10-Q Q3 page:15). The previous 1.35 billion dollar facility maturing October 7, 2029 carried 100.0 million dollars of borrowings at December 31, 2025 (10-K page:113) and was replaced by the Amended RCF in January 2026. A shelf registration permits offerings through October 15, 2027 (10-Q Q3 page:14).

Bridge of total debt from December 31, 2025 to September 30, 2026 (US$ thousands, all from page:13-14 of 10-Q Q3): 1,385,080 at year-end (notes net 1,272,426, finance leases 12,654, revolver 100,000) plus net notes change 267,205 less revolver repayment 100,000 plus finance lease change 82,067 equals 1,634,352 (see Calculations).

### Claims outside the debt figure

| Claim | Amount and date | Inside or outside the debt figure | Locator |
| --- | --- | --- | --- |
| Operating lease liabilities (present value) | 653.8 million dollars at September 30, 2026 (current 229.5, non-current 424.3); 816.6 million dollars at December 31, 2025; undiscounted future minimum payments 815.1 million dollars | Outside | 10-Q Q3 page:2, page:32 |
| Finance lease liabilities | 94.7 million dollars at September 30, 2026; undiscounted payments 134.4 million dollars | Inside | 10-Q Q3 page:14, page:32 |
| Asset retirement obligations | 1,065.4 million dollars at September 30, 2026 (current 46.9, non-current 1,018.5) against 1,012.9 million dollars at January 1, 2026 | Outside | 10-Q Q3 page:15 |
| Pension and retiree medical | Net plan liabilities at December 31, 2025: pension 132.4 million dollars, other postretirement benefits 63.4 million dollars; 9M 2026 contributions 22.5 million dollars, remaining 2026 funding expected 8.1 million dollars; funded status at September 30, 2026 not printed | Outside | 10-K page:124; 10-Q Q3 page:16 |
| Capital expenditure, drilling rig and other commitments | 1,648.0 million dollars undiscounted at December 31, 2025, including Canadian pipeline commitments of 72.2 (2026), 141.1 (2027-2028), 81.0 (2029-2030) and 235.9 million dollars (after 2030) and Vietnam support commitments; minimum transportation payments run through 2045 (US) and 2051 (Canada onshore) | Outside | 10-K page:73-74 |
| New deepwater drillship agreement (October 2026) | Approximately 225 million to 325 million dollars gross for the initial ten-well term, starting in Q1 2027; not recognized at September 30, 2026 | Outside; subsequent event | 10-Q Q3 page:32 |
| Letters of credit | 211.8 million dollars outstanding at December 31, 2025 in total; only 0.4 million dollars reduce the revolver; the September 30, 2026 total is not printed | Outside | 10-K page:74; 10-Q Q3 page:14 |
| Noncontrolling interest in MP GOM | Equity 168.6 million dollars at September 30, 2026; distributions of 21.2 million dollars in 9M 2026 against 43.2 million dollars in 9M 2025 | Outside; claim on a consolidated subsidiary's cash | 10-Q Q3 page:3, page:5 |
| Factoring, supply-chain finance, consent decrees | Searched for factoring, supply chain finance, receivables sale, consent decree and surety in the 10-K, the Q3 10-Q and the Q3 release: none found. Legal proceedings are described as routine and not expected to have a material effect | Not applicable on the sources read | 10-Q Q3 page:56 |

### Liquidity at September 30, 2026

| Component | US$ million | Locator |
| --- | --- | --- |
| Cash and cash equivalents (includes NCI; 105.1 held outside the United States) | 500.3 | 10-Q Q3 page:2, page:47 |
| Amended RCF commitment | 2,000.0 | 10-Q Q3 page:14 |
| Less drawn borrowings | 0.0 (nil outstanding) | 10-Q Q3 page:14 |
| Less letters of credit issued under the RCF | 0.4 | 10-Q Q3 page:14 |
| Undrawn committed capacity | 1,999.6 | calculated |
| Cash plus undrawn committed capacity | 2,499.9 | calculated; the release prints approximately 2.50 billion dollars (EX-99.1 2026-11-04 page:2) |

The only committed facility is the Amended RCF, which expires January 2, 2031, so no facility expires within twelve months of September 30, 2026. Working capital is a liability of 57.2 million dollars (current assets 1,065.1, current liabilities 1,122.3) (10-Q Q3 page:47). For comparison at December 31, 2025: cash 377.2 plus 1,249.6 undrawn on the previous 1.35 billion dollar facility gives 1,626.8 million dollars at December 31, 2025, which the 10-K calls approximately 1.6 billion dollars (10-K page:60).

### Covenants and definitions

| Test | Level and source | Issuer-reported figure | Indicative comparison, not covenant headroom |
| --- | --- | --- | --- |
| Maximum consolidated leverage ratio before the Investment Grade Ratings Date | 3.25x, from the 10-K description of the previous facility (10-K page:113) | None printed; the 10-Qs state only compliance with all covenants (10-Q Q3 page:14) | Calculated total debt / EBITDA 0.89x; definition of the covenant ratio is not supplied |
| Minimum consolidated interest coverage ratio before that date | 2.50x (10-K page:113) | None printed | Calculated EBITDA / interest paid 21.29x and EBITDA / interest expense 18.22x; definition not supplied |
| Maximum ratio of consolidated total debt to consolidated total capitalization from the Investment Grade Ratings Date | 60% (10-K page:113) | None printed | The Q3 10-Q capital employed table prints long-term debt of 1,623.1 over 7,008.0 total capital employed, 23.2 percent (10-Q Q3 page:47); that measure excludes current maturities and NCI equity, so it differs from the covenant definition |

Whether the Investment Grade Ratings Date has occurred is not stated in any source, so which test set applies to the Amended RCF is unknown. The Amended RCF terms are described as substantially similar to the previous facility except for pricing mechanics (10-Q Q3 page:14); the agreement itself is not in the pack.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 0.83 | 0.56 | x | Calculated, consolidated including NCI. Total debt 1,275.4 (notes net plus finance leases, no revolver) and cash 423.6 at December 31, 2024 over EBITDA of 1,531.3 (operating income plus DD&A plus impairment of 62.9), US$m. Excludes operating leases and asset retirement obligations. |
| FY2025 | 0.99 | 0.72 | x | Calculated, consolidated including NCI. Total debt 1,385.1 including the 100.0 revolver draw and cash 377.2 at December 31, 2025 over EBITDA of 1,394.0 (includes a 115.0 impairment add-back), US$m. Management ex-NCI adjusted EBITDA is 1,362.4 (10-K page:64), which gives 1.02x and 0.74x. Excludes operating leases and asset retirement obligations. |
| LTM Q3 2026 | 0.89 | 0.62 | x | Calculated, consolidated including NCI. Total debt 1,634.4 and cash 500.3 at September 30, 2026 over LTM EBITDA of 1,837.5 (FY2025 less 9M 2025 plus 9M 2026), US$m. EBITDA is not the covenant or management definition. Cross-check on management ex-NCI adjusted EBITDA (1,784.8 LTM): 0.92x total debt and 0.64x net debt, mixing consolidated debt with ex-NCI earnings. Excludes operating leases of 653.8 and asset retirement obligations of 1,065.4. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 19.43 | x | Calculated EBITDA of 1,531.3 over interest paid net of amounts capitalized of 78.8 (10-K page:131), US$m. Consolidated including NCI. |
| FY2025 | 15.82 | x | Calculated EBITDA of 1,394.0 over interest paid net of amounts capitalized of 88.1 (10-K page:131), US$m. Interest expense net was 96.1, which gives 14.51x. |
| LTM Q3 2026 | 21.29 | x | Calculated LTM EBITDA of 1,837.5 over LTM interest paid of 86.3 (FY2025 88.1 less 9M 2025 52.4 plus 9M 2026 50.6), US$m. Cash interest is net of 15.7 capitalized in 9M 2026 and is below the 100.9 interest expense net (18.22x); the sources do not bridge the two. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| December 31, 2025 | 377.2 | 1249.6 | US$m | Cash from the 10-K balance sheet; undrawn is the previous 1,350.0 facility less 100.0 drawn and 0.4 of letters of credit (10-K page:60, page:113). Facility was replaced in January 2026. |
| March 31, 2026 | 378.8 | 1999.6 | US$m | Amended RCF of 2,000.0 less 0.4 of letters of credit, nothing drawn (10-Q Q1 page:36). Cash includes NCI. |
| June 30, 2026 | 483.9 | 1999.6 | US$m | Same facility and letters of credit (10-Q Q2 page:46). Cash includes NCI. |
| September 30, 2026 | 500.3 | 1999.6 | US$m | Same facility and letters of credit (10-Q Q3 page:14, page:47). Cash includes NCI and 105.1 held outside the United States. Letters of credit issued outside the revolver (211.8 in total at December 31, 2025) are not netted because the issuing lines are not identified. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 0.0 | US$m | No note or drawn borrowing is listed as maturing; the note schedule at September 30, 2026 lists none (10-Q Q3 page:13). Principal only; finance lease payments (6.4 undiscounted in the rest of 2026) are excluded. |
| 2027 | 0.0 | US$m | The 5.875% notes due 2027 were redeemed in Q1 2026 (10-Q Q3 page:15). Finance lease payments of 15.0 undiscounted excluded. |
| 2028 | 0.0 | US$m | The 6.375% notes due 2028 were redeemed in Q1 2026. Finance lease payments of 15.0 undiscounted excluded. |
| 2029 | 117.6 | US$m | 7.050% notes due May 2029, principal 117.582. Finance lease payments of 14.2 undiscounted excluded. |
| 2030 | 0.0 | US$m | No maturity listed. Finance lease payments of 13.6 undiscounted excluded. |
| 2031 | 0.0 | US$m | Amended RCF of 2,000.0 matures January 2, 2031 and is undrawn, so no debt matures from it at September 30, 2026. |
| 2032 | 600.0 | US$m | 6.000% notes due October 2032, principal. |
| 2033 | 0.0 | US$m | No maturity listed. |
| 2034 | 500.0 | US$m | 6.500% notes due February 2034, principal. |
| 2035 to 2041 | 0.0 | US$m | No maturity listed for these years; finance lease payments continue through October 2039 (remaining undiscounted payments after 2030 of 70.1). |
| 2042 | 339.8 | US$m | Notes due December 2042, principal 339.761; coupon label conflicts between filings. |

Maturity dates are the dates in the note captions of the Q3 10-Q debt table; the filing prints no maturity schedule for September 30, 2026. The 10-K schedule at December 31, 2025 (nil in 2026, 78.9 in 2027, 148.6 in 2028, 217.6 in 2029, nil in 2030, 939.8 thereafter, US$m) pre-dates the redemptions and the 2034 notes (10-K page:113).

### Latest quarter, subsequent events and guidance

- Financing events in 2026: Amended RCF of 2.0 billion dollars effective January 2, 2026 with 12.3 million dollars of costs (10-Q Q3 page:14); 500.0 million dollars of 6.500% notes due 2034 closed January 23, 2026 with 8.3 million dollars of costs; 227.5 million dollars of 2027 and 2028 notes redeemed; the 100.0 million dollar revolver draw repaid (net 2026 revolver activity: borrowings 700.0, repayments 800.0, 10-Q Q3 page:4).
- Q3 2026: a finance lease for the Lac Da Vang floating storage and offloading vessel in Vietnam commenced, with a right-of-use asset of 103.4 million dollars, a lease liability of 83.9 million dollars and about 19.5 million dollars paid before commencement, term September 2026 to October 2039 (10-Q Q3 page:32). Total debt rose by 83.9 million dollars from 1,550.4 million dollars at June 30, 2026, which the release rounds to approximately 80 million dollars (EX-99.1 2026-11-04 page:2).
- Q3 2026 operations: production 186,495 BOEPD ex-NCI against guidance of 171,000 to 179,000; Chinook #8 online and Lac Da Vang first oil; full-year 2026 production guidance raised to 176,000 to 178,000 BOEPD (EX-99.1 2026-11-04 page:2). No share repurchases in Q3; 550 million dollars remains authorized; dividends of 0.35 dollars per share, 50.2 million dollars (10-Q Q3 page:3, page:4, page:53).
- Guidance: Q4 2026 capital expenditure of 190 million dollars and full-year 2026 of 1,500 to 1,600 million dollars, both ex-NCI; full-year exploration expense of 195 million dollars including 90 million dollars of dry hole expense (EX-99.1 2026-11-04 page:3). Nine-month capital expenditures attributable to Murphy were 1,363.2 million dollars (page:12).
- Management non-GAAP, ex-NCI, Q3 2026: adjusted EBITDA 510.9, free cash flow 48.2, and adjusted free cash flow of (8.4) after dividends, debt costs, acquisitions and other items; nine months adjusted free cash flow (32.2) (EX-99.1 2026-11-04 page:10). Net debt per management 1,134.0 million dollars at September 30, 2026 (page:11).
- Subsequent to quarter end, within the cutoff: October 2026 drillship agreement (225 million to 325 million dollars gross, initial ten wells); six Gulf of America exploration blocks secured from the August lease sale and agreements with Mauritania for two offshore blocks (10-Q Q3 page:32, page:34); amended by-laws adopted November 4, 2026 (page:57). An August 2026 produced water release from a pipeline in the Tupper Montney West field is under monitoring and remediation; no amount is stated (page:26).

### Consistency with the CP-0 handoff

Nothing in CP-0 is contradicted by the statements read here. Three additions to it: the 10-K itself reconciles FY2025 and FY2024 non-GAAP EBITDA (10-K page:63-64), which CP-0 did not list; the Q1 10-Q and Q2 release cash flow figures for the three months do not sum exactly to the six-month figure (see Calculations); and the company's free cash flow removes working capital changes and excludes NCI, so calculated free cash flow here differs from the release by definition.

## Calculations

All inputs are from the cited pages, in US$ thousands unless stated; results are rounded for display. Nothing is taken from outside the sources.

### Definitions

- EBITDA (calculated) = operating income from continuing operations + depreciation, depletion and amortization + impairment of assets. It is consolidated, includes NCI, excludes other income (loss) (which carries foreign exchange gains and losses) and keeps accretion of asset retirement obligations and exploration expenses as costs. EBITDAX = EBITDA + exploration expenses, including undeveloped lease amortization. These are not the management definitions, which start from net income attributable to Murphy, exclude NCI, add back accretion and remove foreign exchange and derivative items (EX-99.1 2026-11-04 page:9-10).
- LTM Q3 2026 = FY2025 + 9M 2026 - 9M 2025, applied to each flow line.
- Total debt = total debt including current maturities (notes net of discount plus finance leases) plus the revolver draw. Net debt = total debt less cash and cash equivalents.
- Free cash flow (calculated) = net cash provided by continuing operations activities less property additions and dry hole costs, without removing working capital changes and including NCI.

### EBITDA by period

| Period | Operating income | DD&A | Impairment | EBITDA | Locator |
| --- | --- | --- | --- | --- | --- |
| Q1 2026 | 138,265 | 254,376 | 0 | 392,641 | 10-Q Q1 page:3 |
| Q2 2026 | 354,668 | 262,106 | 0 | 616,774 | EX-99.1 2026-08-05 page:9 |
| Q3 2026 | 256,484 | 271,432 | 0 | 527,916 | 10-Q Q3 page:3 |
| Q3 2025 | 5,793 | 283,465 | 115,002 | 404,260 | 10-Q Q3 page:3 |
| 9M 2026 | 749,417 | 787,914 | 0 | 1,537,331 | 10-Q Q3 page:3 |
| 9M 2025 | 241,898 | 736,949 | 115,002 | 1,093,849 | 10-Q Q3 page:3 |
| FY2025 | 301,237 | 977,753 | 115,002 | 1,393,992 | 10-K page:94 |
| FY2024 | 602,593 | 865,753 | 62,909 | 1,531,255 | 10-K page:94 |
| LTM Q3 2026 | 749,417 + 301,237 - 241,898 = 808,756 | 787,914 + 977,753 - 736,949 = 1,028,718 | 0 + 115,002 - 115,002 = 0 | 1,393,992 - 1,093,849 + 1,537,331 = 1,837,474 | calculated |

Check: Q1 + Q2 + Q3 2026 = 392,641 + 616,774 + 527,916 = 1,537,331, equal to 9M 2026. Implied fourth quarter 2025 EBITDA = 1,393,992 - 1,093,849 = 300,143 (not a printed figure). Impairment is shown as zero where the Q3 10-Q states there were no impairments in the three and nine months of 2026 (page:13) and the Q1 and Q2 statements carry no impairment line (10-Q Q1 page:3; EX-99.1 2026-08-05 page:9).

### Debt, net debt and ratios

| Date | Total debt | Cash | Net debt | EBITDA | Total debt / EBITDA | Net debt / EBITDA |
| --- | --- | --- | --- | --- | --- | --- |
| December 31, 2024 | 1,275,373 | 423,569 | 851,804 | 1,531,255 | 0.833 = 0.83x | 0.556 = 0.56x |
| December 31, 2025 | 1,285,080 + 100,000 = 1,385,080 | 377,196 | 1,007,884 | 1,393,992 | 0.994 = 0.99x | 0.723 = 0.72x |
| September 30, 2026 | 1,634,352 | 500,301 | 1,134,051 | 1,837,474 | 0.889 = 0.89x | 0.617 = 0.62x |

Total debt checks: December 31, 2025 equals current maturities 2,514 + long-term debt 1,382,566 = 1,385,080 (10-K page:93). Management net debt is 1,007.8 at year-end 2025 and 1,134.0 at September 30, 2026 (EX-99.1 2026-11-04 page:10-11); the calculated 1,134,051 differs by 0.1 million dollars because the release subtracts rounded millions (1,634.3 - 500.3). Quarter-end debt: March 31, 2026 2,547 + 1,548,147 = 1,550,694; June 30, 2026 2,578 + 1,547,864 = 1,550,442 (10-Q Q1 page:2; EX-99.1 2026-08-05 page:10). Net debt: 1,550,694 - 378,753 = 1,171,941; 1,550,442 - 483,875 = 1,066,567.

Debt bridge, December 31, 2025 to September 30, 2026: notes principal 1,284,832 + 500,000 - 78,899 - 148,590 = 1,557,343; net notes 1,539,631 - 1,272,426 = +267,205; revolver 0 - 100,000 = -100,000; finance leases 94,721 - 12,654 = +82,067; total 1,385,080 + 267,205 - 100,000 + 82,067 = 1,634,352, equal to the printed total. Quarter on quarter: 1,634,352 - 1,550,442 = 83,910, against the 83.9 million dollar finance lease liability recognized in Q3.

Note tie: 117,582 + 600,000 + 500,000 + 339,761 = 1,557,343; less 17,712 = 1,539,631; plus finance leases 94,721 = 1,634,352 (10-Q Q3 page:13-14).

### Cash interest and cover

- Interest paid, net of amounts capitalized: FY2024 78,806 and FY2025 88,119 (10-K page:131); Q1 2026 4,897 (10-Q Q1 page:13); six months 2026 35,442 and 2025 44,577 (10-Q Q2 page:15); nine months 2026 50,612 and 2025 52,426 (10-Q Q3 page:15).
- Derived quarters: Q2 2026 = 35,442 - 4,897 = 30,545; Q3 2026 = 50,612 - 35,442 = 15,170; Q3 2025 = 52,426 - 44,577 = 7,849.
- LTM = 88,119 - 52,426 + 50,612 = 86,305.
- Cover on interest paid: FY2024 1,531,255 / 78,806 = 19.43x; FY2025 1,393,992 / 88,119 = 15.82x; LTM 1,837,474 / 86,305 = 21.29x.
- Cover on interest expense net: FY2025 1,393,992 / 96,072 = 14.51x; LTM interest expense net = 96,072 - 73,302 + 78,093 = 100,863; 1,837,474 / 100,863 = 18.22x.

### Free cash flow and shareholder distributions

| Period | Operating cash flow | Property additions and dry hole costs | Free cash flow (calculated) |
| --- | --- | --- | --- |
| Q1 2026 | 321,184 | 387,838 | -66,654 |
| Q2 2026 | 655,951 | 478,363 | 177,588 |
| Q3 2026 | 540,516 | 466,880 | 73,636 |
| 9M 2026 | 1,517,609 | 1,333,039 | 184,570 |
| 9M 2025 | 998,162 | 827,007 | 171,155 |
| FY2025 | 1,247,808 | 1,020,611 | 227,197 |
| FY2024 | 1,728,990 | 900,108 | 828,882 |
| LTM Q3 2026 | 1,247,808 - 998,162 + 1,517,609 = 1,767,255 | 1,020,611 - 827,007 + 1,333,039 = 1,526,643 | 240,612 |

After dividends and NCI distributions, 9M 2026: 184,570 - 150,528 - 21,164 = 12,878. Property additions for 9M 2025 include the 125.0 million dollar purchase of the Pioneer FPSO (EX-99.1 2026-11-04 page:10, note 1). Discrete-quarter consistency: Q1 3-month and Q2 3-month operating cash flow sum to 321,184 + 655,951 = 977,135 against the six-month 977,093 (10-Q Q2 page:4), and property additions to 387,838 + 478,363 = 866,201 against 866,159; the 42 thousand dollar difference is the same in both lines and is not explained in the sources; the nine-month totals (977,093 + 540,516 = 1,517,609; 866,159 + 466,880 = 1,333,039) tie.

### Management-basis cross-check

Management adjusted EBITDA attributable to Murphy (ex-NCI, non-GAAP): FY2025 1,362.4 and FY2024 1,519.5 (10-K page:64); 9M 2025 1,064.1 and 9M 2026 1,486.5 (EX-99.1 2026-11-04 page:10); quarters 382.9, 592.7 and 510.9 sum to 1,486.5. LTM = 1,362.4 - 1,064.1 + 1,486.5 = 1,784.8. Ratios (consolidated debt and cash over ex-NCI earnings, so a mixed perimeter used only as a cross-check): December 31, 2025 1,385.080 / 1,362.4 = 1.02x and 1,007.884 / 1,362.4 = 0.74x; September 30, 2026 1,634.352 / 1,784.8 = 0.92x and 1,134.051 / 1,784.8 = 0.64x. Management free cash flow ex-NCI, which removes working capital changes: FY2025 301.3 and adjusted free cash flow 12.1 (10-K page:64); 9M 2026 199.6 and (32.2) (EX-99.1 2026-11-04 page:10). Calculated 9M 2026 free cash flow of 184.6 plus the 15.0 working capital add-back equals 199.6.

### Growth rates cited in the base view

Nine months 2026 against 2025: revenue from production 2,507,861 / 2,076,761 - 1 = 20.8 percent; Q3 849,175 / 720,966 - 1 = 17.8 percent; lease operating expenses 436,357 / 604,986 - 1 = -27.9 percent; EBITDA 1,537,331 / 1,093,849 - 1 = 40.5 percent; operating cash flow 1,517,609 / 998,162 - 1 = 52.0 percent. Realized prices: United States onshore crude $86.29 against $66.24 per barrel for nine months, and net production ex-NCI 176,620 against 182,585 BOEPD (EX-99.1 2026-11-04 page:13-14).

### Liquidity and maturities

Liquidity at September 30, 2026: 2,000.0 - 0.0 - 0.4 = 1,999.6 undrawn; 1,999.6 + 500.3 = 2,499.9 (US$m). December 31, 2025: 1,350.0 - 100.0 - 0.4 = 1,249.6 undrawn (equal to the 10-K figure); 1,249.6 + 377.2 = 1,626.8. March 31 and June 30, 2026: 1,999.6 undrawn; cash 378.8 and 483.9.

Maturities (principal, US$m): 117.582 + 600.000 + 500.000 + 339.761 = 1,557.343, equal to total notes payable. The 10-K year-end schedule: 78.9 + 148.6 + 217.6 + 939.8 = 1,384.9 against 1,284.832 notes plus 100.0 revolver = 1,384.832 (rounding); the 217.6 for 2029 equals 117.582 of notes plus the 100.0 revolver draw, consistent with the previous facility maturing in October 2029.

### Covenant indications

3.25x maximum against calculated 0.89x leaves 2.36x of difference; 2.50x minimum against calculated 21.29x leaves 18.79x of difference; 60% maximum against the printed 23.2 percent leaves 36.8 percentage points. These are differences between a stated level and a calculated ratio on a different definition, not covenant headroom, because the covenant definitions are not supplied.

## Gaps

| Gap | Search performed and result | Severity | Consumers | Action |
| --- | --- | --- | --- | --- |
| Indentures, ranking, guarantors and covenants of the notes | Searched the 10-K and the Q3 10-Q for "unsecured", "secured by", "guarant" and "subordinated" outside the revolver text: no description of security or guarantors of the notes. Indentures are listed as exhibits only (10-K page:83-84) | High for instrument-level terms | CP-1A, CP-2, CP-5 | Obtain the indentures, including the Eighth Supplemental Indenture |
| Covenant definitions and issuer-reported ratios for the Amended RCF | The 10-K describes the previous facility's tests (page:113); no ratio value is printed in any source; the Second Amendment is only an exhibit reference (10-K page:85) | High for covenant headroom | CP-2 | Obtain the conformed credit agreement; until then treat the headroom as not calculable |
| Ratings and whether the Investment Grade Ratings Date has occurred | Searched all sources for rating terms (as in CP-0): no current rating and no statement on the date | Medium | CP-2 | Rating source outside the pack |
| Coupon on the 339.8 million dollar notes due 2042 | 5.875% in the 10-K (page:112), 6.375% in the Q3 10-Q (page:13), 5.125% in the exhibit list (10-K page:83); the weighted-average coupon in the release (6.3 percent) fits 6.375% but does not prove it. Interest cost impact between the two labels is 1.7 million dollars a year on 339,761 at 0.5 percentage points (339,761 x 0.005 = 1,699 thousand), stated here only to size the question | Medium | CP-2, CP-5 | Obtain the indenture or the 8-K for the change |
| Management adjusted EBITDA ex-NCI for the twelve months to September 30, 2026 | Not printed: no fourth quarter 2025 release is in the pack. The 10-K prints FY2025 and FY2024 (1,362.4 and 1,519.5, page:64) and the releases print nine months, so the LTM figure of 1,784.8 is calculated | Low | CP-2 | Leverage here uses calculated consolidated EBITDA with the management-basis cross-check |
| Net production and sales ex-NCI for FY2025 and FY2024 | The 10-K states production including NCI; the releases give ex-NCI for 2026 quarters and nine months | Low | CP-1A, CP-2 | Label perimeter when comparing |
| Debt at September 30, 2025 and quarter-end debt for the Q3 2025 comparison | The September 30, 2025 balance sheet is not in the pack (the Q3 2026 10-Q compares with December 31, 2025) | Low | CP-2 | Leverage rows start at FY2024, FY2025 and LTM Q3 2026 |
| Interim cash taxes paid | Searched for taxes paid in all interim reports: none printed; annual cash taxes paid were 6.1 million dollars in 2025 (10-K page:116) | Low | CP-2 | Treat as not supplied for 2026 |
| Letters of credit outside the revolver at September 30, 2026 | 211.8 million dollars in total at December 31, 2025 (10-K page:74); the 10-Qs print only the 0.4 million dollars under the revolver | Low | CP-2 | Not netted in liquidity |
| Pension and retiree medical funded status at September 30, 2026 | Interim notes print expense and contributions only (10-Q Q3 page:16) | Low | CP-2 | Use December 31, 2025 net liabilities of 132.4 and 63.4 million dollars, labelled |
| Per-note carrying value | The 17,712 thousand dollar discount and cost is not allocated by note (10-Q Q3 page:13) | Low | CP-2 | Use principal by note |
| Produced water release in Tupper Montney West | Described without an amount (10-Q Q3 page:26) | Low | CP-2 | Monitor |
| Discrete fourth quarter 2025 | Not printed; EBITDA of 300,143 and interest paid of 35,693 are implied by subtraction only | Low | CP-2 | Use as LTM building blocks only |

Unknown is not zero: none of the gaps above is treated as nil. Subsequent events inside the cutoff are listed under Latest quarter, subsequent events and guidance; nothing used is dated after 2026-11-05.

## Next module

Proceed to CP-1A (business and transaction context). It should carry forward: (1) the perimeter rule, consolidated including the 20 percent NCI in MP GOM for filings and ex-NCI for the releases, with every figure labelled; (2) the debt stack and the maturity profile with no note due before May 2029 and the Amended RCF undrawn to January 2031; (3) the base figures for leverage (0.89x total debt and 0.62x net debt over calculated LTM EBITDA of 1,837.5 million dollars), interest cover (21.29x on interest paid) and liquidity (2,499.9 million dollars); (4) the open items: the coupon on the 2042 notes, the unverified covenant definitions and ratings, and the absence of indentures and the credit agreement; and (5) the growth and spending context for the business narrative: Vietnam and Gulf of America developments, Côte d'Ivoire appraisal, exploration expense of 155.2 million dollars for 9M 2026 including 86.7 million dollars of unsuccessful well costs, the raised 2026 production guidance and the October 2026 drillship commitment. Later modules must re-check any figure they use against the page-level sources and must not describe covenant headroom as verified.
