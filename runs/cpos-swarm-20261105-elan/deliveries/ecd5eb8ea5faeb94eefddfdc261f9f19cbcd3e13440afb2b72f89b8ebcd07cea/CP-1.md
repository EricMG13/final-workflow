## Request

Issuer: Elanco Animal Health Inc (registrant name on filings: Elanco Animal Health Incorporated; issuer id elan; NYSE: ELAN). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, statements in millions (Q2 10-Q page:6). Current period named by the context: Q2 2026 (quarter and six months ended 2026-06-30). Prior period: FY2025.

Question for this module: build the financial base for the credit snapshot from the pinned filings and releases. That means reported statements, discrete and trailing periods, the Adjusted EBITDA bridge, debt and maturity structure, liquidity, cash flow quality, interest and leverage ratios, and the covenant picture, each labelled by period and perimeter. It uses the readiness handoff (CP-0) and carries its limitations. Locator abbreviations: 10-K is the FY2025 annual report; Q3-25 10-Q, Q1 10-Q and Q2 10-Q are the quarterly reports for the quarters ended 2025-09-30, 2026-03-31 and 2026-06-30; Feb release, May release and Aug release are the earnings release exhibits dated 2026-02-24, 2026-05-06 and 2026-08-05. `page:N` is the extraction chunk, not the printed page. The context holds no ratings, quotes, deal terms or assumptions; blanks are not zero.

## Sources

### Issuer sources relied on

| Source name | sha256 | Use in this module |
| --- | --- | --- |
| 10-K_2025-12-31_elan-20251231.htm.jsonl | 631f12506b56aa385a6cb05350b491f6e4807480f3dfa124f622742afde4eb4d | Audited FY2025 and FY2024 statements (page:92-94), debt note (page:107-112), leases (page:119-121), pensions (page:133), taxes (page:126-127) |
| 10-Q_2025-09-30_elan-20250930.htm.jsonl | 7696222aac33b3c5724420ded155220803d97cf7ef1e18a5f318f74a02a9f48b | Discrete Q3 2025 statements (page:6) |
| 10-Q_2026-03-31_elan-20260331.htm.jsonl | 8e89da9cffbcecbe1eed4ffa4c7a49caeeccf8b4ba6b25abfd3550722e65c68a | Q1 2026 cash flow and debt table (page:7, page:11) |
| 10-Q_2026-06-30_elan-20260630.htm.jsonl | c53b62a714e3fe245be0c34b9cfa53c27b751637f6f9ab0c69e1814c10ec5ae4 | Latest statements (page:6-8), debt (page:12), hedges (page:13-14), fair value (page:15), liability for sale of future revenue (page:17), liquidity (page:36) |
| EX-99.1_2026-02-24_elanco-12312025exhibit991.htm.jsonl | 1f19620e2ed3f724fb36ed2529d45e324cf0c5eb195eeb5f344974991a2cc3a7 | FY2025 and Q4 2025 non-GAAP reconciliations (page:13-19) |
| EX-99.1_2026-05-06_elanco-20260331exhibit991.htm.jsonl | 4e76217e501306dbc17cfb4f968ce0b23feddf7680c305268cc02ac6e80dcede | Q1 2026 Adjusted EBITDA, net leverage and reconciliation (page:1, page:4, page:14) |
| EX-99.1_2026-08-05_elanco-20260630exhibit991.htm.jsonl | b942651707926f126b37ca482f9fd9191b045d925b308278420efd4d0def6d7f | Q2 and six-month 2026 reconciliations, net debt bridge, trailing Adjusted EBITDA (page:11-14), guidance (page:1, page:4-5) |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | f7c64d35ea0396669fb4a13a10eedb17c6d4612678c62234d77a0ad21bc4c259 | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | How it is used |
| --- | --- | --- |
| CP-0 | 8ffd0a3ea4b4fadd946c35793403822f340da652db0c5ccd908ec080b837b7c5 | Readiness and limitations: latest balance sheet at 2026-06-30, Adjusted EBITDA only in releases, covenant ratios and guarantors not supplied, depreciation and amortization difference, FY-only cash interest and taxes. Each is checked below against the sources; one correction is stated in Handoff consumption |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Trailing Adjusted EBITDA of 1,008 against total debt of 3,944 including the finance lease gives 3.91x, versus management's 3.1x net measure. Liquidity of 1,445 and no large maturity before 2028 support the base. | Medium | Adjusted EBITDA is a management measure; trailing cash interest and achieved covenant ratios are not supplied; the latest balance sheet is June 30, 2026. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Total debt including the finance lease fell from 4.49x Adjusted EBITDA at December 31, 2025 to 3.91x at June 30, 2026. | Most of the improvement came from higher trailing Adjusted EBITDA rather than debt paydown. | High |
| Adjusted EBITDA includes net add-backs of 236 over the trailing twelve months, mainly restructuring and impairment charges that are partly cash. | Cash costs sit outside the headline measure, so cash flow should be tested alongside it. | Medium |
| Cash interest paid was 206 in FY2025, a cover of 4.37x Adjusted EBITDA; trailing 2026 cash interest is not supplied. | Interest cover is known only for the annual base. | Medium |
| Scheduled maturities are 63 in 2026 and 63 in 2027, then 1,236 in 2028 when the senior notes, a term facility and the securitization facility fall due. | 2028 is the refinancing event; liquidity covers the nearer years. | High |
| Hedges of 2,300 notional mature in August 2026 against forward-starting hedges of 1,450, so unhedged floating-rate debt rises on the pack's figures. | Interest cost becomes more rate-sensitive after the balance sheet date; the pack does not show later hedging. | Medium |

### Financial base view

The financial base is usable for a credit snapshot, with the limits stated below. Elanco Animal Health Incorporated reports one consolidated perimeter and one segment, so every figure is group level. Revenue was 4,715 in FY2025 and 2,739 in the six months to 2026-06-30, up from 2,434 a year earlier; the trailing twelve month figure is 5,020. Reported net income was a loss of 232 in FY2025 because the fourth quarter carried 202 of impairment and restructuring charges; the trailing twelve month reported result is still a loss of 199, while six-month 2026 net income is 111. Adjusted EBITDA, which management defines and the filed statements do not print, was 901 in FY2025 and is printed as 1,008 for the trailing twelve months at 2026-06-30 (1,009 when rebuilt from the components, a rounding difference). Reported EBITDA from the same reconciliation is 773 on a trailing basis, so the net add-backs are 236.

Leverage depends on the definition. Management's net leverage, which deducts cash and the finance lease from gross debt, is 3.6x at 2025-12-31 and 3.1x at 2026-06-30. On a basis that keeps the 255 headquarters finance lease in debt and deducts only cash, net debt is 3,414 and net leverage 3.39x at 2026-06-30, and total debt leverage is 3.91x. On reported EBITDA, which still includes royalty revenue that is no longer received in cash, total debt leverage is 5.10x. Both bases are shown in the charts and the table because the choice moves the answer by nearly two turns between the lowest basis (3.13x, the company's) and the highest (5.10x, reported EBITDA).

Debt is bank term loans, a securitization facility and 750 of senior notes due 2028. Required principal payments are small until 2028, when 1,236 falls due, and 1,860 falls due in 2031 and later. Liquidity at 2026-06-30 is 530 of cash plus about 750 of undrawn revolver and about 165 of undrawn securitization capacity, 1,445 in total, and no facility matures before June 2028, when the securitization facility falls due. Operating cash flow was 290 in the six months, and operating cash flow less net purchases of property, equipment and software was 206. The main watch items are the dependence of Adjusted EBITDA on add-backs that include cash restructuring, the August 2026 roll-off of 2,300 of interest rate swaps, the debt-like claims outside the debt table (the 315 liability for sale of future revenue, the headquarters lease purchase option and acquisition payments) and the absence of any figure after 2026-08-05. Adjusted EBITDA, net leverage and guidance are management claims; the filed statements control every other figure.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2024 | 4.78 | 4.26 | x | Debt at 2024-12-31: borrowings 4,349 before issuance costs, no finance lease, cash 468 (10-K page:93, page:108). EBITDA is Adjusted EBITDA 910 (Feb release page:18), management non-GAAP; includes the aqua business to 2024-07-09. Company-defined net leverage for this date is not supplied |
| FY2025 | 4.49 | 3.88 | x | Debt at 2025-12-31 is gross debt 4,045 including the 255 finance lease; cash 545; Adjusted EBITDA 901 (Feb release page:18-19). Net debt here deducts cash only, so it is 3,500. The company's own net leverage, which also deducts the finance lease, is 3.6x |
| LTM Q2 2026 | 3.91 | 3.39 | x | Debt at 2026-06-30 is gross debt 3,944 including the 255 finance lease; cash 530; trailing Adjusted EBITDA 1,008 as printed (Aug release page:14). Net debt here is 3,414. The company's own net leverage, deducting the finance lease too, is 3.1x. Adjusted EBITDA is a management measure that excludes covenant adjustments |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2024 | 3.07 | x | Adjusted EBITDA 910 over cash interest paid 296 (10-K page:112), excluding the interest component of finance lease payments and net of 31 of cash interest received on net investment hedges; no finance lease existed at that date |
| FY2025 | 4.37 | x | Adjusted EBITDA 901 over cash interest paid 206 (10-K page:112), net of 43 received on net investment hedges; before that receipt the cover would be 3.62x on 249 |
| LTM Q2 2026 | Not supplied: six-month 2026 and six-month 2025 cash interest paid are not printed in the 2026 10-Qs or releases | x | Cash basis not calculable for the trailing period. For reference only, trailing Adjusted EBITDA 1,008 over trailing reported net interest expense of 248 is 4.06x, an income statement basis that includes non-cash imputed interest of 29 in six months 2026 |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| 2025-12-31 | 545 | 870 | US$m | Undrawn is about 750 revolver plus about 120 securitization capacity (10-K page:82). The securitization amount moves with the U.S. receivables borrowing base, so it is not a fixed commitment. No letters of credit against the revolver are printed |
| 2026-06-30 | 530 | 915 | US$m | Undrawn is about 750 revolver plus about 165 securitization capacity (Q2 10-Q page:36). Same borrowing base caveat. A significant part of cash is held outside the U.S. (page:36); the split is not supplied |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| 2026 | 63 | US$m | Required principal payments at 2025-12-31 (10-K page:111); excludes finance lease payments. Six months of 2026 repayments of 89 have already been made (Q2 10-Q page:8), so the remaining 2026 amount is not supplied |
| 2027 | 63 | US$m | Same schedule; Q2 10-Q gives no updated schedule |
| 2028 | 1236 | US$m | Same schedule; the Senior Notes due 2028 (750), the Incremental Term Facility due 2028 and the securitization facility (June 2028) fall in this year; the table is not split by facility |
| 2029 | 548 | US$m | Same schedule; includes the April 2029 final payments of the Euro Term Loan due 2029 and the Incremental Term Facility due 2029 |
| 2030 | 20 | US$m | Same schedule. Separately, finance lease payments of 259 fall in 2030, including the 250 headquarters purchase option, outside this figure (10-K page:121) |
| 2031 and thereafter | 1860 | US$m | Same schedule; includes the term loans due 2031 and 2032; the 3,790 total is before 28 of unamortized issuance costs |

### Financials and credit metrics

Reporting unit US$m unless stated. LTM is the trailing twelve months to 2026-06-30, calculated as FY2025 plus six months 2026 less six months 2025. For balance sheet rows the columns are the balance sheet dates 2024-12-31, 2025-12-31, 2025-06-30 and 2026-06-30, and the LTM column repeats 2026-06-30.

| Metric | FY2024 | FY2025 | 6M 2025 | 6M 2026 | LTM Q2 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- |
| Revenue | 4,439 | 4,715 | 2,434 | 2,739 | 5,020 | Reported; 10-K page:92, Q2 10-Q page:6; LTM calculated |
| Gross profit | 2,436 | 2,593 | 1,397 | 1,583 | 2,779 | Reported; same pages; LTM calculated |
| Gross margin (percent of revenue) | 54.9% | 55.0% | 57.4% | 57.8% | 55.4% | Calculated from the two rows above |
| Marketing, selling and administrative | 1,314 | 1,430 | 741 | 830 | 1,519 | Reported; LTM calculated |
| Amortization of intangible assets | 527 | 543 | 264 | 277 | 556 | Reported; LTM calculated |
| Asset impairment, restructuring and other special charges | 150 | 237 | 10 | 25 | 252 | Reported; LTM calculated |
| Interest expense, net of capitalized interest | 235 | 220 | 88 | 116 | 248 | Reported; includes imputed interest on the liability for sale of future revenue of 33 in FY2025 and 29 in 6M 2026 (10-K page:94; Q2 10-Q page:34) |
| Income tax expense | 150 | 8 | 7 | 32 | 33 | Reported; LTM calculated |
| Net income (loss) | 338 | (232) | 78 | 111 | (199) | Reported; FY2024 includes a gain on divestiture of 640 (10-K page:92); LTM calculated |
| Depreciation and amortization (EBITDA reconciliation) | 662 | 680 | 330 | 341 | 691 | Feb release page:18, Aug release page:14; cash flow statement shows 343 for 6M 2026 |
| EBITDA, reported reconciliation | 1,385 | 676 | 503 | 600 | 773 | Feb release page:18, Aug release page:14; LTM calculated |
| Adjusted EBITDA (management non-GAAP) | 910 | 901 | 514 | 622 | 1,008 | Feb release page:18; Aug release page:14; LTM as printed, 1,009 when rebuilt |
| Adjusted EBITDA margin | 20.5% | 19.2% | 21.2% | 22.9% | 20.2% | FY and 6M as printed; LTM calculated on revenue less sold royalty of 33 |
| Cash from operating activities | 541 | 560 | 233 | 290 | 617 | Reported cash flow; 10-K page:94; Q2 10-Q page:7; LTM calculated |
| Net purchases of property and equipment and software | (147) | (276) | (122) | (84) | (238) | Reported cash flow; LTM calculated |
| Operating cash flow less net purchases (analyst definition) | 394 | 284 | 111 | 206 | 379 | Calculated; not the company's free cash flow; operating cash flow is after cash interest and taxes |
| Cash interest paid | 296 | 206 | Not supplied | Not supplied | Not supplied | 10-K page:112; no six-month figure in the 2026 10-Qs |
| Cash income taxes paid, net | 140 | 225 | Not supplied | Not supplied | Not supplied | 10-K page:126-127; FY2025 includes payments on the 2024 aqua gain |
| Cash and cash equivalents (balance) | 468 | 545 | 539 | 530 | 530 | 10-K page:93; Q2 10-Q page:6, page:8 |
| Borrowings before issuance costs, excluding finance lease (balance) | 4,349 | 3,790 | Not supplied | 3,689 | 3,689 | 10-K page:108; Q2 10-Q page:12; 2025-06-30 balance sheet not in the pack |
| Finance lease liability (balance) | Not supplied: printed as a dash, no lease | 255 | Not supplied | 255 | 255 | 10-K page:108; Q2 10-Q page:12 |
| Total debt including finance lease (balance) | 4,349 | 4,045 | Not supplied | 3,944 | 3,944 | Calculated; FY2025 and 6M 2026 match the company's gross debt (Feb release page:19; Aug release page:14) |
| Net debt, company definition (balance) | Not supplied | 3,245 | Not supplied | 3,159 | 3,159 | Gross debt less cash and finance lease; Feb release page:19; Aug release page:14 |
| Net debt including finance lease (balance) | 3,881 | 3,500 | Not supplied | 3,414 | 3,414 | Calculated: total debt including finance lease less cash |
| Total debt including lease / Adjusted EBITDA | 4.78x | 4.49x | Not calculable: half-year EBITDA | Not calculable: half-year EBITDA | 3.91x | Calculated; see chart |
| Net debt including lease / Adjusted EBITDA | 4.26x | 3.88x | Not calculable: half-year EBITDA | Not calculable: half-year EBITDA | 3.39x | Calculated; see chart |
| Net leverage as reported by the company | Not supplied | 3.6x | Not supplied | 3.1x | 3.1x | Feb release page:19; Aug release page:14; excludes covenant adjustments; 3.5x at 2026-03-31 (May release page:4) |
| Total debt including lease / reported EBITDA | 3.14x | 5.98x | Not calculable: half-year EBITDA | Not calculable: half-year EBITDA | 5.10x | Calculated; FY2024 EBITDA includes the 640 divestiture gain, so 3.14x is not comparable |
| Adjusted EBITDA / reported net interest expense | 3.87x | 4.10x | 5.84x | 5.36x | 4.06x | Calculated; income statement basis, not cash |
| Adjusted EBITDA / cash interest paid | 3.07x | 4.37x | Not supplied | Not supplied | Not supplied | Calculated; see interest cover chart |
| Total equity (balance) | 6,096 | 6,547 | 6,775 | 6,588 | 6,588 | 10-K page:93; Q2 10-Q page:7 |
| Goodwill plus other intangibles (balance) | 8,095 | 8,187 | Not supplied | 8,049 | 8,049 | 10-K page:93; Q2 10-Q page:6; exceeds total equity at each date supplied |

### Discrete quarters

Only the quarters the pack supports are shown. Q3 2025 Adjusted EBITDA is derived because no release for that quarter is in the pack.

| Quarter | Revenue | Gross profit | Net income (loss) | Adjusted EBITDA | Net leverage reported | Locator and basis |
| --- | --- | --- | --- | --- | --- | --- |
| Q3 2025 | 1,137 | 607 | (34) | 198 derived | Not supplied | Q3-25 10-Q page:6; Adjusted EBITDA is 901 less 189 less 514, a derived figure |
| Q4 2025 | 1,144 | 589 | (276) | 189 | 3.6x at 2025-12-31 | Feb release page:12, page:18-19 |
| Q1 2026 | 1,371 | 785 | 57 | 334 | 3.5x at 2026-03-31 | May release page:1, page:4; gross profit is 1,583 less 798 |
| Q2 2026 | 1,368 | 798 | 54 | 288 | 3.1x at 2026-06-30 | Q2 10-Q page:6; Aug release page:1, page:4 |

### Adjusted EBITDA bridge and quality

Adjusted EBITDA starts from reported net income, adds net interest expense, income tax and depreciation and amortization to reach EBITDA, then adjusts for the cost of sales items, asset impairment, restructuring and other special charges, sold royalty revenue, the 2024 divestiture gain and other (income) expense items (Aug release page:14; Feb release page:18). For the trailing twelve months the adjustments are 252 of impairment, restructuring and other special charges, less 33 of sold royalty revenue, plus 16 of other expense items and 1 of cost of sales, in total 236, equal to 31 percent of reported EBITDA of 773 (calculation below). Three points matter for credit use. First, the sold royalty adjustment removes revenue that Elanco still books under GAAP but no longer receives in cash, because the XDEMVY royalties go to Blackstone through 2033-08-24 (Q2 10-Q page:17); removing it makes Adjusted EBITDA the more conservative measure on that item. Second, the special charges are not one-off in size or frequency: they were 127 in FY2023, 150 in FY2024, 237 in FY2025 and 252 trailing (10-K page:92; Q2 10-Q page:6). Third, the FY2025 charges include 155 of restructuring of which 116 is cash severance (Feb release page:3, page:5); the restructuring reserve stood at 124 at 2025-12-31 and 86 at 2026-06-30, with about 80 classified as current (Q2 10-Q page:11-12). That cash is spent after the add-back and does not appear in Adjusted EBITDA, though it is in operating cash flow.

Imputed interest of 33 in FY2025 and 29 in six months 2026 on the liability for sale of future revenue sits in reported interest expense but is excluded in the company's adjusted interest (Aug release page:3, page:12). It accretes the liability: the balance rose from 304 to 315 in six months because imputed interest of 29 exceeded royalty revenue applied of 18 (Q2 10-Q page:17).

### Capital structure and debt terms

Amounts in US$m, from Note 7 (10-K page:108-111; Q2 10-Q page:12). All floating-rate term debt prices off Term SOFR except the Euro Term Loan, which prices off EURIBOR.

| Instrument | 2025-12-31 | 2026-06-30 | Pricing | Maturity | Other terms |
| --- | --- | --- | --- | --- | --- |
| Revolving Credit Facility | 0 drawn of 750 | 0 drawn of 750 | Term SOFR plus a spread based on net total leverage; spread 1.50% at both dates | July 2029 | Financial maintenance covenants apply |
| Term Loan B due 2032 | 1,100 | 1,095 | Term SOFR plus 1.75% | 2032-10-31 | Quarterly required principal 0.25% |
| Euro Term Loan due 2029 | 470 | 383 | EURIBOR plus a spread based on net total leverage; 1.50% at 2025-12-31 | 2029-04-30 | EUR 400 million originally; quarterly required principal 1.875%; same covenants as the revolver |
| Incremental Term Facility due 2028 | 339 | 336 | Term SOFR plus 1.75% | 2028-08-12 | Quarterly installments |
| Incremental Term Facility due 2029 | 171 | 170 | Term SOFR plus 1.75% | 2029-04-19 | Quarterly installments |
| Incremental Term Facility due 2031 | 321 | 319 | Term SOFR plus 1.75% | 2031-08-13 | Quarterly installments |
| Incremental Term Facility due 2032 | 539 | 536 | Term SOFR plus 2.25% | 2032-10-31 | 540 originally; quarterly required principal 0.25% |
| Securitization Facility | 100 | 100 | Term SOFR plus 1.25% | June 2028 | Maximum 300; borrowing base is U.S. eligible receivables, which are pledged |
| Senior Notes due 2028 | 750 | 750 | 4.900% coupon, 6.650% at 2025-12-31 and 6.40% at 2026-06-30 after a rating upgrade in Q4 2025 | 2028-08-28 | Described as senior unsecured; limits on liens and sale-leasebacks |
| Unamortized debt issuance costs | (28) | (26) | Not applicable | Not applicable | Deducted in the balance sheet total of 3,762 and 3,663 |
| Finance lease liability | 255 | 255 | Discount rate 6.4% (10-K page:120) | Five-year lease from June 2025 | Includes a 250 purchase option or landlord put at the end of the term |

The weighted-average effective interest rate on borrowings, after swaps and excluding the finance lease, was 5.76% at 2025-12-31 and 5.79% at 2026-06-30 (10-K page:113; Q2 10-Q page:14).

### Rate and hedge exposure

At 2026-06-30 floating-rate borrowings are the six term facilities (2,839) plus the securitization facility (100), 2,939 in total, against 750 of fixed-rate notes. Interest rate swaps of 2,300 notional convert floating to fixed and have scheduled maturities in August 2026; forward-starting swaps of 1,450 notional become effective in August 2026 with maturities between 2027 and 2031, up from 850 at 2025-12-31 (Q2 10-Q page:14). On the pack's figures the hedged floating debt falls from 2,300 to 1,450 after August 2026 and unhedged floating-rate borrowings rise from 639 to 1,489, before any hedging added after 2026-06-30, which the pack does not show. The company states that approximately 80 percent of borrowings were fixed or swapped at 2026-06-30 (page:12). The calculation below gives about 83 percent for the pre-August position and about 60 percent for the post-August position on the same base; the post-August figure is an analyst illustration, not a company statement. Net investment hedges (1,000 million CHF notional with tenors in 2026 and 2027, of which 200 million CHF was extended to 2031 in July 2026) generated 23 of interest income in six months 2026, recorded as a reduction of interest expense (page:13-14).

### Covenants

Two financial maintenance covenants apply under the Revolving Credit Facility and, on consistent terms, the Euro Term Loan: a net total leverage ratio of pro forma net debt to pro forma adjusted EBITDA not to exceed 7.71 to 1.00 for the preceding four quarters, not subject to step-downs, and an interest coverage ratio of pro forma adjusted EBITDA to cash interest expense of no less than 2.00 to 1.00 (10-K page:109-110; Q3-25 10-Q page:15). The company states compliance with all covenants at 2026-06-30 (Q2 10-Q page:12). The achieved ratios are not supplied. Both covenant definitions differ from the metrics here: they use pro forma figures and covenant adjustments that the company says reduce its net leverage ratio below the printed measure (Aug release page:14), and a different net debt and cash interest definition. As an illustration only, not a covenant calculation: net debt of 3,159 divided by 7.71 is about 410, so trailing Adjusted EBITDA of 1,008 could fall by about 59 percent before the leverage test is reached on those proxies; and twice FY2025 cash interest of 206 is 412, so Adjusted EBITDA of 901 could fall by about 54 percent before the cover test is reached. The Senior Notes indenture has no financial maintenance covenant in the pack; it limits liens and sale-leasebacks and restricts mergers and sales of substantially all assets (10-K page:111). The Securitization Facility has covenants on the composition of the receivables portfolio, with compliance stated at 2025-12-31 (page:111).

### Liquidity by facility

At 2026-06-30: cash and cash equivalents 530; revolver commitment 750, nothing drawn, unused capacity approximately 750; securitization facility drawn 100 with approximately 165 of undrawn capacity under a borrowing base (Q2 10-Q page:12, page:36). Total of these inputs is 1,445. No letters of credit or other usage of the revolver is printed in any source. The revolver matures in July 2029 and the securitization facility in June 2028, so no facility expires within twelve months of 2026-06-30. Known cash calls over the next twelve months that the pack supports: required amortization (63 for calendar 2026 and 63 for 2027 on the 2025-12-31 schedule), deferred AHV cash consideration of about 60 in January 2027, restructuring reserve payments (about 80 current), 2026 capital expenditure guided at 175 to 200 (10-K page:86), and interest. A fall in cash from 545 to 530 in six months came with 76 paid for the AHV acquisition, 89 of debt repayment and 35 of share withholding payments, against operating cash flow of 290.

### Cash flow quality

Operating cash flow was 560 in FY2025 and 290 in six months 2026 against 233 a year earlier. Quarterly operating cash flow was 13 in Q1 2026 and 277 in Q2 2026 (May release page:4; Aug release page:4), which shows the first-half seasonal pattern; the company notes that parasiticide sales concentrate in the first half (Q2 10-Q page:30). Working capital absorbed 239 in six months 2026 against 185, with receivables up from 873 to 1,077 and inventories up from 1,737 to 1,769 since 2025-12-31 (page:6-7). Net purchases of property, equipment and software fell to 84 from 122 on timing of the Elwood, Kansas monoclonal antibody plant spend (page:37). Cash taxes of 225 in FY2025 compare with a tax expense of 8, driven by payments on the 2024 aqua divestiture gain (10-K page:84, page:126-127), so FY2025 free cash flow is a poor guide to a normal tax year; six-month 2026 cash taxes are not supplied. Interest on the liability for sale of future revenue and the sold royalties are non-cash and sit in operating cash flow adjustments (Q2 10-Q page:7).

### Claims outside the debt figure

| Claim | Amount | In or outside the debt figure | Locator |
| --- | --- | --- | --- |
| Liability for sale of future revenue (Blackstone, XDEMVY royalties to 2033-08-24) | 315 at 2026-06-30 | Outside; shown as its own noncurrent liability | Q2 10-Q page:6, page:17 |
| Headquarters finance lease | 255 liability; 250 purchase option or put at end of term | Inside the company's gross debt of 3,944, deducted in its net debt | 10-K page:108, page:121 |
| Operating lease liabilities | 124 at 2025-12-31 | Outside | 10-K page:121 |
| AHV deferred cash consideration | 100 through 2030; about 60 in January 2027 and 20 in January 2028 | Outside | Q2 10-Q page:10 |
| AHV and NutriQuest contingent consideration | Up to 140 for AHV through 2032, carried at 67; NutriQuest 19; balance sheet total 86 | Outside | Q2 10-Q page:10, page:15-16 |
| Restructuring reserve | 86 | Outside | Q2 10-Q page:11-12 |
| Pensions (Germany and Switzerland principally) | Funded status (150) at 2025-12-31; accrued retirement benefits 158 | Outside | 10-K page:93, page:133 |
| Legal matters | No material liabilities established; appeals pending | Outside | Q2 10-Q page:19-22 |
| Purchase obligations | Amount not supplied | Outside | 10-K page:86 |
| Factoring, supply chain finance, letters of credit | No such amounts printed | Not applicable | Searched, see Gaps |

### Latest quarter and after

Q2 2026 revenue was 1,368, up 10 percent reported and 8 percent in organic constant currency, with Pet Health 718 and Farm Animal 633 (Q2 10-Q page:9; Aug release page:2). Gross margin was 58.3 percent against 57.5 percent (page:32). Net income was 54 and Adjusted EBITDA 288. The AHV International acquisition closed 2026-04-30 for total estimated consideration of 243, with 76 paid in cash and funded from cash on hand and a 50 draw on the securitization facility, repaid in the quarter (page:10, page:30). Net leverage as reported fell from 3.5x to 3.1x in the quarter (May release page:4; Aug release page:4). Management raised 2026 guidance to revenue of 5,090 to 5,140 and Adjusted EBITDA of 1,010 to 1,035 and targeted year-end net leverage of approximately 3.0x (Aug release page:1, page:4); these are management claims. Subsequent items in the 10-Q are the July 2026 extension of 200 million CHF of net investment hedges to 2031 (page:13) and legal: the Ninth Circuit affirmed the Tevra verdict on 2026-07-06 and denied rehearing on 2026-07-31 (page:22). No filing or release dated after 2026-08-05 is in the pack.

### Handoff consumption

This module opened the CP-0 handoff and used it as follows. It kept CP-0's finding that Adjusted EBITDA and net leverage come only from releases, and labels them as management measures throughout. It carried the covenant, guarantor and security gaps unchanged (see Gaps). It used FY2025 only for cash interest and cash taxes, as CP-0 advised, and derived Q3 2025 Adjusted EBITDA as 198 and labelled it derived. It refines one CP-0 statement: CP-0 recorded a difference of 2 between depreciation and amortization on the six-month 2026 cash flow statement (343) and in the EBITDA reconciliation (341) as not explained. The difference sits wholly in Q1 2026, where the cash flow statement shows 172 and the reconciliation 170 (Q1 10-Q page:7; May release page:14); Q2 2026 is 171 in both, because 343 less 172 is 171. The cause is still not given in the sources. The reconciliation figure is used inside the EBITDA bridge and the cash flow figure for cash analysis. CP-0 is otherwise not corrected.

### Definition risks

Adjusted EBITDA differs from reported EBITDA by sold royalty revenue, restructuring and impairment charges, other expense items and, in FY2024, the divestiture gain. The company's net debt deducts the finance lease as well as cash, which lowers its net leverage by about 0.3x against this module's net basis (3.1x against 3.39x at 2026-06-30). Covenant EBITDA and net debt are defined in the credit agreement, which is not supplied, and are not the same as either. The cash interest figure is net of cash interest received on net investment hedges, which flatters cover relative to gross interest paid.

## Calculations

All amounts in US$m. Locators in brackets.

| Item | Inputs | Result |
| --- | --- | --- |
| LTM revenue | 4,715 + 2,739 - 2,434 [10-K page:92; Q2 10-Q page:6] | 5,020; equal to 1,137 + 1,144 + 1,371 + 1,368 |
| LTM gross profit | 2,593 + 1,583 - 1,397 | 2,779 |
| LTM net income | (232) + 111 - 78 | (199); equal to (34) + (276) + 57 + 54 |
| LTM MS&A, amortization, special charges, interest, tax | 1,430 + 830 - 741; 543 + 277 - 264; 237 + 25 - 10; 220 + 116 - 88; 8 + 32 - 7 | 1,519; 556; 252; 248; 33 |
| LTM D&A, reported EBITDA | 680 + 341 - 330; 676 + 600 - 503 | 691; 773 |
| LTM Adjusted EBITDA rebuilt | 901 + 622 - 514 [Feb release page:18; Aug release page:14] | 1,009 against printed 1,008; rounding. 198 + 189 + 334 + 288 = 1,009 |
| Q3 2025 Adjusted EBITDA derived | 901 - 189 - 514 | 198 |
| LTM net adjustments | 252 - 33 + 16 + 1, where 33 = 19 + 18 - 4 and 16 = 5 + 15 - 4 and 1 = 2 + 0 - 1 | 236; 773 + 236 = 1,009 |
| Adjustments share of reported EBITDA | 236 / 773 | 31 percent |
| Gross margin | 2,436 / 4,439; 2,593 / 4,715; 1,397 / 2,434; 1,583 / 2,739; 2,779 / 5,020 | 54.9%; 55.0%; 57.4%; 57.8%; 55.4% |
| Adjusted EBITDA margin LTM | 1,008 / (5,020 - 33) | 20.2% |
| LTM operating cash flow, net purchases, difference | 560 + 290 - 233; 276 + 84 - 122; 617 - 238 | 617; 238; 379. FY2024 541 - 147 = 394; FY2025 560 - 276 = 284; 6M 2025 233 - 122 = 111; 6M 2026 290 - 84 = 206 |
| Total debt including lease, 2026-06-30 | 3,689 + 255 [Q2 10-Q page:12, page:15]; or 3,845 + 73 + 26 [Aug release page:14] | 3,944 both ways |
| Total debt including lease, 2025-12-31 and 2024-12-31 | 3,790 + 255; 4,321 + 28 [10-K page:108] | 4,045; 4,349 |
| Net debt including lease | 3,944 - 530; 4,045 - 545; 4,349 - 468 | 3,414; 3,500; 3,881 |
| Company net debt | 3,944 - 530 - 255; 4,045 - 545 - 255 | 3,159; 3,245; both equal the printed figures |
| Company net leverage | 3,159 / 1,008; 3,245 / 901 | 3.13 (printed 3.1); 3.60 (printed 3.6) |
| Total debt / Adjusted EBITDA | 4,349 / 910; 4,045 / 901; 3,944 / 1,008 | 4.78; 4.49; 3.91 |
| Net debt including lease / Adjusted EBITDA | 3,881 / 910; 3,500 / 901; 3,414 / 1,008 | 4.26; 3.88; 3.39 |
| Total debt / reported EBITDA | 4,349 / 1,385; 4,045 / 676; 3,944 / 773 | 3.14; 5.98; 5.10 |
| What moved leverage 4.49 to 3.91 | 3,944 / 901 (new debt, old EBITDA) and 3,944 / 1,008 | 4.38 and 3.91: debt paydown explains 0.11 and higher EBITDA 0.47 of the 0.58 fall |
| Cash interest cover | 910 / 296; 901 / 206; 901 / (206 + 43); 910 / (296 + 31) | 3.07; 4.37; 3.62; 2.78 |
| Income statement interest cover | 910 / 235; 901 / 220; 514 / 88; 622 / 116; 1,008 / 248 | 3.87; 4.10; 5.84; 5.36; 4.06 |
| Liquidity inputs | 545 + 750 + 120; 530 + 750 + 165 | 1,415; 1,445; the chart shows facilities of 870 and 915 |
| Maturity schedule | 63 + 63 + 1,236 + 548 + 20 + 1,860 [10-K page:111] | 3,790; share of total: 2026-2027 3 percent, 2028 33 percent, 2029 14 percent, 2031 and later 49 percent |
| Debt table adds | 1,095 + 383 + 336 + 170 + 319 + 536 + 0 + 100 + 750 - 26 [Q2 10-Q page:12] | 3,663; plus 255 = 3,918 = 73 + 3,845; 2025-12-31: 3,790 - 28 = 3,762, plus 255 = 4,017 = 74 + 3,943 |
| Debt movement against cash flow | 3,790 - 3,689 against repayments of long-term borrowings of 89 [Q2 10-Q page:8] | 101 against 89; the 12 difference is not explained in the sources and is presumed to be currency and non-cash movement, which is an inference |
| Cash flow ties | 290 - 170 - 139 + 4 [Q2 10-Q page:7-8] | (15); 545 - 15 = 530 |
| Floating-rate debt and hedged share | Floating 1,095 + 383 + 336 + 170 + 319 + 536 + 100 = 2,939; hedged 2,300 | Unhedged 639; fixed or swapped (750 + 2,300) / 3,689 = 83 percent against the printed approximately 80 percent |
| After August 2026 | Hedged 1,450; (750 + 1,450) / 3,689; unhedged 2,939 - 1,450 | 60 percent; 1,489. Illustrative: 100 basis points on 1,489 is about 15 a year before tax, before any hedging after 2026-06-30 |
| Covenant illustration | 3,159 / 7.71; 1 - 410 / 1,008; 2 x 206; 1 - 412 / 901 | 410; 59 percent; 412; 54 percent. A proxy only: covenant definitions differ |
| Goodwill plus intangibles | 4,414 + 3,681; 4,779 + 3,408; 4,845 + 3,204 [10-K page:93; Q2 10-Q page:6] | 8,095; 8,187; 8,049; total equity is 6,096, 6,547 and 6,588, so tangible equity is negative at each date: 6,588 - 8,049 = (1,461) |
| Finance lease payments | 17 x 4 + 259 [10-K page:121] | 327, equal to the printed total; 2030 payment of 259 includes the 250 option; 2030 maturity of 20 plus 259 = 279 |
| Lease balances | 143 - 19; 327 - 72; 16 + 239 | 124; 255; 255 |
| EBITDA reconciliation ties | Q2 2026: 54 + 59 + 2 + 171 = 286, then + 9 - 9 + 2; six months: 111 + 116 + 32 + 341 = 600, then + 25 - 18 + 15 | 288 and 622, equal to printed |
| D&A across statements | Q1 172 - 170; Q2 (343 - 172) - 171 [Q1 10-Q page:7; Q2 10-Q page:7; May release page:14; Aug release page:14] | 2 in Q1; 0 in Q2 |
| Half-year growth | 2,739 / 2,434; 1,583 / 1,397; 622 / 514; 830 / 741 | 12.5 percent; 13.3 percent; 21.0 percent; 12.0 percent |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Achieved covenant ratios and covenant definitions not supplied; 2026 10-Qs state compliance only (Q2 10-Q page:12). The headroom shown is a proxy | High | CP-2, CP-5 | Obtain the compliance certificate and credit agreement definitions |
| Executed credit agreement, indenture and receivables agreement, guarantors and collateral list not supplied; searched "guarant", "collateral", "pledge" in all sources | High | CP-2, CP-5 | Add the documents; priority of claims cannot be mapped from the pack |
| Six-month 2026 and six-month 2025 cash interest paid and cash taxes not supplied, so trailing cash interest cover is not calculable | Medium | CP-1A, CP-2 | Request the cash flow supplement or the Q3 2026 10-Q; use FY2025 until then |
| No filing after 2026-08-05; balance sheet is at 2026-06-30 and the August 2026 swap maturities and any later hedging are not visible | High | CP-2 | Add later filings if they exist before use |
| Adjusted EBITDA, net debt and net leverage only in management releases; no independent reconciliation to a covenant definition | Medium | CP-2 | Treat as an attributed claim |
| Q3 2025 Adjusted EBITDA derived, not printed | Low | CP-1A | Labelled derived |
| Cause of the Q1 2026 difference of 2 in depreciation and amortization not given | Low | CP-2 | None; use each figure for its stated purpose |
| Decomposition of the 2028 and 2029 maturities by facility and an updated schedule after 2025-12-31 not printed; remaining 2026 amortization not supplied | Medium | CP-2 | Rebuild from facility terms downstream and label as derived |
| Letters of credit, factoring, supply chain finance, off-balance-sheet and purchase obligation amounts not printed; searched "letter of credit", "standby", "surety", "factor" and "supplier finance" in all sources | Low | CP-2 | Carry stated unused revolver capacity; no deduction |
| Credit ratings not supplied; the context is blank and filings give no level | Medium | CP-2 | Supply if rating-based work is wanted |
| Pension funded status and lease schedule are at 2025-12-31 only | Low | CP-2 | Carry as annual-report dated |
| Securitization availability depends on a borrowing base not disclosed | Low | CP-2 | Treat 165 as approximate and variable |
| Page-chunk locators; no fidelity review of the extracted tables | Low | CP-5 | Spot-check key tables against the htm |

## Next module

CP-1A (business and transaction context) runs next, then CP-2 and CP-5. CP-1A should use the revenue mix (Pet Health 1,428 and Farm Animal 1,275 in six months 2026), the AHV acquisition terms, the Blackstone royalty sale and the single customer at about 12 percent of revenue (Q2 10-Q page:10). CP-2 should carry the Adjusted EBITDA definition risk, the 3.91x and 3.1x leverage bases, the 2028 maturity of 1,236, the August 2026 hedge roll-off, the debt-like claims table and the open covenant, guarantor and ratings gaps. CP-5 should trace the locators above, which are extraction chunks.
