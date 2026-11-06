## Request

This module is the evidence trace and research-integrity review of the CoreWeave, Inc. (CRWV) run as of 2026-11-05, on the credit snapshot pathway and from the creditor perspective. It re-checks the source readiness, financial base, business and transaction context and credit synthesis handoffs against the seven pinned sources and against each other. It changes no credit conclusion and repairs no accepted handoff; defects are logged for the reader.

## Sources

### Issuer sources

Each source was opened for this review: quotes were matched to their cited pages and printed inputs were re-read for the reperformed calculations.

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_crwv-20251231.htm.jsonl | 0d0cf44f53b9a917ce74530e1073134d5052786896b56bf540c0ff56c3d09cf5 |
| 10-Q_2025-09-30_crwv-20250930.htm.jsonl | 4ab2a43787603e448a27ee75655cd8189c101995b2b2a09f948fefcf24dc65dc |
| 10-Q_2026-03-31_crwv-20260331.htm.jsonl | 02ad347fc934b455da7d76c35b5ed5e2481a8b415629a65ddd1d28789dd893ea |
| 10-Q_2026-06-30_crwv-20260630.htm.jsonl | 8c1fe67059916099b1322f23cd4d1d50ec7098f810b5bf54d990d03a024fa1d1 |
| EX-99.1_2026-02-26_coreweave4q25earningspress.htm.jsonl | d1cb2e7f415a836bfc361c60f3592d7d5ff529dbcae4e476b1fc937be4fb40b5 |
| EX-99.1_2026-05-07_coreweave1q26earningspress.htm.jsonl | e0f8ee20aa75c8abb15cd88aa7bc89813b32cc2ad3558378d8026da7d76cfee8 |
| EX-99.1_2026-08-11_coreweave2q26earningspress.htm.jsonl | af17b6e32fc6d5e125e64130df944ece5d560c39bdc4236cbad0414accede85b |

Context file (settings, not issuer evidence): sha256 98f66cde15d4d68ac95da915aeb204ed4c29c1430841991cd3be8e950d45a9a2.

### Handoffs

| Module | sha256 | How it was consumed |
| --- | --- | --- |
| CP-0 | 0a718ae2802587f76f44cc2a61e8815a4a88834928edca0479e39f7d34976401 | Opened and read in full; its quotes and page locators were re-checked against the sources. |
| CP-1 | df2a422a4928d9e15d084ff62a177ff909f3a1e751a2512de167ccad6229229c | Opened and read in full; every register quote was matched to its page and every derived figure was reperformed. |
| CP-1A | 15e6d01a799b4eadec41d419b7f13d7008399c50166b31b64beabfb6f8b5e942 | Opened and read in full; every verbatim quote was matched to its page and its calculations were reperformed. |
| CP-2 | e290f8612163f220fc92ee22d1a4caacbd176382aaf577d8dac347f401f7ca08 | Opened and read in full; every figure was matched to the financial base or the business context. |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The four handoffs trace to the filings: quotes resolve to their pages and derived figures reproduce. Five minor issues were found, with no critical or material defect. Committee use is restricted by missing covenant and guarantor documents. | Medium | Executed financing documents, covenant levels and guarantor lists are not in the sources, so legal and covenant claims trace only to filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every quoted figure checked resolved to its cited page, and the leverage, cover, liquidity and maturity figures reproduced from printed inputs. | The headline credit metrics can be relied on as stated. | High |
| The availability figure of USD 10,014 million reproduces exactly from facility sizes, balances and letters of credit on the revolver and three delayed-draw facilities. | Headline liquidity is traceable, though draw conditions limit what is usable. | High |
| Five minor issues remain: an unquantified secured-debt remark, a revolver repayment amount, an undated contract duration, a dividend timing remark and an earlier cash tax gap already corrected. | None changes a credit conclusion. | High |
| Covenant levels, guarantors and financing agreements cannot be traced because the documents are not in the sources. | Legal ranking, headroom and recovery mechanics rest on filing summaries only. | High |
| Management statements stay labelled as attributed claims, and four logged conflicts remain unreconciled. | Backlog and some maturity dates carry two stated values; the filing controls. | Medium |

### Evidence trace view

The evidence trace holds: the four handoffs rest on filed statements and notes, each material figure resolves to a pinned page, and every derived figure reproduced to the stated decimals. The strongest support is that all 36 re-read inputs, all register quotes and every arithmetic bridge, including the liquidity rebuild and the maturity schedule, agreed with the sources. The weakest point is legal and covenant lineage: the credit agreements, indentures and guarantor lists are listed as exhibits but not supplied, so ranking, guarantees and headroom trace only to summaries in the notes. What decides committee use is whether those documents and the third quarter 2026 report are added; until then the analysis is traceable but restricted, and the five minor defects below should be read with it.

### Analytical appendix — complete canonical registers

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 response 1; run crwv-2026-11-05-credit_snapshot-host; sha256 0a718ae2802587f76f44cc2a61e8815a4a88834928edca0479e39f7d34976401 | Source readiness for seven pinned sources | Filed statements and releases; text extraction without table-fidelity review | Six H2 headings, Readiness view after Reader summary: pass | Passed with one minor defect | Cash tax gap overstated; corrected in CP-1 |
| CP-1 | requests/CP-1 response 2; same run; sha256 df2a422a4928d9e15d084ff62a177ff909f3a1e751a2512de167ccad6229229c | Financial base, USD millions, Q2 2026 and FY2025 | Filed statements; releases for non-GAAP measures | Six H2 headings, four chart selectors and one metrics table: pass (attempt 2 after a word-limit rejection) | Passed with two minor defects | Covenant levels not supplied |
| CP-1A | requests/CP-1A response 1; same run; sha256 15e6d01a799b4eadec41d419b7f13d7008399c50166b31b64beabfb6f8b5e942 | Business, ownership, transaction context | Filed notes and risk factors; releases tagged as Management Language | Six H2 headings, two table selectors and one prose selector: pass | Passed with two minor defects | Ownership percentages not supplied |
| CP-2 | requests/CP-2 response 1; same run; sha256 e290f8612163f220fc92ee22d1a4caacbd176382aaf577d8dac347f401f7ca08 | Fundamental credit synthesis | Upstream handoffs only; no new source text | Six H2 headings, two prose selectors: pass | Passed with one minor defect | Inherits all upstream limitations |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Latest quarter table: the revolver "had 1.0 billion drawn at December 31, 2025" when it was repaid in April 2026 | Partially Supported | The April 2026 repayment applied to the balance at March 31, 2026, which the Q1 2026 10-Q debt table prints as 1,500, not 1,000 | State that 1,500 was outstanding at March 31, 2026 | Does not block committee use |
| MINOR | CP-1 | Financial base view: principal debt "is mostly secured" | Partially Supported | By principal about 52.7% is secured (delayed-draw loans 13,643 and OEM and software financing 5,102 are 18,745 of 35,551), and unsecured notes and convertibles are 16,617; the filings do not print a secured share and some OEM or software financing may be unsecured | Replace with "about half is secured by principal (calculated)" | Does not block committee use |
| MINOR | CP-1A | Distributions row: preferred dividends of 29 were paid in six months 2025 "before the IPO conversion" | Partially Supported | The Q2 2026 release cash flow statement prints a 3 payment in Q2 2025 and 29 for six months; whether the Q2 amount preceded conversion is not stated | Drop the timing remark or cite the conversion date | Does not block committee use |
| MINOR | CP-1A, CP-2 | Committed contracts at 98% of Q2 2026 revenue, and a weighted-average duration of about five years | Partially Supported | The 98% is revenue related to customer commitments including capacity delivered before commitment start dates; the five years is as of December 31, 2025 and CP-2 states it without the date | Add the definition and the date | Does not block committee use |
| MINOR | CP-0 | Gap 6: cash paid for income taxes "Not supplied" | Contradicted for FY2025 | The 10-K prints FY2025 cash income taxes net of refunds as (1) on its income tax note page | Already corrected in CP-1; no further action | Resolved downstream |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | LTM adjusted EBITDA uses the printed six-month 2025 figure of 1,360, while the two printed 2025 quarters sum to 1,359 | Rounding in the releases; the ratios are unchanged at two decimals (8.08x either way) | Releases only | None; keep the printed six-month figure | None |
| MINOR | CP-1 | Net debt deducts unrestricted cash and marketable securities only; restricted cash is shown separately | Definition stated in the handoff; the alternative of 28,632 is given | None | None | None |
| MINOR | CP-1 | Leverage uses period-end principal over LTM adjusted EBITDA; debt excludes operating leases and adjusted EBITDA is after operating lease cost | Numerator and denominator are consistent; no lease-adjusted ratio is given and the reason is stated | None | None | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Delayed-draw facilities are secured on subsidiary equity and assets and guaranteed by the parent except DDTL 4.0; notes are unsecured and guaranteed by certain wholly-owned subsidiaries | Credit agreements, indentures and the parent guarantee and pledge agreement | Documents are listed as exhibits but not supplied; the handoffs cite the note summaries and say so | Obtain the exhibits before any ranking or guarantor conclusion | Yes, before committee use |
| MINOR | CP-1, CP-2 | Covenant compliance statement for the delayed-draw agreements and the November 2025 revolver amendment of covenant metrics | Credit agreements and compliance certificates | No test, level or reported ratio is printed; headroom is correctly Not calculable | Obtain the agreements | Yes |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | No relative value, pricing or market claim is made; the high-risk label is a fundamental view | Ratings, quotes, peers, market capitalisation and enterprise value (context blanks, not zero) | The relative value and portfolio modules are omitted from this run | None for this run; supply market data if those modules are added | None for the fundamental view |

#### T5.6 Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1 | CP-0 lists FY2025 cash income taxes as Not supplied; CP-1 prints the 10-K figure | CP-1 states the correction; CP-0 cannot be edited | Read CP-0 gap 6 together with CP-1 gap 3 | None |
| MINOR | CP-1A, CP-2 | CP-2 repeats the five-year contract duration without the December 31, 2025 date given in CP-1A | Staleness of one period | Add the date when restated | None |
| MINOR | CP-1, CP-1A, CP-2 | Logged conflicts agree across modules: backlog of about 104 billion versus 103.7 billion of remaining performance obligations; DDTL 5.0 final maturity November 2031 versus May 2031; DDTL 2.1 maturity December 2030 versus March 2031; customer labels across periods | None | Keep unreconciled | None |
| MINOR | CP-1, CP-1A, CP-2 | Shared figures agree: principal debt 35,551, adjusted EBITDA 4,400, leverage 8.08x and 6.82x, cover 3.35x, free cash flow (10,454), availability 10,014, customers 36%, 26% and 10%, voting 66.9% | None | None | None |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Duplication | Covenant, guarantor and financing-document limitations are restated in each module; each restatement changes a distinct conclusion, so none is removed | None | None |
| MINOR | CP-2 | Materiality | The credit view rests on the financial base for leverage and liquidity and on the business context for contracted revenue; no immaterial claim is carried | None | None |
| MINOR | All | Committee readiness | The set is traceable and internally consistent; committee use is restricted until covenant levels, financing documents, guarantors and the third quarter 2026 report are added | Obtain them | Restricted use |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Reader summary table | The first submission had a 31-word finding cell against a 30-word limit; it was rejected and the second submission passed | None; resolved | None |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Required headings, sources, handoff hashes and view sections | No defect found: all name the issuer and as-of date, list the seven sources with hashes and list upstream handoffs with hashes | None | None |
| MINOR | CP-1, CP-1A | Selectors | Chart tables, metrics table, company and profile tables and prose selectors are each present once | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MINOR | CP-0 | Unsupported claim | Cash income taxes stated as Not supplied for all periods; FY2025 is printed | Read with CP-1 gap 3 | Formatting and hygiene only | Resolved downstream |
| CP5-002 | MINOR | CP-1 | Context omitted | Revolver repayment shown against the December 2025 balance of 1,000, not the March 2026 balance of 1,500 | Restate with the March 2026 balance | Does not block committee use | Open |
| CP5-003 | MINOR | CP-1 | Unquantified qualifier | Principal debt described as mostly secured; about half by principal | Restate as about half | Does not block committee use | Open |
| CP5-004 | MINOR | CP-1A | Unsupported timing | Preferred dividends described as paid before the IPO conversion; a 3 payment is printed for Q2 2025 | Remove the timing remark | Does not block committee use | Open |
| CP5-005 | MINOR | CP-1A, CP-2 | Definition and date | Committed share of revenue lacks its definition; contract duration lacks its date in CP-2 | Add the definition and date | Does not block committee use | Open |

#### T5B.1 Source document register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_crwv-20251231.htm.jsonl | Audited filing | FY2025 with FY2024 and FY2023 | CoreWeave, Inc. consolidated | Statements, debt, leases, customers, voting, risk factors | Text extraction; flattened tables | Financial base, business context |
| S2 | 10-Q_2025-09-30_crwv-20250930.htm.jsonl | Unaudited filing | Q3 2025 and nine months 2025 | CoreWeave, Inc. consolidated | Q3 2025 revenue in thousands | Units in thousands | Revenue cross-check only |
| S3 | 10-Q_2026-03-31_crwv-20260331.htm.jsonl | Unaudited filing | Q1 2026 | CoreWeave, Inc. consolidated | Statements, debt, liquidity, leases | Text extraction | Financial base |
| S4 | 10-Q_2026-06-30_crwv-20260630.htm.jsonl | Unaudited filing | Q2 2026 and six months 2026 | CoreWeave, Inc. consolidated | Statements, debt note, commitments, risk factors, subsequent events | Cash flow statement for six months only | All modules |
| S5 | EX-99.1_2026-02-26_coreweave4q25earningspress.htm.jsonl | Management release | Q4 2025 and FY2025 | CoreWeave, Inc. | Adjusted EBITDA reconciliation, backlog | Non-GAAP, attributed | Financial base |
| S6 | EX-99.1_2026-05-07_coreweave1q26earningspress.htm.jsonl | Management release | Q1 2026 | CoreWeave, Inc. | Adjusted EBITDA reconciliation | Non-GAAP, attributed | Financial base |
| S7 | EX-99.1_2026-08-11_coreweave2q26earningspress.htm.jsonl | Management release | Q2 2026 and six months 2026 | CoreWeave, Inc. | Adjusted EBITDA reconciliation, discrete Q2 2026 cash flow, power and backlog statements | Non-GAAP, attributed; no guidance | Financial base, business context |

#### T5B.2 Top credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage and funding dependence | CP-1, CP-2 | Principal debt of USD 35,551 million, LTM adjusted EBITDA of USD 4,400 million, free cash flow of USD (10,454) million for six months 2026 | Debt grows faster than earnings and is funded externally | Sets default and refinancing risk | S4 pages 5, 8, 27; S5 and S7 reconciliation pages |
| 2 | Liquidity and maturities | CP-1, CP-2 | Availability USD 10,014 million, cash USD 5,524 million, USD 4,413 million due in the remainder of 2026 | Availability is conditional on asset purchases | Sets near-term refinancing need | S4 pages 27, 31, 53, 133 |
| 3 | Contracted revenue and delivery | CP-1A, CP-2 | Remaining performance obligations of USD 103.7 billion, committed contracts, undelivered power | Visibility depends on delivery | Supports debt service | S4 pages 14, 15, 24 |
| 4 | Customer concentration | CP-1A, CP-2 | Customers at 36%, 26% and 10% of Q2 2026 revenue | A few counterparties carry cash conversion | Drives loss severity on asset-level debt | S4 pages 14, 15, 72 |
| 5 | Structure, control and obligations outside debt | CP-1, CP-1A | Recourse and non-recourse split, unsecured notes, founder voting, USD 16,319 million of operating leases and USD 35.5 billion of leases not commenced | Claims and control sit outside the debt figure | Limits recovery mechanics analysis | S4 pages 23, 24, 27, 134, 141 |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt 35,551 and its instrument table | CP-1 | S4 pages 26, 27 | Yes | Filed note | Directly Sourced | Supported | High | Traced and re-read |
| LTM adjusted EBITDA 4,400 | CP-1 | S5, S7 reconciliation tables | Yes | Management non-GAAP | Calculated | Supported | Medium | Traced; definition is the company's |
| Leverage 8.08x and 6.82x; cover 3.35x | CP-1 | Reperformed from printed inputs | Yes | Calculated | Calculated | Supported | Medium | Reproduced |
| Free cash flow (10,454) | CP-1 | S4 page 8 | Yes | Filed statement | Calculated | Supported | High | Reproduced |
| Availability 10,014 and its rebuild | CP-1 | S4 pages 31, 53, 57, 133 and S1 page 177 | Yes | Filed notes | Calculated | Supported | Medium | Reproduced exactly |
| Maturity schedule | CP-1 | S4 page 27 | Yes | Filed note | Directly Sourced | Supported | High | Sums to total |
| Claims outside debt | CP-1 | S4 pages 16, 22, 23, 24, 25 | Yes | Filed notes | Directly Sourced | Supported | High | Traced |
| Revenue model and remaining performance obligations | CP-1A | S1 page 8; S4 pages 14, 15 | Yes | Filed | Directly Sourced | Partially supported (definition and date) | High | Traced; see CP5-005 |
| Customer shares and commitments | CP-1A | S4 pages 14, 72, 98; S1 page 32 | Yes | Filed | Directly Sourced | Supported | High | Traced |
| Founder voting weight 66.9% | CP-1A | S4 page 1; S1 page 2 | Yes | Share counts | Analyst Inference | Supported as a calculation | Medium | Reproduced; not a company-disclosed figure |
| Parent notes unsecured, delayed-draw secured | CP-1A | S4 pages 29, 30, 34, 134 | Yes | Filing summary | Directly Sourced | Supported | Medium | Agreements not supplied |
| Credit view: high risk | CP-2 | CP-1 and CP-1A rows | Yes | Upstream | Analyst Inference | Supported by cited basis | Medium | Traced to handoffs |

#### T5B.4 Statement lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt 35,551 | source-text | 10-Q_2026-06-30 | S4 | page:27 | CP-1 maturities | Direct | Filed | Schedule total |
| Recourse debt non-current 25,170 | source-text | 10-Q_2026-06-30 | S4 | page:5 | CP-1 register | Direct | Filed | Balance sheet |
| Cash paid for interest 806 | source-text | 10-Q_2026-06-30 | S4 | page:9 | CP-1 cover | Direct | Filed | Six months 2026 |
| Purchase of property and equipment (14,117) | source-text | 10-Q_2026-06-30 | S4 | page:8 | CP-1 free cash flow | Direct | Filed | Six months 2026 |
| Total liquidity 15,553 | source-text | 10-Q_2026-06-30 | S4 | page:53 | CP-1 liquidity | Direct | Filed | Company table |
| Undrawn availability facilities named | source-text | 10-Q_2026-06-30 | S4 | page:133 | CP-1 liquidity | Direct | Filed | Risk factor |
| Operating leases 29,135 undiscounted | source-text | 10-Q_2026-06-30 | S4 | page:23 | CP-1 claims | Direct | Filed | Lease note |
| Leases not commenced 35.5 billion | source-text | 10-Q_2026-06-30 | S4 | page:24 | CP-1 claims | Direct | Filed | Lease note |
| Adjusted EBITDA 3,093 for FY2025 | source-text | EX-99.1_2026-02-26 | S5 | page:7 | CP-1 EBITDA | Direct | Management | Reconciliation |
| Adjusted EBITDA 2,667 six months 2026 | source-text | EX-99.1_2026-08-11 | S7 | page:7 | CP-1 EBITDA | Direct | Management | Reconciliation |
| Remaining performance obligations 103.7 billion | source-text | 10-Q_2026-06-30 | S4 | page:15 | CP-1A revenue model | Direct | Filed | Revenue note |
| Class B ten votes, held by founders | source-text | 10-Q_2026-06-30 | S4 | page:141 | CP-1A governance | Direct | Filed | Risk factor |
| FY2025 cash income taxes (1) | source-text | 10-K_2025-12-31 | S1 | page:196 | CP-1 gaps | Direct | Audited filing | Corrects CP-0 |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM revenue 7,590 | CP-1, CP-2 | 5,131; 4,653; 2,194 | FY2025 plus six months 2026 less six months 2025 | Reproduced (also equals four discrete quarters, Q3 2025 rescaled) | Supported | High | Scale and margin base | S1 page 138; S4 page 6; S2 page 6 |
| LTM adjusted EBITDA 4,400 | CP-1, CP-2 | 3,093; 2,667; 1,360 | Same | Reproduced | Supported | Medium | Leverage and cover denominator | S5, S7 page 7 |
| Total debt / EBITDA 8.08x; net 6.82x | CP-1, CP-2 | 35,551; 30,012; 4,400 | Principal over LTM adjusted EBITDA | Reproduced | Supported | Medium | Leverage | S4 pages 5, 27 |
| Net debt 30,012 | CP-1 | 35,551; 5,524; 15 | Principal less cash and marketable securities | Reproduced | Supported | High | Leverage | S4 page 5 |
| EBITDA / cash interest 3.35x | CP-1, CP-2 | 4,400; 1,313 (869 + 806 - 362) | Ratio | Reproduced | Supported | Medium | Coverage | S1 page 141; S4 page 9 |
| Free cash flow (10,454), (13,655) | CP-1, CP-2 | 3,663; 14,117; LTM inputs | Operating cash flow less purchase of property and equipment | Reproduced | Supported | High | Cash conversion | S4 page 8; S1 page 140 |
| Availability rebuild 10,014 | CP-1, CP-2 | 2,500; 533; 2,600; 2,215; 8,500; 2,837; 3,100; 1,101 | Sum of facility size less outstanding and letters of credit | Reproduced exactly | Supported | Medium | Liquidity | S4 pages 26 to 31, 57, 133 |
| Maturity schedule sum 35,551 | CP-1 | Six annual amounts | Sum | Reproduced | Supported | High | Refinancing | S4 page 27 |
| Recourse share 89.5% | CP-1 | 31,832; 3,719; 35,551 | Recourse principal over total | Reproduced | Supported | High | Structure | S4 pages 26, 27 |
| Founder voting weight 66.9% | CP-1A, CP-2 | 92,664,912 Class B; 458,871,690 Class A | Class B votes over total votes | Reproduced; assumes cover-page counts | Supported as a calculation | Medium | Control | S4 page 1 |
| Secured share of debt (new) | CP5 | 13,643; 5,102; 35,551 | Secured delayed-draw and OEM principal over total | About 52.7%; assumes all OEM financing is secured | Analyst inference | Low | Tests the "mostly secured" remark | S4 pages 26, 27 |
| Adjusted EBITDA definition | CP-1 | Company reconciliation | Adds back stock compensation and acquisition costs | Company definition, not a lender definition | Management measure | Medium | Leverage covenant mismatch risk | S5, S7 page 7 |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | Principal debt is mostly secured | No source states a secured share | Weak Lineage | Affects the structure narrative | Quantify or restate | CP-1 base view (CP5-003) |
| MINOR | Founders hold about two thirds of votes | Derived from cover-page counts, not disclosed; founders also hold some Class A | Analyst Inference | Control assessment | Keep labelled as calculated | CP-1A, CP-2 |
| MINOR | The April 2026 placement may be the Jane Street investment | The 10-Q does not name the purchaser | Analyst Inference | Equity-support attribution | Keep the link unstated | CP-1A |
| MINOR | Sector label Services-Prepackaged Software | From the run context, external to the filings | Weak Lineage | Descriptive only | Keep labelled external | CP-1A |
| MINOR | Monolith notes of 185 less 13 equal the 172 promissory notes | Inference; the 10-Q does not name the acquiree | Analyst Inference | Tracks a settled debt item | Keep labelled | CP-1A |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Locators and quotes | Strong | All register quotes in CP-0, CP-1 and CP-1A matched their cited pages (no mismatch after review) | A wrong page would break a reader's check | Figures can be re-found | None |
| Calculations | Strong | Every derived figure shown with inputs and reproduced | Hidden arithmetic would hide errors | Leverage and liquidity can be re-run | None |
| Conflicts | Adequate | Four conflicts logged and left unreconciled | Smoothing would hide definition differences | Backlog and dates carry two values | None |
| Subsequent events | Adequate | August 2026 items labelled and kept out of June 30 figures | Blending would misstate liquidity | As-of date liquidity is Not calculable | Add the third quarter 2026 report |
| Units and periods | Strong | Q3 2025 file rescaled and used only for a cross-check; periods labelled | Mixed units would distort trends | None | None |
| Legal and covenant lineage | Weak | Documents not supplied | Summaries may omit carve-outs and baskets | Headroom and ranking untestable | Obtain agreements |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant levels, definitions and headroom | Credit agreements and compliance certificates | Maintenance tests decide acceleration and funding stops | Headroom Not calculable | Confidence capped at Medium | Credit agreements |
| G2 | Guarantors and ranking | Indentures, guarantee and pledge agreements, guarantor list | Sets claims on assets and cash flows | Recovery mechanics untestable | Confidence capped at Medium | Exhibits listed in the 10-Q |
| G3 | Third quarter 2026 results and as-of date balances | Third quarter 2026 report and later filings | August 2026 draws changed availability | Liquidity at the as-of date Not calculable | Lowers confidence | SEC filings after 2026-08-12 |
| G4 | Management guidance | Call transcript and presentation | Forward cash flow view | No forecast | Neutral | Earnings call |
| G5 | Customer contract terms and top-customer identity | Contracts or summaries | Backlog quality and concentration | Durability judged on aggregates | Lowers confidence | Company disclosure |
| G6 | Ownership percentages, ratings | Proxy statement, rating reports | Control and pricing context | Control inferred from share counts | Neutral | Proxy statement |
| G7 | Interim cash income taxes | Interim tax disclosures | Cash conversion | FY2025 only | Neutral | Interim filings |

## Calculations

Reperformance of the handoffs' derived figures from printed inputs. All amounts are USD millions unless stated. All 36 inputs listed were re-read in the sources and matched.

| Check | Inputs and formula | Result | Handoff value | Status |
| --- | --- | --- | --- | --- |
| LTM revenue | 5,131 + 4,653 - 2,194 | 7,590 | 7,590 | Agrees |
| Revenue from four discrete quarters | Q3 2025 revenue of 1,364,676 thousand rescaled to 1,365, + 1,572 + 2,078 + 2,575 | 7,590 | 7,590 | Agrees |
| LTM adjusted EBITDA | 3,093 + 2,667 - 1,360 | 4,400 | 4,400 | Agrees |
| LTM cash interest | 869 + 806 - 362 | 1,313 | 1,313 | Agrees |
| Gross leverage | 35,551 / 4,400 | 8.08x | 8.08x | Agrees |
| Net debt | 35,551 - 5,524 - 15 | 30,012 | 30,012 | Agrees |
| Net leverage | 30,012 / 4,400 | 6.82x | 6.82x | Agrees |
| Cash interest cover | 4,400 / 1,313 | 3.35x | 3.35x | Agrees |
| Free cash flow six months 2026 | 3,663 - 14,117 | (10,454) | (10,454) | Agrees |
| Free cash flow FY2025 | 3,058 - 10,309 | (7,251) | (7,251) | Agrees |
| Free cash flow LTM | 6,911 - 20,566, with 6,911 = 3,058 + 3,663 + 190 and 20,566 = 10,309 + 14,117 - 3,860 | (13,655) | (13,655) | Agrees |
| Availability rebuild | (2,500 - 533) + (2,600 - 2,215) + (8,500 - 2,837) + (3,100 - 1,101) | 10,014 | 10,014 | Agrees |
| Total liquidity | 5,524 + 15 + 10,014 | 15,553 | 15,553 | Agrees |
| Maturity schedule | 4,413 + 6,184 + 4,416 + 2,421 + 3,221 + 14,896 | 35,551 | 35,551 | Agrees |
| Principal from recourse and non-recourse | 31,405 + 427 + 2,837 + 882 | 35,551 | 35,551 | Agrees |
| Recourse share | 31,832 / 35,551 | 89.5% | 89.5% | Agrees |
| Founder voting weight | 926,649,120 / (926,649,120 + 458,871,690) | 66.9% | 66.9% | Agrees |
| Secured share (new, for CP5-003) | (1,300 + 3,190 + 3,000 + 2,215 + 1,101 + 2,837 + 4,220 + 882) / 35,551 = 18,745 / 35,551 | About 52.7% | "Mostly secured" | Overstated; see CP5-003 |
| Confidence score | Script: (0.6 x 80 + 0.4 x 100) x 0.7 - 15 for five minor findings, source gate partial, 23 material claims (10 directly sourced, 8 calculated, 3 analyst inference, 2 insufficient information) | 47, band Low | 47 | Computed by the canon script |

Review status: qa_status Passed (no critical or material finding; five minor findings); Confidence Score 47 of 100, band Low, driven by the partial source gate (financing documents not supplied) and not by trace defects; committee_status Restricted until the gaps below are closed.

## Gaps

1. The five minor issues in the consolidated issue log are open except the first, which CP-1 already corrected; none changes a credit conclusion.
2. Legal and covenant claims trace only to filing summaries: covenant levels, indentures, credit agreements and guarantor lists are Not supplied.
3. Third quarter 2026 results and balances at the as-of date are Not calculable; August 2026 draws are labelled subsequent events only.
4. Table fidelity was not separately reviewed: sources are text extractions, so a mis-parsed table cell would pass a quote match if the quote were taken from the same flattened text. Key figures were additionally cross-checked between filings and releases (for example six months 2026 revenue and cash flow agree between the Q2 10-Q and release).
5. External material: none outside the pinned sources was used in this review.

## Next module

This is the last module in the minimum set, so the next step is publication. Before committee use, a second reviewer should:

1. Obtain the credit agreements, indentures, guarantor list and the third quarter 2026 report, and rerun the covenant, ranking and liquidity sections.
2. Apply the five minor wording fixes, starting with the revolver repayment amount, the secured share and the contract-duration date.
3. Keep the four logged conflicts open and the Management Language tags on release statements.
