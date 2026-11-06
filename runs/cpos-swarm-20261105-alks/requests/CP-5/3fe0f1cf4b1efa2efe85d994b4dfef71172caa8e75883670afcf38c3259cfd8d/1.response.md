## Request

Evidence trace validation and research integrity grade (the absorbed QA phase) for Alkermes plc. as of 2026-11-05, pathway credit_snapshot, current period Q3 2026, prior period FY2025, USD. Scope: the four accepted handoffs (source readiness, financial base, business and transaction context, fundamental credit synthesis), traced to the seven pinned issuer sources, with Top 5 traceability. Source text was re-read for this audit; the key locators were opened and every derived figure below was recomputed.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_alks-20251231.htm.jsonl | e4cb39ef2746983905a66c4851e17231fe0e2b3eb3dd9d346653644971686601 |
| 10-Q_2026-03-31_alks-20260331.htm.jsonl | 2f002a6c3ee21ba1a12ed08afd7616a7de0cb6e62154bfb1ecb118ba4eafd45f |
| 10-Q_2026-06-30_alks-20260630.htm.jsonl | bc67cf08c7dfc8de310d0ecdd1030e2a1391c6b7ce68e53f0b348219bcf79e99 |
| 10-Q_2026-09-30_alks-20260930.htm.jsonl | df6328c67d9ab03d30760e47eacac03760e7e83fb341e7073082128f2c7068d4 |
| EX-99.1_2026-05-05_alks-ex99_1.htm.jsonl | 3f53152d2ff381e382b1d7a092db23f6a1d1dce5883995e4eda0a38a2d5d57a8 |
| EX-99.1_2026-07-28_alks-ex99_1.htm.jsonl | 4e5567773d88766be4958174400b81baacad01bd80fe607c8eb27ade6994b31f |
| EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl | 041cf8e725b3d45a5b701a4d1acae145f94c2d37b75244f3f5fe173ac5392fc6 |

Run context (not issuer evidence): context sha256 885addee0d736fc42d87bc797174ed4ac35a16798074c06e23b1959b2f8975fb.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 1c390a89aa7513afef7abe9931b091489b79fa424d2c8a557db08f15d5e4f8c2 | Source readiness, gap and conflict log |
| CP-1 | ba17ec3b21ea8b787a38b6115fd45721db003c4757249d4451fa745fd7eb5b34 | Financial base, charts, calculations |
| CP-1A | fb57077c42cf725224dc0c8dd52e411550d0fe38c0bf9122107c7138f80a50f8 | Business, transaction, governance rows |
| CP-2 | c0bff421779f3c8762b0e06b69537ba62d8500f3b7030bd82ce75784ffef90db | Credit synthesis |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The upstream conclusions trace to filed sources and every ratio recomputes, but one page reference is wrong, one statement about buybacks is unsupported, and covenant headroom cannot be tested. Committee use is restricted. | Medium | The credit agreement is missing and FY2025 Adjusted EBITDA is derived, so leverage and headroom stay provisional. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All recomputed figures reproduce, including 3.40 times debt to Adjusted EBITDA, 1.61 times net, 89.1% of principal due in 2031 and free cash flow of 227.4 US$m. | Quantitative claims in the credit view can be relied on. | High |
| Leverage on Adjusted EBITDA uses a derived FY2025 base; without the 10.0 US$m add-back it would be 3.48 times. | The estimate is sensitive but not materially so. | Medium |
| The statement that buybacks stopped after the term loans were drawn is not supported; sources show none in Q2 or Q3 2026. | Distribution behaviour is slightly less well documented than stated. | Medium |
| Covenant levels, guarantors and any revolver cannot be traced because the credit agreement is not supplied. | Default triggers and liquidity access remain unverified. | High |
| A page reference for FY2025 depreciation and share-based compensation points to page 168 instead of 167. | Minor trace defect; figures themselves are correct. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 3 are directly sourced, 0 are calculated, 1 is assumption-based, 0 are analyst inferences, and 1 is a weak-lineage, untraced, conflicting, or insufficient-information item. The most important provenance gap is the executed credit agreement and its amendment, which matters because covenant levels, guarantors, baskets and any revolver decide default triggers and liquidity access and imply that committee use must stay restricted until the documents are obtained.

The quality grade is Restricted because there are no Critical findings but there are Material ones (the covenant evidence gap and the add-back dependence of the Adjusted EBITDA leverage figure). A numeric confidence score is not asserted: the scoring routine is script-owned and was not available in this host run. The confidence band for the handoffs taken together is Medium.

### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_alks-20251231.htm.jsonl | High (audited, filed) | FY2025 with FY2024 and FY2023 | Alkermes plc and subsidiaries, consolidated | Statements, notes, business, patents, customers | Pre-acquisition; ownership data incorporated from a proxy not supplied | Financial base, business rows |
| S2 | 10-Q_2026-03-31_alks-20260331.htm.jsonl | High (filed, unaudited) | Q1 2026 | Same | Statements, original term loan terms | Superseded for debt terms by S4 | Quarterly balances |
| S3 | 10-Q_2026-06-30_alks-20260630.htm.jsonl | High (filed, unaudited) | Q2 and six months 2026 | Same | Statements, balance sheet | Cumulative cash flow only | Quarterly balances, subtraction inputs |
| S4 | 10-Q_2026-09-30_alks-20260930.htm.jsonl | High (filed, unaudited) | Q3 and nine months 2026 | Same | Statements, debt note, maturities, litigation, subsequent events | Credit agreement not attached | Debt, liquidity, transaction |
| S5 | EX-99.1_2026-05-05_alks-ex99_1.htm.jsonl | Medium (furnished release, management measures) | Q1 2026 | Same | EBITDA and Adjusted EBITDA reconciliation | Management non-GAAP | Adjusted EBITDA quarters |
| S6 | EX-99.1_2026-07-28_alks-ex99_1.htm.jsonl | Medium (furnished release) | Q2 and six months 2026 | Same | Reconciliations, 2026 expectations | Guidance is forward-looking | Adjusted EBITDA, outlook |
| S7 | EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl | Medium (furnished release) | Q3 and nine months 2026 | Same | Reconciliations, product sales, cash and investments | Management non-GAAP | Adjusted EBITDA, liquidity |
| H0 | CP-0 handoff | Medium (analyst work product) | As of 2026-11-05 | Same | Readiness, gaps | Source readiness only | Gap carry-forward |
| H1 | CP-1 handoff | Medium (analyst work product with derived figures) | FY2025 to Q3 2026 and LTM | Same | Financial figures, charts | FY2025 Adjusted EBITDA derived | Credit synthesis |
| H2 | CP-1A handoff | Medium (analyst work product) | As of 2026-11-05 | Same | Business, transaction, governance | Ownership data not supplied | Credit synthesis |
| H3 | CP-2 handoff | Medium (analyst work product) | As of 2026-11-05 | Same | Credit view, risks | Upstream only | Committee use |

Module Status: Ready with Limitations (all four handoffs and all seven sources available; credit agreement and proxy absent). Traceability Scope: Top 5. Entity key: issuer_id alks available. Re-anchor: each handoff names Alkermes plc., the as-of date 2026-11-05, current period Q3 2026 and prior period FY2025; CP-1, CP-1A and CP-2 list the upstream hashes above and they match the run record.

### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage of 3.40x total debt and 1.61x net debt on LTM Adjusted EBITDA of 440.2 US$m (10.25x and 4.86x on reported EBITDA of 146.2 US$m) | CP-1, restated in CP-2 | Debt on the balance sheet and management EBITDA reconciliations | Add-backs drive the gap between measures; affects leverage tolerance and default risk | Defines how much earnings cushion supports the debt | S4 page:6 and page:27; S7 page:6; S1 pages:166-167 | FY2025 Adjusted EBITDA derived; no covenant definition |
| 2 | Debt of 1,497.7 US$m, senior secured term loans, with 89.1% of principal due in 2031 | CP-1, CP-2 | Debt note and maturity table | Back-ended maturities set the refinancing point and small amortization eases debt service | Refinancing and debt service | S4 pages:27-30 and page:55 | Margin grid and guarantors not supplied |
| 3 | Liquidity of 787.6 US$m of cash and investments, no revolver found | CP-1, CP-2 | Balance sheet and release | Main source of repayment capacity and buffer against 2027 volume changes | Liquidity | S4 pages:5-6; S7 page:2 | Revolver absence is a finding of searched text |
| 4 | VIVITROL at 31.7% of FY2025 revenue with generic entry expected in 2027 | CP-1A, CP-2 | Product net sales and company expectation | A large, mature product may lose volume and price while debt remains | Revenue durability | S1 page:131 and page:166 | Product margins not supplied |
| 5 | Covenant package: maintenance tests named, levels not supplied | CP-0, CP-1, CP-2 | Debt note statement of compliance | Decides default triggers and amendment risk | Monitoring posture | S4 page:28 and page:30 | Executed credit agreement absent |

### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 3.40x and 1.61x on LTM Adjusted EBITDA | CP-1 | Debt 1,497,731 thousand (S4 page:6); Adjusted EBITDA nine months 339,544 and 293,658 (S7 page:6); FY2025 base derived from S1 plus a 10.0 million cost (S1 page:130) | Yes | High for debt, Medium for EBITDA | Assumption-Based | Supported with qualification | Medium | Remediation Needed |
| Debt 1,497.7 US$m secured; 89.1% due in 2031 | CP-1 | Term loan table and maturity schedule (S4 pages:27 and 29); security statement (S4 page:28) | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Liquidity 787.6 US$m | CP-1 | 631,314 + 124,150 + 32,110 (S4 pages:5-6); "$787.6 million" (S7 page:2) | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| VIVITROL 31.7% of FY2025 revenue; generic entry expected 2027 | CP-1A | 467.9 US$m (S1 page:131) over 1,475,899 thousand (S1 page:166); "we expect generic versions of VIVITROL to enter the market in 2027" (S1 page:131) | Yes | High | Directly Sourced | Supported; company expectation | Medium | Committee-Ready |
| Covenant headroom | CP-0, CP-1, CP-2 | Levels "set forth in the Credit Agreement" (S4 page:28); no document | Yes | High for the statement | Insufficient Information | Not testable | Low | Not Traceable |

### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 1,497.7 US$m (26.5 current plus 1,471.2 long-term) | Balance sheet | 10-Q_2026-09-30_alks-20260930.htm.jsonl | S4 | page:6 | CP-1 Debt and capital structure | Sourced | High | Ties to term loan table at page:27 |
| Term Loan A 735.0 and Term Loan B 762.7 US$m | Note 12 | 10-Q_2026-09-30_alks-20260930.htm.jsonl | S4 | page:27 | CP-1 Debt and capital structure | Sourced | High | Carrying amounts |
| Scheduled principal 1,511.750 US$m by year | Note 12 | 10-Q_2026-09-30_alks-20260930.htm.jsonl | S4 | page:29 | CP-1 maturities chart | Sourced | High | Thereafter assigned to 2031 by inference |
| Facilities borrowed in full at 1.525 billion | Note 11 | 10-K_2025-12-31_alks-20251231.htm.jsonl | S1 | page:193 | CP-1 Debt and capital structure | Sourced | High | Also in S2 page:23 |
| Cash 631.3, short-term investments 124.2, long-term investments 32.1 US$m | Balance sheet | 10-Q_2026-09-30_alks-20260930.htm.jsonl | S4 | pages:5-6 | CP-1 Liquidity | Sourced | High | Release states 787.6 |
| Nine-month 2026 cash from operations 72.9 US$m versus 350.7 US$m | Cash flow statement | 10-Q_2026-09-30_alks-20260930.htm.jsonl | S4 | page:7 | CP-1 Cash flow quality | Sourced | High | |
| Nine-month Adjusted EBITDA 339.5 and 293.7 US$m | Reconciliation | EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl | S7 | page:6 | CP-1 Financial table | Sourced | Medium | Management measure |
| FY2025 depreciation and amortization 27,165 and share-based compensation 98,716 thousand | Cash flow statement | 10-K_2025-12-31_alks-20251231.htm.jsonl | S1 | page:167 | CP-1 Calculations 1 and 2 | Sourced | High | CP-1 cites page:168 for these items; page:168 holds operating cash flow and capex |
| FY2025 Adjusted EBITDA 394.3 US$m | Derived | S1 pages:166-167 and page:130; S7 page:6 | S1, S7 | CP-1 Calculations 2 | CP-1 Financial table | Calculated with assumption | Medium | Uses "approximately $10.0 million" of Avadel costs |
| Cost of about 10.0 US$m for Avadel in the fourth quarter of 2025 | MD&A | 10-K_2025-12-31_alks-20251231.htm.jsonl | S1 | page:130 | CP-1 Calculations 2 | Sourced | High | Stated in millions |
| VIVITROL generic entry expected in 2027 | MD&A | 10-K_2025-12-31_alks-20251231.htm.jsonl | S1 | page:131 | CP-1A Credit translations | Sourced | High | Company expectation |
| Wholesaler shares of gross sales (VIVITROL 38%, 15%, 18%) | Business | 10-K_2025-12-31_alks-20251231.htm.jsonl | S1 | page:27 | CP-1A Operating model | Sourced | High | |
| Janssen 9%, 17%, 31% and Biogen 9% of revenues | Business | 10-K_2025-12-31_alks-20251231.htm.jsonl | S1 | pages:20 and 22 | CP-1A Operating model | Sourced | High | |
| Purchase consideration 2,306.9 US$m, cash 2,199.2 US$m | Note 3 | 10-Q_2026-09-30_alks-20260930.htm.jsonl | S4 | page:16 | CP-1A Transaction | Sourced | High | Preliminary allocation |
| CVR up to 165.7 US$m, carried 136.9 US$m, probability raised 75% to 90% | Notes 3, 6, 18 | 10-Q_2026-09-30_alks-20260930.htm.jsonl | S4 | pages:6, 24 and 53 | CP-1, CP-1A | Sourced | High | |
| Buybacks 27.7 US$m in Q1 2026, none in Q2 or Q3, 172.3 US$m remaining | Note 13 | 10-Q_2026-09-30_alks-20260930.htm.jsonl | S4 | page:30 | CP-1A Governance | Sourced | High | CP-1A adds that purchases stopped after the loans were drawn; the source does not date the Q1 purchases |
| Interest rate collars of 375.0 US$m each, entered in October 2026 | Note 12 | 10-Q_2026-09-30_alks-20260930.htm.jsonl | S4 | page:30 | CP-1 Debt | Sourced | High | Subsequent event |
| Guaranteed by subsidiary guarantors and secured on substantially all assets | Note 12 | 10-Q_2026-09-30_alks-20260930.htm.jsonl | S4 | page:28 | CP-1 Debt, CP-2 | Sourced | High | Guarantors unnamed |
| Maintenance covenants named; levels in the Credit Agreement | Note 12 | 10-Q_2026-09-30_alks-20260930.htm.jsonl | S4 | page:28 | CP-0, CP-1, CP-2 | Sourced | High | Executed document absent |
| Credit view: moderately leveraged, adequate liquidity | Synthesis | CP-1 and CP-1A handoffs | H1, H2 | Credit view | CP-2 | Inference | Medium | Analyst Interpretation labelled in CP-2 |

### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FY2025 EBITDA 285,588 thousand | CP-1 | Net income 241,664; interest income 45,304; interest expense 12,277; tax 49,786; D&A 27,165 | Net income less interest income plus interest expense plus tax plus D&A, recomputed 285,588 | Calculated | Reproduced | High | Leverage | S1 pages:166-167 |
| FY2025 Adjusted EBITDA 394,304 thousand | CP-1 | EBITDA 285,588; share-based compensation 98,716; Avadel costs about 10,000 | Sum of the three | Assumption-Based | Reproduced; the 10,000 is rounded | Medium | Leverage | S1 pages:130, 167 |
| LTM EBITDA 146,169 and LTM Adjusted EBITDA 440,190 thousand | CP-1, CP-2 | FY2025 plus nine months 2026 less nine months 2025 | 285,588 + 81,798 - 221,217; 394,304 + 339,544 - 293,658 | Calculated | Reproduced; quarterly cross-check 100,646 + 80,261 + 139,218 + 120,065 = 440,190 | Medium | Leverage | S7 page:6; S5 page:6; S6 page:7 |
| Total debt / LTM Adjusted EBITDA 3.40x; net 1.61x | CP-1, CP-2 | Debt 1,497,731; net debt 710,157; LTM Adjusted EBITDA 440,190 | 1,497,731 / 440,190 = 3.402; 710,157 / 440,190 = 1.613 | Calculated | Reproduced | Medium | Leverage tolerance | S4 pages:5-6 |
| Total debt / LTM reported EBITDA 10.25x; net 4.86x | CP-1, CP-2 | Same debt; LTM EBITDA 146,169 | 1,497,731 / 146,169 = 10.247; 710,157 / 146,169 = 4.858 | Calculated | Reproduced | High | Leverage | S4, S7 |
| Adjusted EBITDA / interest expense LTM 5.08x, Q3 4.36x | CP-1, CP-2 | LTM interest expense 86,645; Q3 27,551 | 440,190 / 86,645 = 5.080; 120,065 / 27,551 = 4.358 | Calculated | Reproduced; expense basis, not cash | Medium | Coverage | S4 page:6, S1 page:166 |
| LTM free cash flow 227.4 US$m; 15.2% of debt | CP-1, CP-2 | CFO 242,986; capex 15,618 | 242,986 - 15,618 = 227,368; 227,368 / 1,497,731 = 15.18% | Calculated | Reproduced | High | Debt service capacity | S1 page:168, S4 page:7, S3 page:7 |
| 89.1% of principal due in 2031; 164.2 US$m due before | CP-2 | 1,347.562 of 1,511.750 | 1,347.562 / 1,511.750 = 89.14% | Calculated | Reproduced | High | Refinancing | S4 page:29 |
| Product shares: VIVITROL 31.7%, ARISTADA 25.1%, LYBALVI 23.5%; LUMRYZ 16.5% of nine-month 2026 revenue | CP-1A | 467.9, 370.0, 346.7 over 1,475.9; 226.0 over 1,369.1 | Division | Calculated | Reproduced | High | Concentration | S1 page:131, S7 page:1 |
| Leverage sensitivity: 3.78x at minus 10% and 4.25x at minus 20% Adjusted EBITDA | CP-2 | 1,497.731 over 396.171 and 352.152 | Division | Calculated, illustrative | Reproduced | Medium | Leverage tolerance | CP-1 figures |
| Assumption: Q4 2025 Avadel cost of 10.0 US$m is the only FY2025 non-recurring add-back | CP-1 | 10-K text and the absence of acquisition costs in nine months 2025 | Judgement | Assumption-Based | Plausible, not company-confirmed | Medium | Leverage | S1 page:130; S7 page:6 |

### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Adjusted EBITDA leverage of 3.40x | FY2025 Adjusted EBITDA is not printed in the pack and rests on a rounded cost | Assumption-Based | The leverage multiple is the main quantitative anchor of the credit view; without the 10.0 US$m add-back it would be 3.48x | Obtain the Q4 2025 release; keep the label derived | CP-1 financial table, CP-2 credit view |
| Material | Covenant headroom and compliance | Levels and definitions not in the pack | Insufficient Information (covenant evidence) | Default triggers and amendment risk cannot be sized | Add the executed credit agreement and Amendment No. 1 | CP-1 gaps, CP-2 risks |
| Minor | Buybacks stopped after the term loans were drawn | Source shows no purchases in Q2 and Q3 but does not date the Q1 purchases | Weak Lineage | Overstates documented distribution behaviour | Replace with "none in Q2 or Q3 2026"; CP-2 already does so | CP-1A Ownership, governance and capital allocation row |
| Minor | FY2025 depreciation and share-based compensation locators | Cited at page:168 but located at page:167 | Weak Lineage | Impairs the audit trail only | Cite page:167 | CP-1 Calculations 1 and 2 |
| Minor | Janssen share row labelled as a conflict | Both spans agree on a declining royalty share | Weak Lineage | Presentation noise in the conflict log | Move to notes | CP-1A conflicts table |

### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2025 to Q3 2026; credit agreement, proxy and Q4 2025 release absent | Missing governing documents leave covenant and control terms unverified | Default risk and sponsor behaviour are bounded by gaps | Add the credit agreement, amendment and proxy |
| Citation completeness | Ready with Remediation | Nearly all statements carry file and page; one page reference is wrong and one claim is unsupported | Small trace defects reduce reliance on single rows | No change to the credit conclusion | Correct the two items in any restatement |
| Calculation traceability | Committee-Ready | All 11 register items recompute from cited inputs, with formulas shown | Reproducible arithmetic limits error risk | Quantitative claims hold | Keep derived labels |
| Assumption transparency | Ready with Remediation | The 10.0 US$m add-back and the thereafter-maturity assignment are labelled as derived or inferred | A hidden assumption could shift leverage by 0.08x | Leverage is stated with its basis | Obtain the Q4 2025 release |
| Markdown artifact integrity | Committee-Ready | Required headings, source hashes and handoff hashes present in all four handoffs | Structure supports downstream consumption | None | None |

Overall auditability is the lowest of the five dimensions: Ready with Remediation.

### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Covenant levels, definitions, grid and guarantors | Executed Credit Agreement and Amendment No. 1 | Decides default triggers, distribution capacity and the meaning of leverage | Credit view, risks | High impact | Credit agreement exhibits |
| CP-5-GAP-002 | FY2025 Adjusted EBITDA is derived | Q4 2025 earnings release | The 3.40x multiple inherits an approximation | Leverage chart | Medium impact | Q4 2025 earnings release |
| CP-5-GAP-003 | Cash interest paid not shown for 2026 | Supplemental cash flow disclosure | Coverage is on an expense basis | Interest cover chart | Medium impact | Q4 2026 filing or company disclosure |
| CP-5-GAP-004 | Ownership, board and large holders | 2026 proxy statement | Control and alignment cannot be assessed | Governance rows | Medium impact | Proxy statement |
| CP-5-GAP-005 | Product-level margins for VIVITROL and LUMRYZ | Segment or product profitability | Cash flow effect of 2027 generic entry cannot be sized | Revenue durability | Medium impact | Management disclosure |
| CP-5-GAP-006 | Revolver or undrawn commitments | Credit agreement | Liquidity may be understated | Liquidity chart | Medium impact | Credit agreement |
| CP-5-GAP-007 | Preliminary purchase price allocation and CVR milestone terms | Final allocation, Transaction Agreement | Goodwill and intangibles can change | Balance sheet, earnings | Medium impact | Later 10-Q and exhibits |

### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | run alks-2026-11-05-credit_snapshot-host, CP-0 response sha256 1c390a89 | Source readiness for seven sources | Medium | Six H2 headings, hashes and readiness view present | Passed with notes | Locators and quotes verified |
| CP-1 | run alks-2026-11-05-credit_snapshot-host, CP-1 response sha256 ba17ec3b | Financial base, four chart selectors, financial table | Medium | Six H2 headings and selectors present | Restricted | One locator error, derived FY2025 base |
| CP-1A | run alks-2026-11-05-credit_snapshot-host, CP-1A response sha256 fb57077c | Business, transaction, governance | Medium | Six H2 headings and selectors present | Restricted | One unsupported statement |
| CP-2 | run alks-2026-11-05-credit_snapshot-host, CP-2 response sha256 c0bff421 | Credit synthesis | Medium | Six H2 headings and selectors present | Passed with notes | Corrects CP-1A buyback statement |

### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Calculations 1 and 2: FY2025 depreciation and amortization 27,165 and share-based compensation 98,716 | Supported at S1 page:167 | Cited at page:168 | Cite page:167 | Formatting / Hygiene Only |
| Minor | CP-1A | Ownership, governance and capital allocation: repurchases stopped after the term loans were drawn | Partly supported | S4 page:30 shows 27.7 US$m in Q1 2026 and none in Q2 or Q3 but does not date the Q1 purchases against February 12, 2026 | Restate as none in Q2 or Q3 2026 | Restricts Committee Use only if relied on; corrected by CP-2 |
| Minor | CP-1A | Conflicts table: Janssen revenue share | Supported | Row does not record a conflict | Move to notes | Formatting / Hygiene Only |
| Minor | CP-1 | Chart: Dec 31, 2025 total debt 0.00x | Supported | Debt nil is printed as a dash at S4 page:6 and no debt line in S1 page:165; the zero is a reported nil, not an invented zero | Keep the basis note | None |
| Minor | CP-1A | Operating model: manufacturing footprint | Supported | Combines the 10-K and the 10-Q statements in one cell | Split by source | Formatting / Hygiene Only |

### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | LTM Adjusted EBITDA 440.2 US$m rests on a derived FY2025 figure | Company definition adds share-based compensation and non-recurring items; FY2025 add-backs use a rounded 10.0 US$m cost. Without it LTM Adjusted EBITDA is 430.190 and leverage 3.48x and 1.65x | None between sources; definition risk only | Obtain the Q4 2025 release and restate if it differs | Restricts Committee Use |
| Minor | CP-1 | Share-based compensation add-back 112.6 versus statement 94.2 US$m (nine months 2026) | Add-back definition differs from statement expense | S7 page:6 against S4 page:7; Q1 differs by 18.251 US$m, Q2 and Q3 agree closely; footnote cites 20.188 of acceleration cost at S7 page:7 | Keep as logged conflict; request bridge | Restricts Committee Use only for Adjusted EBITDA |
| Minor | CP-1 | Interest expense cover | Expense basis includes bridge fees, arranger fees and write-offs | None | Keep the label expense basis | None |
| Minor | CP-1A | Gross-to-net FY2025 46.4% printed against 46.5% recomputed in Calculations | Rounding of printed percentage basis | S1 page:130 | Use the printed figure | Formatting / Hygiene Only |
| Minor | CP-1 | Debt carrying versus principal | Carrying 1,497.731 plus discount and fees 14.0 gives 1,511.731 against 1,511.750 | Rounding of printed millions | None | None |

### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Debt is senior secured, guaranteed by subsidiary guarantors, with Term Loan B outside maintenance tests | Executed Credit Agreement, Amendment No. 1 and security documents | Only the note summary at S4 page:28 is available; priority, baskets, guarantor names and release mechanics unverified | Add the executed documents; no legal interpretation is made here | Legal review of the credit agreement before any headroom or ranking statement |
| Minor | CP-1A | CVR milestone and Transaction Agreement terms | Transaction Agreement, CVR agreement | Terms beyond the 10-K and 10-Q summaries are absent | Add exhibits | Legal review for payment trigger definition |

### T5.5 Market and relative value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | No pricing, spread, rating or peer claim is made; the credit view is fundamental only | Market prices, ratings and peer set | The context holds none, and CP-2 correctly excludes relative value | None needed for this snapshot | Relative value and security selection cannot use this pack |

### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A, CP-2 | CP-1A says buybacks stopped after the loans were drawn; CP-2 says only that none occurred in Q2 or Q3 2026 and states the correction | Later module supersedes the earlier statement; CP-1A cannot be edited | Treat CP-2 wording as controlling | None once read with CP-2 |
| Minor | CP-0, CP-1 | CP-0 logged term loan principal narrative 745.3 plus 773.1 against the 1,511.750 schedule; CP-1 relied on the schedule and the 1.511 billion statement | CP-1 partly resolves CP-0 and keeps the 6.65 US$m difference open | None beyond the logged note | Principal used throughout is 1,511.75 US$m |
| Minor | CP-0, CP-1 | Q3 share-based compensation 26.7 (release and cash flow) against 27.3 US$m (equity statement) | CP-1 extends CP-0 | Keep as logged | Adjusted EBITDA add-back caveat |
| Minor | CP-1A, CP-0 | Run context lists country United States against Irish domicile in the filings | Context is not issuer evidence | Correct the context | None |
| Minor | CP-1, CP-1A, CP-2 | Figures shared across modules (debt 1,497.7, liquidity 787.6, Adjusted EBITDA 440.2, ratios 3.40x, 1.61x, 10.25x, 4.86x, free cash flow 227.4, cash from operations 72.9 and 350.7, CVR 165.7 and 136.9) | Identical values, units and periods in every module that holds them | None | Cross-module identity holds |

### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Duplicative Content | The leverage explanation appears in the financial base view, leverage section and CP-2 key findings | Keep one authoritative statement in a committee version | Formatting / Hygiene Only |
| Material | CP-2 | Committee Readiness | Credit view relies on provisional leverage and untested covenants; stated as such with Medium confidence | Obtain the credit agreement before committee clearance | Restricts Committee Use |
| Minor | CP-1A | Materiality | Timeline and company profile rows add detail beyond the decision drivers | Condense for committee | Formatting / Hygiene Only |

### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Chart selectors | No defect found: the four chart tables and the financial table are present once each, and the liquidity table's undrawn column carries a reason in place of a number, as the rules permit | None | Report liquidity chart shows cash only |
| Minor | CP-1A | Selectors | Operating model and profile tables are single tables; transaction summary is prose | None | None |
| Minor | CP-2 | Sources | Issuer sources are listed as relied on through handoffs although no source text was read | State that in the sources note, as done | None |
| Minor | CP-0 to CP-2 | Envelope | Markdown transport has no front matter or generated file name; headings and hashes follow the run rules | None | None |

### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-1, CP-2 | Definition and Assumption | LTM Adjusted EBITDA relies on a derived FY2025 base with a rounded 10.0 US$m add-back | Obtain the Q4 2025 release; keep derived label | Restricts Committee Use | Open |
| CP5-002 | Material | CP-0, CP-1, CP-2 | Evidence Gap | Covenant levels, guarantors and any revolver cannot be traced | Add the credit agreement and amendment | Restricts Committee Use | Open |
| CP5-003 | Minor | CP-1A | Unsupported Claim | Buybacks stopped after the loans were drawn | Use the CP-2 wording | Formatting / Hygiene Only | Corrected in CP-2 |
| CP5-004 | Minor | CP-1 | Citation Locator | FY2025 depreciation and share-based compensation cited at page:168, located at page:167 | Cite page:167 | Formatting / Hygiene Only | Open |
| CP5-005 | Minor | CP-1 | Source Conflict | Share-based compensation add-back differs from the statement | Request bridge; keep label | Restricts Committee Use | Open |
| CP5-006 | Minor | CP-1A | Presentation | Janssen row listed as a conflict | Move to notes | Formatting / Hygiene Only | Open |
| CP5-007 | Minor | CP-1, CP-2 | Duplicative Content | Leverage narrative repeated | Condense | Formatting / Hygiene Only | Open |

### Remediation priority map

Must-fix before committee: CP5-002 (add the credit agreement and Amendment No. 1) and CP5-001 (obtain the Q4 2025 release or restate the leverage basis).

Must-fix before the handoffs are consumed downstream: CP5-004 and CP5-003 (correct the locator and the buyback statement in any restatement, or have consumers read CP-2 as controlling).

Monitoring follow-up: CP5-005 (share-based compensation bridge), the 2027 VIVITROL generic entry, the final purchase price allocation and the CVR milestone, and cash interest paid once reported.

Formatting and hygiene: CP5-006 and CP5-007.

### Clearance decision

CLEARANCE DECISION: Conditional. Critical Issues: 0. Material Issues: 2. Minor Issues: 5. Committee Use: Restricted. qa_status: Restricted; committee_status: Restricted. No Critical finding changes the credit conclusion, so the Blocked cap does not apply. Committee use should be limited to a provisional fundamental view until the credit agreement is reviewed and the FY2025 Adjusted EBITDA basis is confirmed. The numeric confidence score is not asserted (script-owned); the band is Medium.

## Calculations

Independent recomputation performed for this audit from the cited inputs (USD thousands unless stated): FY2025 EBITDA 241,664 - 45,304 + 12,277 + 49,786 + 27,165 = 285,588. FY2025 Adjusted EBITDA 285,588 + 98,716 + 10,000 = 394,304. LTM EBITDA 285,588 + 81,798 - 221,217 = 146,169. LTM Adjusted EBITDA 394,304 + 339,544 - 293,658 = 440,190. Total debt 26,500 + 1,471,231 = 1,497,731. Cash and investments 631,314 + 124,150 + 32,110 = 787,574. Net debt 1,497,731 - 787,574 = 710,157. Ratios: 1,497,731 / 440,190 = 3.402; 710,157 / 440,190 = 1.613; 1,497,731 / 146,169 = 10.247; 710,157 / 146,169 = 4.858. Sensitivity without the 10,000 add-back: LTM Adjusted EBITDA 430,190; 1,497,731 / 430,190 = 3.481; 710,157 / 430,190 = 1.651. Interest cover on expense: LTM interest expense 12,277 + 74,368 = 86,645; 440,190 / 86,645 = 5.080; Q3 120,065 / 27,551 = 4.358. Cash flow: CFO 520,754 + 72,917 - 350,685 = 242,986; capex 40,420 + 15,638 - 40,440 = 15,618; free cash flow 227,368; 227,368 / 1,497,731 = 15.18%. Maturities: 1,347,562 / 1,511,750 = 89.14%; 6,625 + 26,500 + 40,563 + 45,250 + 45,250 = 164,188. Product shares: 467.9 / 1,475.9 = 31.7%; 370.0 / 1,475.9 = 25.1%; 346.7 / 1,475.9 = 23.5%; 226.0 / 1,369.1 = 16.5%. Sensitivity: 1,497.731 / 396.171 = 3.78; 1,497.731 / 352.152 = 4.25. All reproduce the handoff values. Page checks: the 10-K figures 27,165 and 98,716 sit on page 167 (not 168); all other locators checked resolve to the stated page.

## Gaps

The gaps are listed in the gaps ledger above (CP-5-GAP-001 to CP-5-GAP-007). Principal readiness limits: the executed credit agreement and Amendment No. 1, the Q4 2025 release, the proxy statement and the Transaction Agreement were not supplied, so covenant headroom, guarantor identity, any revolver, ownership and the CVR milestone definition cannot be traced. This audit did not review images or charts (none exist in the text extraction) and relied on text extraction fidelity.

## Next module

This is the final selected module of the minimum set. The outputs for delivery are the four accepted handoffs plus this audit; deliver with the restricted committee status and the remediation map above. Before committee use, obtain the credit agreement and amendment (CP5-002) and the Q4 2025 release (CP5-001), and restate the CP-1 locator and the CP-1A buyback statement if the handoffs are reissued.
