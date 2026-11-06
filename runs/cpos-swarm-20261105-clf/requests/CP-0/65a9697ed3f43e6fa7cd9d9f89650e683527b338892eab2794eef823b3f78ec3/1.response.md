# CP-0 — Source readiness: CLEVELAND-CLIFFS INC. (clf)

## Request

- Issuer: CLEVELAND-CLIFFS INC. (issuer id `clf`, NYSE: CLF), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026; prior period FY2025 (context `run`).
- Run: `clf-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The analyst read the pinned page files and wrote this answer. No provider was called.
- Question: can the supplied public filings support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion. No figure is normalized, reconciled or newly derived in this module.
- Locators: `page:N` is the source chunk number in the pinned `.jsonl` file, not a printed page number. Each pinned file is contiguous from page:1 to its last page with no empty chunk.

## Sources

Issuer sources relied on (name and pinned sha256 of the `.jsonl` file CP-OS supplies):

| Source | sha256 | Chunks | Role |
| --- | --- | --- | --- |
| 10-K_2025-12-31_clf-20251231.htm.jsonl | 4c221bc0965bff2fddf7c4bff630fa79a69227de30709426ec9a8c89ce97e2df | page:1 to page:179 | Annual report on Form 10-K for the year ended December 31, 2025 |
| 10-Q_2026-03-31_clf-20260331.htm.jsonl | cdb78421e299c29e406bbc729a020af9f5e9e2600a8725769f4fc9cce3f48238 | page:1 to page:58 | Quarterly report on Form 10-Q for the quarter ended March 31, 2026 |
| 10-Q_2026-06-30_clf-20260630.htm.jsonl | e0ba1bee447b92cbe2b9ad67268169c4ba2e392089bcf206be2b86a11c01f94b | page:1 to page:61 | Quarterly report on Form 10-Q for the quarter ended June 30, 2026 |
| 10-Q_2026-09-30_clf-20260930.htm.jsonl | c3188e1da0b49175580c8c9484ba8f4a1c413725f4f518851b880884f79957d1 | page:1 to page:63 | Quarterly report on Form 10-Q for the quarter ended September 30, 2026 |
| EX-99.1_2026-04-20_clf-202603318xkex991.htm.jsonl | b9c8fc8d9b4361337a220b73ac602738ac2f0a283bbd73c7b1429c171ac6000c | page:1 to page:9 | Exhibit 99.1 news release dated April 20, 2026 (first quarter 2026) |
| EX-99.1_2026-07-23_clf-202606308xkex991.htm.jsonl | 6e73622f8701012d98293b6d350054a601691c0c525be23eff4b4255d0c4ab32 | page:1 to page:10 | Exhibit 99.1 news release dated July 23, 2026 (second quarter 2026) |
| EX-99.1_2026-10-19_clf-202609308xkex991.htm.jsonl | e6cabc90a6962f04fc1da1253ad4fc1e70365df28408b401d69ed58092c0c0e1 | page:1 to page:10 | Exhibit 99.1 news release dated October 19, 2026 (third quarter 2026) |
| context | 9824d18b9e3851ae3ee2ee1eb294b36a7465c031f02ec1e26c0d1341d4ae46e3 | not paged | User run settings; not issuer evidence. Blank fields (ratings, quotes, market data, borrower, parent, guarantors) are not zero |

Ignored by CP-OS: `_retrieval.json` (pack index, not evidence).

Supplied handoffs: none. CP-0 is the first module in this run.

Lineage note: the first line of each page:1 chunk names the original `.htm` file and its own sha256 (for example the Q3 10-Q: "Visible text of 10-Q_2026-09-30_clf-20260930.htm, sha256 5e70dc3037e10e9c0f660a7030cf28c5fa3192a5766c1fff10981eca8687e647"). That is the hash of the filed HTML the text was taken from. The pinned hashes in the table above are those of the page files and are the ones this run is bound to.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied filings and releases are enough to run the four selected analyses on the issuer's reported financials, debt, liquidity and business, with stated limits. Nothing needed is blocked. | High | No indentures, credit agreement, ratings or market data are supplied, so covenant levels and trading views cannot be verified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Filed statements run from FY2025 through September 30, 2026, so quarter, nine-month and last-twelve-month views can be built from filed figures. | Supports leverage and coverage work on filed numbers; management adjusted figures stay labelled as management measures. | High |
| Debt is itemized note by note and the revolver capacity table is printed each quarter. Reported liquidity was $3.2 billion at September 30, 2026. | Liquidity and maturity work can rest on filed tables. The springing covenant trigger level is not given. | High |
| Management says a major debt reduction is expected in the fourth quarter from free cash flow and property sale proceeds. The filings give no detail of that sale. | The expected deleveraging cannot be verified or sized from the supplied sources. | Medium |
| A few labels and wordings differ between documents, for example an availability label in the first-quarter filing and the leverage-target wording in two releases. | Each must be carried as logged, not resolved, so a reader does not pick one silently. | Medium |

### Readiness view

The effective source set supports all four selected consumers with bounded limitations (READY_WITH_LIMITATIONS for each). The set holds the audited FY2025 annual report, three unaudited interim reports for 2026 and three earnings releases, all issued by the issuer and all dated on or before 2026-10-20, so nothing is later than the cutoff. No source is blocked, and none is used as a fallback for another. The limits are about what is absent, not about what is present: executed debt documents, ratings and market data are not supplied; the earnings presentations the releases point to are not supplied; and the property sale behind the expected fourth-quarter debt reduction is not described in any filed source. None of these is a missing downstream analytical handoff, so none makes a consumer CONDITIONAL. Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Consumer readiness

| Consumer | Status | Evidence located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Annual statements, page:109 to page:110 of the 10-K; Q3 interim statements, 10-Q Q3 page:3 to page:6; debt note, 10-K page:131 to page:140 and 10-Q Q3 page:15 to page:16; liquidity, 10-Q Q3 page:46; Adjusted EBITDA reconciliation, 10-Q Q3 page:47 and release page:10 | Adjusted EBITDA is a non-GAAP issuer measure; net debt is not defined in any filing; covenant threshold and indenture terms not supplied; segment revenue basis differs between two tables (see conflicts) |
| CP-1A | READY_WITH_LIMITATIONS | Business, segments and strategy, 10-K page:5 to page:30 and 10-Q Q3 page:11, page:36 to page:38; Stelco acquisition note, 10-K page:124 to page:126; POSCO Memorandum of Understanding, 10-K page:9 and 10-Q Q3 page:37 to page:38 | POSCO terms are described as subject to definitive agreements; the property sale named in the Q3 release is not described; presentations not supplied; management language in releases is attributed, not adopted |
| CP-2 | READY_WITH_LIMITATIONS | Can draw on CP-1 and CP-1A outputs plus the located liquidity, springing covenant, guarantor and obligated-group text (10-Q Q3 page:15, page:46, page:48 to page:49) | No ratings, market data or peer data supplied; legal documents not supplied; an upstream gap flows to the synthesis |
| CP-5 | READY_WITH_LIMITATIONS | Every source is paged text with stable `page:N` locators, so citations can be opened and matched | Text extraction only: tables are flattened and one stray character was found; no HTML or XBRL view is supplied for layout checks |

### Source register

#### Form 10-K for FY2025 (10-K_2025-12-31_clf-20251231.htm.jsonl)

- Family and authority: filed annual report; original authority for audited consolidated statements. page:1: "For the fiscal year ended December 31, 2025", "Commission File Number: 1-8944 CLEVELAND-CLIFFS INC.".
- Audit: page:165 "We have served as the Company's auditor since 2004."; page:168 "DELOITTE & TOUCHE LLP Cleveland, Ohio February 9, 2026". The pack index lists the filing date as 2026-02-09 (index only, not issuer evidence).
- Statements: statements of operations at page:109, cash flows at page:110. Debt and credit facilities note (NOTE 8) at page:131 to page:140, with the instrument table at page:131 and ABL capacity table at page:140. Leases (NOTE 12) at page:152 to page:153, pensions (NOTE 9) at page:141 to page:147, commitments (NOTE 20) at page:160 to page:163, subsequent events (NOTE 21) at page:163. Adjusted EBITDA reconciliation at page:93, guarantor and obligated-group information at page:94 to page:95.
- Units and perimeter: "In millions" tables, USD. Consolidated Cleveland-Cliffs Inc. and subsidiaries, with noncontrolling interests. The issuer of the senior notes and borrower under the ABL Facility is Cleveland-Cliffs Inc. (page:132 footnote 2: "Refers to Cleveland-Cliffs Inc. as borrower under our ABL Facility").
- Version relationships: this is the only annual report; it is the comparative base for the interim reports.

#### Form 10-Q for the quarter ended March 31, 2026 (10-Q_2026-03-31_clf-20260331.htm.jsonl)

- Family and authority: filed, unaudited condensed interim report. page:1 "For the quarterly period ended March 31, 2026". Balance sheet at page:3, cash flows at page:4 ("Net cash used by operating activities (325) (351)"), debt note at page:12 to page:13, MD&A liquidity at page:40, subsequent events at page:24 (NOTE 19).
- Role: separate active source for Q1 2026. It is not superseded by the later 10-Qs, which carry year-to-date figures.

#### Form 10-Q for the quarter ended June 30, 2026 (10-Q_2026-06-30_clf-20260630.htm.jsonl)

- Family and authority: filed, unaudited condensed interim report. page:1 "For the quarterly period ended June 30, 2026". Cash flows at page:4 to page:5 (six months), debt note and ABL capacity at page:15, MD&A liquidity at page:44, subsequent events at page:26 (NOTE 19).
- Role: separate active source for Q2 2026 and the six-month period.

#### Form 10-Q for the quarter ended September 30, 2026 (10-Q_2026-09-30_clf-20260930.htm.jsonl)

- Family and authority: filed, unaudited condensed interim report; latest filed periodic report in the pack. page:1 "For the quarterly period ended September 30, 2026"; "570,584,966 as of October 20, 2026"; signature date page:63 "Date: October 20, 2026".
- Statements: financial position page:3, operations page:4, comprehensive income page:4, cash flows page:5, equity page:5 to page:6, all for the three and nine months ended September 30, 2026 and 2025 or the stated comparatives. Debt note page:15 to page:16, segment note page:11 to page:13, commitments page:24 to page:27, subsequent events page:27, MD&A liquidity page:46, Adjusted EBITDA page:47, guarantors page:48 to page:50.
- Exhibit list at page:62 to page:63 names Exhibit 22 (obligated group schedule), certifications and Inline XBRL exhibits as filed with the 10-Q; none of those exhibits is in the pack.

#### Earnings releases, Exhibit 99.1 (three files)

- First quarter: page:1 "Cleveland-Cliffs Reports First-Quarter 2026 Results", dated April 20, 2026. Second quarter: page:1 dated July 23, 2026. Third quarter: page:1 dated October 19, 2026.
- Family and authority: management-prepared, unaudited news releases furnished as exhibits. They give attributed supporting claims (outlook, quotations from the Chairman and CEO) and non-GAAP reconciliations. A management claim cannot override a filing.
- The Q3 release restates the statements of operations, financial position and cash flows (page:7 to page:8) and gives a discrete Q2 2026 column ("Three Months Ended Jun. 30, 2026"), which a reader needs because the 10-Qs give only year-to-date columns for later periods. Quarter-versus-year-to-date columns are labelled on each table.
- Each release points to an earnings presentation not supplied: Q3 release page:3 "Additional outlook details can be found on page 10 of the earnings presentation published this morning". The pack index lists no presentations.

### Identity and perimeter

- Reporting entity and issuer: Cleveland-Cliffs Inc., Ohio (10-Q Q3 page:1), parent and issuer of all nine senior note series and borrower under the ABL Facility. The context leaves borrower, parent and guarantor fields blank, which is not evidence of their absence.
- Guarantors: the 10-K (page:136) says eight series are "guaranteed on a senior unsecured basis by our material direct and indirect wholly owned domestic subsidiaries" and "There are no subsidiary guarantees of the interest and principal amounts for the 6.250% 2040 Senior Notes." The 10-Q guarantor sections (Q3 page:48) list the same eight series. The entity list is in Exhibit 22, which is not supplied.
- ABL Facility: guaranteed by certain U.S. subsidiaries and secured (10-K page:139: "first-priority security interest in the accounts receivable"). Commitments are split into a $4.25 billion tranche for the Company and certain U.S. subsidiaries and a $500 million tranche for certain Canadian subsidiaries (10-K page:139). The quarterly capacity tables do not show availability by tranche.
- Restricted versus unrestricted entities: not described in the supplied text beyond the guarantor description. Unresolved distinction kept as a gap.
- Non-guarantor and noncontrolling perimeter: Stelco (Canada) is consolidated; noncontrolling interests are $279 million at September 30, 2026 (10-Q Q3 page:3). The guarantors are described only as "domestic" subsidiaries and none is named, so whether Stelco is a guarantor is not stated in the supplied text.
- Currency and units: all statements are "In millions" US dollars (10-Q Q3 page:2: "References to “$” is to United States currency, unless otherwise stated"). Canadian operations are consolidated in USD. The debt table does not state the currency of ABL borrowings drawn by the Canadian tranche borrowers.

### Document conflicts and differences logged (not reconciled)

| # | Items | Locators | Downstream effect |
| --- | --- | --- | --- |
| 1 | Q1 10-Q labels two different amounts "available borrowing base". The Note 7 table prints "Available borrowing base on ABL Facility1 $ 4,103" and "Borrowing capacity available $ 3,096"; the MD&A says "The available borrowing base, which was $3.1 billion as of March 31, 2026" | 10-Q Q1 page:13 and page:40 | A reader of the MD&A text alone would read availability as the borrowing base. CP-1 must take the Note 7 table as the controlling labelled figure and carry the MD&A wording as a label inconsistency. The Q2 and Q3 10-Qs do not repeat the MD&A sentence |
| 2 | Management leverage target is worded differently: Q2 release "under 2.5x debt to EBITDA by this time next year"; Q3 release "under 2.5x net debt to EBITDA by the middle of next year" | EX-99.1 Q2 page:2; EX-99.1 Q3 page:1 | Different numerator and timing. No filing defines net debt or the ratio. CP-1A and CP-2 must quote each as management language and not compute against it as a covenant |
| 3 | Q3 release says the decision was made to "indefinitely idle our galvanizing lines at Stelco"; the Q3 10-Q says "indefinitely idle the finishing operations at our Hamilton Works facility" | EX-99.1 Q3 page:2; 10-Q Q3 page:29 and page:37 | Scope wording differs (galvanizing lines versus finishing operations) and no supplied text states that Hamilton Works is the Stelco site. CP-1A must not equate them |
| 4 | Steelmaking revenue for the three months ended September 30, 2026 appears as $5,492 million in the segment note and $5,447 million in the revenue-by-market note and release | 10-Q Q3 page:11 ("Revenues $ 5,492 $ 169 $ (49) $ 5,612"); 10-Q Q3 page:10 ("Total Steelmaking 5,447"; "Revenue by market and product are presented net of intersegment revenues"); EX-99.1 Q3 page:2 | Different bases, both stated: segment revenue includes intersegment sales, the market table is net of them. CP-1 must label which basis each figure uses. Not an error |
| 5 | 10-K redemption text for the 7.375% 2033 notes reads "The 7.375% 2029 Senior Notes are redeemable prior to May 1, 2028" and the schedule steps "decreasing to 100% on November 1, 2028", the same date given for the 6.875% 2029 notes | 10-K page:138; compare page:136 | Likely a text error in the filing, but the indenture is not supplied to confirm. Redemption terms for that series are carried as unverified |
| 6 | Release statement of operations prints a stray character in the nine-month 2026 column: "Asset impairment — — 0 — (39)"; the 10-Q prints a dash | EX-99.1 Q3 page:7; 10-Q Q3 page:4 | Extraction or typographic artifact. The 10-Q controls; no figure changes |
| 7 | Secured note capacity is stated as "approximately $3.2 billion" (10-K, Q1 10-Q) and "approximately $3 billion" (Q2 and Q3 10-Qs) | 10-K page:91; 10-Q Q1 page:40; 10-Q Q2 page:44; 10-Q Q3 page:46 | A change in a rounded management estimate, not a conflict. Carry the quarter-specific value and do not infer the cause |

No conflict was found between filed statements and the releases on revenue, net income, cash, long-term debt or Adjusted EBITDA for the periods they share (Q3 2026: revenue $5,612 million, net income $165 million, Adjusted EBITDA $612 million in both 10-Q Q3 page:4, page:47 and EX-99.1 Q3 page:7, page:10).

### Information-availability boundary

- Latest filed periodic report: 10-Q Q3 dated October 20, 2026 (page:63). Latest release: October 19, 2026. Both are before the cutoff 2026-11-05.
- Nothing dated between October 20, 2026 and 2026-11-05 is supplied. Events in that window, for example debt repayments, the property sale, a POSCO agreement or ratings actions, are Not supplied, not absent.
- Subsequent events: the 10-Q Q3 NOTE 19 reads "We have evaluated subsequent events through the date of financial statement issuance." and lists nothing (page:27). The 10-K NOTE 21 and the Q1 and Q2 10-Q subsequent-events notes use the same wording.
- Forward-looking statements in the releases (fourth-quarter 2026 outlook, 2027 outlook) are management guidance dated October 19, 2026 and are not facts about reported periods.

### Source profile reviews

- Financial reports (10-K and three 10-Qs): statements, notes, period labels and footnotes are located. Debt table by instrument with effective rates (10-Q Q3 page:15), maturities by year (page:16), ABL capacity (page:15), fair value of debt (page:19), letters of credit (page:46), guarantor information (page:48 to page:49), pension and OPEB cost components (page:16), supply chain finance programs (page:9), purchase commitments (page:24), leases at year end only (10-K page:152 to page:153). Cash paid for interest is printed for nine months (10-Q Q3 page:9: "Interest paid on debt obligations net of capitalized interest1 411 341").
- Earnings releases: reported and adjusted figures with reconciliations (Q3 release page:9 to page:10), quarter versus nine-month columns labelled, guidance, attributed management narrative. Adjusted figures are issuer non-GAAP measures with reconciliations to net income.
- Legal and financing sources: none supplied (context `legal_documents: none`). Only descriptive summaries inside the notes exist. No definitions, baskets, thresholds or schedules from the indentures or the ABL credit agreement can be opened.
- Workbooks: none. Scans, images and decks: none supplied. Charts in the filed documents are not represented in the text extraction; this is a parse gap for chart content only. Statement and note text is complete.
- Coverage units: every chunk of every source is retained, and none is excluded. No coverage unit is claimed as inspected as an image.

#### Quarter and year coverage for CP-1

| Period | Where located | Basis |
| --- | --- | --- |
| FY2025, FY2024, FY2023 | 10-K page:109 to page:110, page:93 | Audited statements; Adjusted EBITDA unaudited non-GAAP |
| Q1 2026 and Q1 2025 | 10-Q Q1 page:3 to page:4, page:41 | Three months, unaudited |
| Q2 2026 discrete, six months 2026 | 10-Q Q2 page:4 to page:5; EX-99.1 Q3 page:7 to page:10 (Q2 column) | Three and six months, unaudited |
| Q3 2026, nine months 2026 and 2025 | 10-Q Q3 page:3 to page:6, page:47 | Three and nine months, unaudited |
| Fourth quarter 2025 discrete | Not printed as a statement in the pack; EX-99.1 Q1 page:1 gives some fourth-quarter 2025 comparatives | A derived figure would need FY2025 and nine-month 2025 inputs; not computed here |
| Last twelve months to September 30, 2026 | Not printed; its inputs (FY2025, nine months 2026, nine months 2025) are all located | Left to CP-1 |

### Analytical read-through

- Usable coverage: the annual report and three interim reports give statements, debt tables, liquidity tables and the springing covenant statement at each quarter end from December 31, 2025 to September 30, 2026. The three releases add the discrete Q2 2026 column and management outlook. Quarter-end liquidity statements in the filings and releases agree with the capacity tables printed beside them.
- Strongest contrary evidence and limits: the 10-K says of the notes it describes that "there are no financial covenants" (page:133, page:134, page:138) and the ABL covenant is a springing fixed charge test "of 1.0 to 1.0" (10-Q Q3 page:15). The level of availability that triggers the test is not printed anywhere in the pack, and the indentures and credit agreement are not supplied. A consumer that reports covenant headroom would have nothing to measure it against.
- Source risk mechanism: management expects "a major debt reduction in the fourth quarter" from free cash flow and "property sale proceeds" (EX-99.1 Q3 page:1). The filed 10-Q gives no property sale description and the subsequent events note is empty. A synthesis that credits the reduction would rest on a management claim only, so it must be attributed and labelled unverified. Similarly, the POSCO Memorandum of Understanding is stated to be "subject to negotiation of definitive terms" (10-Q Q3 page:37 to page:38), so its debt-reduction proceeds cannot be assumed.
- What cannot proceed: covenant headroom against agreement definitions, guarantor-level or restricted-group analysis, recovery or priority analysis from executed documents, rating-based or market-based comparison, and any verification of the property sale or the POSCO transaction terms.
- Next evidence action: supply the indentures for each note series, the ABL Facility credit agreement and its amendments, Exhibit 22, any Form 8-K between October 20, 2026 and 2026-11-05, the earnings presentations, and any rating agency reports. Until then these stay Not supplied.

## Calculations

No new derived figure is produced; CP-0 does not normalize, reconcile or calculate. The checks below only tie out figures that the sources print, to test that the extraction is faithful. They feed nothing downstream.

| Check | Inputs (millions of USD) | Result | Printed |
| --- | --- | --- | --- |
| Q3 2026 ABL capacity | 4,060 - 834 - 57 (10-Q Q3 page:15) | 3,169 | "Borrowing capacity available $ 3,169" |
| Q3 2026 liquidity statement | 77 + 3,169 (10-Q Q3 page:3, page:15) | 3,246 | "$3.2 billion in liquidity" (page:46) |
| Q2 2026 ABL capacity | 3,969 - 895 - 60 (10-Q Q2 page:15) | 3,014 | "Borrowing capacity available $ 3,014" |
| Q1 2026 ABL capacity | 4,103 - 959 - 48 (10-Q Q1 page:13) | 3,096 | "Borrowing capacity available $ 3,096" |
| Q3 2026 debt principal | 368 + 900 + 750 + 325 + 850 + 1,425 + 900 + 1,125 + 235 + 834 (10-Q Q3 page:15) | 7,712 | "Total principal amount 7,712" |
| Q3 2026 maturity table | 834 + 1,268 + 750 + 4,860 (10-Q Q3 page:16) | 7,712 | "Total 7,712" |
| Q3 2026 carrying value | 7,712 - 67 (page:15) | 7,645 | "Total long-term debt $ 7,645" |
| Second-quarter operating cash flow | (95) - (325) (10-Q Q2 page:5; 10-Q Q1 page:4) | 230 | "Operating cash flow of $230 million" (EX-99.1 Q2 page:1) |
| Third-quarter operating cash flow | 129 - (95) (10-Q Q3 page:5; 10-Q Q2 page:5) | 224 | 224 (EX-99.1 Q3 page:8) |
| Q3 2026 segment revenue | 5,492 + 169 - 49 (10-Q Q3 page:11) | 5,612 | "Total revenues $ 5,612" |

All ten tie. The Q1 and Q2 liquidity statements (about $3.1 billion each) also agree with their capacity tables plus cash of $45 million (10-Q Q1 page:3) and $70 million (10-Q Q2 page:3).

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Indentures for the nine senior note series and the ABL Facility credit agreement and amendments not supplied; springing covenant trigger level not printed in any source | High for covenant work; Medium for CP-2 | CP-1, CP-2 | Supply executed documents. Until then covenant levels and headroom are Not supplied |
| Exhibit 22 (obligated group entity list) not supplied; guarantor status of Stelco and other foreign subsidiaries not stated | Medium | CP-1A, CP-2 | Supply Exhibit 22 from the 10-K and 10-Q |
| Property sale named in the Q3 release as a source of debt reduction is not described in any filed source; Q3 10-Q NOTE 19 lists no subsequent event | Medium | CP-1A, CP-2 | Supply the relevant Form 8-K if one exists between October 20, 2026 and 2026-11-05 |
| Events between October 20, 2026 and the as-of date 2026-11-05 not supplied | Medium | CP-1A, CP-2 | Supply later 8-Ks or confirm none |
| Earnings presentations referenced by the releases not supplied (pack lists none) | Low | CP-1A | Supply if outlook detail on "page 10 of the earnings presentation" is needed |
| POSCO Memorandum of Understanding terms not supplied beyond the 10-K and 10-Q description; definitive agreements not signed per the filings | Medium | CP-1A, CP-2 | Supply the MoU or definitive agreements if signed. Do not assume proceeds |
| ABL availability by U.S. and Canadian tranche not printed | Low | CP-1 | Supply the borrowing base certificate or credit agreement if tranche liquidity is needed |
| Lease maturity table and lease balances at September 30, 2026 not in the 10-Q set; leases only at December 31, 2025 (10-K page:152 to page:153) | Low | CP-1 | Use the year-end table and label it as of December 31, 2025 |
| Pension and OPEB funded status only at December 31, 2025 (10-K page:141); 10-Qs give cost components and balance sheet lines only | Low | CP-1 | Use year-end funded status and label it |
| Ratings, market capitalization, quotes, peers: context fields blank; no rating agency report supplied | Low for selected modules | CP-2 | Not required for this scope; keep Not supplied |
| Text extraction only: charts not represented; no HTML or XBRL for layout checks; one stray character found (conflict 6) | Low | CP-1, CP-5 | Check any flagged table against the filed HTML when available |
| Net debt and the management leverage ratio are not defined in any filing | Medium | CP-1, CP-2 | Define net debt explicitly in CP-1 from filed lines if used; label as analyst-defined |

## Next module

- CP-1: use the 10-K and 10-Q statements as controlling and the releases for the discrete Q2 2026 column and non-GAAP reconciliations. Keep three-month, nine-month and year columns separate and label every figure. Take the Note 7 capacity table as the labelled liquidity input and carry conflict 1. Keep Adjusted EBITDA as the issuer non-GAAP measure. Label the segment versus market revenue basis (conflict 4). Carry the covenant and indenture gaps.
- CP-1A: carry the POSCO Memorandum of Understanding as non-binding, subject to definitive agreements (10-K page:9; 10-Q Q3 page:37 to page:38), and the Stelco galvanizing and Hamilton Works wording as logged (conflict 3). Treat the property sale and the fourth-quarter debt reduction as management language, Not supplied in filings. Label any event after October 20, 2026 as Not supplied.
- CP-2 and CP-5: carry the missing executed documents, Exhibit 22, ratings and market data as restrictions. Quote the two leverage-target wordings (conflict 2) as management language only.
