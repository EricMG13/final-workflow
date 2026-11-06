# CP-0 Source readiness for TripAdvisor, Inc. (trip), as of 2026-11-05

## Request

Issuer: TripAdvisor, Inc. (ticker TRIP, run issuer id trip), the Nevada registrant that files the supplied reports under Commission file number 001-35362. As-of date and evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, which the filings use throughout. Current period: Q3 2026 (quarter ended September 30, 2026). Prior period: FY2025.

Question answered by this handoff: can the pinned source set support the downstream modules CP-1 (financial facts), CP-1A (business and transaction context), CP-2 (fundamental credit synthesis) and CP-5 (evidence trace and research QA), and what remains blocked. This handoff gives no credit conclusion, legal interpretation or investment opinion, and it normalizes, reconciles and calculates nothing. Context fields for borrower, parent, guarantors, ratings, quotes, deal terms and research questions are blank in the run context; blank is treated as not supplied, never as zero.

No upstream handoff exists for this module; it is the first in the sequence.

## Sources

### Issuer sources relied on

Every document below was read as a text extraction in pages of about 3,000 characters (`page:N` is the extraction chunk, not the printed page). The sha256 is of the pinned extraction file. The `Visible text of ... sha256` line inside each file's first page is the hash of the original HTML and differs from the pinned hash by construction; identity rests on the pinned hash and on the cover text, not on the filename.

| Source (exact name) | sha256 | Document family and authority | Period and perimeter | Coverage |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31_trip-20251231.htm.jsonl | 8885b42791d5e90823a0c9c46491e45285d32d010f68b9715cb0b383be7e31bf | Annual report on Form 10-K, audited statements (audit opinion at page:104); primary authority | FY2025, year ended December 31, 2025; consolidated Tripadvisor, Inc. including TheFork; whole USD millions | 194 of 194 pages retained |
| 10-Q_2026-03-31_trip-20260331.htm.jsonl | 9289cc81c4291efc67a199ffd3d95096f8d91f0c627c0d49a15ca4c0525a91f8 | Quarterly report on Form 10-Q, unaudited; primary authority | Q1 2026, three months ended March 31, 2026; consolidated including TheFork as a third segment; USD millions to one decimal | 53 of 53 pages retained |
| 10-Q_2026-06-30_trip-20260630.htm.jsonl | 358dea410a455694571e6fd8ed4ffb768fc6929fddacda37801383944ce9f7e1 | Quarterly report on Form 10-Q, unaudited; primary authority | Q2 2026 and six months ended June 30, 2026; TheFork recast to discontinued operations, two continuing segments | 65 of 65 pages retained |
| 10-Q_2026-09-30_trip-20260930.htm.jsonl | 37e12b49f799525884b2d1c8f8223439d80dbaee990e3c8305474f0abf40c5c7 | Quarterly report on Form 10-Q, unaudited; primary authority and the latest balance sheet | Q3 2026 and nine months ended September 30, 2026; continuing operations with TheFork as discontinued; cover share count as of October 30, 2026 | 72 of 72 pages retained |
| EX-99.1_2026-05-07_trip-ex99_1.htm.jsonl | 986da54f4628e6ef7caa0f060a29736fbe7ef71884de15f953b1b79776621916 | Earnings release (Exhibit 99.1), management narrative with non-GAAP reconciliations; supporting claims only | Q1 2026, dated May 7, 2026; pre-recast perimeter with TheFork as a segment | 20 of 20 pages retained |
| EX-99.1_2026-08-06_trip-ex99_1.htm.jsonl | 4b5f625f62e6af22d7ff5c0ad78ab3c67f22ed4bd26c03b70a227ec22f7f24b0 | Earnings release (Exhibit 99.1); supporting claims only | Q2 2026, dated August 6, 2026; continuing operations, TheFork discontinued | 21 of 21 pages retained |
| EX-99.1_2026-11-05_trip-ex99_1.htm.jsonl | 08c99d197b1e28c92053c736e4c07c927f197a67f49f8aceaed0f5db801c0a1c | Earnings release (Exhibit 99.1); supporting claims only | Q3 2026, dated November 5, 2026 (the cutoff day); continuing operations | 21 of 21 pages retained |

### Run context (not issuer evidence)

| Source | sha256 | Role |
| --- | --- | --- |
| context (1526520-tripadvisor-inc-trip.json) | 1fa2d7822828d80dbe527b9dde9239ab274e8339a7a989f9acc6255a06577c7a | User settings for the run: dates, currency, pathway, identity. Contains no issuer figures. |

### Files in the pack folder that are not pinned sources

`_retrieval.json` is listed by the launcher as ignored. It is retrieval metadata, not issuer evidence, and nothing below relies on it as a fact about the company.

### Supplied handoffs

None. CP-0 is the first module and CP-OS supplied no upstream handoff.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven pinned filings and releases can support a bounded credit snapshot of Tripadvisor, with limitations. The binding caveats are a changed reporting perimeter after the restaurant platform sale and the absence of the lender documents. | Medium | Annual and first-quarter filings include the sold restaurant business; annual continuing figures appear only in a management release; no credit agreement, covenant ratio or ratings are supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual report, three quarterly reports and three earnings releases are all present, and the latest release is dated on the cutoff day. | Debt, liquidity and cash flow can be sourced to filed statements rather than to management claims alone. | High |
| The annual report and first-quarter documents include the sold restaurant business, while later documents present it as discontinued. | Leverage and coverage must not mix perimeters, and the like-for-like annual base rests on a management release, not a filing. | Medium |
| Debt terms come only from filing notes. The credit agreement, covenant calculation and guarantor detail are not supplied. | Covenant headroom and collateral cannot be tested beyond management's statement of compliance. | Medium |
| The restaurant sale closed after quarter end and a new restructuring plan began the day before the cutoff. | Cash and debt after the quarter end are in no balance sheet, and use of sale proceeds is management intent only. | Medium |
| No credit ratings, bond quotes or forward guidance are supplied. | Relative value and rating-based views cannot be supported from this pack. | Medium |

### Readiness view

The effective source set is sufficient for source-level work on Tripadvisor, Inc. across all four requested modules, with bounded limitations, so each consumer is READY_WITH_LIMITATIONS and none is CONDITIONAL or BLOCKED. The evidence is strongest where it is a filed statement: the Q3 2026 Form 10-Q carries the latest balance sheet, debt note, liquidity discussion, goodwill impairment note and subsequent events, and the audited 10-K carries the debt, covenant and security terms. The strongest contrary evidence is a perimeter break. The 10-K, the Q1 10-Q and the Q1 release present TheFork inside the consolidated results, while the Q2 and Q3 10-Qs and releases present only continuing operations with prior periods recast. A downstream reader who joins the annual figures to the latest quarter without noticing this will overstate or understate trends. What cannot proceed from these sources is any test that needs the executed credit agreement, the covenant computation, ratings or market prices, a filed continuing-operations full-year base, or a post-closing balance sheet. The next evidence action is to obtain the Amended Credit Agreement and its three amendments, which the 10-K exhibit index lists as exhibits filed by reference, and to carry the perimeter label on every figure into CP-1. Source sufficiency is established here only; completion of the downstream analysis is not asserted.

### Source-by-source assessment

Each row records what the located text shows. A successful extraction is not a fidelity review: the extraction flattens tables into one cell per line, so column alignment must be checked against the cited page by the consumer. Images, charts and speaker notes were not inspected and no decks are in the pack.

| Source | What located text establishes (evidence) | Authority and extraction notes | Consequence for consumers |
| --- | --- | --- | --- |
| 10-K FY2025 | page:1 cover: "For the fiscal year ended December 31, 2025", registrant TRIPADVISOR, INC., file number 001-35362. page:160-165 debt note; page:161 states the revolver covenant and security; page:192-193 exhibit index lists the credit agreement and three amendments. | Audited; whole USD millions, so figures are rounded to the nearest million and are not to be netted against one-decimal 10-Q figures without a rounding label. Includes TheFork in consolidated and segment data (page:185). | Source for the FY2025 base on the old perimeter and for the contractual debt terms. Not a continuing-operations base. |
| 10-Q Q1 2026 | page:1 cover period March 31, 2026; page:43 debt and liquidity; page:36 TheFork segment discussion. | Unaudited; one decimal. Pre-recast perimeter, so its income statement and cash flows include TheFork. | Used only with a perimeter label; the first-quarter continuing-operations figures are not printed in it. |
| 10-Q Q2 2026 | page:1 cover period June 30, 2026; page:10-11 TheFork put option and held-for-sale; page:15-16 discontinued operations tables; page:55 debt and liquidity. | Unaudited; first filing on the recast perimeter. | Source for six-month and second-quarter continuing figures and for the first disclosure of the sale. |
| 10-Q Q3 2026 | page:1 cover period September 30, 2026; page:3 balance sheet; page:6-7 cash flows; page:11-12 sale and discontinued presentation; page:22-23 goodwill; page:25-26 debt; page:37 subsequent events; page:61-66 liquidity. | Unaudited; the latest balance sheet and the comparative December 31, 2025 column recast for held-for-sale lines. | Primary source for the current position. Controls over the Q3 release where the two differ. |
| EX-99.1 Q1 release | page:1 summary table with TheFork as a segment. | Management narrative and non-GAAP reconciliations (page:11-15). Supports, never overrides, the 10-Q. | Attributed management claims and Adjusted EBITDA bridges on the pre-recast perimeter. |
| EX-99.1 Q2 release | page:1 pending sale; page:2 continuing operations highlights. | Supporting claims with reconciliations (page:12-16). | Bridge from the pre-recast to the recast perimeter in management's words. |
| EX-99.1 Q3 release | page:1 headline figures; page:3 restructuring action and goodwill impairment narrative; page:12-16 reconciliations and quarterly supplemental tables. | Supporting claims. Contains management claims not repeated in the 10-Q, for example expected annualized savings. | Attributed management claim only; a figure stated here alone cannot be carried as a filed fact. |

### Perimeter and period register

The perimeter changed during 2026 and the supplied sources straddle the change. Evidence for the break:

- Q2 release, page:1: "As a result of the pending transaction, the financial results of TheFork are classified as discontinued operations, and are no longer a reportable segment."
- Q3 10-Q, page:12: "the financial results of TheFork business are classified as discontinued operations in the unaudited condensed consolidated financial statements for all periods presented".
- The December 31, 2025 comparative in the Q3 10-Q is recast: goodwill is 724.2 there (page:3) against 844 in the 10-K balance sheet (page:108), and TheFork goodwill of 112.4 and 119.7 is shown separately as held for sale (page:16). The 10-K balance sheet and the Q3 10-Q comparative therefore describe different perimeters for the same date.

Mechanism and consequence: a trend or leverage metric that divides a figure from one perimeter by a figure from the other mixes the sold business into one side only. CP-1 must label every figure by perimeter and period, and CP-2 and CP-5 inherit that label. Cash is the clearest case: the Q3 10-Q balance sheet reports cash and cash equivalents of 706.8 for continuing operations, while the cash flow statement ends at 750.1 including restricted cash and discontinued operations, with 43.3 attributed to discontinued operations (page:6). These are different captions and perimeters, not a conflict.

Period labels the consumers will meet: three months and nine months ended September 30, 2026 and 2025; three and six months ended June 30; three months ended March 31; FY2025, FY2024 and FY2023 in the 10-K. No LTM or trailing figure is printed in any pinned source (searched the Q3 10-Q and Q3 release for twelve-month, trailing and LTM wording; only descriptive year references were found). The Q3 release does carry, at page:12-16, supplemental tables from continuing operations with each 2025 quarter, the 2025 full year and the 2026 quarters and year to date, covering revenue by segment, GAAP net income, Adjusted EBITDA, operating cash flow, capital expenditures and free cash flow. That gives a continuing-operations quarterly series at management-release authority only; the table footnote says full-year totals are as reported and may differ from the sum of the quarters because of rounding. The corresponding filed statements for the 2025 full year and fourth quarter on the continuing perimeter (operating income, interest expense, interest income, cash flow statement, cash paid for interest and taxes) are not in the pack.

### Entity and instrument roles located in the sources

- Issuer and registrant: Tripadvisor, Inc., a Nevada corporation (Q3 10-Q page:1). The 10-K records redomestication from Delaware to Nevada effective April 29, 2025 (10-K page:17).
- Borrowers under the credit agreement: the 10-K exhibit index names "Tripadvisor, Inc., Tripadvisor Holdings, LLC, Tripadvisor, LLC, the other Borrowers party thereto" with JPMorgan Chase Bank, N.A. as Administrative Agent (10-K page:192). The context names no separate borrower or guarantor, so the borrower group and the "Subsidiary Loan Parties" that grant security (10-K page:161) are unresolved distinctions, carried as a gap.
- Instruments located: a revolving Credit Facility of 500.0 maturing June 29, 2028; a Term Loan B Facility of 500.0 issued July 8, 2024 plus a 350.0 tack-on of March 20, 2025, maturing July 8, 2031 at SOFR plus 2.75% (Q3 10-Q page:25); 0.25% Convertible 2026 Senior Notes, repaid at maturity on April 1, 2026 (Q3 10-Q page:25-26). Q3 10-Q page:62 states "an aggregate principal amount remaining of $833.9 million" on the term loan and "The Term Loan B Facility has no financial covenants."
- Covenant evidence: 10-K page:161 states the Amended Credit Agreement "requires us to maintain a maximum total net leverage ratio of 4.5 to 1.0 solely in respect to the Credit Facility". The Q3 10-Q page:62 repeats only that a maximum total net leverage ratio applies and that "we were in compliance with our covenant requirements in effect under the Credit Facility"; it prints no level and no computed ratio.
- Security: 10-K page:161 states obligations are "secured by substantially all assets" of the company and the Subsidiary Loan Parties under the Security Documents.
- Unaudited versus audited: only the 10-K is audited; the three 10-Qs and three releases are unaudited, and the releases are management documents.

### Conflicts and unreconciled differences

| Item | Located statements | Downstream effect | Severity |
| --- | --- | --- | --- |
| Term loan rate at September 30, 2026 | Q3 10-Q page:25 gives an effective interest rate of 6.92%; Q3 10-Q page:62 gives "the interest rate on the Term Loan B Facility was 6.65%" at the same date. The second figure is not labelled effective or contractual. | Cost-of-debt and interest-coverage work must state which rate is used. Not reconciled here. | Low |
| Letters of credit at December 31, 2025 | 10-K page:161 gives $4 million; Q3 10-Q page:62 gives $3.6 million for the same date. | Rounding of whole millions versus one decimal; use the one-decimal figure for liquidity. | Low |
| Net loss for Q3 2026 | Q3 release page:1 headline net loss is on continuing operations (316.9); the Q3 10-Q consolidated statements show net loss including discontinued operations (313.1). | A perimeter difference stated in both documents, not an error; label which is used. | Low |
| Wording on the retired 2026 notes | 10-K page:164-165 calls the 2026 Senior Notes "senior unsecured obligations"; Q3 10-Q page:25 says "the related security interest and liens have been released" on repayment. | Possible springing or shared collateral wording that the pack cannot resolve; relevant only to history of the capital structure now that the notes are repaid. | Low |

### Consumer assessment

| Consumer | Status | Evidence demand and what the sources supply | Carried limitations |
| --- | --- | --- | --- |
| CP-1 financial facts | READY_WITH_LIMITATIONS | Needs statements, quarter versus year-to-date, segments, add-backs, facility-level debt, cash-paid interest and taxes. Supplied: Q3 10-Q statements, segment note (page:33-37), debt note (page:25-26), cash paid for interest and taxes (page:6-7), non-GAAP reconciliations in the releases. | Perimeter break; LTM is not printed and the FY2025 continuing series exists only in the Q3 release supplemental tables (management authority); covenant ratio not printed; 10-K in whole millions; Q1 2026 continuing figures are in no filing and only in the Q3 release tables. |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Needs ownership, business model and change history. Supplied: business description (10-K page:4-6, Q3 10-Q page:39-41), the LTRIP merger (10-K page:17, 111-112), the TheFork sale (Q3 10-Q page:11-12, 42), restructuring (page:43-44), the goodwill impairment (page:22-23, 43). | The Equity Purchase Agreement and Transition Services Agreement are described, not supplied; sale proceeds and gain are stated as approximate and subject to adjustment; the savings claim is a management statement in the Q3 release. |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Works from the CP-1 and CP-1A handoffs only; the source set does not prevent that. | Inherits every CP-1 and CP-1A limitation. Its dependency on those handoffs is sequenced by the planner and is not a source condition. |
| CP-5 evidence trace and QA | READY_WITH_LIMITATIONS | Needs locators that can be reopened. All seven sources are retained in full, so citations resolve to `page:N`. | Table cells are flattened in extraction; derived figures require recomputation by CP-5 from cited components. |

None of the four consumers is marked DO NOT RUN.

### Management claims versus filed facts

The Q3 release (page:3) states that the November 4, 2026 restructuring "is expected to result in total company annualized gross savings of approximately $40 million". The Q3 10-Q (page:37, page:43) gives the plan date and a cost range but this savings figure was not found in the 10-Q. It is an attributed management claim and must stay labelled as such. Likewise the expected gain on the TheFork sale and the intended use of proceeds are management statements: the Q3 10-Q (page:65) says "management currently expects that the Company will prioritize reduction of its long-term debt" and that it "will continue to maintain optionality", which is intent, not an executed commitment.

### Subsequent events and cutoff handling

Events after the September 30, 2026 balance sheet date but on or before the 2026-11-05 cutoff, per the Q3 10-Q (page:11, page:37): the sale of TheFork closed on November 1, 2026 with approximately 741.0 of net cash consideration and an expected fourth-quarter gain of about 487.0, both "subject to change"; a Transition Services Agreement of up to 12 months with American Express started at closing (page:12-13); a restructuring plan began on November 4, 2026 with expected pre-tax costs of approximately $15 million to $20 million (page:37). No pinned source is dated after the cutoff. The Q3 10-Q cover share count is as of October 30, 2026, before the cutoff.

## Calculations

None. CP-0 does not normalize, reconcile or calculate figures. Figures above are reproduced exactly as printed, with their locator, and are not combined. The only counts are source page counts (194, 53, 65, 72, 20, 21 and 21 pages for the seven sources, all retained) taken from the extraction files.

## Gaps

Each gap names the missing input, the consumers it affects, why it matters and the remediation.

| Gap | Missing input and searches made | Affected consumers | Why it matters | Remediation |
| --- | --- | --- | --- | --- |
| Lender documents | Not supplied: the Amended Credit Agreement, its First, Second and Third Amendments and the Security Documents. They are listed in the 10-K exhibit index (page:192-193) but their text is not in the pack. Searched all seven sources for the covenant definitions; only note summaries were found. | CP-1, CP-1A, CP-2, CP-5 | Covenant definition of total net leverage, add-backs, baskets, springing maturity terms and guarantor perimeter cannot be verified. | Obtain the exhibits from the filings that incorporate them. |
| Covenant computation | Not supplied: the issuer's computed total net leverage ratio. Level 4.5 to 1.0 appears only in the 10-K (page:161); the 2026 10-Qs state compliance without a ratio. | CP-1, CP-2 | Headroom cannot be sourced; any derived ratio would use a different definition. | Treat as Not calculable until the compliance certificate or definition is obtained. |
| Filed continuing-operations annual base | Not supplied as a filing: FY2025 and Q4 2025 operating income, interest expense, interest income, cash flow statement and cash paid for interest and taxes on the continuing perimeter, and any printed LTM figure. Supplied only at management-release authority: quarterly 2025 and 2026 revenue, GAAP net income, Adjusted EBITDA, operating cash flow, capital expenditures and free cash flow (Q3 release page:12-16). Nine-month 2025 comparatives in the Q3 10-Q are recast. | CP-1, CP-2 | Leverage and coverage on the post-sale perimeter rest on non-GAAP and unaudited management tables for the Q4 2025 leg; interest coverage on a continuing basis cannot be completed for that leg. | CP-1 may build LTM Adjusted EBITDA and LTM operating cash flow from the release quarters with a calculation shown and the authority labelled; interest for the Q4 2025 leg is Not supplied. |
| Q1 2026 continuing-operations discrete figures | Not printed in the Q1 filing or Q1 release, which include TheFork; the Q3 release supplemental tables (page:12-16) print a first-quarter 2026 continuing column, and the Q2 10-Q gives the six-month continuing result. | CP-1 | The first-quarter continuing figures are available only at management-release authority. | CP-1 to cite the release column and cross-check it against the Q2 and Q3 10-Q year-to-date figures. |
| TheFork sale documents | Not supplied: the Equity Purchase Agreement of August 2, 2026, the Put Option Agreement of June 14, 2026 and the Transition Services Agreement. Terms are known only from the 10-Q and releases. | CP-1A, CP-2, CP-5 | Final consideration, adjustments, indemnities and the proceeds waterfall cannot be confirmed. | Treat the sale terms as filed disclosure, not executed-document evidence. |
| Post-closing capital structure | Not supplied: any balance sheet or debt balance after November 1, 2026, or any commitment to repay the term loan. | CP-1, CP-2 | The roughly 741.0 of proceeds is not in any statement; intended debt reduction is not an executed action. | Revisit when the next periodic report is filed (not available by the cutoff). |
| Ratings, market data and guidance | Not supplied: credit ratings, bond or loan quotes, valuation inputs or forward guidance (searched sources for rating agency names and outlook wording; none found; the context ratings and quotes fields are empty). The only market reference is the statement in the goodwill note that the stock price fell nearly 40% from June 30 to September 30, 2026 (Q3 10-Q page:22). | CP-2 | No rating or market-implied cross-check is possible. | External sources would be needed and would have to be labelled external. |
| Presentations and charts | No investor presentation or decks are in the pack; earnings releases stand in. Text extraction only; no chart or image content was inspected. | CP-1, CP-1A | Visual or slide-only disclosures, if any exist, are not covered. | None for this run. |
| Guarantors and restricted group | The Subsidiary Loan Parties and guarantors under the credit agreement are not named in the pack; the context lists none. | CP-1A, CP-2 | Structural subordination and collateral reach cannot be assessed beyond the "substantially all assets" statement. | Obtain the guarantee and security schedules. |
| Extraction fidelity | Flattened table cells; the first page of each file carries the original HTML hash rather than the pinned hash. No fidelity review was performed. | All | Column misalignment risk when reading numeric tables. | Consumers reopen each cited page and confirm labels, signs and periods. |

## Next module

Proceed to CP-1 on all seven sources. Instructions carried forward: label every figure with its period and perimeter (consolidated including TheFork, or continuing operations with TheFork discontinued); keep the 10-K in whole millions and the 10-Qs in one decimal; take the current position from the Q3 2026 10-Q and use the releases only as attributed management support; reproduce the covenant statement as qualitative compliance without inventing a ratio; build any LTM figure only from the Q3 release quarterly continuing tables (page:12-16) with the calculation shown and the management authority labelled, and mark the filed FY2025 continuing statements, Q4 2025 interest and post-closing figures as Not supplied or Not calculable; and cite the Q3 10-Q page numbers given above for the debt, liquidity, goodwill and subsequent-event items. CP-1A, CP-2 and CP-5 follow in dependency order and inherit this handoff's limitations.
