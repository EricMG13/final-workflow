## Request

Issuer: PRECISION DRILLING Corp (issuer id pds; registrant "PRECISION DRILLING CORPORATION", Alberta, Canada; ticker PDS). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency per the run context: CAD. Current period: Q3 2026. Prior period: FY2025.

Question for this module: can the effective source set support the requested work, and what remains blocked? This module gives no credit conclusion, no legal interpretation and no investment opinion, and it does not normalize, reconcile or calculate figures. It separates source sufficiency from completion of downstream analysis.

Selected consumers: CP-1 (financial extraction), CP-1A (business and transaction context), CP-2 (fundamental credit synthesis), CP-5 (evidence trace review). Report sections this run feeds: key findings, company operating model, model chart strip, financials and credit metrics, strengths and weaknesses, company profile, transaction summary.

The run context supplies identity (issuer name, ticker, sector, country), the dates, the currency and the periods. It is a settings file, not issuer evidence. Its blank fields (borrower, parent, guarantors, sponsor, ratings, quotes, deal terms, peers, market values) are unknowns, not zeros.

## Sources

### Issuer sources relied on

Each file below is a text extraction of an SEC filing. Page numbers in this handoff are the extraction chunks shown as `page:N`, not printed page numbers. The sha256 is that of the pinned extraction file.

| Source (exact name) | sha256 | Pages | Document family and authority |
| --- | --- | --- | --- |
| 40-F_2025-12-31_pds-20251231.htm.jsonl | 370dd908e02517a9c6fdef15ebd1f7cb116b5559c399f640ba611cac38448995 | 4 | Form 40-F annual report cover, signed by the registrant; wrapper only, its exhibits are not in the pack |
| 6-K-EX-99.1_2026-03-31_exh_991.htm.jsonl | dea56c7134da9a355171c554a1de2c864262ee500671edb8950e5a8046055900 | 16 | First quarter 2026 interim report (management discussion, measures, liquidity); issuer narrative |
| 6-K-EX-99.1_2026-07-28_exh_991.htm.jsonl | 36192463cc83167a35ad5734c404a3c626d50b0ad4594b8a7f2194bea3a8cff9 | 18 | Second quarter 2026 press release with embedded unaudited statements; issuer narrative plus statements |
| 6-K-EX-99.1_2026-10-27_exh_991.htm.jsonl | fee608b6431a2965784fc76b2de265f5506a117164e5844d50a088bea40f38a4 | 20 | Third quarter 2026 interim report dated October 27, 2026 (management discussion, liquidity, covenants, contingencies) |
| 6-K-EX-99.2_2026-03-31_exh_992.htm.jsonl | d96a5e5808d43b7099d6d8e58ef62238fb3bf3aa05ae6b50ff5d6edaea1184fb | 10 | Unaudited condensed interim statements and notes, quarter ended March 31, 2026 |
| 6-K-EX-99.2_2026-06-30_exh_992.htm.jsonl | d0dc4f680eda414a6085125595dd65a3350a1093a614c44804e7f758bd709179 | 13 | Unaudited condensed interim statements and notes, six months ended June 30, 2026 |
| 6-K-EX-99.2_2026-10-27_exh_992.htm.jsonl | 2be96c22c1511c1bfacc2dbbfc1299a96c6051c24999485cd2efd4fef772c85e | 13 | Unaudited condensed interim statements and notes, nine months ended September 30, 2026 |

Coverage count: 7 of 7 issuer files, 94 pages in total. The run context (sha256 f0dfb9848210a0a45d246b6d35647f4b02f9221b88bb774a3f1ed2c749bd4a06) is settings, not evidence. The retrieval index file in the pack was ignored by CP-OS and is not a source.

### Supplied handoffs

None. CP-0 is the first module of this run and no upstream handoff exists.

### Coverage actually inspected

The 40-F cover, the Q3 2026 interim report (20 of 20 pages) and the Q3 2026 statements and notes (13 of 13 pages) were read in full. For the Q1 2026 report, the Q2 2026 release, the Q1 2026 statements and the Q2 2026 statements (57 pages), this assessment read the headline pages and searched every page for debt, liquidity, covenant, audit, approval, subsequent-event, restatement, amendment and guarantee terms, and opened each locator cited below. The remaining pages of those four files are retained evidence but were not individually read here; they are listed as a limitation in Gaps.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings support quarterly financial, debt, liquidity and covenant work on Precision Drilling through Q3 2026, with CAD statements and segment detail. They do not include the audited FY2025 statements, legal debt documents or ratings. | Medium | No audited annual statements or debt agreements are supplied, so terms such as guarantors, security and redemption rights rest on summary disclosure only. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Three quarters of unaudited 2026 statements and notes are supplied, with the prior year-end balance sheet as the only year-end comparative. | Quarterly leverage, liquidity and cash flow work can proceed; full-year FY2025 earnings and cash flow cannot be taken from statements. | High |
| The 40-F is a cover wrapper; its annual information form, annual report and audited statements are not in the pack. | Audited FY2025 figures, annual debt maturity detail and annual risk disclosure remain unsupported. | High |
| Debt is disclosed only as summary tables and notes: one senior credit facility and one series of unsecured senior notes. | Instrument terms beyond the tables, including guarantors and security, cannot be confirmed from filings supplied. | Medium |
| The 40-F names one auditor while the interim reports name another. | Unresolved; the audit-quality and engagement history for FY2025 cannot be established from this pack. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for each selected consumer. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. The pack gives the owner of each selected module a located, filed evidence base for the current period (Q3 2026 and the interim periods leading to it): consolidated statements, segment tables, a debt note with facility-level carrying values, a covenant table, a liquidity table, a contingency note and a capital commitment note. The strongest contrary evidence is that none of the audited FY2025 documents named on the 40-F exhibit list are in the pack, no executed financing document is supplied, and no rating or market-price source is supplied. Source risk mechanism: where a downstream module needs an annual period or a legal term, it can only quote management summaries, which are attributed supporting claims and cannot override a filed statement or an executed agreement. No consumer is CONDITIONAL or BLOCKED because each owner can perform its method with bounded gaps; the gaps below must be carried into every downstream answer.

### Source-by-source assessment

| Source | Entity and perimeter | Period and basis | Version relationship | Located evidence |
| --- | --- | --- | --- | --- |
| 40-F | Registrant "PRECISION DRILLING CORPORATION" (Alberta); `Commission file number: 001-14534` (page:1) | Fiscal year ended December 31, 2025; signed `Date: March 9, 2026` (page:4) | Annual report wrapper; exhibits 99.1 to 99.4 listed on page:4 but not supplied | Lists `99.3` `Consolidated Financial Statements for the fiscal year ended December 31, 2025.` (page:4) |
| Q1 2026 report (99.1) | Consolidated Precision Drilling Corporation, two segments | Three months ended March 31, 2026 versus 2025; IFRS measures plus non-IFRS Adjusted EBITDA | Distinct from the Q1 statements (99.2); contains no statements itself | Liquidity table (page:9), covenant table (page:10) |
| Q2 2026 release (99.1) | Consolidated, two segments | Three and six months ended June 30, 2026; unaudited | Embeds the Q2 statements (pages 15 to 18) that duplicate the Q2 99.2 statements; no notes, no liquidity table, no covenant table | `Precision Drilling Announces 2026 Second Quarter Unaudited Financial Statements` (page:1) |
| Q3 2026 report (99.1) | Consolidated, two segments plus Corporate and Other | Three and nine months ended September 30, 2026 versus 2025; dated October 27, 2026 | Latest MD&A; supersedes Q1 and Q2 for current-period facts but does not replace them as the record for those dates | Liquidity (pages 12 and 13), covenants (page:13), contingencies (pages 11 and 12) |
| Q1 2026 statements (99.2) | Consolidated, includes non-controlling interest | March 31, 2026 versus December 31, 2025; `approved by the Board of Directors on April 29, 2026` (page:4) | Controlling source for Q1 statements and notes | Debt note (page:6) |
| Q2 2026 statements (99.2) | Consolidated | June 30, 2026; `approved by the Board of Directors on July 28, 2026` (page:4) | Controlling source for Q2 statements and notes; duplicate content in the Q2 release is contained within it | Debt note (page:8) |
| Q3 2026 statements (99.2) | Consolidated | September 30, 2026; `approved by the Board of Directors on October 27, 2026` (page:4) | Controlling source for Q3 statements and notes | Debt note (pages 8 and 9), contingencies (page:12) |

### Evidence needed by the selected consumers

| Consumer | Evidence demand | Located in pack | Status |
| --- | --- | --- | --- |
| CP-1 financial extraction | Statements, notes, period labels, segments, debt, liquidity, covenants, cash flows | Q3 statements pages 1 to 3; debt note page:8 and page:9; covenant table page:9; interest paid and income taxes paid in the cash flow statement page:2 | READY_WITH_LIMITATIONS: no audited FY2025 income statement or cash flow; year-end comparative is the balance sheet only |
| CP-1A business and transaction context | Business model, ownership, transaction structure, history | Business note `NOTE 1. DESCRIPTION OF BUSINESS` (page:4 of the Q3 statements); strategy, outlook and contracts (pages 5 to 8 of the Q3 report) | READY_WITH_LIMITATIONS: no annual information form; no ownership or sponsor information; no transaction document |
| CP-2 fundamental credit synthesis | Settled upstream registers | Depends on the CP-1 and CP-1A handoffs; not a source-readiness condition | READY_WITH_LIMITATIONS: carries every gap below |
| CP-5 evidence trace | Locatable evidence behind each claim | All seven files retained with page locators | READY_WITH_LIMITATIONS: cannot trace any claim to an executed financing document or audited annual statement |

### Discrete periods, segments and debt items available for the model and credit-metric sections

These items are source sufficiency only; no normalization or reconciliation is asserted.

| Item | Available | Evidence locator |
| --- | --- | --- |
| Discrete quarters | Quarterly revenue, Adjusted EBITDA, net earnings, per-share and cash from operations for eight quarters from Q4 2024 to Q3 2026 | Q3 report page:14 `QUARTERLY FINANCIAL SUMMARY` |
| Quarter versus year to date | Three and nine month columns for 2026 and 2025 | Q3 statements page:2; Q3 report page:2 |
| Fiscal years | FY2025 annual income statement and cash flow: not supplied. Dec 31, 2025 balance sheet column only. FY2025 average commodity prices only | Q3 statements page:1; Q3 report pages 8 and 9 |
| Segments | Contract Drilling Services, Completion and Production Services, Corporate and Other, with revenue, Adjusted EBITDA, depreciation, taxes, assets and capital expenditures | Q3 statements pages 7 and 8 |
| Adjusted EBITDA add-backs | Reconciliation from Adjusted EBITDA to net earnings | Q3 report page:17 |
| KPIs | Rig counts, utilization days, revenue and operating cost per utilization day, term contracts | Q3 report pages 3 and 8 |
| Facility-level debt | Senior credit facility drawn amount and unsecured senior notes by series with carrying values and unamortized issue costs | Q3 statements pages 8 and 9 |
| Cash paid for interest and tax | Interest paid and income taxes paid lines | Q3 statements page:2 |
| Business and transaction narrative | Strategy, outlook, contracts, capital budget, buybacks, debt reduction target | Q3 report pages 5 to 8 |

### Debt, liquidity and covenant evidence located

- Debt note: the Q3 statements list `Senior Credit Facility:` borrowings and `6.875% senior notes due 2029` and reconcile the movement in long-term debt (pages 8 and 9). No current portion of long-term debt line appears on the balance sheet (page:1).
- Liquidity table: Q3 report pages 12 and 13 give the facility, its availability and maturity. The senior credit facility matures `October 31, 2028`, with a footnote that `US$43 million will expire on June 28, 2027.` (page:13). The operating and demand letter of credit facilities are secured; the senior notes are unsecured, per the same table.
- Covenants: the senior credit facility tests a leverage ratio of senior secured debt to covenant EBITDA and an interest coverage ratio, with reported values in the covenant table (Q3 report page:13 and Q3 statements page:9). The notes carry an incurrence-based interest coverage test described on page:13 of the Q3 report. Reported covenant values exist for March 31, 2026 (page:10 of the Q1 report), June 30, 2026 (page:8 of the Q2 statements) and September 30, 2026.
- Fair value of the notes is disclosed in Note 11 (page:11 of the Q3 statements).
- Contingency: a Canada Revenue Agency reassessment matter with a stated maximum exposure and a requirement to pay part of any assessed amount while contested is described in the Q3 report (pages 11 and 12) and in Note 12 of the Q3 statements (pages 12 and 13). It first appears as a subsequent event in the Q2 release (page:6).
- Capital commitments are in Note 10 (page:11 of the Q3 statements) and the Q3 report (page:8).

### Conflicts and anomalies in the sources

| Item | Evidence | Downstream effect |
| --- | --- | --- |
| Auditor name differs | The 40-F states `KPMG LLP, the independent registered public accounting firm that audited` the FY2025 statements (page:2). The interim reports list `PricewaterhouseCoopers LLP` under auditors (Q1 statements page:10, Q2 statements page:13, Q3 statements page:13). | Not resolved by the pack. CP-1A and CP-5 must not state an auditor or an auditor change as fact; carry as an open governance question. |
| Q2 2026 per-share anomaly | Q2 statements page:2 and Q2 release pages 4 and 16 show basic `(0.09 )` but diluted `(0.52 )` per share for a net loss, with diluted weighted shares above basic (Q2 release page:4). Q3 report page:14 repeats the figures. | Per-share figures for Q2 2026 are unreliable for use until the issuer's basis is confirmed; no credit metric in this run depends on them. |
| File labels versus content | File names carry dates such as 2026-03-31 and 2026-06-30 that are not the approval or release dates: the Q1 statements were approved on April 29, 2026 and the Q2 statements on July 28, 2026 (page:4 of each). | Periods and dates were taken from document content, not file names. |

## Calculations

None. CP-0 does not calculate, normalize or reconcile figures. Counts reported above (7 of 7 files, 94 pages: 4, 16, 18, 20, 10, 13 and 13) are source coverage counts, not analytical figures.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Audited FY2025 financial statements, annual MD&A and annual information form are not supplied; the 40-F lists them as exhibits 99.1, 99.2 and 99.3 (page:4) but the pack holds only the cover. | High | CP-1, CP-1A, CP-2, CP-5, financials and credit metrics, model chart strip | Add the 40-F exhibits. Until then FY2025 figures are Not supplied; only the December 31, 2025 balance sheet column, Q4 2025 quarterly summary lines and FY2025 average commodity prices are available. |
| Executed debt documents (credit agreement, note indenture) are not supplied. Guarantors, issuer and borrower entities, security package, redemption terms, covenant definitions (consolidated covenant EBITDA) and the restricted group are Not supplied; the filings describe them only in summary. | High | CP-1, CP-2, CP-5, transaction summary | Add the credit agreement, amendments and indenture. Summary disclosure must not be treated as the legal terms. |
| Ratings, market prices for debt and equity-market values are Not supplied; the context leaves them blank. | Medium | CP-2, relative-value style sections (omitted from this run) | None needed for the omitted sections; carry as Not supplied. |
| Q1 2026 report, Q2 2026 release, Q1 statements and Q2 statements were checked by targeted search and locator opening, not read page by page in this assessment (57 pages). | Low | CP-1, CP-5 | Downstream modules open any page they cite. |
| Per-share anomaly for Q2 2026 (see conflicts table). | Low | CP-1 | Do not use Q2 2026 per-share data. |
| Auditor name conflict (see conflicts table). | Low | CP-1A, CP-5 | Obtain the audit report and consent in the 40-F exhibits. |
| Ownership, parent, sponsor and control information is Not supplied; the context lists none and the filings supplied do not describe a controlling holder. | Medium | CP-1A, transaction summary | Add the annual information form or proxy circular if control matters. |
| Currency and unit basis: statements are in thousands of Canadian dollars; the MD&A rounds to millions; some segment metrics and the senior credit facility and notes are US dollar. No conflict with the context currency, but United States dollar debt is translated at period-end rates, so Canadian dollar carrying values move with exchange rates. | Low | CP-1, CP-2 | Downstream modules label currency on every figure. |
| All statements supplied are unaudited interim statements; no audit or review report for any interim period is supplied. | Medium | CP-1, CP-5 | Treat as unaudited management-prepared interim information. |
| Extraction fidelity: charts and images are not represented in the text extraction; the Q3 report contracts chart (page:7) is represented by its table (page:8) only. | Low | CP-1A | Do not claim chart inspection. |

## Next module

Proceed to CP-1 (financial extraction) on the Q3 2026 statements and report, carrying the gaps above, in particular: FY2025 income statement and cash flow Not supplied; unaudited interim basis; no legal debt terms; Q2 2026 per-share anomaly; and the auditor-name conflict. CP-1A should draw business and strategy facts from the Q3 report pages 5 to 8 and treat management outlook as attributed claims. CP-2 and CP-5 follow once their upstream handoffs exist.
