## Request

This is the evidence trace and research-integrity review of the DXP ENTERPRISES INC (DXPE) credit snapshot, as of 2026-11-05, covering the accepted source-readiness, financial-base, business-context and credit-synthesis work for the consolidated group in USD, Q3 2026 against FY2025. It checks each material claim against the pinned filings and earnings releases, reproduces the calculations and logs conflicts, without changing any upstream conclusion.

## Sources

### Issuer sources relied on

Locators in the appendix are chunk pages (`page:N`), not printed pages.

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_dxpe-20251231.htm.jsonl | c7d8164f031d9598f9c9e55a6ea72326cd8ca955352110463388478f041b6c83 |
| 10-Q_2026-03-31_dxpe-20260331.htm.jsonl | 4b722eaa286fac42b216402a6ee697593be8d829c4523c0675f74f3756f37099 |
| 10-Q_2026-06-30_dxpe-20260630.htm.jsonl | 062fb840fed8d87a2ce7f779ade2c10a2a9fa08cd06748ccc79bfb77eaff175c |
| 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | b25274cf886044ab8c2b70c234e1e7077124a752d54250ff0e625889085dbaa2 |
| EX-99.1_2026-05-07_earningsrelease3312026.htm.jsonl | 7239622f24e9378a19997bda2636b1f0c58c04309af7d0be42e5556062a8f4af |
| EX-99.1_2026-08-05_earningsrelease6302026.htm.jsonl | 6d154d2d8605fdb9abb6da2ab17ed2ed1363c8da5b1cd9a1ff2db3ea0cf9c96c |
| EX-99.1_2026-11-05_earningsrelease9302026.htm.jsonl | 7fc5ad335ae78b4ce865ab4ec5f61033f2b042958c1ba4a250444be1733b49a2 |
| context (1020710-dxp-enterprises-inc-dxpe.json), settings only | be741ade5f3ce71fa0fd12e85135207822d5c3bd4725f3f29649b4083fde9ae2 |

### Supplied handoffs

| Module | sha256 | Scope reviewed |
| --- | --- | --- |
| CP-0 | 1c28b410d01884432fc8e019b3403e1cf46fbc87c18718dda8f14d0e897e7ee0 | Source readiness, conflicts, gaps |
| CP-1 | c1bbfbf25d30d6263e3558a0f95f7d442dadd213e4ba60d3d7022d862445351c | Financial base, chart tables, covenants, events |
| CP-1A | 83e71b8c466ed58c37e417dd68e9fe8cbf05e4c3651a28a7a31e5e5fd72bf863 | Business model, transactions, governance |
| CP-2 | 9152cc37e37242fe518bf7259e0e89249b86866ca444a4e1c56d4e82cab9ef0f | Credit view, findings, risks, sensitivities |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The credit work traces well to filed statements and reproducible calculations. Committee use is restricted because covenant capacity cannot be stated until the covenant level conflict and the missing covenant EBITDA bridge are resolved. | Medium | No credit agreement, compliance certificate or borrowing base is supplied, so covenant and distribution capacity stay unverified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every reproduced figure ties to a located filing line, and all recomputed ratios match. | The leverage, cover and liquidity numbers can be relied on as calculated from filed inputs. | High |
| The 10-K and the 10-Qs give different term loan covenant levels for two 2026 test dates. | Headroom is wide at either level, but the controlling level is undocumented. | Medium |
| The covenant EBITDA headline is management-attributed and has no bridge to reported Adjusted EBITDA. | Covenant leverage cannot be rebuilt independently. | Medium |
| Five minor wording or labelling points were found upstream, such as a level-versus-change comparison and a margin attribution. | None changes a conclusion, but each should be read with the corrections given here. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 1 is a conflicting item. The most important provenance gap is the unresolved term loan covenant level together with the missing bridge from reported Adjusted EBITDA to covenant EBITDA, which matters because covenant headroom is the main default-risk buffer and implies that any statement of covenant or distribution capacity stays restricted until the credit agreement or a compliance certificate is obtained. All other material claims traced to a located filing line or a reproducible calculation. Committee status: Restricted. No upstream conclusion is changed.

### Traceability summary

| Driver | Origin | Classification | Citation present | Traceability status | Main gap |
| --- | --- | --- | --- | --- | --- |
| Leverage trajectory and cover | Financial base | Calculated | Yes | Committee-Ready | LTM not pro forma, cash interest year-to-date only |
| Liquidity and maturity profile | Financial base | Directly Sourced | Yes | Committee-Ready | Borrowing base not printed |
| Free cash flow quality against acquisitions | Financial base, synthesis | Calculated | Yes | Remediation Needed | Tax normalisation is an analyst choice |
| Covenant headroom | Financial base, synthesis | Conflicting | Partial | Remediation Needed | Level conflict, no EBITDA bridge |
| Acquisition-led pumping growth | Business context | Directly Sourced | Yes | Committee-Ready | Q1 2026 deal names matched by count |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-01 | 10-K_2025-12-31_dxpe-20251231.htm.jsonl | High: audited filing | FY2025 | DXP Enterprises, Inc. and subsidiaries, consolidated | Statements, debt note, covenants, leases, business description | ABL description superseded in July 2026 | Financial base, business context |
| SRC-02 | 10-Q_2026-03-31_dxpe-20260331.htm.jsonl | High: unaudited filing | Q1 2026 | Same | Balances, EBITDA, cash interest, availability | Year-to-date items only | LTM build |
| SRC-03 | 10-Q_2026-06-30_dxpe-20260630.htm.jsonl | High: unaudited filing | Q2 2026 and six months | Same | Same, July 2026 ABL event | Year-to-date items only | LTM build |
| SRC-04 | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | High: unaudited filing | Q3 2026 and nine months | Same | Statements, Note 8 debt, covenants, liquidity, acquisitions, subsequent events | No lease note, no borrowing base | All modules |
| SRC-05 | EX-99.1_2026-05-07_earningsrelease3312026.htm.jsonl | Medium: management release | Q1 2026 | Same | Covenant EBITDA headline | Non-GAAP, no bridge | Covenant context |
| SRC-06 | EX-99.1_2026-08-05_earningsrelease6302026.htm.jsonl | Medium: management release | Q2 2026 | Same | Covenant EBITDA headline | Non-GAAP, no bridge | Covenant context |
| SRC-07 | EX-99.1_2026-11-05_earningsrelease9302026.htm.jsonl | Medium: management release | Q3 2026 | Same | Covenant EBITDA headline, reconciliations | Non-GAAP, no bridge | Covenant context |
| CTX-01 | 1020710-dxp-enterprises-inc-dxpe.json | Settings, not issuer evidence | Run dates | Run settings | Dates, currency, pathway | Blank fields are not zero | Scope only |
| HO-00 | CP-0 handoff | Upstream analytical | As of 2026-11-05 | Issuer | Readiness, conflicts | Source sufficiency only | All modules |
| HO-01 | CP-1 handoff | Upstream analytical | Q3 2026, FY2025 | Issuer | Chart tables, registers | LTM splice | CP-1A, CP-2 |
| HO-02 | CP-1A handoff | Upstream analytical | Q3 2026, FY2025 | Issuer | Business and governance rows | Ownership undisclosed | CP-2 |
| HO-03 | CP-2 handoff | Upstream analytical | Q3 2026, FY2025 | Issuer | View, risks, sensitivities | Illustrative stresses | Committee |

Module status: Ready with Limitations (all upstream handoffs present with populated headings; no credit agreements or compliance certificate). Traceability scope: Top 5. Entity key status: issuer_id dxpe available. Upstream re-anchor: all four handoffs name the same issuer, as-of date 2026-11-05, USD, and the current period Q3 2026; their figures were re-opened against the sources below.

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Gross leverage 3.30x and net leverage 2.44x on LTM Adjusted EBITDA (FY2025: 3.76x and 2.41x) | CP-1 | Debt 839,525 and cash 218,834 at September 30, 2026; LTM Adjusted EBITDA 254,413 | Leverage drives default risk and refinancing tolerance; net leverage barely moved because cash funded acquisitions | Supports tolerance for the debt load while earnings grow | SRC-04 page:10, page:2, page:31; SRC-01 page:52 | LTM not pro forma; company-defined EBITDA |
| 2 | Liquidity 411,005 and 2030 maturity wall | CP-1 | Cash 218,834 plus availability 192,171; maturities schedule | Liquidity absorbs debt service and acquisition outflows; one tranche due October 13, 2030 | Low near-term refinancing risk | SRC-04 page:33, page:14, page:11 | Borrowing base not printed |
| 3 | Free cash flow 104,961 LTM against acquisitions 163,461 | CP-1, CP-2 | Operating cash flow less capex; acquisitions net of cash; cash taxes 7,883 against provision 35,409 | Growth is funded from cash, and low cash taxes flatter free cash flow | Cash buffer, not operations, funds M&A | SRC-04 page:3, page:4, page:19; SRC-01 page:70 | Normalisation is an analyst choice |
| 4 | Covenant headroom: secured leverage 2.30 against 5.50 or 5.75 | CP-1, CP-2 | Reported ratios and the two filings' levels | Covenant breach is the main acceleration trigger | Headroom wide on either level | SRC-04 page:12, page:13; SRC-01 page:84 | Level conflict; no EBITDA bridge |
| 5 | Pumping segment growth is mostly acquired | CP-1A, CP-2 | Q3 2026 IPS growth 43.3% total, 1.6% organic; acquisition sales 48,832 | Purchased revenue needs cash and earn-outs (contingent consideration 30,711) | Organic growth is the key uncertainty | SRC-04 page:27, page:20, page:8 | Q1 2026 deals not named per row |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage and cover trajectory | CP-1 | Filed debt, cash, EBITDA and cash interest lines; arithmetic reproduced | Yes | High | Calculated | Verified by recomputation | High | Committee-Ready |
| Liquidity 411.0 US$m and maturities | CP-1 | Company-stated "$411.0 million of liquidity"; maturities table | Yes | High | Directly Sourced | Verified | High | Committee-Ready |
| FCF quality and acquisition funding | CP-1, CP-2 | Cash flow lines; provision against cash taxes | Yes | High | Calculated | Verified; normalisation labelled analyst choice | Medium | Remediation Needed |
| Covenant headroom | CP-1, CP-2 | 10-K step-down table "September 30, 2026 5.50:1.00" against 10-Q "less than 5.75 to 1.00" | Partial | High for each filing, conflicting between them | Conflicting | Logged, not reconciled | Medium | Remediation Needed |
| Acquisition-led pumping growth | CP-1A, CP-2 | Printed organic growth 1.6% and acquisition sales 48,832 | Yes | High | Directly Sourced | Verified | High | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 839,525 at September 30, 2026 | Note 8 debt table | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | SRC-04 | page:10, page:11 | CP-1 leverage table | Sourced | High | Term Loan B only; ABL nil; promissory note repaid |
| Cash 218,834 | Balance sheet | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | SRC-04 | page:2 | CP-1 liquidity table | Sourced | High | No restricted cash reported |
| Adjusted EBITDA 195,444 nine months 2026; 166,333 nine months 2025; 225,302 FY2025 | EBITDA reconciliation | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl; 10-K_2025-12-31_dxpe-20251231.htm.jsonl | SRC-04, SRC-01 | page:31; page:52 | CP-1 financials table | Sourced | High | Company-defined |
| Liquidity 411.0 US$m | Liquidity discussion | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | SRC-04 | page:33 | CP-1 liquidity table | Sourced | High | Equals cash plus availability |
| Secured Leverage Ratio 2.30 to 1.00; level "less than 5.75" | Note 8 covenants | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | SRC-04 | page:12 | CP-1 covenants | Sourced | High | Conflicts with 10-K table |
| Step-down table 5.50 for September 30, 2026 | Note 9 covenants | 10-K_2025-12-31_dxpe-20251231.htm.jsonl | SRC-01 | page:84 | CP-1 covenants | Sourced | High | Conflicts with 10-Q |
| Covenant EBITDA 270.0 US$m | CFO commentary | EX-99.1_2026-11-05_earningsrelease9302026.htm.jsonl | SRC-07 | page:2 | CP-1 covenants | Sourced | Medium | Management-attributed |
| Cash paid for interest 45,330 and 40,225; FY2025 53,698 | Supplemental cash flow notes | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl; 10-K_2025-12-31_dxpe-20251231.htm.jsonl | SRC-04, SRC-01 | page:19; page:92 | CP-1 interest cover | Sourced | High | Year-to-date only |
| ABL 225.0 US$m, matures July 2, 2031, nil drawn | Note 8 ABL | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | SRC-04 | page:12 | CP-1 debt table | Sourced | High | Supersedes 10-K description |
| Acquisitions 126,234 net of cash, nine months 2026 | Cash flow statement | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | SRC-04 | page:3 | CP-2 calculations | Sourced | High | |
| IPS organic growth 1.6% in Q3 2026 | Revenue note | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | SRC-04 | page:27 | CP-1A operating model | Sourced | High | |
| No customer 10% or more of revenues | Item 1 business | 10-K_2025-12-31_dxpe-20251231.htm.jsonl | SRC-01 | page:13 | CP-1A operating model | Sourced | High | Last three fiscal years |
| Repurchase program "completed" while 68,006 of authorisation remained at July 31, 2026 | Note 13 and Item 2 | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | SRC-04 | page:19; page:35 | CP-1A transaction summary | Sourced, with interpretation | High | Lapse of the 24-month term is an interpretation |
| S&P upgrade from B to B+ on July 20, 2026 | Credit ratings paragraph | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | SRC-04 | page:33 | CP-1A profile, CP-2 strengths | Sourced (issuer statement) | Medium | No agency report supplied |
| Related-party lease expense about 2.3 US$m FY2025 | Note 21 related parties | 10-K_2025-12-31_dxpe-20251231.htm.jsonl | SRC-01 | page:100 | CP-1A governance | Sourced | High | |
| Operating cash flow nine months 2026 80,641 | Cash flow statement | 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | SRC-04 | page:3 | CP-1 financials | Sourced | High | |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA 254,413 (Q3 2026) | CP-1 leverage and cover | 225,302; 195,444; 166,333 | FY2025 + 9M 2026 - 9M 2025; recomputed 225,302 + 195,444 - 166,333 = 254,413 | Calculated | Verified | High | Leverage, refinancing | SRC-01 page:52; SRC-04 page:31 |
| Gross leverage 3.30x; net 2.44x | CP-1, CP-2 | 839,525; 218,834; 254,413 | 839,525 / 254,413 = 3.300; 620,691 / 254,413 = 2.440 | Calculated | Verified | High | Leverage | SRC-04 page:10, page:2 |
| LTM cash interest 58,803 and cover 4.33x | CP-1 | 53,698; 45,330; 40,225 | 53,698 + 45,330 - 40,225 = 58,803; 254,413 / 58,803 = 4.327 | Calculated | Verified | Medium | Coverage | SRC-01 page:92; SRC-04 page:19 |
| Liquidity 411,005 | CP-1 | 218,834; 225,000; 32,829 | 218,834 + (225,000 - 32,829) | Calculated | Verified; equals company figure | High | Liquidity | SRC-04 page:33 |
| Covenant cushion: EBITDA could fall 58.2% (5.50) or 60.0% (5.75) | CP-1 | 620,691; 270,000 | 1 - 620,691 / 5.50 / 270,000 | Calculated | Verified arithmetic; assumes all debt secured and no other secured claims | Medium | Default risk | SRC-04 page:12; SRC-07 page:2 |
| Secured leverage cross-check 2.299x | CP-1 | 620,691; 270,000 | 620,691 / 270,000 | Calculated | Matches reported 2.30 | High | Covenant | SRC-04 page:12 |
| LTM free cash flow 104,961; with taxes at provision 77,435 | CP-1, CP-2 | CFO 118,400; capex 13,439; taxes 7,883 and provision 35,409 | 118,400 - 13,439; 104,961 - 35,409 + 7,883 | Calculated; normalisation is Assumption-Based | Verified arithmetic | Medium | Cash flow quality | SRC-01 page:70, page:92; SRC-04 page:3, page:19 |
| LTM acquisitions 163,461 | CP-2 | 61,675; 126,234; 24,448 | 61,675 + 126,234 - 24,448 | Calculated | Verified | High | Liquidity | SRC-01 page:70; SRC-04 page:3 |
| Rate sensitivity: +100 bp adds 8,395; cover 3.79x | CP-2 | 839,525; 58,803; 254,413 | 839,525 x 1%; 254,413 / (58,803 + 8,395) | Calculated; the 100 bp shock is an Assumption | Verified arithmetic | Medium | Debt service | SRC-04 page:11 |
| EBITDA stress -20%: gross 4.12x, net 3.05x | CP-2 | 254,413; 839,525; 620,691 | 254,413 x 0.8 = 203,530 | Assumption-Based | Illustrative, labelled | Low | Downside | CP-2 calculations |
| Metric-definition drift | CP-1, CP-2 | Adjusted EBITDA 254,413; covenant EBITDA 270,000 | Two definitions; difference 15,587 unbridged | Not Calculable (bridge missing) | Flagged | Medium | Covenant | SRC-01 page:85; SRC-07 page:2 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Covenant headroom | The two filings state different Secured Leverage Ratio levels for June 30, 2026 and September 30, 2026; no amendment text | Conflicting | Level sets the breach trigger and the headroom shown to committee | Obtain the December 16, 2025 Term Loan Amendment | CP-1 covenants, CP-2 key findings |
| Material | Covenant leverage on a covenant basis | Covenant EBITDA 270,000 has no bridge to Adjusted EBITDA 254,413 | Insufficient Information | Covenant leverage cannot be rebuilt independently | Obtain compliance certificate | CP-1 covenants, CP-2 |
| Minor | Pumping growth is acquired | CP-1A calculation compares the level of acquisition sales (48,832) with the change in segment sales (43,564); the like-for-like figure is the change in acquisition sales (42,087) | Calculated | Conclusion holds (organic change 1,477) but the wording mixes level and change | Read as corrected here | CP-1A calculations |
| Minor | Margin pressure in Q3 2026 | CP-2 attributes the year-on-year gross margin decline in part to input costs; the filing attributes a 65 basis point impact to input costs "compared to the last quarter" | Weak Lineage | The year-on-year cause is not stated | Cite the sequential wording or drop the attribution | CP-2 key findings |
| Minor | Q1 2026 acquisition names | Names come from 10-K subsequent events and are matched to the Q3 10-Q count of three by number, not by name | Analyst Inference | Deal-level terms cannot be tied to names | Obtain 8-Ks | CP-1A timeline |
| Minor | S&P rating B+ | Issuer statement only | Weak Lineage | Rating is not independently evidenced | Obtain agency report | CP-1A profile, CP-2 strengths |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Committee-Ready | Seven filings and releases cover FY2025 and three 2026 quarters | Complete period chain supports the LTM build | Leverage and liquidity can be relied on | None |
| Citation completeness | Ready with Remediation | Sampled figures all matched their cited pages; two wording points and the covenant conflict logged | Partial citation on the covenant level leaves headroom wording imprecise | Do not state a single covenant level | Resolve with amendment text |
| Calculation traceability | Committee-Ready | Every LTM, ratio and sensitivity was recomputed with inputs and formula | Reproducible formulas limit hidden normalisation | Ratios are dependable | None |
| Assumption transparency | Ready with Remediation | Tax normalisation, 100 bp and stress cases are labelled analyst choices or illustrative | Unlabelled assumptions would overstate certainty | Present stresses as illustrative | Keep labels in committee text |
| Markdown/export artifact integrity | Committee-Ready | All four handoffs carry the required headings, source lists and hashes | Missing headings would break lineage | Chain is intact | None |

Overall auditability: Ready with Remediation (lowest of the five dimensions).

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Covenant level conflict | Term Loan Amendment and later amendments | Breach trigger is undocumented, so default-risk buffer is imprecise | Covenant table, key findings | Medium impact | Term loan agreement and amendment |
| CP-5-GAP-002 | No covenant EBITDA bridge | Compliance certificate | Covenant leverage depends on a management headline | Covenant table | Medium impact | Compliance certificate |
| CP-5-GAP-003 | Restricted payments and investment baskets not printed | Credit agreement | Capacity for buybacks and acquisitions unbounded in the analysis | CP-1A and CP-2 capital allocation | Medium impact | Credit agreement |
| CP-5-GAP-004 | Ownership percentages and control | Proxy statement (10-K Item 12 incorporated by reference) | Control and alignment cannot be assessed | CP-1A, CP-2 | Medium impact | 2026 proxy statement |
| CP-5-GAP-005 | ABL borrowing base and compliance threshold | Borrowing base certificate | Usable availability may be lower than capacity less letters of credit | Liquidity table | Low impact | Borrowing base certificate |
| CP-5-GAP-006 | Finance lease balance at September 30, 2026; backlog after FY2025 | Lease note, Q3 2026 presentation | Debt-like claims and forward visibility | CP-1, CP-1A | Low impact | Company notes and presentation |
| CP-5-GAP-007 | Rating evidence | Agency report | Rating view rests on an issuer statement | CP-1A, CP-2 | Low impact | Agency report |

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | 1.response.md, sha256 1c28b410d01884432fc8e019b3403e1cf46fbc87c18718dda8f14d0e897e7ee0; run dxpe-2026-11-05-credit_snapshot-host | Source readiness | High | Six H2 headings present | Pass with limitations | Conflicts and gaps logged |
| CP-1 | 1.response.md, sha256 c1bbfbf25d30d6263e3558a0f95f7d442dadd213e4ba60d3d7022d862445351c; same run | Financial base | High | Six H2 headings and chart selectors present | Pass with limitations | LTM splice disclosed |
| CP-1A | 1.response.md, sha256 83e71b8c466ed58c37e417dd68e9fe8cbf05e4c3651a28a7a31e5e5fd72bf863; same run | Business and governance | High | Six H2 headings and selectors present | Pass with limitations | One wording correction |
| CP-2 | 1.response.md, sha256 9152cc37e37242fe518bf7259e0e89249b86866ca444a4e1c56d4e82cab9ef0f; same run | Credit synthesis | High | Six H2 headings and selectors present | Pass with limitations | One attribution point |

#### T5.2 Citation and evidence support issues

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Margin decline attributed partly to input costs | Partial support | Filing wording is sequential ("compared to the last quarter") | Reword to the sequential comparison | None on the credit view |
| Minor | CP-1A | Q1 2026 deal names | Count match only | Names from the 10-K, count from the Q3 10-Q | Label as matched by count | None |
| Minor | CP-1, CP-2 | S&P rating B+ | Issuer statement | No agency document | Keep the issuer-only label | None |

#### T5.3 Math, logic and definition issues

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Acquisition sales level compared with change in segment sales | Like-for-like is the change in acquisition sales, 42,087 of the 43,564 change | None | Read as corrected here | None; organic change 1,477 confirms the conclusion |
| Material | CP-1, CP-2 | Covenant leverage and headroom | Adjusted EBITDA 254,413 against covenant EBITDA 270,000, unbridged | 10-K 5.50 against 10-Q 5.75 level | Obtain compliance certificate and amendment | Restricts any covenant capacity statement |
| Minor | CP-1 | LTM splice of audited and unaudited periods; cash interest year-to-date | Not pro forma for acquisitions | None | Keep the disclosed limitation | None |

#### T5.4 Legal and structural claim issues

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-1A | Guarantors, security and lien ranking of the term loan and ABL, and distribution baskets | Executed term loan and ABL agreements | Only filing summaries are supplied | Obtain agreements before stating legal capacity | Required before any capacity statement |
| Minor | CP-1 | Canadian subsidiaries excluded from term loan guarantees | Term loan agreement | Filing summary only | Same | Same |

#### T5.5 Market and relative-value claim issues

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1A, CP-2 | Rating of B+ from S&P | Agency report | Issuer statement only | Keep the issuer-only label | None; no relative-value claim is made |
| Minor | CP-2 | No pricing, spread or peer claim | Market quotes (context blank) | Context holds no quotes or peers | None | None |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A | CP-1 called the 85.0 million repurchase program "completed"; CP-1A shows 68,006 unused at July 31, 2026 | CP-1A refines CP-1, which cannot be edited | Treat the CP-1A wording as controlling | None on figures |
| Minor | CP-0, CP-1, CP-2 | Covenant level conflict carried consistently | None | None | Same limitation in all |
| None found | CP-1, CP-2 | Leverage, cover, liquidity and maturity figures agree between CP-1 and CP-2 | ABL terms taken from the 10-Qs, not the 10-K, in all modules | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Duplication | Leverage and liquidity figures recur in both modules | None; figures agree | None |
| Material | CP-2 | Committee readiness | View is Medium confidence and covenant capacity is unverified | State capacity as unverified | Restricted use |

#### T5.8 Handoff structure and export

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| None found | CP-0 to CP-2 | Headings, source lists, hashes, selectors | No structural defect observed | None | Chain accepted |
| None found | CP-2 | Opening view and selector sections | Opening view length and required selectors conform to the module rules | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-I-01 | Material | CP-1, CP-2 | Source conflict | Covenant level 5.50 against 5.75 for two 2026 test dates | Obtain amendment | Restricts capacity statement | Open |
| CP5-I-02 | Material | CP-1, CP-2 | Missing bridge | Covenant EBITDA 270,000 unbridged to 254,413 | Obtain certificate | Restricts capacity statement | Open |
| CP5-I-03 | Material | CP-1A, CP-2 | Legal source | Distribution baskets and ownership unseen | Obtain agreements and proxy | Restricts capital allocation view | Open |
| CP5-I-04 | Minor | CP-1A | Calculation wording | Level compared with change | Corrected in this review | None | Logged |
| CP5-I-05 | Minor | CP-2 | Attribution | Margin decline attribution | Reword | None | Open |
| CP5-I-06 | Minor | CP-1A | Lineage | Q1 2026 deal names by count | Label | None | Open |
| CP5-I-07 | Minor | CP-1, CP-2 | Lineage | Rating by issuer statement | Keep label | None | Open |
| CP5-I-08 | Minor | CP-1, CP-1A | Version | Repurchase program called completed in CP-1; CP-1A adds the unused 68,006 | Treat CP-1A as controlling | None | Logged |

Clearance decision: committee use is Restricted. The leverage, cover, liquidity and maturity figures are cleared for use as calculated from filed inputs. Covenant capacity and distribution capacity statements are not cleared. Confidence: Medium. Critical findings: none. Material findings: three (CP5-I-01 to CP5-I-03). Minor findings: five.

## Calculations

Recomputation performed for this review, from the filed inputs, USD thousands. Every value agreed with the upstream handoffs unless noted.

- LTM Adjusted EBITDA: Q1 225,302 + 57,812 - 52,519 = 230,595; Q2 225,302 + 128,188 - 109,832 = 243,658; Q3 225,302 + 195,444 - 166,333 = 254,413.
- Gross leverage: 846,785 / 225,302 = 3.758; 844,665 / 230,595 = 3.663; 842,545 / 243,658 = 3.458; 839,525 / 254,413 = 3.300. Net: 543,002 / 225,302 = 2.410; 631,284 / 230,595 = 2.738; 615,927 / 243,658 = 2.528; 620,691 / 254,413 = 2.440.
- Cash interest cover: 225,302 / 53,698 = 4.196; 230,595 / 54,953 = 4.196; 243,658 / 57,097 = 4.267; 254,413 / 58,803 = 4.327.
- EBITDA reconciliations: Q3 2026 36,463 + 16,949 + 12,355 = 65,767, plus 1,489 = 67,256; nine months 2026 102,809 + 50,223 + 36,609 = 189,641, plus 4,757 + 1,046 = 195,444; FY2025 88,677 + 60,530 + 30,545 + 38,850 = 218,602, plus 5,708 + 992 = 225,302. All equal the printed totals.
- Maturity schedule sum: 2,120 + 8,480 + 8,480 + 8,480 + 811,965 = 839,525 equals total debt; debt less discount and issuance costs 839,525 - 16,309 = 823,216 equals 8,480 + 814,736.
- Cash flow cross-check: principal debt payments 7,260 = Term Loan B decline (845,885 - 839,525 = 6,360) plus promissory note 900.
- Liquidity: 218,834 + 192,171 = 411,005.
- Covenant: 620,691 / 270,000 = 2.299; 620,691 / 5.50 = 112,853; 1 - 112,853 / 270,000 = 58.2%; 620,691 / 5.75 = 107,946; 1 - 107,946 / 270,000 = 60.0%.
- Acquisition sales check for the CP-1A wording point: IPS Q3 2026 acquisition sales 48,832 less Q3 2025 acquisition sales 6,745 = 42,087; total IPS sales change 144,115 - 100,551 = 43,564; organic change 43,564 - 42,087 = 1,477 (Q3 10-Q page:20 and page:27).
- Free cash flow: LTM CFO 94,264 + 80,641 - 56,505 = 118,400; capex 40,286 + 10,153 - 37,000 = 13,439; FCF 104,961; with taxes at provision 104,961 - 35,409 + 7,883 = 77,435; acquisitions 61,675 + 126,234 - 24,448 = 163,461.
- CP-2 sensitivities: 839,525 x 1% = 8,395; 254,413 / (58,803 + 8,395) = 3.786; 254,413 x 0.8 = 203,530; 839,525 / 203,530 = 4.125; 620,691 / 203,530 = 3.050; 620,691 / (270,000 x 0.7) = 3.284.
- Top 5 classification counts: directly sourced 2 (liquidity and maturity profile; pumping growth), calculated 2 (leverage and cover; free cash flow quality), assumption-based 0, analyst inference 0, conflicting 1 (covenant headroom). Total 5.

## Gaps

| Gap | Effect | Severity | Action |
| --- | --- | --- | --- |
| Covenant level conflict, no covenant EBITDA bridge, no credit agreement or compliance certificate | Covenant and distribution capacity stay unverified; committee use Restricted | Material | Obtain the Term Loan Amendment of December 16, 2025, the agreements and a compliance certificate |
| Ownership and control not in sources | Alignment cannot be assessed | Material | Obtain the 2026 proxy statement |
| Borrowing base, finance lease balance at September 30, 2026, latest backlog, agency rating report | Smaller effects on liquidity, debt-like claims, visibility and market view | Minor | Obtain as listed in the gaps ledger |
| Sampling basis: this review recomputed all derived figures and re-opened the cited pages for the figures listed in the lineage register; narrative statements were checked for direction and superlatives against the same pages | Unsampled narrative wording could carry unlisted defects | Minor | Spot-check before external use |

## Next module

No further module is selected in this run. The report builder should present the Restricted committee status with the three open material items, carry the covenant level conflict and the unbridged covenant EBITDA as stated limitations, and apply the wording corrections logged here.
