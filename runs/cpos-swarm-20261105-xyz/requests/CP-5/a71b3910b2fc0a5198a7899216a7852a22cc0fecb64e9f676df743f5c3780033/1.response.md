## Request

Block, Inc. (issuer id xyz, ticker XYZ), as of 2026-11-05 (evidence cutoff 2026-11-05), pathway credit_snapshot, reporting currency USD with amounts in US$ millions as the handoffs state them. Question: is the analysis in the four upstream handoffs traceable enough for the decision, and which provenance gap matters most? Scope: the Top 5 material credit drivers, with a full pass over the figures, quotes and locators in the financial base, business context and credit synthesis handoffs; the source readiness handoff is the gate and is graded only for consistency. This review changes no upstream conclusion and repairs no citation silently; where it disagrees with an accepted handoff it says so here, because an accepted handoff cannot be edited.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Used for |
| --- | --- | --- |
| 10-K_2025-12-31_xyz-20251231.htm.jsonl | 6d2723637c4e4692665dfc17c25cdb747bc058fa0efdacc637270724a986bc79 | Re-performance of FY2025 figures, debt coupons, ownership, ratings statement, locators |
| 10-Q_2026-03-31_xyz-20260331.htm.jsonl | fb16696ee2c760f5f516dd4d7d776ad2e1413e975d581b22e43bf743c804dffb | Period coverage check only |
| 10-Q_2026-06-30_xyz-20260630.htm.jsonl | 298a453eb61f62c2eadccf751942418cba8c13261b222b26c193276f0204df4e | Period coverage check only |
| 10-Q_2026-09-30_xyz-20260930.htm.jsonl | c3685fce2b8084b3b1277e2ff24d3b8912d57dba3d48bc4c00ef1cdf864ed3ba | Re-performance of Q3 2026 and nine-month figures, debt note, contingencies, liquidity, locators |
| EX-99.1_2026-05-07_d132441dex991.htm.jsonl | d34a2a9e1d7a5617f1c2e6fc60dfac8b09244c4670a9cb13c493e5c88cddf1a8 | Not needed for any traced claim |
| EX-99.1_2026-08-05_d91486dex991.htm.jsonl | 804a5c312efc62e6ddd1ec8bbc4d12bb902bba131422b7373caf3f4ebbc3e21e | Not needed for any traced claim |
| EX-99.1_2026-11-03_q32026shareholderletter.htm.jsonl | a2c931043c84d33fdc40710a24c2e84aa25d66394cc76e294f6f9e8221b76b85 | Quarterly Adjusted EBITDA series and definition, non-GAAP cash flow, management commentary |

Run context (not issuer evidence): context 1512673-block-inc-xyz-bsqkz.json, sha256 a90d836267c628949bea7547e85d546a29cc1dd93e2cdf0e9cf75961d7745ec4.

### Handoffs supplied

| Module | sha256 |
| --- | --- |
| CP-0 | fde3c57d263f194f36b012cf6dac47111bd001036fc4309d336b4e5a15f1d35b |
| CP-1 | b07cf296fcccfced7fc39b3d89643e1dbe0b2cad1f07c4c884c441e049fe5ca0 |
| CP-1A | eac7020cf732bc7699adb7a3f965221265625fc7f02820560122c035ea5844b3 |
| CP-2 | 24f6eec89ac5abc964ef259f3104d70c7d0e982619908dbc8141600b58fd888b |

Re-anchor: all four handoffs name Block, Inc., as-of 2026-11-05, run xyz-2026-11-05-credit_snapshot-host, current period Q3 2026 and prior period FY2025, in USD. No upstream value mismatched the run.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The figures and quotes in the upstream handoffs trace to the filings and recompute correctly, and the handoffs agree with each other. Committee use is restricted because covenant terms and executed debt documents are missing, not because tracing failed. | Medium | Covenant level, guarantors and executed debt documents are not in the sources, and this review was run in the same session that wrote the handoffs. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every figure taken from the filings was found in the source text, and every derived figure recomputed exactly from the printed inputs. | The leverage, cover, liquidity and maturity numbers a committee would quote can be relied on as labelled. | High |
| All verbatim quotes in the handoffs were found in the sources. | Filing wording and management statements are attributed correctly. | High |
| One statement is only partly supported: that the accrued legal balance includes the Department of Justice amount. | The two amounts are both filed, but the filing does not say one contains the other, so legal claims outside debt should be read with that caveat. | Medium |
| No contradiction between the handoffs was found; definitions of debt and earnings are disclosed consistently. | The set tells one story, with filed-basis leverage of 4.67x and adjusted-basis leverage of 1.69x labelled throughout. | High |
| Covenant headroom, ranking and restricted-payment capacity have no source in the pack. | Conclusions on those points cannot be traced and should not be drawn until the executed documents are supplied. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 0 are assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the covenant level and the executed indentures and credit agreement, which matters because covenant headroom, guarantor ranking and restricted-payment capacity cannot be traced to any source, and implies restricted committee use. Figures and quotes were re-performed against the pinned filings and agreed. One inference, that the accrued legal balance includes the Department of Justice accrual, is stated more firmly in the financial handoff than the filing supports, and the later handoffs already treat it as unconfirmed.

### Evaluated set (inputs and status)

| Input | Status | Evaluated | Notes |
| --- | --- | --- | --- |
| CP-0 source readiness | Accepted; gate | Consistency only | Rated the set ready with limitations and listed the covenant, guarantor and executed-document gaps |
| CP-1 financial base | Accepted | Yes | Leverage, cover, liquidity and maturity tables on filed and adjusted bases; LTM bridge shown |
| CP-1A business and transaction context | Accepted | Yes | Judged CP-2 ready with limitations; governance category Neutral or Mixed |
| CP-2 credit synthesis | Accepted | Yes | Confidence Medium, inside the cap set by the upstream limits |

All four are current for the as-of date; the latest source is dated 2026-11-03. No input is stale, but the ownership percentage and the ratings statement come from the annual report (December 31, 2025 and during 2025).

### Material claim register and support review

Verdicts: supported (the named evidence states the claim or recomputes to it), partly supported (carries part of it, or carries it only with a qualification the claim omits), unsupported (does not carry it).

| Claim | Module | Evidence traced | Verdict | Reviewer note |
| --- | --- | --- | --- | --- |
| Cash and cash equivalents 7,859.3 and an undrawn revolver of 900.0 with no letters of credit | CP-1, CP-2 | 10-Q Q3 page:4, page:28, page:55 | Supported | Revolver stated as 900.0 million; table row 900,000 |
| Note principal 5,775.0 across five series; 2026 notes of 1,575.0 repaid in cash | CP-1, CP-1A, CP-2 | 10-Q Q3 page:27 (575,000 + 1,000,000 repaid; total 5,775,000) | Supported | Sum recomputed |
| Warehouse borrowings 1,543.5, availability 809.3, final maturities by year | CP-1, CP-1A | 10-Q Q3 page:29, page:30 (515,039; 549,437; 479,064) | Supported | Rows sum to the total |
| Total debt 7,318.5 as note principal plus warehouse drawn | CP-1, CP-2 | Recomputed from page:27 and balance sheet page:4 | Supported | A definitional choice, labelled; notes alone give 3.69x |
| LTM EBITDA on the filed basis 1,567.0; leverage 4.67x and 4.19x; cover 3.99x and 8.44x | CP-1, CP-2 | Recomputed from 10-K page:141, page:143, 10-Q Q3 page:5, page:7, page:40 | Supported | Fiscal year and LTM windows differ and are labelled |
| Adjusted EBITDA 4,336.4 LTM and ratios 1.69x and 11.03x | CP-1, CP-2 | 10-K page:125, 10-Q Q3 page:51, letter page:32 (quarters sum to the same total) | Supported | Management-defined; tagged as such |
| Department of Justice accrual 764 (gross 964) and the statement that excess losses are reasonably possible | CP-1, CP-1A, CP-2 | 10-Q Q3 page:34, page:35 | Supported | Agreement in principle; subsequent event labelled |
| Accrued legal contingencies of 980.6 include the 764 | CP-1 | 10-Q Q3 page:22 (980,592) and page:34 (764 million) | Partly supported | Both filed; inclusion not stated. CP-1A and CP-2 mark it unconfirmed |
| Operating cash flow is flattered by unpaid legal accruals | CP-1, CP-2 | 10-Q Q3 page:59 ("primarily due to an increase in accrued legal contingencies"); balance rose 807.6 | Supported | Direction supported; the amount of the effect is not stated by the filing |
| Customer cash residual of 889.0 may fund customer obligations | CP-1, CP-2 | 10-Q Q3 page:4 balances; page:59 mechanism | Partly supported | Calculated indicator; the amount owed is not stated; labelled as indicator |
| Bitcoin 27% of Q3 2026 revenue and 2% of gross profit | CP-1A, CP-2 | 10-Q Q3 page:44 | Supported | |
| Credit losses 601.7 against 363.5 | CP-1A, CP-2 | 10-Q Q3 page:5 | Supported | |
| Class B holders control a majority of votes (about 53% at year-end 2025) | CP-1A, CP-2 | 10-K page:99 | Supported | Dated in CP-1A; CP-2 states control without the date |
| Governance category Neutral or Mixed | CP-1A, CP-2 | Documented actions: repayments from cash, enlarged revolver, repurchases | Supported as an interpretation | Executed documents absent, so capacity is unassessed; labelled |
| Revolver covenant is a maximum total net leverage ratio, compliance stated | CP-1, CP-2 | 10-Q Q3 page:28, page:109 | Supported | Level and definition not printed; flagged by all handoffs |

### Citation trace

| Check | Method | Result |
| --- | --- | --- |
| Verbatim quotes | Each double-quoted span of twelve characters or more searched in the normalised text of all seven sources | 22 of 22 quotes found (17 in the readiness handoff, 5 in the financial handoff); the business handoff has no quoted spans, and the one quoted phrase in the synthesis ("more than double") is an emphasis, not a source quote |
| Figures that appear in the sources | Each comma-grouped number in the financial, business and synthesis handoffs searched against all source numbers, scaled for thousands | All present except derived sums (total debt 7,318.5 and 8,714.9, LTM revenue 25,646.4 and gross profit 12,182.8, and one sum in the synthesis), which have formulas |
| Page locators on figure-bearing lines | Each figure on a line searched on the cited pages | Figures sat on the cited pages except where a cell mixes derived figures, rounded conversions or generic references such as balance sheets and cash flow statements without page numbers |
| Cutoff | Dates after 2026-11-05 | Only labelled future dates (maturities and the November 2027 convertible); the October 2026 settlements precede the cutoff and are labelled subsequent events |
| Currency and period labels | Read every table header | USD throughout; fiscal year, nine months, quarter and LTM labelled; no nine-month figure used as a full-year figure |

Locators are extraction chunks (page:N), not printed page numbers.

### Figure identity across modules

| Figure | CP-1 | CP-1A | CP-2 | Result |
| --- | --- | --- | --- | --- |
| Note principal | 5,775.0 | 5,775.0 | 5,775.0 | Identical |
| Warehouse borrowings | 1,543.5 | 1,543.5 | 1,543.5 | Identical |
| Total debt | 7,318.5 | Not stated | 7,318.5 | Identical |
| Filed-basis leverage and cover | 4.67x; 3.99x | 4.67x; 3.99x | 4.67x; 3.99x | Identical |
| Adjusted-basis leverage and cover | 1.69x; 11.03x | 1.69x | 1.69x; 11.03x | Identical |
| Liquidity | 10,064.0 | 10,064.0 | 10,064.0 | Identical |
| Department of Justice accrual | 764 | 764 | 764 | Identical |
| Accrued legal contingencies | 980.6 (stated to include 764) | 980.6 (unconfirmed) | 980.6 (unconfirmed) | Value identical; wording differs |

### Input currency and scale

All inputs are USD. Statements are printed in thousands and the handoffs convert to US$ millions with one decimal; no value printed in thousands was entered as millions in a handoff. The shareholder letter quarterly operating cash flow and capital expenditure are rounded to millions, and the financial handoff marks them as rounded.

### Gap propagation

| Upstream limitation | Carried by CP-1 | Carried by CP-1A | Carried by CP-2 |
| --- | --- | --- | --- |
| Covenant level and reported ratio not printed | Yes | Yes | Yes |
| Executed indentures, credit agreement and guarantors not supplied | Yes | Yes | Yes |
| Adjusted measures are management claims | Yes | Yes | Yes |
| Department of Justice resolution not final | Yes | Yes | Yes |
| Customer cash share not stated | Yes | Yes | Yes |
| Discrete quarterly cash interest not supplied | Yes | Not applicable | Yes |
| Ratings are company statements only | Yes | Yes | Yes |

### Findings register

| Finding | Type | Severity | Modules | Effect |
| --- | --- | --- | --- | --- |
| Covenant level and executed debt documents are not in the sources | Evidence gap | Material | CP-1, CP-1A, CP-2 | Covenant headroom, ranking and restricted-payment capacity cannot be traced; committee use restricted for those questions |
| The accrued legal balance is said to include the Department of Justice amount, which the filing does not state | Partly supported claim | Minor | CP-1 | Interpretation of other legal accruals; later handoffs carry the caveat |
| The readiness handoff says the Q4 2025 discrete quarter is derivable only by subtraction; the financial handoff used the letter's quarterly series and cross-checked by subtraction | Description inconsistency | Minor | CP-0, CP-1 | None on figures; both routes give the same LTM total |
| Some table cells cite balance sheets or cash flow statements without page numbers, or mix derived and printed figures under one locator | Locator imprecision | Minor | CP-1, CP-1A | Figures are right; a reader needs the pages in the Sources lists |
| Fiscal-year and LTM ratios are compared as if like for like in the summaries | Period comparison | Minor | CP-1, CP-2 | Both are twelve-month windows; labelled in tables. Nine-month 2026 operating income 703.4 against 1,223.0 supports the direction |
| Ownership percentage and ratings are dated to 2025 reporting | Stale input | Minor | CP-1A, CP-2 | Dated in the business handoff; undated in the synthesis |
| Debt includes secured warehouse borrowings of special purpose entities, and neither EBITDA basis is the covenant measure | Definition risk | Material | CP-1, CP-2 | Disclosed in every handoff; the lower-quality basis is used for the headline ratio |
| The review is not independent of the authors and uses extraction text | Process limitation | Material | All | A second reviewer should compare the handoffs with the original filings before external use |

### Cross-module contradictions

None found. Pairs examined and consistent: strong stated liquidity in the synthesis against the unpaid legal accrual in the financial handoff (both carried); low adjusted leverage against high filed leverage (both labelled); repayment of 2026 maturities from cash against continued repurchases (both stated in the business handoff and used in the synthesis as a mixed signal); negative net debt against the customer cash caveat (carried in all three).

### Integrity verdict

Research QA status: Restricted. Committee use is restricted to a screening view of liquidity, near-term maturities, earnings direction on both bases and the funding structure, with the labels given. It does not support covenant headroom, structural ranking, restricted-payment capacity or recovery conclusions until the executed documents are supplied. Confidence band: Low under the canon cap for Restricted (score at most 59); the scoring script was not available in this run, so no numeric score is asserted. The verdicts agree across modules for every shared claim; the synthesis confidence of Medium is no higher than the upstream limits allow.

### Contrary evidence and what would change the view

The strongest evidence against restriction is that every figure traces, the derived figures recompute, and stated liquidity covers the 2027 convertible and warehouse finals many times (cash 7,859.3 against 1,090.0 due in 2027). If the executed credit agreement shows a leverage covenant level far above the filed-basis 4.67x and a definition close to management's adjusted basis, the covenant concern falls away. What would make that case win: the Restated Credit Agreement with its definition of consolidated EBITDA and total net leverage, a compliance certificate, and the indentures showing no guarantor or priming risk. Downside chain with observable triggers: a final Department of Justice agreement above the 764 accrued (first break: legal accrual) leads to a larger cash payment (transmission), which reduces cash below the 7,859.3 reported and weakens net leverage, then raises covenant sensitivity if the covenant definition does not add back the charges; the trigger is the court-approved final terms and the payment date.

### Analytical appendix — complete canonical registers

Module status: Ready with Remediation (all four upstream handoffs available; the quality assurance clearance for the readiness handoff is the CP-0 rating of ready with limitations). Traceability scope: Top 5. Entity key: issuer_id xyz available.

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_xyz-20251231.htm.jsonl | Audited annual filing | FY2025 | Block, Inc. consolidated | Statements, debt note, ownership, reconciliation of Adjusted EBITDA | Pre-2026 for ownership and ratings | Debt history, FY2025 base |
| S2 | 10-Q_2026-03-31_xyz-20260331.htm.jsonl | Unaudited quarterly filing | Q1 2026 | Block, Inc. consolidated | Statements and notes | Unaudited | Period coverage |
| S3 | 10-Q_2026-06-30_xyz-20260630.htm.jsonl | Unaudited quarterly filing | Q2 2026 | Block, Inc. consolidated | Statements and notes | Unaudited | Period coverage |
| S4 | 10-Q_2026-09-30_xyz-20260930.htm.jsonl | Unaudited quarterly filing | Q3 2026 and nine months | Block, Inc. consolidated | Statements, Note 12, Note 16, liquidity | Unaudited; revenue comparatives reclassified | Primary base for current period |
| S5 | EX-99.1_2026-05-07_d132441dex991.htm.jsonl | Management presentation | Q1 2026 | Block, Inc. | Letter and non-GAAP tables | Management language; charts not inspected | Context |
| S6 | EX-99.1_2026-08-05_d91486dex991.htm.jsonl | Management presentation | Q2 2026 | Block, Inc. | Letter and non-GAAP tables | Management language; charts not inspected | Context |
| S7 | EX-99.1_2026-11-03_q32026shareholderletter.htm.jsonl | Management presentation | Q3 2026 | Block, Inc. | Quarterly series, definitions, non-GAAP cash flow | Management language; charts not inspected | Quarterly bridge |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Liquidity and maturity profile | CP-1, CP-2 | Cash 7,859.3, undrawn revolver 900.0, no note before the November 2027 convertible | Determines near-term refinancing and debt service | Supports a screening view of low near-term refinancing risk | S4 page:4, 27, 28, 55 | Part of cash may fund customer balances |
| 2 | Leverage and cover on the filed basis | CP-1, CP-2 | 4.67x and 3.99x LTM | Sets default-risk reading without add-backs | Anchor for monitoring | S1 page:141, 143; S4 page:5, 7, 27, 30, 40 | Not the covenant measure |
| 3 | Dependence on add-backs | CP-1, CP-2 | Adjusted EBITDA 4,336.4 against 1,567.0 | Gap changes leverage from 4.67x to 1.69x | Which basis the covenant uses decides headroom | S1 page:125; S4 page:51; S7 page:22, 32 | Definition of covenant EBITDA not supplied |
| 4 | Legal claims outside debt | CP-1, CP-1A, CP-2 | Accrual 764; accrued legal contingencies 980.6 | Unpaid cash claim reduces liquidity | Payment timing and any excess over accrual are open | S4 page:22, 34, 35, 36 | Agreement in principle only |
| 5 | Customer cash behind net debt | CP-1, CP-2 | Customers payable exceed customer funds and receivables by 889.0 | Net debt may overstate surplus cash | Net leverage is a lower bound on risk | S4 page:4, 59 | Amount owed not stated |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Liquidity and maturity profile | CP-1, CP-2 | Balance sheet, Note 12, liquidity table | Yes | Primary filing | Directly Sourced | Supported | High | Committee-Ready |
| Leverage and cover on the filed basis | CP-1, CP-2 | Statements and cash interest | Yes | Primary filing | Calculated | Supported | High | Committee-Ready |
| Dependence on add-backs | CP-1, CP-2 | Reconciliation tables | Yes | Filing and management reconciliation | Calculated | Supported | Medium | Committee-Ready |
| Legal claims outside debt | CP-1, CP-1A, CP-2 | Note 16 accrual and statement on excess losses | Yes | Primary filing | Directly Sourced | Supported; inclusion in the 980.6 partly supported | Medium | Remediation Needed |
| Customer cash behind net debt | CP-1, CP-2 | Balances and MD&A mechanism | Partial | Primary filing, calculated indicator | Analyst Inference | Partly supported | Medium | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents 7,859.3 | source-text | 10-Q_2026-09-30_xyz-20260930.htm.jsonl | S4 | page:4 balance sheet | CP-1 statement table | Sourced | Primary filing | Printed 7,859,314 in thousands |
| Note principal 5,775.0 | source-text | 10-Q_2026-09-30_xyz-20260930.htm.jsonl | S4 | page:27 Note 12 | CP-1 statement table | Sourced | Primary filing | Total row |
| Revolver 900.0 undrawn, no letters of credit | source-text | 10-Q_2026-09-30_xyz-20260930.htm.jsonl | S4 | page:28 Note 12 | CP-1 liquidity table | Sourced | Primary filing | |
| Warehouse 1,543.5; availability 809.3 | source-text | 10-Q_2026-09-30_xyz-20260930.htm.jsonl | S4 | pages 29, 30 | CP-1 maturities | Sourced | Primary filing | |
| Adjusted EBITDA 4,336.4 LTM | source-text | 10-K and 10-Q and letter | S1, S4, S7 | page:125; page:51; page:32 | CP-1 financial table | Calculated | Filing and management reconciliation | FY2025 less nine months 2025 plus nine months 2026 |
| Cash paid for interest 393.1 LTM | source-text | 10-K and 10-Q | S1, S4 | page:211; page:40 | CP-1 interest cover | Calculated | Primary filing | |
| Department of Justice accrual 764 | source-text | 10-Q_2026-09-30_xyz-20260930.htm.jsonl | S4 | page:34 Note 16 | CP-1, CP-1A, CP-2 | Sourced | Primary filing | Subsequent event labelled |
| Class B ten votes, about 53% voting power | source-text | 10-K_2025-12-31_xyz-20251231.htm.jsonl | S1 | page:99 | CP-1A profile | Sourced | Primary filing | As of December 31, 2025 |
| Ratings BBB-, Ba1, BB+ | source-text | 10-K and 10-Q | S1, S4 | page:130; page:58 | CP-1A profile | Sourced | Company statement | No agency report |
| Bitcoin 27% of revenue, 2% of gross profit | source-text | 10-Q_2026-09-30_xyz-20260930.htm.jsonl | S4 | page:44 | CP-1A operating model | Sourced | Primary filing | |
| Accrued legal contingencies include the 764 | source-text | 10-Q_2026-09-30_xyz-20260930.htm.jsonl | S4 | page:22 and page:34 | CP-1 financial base view | Inference | Primary filing | Inclusion not stated |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM EBITDA, filed basis 1,567.0 | CP-1, CP-2 | Operating income and D&A for FY2025, nine months 2025, nine months 2026 | (1,708.406 - 1,223.035 + 703.371) + (369.529 - 273.464 + 282.148) | Calculated | Supported | High | PD, leverage | S1 page:141, 143; S4 page:5, 7 |
| Total debt 7,318.5 | CP-1, CP-2 | Note principal and warehouse drawn | 5,775.000 + 447.437 + 1,096.103 | Calculated | Supported | High | Leverage, refinancing | S4 page:4, 27 |
| Total debt / EBITDA 4.67x | CP-1, CP-2 | Above | 7,318.540 / 1,566.955 | Calculated | Supported | High | PD | as above |
| EBITDA / cash interest 3.99x | CP-1, CP-2 | LTM cash interest 393.057 | 1,566.955 / 393.057 | Calculated | Supported | High | Debt service | S1 page:211; S4 page:40 |
| Adjusted ratios 1.69x and 11.03x | CP-1, CP-2 | Adjusted EBITDA 4,336.429 | 7,318.540 / 4,336.429; 4,336.429 / 393.057 | Calculated | Supported | Medium | PD | S7 page:32 |
| Customer cash residual 889.0 | CP-1, CP-2 | Customers payable, customer funds, settlements receivable | 7,700.091 - 5,356.911 - 1,454.211 | Calculated | Partly supported | Low | Liquidity | S4 page:4 |
| Run-rate coupon 293.9 | CP-1, CP-2 | Coupons and principal | Sum of principal times coupon | Calculated | Supported | Medium | Debt service | S1 page:186 to 190 |
| Assumptions | All | None; no forward assumptions were used by the handoffs | Not applicable | Not Calculable | Not applicable | High | Not applicable | Not applicable |

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Covenant headroom | No covenant level or definition in sources | Insufficient Information | Headroom drives default risk if earnings fall | Obtain the credit agreement | CP-1, CP-2 gap lists |
| Minor | Accrued legal balance includes the 764 | Inclusion not stated | Analyst Inference | Affects reading of other legal accruals | Treat as unconfirmed | CP-1 financial base view |
| Minor | Customer cash residual | Amount owed not stated | Analyst Inference | Net debt may overstate surplus | Review customer funds disclosure | CP-1, CP-2 |
| Minor | Table locators | Generic references to statements | Weak Lineage | Reader must find the page | Add page numbers if reissued | CP-1 tables |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven sources covering FY2025 and each 2026 quarter; executed documents absent | Missing legal documents leave terms on issuer summaries | Covenant and structural conclusions restricted | Obtain executed documents |
| Citation completeness | Ready with Remediation | All quotes found; a few generic locators | Imprecise locators slow verification | No effect on figures | Add page numbers |
| Calculation traceability | Committee-Ready | Every derived figure recomputed from printed inputs | Errors would misstate leverage | Ratios can be quoted as labelled | None |
| Assumption transparency | Ready with Remediation | No forward assumptions; definition choices disclosed | Definition choice moves leverage from 4.67x to 1.69x | Basis must be quoted with each ratio | Keep labels |
| Markdown/export artifact integrity | Committee-Ready | Six headings and required tables present in each handoff | Missing sections would break the report | None | None |

Overall auditability: Ready with Remediation (lowest of the five dimensions).

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Covenant level, definition and reported ratio | Restated Credit Agreement and compliance certificate | Headroom cannot be traced | Covenant statements restricted | High impact | Credit agreement exhibit |
| CP-5-GAP-002 | Indentures and guarantor list | Executed indentures | Ranking and restricted payments untraced | Structural statements restricted | High impact | Indenture exhibits |
| CP-5-GAP-003 | Department of Justice terms final | Final agreement and court approval | Cash payment and any excess unknown | Net leverage and liquidity provisional | Medium impact | Later filings |
| CP-5-GAP-004 | Customer cash share | Disclosure of amounts owed | Net debt may overstate surplus | Net debt provisional | Medium impact | Customer funds disclosure |
| CP-5-GAP-005 | Independent review | Second reviewer | Same-session review | Overall confidence capped | Medium impact | Second reviewer |

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | CP-0 response, xyz-2026-11-05-credit_snapshot-host | Source readiness | Primary filings and management letters | Six run headings present | Accepted | Gate |
| CP-1 | CP-1 response, same run | Financial base | Primary filings | Six run headings and chart tables present | Accepted | Evaluated |
| CP-1A | CP-1A response, same run | Business and transaction | Primary filings and management letters | Six run headings and selector tables present | Accepted | Evaluated |
| CP-2 | CP-2 response, same run | Credit synthesis | Upstream handoffs | Six run headings and selectors present | Accepted | Evaluated |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Accrued legal balance includes the 764 | Partly supported | Inclusion not stated by the filing | Treat as unconfirmed | Does not block clearance |
| Minor | CP-1, CP-1A | Table cell locators | Supported | Generic or mixed references | Add pages | Does not block clearance |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Leverage differs by basis (4.67x against 1.69x) | Debt includes warehouse SPE borrowings; EBITDA basis is not the covenant measure | None | Quote basis with every ratio | Restricts covenant statements |
| Minor | CP-1, CP-2 | Fiscal-year and LTM windows compared | Both twelve-month windows | None | Keep labels | Does not block clearance |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1A, CP-2 | Notes are senior unsecured and warehouse assets are not available to creditors | Indentures and warehouse agreements | Executed documents absent; guarantors unnamed | Obtain exhibits | Legal review required before ranking conclusions |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | No market or relative-value claim is made | Prices, spreads and peers (context blank) | None needed for this scope | Supply if relative value is later requested | None for this scope |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1 | Q4 2025 discrete description differs | Both accepted; no figure affected | None | None |
| Minor | CP-1, CP-1A, CP-2 | 980.6 and 764 wording differs | CP-1 cannot be edited | Read later handoffs for the corrected wording | Legal-claims reading |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Duplication | Caveats on the covenant and basis repeat across handoffs | None | None |
| Material | All | Committee readiness | Covenant and document gaps restrict use | Obtain documents | Restricted use |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Statement table locators | Generic references without pages | Add pages if reissued | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | Material | CP-1, CP-1A, CP-2 | Evidence gap | Covenant level and executed documents absent | Obtain documents | Restricts covenant and structure conclusions | Open |
| I-02 | Material | CP-1, CP-2 | Definition risk | Leverage depends on debt and EBITDA definition | Quote basis | Restricts covenant statements | Open |
| I-03 | Material | All | Process | Review not independent | Second reviewer | Caps confidence | Open |
| I-04 | Minor | CP-1 | Partly supported claim | Accrued legal balance includes the 764 | Treat as unconfirmed | None | Open |
| I-05 | Minor | CP-1, CP-1A | Locator imprecision | Generic or mixed locators | Add pages | None | Open |
| I-06 | Minor | CP-0, CP-1 | Description inconsistency | Q4 2025 discrete wording | None | None | Open |
| I-07 | Minor | CP-1A, CP-2 | Stale input | Ownership and ratings dated to 2025 | Date in text | None | Open |

## Calculations

Independent recomputation, with inputs read from the source pages (thousands) rather than from the handoffs, and compared with the handoffs.

| Figure | Inputs | Recomputed | Stated in handoffs |
| --- | --- | --- | --- |
| LTM operating income | 1,708,406 - 1,223,035 + 703,371 | 1,188,742 | 1,188.7 |
| Cross-check by quarters | 485,371 + (171,990) + 446,870 + 428,491 | 1,188,742 | Agrees |
| LTM depreciation and amortization | 369,529 - 273,464 + 282,148 | 378,213 | 378.2 |
| LTM EBITDA, filed basis | 1,188,742 + 378,213 | 1,566,955 | 1,567.0 |
| LTM Adjusted EBITDA | 3,466,568 - 2,536,878 + 3,406,739; and 929,690 + 1,010,221 + 1,168,597 + 1,227,921 | 4,336,429 both ways | 4,336.4 |
| LTM cash interest | 246,331 - 124,220 + 270,946 | 393,057 | 393.1 |
| Total debt | 5,775,000 + 447,437 + 1,096,103; 7,350,000 + 466,942 + 897,941 | 7,318,540; 8,714,883 | 7,318.5; 8,714.9 |
| Net debt | 7,318,540 - 7,859,314; 8,714,883 - 6,564,092 | -540,774; 2,150,791 | -540.8; 2,150.8 |
| Total debt / EBITDA | 7,318,540 / 1,566,955; 8,714,883 / 2,077,935 | 4.671; 4.194 | 4.67x; 4.19x |
| Net debt / EBITDA | -540,774 / 1,566,955; 2,150,791 / 2,077,935 | -0.345; 1.035 | -0.35x; 1.04x |
| Notes only / EBITDA | 5,775,000 / 1,566,955 | 3.686 | 3.69x |
| Total debt / Adjusted EBITDA | 7,318,540 / 4,336,429; 8,714,883 / 3,466,568 | 1.688; 2.514 | 1.69x; 2.51x |
| EBITDA / cash interest | 1,566,955 / 393,057; 2,077,935 / 246,331 | 3.987; 8.436 | 3.99x; 8.44x |
| Adjusted EBITDA / cash interest | 4,336,429 / 393,057; 3,466,568 / 246,331 | 11.033; 14.073 | 11.03x; 14.07x |
| Maturity table total | 575,000 + 515,039 + 549,437 + 479,064 + 1,200,000 + 1,000,000 + 2,000,000 + 1,000,000 | 7,318,540 | 7,318.5 equals total debt |
| 2026 maturities repaid | 575,000 + 1,000,000 | 1,575,000 | 1,575.0 |
| Run-rate coupon | 1,200 x 5.625% + 1,000 x 3.50% + 2,000 x 6.50% + 1,000 x 6.000% + 575 x 0.25% | 293.9375 | 293.9 |
| Customer cash residual | 7,700,091 - 5,356,911 - 1,454,211 | 888,969 | 889.0 |
| Change in accrued legal contingencies | 980,592 - 172,959 | 807,633 | 807.6 |
| Adjusted to filed EBITDA | 4,336.4 / 1,567.0 | 2.77 | More than double |

## Gaps

| Gap | Severity | Affects | Action |
| --- | --- | --- | --- |
| Covenant level, definition and reported ratio not in the sources | Material | Covenant headroom, default-risk reading | Obtain the Restated Credit Agreement and a compliance certificate |
| Executed indentures and guarantor list not supplied | Material | Ranking, restricted payments, structural statements | Obtain the exhibits listed in the annual report |
| Department of Justice resolution not final | Material | Net leverage, liquidity | Monitor filings after the cutoff; none used here |
| Share of cash owed to customers not stated | Minor | Net debt | Review customer funds disclosure |
| Review not independent of the authors; extraction text only, locators are chunks, no fidelity review of tables | Material | All | Second reviewer to compare handoffs with original filings |
| Ratings and ownership percentage dated to 2025 reporting | Minor | CP-1A, CP-2 | Refresh from later filings or agency reports |
| Charts and images in the shareholder letters not inspected | Minor | Management commentary | Use filed statements to verify |

## Next module

None remains in the selected set. The integrity verdict is Restricted: the research may support a screening view of liquidity, maturities, earnings on both bases and the funding structure, with the labels given, but not covenant, structural-ranking, restricted-payment or recovery conclusions. Next actions in order: obtain the Restated Credit Agreement, compliance certificate and indentures; track the final Department of Justice terms and payment date; have a second reviewer compare the handoffs with the original filings before external use.
