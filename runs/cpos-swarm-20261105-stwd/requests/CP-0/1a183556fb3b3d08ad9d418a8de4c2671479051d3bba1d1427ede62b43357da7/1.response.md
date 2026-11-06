## Request

Issuer: STARWOOD PROPERTY TRUST, INC. (issuer id stwd, NYSE: STWD), a Maryland corporation and the registrant of every supplied filing. As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot, public case. Reporting currency: USD. Current period: q2-2026 (quarter and six months ended June 30, 2026). Prior period: fy-2025 (year ended December 31, 2025).

Question for this module: can the supplied source set support the four requested downstream modules (CP-1 financial base, CP-1A business and transaction view, CP-2 credit view, CP-5 evidence trace), and what remains blocked? This is a source-readiness answer only. It gives no credit conclusion, no legal interpretation and no investment opinion, and it does not normalise, reconcile or calculate figures. Figures below are quoted from the sources to show that located evidence exists, not to assert a value.

Context settings (source `context`, not issuer evidence): no deal terms, no market quotes, no ratings, no valuation inputs, no peers, no research questions, and attachments `legal_documents` set to none. Blank context fields are not treated as zero.

## Sources

Issuer sources relied on. Each file is a page-chunked text extraction of the filed HTML document; "page:N" below means the extraction chunk N, not a printed page. The sha256 is that of the pinned extraction file. Each file's first line also carries the sha256 of the original HTML (shown in the last column), which is a different value.

| Short name | Exact source name | sha256 of pinned file | Chunks | sha256 of original HTML named inside |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | 10-K_2025-12-31_stwd-20251231.htm.jsonl | 5d034c0380b12617b5276d804970154e60e42e6a23c5bcee4ef0d6e26b8a55fd | 284 | 0a5aa5d61543211b30658568212d0ee2bdd5989e8a6985041daba3f732e27c54 |
| 10-Q Q3 2025 | 10-Q_2025-09-30_stwd-20250930.htm.jsonl | d42c4a9a27c9d73fda589e7dc56562d17c85018a2ea82a77ac4a395ea6aee3bc | 155 | 24b318684e4502cf97b71784b6999dc65300d0f6e65958f07ebcbe2709982d42 |
| 10-Q Q1 2026 | 10-Q_2026-03-31_stwd-20260331.htm.jsonl | a981c1ff096bebb78573fc217060d2be7d932d6a1d88404218dd31da70ce8980 | 138 | e7db2be0f9654c41083016ef5668e2603ac8e8c173f0abe9bf376f14297f0ee8 |
| 10-Q Q2 2026 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | e8c4bcc3fcec859b834e7d77d0075c7162cba6647a0dd89e45052bfa9c8b4b3a | 156 | 895418cb733ab86c60331e4e25e5fcb25daaf4d64670fb222e0e0fa2a8bb1edd |
| Release YE2025 | EX-99.1_2026-02-25_stwd_pressrelease-ye2025.htm.jsonl | 1f1cf65fe88590eb05e524e31bd92875cef8da770ee1cfa5cacc2e06538ebd9a | 10 | b71cb9e5a4514187d57ab4e7bad8998133221a3f21fea0398f6767cc9c55e96b |
| Release Q1 2026 | EX-99.1_2026-05-08_stwd_pressrelease-q12026.htm.jsonl | 316bfad5efe7ce527d0308c8cc555686397e0897e2159e9321c558a9bbed50a7 | 6 | 803942d4a579ee85835305349424073862127d507a4abef44047f72ba2a05058 |
| Release Q2 2026 | EX-99.1_2026-08-06_stwd_pressrelease-q22026.htm.jsonl | b1942a46f485117f96015975cca8555da21dd98692e7e25a0fc84b19a0efbf22 | 7 | 4163e1559bbd68cb6dfbfba0e84f84ee5f5dac68bf5132bc71d342a28f935f1b |

Run-settings source: `context` (bb1537683323815090e6da83a4ec1d608fc4d7c145051f90360ef72eab181e62). The file `_retrieval.json` is ignored by the run and is not relied on.

Supplied handoffs: none. CP-0 is the first module in this run, so CP-OS supplied no upstream handoff and there is no handoff module or sha256 to list.

Coverage count: 7 issuer sources, 756 extraction chunks in total, all of them text extractions of HTML documents. No scans, images, workbooks or slide decks are in the pack.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases are enough to run the financial, business, credit and evidence-trace work, with stated limits. No governing debt documents are supplied, and the third-quarter 2026 report is not in the pack. | Medium | Covenant levels, guarantor terms and ratings are not in the pack, and GAAP and securitization-adjusted views differ. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The latest filed period is the quarter ended June 30, 2026, supported by the annual report and two earlier quarterly reports. | The current-period base is a filed, unaudited quarterly report; later events up to the cutoff cannot be checked. | High |
| Consolidated assets include large securitization VIE balances; the releases also give a lower segment total that leaves them out. | Any leverage or asset figure must name which perimeter it uses, or it will mislead. | High |
| Debt tables, maturities, availability and subsequent refinancings are present in the quarterly report. | Maturity and funding work can proceed from filed tables. | Medium |
| Covenant tests are described only in words, with compliance statements and no numeric levels. | Covenant headroom cannot be computed from this pack. | High |
| No credit ratings, market quotes, indentures or credit agreements are supplied. | Ratings, pricing and legal-term analysis stay open. | High |

### Readiness view

The effective source set supports the requested work with bounded limitations, so the overall view is READY_WITH_LIMITATIONS for CP-1, CP-1A, CP-2 and CP-5, and no consumer is CONDITIONAL or BLOCKED. The evidence is a full annual report for FY2025, three quarterly reports (Q3 2025, Q1 2026 and Q2 2026) and three earnings releases that carry segment statements and a distributable-earnings reconciliation. The strongest contrary evidence is what is absent: no executed indenture, credit agreement or management agreement, no rating or quote input, no investor presentation, and no report for any period after June 30, 2026 although the as-of date is 2026-11-05. Each of these narrows what a downstream module may claim rather than stopping it. Source sufficiency is not completion of downstream analysis, and this answer does not evaluate any model input contract (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED).

### Assessment by source

Document family, original authority, perimeter, period and version relationship for each source, with a located quote showing the identity. Extraction fidelity was not independently reviewed against the original HTML; a successful extraction is not a fidelity review.

| Source | Family and authority | Entity and perimeter | Period and basis | Located identity evidence |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | Annual report, audited; controls for FY2025 and Dec 31, 2025 facts | Starwood Property Trust, Inc. and subsidiaries, consolidated, including securitization VIEs | Year ended Dec 31, 2025, USD in thousands | 10-K FY2025 page:1 "For the fiscal year ended December 31, 2025"; page:157 "We have served as the Company’s auditor since 2009." |
| 10-Q Q3 2025 | Quarterly report, unaudited; comparative period only | Same registrant, consolidated | Three and nine months ended Sep 30, 2025, USD in thousands | 10-Q Q3 2025 page:1 "For the quarterly period ended September 30, 2025" |
| 10-Q Q1 2026 | Quarterly report, unaudited | Same registrant, consolidated | Three months ended Mar 31, 2026, USD in thousands | 10-Q Q1 2026 page:1 "For the quarterly period ended March 31, 2026" |
| 10-Q Q2 2026 | Quarterly report, unaudited; latest filed financial statements and controlling source for June 30, 2026 facts | Same registrant, consolidated | Three and six months ended Jun 30, 2026, USD in thousands | 10-Q Q2 2026 page:1 "For the quarterly period ended June 30, 2026" |
| Release YE2025 | Earnings release exhibit; management attribution, not controlling over the 10-K | Registrant; segment statements with a separate securitization VIE column | Quarter and year ended Dec 31, 2025; includes non-GAAP distributable earnings | Release YE2025 page:2 "The Company’s full year GAAP net income was $411.5 million" |
| Release Q1 2026 | Earnings release exhibit | Same | Quarter ended Mar 31, 2026 | Release Q1 2026 page:1 "Quarterly GAAP Earnings of $0.13 and Distributable Earnings (DE) of $0.39 per Diluted Share" |
| Release Q2 2026 | Earnings release exhibit | Same | Quarter and six months ended Jun 30, 2026 | Release Q2 2026 page:1 "GAAP net income of $6.6 million" |

Version relationships. No two sources share a hash and none is a draft or amendment. Each periodic report is a separate active source for its own period: the Q2 2026 10-Q repeats Dec 31, 2025 balance-sheet comparatives (10-Q Q2 2026 page:4 "Total Assets $ 61,046,276 $ 63,183,357"), which overlap the 10-K FY2025 balance sheet (10-K FY2025 page:159 "Total Assets $ 63,183,357"). Overlap is containment of a comparative, not a duplicate; the 10-K controls the December 31, 2025 balance and the Q2 2026 10-Q controls June 30, 2026. Each release restates figures that its same-period 10-Q also reports, and the filing controls where they differ. No difference in a restated Dec 31, 2025 line was reconciled here, by method.

Roles found in the sources. Issuer and registrant: Starwood Property Trust, Inc. It is a holding company ("We are organized as a holding company and conduct our business primarily through our various wholly-owned subsidiaries", 10-Q Q2 2026 page:11) and is externally managed by SPT Management, LLC (10-Q Q2 2026 page:11 "We are externally managed and advised by SPT Management, LLC"). The unsecured senior notes are indentures between the registrant and The Bank of New York Mellon as trustee (10-Q Q2 2026 page:155 "Indenture, dated as of July 10, 2026"). A search of all four periodic reports found no guarantor or co-issuer text for those notes, so guarantor status is an open gap, not a finding of no guarantors. Fundamental Income Properties, LLC became a subsidiary by merger on July 23, 2025 (10-K FY2025 page:9 "On July 23, 2025, we acquired Fundamental Income Properties, LLC") and has its own asset-backed financing with covenants (10-K FY2025 page:221). No parent above the registrant, borrower, restricted or unrestricted group is named; the context also names none.

### Consumer readiness

| Consumer | Status | Evidence located | Bounded limitations carried forward |
| --- | --- | --- | --- |
| CP-1 financial base | READY_WITH_LIMITATIONS | Balance sheet, operations, cash flow including cash paid for interest and income taxes (10-Q Q2 2026 page:9 "Cash paid for interest $ 609,792 $ 561,948"; 10-K FY2025 page:164 "Cash paid for interest $ 1,188,901"); segment statements in the three releases (Release Q2 2026 page:3); discrete Q4 2025 in Release YE2025; Q3 2025 and Q1 2026 quarters in their 10-Qs | Quarter versus year-to-date versus full-year periods must be labelled; no discrete Q4 2025 statement exists in a 10-Q, only in the release; no report after Jun 30, 2026; GAAP versus ex-VIE perimeter (see conflicts); units are thousands in statements and millions or billions in narrative |
| CP-1A business and transaction | READY_WITH_LIMITATIONS | Business, segments and manager description (10-K FY2025 pages 5 and 8, 10-Q Q2 2026 page:11); Fundamental merger (10-K FY2025 page:9); 2026 financings and subsequent events (10-Q Q2 2026 page:101, 10-K FY2025 page:271) | No investor presentation (releases refer to supplemental schedules on the company website, which are not in the pack); management agreement and fee terms only as described in filings, no executed agreement; no deal terms in context |
| CP-2 credit view | READY_WITH_LIMITATIONS | Secured financing table with maximum size, outstanding and approved-but-undrawn capacity (10-Q Q2 2026 page:143); unsecured notes table (10-Q Q2 2026 page:56); principal repayment schedule (10-Q Q2 2026 page:55); contractual obligations (10-Q Q2 2026 page:148); funding commitments (10-Q Q2 2026 page:94); nonaccrual loans (10-Q Q2 2026 page:33); subsequent refinancings (10-Q Q2 2026 page:101); covenant compliance statements (10-Q Q2 2026 page:50) | Covenant levels and definitions are not supplied; only the unsecured-note unencumbered-asset test is described, in the 10-K FY2025; no ratings; the bulleted list that follows "Our primary sources of liquidity are as follows:" is not in the extracted text (10-Q Q2 2026 page:137), so a stated current-liquidity figure exists only in the YE2025 release headline; guarantors not stated; no post-Jun 30, 2026 financial statements |
| CP-5 evidence trace | READY_WITH_LIMITATIONS | Every source is page-chunked with stable page:N locators and pinned hashes | The trace can only be as complete as the upstream handoffs, which do not yet exist; extraction fidelity was not independently reviewed; release figures are management claims |

### Conflicts and perimeter distinctions

1. Total assets under two perimeters. The balance sheet reports "Total Assets $ 61,046,276" at June 30, 2026 (10-Q Q2 2026 page:4), including securitization VIE assets at fair value. The Q2 2026 release headline says "Record Total Assets of $31.8 Billion" (Release Q2 2026 page:1) and its segment balance sheet shows a subtotal before the VIE column: "$ 31,772,112 $ 29,274,164 $ 61,046,276" (Release Q2 2026 page:7). The two are different perimeters, not an error. Effect: CP-1 and CP-2 must state whether a leverage, asset or liability figure is GAAP-consolidated or ex-VIE, and the filing's consolidated figure controls for GAAP facts. The ex-VIE basis is a management presentation.
2. Cash flow under two perimeters. The liquidity section reports cash flows on a GAAP basis and on a basis "Excluding Securitization VIEs" (10-Q Q2 2026 page:137). Same effect as above.
3. Non-GAAP earnings. Distributable earnings is defined by the company and used to compute the external manager's incentive fee (Release Q2 2026 page:4 "Distributable Earnings, a non-GAAP financial measure"). It differs from GAAP net income attributable to the registrant for the same quarter (Release Q2 2026 page:5 "Distributable Earnings (Loss) $ 185,728 $ 27,139 $ 34,177 $ 42,389 $ (137,930) $ 151,503"; 10-Q Q2 2026 page:5 "Net income attributable to Starwood Property Trust, Inc. $ 6,557 $ 129,814 $ 58,435 $ 242,069"). A release figure cannot silently replace a filed GAAP figure.
4. Debt after the balance-sheet date. The notes table at June 30, 2026 (10-Q Q2 2026 page:56 "Total principal amount 4,930,750 4,330,750") predates July 2026 events that change the maturity profile: a new issue of 5.875% Senior Notes due 2029 used to redeem the 2027 Senior Notes, and repayment of the 2026 Senior Notes at maturity (10-Q Q2 2026 page:101). Effect: maturity-wall work must show the June 30, 2026 table and the July 2026 pro forma separately and label the latter as a subsequent event.
5. Secured debt totals appear in several tables with different scope: other secured financing (10-Q Q2 2026 page:49), the repayment schedule that includes securitized financing (10-Q Q2 2026 page:55) and the MD&A table with undrawn capacity (10-Q Q2 2026 page:143). They are not reconciled here. Downstream modules must tie them before use.

### Coverage accounting

Retained for downstream use: financial statements and notes, segment data, debt and liquidity tables, covenant and compliance statements, cash flow, subsequent-event notes, market-risk item, legal proceedings ("no material legal proceedings are pending", 10-Q Q2 2026 page:154) and exhibit lists for all periodic reports. Explicit gaps: items listed under Gaps. Evidenced exclusions: none; no content was excluded. Unknown values are not treated as zero anywhere in this answer.

## Calculations

No new calculation was made. CP-0 does not normalise, reconcile or calculate figures. The only arithmetic is the coverage count: 4 periodic reports plus 3 releases is 7 issuer sources; chunk counts 284, 155, 138, 156, 10, 6 and 7 sum to 756. The count of seven shown in the sources table was checked against the run's printed source list.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No report or filing for any period after June 30, 2026, although the as-of date is 2026-11-05; the next quarterly report (period ended Sep 30, 2026) is not in the pack, and no later current report is supplied | Medium | CP-1, CP-1A, CP-2, CP-5 | Obtain filings dated on or before the cutoff if any exist; otherwise label all figures as of June 30, 2026 and treat later events as unknown, not as none |
| No executed indentures, credit agreements, repurchase agreements or management agreement; the indentures appear only as exhibit-list entries (10-Q Q2 2026 page:155) | High for covenant and guarantor work | CP-2, CP-5 | Obtain the governing documents; until then covenant headroom is Not calculable and guarantor structure is Not supplied |
| Covenant levels and definitions: the 10-K FY2025 describes a minimum tangible net worth, cash liquidity and ratio tests in general terms (10-K FY2025 page:34) and a 120% unencumbered-asset test for the notes (10-K FY2025 page:35), with compliance statements (10-K FY2025 page:142; 10-Q Q2 2026 page:50), but no numeric levels or reported covenant figures | High | CP-2 | Same as above |
| Guarantors and co-issuers of the unsecured senior notes: no text found in any periodic report | Medium | CP-2 | Same as above |
| Credit ratings of the issuer or its debt: none in context and none located in the filings (the filings mention ratings only for investments held) | Medium | CP-2 | Supply ratings if wanted; absent ratings are Not supplied, not unrated |
| Market quotes, valuation inputs, peers and deal terms: context is blank | Medium | CP-2 | Supply if relative value is later needed; not a source-readiness block for the four consumers |
| Liquidity-source list is missing from the extracted text after "Our primary sources of liquidity are as follows:" in each report; a stated current-liquidity figure is found only in the YE2025 release headline (Release YE2025 page:2 "Current Liquidity of $1.4 Billion") and none for June 30, 2026 | Medium | CP-1, CP-2 | Rebuild liquidity from balance-sheet cash and the undrawn-capacity table; do not assume a June 30, 2026 stated figure exists. Check the original HTML for the lost list |
| No investor presentation; the releases point to supplemental schedules on the company website that are not supplied | Low | CP-1A | Accept the releases as attributed management material |
| Extraction fidelity not independently reviewed against the original HTML; tables flattened to text | Low | all | Spot-check key figures against the filing when cited |
| Quarter labelling: no discrete Q4 2025 statement in a 10-Q; Q4 2025 comes from the YE2025 release, while a derived value would need full-year less nine-month figures | Low | CP-1 | Use the release for Q4 2025 and label it management-attributed |
| Currency and units: all USD; statements in thousands, narrative in millions and billions, per-share figures in dollars. No other currency is reporting currency, although exposure to GBP, EUR, AUD, CHF and SEK is hedged (10-Q Q2 2026 page:154) | Low | CP-1, CP-2 | Keep unit labels on every figure |

## Next module

CP-1 (financial base) may run next on the full pack, followed by CP-1A, CP-2 and CP-5 in the order CP-OS sequences them. Carry forward: use the Q2 2026 10-Q for June 30, 2026 facts and the 10-K FY2025 for December 31, 2025 facts; state the consolidated or ex-VIE perimeter on every figure; label quarter, six-month, full-year and LTM periods; keep management releases as attributed claims; treat covenant levels, guarantors, ratings and any post-June 30, 2026 events as Not supplied; do not infer them from silence.
