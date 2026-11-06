## Request

Module: financial statements and credit metrics for BAYTEX ENERGY CORP. (issuer id bte, TSX and NYSE: BTE), as of 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit snapshot. Reporting currency per run context: CAD. All statement amounts in this handoff are thousands of Canadian dollars (C$k) unless a cell or label says C$m (millions) or US$. Current period: Q2 2026 (three months and balance sheet to June 30, 2026). Prior period: FY2025 (year and balance sheet to December 31, 2025). The Q1 2026 column (March 31, 2026) and the Q3 2025 column (September 30, 2025) are included where the sources print them.

Scope: reported figures, debt and claims outside debt, liquidity, covenants, the latest quarter and subsequent events, with separately labelled calculations. No forecast, rating, valuation or normalization of EBITDA is attempted: the issuer reports no EBITDA; its only EBITDA is the credit-agreement "Bank EBITDA", used as printed. This handoff feeds the business-context, synthesis and trace-validation modules and the report section "Financials and credit metrics".

Perimeter: BAYTEX ENERGY CORP. consolidated. The U.S. Eagle Ford business was sold on December 19, 2025 and is presented as discontinued operations (S6 page:4, S3 page:5). "Continuing" or "Canada" means the retained Canadian business; "consolidated" or "total" includes Eagle Ford up to its sale. Every figure below names its perimeter.

## Sources

### Issuer sources relied on

| Alias | Exact source name | sha256 | Used for |
| --- | --- | --- | --- |
| S1 | 40-F_2025-12-31_bte-20251231.htm.jsonl | 7928c3aee2847a067565e87aab941fb0fa693ec3a05da16abf228b0aca516096 | Reviewed; cover document only, no financial figures used |
| S2 | 6-K-EX-99.1_2025-09-30_a991-q32025fs.htm.jsonl | 88b3b8e7d8e11703b95eab9a12edb425d85ec75970d2d968e209a9c3a366a490 | September 30, 2025 balance sheet, prior debt structure and covenants |
| S3 | 6-K-EX-99.1_2025-12-31_a991-2025yepressrelease.htm.jsonl | 3673c1a3e44baf8845d8213620919370a57219f3e6310c71f221c475210c6b47 | FY2025 and Q4 2025 results, year-end debt and net cash, Canada split |
| S4 | 6-K-EX-99.1_2026-03-31_a991-q12026fs.htm.jsonl | 792eab73e1363b4073690efb2135aa655fd77f770258c41719cb471c48ece251 | March 31, 2026 statements, notes and covenants |
| S5 | 6-K-EX-99.1_2026-03-31_tm2613640d2_ex99-1.htm.jsonl | 9b4c8c62190d6a1b8a9c4e232069f5ad6fc7f4c944563935fd4bf5121d096095 | Q1 2026 release and adjusted funds flow split |
| S6 | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | 16eeba2e704f92279ab76d18bdc0c26c8ff5c06bb58d42d66e8037ca77adddf4 | June 30, 2026 statements, notes, covenants, net cash (primary for Q2 2026) |
| S7 | 6-K-EX-99.1_2026-08-05_tm2619297d2_ex99-1.htm.jsonl | 2da1f8d94e5a6b644192e34205faf74054d51d4cb86b7a7a5ff6f34cc5c6aa6a | Q2 2026 release, management discussion, contractual obligations, subsequent events |

Run context (settings, not issuer evidence): /workspace/secdata/data/2026-11-05/contexts/1279495-baytex-energy-corp-bte.json, sha256 a4beb54d12cde8b01d2e19e329c06ce5b476e74c9a66d64a29ea9c069505e245.

### Supplied handoffs

| Module | sha256 | Consumed for |
| --- | --- | --- |
| CP-0 | 68599e57819209c904b32c5e729b1780b103c65bf8c26f89178fef7d84c1f1ef | Source readiness: S4 inside S5 and S6 inside S7 (standalone statements used as primary); gaps G1 to G10; perimeter notes K1 to K3 |

Carried forward from CP-0: the audited FY2025 statements, annual information form and all debt agreements are not in the pack (G1, G2); debt-issuer identity is not stated (G3, corrected below); the Eagle Ford sale changed the perimeter (G5, K2); adjusted funds flow appears on two perimeters (K1); covenant ratio text prints oddly (K3); nothing after the Q2 2026 documents is supplied (G8).

### Correction to the CP-0 handoff

CP-0 gap G3 said Baytex Energy USA, Inc. "appears only as agent for service". That is wrong for the September 30, 2025 filing: S2 page:8 names it as a borrower under a separate facility ("Baytex's wholly-owned subsidiary, Baytex Energy USA, Inc."). Borrower identity for the credit facilities at September 30, 2025 is therefore stated; for the facilities at 2026 dates and for the 7.375% notes it remains unstated. The earlier handoff cannot be edited; this paragraph supersedes that sentence.

### Citation form

A locator is `alias page:N`, the source chunk number in the pinned `.jsonl`, not a printed page. The evidence register under Findings holds exact quotes. Thousands separators follow the sources.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| After the Eagle Ford sale Baytex has very little debt: an undrawn secured revolver and one small note series, against a large cash balance. Covenant ratios sit far inside their limits on the company's own definitions. | Medium | Debt agreements and audited annual statements are not in the pack, and 2025 comparatives mix reporting bases, so terms and trends rest on company summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt is one note series and an undrawn secured revolver; cash is far larger than the note principal. | Financial leverage is close to nil; credit risk now turns on commodity prices, shareholder payouts and non-debt obligations rather than debt service. | High |
| Covenant tests are far inside their limits on the company's own definitions. | Wide covenant headroom today, but definitions come from company summaries, not the credit agreement itself. | Medium |
| Net cash fell in the first half of 2026 because buybacks and dividends exceeded free cash flow. | Cash-funded shareholder returns are the main way the strong net cash position can erode, and they are discretionary. | High |
| Asset retirement obligations, leases and a contested tax reassessment are large relative to remaining debt, and the first two are outside the covenant debt definition. | These claims on future cash flow are not captured by low debt ratios and need separate monitoring. | Medium |
| The Eagle Ford sale changed the reporting perimeter, so figures before 2026 mix bases. | Trend, leverage and interest-cover comparisons across the sale date are not like for like. | High |

### Financial base view

The financial base is strong but narrow in what it proves. At June 30, 2026 BAYTEX ENERGY CORP. had no drawings on its C$750 million secured revolving credit facilities (maturing June 27, 2030) and one note series, the 7.375% Senior Notes due March 15, 2032, with US$64.1 million (C$91,107 thousand) outstanding, against cash of C$720,337 thousand and company-defined net cash of C$566,286 thousand. Computed liquidity (cash plus undrawn facilities net of letters of credit) was C$1,465,937 thousand. The covenant tests print Total Debt to Bank EBITDA at 0.1 times against a 4.0 times maximum and interest coverage at 9.3 times against a 3.5 times minimum; Bank EBITDA for the twelve months to June 30, 2026 was C$758.9 million. The reading is restricted in four ways. First, all leverage and cover ratios use Bank EBITDA or company-defined net cash, which are company measures pro forma for the sale; the issuer reports no EBITDA, and Bank EBITDA at December 31, 2025 is not in the pack, so the FY2025 ratios are Not supplied. Second, Q2 2026 interest is tiny (net cash interest was income), so cover ratios will keep changing as pre-sale high-interest quarters leave the trailing twelve months. Third, the pre-2026 comparatives mix consolidated, Canada and discontinued bases. Fourth, non-debt claims are material relative to debt: asset retirement obligations of C$546,500 thousand, lease obligations of C$60,256 thousand and a contested tax reassessment, none of which the debt metrics capture. No guarantor, security or covenant text beyond company summaries is verified.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Q3 2025 (September 30, 2025) | 1.1 | Not supplied: Bank EBITDA is printed only as a rounded $1.9 billion | x | Company-printed covenant ratio, Total Debt to Bank EBITDA, trailing twelve months, consolidated including U.S. operations before the sale; Total Debt and Bank EBITDA are both rounded in the source (E50, E51). Not comparable with 2026 rows. |
| FY2025 (December 31, 2025) | Not supplied: Bank EBITDA at December 31, 2025 is in the audited statements, which are not in the pack | Not supplied: same reason | x | Total debt principal was C$97,347 thousand and company-defined net cash C$765,785 thousand at this date (E43, E27), but no EBITDA denominator is supplied. |
| Q1 2026 (March 31, 2026) | 0.14 | -0.89 | x | Calculated C3: Total Debt C$93.9m (covenant definition, includes letters of credit, excludes leases) over Bank EBITDA C$661.0m; net: company-defined net cash C$591.151m (negative sign means net cash) over the same Bank EBITDA. Company-printed ratio is 0.1. |
| Q2 2026 (June 30, 2026) | 0.13 | -0.75 | x | Calculated C3: Total Debt C$95.5m over Bank EBITDA C$758.9m; net cash C$566.286m over the same Bank EBITDA (negative sign means net cash). Company-printed ratio is 0.1. Bank EBITDA is company-defined, trailing twelve months, pro forma for dispositions; net cash is a company capital-management measure that nets working capital. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q3 2025 (September 30, 2025) | 10.5 | x | Company-printed covenant interest coverage (E52b, E52c); Bank EBITDA over financing and interest expense excluding certain non-cash items, trailing twelve months (C$183.0m denominator). Consolidated including U.S. operations before the sale. |
| FY2025 (December 31, 2025) | Not supplied: the covenant table at December 31, 2025 is in the audited statements, which are not in the pack | x | No denominator or numerator supplied for this date. |
| Q1 2026 (March 31, 2026) | 5.54 | x | Calculated C4: Bank EBITDA C$661.0m over financing and interest expense C$119.4m (company-printed 5.5). The denominator is the credit-agreement measure, not a cash-interest figure; it still contains interest from quarters before the Q4 2025 debt repayments. |
| Q2 2026 (June 30, 2026) | 9.31 | x | Calculated C4: Bank EBITDA C$758.9m over financing and interest expense C$81.5m (company-printed 9.3). Credit-agreement measure, not cash interest; the trailing twelve months still contain pre-repayment quarters, while actual Q2 2026 net cash interest was income of C$702 thousand. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Q3 2025 (September 30, 2025) | Not supplied: reported in thousands of Canadian dollars | Not supplied: reported in thousands of Canadian dollars | US$m | Cash C$10,417 thousand (E56). Undrawn capacity not calculable: facilities were US$1.1 billion (C$1.5 billion, rounded) with C$182,345 thousand drawn and C$4.7m letters of credit (E55, E55b); the exact C$ commitment is not supplied. Pre-sale structure including a U.S. subsidiary facility. |
| FY2025 (December 31, 2025) | Not supplied: reported in thousands of Canadian dollars | Not supplied: reported in thousands of Canadian dollars | US$m | Cash C$953,113 thousand (E1); company-stated available credit facility capacity C$744.2 million (E40), consistent with C$750m less C$1.4m drawn and C$4.4m letters of credit. |
| Q1 2026 (March 31, 2026) | Not supplied: reported in thousands of Canadian dollars | Not supplied: reported in thousands of Canadian dollars | US$m | Cash C$757,869 thousand (E46); undrawn C$745,600 thousand calculated C1 (C$750,000 less nil drawn less C$4,400 letters of credit). |
| Q2 2026 (June 30, 2026) | Not supplied: reported in thousands of Canadian dollars | Not supplied: reported in thousands of Canadian dollars | US$m | Cash C$720,337 thousand (E1); undrawn C$745,600 thousand calculated C1. Facilities mature June 27, 2030, so none expires within twelve months of the as-of date; unrestricted status of cash is not stated. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Less than 1 year (to June 30, 2027) | Not supplied: reported in thousands of Canadian dollars | US$m | No debt principal falls due: credit facilities undrawn (E14, E15), notes due 2032 (E16). Contractual cash in the bucket: note interest C$6,719 thousand and lease principal C$15,837 thousand (E57). Notes callable from March 15, 2027 (E58). |
| 1-3 years | Not supplied: reported in thousands of Canadian dollars | US$m | No debt principal falls due. Note interest C$13,438 thousand and lease principal C$23,396 thousand in the bucket (E57). |
| 3-5 years | Not supplied: reported in thousands of Canadian dollars | US$m | No drawn debt principal falls due; the undrawn C$750m revolver commitment matures June 27, 2030 within this bucket (E13). Note interest C$13,438 thousand and lease principal C$18,049 thousand (E57). |
| After 5 years | Not supplied: reported in thousands of Canadian dollars | US$m | 7.375% Senior Notes principal C$91,107 thousand (US$64.1 million) due March 15, 2032 (E16, E57); note interest C$4,786 thousand and lease principal C$39,474 thousand. Redeemable at par from March 15, 2029. |

### Financials and credit metrics

Columns are Q2 2026, Q1 2026 and FY2025; amounts are C$k unless the label says otherwise. "Not supplied" is never zero.

| Metric | Q2 2026 | Q1 2026 | FY2025 | Perimeter, basis and evidence |
| --- | --- | --- | --- | --- |
| Production, boe/d | 71,243 | 69,478 | 65,528 | Continuing (Canada) operations; FY2025 is Canada only (E73, E74, E75) |
| Petroleum and natural gas sales | 639,943 | 452,954 | 1,684,648 | Continuing (Canada); FY2025 consolidated was 3,573,172 (E25, E38, E37) |
| Net income (loss), continuing operations | 168,588 | -79,679 | Not supplied: FY2025 continuing-operations net income is in the audited statements | Continuing (E28, E29) |
| Net income (loss), total | 174,869 | -67,326 | -603,779 | Consolidated; FY2025 includes the Eagle Ford loss and Viking impairment (E35, S6 page:7) |
| Cash flows from operating activities | 230,852 | 122,203 | 1,485,962 | Consolidated total; FY2025 includes Eagle Ford to December 19, 2025 (E19, E33, S7 page:3) |
| Adjusted funds flow, consolidated | 254,433 | 151,125 | 1,514,552 | Company capital-management measure (E18, S7 page:3, E32) |
| Adjusted funds flow, Canada (continuing) | 254,433 | 152,211 | 542,590 | Company measure on continuing basis (E30, E31, S7 page:18) |
| Exploration and development expenditures | 122,242 | 145,012 | 1,206,071 | Q1 and Q2 continuing; FY2025 consolidated, Canada about C$548 million per S3 page:6 (E24, E36) |
| Free cash flow | 128,045 | 1,705 | 274,891 | Company non-GAAP measure; FY2025 consolidated (E23, E34) |
| Net cash interest (income) expense, continuing | -702 | -2,754 | Not supplied: FY2025 consolidated interest is in the audited statements | Net of interest income (S7 page:38, E29b) |
| Interest paid (cash flow statement) | 842 | 4,453 | Not supplied: audited cash flow statement not retained | Consolidated cash flow statement supplementary line (E20, S4 page:3) |
| Cash | 720,337 | 757,869 | 953,113 | Balance sheet; restricted portion not stated (E1, E46) |
| Credit facilities principal | 0 | 0 | 1,400 | Printed as a dash; the discussion states the facilities were undrawn (E14, S7 page:48) |
| 7.375% Senior Notes principal | 91,107 | 89,507 | 95,947 | US$64.1m, US$64.1m and US$70.0m respectively (E15, E47, E16) |
| Long-term notes, carrying value | 89,229 | 87,598 | 93,834 | Net of unamortized issuance costs (E2) |
| Lease obligations, present value | 60,256 | 58,222 | 23,019 | Q1 is current 9,439 plus non-current 48,783 from the balance sheet; includes the Gibson conveyance lease (E3, S4 page:1, E60, E61) |
| Asset retirement obligations | 546,500 | 531,778 | 523,815 | Q1 is current 17,165 plus non-current 514,613; present value, outside debt (E4, S4 page:1) |
| Net cash, company-defined | 566,286 | 591,151 | 765,785 | Printed as negative net debt (E17, E26); nets working capital and excludes leases |
| Bank EBITDA, trailing twelve months, C$m | 758.9 | 661.0 | Not supplied: December 31, 2025 covenant table not in the pack | Credit-agreement measure, pro forma for dispositions (E8, E41) |
| Financing and interest expense for covenant, C$m | 81.5 | 119.4 | Not supplied: same reason | Excludes certain non-cash items (E9, E42) |
| Total Debt, covenant definition, C$m | 95.5 | 93.9 | Not supplied: same reason | Principal plus letters of credit; excludes leases (E10, E43b) |
| Total Debt / Bank EBITDA, printed | 0.1 | 0.1 | Not supplied: same reason | Covenant maximum 4.0 (E7) |
| Interest coverage, printed | 9.3 | 5.5 | Not supplied: same reason | Covenant minimum 3.5 (E6, E45) |
| Senior Secured Debt / Bank EBITDA, printed | 0:0:1.0 | 0:0:1.0 | Not supplied: same reason | Printed form; covenant maximum 3.5; Senior Secured Debt C$4.4m (E5, E11) |
| Total Debt / Bank EBITDA, calculated (x) | 0.13 | 0.14 | Not supplied: no EBITDA | Calculated C3 |
| Net cash / Bank EBITDA, calculated (x) | -0.75 | -0.89 | Not supplied: no EBITDA | Calculated C3; negative means net cash |
| Bank EBITDA / financing and interest expense, calculated (x) | 9.31 | 5.54 | Not supplied: no EBITDA | Calculated C4 |
| Liquidity: cash plus undrawn facilities | 1,465,937 | 1,503,469 | 1,697,313 | Calculated C1; FY2025 uses company-stated C$744.2m capacity (E40) |
| Shares outstanding, thousands | 708,888 | 730,561 | 765,568 | End of period (S7 page:3, S3 page:3) |
| Repurchase of common shares, cash flow | 138,603 | 177,715 | Not supplied: audited cash flow statement not retained | Includes 2% federal levy; FY2025 consideration was C$28.9m per S6 page:11 (E21, S4 page:3) |
| Dividends declared | 16,144 | 16,606 | 69,187 | C$0.0225 per share per quarter (S6 page:11, S3 page:2) |

### Debt register at June 30, 2026

| Instrument | Obligor and guarantors | Amount | Rate and margin | Maturity | Security and terms | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Revolving credit facilities: C$50m operating loan and C$700m syndicated loan | Borrower and guarantors Not supplied for 2026; at September 30, 2025 the borrowers were Baytex and Baytex Energy USA, Inc. under separate facilities (E52) | C$750m committed; drawn nil; letters of credit C$4.4m (Senior Secured Debt C$4.4m) | Prime, CORRA or SOFR plus applicable margins (margins Not supplied); standby fee rate 0.5% (S7 page:38) | June 27, 2030 (was June 27, 2029 at September 30, 2025, E53) | Secured; financial covenants below; debt incurrence and restricted payment covenants | E13, E12, E11 |
| 7.375% Senior Notes | Issuer, co-issuers and guarantors Not supplied | US$64.1m (C$91,107k); issued April 1, 2024 | 7.375% fixed | March 15, 2032 | Redeemable at company option on or after March 15, 2027 at specified prices, at par from March 15, 2029; no significant financial maintenance covenants; security Not supplied | E15, E16, E58, S6 page:10 |
| Lease obligations (IFRS 16) | Not supplied | C$60,256k present value; C$96,756k undiscounted | Interest C$1.4m in Q2 2026 (S6 page:8) | Buckets: less than 1 year C$15,837k to after 5 years C$39,474k | Includes 15-year Gibson infrastructure lease from February 2026 | E3, E57, E60 |
| Retired in Q4 2025 | n/a | 8.50% notes due April 30, 2030 were US$759.4m at September 30, 2025; 7.375% notes were US$575.0m, now US$70.0m at December 31, 2025; credit facilities C$182,345k drawn at September 30, 2025 | n/a | n/a | Repaid or redeemed following the Eagle Ford disposition per management; redemption dates and prices Not supplied (annual notes absent) | E54, E69, S2 page:10, S3 page:3 |

Maturity wall by year (debt principal): 2026 nil, 2027 nil, 2028 nil, 2029 nil, 2030 nil drawn (undrawn C$750m revolver commitment expires June 27, 2030), 2031 nil, 2032 US$64.1m notes. All as printed in the debt notes and the contractual obligations table.

### Claims outside debt

| Claim | Amount and period | Inside or outside the debt figure | Evidence and limit |
| --- | --- | --- | --- |
| Asset retirement obligations | C$546,500k at June 30, 2026, of which C$17,346k current; 3.8% discount, 2.1% inflation | Outside; excluded from covenant Total Debt (E10) and from net cash | E4, S6 page:10. Settlements guided at about C$20m for 2026 (S7 page:25) |
| Lease obligations | C$60,256k present value | Outside covenant Total Debt; outside company net cash; shown separately here | E3, S6 page:8 |
| Processing and transportation agreements | C$4,496k processing and C$66,410k transportation, undiscounted | Outside debt | E57, S7 page:50 |
| Share-based compensation liability | C$29,498k (C$23,406k current plus C$6,092k non-current) | Excluded from covenant Total Debt; included as a deduction in company net cash | S6 page:1, S6 page:18 |
| Canada Revenue Agency reassessment of 2011 to 2015 non-capital losses | CRA statement of account asserts taxes owing by the trusts of C$244.8m, late-payment interest of C$244.2m and a penalty of C$4.1m; C$272.5m insurance purchased for a C$50.3m premium; no payment is required to pursue the appeals | Outside debt; whether any amount is recognised is not stated in the pages read | E59, S6 page:14, S6 page:15 |
| Retained U.S. liabilities | Not supplied: no amount | Outside debt | S7 page:50 |
| Financial derivatives | Net asset C$10,614k at June 30, 2026; Q2 2026 realized loss C$84,146k; no WTI hedges after Q2 2026 | Outside debt | E62, E63 |
| Pensions, retiree medical, factoring and supply-chain finance | Not supplied: a search of all pinned sources for these terms found none | Not assessable | Annual notes (audited statements) are not in the pack |

### Liquidity at each date

| Date | Cash | Facility commitment | Drawn | Letters of credit | Undrawn net of letters of credit | Cash plus undrawn | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| June 30, 2026 | 720,337 | 750,000 | 0 | 4,400 | 745,600 | 1,465,937 | E1, E13, E14, E12; C1 |
| March 31, 2026 | 757,869 | 750,000 | 0 | 4,400 | 745,600 | 1,503,469 | E46, E44, S4 page:8; C1 |
| December 31, 2025 | 953,113 | 750,000 implied | 1,400 | 4,400 | 744,200 stated | 1,697,313 | E1, E40, E14 |

Facilities mature June 27, 2030, outside twelve months of the as-of date. Cash is the balance-sheet line; restricted cash is not mentioned in the pages read.

### Covenants

| Test | Level | Reported figure at June 30, 2026 | Headroom (calculated C5) | Definition differs from metric computed above |
| --- | --- | --- | --- | --- |
| Senior Secured Debt to Bank EBITDA, maximum | 3.5:1.0 | 0:0:1.0 as printed; Senior Secured Debt C$4.4m | Capacity at 3.5 times Bank EBITDA is C$2,656.15m against C$4.4m | Senior secured debt is facility principal plus other secured obligations (here the letters of credit) |
| Interest coverage, minimum | 3.5:1.0 | 9.3:1.0 | Bank EBITDA could fall to C$285.25m before breach, a C$473.65m or about 62% decline, holding the denominator at C$81.5m | Denominator is financing and interest expense excluding certain non-cash items, not cash interest |
| Total Debt to Bank EBITDA, maximum | 4.0:1.0 | 0.1:1.0; Total Debt C$95.5m | Capacity at 4.0 times is C$3,035.6m against C$95.5m | Total Debt includes letters of credit and excludes leases, asset retirement and working-capital liabilities |

No step-downs are stated. Maintenance covenants apply to the Credit Facilities; the notes carry no significant financial maintenance covenants (E72). Company reports compliance with all financial and commercial covenants (S6 page:8). Covenant text beyond these summaries is Not supplied.

### Latest quarter and events after it

| Date | Event | Amount | Evidence |
| --- | --- | --- | --- |
| Q2 2026 | Production above the high end of guidance; full-year guidance raised to about 71,000 boe/d with exploration and development about C$625 million unchanged | 71,243 boe/d | S7 page:2, S7 page:25 |
| Q2 2026 | Share repurchases | 22 million shares for C$136 million (average C$6.27); cash flow C$138,603k including levy | S7 page:7, E21 |
| Q2 2026 | Dividend paid | C$16 million, C$0.0225 per share | S7 page:7 |
| Q2 2026 | No debt issuance, repayment or note repurchase in the quarter; notes repurchased in Q1 2026 | US$5.8m at 103.613% of par in Q1 2026; early redemption expense C$297k | E68, S6 page:3, S6 page:15 |
| Q2 2026 | Realized derivative loss on oil contracts placed before the U.S. sale; no WTI hedges after Q2 2026 | Realized loss C$84,146k | E62, E63 |
| Q2 2026 | Net cash decrease explained by shareholder returns of C$342.9m offset by free cash flow of C$129.8m, year to date | Net cash C$566.286m | E64, E17 |
| June 26, 2026 | Normal course issuer bid renewed for up to 70.9 million shares over 12 months from July 2, 2026 | 70.9 million shares | S6 page:11 |
| July 30, 2026 (subsequent) | Board declared C$0.0225 dividend payable October 1, 2026; 699.2 million shares outstanding at July 30, 2026; buybacks since December 2025 of 69 million shares for C$378 million to July 29, 2026 | See text | E66, S7 page:49, E65 |
| Q2 2026 results release | Two directors appointed, two stepped down | Board of eight, seven independent | S7 page:9 |

No financing amendment, merger or consent decree is described for the quarter. The step-change in the credit facilities between September 30, 2025 (US$1.1 billion across two borrowers, maturity June 27, 2029) and March 31, 2026 (C$750 million, maturity June 27, 2030) is visible in the statements but the amending agreement and its date are not in the pack.

### Evidence register

| ID | Source | Locator | Exact quote |
| --- | --- | --- | --- |
| E1 | S6 | page:1 | Cash 18 $ 720,337 $ 953,113 |
| E2 | S6 | page:1 | Long-term notes 9, 18 89,229 93,834 |
| E3 | S6 | page:8 | Present value of net lease payments 60,256 23,019 |
| E4 | S6 | page:10 | Balance, end of period $ 546,500 $ 523,815 |
| E5 | S6 | page:9 | Senior Secured Debt (1) to Bank EBITDA (2) (Maximum Ratio) 0:0:1.0 3.5:1.0 |
| E6 | S6 | page:9 | Interest Coverage (3) (Minimum Ratio) 9.3:1.0 3.5:1.0 |
| E7 | S6 | page:9 | Total Debt (4) to Bank EBITDA (2) (Maximum Ratio) 0.1:1.0 4.0:1.0 |
| E8 | S6 | page:9 | Bank EBITDA for the twelve months ended June 30, 2026 was $758.9 million |
| E9 | S6 | page:9 | Financing and interest expense for the twelve months ended June 30, 2026 was $81.5 million |
| E10 | S6 | page:9 | Total Debt totaled $95.5 million of principal amounts outstanding |
| E11 | S6 | page:9 | Senior Secured Debt totaled $4.4 million |
| E12 | S6 | page:9 | Baytex had $4.4 million of outstanding letters of credit |
| E13 | S6 | page:8 | Baytex had $750 million of revolving credit facilities |
| E14 | S6 | page:8 | Credit facilities - principal (1) $ — $ 1,400 |
| E15 | S6 | page:9 | 7.375% notes due March 15, 2032 (1) $ 91,107 $ 95,947 |
| E16 | S6 | page:10 | The U.S. dollar denominated principal outstanding of the 7.375% notes was US$64.1 million as at June 30, 2026 (December 31, 2025 - US$70.0 million) |
| E17 | S6 | page:18 | Net Cash $ (566,286) $ (765,785) |
| E18 | S6 | page:18 | Adjusted Funds Flow $ 254,433 $ 366,919 $ 405,558 $ 830,789 |
| E19 | S6 | page:3 | Cash flows from operating activities 230,852 354,312 353,055 785,629 |
| E20 | S6 | page:3 | Interest paid $ 842 $ 53,957 $ 5,295 $ 90,632 |
| E21 | S6 | page:3 | Repurchase of common shares 11 (138,603) (4,137) (316,318) (17,159) |
| E23 | S7 | page:3 | Free cash flow (2) 128,045 1,705 3,188 129,750 55,717 |
| E24 | S7 | page:3 | Exploration and development expenditures $ 122,242 $ 145,012 $ 356,532 $ 267,254 $ 761,629 |
| E25 | S7 | page:3 | Petroleum and natural gas sales - Canada $ 639,943 $ 452,954 $ 411,036 $ 1,092,897 $ 865,187 |
| E26 | S7 | page:3 | Net (cash) debt (1) $ (566,286) $ (591,151) $ 2,293,940 $ (566,286) $ 2,293,940 |
| E27 | S3 | page:3 | Net (cash) debt (1) $ (765,785) $ 2,244,358 $ 2,417,172 $ (765,785) $ 2,417,172 |
| E28 | S6 | page:2 | Net income from continuing operations $ 168,588 $ 103,018 $ 88,909 $ 85,663 |
| E29 | S4 | page:1 | Net loss from continuing operations $ (79,679) $ (17,355) |
| E29b | S4 | page:15 | Net cash interest (income) expense $ (2,754) $ 43,591 |
| E30 | S5 | page:3 | Adjusted funds flow - Canada (4) $ 152,211 $ 116,214 $ 162,012 |
| E31 | S3 | page:4 | Adjusted funds flow - Canada (4) $ 116,214 $ 151,846 $ 148,062 $ 542,590 $ 656,554 |
| E32 | S3 | page:2 | Adjusted funds flow (1) 261,531 422,232 461,886 1,514,552 1,956,518 |
| E33 | S3 | page:2 | Cash flows from operating activities 227,657 472,676 468,865 1,485,962 1,908,264 |
| E34 | S3 | page:2 | Free cash flow (2) 76,486 142,688 254,838 274,891 655,582 |
| E35 | S3 | page:2 | Net (loss) income (856,887) 31,968 (38,477) (603,779) 236,597 |
| E36 | S3 | page:2 | Exploration and development expenditures $ 174,078 $ 270,364 $ 198,177 $ 1,206,071 $ 1,256,633 |
| E37 | S3 | page:2 | Petroleum and natural gas sales $ 759,815 $ 927,648 $ 1,017,017 $ 3,573,172 $ 4,208,955 |
| E38 | S3 | page:12 | Petroleum and natural gas sales $ 381,556 $ 437,905 $ 466,706 $ 1,684,648 $ 1,874,046 |
| E40 | S3 | page:13 | the Company had $744.2 million of available credit facility capacity |
| E41 | S4 | page:9 | Bank EBITDA for the twelve months ended March 31, 2026 was $661.0 million |
| E42 | S4 | page:9 | Financing and interest expense for the twelve months ended March 31, 2026 was $119.4 million |
| E43 | S3 | page:3 | Total debt (3) 97,347 2,037,950 2,321,826 97,347 2,321,826 |
| E43b | S4 | page:9 | the Company's Total Debt totaled $93.9 million of principal amounts outstanding |
| E44 | S4 | page:8 | At March 31, 2026, Baytex had $750 million of revolving credit facilities |
| E45 | S4 | page:8 | Interest Coverage (3) (Minimum Ratio) 5.5:1.0 3.5:1.0 |
| E46 | S4 | page:1 | Cash 18 $ 757,869 $ 953,113 |
| E47 | S4 | page:9 | 7.375% notes due March 15, 2032 (1) $ 89,507 $ 95,947 |
| E50 | S2 | page:9 | Total Debt (4) to Bank EBITDA (2) (Maximum Ratio) 1.1:1.0 4:0:1.0 |
| E51 | S2 | page:9 | Bank EBITDA for the twelve months ended September 30, 2025 was $1.9 billion |
| E52 | S2 | page:8 | a US$45 million operating loan and a US$255 million syndicated revolving loan for Baytex's wholly-owned subsidiary, Baytex Energy USA, Inc. |
| E52b | S2 | page:9 | Interest Coverage (3) (Minimum Ratio) 10.5:1.0 3.5:1.0 |
| E52c | S2 | page:9 | Financing and interest expense for the twelve months ended September 30, 2025 was $183.0 million |
| E53 | S2 | page:8 | On June 27, 2025, Baytex extended the maturity of the revolving credit facilities (the "Credit Facilities") from May 9, 2028 to June 27, 2029. |
| E55 | S2 | page:8 | Baytex had US$1.1 billion ($1.5 billion) of revolving credit facilities that mature on June 27, 2029 |
| E55b | S2 | page:9 | Baytex had $4.7 million of outstanding letters of credit |
| E54 | S2 | page:9 | 8.50% notes due April 30, 2030 (1) $ 1,056,039 $ 1,152,360 |
| E56 | S2 | page:1 | Cash 17 $ 10,417 $ 16,610 |
| E57 | S7 | page:50 | Total $ 297,150 $ 59,278 $ 61,758 $ 35,332 $ 140,782 |
| E57a | S7 | page:50 | Interest on long-term notes 38,381 6,719 13,438 13,438 4,786 |
| E57b | S7 | page:50 | Lease obligations - principal 96,756 15,837 23,396 18,049 39,474 |
| E57c | S7 | page:50 | Transportation agreements 66,410 36,092 24,381 3,320 2,617 |
| E58 | S7 | page:49 | are redeemable at our option, in whole or in part, at specified redemption prices on or after March 15, 2027 and will be redeemable at par from March 15, 2029 to maturity |
| E59 | S6 | page:14 | The most recent statement of account issued by the CRA assert taxes owing by the trusts of $244.8 million, late payment interest of $244.2 million and a late filing penalty in respect of the 2011 tax year of $4.1 million |
| E59a | S6 | page:14 | we purchased $272.5 million of insurance coverage for a premium of $50.3 million |
| E60 | S6 | page:6 | the agreement was determined to contain a lease under IFRS 16 |
| E61 | S6 | page:8 | Additions — 39,745 478 40,223 |
| E62 | S6 | page:17 | Realized financial derivatives loss $ 84,146 $ 11,874 $ 113,435 $ 12,068 |
| E63 | S7 | page:6 | we have no WTI hedges in place after Q2/2026 |
| E64 | S7 | page:47 | shareholder returns of $342.9 million during YTD 2026 |
| E64a | S7 | page:47 | partially offset by $129.8 million of free cash flow |
| E65 | S7 | page:7 | we repurchased 69 million common shares for $378 million |
| E66 | S6 | page:11 | On July 30, 2026, the Company's Board of Directors declared a quarterly cash dividend of $0.0225 per share to be paid on October 1, 2026 |
| E68 | S6 | page:10 | Baytex repurchased and cancelled US$5.8 million principal amount of the 7.375% Senior Notes at 103.613% of par value |
| E69 | S7 | page:38 | redeemed the 8.5% Senior Notes and partially redeemed the 7.375% Senior Notes |
| E72 | S6 | page:10 | The long-term notes do not contain any significant financial maintenance covenants |
| E73 | S7 | page:25 | Daily production (boe/d) - continuing operations 71,243 64,167 11 % 70,366 63,279 11 % |
| E74 | S7 | page:54 | 69,478 boe/d in Q1/2026 |
| E75 | S3 | page:3 | Total Canada (boe/d) (1) 67,295 68,185 65,332 65,528 63,948 |

## Calculations

All inputs are quoted in the evidence register (C$k unless stated). Python-checked.

- **C1 Liquidity (cash plus undrawn facilities net of letters of credit).** June 30, 2026: undrawn = 750,000 - 0 - 4,400 = 745,600; liquidity = 720,337 + 745,600 = 1,465,937. March 31, 2026: undrawn = 750,000 - 0 - 4,400 = 745,600; liquidity = 757,869 + 745,600 = 1,503,469. December 31, 2025: 953,113 + 744,200 (company-stated capacity) = 1,697,313; cross-check 750,000 - 1,400 - 4,400 = 744,200. Inputs E1, E13, E44, E14, E12, E46, E40.
- **C2 Covenant Total Debt tie-out.** Notes principal 91,107 + letters of credit 4,400 = 95,507, which rounds to the printed C$95.5m (E15, E12, E10).
- **C3 Leverage ratios (x).** Total Debt / Bank EBITDA: Q2 2026 95.5 / 758.9 = 0.1258, shown 0.13; Q1 2026 93.9 / 661.0 = 0.1421, shown 0.14. Net cash / Bank EBITDA: Q2 2026 -566.286 / 758.9 = -0.7462, shown -0.75; Q1 2026 -591.151 / 661.0 = -0.8943, shown -0.89. Negative = net cash. Inputs E10, E43b, E8, E41, E17, E26.
- **C4 Interest cover (x).** Q2 2026 758.9 / 81.5 = 9.3117, shown 9.31; Q1 2026 661.0 / 119.4 = 5.5360, shown 5.54. Q3 2025 is taken as printed (10.5) because Bank EBITDA is rounded ($1.9 billion / $183.0m = 10.38 would be false precision). Inputs E8, E9, E41, E42, E51, E52b.
- **C5 Covenant headroom (June 30, 2026).** Interest coverage floor: 3.5 x 81.5 = 285.25 (C$m); headroom 758.9 - 285.25 = 473.65 (C$m), 473.65 / 758.9 = 62.4%. Total Debt cap: 4.0 x 758.9 = 3,035.6 (C$m) versus 95.5. Senior secured cap: 3.5 x 758.9 = 2,656.15 (C$m) versus 4.4. The interest-coverage figure holds the denominator fixed and is an arithmetic headroom, not a forecast.
- **C6 Contractual obligations tie-out.** 91,107 + 38,381 + 96,756 + 4,496 + 66,410 = 297,150 (E57). Less-than-one-year bucket 0 + 6,719 + 15,837 + 630 + 36,092 = 59,278.
- **C7 Net cash change.** 765,785 - 566,286 = 199,499 decline in company-defined net cash from December 31, 2025 to June 30, 2026. The company's own explanation is shareholder returns of 342.9 offset by free cash flow of 129.8 (C$m, E64, E64a); the two are not reconciled here because net cash includes working-capital movements.
- **C8 Quarter-end carrying lines.** Q1 2026 lease obligations 9,439 + 48,783 = 58,222; asset retirement obligations 17,165 + 514,613 = 531,778 (S4 page:1). Q1 2026 net loss from continuing operations check: -67,326 - 12,353 = -79,679 (S4 pages 1 and 2), which agrees with the printed -79,679.
- **C9 Reference: trailing twelve-month adjusted funds flow, continuing basis (cross-check only, not a leverage input).** Q3 2025 151,846 + Q4 2025 116,214 + Q1 2026 152,211 + Q2 2026 254,433 = 674,704 (E31, E30, E18). Notes principal 91,107 / 674,704 = 0.135 times. Adjusted funds flow is after cash interest and realized hedging, so it is not EBITDA; the Q3 and Q4 2025 inputs are the March 2026 "Canada" presentation. Implied reduction in the 7.375% notes from US$575.0m at September 30, 2025 to US$70.0m at December 31, 2025 is 505.0 (US$m), from S2 page:10 and S6 page:10; redemption dates and prices are Not supplied.

## Gaps

| ID | Severity | Gap | Affected | Action |
| --- | --- | --- | --- | --- |
| H1 | High | EBITDA is not reported by the issuer; the only EBITDA is Bank EBITDA, a credit-agreement measure pro forma for the sale, given as a single total per date. Its build-up and the December 31, 2025 value are Not supplied. | Leverage and cover rows, covenants | Obtain the credit agreement definitions and the annual covenant note (CP-0 G1, G2, G7) |
| H2 | High | No credit agreement or indenture: guarantors, security, margins, baskets and call prices beyond the summary are Not supplied. Borrower and obligor identity for 2026 debt is unstated. | Debt register, covenants | Add the debt documents |
| H3 | Medium | The audited FY2025 statements and notes are not in the pack: FY2025 continuing-operations net income, annual interest paid, year-end Bank EBITDA, the pension, factoring and supply-chain search, and any provision for the CRA matter are Not supplied. | FY2025 column, claims outside debt | Add the annual report exhibits |
| H4 | Medium | Perimeter: FY2025, Q3 2025 and Q4 2025 columns are consolidated or split between Canada and discontinued operations on different tables; they are not like for like with 2026 columns. | All trend and ratio use | Label basis; prefer revised comparatives in S6 and S7 |
| H5 | Medium | Credit facility amendment between September 30, 2025 and March 31, 2026 (size, borrowers and maturity changed) is not documented; the interim facility size at December 31, 2025 is implied, not printed. | Liquidity at FY2025, debt register | Add the amending agreement |
| H6 | Medium | Adjusted funds flow is printed on two perimeters (CP-0 K1): C$405,558 thousand year to date on the consolidated reconciliation, and the discussion's C$406.6 million for continuing operations. | Cash flow rows | Cite the perimeter on every use; both are shown here as printed |
| H7 | Low | Covenant ratio text prints oddly (0:0:1.0, 4:0:1.0) per CP-0 K3; treated as print oddity. | Covenant rows | Quote as printed |
| H8 | Medium | Recency: nothing after the Q2 2026 documents (latest event dated July 30, 2026) is supplied; the as-of date is November 5, 2026. | All | Check for later filings before the cutoff |
| H9 | Low | Restricted cash and the unrestricted portion of cash are not stated; liquidity treats the balance-sheet cash line as available. | Liquidity | Check the annual cash note |

## Next module

Proceed to CP-1A (business and transaction context). Carry forward: the retained Canadian business and the Eagle Ford sale of December 19, 2025 as the structural transaction (net proceeds US$2.2 billion, C$3.0 billion, S3 page:5); the Q4 2025 repayment of debt; the shareholder return programme (buybacks and dividends) that moved net cash from C$765,785 thousand to C$566,286 thousand; the CRA reassessment; the Gibson lease; the retained U.S. liabilities. The debt side is thin and the downstream questions are about commodity exposure, capital returns and non-debt obligations. Hand off to CP-2 the liquidity, covenant and perimeter limitations H1 to H9. Next evidence action: the annual report exhibits and the debt documents.
