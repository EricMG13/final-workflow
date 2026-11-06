## Request

Issuer: STARWOOD PROPERTY TRUST, INC. (issuer id stwd), as of 2026-11-05, pathway credit_snapshot. Scope: trace the claims of the four accepted upstream handoffs (source readiness, financial base, business and transaction view, credit view) to the filed sources, recompute their calculations, grade the research for committee use, and record gaps; the underlying credit conclusion is not changed here. Module status is Ready with Limitations, traceability scope is the default Top 5 drivers plus a statement-level register, committee status is Restricted, and QA status is Restricted.

## Sources

Issuer sources relied on (page:N is the extraction chunk, not the printed page):

| Short name | Exact source name | sha256 |
| --- | --- | --- |
| 10-K FY2025 | 10-K_2025-12-31_stwd-20251231.htm.jsonl | 5d034c0380b12617b5276d804970154e60e42e6a23c5bcee4ef0d6e26b8a55fd |
| 10-Q Q3 2025 | 10-Q_2025-09-30_stwd-20250930.htm.jsonl | d42c4a9a27c9d73fda589e7dc56562d17c85018a2ea82a77ac4a395ea6aee3bc |
| 10-Q Q1 2026 | 10-Q_2026-03-31_stwd-20260331.htm.jsonl | a981c1ff096bebb78573fc217060d2be7d932d6a1d88404218dd31da70ce8980 |
| 10-Q Q2 2026 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | e8c4bcc3fcec859b834e7d77d0075c7162cba6647a0dd89e45052bfa9c8b4b3a |
| Release YE2025 | EX-99.1_2026-02-25_stwd_pressrelease-ye2025.htm.jsonl | 1f1cf65fe88590eb05e524e31bd92875cef8da770ee1cfa5cacc2e06538ebd9a |
| Release Q1 2026 | EX-99.1_2026-05-08_stwd_pressrelease-q12026.htm.jsonl | 316bfad5efe7ce527d0308c8cc555686397e0897e2159e9321c558a9bbed50a7 |
| Release Q2 2026 | EX-99.1_2026-08-06_stwd_pressrelease-q22026.htm.jsonl | b1942a46f485117f96015975cca8555da21dd98692e7e25a0fc84b19a0efbf22 |

Run-settings source `context` (bb1537683323815090e6da83a4ec1d608fc4d7c145051f90360ef72eab181e62): identity and period settings only; not issuer evidence.

Supplied handoffs (each opened in full and traced):

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 2dd5f2d188dcfd523c32c5571bb13634e5383866cc3b07a5a7ff8344297fbd4e | source identities, gaps and perimeter distinction re-anchored |
| CP-1 | 4e1540f23d70471fc4b9b2945093c91a4c0f050f9198457596131405cd3f82d1 | financial base, bridges and chart tables recomputed |
| CP-1A | 9e0df2f1a6fca390ee0368bc3a7cb1ba3a1c796d23d87e8940a5abeb1b921158 | business, governance and transaction claims traced |
| CP-2 | 88bacddd0c1534cdc1e8d252ab513c1dde7b772de5d8fdde696dc47352e73324 | credit view claims, liquidity and asset-quality figures traced |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial and funding facts trace to filed pages and recompute correctly, so the research is usable for them. Covenant, guarantor and rating conclusions cannot be traced, so committee use is restricted. | Medium | No indenture, credit agreement or management agreement is supplied, and nothing after August 6, 2026 is covered. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of 38 traced statements, 36 are sourced to filed or released text, one is a calculated total and one has no source in the pack. | The evidence base for the financial base and funding view is sound. | High |
| Of 19 calculation items recomputed, 18 matched exactly and one quoted amount had a rounding error. | Ratios such as 3.65x leverage can be relied on. | High |
| The nonaccrual total of about 947.3 million dollars is an analyst sum of prose amounts with an unclear comparator. | Asset-quality trend statements are not supported. | Medium |
| Covenant headroom, guarantor terms and ratings are missing. | Structural ranking and headroom cannot be verified. | High |
| Three small presentation defects in the credit view were found and corrected here. | They do not change the credit view. | High |

### Evidence trace view

The upstream analysis is traceable enough for its financial and funding facts and only partly traceable for covenant, guarantor and rating conclusions, so committee use is restricted. Of 38 statements traced to a located page, 36 are sourced to filed or released text, one is a calculated debt total and one, shareholder ownership, has no source in the pack. Of 19 calculation items recomputed, 18 matched exactly and one quoted amount had a rounding error. The critical provenance gap is documentary: no indenture, credit agreement or management agreement is supplied, so covenant headroom and structural ranking rest on filing descriptions. The decision most affected is reliance on the credit view, which should stay restricted until the documents and any later filings are obtained.

### Module status and committee grade

Module status: Ready with Limitations (all four upstream handoffs were available and accepted, with incomplete source packages). Traceability scope: Top 5. Committee status: Restricted. QA status: Restricted. The confidence score and band are script-owned and were not computed in this host run; under the canon a Restricted status caps the band at Low, and no score is asserted here. Severity counts across the issues register: five Material and seven Minor, none Critical, because no finding changes a reported economic figure or the recommendation, and the Material items concern monitoring and confidence. Strongest contrary evidence to the restriction: every figure that could be recomputed matched, and the sourced statements are exact strings on the cited pages; what would make the contrary view win is receipt of the executed debt documents and later filings.

### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10-K FY2025 (5d034c0380b12617b5276d804970154e60e42e6a23c5bcee4ef0d6e26b8a55fd) | 10-K_2025-12-31_stwd-20251231.htm.jsonl | Annual report, audited | FY2025 (year ended Dec 31, 2025) | Registrant, consolidated incl. VIEs | Audited statements, notes, MD&A, risk factors, covenants described | Extraction of HTML; fidelity not independently reviewed | CP-1, CP-1A, CP-2 |
| 10-Q Q3 2025 (d42c4a9a27c9d73fda589e7dc56562d17c85018a2ea82a77ac4a395ea6aee3bc) | 10-Q_2025-09-30_stwd-20250930.htm.jsonl | Quarterly report, unaudited | Q3 2025 and nine months 2025 | Registrant, consolidated | Q3 2025 statements, Sep 30, 2025 balance sheet, secured table | Comparative period only | CP-1, CP-2 |
| 10-Q Q1 2026 (a981c1ff096bebb78573fc217060d2be7d932d6a1d88404218dd31da70ce8980) | 10-Q_2026-03-31_stwd-20260331.htm.jsonl | Quarterly report, unaudited | Q1 2026 | Registrant, consolidated | Q1 2026 statements, Mar 31, 2026 balance sheet, secured table | Interim, unaudited | CP-1, CP-2 |
| 10-Q Q2 2026 (e8c4bcc3fcec859b834e7d77d0075c7162cba6647a0dd89e45052bfa9c8b4b3a) | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | Quarterly report, unaudited | Q2 2026 and six months 2026 | Registrant, consolidated | Latest statements, debt and covenant notes, subsequent events, MD&A | Interim, unaudited; liquidity-source bullets missing from extraction | CP-1, CP-1A, CP-2 |
| Release YE2025 (1f1cf65fe88590eb05e524e31bd92875cef8da770ee1cfa5cacc2e06538ebd9a) | EX-99.1_2026-02-25_stwd_pressrelease-ye2025.htm.jsonl | Earnings release exhibit; management-attributed | Q4 and FY2025 | Registrant; segment statements with VIE column | Q4 2025 statement, distributable earnings, headline liquidity | Management claims; filing controls | CP-1, CP-1A |
| Release Q1 2026 (316bfad5efe7ce527d0308c8cc555686397e0897e2159e9321c558a9bbed50a7) | EX-99.1_2026-05-08_stwd_pressrelease-q12026.htm.jsonl | Earnings release exhibit; management-attributed | Q1 2026 | Registrant; segment statements | Q1 2026 distributable earnings | Management claims; filing controls | CP-1 |
| Release Q2 2026 (b1942a46f485117f96015975cca8555da21dd98692e7e25a0fc84b19a0efbf22) | EX-99.1_2026-08-06_stwd_pressrelease-q22026.htm.jsonl | Earnings release exhibit; management-attributed | Q2 and six months 2026 | Registrant; segment statements and ex-VIE balance sheet | Q2 2026 distributable earnings, segment data, management statements | Management claims; filing controls | CP-1, CP-1A, CP-2 |
| context (bb1537683323815090e6da83a4ec1d608fc4d7c145051f90360ef72eab181e62) | 1465128-starwood-property-trust-inc-stwd.json | Run settings; not issuer evidence | As of 2026-11-05 | Issuer identity | Name, ticker, country, sector, periods, currency; no ratings, quotes or deal terms | No financial or legal data | All modules |

### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage rose: total debt to stockholders’ equity 3.65x at Jun 30, 2026 from 3.25x at Dec 31, 2025 | CP-1, CP-2 | Balance sheet lines for secured, securitized and unsecured debt and stockholders’ equity | Less equity beneath all creditors; debt funded growth while equity fell | Leverage tolerance and monitoring posture | 10-Q Q2 2026 page:4; 10-K FY2025 page:159 | Ratio is an analyst calculation on the GAAP perimeter; no covenant definition |
| 2 | Earnings below the dividend: Q2 2026 net income attributable 6,557 thousand against distributable earnings 151,503 thousand; distributable earnings per share 0.78 against 0.96 declared for 6M 2026 | CP-1, CP-2 | Filed income statement, equity statement and release reconciliation | A payout above earnings erodes equity | Dividend and buyback pace is a monitoring item | 10-Q Q2 2026 pages 5, 7 and 129; Release Q2 2026 page:5 | Distributable earnings is management-attributed |
| 3 | Asset quality: nonaccrual loans near 947.3 million dollars and 36.8% of commercial loans above 70% loan-to-stabilized-value | CP-2 | Loan credit-quality table and nonaccrual prose | Stops interest accrual and ties up capital; determines earnings recovery | Resolution of loans is the swing factor in the credit view | 10-Q Q2 2026 pages 32 and 33 | Nonaccrual total is an analyst sum of prose amounts |
| 4 | Funding access and maturity management: new unsecured notes in May and July 2026 retired the 2026 and January 2027 notes | CP-1, CP-1A, CP-2 | Debt notes and subsequent events | Reduces near-term refinancing risk | Supports the adequate-funding view | 10-Q Q2 2026 pages 57 and 101 | Post-June 30, 2026 events only through the Q2 report |
| 5 | Covenant and structural position: most debt is secured on pledged assets; covenant levels and headroom are not available | CP-2, CP-1A | Filing descriptions of covenants and security | Unsecured holders rank behind secured lenders on pledged assets; headroom cannot be monitored | Committee cannot rely on headroom; legal review needed | 10-Q Q2 2026 pages 50, 52, 57, 143 and 145; 10-K FY2025 pages 34 and 35 | Governing documents not supplied |

### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 3.65x versus 3.25x | CP-1, CP-2 | Balance sheet debt lines and equity (10-Q Q2 2026 page:4) | Yes | High | Calculated | Supported; recomputed | High | Committee-Ready |
| Equity fell because dividends declared exceeded net income | CP-1 | Equity roll check: 58,435 less 357,326 equals (298,891) against the accumulated deficit change (10-Q Q2 2026 pages 4 and 7) | Yes | High | Calculated | Supported; recomputed | High | Committee-Ready |
| Q2 2026 earnings thin; distributable earnings far above GAAP | CP-1, CP-2 | Income statement and release reconciliation | Yes | High for GAAP, Medium for distributable earnings | Directly Sourced | Supported; measure is management-attributed | High | Committee-Ready |
| Dividend not covered by distributable earnings per share (0.81x) | CP-1, CP-2 | 0.78 over 0.96 (10-Q Q2 2026 pages 7 and 129) | Yes | Medium | Calculated | Supported; recomputed | High | Committee-Ready |
| Nonaccrual loans near 947.3 million dollars | CP-2 | Prose amounts at 10-Q Q2 2026 page:33 | Yes | Medium | Calculated | Supported with scope caveat; comparator scope unclear | Medium | Remediation Needed |
| 36.8% of commercial loans above 70% loan-to-stabilized-value | CP-2 | Credit-quality table (10-Q Q2 2026 page:32) | Yes | High | Calculated | Supported; recomputed | High | Committee-Ready |
| Unsecured 2026 and January 2027 maturities cleared by new notes | CP-1, CP-1A, CP-2 | Subsequent events (10-Q Q2 2026 page:101) | Yes | High | Directly Sourced | Supported; subsequent event | High | Committee-Ready |
| Approved undrawn secured capacity of 1,399.0 million dollars | CP-1, CP-2 | Facility table (10-Q Q2 2026 page:143) | Yes | High | Directly Sourced | Supported; not stated to be committed | High | Committee-Ready |
| Revolver of 200.0 million dollars committed and undrawn; no letters of credit reduce it | CP-2 | Revolver size (10-K FY2025 page:103) and undrawn 200,000 (10-Q Q2 2026 page:143) | Yes | Medium | Analyst Inference | Size and undrawn amount sourced; absence of letters of credit inferred | Medium | Remediation Needed |
| Covenant compliance stated; headroom Not calculable | CP-2 | Compliance statements (10-Q Q2 2026 pages 50, 52, 57) | Yes | High for compliance, none for levels | Insufficient Information | Levels not supplied | High on compliance statement, Low on headroom | Not Traceable for headroom |
| Guarantors and ratings not available | CP-0, CP-2 | Searches of all periodic reports found none | Yes (search record) | Not applicable to a missing datum | Insufficient Information | Gap preserved | High that they are missing | Not Traceable |
| Manager fee terms, termination fee and related-party loan approvals | CP-1A, CP-2 | 10-K FY2025 pages 26, 237, 238; 10-Q Q2 2026 page:69 | Yes | High | Directly Sourced | Supported; agreement itself not supplied | High | Committee-Ready |
| Governance effect on creditors (weaker control) | CP-1A, CP-2 | Same pages | Yes | Medium | Analyst Inference | Reasoned from terms; no creditor-adverse action found | Medium | Committee-Ready |
| Fundamental acquisition and long lease profile | CP-1A | 10-K FY2025 pages 9 and 188; 10-Q Q2 2026 page:141 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Management expects to resolve nearly 900 million dollars of underperforming assets | CP-1A, CP-2 | Release Q2 2026 page:1 | Yes | Low | Directly Sourced | Management Language; not adopted | Low | Committee-Ready as labelled |
| Total assets on two perimeters (61,046,276 and 31,772,112 thousand) | CP-0, CP-1, CP-1A | 10-Q Q2 2026 page:4; Release Q2 2026 pages 1 and 7 | Yes | High and Medium | Conflicting | Logged, not reconciled; different perimeters | High | Committee-Ready with perimeter label |

### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt at Jun 30, 2026 is the sum of secured financing agreements, securitized financing and unsecured senior notes, net | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:4 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:4 | CP-1 Calculations; CP-2 Key findings | Calculated | High | Components on one balance sheet; the other two lines are on the same page |
| Stockholders’ equity at Jun 30, 2026 and Dec 31, 2025 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:4 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:4 | CP-1 balance sheet table | Sourced | High | Filed unaudited balance sheet |
| Net income attributable to the registrant for Q2 2026, Q2 2025, 6M 2026 and 6M 2025 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:5 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:5 | CP-1 income statement tables; CP-2 Key findings | Sourced | High | Filed unaudited statement |
| Total revenues for the same periods | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:5 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:5 | CP-1 income statement tables | Sourced | High | Filed unaudited statement |
| Distributable earnings Q2 2026 of 151,503 thousand | EX-99.1_2026-08-06_stwd_pressrelease-q22026.htm.jsonl page:5 | EX-99.1_2026-08-06_stwd_pressrelease-q22026.htm.jsonl | Release Q2 2026 | page:5 | CP-1 distributable earnings table; CP-2 | Sourced | Medium | Company non-GAAP measure in an earnings release; management-attributed |
| Cash paid for interest, 6M 2026 and 6M 2025 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:9 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:9 | CP-1 cash flow table | Sourced | High | Supplemental cash flow disclosure |
| Dividends declared per share, 6M 2026 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:7 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:7 | CP-1 payout ratios; CP-2 | Sourced | High | Statement of equity |
| Distributable earnings per share, 6M 2026 of 0.78 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:129 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:129 | CP-1 payout ratios; CP-2 | Sourced | Medium | Management measure in the MD&A |
| Q4 2025 revenue of 492,948 thousand | EX-99.1_2026-02-25_stwd_pressrelease-ye2025.htm.jsonl page:5 | EX-99.1_2026-02-25_stwd_pressrelease-ye2025.htm.jsonl | Release YE2025 | page:5 | CP-1 quarterly table | Sourced | Medium | Release; ties to FY2025 less nine months 2025 from the 10-K and the Q3 2025 10-Q |
| Nine months 2025 revenue of 1,351,341 thousand | 10-Q_2025-09-30_stwd-20250930.htm.jsonl page:5 | 10-Q_2025-09-30_stwd-20250930.htm.jsonl | 10-Q Q3 2025 | page:5 | CP-1 tie-out | Sourced | High | Filed unaudited statement |
| FY2025 revenue of 1,844,289 thousand | 10-K_2025-12-31_stwd-20251231.htm.jsonl page:160 | 10-K_2025-12-31_stwd-20251231.htm.jsonl | 10-K FY2025 | page:160 | CP-1 tie-out | Sourced | High | Audited statement |
| Unsecured senior notes principal at Jun 30, 2026 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:56 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:56 | CP-1 debt table; CP-2 | Sourced | High | Filed note |
| July 2026 issuance of 5.875% notes due 2029 and use of proceeds (subsequent event) | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:101 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:101 | CP-1 pro forma; CP-1A; CP-2 | Sourced | High | Subsequent event, flagged as after Jun 30, 2026 |
| May 26, 2026 issuance of 6.125% notes due June 2031 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:57 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:57 | CP-1A; CP-2 | Sourced | High | Filed note |
| Secured and securitized financing principal and its repayment schedule | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:55 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:55 | CP-1 chart; CP-2 maturity table | Sourced | High | Company schedule on a fully extended or collateral-driven basis |
| Facility totals including approved but undrawn capacity of 1,399,046 thousand | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:143 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:143 | CP-1 liquidity; CP-2 liquidity | Sourced | High | Approved capacity is lender-approved against pledged assets; not stated to be committed |
| Corporate revolver and term loans: undrawn 200,000 thousand | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:143 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:143 | CP-2 liquidity | Sourced | High | Revolver size of 200.0 million dollars from the 10-K amendment text |
| Revolver size 200.0 million dollars and extension to January 2030 | 10-K_2025-12-31_stwd-20251231.htm.jsonl page:103 | 10-K_2025-12-31_stwd-20251231.htm.jsonl | 10-K FY2025 | page:103 | CP-2 liquidity | Sourced | High | No letters of credit against the revolver located; availability therefore read as not reduced (Analyst Inference) |
| Funding commitments by segment | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:148 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:148 | CP-2 claims outside debt | Sourced | High | Other two segments on the same page |
| Commercial loans above 70% loan-to-stabilized-value and their allowance | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:32 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:32 | CP-2 asset quality | Sourced | High | Company-model categories; derived share is a calculation |
| Nonaccrual loan amounts stated in prose | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:33 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:33 | CP-2 Key findings | Sourced | Medium | Total of 947.3 million dollars is the analyst’s sum of prose amounts |
| 68% of repurchase agreements have no valuation adjustment on capital market events | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:50 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:50 | CP-2 Key findings | Sourced | High | Filed note |
| Base management fee terms | 10-K_2025-12-31_stwd-20251231.htm.jsonl page:237 | 10-K_2025-12-31_stwd-20251231.htm.jsonl | 10-K FY2025 | page:237 | CP-1A; CP-2 | Sourced | High | Agreement itself not supplied |
| Termination fee of three times the sum of average annual fees | 10-K_2025-12-31_stwd-20251231.htm.jsonl page:26 | 10-K_2025-12-31_stwd-20251231.htm.jsonl | 10-K FY2025 | page:26 | CP-1A; CP-2 | Sourced | High | Risk-factor description, not the agreement |
| Related-party loans approved by the board with recusal | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:69 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:69 | CP-1A; CP-2 | Sourced | High | Aggregate exposure not given |
| Fundamental acquisition and debt assumed | 10-K_2025-12-31_stwd-20251231.htm.jsonl page:188 | 10-K_2025-12-31_stwd-20251231.htm.jsonl | 10-K FY2025 | page:188 | CP-1A | Sourced | High | Filed note |
| Share repurchase capacity remaining | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:147 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:147 | CP-1A; CP-2 | Sourced | High | Filed MD&A |
| Covenant types for secured facilities | 10-K_2025-12-31_stwd-20251231.htm.jsonl page:34 | 10-K_2025-12-31_stwd-20251231.htm.jsonl | 10-K FY2025 | page:34 | CP-2 covenants | Sourced | Medium | Risk-factor wording; levels not supplied |
| 120% unencumbered asset test for unsecured notes | 10-K_2025-12-31_stwd-20251231.htm.jsonl page:35 | 10-K_2025-12-31_stwd-20251231.htm.jsonl | 10-K FY2025 | page:35 | CP-2 covenants | Sourced | Medium | Definition not supplied; headroom Not calculable |
| ABS minimum debt service coverage covenants and compliance | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:52 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:52 | CP-2 covenants | Sourced | High | Levels not supplied |
| GAAP total assets of 61,046,276 thousand at Jun 30, 2026 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:4 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:4 | CP-1 perimeter; CP-1A conflict | Sourced | High | Consolidated perimeter including VIEs |
| Management segment subtotal assets of 31,772,112 thousand before the VIE column | EX-99.1_2026-08-06_stwd_pressrelease-q22026.htm.jsonl page:7 | EX-99.1_2026-08-06_stwd_pressrelease-q22026.htm.jsonl | Release Q2 2026 | page:7 | CP-1 perimeter | Sourced | Medium | Release; management presentation |
| Management expects to resolve nearly 900 million dollars of underperforming assets | EX-99.1_2026-08-06_stwd_pressrelease-q22026.htm.jsonl page:1 | EX-99.1_2026-08-06_stwd_pressrelease-q22026.htm.jsonl | Release Q2 2026 | page:1 | CP-1A; CP-2 | Sourced | Low | Management Language: a forward statement by management, carried as Management Language only |
| Four-quarter projected principal inflows against required financing repayments | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:146 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:146 | CP-2 maturity profile | Sourced | Medium | Management projection; excludes unsecured notes |
| Unsecured notes swapped notional of 3,875,000 thousand | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:151 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:151 | CP-2 strengths | Sourced | High | Filed risk disclosure at Jun 30, 2026, before the July 2026 hedge unwind |
| Office share of commercial portfolio of 17.6% | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:140 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:140 | CP-1A; CP-2 | Sourced | High | Share of a defined sub-portfolio, not total assets |
| Interest rate sensitivity of net investment income | 10-Q_2026-06-30_stwd-20260630.htm.jsonl page:152 | 10-Q_2026-06-30_stwd-20260630.htm.jsonl | 10-Q Q2 2026 | page:152 | CP-2 asset quality table | Sourced | High | Excludes items the company lists |
| Shareholder ownership percentages | 10-K_2025-12-31_stwd-20251231.htm.jsonl page:3 | 10-K_2025-12-31_stwd-20251231.htm.jsonl | 10-K FY2025 | page:3 | CP-1A ownership row | Untraced | Insufficient | Part III is incorporated by reference; no percentages in the pack, so the CP-1A row correctly records the datapoint as missing |

### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM total revenues 2,007,950 | CP-1 | FY2025 1,844,289; 6M 2026 1,026,124; 6M 2025 862,463 (USD thousands) | FY2025 + 6M 2026 - 6M 2025; recomputed 2,007,950; equals sum of four quarters | Calculated | Matches | High | Earnings base | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| LTM interest expense 1,342,180 | CP-1 | 1,276,987; 673,483; 608,290 | FY2025 + 6M 2026 - 6M 2025; recomputed 1,342,180; equals sum of four quarters | Calculated | Matches | High | Debt service | same |
| LTM net income attributable 227,910 | CP-1 | 411,544; 58,435; 242,069 | Same bridge; recomputed 227,910 | Calculated | Matches | High | Earnings | 10-K FY2025 page:161; 10-Q Q2 2026 page:5 |
| LTM distributable earnings 606,926 | CP-1 | 615,534; 298,777; 307,385 | Same bridge; recomputed 606,926; equals 148,604 + 159,545 + 147,274 + 151,503 | Calculated | Matches | Medium | Earnings (management measure) | Release YE2025 page:9; 10-Q Q2 2026 pages 129 and 130 |
| LTM operating cash flow 1,090,565; dividends paid 699,817; cash interest 1,236,745 | CP-1 | FY2025, 6M 2026 and 6M 2025 cash flow lines | Same bridge; each recomputed to the stated value | Calculated | Matches | High | Cash conversion, payout | 10-K FY2025 pages 163 and 164; 10-Q Q2 2026 pages 8 and 9 |
| Total debt / stockholders’ equity 3.65x (Jun 30, 2026) and 3.25x (Dec 31, 2025) | CP-1, CP-2 | 23,694,124 over 6,498,963; 22,094,237 over 6,795,516 | Sum of three debt lines over STWD equity; recomputed 3.646x and 3.251x | Calculated | Matches | High | Leverage | 10-Q Q2 2026 page:4 |
| Debt excluding securitized financing / equity 2.91x | CP-1 | 18,882,613 over 6,498,963 | Secured plus unsecured over equity; recomputed 2.905x | Calculated | Matches | High | Leverage, recourse view | same |
| GAAP interest cover 1.22x (LTM) and 1.38x (FY2025) | CP-1 | (299,284 + 1,342,180) over 1,342,180; (479,812 + 1,276,987) over 1,276,987 | Pre-tax income plus interest expense over interest expense; recomputed 1.223x and 1.376x | Calculated | Matches | Medium | Coverage; not a covenant ratio | 10-K FY2025 page:160; 10-Q Q2 2026 page:5 |
| Distributable earnings to dividends declared 0.81x per share, 0.84x in dollars | CP-1, CP-2 | 0.78 over 0.96; 298,777 over 357,326 | Ratio; recomputed 0.8125 and 0.8361 | Calculated | Matches | High | Payout | 10-Q Q2 2026 pages 7 and 129 |
| Perimeter ratios 38.8% GAAP and 74.6% ex-VIE | CP-1 | 23,694,124 over 61,046,276; 23,713,780 over 31,772,112 | Debt over total assets on each perimeter; recomputed 38.81% and 74.64% | Calculated | Matches | Medium | Leverage by perimeter; not comparable | 10-Q Q2 2026 page:4; Release Q2 2026 page:7 |
| Unsecured pro forma principal 4,530,750 | CP-1, CP-1A, CP-2 | 4,930,750 less 400,000 repaid, plus 500,000 issued, less 500,000 redeemed | Arithmetic; recomputed 4,530,750 | Calculated | Matches; labelled pro forma | High | Maturity wall | 10-Q Q2 2026 pages 56 and 101 |
| Cash plus approved undrawn capacity 1,766,638 | CP-1 | 367,592 + 1,399,046 | Analyst construct, not the company definition | Assumption-Based | Matches; construct disclosed | Low | Liquidity | 10-Q Q2 2026 pages 3 and 143 |
| Commercial loans above 70% loan-to-stabilized-value 36.8%; allowance share 89.1% | CP-2 | 6,315,793 over 17,144,591; 361,959 over 406,224 | Ratio; recomputed 36.84% and 89.10% | Calculated | Matches | High | Asset quality | 10-Q Q2 2026 page:32 |
| Nonaccrual total 947.3 million dollars (906.9 plus 40.4) | CP-2 | 649.5 less 274.3, plus 93.5, plus 438.2, plus 40.4 | Sum of prose amounts; recomputed 947.3 | Calculated | Matches arithmetic; scope caveat | Medium | Asset quality | 10-Q Q2 2026 page:33 |
| Funding commitments 3,772,708 and 2,938,352 within a year | CP-2 | 2,292,663 + 1,411,425 + 68,620; 1,554,213 + 1,318,174 + 65,965 | Sums; recomputed | Calculated | Matches | High | Liquidity demand | 10-Q Q2 2026 page:148 |
| Four-quarter net inflows 785,067 | CP-2 | 4,937,555 + 126,181 less 4,278,669 | Sum; recomputed 785,067; equals the printed total | Calculated | Matches | Medium | Refinancing; management projection | 10-Q Q2 2026 page:146 |
| Floating share of unsecured notes 78.6% | CP-2 | 3,875,000 over 4,930,750 | Ratio; recomputed 78.59% | Calculated | Matches | High | Interest rate exposure | 10-Q Q2 2026 pages 56 and 151 |
| Non-U.S. share of the lending portfolio 28.6% | CP-1A | 9.1 + 7.6 + 4.4 + 3.7 + 3.1 + 0.7 | Sum; recomputed 28.6 | Calculated | Matches | High | Concentration | 10-Q Q2 2026 page:140 |
| Quoted USD million amounts in CP-2 prose | CP-2 | Thousand-dollar source amounts | Thousands divided by 1,000, one decimal; every quoted amount rechecked | Calculated | One mismatch: unallocated financing amount stated as 9,993.0 but 9,992,934 thousand is 9,992.9 | High | Presentation | 10-Q Q2 2026 page:143 |

### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Nonaccrual loans near 947.3 million dollars (CP-2) | Total is an analyst sum of prose amounts; the December 31, 2025 comparator of 967.7 million dollars may use a different scope, so no trend is stated | Analyst Inference | Asset quality drives the credit view; a mis-scoped total would mislead on direction | Use the stated components in any downstream text; do not state a nonaccrual trend | CP-2 Key findings; report key findings |
| Material | Revolver committed and undrawn with no letters of credit (CP-2) | Letters of credit against the revolver were not found in the pages searched; that is an absence in text | Analyst Inference | Committed liquidity depends on it | Obtain the revolver agreement or a disclosure of drawn letters of credit | CP-2 Liquidity; report liquidity chart |
| Material | Covenant headroom (CP-2) | Levels and definitions not supplied | Insufficient Information | Headroom cannot be monitored | Obtain governing documents | CP-2 Covenants; report credit metrics |
| Material | Liquidity (CP-1, CP-2) | No company-defined liquidity at June 30, 2026; source list missing from the extraction | Weak Lineage | Liquidity is a constructed measure | Check the original HTML; label as an analyst build | CP-1 liquidity chart; CP-2 Liquidity |
| Minor | Unallocated financing amount (CP-2) | Stated as USD 9,993.0 million; the source figure of 9,992,934 thousand is USD 9,992.9 million | Directly Sourced (figure) with presentation error | Not decision critical but a wrong rounding in a committee document | Use USD 9,992.9 million downstream | CP-2 Debt and funding structure |
| Minor | Unsecured note refinancing (CP-2) | Key findings say the registrant refinanced USD 1,100.0 million of notes; it issued USD 1,100.0 million (USD 600.0 million in May 2026 and USD 500.0 million in July 2026) against USD 900.0 million of notes retired | Directly Sourced (amounts) with wording issue | Overstates retired debt by USD 200.0 million if read literally | Say issued, with USD 900.0 million retired | CP-2 Key findings; CP-2 Calculations item 12 is correct |
| Minor | Revolver undrawn history (CP-2) | Liquidity table shows the revolver undrawn amount as Not extracted for March 2026, December 2025 and September 2025, but it was extractable at USD 200.0 million at each date (10-Q Q1 2026 page:126; 10-K FY2025 page:138; 10-Q Q3 2025 page:142) | Directly Sourced | A search before writing Not extracted would have filled it | Fill from the cited pages | CP-2 Liquidity |
| Minor | Committed undrawn facilities (CP-1 chart) | Left as Not supplied for all periods although the revolver is committed and undrawn; CP-2 refines this | Insufficient Information | Chart shows blanks that the evidence can partly fill | Downstream chart should show 200.0 US$m at each period with the revolver basis | CP-1 liquidity chart data |
| Minor | Locators in CP-1 tables (CP-1) | Row-level locators list sources and pages together, not per column | Weak Lineage | Slows cell-level checking | Map columns using the note under each table | CP-1 income statement and balance sheet tables |

### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover FY2025 to Q2 2026; governing debt documents and later filings absent | Missing legal documents leave covenant and structure claims resting on descriptions | Committee cannot rely on headroom or guarantor structure | Obtain documents and later filings |
| Citation completeness | Ready with Remediation | 38 statements traced to located pages with exact strings; row-level locators in CP-1 tables | Coarser locators slow checks but did not hide any figure | Low | Map CP-1 columns to sources |
| Calculation traceability | Committee-Ready | Nineteen calculation items recomputed; eighteen matched exactly and one quoted amount in CP-2 had a rounding error | A rounding error does not change a ratio | Low | Correct the quoted amount downstream |
| Assumption transparency | Ready with Remediation | Liquidity construct, nonaccrual sum, revolver availability and pro forma are labelled but rest on analyst choices | Unlabelled use downstream could pass constructs off as company figures | Restricts liquidity and asset-quality conclusions | Keep labels; obtain missing inputs |
| Markdown and export artifact integrity | Committee-Ready | Each handoff has the six required headings, upstream hashes and its opening view; CP-1 passed the chart selectors on its second attempt | Structure issues would break report assembly; none remain | Low | None |

Overall auditability is the lowest of the five dimensions: Ready with Remediation.

### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence/Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Governing debt documents (indentures, credit agreements, repurchase agreements, management agreement) not supplied | Executed documents | Covenant headroom and structural ranking cannot be verified | CP-2 Covenants, credit view | High impact | Documents from the issuer or filings exhibits |
| CP-5-GAP-002 | No filing after the August 6, 2026 release | Third quarter 2026 report and any later current reports | Later events could change liquidity or leverage | All modules | High impact | Filings dated on or before 2026-11-05 |
| CP-5-GAP-003 | Company-defined liquidity at June 30, 2026 and the lost bullet list of liquidity sources | Original HTML liquidity section | Liquidity is an analyst build | CP-1, CP-2 liquidity | Medium impact | Original filing |
| CP-5-GAP-004 | Nonaccrual comparator scope | Definition of the December 31, 2025 total | Trend cannot be stated | CP-2 asset quality | Medium impact | Prior-period 10-K or loan note |
| CP-5-GAP-005 | Ratings, market quotes and peers | Rating reports and quotes | No external read or relative value | CP-2 | Medium impact | Rating agency and market data |
| CP-5-GAP-006 | Shareholder ownership percentages and related-party exposure total | Proxy statement; related-party loan list | Governance cannot be sized | CP-1A, CP-2 | Medium impact | Proxy statement; filings |
| CP-5-GAP-007 | Extraction fidelity against original HTML | Side-by-side check | Residual extraction risk | All | Low impact | Original filings |
| CP-5-GAP-008 | Confidence score not computed | Script output | Status is a judgment | CP-5 | Low impact | Confidence script |

### T5.1 Handoff register

| Module | Handoff canonical .md / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 (sha256 2dd5f2d188dcfd523c32c5571bb13634e5383866cc3b07a5a7ff8344297fbd4e) | runs/cpos-swarm-20261105-stwd/requests/CP-0/1a183556fb3b3d08ad9d418a8de4c2671479051d3bba1d1427ede62b43357da7/1.response.md / stwd-2026-11-05-credit_snapshot-host | Seven sources, four consumers | High; extraction fidelity not independently reviewed | Six H2 headings and readiness view present | Accepted by CP-OS | All spot-checked quotes found on their pages |
| CP-1 (sha256 4e1540f23d70471fc4b9b2945093c91a4c0f050f9198457596131405cd3f82d1) | runs/cpos-swarm-20261105-stwd/requests/CP-1/3b52b4ab41d6aa83057bc7ce64320fa44b121c16d02b7118f7a8c8d2c0dc1b15/2.response.md / stwd-2026-11-05-credit_snapshot-host | Financial base, chart tables, LTM and leverage bridges | High for filed lines; Medium for release items | Six H2 headings, financial base view, four chart tables and metrics table present | Accepted after one repair | First attempt rejected for missing chart selectors; recomputation here matches |
| CP-1A (sha256 9e0df2f1a6fca390ee0368bc3a7cb1ba3a1c796d23d87e8940a5abeb1b921158) | runs/cpos-swarm-20261105-stwd/requests/CP-1A/79da03b805163b5e800cbda6e79194eb6efe24b6abe2c295f70b8437ebb1dad9/1.response.md / stwd-2026-11-05-credit_snapshot-host | Business, governance, transactions, timeline | High for quotes; Medium for interpretation | Six H2 headings, business and transaction view, two selector tables and prose section present | Accepted first attempt | All quotes verified against cited pages |
| CP-2 (sha256 88bacddd0c1534cdc1e8d252ab513c1dde7b772de5d8fdde696dc47352e73324) | runs/cpos-swarm-20261105-stwd/requests/CP-2/58d575e95e5b130f37d1d74feb32a767b2c4556e8b2991d6210001ee67047627/1.response.md / stwd-2026-11-05-credit_snapshot-host | Credit view, liquidity, covenants, risks | High for filed figures; Medium for interpretation | Six H2 headings, credit view and prose selectors present | Accepted first attempt | Three minor defects found by this trace |

### T5.2 Claim and evidence issues

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Key findings: refinanced USD 1,100.0 million | Sourced; wording overstates retirements | Issued 1,100.0 versus retired 900.0 million dollars | Use issued | None for committee use if read with the calculation |
| Minor | CP-2 | Debt and funding structure: USD 9,993.0 million unallocated | Sourced; rounding error | 9,992,934 thousand is USD 9,992.9 million | Correct to 9,992.9 | None |
| Minor | CP-2 | Liquidity: revolver Not extracted for three dates | Sourced and extractable | Search before Not extracted would have found USD 200.0 million | Fill from cited pages | None |
| Material | CP-2 | Key findings: nonaccrual near USD 947.3 million | Derived from prose | Scope of comparator unclear | Use components; no trend claim | Restricts any trend statement |
| Minor | CP-2 and CP-1A | Credit default swap description | Two descriptions | Infrastructure segment entered the swap (10-Q Q2 2026 page:94) while the market-risk text says it hedges a large commercial loan (10-Q Q2 2026 page:151); notional USD 20.0 million agrees | Keep both descriptions; do not state the hedged loan type | None |

### T5.3 Metric and logic issues

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Leverage uses balance-sheet debt over STWD equity | Differs from covenant definitions that use defined terms, and from the EBITDA-based chart columns, which are Not supplied for a lender | None between modules | Keep the label analyst ratio; do not compare with covenant levels | None |
| Minor | CP-1 | GAAP interest cover includes fair value, foreign currency and consolidated VIE items | Not EBITDA or a covenant ratio | None | Keep disclosed caveat | None |
| Minor | CP-1, CP-2 | Cash plus approved undrawn capacity is an analyst construct | Not the company liquidity definition; year-end release headline of USD 1.4 billion cannot be tied | Release headline versus constructed figure not reconcilable | Label as construct | Restricts liquidity conclusions |
| Minor | CP-1 | Distributable earnings differs from GAAP by design | Company non-GAAP definition | None | Show both, as done | None |
| Minor | CP-2 | Nonaccrual sum | Different classes summed from prose | Comparator scope unstated | As in the flags register | See flags register |

### T5.4 Legal and structural claims

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-2 | Unsecured noteholders rank behind secured lenders on pledged assets | Indentures and facility agreements | Documents not supplied; structure read from filing tables | Obtain documents | Yes |
| Material | CP-2 | Covenant compliance and the 120% unencumbered asset test | Indentures and credit agreements | Levels and definitions not supplied | Obtain documents | Yes |
| Material | CP-2 | Term loans secured on subsidiary equity of USD 8.0 billion | Term loan agreements | Borrower, guarantors and collateral terms not supplied | Obtain documents | Yes |
| Minor | CP-1A | Management agreement fee terms and termination fee | Management agreement | Terms read from 10-K descriptions | Obtain agreement | Yes |
| Minor | CP-1A | Lack of consent rights in some co-lender agreements | Co-lender agreements | Not supplied | Obtain if exposure is sized | Yes |

### T5.5 Market and relative value claims

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | No market or relative-value claim is made; none is permitted in this module | Prices, spreads, ratings and peer data | Context holds no quotes, ratings or peers | Supply quotes and ratings before any relative-value work | Relative value cannot start from this pack |

### T5.6 Data and claim conflicts, version issues

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-0, CP-1, CP-1A, CP-2 | Total assets 61,046,276 thousand (GAAP) versus 31,772,112 thousand (release subtotal before VIE column) | Different perimeters in filing and release; filing controls for GAAP | Label the perimeter on every figure | Leverage and size statements must name the perimeter |
| Minor | CP-1A | January 2026 securitization described as a 600.0 million dollar pool (10-K FY2025 page:271) and as 600.0 million dollars of issued notes (10-Q Q2 2026 page:107); third-party amount agrees | Annual versus quarterly wording | Keep both; do not choose | None for credit conclusions |
| Minor | CP-1, CP-2 | Committed undrawn facilities Not supplied in CP-1 and refined in CP-2 | Later handoff refines an earlier accepted one | Downstream report should use the CP-2 refinement | Liquidity chart basis |
| Minor | CP-2 | Management claim of USD 2.1 billion of corporate debt transactions in the second quarter is not itemised against the filings | Release versus filings | Trace only itemised transactions | None |

### T5.7 Other issues

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-5 | Scoring | The confidence score and band are script-owned and were not computed in this host run; the status below is a judgment | Run the confidence script when available | Committee must treat the status as Restricted |
| Minor | CP-0, CP-5 | Extraction fidelity | All sampled check strings were found on their cited extraction pages; the extraction was not compared with the original HTML | Spot-check against original filings for cited figures | Residual risk of extraction error |

### T5.8 Handoff integrity

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Chart data tables | Committed undrawn facilities blank for all periods | Use the CP-2 refinement downstream | Liquidity chart partly empty |
| Minor | CP-2 | Liquidity table, key findings and debt table | Three presentation defects listed above | Correct downstream | None on credit view |
| Minor | CP-0 to CP-2 | Sha256 lineage | Each handoff lists the sha256 of every upstream handoff it used; no mismatch found | None | None |

### T5.9 Issues register

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-I-001 | Material | CP-2 | Legal | Covenant levels, guarantors, security documents not supplied | Obtain governing documents | Restricts covenant and structure conclusions | Open |
| CP5-I-002 | Material | All | Coverage | No filing after the August 6, 2026 release | Obtain later filings if any exist before the cutoff | Restricts conclusions to June 30, 2026 plus July 2026 events | Open |
| CP5-I-003 | Material | CP-2 | Lineage | Nonaccrual total is a sum of prose amounts with comparator scope unclear | Use components, no trend | Restricts trend statements | Open |
| CP5-I-004 | Material | CP-1, CP-2 | Lineage | Liquidity is an analyst construct; company liquidity and source list missing | Check original HTML; label as construct | Restricts liquidity conclusions | Open |
| CP5-I-005 | Material | CP-2 | Lineage | Revolver availability depends on absence of letters of credit in text | Obtain revolver terms | Qualifies committed liquidity | Open |
| CP5-I-006 | Minor | CP-2 | Calculation | Unallocated financing amount stated as 9,993.0 instead of 9,992.9 million dollars | Use 9,992.9 | None | Corrected here |
| CP5-I-007 | Minor | CP-2 | Wording | Refinanced 1,100.0 million dollars should read issued | Use issued | None | Corrected here |
| CP5-I-008 | Minor | CP-2 | Search | Revolver undrawn amount marked Not extracted but extractable | Fill from cited pages | None | Corrected here |
| CP5-I-009 | Minor | CP-1 | Chart | Committed undrawn facilities blank | Use the CP-2 refinement | None | Corrected here |
| CP5-I-010 | Minor | CP-1 | Locators | Row-level locators | Map columns from table notes | None | Open |
| CP5-I-011 | Minor | CP-1A, CP-2 | Discrepancy | Credit default swap described under two segments | Keep both | None | Open |
| CP5-I-012 | Minor | CP-5 | Scoring | Confidence score not computed in host mode | Run script when available | Status is a judgment | Open |

## Calculations

Recomputation was done independently of the upstream handoffs from the cited source lines; each result is in the calculation register above. The additional arithmetic made in this module is the coverage count: 38 statement rows, of which 36 are Sourced, 1 Calculated and 1 Untraced (36 plus 1 plus 1 equals 38); 19 calculation items, of which 18 matched exactly and 1 had a rounding error in a quoted amount (18 plus 1 equals 19). The corrected amount is 9,992,934 thousand divided by 1,000, which is USD 9,992.9 million, against USD 9,993.0 million stated in the credit view. The issued-versus-retired check is 600,000 plus 500,000 issued, which is 1,100,000, against 400,000 plus 500,000 retired, which is 900,000, a difference of 200,000 thousand.

## Gaps

The gaps ledger above (CP-5-GAP-001 to CP-5-GAP-008) is the complete list. In order of effect on the decision: governing debt documents; filings after August 6, 2026; company-defined liquidity; the nonaccrual comparator scope; ratings and quotes; ownership and related-party exposure; extraction fidelity; and the confidence score. Readiness status: Restricted. No upstream handoff was edited, and the defects found in the credit view are recorded here, not repaired in it.

## Next module

No further module is requested in this run. A reader of the credit view should apply the restrictions above: use the financial base and funding facts, label every perimeter, treat the nonaccrual total and the liquidity construct as analyst builds, correct the three minor presentation items listed, and treat covenant headroom, guarantor structure, ratings and anything after August 6, 2026 as Not supplied until the documents and later filings are obtained.
