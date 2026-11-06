## Request

Evidence trace validation and research integrity review for Weatherford International plc, as of 2026-11-05, on the credit_snapshot pathway. It re-opens the cited pages of the seven supplied filings and releases, tests the three upstream analytical handoffs and the source-readiness handoff against them, recomputes every derived figure, and grades whether the set can be used by a committee. Scope is the Top 5 material credit drivers plus a full pass over the handoffs for defects; no credit conclusion is changed here.

## Sources

Issuer sources re-opened for this review (file name and sha256 as supplied by CP-OS):

| Source file | sha256 |
| --- | --- |
| 10-K_2025-12-31_wfrd-20251231.htm.jsonl | dac00725a2c3d644200d2314099fff47d7f3eb762778ea3920935ae50ab28ce2 |
| 10-Q_2026-03-31_wfrd-20260331.htm.jsonl | 9947bc5d7e7ed46ec27eb5be20182fefc783d1bcf9e98ead61e47e75e87e1802 |
| 10-Q_2026-06-30_wfrd-20260630.htm.jsonl | 0659d6081747e0dbacebc77689bd519f07b2164e0adebad5354150ed075c3f19 |
| 10-Q_2026-09-30_wfrd-20260930.htm.jsonl | 678145577a1f518a8936739eae48408772c69c0e9c66ea7073ec677a8f4ec5f5 |
| EX-99.1_2026-04-21_a2026-q1ex991earningsrelea.htm.jsonl | 16b049423c2a0b3987004d0686dae44f41d8fe13554c66ab3742b5ef18204c19 |
| EX-99.1_2026-07-21_a2026-q2ex991earningsrelea.htm.jsonl | c318686e28c9fd3731b6593cf62a7f0973fd91c30668b11db34c9715af2ad0be |
| EX-99.1_2026-10-20_a2026-q3ex991earningsrelea.htm.jsonl | f95c1562ed4f41199ffe8f8d250788ec78ae6a54ea4c8df350ecd996b8e7fb5e |

Run settings (not issuer evidence): context sha256 01c56abd12b41461776f319879358e62715a2713d739e5e9f5f0984372acf97e.

Supplied handoffs audited:

| Module | sha256 |
| --- | --- |
| CP-0 | 32ac84c9fe8120dabd000a3e4123c1abf4dbaa26e615a38753d7eb75f51a79f8 |
| CP-1 | 7abc17bb61e814c38cabb68fd3b50d842a916227f2807f1bd966fc61b4cd5e4d |
| CP-1A | 03660e813442b291a8a3d4a811adba81c12de92ef5787708e74130f243a60f54 |
| CP-2 | c93a2b119186a457ee3a6d131dc0636c210b32dab9bad911d52d1ff86c8d9e44 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The research traces well to filed pages and its calculations reproduce, but one stated reconciliation of the acquisition price is wrong and legal terms rest on summaries. Committee use should be restricted until those are addressed. | Medium | The executed credit agreement and indentures are not supplied, so covenant, guarantor and security statements need legal review. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every checked figure and quote matches the cited filing page, and every derived ratio reproduces from its stated inputs. | Leverage, liquidity and cash flow conclusions can be relied on as stated, within their definitions. | High |
| The acquisition note says components sum to the total, but they sum to 121 against 128 stated. | A small arithmetic error that does not change the credit view but must be corrected before use. | High |
| Narrative that margins were held is too strong: group adjusted EBITDA margin was 20.9% against 21.4% a year earlier. | Earnings pressure is slightly understated in two summaries; the figures themselves are right. | Medium |
| Covenant levels, guarantors and security rest on filed summaries only. | Headroom and structural claims need legal review and cannot be used as capacity evidence. | Medium |
| The liquidity measure counts performance letter of credit headroom that cannot fund cash needs. | Cash-drawable liquidity is lower than the headline but still exceeds total debt. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 1 are weak-lineage, untraced, conflicting, or insufficient-information items. Each figure and quote checked in the upstream handoffs resolves to a filed page or to a calculation that reproduces, and no source conflict was resolved silently. The most important provenance gap is the absence of the executed credit agreement and indentures, which matters because covenant levels, security, guarantors and the effect of the pending redomestication rest on filed summaries, and implies that legal statements need legal review and covenant headroom stays unsupplied before committee use.

### Input module register (T5.1)

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | wfrd-2026-11-05-credit_snapshot-host, accepted answer sha256 32ac84c9fe8120dabd000a3e4123c1abf4dbaa26e615a38753d7eb75f51a79f8 | Source readiness for seven sources | High (filed) with limits | Six required H2 headings present; reader summary and readiness view present | Accepted by CP-OS | Verdict Ready with Limitations; limits restated in later modules |
| CP-1 | same run, sha256 7abc17bb61e814c38cabb68fd3b50d842a916227f2807f1bd966fc61b4cd5e4d | Financial base, consolidated group, USD millions | High (filed) and Medium (releases) | Six H2 headings, financial base view, four chart tables and metrics table present | Accepted by CP-OS | Audited here in full |
| CP-1A | same run, sha256 03660e813442b291a8a3d4a811adba81c12de92ef5787708e74130f243a60f54 | Business, ownership and transaction context | High (filed) and Medium (releases) | Six H2 headings, three selector sections present | Accepted by CP-OS | One calculation error found |
| CP-2 | same run, sha256 c93a2b119186a457ee3a6d131dc0636c210b32dab9bad911d52d1ff86c8d9e44 | Fundamental credit synthesis from the two handoffs above | Derived from upstream | Six H2 headings, key findings and strengths sections present | Accepted by CP-OS | Quotes no source text, as designed |

Module Status: Ready with Limitations. Traceability scope: Top 5. All four upstream handoffs are available with their canonical headings; the source pack is complete for the supplied periods and has the limits recorded in the gaps ledger.

### Source register (T5B.1)

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_wfrd-20251231.htm.jsonl | High: filed, audited | FY2025 with FY2024 and FY2023 | Weatherford International plc and subsidiaries, consolidated | Statements, debt, lease, pension notes, maturity table, facility split, business description | Text extraction; balance sheet split across page:68 and page:69 | Base-year financials, facility terms, business facts |
| S2 | 10-Q_2026-03-31_wfrd-20260331.htm.jsonl | High: filed, unaudited | Q1 2026 | Same consolidated group | Balance sheet, letters of credit, cash interest, Texas redomestication text | Interim notes condensed | Quarter-end debt, liquidity and trailing interest |
| S3 | 10-Q_2026-06-30_wfrd-20260630.htm.jsonl | High: filed, unaudited | Q2 2026, six months | Same | Balance sheet, six-month cash interest, NCS merger agreement | Interim notes condensed | Same |
| S4 | 10-Q_2026-09-30_wfrd-20260930.htm.jsonl | High: filed, unaudited | Q3 2026, nine months | Same | Statements, debt note, facility terms, liquidity text, acquisition note, subsequent events | Segment tables split across page:6 and page:7 | Controls the current period |
| S5 | EX-99.1_2026-04-21_a2026-q1ex991earningsrelea.htm.jsonl | Medium: management release with reconciliation | Q1 2026, trailing twelve months | Same | Company adjusted EBITDA, total debt, net debt, leverage at 2025-12-31 and 2026-03-31 | Non-GAAP measures defined by management | Base-year trailing EBITDA |
| S6 | EX-99.1_2026-07-21_a2026-q2ex991earningsrelea.htm.jsonl | Medium: management release | Q2 2026 | Same | Same for 2026-06-30; Texas vote outcome | Same | Trailing ratios |
| S7 | EX-99.1_2026-10-20_a2026-q3ex991earningsrelea.htm.jsonl | Medium: management release | Q3 2026, nine months | Same | Reconciliation, net debt, redemption notice, ratings actions | Gross leverage value not printed | Current trailing ratios |

### Top 5 material credit drivers (T5B.2)

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Low reported leverage and large liquidity | CP-1, CP-2 | Total debt 1,480 and cash 1,161 at 2026-09-30; trailing company adjusted EBITDA 1,001 | Sets default risk and refinancing capacity; the near-term maturity is funded from cash | Supports the sound reading of financial risk and liquidity | S4 page:3; S7 page:15, page:16; S4 page:11 | Company-defined EBITDA; cash-drawable facility smaller than headline |
| 2 | Earnings decline from Middle East disruption | CP-1A, CP-2 | Nine-month revenue 3,400 against 3,629; operating income 383 against 557; regional revenue decline stated by the filer | Drives coverage, leverage drift and cash conversion | Recovery timing decides the outcome | S4 page:2, page:18, page:20 | Causal attribution is the filer's statement |
| 3 | Cash flow quality | CP-1, CP-2 | Operating cash flow 503 against 408 with working capital items 65 against (116) | Reported cash flow overstates the underlying run rate | Free cash flow supports debt service and payouts | S4 page:3; S7 page:13 | Working capital caption is the release's |
| 4 | Concentrations and trapped value | CP-1A, CP-1, CP-2 | Largest Mexican customer 14% of net receivables; cash not repatriable 164; Russian cash 128; surety bonds 534 | Cuts usable liquidity and adds callable claims | Liquidity must be read net of these | S4 page:31, page:32, page:34, page:19 | Overlap of Russian and non-repatriable cash not stated |
| 5 | Structural transition: redomestication and co-issuer changes | CP-1A, CP-2 | Shareholder approval 2026-09-03 pending court sanction; co-issuer added 2026-09-25 | Could change obligors, guarantors and collateral | Creditor protection cannot be assessed until terms are visible | S4 page:10, page:16, page:39 | Terms and purpose not described in the pack |

### Traceability map (T5B.3)

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 1,480 and net debt 282 at 2026-09-30 | CP-1 | S4 page:3 (264 + 1,216); S7 page:16 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Trailing adjusted EBITDA 1,001 and leverage 1.48x gross, 0.28x net | CP-1, CP-2 | S7 page:16 for the trailing figure; ratios calculated | Yes | Medium | Calculated | Supported | Medium | Committee-Ready |
| Liquidity: cash 1,161 plus undrawn 766 | CP-1, CP-2 | S4 page:3, page:11; commitment split S1 page:55 | Yes | High | Calculated | Partially Supported | Medium | Remediation Needed |
| Interest cover 9.02x on trailing cash interest 111 | CP-1, CP-2 | S1 page:70; S3 page:4; S4 page:4 | Yes | High | Calculated | Supported | Medium | Committee-Ready |
| Revenue and operating income decline, Iran Conflict attribution | CP-1A, CP-2 | S4 page:2, page:18, page:20 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Operating cash flow before working capital fell by 86 | CP-1, CP-2 | S4 page:3; S7 page:13 | Yes | High | Calculated | Supported | Medium | Committee-Ready |
| Mexican receivable, trapped cash, Russian cash, surety bonds | CP-1A, CP-1 | S4 page:19, page:31, page:32, page:34 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Covenant levels and facility security | CP-1 | S4 page:11, page:33 (summary text) | Yes | High | Directly Sourced | Partially Supported | Medium | Remediation Needed |
| Acquisition consideration of 128 made up of three components | CP-1A | S4 page:15 | Yes | High | Conflicting | Unsupported as a sum | Low | Remediation Needed |
| Redomestication destination sequence | CP-0, CP-1, CP-1A | S2 page:12; S6 page:5; S4 page:16 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Creditor effect of redomestication and co-issuer changes | CP-1A, CP-2 | S4 page:10, page:16 | Partial | Medium | Insufficient Information | Not testable | Low | Remediation Needed |
| Overall credit view: sound with cyclical and structural uncertainty | CP-2 | Upstream rows above | Yes | Medium | Analyst Inference | Supported by cited rows | Medium | Committee-Ready |

### Source lineage register (T5B.4)

All paths are in the pinned pack folder `/workspace/secdata/data/2026-11-05/packs/1603923-weatherford-international-plc-wfrd/`; the file name column gives the file.

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Current portion of long-term debt 264 and long-term debt 1,216 | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:3, balance sheet | CP-1 balance sheet and debt table | Sourced | High | Opened and matched |
| Cash and cash equivalents 1,161; restricted cash 37 | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:3 | CP-1 balance sheet table | Sourced | High | Matched |
| Net debt 282; trailing adjusted EBITDA 1,001; net leverage 0.28x | pack folder | EX-99.1_2026-10-20_a2026-q3ex991earningsrelea.htm | S7 | page:16 | CP-1 leverage chart data | Sourced | Medium | Management measure; matched |
| Trailing adjusted EBITDA 1,067 at 2025-12-31 | pack folder | EX-99.1_2026-04-21_a2026-q1ex991earningsrelea.htm | S5 | page:15 | CP-1 leverage chart data | Sourced | Medium | Reproduced from S1 page:45 segment table |
| Adjusted EBITDA nine months 710 against 776; Q3 254 against 269 | pack folder | EX-99.1_2026-10-20_a2026-q3ex991earningsrelea.htm | S7 | page:15 | CP-1 income statement table | Sourced | Medium | Reproduced from S4 segment tables |
| Credit Agreement commitment 1 billion, zero borrowings, letters of credit 1 and 233, bilateral 297 | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:11 | CP-1 liquidity and obligations | Sourced | High | Matched |
| Commitment split 600 revolving and financial letters of credit, 400 performance | pack folder | 10-K_2025-12-31_wfrd-20251231.htm | S1 | page:55, page:85 | CP-1 liquidity note | Sourced | High | Not restated in 2026 reports |
| Covenant levels 250, 2.50 to 1.00, 3.50 to 1.00, 1.50 to 1.00 | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:11, page:33 | CP-1 covenants | Sourced | High | Summary only |
| Revenue 3,400 against 3,629; operating income 383 against 557 | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:2 | CP-1, CP-1A, CP-2 | Sourced | High | Matched |
| Iran Conflict effect and decline of 191 in Middle East, North Africa and Asia | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:18, page:20 | CP-1A operating model | Sourced | High | Quote matched |
| Operating cash flow 503 against 408; capex 141; proceeds 17 | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:3 | CP-1 cash flow table | Sourced | High | Matched |
| Working capital items 65 against (116) | pack folder | EX-99.1_2026-10-20_a2026-q3ex991earningsrelea.htm | S7 | page:13 | CP-1 cash flow table | Sourced | Medium | Components in S4 page:3 sum to 65 |
| Interest paid 125 (FY2025), 71 and 57 (nine months), 70 and 55 (six months), 2 and 1 (Q1) | pack folder | 10-K, 10-Q Q1, Q2, Q3 files | S1, S2, S3, S4 | S1 page:70; S2 page:3; S3 page:4; S4 page:4 | CP-1 interest cover | Sourced | High | Matched |
| 2030 notes remaining principal 236, redemption notice 2026-10-20, expected 2026-10-30 | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:16 | CP-1, CP-1A, CP-2 | Sourced | High | Expected date; completion not evidenced |
| Largest Mexican customer 14% of net receivables; cash not repatriable 164; Russian cash 128; surety bonds 534 | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:32, page:31, page:19, page:34 | CP-1, CP-1A, CP-2 | Sourced | High | Matched |
| NCS acquisition total consideration 128; 13 cash net of cash acquired; 101 shares; 7 assumed awards | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:15 | CP-1A transaction summary | Sourced | High | Components sum to 121, not 128 (issue CP5-001) |
| Tangible assets 150, intangibles and goodwill 46, liabilities 34, noncontrolling interest 34 | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:15 | CP-1A transaction summary | Sourced | High | 150 + 46 - 34 - 34 = 128 reconciles |
| Texas proposal failed; Delaware plan approved 2026-09-03; completion expected Q4 2026 | pack folder | S2, S6, S4 files | S2, S6, S4 | S2 page:12; S6 page:5; S4 page:16 | CP-0, CP-1, CP-1A | Sourced | High | Dated sequence, consistent across handoffs |
| Weatherford International Holding LLC added as co-issuer of the 2033 notes on 2026-09-25 | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:10, page:39 | CP-1, CP-1A | Sourced | High | Purpose not stated |
| Dividends paid 59 and repurchases 54 in nine months 2026; 246 remaining authorization | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:4, page:38 | CP-1A, CP-2 | Sourced | High | Matched |
| Revenue by geography FY2025 and nine months 2026 | pack folder | S1 and S4 files | S1, S4 | S1 page:81; S4 page:8 | CP-1A operating model | Sourced | High | Components sum to totals |
| Segment adjusted EBITDA margins 23.3%, 23.9%, 21.3% for nine months 2026 | pack folder | 10-Q_2026-09-30_wfrd-20260930.htm | S4 | page:24, page:25, page:26 | CP-1A operating model | Sourced | High | Matched |
| Ownership, sponsor and holdings not disclosed; Item 12 incorporated by reference | pack folder | 10-K_2025-12-31_wfrd-20251231.htm | S1 | page:99 | CP-1A ownership | Sourced (absence) | High | Proxy statement not in pack |
| Context country Bermuda against filing Ireland | context and S1 | context file; 10-K | S1 | page:1 | CP-1A conflicts | Conflicting | Medium | Logged in CP-1A, not reconciled |

### Calculation and assumption register (T5B.5)

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt, net debt | CP-1, CP-2 | 264, 1,216, 1,161, 37 at 2026-09-30 | 264 + 1,216 = 1,480; 1,480 - 1,161 - 37 = 282 | Calculated | Reproduced | High | Leverage, refinancing | S4 page:3; S7 page:16 |
| Trailing adjusted EBITDA | CP-1, CP-2 | 1,067, 776, 710 | 1,067 - 776 + 710 = 1,001 | Calculated | Reproduced and equal to company figure | High | Leverage, cover | S5 page:15; S7 page:15, page:16 |
| Adjusted EBITDA base year tie-out | Review | Segment adjusted EBITDA 309, 515, 257; All Other 42; Corporate (56) | 309 + 515 + 257 + 42 - 56 = 1,067 | Calculated | Reproduced from filed segment table | High | Clears single-source concern | S1 page:45 |
| Total debt / EBITDA and net debt / EBITDA | CP-1, CP-2 | Debt 1,485, 1,484, 1,480, 1,480; net debt 443, 434, 343, 282; trailing EBITDA 1,067, 1,047, 1,016, 1,001 | Debt divided by trailing adjusted EBITDA, four period ends | Calculated | Reproduced: 1.39x, 1.42x, 1.46x, 1.48x and 0.42x, 0.41x, 0.34x, 0.28x | High | Leverage | S5, S6, S7 page:15, page:16 |
| EBITDA before add-backs | CP-1, CP-2 | Operating income 756, 557, 383; D&A 267, 193, 211 | (756 + 267) - (557 + 193) + (383 + 211) = 867; 1,001 - 867 = 134 equals add-backs 50 + 35 + 30 + 19 | Calculated | Reproduced | High | Definition risk | S1 page:68, page:70; S4 page:2, page:3 |
| Trailing cash interest and cover | CP-1, CP-2 | Interest paid 125, 71, 57; adjusted EBITDA 1,001 | 125 - 71 + 57 = 111; 1,001 / 111 = 9.02x | Calculated | Reproduced | Medium | Debt service | S1 page:70; S4 page:4 |
| Undrawn committed facilities | CP-1, CP-2 | Commitment 1,000; letters of credit 1 and 233 | 1,000 - 0 - 1 - 233 = 766; cash-drawable 600 - 1 = 599 | Calculated | Reproduced; definition issue CP5-005 | Medium | Liquidity | S4 page:11; S1 page:55 |
| Liquidity cover of total debt | CP-2 | 1,161 + 766 = 1,927; 1,161 + 599 = 1,760; debt 1,480 | 1,927 / 1,480 = 1.30x; 1,760 / 1,480 = 1.19x | Calculated | Reproduced | Medium | Liquidity | CP-1 chart data |
| Cash flow before working capital items | CP-1, CP-2 | 503, 65, 408, (116) | 503 - 65 = 438; 408 + 116 = 524; difference (86), (16.4)% | Calculated | Reproduced | High | Cash conversion | S4 page:3; S7 page:13 |
| Trailing free cash flow, company definition | CP-1 | Operating cash flow 676, 408, 503; capex 226, 175, 141; proceeds 16, 11, 17 | 771 - 192 + 22 = 601 | Calculated | Reproduced | High | Cash generation | S1 page:70; S4 page:3 |
| Pro forma redemption | CP-1 | Debt 1,480, carrying value 234, cash 1,198, cash payment 236 | 1,246 and 962; net debt 284; 1,246 / 1,001 = 1.24x | Assumption-Based | Illustrative; mixes carrying value and cash paid (issue CP5-007) | Low | Refinancing | S4 page:16 |
| Instruments outside debt | CP-2 | 1, 233, 297, 534 | Sum 1,065; 1,065 / 1,480 = 0.72x | Calculated | Reproduced; heterogeneous items (issue CP5-006) | Low | Contingent claims | S4 page:11, page:34 |
| Nine-month changes | CP-2 | 3,400, 3,629, 383, 557, 710, 776 | (6.3)%, (31.2)%, (8.5)% | Calculated | Reproduced | High | Earnings trend | S4 page:2; S7 page:15 |
| Shareholder return share of free cash flow | CP-2 | 113, 379 | 113 / 379 = 29.8% | Calculated | Reproduced | High | Capital allocation | S7 page:5, page:15 |
| International revenue share | CP-2 | 3,935 / 4,918; 2,739 / 3,400 | 80.0%; 80.6% | Calculated | Reproduced | High | Concentration | S1 page:81; S4 page:8 |
| Acquisition consideration components | CP-1A | 13, 101, 7 against 128 | 13 + 101 + 7 = 121, not 128 | Calculated | Fails as a stated sum | Low | Transaction summary | S4 page:15 |

### Missing citation and weak-lineage flags (T5B.6)

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | Acquisition consideration of 128 made up of three components | Components sum to 121; the unexplained 7 is not stated in the source | Conflicting | A false stated reconciliation in a committee-facing transaction summary undermines trust in the other sums | State that the 7 difference is unexplained in the note and use the net-assets reconciliation (150 + 46 - 34 - 34 = 128) | CP-1A transaction summary; any report text using it |
| MATERIAL | Covenant levels, security and obligor structure | Rest on filed summaries; executed documents absent | Weak Lineage | Capacity and structural statements cannot be tested at clause level | Obtain executed documents or restrict to filed text | CP-1 liquidity and covenants; CP-1A governance; CP-2 assessment |
| MINOR | Creditor effect of redomestication and co-issuer changes | Properly marked as not described; no cited evidence of effect | Insufficient Information | Orphan risk if carried into the report as a conclusion | Keep as a gap, not a finding | CP-1A, CP-2 |
| MINOR | Margins held by cost action | Statement stronger than the figures | Analyst Inference | Understates earnings pressure | Cite the margin figures | CP-1 financial base view; CP-1A business view |

### Auditability assessment (T5B.7)

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven sources cover FY2025 and Q1 to Q3 2026; no governing legal document is in the pack | Legal terms and covenant definitions can only be taken from summaries | Covenant headroom and structure cannot be measured | Add executed credit agreement and indentures, or keep restricted |
| Citation completeness | Ready with Remediation | Every checked locator opens on the cited page and quotes match; one stated sum fails | A wrong stated reconciliation weakens reliance on neighbouring rows | Small figure error; no change to credit view | Correct the acquisition statement downstream |
| Calculation traceability | Committee-Ready | All derived figures reproduce from stated inputs; base-year EBITDA ties to the filed segment table | Company-defined EBITDA remains the basis | Ratios are reliable within definition | Show the unadjusted ratio beside the adjusted one |
| Assumption transparency | Ready with Remediation | Cash-drawable facility split and pro forma redemption rest on stated assumptions | Assumptions mixed into chart cells could be read as reported | Liquidity could be read as larger than cash-drawable | Label chart cells; show both bases |
| Markdown/export artifact integrity | Committee-Ready | All handoffs carry the six required headings, hashes and selector sections | Transport differs from the skill's YAML envelope by design | None for use | None |

Overall auditability: Ready with Remediation (lowest of the five dimensions).

### Gaps ledger (T5B.8)

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed Credit Agreement, indentures and supplemental indenture not in pack | Clause-level text for covenants, baskets, guarantors, security, springing maturity | Covenant headroom and payout capacity cannot be tested; structural priority unclear | Covenant and structure statements in CP-1, CP-1A, CP-2 | High impact | Executed documents from the SEC exhibit index |
| CP-5-GAP-002 | No covenant compliance statement or ratios | Reported covenant ratios | Headroom reads as Not supplied, which limits the liquidity and default-risk view | CP-1 covenant section; CP-2 assessment | High impact | Compliance certificate or later filing |
| CP-5-GAP-003 | Redomestication terms and lender effects not described | Scheme documents, tax and intellectual property plan | Obligor and collateral arrangements could change | CP-1A governance; CP-2 structure row | Medium impact | Scheme documents; filings before the cutoff |
| CP-5-GAP-004 | Completion of the 2030 notes redemption not evidenced | Filing after 2026-10-21 | Debt after 2026-10-30 unconfirmed | CP-1 pro forma | Low impact | Later filing |
| CP-5-GAP-005 | Ownership detail not in pack | Proxy statement | Control and alignment cannot be assessed | CP-1A ownership | Low impact | Proxy statement |
| CP-5-GAP-006 | Gross leverage value and quarterly add-back bridge beyond the release reconciliation not printed | Printed gross leverage figure | Gross leverage is analyst-calculated | CP-1 leverage chart | Low impact | Company releases |
| CP-5-GAP-007 | Facility availability split not restated in 2026 | Amendment text or later note | Cash-drawable liquidity uncertain | CP-1 liquidity chart | Medium impact | Executed amendment |
| CP-5-GAP-008 | Pricing, backlog, tenor not disclosed | Contract disclosures | Revenue visibility unmeasured | CP-1A operating model | Low impact | None in filings |
| CP-5-GAP-009 | Original HTML and chart or image content not inspected; text extraction only | Original filing images | Table splits could hide rows | All | Low impact | Original filings |
| CP-5-GAP-010 | Market data on the notes: prices, spreads, yields | Market quotes | Relative value outside scope; omitted sections | Selected report sections omit relative value | Low impact | Market data source |

### Audit lanes and issue registers

Citation and evidence support (T5.2):

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A | "cost reductions held margins" (financial base view) and "margins were held by cost action" (business view) | Partially Supported | Group adjusted EBITDA margin was 20.9% for nine months 2026 against 21.4% a year earlier (S7 page:15), and Well Construction and Completions margin fell to 23.9% from 27.2% (S4 page:25); only two segments held or improved margins | Cite the margin figures instead of a general statement; do not repeat the phrase in the report | Requires Source Reconciliation |
| MINOR | CP-1 | Gap note that segment totals are "consistent in direction" with release EBITDA | Supported after this review | Reproduced exactly: segment adjusted EBITDA 1,081 plus All Other 42 less Corporate 56 equals 1,067 (S1 page:45); the single-source concern is cleared | None; cite the tie-out | Monitoring Follow-Up |

Math, logic and definition (T5.3):

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A | Transaction summary and calculations say 13, 101 and 7 "sum to the stated total of 128" | 13 + 101 + 7 = 121; the source says total consideration of 128 "includes" the three items and does not name the 7 difference (S4 page:15) | Stated sum against source arithmetic | Correct the statement: components 121 plus 7 unexplained; total reconciles through net assets 150 + 46 - 34 - 34 = 128 | Requires Calculation Rebuild |
| MINOR | CP-1 | Undrawn committed facilities 766 | Counts 167 of performance letter of credit headroom that the 10-K says cannot fund borrowings; cash-drawable is 599 | None; both bases shown | Show 599 beside 766 in the report liquidity strip | Requires Calculation Rebuild |
| MINOR | CP-2 | Instruments outside debt 1,065 and 0.72x of total debt | Adds facility letters of credit, uncommitted bilateral letters of credit and surety bonds, which have different calling conditions and overlap in purpose | None | Present as a size indicator; do not use as a ratio | Monitoring Follow-Up |
| MINOR | CP-1 | Pro forma after the redemption | Removes carrying value 234 from debt but 236 from cash; net debt 284 against 282 | None | Label as illustrative; completion not evidenced | Monitoring Follow-Up |

Legal and structural (T5.4):

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-1A, CP-2 | Covenant levels, secured status of the facility, guarantee and co-issuer structure, early maturity trigger of the facility, payout limits | Executed Amended and Restated Credit Agreement and amendments listed in the 10-K exhibit index; indentures for the 2030 and 2033 notes; supplemental indenture of 2026-09-25 | Only filed note and MD&A summaries are in the pack; no clause text, definitions or baskets | Mark as Source Limitation; do not infer capacity or headroom | Legal review required before covenant or structure statements are relied on |

Market and relative value (T5.5):

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | None made, and none permitted at this stage; the fair value table of the notes in the Q3 10-Q is the only market-related datum | Trading prices, spreads and yields of the notes and comparable set | Not in the pack and outside the selected sections | None for the current scope | Relative value is omitted from the selected report sections |

Cross-module consistency and version control (T5.6):

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Figures and names agree across modules (total debt, net debt, cash, undrawn facility, leverage, co-issuers, ratings, destination sequence); readiness labels differ: "READY_WITH_LIMITATIONS", "Sufficient with limits", "Ready with limits" | The redomestication destination moved from Texas to Delaware and the interest estimate from 103 to 102; both are logged as dated sequences, not conflicts | Use one label set in the report | None for figures |

Committee readiness and duplication (T5.7):

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Unsupported adjectives | "sound", "ample", "strong" and "light" describe leverage, liquidity and interest burden without an external benchmark, which is correct because peer ranking is prohibited | Qualify as "on reported figures" in the report | Avoids implied comparison |

Handoff envelope and evidence trace (T5.8):

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | YAML front-matter envelope and the skill's canonical headings | CP-OS Markdown transport uses six H2 headings, hashes and selector sections instead of the skill's envelope; this is a transport rule, not a defect of content | None; recorded for awareness | None |

### Consolidated issue log (T5.9)

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-1A | Calculation Error | Acquisition components stated to sum to 128 actually sum to 121 | Correct the statement; show net-assets reconciliation | Requires Calculation Rebuild | Open |
| CP5-002 | MATERIAL | CP-1, CP-1A, CP-2 | Legal Support Gap | Covenant, security, guarantor and payout statements rest on filed summaries | Obtain executed documents or restrict to summaries | Requires Legal Review | Open |
| CP5-003 | MINOR | CP-1, CP-1A | Partially Supported Claim | "Margins held" is stronger than the figures | Cite figures | Requires Source Reconciliation | Open |
| CP5-004 | MINOR | CP-2 | Promotional or Non-Credit Language | Unbenchmarked evaluative adjectives | Qualify wording | Formatting / Hygiene Only | Open |
| CP5-005 | MINOR | CP-1 | Formula / Definition Drift | Undrawn facility 766 includes performance letter of credit headroom; cash-drawable 599 | Show both | Requires Calculation Rebuild | Open |
| CP5-006 | MINOR | CP-2 | Formula / Definition Drift | Contingent instruments total mixes different items | Present as indicator only | Monitoring Follow-Up | Open |
| CP5-007 | MINOR | CP-1 | Calculation Error | Pro forma mixes carrying value and cash paid | Label illustrative | Monitoring Follow-Up | Open |
| CP5-008 | MINOR | CP-0, CP-1, CP-1A, CP-2 | Cross-Module Inconsistency | Readiness labels differ | One label set | Formatting / Hygiene Only | Open |
| CP5-009 | MINOR | CP-1 | Source Quality Limitation | Single-source base-year adjusted EBITDA | Cleared by tie-out to the filed segment table | Monitoring Follow-Up | Resolved |
| CP5-010 | MINOR | CP-2 | Market Data Gap | No market data on the notes; relative value out of scope | None now | Monitoring Follow-Up | Open |
| CP5-011 | MINOR | All | canonical Markdown Handoff Integrity Defect | Transport envelope differs from the skill's; by design | None | Formatting / Hygiene Only | Open |

### Remediation priority map

Must-fix before committee: CP5-001 (correct the acquisition arithmetic statement in any report text) and CP5-002 (legal review of covenant, security and obligor statements, or restriction of those statements to filed summaries).

Must-fix before the canonical Markdown handoff is consumed downstream: CP5-003 (replace the "margins held" wording with the margin figures) and CP5-005 (show cash-drawable and headline undrawn amounts together in the liquidity strip).

Monitoring follow-up: CP5-006, CP5-007, CP5-009 (resolved), CP5-010.

Formatting and hygiene: CP5-004, CP5-008, CP5-011.

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 9. Committee Use: Restricted.

The upstream research reproduces from the filed pages and carries no thesis-changing defect. Two Material issues restrict committee use: the false acquisition sum in the business and transaction handoff (CP5-001) and covenant and structural statements that rest on summaries and need legal review (CP5-002). The qa_status under the severity engine is Restricted; a numeric confidence score is not computed here because the scoring script and its specification are not in this repository, and the band is Medium.

## Calculations

Each derived figure in the audited handoffs was recomputed from its cited inputs; results match unless stated. Amounts are USD millions. This module's own new calculations are the reproductions and tie-outs below.

1. Base-year adjusted EBITDA tie-out from the filed segment table (S1 page:45): 309 + 515 + 257 = 1,081; plus All Other 42; less Corporate 56; equals 1,067, equal to the company trailing figure at 2025-12-31 (S5 page:15). Nine months 2026 (S4 page:6, page:23): 220 + 317 + 197 + 29 - 53 = 710. Nine months 2025 (S4 page:7, page:24): 226 + 371 + 184 + 37 - 42 = 776.
2. Trailing adjusted EBITDA at 2026-09-30: 1,067 - 776 + 710 = 1,001, equal to the company figure (S7 page:16). The Q3 2026 reconciliation: 153 + 70 + 4 + 6 + 6 + 15 = 254.
3. Total debt at 2026-09-30: 264 + 1,216 = 1,480 and 1,183 + 234 + 63 = 1,480. At 2025-12-31: 30 + 1,455 = 1,485 and 1,181 + 234 + 70 = 1,485. Net debt: 1,480 - 1,161 - 37 = 282; 1,485 - 987 - 55 = 443; 1,484 - 1,012 - 38 = 434; 1,480 - 1,100 - 37 = 343.
4. Leverage: 1,485 / 1,067 = 1.39x; 1,484 / 1,047 = 1.42x; 1,480 / 1,016 = 1.46x; 1,480 / 1,001 = 1.48x. Net: 443 / 1,067 = 0.42x; 434 / 1,047 = 0.41x; 343 / 1,016 = 0.34x; 282 / 1,001 = 0.28x. Unadjusted basis: EBITDA before add-backs 1,023 - 750 + 594 = 867; 1,480 / 867 = 1.71x; add-back bridge 1,001 - 867 = 134 = 50 + 35 + 30 + 19.
5. Trailing cash interest: Q1 125 - 2 + 1 = 124; Q2 125 - 70 + 55 = 110; Q3 125 - 71 + 57 = 111. Cover: 1,067 / 125 = 8.54x; 1,047 / 124 = 8.44x; 1,016 / 110 = 9.24x; 1,001 / 111 = 9.02x.
6. Undrawn facility: 1,000 - 7 - 245 = 748; 1,000 - 7 - 257 = 736; 1,000 - 4 - 243 = 753; 1,000 - 1 - 233 = 766; cash-drawable at 2026-09-30: 600 - 1 = 599. Liquidity: 1,161 + 766 = 1,927 (1.30x of 1,480); 1,161 + 599 = 1,760 (1.19x).
7. Cash flow before working capital items: 503 - 65 = 438; 408 - (-116) = 524; difference -86 (-16.4%). Components 186 - 19 - 72 - 7 - 23 = 65 and 22 - 17 - 91 - 27 - 3 = -116, equal to the release caption (S7 page:13). Trailing company-definition free cash flow: (676 - 408 + 503) - (226 - 175 + 141) + (16 - 11 + 17) = 771 - 192 + 22 = 601. Nine-month adjusted free cash flow: 503 - 141 + 17 = 379.
8. Nine-month changes: 3,400 / 3,629 - 1 = -6.3%; 383 / 557 - 1 = -31.2%; 710 / 776 - 1 = -8.5%; adjusted EBITDA margin 710 / 3,400 = 20.9% against 776 / 3,629 = 21.4%; operating margin 383 / 3,400 = 11.3% against 557 / 3,629 = 15.3%.
9. Revenue sums: segments 943 + 1,326 + 926 + 205 = 3,400; FY2025 geography 983 + 3,935 = 4,918 and 898 + 921 + 2,116 = 3,935; nine months 2026 661 + 2,739 = 3,400 and 645 + 725 + 1,369 = 2,739; services plus products 2,980 + 1,938 = 4,918 and 2,086 + 1,314 = 3,400.
10. Debt maturity schedule: 29 + 20 + 9 + 4 + 238 + 1,206 = 1,506; less 21 = 1,485 (S1 page:86).
11. Acquisition: components 13 + 101 + 7 = 121 against stated total 128, difference 7 unexplained in the note; net assets 150 + 46 - 34 = 162; less noncontrolling interest 34 = 128 (S4 page:15). The correction to the earlier handoff is stated here because the handoff cannot be edited.
12. Other: contingent instruments 1 + 233 + 297 + 534 = 1,065 (0.72x of 1,480); shareholder return 59 + 54 = 113 (29.8% of 379); pro forma debt 1,480 - 234 = 1,246 (1.24x); pro forma cash 1,198 - 236 = 962; pro forma net debt 284.

## Gaps

The gaps ledger above lists the ten evidence gaps with follow-up sources. In summary, the evidence limits that change a conclusion are the missing executed debt documents and covenant compliance figures (covenant headroom and structural statements stay restricted), the undescribed lender effects of the pending redomestication, the unconfirmed completion of the October 2026 redemption, and the cash-drawable portion of the facility. Limits that do not change a conclusion are text-only extraction, undisclosed backlog and pricing, and absent market data for relative value.

## Next module

This is the final module of the selected set; no further module is run for this pathway. Before the report is used for committee, correct the acquisition arithmetic statement (CP5-001), obtain legal review of the covenant, security and obligor statements or keep them labelled as filed summaries (CP5-002), replace the "margins held" wording with the figures (CP5-003), and show cash-drawable and headline undrawn amounts together (CP5-005). Re-run this review if the executed credit agreement, a covenant compliance statement, the redomestication scheme documents or a filing after 2026-10-21 and before the cutoff becomes available.
