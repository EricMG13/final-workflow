## Request

Evidence trace and research-integrity review for ADVANCE AUTO PARTS INC (Advance Auto Parts, Inc., consolidated), as of 2026-11-05, pathway credit_snapshot, reporting currency USD in millions. The module re-checks the four upstream handoffs (source readiness, financial base, business and transaction context, credit synthesis) against the seven pinned filings and releases, grades what the trace finds, and states whether committee use is permitted, restricted or blocked. Quotes are verbatim from the named page; a locator `page:N` is the chunk number in the pinned file.

## Sources

### Issuer sources re-opened for this trace

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2026-01-03_aap-20260103.htm.jsonl | 88f0e66024a1a4e436956477a1b2bdacaf04082e37a839a013e4cf7b08a76ecc |
| 10-Q_2026-04-25_aap-20260425.htm.jsonl | b2dda8d971a035721b55c0b12971db6aed3046b92a0ea3374bd34ecc4d16e660 |
| 10-Q_2026-07-18_aap-20260718.htm.jsonl | d30e886360cdf677d2862f5aa362e3322f6a90f56e6bf5994651f2a56dce1ba0 |
| 10-Q_2026-10-10_aap-20261010.htm.jsonl | 32c4d101ba1517004b623cd5dd9218257b19e48552a751844ca10c65f72b2dcf |
| EX-99.1_2026-05-21_aap-ex99_1.htm.jsonl | 281142b5117a0fb7df01ee4cf7cccfd81f8a80502e2274192453a4d9bcd9063f |
| EX-99.1_2026-08-20_aap-ex99_1.htm.jsonl | 6fa6d0f76f705af9a8078a4e1b4a20159ae0682aa896d374dffc425d834ff4a2 |
| EX-99.1_2026-11-05_aap-ex99_1.htm.jsonl | de47b06e79c571c89947b08d25437b94293b8641bb8475120032ad32f61878b9 |

The context input (sha256 ffcc1267b075abb958b7ec70e65c9102a0d2613c38bcd4fb41ec20b2a4c808c3) is the requester's settings and not issuer evidence.

### Handoffs reviewed

| Module | sha256 | Scope reviewed |
| --- | --- | --- |
| CP-0 | 29209c406c3dbcb47beef8e7094c9acab8905f427370b8271dbe27c2816b6d03 | Source readiness and gaps G1 to G11 |
| CP-1 | 6fd45275ddb5cbdb5982040a992f95f406215372a19750692a32638091271979 | Financial base, ratios, liquidity, maturities, claims outside debt, covenants |
| CP-1A | 4e76df7c0784fbd3efc90d47104c8c68cb3192ef5e1a3d6c895e43caa5029d90 | Business, transaction, governance, credit translations |
| CP-2 | 1fe48bae8e9025dc26fefd616e090510db7efb3d686d545407fa78bf4c632b62 | Credit view, strengths, weaknesses, risks |

Short names 10-K FY2025, 10-Q Q1, 10-Q Q2, 10-Q Q3, Release Q1, Release Q2 and Release Q3 name the seven sources in table order. Earlier handoffs cannot be edited; where this review corrects one, it says so in the Findings below and downstream readers should use the correction.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis traces to the filings: headline figures recompute and quotes match. Two points need correction: earlier interest cover flatters, and the old revolver's unsecured status is inferred. Committee use is restricted. | Medium | Indentures, the revolver agreement, ratings and covenant ratios are absent, so ranking and headroom claims rest on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every headline figure traced to a filing page and recomputed, including liquidity of USD 3,979 million, gross leverage of 6.67x and net leverage of 0.60x. | The core liquidity and leverage view can be relied on as stated. | High |
| Coupons on the 2030 and 2033 notes first fell due on February 1, 2026, so cover of 3.01x for FY2025 and the two earlier last-twelve-month periods flatters. | Only the period to October 10, 2026, at 2.54x, shows a full year of coupons. | High |
| The unsecured status of the replaced revolver is inferred from a letter-of-credit note. | The ranking change is an interpretation; the current first lien over receivables, inventory and cash is documented. | Medium |
| No claim is untraced, and management claims are kept separate from filed facts. | Management guidance and adjusted measures cannot be treated as facts. | High |

### Evidence trace view

The analysis is traceable enough for a restricted committee read: every headline figure traces to a filing page and recomputes, and no claim is untraced. The strongest support is that the liquidity, debt and leverage inputs come directly from the latest 10-Q and 10-K and agree to management's own total debt of USD 3,388 million. The most important provenance gap is interest cover: the 2030 and 2033 notes pay coupons on February 1 and August 1 and were issued on August 4, 2025, so FY2025 cash interest holds none of their coupons and cover of 3.01x flatters. Cover of 2.54x for the twelve months to October 10, 2026 is the first with a full year. Legal documents, ratings and covenant ratios remain absent.

### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K FY2025 | High: filed, audited | Fifty-three weeks ended January 3, 2026 | Advance Auto Parts, Inc. and subsidiaries, consolidated | Statements, debt table, maturities, ABL terms, leases, supplier finance, business description | Flattened tables; indentures and ABL agreement not attached | Financial base, business context |
| S2 | 10-Q Q1 | High: filed, unaudited | Sixteen weeks ended April 25, 2026 | Consolidated | Statements, ABL availability | Year-to-date cash flow only | Quarterly columns, LTM |
| S3 | 10-Q Q2 | High: filed, unaudited | Twelve and twenty-eight weeks ended July 18, 2026 | Consolidated | Statements, repurchase of notes | Year-to-date cash flow only | Quarterly columns, LTM |
| S4 | 10-Q Q3 | High: filed, unaudited | Twelve and forty weeks ended October 10, 2026 | Consolidated | Statements, debt note, liquidity, restructuring | No debt table by series | Latest position |
| S5 | Release Q1 | Medium: furnished, management | Q1 FY2026 | Consolidated | Net leverage reconciliation, guidance | Non-GAAP measures defined by management | Cross-check only |
| S6 | Release Q2 | Medium: furnished, management | Q2 FY2026 | Consolidated | Net leverage reconciliation, debt repurchase | Same | Cross-check only |
| S7 | Release Q3 | Medium: furnished, management | Q3 FY2026 | Consolidated | Net leverage reconciliation, free cash flow, guidance, dividend | Same | Cross-check, guidance |

Module status: Full run on available inputs; the missing legal documents, ratings and proxy content limit depth but not the trace. Traceability scope: Top 5 drivers plus every figure that appears in a reader summary. Entity key: issuer id aap is present.

### Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Liquidity versus debt | CP-1, CP-2 | Cash 3,085 and availability 894 against total debt 3,388 | Cash exceeds all debt, so near-term repayment does not depend on market access | Low default risk over the next two years | 10-Q Q3 page:4 and page:12; Release Q3 page:10 | Qualified cash of 2.3 billion carries conditions |
| 2 | Earnings coverage | CP-1, CP-2 | LTM EBITDA 508, gross leverage 6.67x, net leverage 0.60x, cover 2.54x | Thin earnings convert to high gross leverage and modest cover | Debt service rests on cash and margin gains | Derived from S1, S2, S3, S4 | Simple EBITDA with no add-backs |
| 3 | Supplier finance | CP-1, CP-1A, CP-2 | Confirmed obligations 2.6 billion inside payables 3,065 | Bank pullback shortens payable terms and absorbs cash | Main liquidity sensitivity outside debt | 10-Q Q3 page:14 and page:4; 10-K FY2025 page:49 | No rating to anchor |
| 4 | Ranking after the 2025 financing | CP-1, CP-1A, CP-2 | First lien over receivables, inventory, cash; notes unsecured | Unsecured claims sit behind up to 1 billion of secured claims on current assets | Ranking matters if cash is spent or the revolver drawn | 10-K FY2025 page:89, page:90, page:91 | Indentures and ABL agreement absent; prior facility's unsecured status inferred |
| 5 | Demand and margin recovery | CP-1A, CP-2 | Comparable sales 3.5% in Q1, minus 0.5% in Q2, minus 1.2% in Q3; operating income 218 against minus 87 over forty weeks | Recovery relies on margin and cost savings rather than volume | Earnings base not yet shown to hold | Release Q1 page:1; Release Q2 page:1; 10-Q Q3 page:22 | Management attribution is Management Language |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Liquidity 3,979 against debt 3,388 | CP-1, CP-2 | 10-Q Q3 page:4 and page:12 | Yes | High | Calculated | Supported | High | Committee-Ready |
| Gross leverage 6.67x and net 0.60x on EBITDA 508 | CP-1, CP-2 | Statements in S1 to S4; recomputed below | Yes | High | Calculated | Supported | Medium | Committee-Ready |
| Cash interest cover 2.54x | CP-1, CP-2 | Interest paid in S1 to S4 | Yes | High | Calculated | Supported | Medium | Committee-Ready |
| FY2025 cover 3.01x and earlier LTM cover 3.04x and 3.62x | CP-1 | Interest paid and note payment dates | Yes | High | Calculated | Partly supported | Medium | Remediation Needed |
| Supplier finance 2.6 billion | CP-1, CP-2 | 10-Q Q3 page:14 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Revolver now first lien on current assets | CP-1, CP-1A, CP-2 | 10-K FY2025 page:91 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Revolver replaced an unsecured facility | CP-1A, CP-2 | 10-K FY2025 page:90 and page:105 | Partial | High | Analyst Inference | Partly supported | Medium | Remediation Needed |
| Maturity wall by year | CP-1, CP-2 | 10-K FY2025 page:87 and page:89; 10-Q Q3 page:11 | Yes | High | Calculated | Supported | High | Committee-Ready |
| Management leverage 2.2x | CP-1 | Release Q3 page:10 | Yes | Medium | Directly Sourced as a management claim | Supported as attributed | High | Committee-Ready |
| No sponsor or controlling holder | CP-1A, CP-2 | Absence in all seven sources | Not applicable | High | Insufficient Information | Not a finding | Low | Remediation Needed: proxy statement |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cash was 3,085 at October 10, 2026 | Balance sheet | 10-Q Q3 | S4 | page:4 | CP-1 financial table | Sourced | High | Agrees to Release Q3 net debt table |
| Current portion of debt 349 and long-term debt 3,039 | Balance sheet | 10-Q Q3 | S4 | page:4 | CP-1 calculations | Sourced | High | Sum 3,388 agrees to management total debt |
| Revolver availability 894 and letters of credit 106; no borrowings | Note 5 | 10-Q Q3 | S4 | page:12 "no outstanding borrowings under its asset-based loan revolving credit facility" | CP-1 liquidity | Sourced | High | 1,000 less 106 equals 894 |
| Principal by series 3,450 at January 3, 2026 | Note on long-term debt | 10-K FY2025 | S1 | page:87 | CP-1 debt table | Sourced | High | Six series sum to 3,450 |
| Maturities 0, 350, 300, 0, 1,475, 1,325 thereafter | Future payments | 10-K FY2025 | S1 | page:89 | CP-1 maturity chart | Sourced | High | Roll-forward to October 10, 2026 is Calculated |
| 29 and 0.1 of notes repurchased in Q2 FY2026 | Note 5 | 10-Q Q3 | S4 | page:11 | CP-1 roll-forward | Sourced | High | Release Q2 says about 30; rounding |
| Springing 1:1 fixed charge test | Credit facilities | 10-K FY2025 | S1 | page:91 "a springing financial covenant" | CP-1 covenants | Sourced | High | No reported ratio |
| Supplier finance 2.6 billion and 2.5 billion | Note 8 | 10-Q Q3 | S4 | page:14 | CP-1, CP-2 | Sourced | High | In accounts payable |
| Interest paid 76, 99, 100, 189 and comparatives | Cash flow statements | S1 to S4 | S1 to S4 | page:68; page:6 (Q1); page:6 (Q2); page:7 (Q3) | CP-1 cover | Sourced | High | Year-to-date figures |
| New notes pay February 1 and August 1; issued August 4, 2025 | Payment table and long-term debt | 10-K FY2025 | S1 | page:88 and page:87 | Not stated upstream | Sourced | High | Basis of the correction below |
| Accrued interest 79 against 23 a year earlier | Note 10 | 10-K FY2025 | S1 | page:94 | Not stated upstream | Sourced | High | Consistent with accrual and no coupon paid in FY2025 |
| Professional about half of sales | Customers | 10-K FY2025 | S1 | page:7 | CP-1A operating model | Sourced | High | |
| Comparable sales 3.5%, minus 0.5%, minus 1.2% | Releases and MD&A | S5, S6, S4 | S5, S6, S4 | page:1; page:1; page:22 | CP-1A, CP-2 | Sourced | Medium | Company-defined metric |
| Dividends declared 2.25 per share in 2023 and 1.00 in 2024 and 2025 | Equity statement | 10-K FY2025 | S1 | page:67 | CP-1A governance | Sourced | High | |
| Worldpac sale: agreement August 22, 2024, closed November 1, 2024, net proceeds about 1.44 billion | Note 19 | 10-K FY2025 | S1 | page:105 | CP-1A transaction | Sourced | High | Buyer not named |
| Old revolver was unsecured | Note 19 letter-of-credit paragraph | 10-K FY2025 | S1 | page:105 "issued under its unsecured revolving credit facility" | CP-1A, CP-2 | Inference | High source, weak link | Source names an unsecured facility at the Worldpac closing; link to the facility replaced in 2025 is by inference |
| Free cash flow 109 over forty weeks and minus 277 a year earlier | Non-GAAP reconciliation | Release Q3 | S7 | page:10 | CP-2 | Sourced | Medium | The prior-year figure is in the source but not in CP-1 |
| Guided interest expense about 210 and interest income about 105 | Guidance footnote | Release Q3 | S7 | page:3 | CP-1, CP-2 | Sourced | Medium | Management Language |

### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM EBITDA to October 10, 2026 | CP-1, CP-2 | Operating income minus 43, 218 and minus 87; D&A 272, 188 and 214 | (-43 + 218 + 87) + (272 + 188 - 214) = 262 + 246 | Calculated: 508, recomputed and agrees | Supported | Medium | PD, liquidity | S1, S4 |
| Total debt / EBITDA | CP-1, CP-2 | 3,388 and 508 | 3,388 / 508 | Calculated: 6.67x, recomputed and agrees | Supported | Medium | Leverage | S4 |
| Net debt / EBITDA | CP-1, CP-2 | 3,388, 3,085 and 508 | (3,388 - 3,085) / 508 | Calculated: 0.60x, recomputed and agrees | Supported | Medium | Leverage | S4 |
| LTM interest paid | CP-1, CP-2 | 76, 189, 65 | 76 + 189 - 65 | Calculated: 200, recomputed and agrees | Supported | Medium | Coverage | S1, S4 |
| EBITDA / interest paid | CP-1, CP-2 | 508 and 200 | 508 / 200 | Calculated: 2.54x, recomputed and agrees | Supported | Medium | Coverage | S4 |
| FY2025 cover | CP-1 | 229 and 76 | 229 / 76 | Calculated: 3.01x, arithmetic agrees; interpretation corrected | Partly supported | Medium | Coverage | S1 |
| Liquidity | CP-1, CP-2 | 3,085 and 894 | 3,085 + 894 | Calculated: 3,979, agrees | Supported | High | Liquidity | S4 |
| Principal roll-forward | CP-1 | 3,450, 0.1 and 29 | 3,450 - 29.1 | Calculated: 3,420.9, agrees; maturities sum 3,421 | Supported | High | Refinancing | S1, S4 |
| Management net leverage | CP-1 | 3,388, 2,189, 3,085 and 1,157 | (3,388 + 2,189 - 3,085) / 1,157 | Calculated: 2.15x, rounds to the 2.2x printed | Supported as attributed | High | Cross-check | S7 |
| Run-rate annual note coupons | New in this review | Principal at January 3, 2026 excluding the redeemed 2026 notes, and coupon rates | 350 x 1.75% + 300 x 5.95% + 500 x 3.90% + 975 x 7.00% + 350 x 3.50% + 975 x 7.375% | Calculated: 195.9 | Reasonableness check | Medium | Coverage | S1 page:87 |
| Coupon dates in the 16 weeks to April 25, 2026 | New in this review | Coupons on February 1, March 9, March 15, April 1 and April 15 | 70.1 + 8.9 + 6.1 + 3.1 + 9.8 | Calculated: 98.0 against interest paid of 99 | Reasonableness check | Medium | Coverage | S1 page:88, S2 page:6 |
| Coupon dates in Q3 FY2026 | New in this review | Coupons on August 1, September 9, September 15 and October 1 | 70.1 + 7.2 + 6.1 + 3.1 | Calculated: 86.5 against interest paid of 89 (difference is facility fees and rounding) | Reasonableness check | Medium | Coverage | S1 page:88, S4 page:7 |
| Cover on run-rate coupons | New in this review | 508 and 195.9 | 508 / 195.9 | Calculated: 2.59x, close to 2.54x | Reasonableness check | Medium | Coverage | Derived |

### Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Interest cover of 3.01x for FY2025 and 3.04x and 3.62x for the periods to April 25 and July 18, 2026 | The financial base says the new notes paid their first coupons late in FY2025. The payment table shows February 1 and August 1 dates and the notes were issued on August 4, 2025, so no coupon on them was paid in FY2025. The two earlier last-twelve-month periods hold only the February 1, 2026 coupon. | Calculated, with a wrong explanation | Cash interest in those periods is understated against the run-rate, so cover flatters; this drives the coverage view | Use 2.54x as the cover reference; treat the earlier rows as not comparable | CP-1 interest cover chart rows and leverage chart note for FY2025 |
| Material | The revolver replaced an unsecured facility | The word unsecured appears in the note on Worldpac letters of credit, which refers to the revolver existing in November 2024; the financial base and the business context state that the facility replaced in August 2025 was unsecured as a fact | Analyst Inference | The ranking change is central to the priming view; it rests on an inference about which facility was meant | Label as inference; rely on the documented first-lien terms of the current facility | CP-1A transaction summary, governance row and credit translation; CP-2 key finding on financing |
| Minor | Certain Canadian subsidiaries guarantee only the revolver | The source lists note guarantors and certain Canadian subsidiaries as revolver guarantors; it does not say the Canadian subsidiaries do not guarantee the notes | Weak Lineage | Guarantor perimeter feeds structural ranking | Say the Canadian subsidiaries are additional revolver guarantors | CP-1 debt discussion |
| Minor | Final Worldpac payment of 55 made in the first half of FY2026 | The 16-week cash flow already shows it, so it fell in Q1 | Directly Sourced, imprecise | Period labelling | Say Q1 FY2026 | CP-1A transaction summary |
| Minor | Net sales guidance moved toward the lower end | The source shows a point guidance of about 8,500 against a prior range of 8,485 to 8,575 | Calculated | Direction supported; the range endpoints are not stated upstream | Cite both ranges | CP-1A reader summary, CP-2 |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Citation coverage | Strong: every figure has a file and page, and quotes in the earlier handoffs were matched to their pages | Locators in the lineage register | A claim without a page cannot be audited | Supports reliance on the headline view | None beyond the flags above |
| Calculation reproducibility | Strong: all listed ratios recompute from cited inputs | Calculation register | Wrong derived figures would mislead leverage and cover | Headline ratios stand | Correct explanation of earlier cover rows |
| Definition consistency | Adequate: EBITDA is simple operating income plus D&A in both CP-1 and CP-2; management's adjusted EBITDAR and the revolver's covenant EBITDA are separate definitions | Release Q3 page:10; 10-K FY2025 page:91 | Mixing definitions would misstate headroom | Covenant headroom stays Not supplied | Keep definitions separate |
| Management versus filed fact | Adequate: guidance, adjusted margins and net leverage are tagged Management Language | CP-1A rows, CP-2 text | Adopting management claims would overstate improvement | Late-quarter comparable-sales recovery is not evidence of a trend | None |
| Legal and structural support | Weak: no indentures, revolver agreement or guarantor list | Gaps in all four handoffs | Priming, lien and distribution limits cannot be tested | Ranking conclusions are interpretations | Obtain legal documents |
| Downside logic | Adequate: initiating condition (bank pullback or ratings pressure on supplier finance), first break (shorter payable terms), transmission (working capital outflow against a 2.6 billion programme), consequence (draw on liquidity of 3,979), trigger (fall in confirmed obligations in the next 10-Q or a rating action) | 10-Q Q3 page:14; 10-K FY2025 page:49 | A working-capital drain is the fastest route to stress | Supplier finance is the key monitoring item | Monitor confirmed obligations each quarter |
| Contrary evidence | Strongest counter to the liquidity strength: USD 2.3 billion of cash is qualified cash with availability conditions, and the revolver ranks ahead of the notes. It would win if cash were spent on distributions or a default made qualified cash restricted. | 10-Q Q3 page:12 | Restricted cash is not free for debt repayment | Net leverage of 0.60x would rise if cash were deployed | Obtain the revolver definitions |

### Cross-module consistency

The four handoffs tell one story and no direct contradiction was found. All use the same period labels (FY2025, forty weeks, LTM to October 10, 2026), the same cash of 3,085, debt of 3,388, EBITDA of 508 and liquidity of 3,979, and all carry the period-label mismatch with the context. The credit synthesis repeats the financial base's ratios exactly. One definitional difference is recorded rather than resolved: the financial base's simple EBITDA of 508 is not management's adjusted EBITDAR of 1,157 or the revolver's covenant EBITDA, and the synthesis keeps them apart. The synthesis states free cash flow was an outflow a year earlier; the source supports this (Release Q3 page:10 shows 109 now and minus 277 a year earlier) though the financial base did not print the comparative.

### Issue log and clearance

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | Material | CP-1 | Metric explanation | New-note coupons not paid in FY2025; earlier cover rows flatter | Use 2.54x as reference; this review is the correction | Restricts coverage statements | Open: corrected here |
| E2 | Material | CP-1A, CP-2 | Inference stated as fact | Unsecured status of the replaced revolver | Label as inference | Restricts the priming narrative | Open: corrected here |
| E3 | Minor | CP-1 | Wording | Canadian guarantor wording | Reword | None | Open: corrected here |
| E4 | Minor | CP-1A | Period label | Worldpac payment timing | Say Q1 FY2026 | None | Open: corrected here |
| E5 | Material | All | Evidence gap | Indentures, revolver agreement, guarantor list, ratings, proxy | Obtain documents | Restricts legal capacity and ranking claims | Open |
| E6 | Material | All | Evidence gap | Covenant ratio, trigger and headroom not reported | Obtain compliance detail | Restricts covenant statements | Open |

Research QA status: Restricted. Committee status: Restricted use. The headline credit view on liquidity, leverage and maturities is supported and may be used; statements on interest cover before the twelve months to October 10, 2026, on the unsecured status of the replaced revolver, on ranking and on covenant headroom may not be used without the stated qualification. The confidence band is Medium.

## Calculations

Independent recomputation from the cited inputs, in USD millions. Every result agrees with the upstream value unless stated.

| Check | Inputs | Result |
| --- | --- | --- |
| Total debt at October 10, 2026 | 349 + 3,039 | 3,388, agrees |
| Net debt | 3,388 - 3,085 | 303, agrees |
| LTM operating income | -43 + 218 - (-87) | 262, agrees |
| LTM D&A | 272 + 188 - 214 | 246, agrees |
| LTM EBITDA | 262 + 246 | 508, agrees |
| Total debt / EBITDA | 3,388 / 508 | 6.67x, agrees |
| Net debt / EBITDA | 303 / 508 | 0.60x, agrees |
| LTM interest paid | 76 + 189 - 65 | 200, agrees |
| EBITDA / interest paid | 508 / 200 | 2.54x, agrees |
| FY2025 EBITDA and cover | (-43 + 272) = 229; 229 / 76 | 3.01x, arithmetic agrees |
| LTM cover to April 25, 2026 | (-43 + 69 + 131 + 257 = 414); 414 / (76 + 99 - 39 = 136) | 3.04x, arithmetic agrees |
| LTM cover to July 18, 2026 | (-43 + 170 + 109 + 256 = 492); 492 / (76 + 100 - 40 = 136) | 3.62x, arithmetic agrees |
| Liquidity | 3,085 + 894 | 3,979, agrees |
| Principal at January 3, 2026 | 350 + 300 + 500 + 975 + 350 + 975 | 3,450, agrees |
| Principal roll-forward | 3,450 - 0.1 - 29 | 3,420.9, agrees |
| Annual coupon on the six note series | 6.1 + 17.9 + 19.5 + 68.3 + 12.3 + 71.9 | 195.9 |
| New-note coupons per payment date | 975 x 7.000% / 2 + 975 x 7.375% / 2 | 70.1 |
| Accrued interest on the new notes from August 4, 2025 to January 3, 2026 (reasonableness) | (975 x 7.000% + 975 x 7.375%) x 152 / 360 | 59.2, against a rise of 56 in accrued interest from 23 to 79 |
| Cover on run-rate coupons | 508 / 195.9 | 2.59x, versus 2.54x on paid interest |

## Gaps

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | Legal documents absent | Indentures, supplemental indentures, revolver agreement, guarantor list | Lien, restricted payment, priming and guarantor terms cannot be tested | Ranking and distribution statements are interpretations | Confidence capped at Medium | Filed exhibits listed in the exhibit index |
| T2 | Covenant measures absent | Fixed charge ratio, springing trigger, line cap definition | Covenant distance unknown | Covenant headroom Not supplied | Confidence capped at Medium | Compliance certificate |
| T3 | Credit ratings absent | Agency reports | Supplier finance and pricing are rating-sensitive | Sensitivity cannot be anchored | Lower | Agency reports |
| T4 | Ownership information absent | Proxy statement | Sponsor alignment and related-party behaviour unknown | Insufficient Information, not adverse | Lower | Proxy statement |
| T5 | Management bridge absent | Adjusted operating income reconciliation detail for prior periods | Adjusted margins cannot be rebuilt | Treated as Management Language | Lower | Earlier releases |
| T6 | Text extraction flattened tables | Layout check of the original tables | Cell-order errors are possible though totals tie | Figures cross-checked to totals | No further reduction | Original filings |
| T7 | Context period labels q2-2027 and fy-2026 match no period in the pack | Requester confirmation | Periods follow the filings | Labels are the filing labels | No further reduction | Requester |

## Next module

This is the last selected module. Delivery should present the credit view with the corrections above applied: use cover of 2.54x for the twelve months to October 10, 2026 as the coverage reference, describe the replaced revolver's unsecured status as an inference, and keep committee use Restricted until the legal documents, ratings and covenant detail are obtained.
