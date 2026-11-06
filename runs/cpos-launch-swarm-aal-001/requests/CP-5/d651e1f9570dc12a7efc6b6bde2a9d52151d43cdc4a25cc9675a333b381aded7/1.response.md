## Request

Evidence trace validation and research integrity grade (CP-5 with the absorbed CP-5A phase) for American Airlines, Inc., as of 2026-11-05, pathway credit_snapshot, over the CP-0, CP-1, CP-1A and CP-2 handoffs of run aal-2026-11-05-credit_snapshot-host. Traceability scope is the top five credit drivers plus every defect found. This module changes no credit conclusion and silently repairs nothing.

## Sources

### Issuer sources checked

| Source (exact name) | sha256 |
|---|---|
| 10-K_2025-12-31_aal-20251231.htm.jsonl | 241cb406125cf4a40a3dec4d315c7a8e709f73f5f12957d46a28f056de7b338c |
| 10-Q_2026-03-31_aal-20260331.htm.jsonl | bd54f0ef7be7c4905b1acb2a15d1e60b5211836b6a174b954a6d8e979771d4f3 |
| 10-Q_2026-06-30_aal-20260630.htm.jsonl | e590d34e327bfac4cc2a446c7444656df89c4b6aac523f8df741e9c71b1ace9a |
| 10-Q_2026-09-30_aal-20260930.htm.jsonl | edb09356472b6a21c11979d0ace904761af85e302b5218542813aede49a0decc |
| EX-99.2_2026-04-23_earningspresentation.htm.jsonl | 9a2e0cf77a5348cca76e4e1fa089b91044513dded2916dcf498cbc76a4f142fe |
| EX-99.2_2026-07-23_earningspresentation.htm.jsonl | 60d450333d317c8f5bcb2c0834ff53272fd96fa253d4a67d36813c30742d7ee9 |
| EX-99.2_2026-10-22_earningspresentation.htm.jsonl | ce6723a4b2e59ac217d38de9b2fa855bbf5fa9fd11b713b0732222688fa7865b |

The run context (sha256 98f1f716e6f02a189c11cf5090f848cbc3d38a64fb4114f8c880e8ed58e5a16a) carries settings only and is not issuer evidence.

### Upstream handoffs audited

| Module | sha256 |
|---|---|
| CP-0 | c9fc1ee51323e9485527b31166514f55845df1128f8859f71310606b529d8791 |
| CP-1 | 70223bba15c1520b15ac80c58f3e614e36c2f94213390621338d6bf3ca601fdc |
| CP-1A | 37a396f815173181e9565663399d31e78c068be0957106b32a758ab0fdbccd3b |
| CP-2 | a241bffd065e11d75c5e89391326f7272bb84b41c9e216b03cc596616d0ea8d5 |

## Findings

### Traceability conclusion

Evidence traceability for this run is adequate for committee reading, with remediation. The financial figures in the CP-1 table trace to named pages of the filings: I found each reported value on its cited page, and the calculations reproduce from their stated inputs. Three defects need correction rather than silent repair: a garbled net debt bullet in CP-1, a CP-1A statement that revenue was a record in each of the last three quarters (the decks say so only for the first two), and a CP-2 sentence implying partner cash is the loan collateral, which the filings do not say. The most important provenance gap is the absence of executed financing documents, so covenant statements rest on summaries.

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 3 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the missing executed financing documents, which matters because covenant, collateral and guarantor claims in CP-1, CP-1A and CP-2 cannot be tested against operative terms and implies that covenant headroom and loss-given-default views stay unassessed for committee use. Module Status: Ready with Limitations. Traceability Scope: Top 5. Committee status: Restricted for covenant and recovery uses; permitted for the liquidity, earnings and maturity views once the three corrections below are carried.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
|---|---|---|---|---|---|---|---|
| S1 | 10-K_2025-12-31_aal-20251231.htm.jsonl | High: audited annual report, filed | FY2025 with FY2024 and FY2023 comparatives | AAG consolidated and American consolidated | Statements, debt note, contractual obligations, business, fleet, labor, exhibit list | Exhibits referenced, not supplied | CP-1 prior-period figures, CP-1A business facts |
| S2 | 10-Q_2026-03-31_aal-20260331.htm.jsonl | High: unaudited filed quarterly report | Q1 2026 | AAG and American | Q1 cash flow and statements | Condensed notes | CP-1 discrete cash flow |
| S3 | 10-Q_2026-06-30_aal-20260630.htm.jsonl | High: unaudited filed quarterly report | Q2 2026 and six months | AAG and American | Six-month cash flow | Condensed notes | CP-1 discrete cash flow |
| S4 | 10-Q_2026-09-30_aal-20260930.htm.jsonl | High: unaudited filed quarterly report, signed October 22, 2026 | Q3 2026 and nine months | AAG and American | Statements, debt note, liquidity, covenants text, maturities, MD&A drivers | Cash flow year to date only; covenant levels absent | CP-1, CP-1A, CP-2 |
| S5 | EX-99.2_2026-04-23_earningspresentation.htm.jsonl | Medium: management presentation, text layer only | Q1 2026 | AAG | Non-GAAP reconciliations, total debt, free cash flow, EBITDAR | Charts and images not inspected | CP-1 Q1 comparatives, CP-1A management language |
| S6 | EX-99.2_2026-07-23_earningspresentation.htm.jsonl | Medium: management presentation, text layer only | Q2 2026 | AAG | Reconciliations, outlook | No debt or cash flow reconciliation | CP-1 Q2 operating income, net income |
| S7 | EX-99.2_2026-10-22_earningspresentation.htm.jsonl | Medium: management presentation, text layer only | Q3 2026 | AAG | Net debt, liquidity, outlook, reconciliations | Net debt chart series not mappable from text | CP-1 leverage inputs, CP-1A and CP-2 guidance |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
|---|---|---|---|---|---|---|---|
| 1 | Unhedged fuel compressing operating income | CP-1 | Q3 2026 fuel expense 4,635 against 2,767 and operating income 115 against 151 | Fuel price passes to operating income and cash flow within a quarter | Drives coverage, liquidity burn and default risk | S4 page:6, page:44, page:48 | Management guidance is a forecast |
| 2 | Leverage far above management target | CP-1 | Management net debt 28,079 and LTM EBITDAR 4,127 built from income statement lines | Sets leverage tolerance and deleveraging path | Frames refinancing capacity | S7 page:10; S1 page:142; S4 page:6 | EBITDAR excludes regional depreciation and rent; AAG perimeter, not American |
| 3 | Liquidity with undrawn facilities | CP-1 | Total available liquidity 11,763 for American and 11,797 for AAG | Buffer against earnings shortfall | Primary mitigant | S4 page:59, page:60 | Includes facilities with 2026 and 2028 expiries |
| 4 | 2028 maturity concentration | CP-1 | American principal due 7,861 in 2028 | Peak refinancing year | Needs secured market access | S4 page:65 | Instrument split of 2028 not supplied |
| 5 | Dependence on float for operating cash flow | CP-1 | Air traffic and loyalty liabilities 20,928 against 17,722; derived Q3 operating cash flow (153) | Reversal drains liquidity | Quality of cash generation | S4 page:7, page:13, page:8; S3 page:8 | Discrete quarter derived by difference |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
|---|---|---|---|---|---|---|---|---|
| Fuel compresses operating income | CP-1, CP-2 | S4 page:6 income statement rows; page:48 fuel price per gallon 3.85 against 2.37 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Leverage 6.80x on net debt to LTM EBITDAR | CP-1, CP-2 | S7 page:10 net debt 28,079; EBITDAR from S1 page:142 and S4 page:6 | Yes | High and Medium | Calculated | Supported with definition limits | Medium | Remediation Needed |
| Liquidity 11,763 and 11,797 | CP-1, CP-2 | S4 page:59, page:60 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| 2028 principal 7,861 | CP-1, CP-2 | S4 page:65 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Float dependence | CP-1, CP-2 | S4 page:7, page:13; derived Q3 operating cash flow from S3 page:8 and S4 page:8 | Yes | High | Calculated | Supported | Medium | Committee-Ready |
| Record revenue in each of the last three quarters | CP-1A | S5 and S6 state records for Q1 and Q2; S7 does not | Partial | Medium | Untraced | Unsupported for Q3 | Low | Remediation Needed |
| Partner cash is the collateral base of the AAdvantage Financing | CP-2 | S4 page:16 lists loyalty program assets among collateral; cash payments are in S1 page:13 | Partial | High | Analyst Inference | Partially supported | Low | Remediation Needed |
| Net debt fell between Q1 and Q3 2026 (garbled CP-1 bullet) | CP-1 | S5 page:11 net debt 27,438; S7 page:10 net debt 28,079 | Yes | High | Conflicting | Contradicted by cited sources | Low | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
|---|---|---|---|---|---|---|---|---|
| Q3 2026 revenue 16,335 and operating income 115 | Income statement | 10-Q_2026-09-30_aal-20260930.htm.jsonl | S4 | page:6 | CP-1 table | Sourced | High | Found on page |
| Nine-month operating cash flow 4,541; capex 2,728 | Cash flow statement | 10-Q_2026-09-30_aal-20260930.htm.jsonl | S4 | page:8 | CP-1 table | Sourced | High | Found on page |
| Total debt per Note 5 29,321; secured 25,575; unsecured 3,746 | Note 5 Debt | 10-Q_2026-09-30_aal-20260930.htm.jsonl | S4 | page:15 | CP-1 table, CP-2 | Sourced | High | Found on page |
| Available liquidity 11,797 (AAG) and 11,763 (American) | Liquidity table | 10-Q_2026-09-30_aal-20260930.htm.jsonl | S4 | page:59, page:60 | CP-1, CP-2 | Sourced | High | Table split across pages |
| American principal due 631, 3,550, 7,861, 3,884, 972, 8,677 | Contractual obligations | 10-Q_2026-09-30_aal-20260930.htm.jsonl | S4 | page:65 | CP-1 table, CP-2 | Sourced | High | Sums to 25,575 |
| Covenant types and compliance statement | Certain Covenants | 10-Q_2026-09-30_aal-20260930.htm.jsonl | S4 | page:61 | CP-1, CP-1A | Sourced | High | Thresholds not stated |
| Management net debt 28,079 and total debt 36,366 | Appendix reconciliation | EX-99.2_2026-10-22_earningspresentation.htm.jsonl | S7 | page:10 | CP-1, CP-2 | Sourced | Medium | Management non-GAAP |
| Cash from co-branded card and other partners 6.2 billion in 2025 | Item 1 Business | 10-K_2025-12-31_aal-20251231.htm.jsonl | S1 | page:13 | CP-1A, CP-2 | Sourced | High | Found on page |
| Mainline fleet 1,013 with 547 owned and 466 leased | Item 2 Properties | 10-K_2025-12-31_aal-20251231.htm.jsonl | S1 | page:100 | CP-1A, CP-2 | Sourced | High | Year-end 2025 |
| Salaries, wages and benefits 38% of 2025 operating expenses; contracts amendable 2027 | Item 1 Business | 10-K_2025-12-31_aal-20251231.htm.jsonl | S1 | page:17, page:19 | CP-1A, CP-2 | Sourced | High | Found on page |
| No hedges outstanding at September 30, 2026 | MD&A Fuel | 10-Q_2026-09-30_aal-20260930.htm.jsonl | S4 | page:44 | CP-1, CP-1A | Sourced | High | Found on page |
| Premium products about half of ticket revenue on about 30% of seats | Deck narrative | EX-99.2_2026-10-22_earningspresentation.htm.jsonl | S7 | page:5 | CP-1A | Sourced | Medium | Management Language, correctly tagged |
| Record revenue in each of the last three quarters | Deck narrative | EX-99.2 decks | S5, S6, S7 | Q1 and Q2 deck page:4 only | CP-1A credit translations | Untraced for Q3 | Medium | Q3 deck states growth, not a record |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
|---|---|---|---|---|---|---|---|---|
| LTM revenue, operating income, D&A, rent, interest | CP-1 C1 to C6 | FY2025 plus nine months 2026 less nine months 2025 | Stated in CP-1; recomputed here and matched | Calculated | Supported | High | Coverage, leverage | S1 page:142; S4 page:6 |
| LTM EBITDA and EBITDAR | CP-1 C4, CP-2 | Operating income plus income statement D&A plus aircraft rent | Stated in CP-1; reproduces to 2,891 and 4,127 | Calculated | Supported with definition drift | Medium | Leverage, coverage | S1 page:142; S4 page:6 |
| Leverage multiples | CP-1 C13, C14 | Balance sheet debt 29,635; management total debt 36,366; net debt 28,079 | Ratios of stated inputs; recomputed to 10.25x, 8.81x, 6.80x | Calculated | Supported | Medium | Leverage tolerance | S4 page:7; S7 page:10 |
| Interest coverage | CP-1 C15 | EBITDA 2,891; interest expense, net 1,664 | Ratio; recomputed 1.74x | Calculated | Supported | Medium | Debt service | S1 page:142; S4 page:6 |
| Discrete Q3 cash flow | CP-1 C7 | Nine months less six months | 4,541 less 4,694; 2,728 less 1,633 | Calculated | Supported | Medium | Liquidity, cash quality | S3 page:8; S4 page:8 |
| Simple free cash flow | CP-1 C8 | Operating cash flow less capex and aircraft deposits | Stated; management defines free cash flow differently | Calculated | Supported with definition drift | Medium | Cash conversion | S4 page:8; S5 page:10 |
| Covenant headroom indication | CP-1 C16 | Cash 1,124 plus undrawn 3,510 against a 2.0 billion minimum | Sum; treatment of short-term investments not stated | Calculated | Partially supported | Low | Liquidity covenant | S4 page:7, page:15, page:61 |
| Covenant compliance margin on LTV and debt service coverage | Not computed | Thresholds not supplied | No formula possible | Not Calculable | Unsupported | Low | Default risk | S4 page:61 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
|---|---|---|---|---|---|---|
| Material | Net debt movement between Q1 and Q3 2026 | CP-1 bullet states net debt fell then trails into a note; sources show net debt rose from 27,438 to 28,079 | Conflicting | A reader could take leverage as improving when it worsened, which understates refinancing and coverage risk | Treat CP-1A and CP-2 corrections as controlling: net debt and total debt rose | CP-1 Findings, Latest quarter changes |
| Material | Revenue record in each of the last three quarters | Decks support records for Q1 and Q2 only | Untraced | Overstates revenue momentum, a revenue durability input | Restrict to Q1 and Q2, or drop | CP-1A Credit translations |
| Material | Partner cash is the collateral base of the AAdvantage Financing | Filing lists loyalty program assets as collateral; it does not say partner cash is the base | Analyst Inference | Overstates recovery support for the secured loan | Reword as loyalty program assets and related cash flows are among collateral | CP-2 Key findings |
| Material | Leverage ratios use AAG consolidated inputs | Issuer is American, whose own EBITDA, debt (25,876) and interest differ | Weak Lineage | Ratio perimeter differs from the credit's obligor | Compute American-perimeter ratios or label as AAG | CP-1 C13 to C15; CP-2 Key findings |
| Minor | Phrase that the LTM ratio is conservative | Wording is contradictory about direction | Weak Lineage | Confuses reader on whether leverage is over or understated | CP-1A note states it overstates relative to management adjusted EBITDAR | CP-1 Credit read-through |
| Minor | PSP notes issue history | Locator for PSP notes in CP-1A timeline points to fleet and debt pages that do not describe issue dates | Weak Lineage | None for credit view; minor lineage defect | Cite Q3 page:15 | CP-1A Timeline |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
|---|---|---|---|---|---|
| Source coverage | Ready with Remediation | Seven filings and decks cover FY2025 to Q3 2026; no executed debt documents | Covenant and guarantor claims rest on summaries | Default and loss-given-default views cannot be tested | Obtain executed credit agreements and indentures |
| Citation completeness | Ready with Remediation | Every CP-1 reported value found on its cited page; three defects in CP-1, CP-1A and CP-2 | Unsupported statements can reach the committee | Momentum and collateral support may be overstated | Carry the three corrections |
| Calculation traceability | Committee-Ready | Calculations C1 to C18 recomputed and matched | Definition drift on EBITDAR could mislead if unlabelled | Leverage comparisons to the 3.0x target are indicative | Label definition on use |
| Assumption transparency | Committee-Ready | No forward assumptions are used; guidance is tagged as management forecast | Forecasts could be read as results | Low | None |
| Markdown and export artifact integrity | Ready with Remediation | Handoffs carry the six host-mode headings but not the canonical envelope headings of the method | Registers differ from the full-run template | Tool integration only | Convert in the report build |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
|---|---|---|---|---|---|---|
| CP-5-GAP-001 | Executed financing documents absent | Credit agreements, indentures, EETC documents | Covenant, collateral and guarantor terms drive default and recovery mechanics | CP-1, CP-1A, CP-2 covenant statements | High impact | Exhibits listed in the 10-K and 10-Q exhibit indexes |
| CP-5-GAP-002 | Covenant thresholds and test dates not stated | Numeric LTV, debt service coverage and liquidity tests | Headroom cannot be assessed | CP-1 liquidity and covenants; CP-2 risks | High impact | Executed documents; compliance certificates |
| CP-5-GAP-003 | American-perimeter leverage not computed | American EBITDA and interest for LTM | Obligor and ratio perimeter differ | CP-1 C13 to C15 | Medium impact | American statements in the same filings |
| CP-5-GAP-004 | Management adjusted EBITDAR only for Q1 2026 | LTM adjusted EBITDAR build including regional | Leverage versus 3.0x target not comparable | CP-1, CP-2 | Medium impact | Management reconciliation or cash flow D&A and rent |
| CP-5-GAP-005 | Cash taxes paid not located | Supplemental cash flow line | Cash conversion detail | CP-1 | Low impact | Income tax note |
| CP-5-GAP-006 | Deck charts and images not inspected | Image and speaker notes | Management claims not traceable beyond text | CP-1A, CP-2 | Low impact | Original deck files |
| CP-5-GAP-007 | Intercompany terms and PSP origin | Terms of the receivable from related parties and PSP issuance | Value flow between American and AAG | CP-1A, CP-2 structure points | Medium impact | Notes and parent filings |
| CP-5-GAP-008 | Ratings, prices and collateral values absent | Ratings, quotes, appraisals | Recovery and market views cannot be formed | CP-2 | Medium impact | Rating reports, appraisals |

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
|---|---|---|---|---|---|---|
| CP-0 | requests/CP-0 response, sha256 c9fc1ee5...8d791, run aal-2026-11-05-credit_snapshot-host | Source readiness for seven sources | High and Medium | Six host-mode headings present; method envelope fields absent | Accepted by CP-OS structure check | Quotes verified verbatim on cited pages |
| CP-1 | requests/CP-1 response, sha256 70223bba...01fdc | Financials, debt, liquidity, metrics | High and Medium | Six host-mode headings and required table present; envelope absent | Accepted by CP-OS structure check | One garbled bullet |
| CP-1A | requests/CP-1A response, sha256 37a396f8...3b0732222688fa7865b is not part of this id; full hash 37a396f815173181e9565663399d31e78c068be0957106b32a758ab0fdbccd3b | Business, ownership, transactions, governance | High and Medium | Required three selector sections present; envelope absent | Accepted by CP-OS structure check | One unsupported statement; one locator slip |
| CP-2 | requests/CP-2 response, sha256 a241bffd065e11d75c5e89391326f7272bb84b41c9e216b03cc596616d0ea8d5 | Credit synthesis | Derived from CP-1 and CP-1A | Credit view and selector sections present; envelope absent | Accepted by CP-OS structure check | One collateral inference |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
|---|---|---|---|---|---|---|
| Material | CP-1A | Credit translations: record revenue in each of the last three quarters | Unsupported | Only the Q1 and Q2 decks describe records | Restrict to Q1 and Q2 | Remediate before committee use |
| Material | CP-2 | Key findings: partner cash as collateral base | Partially Supported | Filing lists loyalty program assets as collateral | Reword | Remediate before committee use |
| Material | CP-1 | Latest quarter changes: net debt bullet | Conflicting | Bullet contradicts its own sources | Use corrected statement from CP-1A | Remediate before committee use |
| Minor | CP-1A | Timeline locators for PSP notes | Partially Supported | Locators do not describe PSP issue | Cite Q3 page:15 | None |
| Minor | CP-1 | Reported table values | Supported | 174 reported values found on their cited pages | None | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
|---|---|---|---|---|---|---|
| Material | CP-1, CP-2 | Leverage ratios use AAG inputs for an American obligor | EBITDA from income statement lines excludes regional depreciation and rent; management adjusted EBITDAR differs | None between sources; definition drift | Label perimeter and definition on every use; add American-perimeter ratio | Restricts comparison with the 3.0x target |
| Minor | CP-1 | Free cash flow uses a simple definition | Management defines free cash flow with short-term investment and restricted cash adjustments | Not a conflict, a definition difference | Keep labels as written | None |
| Minor | CP-1 | Covenant liquidity indication | Qualifying cash and investments not defined in the text | None | Keep marked indicative | None |
| Minor | CP-1 | Discrete Q3 cash flow | Derived by difference of year-to-date filings | None | Keep marked derived | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
|---|---|---|---|---|---|---|
| Critical | CP-1, CP-1A, CP-2 | Covenants include loan to value, minimum liquidity and debt service coverage tests and the issuer is in compliance | Executed credit agreements, indentures, compliance certificates | Operative terms absent; claim rests on 10-Q summary | Keep statements at filing-summary level; obtain documents before any covenant conclusion | Required before covenant or recovery use |
| Material | CP-1A, CP-2 | PSP notes are unsecured at the AAG parent and outside American's maturity table | PSP promissory note agreements | Agreements absent; position inferred from the maturity table presentation | Confirm obligor and ranking | Required for structural subordination view |
| Material | CP-1A | Guarantor and restricted group perimeter by instrument | Credit and guaranty agreements | Not supplied | Obtain documents | Required for structure view |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
|---|---|---|---|---|---|---|
| Minor | CP-1, CP-1A, CP-2 | No relative value, pricing or spread claim is made in any module; the method prohibits them at this stage | Prices, spreads, yields, ratings, peer data | None needed for the claims made | None; keep excluded | None for the credit view; relative value is not supported by this run |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
|---|---|---|---|---|---|
| Material | CP-1, CP-1A, CP-2 | CP-1 net debt bullet contradicts CP-1A and CP-2, which correct it | Accepted CP-1 cannot be edited; correction lives in later handoffs | Carry CP-1A note as controlling | Reader of CP-1 alone is misled |
| Minor | CP-1, CP-2 | Liquidity of AAG (11,797) versus American (11,763) used interchangeably in prose | Both are correct for their perimeter | Label perimeter | Low |
| Minor | CP-0, CP-1 | CP-0 inner file hashes differ from pinned hashes by design | Pinned hashes control | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
|---|---|---|---|---|---|
| Minor | CP-1, CP-2 | Duplication | Leverage, liquidity and maturity points appear in CP-1, CP-1A and CP-2 | Keep one statement in the report | Readability only |
| Material | CP-1A | Materiality | Revenue momentum overstated by the unsupported record statement | Correct | Affects revenue durability view |
| Material | CP-2 | Committee readiness | Confidence Medium is consistent with open gaps | Keep | Appropriate |

#### T5.8 Handoff structure and export audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
|---|---|---|---|---|---|
| Minor | CP-0 to CP-2 | Envelope | Host-mode handoffs omit the method's front-matter envelope and canonical H2 names such as Audit Summary and Evidence Trace | Build in report assembly | Report builder reads host-mode sections |
| Minor | CP-1 | Table selector | One table under Financials and credit metrics is present | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
|---|---|---|---|---|---|---|---|
| CP-5-ISS-001 | Critical | CP-1, CP-1A, CP-2 | Legal | Covenant statements rest on a 10-Q summary; no executed documents | Obtain documents | Blocks covenant and recovery use | Open |
| CP-5-ISS-002 | Material | CP-1 | Consistency | Net debt bullet contradicts sources | Use CP-1A correction | Remediation needed | Open |
| CP-5-ISS-003 | Material | CP-1A | Citation | Record revenue statement unsupported for Q3 | Restrict to Q1 and Q2 | Remediation needed | Open |
| CP-5-ISS-004 | Material | CP-2 | Citation | Partner cash described as collateral base | Reword | Remediation needed | Open |
| CP-5-ISS-005 | Material | CP-1, CP-2 | Definition | Leverage on AAG perimeter and income statement EBITDAR | Label; add American ratio | Restricts target comparison | Open |
| CP-5-ISS-006 | Minor | CP-1A | Citation | PSP notes locator | Cite Q3 page:15 | None | Open |
| CP-5-ISS-007 | Minor | All | Structure | Host-mode envelope differs from method template | Convert in report assembly | None | Open |

#### Remediation priority and clearance decision

Priority 1: obtain executed financing documents (CP-5-ISS-001). Priority 2: carry the three corrections (CP-5-ISS-002 to 004). Priority 3: add American-perimeter ratios and label definitions (CP-5-ISS-005). Clearance decision: committee use is Restricted. The earnings, liquidity and maturity views are permitted once the three corrections are carried; covenant, collateral and recovery views are blocked until executed documents are supplied. QA confidence: Medium.

## Calculations

No new analytical calculation was made. Verification work performed:

- Recomputed CP-1 calculations C1 to C18 from the stated inputs. All matched: LTM revenue 60,981; LTM operating income 973; EBITDA 2,891; EBITDAR 4,127; interest expense, net 1,664; debt and finance leases 29,635 and 25,876; leverage 10.25x, 8.81x, 6.80x; coverage 1.74x, 0.58x, 1.42x; discrete Q3 operating cash flow (153), capex 1,095, free cash flow (1,248).
- Checked that each of 174 reported (non-calculated) CP-1 table values appears on the page cited for it in the pinned source text. All were found; this confirms presence on the page, not that the label matches, which was sampled by reading the pages.
- Checked that the CP-0 citation quotes are exact substrings of their cited pages; all passed after one locator correction made before acceptance.

## Gaps

The consolidated gaps are in the gaps ledger above (CP-5-GAP-001 to CP-5-GAP-008) and the issue log (CP-5-ISS-001 to CP-5-ISS-007). The critical gap is the absence of executed financing documents. Extraction fidelity of the converted text against the original filings was not reviewed.

## Next module

This is the last module in the minimum set. Publish the report with the three corrections carried as noted: net debt rose between March 31 and September 30, 2026; revenue was described as a record only in the first and second quarter decks; and partner cash is not stated to be the loan collateral. Keep covenant and recovery content restricted until executed documents are supplied.
