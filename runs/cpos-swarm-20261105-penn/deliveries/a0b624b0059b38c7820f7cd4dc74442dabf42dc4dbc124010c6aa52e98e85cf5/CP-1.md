## Request

Issuer: PENN Entertainment, Inc. (Nasdaq: PENN), consolidated. As-of date and cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency USD, in millions unless stated. Current period q3-2026 (three and nine months ended 2026-09-30); prior period fy-2025 (year ended 2025-12-31). Task: extract and organise the financial base for a creditor view: reported statements, debt by instrument, liquidity, maturities, leases and other claims outside debt, covenants, the latest quarter and events to the cutoff. Every derived figure is shown in `## Calculations`. Period labels used throughout: Q3 2026 (three months), 9M 2026 (nine months), LTM Q3 2026 (twelve months to 2026-09-30), FY2025, and the same for prior-year comparatives.

Perimeter: PENN Entertainment, Inc. and subsidiaries, as consolidated in the filings. The filings contain no separate issuer-level or subsidiary statements. The perimeter is the same for every figure below.

## Sources

### Issuer sources relied on

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_penn-20251231.htm.jsonl | e6f090720b62a51573341a18254da71e5663d9a3ca11809ee32b87032414e4c4 |
| 10-Q_2026-03-31_penn-20260331.htm.jsonl | f74720e254c5d598fec44396bf0d01f4b1fcb35191eafe54dbae1433241cfe17 |
| 10-Q_2026-06-30_penn-20260630.htm.jsonl | e4a4a68372f7e9e6e78807b6eaf280e8a90a9eb8c02165e49ee603cc73e74ba7 |
| 10-Q_2026-09-30_penn-20260930.htm.jsonl | 289bd66b2b3ba7c0442b90807e0166affa057570b7680ca91b89ac74aa566568 |
| EX-99.1_2026-04-23_pennex991-q12026.htm.jsonl | bd58a1d530bb3cf8b4081bd3c78bc172ec144332ab675d2b2c776af0b2ffd599 |
| EX-99.1_2026-08-06_pennex991-q22026.htm.jsonl | 29f1d9698d7fe07b2e827f80ed415692eef3a01380a671b91317aa4e3711e167 |
| EX-99.1_2026-11-05_pennex991-q32026.htm.jsonl | 9cd3b27bc143946725e283ad70f7a65c0842d014c7b12f2cd6670b5aee829c8c |

Authority: the filings (10-K audited, 10-Qs unaudited) control reported facts. The releases are management documents and are used for the non-GAAP Consolidated Adjusted EBITDA, the lease-adjusted measures and discrete-quarter items, always labelled as management measures. The context file (sha256 de76f6d737b4f874d55cfe4efb68426523509ccefb05817de5c048370ec1b054) is run settings, not evidence.

Locators are written `source page:N`, where N is the chunk number in the supplied extraction, not the printed page. "10-Q Q3" means the 10-Q for the quarter ended 2026-09-30; "release Q3" means the exhibit dated 2026-11-05.

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 8e6b52c72fe186ee073cb0e5f0c242ec3f53d4e3a091c87a50ef71a77d1acea5 |

How CP-0 is used and one correction. CP-0 rated the pack READY_WITH_LIMITATIONS and carried: no executed credit agreement, indentures or leases; no reported covenant ratio values; management measures differ from covenant and GAAP measures; the debt table changed version in 2026; and cash paid for interest has two definitions. This handoff keeps all of them. One correction: CP-0 wrote that lease cash rent comes from release or MD&A text only. It is also in the filed 10-Q Q3 Note 6, "Total payments made under our Triple Net Leases" (10-Q Q3 page:27: 251.8 for Q3 2026 and 746.6 for 9M 2026), so the filing supports it.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Financial leverage on the company's debt definition fell to 2.58x gross and 1.62x net at LTM Q3 2026, with liquidity of 2020.9, but lease and financing obligations of 8157.6 sit outside that debt. | Medium | Covenant ratios and definitions are not supplied, so covenant headroom cannot be measured. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt principal of 2806.6 is mostly term loans due 2031 to 2033 and notes; 400.0 of notes mature in January 2027, within twelve months. | Near-term maturity is covered by cash of 1044.8 and an undrawn revolver. | High |
| LTM Consolidated Adjusted EBITDA rose to 1088.2 from 830.1 at FY2025, mainly from a smaller Interactive loss and higher Retail earnings. | Stronger earnings drive the lower leverage; Interactive still loses money. | Medium |
| Financing obligations of 2309.8 and finance lease liabilities of 2049.6 are outside debt and outside the EBITDA deduction; adding them lifts net leverage to 5.63x. | Debt-like landlord claims are the larger part of fixed obligations. | Medium |
| Cash paid for interest was 382.4 over the last twelve months, giving 2.85x cover from LTM Consolidated Adjusted EBITDA. | Cover has improved but remains modest against fixed lease and interest costs. | Medium |

### Financial base view

PENN's reported base improved through 2026 on every measure the sources support. The company's own debt measure, traditional debt of principal outstanding, fell from 2904.1 at FY2025 to 2806.6 at 2026-09-30 while cash rose from 686.6 to 1044.8. Over the same period LTM Consolidated Adjusted EBITDA, the company's non-GAAP measure struck after triple net operating lease rent, rose from 830.1 to 1088.2, so the debt ratios on that basis fell to 2.58x gross and 1.62x net from 3.50x and 2.67x. Liquidity at 2026-09-30 is 2020.9 and no committed facility expiring within twelve months was located (the revolver matures in April 2031). Cash interest cover on LTM Consolidated Adjusted EBITDA is 2.85x. The refinancing in 2026 pushed bank maturities to 2031 and 2033, replaced the 2027 revolver and term loan maturities, and added 600.0 of 6.75% notes due 2031. The base view is limited in three ways. First, 8157.6 of lease and financing obligations to landlords sit outside the debt figure, and 4359.4 of that (financing obligations of 2309.8 and finance lease liabilities of 2049.6) is also outside the rent deduction in EBITDA, so debt ratios on the company's definition understate fixed-charge leverage; on a perimeter that adds those two items, net leverage is 5.63x. Second, the covenant tests (total net leverage 4.50x maximum and interest coverage 2.00x minimum) are described but their reported values and definitions are not supplied, so headroom is Not calculable. Third, the improvement in EBITDA depends on the Interactive segment, whose loss narrowed to 18.3 in Q3 2026 but which remains negative, and the Q3 2025 comparison is flattered by the absence of ESPN-related advertising of 52.0 (37.5 under the Sportsbook Agreement and 14.5 under the Investment Agreement, 10-Q Q3 page:41) that was in Q3 2025 media and advertising expense; the 825.0 Q3 2025 impairment distorts net income but not Consolidated Adjusted EBITDA, which adds impairment back.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 3.50 | 2.67 | x | Debt principal 2904.1 less cash 686.6 over Consolidated Adjusted EBITDA 830.1. Company non-GAAP, after triple net operating lease rent. Excludes financing obligations, finance leases and operating lease liabilities. Not the covenant ratio. |
| LTM Q1 2026 | 3.20 | 2.43 | x | Debt principal 2948.9 less cash 708.0 over LTM Consolidated Adjusted EBITDA 922.6. Same basis and exclusions as FY2025. |
| LTM Q2 2026 | 2.82 | 1.93 | x | Debt principal 2814.7 less cash 887.2 over LTM Consolidated Adjusted EBITDA 999.1. Same basis and exclusions. |
| LTM Q3 2026 | 2.58 | 1.62 | x | Debt principal 2806.6 less cash 1044.8 over LTM Consolidated Adjusted EBITDA 1088.2. Same basis and exclusions. On a perimeter adding financing obligations and finance leases, 6.59x gross and 5.63x net (see Calculations). |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 2.17 | x | Consolidated Adjusted EBITDA 830.1 over cash paid for interest, net of amounts capitalized, 383.0 (10-K cash-flow supplement). The cash figure includes interest on finance leases and financing obligations. |
| LTM Q1 2026 | 2.37 | x | LTM EBITDA 922.6 over LTM cash interest 388.8, calculated as FY2025 383.0 less Q1 2025 102.0 plus Q1 2026 107.8. |
| LTM Q2 2026 | 2.61 | x | LTM EBITDA 999.1 over LTM cash interest 382.9, calculated as 383.0 less 188.0 plus 187.9 (six-month figures). |
| LTM Q3 2026 | 2.85 | x | LTM EBITDA 1088.2 over LTM cash interest 382.4, calculated as 383.0 less 292.2 plus 291.6 (nine-month figures). Not the covenant coverage ratio, whose definition is not supplied. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (2025-12-31) | 686.6 | 406.1 | US$m | Unrestricted cash and equivalents. Revolver 1000.0 less 570.0 drawn less 23.9 letters of credit (10-K page:89). Excludes restricted cash of 28.2. |
| Q1 2026 (2026-03-31) | 708.0 | 951.1 | US$m | Cash from release Q1 page:6. Revolver 1000.0 less 25.0 drawn less 23.9 letters of credit (10-Q Q1 page:16). |
| Q2 2026 (2026-06-30) | 887.2 | 976.1 | US$m | Cash from release Q2 page:8. Revolver, 2031 maturity, undrawn, 23.9 letters of credit (10-Q Q2 page:19). |
| Q3 2026 (2026-09-30) | 1044.8 | 976.1 | US$m | Cash from 10-Q Q3 page:2. Revolver 1000.0 undrawn less 23.9 letters of credit (10-Q Q3 page:18). Excludes restricted cash of 29.3. Revolver matures April 2031. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q4 2026 (remainder of 2026) | 8.1 | US$m | Minimum principal repayments at 2026-09-30 (10-Q Q3 page:16). |
| 2027 | 433.1 | US$m | Includes 400.0 of 5.625% Notes due 2027 (January 15, 2027); remainder 33.1 is scheduled term loan and other repayment. Notes are classified long-term on intent and ability to refinance. |
| 2028 | 33.1 | US$m | Scheduled term loan and other repayments. |
| 2029 | 433.2 | US$m | Includes 400.0 of 4.125% Notes due 2029; remainder 33.2 scheduled repayment. |
| 2030 | 33.2 | US$m | Scheduled term loan and other repayments. |
| Thereafter | 1865.9 | US$m | Includes 600.0 of 6.75% Notes due 2031, Term Loan A due April 2031 balance and Term Loan B due May 2033 balance. Total of all rows is 2806.6. Excludes lease and financing obligations. |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2025 | 9M 2025 | 9M 2026 | Q3 2025 | Q3 2026 | LTM Q3 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenues | 6,961.0 | 5,154.8 | 5,476.4 | 1,717.3 | 1,840.0 | 7,282.6 | Statements of operations (10-K page:106; 10-Q Q3 page:3). LTM calculated. |
| Operating income (loss) | (673.6) | (656.1) | 355.9 | (776.4) | 127.3 | 338.4 | Same. LTM calculated. |
| Impairment losses | 945.3 | 840.0 | 8.0 | 825.0 | 8.0 | 113.3 | Same. FY2025 includes 825.0 Interactive goodwill charge recorded in Q3 2025. LTM calculated. |
| Net income (loss) | (845.3) | (771.9) | 62.4 | (865.1) | 32.6 | (11.0) | 10-K page:107; 10-Q Q3 page:3. LTM calculated. |
| Consolidated Adjusted EBITDA (company, after triple net operating lease rent) | 830.1 | 604.3 | 862.4 | 194.9 | 284.0 | 1,088.2 | Management non-GAAP (10-K page:74; release Q3 pages 3-6, 7). LTM as printed. |
| Rent expense, triple net operating leases | 631.7 | 470.0 | 494.4 | 158.1 | 167.9 | 656.2 | Release Q3 pages 3-4, 7; 10-Q Q3 page:27. LTM as printed. |
| Retail Segment Adjusted EBITDAR (four retail segments) | 1,868.8 | 1,412.4 | 1,490.4 | 465.8 | 501.8 | 1,946.8 | Sum of Northeast, South, West, Midwest (10-K page:74; release Q3 pages 3-4). Before rent. LTM calculated. |
| Interactive Segment Adjusted EBITDA | (267.5) | (227.6) | (38.7) | (76.6) | (18.3) | (78.6) | Same sources. LTM calculated. |
| Net cash provided by operating activities | 508.2 | 401.0 | 626.4 | 180.9 | 263.3 | 733.6 | 10-K page:108; 10-Q Q3 page:6. Q3 values derived as nine months less six months (10-Q Q2 page:5). LTM calculated. |
| Capital expenditures | 647.7 | 457.3 | 251.2 | 172.7 | 59.2 | 441.6 | 10-K page:108; 10-Q Q3 page:6; release Q3 page:8. LTM calculated. |
| Proceeds from sale-and-leaseback in development projects | 280.0 | 130.0 | 216.3 | Not extracted | Not extracted | 366.3 | 10-K page:109; 10-Q Q3 page:6. LTM calculated. |
| Cash paid for interest, net of amounts capitalized | 383.0 | 292.2 | 291.6 | 104.2 | 103.7 | 382.4 | 10-K page:109; 10-Q Q3 page:6. Q3 derived as nine months less six months (10-Q Q2 page:6). LTM calculated. |
| Interest expense, net | 405.8 | 303.9 | 307.7 | 97.2 | 105.8 | 409.6 | Statements of operations. LTM calculated. |
| Cash and cash equivalents (period end) | 686.6 | 660.1 | 1,044.8 | Not applicable | Not applicable | 1,044.8 | Point in time: 2025-12-31, 2025-09-30, 2026-09-30 (10-Q Q3 pages 2 and 6). |
| Total debt principal (period end) | 2,904.1 | Not extracted | 2,806.6 | Not applicable | Not applicable | 2,806.6 | Point in time (10-K page:137; 10-Q Q3 page:15). |
| Financing obligations plus finance lease liabilities (period end) | 4,406.7 | Not extracted | 4,359.4 | Not applicable | Not applicable | 4,359.4 | Current plus long-term, balance sheet (10-K page:106; 10-Q Q3 page:2). Calculated. |
| Operating lease liabilities (period end) | 3,978.4 | Not extracted | 3,798.2 | Not applicable | Not applicable | 3,798.2 | Current plus long-term. Calculated. |
| Total debt / LTM Consolidated Adjusted EBITDA (x) | 3.50 | Not applicable | Not applicable | Not applicable | Not applicable | 2.58 | Calculated; management basis. |
| Net debt / LTM Consolidated Adjusted EBITDA (x) | 2.67 | Not applicable | Not applicable | Not applicable | Not applicable | 1.62 | Calculated; management basis. |
| LTM Consolidated Adjusted EBITDA / cash interest (x) | 2.17 | Not applicable | Not applicable | Not applicable | Not applicable | 2.85 | Calculated. |

### Debt by instrument at 2026-09-30

Principal outstanding, 10-Q Q3 page:15 (Note 5). The issuer of every instrument is PENN Entertainment, Inc.

| Instrument | Principal 2026-09-30 | Principal 2025-12-31 | Rate and maturity | Security and guarantors as printed |
| --- | --- | --- | --- | --- |
| Amended Revolving Credit Facility due 2031 | 0.0 drawn (commitment 1000.0, 23.9 letters of credit) | Revolver due 2027: 570.0 drawn | Term SOFR plus 1.50% to 2.25% (base rate 0.50% to 1.25%), unused fee 0.20% to 0.35%; April 2031 (10-Q Q3 page:17) | Interests in owned real property, other than named exceptions, collateralize the Amended Credit Facilities (10-K page:64); guarantor identity not located in the supplied text |
| Amended Term Loan A Facility due 2031 | 441.3 | 453.8 (due 2027) | Same margins as revolver; April 2031 | Same |
| Amended Term Loan B Facility due 2033 | 957.5 | 965.0 (due 2029) | Term SOFR plus 2.00% (base rate 1.00%), SOFR floor 0.50%; May 2033 (10-Q Q3 page:18) | Same |
| 5.625% Notes due 2027 | 400.0 | 400.0 | Fixed, January 15, 2027; callable at declining premiums | Senior unsecured; not guaranteed by subsidiaries unless certain guaranteed debt is later issued (10-Q Q3 page:18) |
| 4.125% Notes due 2029 | 400.0 | 400.0 | Fixed, 2029; fair value 375.0 (10-Q Q3 page:78) | Principal and rate from Note 5; ranking and guarantor wording for these notes not located on the pages read beyond the covenant paragraph (10-Q Q3 page:20) |
| 6.75% Notes due 2031 | 600.0 | not outstanding | Fixed, April 1, 2031, issued at par on March 16, 2026; callable from April 1, 2028; fair value 574.5 | Senior unsecured; not guaranteed by subsidiaries unless certain guaranteed debt is later issued (10-Q Q3 page:18) |
| 2.75% Convertible Notes due 2026 | 0.0 (repaid May 2026, 106.7) | 106.7 | Fixed | Unsecured |
| Other long-term obligations | 7.8 | 8.6 | Not stated | Not stated |
| Total traditional debt | 2,806.6 | 2,904.1 | | Balance sheet debt is 2,768.3 (current maturities 33.1 plus long-term 2,735.2) after discounts and issuance costs of 38.3 |

The 4.125% Notes are described in Note 5 only through the covenant paragraph and the principal table; no co-issuer is printed for any note. Interest rate exposure: the term loans are floating, with weighted-average rates of 6.746% in the first year and 6.941% thereafter (10-Q Q3 page:78).

### Claims outside debt

| Claim | Amount | Inside the debt figure? | Locator |
| --- | --- | --- | --- |
| Financing obligations (Pinnacle Master Lease buildings and Morgantown Lease) | 2,309.8 present value (47.5 current, 2,262.3 long term); undiscounted payments 4,204.8 | No | 10-Q Q3 pages 2 and 27 |
| Finance lease liabilities (Pinnacle Master Lease land) | 2,049.6 (55.6 current, 1,994.0 long term); undiscounted 3,628.0 | No | 10-Q Q3 pages 2 and 27 |
| Operating lease liabilities (AR PENN, 2023 and VICI Master Leases and other) | 3,798.2; undiscounted 5,145.3 | No; the rent is deducted inside Consolidated Adjusted EBITDA | 10-Q Q3 page:27 |
| Cash paid to REIT landlords under the Triple Net Leases | 746.6 for 9M 2026 and 721.9 for 9M 2025; 967.8 for FY2025 | Not debt; includes payments on operating leases, finance leases and financing obligations | 10-Q Q3 page:27; 10-K page:31 |
| Purchase obligations | 473.4 at 2025-12-31 (268.5 due in 2026); not updated in the 10-Q Q3 on search | Outside | 10-K pages 92 and 158 |
| Barstool indemnification liability | 38.7 recorded at 2026-09-30; maximum not estimable | Outside | 10-Q Q3 pages 30-31 |
| Insurance financing | 26.2 paid and 7.2 received in 9M 2026 (financing cash flows) | Balance not located; treated as outside debt | 10-Q Q3 page:6 |
| Pensions and retiree medical | Not supplied: no such obligation located on search of "pension", "postretirement" and "retiree" in the 10-K and 10-Q Q3; a 401(k) plan is described (10-K page:158) | Not applicable | |
| Factoring and supply chain finance | Not supplied: none located on search of the 10-K and 10-Q Q3 | Not applicable | |
| Litigation or consent decree funding | None quantified: "does not believe that the final outcome of these matters will have a material adverse effect" (10-Q Q3 page:30); Indiana tax matter resolved in the Company's favour (page:30) | Not applicable | |
| Development funding commitments | Council Bluffs project 180.0 to 200.0, GLPI committed to finance up to 150.0 at a 7.1% cap rate, as rent or a 5-year term loan; New Orleans project about 195.0, to be financed from cash on hand | Outside | 10-Q Q3 page:48 |
| Capital expenditure for 2026 | Anticipated maintenance 220.0 and project 170.0, of which 111.5 and 139.7 incurred in 9M 2026 | Outside | 10-Q Q3 page:69 |

### Latest quarter, financing events and after the quarter

2026 financing events in order. On March 16, 2026 PENN issued 600.0 of 6.75% senior unsecured notes at par, due April 1, 2031, and used the net proceeds to repay revolver borrowings (10-Q Q3 page:18). On April 16, 2026 the Third Amendment refinanced and extended the 1.0 billion revolver and the 446.9 Term Loan A to April 2031 and removed the credit spread adjustment (page:17). On May 28, 2026 the Fourth Amendment extended the 962.5 Term Loan B to May 2033 and cut margins by 50 basis points to 2.00% (page:18). The 106.7 convertible notes were repaid in May 2026 (page:19). In connection with the two amendments the Company recorded 16.3 of issuance costs and a 2.4 original issue discount (page:18). The loss on early extinguishment of debt was 1.8 for 9M 2026 and nil in Q3 2026 (10-Q Q3 page:3). On June 24, 2026 the Aurora facility opened, GLPI funded 216.3 and annual rent rose by 17.4 (10-Q Q3 pages 23 and 70). Quarter ended 2026-09-30: Q3 events are the Boomtown New Orleans relocation announced August 17, 2026 and the Council Bluffs groundbreaking on September 14, 2026 (page:48).

Events after 2026-09-30 and up to the cutoff, labelled subsequent: on October 15, 2026 the Company gave notice that it will redeem all outstanding exchangeable shares for common stock on or about December 15, 2026 (98,920 shares outstanding at 2026-09-30; 10-Q Q3 page:31); effective November 1, 2026 the fixed rent under the AR PENN Master Lease rose by 4.4 (page:21); the shares outstanding at October 29, 2026 were 134,253,794 (page:1). No debt event after 2026-09-30 was located. No dedicated subsequent-events note was found.

Q3 2026 against Q3 2025, from the statements and segment note. Revenue 1840.0 against 1717.3, an increase of 7.1%. Consolidated Adjusted EBITDA 284.0 against 194.9, an increase of 89.1. By component of that increase: Interactive improved by 58.3 (a loss of 18.3 against 76.6), the four retail segments by 36.0 (501.8 against 465.8), the Other category by 4.6, and triple net operating lease rent rose by 9.8, which reduces EBITDA. The retail margin was 33.7% (501.8 over 1489.5) against 32.8% (465.8 over 1418.1). Management states in the release that the "healthy operating trends" continued through October (release Q3 page:1); this is a management claim, not tested here.

Interactive revenue quality. Interactive revenue of 348.4 includes a gaming tax reimbursement gross-up from third-party partners of 191.4 in Q3 2026 and 139.5 in Q3 2025 (10-Q Q3 page:15). Excluding the gross-up, Interactive revenue was 157.0 in Q3 2026 against 158.2 in Q3 2025, a decline of 1.2, and for 9M 2026 493.3 against 498.3, a decline of 5.0. Interactive gaming revenue was 126.6 against 129.3 in Q3. The reported 17.0% increase in Interactive revenue (348.4 against 297.7, an increase of 50.7) is therefore more than accounted for by the gross-up, which rose by 51.9 (191.4 less 139.5). The earnings improvement came from lower costs: media and advertising fell to 39.8 from 73.0 (10-Q Q3 pages 38 and 40), and Q3 2025 media and advertising included 52.0 of ESPN-related advertising (10-Q Q3 page:41); the Sportsbook Agreement was terminated on November 5, 2025 (page:12).

Segments, Q3 2026 against Q3 2025 (10-Q Q3 pages 15, 38 and 40):

| Segment | Revenue Q3 2026 | Revenue Q3 2025 | Segment Adjusted EBITDAR Q3 2026 | Segment Adjusted EBITDAR Q3 2025 |
| --- | --- | --- | --- | --- |
| Northeast | 708.3 | 690.5 | 208.1 | 197.9 |
| South | 291.8 | 291.0 | 108.3 | 97.7 |
| West | 147.5 | 138.3 | 50.9 | 51.1 |
| Midwest | 341.9 | 298.3 | 134.5 | 119.1 |
| Interactive | 348.4 | 297.7 | (18.3) | (76.6) |

### Covenants

The Amended Credit Facilities contain a maximum total net leverage ratio of 4.50 to 1.00, with a step up to 5.00 to 1.00 for certain significant acquisitions, and a minimum interest coverage ratio of 2.00 to 1.00, each "as defined within the Second Amended and Restated Credit Agreement" (10-Q Q3 page:17). The Company states it "was in compliance with all required financial covenants" at 2026-09-30 and expects to remain so for at least twelve months (page:20); the same statement is made at 2026-03-31, 2026-06-30 and 2025-12-31. No step-down is printed. The reported covenant ratio values are Not supplied. Headroom is Not calculable because the agreement is not supplied and the definitions may treat leases, add-backs and cash differently. The metrics computed above differ from the covenant: they are the company's non-GAAP Consolidated Adjusted EBITDA on a principal-debt basis, with cash interest that includes lease interest. The notes and credit agreement also carry cross-default provisions tied to the Master Leases (page:20). The Master Leases (AR PENN and 2023) are cross-defaulted, cross-collateralized and coterminous, with a parent guarantee (page:21).

### Quality and definition notes on EBITDA

Consolidated Adjusted EBITDA adds back stock-based compensation (47.2 for 9M 2026), pre-opening expenses (29.0), impairment, and "Other" of 44.9 for 9M 2026, described as transaction costs, restructuring (severance) and settlement costs and legal and advisory fees for the HG Vora Cooperation Agreement (release Q3 pages 6-7). It is struck after triple net operating lease rent but before interest and depreciation on finance leases and financing obligations; 9M 2026 cash paid to REIT landlords of 746.6 exceeds operating lease rent expense of 494.4 by 252.2, which is the part of landlord payments not deducted in EBITDA. Cash paid for interest on traditional debt only was 100.9 for 9M 2026 against 291.6 cash paid for interest in the cash-flow statement; the cash-flow figure includes lease and financing obligation interest (interest on finance leases 80.8 and on financing obligations 108.8 for 9M 2026, 10-Q Q3 page:28). The sum of 100.9, 80.8 and 108.8 is 290.5, within 1.1 of 291.6; the company does not state this reconciliation and it is an analyst reading.

## Calculations

Inputs are quoted from the locators shown. All amounts in US$m. LTM = FY2025 + 9M 2026 - 9M 2025 unless stated; all three periods are on the same consolidated perimeter. The nine-month 2025 comparatives are taken from the 10-Q Q3 and the FY2025 figures from the 10-K; a reclassification of prior periods is disclosed as possible (10-Q Q3 page:8) and no difference was found in the totals checked.

### Leverage (management basis)

| Period | Calculation | Result |
| --- | --- | --- |
| FY2025 total | 2,904.1 / 830.1 | 3.498, shown 3.50x |
| FY2025 net | (2,904.1 - 686.6) / 830.1 = 2,217.5 / 830.1 | 2.671, shown 2.67x |
| LTM Q1 2026 total, net | 2,948.9 / 922.6; (2,948.9 - 708.0) / 922.6 = 2,240.9 / 922.6 | 3.196 (3.20x); 2.429 (2.43x) |
| LTM Q2 2026 total, net | 2,814.7 / 999.1; (2,814.7 - 887.2) / 999.1 = 1,927.5 / 999.1 | 2.817 (2.82x); 1.929 (1.93x) |
| LTM Q3 2026 total, net | 2,806.6 / 1,088.2; (2,806.6 - 1,044.8) / 1,088.2 = 1,761.8 / 1,088.2 | 2.579 (2.58x); 1.619 (1.62x) |

LTM EBITDA values for Q1, Q2 and Q3 2026 are as printed in the releases (922.6, 999.1, 1,088.2). Check: 830.1 + 862.4 - 604.3 = 1,088.2.

Extended perimeter (analyst construction, not a company measure): add financing obligations 2,309.8 and finance lease liabilities 2,049.6 to debt, because their costs sit below EBITDA. Total 2,806.6 + 2,309.8 + 2,049.6 = 7,166.0; over 1,088.2 = 6.585, shown 6.59x. Net of cash 1,044.8: 6,121.2 / 1,088.2 = 5.625, shown 5.63x. Operating lease liabilities of 3,798.2 are excluded because the rent is deducted in EBITDA. For comparison the company prints a lease-adjusted net leverage of 5.6x, which capitalises cash rent at eight times (7,940.0) and adds it to traditional net debt over EBITDA plus rent (release Q3 page:7).

### Interest cover

LTM cash interest: FY2025 383.0; Q1 2026 LTM 383.0 - 102.0 + 107.8 = 388.8 (10-Q Q1 page:5); Q2 2026 LTM 383.0 - 188.0 + 187.9 = 382.9 (10-Q Q2 page:6); Q3 2026 LTM 383.0 - 292.2 + 291.6 = 382.4 (10-Q Q3 page:6). Cover: 830.1 / 383.0 = 2.167; 922.6 / 388.8 = 2.373; 999.1 / 382.9 = 2.609; 1,088.2 / 382.4 = 2.846. For reference, LTM interest expense, net is 405.8 + 307.7 - 303.9 = 409.6, and 1,088.2 / 409.6 = 2.657.

### Liquidity

Q3 2026: 1,044.8 + (1,000.0 - 23.9) = 1,044.8 + 976.1 = 2,020.9. The release prints "$2.0 billion" (release Q3 page:2). FY2025: 686.6 + (1,000.0 - 570.0 - 23.9) = 686.6 + 406.1 = 1,092.7. Q1 2026: 708.0 + 951.1 = 1,659.1 (release prints $1.7 billion). Q2 2026: 887.2 + 976.1 = 1,863.3 (release prints $1.9 billion). Restricted cash excluded: 28.1 + 1.2 = 29.3 at 2026-09-30; 27.0 + 1.2 = 28.2 at 2025-12-31. The twelve-month maturity bucket from 2026-10-01 to 2027-09-30 is 400.0 fixed plus 32.3 variable = 432.3 (10-Q Q3 page:78); this is covered 4.7 times by liquidity, calculated as 2,020.9 / 432.3.

### Obligations

Financing obligations at 2026-09-30: 47.5 + 2,262.3 = 2,309.8; at 2025-12-31: 45.8 + 2,297.8 = 2,343.6. Finance lease liabilities: 55.6 + 1,994.0 = 2,049.6; 45.7 + 2,017.4 = 2,063.1. Sum of the two: 4,359.4 and 4,406.7. Operating lease liabilities: 422.0 + 3,376.2 = 3,798.2; 386.0 + 3,592.4 = 3,978.4. All three at 2026-09-30: 2,309.8 + 2,049.6 + 3,798.2 = 8,157.6. Debt in the balance sheet: 33.1 + 2,735.2 = 2,768.3, equal to principal 2,806.6 less 38.3 of discounts and costs. Landlord payments less operating rent: 746.6 - 494.4 = 252.2.

### Operating and cash flow

Q3 2026 revenue growth: 1,840.0 / 1,717.3 - 1 = 7.1%. EBITDA bridge: 284.0 - 194.9 = 89.1 = 58.3 (Interactive: -18.3 - (-76.6)) + 36.0 (retail: 501.8 - 465.8) + 4.6 (Other: -31.6 - (-36.2)) - 9.8 (rent: 167.9 - 158.1). Retail Q3 2026 revenue 708.3 + 291.8 + 147.5 + 341.9 = 1,489.5; EBITDAR 208.1 + 108.3 + 50.9 + 134.5 = 501.8; margin 33.7%. Retail Q3 2025 revenue 690.5 + 291.0 + 138.3 + 298.3 = 1,418.1; EBITDAR 197.9 + 97.7 + 51.1 + 119.1 = 465.8; margin 32.8%. Interactive revenue excluding gross-up: 348.4 - 191.4 = 157.0; 297.7 - 139.5 = 158.2; 9M 1,056.0 - 562.7 = 493.3; 903.9 - 405.6 = 498.3. LTM revenue 6,961.0 + 5,476.4 - 5,154.8 = 7,282.6; LTM operating income -673.6 + 355.9 + 656.1 = 338.4; LTM impairment 945.3 + 8.0 - 840.0 = 113.3; LTM net income -845.3 + 62.4 + 771.9 = -11.0; LTM CFO 508.2 + 626.4 - 401.0 = 733.6; LTM capex 647.7 + 251.2 - 457.3 = 441.6; LTM sale-leaseback proceeds 280.0 + 216.3 - 130.0 = 366.3; LTM retail EBITDAR 1,868.8 + 1,490.4 - 1,412.4 = 1,946.8 (FY2025 retail 795.0 + 401.6 + 197.6 + 474.6 = 1,868.8); LTM Interactive -267.5 + (-38.7) - (-227.6) = -78.6. Q3 discrete: CFO 626.4 - 363.1 = 263.3 and 401.0 - 220.1 = 180.9; cash interest 291.6 - 187.9 = 103.7 and 292.2 - 188.0 = 104.2. Free cash flow before lease principal, 9M 2026: 626.4 - 251.2 = 375.2; FY2025: 508.2 - 647.7 = -139.5. Principal on finance leases and financing obligations for 9M 2026 is 41.0 + 34.1 = 75.1, matching the MD&A (10-Q Q3 page:70). No share repurchases in 9M 2026 (10-Q Q3 page:6) against 354.4 in FY2025 (10-K page:109).

Segment bridge check, FY2025: 1,868.8 - 267.5 = 1,601.3; less Other 139.5 = 1,461.8; less rent 631.7 = 830.1, equal to the printed Consolidated Adjusted EBITDA. LTM rent expense computed as 631.7 + 494.4 - 470.0 = 656.1 against 656.2 printed (release Q3 page:7); the printed figure is used and the 0.1 difference is rounding in the source.

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Covenant ratio values, definitions and any step-downs beyond the acquisition step up are Not supplied; the agreement and compliance certificate are absent | Headroom Not calculable; leverage shown is management basis | Obtain the Second Amended and Restated Credit Agreement, amendments and compliance certificate |
| Guarantor identity and restricted perimeter for the credit facilities not located | Priority and structural position of bank debt against notes cannot be stated beyond "senior unsecured, not subsidiary guaranteed" for the 5.625% and 6.75% Notes | Obtain guarantor schedule |
| Ranking and guarantee wording of the 4.125% Notes due 2029 not located on the pages read | Treated as the same class as the other notes only by inference; not asserted | Read the Note 5 note paragraph for the 2029 notes or the indenture |
| Discrete Q3 2026 cash-flow statement not printed | Q3 CFO and cash interest are derived from year-to-date differences | Accept as derived |
| Q3 2025 and 9M 2025 balance sheet debt and lease balances not extracted | Prior-year leverage for those dates not built; the chart uses FY2025 and three 2026 quarter ends | Not needed for the snapshot |
| Purchase obligations after 2025-12-31 not updated in the 10-Q | Latest amount is 473.4 at 2025-12-31 | Request update |
| Balance of insurance financing not located | Small, outside debt | None |
| Guidance amounts not supplied; management states confidence in a full-year Interactive Adjusted EBITDA target without a figure | No forward earnings view from sources | Obtain outlook materials |
| Management presentation not supplied | No slide-level evidence | Obtain if needed |
| Extraction is text only; flattened tables | Page numbers are chunk numbers; spot check any figure that drives a conclusion | Review rendered filings |
| LTM figures mix audited FY2025 with unaudited interim periods and rely on unrestated prior-period comparatives | Small risk of reclassification differences | Accept; labelled |
| EBITDA is a management non-GAAP measure and includes add-backs of 44.9 labelled Other for 9M 2026 | Quality of earnings cannot be tested against the underlying ledger | Treat as management measure |
| No pension, retiree medical, factoring or supply chain finance obligation located | Stated as Not supplied rather than zero | None |

## Next module

CP-1A (business and transaction context) should consume this handoff for the lease structure, the 2026 refinancing sequence, the Interactive segment's dependence on tax gross-up revenue and ESPN termination effects, the Council Bluffs and New Orleans development commitments, and the shareholder cooperation costs. Carry forward: leverage is on a management principal-debt basis and excludes 4,359.4 of financing obligations and finance leases; covenant headroom is Not calculable; the 5.625% Notes of 400.0 mature January 15, 2027; and all LTM values are calculated from year-to-date differences.
