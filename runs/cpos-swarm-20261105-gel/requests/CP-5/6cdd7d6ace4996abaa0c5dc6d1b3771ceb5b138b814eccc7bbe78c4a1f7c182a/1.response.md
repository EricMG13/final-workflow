## Request

Issuer: GENESIS ENERGY LP (Genesis Energy, L.P., ticker GEL). As-of date 2026-11-05; pathway credit_snapshot; currency USD. Scope: trace the evidence behind the accepted CP-0, CP-1, CP-1A and CP-2 handoffs to the pinned sources and grade whether committee use is permitted, restricted or blocked.

## Sources

### Issuer sources traced

| Source file (exact name) | sha256 | Document family and period |
| --- | --- | --- |
| 10-K_2025-12-31_gel-20251231.htm.jsonl | ccb89bebbe1f6460b65cf41694753b9c46d6084fa3c93974775412b94a4649f8 | Form 10-K, FY2025 (audited) |
| 10-Q_2026-03-31_gel-20260331.htm.jsonl | 25844b5fb23f8fb7e6ed5e3ecd46a1d84117c9d80e65e2ca8d092544b9bdbfa5 | Form 10-Q, Q1 2026 |
| 10-Q_2026-06-30_gel-20260630.htm.jsonl | abd4ada77d59922e6f0bafe2fa139c2cc408c45768d2e839399c3eb81593724d | Form 10-Q, Q2 2026 |
| 10-Q_2026-09-30_gel-20260930.htm.jsonl | b8ecb63006d005d24876220dffec5b55d573a9ed4071631f5d65780aeca8bd64 | Form 10-Q, Q3 2026 |
| EX-99.1_2026-05-07_a90ex9918kearnings_q12026.htm.jsonl | dacbb1e9e5b2b770bd5cf7b317240e0ada11d6948f3a4f941eec0c98544a6e5d | Earnings release, May 7, 2026 |
| EX-99.1_2026-08-06_a90ex9918kearnings_q22026.htm.jsonl | e543ee3e3398ce04f2a72be94919a9105edf4587f39625f574d75860af788168 | Earnings release, August 6, 2026 |
| EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | c64ffa295db0861a2124c70f86ea927a2ba296a55d07643ed60b307a769d0d5c | Earnings release, November 5, 2026 |

Run settings (not issuer evidence): context file /workspace/secdata/data/2026-11-05/contexts/1022321-genesis-energy-lp-gel.json, sha256 df9790453496c7c6915bcace0e2562d4cd49506ea6a01ef11c0fdc0b1c2fef47.

### Supplied handoffs

| Module | sha256 | Run and use |
| --- | --- | --- |
| CP-0 | 4b65b01575675a608bc6fc6997ea8b40b64b585c6caafd62892d7c3a4a40acae | Run gel-2026-11-05-credit_snapshot-host; source readiness, re-anchored below |
| CP-1 | d462428272340cea7077b0e2cc754aeebca5b246e4bdf0b36a518466a8dd78f4 | Same run; financial base, every figure re-traced |
| CP-1A | 48e419f82e8a5058691338a6ba98e693561b90e965ff21533e48a0e1d9ca1c11 | Same run; business and transaction facts, re-traced |
| CP-2 | cbd45124daa9a5fc6b1ffc7a3da6c1b411a52a253009372e85aae8b6b34e2f3e | Same run; credit synthesis, re-traced |

Upstream re-anchor: all four handoffs name Genesis Energy LP, the as-of date 2026-11-05 and the same run; no module, run, entity or period mismatch was found. The datapoints used here are restated in the registers below.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The credit analysis traces to filed pages or to calculations that reproduce from source text, but covenant headroom and legal capacity cannot be cleared; committee use is permitted with restrictions. | Medium | The executed credit agreement and note indentures are not in the source set. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of 27 material statements traced, 14 are directly sourced and 9 are calculated, and every calculated statement reproduces from the source figures. | Liquidity, leverage, cover and maturity figures can be relied on with their basis labels. | High |
| Covenant leverage of 5.03X rests on management inputs, and a USD 10.5 million inventory item and a cash figure differ between filing and release. | The 12.5% headroom cannot be confirmed and should be read as management-reported. | Medium |
| Leverage is 5.18x on debt principal and 5.11x on balance sheet carrying value. | Basis choice moves leverage by 0.07x; both bases should be labelled. | High |

### Evidence trace view

The analysis is traceable enough for a restricted committee snapshot: every figure in the credit view resolves to a filed page or to a calculation recomputed from source text and matched, but covenant headroom and legal capacity cannot be cleared because the executed credit agreement and note indentures are not in the source set. Of 27 material statements traced, 14 are directly sourced, 9 are calculated, 2 are logged conflicts and 2 are insufficient information; none is untraced. The most important provenance gap is the covenant ratio of 5.03X against a 5.75x maximum, which rests on management's release and on an inventory deduction the filing labels differently. Remediation is to add the Eighth credit agreement and the indentures. Nothing here changes the underlying credit conclusion.

### Clearance decision

Committee status: Restricted. One Critical issue is open (covenant headroom and legal capacity without executed documents), four Material issues are open or logged, and the remaining issues are Minor. Committee use is permitted for the credit snapshot, with covenant headroom and legal-capacity statements excluded from reliance until the documents are added. The numeric confidence score and band are not computed in this transport; under the CP-5 rule a Restricted status caps the band at Low, and no upstream conclusion is changed.

### Traceability summary

| Classification | Count of statements |
| --- | --- |
| Directly Sourced | 14 |
| Calculated | 9 |
| Conflicting | 2 |
| Insufficient Information | 2 |
| Assumption-Based, Analyst Inference, Weak Lineage, Untraced | 0 |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-01 | 10-K_2025-12-31_gel-20251231.htm.jsonl | High (filed, audited) | FY2025, FY2024, FY2023; instants Dec 31, 2025 and 2024 | Genesis Energy, L.P. and subsidiaries, consolidated | Audited statements, debt note, segments, ownership, risk factors | Describes the superseded Seventh credit agreement; organization chart is an image | Opening balances, FY2025 base, ownership, business description |
| SRC-02 | 10-Q_2026-03-31_gel-20260331.htm.jsonl | High (filed, unaudited) | Quarter to March 31, 2026 | Same consolidated perimeter | Statements, debt note, Eighth credit agreement terms, Q1 comparatives | Condensed notes; exhibit 10.1 not supplied | Q1 2026 LTM and liquidity points |
| SRC-03 | 10-Q_2026-06-30_gel-20260630.htm.jsonl | High (filed, unaudited) | Quarter and six months to June 30, 2026 | Same consolidated perimeter | Statements, debt note, AR Facility | Condensed notes; exhibit 22.1 not supplied | Q2 2026 LTM and liquidity points |
| SRC-04 | 10-Q_2026-09-30_gel-20260930.htm.jsonl | High (filed, unaudited) | Quarter and nine months to September 30, 2026 | Same consolidated perimeter | Statements, debt note, segments, MD&A, guarantor information | Condensed notes; no subsequent-events note | Latest balance sheet, debt register, covenant levels, transactions |
| SRC-05 | EX-99.1_2026-05-07_a90ex9918kearnings_q12026.htm.jsonl | Medium (management release) | Quarter to March 31, 2026 and trailing twelve months | Same perimeter | Adjusted EBITDA, adjusted debt ratio 5.38X | Management definitions | Q1 covenant cushion |
| SRC-06 | EX-99.1_2026-08-06_a90ex9918kearnings_q22026.htm.jsonl | Medium (management release) | Quarter and six months to June 30, 2026 | Same perimeter | Adjusted EBITDA, adjusted debt ratio 5.00X | Management definitions | Q2 covenant cushion |
| SRC-07 | EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | Medium (management release) | Quarter and nine months to September 30, 2026 | Same perimeter | Adjusted EBITDA, adjusted debt ratio 5.03X, outlook language | Management definitions; outlook is management language | Q3 covenant inputs, guidance language, hurricane event |
| SRC-08 | context file 1022321-genesis-energy-lp-gel.json | Run setting, not issuer evidence | as-of 2026-11-05 | Genesis Energy LP (gel) | Dates, currency, sector label; ratings, peers, market data blank | Blank fields are not zero | Scope and period labels |
| HND-00 | CP-0 handoff | Upstream analytical handoff | as-of 2026-11-05 | Genesis Energy LP | Source readiness and coverage | Not a source of issuer facts | Gap propagation |
| HND-01 | CP-1 handoff | Upstream analytical handoff | FY2025 to Q3 2026 | Genesis Energy LP | Statements, debt register, metrics, covenant review | Management ratio basis differs from computed basis | CP-2 figures |
| HND-1A | CP-1A handoff | Upstream analytical handoff | 2017 to November 5, 2026 | Genesis Energy LP | Business, ownership, transactions, governance | Legal documents not supplied | CP-2 business risk |
| HND-02 | CP-2 handoff | Upstream analytical handoff | as-of 2026-11-05 | Genesis Energy LP | Credit view, key findings, risks | Confidence below High | Committee view |

#### T5B.2 Top five material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Liquidity and maturity profile | CP-1; CP-2 | Cash USD 41.477 million, revolver availability USD 894.4 million, no maturity before January 15, 2029 | Determines whether debt service and the 2029 and 2030 refinancing can be met without market access | Sets near-term default and refinancing risk | 10-Q Q3 pages:2, 17-18, 49 | Availability is subject to covenants; credit agreement not supplied |
| 2 | Leverage and interest cover | CP-1; CP-2 | Computed 5.18x total debt to EBITDA, 5.12x net, 2.36x cover on last-twelve-months data | Fixed high coupons against a margin base concentrated in offshore pipelines | Sets tolerance for an EBITDA shortfall | 10-K pages:166-167, 191, 210; 10-Q Q3 pages:2-3, 14-15, 29 | Computed basis differs from management and covenant basis |
| 3 | Contracted offshore base and Shenandoah volumes | CP-1A; CP-2 | 67.7% of nine-month Segment Margin from offshore pipelines; Shenandoah volumes below the MVC in Q3 2026 | MVC floors hold margin but not growth; third-party wells drive upside | Determines earnings stability behind debt service | 10-Q Q3 pages:26, 40; release page:4 | MVC levels and contract terms not supplied |
| 4 | Covenant headroom | CP-1; CP-2 | Management ratio 5.03X against a 5.75x maximum; cushion USD 76.041 million | Revolver availability depends on staying inside the leverage test | Governs access to liquidity and refinancing room | Release R3 pages:1, 11; 10-Q Q3 page:17 | Definitions in unsupplied agreement; cash and inventory inputs conflict |
| 5 | Debt-funded preferred purchases and distributions | CP-1A; CP-2 | Debt principal rose by USD 163.740 million while preferred units were bought for USD 221.6 million | Junior capital replaced by senior debt; control with Class B holders | Raises senior claims and limits deleveraging | 10-Q Q3 pages:14-15, 19, 21; 10-K page:64 | Seller identity and legal capacity not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Liquidity and maturity profile | CP-1 | Q3 10-Q pages:2, 17, 18, 49 | Yes | High (filed) | Directly Sourced | Supported | High | Committee-Ready |
| Leverage 5.18x, net 5.12x, cover 2.36x | CP-1 | 10-K pages:166-167, 191, 210; Q3 10-Q pages:2-3, 14-15, 29 | Yes | Medium (analyst calculation on filed lines) | Calculated | Supported; recomputed | Medium | Committee-Ready with basis label |
| Offshore base is 67.7% of Segment Margin; Shenandoah below the MVC in Q3 2026 | CP-1A | Q3 10-Q pages:26, 40 | Yes | High (filed); Segment Margin is a management measure | Calculated | Supported | Medium | Committee-Ready |
| Covenant leverage 5.03X against 5.75x maximum; cushion 12.5% | CP-1 | Q3 release pages:1, 11; Q3 10-Q page:17 | Partial | Medium (management release) | Directly Sourced | Supported as management-reported; inputs conflict | Medium | Remediation Needed |
| Debt-funded preferred purchases | CP-1A | Q3 10-Q pages:14-15, 21 | Yes | High (filed) | Calculated | Supported; seller identity not disclosed | Medium | Committee-Ready |
| Control by Class B holders; family holds 77% | CP-1A | Q3 10-Q page:19; 10-K page:64 | Yes | High (filed) | Directly Sourced | Supported | High | Committee-Ready |
| Management guidance near or below the low end | CP-1A | Q3 release page:4 | Yes | Medium (management release) | Directly Sourced | Management Language, not adopted | Medium | Committee-Ready |
| Inventory financing item is a sublimit size, not borrowing | CP-1; CP-1A | 10-K page:12; Q3 10-Q page:17; Q3 release page:11 | Yes | Medium | Conflicting | Logged, unresolved | Low | Remediation Needed |
| Covenant interest coverage and senior secured leverage headroom | CP-1 | None located | No | Not applicable | Insufficient Information | Not calculable | Low | Not Traceable |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents were USD 41.477 million at September 30, 2026 | CP-1 Chart data: liquidity -> Q3 10-Q balance sheet | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | page:2 balance sheet | CP-1 liquidity chart; CP-2 Key findings | Sourced | High (filed, unaudited) | Restricted cash of 4,975 thousand shown separately and excluded |
| Revolver availability was USD 894.4 million, subject to covenants | CP-1 Chart data: liquidity -> Q3 10-Q debt note | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | page:18 note 10 | CP-1 liquidity chart; CP-2 Credit view | Sourced | High (filed, unaudited) | Equals 900.0 less letters of credit of 5.6 (page:17); recomputed |
| AR Facility limit USD 99.5 million, fully drawn, expires June 26, 2029 | CP-1 Debt register -> Q3 10-Q debt note | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | page:16 note 10 | CP-1 debt register; CP-1A Transaction summary | Sourced | High (filed, unaudited) | Classified current on the balance sheet (page:2) |
| Senior unsecured notes principal USD 3,150.0 million in five series | CP-1 Debt register -> Q3 10-Q debt table | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | pages:14-15 note 10 | CP-1 debt register and maturity chart | Sourced | High (filed, unaudited) | Series, rates and maturities match the table |
| No debt matures before January 15, 2029 | CP-1 Chart data: debt maturities; CP-2 Credit view -> Q3 10-Q MD&A | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | page:49 liquidity | CP-1 maturity chart; CP-2 Key findings | Sourced | High (filed, unaudited) | Statement is management's in MD&A and agrees with the debt table; AR Facility is classified current but expires in 2029 |
| Total debt principal rose to USD 3,249.5 million from USD 3,085.760 million | CP-1 Credit narrative; CP-2 Key findings -> 10-K and Q3 10-Q debt tables | 10-K_2025-12-31_gel-20251231.htm.jsonl; 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-01; SRC-04 | 10-K page:191; 10-Q pages:14-15 | CP-1 leverage; CP-2 Key findings | Calculated | High (filed) | Difference 163,740 thousand recomputed; also equals movements in notes, AR Facility and revolver |
| LTM Q3 2026 computed EBITDA is USD 626.898 million | CP-1 Calculations -> 10-K and 10-Q operating statements | 10-K_2025-12-31_gel-20251231.htm.jsonl; 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-01; SRC-04 | 10-K pages:166-167; 10-Q page:3 | CP-1 leverage, cover; CP-2 Credit view | Calculated | Medium (analyst calculation from filed lines) | Operating income + D&A + equity earnings - 2026 gain on sale; recomputed from source text and matched |
| Total debt to EBITDA 5.18x and net debt to EBITDA 5.12x (LTM Q3 2026) | CP-1 Chart data: leverage | 10-K_2025-12-31_gel-20251231.htm.jsonl; 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-01; SRC-04 | 10-K page:191; 10-Q pages:2, 14-15 | CP-1 leverage chart; CP-2 Credit view | Calculated | Medium (analyst calculation) | Uses debt principal; carrying-value basis gives 5.11x and 5.05x (see calculation register) |
| EBITDA to cash interest 2.36x (LTM Q3 2026) | CP-1 Chart data: interest cover | 10-K_2025-12-31_gel-20251231.htm.jsonl; 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-01; SRC-04 | 10-K page:210; 10-Q page:29 | CP-1 interest cover chart; CP-2 Key findings | Calculated | Medium (analyst calculation) | Cash interest is payments of interest and commitment fees; consolidated, not continuing-only |
| Management reports covenant leverage of 5.03x against a 5.75x maximum | CP-1 Covenants and definitions review -> Q3 release and Q3 10-Q | EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl; 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-07; SRC-04 | release pages:1, 11; 10-Q page:17 | CP-1 covenant table; CP-2 Key findings | Sourced | Medium (management release); High for covenant level (filed) | Definitions are in the credit agreement, which is not supplied |
| EBITDA cushion of USD 76.041 million (12.5%) at the 5.75x maximum | CP-1 Covenant cushion -> Q3 release ratio table | EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | SRC-07 | page:11 ratio table | CP-1 covenant review; CP-2 Key findings | Calculated | Medium (analyst calculation on management inputs) | Inputs include a cash figure and an inventory deduction that differ from the filing |
| Cash for the leverage ratio is 40,553 thousand against 41,477 thousand on the balance sheet | CP-1 Conflicts -> Q3 10-Q and Q3 release | 10-Q_2026-09-30_gel-20260930.htm.jsonl; EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | SRC-04; SRC-07 | 10-Q page:2; release page:11 | CP-1 conflicts; CP-1A conflicts | Conflicting | Medium | Both spans preserved; release page:2 states approximately 41.5 million unrestricted cash on hand, consistent with the balance sheet |
| Inventory financing item of USD 10.5 million: sublimit or outstanding borrowing | CP-1 Conflicts; CP-1A Conflicts -> 10-K, Q3 10-Q, Q3 release | 10-K_2025-12-31_gel-20251231.htm.jsonl; 10-Q_2026-09-30_gel-20260930.htm.jsonl; EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | SRC-01; SRC-04; SRC-07 | 10-K page:12; 10-Q page:17; release page:11 | CP-1 conflicts; CP-1A conflicts | Conflicting | Medium | 10-K calls the quantity an inventory borrowing base; release deducts it as outstanding borrowings; not reconciled, not netted |
| Run-rate coupon on the notes is USD 247.625 million a year | CP-1 Calculations; CP-2 Key findings -> Q3 10-Q debt table | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | pages:14-15 note 10 | CP-2 Key findings | Calculated | Medium (analyst calculation) | Principal x stated rate for five series; excludes revolver, AR Facility and fees |
| Offshore pipelines were 67.7% of nine-month 2026 Segment Margin | CP-1A Fact register; CP-2 Strengths -> Q3 10-Q segment note | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | page:26 note 13 | CP-1A fact register; CP-2 Strengths | Calculated | Medium (analyst calculation on a management measure) | 320,508 / 473,128; Segment Margin is a non-GAAP management measure |
| Q3 2026 Shenandoah volumes were below the minimum volume commitment | CP-1A Fact register -> Q3 10-Q MD&A | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | page:40 MD&A | CP-1A fact register; CP-2 Credit view | Sourced | High (filed, unaudited) | MVC level and contract terms not supplied |
| Adjusted EBITDA for 2026 will likely be near or below the low end of guidance | CP-1A Fact register; CP-2 Strengths and weaknesses -> Q3 release | EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | SRC-07 | page:4 | CP-1A fact register; CP-2 Weaknesses | Sourced | Medium (management release) | Management Language; guidance range not supplied |
| Operating cash flow of USD 340.898 million in nine months 2026 included a working capital inflow of USD 58.619 million | CP-1 Statement extraction -> Q3 10-Q cash flow statement | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | page:5 | CP-1 cash flow quality; CP-2 Key findings | Sourced | High (filed, unaudited) | Nine-month 2025 comparative includes discontinued operations |
| Cash after capital payments and distributions was USD 101.661 million in nine months 2026 | CP-1 Calculations -> Q3 10-Q cash flow statement | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | pages:5-6 | CP-2 Key findings | Calculated | Medium (analyst calculation) | 340,898 - 84,996 - 68,531 - 38,946 - net noncontrolling distributions of 46,764; recomputed |
| Preferred units bought in 2026: 6,459,192 units for USD 221.6 million | CP-1A Transaction summary -> Q3 10-Q equity note | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | page:21 note 11 | CP-1A transaction summary; CP-2 Key findings | Calculated | High for components (filed); calculation by analyst | Sum of three purchases; cash flow statement shows 221,594 thousand redeemed, consistent after rounding |
| Class B units elect the whole board; family and affiliates hold 77% of them | CP-1A Ownership and control -> Q3 10-Q and 10-K risk factors | 10-Q_2026-09-30_gel-20260930.htm.jsonl; 10-K_2025-12-31_gel-20251231.htm.jsonl | SRC-04; SRC-01 | 10-Q page:19; 10-K page:64 | CP-1A ownership; CP-2 Weaknesses | Sourced | High (filed) | Ownership percentages as of the 10-K date |
| The $750.0 million 6.750% notes due 2034 refinanced the 2028 notes | CP-1A Transaction summary -> Q3 10-Q debt note | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | page:18 note 10 | CP-1A transaction summary; CP-2 Key findings | Sourced | High (filed, unaudited) | Net proceeds about 735.9 million |
| Alkali Business sold February 28, 2025 for a gross USD 1.425 billion | CP-1A Transaction summary -> Q3 10-Q note 4 | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | page:11 note 4 | CP-1A transaction summary | Sourced | High (filed, unaudited) | Comparatives separate discontinued operations |
| Hurricane Isaias caused about four days of offshore disruption in early October 2026 | CP-1A Fact register -> Q3 release | EX-99.1_2026-11-05_a90ex9918kearnings_q32026.htm.jsonl | SRC-07 | page:4 | CP-1A fact register; CP-2 Key credit risks | Sourced | Medium (management release) | Subsequent event; not in the Q3 10-Q |
| The seller of the 2026 repurchased preferred units is not named | CP-1A Fact register -> Q3 10-Q equity note | 10-Q_2026-09-30_gel-20260930.htm.jsonl | SRC-04 | page:21 note 11 | CP-1A fact register | Insufficient Information | High (filed) | Identity not disclosed; no inference made |
| A reported interest coverage covenant figure | CP-1 Covenants and definitions review -> not in any source | none | none | Not located | CP-1 covenant table; CP-2 Gaps | Insufficient Information | Not applicable | Covenant requires 2.00x through December 31, 2026; the reported figure is not supplied, so headroom is not calculable |
| The sector is Pipe Lines (No Natural Gas) and the country is the United States | CP-1A Company profile -> run settings | context | SRC-08 | context file | CP-1A company profile | Sourced | Run setting, not issuer evidence | Labelled as a run setting in CP-1A |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM computed EBITDA (Q1, Q2, Q3 2026) | CP-1 Calculations | FY2025 + year-to-date 2026 - year-to-date 2025 of operating income, D&A and equity earnings, less the 2026 gain on sale | Operating income + D&A + equity in earnings - gain on sale; LTM = FY + YTD current - YTD prior | Calculated; recomputed from source text: 596,939; 630,482; 626,898 thousand | Supported | Medium | PD, refinancing | 10-K pages:166-167; 10-Q pages:3 |
| Total debt / EBITDA | CP-1 Chart data: leverage; CP-2 | Debt principal and LTM EBITDA at each date | 3,085.760/537.891; 3,224.100/596.939; 3,249.500/630.482; 3,249.500/626.898 | Calculated; recomputed: 5.74, 5.40, 5.15, 5.18 | Supported | Medium | PD, leverage tolerance | 10-K page:191; 10-Q pages:12, 15 |
| Net debt / EBITDA | CP-1 Chart data: leverage | Total debt less unrestricted cash | (Debt - cash) / EBITDA: 5.72, 5.39, 5.09, 5.12 | Calculated; recomputed | Supported | Medium | PD, liquidity | Balance sheets pages:2 |
| EBITDA / cash interest | CP-1 Chart data: interest cover | LTM EBITDA over LTM payments of interest and commitment fees | 537.891/282.4; 596.939/268.1; 630.482/266.2; 626.898/266.1 | Calculated; recomputed: 1.90, 2.23, 2.37, 2.36 | Supported; FY2025 may be understated | Medium | Debt service | 10-K page:210; 10-Q pages:24, 29 |
| Revolver availability | CP-1 liquidity chart | Commitment less borrowings less letters of credit | 800.0-6.4-5.0=788.6; 900.0-74.1-6.8=819.1; 900.0-5.6=894.4 | Calculated; matches printed availability each date | Supported | High | Liquidity | 10-K page:194; 10-Q pages:14, 17-18 |
| Covenant EBITDA cushion | CP-1 Covenant cushion | Adjusted Debt / 5.75 compared with Adjusted Consolidated EBITDA | 3,055,602/5.75=531,409; 607,450-531,409=76,041; 12.5% | Calculated; recomputed | Supported on management inputs | Medium | Covenant headroom | Release R3 page:11 |
| Run-rate note coupon | CP-1 Calculations; CP-2 | Principal x stated rate | 600 x 8.250% + 500 x 8.875% + 700 x 7.875% + 600 x 8.000% + 750 x 6.750% = 247.625 | Calculated; recomputed | Supported | Medium | Debt service | 10-Q Q3 pages:14-15 |
| Free cash after distributions, nine months 2026 | CP-1 Calculations; CP-2 | Operating cash flow less capital payments and distributions | 340,898 - 84,996 - 68,531 - 38,946 - (53,442 - 6,678) = 101,661 | Calculated; recomputed | Supported | Medium | Liquidity, cash conversion | 10-Q Q3 pages:5-6 |
| Segment shares | CP-1A; CP-2 | Segment Margin over total | 320,508/473,128 = 67.7%; 82,246/473,128 = 17.4%; 70,374/473,128 = 14.9% | Calculated; recomputed | Supported | Medium | Revenue durability | 10-Q Q3 page:26 |
| Preferred units bought and price | CP-1A | Sum of three 2026 purchases | 741,620 + 3,263,127 + 2,454,445 = 6,459,192; 25.0 + 112.2 + 84.4 = 221.6 | Calculated; recomputed | Supported | Medium | Capital allocation | 10-Q Q3 page:21 |
| Debt on balance sheet carrying basis | CP-5 recomputation (not used upstream) | Notes net of costs plus AR Facility | 3,106,655 + 99,500 = 3,206,155 thousand; delta to principal 43,345; 3,206.155/626.898 = 5.11x; net 5.05x | Calculated here to log the gross delta | Supported | Medium | Leverage basis | 10-Q Q3 pages:2, 15 |
| Illustrative EBITDA decline to 5.75x on the computed basis | CP-2 Calculations | Debt principal / 5.75 | 3,249.5/5.75 = 565.130; 626.898 - 565.130 = 61.768; 9.9% | Assumption-Based illustration; recomputed; computed basis, not the covenant test | Supported as labelled | Low | Leverage tolerance | CP-1 figures |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Critical | Covenant headroom of 12.5% and covenant leverage 5.03X | Rests on management inputs; the executed credit agreement defining Consolidated EBITDA, adjustments and covenant debt is not in the source set | Insufficient Information (for legal definition) | Headroom determines revolver access and refinancing room (PD, liquidity) | Add the Eighth Amended and Restated Credit Agreement and compliance certificate | CP-1 covenant review; CP-2 Key findings and risks |
| Material | Inventory financing item of USD 10.5 million | 10-K labels the quantity an inventory borrowing base; release deducts it as outstanding borrowings; CP-1 hedged and CP-1A logged the conflict | Conflicting | Changes management Adjusted Debt and the ratio | Confirm from credit agreement; do not net; keep both spans | CP-1 conflicts; CP-1A conflicts |
| Material | Cash used in the leverage ratio (40,553 vs 41,477 thousand) | Release uses cash of restricted subsidiaries; reason not reconciled in sources | Conflicting | Changes adjusted debt by under USD 1 million; basis difference | Confirm definition in the credit agreement | CP-1 conflicts; CP-2 Gaps |
| Material | FY2025 Adjusted EBITDA and covenant ratio | Not printed in the 10-K; FY2025 leverage uses computed EBITDA | Insufficient Information | Trend from year end cannot be shown on the covenant basis | Obtain from the year-end release if needed | CP-1 metrics table; CP-2 Gaps |
| Material | Guidance range and MVC terms | Not supplied; guidance is Management Language | Insufficient Information | Distance to guidance and the size of the Shenandoah floor unknown | Add call materials or contract terms | CP-1A fact register; CP-2 Key findings |
| Minor | Leverage on principal rather than carrying value | Upstream used debt principal; balance sheet carrying value is 43,345 thousand lower | Calculated | Leverage is 5.11x on carrying value against 5.18x on principal | Label basis; log delta (done here) | CP-1 leverage chart; CP-2 |
| Minor | FY2025 interest cover | Payments include commitment fees and may include Alkali interest for January and February 2025 | Weak Lineage (perimeter) | FY2025 cover may be understated | Prefer LTM Q3 2026 | CP-1 interest cover chart |
| Minor | Seller of repurchased preferred units and current holders | Not disclosed; 10-K ownership predates 2026 purchases | Insufficient Information | Governance reading incomplete | Add ownership update | CP-1A ownership |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2025 to Q3 2026; legal documents, organization chart and call materials absent | Missing legal terms leave covenant definitions and guarantor perimeter unverified | Covenant headroom and legal capacity cannot be cleared for committee reliance | Add credit agreement, indentures, exhibit 22.1 |
| Citation completeness | Committee-Ready | Every figure in the three handoffs carries a page locator or a calculation shown with inputs; quotes were matched to source text | Low risk of unsupported claims | Claims can be relied on as traced | None |
| Calculation traceability | Committee-Ready | Twelve calculations recomputed from the source figures and matched; the four main ratio series were recomputed from the extracted statement lines | Low risk of arithmetic error | Leverage, cover and liquidity figures reproduce | Label computed versus management basis |
| Assumption transparency | Ready with Remediation | EBITDA definition is an analyst choice (excludes the 2026 gain; includes equity earnings and 100% of subsidiaries with noncontrolling holders); debt on principal basis | Basis choices move ratios by up to 0.07x on carrying value and differ from management | Ratios must not be compared with management or covenant ratios without the label | Keep basis labels in every use |
| Markdown and export artifact integrity | Committee-Ready | Each handoff has the required headings, tables and sha256 lineage; the run accepted CP-0, CP-1, CP-1A and CP-2 | Low risk of broken lineage | Downstream consumers can read the handoffs | None |

Overall auditability is Ready with Remediation, the lowest of the five dimension assessments.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed Eighth Amended and Restated Credit Agreement and compliance certificate not supplied | Covenant definitions, adjustments and reported interest coverage and senior secured ratios | Covenant headroom governs revolver access (liquidity, PD) | CP-1 covenant review; CP-2 Key findings | High | Exhibit 10.1 to the March 31, 2026 10-Q |
| CP-5-GAP-002 | Note indentures and exhibit 22.1 guarantor list not supplied | Collateral, guarantor release and restricted payment terms | Structural ranking and creditor control depend on them | CP-1 debt register; CP-1A governance | High | Indentures and June 30, 2026 10-Q exhibit 22.1 |
| CP-5-GAP-003 | FY2025 Adjusted EBITDA and year-end covenant ratio not printed | Year-end release | Trend of the management ratio cannot start at year end | CP-1 metrics table | Medium | Fourth-quarter 2025 release |
| CP-5-GAP-004 | Cash and inventory financing items conflict between 10-Q and release | Credit agreement definition | Management ratio inputs not reproducible | CP-1 conflicts; CP-2 Gaps | Medium | Credit agreement and compliance certificate |
| CP-5-GAP-005 | Guidance range, call transcripts and MVC terms not supplied | Year-end call materials; offshore contracts | Distance to guidance and floor size unknown | CP-1A fact register; CP-2 Key findings | Medium | Year-end call transcript |
| CP-5-GAP-006 | Seller of repurchased preferred units and current preferred holders not disclosed | Ownership update | Governance reading incomplete | CP-1A ownership | Low | Schedule 13D/G or a later ownership table |
| CP-5-GAP-007 | Organization chart image not extracted | Chart text | Guarantor and subsidiary structure rests on narrative | CP-1A company profile | Low | 10-K page:9 image |

#### T5.1 Source gate and input module register

| Module | Handoff canonical .md / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | CP-0 handoff; run gel-2026-11-05-credit_snapshot-host; sha256 4b65b015...a40acae | Source readiness for seven sources | High (filed documents; extraction unreviewed) | Six H2 headings present; Readiness view after Reader summary | Ready with limitations | Legal documents, organization chart not supplied |
| CP-1 | CP-1 handoff; run gel-2026-11-05-credit_snapshot-host; sha256 d4624282...78f4 | Financial base FY2025 to Q3 2026 | High for printed lines; Medium for calculations | Six H2 headings, four chart tables and metrics table present | Ready with limitations | Management ratio basis differs from computed basis |
| CP-1A | CP-1A handoff; run gel-2026-11-05-credit_snapshot-host; sha256 48e419f8...1ca11 | Business, ownership, transactions, governance | High for filed facts; management language labelled | Six H2 headings, selector tables and prose present | Ready with limitations | Executed documents not supplied |
| CP-2 | CP-2 handoff; run gel-2026-11-05-credit_snapshot-host; sha256 cbd45124...e2f3e | Fundamental credit synthesis | Medium (upstream only) | Six H2 headings, Credit view 110 words, prose selectors present | Ready with limitations | Confidence capped below High |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Critical | CP-1; CP-2 | Covenant leverage 5.03X and 12.5% cushion | Supported as management-reported only | No executed agreement behind the definitions | Add credit agreement and compliance certificate | Restricts reliance on headroom |
| Material | CP-1; CP-1A | Inventory financing item | Conflicting | Three labels for one quantity | Confirm and keep un-netted | Management ratio not reproducible |
| Minor | CP-1A | Seller of preferred units | Insufficient Information | Not named in filings | Add ownership update | None beyond governance reading |
| Minor | CP-2 | Illustrative EBITDA decline of 9.9% | Assumption-Based and labelled | Cross-basis illustration | Keep label | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Total debt and net debt use principal | Canon debt basis is balance sheet carrying value; delta 43,345 thousand | None; both values in the filing | Log delta (done); show 5.11x and 5.05x | None |
| Minor | CP-1 | FY2025 EBITDA / cash interest | Cash interest includes commitment fees and consolidated perimeter; EBITDA is continuing operations | 10-K page:210 is consolidated | Prefer LTM | None |
| Material | CP-1; CP-2 | Computed EBITDA versus management Adjusted EBITDA and covenant EBITDA | Three EBITDA definitions in use | Release states net-to-ownership and pro forma adjustments | Keep labels in every use | Ratios not comparable without label |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Critical | CP-1; CP-1A; CP-2 | Covenant levels, springing revolver maturities, guarantor coverage, bankruptcy-remote AR Facility, preferred ranking and Class B board election | Eighth credit agreement, note indentures, exhibit 22.1, partnership agreement | Only the filings' summaries are supplied | Add the documents | Legal review required before reliance |
| Material | CP-1A | No priming, uptiering or collateral release appears | Credit agreement and indentures | Absence of evidence is not evidence of absence of capacity | Add the documents | Legal review required |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | No market or relative-value claim is made in CP-1, CP-1A or CP-2 | Market prices, spreads, peers and ratings are blank in the run settings | Not in scope of the requested modules | None for this run | None; relative value belongs to a later module |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-1; CP-1A | Inventory financing item: CP-1 said it was probably a sublimit size but unconfirmed; CP-1A found the 10-K wording inventory borrowing base | CP-1 is accepted and cannot be edited; CP-1A states the correction | CP-1A statement controls; both spans preserved | Management ratio still not reproducible |
| Minor | CP-1; CP-1A; CP-2 | Preferred purchase total 221.6 (CP-1A, CP-2) versus 221.594 (CP-1 cash flow) | Same transaction, rounded versus exact | Cite the exact figure where it matters | None |
| Minor | CP-0; CP-1 | CP-0 listed the cash difference as unreconciled; release page:2 states approximately 41.5 million unrestricted cash, supporting the balance sheet figure | No version conflict | Carry both figures | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Duplication | Several limitations about the credit agreement recur across modules | Each module states it where it changes a conclusion; CP-2 restates it in gaps only | None |
| Material | CP-2 | Materiality | Covenant headroom is a top-five driver whose basis is the weakest | Keep headroom statements qualified | Committee should read headroom as management-reported |

#### T5.8 Structured export and handoff integrity

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Chart data tables | Cash interest label in chart is payments of interest and commitment fees | Label kept; no change needed | None |
| Minor | CP-1A | Selector sections | Transaction section is prose only as required | None | None |
| Minor | CP-2 | Credit view | 110 words, first sentence states the view | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISS-01 | Critical | CP-1; CP-2 | Missing legal source | Covenant headroom and legal capacity rest on management-reported figures; executed agreements not supplied | Add the credit agreement and indentures | Restricts committee reliance on covenant headroom and legal capacity | Open |
| ISS-02 | Material | CP-1; CP-1A | Conflict | Inventory financing item labelled sublimit, borrowing base and outstanding borrowing in different sources | Confirm from credit agreement; keep un-netted | Management ratio cannot be reproduced | Open (logged) |
| ISS-03 | Material | CP-1; CP-2 | Conflict | Cash 41,477 vs 40,553 thousand in the ratio | Confirm definition | Management ratio cannot be reproduced | Open (logged) |
| ISS-04 | Material | CP-1; CP-2 | Missing evidence | FY2025 Adjusted EBITDA and year-end covenant ratio not printed | Use computed basis, label it | FY2025 comparison is on the computed basis only | Open (disclosed) |
| ISS-05 | Material | CP-1A; CP-2 | Missing evidence | Guidance range and MVC terms not supplied | Add call materials | Business risk reading bounded | Open |
| ISS-06 | Minor | CP-1; CP-2 | Definition | Leverage on principal (5.18x) versus carrying value (5.11x); delta 43,345 thousand | Label basis; delta logged here | None beyond labelling | Closed (logged) |
| ISS-07 | Minor | CP-1 | Perimeter | FY2025 cash interest consolidated and includes commitment fees; may include Alkali interest | Prefer LTM Q3 2026 | FY2025 cover possibly understated | Closed (disclosed) |
| ISS-08 | Minor | CP-1; CP-2 | Classification | AR Facility is a current borrowing on the balance sheet but sits in 2029 in the maturity chart | Keep both labels | None | Closed (disclosed) |
| ISS-09 | Minor | CP-2 | Basis mixing | Illustrative 9.9% EBITDA decline uses computed EBITDA against the covenant maximum | Keep the illustration label | None if labelled | Closed (disclosed) |
| ISS-10 | Minor | CP-1; CP-1A; CP-2 | Rounding | Preferred purchases are 221.6 (sum of rounded) in two modules and 221.594 in the cash flow statement | Treat as equal after rounding | None | Closed |
| ISS-11 | Minor | CP-1A | Missing evidence | Seller identity and current preferred holders not disclosed | Add ownership update | Governance reading incomplete | Open |
| ISS-12 | Minor | CP-1; CP-1A | Version | CP-1 said the inventory item was probably a sublimit size but unconfirmed; CP-1A found the 10-K borrowing base wording | CP-1A statement controls; CP-1 cannot be edited | None for figures | Closed |

## Calculations

Recomputed independently from the extracted source text for this module. Thousands of dollars unless stated.

| Check | Inputs from source | Result |
| --- | --- | --- |
| LTM computed EBITDA, Q1, Q2, Q3 2026 | Operating income, D&A, equity earnings and gain lines read from the statements (10-K_2025-12-31_gel-20251231.htm.jsonl pages:166-167; 10-Q_2026-03-31_gel-20260331.htm.jsonl, 10-Q_2026-06-30_gel-20260630.htm.jsonl, 10-Q_2026-09-30_gel-20260930.htm.jsonl page:3) | 596,939; 630,482; 626,898 (matches CP-1) |
| Debt principal at four dates | Debt tables (10-K_2025-12-31_gel-20251231.htm.jsonl page:191; 10-Q_2026-03-31_gel-20260331.htm.jsonl page:12; 10-Q_2026-06-30_gel-20260630.htm.jsonl page:15; 10-Q_2026-09-30_gel-20260930.htm.jsonl page:15) | 3,085,760; 3,224,100; 3,249,500; 3,249,500 (matches CP-1) |
| Cash at four dates | Balance sheets (page:166 and page:2) | 6,437; 4,210; 39,261; 41,477 (matches CP-1) |
| Total debt / EBITDA | Debt over LTM EBITDA | 5.74; 5.40; 5.15; 5.18 (matches CP-1) |
| Net debt / EBITDA | (Debt - cash) / EBITDA | 5.72; 5.39; 5.09; 5.12 (matches CP-1) |
| EBITDA / cash interest | EBITDA / (282.4; 268.1; 266.2; 266.1) | 1.90; 2.23; 2.37; 2.36 (matches CP-1) |
| Debt on carrying basis | 3,106,655 + 99,500 = 3,206,155; principal 3,249,500; delta 43,345 | 5.11x total and 5.05x net (3,206,155 - 41,477 = 3,164,678; / 626,898) |
| Covenant cushion | 3,055,602 / 5.75 = 531,409; 607,450 - 531,409 | 76,041; 12.5% (matches CP-1) |
| Run-rate coupon share | 247.625 / 626.898 | 39.5% (matches CP-2) |
| Statement counts | Rows in the lineage register | 27 statements: 14 Sourced, 9 Calculated, 2 Conflicting, 2 Insufficient Information |

## Gaps

Source gaps are in the gaps ledger above (CP-5-GAP-001 to CP-5-GAP-007). Additional limits of this audit:

| Gap | Effect | Action |
| --- | --- | --- |
| The scoring script and the automated handoff validator named in the CP-5 method are not part of this transport | The numeric confidence score and band are not computed; status is set from the Restricted rule | Run the scoring step if a numeric band is required |
| Extraction fidelity was not reviewed beyond locating quoted text and re-reading statement rows | Table alignment errors in source extraction remain possible | Spot-check the cited page when a figure is used |
| Charts, images and speaker notes are absent from the pack | No claim rests on them | None |

## Next module

No further module is selected in this run. Hand the four accepted handoffs to the committee with the clearance decision: Restricted, with covenant headroom and legal capacity excluded from reliance. The next evidence action is to add the Eighth Amended and Restated Credit Agreement, the compliance certificate, the note indentures and exhibit 22.1, then rerun this module.
