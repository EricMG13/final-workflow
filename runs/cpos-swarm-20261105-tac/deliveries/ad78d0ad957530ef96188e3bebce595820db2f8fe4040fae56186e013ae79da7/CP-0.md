## Request

Module CP-0 (source readiness) for TRANSALTA CORP (issuer id tac, TransAlta Corporation, a Canadian federal company that files Form 40-F and furnishes Form 6-K), as of 2026-11-05. Pathway credit_snapshot, selected modules CP-0, CP-1, CP-1A, CP-2 and CP-5. Reporting currency CAD, current period Q3 2026, prior period FY2025, cutoff 2026-11-05. The question is only whether the pinned source set can support the requested work and what stays blocked. This handoff gives no credit conclusion and calculates nothing; every figure below is quoted from a source and the downstream modules must compute their own numbers. Source sufficiency is not completion of downstream analysis.

The reporting entity in every financial source is TransAlta Corporation and its subsidiaries (consolidated). No separate borrower, parent or guarantor is named in the context. The subsidiaries that matter to the debt perimeter are described in the sources (non-recourse project entities, TransAlta OCP LP, TEC Hedland Pty Ltd., Heartland); their individual obligor roles are not documented in this pack (see Gaps).

## Sources

### Issuer sources relied on

| Short name | Exact name | sha256 |
| --- | --- | --- |
| 40-F | 40-F_2025-12-31_tac-20251231_d2.htm.jsonl | b63199bf5537d0e75a2ebecac96b19dc805f7429906c75e8842f8eebec31d328 |
| Q1 release | 6-K-EX-99.1_2026-05-06_q12026newsreleasecombined.htm.jsonl | d77c128beb98e2437eea81e4016d41f6df7e8423fe8e2c62937d63154e11b8b4 |
| Q2 release | 6-K-EX-99.1_2026-07-31_q22026newsreleasecombined.htm.jsonl | 6517eb0175389824e2dbf8ed01f28c9ed380ca26fb5f07df6426985d4637070b |
| Q3 release | 6-K-EX-99.1_2026-11-03_q32026newsreleasecombined.htm.jsonl | 4a5154cd49419e37e9331d492d10dca95a118322f6bfb6d110e3d5c77d11c75e |
| Q1 MD&A | 6-K-EX-99.2_2026-03-31_a20260331tacex992mda.htm.jsonl | 825154ea09ce104089ded78858b6df4a99000ad1f2700c2f48ae4e03f8fb77c2 |
| Q2 MD&A | 6-K-EX-99.2_2026-06-30_a20260630tacex992mda.htm.jsonl | 485b1665b7c8e9772076589eaca23e22bc7e6e99c60259c137d99f66a46a0e8c |
| Q3 MD&A | 6-K-EX-99.2_2026-09-30_a20260930tacex992mda.htm.jsonl | da5d3b9a14d1f4629b51ce9b284f3347ecb5867ab9fb86b1f0ad3a5f6a8c9267 |

The run context file (sha256 178162ae8d9f49e1154d6d4d699e1a01b377d7894f6aad3df2cecb292677e5d8) holds the dated settings of this run; it is not issuer evidence. The pack also holds a retrieval index (_retrieval.json) that CP-OS ignored; it is not a source.

### Supplied handoffs

None. CP-0 is the first module and no upstream handoff exists.

### Document-by-document profile

| Source | Document family and authority | Entity and perimeter | Period and basis | Pages |
| --- | --- | --- | --- | --- |
| 40-F | Annual report cover on Form 40-F, filed with the SEC. Authority is the registrant's own filing, but the text supplied is the cover and wrapper only: it points to Exhibit 99.3 for the audited statements and Exhibit 99.2 for the annual MD&A, and neither exhibit is in the pack. | TransAlta Corporation, registrant; TransAlta Centralia Generation LLC named as US agent for service. | Fiscal year ended Dec. 31, 2025. | 11 pages |
| Q1 release | Exhibit 99.1 to Form 6-K: news release dated May 6, 2026 combined with the MD&A dated May 5, 2026 and the unaudited condensed interim consolidated financial statements with notes. Filed financial statements control over release narrative. | TransAlta Corporation and subsidiaries, consolidated, IFRS. | Three months ended Mar. 31, 2026 with 2025 comparatives; balance sheet at Dec. 31, 2025. | 93 pages |
| Q2 release | Same family: release dated July 31, 2026, MD&A dated July 30, 2026, unaudited interim statements and notes. | Same. | Three and six months ended June 30, 2026 with 2025 comparatives. | 96 pages |
| Q3 release | Same family: release dated November 3, 2026, MD&A dated Nov. 2, 2026, unaudited interim statements and notes, including Note 18 subsequent events. The most current source and the main evidence. | Same. | Three and nine months ended Sept. 30, 2026 with 2025 comparatives; balance sheet at Dec. 31, 2025. | 98 pages |
| Q1 MD&A | Exhibit 99.2 to Form 6-K: the MD&A alone, dated May 5, 2026. Text-contained in the Q1 release (see Version relationships). | Same. | Three months ended Mar. 31, 2026. | 55 pages |
| Q2 MD&A | Exhibit 99.2: the MD&A alone, dated July 30, 2026. Text-contained in the Q2 release. | Same. | Six months ended June 30, 2026. | 62 pages |
| Q3 MD&A | Exhibit 99.2: the MD&A alone, dated Nov. 2, 2026. Text-contained in the Q3 release. | Same. | Nine months ended Sept. 30, 2026. | 60 pages |

### Version relationships and duplicates

Each Exhibit 99.2 MD&A is a separate filed document. The matching release restates that MD&A inside the release, and the MD&A text sits in the release under a different page numbering. A page-by-page text comparison done for this review found, for every MD&A page after the title page, the same opening and closing text inside the matching release (Q3: 59 of 59 pages; Q2: 61 of 61; Q1: 54 of 54). The Exhibit 99.2 documents therefore add no figure that the releases lack; the releases additionally hold the financial statements and notes that the MD&As lack. Hash difference between the files is expected. Retained source for financial statement and note facts: the release of the same quarter. Retained source for an MD&A fact: the Exhibit 99.2 file may be cited, with the release as a containment cross-check. The three quarters are separate periods, not versions of one another; later quarters do not supersede earlier ones for historical facts, and the Q3 release controls where it restates a Dec. 31, 2025 balance.

Exhibit numbers and dates come from the file headers and the quoted text below. No base agreement, amendment, waiver or supplement is in the pack, so no version chain of legal documents exists to resolve.

### Located evidence quoted for this review

| Point | Source and locator | Exact quote |
| --- | --- | --- |
| Audited FY2025 statements are not in the pack | 40-F page:2 | "For consolidated audited annual financial statements for the year ended Dec. 31, 2025, including the report of the independent registered public accounting firm with respect thereto, see Exhibit 99.3 incorporated by reference herein." |
| Annual MD&A is not in the pack | 40-F page:2 | "For management’s discussion and analysis, see Exhibit 99.2 incorporated by reference herein." |
| Q3 interim statements are IFRS, CAD, unaudited | Q3 release page:9 | "All tabular amounts in the following discussion are in millions of Canadian dollars unless otherwise noted" |
| Q3 financial position with Dec. 31, 2025 comparative | Q3 release page:68 | "Condensed Consolidated Statements of Financial Position (in millions of Canadian dollars) (Unaudited)" |
| Debt composition by instrument class | Q3 release page:89 | "11. Credit Facilities, Long-Term Debt and Lease Liabilities A. Amounts Outstanding" |
| Facility-level table (size, letters of credit, drawings, availability, maturity) | Q3 release page:89 | "Syndicated credit facility 1,900 327 — 1,573 Q2 2030" |
| Maturity profile of financial liabilities | Q3 release page:87 | "Long-term debt(1) 52 332 166 245 284 2,277 3,356" |
| Cash interest paid in the cash flow statement | Q3 release page:71 | "Cash interest paid 85 67 200 205" |
| Capital structure and net debt as reported | Q3 release page:38 | "Total Consolidated Net Debt(3)(4)(5) 3,450 60 3,725 67" |
| Management leverage ratio and trailing Adjusted EBITDA | Q3 release page:40 | "Adjusted Net Debt to Adjusted EBITDA (times) 4.1 4.0" |
| Covenants only described generically | Q3 release page:89 | "TransAlta's debt has terms and conditions, including financial covenants, that are considered ordinary and customary." |
| Non-recourse distribution tests | Q3 release page:40 | "These requirements were met in the third quarter of 2026 for all entities, with the exception of Melancthon Wolfe Wind LP." |
| Credit facility extension | Q3 release page:40 | "extend the maturity dates of the syndicated credit facility from June 30, 2029 to June 30, 2030" |
| Ratings (agency actions, no agency report) | Q3 release page:38 | "S&P Global Ratings affirmed the Company’s senior unsecured debt rating and issuer credit rating of BB+ and revised its outlook from stable to negative." |
| Subsequent events up to the MD&A date | Q3 release page:98 | "On Oct. 22, 2026, the Company acquired all issued and outstanding common shares of Mountain Peak Power and Canyon Peak Power (Colorado)" |
| Mothballing notice dated within the cutoff | Q3 release page:5 | "On Nov. 2, 2026, the Company provided notice to the Alberta Electric System Operator (AESO)" |
| Quarterly trend table including Q4 2025 | Q3 release page:45 | "Q4 2025 Q1 2026 Q2 2026 Q3 2026" |
| Outlook table with a "2025 Actual" column for management measures | Q3 release page:23 | "Adjusted EBITDA(1) $759 million $950 million to $1,050 million $1,104 million" |
| Segment and Energy Transition presentation change | Q3 release page:13 | "Following Centralia's cessation of coal-fired operations at the end of 2025 in the normal course, the Energy Transition segment is no longer considered a reportable segment." |
| Required Divestitures excluded from non-IFRS measures only | Q3 release page:14 | "Our non-IFRS measures and operational Key Performance Indicators exclude the results of the Required Divestitures." |
| Acquisition outside internal-control evaluation | Q3 release page:67 | "the scope of the evaluation did not include internal controls over financial reporting of Far North" |
| Exchangeable securities treated as current liabilities | Q3 release page:37 | "The working capital deficit is primarily caused by the classification of exchangeable securities totaling $750 million as current liabilities" |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The pack supports a snapshot of group liquidity, leverage, debt by class and recent events from three quarterly filings with statements. It cannot support instrument-level debt terms, covenant tests or the full prior year. | Medium | No audited FY2025 statements, annual MD&A, indentures or credit agreements are supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The third quarter filing is current, includes unaudited statements and notes, and is dated before the cutoff. | Latest balance sheet, debt and liquidity can be read directly from filed statements. | High |
| The 40-F text is a cover and wrapper; the audited annual statements and annual MD&A are incorporated by reference but not supplied. | Full-year FY2025 income and cash flow cannot be taken from audited statements; only comparatives and management figures are available. | High |
| Debt is shown by class and facility, not by individual note series with coupons, guarantors and security. | Instrument-level capital structure and ranking cannot be mapped from this pack. | High |
| Covenants are described only as ordinary and customary, with compliance stated. | Maintenance test levels and headroom cannot be computed. | High |
| Two restricted-cash figures differ between the narrative and the note. | Cash available to the parent may be misstated if the wrong figure is used. | Medium |

### Readiness view

Readiness view: the effective source set supports the selected modules with limitations. The requested pathway is a credit snapshot built on filed quarterly statements, and the Q3 release carries those statements, the MD&A and the subsequent events note in one document dated before the cutoff, so every selected consumer can proceed. None is conditional or blocked on identity, because the reporting entity is the consolidated group in every source. The limitations are bounded and listed in the tables below: the audited annual statements and annual MD&A for FY2025 are not in the pack, instrument-level debt terms and covenant definitions are not in the pack, and a few narrative figures need reconciling before use. Source readiness here is not a statement that the downstream analysis is complete or that any figure has been normalised.

### Consumer readiness

| Consumer | Status | Evidence demanded and located | Limitations carried forward |
| --- | --- | --- | --- |
| CP-1 (financial and operating data, report strip, chart data) | READY_WITH_LIMITATIONS | Q3 release pages 67 to 71 hold the statements of earnings, financial position and cash flows; pages 12 to 14 hold the highlights table; page 45 holds the eight-quarter table; pages 89 to 91 hold Note 11 on debt. Q1 and Q2 releases supply the earlier quarters of 2026. | No audited FY2025 statements, so FY2025 full-year income statement and cash flow are not supplied; only the Dec. 31, 2025 balance sheet comparatives, the quarterly table and the management-reported figures in the Outlook section are available for the prior period. Segment presentation changed with Energy Transition. 2025 IFRS results include the Required Divestitures while non-IFRS measures exclude them. |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Q3 release pages 12 and 13 describe the business and fleet; pages 5 and 98 describe the Colorado acquisition, the Oklahoma wind sale, the mothballing notices and the Centralia order. | No AIF, no ownership or governance documents beyond the 40-F cover, and no transaction agreements. The Colorado acquisition purchase price allocation is stated as not yet determined. Management language must stay attributed. |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Consumes only upstream registers; their evidence is available as above. | Inherits every limitation of CP-1 and CP-1A, including missing covenant levels and instrument terms. |
| CP-5 (evidence trace review) | READY_WITH_LIMITATIONS | Reviews the other modules against this pack; the pack has located quotes at page level for every filed fact. | Cannot verify any fact whose source is an unsupplied exhibit. Duplicate content between each release and its MD&A means a quote must name the retained source. |

### Source-quality and conflict log

| Item | Locators | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| Restricted cash: the MD&A narrative says "$100 million (Dec. 31, 2025 – $101 million) of cash was subject to such restrictions" while Note 11 says "$84 million (Dec. 31, 2025 – $101 million) of cash was subject to these financial restrictions". The two sentences may use different scopes; the pack does not reconcile them. | Q3 release page:40 and page:90 | Medium | CP-1, CP-2, CP-5 | Carry both, label scope, and do not use either as the only measure of cash trapped in subsidiaries; read Note 11 sub-items on page:91 (OCP, Hedland, holdbacks) alongside. |
| Audited FY2025 statements and annual MD&A are referenced, not supplied. | 40-F page:2 | High for any full-year FY2025 figure | CP-1, CP-2, CP-5 | Add Exhibit 99.3 and Exhibit 99.2 of the 40-F, or the Annual Report, if full-year FY2025 statements are required. |
| Instrument-level debt terms (series, coupon, maturity, issuer, guarantors, security) not supplied; only class totals, a maturity profile and a facility table appear. | Q3 release page:89 and page:87 | High for debt-structure and recovery questions | CP-1, CP-2 | Add the Note on credit facilities and long-term debt in the audited statements, or indentures and credit agreements. |
| Financial covenant levels, definitions and reported ratios not supplied. | Q3 release page:89 | High for covenant headroom | CP-1, CP-2 | Add the credit agreement and note covenants; until then covenant headroom is Not calculable. |
| Credit ratings appear only as agency actions in the MD&A; no agency report. | Q3 release page:38 | Low | CP-2 | Optional: add agency reports. |
| The three Exhibit 99.2 files duplicate MD&A text found in the releases. | See version relationships | Low | CP-5 | Cite the release for statement and note facts. |
| Q3 filing says the Colorado acquisition fair values and purchase price allocation are not yet determined, so post-closing balances cannot be taken from the statements. | Q3 release page:98 | Medium | CP-1, CP-2 | Treat pro forma debt and capital structure as outside this pack; flag the US$750 million project debt as a subsequent event. |
| Management-defined measures (Adjusted EBITDA, Adjusted Net Debt, Available liquidity, FCF) are not IFRS and are defined by the issuer. | Q3 release page:14, page:15, page:40 | Medium | CP-1, CP-2 | Label each as management-defined and reconcile where the filing provides a reconciliation. |

### Coverage statement

All seven sources are text extractions of filed HTML documents, so there are no scans, images, charts or workbook content in this pack, and no presentation slides are supplied. The extraction is complete at page level in the sense that each file carries its stated page count (11, 93, 96, 98, 55, 62 and 60 pages), but extraction success is not a fidelity review. Tables in the extraction lose some column alignment (for example the segment tables on pages 55 to 58 of the Q3 release lose their column headers), so a figure read from such a table must be checked against the narrative before it is relied on. Nothing in the pack is dated after the cutoff; the latest event is a notice dated Nov. 2, 2026 and the latest source is the release dated Nov. 3, 2026. The quarterly releases are not audited; the 40-F cover states that audited statements exist but does not contain them. For an HTML model objective the pack holds discrete quarters for 2025 and 2026 in the eight-quarter table, quarter and year-to-date figures in the highlights, segment Adjusted EBITDA, debt carrying values by class, cash interest paid and cash taxes paid; facility-level carrying values by individual note and fiscal-year statements are absent. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

## Calculations

None. CP-0 does not normalise, reconcile or calculate figures. Every number above is a located quotation. Where two quoted figures conflict (restricted cash), no reconciliation is attempted here.

## Gaps

- Audited FY2025 consolidated statements and report of the auditor (Exhibit 99.3 of the 40-F) and the 2025 annual MD&A (Exhibit 99.2): Not supplied. FY2025 full-year income statement, cash flow statement and notes are therefore Not calculable from audited statements.
- Annual Information Form and 2025 Annual Report sections cited by the MD&A for credit ratings, glossary and risk management: Not supplied.
- Indentures, note purchase terms, credit agreements, intercreditor terms and guarantee structure: Not supplied (the context states legal documents: none). Obligor, guarantor and security roles by instrument are Not supplied.
- Financial covenant levels and compliance ratios: Not supplied; only a statement of compliance is made.
- Rating agency reports: Not supplied.
- Presentations and investor decks: Not supplied; there is no slide coverage to account for.
- Pro forma capital structure after the Oct. 22, 2026 Colorado acquisition and Oklahoma wind sale: Not supplied; the Q3 statements are as at Sept. 30, 2026.
- Currency: reporting currency is CAD as the context states. Part of the debt and some transaction amounts are stated in US dollars (US$) or Australian dollars; those amounts must be kept in their stated currency.

## Next module

Proceed to CP-1 on the Q3 release as the primary source, using Q1 and Q2 releases for the earlier 2026 quarters, and carry the limitations above: no audited FY2025 statements, no instrument-level debt terms, no covenant levels, and the restricted cash discrepancy. Then CP-1A, CP-2 and CP-5 in the order CP-OS sets. No consumer is marked DO NOT RUN.
