## Request

Module CP-0 (source readiness) for Sunoco LP (ticker SUN), as of 2026-11-05, pathway credit_snapshot, reporting currency USD, current period Q3 2026 (quarter ended 2026-09-30), prior period FY2025. Requested downstream consumers: CP-1, CP-1A, CP-2 and CP-5. This module judges only whether the pinned sources can support that work and what stays blocked. It gives no credit conclusion, calculation or reconciliation. The context file holds no deal terms, quotes, ratings, peers or legal documents (legal_documents is "none"); its blank fields are not zero.

Reporting entity: Sunoco LP and its consolidated subsidiaries (the Partnership). The filings are consolidated; no standalone issuer-only statements are supplied. Units are USD millions unless a source says otherwise (Q3 10-Q page:4 heading "Dollars in millions").

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-12-31_sun-20251231.htm.jsonl | 4d533c7220ddbcba5e79429a3e55af6f981f4028bd3240e90c171b5489b87bbb | Annual report, Form 10-K; filed financial statements control (page:1, page:215) | FY2025, year ended December 31, 2025, USD millions |
| 10-Q_2026-03-31_sun-20260331.htm.jsonl | 4e2f1b55ee8eafcd725aa5897bfa24cca76e00e715174c97a0131e050e960f56 | Quarterly report, Form 10-Q, unaudited | Q1 2026, quarter ended March 31, 2026 |
| 10-Q_2026-06-30_sun-20260630.htm.jsonl | b55118b081c6aab25bae8900552db80c2175a7fbe9c987d7af0591769205eba8 | Quarterly report, Form 10-Q, unaudited | Q2 2026 and six months ended June 30, 2026 |
| 10-Q_2026-09-30_sun-20260930.htm.jsonl | 9d81b6ce13f6414e34143a0e003cbfdaa5fb004a754a0331e64ef28cbefb606f | Quarterly report, Form 10-Q, unaudited; signed November 5, 2026 (page:52) | Q3 2026 and nine months ended September 30, 2026 |
| EX-99.1_2026-05-05_ex991sunerq12026.htm.jsonl | b543c996b78993ca218c78bb6345ef94cc7c1414aa2f0dc957df2eabc33099ef | Earnings release, Exhibit 99.1; management claims, supporting only | Q1 2026 |
| EX-99.1_2026-08-04_ex991sunerq22026.htm.jsonl | 99167c2338b2c4908c4d210398b4d6c13f7757d59d0f0344be48d8d23d38d4f9 | Earnings release, Exhibit 99.1; management claims, supporting only | Q2 2026 |
| EX-99.1_2026-11-03_ex991sunocoandsunococorper.htm.jsonl | 9cda190739e5a6207ea6c7ec1f929f6d3b9334edb87da0e79d1dca3af0892d56 | Earnings release, Exhibit 99.1, joint with SunocoCorp LLC; management claims, supporting only | Q3 2026 |

The pack also holds _retrieval.json, a retrieval log. It is not issuer evidence and was not relied on. The context file (sha256 eaf301b6e48e67e6aaccb094631a52cadaa411c1b95b847269bbb6c22d3bdb77) holds the run settings and is not issuer evidence.

### Handoffs relied on

None. CP-0 is the first module and no upstream handoff exists (the request lists an empty handoff set).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases are enough for a source-based credit snapshot of the consolidated Partnership, with bounded gaps. Debt, liquidity, covenant level and subsequent events are all in the filings. | Medium | No indentures, credit agreement, ratings or market data are supplied, and the sources are consolidated only. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The filings cover the latest quarter, the prior year and three interim periods, including the debt table, facility availability and the leverage figure. | Debt and liquidity work can use filed figures rather than management claims. | High |
| Debt terms rest on filing summaries only; no indenture or credit agreement is supplied. | Covenant definitions and baskets cannot be read from executed documents. | Medium |
| The Partnership changed its stated jurisdiction and exchange between the annual report and later quarters, and no source explains the change. | The legal entity perimeter for issuers and guarantors needs care. | Low |
| Management adjusted EBITDA appears in the filings and in the releases with differing treatments. | Earnings metrics must be tied to the filing definition. | Medium |

### Readiness view

The effective source set supports the requested snapshot work with limitations. It is source sufficiency only, not completion of any downstream analysis, and the model input contract is not evaluated (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED). Each consumer is rated READY_WITH_LIMITATIONS. No consumer is CONDITIONAL or BLOCKED, because every source has retained, readable text and the identity of the reporting entity is clear. The strongest contrary evidence is the absence of executed legal documents, ratings and market data, together with a consolidated-only perimeter and unexplained corporate-form changes. These limit how far debt terms and guarantee structure can be verified, but the filings summarise them.

### Source assessment

| Source | Located content and coverage | Entity and perimeter | Limitation |
| --- | --- | --- | --- |
| 10-K FY2025 | Business, risk factors, MD&A, financial statements, debt note and covenant text across 279 of 279 pages (page:1 to page:279). Auditor reports at page:152 and page:215. Debt note at pages 248 to 252; covenant text at page:251; lease note at page:265. | Sunoco LP and consolidated subsidiaries; the Partnership describes itself as "Delaware master limited partnership" (see Findings, jurisdiction). Guarantor information at page:141. | FY2025 year-end only; Parkland Acquisition closed October 31, 2025, so FY2025 includes only two months of Parkland. Not a Q3 2026 source. |
| 10-Q Q1 2026 | Statements at pages 1 to 4, debt note at page:11, liquidity at page:42, guarantor information at pages 42 to 43. | Consolidated Partnership; "Delaware master limited partnership". | Unaudited, condensed notes. |
| 10-Q Q2 2026 | Debt note at page:12, liquidity at page:45, guarantor information at pages 45 to 46. | Consolidated Partnership; "Texas master limited partnership". | Unaudited, condensed notes. |
| 10-Q Q3 2026 | Balance sheet page:3, operations page:4, cash flows pages 5 to 6, debt note pages 13 to 15, segments pages 21 to 22, Adjusted EBITDA reconciliation page:22, liquidity and debt description pages 42 to 46, guarantor information pages 47 to 48. | Consolidated Partnership. Guarantor Issuer Group (Sunoco LP, Sunoco Finance Corp. and NuStar Logistics plus guarantors) summarised at page:47, nine months 2026 only. | Latest source; signed on the cutoff date. Unaudited. Offen purchase accounting not yet determined (page:10). |
| EX-99.1 Q1 2026 | Net income, Adjusted EBITDA, Distributable Cash Flow, segment tables (page:2, page:9, page:12). | Sunoco LP and SunocoCorp LLC joint release. | Management narrative; non-GAAP measures. |
| EX-99.1 Q2 2026 | Same structure; raises 2026 guidance (page:2). | Joint release. | Management narrative; guidance is a forward claim. |
| EX-99.1 Q3 2026 | Same structure; liquidity and leverage paragraph and 2026 guidance (page:2). | Joint release. | Management narrative; headline and body Adjusted EBITDA differ in treatment of one-time transaction expenses (see Gaps). |

### Coverage of required evidence

| Evidence needed | Located in | Status |
| --- | --- | --- |
| Quarterly and annual income statement, balance sheet, cash flow | 10-Q Q3 pages 3 to 6; 10-K pages 215 to 221 | Retained |
| Segment Adjusted EBITDA and net income reconciliation | 10-Q Q3 pages 21 to 22; releases page:9 and page:12 | Retained |
| Debt by instrument with rates, maturities and carrying amounts | 10-Q Q3 page:13; 10-K page:139 and pages 248 to 249 | Retained as filing summary |
| Facility size, drawn amount, letters of credit, availability | 10-Q Q3 page:15 and page:46 | Retained |
| Maintenance covenants (level and reported ratio) | 10-K page:251 for the level and 10-Q Q3 page:15 for the reported ratio | Retained as filing summary, no executed agreement |
| Cash interest paid | 10-Q Q3 page:11 | Retained |
| Guarantor and issuer structure | 10-Q Q3 pages 46 to 48; 10-K page:141 and page:250 | Retained as filing summary |
| Subsequent events and acquisitions | 10-Q Q3 page:10 (Offen), page:15 (receivables facility termination), page:44 (distribution) | Retained |
| Lease obligations | 10-K page:265; 10-Q Q3 balance sheet page:3 | Retained at balance sheet and note level |
| Ratings, market prices, peers | none | Not supplied |

### Version relationships

The three 10-Qs and the 10-K are separate active sources for separate periods; none supersedes the others. The Q3 10-Q repeats the December 31, 2025 comparatives, and its guarantor table says the 2025 balances were "adjusted from previously reported amounts" (page:47), so the 10-K guarantor figures and the Q3 comparatives can differ. The Q2 and Q3 releases are separate Exhibit 99.1 documents, not amendments. No draft, unsigned or superseded document is in the pack.

## Calculations

None. CP-0 performs no normalisation, calculation or reconciliation. Figures quoted in the tables above are located, not recomputed.

## Gaps

| Gap | Evidence | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| No executed indentures, credit agreement or amendments | Legal documents are "none" in the context; debt terms appear only in note text, for example "The Credit Facility also requires the Partnership to maintain an Interest Coverage Ratio" (10-K page:251) | Material | CP-1A, CP-2, CP-5 | Obtain the credit agreement and note indentures; until then cite filing summaries |
| Covenant definitions and headroom not in executed form; the reported Net Leverage Ratio (Q3 10-Q page:15) uses a credit-agreement definition that differs from any ratio computed from statements | "The Partnership’s net leverage ratio was 3.5 to 1.00 at September 30, 2026." (page:15) | Material | CP-2, CP-5 | Label any computed leverage as a different definition; use the reported ratio only as management-reported |
| Jurisdiction and exchange changed with no explanation: 10-K and Q1 10-Q say Delaware; Q2 and Q3 10-Q say Texas; the Q1 and Q2 releases show NYSE and the Q3 release shows TXSE | "We are a Texas master limited partnership." (Q3 10-Q page:7) versus "We are a Delaware master limited partnership." (Q1 10-Q) | Moderate | CP-1, CP-5 | Name the filing-stated entity at each date; treat the cause as unresolved |
| Consolidated perimeter only; guarantor summary covers nine months 2026 with 2025 balances restated | "adjusted from previously reported amounts" (Q3 10-Q page:47) | Moderate | CP-1, CP-2 | Use consolidated figures for the Partnership; show guarantor data as context |
| Adjusted EBITDA is a management non-GAAP measure with differing treatment of one-time transaction expenses between the release headline and body | Release Q3 page:2 headline "excluding one-time transaction-related expenses" and body "Adjusted EBITDA for the third quarter of 2026 was" a lower figure | Moderate | CP-1, CP-2 | Use the 10-Q reconciliation (page:22) as the controlling definition; report the release figure as a management claim |
| Ratings, market data, peers and management bridge not supplied | Context ratings, quotes and peers are empty | Moderate | CP-2, CP-5 | Do not infer; state Not supplied |
| Pre-acquisition comparatives: Parkland, TanQuid, Delta and Offen change the perimeter between periods; Offen closed after quarter end and its purchase accounting is open | "Management ... is in the process of determining the fair value of assets and liabilities" (Q3 10-Q page:10) | Moderate | CP-1, CP-2 | Flag period comparability; no pro forma statements supplied |
| Text extraction only; no image, chart or table-image inspection | Sources are visible-text extracts; successful extraction is not a fidelity review | Minor | All | Open the cited page before relying on a table |
| Releases are management claims and cannot override filings | Method rule on authority | Minor | All | Prefer the 10-Q and 10-K where both report a figure |

## Next module

Proceed to CP-1, then CP-1A, CP-2 and CP-5 in the order CP-OS sequences them. Carry forward: use the 10-Q for Q3 2026 and the 10-K for FY2025; label management-reported ratios as such; name the filing-stated entity and its jurisdiction; treat guarantor and perimeter points as unresolved; and state Not supplied for legal documents, ratings and market data. The next evidence action is to obtain the credit agreement and indentures if covenant headroom or guarantee analysis is to be completed.
