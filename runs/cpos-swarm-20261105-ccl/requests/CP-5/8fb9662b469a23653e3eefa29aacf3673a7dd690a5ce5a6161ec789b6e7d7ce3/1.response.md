## Request

Evidence trace and research integrity QA (CP-5 with CP-5A) for Carnival Corp Ltd. (issuer id ccl), as of 2026-11-05, pathway credit_snapshot, run ccl-2026-11-05-credit_snapshot-host. Scope: Top 5 material credit drivers across the four accepted handoffs (CP-0, CP-1, CP-1A, CP-2), traced to the pinned sources, with calculation, legal, market, cross-module and handoff checks and a clearance decision. This module changes no credit conclusion and repairs no lineage silently.

## Sources

### Issuer sources traced

| Alias | Exact source name | sha256 |
| --- | --- | --- |
| 10-K | 10-K_2025-11-30_ccl-20251130.htm.jsonl | 319fc4f2d973f28d585a1955a2d440c02d8b1b6dbc0973c191e2363a73060526 |
| Q1 10-Q | 10-Q_2026-02-28_ccl-20260228.htm.jsonl | 618bcc494da0b2893a6d142c3d1a9bab122d817be7203e48a24415f7863a4619 |
| Q2 10-Q | 10-Q_2026-05-31_ccl-20260531.htm.jsonl | 7f4c931117646bfadf44441c2cfafd9c06b54d8efce3cf617ece0b76c9969691 |
| Q3 10-Q | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | d3735109439ee392b1d7fba90666d820b500bbba0c767539cc84776ce14477e7 |
| Q1 release | EX-99.1_2026-03-27_a20261qearningsrelease8-k.htm.jsonl | 30b7e2e340d9ff04fd374426ee85a1b23f2a0ad36a11daf5d191cd2b3b5e65b3 |
| Q2 release | EX-99.1_2026-06-23_a20262qearningsrelease8-k.htm.jsonl | 5b3125d03084066ceb1281134ac06b53a255fd76fa75628f167339ceb2fd622a |
| Q3 release | EX-99.1_2026-09-29_a20263qearningsrelease8-k.htm.jsonl | a4d2ebb65632ec32cdeeba0842dfc488f9c01a40330706395f7804c9f49dd751 |

### Run context

| Source | sha256 | Role |
| --- | --- | --- |
| context | 0ae02699c3e76f28ddabed001602c70760df4bfe5d4037c1d00e74d8c149ab79 | Dated run settings. Not issuer evidence. Ratings, quotes, peers, deal terms and legal documents are blank or none in it. |

### Handoffs audited

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 81f58a8d0f2ad55a3b1e80b1f1daf6e29ce8a917e87841c474eb01e0d80a4f24 | Source readiness |
| CP-1 | 464c9de32de8fce38eb134451b0f942c49ff86e27b5659c99e70bd137a32ea7a | Financial base |
| CP-1A | e6bdf4e8a0bd7f9bc2074387f01e5f1005e099ab84dc85660b5d32b8e2059665 | Business and transaction context |
| CP-2 | 35934a3f93672a733a2dbf1e43d797b19d2e1726a301f906c69499c99ef7d2bc | Fundamental credit synthesis |

Locators are `<alias> page:N`, the extracted chunk number of the pinned text file, not the printed page.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Traceability is good but needs remediation: the sampled figures all match their source pages, yet leverage rests on unadjusted EBITDA and legal structure rests on summary notes, so committee use should be restricted. | Medium | Debt documents, covenant ratios, rating levels and fiscal 2025 adjusted EBITDA are absent, so those claims cannot be traced to a primary source. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 86 sampled figures and quotations match the cited source pages. | The numbers a committee reads can be relied on as reported. | High |
| Leverage and coverage use unadjusted EBITDA, which differs from the company's own measure and from covenant definitions. | Headline leverage is not comparable with the company's 3.1x or with covenant headroom. | High |
| Claims about security and guarantee releases and ranking rest on summary notes, not debt documents. | Ranking and creditor protection conclusions stay provisional until legal review. | High |
| Management statements on bookings, ratings and targets are attributed to management in the earlier work. | A committee can separate reported results from management claims. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 1 is calculated, 0 are assumption-based, 2 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. A sample of 86 figures and quotations from the four handoffs was found on the cited source pages with no mismatch. The most important provenance gap is that the debt documents and fiscal 2025 adjusted EBITDA are not in the pack, which matters because leverage, covenant headroom and creditor ranking can then only be stated on unadjusted or summary evidence, and implies committee use is restricted until those documents are obtained.

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 7. Committee Use: Restricted.

qa_status is Restricted and committee_status is Restricted, so the confidence band is Low under the Restricted cap (score at or below 59). A numeric confidence score was not computed here because the scoring script is not available to this run.

### Source register

Module status: Ready with Limitations. Traceability scope: Top 5.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-11-30_ccl-20251130.htm.jsonl | Filed, audited annual report | Fiscal year ended November 30, 2025 | Carnival Corporation & plc (joint registrants) | Statements, debt note, covenants, leases, pensions, business description | Combined perimeter; no adjusted EBITDA | Fiscal 2025 base for all handoffs |
| S2 | 10-Q_2026-02-28_ccl-20260228.htm.jsonl | Filed, unaudited interim report | Quarter ended February 28, 2026 | Carnival Corporation & plc | Statements, debt, liquidity, commitments | Combined perimeter; cash interest not printed | LTM construction, liquidity point |
| S3 | 10-Q_2026-05-31_ccl-20260531.htm.jsonl | Filed, unaudited interim report | Quarter and six months ended May 31, 2026 | Carnival Corporation Ltd. | Statements, debt, liquidity, DLC unification | Cash interest not printed | LTM construction, liquidity point |
| S4 | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | Filed, unaudited interim report | Quarter and nine months ended August 31, 2026 | Carnival Corporation Ltd. | Statements, debt table, maturities, covenants, segments, obligor group | Covenant ratios not printed; no issuer or guarantor by instrument | Current-period base for all handoffs |
| S5 | EX-99.1_2026-03-27_a20261qearningsrelease8-k.htm.jsonl | Furnished management release | First quarter 2026 | Carnival Corporation & plc | Adjusted EBITDA, PROPEL targets, buyback | Management language; possible graphics not in text | First quarter adjusted EBITDA, targets |
| S6 | EX-99.1_2026-06-23_a20262qearningsrelease8-k.htm.jsonl | Furnished management release | Second quarter 2026 | Carnival Corporation Ltd. | Adjusted EBITDA, net debt to adjusted EBITDA ratio, rating statement, ship order | Management language | Company leverage figure |
| S7 | EX-99.1_2026-09-29_a20263qearningsrelease8-k.htm.jsonl | Furnished management release | Third quarter 2026 and guidance | Carnival Corporation Ltd. | Adjusted EBITDA reconciliation, customer deposits, guidance, rating and redemption statements | Management language; guidance is a forecast | Company adjusted EBITDA, guidance |
| S8 | context | Run settings, not evidence | As of 2026-11-05 | Carnival Corp Ltd. | Currency, periods, blank ratings and quotes | Not issuer evidence | Scope only |

### Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Debt-led deleveraging with flat EBITDA: total debt 24,559; total debt / EBITDA 3.36x; net debt / EBITDA 3.19x against 3.77x and 3.50x at fiscal 2025 | CP-1 | Debt table and statements | Leverage tolerance and refinancing depend on whether EBITDA grows or repayment continues | Sets the credit view | Q3 10-Q page:9, page:2; 10-K page:79, page:63 | EBITDA is unadjusted; company measure not rebuildable |
| 2 | Liquidity of 5,720 and maturity profile (13,295 due through 2030; 2,036 current) | CP-1 | Cash, revolver availability, maturity table | Debt service and refinancing capacity | Near-term safety and refinancing dependence | Q3 10-Q page:2, page:10, page:25 | Revolver usage by letters of credit not printed; rating levels absent |
| 3 | Capital allocation against deleveraging: distributions of 1,547 in nine months, ship commitments of 18.3 billion, management targets | CP-1, CP-1A, CP-2 | Cash flow, commitments, release targets | Discretionary cash leaves before maturities | Decides pace of leverage reduction | Q3 10-Q page:3, page:13, page:28; Q1 release page:3 | Targets are management language; restricted payment terms not supplied |
| 4 | Deposit-funded seasonal business model with no loss-of-earnings insurance | CP-1A | Revenue mix, deposits, seasonality, insurance statement | Cash flow shocks in the peak quarter are uninsured | Downside severity | 10-K page:19, page:14; Q3 10-Q page:2, page:8; Q3 release page:9 | Refundable share of deposits not split |
| 5 | Structure after unification: all debt unsecured, subsidiary guarantees released, obligor group earns under half of revenue | CP-1, CP-1A, CP-2 | Debt table footnotes, obligor summary | Creditor ranking and structural claims | Ranking and protection | Q3 10-Q page:9, page:10, page:26; Q3 release page:3 | Debt documents and guarantor lists absent; cause of releases unknown |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debt-led deleveraging with flat EBITDA | CP-1 | Operating income 4,483 and 3,678, depreciation 2,790 and 2,172, debt 27,383 and 24,559 (sources above) | Yes | Filed statements | Calculated | Reproduced by recomputation | Medium | Remediation Needed |
| Liquidity and maturity profile | CP-1 | "$4.5 billion available for borrowing under the Revolving Facility"; maturity table (Q3 10-Q page:10) | Yes | Filed note | Directly Sourced | Verified on page | High | Committee-Ready |
| Capital allocation against deleveraging | CP-1, CP-1A, CP-2 | Dividends 618, repurchases 929 (Q3 10-Q page:3); commitments (Q3 10-Q page:13); targets (Q1 release page:3) | Yes | Filed and management | Analyst Inference | Facts verified; the competing-claims reading is interpretation | Medium | Remediation Needed |
| Deposit-funded seasonal model, uninsured | CP-1A | "We do not carry coverage related to loss of earnings or revenues" (10-K page:19) | Yes | Filed annual report | Directly Sourced | Verified on page | High | Committee-Ready |
| Structure after unification | CP-1, CP-1A, CP-2 | "no longer secured"; footnote (f) on guarantees (Q3 10-Q page:10) | Yes | Filed note | Analyst Inference | Facts verified; the reduced-protection reading is interpretation | Medium | Remediation Needed |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 24,559 at August 31, 2026 | packs/815097-carnival-corp-ltd-ccl/10-Q_2026-08-31_ccl-20260831.htm | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | S4 | page:9, Note 3 | CP-1 Debt schedule | Sourced | Filed | Foots to 24,559 |
| Total debt 27,383 at November 30, 2025 | packs/815097-carnival-corp-ltd-ccl/10-K_2025-11-30_ccl-20251130.htm | 10-K_2025-11-30_ccl-20251130.htm.jsonl | S1 | page:79, Note 5 | CP-1 Chart data: leverage | Sourced | Filed, audited | Maturity table sums to 27,382 (source rounding) |
| Operating income 2,220 and 3,678; revenue 8,435 and 21,263 | packs/.../10-Q_2026-08-31_ccl-20260831.htm | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | S4 | page:2 | CP-1 Financials and credit metrics | Sourced | Filed | Quarter and nine-month columns |
| Fuel expense 615 against 451 | packs/.../10-Q_2026-08-31_ccl-20260831.htm | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | S4 | page:2 | CP-1 Financial base view | Sourced | Filed | Direction verified |
| Cash 1,220; revolver 4.5 billion; liquidity 5.7 billion | packs/.../10-Q_2026-08-31_ccl-20260831.htm | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | S4 | page:2, page:10, page:25 | CP-1 Chart data: liquidity | Sourced | Filed | Revolver printed to 0.1 billion |
| Scheduled maturities 301, 2,517, 3,961, 3,631, 2,885, 11,264 | packs/.../10-Q_2026-08-31_ccl-20260831.htm | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | S4 | page:10 | CP-1 Chart data: debt maturities | Sourced | Filed | Sum 24,559 |
| Covenant levels: 3.0 to 1.0 coverage, 5.0 billion, 65 percent, 1.5 billion | packs/.../10-Q_2026-08-31_ccl-20260831.htm | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | S4 | page:10 | CP-1 Covenants | Sourced | Filed summary | Definitions in agreements not supplied |
| Notes no longer secured; guarantees released | packs/.../10-Q_2026-08-31_ccl-20260831.htm | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | S4 | page:10, notes (c), (d), (f) | CP-1 Capital structure; CP-1A Transaction summary | Sourced | Filed | Dates of guarantee releases not stated |
| "does not have any remaining secured debt" | packs/.../a20263qearningsrelease8-k.htm | EX-99.1_2026-09-29_a20263qearningsrelease8-k.htm.jsonl | S7 | page:3 | CP-1 Capital structure | Sourced (management) | Furnished | Attributed to management in CP-1 |
| Obligor group revenue 9,636 against 21,263 consolidated | packs/.../10-Q_2026-08-31_ccl-20260831.htm | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | S4 | page:26, page:2 | CP-1 Perimeter | Sourced; share calculated | Filed | 45.3 percent calculated |
| Ship commitments 0.3, 1.6, 1.5, 1.8, 1.7, 11.4 billion | packs/.../10-Q_2026-08-31_ccl-20260831.htm | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | S4 | page:13, Note 4 | CP-1 Claims outside the debt figure | Sourced; total calculated | Filed | 18.3 billion is a sum of rounded figures |
| Dividends 618, repurchases 929; 1,562 remaining | packs/.../10-Q_2026-08-31_ccl-20260831.htm | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | S4 | page:3, page:28 | CP-1 Cash flow and capital returns | Sourced | Filed | Release states nearly 1.2 billion (conflict logged) |
| Distribute more than 40 percent of cash from operations; 2.75x target | packs/.../a20261qearningsrelease8-k.htm | EX-99.1_2026-03-27_a20261qearningsrelease8-k.htm.jsonl | S5 | page:3 | CP-1A Capital allocation | Management Language | Furnished | Attributed |
| Net debt to adjusted EBITDA ratio of 3.1x | packs/.../a20262qearningsrelease8-k.htm | EX-99.1_2026-06-23_a20262qearningsrelease8-k.htm.jsonl | S6 | page:3 | CP-1 Chart data: leverage | Management Language | Furnished | Definition differs across releases |
| Adjusted EBITDA 2,993 quarter, 5,842 nine months | packs/.../a20263qearningsrelease8-k.htm | EX-99.1_2026-09-29_a20263qearningsrelease8-k.htm.jsonl | S7 | page:10 | CP-1 Financials and credit metrics | Sourced (management) | Furnished | Not the metric used for ratios |
| No loss-of-earnings insurance | packs/.../10-K_2025-11-30_ccl-20251130.htm | 10-K_2025-11-30_ccl-20251130.htm.jsonl | S1 | page:19 | CP-1A Company and operating model | Sourced | Filed, audited | Fiscal 2025 statement |
| Ticket 13,825 and onboard 7,438 revenue | packs/.../10-Q_2026-08-31_ccl-20260831.htm | 10-Q_2026-08-31_ccl-20260831.htm.jsonl | S4 | page:2 | CP-1A Company and operating model | Sourced; shares calculated | Filed | 65.0 and 35.0 percent calculated |
| Unification completed May 2026; Bermuda | packs/.../10-Q_2026-05-31_ccl-20260531.htm | 10-Q_2026-05-31_ccl-20260531.htm.jsonl | S3 | page:5 | CP-1A Transaction summary | Sourced | Filed | Repeated in S4 page:5 |
| Moody's upgrade; S&P upgrade, second investment grade rating | packs/.../a20262qearningsrelease8-k.htm | EX-99.1_2026-06-23_a20262qearningsrelease8-k.htm.jsonl | S6, S7 | S6 page:3; S7 page:3 | CP-1A Transaction summary; CP-2 | Management Language | Furnished | Levels not supplied |
| Customer deposits 7,639 | packs/.../a20263qearningsrelease8-k.htm | EX-99.1_2026-09-29_a20263qearningsrelease8-k.htm.jsonl | S7 | page:9 | CP-1 Financials and credit metrics | Sourced | Furnished | Refundable portion not split |
| Fiscal 2025 refinancing: six note series, 4.5 billion revolver, 11.6 billion prepaid | packs/.../10-K_2025-11-30_ccl-20251130.htm | 10-K_2025-11-30_ccl-20251130.htm.jsonl | S1 | page:80, page:81 | CP-1A Transaction summary | Sourced | Filed, audited | Verified |

### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM EBITDA to August 31, 2026 (unadjusted) | CP-1 leverage chart, CP-2 | 4,483 + 2,790; 3,678 + 2,172; 3,748 + 2,064 | (FY2025 operating income + D&A) + (nine months 2026) - (nine months 2025) = 7,273 + 5,850 - 5,812 = 7,311, USD million, LTM to 2026-08-31, no normalization | Calculated | Reproduced exactly | High | Leverage, coverage | 10-K page:63; Q3 10-Q page:2 |
| Total debt / EBITDA | CP-1, CP-2 | 24,559; 7,311 | 24,559 / 7,311 = 3.36; principal debt before issuance costs | Calculated | Reproduced exactly | Medium | Leverage | Q3 10-Q page:9 |
| Net debt / EBITDA | CP-1, CP-2 | 24,559 - 1,220 = 23,339; 7,311 | 23,339 / 7,311 = 3.19; cash and cash equivalents only, restricted cash excluded | Calculated | Reproduced exactly | Medium | Leverage | Q3 10-Q page:2, page:9 |
| Fiscal 2025 leverage | CP-1 | 27,383; 25,455; 7,273 | 3.77 and 3.50 | Calculated | Reproduced exactly | Medium | Leverage trend | 10-K page:63, page:79 |
| EBITDA / accrual interest | CP-1 | 7,311; 1,177 | 6.21; interest net of capitalized interest, LTM | Calculated | Reproduced exactly | Medium | Coverage | 10-K page:63; Q3 10-Q page:2 |
| FY2025 EBITDA / cash interest | CP-1, CP-2 | 7,273; 1.2 billion printed to 0.1 billion | 7,273 / 1,200 = 6.06, range 5.82 to 6.32 | Calculated | Reproduced; range disclosed | Medium | Coverage | 10-K page:63, page:98 |
| Liquidity | CP-1, CP-2 | 1,220; 4,500 | 5,720 against printed 5.7 billion | Calculated | Reproduced; ties to printed | High | Liquidity | Q3 10-Q page:2, page:10, page:25 |
| Principal through 2030 | CP-2 | 301; 2,517; 3,961; 3,631; 2,885 | Sum 13,295; 13,295 / 3,176 = 4.19x | Calculated | Reproduced exactly | Medium | Refinancing | Q3 10-Q page:10 |
| LTM cash from operations less capital expenditure | CP-1, CP-2 | 6,218 + 5,303 - 4,700; 3,611 + 2,139 - 2,105 | 6,821 - 3,645 = 3,176; not a company-defined free cash flow | Calculated | Reproduced exactly | Medium | Cash flow | 10-K page:64; Q3 10-Q page:3 |
| Illustration of 2.75x | CP-2 | 23,339; 7,311; 2.75 | 3,234 net debt reduction at constant EBITDA, or EBITDA of 8,487 at constant net debt | Calculated on assumption that target applies to unadjusted EBITDA | Reproduced; assumption disclosed | Low | Leverage tolerance | Q1 release page:3 |
| Shareholder returns share | CP-1, CP-2 | 618 + 929; 3,164 | 1,547 / 3,164 = 48.9 percent | Calculated | Reproduced exactly | Medium | Capital allocation | Q3 10-Q page:3 |
| Debt to capital (book) | CP-1 | 23,912; 14,207; 26,640; 12,284 | 62.7 percent and 68.4 percent; not the contract definition | Calculated | Reproduced; caveat disclosed | Low | Covenant proxy | Q3 10-Q page:2, page:3; 10-K page:64 |
| Obligor group revenue share | CP-1, CP-1A, CP-2 | 9,636; 21,263; 12,910; 26,622 | 45.3 and 48.5 percent | Calculated | Reproduced exactly | Medium | Structure | Q3 10-Q page:26, page:2 |
| Guarantee category reclassification | CP-1 | 13,764; 1,244; ten footnote (f) lines | 12,520 against 12,521 | Calculated | Reproduced; 1 rounding | Medium | Structure | Q3 10-Q page:9; 10-K page:79 |

### Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Net debt to EBITDA of 3.19x and total debt to EBITDA of 3.36x | Headline leverage is on unadjusted EBITDA (operating income plus D&A), which differs from the company's adjusted EBITDA and from the covenant definition; CP-2 first states the ratio without the "unadjusted" label | Calculated | A committee could read the ratio as comparable with the company's 3.1x or with covenant tests, misjudging deleveraging progress and headroom | Label the basis wherever the ratio is cited; obtain fiscal 2025 adjusted EBITDA and rebuild | CP-2 Reader summary and Credit view; CP-1 Chart data: leverage |
| Material | Release of security and guarantees reduces protection for some holders; ranking not assessable | Conclusion rests on a summary note and a management release; no indenture, guarantee or release clause is supplied | Analyst Inference | Creditor rights and ranking drive loss given default; without clauses the direction and size of the effect are unknown | Obtain debt documents and the guarantor list; legal review | CP-1 Capital structure; CP-1A governance table; CP-2 Key findings |
| Minor | Debt and cash reductions between May 31, 2026 and August 31, 2026 | The May 31, 2026 comparators are cited only in a chart table; the Financial base view sentence cites Q3 pages only | Directly Sourced | Reader cannot check the quarter's change from the sentence | Add Q2 10-Q page:10 and page:2 to the sentence | CP-1 Financial base view |
| Minor | Security and guarantees were released "while ratings rose" | Releases are not dated in the sources; the ratings statements are dated (Q2 release page:3; Q3 release page:3) | Weak Lineage | A causal or timing link may be inferred that the sources do not show | Rephrase as coincident only where dated | CP-1A Reader summary |
| Minor | Book debt to capital of 68.4 percent at fiscal 2025 | Shown next to a 65 percent covenant limit while compliance is stated | Calculated | May be read as a breach; caveat is present but the figure is prominent | Move the figure to a footnote or remove | CP-1 Covenants |
| Minor | "diversified across eight brands and two segments" | The filing has four reportable segments (Q3 10-Q page:16) | Directly Sourced | Loose wording | Use four reportable segments | CP-2 Strengths and weaknesses |
| Minor | "strong and improving", "diversified" | Adjectives used in CP-2 summary lines | Analyst Inference | Style discipline; supported by figures in the same section | Replace with the supporting figures | CP-2 Reader summary |
| Minor | Repeated figures and conflicts across handoffs | The same conflict log items appear in CP-0 and CP-1A, and figures recur in CP-1, CP-1A and CP-2 | Directly Sourced | Dilutes committee reading | Cross-refer instead of repeating | CP-0, CP-1A, CP-2 |
| Minor | Handoff envelope | The four handoffs carry the six transport headings and no YAML front matter or evidence trace heading | Directly Sourced | Under the Markdown transport the envelope fields are owned by CP-OS, so the effect is limited | None needed in this run | All four handoffs |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | 7 filed or furnished sources cover statements, debt, covenants, liquidity, segments; no debt documents or ratings | Missing primary legal and rating evidence leaves ranking and headroom on summary notes | Committee use restricted for structure and covenant conclusions | Obtain debt documents, rating publications, fiscal 2025 adjusted EBITDA |
| Citation completeness | Ready with Remediation | 86 sampled figures and quotations found on the cited pages; one sentence with incomplete citations | Reader cannot check one quarter change | Low | Add the two locators |
| Calculation traceability | Committee-Ready | 14 calculation items reproduced with formula, inputs, period and unit | Definition drift is disclosed in CP-1 but not labelled in every CP-2 sentence | Medium, covered by the Material flag | Label basis in CP-2 |
| Assumption transparency | Committee-Ready | 2.75x illustration, rounded cash interest range, perimeter judgment all disclosed | Assumptions are visible and bounded | Low | None |
| Markdown artifact integrity | Ready with Remediation | Six transport headings present in all handoffs; no YAML envelope | Envelope fields are owned by CP-OS | Limited | None needed in this run |

Overall auditability follows the lowest dimension: Ready with Remediation.

### Audit lane results

#### Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | ccl-2026-11-05-credit_snapshot-host; sha256 81f58a8d0f2a... | Source readiness for 7 sources | Filed and furnished | Six transport headings present; no YAML envelope | Passed | No issue found |
| CP-1 | ccl-2026-11-05-credit_snapshot-host; sha256 464c9de32de8... | Financial base, fiscal 2025 to August 31, 2026 | Filed statements and notes | Six transport headings present; selectors present | Restricted | Material flag on leverage basis |
| CP-1A | ccl-2026-11-05-credit_snapshot-host; sha256 e6bdf4e8a0bd... | Business and transaction context | Filed and furnished | Six transport headings present; selectors present | Restricted | Legal dependency; one minor coupling |
| CP-2 | ccl-2026-11-05-credit_snapshot-host; sha256 35934a3f9367... | Credit synthesis | Upstream only | Six transport headings present; selectors present | Restricted | Basis label and wording |

#### Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Financial base view: debt reduction of 1,011 and cash reduction of 1,023 since May 31, 2026 | Partially Supported | Sentence cites Q3 pages only; the Q2 comparators are in the chart table | Add Q2 10-Q page:10 and page:2 | Monitoring Follow-Up |
| Minor | CP-1A | Reader summary: releases occurred "while ratings rose" | Partially Supported | Release dates are not stated | Rephrase | Monitoring Follow-Up |

#### Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Leverage 3.36x and 3.19x | Unadjusted EBITDA (operating income + D&A) against company adjusted EBITDA and covenant EBITDA | The company prints 3.1x at May 31, 2026 on an unsupplied adjusted LTM EBITDA; its net debt definition also changes between releases (Q1 release page:13; Q2 release page:13) | Label basis in every citation; obtain fiscal 2025 adjusted EBITDA | Restricts Committee Use |
| Minor | CP-1 | Book debt to capital 62.7 and 68.4 percent | Not the contractual definition | The 10-K states compliance at 65 percent limit (10-K page:82) | Footnote or remove | Monitoring Follow-Up |

#### Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-1A, CP-2 | Security and subsidiary guarantees were released; protection for those holders is lower; ranking by entity not assessable | Indentures, guarantee and release clauses, revolver agreement, guarantor list | None of these is in the pack; the context states legal documents none | Obtain documents; state the claim as interpretation until then | Legal review required; the analyst interpretation is separate from the contractual provision, which is not seen |

#### Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | CP-0, CP-1, CP-1A, CP-2 | No market, price, spread, yield or relative-value claim is made; no peer ranking | Context quotes and peers are blank | Not required because no such claim is made | None | No effect on committee use |

#### Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A, CP-2 | CP-2 refers to "two segments"; CP-1 and CP-1A cite four reportable segments, with two cruise segments | None; same sources | Align wording | None on figures |

Other shared data points agree across the four handoffs: debt 24,559, cash 1,220, liquidity 5,720, LTM EBITDA 7,311, ratios 3.36x and 3.19x, ship commitments 18.3 billion, obligor share 45.3 percent, and the logged conflicts on repurchases, net debt definition and equity presentation. Issuer name, as-of date, run id and currency are the same in all four.

#### Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Promotional or Non-Credit Language | "strong and improving" and "diversified" used as adjectives in summary lines, each supported by figures in the same section | Replace with the supporting figures | Low |
| Minor | CP-0, CP-1, CP-1A, CP-2 | Duplicative or Immaterial Content | Conflicts and headline figures repeat across handoffs | Cross-refer | Low |

#### Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A, CP-2 | YAML front matter and evidence trace heading | Absent; the Markdown transport requires six headings and CP-OS owns envelope fields | None needed in this run | None; each handoff was consumed by the next module with hashes matching |

### Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-1, CP-2 | Formula / Definition Drift | Leverage on unadjusted EBITDA is not labelled at first citation in CP-2 and differs from the company's adjusted measure and covenant EBITDA | Label basis; obtain fiscal 2025 adjusted EBITDA | Restricts Committee Use | Open |
| CP5-002 | Material | CP-1, CP-1A, CP-2 | Legal Support Gap | Security and guarantee release effects and ranking are stated without debt documents | Obtain documents; present as interpretation | Requires Legal Review | Open |
| CP5-003 | Minor | CP-1 | Citation Gap | May 31, 2026 comparators not cited in the Financial base view sentence | Add locators | Monitoring Follow-Up | Open |
| CP5-004 | Minor | CP-1A | Partially Supported Claim | "while ratings rose" coupling is not dated | Rephrase | Monitoring Follow-Up | Open |
| CP5-005 | Minor | CP-1 | Formula / Definition Drift | Book debt to capital shown against a contractual 65 percent limit | Footnote or remove | Monitoring Follow-Up | Open |
| CP5-006 | Minor | CP-2 | Cross-Module Inconsistency | "two segments" against four reportable segments | Align wording | Formatting / Hygiene Only | Open |
| CP5-007 | Minor | CP-2 | Promotional or Non-Credit Language | Adjectives in summary lines | Replace with figures | Formatting / Hygiene Only | Open |
| CP5-008 | Minor | CP-0, CP-1, CP-1A, CP-2 | Duplicative / Immaterial Content | Repeated figures and conflicts | Cross-refer | Formatting / Hygiene Only | Open |
| CP5-009 | Minor | CP-0, CP-1, CP-1A, CP-2 | canonical Markdown Handoff Integrity Defect | No YAML envelope or evidence trace heading under the transport | None needed in this run | Formatting / Hygiene Only | Open |

### Remediation priority map

Must-fix before committee: CP5-001 label the leverage basis as unadjusted wherever cited and obtain fiscal 2025 adjusted EBITDA; CP5-002 obtain the revolver agreement, indentures, guarantee and release clauses and the guarantor list, and treat release effects as interpretation until reviewed.

Must-fix before canonical Markdown handoff is consumed downstream: None.

Monitoring follow-up: CP5-003 add the two locators; CP5-004 rephrase the rating coupling; CP5-005 footnote or remove the book debt to capital figure; re-audit when documents or filings after September 29, 2026 arrive.

Formatting / hygiene: CP5-006 align the segment wording; CP5-007 replace adjectives with figures; CP5-008 cross-refer repeated items; CP5-009 none needed.

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 7. Committee Use: Restricted.

No finding changes the credit conclusion, and every sampled figure traces to its source page. The two Material issues (CP5-001 and CP5-002) must be disclosed for committee use: leverage is on an unadjusted basis, and creditor ranking and release effects are not assessable without debt documents.

## Calculations

Independent recomputation from the pinned sources (inputs read from the cited pages, not from the handoffs):

| Check | Inputs and locators | Result | Handoff value | Outcome |
| --- | --- | --- | --- | --- |
| FY2025 EBITDA | 4,483 + 2,790 (10-K page:63) | 7,273 | 7,273 | Reproduced |
| Nine months 2026 and 2025 EBITDA | 3,678 + 2,172; 3,748 + 2,064 (Q3 10-Q page:2) | 5,850; 5,812 | 5,850; 5,812 | Reproduced |
| LTM EBITDA | 7,273 + 5,850 - 5,812 | 7,311 | 7,311 | Reproduced |
| First quarter and six-month LTM | 7,273 + 1,303 - 1,197 (Q1 10-Q page:2); 7,273 + 2,877 - 2,823 (Q2 10-Q page:2) | 7,379; 7,327 | 7,379; 7,327 | Reproduced |
| Total debt / EBITDA | 27,383 / 7,273; 26,004 / 7,379; 25,570 / 7,327; 24,559 / 7,311 | 3.77; 3.52; 3.49; 3.36 | Same | Reproduced |
| Net debt / EBITDA | (27,383 - 1,928) / 7,273; (26,004 - 1,424) / 7,379; (25,570 - 2,243) / 7,327; (24,559 - 1,220) / 7,311 | 3.50; 3.33; 3.18; 3.19 | Same | Reproduced |
| Debt table foots | 10,953 + 13,606 (Q3 10-Q page:9) | 24,559 | 24,559 | Reproduced |
| Maturities foot | 301 + 2,517 + 3,961 + 3,631 + 2,885 + 11,264 (Q3 10-Q page:10) | 24,559 | 24,559 | Reproduced |
| Liquidity | 1,220 + 4,500 | 5,720 | 5,720 | Reproduced |
| Principal through 2030 and relative to LTM cash flow | 13,295; 13,295 / 3,176 | 13,295; 4.19 | Same | Reproduced |
| Quarter adjusted EBITDA ties to nine months | 1,267 (Q1 release page:11) + 1,582 (Q2 release page:10) + 2,993 (Q3 release page:10) | 5,842 | 5,842 (Q3 release page:10) | Reproduced |
| Sampled figures and quotations found on the cited pages | 56 headline figures and 30 supporting figures and quotations checked by text search against the page named in the handoff | 86 of 86 found | Not applicable | No mismatch |

The 86 checks are a sample and not an exhaustive check of every figure; every derived number in the registers above was recomputed.

## Gaps

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Debt documents and guarantor lists | Indentures, revolver agreement, guarantee and release clauses | Ranking, covenant definitions and the cause of releases decide creditor protection and loss given default | Structure claims in CP-1, CP-1A, CP-2 are interpretation | High impact | Executed debt documents |
| CP-5-GAP-002 | Fiscal 2025 adjusted EBITDA and fourth quarter 2025 | Fourth quarter 2025 earnings release | The company's own leverage cannot be rebuilt | Leverage is unadjusted | High impact | Fourth quarter 2025 earnings release |
| CP-5-GAP-003 | Covenant ratios | Compliance certificates or reported ratios | Headroom cannot be measured | Covenant section is proxy and compliance statements only | Medium impact | Facility compliance information |
| CP-5-GAP-004 | Rating levels and outlooks | Agency publications | Revolver pricing and market access cannot be sized | Refinancing view is qualitative | Medium impact | Rating agency reports |
| CP-5-GAP-005 | Interim cash interest paid | Quarterly cash flow supplement | Cash interest cover exists for fiscal 2025 only | Coverage is accrual-based for interim periods | Medium impact | Company supplemental data |
| CP-5-GAP-006 | Filings after September 29, 2026 | Form S-3 status, post-quarter repurchases, later events | Net debt after the quarter may differ | No filing in the pack is dated after September 29, 2026, about five weeks before the cutoff | Medium impact | Filing list to November 5, 2026 |
| CP-5-GAP-007 | Graphics in earnings releases not inspected | Images under Advance Sales and Capital Allocation headings | Booking curve content is not read | None on figures cited | Low impact | Original release exhibits |
| CP-5-GAP-008 | Refundable share of customer deposits | Breakdown not printed | Cash call under a demand shock cannot be sized | Liquidity stress not quantified | Low impact | Company disclosure if available |
| CP-5-GAP-009 | Numeric confidence score and scripted completeness and envelope checks | The scoring, completeness and envelope validation scripts are not available to this run | The band is set by the Restricted cap and not by a computed score | Confidence band stated without a score | Low impact | Run the scripts in the CP-OS toolchain |

## Next module

This is the last module in the requested set, so the report can be assembled from the accepted handoffs. Before committee use, apply the two Material remediations (label the leverage basis; obtain the debt documents and fiscal 2025 adjusted EBITDA) and re-run this audit when those documents or any filing dated after September 29, 2026 arrive.
