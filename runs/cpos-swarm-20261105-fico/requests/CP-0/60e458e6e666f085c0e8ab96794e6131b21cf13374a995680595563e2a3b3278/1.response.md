# CP-0 - Source readiness: FAIR ISAAC CORP (fico)

## Request

- Issuer: FAIR ISAAC CORP (Fair Isaac Corporation, NYSE "FICO", issuer id `fico`), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run: `fico-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned files and wrote this answer. No provider was called.
- Question: can the supplied public filings and earnings releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion is given; no figure is normalized, reconciled or calculated here.
- Periods and currency: the context names USD, current period q3-2026 and prior period fy-2025. FICO's fiscal year ends September 30, so fiscal Q3 2026 is the quarter ended June 30, 2026 and fiscal 2025 is the year ended September 30, 2025. These are the sources' own periods; no other currency or period is reported.

## Sources

| Source (exact name) | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-09-30_fico-20250930.htm.jsonl | 2cd0fc2b16386652e87f31c986fda43ca1da2a923ef1840b57f765a69322682e | Form 10-K, fiscal year ended September 30, 2025 (137 pages) |
| 10-Q_2025-12-31_fico-20251231.htm.jsonl | 905bfc6e05d39d56e0eed3225e1079b7eb97528806ef0d9d2d8efa0e76893510 | Form 10-Q, quarter ended December 31, 2025 (37 pages) |
| 10-Q_2026-03-31_fico-20260331.htm.jsonl | 1d56011f469dd7f9f01c0afabb2cc5e52bf600c9b61e1e02a22c20a1382a76cb | Form 10-Q, quarter ended March 31, 2026 (43 pages) |
| 10-Q_2026-06-30_fico-20260630.htm.jsonl | 9928c89c8cd74e2a4ae5180bf504e58edee7d7a0cfbf531e71dc30f830e9f9a7 | Form 10-Q, quarter ended June 30, 2026 (46 pages) |
| EX-99.1_2026-01-28_exhibit991erq12026.htm.jsonl | 7ff326f8e766ed76e0e346c09be22d1a6689de853a63261725535c212fd1ea11 | Earnings release for fiscal Q1 2026 (6 pages) |
| EX-99.1_2026-04-28_exhibit991erq22026.htm.jsonl | 98fcf8141dae7e420bccc2579f8ef67af179818384ed4fb3d51d12d1c6831d98 | Earnings release for fiscal Q2 2026 (6 pages) |
| EX-99.1_2026-07-29_exhibit991erq32026.htm.jsonl | 4bcf15097cd5d352a02b7a02cc65369e0e3cdadccda74b9b84b0c06bd098be52 | Earnings release for fiscal Q3 2026 (6 pages) |
| context | 67fd10ada0c60e1a58280c6938025b16a97aebcc1d2e25ac2914a3e17b05c7a0 | User run settings; not issuer evidence |

Supplied handoffs: none (CP-0 is the first module). Ignored by the launcher: `_retrieval.json` (fetch log, not issuer evidence). Locators are `page:N` chunks of the named jsonl file, not printed pages.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filed annual report, three quarterly reports and three earnings releases are enough for every requested module to run, each with stated limitations. Nothing blocks the work. | Medium | Credit agreement, indentures and any covenant calculation are not supplied, and nothing after the latest quarterly filing is supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited annual statements and unaudited interim statements with comparatives are located, with a debt note that lists every instrument. | Debt, liquidity and cash flow can be traced to filed statements. | High |
| The credit agreement, its amendment and the note indentures are only listed as exhibits, not supplied. | Covenant definitions and guarantor terms cannot be checked against executed documents. | Medium |
| The latest filing is the quarterly report for the quarter ended in June 2026; the later fiscal year-end is not covered. | Events between the filing and the cutoff are Not supplied, not absent. | Medium |
| No presentation, rating report, call transcript or EBITDA measure is supplied. | Leverage must come from filed lines; management bridges are unavailable. | Medium |

### Readiness view

The effective source set supports all four requested consumers, each as READY_WITH_LIMITATIONS, and no consumer is CONDITIONAL or BLOCKED. The filed 10-K and the three filed 10-Qs are the controlling authority for statement facts; the three earnings releases are management-prepared and are treated as attributed supporting claims that repeat, condense or add to the filings. The limits are bounded: executed financing documents are absent, there is no company-defined EBITDA or covenant leverage figure, and nothing dated after the July 29, 2026 filing is supplied. This is a statement of source sufficiency only; it does not assert that the downstream analyses are complete.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited fiscal 2025 statements (10-K page:88 to page:91) and unaudited June 30, 2026 statements with comparatives (10-Q page:2 to page:5) are located. No company-defined EBITDA is supplied; the March and June 10-Qs give cash flow year to date only. |
| CP-1A | READY_WITH_LIMITATIONS | Business, segments, history and the 2026 financing events are located (10-K page:5 to page:17; 10-Q page:11 to page:13, page:18 to page:19). Credit agreement, amendment, indentures and ASR agreement are not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Can synthesise from CP-1 and CP-1A plus the located covenant, liquidity and contingency text (10-Q page:11, page:20, page:33, page:37). Covenant ratio calculation and revolver availability net of any letters of credit are not supplied. |
| CP-5 | READY_WITH_LIMITATIONS | Every source carries stable page chunks and a visible-text hash, so claims can be traced. Text extraction flattens tables; no image, chart or XBRL review is possible. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source register

#### Form 10-K for fiscal 2025 (`10-K_2025-09-30_fico-20250930.htm.jsonl`)

- Family and authority: filed annual report, original authority for audited consolidated statements. page:1 "For the fiscal year ended September 30, 2025" and "Commission File Number 1-11689". Auditor report page:85 to page:88, signed "Deloitte & Touche LLP" with the date "November 7, 2025" (page:88).
- Statements located: balance sheet page:88 to page:89, income statement page:89, equity statement page:89 to page:90, cash flows page:90 to page:91. Debt note page:104 to page:105. Contractual obligations page:76. Leases page:123 to page:125, commitments page:125, contingencies and guarantees page:126.
- Units: "(In thousands, except par value" on the balance sheet (page:88), USD.
- Perimeter: consolidated Fair Isaac Corporation and subsidiaries. Page:5 "(together with its consolidated subsidiaries, the".
- Extraction: page:94 is a 26-character fragment and page:19 is a heading only; these are chunk boundaries, not lost content, but they are noted as extraction artefacts.

#### Forms 10-Q for the quarters ended December 31, 2025, March 31, 2026 and June 30, 2026

- Family and authority: filed unaudited quarterly reports. Covers: page:1 "For the quarterly period ended December 31, 2025", "For the quarterly period ended March 31, 2026" and "For the quarterly period ended June 30, 2026". Signature dates "DATE: January 28, 2026" (page:37), "DATE: April 28, 2026" (page:43) and "DATE: July 29, 2026" (page:46).
- Statements located in each: balance sheet and income statement at page:2 (and page:3), cash flows at page:3 to page:5. The June 30, 2026 report: balance sheet page:2, income statement page:2 to page:3, equity statement page:3 to page:4, cash flows page:4 to page:5, debt note page:10 to page:12, share repurchase and ASR note page:13, segment note page:18 to page:19, contingencies page:20, liquidity page:33 to page:38.
- Version relationship: the three 10-Qs are separate periods and are all active. The December 2025 and March 2026 reports are superseded for balance-sheet position by the June 2026 report but remain the only source of those interim dates. The December 2025 report carries a three-month cash flow; the March and June reports carry six-month and nine-month cash flows, so discrete second and third quarter cash flows are not in the 10-Qs.
- Units: "(In thousands" tables, USD.

#### Earnings releases (Exhibit 99.1)

- Family and authority: issuer press releases furnished as exhibits, management-prepared and unaudited. The June 2026 quarter release is dated "July 29, 2026" (page:1) and is the only source of the discrete quarter operating cash flow and the free cash flow measure (page:1, page:5).
- It condenses captions relative to the 10-Q: the balance sheet shows "Other assets 193,827" (page:3) where the 10-Q shows deferred income taxes and other assets separately (10-Q page:2), and the income statement shows "Other expense, net" (page:4) where the 10-Q shows interest expense, net and other income, net separately. These are presentation differences, not conflicts.
- Non-GAAP net income, non-GAAP EPS and free cash flow (page:5) and fiscal 2026 guidance (page:2) are management measures. The 10-Q controls statement facts; the releases are not independent corroboration of them.

### Information-availability boundary

- All sources are dated before the as-of date and the cutoff. The latest filed document is the June 30, 2026 10-Q and release, both dated July 29, 2026.
- The fiscal year ended September 30, 2026 is complete before the cutoff, but no fiscal fourth-quarter release or fiscal 2026 10-K is supplied. Events from July 29, 2026 to the cutoff, including the expected settlement of the accelerated share repurchase ("expected to occur during the fourth quarter of fiscal 2026", 10-Q page:13), are Not supplied, not absent.
- The 10-Q lists no subsequent events note; a search for the phrase "subsequent event" returned no match in any source.

### Identity and perimeter

- Reporting entity and debt issuer: Fair Isaac Corporation, Delaware, with consolidated subsidiaries. The 10-Q describes "a credit agreement with a syndicate of banks" (page:11) and notes issued by "we" (page:12). The administrative agent is named on the exhibit list as "Wells Fargo Bank, National Association" (10-Q page:46).
- No parent, sponsor or borrower distinct from the registrant appears; the context leaves borrower, parent and guarantor fields blank, which is not evidence of absence.
- Guarantors: a search of every source for "guarantor" returned no match. The notes and facilities are described as unsecured (10-Q page:11: "unsecured revolving line of credit"; 10-K page:105 for the notes). Whether any subsidiary guarantees them is Not supplied.
- Restricted or unrestricted subsidiary structure is not described in the supplied text.
- Equity: the registrant has a stockholders deficit and large treasury stock (10-Q page:2), which affects what a book-equity measure can say; this is a presentation fact for CP-1, not a conclusion here.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, debt, liquidity, cash-paid interest and tax, KPIs | 10-K page:88 to page:91, page:104 to page:105; 10-Q (June 2026) page:2 to page:5, page:10 to page:12, page:22 to page:25; release page:4 to page:5 | No company EBITDA; year-to-date cash flows only in 10-Qs; fiscal Q4 2026 absent |
| CP-1A | Business, segments, ownership, 2026 financing and capital return events | 10-K page:5 to page:17, page:60 to page:61; 10-Q page:11 to page:13, page:18 to page:19, page:43 | Executed financing documents and ASR agreement not supplied; ownership and sponsor fields blank in context |
| CP-2 | Settled CP-1 and CP-1A registers, covenant and liquidity text, contingencies | 10-Q page:11, page:20, page:33 to page:38, page:43 | Covenant ratio value not printed; undrawn revolver capacity not stated as a figure |
| CP-5 | Pinned pages for every claim | All seven filings and releases | Table flattening; no image or chart inspection |

### Located evidence for downstream use

| Topic | Located evidence (exact text) | Locator |
| --- | --- | --- |
| Debt instruments | "Total debt $ 5,582,389 $ 3,055,691" | 10-Q page:10 |
| Revolver and term loan terms | "a $1.0 billion unsecured revolving line of credit that matures on May 13, 2030" | 10-Q page:11 |
| Term loan | "a $1.5 billion unsecured term loan that was borrowed in full on June 5, 2026 and matures on May 15, 2028" | 10-Q page:11 |
| Term loan amortisation | "(i) $75.0 million from September 30, 2026 through and including June 30, 2027 and (ii) $112.5 million thereafter" | 10-Q page:11 |
| Financial covenant | "a maximum consolidated leverage ratio of 4.5 to 1.0 through December 30, 2026" | 10-Q page:11 |
| Covenant compliance | "we were in compliance with all financial covenants under the credit agreement" | 10-Q page:12 |
| Senior notes | "The 2026 Senior Notes require interest payments semi-annually at a rate of 6.25% per annum and will mature on September 15, 2034" | 10-Q page:12 |
| Senior note face and fair values | "Total $ 3,400,000 $ 3,333,500 $ 2,800,000 $ 2,793,500" | 10-Q page:12 |
| Cash | "Cash and cash equivalents $ 248,444 $ 134,136" | 10-Q page:2 |
| Interest paid | "Cash paid for interest $ 162,420 $ 101,112" | 10-Q page:5 |
| Operating cash flow | "Net cash provided by operating activities 777,880 555,138" | 10-Q page:4 |
| Share repurchase | "we paid $1.5 billion to Wells Fargo Securities and received an initial delivery of 1,055,103 shares" | 10-Q page:13 |
| Litigation | "alleging antitrust claims in connection with the distribution of FICO Scores" | 10-Q page:43 |
| Fiscal 2025 comparator | "Cash paid for interest $ 103,564 $ 106,388 $ 96,877" | 10-K page:90 |
| Fiscal 2025 debt maturities | "Interest due on Senior Notes 147,500 126,000 126,000 90,000 90,000 270,000 849,500" | 10-K page:76 |

### Conflicts and version notes

- No conflict between a filing and a release was found in the lines checked. The release reports the same revenue, net income and cash figures as the 10-Q ("Total revenues 674,188 536,415 1,877,824 1,475,118" on both 10-Q page:2 and release page:4).
- Structure change inside the run: the 10-K debt note (page:104 to page:105) describes a revolver only, with a covenant of "a maximum consolidated leverage ratio of 3.5 to 1.0"; the June 2026 10-Q (page:11) describes a revolver plus a term loan and a stepped covenant schedule. These are different dates and an amendment, not a conflict. The June 2026 text controls for the current position; the base credit agreement and the June 5, 2026 amendment remain separate documents that are not supplied.
- The 10-K note on notes mentions the 2018 notes as outstanding; the 10-Q (page:12) states they were repaid in full on March 26, 2026. This is a dated change, not a conflict.

## Calculations

None. CP-0 does not normalize, reconcile or calculate figures. Coverage counts are source page counts as listed under Sources: 137, 37, 43, 46, 6, 6 and 6 pages, all retained. No derived number is carried into the handoff.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Third Amended and Restated Credit Agreement and First Amendment dated June 5, 2026 not supplied; listed on the exhibit list only (10-Q page:46) | Medium | CP-1A, CP-2 | Obtain the exhibit via the 8-K filed June 8, 2026. Until then covenant definitions and the leverage ratio definition are Not supplied; only the summary text on 10-Q page:11 is used |
| Note indentures (10-K exhibit 4.3 and later, page:133) and the 2026 Senior Notes indenture not supplied | Medium | CP-1A, CP-2 | Obtain indentures; guarantor and covenant terms for the notes are Not supplied |
| Accelerated share repurchase agreement not supplied | Low | CP-1A | Terms are summarised in the 10-Q only (page:13) |
| Company-defined EBITDA, adjusted EBITDA and reported consolidated leverage ratio are not printed in any source (a search for EBITDA returned no match) | Medium | CP-1, CP-2 | Any leverage measure must be built from filed statement lines and labelled as an analyst construction |
| Undrawn revolver capacity and letters of credit usage are not stated as figures (a search for letters of credit and undrawn returned no match); only drawn amounts and the facility size are printed | Medium | CP-1, CP-2 | Report availability as Not supplied unless derived and labelled |
| No filing, release or presentation dated after July 29, 2026; fiscal Q4 2026 and fiscal 2026 results absent | Medium | CP-1, CP-1A, CP-2, CP-5 | Add the fiscal Q4 release and any 8-K when available; events after the filing are Not supplied |
| No investor presentation, call transcript, rating report or market quotes; releases stand in for presentations | Low | CP-1A, CP-2 | Treat management language as attributed; ratings and quotes are blank in context |
| Second and third fiscal quarter cash flows are year to date in the 10-Qs; only the third quarter operating cash flow and free cash flow are in the release (page:1, page:5) | Low | CP-1 | Derive discrete quarters only when both year-to-date figures are present and label them as derived |
| Text extraction flattens tables; no image, chart or XBRL fidelity review | Low | CP-5 | Spot-check tables against the filed HTML if available |
| Context fields for borrower, parent, guarantors, deal terms, quotes and ratings are blank | Low | CP-1A, CP-2 | Blank is not zero; treat as not supplied |

## Next module

Run CP-1 next on the same pack, followed by CP-1A, CP-2 and CP-5. Carry forward these limitations: no executed financing documents, no company-defined EBITDA or covenant leverage figure, no stated revolver availability, second and third quarter cash flows stated year to date, and no evidence dated after July 29, 2026. Use the June 30, 2026 10-Q as the controlling source for current debt, liquidity and covenant text, the fiscal 2025 10-K for annual comparators, and label the releases as management-prepared.
