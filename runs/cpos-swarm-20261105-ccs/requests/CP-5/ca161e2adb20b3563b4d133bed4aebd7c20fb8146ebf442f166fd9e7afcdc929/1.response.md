## Request

Evidence trace and research-integrity review of the upstream handoffs for Century Communities, Inc. (ticker CCS, issuer id ccs), as of 2026-11-05, pathway credit_snapshot. Scope: the Top 5 material credit drivers carried by the source-readiness [CP-0], financial base [CP-1], business context [CP-1A] and credit synthesis [CP-2] handoffs, traced to the pinned filings and releases (USD, Q3 2026 and FY2025).

## Sources

### Issuer sources traced to

| Source (exact name) | Short name | Pinned sha256 |
| --- | --- | --- |
| 10-K_2025-12-31_ccs-20251231x10k.htm.jsonl | 10-K | 40822bca77f3d1f280fa9bdb025667cff0a3cbada92f0367c2ce2aea0f14cd10 |
| 10-Q_2026-03-31_ccs-20260331x10q.htm.jsonl | Q1 10-Q | 6dbfc2b9b1702aabe0ae62a15ab79d805237cf407bb87b6f748285ee6819232c |
| 10-Q_2026-06-30_ccs-20260630x10q.htm.jsonl | Q2 10-Q | 7826d33d347b5ba4a0f0ded6692f553b2cb2eab216f48c0b48fab887a5e242a0 |
| 10-Q_2026-09-30_ccs-20260930x10q.htm.jsonl | Q3 10-Q | 5bb6ede8961747c92feb57cbf28091469edbccbe289914d1a5a3c7cff3b959d0 |
| EX-99.1_2026-04-22_ccs-20260422xex99_1.htm.jsonl | Q1 release | ef23de5e89dc27836c0aa67c681d5f651593a95499849c764478ef4002ab9849 |
| EX-99.1_2026-07-22_ccs-20260722xex99_1.htm.jsonl | Q2 release | 8fa7d8813bf620e387c89f24634e9692af83d752a4591b259b033efbe214d3eb |
| EX-99.1_2026-10-28_ccs-20261028xex99_1.htm.jsonl | Q3 release | 1a2c31ec21a3900623ca510eba56234f123a5a1fb09a2e417f1dc9e6e8c01b85 |

Run settings, not issuer evidence: context, sha256 3f4bc378facbce0f1396d451dfff0e16ea0431cd8d227bb7281acea631c866f1.

### Handoffs audited

| Module | Pinned sha256 |
| --- | --- |
| CP-0 | c251b67407b3993cf09de40f1b6adea510b7bad7bb25a2815575a608bae15041 |
| CP-1 | deba02fbf78513edd8848cc803441953597a0770ce39b23fafaf06d522a04d21 |
| CP-1A | 0d321ce4e4e6edfb589c2f39b96943e74f895ae8f426b8382a22e2742976563a |
| CP-2 | 1f879b0709105a1cea7a109ef0c2cb58520640763ae795bd5c2511c17a994cc8 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The conclusions are well traced: all five top drivers rest on filed figures or reproduced calculations, and no critical defect was found. Committee use is restricted by one material and eleven minor issues. | Medium | Covenant and legal statements rest on 10-Q summaries because the executed credit agreement, amendment and indentures are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Leverage of 6.16x, negative operating cash flow, liquidity, margin pressure and the HistoryMaker Homes acquisition each trace to filed pages or reproduced calculations. | The core credit conclusions rest on checked evidence. | High |
| Covenant limits and the revised financial covenants are described only in 10-Q summaries, with no executed agreement in the sources. | Covenant headroom and legal capacity cannot be verified. | High |
| One backlog comparison, two segment descriptions and a year-end revolver commitment were stated more firmly than the sources support. | Minor wording corrections; no conclusion changes. | High |
| Net debt is used in three senses: total debt less cash, the company's homebuilding measure, and company-defined liquidity. | Ratios are not interchangeable and must be labelled. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 3 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the executed Credit Agreement, its September 30, 2026 First Amendment and the indentures, which matters because the covenant, liquidity-availability and legal-capacity statements in the upstream work rest on the company's own 10-Q summaries, and implies that committee use must be restricted until the documents are reviewed. Every figure that the upstream handoffs print was found on the page it cites or reproduced from cited inputs; the defects are one material legal-source dependency and eleven minor issues of wording, definition and presentation, none of which changes a credit conclusion.

### Traceability summary

| Credit driver | Originating module | Classification | Traceability status |
| --- | --- | --- | --- |
| Leverage of 6.16x adjusted EBITDA | CP-1 | Calculated | Committee-Ready |
| Negative operating cash flow funded by the revolver | CP-1 | Directly Sourced | Committee-Ready |
| Liquidity and maturity runway | CP-1 | Calculated | Remediation Needed |
| Margin and demand pressure | CP-1A | Directly Sourced | Committee-Ready |
| HistoryMaker Homes acquisition | CP-1A | Directly Sourced | Committee-Ready |

### Remediation priorities

- Must-fix before committee: CP5-001 (obtain and review the executed Credit Agreement, First Amendment and indentures).
- Must-fix before the handoff is consumed downstream: CP5-011 and CP5-012 (envelope note and chart bucket labelling).
- Monitoring follow-up: CP5-002, CP5-003, CP5-004, CP5-005, CP5-006, CP5-007, CP5-008, CP5-009 and CP5-010.
- Formatting and hygiene: none beyond the items above.

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 1. Minor Issues: 11. Committee Use: Restricted.

The one material issue, the missing executed debt documents, means the covenant and liquidity-availability statements may be disclosed to the committee only as company summaries. The minor issues are wording and definition fixes that leave every conclusion unchanged, and no Critical issue blocks use.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_ccs-20251231x10k.htm.jsonl | Audited annual report | FY2025 (with FY2024 and FY2023) | Century Communities, Inc. consolidated | Statements, debt note, EBITDA reconciliation, business description, exhibit list | Executed debt agreements incorporated by reference, not supplied | CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2026-03-31_ccs-20260331x10q.htm.jsonl | Unaudited quarterly report | Q1 2026 | Century Communities, Inc. consolidated | Balance sheet, debt table, liquidity | Unaudited; 2025 comparatives recast | CP-1 |
| S3 | 10-Q_2026-06-30_ccs-20260630x10q.htm.jsonl | Unaudited quarterly report | Q2 2026 and six months | Century Communities, Inc. consolidated | Balance sheet, debt table, liquidity | Unaudited; 2025 comparatives recast | CP-1 |
| S4 | 10-Q_2026-09-30_ccs-20260930x10q.htm.jsonl | Unaudited quarterly report | Q3 2026 and nine months | Century Communities, Inc. consolidated | Statements, notes, debt, non-GAAP tables, subsequent event | Unaudited; covenant levels absent | CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-04-22_ccs-20260422xex99_1.htm.jsonl | Management earnings release | Q1 2026 | Century Communities, Inc. consolidated | Liquidity and results headline | Management document; cash definition differs from the filing | CP-1 |
| S6 | EX-99.1_2026-07-22_ccs-20260722xex99_1.htm.jsonl | Management earnings release | Q2 2026 | Century Communities, Inc. consolidated | Liquidity and results headline | Management document | CP-1 |
| S7 | EX-99.1_2026-10-28_ccs-20261028xex99_1.htm.jsonl | Management earnings release | Q3 2026 | Century Communities, Inc. consolidated | Liquidity, outlook, HistoryMaker claims | Management document; outlook is forward-looking | CP-1A, CP-2 |

Module Status: Ready with Limitations. Traceability Scope: Top 5. All four upstream handoffs and the seven sources were available; entity key issuer id ccs is available; the executed debt agreements are missing.

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Total debt 6.16x last-twelve-month adjusted EBITDA (net 5.87x) | CP-1 | Debt 1,812.587 and adjusted EBITDA components from filed tables | Leverage drives default risk and covenant pressure | Sets the fundamental credit view | S4 page:14, page:65; S1 page:91 | Company-defined EBITDA; covenant definition not supplied |
| 2 | Operating cash flow of negative 267.475 in nine months 2026 with revolver drawn to 456.0 | CP-1 | Cash flow statement and debt table | Cash burn funded by floating-rate bank debt raises liquidity and interest risk | Determines how long growth and returns can continue | S4 page:3, page:14 | Seasonal pattern limits annualisation |
| 3 | Liquidity of 744.0 undrawn revolver plus 86.086 cash, with first bond maturity in August 2029 | CP-1 | Commitment and drawn balance; maturity table | Protects refinancing and near-term liquidity | Supports the liquid but weakened view | S4 page:16, page:17, page:2, page:14, page:52 | Letters of credit of 42.3 unallocated; covenant tests absent |
| 4 | Margin and demand pressure from incentives | CP-1A | Q3 2026 price, volume, margin tables | Reduces EBITDA and cash conversion | Drives forward leverage | S4 page:37, page:35, page:46 | Causes are management's explanation |
| 5 | HistoryMaker Homes acquisition for about 160.2 closed 2026-10-07 | CP-1A | Subsequent-event note | Cash call outside the reported balance sheet | Post-quarter leverage unknown | S4 page:7, page:34; S7 page:1, page:2 | Funding and purchase accounting not stated |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 6.16x total and 5.87x net | CP-1 | Debt 1,812.587; cash 86.086; LTM adjusted EBITDA 294.366 derived from 349.705 + 197.013 − 252.352 | Yes | Filed statements (unaudited for 2026) | Calculated | Supported | Medium | Committee-Ready |
| Negative operating cash flow and revolver funding | CP-1 | Net cash used 267.475; revolver 456.0 against 51.5 | Yes | Filed statements | Directly Sourced | Supported | High | Committee-Ready |
| Liquidity and maturity runway | CP-1 | Commitments 1,200.0 less drawn 456.0 equals 744.0; company liquidity 863.8; notes due 2029 and 2033 | Yes | Filed statements and notes | Calculated | Supported with limitation | Medium | Remediation Needed |
| Margin and demand pressure | CP-1A | ASP 345.0 against 384.2 thousand; gross margin 15.0% against 17.9% | Yes | Filed MD&A tables; causes are management language | Directly Sourced | Supported | High | Committee-Ready |
| HistoryMaker Homes acquisition | CP-1A | Initial cash consideration about 160.2; 29 communities | Yes | Filed subsequent-event note | Directly Sourced | Supported | High | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 1,812.587 at 2026-09-30 | packs/1576940-century-communities-inc-ccs | 10-Q_2026-09-30 | S4 | page:14 (Note 9) | CP-1 Financials | Sourced | Filed, unaudited | Carrying value |
| Cash and cash equivalents 86.086 | same | 10-Q_2026-09-30 | S4 | page:2 | CP-1 Liquidity | Sourced | Filed, unaudited | Excludes escrow 33.740 |
| LTM adjusted EBITDA 294.366 | same | 10-K; 10-Q_2026-09-30 | S1; S4 | page:91; page:65 | CP-1 Leverage | Calculated | Filed non-GAAP | Recast basis consistent |
| Total debt / adjusted EBITDA 6.16x | same | derived | S1; S4 | pages above | CP-1 Leverage | Calculated | Derived | Reperformed |
| Net cash used in operating activities 267.475 | same | 10-Q_2026-09-30 | S4 | page:3 | CP-1; CP-2 | Sourced | Filed, unaudited | Nine months |
| Revolver 456.0 against 51.5 | same | 10-Q_2026-09-30 | S4 | page:14, page:17 | CP-1; CP-2 | Sourced | Filed, unaudited | |
| Undrawn revolver 744.0 | same | 10-Q_2026-09-30 | S4 | page:16, page:17 | CP-1 Liquidity | Calculated | Derived | Letters of credit not deducted |
| Company-reported liquidity 863.8 | same | 10-Q; release | S4; S7 | page:52; page:2 | CP-1 | Sourced | Filed and management | Ties to cash plus escrow plus 744.0 |
| First Amendment: 1.0 billion to 1.2 billion, maturities, revised covenants | same | 10-Q_2026-09-30 | S4 | page:16 | CP-1; CP-1A | Sourced | Filed summary of executed document | Executed document not supplied |
| Notes: 500.0 due August 2029; 500.0 due September 2033 | same | 10-Q_2026-09-30 | S4 | page:14, page:15 | CP-1 | Sourced | Filed | |
| Cash interest paid 78.9 (2024) and 81.3 (2025) | same | 10-K | S1 | page:130, page:43 | CP-1 | Sourced | Audited note, rounded | "Approximately" |
| Q3 ASP 345.0 against 384.2; margin 15.0% against 17.9% | same | 10-Q_2026-09-30 | S4 | page:37 | CP-1A; CP-2 | Sourced | Filed MD&A | |
| Incentives and slower absorption as causes | same | 10-Q_2026-09-30 | S4 | page:35 | CP-1A; CP-2 | Sourced | Management explanation | Management Language |
| HistoryMaker Homes about 160.2, 29 communities | same | 10-Q_2026-09-30 | S4 | page:7, page:34 | CP-1A; CP-2 | Sourced | Filed note | Subsequent event |
| Dallas communities 12 to 41; deliveries 211 to 669 | same | EX-99.1_2026-10-28 | S7 | page:1 | CP-1A | Sourced | Management release | Management Language |
| Insiders own 13.9% | same | 10-K | S1 | page:48 | CP-1A; CP-2 | Sourced | Filed | At 2025-12-31 |
| Repurchases financed through cash and the revolver | same | 10-Q_2026-09-30 | S4 | page:62 | CP-1A; CP-2 | Sourced | Filed | General policy statement |
| Compliance with all covenants | same | 10-Q_2026-09-30 | S4 | page:56 | CP-1 | Sourced | Filed statement | Levels not printed |
| Credit Agreement limits on liens, debt, dividends and others | same | 10-Q_2026-09-30 | S4 | page:17 | CP-1; CP-1A | Weak Lineage | Summary of unseen contract | Executed agreement not supplied |
| Century Complete state lists differ | same | 10-K; 10-Q_2026-09-30 | S1; S4 | page:6; page:8 | CP-1A | Conflicting | Filed | Logged, not reconciled |
| Segment revenue shares, nine months 2026 | same | 10-Q_2026-09-30 | S4 | page:9, page:10 | CP-1A | Calculated | Derived | Reperformed |
| Backlog of about one quarter of deliveries | same | none | none | no source | CP-1A | Untraced | None | Not supported; see CP5-004 |
| FY2024 undrawn revolver 764.5 | same | 10-K | S1 | page:74, page:77 | CP-1 Liquidity | Analyst Inference | Derived from April 2025 text | Commitment inferred as 900.0 |
| Identified secured debt 320.716 | same | 10-Q_2026-09-30 | S4 | page:14, page:17, page:18 | CP-1; CP-2 | Calculated | Derived | Floor, other financing obligations unsplit |
| Net homebuilding debt to net capital 34.9% | same | 10-Q_2026-09-30 | S4 | page:66 | CP-1; CP-2 | Sourced | Filed non-GAAP | Company definition |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM adjusted EBITDA | CP-1 Leverage; CP-2 | 349.705 (FY2025), 197.013 (9M 2026), 252.352 (9M 2025) | FY2025 + 9M 2026 − 9M 2025 = 294.366 | Calculated | Reperformed, agrees | High | PD, leverage | S1 page:91; S4 page:65 |
| Total debt / adjusted EBITDA | CP-1; CP-2 | 1,812.587 and 294.366 | 1,812.587 / 294.366 = 6.157, shown 6.16x | Calculated | Reperformed, agrees | High | PD, leverage | S4 page:14 |
| Net debt / adjusted EBITDA | CP-1; CP-2 | 1,812.587 − 86.086 = 1,726.501 and 294.366 | 1,726.501 / 294.366 = 5.865, shown 5.87x | Calculated | Reperformed, agrees | High | PD, leverage | S4 page:2, page:14 |
| Unadjusted ratios | CP-1; CP-2 | EBITDA LTM 236.052 | 1,812.587 / 236.052 = 7.68x; 1,726.501 / 236.052 = 7.31x | Calculated | Reperformed, agrees | High | PD | S1 page:91; S4 page:65 |
| Adjusted EBITDA / cash interest | CP-1; CP-2 | 583.926 and 78.9; 349.705 and 81.3 | 7.40x; 4.30x | Calculated | Reperformed, agrees | Medium | Debt service | S1 page:91, page:130 |
| Interest incurred proxy cover | CP-1; CP-2 | 294.366 and 81.424 | 3.62x | Calculated | Reperformed, agrees | Medium | Debt service | S1 page:130; S4 page:18, page:65 |
| Undrawn revolver | CP-1; CP-2 | 1,200.0 and 456.0 | 744.0 | Calculated | Reperformed, agrees | Medium | Liquidity | S4 page:16, page:17 |
| Debt effect alone | CP-1; CP-2 | 1,812.587 and 349.705 | 5.18x | Calculated | Reperformed, agrees | Medium | PD | S1 page:91 |
| Segment revenue shares | CP-1A; CP-2 | 2,581.367 total | segment / total | Calculated | Reperformed, agrees | High | Concentration | S4 page:9, page:10 |
| Identified secured debt | CP-1; CP-2 | 129.450 and 191.266 | Sum = 320.716 | Calculated | Reperformed, agrees | Medium | LGD mechanics | S4 page:14 |
| FY2024 revolver commitment | CP-1 Liquidity | 900.0 inferred from April 22, 2025 increase text | Assumption-Based inference | Assumption-Based | Disclosed in basis | Medium | Liquidity | S1 page:77 |
| Backlog share of deliveries | CP-1A | 1,106 backlog; 2,442 deliveries (Q3) or 6,961 (nine months) | Reperformed 45.3% and 15.9%; stated "about one quarter" matches neither | Not Calculable as stated | Contradicted | Low | Revenue visibility | S4 page:37 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Covenant limits and revised financial covenants | Described from 10-Q summaries only; the executed Credit Agreement, First Amendment and indentures are not supplied | Weak Lineage | Liquidity availability and legal capacity depend on covenant terms; unverified terms could change the liquidity assessment | Obtain and review the executed documents; label summaries as company descriptions | CP-1 Liquidity and covenants; CP-1A Ownership, governance; CP-2 Gaps |
| Minor | Backlog gives limited visibility | Comparison "about one quarter of deliveries" has no source or calculation | Untraced | Revenue-visibility wording could mislead a reader | State the reperformed ratios (45.3% of Q3 deliveries, 15.9% of nine-month deliveries) | CP-1A Company and operating model |
| Minor | FY2024 undrawn revolver 764.5 | Commitment of 900.0 at 2024-12-31 is inferred from text about an April 2025 increase | Analyst Inference | Small effect on the liquidity trend | Confirm from the FY2024 annual report | CP-1 Chart data: liquidity |
| Minor | Century Complete states | The 10-K and Q3 10-Q state lists differ | Conflicting | Segment geography is uncertain | Confirm in a later filing | CP-1A Conflicts |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2025 and three 2026 quarters; no executed debt documents | Missing contracts leave covenant and priority claims on summaries | Covenant headroom and legal capacity are unverified | Obtain the executed agreements |
| Citation completeness | Ready with Remediation | Every printed figure was found on a cited page; three statements have no or weak source | Unsupported wording can overstate visibility or certainty | Minor wording, no conclusion changes | Correct the flagged statements |
| Calculation traceability | Committee-Ready | Eleven of twelve calculation items were reperformed and agree; the backlog comparison does not | Calculations are reproducible from filed inputs | Leverage and liquidity figures can be relied on | None |
| Assumption transparency | Ready with Remediation | Revolver commitment at 2024-12-31 and letters-of-credit treatment are disclosed as inferences or gaps | Undisclosed assumptions would hide liquidity uncertainty | Small effect | Confirm from source documents |
| Markdown/export artifact integrity | Committee-Ready | All four handoffs carry the required headings, source hashes and handoff hashes | Broken lineage would block downstream use | Handoffs are consumable | None |

Overall auditability: Ready with Remediation.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed debt documents | Credit Agreement, First Amendment, Incremental Joinder, two indentures | Covenant levels, baskets and availability govern liquidity and creditor control | Covenant statements are summaries; headroom not calculable | High impact | Executed agreements from the company's filings |
| CP-5-GAP-002 | Cash interest paid for 2026 | Interim cash interest | Debt service cover for the latest period rests on an accrual proxy | Chart cell Not supplied | Medium impact | Next annual report |
| CP-5-GAP-003 | Letters of credit allocation | Facility-level split of 42.3 | Revolver availability could be lower by up to 42.3 | Liquidity may be overstated by up to that amount | Medium impact | Credit Agreement or lender data |
| CP-5-GAP-004 | HistoryMaker Homes funding and purchase accounting | Funding source, allocation, pro forma | Post-quarter leverage and liquidity unmeasured | CP-1 and CP-2 exclude the deal from ratios | Medium impact | Q4 2026 filings |
| CP-5-GAP-005 | Proxy statement | Related-party and control detail | Governance judgement uses risk-factor text only | CP-1A governance rows | Medium impact | 2026 proxy statement |
| CP-5-GAP-006 | Ratings and market data | Context carries no ratings, quotes or deal terms | No external cross-check | No relative-value or rating claim made | Low impact | Context inputs |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 response, run ccs-2026-11-05-credit_snapshot-host, sha256 c251b674… | Source readiness for seven sources | Filed sources; releases are management documents | Six required headings present | Accepted by CP-OS structural check | Ready with limitations |
| CP-1 | requests/CP-1 response, same run, sha256 deba02fb… | Financial base, FY2024 to LTM Q3 2026 | Filed statements | Six required headings and chart selectors present | Accepted by CP-OS structural check | Findings in this review |
| CP-1A | requests/CP-1A response (attempt 2), same run, sha256 0d321ce4… | Business and transaction context | Filed statements and management language | Six required headings and selectors present | Accepted by CP-OS structural check | Findings in this review |
| CP-2 | requests/CP-2 response, same run, sha256 1f879b07… | Credit synthesis | Upstream only | Six required headings and selectors present | Accepted by CP-OS structural check | Findings in this review |

Module Status: Ready with Limitations.

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Company and operating model, Backlog and communities | Unsupported | "Backlog of about one quarter of deliveries" is not supported: backlog of 1,106 homes is 45.3% of Q3 deliveries of 2,442 and 15.9% of nine-month deliveries of 6,961 | State the ratio with its base | Pass with Remediation |
| Minor | CP-1A | Company and operating model, Revenue mix | Partially Supported | Century Complete is described as a low-price, no-option model and the segments as regions; the filing says entry-level buyers and no options, and Century Complete is a brand segment | Use the filing wording | Pass with Remediation |
| Minor | CP-2 | Strengths, diversified operations | Partially Supported | "Five regional homebuilding segments ... none above 25.0%" treats Century Complete, at 25.0%, as regional | Say four regions and one brand segment | Pass with Remediation |
| Minor | CP-1 | Chart data: liquidity, 2024-12-31 | Partially Supported | Commitment of 900.0 at 2024-12-31 is inferred from the April 22, 2025 increase text, not stated for that date | Mark as inferred or confirm | Pass with Remediation |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1; CP-2 | Net debt is used in three senses: total debt less cash and equivalents (5.87x), the company's net homebuilding debt to net capital (34.9%, which deducts escrow and excludes repurchase and construction debt), and company liquidity (which includes escrow) | Definitions differ by perimeter and by escrow treatment; each is labelled in CP-1 but CP-2 places them side by side | None; the filings define their own measures | Keep labels at every use; do not compare the measures | Pass with Remediation |

All other calculations were reperformed from cited inputs and agree with the handoffs (T5B.5).

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1; CP-1A; CP-2 | Credit Agreement limits on liens, debt, dividends, redemptions and affiliate transactions; revised financial covenants; indenture limits on secured debt; compliance with all covenants | Executed Credit Agreement, First Amendment, Incremental Joinder and both indentures | Only the company's 10-Q summaries are supplied; no clause-level support; no capacity calculation was attempted, which is correct | Label as company summary; obtain executed documents | Legal review required before covenant or basket conclusions |
| Minor | CP-1; CP-2 | Unsecured notes are "effectively subordinated" to identified secured debt of 320.716 at "guarantor level", and CP-2 adds the mortgage subsidiary's lines | Indentures and security documents | Construction loans sit at Century Living subsidiaries and repurchase lines at the non-guarantor Inspire; the 320.716 already includes the repurchase lines; this blends effective and structural subordination and double-counts in CP-2 wording | State which debt is at which obligor and do not add the lines twice | Legal review for priority conclusions |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1; CP-1A; CP-2 | No relative-value, spread, price, rating or comparable-set claim is made | Market quotes and ratings are blank in the context | No market input to test | None beyond keeping RV out of the credit view | Committee must source market views separately |

#### T5.6 Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A; CP-2 | The Century Complete state list differs between the 10-K (nine states) and the Q3 10-Q (ten states, including Nevada); CP-1A logs it, CP-2 does not mention it. Issuer id, perimeter, period, currency, debt, liquidity, maturities and the 6.16x and 5.87x ratios are identical across CP-1, CP-1A and CP-2 | Different filing dates, 2026-01-29 versus 2026-10-29 | Confirm the list in a later filing | None for credit ratios |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1; CP-1A; CP-2 | Duplicative content | The covenant and acquisition-funding gaps are restated in each handoff's findings and in its gap table | Keep one statement where it changes a conclusion | Reading load only |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Chart data: debt maturities | The maturity table mixes calendar years with overlapping buckets (through May 2027, December 2026 to February 2029) and two Not supplied cells; a chart reader could plot them as separate years | Label the buckets as ranges in the chart or split by year when facility schedules are available | Chart consumers need the basis column |
| Minor | CP-0; CP-1; CP-1A; CP-2 | Transport envelope | The handoffs use the CP-OS six-heading Markdown transport without the standalone YAML envelope fields (confidence score, committee status), so those fields are not auditable here | Record them in the delivery metadata | None for content |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-1; CP-1A; CP-2 | Legal source dependency | Covenant and legal statements rest on 10-Q summaries; executed agreements not supplied | Obtain and review executed documents | Restricts committee use | Open |
| CP5-002 | MINOR | CP-1A | Unsupported claim | Backlog "about one quarter of deliveries" | State 45.3% of Q3 and 15.9% of nine-month deliveries | Pass with Remediation | Open |
| CP5-003 | MINOR | CP-1A | Partially supported claim | Century Complete described as low-price and segments as regional | Use filing wording | Pass with Remediation | Open |
| CP5-004 | MINOR | CP-2 | Partially supported claim | Five "regional" segments, none above 25.0% | Four regions and one brand segment | Pass with Remediation | Open |
| CP5-005 | MINOR | CP-1 | Inference | 900.0 commitment at 2024-12-31 inferred | Mark or confirm | Pass with Remediation | Open |
| CP5-006 | MINOR | CP-1; CP-2 | Definition drift | Three net debt senses | Keep labels | Pass with Remediation | Open |
| CP5-007 | MINOR | CP-1; CP-2 | Structural claim wording | Effective versus structural subordination and double-count | Clarify obligors | Pass with Remediation | Open |
| CP5-008 | MINOR | CP-1; CP-1A; CP-2 | Market data | No market or rating inputs in context | Source separately | Pass with Remediation | Open |
| CP5-009 | MINOR | CP-1A; CP-2 | Cross-module version | Century Complete state list difference not carried by CP-2 | Confirm in later filing | Pass with Remediation | Open |
| CP5-010 | MINOR | CP-1; CP-1A; CP-2 | Duplication | Covenant and funding gaps restated | Single statement | Pass with Remediation | Open |
| CP5-011 | MINOR | CP-1 | Chart labelling | Overlapping maturity buckets | Label as ranges | Pass with Remediation | Open |
| CP5-012 | MINOR | CP-0; CP-1; CP-1A; CP-2 | Envelope | Standalone envelope fields not carried | Record in delivery metadata | Pass with Remediation | Open |

## Calculations

Independent recomputation of the upstream figures that drive the top drivers, in US$ thousands as printed unless stated.

| Item | Formula and inputs | Result | Agrees with handoff |
| --- | --- | --- | --- |
| LTM adjusted EBITDA | 349,705 + 197,013 − 252,352 | 294,366 | Yes |
| LTM EBITDA | 284,630 + 160,168 − 208,746 | 236,052 | Yes |
| Total debt / adjusted EBITDA | 1,812,587 / 294,366 | 6.157x | Yes (6.16x) |
| Net debt / adjusted EBITDA | (1,812,587 − 86,086) / 294,366 = 1,726,501 / 294,366 | 5.865x | Yes (5.87x) |
| Total debt / EBITDA and net debt / EBITDA | 1,812,587 / 236,052; 1,726,501 / 236,052 | 7.679x; 7.314x | Yes |
| FY2024 and FY2025 total debt / adjusted EBITDA | 1,476,213 / 583,926; 1,443,145 / 349,705 | 2.528x; 4.127x | Yes |
| Adjusted EBITDA / cash interest | 583.926 / 78.9; 349.705 / 81.3 | 7.401x; 4.301x | Yes |
| Interest incurred, LTM | 81,980 + 57,466 − 58,022 | 81,424 | Yes |
| Undrawn revolver and liquidity tie | 1,200.0 − 456.0; 86.086 + 33.740 + 744.0 | 744.0; 863.826 | Yes (863.8 printed) |
| Revolver net drawings, nine months | 1,584.3 − 1,179.8 | 404.5 | Yes |
| Backlog ratios | 1,106 / 2,442; 1,106 / 6,961 | 45.3%; 15.9% | No: handoff says about one quarter |
| Identified secured debt | 129.450 + 191.266 | 320.716 | Yes |

## Gaps

| Gap | Severity | What it affects | Action |
| --- | --- | --- | --- |
| Executed Credit Agreement, First Amendment, Incremental Joinder and indentures not supplied | High | Every covenant, availability and priority statement | Obtain and review before committee use |
| Cash interest for 2026, letters-of-credit allocation, acquisition funding, proxy detail, ratings and market inputs not supplied | Medium | Debt service cover, availability, post-deal leverage, governance, external cross-check | See CP-5-GAP-002 to CP-5-GAP-006 |
| Prior-period 2025 interim filings not supplied; comparatives are recast | Low | LTM series rest on derived figures | Label as derived |
| This review used the pinned sources and the four handoffs only; no external source was used | Low | Scope | None |

## Next module

None in this run. CP-5 is the last selected module; the report can be published subject to the Restricted committee-use clearance above. Remediation: obtain the executed debt agreements, correct the minor wording items listed in the issue log, and re-run the affected modules in a new run folder if the handoffs are to be corrected, because accepted answers cannot be replaced.
