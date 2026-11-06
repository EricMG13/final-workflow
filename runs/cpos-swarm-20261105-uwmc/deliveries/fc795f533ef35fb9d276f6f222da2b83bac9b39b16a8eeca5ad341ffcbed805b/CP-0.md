# CP-0 — Source readiness: UWM Holdings Corp (uwmc)

## Request

- Issuer: UWM Holdings Corp (UWM Holdings Corporation, NYSE "UWMC"), as of 2026-11-05, information cutoff 2026-11-05, pathway credit_snapshot, reporting currency USD, current period Q2 2026 (quarter ended June 30, 2026), prior period FY2025 (context).
- Requested consumers: CP-1, CP-1A, CP-2 and CP-5 (the launcher's minimum set). CP-0 runs first as their dependency.
- Execution: host session; the host read the pinned files and wrote this answer. No provider was called.
- Question: can the supplied filings support those four consumers, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This handoff gives no credit conclusion, legal interpretation or investment opinion, and it normalizes, reconciles and calculates no figures.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_uwmc-20251231.htm.jsonl | 6df0e879c343753ce405aeb907aabeaeac058e835b89efb10be5b5f6ef447e2d | Annual report on Form 10-K for the year ended December 31, 2025 (176 pages) |
| 10-Q_2025-09-30_uwmc-20250930.htm.jsonl | 84f53b3c261a44ff2b63ce2fd8da76aab14001838b1a0e3a2f304e513f9c0145 | Quarterly report on Form 10-Q for the quarter ended September 30, 2025 (75 pages) |
| 10-Q_2026-03-31_uwmc-20260331.htm.jsonl | eb1fccb72198e8bd32b24af480098c49a4e103fa66da8e8b43ba0a46fdd7b8e3 | Quarterly report on Form 10-Q for the quarter ended March 31, 2026 (66 pages) |
| 10-Q_2026-06-30_uwmc-20260630.htm.jsonl | cea2518652546d9284379186814d587a8012203f70fc41bfc3b1a399bf834746 | Quarterly report on Form 10-Q for the quarter ended June 30, 2026 (72 pages) |
| EX-99.1_2026-02-26_irdeck4q25andfy2025-fina.htm.jsonl | 80372136ddaf727708bb7d020bd60e922c0bc6f80a8ff31bd92d35cba8e5b9c2 | Exhibit 99.1 earnings presentation, February 2026, fourth quarter and FY2025 (12 pages) |
| EX-99.1_2026-05-06_q12026ex-991pressrelease.htm.jsonl | 3516810c7f76bb754add7c9c09ef459031d4e398744e48f97ba6a9a478ed6c73 | Exhibit 99.1 press release dated May 6, 2026, first quarter 2026 results (12 pages) |
| EX-99.1_2026-08-05_q22026ex-991pressrelease.htm.jsonl | fce3d1caab58675ec9b80c128baca52e2510780e5b4d2dc29c8a0ea2b81bebde | Exhibit 99.1 press release dated August 5, 2026, second quarter 2026 results (12 pages) |
| context | 9e4b4c779a926897468f1dfd198d157aa081551eb0aa185c7568e6564f764c9f | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module.

Locators are `page:N` of the pinned `.jsonl` text, which is a chunk of about 3,000 characters and not a printed page. The pack's `_retrieval.json` is ignored by the launcher and is not relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied documents support all four requested analyses. Statements, debt notes, liquidity, covenant language and the August capital raise are located, so the work can proceed with bounded gaps. | Medium | No debt agreements, preferred terms or termination terms are supplied, and nothing after the August 2026 filings is included. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited FY2025 and unaudited June 2026 statements are both supplied, so a last-twelve-months view can be built from the filings. | Supports the financial base, with the interim period unaudited. | High |
| Debt agreements are not supplied; the filings name the facility covenants without levels and report compliance. | Facility covenant headroom cannot be verified. | High |
| The August 2026 preferred and warrant raise is described only in a subsequent-event note and a press release. | Pro forma capital structure rests on summary text. | Medium |
| One filing contradicts another on which covenants the Citibank servicing-rights facility has, and the press release headline differs from the note on the raise. | Both must be carried as unresolved conflicts. | Medium |

### Readiness view

The effective source set is sufficient to run the financial base, business and transaction, credit synthesis and evidence-trace work for UWM Holdings Corp on the consolidated perimeter, each with stated limitations. The set holds one annual report, three quarterly reports and three Exhibit 99.1 documents, all issuer-filed with located statements and notes. It does not include the senior note indentures, the servicing-rights facility agreements, the warehouse agreements, the Certificate of Designation and warrant terms for the August 2026 preferred stock, or any filing dated after the second quarter 2026 report. No consumer is conditional or blocked. Source sufficiency is not completion of downstream analysis.

### Readiness verdicts by consumer

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025, FY2024 and FY2023 statements (10-K `page:123` to `page:129`) and unaudited June 30, 2026 statements with comparatives (10-Q Q2 `page:2` to `page:5`) are located. Discrete quarters are in the Q2 release addendum (`page:8` to `page:12`). Text conversion flattens tables. |
| CP-1A | READY_WITH_LIMITATIONS | Business, Up-C structure, funding model, the terminated Two Harbors merger and the August 5, 2026 capital transaction are located. The underlying agreements are not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Debt, facility-level borrowings, maturities, covenant descriptions, liquidity and regulatory minimums are located. Covenant levels and executed agreements are not supplied. |
| CP-5 | READY_WITH_LIMITATIONS | Every source has page-level text locators. Chart and image content in the February 2026 presentation was not inspected. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source register

#### Form 10-K for FY2025 (`10-K_2025-12-31_uwmc-20251231.htm.jsonl`)

- Family and authority: filed annual report; original authority for audited consolidated statements and annual notes. Cover and `page:1`; Deloitte & Touche LLP opinion dated February 25, 2026 at `page:123` to `page:125` ("We have served as the Company's auditor since 2020").
- Statements: balance sheet at `page:126`, cash flows at `page:128`. Notes: Note 8 warehouse and other secured lines at `page:146`, Note 9 other borrowings at `page:149`, Note 10 commitments at `page:153`, Note 14 regulatory net worth at `page:157`, Note 21 subsequent events at `page:167`. Liquidity and Capital Resources starts at `page:99`.
- Perimeter: consolidated UWM Holdings Corporation in an Up-C structure with non-controlling interest held by SFS Corp. Units are thousands of USD.
- Transaction content: the Agreement and Plan of Merger with Two Harbors Investment Corp. dated December 17, 2025 is described at `page:140`; the merger was pending at the filing date (risk factor at `page:31`).
- Exhibit index at `page:169` to `page:175` lists the senior note indentures, the Revolving Credit Agreement, and the Citibank and Goldman Sachs facility agreements by reference. The documents themselves are not supplied.

#### Form 10-Q for the quarter ended September 30, 2025 (`10-Q_2025-09-30_uwmc-20250930.htm.jsonl`)

- Family and authority: filed interim report, unaudited. Controls the Q3 2025 and nine-month 2025 statements; the September 30, 2025 balance sheet is also shown in the Q2 2026 release addendum (`page:10`).
- Role: comparative history only. It is not needed to build the Q2 2026 last-twelve-months view, which uses FY2025 plus the six months of 2026 less the six months of 2025.

#### Form 10-Q for the quarter ended March 31, 2026 (`10-Q_2026-03-31_uwmc-20260331.htm.jsonl`)

- Family and authority: filed interim report, unaudited, for the three months ended March 31, 2026. Controls Q1 2026 statement facts.
- Terminated Two Harbors merger: the Adjusted EBITDA footnote (`page:37`) refers to "the fee associated with the termination of the merger agreement with Two Harbors received in the first quarter of 2026", and `page:42` repeats the termination fee. The date of termination and the amount of the fee are not stated in this filing.

#### Form 10-Q for the quarter ended June 30, 2026 (`10-Q_2026-06-30_uwmc-20260630.htm.jsonl`)

- Family and authority: filed interim report, unaudited, signed August 7, 2026 (`page:72`). Controls Q2 2026 and six-month 2026 statement facts. Cover (`page:1`): 342,349,795 Class A and 1,261,862,603 Class D shares outstanding as of August 4, 2026.
- Statements: balance sheet `page:2` to `page:3`, operations `page:3`, equity `page:4`, cash flows `page:4` to `page:5`.
- Debt: Note 6 warehouse and secured lines `page:14` to `page:16`; Note 7 senior notes and revolver `page:16` to `page:19`; MD&A facility discussion `page:49` to `page:57`.
- Other: Note 8 commitments `page:20` to `page:21`; Note 12 regulatory net worth `page:23`; Note 18 subsequent events `page:31` to `page:33`; legal proceedings `page:68` to `page:71`; Adjusted EBITDA reconciliation `page:38`.
- Units: thousands of USD in statements; the notes also state amounts in millions and billions.

#### Exhibit 99.1 press release, second quarter 2026 (`EX-99.1_2026-08-05_q22026ex-991pressrelease.htm.jsonl`)

- Family and authority: issuer press release dated August 5, 2026 ("PONTIAC, MI, August 5, 2026"); management-prepared and unaudited. It supports attributed management claims and non-GAAP presentations: Adjusted EBITDA, non-funding debt and the non-funding debt-to-equity ratio (`page:5` to `page:6`) and the "approximately $1.3 billion of available liquidity" claim (`page:1`).
- It repeats the 10-Q statements and adds a five-quarter balance sheet and operations addendum (`page:8` to `page:12`). The 10-Q controls statement facts; the release is not independent corroboration of them.
- It announces the dividend suspension "Subsequent to June 30, 2026" (`page:3`).

#### Exhibit 99.1 press release, first quarter 2026 (`EX-99.1_2026-05-06_q12026ex-991pressrelease.htm.jsonl`)

- Family and authority: issuer press release dated May 6, 2026, management-prepared and unaudited. Supports quarter-level management claims for Q1 2026 (`page:1`: "approximately $1.3 billion of available liquidity, reflecting $424.0 million of cash"). The Q1 2026 10-Q controls the statement facts.

#### Exhibit 99.1 earnings presentation, February 2026 (`EX-99.1_2026-02-26_irdeck4q25andfy2025-fina.htm.jsonl`)

- Family and authority: issuer presentation; management claims only. Text pages cover market position, strategy, the Two Harbors transaction (`page:7`) and an appendix with FY2022 to FY2025 Adjusted EBITDA and non-funding debt (`page:12`).
- Parse gap: the presentation is a slide deck. Only extracted text is available. Charts, images and speaker notes are not inspected, and some slide tables extract as unlabelled number runs (for example `page:5` and `page:8`). Chart content must not be cited as inspected.
- It treats the pending Two Harbors acquisition as on track for mid second quarter 2026 (`page:7`); the later filings supersede this.

### Information-availability boundary

- Latest supplied filing: the Q2 2026 10-Q signed August 7, 2026 and the press release of August 5, 2026. Both precede the as-of date and cutoff of 2026-11-05.
- Nothing dated between August 7, 2026 and 2026-11-05 is supplied. This includes any Form 8-K for the August 5, 2026 transaction, any rights offering prospectus, and any third quarter 2026 report. These are Not supplied, not absent.
- The Q2 10-Q (`page:33`) schedules a $400 million rights offering with a record date of October 2, 2026, expected commencement on October 5, 2026 and expiry on November 12, 2026. Expiry is after the cutoff. Whether it launched and its result are Not supplied. The note says it would proceed "if needed".

### Identity and perimeter

- Registrant: UWM Holdings Corporation, Delaware, Commission file number 001-39189 (Q2 10-Q `page:1`). The context leaves borrower, parent, guarantor and sponsor fields blank; that is not evidence of their absence.
- Structure (Q2 10-Q `page:6`): UWMC's only material direct asset is the Class A Common Units of UWM Holdings, LLC ("Holdings LLC"), which owns 100% of United Wholesale Mortgage, LLC ("UWM"), the operating subsidiary. SFS Holding Corp. ("SFS Corp.") holds Class B units and Class D shares. Ownership of Holdings LLC at June 30, 2026 was 21.3% UWMC and 78.7% SFS Corp. (`page:23`).
- Debt roles: the 2027 and 2029 senior notes were issued by UWM; the 2030 and 2031 senior notes were issued by Holdings LLC and are guaranteed by UWM (`page:17` to `page:18`). The servicing-rights facilities are with UWM as borrower. The $500.0 million Revolving Credit Facility has UWM as borrower and SFS Corp. as lender (`page:19`). Guarantor lists beyond UWM and restricted-group definitions are not supplied.
- The consolidated statements effectively represent Holdings LLC and its subsidiaries (Note 10, `page:22`). No separate issuer-level or restricted-group financial statements are supplied.
- The company reports one operating segment (`page:7`).
- Reporting basis: US GAAP, USD, thousands in the statements; unaudited for interim periods.

### Document relationships and duplicates

- December 31, 2025 balance sheet data appear in the 10-K, the Q1 and Q2 2026 10-Qs and the releases. The 10-K controls them; the later copies are retained as comparatives and the releases are not independent corroboration.
- Q1 2026 data appear in the Q1 10-Q, the Q1 release and the Q2 release addendum. The Q1 10-Q controls.
- Q2 2026 data appear in the Q2 10-Q and Q2 release. The 10-Q controls.
- Nothing is a draft. All filings are final filed documents. No amendment, waiver or supplement to any debt agreement is supplied; the Revolving Credit Agreement Amendment No. 1 of September 2025 is described in the notes (`page:19`) but not supplied.

### Document conflicts

| Conflict | Locators | Downstream effect |
| --- | --- | --- |
| The Note 6 text lists "maximum debt to net worth ratio" among the Conventional (Citibank) servicing-rights facility covenants; the MD&A description of the same facility lists minimum tangible net worth, minimum liquidity and net income only. | Q2 10-Q `page:16` and `page:55` (Ginnie Mae facility) against `page:54` (Conventional facility) | CP-2 must not state the Conventional facility's covenant set as settled; the agreement is not supplied. |
| The Q2 release headline announces "a $2.05 Billion Equity Investment"; the 10-Q describes $1.65 billion of gross preferred proceeds that closed on August 5, 2026 plus a separate $400 million rights offering that proceeds "if needed". | Q2 release `page:1`; Q2 10-Q `page:32` to `page:33` | CP-1A and CP-2 must use the filing's split and treat the rights offering as contingent. |

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, discrete quarters, debt, cash paid for interest and taxes, non-GAAP | 10-K `page:123` to `page:129`, `page:149` to `page:153`; Q2 10-Q `page:2` to `page:5`, `page:16` to `page:19`, `page:38`; Q2 release `page:5` to `page:12` | Interim figures unaudited; text conversion flattens tables; Adjusted EBITDA is a company-defined non-GAAP measure; no Q3 2026 report |
| CP-1A | Business model, Up-C, history, ownership, transactions | 10-K `page:7`, `page:140`; Q2 10-Q `page:6`, `page:22` to `page:23`, `page:31` to `page:35`, `page:68` to `page:71` | Two Harbors termination date and fee, preferred terms, warrants and investor rights agreement not supplied |
| CP-2 | CP-1 and CP-1A outputs, facility-level debt, covenants, maturities, liquidity, regulatory capital | Q2 10-Q `page:14` to `page:19`, `page:23`, `page:49` to `page:60`; Q2 release `page:1`, `page:5` to `page:6` | Covenant levels, advance rates and executed agreements not supplied; no ratings in the context |
| CP-5 | Traceable claims with locators | All seven sources carry page locators | Deck charts and images not inspected; locators are text chunks, not printed pages |

### Analytical read-through

- Usable coverage: the 10-K and the three quarterly reports give audited annual and unaudited quarterly statements through June 30, 2026, with the debt notes, a facility-by-facility warehouse table (`page:14`), a senior note table (`page:17`), a liquidity discussion (`page:48` to `page:60`) and a subsequent-event note (`page:31` to `page:33`). The Q2 release addendum adds five quarters of balance sheet and operations (`page:8` to `page:12`).
- Strongest contrary evidence: the subsequent-event note says the August 5, 2026 raise "closed subsequent to June 30, 2026" and that "the effects of the transaction have not been reflected" in the statements (`page:33`). The June 30, 2026 balance sheet therefore shows no preferred stock outstanding (`page:2`), although preferred stock was issued five weeks later. A consumer that reads only that balance sheet misses the raise; one that adds it must rely on note text.
- Source risk mechanism: the filings name the maintenance covenants of the warehouse and servicing-rights facilities (minimum tangible net worth, minimum liquidity, maximum debt to net worth, net income) but print no levels (`page:15`, `page:52`, `page:54`). The senior note incurrence thresholds are printed (Fixed Charge Coverage Ratio of at least 3.0 to 1.0 or Debt-to-Equity Ratio not above 2.0 to 1.0, `page:54`), as are the most restrictive agency minimums (net worth of $743.6 million, liquidity of $343.9 million, `page:23`). For the facility covenants, compliance statements are the only evidence of headroom, and the MD&A and the note differ on one facility's covenant set. Downstream, CP-2 can report that the tests exist and were stated as met, but cannot compute facility covenant headroom.
- What cannot proceed: covenant headroom against executed definitions; the pro forma capital structure after the preferred issuance beyond the note's summary terms; the outcome of the rights offering; any analysis of events after August 7, 2026.
- Next evidence action: supply the Form 8-K and exhibits for the August 5, 2026 transaction (Certificate of Designation, warrants, investor rights agreement), the Two Harbors termination agreement or 8-K, the four senior note indentures, the Citibank, Goldman Sachs and SFS Corp. facility agreements and amendments, any rights offering documents, and any Form 10-Q or 8-K filed after August 7, 2026.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Page counts in `## Sources` are the number of text chunks in each pinned file.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Certificate of Designation, warrant terms and investor rights agreement for the August 5, 2026 preferred stock are not supplied; only the Note 18 summary is | High | CP-1A, CP-2 | Supply the 8-K and exhibits for the transaction |
| Executed senior note indentures, servicing-rights facility agreements, Revolving Credit Agreement and warehouse agreements are not supplied; covenant levels, definitions and cross-default terms cannot be verified | High | CP-2, CP-5 | Supply the agreements listed in the 10-K exhibit index (`page:170` to `page:174`) |
| Events between August 7, 2026 and 2026-11-05 are not supplied, including rights offering launch and any third quarter 2026 report | Medium | CP-1, CP-1A, CP-2 | Supply later 8-Ks, prospectus supplements and the third quarter 2026 report if filed |
| Two Harbors merger termination date, terms and fee amount are not stated in the supplied text | Medium | CP-1A, CP-2 | Supply the termination 8-K or agreement |
| Conflict on the Conventional servicing-rights facility covenant set (Note 6 against MD&A) | Medium | CP-2, CP-5 | Supply the Citibank agreement |
| Press release headline of $2.05 billion against the filing's $1.65 billion closed plus $400 million contingent | Medium | CP-1A, CP-2 | Use the filing's split; supply the rights offering documents |
| No ratings, market quotes or valuation inputs in the context or sources | Low | CP-2 | Supply if a ratings or relative-value view is later requested |
| February 2026 presentation charts and images not inspected; text extraction only | Low | CP-5 | Supply or inspect the slide images if chart claims are needed |
| Text conversion flattens tables; no XBRL data or original filing layout supplied | Low | CP-1, CP-5 | Check amounts against the filed HTML where a table is ambiguous |
| No standalone UWM, LLC or Holdings LLC statements; consolidated perimeter only | Low | CP-1, CP-2 | Rely on consolidated statements, which Note 10 says effectively represent Holdings LLC |

## Next module

CP-1, then CP-1A, CP-2 and CP-5 in the order the dependency planner sets. Carry forward: the consolidated perimeter and Up-C structure, the unaudited status of 2026 interim figures, the closed-after-period August 5, 2026 transaction that the statements do not reflect, the two conflicts above, and the absence of executed debt agreements and of any filing after August 7, 2026.
