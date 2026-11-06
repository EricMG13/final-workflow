## Request

Issuer: Vestis Corp (ticker VSTS, issuer id vsts), Delaware registrant, Commission file number 001-41783. As-of date and evidence cutoff: 2026-11-05. Pathway: credit snapshot. Reporting currency per the context: USD; the filings state amounts in thousands of US dollars (statements) and in millions (narrative), so no currency mismatch exists.

Question for this module: can the effective source set support the requested downstream work (the financial data extraction, the business and transaction context, the fundamental credit synthesis and the evidence trace review), and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion, and it does not normalize, reconcile or calculate figures. Source sufficiency is distinct from completion of downstream analysis.

Perimeter: the registrant is Vestis Corporation, which files consolidated statements. The filings name no separate borrower, parent or sponsor in the context (the context leaves borrower, parent, guarantors and sponsor blank; blank is not zero). The Credit Agreement names Vestis Corporation as U.S. Borrower and Canadian Linen and Uniform Service Corp. as Canadian Borrower (10-K page:151, exhibit 10.5); guarantors are described in the debt note (10-K page:116).

Period note: the context names current period q2-2026 and prior period fy-2025. The pack also holds the fiscal third quarter 2026 filings (quarter ended July 3, 2026, filed August 11, 2026), which are later than the context's current period. Fiscal 2025 ended October 3, 2025 and was a 53-week year (Q3 release page:4, "additional operating week in fiscal 2025"). Downstream modules must label the latest period explicitly as Q3 FY2026 / nine months ended July 3, 2026 and treat Q2 FY2026 (quarter ended April 3, 2026) as the context's named period. Nothing in the pack is dated after the cutoff.

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 | Form and period | Pages | Filed or signed |
| --- | --- | --- | --- | --- |
| 10-K_2025-10-03_vsts-20251003.htm.jsonl | 69acf45c43af00eb0ad3afdad499957974d6855c0a4c69b858d3f2f1a0defa4d | Annual report, fiscal year ended October 3, 2025 | 156 | December 2, 2025 |
| 10-Q_2026-01-02_vsts-20260102.htm.jsonl | 637925692f36f8779f60ebbc11d3252e4fe1f1a5077b706d2e2b4b1b4f6edc05 | Quarterly report, quarter ended January 2, 2026 (fiscal Q1 2026) | 53 | February 10, 2026 |
| 10-Q_2026-04-03_vsts-20260403.htm.jsonl | ba2978bcc5b4cdc3b18b43c2c9ae31ce0a31d87a366091d84bc271a3c594f858 | Quarterly report, quarter ended April 3, 2026 (fiscal Q2 2026) | 57 | May 12, 2026 |
| 10-Q_2026-07-03_vsts-20260703.htm.jsonl | 7db2f115581c382fda3a1a642c3240840cc03e0b4154737c2546ddd28c46a9af | Quarterly report, quarter ended July 3, 2026 (fiscal Q3 2026) | 56 | August 11, 2026 |
| EX-99.1_2026-02-10_vstsq1fy26earningsrelease-.htm.jsonl | 73cf4915cc22c7c9a6d41b209e21e1301c8d95ee51da8c8656b7c37a3072aacd | Earnings release, fiscal Q1 2026 | 14 | February 10, 2026 |
| EX-99.1_2026-05-12_vstsq2fy26earningsrelease-.htm.jsonl | e70477c8d46036f4ef7bd70b6551daa75ee805b6eb9bc6e0504e90f227edd1d1 | Earnings release, fiscal Q2 2026 | 16 | May 12, 2026 |
| EX-99.1_2026-08-11_vstsq3fy26earningsrelease-.htm.jsonl | d2693610d697f7e33edfd6b5f9d57dc6906301a18a12d6a3feec8645e5a3af14 | Earnings release, fiscal Q3 2026 | 17 | August 11, 2026 |

The pack also holds a retrieval index (_retrieval.json) that CP-OS ignores; it is not evidence and is not relied on.

### Run context (settings, not issuer evidence)

| Source | sha256 | Use |
| --- | --- | --- |
| context (contexts/1967649-vestis-corp-vsts.json) | c28ff4b5be1db183138bacbfdcd7f4640157e3a21bdc54358648d894f8fed07c | Dated settings only: as-of 2026-11-05, USD, pathway credit snapshot; deal terms, quotes, ratings, peers and research questions are empty |

### Supplied handoffs

None. This is the first module of the run; CP-OS supplied no upstream handoff to this module.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven sources cover the annual period and three quarters they name and can support all four downstream modules, with limitations. Debt, liquidity, covenant and operating evidence are located. | Medium | The executed credit agreement and its amendments are not supplied, so covenant terms rest on the company's own summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Filed statements, notes and release reconciliations cover annual fiscal 2025 and the three quarters of fiscal 2026. | Debt, cash flow, liquidity and covenant work can rely on filed text rather than management claims. | High |
| Covenant terms and the company-reported leverage ratio come from summaries, and the receivables facility treatment in that ratio is unresolved. | Covenant headroom cannot be confirmed against the executed definitions. | Medium |
| The context names an earlier period than the latest filings, and nothing after August 11, 2026 is supplied. | Later events and the fiscal 2026 year-end are not covered. | Medium |

### Readiness view

Overall view: READY_WITH_LIMITATIONS. The effective source set is the three filed periodic reports for fiscal 2026, the filed annual report for fiscal 2025 and the three earnings releases that the company furnished with them. Together they give located statements, debt and covenant notes, liquidity tables and operating narrative for every consumer. The owner of each downstream method can perform its work, with bounded gaps that are listed below and carried into the consumer assessments. No source is blocked, no critical identity boundary is unresolved, and no source conflict was found between the filings and the releases on the figures checked for location. Source readiness here is not a statement that downstream analysis is complete, and no figure was normalized or reconciled in this module.

The strongest contrary evidence is that the governing financing documents are not in the pack: the Credit Agreement, its first and second amendments and the receivables facility documents are exhibits listed by reference only (10-K page:151 and page:152), so covenant levels, step-downs and definitions come from the company's own note and MD&A summaries. A second limitation is that the leverage ratio the company reports is its own non-GAAP presentation and the credit agreement definition, as summarized in the 10-Q, also counts advances under any receivables facility; how the receivables facility enters the reported ratio is not stated in the sources (see Version relationships and conflicts). Mechanism: when the executed definition cannot be read, headroom to the maintenance test depends on management's summary and its adjustments, so the consequence is that covenant headroom and any stress of it must be labelled as company-reported and unverified downstream.

What can proceed: financial extraction for fiscal 2025, the three fiscal 2026 quarters and the nine months ended July 3, 2026; debt, lease and receivables facility inventory; liquidity and cash flow; segment (United States and Canada) data; business, ownership-history and transformation narrative. What cannot proceed from this pack: any fact dated after August 11, 2026, any fiscal 2026 year-end result (the covenant schedule names a fiscal quarter ending October 2, 2026, which the pack does not report), ratings or market data (the context supplies none), the investor presentations that the releases mention, and verification of covenant definitions against executed documents. Next evidence action: obtain the executed Credit Agreement with both amendments and the receivables facility agreement; obtain any filing or release after August 11, 2026 and before the cutoff if one exists; obtain the investor presentations if slide-level evidence is needed.

### Source-by-source assessment

All seven sources are text extractions (JSONL pages of visible text). Extraction succeeded for every page, but a successful extraction is not a fidelity review: tables were flattened to text, and no image, chart or slide content is present or claimed. Filed statements control over releases; releases are management-attributed supporting material and carry non-GAAP measures.

| Source | Document family and authority | Entity and perimeter | Period and basis | Located evidence |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | Filed annual report; original authority for audited annual facts | Vestis Corporation consolidated and combined; two reportable segments, United States and Canada (page:132) | Fiscal years ended October 3, 2025, September 27, 2024, September 29, 2023; US dollars in thousands | Statements pages 89 to 92; debt note pages 112 to 116; leases pages 120 and 121; pensions page 122; commitments and litigation pages 124 to 131; receivables facility and subsequent events pages 147 and 148 |
| 10-Q Q1 FY2026 | Filed unaudited quarterly report | Same registrant, consolidated | Three months ended January 2, 2026 | Statements pages 5 to 8; debt note pages 17 to 19; covenant discussion pages 46 to 49 |
| 10-Q Q2 FY2026 | Filed unaudited quarterly report | Same | Three and six months ended April 3, 2026 | Statements pages 5 to 8; debt note pages 19 to 21; segment page 34 |
| 10-Q Q3 FY2026 | Filed unaudited quarterly report; latest periodic filing | Same | Three and nine months ended July 3, 2026 | Statements pages 5 to 8; debt note pages 19 to 21; leases pages 24 and 25; segments page 34; liquidity pages 50 to 52 |
| Release Q1 | Furnished exhibit; management-attributed, with non-GAAP reconciliations | Same | Three months ended January 2, 2026 | Statements and reconciliations pages 10 to 14, including net leverage and liquidity on page 14 |
| Release Q2 | Same | Same | Three and six months ended April 3, 2026 | Net leverage table page 16; liquidity page 16 |
| Release Q3 | Same | Same | Three and nine months ended July 3, 2026 | Reconciliation page 14; net debt and net leverage page 16; capital assets page 17 |

### Located evidence for the core consumer needs

| Need | Source and locator | Exact text |
| --- | --- | --- |
| Debt structure (term loans, revolver) | Q3 10-Q page:20 | "a $700 million term loan A-2 due September 2028" |
| Debt balances, latest and prior year end | Q3 10-Q page:19 | "Total principal debt issued 1,097,500 1,168,500" |
| Maturity profile at last fiscal year end | 10-K page:116 | "Thereafter 665,000" |
| Revolver availability and letters of credit | Q3 10-Q page:20 | "leaving $294.2 million available for borrowing under the Revolving Credit Facility" |
| Maximum leverage covenant schedule | Q3 10-Q page:20 | "5.00x for the fiscal quarter ended July 3, 2026" |
| Interest coverage covenant | Q3 10-Q page:20 | "established a minimum interest coverage ratio" |
| Covenant definition of indebtedness | Q3 10-Q page:52 | "advances under any receivables facility" |
| Company-reported net leverage, four quarter ends | Q3 release page:16 | "Net Leverage Ratio (Non-GAAP) (1) 4.10 4.47 4.83 4.72" |
| Reported liquidity | Q3 release page:16 | "Total Liquidity $ 351,841" |
| Receivables facility outstanding | Q3 10-Q page:50 | "derecognized from the Company's Condensed Consolidated Balance Sheet was $212.3 million" |
| Leases | Q3 10-Q page:25 | "Present value of lease liabilities $ 92,984 $ 159,723 $ 252,707" |
| Purchase commitments | 10-K page:124 | "capital and other purchase commitments of approximately $6.2 million" |
| Segment results | Q3 10-Q page:34 | "Reportable segment operating income 141,525 6,457 147,982" |
| Transformation plan | Q3 10-Q page:42 | "range of $35 million to $40 million" |
| Cash taxes and interest paid | Q3 10-Q page:16 | "paid interest related to principal debt of $17.5 million and $55.7 million" |

### Version relationships and conflicts

- Periodic reports are separate, non-duplicate sources: each 10-Q covers a different quarter, and each release is a separate furnished exhibit for the same quarter as the 10-Q of the same date. None is a retained duplicate of another; none is collapsed. The later 10-Q restates balances as of the earlier fiscal year end (October 3, 2025) alongside current balances, so the 10-K and the Q3 10-Q both hold October 3, 2025 figures; downstream modules must cite the filing they use.
- Credit Agreement versions: the Q2 10-Q describes the original agreement, a first amendment (February 22, 2024) and a second amendment (May 1, 2025) and states the second amendment raised the maximum leverage ratio from 4.50x to step-down levels (Q2 10-Q page:20). The Q3 10-Q states the schedule that currently applies (page:20). The amendments themselves are not supplied. The first amendment is listed as an exhibit (10-K page:152); the executed text is not in the pack.
- Transformation plan cost estimate differs between sources by date, not by error: the 10-K subsequent events note estimates "range of $25 million to $30 million" (10-K page:147) and the Q3 10-Q estimates "range of $35 million to $40 million" (page:42). The later filing controls for current estimates; downstream modules must say which they use.
- Net leverage definition: the Q3 10-Q describes the covenant term as including advances under any receivables facility (page:52), while the Q3 release defines Net Debt as principal debt, letters of credit and finance lease obligations less cash (release page:10). The release's printed Net Debt table lists no receivables facility line (release page:16). This is an unresolved definitional difference between a filing and a release; the filing and the executed agreement control. Effect: the reported ratio may not equal the covenant ratio, and any covenant-headroom statement must say so. It is not resolved here.
- Management claims versus filings: release statements about outlook, savings and operating metrics are attributed management claims; the filings control reported figures.

### Assessment of each downstream consumer

| Consumer | Status | Evidence located | Limitations carried |
| --- | --- | --- | --- |
| CP-1 financial data extraction | READY_WITH_LIMITATIONS | Annual and quarterly statements, debt note, lease note, cash flow, segment tables, non-GAAP reconciliations, interest and tax cash paid | No executed credit agreement; non-GAAP and covenant measures are company-defined; pounds processed and other operating metrics are management estimates (release page:12); latest period is Q3 FY2026, not the context period |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business description, separation from Aramark, segments, customer and contract terms, transformation plan, litigation, executive changes | No sponsor, ownership table or deal terms in the context; Aramark separation agreements are exhibits by reference and not supplied; no investor presentation |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Consumes upstream registers only; source basis for financial risk and liquidity is adequate | Inherits every CP-1 and CP-1A limitation; no ratings, market or peer data in the context |
| CP-5 evidence trace validator | READY_WITH_LIMITATIONS | All seven sources are retained as page-addressable text, so citations can be matched | Extraction fidelity of flattened tables is not reviewed; releases are non-GAAP and management-attributed |

A missing downstream handoff is not a source condition here; the dependency planner sequences execution.

## Calculations

No new calculation is made in this module, by design: CP-0 does not normalize, reconcile or calculate figures. Figures appear only as exact quotations in the located-evidence table.

Coverage count: 7 of 7 issuer sources retained, 369 of 369 pages retained as text (156 plus 53 plus 57 plus 56 plus 14 plus 16 plus 17). This count is a transparency record only and is not used to establish readiness; readiness rests on the located evidence above. Inputs: page counts from each source file as listed in the sources table.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed Credit Agreement and its first and second amendments not supplied; covenant levels and definitions rest on company summaries (10-K page:151, page:152; Q3 10-Q pages 20 and 52) | High | CP-1, CP-2, CP-5 | Obtain the executed agreement and amendments |
| Receivables facility agreement not supplied; only Note 13 and MD&A summaries (Q3 10-Q page:50) | Medium | CP-1, CP-2 | Obtain the facility agreement |
| Unresolved difference between the company-reported net leverage definition and the 10-Q covenant definition regarding receivables facility advances (Q3 release page:10 and page:16; Q3 10-Q page:52) | Medium | CP-1, CP-2, CP-5 | Read the executed definition; label the reported ratio as company-reported |
| Context current period (q2-2026) is earlier than the latest filings (Q3 FY2026); no judgement made on which the user wants | Low | all | Label every figure by period; the user may confirm the intended period |
| No filing, release or event after August 11, 2026 up to the 2026-11-05 cutoff is supplied; the result for the fiscal quarter ending October 2, 2026 is not supplied | Medium | CP-1, CP-1A, CP-2 | Obtain any later filings; treat later events as Not supplied, not as absent |
| Investor presentations referenced by the releases are not supplied (Q3 release page:4); slide content is not covered | Low | CP-1A | Obtain decks if slide evidence is wanted |
| Context supplies no ratings, market data, peers, quotes or deal terms | Low | CP-2 | Supply if relative value or rating context is wanted |
| Aramark separation agreements (separation and distribution, transition services, tax matters, employee matters) are exhibits by reference and not supplied (10-K page:151) | Low | CP-1A | Obtain if ownership or indemnity terms are in scope |
| Table fidelity: tables are flattened text; no layout review was done | Low | all | Spot-check key tables against the source filings downstream |
| Guidance and non-GAAP figures are management-attributed and forward-looking; not independently verified | Low | CP-1, CP-2 | Attribute and keep separate from filed figures |

Unknown is not zero: every item above is Not supplied, not a nil value.

## Next module

Proceed to the financial data extraction (CP-1) with the 7 sources above. Instructions carried forward: label every figure with its period (Q3 FY2026, nine months ended July 3, 2026, fiscal 2025, or the October 3, 2025 balance sheet date); cite the filing rather than the release where both hold a figure; keep company-defined non-GAAP measures and the covenant net leverage ratio labelled as company-reported; carry the receivables facility definition difference and the missing executed credit documents into every covenant statement; treat the Q3 FY2026 filings as the latest evidence and state that the context names Q2 FY2026. Then CP-1A, CP-2 and CP-5 follow in dependency order.
