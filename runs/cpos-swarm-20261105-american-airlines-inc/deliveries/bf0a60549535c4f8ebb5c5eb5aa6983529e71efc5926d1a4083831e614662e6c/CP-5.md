## Request

Evidence trace and research-integrity review for AMERICAN AIRLINES, INC. (issuer id american-airlines-inc), as of 2026-11-05, pathway credit_snapshot, reporting currency USD (US$ millions unless stated). Scope: the Top 5 credit drivers across the source readiness, financial base, business context and credit synthesis handoffs, each traced to a pinned source locator, with the audit lanes of the research-integrity grade. Source figures and locators were re-opened and recomputed independently of those handoffs.

## Sources

### Issuer sources

| Source file | sha256 |
| --- | --- |
| 10-K_2025-12-31_aal-20251231.htm.jsonl | 241cb406125cf4a40a3dec4d315c7a8e709f73f5f12957d46a28f056de7b338c |
| 10-Q_2026-03-31_aal-20260331.htm.jsonl | bd54f0ef7be7c4905b1acb2a15d1e60b5211836b6a174b954a6d8e979771d4f3 |
| 10-Q_2026-06-30_aal-20260630.htm.jsonl | e590d34e327bfac4cc2a446c7444656df89c4b6aac523f8df741e9c71b1ace9a |
| 10-Q_2026-09-30_aal-20260930.htm.jsonl | edb09356472b6a21c11979d0ace904761af85e302b5218542813aede49a0decc |
| EX-99.2_2026-04-23_earningspresentation.htm.jsonl | 9a2e0cf77a5348cca76e4e1fa089b91044513dded2916dcf498cbc76a4f142fe |
| EX-99.2_2026-07-23_earningspresentation.htm.jsonl | 60d450333d317c8f5bcb2c0834ff53272fd96fa253d4a67d36813c30742d7ee9 |
| EX-99.2_2026-10-22_earningspresentation.htm.jsonl | ce6723a4b2e59ac217d38de9b2fa855bbf5fa9fd11b713b0732222688fa7865b |

### Context

| Item | sha256 |
| --- | --- |
| context (user settings, not issuer evidence) | 4315193a9d24f5f5ddc6f4bf134c08d91788bf1e14ed0a34e81f98521fa4fc9b |

### Handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | d2c2217d545d90f74a5b8e3d65418442e5f1ebc0d6624ce35bbca3459b6fd9f3 |
| CP-1 | ee800a14f4d54fb51366d1b36ecf9d88e3f7b9083ef36890e8e5611bb9bb03cd |
| CP-1A | b195565a04b618b13acdab6a311719fd1afa87d28a98e633f9b3fce9861b01df |
| CP-2 | abdb55babaeb3923043cbc5f348157653f85751b31d77a64e0b15ebfeabe8e66 |

Consistency with upstream: this review audits the four handoffs above and does not change their conclusions. It restates their figures only to test them; where it finds a defect the defect is recorded as a finding, and the earlier handoffs are not edited.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The five main credit drivers trace to filed statements and recomputed figures, so the credit view is traceable. Two material issues and five minor ones remain, so committee use is restricted until fixed. | Low | No executed debt documents are supplied, and the earlier write-ups cannot be edited here. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Four of the five main drivers are directly sourced and one is calculated; every figure recomputed correctly. | Leverage, cover, liquidity and maturity figures can be relied on as stated. | High |
| The business context omits the readiness judgment for the next module that its method requires. | The synthesis cannot rely on a stated readiness for its own use. | Medium |
| The credit synthesis credits the prepayment of the 8.50% notes with easing near-term refinancing, but those notes mature in 2029. | The refinancing strength is overstated; the term loan extension is the real near-term relief. | Medium |
| Guarantee, collateral and covenant claims rest on filing summaries rather than executed documents. | Priority and covenant headroom stay untested. | Medium |

### Evidence trace view

Evidence traceability for American is Ready with Remediation. The strongest point is that every leverage, liquidity, maturity and parent-link figure used by the credit synthesis was reopened at its page in the 10-K or third-quarter 10-Q, matched exactly, and recomputed without difference. The weakest point is a small set of presentational and attribution defects: one handoff omits a required readiness judgment, one strength is mis-attributed to an event that did not ease near-term refinancing, and a few locators or quotes are imprecise. The decision turns on whether those are fixed and on whether executed debt documents are obtained, because guarantee, collateral and covenant claims currently rest on management summaries in the filings. None of the defects changes the credit conclusion, so committee use is restricted rather than blocked.

### Overall traceability view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 4 are directly sourced, 1 is calculated, 0 are assumption-based, 0 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of executed debt, guarantee and collateral documents, which matters because covenant headroom, guarantor structure and priority of claims can only be described from management summaries in the filings, and implies that legal conclusions stay restricted and the headroom measure stays Not calculable until the documents are supplied.

The defects that do exist are limited to citation precision and attribution (two Material, five Minor) and none alters a figure or the direction of the credit view.

### Remediation priority map

1. Must-fix before committee: CP5-001 (re-state the strength in the credit synthesis as the 2014 term loan extension and drop the 8.50% prepayment as a near-term refinancing relief).
2. Must-fix before the handoff is consumed downstream: CP5-002 (add the per-module readiness judgments to the business context handoff, or record that the synthesis proceeds without it).
3. Monitoring follow-up: CP5-003 (obtain the executed debt, guarantee and collateral documents and re-run the legal lane), CP5-004 (date the parent note guarantee amounts consistently).
4. Formatting / hygiene: CP5-005 (correct the page locator for the aircraft and engine commitments from page 66 to page 65), CP5-006 (quote the yield statement on page 44 in the operating model row), CP5-007 (replace evaluative words in the credit synthesis with the supporting figures).

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 5. Committee Use: Restricted.

No finding changes a figure or the direction of the credit view, but two Material issues (a mis-attributed refinancing strength and a missing readiness judgment) must be disclosed for committee use, and the covenant and guarantee claims remain limited by the absence of executed documents.

### Audit summary

Confidence score 24 of 100, band Insufficient Information, qa_status Restricted, committee_status Restricted. The score is script-owned: score = clamp((0.6*98 + 0.4*100) * 0.7 - 45, 0, 100) = 24.16, rounded to 24. The low band is driven by the penalty for seven open findings and the partial source gate (no executed documents), not by errors in the figures.

### Analytical appendix — complete canonical registers

#### T5.1 Input module register

Module Status: Ready with Limitations (all four handoffs available; executed documents absent; no extended YAML envelope in this transport).

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | run american-airlines-inc-2026-11-05-credit_snapshot-host; handoff sha256 d2c2217d545d90f74a5b8e3d65418442e5f1ebc0d6624ce35bbca3459b6fd9f3 | Source readiness, 7 issuer sources | High for filings; Medium for decks | Six required H2 headings present and the readiness view follows the reader summary | Accepted by the run checker; pre-audit | Consumer statuses are limited, not blocked |
| CP-1 | same run; sha256 ee800a14f4d54fb51366d1b36ecf9d88e3f7b9083ef36890e8e5611bb9bb03cd | Issuer financial base, FY2024, FY2025, nine months 2026, LTM Q3 2026 | High for filed statements; derived EBITDA is a calculation | Six H2 headings present; four chart selectors and financials selector present | Accepted by the run checker; pre-audit | One locator error recorded as CP5-005 |
| CP-1A | same run; sha256 b195565a04b618b13acdab6a311719fd1afa87d28a98e633f9b3fce9861b01df | Business, ownership, governance, transaction context | High for filings; Low for deck claims (tagged Management Language) | Six H2 headings and three selectors present; consumer readiness section absent | Accepted by the run checker; pre-audit | See CP5-002 |
| CP-2 | same run; sha256 abdb55babaeb3923043cbc5f348157653f85751b31d77a64e0b15ebfeabe8e66 | Credit synthesis from upstream registers only | Derived from the handoffs above | Six H2 headings and two selectors present | Accepted by the run checker; pre-audit | See CP5-001 and CP5-007 |

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-10K | 10-K_2025-12-31_aal-20251231.htm.jsonl | High: audited filing | FY2025 with FY2024 and FY2023 comparatives | American Airlines, Inc. (Item 8B) and American Airlines Group Inc. (Item 8A) | Issuer statements, debt note, guarantees, liquidity, covenants, related parties, business description | Combined filing; tables flattened in text | Financial base, business context |
| SRC-Q1 | 10-Q_2026-03-31_aal-20260331.htm.jsonl | High: unaudited filing | Q1 2026 | Both registrants | Q1 liquidity table, issuer statements | Unaudited | Liquidity trend |
| SRC-Q2 | 10-Q_2026-06-30_aal-20260630.htm.jsonl | High: unaudited filing | Q2 2026 and six months | Both registrants | Q2 liquidity table, issuer statements | Unaudited | Liquidity trend |
| SRC-Q3 | 10-Q_2026-09-30_aal-20260930.htm.jsonl | High: unaudited filing | Q3 2026 and nine months | Both registrants | Issuer statements, debt note, liquidity, covenants, contractual obligations, financing activity | Unaudited; no interim letters of credit figure | All modules |
| SRC-D1 | EX-99.2_2026-04-23_earningspresentation.htm.jsonl | Medium: management presentation | Q1 2026 | American Airlines Group Inc. only | Parent net debt reconciliation | Parent perimeter; charts not inspected | Context only |
| SRC-D2 | EX-99.2_2026-07-23_earningspresentation.htm.jsonl | Medium: management presentation | Q2 2026 | American Airlines Group Inc. only | Results commentary and outlook | Parent perimeter; no debt table | Context only |
| SRC-D3 | EX-99.2_2026-10-22_earningspresentation.htm.jsonl | Medium: management presentation | Q3 2026 | American Airlines Group Inc. only | Net debt reconciliation, target, outlook | Parent perimeter; charts not inspected | Context only |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Earnings compression from unhedged fuel | CP-1, CP-2 | Nine-month 2026 revenue 46,979, fuel 12,444, operating income 535 against 1,042 | Fuel is the largest swing item and unhedged, so EBITDA falls with price; EBITDA drives every ratio | Debt service capacity and leverage tolerance | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:25; page:44 | Parent-level hedging statement; issuer income statement is the numeric basis |
| 2 | Leverage and interest cover | CP-1, CP-2 | LTM EBITDA 2,916; net debt 17,623; total debt 25,876; net 6.04x, gross 8.87x, cover 2.06x | High leverage and thin cover raise default sensitivity to earnings and rates | PD, leverage tolerance | 10-Q_2026-09-30_aal-20260930.htm.jsonl pages 25, 26, 27; 10-K_2025-12-31_aal-20251231.htm.jsonl pages 201, 254 | EBITDA derived, not reported; excludes leases and pensions |
| 3 | Liquidity and 2028 maturity concentration | CP-1, CP-2 | Liquidity 11,763; principal due 2028 7,861 of 25,575 | Liquidity buffers refinancing, but 2028 needs market access | Refinancing and liquidity | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:60; page:65 | Letters of credit under facilities at 2026-09-30 not printed |
| 4 | Parent linkage | CP-1, CP-1A, CP-2 | Parent guarantees about 14.1 billion of American debt; American guarantees AAG's PSP notes; net related-party receivable 10,430 | Issuer and parent credit are tied; intercompany cash is not liquidity | Structural support and exposure | 10-K_2025-12-31_aal-20251231.htm.jsonl page:173; page:230; 10-Q_2026-09-30_aal-20260930.htm.jsonl page:26; page:40 | Guarantee amounts dated 2025-12-31; no executed documents |
| 5 | Fleet and purchase commitments | CP-1, CP-2 | Aircraft and engine purchase commitments 24,056; capex 2,660 for nine months | Standing financing need against EBITDA 2,916 | Refinancing and cash conversion | 10-Q_2026-09-30_aal-20260930.htm.jsonl page:65; page:27 | Delivery schedule is a management estimate; CP-1 cites page 66 in error |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Earnings compression from unhedged fuel | CP-1 | "Operating income 114 167 535 1,042" and "Aircraft fuel and related taxes 4,635 2,767 12,444 8,017" (Q3 10-Q page:25) | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Leverage and interest cover | CP-1 | Debt lines on page:26, interest paid on page:27 and the 10-K income statement; ratios recomputed here | Yes | High for inputs | Calculated | Supported | Medium | Committee-Ready |
| Liquidity and 2028 maturity concentration | CP-1 | "Total available liquidity $ 11,797 $ 9,233 $ 11,763 $ 9,213" (page:60) and principal row (page:65) | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Parent linkage | CP-1A | "AAG had issued guarantees covering approximately $14.1 billion of American’s debt" (10-K page:173); related-party receivable (Q3 page:26, page:40) | Yes | High | Directly Sourced | Supported | Medium | Remediation Needed |
| Fleet and purchase commitments | CP-1 | "Aircraft and engine purchase commitments (d) 625 3,135 3,606 5,641 3,982 7,067 24,056" (Q3 10-Q page:65) | Partial | High | Directly Sourced | Supported | Medium | Remediation Needed |

The parent linkage row is marked Remediation Needed because the guarantee amounts are dated differently across handoffs (CP5-004); the fleet row because of the locator error (CP5-005).

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nine-month 2026 operating revenues 46,979 | CP-1 financials table | 10-Q_2026-09-30_aal-20260930.htm.jsonl | SRC-Q3 | page:25 | Financials and credit metrics | Sourced | High | Matches |
| Nine-month 2026 fuel expense 12,444 | CP-1 financials table | 10-Q_2026-09-30_aal-20260930.htm.jsonl | SRC-Q3 | page:25 | Financials and credit metrics | Sourced | High | Matches |
| Nine-month 2026 operating income 535 | CP-1 financials table | 10-Q_2026-09-30_aal-20260930.htm.jsonl | SRC-Q3 | page:25 | Financials and credit metrics | Sourced | High | Matches |
| FY2025 operating income 1,511 and D&A 1,884 | CP-1 financials table | 10-K_2025-12-31_aal-20251231.htm.jsonl | SRC-10K | page:201 | Financials and credit metrics | Sourced | High | Matches |
| Debt and finance leases 3,689 current and 22,187 noncurrent | CP-1 financials table | 10-Q_2026-09-30_aal-20260930.htm.jsonl | SRC-Q3 | page:26 | Financials and credit metrics | Sourced | High | Matches |
| Debt principal 25,575 | CP-1 debt structure | 10-Q_2026-09-30_aal-20260930.htm.jsonl | SRC-Q3 | page:31 | Debt structure | Sourced | High | Matches |
| Total available liquidity 11,763 | CP-1 liquidity | 10-Q_2026-09-30_aal-20260930.htm.jsonl | SRC-Q3 | page:60 | Liquidity and covenants | Sourced | High | American column; matches |
| Principal due 2028 of 7,861 | CP-1 maturities | 10-Q_2026-09-30_aal-20260930.htm.jsonl | SRC-Q3 | page:65 | Debt structure | Sourced | High | Matches |
| Interest paid, net FY2025 1,551 and nine months 1,044 | CP-1 coverage | 10-K_2025-12-31_aal-20251231.htm.jsonl | SRC-10K | page:254 and Q3 page:27 | Leverage and coverage | Sourced | High | Matches |
| LTM EBITDA 2,916 | CP-1 calculations | Derived from SRC-Q3 and SRC-10K | SRC-Q3, SRC-10K | pages 25 and 201 | Calculations | Calculated | High for inputs | Recomputed; matches |
| Aircraft and engine commitments 24,056 | CP-1 claims table | 10-Q_2026-09-30_aal-20260930.htm.jsonl | SRC-Q3 | cited page:66, actual page:65 | Claims outside the debt figure | Sourced | High | Locator error (CP5-005) |
| Parent guarantees about 14.1 billion of American debt | CP-1A governance table | 10-K_2025-12-31_aal-20251231.htm.jsonl | SRC-10K | page:173 | Ownership, governance and behaviour | Sourced | High | AAG notes page; dated 2025-12-31 |
| American guarantees AAG PSP notes | CP-1A governance table | 10-K_2025-12-31_aal-20251231.htm.jsonl | SRC-10K | page:230 | Ownership, governance and behaviour | Sourced | High | Dated 2025-12-31; amounts 1.8 billion, 1.0 billion, 959 |
| Net related-party receivable 10,430 | CP-1 and CP-1A | 10-Q_2026-09-30_aal-20260930.htm.jsonl | SRC-Q3 | page:26; page:40 | Claims outside the debt figure | Sourced | High | Matches |
| No fuel hedges at 2026-09-30 | CP-1A operating model | 10-Q_2026-09-30_aal-20260930.htm.jsonl | SRC-Q3 | page:44 | Company and operating model | Sourced | High | Parent-level statement |
| Reduced near-term refinancing from prepaying the 8.50% notes | CP-2 strengths | 10-K_2025-12-31_aal-20251231.htm.jsonl | SRC-10K | page:218 (notes due May 2029) | Strengths and weaknesses | Weak Lineage | High source, claim unsupported | CP5-001 |
| Premium products roughly half of ticket revenue | CP-1A operating model | EX-99.2_2026-10-22_earningspresentation.htm.jsonl | SRC-D3 | page:5 | Company and operating model | Inference | Medium | Tagged Management Language |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM operating income | CP-1 | 1,511 + 535 - 1,042 | FY2025 + 9M 2026 - 9M 2025 = 1,004 | Calculated; recomputed here, matches | Supported | High | Debt service | Pages 201 and 25 |
| LTM EBITDA | CP-1, CP-2 | Operating income 1,004 + D&A 1,912 | Operating income + income statement D&A = 2,916 | Calculated; matches | Supported | Medium: derived definition | Leverage, cover | Pages 201 and 25 |
| LTM D&A | CP-1 | 1,884 + 1,442 - 1,414 | = 1,912 | Calculated; matches | Supported | High | Leverage | Pages 201 and 25 |
| Total debt including finance leases at 2026-09-30 | CP-1 | 3,689 + 22,187 | = 25,876 | Calculated; matches | Supported | High | Leverage | Page 26 |
| Net debt at 2026-09-30 | CP-1 | 25,876 - (1,094 + 7,159) | = 17,623 | Calculated; matches | Supported | High | Leverage | Page 26 |
| Net debt over LTM EBITDA | CP-1, CP-2 | 17,623 / 2,916 | = 6.04x | Calculated; matches | Supported | Medium | Leverage | Derived |
| Total debt over LTM EBITDA | CP-1, CP-2 | 25,876 / 2,916 | = 8.87x | Calculated; matches | Supported | Medium | Leverage | Derived |
| LTM interest paid, net | CP-1 | 1,551 + 1,044 - 1,179 | = 1,416 | Calculated; matches | Supported | High | Cover | Pages 254 and 27 |
| EBITDA over cash interest | CP-1, CP-2 | 2,916 / 1,416 | = 2.06x | Calculated; matches | Supported | Medium | Cover | Derived |
| Liquidity sum | CP-1 | 1,094 + 7,159 + 3,510 | = 11,763 | Calculated; matches the printed total | Supported | High | Liquidity | Page 60 |
| Conservative covenant proxy | CP-1 | 1,094 + 363 + 1,296 + 1,451 | = 4,204; less 2,000 = 2,204 | Calculated; matches; covenant definition not supplied so headroom is Not Calculable exactly | Supported | Low | Covenant | Pages 26 and 31, 61 |
| 2028 share of principal | CP-1 | 7,861 / 25,575 | = 30.7 percent | Calculated; matches | Supported | High | Refinancing | Page 65 |
| Operating cash flow less capex, LTM | CP-1, CP-2 | 4,141 - 4,273 | = -132 | Calculated; matches | Supported | High | Cash conversion | Pages 202, 26, 27 |
| Net debt reduction | CP-2 | 19,443 - 17,623 | = 1,820 | Calculated; matches | Supported | High | Leverage | Derived |
| Assumption: 2025 nine-month comparatives are not restated | CP-1 | Comparatives taken from the Q3 2026 10-Q | Stated assumption | Assumption-Based | Supported by absence of restatement language | Medium | LTM construction | Q3 10-Q page:25 |

Definition drift check: EBITDA is defined as operating income plus income statement D&A in every module that uses it; the cash flow statement D&A (2,177 for FY2025) is disclosed in CP-1 and not used. No drift between modules.

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2: prepayment of the 8.50% notes reduced near-term refinancing pressure | The notes mature in May 2029 (10-K page:218); their prepayment did not ease near-term maturities, which are eased by the 2014 term loan extension | Weak Lineage | A refinancing strength is overstated in a committee-facing section | Re-state with the term loan extension only | CP-2 Strengths and weaknesses |
| MATERIAL | CP-1A omits per-module readiness judgments | Method requires each consumer module to be judged once | Insufficient Information | Downstream synthesis relies on an unstated readiness | Add consumer readiness section or record the omission | CP-1A handoff |
| MINOR | CP-1 aircraft and engine commitments cited to page 66 | Figure sits on page 65 | Directly Sourced with citation gap | Reader opening page 66 will not find the row | Correct locator | CP-1 claims table and prose |
| MINOR | CP-1A yield and unit revenue statement quotes the fuel price sentence | Supporting yield figures are on the same page but not quoted | Directly Sourced with citation gap | Quote does not match claim | Quote the yield sentence | CP-1A operating model |
| MINOR | Parent note guarantee stated as 3,746 | Guarantee text is dated 2025-12-31 while 3,746 is the 2026-09-30 principal | Calculated mixing dates | Small date mismatch on a contingent claim | Date the figure in each use | CP-1A, CP-2 |
| MINOR | Guarantee, collateral and covenant claims | Rest on filing summaries; no executed documents | Weak Lineage for clause-level claims | Legal meaning not tested | Obtain documents | CP-1, CP-1A, CP-2 |
| MINOR | Evaluative words in the credit synthesis | "Solid", "comfortably" and "large" used where figures are given | Analyst Inference | Style standard prefers figures to adjectives | Replace with figures | CP-2 |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven pinned issuer sources, issuer-level statements located in every filing; executed documents absent | Gaps in legal sources limit clause-level claims | Priority and headroom cannot be tested | Obtain executed documents |
| Citation completeness | Ready with Remediation | Every figure carries a file and page locator; one wrong page (CP5-005) and one imprecise quote (CP5-006) | Wrong locator wastes reviewer effort and weakens audit | Low effect on the credit view | Correct locator and quote |
| Calculation traceability | Committee-Ready | Fourteen calculations recomputed with formula, inputs, period and unit; all match | Derived EBITDA could drift from a covenant definition | Covenant headroom stays Not Calculable | State definition with each ratio |
| Assumption transparency | Committee-Ready | Single assumption (no restatement of nine-month 2025) stated; liquidity availability taken as printed with date gap disclosed | Hidden assumptions would mislead | Minimal | None |
| Markdown/export artifact integrity | Ready with Remediation | All handoffs carry the six H2 headings and mandated selectors; CP-1A lacks the consumer section | Missing method section hides a readiness view | Limits the synthesis basis | Add the section |

Overall auditability: Ready with Remediation (lowest of the five dimensions).

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed credit agreements, indentures and EETC documents | Clause-level support for guarantees, collateral, covenant tests | Priority of claims and headroom depend on definitions | Legal and covenant statements in CP-1, CP-1A, CP-2 | High impact | Executed documents |
| CP-5-GAP-002 | Letters of credit drawn on revolvers at 2026-09-30 | Interim letter of credit figure | Availability of 3,510 may be overstated | Liquidity figure | Low impact | Company disclosure |
| CP-5-GAP-003 | Covenant measured values and the qualifying cash definition | Compliance certificates | Headroom exact measure | Covenant lane | Medium impact | Facility documents |
| CP-5-GAP-004 | Ratings and market data | Rating reports, quotes | No market-implied cross-check | Relative value lane (none claimed) | Low impact | Rating agencies, market data |
| CP-5-GAP-005 | Events after the third-quarter report to the cutoff | Later filings | Recent developments untested | All modules | Low impact | Filings after 2026-10-22 |
| CP-5-GAP-006 | Chart and image content of the three decks | Visual inspection | Chart-only data points unverified | Context only | Low impact | Deck images |
| CP-5-GAP-007 | Per-module readiness judgments in the business context | The omitted section | Readiness basis for the synthesis | CP-2 | Medium impact | Updated business context |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-2 | Strengths: "the 8.50 percent notes of USD 1.0 billion were prepaid, which reduced near-term refinancing pressure" | Unsupported | The 8.50 percent notes mature in May 2029 (10-K page:218), so their prepayment did not ease near-term maturities; only the 2014 term loan extension did (Q3 10-Q page:32). | Re-state the strength using the term loan extension | Restricts Committee Use |
| MINOR | CP-1 | Claims table and prose: aircraft and engine purchase commitments of 24,056 cited at page:66 | Partially Supported | The row is on page:65; page:66 holds other rows. CP-1A already notes the correction. | Correct the locator | Formatting / Hygiene Only |
| MINOR | CP-1A | Operating model row: yield and unit revenue rose, quoted with the fuel price sentence | Partially Supported | The quote supports the fuel price rise; yield and unit revenue are stated elsewhere on the same page (Q3 10-Q page:44) | Quote the yield sentence | Formatting / Hygiene Only |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | CP-1, CP-2 | Fourteen derived figures recomputed (LTM construction, EBITDA, debt, net debt, leverage ratios, cash interest cover, liquidity, shares, cash flow less capex, net debt change); all match to the stated precision | EBITDA defined consistently as operating income plus income statement D&A; not a covenant definition and disclosed as such; interest paid may net capitalised interest and is disclosed | None between modules; cash flow D&A of 2,177 disclosed against income statement 1,884 | None required | Monitoring Follow-Up |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Parent guarantees of American debt, American guarantee of parent notes, security over aircraft and loyalty assets, covenant tests, and absence of creditor-adverse actions | Executed credit agreements, indentures, guarantees and amendments | Only management summaries in the 10-K and Q3 10-Q; the absence of priming or uptier language rests on a text search of the filings, not on documents | Obtain documents; keep claims labelled as summary-based | Legal review required before relying on priority, release mechanics or headroom |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | CP-1, CP-1A, CP-2 | No market, spread, price, rating or relative-value claim appears in the four handoffs, and the synthesis states that ratings and quotes are not supplied | Prices, spreads and ratings are absent by design and recorded as gaps | None created by the handoffs | None required | No effect on committee use |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A, CP-2 | American's guarantee of parent notes is shown as 3,746 although the guarantee text is dated 2025-12-31 (about 1.8 billion, 1.0 billion and 959) and 3,746 is the 2026-09-30 principal | Date basis differs between guarantee text and principal table; CP-1 labels both dates, later modules do not | Date each use | Small; contingent claim sizing is approximate |
| None | CP-0, CP-1, CP-1A | Issuer country: context says Cayman Islands, filing says Delaware | Logged in CP-1 and CP-1A as an unresolved conflict; not reconciled | None; keep logged | Report should not state a Cayman domicile |
| None | CP-0, CP-1, CP-1A, CP-2 | Issuer name, parent, perimeter, period, EBITDA definition, net debt, liquidity, maturities | Consistent across all four handoffs | None | None |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Promotional or Non-Credit Language | Evaluative words (solid, comfortably, large) accompany liquidity figures that already support the point | Replace with the figures | Minor; does not impair interpretation |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A | Consumer readiness judgments | The method requires each consumer module to be judged once for readiness, what to take, why, the gap and the action; the handoff has none | Add the section or record the omission | The synthesis lists a missing readiness signal and holds confidence below High |

All four handoffs carry the six required headings and the mandated sub-headings after their reader summaries. No orphan claim of Critical weight was found; the one weak-lineage claim (CP5-001) is a supporting strength, not a decision driver.

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-2 | Unsupported Claim | Prepayment of the 8.50 percent notes described as easing near-term refinancing; notes mature in May 2029 | Re-state with the 2014 term loan extension only | Restricts Committee Use | Open |
| CP5-002 | MATERIAL | CP-1A | canonical Markdown Handoff Integrity Defect | Consumer readiness judgments absent | Add the section or record the omission | Blocks canonical Markdown Handoff / Downstream Grounding | Open |
| CP5-003 | MINOR | CP-1, CP-1A, CP-2 | Legal Support Gap | Guarantee, collateral and covenant claims rest on filing summaries | Obtain executed documents | Requires Legal Review | Open |
| CP5-004 | MINOR | CP-1A, CP-2 | Version Conflict | Parent note guarantee amount mixes 2025-12-31 and 2026-09-30 dates | Date each use | Monitoring Follow-Up | Open |
| CP5-005 | MINOR | CP-1 | Citation Gap | Commitments cited to page 66; figure on page 65 | Correct locator | Formatting / Hygiene Only | Open |
| CP5-006 | MINOR | CP-1A | Partially Supported Claim | Yield statement quoted with fuel sentence | Quote the yield sentence | Formatting / Hygiene Only | Open |
| CP5-007 | MINOR | CP-2 | Promotional or Non-Credit Language | Evaluative words beside supporting figures | Replace with figures | Formatting / Hygiene Only | Open |

## Calculations

Recomputed from the pinned sources, independent of the handoffs (US$ millions): LTM revenue 54,626 + 46,979 - 40,628 = 60,977; LTM operating income 1,511 + 535 - 1,042 = 1,004; LTM D&A 1,884 + 1,442 - 1,414 = 1,912; LTM EBITDA 1,004 + 1,912 = 2,916; debt 3,689 + 22,187 = 25,876; cash and short-term investments 1,094 + 7,159 = 8,253; net debt 25,876 - 8,253 = 17,623; net debt over EBITDA 17,623 / 2,916 = 6.04x; total debt over EBITDA 25,876 / 2,916 = 8.87x; LTM interest paid 1,551 + 1,044 - 1,179 = 1,416; cover 2,916 / 1,416 = 2.06x; liquidity 1,094 + 7,159 + 3,510 = 11,763; maturities 631 + 3,550 + 7,861 + 3,884 + 972 + 8,677 = 25,575. All match the handoffs.

Confidence score (script-owned, from the lineage counts and findings above): E = 98 from 4 Directly Sourced and 1 Calculated material drivers ((4 x 1.0 + 1 x 0.9) / 5 x 100); C = 100 (6 of 6 required headings present); S = 0.7 (source gate partial: executed documents absent); P = 45 (2 Material at 15 and 5 Minor at 3). Score = clamp((0.6 x 98 + 0.4 x 100) x 0.7 - 45, 0, 100) = 24.16, rounded to 24; band Insufficient Information; qa_status Restricted (Material findings, no Critical).

## Gaps

| Gap | Effect | Action |
| --- | --- | --- |
| Executed debt, guarantee and collateral documents Not supplied | Legal and covenant claims remain summary-based; headroom Not calculable exactly | Obtain documents and re-run the legal lane |
| Earlier handoffs cannot be edited in this run | Defects CP5-001 to CP5-007 persist in them and are recorded here only | Re-run the affected modules in a new run folder if committee use requires clean text |
| Chart and image content of the decks was not inspected | Chart-only data points unverified | Use filings for the same data |
| Letters of credit at 2026-09-30, ratings, market data and post-quarter events Not supplied | Liquidity availability and recent developments untested | Obtain disclosures |

## Next module

No further module is selected in this minimum set. For delivery, the report should carry the Restricted committee status, the two Material findings, and the gaps above; the credit conclusion of the synthesis stands, subject to re-statement of the refinancing strength (CP5-001).
