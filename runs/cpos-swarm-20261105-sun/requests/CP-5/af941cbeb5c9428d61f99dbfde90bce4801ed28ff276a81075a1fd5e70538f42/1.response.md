## Request

Module CP-5 (evidence trace validator, absorbing the CP-5A research integrity grade) for Sunoco LP (ticker SUN), as of 2026-11-05, pathway credit_snapshot, run sun-2026-11-05-credit_snapshot-host. Scope: Top 5 credit drivers, claim-to-source lineage, locators, calculations, conflicts and handoff consistency across the accepted source-readiness, financial-base, business-context and credit-synthesis handoffs, in USD millions for the consolidated Partnership, current period Q3 2026 and prior period FY2025. This module changes no credit conclusion and silently repairs nothing; where it corrects an earlier locator it says so.

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_sun-20251231.htm.jsonl | 4d533c7220ddbcba5e79429a3e55af6f981f4028bd3240e90c171b5489b87bbb |
| 10-Q_2026-03-31_sun-20260331.htm.jsonl | 4e2f1b55ee8eafcd725aa5897bfa24cca76e00e715174c97a0131e050e960f56 |
| 10-Q_2026-06-30_sun-20260630.htm.jsonl | b55118b081c6aab25bae8900552db80c2175a7fbe9c987d7af0591769205eba8 |
| 10-Q_2026-09-30_sun-20260930.htm.jsonl | 9d81b6ce13f6414e34143a0e003cbfdaa5fb004a754a0331e64ef28cbefb606f |
| EX-99.1_2026-05-05_ex991sunerq12026.htm.jsonl | b543c996b78993ca218c78bb6345ef94cc7c1414aa2f0dc957df2eabc33099ef |
| EX-99.1_2026-08-04_ex991sunerq22026.htm.jsonl | 99167c2338b2c4908c4d210398b4d6c13f7757d59d0f0344be48d8d23d38d4f9 |
| EX-99.1_2026-11-03_ex991sunocoandsunococorper.htm.jsonl | 9cda190739e5a6207ea6c7ec1f929f6d3b9334edb87da0e79d1dca3af0892d56 |

Every locator below was opened in the source text of this run. "Q3 10-Q page:13" is the Q3 2026 10-Q source chunk page:13, and so on for the other filings.

### Handoffs relied on

| Module | sha256 |
| --- | --- |
| CP-0 | 57b161fbd7e67eac0d6f2f2ef29f60aa3fbd5113ce9bed40f825ee33e1b2f40a |
| CP-1 | 401a06668766db5a4259c5743307b8caec6c76d1f88a9508bac9110bc2cd0d87 |
| CP-1A | 3bc9e341cf71dca7ff3b5bc1e47abb185281f5f4079598326a943c6cf7f10391 |
| CP-2 | 7376f87f3c4f924bd47342083b8973282a2cd33e862885cf031325906f980b10 |

Upstream re-anchor: all four handoffs name run sun-2026-11-05-credit_snapshot-host, Sunoco LP, as-of 2026-11-05, Q3 2026 and FY2025, in USD millions. The datapoints re-checked against sources are listed in Calculations. No research dossier or adoption question was assigned to this module.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The upstream conclusions trace to filings, and every recomputed figure matched. Traceability is ready with remediation: four material gaps limit committee use, mainly executed debt documents, pro forma earnings and the covenant level date. | Medium | Legal and covenant statements rest on filing summaries, and the trailing leverage ratios use partial-period acquired earnings. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of the five top credit drivers, two are directly sourced and three are calculated from sourced inputs; none is untraced. | The leverage, liquidity and cash-flow conclusions can be reproduced from filing pages. | High |
| Recomputed trailing Adjusted EBITDA is 3,535 US$m and net debt over it is 3.51x, matching the earlier handoffs. | The reported covenant net leverage of 3.5x is consistent with the derived figure, though the definitions differ. | High |
| The 5.50x leverage ceiling and 2.25x interest cover minimum come from the FY2025 10-K, not from a 2026 filing. | Statements of wide headroom rest on a covenant level dated 2025-12-31 and a definition not supplied. | Medium |
| Guarantee, ranking, change-of-control and distribution-equalisation statements rest on filing summaries, not on indentures or the partnership agreement. | Creditor rights and distribution limits cannot be confirmed; legal review is needed. | Medium |

### Evidence trace view

The earlier analysis of Sunoco LP is traceable enough for a restricted committee reading, but not yet for a clean clearance. Its strongest support is that every headline figure, including trailing Adjusted EBITDA, net debt, liquidity, maturities and cash interest, reproduces exactly from filing pages, and both interim and annual sources agree. The weakest point is that the legal and covenant statements depend on summaries in filings rather than executed debt documents, and the trailing ratios blend partial-period earnings from acquired businesses. What decides clearance is whether the credit agreement, indentures and a pro forma earnings view can be obtained; until then covenant headroom and creditor protection stay reported claims, not verified results.

### Analytical appendix — complete canonical registers

Module Status: Ready with Limitations. Traceability Scope: Top 5. External sources: none used. Perimeter: consolidated Partnership only. Entity key: issuer_id sun available.

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_sun-20251231.htm.jsonl | High: audited annual report | FY2025, year ended 2025-12-31 | Sunoco LP and consolidated subsidiaries | Statements, debt note, covenant text, business, governance, related parties | Parkland included for two months; text extraction only | Base year, covenant levels, ownership and history |
| S2 | 10-Q_2026-03-31_sun-20260331.htm.jsonl | High: unaudited interim | Q1 2026 | Same | Statements, debt, liquidity, Adjusted EBITDA reconciliation | Condensed notes | Trailing build and trend |
| S3 | 10-Q_2026-06-30_sun-20260630.htm.jsonl | High: unaudited interim | Q2 2026, six months | Same | Same | Condensed notes | Trailing build and trend |
| S4 | 10-Q_2026-09-30_sun-20260930.htm.jsonl | High: unaudited interim | Q3 2026, nine months, subsequent events to 2026-11-05 | Same | Statements, debt, liquidity, segments, Offen, guarantor information | Offen purchase accounting open | Current-period base |
| S5 | EX-99.1_2026-05-05_ex991sunerq12026.htm.jsonl | Medium: management release | Q1 2026 | Sunoco LP and SunocoCorp LLC | Non-GAAP results | Management characterisation | Supporting claims only |
| S6 | EX-99.1_2026-08-04_ex991sunerq22026.htm.jsonl | Medium: management release | Q2 2026 | Same | Non-GAAP results, guidance | Management characterisation | Supporting claims only |
| S7 | EX-99.1_2026-11-03_ex991sunocoandsunococorper.htm.jsonl | Medium: management release | Q3 2026 | Same | Non-GAAP results, guidance, leverage claim | Management characterisation | Supporting claims only |
| H1 | CP-0 handoff, run sun-2026-11-05-credit_snapshot-host | High: structurally accepted | As-of 2026-11-05 | Consolidated Partnership | Source readiness and gaps | Locator defects logged below | Perimeter and limitations |
| H2 | CP-1 handoff | High: structurally accepted | FY2025 to Q3 2026 | Consolidated Partnership | Financial base, charts, debt, liquidity | Derived ratios not pro forma | Credit drivers 1 to 3 |
| H3 | CP-1A handoff | High: structurally accepted | 2024 to 2026-11-05 | Consolidated Partnership | Business, transactions, governance | Executed documents not supplied | Credit drivers 4 and 5 |
| H4 | CP-2 handoff | High: structurally accepted | Q3 2026 and FY2025 | Consolidated Partnership | Credit view, findings, risks | Inherits upstream limits | All drivers |

#### T5B.2 Top 5 credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Trailing leverage fell to 3.72x gross and 3.51x net at Q3 2026 from 6.54x and 6.11x at FY2025 | CP-1 | Debt 13,163 and cash 760 at 2026-09-30; trailing Adjusted EBITDA 3,535 | Leverage tolerance and refinancing capacity depend on the earnings base, which changed with Parkland | Sets the leverage conclusion and the covenant discussion | Q3 10-Q page:13, page:3, page:22; 10-K page:129, page:247 | Not pro forma; management-adjusted EBITDA |
| 2 | Liquidity of 3,060 against 1,049 of 2027 notes, with a modest wall until 2029 | CP-1 | Cash 760 plus unused revolver 2,300; debt table by maturity | Liquidity and refinancing risk | Near-term refinancing view | Q3 10-Q page:15, page:13, page:14 | 2027 notes classed long-term on intent; Offen funding not stated |
| 3 | Debt service and cash conversion: cash interest cover 4.87x; operating cash flow above capital expenditure and distributions | CP-1 | Interest paid, operating cash flow, capital expenditure, distributions | Debt service capacity | Cash coverage view | Q3 10-Q page:5, page:6, page:11; 10-K page:243 | Working capital timing and inventory effects |
| 4 | Sponsor control, incentive distributions and equalisation payments | CP-1A | Energy Transfer holdings, Delegation Agreement, distribution table | Creditor control and cash leakage | Governance posture | Q3 10-Q page:7, page:19, page:44; 10-K page:122, page:197 | Partnership agreement and indentures not supplied |
| 5 | Acquisition pace: Parkland, TanQuid, Delta and Offen with open purchase accounting | CP-1A | Acquisition notes and subsequent event | Leverage, perimeter and integration | Forward leverage risk | 10-K page:7, page:238; Q3 10-Q page:9, page:10 | Offen funding and pro forma earnings not stated |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Driver 1: net debt over trailing Adjusted EBITDA is 3.51x | CP-1 | "Total debt 13,163 13,389"; Adjusted EBITDA reconciliation rows | Yes | High | Calculated | Supported | High | Committee-Ready |
| Driver 1 sub-claim: part of the fall reflects acquired earnings entering the base | CP-2 | Parkland closed 2025-10-31 (10-K page:7); FY2025 includes two months (10-K page:129) | Yes | High | Analyst Inference | Partially Supported | Medium | Remediation Needed |
| Driver 1 sub-claim: reported covenant net leverage 3.5x | CP-1 | "The Partnership’s net leverage ratio was 3.5 to 1.00 at September 30, 2026." (Q3 10-Q page:15) | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Driver 2: liquidity of 3,060 | CP-1 | Cash 760 (page:3); unused availability 2.30 billion (page:15) | Yes | High | Calculated | Supported | High | Committee-Ready |
| Driver 2: 2027 notes 1,049 classed long-term on refinancing intent | CP-1 | Footnote (2), Q3 10-Q page:14 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Driver 3: cash interest cover 4.87x | CP-1 | Interest paid 434 (10-K page:243); 573 and 281 (Q3 10-Q page:11) | Yes | High | Calculated | Supported | Medium | Committee-Ready |
| Driver 3: operating cash flow 2,251 against distributions 880 | CP-1 | Q3 10-Q page:5 and page:6 | Yes | High | Calculated | Supported | High | Committee-Ready |
| Driver 4: Energy Transfer ownership and control | CP-1A | 28,463,967 common units, general partner, incentive distribution rights (Q3 10-Q page:7) | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Driver 4 sub-claim: incentive distributions compete with debt reduction for cash | CP-2 | Distribution table (Q3 10-Q page:44); tier table (10-K page:122) | Yes | High | Analyst Inference | Partially Supported | Medium | Remediation Needed |
| Driver 5: Offen acquired 2026-10-27 for about 600 | CP-1A | Q3 10-Q page:10 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Management claim: returns to leverage target in under a year | CP-1A | Release Q3 page:2; target level not stated | Yes | Medium | Weak Lineage | Insufficient support for verification | Low | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 13,163 at 2026-09-30 | source-text/10-Q_2026-09-30_sun-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:13, Note 9 | CP-1 financials | Sourced | High | Items sum to 13,163 after 80 of issuance costs |
| Cash 760 at 2026-09-30 | source-text/10-Q_2026-09-30_sun-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:3, balance sheet | CP-1 liquidity | Sourced | High | Consolidated cash |
| Revolver: 111 drawn, 84 letters of credit, 2.30 billion unused, maturity 2030-06-17 | source-text/10-Q_2026-09-30_sun-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:15, Credit Facility | CP-1 liquidity | Sourced | High | Facility size 2,500 |
| Adjusted EBITDA FY2025 2,047; nine months 2026 2,889; nine months 2025 1,401 | source-text files S1 and S4 | 10-K; 10-Q Q3 2026 | S1; S4 | page:129; page:22 and page:33 | CP-1 financials | Sourced | High | Management non-GAAP measure |
| Trailing Adjusted EBITDA 3,535 | Derived from S1 and S4 | 10-K; 10-Q Q3 2026 | S1; S4 | page:129; page:33 | CP-1 calculations | Calculated | High | 2,047 + 2,889 − 1,401 |
| Covenant: maximum Net Leverage Ratio 5.50 to 1.00 and minimum Interest Coverage Ratio 2.25 to 1.00 | source-text/10-K_2025-12-31_sun-20251231.htm.jsonl | 10-K FY2025 | S1 | page:251, Credit Facility | CP-1 covenants | Sourced | High | Level dated 2025-12-31; not restated in 2026 filings |
| Reported net leverage 4.03, 3.98, 3.7, 3.5 | S1, S2, S3, S4 | 10-K; three 10-Qs | S1 to S4 | page:251; page:13; page:14; page:15 | CP-1 chart notes | Sourced | High | Management-reported, credit-agreement definition |
| Maturities 2027 1,049; 2029 2,723; 2030 2,309 | S4 | 10-Q Q3 2026 | S4 | page:13 | CP-1 maturities | Calculated | High | Sum of debt table lines by stated year |
| Interest paid 434; 573; 281 | S1; S4 | 10-K; 10-Q Q3 2026 | S1; S4 | page:243; page:11 | CP-1 interest cover | Sourced | High | Cash-flow supplemental data |
| Operating cash flow 2,251; capital expenditure 579; distributions 611, 151 and 118 | S4 | 10-Q Q3 2026 | S4 | page:5 and page:6 | CP-1 and CP-2 | Sourced | High | Sum of distributions is 880 |
| Energy Transfer owns the general partner, 28,463,967 common units and all incentive distribution rights | S4 | 10-Q Q3 2026 | S4 | page:7, Note 1 | CP-1A profile | Sourced | High | Controls SunocoCorp |
| Delegation Agreement dated 2025-10-27 | S1 | 10-K FY2025 | S1 | page:197 | CP-1A governance | Sourced | High | Board appointment right delegated to SunocoCorp |
| Q3 2026 distribution: 139 common, 52 Class D, 76 incentive holders | S4 | 10-Q Q3 2026 | S4 | page:44 | CP-1A governance | Sourced | High | Rounded in source |
| Offen Petroleum acquired 2026-10-27 for about 600 in cash | S4 | 10-Q Q3 2026 | S4 | page:10 | CP-1A transactions | Sourced | High | Subsequent event |
| 7-Eleven about 13% of FY2025 revenues; 15-year take-or-pay agreement | S1 | 10-K FY2025 | S1 | page:261 | CP-1A operating model | Sourced | High | FY2025 only |
| Variable-rate debt 398; fair value of debt 12.88 billion against carrying 13.16 billion | S4 | 10-Q Q3 2026 | S4 | page:48; page:15 | CP-2 findings | Sourced | High | Aggregate, Level 2 |
| Release: returns to leverage target in less than one year | S7 | EX-99.1 Q3 2026 | S7 | page:2 | CP-1A operating model | Management Language | Medium | Target level not stated |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Trailing Adjusted EBITDA, Q3 2026 | CP-1 charts and table; CP-2 | 2,047; 2,889; 1,401 (USD millions) | FY2025 + nine months 2026 − nine months 2025; no pro forma adjustment | Calculated | Supported | High | Leverage, coverage | S1 page:129; S4 page:33 |
| Total debt over trailing Adjusted EBITDA | CP-1 leverage chart | 13,163; 3,535 | Carrying total debt at 2026-09-30 divided by trailing figure; result 3.72x | Calculated | Supported | High | Leverage | S4 page:13 |
| Net debt over trailing Adjusted EBITDA | CP-1; CP-2 | 13,163; 760; 3,535 | (Debt − cash) divided by trailing figure; result 3.51x | Calculated | Supported | High | Leverage | S4 page:13, page:3 |
| Cash interest cover | CP-1 interest chart | 3,535; 726 | Trailing Adjusted EBITDA divided by trailing interest paid (434 + 573 − 281); result 4.87x | Calculated | Supported | Medium | Debt service | S1 page:243; S4 page:11 |
| Liquidity | CP-1 liquidity chart; CP-2 | 760; 2,300 | Cash plus stated unused availability; check 2,500 − 111 − 84 = 2,305 | Calculated | Supported | High | Liquidity | S4 page:3, page:15 |
| Maturities by year | CP-1 maturity chart | Debt table lines | Sum by stated maturity year; total 13,243 less 80 issuance costs equals 13,163 | Calculated | Supported | High | Refinancing | S4 page:13 |
| Free cash flow after distributions | CP-2 | 2,251; 579; 880 | Operating cash flow − capital expenditure − distributions = 792 | Calculated | Supported | Medium | Liquidity, distribution capacity | S4 page:5, page:6 |
| Illustrative net leverage if Offen is fully debt-funded | CP-2 | 12,403; 600; 3,535 | (Net debt + 600) divided by trailing figure = 3.68x; no Offen earnings; funding assumption | Assumption-Based | Partially Supported | Low | Forward leverage | S4 page:10; labelled illustrative in CP-2 |
| EBITDA fall at which derived net leverage reaches 5.50x | CP-2 | 12,403; 5.50 | 12,403 / 5.50 = 2,255; decline 1,280 or 36.2%; covenant definition not applied | Calculated | Partially Supported | Low | Headroom, derived basis | S1 page:251 for the level |
| Debt over debt plus equity | CP-2 | 13,163; 8,512 | 13,163 / (13,163 + 8,512) = 60.7% | Calculated | Supported | Medium | Capital structure | S4 page:3 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Reported headroom to the 5.50x ceiling is wide | The ceiling and the 2.25x minimum are cited only to the 10-K dated 2025-12-31; later filings report compliance and net leverage but not the levels | Analyst Inference | Headroom drives the perception of default risk and liquidity; a changed level or definition would change it | State the level with its date; avoid computing headroom until the credit agreement is supplied | CP-1 Debt and claims outside debt; CP-2 Reader summary and Key findings |
| Material | Guarantee, ranking and change-of-control statements | Rest on filing summaries; indentures and partnership agreement not supplied | Weak Lineage | Creditor rights and recovery mechanics depend on clause-level terms | Obtain executed documents; label statements as filing summaries | CP-1 Debt and claims outside debt; CP-1A Ownership; CP-2 Key findings |
| Minor | Management claim of a return to leverage target | Target level not stated | Weak Lineage | Cannot be verified against the reported ratio | Keep tagged as Management Language | CP-1A Company and operating model |
| Minor | Locators for the audit report and statements in the readiness handoff | Page numbers point to an index and an Item 9A reference | Weak Lineage | Misdirects a reviewer; the figures themselves are unaffected | Use the corrected locators in this handoff | CP-0 Source assessment |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2025 and Q1 to Q3 2026 and subsequent events to 2026-11-05 | Executed legal documents, ratings and Q3 2025 balance sheet are absent, so legal and trend statements stop at summaries | Covenant and ranking conclusions stay reported claims | Obtain credit agreement, indentures and partnership agreement |
| Citation completeness | Ready with Remediation | Every statement in the Top 5 maps to a filing page; three locator defects found | Imprecise locators slow review but do not change figures | Low impact on credit conclusions | Correct locators as logged |
| Calculation traceability | Ready with Remediation | All ten calculations reproduce from filing inputs; none is pro forma | Partial-period acquired earnings distort trailing ratios | Leverage trajectory should be read as reported, not as a run rate | Provide pro forma earnings or label ratios as not pro forma |
| Assumption transparency | Committee-Ready | The only assumptions, the Offen debt-funding illustration and the 5.50x breakeven, are labelled illustrative or derived | Unlabelled scenarios would overstate precision | Limited | None beyond keeping the labels |
| Markdown and export artifact integrity | Ready with Remediation | Handoffs use the six CP-OS headings and passed the structural check; no YAML envelope or filename convention is used in this transport | A reader expecting the full envelope will not find it | Handoff is consumed as designed by CP-OS | Note the transport difference in downstream use |

Overall auditability: Ready with Remediation, the lowest of the five dimensions.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed debt documents not supplied | Credit agreement, senior note indentures, GoZone bond agreements, partnership agreement | Restricted payments, incurrence, guarantees and change of control cannot be verified, which limits default risk and recovery mechanics | Covenant, ranking and governance statements | High impact | Executed documents |
| CP-5-GAP-002 | Pro forma earnings absent | Pro forma Adjusted EBITDA for Parkland, TanQuid, Delta and Offen | Trailing ratios mix partial and full periods | Leverage and cover charts | High impact | Pro forma disclosure or management bridge |
| CP-5-GAP-003 | Covenant level date and definition | Compliance certificate or 2026 credit agreement terms | Headroom claims rest on a level dated 2025-12-31 | Credit view | Medium impact | Compliance certificate |
| CP-5-GAP-004 | Offen funding not stated | Funding description for about 600 cash | Post-quarter leverage and liquidity | Forward leverage | Medium impact | Next filing |
| CP-5-GAP-005 | Entity jurisdiction and exchange change unexplained | Disclosure of the Delaware to Texas and NYSE to TXSE changes | Entity naming in debt documents | Profile and conflicts | Medium impact | Form 8-K or debt documents |
| CP-5-GAP-006 | Ratings and market prices not supplied | Ratings, instrument prices, spreads | Rating-linked pricing and market view cannot be tested | Refinancing assessment | Medium impact | Rating reports and market data |
| CP-5-GAP-007 | Refinery transfer pricing not described | Intersegment pricing terms | Segment earnings may not equal external margin | Earnings quality | Medium impact | Segment disclosures |
| CP-5-GAP-008 | Q3 2025 balance sheet not in pack | September 2025 debt and cash | Trend before Q1 2026 incomplete | Leverage chart | Low impact | Q3 2025 10-Q |
| CP-5-GAP-009 | Tables and charts read from text only | Image and chart inspection | A successful extraction is not a fidelity review | All tables | Low impact | Original filings |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 response, sha 57b161fbd7e67eac0d6f2f2ef29f60aa3fbd5113ce9bed40f825ee33e1b2f40a; run sun-2026-11-05-credit_snapshot-host | Source readiness | High | Six CP-OS H2 headings present; no YAML envelope in this transport | Accepted by CP-OS structural check | Issues CP5-004, CP5-005, CP5-010 |
| CP-1 | requests/CP-1 response, sha 401a06668766db5a4259c5743307b8caec6c76d1f88a9508bac9110bc2cd0d87; same run | Financial base | High | Six CP-OS H2 headings and report selectors present | Accepted by CP-OS structural check | Issues CP5-001, CP5-002, CP5-003, CP5-007 |
| CP-1A | requests/CP-1A response, sha 3bc9e341cf71dca7ff3b5bc1e47abb185281f5f4079598326a943c6cf7f10391; same run | Business and transactions | High | Six CP-OS H2 headings and selectors present | Accepted by CP-OS structural check | Issues CP5-003, CP5-004, CP5-006 |
| CP-2 | requests/CP-2 response, sha 7376f87f3c4f924bd47342083b8973282a2cd33e862885cf031325906f980b10; same run | Credit synthesis | High | Six CP-OS H2 headings and selectors present | Accepted by CP-OS structural check | Issues CP5-001, CP5-002, CP5-008, CP5-009 |

Module Status for the QA phase: Ready with Limitations. CP-5 evidence trace (T5B.1 to T5B.8) is available above.

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1; CP-2 | "Reported headroom to the 5.50x ceiling is wide" (CP-2 Reader summary); covenant levels in CP-1 | Partially Supported | The 5.50x maximum and 2.25x minimum are stated in the 10-K at page:251 as of 2025-12-31; the Q3 10-Q at page:15 reports 3.5 to 1.00 and compliance but not the levels. Headroom is therefore an inference from a dated level and a definition not supplied | State the date of the level; do not present headroom as verified | Requires Legal Review |
| Minor | CP-0 | Auditor reports "at page:152 and page:215"; statements "pages 215 to 221"; debt note "pages 248 to 252" | Partially Supported | Page 152 is Item 9A text and page 215 is the financial statement index. The audit opinion is at page:217 to page:219, the balance sheet at page:219 and page:220, operations at page:220, cash flows at page:221 and page:222, and the debt table begins at page:247. This handoff corrects those locators; the figures were unaffected | Use corrected locators | Formatting / Hygiene Only |
| Minor | CP-1A | Pipeline Systems and Refinery segment figures cited to page:21 and page:15 in the operating model table; auditor named in the profile at page:217 | Partially Supported | The segment Adjusted EBITDA figures print at Q3 10-Q page:22, and the firm name Grant Thornton prints at 10-K page:219; the cited pages carry the descriptions and the opinion text | Cite page:22 and page:219 | Formatting / Hygiene Only |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1; CP-2 | Trailing leverage and cover mix partial and full periods: Parkland closed 2025-10-31, so the trailing window to 2026-09-30 omits one month and FY2025 includes two months | No pro forma adjustment; trailing Adjusted EBITDA is FY2025 + nine months 2026 − nine months 2025 = 3,535 | None between sources; the reported covenant ratio is pro forma in a way not disclosed | Label as not pro forma; obtain pro forma earnings | Requires Source Reconciliation |
| Minor | CP-1; CP-2 | Derived net leverage 3.51x and reported covenant net leverage 3.5x are used side by side and in the credit view as "about 3.5x" | Derived ratio uses carrying debt and Adjusted EBITDA; the covenant ratio uses credit-agreement definitions not supplied (10-K page:252 describes cash netting for Parkland) | None | Keep the two labelled separately | Monitoring Follow-Up |

All recomputations tied to the inputs; see Calculations. No arithmetic error was found.

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1; CP-1A; CP-2 | Notes are guaranteed by subsidiaries and rank effectively behind secured obligations, including the revolver, and structurally behind non-guarantor subsidiary debt; the GoZone bonds carry a 101% change-of-control repurchase right after a ratings decline; distributions to SunocoCorp must match Sunoco unit distributions through 2027-12-31; the board appointment right is delegated to SunocoCorp | Senior note indentures, credit agreement, GoZone bond agreements, Partnership Agreement, Delegation Agreement and Omnibus Agreement | Statements rest on summaries at Q3 10-Q pages 15, 19, 46 and 47 and 10-K pages 197, 250 and 251; no clause-level text is supplied; collateral package not described | Label as filing summaries; obtain executed documents | Legal review required before any capacity conclusion |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Aggregate fair value of debt of 12.88 billion against a carrying amount of 13.16 billion at 2026-09-30, the reverse of 2025-12-31 | Instrument-level prices, spreads and ratings | The source gives a Level 2 aggregate only (Q3 10-Q page:15) and no explanation of the move | Keep it as an aggregate observation; do not read it as instrument pricing | Monitoring Follow-Up |

No relative value ranking, instrument recommendation or recovery conclusion appears in the audited handoffs.

#### T5.6 Cross-module consistency and version-control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-0; CP-1A | The 10-K and Q1 10-Q say Delaware, the Q2 and Q3 10-Qs say Texas, the auditor opinion says "a Delaware limited partnership", and the exchange moves from NYSE to TXSE; no source explains the change | Different filing dates, same entity name and the same Commission File Number 001-35653 | Keep the conflict logged; confirm entity naming in the debt documents | Issuer and guarantor naming in later legal work |

Cross-module checks that agreed: issuer name and as-of date; consolidated perimeter; total debt 13,163 and cash 760; liquidity 3,060; maturities by year; trailing Adjusted EBITDA 3,535; reported net leverage series; Offen amount; Energy Transfer holdings. No contradictory conclusions were found.

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Promotional or Non-Credit Language | Terms such as "ample", "strong" and "comfortable" appear in the credit view and summaries; each is followed by the supporting figures, but the headline words add no information | Prefer the figures | Formatting / Hygiene Only |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0; CP-1; CP-1A; CP-2 | Envelope | The handoffs carry the six CP-OS headings and not the YAML front matter, the Audit Summary, Evidence Trace, Source Registry and QA Validation headings of the canonical envelope; no scripted confidence score or file name convention is applied in this transport | Note the transport difference when the handoffs are consumed outside CP-OS | Formatting / Hygiene Only |

Orphan claim check: the one Weak Lineage conclusion in committee-facing output, the management leverage target, is tagged Management Language and carries a limitation, so it is not an orphan claim.

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-1; CP-2 | Partially Supported Claim | Covenant headroom statement rests on 5.50x and 2.25x levels dated 2025-12-31 and an unsupplied definition | State the date; do not present headroom as verified | Requires Legal Review | Open |
| CP5-002 | Material | CP-1; CP-2 | Entity / Perimeter Mismatch | Trailing ratios not pro forma for Parkland, TanQuid, Delta and Offen | Label as not pro forma; obtain pro forma earnings | Requires Source Reconciliation | Open |
| CP5-003 | Material | CP-1; CP-1A; CP-2 | Legal Support Gap | Guarantee, ranking, change-of-control and distribution-equalisation statements rest on filing summaries | Obtain executed documents | Requires Legal Review | Open |
| CP5-004 | Material | CP-0; CP-1A | Conflicting Evidence | Delaware and Texas wording and NYSE and TXSE listing unexplained | Confirm in debt documents | Requires Source Reconciliation | Open |
| CP5-005 | Minor | CP-0 | Citation Gap | Audit report, statement and debt note locators imprecise; corrected here | Use corrected locators | Formatting / Hygiene Only | Open |
| CP5-006 | Minor | CP-1A | Citation Gap | Segment figures and auditor name cited to neighbouring pages | Cite page:22 and page:219 | Formatting / Hygiene Only | Open |
| CP5-007 | Minor | CP-1; CP-2 | Formula / Definition Drift | Derived 3.51x and reported 3.5x used side by side | Label separately | Monitoring Follow-Up | Open |
| CP5-008 | Minor | CP-2 | Market Data Gap | Fair value aggregate has no instrument-level pricing | Keep as aggregate | Monitoring Follow-Up | Open |
| CP5-009 | Minor | CP-2 | Promotional or Non-Credit Language | Headline adjectives without added information | Prefer figures | Formatting / Hygiene Only | Open |
| CP5-010 | Minor | CP-0; CP-1; CP-1A; CP-2 | canonical Markdown Handoff Integrity Defect | Transport uses six CP-OS headings, not the YAML envelope | Note when consumed outside CP-OS | Formatting / Hygiene Only | Open |

#### Remediation priority map

Must-fix before committee: CP5-001 (state the covenant level date and treat headroom as unverified), CP5-002 (label trailing ratios as not pro forma), CP5-003 (obtain executed debt documents or label statements as filing summaries), CP5-004 (confirm entity naming).

Must-fix before the canonical Markdown handoff is consumed downstream: CP5-010 (note the transport difference).

Monitoring follow-up: CP5-007 and CP5-008 (keep derived and reported ratios, and the fair value aggregate, labelled).

Formatting and hygiene: CP5-005, CP5-006 and CP5-009 (use the corrected locators; prefer figures to adjectives).

#### Overall traceability view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 3 are calculated, 0 are assumption-based, 0 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the executed credit agreement, indentures and partnership agreement together with the covenant levels dated 2025-12-31, which matters because default risk, distribution capacity and recovery mechanics depend on clause-level terms and implies that committee use is restricted until they are obtained. Sub-claims in drivers 1 and 4 are analyst inferences and one management claim has weak lineage; they are logged in the traceability map and do not change a driver's class.

#### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 4. Minor Issues: 6. Committee Use: Restricted.

No finding changes the credit conclusion, so qa_status is Restricted under the severity engine (any Material, no Critical). The four material issues (CP5-001 to CP5-004) must be disclosed for committee use: the covenant level date, the non-pro-forma perimeter, the reliance on filing summaries for legal terms, and the unexplained entity wording. The numeric confidence score is script-owned and the scoring script is not part of this transport, so no score or band is stated.

## Calculations

Independent recomputation from the source text of this run, not from the handoffs. All figures USD millions unless stated.

| Item | Source inputs (page) | Recomputed result | Handoff value | Match |
| --- | --- | --- | --- | --- |
| Trailing Adjusted EBITDA, Q3 2026 | 2,047 (10-K page:129); 2,889 and 1,401 (Q3 10-Q page:33) | 2,047 + 2,889 − 1,401 = 3,535 | 3,535 | Yes |
| Trailing Adjusted EBITDA, Q1 and Q2 2026 | 858 and 458 (Q1 10-Q page:20); 1,840 and 912 (Q2 10-Q page:21) | 2,447; 2,975 | 2,447; 2,975 | Yes |
| Quarterly sum | 858 + 982 + 1,049 | 2,889 | 2,889 | Yes |
| Debt table sum, 2026-09-30 | Q3 10-Q page:13 lines, including 111 for the revolver | 13,163 after 80 of issuance costs | 13,163 | Yes |
| Maturity buckets | Same lines by stated year | 1,049; 900; 2,723; 2,309; 1,600; 1,243; 1,000; 1,500; 322; 597 | Same | Yes |
| Net debt | 13,163 − 760 | 12,403 | 12,403 | Yes |
| Total debt over trailing Adjusted EBITDA | 13,163 / 3,535 | 3.724x | 3.72x | Yes |
| Net debt over trailing Adjusted EBITDA | 12,403 / 3,535 | 3.509x | 3.51x | Yes |
| FY2025 ratios | 13,389 and 891 (10-K page:247, page:219); 2,047 | 6.541x; 6.106x | 6.54x; 6.11x | Yes |
| Trailing cash interest | 434 (10-K page:243); 573 and 281 (Q3 10-Q page:11) | 726; cover 4.869x | 726; 4.87x | Yes |
| Liquidity | 760 + 2,300; check 2,500 − 111 − 84 | 3,060; 2,305 | 3,060; consistent | Yes |
| Free cash flow after distributions, nine months 2026 | 2,251 − 579 − 880 (Q3 10-Q page:5 and page:6) | 792 | 792 | Yes |
| Distributions | 611 + 151 + 118 | 880 | 880 | Yes |
| FY2025 maturity schedule check | 954 + 1,661 + 1,202 + 2,797 + 2,206 + 4,650 (10-K page:248) | 13,470 | 13,470 | Yes |

## Gaps

The nine gaps are in the gaps ledger above (CP-5-GAP-001 to CP-5-GAP-009). The ones that change a conclusion are the missing executed debt documents (limits covenant, ranking and distribution conclusions), the missing pro forma earnings (limits the leverage trajectory), the covenant level dated 2025-12-31 (limits headroom statements), and the unstated Offen funding (limits post-quarter leverage). Readiness: Ready with Limitations. No earlier accepted answer was changed; corrections of locators are stated in the issue log.

## Next module

This is the last module in the minimum set, so CP-OS can assemble the report. A reader using it should treat covenant headroom, guarantee and ranking statements, and the trailing leverage ratios as reported or derived claims until the credit agreement, the indentures and a pro forma earnings view are obtained.
