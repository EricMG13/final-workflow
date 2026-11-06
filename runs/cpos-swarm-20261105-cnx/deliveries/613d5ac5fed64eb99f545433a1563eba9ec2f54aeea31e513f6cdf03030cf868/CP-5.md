## Request

This is the evidence trace and research integrity review for CNX Resources Corp as of 2026-11-05, on the credit snapshot pathway, covering the readiness, financial, business and credit synthesis handoffs for the consolidated group (CNX Resources Corporation and subsidiaries, with CNX Midstream Partners LP kept as a separate credit group) for FY2025 to Q3 2026. Scope is the Top 5 material credit drivers, with a full audit of all four handoffs for citation support, calculations, consistency and structure. Every locator below was re-opened in the pinned source text and every derived figure was recomputed from source-extracted inputs.

## Sources

Issuer sources behind the audited handoffs (sha256 of the pinned `.jsonl` file), each re-read for this review:

| Source file | sha256 |
| --- | --- |
| 10-K_2025-12-31_cnx-20251231.htm.jsonl | 34906d26867f4063a9570548326f1aea238accaf202234ed312875cc66d730a2 |
| 10-Q_2026-03-31_cnx-20260331.htm.jsonl | f35c89e68df093f0b33c8b07e7cb640d444c8935ee3804f523cf6d7a71ff1fc7 |
| 10-Q_2026-06-30_cnx-20260630.htm.jsonl | 19c075fbeb27af8c1c213ff72323d0cfdbec50455060a5f2125b46e7ba51d5e1 |
| 10-Q_2026-09-30_cnx-20260930.htm.jsonl | 9faf7d3a55a356eeebefe08284a5f300d91a2458f040ef83dd387bbff3cef8f1 |
| EX-99.1_2026-04-30_ex991supplementalq126.htm.jsonl | 3a5697850deb2e3211d5d3185b6661a51563bd62fdb20267f3de757d37357681 |
| EX-99.1_2026-07-30_ex991supplementalq226.htm.jsonl | 2b713e19b995caa894ecb7c089bf8f3063b820ae69afc0691f484cdb6def48b2 |
| EX-99.1_2026-10-29_ex991supplementalq326.htm.jsonl | 8ed99193157f937c422b4de1e94f2baf28f198a6be7de2f9096adc91e46b5481 |

Run context (settings only, not issuer evidence): sha256 85b88b96cc0f2168f01ec8d7b4e089124543ac7d5895fc347354eca91d4820c2.

Supplied handoffs:

| Module | sha256 |
| --- | --- |
| CP-0 | 7ad6229e7d5c097f885bb120231d68f2ddee94a0b2cf113866bd529515291d7b |
| CP-1 | c0f44bdd70d7e099610125a54c1d5c9012c94f2f941873e4e05bc3a34c0b1a67 |
| CP-1A | ecc90b7e29bec484005e3ca2c831b414057b9e1243698ff9c50335aad52c6948 |
| CP-2 | 62bf2b031a399406cbbf446da9c4de3cf825d8feac79239f5ebf65aa3b540400 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The research traces to the filings and every checked figure recomputes. One statement is wrong: 2025 cash taxes were called not supplied but the annual report prints 7,398. Use is restricted until that is corrected. | Low | Credit agreements, indentures, ratings and covenant ratios are not supplied, so legal and covenant claims rest on note summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Leverage of 1.79x, net leverage of 1.78x and interest cover of 8.07x recompute exactly from filing and supplement inputs. | The headline credit metrics can be relied on as management-measure results. | High |
| Liquidity of 1,673.053 and the maturity schedule trace directly to the debt and facility notes. | Refinancing and liquidity conclusions are sound, with the midstream part kept separate. | High |
| The claim that buybacks outran free cash flow is an inference built on checked figures. | It is reasonable but remains an analyst reading, not a reported fact. | Medium |
| Covenant headroom and legal capacity cannot be traced because the governing documents are absent. | These conclusions stay insufficient and should not be used for sizing or limits. | Low |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 is directly sourced, 2 are calculated, 0 are assumption-based, 1 is an analyst inference, and 1 is a weak-lineage, untraced, conflicting, or insufficient-information item. The most important provenance gap is the absence of the executed credit agreements and indentures, which matters because covenant levels, guarantees and security rest on note summaries and the company's own compliance statements, and implies that legal-capacity and headroom conclusions are not committee-ready. Separately, the financial handoff states that 2025 cash taxes are not supplied although the annual report prints them, a correctable limitation error that does not change any credit metric.

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 1. Minor Issues: 7. Committee Use: Restricted.

The single Material issue is the incorrect not-supplied statement for 2025 cash taxes in the financial handoff (limitation transparency); no figure used in a credit metric is affected. Committee use is restricted by rule while a Material issue is open, and the missing legal documents keep covenant and capacity conclusions out of committee reliance. The status is Restricted, so the confidence band is Low; the numeric confidence score is not computed because the scoring script and its specification are not part of the pinned inputs, and any score must not exceed 59.

### Remediation priority map

1. Must-fix before committee: CP5-001 (replace the not-supplied statement on 2025 cash taxes with the printed amount of 7,398 thousand from the annual report income tax note, page:140, and the derivable trailing figure).
2. Must-fix before the handoff is consumed downstream: none. The six-heading structure is the run transport and was accepted.
3. Monitoring follow-up: CP5-004, CP5-005 and CP5-006 (cash interest basis, rounded quarterly sums, summary-only legal evidence); re-audit when compliance certificates, credit agreements and indentures are supplied.
4. Formatting and hygiene: CP5-002, CP5-003, CP5-007 and CP5-008 (unsupported adjective, undefined risk label, envelope note, duplication).

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

Module status: Ready with Limitations (all four handoffs and all seven filings available; legal documents, ratings and the confidence script are not). Traceability scope: Top 5.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_cnx-20251231.htm.jsonl | High: audited annual report | FY2025, FY2024, FY2023 | CNX Resources Corporation and subsidiaries, consolidated | Statements, debt note, maturities, cash paid, taxes paid, pension, business description | Chunked text; exhibits listed, not supplied | Financial base, business context |
| S2 | 10-Q_2026-03-31_cnx-20260331.htm.jsonl | High: unaudited quarterly filing | Q1 2026 | Same | Balance sheet, facilities, cash paid | Unaudited | Liquidity and debt by date |
| S3 | 10-Q_2026-06-30_cnx-20260630.htm.jsonl | High: unaudited quarterly filing | Q2 2026, six months | Same | Balance sheet, facilities, six-month cash flows | Unaudited | Discrete Q3 derivation, liquidity |
| S4 | 10-Q_2026-09-30_cnx-20260930.htm.jsonl | High: unaudited quarterly filing | Q3 2026, nine months | Same | Statements, debt, covenants, commitments, segments, buybacks | Unaudited | Current-period base |
| S5 | EX-99.1_2026-04-30_ex991supplementalq126.htm.jsonl | Medium: management non-GAAP supplement | Q1 2026 and five quarters | Consolidated | Quarterly adjusted EBITDAX incl. Q1 2025 | Management definitions; rounded to millions | FY2025 earnings sum |
| S6 | EX-99.1_2026-07-30_ex991supplementalq226.htm.jsonl | Medium: management non-GAAP supplement | Q2 2026, trailing | Consolidated | Trailing adjusted EBITDAX | Same | Trailing leverage |
| S7 | EX-99.1_2026-10-29_ex991supplementalq326.htm.jsonl | Medium: management non-GAAP supplement | Q3 2026, trailing | Consolidated | Trailing adjusted EBITDAX, net debt, hedges, guidance | Same | Current leverage, hedge book |
| H0 | Readiness handoff | Derived from S1 to S7 | As of 2026-11-05 | Same | Source readiness | None found | Scope of reliance |
| H1 | Financial handoff | Derived | FY2025 to Q3 2026 | Same | Metrics, charts, debt, liquidity | One limitation error (CP5-001) | Credit synthesis |
| H2 | Business handoff | Derived | FY2025 to Q3 2026 | Same | Operating model, transactions, governance | None material | Credit synthesis |
| H3 | Credit synthesis handoff | Derived | Same | Same | Credit view, strengths, weaknesses, risks | Minor wording items | Committee reading |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Low leverage and high interest cover on management adjusted EBITDAX | Financial handoff | Debt 2,278,924 and cash 1,977 (S4); trailing adjusted EBITDAX 1,276 (S7); cash interest from S1 and S4 | Sets debt-service capacity and tolerance to a price fall | Supports a moderate risk view | S4 page:21, S7 page:13, S1 page:155, S4 page:36 | Management measure, not covenant EBITDA |
| 2 | Liquidity and maturity profile | Financial handoff | Parent unused 1,140,053 and CNXM unused 533,000 (S4); all debt matures 2029 or later | Liquidity is revolver capacity; refinancing is back-ended | Concentrates refinancing in 2029 | S4 page:20, page:21 | CNXM part not available to the parent |
| 3 | Hedged, single-basin, concentrated-customer revenue | Business handoff | Hedge volumes (S7); market-priced short-term sales (S1); three customers over 10% (S1) | Drives revenue visibility and counterparty risk | Cash flow protected about two years | S7 page:2, S1 page:17, S1 page:156 | Hedge positions as of October 14, 2026 |
| 4 | Buybacks above free cash flow | Business handoff and credit synthesis | Purchases of common stock 434,678 against operating cash flow less capital expenditures of 359,500 (S4) | Shareholder returns draw on revolver headroom | Liquidity erosion if repeated | S4 page:10, page:11 | Inference about funding; periods are nine months |
| 5 | Covenant headroom and legal capacity | Financial and business handoffs | Compliance statements and covenant levels in note text (S4) | Controls default risk and distribution capacity | Cannot be sized without ratios | S4 page:20, page:21 | Credit agreements and indentures not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gross leverage 1.79x, net 1.78x, cover 8.07x | Financial handoff | Inputs in S4, S7, S1; recomputed here (see T5B.5) | Yes | High inputs; management EBITDAX | Calculated | Supported | High | Committee-Ready |
| Liquidity 1,673.053 and maturities from 2029 | Financial handoff | S4 page:19 to page:21 | Yes | High | Calculated | Supported | High | Committee-Ready |
| Hedged, market-priced, concentrated revenue | Business handoff | S7 page:2, S1 page:17, page:156, page:10 | Yes | High and Medium (hedge table is a supplement) | Directly Sourced | Supported | High | Committee-Ready |
| Buybacks exceeded free cash flow | Business handoff and credit synthesis | S4 page:10, page:11, page:35 | Yes | High inputs | Analyst Inference | Partially Supported | Medium | Remediation Needed (label as inference, already tagged) |
| Covenant headroom and legal capacity | Financial and business handoffs | Compliance statements only (S4 page:20, page:21) | Partial | Medium: note summary of unsupplied agreements | Insufficient Information | Insufficient | Low | Not Traceable for headroom |
| Overall moderate credit view | Credit synthesis handoff | Drivers 1 to 5 | Yes | Derived | Analyst Inference | Supported by cited drivers | Medium | Committee-Ready as an interpretation |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Balance-sheet debt at September 30, 2026 is 2,278,924 thousand | pinned text | 10-Q_2026-09-30_cnx-20260930.htm.jsonl | S4 | page:21, Note 10 | Financial base | Sourced | High | Confirmed in chunk |
| Cash and cash equivalents 1,977 and 779 thousand | pinned text | 10-Q_2026-09-30_cnx-20260930.htm.jsonl | S4 | page:8, balance sheet | Financial base | Sourced | High | Confirmed |
| Trailing adjusted EBITDAX 1,276 million | pinned text | EX-99.1_2026-10-29_ex991supplementalq326.htm.jsonl | S7 | page:13 | Leverage chart | Sourced | Medium | Management measure |
| FY2025 adjusted EBITDAX 1,247 million is the sum of four quarters | pinned text | EX-99.1_2026-04-30_ex991supplementalq126.htm.jsonl | S5 | page:12 | Leverage chart | Calculated | Medium | Rounded quarters |
| Cash interest paid FY2025 154,598 thousand, net of amounts capitalized | pinned text | 10-K_2025-12-31_cnx-20251231.htm.jsonl | S1 | page:155, Note 16 | Interest cover chart | Sourced | High | Interim amounts lack the label |
| Cash interest paid nine months 139,234 and 135,812 thousand | pinned text | 10-Q_2026-09-30_cnx-20260930.htm.jsonl | S4 | page:36, Note 16 | Interest cover chart | Sourced | High | Confirmed |
| Parent revolver unused 1,140,053 after 27,097 of letters of credit | pinned text | 10-Q_2026-09-30_cnx-20260930.htm.jsonl | S4 | page:20, Note 8 | Liquidity chart | Sourced | High | Confirmed |
| CNXM revolver unused 533,000; CNX is not a guarantor | pinned text | 10-Q_2026-09-30_cnx-20260930.htm.jsonl | S4 | page:21, Note 8 and Note 10 | Liquidity chart, structure | Sourced | High | Confirmed |
| Covenant levels 3.50 to 1.00 and 1.00 to 1.00; CNXM 5.00, 3.25 and 2.50 | pinned text | 10-Q_2026-09-30_cnx-20260930.htm.jsonl | S4 | page:20, page:21 | Covenants | Sourced | Medium | Summary of unsupplied agreements |
| Hedged volumes 115.0, 461.2, 409.4, 233.1 and 38.2 Bcf | pinned text | EX-99.1_2026-10-29_ex991supplementalq326.htm.jsonl | S7 | page:2 | Operating model | Sourced | Medium | Positions as of 10/14/2026 |
| Substantially all natural gas sold at market prices under short-term contracts | pinned text | 10-K_2025-12-31_cnx-20251231.htm.jsonl | S1 | page:17, Item 1 Marketing | Operating model | Sourced | High | Confirmed |
| Three customers each over 10% of FY2025 customer revenue | pinned text | 10-K_2025-12-31_cnx-20251231.htm.jsonl | S1 | page:156, Note 17 | Operating model | Sourced | High | Confirmed |
| Unconditional purchase obligations 1,248,484 thousand | pinned text | 10-Q_2026-09-30_cnx-20260930.htm.jsonl | S4 | page:28, Note 11 | Claims outside debt | Sourced | High | Confirmed |
| Purchases of common stock 434,678; operating cash flow 810,558; capital expenditures 451,058 | pinned text | 10-Q_2026-09-30_cnx-20260930.htm.jsonl | S4 | page:10 and page:11, cash flow statement | Capital allocation | Sourced | High | Confirmed; comparison is Calculated |
| 5.875% senior notes due March 2034 issued at par on an indenture dated February 26, 2026 | pinned text | 10-Q_2026-09-30_cnx-20260930.htm.jsonl | S4 | page:22, Note 10 | Transactions | Sourced | High | Use of proceeds not stated |
| Convertible notes matured May 1, 2026 and settled in shares | pinned text | 10-Q_2026-09-30_cnx-20260930.htm.jsonl | S4 | page:23, Note 10 | Transactions | Sourced | High | Confirmed |
| Total income taxes paid FY2025 is 7,398 thousand | pinned text | 10-K_2025-12-31_cnx-20251231.htm.jsonl | S1 | page:140, Note 6 | Contradicts the financial handoff's not-supplied statement | Conflicting | High | See CP5-001 |

#### T5B.5 Calculation and assumption register

All items recomputed from inputs extracted from the pinned text; every result agrees with the handoff.

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Adjusted EBITDAX FY2025 | Leverage and cover charts | Quarters 325, 332, 298, 292 (US$m) | Sum of four quarters = 1,247 | Calculated | Supported | High | PD, liquidity | S5 page:12 |
| Trailing adjusted EBITDAX 1,322, 1,280, 1,276 | Charts | Printed trailing totals; check 292 + 400 + 290 + 294 | As printed; four-quarter sum = 1,276 | Calculated | Supported | High | PD | S5 page:14, S6 page:13, S7 page:13 |
| Total debt / adjusted EBITDAX, September 30, 2026 | Leverage chart | Debt 2,278.924; EBITDAX 1,276 | 2,278.924 / 1,276 = 1.786, shown 1.79 | Calculated | Supported | High | Leverage | S4 page:21, S7 page:13 |
| Net debt / adjusted EBITDAX | Leverage chart | Net debt 2,278.924 less 1.977 = 2,276.947 | 2,276.947 / 1,276 = 1.784, shown 1.78 | Calculated | Supported | High | Leverage | S4 page:8, page:21 |
| FY2025 gross and net leverage | Leverage chart | Debt 2,421.359; cash 0.779; EBITDAX 1,247 | 1.94 and 1.94 | Calculated | Supported | High | Leverage | S4 page:9, page:21 |
| Trailing cash interest | Interest cover chart | FY2025 154.598; nine months 139.234 and 135.812 | 154.598 less 135.812 plus 139.234 = 158.020 | Calculated | Supported with basis caveat | Medium | Coverage | S1 page:155, S4 page:36 |
| Interest cover | Interest cover chart | 1,276 and 158.020 | 8.075, shown 8.07 (rounded half to even) | Calculated | Supported | High | Coverage | as above |
| Undrawn facilities September 30, 2026 | Liquidity chart | 1,140.053 and 533.000 | Sum = 1,673.053; parent check 1,400.000 less 232.850 less 27.097 = 1,140.053 | Calculated | Supported | High | Liquidity | S4 page:19 to page:21 |
| Principal by maturity year | Maturity chart | Note 10 principals; revolver maturity May 17, 2029 | 232.85 + 67.000 = 299.85; total 2,299.850 | Calculated | Supported | High | Refinancing | S4 page:19 to page:21 |
| Buybacks less free cash generation | Capital allocation | 434,678; 810,558; 451,058 | 434,678 less 359,500 = 75,178 | Calculated | Supported | High | Liquidity | S4 page:10, page:11 |
| Net revolver borrowings | Capital allocation | CNX 1,549,700 and 1,516,850; CNXM 273,050 and 238,800 | 32,850 + 34,250 = 67,100 | Calculated | Supported | High | Liquidity | S4 page:11 |
| Discrete Q3 amounts | Financial table | Nine-month and six-month amounts | Operating cash flow 253,526; capital expenditures 139,152 (agrees with the segment note total on S4 page:33) | Calculated | Supported | High | Cash flow | S4 page:10 and page:11, S3 page:10 |
| Gross versus net, principal basis | Leverage sensitivity | Principal 2,299.850 | 2,299.850 / 1,276 = 1.80 | Calculated | Supported | High | Leverage | S4 page:21 |
| "Moderate" overall risk view | Credit synthesis | Drivers 1 to 5 | Qualitative; no scale stated | Assumption-Based | Interpretation | Medium | Overall | Credit synthesis |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | 2025 cash taxes not supplied | The annual report prints Total Income Taxes Paid of 7,398 thousand (page:140), so the stated gap is wrong and a trailing cash tax figure is derivable (7,398 less 4,850 plus 7,120 = 9,668) | Conflicting | A wrong limitation understates available evidence; cash taxes bear on free cash flow after tax | Replace with the printed amount and note the net of refunds basis | Financial handoff, financials table and gaps |
| Minor | Strengths text calls the business "long-lived" | No reserve-life figure is cited; the adjective is unsupported | Weak Lineage | Reserve life affects long-term repayment capacity | Delete or support with a stated reserve-life calculation | Credit synthesis, strengths |
| Minor | Overall view is "moderate" risk | No scale defines the label | Analyst Inference | A committee cannot place the label without a scale | Define the scale or state the drivers only | Credit synthesis, credit view |
| Minor | Trailing cash interest mixes bases | A full-year amount net of capitalized interest is combined with interim amounts that carry no such label | Calculated | Could shift cover slightly | Check the interim wording | Financial handoff, interest chart |
| Minor | FY2025 and nine-month adjusted EBITDAX are sums of rounded quarters | Rounding to millions can move the total by a small amount | Calculated | Marginal effect on ratios | None beyond disclosure | Financial handoff, charts |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | All seven filings are pinned and cited; executed legal documents, ratings and proxy are not supplied | Covenant, guarantee and ownership claims rest on summaries | Legal capacity and headroom stay out of reliance | Obtain the documents |
| Citation completeness | Ready with Remediation | Every register row carries a file and chunk; one limitation statement contradicts a filing | A wrong gap hides available evidence | Cash tax analysis is incomplete, credit metrics unaffected | Correct CP5-001 |
| Calculation traceability | Committee-Ready | All derived figures recompute from source inputs | Reproducible ratios | Leverage, cover and liquidity can be relied on as management-measure results | None |
| Assumption transparency | Ready with Remediation | Management EBITDAX and the moderate label are disclosed but one label lacks a scale | Undefined scale limits reading | Interpretive wording only | Define or drop the label |
| Markdown and export artifact integrity | Committee-Ready | Required headings, tables and hashes present in each handoff; the six-heading structure is the run transport | Format defects would break ingestion | None | None |

Overall auditability: Ready with Remediation (lowest of the five dimensions).

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed credit agreements and indentures | Documents listed as exhibits, not supplied | Covenant definitions, security and guarantees cannot be verified | Covenants, structure | High impact | Exhibit filings |
| CP-5-GAP-002 | Covenant ratios and headroom | Compliance certificate | Headroom against leverage and current-ratio tests is unknown | Leverage, liquidity | High impact | Compliance certificate |
| CP-5-GAP-003 | 2025 cash taxes statement | Printed amount in the annual report, page:140 | Free cash flow after tax | Financial table | Low impact | Annual report income tax note |
| CP-5-GAP-004 | Ratings, market data, proxy statement | None in pack | No external view or holder detail | Whole assessment | Medium impact | External sources, labelled |
| CP-5-GAP-005 | Documents after October 29, 2026 | None in pack | Events before the cutoff are unknown | Subsequent events | Low impact | Later filings |
| CP-5-GAP-006 | Confidence score script and specification | Not among pinned inputs | Numeric score cannot be computed | QA status | Medium impact | Scoring specification |
| CP-5-GAP-007 | Use of proceeds of the 2034 notes | Offering document | Link to the 2029 repurchase is an inference | Capital allocation | Low impact | Offering document |

#### T5.1 QA module register

Module status: Ready with Limitations.

| Module | Handoff canonical file / run id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | Readiness handoff, run cnx-2026-11-05-credit_snapshot-host | Source readiness | High | Six run headings present; no YAML envelope in this transport | Passed on audit | Source claims verified |
| CP-1 | Financial handoff, same run | Financial data and charts | High | Six run headings and selector headings present | Restricted (CP5-001) | Figures recompute |
| CP-1A | Business handoff, same run | Business and transaction | High | Six run headings and selector headings present | Passed on audit | Facts verified |
| CP-2 | Credit synthesis handoff, same run | Credit view | Medium | Six run headings and selector headings present | Passed with minor items | Two wording items |
| CP-5 | This review | Evidence trace | Not applicable | Present | Restricted | Self-review excluded |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1 | 2025 cash paid for income taxes "Not supplied" | Conflicting | Annual report page:140 prints 7,398 thousand | Replace with the printed amount | Restricts committee use until corrected |
| MINOR | CP-2 | Business "large and long-lived" | Unsupported | No reserve-life figure cited | Delete or support | Presentation |
| MINOR | CP-2 | "Moderate" credit risk | Partially Supported | No defined scale | Define the scale | Interpretation only |
| None | CP-1A | Absence of creditor-adverse actions | Supported with limit | Bounded to seven filings and stated so | None | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Trailing cash interest | Full-year net of capitalized interest plus interim amounts without that label | None found | Check interim wording | Monitoring |
| MINOR | CP-1 | FY2025 adjusted EBITDAX | Sum of rounded quarters | None | None beyond disclosure | None |
| None | CP-1, CP-2 | Leverage definition | Management adjusted EBITDAX versus balance-sheet debt; covenant definition differs and is disclosed; no definition drift between modules | None | Keep labelled | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A | Covenant tests, guarantors, security and CNXM separation | Executed credit agreements and indentures | Note summaries only; the modules label them as summaries and leave security and legal capacity as Insufficient Information | Obtain documents when conclusions on capacity are needed | Legal Review Required before any capacity or headroom use |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | All | No price, spread, yield, rating or peer claim is made; the context holds no market inputs | Market data not provided | None needed for the claims made | None | None; relative value is out of scope |

#### T5.6 Cross-module consistency and version-control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| None | CP-0, CP-1, CP-1A, CP-2 | None found. Checked and consistent across modules: issuer and perimeter, debt 2,278.924, adjusted EBITDAX 1,276, leverage 1.79x and 1.78x, cover 8.07x, liquidity 1,673.053, maturities from 2029, buyback comparison of 434,678 against 359,500, hedge volumes, parent and CNXM separation | One logged difference on the Utica payment (16 million versus 16,500 thousand) is a rounding difference and is already logged and not reconciled; the readiness handoff's earlier wording on Q4 2025 was refined by the financial handoff | None | None |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Duplication | Liquidity, buyback and maturity figures repeat across the financial, business and synthesis handoffs | Keep repetition to what each module needs | Slight reading load |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Envelope and headings | The handoffs use the run's six headings and no YAML front matter, so the generic envelope fields, evidence trace and source registry headings are absent by design of the transport; hashes, sources and locators are inside Sources and the tables | Note the transport difference; no change needed for this run | None; CP-OS accepted each handoff |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-1 | Incorrect limitation | 2025 cash taxes stated as not supplied; 7,398 thousand is printed (page:140) | Replace with printed amount | Restricts committee use | Open |
| CP5-002 | MINOR | CP-2 | Unsupported adjective | "long-lived" with no reserve-life support | Delete or support | Presentation | Open |
| CP5-003 | MINOR | CP-2 | Undefined label | "Moderate" risk without scale | Define scale | Interpretation | Open |
| CP5-004 | MINOR | CP-1 | Mixed basis | Trailing cash interest combines labelled and unlabelled bases | Check wording | Monitoring | Open |
| CP5-005 | MINOR | CP-1 | Rounding | Sums of rounded quarters in adjusted EBITDAX | Disclosure only | None | Open |
| CP5-006 | MINOR | CP-1, CP-1A | Source limitation | Legal terms from summaries only | Obtain documents | Legal review dependency | Open |
| CP5-007 | MINOR | All | Envelope | Six-heading transport without YAML envelope | Note only | None | Open |
| CP5-008 | MINOR | CP-1, CP-1A, CP-2 | Duplication | Repeated figures across handoffs | Trim | Slight | Open |

## Calculations

Independent recomputation of every derived figure listed in the calculation register, from inputs extracted directly from the pinned text rather than from the handoffs: adjusted EBITDAX FY2025 is 325 + 332 + 298 + 292 = 1,247; trailing totals 1,322, 1,280 and 1,276 as printed (292 + 400 + 290 + 294 = 1,276); gross leverage 2,278.924 / 1,276 = 1.786; net leverage 2,276.947 / 1,276 = 1.784; FY2025 leverage 2,421.359 / 1,247 = 1.942; trailing cash interest 154.598 less 135.812 plus 139.234 = 158.020; cover 1,276 / 158.020 = 8.075 and 1,247 / 154.598 = 8.066; undrawn 1,140.053 + 533.000 = 1,673.053; buyback excess 434,678 less 359,500 = 75,178; net revolver borrowings 32,850 + 34,250 = 67,100; discrete Q3 capital expenditures 451,058 less 311,906 = 139,152, equal to the segment note total. Trailing cash taxes for the corrected item: 7,398 less 4,850 plus 7,120 = 9,668 thousand (indicative; the annual figure is net of refunds). All results agree with the handoffs to the stated rounding.

## Gaps

The gaps ledger above (CP-5-GAP-001 to CP-5-GAP-007) is the complete list. The binding ones are the absent executed legal documents and covenant ratios, which keep legal capacity and headroom conclusions out of committee reliance, and the correctable cash tax statement. The numeric confidence score and the mechanical completeness script were not available among the pinned inputs, so the score is not asserted and the status rests on the severity rules.

## Next module

This is the last module of the run. Before the report is used, correct the cash taxes statement in the financial handoff (CP5-001) in a new run or in the report text, and re-audit when the credit agreements, indentures and a compliance certificate are supplied.
