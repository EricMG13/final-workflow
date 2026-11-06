# CP-0 source readiness: ESCO TECHNOLOGIES INC (ese)

## Request

- Issuer: ESCO TECHNOLOGIES INC (issuer id `ese`, NYSE: ESE), registrant of all three filing types supplied, as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run `ese-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Requested consumers: CP-1, CP-1A, CP-2 and CP-5 (the launcher's minimum set). CP-0 runs first and has no upstream handoff.
- Execution: host session. The host read the pinned source text and wrote this answer. No provider was called.
- Periods and currency (context): current period `q3-2026`, prior period `fy-2025`, reporting currency USD. ESCO has a September fiscal year end, so "Q3 2026" is the fiscal quarter ended June 30, 2026 and "FY2025" is the year ended September 30, 2025. The 10-Q says so: 10-Q Q3 page:4 "References to the third quarters of 2026 and 2025 represent the fiscal quarters ended June 30, 2026 and 2025, respectively." The statements are in thousands of USD (10-Q Q3 page:2 "(Dollars in thousands, except per share amounts)"); the narrative text uses millions. No other currency is the reporting currency.
- Question: can the supplied public filings support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion. No figure is normalized, reconciled or calculated here.

## Sources

Locators are `page:N` of the pinned text files (a page is the source chunk, not the printed page).

### Issuer sources relied on

| Source (exact name) | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-09-30_ese-20250930x10k.htm.jsonl | fe80d5d10f35aaa7f1b7aa40e6d69aeaea7f501fabdde619947c03aa0fe69d71 | Form 10-K for FY2025 (year ended September 30, 2025), 89 pages |
| 10-Q_2025-12-31_ese-20251231x10q.htm.jsonl | 028e0b9aec25ecf720ca796f0beef13fd8b40ddc333348a8ba8153fe3b16e523 | Form 10-Q for Q1 2026 (quarter ended December 31, 2025), 24 pages |
| 10-Q_2026-03-31_ese-20260331x10q.htm.jsonl | d207365eeea17e17e69c10625b481ddba582ee4861f7a9c60376e4bd5dffc806 | Form 10-Q for Q2 2026 (quarter ended March 31, 2026), 28 pages |
| 10-Q_2026-06-30_ese-20260630x10q.htm.jsonl | 056428009193705ead08cb6828be9f20a62a9323946644ad69e280efbf618711 | Form 10-Q for Q3 2026 (quarter ended June 30, 2026), 31 pages |
| EX-99.1_2026-01-30_tm264950d1_ex99-1.htm.jsonl | 73c00c863e8360707e7681c62537391b693f1632ac470f63ec94b54622dbc238 | Earnings release for Q1 2026, 8 pages |
| EX-99.1_2026-05-07_tm2613615d1_ex99-1.htm.jsonl | 4483c93985a6b3ea98a959d8659fafa040f3230850186662a7c5bb7c5d2d8a1d | Earnings release for Q2 2026, 9 pages |
| EX-99.1_2026-08-06_tm2621646d1_ex99-1.htm.jsonl | f683102e1a6a6e74cee756fd0639a64a1d810e0d5fd17fcb2dc502f25f716fb6 | Earnings release for Q3 2026, 9 pages |

### Other inputs

| Input | sha256 | Role |
| --- | --- | --- |
| context (`contexts/866706-esco-technologies-inc-ese.json`) | da65696ce609dcf19999b44c58b8a10f43f7d7bc7cde7c4a3762d76affdde214 | User run settings; not issuer evidence. Borrower, parent, guarantor, sponsor, deal terms, quotes and ratings are blank, which is not evidence of their absence. |

### Supplied handoffs

None. CP-0 is the first module; the run supplies no upstream handoff.

### Labels used below

"10-K" is the FY2025 10-K. "10-Q Q1", "10-Q Q2" and "10-Q Q3" are the three 10-Qs. "Release Q1", "Release Q2" and "Release Q3" are the three EX-99.1 releases. The retrieval record (`_retrieval.json`) is pack metadata, not a source, and was ignored by the launcher.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied filings can support a credit snapshot of ESCO as of the quarter ended June 30, 2026, with limitations. The pending Megger acquisition and its new financing are described only in summary form. | Medium | Megger's own financials, the 2026 credit agreement and the covenant levels are not supplied, so a post-acquisition leverage view cannot be sourced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited FY2025 statements and unaudited statements for the three later quarters are located, with the VACCO business shown as discontinued operations. | Gives a reported financial base; comparisons must stay on continuing operations. | High |
| The existing $500 million revolver and incremental term loan mature August 30, 2028 and are to be replaced when the Megger deal closes. | Current debt terms are temporary; the new structure rests on an agreement that is not supplied. | Medium |
| Covenants are named as a leverage ratio and an interest coverage ratio, but required levels and reported ratios are not printed. | Covenant headroom cannot be sourced from these filings. | High |
| Nothing dated after August 10, 2026 is supplied, and management expected Megger to close in the first quarter of fiscal 2027. | Closing status at the as-of date is unknown, so debt may already have changed. | Medium |
| Earnings releases carry management-defined adjusted measures that the filings do not show. | Use filings for amounts and treat adjusted figures as attributed management claims. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for all four requested consumers. The sources are filed statements, filed notes and management releases for one registrant, all dated before the 2026-11-05 cutoff, and they cover the audited FY2025 year and each fiscal quarter since. They do not contain the documents that would govern the pending change in the capital structure: the Megger share purchase agreement, the May 29, 2026 credit agreement, any Megger financial statements, or the existing credit agreement with its covenant definitions. Those gaps bound CP-2 and CP-1A rather than prevent them, because the 10-Q Q3 summarises the transaction and the new facility sizes. No consumer is CONDITIONAL or BLOCKED, and no downstream analytical handoff is treated as a source condition.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025 statements and unaudited interim statements for all three later quarters are located with prior-year comparatives. Release adjusted measures and the interim contract-liability note need care (see Gaps). |
| CP-1A | READY_WITH_LIMITATIONS | Business, segments, the VACCO sale, the Maritime acquisition and the Megger summary are located. Megger agreements and Megger financials are not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Facility-level debt, availability, letters of credit and the new facility sizes are located. Covenant levels, the new credit agreement terms and Megger's financials are not supplied, so headroom and pro forma leverage are not sourceable. |
| CP-5 | READY_WITH_LIMITATIONS | Every source has page locators, so claims can be traced. Extraction fidelity is unreviewed and no original HTML, XBRL or slide deck is supplied. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN. None is DO NOT RUN.

### Source register

#### 10-K for FY2025 (`10-K_2025-09-30_ese-20250930x10k.htm.jsonl`)

- Family and authority: filed annual report, original authority for audited FY2025, FY2024 and FY2023 consolidated statements. page:1 "For the fiscal year ended September 30, 2025"; signed December 1, 2025 (page:51 "December 1, 2025"). Commission file number 1-10596.
- Audit: page:51 index lists "Grant Thornton LLP, PCAOB ID Number 248"; page:55 "We have served as the Company’s auditor since 2021." The internal control opinion excludes the acquired Maritime business: page:56 "Our audit of, and opinion on, the Company’s internal control over financial reporting does not include the internal control over financial reporting of ESCO Maritime Solutions Ltd."
- Statements located: operations page:57, balance sheet pages:57 to 58, equity page:58, cash flows page:59. Debt note 7 on pages:80 to 81, which prints the revolving line of credit commitment: page:80 "The Credit Facility includes a $500 million revolving line of credit as well as provisions allowing for the increase of the credit facility commitment amount by an additional $250 million". Commitments note 11 on page:86. Leases note 12 starting page:86. Income tax note around page:79. MD&A liquidity on page:39.
- Perimeter: consolidated ESCO Technologies Inc. and subsidiaries, continuing operations. The VACCO business is recast: page:8 "VACCO is reflected as discontinued operations in the Consolidated Financial Statements and related notes for all periods shown in this Annual Report." The 10-K controls the recast FY2025 and FY2024 comparatives.
- Debt terms: page:80 "The financial covenants of the Credit Facility include a leverage ratio and an interest coverage ratio." and "The Credit Facility is secured by the unlimited guaranty of our direct and indirect material U.S. subsidiaries and the pledge of 100% of the equity interests of our direct and indirect material foreign subsidiaries." Levels are not printed.
- Units: thousands of USD in statements (page:57 "(Dollars in thousands, except per share amounts)").
- Pension: a search of all 89 10-K pages for pension, retiree, postretirement, defined benefit, retirement and savings plan found only the deferred tax asset line "Pension and other postretirement benefits" (page:79). No pension or retiree medical note is in the extracted text; see Gaps.

#### 10-Q for Q1 2026 (`10-Q_2025-12-31_ese-20251231x10q.htm.jsonl`)

- Family and authority: filed unaudited quarterly report for the quarter ended December 31, 2025, filed 2026-02-09 per the pack retrieval record.
- Debt and liquidity pages:9 and 19: availability and cash are given as of December 31, 2025, and this 10-Q states the availability figure "excluding the Incremental Facility", a different basis from the 10-Q Q3. Short-term borrowings at foreign locations are also reported (page:19 "short-term borrowings at its foreign locations").
- Role: sequential quarter evidence. It is a separate active source; it does not replace the 10-K or later 10-Qs.

#### 10-Q for Q2 2026 (`10-Q_2026-03-31_ese-20260331x10q.htm.jsonl`)

- Family and authority: filed unaudited quarterly report for the quarter ended March 31, 2026.
- Debt and liquidity page:11: availability and letters of credit at March 31, 2026, weighted average rates, and the statement "As of March 31, 2026, the Company was in compliance with all covenants."
- Megger: pages:18 and 24 give the April 15, 2026 agreement. Page:24 labels it a "Subsequent Event" at the March 31, 2026 balance sheet date.

#### 10-Q for Q3 2026 (`10-Q_2026-06-30_ese-20260630x10q.htm.jsonl`)

- Family and authority: filed unaudited quarterly report for the quarter ended June 30, 2026, the latest filing supplied. Page:1 "QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(D) OF THE SECURITIES EXCHANGE ACT OF 1934 FOR THE QUARTERLY PERIOD ENDED JUNE 30, 2026". Signed page:31 "Dated: August 10, 2026".
- Statements located: three-month operations page:2, nine-month operations page:2, comprehensive income page:2, balance sheet pages:2 to 3, nine-month cash flows pages:3 to 4. The balance sheet compares June 30, 2026 with September 30, 2025. Cash flow has nine-month periods only; no discrete three-month cash flow is printed in this filing.
- Notes: segments pages:6 to 10 (A&D, USG, Test, with segment profit, D&A, assets and capex by quarter and nine months, for both years), debt note 7 pages:10 to 12, revenue disaggregation pages:13 to 15, remaining performance obligations page:16, leases note 12 pages:16 to 18, acquisition note 15 page:19.
- Debt and liquidity: page:10 "The Existing Credit Facility matures August 30, 2028, with balance due by this date." Page:11 "The letters of credit issued and outstanding under the Credit Facility totaled $12.7 million at June 30, 2026." and "As of June 30, 2026, the Company was in compliance with all covenants." The debt table (page:10) shows the revolver and the incremental term loan A separately, with the current portion.
- New facility: page:12 "The New Credit Facility will become effective subject to several conditions" and "will replace the Existing Credit Facility on the Transaction closing date". Sizes and tenors are on that page; the agreement itself is an exhibit incorporated by reference (page:30 "Exhibit 10.1 to the Company’s Form 8-K filed June 3, 2026") and is not supplied.
- Transaction: page:19 "The Company expects to complete the acquisition in the first quarter of fiscal 2027." The 8-Ks of April 15, 2026 and April 16, 2026 are referred to for terms (page:19) and are not supplied.
- Financing cost in the period: page:23 "approximately $7 million of debt financing costs incurred in the third quarter of 2026 related to the pending Megger acquisition" sits inside interest expense, net.

#### Earnings releases (EX-99.1)

- Family and authority: management-prepared, unaudited press releases furnished as Exhibit 99.1. They provide attributed supporting claims and do not override the 10-Qs. Their statements of operations repeat the 10-Q numbers, so they are not independent corroboration.
- Release Q3 (page:1 "ESCO REPORTS THIRD QUARTER FISCAL 2026 RESULTS"): segment EBIT, adjusted EBIT, EBITDA and adjusted EBITDA reconciliation (pages:6 to 8), balance sheet and cash flow (pages:8 to 9), backlog and orders (page:9), guidance and Megger status (page:3 "All filings for regulatory approval are underway and we continue to anticipate closing on the transaction in Q1 of fiscal 2027."). Non-GAAP definitions are on page:4. The adjusted interest line differs from the GAAP line (page:7), and the release footnotes list "$0.20 of debt financing" among the excluded items (page:6).
- Release Q2 (page:1 "ESCO REPORTS SECOND QUARTER FISCAL 2026 RESULTS", dated May 7, 2026) and Release Q1 (page:1 "ST. LOUIS, February 5, 2026"; the filename date 2026-01-30 is not the release date; the filename was not used to infer the period).
- Version note: guidance moved across releases (Release Q2 page:3 and Release Q3 page:3 each restate earlier ranges). Each release is a dated statement and does not revise an earlier one.

### Information-availability boundary

- Latest supplied documents: Release Q3 dated August 6, 2026 and 10-Q Q3 dated August 10, 2026. The cutoff is 2026-11-05. Nothing from August 11, 2026 to the cutoff is supplied. Events in that window, including regulatory approvals, a Megger closing, a draw on or replacement of the credit facility, an equity issuance, a dividend paid after the October 15, 2026 date announced in Release Q3 page:3, or any ratings action, are Not supplied, not absent.
- No FY2026 10-K is supplied (the fiscal year ends September 30). With that year end, the first quarter of fiscal 2027 begins October 1, 2026, which is before the as-of date, so the expected closing window had opened by then.

### Identity and perimeter

- Reporting entity: ESCO Technologies Inc., a Missouri corporation (10-Q Q3 page:1 "ESCO TECHNOLOGIES INC."; 10-K page:56 "(a Missouri corporation)"), consolidated with subsidiaries. The 10-K states the credit facility is guaranteed by material US subsidiaries (page:80). No separate issuer, co-issuer or unrestricted-subsidiary distinction is printed; the registrant is the borrower together with "certain of its subsidiaries" (10-Q Q3 page:12).
- Debt roles: the Existing Credit Facility is led by JP Morgan Chase Bank, N.A. as administrative agent (10-Q Q3 page:10). The New Credit Facility is with the same administrative agent (page:12). No bonds or notes are identified in the debt tables (10-Q Q3 page:10 shows only a revolver and an incremental term loan A).
- Acquisition parties: the seller is TBG AG, the target is Megger Group Limited (10-Q Q3 page:19). A shareholder agreement with TBG AG is "to be executed concurrently with completion" (page:30). Its terms are not supplied.
- Discontinued operations: VACCO Industries was sold in July 2025 (10-K page:8). Net cash from discontinued operations is shown separately in the cash flows (10-K page:59; 10-Q Q3 page:3).

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, segment and KPI tables, debt, cash flows, non-GAAP | 10-K pages:57 to 59, 80 to 86; 10-Q Q3 pages:2 to 12, 14 to 18; Release Q3 pages:5 to 9 | Cash flows are nine-month only in the 10-Q Q3; adjusted measures are management-defined; no discrete Q3 cash flow is printed |
| CP-1A | Business, segments, history, transaction, ownership | 10-K pages:7 to 8, 13; 10-Q Q3 pages:6 to 7, 19, 25; Release Q3 pages:1 to 3 | Share purchase agreement, shareholder agreement and Megger financials not supplied; no proxy or registration statement for the equity component |
| CP-2 | Facility-level debt, liquidity, covenants, lease and other claims | 10-Q Q3 pages:3, 10 to 12, 16 to 18, 25; 10-K pages:80 to 81, 86 | Covenant levels and ratios not printed; new credit agreement terms not supplied; no pension note located |
| CP-5 | Traceable claims, consistency across modules | All sources have page locators | Extraction fidelity unreviewed; no slides, HTML or XBRL |

### Document conflicts and consistency checks

- Contract liabilities: 10-Q Q3 page:16 states "contract assets, contract liabilities and accounts receivable totaled $127.6 million, $293.4 million and $267.5 million, respectively", while the balance sheet (page:3) prints contract liabilities of 288,142 (thousands). The same pattern appears at September 30, 2025: the 10-K balance sheet (page:58) prints 216,590 while the 10-Q Q3 note (page:16) gives "$224.7 million". The filings do not explain the difference on the pages opened. Downstream effect: CP-1 must not use the note figure and the balance sheet line interchangeably.
- Availability: the stated availability figures are not all on one basis. The 10-Q Q1 states availability "excluding the Incremental Facility" (page:19), while the 10-Q Q3 states "approximately $442 million available to borrow under the Existing Credit Facility" (page:11). Downstream effect: CP-2 must compute liquidity by facility from the printed inputs, not splice the stated availability figures across quarters.
- Interest: the 10-Q Q3 labels the caption "Interest expense, net" (page:2) and the release labels it "Interest expense" (Release Q3 page:5). The amounts shown for the quarter match. Downstream effect: label only; no amount conflict found on those pages.
- Balance sheet captions: the release prints one "Other current liabilities" line (Release Q3 page:8) where the 10-Q prints accrued salaries and accrued other expenses separately (page:3). Whether the release line is the sum of those two captions is not stated; the 10-Q controls the caption detail.

### Analytical read-through

- Usable coverage: the 10-K plus three 10-Qs give an audited year and three consecutive unaudited quarters with comparatives on one perimeter (continuing operations after the VACCO sale), so a last-twelve-months view can be built from printed periods by downstream modules. Segment data is printed by quarter and nine months.
- Strongest contrary evidence: the Existing Credit Facility is to be replaced when the Megger acquisition completes, per the 10-Q Q3 page:12 text quoted above, and the acquisition is described as "total consideration of approximately $2.35 billion, consisting of $0.9 billion in cash and ESCO equity valued at approximately $1.4 billion" (page:19). The newest balance sheet therefore describes a capital structure that management expects to change when the acquisition closes, expected in the first quarter of fiscal 2027.
- Source risk mechanism: the filings print the sizes and tenors of the New Credit Facility but not its pricing, covenant definitions, conditions, or the Megger target's earnings. A consumer that reads only the June 30, 2026 debt table will understate the post-closing debt and cannot test post-closing leverage or interest coverage. The existing facility's covenant levels are also unprinted, so even the present headroom is not sourceable.
- Evidence to downstream consequence: CP-2 can describe facility-level debt, availability, letters of credit, lease obligations and the stated covenant types, and must mark headroom and pro forma leverage Not supplied. CP-1A can describe the transaction as management summarises it and must not state terms that sit only in the unsupplied agreements.
- What cannot proceed: covenant headroom on agreement definitions; pro forma leverage or coverage; Megger standalone analysis; any statement about events after August 10, 2026.
- Next evidence action: supply the Form 8-Ks of April 15, April 16 and June 3, 2026 with their exhibits (the share purchase agreement, the shareholder agreement and the May 29, 2026 credit agreement), the Amended and Restated Credit Agreement of August 30, 2023 with Amendment No. 1, any Megger financial statements or pro forma information, and any filing between August 11, 2026 and the cutoff.

### Coverage accounting

Pages opened and read for this review: 10-K pages 1, 8, 13, 39, 44, 51, 55 to 59, 63 to 66, 79 to 82 and 86, plus search-hit excerpts of pages 7, 14, 19, 21, 22, 26 and 72; 10-Q Q3 pages 1 to 31 (all); 10-Q Q2 pages 1, 11, 18 and 24; 10-Q Q1 pages 9 and 19; Release Q3 pages 1 to 9 (all); Release Q2 pages 1 and 3; Release Q1 page 1. The remaining pages of the 10-K (89 pages), the 10-Q Q1 (24 pages), the 10-Q Q2 (28 pages), Release Q1 (8 pages) and Release Q2 (9 pages) are retained but were located by search only, not read in full. They are not claimed as inspected. Source quality and extraction status are kept apart: the text was extracted successfully, but no fidelity review against the filed HTML was done.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Every number above is quoted or located as printed, in USD, with the period given by its source.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Megger share purchase agreement, shareholder agreement and the 8-Ks of April 15, April 16 and June 3, 2026 not supplied; only the 10-Q summary and exhibit list are | High | CP-1A, CP-2 | Supply the 8-Ks and exhibits |
| Megger financial statements or pro forma information not supplied | High | CP-1A, CP-2 | Supply target financials or pro forma 8-K/A if filed |
| May 29, 2026 credit agreement terms (pricing, covenants, conditions) not supplied; only facility sizes and tenors on 10-Q Q3 page:12 | High | CP-2 | Supply the agreement (Exhibit 10.3 in the 10-Q Q3 exhibit index, page:30, found in the Form 8-K filed June 3, 2026) |
| Covenant levels and the issuer's reported leverage and coverage ratios not printed; only "compliance with all covenants" and the two covenant types | High | CP-2 | Supply the Amended and Restated Credit Agreement of August 30, 2023 and Amendment No. 1, or a compliance certificate |
| No filing or release dated August 11, 2026 to November 5, 2026 supplied, including Megger closing status | High | CP-1A, CP-2, CP-5 | Supply later 8-Ks or confirm none |
| Release adjusted EBITDA, adjusted EBIT and adjusted EPS are management-defined and exclude items such as debt financing and acquisition costs | Medium | CP-1, CP-2 | Treat as attributed claims; use filed amounts as controlling |
| Contract liabilities note totals differ from balance sheet captions without a located explanation | Medium | CP-1 | Locate the note reconciliation in the 10-K and 10-Q or flag as presentation difference |
| 10-Q Q3 has nine-month cash flows only; no discrete Q3 cash flow printed | Medium | CP-1 | Derive downstream only if inputs permit, and label as derived |
| No pension or retiree medical note in the extracted 10-K text; only a deferred tax asset line (a full-text search of the 10-K found nothing else) | Low | CP-2 | Treat pension as Not supplied; confirm against the filed 10-K if it matters |
| Quarterly slide presentations not supplied (releases used instead); Release Q3 refers to an accompanying slide presentation | Low | CP-1A, CP-5 | Supply decks if narrative slides are required |
| Original HTML and XBRL not supplied; text extraction only | Low | CP-1, CP-5 | Check flagged tables against the filed HTML |
| No ratings, market prices, peer or valuation data (context blank) | Low for these modules | CP-2 | Not required for the minimum set; keep Not supplied |
| Pages outside the read list are retained but not individually reviewed | Low | CP-5 | Search them when a downstream claim needs them |

## Next module

- CP-1: use the 10-K and the 10-Qs as controlling; label the periods Q3 2026 (three months to June 30, 2026), nine months 2026, FY2025 and LTM only if built from printed periods; keep the VACCO discontinued-operations perimeter; keep the contract liabilities note and balance sheet caption separate; treat release adjusted measures as management claims.
- CP-1A: carry the pending Megger acquisition as the central transaction (signed April 15, 2026; expected closing first quarter of fiscal 2027; seller TBG AG); label anything after August 10, 2026 as Not supplied; state terms only as the 10-Q Q3 summarises them.
- CP-2: build liquidity from the printed facility inputs (revolver, term loan A, letters of credit, cash) and show the locators; name the two covenant types and mark levels and headroom Not supplied; mark pro forma leverage Not supplied until the new agreement and Megger financials are available.
- CP-5: trace claims by page locator, keep the 10-Q controlling over the releases, and carry the extraction-fidelity limitation.
