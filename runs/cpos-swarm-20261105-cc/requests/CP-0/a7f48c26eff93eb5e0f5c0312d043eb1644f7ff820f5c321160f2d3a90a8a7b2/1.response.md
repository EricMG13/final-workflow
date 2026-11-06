## Request

Issuer: Chemours Co (The Chemours Company, Delaware, NYSE: CC, issuer id cc). As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, dollars in millions as the filings print them. Current period: Q3 2026 (three months and nine months ended 2026-09-30); prior period: FY2025.

Question for this module: can the supplied source set support the requested downstream work (the leverage, interest-cover, liquidity and debt-maturity data module; the business and transaction context module; the fundamental credit synthesis; the evidence-trace validation), and what remains blocked or limited? This is a source-readiness assessment only. It gives no credit conclusion, no legal interpretation and no investment opinion, and it does not normalize or reconcile figures. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

Perimeter: the reporting entity is The Chemours Company and its consolidated subsidiaries (10-K page:1; 10-Q Q3 2026 page:7). The context names no borrower, parent, guarantor, sponsor or deal terms, and attaches no portfolio workbook, management bridge or legal documents (context: legal_documents "none"). Context values left blank (ratings, quotes, valuation inputs) are not treated as zero.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Document family and authority | Entity and period |
| --- | --- | --- | --- |
| 10-K_2025-12-31_cc-20251231.htm.jsonl | adf80f4588f501b9f797e1b55a5853888465c5d9b30aef8ff07b3cd4340b3957 | Annual report on Form 10-K, 324 text pages; filed statements, controlling for FY2025 facts | The Chemours Company, consolidated, fiscal year ended 2025-12-31 (filed 2026-02-24 per the pack index) |
| 10-Q_2026-03-31_cc-20260331.htm.jsonl | 544e858f14516405499b0793277b117ab856893d213de4bfdfd312ae33ddb9fd | Quarterly report on Form 10-Q, 166 text pages; filed statements | Consolidated, quarter ended 2026-03-31 |
| 10-Q_2026-06-30_cc-20260630.htm.jsonl | 5934bf743b44e940824956ac90d2979f28da0477a0f669044693e5e59c78b62f | Quarterly report on Form 10-Q, 179 text pages; filed statements | Consolidated, quarter and six months ended 2026-06-30 |
| 10-Q_2026-09-30_cc-20260930.htm.jsonl | f23013a765ad5943b395240230ccfbe7a0cca417e186c8a1a82b34a215485de7 | Quarterly report on Form 10-Q, 193 text pages; filed statements; filed 2026-11-05, the cutoff date, per the pack index | Consolidated, quarter and nine months ended 2026-09-30 |
| EX-99.1_2026-05-05_cc-ex99_1.htm.jsonl | cf37012a81481ef001a376d207312af6444e1ec5683c9d45ff930f84bd36dd4e | Earnings release (Exhibit 99.1), 17 text pages; management document, attributed supporting claims | Consolidated and segments, Q1 2026 |
| EX-99.1_2026-08-04_cc-ex99_1.htm.jsonl | 5e0a77f0453e40d6a00670f0f971f2e2c0487e12a68a0222858c84133578166e | Earnings release (Exhibit 99.1), 17 text pages; management document | Consolidated and segments, Q2 2026 |
| EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | d716a94a423338ae97b02c515014fccad1457c8952131fe6a67cf2f82a22b1e0 | Earnings release (Exhibit 99.1), 18 text pages; management document | Consolidated and segments, Q3 2026 |

### Run context

| Source | sha256 | Use |
| --- | --- | --- |
| context (1627223-chemours-co-cc.json) | e4e3509e830ce866831093e05761a30c7677098a166e3ae01f6bf5702202686d | Dated run settings and inputs; not issuer evidence |

### Supplied handoffs

None. CP-0 is the first module in this run; no upstream handoff exists. The pack index file `_retrieval.json` is ignored by CP-OS and is not evidence.

### Source profile and original authority

- Filed statements (10-K, three 10-Qs) control their respective facts. The three releases give attributed management claims and non-GAAP figures. A management claim does not override a filing.
- The pack holds no presentation decks (the index lists releases "instead of presentations"), no credit agreement, no indentures, no guarantor schedule, no legal settlement or consent-decree documents. The only financing and legal evidence is therefore the issuer's own description in the filings.
- Version relationships: the 10-K and each 10-Q are separate periodic reports, not amendments of one another. Prior-period amounts in the 2026 filings are labelled revised (see Gaps), so the 2026 10-Qs and releases carry the controlling revised FY2025 and 2025-quarter comparatives. No duplicate documents were found among the seven sources.
- Extraction fidelity: all seven are text extractions in page-sized chunks (`page:N` is a chunk, not a printed page). Tables are flattened to one cell per line. No chart, image or speaker note was inspected, and a successful extraction is not a fidelity review.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases cover statements, debt, liquidity, segments and legal exposure for a leverage, liquidity and context review to Q3 2026. All four downstream modules can run, each with bounded gaps. | Medium | No credit agreement or indenture is supplied, so covenant tests, guarantors and the revolver after its October 2026 maturity are not verifiable. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt, cash, revolver availability and a maturity table are printed at 2026-09-30 and 2025-12-31, so the leverage and liquidity data can be built from filed figures. | Debt and liquidity figures can be traced to filings. | High |
| A $220 million revolving tranche matured on October 7, 2026, after the balance-sheet date, and the sources do not say whether it was extended or replaced. | Reported availability of $953 million may overstate liquidity after that date. | Medium |
| Interim cash interest paid is not printed; only FY2025 shows it. | A cash-basis interest cover for the last twelve months to Q3 2026 cannot be built from the pack. | High |
| The covenant level is printed only as a 2.00 to 1.00 maximum senior secured net leverage ratio, with no reported ratio or headroom. | Covenant headroom needs the Credit Agreement definitions, which are not supplied. | High |
| Prior-year amounts were revised, and one prior-period Adjusted EBITDA figure does not tie between the filing components and the release. | Period comparisons need a stated basis and a documented conflict. | Medium |

### Readiness view

Source sufficiency is READY_WITH_LIMITATIONS for all four selected consumers: the financial data and ratio module (CP-1), the business and transaction context module (CP-1A), the fundamental credit synthesis (CP-2) and the evidence-trace validator (CP-5). No consumer is CONDITIONAL or BLOCKED, because no missing source prevents any consumer's own method and no critical identity boundary is unresolved: the reporting entity is the consolidated registrant, named identically on the cover of every filing. The limitations below are carried into each consumer and are source gaps, not findings about downstream analysis, which is not yet done.

### Coverage of the requested work

| Evidence need | Located in the pack | Assessment |
| --- | --- | --- |
| Income statement, balance sheet, cash flow, equity | 10-K pages 160-162; 10-Q Q3 pages 2-6 (nine-month and three-month; balance sheet at 2026-09-30 versus 2025-12-31) | Adequate; filed |
| Discrete quarters and year-to-date | 10-K Note 30 page:319 prints Q1-Q4 2025 and 2024 income statement lines; the 10-Qs print three-month and year-to-date columns; the three releases print the quarter, the prior-year quarter and the prior quarter | Adequate for sales and income lines; see Gaps for Adjusted EBITDA |
| Segments and KPIs | 10-K Note 29 page:314; 10-Q Q3 Note 23 pages 130-133; release page:3-4 (net sales, Adjusted EBITDA and margin by segment, sub-product sales) | Adequate; Adjusted EBITDA is a management measure defined in the notes |
| Facility-level debt and carrying values | 10-Q Q3 Note 15 pages 23-30 (debt table, maturities, fair values); 10-K Note 20 pages 208-220 | Adequate; each tranche printed with principal, rate or margin, maturity |
| Liquidity, revolver, letters of credit | 10-Q Q3 page:149 (unrestricted cash $698 million; availability $953 million net of $47 million letters of credit) and page:26; release page:4 | Adequate with the maturity caveat in Gaps |
| Covenants | 10-K page:211 (maximum senior secured net leverage ratio of 2.00 to 1.00); 10-Q Q3 page:149 (in compliance, tests based on last twelve months EBITDA and senior secured net debt) | Level printed; reported ratio and definitions not supplied |
| Cash-paid interest and tax | 10-K page:163 (FY2025 only) | Not printed for 2026 interim periods |
| Off-debt claims | Leases 10-K Note 14 page:202; receivables securitization and supplier financing 10-Q Q3 pages 20, 22, 27, 150; environmental and PFAS liabilities 10-Q Q3 Note 17 pages 31-120 and balance sheet page:3; pensions 10-Q Q3 Note 21 page:129 and 10-K Note 27 page:307 | Described by the issuer; underlying legal documents absent |
| Business and transaction narrative | 10-K Item 1 and MD&A; 10-Q Q3 page:6 (Note 1), page:151; release pages 1-6 | Adequate for an operating-company profile; no sponsor or buyout transaction exists in the sources |

### Source-by-source assessment

- **10-K FY2025.** Entity: The Chemours Company, Commission File Number 001-36794 (page:1). Covers three years of statements (page:160-162), debt Note 20 (page:208), commitments and contingent liabilities Note 22 (page:221), long-term employee benefits Note 27 (page:307), supplemental cash flow Note 28 (page:313, cash and restricted cash reconciliation; cash paid for interest and taxes at page:163) and segment Note 29 (page:314). It carries the revision of previously issued financial statements (page:165). Quote at page:211: "maximum senior secured net leverage ratio of 2.00 to 1.00".
- **10-Q Q1 2026.** Same entity; three months ended 2026-03-31. Debt Note 15 at page:19, liquidity at page:124, segments at page:110. The debt maturities paragraph at page:24 states "The Company is not required to make additional principal payments in 2025", which sits oddly in a 2026 filing; the Q2 and Q3 filings say 2026 (page:29 and page:30). Treated as a wording inconsistency, not a conflict of figures.
- **10-Q Q2 2026.** Same entity; three and six months ended 2026-06-30. Debt Note 15 at page:23, liquidity at page:135, segments at page:119. At page:136 it records Moody's downgrade to B1 from Ba3 on July 17, 2026.
- **10-Q Q3 2026.** Same entity; three and nine months ended 2026-09-30; 150,534,489 shares outstanding at November 2, 2026 (page:1). Income statement page:2 (net sales $1,540 for the quarter and $4,512 for nine months), balance sheet page:3, cash flow pages 5-6, debt Note 15 pages 23-30, segments pages 130-133, liquidity pages 148-151. Footnote on page:2: SG&A includes "$150 received by the Company related to the PFAS Insurance MOU".
- **Releases.** Each release is a management summary of one quarter with a non-GAAP reconciliation (Q3: pages 12-13). They give Adjusted EBITDA, Adjusted Net Income, free cash flow, a net leverage ratio of approximately 4.3x and a Full Year 2026 Outlook (pages 5-6). Attributed management claims only; the net leverage ratio is management's definition (total debt principal less unrestricted cash over Adjusted EBITDA).

### Source-risk mechanisms and downstream consequences

- **Revolver maturity.** Evidence: the 10-Q states "$220 million in revolving commitments that matured on October 7, 2026" (page:149), while the $953 million availability is measured at September 30, 2026, before that date. Mechanism: the headline liquidity figure includes a tranche that expired five weeks later, and the sources do not say whether it was extended, replaced or lapsed. Consequence: the liquidity data module must show availability at the balance-sheet date and flag the post-balance-sheet change, and cannot state post-October availability.
- **Interest cover basis.** Evidence: cash paid for interest is printed for FY2025 only (10-K page:163); the interim cash flow statements print only non-cash items in the supplemental section (10-Q Q3 page:6). Mechanism: net interest expense is available for every period, cash interest is not. Consequence: any 2026 interest cover must be labelled as based on interest expense, net, not cash interest.
- **Covenant headroom.** Evidence: a 2.00 to 1.00 maximum is printed (10-K page:211), the Third Amendment is said to have "increased the maximum senior secured net leverage ratio quarterly maintenance test through the fiscal quarter ended September 30, 2026" (10-Q Q3 page:25), but neither the temporary level nor the reported ratio is printed. Mechanism: the Credit Agreement definitions of EBITDA and senior secured net debt differ from the Adjusted EBITDA and total debt principal used in the release. Consequence: headroom cannot be computed from the pack and must be written Not calculable.
- **Revised comparatives.** Evidence: prior-period amounts were revised for immaterial errors related primarily to income tax expense timing (10-Q Q3 page:7-8; 10-K page:165). Mechanism: 2025 figures in the 2026 filings differ from the originally reported 2025 filings, which are not in the pack. Consequence: year-over-year and LTM figures must use the revised comparatives and say so.

## Calculations

No new analytical calculation is made in this module. The checks below only test whether printed figures tie, to find source conflicts; their results are not normalized figures.

| Check | Inputs (with locator) | Result | Printed comparison |
| --- | --- | --- | --- |
| Nine months 2026 Adjusted EBITDA from 10-Q components | Segment Adjusted EBITDA 746, other non-reportable 6, corporate expenses (136); 10-Q Q3 page:133 | 746 + 6 - 136 = 616 | Release page:13 prints 616. Ties. |
| Three months 2026 Adjusted EBITDA from 10-Q components | 245, 1, (46); 10-Q Q3 page:133 | 245 + 1 - 46 = 200 | Release prints 200. Ties. |
| Nine months 2025 Adjusted EBITDA from 10-Q components | 760, 7, (148); 10-Q Q3 page:133 | 760 + 7 - 148 = 619 | Release page:13 prints 614. Differs by 5. |
| Three months 2025 Adjusted EBITDA from 10-Q components | 233, 2, (45); 10-Q Q3 page:133 | 233 + 2 - 45 = 190 | Release prints 189. Differs by 1. |
| Net debt tie-out | Total debt principal 3,872 less unrestricted cash 698; 10-Q Q3 page:24 and page:149 | 3,872 - 698 = 3,174 | Release page:13 prints 3,174. Ties. |
| Liquidity tie-out | Cash 698 plus revolver availability 953 (1,000 commitments less 47 letters of credit); 10-Q Q3 page:149, page:26 | 698 + 953 = 1,651 | Release page:4 prints "$1.7 billion". Ties after rounding. |
| Restricted cash tie-out | Current 41 plus non-current 62; 10-Q Q3 page:3 | 41 + 62 = 103 | Release page:2 footnote: "Restricted cash approximated $103 million". Ties. |

The two Adjusted EBITDA differences are logged as a conflict in Gaps. The 10-Q does not print a consolidated Adjusted EBITDA total, so the 10-Q-side totals above are sums of printed components, not printed figures.

## Gaps

| # | Gap or conflict | Severity | Affected consumers | Locator and detail | Remediation |
| --- | --- | --- | --- | --- | --- |
| 1 | Revolving tranche of $220 million matured on October 7, 2026; availability of $953 million is stated at 2026-09-30; no source says whether it was extended or replaced. A subsequent event within the filing, before the cutoff. | High | Liquidity data, synthesis, trace | 10-Q Q3 page:149, page:25, page:26 | Show availability at the balance-sheet date and flag the subsequent maturity; look for an 8-K or amendment after 2026-11-05 only outside this cutoff. |
| 2 | Covenant: temporary senior secured net leverage maximum under the Third Amendment, reported ratio, headroom and Credit Agreement EBITDA and senior secured net debt definitions not supplied. Level printed: 2.00 to 1.00. | High | Financial data, synthesis | 10-K page:211; 10-Q Q3 page:25, page:149 | Obtain the Credit Agreement and Amendments 1-4. Until then write Not calculable. |
| 3 | Cash-paid interest and income taxes not printed for 2026 interim periods or the last twelve months to Q3 2026. FY2025 printed. | Medium | Financial data (interest cover) | 10-K page:163; absent from 10-Q Q1, Q2 and Q3 supplemental cash flow (Q3 page:6, page:129) | Label interest cover as based on interest expense, net; request the interim cash interest data. |
| 4 | Conflict: nine-month 2025 Adjusted EBITDA is 614 in the Q3 2026 release and 619 as the sum of printed 10-Q components; three-month 2025 is 189 versus 190. The same release prints 2025 depreciation and amortization of 236 for nine months while the 10-Q prints 239 for 2026 and 259 for 2025 (page:133), and restructuring of 54 versus 31, so definitions differ between documents. | Medium | Financial data (LTM EBITDA, leverage trend), trace | Release page:13; 10-Q Q3 page:133 | Do not choose or average. Quote both, use the filing for statement lines and the release only as an attributed management measure, and let the next module disclose its basis. |
| 5 | Prior-period amounts revised for immaterial errors (income tax timing and cost of goods sold timing); originally reported 2025 filings are not in the pack. | Medium | Financial data, trace | 10-Q Q3 page:7-8; 10-K page:165, page:319 | Use revised comparatives only; label them revised. |
| 6 | Discrete Q4 2025: the 10-K quarterly note prints sales and income lines (page:319) but no Q4 2025 Adjusted EBITDA or segment data, and no Q4 2025 release is in the pack (earliest release 2026-05-05). | Medium | Financial data (quarterly series) | 10-K page:319; pack index | Treat Q4 2025 Adjusted EBITDA as Not supplied; any derivation from FY2025 and nine-month figures must be shown as a calculation with the basis conflict in item 4. |
| 7 | Guarantors not named; no indenture, credit agreement, guarantor schedule (Exhibit 22) or collateral documents. The notes refer to "the guarantor named therein" and the 10-K says debt is the obligation of the company "and our guarantor subsidiaries" and that "a significant portion of our operations are conducted by non-guarantor subsidiaries". No guarantor or non-guarantor financial data. | Medium | Financial data, context, synthesis | 10-Q Q3 page:27; 10-K page:62 | Obtain indentures and the guarantor list. The perimeter used is the consolidated registrant. |
| 8 | Legal documents for PFAS and environmental matters (PFAS MOU, New Jersey judicial consent order, North Carolina settlement, 2026 Consent Decree) are not in the pack; only the filings' summaries. Amounts and payment schedules cannot be checked against executed documents. | Medium | Business context, synthesis, trace | 10-Q Q3 pages 31-120 (Note 17); balance sheet page:3 (current environmental remediation 116, long-term 689; accrued litigation 362 at page:30) | Treat the filings as the controlling description; cite Note 17 locators; request the executed documents. |
| 9 | No presentation decks. The releases refer to a "2025 Earnings Presentation" that is not supplied. No chart, image or speaker-note content inspected; table fidelity not reviewed beyond text extraction. | Low | All | Release page:2; extraction note above | Record as a parse limit; no claim of chart coverage. |
| 10 | Ratings: the context lists none. The 10-Q records Moody's downgrade to B1 from Ba3 on July 17, 2026 (Q3 page:149; Q2 page:136) and an S&P BB- affirmation dated April 16, 2025 with negative outlook, which is older than the other evidence. No agency report supplied. | Low | Context, synthesis | 10-Q Q3 page:149 | Label as issuer-reported; request current agency reports. |
| 11 | Management-attributed items: net leverage ratio of approximately 4.3x, total liquidity of $1.7 billion and the Full Year 2026 outlook are release claims on management definitions. | Low | Financial data, synthesis | Release Q3 page:4-6 | Attribute to management; do not treat as filed facts. |
| 12 | Timing: the Q3 2026 10-Q was filed on 2026-11-05, the cutoff date; the Q3 release is dated 2026-11-02. Both are within the cutoff. Nothing dated after 2026-11-05 is relied on. | Low | All | Pack index; 10-Q Q3 page:1 | None. |
| 13 | No transaction, sponsor, quotes, valuation or relative-value inputs are supplied (context deal terms, quotes and valuation inputs blank). Not treated as zero. | Low | Context, synthesis | Context | Those modules are outside the selected set. |

## Next module

Run the financial data and ratio module (CP-1) next, then the business and transaction context module (CP-1A), then the fundamental credit synthesis (CP-2), then the evidence-trace validator (CP-5). Each is READY_WITH_LIMITATIONS and must carry the gaps above: report availability at 2026-09-30 and flag the October 7, 2026 maturity; state interest cover on interest expense, net, because 2026 cash interest is not printed; write covenant headroom as Not calculable; use revised 2025 comparatives; quote both sides of the 2025 Adjusted EBITDA conflict; and keep management ratios attributed. Next evidence action: obtain the Credit Agreement with Amendments 1-4, the indentures and guarantor list, and any filing after the cutoff that addresses the revolving tranche, none of which can be used before the cutoff date.
