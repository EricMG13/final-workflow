## Request

This is the evidence trace and research integrity review for CONSTELLIUM SE (cstm) as of 2026-11-05, pathway credit_snapshot, run cstm-2026-11-05-credit_snapshot-host. It tests whether the source readiness, financial base, business context and credit synthesis handoffs trace to the pinned filings and agree with each other, at the default Top 5 driver scope plus the full issue lanes.

## Sources

### Issuer sources used for re-verification

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_cstm-20251231.htm.jsonl | 288710d87622fdc4221b04fe663b54006fefe681affd88d991e0c62a7fae557e |
| 10-Q_2026-03-31_cstm-20260331.htm.jsonl | f508cc04bb1d5022d897f65511fba2be0b07f2bdaa8a5cc617f164926ff68332 |
| 10-Q_2026-06-30_cstm-20260630.htm.jsonl | 76cf731f2bbd1f819dbd7897e17733bda76f7874b9476e07730ab0699fd6efb3 |
| 10-Q_2026-09-30_cstm-20260930.htm.jsonl | 1b8ca1fa48ee252c4860c88dfca118c5a65ba8e96003e3543924c42bf0d5a6cc |
| EX-99.1_2026-04-29_a2026-q1xearningspressre.htm.jsonl | e6abca1d5a467da9a078ef479a04052c0f179037d4c463a045159ca23884f80e |
| EX-99.1_2026-07-29_a2026-q2xearningspressre.htm.jsonl | e63d9d2c8751c74a8e5dada7565bb132595b18bca9ad9c4ef12f98be9c09a4ae |
| EX-99.1_2026-10-28_a2026-q3xearningspressre.htm.jsonl | 6f8f81f1120f3b29fefca592a7a8bc48697b73e3a95ba4114c430951126fc70a |

Context (user settings, not issuer evidence): sha256 d8ee79011dd587819ea89f0119056a42b6a9a7490b73bd4082709f4e37cfea92. Blank context fields are unknown, not zero.

### Handoffs audited

| Module | sha256 | How it was used |
| --- | --- | --- |
| CP-0 | e448de069eb7c811e3b2a2cfd9bc5a9082f5527e833a6cdf53464bc5bafe5bb4 | Opened and audited: source identity, readiness and gap statements. |
| CP-1 | 0be39b719ef3e1ad43f3001b21e072ad911c3e441b42c3067a440ada26b88568 | Opened and audited: every figure and chart table recomputed from the cited statements. |
| CP-1A | 96d690230ddab7f652a1700962c5d908397d38400cb598136c3a4e909782a343 | Opened and audited: business and transaction facts re-opened at their locators. |
| CP-2 | 88053d74cf5304d750fbdff7bf6c6c534651632fde82acc998af36ee41249c94 | Opened and audited: every figure matched to CP-1 or CP-1A, every claim matched to its basis. |

### Scope of re-verification

For this review I re-opened the cited pages for the inputs of the five material drivers and for the figures in the registers: the Q3 2026 10-Q pages for the debt table, balance sheet, cash flow, segment tables, Adjusted EBITDA reconciliation and liquidity; the FY2025 10-K pages for the income statement, cash flow, Adjusted EBITDA, debt note, maturity ladder, customers and suppliers; and the Q3 2026 earnings release pages for net debt, leverage and guidance. Pages not named in a locator were not individually re-read. Retrieval of the original HTML was not performed, so extraction fidelity was not reviewed.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The four upstream handoffs trace to the filed sources and agree with each other on every figure checked. Committee use is restricted by the absence of legal documents, ownership and ratings, not by any unsupported figure. | High | Covenant, guarantee and amendment statements rest on filing descriptions, not executed documents, and the trace covers five material drivers rather than every sentence. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Five material drivers were traced: two are directly sourced and three are calculated from filed figures; none is untraced. | Provenance supports the leverage, liquidity, maturity and customer concentration conclusions. | High |
| Recomputed last-twelve-months earnings, leverage, interest cover and liquidity figures reproduce the upstream values. | Figures such as 1.56x net leverage and 10.65x interest cover can be relied on as stated. | High |
| Covenant, guarantee and facility amendment statements rest on report descriptions, not on indentures or credit agreements. | Legal-structure conclusions need legal review before committee use. | Medium |
| Net debt and the 1.6x leverage appear in management releases and were recomputed from filed figures. | Treat the company's leverage as a management figure; the recomputed 1.56x is the reference. | Medium |
| Twelve provenance issues were logged: no Critical, three Material and nine Minor. | None changes a credit conclusion, but three must be cleared before legal-structure conclusions are used. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 3 are calculated, 0 are assumption-based, 0 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the indentures, credit agreements and the October 22, 2026 facility amendment, which matters because covenant headroom, guarantor perimeter and distribution capacity determine creditor protection, and it implies that committee use of any legal-structure conclusion is restricted until those documents are read. Financial figures, by contrast, reproduce from the filed statements, and the upstream modules state their own limits consistently. Committee status: Restricted for legal-structure and ownership conclusions; Draft Only is not needed for the financial base.

### Auditability and clearance

The auditability assessment is the lowest of five dimensions: source coverage is Ready with Remediation, citation completeness is Committee-Ready for the financial base, calculation traceability is Committee-Ready, assumption transparency is Committee-Ready, and Markdown artifact integrity is Ready with Remediation (see the registers). Overall: Ready with Remediation. Clearance decision: committee use permitted for the financial base, leverage, liquidity, maturity and business risk conclusions; restricted for covenant headroom, guarantor, ownership and distribution capacity conclusions. The confidence score is script-owned and was not computed in this transport; it is Not calculable here, and the status above is set by the severity counts (no Critical issue, three Material).

### Remediation priority map

Must-fix before committee: CP5-001 (obtain indentures and credit agreements), CP5-002 (obtain the amendment exhibit). Must-fix before the handoffs are consumed downstream: CP5-003 (label the last-twelve-months comparability caveat where the ratios are quoted). Monitoring follow-up: CP5-004, CP5-005, CP5-007, CP5-008, CP5-009. Formatting and hygiene: CP5-006, CP5-010, CP5-011, CP5-012. These are remediation instructions only; no upstream analysis is rewritten here.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_cstm-20251231.htm | High: audited annual report | FY2025 with FY2024 and FY2023 comparatives | Constellium SE and subsidiaries, consolidated | Statements, notes, debt note, leases, customers, suppliers, risk factors | Items 10 to 14 incorporated from a proxy statement not supplied | Annual base for CP-1, business facts for CP-1A |
| S2 | 10-Q_2026-03-31_cstm-20260331.htm | High: unaudited filed interim report | Q1 2026 | Same consolidated group | Statements, debt note, liquidity | Unaudited | Liquidity series, covenant compliance statement |
| S3 | 10-Q_2026-06-30_cstm-20260630.htm | High: unaudited filed interim report | Q2 2026 and first half | Same consolidated group | Statements, debt note, liquidity, subsequent event | Unaudited | Liquidity series, note redemption event |
| S4 | 10-Q_2026-09-30_cstm-20260930.htm | High: unaudited filed interim report | Q3 2026 and nine months | Same consolidated group | Statements, segments, debt table, factoring, liquidity, subsequent events, buyback table, exhibit list | Unaudited; exhibits themselves not in the pack | Current-period base for all modules |
| S5 | EX-99.1_2026-04-29_a2026-q1xearningspressre.htm | Medium: management release | Q1 2026 | Constellium SE group | Leverage, net debt, Adjusted EBITDA reconciliation | Management non-GAAP measures | Reported leverage series |
| S6 | EX-99.1_2026-07-29_a2026-q2xearningspressre.htm | Medium: management release | Q2 2026 and first half | Constellium SE group | Leverage, net debt, guidance | Management non-GAAP measures | Reported leverage series |
| S7 | EX-99.1_2026-10-28_a2026-q3xearningspressre.htm | Medium: management release | Q3 2026 and nine months | Constellium SE group | Net debt, leverage definition, free cash flow, guidance, amendment notice | Management non-GAAP measures | Reported leverage, guidance |
| S8 | context (1563411-constellium-se-cstm.json) | User settings, not issuer evidence | As of 2026-11-05 | Not issuer-specific evidence | Periods, currency, blank ratings and market fields | Blank fields are unknown, not zero | Scope only |

Module Status: Ready with Limitations (all four handoffs available; legal documents, ownership and ratings absent). Traceability Scope: Top 5. Entity-key status: issuer_id cstm available. Missing required inputs: indentures, credit agreements, the amendment exhibit, the proxy statement.

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Net leverage of 1.56x on Adjusted EBITDA excluding metal price lag at September 30, 2026, down from 2.53x at FY2025 | CP-1 | Debt 1,817 and cash 158 against LTM earnings excluding lag 1,065 | Leverage sets debt capacity and refinancing room | Core input to default risk and tolerance | S4 page:15, 4, 9, 41; S1 page:67, 94, 107 | Management-defined EBITDA basis; no covenant definition supplied |
| 2 | Earnings quality: metal price lag 222 of 1,074 of nine-month Adjusted EBITDA as reported | CP-1, CP-2 | Reconciliation shows lag inside reported Adjusted EBITDA | Non-cash lag inflates reported earnings when prices rise and absorbs cash in working capital | Reading leverage on the reported basis understates risk | S4 page:41; S7 page:6 | Lag is a management calculation |
| 3 | Total liquidity of 992, of which cash plus committed undrawn facilities is 813 | CP-1, CP-2 | Components 158, 541, 179, 114 in the liquidity paragraph | Liquidity is the first defense in a downturn and in a refinancing delay | Near-term default risk | S4 page:38 | ABL availability definition not supplied; amendment after quarter-end not reflected |
| 4 | 2029 maturities of 841 and 2032 maturities of 691 at coupons below the 2024 issues | CP-1, CP-2 | Face values and coupons in the debt table | Refinancing at higher coupons would raise interest cost | Refinancing risk | S4 page:15; S1 page:109 | Face values derived from the table; euro notes at printed dollar face |
| 5 | Customer concentration: 10 largest customers approximately 56% of FY2025 revenue | CP-1A, CP-2 | Statement in Item 1 and risk factor | Revenue visibility and pricing power depend on a few accounts | Business risk | S1 page:13, 30 | Customer names and per-customer shares not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net leverage 1.56x | CP-1 | Total debt 1,812 (16) 21 1,817; cash 158; Segment Adjusted EBITDA 852 and 507; FY2025 720 | Yes | High | Calculated | Supported | High | Committee-Ready |
| Metal price lag share of Adjusted EBITDA | CP-1, CP-2 | Adjusted EBITDA 1,074 and lag 222 in the reconciliation | Yes | High | Calculated | Supported | High | Committee-Ready |
| Total liquidity 992 | CP-1, CP-2 | At September 30, 2026, we had $992 million of total liquidity | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| 2029 maturities 841 | CP-1, CP-2 | Notes of 500 and 341 due 2029 in the debt table | Yes | High | Calculated | Supported | Medium | Committee-Ready |
| Customer concentration 56% | CP-1A, CP-2 | 10 largest customers representing approximately 56% of our revenue | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Covenant and guarantee protections | CP-1, CP-1A, CP-2 | Springing covenant text and compliance statements | Yes | Medium: descriptions of agreements | Insufficient Information | Partially Supported | Low | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt of 1,817 at September 30, 2026 | /workspace/secdata/data/2026-11-05/packs/1563411-constellium-se-cstm | 10-Q_2026-09-30_cstm-20260930.htm | S4 | page:15, Note 11 | CP-1 Financials and credit metrics | Sourced | High | Carrying value including accrued interest and net of issuance costs |
| Cash of 158 at September 30, 2026 | same pack folder | 10-Q_2026-09-30_cstm-20260930.htm | S4 | page:4, balance sheet | CP-1 Financials and credit metrics | Sourced | High | None |
| Adjusted EBITDA 1,074 and lag 222 for nine months 2026 | same pack folder | 10-Q_2026-09-30_cstm-20260930.htm | S4 | page:41, Item 2 reconciliation | CP-1 table; CP-2 key findings | Sourced | High | Non-GAAP |
| Adjusted EBITDA 846 and lag 126 for FY2025 | same pack folder | 10-K_2025-12-31_cstm-20251231.htm | S1 | page:67, Item 7 reconciliation | CP-1 table | Sourced | High | Non-GAAP |
| Segment Adjusted EBITDA 339, 353, 72 and -44 for FY2025 | same pack folder | 10-K_2025-12-31_cstm-20251231.htm | S1 | page:94, Note 3 | CP-1 segment base | Sourced | High | Includes the revision of A&T figures |
| Interest paid 104 for FY2025, 79 and 83 for the nine months | same pack folder | 10-K_2025-12-31_cstm-20251231.htm; 10-Q_2026-09-30_cstm-20260930.htm | S1, S4 | page:79; page:5 | CP-1 interest cover | Sourced | High | Cash flow line |
| Liquidity components 158, 541, 179 and 114 | same pack folder | 10-Q_2026-09-30_cstm-20260930.htm | S4 | page:38, Item 2 liquidity | CP-1 liquidity chart | Sourced | High | Factoring availability not described as committed |
| Notes due 2028, 2029 and 2032 with rates and dates | same pack folder | 10-Q_2026-09-30_cstm-20260930.htm; 10-K_2025-12-31_cstm-20251231.htm | S4, S1 | page:15; page:109 | CP-1 debt structure | Sourced | High | Maturity dates from the annual report |
| Springing fixed charge coverage covenant | same pack folder | 10-K_2025-12-31_cstm-20251231.htm | S1 | page:108, Note 15.1 | CP-1 covenants | Sourced | Medium | Description, not the executed agreement |
| Amendment of October 22, 2026 raising commitments from 550 to 700 | same pack folder | 10-Q_2026-09-30_cstm-20260930.htm; EX-99.1_2026-10-28_a2026-q3xearningspressre.htm | S4, S7 | page:23; page:8 | CP-1, CP-1A, CP-2 subsequent events | Sourced | Medium | One-sentence disclosure |
| 10 largest customers approximately 56% of revenue | same pack folder | 10-K_2025-12-31_cstm-20251231.htm | S1 | page:13, Item 1 | CP-1A operating model | Sourced | High | None |
| Top 10 suppliers approximately 49% of metal purchases | same pack folder | 10-K_2025-12-31_cstm-20251231.htm | S1 | page:12, Item 1 | CP-1A operating model | Sourced | High | None |
| Net debt 1,658 and leverage 1.6x | same pack folder | EX-99.1_2026-10-28_a2026-q3xearningspressre.htm | S7 | page:7, 1 | CP-1 chart note | Sourced | Medium | Management release; recomputed in CP-1 |
| Share repurchase program of up to 300 with about 257 remaining | same pack folder | 10-Q_2026-09-30_cstm-20260930.htm | S4 | page:43, Part II Item 2 | CP-1A transaction summary; CP-2 | Sourced | High | None |
| Ravenswood Salaried Pension Plan settlement | same pack folder | 10-Q_2026-09-30_cstm-20260930.htm | S4 | page:20, Note 13 | CP-1A transaction summary | Sourced | High | Not carried into CP-1 pension comparison |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA excluding lag, period to September 30, 2026 | CP-1 chart and table; CP-2 | 846, 126, 1,074, 222, 566, 59 | (846 - 126) + (1,074 - 222) - (566 - 59) = 720 + 852 - 507 = 1,065 | Calculated | Supported | High | PD, leverage | S1 page:67; S4 page:41 |
| Net debt / EBITDA excluding lag, LTM Q3 2026 | CP-1, CP-1A, CP-2 | Debt 1,817, cash 158, EBITDA 1,065 | (1,817 - 158) / 1,065 = 1,659 / 1,065 = 1.56x | Calculated | Supported | High | Leverage tolerance | S4 page:15, 4 |
| Total debt / EBITDA excluding lag, LTM Q3 2026 | CP-1, CP-2 | Same | 1,817 / 1,065 = 1.71x | Calculated | Supported | High | Leverage | S4 page:15 |
| Net debt / EBITDA excluding lag, FY2025 | CP-1, CP-2 | Debt 1,944, cash 120, EBITDA 720 | (1,944 - 120) / 720 = 2.53x | Calculated | Supported | High | Leverage trend | S1 page:107, 77 |
| EBITDA excluding lag / cash interest, LTM Q3 2026 | CP-1, CP-2 | 1,065 and interest paid 104 + 79 - 83 = 100 | 1,065 / 100 = 10.65x | Calculated | Supported | High | Debt service | S1 page:79; S4 page:5 |
| EBITDA excluding lag / cash interest, FY2025 | CP-1, CP-2 | 720 and 104 | 720 / 104 = 6.92x | Calculated | Supported | High | Debt service | S1 page:79, 67 |
| LTM free cash flow | CP-1 | Cash from operations 489, 420, 271; net capex 311, 197, 203 | (489 + 420 - 271) - (311 + 197 - 203) = 638 - 305 = 333 | Calculated | Supported | High | Cash conversion | S1 page:79; S4 page:6 |
| Cash plus committed undrawn facilities | CP-1, CP-2 | 158, 541, 114 | 158 + 541 + 114 = 813 | Calculated | Supported | Medium | Liquidity | S4 page:38 |
| Maturity shares of face value | CP-2 | 225, 841, 691 of 1,812 | 841 / 1,812 = 46.4%; 691 / 1,812 = 38.1% | Calculated | Supported | High | Refinancing | S4 page:15 |
| Metal price lag share of reported Adjusted EBITDA | CP-1, CP-2 | 222 and 1,074 | 222 / 1,074 = 20.7% | Calculated | Supported | High | Earnings quality | S4 page:41 |
| Working capital lines, nine months 2026 | CP-1, CP-2 | -527, -267, 310, -4 | -527 - 267 + 310 - 4 = -488 | Calculated | Supported | High | Cash conversion | S4 page:5 |
| Debt including factored receivables | CP-1, CP-2 | 1,817, 417, EBITDA 1,065 | (1,817 + 417) / 1,065 = 2.10x | Assumption-Based | Supported as a labeled sensitivity | Medium | Leverage sensitivity | S4 page:14, 15 |

All formulas show numerator, denominator, period and source trace; none required normalization beyond the exclusion of metal price lag, which is labeled in each module.

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Covenant and guarantee protections | Rest on descriptions in the annual and quarterly reports; the executed documents are not in the pack | Insufficient Information | Covenant headroom, guarantor perimeter and structural subordination drive default and loss given default mechanics | Obtain indentures and credit agreements | CP-1 covenants, CP-2 risks, CP-1A governance |
| Material | Effect of the October 22, 2026 facility amendment on liquidity | One-sentence disclosure of commitment size and maturity; availability effect not given | Weak Lineage | Liquidity after the amendment may differ from the 992 reported at September 30, 2026 | Obtain the exhibit to the quarterly report | CP-1 liquidity, CP-2 liquidity finding |
| Minor | Company-reported leverage 1.6x and net debt 1,658 | Management release only; recomputed in CP-1 from filed figures | Calculated | A management measure could differ from covenant definitions | Keep labeled as management measures | CP-1 chart notes, CP-2 |
| Minor | Fixed-rate statement on the senior notes | Omits contingent coupon step-ups on the sustainability-linked notes | Directly Sourced | Interest cost on those notes can rise if a target is missed | Add the step-up caveat when the statement is quoted | CP-2 key findings |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filed documents cover the annual and three quarterly periods; no legal documents or proxy statement | Absent legal documents leave protections untested | Legal-structure conclusions stay restricted | Obtain legal documents and proxy statement |
| Citation completeness | Committee-Ready | Every financial figure in CP-1 carries a page locator that reopened to the stated figure | Missing locators would break lineage | Financial base can be relied on | None |
| Calculation traceability | Committee-Ready | Twenty-one calculations recomputed and matched | Unshown formulas would hide definition drift | Leverage and cover can be relied on as stated | Keep the basis label with each ratio |
| Assumption transparency | Committee-Ready | The only assumption-based figure, debt including factoring, is labeled a sensitivity | An unlabeled adjustment would overstate a company measure | No hidden adjustment found | None |
| Markdown artifact integrity | Ready with Remediation | Handoffs use the CP-OS transport headings rather than the method's front-matter envelope | Downstream consumers read identity from CP-OS | No loss of lineage in this run | Note in the issue log |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Indentures, credit agreements, covenant levels, guarantor list | Executed documents | Protection, headroom and structural position cannot be tested | CP-1 covenants, CP-2 risks | High impact | Issuer filing exhibits |
| CP-5-GAP-002 | October 22, 2026 amendment terms | Amendment No. 8 exhibit | Post-quarter availability, pricing and covenants unknown | CP-1 liquidity, CP-2 | Medium impact | Exhibit 10.1 of the Q3 report |
| CP-5-GAP-003 | Ownership, control rights | Proxy statement | Support or extraction behavior cannot be judged | CP-1A governance, CP-2 | Medium impact | Proxy statement |
| CP-5-GAP-004 | Ratings, prices, peers | Context blank | No market-based view | CP-2 confidence | Medium impact | External source, labeled external |
| CP-5-GAP-005 | Prior-year balances at September 30, 2025 and stand-alone Q4 2025 | Quarterly report for Q3 2025 | LTM windows combine annual and interim data after a revision | CP-1 ratios | Low impact | Q3 2025 quarterly report |
| CP-5-GAP-006 | Letters of credit drawn, lease liabilities and purchase commitments after December 31, 2025 | Facility and lease notes | Claims on liquidity may be understated | CP-1 claims table | Low impact | Issuer notes |
| CP-5-GAP-007 | Page-level coverage of the audit | Pages not named in locators were not re-read | Defects could exist outside traced locators | All modules | Low impact | Full page review |

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | Handoff sha256 e448de069eb7c811e3b2a2cfd9bc5a9082f5527e833a6cdf53464bc5bafe5bb4; run_id cstm-2026-11-05-credit_snapshot-host | Source readiness for four downstream modules | High | Six CP-OS headings present; no YAML envelope in this transport | Accepted by CP-OS structural check | Accepted on second attempt after a word-count correction |
| CP-1 | Handoff sha256 0be39b719ef3e1ad43f3001b21e072ad911c3e441b42c3067a440ada26b88568; same run_id | Financial base, four chart tables, metrics | High | Six CP-OS headings and required selectors present | Accepted by CP-OS structural check | None |
| CP-1A | Handoff sha256 96d690230ddab7f652a1700962c5d908397d38400cb598136c3a4e909782a343; same run_id | Business, ownership and transaction context | High | Six CP-OS headings and required selectors present | Accepted by CP-OS structural check | None |
| CP-2 | Handoff sha256 88053d74cf5304d750fbdff7bf6c6c534651632fde82acc998af36ee41249c94; same run_id | Credit synthesis | Medium: upstream only by design | Six CP-OS headings and required selectors present | Accepted by CP-OS structural check | None |

Module Status: Ready with Limitations.

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Key findings: senior notes carry fixed coupons, so rate moves do not change cash interest on the notes | Partially Supported | The 3.750% and 3.125% notes can step up to 3.875% and 3.275% from 2027 if a recycled-input target is missed (CP-1 debt structure) | Add the step-up caveat | Monitoring follow-up |
| MINOR | CP-2 | Key findings: the July 2026 redemption shows a willingness to retire debt early | Supported | The sentence is analyst interpretation inside a paragraph tagged Documentary Fact; the sources do not state how the redemption was funded | Tag the sentence Analyst Interpretation | Hygiene |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-2 | Last-twelve-months ratios combine the FY2025 annual report with 2026 quarterly comparatives | A revision of A&T metal price lag and Segment Adjusted EBITDA touched 2025 and 2024 periods; the original 2025 interim reports are not supplied, so comparability of the nine-month 2025 comparative cannot be verified | None between sources; limitation only | Keep the caveat wherever LTM ratios are quoted | Must be labeled before downstream consumption |
| MINOR | CP-1 | Net debt 1,659 against the company's 1,658 | The company definition adjusts for a cross-currency swap of 1 | Management release 1,658 against recomputed 1,659 | Keep both figures labeled | Monitoring follow-up |
| MINOR | CP-2 | Reader summary quotes net leverage of 1.56x without naming the basis | Basis (excluding metal price lag) is named in the credit view and CP-1 | None | Name the basis where the ratio is first quoted | Hygiene |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-1A, CP-2 | Springing fixed charge coverage covenant on the asset-based facility, indenture restrictions, 101% change-of-control offer, subsidiary guarantees, security over borrower assets | Executed indentures and the asset-based credit agreement with amendments | Pack holds annual report descriptions only; the covenant level, definitions and guarantor list are absent | Obtain the documents; until then keep each claim labeled a report description | Legal review required before committee use |
| MATERIAL | CP-1, CP-1A, CP-2 | Asset-based facility amendment of October 22, 2026: commitments 550 to 700, maturity October 22, 2031 | Amendment No. 8 (listed as Exhibit 10.1 of the Q3 2026 report) | One-sentence disclosure; exhibit not in the pack | Obtain the exhibit | Legal review required for availability and covenants |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | No relative value, price, spread or rating claim is made; CP-2 compares the 2029 coupons with the 2024 issue coupons only | Ratings, quotes and peer set (context blank) | No market inputs supplied | None; keep market views out of scope | None on the audited claims |

#### T5.6 Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A | CP-1 compares pension and other benefit obligations of 362 at FY2025 with 341 at September 30, 2026 without noting the Q3 2026 settlement of the Ravenswood plan (47 of obligations derecognized, in CP-1A) | CP-1 cannot be edited; CP-1A carries the fact | State the settlement when the comparison is used | Pension movement is not all liability reduction |
| MINOR | CP-0, CP-1A, CP-2 | CP-0 and CP-1 treat the facility amendment terms as Not supplied; CP-1A and CP-2 add that the amending agreement is listed as an exhibit to the Q3 report | Later handoffs refine, not contradict, the earlier wording | Cite CP-1A and CP-2 for the exhibit fact | None on figures |

Checked and consistent across modules: issuer identity and perimeter, USD and US GAAP basis, net leverage 1.56x and 2.53x, total liquidity 992, cash plus committed undrawn 813, maturities 225, 841 and 691, interest cover 10.65x and 6.92x, customer share 56%, segment shares 60% and 49%, and the metal price lag share 20.7%. No covenant capacity, recovery or ranking claim appears in any module.

#### T5.7 Duplication, materiality and committee readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Duplicative content | The same leverage, cover and liquidity figures recur in the reader summary, credit view, key findings and strengths | Keep one full statement and refer back | Low; readability only |

No promotional or generic language was found in the audited modules; claims taken from management are tagged Management Language.

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Envelope and canonical headings | Handoffs use the CP-OS six-heading transport and carry no YAML front-matter envelope, evidence trace or QA validation headings of the method | None needed under CP-OS; identity and lineage are carried by the run record | None; recorded for transparency |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-1, CP-1A, CP-2 | Legal claim without executed source | Covenant, guarantee, indenture and security statements rest on report descriptions (T5.4) | Obtain indentures and credit agreements | Restricts legal-structure conclusions | Open |
| CP5-002 | MATERIAL | CP-1, CP-1A, CP-2 | Legal claim without executed source | Facility amendment terms rest on one sentence (T5.4) | Obtain Exhibit 10.1 | Restricts liquidity-after-amendment conclusion | Open |
| CP5-003 | MATERIAL | CP-1, CP-2 | Comparability limitation | Last-twelve-months ratios combine annual and interim data after a segment revision (T5.3) | Keep the caveat with each LTM ratio | Label before downstream use | Open |
| CP5-004 | MINOR | CP-1 | Management measure | Net debt 1,659 against 1,658 (T5.3) | Keep both labeled | Monitoring | Open |
| CP5-005 | MINOR | CP-2 | Partially supported claim | Fixed-coupon statement omits step-ups (T5.2) | Add the caveat | Monitoring | Open |
| CP5-006 | MINOR | CP-2 | Category tagging | Willingness sentence is analyst interpretation (T5.2) | Retag | Hygiene | Open |
| CP5-007 | MINOR | CP-1, CP-1A | Cross-module context | Pension comparison omits the plan settlement (T5.6) | State the settlement | Monitoring | Open |
| CP5-008 | MINOR | CP-0, CP-1A, CP-2 | Version refinement | Amendment exhibit fact appears only in later handoffs (T5.6) | Cite later handoffs | Monitoring | Open |
| CP5-009 | MINOR | CP-2 | Market input absence | No market or ratings inputs (T5.5) | None; keep out of scope | Monitoring | Open |
| CP5-010 | MINOR | CP-2 | Duplication | Repeated figures across sections (T5.7) | Consolidate | Hygiene | Open |
| CP5-011 | MINOR | CP-0, CP-1, CP-1A, CP-2 | Envelope | CP-OS transport differs from the method envelope (T5.8) | None needed | Hygiene | Open |
| CP5-012 | MINOR | CP-2 | Metric definition | Reader summary quotes 1.56x without its basis (T5.3) | Name the basis | Hygiene | Open |

## Calculations

Independent recomputation from the cited statement figures, each matched to the upstream value. Inputs are US$m unless stated.

| Item | Recomputation | Upstream value | Match |
| --- | --- | --- | --- |
| LTM revenue | 8,449 + 7,848 - 6,248 = 10,049 | 10,049 (CP-1) | Yes |
| LTM Adjusted EBITDA as reported | 846 + 1,074 - 566 = 1,354 | 1,354 (CP-1) | Yes |
| LTM metal price lag | 126 + 222 - 59 = 289 | 289 (CP-1) | Yes |
| LTM EBITDA excluding lag | 1,354 - 289 = 1,065; by segments 720 + 852 - 507 = 1,065 | 1,065 (CP-1) | Yes |
| Net debt FY2025 and September 30, 2026 | 1,944 - 120 = 1,824; 1,817 - 158 = 1,659 | 1,824 and 1,659 (CP-1) | Yes |
| Net debt / EBITDA excluding lag | 1,824 / 720 = 2.53x; 1,659 / 1,065 = 1.56x | 2.53x and 1.56x | Yes |
| Total debt / EBITDA excluding lag | 1,944 / 720 = 2.70x; 1,817 / 1,065 = 1.71x | 2.70x and 1.71x | Yes |
| Net debt / reported Adjusted EBITDA | 1,824 / 846 = 2.16x; 1,659 / 1,354 = 1.23x | 2.16x and 1.23x | Yes |
| Cash interest cover excluding lag | 720 / 104 = 6.92x; 1,065 / 100 = 10.65x | 6.92x and 10.65x | Yes |
| Cash interest cover as reported | 846 / 104 = 8.13x; 1,354 / 100 = 13.54x | 8.13x and 13.54x | Yes |
| LTM free cash flow | 638 - 305 = 333; 178 + 223 - 68 = 333 | 333 (CP-1) | Yes |
| LTM working capital lines | -175 - 488 + 161 = -502 | -502 (CP-1) | Yes |
| Total liquidity by quarter | 120 + 541 + 87 + 118 = 866; 143 + 491 + 155 + 115 = 904; 163 + 541 + 240 + 114 = 1,058; 158 + 541 + 179 + 114 = 992 | 866, 904, 1,058, 992 | Yes |
| Undrawn committed facilities | 541 + 118 = 659; 491 + 115 = 606; 541 + 114 = 655 (twice) | 659, 606, 655, 655 | Yes |
| Face value by maturity | 225 + 841 + 691 + 55 = 1,812 | 1,812 (printed total face value) | Yes |
| Maturity shares | 841 / 1,812 = 46.4%; 691 / 1,812 = 38.1%; 225 / 1,812 = 12.4% | 46.4%, 38.1%, 12.4% (CP-2) | Yes |
| Metal price lag share | 222 / 1,074 = 20.7% | 20.7% | Yes |
| Debt including factored receivables | (1,817 + 417) / 1,065 = 2.10x | 2.10x | Yes |
| Segment shares FY2025 | 5,078 / 8,449 = 60.1%; 353 / 720 = 49.0% | 60% and 49% (CP-1A) | Yes |
| Share count change | 143,523,308 - 134,536,604 = 8,986,704, 6.3% | 8,986,704 and 6.3% (CP-1A) | Yes |
| Cost of sales share | 7,262 / 8,449 = 86.0% | 86% (CP-1A) | Yes |

## Gaps

| Gap | Effect on this review | Action |
| --- | --- | --- |
| Executed indentures, credit agreements and the amendment exhibit | Legal-structure claims can be traced only to descriptions, so they stay restricted | Obtain the documents (CP5-001, CP5-002) |
| Proxy statement and ratings | Ownership and market views are not testable | Obtain the proxy statement; supply ratings externally |
| Original 2025 interim reports | The revised nine-month 2025 comparative cannot be tied to an original | Obtain the Q3 2025 report if the LTM windows are used for covenant work |
| Pages not named in locators and the original HTML | Defects outside the traced pages and extraction errors would not be detected | Run a full page review before committee use |
| Confidence score | Script-owned; not computed in this transport | Compute with the confidence script when the handoff is exported |

## Next module

No further module follows in the selected set. Consumers of the run should read the credit synthesis with the three Material issues in mind: obtain the legal documents and the amendment exhibit before relying on any covenant, guarantor or distribution-capacity conclusion, and quote the last-twelve-months ratios with their basis and comparability caveat.
