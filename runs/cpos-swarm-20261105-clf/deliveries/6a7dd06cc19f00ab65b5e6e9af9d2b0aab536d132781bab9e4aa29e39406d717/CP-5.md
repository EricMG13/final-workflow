# CP-5 — Evidence trace and research-integrity QA: CLEVELAND-CLIFFS INC. (clf)

## Request

- Issuer: CLEVELAND-CLIFFS INC. (issuer id `clf`, NYSE: CLF), as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD.
- Run: `clf-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, `minimum` module set. CP-5 checks the four accepted handoffs CP-0, CP-1, CP-1A and CP-2 and grades the result (absorbed CP-5A phase).
- Execution: host session. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called.
- Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- QA envelope: `qa_status` Restricted; Confidence Score 29, band Insufficient Information (from `scripts/confidence_score.py`, see Calculations); `committee_status` Requires More Work.
- Method of checking: every double-quoted span in the four handoffs was searched in the pinned source pages; every CP-1 metric was recomputed from numbers parsed out of the pinned source pages, not from the handoff; statement and table totals were re-added; each Reader summary was compared with its handoff body; CP-0 through CP-2 were read for omissions against the sources. `page:N` is the source chunk number in the pinned `.jsonl` file.

## Sources

Issuer sources checked against (name and pinned sha256):

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_clf-20251231.htm.jsonl | 4c221bc0965bff2fddf7c4bff630fa79a69227de30709426ec9a8c89ce97e2df |
| 10-Q_2026-03-31_clf-20260331.htm.jsonl | cdb78421e299c29e406bbc729a020af9f5e9e2600a8725769f4fc9cce3f48238 |
| 10-Q_2026-06-30_clf-20260630.htm.jsonl | e0ba1bee447b92cbe2b9ad67268169c4ba2e392089bcf206be2b86a11c01f94b |
| 10-Q_2026-09-30_clf-20260930.htm.jsonl | c3188e1da0b49175580c8c9484ba8f4a1c413725f4f518851b880884f79957d1 |
| EX-99.1_2026-04-20_clf-202603318xkex991.htm.jsonl | b9c8fc8d9b4361337a220b73ac602738ac2f0a283bbd73c7b1429c171ac6000c |
| EX-99.1_2026-07-23_clf-202606308xkex991.htm.jsonl | 6e73622f8701012d98293b6d350054a601691c0c525be23eff4b4255d0c4ab32 |
| EX-99.1_2026-10-19_clf-202609308xkex991.htm.jsonl | e6cabc90a6962f04fc1da1253ad4fc1e70365df28408b401d69ed58092c0c0e1 |
| context | 9824d18b9e3851ae3ee2ee1eb294b36a7465c031f02ec1e26c0d1341d4ae46e3 |

Supplied handoffs:

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | a3ac66d14ed58e324a2e51f64f8df6ffab5558cd2acad9a6736446039b68520e |
| CP-1 | febe06aea238831d2c068e9106ca38dc5907ecb1605c542b2cdb6b84313cc844 |
| CP-1A | 310fc2953d3ffb8e3cbbb069d2eb18d26a5197d7f3356b5971f1ef80566e3459 |
| CP-2 | 8a93d4d79d1c6d4fb07c09d4d0d007eee7270ef0afcc24eb4bd2bcf445c83638 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The four handoffs are traceable and agree on every figure checked, but the business and credit views omit the tariff and import dependence behind the 2026 price recovery, so committee use is restricted until that driver is added. | Medium | The same host wrote and checked all four handoffs, so this is a self-review, and no executed debt documents, ratings or later events were available to test. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 41 recomputed metrics and 19 statement tie-outs matched the pinned filings. | Leverage of 7.93x, cover and liquidity can be relied on as issuer-reported figures, subject to the stated definitions. | High |
| Of 115 quotations, 110 are literal matches in the pinned sources; five are table-cell assemblies, an altered quote or a paraphrase in quote marks. | No conclusion rests on a misquote, but five citations need correcting. | High |
| The filings attribute part of the 2026 price recovery to a 50% import tariff regime and low imports, but the business and credit handoffs omit this driver. | Whether earnings hold, and so whether leverage keeps falling below 7.93x, depends on trade policy that the credit view does not name. | Medium |
| Two wordings overstate: the leverage fall was not only from earnings, and the springing test is the only financial covenant, not the only covenant. | Minor; no number changes. | High |
| Expected fourth-quarter debt reduction, the POSCO agreement and the property sale stay unverified, and covenant headroom is Not calculable. | These remain labelled gaps and cannot support a deleveraging conclusion. | High |

### Evidence trace view

The run is traceable enough for a view of the current capital structure and liquidity, and not yet for a view of how durable the earnings recovery is. All figures used downstream reproduce from the pinned filings, quotations are almost always on the cited pages, and the four handoffs agree with each other. The provenance gap that matters most is an omission, not an error: the filings attribute the price recovery partly to import tariffs and low imports, and the business and credit handoffs do not carry that driver, although one summary names trade protection. The affected decision is how far to rely on the 2026 earnings run-rate. Remediation owner: the business-context step, with the located evidence supplied below. Five open minor locator, wording and omission defects need no change to any conclusion.

| Traceability summary | Result |
| --- | --- |
| Quotations checked against the pinned pages | 115 in four handoffs; 110 literal matches; 5 not literal |
| CP-1 metrics recomputed from parsed source numbers | 41 of 41 equal |
| Statement and table totals re-added | 19 of 19 equal |
| Reader summary numbers found in the handoff body | All four; word limits met |
| Material claims by lineage | 5 Directly Sourced, 4 Calculated, 1 Analyst Inference, 2 Insufficient Information |
| Open findings | 1 MATERIAL, 5 MINOR (one further MINOR closed) |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_clf-20251231.htm.jsonl | High: filed, audited annual report | Years ended December 31, 2025, 2024 and 2023 | Cleveland-Cliffs Inc. and subsidiaries, consolidated | Statements, debt note, leases, pensions, commitments, business, legal proceedings | Text extraction; 179 pages, contiguous | CP-0, CP-1, CP-1A |
| S2 | 10-Q_2026-03-31_clf-20260331.htm.jsonl | High: filed, unaudited interim report | Three months ended March 31, 2026 | Same | Interim statements, debt and ABL table, liquidity, strategy text | Text extraction; 58 pages | CP-0, CP-1, CP-1A |
| S3 | 10-Q_2026-06-30_clf-20260630.htm.jsonl | High: filed, unaudited interim report | Three and six months ended June 30, 2026 | Same | Same | Text extraction; 61 pages | CP-0, CP-1, CP-1A |
| S4 | 10-Q_2026-09-30_clf-20260930.htm.jsonl | High: filed, unaudited interim report | Three and nine months ended September 30, 2026 | Same | Same, plus segment, fair value, guarantor information | Text extraction; 63 pages; purchase commitment table absent | CP-0, CP-1, CP-1A |
| S5 | EX-99.1_2026-04-20_clf-202603318xkex991.htm.jsonl | Medium: issuer news release | Q1 2026 | Same | Reported results, outlook, management commentary | Issuer non-GAAP presentation; 9 pages | CP-1, CP-1A |
| S6 | EX-99.1_2026-07-23_clf-202606308xkex991.htm.jsonl | Medium: issuer news release | Q2 2026 | Same | Discrete Q2 figures, outlook | Same; 10 pages | CP-1, CP-1A |
| S7 | EX-99.1_2026-10-19_clf-202609308xkex991.htm.jsonl | Medium: issuer news release | Q3 2026 | Same | Discrete Q2 and Q3 figures, outlook, leverage target | Same; 10 pages; stray character in one cell | CP-1, CP-1A |
| S8 | context | User settings, not evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency | Not issuer evidence; ratings, market data and sponsor blank | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | High leverage, 7.93x total debt to LTM Adjusted EBITDA, falling through earnings | CP-1, CP-2 | Debt principal 7,712 and LTM Adjusted EBITDA 972, both recomputed from sources | Sets default risk and leverage tolerance | Core credit metric | S4 page:15, page:47; S1 page:93, page:131 | Adjusted EBITDA is a management measure with non-cash pension credits |
| 2 | Thin interest cover, 1.84x on cash interest | CP-1, CP-2 | Cash interest 529 from supplemental cash flow notes | Little room for an earnings fall | Debt service capacity | S4 page:9; S1 page:123 | Cash interest excludes finance lease interest |
| 3 | Liquidity 3,246 and back-ended maturities | CP-1, CP-2 | ABL table plus cash; maturity table | Low near-term refinancing risk | Monitoring horizon | S4 page:3, page:15, page:16 | Borrowing base moves with working capital |
| 4 | Earnings recovery depends on steel prices, tariffs and automotive contracts | CP-1A, CP-2 | Price effect and mix in S4; tariff and import facts below | Determines whether leverage keeps falling | Sets durability of the view | S4 page:28, page:29, page:40 | Tariff driver omitted by the handoffs (finding QA-1) |
| 5 | Unverified deleveraging: POSCO, property sale, asset sales | CP-1A, CP-2 | Management statements only | Cannot be counted as repayment | Limits conclusions | S4 page:37, page:38; S7 page:1 | No terms, buyer or price disclosed |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA 972 and leverage 7.93x / 7.85x | CP-1 | S1 page:93; S4 page:47; S2 page:41; S3 page:45; debt tables | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Liquidity 3,246 | CP-1 | ABL tables S1 page:140, S2 page:13, S3 page:15, S4 page:15; balance sheets | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Total debt 7,712 and maturity profile | CP-1 | S4 page:15, page:16 | Yes | High | Directly Sourced | Supported | High | Traced |
| Interest cover 1.84x and 1.61x | CP-1, CP-2 | S1 page:123; S4 page:9, page:4 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Springing covenant not applicable | CP-1 | S4 page:15, page:46; S1 page:139 | Yes | High; management statement of compliance | Directly Sourced | Supported as a statement | Medium | Traced |
| Covenant headroom | CP-1, CP-2 | Trigger level and definitions not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Business mix, fixed price share, labor, vertical integration | CP-1A | S1 page:6, page:12, page:13, page:26, page:58; S4 page:7, page:34 | Yes | High | Directly Sourced | Supported | High | Traced |
| Stelco consideration 3,208 and 2025 debt and equity actions | CP-1A | S1 page:124, page:133, page:134, page:140, page:157 | Yes | High | Directly Sourced | Supported | High | Traced |
| POSCO Memorandum of Understanding non-binding | CP-1A | S4 page:37, page:38 | Yes | High | Directly Sourced | Supported | High | Traced |
| Expected Q4 debt reduction and property sale | CP-1A, CP-2 | S7 page:1 only | Yes, management statement | Medium | Insufficient Information | Open gap, correctly labelled | Low | Gap correctly labelled |
| Leverage 10.80x excluding pension credits | CP-1, CP-2 | S1 page:109; S4 page:4; 223 + 192 - 157 = 258 | Yes | High inputs | Calculated | Supported with label caveat | Medium | Recomputed equal |
| Fundamental credit view, Medium confidence | CP-2 | CP-1 and CP-1A sections | Yes | High inputs | Analyst Inference | Supported by the basis it cites; omits trade-policy driver | Medium | Traced to handoffs |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total principal amount 7,712 | /workspace/secdata/data/2026-11-05/packs/764065-cleveland-cliffs-inc-clf | 10-Q_2026-09-30_clf-20260930.htm | S4 | page:15, Note 7 | CP-1 debt register | Reported | High | Components re-added equal |
| Total Adjusted EBITDA nine months 2026 993; 2025 58 | same | 10-Q_2026-09-30_clf-20260930.htm | S4 | page:47, reconciliation | CP-1 LTM | Issuer non-GAAP | Medium | Reconciliation re-added equal |
| Total Adjusted EBITDA FY2025 37 | same | 10-K_2025-12-31_clf-20251231.htm | S1 | page:93 | CP-1 LTM | Issuer non-GAAP | Medium | Reconciliation re-added equal |
| Interest paid net of capitalized interest 459, 411, 341 | same | 10-K and 10-Q Q3 | S1, S4 | page:123; page:9 | CP-1 cover | Reported | High | Matches |
| Borrowing capacity available 3,169 | same | 10-Q_2026-09-30_clf-20260930.htm | S4 | page:15 | CP-1 liquidity | Reported | High | 4,060 - 834 - 57 equal |
| Stelco total purchase consideration 3,208 | same | 10-K_2025-12-31_clf-20251231.htm | S1 | page:124, NOTE 3 | CP-1A transaction | Reported | High | 2,450 + 343 + 415 equal |
| Direct automotive 30% of 2025 revenue | same | 10-K_2025-12-31_clf-20251231.htm | S1 | page:12 | CP-1A operating model | Reported | High | Matches |
| MinnTac option price 500, expires January 31, 2027 | same | 10-Q_2026-09-30_clf-20260930.htm | S4 | page:20, NOTE 12 | CP-1A transaction | Reported | High | Matches |
| Q4 Adjusted EBITDA outlook about 715; 2027 above 4,000 | same | EX-99.1_2026-10-19_clf-202609308xkex991.htm | S7 | page:3, page:2 | CP-1 events, CP-2 illustrations | Management Language | Medium | Labelled as outlook |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA | CP-1, CP-2 | FY2025, nine months 2026 and 2025; Q1 and six-month comparatives | FY2025 + current - prior | Recomputed from parsed source text: 311, 503, 972 equal | Supported | High | Basis of every ratio | S1 page:93; S2 page:41; S3 page:45; S4 page:47 |
| Total and net leverage | CP-1, CP-2 | Debt principal and cash at each quarter end | Debt / LTM EBITDA; (debt - cash) / LTM EBITDA | Recomputed: 25.20/25.05, 15.45/15.31, 7.93/7.85 equal | Supported | High | Leverage | S1 page:131; S2 page:12; S3 page:15; S4 page:15 |
| Cash interest and cover | CP-1, CP-2 | Supplemental interest paid | FY2025 + current - prior; EBITDA / cash interest | Recomputed: 520, 505, 529; 0.60, 1.00, 1.84 equal | Supported | High | Debt service | S1 page:123; S2 page:8; S3 page:9; S4 page:9 |
| Liquidity | CP-1, CP-2 | Cash and ABL table | Cash + capacity | Recomputed: 3,270, 3,141, 3,084, 3,246 equal | Supported | High | Liquidity | ABL tables |
| Ex-pension-credit leverage | CP-1, CP-2 | Non-service credit 223, 192, 157 | 7,712 / (972 - 258) | Recomputed: 10.80x equal | Supported with label caveat | Medium | Earnings quality | S1 page:109; S4 page:4 |
| CP-2 sensitivities | CP-2 | CP-1 figures, management outlook | See CP-2 Calculations | Recomputed: 45.6%, 0.70x, 26.5%, 8.35x, 2.67x, 1.91x equal | Supported; illustrations labelled | Medium | Headroom | CP-1, CP-2 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial source gate, 1 MATERIAL and 5 open MINOR | Script formula | 29, band Insufficient Information | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | Earnings recovery drivers | The sources tie price strength to import tariffs and low imports; no CP-1A row, CP-1 note or CP-2 risk carries it, yet the CP-1A summary names trade protection | Omission; unsupported summary phrase | The durability of the 7.93x improvement depends on trade policy, which the credit view leaves unnamed | Add a trade-policy row and a CP-2 risk trigger in a later run; evidence is supplied below | CP-1A, CP-2 |
| MINOR | CP-0 table quotations | "Three Months Ended Jun. 30, 2026" and "Total 7,712" are assembled from table header and cell text | Non-literal quote | A parser searching for the quote finds nothing | Quote one row or one cell | CP-0 |
| MINOR | CP-0 calculation row | "Total revenues $ 5,612" cited at page:11; the words are on page:10, page:11 prints the figure in the segment row | Wrong page | Slower verification | Cite page:10 | CP-0 |
| MINOR | CP-1 debt maturities | "Thereafter 4,860" is assembled from table header and cell | Non-literal quote | As above | Quote one cell | CP-1 |
| MINOR | CP-1A quotation | "we intend to utilize it to deleverage our balance sheet" misquotes S1 page:10, which reads "and intend to utilize it to deleverage our balance sheet" | Altered quote | A word was added | Quote exactly | CP-1A |
| MINOR | CP-1A conflict 1 | The 10-K quote spans page:8 and page:9, and the same "permanently close" sentence is also in S4 page:36, so the contradiction exists inside the Q3 10-Q (page:14 against page:36) | Locator and attribution | Understates that the 10-Q itself differs | Add S4 page:36 | CP-1A |
| MINOR | CP-2 paraphrase | "above 4,000" is in quote marks; the source reads "exceed $4 billion" | Paraphrase as quote | A reader could think it a quotation | Remove quote marks | CP-2 |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves by cover text and each page:1 names the filed HTML | A wrong document would change every figure | None found | None |
| Locator precision | Adequate | 110 of 115 quotations literal; 2 page or attribution defects | Slower checks; risk of a misplaced citation | None on conclusions | Exact locators, one cell per quote |
| Calculation reproducibility | Strong | 41 of 41 metrics and 19 of 19 tie-outs recomputed equal from parsed source text | Calculation errors would move leverage | None found | None |
| Cross-module consistency | Strong | CP-2 adds no figure absent from CP-1, CP-1A or its own Calculations; CP-1A states its corrections to CP-0 and CP-1 | Inconsistent figures mislead a committee | None found | None |
| Completeness against sources | Adequate | One material omission (trade policy) and small omissions (market-risk sensitivities) | A missing driver understates how the recovery can reverse | Restricts durability conclusions | Add the omitted rows |
| Reviewer independence | Weak | The host wrote and checked the handoffs | Shared blind spots go undetected, as the pilot showed | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Trade-policy dependence of the price recovery not in the business and credit handoffs | Tariff and import facts exist in S4 page:28, page:29 and S7 page:2; no handoff row | Price is the largest earnings driver; policy change would reverse it | CP-1A summary, CP-2 risk 1 | Restricts durability conclusions | Add a row from S4 page:28 and page:29 |
| G2 | Covenant trigger, fixed charge definition, indentures and credit agreement | Executed documents | Headroom Not calculable | Covenant risk row | Covenant view rests on a management statement | Credit agreement and indentures |
| G3 | Events from October 20, 2026 to 2026-11-05 | Later 8-Ks | View may be stale | Monitoring posture | Lowers currency | EDGAR filings to the cutoff |
| G4 | Property sale, POSCO terms, MinnTac decision | Disclosures not in the pack | Deleveraging and cash calls unquantified | CP-1A, CP-2 | Held as unverified | Later 8-Ks |
| G5 | Ratings, market data, ownership, customer concentration | Not in the pack | No external view | CP-2 | Caps confidence | Rating reports, proxy statement |
| G6 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / clf-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed with 2 MINOR findings | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, LTM, debt, liquidity, claims outside debt | High | Six headings and five report selectors; accepted | Passed with 2 MINOR findings | All metrics recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, transactions, governance | High | Six headings and three selectors; accepted | Restricted: 1 MATERIAL and 2 MINOR findings | Corrects CP-0 and CP-1 in its Sources |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings and two selectors; accepted | Restricted through CP-1A omission; 1 MINOR finding | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A, CP-2 | "Trade protection" in the CP-1A summary; CP-2 risk 1 | Unsupported in the handoff, supported in sources | No body row carries the tariff and import evidence | Add row and risk trigger | Restricts committee use |
| MINOR | CP-0 | Two table-assembled quotations | Supported in substance | Non-literal quote | Quote one cell | None |
| MINOR | CP-0 | Segment revenue row | Supported | Cited page:11, words on page:10 | Cite page:10 | None |
| MINOR | CP-1 | "Thereafter 4,860" | Supported | Non-literal quote | Quote one cell | None |
| MINOR | CP-1A | Deleveraging intention quote | Supported | Word "we" added | Quote exactly | None |
| MINOR | CP-1A | Conflict 1 locators | Supported | Misses S4 page:36 and the page split | Add page:36 | None |
| MINOR | CP-2 | "above 4,000" | Supported by S7 page:2 as "exceed $4 billion" | Paraphrase in quote marks | Remove quote marks | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | "The multiple has fallen ... only because earnings recovered" | Debt principal also fell by 125 between March 31 and September 30, 2026 (7,837 to 7,712); at March debt the Q3 multiple would be 8.06x against 7.93x | None | Say "mainly because" | None |
| MINOR | CP-1 | "the only covenant the sources describe" | The springing fixed charge test is the only financial covenant; the ABL also has affirmative and negative covenants (S1 page:139) | None | Say "only financial covenant" | None |
| MINOR | CP-2 | "guaranteed only by domestic subsidiaries" for the notes | The 6.250% 2040 notes have no subsidiary guarantees (S1 page:136) | None | Add the exception | None |

All 41 CP-1 metrics and all CP-2 sensitivities recomputed equal; no number is wrong.

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1, CP-2 | Covenant headroom and structural ranking | Indentures, ABL credit agreement, Exhibit 22 | Not supplied; claims correctly marked Not calculable or Insufficient Information | Supply documents | Required for headroom and structure |
| MINOR | CP-1 | Redemption terms of the 7.375% 2033 notes | Indenture | Filing text names "7.375% 2029" in the redemption sentence; handoff flags it as unverified | None needed | Required to confirm |
| MINOR | CP-1A, CP-2 | Secured note capacity "approximately $3 billion" | Indentures and ABL | Management statement only | Keep as Management Language | Required for legal capacity |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made; the handoffs state no peer ranking, instrument recommendation or recovery conclusion, and none was found | Prices, spreads, ratings, peers | Outside the minimum pack | Add market data only from sourced material | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A | CP-0 and CP-1 said the property sale was not described in any filed source; CP-1A shows general sell-side processes in S1 page:9 and S2 page:34 and that the Q2 and Q3 10-Qs dropped the wording | Corrections stated in CP-1A Sources; later modules adopt them | None; keep the specific sale as unidentified | None |
| MINOR | CP-1, CP-1A | CP-1 omitted the Stelco employee benefit commitment and the MinnTac option price from claims outside debt | Added in CP-1A and used in CP-2 | None | None |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Differences logged and carried consistently: Q1 availability label, leverage target wording, capex horizons, closure versus idling, Hamilton Works versus Stelco galvanizing | Same wording across modules | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A, CP-2 | Committee readiness | The financial base view is traceable and reproducible; the durability view is missing the trade-policy driver; the review is a self-review | Add the driver and run an independent review | Committee status Requires More Work |
| MINOR | CP-1, CP-1A | Duplication | CP-1A repeats CP-1 figures in its profile table and Calculations by design | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 | Reader summary and Readiness view | None found; Reader summary uses no module codes or hashes and every number appears in the body | None | None |
| MINOR | CP-1 | Report selectors | Five selectors present once each; chart tables use plain numbers and Not supplied reasons | None | None |
| MINOR | CP-1A, CP-2 | Report selectors | Present once each; prose-only selectors contain no table | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MATERIAL | CP-1A, CP-2 | Omission | Trade-policy and import dependence of the price recovery not carried; summary names trade protection without a row | Add row and risk trigger | Restricts committee use | Open |
| QA-2 | MINOR | CP-0, CP-1 | Locator | Three table-assembled quotations and one wrong page for a quote | Quote one cell; cite page:10 | None | Open |
| QA-3 | MINOR | CP-1A | Quotation | Altered quote and incomplete conflict 1 locators | Quote exactly; add S4 page:36 | None | Open |
| QA-4 | MINOR | CP-1 | Wording | "only because" and "only covenant" overstate | Reword | None | Open |
| QA-5 | MINOR | CP-2 | Wording | Paraphrase in quote marks; guarantor description omits the 2040 exception | Reword | None | Open |
| QA-6 | MINOR | CP-1, CP-1A | Omission | Market-risk sensitivities not carried: a 100 basis point change on ABL borrowings of 834 is 8 of annual interest; a 1% Canadian dollar move is 9 of currency exchange; single-source energy supply (S4 page:55) | Add to risk register | None | Open |
| QA-7 | MINOR | CP-0, CP-1 | Imprecision | Property sale and claims-outside-debt statements corrected in CP-1A | None needed | None | Closed |

### Supplemental evidence for the omitted driver

The following located facts are supplied here because the earlier handoffs cannot be edited. In the Q3 10-Q the issuer states that "Finished steel import levels remained significantly below historical levels during the third quarter of 2026, which helped support domestic steel pricing" (S4 page:28). The same page says domestic HRC averaged $1,195 per net ton, "representing a 42% increase compared to the third quarter of 2025". The next page says the President signed a proclamation "to implement 50% tariffs on steel imports originating from all major steel producing countries" during 2025, that an April 2026 proclamation "maintained 50% tariff coverage on steel products", and that "Year-to-date total steel imports through August 2026 declined 15% as compared to the same period in 2025" (S4 page:29). The Q3 release quotes management that "Imports remain well below historical levels" (S7 page:2). The goodwill discussion lists "significant recent shifts in trade policies, including the imposition of tariffs" among conditions that could affect impairment assessments (S4 page:54).

Evidence to risk to implication: the HRC price is the index that most affects revenue and profitability (S4 page:28), the price rise is described as supported by low imports and tariffs, so a change in tariff coverage, an increase in import levels or retaliation would lower price and hence LTM Adjusted EBITDA, on which the 7.93x leverage and 1.84x cash interest cover depend (CP-1). The CP-2 sensitivity that a 45.6% fall in LTM Adjusted EBITDA would take cash interest cover to 1.0x gives the scale. The first observable trigger would be import volumes or HRC price moving against the 2026 level in the next filing. This supplement does not change the credit view; it names a driver the view should carry as a Critical or Material risk trigger.

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Each double-quoted span of 10 or more characters in the four handoffs searched in the pinned page text after normalizing whitespace, case and quote marks | 119 spans parsed; 4 were parser artifacts or labels; of 115 quotations, 110 literal matches and 5 not literal (3 table-cell assemblies, 1 altered quote, 1 paraphrase in quote marks) |
| Q2 | Locator trace | For each quotation on a line that cites a page, the quoted words searched on the cited pages | 2 defects: one wrong page (CP-0 segment row), one incomplete attribution (CP-1A conflict 1); the rest on a cited page or carry a locator on the same line |
| Q3 | Metric recomputation | Inputs parsed from the source pages CP-1 cites (Adjusted EBITDA, debt, cash, cash interest, interest expense, revenue, cash flow, capital expenditure, pension credit, ABL tables); LTM, leverage, cover and liquidity recomputed with exact decimals | 41 of 41 equal to CP-1 |
| Q4 | Tie-outs | Operating cost blocks (FY2025, nine months 2026 and 2025, Q3 2026) and operating income, debt and maturity totals, operating cash flow by quarter, ABL repayment, leases, segment revenue and quarterly revenue re-added | 19 of 19 equal |
| Q5 | Reader summary check | Every number in each Reader summary searched in the rest of its handoff; word counts against the limits | All numbers found; limits met in all four handoffs |
| Q6 | New figures in CP-2 | Numbers in CP-2 body not present in CP-0, CP-1, CP-1A or CP-2 Calculations | None |
| Q7 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:5,Calculated:4,Analyst Inference:1,Insufficient Information:2" --fields-present 17 --fields-total 17 --source-gate partial --findings MATERIAL:1,MINOR:5` | score = clamp((0.6 × 75 + 0.4 × 100) × 0.7 - 30) = 29.5, reported as 29; band Insufficient Information; qa_status Restricted |

Source gate is partial because executed debt documents, ratings and post-October 20, 2026 events are not supplied, although all four modules are accepted and the pack supports the selected scope.

## Gaps

- G1 Material for durability: the trade-policy and import driver is absent from the business and credit handoffs (evidence supplied above).
- G2: covenant trigger, fixed charge definition, indentures and credit agreement not supplied; headroom Not calculable.
- G3: events from October 20, 2026 to 2026-11-05 not supplied.
- G4: property sale, POSCO terms and the MinnTac exercise decision not disclosed.
- G5: ratings, market data, ownership and customer concentration not supplied.
- G6: no independent review; this CP-5 was written by the same host that wrote CP-0 to CP-2.

## Next module

- Report delivery: carry `qa_status` Restricted, Confidence Score 29 (Insufficient Information), committee status Requires More Work, finding QA-1 and gaps G1 to G6. Report the supplemental evidence on trade policy beside the credit view.
- Rerun in a new run folder if the report is to be used for a decision: add a trade-policy row to the business context, a trade-policy trigger to the credit risks, the market-risk sensitivities from S4 page:55, and fix the minor quotation and wording defects.
- Independent review: an independent agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
