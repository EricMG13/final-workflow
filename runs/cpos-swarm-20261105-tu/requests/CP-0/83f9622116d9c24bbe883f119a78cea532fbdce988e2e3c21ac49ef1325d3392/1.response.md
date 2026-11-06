# CP-0 source readiness: TELUS CORP (tu)

## Request

- Issuer: TELUS CORP (issuer id `tu`; registrant name in the filings "TELUS Corporation"; NYSE ticker TU; Commission File Number 001-15144), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run: `tu-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, case kind public. Requested downstream modules: CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Context settings (not issuer evidence): reporting currency CAD, current period `q2-2026`, prior period `fy-2025`. The context leaves borrower, parent, guarantor, rating, quote, valuation and deal-term fields blank. A blank is not evidence of absence.
- Execution: host session. The host read the pinned files and wrote this answer. No provider was called.
- Question: can the supplied public filings support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion is given. No figure is normalized, reconciled or calculated here.
- Currency and units: the sources report in Canadian dollars, in millions unless stated. MD&A page:8: "All currency amounts are stated in Canadian dollars, unless otherwise specified". This matches the context. Some debt is U.S. dollar denominated and is stated as such in the notes.

## Sources

Locators are `page:N`, the chunk number shown in the pinned text file, not a printed page number.

| Source (exact name) | sha256 | Role |
| --- | --- | --- |
| 40-F_2025-12-31_tu-20251231x40f.htm.jsonl | b0f2582e02ab1590b79f57963d19432006a5c182a75869a932135c754b75fcd3 | Form 40-F cover document for the fiscal year ended December 31, 2025 (7 chunks) |
| 6-K-EX-99.1_2025-09-30_tm2525674d1_ex99-1.htm.jsonl | 436bedaf1f4dce1c7e6eb59881bfd06b2eda28c728cd8f139c3e87e5b19f9141 | Condensed interim consolidated financial statements, September 30, 2025 (72 chunks) |
| 6-K-EX-99.1_2026-02-12_tm261121d3_ex99-1.htm.jsonl | 86a3aab6322382ed8099639d74b8a5a665cd61822ab77656954f6c33682e6312 | News release dated February 12, 2026, fourth quarter 2025 (31 chunks) |
| 6-K-EX-99.1_2026-03-31_tm2610993d1_ex99-1.htm.jsonl | 786ff091c72b6c68ad509f7615fb77cb4d9d97ec151a629884165ec7501f67f6 | Condensed interim consolidated financial statements, March 31, 2026 (55 chunks) |
| 6-K-EX-99.1_2026-05-08_tm2610993d2_ex99-1.htm.jsonl | 4a46a2ffd615b6354baf9f5fba0823218c2071cb4a3fa919c80e6fdbc83658f3 | News release dated May 8, 2026, first quarter 2026 (24 chunks) |
| 6-K-EX-99.1_2026-07-31_tm2615221d2_ex99-1.htm.jsonl | 159e10207755e982fc8e0761482d512b4d2a82246d4508c8eb2d2f1f129bbd5c | News release dated July 31, 2026, second quarter 2026 (22 chunks) |
| 6-K-EX-99.2_2026-06-30_tu-20260630xex99d2.htm.jsonl | df34bf40fbe3d3b13f773ae380315ed0a4e21b523c7736a3fcf69277289ecba4 | Management's discussion and analysis (MD&A), second quarter 2026 (86 chunks) |
| context | 444f0b1a3ec6fedd71ff422ee4a294e2ddb38e2b78bcbad2de66f2441a8d4efa | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module, so no upstream handoff exists. The retrieval index `_retrieval.json` in the pack folder is ignored by CP-OS and is not relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The supplied TELUS filings support all four downstream analyses with stated limits. The latest quarter is well covered, but audited annual statements, second-quarter notes and the debt agreements are absent. | Medium | Audited 2025 statements and second-quarter 2026 notes are not supplied, so annual and debt-by-series figures rest on later filings and quarterly summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual report filing is only a cover document. The audited annual statements and the annual information form are listed as exhibits but are not supplied. | Full-year 2025 figures must be assembled from quarterly sources, which weakens annual comparisons. | High |
| The second-quarter management discussion and results release give liquidity, covenant, facility and debt-movement figures at the latest quarter-end. | Liquidity and covenant headroom can be assessed at June 30, 2026 from located figures. | High |
| The second-quarter interim statement notes are not supplied. The last debt-by-series table and maturity schedule are at March 31, 2026. | Debt composition and the refinancing schedule at June 30, 2026 cannot be verified series by series. | High |
| Segment reporting was restated from 2026, and the latest quarter brought a dividend reset, revised guidance, an impairment and management changes. | Earlier segment figures and guidance are not like-for-like; later work must label periods and vintages. | Medium |
| Credit agreements, indentures and named rating-agency ratings are not supplied. | Covenant definitions, guarantees and rating-trigger terms rest on issuer summaries only. | High |

### Readiness view

The effective source set can support all four selected consumers, each with limitations. No consumer is conditional or blocked, because every consumer has located statements, notes or narrative for the latest quarter and for several earlier periods. The strongest limits are three missing documents. First, the audited fiscal year 2025 financial statements and annual MD&A (Exhibit 99.4 to the Form 40-F) and the annual information form (Exhibit 99.3) are named in the exhibit index but are not in the pack. Second, the June 30, 2026 interim financial statements and notes are not in the pack; only the MD&A and the results release for that quarter are. Third, the indentures, credit agreements and securitization agreement are not in the pack. These limits are carried into each consumer assessment below. This is a statement of source sufficiency only. It does not say that any downstream analysis is complete or that any figure has been checked.

### Consumer verdicts

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Located: quarterly income, balance sheet, cash flow and notes for March 31, 2026 and September 30, 2025; MD&A balance sheet, cash flow, liquidity, covenant and eight-quarter tables for June 30, 2026. Missing: audited fiscal year 2025 statements and the June 30, 2026 notes. |
| CP-1A | READY_WITH_LIMITATIONS | Located: business description, segments, the TELUS Digital privatization, the Terrion partnership, strategic priorities, dividend reset, portfolio review and management changes. Missing: annual information form. |
| CP-2 | READY_WITH_LIMITATIONS | Can synthesise from CP-1 and CP-1A outputs and the located liquidity, covenant, facility, ratings-wording and debt-movement text. Covenant definitions, guarantee structure and named ratings are not supplied. |
| CP-5 | READY_WITH_LIMITATIONS | Every source has stable chunk locators, so claims can be traced. Sources are text extractions with flattened tables; no original HTML or XBRL is supplied for visual or layout checks. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN. None is DO NOT RUN.

### Source register

#### Form 40-F cover document (`40-F_2025-12-31_tu-20251231x40f.htm.jsonl`)

- Family and authority: filed annual report on Form 40-F, page:1 "For the fiscal year ended December 31, 2025". It is the original authority for the exhibit list, the controls statements and the share count on its cover, not for financial statements.
- Content is a cover document. The financial statements are incorporated by reference. Page:3: "which are filed as Exhibit 99.4 to this annual report on Form 40-F". Page:6 exhibit index: "Annual Information Form for the year ended December 31, 2025, dated February 12, 2026" (Exhibit 99.3) and "Audited Consolidated Financial Statements as at and for the years ended December 31, 2025 and 2024 and Management’s Discussion and Analysis" (Exhibit 99.4).
- Also located: page:5 "The Registrant has no off-balance sheet arrangements"; page:6 contractual obligations table is incorporated from "page 59 of the Management’s Discussion and Analysis filed as Exhibit 99.4", which is not supplied; page:1 "1,548,656,383 Common Shares" outstanding as of December 31, 2025.
- Entity and perimeter: registrant TELUS Corporation, incorporated in British Columbia, Canada (page:1). Signed February 12, 2026 (page:7).
- Extraction fidelity: text extraction of the HTML. Not an inspection of the exhibits, which are separate documents outside the pack.

#### Condensed interim consolidated financial statements, September 30, 2025 (`6-K-EX-99.1_2025-09-30_tm2525674d1_ex99-1.htm.jsonl`)

- Family and authority: unaudited condensed interim consolidated financial statements furnished on Form 6-K (Exhibit 99.1), page:1 "CONDENSED INTERIM CONSOLIDATED FINANCIAL STATEMENTS" and page:3 "SEPTEMBER 30, 2025". Page:5: "were authorized by our Board of Directors for issue on November 7, 2025". Original authority for three-month and nine-month 2025 and 2024 statement facts and notes.
- Located content: income statement, financial position, changes in equity, cash flows, and notes. The liquidity-risk text states "Our debt maturities in future years are disclosed in Note 26(j)" (page:17).
- Perimeter at this date: TELUS Digital (the segment of TELUS International (Cda) Inc.) was still consolidated with a non-controlling interest. Page:64: "The transaction closed October 31, 2025". The Terrion tower partnership is described at page:64: "Our Terrion subsidiary was established under the Partnership Act (Ontario) on July 24, 2025".
- Version relationship: supports nine-month 2025 comparatives. It is not superseded by later filings for its own period, but the 2026 filings restate segment presentation (see Version relationships).

#### News release dated February 12, 2026 (`6-K-EX-99.1_2026-02-12_tm261121d3_ex99-1.htm.jsonl`)

- Family and authority: issuer news release furnished as Exhibit 99.1; management-prepared. Page:1 title "TELUS reports strong and industry leading operational and financial results for the fourth quarter and full year 2025"; page:2 "today released its unaudited results for the fourth quarter of 2025".
- Scope as located: fourth quarter 2025 highlights, segment discussion, 2026 targets, reconciliations. It does not contain a full-year 2025 income statement, balance sheet or cash flow statement. Full-year facts it states are narrative, for example page:12 "Consolidated Service revenues for 2025 were $18.0 billion" and page:5 "leverage ratio improving to 3.4-times at year-end 2025".
- Use: attributed management claims and quarter figures (for example page:8 "Net income 290 320 (9 )"). It does not substitute for the audited fiscal year 2025 statements.
- Also located: CEO succession, page:13 "Darren Entwistle will retire on June 30, 2026". Segment note at page:28: "TTech results for 2024 have been restated to conform with our new segmented reporting structure".

#### Condensed interim consolidated financial statements, March 31, 2026 (`6-K-EX-99.1_2026-03-31_tm2610993d1_ex99-1.htm.jsonl`)

- Family and authority: unaudited condensed interim consolidated financial statements, page:1 "MARCH 31, 2026". Page:5: "were authorized by our Board of Directors for issue on May 8, 2026". Original authority for March 31, 2026 and December 31, 2025 statement of financial position facts and the notes.
- Located content: income statement and cash flows (three months 2026 and 2025), financial position at March 31, 2026 and December 31, 2025 (page:1 and page:2), Note 26 long-term debt with the series table (page:39 "Details of long-term debt"; page:40 senior note series), commercial paper, credit facilities (page:43 "Net available $ 1,107 $ 1,798"), junior subordinated notes (page:44 to page:45), maturities (page:46 "Anticipated requirements for long-term debt repayments, calculated for long-term debt owed as at March 31, 2026"), pensions (page:47 "Pension benefit liabilities 15 452 453"), contingent liabilities Note 29 (page:50).
- Covenant text: page:43 "two financial quarter-end ratio tests: our leverage ratio must not exceed 4.25:1.00; and our operating cash flow to interest expense ratio must not be less than 2.00:1.00, all as defined in the credit facilities". The definitions themselves are in the credit facilities, which are not supplied.
- Capital structure policy: page:8 "Our long-term objective range for this ratio is 2.2 – 2.7 times"; page:7 states how net debt to EBITDA is calculated.
- Version relationship: this is the latest source with a debt-by-series table and maturity schedule. It is one quarter earlier than the MD&A.

#### News release dated May 8, 2026 (`6-K-EX-99.1_2026-05-08_tm2610993d2_ex99-1.htm.jsonl`)

- Family and authority: issuer news release, first quarter 2026; page:1 "today released its unaudited results for the first quarter of 2026". Management-prepared and attributed.
- States guidance now superseded: page:1 "3.3-times or lower by year-end 2026 and 3.0-times or better by year-end 2027" and "Consolidated Free Cash Flow of approximately $2.45 billion". See Version relationships.
- Perimeter and presentation: restated segment reporting from January 1, 2026 following the October 2025 privatization of TELUS Digital (page:1).

#### News release dated July 31, 2026 (`6-K-EX-99.1_2026-07-31_tm2615221d2_ex99-1.htm.jsonl`)

- Family and authority: issuer news release, second quarter 2026; page:1 "today released its unaudited results for the second quarter ended June 30, 2026". Management-prepared and attributed. It is the latest-dated source in the pack.
- Credit-relevant claims located: page:1 "pre-tax, non-cash intangible asset and goodwill impairment of $2.1 billion" relating to TELUS Digital; page:2 "Net debt to Adjusted EBITDA of 3.5-times at quarter-end"; page:2 "full-year free cash flow is anticipated to be approximately $1.8 billion"; page:2 and page:4 "approximately $2.7 billion in cumulative cash savings through 2028" from the dividend reset; page:4 "the company remains active in the market on TELUS Health-related non-core assets"; page:3 a "more detailed outline of the capital returns framework and corporate strategy will be provided with TELUS' third quarter 2026 results in November".
- Management change: page:3 "Gopi Chande, Chief Financial Officer". The May 8, 2026 release quotes "Doug French, Executive Vice-president and CFO" (page:4), so the CFO named differs between the two releases. The February release announces the CEO change (page:13).
- Cross-reference: page:5 "See Note 18(b) of the interim consolidated financial statements for additional details". Those interim statements are not in the pack.

#### MD&A, second quarter 2026 (`6-K-EX-99.2_2026-06-30_tu-20260630xex99d2.htm.jsonl`)

- Family and authority: management's discussion and analysis furnished as Exhibit 99.2. Page:9: "This MD&A and the interim consolidated financial statements were reviewed by our Audit Committee and authorized by our Board of Directors (Board) for issuance on July 31, 2026". Unaudited. It is management commentary with statement-derived tables, not the financial statements themselves.
- Located content: section 6 changes in financial position (page:50 and page:51, including "Current maturities of long-term debt" and "Long-term debt" at June 30, 2026 and December 31, 2025); section 7 liquidity (cash flows page:51, financing page:55 to page:56, measures page:59); credit facilities (page:60 "At June 30, 2026, we had $657 million of liquidity available from the TELUS revolving credit facility"); covenants (page:61 "As at June 30, 2026, our consolidated leverage ratio was 3.5 to 1.00 and our consolidated coverage ratio was 4.9 to 1.00"); short-term borrowings (page:62 "Available liquidity under this agreement was $680 million as at June 30, 2026" and a separate "$344 million" non-revolving facility); total liquidity wording (page:63 "we had over $2.7 billion of liquidity available at June 30, 2026"); credit ratings (page:62 "We continued to have investment-grade ratings in the second quarter of 2026 and as at July 31, 2026"); eight-quarter income table (section 5.2, page:29 and following).
- Debt movements: page:56 commercial paper "a balance of $2.1 billion (US$1.5 billion) at June 30, 2026"; page:56 "Subsequent to June 30, 2026, the remaining $300 million was paid upon maturity in the normal course"; page:50 reclassification of a U.S. dollar note series to current.
- Limits: it points to Notes 18, 22, 26, 29 and 31 of interim statements not supplied (for example page:50 "See Note 22 of the interim consolidated financial statements"). It incorporates the 2025 annual MD&A by reference, which is not supplied.
- Segment restatement: page:9 "Effective January 1, 2026, we are retrospectively restating our segmented reporting information".

### Version relationships and conflicts

- Guidance vintages. The May 8, 2026 release states free cash flow of approximately $2.45 billion and leverage targets for year-end 2026 and year-end 2027 (page:1). The July 31, 2026 release states "full-year free cash flow is anticipated to be approximately $1.8 billion" (page:2) and says "The company had previously targeted net debt to Adjusted EBITDA of approximately 3.0-times or lower by year-end 2027" (page:4). The later release controls current guidance. Both are retained as dated management claims. This is a superseded claim, not a document conflict.
- Metric naming. The July release says "Net debt to Adjusted EBITDA of 3.5-times" (page:2). The MD&A reports the covenant-related measure "Net debt to EBITDA – excluding restructuring and other costs" at 3.5 times (page:59). The names differ and the MD&A defines its measure in section 11.1. CP-1 must state which definition it uses and must not treat the two as the same measure without reading the definitions.
- Covenant wording. The March 31, 2026 statements describe the second covenant as an "operating cash flow to interest expense ratio" (page:43). The MD&A calls it the "consolidated coverage ratio" and states 4.9 (page:61), and also reports a separate "EBITDA – excluding restructuring and other costs interest coverage" measure (page:59). The MD&A says "There are certain minor differences in the calculation of the leverage ratio and coverage ratio under the revolving credit facility" (page:61). The facility definitions are not supplied, so the exact covenant calculation cannot be verified.
- Segment structure. The February 12, 2026 release and the September 30, 2025 statements use the earlier structure. The 2026 filings restate it retrospectively for the TELUS Digital privatization (MD&A page:9; May release page:1). Comparing segment figures across these vintages needs a label for each source.
- Perimeter. TELUS Digital was consolidated with a non-controlling interest until the transaction closed on October 31, 2025 (September statements page:64; March statements page:48). Terrion has had a non-controlling interest since July 2025 (September statements page:64). Period comparisons across these dates are not like-for-like.
- Duplicates. The quarterly figures in the July release repeat figures in the MD&A. The MD&A is the more detailed source for the quarter; neither is independent corroboration of the other. Dividend reset statements recur in the July release and the MD&A.
- No hash duplicates are present among the seven sources.

### Identity and perimeter

- Reporting entity and debt issuer: TELUS Corporation. The long-term debt note presents "TELUS Corporation senior notes", "TELUS Corporation commercial paper" and "TELUS Corporation junior subordinated notes" (March statements page:39).
- Principal subsidiaries named: TELUS Communications Inc. and TELUS Health Inc. (March statements page:4, "Our principal subsidiaries"). The TELUS Digital segment sat in TELUS International (Cda) Inc. until October 31, 2025.
- Structural ranking. The notes are described as "effectively subordinated to all existing and future obligations of, or guaranteed by, our subsidiaries" (March statements page:39 and page:45). Whether any subsidiary guarantees a TELUS Corporation instrument is not stated in the supplied text. That is a gap, not a finding of no guarantees.
- Junior subordinated notes receive partial equity credit in leverage ratios: MD&A page:57 "only one-half of the principal of our junior subordinated notes is included as debt".
- Roles not resolved by the sources: restricted and unrestricted group boundaries, covenant borrower group and guarantor list. The context leaves these blank.

### Information-availability boundary

- Latest-dated source: the July 31, 2026 release and MD&A. The as-of date and cutoff are November 5, 2026, so the supplied set ends about three months before the as-of date.
- Nothing dated after July 31, 2026 is supplied. The July release says the fuller capital-returns framework follows with third-quarter 2026 results "in November" (page:3). Those results are Not supplied; whether they were published before the cutoff cannot be determined from the pack.
- Subsequent events inside the pack are bounded to the MD&A and release dates: the remaining $300 million of the 2.75% Series CZ notes paid at maturity after June 30, 2026 (MD&A page:56); the dividend payable on October 1, 2026 and the removal of the dividend reinvestment discount effective October 1, 2026 (release page:4). Both are labelled as dated before or at the release and do not show later outcomes.
- Events between July 31, 2026 and the as-of date, including any debt issuance, asset sale proceeds or rating action, are Not supplied, not absent.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Statements, debt, liquidity, covenants, cash flows, non-GAAP measures, quarter versus year-to-date | March 2026 statements page:1 to page:47; September 2025 statements; MD&A page:50 to page:63 and the eight-quarter table at page:29 onward; release tables | No audited fiscal year 2025 statements; no June 2026 notes; full-year 2025 must be built from quarters; segment and perimeter changes; non-GAAP definitions sit in MD&A section 11.1 |
| CP-1A | Business model, segments, history, ownership, strategic actions, management | MD&A sections 1 to 5 and 9; release page:1 to page:4; September statements page:63 to page:64 | No annual information form; management-attributed strategy claims; regulatory proceedings only as summarized in MD&A section 9 |
| CP-2 | CP-1 and CP-1A outputs; liquidity; covenants; refinancing; leases and pensions | MD&A page:56 to page:63; March statements page:43 to page:47 | Maturity schedule is at March 31, 2026; covenant definitions, guarantees and named ratings not supplied |
| CP-5 | Traceable claims and cross-module consistency | All seven sources have chunk locators | Text only; flattened tables; no HTML or XBRL |

### Analytical read-through

- Usable coverage: three interim sources (September 30, 2025 statements; March 31, 2026 statements; June 30, 2026 MD&A) plus the fourth quarter 2025 and 2026 releases give a continuous quarterly record. The December 31, 2025 statement of financial position is available as a comparative in the March 2026 statements (page:1 and page:2) and the MD&A (page:50 and page:51). The MD&A eight-quarter table covers each quarter of 2025 and 2026.
- Strongest contrary evidence: the audited annual layer is missing, and the latest quarter contains events that change the credit picture. The July release reports a net loss driven by an impairment relating to TELUS Digital and a dividend reset to support deleveraging. Management also states the leverage target date moved to year-end 2028. These are management claims in a release, and the MD&A is the filed document that carries the figures.
- Source risk mechanism, evidence to risk to consequence. First, evidence: the Form 40-F text incorporates its financial statements by reference from an exhibit not in the pack. Risk: an analyst could mistake the cover document for the annual report and treat full-year 2025 figures as audited. Consequence: CP-1 must label fiscal year 2025 as assembled from quarterly sources, and CP-5 must not treat quarterly sums as audited. Second, evidence: debt by series, maturities and the facility table are in the March 2026 notes, while the June 2026 MD&A gives only movements and totals. Risk: the refinancing schedule and series list are one quarter old, and the quarter had redemptions, a note reclassified to current and growth in commercial paper. Consequence: CP-2 can state liquidity at June 30, 2026 but must date the maturity schedule at March 31, 2026. Third, evidence: junior subordinated notes get partial equity credit in the leverage measure, and covenant definitions are not supplied. Risk: reported leverage and covenant leverage may differ from a gross-debt view. Consequence: CP-1 and CP-2 must show each definition and carry the gap instead of assuming headroom from the reported ratio.
- What cannot proceed: verification of covenant calculations against agreement definitions; guarantor-level or restricted-group analysis; a series-by-series debt schedule at June 30, 2026; audited full-year 2025 tie-outs; any event after July 31, 2026.
- Next evidence action: supply Exhibit 99.4 and Exhibit 99.3 of the Form 40-F, the Exhibit 99.1 interim statements that accompany the June 30, 2026 MD&A, the credit agreements and indentures, a rating-agency source, and any filing between July 31, 2026 and November 5, 2026.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Figures quoted above are copied from the sources with their locators. No sum, ratio or difference is computed in this handoff.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Audited consolidated financial statements and annual MD&A for fiscal year 2025 (Exhibit 99.4) not supplied; the Form 40-F incorporates them by reference (page:3, page:6) | High | CP-1, CP-2, CP-5 | Supply Exhibit 99.4 of the Form 40-F |
| Annual information form (Exhibit 99.3) not supplied | Medium | CP-1A, CP-2 | Supply Exhibit 99.3 |
| June 30, 2026 interim financial statements and notes not supplied; Notes 18, 22, 26, 29 and 31 are cited by the MD&A but absent | High | CP-1, CP-2, CP-5 | Supply the Exhibit 99.1 interim statements that accompany the MD&A |
| Debt-by-series table and maturity schedule only at March 31, 2026 | Medium | CP-1, CP-2 | Carry the March 31, 2026 date; supply June 30, 2026 Note 26 |
| Credit agreements, indentures, securitization agreement and guarantee terms not supplied; covenant definitions unverified | Medium | CP-2, CP-5 | Supply the executed agreements or the filings that attach them |
| Named rating agencies, grades and outlooks not supplied; the MD&A states only "investment-grade" wording (page:62) | Medium | CP-2 | Supply agency reports or release text |
| Segment restatement from 2026 and the October 31, 2025 privatization change comparability across vintages | Medium | CP-1, CP-1A | Label each figure with its source vintage and structure |
| No filing or event after July 31, 2026 supplied; third-quarter 2026 results referenced for "November" (release page:3) | Medium | CP-1, CP-1A, CP-2 | Supply later filings, or confirm none before the cutoff |
| Text extraction only; tables are flattened and footnote markers attach to labels (for example "Net debt1") | Low | CP-1, CP-5 | Use the filed HTML or XBRL if exact table layout matters |
| Full-year 2025 cash flow statement and year-end debt note not supplied in a single source | Medium | CP-1 | Assemble from quarters and label as assembled, or supply Exhibit 99.4 |

## Next module

CP-1 is next, with CP-1A to follow, then CP-2 and CP-5. CP-1 should start from the March 31, 2026 statements for debt composition and the June 30, 2026 MD&A for the latest balance sheet, liquidity and covenant figures. It should label fiscal year 2025 as assembled from quarterly sources unless the audited statements are supplied, state which leverage and coverage definition each figure uses, and carry forward the version, perimeter and missing-document limits above.
