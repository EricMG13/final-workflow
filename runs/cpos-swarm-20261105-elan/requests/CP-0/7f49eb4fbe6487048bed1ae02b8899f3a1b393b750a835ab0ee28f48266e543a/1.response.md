## Request

Issuer: Elanco Animal Health Inc, whose registrant name on every filing cover is Elanco Animal Health Incorporated (issuer id elan; NYSE ticker ELAN; Indiana registrant; SEC file number 001-38661; 10-Q page:1). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD; the statements are in millions of US dollars (10-Q Q2 2026 page:6). Current period named by the context: Q2 2026 (quarter ended 2026-06-30). Prior period named by the context: FY2025.

Question for this module: can the supplied source set support the requested downstream work (CP-1, CP-1A, CP-2, CP-5), and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion. It does not normalize, reconcile or calculate figures. Arithmetic below is limited to tie-outs that test source consistency.

The context file holds run settings and is not issuer evidence. Its deal terms, quotes, ratings, peers, precedents and research questions are empty, it names no borrower, parent, guarantor or sponsor, and its legal-documents attachment is "none". Those blanks are treated as not supplied, never as zero.

## Sources

### Issuer sources relied on

Each file is a JSONL text extraction of an SEC filing or exhibit. The locator `page:N` is the extraction chunk, not the printed page. The sha256 below is the pinned file hash; each file also prints a different hash for its underlying htm document in its first line, which is not used here.

| Source name | sha256 | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-12-31_elan-20251231.htm.jsonl | 631f12506b56aa385a6cb05350b491f6e4807480f3dfa124f622742afde4eb4d | Audited annual report, Form 10-K, 150 chunks; signed 2026-02-24 (page:150); auditor opinion at page:138-142; filed statements control their facts | Fiscal year ended 2025-12-31; single reporting segment (page:138); consolidated Elanco Animal Health Incorporated and subsidiaries (page:7) |
| 10-Q_2025-09-30_elan-20250930.htm.jsonl | 7696222aac33b3c5724420ded155220803d97cf7ef1e18a5f318f74a02a9f48b | Unaudited quarterly report, Form 10-Q, 49 chunks | Quarter and nine months ended 2025-09-30 (page:1, page:6); the only source for discrete Q3 2025 statements |
| 10-Q_2026-03-31_elan-20260331.htm.jsonl | 8e89da9cffbcecbe1eed4ffa4c7a49caeeccf8b4ba6b25abfd3550722e65c68a | Unaudited quarterly report, Form 10-Q, 37 chunks | Quarter ended 2026-03-31 (page:1); debt note at page:11 |
| 10-Q_2026-06-30_elan-20260630.htm.jsonl | c53b62a714e3fe245be0c34b9cfa53c27b751637f6f9ab0c69e1814c10ec5ae4 | Unaudited quarterly report, Form 10-Q, 41 chunks; signed 2026-08-05 (page:41); latest filed statements in the pack | Quarter and six months ended 2026-06-30; balance sheet at 2026-06-30 against 2025-12-31 (page:6) |
| EX-99.1_2026-02-24_elanco-12312025exhibit991.htm.jsonl | 1f19620e2ed3f724fb36ed2529d45e324cf0c5eb195eeb5f344974991a2cc3a7 | Earnings release exhibit dated 2026-02-24, 19 chunks; management attribution, supporting claims only | Q4 2025 and FY2025; non-GAAP reconciliations (page:13-19) |
| EX-99.1_2026-05-06_elanco-20260331exhibit991.htm.jsonl | 4e76217e501306dbc17cfb4f968ce0b23feddf7680c305268cc02ac6e80dcede | Earnings release exhibit dated 2026-05-06, 15 chunks; supporting claims only | Q1 2026; guidance (page:1) |
| EX-99.1_2026-08-05_elanco-20260630exhibit991.htm.jsonl | b942651707926f126b37ca482f9fd9191b045d925b308278420efd4d0def6d7f | Earnings release exhibit dated 2026-08-05, 14 chunks; supporting claims only | Q2 2026 and six months; Adjusted EBITDA and net leverage reconciliations (page:11-14) |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | f7c64d35ea0396669fb4a13a10eedb17c6d4612678c62234d77a0ad21bc4c259 | Run settings only; not issuer evidence |

### Supplied handoffs

None. This is the first module in the run, so the handoff set is empty.

### Ignored file

_retrieval.json sits in the pack folder and is not a pinned source. It is not relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filings and releases through June 30, 2026 are enough to build the financial base, debt and liquidity picture and business context. Executed credit documents, reported covenant ratios and anything after August 5, 2026 are not in the pack. | Medium | No executed debt documents, and no filing or release after the second quarter of 2026; Adjusted EBITDA and net leverage come only from management releases. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt instruments, maturities, covenant levels and facility capacity are printed in the annual report, and the second-quarter report updates balances and capacity. | The debt table, maturity wall and liquidity inputs can be built from filed statements. | High |
| Adjusted EBITDA and the 3.1x net leverage ratio appear only in management releases, not in the filed statements. | Leverage work rests on an attributed non-GAAP measure that excludes covenant adjustments. | High |
| Reported covenant ratios, the guarantor list and the security package are not in the pack. Only covenant levels and compliance statements are. | Covenant headroom cannot be measured and lender priority cannot be mapped; downstream work must carry these as limits. | High |
| Claims outside the debt table are disclosed: a sold-royalty liability, a headquarters finance lease with a purchase option, deferred and contingent acquisition payments, and pension shortfalls. | These add calls on cash flow that need separate treatment downstream. | Medium |

### Readiness view

The effective source set supports the requested work with limitations. All four requested consumers are assessed as READY_WITH_LIMITATIONS; none is CONDITIONAL and none is BLOCKED. The audited annual report, three quarterly reports and three earnings releases cover the periods the context names (Q2 2026 and FY2025), in the reporting currency, up to the latest evidence dated 2026-08-05, which is before the cutoff. The binding limitations are five. First, the newest balance sheet is at 2026-06-30, and no filing or release dated after 2026-08-05 is in the pack, so the Q3 2026 position is not supplied. Second, Adjusted EBITDA, net debt and the 3.1x net leverage ratio come only from management releases and exclude covenant adjustments; the filed 10-Qs print none of them. Third, no executed legal document is in the pack, so guarantors, security and covenant definitions rest on filing summaries and exhibit lists. Fourth, the reported covenant ratios are not printed, only the levels and compliance statements. Fifth, no fidelity review of the text extraction has been done, and the pack has no charts, images or slides. None of these blocks a consumer from starting, and each carries forward as a stated limit.

### Source-by-source assessment

All seven sources identify Elanco Animal Health Incorporated as the registrant or the announcing company (page:1 of each). No source is draft, unsigned, blocked or a duplicate of another. The 10-K is audited; the 10-Qs are unaudited. The filed 10-K and 10-Qs control their own facts. The three releases are management claims and must not override the filings.

| Source | What it supports | Limit |
| --- | --- | --- |
| 10-K FY2025 | Audited statements (page:92-94), debt note with facility terms, covenant levels and maturity schedule (page:108-112), lease note (page:119-121), pensions (page:133-136), tax payments (page:126-127), restructuring (page:107), subsequent event (page:138) | Covenant ratios achieved not printed; no guarantor list |
| 10-Q Q3 2025 | Discrete Q3 2025 statements (page:6) and the October 2025 refinancing description with covenant levels (page:15) | Prior-year quarter only |
| 10-Q Q1 2026 | Q1 2026 statements and debt table at 2026-03-31 (page:11) | Superseded by the Q2 report for balances |
| 10-Q Q2 2026 | Latest statements (page:6-8), debt note (page:12), fair value of debt (page:15), sale of future revenue (page:17), contingencies (page:19-22), liquidity (page:36) | No Adjusted EBITDA; covenant levels not restated, compliance only (page:12); cash interest and cash taxes not printed |
| EX-99.1 2026-02-24 | FY2025 and Q4 2025 Adjusted EBITDA 901 for the year, net debt and net leverage 3.6 at 2025-12-31 (page:18-19), guidance | Management claim; non-GAAP |
| EX-99.1 2026-05-06 | Q1 2026 highlights, Adjusted EBITDA 334, net leverage 3.5x, guidance (page:1) | Management claim; guidance superseded |
| EX-99.1 2026-08-05 | Q2 2026 Adjusted EBITDA 288, six-month 622, gross to net debt bridge and trailing twelve month Adjusted EBITDA (page:14), guidance (page:4-5) | Management claim; excludes covenant adjustments (page:14) |

### Entity and perimeter

The registrant and reporting entity is Elanco Animal Health Incorporated and its subsidiaries, consolidated (10-K page:7; 10-Q Q2 2026 page:1). The company operates as a single reporting segment, so there is no segment profit measure other than consolidated net income (10-Q Q2 2026 page:24). The 10-K exhibit list names the roles in the debt: under the Credit Agreement dated 2020-08-01 as amended by Amendment No. 3 dated 2025-10-31, Elanco Animal Health Incorporated is borrower, Elanco US Inc. is co-borrower and Elanco Financing (Netherlands) B.V. is the Dutch borrower, with "subsidiary loan parties", JPMorgan Chase Bank, N.A. as administrative agent and U.S. and Canadian collateral agent, and Wilmington Trust, National Association as non-U.S. and non-Canadian collateral agent and security trustee (page:147). The 4.900 percent senior notes were issued by Elanco Animal Health Incorporated under an indenture with Deutsche Bank Trust Company Americas as trustee (page:146; page:111). The receivables facility is documented in a Receivables Loan Agreement among Elanco SPEAR LLC, Elanco US Inc., and the lenders and lender agents, with Coöperatieve Rabobank U.A., New York Branch named (page:146), and the receivables are pledged for it (page:110-111). The pack does not name the subsidiary loan parties, does not state whether the senior notes carry subsidiary guarantees, and does not list the collateral; the risk factors say only that a significant portion of assets is pledged under the credit facilities and call the notes "senior unsecured notes" (page:44). The issuer-versus-guarantor-versus-collateral map is therefore an unresolved gap, not a conclusion. The context names no borrower, parent or guarantor. The name in the context ("Inc") and the registrant name ("Incorporated") are the same entity.

### Period basis and version relationships

There is no perimeter recast in the pack. All periods are on one consolidated basis, with one change of scope: the AHV International B.V. acquisition closed on 2026-04-30 and its results are included since that date, with revenue described as not material in Q2 2026 (10-Q Q2 2026 page:10-11, page:32). The aqua business was divested on 2024-07-09 (Feb release page:4), which affects FY2024 comparatives only. Quarter-versus-year-to-date labels are explicit in each report. The pack supports these discrete periods: Q3 2025 from the Q3 2025 10-Q (page:6), Q4 2025 from the February release (page:12), Q1 2026 from the May release (page:1) and Q2 2026 from the 10-Q and August release. Discrete Q3 2025 Adjusted EBITDA is not printed in any source (no Q3 2025 release is in the pack); it can be derived downstream and must be labelled derived.

Trailing-twelve-month Adjusted EBITDA of 1,008 as of 2026-06-30 is printed by the company (August release page:14). The pack also contains the components to rebuild it: FY2025 901 (February release page:18) plus six months 2026 of 622 less six months 2025 of 514 (August release page:14). The rebuilt figure is in Calculations.

### Debt and liquidity evidence present

Amounts in millions of USD at 2026-06-30 (10-Q Q2 2026 page:12): Term Loan B due 2032 1,095; Euro Term Loan due 2029 383 (original amount EUR 400 million, 10-K page:109); Incremental Term Facilities due 2028, 2029, 2031 and 2032 of 336, 170, 319 and 536; Revolving Credit Facility nil drawn on 750 of commitments, maturing July 2029; Securitization Facility 100 drawn, maturing June 2028; Senior Notes due 2028 750, bearing 6.40 percent; unamortized debt issuance costs (26); total debt 3,663; finance lease liability 255; total 3,918, of which 73 is current. Facility pricing, amortization and maturities are printed in the 10-K (page:109-111). The 10-K schedule of required principal payments at 2025-12-31 runs 2026 63, 2027 63, 2028 1,236, 2029 548, 2030 20, and 2031 and thereafter 1,860 (page:111); the 10-Q Q2 2026 gives no updated schedule.

Financial maintenance covenants under the Revolving Credit Facility are a net total leverage ratio not to exceed 7.71 to 1.00, without step-downs, and an interest coverage ratio of no less than 2.00 to 1.00, both on pro forma adjusted EBITDA for four quarters (10-K page:109; 10-Q Q3 2025 page:15). The Euro Term Loan has consistent covenants (10-K page:110). The Q2 2026 10-Q states compliance with all covenants at 2026-06-30 (page:12) but prints neither the levels nor the achieved ratios. The Senior Notes indenture limits liens and sale-leaseback transactions and restricts consolidation, merger or sale of substantially all assets (10-K page:111).

Liquidity inputs printed at 2026-06-30 (10-Q Q2 2026 page:36): cash and cash equivalents 530, unused Revolving Credit Facility capacity of approximately 750, and approximately 165 of undrawn Securitization Facility capacity that fluctuates with the borrowing base. At 2025-12-31 the comparable figures were 545, approximately 750 and approximately 120 (10-K page:82). No letters of credit drawn against the revolver are printed (searched, see Gaps). A significant part of cash is held outside the U.S. (page:36). Management's net debt at 2026-06-30 is 3,159 and net leverage 3.1 times trailing twelve month Adjusted EBITDA of 1,008, a management measure that excludes covenant-related adjustments (August release page:14).

Debt-like and other claims disclosed: liability for sale of future revenue to Blackstone of 315 at 2026-06-30 after a 295 payment received in May 2025, with an effective interest rate of 18.3 percent and imputed interest of 29 in six months 2026 (10-Q Q2 2026 page:17); the corporate headquarters finance lease, with liability 255 and a purchase option and landlord put at 250 at the end of five years (10-K page:120-121); operating lease liabilities of 124 at 2025-12-31 (10-K page:121); AHV deferred cash consideration of 100 due through 2030, of which approximately 60 is payable in January 2027 and 20 in January 2028, and contingent consideration of up to 140 through 2032 carried at fair value 67 (10-Q Q2 2026 page:10); other contingent consideration of 19 for NutriQuest (page:16); a restructuring reserve of 86 (page:11-12); and pension and retirement obligations, with a funded status of (150) at 2025-12-31 (10-K page:133). Cash paid for interest was 206 and net cash taxes were 225 in FY2025 (10-K page:112, page:126). Six-month 2026 cash interest and cash taxes are not printed.

### Quarter, subsequent events and contingencies

Evidence present for the latest quarter and the period after it: the AHV acquisition closed on 2026-04-30 for total estimated consideration of 243, funded from cash on hand and a 50 draw on the Securitization Facility repaid within the quarter (page:10, page:30); the weighted-average effective interest rate on debt excluding the finance lease was 5.79 percent, with interest rate swaps of 2,300 notional maturing in August 2026 and forward-starting swaps of 1,450 effective August 2026 (page:14); the pack does not show what happened at those August 2026 dates; in July 2026 the company extended 200 million CHF of net investment hedges to 2031 (page:13); the Fourth Circuit appeal in the Barpar securities class action is pending after a dismissal with prejudice on 2026-03-26 (page:19); the Ninth Circuit affirmed the jury verdict in the Tevra matter on 2026-07-06 and denied rehearing on 2026-07-31 (page:22), with a settlement in principle of a non-material amount in two related class actions (page:22); the company states it has no material liabilities established for these legal matters (page:19). The 2026-08-05 release raised full-year revenue guidance to 5,090 to 5,140, Adjusted EBITDA to 1,010 to 1,035 and targeted a year-end net leverage ratio of approximately 3.0 times (August release page:1, page:4). That guidance is a management claim. No event dated after 2026-11-05 is relied on. The FY2026 guidance, the January 2027 and January 2028 deferred payments and the interest rate swap start dates are future dates stated as scheduled or expected, not as facts.

### Consumer assessment

| Consumer | Evidence demand | Status | Carried limitations |
| --- | --- | --- | --- |
| CP-1 financial base | Discrete periods, annual base, add-backs, facility-level debt and carrying values, cash interest and cash taxes, KPIs | READY_WITH_LIMITATIONS | Latest period is Q2 2026; Adjusted EBITDA only in releases; Q3 2025 discrete Adjusted EBITDA not printed; six-month 2026 cash interest and cash taxes not printed; single segment so no segment profit; depreciation and amortization differs between the cash flow statement and the EBITDA reconciliation |
| CP-1A business and transaction context | Business, ownership, transaction and history facts | READY_WITH_LIMITATIONS | AHV agreement, the Blackstone purchase and sale agreement and the refinancing documents are described only in filings; no sponsor, deal terms or ownership map in the context |
| CP-2 fundamental synthesis | Settled upstream registers plus filings | READY_WITH_LIMITATIONS | Reported covenant ratios, guarantor map, security package and ratings not supplied; no Q3 2026 data |
| CP-5 evidence trace | Citations that resolve in pinned sources | READY_WITH_LIMITATIONS | Depends on page-chunk locators; extraction fidelity not reviewed |

Missing downstream analytical handoffs are not treated as source conditions. The dependency planner sequences them.

### Extraction status and fidelity

Every source was retrieved as text chunks and read by search and targeted page reads. Tables arrived as flattened text; column headers were checked against the period labels printed in each table. No image, chart or slide content exists in the pack, and the releases are text only. A successful extraction is not a fidelity review, and none is claimed.

## Calculations

These are source tie-outs only, in millions of USD unless stated. No figure is normalized. Locators are in the Inputs column.

| Check | Inputs and locator | Result |
| --- | --- | --- |
| Debt table adds at 2026-06-30 | 1,095 + 383 + 336 + 170 + 319 + 536 + 0 + 100 + 750 = 3,689; less 26 (10-Q Q2 2026 page:12) | 3,663, equal to the printed total debt |
| Debt plus finance lease | 3,663 + 255 (page:12) | 3,918, equal to the printed subtotal; 73 + 3,845 = 3,918, equal to the balance sheet lines (page:6) |
| Debt table adds at 2025-12-31 | 1,100 + 470 + 339 + 171 + 321 + 539 + 0 + 100 + 750 = 3,790; less 28 (page:12) | 3,762, equal; plus 255 = 4,017, equal to 74 + 3,943 |
| Debt before issuance costs vs fair value table | 3,663 + 26 (page:12) vs 3,689 carrying (page:15) | 3,689, equal. Fair value is 3,713 at 2026-06-30 (page:15) |
| Maturity schedule adds | 63 + 63 + 1,236 + 548 + 20 + 1,860 (10-K page:111) | 3,790, equal to the printed total, which matches the 2025-12-31 debt before issuance costs above |
| Gross debt to net debt bridge | 3,845 + 73 + 26 = 3,944; less 530 and less 255 (August release page:14) | 3,159, equal to the printed net debt |
| Net leverage as printed | 3,159 / 1,008 (August release page:14) | 3.13, rounds to the printed 3.1 |
| Net leverage at 2025-12-31 | Gross debt 3,943 + 74 + 28 = 4,045; less 545 and 255 = 3,245; 3,245 / 901 (February release page:19) | 3.60, equal to the printed 3.6 |
| Trailing twelve month Adjusted EBITDA rebuilt | 901 (February release page:18) + 622 - 514 (August release page:14) | 1,009 against the printed 1,008; difference of 1 is rounding ("Numbers may not add due to rounding", page:14) |
| Quarters add to six months | Q1 revenue 1,371 (May release page:1) + Q2 1,368 (10-Q page:6) vs six months 2,739; net income 57 + 54 vs 111; Adjusted EBITDA 334 + 288 vs 622 | 2,739, 111 and 622, all equal |
| Quarters add to FY2025 | Revenue nine months 3,571 (10-Q Q3 2025 page:6) + Q4 1,144 (February release page:12) vs 4,715; net income 44 + (276) vs (232) | 4,715 and (232), equal |
| Revenue by product, six months 2026 | 1,428 + 1,275 + 36; Farm Animal 629 + 453 + 193 (10-Q Q2 2026 page:9) | 2,739 and 1,275, equal |
| EBITDA reconciliation, Q2 2026 | 54 + 59 + 2 + 171 = 286; + 9 - 9 + 2 (August release page:14) | 288, equal to the printed Adjusted EBITDA |
| EBITDA reconciliation, six months 2026 | 111 + 116 + 32 + 341 = 600; + 25 - 18 + 15 (August release page:14) | 622, equal |
| Depreciation and amortization across statements | 343 on the cash flow statement (10-Q Q2 2026 page:7) vs 341 in the EBITDA reconciliation (August release page:14), six months 2026 | Difference of 2 not explained by the sources; the 2025 figure is 330 in both. Carried as a limitation |
| Revolver availability | 750 commitments (page:12) less 0 drawn (page:12) vs approximately 750 unused (page:36) | Equal; no letter of credit amount is printed to deduct |
| AHV consideration | 76 + 100 + 67 (10-Q Q2 2026 page:10) | 243, equal to the printed total; identifiable net assets 106 + goodwill 137 = 243 (page:11) |
| Lease liabilities at 2025-12-31 | 143 - 19 = 124 operating; 327 - 72 = 255 finance; 16 + 239 = 255 (10-K page:120-121) | Equal to printed totals |
| Interest expense split, Q2 2026 | 59 reported less 15 imputed (10-Q page:34; August release page:12) | 44, equal to the printed adjusted net interest expense (August release page:3) |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No filing or release dated after 2026-08-05 is in the pack; the latest balance sheet is at 2026-06-30, so any Q3 2026 position is not supplied | High | CP-1, CP-2 | Carry the Q2 2026 date as the latest balance sheet; add the Q3 2026 10-Q and release if they exist before the report is used |
| Reported (achieved) covenant ratios not supplied; the 2026 10-Qs state compliance only (10-Q Q2 2026 page:12). Levels of 7.71 to 1.00 and 2.00 to 1.00 are printed only in the 10-K and the Q3 2025 10-Q; searched "covenant", "interest coverage" and "net total leverage" across all seven sources | High | CP-1, CP-2 | Obtain the compliance certificate or covenant calculation; headroom is not calculable from the pack because the covenant EBITDA and net debt differ from the management measures (August release page:14) |
| Executed legal documents (credit agreement and Amendment No. 3, indenture and supplemental indentures, receivables loan agreement) not supplied; they appear only in the 10-K exhibit list (page:146-147); context legal_documents is none | High | CP-2, CP-5 | Add the executed documents; until then legal terms are filing summaries |
| Subsidiary loan parties, guarantors of the senior notes and the collateral package not named; searched "guarant", "collateral", "pledge", "secured" in all sources | High | CP-2, CP-5 | Obtain the credit agreement security schedules and the notes indenture |
| Adjusted EBITDA, net debt and net leverage appear only in management releases; the filed reports contain no Adjusted EBITDA | Medium | CP-1, CP-2 | Treat as an attributed non-GAAP claim; rebuild from the reconciliation tables and label |
| Discrete Q3 2025 Adjusted EBITDA not printed (no Q3 2025 release in the pack) | Medium | CP-1 | Derive from FY2025, Q4 2025 and six-month 2025 figures downstream and label as derived |
| Six-month 2026 cash paid for interest and cash taxes not printed; searched "interest paid", "cash paid", "income taxes paid" in the 2026 10-Qs. FY2025 is printed (10-K page:112, page:126) | Medium | CP-1 | Use FY2025 values for the annual base; request the cash flow supplement if a 2026 figure is needed |
| Letters of credit or other drawings that reduce revolver capacity not printed; searched "letter of credit", "LC", "standby", "surety", "bank guarantee" in all sources with no match. The unused capacity is stated as approximately 750 | Low | CP-1, CP-2 | Carry the stated figure; do not deduct an unknown amount |
| Depreciation and amortization of 343 versus 341 across statements (see Calculations) | Low | CP-1 | Use the cash flow statement figure for cash analysis and the reconciliation figure only inside the EBITDA bridge |
| Credit ratings and agency actions not supplied beyond the statement that ratings were downgraded most recently in 2023 (10-K page:45) and a rating upgrade in the fourth quarter of 2025 reduced the senior notes rate (10-Q Q2 2026 page:12); no agency level is printed. Context ratings are blank | Medium | CP-2 | Supply current ratings if rating-based work is wanted; not zero |
| Pension funded status and the operating lease schedule are at 2025-12-31 only; no 2026 update | Low | CP-1, CP-2 | Carry as annual-report dated |
| Purchase obligations amount not printed; the 10-K describes them as primarily short term without an amount (page:86) | Low | CP-1 | None beyond carrying the description |
| Fair value of debt is supplied at 2026-06-30 and 2025-12-31 in aggregate, not by instrument | Low | CP-1 | None |
| Page-chunk locators are extraction chunks, not printed page numbers; no fidelity review of extracted tables | Low | CP-5 | Spot-check key tables against the original htm if used externally |
| Release guidance and the net leverage target are forward-looking management claims | Low | CP-2 | Treat as attributed claims, not evidence of outcome |

## Next module

CP-1 (financial base) runs next, followed by CP-1A, CP-2 and CP-5. It should open this handoff and carry forward: the latest balance sheet at 2026-06-30 with no later filing in the pack; the filed-statement versus management-release split for Adjusted EBITDA and net leverage; the unresolved depreciation and amortization difference between 343 and 341; discrete Q3 2025 Adjusted EBITDA as a derived figure only; FY2025 only for cash interest and cash taxes; and the claims outside the debt table (liability for sale of future revenue, headquarters finance lease, AHV deferred and contingent payments, restructuring reserve, pensions). CP-2 and CP-5 should carry the covenant, guarantor and security gaps unchanged.
