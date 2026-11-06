## Request

Synchrony Financial (issuer id syf) is reviewed as of 2026-11-05 on the credit_snapshot pathway: this evidence trace and research-integrity review covers the four upstream handoffs (source readiness, financial base, business and transaction context, fundamental synthesis) against the seven pinned issuer documents. Current period Q3 2026, prior period FY2025, reporting currency USD. The review changes no credit conclusion and repairs no lineage silently.

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_syf-20251231.htm.jsonl | 0b60c3e342553b852e824b86621a2fdaa6ad093dc06c4e55a2eed5e6cf19d9d4 |
| 10-Q_2026-03-31_syf-20260331.htm.jsonl | 25bad560fab9d89eaa95fa105d6deb566b793ff4487d93802c1c0d41e804e06c |
| 10-Q_2026-06-30_syf-20260630.htm.jsonl | e78db7390d45896274c6d04cfc239ed8817a6d1e34b0f8639e41e84d8aaaf93a |
| 10-Q_2026-09-30_syf-20260930.htm.jsonl | bb3d956d892f83bdc99a4d6e03538bf27003f138c169bcc3d1bc7e8f04cc2a06 |
| EX-99.1_2026-04-21_earningsrelease1q26.htm.jsonl | 0d50d951300ce2cbbde6c33a9c8f647888bd4c1a3c654b0abb8bb16574fa4c01 |
| EX-99.1_2026-07-21_earningsrelease2q26.htm.jsonl | 6450eda3e6d3c5e0b0af4323ee79065c818c4ce5b11bc0f800cb9d5d7e7bc639 |
| EX-99.1_2026-10-20_earningsrelease3q26.htm.jsonl | 79e5f3de157c7238c31f3c91c9d36532abc559b56d3ee90900d572761d0e13ee |

Locators are the extracted page number of the source chunk (page:N), not the printed page.

### Handoffs relied on

| Module | sha256 |
| --- | --- |
| CP-0 | a24d97e6ad4989187dee1bdfc73f1788c04f3ac901ef805ad06227bbfefe017f |
| CP-1 | c8b56ac2c101a114e896b6fe40c1d0fc166fb0aeb10b0a7468d29aa6d079f4d9 |
| CP-1A | 7cc6fb1d431320443212f70fcb053fcdb584d9ad7c9ab9d7e8a5a9f1c75204b3 |
| CP-2 | ffc2237580b33daf84bd6e84b58eb12f725417db1cb31e57eb97122fa7089861 |

Run context sha256 b7d2667de27eee9eaad22a8f2531b97f3d412b9a580fc12af95f3529015a7aad (settings only).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is traceable enough for committee use with restrictions. Figures and quotes trace to filed documents and recompute; covenant, ownership and contract conclusions cannot be traced because the documents are not in the pack. | Medium | Executed indentures, ownership percentages, partner contracts and a financial supplement are missing, so some conclusions rest on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Financial base figures and quoted facts match the filed pages cited. | Funding, liquidity, capital and credit-quality conclusions can be relied on at the stated basis. | High |
| Year-end 2025 capital appears on two bases because of a disclosed recast. | Capital trends must use one basis; the logged difference is explained, not an error. | High |
| An early covenant description was narrower than the annual report and was corrected in later modules. | Covenant content is now stated correctly, but headroom is still not measurable. | Medium |
| Leverage and interest cover use labelled substitutes, as no EBITDA is reported. | Debt service strength rests on proxies and funding structure, not standard multiples. | Medium |

### Evidence trace view

The credit analysis is traceable enough for committee use, with restrictions. Every figure in the financial base and every quoted business fact traces to a filed statement or note in the seven pinned documents, and the derived ratios recompute from those inputs. Traceability is strongest for funding, liquidity, capital and credit-quality figures, which come straight from filed statements. The weakest point is that three conclusions rest on documents the pack does not contain: covenant headroom, ownership and partner contract terms. Two upstream differences are logged and explained, a covenant description and the recast year-end capital ratio. What decides use is whether those documents are added before covenant or distribution capacity is relied on.

### Traceability conclusion

Module status: Ready with Limitations. Traceability scope: Top 5 credit drivers. Committee use: Restricted, because material conclusions on covenants, ownership and partner contracts have no source in the pack. The research quality status is therefore Restricted and the confidence band follows from the register counts below, not from a score stated here.

| Check | Result |
| --- | --- |
| Quotes in the business handoff found on the cited pages | All quoted strings found |
| Table figures in the financial handoff found on or next to the cited pages | All numeric cells found |
| Derived figures recomputed | All recompute to the stated values (see Calculations) |
| Cross-module differences | Two logged: covenant wording, year-end 2025 capital basis |
| Critical findings | None |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_syf-20251231.htm.jsonl | High: filed audited annual report | FY2025 | Synchrony Financial consolidated, plus parent-only note | Statements, notes, funding, covenant wording, parent-only data, business description | Text extraction only; indentures incorporated by reference | CP-1, CP-1A |
| S2 | 10-Q_2026-03-31_syf-20260331.htm.jsonl | High: filed unaudited quarterly report | Q1 2026 | Synchrony Financial consolidated | Statements, liquidity, capital on the earlier basis | Unaudited | CP-1 |
| S3 | 10-Q_2026-06-30_syf-20260630.htm.jsonl | High: filed unaudited quarterly report | Q2 2026 and six months | Synchrony Financial consolidated | Statements, liquidity, capital on the recast basis | Unaudited | CP-1 |
| S4 | 10-Q_2026-09-30_syf-20260930.htm.jsonl | High: filed unaudited quarterly report | Q3 2026 and nine months | Synchrony Financial consolidated | Statements, borrowings, maturities, liquidity, capital, partner events | Unaudited; no interim parent-only data | CP-1, CP-1A |
| S5 | EX-99.1_2026-04-21_earningsrelease1q26.htm.jsonl | Medium: management narrative | Q1 2026 | Synchrony Financial consolidated | Metrics, repurchase programme | Narrative only; tables not included | CP-1A |
| S6 | EX-99.1_2026-07-21_earningsrelease2q26.htm.jsonl | Medium: management narrative | Q2 2026 | Synchrony Financial consolidated | Metrics, credit quality | Narrative only | CP-1 |
| S7 | EX-99.1_2026-10-20_earningsrelease3q26.htm.jsonl | Medium: management narrative | Q3 2026 | Synchrony Financial consolidated | Metrics, management commentary | Narrative only; financial supplement not included | CP-1A |

#### T5B.2 Top credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Partner concentration | CP-1A | Five largest programs were 54% of interest and fees | Loss or repurchase of a program removes receivables and fee income | Monitoring of renewal dates from 2030 | S1 page:13, page:14 | Contract terms not in the pack |
| 2 | Deposit-led funding and liquidity | CP-1 | Deposits of 82,951 and liquid assets of USD 19.5 billion at Q3 2026 | Lowers refinancing risk for debt due within a year | Liquidity does not depend on committed lines | S4 page:39, page:29 | Cash includes cash in transit not counted as liquid |
| 3 | Distributions against earnings and capital | CP-1, CP-1A | Distributions of 3,262 against net earnings of 2,582 in nine months 2026 | Lowers equity cushion beneath creditors | Pace of buybacks versus capital ratio | S4 page:41, page:60 | Intent and capital targets not disclosed |
| 4 | Credit quality and earnings | CP-1 | Net charge-off rate of 4.79% in Q3 2026; net earnings of 892 against 1,077 a year earlier | Drives provision and capital generation | Debt service support | S4 page:14, page:38 | Seasonality; reserve build in the quarter |
| 5 | Holding-company access to bank cash | CP-1, CP-2 | Holding-company notes of 7,511 and reliance on bank dividends | Parent debt service depends on dividends and regulation | Structural subordination of parent creditors in asset access | S4 page:28, page:30, page:57 | No interim parent-only statements |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Five programs produced 54% of interest and fees | CP-1A | Filed statement of the five programs and 54% | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Deposits and borrowings at Q3 2026 | CP-1 | Statement of financial position | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Liquid assets and discount window capacity | CP-1 | Liquidity discussion in the Q3 report | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Distributions of 3,262 exceed net earnings of 2,582 | CP-1A, CP-2 | Cash-flow lines summed | Yes | High | Calculated | Supported | Medium | Committee-Ready |
| Recast year-end capital basis | CP-1 | Two filed capital tables with the recast note | Yes | High | Conflicting | Explained | High | Remediation Needed |
| Covenant content | CP-1, CP-1A | 10-K covenant paragraph; indentures absent | Partial | Medium | Weak Lineage | Partly supported | Medium | Remediation Needed |
| Liquid assets cover debt due within a year 4.3x | CP-2 | Calculated from CP-1 values | Yes | High | Calculated | Supported | Medium | Committee-Ready |
| Retailer share arrangements as a partial hedge | CP-1A | Analyst reading of filed statements and release text | Yes | Medium | Analyst Inference | Interpretation | Medium | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total deposits 82,951 and total borrowings 17,025 at 2026-09-30 | Statement of financial position | 10-Q_2026-09-30_syf-20260930.htm.jsonl | S4 | page:39 | CP-1 financials table | Sourced | High | Opened and matched |
| Liquid assets of 19.5 billion; discount window 13.0 billion | Liquidity discussion | 10-Q_2026-09-30_syf-20260930.htm.jsonl | S4 | page:29 | CP-1 liquidity | Sourced | High | Opened and matched |
| Unsecured notes principal 8,150 and ladder | Funding discussion | 10-Q_2026-09-30_syf-20260930.htm.jsonl | S4 | page:28 | CP-1 maturities | Sourced | High | Series sum to 8,150 |
| Securitized maturities 3,900 and 5,025 | Funding discussion | 10-Q_2026-09-30_syf-20260930.htm.jsonl | S4 | page:26 | CP-1 maturities | Sourced | High | Includes 750 repaid in October 2026 |
| Common equity Tier 1 12.9% and recast 13.5% | Note 10 | 10-Q_2026-09-30_syf-20260930.htm.jsonl | S4 | page:60 | CP-1 financials | Sourced | High | Recast basis |
| Common equity Tier 1 12.6% at 2025-12-31 | Note 11 | 10-K_2025-12-31_syf-20251231.htm.jsonl | S1 | page:188 | CP-1 corrections | Sourced | High | Original basis |
| Covenants on Bank voting stock and 80% control | Funding discussion | 10-K_2025-12-31_syf-20251231.htm.jsonl | S1 | page:57 | CP-1 and CP-1A | Sourced | High | Not repeated in the Q3 report wording |
| Five largest programs 54% | Partner agreements | 10-K_2025-12-31_syf-20251231.htm.jsonl | S1 | page:13 | CP-1A | Sourced | High | Opened and matched |
| Share repurchases 2,878; dividends 314 and 70 | Statement of cash flows | 10-Q_2026-09-30_syf-20260930.htm.jsonl | S4 | page:41 | CP-1A, CP-2 | Sourced | High | Sum of three lines is a calculation |
| Net earnings 892 and 1,077 | Statement of earnings | 10-Q_2026-09-30_syf-20260930.htm.jsonl | S4 | page:38 | CP-1, CP-2 | Sourced | High | Opened and matched |
| Parent-only cash 2,465 and bank dividends 2,700 at FY2025 | Note 16 | 10-K_2025-12-31_syf-20251231.htm.jsonl | S1 | page:194 | CP-1 | Sourced | High | Year-end only |
| Financial table rows cited as "same pages" | Various | Various | S1 to S4 | Page lists in the row | CP-1 financials | Sourced | Medium | Locator granularity coarse but resolvable |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nine-month tie-out of net earnings | CP-1 | 805, 885, 892 | 805 + 885 + 892 = 2,582 | Calculated | Supported | High | Monitoring | S2 page:34, S3 page:37, S4 page:38 |
| LTM net earnings to Q3 2026 | CP-1 | 3,552, 2,801, 2,582 | 3,552 - 2,801 + 2,582 = 3,333 | Calculated | Supported | High | Debt service | S1 page:148, S4 page:38 |
| Borrowings to equity | CP-1, CP-2 | 17,025 and 16,550 | 17,025 / 16,550 = 1.03x | Calculated | Supported | High | Leverage substitute | S4 page:39 |
| Interest cover proxy | CP-1, CP-2 | LTM pre-tax 4,366 and interest expense 3,895 | (4,366 + 3,895) / 3,895 = 2.12x | Calculated | Supported with caveat | Medium | Debt service proxy, not EBITDA | S1 page:148, S4 page:38 |
| Distributions over earnings | CP-1A, CP-2 | 2,878, 314, 70 and 2,582 | 3,262 / 2,582 = 1.26x | Calculated | Supported | High | Capital allocation | S4 page:41, page:38 |
| Holding-company notes carrying value | CP-2 | 8,110 and 599 | 8,110 - 599 = 7,511 (also 2,393 + 4,375 + 743) | Calculated | Supported | High | Structural subordination | S4 page:57 |
| Liquid assets over debt due within a year | CP-2 | 19,500 and 4,500 | 19,500 / 4,500 = 4.3x | Calculated | Supported with rounding | Medium | Liquidity | S4 page:26, page:28, page:29 |
| EBITDA based leverage and cover | CP-1 | No EBITDA reported | Not Calculable from Provided Materials | Not Calculable | Gap recorded | High | Leverage | S1 to S4 |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Covenant content and headroom | Indentures are not supplied, only filing summaries | Weak Lineage | Distribution capacity and acceleration risk depend on the terms | Add executed indentures | CP-1, CP-1A, CP-2 |
| Material | Ownership and control | Percentages and control rights are not supplied | Insufficient Information | Sponsor alignment and control change cannot be traced | Add the proxy statement | CP-1A, CP-2 |
| Material | Partner contract terms | Agreements not in the pack | Insufficient Information | Concentration risk quantification depends on renewal and purchase terms | Add summaries of the top programs | CP-1A, CP-2 |
| Minor | Financial table locators | Several rows cite "same pages" | Weak Lineage | Auditor must resolve the page list | Use page-specific locators | CP-1 |
| Minor | Debt maturity profile | Securitized relative buckets and unsecured calendar years are combined in one chart | Analyst Inference | Buckets are not like for like | Label the basis, as done | CP-1 |
| Minor | Retailer share as a partial hedge | Interpretation of filed text | Analyst Inference | Informs margin resilience | Keep tagged as interpretation | CP-1A |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Citation presence | Strong | Every table figure and quote carries a page locator | Reader can reopen the filed page | Claims can be challenged and verified | Page-specific locators for grouped rows |
| Quote accuracy | Strong | Quoted strings found verbatim on cited pages | Misquote would mislead covenant or concentration reading | Quoted facts are reliable | None |
| Calculation reproducibility | Strong | Each derived figure shows inputs and recomputes | Hidden arithmetic would hide errors | Ratios can be rechecked | None |
| Version and recast control | Adequate | Two capital bases labelled and explained | Mixing bases would misstate capital trend | Capital comparisons are safe if labelled | Keep basis labels |
| Perimeter control | Adequate | Consolidated group, parent-only and bank notes separated | Mixing perimeters misstates structure | Parent claims are shown apart from deposits | Interim parent-only data |
| Upstream consistency | Adequate | Covenant wording corrected downstream | Silent contradiction would hide a defect | Corrections are stated plainly | None |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Executed indentures and covenant certificates | Documents not in the pack | Covenant headroom is a creditor control | Headroom Not Calculable | Caps confidence at Medium | Indentures and compliance certificates |
| G2 | Ownership percentages and control rights | Proxy statement | Alignment and control change | Ownership rows are gaps | Reduces governance confidence | Proxy statement |
| G3 | Partner program agreements | Agreements or summaries | Concentration quantification | Contract risk unsized | Reduces business risk confidence | Partner program summaries |
| G4 | Financial supplement and non-GAAP reconciliation | Supplement referenced by the releases | Tangible metrics rest on management | Tangible metrics excluded | Minor reduction | Financial supplements |
| G5 | Interim parent-only statements | Not printed in quarterly reports | Parent liquidity is stale at year-end 2025 | Parent debt service not measured | Caps liquidity confidence | Parent-only schedules |
| G6 | EBITDA and cash interest | Not reported | Standard leverage and cover unavailable | Substitutes used | Caps leverage confidence | None available |

#### T5.1 Module and handoff register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | syf-2026-11-05-credit_snapshot-host, sha256 a24d97e6ad4989187dee1bdfc73f1788c04f3ac901ef805ad06227bbfefe017f | Source readiness | High | Six headings present | Accepted | Covenant wording corrected downstream |
| CP-1 | syf-2026-11-05-credit_snapshot-host, sha256 c8b56ac2c101a114e896b6fe40c1d0fc166fb0aeb10b0a7468d29aa6d079f4d9 | Financial base | High | Six headings present | Accepted | Corrects CP-0 covenant wording |
| CP-1A | syf-2026-11-05-credit_snapshot-host, sha256 7cc6fb1d431320443212f70fcb053fcdb584d9ad7c9ab9d7e8a5a9f1c75204b3 | Business and transaction | High | Six headings present | Accepted | No transaction beyond a portfolio purchase |
| CP-2 | syf-2026-11-05-credit_snapshot-host, sha256 ffc2237580b33daf84bd6e84b58eb12f725417db1cb31e57eb97122fa7089861 | Credit synthesis | Medium | Six headings present | Accepted | Confidence capped below High |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Financial table rows with grouped locators | Supported | Page lists are coarse | Page-specific locators | None |
| Minor | CP-1A | Company profile employees | Not supplied | Employee count not located | None possible | None |
| Minor | CP-2 | Figures carried from upstream | Supported | No source text read by design | None | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Interest cover proxy is not EBITDA cover | Uses accrued interest and includes deposit interest | None | Keep the label | None |
| Minor | CP-1A | Active accounts of 68.0 million at period end in the filing versus an average of 68.3 million in the release | Period-end total and average are different measures | Definitions differ, not a conflict | Label the measure | None |
| Minor | CP-2 | Liquid assets over debt due within a year | Rounded liquid assets in billions against principal in millions | None | Note rounding | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Covenants restrict liens on and loss of control of the Bank | Executed indentures | Filing summary only | Add indentures | Counsel review of covenant text |
| Material | CP-1, CP-2 | Holding-company creditors rank behind deposits and trust notes in asset access | Legal structure documents | Not a printed waterfall | Treat as structural interpretation | Counsel review |
| Minor | CP-1A | Partner purchase rights on termination | Program agreements | Summary only | Add summaries | None |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | No relative value or pricing claim is made | Market quotes and spreads | Context supplies none | None needed | No pricing view is supported |
| Minor | CP-1A | Ratings are issuer-reported | Agency reports | Not in the pack | Add if needed | Ratings are attributed statements |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-0, CP-1 | CP-0 described covenant terms as general only, while the annual report states the covenant types | CP-1 corrected it; CP-0 cannot be edited | State the correction, as CP-1 and CP-1A did | Later modules use the corrected description |
| Material | CP-1, CP-1A, CP-2 | Year-end 2025 common equity Tier 1 of 12.6% (annual report) against 13.5% (Q3 report) | Disclosed recast for software presentation | Label the basis everywhere | Use the recast basis for comparison |
| Minor | CP-1, CP-1A | Lowe's portfolio expected at about 0.8 billion and completed at 0.7 billion | Expectation versus completed filing | Use the completed figure | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A, CP-2 | Duplication | Distribution and capital figures recur across modules | Keep one source figure | None |
| Material | CP-2 | Committee readiness | Confidence is capped by missing covenant, ownership and contract documents | Add documents | Use restricted |

#### T5.8 Structured export, master index and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Chart data tables | Maturity rows mix two bases; labelled | Keep labels | Chart consumers must read the basis column |
| Minor | CP-1 | Leverage and cover tables | Values are Not supplied by design | None | Charts show gaps, not zero |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I1 | Material | CP-0, CP-1 | Version | Covenant description narrower in CP-0 than the annual report | State correction | Restricted use | Resolved in later modules |
| I2 | Material | CP-1, CP-1A, CP-2 | Definition | Year-end 2025 capital on two bases | Label basis | Restricted use | Explained |
| I3 | Material | CP-1, CP-1A, CP-2 | Evidence gap | Indentures, ownership and contract terms absent | Add documents | Restricted use | Open |
| I4 | Minor | CP-1 | Locator | Grouped page locators | Page-specific locators | None | Open |
| I5 | Minor | CP-1 | Definition | EBITDA substitutes | Keep labels | None | Explained |

## Calculations

Recomputed from the cited figures by this review; all agree with the upstream values.

| Item | Inputs | Result |
| --- | --- | --- |
| Nine-month net earnings | 805 + 885 + 892 | 2,582 |
| LTM net earnings | 3,552 - 2,801 + 2,582 | 3,333 |
| Borrowings to equity, Q3 2026 and FY2025 | 17,025 / 16,550; 15,182 / 16,766 | 1.03x; 0.91x |
| Interest cover proxy | (4,366 + 3,895) / 3,895 | 2.12x |
| Distributions | 2,878 + 314 + 70 | 3,262 |
| Distributions over earnings | 3,262 / 2,582 | 1.26x |
| Holding-company notes | 8,110 - 599 | 7,511 |
| Unsecured share of borrowings | 8,110 / 17,025; 6,767 / 15,182 | 47.6%; 44.6% |
| Securitization collateral | 21,898 / 8,915 | 2.46x |
| Liquid assets over debt due within a year | 19,500 / 4,500 | 4.3x |

## Gaps

Committee use is Restricted. The open gaps are the executed indentures and covenant certificates, ownership percentages and control rights, partner program agreements, interim parent-only statements, the financial supplement with its non-GAAP reconciliation, and EBITDA with cash interest. Each is listed with its follow-up source in the gaps ledger above. The review did not inspect charts or images, and the pack has no source dated 2026-10-23 to 2026-11-05.

## Next module

No further module is selected. The published report draws on these four handoffs; the open gaps above are the evidence to add before covenant or distribution capacity is relied on.
