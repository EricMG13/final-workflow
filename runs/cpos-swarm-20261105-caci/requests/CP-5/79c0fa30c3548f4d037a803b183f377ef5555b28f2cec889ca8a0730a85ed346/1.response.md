## Request

Module: evidence trace and research-integrity review for CACI INTERNATIONAL INC /DE/ (issuer id caci), as of 2026-11-05, cutoff 2026-11-05, pathway credit snapshot, minimum module set. It checks the CP-0, CP-1, CP-1A and CP-2 handoffs against the pinned sources and against each other, and grades them. The review was performed by the same host session that wrote the four handoffs, so it is a self-review and not an independent one. QA envelope: qa_status Passed; Confidence Score 41, band Low (script output, see Calculations); committee status Requires More Work.

## Sources

### Issuer sources

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2026-06-30_caci-20260630.htm.jsonl | f2d21cb22e8c5506b4bb126ec8c544c48dff7d613005574465264d0d51f72c87 |
| 10-Q_2025-12-31_caci-20251231.htm.jsonl | 6f56468069c0ca930d3949dd2a9dc046bc39d9a3ee2fbfe67786310e4a593a88 |
| 10-Q_2026-03-31_caci-20260331.htm.jsonl | 743998e742f09f0797de29d0f737948ca0facb537bfd7546eb293e55de92e220 |
| 10-Q_2026-09-30_caci-20260930.htm.jsonl | dea393e31122fa0362a795e376fb4e1b82a07df3fbc9a647679762ac053e54fc |
| EX-99.1_2026-04-22_fy26-q3caci20260422ex991.htm.jsonl | 3baba025aa721deb2088cd8c20105e1486e76edc2a788c07afcf9740e7703457 |
| EX-99.1_2026-08-05_fy26-q4caci20260805ex991.htm.jsonl | 365693dc6db2c9b512bcdf65c2cb01ffe29245082e9245fc25f8496d007e334e |
| EX-99.1_2026-10-21_fy27-q1caci20261021ex991.htm.jsonl | 5ac06623a6e500e9ed51b547855a7fd7b4c66f8019da3cafa8cd0fb6f8596399 |

User context (settings, not issuer evidence): context sha256 771458f144b8d7a95d0c8ef74d2f2b133b5846c23aea051905b07e94014f45fd.

### Handoffs supplied

| Module | sha256 |
| --- | --- |
| CP-0 | 762cecbf926d995975842c532bf62ee7e0ca710d78ac7cdd487a629157bb5aa2 |
| CP-1 | 754b7bb7e2540f70cdcb2620bcf9c754b96a73b97c903a97135c15c797fe1220 |
| CP-1A | 41d334b949508139d8f80ad17071c0d78219e102c14bb94f127f21d949bc8517 |
| CP-2 | 6c8d0aab4cf5415e4ddcd2499187d65727f89741b83012a35b67c505a51a9952 |

Locators are the source chunk shown as page:N, which is not the printed page.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is traceable for a statement-based view of debt, liquidity, cash flow and business risk. Printed figures match the sources and derived figures recompute. Covenant, guarantor and run-rate leverage conclusions are not traceable. | Low | Executed debt documents are absent and the review was done by the same host that wrote the handoffs, so it is a self-review. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 70 quoted spans were found in the pinned sources, and 24 of 24 statement and schedule re-additions tie. | Reported balance sheet, debt, earnings and cash flow figures can be relied on as printed. | High |
| Leverage, cover and liquidity ratios recompute exactly from printed inputs, for example 3.94x total debt to EBITDA on the twelve months to September 30, 2026. | Credit metrics in the financial base are reproducible, though not covenant ratios. | High |
| Covenant headroom and entity-level ranking rest on a management compliance statement because no debt document is supplied. | A covenant or structure judgment cannot be supported from this pack. | High |
| Five minor defects were found, including a derived sum, a derived undrawn figure and a receivable program claim tagged as fact. | No conclusion changes; the claims need relabelling or exact references in a later run. | Medium |

### Evidence trace view

The analysis is traceable enough for a statement-based view of CACI's debt, liquidity, cash flow and business risk, and not for covenant, guarantor or run-rate leverage conclusions. Every printed figure in the financial base is found in the pinned sources, every derived figure recomputes exactly, and every quoted span sits in source text. Coverage of nine material claims: three directly sourced, two calculated, three analyst inferences and one open gap. The critical provenance gap is the absence of the executed debt documents: covenant headroom and ranking by entity rest on a compliance statement only. The affected decision is any covenant or structure judgment. Remediation owner: the sourcing step. Five minor defects need no change to any conclusion.

| Traceability summary | Result |
| --- | --- |
| Quoted spans checked against source text | 70 spans in three handoffs; none misquoted |
| Statement and schedule re-additions | 24 of 24 equal |
| Ratios and last-twelve-month bridge items recomputed | 12 of 12 ratios and 14 of 14 bridge rows equal |
| Printed figures in the financial base found in sources | All; the remainder are labelled calculations |
| Material claims by lineage | 3 Directly Sourced, 2 Calculated, 3 Analyst Inference, 1 open gap |
| Open findings | 5 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2026-06-30_caci-20260630.htm.jsonl | High: filed, audited annual report | Fiscal years ended June 30, 2026, 2025 and 2024 | CACI International Inc, consolidated | Statements, debt note, leases, receivable sale note, acquisitions, segments, legal note, exhibit index | Text extraction of the filed HTML | CP-0, CP-1, CP-1A |
| S2 | 10-Q_2025-12-31_caci-20251231.htm.jsonl | High: filed, unaudited interim report | Quarter and six months ended December 31, 2025 | Same | Interim statements, debt note, covenant types | Unaudited; extraction | CP-0, CP-1 |
| S3 | 10-Q_2026-03-31_caci-20260331.htm.jsonl | High: filed, unaudited interim report | Quarter and nine months ended March 31, 2026 | Same | Interim statements, debt, undrawn revolver | Unaudited; extraction | CP-0, CP-1 |
| S4 | 10-Q_2026-09-30_caci-20260930.htm.jsonl | High: filed, unaudited interim report, latest period | Quarter ended September 30, 2026 | Same | Interim statements, debt, swaps, receivable program, subsequent event, legal | Unaudited; extraction | CP-0, CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-04-22_fy26-q3caci20260422ex991.htm.jsonl | Medium: issuer earnings release | Quarter and nine months ended March 31, 2026 | Same | EBITDA reconciliation, free cash flow | Non-GAAP management measures | CP-0, CP-1 |
| S6 | EX-99.1_2026-08-05_fy26-q4caci20260805ex991.htm.jsonl | Medium: issuer earnings release | Quarter and year ended June 30, 2026 | Same | Discrete fourth quarter, EBITDA reconciliation, awards, guidance | Non-GAAP; guidance is a forecast | CP-0, CP-1, CP-1A |
| S7 | EX-99.1_2026-10-21_fy27-q1caci20261021ex991.htm.jsonl | Medium: issuer earnings release | Quarter ended September 30, 2026 | Same | EBITDA reconciliation, KPIs, raised guidance | Non-GAAP; no mention of the fiscal-year change | CP-0, CP-1, CP-1A |
| S8 | context | User settings, not evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency | Not issuer evidence; ratings, sponsor and deal fields blank | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage after the March 2026 acquisition: 3.94x total debt to EBITDA on the latest twelve months | CP-1, CP-2 | Debt principal and EBITDA reconciliations | Sets leverage tolerance | Core leverage metric | S4 page:9; S6 page:12; S7 page:10; S1 page:86 | Not pro forma; not a covenant ratio |
| 2 | Liquidity and light near-term maturities | CP-1, CP-2 | Cash, undrawn revolver, maturity table | Low near-term default risk | Monitoring horizon | S4 pages:3, 21; S1 page:89 | Receivable program not counted |
| 3 | Federal customer concentration and funding conditions | CP-1A, CP-2 | Customer shares, termination rights, continuing resolution | Concentrates revenue risk in one payer | Sets business risk | S1 pages:8, 12, 50; S4 pages:16, 17 | None beyond labels |
| 4 | Cash interest cover 5.60x on the latest twelve months | CP-1, CP-2 | EBITDA and cash paid for interest | Debt service capacity | Cushion over interest | S1 page:67; S4 page:4; S7 page:10 | Quarterly cash interest omits note coupons |
| 5 | Covenants, guarantors and ownership not verifiable | CP-0, CP-1, CP-1A, CP-2 | Exhibit index lists debt documents not supplied | Determines default distance and ranking | Restricts committee use | S1 pages:104, 105; S2 page:12 | Documents absent from the pack |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debt principal, maturities, rates and security wording | CP-1, CP-1A | S1 pages:86, 88, 89; S4 page:9 | Yes | High | Documentary Fact | Supported | High | Traced |
| Leverage and net leverage ratios | CP-1, CP-2 | Debt, cash and EBITDA inputs | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Cash interest cover | CP-1, CP-2 | S1 page:67; S4 page:4; releases | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Liquidity and maturity wall | CP-1, CP-2 | S4 pages:3, 21; S1 page:89 | Yes | High | Documentary Fact | Supported | High | Traced |
| Customer concentration and contract mix | CP-1A, CP-2 | S1 pages:8, 12, 52; S7 page:8 | Yes | High | Documentary Fact | Supported | High | Traced |
| Run-rate leverage may be overstated | CP-1, CP-2 | Acquisition date against the latest twelve months | Yes, inferred | Medium | Analyst Interpretation | Supported as an inference | Medium | Traced to dates, size not quantified |
| Receivable program near its cap | CP-1, CP-2 | S4 page:8 sold balance 349,999 against maximum | Yes, inferred | Medium | Analyst Interpretation | Supported as an inference | Medium | Traced; CP-2 tags it as fact |
| More fixed-price work raises margin variability | CP-1A, CP-2 | S7 page:8; S1 page:52 | Yes, inferred | Medium | Analyst Interpretation | Supported as an inference | Medium | Traced |
| Covenant headroom, guarantors, ownership | CP-0, CP-1, CP-1A, CP-2 | Debt documents and proxy not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt 4,864.438 at September 30, 2026 | pinned pack | 10-Q_2026-09-30_caci-20260930.htm.jsonl | S4 | page:9, Note 8 | CP-1 leverage and instrument tables | Reported | High | Instrument rows re-added equal |
| Undrawn revolver 1,395.0 | pinned pack | 10-Q_2026-09-30_caci-20260930.htm.jsonl | S4 | page:21, liquidity | CP-1 liquidity table | Reported | High | Equals commitment less drawn |
| EBITDA 1,173.914 FY2026 | pinned pack | EX-99.1_2026-08-05_fy26-q4caci20260805ex991.htm.jsonl | S6 | page:12 | CP-1 financials table | Issuer non-GAAP | Medium | Reconciliation re-added equal |
| EBITDA 328.828 and 268.613 for the two first quarters | pinned pack | EX-99.1_2026-10-21_fy27-q1caci20261021ex991.htm.jsonl | S7 | page:10 | CP-1 financials table | Issuer non-GAAP | Medium | Reconciliations re-added equal |
| Cash paid for interest 213.640 FY2026 | pinned pack | 10-K_2026-06-30_caci-20260630.htm.jsonl | S1 | page:67 | CP-1 interest cover | Reported | High | Matches |
| Federal share 95.6% of FY2026 revenue | pinned pack | 10-K_2026-06-30_caci-20260630.htm.jsonl | S1 | page:12 | CP-1A operating model | Reported | High | Matches |
| Acquisition consideration 2,642.7 and 2,637.7 | pinned pack | 10-K and 10-Q S1 and S4 | S1, S4 | S1 page:79; S4 page:5 | CP-1A conflicts | Reported | High | Version difference logged, not reconciled |
| Fiscal-year change approved October 20, 2026 | pinned pack | 10-Q_2026-09-30_caci-20260930.htm.jsonl | S4 | page:13, Note 14 | CP-0, CP-1, CP-1A | Reported subsequent event | High | Matches |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Last-twelve-month bridge, 14 rows | CP-1 financials table | FY2026, Q1 FY2027 and Q1 FY2026 printed values | FY2026 plus Q1 FY2027 less Q1 FY2026 | Recomputed: 14 of 14 equal | Supported | High | Basis of LTM ratios | S1 pages:66, 67, 98; S4 pages:2, 4, 12 |
| Total debt and net debt leverage | CP-1 leverage chart; CP-2 | Principal debt, cash, EBITDA | Debt over EBITDA; (debt less cash) over EBITDA | Recomputed: 3.04x, 4.20x, 3.94x and 2.93x, 4.04x, 3.72x equal | Supported | High | Leverage tolerance | S1 pages:67, 86; S4 pages:3, 9 |
| Interest cover | CP-1 cover chart; CP-2 | EBITDA, cash paid for interest | EBITDA over cash interest | Recomputed: 6.67x, 5.49x, 5.60x, 7.51x, 7.72x equal | Supported | High | Debt service | S1 page:67; S4 page:4 |
| Liquidity | CP-1 liquidity chart | Cash plus undrawn revolver | Sum | Recomputed: 1,674.389 and 1,531.756 equal | Supported | High | Near-term funding | S4 pages:3, 21; S1 pages:53, 66 |
| Floating principal and unhedged part | CP-1 interpretation; CP-2 | Four floating instruments and swap notional | Sum; difference | Recomputed: 3,364.438 and 1,964.438 equal | Supported | High | Rate exposure | S4 page:9 |
| EBITDA reconciliations, four periods | CP-1 definition review | Net income, taxes, net interest, D&A | Re-addition | Recomputed: four of four equal | Supported | High | Definition check | S6 page:12; S7 page:10 |
| Confidence Score | This handoff | 9 material claims, 17 of 17 registers, partial gate, 5 MINOR | Script formula | 41, band Low | Script output | High | QA envelope | confidence_score.py output |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 senior unsecured notes total | A total of 1,500.0 for the two note issues is not a figure in the financial base; it adds two rows that are there | Derived figure | CP-2 says it calculates nothing new | Reference the two rows or add the sum to the financial base | CP-2 key findings |
| MINOR | CP-1 liquidity table, December 31, 2025 | Undrawn revolver of 2,000.0 is derived from the commitment and the statement of no borrowings, not printed as undrawn; the cell says so | Derived figure | A reader may take it as printed | Keep the basis note, or label the cell derived | CP-1 liquidity chart |
| MINOR | CP-2 weaknesses | Receivable program at its cap is tagged Documentary Fact; the filing prints a sold balance and a maximum but does not state capacity used, and a net remaining sold balance of 189.280 is also printed | Mis-tagged inference | Overstates certainty about a funding source | Tag as Analyst Interpretation | CP-2 strengths and weaknesses |
| MINOR | CP-1A company profile | Sector row is tagged Documentary Fact but comes from the user context, which is not issuer evidence | Mis-tagged source | The context is settings, not evidence | Tag as context or Insufficient Information for the sector | CP-1A company profile |
| MINOR | CP-1, CP-1A locators | Locators use short forms such as Q1 10-Q and 10-K and some page lists, not the exact file name | Imprecise locator | Slower verification; no misquotation | Use exact file name plus page | CP-1, CP-1A |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; each filing names its period on its cover | A wrong document would change every figure | None found | None |
| Quotation accuracy | Strong | 70 of 70 quoted spans found in the pinned text | A misquote would misstate a fact | None found | None |
| Calculation reproducibility | Strong | 12 of 12 ratios, 14 of 14 bridge rows and 24 of 24 re-additions equal | Calculation errors would move leverage | None found | None |
| Locator precision | Adequate | Most locators give file and page; shorthand in some | Slower checks | None on conclusions | Exact file and page |
| Cross-module consistency | Strong | CP-2 figures found in CP-1 or CP-1A except one derived sum; CP-1 states its one correction of CP-0 | Inconsistent figures mislead a committee | None found | Fix the one sum |
| Reviewer independence | Weak | The same host wrote and checked the handoffs | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant levels, definitions, reported ratios and headroom | Credit agreement, term loan agreement, indentures | Default distance cannot be sized | Covenant risk rows in CP-1 and CP-2 | Covenant view rests on a management statement | Executed debt documents listed in the exhibit index |
| G2 | Guarantors and collateral schedule | Subsidiaries exhibit and guarantor schedules | Ranking by entity cannot be built | Structure view | Moderate | Exhibits to the 10-K and indenture supplements |
| G3 | Pro forma earnings of the acquired business | Pro forma or later full-period data | Run-rate leverage not sized | Leverage and cover findings | Moderate | Later filings (after the cutoff) or acquirer data |
| G4 | Ownership and control rights | Proxy statement | Governance view limited | CP-1A governance rows | Moderate | Proxy statement |
| G5 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / caci-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed, no finding | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, LTM, debt, liquidity, maturities, outside-debt claims | High | Six headings; accepted | Passed with 2 MINOR findings | States its one correction of CP-0 |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, transaction, governance, timeline, conflicts | High | Six headings; accepted | Passed with 2 MINOR findings | Three conflicts logged, none reconciled |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Passed with 2 MINOR findings | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A | Locators in tables | Supported | Short-form locators without the exact file name | Cite exact file and page | None |
| MINOR | CP-1A | Sector row | Supported by context only | Context tagged as Documentary Fact | Retag | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Notes total of 1,500.0 | Sum of two CP-1 rows, not in CP-1 | None | Reference the rows | None |
| MINOR | CP-1 | Undrawn revolver at December 31, 2025 | Derived by identity from commitment and nil borrowings | None; cell discloses the basis | Label as derived | None |
| MINOR | CP-1 | EBITDA as leverage denominator | Management EBITDA, not covenant EBITDA; stated in CP-1 | Definition differs from any covenant measure, which is not supplied | Keep the caveat, as CP-1 does | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1, CP-1A, CP-2 | Covenant compliance, guarantors, security and ranking of the notes | Credit agreement, term loan agreement, indentures, guarantor schedules | Documents not supplied; claims correctly limited to the filings' prose and a management compliance statement | Supply the documents | Required before any covenant or structure view |
| MINOR | CP-1, CP-2 | Notes described as senior unsecured and, in the same note, subordinated to senior secured debt | Indenture | Wording quoted as printed and not reinterpreted | Read the indenture | Required for ranking detail |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made; prices, spreads and ratings are outside the minimum set | Prices, spreads and ratings | Recorded by design; ratings absent from the context | Add market data only if a later module needs it | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1 | CP-0 said no Q1 FY2026 balance sheet items were supplied; CP-1 found cash and equity at that date in later comparatives and states the correction | CP-1 cites the accepted CP-0 hash | None needed; correction is explicit | None |
| MINOR | CP-2 | One derived sum not in CP-1 | CP-2 cites accepted CP-1 and CP-1A hashes | Reference the rows | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | The statement-based view is traceable; covenant and structure views are not; review is a self-review | Supply the debt documents and an independent review | Committee status Requires More Work |
| MINOR | CP-1, CP-1A, CP-2 | Duplication | Financial figures are restated in three handoffs; values agree | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A | Locator form | Short-form locators in tables | Use exact file name plus page | None; all four handoffs accepted at attempt 1 |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-2 | Derived figure | Notes total of 1,500.0 not in CP-1 | Reference the two rows | None | Open |
| QA-2 | MINOR | CP-1 | Derived figure | Undrawn revolver at December 31, 2025 derived, not printed | Label as derived | None | Open |
| QA-3 | MINOR | CP-2 | Mis-tagged inference | Receivable program at its cap tagged as Documentary Fact | Tag as Analyst Interpretation | None | Open |
| QA-4 | MINOR | CP-1A | Mis-tagged source | Sector row from context tagged as Documentary Fact | Retag | None | Open |
| QA-5 | MINOR | CP-1, CP-1A | Locator | Short-form locators | Use exact file name plus page | None | Open |

Clearance decision: Pass with conditions. Critical issues: 0. Material issues: 0 as defects (two items are readiness limits, not defects). Minor issues: 5. Committee use: Requires More Work, until the debt documents and an independent review are added.

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Every double-quoted span of six or more characters in CP-0, CP-1 and CP-1A searched in the pinned source text | 70 spans (CP-0 34, CP-1 5, CP-1A 31), none missing; CP-2 holds no quotation |
| Q2 | Printed figure trace | Every figure with three decimals in CP-1 and CP-1A converted to US$ thousands and searched in the pinned text | All printed figures found; of the 29 not found in CP-1, 28 are labelled calculations or sums that were recomputed and one (6.375) is the printed note rate written as a percent; the 2 not found in CP-1A are a CP-1 sum and the same rate |
| Q3 | Ratio recomputation | Debt, cash, EBITDA and cash interest taken from source pages and the ratios recomputed independently | 12 of 12 equal to CP-1 |
| Q4 | Bridge recomputation | FY2026 plus Q1 FY2027 less Q1 FY2026 for each of 14 rows | 14 of 14 equal |
| Q5 | Tie-outs | Balance sheet sections, segment sums, contract and customer mix sums, instrument and maturity totals, four EBITDA reconciliations, undrawn identity re-added | 24 of 24 equal |
| Q6 | Confidence Score | confidence_score.py with lineage Directly Sourced 3, Calculated 2, Analyst Inference 3, Insufficient Information 1; 17 of 17 registers; source gate partial; 5 MINOR findings | score = clamp((0.6 x 66.67 + 0.4 x 100) x 0.7 - 15) = 41; band Low; qa_status Passed |

## Gaps

- G1, critical for covenant and structure views: executed debt documents are not supplied, so covenant levels, definitions, headroom and guarantors cannot be traced.
- G2: pro forma earnings of the acquired business are not supplied, so run-rate leverage is not sized.
- G3: ownership and control rights are not supplied.
- G4: the fiscal-year change makes the next report a six-month transition period; the guidance basis in the October 21, 2026 release is not reconciled to it.
- G5: no independent review; this review was written by the same host.

## Next module

- Report delivery: carry qa_status Passed, Confidence Score 41 (Low), committee status Requires More Work, and gap G1.
- Swarm review: an independent agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Sourcing: add the executed credit agreement, term loan agreement, indentures, guarantor schedules and proxy statement, then rerun the four modules in a new run folder.
- Minor repairs for a later run: relabel the receivable program claim, the derived sum and the derived undrawn figure; use exact file names in locators.
