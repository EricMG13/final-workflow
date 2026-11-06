## Request

Module CP-5 (evidence trace validation with the research-integrity grade) for TRANSALTA CORP (issuer id tac, TransAlta Corporation and subsidiaries), as of 2026-11-05, cutoff 2026-11-05. Pathway credit_snapshot, reporting currency CAD, current period Q3 2026, prior period FY2025. The reader question is whether the analysis is traceable enough for a committee decision and which provenance gap matters most. Scope is the Top 5 credit drivers plus every figure that two or more handoffs share. The review is independent of the author: each driver was re-opened in the retained Q3 release, and the key ratios were recomputed from the printed inputs. It changes no upstream conclusion and repairs no lineage silently; where a handoff is wrong or overstated, the defect is logged and the earlier handoff stays as accepted. No numeric confidence score is computed here because the scoring script is not part of this transport; the QA status and committee status are stated with reasons.

## Sources

### Issuer sources relied on

| Short name | Exact name | sha256 |
| --- | --- | --- |
| Q3 release | 6-K-EX-99.1_2026-11-03_q32026newsreleasecombined.htm.jsonl | 4a5154cd49419e37e9331d492d10dca95a118322f6bfb6d110e3d5c77d11c75e |
| Q2 release | 6-K-EX-99.1_2026-07-31_q22026newsreleasecombined.htm.jsonl | 6517eb0175389824e2dbf8ed01f28c9ed380ca26fb5f07df6426985d4637070b |
| Q1 release | 6-K-EX-99.1_2026-05-06_q12026newsreleasecombined.htm.jsonl | d77c128beb98e2437eea81e4016d41f6df7e8423fe8e2c62937d63154e11b8b4 |
| 40-F | 40-F_2025-12-31_tac-20251231_d2.htm.jsonl | b63199bf5537d0e75a2ebecac96b19dc805f7429906c75e8842f8eebec31d328 |
| Q3 MD&A | 6-K-EX-99.2_2026-09-30_a20260930tacex992mda.htm.jsonl | da5d3b9a14d1f4629b51ce9b284f3347ecb5867ab9fb86b1f0ad3a5f6a8c9267 |
| Q2 MD&A | 6-K-EX-99.2_2026-06-30_a20260630tacex992mda.htm.jsonl | 485b1665b7c8e9772076589eaca23e22bc7e6e99c60259c137d99f66a46a0e8c |
| Q1 MD&A | 6-K-EX-99.2_2026-03-31_a20260331tacex992mda.htm.jsonl | 825154ea09ce104089ded78858b6df4a99000ad1f2700c2f48ae4e03f8fb77c2 |

### Supplied handoffs

| Module | sha256 | Role in this review |
| --- | --- | --- |
| CP-0 | e649beec406ce7c4f934a5470672343568948805478270034136ec0060a7db24 | Source readiness; re-anchored for source identity, page counts and limits |
| CP-1 | 71e5320148085be3260b4ae0d87da56d2570b0349c017fe905a360f73feab8a7 | Financial base; every table row and calculation re-opened or recomputed |
| CP-1A | 9c6fd1dc6de0dbc116a3ba5a4f208156d53ce129274cb308b66f5fa8f6f5ba0f | Business and transaction facts; quotes and locators re-opened |
| CP-2 | ae322a884569224e44514ab919f21777a132fd6dee16499c1b2894df042024cb | Credit synthesis; each figure matched to CP-1 or CP-1A |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is largely traceable: every checked figure matches the Q3 release, and the leverage, cover and liquidity calculations recompute. One unsupported statement and several overstatements need correction before committee use, which should be restricted. | Medium | Covenant levels, instrument terms, audited FY2025 statements and transaction agreements are not in the sources, so those conclusions cannot be traced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every sampled financial figure matched the Q3 release, and all derived ratios recompute, including 4.19 and 3.85 times and 3.80 times cover. | Financial base figures can be relied on as stated. | High |
| The business handoff says the company keeps control of the Oklahoma wind portfolio after the 49 per cent sale; the source says only that it provides operational oversight. | Control and consolidation of those assets are unconfirmed. | High |
| The restricted-cash figures of 100 and 84 remain unreconciled in every handoff that uses them. | Cash available to the parent is uncertain. | Medium |
| The assumed US$750 million of Colorado project debt is described as backed by contracted assets without a source for security or ranking. | Ranking against group creditors is not supported. | Medium |
| Covenant headroom and instrument ranking cannot be traced because the legal documents are absent. | Committee conclusions on structure should be treated as limited. | High |

### Evidence trace view

Committee use is restricted. The financial base is well traced: sampled figures in the earnings, balance sheet, cash flow, debt, facility and maturity tables agree with the Q3 release, the ratios recompute from printed inputs, and the figures shared across the three analytical handoffs are identical. Traceability weakens where the analysis moves from facts to mechanisms about structure: the Oklahoma control statement, the description of the assumed Colorado debt as asset-backed, and the contracted status of Far North in the synthesis lack a source in the handoffs that make them. Those are bounded defects, none changes the leverage, liquidity or earnings conclusions, and each has a stated fix. The most material provenance gap is absence of covenant, indenture and transaction documents, which limits structural conclusions however carefully the figures are traced.

### Traceability summary

| Measure | Result |
| --- | --- |
| Handoffs reviewed | 4 |
| Top drivers traced | 5 of 5 |
| Reported rows of the financial base table checked against the Q3 release | 33 of 33 agree |
| Ratios and sums recomputed | 20 of 20 agree |
| Unsupported or overstated statements | 3 (1 material, 2 minor), plus presentation points |
| Open conflicts | 3 logged, none reconciled by the sources |

### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q3 release | 6-K-EX-99.1_2026-11-03_q32026newsreleasecombined.htm.jsonl | High (filed Form 6-K exhibit; unaudited interim statements) | Q3 2026 and nine months to Sept. 30, 2026 | TransAlta Corporation, consolidated | Statements, notes, MD&A, non-IFRS reconciliations, subsequent events | Unaudited; management measures; no legal documents | Primary evidence for all drivers |
| Q2 release | 6-K-EX-99.1_2026-07-31_q22026newsreleasecombined.htm.jsonl | High (same family) | Q2 2026 and six months | Same | June 30 balances, facilities, six-month cash flow | Unaudited | Trend rows |
| Q1 release | 6-K-EX-99.1_2026-05-06_q12026newsreleasecombined.htm.jsonl | High (same family) | Q1 2026 | Same | March 31 balances, facilities, Far North contracting footnote | Unaudited | Trend rows |
| 40-F | 40-F_2025-12-31_tac-20251231_d2.htm.jsonl | High for identity only | FY2025 | TransAlta Corporation | Cover, controls, auditor | Annual statements are incorporated by reference, not supplied | Identity and auditor |
| Q3 MD&A | 6-K-EX-99.2_2026-09-30_a20260930tacex992mda.htm.jsonl | High (contained in Q3 release) | Q3 2026 | Same | MD&A text only | Duplicate content | Cross-check only |
| Q2 MD&A | 6-K-EX-99.2_2026-06-30_a20260630tacex992mda.htm.jsonl | High (contained in Q2 release) | Q2 2026 | Same | MD&A text only | Duplicate content | Cross-check only |
| Q1 MD&A | 6-K-EX-99.2_2026-03-31_a20260331tacex992mda.htm.jsonl | High (contained in Q1 release) | Q1 2026 | Same | MD&A text only | Duplicate content | Cross-check only |

Module status: Ready with Limitations. Traceability scope: Top 5.

### Top five credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage above target because last-four-quarter Adjusted EBITDA fell | CP-1, CP-2 | Reported 4.1 times against 4.0 times; Adjusted EBITDA 1,006 against 1,104; Adjusted Net Debt 4,121 | Denominator decline, not debt, moved the ratio | Little room for further earnings weakness | Q3 release page:40 | Management-defined measures |
| 2 | Liquidity of 1,867 with no cash drawings | CP-1, CP-2 | Facility table and liquidity rebuild | Supports near-term refinancing | Low near-term risk | Q3 release page:14, page:39, page:89 | Some cash restricted; 60 in Heartland facilities |
| 3 | Alberta merchant exposure and hedge cover | CP-1A, CP-2 | 61 per cent of capacity, 77 per cent merchant, hedges 9,364 GWh and 6,732 GWh | Largest earnings swing factor | Visibility to 2027 only | Q3 release page:12, page:24 | Hedge terms beyond 2027 absent |
| 4 | October 2026 transactions and assumed project debt | CP-1, CP-1A, CP-2 | US$750 million assumed; US$305 million proceeds | Changes debt after the balance sheet date | Pro forma leverage not calculable | Q3 release page:5, page:98 | No acquired earnings or debt terms |
| 5 | Centralia Order costs and recovery | CP-1, CP-1A, CP-2 | 27 in Q3 and 38 in nine months excluded from Adjusted EBITDA; FERC rejected two petitions | Cash cost excluded from the headline measure | Leverage understated if costs continue | Q3 release page:54, page:56, page:65 | Pre-2026 Order costs absent |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reported leverage 4.1 times | CP-1 | Adjusted Net Debt table | Yes | High | Directly Sourced | Supported | High | Traced |
| Calculated total and net leverage 4.19 and 3.85 times | CP-1 | Balance sheet debt plus exchangeable securities; cash | Yes | High | Calculated | Supported | High | Recomputed |
| Interest cover 3.80 times nine months | CP-1 | Reconciliation EBITDA; cash interest paid | Yes | High | Calculated | Supported | High | Recomputed |
| Liquidity 1,867 | CP-1 | Facility table plus cash | Yes | High | Directly Sourced and Calculated | Supported | High | Recomputed to the reported figure |
| Maturity profile | CP-1 | Maturity table | Yes | High | Directly Sourced | Supported | High | Traced; 34 difference to carrying value unexplained in the source |
| Alberta merchant exposure and hedges | CP-1A | Description and Outlook hedging table | Yes | High | Directly Sourced | Supported | High | Traced |
| Colorado acquisition and assumed debt | CP-1A | Note 18 | Yes | High | Directly Sourced | Supported for facts; overstated for security | Medium | Partly traced |
| Oklahoma sale | CP-1A | Page 5 and Note 18 | Yes | High | Directly Sourced | Supported for facts; control statement unsupported | Medium | Partly traced |
| Credit thesis | CP-2 | CP-1 and CP-1A rows | Yes | Medium | Analyst Interpretation | Supported by upstream | Medium | Traced to upstream |
| Structure not assessable | CP-1, CP-2 | Absence of legal documents | Yes (CP-0) | High | Insufficient Information | Supported | High | Gap, correctly stated |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenues 536, 615, 1,588 and 1,806 | source-text | Q3 release file | Q3 release | page:67 | CP-1 Financials and credit metrics | Statement | High | Agrees |
| Cash interest paid 85, 67, 200 and 205 | source-text | Q3 release file | Q3 release | page:71 | CP-1 Financials and credit metrics | Statement | High | Agrees |
| Available liquidity 1,867 | source-text | Q3 release file | Q3 release | page:14 and page:39 | CP-1 Liquidity | MD&A | High | Agrees with rebuild |
| Facility table | source-text | Q3 release file | Q3 release | page:89 | CP-1 Liquidity by facility | Note | High | Bilateral drawn cell blank in extraction; nil is implied and disclosed |
| Maturity table | source-text | Q3 release file | Q3 release | page:87 | CP-1 Chart data: debt maturities | Note | High | Agrees |
| Restricted cash 100 and 84 | source-text | Q3 release file | Q3 release | page:40 and page:90 | CP-0, CP-1, CP-1A, CP-2 | Conflict | High | Logged consistently |
| Capacity, contracting, Alberta exposure | source-text | Q3 release file | Q3 release | page:12 | CP-1A Company and operating model | MD&A | High | Agrees |
| Hedged production and sensitivity | source-text | Q3 release file | Q3 release | page:24 | CP-1A, CP-2 | MD&A | High | Agrees |
| Colorado terms | source-text | Q3 release file | Q3 release | page:98 | CP-1A Transaction summary | Note | High | Agrees except the asset-backing remark |
| Oklahoma terms | source-text | Q3 release file | Q3 release | page:5 and page:98 | CP-1A Transaction summary | Note | High | Control remark unsupported |
| FERC rejections | source-text | Q3 release file | Q3 release | page:65 | CP-1, CP-1A, CP-2 | MD&A | High | Agrees |
| Far North contracting | source-text | Q1 release file | Q1 release | page:12 | CP-2 Strengths | Footnote | High | Not carried into CP-1A; see issue log |

### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Last-four-quarter Adjusted EBITDA | CP-1 | 1,104 + 759 - 857 | Sum | Recomputed 1,006, agrees | Supported | High | Leverage denominator | Q3 release page:23, page:3 |
| Total debt | CP-1 | 3,470 + 750 | Sum | Recomputed 4,220, agrees | Supported | High | Leverage numerator | Q3 release page:89, page:69 |
| Total debt / EBITDA | CP-1, CP-2 | 4,220 / 1,006 | Division | Recomputed 4.19, agrees | Supported | High | Leverage | As above |
| Net debt / EBITDA | CP-1, CP-2 | (4,220 - 345) / 1,006 | Division | Recomputed 3.85, agrees | Supported | High | Leverage | As above |
| Adjusted Net Debt / Adjusted EBITDA | CP-1 | 3,470 + 350 - 345 + 671 - 25 = 4,121; / 1,006 | Division | Recomputed 4.10, printed 4.1, agrees | Supported | High | Leverage | Q3 release page:40 |
| December leverage | CP-1 | 4,343 / 1,104 and 4,138 / 1,104 | Division | Recomputed 3.93 and 3.75, agrees | Supported | High | Trend | Q3 release page:40 |
| Nine-month cover 2026 and 2025 | CP-1, CP-2 | 759 / 200 and 857 / 205 | Division | Recomputed 3.795 (3.80) and 4.18, agrees | Supported | High | Cover | Q3 release page:3, page:71 |
| Quarter cover | CP-1 | 264 / 85 and 238 / 67 | Division | Recomputed 3.11 and 3.55, agrees | Supported | High | Cover | Q3 release page:3, page:71 |
| Liquidity rebuild | CP-1 | 1,733 - 211 + 345 | Sum | Recomputed 1,867, agrees | Supported | High | Liquidity | Q3 release page:89, page:39 |
| Maturity sum | CP-1 | 52 + 332 + 166 + 245 + 284 + 2,277 | Sum | Recomputed 3,356, agrees | Supported | High | Maturity wall | Q3 release page:87 |
| Liquidity to 2026-2028 maturities | CP-2 | 1,867 / 550 | Division | Recomputed 3.39, agrees | Supported | High | Liquidity | CP-1 maturities |
| Order-cost sensitivity | CP-1, CP-2 | 4,220 / 968 and 3,875 / 968 | Division | Recomputed 4.36 and 4.00, agrees; illustrative; assumes Q4 2025 Order costs nil | Analyst Inference | Medium | Leverage if costs persist | Q3 release page:56 |
| Cash bridge | CP-1, CP-2 | 140 - 338 | Subtraction | Recomputed -198, agrees | Supported | High | Cash quality | Q3 release page:70 |
| Free cash flow less common dividends | CP-1, CP-2 | 338 - 59 | Subtraction | Recomputed 279, agrees | Supported | High | Dividend cover | Q3 release page:59, page:70 |
| Segment change | CP-1, CP-2 | Segment table | Sum of changes | Recomputed -98 and +26, agree | Supported | High | Earnings drivers | Q3 release page:3 |
| Net debt reduction | CP-2 | 3,725 - 3,450 | Subtraction | Recomputed 275, agrees | Supported | High | Deleveraging | Q3 release page:38 |
| Revenue mix | CP-1A | 766 + 359 + 435 + 28 | Sum | Recomputed 1,588, agrees | Supported | High | Revenue quality | Q3 release page:78, page:79 |
| Project debt | CP-1, CP-2 | 1,446 + 139 | Sum | Recomputed 1,585, agrees | Supported | High | Structure | Q3 release page:89 |
| Far North price | CP-1A | 95 + 12 | Sum | Recomputed 107, agrees | Supported | High | Acquisition | Q3 release page:77 |
| Working capital deficit | CP-1 | 1,440 - 1,659 | Subtraction | Recomputed -219, agrees | Supported | High | Liquidity | Q3 release page:36, page:37 |

### Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Oklahoma sale: the company keeps control | The source states only continued operational oversight under an asset management agreement | Untraced | Control decides whether the cash flows stay consolidated and whether creditors keep the full claim | Treat control and accounting as Not supplied; remove the statement from committee text | CP-1A Transaction summary |
| Minor | Assumed Colorado debt is backed by contracted peaking assets | Sources say the facilities are fully contracted and the debt is project debt; security and ranking are not stated | Analyst Inference | Ranking against group creditors | Describe as project debt of unspecified security | CP-1A Transaction summary |
| Minor | Far North adds contracted gas capacity | True per Q1 release page:12 (contracted capacity nil at March 31, 2026 and 100 per cent from May 1, 2026) but absent from CP-1A rows that CP-2 relies on | Weak Lineage | Upstream-only rule for the synthesis | Add the Q1 locator in the next version | CP-2 Strengths |
| Minor | Illustrative leverage after Order costs | Assumes no Order cost in Q4 2025; disclosed | Assumption-Based | Overstates headroom if Q4 2025 costs existed | Keep labelled illustrative | CP-1 C10, CP-2 Key findings |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Citation presence | Strong | Every table row carries a page locator; quotes in CP-1A match the cited pages | Low risk of unsupported figures | Figures can be checked quickly | None |
| Calculation reproducibility | Strong | All derived figures show inputs and recompute | Low risk of arithmetic error | Ratios can be relied on as defined | None |
| Definition consistency | Adequate | Management and calculated leverage both shown with bases | Different net debt definitions can be confused | 4.1 times and 3.85 times are not interchangeable | Keep labels |
| Cross-module identity | Strong | Figures shared by CP-1, CP-1A and CP-2 are identical (1,867, 4.1, 1,006, 38, 1,585, US$750 million) | Low risk of divergent numbers | Consistent committee story | None |
| Interpretation versus fact | Adequate | Three statements go beyond sources (control, asset backing, Far North lineage) | Overstatement shifts weight to structure | Structure conclusions less reliable than financial ones | Correct as in the flags |
| Legal and structural support | Weak | No indentures, credit agreement or transaction agreements | Ranking and covenant claims cannot be tested | Structure remains Insufficient Information | Obtain documents |

### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant levels and headroom | Credit agreement, note covenants | Headroom drives default risk | Not calculable in every module | Caps committee readiness | Credit agreement and debt note |
| G2 | Instrument terms, guarantors, security | Indentures, debt note | Ranking and structural subordination | Structure not assessable | Restricts structural conclusions | Indentures |
| G3 | Audited FY2025 statements | Exhibit 99.3 of the 40-F | Prior-year baseline | FY2025 rows Not supplied | Lowers trend confidence | 40-F exhibits |
| G4 | Pro forma post-quarter leverage | Colorado and Oklahoma agreements, acquired EBITDA | Debt and cash changed on Oct. 22, 2026 | Leverage direction unknown | Medium confidence at best | Transaction documents |
| G5 | Restricted cash reconciliation | Management reconciliation | Cash movable to the parent | Liquidity qualified | Medium | Company disclosure |
| G6 | Mothballing earnings effects | Asset-level earnings | Forward EBITDA | Forward earnings uncertain | Medium | Company disclosure |

### Module register

| Module | Handoff canonical .md / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | tac-2026-11-05-credit_snapshot-host, accepted | Source readiness for seven sources | High | Six headings present | Pass with limitations | Restricted-cash conflict logged |
| CP-1 | Same run, accepted | Financial base | High | Six headings and selectors present | Pass with limitations | Figures agree; presentation points in issue log |
| CP-1A | Same run, accepted | Business and transaction context | High | Six headings and selectors present | Restricted | Control statement unsupported |
| CP-2 | Same run, accepted | Credit synthesis | Medium | Six headings and selectors present | Pass with limitations | Far North lineage; otherwise consistent |

### Claim and evidence issues

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1A | Transaction summary, Oklahoma sale: company keeps control | Untraced | Source states operational oversight only | Remove or mark Not supplied | Restricts Oklahoma conclusions |
| Minor | CP-1A | Transaction summary, Colorado: debt backed by contracted peaking assets | Weak Lineage | Security not stated | Reword | None on figures |
| Minor | CP-2 | Strengths: Far North contracted | Weak Lineage | Not in upstream rows | Add locator | None |
| Minor | CP-1A | Oklahoma sentence repeats the 49 per cent point and says the co-owner takes 49 per cent of cash flows, a proportionality assumption | Assumption-Based | Wording | Reword | None |

### Metric, logic and definition issues

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Calculated total debt includes the 400 of exchangeable preferred shares that management treats as equity | Differs from Total Consolidated Net Debt | None | Keep both labelled | Readers must not compare 3.85 times with 4.1 times |
| Minor | CP-1 | Interest cover rows mix three-, six- and nine-month periods | Quarterly cash interest varies (66, 49, 85) | None | Use the nine-month rows | None |
| Minor | CP-1 | Maturity table total 3,356 plus leases 148 exceeds carrying value 3,470 by 34 | Principal against carrying amount; hedge impacts excluded | Unexplained in source | Log as unreconciled | None |

### Legal and structural claim issues

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-1A, CP-2 | Ranking, guarantees, covenant compliance and the position of the project debt | Indentures, credit agreement, project debt documents | All absent (context states legal documents: none) | Obtain documents before any structural view | Required before committee reliance |

### Market and relative value claim issues

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | Not applicable | None: this run contains no market or relative value module and no quotes, ratings reports or peers | Not applicable | Not applicable | None | None |

### Conflicts and version issues

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-0, CP-1, CP-1A, CP-2 | Restricted cash 100 (page:40) against 84 (page:90), same release | None; both in the retained release | Management reconciliation | Parent-accessible cash uncertain |
| Minor | CP-1A | Centralia Order end date Dec. 12, 2026 (page:5) against Dec. 11, 2026 (page:65) | None | None | One day |
| Minor | CP-1A | Cash at March 31, 2026: 274 (Q1 release page:39) against 267 (page:86) | None | None | Q1 liquidity row only |

### Other integrity issues

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Labelling | The table titled subsequent events and post-quarter items includes events dated within the quarter (the Sept. 14 order, the July 17 extension, the ratings) | Retitle | None; dates are shown |
| Minor | CP-1 | Presentation | Liquidity and maturity chart tables carry no numbers in the numeric cells because the issuer reports in CAD; the amounts sit in the basis text | None required by the transport | Chart consumers get no values |
| Minor | CP-0 | Scope | Readiness view lists restricted cash as a conflict, consistent with later handoffs | None | None |
| Minor | CP-2 | Scope | Rating references are issuer-reported, labelled as context | None | None |

### Handoff component defects

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Transaction summary | Unsupported control statement and wording repetition | Correct in next version | None on later modules |
| Minor | CP-2 | Strengths | Far North contracting not traced to a CP-1A row | Add locator | None |
| Minor | CP-1 | Subsequent events table | Title includes in-quarter events | Retitle | None |

### Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I1 | Material | CP-1A | Unsupported claim | Company said to keep control of Oklahoma portfolio | Remove; mark control Not supplied | Restricted | Open |
| I2 | Material | All | Source conflict | Restricted cash 100 against 84 | Management reconciliation | Restricted | Open |
| I3 | Material | All | Legal gap | Covenants, instruments and transaction agreements absent | Obtain documents | Restricted | Open |
| I4 | Minor | CP-1A | Overstatement | Colorado debt described as backed by contracted assets | Reword | None | Open |
| I5 | Minor | CP-2 | Weak lineage | Far North contracting not traced upstream | Add Q1 locator | None | Open |
| I6 | Minor | CP-1 | Definition | Total debt includes exchangeable preferred; comparability with 4.1 times | Keep labels | None | Open |
| I7 | Minor | CP-1 | Presentation | Subsequent-events table title; mixed-period cover rows | Retitle; use nine-month rows | None | Open |
| I8 | Minor | CP-1A | Wording | Oklahoma sentence duplication and proportionality assumption | Reword | None | Open |

### QA status and clearance

QA status: Restricted. Committee status: Restricted. Reasons: three material issues remain open (an unsupported control statement, an unreconciled restricted-cash conflict, and the absence of legal documents), none of which can be cleared from the pack. Committee use is permitted for the financial base, liquidity and earnings conclusions, which trace cleanly, and not permitted to rely on any statement about control, ranking, covenant headroom or pro forma leverage. No numeric confidence score is computed in this transport; qualitatively the band is Medium.

## Calculations

Every derived figure used by the other handoffs was recomputed from the printed inputs; the results are in the calculation register above and all 20 agree. Independent recomputation done here, with unrounded values: 4,220 / 1,006 = 4.1948; 3,875 / 1,006 = 3.8519; 4,121 / 1,006 = 4.0964 (printed 4.1); 4,396 / 1,104 = 3.9819 (printed 4.0); 759 / 200 = 3.795; 857 / 205 = 4.1805; 264 / 85 = 3.1059; 238 / 67 = 3.5522; 1,867 / 550 = 3.3945; 4,220 / 968 = 4.3595; 3,875 / 968 = 4.0031. Sum checks: 1,573 + 100 + 22 + 13 + 25 = 1,733; 1,733 - 211 + 345 = 1,867; 766 + 359 + 435 + 28 = 1,588; 1,446 + 139 = 1,585. The 3.795 case gives 3.80 under both round-half-up, as the handoff states, and round-half-even. No new analytical figure is introduced.

## Gaps

- Covenant levels, instrument terms, guarantor and security detail, and transaction agreements: Not supplied; every structural claim downstream is limited by this.
- Audited FY2025 statements: Not supplied; FY2025 comparatives in the handoffs are management figures and the Dec. 31, 2025 comparatives printed in the Q3 release.
- Restricted cash reconciliation, pro forma post-quarter leverage and mothballing earnings effects: Not supplied.
- This review did not independently open every figure in the narrative paragraphs of the three analytical handoffs; it opened every table row of the financial base, every quote in the business handoff, every figure shared across handoffs and all derived numbers. Residual risk is in narrative figures not shared across modules.
- Currency and period: CAD throughout and no mismatch with the context; US dollar items labelled.

## Next module

This is the last selected module. The run can publish with committee use restricted. Before any committee reliance, correct the unsupported Oklahoma control statement (I1), obtain management's restricted-cash reconciliation (I2) and the covenant, indenture and transaction documents (I3), and rerun the structure-dependent conclusions.
