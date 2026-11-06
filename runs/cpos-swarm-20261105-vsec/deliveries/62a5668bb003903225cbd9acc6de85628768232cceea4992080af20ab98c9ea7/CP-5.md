## Request

This handoff validates the evidence trace and research integrity of the CP-0, CP-1, CP-1A and CP-2 handoffs for VSE CORP (VSE Corporation, ticker VSEC) as of 2026-11-05 on the credit_snapshot pathway, run vsec-2026-11-05-credit_snapshot-host, reporting period Q3 2026 against FY2025, in USD. Scope is the Top 5 material credit drivers, with every locator and calculation in the four handoffs rechecked against the pinned sources. It changes no credit conclusion and silently repairs nothing; defects are logged with a required fix.

## Sources

Issuer sources against which the upstream handoffs were rechecked. Locators are `page:N`, the chunk of the converted file, not the printed page.

| Label | Exact source name | sha256 |
| --- | --- | --- |
| S1 | 10-K_2025-12-31_vsec-20251231.htm.jsonl | 83b072172f28f55aebaf3a6972f9c86687a4b113bdf988f323774cea0cf36aed |
| S2 | 10-Q_2026-03-31_vsec-20260331.htm.jsonl | f6b924ea5eba470e1f49667b84c48b593c43a380b95f687d6114875e8f37f39d |
| S3 | 10-Q_2026-06-30_vsec-20260630.htm.jsonl | fa3609d44d226dc8671529fb2fbfc175fcb641b5ffc98070769608107bc75600 |
| S4 | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | 68af0ce7093699c714a705843bb9cea05a028d2dd1bb6a0a12fdd362022c36f1 |
| S5 | EX-99.1_2026-05-05_vse-prxq1x2026earningsrele.htm.jsonl | 1a0b0741e0cb41d8d01fb77bba0765b0d91e0ee2d640c0871a3ef4c38f0e2f04 |
| S6 | EX-99.1_2026-08-05_vse-prxq2x2026earningsrele.htm.jsonl | 047a25aea3f55f6b12255c44556aba2d1cd8074d64427d9b3bf8fc3f0328e7e4 |
| S7 | EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | 433c5d4af4ceef97f7133d6bf32c06676acee7a23adece5c52f374d8108500f0 |

Run settings (not issuer evidence): context sha256 40207d2127823884a7bc8082859719f4c4c78b2e88a9548b0c57178ea14b1746.

Supplied handoffs, all opened in full and re-anchored (module, run, entity, period and values restated in the first appendix register):

| Module | sha256 |
| --- | --- |
| CP-0 | 2cdcc9415abc8726a2bd6013cc3fc6053fad1900f1d23a6661cbe4e6c3b944c9 |
| CP-1 | 0ce2ba0d41587fd6984e42432ff1f87478ce6e2541bbe874409fd590811a2170 |
| CP-1A | bbe5dabc3d375b69ee76ab844cf013f38bda2f0326a4a2247d2db1ff3e9b86f4 |
| CP-2 | a8a1ab8afd1514757a3bb5aa4b4cd16d01a6b93effbaf65a791adfe4044700b1 |

Method of the check: every quoted phrase in the four handoffs was searched in the cited source page text; every page locator was confirmed to exist; every comma-formatted figure on a line with a locator was searched on the cited pages; every calculation was recomputed from the cited inputs. The numeric confidence script and the mechanical completeness script named in the method are not part of this run, so no numeric confidence score is asserted. The sources are text conversions of HTML filings and were not compared with the original filings or inline XBRL.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial base, business and credit work on VSE is largely traceable to filed sources, with limitations. Committee use should be restricted: covenant headroom, acquisition-adjusted leverage and the guidance-based year-end estimate are not independently supported. | Medium | The credit agreement is absent and the text conversions were never checked against the original filings, so legal terms and some figures rest on management statements. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of the five main credit drivers, three are directly sourced and two are calculated from sourced figures; none rests on an untraced claim. | The core leverage, liquidity and cash flow view can be relied on, subject to the management-EBITDA limitation. | High |
| Covenant headroom, guarantor structure and security cannot be traced because the credit agreement and its amendment are not supplied. | Creditor control and headroom must be treated as not supplied, which restricts committee use. | High |
| Acquisition-adjusted leverage of 2.35x and the year-end estimate of about 2.6x rest on management figures and guidance; leverage on filed figures is 3.04x. | Treat those two ratios as management-attributed and quote the filed-basis ratio first. | Medium |
| The review found no calculation errors and three page-locator slips, recorded here without changing any conclusion. | Citation hygiene is adequate for committee use once the recorded corrections are applied. | Medium |
| The acquisition price appears as USD 2.025 billion in one filing and USD 2,020,007 thousand in another; the conflict is logged, not reconciled. | Any size comparison must quote the figure with its basis. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 3 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the credit agreement and its first amendment, which matters because covenant levels, guarantors and distribution limits govern creditor control and so bound any claim about headroom, and implies that committee use is restricted to the stated figures with covenant headroom treated as not supplied.

Outside the Top 5, the guidance-implied year-end leverage is assumption-based and the acquisition price is conflicting; both are flagged in the upstream handoffs and are not repaired here.

### Traceability scope and clearance

Traceability scope: Top 5. Module status: Ready with Limitations (all four upstream handoffs present and accepted; legal documents and cash interest for 2026 absent). Clearance decision: Pass with Remediation, because no Critical issue is unresolved and six Material and seven Minor issues require correction or disclosed limitation. Committee status: Restricted. Severity counts for the issue log: Critical 0, Material 6, Minor 7.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_vsec-20251231.htm.jsonl | High: filed, audited, auditor opinion present | FY2025, year ended 2025-12-31 | VSE Corporation consolidated | Statements, notes, debt note, cash paid for interest and taxes, customer concentration, segment and geography | Pre-dates the 2026 acquisition; PAG appears as a subsequent event | CP-1 base period; CP-1A business facts; CP-2 prior-period comparison |
| S2 | 10-Q_2026-03-31_vsec-20260331.htm.jsonl | High: filed, unaudited | Q1 2026 | VSE Corporation consolidated | Statements, debt, unused commitments, PAG summary | Cash is pre-closing offering proceeds | CP-1 chart rows; CP-1A transaction facts |
| S3 | 10-Q_2026-06-30_vsec-20260630.htm.jsonl | High: filed, unaudited | Q2 2026, six months | VSE Corporation consolidated | Statements, debt, PAG purchase accounting | Purchase accounting preliminary | CP-1 chart rows; CP-1A conflicts |
| S4 | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | High: filed, unaudited, latest | Q3 2026, nine months | VSE Corporation consolidated | Statements, debt by facility, maturity table, covenant statement, acquisitions, subsequent event | Purchase accounting preliminary; signed on the cutoff date | Primary source for all current figures |
| S5 | EX-99.1_2026-05-05_vse-prxq1x2026earningsrele.htm.jsonl | Medium: management release, non-GAAP | Q1 2026 | VSE Corporation | Adjusted EBITDA, net debt, TTM measures | Definitions later changed; supporting claims only | CP-1 EBITDA inputs |
| S6 | EX-99.1_2026-08-05_vse-prxq2x2026earningsrele.htm.jsonl | Medium: management release, non-GAAP | Q2 2026, six months | VSE Corporation | Adjusted EBITDA, TTM measures, guidance | Adjusted Net Income definition changed | CP-1 EBITDA inputs |
| S7 | EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | Medium: management release, non-GAAP | Q3 2026, nine months | VSE Corporation | Adjusted EBITDA reconciliation, TTM, net debt, guidance | Acquisition-adjusted figures have no schedule | CP-1 and CP-2 EBITDA and guidance inputs |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage after the acquisition: net debt 3.04x trailing adjusted EBITDA (1.24x at 2025-12-31) | CP-1, CP-2 | Principal debt 978,793 and cash 65,786 (USD k) from the 10-Q; management TTM Adjusted EBITDA 300,387 | Floating-rate acquisition debt on trailing earnings that include five months of the acquired business drives default risk and leverage tolerance | Sets the starting point for deleveraging and covenant questions | S4 page:17; S4 page:4; S7 page:7 | EBITDA is a management measure, not the credit-agreement EBITDA |
| 2 | Liquidity and maturities: USD 545.0 million liquidity against USD 32.3 million due within twelve months | CP-1, CP-2 | Cash 65,786; unused commitments 479.2 million; maturity table | Determines refinancing and debt service capacity | Supports a low near-term refinancing risk finding | S4 page:4; S4 page:32; S4 page:19 | Acquisition spending from the revolver can erode it |
| 3 | Cash conversion: free cash flow negative 3,415 for nine months after a 148,409 inventory build | CP-1, CP-2 | Operating cash flow 21,284 and capital expenditures 24,699 | Deleveraging depends on working capital release and fourth-quarter cash flow | Frames the weakest point of the credit view | S4 page:6; S7 page:7; S4 page:33 | Quarter is positive; year-end release is a management expectation |
| 4 | Floating-rate cost: 667,750 unhedged floating-rate debt (USD k) | CP-1, CP-2 | Term loan B 897,750 and revolver 20,000 against 250,000 of swap notional | Interest cost and cover move with rates | Quantifies rate sensitivity | S4 page:17; S4 page:19 | Swap benchmark and loan reset tenor may differ; full offset is assumed |
| 5 | Customer and OEM concentration: one customer group about 20% of FY2025 revenue; repair margins rest on OEM approvals and licenses | CP-1A, CP-2 | Customer group 20%, 21%, 14% for FY2025, FY2024, FY2023; PT6 license; Atech approvals | Single-name loss removes high-margin work while inventory and capacity remain | Business risk driver for revenue durability | S1 page:11; S1 page:70; S4 page:14; S7 page:2 | Figure is pre-acquisition; current exposure not disclosed |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rank 1: net debt 3.04x TTM Adjusted EBITDA | CP-1, CP-2 | Principal 978,793 less cash 65,786, over 300,387 (S4 page:17; S4 page:4; S7 page:7) | Yes | High for debt and cash; Medium for management EBITDA | Calculated | Supported with limitation | Medium | Remediation Needed |
| Rank 2: liquidity USD 545.0 million; maturities by year | CP-1, CP-2 | "$479.2 million of unused commitments under the Credit Agreement" (S4 page:32); cash 65,786 (S4 page:4); maturity table (S4 page:19) | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Rank 3: nine-month free cash flow negative 3,415; inventory build 148,409 | CP-1, CP-2 | Free cash flow (3,415) (S7 page:7); inventories (148,409) (S4 page:6) | Yes | High for cash flow lines; Medium for the management free cash flow label | Directly Sourced | Supported | High | Committee-Ready |
| Rank 4: unhedged floating debt 667,750; 100 bp adds 6,678 a year | CP-1, CP-2 | Principal by facility (S4 page:17); swap notionals (S4 page:19) | Yes | High for inputs | Calculated | Supported with assumption | Medium | Remediation Needed |
| Rank 5: customer group about 20% of FY2025 revenue | CP-1A, CP-2 | "collectively accounted for approximately 20% of the Company" (S1 page:11) | Yes | High, stale for the current perimeter | Directly Sourced | Supported for FY2025 | Medium | Remediation Needed |
| Year-end leverage about 2.6x from guidance | CP-2 | Guidance growth and margin (S7 page:3); FY2025 revenue (S1 page:42) | Yes | Medium: management guidance | Assumption-Based | Supported as an estimate | Low | Remediation Needed |
| Acquisition-adjusted leverage 2.35x and 2.51x | CP-1, CP-2 | TTM Acquisition Adjusted EBITDA 389,234 (S7 page:7) | Partial: no component schedule | Medium | Weak Lineage | Flagged with limitation | Low | Remediation Needed |
| Acquisition price size | CP-0, CP-1A | USD 2.025 billion (S2 page:20) against 2,020,007 USD k (S4 page:10) | Yes | High | Conflicting | Conflict logged | Medium | Remediation Needed |
| Covenant headroom | CP-1, CP-2 | Covenants named without levels (S4 page:19) | Yes | High for the existence statement | Insufficient Information | Not calculable, stated as such | Medium | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal amount of long-term debt 978,793 at 2026-09-30 | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:17, Note 5 Debt | CP-1 Financials and credit metrics | Sourced | High | Term loan 897,750; revolver 20,000; notes 61,043 |
| Cash and cash equivalents 65,786 | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:4, balance sheet | CP-1 liquidity | Sourced | High | |
| Unused commitments 479.2 million | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:32, Liquidity | CP-1 liquidity chart | Sourced | High | Equals 500,000 less 20,000 less 800 |
| Maturity table by year, total 978,793 | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:19, Note 5 | CP-1 maturity chart | Sourced | High | Buckets sum to total |
| Term loan B rate 5.90%, revolver 5.65% | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:17 | CP-1 debt table | Sourced | High | |
| Amortizing notes 5.93%, final installment 2029-02-01, senior unsecured | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:19 | CP-1 debt table | Sourced | High | Indenture not supplied |
| Covenants: maximum Total Net Leverage Ratio, minimum Interest Coverage Ratio, in compliance | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:19 | CP-1 covenants | Sourced | High | No levels |
| TTM Adjusted EBITDA 300,387; TTM Acquisition Adjusted EBITDA 389,234 | source-text/EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | S7 | page:7, net leverage table | CP-1 leverage | Sourced | Medium | Management measures |
| Adjusted EBITDA Q3 2026 107,165; 9M 2026 248,619 | source-text/EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | S7 | page:7 | CP-1 financials | Sourced | Medium | Reconciliation shown |
| Free cash flow Q3 2026 46,619; 9M 2026 (3,415) | source-text/EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | S7 | page:7 | CP-1 financials | Sourced | Medium | Operating cash flow less capital expenditures |
| Operating cash flow 21,284; capital expenditures 24,699; inventory change (148,409) | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:6, cash flow statement | CP-1 cash flow | Sourced | High | |
| Revenue Q3 2026 541,006; repair 318,024; distribution 222,982 | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:4; page:17 | CP-1A operating model | Sourced | High | |
| PAG revenue 173,666 for Q3 2026 | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:11, Note 2 | CP-1, CP-1A | Sourced | High | Upstream handoffs cite page:30 for this figure, which gives USD 173.7 million (logged) |
| PAG consideration headline USD 2.025 billion | source-text/10-Q_2026-03-31_vsec-20260331.htm.jsonl | 10-Q_2026-03-31_vsec-20260331.htm.jsonl | S2 | page:20, Subsequent Events | CP-1A transaction | Sourced | High | Conflicts with accounting consideration |
| Total purchase consideration 2,020,007 USD k | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:10, Note 2 | CP-1A transaction | Sourced | High | |
| Customer group about 20% of FY2025 revenue | source-text/10-K_2025-12-31_vsec-20251231.htm.jsonl | 10-K_2025-12-31_vsec-20251231.htm.jsonl | S1 | page:11, Item 1A; page:70, Note 14 | CP-1A, CP-2 | Sourced | High | FY2025, pre-acquisition |
| Cash paid for interest 26,849 for FY2025 | source-text/10-K_2025-12-31_vsec-20251231.htm.jsonl | 10-K_2025-12-31_vsec-20251231.htm.jsonl | S1 | page:44, supplemental cash flow | CP-1 interest cover | Sourced | High | Only period with cash interest |
| Management guidance: revenue growth 65% to 66.5%; Adjusted EBITDA margin 18.9% to 19.1% | source-text/EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | S7 | page:3 | CP-1 latest quarter; CP-2 | Sourced | Medium | Management statement |
| Term loan B and revolver are senior secured; guarantors named generically | source-text/10-K_2025-12-31_vsec-20251231.htm.jsonl | 10-K_2025-12-31_vsec-20251231.htm.jsonl | S1 | page:81, exhibit list; S4 page:18 | CP-1 debt table | Sourced | High | Legal documents absent; ranking taken from the 10-Q wording only |
| Repair is 58.8% of Q3 2026 revenue | source-text/10-Q_2026-09-30_vsec-20260930.htm.jsonl | 10-Q_2026-09-30_vsec-20260930.htm.jsonl | S4 | page:17 | CP-1A, CP-2 | Calculated | High | 318,024 / 541,006 |
| Atech repairs include sole-source flight-critical components | source-text/EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | EX-99.1_2026-11-04_vse-prxq3x2026earningsrele.htm.jsonl | S7 | page:2 | CP-1A operating model | Sourced | Medium | Management Language, tagged as such upstream |
| Beneficial ownership and sponsor status | Not applicable: no source path | No source file | Source Not Provided | S1 page:79 refers to the proxy statement | CP-1A company profile | Untraced | Low | Correctly tagged Insufficient Information upstream |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt / TTM Adjusted EBITDA, four period-ends | CP-1 chart; CP-2 | Principal 296,250; 366,342; 966,668; 978,793 and TTM 182,924; 198,001; 240,573; 300,387 | Principal / TTM; recomputed 1.62x, 1.85x, 4.02x, 3.26x | Calculated | Verified | High | PD, leverage | S4 page:17; S2 page:12; S3 page:15; S7 page:7; S5 page:6; S6 page:8 |
| Net debt / TTM Adjusted EBITDA | CP-1; CP-2 | Principal less cash; TTM | Recomputed 1.24x (2025-12-31), 3.70x (2026-06-30), 3.04x (2026-09-30); 2026-03-31 not meaningful, cash exceeds debt | Calculated | Verified | High | PD, leverage | as above plus cash from S4 page:4, S3 page:4, S2 page:4 |
| Net debt on management's definition | CP-1 | 978,793 less 18,854 less 65,786 | 894,153, equal to S7 page:7; 894,153 / 300,387 = 2.98x and / 389,234 = 2.30x, printed as 3.0x and 2.3x | Calculated | Verified | High | Definition drift flag | S7 page:7 |
| TTM identity | CP-1 | FY2025 182,924; 9M 2025 131,156; 9M 2026 248,619 | 182,924 - 131,156 + 248,619 = 300,387 | Calculated | Verified | High | Earnings base | S7 page:7 |
| Acquisition-adjusted ratios | CP-1; CP-2 | 389,234 and 370,179 | Recomputed 2.51x and 2.35x; 2.61x and 2.41x | Calculated | Verified arithmetic; input unsupported | Low | Leverage view | S7 page:7; S6 page:8 |
| Liquidity | CP-1; CP-2 | 65,786 + 479,200 | 544,986 | Calculated | Verified | High | Liquidity | S4 page:4; S4 page:32 |
| Contractual annual interest | CP-1; CP-2 | 897,750 x 5.90%; 20,000 x 5.65%; 61,043 x 5.93% | 52,967 + 1,130 + 3,620 = 57,717, before swaps and fee amortization | Calculated | Verified | Medium | Debt service | S4 page:17; S4 page:19 |
| TTM Adjusted EBITDA / contractual interest | CP-1; CP-2 | 300,387 and 389,234 over 57,717 | Recomputed 5.20x and 6.74x | Calculated | Verified | Medium | Coverage | as above |
| Adjusted EBITDA / cash interest FY2025 | CP-1 | 182,924 / 26,849 | Recomputed 6.81x | Calculated | Verified | Medium | Coverage | S7 page:7; S1 page:44 |
| Unhedged floating debt and 100 bp sensitivity | CP-2 | 917,750 less 250,000; 1% | 667,750; 6,678 a year; assumes swaps on 1-month SOFR fully offset the same benchmark | Assumption-Based | Verified arithmetic; assumption flagged | Medium | Rate risk | S4 page:17; S4 page:19 |
| Guidance-implied FY2026 Adjusted EBITDA and year-end leverage | CP-2 | FY2025 revenue 1,112,275; growth 65% to 66.5%; margin 18.9% to 19.1%; net debt 913,007 held flat | 346,863 to 353,720; 2.63x to 2.58x | Assumption-Based | Verified arithmetic; depends on guidance and base | Low | Deleveraging path | S1 page:42; S7 page:3 |
| Secured share, goodwill share, debt to book capitalisation, inventory share | CP-1; CP-1A; CP-2 | Balance sheet lines | 93.8%, 62.6%, 24.7%, 19.9% recomputed | Calculated | Verified | High | Structure | S4 page:4; S4 page:17 |
| Repair, PAG and commercial shares of Q3 2026 revenue | CP-1A | Revenue lines | 58.8%, 32.1% and 98.9% recomputed | Calculated | Verified | High | Business risk | S4 page:4; S4 page:11; S4 page:17 |
| Covenant headroom | CP-1; CP-2 | No levels | Not Calculable from Provided Materials | Not Calculable | Correctly stated | Medium | PD, creditor control | S4 page:19 |
| Metric-definition drift | CP-1; CP-2 | Net debt: management deducts issuance costs, this run does not; EBITDA: management TTM, not credit-agreement EBITDA; Adjusted Net Income definition changed in Q2 2026 | Each is labelled upstream | Flagged | Disclosed | Medium | Comparability | S7 page:5; S6 page:1 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Covenant headroom and structural position | Credit agreement and first amendment absent; levels, guarantors, security Not supplied | Insufficient Information | Creditor control and headroom bound default risk; no headroom claim can be made | Obtain both documents and a covenant certificate | CP-1 covenants table; CP-2 gaps ledger |
| Material | Acquisition-adjusted leverage 2.35x, 2.51x, 6.74x | Pre-acquisition EBITDA has no component schedule | Weak Lineage | The ratios could understate leverage if the add-in is generous | Obtain the schedule or pro forma EBITDA; keep as management-attributed | CP-1 leverage chart notes; CP-2 financial risk table |
| Material | Year-end leverage about 2.6x | Depends on guidance and an assumed revenue base | Assumption-Based | A miss would leave leverage near the filed-basis level | Re-test with FY2026 results | CP-2 key findings 1 |
| Material | Interest cover for 2026 | Cash paid for interest not reported in 2026 reports | Insufficient Information | Cover can be shown for FY2025 only | Obtain 2026 cash interest | CP-1 interest cover chart |
| Material | Acquisition size | Headline and accounting consideration differ without a bridge | Conflicting | Wrong basis changes size comparisons | Obtain the purchase agreement and its amendment | CP-1A conflicts table |
| Material | Customer concentration | FY2025 figure pre-dates the acquisition | Weak Lineage | Current single-name exposure unknown | Obtain post-acquisition disclosure | CP-1A operating model; CP-2 risks |
| Minor | PAG revenue 173,666 | Cited to S4 page:30, where only the rounded USD 173.7 million appears; the figure is at S4 page:11 | Directly Sourced | Locator hygiene | Cite S4 page:11 | CP-1 reconciliation paragraph (accepted, cannot be edited) |
| Minor | Commercial and government revenue split | CP-1A cites S4 page:16; the rows are at S4 page:17 | Directly Sourced | Locator hygiene | Cite S4 page:17 | CP-1A operating model |
| Minor | FY2025 critical audit matter on slow-moving inventory | CP-1A cites S1 page:39; the matter is at S1 page:40 (CP-2 already corrects it) | Directly Sourced | Locator hygiene | Cite S1 page:40 | CP-1A credit translations |
| Minor | Margin terms of the facilities | CP-1 reports that searches for "applicable margin" found only generic statements; S1 page:62 gives the 2025 agreement ranges (term SOFR plus 1.25% to 2.25%; commitment fee 0.20% to 0.30%) | Directly Sourced | The post-amendment grid is still absent, but the sentence overstates the absence | State that only the superseded 2025 ranges are available | CP-1 gaps |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filed or furnished documents cover FY2025 and Q1 to Q3 2026; no legal documents, ratings or market data | Missing legal terms leave structure and creditor control unverified | Headroom and priority claims cannot be tested | Add credit agreement, amendment, seller agreements |
| Citation completeness | Ready with Remediation | All quoted phrases and page locators resolved; three locator slips and one overstated search statement logged | Wrong pages slow verification but do not change figures | Low direct impact; raises review cost | Apply the recorded locator corrections |
| Calculation traceability | Ready with Remediation | Every calculation recomputed and matched; inputs shown; management EBITDA and acquisition-adjusted EBITDA not independently reconcilable | Dependence on management measures can mask leverage | Reported leverage is a management view, not covenant leverage | Obtain EBITDA bridge to the credit agreement definition |
| Assumption transparency | Ready with Remediation | Guidance base, swap offset and net debt definition disclosed upstream | Undisclosed assumptions could be mistaken for facts | Year-end leverage is an estimate | Re-test at FY2026 results |
| Markdown and export artifact integrity | Committee-Ready | Required headings, reader summaries, selectors and source hashes passed the launcher checks for each accepted handoff | A broken envelope would block downstream use | None identified | None required |
| Overall | Ready with Remediation | Lowest of the five dimensions | | | |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Credit agreement and first amendment | Covenant levels, definitions, margins, guarantors, security, distribution limits | Control rights and headroom determine default and loss given default mechanics | Covenant and structure statements in CP-1 and CP-2 | High impact | Executed credit agreement 2025-05-02 and amendment 2026-05-05 |
| CP-5-GAP-002 | Pre-acquisition EBITDA schedule | Components of TTM Acquisition Adjusted EBITDA | Acquisition-adjusted leverage unverifiable | CP-1 leverage chart; CP-2 financial risk | Medium impact | Management bridge or pro forma EBITDA |
| CP-5-GAP-003 | 2026 cash interest and taxes | Cash paid for interest and taxes in 2026 reports | Cash cover cannot be shown beyond FY2025 | CP-1 interest cover chart | Medium impact | Next 10-K or supplemental disclosure |
| CP-5-GAP-004 | PAG consideration bridge | Purchase agreement, first amendment of 2026-05-04 | Two bases for one price | CP-1A conflicts; size comparisons | Medium impact | Purchase agreement documents |
| CP-5-GAP-005 | Customer concentration after the acquisition | Updated concentration disclosure | Revenue durability | CP-1A, CP-2 business risk | Medium impact | Proxy statement or next 10-K |
| CP-5-GAP-006 | Seller agreements | Exchange, registration rights, lock-up, earn-out terms | Share overhang and possible cash earn-out | CP-1A governance; CP-2 risks | Low impact | Exhibits 2.1 to 2.5 listed in the second-quarter 10-Q |
| CP-5-GAP-007 | Fourth-quarter 2026 results and free cash flow | Filed Q4 and FY2026 statements | Year-end leverage is an estimate | CP-2 key findings 1 and 3 | Medium impact | FY2026 10-K |
| CP-5-GAP-008 | Extraction fidelity | Comparison of text conversions with original filings and inline XBRL | Table flattening could misplace a figure | All figures | Low impact | Original filings |
| CP-5-GAP-009 | Ratings, market prices, peers | Not supplied in context | No market check; out of scope for these modules | Monitoring | Low impact | Market data when a relative value module is run |
| CP-5-GAP-010 | Presentation materials for the 2026-11-05 call | Slides and transcript | Management commentary beyond the release | CP-1A, CP-2 management language | Low impact | Investor relations site |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/6cd8c23e091b3696e6965b2178298f1b707a98ac77c3c1db7442200713d0c48f/1.response.md; run vsec-2026-11-05-credit_snapshot-host | Source readiness for seven sources, as of 2026-11-05 | High for filed sources, Medium for releases | Six H2 headings present; readiness view after reader summary | Pass with Remediation | Status READY_WITH_LIMITATIONS; sha256 2cdcc9415abc8726a2bd6013cc3fc6053fad1900f1d23a6661cbe4e6c3b944c9 |
| CP-1 | requests/CP-1/777d8b2e6a16a27ae39110401748ce79fd76e86e3193ce73271f5f41eb254983/1.response.md; run vsec-2026-11-05-credit_snapshot-host | Financial base, FY2025 and Q1 to Q3 2026, USD | High for statements, Medium for management measures | Six H2 headings, four chart selectors and metrics table present | Pass with Remediation | One locator slip (PAG revenue page) and one overstated search statement; sha256 0ce2ba0d41587fd6984e42432ff1f87478ce6e2541bbe874409fd590811a2170 |
| CP-1A | requests/CP-1A/3e95acf0d37fbee878c119934804fc83bcf94e9faf2dd0be0ccd0d68605d5f5c/1.response.md; run vsec-2026-11-05-credit_snapshot-host | Business, transaction, ownership and governance context | High for filed facts, Medium for management language | Six H2 headings, three selectors present | Pass with Remediation | Two locator slips (commercial revenue page, audit matter page); sha256 bbe5dabc3d375b69ee76ab844cf013f38bda2f0326a4a2247d2db1ff3e9b86f4 |
| CP-2 | requests/CP-2/0144ba9cbc65a319f1e014d5d340992b103cce35fb9d3a85d2a3fd9c2967cc04/1.response.md; run vsec-2026-11-05-credit_snapshot-host | Fundamental credit view | Derived from the upstream handoffs | Six H2 headings, two selectors present | Pass with Remediation | Guidance-implied leverage is Assumption-Based; sha256 a8a1ab8afd1514757a3bb5aa4b4cd16d01a6b93effbaf65a791adfe4044700b1 |

Re-anchored values consumed: issuer VSE Corporation (issuer id vsec); as-of 2026-11-05; current period Q3 2026, prior period FY2025; principal debt 978,793 and 296,250 (USD k); cash 65,786 and 69,358; TTM Adjusted EBITDA 300,387 and 182,924; unused commitments 479.2 million; liquidity 544,986 (USD k).

#### T5.2 Citation and evidence-support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Reconciliation paragraph: PAG contributed 173,666 of Q3 2026 revenue | Supported | Cited to S4 page:30, which prints USD 173.7 million; the thousands figure is at S4 page:11 | Cite S4 page:11 | Formatting / Hygiene Only |
| Minor | CP-1A | Operating model row: commercial 535,080 and government 5,926 | Supported | Cited to S4 page:16; the rows are at S4 page:17 | Cite S4 page:17 | Formatting / Hygiene Only |
| Minor | CP-1A | Credit translation: inventory write-down was a critical audit matter | Supported | Cited to S1 page:39; the matter is at S1 page:40 | Cite S1 page:40 (CP-2 already corrects this) | Formatting / Hygiene Only |
| Minor | CP-1 | Gaps: "applicable margin" found only in generic statements | Partially Supported | S1 page:62 gives 2025 agreement margin ranges, superseded for the term loan | Say only the superseded ranges are available | Monitoring Follow-Up |
| Material | CP-1A, CP-2 | Customer group about 20% of revenue | Partially Supported | FY2025 pre-acquisition figure carried into a 2026 credit view | Label as FY2025 wherever used; seek update | Restricts Committee Use |
| Material | CP-2 | Year-end leverage about 2.6x | Partially Supported | Depends on guidance and an assumed revenue base | Keep tagged Assumption-Based; re-test at FY2026 results | Restricts Committee Use |
| Material | CP-1, CP-2 | Acquisition-adjusted ratios | Partially Supported | No component schedule for pre-acquisition EBITDA | Keep as management-attributed | Requires Source Reconciliation |
| Minor | CP-0, CP-1, CP-1A, CP-2 | All other quoted phrases and page locators | Supported | None: every quoted phrase was found on its cited page and every page locator exists | None | Monitoring Follow-Up |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Net debt differs by definition | Management deducts issuance costs (894,153); this run uses principal less cash (913,007); both labelled | None between sources; definitional | Keep both labels wherever net debt is quoted | Monitoring Follow-Up |
| Material | CP-1, CP-2 | EBITDA is a management TTM measure | Not the credit-agreement EBITDA; covenant definition not supplied | S7 page:5 says the measures differ from the credit agreement definition | Do not read leverage as covenant leverage | Restricts Committee Use |
| Minor | CP-2 | 100 bp sensitivity and hedge ratio | Swaps reference 1-month SOFR while the loans may reset on 1, 3 or 6 month Term SOFR (S4 page:19; S4 page:32); full offset is assumed | None | Keep the assumption stated | Monitoring Follow-Up |
| Minor | CP-1 | Interest cover chart mixes bases | FY2025 cash basis; 2026 rows Not supplied; expense and contractual-rate substitutes sit in the basis column | None | Keep substitutes labelled as not cash | Monitoring Follow-Up |
| Minor | CP-1, CP-1A, CP-2 | Recomputation of every calculation | Inputs, formula and result reproduced for the registers above; all matched within rounding | None | None | Monitoring Follow-Up |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Term loan B and revolver are senior secured; amortizing notes are senior unsecured, so secured lenders rank ahead | Credit agreement, security documents, note indenture | Wording comes from the 10-Q only; no clause-level support for ranking, security scope or guarantor coverage | Describe as the registrant's statement; obtain documents | Legal review required before any ranking conclusion |
| Material | CP-1, CP-2 | Covenants exist and were met | Credit agreement and compliance certificate | Levels, definitions and step-downs absent | Keep headroom Not Calculable | Legal review required |
| Material | CP-1A | Seller exchangeable shares, lock-up, registration rights, earn-out in cash or equity at the Company's discretion | Exchange and redemption agreement, registration rights agreement, lock-up agreements, purchase agreement amendment | Only exhibit listings and the 10-Q summary | Keep tagged Insufficient Information for terms | Legal review required |
| Minor | CP-2 | No recovery conclusion is drawn | Not required | None; the prohibition was respected | None | Monitoring Follow-Up |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1A, CP-2 | No price, spread, yield, rating, peer or relative-value claim is made upstream | Ratings, prices, spreads and peer data are not in the context | None for the current scope; the modules correctly state this | None now; add when a relative-value module is run | Monitoring Follow-Up |

#### T5.6 Cross-module consistency and version-control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-0, CP-1A, CP-2 | PAG consideration: USD 2.025 billion headline (S2 page:20) against 2,020,007 USD k accounting consideration (S4 page:10); cash USD 1.750 billion against 1,770,370 USD k; 16,628 USD k unexplained between 2.025 billion and cash plus equity | Different documents and dates; logged consistently in CP-0 and CP-1A, repeated in CP-2 | Obtain the purchase agreement and amendment; quote basis with every size | Size comparisons restricted |
| Minor | CP-1A, CP-1 | Term loan A versus B: the 10-K commitment-stage text (S1 page:74) differs from the executed term loan B (S4 page:18) | Superseded by the executed amendment | Use S4 for terms | None |
| Minor | CP-1, CP-1A | Aero 3 consideration USD 346.4 million (S2 page:8) against USD 346.1 million (S4 page:13) | Measurement-period working capital settlement | Use the latest filed figure | None |
| Minor | CP-1, CP-2 | Leverage, liquidity and maturity figures | Identical across CP-1 and CP-2 (3.26x, 3.04x, 1.24x, 545.0, 62.6%, 93.8%) | None | None |
| Minor | CP-1, CP-5 | Adjusted EBITDA definition and Adjusted Net Income definition changed between the first and later 2026 releases (S6 page:1) | Later releases restate prior periods | Do not compare Q1 2026 adjusted net income with later quarters | Comparability |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A, CP-2 | Duplicative content | The missing credit agreement and the concentration caveat are repeated in several sections | State once where it changes a conclusion in the final report | Formatting / Hygiene Only |
| Minor | CP-1 | Immaterial detail | The long metrics table mixes reported and calculated rows; a reader must use the basis column to tell them apart | Keep the basis column; consider splitting in the report | Formatting / Hygiene Only |
| Minor | CP-2 | Promotional language | Management characterisations (record results, sole-source repairs) appear only as Management Language | None | Monitoring Follow-Up |
| Material | CP-2 | Committee readiness | The credit view is usable with restrictions: covenant headroom Not supplied, guidance-based and management-EBITDA-based ratios flagged | Present restrictions with the view | Restricts Committee Use |

#### T5.8 Structured export, master index and evidence-trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A, CP-2 | Required H2 headings, reader summary, opening H3, source hashes, handoff hashes | None: all present and accepted by the launcher | None | Grounds this handoff |
| Minor | CP-1 | Chart tables | All four chart tables passed the plain-number or Not supplied rule | None | Feeds the report strip |
| Minor | All | Locators | Page locators are chunk numbers, not printed pages, as stated in each handoff | Keep the statement in the report | Reader needs the converted text to open a locator |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-1, CP-1A, CP-2 | Legal Support Gap | Credit agreement and first amendment absent; covenant levels, guarantors, security not traceable | Supply documents | Restricts Committee Use | Open |
| CP5-002 | Material | CP-1, CP-2 | Source Quality Limitation | Acquisition-adjusted EBITDA has no schedule | Supply schedule | Requires Source Reconciliation | Open |
| CP5-003 | Material | CP-2 | Partially Supported Claim | Year-end leverage about 2.6x rests on guidance and an assumed base | Re-test at FY2026 results | Restricts Committee Use | Open |
| CP5-004 | Material | CP-1 | Citation Gap | 2026 cash interest absent | Supply cash interest | Requires Source Reconciliation | Open |
| CP5-005 | Material | CP-0, CP-1A, CP-2 | Conflicting Evidence | PAG consideration headline against accounting figure | Supply purchase agreement | Requires Source Reconciliation | Open |
| CP5-006 | Material | CP-1A, CP-2 | Partially Supported Claim | Customer concentration is a FY2025 figure | Supply update | Restricts Committee Use | Open |
| CP5-007 | Minor | CP-1 | Citation Gap | PAG revenue 173,666 cited to S4 page:30; correct page is page:11 | Cite page:11 | Formatting / Hygiene Only | Open: accepted answer not editable; correction recorded here |
| CP5-008 | Minor | CP-1A | Citation Gap | Commercial and government revenue cited to S4 page:16; correct page is page:17 | Cite page:17 | Formatting / Hygiene Only | Open: correction recorded here |
| CP5-009 | Minor | CP-1A | Citation Gap | Audit matter cited to S1 page:39; correct page is page:40 | Cite page:40 | Formatting / Hygiene Only | Resolved in CP-2; recorded here |
| CP5-010 | Minor | CP-1 | Partially Supported Claim | Search statement on margin terms overlooks the 2025 ranges at S1 page:62 | Reword | Monitoring Follow-Up | Open |
| CP5-011 | Minor | CP-1, CP-2 | Formula / Definition Drift | Net debt definition differs between management and this run | Keep both labels | Monitoring Follow-Up | Open: disclosed |
| CP5-012 | Minor | CP-2 | Formula / Definition Drift | Swap benchmark and loan reset tenor assumed to offset fully | Keep assumption stated | Monitoring Follow-Up | Open: disclosed |
| CP5-013 | Minor | All | Source Quality Limitation | Text conversions not compared with original filings | Compare before committee use | Monitoring Follow-Up | Open |

#### Remediation priority and clearance decision

Priority order: first the credit agreement, amendment and covenant certificate (CP5-001), then the purchase agreement bridge (CP5-005), the pre-acquisition EBITDA schedule (CP5-002), 2026 cash interest (CP5-004), post-acquisition concentration (CP5-006), the FY2026 results re-test (CP5-003), then the locator and wording fixes (CP5-007 to CP5-013). Clearance decision: Pass with Remediation. No upstream conclusion is changed. The upstream credit view may be used by a committee only with the restrictions in the issue log.

## Calculations

Each calculation in the four upstream handoffs was recomputed from the cited inputs (USD thousands unless stated). All matched the upstream figure.

| Calculation | Inputs | Recomputed result | Upstream figure | Match |
| --- | --- | --- | --- | --- |
| Total debt / TTM Adjusted EBITDA | 296,250 / 182,924; 366,342 / 198,001; 966,668 / 240,573; 978,793 / 300,387 | 1.62x; 1.85x; 4.02x; 3.26x | 1.62; 1.85; 4.02; 3.26 | Yes |
| Net debt / TTM Adjusted EBITDA | (296,250 - 69,358) / 182,924; (966,668 - 75,360) / 240,573; (978,793 - 65,786) / 300,387 | 1.24x; 3.70x; 3.04x | 1.24; 3.70; 3.04 | Yes |
| Acquisition-adjusted ratios, 2026-09-30 | 978,793 / 389,234; 913,007 / 389,234 | 2.51x; 2.35x | 2.51; 2.35 | Yes |
| Acquisition-adjusted ratios, 2026-06-30 | 966,668 / 370,179; 891,308 / 370,179 | 2.61x; 2.41x | 2.61; 2.41 | Yes |
| Management net debt | 978,793 - 18,854 - 65,786 | 894,153 | 894,153 | Yes |
| TTM identity | 182,924 - 131,156 + 248,619 | 300,387 | 300,387 | Yes |
| Maturity buckets | 7,958 + 32,691 + 34,128 + 15,516 + 29,000 + 9,000 + 850,500 | 978,793 | 978,793 | Yes |
| Liquidity | 65,786 + (500,000 - 20,000 - 800) | 544,986 | 544,986 | Yes |
| Contractual annual interest | 52,967 + 1,130 + 3,620 | 57,717 | 57,717 | Yes |
| Covers | 300,387 / 57,717; 389,234 / 57,717; 182,924 / 26,849; 107,165 / 14,097 | 5.20x; 6.74x; 6.81x; 7.60x | same | Yes |
| Unhedged floating debt and sensitivity | 917,750 - 250,000; 667,750 x 1% | 667,750; 6,678 | same | Yes |
| Guidance-implied EBITDA and leverage | 1,112,275 x 1.65 x 18.9%; 1,112,275 x 1.665 x 19.1%; 913,007 / each | 346,863; 353,720; 2.63x; 2.58x | same | Yes |
| Shares of revenue and assets | 318,024 / 541,006; 173,666 / 541,006; 535,080 / 541,006; (917,750 / 978,793); (1,853,509 + 950,496) / 4,479,958; 893,006 / 4,479,958 | 58.8%; 32.1%; 98.9%; 93.8%; 62.6%; 19.9% | same | Yes |
| Counts for the traceability view | Top 5 drivers classified in the traceability map: Directly Sourced (ranks 2, 3, 5), Calculated (ranks 1, 4) | 3 and 2, with 0 in each remaining class | as stated | Yes |
| Issue log counts | Material: CP5-001 to CP5-006; Minor: CP5-007 to CP5-013 | 6 Material, 7 Minor, 0 Critical | as stated | Yes |

## Gaps

The gaps ledger is the register headed T5B.8 above. The limitations that matter most to committee use are: the credit agreement and its first amendment are not supplied (CP-5-GAP-001); acquisition-adjusted earnings have no schedule (CP-5-GAP-002); 2026 cash interest is not reported (CP-5-GAP-003); the acquisition price is stated on two bases (CP-5-GAP-004); and the sources are text conversions not compared with the originals (CP-5-GAP-008). The numeric confidence script and the mechanical completeness script were not run, so no numeric score is asserted. Nothing dated after the 2026-11-05 cutoff is used as fact, and all figures are USD.

## Next module

This is the last module of the run. The report should present the upstream credit view with the restrictions in the issue log, apply the three locator corrections and the margin-terms wording fix when the report is assembled, quote each acquisition size with its basis, and treat covenant headroom as not supplied until the credit agreement and its first amendment are provided.
