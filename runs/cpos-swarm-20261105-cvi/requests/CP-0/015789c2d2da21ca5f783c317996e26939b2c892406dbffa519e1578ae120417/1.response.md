## Request

Module CP-0, source readiness, for CVR ENERGY INC (ticker CVI, issuer id cvi), as of 2026-11-05, pathway credit_snapshot, current period Q3 2026, prior period FY2025, reporting currency USD. The cutoff is 2026-11-05. The selected downstream consumers are CP-1, CP-1A, CP-2 and CP-5. The question is whether the supplied source set can support that work and what remains blocked. This handoff gives no credit conclusion, no legal interpretation and no investment opinion, and it calculates nothing. Figures appear only inside quotes of retained source text.

The context file is the user's dated settings and not issuer evidence. It leaves the borrower, parent, guarantor, ratings, quotes, deal terms, valuation inputs and research questions blank. Blank means unknown here, not zero.

## Sources

### Issuer sources relied on

Each row is a pinned source file. Page is the source chunk shown as page:N, not the printed page.

| Source name | sha256 | Document family and period | Chunks |
| --- | --- | --- | --- |
| 10-K_2025-12-31_cvi-20251231.htm.jsonl | 11b2ae0e09456bfa771d4cab8a17d5e6eecebad270822a0aa27a6321ae3e1326 | Form 10-K, fiscal year ended December 31, 2025 | 192 |
| 10-Q_2026-03-31_cvi-20260331.htm.jsonl | 0d5ec22f9043f7de61004c1d3fc3166812200367bbaae195e5e1fbdd81619bfc | Form 10-Q, quarter ended March 31, 2026 | 59 |
| 10-Q_2026-06-30_cvi-20260630.htm.jsonl | 358aaec14a40e7fb2473ba1f5c1574588c88cdab98ea0a6156b8c6e07d430343 | Form 10-Q, quarter ended June 30, 2026 | 58 |
| 10-Q_2026-09-30_cvi-20260930.htm.jsonl | c1bc2003ec1856161a58b4e8e6474dd136cd1e6864fe6be884dd4ce7689172a8 | Form 10-Q, quarter ended September 30, 2026, signed November 3, 2026 | 73 |
| EX-99.1_2026-04-29_exhibit991-cviq12026earnin.htm.jsonl | ec1426d7dc5a0e9978dd49bcfe1d59907ecfcc63064a0912a9028158f50040e7 | Earnings release exhibit, Q1 2026, dated April 29, 2026 | 14 |
| EX-99.1_2026-07-29_exhibit991-cviq22026earnin.htm.jsonl | 1459a1187a6f9d055543784814ad9e46560c18ce90ff9327aed9062ea6d7d429 | Earnings release exhibit, Q2 2026, dated July 29, 2026 | 11 |
| EX-99.1_2026-11-03_d897437dex991.htm.jsonl | a8afdbbc4ca0ef0b0aa3933661eb6fa3f49fab4f6b6643dc433309cf920a00ae | Earnings release exhibit, Q3 2026, dated November 3, 2026 | 12 |

### Other inputs

| Input | sha256 | Role |
| --- | --- | --- |
| context (1376139-cvr-energy-inc-cvi.json) | 90a4adce7121ac13b0bc8c46b1ee93789832813a3c6223523e8f15963f3f61b5 | User settings, not issuer evidence |
| _retrieval.json | Not supplied to this module | Ignored by CP-OS; not used as evidence |

### Supplied handoffs

None. CP-0 is the first module in this run, so no upstream handoff exists.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases are enough for the selected financial, business and evidence-trace work. The set has gaps in legal documents, in the pending acquisition papers and in segment comparability across periods. | Medium | No indentures, credit agreements or acquisition agreement are supplied, and text extraction was not checked against images or layout. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Filed statements, debt notes, liquidity text and compliance statements are located for the latest quarter and the prior year end. | Debt, liquidity and cash flow work can be traced to filings. | High |
| A pending refinery acquisition with new financing and a minimum cash requirement is described only in the latest quarterly report and its release. | Acquisition terms and financing cannot be tested against executed documents. | Medium |
| The segment structure changed from three segments in the annual report to two in 2026 quarterly reports. | Annual and quarterly segment figures may not compare without care. | Medium |
| Debt totals differ by presentation between the notes, the discussion section and the release. | Any leverage or maturity work must name the basis used. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for source sufficiency only. The annual report, three quarterly reports and three earnings releases are all filed or furnished primary documents of one registrant, CVR Energy, Inc., and every period between FY2025 and Q3 2026 is covered by a located filing. That is enough for the owners of CP-1, CP-1A, CP-2 and CP-5 to perform their methods. No source is blocked and no consumer is CONDITIONAL. The limitations are bounded and listed below: no executed legal documents, no acquisition agreement or financing commitment papers, no presentations, a segment re-cut between the annual and quarterly reports, differing debt presentation bases, and an extraction that was not reviewed for fidelity. This is not a statement that downstream analysis is complete, and the assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

### Source-by-source assessment

Original authority: the annual report and the three quarterly reports are filed statements and control their own facts. The three releases are furnished management documents; their narrative is attributed management language and cannot override the filings. Extraction status is not a fidelity review. Every source is a text extraction, so images, charts and layout were not inspected.

| Source | Entity and perimeter | Period and basis | Use and limit |
| --- | --- | --- | --- |
| Form 10-K FY2025 | CVR Energy, Inc., a holding company consolidating CVR Partners, LP as a variable interest entity (Q3 report page:13 states this; the annual report cover is page:1) | Audited year; three-year comparatives; three reportable segments | Debt note, covenant text, guarantee text, liquidity at year end, segment note. Authoritative for FY2025. |
| Form 10-Q Q1 2026 | Same registrant and perimeter | Unaudited three months to March 31, 2026; two reportable segments | Interim statements, debt, liquidity; superseded for balance sheet date by later quarters but retained as a separate source. |
| Form 10-Q Q2 2026 | Same | Unaudited three and six months to June 30, 2026 | Same use; retained separately. |
| Form 10-Q Q3 2026 | Same; carries the pending acquisition and subsequent events | Unaudited three and nine months to September 30, 2026 and balance sheet at that date, with December 31, 2025 comparative | Primary source for current period, debt, liquidity, covenant compliance, acquisition note, segment recast. |
| Release Q1 2026 | Same | Attributed management narrative and non-GAAP measures for Q1 2026 | Supporting claims only. Chunk 1 holds only the extraction header; narrative starts in chunk 2. |
| Release Q2 2026 | Same | Same for Q2 2026 | Supporting claims only. |
| Release Q3 2026 | Same | Same for Q3 2026, dated November 3, 2026, inside the cutoff | Supporting claims; announces the acquisition and the dividend. |

The three quarterly reports and the three releases are separate active sources. None is a duplicate of another, and none is collapsed because a later one exists. The Q3 report restates the debt table twice (note 6 and the liquidity discussion); that is containment inside one source, not a duplicate source.

### Coverage of evidence demanded by the selected work

| Evidence need | Located in | Status |
| --- | --- | --- |
| Statements: balance sheet, operations, equity, cash flows | Q3 report page:8, page:9, page:10 | Retained |
| Debt by instrument with coupon and maturity | Q3 report page:16; annual report page:119 and notes around page:151 to page:159 | Retained |
| Facility capacity, borrowings, letters of credit, availability | Q3 report page:16 | Retained |
| Liquidity and minimum cash related to the acquisition | Q3 report page:59 | Retained |
| Covenant compliance statements | Q3 report page:17 and page:59; annual report page:159 | Retained as statements only |
| Covenant test terms, thresholds and headroom | Annual report page:156 mentions a minimum fixed charge coverage ratio test "in certain circumstances" | Gap: levels and triggers not located |
| Segment results and total assets | Q3 report page:26 and page:27 | Retained for two segments |
| Non-GAAP reconciliations | Q3 report page:56; annual report page:115; releases | Retained, management definitions |
| Cash paid for interest and taxes | Q3 report page:27 note 14; annual report page:177 | Retained |
| Business and transaction narrative | Q3 report page:11 to page:13 and page:30; Q3 release page:1 | Retained, acquisition from filing summary only |
| Discrete quarters | Q1, Q2, Q3 2026 reports and releases; 2025 quarters appear as comparatives | Retained for 2026; Q4 2025 not reported discretely in the supplied set |

### Conflicts and comparability issues

1. Segment structure. The annual report says "three reportable segments: petroleum, renewables, and nitrogen fertilizer" (annual report page:88). The 2026 quarterly reports say "two reportable segments: Petroleum and Nitrogen Fertilizer" (Q3 report page:26), and the annual report anticipated the change ("This reversion is expected to result in changes to the Company's reportable segments in 2026", annual report page:175). Downstream effect: FY2025 segment figures from the annual report are not on the same basis as 2025 comparatives in the 2026 quarterly reports, where renewable fuel activity sits in "Other". CP-1 must label the basis and not splice them.
2. Debt presentation. The note 6 total for CVR Energy debt includes finance lease obligations ("Total CVR Energy debt 1,175 999", Q3 report page:16) while the liquidity discussion table excludes them ("Total CVR Energy debt 1,171 997", Q3 report page:59). The release rounds ("including $570 million held by the Nitrogen Fertilizer Segment", Q3 release page:2) against the note ("Total Nitrogen Fertilizer Segment debt 569 569", Q3 report page:16). These are basis and rounding differences, not contradictions of fact, but any leverage or maturity work must name its basis.
3. Management language. The Q3 release calls the quarter "the best quarterly results in the Company's history" (Q3 release page:1). That is management characterisation and is not adopted here.
4. The Q3 report cover page states shares outstanding at October 30, 2026, and the signature is dated November 3, 2026. Both are inside the cutoff.

### Evidence register

Quotes are exact substrings of the cited chunk.

| Source | Locator | Quote | Supports |
| --- | --- | --- | --- |
| 10-Q Q3 2026 | page:1 | For the quarterly period ended September 30, 2026 | Period identity |
| 10-Q Q3 2026 | page:1 | CVR ENERGY, INC. (Exact name of registrant as specified in its charter) | Entity identity |
| 10-Q Q3 2026 | page:8 | Cash and cash equivalents (including $158 and $69, respectively, of consolidated variable interest entity (“VIE”)) $ 1,278 $ 511 | Balance sheet retained, VIE perimeter |
| 10-Q Q3 2026 | page:9 | Net sales $ 3,281 $ 1,944 $ 8,000 $ 5,352 | Statement of operations, quarter and nine months |
| 10-Q Q3 2026 | page:10 | Net cash provided by operating activities 1,026 144 | Cash flow statement, nine months |
| 10-Q Q3 2026 | page:11 | CVR Partners, LP, a publicly traded limited partnership | Subsidiary perimeter |
| 10-Q Q3 2026 | page:11 | for aggregate cash consideration of approximately $4.2 billion | Pending acquisition, subsequent event dated November 2, 2026 |
| 10-Q Q3 2026 | page:12 | senior secured 364-day bridge loan facility in an aggregate principal amount of up to $2.5 billion | Acquisition financing commitment |
| 10-Q Q3 2026 | page:16 | 7.500% Senior Notes, due February 2031 $ 600 $ — | Debt by instrument |
| 10-Q Q3 2026 | page:16 | 6.125% Senior Secured Notes, due June 2028 550 550 | Segment-level secured notes |
| 10-Q Q3 2026 | page:16 | CVR Energy’s Amended and Restated ABL Credit Agreement (“CVR Energy ABL”) $ 550 $ — $ 20 $ 530 February 12, 2031 | Facility capacity, letters of credit, availability |
| 10-Q Q3 2026 | page:17 | were in compliance with all covenants under their respective debt instruments as of September 30, 2026 | Covenant statement only |
| 10-Q Q3 2026 | page:26 | two reportable segments: Petroleum and Nitrogen Fertilizer | Segment basis in 2026 |
| 10-Q Q3 2026 | page:27 | Cash paid for interest 106 116 | Cash interest, nine months |
| 10-Q Q3 2026 | page:56 | Adjusted EBITDA $ 582 $ 180 $ 828 $ 302 | Management non-GAAP measure |
| 10-Q Q3 2026 | page:58 | continues to accrue WRC’s 2026 RFS obligations at 100% of the required amount | Contingent obligation context |
| 10-Q Q3 2026 | page:59 | we had total liquidity of approximately $1.9 billion | Liquidity statement |
| 10-Q Q3 2026 | page:59 | maintain at least $500 million of unrestricted cash and cash equivalents | Acquisition-related cash restriction |
| 10-Q Q3 2026 | page:59 | Total CVR Energy debt 1,171 997 | Debt basis differs from page:16 |
| 10-Q Q3 2026 | page:64 | Interim Chief Financial Officer | Governance context |
| 10-K FY2025 | page:88 | three reportable segments: petroleum, renewables, and nitrogen fertilizer | Segment basis in FY2025 |
| 10-K FY2025 | page:115 | Adjusted EBITDA $ 393 $ 317 $ 1,164 | FY2025, FY2024, FY2023 non-GAAP |
| 10-K FY2025 | page:119 | Total long-term debt, including current portion $ 1,699 $ 1,861 | Prior year end debt |
| 10-K FY2025 | page:153 | The Notes are jointly and severally guaranteed on a senior unsecured basis by the wholly owned subsidiaries of CVR Energy with the exception of CVR Partners and its subsidiaries | Guarantee perimeter, annual report text |
| 10-K FY2025 | page:156 | requires the Credit Parties in certain circumstances to comply with a minimum fixed charge coverage ratio test | Covenant exists, terms not located |
| 10-K FY2025 | page:175 | This reversion is expected to result in changes to the Company’s reportable segments in 2026 | Segment change foreshadowed |
| 10-Q Q1 2026 | page:2 | Condensed Consolidated Balance Sheets - March 31, 2026 and December 31, 2025 (unaudited) | Period identity |
| 10-Q Q2 2026 | page:52 | As of June 30, 2026, we had total liquidity of approximately $1.3 billion | Liquidity statement at Q2 |
| Release Q1 2026 | page:2 | Adjusted EBITDA of $37 million | Management measure, Q1 |
| Release Q2 2026 | page:1 | Adjusted EBITDA of $209 million | Management measure, Q2 |
| Release Q3 2026 | page:1 | Adjusted EBITDA for the third quarter of 2026 was $582 million compared to $180 million for the third quarter of 2025. | Management measure, Q3 |
| Release Q3 2026 | page:1 | the best quarterly results in the Company’s history | Management language, not adopted |
| Release Q3 2026 | page:2 | including $570 million held by the Nitrogen Fertilizer Segment | Rounded segment debt in release |

### Consumer assessment

| Consumer | Source view | Evidence demand and carried limitations |
| --- | --- | --- |
| CP-1 financial extraction | READY_WITH_LIMITATIONS | Needs statements, debt by facility, cash interest and tax, discrete quarters, non-GAAP. All are located. Carry the segment re-cut, the debt basis differences, the absence of a discrete Q4 2025, and the fact that adjusted measures are management definitions. |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Needs ownership, operating model, history and the transaction. Located in the Q3 report and release. Carry that the Purchase Agreement, commitment letter and subscription agreements are not supplied, so terms rest on the filing summary only. |
| CP-2 fundamental synthesis | READY_WITH_LIMITATIONS | Draws on CP-1 and CP-1A; the source set does not itself block it. Carry every limitation above. Upstream handoffs are sequenced by CP-OS and are not a readiness condition. |
| CP-5 evidence trace | READY_WITH_LIMITATIONS | All claims can be traced to page-addressable text. Carry that extraction fidelity of tables was not reviewed and that no image or chart content was inspected. |

The report sections selected for this run (key findings, company operating model, model chart strip, financials and credit metrics, strengths and weaknesses, company profile, transaction summary) rest on the same set. Sections omitted by CP-OS (capital structure, relative value, portfolio fit, committee challenge, what changed) are out of scope and no readiness is assessed for them.

## Calculations

None. CP-0 does not normalize, reconcile or calculate figures. Coverage counts are the chunk counts in the source table. No derived number appears in this handoff; every figure is inside a quote.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No executed legal documents (indentures, ABL credit agreements, CVR Partners credit agreement) are supplied; the context records legal documents as none. Covenant terms, baskets, springing tests, guarantee releases and security are known only from filing summaries (annual report page:152 to page:159). | Medium | CP-1, CP-2, CP-5 | Add the documents if covenant headroom or structural claims are to be tested. Otherwise state them as filing-summary level. |
| Covenant test levels, step-downs and the issuer-reported fixed charge ratio are not located. Compliance is stated, thresholds are not. | Medium | CP-1, CP-2 | Report as Not supplied unless an executed agreement is added. |
| Acquisition papers are not supplied: Purchase Agreement, debt commitment letter, subscription agreements, the permanent financing terms. Terms rest on the Q3 report page:11 to page:13 and the Q3 release. The acquisition is pending and not closed at the cutoff. | Medium | CP-1A, CP-2 | Treat as filing summary. Do not treat financing as completed. Closing outcome is unknown at the cutoff. |
| No presentations or investor decks are supplied. The pack holds earnings releases only, so no slide coverage is claimed. | Low | CP-1A | None needed for the selected scope. |
| Segment re-cut: annual report uses three segments, 2026 reports use two. FY2025 segment data in the annual report is not recast in the supplied annual report. | Medium | CP-1, CP-2 | Label basis on every segment figure; use the recast 2025 comparatives from the 2026 reports when comparing quarters. |
| Debt presentation bases differ between note 6, the liquidity discussion table and the release (see conflicts). | Low | CP-1, CP-5 | Name the basis used for each debt total. |
| Discrete Q4 2025 is not reported in the supplied set; a last-twelve-months view needs derivation from the annual report and the interim periods, on mixed segment bases. | Low | CP-1 | Derive only with labelled inputs, or report as Not calculable on a consistent basis. |
| Extraction fidelity: all sources are text extractions. Tables are flattened and column alignment was not checked against the rendered documents. Images and charts were not inspected. Q1 release chunk 1 holds only the extraction header. | Low | All | Spot-check any table figure that drives a conclusion against the cited chunk. |
| Ratings, market quotes, peer data and sponsor materials are blank in the context. | Low | CP-2 | Do not use external knowledge to fill them. |
| Interim Chief Financial Officer and a separate chief accounting officer certification appear in the Q3 report (page:64, page:71). This is a governance observation, not a source defect. | Low | CP-1A | Carry as context only. |

Nothing dated after 2026-11-05 is used. The acquisition agreement date, November 2, 2026, and the dividend declaration, November 3, 2026, are inside the cutoff. Contract dates later than the cutoff, such as notes maturing in 2031 and 2034, are terms and not events.

## Next module

CP-1, financial data extraction, may proceed. It should take the Q3 2026 quarterly report as the primary source for the current period, use the annual report for FY2025, label the segment basis and the debt basis on every figure, state covenant levels as Not supplied, and keep adjusted measures attributed to management. CP-1A should follow with the acquisition described from the filing summary only, then CP-2, then CP-5. Evidence action before any covenant headroom or structural claim: obtain the executed credit agreement and indentures if the committee needs them.
