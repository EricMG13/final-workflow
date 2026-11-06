## Request

Source readiness review of the pinned pack for Service Properties Trust (SVC, issuer id svc), as of 2026-11-05 (cutoff 2026-11-05), pathway credit_snapshot, case kind public. The run context names reporting currency USD, current period q3-2026 and prior period fy-2025. The requested downstream modules are CP-1, CP-1A, CP-2 and CP-5, which feed the minimum report set (key findings, company and operating model, model and chart strip, financials and credit metrics, strengths and weaknesses, company profile, transaction summary).

Question answered: can the pinned source set support that work, and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion. It does not normalise, reconcile or calculate figures. Source sufficiency is kept separate from completion of downstream analysis. The assertion for the model objective is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

Perimeter and units: the registrant is Service Properties Trust, a Maryland REIT, and the filings are consolidated for it and its wholly owned subsidiaries, including taxable REIT subsidiaries (TRSs) that are consolidated variable interest entities. The 10-K and 10-Qs state dollars in thousands. The units are printed in the headings of the statements, for example in the 10-Q for the quarter ended September 30, 2026, page:2 ("dollars in thousands, except per share data"), and the consolidation basis is on page:7.

## Sources

### Issuer sources relied on

Each file below is a text extraction of an SEC filing, pinned by the sha256 of the extraction file. The sha256 printed on page:1 of each extraction is the hash of the original HTML and is a different value, so it is not the pin.

| Source (exact name) | sha256 | Pages | Document family and authority |
| --- | --- | --- | --- |
| 10-K_2025-12-31_svc-20251231.htm.jsonl | 15b3016df80eabdf6701b53b9a448339a1d5ae915a5566d3f751538a9f1cf080 | 219 | Audited annual report, FY2025 (year ended December 31, 2025). Controls for audited annual facts. |
| 10-Q_2026-03-31_svc-20260331.htm.jsonl | ddc1e35889e90bee1694334ce247e9f387726f16b7ce89bd8b9a51b4f4bc89df | 61 | Unaudited quarterly report, Q1 2026. |
| 10-Q_2026-06-30_svc-20260630.htm.jsonl | da660527db0f1353ac545e91f43f35b2233d5df64df735bb0e6f23f04bc598ba | 71 | Unaudited quarterly report, Q2 2026 and six months. |
| 10-Q_2026-09-30_svc-20260930.htm.jsonl | f0504ddf51d9be829b263ff0aec5ab5ea7aa542d5518e107dbff10e9d9d5c34a | 73 | Unaudited quarterly report, Q3 2026 and nine months. Latest filed financial statements before the cutoff. |
| EX-99.1_2026-05-06_svc_033126xexhibitx991.htm.jsonl | 2f1a4993f8cd70e48576dc6e794111c2977d7a50e2e8b2ecb75d059468ae6628 | 1 | Press-release notice for Q1 2026 results, dated May 6, 2026. |
| EX-99.1_2026-08-05_svc_063026xexhibitx991.htm.jsonl | fb76ab0c1c7105cbf6ef323f85f2c808f256d901d8e982c18e3c61667221ab25 | 1 | Press-release notice for Q2 2026 results, dated August 5, 2026. |
| EX-99.1_2026-11-04_svc_093026xexhibitx991.htm.jsonl | 865a9819dca5454c3d53aca165a47efc28c6cf0685e35747e559ffc2c9cf026d | 1 | Press-release notice for Q3 2026 results, dated November 4, 2026. |

### Run context (not issuer evidence)

| Item | sha256 | Use |
| --- | --- | --- |
| context (945394-service-properties-trust-svc.json) | a72cf33ce12be07f9ed0051d7ed4f82ab1f3905d4d81ff0fe1a5919c08327fd3 | Dated settings only. It leaves market data, ratings, deal terms, guarantors, parent and borrower blank. Blank values are not read as zero. |

### Supplied handoffs

None. CP-0 is the first module in this run and CP-OS supplied no upstream handoff, so no handoff module or sha256 is listed.

### Ignored file

_retrieval.json is in the pack folder and was ignored by CP-OS. It is not a source.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings are enough to build the requested snapshot for Service Properties Trust through the September 30, 2026 quarter, with limits. All four downstream workflows can proceed, none is blocked. | Medium | No credit agreement or indentures, and the three earnings releases carry no financial figures, so revolver covenant levels and adjusted metrics are not available. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited FY2025 and three unaudited 2026 quarterly filings give a full statement and debt-note base, with the latest period ended September 30, 2026. | Leverage, liquidity and maturity work can be sourced to filed statements rather than management claims. | High |
| The revolver covenant levels are not printed. Only the senior notes indenture ratios are, as of September 30, 2026. | Headroom on the secured revolver, which matures June 29, 2027, cannot be sized from this pack. | High |
| The 1-for-5 reverse share split is applied in the Q2 and Q3 reports but not in the Q1 report or the 10-K. | Per-share and share-count figures need restating before any cross-period comparison. | High |
| The earnings releases only announce results and point to a website. No presentation is in the pack. | Management adjusted metrics, guidance and presentation claims are unavailable, so the view rests on filings alone. | Medium |

### Readiness view

Overall view: READY_WITH_LIMITATIONS for each of the four selected consumers (CP-1, CP-1A, CP-2, CP-5). No consumer is CONDITIONAL or BLOCKED. No source has blocked preparation, and every source is in the effective set. A missing downstream analytical handoff is not treated as a source condition: the dependency planner sequences CP-1 and CP-1A before CP-2, and CP-2 before CP-5.

Why the view is not READY: the pack holds filed statements and notes only. The evidence chain is statement or note text, then the risk that the credit agreement, indenture covenants and any management presentation are absent, then the consequence that covenant headroom on the revolver, adjusted EBITDA-type measures and management guidance cannot be established from the pack and must be logged as gaps rather than filled.

Why the view is not CONDITIONAL: the Q3 report prints the debt note by class, the maturity table, the indenture covenant tests, liquidity and subsequent events, and the 10-K supplies the audited annual base. The method of each consumer can run on those pages with bounded gaps.

Strongest contrary evidence: the committed revolving facility is the line the filing relies on for cash needs, and the filing says "We are currently exploring our options to extend or refinance our secured revolving credit facility." (Q3 10-Q, page:47). Its covenants and borrowing-base style conditions sit in a credit agreement that is not in the pack, so the consumers that size liquidity must carry that as a limitation.

### Per-source assessment

#### Annual report, FY2025

The 10-K is the audited base. The auditor opinion begins "We have audited the accompanying consolidated balance sheets of Service Properties Trust" (10-K, page:167). The cover gives the share count as "Number of the registrant’s common shares outstanding as of February 23, 2026: 168,061,029." (10-K, page:2). The balance sheet gives "168,070,129 and 166,636,537 shares issued and outstanding" (10-K, page:171). These are before the July 2026 reverse split. Schedule III is headed "(dollars in millions)" (10-K, page:213) while the notes to it say "NOTES TO SCHEDULE III December 31, 2025 (dollars in thousands)" (10-K, page:218). The unit label differs inside the same schedule and must be checked before any Schedule III figure is used.

#### Quarterly reports, Q1 to Q3 2026

All three are unaudited condensed statements and carry a three-month column (Q2 and Q3 also a year-to-date column). Q1 reports "168,054,570 and 168,070,129 shares issued and outstanding" (Q1 10-Q, page:2), which is unadjusted. Q2 reports "129,527,433 and 33,614,025 shares issued and outstanding" (Q2 10-Q, page:2), which is adjusted for the split. The Q3 10-Q states that share information is "retroactively adjusted for the 1-for-5 reverse share split" (Q3 10-Q, page:8) and its equity statement restates the March 31, 2026 balance as 33,610,914 shares (Q3 10-Q, page:3). The Q1 10-Q and the 10-K therefore cannot be combined with Q2 or Q3 share data without a split adjustment.

The Q3 10-Q carries the full statement set. Balance sheet: "Cash and cash equivalents 40,118 346,813" for September 30, 2026 and December 31, 2025 (page:2). Income statement: "Net loss (87,940) (46,945) (462,956) (201,539)" for the three and nine months of 2026 and 2025 (page:3). Cash flow: "Cash paid for interest $ 196,080 $ 239,155" for the nine months (page:5). Segment note: "Segment profit (loss) 36,414 (52,142) (15,728) 47,206 6,909 54,115" for the three months, net lease then hotels then total (page:31). All amounts are in USD thousands.

#### Debt, liquidity and covenants evidence in the Q3 10-Q

Debt note: "Our principal debt obligations at September 30, 2026 were: (1) $1,725,000 aggregate outstanding principal amount of senior unsecured notes" (page:20), with senior secured notes and net lease mortgage notes also stated there. The mortgage note table closes with "Total / weighted average $ 1,347,167 5.80%" (page:22). A per-instrument carrying value and fair value table is on page:33. The maturity table totals "$ 4,652,322" (page:49). Revolver: "we had no amounts outstanding under our revolving credit facility and $650,000 available for borrowing" (page:20), and "The maturity date of our revolving credit facility is June 29, 2027" (page:20). The indenture tests are printed, for example "Total debt / adjusted total assets 53.9% Maximum of 60%" and "Consolidated income available for debt service / debt service 1.83x Minimum of 1.50x" (page:51). The guarantee perimeter is stated: "Our $1,225,000 of senior unsecured notes do not have the benefit of any guarantees." (page:53).

Prior-quarter revolver status for the quarter bridge: the Q2 10-Q reports "$25,000 of borrowings outstanding under our $650,000 revolving credit facility" (Q2 10-Q, page:49), and the Q1 10-Q reports "we had no amounts outstanding under our revolving credit facility and $650,000 available for borrowing" (Q1 10-Q, page:17).

Business facts: "Our net lease properties generated rent coverage of 2.17x and 2.04x as of September 30, 2026 and 2025, respectively." (page:43). Subsequent events through the filing are stated, for example "From October 1, 2026 through November 2, 2026, we sold one net lease property" (page:46). The cover gives "Number of registrant’s common shares of beneficial interest, $.01 par value per share, outstanding as of November 2, 2026: 129,813,906." (page:1).

#### Earnings-release exhibits

The three EX-99.1 files are one-page announcements. Each says the results "can be found at the Quarterly Results section of SVC’s website" (Q3 release, page:1; the same wording is on page:1 of the Q1 and Q2 releases). They contain no income statement, balance sheet, adjusted measure, reconciliation or guidance. The Q3 release adds "SVC also posted an updated investor presentation to its website." (page:1) but the presentation is not in the pack, so its content cannot be used and nothing in this review relies on it. The releases do give portfolio counts, for example "87 hotels with approximately 20,000 guest rooms" at September 30, 2026 (Q3 release, page:1). They are management statements and are subordinate to the filed 10-Q, which reports 87 hotels at September 30, 2026 (Q3 10-Q, page:7).

#### Conflicts

No conflict between sources was found in the items checked. The one difference noted is a unit label, not a conflicting figure: the Schedule III heading in millions against its notes in thousands (10-K, page:213 and page:218). Its downstream effect falls on any consumer that uses Schedule III property data.

#### Version relationships

The three 10-Qs are separate active periodic reports for consecutive quarters, and the 10-K is the annual report. None supersedes another. The Q3 10-Q supersedes the earlier 10-Qs only for facts stated as of September 30, 2026. Prior-period comparatives inside later filings are retained as stated there; this module does not rule which version controls a given fact.

### Consumer assessment

| Consumer | View | Evidence located | Limitations carried |
| --- | --- | --- | --- |
| CP-1 (financial and credit data) | READY_WITH_LIMITATIONS | Statements, debt note by class, maturity table, indenture tests, liquidity and cash flow in the Q3 10-Q; audited base in the 10-K | Revolver covenant levels not supplied; no adjusted EBITDA-type measure outside filings; split-unadjusted share data in the 10-K and Q1 10-Q; Schedule III unit label |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description and operating model in the 10-K; tenant and manager concentration, segment note, related-party notes in the Q3 10-Q | No investor presentation; ownership and sponsor fields in the context are blank; management narrative limited to filing text |
| CP-2 (credit synthesis) | READY_WITH_LIMITATIONS | Depends on CP-1 and CP-1A handoffs, which the planner sequences | Inherits every CP-1 and CP-1A limitation; no ratings in the context |
| CP-5 (evidence trace) | READY_WITH_LIMITATIONS | Depends on settled upstream modules and the pinned pack | Inherits upstream limitations; cannot test claims that rest on documents outside the pack |

### Model objective coverage

For the HTML Model objective the pack holds: discrete three-month columns for each of Q1, Q2 and Q3 2026 and the 2025 comparatives; year-to-date columns in the Q2 and Q3 reports; FY2025 and FY2024 annual statements in the 10-K; a segment note for net lease and hotels; debt by class with carrying and fair values; and cash paid for interest and income taxes (Q3 10-Q, page:5 and the supplemental table after it). Source evidence is sufficient for these. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This module does not assert normalised quarters, reconciliation or downstream input acceptance. A last-twelve-month view and Q4 2025 are not printed as such and would have to be derived downstream from filed columns; that derivation is not performed here.

## Calculations

None. CP-0 does not normalise, reconcile or calculate figures. Every amount quoted above is copied as printed, in USD thousands unless the text states a count, a ratio or a percentage. The following were deliberately not derived: last-twelve-month figures, Q4 2025, net debt, leverage ratios, liquidity totals and covenant headroom. Each is Not calculable in this module because it is a downstream analytical step, not because an input is missing.

## Gaps

| Gap | Severity | Affected consumers | Why it matters | Remediation |
| --- | --- | --- | --- | --- |
| Credit agreement for the $650,000 secured revolver is not in the pack. Financial covenant levels and borrowing conditions are described only in general terms (Q3 10-Q, page:20 and page:21). | High | CP-1, CP-2, CP-5 | Covenant headroom and drawing conditions on the revolver, which matures June 29, 2027, cannot be tested. | Obtain the credit agreement and its amendments, or log headroom as Not calculable. |
| Indentures and supplements for the senior secured and unsecured notes are not in the pack. Only the summary tests on page:51 of the Q3 10-Q are available. | Medium | CP-1, CP-2 | Definitions of adjusted total assets and income available for debt service cannot be checked. | Obtain the indentures if definitions are needed; otherwise cite the printed tests as issuer-reported. |
| Earnings releases carry no figures, adjusted measures or guidance; the Q3 investor presentation is not in the pack. | Medium | CP-1, CP-1A, CP-2 | No management bridge or guidance; slides cannot be inspected from this pack. | Obtain the website results document and presentation if management claims are wanted. |
| Share data is unadjusted for the 1-for-5 reverse split in the 10-K and the Q1 10-Q, and adjusted in the Q2 and Q3 10-Qs. | Medium | CP-1 | Per-share and share-count comparisons across filings are not like for like. | Use split-adjusted amounts from the Q3 10-Q for 2025 and 2026 comparisons, or restate explicitly. |
| Schedule III heading "(dollars in millions)" against notes "(dollars in thousands)" (10-K, page:213 and page:218). | Low | CP-1 | Wrong scale if a Schedule III figure is used. | Check the scale against the balance sheet before use. |
| Context leaves ratings, market capitalisation, net debt, peers and deal terms blank. | Low | CP-2 | No external ratings or market-based cross-check is available. Blank is not zero. | Supply ratings and market data if wanted; otherwise treat as Not supplied. |
| Original HTML tables, charts and images were not inspected; only extracted text was reviewed. This is a text-extraction review, not a fidelity review. | Low | All | Table alignment errors in the extraction are possible. | Check key figures against the statements when used. |
| The dollar scale of the 10-K and 10-Qs is stated in thousands, and the reporting currency of the context is USD. No other currency or period basis was found in the sources. | Low | All | None identified. | None required. |

## Next module

Proceed to CP-1 (financial and credit data) and CP-1A (business and transaction context), then CP-2 and CP-5 in dependency order. All four are READY_WITH_LIMITATIONS. CP-1 should take the Q3 10-Q as the primary source for the September 30, 2026 position and the 10-K for the audited FY2025 base, apply the split adjustment where share data is compared, and record the revolver covenant levels as Not supplied. Do not use the investor presentation referred to in the Q3 release as evidence, because it is not in the pack.
