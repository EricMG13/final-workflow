## Request

Vestis Corp (VSTS, issuer id vsts), as of 2026-11-05, credit snapshot pathway: an independent evidence trace and research integrity review of the four accepted handoffs (source readiness, financial base, business and transaction context, credit synthesis) against the seven pinned issuer sources. This module audits and grades; it does not change the credit conclusion or repair lineage. Figures are USD; the latest period is Q3 FY2026, the quarter ended July 3, 2026.

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 |
| --- | --- |
| 10-K_2025-10-03_vsts-20251003.htm.jsonl | 69acf45c43af00eb0ad3afdad499957974d6855c0a4c69b858d3f2f1a0defa4d |
| 10-Q_2026-01-02_vsts-20260102.htm.jsonl | 637925692f36f8779f60ebbc11d3252e4fe1f1a5077b706d2e2b4b1b4f6edc05 |
| 10-Q_2026-04-03_vsts-20260403.htm.jsonl | ba2978bcc5b4cdc3b18b43c2c9ae31ce0a31d87a366091d84bc271a3c594f858 |
| 10-Q_2026-07-03_vsts-20260703.htm.jsonl | 7db2f115581c382fda3a1a642c3240840cc03e0b4154737c2546ddd28c46a9af |
| EX-99.1_2026-02-10_vstsq1fy26earningsrelease-.htm.jsonl | 73cf4915cc22c7c9a6d41b209e21e1301c8d95ee51da8c8656b7c37a3072aacd |
| EX-99.1_2026-05-12_vstsq2fy26earningsrelease-.htm.jsonl | e70477c8d46036f4ef7bd70b6551daa75ee805b6eb9bc6e0504e90f227edd1d1 |
| EX-99.1_2026-08-11_vstsq3fy26earningsrelease-.htm.jsonl | d2693610d697f7e33edfd6b5f9d57dc6906301a18a12d6a3feec8645e5a3af14 |

Run context (settings only, not issuer evidence): context, sha256 c28ff4b5be1db183138bacbfdcd7f4640157e3a21bdc54358648d894f8fed07c.

### Supplied handoffs

| Module | sha256 | Reviewed for |
| --- | --- | --- |
| CP-0 | fb64725ea4a061e1ccbb327ea1648238e8928972fee966ac507aa72bbbb573c2 | Readiness claims and limitations |
| CP-1 | 885870b4672dfea8973940557a2d24917debec5a820a3ff44934bc123d031955 | Figures, calculations, locators, period and definition consistency |
| CP-1A | c554b3d7796c7d2a04977f4bbc28bd611c0e1d2c91843e4c5a928f4f5ae25623 | Quotations, categories, locators, consistency with the financial handoff |
| CP-2 | 9bc6bc469ef4ebfb2f2179afff2b40f2bed36bf43796c6cf5a5859073f98a24d | Figure identity with upstream, category tags, scope limits |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The research traces well to the filings and is consistent across modules. It is cleared with remediation but restricted for covenant-dependent decisions, because covenant terms are company summaries and trailing twelve month figures include a 53rd week. | Medium | Executed credit documents are not supplied, so covenant levels, definitions and the receivables facility treatment cannot be verified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every quotation and tabulated figure tested was found at its cited page, and values agree across the four reports. | Debt, liquidity and leverage inputs can be relied on as filed or as company-reported. | High |
| All four trailing twelve month windows contain the 14-week fourth quarter of fiscal 2025, which the reports did not state. | Trailing leverage and cover are flattered by about USD 6.5 million of EBITDA, modest against the covenant cushion. | Medium |
| Two company figures for fiscal 2025 Adjusted EBITDA and the covenant treatment of sold receivables remain unreconciled. | Leverage and headroom carry definition risk; the reports disclosed both. | Medium |
| One business report row carries two categories, and some inference in the synthesis is not tagged as interpretation. | Presentation defects only; the credit conclusion is unaffected. | High |

### Evidence trace view

The analysis is traceable enough for committee screening but not for covenant-dependent decisions. The quotations and tabulated figures tested were found at their cited pages, and values agree across the four reports. The strongest support is that debt, liquidity, leverage and cash flow tie to filed statements and notes. The most important provenance gap is that covenant levels and definitions come from company summaries because the executed credit agreement is not supplied, and the company's two figures for fiscal 2025 Adjusted EBITDA are unreconciled. This review also found that every trailing twelve month window contains the 14-week fourth quarter of fiscal 2025, which the reports did not state. The research is cleared with remediation and restricted for committee use until those items are addressed.

### Clearance decision

| Item | Decision | Basis |
| --- | --- | --- |
| Committee clearance | Pass with Remediation | No unresolved Critical issue; at least one Material issue requires correction or limitation disclosure |
| Committee status | Restricted | Covenant and definition statements are company-reported and unverified |
| Research QA status | Restricted | Material issues open; the confidence score is script-owned and was not run in this transport, so no numeric score is stated |
| Credit conclusion | Unchanged | This review does not alter the synthesis |

### Top drivers and traceability

| Rank | Driver | Originating report | Traceability | Classification |
| --- | --- | --- | --- | --- |
| 1 | Reported net leverage fell from 4.72x to 4.10x against a 5.00x maximum | Financial base | Fully traced to the net leverage table and covenant schedule; ratio is company-reported | Directly Sourced, company non-GAAP |
| 2 | Covenant maximum steps down to 4.75x then 4.50x, cushion narrows | Financial base | Schedule traced; cushion calculated and recomputed here | Directly Sourced and Calculated |
| 3 | Liquidity of USD 351.8 million and bank maturities only in fiscal 2028 and fiscal 2031 | Financial base | Traced to the liquidity table and debt note; maturities derived | Directly Sourced and Calculated |
| 4 | Receivables facility ends August 2, 2027 with USD 212.3 million sold | Financial base and business context | Traced to the MD&A liquidity section; covenant treatment unresolved | Directly Sourced; treatment Analyst Inference |
| 5 | Recovery rests on a transformation plan with savings quantified by management | Business context | Savings are management statements; cost estimate change traced to two filings | Management Language and Directly Sourced |

### Analytical appendix — complete canonical registers

#### Handoff register

| Module | Handoff canonical .md / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/.../1.response.md, sha256 fb64725e...; run vsts-2026-11-05-credit_snapshot-host | Source readiness of seven sources | High for filings, Medium for releases | All six H2 headings present | Pass with Remediation | A statement that no filing-to-release conflict was found is still true, but later reports found conflicts inside the releases |
| CP-1 | requests/CP-1/.../1.response.md, sha256 885870b4...; same run | Financial base | High for filed figures, Medium for company non-GAAP | All six H2 headings and selectors present | Pass with Remediation | Trailing windows not flagged as 53-week; otherwise reconciled |
| CP-1A | requests/CP-1A/.../1.response.md, sha256 c554b3d7...; same run | Business, ownership, transaction, governance | High for filed facts, Low for management claims | All six H2 headings and selectors present | Pass with Remediation | One row tagged with two categories |
| CP-2 | requests/CP-2/.../1.response.md, sha256 9bc6bc46...; same run | Credit synthesis | Medium (upstream only) | All six H2 headings and selectors present | Pass with Remediation | Figures identical to upstream; some inference untagged |

#### Source quality register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-10-03_vsts-20251003.htm.jsonl | High, filed and audited | Fiscal 2025, 53 weeks to October 3, 2025 | Vestis Corporation consolidated | Statements, debt note, maturities, covenants, leases, business, litigation | Text extraction; tables flattened | Base year, structure, business |
| S2 | 10-Q_2026-01-02_vsts-20260102.htm.jsonl | High, filed unaudited | Q1 FY2026 | Same | Balance sheet, debt note, cash interest | Unaudited | Quarterly balances |
| S3 | 10-Q_2026-04-03_vsts-20260403.htm.jsonl | High, filed unaudited | Q2 FY2026 | Same | Balance sheet, debt note, six month cash interest | Unaudited | Quarterly balances |
| S4 | 10-Q_2026-07-03_vsts-20260703.htm.jsonl | High, filed unaudited | Q3 FY2026 | Same | Statements, debt, leases, segments, MD&A, litigation | Unaudited | Latest period |
| S5 | EX-99.1_2026-02-10_vstsq1fy26earningsrelease-.htm.jsonl | Medium, management-attributed | Q1 FY2026 | Same | Net debt, liquidity, reconciliations | Non-GAAP | Cross-check |
| S6 | EX-99.1_2026-05-12_vstsq2fy26earningsrelease-.htm.jsonl | Medium, management-attributed | Q2 FY2026 | Same | Net debt, liquidity, outlook | Non-GAAP | Cross-check |
| S7 | EX-99.1_2026-08-11_vstsq3fy26earningsrelease-.htm.jsonl | Medium, management-attributed | Q3 FY2026 | Same | Reconciliations, trailing twelve months, net leverage, liquidity, outlook | Non-GAAP, forward-looking | Covenant ratio, EBITDA |

#### Top five material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Company-reported net leverage 4.10x against 5.00x maximum | CP-1 | Net leverage table and covenant schedule | Maintenance test is the main default trigger | Headroom judgement | S7 page:16; S4 page:20 | Company-defined; executed agreement not supplied |
| 2 | Step-downs to 4.75x and 4.50x | CP-1 | Covenant schedule | Cushion narrows on known dates | Monitoring triggers | S4 page:20; S1 page:115 | Static constant-net-debt sensitivity |
| 3 | Liquidity USD 351.8 million and maturity profile | CP-1 | Liquidity table, debt note | Funds debt service and plan costs | Liquidity adequacy | S7 page:16; S4 page:19 and page:20 | Receivables facility capacity not supplied |
| 4 | Receivables facility end and treatment | CP-1, CP-1A | MD&A liquidity section, covenant definition | Funding event and covenant ambiguity | Refinancing watch | S4 page:50 and page:52 | Facility documents not supplied |
| 5 | Transformation plan delivery | CP-1A, CP-2 | Plan description and release | Earnings recovery and cost risk | Execution monitoring | S4 page:42; S7 page:2; S1 page:147 | Savings are management claims |

#### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net leverage 4.10x, liquidity USD 351.8 million | CP-1, CP-2 | S7 page:16 | Yes | Medium | Directly Sourced | Supported | Medium | Traced |
| Principal debt 1,097,500 thousand, term loans and zero revolver | CP-1 | S4 page:19 | Yes | High | Directly Sourced | Supported | High | Traced |
| Maturities in fiscal 2028 and fiscal 2031 | CP-1 | S4 page:19 and page:20; S1 page:113 and page:116 | Yes | High | Calculated | Supported | Medium | Traced |
| Covenant maximum schedule | CP-1, CP-2 | S4 page:20; S1 page:115 | Yes | High | Directly Sourced | Supported | Medium | Traced to summary, not executed text |
| Cash interest paid, cover ratios | CP-1 | S4 page:16; S3 page:16; S2 page:15; S1 page:113 | Yes | High | Calculated | Partially Supported | Medium | Traced; rounded inputs |
| Recurring rental 95%, customers, Mexico 60% | CP-1A, CP-2 | S1 page:10, page:11, page:13 | Yes | High | Directly Sourced | Supported | High | Traced |
| Plan savings and cost estimate | CP-1A, CP-2 | S4 page:42; S7 page:2; S1 page:147 | Yes | Medium | Management Language | Supported as management claim | Medium | Traced |
| Sold receivables sensitivity 4.82x and 5.45x | CP-1, CP-2 | Calculated from S7 page:16, S4 page:50, S1 page:147 | Yes | Medium | Analyst Inference | Partially Supported | Low | Traced; not a covenant measure |
| Governance and litigation | CP-1A, CP-2 | S1 page:126, page:156; S4 page:29, page:56 | Yes | High | Directly Sourced | Supported | Medium | Traced |
| Thesis that the debt can be sustained through two years | CP-2 | Upstream judgement | Partly | Medium | Analyst Inference | Partially Supported | Medium | Conditional wording; no forward test |

#### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net leverage 4.10x, 4.47x, 4.83x, 4.72x | source-text | EX-99.1_2026-08-11_vstsq3fy26earningsrelease-.htm.jsonl | S7 | page:16 | CP-1 Financial base | Release table | Medium | Recomputed 1,205,382 / 294,037 equals 4.099 |
| Total liquidity 351,841 | source-text | same | S7 | page:16 | CP-1 Chart data liquidity | Release table | Medium | Recomputed 294,182 plus 57,659 |
| Term loan A-2 436,000, term loan B-1 661,500, revolver nil | source-text | 10-Q_2026-07-03_vsts-20260703.htm.jsonl | S4 | page:19 | CP-1 Period-end table | Debt note | High | Total 1,097,500 recomputed |
| Covenant maxima 5.00x, 4.75x, 4.50x; minimum interest cover 2.00x | source-text | same | S4 | page:20 | CP-1 and CP-2 | Debt note summary | High | Summary of executed terms |
| Covenant indebtedness includes receivables facility advances | source-text | same | S4 | page:52 | CP-1 Definition risks | MD&A | High | Source of the open definition question |
| Receivables sold 212.3 million, facility ends August 2, 2027 | source-text | same | S4 | page:50 | CP-1, CP-2 | MD&A liquidity | High | Quarterly series from S2 and S3 |
| FY2025 cash interest 93.6 million | source-text | 10-K_2025-10-03_vsts-20251003.htm.jsonl | S1 | page:113 | CP-1 Cover chart | Debt note | High | Rounded to one decimal |
| FY2025 Adjusted EBITDA 257,425 and 272.6 million | source-text | S7 file | S7 | page:14; page:4 | CP-1 Definition risks | Release tables | Medium | Conflict preserved |
| Plan cost 25 to 30 million then 35 to 40 million | source-text | S1 and S4 files | S1, S4 | page:147; page:42 | CP-1A Conflicts | Notes and MD&A | High | Conflict by date |
| Recurring rental 95%, ten largest customers under 10% | source-text | S1 file | S1 | page:10; page:11 | CP-1A | Business section | High | Company statements |
| 53rd week: revenue 51.6 million, cost of services 37.9 million, SG&A 7.2 million | source-text | S1 file | S1 | page:68 | This review | MD&A | High | Used for the period finding |
| Fiscal 2025 had 53 weeks | source-text | S1 file | S1 | page:65 | CP-1, this review | MD&A | High | Fourth quarter length derived from printed quarter-end dates |

#### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total and net debt over trailing EBITDA | CP-1 leverage chart | Principal debt, finance leases, cash, trailing Adjusted EBITDA at four dates | (debt + leases) / EBITDA; less cash for net | Recomputed and matches: 5.19, 5.37, 4.72, 4.33 and 5.07, 5.20, 4.54, 4.13 | Supported | High | Leverage trend | S7 page:16; S4 page:19 |
| Trailing cash interest | CP-1 cover chart | FY2025 93.6 plus year-to-date less prior year-to-date | 93.6 + 55.7 - 64.7 = 84.6 and equivalents | Recomputed and matches: 93.6, 90.5, 88.1, 84.6 | Supported, rounded | Medium | Cover | S1 page:113; S2 page:15; S3 page:16; S4 page:16 |
| EBITDA over cash interest | CP-1 | As above | 290.437 / 84.6 = 3.433 | Recomputed and matches: 2.75, 2.72, 3.11, 3.43 | Supported | Medium | Cover | S7 page:14 |
| Covenant cushion | CP-1, CP-2 | Company Net Debt, covenant EBITDA, maxima | EBITDA less Net Debt / maximum | Recomputed and matches 52,961 (18.0%), 40,272 (13.7%), 26,174 (8.9%) | Supported | Medium | Headroom | S7 page:16; S4 page:20 |
| Free cash flow and conversion | CP-1, CP-2 | Operating cash flow and purchases | OCF - purchases; LTM 191,800 - 55,389 = 136,411; 136,411 / 290,437 = 47.0% | Recomputed and matches | Supported | Medium | Cash generation | S7 page:13 and page:14; S1 page:91 |
| Sold receivables sensitivity | CP-1, CP-2 | Net Debt plus sold balance | (1,205,382 + 212,300) / 294,037 = 4.82; (1,310,875 + 202,500) / 277,825 = 5.45 | Recomputed and matches; illustrative only | Partially Supported | Low | Definition risk | S7 page:16; S4 page:50; S1 page:147 |
| 53rd week contribution (this review) | I-01 | 10-K exclusion figures: revenue 51.6, cost of services 37.9, SG&A 7.2 (US$ millions) | 51.6 - 37.9 - 7.2 = 6.5 | Indicative; extra-week EBITDA not disclosed | Analyst Judgement | Low | Period comparability | S1 page:68 |
| Effect of removing it (this review) | I-01 | Trailing windows at July 3, 2026 | (290.437 - 6.5) gives chart net debt over EBITDA 4.22x against 4.13x; (294.037 - 6.5) gives company ratio 4.19x against 4.10x; cushion 46.5 against 53.0 (US$ millions) | Indicative; does not change the 5.00x test result | Analyst Judgement | Low | Headroom sensitivity | S7 page:14 and page:16 |

#### Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Trailing twelve month leverage, cover and conversion | Windows include a 14-week quarter; only the fiscal 2025 column was flagged as 53 weeks | Period Mismatch | Ratios are modestly flattered and the 52-week test at October 2, 2026 will not include the extra week | State the 53-week basis; restate on 52 weeks when quarterly data allow | CP-1 charts; CP-2 leverage statements |
| Material | Covenant headroom | Levels and definitions rest on summaries | Source Quality Limitation | Headroom may differ under executed definitions | Obtain executed agreement and amendments | CP-1, CP-2 |
| Minor | Sold receivables treatment | Explanation that receivables would return to the balance sheet if the facility ended is inference, not tagged as such | Partially Supported Claim | Mechanism is plausible but not stated in the sources | Tag as Analyst Interpretation | CP-2 Key findings |
| Minor | Pricing and volume row | Row carries two categories where the method requires one | Evidence Trace Defect | Mixes documentary fact and management claim | Split into two rows | CP-1A Company and operating model |
| Minor | Scheduled amortization | Latest 10-Q repeats a requirement of 2.0 million quarterly principal on the B-1 tranche while the 10-K says obligations were met through maturity | Conflicting Evidence | Zero scheduled maturities in FY2026 to FY2030 rests on the 10-K statement | Confirm against the executed agreement | CP-1 maturity chart |

#### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Citation presence and exact match | Strong | Every quotation in the business report matched its cited page (the sector label comes from the run context and is labelled as such); tabulated figures matched cited pages | Low orphan-claim risk | Facts can be relied on as filed | None |
| Calculation reproducibility | Strong | All listed calculations recomputed to the stated rounding | Low arithmetic risk | Ratios reproducible | State 53-week basis |
| Cross-module consistency | Strong | Figures in the synthesis match the financial and business reports | Low contradiction risk | One story across modules | None |
| Definition control | Moderate | Company ratio, chart ratio, covenant definition and sold receivables are distinct and disclosed | Definition drift can mislead if cited alone | Headroom must be labelled company-reported | Executed documents |
| Period control | Moderate | Latest period, context period and 53-week windows are differently handled | Period mismatch can flatter trends | Trend slightly overstated | Add 53-week label |
| Management claim control | Strong | Savings and operating metrics tagged as Management Language | Low risk of silent adoption | Plan benefits are not treated as fact | None |

#### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Executed credit agreement and amendments | Operative covenant text and definitions | Verifies headroom and sold receivable treatment | Covenant statements are company-reported | Caps confidence at Medium | Executed agreement |
| G2 | Receivables facility documents | Facility terms, availability, renewal | Funding event in fiscal 2027 | Liquidity excludes the facility | Lowers liquidity confidence | Facility agreement |
| G3 | Extra-week EBITDA | Earnings contribution of the 53rd week | Sizes the period distortion | Only an indicative 6.5 million estimate | Lowers precision | Management disclosure |
| G4 | Fiscal 2025 Adjusted EBITDA reconciliation | Bridge from 257,425 thousand to USD 272.6 million | Prior-year leverage level | Conflict preserved | Lowers prior-period confidence | Company reconciliation |
| G5 | Evidence after August 11, 2026 | Later filings, fiscal quarter ending October 2, 2026 | Next covenant test | Latest period is Q3 FY2026 | Currentness limit | Later filings |
| G6 | Ratings, market data | External views | None used | No relative value claims possible | Not applicable to confidence | Market data provider |

#### Handoff and claim audit (claims)

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Trailing twelve month ratios | Partially Supported | 53-week windows not stated | Add basis label | Requires Calculation Rebuild |
| Minor | CP-2 | Receivables would return to the balance sheet if the facility ended | Partially Supported | Inference not tagged | Tag as interpretation | Formatting / Hygiene Only |
| Minor | CP-2 | Thesis that debt can be sustained through the next two years | Partially Supported | Conditional but no forward test at October 2, 2026 | Soften wording or add a forward test | Monitoring Follow-Up |
| Minor | CP-1A | Pricing and volume row | Supported | Two categories on one row | Split row | Formatting / Hygiene Only |
| Minor | CP-1 | Zero scheduled maturities FY2026 to FY2030 | Partially Supported | Two filings differ on amortization wording | Confirm in executed agreement | Monitoring Follow-Up |

#### Metric and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1 | Trailing windows are 53 weeks | LTM definition not adjusted for the 14-week fourth quarter | Fiscal 2026 is a 52-week year | Label and, when possible, restate | Requires Calculation Rebuild |
| Material | CP-1, CP-2 | Net leverage as reported versus covenant | Covenant indebtedness includes receivables facility advances; company Net Debt shows none | Filing definition versus release table | Obtain executed definition | Requires Source Reconciliation |
| Material | CP-1 | Fiscal 2025 Adjusted EBITDA 257,425 thousand versus USD 272.6 million | Reconciled versus outlook-table figure | Release against release | Obtain bridge | Requires Source Reconciliation |
| Minor | CP-1 | Cash interest from rounded millions | Rounding on trailing sums | None | Disclosed already | Formatting / Hygiene Only |
| Minor | CP-1 | Fiscal 2025 free cash flow 5,769 thousand versus USD 5.9 million in the outlook table | Rounding or definition | Release against calculation | Note only | Formatting / Hygiene Only |

#### Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Covenant maxima, minimum interest cover, dividend and buyback restriction | Executed credit agreement and Amendment No. 2 | Only note and MD&A summaries supplied | Obtain documents | Required before reliance |
| Material | CP-1, CP-2 | Receivables facility treatment in covenant indebtedness | Receivables purchase agreement and credit agreement definitions | Definition not supplied | Obtain documents | Required |
| Minor | CP-1 | All debt guaranteed and secured on substantially all tangible assets | Security documents | Summary from the 10-K only | Obtain if recovery work is later requested | Not required for this view |
| Minor | CP-1A | Tax-free spin-off restrictions and indemnification | Tax matters and separation agreements | Exhibits by reference only | Obtain if exposure is to be sized | Not required for this view |

#### Market and relative value audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | No market, spread, rating or peer claim is made, and none is supported | Ratings, prices, spreads, peer set | Context supplies none | None; keep absent | None for this view; relative value cannot be started |

#### Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Fiscal 2025 Adjusted EBITDA 257,425 thousand versus USD 272.6 million | Same release family, different tables | Preserve both; obtain bridge | Prior-year leverage level uncertain |
| Material | CP-1, CP-2, CP-0 | Covenant ratio definition versus company Net Debt | Filing versus release | Obtain executed definition | Headroom label |
| Minor | CP-1A, CP-2 | Plan cost estimate 25 to 30 million versus 35 to 40 million | Earlier versus later filing | Use the later estimate | None |
| Minor | CP-0, CP-1 | Readiness statement that no filing-to-release conflict was found | Superseded in part by findings inside the releases | CP-1 states the correction | None |
| Minor | All | Context period q2-2026 versus latest period Q3 FY2026 | Context versus filings | All reports label Q3 FY2026 as latest | Confirm intended period |

#### Duplication and materiality

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A, CP-2 | Duplicative content | The missing executed documents caveat is restated in each report | Keep once in committee material | Hygiene only |
| Minor | CP-1A | Immaterial content | Detailed timeline rows of limited credit relevance (exhibit signatures) | Trim in committee material | Hygiene only |

#### Handoff envelope audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Selector table categories | One row has two categories | Split row | None for ingestion |
| Minor | CP-2 | Basis references | Basis cites section names, not row identifiers, as the Markdown transport has none | None | None |

#### Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | Material | CP-1, CP-2 | Period Mismatch | Trailing twelve month windows at all four dates contain the 14-week fourth quarter of fiscal 2025; indicative extra-week EBITDA about 6.5 million (US$) | Label 53-week basis; restate when data allow | Requires Calculation Rebuild | Open |
| I-02 | Material | CP-1, CP-2, CP-0 | Formula / Definition Drift | Receivables facility treatment in covenant leverage unresolved | Obtain executed definition | Requires Source Reconciliation | Open, disclosed |
| I-03 | Material | CP-1, CP-2 | Conflicting Evidence | Two fiscal 2025 Adjusted EBITDA figures | Obtain bridge | Requires Source Reconciliation | Open, disclosed |
| I-04 | Material | CP-1, CP-2 | Legal Support Gap | Covenant terms rest on summaries | Obtain executed documents | Restricts Committee Use | Open, disclosed |
| I-05 | Minor | CP-2 | Partially Supported Claim | Receivables mechanism inference untagged | Tag as interpretation | Formatting / Hygiene Only | Open |
| I-06 | Minor | CP-2 | Partially Supported Claim | Thesis lacks a forward covenant test | Soften or add test | Monitoring Follow-Up | Open |
| I-07 | Minor | CP-1A | Evidence Trace Defect | One row carries two categories | Split row | Formatting / Hygiene Only | Open |
| I-08 | Minor | CP-1 | Conflicting Evidence | Amortization wording differs between filings | Confirm in agreement | Monitoring Follow-Up | Open |

#### Remediation priority

| Priority | Issue IDs | Action | Owner | Timing |
| --- | --- | --- | --- | --- |
| 1 | I-02, I-03, I-04 | Obtain the executed credit agreement, amendments, receivables facility documents and the Adjusted EBITDA bridge | Research lead | Before any covenant-dependent decision |
| 2 | I-01 | Add a 53-week label to trailing ratios and restate on a 52-week basis as data allow | Analyst | Next refresh |
| 3 | I-05 to I-08 | Tag, split and confirm the minor items | Analyst | Next refresh |

## Calculations

Recomputations performed in this review, all from figures printed in the sources or in the reports (US$ unless stated):

- Fourth quarter length of fiscal 2025: quarter ends June 27, 2025 and October 3, 2025 are 98 days apart, which is 14 weeks; the other quarters tested (September 27, 2024 to December 27, 2024, and October 3, 2025 to January 2, 2026) are 91 days, or 13 weeks. Every trailing window ending at October 3, 2025, January 2, 2026, April 3, 2026 and July 3, 2026 contains that 98-day quarter.
- Indicative extra-week EBITDA: 51.6 million of revenue less 37.9 million of cost of services less 7.2 million of SG&A equals 6.5 million (S1 page:68). This is a reviewer estimate from the company's own exclusion figures, not a disclosed EBITDA.
- Indicative effect at July 3, 2026: chart net debt over EBITDA is 1,199.564 / (290.437 - 6.5) = 4.22x against 4.13x; company ratio is 1,205.382 / (294.037 - 6.5) = 4.19x against 4.10x; cushion to the 5.00x maximum is 294.037 - 6.5 - 1,205.382 / 5.00 = 46.5 million against 53.0 million (US$ millions). The 5.00x test is passed either way, so the finding is Material, not Critical.
- Recomputation of the financial handoff's ratios, cushions, free cash flow, trailing cash interest and sensitivities matched the stated values to the stated rounding in every case (register above).
- Cross-module identity: every figure in the synthesis was found in the financial or business handoff with the same value, unit and period.

## Gaps

Readiness: the review is complete for the quotations, tabulated figures and calculations tested; it did not re-read every narrative sentence of the source filings, and it could not review extraction fidelity of flattened tables beyond the pages opened. Residual gaps: executed credit documents, receivables facility documents, the extra-week earnings contribution, the fiscal 2025 Adjusted EBITDA bridge and any evidence after August 11, 2026 (see the gaps ledger above). The numeric confidence score is script-owned and was not computed in this transport; the qualitative status is Restricted at Medium confidence in the underlying evidence.

## Next module

This is the final module of the run. Deliver the report with the clearance decision (Pass with Remediation, committee status Restricted), the open items I-01 to I-04 shown to committee readers, and the instruction to label covenant statements as company-reported and trailing ratios as 53-week windows until the executed documents and a 52-week restatement are available.
