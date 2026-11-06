## Request

Module CP-0 (source readiness) for SM Energy Co (issuer id sm, ticker SM; registrant name on the cover is SM ENERGY COMPANY), as of 2026-11-05, pathway credit_snapshot, case kind public. Cutoff 2026-11-05. Reporting currency USD (every source reports in US dollars, in millions unless a sentence says billions). Current period q3-2026, prior period fy-2025, as set in the run context. Requested downstream consumers: CP-1, CP-1A, CP-2 and CP-5. The report blocks selected for the minimum set are key-findings, company-operating-model, model-chart-strip, financials-credit-metrics, strengths-weaknesses, company-profile and transaction-summary.

Question answered here: can the supplied source set support that work, and what remains blocked? This handoff gives no credit conclusion, legal interpretation or investment opinion, and it normalizes, reconciles or calculates no figure. Source sufficiency is kept apart from completion of downstream analysis.

The run context is user settings, not issuer evidence. It leaves the borrower, parent, guarantor, ratings, quotes, deal terms, valuation and assumptions fields blank and sets legal_documents to none. Blank is treated as not supplied, never as zero.

## Sources

### Issuer sources relied on

All seven issuer sources are retained as text extractions (one record per page chunk; a locator `page:N` below is the chunk number, not the printed page). The sha256 is the pinned hash of the extraction file that CP-OS supplied. Page 1 of each extraction also prints a different sha256 for the original HTML document; that is the hash of the upstream file, not of the pinned extraction, and the pinned hash controls this run.

| Source (exact name) | Pinned sha256 | Chunks |
| --- | --- | --- |
| 10-K_2025-12-31_sm-20251231.htm.jsonl | e8932d9647a97ab4096dd543c01cda4006057a408b2bc3fa1755c23dc94ba27e | 205 |
| 10-Q_2026-03-31_sm-20260331.htm.jsonl | 45237f139ae59527446c46c29ce6b302442f1b1133c6a522f87376bfd87f4049 | 68 |
| 10-Q_2026-06-30_sm-20260630.htm.jsonl | 6404fb70a5450d38bf3b3c16da403bf19b4d2205562c84a2c87afdc694f9126d | 68 |
| 10-Q_2026-09-30_sm-20260930.htm.jsonl | 354b7aaa1a83736b6232300aa038c2e407fc12a2943b257d38be5e15b857042f | 66 |
| EX-99.1_2026-05-06_exhibit99105062026er.htm.jsonl | 5913cf03f0dc7c1579e2da8f8a0720be2946682a7844315b0aa6198cf5e98607 | 13 |
| EX-99.1_2026-08-05_exhibit99108052026er.htm.jsonl | c611381a32ea896857849afba30a25e0af8ac568cabbb54d05c3d2eded519c0a | 15 |
| EX-99.1_2026-11-03_exhibit99111032026er.htm.jsonl | 4d33629074f8a450075efc018d0d5d57de50a9ccd6af427fe22e4ed725fe6f8a | 14 |

Context file (user settings, not issuer evidence): context, sha256 816e6f5709a9a2983bc6f7b0c91f473b414f35053a0b72e52f3a0a46de98a561. The pack index _retrieval.json was ignored by CP-OS and is not relied on.

### Handoffs relied on

None. CP-0 is the first module of this run and CP-OS supplied no upstream handoff.

### Source register

Document family, original authority, perimeter and period are taken from located content, not from file names.

| Source | Family and authority | Entity and perimeter | Period and basis | Located evidence |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | Annual report, audited statements (control for audited facts) | Registrant SM Energy Company and consolidated subsidiaries, a single reporting entity | Year ended December 31, 2025, SM standalone before the Civitas merger; merger closing and Fourth Amendment appear as post-year-end events | page:1 "For the fiscal year ended December 31, 2025"; audit report page:132; statements pages 132-137; Note 5 debt pages 158-162; exhibit list pages 198-201 |
| 10-Q Q1 2026 | Interim report, unaudited, filed statements | Same registrant, now including Civitas from the closing date | Quarter ended March 31, 2026 | page:1 "For the quarterly period ended March 31, 2026" |
| 10-Q Q2 2026 | Interim report, unaudited, filed statements | Same registrant | Quarter ended June 30, 2026 with six-month year-to-date columns | page:1 "For the quarterly period ended June 30, 2026" |
| 10-Q Q3 2026 | Interim report, unaudited, filed statements (latest filed financials) | Same registrant; one reportable segment | Quarter and nine months ended September 30, 2026, signed before the cutoff | page:1 "For the quarterly period ended September 30, 2026"; page:66 "November 4, 2026"; segment note page:29 |
| EX-99.1 May 2026 release | Earnings release, unaudited, management narrative and non-GAAP; supporting only | Same registrant | Quarter ended March 31, 2026 | page:2 "DENVER, May 6, 2026"; reconciliations pages 10-12 |
| EX-99.1 August 2026 release | Earnings release, unaudited; supporting only | Same registrant | Quarter ended June 30, 2026 | page:1 "SM Energy Reports Second Quarter 2026 Results" |
| EX-99.1 November 2026 release | Earnings release, unaudited; supporting only | Same registrant | Quarter ended September 30, 2026, dated before the cutoff | page:1 "SM Energy Reports Third Quarter 2026 Results"; net debt reconciliation page:14 |

Version relationships: the three 10-Qs and the 10-K are separate periodic filings, not amendments or duplicates; none supersedes another, and each is retained. Each release is the management view of the same quarter as the 10-Q of the matching date; where the two differ in a figure the filing controls and the difference is logged under Gaps. No draft, unsigned or superseded document was found. No duplicate hash pairs exist among the seven sources.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed documents are enough for the requested snapshot work on the merged company, with limitations. Debt, liquidity, the merger, the asset sale and the quarterly trend are all in the filings. | Medium | No credit agreement, indentures, ratings or investor slides are supplied, so current covenant terms and guarantor detail cannot be confirmed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The latest filing gives a note-by-note debt table, revolver availability and the maturity profile after the recent redemptions. | Debt and near-term liquidity work can proceed from filed numbers. | High |
| The merger closed in the first quarter and changed the entity; prior-year comparatives are the old smaller company. | Year-over-year trends mislead unless the merger effect is separated. | High |
| Covenant levels are given only in the annual report, before the credit agreement amendment that changed the definitions. | Covenant headroom cannot be stated as current from these sources. | Medium |
| Ratings, indenture terms and the investor slides are absent. | Rating-linked and legal-structure points must be marked not supplied. | High |

### Readiness view

The effective source set supports the requested snapshot work for SM Energy Co with stated limitations. Four filed periodic reports and three earnings releases cover the full period from the last annual report through the quarter ended 2026-09-30, one reporting entity, and one currency. The financial statements, the debt note, the liquidity table, the merger and divestiture notes, the derivative notes and the non-GAAP reconciliation are all present and located. What the set cannot do is confirm governing legal terms, current covenant levels after the credit agreement was amended, ratings, post-merger reserves, or anything shown only on investor slides. These gaps bound the work; none stops it. Source sufficiency is the only assertion made: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

| Consumer | Readiness | Reason in one line |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Statements, debt table, liquidity table and reconciliations are present; legal terms, guarantors and current covenant levels are not. |
| CP-1A | READY | The merger, divestiture, operating areas and one-segment structure are described in the filings; sponsor and ownership fields are blank because the company is listed. |
| CP-2 | READY_WITH_LIMITATIONS | Enough filed evidence for a fundamental synthesis; ratings, reserves after the merger and covenant headroom are bounded gaps. |
| CP-5 | READY | Every claim can be traced to a located page of a pinned source; the trace depends on upstream handoffs that the dependency planner sequences, which is not a source condition. |

### Evidence by area

Located evidence, each quote an exact substring of the cited chunk. The mechanism column states why the evidence matters to the source set, not a credit conclusion.

| Area | Locator and exact quote | Source risk mechanism and downstream consequence |
| --- | --- | --- |
| Entity change | 10-Q Q3 page:10 "Upon completion of the Merger, we issued 124 million shares to holders of Civitas common stock" | The registrant after 2026-01-30 is a different perimeter from the one in the annual report; CP-1 and CP-2 must not roll annual figures forward without the merger bridge. |
| Prior-year comparability | 10-Q Q3 page:6 "Basic weighted-average common shares outstanding 237 115 225 115" | Comparative columns are the pre-merger company; the same filing offers pro forma revenue and net income on page:13 only. A like-for-like discrete-quarter series cannot be read straight across. |
| Debt instruments | 10-Q Q3 page:19 "Total $ 6,456 $ 190 $ (32) $ 6,614" | Principal, premium and deferred costs are all given per series, so the facility-level debt schedule is supportable; the premium belongs to assumed notes and affects carrying value, not principal. |
| Maturity profile | 10-Q Q3 page:21 "we have no Senior Notes maturities until mid-2028" | The maturity ladder is readable from the note table and the rate table on page:18; the revolver maturity is only partly stated (see Gaps). |
| Revolver liquidity | 10-Q Q3 page:18 "Available borrowing capacity 2,498 2,498 1,999" | Drawn balance, letters of credit and commitments are given at three dates, so liquidity can be built from printed inputs; the October 22, 2026 column is a subsequent event. |
| Borrowing base | 10-Q Q3 page:17 "the borrowing base and aggregate revolving lender commitments under the Credit Agreement were $5.0 billion and $2.5 billion, respectively" | Commitments, not the larger borrowing base, cap availability; consumers must not read the borrowing base as liquidity. |
| Covenant test | 10-Q Q3 page:60 "a maximum permitted ratio of total funded debt, as defined in the Credit Agreement, to adjusted EBITDAX" | The test exists and compliance is stated on page:21, but the level and the amended definition are not printed in the quarterly report. |
| Covenant level (older) | 10-K page:161 "cannot be greater than 3.50 to 1.00 on the last day of each fiscal quarter" | Dated before the Fourth Amendment; see conflicts below. |
| Divestiture | 10-Q Q3 page:13 "total cash proceeds of $894 million after final purchase price adjustments and selling costs" | Final proceeds and gain are filed; earlier estimates in other sources differ (see conflicts). |
| Cash interest | 10-Q Q3 page:8 "Cash paid for interest, net of capitalized interest $ (331) $ (165)" | Nine-month figure only; a discrete third-quarter cash interest figure needs subtraction from earlier filings and is not printed. |
| Non-GAAP | 10-Q Q3 page:60 "Adjusted EBITDAX (non-GAAP) 1,341 588 3,717 1,747" | Reconciled to GAAP in the filing, so the metric has filed authority for the periods shown; the covenant EBITDAX definition may differ. |
| Net debt | EX-99.1 Nov page:14 "Net Debt (non-GAAP) $ 6,014" | Management measure derived from filed principal and cash; supporting claim only. |
| Segment | 10-Q Q3 page:29 "We have one reportable segment" | No segment tables to extract; model inputs are consolidated. |
| Commitments | 10-Q Q3 page:22 "the aggregate undiscounted deficiency payments would total $205 million" | Off-debt claims exist and are printed; the contingent drilling commitment has no damages estimate ("We cannot reasonably estimate the amount of damages"). |
| Hedging | 10-Q Q3 page:26 "all of our derivative counterparties were members of our Credit Agreement lender group" | The derivative book is secured alongside the revolver, a structural fact for CP-2. |

### Conflicts and inconsistencies between sources

| Item | Locators | Downstream effect |
| --- | --- | --- |
| Divestiture proceeds appear on three bases: "net proceeds of approximately $900 million" (EX-99.1 May page:4, an estimate at closing), "net cash proceeds of $888 million received" (10-Q Q3 page:56, cash received in the nine months), and "$894 million after final purchase price adjustments" (10-Q Q3 page:13, final, with part settled after September 30, 2026). | EX-99.1 May page:4; 10-Q Q3 pages:13, 56 | Not a contradiction: estimate, cash received to date and final settlement. Consumers must label the basis and use the filing for amounts. |
| The same figure of $894 million is also the principal of 2028 Civitas notes repurchased in the tender ("we repurchased $894 million aggregate principal amount", 10-Q Q3 page:20). | 10-Q Q3 pages:13, 20 | Two unrelated items with equal amounts; a lookup by amount alone would confuse them. |
| The divestiture is named "South Texas Divestiture" in the 10-Qs and "Galvan Divestiture" in a footnote to the November release guidance table, dated the same day ("the Galvan Divestiture"). | 10-Q Q3 page:13; EX-99.1 Nov page:3 | Same event inferred from the April 30, 2026 date; the release does not define the term. Use the filing name. |
| Covenant level: 10-K states a total funded debt to adjusted EBITDAX ceiling and a current ratio floor; the Fourth Amendment (January 30, 2026) made "certain other amendments to the financial covenant definitions". | 10-K pages:158, 161; 10-Q Q3 page:17 | Current levels and definitions are unconfirmed. Older level must be labelled as FY2025 and pre-amendment. |
| Gain on divestiture: Q2 shows "an estimated gain of $262 million" (10-Q Q3 page:37), the nine-month figure is "(260)" with a third-quarter loss of "2" (10-Q Q3 page:60). | 10-Q Q3 pages:37, 60 | Consistent as a true-up in the third quarter; the quarter and nine-month figures must not be mixed. |

## Calculations

None. CP-0 does not normalize, reconcile or calculate figures. The only arithmetic in this handoff is counting: seven issuer sources (four periodic filings and three releases) and one context file; 205, 68, 68, 66, 13, 15 and 14 chunks respectively, as printed in the pinned extractions. Every figure quoted above is copied from its located chunk and was checked against that chunk; none is derived.

Inputs that downstream modules can compute from printed figures, listed for planning and not calculated here: liquidity (cash, commitments, letters of credit, drawn balance at 10-Q Q3 pages:5 and 18); gross and net leverage (principal at page:19, cash at page:5, adjusted EBITDAX at page:60 and in the 10-K reconciliation at page:131); interest coverage (interest expense at page:6, cash interest at page:8); a trailing twelve-month series (10-K year, nine-month filings and the quarterly releases).

## Gaps

| Gap | Severity | Affected consumers | Remediation and evidence |
| --- | --- | --- | --- |
| Credit agreement, Fourth Amendment, indentures and supplemental indentures are not supplied. The 10-K exhibit list names them (page:201 "Fourth Amendment to Seventh Amended and Restated Credit Agreement"; page:200 "First Supplemental Indenture, dated as of January 30, 2026") but the executed documents are not in the pack, and the context sets legal_documents to none. | High for legal analysis; bounded for financial work | CP-1, CP-2 | Obtain the executed documents. Until then covenant definitions, baskets, restricted-payment capacity, guarantor lists and call schedules are Not supplied. |
| Current financial covenant levels. Only the 10-K states them, before the amendment that changed the definitions. The quarterly report states compliance and the test but not the level or the reported ratio. | High for headroom | CP-1, CP-2 | Obtain the amended credit agreement or a compliance certificate. Headroom is Not calculable on current terms. |
| Revolver maturity detail. The Fourth Amendment extends maturity "for elected revolving commitments to January 30, 2031"; the maturity of non-elected commitments is not stated, and whether the springing maturity added by the Third Amendment (10-K page:158) still applies is not stated. | Medium | CP-1, CP-2 | Obtain the amendment. Label the revolver maturity as partly supported. |
| Guarantors and obligors by instrument. The filing says notes are guaranteed by "each of our existing subsidiaries that guarantee the Credit Agreement" (10-Q Q3 page:21) without naming them; the context lists no guarantors. Restricted versus unrestricted subsidiaries are not described. | Medium | CP-1, CP-2 | Obtain the indenture guarantor schedules. Perimeter beyond the consolidated registrant is unresolved. |
| Credit ratings are not supplied. The 10-Q Q3 (page:51) says two agencies upgraded the company but names neither agency nor the level; the context ratings list is empty. | Medium | CP-2 | Obtain rating reports. Rating level and outlook are Not supplied. |
| Investor slides. The November release (page:1) refers to "accompanying slides" at the company website; the pack holds earnings releases only, no presentation. No slide, image or speaker note is claimed as inspected. | Low to medium | CP-1A, CP-2 | Obtain the decks if slide claims are needed. Release text is attributed management narrative only. |
| Reserves after the merger. The only reserve and standardized measure disclosures are year-end FY2025 (10-K pages:21-24, 187-190), covering the company before the merger; the 10-Qs do not update them. | Medium | CP-2 | Obtain a post-merger reserve report if asset coverage is wanted; otherwise mark Not supplied. |
| Purchase price allocation is preliminary (10-Q Q3 page:11 "The purchase price allocation for the Merger is preliminary"), so acquired-asset and assumed-liability amounts may change. | Medium | CP-1, CP-2 | Use as filed and label as preliminary. |
| Pro forma leverage or EBITDAX including Civitas before January 30, 2026 is not supplied; only pro forma revenue and net income are (10-Q Q3 page:13). Prior-year columns are the pre-merger company. | Medium | CP-1, CP-2 | Trailing-period metrics must be labelled as mixing a standalone and a merged period. |
| Discrete quarter and cash-flow detail. Cash flows, cash interest and cash taxes are year-to-date in each 10-Q; discrete quarters need subtraction of consecutive filings. The Q1 and Q2 10-Q statements were checked in this review only for period identity, the covenant sentence and the cover; their line items were not read here. | Low | CP-1 | Downstream module reads the exact lines it uses. |
| Off-balance-sheet and non-debt claims. Delivery commitments, a drilling commitment and liquidated damages are described in 10-Q Q3 page:22. Pension and lease detail is last given at year-end in the 10-K (pages:176, 180). The 10-Q describes no pension or lease change. | Low | CP-1, CP-2 | Carry the year-end figures forward labelled as FY2025. |
| Extraction fidelity. Tables are flattened to text lines, so a dash cell can shift columns (for example premium cells on 10-Q Q3 page:19). No fidelity review against the original HTML was done; successful extraction is not a fidelity review. | Low | All | Open the cited chunk before using any table figure. |
| Currency and units: the sources print USD in millions, with some sentences in billions. No other currency or period basis was found; the context currency and periods match the sources. | None | All | No action. |

Nothing dated after the cutoff 2026-11-05 is used as fact. The 10-Q Q3 and the November release are dated before the cutoff. Subsequent events inside the filings (borrowing base reaffirmed after September 30, 2026, final divestiture settlement, the October 22, 2026 column) are dated before the cutoff and are labelled as subsequent.

## Next module

Proceed to CP-1, then CP-1A, CP-2 and CP-5 in the order CP-OS plans them. No consumer is marked DO NOT RUN: none is CONDITIONAL or BLOCKED. Carry these limits forward: (1) label every covenant level from the 10-K as FY2025 and pre-amendment, and state headroom as Not calculable on current terms; (2) separate pre-merger comparatives from merged periods and label any trailing figure that mixes them; (3) use filings over releases wherever they differ, and label divestiture proceeds by basis; (4) write Not supplied for ratings, guarantor lists, executed legal terms, post-merger reserves and slide content; (5) cite chunk numbers as `page:N` and open each before use. The next evidence action, if the analyst wants the gaps closed, is to add the Fourth Amendment and indentures and the rating reports to the pack.
