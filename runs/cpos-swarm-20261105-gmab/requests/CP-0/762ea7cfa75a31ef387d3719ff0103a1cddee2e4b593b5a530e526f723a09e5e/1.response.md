## Request

Module: source readiness for GENMAB A/S (issuer id gmab), as of 2026-11-05 (cutoff 2026-11-05). Pathway: credit_snapshot. Reporting currency per the run context: USD; current period Q3 2026 (three and nine months ended September 30, 2026); prior period FY2025. Selected downstream consumers: CP-1, CP-1A, CP-2 and CP-5, for the report sections key findings, company operating model, model chart strip, financials and credit metrics, strengths and weaknesses, company profile and transaction summary.

Question answered: can the four supplied filings support that work, and what remains blocked. This handoff gives no credit conclusion, legal interpretation or investment opinion, and it normalizes, reconciles and calculates no financial figure. It is a source-sufficiency assessment only (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED).

Perimeter: the reporting entity is the Genmab consolidated Group, that is Genmab A/S (parent, CVR 2102 3884) and its subsidiaries. The Q3 2026 report states: "The interim report is prepared on a consolidated basis for Genmab A/S (parent company) and its subsidiaries." (page:18). The run context names no borrower, parent, guarantor, sponsor or deal terms (all blank or empty); blank values are not treated as zero.

## Sources

Issuer sources relied on (exact names and sha256 of the pinned text files):

| Source name | sha256 | Document family and authority | Period and basis | Chunks read (page:N) |
| --- | --- | --- | --- | --- |
| 20-F_2025-12-31_gmab-20251231_d2.htm.jsonl | 041104aadf76e2dd3c99b07f2a5c8ca0092780880cc53f8276cda7db55a72e43 | Form 20-F annual report filed with the SEC, signed February 17, 2026; filed document, controls its own facts | Fiscal year ended December 31, 2025; IFRS Accounting Standards; USD | page:1 to page:190 (190 of 190 chunks present; searched in full, relevant chunks opened) |
| 6-K-EX-99.1_2025-11-06_genmabinterimreportq32025.htm.jsonl | 06978ddb790610f6f32c0187b617be9da7c780d7403fa742ff98ba9049d5f051 | Form 6-K Exhibit 99.1 interim report and earnings release dated November 6, 2025; issuer-published, unaudited | Nine months ended September 30, 2025 with comparatives; IAS 34; USD million | page:1 to page:49 (49 of 49 chunks present) |
| 6-K-EX-99.1_2026-05-07_genmabinterimreportq12026.htm.jsonl | 4ecbe1ab5be0468827b42bbf43fa8fbdbec0fdd369b4737a86f629cb84e67e45 | Form 6-K Exhibit 99.1 interim report and earnings release dated May 7, 2026; issuer-published, unaudited | Three months ended March 31, 2026 with comparatives; IAS 34; USD million | page:1 to page:40 (40 of 40 chunks present) |
| 6-K-EX-99.1_2026-11-05_genmabinterimreportq32026.htm.jsonl | 864b19bf237a4d5a6460638b8680b6339157a3234e843d8e76bb977e4dc1d4f8 | Form 6-K Exhibit 99.1 interim report and earnings release dated November 5, 2026; issuer-published, not audited or reviewed | Three and nine months ended September 30, 2026 with comparatives; IAS 34; USD million | page:1 to page:54 (54 of 54 chunks present; read in full) |

Run settings, not issuer evidence: context file f11f6ebfef20e70f4d6999b74c1449c3a4d8535f2ef28448cb9cbb9dc6331b4f (sha256). The pack also holds _retrieval.json, which CP-OS ignored; it is not a source.

Supplied handoffs: none. CP-0 is the first module in this run, so no upstream handoff exists to re-anchor.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The four filings can support a credit snapshot of Genmab as of 2026-11-05, with limitations. Genmab now reports $4,992 million of borrowings against $1,860 million of cash, so debt terms matter, and those are largely missing. | Medium | The audited 2025 financial statements and the credit agreement and indenture terms are not in the pack, so maturities, coupons, covenant levels and revolver availability cannot be sourced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Statements, notes and prior-year comparatives for the three and nine months to September 30, 2026 are present in full text. | Current-period flows, balance sheet and facility carrying values can be extracted, but the report is not audited or reviewed. | High |
| Full-year 2025 appears only as comparatives in interim reports; the audited statements are incorporated by reference but not supplied. | Full-year 2025 detail beyond key figures and the year-end balance sheet cannot be traced to audited statements. | High |
| Borrowings sit in four instruments with carrying values disclosed, but coupons, maturities and covenant levels are not. | Refinancing timing, interest burden by instrument and covenant headroom cannot be assessed from this pack. | High |
| No first-half 2026 report is supplied, and 2025 comparatives were reclassified in the latest report. | Discrete second-quarter 2026 figures and like-for-like expense lines need explicit bridging downstream. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for the selected work. No selected consumer is CONDITIONAL or BLOCKED. Identity is unambiguous: all four documents are issued by Genmab A/S, in USD million, on a consolidated basis, and the run context currency (USD) matches the sources. The current-period evidence (Q3 2026 and nine months 2026, with Q3 2025 and nine months 2025 comparatives) is complete in extracted text, including income statement, balance sheet, cash flow, equity statement, a borrowings note with facility-level carrying values, derivative, lease, contingency and subsequent-event notes. The binding restrictions are: (a) the audited FY2025 financial statements and the annual-report notes on borrowings are not in the pack; (b) the executed credit agreement and indentures are listed as exhibits but not supplied; (c) no first-half 2026 report is supplied; (d) the 2026 interim statements are unaudited. These restrict, rather than prevent, each consumer, as set out in the consumer table below. This is a source-sufficiency judgment only; it does not accept any downstream input contract.

### Source assessments

#### 20-F for the fiscal year ended December 31, 2025

- Identity and authority: the cover page states "Form 20-F" for "the fiscal year ended December 31, 2025" by "Genmab A/S" (page:1). It is a filed annual report and controls its own narrative facts (business, risk factors, governance, exhibits list).
- What is present: business, risk factors including "Risks Related to Our Indebtedness" (page:64), Item 5 narrative (page:126 to page:132), exhibits list (page:180 to page:184), signature dated February 17, 2026 (page:185) and auditor reports (page:185 to page:190).
- What is not present: the financial statements themselves. Item 18 states "The financial statements required by this item are incorporated herein by reference to pages 107-156 of our Annual Report 2025" (page:180), and the Annual Report 2025 is Exhibit 15.3, listed as "Genmab A/S statutory Annual Report 2025*" (page:183). That exhibit is not part of the pack. Item 5 likewise incorporates by reference the Financial Review, liquidity, lease (Note 3.3), commitments (Note 5.3) and borrowings (Note 4.8) disclosures (page:130, page:131). Consequently no FY2025 income statement, balance sheet, cash flow statement or debt note is in this source's text.
- Debt facts that are present in narrative: December 2025 senior secured credit facilities of "a $1 billion Term Loan A Facility and a $2 billion Term Loan B Facility", "a $500 million revolving credit facility", "$1.5 billion principal amount of Senior Secured Notes and $1.0 billion principal amount of Senior Unsecured Notes" (page:126). The risk factor states the credit agreement "requires us to comply with certain financial maintenance covenants" (page:65), and the dividend discussion says the credit agreement and indentures restrict "restricted payments" (page:152).
- Currency: the 2023 auditor report records that the Company "changed the currency in which it presents its financial statements in 2025 from Danish Kroner to U.S. Dollar" (page:189), which is consistent with the USD context.
- Extraction: text extraction only; successful extraction is not a fidelity review, and no table image or XBRL tagging was inspected.

#### Interim report Q3 2025 (6-K Exhibit 99.1, November 6, 2025)

- Identity and period: nine months ended September 30, 2025 (page:1). Supplies the prior-year Q3 and nine-month base and the December 31, 2024 and full-year 2024 columns (page:4).
- Transaction evidence: the proposed Merus acquisition at "USD 97.00 per share in an all-cash transaction representing a transaction value of approximately USD 8.0 billion", expected funding "through a combination of cash on hand and approximately $5.5 billion of non-convertible debt financing", backed by a funding commitment from Morgan Stanley Senior Funding, Inc.; and a management target of "gross leverage <3x within two years after the closing" (page:3). This is a pre-closing statement and a management target, not an achieved outcome.
- Version relationship: this is the originally published presentation of the 2025 comparatives. The Q3 2026 report restates them (see the version log). The Q3 2025 report is retained as a separate active source and is not collapsed into the later one.

#### Interim report Q1 2026 (6-K Exhibit 99.1, May 7, 2026)

- Identity and period: three months ended March 31, 2026 (page:1), with full-year 2025 column in the key figures (page:3).
- Content: first-quarter statements, borrowings note by facility (page:35), covenant statement "Term Loan A is subject to financial covenants, with the financial covenant tests on a quarter-end basis beginning March 31, 2026" (page:35), swap schedule, legal and subsequent-event notes.
- Role: supplies discrete Q1 2026 and Q1 2025. Together with the nine-month report it brackets, but does not state, discrete Q2 2026.

#### Interim report Q3 2026 (6-K Exhibit 99.1, November 5, 2026)

- Identity and period: "Interim Report for the Nine Months Ended September 30, 2026" (page:1), dated on the run as-of date. Management states "The interim report has not been audited or reviewed by Genmab's external auditors" (page:37, page:54).
- Content: highlights and non-IFRS reconciliation (page:2, page:3), key figures (page:5, page:6), 2026 outlook table (page:6), financial review (page:18 to page:32), legal matters (page:33), statements (page:34 to page:36), notes 1 to 15 (page:37 to page:52).
- Debt: Note 8 gives current and non-current carrying values for Term A Loans (Secured), Term B Loans (Secured), Secured Notes and Unsecured Notes, a roll-forward from the December 31, 2025 balance, and the June 2026 amendment of the Term B margin "from 3.00% to 2.00%" with nominal value "$1,900 million" after the amendment (page:45, page:46). Note 9 gives four interest rate swaps with a fixed rate, 3-month SOFR index and termination date 6/30/2028 (page:47).
- Subsequent events: Note 15 states "No events have occurred subsequent to the balance sheet date that could significantly affect the condensed consolidated financial statements" (page:52). Separately, the highlights section lists October 2026 topline results of three Phase 3 trials (page:4). Both are dated on or before the cutoff and are treated as post-quarter events, not as period figures.
- Management claims, such as the CEO characterization of the data-rich fourth quarter and "first bispecific-based therapy approved in Europe for second-line FL" (page:1), are attributed management language, not filing-controlled facts.
- Extraction: text extraction only; no chart, image or speaker-note coverage is claimed (none applies; the documents are text exhibits).

### Consumer readiness

| Consumer | Status | Evidence demand | Evidence located | Limitations carried |
| --- | --- | --- | --- | --- |
| CP-1 financial extraction | READY_WITH_LIMITATIONS | Statements, notes, period labels, debt and cash-flow lines, quarter versus year-to-date distinctions | Q3 2026 and nine months 2026 with 2025 comparatives (Q3 2026 report, page:34 to page:36); Q1 2026 (Q1 report, page:3, page:35); Q3 2025 base (Q3 2025 report, page:4); facility carrying values (Q3 2026 report, page:45) | FY2025 audited statements absent; FY2025 cash flow only as key-figure lines; no first-half 2026 report; 2025 comparatives reclassified; unaudited 2026 data |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business model, Merus transaction and its financing, ownership, history, governance | 20-F Item 4 business overview (from page:67) and Item 5 and Item 6 narrative (Item 5 and 6 at page:126 to page:132); Q3 2025 report (page:3, page:40); Q3 2026 Notes 2 and 8 (page:39, page:45) | No sponsor or deal terms in the context; credit agreement and indentures not supplied (only exhibit titles, 20-F page:180, page:181); no rating source; guarantor and co-issuer detail beyond exhibit titles not supplied |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Consumes CP-1 and CP-1A only; source demand is liquidity, leverage inputs and gaps | Cash, borrowings, interest and cash-interest lines in the Q3 2026 report (page:5, page:28, page:35) | Revolver drawn or undrawn amount, covenant levels and headroom, maturity profile, ratings and market data are not supplied; inherits all CP-1 and CP-1A limits |
| CP-5 evidence trace | READY_WITH_LIMITATIONS | Locators, calculations, conflicts, subsequent events | All four sources are searchable by page:N chunk | Chunk numbers differ from printed page numbers; text-only extraction; accepted upstream handoffs are required before it can run |

Nothing in this table makes a missing downstream analytical handoff a readiness condition; sequencing is left to the dependency planner.

### Report-model input sufficiency (source level only)

- Discrete quarters: Q3 2026 and Q3 2025 (Q3 2026 report, page:5); Q1 2026 and Q1 2025 (Q1 report, page:3). Discrete Q2 2026 is not stated in any supplied source because the first-half 2026 report is not supplied (the Q3 2026 report refers to it, page:8).
- Fiscal years: FY2025 and FY2024 key figures (Q3 2026 report page:5; Q3 2025 report page:4). The 20-F audit reports cover the years but the statements are not in the pack.
- Quarter versus year-to-date: the Q3 2026 report prints three-month and nine-month columns side by side (page:5, page:34). The cash flow statement prints nine months only (page:35).
- Segments: the report states Genmab is "managed and operated as one business unit" (page:39). Revenue by type, partner and royalty product is in Note 3 (page:39).
- Add-backs: the non-IFRS reconciliation for nine months 2026 and 2025 is on page:3. No quarter-level reconciliation table is supplied.
- Debt: facility-level carrying values and a roll-forward (page:45); cash interest "Interest paid on borrowings" and "Corporate taxes paid" are printed for nine months (page:35).

### Version and conflict log

| Item | Document A (locator) | Document B (locator) | Effect downstream |
| --- | --- | --- | --- |
| FY2025 research and development expense | Q1 2026 report key figures: "Research and Development expenses (440) (359) (1,606)" (page:3) | Q3 2026 report key figures: R&D shown excluding amortization of acquired intangibles, FY2025 (1,592), with a separate FY2025 amortization line of (14) (page:5) | Presentation change, not a conflict: the Q3 2026 report states that, beginning in the third quarter of 2026, amortization is a separate line and comparatives were reclassified (page:39). Use one basis per series and label it. |
| Q3 2025 and nine-month 2025 R&D | Q3 2025 report as originally published (page:4) | Q3 2026 report: "$3 million and $9 million, respectively, were reclassified from Research and development expenses to Amortization of acquired intangible assets" (page:39) | Prior-year R&D differs between the two reports by the reclassified amounts; operating profit is unchanged per the same note. |
| Subsequent events | Note 15: no significant subsequent events (page:52) | Highlights list October 2026 Phase 3 topline results (page:4) | Not a numeric conflict. The October results are non-financial post-quarter events; keep them out of period figures. |
| Merus transaction value | Q3 2025 report: "approximately USD 8.0 billion" (page:3) | 20-F auditor report: "USD 8.017 billion" (page:187); Q3 2026 Note 2: "approximately $8.0 billion" (page:39) | Rounded versus precise statement of the same transaction; quote both when used. |

No source conflicts on any reported statement figure were found in the figures that CP-0 compared (revenue, operating profit, net profit, cash, borrowings), which agree between the Q1 2026 and Q3 2026 full-year 2025 columns.

### Evidence citations

| Source | Locator | Exact quote |
| --- | --- | --- |
| 6-K-EX-99.1_2026-11-05_genmabinterimreportq32026.htm.jsonl | page:45 | Total Borrowings $ 318 $ 273 $ 4,674 $ 5,001 |
| 6-K-EX-99.1_2026-11-05_genmabinterimreportq32026.htm.jsonl | page:46 | The Term A Loans are subject to financial covenants. As of September 30, 2026, Genmab was in compliance with these covenants. |
| 6-K-EX-99.1_2026-11-05_genmabinterimreportq32026.htm.jsonl | page:5 | Cash and cash equivalents 1,860 1,761 1,860 1,761 1,715 |
| 6-K-EX-99.1_2026-11-05_genmabinterimreportq32026.htm.jsonl | page:6 | Genmab incurred borrowings of $5.5 billion and utilized cash on hand. |
| 6-K-EX-99.1_2026-11-05_genmabinterimreportq32026.htm.jsonl | page:52 | No events have occurred subsequent to the balance sheet date that could significantly affect the condensed consolidated financial statements as of September 30, 2026. |
| 6-K-EX-99.1_2026-11-05_genmabinterimreportq32026.htm.jsonl | page:8 | For events that occurred during the first and second quarters of 2026, please refer to Genmab’s Q1 2026 and Genmab’s First Half 2026 reports. |
| 20-F_2025-12-31_gmab-20251231_d2.htm.jsonl | page:180 | The financial statements required by this item are incorporated herein by reference to pages 107-156 of our Annual Report 2025. |
| 20-F_2025-12-31_gmab-20251231_d2.htm.jsonl | page:126 | a $1 billion Term Loan A Facility and a $2 billion Term Loan B Facility |
| 6-K-EX-99.1_2026-05-07_genmabinterimreportq12026.htm.jsonl | page:35 | Term Loan A is subject to financial covenants, with the financial covenant tests on a quarter-end basis beginning March 31, 2026. |
| 6-K-EX-99.1_2025-11-06_genmabinterimreportq32025.htm.jsonl | page:3 | target of gross leverage <3x within two years after the closing |

## Calculations

None of the readiness judgments depends on a new calculation, and CP-0 does not normalize, reconcile or recompute reported figures. Two counts and one consistency check were made to support the version log:

| Check | Inputs | Result |
| --- | --- | --- |
| Source coverage count | Chunks present per source: 190 (20-F), 49 (Q3 2025), 40 (Q1 2026), 54 (Q3 2026) | 333 chunks across the four sources; every chunk is retained, none is an excluded or degraded unit |
| FY2025 R&D presentation consistency | Q1 2026 report FY2025 R&D of 1,606 (page:3); Q3 2026 report FY2025 R&D of 1,592 and FY2025 amortization of acquired intangible assets of 14 (page:5) | 1,606 less 1,592 is 14, equal to the separately presented FY2025 amortization line; this confirms a presentation change only, not a restatement of operating profit (1,065 in both reports) |
| Total borrowings tie-out, September 30, 2026 | Current 318 plus non-current 4,674 (page:45) versus key figures Borrowings 4,992 (page:5) | 318 plus 4,674 is 4,992; ties |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Audited FY2025 consolidated financial statements and notes (Annual Report 2025, Exhibit 15.3, pages 107-156) not in pack; 20-F incorporates them by reference (page:180, page:183) | High | CP-1, CP-2, CP-5 | Add Exhibit 15.3 to the pack. Until then FY2025 figures rest on the unaudited interim comparatives and are labelled that way. |
| Credit agreement, indentures and first supplemental indenture listed as exhibits (20-F page:180, page:181) but not supplied; Note 4.8 of the annual report not supplied | High | CP-1, CP-1A, CP-2 | Add the executed documents or Note 4.8. Not supplied: coupons and margins (except the Term B margin change in Q3 2026 page:46), contractual maturities, amortization schedule, security package, guarantors, covenant definitions and levels. |
| Revolving credit facility: the 20-F refers to a $500 million revolver (page:126) and to an unsecured three-year and a senior secured five-year revolver (page:131), but no supplied interim report states a drawn or undrawn amount | High | CP-1, CP-2 | Not supplied: drawn amount and availability. Liquidity cannot be sourced beyond cash until this is added. |
| Covenant levels and the issuer's reported covenant ratios: only a compliance statement is printed (Q3 2026 page:46; Q1 2026 page:35) | High | CP-2, CP-5 | Not calculable: headroom needs the test levels and definitions. |
| First-half 2026 report not supplied (referenced in Q3 2026 page:8) | Medium | CP-1 | Add the first-half 2026 report for discrete Q2 2026. Do not derive Q2 from year-to-date differences without labelling it. |
| 2026 interim statements are not audited or reviewed (Q3 2026 page:37, page:54; Q1 2026 report states the same) | Medium | all | Carry the status into every figure's label. |
| Reclassified 2025 comparatives (Q3 2026 page:39) versus originally published (Q3 2025 report, Q1 2026 report) | Medium | CP-1, CP-5 | Choose a basis per series, label it, and bridge using the reclassification note. |
| No credit rating, market price, market capitalization or peer data in any source; the run context valuation block is blank | Medium | CP-2, relative value (not selected) | Not supplied. External material, if added later, must be labelled as external. |
| Guarantor list and co-issuer roles: indenture parties "Genmab A/S, Genmab Finance LLC, the guarantors named therein" appear only in exhibit titles (20-F page:181) | Medium | CP-1A, CP-2 | Add the indenture. Obligor and guarantor perimeter remains unresolved. |
| Text extraction only: no table-image, XBRL or fidelity review was performed | Low | all | A fidelity spot check of key tables against the filing is recommended before committee use. |
| Colliding names for the loans across reports ("Term Loan A" in the 20-F and Q1 2026; "Term A Loans" in Q3 2026) | Low | CP-1 | Treated as the same facilities by label similarity and matching amounts; not independently confirmed in an agreement. |

## Next module

Proceed to CP-1 (financial extraction), then CP-1A, CP-2 and CP-5 in the order CP-OS schedules. Carry forward: USD million throughout; label every 2026 figure as unaudited; label FY2025 figures as interim comparatives unless the audited statements are added; use one R&D basis (before or after the separate amortization line) per series; keep October 2026 trial readouts and Note 15 as post-quarter events; and treat covenant levels, revolver availability, maturities, coupons and guarantors as Not supplied rather than zero. Next evidence action: add Annual Report 2025 (Exhibit 15.3), the credit agreement and indentures, and the first-half 2026 report to the pack.
