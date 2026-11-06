# CP-0 — Source readiness: CCO HOLDINGS LLC (cco-holdings-llc)

## Request

- Issuer: CCO HOLDINGS LLC (issuer id `cco-holdings-llc`), co-registrant with CCO Holdings Capital Corp., as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period q2-2026, prior period fy-2025 (context).
- Run: `cco-holdings-llc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned files and wrote this answer. No provider was called.
- Question: can the supplied public filings and releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion is given, and no figure is normalized, reconciled or calculated here.

## Sources

Issuer sources relied on (exact pinned names). Locators are `page:N` chunks of the pinned text file, not printed page numbers.

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_ccoh-20251231.htm.jsonl | 98fc08971e7b602f253b4465dc2493c7d1fd2140d7f51b96e967ed5fb3218118 | Annual report on Form 10-K for the year ended December 31, 2025, CCO Holdings, LLC and CCO Holdings Capital Corp. (189 pages) |
| 10-Q_2025-09-30_ccoh-20250930.htm.jsonl | bf1745dd3dbecf91195f9fef9fea0cafc9d8a639b8157c8bb3d02dd7240529a1 | Quarterly report for the period ended September 30, 2025 (53 pages); prior-year comparative |
| 10-Q_2026-03-31_ccoh-20260331.htm.jsonl | 213317fa77d5c45445d49d044bc961ab9dfa41083289474b65a9c5985c9bbe1b | Quarterly report for the period ended March 31, 2026 (36 pages) |
| 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | 9af8d8232114d58e6ac96035eb67adc4aa9622876079128a14eacfcc389f347e | Quarterly report for the period ended June 30, 2026 (40 pages); latest filing in the pack |
| EX-99.1_2026-01-30_chtrex991earningsrelease12.htm.jsonl | cb5b5ac26ab78f0a85b295e8b2969a94081a4aecc513efb234aeefb51019e762 | Charter Communications, Inc. fourth quarter and full year 2025 earnings release, January 30, 2026 (18 pages); parent perimeter |
| EX-99.1_2026-04-24_chtrex991earningsrelease33.htm.jsonl | 483c56fedf60126a16d804e1d36760024be2164b76b1c1509864a6a063bd22be | Charter Communications, Inc. first quarter 2026 earnings release, April 24, 2026 (17 pages); parent perimeter |
| EX-99.1_2026-07-24_chtrex991earningsrelease63.htm.jsonl | 07d1723b22b814c108cba78554e38a4e4a76d8f38c9cdfecbd3804011635822c | Charter Communications, Inc. second quarter 2026 earnings release, July 24, 2026 (17 pages); parent perimeter |
| context | 1a68c05f8e4415af1307ec03597fe0b094afc35e94c83b63b62cbe99d897f95e | User run settings; not issuer evidence |

The pack also holds `_retrieval.json`, a retrieval record that the launcher ignores. It is pack metadata, not issuer evidence. It lists the filing dates used below and states "3 of 3 quarters have a release, not a presentation, on EDGAR".

Supplied handoffs: none. CP-0 is the first module and no upstream handoff exists.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filings support all four requested analyses for the issuer's own perimeter, with limits. Audited annual and unaudited interim statements are present, but no debt documents or post-June events are. | Medium | No indentures, credit agreements or filings after the June quarter; releases cover the parent, not the issuer. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Issuer statements are separate from the parent's releases, which describe a different, larger perimeter and must not be mixed in. | Using parent figures for the issuer would misstate earnings, cash and leverage. | High |
| The latest quarterly filing is for the June quarter; nothing for the September quarter is supplied. | Leverage, liquidity and debt may have moved since June; the view is stale by months. | High |
| Series-level debt detail is only in the annual report, and later redemptions and repurchases are not mapped to series. | The current maturity ladder cannot be rebuilt exactly from the supplied text. | High |
| Covenant levels are stated only in the annual report; later filings say tests were met without figures. | Current covenant headroom cannot be verified from the pack. | Medium |
| The Cox acquisition is pending and its financing is described differently across filings. | Post-closing debt and guarantor structure are unknown and may change the credit materially. | Medium |

### Readiness view

The effective source set is sufficient to start all four requested modules, each with stated limitations: all four are READY_WITH_LIMITATIONS and none is CONDITIONAL or BLOCKED. The issuer's own audited FY2025 statements and unaudited interim statements through June 30, 2026 are located with comparatives, together with a series-level debt table, covenant ratios and guarantor structure as of December 31, 2025. The binding limits are that no debt instrument, credit agreement or Cox transaction document is supplied, that nothing after the June 2026 quarter is supplied although the as-of date is November 5, 2026, and that the three earnings releases describe Charter Communications, Inc., a larger perimeter than the issuer. Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Issuer statements for FY2025 (with FY2024 and FY2023), the three-month and six-month periods to June 30, 2026 with comparatives, Adjusted EBITDA and free cash flow reconciliations and cash paid for interest are located. The maturity ladder and series list are as of December 31, 2025 only. |
| CP-1A | READY_WITH_LIMITATIONS | Business description, single reportable segment, ownership chain, guarantor and collateral structure, the equipment installment plan financing vehicle and the Cox and Liberty Broadband transactions are located. The transaction agreements themselves are not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | CP-2 can synthesize from CP-1 and CP-1A plus the located indenture and credit facility covenant text. Covenant definitions and current covenant figures are not verifiable from executed documents. |
| CP-5 | READY_WITH_LIMITATIONS | Every source has stable page locators, so claims can be traced. Visual and table-layout checks against the filed HTML or XBRL are not possible from text. |

### Source register

#### 10-K_2025-12-31_ccoh-20251231.htm.jsonl

- Family and authority: filed annual report, original authority for audited facts. page:1: "ANNUAL REPORT PURSUANT TO SECTION 13 OR 15(d)", "For the fiscal year ended December 31, 2025", registrants "CCO Holdings, LLC CCO Holdings Capital Corp." Reduced disclosure format (page:2).
- Audit: KPMG LLP report dated "January 29, 2026" (page:140), "We have served as the Company’s auditor since 2003." Critical audit matter on residential and small business revenue (page:140).
- Statements located: balance sheet (page:140-141, December 31, 2025 and 2024), statement of operations (page:141, 2025, 2024, 2023), cash flows (page:141-142, including cash paid for interest). Units "(dollars in millions)". USD.
- Debt: series-level table with principal, accreted value, interest dates and maturity, by issuer (CCO Holdings, Charter Operating, Time Warner Cable, LLC, Time Warner Cable Enterprises LLC) at page:102-104; Note 9 at page:154-160 (indenture leverage test at page:156, credit facility terms at page:157, Charter Operating covenant ratios at page:158, principal and interest by year at page:160). Leases at page:153-154. Commitments, letters of credit and legal at page:181-182. Related party at page:172.
- Non-GAAP: Adjusted EBITDA and free cash flow reconciliation at page:91 (unaudited, management-defined).
- Perimeter: CCO Holdings, LLC and subsidiaries. page:2: all membership interests are held by CCH I Holdings, LLC, a subsidiary of Charter Communications, Inc.

#### 10-Q_2025-09-30_ccoh-20250930.htm.jsonl

- Family and authority: filed quarterly report, unaudited. page:1: "For the quarterly period ended September 30, 2025". Statements of operations (three and nine months) at page:5; balance sheet page:5; cash flows page:6; debt note page:10; availability and cash at page:28.
- Role: provides the nine-month 2025 base and the September 30, 2025 balance sheet. It does not describe the current period.

#### 10-Q_2026-03-31_ccoh-20260331.htm.jsonl

- Family and authority: filed quarterly report, unaudited. page:1: "For the quarterly period ended March 31, 2026". Statements page:5-6; debt note page:10-11 (February 2026 redemptions of the 5.500% notes due 2026 and part of the 5.125% notes due 2027); Adjusted EBITDA page:18 and page:24; guarantor and distributions text page:29-31.
- Role: discrete first quarter 2026 (three months), so the second quarter can be isolated from the six-month figures.

#### 10-Q_2026-06-30_ccoh-20260630.htm.jsonl

- Family and authority: filed quarterly report, unaudited, signed July 24, 2026 (page:39). page:1: "For the quarterly period ended June 30, 2026"; non-accelerated filer; reduced disclosure format (page:2).
- Statements: balance sheet page:5; statement of operations page:5-6 (three and six months, 2026 and 2025); member's equity page:6; cash flows page:6-7 including "CASH PAID FOR INTEREST"; Notes 1 to 9 at page:7-16; MD&A page:16-33; Adjusted EBITDA and free cash flow reconciliation page:26; guarantors and collateral page:33-35; distribution limits page:36; no subsequent events note is present.
- Debt: Note 4 at page:10-11 gives only three classes (senior unsecured notes, senior secured notes and debentures, credit facilities) with principal, carrying and fair value, plus availability "approximately $3.7 billion" (page:11). No series list, maturity schedule, letters of credit figure or covenant ratio appears in this filing.
- Perimeter: CCO Holdings, LLC and subsidiaries; USD millions.

#### EX-99.1 releases (three files)

- Family and authority: management-prepared earnings releases of Charter Communications, Inc. (page:1 of each), furnished as Exhibit 99.1; unaudited and non-GAAP where stated. Issuer is a subsidiary of the releasing entity, so the releases are attributed parent-level supporting claims, not the issuer's statements.
- Perimeter conflict that downstream modules must respect: the second quarter 2026 release states "Net income attributable to Charter shareholders totaled $1.3 billion in the second quarter" (page:1) while the issuer's 10-Q shows "Net income attributable to CCO Holdings member" of $1,973 million for the same quarter (10-Q June 2026, page:6). Cash also differs: "$509 million cash position" for Charter (release page:7) versus "$285 million" for the issuer (10-Q June 2026, page:36). The 10-Q controls for issuer facts.
- Use: the releases add quarter narrative, customer data, parent leverage and a statement that "$1.2 billion in aggregate principal amount of Charter Communications Operating, LLC and CCO Holdings, LLC notes" were repurchased for "$1.0 billion in cash" (release page:1). The January release also records the January 2026 issuance by CCO Holdings of $1.75 billion 7.000% senior notes due February 2033 and $1.25 billion 7.375% senior notes due February 2036 (release page:7), which the 10-K also states (page:104 and page:155).

### Information-availability boundary

- All sources predate the as-of date and cutoff. The latest is the June 2026 10-Q and release, dated July 24, 2026.
- Nothing dated after July 24, 2026 is supplied. The pack retrieval record lists the June 2026 10-Q as the latest of the three newest 10-Qs, so no 10-Q for the September 2026 quarter is in the pack. Whether one was filed before 2026-11-05 cannot be determined from the supplied text. Events in the window July 25 to November 5, 2026, including Cox closing status, are Not supplied, not absent.
- The Q3 2025 10-Q is a comparative, not a current-period source.

### Identity and perimeter

- Issuer and reporting entity: CCO Holdings, LLC (Delaware) with co-issuer CCO Holdings Capital Corp. (all shares held by CCO Holdings, page:1 of the June 2026 10-Q). The consolidated statements are of CCO Holdings, LLC and subsidiaries.
- Ownership: 10-Q June 2026, page:1: "All of the limited liability company membership interests of CCO Holdings, LLC are held by CCH I Holdings, LLC (an indirect subsidiary of Charter Communications, Inc.". Parent, borrower and guarantor fields in the context are blank, which is not evidence of their absence.
- Debt issuers and guarantors (10-Q June 2026, page:33): "Each of CCO Holdings, Charter Operating, Time Warner Cable, LLC and Time Warner Cable Enterprises LLC (collectively, the “Issuers”)" with "substantially all of Charter Operating’s direct and indirect subsidiaries" as Obligor Subsidiaries guaranteeing the debt "(other than the CCO Holdings unsecured notes)". CCO Holdings guarantees the Charter Operating notes and credit facilities (10-K page:156-158). The Charter Operating credit facilities are the secured layer; the CCO Holdings notes are senior unsecured and "structurally subordinated to all obligations of subsidiaries" (10-K page:155).
- Outside the guarantor group: CCO EIP Financing, LLC, a bankruptcy-remote consolidated vehicle with a senior secured equipment installment plan facility (10-Q June 2026, page:11-12 and page:35). Its carrying value is a separate balance sheet line from long-term debt (page:5).
- Parent-level transactions that do not change the issuer's statements yet: the Cox Transactions (Transaction Agreement of May 16, 2025, 10-Q June 2026, page:8-9) and the Liberty Broadband Combination (page:28). The 10-Q states Cox Communications' notes are expected after closing to "constitute Guaranteed and Secured Debt" and Cox entities to "become Obligors" (page:34).

### Document conflicts and updates

| Item | Earlier statement | Later statement | Downstream effect |
| --- | --- | --- | --- |
| Cox debt to be assumed | 10-K page:64: "approximately $12.6 billion of Cox Communications’ outstanding net debt and finance leases" | 10-Q June 2026 page:9: "approximately $12.4 billion in outstanding net debt and finance leases" | Different dates and wording; the later filing is the more recent statement. CP-1A and CP-2 must show both and not pick one silently. |
| Cash to fund at Cox closing | 10-K page:64: "obligated to fund $4.0 billion of cash consideration" | 10-Q June 2026 page:27: "approximately $4.2 billion of cash purchase price"; page:8-9 lists $3.5 billion and $650 million | CP-2 must carry the stated amounts with their dates; the components in the 10-Q do not equal the $4.0 billion in the 10-K. |
| Year-end availability under credit facilities | 10-K page:104: "approximately $4.4 billion as of December 31, 2025" | 10-Q June 2026 page:11: "approximately $3.7 billion as of June 30, 2026" (March 31, 2026: approximately $4.6 billion, 10-Q March 2026 page:11) | Not a conflict; different dates. A letters-of-credit split is available only at year-end (10-K page:157, page:182). |

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, debt, liquidity, cash interest, Adjusted EBITDA, free cash flow | 10-K page:140-141, 91, 102-104, 154-160; 10-Q June 2026 page:5-7, 10-11, 26; 10-Q March 2026 page:5-6, 18, 24; 10-Q Sept 2025 page:5-6 | Series list and maturity ladder only as of December 31, 2025; no discrete third and fourth quarter 2025 statements (nine-month and full-year only); text conversion |
| CP-1A | Business, segments, ownership, guarantor structure, transactions | 10-K page:5, 98-100; 10-Q June 2026 page:7-9, 16-19, 33-35 | Cox transaction agreement, Liberty Broadband merger agreement and Exhibit 22.1 are not supplied |
| CP-2 | CP-1 and CP-1A outputs, covenants, lease and other claims, liquidity | 10-K page:153-154, 156-158, 160, 181-182; 10-Q June 2026 page:10-12, 27, 36 | Executed indentures and credit agreement not supplied; covenant figures after December 31, 2025 not stated |
| CP-5 | Traceable claims | All seven filings and releases carry page chunks | Original HTML and XBRL not supplied; releases are parent perimeter |

### Analytical read-through

- Usable coverage: the issuer's audited FY2025 statements and unaudited statements to June 30, 2026, with comparatives, support a reported financial foundation, including a last-twelve-months view to be built by CP-1 from the year and the two six-month periods. Evidence is the issuer's own 10-K (page:141) and 10-Q (page:5-6), not the parent's releases.
- Strongest contrary evidence: the pending Cox Transactions and Liberty Broadband Combination. The 10-Q states Charter will "fund approximately $4.2 billion of cash purchase price at the closing" (page:27) and expects Cox entities to become Obligors (page:34). Source risk mechanism: the supplied filings describe the post-closing guarantor group and debt only as expectations, so any capital structure built from them is a pre-closing view. Downstream consequence: CP-1A and CP-2 must label closing-dependent items as unrealized and must not treat parent leverage statements, such as Charter's "4.18 times" (10-Q June 2026 page:27), as issuer leverage.
- Perimeter mechanism: the releases and some 10-Q text are written at Charter level (net income attributable to Charter shareholders, Charter's leverage ratio, share repurchases), while the debt, interest and cash sit in the issuer. A consumer that mixes the two overstates or understates earnings and cash.
- Debt-detail mechanism: the series table is at December 31, 2025 (10-K page:102-103). The 10-Qs report only three classes and describe February 2026 redemptions of $750 million and $2.25 billion and $1.2 billion of repurchases of "various series" without series names (10-Q June 2026 page:11). CP-1 cannot rebuild an exact current maturity ladder without a disclosed series list; it can show the year-end ladder and the stated post-year-end events.
- Other claims outside debt, located for CP-2: operating leases and their maturities (10-K page:154), supply chain finance and deferred payment programs (10-Q June 2026 page:9-10), the equipment installment plan facility (page:11-12), letters of credit and surety bonds (10-K page:182), and cross-currency derivatives (10-Q June 2026 page:13). Pension plan settlement detail appears in the 10-K (page:184-185) and is not repeated in the 10-Qs.
- What cannot proceed: covenant headroom measured on executed definitions, current series-level maturity ladder, Cox closing structure, any view after July 24, 2026.
- Next evidence action: supply the Charter Operating credit agreement and the CCO Holdings and Charter Operating indentures, Exhibit 22.1 of the June 2026 10-Q, the Cox Transaction Agreement and any financing commitments, any 10-Q and 8-Ks filed from July 25, 2026 to the cutoff, and the issuer's Q3 2026 release if it exists.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Every figure above is quoted from a located page. Differences such as $4.0 billion versus $4.2 billion are reported as stated, not derived.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No filing or release after July 24, 2026 (the September 2026 quarter and events to the cutoff, including Cox closing status) | High | CP-1, CP-1A, CP-2 | Supply the third quarter 2026 10-Q and any 8-K from July 25 to November 5, 2026, or confirm none exists |
| Executed indentures, Charter Operating credit agreement and covenant definitions not supplied (context legal_documents is "none") | High for legal work; Medium for CP-2 | CP-2 | Supply the executed documents or the 10-K exhibit versions |
| Series-level debt list and maturity ladder only as of December 31, 2025; February 2026 redemptions identified by series but $1.2 billion repurchases are "various series" | High | CP-1, CP-2 | Supply a current debt schedule or a later 10-K/10-Q debt note with series detail |
| Letters of credit and revolver split only at year-end (10-K page:157, page:182); the June 2026 10-Q gives only total availability | Medium | CP-1, CP-2 | Supply facility-level availability and letters of credit at the latest date |
| Covenant ratios for Charter Operating and indenture leverage stated only at December 31, 2025 (10-K page:156, page:158); later 10-Qs say the test was met without figures | Medium | CP-2 | Supply compliance certificates or later covenant disclosure |
| Cox Transaction Agreement, Liberty Broadband merger agreement and Exhibit 22.1 not supplied | Medium | CP-1A, CP-2 | Supply the agreements and the exhibit |
| Earnings releases are Charter-level; no issuer-level release exists in the pack | Medium | CP-1, CP-5 | Use the issuer 10-Q for issuer facts and label release data as parent |
| No discrete fourth quarter 2025 statements; only full-year (10-K) and nine-month (Q3 2025 10-Q) | Low | CP-1 | Build the fourth quarter only by labelled difference, as CP-1 decides |
| No rating agency reports; the filings say only "Our split credit rating" (10-Q June 2026 page:26) | Low for selected modules | CP-2 | Not required for this scope; keep Not supplied |
| Text conversion only; original HTML and XBRL not supplied, and extraction is not a fidelity review | Low | CP-1, CP-5 | Check flagged tables against the filed HTML when available |

## Next module

- CP-1: treat the issuer's 10-K and 10-Qs as controlling; show FY2025, six months and three months to June 30, 2026 as separate labelled periods; keep the parent's releases as labelled context only; carry the year-end series table with the February 2026 redemptions and $1.2 billion repurchases as stated events; keep the equipment installment plan facility, supply chain finance and deferred payment program separate from debt and say whether each is inside the debt figure.
- CP-1A: carry the ownership chain, guarantor and collateral structure and the pending Cox Transactions and Liberty Broadband Combination as unclosed; show both the $12.6 billion and $12.4 billion Cox debt statements and the $4.0 billion and $4.2 billion cash figures with their dates.
- CP-2 and CP-5: carry the missing executed documents, the lack of post-July 24, 2026 evidence and the perimeter mismatch of the releases as restrictions; do not present closing-dependent structure as current.
