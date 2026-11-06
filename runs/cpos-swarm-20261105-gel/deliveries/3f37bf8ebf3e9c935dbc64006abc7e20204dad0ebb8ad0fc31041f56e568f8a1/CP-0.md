## Request

Issuer: GENESIS ENERGY LP (registrant name in the filings: Genesis Energy, L.P.; issuer id gel; ticker GEL). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot, public case. Reporting currency per the run settings: USD (the filings state amounts in thousands of dollars unless noted). Current period: Q3 2026 (quarter ended September 30, 2026). Prior period: FY2025.

Question for this handoff: can the pinned source set support the requested downstream modules CP-1, CP-1A, CP-2 and CP-5 for this issuer, and what remains blocked? This is a source-readiness assessment only. It gives no credit conclusion, no legal interpretation and no recalculation of any figure. Nothing is used from outside the pinned sources. No upstream handoff exists for this module.

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 | Document family and period |
| --- | --- | --- |
| 10-K_2025-12-31_gel-20251231.htm.jsonl | ccb89bebbe1f6460b65cf41694753b9c46d6084fa3c93974775412b94a4649f8 | Form 10-K, fiscal year ended December 31, 2025, signed February 18, 2026 |
| 10-Q_2026-03-31_gel-20260331.htm.jsonl | 25844b5fb23f8fb7e6ed5e3ecd46a1d84117c9d80e65e2ca8d092544b9bdbfa5 | Form 10-Q, quarter ended March 31, 2026 |
| 10-Q_2026-06-30_gel-20260630.htm.jsonl | abd4ada77d59922e6f0bafe2fa139c2cc408c45768d2e839399c3eb81593724d | Form 10-Q, quarter ended June 30, 2026, signed August 6, 2026 |
| 10-Q_2026-09-30_gel-20260930.htm.jsonl | b8ecb63006d005d24876220dffec5b55d573a9ed4071631f5d65780aeca8bd64 | Form 10-Q, quarter ended September 30, 2026, signed November 5, 2026 |
| EX-99.1_2026-05-07_a90ex9918kearnings_q12026.htm.jsonl | dacbb1e9e5b2b770bd5cf7b317240e0ada11d6948f3a4f941eec0c98544a6e5d | Exhibit 99.1 earnings release dated May 7, 2026 (first quarter 2026) |
| EX-99.1_2026-08-06_a90ex9918kearnings_q22026.htm.jsonl | e543ee3e3398ce04f2a72be94919a9105edf4587f39625f574d75860af788168 | Exhibit 99.1 earnings release dated August 6, 2026 (second quarter 2026) |
| EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | c64ffa295db0861a2124c70f86ea927a2ba296a55d07643ed60b307a769d0d5c | Exhibit 99.1 earnings release dated November 5, 2026 (third quarter 2026) |

### Run settings (not issuer evidence)

| Item | sha256 | Use |
| --- | --- | --- |
| context (/workspace/secdata/data/2026-11-05/contexts/1022321-genesis-energy-lp-gel.json) | df9790453496c7c6915bcace0e2562d4cd49506ea6a01ef11c0fdc0b1c2fef47 | Dated settings only: as-of 2026-11-05, current period q3-2026, prior period fy-2025, currency USD. It leaves borrower, parent, guarantors, ratings, quotes, peers and deal terms blank; blank is not zero. |

### Supplied handoffs

None. CP-0 is the first module, and the run supplies no upstream handoff for it.

### Pack housekeeping

The pack also holds a file named _retrieval.json, which CP-OS ignores and this handoff does not rely on. Each source file is a page-by-page text extraction (jsonl). Page 1 of each file opens with a line that gives the digest of the original HTML document; that is a different digest from the pack file digests above, and the pack file digests are the ones this handoff uses. Page below always means the extracted chunk shown as page:N, not the printed page number.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases are enough to run the four requested analyses on the partnership, with limitations. Financial statements, debt note, liquidity and management-reported covenant ratio are all located. | Medium | The credit agreement, note indentures and guarantor list are not supplied, so covenant definitions and debt terms rest on the filings' own descriptions. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited annual and three quarterly filings plus three releases cover the latest quarter, dated on the as-of date. | Current-quarter debt, liquidity and results can be traced to filed statements. | High |
| Debt, revolver availability, letters of credit and the asset-backed receivables facility are all described in the debt note. | Funded debt and liquidity can be built from filed figures without outside data. | High |
| The covenant ratio is quoted only by management in the releases; the release deducts an inventory item the filing describes differently. | Covenant headroom cannot be confirmed against executed legal terms and may differ by definition. | Medium |
| The organization chart, call transcripts and executed financing documents are absent or not extracted. | Guarantor perimeter and structural ranking rest on narrative text only. | Medium |

### Readiness view

The effective source set supports the requested work with limitations. All four consumers (CP-1, CP-1A, CP-2 and CP-5) are READY_WITH_LIMITATIONS and none is CONDITIONAL or BLOCKED. The set is current: the latest source, the third-quarter 10-Q and release, is dated November 5, 2026, the as-of date, and nothing in the pack is dated after the cutoff. The identity boundary is resolved: one registrant, Genesis Energy, L.P., a Delaware master limited partnership, files every document under Commission file number 1-12295. This verdict is source sufficiency only (SOURCE_SUFFICIENCY_ONLY): it does not assert that any downstream input contract is met or that any figure reconciles. Extraction status is not a fidelity review; no image, chart or table rendering was inspected and only the extracted text was read.

### Source-by-source assessment

| Source | Original authority | Entity and perimeter | Period and basis | Located content | Limitation |
| --- | --- | --- | --- | --- | --- |
| 10-K_2025-12-31_gel-20251231.htm.jsonl | Audited filed annual report; auditor opinion on statements and internal control | Genesis Energy, L.P. and subsidiaries, consolidated | FY2025 with FY2024 and FY2023 comparatives; Alkali Business shown as discontinued | Balance sheet page:166, statements page:166 and page:168, debt note 11 near page:191, segment note 14 page:207, subsequent events page:220, exhibits page:158 | Describes the Seventh Amended and Restated Credit Agreement, which the Eighth agreement replaced on March 4, 2026; organization chart on page:9 is an image with no extracted content |
| 10-Q_2026-03-31_gel-20260331.htm.jsonl | Filed unaudited interim report | Same consolidated perimeter | Quarter to March 31, 2026 against the prior-year quarter and December 31, 2025 | Statements pages:2-4, debt note 10 pages:12-14, segment note page:20, MD&A page:28 onward, exhibits page:57 | Condensed notes; unaudited; exhibit 10.1 is listed but not supplied |
| 10-Q_2026-06-30_gel-20260630.htm.jsonl | Filed unaudited interim report | Same consolidated perimeter | Quarter and six months to June 30, 2026 | Statements pages:2-5, debt note 10 pages:15-18, segment note pages:25-26, MD&A page:33 onward | Condensed notes; unaudited; exhibit 22.1 (list of issuers and guarantor subsidiaries) is filed with this report but not supplied |
| 10-Q_2026-09-30_gel-20260930.htm.jsonl | Filed unaudited interim report, the latest periodic filing | Same consolidated perimeter; guarantor summarized financial information given for the issuer and guarantor subsidiaries | Quarter and nine months to September 30, 2026 against the prior-year periods and December 31, 2025 | Balance sheet page:2, operations page:3, cash flows page:5, debt note 10 pages:14-19, segment note pages:25-27, MD&A liquidity pages:48-55 | Condensed notes; unaudited; no subsequent-events note in the table of contents (page:2) |
| EX-99.1_2026-05-07_a90ex9918kearnings_q12026.htm.jsonl | Management release, attributed claims; filings control | Genesis Energy, L.P. consolidated | Quarter to March 31, 2026 and trailing twelve months | Statements of operations page:7, balance sheet page:8, reconciliations pages:9-10, ratio table page:10 | Adjusted measures are management definitions |
| EX-99.1_2026-08-06_a90ex9918kearnings_q22026.htm.jsonl | Management release, attributed claims; filings control | Genesis Energy, L.P. consolidated | Quarter and six months to June 30, 2026 and trailing twelve months | Statements of operations page:9, balance sheet page:11, reconciliations pages:11-13, ratio table page:14 | Adjusted measures are management definitions |
| EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | Management release, attributed claims; filings control | Genesis Energy, L.P. consolidated | Quarter and nine months to September 30, 2026 and trailing twelve months | Statements of operations page:7, balance sheet pages:8-9, reconciliations pages:9-11, ratio table page:11 | Adjusted measures are management definitions; outlook statements are management language |

Version relationships: the three 10-Qs and the 10-K are successive periodic reports of the same registrant, not duplicates and not amendments of each other. Each release is a separate source from the 10-Q for the same period and neither replaces the other. The 10-K continues to describe the Seventh credit agreement, so for covenant terms the 10-Qs from March 31, 2026 control over the 10-K.

### Entity, perimeter and instrument roles located

| Role | Entity | Evidence |
| --- | --- | --- |
| Registrant, borrower under the credit agreement and issuer of notes | Genesis Energy, L.P. | 10-Q_2026-03-31_gel-20260331.htm.jsonl page:57 lists the credit agreement "among Genesis Energy, L.P., as the borrower"; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:18: "co-issued by Genesis Energy, L.P. and Genesis Energy Finance Corporation" |
| Co-issuer of the senior unsecured notes | Genesis Energy Finance Corporation | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:18, same sentence |
| Guarantors of the notes | Current and future 100% owned domestic subsidiaries, except Genesis AR LLC, Genesis AR Holdings LLC and certain other immaterial subsidiaries | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:18: "fully and unconditionally guaranteed jointly and severally by all of Genesis Energy, L.P.’s current and future 100% owned domestic subsidiaries" |
| Non-guarantor receivables vehicle | Genesis AR LLC, a wholly-owned consolidated special purpose entity | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:16: "a consolidated and bankruptcy-remote special purpose entity" |
| General partner | Genesis Energy, LLC | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:7: "Genesis Energy, LLC, our general partner, is a wholly-owned subsidiary." |
| Equity investee with its own non-recourse revolver | Poseidon Oil Pipeline Company, LLC | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:14: facility "is non-recourse to Poseidon’s owners and secured by its assets" |
| Non-100% owned consolidated subsidiaries | Noncontrolling interests | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3: "Noncontrolling interests 461,233 469,907" |

Unresolved: the full guarantor list (exhibit 22.1) and the organizational chart are not in the extracted text, so which named subsidiaries are restricted, unrestricted or non-guarantor beyond the descriptions above stays a gap.

### Located evidence by profile

Financial reports. Balance sheet, statements of operations, cash flows, debt, segments, derivatives, fair value and commitments are all present in the Q3 10-Q. Anchors:

- Cash and debt at September 30, 2026, 10-Q_2026-09-30_gel-20260930.htm.jsonl page:2: "Cash and cash equivalents $ 41,477 $ 6,437", "Restricted cash 4,975 —", "Accounts receivable securitization credit facility 99,500 —" and "SENIOR UNSECURED NOTES, net of debt issuance costs and discount 3,106,655 3,040,415".
- Debt table, 10-Q_2026-09-30_gel-20260930.htm.jsonl page:15: "Total long-term debt $ 3,150,000 $ 43,345 $ 3,106,655 $ 3,085,760 $ 38,945 $ 3,046,815". The five note series are listed on pages:14-15 (2029, 2030, 2032, 2033 and 2034 notes).
- Maturity profile, 10-Q_2026-09-30_gel-20260930.htm.jsonl page:49: "with nothing maturing until January 15, 2029".
- Revolver, 10-Q_2026-09-30_gel-20260930.htm.jsonl pages:16-18: a $900 million senior secured revolving facility under the Eighth Amended and Restated Credit Agreement entered into on March 4, 2026; letters of credit (10-Q_2026-09-30_gel-20260930.htm.jsonl page:17: "of which $5.6 million was outstanding at September 30, 2026"); (10-Q_2026-09-30_gel-20260930.htm.jsonl page:18: "The total amount available for borrowings under our senior secured credit facility at September 30, 2026 was $894.4 million, subject to compliance with covenants."
- Receivables facility, 10-Q_2026-09-30_gel-20260930.htm.jsonl page:16: "The AR Facility provides for a credit facility limit of $99.5 million and expires on June 26, 2029."
- Latest-quarter results, 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3: "NET INCOME (LOSS) ATTRIBUTABLE TO GENESIS ENERGY, L.P. $ 2,415 $ 9,207 $ 52,072 $ (460,274)" (three months 2026, three months 2025, nine months 2026, nine months 2025).
- Annual statements, 10-K_2025-12-31_gel-20251231.htm.jsonl page:166 and page:168, with the auditor opinion on page:162: "present fairly, in all material respects, the financial position of the Partnership as of December 31, 2025 and 2024".

Earnings releases. Each release carries reported and adjusted measures, a reconciliation, quarter and year-to-date columns, and attributed management narrative. Management outlook is language, not fact: EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:4 says "we will likely be near, or possibly even below, the low end of our original guidance for Adjusted EBITDA for the year". The numerical guidance range is not stated in any release; EX-99.1_2026-05-07_a90ex9918kearnings_q12026.htm.jsonl page:1 refers to "the midpoint of the range we discussed on our year-end call", and the year-end call is not supplied.

Covenants and ratios. 10-Q_2026-09-30_gel-20260930.htm.jsonl page:17 states the covenant levels: "5.75 to 1.00 for the fiscal quarters ending March 31, 2026 through December 31, 2027", "2.00 to 1.00 for the fiscal quarters ending March 31, 2026 through December 31, 2026" for minimum interest coverage and "(iii) the maximum Senior Secured Leverage Ratio as 2.50 to 1.00". The reported bank leverage ratios are management figures in the releases: EX-99.1_2026-05-07_a90ex9918kearnings_q12026.htm.jsonl page:1 "a bank leverage ratio of 5.38X", EX-99.1_2026-08-06_a90ex9918kearnings_q22026.htm.jsonl page:1 "a bank leverage ratio of 5.00X", EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:1 "a bank leverage ratio of 5.03X". The 10-Q text extracted for the quarter does not state the reported ratio or the interest coverage ratio, and the definitions sit in the credit agreement, which is not supplied.

Segments and operating KPIs. Three reportable segments (offshore pipeline transportation, marine transportation, onshore transportation and services) with Segment Margin by segment: EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:5 and 10-Q_2026-09-30_gel-20260930.htm.jsonl pages:25-27; volumes and utilization EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:8.

Legal and financing sources. No executed legal document is in the pack. The Q1 10-Q exhibit list (10-Q_2026-03-31_gel-20260331.htm.jsonl page:57) shows "10.1 Eighth Amended and Restated Credit Agreement, dated as of March 4, 2026" as filed with that report, and the Q3 10-Q lists "22.1 List of Issuers and Guarantor Subsidiaries" by reference to the June 30, 2026 10-Q (10-Q_2026-09-30_gel-20260930.htm.jsonl page:65). These are pointers only. The Q3 10-Q says legal proceedings are unchanged: "There have been no material developments in legal proceedings since the filing of such Form 10-K." (10-Q_2026-09-30_gel-20260930.htm.jsonl page:64).

Presentations, workbooks and scans. None supplied. No slide, chart or speaker-note coverage is claimed. The 10-K organization chart is an image: 10-K_2025-12-31_gel-20251231.htm.jsonl page:9 reads "The following chart depicts our organizational structure at December 31, 2025." and the chart content is not in the extracted text.

### Coverage units

Every extracted page is retained as evidence. No page is excluded. Short pages (under 400 characters) were opened: they are table fragments, signature or exhibit-footer pages (for example 10-K_2025-12-31_gel-20251231.htm.jsonl page:105, page:142 and page:193, and 10-Q_2026-06-30_gel-20260630.htm.jsonl page:66), and none is an extraction failure. Retained page counts per source are in Calculations. Degraded content is bounded to the 10-K organization chart (10-K_2025-12-31_gel-20251231.htm.jsonl page:9). Whether tables were flattened without loss of column alignment is not tested; filings' tables appear as space-separated rows and column meaning must be read from the headers on the same page.

### Conflicts and definitional differences between sources

| Item | Source A | Source B | Downstream effect |
| --- | --- | --- | --- |
| Cash at September 30, 2026 | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:2: "Cash and cash equivalents $ 41,477 $ 6,437" and "Restricted cash 4,975 —" | EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:11, ratio table: "Less: Cash and cash equivalents (40,553)"; the table note says cash "from our restricted subsidiaries" | The covenant cash figure differs from the balance sheet figure and the reason is not reconciled in the sources. CP-1 should use the filed balance sheet for liquidity and carry the release figure only as the management covenant input. Not reconciled here. |
| Inventory financing item | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:17: "Our inventory financing sublimit as of September 30, 2026 was $10.5 million of the maximum allowed of $200 million." and "we had no borrowings outstanding under our senior secured credit facility" | EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:11: "Less: Outstanding inventory financing sublimit borrowings (10,500)" | The 10-Q describes $10.5 million as a sublimit size; the release deducts it as outstanding borrowings. Whether it is drawn is unresolved, which affects the release's adjusted debt and the covenant ratio. |
| Receivables facility in debt | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:2 and page:15 show $99.5 million as a current borrowing | EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:11: "Adjusted Debt excludes amounts outstanding under our accounts receivable securitization credit facility" | Funded debt on the balance sheet and the covenant debt measure have different perimeters; CP-1 must label which one each ratio uses. |
| Credit agreement version | 10-K_2025-12-31_gel-20251231.htm.jsonl page:109 describes the Seventh Amended and Restated Credit Agreement, entered into on July 19, 2024 | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:16 describes the Eighth, entered into on March 4, 2026, to "replace our Seventh Amended and Restated Credit Agreement" | Covenant levels and maturity in the 10-K are superseded. Use the 10-Q terms for current analysis. |
| Prior-year comparability | 10-Q_2026-09-30_gel-20260930.htm.jsonl page:7: Alkali Business sold February 28, 2025 and shown as discontinued operations for the nine months ended September 30, 2025 | 10-K_2025-12-31_gel-20251231.htm.jsonl page:166 FY2024 balance sheet carries lines "held for discontinued operations" | Nine-month and annual 2025 figures include or exclude Alkali by line; consumers must keep continuing and discontinued operations apart. |

### Consumer assessment

| Consumer | Status | Usable coverage | Strongest limitation | Next evidence action |
| --- | --- | --- | --- | --- |
| CP-1 (financial data and ratios) | READY_WITH_LIMITATIONS | Annual and quarterly statements, debt note by instrument, liquidity, cash flows, segment and non-GAAP reconciliations, with FY2025, Q1 to Q3 2026 and nine months 2026 | Covenant ratio and its debt and cash inputs rest on release definitions; cash and inventory-financing items conflict between filing and release; no fourth-quarter 2025 discrete statement is printed in the pack | Obtain the Eighth credit agreement; keep filed and covenant bases labelled separately |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description, segments, ownership, 2026 financing and preferred-unit purchases, asset sale and subsequent items in MD&A and releases | Organization chart is an image; no transaction documents; governance and board detail is from the 10-K at December 31, 2025 and is not refreshed in the 10-Qs | Obtain the organization chart and note indentures if structure scoring is needed |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Depends on CP-1 and CP-1A outputs; the underlying filed evidence for business risk, financial risk and liquidity is present | Inherits all CP-1 and CP-1A limitations; no rating agency, market or peer data is in the pack | None needed for source readiness; sequence after CP-1 and CP-1A |
| CP-5 (evidence trace validation) | READY_WITH_LIMITATIONS | Every figure can be traced to a located page in a filed statement or release | Management claims in releases cannot be tied to executed documents; extraction fidelity is unreviewed | None needed for source readiness |

CP-2 and CP-5 are scheduled after the upstream modules by the dependency planner; a missing upstream handoff is not a source-readiness condition here.

### Subsequent events and cutoff

All sources are dated on or before 2026-11-05. The third-quarter release and 10-Q are dated November 5, 2026 (same day as the cutoff) and are in scope. Events after the quarter end that appear in the sources: the October 2026 distribution declaration (10-Q_2026-09-30_gel-20260930.htm.jsonl page:53: "In October 2026, we declared our quarterly distribution to our common unitholders of $0.20 per unit related to the 2026 Quarter.") and, in the release only, "due to Hurricane Isaias in early October" (EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl page:4). The 10-Q does not mention the hurricane. Subsequent events must be labelled as such downstream. Financing events earlier in 2026 are located: the 6.750% notes due 2034 (10-Q_2026-09-30_gel-20260930.htm.jsonl page:18: "On March 4, 2026, we issued $750.0 million in aggregate principal amount of 6.750% senior unsecured notes due March 15, 2034"), the preferred-unit purchases (10-Q_2026-09-30_gel-20260930.htm.jsonl page:48: "we opportunistically purchased 3,263,127 Class A Convertible Preferred Units at a purchase price of $34.38 per unit") and the June 2026 divestiture "for total consideration of $95.0 million" (10-Q_2026-09-30_gel-20260930.htm.jsonl page:48).

## Calculations

No financial figure was calculated, normalized or reconciled in this module, as the method requires. The only arithmetic is the page-coverage count, from the extracted files:

| Source | Pages retained |
| --- | --- |
| 10-K_2025-12-31_gel-20251231.htm.jsonl | 220 |
| 10-Q_2026-03-31_gel-20260331.htm.jsonl | 58 |
| 10-Q_2026-06-30_gel-20260630.htm.jsonl | 66 |
| 10-Q_2026-09-30_gel-20260930.htm.jsonl | 66 |
| EX-99.1_2026-05-07_a90ex9918kearnings_q12026.htm.jsonl | 18 |
| EX-99.1_2026-08-06_a90ex9918kearnings_q22026.htm.jsonl | 21 |
| EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | 18 |

Total: 220 + 58 + 66 + 66 + 18 + 21 + 18 = 467 pages. Coverage: 467 of 467 extracted pages are retained; 0 excluded. This is a retention count, not proof that every page was read for every purpose, and not a fidelity review.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Not supplied: the Eighth Amended and Restated Credit Agreement, which defines Consolidated EBITDA, Adjusted Consolidated EBITDA, the covenant tests and baskets | High | CP-1, CP-2, CP-5 | Add the executed agreement (exhibit 10.1 to the March 31, 2026 10-Q). Until then covenant definitions are management-described and headroom is not verifiable against legal text. |
| Not supplied: the indentures for the senior unsecured notes and the AR Facility documents | Medium | CP-1A, CP-2 | Add the indentures; note terms (call, change of control, covenants) are known only from the filings' summaries. |
| Not supplied: exhibit 22.1, the list of issuers and guarantor subsidiaries | Medium | CP-1A, CP-2 | Add it from the June 30, 2026 10-Q exhibits. The guarantor perimeter rests on the narrative description. |
| Not extracted: the 10-K organizational structure chart (10-K_2025-12-31_gel-20251231.htm.jsonl page:9) | Medium | CP-1A | Obtain the chart image or a text equivalent. |
| Unresolved conflict: cash used in the covenant ratio versus balance sheet cash | Medium | CP-1, CP-5 | Reconcile through the credit agreement definition; carry both labelled. |
| Unresolved conflict: whether the $10.5 million inventory financing item is a sublimit size or an outstanding borrowing | Medium | CP-1, CP-5 | Confirm from the credit agreement or a later filing; do not net it silently. |
| Not supplied: numerical 2026 Adjusted EBITDA guidance range and the year-end call it came from | Low | CP-2 | Add the call transcript or the earlier release if guidance is to be quoted. |
| Not supplied: investor presentations, rating agency reports, market data and peer data (the context leaves ratings, quotes and peers blank) | Low | CP-2 | Not needed for source readiness; relative value and ratings are out of the requested scope. |
| Not supplied: a stand-alone fourth-quarter 2025 statement; only FY2025 (10-K) and nine months 2025 (comparatives) are printed | Low | CP-1 | Derive downstream only with the period labelled, or use the quarters printed in the filings. |
| Extraction fidelity not reviewed: tables are flattened text; no image, chart or formatting inspection | Low | all | Spot-check table headers against the filing when a figure is used. |
| Management claims in releases (outlook, ahead-of-expectations remarks, cost-of-capital statements) are attributed claims, not filed facts | Low | CP-1A, CP-2 | Cite as management language. |
| The pack is one issuer with no draft or unsigned material; the 10-K is audited and the 10-Qs are unaudited | Low | all | Label the audit status of each figure. |

## Next module

Run CP-1 next, then CP-1A, then CP-2 and CP-5, in the order the dependency planner sets. Carry these limitations forward: (1) covenant ratio, debt and cash inputs are management-reported and the credit agreement is not supplied; (2) the cash and inventory-financing differences between the Q3 10-Q and the Q3 release are unreconciled; (3) the AR Facility is inside balance sheet debt but outside the release's adjusted debt; (4) the 10-K describes the superseded credit agreement; (5) 2025 comparatives separate the discontinued Alkali Business; (6) the organization chart and guarantor list are not available. The next evidence action is to add the Eighth credit agreement, the note indentures and exhibit 22.1 if covenant headroom or structural ranking must be verified against executed terms.
