# CP-0 — Source readiness: MAXIMUS, INC. (mms)

## Request

- Issuer: MAXIMUS, INC. (issuer id `mms`; the filings name the registrant "Maximus, Inc.", NYSE ticker MMS), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run: `mms-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, current period `q3-2026`, prior period `fy-2025`, reporting currency USD (context). Requested modules: CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Period convention. Maximus has a fiscal year ending September 30. The context label `q3-2026` is read here as fiscal third quarter 2026, the three months ended June 30, 2026, which the issuer titles "Third Quarter 2026 Form 10-Q" (`10-Q_2026-06-30…` page:1). The label `fy-2025` is read as the fiscal year ended September 30, 2025. The quarter ended September 30, 2026 is the issuer's fiscal fourth quarter and is not supplied (see Information-availability boundary).
- Execution: host session. The host read the pinned files and wrote this answer. No provider was called.
- Question: can the supplied public filings support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion. No figure is normalized or reconciled here.
- Context fields for borrower, parent, guarantors, ratings, quotes, deal terms, peers and research questions are blank. Blank is not evidence of absence and is not read as zero.

## Sources

Locators are `page:N` chunks of the pinned `.jsonl` text, not printed page numbers. Each file's first chunk also quotes the sha256 of the original `.htm` that it was extracted from; the table gives the sha256 of the pinned `.jsonl` file that CP-OS holds.

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-09-30_mms-20250930.htm.jsonl | 962786100737da7c8a25bf2c0b0d8b7bba5fc8fe85f1a63dc4a22607d3101fd0 | Form 10-K for the fiscal year ended September 30, 2025 (105 chunks; original `.htm` sha256 5f68c32bb74499653eef8cf005ce76e087d0fee69cfc1ec3eae26b7c122b7167) |
| 10-Q_2025-12-31_mms-20251231.htm.jsonl | 1ece10b3b4a1f72edf52da31ebe99ab2543998f22e423edd0be2ded3496f545d | Form 10-Q for the quarter ended December 31, 2025, fiscal first quarter 2026 (34 chunks) |
| 10-Q_2026-03-31_mms-20260331.htm.jsonl | 72c28dae66fdf3271ecd55284a1e9ffd02e932cd689052dff69253e7614fe8a8 | Form 10-Q for the quarter ended March 31, 2026, fiscal second quarter 2026 (36 chunks) |
| 10-Q_2026-06-30_mms-20260630.htm.jsonl | e0ee49037a76362fa1359adeb6f1d6ec0af3bf048fce3d62f4b088d4d2e2d60b | Form 10-Q for the quarter ended June 30, 2026, fiscal third quarter 2026 (39 chunks) |
| EX-99.1_2026-02-05_mms-2025x12x31x8kxex991.htm.jsonl | ff62eabdd3d1037513edc754533c1c20140d9d029aa9713e0d89283ab79659d9 | Exhibit 99.1 earnings release for fiscal Q1 2026, dated February 5, 2026 (10 chunks) |
| EX-99.1_2026-05-07_mms-2026x03x31x8kxex991.htm.jsonl | 3cc2b6ddbaacd127b88b399aaed54a4ba71be05c3b12c29939da2343ffcad4ec | Exhibit 99.1 earnings release for fiscal Q2 2026, dated May 7, 2026 (10 chunks) |
| EX-99.1_2026-08-06_mms-2026x06x30x8kxex991.htm.jsonl | 78b1fb3302628c3c36cbd9a44260145bf92a755c30565ab852ed03fa9e5e9aa0 | Exhibit 99.1 earnings release for fiscal Q3 2026, dated August 6, 2026 (9 chunks) |
| context | 427dc9f0877ed950bde305fcdd6af025bde473794c90eea607afca11f0c6cd79 | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module in this run, so there is no upstream handoff to list.

Ignored by the launcher: `_retrieval.json` (pack metadata, not issuer evidence). The host used it only to confirm filing dates and that the pack holds no presentations ("3 of 3 quarters have a release, not a presentation, on EDGAR").

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed documents and releases are enough to start all four requested downstream modules on the consolidated company, with limitations. Filed statements control; releases are attributed support. | Medium | Credit agreement text, ratings, fiscal fourth quarter results and earnings presentations are not supplied, so legal terms cannot be verified and nothing after August 6, 2026 is covered. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited fiscal 2025 statements, three quarterly reports and three releases give a continuous record from September 30, 2025 to June 30, 2026. | Debt, liquidity and cash flow work can proceed on filed figures for the quarter, nine months and fiscal 2025. | High |
| Both financial covenants, their levels, the reported ratios and the covenant EBITDA reconciliation are printed, but the Credit Agreement itself is not supplied. | Headroom can be quoted from the filings; definitions, baskets and amendment terms cannot be verified. | Medium |
| A May 27, 2026 amendment added $325 million to Term Loan B; the filing prints no other amendment terms. | The post-amendment maturity wall and pricing rest on the note tables alone. | Medium |
| Receivable sales under a bank agreement sit inside operating cash flow, and payments from a large federal customer were delayed. | Cash conversion and liquidity need a label for the receivable-sale effect and the timing of collections. | Medium |
| No ratings, earnings presentations, guarantor names or fiscal 2026 annual results are supplied. | Instrument ranking, rating view and full-year fiscal 2026 results stay as gaps. | Medium |

### Readiness view

The effective source set can support the minimum module set for MAXIMUS, INC. with limitations. All seven issuer sources are filed SEC documents or furnished earnings releases of one registrant, with text extracted from the original HTML. The audited fiscal 2025 statements, three unaudited 2026 interim filings and three releases give a continuous record from September 30, 2025 to June 30, 2026, and the latest document is dated August 6, 2026. Nothing is blocked on identity. Each of the four consumers is READY_WITH_LIMITATIONS. None is CONDITIONAL or BLOCKED. This is source sufficiency only; it does not say that downstream analysis is complete or that any model input contract is met.

### Information-availability boundary

- Every supplied document is dated on or before August 6, 2026, before the cutoff of 2026-11-05. The latest are the fiscal Q3 2026 10-Q, signed "/s/ Bruce L. Caswell August 6, 2026" (`10-Q_2026-06-30…` page:39), and the fiscal Q3 release, "Date: August 6, 2026" (`EX-99.1_2026-08-06…` page:1).
- Nothing dated between August 7, 2026 and the cutoff is supplied. That window contains the end of the fiscal year (September 30, 2026). The fiscal 2026 annual report, any fiscal fourth quarter release, and any 8-K, financing event or rating action in the window are Not supplied, not absent. The host infers, without evidence from the pack, that the fiscal 2026 10-K may fall after the cutoff because the fiscal 2025 10-K was signed on November 20, 2025 (`10-K_2025-09-30…` page:105). That inference does not establish whether any later document exists before the cutoff.
- Post-balance-sheet events in the fiscal Q3 10-Q: a quarterly dividend of $0.33 per share declared July 6, 2026, payable August 31, 2026, about $17.3 million (page:22); and "Subsequent to June 30, 2026, we have received $245 million of cash due from this customer" (page:31). The temporary contractual modification on a major federal program runs "effective July 1, 2026 through December 31, 2026" (page:27), so part of its effect falls after the balance sheet date.
- The fiscal 2025 10-K reports its own subsequent event: a dividend of $0.30 per share declared October 6, 2025 (`10-K_2025-09-30…` page:99).

### Identity and perimeter

- Reporting entity: Maximus, Inc., a Virginia corporation, "Commission file number: 1-12997", common stock listed on the New York Stock Exchange as MMS, large accelerated filer (`10-K_2025-09-30…` page:1; `10-Q_2026-06-30…` page:1). All statements are consolidated. No parent is named in the supplied text; the context parent is blank.
- Debt perimeter. The 10-K states: "The Credit Agreement is, subject to customary exceptions, secured by substantially all of our assets and all of the assets of our wholly owned material domestic subsidiaries, and guaranteed by each of our wholly owned material domestic subsidiaries" (`10-K_2025-09-30…` page:84). The guarantor entities are not named, the borrower entity is not separated from the registrant, and the restricted or unrestricted split is not stated in any supplied source. The 10-Qs do not repeat the security and guarantee sentence (a search of all three 10-Qs and the three releases for "secured by", "guaranteed by" and "guarantor" found nothing). The context guarantor list is blank. This is an unresolved perimeter gap.
- Units and currency: statements are in thousands of USD ("(in thousands, except per share amounts)", `10-Q_2026-06-30…` page:4). MD&A text and the releases mix millions, billions and thousands. Operations also run in the United Kingdom, Canada and the Middle East, and a foreign currency translation line appears in comprehensive income (page:5); statements are nonetheless presented in USD, which matches the context currency. No other reporting currency is used.
- Fiscal calendar: fiscal year ends September 30. Quarterly statements carry three-month and nine-month columns; the cash flow statement in the 10-Q is nine-month only, while the release adds a three-month cash flow column (`EX-99.1_2026-08-06…` page:7).
- Auditor: KPMG LLP, report dated "November 20, 2025", "We have served as the Company's auditor since 2024" (`10-K_2025-09-30…` page:63). The fiscal 2024 comparatives carry a separate Ernst & Young LLP report dated November 21, 2024 (page:64). Interim statements are unaudited.

### Source register

#### Form 10-K for fiscal 2025

- Family and authority: filed annual report, original authority for audited consolidated statements for the years ended September 30, 2025, 2024 and 2023. Signed November 20, 2025 (page:105).
- Located: statement of operations page:64, balance sheet pages:64 to 65, cash flows pages:65 to 66, business pages:4 to 17, risk factors pages:18 to 38, cybersecurity page:39, MD&A results page:44, backlog page:49, liquidity and cash requirements pages:50 to 54, non-GAAP measures pages:58 to 59, segment note page:78, revenue disaggregation page:80, debt note pages:83 to 84 (debt table, maturities and swaps), leases page:89, receivable-sale agreement page:94, litigation pages:96 to 97, subsequent event page:99.
- Period and basis: fiscal years ended September 30, 2025, 2024 and 2023. Page:64 heads the columns "2025 2024 2023".
- Limits: exhibits are listed by reference only (page:104); no exhibit text, including the Credit Agreement, is supplied. Part III is incorporated from a proxy statement that is not supplied (page:2).

#### Forms 10-Q for fiscal Q1, Q2 and Q3 2026

- Family and authority: filed quarterly reports with unaudited condensed consolidated statements.
- Fiscal Q3 (June 30, 2026): statement of operations page:4, comprehensive income page:5, balance sheet pages:5 to 6, cash flows page:6, segment note pages:10 to 12, revenue disaggregation page:12, divestitures page:15, debt note and maturities pages:15 to 16, swaps pages:16 to 17, fair value page:17, equity and repurchases page:19, cash and restricted cash page:19, receivable-sale agreement page:20, litigation pages:21 to 22, subsequent event page:22, results of operations pages:22 to 29, liquidity and credit facilities pages:29 to 33, free cash flow pages:33 to 34, non-GAAP pages:35 to 36, signatures page:39.
- Fiscal Q1 (December 31, 2025): debt note page:13, receivable-sale agreement page:17, covenant tables pages:28 to 29, subsequent event page:19.
- Fiscal Q2 (March 31, 2026): debt note page:14, receivable-sale agreement page:18, covenant tables pages:30 to 31, subsequent event page:20.
- Period and basis: Q1 is three months. Q2 and Q3 carry three-month and year-to-date columns for the income statement; the cash flow statements in the 10-Qs are year-to-date, so a discrete quarter needs the release or subtraction downstream. This module does not do it.

#### Earnings releases (Exhibit 99.1) for fiscal Q1, Q2 and Q3 2026

- Family and authority: issuer press releases furnished as Exhibit 99.1, unaudited and management-prepared. They give reported and adjusted figures, guidance, pipeline statistics and quarter narrative. They are attributed management claims; the 10-Q controls where the two overlap.
- Located in the fiscal Q3 release: highlights page:2, segment narrative, pipeline and leverage statement pages:3 to 4, guidance reconciliation pages:5 to 6, statements of operations page:6, balance sheet pages:6 to 7, cash flows pages:7 to 8, segment results pages:8 to 9, free cash flow and adjusted EBITDA reconciliation page:9. The Q1 release has its leverage statement on page:5 and the Q2 release on page:4.
- Non-GAAP: "adjusted EBITDA", "adjusted diluted earnings per share" and "free cash flow" are the issuer's measures. The releases say that calculation details "are included with our earnings presentation and forthcoming Form 10-Q" (`EX-99.1_2026-08-06…` page:5); no earnings presentation is supplied.

### Document relationships and conflicts

- Overlap, not independent corroboration. The fiscal Q3 release repeats the 10-Q statements. For example fiscal Q3 revenue is 1,278,971 thousand in both (`10-Q_2026-06-30…` page:4; `EX-99.1_2026-08-06…` page:6) and the balance sheets agree line by line. Treat the 10-Q as controlling and do not count the release as independent evidence.
- Two EBITDA measures. The release's adjusted EBITDA for the quarter is $192,327 thousand (`EX-99.1_2026-08-06…` page:9) and the Credit Agreement's Consolidated EBITDA for the same quarter is $210,398 thousand (`10-Q_2026-06-30…` page:33). The definitions differ ("The definition of Consolidated EBITDA requires us to include adjustments not typically included within EBITDA", page:32). Downstream modules must keep the two measures apart and label which is used. The difference is accounted for by items printed in the two reconciliations (see Calculations); no figure is reconciled here.
- Net leverage text. The release says the ratio was "2.0x" at June 30, 2026 and "1.8x at March 31, 2026" (`EX-99.1_2026-08-06…` page:4), while the 10-Qs print 2.00 and 1.75 for those dates (`10-Q_2026-06-30…` page:33; `10-Q_2026-03-31…` page:30). They agree after rounding. The ratio uses the Credit Agreement definition, not a rebuilt one.
- Liquidity text. The 10-K says "access to an additional $750.0 million through a revolving credit facility" at September 30, 2025 (page:52). The fiscal Q3 10-Q says "access to approximately $730.0 million" at June 30, 2026 while the debt table shows a $20,000 thousand revolver balance (`10-Q_2026-06-30…` pages:32, 15). The 10-K also states letters of credit of $3.0 million issued under the Credit Agreement at September 30, 2025 (page:84). No 10-Q mentions letters of credit (a search of the three 10-Qs for "letter" found nothing), so availability net of letters of credit at June 30, 2026 is not determinable. The 10-K also notes revolving credit facilities in Canada and the United Kingdom (page:83), with no size or balance, and the 10-Qs do not mention them.
- Receivable-sale capacity. The maximum amount of receivables that may be sold at one time is $250.0 million in the 10-K and the fiscal Q1 10-Q (`10-K…` page:94; `10-Q_2025-12-31…` page:17) and $350.0 million in the fiscal Q2 and Q3 10-Qs (`10-Q_2026-03-31…` page:18; `10-Q_2026-06-30…` page:20). The change falls between December 31, 2025 and March 31, 2026; the sources give no date or terms for the increase. This is a change over time, not a conflict.
- Guidance direction. Adjusted diluted EPS guidance was $8.25 to $8.55 in May 2026 (`EX-99.1_2026-05-07…` page:4) and is $7.90 to $8.20 in August 2026 (`EX-99.1_2026-08-06…` page:2). Free cash flow guidance was $450 million to $500 million in May (page:4 of that release) and is $425 million to $475 million in August (`EX-99.1_2026-08-06…` page:2). Both moved down.
- Terminology: the 10-Qs call the whole agreement the "Credit Agreement" with a Term Loan A, a Term Loan B and a Revolver. Consumers should keep them as separate instruments.

### Consumer evidence demand

| Consumer | Status | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Annual and interim statements, segments, debt, cash flow, non-GAAP | 10-K pages:64 to 66, 78 to 80, 83 to 84, 58 to 59; fiscal Q3 10-Q pages:4 to 6, 10 to 12, 15 to 17, 33 to 36; releases pages:6 to 9 of the fiscal Q3 release | Two EBITDA definitions; discrete quarter cash flows only in the releases; no trailing twelve month adjusted EBITDA printed; letters of credit and non-US facilities not quantified at June 30, 2026; text extraction flattens tables |
| CP-1A | READY_WITH_LIMITATIONS | Business, segments, customers, history, strategy, capital allocation, transactions | 10-K pages:4 to 17, 44 to 49; fiscal Q3 10-Q pages:15, 23 to 29; fiscal Q3 release pages:2 to 4 | No proxy statement or board and ownership detail (Part III incorporated by reference); no transaction documents for the May 27, 2026 amendment; nothing after August 6, 2026 |
| CP-2 | READY_WITH_LIMITATIONS | Debt stack, liquidity, covenants, interest, receivable sales, litigation, leases | 10-K pages:52 to 54, 83 to 84, 89, 94, 96 to 97; fiscal Q3 10-Q pages:15 to 17, 19 to 22, 29 to 34 | Credit Agreement, amendment and EBITDA definition not supplied; guarantors not named; no ratings; MOVEit litigation accrual amount not printed |
| CP-5 | READY_WITH_LIMITATIONS | Traceable claims across filings | All seven sources carry page chunks; the figures above are locatable | Text only; no original HTML, XBRL or images supplied for visual or table-layout checks |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Analytical read-through

- Usable coverage: the audited fiscal 2025 statements, three interim 10-Qs and three releases support a reported-basis financial foundation for fiscal Q3 2026, nine months 2026 and fiscal 2025, and a trailing twelve month view to June 30, 2026 built from fiscal 2025 plus nine months 2026 less nine months 2025, with all three components located (`10-K…` page:64; `10-Q_2026-06-30…` page:4). The Credit Agreement's own trailing twelve month Consolidated EBITDA is also printed for each quarter (page:33).
- Strongest contrary evidence: the covenant package is described only through the issuer's own disclosure. The 10-Q gives "Consolidated Net Total Leverage Ratio ... cannot exceed 4.00:1.00 ... with a step up to 4.50:1.00 under certain circumstances" and "cannot be less than 3.00:1.00" for coverage (page:32), and prints ratios of 2.00 and 8.72 (page:33). The definition of Consolidated EBITDA includes "estimated synergies from acquisitions" and "pro forma effects" (page:32), and the Credit Agreement text is not supplied. A downstream module that computes its own leverage from reported EBITDA will not match the printed ratio without the definition, and the source set cannot settle the difference.
- Source-risk mechanism, cash flow. Operating cash flow was an outflow of $179.9 million for nine months ended June 30, 2026 and is described as affected by "administrative delays on payments from one of our large contracts with the U.S. federal government" (page:31). Receivables of $1.28 billion were sold to a bank in the nine months and recorded in operating cash flows (page:20). A reader who compares operating cash flow or days sales outstanding across periods without the receivable-sale effect would misread conversion: the 10-Q reports days sales outstanding of 98 days, or 123 days "Excluding the effects of the RPA" (page:31). The $245 million collected after June 30, 2026 is a subsequent event, and the fiscal fourth quarter that would show the effect is not supplied.
- Perimeter risk: restricted cash of $96,296 thousand is held for customers within prepaid and other current assets, and the cash flow statement's ending balance of 153,249 thousand includes it while the balance sheet cash is 56,953 thousand (page:19, page:6). Liquidity work must use unrestricted cash.
- What cannot proceed: legal ranking, collateral and guarantor coverage beyond the 10-K sentence; covenant testing on Credit Agreement definitions; amendment terms; any rating-based or market-price-based view, because no ratings, quotes or peers are supplied; fiscal 2026 full-year results; anything after August 6, 2026.
- Next evidence action: supply the executed Credit Agreement with its May 27, 2026 amendment, the fiscal 2026 10-K and any fiscal Q4 release, the earnings presentations, any rating reports, and 8-K filings dated August 7, 2026 to the cutoff. Until then carry each limitation above into the modules.

## Calculations

No new calculation is made for readiness. The checks below are source tie-outs that support the document relationships recorded above. They are not normalized or reconciled figures. Amounts are in thousands of USD unless stated.

- Fiscal Q3 debt table foots (`10-Q_2026-06-30…` page:15): Term Loan A 819,375 + Term Loan B 814,173 + Revolver 20,000 = 1,653,548, which equals "Total debt principal". Less unamortized debt-issuance costs and discounts 16,613 = 1,636,935, which equals "Total debt".
- Fiscal Q3 maturity table foots (page:15): 18,952 + 75,809 + 81,434 + 690,184 + 8,309 + 778,860 = 1,653,548, equal to the principal total.
- Fiscal 2025 maturity table foots (`10-K…` page:84): 55,625 + 72,500 + 78,125 + 666,875 + 5,000 + 468,750 = 1,346,875, equal to "Total debt principal" at September 30, 2025 (page:83).
- Interest rate swap notional (`10-Q_2026-06-30…` page:16): 75,000 + 75,000 + 150,000 + 200,000 + 75,000 + 50,000 + 50,000 = 675,000, which equals the $450 million asset notional plus the $225 million liability notional in the fair value table (page:17).
- Credit Agreement EBITDA reconciliation for the trailing twelve months to June 30, 2026 (page:33): 370,887 + 89,237 − 1,676 + 120,539 + 83,791 + 35,132 + 6,914 − 9,941 + 51,258 + 52,278 = 798,419, equal to the printed Consolidated EBITDA. For fiscal 2025 (`10-K…` page:54): 319,034 + 84,080 − 640 + 125,815 + 92,047 + 41,182 + 427 + 39,549 + 41,669 + 50,832 = 793,995, equal to the printed figure.
- Printed ratios recomputed from printed inputs: (1,653,548 − 56,953) = 1,596,595; 1,596,595 / 798,419 = 2.00 (page:33). 798,419 / 91,588 = 8.72 (page:33). For fiscal 2025: (1,346,875 − 150,000) = 1,196,875; 1,196,875 / 793,995 = 1.51 (`10-K…` page:54).
- Difference between the two EBITDA measures for fiscal Q3 2026: 210,398 − 192,327 = 18,071. The Credit Agreement reconciliation shows stock compensation expense 7,356 and pro forma and other adjustments 10,715 (page:33), and 7,356 + 10,715 = 18,071. The release's adjusted EBITDA reconciliation (`EX-99.1_2026-08-06…` page:9) has no stock compensation or pro forma line. This is a tie-out of printed items, not a reconciliation of definitions.
- Revolver capacity arithmetic: 750,000 − 20,000 = 730,000, equal to the "approximately $730.0 million" access in the 10-Q (page:32). This leaves no deduction for letters of credit, which the 10-Qs do not mention.
- Cash tie: balance sheet cash 56,953 + restricted cash 96,296 = 153,249, equal to the cash flow statement ending balance (page:19, page:6). At September 30, 2025: 222,351 + 38,108 = 260,459.
- Days between the latest document and the cutoff: August 6, 2026 to November 5, 2026 is 91 days.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit Agreement text, the May 27, 2026 amendment terms (pricing, maturity, baskets) and the Consolidated EBITDA definition are not supplied; the filings state only that the amendment "increased our TLB by $325 million" (`10-Q_2026-06-30…` page:15) | High | CP-2, CP-1 | Supply the executed Credit Agreement and amendment; keep the printed 2.00 and 8.72 as attributed figures only |
| Guarantor and borrower entities not named; the security and guarantee sentence appears only in the 10-K (page:84); no restricted or unrestricted split | High | CP-2 | Supply the guarantor schedule or the agreement; carry the perimeter gap forward |
| No ratings, price quotes, peers or valuation inputs in the context or the sources (a search of all seven sources for rating-agency names found only stock index references) | Medium | CP-2 | Not required for source readiness; keep Not supplied |
| Fiscal 2026 annual report, any fiscal Q4 release and anything dated August 7, 2026 to the cutoff are not supplied | High | CP-1, CP-1A, CP-2 | Supply later filings or confirm none exist before the cutoff |
| Earnings presentations are not supplied; the pack holds releases instead ("3 of 3 quarters have a release, not a presentation") | Low | CP-1A | Supply the decks if non-GAAP calculation details or pipeline slides are needed |
| Letters of credit under the revolver are quantified only at September 30, 2025 ($3.0 million); the Canada and United Kingdom revolving facilities have no size or balance | Medium | CP-2 | Request the later disclosure; do not net or add them from these sources |
| Date and terms of the increase in the receivable-sale limit from $250.0 million to $350.0 million are not printed | Medium | CP-2 | Supply the agreement amendment |
| MOVEit litigation: the accrual is described as "an amount within a range of possible outcomes" with no amount (`10-Q_2026-06-30…` page:22); insurance recovery is not mentioned | Medium | CP-2 | Carry as an unquantified contingency |
| Performance bond commitments are quantified only at September 30, 2025 ($33.2 million, `10-K…` page:98); no 10-Q mentions performance bonds (a search of the three 10-Qs for "performance bond" found nothing) | Low | CP-2 | Carry the year-end figure as dated; request later disclosure |
| Trailing twelve month adjusted EBITDA is not printed; the release gives quarter and nine-month figures only | Low | CP-1 | Derive downstream by addition and subtraction and label the derivation |
| Discrete fiscal Q2 and Q3 cash flows are not printed in the 10-Qs (nine-month columns); the releases give the three-month column | Low | CP-1 | Use the release column and label it as attributed, or subtract downstream |
| Text extraction only; original HTML, XBRL and images not supplied; page chunks are not printed page numbers | Low | CP-1, CP-5 | Check flagged tables against filed HTML when available |
| Exhibits and the proxy statement are not supplied | Low | CP-1A | Supply if governance or ownership detail is needed |

## Next module

- CP-1: use the 10-K and 10-Q statements as controlling and the releases as attributed support. Keep thousands and millions apart. Keep fiscal year, three-month, nine-month and trailing twelve month columns separate, and state that the fiscal year ends September 30. Label the two EBITDA measures. Do not net revolver capacity for letters of credit. Show cash and restricted cash separately.
- CP-1A: describe the business from the 10-K and the fiscal Q3 10-Q and attribute the releases. Carry the temporary contractual modification, the child support divestiture of December 2025 and the Australia and Korea divestiture of December 2024 from the notes. Label anything after August 6, 2026 as Not supplied.
- CP-2: list the instruments from the debt tables (Term Loan A, Term Loan B, Revolver, and the receivable-sale agreement as an off-balance-sheet financing) and carry the missing Credit Agreement, amendment, guarantor detail and covenant definition as restrictions. Quote covenant levels and reported ratios as attributed.
- CP-5: all claims can be traced to page chunks. Keep the extraction-only, release-versus-filing and covenant-definition limits visible.
