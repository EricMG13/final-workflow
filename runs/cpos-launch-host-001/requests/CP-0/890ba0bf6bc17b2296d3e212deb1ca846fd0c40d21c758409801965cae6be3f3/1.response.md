# CP-0 — Source readiness: TransDigm Group Incorporated (tdg)

## Request

- Issuer: TransDigm Group Incorporated (issuer id `tdg`), as of 2024-09-30.
- Run: `tdg-2024-09-30-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1 and CP-1A. CP-0 runs first as their dependency.
- Execution: host session. This answer was written by the host from the pinned files below. No provider was called.
- Question: can the effective source set support CP-1 and CP-1A for the fiscal year ended 2024-09-30, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. CP-0 gives no credit conclusion, legal interpretation or investment opinion, and does not normalize, reconcile or calculate figures.

## Sources

| Source | sha256 | Role in this review |
| --- | --- | --- |
| TDG_2024-09-30_10-K_0001260221-24-000083_tdg-20240930.htm.jsonl | d75c469fdb1966dd895c0f6faa6d5179b380d3ed95aa00aca99aa258059edab6 | Primary: filed annual report for FY2024 (visible text, 181 pages of extracted text) |
| TDG_FY2024_annual-report_SEC-PDF_0001260221-25-000008_a841225transdigmgroupbookm.pdf | dc6a8ea6249e4e919d190a4bbb459d9bf4eded005b7d5680ae911b32d44d44af | Secondary: printed annual-report book that reproduces the FY2024 Form 10-K, plus a long-run non-GAAP history page (160 PDF pages) |
| TDG_2024-03-30_10-Q_0001260221-24-000046_tdg-20240330.htm.jsonl | fcec3566cfda08c82a8aaed7289c6440cc05d12976f237cd72a32cf9fbfb2ed6 | Interim: second fiscal quarter of FY2024 (72 pages of extracted text) |
| TDG_2024-06-29_10-Q_0001260221-24-000069_tdg-20240629.htm.jsonl | ce1b0541d5e8222dc536d748942a3cb51236d7ff62d8613b002460bd8b41dcf2 | Interim: third fiscal quarter of FY2024 (77 pages of extracted text) |
| TDG_2024-12-28_10-Q_0001260221-25-000014_tdg-20241228.htm.jsonl | ec98b47e6ebad9663286dc04b35dade04d11e7d12c3642ddaa6ef549a33d671f | Subsequent: first fiscal quarter of FY2025, after the as-of date (58 pages of extracted text) |
| context | f7b95e1ff471b47547a3ac86cb68e7e7144a06231f6e94de0eee48e0c6828449 | User run settings; not issuer evidence |

Supplied handoffs: none (CP-0 is the first module).

Locators below use `page N` for the extracted-text page of a `.jsonl` source and `PDF page N` for the physical page of the PDF.

## Findings

### Readiness verdict

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 (financial statements and credit metrics) | READY_WITH_LIMITATIONS | Audited FY2024 statements with FY2023 and FY2022 comparatives are located in the 10-K. The first fiscal quarter of FY2024 has no supplied 10-Q, and no executed debt documents are supplied. |
| CP-1A (business, governance, transaction summary) | READY_WITH_LIMITATIONS | Business, segment, ownership-perimeter, debt-description and subsequent-event text is located in the 10-K and interim filings. Governing debt terms are only described, not supplied as executed documents. |

Command sheet: CP-1 RUN; CP-1A RUN. Pathway modules not selected for this run (CP-2, CP-3, CP-4, CP-5, CP-6) are not assessed here.

### Source register

#### 10-K for FY2024 (`TDG_2024-09-30_10-K_...jsonl`)

- Family and authority: filed annual report on Form 10-K; original authority for the audited consolidated statements. Cover, page 1: "FORM 10-K", "For the fiscal year ended September 30, 2024", "Commission File Number 001-32833 TransDigm Group Incorporated".
- Audit and signature: page 120: "/s/ Ernst & Young LLP We have served as the Company’s auditor since 2004. | Cleveland, Ohio November 7, 2024". Page 116: "duly authorized on November 7, 2024".
- Statements located: balance sheet page 120 ("Total stockholders’ deficit (6,283) (1,978)"), income statement page 121 ("NET SALES $ 7,940 $ 6,585 $ 5,429"), cash flows from page 122. MD&A balance-sheet data page 52 ("Cash and cash equivalents $ 6,261 $ 3,472").
- Units: page 44: "(amounts in millions, except per share data)". USD is the reporting currency; per-share figures are a separate unit.
- Non-GAAP: page 71 holds "a reconciliation of net cash provided by operating activities to EBITDA and EBITDA As Defined (in millions)", with the net-income reconciliation introduced on page 70. These are issuer-defined measures, not audited statement lines.
- Segments: page 5: "three reporting segments: Power & Control, Airframe and Non-aviation"; segment note from page 162.
- Perimeter: page 4: "TD Group, through its wholly-owned subsidiary, TransDigm Inc.". Page 57: the Subordinated Notes "are fully and unconditionally guaranteed on a senior subordinated unsecured basis by TD Group, TransDigm UK and TransDigm Inc.’s Domestic Restricted Subsidiaries". Page 58: "Separate financial statements of TransDigm Inc. are not presented". A summarized obligor-group table starts on page 59 ("Net sales $ 6,294" for the issuer and guarantors).
- Subsequent events inside the filing: page 152: "Subsequent Event – Trade Receivable Securitization Facility – The Company drew the remaining $162.5 million available under the Securitization Facility in October 2024." Page 170: "Subsequent Event – $75.00 Special Dividend Payment – The Company paid $4,216 million and $132 million in special dividend and dividend equivalents, respectively, in October 2024."
- Legal documents: the exhibit index lists governing documents by reference only, for example page 103: "4.2 Indenture, dated as of November 13, 2019, among TransDigm Inc., as issuer" and page 40: "the Second Amended and Restated Credit Agreement dated as of June 4, 2014 (the “Credit Agreement”)". The exhibits themselves are not in the source set.

#### Annual-report book PDF (`TDG_FY2024_annual-report_SEC-PDF_...pdf`)

- Family: printed annual report to shareholders. Its content identifies itself by text, not by filename: PDF page 1: "FORM 10-K" and "For the fiscal year ended September 30, 2024".
- Version relationship: it reproduces the same Form 10-K. PDF page 104 repeats the audit opinion dated "November 7, 2024"; PDF page 105 is the balance sheet and PDF page 106 the income statement, with the same "7,940", "6,261", "25,586" and "(6,283)" values as the HTML 10-K. Treat the HTML 10-K as the controlling copy for statement facts. The PDF is a duplicate presentation, not an independent corroboration.
- Additional content: PDF page 156: "Reconciliations of Non-GAAP Measures to Most Directly Comparable U.S. GAAP Measures", a long-run EBITDA history table by fiscal year from FY1994 to FY2024. This page is not in the HTML 10-K. It is issuer-prepared, unaudited and attributable to management.
- Coverage: 160 PDF pages. PDF pages 102, 157 and 158 are explicit "[THIS PAGE INTENTIONALLY LEFT BLANK]" pages. PDF pages 159 and 160 have no extractable text and no raster images, so any cover artwork or text on them is not inspected. No shareholder letter text was located.
- Extraction: text layer extracted with layout preserved. Tables are readable as text but column alignment is by spacing, so a downstream module that reads a table from this PDF must check column assignment against the HTML 10-K.

#### Interim 10-Qs within FY2024

- `TDG_2024-03-30_10-Q_...jsonl`: page 1: "For the quarterly period ended March 30, 2024". Page 2 lists "Thirteen and Twenty-Six Week Periods Ended March 30, 2024 and April 1, 2023". Unaudited condensed statements.
- `TDG_2024-06-29_10-Q_...jsonl`: page 1: "For the quarterly period ended June 29, 2024". Page 2 lists "Thirteen and Thirty-Nine Week Periods Ended June 29, 2024 and July 1, 2023". Unaudited condensed statements.
- Fiscal calendar: quarters end on a Saturday near the calendar quarter end, and the fiscal year ends on September 30. Quarter and year-to-date columns are distinct and must not be mixed.

#### Subsequent interim 10-Q (`TDG_2024-12-28_10-Q_...jsonl`)

- Page 1: "For the quarterly period ended December 28, 2024". Page 2: "Thirteen Week Periods Ended December 28, 2024 and December 30, 2023".
- This period ends after the as-of date. Use it only as a dated subsequent event or as the source of the comparative quarter ended December 30, 2023, always labelled as such. It is not FY2024 evidence for the annual balance sheet or income statement.

### Identity and perimeter

- Reporting entity: TransDigm Group Incorporated ("TD Group"), Delaware, Commission File Number 001-32833, common stock listed as TDG on the New York Stock Exchange (10-K page 1).
- Borrower and note issuer: TransDigm Inc., a wholly-owned subsidiary (10-K page 4; exhibit index page 103 names TransDigm Inc. "as issuer").
- Guarantors: TD Group, TransDigm UK and TransDigm Inc.'s Domestic Restricted Subsidiaries, as defined in the indentures (10-K page 57). The context file leaves borrower, parent and guarantor fields blank; that is not evidence of their absence.
- Unresolved distinction: the consolidated statements are for TD Group. Obligor-group figures exist only as the summarized table from page 59. Restricted and unrestricted subsidiary designations are defined in documents that are not supplied.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Audited FY2024 and FY2023 statements, notes, units, period labels | 10-K pages 120 to 123 and notes; units page 44 | Consolidated TD Group basis only |
| CP-1 | Debt, maturities, liquidity, cash flow | 10-K debt note and contractual obligations table (page 64); cash flows from page 122 | Governing debt terms not supplied |
| CP-1 | Issuer non-GAAP EBITDA measures | 10-K pages 70 to 71; PDF page 156 history | Issuer-defined and unaudited; As Defined is a covenant-style measure described by the issuer, not by the executed agreement |
| CP-1 | Discrete quarters for FY2024 | Second and third quarter 10-Qs; fourth quarter only by subtraction | No first-quarter FY2024 10-Q; any derived quarter is a calculation for CP-1, not a reported figure |
| CP-1A | Business model, segments, products, customers | 10-K Item 1 from page 4; segment note from page 162 | Management description, not independently verified |
| CP-1A | Ownership, governance, capital allocation | 10-K cover and Item 5; special dividend notes (page 170). Page 2: "Certain sections of the registrant’s definitive Proxy Statement to be filed in connection with its 2025 Annual Meeting" are incorporated by reference | Proxy statement not supplied; governance detail incorporated by reference is missing |
| CP-1A | Transaction summary and new debt issues | 10-K debt and liquidity discussion (page 48 lists notes issued at par); subsequent events (pages 152 and 170); first fiscal quarter FY2025 10-Q for later events | Executed indentures and credit agreement amendments not supplied |

### Analytical read-through

- Usable coverage: the FY2024 10-K is complete and audited, signed on November 7, 2024, and carries three fiscal years of income and cash-flow statements and two balance sheets. It supports CP-1's annual statements and CP-1A's business and capital-structure description. The two FY2024 10-Qs support interim and year-to-date views.
- Strongest contrary evidence: the stockholders' deficit and the October 2024 special dividend payment ("The Company paid $4,216 million", page 170) show that the balance sheet at the as-of date is followed within weeks by a large cash outflow. A consumer that reads cash at September 30, 2024 must carry this subsequent event. The issuer's EBITDA As Defined is a management measure; without the credit agreement, its alignment with covenant definitions cannot be checked.
- Source risk mechanism: the PDF duplicates the 10-K. Counting the two as independent sources would overstate corroboration. The PDF's long-run EBITDA history is management-prepared and is not covered by the audit opinion.
- What cannot proceed from this set: covenant interpretation, guarantor-level legal analysis and any test that needs the executed credit agreement or indentures. These belong to CP-4, which is not selected. Discrete reported figures for the first fiscal quarter of FY2024 cannot be read directly.
- Next evidence action: supply the executed Credit Agreement with amendments and the indentures if a legal or covenant module is added, and the 10-Q for the quarter ended December 30, 2023 if discrete FY2024 quarters are required.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Page counts are coverage counts from the extracted text: 181, 72, 77 and 58 extracted-text pages for the four HTML filings, and 160 PDF pages, of which 5 have no analytical text.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed Credit Agreement, amendments and indentures not supplied; only the exhibit index references them | High for legal work; Medium for CP-1A transaction summary | CP-1A; CP-4 if added later | Supply executed documents. The context declares executed legal documents, but none are in the source set. |
| No 10-Q for the first fiscal quarter of FY2024 (quarter ended December 30, 2023) | Medium | CP-1 quarterly view | Supply the filing. Its comparative column in the FY2025 first-quarter 10-Q is the only located substitute and must be labelled as a comparative. |
| Proxy statement not supplied; Part III governance items are incorporated by reference | Medium | CP-1A governance | Supply the 2025 proxy statement. |
| PDF pages 159 and 160 have no extractable text | Low | CP-1A | Visual inspection is required to claim coverage of these pages. |
| Obligor-group figures are summarized only | Medium | CP-1 credit metrics at issuer level | Use the summarized table and label it; no separate TransDigm Inc. statements exist in the set. |
| No earnings release, rating report or market data | Low for the selected modules | CP-1, CP-1A | Not required for the selected scope. Ratings, prices and peers stay Not supplied. |
| Context fields for borrower, parent, guarantors and sponsor are blank | Low | CP-1A | Treat as Not supplied, never as none. |

## Next module

- CP-1: use the HTML 10-K as the controlling annual source, with units "in millions" and per-share figures kept separate. Keep TD Group consolidated and obligor-group figures distinct. Keep FY2024 quarters, year-to-date columns and the subsequent FY2025 quarter separate. Carry the October 2024 special dividend payment and securitization draw as subsequent events.
- CP-1A: use 10-K Item 1, the segment note, the debt discussion and the subsequent events. State that governing debt terms are described from the 10-K, not read from executed documents.
