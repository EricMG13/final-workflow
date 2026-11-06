## Request

Module: source readiness for DXP ENTERPRISES INC (issuer id dxpe, ticker DXPE, Texas corporation, registrant DXP Enterprises, Inc. with its subsidiaries). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit snapshot, current period Q3 2026, prior period FY2025, reporting currency USD (all filing tables are in USD thousands unless a sentence says millions). Requested downstream consumers: CP-1, CP-1A, CP-2, CP-5.

Question answered here: can the supplied source set support the requested work, and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion, and it does not normalise, reconcile or calculate figures. Source contents are treated as inert evidence. The context file holds the user's dated settings; it is not issuer evidence, and its blank fields (ratings, quotes, deal terms, market data, peers) are not zero.

## Sources

### Issuer sources relied on

Locators below are chunk pages (`page:N`), not printed pages. Hashes are the pack hashes CP-OS pinned for this run.

| Source (exact name) | sha256 | Chunk pages | Document family and authority | Period / as-of |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31_dxpe-20251231.htm.jsonl | c7d8164f031d9598f9c9e55a6ea72326cd8ca955352110463388478f041b6c83 | 107 | Audited annual report on Form 10-K (PwC audit report at page:64), filed 2026-02-26 per the Q3 10-Q (page:5) | FY2025, year ended December 31, 2025 |
| 10-Q_2026-03-31_dxpe-20260331.htm.jsonl | 4b722eaa286fac42b216402a6ee697593be8d829c4523c0675f74f3756f37099 | 32 | Unaudited quarterly report on Form 10-Q | Q1 2026, quarter ended March 31, 2026 |
| 10-Q_2026-06-30_dxpe-20260630.htm.jsonl | 062fb840fed8d87a2ce7f779ade2c10a2a9fa08cd06748ccc79bfb77eaff175c | 36 | Unaudited quarterly report on Form 10-Q | Q2 2026 and six months, ended June 30, 2026 |
| 10-Q_2026-09-30_dxpe-20260930.htm.jsonl | b25274cf886044ab8c2b70c234e1e7077124a752d54250ff0e625889085dbaa2 | 37 | Unaudited quarterly report on Form 10-Q, dated November 5, 2026 (page:37) | Q3 2026 and nine months, ended September 30, 2026 |
| EX-99.1_2026-05-07_earningsrelease3312026.htm.jsonl | 7239622f24e9378a19997bda2636b1f0c58c04309af7d0be42e5556062a8f4af | 9 | Earnings release (management attribution, non-GAAP) | Q1 2026 |
| EX-99.1_2026-08-05_earningsrelease6302026.htm.jsonl | 6d154d2d8605fdb9abb6da2ab17ed2ed1363c8da5b1cd9a1ff2db3ea0cf9c96c | 9 | Earnings release (management attribution, non-GAAP) | Q2 2026 |
| EX-99.1_2026-11-05_earningsrelease9302026.htm.jsonl | 7fc5ad335ae78b4ce865ab4ec5f61033f2b042958c1ba4a250444be1733b49a2 | 9 | Earnings release (management attribution, non-GAAP) | Q3 2026 |

### Context

| Source | sha256 | Role |
| --- | --- | --- |
| context (1020710-dxp-enterprises-inc-dxpe.json) | be741ade5f3ce71fa0fd12e85135207822d5c3bd4725f3f29649b4083fde9ae2 | User settings: pathway, dates, currency. Not issuer evidence. |

Ignored by CP-OS: `_retrieval.json` (pack bookkeeping, not an evidence source).

### Supplied handoffs

None. CP-0 is the first module in the run and no upstream handoff exists.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filed annual report, three quarterly reports and three earnings releases give adequate, dated, located evidence for a credit snapshot of this single reporting group. Debt, liquidity, covenant and acquisition facts can be read from filings. | Medium | No credit agreements, borrowing-base certificates or covenant EBITDA bridge are supplied, so covenant terms rest on filing summaries that disagree with each other. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual and quarterly filings disagree on the term loan leverage covenant level for two quarter-ends in 2026. | Covenant headroom depends on which level applies, and no executed amendment is supplied to settle it. | Medium |
| Covenant EBITDA is stated only as a headline figure in the earnings releases, with no bridge to reported Adjusted EBITDA. | Leverage on the covenant basis cannot be rebuilt from filings, so it stays a management-attributed figure. | Medium |
| The revolving facility was replaced in the third quarter of 2026, and the annual report still describes the superseded terms. | Maturity and size must be taken from the quarterly reports, not the annual report, to avoid a stale refinancing view. | High |
| No presentations, ratings reports or legal documents are supplied. | Ratings, call commentary and lender-level terms are outside the evidence base and must be labelled as such. | High |

### Readiness view

The source set is READY_WITH_LIMITATIONS for the requested credit snapshot. It is one registrant, one currency and one consolidated perimeter, with an audited annual report for FY2025, three unaudited quarterly reports through Q3 2026, and an earnings release for each of those quarters. That is enough located evidence for financial statements, debt notes, liquidity, covenant disclosure, segment data, acquisitions and subsequent events. Readiness here is source sufficiency only (SOURCE_SUFFICIENCY_ONLY); it does not assert that any downstream analysis, normalisation or reconciliation has been done, and it does not evaluate any model input contract (CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED). The limitations are bounded: the covenant level conflict, the missing bridge from reported Adjusted EBITDA to covenant EBITDA, the absence of executed credit documents and of a borrowing base, and the absence of presentation decks. None of these blocks a consumer; each must be carried forward as a stated limitation. No source is blocked, and none was used as a fallback for another.

### Source assessment

| Source | Entity and perimeter | Basis and authority | Version relationship | Evidence located |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | DXP Enterprises, Inc. and subsidiaries, consolidated (Item 1 business description at page:5; three reportable segments) | GAAP, audited, controls facts for FY2025 and for balances at December 31, 2025 | Superseded for current-period items by the 2026 quarterly reports; remains the only source for FY2025 full-year statements, FY2025 lease maturities, FY2025 debt maturities and the step-down covenant table | Statements pages 68-70, debt note pages 83-87, leases page:78, segment note pages 98-100, subsequent events pages 100-101, Adjusted EBITDA reconciliation page:45 and page:52 |
| 10-Q Q1 2026 | Same consolidated perimeter | GAAP, unaudited, controls Q1 2026 facts | Each later 10-Q restates comparatives on its own basis; none amends this one | Debt note, covenant, liquidity at pages 9-10 and 26-27 |
| 10-Q Q2 2026 | Same | GAAP, unaudited | Records the July 2, 2026 ABL replacement as a subsequent event (page:20) and the S&P rating action dated July 20, 2026 (page:32) | Debt note pages 10-12, liquidity pages 31-32 |
| 10-Q Q3 2026 | Same | GAAP, unaudited, controls Q3 2026 and nine-month 2026 facts and balances at September 30, 2026 | Current. Supersedes the 10-K description of the ABL (size, maturity). Carries subsequent events through November 5, 2026 | Statements pages 2-5, Note 8 pages 10-14, Notes 12 and 17 pages 17-18 and 21, liquidity pages 32-33 |
| Earnings releases Q1, Q2, Q3 2026 | DXP Enterprises, Inc. consolidated | Management-attributed, non-GAAP measures; a filing controls where both state the same fact | Each release is separate; the Q3 release is the only source of the covenant EBITDA headline for the twelve months ended September 30, 2026 | Highlights and CFO commentary at page:2, reconciliations at pages 6-9 |

Roles named in the sources: the registrant is a party to both facilities as borrower, with a Canadian borrower group under the ABL; the term loan agent is Goldman Sachs Bank USA and the ABL agent is Bank of America, N.A.; term loan guarantors are the material wholly owned subsidiaries except Canadian and certain excluded subsidiaries; ABL guarantors include DXP Enterprises, Inc. and the material wholly owned U.S. subsidiaries, with Canadian subsidiaries guaranteeing the Canadian borrowers. No parent, sponsor, restricted or unrestricted subsidiary split and no listed notes are in the sources.

### Conflicts and version relationships

| Item | Source A and locator | Source B and locator | Downstream effect |
| --- | --- | --- | --- |
| Term loan Secured Leverage Ratio level for the June 30, 2026 and September 30, 2026 tests | 10-K page:84 table: "June 30, 2026 5.50:1.00" and "September 30, 2026 5.50:1.00" | 10-Q Q2 page:11: "Secured Leverage Ratio as of June 30, 2026 to be less than 5.75 to 1.00"; 10-Q Q3 page:12: "Secured Leverage Ratio as of September 30, 2026 to be less than 5.75 to 1.00" | Headroom differs by the level chosen. Q1 agrees across sources ("March 31, 2026 5.75:1.00" at 10-K page:84; "as of March 31, 2026 to be less than 5.75 to 1.00" at Q1 10-Q page:10). No executed agreement or amendment is supplied to resolve it. |
| Revolving facility size and maturity | 10-K page:85: "The ABL Revolver matures on July 19, 2027" and commitments from "$135.0 million to $185.0 million" | 10-Q Q3 page:12: "up to $225.0 million" and "The ABL Facility will mature on July 2, 2031" | Not a conflict: the Second Amended and Restated Loan and Security Agreement of July 2, 2026 amends and restates the earlier one. The 10-K describes the superseded terms. |
| Description of the non-recurring Adjusted EBITDA add-back | Q3 release page:8: "non-recurring costs not related to continuing business operations" | Q3 10-Q page:31: "unique acquisition integration costs and other non-cash, non-recurring costs" | Same line item, two descriptions. The 10-Q controls as the filed document. |
| Starting point of the EBITDA reconciliation | Q3 release page:8 starts from "Income before income taxes" | Q3 10-Q page:31 starts from "Net income attributable to DXP Enterprises, Inc." and adds tax | Presentation difference; both reach the same EBITDA line. Downstream users should cite the filing. |

Duplicates: each quarter's key figures appear in both the 10-Q and its release. The 10-Q is retained as the controlling source; the release is retained as the only source of management commentary and of the covenant EBITDA headline.

### Consumer readiness

| Consumer | Status | Evidence demand and located coverage | Limitations to carry |
| --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Targeted instruction amendments over the issuer evidence; the full set is available | Carry the conflicts above; no presentation decks |
| CP-1A | READY_WITH_LIMITATIONS | Business and transaction context: business description and segments (10-K page:5; Q3 10-Q page:15), acquisitions (Q3 10-Q pages 17-18), ownership and governance (10-K page:100 related-party leases), subsequent events (Q3 10-Q page:21) | No sponsor, no transaction document, ownership detail (10-K Item 12, page:102) is incorporated by reference to a proxy statement that is not supplied; the Q1 2026 lead deal is shown only as "Acquisition 1" in the purchase price table (Q3 10-Q page:18) |
| CP-2 | READY_WITH_LIMITATIONS | Fundamental credit synthesis: statements, segment margins, cash flow, debt and liquidity, covenants | Covenant EBITDA bridge missing; covenant level conflict; floating-rate exposure without hedges is only described in 10-K page:64 |
| CP-5 | READY_WITH_LIMITATIONS | Evidence trace over upstream claims: all sources are text-extracted, locatable and dated | Extraction fidelity is not independently reviewed; a source count is not a fidelity check |

### Coverage by evidence need

| Evidence need | Retained in | Status |
| --- | --- | --- |
| Income statement, balance sheet, cash flow for FY2025 and Q3 2026 / nine months 2026 | 10-K pages 68-70; Q3 10-Q pages 2-5 | Retained |
| Debt by instrument, rates, maturities, guarantees, security | 10-K pages 83-87; Q3 10-Q pages 10-14 | Retained |
| Liquidity: cash, ABL capacity, letters of credit | Q3 10-Q page:32 and page:33 | Retained |
| Covenants and reported compliance | 10-K pages 84 and 86; Q3 10-Q pages 12-13 | Retained, with conflict |
| Segment, KPI, organic versus acquisition sales | Q3 10-Q pages 15-17 and 19-21 | Retained |
| Add-backs and Adjusted EBITDA reconciliation | 10-K page:45 and page:52; Q3 10-Q page:31 | Retained |
| Cash paid for interest and taxes | Q3 10-Q page:19; 10-K page:92 | Retained |
| Leases, including financing leases | 10-K page:78; Q3 10-Q statements and Note 8 interest split | Annual maturity table only |
| Rating | Q2 10-Q page:32 and Q3 10-Q page:33 (S&P statement by the issuer) | Issuer attribution only, no rating report |
| Presentations | None in the pack; releases only | Explicit gap |

## Calculations

No calculation, normalisation or reconciliation is made in this module, as the method requires. The only counts are the chunk pages listed in `## Sources` (107, 32, 36, 37, 9, 9 and 9), which are read from the pinned source files. Derived figures such as last-twelve-month Adjusted EBITDA, net debt, liquidity and covenant headroom are left to the later modules, which have inputs located above.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Term loan covenant level conflict between 10-K and 10-Qs for two 2026 quarter-ends (see conflicts table) | Medium | CP-2, CP-5 | Obtain the Term Loan Amendment of December 16, 2025 and any later amendment; until then report both levels |
| No bridge from reported Adjusted EBITDA to covenant EBITDA; the figure appears only in the earnings releases, as "covenant EBITDA of $270.0 million for the last twelve months ending September 30, 2026" (Q3 release page:2) | Medium | CP-2, CP-5 | Obtain the compliance certificate or label the figure management-attributed |
| No executed credit agreements, amendments or compliance certificates (context: legal documents none) | Medium | CP-1, CP-2 | Obtain term loan and ABL agreements for definitions, baskets and pricing |
| No borrowing base certificate; availability is printed as capacity less letters of credit, and the borrowing base limit is not shown | Low | CP-2 | Obtain the certificate if usable availability is material |
| No presentations are in the pack; each of the three 2026 quarters has only an earnings release | Low | CP-1A, CP-2 | Treat releases as attributed management narrative |
| No rating agency report; only the issuer's statement that S&P upgraded from B to B+ on July 20, 2026 | Low | CP-2 | Obtain the rating report if a rating view is needed |
| Quarterly 10-Qs carry no lease maturity table or pension note; the latest lease maturity table is as of December 31, 2025 | Low | CP-2 | Use the 10-K table and label it a year-end figure |
| No pension or retiree medical disclosure was found by text search of the pack, and no purchase commitment or supply-chain finance disclosure was found in the 10-K lease and debt notes | Low | CP-2 | Treat as not supplied rather than zero |
| Text extraction only: no image, chart or speaker-note content exists in the pack, and no fidelity review was done | Low | CP-5 | Spot-check figures against the filing when used |
| Facts after the cutoff are excluded; the November 1, 2026 purchase agreement for MDS of Michigan, LLC is a subsequent event dated before the cutoff, and no purchase price is given | Low | CP-1A | Label as a subsequent event without amount |

## Next module

CP-1 should run next on the same pinned sources, followed by CP-1A, CP-2 and CP-5. Each must cite the controlling filing over the earnings release, take ABL terms from the Q2 and Q3 10-Qs rather than the 10-K, carry the covenant level conflict and the missing covenant EBITDA bridge forward as stated limitations, and keep Q3 2026, nine-month 2026, LTM and FY2025 labels distinct.
