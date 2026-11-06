# CP-0 — Source readiness: Bausch Health Companies Inc. (bhc)

## Request

- Issuer: Bausch Health Companies Inc. (issuer id `bhc`), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD, current period Q3 2026, prior period FY2025 (context).
- Run: `bhc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host searched and read the pinned files and wrote this answer. No provider was called.
- Question: can the supplied public filings and earnings releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This answer gives no credit conclusion, legal interpretation or investment opinion and normalizes, reconciles or calculates no figure.

## Sources

Issuer sources relied on (the page-numbered text extractions CP-OS pinned; a locator `page:N` is the extraction chunk, not a printed page):

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_bhc-20251231.htm.jsonl | dd4233546d8f09a0a7172210eae9b856cf06217c0da999f68b6e9a8283f6671d | Annual report on Form 10-K for the fiscal year ended December 31, 2025 (343 chunks) |
| 10-Q_2026-03-31_bhc-20260331.htm.jsonl | 2ab4f9a58a29bd8e4f27c1aaa3b34a916ad63a6c5e24a2f2cf1f677d2bf1adb3 | Quarterly report on Form 10-Q for the quarter ended March 31, 2026 (124 chunks) |
| 10-Q_2026-06-30_bhc-20260630.htm.jsonl | 9bd8cebbf75325a6e2424a90dc4ffd52c51b1a73535e612ffb413df53a0d5061 | Quarterly report on Form 10-Q for the quarter ended June 30, 2026 (134 chunks) |
| 10-Q_2026-09-30_bhc-20260930.htm.jsonl | bbe6464eac7c28eba7ae73d3d4c1550a00ee295236fd32b72332e63bba1b2690 | Quarterly report on Form 10-Q for the quarter ended September 30, 2026 (139 chunks) |
| EX-99.1_2026-04-29_ex991-q1x2026.htm.jsonl | a03142c8b51f52ce0bcea39df704d05d1ec6cd25d01c476f43f591aef5327135 | Exhibit 99.1 first quarter 2026 earnings release dated April 29, 2026 (26 chunks) |
| EX-99.1_2026-07-29_ex991-q22026.htm.jsonl | b572ec3ee8791446c7753f44c437564f85dc7c22a9282dc8fe3094943c7ca9ed | Exhibit 99.1 second quarter 2026 earnings release dated July 29, 2026 (30 chunks) |
| EX-99.1_2026-10-28_ex991-q32026.htm.jsonl | d176e2b2337e8c9ee765792690a4c9894f8e78c9eadadca91a11afce842a8bb9 | Exhibit 99.1 third quarter 2026 earnings release dated October 28, 2026 (28 chunks) |
| context | ce3ba040ad702f7a097a4705cf09e05a5541c48113a20eaf4b83ee334242bc43 | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module, so no upstream handoff exists.

Not relied on: `_retrieval.json` (a retrieval log, ignored by CP-OS, not issuer evidence). No investor presentation is in the pack; the three earnings releases stand in for presentations.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases cover the annual and three quarterly reporting periods and the debt, liquidity and covenant text that the downstream work needs, so analysis can proceed with stated limitations. | Medium | No credit agreement, indenture or lease document is supplied, so covenant definitions and the reported covenant ratio cannot be checked. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Statements are consolidated and include the majority-owned Bausch + Lomb, whose debt sits outside the covenant group of the parent. | Consolidated figures overstate what the parent group can access or must test; the split must be carried forward. | High |
| The only financial maintenance covenant text is on the revolving facility, and its step-up date is defined in a document not supplied. | Covenant headroom cannot be computed from the pack. | High |
| Debt maturities and revolver availability are printed in the latest quarterly report. | Liquidity and the maturity wall can be built from printed figures. | High |
| Several events after quarter end are disclosed, including a note redemption announced for November 2026. | They must be treated as subsequent events, not as September 30, 2026 balances. | Medium |

### Readiness view

The effective source set can support all four requested consumers with bounded limitations. The three quarterly reports and the annual report are filed documents with consolidated statements, a financing note, a covenant description and liquidity discussion. The three releases add management-defined adjusted measures, segment revenue and guidance, and are attributed supporting claims, not controlling facts. The command sheet reads CP-1 RUN, CP-1A RUN, CP-2 RUN and CP-5 RUN, each READY_WITH_LIMITATIONS. No consumer is CONDITIONAL or BLOCKED, because the missing items (executed debt agreements, a covenant compliance figure, Bausch + Lomb's own filings) narrow depth and do not remove the statements those consumers need.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025 statements (10-K, auditor report at page:212; balance sheet at page:218; cash flows at page:220) and unaudited Q1, Q2 and Q3 2026 condensed statements with comparatives are located. Debt note, maturity table and cash-by-entity split are located. Text extraction flattens tables; no original HTML or XBRL is supplied. |
| CP-1A | READY_WITH_LIMITATIONS | Business description and segments (10-K page:7 to page:14, 10-Q Q3 page:9), the Bausch + Lomb ownership and separation status (10-Q Q3 page:9 to page:10), the refinancing history (10-Q Q3 page:29 to page:30) and subsequent events (10-Q Q3 page:76) are located. Executed debt documents and Bausch + Lomb's own filings are not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Can synthesize from CP-1 and CP-1A plus located covenant, liquidity, rating and litigation text. The covenant ratio and the Covenant Step Up Date are not in the pack. |
| CP-5 | READY_WITH_LIMITATIONS | Every source has stable chunk numbers, so claims can be traced. Layout and table-fidelity checks against the filed HTML cannot be done from text extraction. |

### Source register

#### Form 10-K for FY2025 (`10-K_2025-12-31_bhc-20251231.htm.jsonl`)

- Family and authority: filed annual report, original authority for audited consolidated statements. page:1 reads "For the Fiscal Year Ended December 31, 2025" and "Commission File Number: 001-14956". Directors' signature dates on page:211 are February 2026, and the liquidity section dates revolver availability "As of February 18, 2026" (page:176).
- Audit: page:211 index lists "Report of Independent Registered Public Accounting Firm (PCAOB ID 238)"; page:215 presents critical audit matters (Medicaid rebates and sales returns allowances; goodwill impairment assessments of the Salix and Generics reporting units, page:217).
- Statements and notes located: balance sheet page:218, cash flows page:220, financing note "10.FINANCING ARRANGEMENTS" starting page:269 with the instrument table, maturities at page:56, page:136 and page:173, lease note at page:301, segment note referenced as Note 23.
- Perimeter: consolidated Bausch Health Companies Inc. with noncontrolling interest, including Bausch + Lomb. Currency: USD per the context; the Q3 10-Q states that "references to “$” are to United States (“U.S.”) dollars" (page:3). A statement of currency inside the 10-K itself was not located by search, so the 10-K currency rests on the context setting and the table headings.

#### Forms 10-Q for Q1, Q2 and Q3 2026 (three files)

- Family and authority: filed, unaudited quarterly reports. Each cover page states its period: "For the Quarterly Period Ended March 31, 2026" (Q1 page:1), "June 30, 2026" (Q2 page:1) and "September 30, 2026" (Q3 page:1).
- Q3 10-Q statements: balance sheet at September 30, 2026 and December 31, 2025 (page:5 to page:6), statements of operations for three and nine months (page:6), cash flows for nine months (page:8). Note 10 "FINANCING ARRANGEMENTS" at page:27, covenant compliance at page:28 to page:29, 2025 Senior Secured Credit Facilities and covenant terms at page:31 to page:34, Bausch + Lomb facilities at page:34 to page:38, maturities at page:42, Note 17 legal proceedings from page:50, Note 18 segment information at page:74, Note 19 subsequent events at page:76. MD&A liquidity at page:126 to page:133, revolver availability and credit ratings at page:131.
- Q1 10-Q: balance sheet page:5, cash flows page:7, financing note page:25 onward, availability page:116. Q2 10-Q: balance sheet page:5, cash flows page:7, financing note page:26 onward, availability page:127.
- Version relationship: the Q3 report carries December 31, 2025 balance sheet comparatives; the quarterly reports are separate active sources, not replacements for one another. Q1 and Q2 are needed for discrete-quarter and nine-month movement; the Q3 report carries three-month and nine-month columns.

#### Earnings releases (three files, Exhibit 99.1)

- Family and authority: management-prepared, unaudited, furnished with Form 8-K. Datelines: "LAVAL, QC, April 29, 2026", "July 29, 2026", "October 28, 2026".
- Content: reported revenue by segment, adjusted EBITDA reconciliation for Bausch Health, Bausch + Lomb and "Bausch Health (excl. B+L)" (Q3 release page:28), adjusted net income reconciliation (page:22), adjusted cash flow reconciliation (page:27), debt maturity table (page:27) and full-year guidance (page:4).
- These are attributed supporting claims. Adjusted measures are management-defined and not GAAP. Where a release and a 10-Q state the same item, the 10-Q controls. The Q3 release states consolidated "Cash provided by operating activities $ 813" for the three months (page:27), a quarter-only figure; the Q3 10-Q cash flow statement is nine-month (page:8).

### Information-availability boundary

- All seven documents are dated on or before the cutoff. The latest are the Q3 release (October 28, 2026) and the Q3 10-Q, whose cover gives shares outstanding "as of October 23, 2026" (page:1) and whose subsequent-events note refers to October 29, 2026 (page:76).
- The Q3 10-Q contains forward-dated terms, not post-cutoff facts: the redemption of the 8.500% Senior Notes due 2027 is "scheduled for November 30, 2026" (page:76) and a mediation "is scheduled for November 3, 2026" (page:66), which is before the as-of date but whose outcome is not supplied. The redemption date is a contract term and is labelled as a future date. A mediation outcome after October 29, 2026 is Not supplied.
- Nothing dated after the Q3 10-Q and Q3 release and before 2026-11-05 is supplied. Events in that window are Not supplied, not absent.

### Identity and perimeter

- Reporting entity: Bausch Health Companies Inc., a British Columbia, Canada company; common shares on the NYSE and TSX under BHC (Q3 10-Q page:1). Statements are consolidated with its subsidiaries (page:3).
- Bausch + Lomb: Bausch Health "indirectly holds 310,449,643 common shares of Bausch + Lomb, which represents approximately 87%" (Q3 10-Q page:9). The unaudited statements "do not include any adjustments to give effect to the B+L Separation" (page:10). Consolidated cash is split in the MD&A between Bausch Health and Bausch + Lomb and "is generally not available to support" other entities unless paid as a dividend (page:127).
- Debt issuers and borrowers: the 2025 Credit Agreement borrower is 126NumberCo (a wholly owned indirect subsidiary, page:29); the 2032 Senior Secured Notes were issued by it (page:29) and the company with 126NumberCo exchanged notes in December 2025 (page:30); Bausch Health Americas, Inc. ("BHA") issues certain Senior Unsecured Notes (page:39); Bausch + Lomb is borrower under the B+L credit facilities and issuer of the B+L Senior Secured Notes (page:34 to page:38).
- Restricted and unrestricted status: 126NumberCo is a non-guarantor restricted subsidiary under the Existing Senior Notes indentures (page:30). Bausch + Lomb and its subsidiaries "continue to be unrestricted subsidiaries of the Company" and its earnings and net debt are excluded from the financial maintenance covenant calculation (page:40).
- Guarantors: described in prose (page:31, page:39). The Q3 10-Q gives non-guarantor summary figures on a non-consolidated basis (page:130). A named guarantor list is Not supplied in the pack.
- Context fields for borrower, parent, guarantors and sponsor are blank; blank is not evidence of absence.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, debt table, maturities, cash by entity, covenants, non-GAAP | 10-K page:218 to page:220, page:269; Q3 10-Q page:5 to page:8, page:27 to page:29, page:42, page:127; Q3 release page:22 to page:28 | Consolidated perimeter includes Bausch + Lomb; adjusted EBITDA is management-defined; text extraction |
| CP-1A | Business, segments, ownership, separation, refinancing history, subsequent events | 10-K page:7 to page:14; Q3 10-Q page:9 to page:10, page:29 to page:30, page:76 | Executed agreements and Bausch + Lomb filings not supplied |
| CP-2 | CP-1 and CP-1A outputs, covenants, liquidity, ratings, litigation | Q3 10-Q page:31 to page:34 (covenants), page:131 (availability, ratings), page:50 to page:74 (litigation) | Covenant ratio and Covenant Step Up Date not supplied; litigation outcomes after October 29, 2026 not supplied |
| CP-5 | Traceable claims | All seven sources carry chunk numbers | Original HTML and XBRL not supplied; extraction fidelity not reviewed |

### Debt, liquidity and covenant evidence located (for downstream use; not calculated here)

- Instrument table: Q3 10-Q page:27 lists principal and carrying amounts by instrument at September 30, 2026 and December 31, 2025, with a printed total of "$ 20,168" principal and "20,637" net of premiums, discounts and issuance costs. It includes the 2025 Credit Agreement 2030 Term Loan B Facility, the B+L Credit Facilities, Senior Secured Notes (including the 10.00% Secured Notes due April 2032), the B+L Senior Secured Notes and the Senior Unsecured Notes.
- Maturities: printed for the remainder of 2026 through thereafter (page:42), and split between "Bausch Health debt obligations" and "Bausch + Lomb debt obligations" (page:127 to page:128).
- Revolvers: the 2030 Revolving Credit Facility had "no outstanding borrowings" and "$31 million of issued and outstanding letters of credit" at September 30, 2026 (page:32) and "approximately $469 million of remaining availability" at October 28, 2026 (page:131). The B+L 2030 Revolving Credit Facility had "$100 million of outstanding borrowings" at September 30, 2026 (page:27) and "$666 million of remaining availability" at October 28, 2026 (page:131). Dates differ between the balance sheet and the availability statement.
- Covenants: the 2030 Revolving Credit Facility requires a Blended First Lien Leverage Ratio of not greater than "4.25:1.00" before the Covenant Step Up Date and "5.75:1.00" on and after it, and minimum liquidity of "$400 million" on and after it (page:34). The Company states compliance at September 30, 2026 (page:29). The B+L Term Facilities also contain financial covenants (page:28).
- Ratings as of October 28, 2026 (page:131): Moody's corporate rating Caa2, S&P B-, Fitch B for the Company; Moody's B1 and S&P B for Bausch + Lomb.
- Subsequent events (page:76): Bausch + Lomb CEO transition with a lump-sum payment of approximately "$75 million", a "$50 million" share repurchase authorization dated October 24, 2026, and the announced redemption of "approximately $643 million" of 8.500% Senior Notes due 2027, scheduled for November 30, 2026 and funded with cash on hand.

### Analytical read-through

- Usable coverage: filed statements for FY2025 and Q1 to Q3 2026 allow a consolidated reported view and a split of debt and cash between the parent group and Bausch + Lomb, because the 10-Q prints both splits (page:127 to page:128).
- Strongest contrary evidence: the parent's restricted group excludes Bausch + Lomb for covenant purposes (page:40), while the consolidated statements include it. A consumer reading only consolidated debt would mix two perimeters with different covenants and cash access. The releases present "Bausch Health (excl. B+L)" adjusted EBITDA (Q3 release page:28), which is management's own perimeter and not a covenant definition.
- Source risk mechanism: the covenant ratio is defined by terms of the 2025 Credit Agreement, which is not supplied, and no source prints the reported ratio or the Covenant Step Up Date. Evidence of a threshold without a numerator, a denominator or a date means headroom cannot be sourced and any figure computed by a consumer would be the analyst's estimate, not the covenant calculation.
- Premium accounting: the 2022 Exchange was a troubled debt restructuring, so some notes are carried at a premium and interest expense differs from contractual interest (page:40, page:131). Carrying value therefore differs from principal; consumers must state which they use.
- What cannot proceed: covenant headroom on agreement definitions, guarantor-level analysis, collateral-level recovery analysis, Bausch + Lomb standalone credit analysis.
- Next evidence action: supply the 2025 Credit Agreement and indentures (exhibits are listed in the 10-K at page:199 to page:211 but not included), Bausch + Lomb's own Form 10-Q, any compliance certificate or covenant calculation, and filings dated after October 29, 2026 if any.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Totals quoted above are printed in the sources.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| 2025 Credit Agreement, indentures, intercreditor and collateral documents not supplied; only filing summaries exist | High | CP-2, CP-5 | Supply executed agreements from the filing exhibit list |
| Reported Blended First Lien Leverage Ratio and liquidity covenant figure not printed in any source; searched "Blended First Lien", "leverage ratio" and "financial maintenance" across all seven sources | High | CP-2 | Supply compliance certificate or issuer covenant calculation |
| Covenant Step Up Date is "as defined in the 2025 Credit Agreement" and not stated in the filings | High | CP-2 | Supply the credit agreement |
| Bausch + Lomb standalone filings and its credit agreement not supplied; B+L covenant levels not printed | Medium | CP-1A, CP-2 | Supply Bausch + Lomb Form 10-Q and credit agreement |
| Named guarantor list and guarantor-level financials not supplied | Medium | CP-2 | Supply guarantor schedules or exhibit lists |
| Operating lease and pension disclosures are in the 10-K (lease table at page:301) but the Q3 10-Q has no lease or pension note; searches for "lease liabilit", "pension" and "operating lease" in the Q3 10-Q found only a pension line in other comprehensive loss (page:45) | Medium | CP-1, CP-2 | Treat December 31, 2025 lease balances as the latest available |
| No investor presentation in the pack; releases stand in | Low | CP-1A | Accept releases or supply decks |
| Events between October 29, 2026 and 2026-11-05 not supplied, including the outcome of a mediation scheduled for November 3, 2026 | Medium | CP-2 | Supply later 8-Ks or confirm none |
| Extraction is text only: no image, chart or table-layout inspection; extraction status is not a fidelity review | Low | CP-5 | Supply original HTML or XBRL |
| Adjusted EBITDA is management-defined and may differ from covenant EBITDA | Medium | CP-1, CP-2 | Carry the release definition and label it as non-GAAP |

## Next module

CP-1 follows with the full-statement extraction of FY2025 and Q1 to Q3 2026, carrying forward: the consolidated perimeter includes Bausch + Lomb; debt and cash must be shown for Bausch Health and for Bausch + Lomb separately using page:127 to page:128 of the Q3 10-Q; principal and carrying value differ; period labels must separate Q3 2026, nine months 2026 and FY2025; the covenant ratio is Not supplied. Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.
