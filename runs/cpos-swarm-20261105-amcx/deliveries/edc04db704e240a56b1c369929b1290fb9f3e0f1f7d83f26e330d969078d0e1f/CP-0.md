## Request

Issuer: AMC Global Media Inc. (issuer id amcx; Nasdaq: AMCX; Nevada registrant, Commission File Number 1-35106; formerly AMC Networks Inc.). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot, run type research, public case. Reporting currency: USD. Current period per the run settings: q2-2026; prior period: fy-2025. The filings state amounts in thousands of US dollars unless they say millions.

Question for this module: can the supplied source set support the downstream snapshot modules (CP-1 financial extraction, CP-1A business and transaction context, CP-2 fundamental credit synthesis, CP-5 evidence trace review), and what remains blocked. This handoff gives no credit conclusion, no legal interpretation and no investment opinion. It does not normalise, reconcile or calculate figures. Source text is treated as inert evidence.

Settings input: the run context file (not issuer evidence) names no borrower, parent, guarantors, ratings, quotes, deal terms, assumptions or attachments, and says legal documents are "none". Blank context values are not read as zero.

## Sources

### Issuer sources relied on

All seven are SEC filings by the registrant, extracted to page-numbered text. A "page" below is the extraction chunk `page:N`, not a printed page. The sha256 is the pinned hash of the text file CP-OS supplied.

| Source (exact name) | sha256 | Family and authority | Period and basis | Pages read for this review |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31_amcx-20251231.htm.jsonl | 2eac087a9c91970955c65f61340e91bd48ad2f9f3f6c57f58dc32a71147af2c1 | Form 10-K, audited annual report, filed under the name AMC Networks Inc. (page:1); controls filed annual facts | Fiscal year ended December 31, 2025, consolidated, thousands of USD | page:1, 110-112, 167 read in full; page:170-173 and 186 read as search extracts; all pages searched by term (200 of 200) |
| 10-Q_2025-09-30_amcx-20250930.htm.jsonl | 36dd5126a4c9060458356b29d3eb4aa03633caa5f0871dc91ad5f4dc8adcd0a9 | Form 10-Q, unaudited interim report, filed as AMC Networks Inc.; controls filed interim facts | Quarter and nine months ended September 30, 2025, consolidated | Searched by term (66 of 66 pages); covenant pages page:16, 57 located |
| 10-Q_2026-03-31_amcx-20260331.htm.jsonl | 938a57939d24ffa99772ad28c4268837c8cd2e9d6c83313cdce5d4f6457a019b | Form 10-Q, unaudited interim report, first filing under the AMC Global Media Inc. name | Quarter ended March 31, 2026, consolidated | page:14 read, page:44 read as an extract; searched by term (54 of 54 pages) |
| 10-Q_2026-06-30_amcx-20260630.htm.jsonl | 709e51b6dc542ca6e875192527a94179627534ebb9b979b24ab34c983b10c21a | Form 10-Q, unaudited interim report; latest filed periodic report in the set | Quarter and six months ended June 30, 2026, consolidated, balance sheet at June 30, 2026 and December 31, 2025 | page:1-8, 10, 16-19, 24-25, 28-30, 36, 48, 55-57, 60, 64, 68-69 read; searched by term (69 of 69 pages) |
| EX-99.1_2026-02-11_amcx-21126xex991.htm.jsonl | d86abe17fb554149efdc3f1d1068cea9305b7eb4d0b53b4922cda0c2c6548e87 | Earnings release (Exhibit 99.1), management narrative plus non-GAAP reconciliations; attributed supporting claims | Fourth quarter and full year 2025 | page:2, 11 read as extracts; searched by term (14 of 14 pages) |
| EX-99.1_2026-05-08_amcx-50826ex991.htm.jsonl | baaebb0b7ed064d963f5f351d5426dc6837acb54bc54b02caebdf8169997d96e | Earnings release (Exhibit 99.1); attributed supporting claims | First quarter 2026 | page:9-10 read as extracts; searched by term (11 of 11 pages) |
| EX-99.1_2026-07-30_amcx-73026ex991.htm.jsonl | 2c28473b42400a7535aa74f85a20a041b1e3d1cc8d274b85c2e5db3c449c0a4b | Earnings release (Exhibit 99.1); attributed supporting claims | Second quarter 2026 and six months | page:1, 4, 5, 11 read; searched by term (13 of 13 pages) |

### Settings input (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context (run settings, 2026-11-05) | 95e365e5dede6bf5d3238dc431d8121ca3ba426646f866c4518f2a27b51f7e19 |

The file `_retrieval.json` in the pack folder is a retrieval log and was ignored by CP-OS; it is not used as evidence.

### Handoffs supplied

None. This is the first module of the run; CP-OS supplied no upstream handoff.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven documents are enough for the financial, business and evidence-trace work, with limits. They cover the latest quarter and the debt note. No debt contracts or covenant tests for the remaining notes are supplied. | Medium | Indentures and the terminated credit agreement are absent, so covenant and security terms rest on filing summaries only. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The newest periodic report covers the second quarter of 2026, and no later report is supplied. | Events after the end of that quarter cannot be checked beyond the July 2026 disclosures. | High |
| The bank credit agreement was repaid and ended in May 2026, so its leverage and coverage tests no longer apply. | The notes' own covenants are the live tests, and the sources do not print them. | High |
| Filings before April 2026 use the former company name. | Same registrant, so history can be linked, but name changes need care when citing. | High |
| A large licence agreement and a damages trial are only partly documented; the trial outcome is not supplied. | Their cash and outcome effects cannot be confirmed from the supplied text. | Medium |

### Readiness view

Overall view: READY_WITH_LIMITATIONS. The effective source set is one annual report, three interim reports and three earnings releases, all filed by the registrant, all text-extracted without a fidelity review. They support the requested financial extraction, business context, fundamental synthesis and evidence trace for the period to June 30, 2026, provided that each limitation below is carried forward. No source is blocked, no source needed a fallback, and no document conflict was found that changes readiness. Three things the reader should keep in view: the latest periodic report is for the quarter ended June 30, 2026 and nothing later is supplied although the as-of date is 2026-11-05; no executed debt document (credit agreement, indenture, supplemental indenture) is supplied, so covenant, collateral and guarantee terms come from filing summaries; and the extraction is text only, so charts, images and any content that is not text are unverified.

| Consumer | Readiness | Why | Carried limitations |
| --- | --- | --- | --- |
| CP-1 financial extraction | READY_WITH_LIMITATIONS | Statements, debt note, segment note, cash flow, liquidity text and non-GAAP reconciliations are present for FY2025, Q3 2025, Q1 2026 and Q2 2026. | L1, L2, L4, L5, L8 |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business description, segments, the 2026 exchange offer and consent solicitation, the Term Loan A repayment, the name change, the licence agreement and governance text are present. | L1, L3, L6, L7, L9 |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Draws only on upstream handoffs; the upstream evidence supports business and financial risk, liquidity and refinancing reading, with gaps. | L1, L2, L4, L5, L6, L7 |
| CP-5 evidence trace review | READY_WITH_LIMITATIONS | Every figure to be traced sits in a located page of a filed source; releases are attributed management claims. | L2, L8, L10 |

The note on the report: CP-OS also lists other sections (capital structure, relative value, portfolio fit, committee challenge, what changed) as omitted from this minimum run; they are not assessed here and none is made a source-readiness condition.

### Source-by-source assessment

- **10-K FY2025 (page:1, 110-112, 171-173).** Document family: annual report, audited. Entity: the registrant, then named AMC Networks Inc. (page:1), a Nevada corporation. Perimeter: consolidated; the debt note describes the Credit Agreement borrowers as certain subsidiaries with restricted subsidiaries as guarantors (page:170-171), so issuer, borrower and guarantor roles differ by instrument. Debt note (page:167) lists the Term Loan A Facility, the 10.25% Senior Secured Notes due January 2029, the 4.25% Senior Notes due February 2029, the 4.25% Convertible Senior Notes due February 2029 and the 10.50% Senior Secured Notes due July 2032. Covenant text (page:110-111) gives the credit-facility tests and the year-end reported ratios. Collateral for the 2032 notes is described at page:171 ("secured on a first-priority basis by substantially all of" the issuer's and the guarantors' assets and property).
- **10-Q Q3 2025.** Interim, unaudited, former name. It is the prior-year comparative for the third quarter; it is a separate active source and is not superseded by later reports. Covenant ratio disclosure at page:57.
- **10-Q Q1 2026.** Interim, unaudited, new name. Debt note at page:14 shows the exchange offer outcome at March 31, 2026 and a notice dated May 6, 2026 of the Term Loan A repayment and revolver termination; ratio disclosure at page:44.
- **10-Q Q2 2026.** Latest periodic report. Balance sheet (page:2), income statement (page:3), cash flow (page:5-6), debt note (page:16-19), commitments and legal matters (page:24-25), segment note (page:28-30), liquidity (page:55-57), supplemental guarantor information (page:60), free cash flow reconciliation (page:64) and Item 5 (page:68) are located. The debt table at page:16 shows no Term Loan A balance at June 30, 2026 and no 10.25% notes; page:17 states the Term Loan A was repaid and "terminated its revolving credit facility" on May 12, 2026.
- **Earnings releases.** Management-prepared, attributed supporting claims. They hold the adjusted operating income reconciliation, free cash flow and a net debt and leverage table. Page:11 of the July release states leverage "net debt and finance leases divided by Adjusted Operating Income"; earlier releases state that this ratio "differs from the calculation contained in the Credit Agreement". These management measures do not override the filings. The credit-agreement ratios are printed only in the December 2025 and March 2026 releases and the filings up to the first quarter of 2026.

### Version and relationship notes

- The registrant changed its name from AMC Networks Inc. to AMC Global Media Inc. on April 8, 2026 (10-Q Q2 2026, page:7). The 10-K, the Q3 2025 10-Q and the February 2026 release carry the old name; all are the same registrant (same file number 1-35106, same employer identification number on the cover pages). Citing an old-name source for the current issuer is valid; the name must be mapped, not treated as a different entity.
- Each interim report and release remains a separate active source. The Q2 2026 debt table supersedes the earlier tables only for balances at June 30, 2026; earlier tables remain the evidence for their own dates.
- Duplicate content: the Q2 2026 10-Q and the July 2026 release repeat the licence agreement and the debt repayment text. Retained source for each fact: the 10-Q (filed, controlling); the release is supporting only.

### Coverage and limitation register

| ID | Gap or limitation | Severity | Affected consumers | Evidence and remediation |
| --- | --- | --- | --- | --- |
| L1 | No periodic report after the quarter ended June 30, 2026 is supplied, although the as-of date is 2026-11-05. Whether a later report was filed before the cutoff cannot be told from the sources. | Medium | CP-1, CP-1A, CP-2 | Latest filing is dated July 30, 2026 (10-Q Q2 2026, page:69). Remedy: add any later 10-Q or 8-K filed on or before 2026-11-05 if one exists. Treat events after June 30, 2026 as subsequent events at best. |
| L2 | No executed financing document is supplied: no credit agreement, amendments, 2032 secured notes indenture, 4.25% senior notes indenture, convertible notes indenture or the 2029 notes indenture. Covenant and collateral terms come from filing summaries. The context file records legal documents as "none". | High for covenant analysis, Medium overall | CP-1, CP-2, CP-5 | 10-K page:110-111, 170-173; 10-Q Q2 2026 page:17-19, 60. Remedy: add the 2032 notes indenture and the 2026 consent amendments. |
| L3 | The credit agreement tests (maximum net leverage and minimum interest coverage) ended with the facility on May 12, 2026. The sources do not print the maintenance or incurrence covenants of the surviving notes. Q2 2026 text says only "We were in compliance with all of our debt covenants as of June 30, 2026" (page:57). | High for covenant headroom | CP-1A, CP-2 | Latest printed credit-agreement ratios are at March 31, 2026 (10-Q Q1 2026, page:44; release page:10). No covenant headroom can be derived for June 30, 2026 from the sources. |
| L4 | Wording tension inside the 10-K on guarantees: the supplemental guarantor text says note guarantees are given "on an unsecured basis" (page:112) while the 2032 notes are described as secured by a first-priority lien on substantially all assets (page:171). Not resolved by the sources. Later filings repeat the unsecured wording (10-Q Q2 2026, page:60). | Medium | CP-1, CP-2 | Remedy: read the 2032 notes indenture and security documents. Until then, report both statements with their locators. |
| L5 | Debt perimeter: the pack gives consolidated figures. Restricted and unrestricted subsidiary splits, and the non-wholly-owned entities, are not separately printed; the release says "No adjustments have been made for consolidated entities that are not 100% owned" (July release, page:11). Summarised guarantor financial information for December 31, 2025 and 2024 is in the 10-K (page:112); for the 10-Q the guarantee terms are at page:60 and whether summarised figures follow was not checked. | Medium | CP-1, CP-2 | Treat consolidated as the perimeter, with this caveat. |
| L6 | The licence agreement with Netflix is a subsequent event dated July 30, 2026, described in the 10-Q (page:10, 68) and the release (page:4). Its fee, timing and present-value revenue are management statements about expected cash; the agreement itself is not supplied. | Medium | CP-1A, CP-2 | Amounts must be tagged as expected, not received. |
| L7 | A damages claim (the "MFN Litigation") is described with a trial date of October 27, 2026 (10-Q Q2 2026, page:24). That date falls before the as-of date, but no source reports the outcome or any later ruling. A customer Chapter 11 filing on June 30, 2026 is described without the customer's name or any exposure amount (page:57). | Medium | CP-1A, CP-2 | Outcome and exposure are Not supplied. |
| L8 | The extraction is visible text only. Text has been located for statements and notes, but no table-by-table fidelity review against the original filing layout was done. Tables run as flowing text, so row and column alignment must be rechecked by the user of any figure. | Low to Medium | CP-1, CP-5 | Extraction status is not a fidelity review. Cite page numbers and recheck the figure at the page. |
| L9 | No investor presentation is supplied; the pack holds earnings releases instead (per the retrieval log). Slide content, if any, is outside coverage. | Low | CP-1A | Releases are attributed management claims only. |
| L10 | Period labelling: balance sheet dates and flow periods differ across the sources (year, quarter, six months, twelve months to June 30, 2026 in the release). Twelve-month figures appear only in management non-GAAP tables. | Low | CP-1, CP-5 | Label every figure with its period; do not mix quarter, six-month and twelve-month amounts. |
| L11 | The company reports its own adjusted measures (Adjusted Operating Income, Free Cash Flow, leverage ratio). They are management definitions and differ from the credit-agreement ratios. | Low | CP-1, CP-2 | Keep definitions separate. |

### Conflicts

No conflict between two sources on a figure was found in the pages read. One wording tension is recorded as L4. Management's leverage ratio in the releases and the credit-agreement ratio are different definitions, stated as different by the company, and are not a conflict.

### What cannot proceed

- Covenant headroom for the notes: cannot proceed from these sources (L2, L3).
- Any statement about the period after June 30, 2026 other than the July 2026 subsequent events: cannot proceed (L1).
- Any legal reading of guarantees, liens or covenants: out of scope for this module and unsupported without the executed documents.

### Next evidence action

Add, if they exist on or before 2026-11-05: any later periodic report or 8-K, the 2032 notes indenture with its 2026 amendments, and the 4.25% senior and convertible indentures. Then re-run source readiness for the debt and covenant consumers. For all other consumers, proceed.

## Calculations

No new calculation. CP-0 does not normalise, reconcile or derive figures. Two bookkeeping checks were made on the sources, neither is a derived analytical figure:

- Coverage counts: pages searched by term were 200 of 200 (10-K), 66 of 66 (Q3 2025 10-Q), 54 of 54 (Q1 2026 10-Q), 69 of 69 (Q2 2026 10-Q), 14 of 14, 11 of 11 and 13 of 13 for the three releases. Pages read in full are those named in the Sources table; this is a targeted read, not a page-by-page review of every page.
- The June 30, 2026 debt table at 10-Q Q2 2026 page:16 lists the 4.25% Senior Notes 276,706, the 4.25% Convertible Senior Notes 143,750 and the 10.50% Senior Secured Notes 1,315,098 (thousands of USD) against a printed total of 1,735,554; the three lines add to that printed total. No other figure was recomputed here.

## Gaps

- Not supplied: any filing after July 30, 2026 (L1).
- Not supplied: executed credit agreement and amendments, all indentures, security and guarantee documents (L2).
- Not calculable from the sources: covenant headroom at June 30, 2026, because the credit agreement ended May 12, 2026 and the note covenants are not printed (L3).
- Not supplied: outcome of the trial scheduled for October 27, 2026, name and exposure of the customer in Chapter 11, text of the Netflix licence agreement (L6, L7).
- Not supplied: ratings, market prices, quotes, peers and deal terms (the run settings leave them blank; blank is not zero).
- Unresolved distinction: guarantee "unsecured basis" wording against the secured status of the 2032 notes (L4).
- Extraction is not a fidelity review; layout of tables must be rechecked at the cited page (L8).

## Next module

Proceed to CP-1 with READY_WITH_LIMITATIONS, then CP-1A, CP-2 and CP-5 in the order CP-OS sets. Carry forward L1 to L11 as listed per consumer. CP-1 should take the debt, liquidity, cash flow and segment figures from the filed statements and notes first and use the releases only as attributed support. Do not treat any of the four consumers as DO NOT RUN; a request for covenant headroom or a post-June 30, 2026 view would be CONDITIONAL on the missing documents named above.
