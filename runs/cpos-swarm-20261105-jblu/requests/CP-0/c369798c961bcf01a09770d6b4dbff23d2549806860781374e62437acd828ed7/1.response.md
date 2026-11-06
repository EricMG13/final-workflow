# CP-0 — Source readiness: JETBLUE AIRWAYS CORP (jblu)

## Request

- Issuer: JETBLUE AIRWAYS CORP (issuer id `jblu`; registrant name in the filings: "JETBLUE AIRWAYS CORPORATION"; ticker JBLU, NASDAQ). As-of date 2026-11-05; information cutoff 2026-11-05 (context).
- Run `jblu-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, reporting currency USD, current period Q3 2026 (quarter ended September 30, 2026), prior period FY2025 (context). Requested downstream modules: CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned source text and wrote this answer. No provider was called.
- Question: can the supplied public filings support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This handoff gives no credit conclusion, legal interpretation or investment opinion, and normalizes, reconciles or calculates no figure.

## Sources

Hashes below are the sha256 of the pinned text extraction (`.jsonl`) that CP-OS names for this run. Each extraction opens with the sha256 of the original filed HTML, which is shown in the Role column. A locator `page:N` is the extraction chunk number, not the printed page number.

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_jblu-20251231.htm.jsonl | 5eaf617accf854e4d3e9a550a2ff2955ebfa71253742ee07dd6faac0b2e32a8c | Annual report on Form 10-K, fiscal year ended December 31, 2025, 182 chunks; original HTML sha256 a0b71a2a1a64296be62dc053b37f90838832bc02d616bd84eb540e02f4f58101 |
| 10-Q_2026-03-31_jblu-20260331.htm.jsonl | 23aa04d969e5d0170c0af37c935f385dfb36e65e5eefd81c73b6d9abfad792fa | Quarterly report on Form 10-Q, quarter ended March 31, 2026, 47 chunks; original HTML sha256 0da7ddb97f631028d05a16f18f957ded306b75c73cdfce8dbf31aba6eec322af |
| 10-Q_2026-06-30_jblu-20260630.htm.jsonl | 909f0d616195258039c6cade15d6ec9c2498b992386b681904fa4366c00d0fca | Quarterly report on Form 10-Q, quarter ended June 30, 2026, 54 chunks; original HTML sha256 af1854765d1bd016637512a25da83427cdde1f94b3ffc70cda72d9592b4c51b0 |
| 10-Q_2026-09-30_jblu-20260930.htm.jsonl | acf402823b4f024901754bb305241f6c703d6a3c7b62a75b67703d555b0a8e99 | Quarterly report on Form 10-Q, quarter ended September 30, 2026, 54 chunks; original HTML sha256 f900391489099ff64b7425ae0818da2e8106caa7599107b859795f7b72ee924f |
| EX-99.1_2026-04-28_ex991-earningsreleaseq12026.htm.jsonl | d4d4219d15ba6a638e2373e8ae55aa1c8d909855e1454637cd8095dcf728854e | Exhibit 99.1 earnings release dated April 28, 2026 (first quarter 2026), 11 chunks; original HTML sha256 ffb248a3a8304164cee0aa5a6d5774f6420d4c0991253f038e2e211c1cb7aecb |
| EX-99.1_2026-07-28_ex991-earningsreleaseq22026.htm.jsonl | 802f55be8bbdb2947fd6f1ea1be406ca4f8ca6aa8c3d778ecad7cf301e68ccf6 | Exhibit 99.1 earnings release dated July 28, 2026 (second quarter 2026), 12 chunks; original HTML sha256 c1022a876f8ea1fb272f33557ad0cc853122140c742332a3d0c12a9b6e63d3b9 |
| EX-99.1_2026-10-26_ex991-earningsreleaseq32026.htm.jsonl | 698b07a0502ae526f90cdcc0cd39f907723cfed08c5317bc057549e3a8aec7de | Exhibit 99.1 earnings release dated October 26, 2026 (third quarter 2026), 12 chunks; original HTML sha256 218669fdb1adf3f2bcfe937b6575f5d073366b63618bda08815ffe1f7c15d6eb |
| context | 31c25d56081dda135cad8e796a84043b049461aaa2d0b6432dd4792f868c14f8 | User run settings; not issuer evidence. Borrower, parent, guarantor, rating, quote and deal-term fields are blank, which is not evidence that none exist |

Supplied handoffs: none. CP-0 is the first module and CP-OS supplies no upstream handoff.

Ignored by the launcher: `_retrieval.json`, a retrieval log, not issuer evidence. It records that all three quarters have a release and no presentation on EDGAR; the pack therefore holds no investor presentation.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filed 10-K, three 10-Qs and three earnings releases give a dated, internally consistent base for downstream work on JetBlue through the quarter ended September 30, 2026, with bounded limitations. | Medium | Debt agreements, covenant levels and rating or market data are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The audited annual report and unaudited quarterly reports cover FY2025 and Q3 2026 on one reporting entity in USD millions. | Statements, debt and liquidity can be read at issuer level without a perimeter change. | High |
| Debt is itemised by instrument in the quarterly debt note with a maturity table, but the debt agreements themselves are not supplied. | Guarantor and covenant terms can only be taken from filing summaries, not checked against the agreements. | Medium |
| Management states it complied with the material covenants, and gives no numeric covenant levels or headroom. | Covenant headroom cannot be measured from these sources. | Medium |
| Later events up to the cutoff are limited to what the latest quarterly report and release describe. | Anything filed after October 26, 2026 is not supplied, so recent financing or litigation steps may be missing. | Medium |

### Readiness view

The view is READY_WITH_LIMITATIONS for all four requested consumers. The effective source set is one registrant's filed annual report, three filed quarterly reports and three furnished earnings releases, all dated before the as-of date, so each consumer can perform its own method; none is made CONDITIONAL or BLOCKED. The limitations are that the pack contains no executed debt or lease agreements, no investor presentations, no ratings or market data, and only text extractions in which tables are flattened. These bounds carry into each consumer's assessment below. Source sufficiency is not completion of any downstream analysis.

| Consumer | Status | Basis | Command sheet |
| --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025, FY2024 and FY2023 statements and unaudited statements for each of Q1 2026, Q2 2026 and Q3 2026 with comparatives are located. Limits: text extraction flattens tables; no XBRL or original layout is supplied. | RUN |
| CP-1A | READY_WITH_LIMITATIONS | Business description, strategy, fleet, labor, Blue Sky and TrueBlue financing narrative, litigation and later events are located in the 10-K and 10-Qs. Limits: the exhibit-listed agreements and any proxy statement are not supplied. | RUN |
| CP-2 | READY_WITH_LIMITATIONS | Debt note, maturity table, liquidity statement, commitments and covenant description are located. Limits: covenant levels and headroom, guarantor detail and agreement definitions are not supplied. | RUN |
| CP-5 | READY_WITH_LIMITATIONS | All seven sources carry stable chunk numbers, so claims can be traced. Limits: visual and table-layout checks against the filed HTML are not possible from text. | RUN |

### Source register

#### Form 10-K for FY2025 (10-K_2025-12-31_jblu-20251231.htm.jsonl)

- Family and authority: filed annual report; original authority for audited FY2025, FY2024 and FY2023 results. Cover, page:1: "For the fiscal year ended December 31, 2025". Registrant, page:1: "JETBLUE AIRWAYS CORPORATION (Exact name of registrant as specified in its charter)".
- Audit: page:108 "We have audited the accompanying consolidated balance sheets of JetBlue Airways Corporation (the Company) as of December 31, 2025 and 2024". Auditor tenure, page:109: "We have served as the Company’s auditor since 2001." Report date, page:109: "New York, New York February 12, 2026". The internal-control opinion is unqualified (page:108: "expressed an unqualified opinion thereon").
- Statements located: balance sheets page:112 ("TOTAL ASSETS $ 16,570 $ 16,841" is the December 31, 2025 and 2024 pair on the asset side), statements of operations page:113, cash flows page:114. Units, page:113: "(in millions, except per share data)". USD.
- Perimeter: one consolidated registrant; page:159 "JetBlue has one reportable operating segment, air transportation services."
- Debt: financing narrative at page:129 and page:130 (TrueBlue notes and term loan); market-risk and covenant description at page:94 and page:97.
- Exhibit index at page:168 onwards lists indentures and credit agreements by title; the agreements themselves are not supplied.

#### Form 10-Q for the quarter ended March 31, 2026 (10-Q_2026-03-31_jblu-20260331.htm.jsonl)

- Family and authority: filed, unaudited quarterly report. Page:1: "For the quarterly period ended March 31, 2026". Signature, page:47: "Date: April 28, 2026".
- Statements: operations page:6 with "Three Months Ended March 31,"; basis is quarter only (no year-to-date column for Q1). Liquidity statement located on page:30: "At March 31, 2026, we had $2.4 billion in liquidity".
- Version relationship: the Q1 report remains a separate active source and is not collapsed into the later reports.

#### Form 10-Q for the quarter ended June 30, 2026 (10-Q_2026-06-30_jblu-20260630.htm.jsonl)

- Family and authority: filed, unaudited. Page:1: "For the quarterly period ended June 30, 2026". Signature, page:54: "Date: July 28, 2026".
- Statements: operations page:6 with "Three Months Ended June 30, Six Months Ended June 30," so quarter and six-month year-to-date are both labelled.

#### Form 10-Q for the quarter ended September 30, 2026 (10-Q_2026-09-30_jblu-20260930.htm.jsonl)

- Family and authority: filed, unaudited; the latest filed financial report in the pack. Page:1: "For the quarterly period ended September 30, 2026". Signature, page:54: "Date: October 26, 2026".
- Statements: balance sheets page:5 and page:6 ("September 30, 2026 December 31, 2025"), operations page:6 ("Three Months Ended September 30, Nine Months Ended September 30,"), cash flows page:7 ("Nine Months Ended September 30,"), units page:5 "(in millions, except per share data)". USD.
- Debt: Note 3 at page:11 to page:15 holds the instrument table, the maturity table, fair value and the Citibank and Morgan Stanley lines. Liquidity at page:44, covenant statement at page:47, commitments at page:17, market risk at page:53.
- Perimeter note: the debt note describes TrueBlue notes "co-issued with JetBlue Loyalty LP" (page:47: "In August 2024, JetBlue co-issued with JetBlue Loyalty LP"). The statements are consolidated; no stand-alone statements for JetBlue Loyalty LP are supplied.
- Basis note: two debt totals appear with different bases. Page:11: "Total debt and finance lease obligations $ 8,450 $ 8,560" before issuance costs, and page:12: "Total Debt $ 8,393 $ 7,620 $ 8,498 $ 7,829" as carrying value net of issuance costs followed by fair value. A downstream user must name which basis is used.

#### Earnings releases, Exhibit 99.1 (three files)

- Family and authority: issuer press releases furnished with Form 8-K; management-prepared and unaudited, so they give attributed supporting claims and do not override the filings. Q1 page:2 "JETBLUE ANNOUNCES FIRST QUARTER 2026 RESULTS"; Q2 page:1 "JETBLUE ANNOUNCES SECOND QUARTER 2026 RESULTS" and "NEW YORK (July 28, 2026)"; Q3 page:1 "JETBLUE ANNOUNCES THIRD QUARTER 2026 RESULTS" and "NEW YORK (October 26, 2026)".
- Content: statements of operations, operating statistics, selected balance sheet and cash-flow data, and non-GAAP reconciliations (Q3 page:9 "Note A - Non-GAAP Financial Measures"; page:11 reconciliation excluding special items and gain on investments). Guidance basis, Q3 page:4: "Revised guidance as of September 10, 2026."
- Version relationship: the release statements of operations repeat the 10-Q statements (Q3 page:7 and the 10-Q page:6 both show "Total operating revenues 2,812 2,322 7,749 6,818"). Treat the 10-Q as controlling for statement facts and the release as supporting, not independent, corroboration.
- Management claims to be attributed, not verified from filings: Q3 page:2 "Expanded unencumbered asset base to ~$7 billion".
- Non-GAAP: CASM ex-fuel, adjusted operating margin and loss per share excluding special items are management measures, not GAAP.

### Information-availability boundary

- Latest dated evidence: the Q3 10-Q and Q3 release, both dated October 26, 2026, which is before the as-of date and cutoff 2026-11-05. No source is dated after the cutoff. Text of future dates in the sources, for example the inflight crewmember contract "amendable date of December 13, 2026" (Q3 10-Q page:19) and a BlueFirst service start in December 2026, is forward-looking and labelled as such there.
- Events between October 26, 2026 and 2026-11-05 are Not supplied, not absent.
- Subsequent events inside the filings: Q3 10-Q page:44 "Following receipt of regulatory approval, the Company completed the acquisition in October 2026" (22 LaGuardia slots previously operated by Spirit Airlines); page:14 additional aircraft-secured financing "Funding is expected in the fourth quarter of 2026"; page:21 "On October 9, 2026, the Company and American filed a brief opposing that class certification".

### Identity and perimeter

- Reporting entity: JetBlue Airways Corporation, Delaware (10-K page:1), a single consolidated registrant with one reportable segment (10-K page:159).
- Issuer, borrower and guarantor roles: the filings name JetBlue and JetBlue Loyalty LP as co-issuers of the TrueBlue notes (10-K page:129: "co-issued $2.0 billion aggregate principal amount of senior secured notes due 2031"). Guarantor identities are in the indenture, which is not supplied. Equipment notes and EETCs are issued by the Company, with pass-through trusts that are not consolidated (Q3 10-Q page:13: "we have not consolidated these trusts in our financial statements").
- Unresolved: no restricted-group, parent or stand-alone Loyalty LP statements; the context leaves these fields blank.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, debt, liquidity, cash flows, non-GAAP | 10-K page:112 to page:114; 10-Q Q3 page:5 to page:7, page:11 to page:15; releases | Text extraction; two debt bases; quarter versus year-to-date labels must be kept; non-GAAP is management-defined |
| CP-1A | Business, fleet, strategy, labor, ownership of financings, later events | 10-K page:9; Q3 10-Q page:31 to page:33, page:19 | No agreements or proxy statement; no stand-alone Loyalty LP view |
| CP-2 | CP-1 and CP-1A outputs, maturity wall, liquidity, covenants, commitments | Q3 10-Q page:12, page:17, page:44, page:46 to page:47 | Covenant levels and headroom not printed; pledged assets stated only as share and net book value |
| CP-5 | Traceable claims | All seven sources carry chunk numbers | No original layout or XBRL; chunk numbers differ from printed pages |

### Analytical read-through

- Usable coverage: an audited three-year annual set plus three consecutive unaudited quarters and three releases give a complete run of reporting dates from December 31, 2025 to September 30, 2026. The interim 10-Qs carry the December 31, 2025 balance sheet as comparative, which lets a downstream user tie the balance sheet to the audited annual report.
- Strongest contrary evidence: the pack is filings only. The 10-Q states management's covenant position as "we were in compliance with the material covenants of our debt and lease agreements" (page:47) but prints no test level, so a reader cannot test headroom. The TrueBlue agreements are described as containing "debt service coverage ratios and minimum liquidity requirements" and "a cross-default to other material indebtedness" (page:47), and the notes and term loan are co-issued with a subsidiary partnership. A consumer that reads only the consolidated debt line would miss that this financing has its own tests and its own cross-default.
- Source risk mechanism: debt, finance lease obligations and failed sale-leaseback obligations sit in one reported line ("Aircraft failed sale-leaseback transactions, due through 2036", Q3 10-Q page:11), and the debt note shows two totals on different bases. A consumer that picks a total without naming its basis, or that excludes the failed sale-leasebacks, would misstate fixed obligations. Operating lease liabilities, flight equipment purchase commitments and other obligations are reported outside the debt note (Q3 10-Q page:46 contractual obligations table), so they need separate handling downstream.
- What cannot proceed: covenant headroom against agreement definitions, guarantor-level analysis, any rating-agency or market-implied view, and peer relative value from these sources.
- Next evidence action: supply the TrueBlue indenture and term loan agreement and the Citibank credit agreement listed in the 10-K exhibit index, any covenant compliance certificates or levels, and any filings made between October 26, 2026 and 2026-11-05.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Figures quoted above are reproduced from the cited locators only.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed debt agreements (TrueBlue indenture and term loan, equipment notes, Citibank credit agreement) are not supplied | High | CP-2, CP-1A | Supply the agreements named in the 10-K exhibit index |
| Numeric covenant levels and headroom are not printed in the supplied filings | High | CP-2 | Supply compliance certificates or the covenant schedules |
| Guarantor identities and restricted-group perimeter for the TrueBlue financing are not in the supplied text | Medium | CP-2, CP-1A | Supply the indenture and guarantor schedule |
| No investor presentations: all three quarters have a release only | Low | CP-1A, CP-5 | Supply presentations if management claims need slide-level support |
| No ratings, market prices or valuation inputs (context fields blank) | Medium | CP-2 | Supply ratings and quotes if a market view is wanted |
| Text extraction only: tables are flattened and no XBRL or original layout is supplied | Medium | CP-1, CP-5 | Check figures against the filed HTML when a number drives a conclusion |
| Two debt totals on different bases (gross of issuance costs versus carrying value) | Low | CP-1, CP-2 | Name the basis in every downstream use |
| Events after October 26, 2026 up to 2026-11-05 are not supplied | Medium | CP-1A, CP-2 | Supply later 8-K filings or confirm none |
| Revised guidance dated September 10, 2026 is referenced in the Q3 release but the announcement itself is not supplied | Low | CP-1A | Supply the September 10, 2026 announcement if guidance changes matter |

## Next module

CP-1 (financial statements and credit metrics) runs first under the dependency order; CP-1A, CP-2 and CP-5 follow. All four are RUN with the limitations recorded above.
