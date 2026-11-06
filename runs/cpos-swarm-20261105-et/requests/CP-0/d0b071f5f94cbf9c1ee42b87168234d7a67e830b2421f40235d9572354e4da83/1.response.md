# CP-0 source readiness: Energy Transfer LP (et)

## Request

- Issuer: Energy Transfer LP (issuer id et, ticker ET), as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD (context); period focus Q3 2026 against FY2025.
- Run: `et-2026-11-05-credit_snapshot-host`, pathway credit_snapshot, requested modules CP-1, CP-1A, CP-2 and CP-5. CP-0 runs first and is their dependency.
- Execution: host session. The host searched and read the pinned page-chunked text files and wrote this answer. No provider was called.
- Question: can the seven supplied public filings and releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion is given, and no figure is normalized, reconciled or calculated here.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_et-20251231.htm.jsonl | cf6ec450a74c280b3feab654167ed9d76760431021a13bf17a88d72b8532eaa7 | Form 10-K for the year ended December 31, 2025 (398 pages) |
| 10-Q_2026-03-31_et-20260331.htm.jsonl | 204d33e965723c9110a8bd3c410929503a162c990398e4a307e9e4585208124c | Form 10-Q for the quarter ended March 31, 2026 (83 pages) |
| 10-Q_2026-06-30_et-20260630.htm.jsonl | f6fbfa69a08a1bbb53482543b3abf672768e886f0ec8d32dd533da3f97f4bf88 | Form 10-Q for the quarter ended June 30, 2026 (95 pages) |
| 10-Q_2026-09-30_et-20260930.htm.jsonl | b99e2e6cdfbc85d8be8a5393c48692fdcdcd98f8ad63f20f2e4b37b17c6562f1 | Form 10-Q for the quarter ended September 30, 2026 (99 pages) |
| EX-99.1_2026-05-05_ex991eterq12026.htm.jsonl | 28e020c73aad041b3d8d17b54f534d805074c7d2b4b4b027cc87b57e5e12fd7c | Exhibit 99.1 first-quarter 2026 earnings release dated May 5, 2026 (19 pages) |
| EX-99.1_2026-08-04_ex991eterq22026.htm.jsonl | ee1907b3dce0abf5f0cf3c0b28a73722fa7c995776f463ee976582a26da21fa9 | Exhibit 99.1 second-quarter 2026 earnings release dated August 4, 2026 (18 pages) |
| EX-99.1_2026-11-03_ex991eterq32026.htm.jsonl | 5531a7cf0a40c534ed0feab25ecafdebb29b6fb0df1d6b068954124b5c1f91f7 | Exhibit 99.1 third-quarter 2026 earnings release dated November 3, 2026 (18 pages) |
| context | dfad783f6af55323b89ba2b387376722ec78e773820c07687193a91e09314cf8 | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module. `_retrieval.json` in the pack was ignored by the launcher and is not a source.

Locators are `page:N`, the chunk number inside the named `.jsonl` file, not the printed page number. Each file's first chunk repeats an internal digest of the original HTML text; that digest is a different value from the file hash above and was not used.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases are enough to run the four requested modules with stated limits. Statements, debt notes, liquidity and the latest quarter are all located; indentures, credit agreements and the corporate conversion documents are not. | Medium | Executed debt documents and the filing that records the change of corporate form are not supplied, so covenant terms and guarantor structure rest on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited year-end statements and three quarterly reports are all present, and the latest quarterly report is dated on the as-of date. | Current-period work can use filed, controlling statements without gaps in the quarter sequence. | High |
| The issuer's form and listing changed during 2026, but the supplied files only show this on cover pages and in one cross-reference. | The legal entity that owns the debt should be confirmed before any structural conclusion. | Medium |
| Debt sits at the parent and at two publicly traded subsidiaries, each with its own facilities. | A single consolidated debt figure mixes parent and subsidiary obligations; later work must keep them apart. | Medium |
| Earnings releases are management presentations and repeat the quarterly reports. | They add non-GAAP measures and guidance but cannot override the filings. | High |

### Readiness view

The effective source set supports all four requested modules with limitations. The company's annual report, its three 2026 quarterly reports and its three earnings releases carry consistent period labels and the same commission file number, differing only in state of organisation and listing venue (see Identity and perimeter), and together cover the full fiscal year 2025, the nine months to September 30, 2026 and the events up to the as-of date. Source sufficiency is established for statements, the debt note, liquidity text, segments and subsequent events. It is not established for executed debt agreements, indentures, or the filing that records the change of corporate form, none of which is supplied. This is a source verdict only; completion of downstream analysis is not asserted.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025 statements, interim statements for Q1, Q2 and Q3 2026 with comparatives, debt tables and segment note are located. Source text is a flattened HTML extraction, so table layout was not visually checked. |
| CP-1A | READY_WITH_LIMITATIONS | Business description, segments, subsidiary structure, acquisitions and the October 2026 Vaquero agreement are located. The change in jurisdiction and exchange listing is evidenced only on cover pages and one cross-reference; the underlying filing is not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Debt tables, credit facility availability, the stated covenant leverage ratio and subsidiary facilities are located. Credit agreement and indenture definitions are not supplied, so the covenant ratio cannot be rebuilt from definitions. |
| CP-5 | READY_WITH_LIMITATIONS | Every source is page-chunked and traceable. No original HTML, XBRL or images are supplied; visual and chart checks are not possible. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source register

#### Form 10-K, fiscal year 2025 (`10-K_2025-12-31_et-20251231.htm.jsonl`)

- Family and authority: filed annual report and original authority for audited FY2025 and FY2024 statements. page:1 reads "For the fiscal year ended DECEMBER 31, 2025" and "Commission file number 1-32740".
- Audit: page:283 holds the report of the independent registered public accounting firm ("We have audited the accompanying consolidated balance sheets of Energy Transfer LP (a Delaware limited partnership)"). The internal-control opinion is signed "GRANT THORNTON LLP Dallas, Texas February 19, 2026" (page:229).
- Statements: balance sheet at page:286 and page:287; statements of operations at page:287 and page:288; cash flows at page:288 and page:289. Debt note tables at page:323 and page:324, with text on notes and the credit facility from page:325. Reportable segments note at page:394. The index to financial statements is at page:282.
- Perimeter: consolidated Energy Transfer LP and subsidiaries, with noncontrolling interests. At filing, the cover shows state "Delaware" and exchange "New York Stock Exchange" (page:1).
- Units: dollars in millions unless stated; USD.

#### Form 10-Q, quarter ended March 31, 2026 (`10-Q_2026-03-31_et-20260331.htm.jsonl`)

- Family and authority: filed, unaudited interim report. page:1 reads "For the quarterly period ended March 31, 2026"; signature page:83 "Date: May 7, 2026".
- Debt table with March 31, 2026 and December 31, 2025 columns at page:72 ("Total debt 69,336 68,333").
- Cover state is "Delaware" (page:1).

#### Form 10-Q, quarter ended June 30, 2026 (`10-Q_2026-06-30_et-20260630.htm.jsonl`)

- Family and authority: filed, unaudited interim report. page:1 reads "For the quarterly period ended June 30, 2026"; signature page:95 "Date: August 6, 2026".
- Debt table at page:84 ("Total debt 68,405 68,333").
- Cover state is "Texas" while the listing is still "New York Stock Exchange" (page:1). The state of incorporation therefore differs from the 10-K and first-quarter report.

#### Form 10-Q, quarter ended September 30, 2026 (`10-Q_2026-09-30_et-20260930.htm.jsonl`)

- Family and authority: filed, unaudited interim report and the controlling source for the latest period. page:1 reads "For the quarterly period ended September 30, 2026"; signature page:99 "Date: November 5, 2026", which is the as-of date. It is inside the cutoff.
- Statements: balance sheet page:3 and page:4 (cash "Cash and cash equivalents $ 926 $ 1,272"), statements of operations page:4 and page:5, equity page:6, cash flows page:6 and page:7. Note 7 debt at page:17 and page:18; debt table at page:87; segment note 13 at page:52; Management's Discussion from page:57; liquidity from page:83.
- Cover state "Texas" and exchange "Texas Stock Exchange" for both the common units and the Series I preferred units (page:1). The MD&A refers to a "Current Report on Form 8-K12B filed with the SEC on July 6, 2026" (page:57). That current report is not supplied.

#### Earnings releases, Exhibit 99.1 (three files)

- Family and authority: issuer press releases furnished as exhibits: first quarter "Dallas – May 5, 2026", second quarter "Dallas – August 4, 2026", third quarter "Dallas – November 3, 2026" (page:2 of each). Management-prepared and unaudited; they present reported and non-GAAP measures.
- The first two releases label the listing "NYSE:ET" and the third labels it "TXSE:ET" (page:2 of each), matching the cover pages of the 10-Qs.
- Content located in the third-quarter release: condensed balance sheet (page:6), statement of operations (page:6, page:7), reconciliation of net income to Adjusted EBITDA and Distributable Cash Flow (page:7), segment discussion (page:12 to page:17), liquidity table (page:17), unconsolidated affiliates (page:17) and non-wholly owned subsidiaries (page:18). Guidance: "The Partnership now expects its Adjusted EBITDA for the full year of 2026 to range between $19.7 billion and $19.9 billion" (page:2).
- Version relationship: the statement of operations and balance sheet repeat the 10-Q for the same period. The 10-Q controls for statement facts; the release is attributed management presentation for Adjusted EBITDA, Distributable Cash Flow and guidance. The release is not independent corroboration of the 10-Q statements.
- The release liquidity table shows only the parent facility: "We also have consolidated subsidiaries with revolving credit facilities which are not included in this table." (page:17)

### Information-availability boundary

- Latest supplied document is the Form 10-Q signed November 5, 2026, the as-of date. Nothing is dated after the cutoff.
- Events between the September 30, 2026 balance sheet date and November 5, 2026 are limited to what the 10-Q and the third-quarter release state, for example the acquisition agreement signed on "October 6, 2026" for Vaquero (10-Q page:57) and the termination on "October 8, 2026" of Sunoco LP's receivables financing agreement (10-Q page:18). Other post-quarter filings, such as current reports, are Not supplied, not absent.

### Identity and perimeter

- Reporting entity: Energy Transfer LP, Dallas, Texas. The filings describe the Partnership as consolidating Sunoco LP, USAC and SunocoCorp (10-Q Q3 page:8, "The Partnership owns a controlling interest in USAC.").
- Subsidiary debt: the Q3 10-Q note on debt names separate facilities for Sunoco LP ("Sunoco LP Credit Facility") and USAC ("USAC Credit Facility") in addition to the parent's "Five-Year Credit Facility" (page:18), and the Q3 debt table at page:87 lists them as separate lines. These are consolidated but separate borrowers.
- Notes at the parent: the 10-K states "The Energy Transfer senior notes are not guaranteed by any of its subsidiaries." (page:325). Guarantor structure for other instruments is not stated in the supplied text; the context leaves borrower, parent and guarantor fields blank, which is not evidence of their absence.
- Change of form and listing: the 10-K cover shows Delaware and the New York Stock Exchange; the first-quarter report shows Delaware; the second-quarter report shows Texas with the New York Stock Exchange; the third-quarter report shows Texas with the Texas Stock Exchange. The files do not describe the transaction that caused this, apart from the 8-K12B cross-reference. Whether the registrant is the same legal entity, a successor, and whether indenture and credit agreement parties changed is an unresolved distinction carried as a gap. The commission file number is unchanged at "1-32740" on all four periodic reports (page:1 of each).
- Preferred units: "9.250% Series I Fixed Rate Perpetual Preferred Units" are listed with the common units (page:1 of the Q3 10-Q).

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, debt, liquidity, non-GAAP, nine-month and quarter columns | 10-K page:286 to page:289 and page:323 to page:324; Q3 10-Q page:3 to page:7, page:17 to page:18, page:87; Q3 release page:6 to page:7 | Flattened text; Adjusted EBITDA and Distributable Cash Flow are issuer non-GAAP; consolidated debt includes subsidiary debt |
| CP-1A | Business, segments, subsidiaries, acquisitions, ownership, recent developments | 10-K page:394; Q3 10-Q page:8, page:52, page:57; Q3 release page:2 to page:4 | Change of state and exchange documented only on covers; Vaquero closing is a post-quarter expectation |
| CP-2 | Debt by issuer, maturities, facilities, covenant statement, liquidity, commitments | 10-K page:323 to page:325; Q3 10-Q page:18, page:83 to page:89 | Credit agreements and indentures not supplied; covenant ratio is as reported, not rebuildable |
| CP-5 | Traceable claims | All seven sources are chunked with stable page numbers | No HTML, XBRL or images; chunk numbers are not printed page numbers |

### Analytical read-through

- Usable coverage: the 10-K gives audited FY2025 and prior-year comparatives; the three 10-Qs give Q1, Q2 and Q3 2026 with comparatives and a nine-month cash flow statement in the latest report. Together they allow discrete quarters to be derived later and a last-twelve-months view to be built from the year and the nine-month periods. This is a statement of source sufficiency; the derivation itself is not performed here.
- Strongest contrary evidence: the issuer changed state of organisation and listing venue mid-year, and the files give only cover-page evidence and the 8-K12B cross-reference. If the registrant, obligor or indenture parties changed, a consumer that treats the FY2025 audited entity as identical to the Q3 2026 entity could misattribute debt and covenants.
- Source risk mechanism: reported debt combines the parent's notes and facilities with those of Sunoco LP and USAC, which have their own revolvers and note series and are not guaranteed by the parent's notes. A consumer that reads only a consolidated debt total can overstate the parent's own claim stack or understate the subsidiary-level priority.
- Second mechanism: management's Adjusted EBITDA and Distributable Cash Flow in the releases are reconciled to net income but include items such as Adjusted EBITDA of unconsolidated affiliates; they are not audited and the covenant leverage ratio in the 10-Q is defined in agreements that are not supplied.
- What cannot proceed: covenant rebuilds from agreement definitions, guarantor-by-guarantor analysis, legal entity mapping across the change of form, and any use of market, ratings or peer data (none supplied, context lists none).
- Next evidence action: supply the Form 8-K12B filed on July 6, 2026 and the related successor documentation, the current revolving credit agreement and indentures for the parent senior and junior subordinated notes, and any current reports dated after the September 30, 2026 balance sheet date up to November 5, 2026.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Figures that appear above are quoted from the cited locators for identification only.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Form 8-K12B filed July 6, 2026 and documents of the change of state and listing not supplied | High | CP-1A, CP-2 | Supply the filing and any successor-obligor or supplemental indenture documents |
| Executed credit agreement, indentures and supplemental indentures not supplied; covenant definitions and guarantor lists not verifiable | High for legal work; Medium for CP-2 | CP-2 | Supply executed documents |
| Current reports and other filings between the Q3 balance sheet date and November 5, 2026 not supplied | Medium | CP-1A, CP-2 | Supply or confirm none |
| Flattened HTML text only; tables not visually checked, no XBRL, no images or charts | Low | CP-1, CP-5 | Check flagged tables against the filed HTML |
| Releases are management non-GAAP presentations; Adjusted EBITDA and Distributable Cash Flow are not audited | Medium | CP-1, CP-2 | Label as issuer non-GAAP; rely on the 10-Q for statement facts |
| Subsidiary credit facilities and note series sit inside consolidated debt; guarantor structure beyond the parent senior notes statement not located | Medium | CP-2 | Keep parent and subsidiary debt separate; seek subsidiary debt documents if needed |
| No rating reports, market prices, peer or valuation data (context fields blank) | Low for the selected modules | CP-2 | Not required for this scope; keep Not supplied |

## Next module

- CP-1: treat the 10-K and the 10-Qs as controlling for statements; keep audited annual, quarter and nine-month columns separate; keep parent and subsidiary debt separate; label Adjusted EBITDA and Distributable Cash Flow from the releases as issuer non-GAAP; use the Q3 10-Q as the latest balance sheet.
- CP-1A: carry the change of state and exchange as an unresolved identity point with only cover-page evidence; carry the Vaquero acquisition as signed on October 6, 2026 and not closed; treat anything after November 5, 2026 as outside the cutoff.
- CP-2 and CP-5: carry the missing executed debt documents and the 8-K12B as restrictions; do not rebuild the covenant ratio from definitions; cite by file and page chunk.
