## Request

Issuer: HERC HOLDINGS INC (issuer id hri; ticker HRI), consolidated (Herc Holdings Inc. and subsidiaries). As-of date and evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. Every figure below is in US$ millions (US$m) unless a unit is stated; per-share and ratio figures carry their own unit.

Task: CP-1 financial extraction and base view from the pinned filings and releases: reported statements for FY2025, Q1 2026, Q2 2026 and Q3 2026 (with six-month and nine-month figures), debt by instrument, liquidity by facility, cash interest, covenants, and the chart data the report needs (leverage, interest cover, liquidity, debt maturities). Period labels used throughout: FY2025 (year ended December 31, 2025), Q1 2026, Q2 2026 and Q3 2026 (discrete quarters), 9M 2026 and 9M 2025 (nine months ended September 30), and LTM (twelve months to a quarter-end, built as FY2025 plus year-to-date 2026 less year-to-date 2025). Reported figures are quoted from the sources; anything marked (calc) is calculated in `## Calculations` from the quoted inputs.

The upstream source-readiness handoff (CP-0) found the set READY_WITH_LIMITATIONS for this module: FY2025 and Q4 2025 adjusted EBITDA are not supplied, the pro forma net leverage in the releases cannot be rebuilt, springing covenant trigger levels are not quantified, and executed legal documents are not supplied. Those limitations are carried below. This handoff agrees with CP-0 and corrects none of it, with one refinement: CP-0 said the 10-K maturity schedule shows no amount "labelled" for the AR Facility; the schedule is read here as unlabelled by instrument (see Gaps).

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_hri-20251231.htm.jsonl | 1e4fc8e6ec5ecb19b2d87edd4dd39a4f8c262f1bbf4300e6c71728880e6a40f2 | FY2025 statements (page:78-81), Note 11 debt (page:103-118), maturities (page:103-104), notes ranking and guarantees (page:105-113), ABL and term loan terms (page:114-116), leases (page:103), pension (page:119-120) |
| 10-Q_2026-03-31_hri-20260331.htm.jsonl | 957fad2e7bcc77d998a4d47ace97dbbe723d0ae0ec8bb0e66ef9b0a24106db4a | Q1 2026 statements (page:3-5), Note 8 debt (page:17-18), availability (page:20) |
| 10-Q_2026-06-30_hri-20260630.htm.jsonl | e3f28b820e10e5baa7e77b727c26f2b087fc86a20a6ecf0c0005cebe89eab4df | Q2 and six-month 2026 statements (page:3-6), Note 8 debt (page:16-17), availability (page:17) |
| 10-Q_2026-09-30_hri-20260930.htm.jsonl | b4f098a700c1a9ded56e8016e540343e20a52efa45a322a642b6b1a64bf553ce | Q3 and nine-month 2026 statements (page:3-6), Note 8 debt (page:17-18), availability (page:18-19, 32), covenants (page:33), fair value of debt (page:21) |
| EX-99.1_2026-04-28_herc2026q1-pressrelease.htm.jsonl | 6727d6749dee62dba3ecdf247326c2640487c30ff4e58831034efb2c2e6000e2 | Q1 2026 EBITDA and adjusted EBITDA reconciliation (page:8), management net leverage and liquidity (page:3) |
| EX-99.1_2026-07-28_herc2026q2-pressrelease.htm.jsonl | 0768981a704e5281116cd18bf157f1264a3d3fbf5f9bb078071dab4e27ecc390 | Q2 and six-month reconciliation (page:9), free cash flow (page:11), management net leverage (page:3) |
| EX-99.1_2026-10-27_herc2026q3-pressrelease.htm.jsonl | aa1bf8bfd1f475ff27dc8e4345039b652970320635f5a3f0648d622e08bd7d29 | Q3 and nine-month reconciliation (page:9), free cash flow (page:11), management net leverage, liquidity and outlook (page:4) |

Run context (not issuer evidence): sha256 5d9781ebccde905b27f5dd6b19356b8d3ac042aedfacbbb25d2f4ac0a0fab2ab (1364479-herc-holdings-inc-hri.json); it sets the dates, USD currency and pathway only.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | eb84541ef3ec464072f6948bbd0e47034a850882250e2610e4b23144076a659d | Source readiness, entity perimeter, gap register; opened and used for the period map, the perimeter (consolidated Herc Holdings Inc., with Herc Rentals Inc. as operating subsidiary and Herc Receivables U.S. LLC as consolidated securitization vehicle) and the carried limitations |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Gross debt to trailing reported EBITDA fell from 5.41x at FY2025 to 4.18x at Q3 2026, while gross debt moved only from US$8,103m to US$8,080m; cash plus borrowing-base availability was US$2,100m. | Medium | FY2025 adjusted EBITDA is not supplied, so management's 3.90x pro forma net leverage cannot be rebuilt; ratios here use unadjusted reported EBITDA. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Cash interest paid over the twelve months to Q3 2026 was US$530m against reported EBITDA of US$1,932m, giving cover of 3.65x. | Cover is moderate, and quarterly cash interest swings with coupon dates, so trailing figures are more reliable than single quarters. | High |
| Net rental equipment spending over the same twelve months was US$857m, leaving US$1,075m of EBITDA after fleet reinvestment. | Gross debt is 7.52x that residual, so fleet capital intensity matters more than headline EBITDA leverage. | Medium |
| Liquidity at Q3 2026 was cash of US$66m plus US$2,034m of ABL availability; the AR Facility is fully drawn at US$550m. | Liquidity rests on the asset-based revolver; the AR Facility matures August 31, 2027, within twelve months of the balance sheet date. | High |
| Derived free cash flow was negative US$69m in Q3 2026 after rental equipment spending of US$499m, with US$252m of equipment purchases unpaid in payables. | Unpaid purchases are a near-term cash call, and raised capex guidance implies further fleet spending in Q4 2026. | Medium |
| No maintenance covenants apply; a 1.00:1.00 fixed charge ratio springs only if liquidity falls below levels the filings do not quantify. | Covenant headroom cannot be tested from the filings; the revolver liquidity trigger is the relevant protection. | Medium |

### Financial base view

The financial base is usable with stated limitations. Every statement the module needs (income statement, balance sheet, cash flow, debt note, availability table and the non-GAAP reconciliations) is present for FY2025 and for each of Q1, Q2 and Q3 2026, and the figures tie internally: the expense blocks reconcile to pretax income in each period, the three discrete quarters sum to 9M 2026, the debt instruments sum to the printed total debt, the maturity schedule sums to the FY2025 gross debt, and the ABL availability equals the US$4,000m commitment less borrowings and standby letters of credit (all in `## Calculations`). The filing perimeter is the consolidated group; the 10-Q states Holdings and Herc are substantially identical apart from the debt held at Holdings, so no separate operating-company statements are needed or supplied.

Two limits shape how far the ratios can be pushed. First, the only EBITDA that can be built for every window is the company's unadjusted EBITDA (net income plus tax, net interest, rental depreciation and non-rental depreciation and amortization). Adjusted EBITDA is printed for the 2026 quarters, 6M and 9M and their 2025 comparatives, but not for FY2025 or Q4 2025, so no trailing adjusted EBITDA exists in the pack. Second, the H&E acquisition closed on June 2, 2025, so the LTM windows to FY2025, Q1 2026 and Q2 2026 contain months before the acquired earnings arrive while the year-end debt already funds them; their leverage is overstated against a pro forma view, and only the LTM to Q3 2026 (October 2025 to September 2026) is a clean post-acquisition window. Management's net leverage of 3.90x at Q3 2026 uses pro forma trailing adjusted EBITDA and is shown as attributed management data only. A ratio calculated here is a CP-1 calculation, not a covenant or management figure.

| Item | View |
| --- | --- |
| Statement coverage | Complete for FY2025 and Q1 to Q3 2026; interim figures unaudited, FY2025 audited |
| EBITDA basis | Company-defined unadjusted EBITDA; adjusted EBITDA only for 2026 periods and 2025 comparatives |
| Leverage window quality | Only LTM Q3 2026 is a full post-acquisition window |
| Debt completeness | All instruments listed with rate, maturity and security; legal documents not supplied |
| Covenants | No maintenance covenants; springing fixed charge ratio with unquantified trigger |

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 (December 31, 2025) | 5.41 | 5.38 | x | Total debt is the sum of printed instrument principal incl. finance leases (8,103); net debt less cash 52. EBITDA is unadjusted reported EBITDA for FY2025 (1,497, calc). Not pro forma: H&E included only from June 2, 2025, so overstated against a pro forma view. |
| Q1 2026 (LTM to March 31, 2026) | 4.85 | 4.82 | x | Debt 8,038; cash 43. LTM EBITDA 1,658 (calc: FY2025 plus Q1 2026 less Q1 2025). Window includes pre-acquisition months; not pro forma. Management reports net leverage of 3.96x on pro forma adjusted EBITDA (Q1 release page:3). |
| Q2 2026 (LTM to June 30, 2026) | 4.32 | 4.29 | x | Debt 7,963; cash 43. LTM EBITDA 1,845 (calc). Window includes pre-acquisition months; not pro forma. Management reports 3.95x on pro forma adjusted EBITDA (Q2 release page:3). |
| Q3 2026 (LTM to September 30, 2026) | 4.18 | 4.15 | x | Debt 8,080; cash 66. LTM EBITDA 1,932 (calc), the only full post-acquisition window. Unadjusted: excludes the add-backs management uses. Management reports 3.90x on pro forma adjusted EBITDA (Q3 release page:4). Financing obligations (sale-leasebacks) and operating leases are outside both ratios. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 3.57 | x | Unadjusted EBITDA 1,497 (calc) over cash paid for interest 419 (10-K page:81). Interest stepped up from June 2, 2025 with the acquisition debt, so the year mixes pre- and post-acquisition interest. |
| Q1 2026 (LTM) | 3.99 | x | LTM EBITDA 1,658 over LTM cash interest 416 (calc: 419 plus 63 less 66). Coupon dates make single quarters lumpy, so only LTM is shown. |
| Q2 2026 (LTM) | 3.47 | x | LTM EBITDA 1,845 over LTM cash interest 532 (calc: 419 plus 232 less 119). The 6M 2025 comparative of 119 includes only one month of the acquisition debt. |
| Q3 2026 (LTM) | 3.65 | x | LTM EBITDA 1,932 over LTM cash interest 530 (calc: 419 plus 313 less 202). Unadjusted EBITDA; cash paid for interest per the cash flow statement supplemental disclosure (Q3 10-Q page:6). |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| December 31, 2025 | 52 | 1,880 | US$m | ABL availability under the borrowing base limitation (remaining capacity 1,900, net of 53 standby letters of credit); AR Facility availability nil (10-K page:118). Cash is the balance sheet line; restricted cash is not separately disclosed. |
| March 31, 2026 | 43 | 1,906 | US$m | ABL availability under the borrowing base (remaining capacity 1,972, net of 47 standby letters of credit); AR Facility nil (Q1 10-Q page:20). |
| June 30, 2026 | 43 | 2,007 | US$m | ABL availability under the borrowing base (remaining capacity 2,089, net of 33 standby letters of credit); AR Facility nil (Q2 10-Q page:17). |
| September 30, 2026 | 66 | 2,034 | US$m | ABL availability under the borrowing base equals remaining capacity (2,034, net of 16 standby letters of credit); AR Facility fully drawn at 550, availability nil (Q3 10-Q page:18-19). AR Facility matures August 31, 2027. Surety-backed letters of credit of 39 are outside the ABL sublimit. Availability depends on the borrowing base. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 26 | US$m | Nominal principal maturing in the year ending December 31, 2026, per the 10-K schedule at December 31, 2025 (page:103-104). No later schedule is printed. |
| 2027 | 21 | US$m | As above. The Q3 10-Q (page:18) extends the AR Facility maturity to August 31, 2027; the schedule predates that amendment. |
| 2028 | 497 | US$m | As above. The size is consistent with, but the filing does not state, the AR Facility (475 at December 31, 2025) sitting here; its debt-table maturity then read 2026. |
| 2029 | 819 | US$m | As above; includes the 6.625% Senior Notes due 2029 (800). |
| 2030 | 3,713 | US$m | As above; includes the 7.00% Senior Notes due 2030 (1,650) and the ABL Credit Facility (2,047 drawn at December 31, 2025, maturing June 2, 2030). |
| Thereafter | 3,027 | US$m | As above; 2031 Notes (600), 2033 Notes (1,100), 2034 Notes (600), the Term Loan Facility balance after scheduled amortization and finance leases beyond 2030. Total of all rows 8,103. |

### Financials and credit metrics

| Metric (US$m unless stated) | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | 9M 2026 | 9M 2025 | Basis and source locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenues | 4,376 | 1,139 | 1,204 | 1,364 | 3,707 | 3,167 | Statements of operations: 10-K page:78-79; Q1 10-Q page:4; Q2 10-Q page:4; Q3 10-Q page:4 |
| Equipment rental revenue | 3,770 | 981 | 1,072 | 1,254 | 3,307 | 2,731 | Same locators |
| Direct operating expense | 1,602 | 453 | 491 | 532 | 1,476 | 1,173 | Same locators |
| Selling, general and administrative | 564 | 146 | 155 | 178 | 479 | 411 | Same locators |
| Depreciation of rental equipment | 856 | 242 | 242 | 255 | 739 | 613 | Same locators |
| Non-rental depreciation and amortization | 224 | 73 | 75 | 74 | 222 | 148 | Same locators |
| Transaction expenses | 199 | 5 | 3 | 1 | 9 | 185 | Same locators |
| Interest expense, net | 416 | 128 | 126 | 126 | 380 | 282 | Same locators; FY2025 includes loss on early extinguishment of 2 (10-K page:80, page:104) |
| Income (loss) before income taxes | 1 | (23) | 24 | 120 | 121 | (16) | Same locators |
| Income tax provision | nil (printed dash) | (1) | (5) | (16) | (22) | (7) | Same locators; FY2025 line prints a dash |
| Net income (loss) | 1 | (24) | 19 | 104 | 99 | (23) | Same locators |
| EBITDA, company definition | 1,497 (calc) | 420 | 467 | 575 | 1,462 | 1,027 | Reconciliations: Q1 release page:8; Q2 release page:9; Q3 release page:9; FY2025 calculated from 10-K lines |
| Adjusted EBITDA, as reported | Not supplied: no FY2025 reconciliation in the pack | 448 | 487 | 603 | 1,538 | 1,299 | Same release locators |
| Adjusted EBITDA margin, as reported (%) | Not supplied | 39.3 | 40.4 | 44.2 | 41.5 | 41.0 | Same release locators |
| LTM EBITDA, company definition (calc) | 1,497 | 1,658 | 1,845 | 1,932 | Not applicable | Not applicable | Period-end LTM at each column date; see Calculations |
| Net cash from operating activities | 1,085 | 277 | 314 (calc) | 360 (calc) | 951 | 770 | Cash flow statements: 10-K page:80; Q1 10-Q page:5; Q2 10-Q page:5-6 (6M 591); Q3 10-Q page:6 |
| Rental equipment expenditures | 1,097 | 272 | 285 (calc) | 499 (calc) | 1,056 | 835 | Same cash flow locators; Q2 and Q3 discrete derived from cumulative figures (6M 557) |
| Proceeds from disposal of rental equipment | 448 | 117 | 113 (calc) | 89 (calc) | 319 | 306 | Same cash flow locators (6M 230) |
| Free cash flow, company definition | 299 (calc) | 94 | 108 (calc) | (69) (calc) | 133 | 133 | Release schedules: Q2 release page:11 (6M 202); Q3 release page:11; Q1 value is the Q1 release headline (page:1) |
| Cash paid for interest | 419 | 63 | 169 (calc) | 81 (calc) | 313 | 202 | Supplemental cash flow disclosures: 10-K page:81; Q1 10-Q page:5; Q2 10-Q page:6 (6M 232); Q3 10-Q page:6 |
| Cash paid for income taxes, net | 24 | nil (printed dash) | 6 (calc) | 4 (calc) | 10 | 18 | Same locators (6M 6) |
| Dividends paid | 87 | 24 | 23 (calc) | 24 (calc) | 71 | 64 | Same cash flow locators (6M 47) |
| Cash and cash equivalents (period end) | 52 | 43 | 43 | 66 | Not applicable | Not applicable | Balance sheets: 10-K page:78; Q1 10-Q page:3; Q2 10-Q page:3; Q3 10-Q page:3 |
| Gross debt, sum of instrument principal (period end, calc) | 8,103 | 8,038 | 7,963 | 8,080 | Not applicable | Not applicable | Note 11 and Note 8 debt tables; includes finance leases, excludes sale-leaseback financing obligations |
| Total debt as printed, net of unamortized costs (period end) | 8,047 | 7,985 | 7,912 | 8,031 | Not applicable | Not applicable | 10-K page:103; Q1 10-Q page:17; Q2 10-Q page:17; Q3 10-Q page:18 |
| Financing obligations, net (balance sheet, period end) | 95 | 94 | 93 | 92 | Not applicable | Not applicable | Balance sheets, same locators |
| Operating lease liabilities, current plus non-current (period end, calc) | 1,535 | 1,559 | 1,548 | 1,502 | Not applicable | Not applicable | Balance sheets, same locators |
| Total equity (period end) | 1,948 | 1,898 | 1,890 | 1,984 | Not applicable | Not applicable | Balance sheets, same locators |
| Total assets (period end) | 13,776 | 13,564 | 13,717 | 14,057 | Not applicable | Not applicable | Balance sheets; Q1 from Q1 release page:7, Q2 from Q2 release page:8 |
| Gross debt / LTM EBITDA (x, calc) | 5.41 | 4.85 | 4.32 | 4.18 | Not applicable | Not applicable | See leverage chart basis |
| EBITDA / LTM cash interest (x, calc) | 3.57 | 3.99 | 3.47 | 3.65 | Not applicable | Not applicable | See interest cover chart basis |
| Net leverage as reported by management (x) | Not supplied | 3.96 | 3.95 | 3.90 | Not applicable | Not applicable | Pro forma trailing adjusted EBITDA; attributed management data (release pages above) |

### Debt by instrument at September 30, 2026

All security and guarantor statements below are from the 10-K note (page numbers cited) and are as the filing describes them; the executed documents are not supplied. Issuer and borrower: Herc Holdings Inc. is the issuer of the Senior Notes and the Term Loan borrower; the ABL borrowers include Herc Holdings Inc., Herc Rentals Inc., Matthews Equipment Limited and other subsidiaries (10-K page:114). Co-issuer: none is stated in the note text read; the exhibit list also names Herc Holdings Escrow, Inc. as a party to the June 2, 2025 indenture (10-K page:136), a role the note text does not describe.

| Instrument | Amount | Stated rate | Maturity | Ranking and security | Guarantors | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| 2029 Notes | 800 | 6.625% fixed (weighted stated 6.63%) | June 15, 2029 | Senior unsecured; effectively junior to ABL and Term Loan to the extent of collateral | Current and future domestic subsidiaries, with exceptions including securitization subsidiaries | Q3 10-Q page:17; Q1 10-Q page:18; 10-K page:105 |
| 2030 Notes | 1,650 | 7.00% fixed | June 15, 2030 | Senior unsecured | Same description | Q1 10-Q page:18; 10-K page:107 |
| 2031 Notes | 600 | 5.75% fixed | March 15, 2031 | Senior unsecured | Same description | Q1 10-Q page:18; 10-K page:108 |
| 2033 Notes | 1,100 | 7.25% fixed | June 15, 2033 | Senior unsecured | Same description | Q1 10-Q page:18; 10-K page:110 |
| 2034 Notes | 600 | 6.00% fixed | March 15, 2034 | Senior unsecured | Same description | Q1 10-Q page:18; 10-K page:112 |
| ABL Credit Facility | 1,950 drawn (maximum borrowings 4,000 per the 10-K) | Floating, weighted stated 5.24%; Term SOFR plus an initial 1.375% margin | June 2, 2030 | Senior secured; first-priority liens on substantially all assets of borrowers and guarantors, pari passu with the Term Loan | U.S. and Canadian subsidiaries, with exceptions including securitization subsidiaries | Q3 10-Q page:17; 10-K page:114-115 |
| Term Loan Facility | 744 | Floating, weighted stated 5.64%; Term SOFR plus 1.75% | June 2, 2032; 1.00% annual amortization paid quarterly | Senior secured, pari passu with the ABL | U.S. subsidiaries, with exceptions | Q3 10-Q page:17; 10-K page:116 |
| AR Facility | 550 (commitments raised to 550 in August 2026) | Floating, weighted stated 4.49% | August 31, 2027 (extended in August 2026) | Secured on receivables of the consolidated special-purpose entity Herc Receivables U.S. LLC; assets not available to other creditors | Herc Rentals Inc. gives a performance guarantee as servicer | Q3 10-Q page:17-18; 10-K page:117 |
| Finance lease liabilities | 86 | 4.72% effective | 2026 to 2044 | Lease obligations | Not applicable | Q3 10-Q page:18 |
| Unamortized costs and discount | (49) | Not applicable | Not applicable | Not applicable | Not applicable | Q3 10-Q page:18 |
| Total debt as printed | 8,031 | Not applicable | Not applicable | Sum ties to printed total (see Calculations) | Not applicable | Q3 10-Q page:18 |

Fair value (Level 2) of the Notes and Term Loan at September 30, 2026 was US$5,453m against nominal US$5,494m (Q3 10-Q page:21), a management-reported market indication, not a trading price.

### Obligations outside the debt figure

| Claim | Amount and period | Inside or outside gross debt | Locator |
| --- | --- | --- | --- |
| Sale-leaseback financing obligations (44 properties and certain service vehicles, not sale-leaseback accounted) | 99 gross, 97 net of costs at September 30, 2026; maturities 2037 to 2038 | Outside; separate balance sheet line with 92 non-current and 5 current | Q3 10-Q page:19 |
| Operating lease liabilities | 1,502 at September 30, 2026 (59 current plus 1,443 non-current, calc) | Outside | Q3 10-Q page:3 |
| Finance leases | 86 | Inside | Q3 10-Q page:18 |
| Standby letters of credit | 16 issued, none drawn, at September 30, 2026 | Outside debt; reduces ABL capacity | Q3 10-Q page:18 |
| Surety-backed letters of credit | 39 at September 30, 2026, including 25 that replaced insurance-related bank letters of credit in July 2026 | Outside; do not reduce ABL capacity | Q3 10-Q page:18 |
| Pension (Herc Holdings Retirement Plan, frozen to new employees; multiemployer plans) | Funded status deficit of 8 at December 31, 2025; the Q3 10-Q does not update it | Outside | 10-K page:119-120 |
| Service vehicle purchase commitment | 12 accrued at December 31, 2025 | Outside; no later figure | 10-K page:103 |
| Litigation and indemnities | Ordinary-course claims; no material adverse effect expected by management; indemnities customary | Outside; not quantified | Q3 10-Q page:19-20 |
| Cinelease earnout receivable (asset) | 32 at fair value, payable primarily in 2028 and 2029 | Asset, not a claim | Q3 10-Q page:21-22 |
| Factoring and supply-chain finance | Not found in the filings; the AR Facility is an on-balance-sheet securitization inside debt | Inside (AR Facility) | Q3 10-Q page:17-18 |

### Covenants and compliance

No financial maintenance covenants apply to the ABL Credit Facility, AR Facility, Term Loan Facility or Notes. Under the ABL, "failure to maintain certain levels of liquidity" triggers a fixed charge coverage ratio of not less than 1:1 for the four most recent quarters; at September 30, 2026 "the appropriate levels of liquidity have been maintained", so the test is not applicable and the company states it was in compliance with all applicable covenants (Q3 10-Q page:33; 10-K page:115). The trigger level of liquidity or excess availability and the covenant's own definition of fixed charge coverage are not quantified in the filings, so headroom is Not calculable. The covenant definition would differ from the EBITDA used here: the ABL ratio is a fixed charge ratio on the credit agreement's own definitions, not EBITDA over cash interest. The indentures contain incurrence-type limitations on debt, restricted payments and liens, and a change of control put at 101% (10-K page:105), described at summary level only. Dividends are restricted by the debt agreements (Q3 10-Q page:33).

### Latest quarter and subsequent events

| Event | Date and amount | Locator |
| --- | --- | --- |
| AR Facility commitments raised | May 2026, from 475 to 500; August 2026, to 550 with maturity extended to August 31, 2027 | Q3 10-Q page:18 |
| Insurance-related bank letters of credit replaced by surety-backed letters of credit | July 2026, 25 | Q3 10-Q page:18, page:32 |
| Quarterly dividend declared | August 19, 2026, US$0.70 per share, paid September 16, 2026 | Q3 10-Q page:33 |
| Outlook raised | October 27, 2026: equipment rental revenue 4,475 to 4,550; adjusted EBITDA 2,100 to 2,150; net rental equipment capex 1,000 to 1,100; gross capex 1,450 to 1,600 (previous ranges 4,375 to 4,475; 2,050 to 2,125; 850 to 950; 1,250 to 1,400) | Q3 release page:4 |
| Greenfield branches opened | 2 in Q3 2026 | Q3 release page:3 |
| H&E measurement period adjustments finalized | Q2 2026; goodwill decreased by 12 | Q3 10-Q page:16 |
| Subsequent events after September 30, 2026 | None stated in the Q3 10-Q; the only post-quarter items are the October 27, 2026 release and outlook | Q3 10-Q (no subsequent events note found) |

### Definition review

| Definition | Reading and risk |
| --- | --- |
| EBITDA (company) | Net income plus income tax, interest expense net, depreciation of rental equipment and non-rental depreciation and amortization (Q3 release page:9). Adding back rental depreciation is normal for the sector but leaves the fleet replacement cost, which is why EBITDA after net rental capex is shown. |
| Adjusted EBITDA (company) | EBITDA plus non-cash stock compensation, transaction expenses, restructuring, fair-value mark-up of acquired fleet sold, and other items. For 9M 2026 the add-backs are the difference between 1,538 and 1,462, which is 76 (calc). Stock compensation is a recurring cost and the fair-value mark-up is an acquisition-accounting effect; both flatter adjusted EBITDA relative to cash earnings. |
| Free cash flow (company) | Operating cash flow less rental and non-rental capex plus disposal proceeds (Q3 release page:11). Disposal proceeds of 319 for 9M 2026 are included, so the measure depends on continued fleet sales. |
| Net leverage (management) | Net debt over pro forma trailing twelve-month adjusted EBITDA including H&E standalone pre-acquisition results (Q3 release page:4). Not reproducible here. Net debt printed as US$8.0 billion at Q3 2026 agrees with the 8,014 calculated here from instrument principal less cash. |
| Total debt / net debt (this module) | Instrument principal including finance leases, before unamortized costs, with net debt after cash. Excludes sale-leaseback financing obligations and operating leases. |
| Dollar utilization and OEC | Management operating measures (Q3 release page:5); not used in any ratio. |

### Interpretation

**Leverage fell mainly because earnings grew, not because debt was repaid.** Gross debt moved from 8,103 at FY2025 to 8,080 at Q3 2026 (calc), while LTM unadjusted EBITDA rose from 1,497 to 1,932 (calc) as the H&E contribution replaced pre-acquisition months in the window and the 2026 quarters grew. The mechanism is the acquisition debt carried in full against a part-year earnings base at year-end; the credit implication is that deleveraging depends on EBITDA delivery and fleet-spending discipline rather than on scheduled amortization (the term loan amortizes at 1.00% a year). The LTM to Q3 2026 window starts after the H&E closing, so the stated pro forma element should add little there. Analyst interpretation: management's lower 3.90x is therefore mostly add-backs rather than pro forma earnings; this cannot be verified without FY2025 adjusted EBITDA.

**Fleet reinvestment absorbs much of the EBITDA.** Net rental equipment capex was 857 over the LTM (calc) and the raised outlook of US$1,000m to US$1,100m for FY2026 against 737 in 9M 2026 implies Q4 2026 net rental capex of 263 to 363 (calc). Operating cash flow of 951 in 9M 2026 exceeded net capex and left company-defined free cash flow of 133, but derived free cash flow was negative in Q3 2026 and equipment purchases in payables rose to 252 from 19 at FY2025 (10-K page:81; Q3 10-Q page:6). The implication is that liquidity must absorb timing swings in fleet payments, and the revolver, not internally generated cash, is the buffer.

**Interest is mostly fixed and lumpy by coupon dates.** The five Senior Notes (4,750, fixed rate) carry coupons that sum to 318.75 a year (calc), paid on June 15 and December 15 for the 2029, 2030 and 2033 Notes and on March 15 and September 15 for the 2031 and 2034 Notes. That explains cash interest of 169 in Q2 2026 against 81 in Q3 2026 (calc). Floating debt (ABL, Term Loan, AR Facility) is 3,244 at September 30, 2026, which is 40.1% of gross debt (calc), so a change in short-term rates feeds directly into that share. Weighted stated rates at September 30, 2026 were 5.24% (ABL), 5.64% (Term Loan) and 4.49% (AR Facility) against 5.10%, 5.52% and 4.68% at December 31, 2025 (Q3 10-Q page:17; 10-K page:103), so floating costs were not lower than at year-end. Indicative annual interest at September 30, 2026 stated rates is 491.65 (calc), against LTM cash interest of 530 and Q3 2026 interest expense of 126, which brackets a run-rate near 500.

**Liquidity depends on the borrowing base and a single facility.** Cash plus ABL availability was 2,100 at Q3 2026, up from 1,932 at FY2025, helped by lower ABL borrowings and the replacement of 25 of bank letters of credit with surety-backed ones. The AR Facility is fully drawn and matures August 31, 2027; the company classifies it as long-term on its intent and ability to refinance it or use ABL capacity (Q3 10-Q page:18), which makes the revolver the fallback. The ABL matures June 2, 2030. No maintenance covenant restricts drawing, but a fixed charge test would apply if availability fell below an unquantified level.

**Balance sheet quality.** Goodwill of 2,859 and intangible assets of 1,559 exceed total equity of 1,984, so tangible equity is negative 2,434 (calc). Rental equipment, net was 6,190 against secured debt of 3,244 (ABL, Term Loan, AR Facility; ratio 1.91x, calc), but the rental equipment is also the main collateral for the ABL and Term Loan, so the unsecured Notes of 4,750 rank behind those claims on the same assets.

## Calculations

All inputs are quoted from the sources listed above; results are calculated as shown. US$m unless stated.

### Statement tie-outs

| Check | Inputs | Result |
| --- | --- | --- |
| Q3 2026 expenses | 532 + 255 + 68 + 9 + 178 + 1 + 74 + 126 + 0 + 1 | 1,244 = printed total expenses; revenues 1,364 less 1,244 = 120 pretax, as printed |
| 9M 2026 expenses | 1,476 + 739 + 263 + 26 + 479 + 9 + 222 + 380 + 0 - 8 | 3,586 = printed; 3,707 - 3,586 = 121 pretax, as printed |
| Q1 2026 expenses | 453 + 242 + 109 + 9 + 146 + 5 + 73 + 128 - 3 | 1,162 = printed; 1,139 - 1,162 = -23 pretax, as printed |
| Q2 2026 expenses | 491 + 242 + 86 + 8 + 155 + 3 + 75 + 126 + 0 - 6 | 1,180 = printed; 1,204 - 1,180 = 24 pretax, as printed |
| FY2025 expenses | 1,602 + 856 + 418 + 42 + 564 + 199 + 224 + 416 + 48 + 6 | 4,375 = printed; 4,376 - 4,375 = 1 pretax, as printed |
| Quarters sum to 9M 2026 | Revenue 1,139 + 1,204 + 1,364; net income -24 + 19 + 104; interest 128 + 126 + 126 | 3,707; 99; 380 = printed 9M figures |
| EBITDA quarters sum | 420 + 467 + 575 | 1,462 = printed 9M 2026 EBITDA |
| Q3 2026 balance sheet | Total liabilities 12,073 + total equity 1,984 | 14,057 = printed total assets |
| 9M 2026 cash | 951 - 818 - 119 = 14; 52 + 14 | 66 = printed cash at September 30, 2026 |
| FY2025 cash | 1,085 - 4,944 + 3,827 + 1 (FX) = -31; 83 - 31 | 52 = printed cash |
| Debt table at September 30, 2026 | 800 + 1,650 + 600 + 1,100 + 600 + 1,950 + 744 + 550 + 86 - 49 | 8,031 = printed total debt; current 27 + non-current 8,004 = 8,031 |
| Maturity schedule | 26 + 21 + 497 + 819 + 3,713 + 3,027 | 8,103 = gross debt at December 31, 2025 (800 + 1,650 + 600 + 1,100 + 600 + 2,047 + 750 + 475 + 81) |
| ABL availability, September 30, 2026 | 4,000 maximum borrowings - 1,950 drawn - 16 standby letters of credit | 2,034 = printed remaining capacity |
| ABL availability, December 31, 2025 | 4,000 - 2,047 - 53 | 1,900 = printed remaining capacity |
| ABL availability, March 31, 2026 | 4,000 - 1,981 - 47 | 1,972 = printed |
| ABL availability, June 30, 2026 | 4,000 - 1,878 - 33 | 2,089 = printed |

The US$4,000m ABL maximum is from the 10-K (page:114) and is assumed unchanged; the tie-outs above support that assumption, and the 10-Q reports no change to material terms.

### EBITDA and LTM bridges

| Item | Inputs | Result |
| --- | --- | --- |
| FY2025 EBITDA (company definition) | Net income 1 + income tax nil + interest expense, net 416 + depreciation of rental equipment 856 + non-rental depreciation and amortization 224 | 1,497 |
| Q4 2025 EBITDA (derived) | 1,497 - 1,027 (9M 2025) | 470 |
| LTM EBITDA to Q1 2026 | 1,497 + 420 - 259 | 1,658 |
| LTM EBITDA to Q2 2026 | 1,497 + 887 - 539 | 1,845 |
| LTM EBITDA to Q3 2026 | 1,497 + 1,462 - 1,027 | 1,932 |
| Q2 and Q3 2026 EBITDA tie | 887 - 420; 1,462 - 887 | 467 and 575, equal to the printed quarterly reconciliations |
| 9M 2026 add-backs to adjusted EBITDA | 1,538 - 1,462 | 76 |

### Debt, leverage and cover

| Item | Inputs | Result |
| --- | --- | --- |
| Gross debt, FY2025 | 800 + 1,650 + 600 + 1,100 + 600 + 2,047 + 750 + 475 + 81 | 8,103 |
| Gross debt, Q1 2026 | 4,750 + 1,981 + 748 + 475 + 84 | 8,038 |
| Gross debt, Q2 2026 | 4,750 + 1,878 + 746 + 500 + 89 | 7,963 |
| Gross debt, Q3 2026 | 4,750 + 1,950 + 744 + 550 + 86 | 8,080 |
| Net debt FY2025 / Q1 / Q2 / Q3 | 8,103 - 52; 8,038 - 43; 7,963 - 43; 8,080 - 66 | 8,051; 7,995; 7,920; 8,014 |
| Gross debt / LTM EBITDA | 8,103 / 1,497; 8,038 / 1,658; 7,963 / 1,845; 8,080 / 1,932 | 5.41x; 4.85x; 4.32x; 4.18x |
| Net debt / LTM EBITDA | 8,051 / 1,497; 7,995 / 1,658; 7,920 / 1,845; 8,014 / 1,932 | 5.38x; 4.82x; 4.29x; 4.15x |
| LTM cash interest | FY2025 419; Q1: 419 + 63 - 66; Q2: 419 + 232 - 119; Q3: 419 + 313 - 202 | 419; 416; 532; 530 |
| EBITDA / LTM cash interest | 1,497 / 419; 1,658 / 416; 1,845 / 532; 1,932 / 530 | 3.57x; 3.99x; 3.47x; 3.65x |
| Discrete cash interest | Q2: 232 - 63; Q3: 313 - 232 | 169; 81 |
| Note coupons per year | 800 x 6.625% + 1,650 x 7.00% + 600 x 5.75% + 1,100 x 7.25% + 600 x 6.00% | 53.00 + 115.50 + 34.50 + 79.75 + 36.00 = 318.75 |
| Floating debt, September 30, 2026 | ABL 1,950 + Term Loan 744 + AR Facility 550 | 3,244 |
| Indicative annual interest at stated rates | Notes 318.75 + ABL 1,950 x 5.24% (102.18) + Term Loan 744 x 5.64% (41.96) + AR 550 x 4.49% (24.70) + finance leases 86 x 4.72% (4.06) | 491.65, excluding fees, amortization of debt costs and sale-leaseback financing obligations |
| Floating share of gross debt, September 30, 2026 | 3,244 / 8,080 | 40.1% |
| Change in gross debt FY2025 to Q3 2026 | 8,080 - 8,103 | -23 |

### Capital intensity, cash flow and liquidity

| Item | Inputs | Result |
| --- | --- | --- |
| Discrete operating cash flow | Q2: 591 - 277; Q3: 951 - 591 | 314; 360 |
| Discrete rental equipment expenditures | Q2: 557 - 272; Q3: 1,056 - 557 | 285; 499 |
| Discrete disposal proceeds | Q2: 230 - 117; Q3: 319 - 230 | 113; 89 |
| Free cash flow, company definition, FY2025 | 1,085 - 1,097 + 448 - 157 + 20 | 299 |
| Free cash flow, Q1 2026 check | 277 - 272 + 117 - 41 + 13 | 94, equal to the Q1 release headline |
| Free cash flow, 6M 2026 check | 591 - 557 + 230 - 82 + 20 | 202, equal to the Q2 release |
| Free cash flow, Q2 and Q3 2026 | Q2: 202 - 94; Q3: 133 - 202 | 108; -69 |
| Net rental equipment capex, LTM to Q3 2026 | (1,097 - 448) + (1,056 - 319) - (835 - 306) = 649 + 737 - 529 | 857 |
| EBITDA after net rental capex, LTM | 1,932 - 857 | 1,075 |
| Gross debt / EBITDA after net rental capex | 8,080 / 1,075 | 7.52x |
| LTM operating cash flow | 1,085 + 951 - 770 | 1,266 |
| Implied Q4 2026 net rental capex from outlook | 1,000 - 737; 1,100 - 737 | 263 to 363 |
| Implied Q4 2026 adjusted EBITDA from outlook | 2,100 - 1,538; 2,150 - 1,538 | 562 to 612 (management outlook, forward-looking) |
| Liquidity (cash + ABL availability under the borrowing base) | FY2025 52 + 1,880; Q1 43 + 1,906; Q2 43 + 2,007; Q3 66 + 2,034 | 1,932; 1,949; 2,050; 2,100 |
| Tangible equity, September 30, 2026 | 1,984 - 2,859 - 1,559 | -2,434 |
| Secured debt, September 30, 2026 | ABL 1,950 + Term Loan 744 + AR Facility 550 | 3,244 |
| Rental equipment, net / secured debt | 6,190 / 3,244 | 1.91x |
| Operating lease liabilities | FY2025: 56 + 1,479; Q1: 57 + 1,502; Q2: 57 + 1,491; Q3: 59 + 1,443 | 1,535; 1,559; 1,548; 1,502 |

## Gaps

| Gap | Severity | Affected | Why it matters | Action |
| --- | --- | --- | --- | --- |
| FY2025 and Q4 2025 adjusted EBITDA are Not supplied (no Q4 2025 release; the 10-K has no reconciliation) | Material | Leverage and cover on an adjusted basis; CP-2, CP-5 | No trailing adjusted EBITDA; only unadjusted EBITDA ratios are available. Not calculable | Add the Q4 2025 earnings release |
| Management net leverage (3.90x, 3.95x, 3.96x) relies on pro forma H&E pre-acquisition earnings and adjusted EBITDA that are Not supplied | Material | Cross-check of the ratios above | Cannot reproduce or reconcile the management figure | Add the release pro forma bridge or H&E standalone results |
| ABL springing fixed charge trigger level and the covenant definition are Not supplied | Material | Covenant headroom | Headroom Not calculable | Add the executed ABL credit agreement |
| Maturity schedule exists only at December 31, 2025; it does not state where the AR Facility sits and predates the August 2026 extension | Minor | Maturity chart | 2028 shows 497; the AR Facility (550 now, due August 31, 2027) may belong in 2027 | Add a later schedule or the 10-K for FY2026 |
| Restricted cash is not separately disclosed; liquidity uses the balance sheet cash line | Minor | Liquidity | Unrestricted cash could be lower | None available in pack |
| Pension and lease figures after December 31, 2025 are not updated beyond the balance sheet lines; purchase commitments after December 31, 2025 not disclosed | Minor | Claims outside debt | Debt-like claims may have moved | Add the FY2026 10-K |
| 2025 comparatives for Q1 to Q3 are as presented in 2026 filings; originally filed 2025 quarterlies are not supplied | Minor | LTM windows | A restatement of comparatives, if any, cannot be checked | Add the 2025 10-Qs |
| No credit ratings, quotes or valuation inputs in context | Minor | Relative value | Not a CP-1 input | Supply if needed |

## Next module

Proceed to CP-1A (business and transaction context). It should carry from this handoff: the consolidated perimeter; the H&E acquisition closing on June 2, 2025 and its funding (new senior unsecured notes, term loan and ABL borrowings per the 10-Q business combination note); the one-segment equipment rental model; that leverage is high but falling with earnings growth, that fleet capital intensity and payables-funded equipment purchases absorb cash, and that liquidity relies on the ABL. CP-2 and CP-5 should treat FY2025 adjusted EBITDA, pro forma leverage and covenant triggers as Not supplied, and label every ratio from this handoff as a CP-1 calculation on unadjusted EBITDA.
