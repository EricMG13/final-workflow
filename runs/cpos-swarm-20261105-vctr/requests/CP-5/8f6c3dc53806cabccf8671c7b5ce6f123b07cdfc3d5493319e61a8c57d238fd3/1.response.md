## Request

Evidence trace validation and research-integrity grade (CP-5, with the absorbed CP-5A phase) for Victory Capital Holdings, Inc. (VCTR), as of 2026-11-05, pathway credit_snapshot, reporting currency USD. Scope: the four upstream handoffs (readiness, financial base, business and transaction context, credit synthesis) checked against the seven pinned filed sources. This module changes no upstream conclusion and repairs no lineage silently.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_vctr-20251231.htm.jsonl | f6e853fafdad024596ae018622fdc2c105ae3123da9ff8c0ffc4cc35ba62a4c6 |
| 10-Q_2026-03-31_vctr-20260331.htm.jsonl | 51ecb3082ef4b8f61e744997e8179f3f8048703f134354cd3a9232ffa5550840 |
| 10-Q_2026-06-30_vctr-20260630.htm.jsonl | dced821a8cf47e367f9af63545645defedd6eb1c20287807f650044bdd40db14 |
| 10-Q_2026-09-30_vctr-20260930.htm.jsonl | f5b50500d26e0dc2485801a8df14aa064707215b873d8b5442ac072a0ef88f50 |
| EX-99.1_2026-05-06_vctr-ex99_1.htm.jsonl | ce379672b7f1d4e69ae12e2fdf1e719857d5076de9696a4055a1b0edae6c5455 |
| EX-99.1_2026-08-05_vctr-ex99_1.htm.jsonl | 981c5f312fef484f40e89934d8e4fda4e7cdfbbdce01c09bbd4ee44b7bfd4c62 |
| EX-99.1_2026-11-04_vctr-ex99_1.htm.jsonl | e1350c6fc75fc57c66528cfff71a5ac81718d36de8c659965d370dbd5d1f67b9 |

Context file (settings, not issuer evidence): sha256 9e96aec1be60fc30bd3853ebe28d82af5bc222a4621f74e4d59778dfc86b3113.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 4e7499ed1421d528acf730a77740ef202066489175c40b1ee55d70d91d8e7f75 | Source gate and inherited limitations |
| CP-1 | d301b10470f387a928e4cc51b12e6dd730b54fd41535e9908f3af5c8aa30f352 | Financial figures, calculations, chart data |
| CP-1A | 27f13f13115fcc9606ca931244a5af162b097c7965e7cf4095894ffef527698c | Business, ownership, governance, transaction facts |
| CP-2 | cb85c5a97c12040540a1d9d309c2248a03f0ea2df761fb3439f27b56914dece8 | Credit synthesis, strengths, weaknesses, risks |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The standalone credit view traces to the filings and its calculations reproduce. The view after the First Eagle acquisition has no source support and is withheld. Overall confidence is Low because key documents are absent. | Low | The merger agreement, financing commitment, proxy statement and credit agreement are not in the sources. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every locator in the financial and business handoffs points to a real page, and the figures and quotes checked match the pages cited. | Reported debt, cash, liquidity and adjusted EBITDA can be relied on as sourced. | High |
| Every calculation was recomputed from its printed inputs and agreed, including the last-twelve-months bridges, ratios and the debt maturity schedule. | Leverage of 1.14x gross and 0.90x net, and cover of 14.83x, are reproducible. | High |
| The debt maturity schedule is calculated from a 1% annual amortization and quarterly payments, not printed. | Annual maturities are estimates; the main maturity date of September 23, 2032 is sourced. | Medium |
| Two statements in the business handoff do not fully agree: the largest franchise share and the location of clients. | Concentration and foreign exposure statements should carry the stated caveats. | Medium |
| Post-acquisition leverage, covenant headroom and ranking have no sourced inputs. | These conclusions are withheld and need the missing documents before committee use. | High |

### Evidence trace view

The evidence trace holds for the standalone credit view and fails for the post-acquisition view, because the documents that would support the latter are not in the sources. Every figure in the financial, business and synthesis handoffs resolves to a located page of the seven filed sources, and each calculation was recomputed from its printed inputs with the same result. The strongest support is that debt, cash, liquidity and adjusted EBITDA come directly from the statements and the company's own reconciliation. The weakest point is that the First Eagle financing, the covenant ratio and the credit agreement terms have no source, so conclusions on them are withheld rather than inferred. What decides committee use is whether the merger agreement, commitment letter and proxy statement are added to the sources.

Scoring (script output, not hand-derived): Confidence Score 53, band Low, QA status Passed, from 15 material claims (8 Directly Sourced, 5 Calculated, 2 Analyst Inference), required sections 6 of 6, source gate partial, and 4 MINOR findings. Committee status: Restricted. The standalone credit view may be used with the stated limits; any post-acquisition statement may not.

### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_vctr-20251231.htm.jsonl | Primary, audited, filed | FY2025 with FY2024 and FY2023 comparatives | Victory Capital Holdings, Inc. consolidated | Statements, debt note, adjusted EBITDA reconciliation, business description, leases | Chart values in the business section are not in the text; auditor changed in 2025 | CP-1, CP-1A |
| S2 | 10-Q_2026-03-31_vctr-20260331.htm.jsonl | Primary, unaudited, filed | Q1 2026 | Same | Term loan principal, cash, adjusted EBITDA, cash interest | MD&A text has a unit error ("$985.0 billion") | CP-1 |
| S3 | 10-Q_2026-06-30_vctr-20260630.htm.jsonl | Primary, unaudited, filed | Q2 2026 and six months | Same | Same plus Seventh Amendment | None beyond unaudited status | CP-1, CP-1A |
| S4 | 10-Q_2026-09-30_vctr-20260930.htm.jsonl | Primary, unaudited, filed on the cutoff date | Q3 2026 and nine months | Same | Statements, debt note, liquidity, First Eagle note, legal proceedings | MD&A debt paragraph still uses prior-amendment wording | CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-05-06_vctr-ex99_1.htm.jsonl | Management release, furnished | Q1 2026 | Same | Flows, adjusted measures | Management claims; filings control | CP-1A |
| S6 | EX-99.1_2026-08-05_vctr-ex99_1.htm.jsonl | Management release, furnished | Q2 2026 | Same | Flows, adjusted measures | Pre-dates First Eagle agreement | CP-1A |
| S7 | EX-99.1_2026-11-04_vctr-ex99_1.htm.jsonl | Management release, furnished | Q3 2026 | Same | AUM, flows, fee realization, benchmark statistic | Management claims; filings control | CP-1A, CP-2 |

### Top credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Pending First Eagle acquisition and its financing | CP-1A | Q3 note describes consideration, commitment letter and expected closing; no amounts | Largest forward change to leverage and ranking | Withholds any post-deal view | S4 page:12, page:13, page:48 | Merger agreement, commitment letter and proxy statement absent |
| 2 | Standalone leverage and interest cover | CP-1 | Term loan principal 975,150 thousand; LTM adjusted EBITDA 856,348 thousand; cash interest 57,742 thousand | Core debt service capacity | Supports the standalone view | S4 page:20, page:42, page:8; S1 page:97, page:110 | Adjusted EBITDA is a management measure; covenant EBITDA absent |
| 3 | Liquidity | CP-1 | Cash 207,724 thousand and undrawn revolver 100,000 thousand at September 30, 2026 | Covers near-term calls | Supports the standalone view | S4 page:4, page:43, page:44 | Cash includes regulated subsidiaries |
| 4 | Fee-on-assets revenue with short-notice contracts | CP-1A | Funds may end advisory agreements on not more than 60 days' notice | Revenue visibility | Main business risk | S1 page:26, page:16 | No client concentration data beyond channel mix |
| 5 | Amundi ownership, board rights and distribution | CP-1A | 26.1% of fully diluted shares; two board designees; exclusive offshore distribution | Counterparty concentration | Governance and distribution risk | S4 page:11; S1 page:135, page:14 | Preferred stock terms and other holders absent |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Term loan 975,150 thousand at September 30, 2026 | CP-1 | S4 page:20 table | Yes | Primary | Directly Sourced | Verified against page | High | Fully traced |
| LTM adjusted EBITDA 856,348 thousand | CP-1 | S1 page:97; S4 page:42 | Yes | Primary, company reconciliation | Calculated | Recomputed and agrees | Medium | Fully traced; management measure |
| Gross leverage 1.14x, net 0.90x | CP-1 | Derived from the two rows above and cash 207,724 thousand | Yes | Primary inputs | Calculated | Recomputed and agrees | Medium | Fully traced |
| Cash interest cover 14.83x | CP-1 | S1 page:110; S4 page:8 | Yes | Primary | Calculated | Recomputed and agrees | Medium | Fully traced; Q3 2025 base anomaly flagged |
| Liquidity 307.724 US$ million | CP-1 | S4 page:4, page:43 | Yes | Primary | Calculated | Recomputed and agrees | High | Fully traced |
| Maturity schedule by year | CP-1 | S1 page:143 amortization wording; S4 page:20 | Yes | Primary wording, calculated amounts | Calculated | Recomputed; assumption stated | Medium | Traced; schedule not printed |
| Advisory contracts terminable on 60 days' notice | CP-1A | S1 page:26 | Yes | Primary | Directly Sourced | Quote matches | High | Fully traced |
| Two-thirds variable cost | CP-1A, CP-2 | S1 page:16 | Yes | Primary, management statement | Directly Sourced | Quote matches; Management Language | Medium | Traced; not verified by financials |
| Amundi 26.1%, two nominees, 15-year distribution agreement | CP-1A | S4 page:11; S1 page:135, page:14 | Yes | Primary | Directly Sourced | Quotes match | High | Fully traced |
| First Eagle description | CP-1A, CP-2 | S4 page:12, page:13 | Yes | Primary | Directly Sourced | Quotes match | High | Fully traced; amounts absent |
| Credit view and thesis | CP-2 | CP-1 and CP-1A rows | Yes | Upstream handoffs | Analyst Inference | Reasoned from traced rows | Medium | Traced to upstream rows |
| Shareholder distributions as main call on cash | CP-2 | S4 page:8 | Yes | Primary, calculated share | Analyst Inference | Share recomputed; interpretation is judgment | Medium | Traced; legal capacity absent |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Term loan principal, rate 5.82%, effective 5.98% | Note 10 debt table | 10-Q_2026-09-30_vctr-20260930.htm.jsonl | S4 | page:20 | CP-1 capital structure | Table | Primary | Checked on page |
| Revolver 100.0 million dollars, undrawn, matures September 23, 2030 | MD&A liquidity | 10-Q_2026-09-30_vctr-20260930.htm.jsonl | S4 | page:44 | CP-1 capital structure | Narrative | Primary | Checked on page |
| Springing first lien leverage covenant 4.00 to 1.00, 35.0% draw trigger | Note 10 | 10-Q_2026-09-30_vctr-20260930.htm.jsonl | S4 | page:20 | CP-1 covenants | Narrative | Primary | Ratio itself absent |
| Adjusted EBITDA reconciliation FY2025 682,851 thousand | Non-GAAP reconciliation | 10-K_2025-12-31_vctr-20251231.htm.jsonl | S1 | page:97 | CP-1 financials | Table | Primary, company | Checked on page |
| Cash paid for interest FY2025 79,672 thousand | Supplemental cash flow | 10-K_2025-12-31_vctr-20251231.htm.jsonl | S1 | page:110 | CP-1 financials | Table | Primary | Checked on page |
| Q1 and Q2 adjusted EBITDA and cash interest for LTM bridges | Reconciliations and cash flows | 10-Q_2026-03-31 and 10-Q_2026-06-30 files | S2, S3 | S2 page:30, page:6; S3 page:39, page:7 | CP-1 calculations | Tables | Primary | Checked on page |
| Operating leases 42,405 and 45,610 thousand | Balance sheet; Note 17 | S4; S1 | S4, S1 | S4 page:5; S1 page:149 | CP-1 claims outside debt | Table | Primary | Checked on page |
| WestEnd contingent consideration 53,760 thousand, maximum 80.0 million dollars | MD&A | 10-Q_2026-09-30_vctr-20260930.htm.jsonl | S4 | page:45 | CP-1 claims outside debt | Narrative | Primary | Checked on page |
| Auditor change: Deloitte since 2025, Ernst & Young 2013 to 2025 | Audit reports | 10-K_2025-12-31_vctr-20251231.htm.jsonl | S1 | page:153, page:156 | CP-1A profile | Narrative | Primary | Checked on page |
| First Eagle merger description | Note 3 | 10-Q_2026-09-30_vctr-20260930.htm.jsonl | S4 | page:12, page:13 | CP-1A transaction | Narrative | Primary | Quotes checked; the quote straddles two pages and is cited separately |
| Stockholder litigation, two complaints, ten demand letters | Part II Item 1 | 10-Q_2026-09-30_vctr-20260930.htm.jsonl | S4 | page:47, page:48 | CP-1A transaction | Narrative | Primary | Checked on page |
| Fee realization 44.8 bp, flows | Release table | EX-99.1_2026-11-04_vctr-ex99_1.htm.jsonl | S7 | page:2, page:3 | CP-1A operating model | Table | Management release | Management Language where characterised |

### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM adjusted EBITDA, Q1, Q2, Q3 2026 | CP-1, CP-2 | FY2025 plus year-to-date 2026 less year-to-date 2025 | 770,472; 834,664; 856,348 thousand | Recomputed, agrees | Calculated | Medium | Leverage and cover denominator | S1 page:97; S2 page:30; S3 page:39; S4 page:42 |
| LTM cash interest | CP-1, CP-2 | Same bridge | 76,377; 74,071; 57,742 thousand | Recomputed, agrees | Calculated | Medium | Cover denominator | S1 page:110; S2 page:6; S3 page:7; S4 page:8 |
| Gross and net leverage by period | CP-1, CP-2 | Principal and cash by balance-sheet date over LTM adjusted EBITDA | 1.44x/1.20x, 1.27x/1.17x, 1.17x/1.09x, 1.14x/0.90x | Recomputed, agrees | Calculated | Medium | Leverage trend | S1 page:106, page:142; S2 page:16; S3 page:18; S4 page:20 |
| Interest cover | CP-1, CP-2 | Adjusted EBITDA over cash interest | 8.57x, 10.09x, 11.27x, 14.83x | Recomputed, agrees | Calculated | Medium | Debt service | As above |
| EBITDA proxy | CP-1, CP-2 | Operating income plus depreciation and amortization | 727,102 thousand LTM; leverage 1.34x gross, 1.06x net | Recomputed, agrees | Calculated | Medium | Definition sensitivity | S1 page:107; S4 page:5 |
| Debt maturity schedule | CP-1, CP-2 | 1% a year of 985.0 million dollars paid quarterly; maturity September 23, 2032; assumes quarter-end payments and no prepayment | 2.4625 million per quarter; bullet 918.5125 million | Recomputed, agrees; the four installments to date reconcile to the principal paid down | Calculated, Assumption-Based for timing | Medium | Refinancing profile | S1 page:143; S4 page:20, page:21 |
| Shareholder and contingent uses | CP-1, CP-2 | Dividends, repurchases, net share settlement taxes, WestEnd payments | 443,212 thousand against 479,740 thousand operating cash flow, 92.4% | Recomputed, agrees | Calculated | Medium | Cash allocation | S4 page:8 |
| Adjusted EBITDA excess over proxy | CP-2 | 856,348 less 727,102 | 129,246 thousand, 15.1% | Recomputed, agrees | Calculated | Medium | Earnings quality | CP-1 rows |

### Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | Maturity amounts by year | Not printed in any source; calculated with stated timing assumption | Assumption-Based | Annual maturity amounts are estimates | Confirm against the credit agreement | CP-1 maturity chart; CP-2 strengths |
| MINOR | Largest franchise at about 42% of AUM | Two printed figures give 42.2% against a printed ceiling of 42% | Conflicting | Concentration statement | Carry the printed 42% with the 42.2% note | CP-1A operating model; CP-2 |
| MINOR | Revenue from U.S. clients versus 17% of AUM from clients outside the U.S. | Two filing statements on client location do not reconcile | Conflicting | Foreign exposure statements | State both and do not size non-U.S. revenue | CP-1A conflicts log |
| MINOR | Two-thirds variable cost | Management statement only, not tested against expense detail | Weak Lineage | Margin resilience claim | Keep as Management Language | CP-1A; CP-2 |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Locator integrity | Strong: all page references fall inside each source's page count and the quotes and figures checked match | 86 locators in the financial handoff and 77 in the business handoff were range-checked; every quoted string and every table figure was matched to its cited page, and narrative figures were matched for the items in the lineage register | A wrong page would break committee verification | Sourced figures can be relied on | None |
| Calculation reproducibility | Strong | Every bridge and ratio recomputed from printed inputs | A silent error would mis-state leverage | Leverage and cover are reproducible | None |
| Cross-module consistency | Strong: all figures in the synthesis resolve to the financial and business handoffs | Figure identity check across the three handoffs | A mismatch would mislead the committee | No contradiction found | None |
| Definition control | Moderate | Adjusted EBITDA is the company's measure; proxy shown beside it | Add-backs can flatter leverage | Leverage is shown on two bases | Obtain covenant EBITDA definition |
| Subsequent events | Strong | Items after September 30, 2026 are labelled and nothing is dated after 2026-11-05 | Blending would distort the period | Dividend, proxy and litigation kept separate | None |
| Management language | Strong | Release characterisations such as record flows are tagged Management Language | Adopting them would bias the view | Facts and claims are separate | None |

### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | First Eagle terms and financing | Merger agreement (Exhibit 2.1 of the Q3 report), commitment letter, definitive proxy statement | Post-deal leverage, liquidity and ranking | Post-acquisition conclusions withheld | Source gate partial; confidence band Low | Those three documents |
| G2 | First Eagle financials | Target statements and flows | Whether acquired earnings support new debt | Same | Same | Proxy statement |
| G3 | Credit agreement and covenant | Agreement, amendments, compliance ratio, covenant EBITDA | Headroom, guarantors, restricted payments | Covenant headroom not calculable | Lowers confidence on creditor control | Credit agreement and compliance reporting |
| G4 | Amundi preferred and holders | Certificate of designations, holder register | Claims ahead of common equity; control | Ownership view limited | Lowers confidence on governance | Exhibit 3.5 of the 10-K index; proxy |
| G5 | Ratings and quotes | Any rating or price | External view | None used | Cannot cross-check | Rating agencies, market data |
| G6 | Business charts | Asset class, vehicle, franchise and geography mixes are graphics | Product concentration | Not quantified | Minor | Filing graphics |

## Calculations

Recomputations performed in this module, from the cited printed inputs (US$ thousands):

| Item | Inputs | Result | Agrees with upstream |
| --- | --- | --- | --- |
| LTM adjusted EBITDA, Q3 2026 | 682,851 + 658,872 - 485,375 | 856,348 | Yes |
| LTM cash interest, Q3 2026 | 79,672 + 41,456 - 63,386 | 57,742 | Yes |
| Gross leverage, Q3 2026 | 975,150 / 856,348 | 1.1387, shown as 1.14x | Yes |
| Net leverage, Q3 2026 | (975,150 - 207,724) / 856,348 = 767,426 / 856,348 | 0.8962, shown as 0.90x | Yes |
| Cover, Q3 2026 | 856,348 / 57,742 | 14.8306, shown as 14.83x | Yes |
| Debt principal paid down since the repricing | 985,000 - 975,150 = 9,850, equal to four installments of 2,462.5 | 9,850 | Yes |
| Liquidity, Q3 2026 | 207,724 + 100,000 | 307,724 | Yes |
| Pioneer share of AUM | 132.3 / 313.8 | 0.4216 | Yes, and shows the 42% note |
| Confidence score | Script inputs given above | 53, Low, Passed | Script-owned |

## Gaps

### Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-1 | MINOR | CP-1A | Cross-source figure | Largest franchise share computes to 42.2% against a printed ceiling of 42%; logged and not reconciled | Carry both | Concentration statement carries a note | Open |
| I-2 | MINOR | CP-1A | Cross-source statement | Revenue historically from U.S. clients versus 17% of AUM from clients outside the U.S. | Carry both; do not size non-U.S. revenue | Foreign exposure statement carries a note | Open |
| I-3 | MINOR | CP-1, CP-2 | Calculated, not printed | Maturity amounts by year depend on a quarter-end payment assumption; quarterly cash flow lines are empty in the Q3 columns of the financial table | Confirm with the credit agreement; use discrete quarters if needed | Estimates, not facts | Open |
| I-4 | MINOR | CP-2 | Duplication | The synthesis repeats the adjusted EBITDA caveat and the First Eagle gap in several sections | Say each limitation once | No effect on figures | Open |
| G-1 | Gap | CP-1A, CP-2 | Source absent | First Eagle documents and credit agreement not supplied | Add documents | Post-acquisition view barred | Open |

### Handoff status and structure

| Module | Handoff canonical file or run | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | Run vctr-2026-11-05-credit_snapshot-host, accepted | Seven sources, four consumers | Primary and management releases | Six headings, readiness view present | Passed | Source gate partial because key First Eagle and credit documents are absent |
| CP-1 | Same run, accepted | Statements, debt, liquidity, charts | Primary | Six headings, chart selectors once each | Passed | Figures and locators verified |
| CP-1A | Same run, accepted | Business, ownership, transaction | Primary and management | Six headings, selectors once each | Passed | Conflicts logged, not reconciled |
| CP-2 | Same run, accepted | Credit synthesis | Upstream handoffs | Six headings, selectors once each | Passed | Confidence capped below High |

### Other audit registers

| Register | Result |
| --- | --- |
| Legal and structural claims | The first lien description, the springing covenant and the amendment history rest on filing summaries; the credit agreement and amendments are not supplied, so legal terms are not independently confirmed (Legal review dependency: credit agreement) |
| Relative value and market claims | None are made in the upstream handoffs, which is correct since no quotes or ratings exist; missing datapoints are prices, ratings and peers |
| Cross-module consistency and version control | No numeric contradiction between CP-0, CP-1, CP-1A and CP-2; the Q1 report unit error and the Q3 report's prior-amendment wording were handled consistently |
| Duplication and materiality | Issue I-4 only; no material claim is missing from the synthesis |
| Remediation priority | First, add the First Eagle documents; second, the credit agreement and compliance data; third, ratings and holder data |

## Next module

The run proceeds to delivery with committee use restricted to the standalone credit view. Re-run this validation after the First Eagle merger agreement, commitment letter, proxy statement and the credit agreement are added to the sources.
