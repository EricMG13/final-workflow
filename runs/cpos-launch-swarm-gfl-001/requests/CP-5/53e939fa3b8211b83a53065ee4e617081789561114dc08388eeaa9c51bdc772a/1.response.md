# CP-5 - Evidence trace and research-integrity QA: GFL Environmental Inc. (gfl)

## Request

- Issuer: GFL Environmental Inc. (issuer id gfl), as of 2026-11-05, information cutoff 2026-11-05.
- Run: gfl-2026-11-05-credit_snapshot-host, pathway credit_snapshot, minimum module set. CP-5 checks CP-0, CP-1, CP-1A and CP-2 and grades the result (absorbed CP-5A phase).
- Execution: host session. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called.
- Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- QA envelope: qa_status Restricted; Confidence Score 26, band Insufficient Information (scripts/confidence_score.py, see Calculations); committee_status Requires More Work.

## Sources

| Source | sha256 |
| --- | --- |
| 40-F_2025-12-31_gfl-20251231x40f.htm.jsonl | b934765df3e7c34910af8387591b8fa09e1dab95cdcc8ca06bb6c968dd003ae6 |
| 6-K-EX-99.1_2026-03-31_tm2612685d3_ex99-1.htm.jsonl | cb537fb74c382c1d0201e410842d4660c8613b15a362445d11ff422e5b399f25 |
| 6-K-EX-99.1_2026-04-29_tm2612685d2_ex99-1.htm.jsonl | 3df073d71665ee940b9aad03ce71f25168457a8b67f443c14d9006bb7687f437 |
| 6-K-EX-99.1_2026-06-30_tm2619744d3_ex99-1.htm.jsonl | f263228fdadc42723c2dcd6496cb1b52232f1a5fd2b7778ad4e13cf2111721c2 |
| 6-K-EX-99.1_2026-07-29_tm2619744d2_ex99-1.htm.jsonl | 5fa07feeac05724810518cb847015c4db9d05aa3ab7046fa5917870573c8a1c3 |
| 6-K-EX-99.1_2026-10-28_tm2626649d2_ex99-1.htm.jsonl | ee28f5cf135f3ebbb50b3dfc34b1ac6447600e4aae341e5faea9d8d69de358cb |
| 6-K-EX-99.1_2026-10-30_tm2626649d1_ex99-1.htm.jsonl | 21de76c788e5b3fc408d84e05a80d6dd1586537f33922ada67131193bae391d4 |
| context | 3b2c2e634d2c0d1d787b2efc6bec59a8cda3a4f73d98ab4b38ff36c15a35719c |

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | 3ca64bc77aec22a65a5d22e442dcfacbafbe8c6089ae8fbfcc4a83ff34445b20 |
| CP-1 | fd0b36c4541facbcfd57f1a25ee1d99854d60785b7b605c0414327e7191ae883 |
| CP-1A | 2a8756fdbb4cdcf8b1c1ac603e4418c295b7471037d29ecc999196401404c49c |
| CP-2 | daff410e3d612a3a17437615f391a9fd2ee3da7c860efc94285b7a8a9d40efc7 |

Locators are page numbers of the pinned converted text (page:N). Source text inside each file quotes a different sha256 for the original HTML; the pinned hashes above are used.

## Findings

### Traceability conclusion

The run is traceable enough for a view of GFL's reported results, debt table and covenant text, and not for the decision that matters most, the leverage and liquidity position after the SECURE acquisition. Every reported figure in the four handoffs that I checked sits on its cited page, and every calculation I recomputed matches. One statement is wrong: CP-2 calls the revolver largely undrawn, but CAD 868.0 million of CAD 2,025.0 million is drawn. The critical provenance gap is the missing covenant definitions, revolver availability and run-rate EBITDA bridge, so headroom and liquidity cannot be traced.

| Traceability summary | Result |
| --- | --- |
| Distinct numbers in CP-0, CP-1A | 64; all found in the sources |
| Distinct numbers in CP-1, CP-2 | 221; 202 found in the sources, 19 are my calculations |
| CP-1 calculations recomputed | 22 of 22 equal |
| Material claims by lineage | 4 Directly Sourced, 2 Calculated, 2 Analyst Inference, 2 Insufficient Information |
| Open findings | 1 MATERIAL, 5 MINOR |

### Analytical appendix - complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 40-F_2025-12-31_gfl-20251231x40f.htm.jsonl | High: filed annual report cover | Fiscal year ended December 31, 2025 | GFL Environmental Inc. | Identity, listing, share counts, exhibit index | Annual information form, MD&A and audited statements are exhibits not supplied | CP-0, CP-1A |
| S2 | 6-K-EX-99.1_2026-03-31_tm2612685d3_ex99-1.htm.jsonl | High: furnished unaudited interim statements | Three months ended March 31, 2026 | GFL and subsidiaries, consolidated | Statements, debt note, covenants, subsequent events | Text conversion; unaudited; file label date is period end | CP-1, CP-1A |
| S3 | 6-K-EX-99.1_2026-04-29_tm2612685d2_ex99-1.htm.jsonl | Medium: issuer earnings release | Q1 2026 | Same | Non-IFRS bridges, Net Leverage, guidance | Management measures | CP-1, CP-2 |
| S4 | 6-K-EX-99.1_2026-06-30_tm2619744d3_ex99-1.htm.jsonl | High: furnished unaudited interim statements | Three and six months ended June 30, 2026 | Same | Statements, debt note, covenants | Text conversion; unaudited | CP-1 |
| S5 | 6-K-EX-99.1_2026-07-29_tm2619744d2_ex99-1.htm.jsonl | Medium: issuer earnings release | Q2 2026 | Same | Non-IFRS bridges, Net Leverage, guidance, special committee statement | Management measures | CP-1, CP-1A, CP-2 |
| S6 | 6-K-EX-99.1_2026-10-28_tm2626649d2_ex99-1.htm.jsonl | Medium: issuer earnings release | Q3 2026 and nine months | Same | Guidance, Net Leverage, non-IFRS bridges, take-private statement | Management measures; guidance forward-looking | CP-1, CP-1A, CP-2 |
| S7 | 6-K-EX-99.1_2026-10-30_tm2626649d1_ex99-1.htm.jsonl | High: furnished unaudited interim statements | Three and nine months ended September 30, 2026 | Same | Statements, notes 1 to 17, debt, SECURE allocation, commitments | Text conversion; unaudited; provisional SECURE accounting | CP-1, CP-1A, CP-2 |
| S8 | context | User settings, not evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency | Not issuer evidence | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SECURE acquisition and perimeter change | CP-1, CP-1A, CP-2 | Closing on September 1, 2026; consideration of about CAD 5,414.1 million | Debt and liabilities assumed against one month of earnings | Sets the post-closing credit view | S7 page:6, page:7 | Provisional accounting |
| 2 | Leverage on stated and reported bases | CP-1, CP-2 | Net Leverage 3.8x; net debt over trailing Adjusted EBITDA 5.05x | The two bases differ by CAD 730.9 million of run-rate adjustments | Core leverage metric | S6 page:14; S7 page:11 | Covenant definitions not supplied |
| 3 | Covenant structure | CP-1, CP-2 | 5.00x for four fiscal quarters after a Material Acquisition, then 4.50x; 3.00x interest coverage | Determines headroom and the date pressure returns | Monitoring horizon | S7 page:12, page:13 | Ratio values not disclosed |
| 4 | Cash conversion | CP-1, CP-2 | Operating cash flow less capital spending of CAD 37.3 million over nine months | Little internal funding for deleveraging | Debt-service capacity | S7 page:4 | Add-back bridge not independently checked |
| 5 | Take-private review | CP-1A, CP-2 | Special Committee; deadline November 9, 2026 | Possible change of control and financial policy | Event risk, open after the cutoff | S6 page:1, page:6 | Terms and legal documents not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SECURE consideration and closing date | CP-1, CP-1A | S7 page:6, page:7 | Yes | High | Documentary Fact | Supported | High | Traced |
| Debt by instrument and stated maturities | CP-1, CP-2 | S7 page:11 to page:13 | Yes | High | Documentary Fact | Supported | High | Traced; instrument sum equals 11,696.4 |
| Net Leverage 3.8x versus 3.4x | CP-1, CP-2 | S6 page:14 | Yes | Medium: management measure | Documentary Fact | Supported as a management statement | Medium | Traced |
| Net debt over trailing reported Adjusted EBITDA 5.05x | CP-1, CP-2 | S6 page:14 inputs | Yes | Medium inputs | Calculated | Supported | Medium | Recomputed equal |
| Operating cash flow less capex 37.3 | CP-1, CP-2 | S7 page:4 inputs | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Covenant thresholds | CP-1, CP-2 | S7 page:12, page:13 | Yes | High | Documentary Fact | Supported | High | Traced |
| Covenant headroom | CP-1, CP-2 | Definitions not in the set | No source exists in the set | Not available | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Revolver availability | CP-1, CP-2 | Not in the set | No source exists in the set | Not available | Insufficient Information | Open gap | Low | CP-2 wording conflicts with the gap (finding QA-1) |
| Pricing-led margin resilience | CP-1A, CP-2 | S6 page:2 (management statement) | Yes | Medium | Analyst Inference | Supported as management language | Medium | Traced |
| Take-private effect on leverage and debt terms | CP-1A, CP-2 | S6 page:1 | Yes for the event, no for the effect | Medium | Analyst Inference | Event supported; effect is inference | Low | Correctly hedged |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenue 2,155.3 and Adjusted EBITDA 678.7, Q3 2026 | pinned source-text folder | 6-K-EX-99.1_2026-10-30 file | S7 | page:1 statement of operations; S6 page:15 | CP-1 table | Reported | High | Matches in both |
| Total long-term debt 11,671.4 | pinned source-text folder | 6-K-EX-99.1_2026-10-30 file | S7 | page:11 note 7 | CP-1 balance sheet table | Reported | High | Matches |
| Revolver drawn 182.0 at June 30, 2026 | pinned source-text folder | 6-K-EX-99.1_2026-06-30 file | S4 | page:10 note 7 | CP-1 latest-quarter changes | Reported | High | CP-1 cites page:11, wrong by one (QA-3) |
| Covenant 5.00x or 4.50x, 3.00x | pinned source-text folder | 6-K-EX-99.1_2026-10-30 file | S7 | page:12, page:13 note 7 | CP-1 definitions | Reported description | High | Matches |
| Net Leverage 3.8x, Run-Rate EBITDA 2,988.0 | pinned source-text folder | 6-K-EX-99.1_2026-10-28 file | S6 | page:14 | CP-1 definitions | Management non-IFRS | Medium | Matches |
| SECURE consideration 5,414.1 | pinned source-text folder | 6-K-EX-99.1_2026-10-30 file | S7 | page:6, page:7 note 3 | CP-1, CP-1A | Reported | High | Matches |
| Q1 Board approval April 29, 2026 | pinned source-text folder | 6-K-EX-99.1_2026-03-31 file | S2 | page:4 note 1 | CP-1A timeline | Reported | High | CP-1A cites page:3 (QA-3) |
| Special Committee, deadline November 9, 2026 | pinned source-text folder | 6-K-EX-99.1_2026-10-28 file | S6 | page:1, page:6 | CP-1A, CP-2 | Management statement | Medium | Matches |
| Performance bonds 2,324.1; letters of credit 535.1 | pinned source-text folder | 6-K-EX-99.1_2026-10-30 file | S7 | page:18, page:19 note 15 | CP-1, CP-1A, CP-2 | Reported | High | Matches |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Discrete quarters sum to nine months (revenue, Adjusted EBITDA, net loss, Adjusted Free Cash Flow, operating cash flow, cash interest) | CP-1 calculations | Q1, Q2, Q3 2026 values | Sum of three quarters | Recomputed: all equal printed nine-month values | Supported | High | Tie-out of the discrete table | S2 to S7 |
| Net Leverage reproduced | CP-1, CP-2 | 11,399.9 over 2,988.0 | Division | 3.815x, prints 3.8x | Supported | Medium | Leverage | S6 page:14 |
| Net debt over trailing reported Adjusted EBITDA | CP-1, CP-2 | 11,399.9 over 2,257.1 | Division | 5.05x equal | Supported | Medium | Leverage on reported base | S6 page:14 |
| Adjusted EBITDA to interest coverage proxies | CP-1 | 678.7 over 179.4; 678.7 over 172.5; 1,748.4 over 482.9 | Division | 3.78x, 3.93x, 3.62x equal | Supported with label caveat | Medium | Not the covenant ratio | S7 page:1, page:4 |
| Operating cash flow less capex | CP-1, CP-2 | 950.1 less 912.8 | Subtraction | 37.3 equal | Supported | High | Cash conversion | S7 page:4 |
| Maturity buckets | CP-1, CP-2 | Carrying amounts of notes by stated maturity | Addition | 2,128.2 for 2028, 1,844.4 for 2029, 2,780.8 for 2031 equal | Supported with caveat that amounts are CAD carrying values | Medium | Refinancing | S7 page:11, page:12 |
| Implied Q4 figures from guidance | CP-2 | Guidance less nine-month actuals | Subtraction | 741.6 to 746.6, 83.3, 535.1 equal | Supported as arithmetic; guidance reliability unverified | Low | Forward cash flow | S6 page:2, page:3 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial gate, 1 MATERIAL and 5 MINOR | Script formula | 26, band Insufficient Information | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2 strengths: revolver largely undrawn | Sources show 868.0 drawn against facilities of 2,000.0 and 25.0; availability is not stated | Unsupported claim | Overstates liquidity headroom in the committee-facing strengths | Restate as drawn about 43 percent of commitments with availability not supplied, in a new run | CP-2 handoff |
| MINOR | CP-1A: cash portion of SECURE price and costs funded with new debt | Sources give debt issued and the cash price but do not state the use of proceeds | Analyst Inference presented as mechanism | Overstates what is known about the financing link | Tag as inference and keep use of proceeds as Insufficient Information | CP-1A transaction summary |
| MINOR | CP-1A: July 29, 2026 entry for formation of the Special Committee | Q2 release says the Board has formed a committee; Q3 release says it was formed during the third quarter; formation date not stated | Imprecise date | Timeline placement could mislead | Date the entry as announced July 29, 2026 | CP-1A timeline |
| MINOR | CP-2: swaps on the newest instruments; foreign exchange loss attributed to currency mix | Swaps are documented for the 5.625% 2031 notes and the Term Loan B only; causes of the foreign exchange loss are not stated | Overstated attribution | Reader may infer wider hedging | Name the instruments hedged; drop the causal wording | CP-2 strengths and weaknesses |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Each source pinned by sha256; statements identify entity and period on their first page | A wrong document would change every figure | None found | None |
| Locator precision | Adequate | All spot-checked page locators correct except two off-by-one cases | Slower checks | None on conclusions | Correct two locators |
| Calculation reproducibility | Strong | 22 of 22 CP-1 calculations recomputed equal | Arithmetic errors would move leverage | None found | None |
| Cross-module consistency | Adequate | All figures in CP-1A found in sources; CP-2 figures are in CP-1 or listed calculations; one wording conflict on the revolver | Inconsistent wording misleads a committee | Liquidity impression too favourable | Fix CP-2 wording |
| Management measures | Adequate | Net Leverage and Adjusted Free Cash Flow carry management add-backs and are labelled as such | Management numbers can be read as filed facts | Leverage looks lower than on reported earnings | Keep both bases visible, as CP-1 and CP-2 do |
| Reviewer independence | Weak | Host wrote and checked the handoffs | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant definitions and ratio values | Revolving Credit Agreement, compliance certificate | Headroom and step-up status cannot be traced | CP-1, CP-2 top risks | Leverage view rests on management statements | Credit agreement and amendments |
| G2 | Revolver availability and total liquidity | Liquidity disclosure in MD&A | Liquidity view is not traceable | CP-2 liquidity row | Low confidence on liquidity | FY2025 MD&A and later liquidity disclosure |
| G3 | Run-Rate EBITDA Adjustments bridge | Management bridge | Quality of the stated leverage ratio | CP-1, CP-2 leverage | Stated ratio not auditable | Management bridge or investor presentation |
| G4 | Indentures, guarantors, change-of-control terms | Legal documents | Take-private event risk and ranking | CP-1A, CP-2 | Event risk not assessable | Indentures and credit agreements |
| G5 | FY2025 annual exhibits | 40-F exhibits 99.1 to 99.3 | Original FY2025 figures and maturity table | CP-1 trend | Comparatives revised and unbridged | 40-F exhibits |
| G6 | Events after the Q3 statements | Later 6-K filings | Status at the as-of date | Monitoring | Currency of the view | EDGAR filings to the cutoff |
| G7 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical .md / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / gfl-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed with one MINOR finding | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 1 / same run | Quarterly financials, debt, covenants, definitions | High | Six headings; accepted | Passed with one MINOR locator finding | Calculations recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, transaction, governance | High | Six headings; accepted | Passed with three MINOR findings | Includes a conflicts entry that is not a real conflict |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Restricted by one MATERIAL finding | Confidence Medium for business, Low for forward leverage |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Q2 debt table locator | Supported | Cited page:11, content is on page:10 | Cite page:10 | None |
| MINOR | CP-1A | Q1 Board approval locator | Supported | Cited page:3, content is on page:4 | Cite page:4 | None |
| MINOR | CP-1A | Special Committee timeline date | Supported in substance | Formation date not stated in sources | Date as announced | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Net debt over trailing reported Adjusted EBITDA | Excludes only one month of SECURE and is not the covenant ratio; labelled as such | None | Keep the label and the management ratio beside it | None |
| MINOR | CP-2 | Implied Q4 figures from guidance | Net capex definition not supplied; Q4 cash interest and free cash flow implied by guidance look unusual | None | Treat as unverified, as CP-2 does | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1A, CP-2 | Effect of a take-private or change of control on notes and facilities | Indentures, credit agreements | Documents not supplied; claims marked Insufficient Information | Supply documents | Required before any event-risk view |
| MINOR | CP-1, CP-2 | Covenant thresholds and step-up | Executed credit agreement | Description only | Supply agreement | Required for headroom |
| MINOR | CP-1, CP-1A | Collateral release on the 6.750% 2031 notes | Indenture | Release stated in the note; terms not supplied | Supply indenture | Required to judge willingness |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made; prices, spreads and ratings are outside the minimum set | Prices, spreads, ratings | Recorded by design | Add market modules only with sourced market data | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-2 | CP-1 gaps say revolver availability is not calculable; CP-2 strengths call the revolver largely undrawn | CP-2 cites CP-1 hash fd0b36c4 correctly | Correct CP-2 wording in a new run | Liquidity impression in the report |
| MINOR | CP-1A | Conflicts entry compares a consideration figure with an annualized revenue claim, which are different quantities | None | Log no conflict | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | Reported results and debt table are traceable; post-SECURE leverage headroom and liquidity are not; review is a self-review | Supply covenant, liquidity and legal documents; independent review | Committee status Requires More Work |
| MINOR | CP-1, releases | Duplication | The releases repeat the interim statements; statements are treated as controlling and the releases are not counted as corroboration of non-IFRS measures | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 | Next module paragraph and note on file date labels | Final sentence is garbled; file date labels described as period end for statements but the Q3 statements file carries a later date | Clean wording in a later run | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MATERIAL | CP-2 | Unsupported claim | Revolver described as largely undrawn though 868.0 of 2,025.0 is drawn | Correct wording; state availability not supplied | Restricts committee use of the liquidity view | Open |
| QA-2 | MINOR | CP-1A, CP-2 | Inference | SECURE financing link and hedging breadth stated more firmly than sources allow | Tag as inference | None | Open |
| QA-3 | MINOR | CP-1, CP-1A | Locator | Two off-by-one page locators | Correct | None | Open |
| QA-4 | MINOR | CP-1A | Date and conflicts | Special Committee date; non-conflict logged as conflict | Correct | None | Open |
| QA-5 | MINOR | CP-0 | Wording | Garbled last sentence; date label description | Correct | None | Open |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Number trace | Every distinct decimal and comma-grouped number in each handoff searched as text in the pinned sources | CP-0: 13 numbers, all found. CP-1A: 51, all found. CP-1: 165, of which 11 not found (1,844.4; 2,128.2; 2,780.8; 3.62; 3.78; 3.82; 3.93; 31.49; 4,248.8; 5.05; 705.0), all CP-1 calculations. CP-2: 56, of which 8 not found (1,844.4; 2,128.2; 2,492.5; 4,248.8; 4.57; 5.05; 741.6; 746.6), all calculations. Presence of a number is not proof of correct attribution, so key figures were also checked by page |
| Q2 | Calculation recomputation | The 22 rows of the CP-1 calculations table and the 6 CP-2 rows recomputed from inputs in the sources | 22 of 22 and 6 of 6 equal (CP-2 net capex row is Not calculable by design) |
| Q3 | Locator spot check | About 30 page locators in CP-1 and CP-1A checked by searching the page text | 28 correct, 2 off by one page |
| Q4 | Instrument tie-out | Twelve debt lines added | 11,696.4, equal to the printed subtotal |
| Q5 | Confidence Score | scripts/confidence_score.py --lineage "Directly Sourced:4,Calculated:2,Analyst Inference:2,Insufficient Information:2" --fields-present 17 --fields-total 17 --source-gate partial --findings MATERIAL:1,MINOR:5 | score = clamp((0.6 x 66 + 0.4 x 100) x 0.7 - 30) = 25.72, rounded to 26; band Insufficient Information; qa_status Restricted |

## Gaps

- G1 Critical for the decision: covenant definitions, ratio values and step-up status are not supplied.
- G2 Critical for liquidity: revolver availability and total liquidity are not supplied; CP-2 wording on this point is wrong (QA-1).
- G3: the Run-Rate EBITDA bridge of CAD 730.9 million is not supplied.
- G4: indentures, guarantors and change-of-control terms are not supplied.
- G5: the FY2025 annual exhibits are not supplied.
- G6: events after the Q3 statements and the outcome of the November 9, 2026 deadline are unknown.
- G7: no independent review; this CP-5 was written by the same host.

## Next module

- Report delivery: carry qa_status Restricted, Confidence Score 26 (Insufficient Information), committee status Requires More Work, finding QA-1 and gaps G1 and G2.
- Swarm review step: an independent agent or model should repeat this check, starting with omissions, claims about liquidity and the take-private event.
- Sourcing: obtain the credit agreement, indentures and FY2025 MD&A, then rerun CP-1A, CP-2 and CP-5 in a new run folder with the CP-2 revolver wording corrected.
