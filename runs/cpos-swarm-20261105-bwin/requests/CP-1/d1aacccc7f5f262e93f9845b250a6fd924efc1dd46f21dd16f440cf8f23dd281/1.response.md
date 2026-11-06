## Request

Issuer: Baldwin Insurance Group, Inc. (issuer id bwin; Nasdaq ticker BWIN; Delaware registrant; brand name The Baldwin Group). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. The statements are in thousands of US dollars; chart tables below are in US$m or x as their headings require. Current period named by the context: Q2 2026 (quarter ended 2026-06-30). Prior period: FY2025.

Question for this module: what is the financial base, that is the reported statements, the definitions behind adjusted earnings, the debt and liquidity position and the credit metrics, that the later modules may rely on? Scope: the supplied filings and releases only. No outside knowledge of the company is used. Nothing dated after 2026-07-30 is in the pack and no fact dated after the cutoff is relied on.

The readiness handoff from the earlier module is a supplied handoff. This module follows its carry-forward instructions: the Q2 2026 10-Q controls the 2026-06-30 balance sheet, debt and six-month results; FY2025 figures come from the 10-K; 2025 comparatives exclude the January 2026 acquisitions; the company-stated revolver capacity is not covenant headroom; exact term loan principal is derived from the fair-value table; and the covenant ratio, guarantor map, ratings and later-period events stay open gaps.

The context holds run settings only and is not issuer evidence. Its ratings, quotes, peers, deal terms and assumption fields are empty and are treated as not supplied, never as zero.

## Sources

### Issuer sources relied on

The locator `page:N` is the extraction chunk of the named file, not the printed page. Hashes are the pinned file hashes.

| Source name | sha256 | Use in this module |
| --- | --- | --- |
| 10-K_2025-12-31_bwin-20251231.htm.jsonl | 435ed820e1dedd05dae93bd87717be3ea65acd13ff9cfffaff7aef178e8494c0 | Audited FY2024 and FY2025 statements, debt note, covenant text, Adjusted EBITDA reconciliation, subsequent events |
| 10-Q_2025-09-30_bwin-20250930.htm.jsonl | 0c90579fda7c87633de78b7017eb30aa8347d6e49afceae9c9779736c12ef751 | Reviewed for nine-month 2025 context; no figure in the tables below depends on it |
| 10-Q_2026-03-31_bwin-20260331.htm.jsonl | 5f7ff56cb35eb60658f5417d0bba0ed7cf98e6637612d04f68a150a621f88e2d | Q1 2026 balance sheet, cash flow, debt note and liquidity sentence |
| 10-Q_2026-06-30_bwin-20260630.htm.jsonl | c7872b5a0e467a855aa0647c334b01115eb4a8b78c766a2ae8d6dccc7348e147 | Controlling source for the 2026-06-30 balance sheet, six-month 2026 and 2025 statements, debt, segments, non-GAAP reconciliation and liquidity |
| EX-99.1_2026-02-26_ex991bwinfy2025q4earningsr.htm.jsonl | a080932734c7e6f80d7856122b745700585d5721dda88f2356f627e5082d8b98 | FY2025 and FY2024 adjusted free cash flow, pro forma adjusted EBITDA, Q4 2025 reconciliation |
| EX-99.1_2026-05-04_ex99-1fy2026q1earningsrele.htm.jsonl | e172c6af59bf6e4ced5ad8c6113ef1f6cea50e4c9e4f92d7126f157d6d775038 | Q1 2026 headline results used to test Q2 differences |
| EX-99.1_2026-07-30_ex99-1fy2026q2earningsrele.htm.jsonl | cbd7cabcbf8fcf9cc1502cda8859930cd02f842bc6bfad19f57059a1a93bf562 | Q2 2026 reconciliations and adjusted free cash flow |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 8078b6eb19ff2611ca7e63e8361807aa16e370931c16f21c4255d38d5faaa273 | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 9bfff3ec79f0002a828742fed2ffc0e0ea83352ff5b4551aef0d1e1eea205802 | Source readiness; its carry-forward instructions are followed and its gaps are carried below |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Total debt to adjusted EBITDA rose to 6.30x at 2026-06-30 from 5.01x at FY2025 after the January 2026 term loan add-on, while cash interest cover held near 2.89x. Covenant headroom cannot be measured. | Medium | Adjusted EBITDA is company defined, holds only six months of acquired earnings against full acquisition debt, and no pro forma or covenant figure is supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Leverage on adjusted EBITDA rose from 4.59x at FY2024 to 5.01x at FY2025 and 6.30x for the last twelve months to 2026-06-30. | Debt grew faster than reported adjusted earnings, so the cushion against a covenant or refinancing test is thinner than a year ago. | Medium |
| Adjustments other than interest, amortization and depreciation were 42.5% of FY2025 adjusted EBITDA and 48.6% for the last twelve months. | Reported leverage depends on management's earnings definition; the covenant EBITDA is not supplied, so the gap cannot be sized. | High |
| Undrawn revolver capacity fell to US$259.4m at 2026-06-30 from US$477.0m at FY2025, while cash rose to US$184.5m. | Liquidity is lower than at year end, but the revolver matures 2029-05-24 and the term loans and notes mature in 2031. | High |
| Contingent earnout liabilities of 346,824 thousand, deferred payments of 192,500 thousand and Tax Receivable Agreement liabilities of 144,570 thousand sit outside the debt total. | These are further cash claims that compete with debt service, and part falls due within one year. | High |
| Net cash from operations was 39,486 thousand for six months 2026 against an outflow of 80,704 thousand a year earlier. | The swing reflects lower earnout payments inside operating cash flow, so cash conversion depends on earnout timing. | Medium |

### Financial base view

The financial base supports a bounded reported-fact view of Baldwin Insurance Group, Inc. at the consolidated level, with specific limits. Reported FY2024 and FY2025 statements are audited and consolidated. Six-month 2026 and 2025 statements are unaudited. The base is dominated by the January 2026 acquisitions of CAC Group, Obie and Capstone, which closed against a 600,000 thousand incremental term loan, new equity and new contingent claims. As a result the 2025 comparatives and the FY2025 balance sheet are not like for like with 2026. On the company's adjusted EBITDA definition, total debt to adjusted EBITDA is 4.59x at FY2024, 5.01x at FY2025 and 6.30x on a last-twelve-months basis to 2026-06-30, and net debt to adjusted EBITDA is 4.31x, 4.65x and 5.83x. Cash interest cover on the same earnings is 2.81x, 2.96x and 2.89x. These ratios are calculated here from printed components and are not company-reported credit metrics. Three limits bind every use. First, adjusted EBITDA carries large management addbacks, and EBITDA before addbacks, calculated from the statements, is far lower, so the leverage view depends on which earnings measure a reader accepts. Second, the last-twelve-months earnings include six months of acquired earnings while the 2026-06-30 debt carries the full acquisition financing, and a pro forma adjusted EBITDA for the 2026 acquisitions is not supplied, so the 6.30x is probably overstated relative to a full-year acquired run rate by an amount the pack does not size. Third, the single financial maintenance covenant, a total first lien net leverage test, is described only in the 10-K, with no reported ratio, so headroom is not calculable. Liquidity is stated by the company at the latest date. Debt maturities after the January 2026 add-on are derived here, not printed. No perimeter other than the consolidated group is supplied.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 4.59 | 4.31 | x | Principal debt 1,435,800 thousand at 2024-12-31 (10-K page:181) over company Adjusted EBITDA 312,485 thousand (10-K page:99). Net debt deducts cash and equivalents 90,045 thousand and excludes fiduciary cash. Calculated here; not company-reported or covenant leverage. Excludes earnouts, deferred payments, leases and the Tax Receivable Agreement. |
| FY2025 | 5.01 | 4.65 | x | Principal debt 1,603,606 thousand plus revolver 107,000 thousand at 2025-12-31 (10-K page:165) over Adjusted EBITDA 341,472 thousand (10-K page:99). Cash and equivalents 123,669 thousand. Debt precedes the January 2026 add-on and the EBITDA excludes the January 2026 acquisitions. Calculated here. |
| LTM Q2 2026 | 6.30 | 5.83 | x | Principal debt 2,193,045 thousand plus revolver 302,000 thousand at 2026-06-30 (10-Q Q2 2026 page:38) over last-twelve-months Adjusted EBITDA 396,153 thousand, built as FY2025 plus six months 2026 less six months 2025 (page:61, 10-K page:99). Cash and equivalents 184,499 thousand. Debt carries full acquisition financing but EBITDA holds about six months of acquired earnings; no pro forma figure supplied. Calculated here. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 2.81 | x | Adjusted EBITDA 312,485 thousand over cash paid for interest 111,397 thousand (10-K page:99, page:135). Calculated here. |
| FY2025 | 2.96 | x | Adjusted EBITDA 341,472 thousand over cash paid for interest 115,276 thousand (10-K page:99, page:135). Calculated here. |
| 6M 2025 | 3.66 | x | Adjusted EBITDA 199,307 thousand over cash paid for interest 54,528 thousand (10-Q Q2 2026 page:61, page:10). Six-month period; the notes coupons are paid May 15 and November 15. |
| 6M 2026 | 3.33 | x | Adjusted EBITDA 253,988 thousand over cash paid for interest 76,315 thousand (10-Q Q2 2026 page:61, page:10). Includes acquired earnings from 2026-01-01 and interest on the January 2026 add-on. |
| LTM Q2 2026 | 2.89 | x | Adjusted EBITDA 396,153 thousand over last-twelve-months cash interest 137,063 thousand, built as FY2025 plus six months 2026 less six months 2025. Whether cash paid for interest is net of interest rate swap settlements is not stated. Calculated here. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| 2024-12-31 | 90.0 | 588.0 | US$m | Cash and equivalents 90,045 thousand (10-K page:131), excluding fiduciary cash of 222,724 thousand. Undrawn revolver derived as 600.0 commitments less nil drawn less 12.0 letters of credit (10-K page:162-163). Calculated here. |
| 2025-12-31 | 123.7 | 477.0 | US$m | Cash 123,669 thousand (10-K page:131); company-stated available revolver capacity 477.0 (10-K page:110). Excludes fiduciary cash of 223,228 thousand. |
| 2026-03-31 | 146.4 | 393.0 | US$m | Cash 146,409 thousand (10-Q Q1 2026 page:5); company-stated available capacity (10-Q Q1 2026 page:65). Excludes fiduciary cash. |
| 2026-06-30 | 184.5 | 259.4 | US$m | Cash 184,499 thousand (10-Q Q2 2026 page:5); company-stated available capacity (page:74). Excludes fiduciary cash of 426,189 thousand. Availability is net of letters of credit; any covenant limit on drawing is not supplied. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 (Jul-Dec) | 8.0 | US$m | Derived, not printed: two scheduled Term Loan payments of 4.0 each (10-Q Q2 2026 page:25). Assumes payments continue quarterly at that amount with no excess cash flow or voluntary prepayment. |
| 2027 | 16.0 | US$m | Derived: four scheduled Term Loan payments of 4.0. |
| 2028 | 16.0 | US$m | Derived: four scheduled Term Loan payments of 4.0. |
| 2029 | 318.0 | US$m | Derived: Term Loan payments of 16.0 plus the revolver drawn balance of 302.0 due 2029-05-24 (10-Q Q2 2026 page:25). The revolver may be repaid or redrawn earlier. |
| 2030 | 16.0 | US$m | Derived: four scheduled Term Loan payments of 4.0. |
| 2031 | 2121.0 | US$m | Derived: one Term Loan payment of 4.0, the Term Loan balance at maturity 2031-05-24 of about 1517.0, and the 7.125% Senior Secured Notes of 600.0 due 2031-05-15 (10-Q Q2 2026 page:5). Total across rows equals principal debt plus revolver of 2,495.0 within rounding. |

### Financials and credit metrics

| Metric (US$ thousands unless stated) | FY2024 | FY2025 | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 | LTM Q2 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenues | 1,389,037 | 1,504,884 | 378,811 | 492,939 | 792,216 | 1,025,174 | 1,737,842 |
| Operating income (loss) | 60,648 | 73,936 | 27,940 | (8,343) | 83,957 | (109,609) | (119,630) |
| Interest expense, net (income statement) | 123,644 | 121,428 | 31,320 | 45,666 | 61,296 | 84,566 | 144,698 |
| Net income (loss) | (41,081) | (54,154) | (5,141) | (55,981) | 19,757 | (57,877) | (131,788) |
| Adjusted EBITDA (company definition) | 312,485 | 341,472 | 85,512 | 116,740 | 199,307 | 253,988 | 396,153 |
| Adjusted EBITDA margin, % (company printed; LTM calculated) | 22.5 | 22.7 | 22.6 | 23.7 | 25.2 | 24.8 | 22.8 |
| EBITDA before addbacks (calculated: net income plus interest, income tax, depreciation and amortization) | 193,218 | 196,833 | 54,516 | 48,569 | 136,855 | (1,870) | 58,108 |
| Adjustments other than interest, amortization and depreciation, % of Adjusted EBITDA (calculated) | 38.7 | 42.5 | 37.0 | 58.1 | 31.7 | 43.6 | 48.6 |
| Net cash provided by (used in) operating activities | 51,453 | (29,418) | (16,721) | 45,559 | (80,704) | 39,486 | 90,772 |
| Capital expenditures | 41,049 | 39,527 | 11,377 | 15,184 | 20,310 | 27,848 | 47,065 |
| Operating cash flow less capital expenditures (calculated) | 10,404 | (68,945) | (28,098) | 30,375 | (101,014) | 11,638 | 43,707 |
| Adjusted free cash flow (company definition) | 91,960 | 87,220 | 8,638 | 46,422 | 34,447 | 46,225 | 98,998 |
| Cash paid for interest | 111,397 | 115,276 | 40,741 | 50,001 | 54,528 | 76,315 | 137,063 |
| Cash paid for income taxes | 2,745 | 1,700 | 1,315 | 754 | 1,340 | 759 | 1,119 |
| Cash and cash equivalents, period end | 90,045 | 123,669 | Not supplied | 184,499 | Not supplied | 184,499 | 184,499 |
| Fiduciary cash, period end | 222,724 | 223,228 | Not supplied | 426,189 | Not supplied | 426,189 | 426,189 |
| Principal debt including revolver, period end | 1,435,800 | 1,710,606 | Not supplied | 2,495,045 | Not supplied | 2,495,045 | 2,495,045 |
| Net debt: principal debt less cash and equivalents (calculated) | 1,345,755 | 1,586,937 | Not supplied | 2,310,546 | Not supplied | 2,310,546 | 2,310,546 |
| Contingent earnout liabilities, current plus non-current | 145,559 | 23,293 | Not supplied | 346,824 | Not supplied | 346,824 | 346,824 |
| Tax Receivable Agreement liabilities | No line printed | Nil (printed as a dash) | Not supplied | 144,570 | Not supplied | 144,570 | 144,570 |
| Total debt / Adjusted EBITDA, x (calculated) | 4.59 | 5.01 | Not supplied | Not supplied | Not supplied | Not supplied | 6.30 |
| Net debt / Adjusted EBITDA, x (calculated) | 4.31 | 4.65 | Not supplied | Not supplied | Not supplied | Not supplied | 5.83 |
| Adjusted EBITDA / cash paid for interest, x (calculated) | 2.81 | 2.96 | 2.10 | 2.33 | 3.66 | 3.33 | 2.89 |
| Total debt / EBITDA before addbacks, x (calculated) | 7.43 | 8.69 | Not supplied | Not supplied | Not supplied | Not supplied | 42.94 |

### Source context

| Source | Entity and perimeter | Period and statement kind | Units, currency and version |
| --- | --- | --- | --- |
| 10-K FY2025 | The Baldwin Insurance Group, Inc. and consolidated subsidiaries including The Baldwin Insurance Group Holdings, LLC (structure at 10-Q Q2 2026 page:11; statements at 10-K page:131) | Audited statements for FY2025, FY2024 and FY2023 (page:128, page:132, page:134) | Thousands of USD; original filing; auditor report signed 2026-02-26 (page:131) |
| 10-Q Q2 2026 | Same consolidated perimeter, including the three January 2026 acquisitions from their dates | Unaudited three and six months to 2026-06-30 with 2025 comparatives; balance sheet at 2026-06-30 and 2025-12-31 (page:5-7) | Thousands of USD; controls 2026-06-30 facts |
| 10-Q Q1 2026 | Same | Unaudited three months to 2026-03-31 (page:5-9) | Thousands of USD; used for Q1 cash interest and the 2026-03-31 liquidity |
| 10-Q Q3 2025 | Same, pre acquisition | Unaudited three and nine months to 2025-09-30 | Thousands of USD; background only |
| Three releases | Company announcing; management attribution | Q4 and FY2025, Q1 2026, Q2 2026 | Thousands of USD; supporting claims; the 10-K and 10-Qs control where both state a fact |

All statement scopes use one perimeter: the consolidated group with a noncontrolling interest for LLC Units held outside the parent. No stand-alone financial statements of the borrower, Baldwin Holdings, are supplied.

### Reported income statement, cash flow and balance sheet detail

| Line | FY2024 | FY2025 | 6M 2025 | 6M 2026 | Source |
| --- | --- | --- | --- | --- | --- |
| Commissions and fees | 1,377,116 | 1,493,680 | 786,780 | 1,017,650 | 10-K page:132; 10-Q Q2 2026 page:6 |
| Investment income | 11,921 | 11,204 | 5,436 | 7,524 | same |
| Colleague compensation and benefits | 762,219 | 777,531 | 393,491 | 547,935 | same |
| Outside commissions | 269,829 | 279,711 | 139,409 | 138,477 | same |
| Other operating expenses | 192,366 | 240,282 | 114,138 | 318,221 | same |
| Amortization expense | 102,730 | 121,316 | 51,892 | 111,074 | same |
| Change in fair value of contingent consideration | (4,949) | 5,594 | 6,104 | 14,272 | same |
| Depreciation expense | 6,194 | 6,514 | 3,225 | 4,804 | same |
| Loss on extinguishment and modification of debt | 15,113 | 6,226 | 2,394 | 7,538 | same |
| Income tax expense (benefit) | 1,731 | 1,729 | 685 | (144,437) | same |
| Net loss attributable to noncontrolling interests | (16,563) | (20,341) | 8,982 | (21,223) | same (6M 2025 is income attributable) |
| Share-based compensation (cash flow add-back) | 65,503 | 71,113 | 29,755 | 33,519 | 10-K page:134; 10-Q Q2 2026 page:9 |
| Payment of contingent earnout consideration in excess of purchase price accrual (inside operating cash flow) | (23,395) | (85,784) | (85,090) | (6,739) | same |
| Payment of contingent earnout consideration up to purchase price accrual (inside financing cash flow) | (98,678) | (66,171) | (64,256) | Not supplied: no such line printed for 6M 2026 | same |
| Repurchase of common stock | Not supplied: no such line printed | Not supplied: no such line printed | Not supplied: no such line printed | (126,833) | 10-Q Q2 2026 page:9 |

Other operating expenses for 6M 2026 include 128.8 million of Tax Receivable Agreement expense and 7.7 million of transaction-related insurance premiums (10-Q Q2 2026 page:72).

### Segments

The segment note discloses revenue and net income by operating group; segment adjusted EBITDA is not disclosed (10-Q Q2 2026 page:41). Corporate and Other holds interest expense and unallocated costs.

| Operating group | Q2 2026 revenue | Q2 2025 revenue | Q2 2026 net income (loss) | Q2 2025 net income (loss) | 6M 2026 revenue | 6M 2025 revenue | 6M 2026 net income (loss) | 6M 2025 net income (loss) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Insurance Advisory Solutions | 275,343 | 183,265 | (1,279) | 17,778 | 606,539 | 410,938 | 41,003 | 64,863 |
| Underwriting, Capacity & Technology Solutions | 160,247 | 147,510 | 6,693 | 27,115 | 295,190 | 272,684 | 9,199 | 44,479 |
| Mainstreet Insurance Solutions | 75,327 | 66,564 | 3,764 | 4,223 | 156,985 | 144,433 | 14,586 | 19,157 |
| Corporate and Other | (17,978) | (18,528) | (65,159) | (54,257) | (33,540) | (35,839) | (122,665) | (108,742) |
| Total | 492,939 | 378,811 | (55,981) | (5,141) | 1,025,174 | 792,216 | (57,877) | 19,757 |

Sources: 10-Q Q2 2026 page:41-44. The acquired businesses recognized revenue of 99.9 million and a net loss of 32.4 million for Q2 2026, and 202.1 million and 42.3 million for six months 2026 (page:17).

### Adjusted EBITDA definition review

The company defines adjusted EBITDA as net income (loss) before interest, taxes, depreciation, amortization, change in fair value of contingent consideration and certain items of income and expense, including share-based compensation expense, transaction-related partnership and integration expenses, transformation costs, severance and certain non-recurring items (10-Q Q2 2026 page:58-59). It is a non-GAAP measure management uses; the reconciliation below is transcribed from the filings.

| Reconciling item | FY2024 | FY2025 | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| Net income (loss) | (41,081) | (54,154) | (5,141) | (55,981) | 19,757 | (57,877) |
| Interest expense, net (reconciliation basis) | 123,644 | 122,778 | 31,320 | 46,140 | 61,296 | 85,347 |
| Amortization expense | 102,730 | 121,316 | 26,010 | 56,027 | 51,892 | 111,074 |
| Share-based compensation | 65,503 | 71,113 | 16,952 | 20,701 | 29,755 | 33,519 |
| Transaction-related partnership and integration expenses | 10,501 | 23,051 | 3,985 | 14,695 | 5,518 | 22,868 |
| Transaction closing costs | Not supplied: no such line | Not supplied: no such line | — | — | — | 17,668 |
| Change in fair value of contingent consideration | (4,949) | 5,594 | (1,957) | 12,303 | 6,104 | 14,272 |
| Income and other taxes (includes Tax Receivable Agreement expense) | 7,184 | 4,255 | 1,348 | 1,084 | 2,819 | (13,064) |
| Transformation costs | — | 7,003 | 227 | 6,441 | 772 | 9,500 |
| Loss on extinguishment and modification of debt | 15,113 | 6,226 | — | 129 | 2,394 | 7,538 |
| Severance | 5,756 | 6,790 | 1,618 | 3,874 | 2,825 | 5,689 |
| Depreciation expense | 6,194 | 6,514 | 1,642 | 2,773 | 3,225 | 4,804 |
| Colleague earnout incentives | 41,917 | (1,779) | 1,490 | — | (1,779) | — |
| Impairment of right-of-use assets | — | 1,275 | 1,188 | — | 1,188 | — |
| Loss (gain) on divestitures | (38,953) | (290) | 1,111 | — | (290) | — |
| Loss on interest rate caps | 244 | 18 | Not supplied: no such line | Not supplied: no such line | Not supplied: no such line | Not supplied: no such line |
| Other | 18,682 | 21,762 | 5,719 | 8,554 | 13,831 | 12,650 |
| Adjusted EBITDA | 312,485 | 341,472 | 85,512 | 116,740 | 199,307 | 253,988 |

Sources: 10-K page:99; Q2 release page:11; 10-Q Q2 2026 page:61. Credit-relevant observations follow.

- Share-based compensation is the largest addback other than interest and amortization (71,113 for FY2025).
- "Income and other taxes" includes Tax Receivable Agreement expense, so the 128.8 million of expense recognized in 6M 2026 is added back, while the future payments are a cash obligation of 144,570 (page:81).
- Cash earnout payments are not deducted in adjusted EBITDA. The operating cash flow carries those "in excess of purchase price accrual" (85,784 for FY2025); payments up to the accrual are in financing cash flow.
- A pro forma adjusted EBITDA exists only for FY2025 and FY2024 and adjusts for MultiStrat and Hippo's Homebuilder Distribution Network and for divestitures: 352,505 and 310,888 (Q4 release page:15-16). It does not include CAC Group, Obie or Capstone. No pro forma adjusted EBITDA for the 2026 acquisitions is supplied.
- Pro forma revenue and net loss that include the 2026 acquisitions are supplied for 2025 and 2026 comparisons (10-Q Q2 2026 page:19-20): pro forma revenues 468,120 for Q2 2025 and 956,381 for 6M 2025, with pro forma net loss of (31,136) and (45,824).
- Interest expense in the reconciliation (46,140 for Q2 2026) differs from the income statement (45,666) because interest income on surplus notes is excluded (page:61). The same gap exists at FY2025 (122,778 against 121,428) without a footnote in the 10-K text read.
- The covenant EBITDA ("Consolidated EBITDA" in the credit agreement) is referenced in the 10-K (page:163) but its definition is not supplied. Adjusted EBITDA is not shown to equal it.

### Debt facilities

| Instrument | Obligor | Principal at 2026-06-30 (US$ thousands) | Rate and terms | Maturity | Security and guarantees | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| Term Loans, JPM Credit Facility | The Baldwin Insurance Group Holdings, LLC as borrower | 1,593,045 derived from the fair-value table less the notes; printed as "$1.6 billion" | Term SOFR plus 250 bps; applicable rate 6.13%; quarterly principal payments of $4.0 million; 500,000 notional swapped to a fixed 3.244% through 2028-09-14 | 2031-05-24 | First lien, secured by substantially all assets of Baldwin Holdings and the guarantors; guarantors not named | 10-Q Q2 2026 page:25, page:38, page:73; 10-K page:163 |
| Revolving Facility | Baldwin Holdings | 302,000 drawn of 600,000 commitments; letters of credit 38,600 | Term SOFR plus 10 bps adjustment plus 175 to 250 bps by total first lien net leverage; applicable rate 6.23%; commitment fee 0.40% | 2029-05-24 | Same collateral and guarantors | 10-Q Q2 2026 page:24-25 |
| 7.125% Senior Secured Notes | Baldwin Holdings and a wholly-owned corporate co-issuer (named in the 10-K exhibit list as The Baldwin Insurance Group Holdings Finance, Inc.) | 600,000 | Fixed 7.125%; interest each May 15 and November 15; redeemable from 2027-05-15 at indenture prices; make-whole before then; change of control offer | 2031-05-15 | Guaranteed by the subsidiaries that guarantee the JPM Credit Facility; first lien on the same collateral, pari passu | 10-K page:161-162, page:196 |

Total principal 2,495,045 thousand includes the revolver. The 10-K reconciliation of principal to the balance sheet at 2025-12-31 is 1,603,606 less 24,907 of unamortized discount and costs, equal to 1,578,699 (10-K page:165). At 2026-06-30 the balance sheet shows revolving line of credit 302,000 and long-term debt less current portion 2,150,725, with 16,091 of current portion in accrued expenses (10-Q Q2 2026 page:5, page:23). Estimated fair value of long-term debt was 2,157,201 and of the revolver 298,415 (page:38). A 100 bp rise in SOFR, after the swap, would raise annual interest expense on the JPM Credit Facility by 14.0 million (page:82).

### Debt maturities as printed at 2025-12-31

| Year | Amount (US$ thousands) |
| --- | --- |
| 2026 | 12,577 |
| 2027 | 10,061 |
| 2028 | 10,061 |
| 2029 | 10,061 |
| 2030 | 10,061 |
| Thereafter | 1,550,785 |

Source: 10-K page:165. This is the term loans and notes before the January 2026 add-on and excludes the 107,000 revolver. A principal maturity table at 2026-06-30 is not printed; the contractual obligations table at page:74 of the Q2 10-Q gives debt obligations payable of 3,230,978 including estimated interest, with 174,743 due in less than one year, 646,857 in one to three years and 2,409,378 in three to five years.

### Other claims outside the debt figure

| Claim | Amount at 2026-06-30 (US$ thousands) | Inside or outside the debt figure | Locator |
| --- | --- | --- | --- |
| Contingent earnout liabilities, current 120,901 and non-current 225,923 | 346,824 | Outside; undiscounted expected payments are 410,547, of which 131,069 within one year | 10-Q Q2 2026 page:5, page:74 |
| Maximum potential contingent earnout on the three 2026 acquisitions | 544,855 | Outside; maximum, not expected | 10-Q Q2 2026 page:18 |
| Deferred payments for acquisitions | 192,500 undiscounted, of which 40,833 within one year; non-current portion 129,400 sits in other liabilities | Outside | 10-Q Q2 2026 page:19, page:74 |
| Tax Receivable Agreement liabilities | 144,570 | Outside; an obligation of the parent to LLC members, 85% of realized tax savings | 10-Q Q2 2026 page:5, page:15, page:81 |
| Operating lease liabilities | 97,117 (21,989 current plus 75,128 non-current) | Outside; operating lease payments of 111,701 undiscounted | 10-Q Q2 2026 page:5, page:23, page:74 |
| University of South Florida commitment | 2,496 | Outside | 10-Q Q2 2026 page:74 |
| Share repurchase authorization | 250 million authorized; about 124.5 million remaining | Discretionary; not a liability | 10-Q Q2 2026 page:83 |

Pensions and retiree medical: none found beyond a 401(k) plan with employer matching. Factoring and supply-chain finance: none found. Fiduciary liabilities of 1,208,383 thousand are matched by fiduciary cash and receivables and are not treated as debt (10-Q Q2 2026 page:5).

### Subsequent events and 2026 transaction narrative

- January 2026 acquisitions. CAC Group (effective 2026-01-01), Obie and Capstone (effective 2026-01-02) cost 1,559,612 thousand in total consideration: cash 567,889, contingent earnouts at fair value 315,998, equity 510,561 and deferred payments 165,164. Goodwill of 1,134,895 and intangibles of 550,983 were recognized, and the purchase accounting is provisional (10-Q Q2 2026 page:16-19).
- Amendment No. 4. On 2026-01-02 the JPM Credit Agreement added 600,000 of incremental term loans, with about 12.0 million of debt issuance costs (10-K page:189; 10-Q Q2 2026 page:25).
- Deferred payment. A 25.0 million deferred payment to a partner was settled on 2026-01-02 (10-K page:189).
- Tax items. A partial valuation allowance release drove an income tax benefit of 144,437 for six months 2026, and Tax Receivable Agreement liabilities were recognized for the first time as probable (10-Q Q2 2026 page:30, page:72, page:81).
- Share repurchases. 126,833 was spent on repurchases in six months 2026, including 3,839,937 shares in Q2 (10-Q Q2 2026 page:9, page:83).
- Media Guarantors. A plan to sell this subsidiary was committed in Q2 2026 and a definitive agreement was signed on 2026-07-02 for 4.0 million cash, with the held-for-sale assets of 5.0 million and liabilities of 3.6 million immaterial (10-Q Q2 2026 page:46-47).
- No event dated after 2026-07-30 is in the pack. Events to the cutoff are Not supplied.

### Narrative findings

Each finding runs from evidence to risk mechanism to creditor implication.

- Leverage and the earnings measure. Evidence: calculated total debt to adjusted EBITDA is 6.30x for the last twelve months to 2026-06-30 against 5.01x at FY2025, and adjustments other than interest, amortization and depreciation were 48.6% of last-twelve-months adjusted EBITDA. Risk mechanism: the acquisition debt is fully in the numerator while only six months of acquired earnings is in the denominator, and management addbacks are a large share of the earnings, so the ratio can move materially with the covenant definition. Creditor implication: the first lien covenant at 7.00x (10-K page:164) cannot be tested from the pack, and the adjusted figure should not be read as covenant headroom.
- Interest burden. Evidence: net interest expense of 144,698 for the last twelve months and cash interest cover of 2.89x. Risk mechanism: the Term Loans and revolver are floating, with a 500,000 swap to a fixed 3.244% covering part of the exposure, and the notes at 7.125% pay semi-annually, so quarterly cover is seasonal (2.10x in Q2 2025 and 2.33x in Q2 2026, both quarters containing the May coupon). Creditor implication: the six-month trend in cover fell from 3.66x to 3.33x as interest rose faster than adjusted earnings; the 100 bp sensitivity is 14.0 million a year.
- Liquidity. Evidence: cash of 184.5 million and undrawn capacity of 259.4 million at 2026-06-30, against 123.7 million and 477.0 million at 2025-12-31. Risk mechanism: revolver drawings rose by a net 195,000 in six months while cash paid for repurchases and acquisition-related payments was large. Creditor implication: liquidity remains sizeable against near-term scheduled debt service, but the buffer fell and sits ahead of a 2029 revolver maturity and 346,824 of earnout liabilities.
- Claims outside debt. Evidence: earnouts of 346,824, deferred payments of 192,500 undiscounted and Tax Receivable Agreement liabilities of 144,570. Risk mechanism: these are contractual or probable cash outflows that compete with debt service, and the earnouts are at fair value with a maximum for the 2026 deals of 544,855. Creditor implication: debt-only leverage understates fixed and contingent cash claims; downstream work must show them separately.
- Cash conversion. Evidence: net cash from operations of 39,486 for six months 2026 and an outflow of 80,704 for six months 2025, with earnout payments in excess of the accrual of 6,739 and 85,090. Risk mechanism: most of the swing is lower earnout payments and no colleague earnout incentive payments inside operating cash flow (31,824 in 6M 2025), so cash flow before earnouts is a better indicator of conversion. Creditor implication: adjusted free cash flow of 46,225 is the company's definition and adds back earnout payments; it should not be mistaken for free cash flow after all acquisition-related payments.
- Comparability. Evidence: acquired businesses added revenue of 202.1 million in six months 2026 while organic revenue growth was 2% (10-Q Q2 2026 page:17, page:60). Risk mechanism: the reported 29% revenue growth for six months mostly reflects acquisitions. Creditor implication: use organic and pro forma measures to judge underlying trend.

### Readiness for downstream modules

| Consumer | Requirement | Status | Evidence and limitation |
| --- | --- | --- | --- |
| CP-1A | Business and transaction facts from this base | limited | Acquisition consideration, financing and segments are present; acquisition agreements and ownership map are not supplied |
| CP-2 | Financial risk and liquidity inputs | limited | Leverage, cover and liquidity are calculated; covenant ratio, pro forma 2026 adjusted EBITDA and ratings are not supplied |
| CP-5 | Traceable figures | limited | Every reported figure carries a page locator; calculated figures are labelled with their inputs in the section below |

### Evidence quality and confidence

- Directly Sourced: statement lines, reconciliation lines, company-stated liquidity, debt terms and the covenant text, each with a page locator.
- Calculated: LTM figures, ratios, net debt, EBITDA before addbacks, CFO less capex, Q2 cash flow and interest by difference, undrawn capacity at 2024-12-31 and the debt maturity rows. Inputs are in the next section.
- Analyst Inference: the statement that the 6.30x is overstated relative to a full-year acquired run rate; the inference rests on the stated acquisition dates and the absence of a pro forma EBITDA.
- Insufficient Information: covenant ratio, covenant EBITDA definition, segment adjusted EBITDA, ratings and the debt maturity table at 2026-06-30.

## Calculations

All inputs are US$ thousands unless stated, taken from the cited pages. LTM means FY2025 plus 6M 2026 less 6M 2025.

| Calculation | Inputs and locator | Result |
| --- | --- | --- |
| LTM revenue | 1,504,884 + 1,025,174 - 792,216 (10-K page:132; 10-Q Q2 2026 page:7) | 1,737,842 |
| LTM operating income (loss) | 73,936 + (109,609) - 83,957 | (119,630) |
| LTM interest expense, net | 121,428 + 84,566 - 61,296 | 144,698 |
| LTM net income (loss) | (54,154) + (57,877) - 19,757 | (131,788) |
| LTM Adjusted EBITDA | 341,472 + 253,988 - 199,307 (10-K page:99; 10-Q Q2 2026 page:61) | 396,153 |
| Q1 2026 Adjusted EBITDA by difference | 253,988 - 116,740 (10-Q Q2 2026 page:61) | 137,248, equal to the Q1 release's 137.2 million (Q1 release page:1) |
| LTM Adjusted EBITDA margin | 396,153 / 1,737,842 | 22.8% |
| Q2 2026 depreciation and amortization | 115,878 - 57,078 (10-Q Q2 2026 page:9; 10-Q Q1 2026 page:8) | 58,800, equal to segment total 58,800 (page:42) |
| Q2 2025 depreciation and amortization | 55,117 - 27,465 | 27,652, equal to the segment total 27,652 (page:42) |
| LTM depreciation and amortization | 127,830 + 115,878 - 55,117 | 188,591 |
| EBITDA before addbacks, FY2025 | (54,154) + 121,428 + 1,729 + 127,830 | 196,833 |
| EBITDA before addbacks, FY2024 | (41,081) + 123,644 + 1,731 + 108,924 | 193,218 |
| EBITDA before addbacks, 6M 2026 | (57,877) + 84,566 + (144,437) + 115,878 | (1,870) |
| EBITDA before addbacks, LTM | (131,788) + 144,698 + (143,393) + 188,591, where LTM income tax is 1,729 + (144,437) - 685 = (143,393) | 58,108 |
| Adjustments other than interest, amortization and depreciation, FY2025 | 341,472 - ((54,154) + 122,778 + 121,316 + 6,514) = 341,472 - 196,454 | 145,018, which is 42.5% of 341,472 |
| Same, LTM | 396,153 - ((131,788) + 146,829 + 180,498 + 8,093) where each LTM reconciliation item is FY2025 plus 6M 2026 less 6M 2025 | 192,521, which is 48.6% of 396,153 |
| Reconciliation ties | Net income plus all listed items equals printed Adjusted EBITDA for FY2024, FY2025, Q2 2025, Q2 2026, 6M 2025 and 6M 2026 | Each equals the printed total |
| Q2 2026 operating cash flow | 39,486 - (6,073) (10-Q Q2 2026 page:9; 10-Q Q1 2026 page:8) | 45,559, equal to the Q2 release |
| Q2 2025 operating cash flow | (80,704) - (63,983) | (16,721), equal to the Q2 release |
| LTM operating cash flow | (29,418) + 39,486 - (80,704) | 90,772 |
| Q2 2026 capital expenditures | 27,848 - 12,664 | 15,184 |
| Q2 2025 capital expenditures | 20,310 - 8,933 | 11,377 |
| LTM capital expenditures | 39,527 + 27,848 - 20,310 | 47,065 |
| Operating cash flow less capital expenditures | FY2024 51,453 - 41,049; FY2025 (29,418) - 39,527; Q2 2025 (16,721) - 11,377; Q2 2026 45,559 - 15,184; 6M 2025 (80,704) - 20,310; 6M 2026 39,486 - 27,848; LTM 90,772 - 47,065 | 10,404; (68,945); (28,098); 30,375; (101,014); 11,638; 43,707 |
| Q2 2026 cash interest | 76,315 - 26,314 (10-Q Q2 2026 page:10; 10-Q Q1 2026 page:9) | 50,001 |
| Q2 2025 cash interest | 54,528 - 13,787 | 40,741 |
| LTM cash interest | 115,276 + 76,315 - 54,528 | 137,063 |
| Q2 cash taxes | 759 - 5 (2026); 1,340 - 25 (2025) | 754; 1,315 |
| LTM cash taxes | 1,700 + 759 - 1,340 | 1,119 |
| LTM adjusted free cash flow | 87,220 + 46,225 - 34,447 (Q4 release page:16; Q2 release page:13) | 98,998 |
| Principal debt including revolver | FY2024: 1,435,800 + nil; FY2025: 1,603,606 + 107,000 = 1,710,606; 2026-06-30: 2,193,045 + 302,000 = 2,495,045 (10-K page:181; 10-Q Q2 2026 page:38) | 1,435,800; 1,710,606; 2,495,045 |
| Net debt | 1,435,800 - 90,045; 1,710,606 - 123,669; 2,495,045 - 184,499 | 1,345,755; 1,586,937; 2,310,546 |
| Total debt / Adjusted EBITDA | 1,435,800 / 312,485; 1,710,606 / 341,472; 2,495,045 / 396,153 | 4.59x; 5.01x; 6.30x |
| Net debt / Adjusted EBITDA | 1,345,755 / 312,485; 1,586,937 / 341,472; 2,310,546 / 396,153 | 4.31x; 4.65x; 5.83x |
| Adjusted EBITDA / cash interest | 312,485 / 111,397; 341,472 / 115,276; 199,307 / 54,528; 253,988 / 76,315; 396,153 / 137,063; 85,512 / 40,741; 116,740 / 50,001 | 2.81x; 2.96x; 3.66x; 3.33x; 2.89x; 2.10x; 2.33x |
| Total debt / EBITDA before addbacks | 1,435,800 / 193,218; 1,710,606 / 196,833; 2,495,045 / 58,108 | 7.43x; 8.69x; 42.94x. The LTM figure is depressed by the 128.8 million of Tax Receivable Agreement expense recognized in 6M 2026 and is not meaningful as a credit measure |
| Undrawn revolver, 2024-12-31 | 600.0 - nil - 12.0 (10-K page:162-163) | 588.0 |
| Undrawn revolver, three dates | 600.0 - 302.0 - 38.6; 600.0 - 191.0 - 16.0; 600.0 - 107.0 - 16.0 (10-Q Q2 2026 page:25; 10-Q Q1 2026 page:23; 10-K page:165) | 259.4; 393.0; 477.0, each equal to the company's printed figure |
| Implied Term Loan principal at 2026-06-30 | 2,193,045 - 600,000 notes; cross-check 1,003,606 + 600,000 - 10,561 repaid (10-K page:165, page:181; 10-Q Q2 2026 page:9) | 1,593,045 on both routes |
| Gross principal tie to balance sheet | 2,150,725 + 16,091 = 2,166,816; 2,193,045 - 2,166,816 | 26,229, consistent with the printed 26.2 million of unamortized costs (page:38) |
| Debt maturity rows | Term Loan 1,593,045 less 8,000, four years of 16,000 and 4,000 = 1,517,045 at maturity; 2029 includes revolver 302,000; 2031 includes notes 600,000 | 8.0; 16.0; 16.0; 318.0; 16.0; 2121.0 (US$m), summing to 2,495.0 |
| Current portion tie | Four payments of 4.0 within twelve months against 16,091 printed current portion (page:23) | 16.0 against 16.091, consistent |
| Six-month 2026 cash flow tie | 39,486 + 600,000 + 371,000 - 176,000 - 447,503 - 27,848 - 25,000 - 12,052 - 8,465 - 126,833 - 10,561 - 4,040 - 7,361 + 98,968 (10-Q Q2 2026 page:9) | 263,791, equal to the printed net increase |
| Unrestricted cash tie | 263,791 net increase less fiduciary cash change (426,189 - 223,228 = 202,961) | 60,830, equal to 184,499 - 123,669 |
| Gross cash consideration | 447,503 + 16,393 + 103,993 (cash and fiduciary cash acquired; 10-Q Q2 2026 page:9, page:18) | 567,889, equal to the printed cash consideration |
| Segment ties | Q2 2026 segment revenue 275,343 + 160,247 + 75,327 - 17,978; segment net income (1,279) + 6,693 + 3,764 - 65,159 (page:41-42); the same ties for Q2 2025, 6M 2026 and 6M 2025 (page:42-44) | 492,939 and (55,981); the other periods equal their consolidated totals |
| Interest definition gap | Q2 46,140 - 45,666; 6M 85,347 - 84,566; FY2025 122,778 - 121,428 | 474; 781; 1,350 |
| Earnouts, current plus non-current | 142,949 + 2,610; 9,004 + 14,289; 120,901 + 225,923 (10-K page:131; 10-Q Q2 2026 page:5) | 145,559; 23,293; 346,824 |
| Lease liabilities | 21,989 + 75,128 | 97,117 |
| Fiduciary balance tie, 2026-06-30 | 426,189 + 782,194 against 1,208,383 (10-Q Q2 2026 page:5) | 1,208,383, equal to fiduciary liabilities |
| Balance sheet debt tie, 2025-12-31 | 1,566,122 + 12,577 (10-K page:131, page:165) | 1,578,699, equal to net long-term debt |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Covenant ratio, covenant EBITDA definition and the conditions of the 7.00x test are not supplied; searched covenant and leverage ratio across all seven sources; headroom not calculable | High | CP-2, CP-5 | Obtain the executed JPM Credit Agreement or a compliance disclosure |
| Pro forma adjusted EBITDA for the January 2026 acquisitions is not supplied; the last-twelve-months ratios mix six months of acquired earnings with full acquisition debt | High | CP-2 | Obtain management pro forma EBITDA or the acquisition run-rate; keep the calculated ratios labelled |
| Principal maturity table at 2026-06-30 not printed; rows are derived from the 4.0 quarterly amortization and stated maturities; the Q1 2026 note states the 4.0 payment for the incremental loans and the Q2 2026 note states it for all Term Loans | Medium | CP-1A, CP-2 | Confirm the schedule from the credit agreement; rows may shift with excess cash flow payments |
| Segment adjusted EBITDA not disclosed; segment net income only | Medium | CP-2 | Treat segment cash earnings as not supplied |
| Balance sheet items at 2025-06-30 and 2025-03-31 are not in the pack, so Q2 2025 balance and ratio cells are Not supplied | Low | CP-2 | None needed for the current view |
| Cash paid for interest is not stated net or gross of swap settlements | Low | CP-2 | Confirm in a later filing |
| Guarantors and the co-issuer's role beyond its name are not detailed; no stand-alone borrower statements | Medium | CP-1A, CP-2 | Obtain Exhibit 21.1 and indenture |
| Purchase price accounting for CAC Group and Obie is provisional, so goodwill, intangibles, deferred taxes and earnout fair values may change | Medium | CP-2 | Recheck at the next filing |
| Timing of Tax Receivable Agreement payments and the cash settlement dates of earnouts beyond the contractual table are not supplied | Medium | CP-2 | Obtain schedule if available |
| Ratings, market quotes and valuation inputs are blank in the context | Medium | CP-2 | Supply if wanted |
| No report for the quarter ended 2026-09-30 and nothing dated after 2026-07-30 | Medium | CP-1A, CP-2 | Supply later filings if they exist before the cutoff |
| Management guidance has no GAAP reconciliation (Q2 release page:11) and is not used | Low | CP-2 | None |

## Next module

Proceed to CP-1A. Carry these instructions forward: use the Q2 2026 10-Q for 2026-06-30 and six-month figures and the 10-K for FY2025; label 2025 comparatives and FY2025 as excluding the January 2026 acquisitions; use the calculated ratios of 4.59x, 5.01x and 6.30x for total debt to adjusted EBITDA and 2.81x, 2.96x and 2.89x for cash interest cover only with their stated basis and the six-month acquired-earnings limit; do not describe the company-stated revolver capacity of US$259.4m as covenant headroom; keep earnouts, deferred payments and Tax Receivable Agreement liabilities visible as claims outside debt; describe the Term Loan principal of 1,593,045 as derived; and keep the covenant ratio, guarantor map, ratings and later-period events as open gaps.
