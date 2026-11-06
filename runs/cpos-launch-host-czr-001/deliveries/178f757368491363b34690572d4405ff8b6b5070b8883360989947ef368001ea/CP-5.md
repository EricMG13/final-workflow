# CP-5 — Evidence trace and research-integrity QA: Caesars Entertainment, Inc. (czr)

## Request

- Issuer: Caesars Entertainment, Inc. (issuer id `czr`), as of 2026-10-02, information cutoff 2026-10-02.
- Run: `czr-2026-10-02-credit_snapshot-host`, pathway `credit_snapshot`, `minimum` module set. CP-5 checks CP-0, CP-1, CP-1A and CP-2 and grades the result (absorbed CP-5A phase).
- Execution: host session. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called.
- Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- QA envelope: `qa_status` Passed; Confidence Score 47, band Low (from `scripts/confidence_score.py`, see Calculations); `committee_status` Requires More Work.

## Sources

| Source | sha256 |
| --- | --- |
| CZR_FY2025_10K.txt | 172309048af2a6a2dab515d765f00a7c89bf8c874c6104a5e3a052b66cad4512 |
| CZR_Q2_2026_10Q.txt | f369ce5f1ebeddd9a0d4ce02ce3958112267d8701d1a348dfd6dc82d2034793a |
| CZR_Q2_2026_Earnings_Release.txt | b385f76ff631243d1053fa8073ebde4f8886b4a50c9ce34ce3498d6b2ac3e9f8 |
| context | 70a1a94c5cc4a6bf8f11bf47e9f0a41d9be046e2bcfa93425809b6450d15d5c1 |

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | c25e5a54d628dec4614d6d52f99b207b6b261bfcb442c3bed0d41c0af7f514a3 |
| CP-1 | 61c83d3e3ee8df68a362930def996cf678e2e35924dc16aa46093cfd4d02ba30 |
| CP-1A | 89de62ee6354c11acba13cac4ef871638c52f2ac6bcb8731ef91f99f58e5c17f |
| CP-2 | 43ffa3dd2cbc9914263ec4b17e9172e2b69e0e807efec56e0701aa850a87d7a3 |

Locators are line numbers of the pinned text files.

## Findings

### Traceability conclusion

The run is traceable enough for a view of Caesars' current capital structure, and not for the decision that matters most, the post-merger credit. Every CP-1 metric used by CP-2 reproduces exactly from the cited source lines, and every checked quotation is on its cited lines or carries a resolvable locator. Coverage of material claims: four directly sourced, three calculated, two Insufficient Information. The critical provenance gap is the merger financing and the treatment of existing debt and leases: CP-2's top risk and its Medium confidence rest on it, and no supplied source describes it. The affected decision is any view beyond closing. Remediation owner: the sourcing step, which must add the Merger Agreement and financing documents. Four minor locator and restatement defects need no change to any conclusion.

| Traceability summary | Result |
| --- | --- |
| Quotations checked against cited lines | 59 quotations in four handoffs; none misquoted; 7 with imprecise locators |
| CP-1 metrics recomputed from cited source lines | 15 of 15 equal |
| Statement totals and reconciliations re-added | 24 of 24 equal |
| CP-2 figures found in CP-1 or CP-1A | All, three as rounded billions |
| Material claims by lineage | 4 Directly Sourced, 3 Calculated, 2 Insufficient Information |
| Open findings | 4 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | CZR_FY2025_10K.txt | High: filed, audited annual report | Years ended December 31, 2025, 2024 and 2023 | Caesars Entertainment, Inc., consolidated | Statements, debt note, Adjusted EBITDA reconciliation, business, history | Text conversion of the filed HTML | CP-0, CP-1, CP-1A |
| S2 | CZR_Q2_2026_10Q.txt | High: filed, unaudited interim report | Three and six months ended June 30, 2026 | Same | Interim statements, debt note, covenants, merger terms, liquidity | Text conversion; unaudited | CP-0, CP-1, CP-1A |
| S3 | CZR_Q2_2026_Earnings_Release.txt | Medium: issuer press release | Three and six months ended June 30, 2026 | Same | Segment results, Adjusted EBITDA, net debt | Issuer non-GAAP presentation | CP-1, CP-1A |
| S4 | context | User settings, not evidence | Run date 2026-10-02 | Run identity | Pathway, dates, currency | Not issuer evidence | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Pending take-private with unknown financing | CP-1A, CP-2 | Merger terms in S2 lines 273 to 298 | Can change leverage and debt ranking | Sets the post-closing credit view | S2 lines 273, 294, 296 to 298, 1391 | Financing and debt treatment not supplied |
| 2 | Lease obligations larger than debt | CP-1, CP-2 | Financing obligations 13,157 against debt 11,807 | Fixed, CPI-linked claims outside Adjusted EBITDA | Sets leverage tolerance | S2 lines 89, 507; S3 line 96 | Lease agreements not supplied |
| 3 | Lease-adjusted leverage 5.30x to 6.95x | CP-1 | C4 and C5 | Fuller leverage view than debt-only 3.29x | Core leverage metric | S2 lines 89, 250, 507; S3 line 64; S1 lines 1329, 1868 | Rent label differs by period |
| 4 | Thin coverage 1.57x on total net interest | CP-1 | C6 | Little room for an earnings decline | Debt-service capacity | S1 line 1748; S2 line 126; S3 line 64 | None beyond labels |
| 5 | Adequate near-term liquidity | CP-1 | 2,928 liquidity; no large maturity before 2028 | Low near-term default risk | Monitoring horizon | S2 lines 1282 to 1289, 1296 to 1300 | Status after July 28, 2026 not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Merger terms: 31 US dollars per share, conditions, fees, end dates | CP-1A | S2 lines 273 to 298 | Yes | High | Documentary Fact | Supported | High | Traced |
| Merger financing and debt treatment | CP-1A, CP-2 | No source in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Lease obligations exceed debt | CP-1, CP-2 | S2 lines 89 and 507 | Yes | High | Documentary Fact | Supported | High | Traced |
| Lease-adjusted leverage and coverage | CP-1 | C4, C5, C6 from S1, S2, S3 lines | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Earnings flat, margin down | CP-1, CP-2 | C1, C7 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Liquidity 2,928 and maturities | CP-1 | S2 lines 1282 to 1289 and debt service table | Yes | High | Documentary Fact | Supported | High | Traced |
| Covenant compliance | CP-1 | S2 line 600 | Yes | High; management statement | Documentary Fact | Supported as a statement | Medium | Traced |
| Covenant headroom | CP-1 | Definitions not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net revenues FY2025 11,486 | cases/czr-2026q2-earnings-update/documents | CZR_FY2025_10K.txt | S1 | Line 1734, statements of operations | CP-1 metrics table | Reported | High | Matches |
| Total debt face 11,807 | cases/czr-2026q2-earnings-update/documents | CZR_Q2_2026_10Q.txt | S2 | Line 507, Note 6 | CP-1 debt register | Reported | High | Components re-added equal |
| Long-term financing obligations 13,157 | cases/czr-2026q2-earnings-update/documents | CZR_Q2_2026_10Q.txt | S2 | Line 89, balance sheet | CP-1 lease section | Reported | High | Matches |
| Adjusted EBITDA six months 2026 1,807 | cases/czr-2026q2-earnings-update/documents | CZR_Q2_2026_Earnings_Release.txt | S3 | Line 64 | CP-1 C1 | Issuer non-GAAP | Medium | Reconciliation re-added equal |
| Merger signed May 27, 2026 | cases/czr-2026q2-earnings-update/documents | CZR_Q2_2026_10Q.txt | S2 | Line 273, Note 1 | CP-1A transaction summary | Reported | High | Matches |
| Covenant 6.50:1 and 2.0:1 | cases/czr-2026q2-earnings-update/documents | CZR_Q2_2026_10Q.txt | S2 | Lines 595 to 596 | CP-1 covenant table | Reported description | High | Matches |
| Remaining 2026 lease payments of about 687 | cases/czr-2026q2-earnings-update/documents | CZR_Q2_2026_10Q.txt | S2 | Line 1300, liquidity | CP-1 lease section | Issuer estimate | High | CP-1 locates it only as "after line 1289" |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM figures | CP-1 C1; CP-2 findings 3 and 4 | FY2025 and both six-month periods | FY2025 + six months 2026 − six months 2025 | Recomputed from cited lines: equal | Supported | High | Basis of every ratio | S1 lines 1329, 1734, 1748, 1833, 1835, 1867, 1868; S2 lines 113, 126, 218, 220, 249, 250; S3 line 64 |
| Lease-inclusive leverage | CP-1 C4; CP-2 finding 1 | Carrying amount of financing obligations | (debt + obligations) / Adjusted EBITDA | Recomputed: 6.95x equal | Supported | High | Leverage tolerance | S2 lines 89, 507 |
| Leverage after cash rent | CP-1 C5 | LTM cash rent combines two labels | debt / (Adjusted EBITDA − cash rent) | Recomputed: 5.30x equal | Supported with label caveat | Medium | Leverage tolerance | S1 line 1868; S2 line 250 |
| Coverage | CP-1 C6; CP-2 finding 3 | Net interest includes lease interest | Adjusted EBITDA / net interest; after-rent / cash interest | Recomputed: 1.57x and 2.87x equal | Supported | High | Debt service | S1 lines 1748, 1867; S2 lines 126, 249 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial gate, 4 MINOR | Script formula | 47, band Low | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 release register | Segment Adjusted EBITDA cited as release lines 52 to 67; the tables run from line 47 to line 64 | Imprecise locator | A reader checking the range misses the first rows | Cite lines 47 to 64 in a later run | CP-0 handoff |
| MINOR | CP-0 identity and read-through | Two quotations carry "(line 106)" and "(line 1391)" without a document name | Ambiguous locator | The sentence names the document, but a parser cannot | Prefix the document name | CP-0 handoff |
| MINOR | CP-1 lease and liquidity text | Three quotations located as "10-Q liquidity section" or "after line 1289"; the quotes are on 10-Q lines 1296, 1298 and 1300 | Imprecise locator | Slower verification; no misquotation | Cite exact lines | CP-1 handoff |
| MINOR | CP-1A and CP-2 summaries | Figures restated as rounded billions, for example about 11.8 and 13.2 billion | Restated figure | Not a literal copy of a CP-1 cell; values agree | Reference the CP-1 cell or keep the exact figure | CP-1A credit translations; CP-2 assessment |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves by cover text | A wrong document would change every figure | None found | None |
| Locator precision | Adequate | 52 of 59 quotations on exactly the cited lines; 7 with imprecise or document-less locators | Slower checks; risk of a misplaced citation | None on conclusions | Exact line locators |
| Calculation reproducibility | Strong | 15 of 15 metrics and 24 of 24 tie-outs recomputed equal | Calculation errors would move leverage | None found | None |
| Cross-module consistency | Strong | All CP-2 figures found in CP-1 or CP-1A; CP-1A and CP-2 cite current CP-1 hash | Inconsistent figures mislead a committee | None found | None |
| Reviewer independence | Weak | Host wrote and checked the handoffs | Shared blind spots go undetected, as the TDG pilot showed | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Merger financing and treatment of existing debt and leases | Merger Agreement, commitment letters, merger proxy | Post-closing leverage and ranking unknown | CP-2 top risk and confidence | Holds the view to the current structure | 8-K of May 28, 2026, exhibit 2.1, and later merger filings |
| G2 | Events after July 28, 2026 | Later 8-Ks and filings | Approval and financing status at the as-of date unknown | Monitoring posture | Lowers currency of the view | EDGAR filings to the cutoff date |
| G3 | Covenant definitions | Executed credit agreement | Headroom Not calculable | Covenant risk row | Covenant view rests on a management statement | Credit agreement and amendments |
| G4 | Lease terms | VICI and GLPI lease agreements | Escalators and variable rent described, not read | Lease burden view | Moderate | Lease agreements |
| G5 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / czr-2026-10-02-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed with two MINOR locator findings | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, LTM, debt, leases, covenants | High | Six headings; accepted | Passed with one MINOR locator finding | All metrics recomputed equal |
| CP-1A | requests/CP-1A attempt 2 / same run | Business, merger, governance | High | Six headings; attempt 1 refused for a split table row, attempt 2 accepted | Passed with one MINOR restatement finding | Quoted pipe characters split a table cell in attempt 1 |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Passed with one MINOR restatement finding | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 | Release register | Supported | Locator range starts mid-table | Cite lines 47 to 64 | None |
| MINOR | CP-0 | Merger announcement and leverage risk quotations | Supported | Document name missing from two locators | Add document name | None |
| MINOR | CP-1 | Lease and liquidity quotations | Supported | Section-level locators | Cite 10-Q lines 1296, 1298, 1300 | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | LTM cash rent | FY2025 label "related to financing obligations"; 2026 label "related to GLPI and VICI Leases" with a separate "other financing obligations" line | Label change, not a value conflict | Keep the after-rent ratios labelled approximate, as CP-1 does | None |
| MINOR | CP-1 | Adjusted EBITDA as leverage denominator | Excludes lease cost by issuer definition (S3 line 96) | None | Keep the lease-inclusive bases beside the debt-only ratio, as CP-1 does | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1A, CP-2 | Effect of the merger on existing debt and leases | Merger Agreement, indentures, credit agreement, leases | Documents not supplied; claims correctly marked Insufficient Information | Supply documents; add CP-4 | Required before any post-closing view |
| MINOR | CP-1 | Covenant thresholds 6.50:1 and 2.0:1 | Executed credit agreement | Description only | Supply agreement | Required for headroom |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made in this run; bond prices, spreads and ratings are outside the minimum set | Prices, spreads and ratings are not part of the minimum source pack | Recorded by design | Add CP-3D or CP-2H only with sourced market data | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A, CP-2 | Rounded billions restate CP-1 figures; values agree | CP-1A attempt 2 is the accepted version and CP-2 cites its hash 89de62ee | Keep exact figures or cell references | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | Current-structure view is traceable; the post-merger view is not; review is self-review only | Supply merger documents and an independent review | Committee status Requires More Work |
| MINOR | CP-1, release | Duplication | The release repeats the 10-Q statement of operations; CP-0 and CP-1 treat the 10-Q as controlling and do not count the release as corroboration | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A | Company and operating model table, attempt 1 | Quoted source text with pipe characters split a table row; refused by the report adapter and repaired in attempt 2 | Avoid pipe characters inside table cells | Resolved; attempt 2 accepted |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-0 | Locator | Release segment range 52 to 67 should be 47 to 64 | Correct in a later run | None | Open |
| QA-2 | MINOR | CP-0 | Locator | Two locators without document name | Add document name | None | Open |
| QA-3 | MINOR | CP-1 | Locator | Three section-level locators | Cite exact lines | None | Open |
| QA-4 | MINOR | CP-1A, CP-2 | Restatement | Rounded billions instead of exact CP-1 figures | Use exact figures | None | Open |
| QA-5 | MINOR | CP-1A | Export | Split table row in attempt 1 | Repaired in attempt 2 | None | Closed |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Each double-quoted phrase in the four handoffs searched on the source lines its sentence cites | 64 quoted spans parsed, of which 5 were parser artifacts; of 59 quotations none is misquoted, 52 are on the cited lines and 7 have imprecise or document-less locators |
| Q2 | Metric recomputation | Inputs parsed from the source lines CP-1 cites; LTM and ratios recomputed with exact fractions | 15 of 15 equal to CP-1 |
| Q3 | Tie-outs | Balance-sheet totals, cash roll-forwards, Adjusted EBITDA reconciliations and debt totals re-added | 24 of 24 equal |
| Q4 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:4,Calculated:3,Insufficient Information:2" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:4` | score = clamp((0.6 × 74.44 + 0.4 × 100) × 0.7 − 12) = 47.27, rounded to 47; band Low; qa_status Passed |

## Gaps

- G1 Critical for the decision: merger financing and the treatment of existing debt and leases are not supplied.
- G2: events after July 28, 2026 not supplied.
- G3 and G4: covenant definitions and lease terms not supplied.
- G5: no independent review; this CP-5 was written by the same host.

## Next module

- Report delivery: carry `qa_status` Passed, Confidence Score 47 (Low), committee status Requires More Work, and gap G1.
- Swarm review step: an independent agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Sourcing: fetch the Merger Agreement (8-K of May 28, 2026, exhibit 2.1) and later merger filings, then rerun CP-1A, CP-2 and CP-5 in a new run folder.
