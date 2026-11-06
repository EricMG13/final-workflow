## Request

Module CP-0 (source readiness) for GFL Environmental Inc. (ticker GFL; Ontario, Canada; foreign private issuer filing Form 40-F and furnishing interim reports and earnings releases on Form 6-K; reporting currency CAD, "$" in the 6-K documents means Canadian dollars unless noted). As-of date: 2026-11-05 (cutoff 2026-11-05). Pathway: credit_snapshot. Current period q3-2026 (three and nine months ended September 30, 2026); prior period fy-2025. Requested downstream modules: CP-1, CP-1A, CP-2, CP-5 (the "minimum" set).

Question answered: can the supplied source set support those modules, and what remains blocked. This module gives no credit conclusion, no legal interpretation and no investment opinion, and it does not normalize, reconcile or calculate figures. Assertion: SOURCE_SUFFICIENCY_ONLY.

## Sources

### Issuer sources relied on (name, sha256 as pinned by CP-OS)

| Source name | sha256 |
|---|---|
| 40-F_2025-12-31_gfl-20251231x40f.htm.jsonl | b934765df3e7c34910af8387591b8fa09e1dab95cdcc8ca06bb6c968dd003ae6 |
| 6-K-EX-99.1_2026-03-31_tm2612685d3_ex99-1.htm.jsonl | cb537fb74c382c1d0201e410842d4660c8613b15a362445d11ff422e5b399f25 |
| 6-K-EX-99.1_2026-04-29_tm2612685d2_ex99-1.htm.jsonl | 3df073d71665ee940b9aad03ce71f25168457a8b67f443c14d9006bb7687f437 |
| 6-K-EX-99.1_2026-06-30_tm2619744d3_ex99-1.htm.jsonl | f263228fdadc42723c2dcd6496cb1b52232f1a5fd2b7778ad4e13cf2111721c2 |
| 6-K-EX-99.1_2026-07-29_tm2619744d2_ex99-1.htm.jsonl | 5fa07feeac05724810518cb847015c4db9d05aa3ab7046fa5917870573c8a1c3 |
| 6-K-EX-99.1_2026-10-28_tm2626649d2_ex99-1.htm.jsonl | ee28f5cf135f3ebbb50b3dfc34b1ac6447600e4aae341e5faea9d8d69de358cb |
| 6-K-EX-99.1_2026-10-30_tm2626649d1_ex99-1.htm.jsonl | 21de76c788e5b3fc408d84e05a80d6dd1586537f33922ada67131193bae391d4 |

### Run context (not issuer evidence)

| Source name | sha256 |
|---|---|
| context | 3b2c2e634d2c0d1d787b2efc6bec59a8cda3a4f73d98ab4b38ff36c15a35719c |

### Supplied handoffs

No upstream handoff is supplied for CP-0. CP-0 is the first module in the run and the handoff set is empty.

### Document identification from located content (not from filenames)

| Source | Document family and original authority | Entity and perimeter | Period and basis | Pages |
|---|---|---|---|---|
| 40-F file | Annual report cover document, Form 40-F, signed "February 18, 2026" by Patrick Dovigi. Filed regulatory wrapper only. | Registrant GFL Environmental Inc., consolidated | "For the fiscal year ended December 31, 2025", Commission File Number 001-39240 | 5 |
| 6-K file dated 2026-03-31 | Exhibit 99.1: unaudited interim condensed consolidated financial statements (IFRS, IAS 34). Filed financial report, controlling for reported figures. | GFL and subsidiaries | "For the three months ended March 31, 2026"; Board approval "April 29, 2026" | 15 |
| 6-K file dated 2026-04-29 | Exhibit 99.1: first quarter 2026 earnings release. Management document with non-IFRS measures and guidance. | GFL | Q1 2026 (three months ended March 31, 2026) | 16 |
| 6-K file dated 2026-06-30 | Exhibit 99.1: unaudited interim condensed consolidated financial statements. | GFL and subsidiaries | "For the three and six months ended June 30, 2026"; Board approval "July 29, 2026" | 18 |
| 6-K file dated 2026-07-29 | Exhibit 99.1: second quarter 2026 earnings release. | GFL | Q2 2026 | 18 |
| 6-K file dated 2026-10-28 | Exhibit 99.1: third quarter 2026 earnings release and updated guidance. | GFL | Q3 2026 and nine months ended September 30, 2026 | 18 |
| 6-K file dated 2026-10-30 | Exhibit 99.1: unaudited interim condensed consolidated financial statements. | GFL and subsidiaries | "For the three and nine months ended September 30, 2026"; Board approval "October 28, 2026" | 20 |

## Findings

### Readiness verdict by consumer

| Consumer | Status | Basis |
|---|---|---|
| CP-1 | READY_WITH_LIMITATIONS | Q3 2026 interim financial statements and release give statements of operations, financial position, cash flows, segments, debt and covenant text for the current period. FY2025 audited annual statements and MD&A are not in the pack (see Gaps G1 and G2). |
| CP-1A | READY_WITH_LIMITATIONS | Same evidence; facility-level debt, interest and cash interest for the latest quarter are located. Maturity ladder, revolver availability and covenant ratio values are not supplied (G3, G4, G5). |
| CP-2 | READY_WITH_LIMITATIONS | Discrete Q1, Q2, Q3 and nine-month figures, Adjusted EBITDA reconciliations and segment tables are located. Fiscal year 2025 figures are available only as comparatives or "December 31, 2025" columns inside 2026 interim documents (G1). |
| CP-5 | READY_WITH_LIMITATIONS | Latest-quarter movements, guidance and subsequent-period events are located in the Q3 release; the pending take-private review and the SECURE acquisition are narrated only by management. |

No consumer is CONDITIONAL or BLOCKED. No missing downstream analytical handoff is treated as a source condition.

### Usable coverage

- The 40-F is a cover and incorporation-by-reference document. Its text states the annual information form is "filed as Exhibit 99.1", the MD&A as "Exhibit 99.2" and the audited statements as "Exhibit 99.3". None of those exhibits is in the supplied text, so the 40-F supports identity, listing, share counts and filing status only: "At December 31, 2025, 346,110,312 subordinate voting shares, 11,812,964 multiple voting shares, 4,867,006 Series A perpetual convertible preferred shares and 8,196,721 Series B perpetual convertible preferred shares were issued and outstanding."
- The three interim financial statement exhibits (Q1, Q2, Q3 2026) are filed financial reports and control reported figures. The three earnings releases are management documents; their IFRS tables repeat the statements and their non-IFRS tables (Adjusted EBITDA, Adjusted Free Cash Flow, Net Leverage, Run-Rate EBITDA) are attributed management measures.
- Q3 statements (source 21de76c7...): statement of operations (page 1), financial position (page 2), cash flows (pages 3 and 4), note 7 long-term debt (pages 11 to 13), note 8 interest (pages 13 and 14), note 11 operating segments with Adjusted EBITDA reconciliation (pages 14 to 16), note 15 commitments including letters of credit and performance bonds (page 18 and 19). Quote located: "The Total Net Funded Debt to Adjusted EBITDA ratio to be maintained is equal to or less than 5.00 to 1.00 for a period of four complete fiscal quarters following completion of a Material Acquisition and at all other times, equal to or less than 4.50 to 1.00."
- Q3 release (source ee28f5cf...): guidance, Net Leverage table and non-IFRS reconciliations (pages 2, 3, 10 to 18). Quote located: "Net Leverage2 is estimated to be in the mid 3s by the end of 2026."

### Strongest contrary evidence and limitations

- Perimeter change: the SECURE Waste Infrastructure Corp. acquisition closed "On September 1, 2026" and its purchase price allocation is described as "provisional and subject to adjustment during the measurement period" (Q3 statements, note 3, page 7). Evidence to mechanism to consequence: only one month of SECURE is in the Q3 statements, so quarterly and nine-month totals mix pre- and post-acquisition perimeters, and downstream trend or pro forma work needs the separately stated pro forma disclosure ("unaudited consolidated pro forma revenue and loss before income taxes for the nine months ended September 30, 2026") rather than reported totals alone.
- Comparative revision: the Q3 statements state "comparative amounts have been revised for the three and nine months ended September 30, 2025" and for December 31, 2025 balances (note 3, pages 8 and 9). Evidence to mechanism to consequence: the December 31, 2025 column in 2026 documents differs from the as-originally-reported FY2025 annual statements, which are not supplied, so the original-versus-revised bridge for FY2025 cannot be checked from this pack.
- Period conventions of the 2026 filings: the file labels do not equal period or filing date (for example the statements for the three months ended March 31, 2026 carry a file label dated 2026-03-31 but state Board approval on April 29, 2026). Period and basis here come from located content only.
- Management measures versus filed statements: Net Leverage uses "Run-Rate EBITDA" that adds management-estimated "Run-Rate EBITDA Adjustments"; it is an attributed management claim and does not override filed statement figures.
- Source quality versus extraction: all sources are text extractions of HTML. Text extraction is not a fidelity review; tables were read as extracted and no image, chart or footnote-marker rendering was inspected.

### Entity and instrument roles located

- Registrant, issuer of the reporting group and parent: GFL Environmental Inc.; subsidiaries consolidated. Borrower and guarantor identities for each debt instrument are not stated in the supplied text, except the tax-exempt bonds: "guaranteed jointly and severally, fully and unconditionally by GFL and certain of its subsidiaries" (note 7). Restricted versus unrestricted subsidiary definitions are not supplied.
- Revolving Credit Agreement "dated as of September 27, 2021 and as amended and restated through September 1, 2026"; Term Loan B Facility entered "On August 28, 2026", maturing "August 28, 2033"; both described as secured by mortgages, a general security agreement and share pledges. The 6.750% 2031 notes: "Collateral securing the 6.750% 2031 Secured Notes has been released ... the notes are no longer secured."
- Non-wholly owned subsidiary stand-alone facilities are included in "Other" debt (note 7).
- Equity-method associate GFL Environmental Services (divested March 1, 2025) with a Call Option carried at fair value; related party transactions in note 16.

### Version relationships

- The Q1, Q2 and Q3 statements and releases are separate periodic documents; none supersedes another. Each release pairs with the same-period statements. No duplicates are present; no hash-identical sources are in the set.
- The Revolving Credit Agreement text moved from "amended and restated through April 29, 2025" (Q1, Q2 statements) to "amended and restated through September 1, 2026" (Q3 statements); the agreement itself and its amendments are not supplied, so these descriptions are the only evidence.

### Source profile coverage notes

- Earnings releases: reported and adjusted figures, reconciliations, quarter and year-to-date columns and guidance are present in each release. Q1 release guidance is dated with the original guidance of February 11, 2026 referenced but not supplied.
- Decks and workbooks: none supplied. No slide, speaker note, chart or workbook coverage is claimed.
- Legal and financing documents: none supplied (context states legal_documents "none"). Indentures, credit agreement and Term Loan B credit agreement are absent.

## Calculations

None. CP-0 does not normalize, reconcile or calculate. Counts only: 7 issuer sources; pages as stated in the table in Sources (5, 15, 16, 18, 18, 18, 20; 110 pages in total); 0 handoffs.

## Gaps

| ID | Gap | Severity | Affected consumers | Remediation |
|---|---|---|---|---|
| G1 | Fiscal year 2025 audited consolidated financial statements, MD&A and annual information form (Exhibits 99.1 to 99.3 of the 40-F) are not in the pack; only the 40-F cover is supplied. FY2025 figures exist only as comparative columns in 2026 documents and are partly revised. Not supplied. | High | CP-1, CP-2 | Supply the 40-F exhibits or the FY2025 earnings release. |
| G2 | No Q4 2025 or full-year 2025 earnings release. The fourth quarter of 2025 discrete figures are Not calculable from supplied text without arithmetic outside CP-0. Trailing twelve months Adjusted EBITDA at December 31, 2025 appears only as a management figure in 2026 releases. | Medium | CP-2, CP-5 | Supply the Q4 2025 release. |
| G3 | Debt maturity schedule by year, including a contractual cash flow table, is not in the interim statements; maturities are available only per instrument in note 7 footnotes. The annual MD&A "Contractual Obligations" section is incorporated by reference in the 40-F but not supplied. Not supplied. | Medium | CP-1A | Supply the FY2025 MD&A or an obligations table. |
| G4 | Revolving credit facility undrawn availability and total liquidity are not stated. Drawn amounts, facility size and letters of credit are stated separately; the split of letters of credit between facilities is partial ("inclusive of letters of credit under both the Revolving Credit Facility and EDC Guaranteed LC Facility"). Not supplied. | Medium | CP-1A, CP-5 | Supply an MD&A liquidity section or lender disclosure. |
| G5 | Actual covenant ratio values are not disclosed; only compliance statements and thresholds are given ("GFL was in compliance with these covenants"). Definitions of "Total Net Funded Debt", "Adjusted EBITDA" for covenant purposes and "Material Acquisition" are in the credit agreement, which is not supplied. Whether the SECURE acquisition triggered the 5.00 to 1.00 step-up is not stated in the supplied text. | High | CP-1A, CP-5 | Supply the Revolving Credit Agreement and compliance certificate data. |
| G6 | Indentures, guarantor structure, ranking, redemption terms, change-of-control provisions and the Term Loan B credit agreement are not supplied; these matter for the pending take-private review. | High | CP-1A, CP-5 | Supply indentures and the credit agreements. |
| G7 | SECURE purchase price allocation is provisional; SECURE standalone financials, financing sources detail and any post-September 30, 2026 acquisition or financing events are not covered by a subsequent-events note in the Q3 statements (no such note appears in the extracted text). Subsequent events are visible only in the Q1 statements (note 18) and in management narrative. | Medium | CP-1, CP-5 | Check for a subsequent-events note or later 6-K. |
| G8 | Pending take-private review: the Q3 release states a Special Committee "provided interested parties with a final deadline of November 9, 2026". That date is after the cutoff 2026-11-05; outcome is unknown and must not be assumed. | Medium | CP-5 | Treat as an open subsequent event; no evidence after the cutoff may be used. |
| G9 | No credit ratings, quotes, market data or peer data are supplied (context ratings, quotes and valuation inputs are blank; blank is not zero). | Low for the minimum set | CP-5 | Supply if required. |
| G10 | Extraction fidelity not reviewed: sources are text extractions; no table-image or footnote-marker verification was done. The text inside each extracted file quotes a different sha256 for the underlying HTML than the pinned sha256 of the extracted file; the pinned values are used here and the difference is a transport artefact, not a content conflict. | Low | All | Spot-check key tables against filings downstream. |
| G11 | Inconsistent file date labels (period end for the statements, filing date for the releases) leave exact 6-K filing dates unsupplied for the statements. | Low | CP-5 | Confirm filing dates from EDGAR index if timing matters. |

### Conflicts

No conflict between a filed statement and a management document was found in the located core figures. Examples checked for agreement between release and statements: revenue "$2,155.3" and Adjusted EBITDA "$678.7" appear in both for Q3 2026. Net Leverage definitions differ from covenant definitions, which is a definitional difference to carry downstream, not a numeric conflict.

## Next module

CP-1 may proceed on the sources listed, with the limitations G1 to G11 carried forward, then CP-1A, CP-2 and CP-5 in the order the dependency planner sets. Next evidence action: obtain the FY2025 Form 40-F Exhibits 99.1 to 99.3, the credit agreements and indentures, and a post-November 5, 2026 check is not permitted for this run. DO NOT RUN is not recommended for any consumer.
