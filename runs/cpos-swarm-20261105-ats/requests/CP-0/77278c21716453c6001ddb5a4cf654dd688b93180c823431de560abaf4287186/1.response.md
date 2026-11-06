## Request

Issuer: ATS Corp /ATS (ATS Corporation, TSX and NYSE ticker ATS; identity ats, SEC central index key 1394832). As-of date: 2026-11-05, which is also the evidence cutoff. Pathway: credit_snapshot with the minimum module set, so this source-readiness review serves the financial base, business and transaction context, fundamental credit synthesis and evidence-trace modules that follow it. Reporting currency: Canadian dollars. Requested periods: current period Q2 FY2027 (quarter ended September 27, 2026) and prior period FY2026 (year ended March 31, 2026), as named in the run context.

This module answers one question: can the pinned source set support the requested work, and what remains blocked. It gives no credit conclusion, legal interpretation or investment opinion, and it does not normalize, reconcile or calculate any figure.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Document family |
| --- | --- | --- |
| 40-F_2026-03-31_ats-20260331_d2.htm.jsonl | 461a9e1a5795ad26589158b15641a8ecb65a515f78e81e620080a11c1ee51f03 | Annual report cover document on Form 40-F, fiscal year ended March 31, 2026 |
| 6-K-EX-99.1_2025-12-28_ats-mdaxfy26q3.htm.jsonl | 495104fe5a368c3f86fa5f222fb1d1be8a8ff26e6c4af4a09766387bac60f769 | Management's discussion and analysis, Q3 FY2026 (quarter ended December 28, 2025) |
| 6-K-EX-99.1_2026-03-31_ats-pressreleasexfy26q4.htm.jsonl | 9c0afcbd3db8908a2bce9809ae30cf6e21e3c8555f5c3d8e1a44911b7a679728 | Earnings release, Q4 and FY2026 (year ended March 31, 2026) |
| 6-K-EX-99.1_2026-06-28_ats-mdaxfy27q1.htm.jsonl | 7139467d52f7afd7dcfcd7f72f26d02042ad1d04d4e987664edd2eeedb7dac8a | Management's discussion and analysis, Q1 FY2027 (quarter ended June 28, 2026) |
| 6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl | 927254e506c477f0f3c479b731264614078302a7152fb02abbd056d0f3cf2206 | Management's discussion and analysis, Q2 FY2027 (quarter ended September 27, 2026) |
| 6-K-EX-99.5_2026-06-28_ats-pressreleasexfy27q1.htm.jsonl | bd6442bf8c1097adcf56b29d660c89aa138c0b9c5262ef32298dfe327594d94e | Earnings release, Q1 FY2027 |
| 6-K-EX-99.5_2026-09-27_ats-pressreleasexfy27q2.htm.jsonl | 678b14cb1aaa7e6f176b56c413e4c96ec51b564dcfbf0025fed22fc9c315392b | Earnings release, Q2 FY2027 |

### Run context (settings, not issuer evidence)

| Source (exact name) | sha256 | Use |
| --- | --- | --- |
| context (1394832-ats-corp-ats-ats.json) | 657290ce48739d0b0b92feb39cafad5f5190fec8cfc7776e258254d4e8b4159c | Dated run settings: as-of and cutoff 2026-11-05, current period q2-2027, prior period fy-2026, reporting currency CAD. It leaves borrower, parent, guarantors, sponsor, deal terms, quotes and ratings blank; blank is not zero. |

### Supplied handoffs

None. This is the first module of the run, so CP-OS supplied no upstream handoff. The retrieval file `_retrieval.json` in the pack folder is ignored by the launcher and is not a pinned source.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The pack can support a financial, business and credit read of ATS through the latest quarter, with limitations. Quarterly disclosure is detailed; audited annual statements, debt notes and covenant terms are not included. | Medium | Annual report exhibits and financing documents are missing, so covenant levels, debt carrying values by instrument and audited annual notes cannot be sourced from this pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Reporting is in Canadian dollars, and the periods needed are covered: the latest quarter ended in September 2026 and the prior year ended in March 2026. | Currency and period labels are clear, which lowers the risk of mixing bases. | High |
| Debt, liquidity and covenant compliance are described each quarter, but covenant thresholds and debt carrying values by instrument are not printed. | Covenant headroom cannot be tested against actual limits from this pack. | Medium |
| Management reports a material weakness in internal control, and its disclosure controls were not effective at the latest quarter end. | Reported figures carry extra reliability risk until remediation is shown. | High |
| The annual report is a cover document only; the annual discussion and analysis, audited statements and annual information form are not in the pack. | Fiscal 2026 figures rest on the year-end news release, not on audited filings. | High |

### Readiness view

The effective source set is sufficient for the requested work, with bounded limitations, and no source is blocked. The seven issuer files are all text-extractable, share one reporting entity and one reporting currency, and between them cover the latest quarter, the three quarters before it and the prior fiscal year. The quarterly discussion and analysis documents and the two latest earnings releases carry the debt, liquidity, cash-flow, reconciliation and business narrative that the financial base, business context, credit synthesis and evidence-trace modules need. The principal weaknesses are structural rather than fatal. The annual report in the pack is only the Form 40-F cover document, so the audited fiscal 2026 statements, the annual discussion and analysis and the annual information form are named but absent. No credit agreement, note indenture or other executed financing document is supplied, so covenant levels, definitions and baskets can be read only as management describes them. The interim statements in the releases are primary statements without notes. Management states that disclosure controls were not effective because of a material weakness, which bounds how much weight any single reported figure can carry. Each limitation is carried into the consumer assessments below and into the gaps. Source sufficiency here is separate from completion of downstream analysis.

### Source-by-source assessment

| Source | Document family and original authority | Entity and perimeter | Period and basis | Version relationships and limits |
| --- | --- | --- | --- | --- |
| 40-F cover document | Form 40-F filed by the registrant; a filed regulatory document, but only the cover and incorporation-by-reference text | ATS Corporation, Ontario, Canada, the registrant and issuer of all debt described in the later sources | Fiscal year ended March 31, 2026; IFRS; Canadian dollars | Names the annual information form, annual discussion and analysis and audited statements as separate exhibits that are not in the pack. Nothing supersedes anything here. |
| Q3 FY2026 MD&A | Management's discussion and analysis furnished on Form 6-K; management narrative with filed status, not audited | ATS Corporation consolidated | Three and nine months ended December 28, 2025; interim, IFRS; Canadian dollars | No earnings release or statements for this quarter are in the pack, so this is the only source for Q3 FY2026 and its comparatives. |
| Q4 FY2026 earnings release | Earnings release furnished on Form 6-K; attributed management narrative plus primary statements | ATS Corporation consolidated | Three and twelve months ended March 31, 2026; Canadian dollars | Sole in-pack source for fiscal 2026 full-year statements and the March 31, 2026 balance sheet. No audit status is shown in the release itself. No facility-level debt text. |
| Q1 FY2027 MD&A | Management's discussion and analysis furnished on Form 6-K | ATS Corporation consolidated | Three months ended June 28, 2026; interim, IFRS; Canadian dollars | Same quarter as the Q1 FY2027 release; the two are retained as separate sources, with neither replacing the other. |
| Q1 FY2027 earnings release | Earnings release furnished on Form 6-K; primary condensed statements without notes | ATS Corporation consolidated | Three months ended June 28, 2026; statements labelled unaudited; Canadian dollars | Announces the Fixed Cost Transformation Program; carries cash interest and cash tax paid. |
| Q2 FY2027 MD&A | Management's discussion and analysis furnished on Form 6-K, dated November 4, 2026 | ATS Corporation consolidated | Three and six months ended September 27, 2026; interim, IFRS; Canadian dollars | Latest period and the controlling source for current liquidity, debt and covenant statements. Its leverage statement differs from the Q1 FY2027 statement (see conflicts). |
| Q2 FY2027 earnings release | Earnings release furnished on Form 6-K; primary condensed statements without notes | ATS Corporation consolidated | Three and six months ended September 27, 2026; unaudited; Canadian dollars | Same quarter as the Q2 FY2027 MD&A and largely overlapping; retained as the source for full primary statements, cash interest and cash tax paid. |

No source identifies an issuer, co-issuer, borrower, parent or guarantor by legal name other than ATS Corporation. Guarantors of the notes and the credit facility are described only by class, and no restricted or unrestricted subsidiary distinction is stated. These remain gaps.

### Authority and perimeter evidence

The registrant and its fiscal year are fixed by the cover document: [40-F_2026-03-31_ats-20260331_d2.htm.jsonl, page:1] "For the fiscal year ended March 31, 2026 Commission File Number 001-41713" and [40-F_2026-03-31_ats-20260331_d2.htm.jsonl, page:1] "ATS CORPORATION (Exact name of Registrant as specified in its charter)". The currency basis is stated at [40-F_2026-03-31_ats-20260331_d2.htm.jsonl, page:6] "Unless otherwise indicated, all dollar amounts in this Annual Report are in Canadian dollars." The accounting basis is stated at [40-F_2026-03-31_ats-20260331_d2.htm.jsonl, page:6] "in accordance with International Financial Reporting Standards as issued by".

The cover document lists exhibits that are not part of the pack: [40-F_2026-03-31_ats-20260331_d2.htm.jsonl, page:8] "99.2 Management Discussion and Analysis for the year ended March 31, 2026" and [40-F_2026-03-31_ats-20260331_d2.htm.jsonl, page:8] "99.3 Audited consolidated Financial Statements for the year ended March 31, 2026". The annual information form is listed as exhibit 99.1 on the same page. The retrieval record for the pack itself flagged that interim results are furnished on Form 6-K rather than 10-Q and that releases stand in for presentations.

The latest MD&A fixes the current period and its date: [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:1] "for the three and six months ended September 27, 2026" and [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:1] "is as of November 4, 2026". This is before the cutoff of 2026-11-05. No source in the pack is dated after the cutoff.

### Consumer readiness

| Consumer | Status | Evidence located | Limitation carried |
| --- | --- | --- | --- |
| Financial base (CP-1) | READY_WITH_LIMITATIONS | Quarterly statements and reconciliations for Q1 and Q2 FY2027, full-year FY2026 statements, a quarterly results table, net debt reconciliations, cash flow summaries, credit facility and notes text, contractual obligations table | No audited annual statements or notes; no debt note with carrying values by instrument; no covenant thresholds; Q3 FY2026 statements absent, only MD&A tables; material weakness in internal control |
| Business and transaction context (CP-1A) | READY_WITH_LIMITATIONS | Company profile, strategy, end-market narrative, order bookings and backlog by market, reorganization and Fixed Cost Transformation Program, leadership changes, post-quarter facility sales, tariff discussion | Annual information form absent, so ownership, customer concentration and legal structure rest on MD&A text only; no named guarantor or subsidiary list; sponsor, parent and borrower fields are blank in the context |
| Credit synthesis (CP-2) | READY_WITH_LIMITATIONS | Evidence is upstream handoffs only; the pack gives the underlying facts for both the business and financial registers | Inherits every limitation above; no ratings, quotes or deal terms in the context |
| Evidence-trace validation (CP-5) | READY_WITH_LIMITATIONS | Seven text sources with stable page locators allow quote matching | Chart images and tables flattened to text; matching depends on exact extracted wording |

All four consumers remain runnable. The command sheet marks none as DO NOT RUN, because no consumer is missing a source that prevents its workflow and no preparation is blocked. A missing downstream handoff is not a source-readiness condition.

### Coverage by evidence area

This assessment is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. It does not assert normalized quarters, reconciliation or acceptance of any downstream input.

| Evidence area | Located in the pack | Status |
| --- | --- | --- |
| Discrete quarters | Q3 FY2026 and Q4 FY2026 through the Q3 MD&A and Q4 release; Q1 FY2027 and Q2 FY2027 through MD&A and releases; the consolidated quarterly results table at [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:31] lists the eight latest quarters | Located with limits: no Q3 FY2026 statements |
| Fiscal years | FY2026 and FY2025 in the Q4 release statements and reconciliations | Located; no audited statements or notes |
| Quarter versus year-to-date | Three-month and year-to-date columns in the Q2 FY2027 sources, nine-month in Q3 FY2026, twelve-month in the Q4 release | Located; labels must be kept apart |
| Segments and markets | Revenue, bookings and backlog by market (life sciences, industrial and consumer, food and beverage, energy) and revenue by type in the releases and by customer location in the Q4 release | Located by market; no statutory segment note |
| Add-backs and adjusted measures | Reconciliations of adjusted revenues, adjusted EBITDA, adjusted earnings from operations, free cash flow and net debt in every quarterly source | Located; company-defined non-IFRS measures |
| Key performance indicators | Order bookings, order backlog, non-cash working capital ratio, net debt to pro forma adjusted EBITDA | Located; supplementary or non-IFRS measures |
| Facility-level debt | Principal, rate and maturity by instrument in MD&A text; contractual obligations table at [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:28] | Partly located; carrying values by facility and fair values absent |
| Cash-paid interest and tax | Supplemental lines in the Q4, Q1 and Q2 releases | Located for those periods; absent for Q3 FY2026 |
| Business and transaction narrative | MD&A executive update, strategy, outlook and reorganization sections | Located |
| Legal and financing documents | None supplied; the context sets legal documents to none | Not supplied |
| Ratings, quotes, peers | None in the context | Not supplied |

### Evidence for the key readiness points

Statements in the releases are condensed and unaudited at interim dates: [6-K-EX-99.5_2026-09-27_ats-pressreleasexfy27q2.htm.jsonl, page:19] "Interim Condensed Consolidated Statements of Financial Position (in thousands of Canadian dollars - unaudited)". Notes are not reproduced: [6-K-EX-99.5_2026-09-27_ats-pressreleasexfy27q2.htm.jsonl, page:20] "Please refer to complete Interim Condensed Consolidated Financial Statements for supplemental notes". The year-end release has the same limit: [6-K-EX-99.1_2026-03-31_ats-pressreleasexfy26q4.htm.jsonl, page:16] "Consolidated Statements of Financial Position (in thousands of Canadian dollars)".

Credit facility and notes are described in MD&A text. The facility consists of [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:26] "a fully drawn $150.0 million secured term credit facility" alongside a revolving line, with [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:26] "$966.7 million of unutilized multipurpose credit, including letters of credit" reported at the latest quarter end. Covenants are named but not quantified: [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:27] "financial covenants including a net debt-to-EBITDA test and an interest coverage test" and [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:27] "At September 27, 2026, all of the covenants were met." No threshold, definition or reported covenant ratio is printed in any source, and the credit agreement is not supplied, so compliance is a management assertion that cannot be tested here. The company-defined leverage ratio is shown as [6-K-EX-99.5_2026-09-27_ats-pressreleasexfy27q2.htm.jsonl, page:17] "Net Debt to Pro Forma Adjusted EBITDA 3.1x 2.8x"; whether it matches the credit agreement definition is not shown.

The two note series carry their maturities in text: [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:27] "mature on December 15, 2028" for the U.S. dollar notes and [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:28] "mature on August 21, 2032" for the Canadian dollar notes. Instrument amounts are in the MD&A narrative and the contractual obligations table, which shows principal and interest combined, so principal-only maturity walls need a downstream calculation with stated limits.

Letters of credit outside the credit facility are disclosed: [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:29] "the total value of outstanding letters of credit was approximately $274.4 million". Their split among facilities needs the figures at [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:26] and the additional letter of credit facilities, which is a downstream task.

Control environment: [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:37] "disclosure controls and procedures were not effective as of September 27, 2026, due to the material weakness". The Q3 FY2026 text speaks of weaknesses in the plural: [6-K-EX-99.1_2025-12-28_ats-mdaxfy26q3.htm.jsonl, page:31] "address the identified material weaknesses". The later sources use the singular, and the annual MD&A that would explain the change is not in the pack.

Subsequent event inside the cutoff: [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:13] "Subsequent to quarter end, the Company completed the sale of the two U.S. facilities for consideration of $71.2 million". Its accounting is described as falling in the following quarter, so no statements in the pack reflect it.

### Conflicts and superseded statements

| Item | Earlier locator | Later locator | Downstream effect |
| --- | --- | --- | --- |
| Leverage versus target range | [6-K-EX-99.5_2026-06-28_ats-pressreleasexfy27q1.htm.jsonl, page:6] "management expects the Company to continue to operate within its targeted leverage ratio of 2.0 to 3.0 times throughout fiscal 2027" | [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:6] "slightly above the targeted range of 2.0 to 3.0 times" | A later management update, not a document conflict. Use the Q2 FY2027 statement for the current view and carry the Q1 FY2027 statement as the earlier expectation. Both stay as separate sources; the later one does not delete the earlier. |

No conflicting figure was found between the overlapping Q2 FY2027 MD&A and release in the areas read, but no systematic cross-check was done in this module, and none is claimed.

### Extraction fidelity and parse gaps

Text extraction succeeded for all seven files; extraction success is not a fidelity review. Tables arrive as flattened text lines, so column alignment must be confirmed against the header lines on the same page. Charts and images are not retained: the Q2 FY2027 MD&A shows the heading [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:6] "ORDER BOOKINGS BY QUARTER" with no chart data after it. The quarterly series that the chart presumably depicts is available as text in the results table at [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:31], so the gap is bounded, but no image inspection is claimed. There are no workbooks, scans or slide decks in the pack, and no speaker notes.

Page coverage by source (chunks of extracted text): 9, 42, 29, 45, 51, 30 and 34 pages for the seven files, totalling 240 pages. All pages were searched by term for debt, liquidity, covenant, rating, subsequent-event, control and statement content; the pages cited above were read in full. This is a search-based review, and a page-by-page reading of every narrative page is left to the modules that need them.

## Calculations

No new calculation was performed. This module does not normalize, reconcile or derive figures, and every figure above is quoted verbatim from a cited span. The only arithmetic is the page count: 9 + 42 + 29 + 45 + 51 + 30 + 34 = 240 pages across seven issuer files (inputs from the page index of each pinned source).

Calculations deferred to later modules, with their inputs located: liquidity (cash at [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:24] "Cash and cash equivalents $ 231.0 $ 285.0", facility availability at [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:26]), maturity wall (contractual obligations at [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:28]), and leverage (net debt reconciliation at [6-K-EX-99.1_2026-09-27_ats-mdaxfy27q2.htm.jsonl, page:34]). Principal and interest are combined in the obligations table, and some facilities are in foreign currencies, so those calculations need explicit conversion and perimeter notes.

## Gaps

| ID | Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| G1 | Audited FY2026 annual MD&A, financial statements with notes and annual information form are named in the cover document but not in the pack | High | Financial base, business context, credit synthesis | Add exhibits 99.1 to 99.3 of the annual report; until then use the Q4 release and label the audit status as not shown in-pack |
| G2 | Credit agreement, note indentures and any amendments not supplied; covenant levels, definitions, step-downs and baskets unavailable | High | Financial base, credit synthesis | Add the executed documents; until then state covenants as management describes them and make no headroom claim |
| G3 | Debt note with carrying value, fair value and currency by instrument absent; only narrative principal, rate and maturity | Medium | Financial base | Add the audited or interim notes on borrowings |
| G4 | Interim condensed statements are reproduced without notes in the releases; Q3 FY2026 has no statements, only MD&A tables | Medium | Financial base | Add the interim statements with notes for each quarter |
| G5 | Material weakness in internal control over financial reporting and ineffective disclosure controls at the latest quarter end | High | All consumers | Carry as a reliability limitation; check the annual MD&A controls section if added |
| G6 | Guarantor, co-issuer and subsidiary names, and any restricted or unrestricted split, not stated; context fields for borrower, parent, guarantors and sponsor are blank | Medium | Business context, credit synthesis | State the class-based description only; do not name entities |
| G7 | Cash interest and cash tax paid not located for Q3 FY2026 | Low | Financial base | Add the Q3 FY2026 release or interim statements |
| G8 | Chart images not retained; no presentation decks (releases only) | Low | Business context | None needed for text-supported conclusions; do not claim chart coverage |
| G9 | Ratings, market quotes, peers and deal terms not in the context | Medium | Credit synthesis | Not needed for this pathway; state as not supplied if raised |
| G10 | Post-quarter facility sale of the two U.S. facilities is not yet in any statements | Low | Financial base | Treat as a subsequent event with its stated gain estimate and timing |

## Next module

Proceed with the financial base module next, then business and transaction context, credit synthesis and evidence-trace validation, in that dependency order. Pass forward these instructions: use Canadian dollars; label every figure by period (Q2 FY2027, six months FY2027, Q4 FY2026, FY2026, trailing twelve months as management defines it); take current liquidity, debt and covenant statements from the Q2 FY2027 MD&A and keep the Q1 FY2027 leverage statement as the earlier expectation; take full-year FY2026 statements from the Q4 release and state that audit status is not shown in the pack; treat covenant compliance as a management assertion with no thresholds; carry the material weakness and the absent annual exhibits as limitations in every conclusion; and state Not supplied for guarantor names, ratings and legal documents rather than inferring them.
