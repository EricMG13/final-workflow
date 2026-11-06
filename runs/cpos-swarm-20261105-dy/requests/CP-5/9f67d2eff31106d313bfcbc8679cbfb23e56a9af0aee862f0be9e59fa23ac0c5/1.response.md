## Request

Issuer: DYCOM INDUSTRIES INC (ticker DY; Dycom Industries, Inc., SEC file number 001-10613). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency per the context: USD. Perimeter: Dycom Industries, Inc. and its wholly owned subsidiaries, consolidated.

Task: validate the evidence trace behind every material claim in the run, and the integrity of the story the modules tell together. Evaluated set: the source readiness handoff (CP-0), the financial base (CP-1), the business and transaction registers (CP-1A) and the fundamental credit synthesis (CP-2). Scope is the default Top 5 material credit drivers, with a statement-level lineage register for the claims that carry them. This is a governance layer: it does not change upstream conclusions, adds no new credit analysis, and does not silently repair a defect; where it finds one it logs it with the fix the owner should make. Because accepted handoffs cannot be edited, every correction is stated here. I re-opened the pinned sources for 53 located checks (a located quote on the cited page for each figure or fact tested), recomputed the derived figures independently, and compared figures across the four handoffs. Periods follow Dycom's fiscal labels: FY2025 is the 52 weeks ended January 25, 2025; FY2026 is the 53 weeks ended January 31, 2026; Q2 2027 is the quarter ended August 1, 2026; LTM Q2 2027 is the constructed 53-week last-twelve-months period to August 1, 2026.

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 |
| --- | --- |
| 10-K_2026-01-31_dy-20260131.htm.jsonl | d3cce30e8b33b40ee726fca361a4ac5af2d47cfff9b57a3f36d911b5b73b8e31 |
| 10-Q_2025-10-25_dy-20251025.htm.jsonl | 629b328324cc0ef5393e62b61d8db6e3a1e48e205e2a0f26575592aea3390dd7 |
| 10-Q_2026-05-02_dy-20260502.htm.jsonl | 237d7d80121afc72a5bb1b73d79141b69d6396b9608af9b8f3dec2db64be0f4f |
| 10-Q_2026-08-01_dy-20260801.htm.jsonl | 666dcd463f60ce7cc9d18464ad1e3020b3cf1f9ca79b66ed79bb20b35e9cbf79 |
| EX-99.2_2026-03-04_q42026presentationmateri.htm.jsonl | 6988c6bbc189fb06cb090ad132fb7c67f67f6d428cb3b75cae839c0b2d040376 |
| EX-99.2_2026-05-27_q12027presentationmateri.htm.jsonl | fb3e1da73422f05d34562fe3208f0c4af7eb6fffd05db64f60aea98effba2a9e |
| EX-99.2_2026-08-26_q22027presentationmateri.htm.jsonl | db5426dcb5222e08c260f53364ad7255c795bb75eba46ab3566a5906d530e4b2 |

### Run context (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context (67215-dycom-industries-inc-dy.json) | c91849e9583c2227ff5d8a95aa89da364bfff0f885232cdd128e95fb51281f42 |

### Handoffs relied on

| Module | sha256 | Run and scope consumed |
| --- | --- | --- |
| CP-0 | 718647fe146a481414f4709c9a5b01ad4b5d904e03712717acf9f85199936a95 | Run dy-2026-11-05-credit_snapshot-host; source readiness as of 2026-11-05; READY_WITH_LIMITATIONS |
| CP-1 | 2e646964e839fbbfdb014df8aa772f6b2ce96e116e3987210169134e31b290b6 | Same run; FY2025, FY2026 and LTM Q2 2027 figures, accepted on its second attempt |
| CP-1A | be83b92d1a68b62a9b3878af2bcf4cf3b073b0ae5fd3dff96f237efe3b9223c8 | Same run; business and transaction registers to August 27, 2026 events |
| CP-2 | da6b86e2764359d7d4adc71daecab8f17d002c22415f22007b038ddc9e5e5aed | Same run; fundamental credit view held with Medium confidence |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Figures in the analytical handoffs trace to the filings, with no mismatch in 53 located checks. Leverage and cover conclusions rest on constructed figures and need pro forma and covenant inputs before committee reliance. | Medium | Executed credit documents and pro forma acquired earnings are missing, so leverage and covenant conclusions trace only to constructed figures. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 53 sampled locators match their sources and the shared figures agree across the four handoffs; no unsupported figure was found. | Reported debt, cash, liquidity and customer facts can be relied on at their cited sources. | High |
| Leverage of 2.96x and 2.61x and interest cover of 11.10x are calculated from sourced inputs but are not pro forma and not covenant ratios. | Committee use of these ratios is restricted until acquired earnings and covenant EBITDA are available. | Medium |
| The run-rate interest of about 148.9 million and cover of about 6.45x rest on an assumption: the August 1, 2026 weighted rate applied to balances, excluding fees. | Cover is directional, and the true cost of debt may differ. | Medium |
| The statement of no maturity before April 2029 does not mention an unexplained 28.4 million current portion of debt at August 1, 2026. | The wording needs a qualification, though refinancing risk stays low against 1,086.5 million of liquidity. | Medium |
| Two source conflicts stay logged and unresolved: extra-week revenue of 97.3 and 90.8 million, and Power Solutions share value of 292.5 versus 351.0 million. | Organic growth should be cited only as a management claim, and deal value should cite the closing figure. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 1 is calculated, 1 is assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the executed Credit Agreement, its First Amendment and the notes indenture together with pro forma EBITDA for the acquired businesses, which matters because every leverage, cover and headroom conclusion then traces to Dycom's management EBITDA and a non-pro-forma last-twelve-months base rather than to the lenders' covenant definitions, and it implies that committee use of leverage-based conclusions is Restricted until those inputs are obtained.

Method of the trace: for each Top 5 driver I read the claim in the handoff that makes it, opened the pinned source at the cited page and confirmed the quoted figure, then followed every derived figure back to its inputs and recomputed it. The 53 located checks cover customer concentration, contract mix, backlog, cash, revolver availability, supplier finance, liquidity, the weighted interest rate, the floating-rate share, the interest-rate sensitivity, Adjusted EBITDA for each discrete quarter and period, cash interest, debt carrying values, the extra-week revenue amounts, the Power Solutions consideration and share value, unbilled receivables, days sales outstanding, contractual obligations, the current portion of debt, buyback authorizations, employees, shares outstanding, the date of the National Technology Integrators transaction and the ownership statement. All 53 matched. The defects below are therefore about wording, basis and completeness, not about transcription of sourced figures. The strongest contrary evidence to a clean trace is that most ratios are constructed by the analyst chain rather than printed by the issuer, and the set contains two management-versus-filing or filing-versus-filing differences that no source resolves. What would make that evidence win: if the executed credit documents show a covenant EBITDA materially different from management Adjusted EBITDA, every ratio in this set would need restating on that basis.

Cross-module consistency: the figures shared by the financial base, the business and transaction registers and the synthesis are identical wherever they recur (for example 959.8 million of last-twelve-months Adjusted EBITDA, 2.96x and 2.61x, 11.10x, 6.45x, 1,086.5 million, 746.4 million, 367.4 million, 50.2%, 12,242 million and 94.0%). The synthesis introduces no number that is not in an upstream handoff. The business and transaction handoff corrected the financial base's presentation of National Technology Integrators consideration; that correction is carried here as flag 1 below.

### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-10K | 10-K_2026-01-31_dy-20260131.htm.jsonl | High (filed, audited) | FY2026 with FY2025 and FY2024 comparatives | Dycom Industries, Inc. consolidated | Statements, debt note, contractual obligations, segments, backlog, business description | 53-week year; ownership incorporated by reference to a proxy not in the pack | Debt, history, business facts |
| SRC-10Q-Q3 | 10-Q_2025-10-25_dy-20251025.htm.jsonl | High (filed, unaudited) | Q3 2026 and nine months | Same | Cash, revolver availability, Adjusted EBITDA, Power Solutions agreement and commitment letter | Single segment; pre-acquisition | Quarter bridges, transaction history |
| SRC-10Q-Q1 | 10-Q_2026-05-02_dy-20260502.htm.jsonl | High (filed, unaudited) | Q1 2027 | Same | Cash, availability, Adjusted EBITDA, National Technology Integrators agreement | Unaudited | Quarter bridges |
| SRC-10Q-Q2 | 10-Q_2026-08-01_dy-20260801.htm.jsonl | High (filed, unaudited) | Q2 2027 and six months | Same | Latest statements, debt, covenants, segments, leases, supplier finance, subsequent events | Unaudited; covenant ratios not printed | Primary current-period source |
| SRC-DECK-Q4 | EX-99.2_2026-03-04_q42026presentationmateri.htm.jsonl | Medium (management presentation, non-GAAP) | Q4 2026 and FY2026 | Same | Debt and liquidity summary, EBITDA reconciliation, outlook | Attributed claims; extra-week amounts do not tie | Cross-check only |
| SRC-DECK-Q1 | EX-99.2_2026-05-27_q12027presentationmateri.htm.jsonl | Medium | Q1 2027 | Same | Debt summary, acquisition profile, outlook | Attributed claims | Cross-check only |
| SRC-DECK-Q2 | EX-99.2_2026-08-26_q22027presentationmateri.htm.jsonl | Medium | Q2 2027 and six months | Same | Debt, liquidity, cash flow summary, reconciliations, outlook | Attributed claims; charts and notes not inspected | Cross-check only |

Module status: Ready with Limitations (all four substantive handoffs present and accepted by the run; no separate research-integrity grading output exists outside this run, and the source set lacks executed legal documents). Traceability scope: Top 5. Entity key: issuer_id dy available.

### Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Customer concentration and uncommitted volumes | CP-1A, CP-2 | AT&T, Verizon and Lumen at 25.4%, 14.0% and 10.8% of FY2026 revenue; customers not committed to volumes and may terminate for convenience; backlog 12,242 million | Revenue, working capital and debt service depend on a few carriers | Default risk and monitoring posture | 10-K page:9, page:11; 10-Q Q2 FY27 page:55 | Attribution distorted by customer mergers; backlog is an estimate |
| 2 | Acquisition-led leverage step-up | CP-1, CP-2 | Debt 950.0 million at FY2025 to 2,842.7 million at August 1, 2026; constructed 2.96x gross and 2.61x net on LTM Adjusted EBITDA of 959.8 million | Debt arrived before a full year of acquired earnings | Leverage tolerance and refinancing | 10-K page:112-115; 10-Q Q2 FY27 page:18, page:44 | Not pro forma, not covenant, 53-week base |
| 3 | Liquidity of 1,086.5 million | CP-1, CP-2 | Cash 340.1 million plus 746.4 million of revolver availability; no revolver draw | Main mitigant to leverage; sets near-term refinancing risk | Liquidity and refinancing | 10-Q Q2 FY27 page:2, page:21; Q2 deck page:4 | Availability computation not printed |
| 4 | Interest burden and floating-rate exposure | CP-1, CP-2 | LTM cash interest 86.4 million; run-rate about 148.9 million; cover 11.10x versus about 6.45x; 82% floating-rate; 11.7 million per 50 basis points | Cash interest understates the cost of debt that arrived late in FY2026 | Debt service | 10-K page:82, page:85; 10-Q Q2 FY27 page:5, page:20 | Run-rate is an assumption excluding fees |
| 5 | Working capital and supplier finance | CP-1, CP-2 | Six-month free cash flow negative 54.2 million after a 520.8 million receivables build; supplier finance 367.4 million versus cash 340.1 million | Cash conversion is seasonal and relies on a third-party program | Liquidity | 10-Q Q2 FY27 page:4, page:29, page:49 | Program terms not disclosed |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Customer concentration 25.4%, 14.0%, 10.8%; no volume commitments | CP-1A, CP-2 | 10-K page:9 "approximately 25.4% of our total contract revenues from AT&T"; page:11 "customers are not contractually committed" | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Gross leverage 2.96x and net 2.61x | CP-1, CP-2 | Notional debt 2,842.7 (Q2 deck page:4), cash 340.080 (10-Q Q2 FY27 page:2), LTM Adjusted EBITDA 959.8 built from filings | Yes | High inputs, constructed ratio | Calculated | Supported with limitation | Medium | Remediation Needed (pro forma and covenant basis) |
| Liquidity 1,086.5 million | CP-1, CP-2 | Cash 340.080 and availability 746.4 (10-Q Q2 FY27 page:2, page:21); deck liquidity 1,086.5 (Q2 deck page:4) | Yes | High | Directly Sourced | Supported with limitation | Medium | Committee-Ready with availability method caveat |
| Run-rate interest about 148.9 million, cover about 6.45x | CP-1, CP-2 | Floating-rate 2,340.0 times 5.40% (10-Q Q2 FY27 page:20) plus 22.5 fixed (10-K page:78) | Yes | High inputs | Assumption-Based | Supported as illustration | Medium | Remediation Needed (label as illustration) |
| Supplier finance 367.4 million as a liquidity sensitivity | CP-1, CP-2 | 10-Q Q2 FY27 page:29 for the amount; sensitivity to withdrawal is the analyst's reading | Yes for amount | High for amount | Analyst Inference | Supported for amount, inferred for effect | Medium | Remediation Needed (state the terms are not disclosed) |
| Extra-week revenue 97.3 versus 90.8 million | CP-0, CP-1, CP-1A | Q4 deck page:7 | Yes | Medium | Conflicting | Unresolved | Low | Not Traceable to a single figure; logged |
| Power Solutions share value 292.5 versus 351.0 million | CP-1A | 10-Q Q3 FY26 page:25; 10-K page:99 | Yes | High | Conflicting | Logged, probable measurement-date difference not stated | Medium | Remediation Needed (cite closing value) |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AT&T, Verizon, Lumen 25.4%, 14.0%, 10.8% of FY2026 revenue | pack/10-K | 10-K_2026-01-31_dy-20260131.htm.jsonl | SRC-10K | page:9 | CP-1A Company and operating model | Sourced | High | Matched |
| 94.0% of Q2 2027 revenue from multi-year contracts | pack/10-Q Q2 | 10-Q_2026-08-01_dy-20260801.htm.jsonl | SRC-10Q-Q2 | page:34 | CP-1A, CP-2 | Sourced | High | Matched |
| Backlog 12,242 million, next twelve months 6,472 million | pack/10-Q Q2 | Same | SRC-10Q-Q2 | page:55 | CP-1A, CP-2 | Sourced | High | Matched |
| Cash 340,080 thousand at August 1, 2026 | pack/10-Q Q2 | Same | SRC-10Q-Q2 | page:2 | CP-1 | Sourced | High | Matched |
| Revolver availability 746.4 million | pack/10-Q Q2 | Same | SRC-10Q-Q2 | page:21 | CP-1, CP-2 | Sourced | High | Matched; method not printed |
| Deck liquidity 1,086.5 million | pack/deck Q2 | EX-99.2_2026-08-26_q22027presentationmateri.htm.jsonl | SRC-DECK-Q2 | page:4 | CP-1 | Sourced (management) | Medium | Matched to filing inputs |
| Supplier finance 367.4 million | pack/10-Q Q2 | 10-Q_2026-08-01_dy-20260801.htm.jsonl | SRC-10Q-Q2 | page:29 | CP-1, CP-2 | Sourced | High | Matched |
| Weighted rate 5.40% on term loans | pack/10-Q Q2 | Same | SRC-10Q-Q2 | page:20 | CP-1, CP-2 | Sourced | High | Matched |
| 82% floating-rate and 11.7 million per 50 basis points | pack/10-K | 10-K_2026-01-31_dy-20260131.htm.jsonl | SRC-10K | page:82 | CP-1, CP-2 | Sourced | High | As of January 31, 2026 debt; unchanged principal at August 1, 2026 |
| Adjusted EBITDA 737.7 million (FY2026) | pack/10-K | Same | SRC-10K | page:70 | CP-1 | Sourced (management measure) | High | Matched |
| Adjusted EBITDA 219.4, 162.4, 262.5, 315.5 million for the four quarters of LTM | pack/10-Q Q3, deck Q4, 10-Q Q1, 10-Q Q2 | Respective files | SRC-10Q-Q3 page:41; SRC-DECK-Q4 page:8; SRC-10Q-Q1 page:39; SRC-10Q-Q2 page:44 | As cited | CP-1 | Sourced | High | Matched; sum equals 959.8 |
| LTM Adjusted EBITDA 959.8 million | derived | Derived | None | CP-1 Calculations | CP-1, CP-2 | Calculated | High inputs | Recomputed two ways |
| Cash paid for interest 62,302 and 52,042 thousand | pack/10-K, 10-Q Q2 | Respective files | SRC-10K page:85; SRC-10Q-Q2 page:5 | As cited | CP-1 | Sourced | High | Matched |
| Current portion of debt 28,397 thousand | pack/10-Q Q2 | 10-Q_2026-08-01_dy-20260801.htm.jsonl | SRC-10Q-Q2 | page:18 | CP-1 | Sourced | High | Composition not printed |
| Scheduled Term Loan B payment of 4.0 million in FY2027 | pack/10-K | 10-K_2026-01-31_dy-20260131.htm.jsonl | SRC-10K | page:78 | CP-1 | Sourced | High | Basis is January 31, 2026 |
| Extra-week revenue 97.3 and 90.8 million | pack/deck Q4 | EX-99.2_2026-03-04_q42026presentationmateri.htm.jsonl | SRC-DECK-Q4 | page:7 | CP-0, CP-1A | Conflicting | Medium | Both reconcile to the stated organic totals |
| Power Solutions shares 292.5 million at signing; 351.0 million at closing | pack/10-Q Q3, 10-K | Respective files | SRC-10Q-Q3 page:25; SRC-10K page:99 | As cited | CP-1A | Conflicting | High | Logged |
| Power Solutions total consideration 1,995.9 then 2,008.7 million | pack/10-K, 10-Q Q2 | Respective files | SRC-10K page:99; SRC-10Q-Q2 page:35 | As cited | CP-1A | Sourced | High | Explained by a 12.8 million adjustment |
| Unbilled receivables 1,334,390 of 2,281,043 thousand | pack/10-Q Q2 | 10-Q_2026-08-01_dy-20260801.htm.jsonl | SRC-10Q-Q2 | page:12 | CP-1A, CP-2 | Sourced | High | Matched |
| New 150.0 million repurchase authorization on August 26, 2026 | pack/10-Q Q2 | Same | SRC-10Q-Q2 | page:30 | CP-1, CP-1A, CP-2 | Sourced (subsequent event) | High | Flagged as subsequent event; not blended into period figures |
| Ownership not in the pack | pack/10-K | 10-K_2026-01-31_dy-20260131.htm.jsonl | SRC-10K | page:134 | CP-1A | Sourced (absence) | High | Insufficient Information correctly applied |

### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA 959.8 million | CP-1, CP-2 | 737.7, 355.9, 578.0; or 219.4, 162.4, 262.5, 315.5 | FY2026 less six months 2026 plus six months 2027; cross-checked by four quarters | Calculated | Reproduced | High | Leverage, cover | As in the lineage register |
| Gross leverage 2.96x | CP-1, CP-2 | 2,842.7; 959.8 | Notional debt over LTM Adjusted EBITDA | Calculated | Reproduced | Medium | Leverage tolerance | Q2 deck page:4 |
| Net leverage 2.61x | CP-1, CP-2 | 2,502.62; 959.8 | Notional net debt over LTM Adjusted EBITDA | Calculated | Reproduced | Medium | Leverage tolerance | 10-Q Q2 FY27 page:2 |
| Cash interest cover 11.10x | CP-1, CP-2 | 959.8; 86.434 | LTM Adjusted EBITDA over LTM cash paid for interest | Calculated | Reproduced | Medium | Debt service | 10-K page:85; 10-Q Q2 FY27 page:5 |
| Run-rate interest about 148.9 million; cover about 6.45x | CP-1, CP-2 | 2,340.0; 5.40%; 500.0; 4.50%; 959.8 | Floating times rate plus fixed times coupon; EBITDA over interest | Assumption-Based | Reproduced | Medium | Debt service | 10-Q Q2 FY27 page:20; 10-K page:78 |
| Annualized Q2 interest about 151.9 million; cover about 6.32x | CP-1, CP-2 | 37.965; 959.8 | Quarterly interest expense, net times 4; EBITDA over that | Assumption-Based | Reproduced | Medium | Debt service | 10-Q Q2 FY27 page:2 |
| Free cash flow 485.3 million LTM; negative 54.2 million for six months | CP-1, CP-2 | Operating cash flow and net capital expenditures | Operating cash flow less capital expenditures net of asset sale proceeds | Calculated | Reproduced | High | Liquidity | 10-K page:85; 10-Q Q2 FY27 page:4 |
| Top three customers 50.2% | CP-1A, CP-2 | 25.4%, 14.0%, 10.8% | Sum by customer name | Calculated | Reproduced | High | Concentration | 10-K page:9 |
| Goodwill plus intangibles 2,534.3 million versus equity 2,063.9 million | CP-1, CP-2 | 1,598.946; 935.389; 2,063.906 | Sum compared with equity | Calculated | Reproduced | High | Loss absorption mechanic | 10-Q Q2 FY27 page:2 |
| Covenant headroom | CP-1, CP-2 | Covenant EBITDA and ratios | None | Not Calculable | Correctly withheld | Not applicable | Covenant | 10-Q Q2 FY27 page:21 |
| Metric-definition drift | All | Adjusted EBITDA versus covenant EBITDA | Compare | Flagged | The set consistently labels ratios as constructed | Medium | Leverage | CP-1 covenants table |

### Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | No maturity before April 2029 beyond small amortization (CP-2 findings; CP-1 maturities) | The 4.0 million FY2027 amount is on a January 31, 2026 basis, while the current portion of debt at August 1, 2026 is 28.4 million and unexplained; the synthesis summary row states the claim without that caveat, although its credit view lists the unexplained current portion as counter-evidence | Weak Lineage for the wording | Near-term amortization could be larger than shown, affecting liquidity planning and the refinancing view | Qualify the statement and obtain the amortization schedule | CP-1 debt maturities chart; CP-2 liquidity finding |
| Material | Constructed leverage and cover (2.96x, 2.61x, 11.10x) | Not pro forma, not covenant, built on a 53-week LTM span; labeled correctly but used as headline in the synthesis | Calculated | Committee may read them as lenders' ratios | Keep the constructed label and pro forma gap in every citation | CP-1, CP-2 summaries |
| Material | Run-rate interest and 6.45x cover | Rate times balances at one date, excluding fees and amortization | Assumption-Based | Cover may be higher or lower than shown | Label as illustration | CP-1, CP-2 |
| Material | Organic revenue growth and the extra-week adjustment | Q4 deck extra-week amounts differ between quarter and year | Conflicting | Organic growth percentages depend on an unresolved adjustment | Cite as management claims only | CP-0 conflict log; CP-1A growth row |
| Minor | National Technology Integrators total consideration in CP-1 | The parenthesis listed assumed debt beside the total, which can be read as part of it; the filing's total is cash plus shares | Weak Lineage (presentation) | Could overstate deal cost by 12.3 million if misread | Use the correction stated in CP-1A | CP-1 non-debt and latest-quarter sections |
| Minor | FY2026 liquidity in CP-1 shown as 1,455.6 million | Deck prints 1,455.5 million; the difference is of rounding size and the cause is not stated; disclosed in CP-1 | Calculated | Immaterial | None beyond the disclosure | CP-1 metrics table |
| Minor | Power Solutions share value 292.5 versus 351.0 million | Different dates; conflict logged but not explained by the filings | Conflicting | Deal value reading | Cite the closing value in accounting contexts | CP-1A conflicts |
| Minor | Interest-rate sensitivity of 11.7 million | Computed by the issuer at January 31, 2026 balances; applied to August 1, 2026 balances, which are unchanged in principal | Sourced | None | None | CP-1, CP-2 |

No orphan claim (an untraced or weak-lineage conclusion in committee-facing output with no mitigation) was found: the weak-lineage item above carries a limitation in the handoff that makes it (the unexplained current portion is listed as a gap in CP-1 and CP-2).

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and decks cover FY2026 to Q2 2027; executed credit agreement, indenture and purchase agreements are absent | Covenant and guarantee claims rest on filing summaries | Headroom and structure conclusions are not testable | Obtain the executed documents |
| Citation completeness | Ready with Remediation | 53 of 53 sampled locators matched; not every figure in every handoff was re-opened | Residual transcription risk in unsampled figures | Low | Spot-check remaining figures |
| Calculation traceability | Ready with Remediation | Every derived figure has inputs and formula; all recomputed to the stated value | LTM and run-rate constructions rest on non-pro-forma and point-in-time inputs | Ratios are directional | Add pro forma and covenant bases |
| Assumption transparency | Ready with Remediation | Run-rate and annualized interest labeled as illustrations | Assumptions exclude fees and amortization | Cover may be overstated or understated | Show fee-inclusive run-rate when available |
| Markdown and export artifact integrity | Committee-Ready | Required headings, source hashes and handoff hashes present and consistent across the four handoffs; run accepted each | None identified | None | None |

Overall auditability: Ready with Remediation (the lowest assessment among the five dimensions). Committee status: Restricted for leverage, interest-cover and covenant conclusions; otherwise usable with the stated qualifications. Confidence: Medium.

### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed Credit Agreement, First Amendment, notes indenture and purchase agreements not supplied | Operative clauses, definitions, baskets, guarantors | Covenant EBITDA and restricted-payment capacity decide headroom and creditor control | Leverage, cover and financial-policy conclusions | High impact | Executed documents and compliance certificate |
| CP-5-GAP-002 | No pro forma EBITDA for Power Solutions and National Technology Integrators | Pre-acquisition EBITDA | Leverage and cover are distorted by partial-period earnings | CP-1 ratios, CP-2 view | High impact | Acquisition materials or later filings |
| CP-5-GAP-003 | Amortization schedule and the composition of the 28.4 million current portion of debt | Annual schedule | Near-term cash needs and the maturity wording | CP-1 chart, CP-2 liquidity finding | Medium impact | Credit agreement schedule |
| CP-5-GAP-004 | Revolver availability computation | Covenant calculation | Liquidity depends on a non-printed computation | CP-1, CP-2 liquidity | Medium impact | Compliance computation |
| CP-5-GAP-005 | Extra-week revenue amounts do not tie | Management explanation | Organic growth depends on the adjustment | Growth claims | Low impact | Company clarification |
| CP-5-GAP-006 | Ownership, ratings, supplier finance terms and receivable sale volumes | Proxy, rating reports, program terms | Control, market access and liquidity sensitivity | CP-1A, CP-2 | Medium impact | Proxy statement, rating reports, program documents |
| CP-5-GAP-007 | Deck charts, images and speaker notes not inspected; text extraction fidelity not reviewed | Image-level review | Residual extraction risk | Low | Low impact | Spot-check against the filings |

## Calculations

Independent recomputation from the cited source figures (US$ millions unless stated). Every handoff value matched.

| Item | Inputs (source) | Recomputed | Handoff value | Match |
| --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA, method A | 737.7 less 355.9 plus 578.0 | 959.8 | 959.8 | Yes |
| LTM Adjusted EBITDA, method B | 219.4 plus 162.4 plus 262.5 plus 315.5 | 959.8 | 959.8 | Yes |
| FY2026 check | 575.3 plus 162.4 | 737.7 | 737.7 | Yes |
| Gross leverage FY2025, FY2026, LTM | 950.0 over 576.3; 2,840.0 over 737.7; 2,842.7 over 959.8 | 1.648; 3.850; 2.962 | 1.65x; 3.85x; 2.96x | Yes |
| Net leverage FY2025, FY2026, LTM | 857.330 over 576.3; 2,130.835 over 737.7; 2,502.620 over 959.8 | 1.488; 2.888; 2.607 | 1.49x; 2.89x; 2.61x | Yes |
| Cash interest cover FY2025, FY2026, LTM | 576.3 over 57.924; 737.7 over 62.302; 959.8 over 86.434 | 9.949; 11.841; 11.104 | 9.95x; 11.84x; 11.10x | Yes |
| LTM cash interest | 62.302 less 27.910 plus 52.042 | 86.434 | 86.434 | Yes |
| Run-rate interest | 2,340.0 times 5.40% plus 500.0 times 4.50% | 148.86 | about 148.9 | Yes |
| Run-rate cover | 959.8 over 148.86 | 6.448 | about 6.45x | Yes |
| Annualized Q2 interest and cover | 37.965 times 4 = 151.860; 959.8 over 151.860 | 6.320 | about 151.9 and about 6.32x | Yes |
| Interest sensitivity | 2,340.0 times 0.50% | 11.7 | 11.7 | Yes |
| LTM free cash flow | 718.107 less 232.766 | 485.341 | 485.3 | Yes |
| Six-month free cash flow | 79.082 less 133.301 | negative 54.219 | negative 54.2 | Yes |
| Liquidity at August 1, 2026 | 340.080 plus 746.4 | 1,086.480 | 1,086.5 | Yes |
| Goodwill plus intangibles | 1,598.946 plus 935.389 | 2,534.335 | 2,534.3 | Yes |
| Top three customers | 25.4 plus 14.0 plus 10.8 | 50.2 | 50.2% | Yes |
| Unbilled share of gross receivables | 1,334,390 over 2,281,043 | 58.5% | 58.5% (CP-1A calculations) | Yes |
| Power Solutions total consideration | 1,644.9 plus 351.0; plus 12.8 | 1,995.9; 2,008.7 | 1,995.9; 2,008.7 | Yes |

Not recomputable: covenant leverage, covenant coverage and headroom (inputs not supplied); pro forma ratios (pre-acquisition EBITDA not supplied).

## Gaps

The gaps that limit committee reliance are listed in the gaps ledger above (CP-5-GAP-001 to CP-5-GAP-007) and are repeated here by consequence. High: the executed credit documents with the covenant EBITDA definition, and pro forma EBITDA for the acquired businesses; without them, leverage, cover and headroom conclusions trace only to constructed figures. Medium: the unexplained 28.4 million current portion of debt and the amortization schedule; the revolver availability computation; ownership, ratings, supplier finance terms and receivable sale volumes. Low: the unreconciled extra-week revenue amounts, deck chart and note content, and extraction fidelity of the text files. A weakness in this review itself: 53 located checks were sampled, not every figure in every handoff; a defect in an unsampled figure cannot be excluded. Results for the quarter ending October 31, 2026 are not in the pack and nothing after the cutoff of 2026-11-05 is used.

## Next module

This is the last module in the selected set. For the report and any reader of the four handoffs, apply these corrections and cautions that the accepted handoffs cannot carry: cite the National Technology Integrators total consideration of 271.4 million as cash 226.4 million plus shares 45.0 million, with assumed seller debt of 12.3 million separate; qualify the no-maturity-before-April-2029 statement with the unexplained 28.4 million current portion of debt at August 1, 2026; keep leverage, interest cover and run-rate figures labeled as constructed, not pro forma and not covenant; cite organic growth only as a management claim; and treat covenant headroom, ownership, ratings and restricted-payment capacity as not supplied. Next evidence action: obtain the executed Credit Agreement, First Amendment, 2029 indenture, the compliance computation and pro forma acquired EBITDA, then re-run the financial base and synthesis on those inputs.
