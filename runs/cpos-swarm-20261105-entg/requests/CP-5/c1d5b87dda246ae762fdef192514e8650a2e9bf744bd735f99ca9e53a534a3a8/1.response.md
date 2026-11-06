## Request

Issuer: ENTEGRIS INC (issuer id entg), as of 2026-11-05, information cutoff 2026-11-05. Run `entg-2026-11-05-credit_snapshot-host`, pathway credit snapshot, minimum module set. This module checks the evidence trace behind the four accepted handoffs (CP-0, CP-1, CP-1A, CP-2) against the seven pinned sources and grades the result (absorbed CP-5A phase). Execution: host session; the same host wrote the four handoffs, so this is a self-review, not an independent one. No provider was called. QA envelope: `qa_status` Passed; Confidence Score 42, band Low (from `scripts/confidence_score.py`, see Calculations); `committee_status` Requires More Work. Currency USD millions; locators are `page:N` chunk numbers of the pinned extractions.

## Sources

### Issuer sources

| Source (exact name) | sha256 |
| --- | --- |
| `10-K_2025-12-31_entg-20251231.htm.jsonl` | `260dc4cc98d7ad114dcfe1b4d9e49beac9ed9f7c97f27f59e6df3a75c0628528` |
| `10-Q_2026-03-28_entg-20260328.htm.jsonl` | `3b83d32b0eaaaa1280f7799359a8f16448b715b610a83c1edceec0d49387802a` |
| `10-Q_2026-06-27_entg-20260627.htm.jsonl` | `5d06fd99ce42692b479a85d0b3d96bd08dbc1bdd295141cd5adf69b1988058ed` |
| `10-Q_2026-09-26_entg-20260926.htm.jsonl` | `7b5685a1d8fe745548fe7c65968e18c36857c1e4dd7f2b8045f8166b689f4db9` |
| `EX-99.1_2026-04-30_entgq12026ex991.htm.jsonl` | `0e10b62e7e542aab19ae90b6d94252e94c7183b272237a1b5ecd040e7a3bb9d7` |
| `EX-99.1_2026-08-04_entgq22026ex991.htm.jsonl` | `729b6288fa7f91f06fa1d1330da9031db0436138ba5a59730b16535055ac78c0` |
| `EX-99.1_2026-10-29_entgq32026ex991.htm.jsonl` | `e35116403bbcb30c3a986093aa969493d265b238a073d77c0b1aa4aec9296a99` |

Run settings (not issuer evidence): `context`, sha256 `a75dcef49bab6da60dc1054c04d1bf4409ccb60667119c9ab2f0bfc98a4c262f`.

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | `69484fc1896f94421c30f81bc1a11d139a430313a621007d9d0706850a8bf3c8` |
| CP-1 | `82c71de6730d91491596125486a55b1b0f81a9f0dbf34c12db6c3b2214bb379a` |
| CP-1A | `0c9b2ae0de5fe9d086bc58201434c080929ff92cc100e802e3a3b791c6928a72` |
| CP-2 | `c73564e7572c1c6a331890dcde54db01b8476eebd1e290f1a7c7cfd9b5c35358` |

Source abbreviations in locators: `10-K`, `Q1 10-Q`, `Q2 10-Q`, `Q3 10-Q` (quarterly reports for the quarters ended March 28, June 27 and September 26, 2026), `Q1 release`, `Q2 release`, `Q3 release` (Exhibit 99.1 releases of April 30, August 4 and October 29, 2026).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is traceable for the current capital structure and cash flow: every checked figure reproduces from the filings and no quotation is misquoted. It is not committee ready because contract evidence is missing and the review is a self-review. | Medium | Self-review by the same author; five minor locator and definition defects remain open; financing contracts, letters of credit and guarantors are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 41 recomputed financial base values and 31 statement tie-outs matched the filed figures, including leverage of 3.27x, net leverage of 2.91x and cover of 5.57x. | The leverage, cover and cash flow arithmetic can be relied on. | High |
| No quotation from a source was misquoted; five minor defects were found, none changing a conclusion. | Locators need tidying in later runs; no conclusion needs restating. | High |
| Covenant headroom, net revolver availability and guarantor structure are correctly marked as not supplied rather than estimated. | Committee must not rely on headroom or structural priority until the contracts are seen. | High |
| Debt is measured at par; on carrying value total leverage is 3.23x rather than 3.27x. | The definition choice moves leverage only slightly, but should be stated beside the ratio. | High |
| The Confidence Score is 42, band Low, and committee status is Requires More Work. | Use the work as a draft snapshot and seek an independent review. | Medium |

### Evidence trace view

The run is traceable enough for a view of the current capital structure, liquidity and cash flow of Entegris, Inc., and not for a view of covenant headroom, structural priority or market standing. Every derived figure in the four handoffs recomputed from values parsed directly from the cited source chunks, every source quotation was found verbatim, and the figures that CP-2 repeats all appear in CP-1 or CP-1A (the two new sums in CP-2 are declared and recomputed). Coverage of the 13 material claims by strongest lineage: four Directly Sourced, five Calculated, one Analyst Inference and three Insufficient Information. The provenance gaps that matter most are the absence of the executed credit agreement and covenant calculation, the letters of credit under the revolver and the guarantor list: CP-2's assessment, its Medium confidence and its liquidity figure of USD 1,106.5 million rest on them, and each is correctly labelled as a gap in every module. The five defects are minor: one wrong chunk number in CP-0, one in CP-1, omitted or imprecise locators in CP-1 and CP-1A, and a debt-definition choice (par rather than carrying value) that CP-1 discloses. Because the same host wrote and checked the handoffs, shared blind spots, especially omissions, are the main residual risk.

| Traceability summary | Result |
| --- | --- |
| Source quotations checked | 11 source quotations in four handoffs, all found verbatim; 2 quotations of the run context found in the context file; 4 parser artifacts |
| Figures on cited lines | 144 lines carry locators; 112 had every figure on the cited chunk; 32 had a figure not on a cited chunk, of which 7 were genuine locator defects (4 lines in CP-1, 3 in CP-1A) and the rest derived values, cross-chunk sums or a locator notation the script did not parse |
| CP-1 values recomputed from source values | 41 of 41 equal (20 in the leverage, net debt and cover block; 21 in the LTM flow, margin, free cash flow and other ratio block) |
| CP-1A and CP-2 derived values recomputed | 8 of 8 and 1 of 1 equal |
| Statement totals and reconciliations re-added | 31 of 31 equal |
| Material claims by lineage | 4 Directly Sourced, 5 Calculated, 1 Analyst Inference, 3 Insufficient Information |
| Open findings | 5 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_entg-20251231.htm.jsonl | High: filed, audited annual report | Years ended December 31, 2025, 2024 and 2023 | Entegris, Inc. and subsidiaries, consolidated | Statements, debt note, Adjusted EBITDA reconciliation, business, customers, history, exhibits | Text extraction; thousands captions on millions amounts | CP-0, CP-1, CP-1A |
| S2 | 10-Q_2026-03-28_entg-20260328.htm.jsonl | High: filed, unaudited interim report | Three months ended March 28, 2026 | Same | Statements, debt note, revolver amendment as subsequent event | Text extraction; unaudited | CP-1, CP-1A |
| S3 | 10-Q_2026-06-27_entg-20260627.htm.jsonl | High: filed, unaudited interim report | Three and six months ended June 27, 2026 | Same | Statements, debt note, covenant statement, voluntary payment | Text extraction; unaudited | CP-1, CP-1A |
| S4 | 10-Q_2026-09-26_entg-20260926.htm.jsonl | High: filed, unaudited interim report | Three and nine months ended September 26, 2026 | Same | Statements, debt, maturities, liquidity, covenant, non-GAAP, segments | Text extraction; unaudited | All modules |
| S5 | EX-99.1_2026-04-30_entgq12026ex991.htm.jsonl | Medium: issuer press release | Quarter ended March 28, 2026 with comparative columns | Same | Discrete quarters including December 31, 2025 | Management non-GAAP presentation | CP-1 |
| S6 | EX-99.1_2026-08-04_entgq22026ex991.htm.jsonl | Medium: issuer press release | Quarter ended June 27, 2026 | Same | Discrete second quarter | Same | CP-1 |
| S7 | EX-99.1_2026-10-29_entgq32026ex991.htm.jsonl | Medium: issuer press release | Quarter ended September 26, 2026 | Same | Discrete third quarter, fourth-quarter outlook | Outlook is management expectation | CP-1, CP-1A, CP-2 |
| S8 | context | User settings, not evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency, sector label | Not issuer evidence | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Deleveraging to 3.27x total and 2.91x net on Adjusted EBITDA | CP-1, CP-2 | Par debt 3,295.0 and cash 356.5 over LTM Adjusted EBITDA 1,008.2 | Sets leverage tolerance | Core metric | S4 pages 4 and 11; S1 page 85; S4 page 38 | Adjusted EBITDA is management-defined |
| 2 | Free cash flow of 616.0 LTM and cash interest cover of 5.57x | CP-1, CP-2 | Operating cash flow 798.0 less capex 182.0; EBITDA over interest paid 181.1 | Debt service capacity | Supports repayment capacity | S1 page 108; S4 page 7 | Working capital timing support |
| 3 | Customer concentration | CP-1A, CP-2 | TSMC 16% and top ten customers 50% of FY2025 net sales; no long-term purchase commitments | Revenue visibility | Business risk driver | S1 pages 18 and 38 | FY2025 only |
| 4 | 2029 maturity of 2,000.0 | CP-1, CP-2 | 1,600.0 secured notes and 400.0 unsecured notes; 60.7% of par debt | Refinancing concentration | Monitoring horizon | S4 page 11 | Month of maturity not printed |
| 5 | Liquidity of 1,106.5 before letters of credit | CP-1, CP-2 | Cash 356.5 and undrawn commitment 750.0 | Cushion for a downturn | Near-term default risk | S4 pages 4, 12, 34 | Letters of credit not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Par debt 3,295.0 and maturities by year | CP-1 | S4 page 11 | Yes | High | Documentary Fact | Supported | High | Traced |
| Adjusted EBITDA 1,008.2 LTM | CP-1 | S1 page 85; S4 page 38; quarters in S5 to S7 | Yes | High inputs | Calculated | Supported | High | Recomputed equal; quarter sum 228.1 + 226.1 + 250.7 + 303.3 equals it |
| Leverage 3.27x, 2.91x; cover 5.57x | CP-1, CP-2 | Same plus S4 page 7 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Free cash flow 616.0 | CP-1, CP-2 | S1 page 108; S4 page 7 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Liquidity 1,106.5 before letters of credit | CP-1, CP-2 | S4 pages 4, 12, 34 | Yes | High inputs | Calculated | Supported with stated limit | High | Recomputed equal |
| Customer concentration | CP-1A, CP-2 | S1 pages 18, 38 | Yes | High | Documentary Fact | Supported | High | Traced |
| Capital allocation: repayment, dividends, no buybacks | CP-1A, CP-2 | S1 pages 65, 66, 10; S4 page 7 | Yes | High | Documentary Fact | Supported | High | Traced |
| 2026 margin flattered by useful-life change and tariff refunds | CP-1, CP-2 | S4 pages 9, 38 | Yes | High | Documentary Fact | Supported | High | Traced |
| Unit-driven, recurring revenue; intention to repay debt | CP-1A | S1 pages 9 and 10 | Yes | Management statement | Management Language | Supported as a statement, tagged | Medium | Traced, tag kept in CP-2 |
| Equipment and Engineering growth of 66.8% against Fabs 19.3% | CP-1A, CP-2 | S4 page 10 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Covenant headroom | CP-1, CP-2 | Definitions and threshold not in the set | No source exists in the set | Not available | Insufficient Information | Open gap | Low | Gap correctly labelled in all four modules |
| Net revolver availability after letters of credit | CP-1, CP-2 | Letters of credit not in the set | No source exists in the set | Not available | Insufficient Information | Open gap | Low | Gap correctly labelled |
| No creditor-adverse action in the pack | CP-1A, CP-2 | Executed documents not in the set | No source exists in the set | Not available | Insufficient Information | Open gap | Low | Labelled as absence in summaries, not proof |
| Fundamental credit view: improving and adequate | CP-2 | CP-1 and CP-1A rows | Yes, upstream | Mixed | Analyst Inference | Supported by upstream, interpretation | Medium | Tagged Analyst Interpretation |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Par debt 3,295.0 at September 26, 2026 | runs/cpos-swarm-20261105-entg/source-text | 10-Q_2026-09-26 | S4 | page:11, Note 5 | CP-1 debt table | Reported | High | Instruments re-added equal |
| Adjusted EBITDA FY2025 886.2 and FY2024 931.1 | same | 10-K_2025-12-31 | S1 | page:85, reconciliation | CP-1 metrics | Issuer non-GAAP | Medium | Reconciliation re-added equal |
| Adjusted EBITDA nine months 2026 780.1 and 2025 658.1 | same | 10-Q_2026-09-26 | S4 | page:38 | CP-1 metrics | Issuer non-GAAP | Medium | Reconciliation re-added equal |
| Interest paid FY2025 185.4; nine months 90.4 and 94.7 | same | 10-K_2025-12-31; 10-Q_2026-09-26 | S1, S4 | page:108; page:7 | CP-1 interest cover | Reported | High | Matches |
| Revolver commitment 750.0, no borrowings | same | 10-Q_2026-09-26 | S4 | page:12 and page:34 | CP-1 liquidity | Reported | High | Matches |
| Covenant 5.20 to 1.00 | same | 10-Q_2026-09-26 | S4 | page:34 | CP-1 covenants | Reported description | High | Threshold not printed |
| TSMC 16%, top ten 50% | same | 10-K_2025-12-31 | S1 | page:18 | CP-1A customers | Reported | High | Matches |
| Q4 2025 discrete column, Adjusted EBITDA 228.1 | same | EX-99.1_2026-04-30 | S5 | page:7 | CP-1 discrete quarters | Issuer non-GAAP | Medium | Equals FY2025 less nine months 2025 |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA | CP-1 C1, C1a; CP-2 | FY2025, nine and six months | FY2025 + year-to-date 2026 − year-to-date 2025 | Recomputed: 1,008.2 and 925.6 equal | Supported | High | Basis of every ratio | S1 p85; S4 p38; S3 p35 |
| Leverage and net debt ratios | CP-1 C5; CP-2 | Par debt, cash, LTM Adjusted EBITDA | Debt / EBITDA; (debt − cash) / EBITDA | Recomputed for four periods: equal | Supported | High | Leverage | S1 p105, p120; S4 p4, p11; S3 p4, p11 |
| Cash interest cover | CP-1 C5; CP-2 | Interest paid LTM 181.1 | EBITDA / interest paid | Recomputed: 4.67x, 4.78x, 4.88x, 5.57x equal | Supported | High | Debt service | S1 p108; S3 p7; S4 p7 |
| Free cash flow | CP-1 C4; CP-2 | Operating cash flow less capex | CFO − acquisition of property, plant and equipment | Recomputed: 316.1, 396.2, 262.2, 482.0, 616.0 equal | Supported | High | Cash generation | S1 p108; S4 p7 |
| LTM flows | CP-1 C2 | Eleven statement lines | FY2025 + nine months 2026 − nine months 2025 | Recomputed: equal | Supported | High | Basis of LTM columns | S1 p106 to p108; S4 p5, p7 |
| Unadjusted EBITDA and leverage on it | CP-1 C3; CP-2 | Operating income, depreciation, amortization | Sum; debt / sum | Recomputed: 982.1 and 3.36x equal | Supported | High | Definition sensitivity | S1 p106, p107; S4 p5, p7 |
| Illustrative first lien net leverage 1.23x | CP-1 C8; CP-2 | Assumption that the 1,600.0 secured notes are first lien debt and cash is fully netted | (1,600.0 − 356.5) / 1,008.2 | Recomputed equal; assumption-based, not covenant | Supported as illustration only | Low | Not headroom | S4 p4, p11 |
| Annual note coupons 161.3 | CP-1 C9; CP-2 | Par amounts and fixed rates | Sum of par × rate | Recomputed: 161.25 equal | Supported | High | Debt service | S4 p11; S1 p120 |
| Segment, category and geography ties | CP-1, CP-1A | Printed tables | Re-added to totals | Equal | Supported | High | Mix | S4 p10, p15, p23 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial source gate, 5 MINOR | Script formula | 42, band Low | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 covenant compliance in the Q1 10-Q | Cited as chunk 27; the sentence is on chunk 28 | Wrong locator | A reader checking chunk 27 does not find it; CP-1 states the correction | Cite chunk 28 | CP-0 source review table |
| MINOR | CP-1 share-based compensation of 54.8 | Cited to Q3 10-Q chunk 38; the figure is in the cash flow statement on chunk 7 | Wrong locator | Slower verification; value correct | Cite chunk 7 | CP-1 definition review |
| MINOR | CP-1 debt table and carrying-value sentence; C1a input | First table row shows 1,600.0 and 4.75% with locators to the exhibit list only; the sentence on carrying value cites only the fair value chunk; C1a omits the source of 886.2 | Omitted or imprecise locator | Values are correct and located elsewhere in the handoff | Cite chunk 11 of the Q3 10-Q and chunk 85 of the 10-K beside the figures | CP-1 capital structure and calculations |
| MINOR | CP-1A FY2025 capex of 299.2, the 24.6% sales growth in the business view and the USD 0.10 dividend | Figures stated without a locator on the line (10-K chunk 108; Q3 10-Q chunk 23) or with a neighbouring chunk (dividend cited at chunk 66, stated on chunk 65) | Omitted locator | Slower verification | Add locators | CP-1A operating model and business view |
| MINOR | CP-1 leverage basis | Total debt measured at par (3,295.0) while the canon prefers balance-sheet carrying value (3,260.6); delta 34.4 | Definition choice, disclosed | On carrying value total leverage is 3.23x and net leverage 2.88x, against 3.27x and 2.91x | Show carrying-value ratios beside par ratios in a later run | CP-1 chart data, CP-2 findings |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Seven sources pinned by sha256; filings identify themselves by cover text and period | A wrong document would shift every figure | None found | None |
| Locator precision | Adequate | 112 of 144 cited lines fully matched; of the 32 others, 7 were genuine defects and the rest derived or cross-chunk values | Slower checks | None on conclusions | Exact chunk locators beside every figure |
| Calculation reproducibility | Strong | 41 of 41 CP-1, 8 of 8 CP-1A and 1 of 1 CP-2 derived values and 31 of 31 tie-outs recomputed equal from parsed source values | Errors would move leverage | None found | None |
| Cross-module consistency | Strong | Every CP-2 figure except two declared sums appears in CP-1, CP-1A or CP-0; CP-1 and CP-1A cite the current upstream hashes | Inconsistent figures mislead a committee | None found | None |
| Management language handling | Adequate | Unit-driven revenue and debt repayment intention are tagged Management Language in CP-1A and CP-2; outlook and Capital Markets Day labelled as expectation | Management claims adopted as fact | None found | None |
| Reviewer independence | Weak | The host wrote and checked all handoffs | Shared blind spots, especially omissions, go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant ratio, utilisation threshold and covenant EBITDA | Executed credit agreement and compliance certificate | Headroom Not calculable | CP-1 covenants, CP-2 monitoring | Covenant view rests on a management statement | Credit agreement and April 29, 2026 amendment |
| G2 | Letters of credit under the revolver | Letter-of-credit balance | Liquidity of 1,106.5 is an upper bound | CP-1 liquidity, CP-2 | Lowers liquidity confidence | Credit agreement notices or later filing |
| G3 | Guarantors, collateral and executed indentures | Subsidiary list, indentures, intercreditor agreement | Structural priority unknown | CP-1A, CP-2 creditor control | Holds structural view open | EX-21 and exhibits listed in the 10-K |
| G4 | Ratings and holder detail | Agency reports, proxy statement | Market view and control rights unknown | CP-1A, CP-2 | Minor | External sources |
| G5 | Events after October 29, 2026 | Later filings | Final week before the cutoff unknown | Monitoring posture | Lowers currency | EDGAR filings to the cutoff |
| G6 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / entg-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed with one MINOR locator finding | READY_WITH_LIMITATIONS |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, LTM, debt, liquidity, covenants | High | Six headings; accepted | Passed with three MINOR findings | All values recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, transaction, governance | High | Six headings; accepted | Passed with one MINOR locator finding | Management Language tagged |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Passed, no finding | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 | Q1 10-Q covenant compliance | Supported | Chunk 27 cited, sentence on chunk 28 | Cite chunk 28 | None |
| MINOR | CP-1 | Share-based compensation 54.8 | Supported | Cited to chunk 38, figure on chunk 7 | Cite chunk 7 | None |
| MINOR | CP-1 | Debt table row, carrying value sentence, C1a input | Supported | Figures without adjacent locators | Add locators | None |
| MINOR | CP-1A | Capex 299.2, growth 24.6%, dividend of USD 0.10 | Supported | Locators omitted or one chunk off | Add or correct locators | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Total debt in leverage | Par rather than carrying value; delta 34.4, effect 0.04x on total and 0.03x on net leverage | None | Show both bases | None |
| MINOR | CP-1 | Adjusted EBITDA as denominator | Management-defined; does not add back share-based compensation; difference from unadjusted EBITDA 2.9 for nine months 2026 and 40.6 for FY2025 | None | Keep unadjusted ratio beside it, as CP-1 does | None |
| MINOR | CP-1 | Illustrative first lien net leverage 1.23x | Assumes secured notes are first lien debt; covenant definition not supplied | None | Keep labelled as illustration, as CP-1 and CP-2 do | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1, CP-1A, CP-2 | Covenant level 5.20 to 1.00, springing test; incremental capacity of the greater of USD 1.1 billion or 100% of EBITDA; equal priority liens | Credit agreement, indentures, intercreditor agreement | Descriptions only; documents not supplied; claims correctly stated as descriptions | Supply documents before any headroom or priority view | Required before structural conclusions |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made; fair value of debt appears only as a filed figure in CP-1 | Prices, spreads, ratings, peers | Not part of the minimum pack | Add market data only with sourced inputs | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1 | CP-0 gap on the fourth quarter of 2025 not being presented on its own was corrected in CP-1, which found the discrete column in the Q1 release | CP-1 states the correction; CP-0 cannot be edited | Read CP-1 alongside CP-0 | None |
| MINOR | CP-0, CP-1 | CP-0 chunk 27 for Q1 compliance corrected to chunk 28 in CP-1 | Same | Same | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | Current-structure, liquidity and cash flow view is traceable; covenant headroom, net revolver availability and structural priority are not; review is self-review only | Supply contracts and obtain an independent review | Committee status Requires More Work |
| MINOR | CP-1, CP-1A | Duplication | CP-1A repeats CP-1 figures by design (par debt, LTM Adjusted EBITDA); values agree | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Chart data tables | None found: four selectors present once each with the required headers; values plain numbers; the three maturity cells printed as dashes are shown as 0.0 with the printed total as basis | None | None |
| MINOR | CP-1A, CP-2 | Report selectors | None found: tables and prose-only sections as specified | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-0 | Locator | Q1 10-Q compliance sentence cited at chunk 27, is on chunk 28 | Cite chunk 28 | None | Open, corrected in CP-1 |
| QA-2 | MINOR | CP-1 | Locator | Share-based compensation 54.8 cited to chunk 38, is on chunk 7 | Cite chunk 7 | None | Open |
| QA-3 | MINOR | CP-1 | Locator | Figures without adjacent locators in debt table row, carrying-value sentence and C1a | Add locators | None | Open |
| QA-4 | MINOR | CP-1A | Locator | Capex 299.2 and growth 24.6% stated without locators; dividend of USD 0.10 cited at chunk 66, stated on chunk 65 | Add or correct locators | None | Open |
| QA-5 | MINOR | CP-1 | Definition | Par debt used for leverage; carrying-value ratios 3.23x and 2.88x not shown | Show both bases | None | Open |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Every double-quoted phrase in the four handoffs searched in the seven source files and the context file after normalising quotes and spacing | 17 spans parsed; 4 were parser artifacts (fragments or search terms); 2 quoted the run context sector label, found in the context file; 11 source quotations, all found verbatim |
| Q2 | Locator check | A script compared each figure on every line with a locator against the cited chunks (144 lines) | 112 lines fully matched; 32 had a figure not on a cited chunk; manual review classed 7 as genuine locator defects (QA-2, QA-3 and QA-4; 4 lines in CP-1 and 3 in CP-1A) and the other 25 as derived values, sums across chunks, or notation the script could not parse |
| Q3 | Metric recomputation | Inputs parsed from the source chunks by label; LTM and ratios recomputed with exact fractions | CP-1: 41 of 41 equal (LTM Adjusted EBITDA 1,008.2 and 925.6; LTM interest paid 181.1 and 189.7; net debt 3,715.8, 3,384.6, 3,141.4 and 2,938.5; total leverage 4.34x, 4.23x, 3.78x, 3.27x; net leverage 3.99x, 3.82x, 3.39x, 2.91x; cover 4.67x, 4.78x, 4.88x, 5.57x; eleven LTM statement lines; margin 28.6%; free cash flow ratios 7.8%, 10.6%, 18.7%; unadjusted leverage 3.36x; expense cover 5.27x; first lien illustration 1.23x; interest gap 52.5; accrual build 40.6; fair value ratio 96.4%). CP-1A: 8 of 8 equal (growth 66.8%, 19.3%, 24.6%; shares 58.6%, 19.1%; cost ratios 50.3%, 56.5%; segment share 87.4%). CP-2: 393.4 equal |
| Q4 | Tie-outs | Statement totals, debt tables, maturity rows, segment and geography tables, Adjusted EBITDA reconciliations, quarter sums, cash flow bridge and coupons re-added | 31 of 31 equal |
| Q5 | Cross-module figures | Numbers in CP-2 compared with those in CP-0, CP-1 and CP-1A; numbers in the four reader summaries compared with the rest of their own handoff | CP-2: only 222.6 and 393.4 are new, both declared in its Calculations; all reader summary figures appear in the body; no module code or hash appears in a reader summary |
| Q6 | Par against carrying value | 3,260.6 / 1,008.2; (3,260.6 − 356.5) / 1,008.2 | 3.23x; 2.88x |
| Q7 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:4,Calculated:5,Analyst Inference:1,Insufficient Information:3" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:5` | E 68.46, C 100, S 0.7, P 15: score = clamp((0.6 × 68.46 + 0.4 × 100) × 0.7 − 15) = 41.75, rounded to 42; band Low; qa_status Passed |

## Gaps

- G1 Material for the decision: covenant ratio, threshold and covenant EBITDA are not supplied, so headroom is Not calculable.
- G2 Material: letters of credit under the revolver are not supplied, so liquidity of USD 1,106.5 million is an upper bound.
- G3 Material: guarantors, collateral and executed indentures are not supplied.
- G4 and G5: ratings, holder detail and events after October 29, 2026 are not supplied.
- G6: no independent review; this CP-5 was written by the same host that wrote the handoffs it checks. A script check cannot find omissions, which a self-review is least likely to find.
- Readiness: the upstream modules are READY_WITH_LIMITATIONS and all four were accepted at the first attempt.

## Next module

- Report delivery: carry `qa_status` Passed, Confidence Score 42 (Low), committee status Requires More Work, and gaps G1 to G3.
- Swarm review step: an independent agent or model should repeat this check, starting with omissions and with the generated 10-K to 10-Q consistency of debt, lease and covenant statements.
- Sourcing: obtain the credit agreement, the April 29, 2026 revolver amendment, the indentures, the subsidiary list and a compliance certificate, then rerun CP-1, CP-2 and CP-5 in a new run folder; apply the five minor corrections (QA-1 to QA-5) in that run.
