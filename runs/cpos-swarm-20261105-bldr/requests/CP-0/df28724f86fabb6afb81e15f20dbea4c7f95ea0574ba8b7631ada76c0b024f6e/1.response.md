## Request

Source-readiness review (CP-0) for Builders FirstSource, Inc. (issuer id bldr, NYSE: BLDR), as of 2026-11-05, evidence cutoff 2026-11-05. Pathway credit_snapshot, case kind public, current period Q3 2026 (quarter ended September 30, 2026), prior period FY2025 (year ended December 31, 2025), reporting currency USD. The filings print amounts in thousands of US dollars (financial statements) or millions of US dollars (release reconciliations and MD&A); no other currency was found in the pages reviewed.

Question answered: can the pinned source set support the selected downstream work (CP-1, CP-1A, CP-2, CP-5, the minimum module set), and what remains blocked? This module gives no credit conclusion and calculates no financial figure. It judges source sufficiency only; it does not judge completion of the downstream analyses.

The run context (sha256 26c088bea94d5b4a50b7398f335a28e56083f68ba3e62b9362de602502e2ae7e) holds the user's settings, not issuer evidence. It leaves borrower, parent, guarantors, ratings, quotes, deal terms, market valuation inputs, peers and research questions blank. Blank is not zero; each stays Not supplied.

## Sources

### Issuer sources relied on

Short labels in the second column are used for locators below, written as `[label page:N]`, where a page is the source chunk shown as `page:N`, not a printed page.

| Source name (exact) | Label | sha256 of pinned file | Document family and authority | Pages retained |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31_bldr-20251231.htm.jsonl | K10 | 9bd0da5e45c4f2248ca4db64d57fc684925bf29516d1562226f10d757c9e4459 | Annual report Form 10-K, audited, fiscal year ended December 31, 2025; controlling for FY2025 facts | 114 of 114 |
| 10-Q_2026-03-31_bldr-20260331.htm.jsonl | Q1 | 363b4992626af02adfa3367e60743e610fb97e980272b73e97926fb679323cd7 | Quarterly report Form 10-Q, unaudited, quarter ended March 31, 2026 | 25 of 25 |
| 10-Q_2026-06-30_bldr-20260630.htm.jsonl | Q2 | 02ee03cdc0624d85cbcbf7a710722ddc9ac45fd9b91dc10f08e351fa9e01c57b | Quarterly report Form 10-Q, unaudited, quarter ended June 30, 2026 | 31 of 31 |
| 10-Q_2026-09-30_bldr-20260930.htm.jsonl | Q3 | eb3b1081f3726d9edfb8731ffaa8e1149a0312dcd5760fffdc5c5e326cc6f78d | Quarterly report Form 10-Q, unaudited, quarter ended September 30, 2026; controlling for current-period facts | 33 of 33 |
| EX-99.1_2026-04-30_bldr-ex99_1.htm.jsonl | R1 | 57b8b8fc9c442c401865b306d40dc3f4e8bf2c98e87e713da2af276f2efa22fe | Earnings release (Exhibit 99.1), first quarter 2026; management attributed, supporting | 12 of 12 |
| EX-99.1_2026-07-30_bldr-ex99_1.htm.jsonl | R2 | d9ac22d1edd973fb8f940548ad5207a292c8d1318f8581d90b82000eb7ba1b98 | Earnings release (Exhibit 99.1), second quarter 2026; management attributed, supporting | 13 of 13 |
| EX-99.1_2026-10-29_bldr-ex99_1.htm.jsonl | R3 | e8822f68613ed2eb08d6f6868127023f13ee8e8fe4e83662a7f4abe50d874bbc | Earnings release (Exhibit 99.1), third quarter 2026; management attributed, supporting | 14 of 14 |

Other pinned input: context, sha256 26c088bea94d5b4a50b7398f335a28e56083f68ba3e62b9362de602502e2ae7e (settings only, not issuer evidence). CP-OS also reported an ignored file, `_retrieval.json`; it is retrieval metadata, is not a pinned source and is not relied on here.

### Supplied handoffs

None. CP-0 is the first module in this run and no upstream handoff was supplied. Downstream handoffs are not a source-readiness condition.

### Extraction note on hashes

Each pinned file begins with a line "Visible text of <file>.htm, sha256 <hash>". That embedded hash is of the original HTML document and differs from the pinned file's sha256 above, as expected for a derived text extract. Examples: K10 embeds 98a37e6dbf198c1f17c7e76d3c264be8e774be5ed8cb563bfa51ab28b40f9f5d and Q3 embeds 6474c9ad29f66248e8f92688fc59130dc8c0fc46859307d8a54a1f8197e45cd0. The pinned sha256 identifies the evidence used in this run.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven pinned filings and releases cover the latest annual report and all three 2026 quarters for the single listed registrant, and support the four selected downstream analyses with stated limitations. No source is blocked. | Medium | The credit agreement, indentures and guarantor list are referenced but not supplied, so covenant and guarantor terms rest on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The audited annual report, three quarterly reports and three earnings releases are present, period-labelled and on one consolidated perimeter. | Current-period and prior-period facts can be sourced from controlling filings. | High |
| Debt by series, revolver availability, letters of credit and a covenant-compliance statement are printed in each quarterly report. | Liquidity and debt can be sourced; covenant headroom beyond the availability trigger cannot. | Medium |
| The operating segments were realigned in the second quarter and prior-period product categories were reclassified. | Period-to-period comparisons need care about the basis used. | Medium |
| Adjusted EBITDA and the net debt ratio appear only in management releases, with reconciliation lines that differ from some reported lines. | Leverage on that basis is management attributed and needs reconciling to the filings. | Medium |
| No legal documents, guarantor list, presentations or fourth-quarter 2025 release are supplied. | Collateral, guarantee and covenant terms stay summary-level; structural analysis is limited. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for each of the four selected consumers (CP-1, CP-1A, CP-2 and CP-5). No source is blocked and none is a fallback for a blocked source. The set contains the audited FY2025 annual report, the three 2026 quarterly reports and the three 2026 earnings releases, all for Builders FirstSource, Inc. as a single consolidated registrant. The limitations that every consumer must carry are: legal and financing documents are only listed as exhibits and incorporated by reference, not supplied; the guarantor subsidiaries are not named in any pinned source; Adjusted EBITDA and the leverage ratio are management-attributed measures that exist only in the releases; segment and product-category presentation changed during 2026; and the text extract flattens tables, so every figure must be checked against its page when used. A missing downstream analytical handoff is not a condition of readiness. The next evidence action is to read the debt note, the revolver availability table and the release reconciliations on the Q3 pages cited below, and to obtain the credit agreement, the indentures and the subsidiary list if covenant or structural work needs more than the filing summaries.

### Source assessment by document

#### Annual report K10

- Identity and perimeter: the registrant is the issuer itself, not a subsidiary in a combined filing. [K10 page:1] "BUILDERS FIRSTSOURCE, INC." and [K10 page:1] "For the fiscal year ended December 31, 2025". The consolidated statements cover the Company and its subsidiaries; the Revolving Facility and notes are guaranteed by "Debt Guarantors" who are not named. [K10 page:93] "guaranteed jointly and severally by the Company and all other subsidiaries that guarantee our 5.00% 2030 notes".
- Authority and fidelity: audited statements with an auditor report dated February 17, 2026, which states [K10 page:71] "recognized consolidated net sales of $15.2 billion for the year ended December 31, 2025". The statement of operations is on K10 page:71, the debt note on K10 pages:92-95, leases and other finance obligations on K10 pages:95-96, subsequent events on K10 page:103 and the exhibit index on K10 pages:108-112.
- Coverage: Items 1, 1A, 7, 7A, 8, 9A and 15 are present (Item 1 starts [K10 page:2] "Item 1. Business"). The final chunk, K10 page:114, holds only a page number and no content.
- Version relationships: no amended 10-K is in the pack. The 10-K is the only audited source; its statement of operations is the FY2025 basis for the prior period.
- Reclassification: prior-year cash flow lines were combined to conform to current presentation. [K10 page:75] "have been combined with other non-cash adjustments".

#### Quarterly reports Q1, Q2 and Q3

- Q3 is the controlling source for the current period. [Q3 page:1] "For the quarterly period ended September 30, 2026". The same registrant and the same single consolidated perimeter apply to Q1 and Q2. [Q1 page:1] "For the quarterly period ended March 31, 2026" and [Q2 page:1] "For the quarterly period ended June 30, 2026".
- Statements: Q3 holds the statement of operations (Q3 page:2), balance sheet (Q3 pages:2-3), cash flows with cash paid for interest (Q3 pages:3-4) and the debt note (Q3 page:13). Statements are continuous across page breaks (the balance sheet runs from Q3 page:2 to Q3 page:3 and the cash flow statement from Q3 page:3 to Q3 page:4), so the reader must join chunks.
- Debt and liquidity: the debt table is [Q3 page:13] "Long-term debt consisted of the following as of:" with five fixed-rate senior note series, the revolver, other finance obligations and finance leases. Availability, letters of credit and the minimum-availability trigger are on Q3 page:27: [Q3 page:27] "Net excess borrowing availability on revolving facility" and [Q3 page:27] "Excess availability must equal or exceed a minimum specified amount, currently $173.2 million". Earlier thresholds are in [Q2 page:25] "Excess availability must equal or exceed a minimum specified amount, currently $180.1 million" and the Q1 equivalent on Q1 page:19.
- Covenant status: [Q3 page:13] "We were not in violation of any covenants or restrictions imposed by any of our debt agreements at September 30, 2026." The reported fixed charge coverage ratio itself is not printed in any pinned source; only the 1.00 to 1.00 springing test is described.
- Maturity schedule: the Q3 report contains no future-maturities table. The latest dated schedule is the FY2025 one at [K10 page:95] "Future maturities of long-term debt as of December 31, 2025, were as follows", which precedes the 2026 revolver borrowings and covers notes and revolver only.
- Revolver term: the Q3 report states the facility is [Q3 page:9] "revolving credit facility due May 20, 2030".
- Acquisitions: Q3 page:9 and Q3 page:10 list the 2026 acquisitions and give the fair-value table; pro forma information is stated as not presented, so no pro forma base exists in the pack.
- Segment change: Q1 describes three divisions as the operating segments, while Q2 and Q3 describe two. [Q3 page:6] "realigned its geographical divisional structure from three operating divisions (East, Central, and West) to two operating divisions (East and West)". The two are aggregated: [Q3 page:18] "We aggregate our two operating segments into one reportable segment". No segment-level figures are therefore available beyond the consolidated statements.
- Reclassification: [Q3 page:10] "As our product category alignment continues to be refined" the prior-period category net sales were restated; each 2026 quarter carries its own restated prior-period categories, so product-category history is not on one basis across Q1, Q2 and Q3.
- Subsequent events: no subsequent-events note was found in the Q3 report by searching "subsequent event" and "subsequent to". The latest dated event in the Q3 cover is the share count date. [Q3 page:1] "The number of shares of the issuer’s common stock, par value $0.01, outstanding as of October 23, 2026, was 107,606,319."

#### Earnings releases R1, R2 and R3

- Family and authority: management press releases furnished as Exhibit 99.1; attributed supporting claims that do not override filings. [R3 page:1] "Builders FirstSource Reports Third Quarter 2026 Results"; R1 page:1 and R2 page:1 are the first-quarter and second-quarter equivalents.
- Content: reported and adjusted figures, reconciliations, balance sheet, cash flows, product-category sales, guidance and an interest reconciliation. [R3 page:13] "Reconciliation of GAAP Net Income to Adjusted EBITDA" and [R3 page:13] "Interest Reconciliation". Product categories are on R3 page:14.
- Leverage statement: [R3 page:3] "net debt to LTM Adjusted EBITDA ratio of 4.1x" is a management statement. Adjusted EBITDA is not defined in any pinned filing: a search of K10, Q1, Q2 and Q3 for "Adjusted EBITDA" finds no occurrence, so the measure cannot be tied to an audited or reviewed definition.
- Add-backs: the reconciliation includes an unspecified line. [R3 page:13] "Other management-identified adjustments (1)" with the note [R3 page:12] "Primarily relates to severance, net gain/loss on sale of assets, and other one-time costs." The amount of each constituent is not given.
- Guidance: forward-looking guidance is given without reconciliation. [R3 page:4] "We are not providing a quantitative reconciliation of our forward-looking guidance".
- Presentations: no investor presentation is in the pack. The release points to one outside the pack: [R3 page:4] "accompanying presentation can be accessed". Releases serve in place of presentations; speaker notes and slide content are therefore not covered and are not claimed.

### Entity and instrument roles

| Role | Finding | Status |
| --- | --- | --- |
| Issuer and registrant | Builders FirstSource, Inc., a Delaware corporation, consolidated with its subsidiaries | Resolved |
| Borrower and note issuer | The Company is the obligor on the Revolving Facility and five senior unsecured note series, per the debt note | Resolved from the 10-K and Q3 summaries; credit agreement and indentures not supplied |
| Parent | None named; the registrant is a listed company (context ticker BLDR) | No parent evidence; context field blank |
| Guarantors | "Debt Guarantors", defined as subsidiaries that guarantee the notes; not named in any pinned source | Unresolved gap |
| Restricted and unrestricted subsidiaries | The indentures restrict "designate unrestricted subsidiaries"; no designation list is supplied | Not supplied |
| Collateral | Revolver secured first on revolving collateral and second on notes collateral; notes senior unsecured | Summary only, from K10 page:93 and K10 page:94 |

### Consumer assessment

| Consumer | Status | Evidence demand and located coverage | Limitations carried |
| --- | --- | --- | --- |
| CP-1 financial extraction | READY_WITH_LIMITATIONS | Statements and notes in K10 (annual) and Q1, Q2, Q3 (quarterly); debt table Q3 page:13; availability Q3 page:27; cash paid for interest Q3 page:4; reconciliations R3 pages:12-13 | Flattened tables; no maturity table after the annual one; Adjusted EBITDA only from releases; no discrete fourth-quarter 2025 report |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business description K10 page:2 onward; acquisitions Q3 pages:9-10; subsequent event K10 page:103; segment note Q3 page:6; listed equity, no sponsor in context | No sponsor, ownership schedule or transaction documents supplied; acquisition accounting not complete at the 10-K date |
| CP-2 fundamental synthesis | READY_WITH_LIMITATIONS | Draws on upstream registers built from the sources above; source evidence for financial risk and business risk is present | Inherits every limitation here; depends on upstream handoffs, which are sequenced by the planner and are not a source condition |
| CP-5 evidence trace | READY_WITH_LIMITATIONS | All seven sources are retained and quotable; the locators above resolve to retained spans | The extraction was not reviewed against the original HTML; table-cell alignment must be re-read on the page |

No consumer is CONDITIONAL or BLOCKED, so none is marked DO NOT RUN.

### Conflicts and presentation differences

| Item | Source A | Source B | Downstream effect |
| --- | --- | --- | --- |
| Nine-month 2025 net interest expense | [Q3 page:2] "206,139" (thousands, statement of operations) | [R3 page:13] "205.9" (millions, Adjusted EBITDA reconciliation) | The filing controls; the release line is adjusted. The 0.2 difference is the same size as the release line "Debt issuance and refinancing cost" for that period but the release does not say it is the cause. Do not mix the two bases |
| Third quarter 2026 income tax | [Q3 page:2] "(33,562" (thousands, statement of operations) | [R3 page:13] "(1.5" (millions, Adjusted EBITDA reconciliation) | The release tax line differs from the statement and the release also lists "Tax-effect of adjustments to net income" as a separate line; the release does not explain the difference, so a reader should rebuild any EBITDA from operating lines and not copy the release line |
| Debt perimeter at December 31, 2025 | [K10 page:95] "Future maturities of long-term debt as of December 31, 2025, were as follows" (notes and revolver) | [Q3 page:13] "Long-term debt consisted of the following as of:" (includes other finance obligations and finance leases) | Different perimeters of "debt"; CP-1 must label which one it uses |
| Segment structure | [Q1 page:5] three divisions as operating segments | [Q3 page:6] two operating divisions | Basis change in the second quarter of 2026; no restated first-quarter segment data is needed because one reportable segment is reported |
| Minimum availability trigger | [Q2 page:25] "currently $180.1 million" | [Q3 page:27] "currently $173.2 million" | Different dates and a threshold that moves with the facility; not a contradiction, but headroom must use the threshold dated to the balance |

No conflict is reconciled here. Each is logged with both locators.

## Calculations

None. CP-0 does not normalize, reconcile or calculate financial figures.

Coverage counts only, from the retained page lists above:

| Count | Value | Inputs |
| --- | --- | --- |
| Sources classified | 7 of 7 | K10, Q1, Q2, Q3, R1, R2, R3 |
| Pages retained | 242 of 242 | 114 + 25 + 31 + 33 + 12 + 13 + 14 |
| Pages with no content | 1 | K10 page:114 holds a page number only |
| Handoffs consumed | 0 | None supplied at this first module |

Page-level review: the pages cited above were opened and read for this assessment. Statement, debt, liquidity, reconciliation, exhibit-index and segment pages were read in full; other pages (risk factors, equity plan, tax and similar notes) were searched by keyword and not read line by line. A successful text extraction is not a fidelity review, and none was done against the original HTML.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreement (Amended and Restated ABL Credit Agreement with Amendments No. 1 to No. 8), ABL/Bond Intercreditor Agreement, collateral agreements and six indenture exhibits (one a supplemental indenture) are listed only as exhibits incorporated by reference. [K10 page:110] "Amendment No. 8 to Credit Agreement, dated as of May 20, 2025" and [K10 page:109] "(incorporated by reference to Exhibit 4.1 to the Company’s Current Report on Form 8-K, filed with the Securities and Exchange Commission on May 8, 2025" | Medium | CP-1, CP-1A, CP-2, CP-5 | Fetch the executed documents if covenant definitions, baskets or change-of-control terms are needed. Until then use the summaries at K10 pages:93-95 and label them as summaries |
| Guarantor subsidiaries not named; the subsidiary list is listed as filed with the 10-K but is not in the pack. [K10 page:112] "Subsidiaries of the Registrant" | Medium | CP-1, CP-1A, CP-2 | Obtain Exhibit 21.1 and any guarantor schedule; leave the guarantor perimeter unresolved until then |
| Fixed charge coverage ratio and covenant headroom beyond the availability trigger are Not supplied; only the test description and the not-in-violation statements are printed | Medium | CP-1, CP-2 | State the trigger and the stated compliance only; do not compute a ratio headroom the sources do not support |
| No future-maturities table after the annual one, so the maturity profile at September 30, 2026 is not printed. The annual table predates the revolver borrowing shown in the debt table | Medium | CP-1 | Use the series list and the revolver due date; label any year-by-year wall as derived from principal and maturity dates |
| Adjusted EBITDA and the net debt to LTM Adjusted EBITDA ratio exist only in management releases and are not defined in a filing; the amount of each add-back is not itemised beyond the reconciliation lines | Medium | CP-1, CP-2, CP-5 | Present as management-attributed; rebuild a GAAP-based measure from operating income and depreciation where needed |
| No fourth-quarter 2025 earnings release, no third-quarter 2025 10-Q and no discrete fourth-quarter 2025 statement are supplied; a fourth-quarter 2025 or full-year 2025 Adjusted EBITDA is not printed in any pinned source | Low | CP-1 | Prior-period comparison rests on audited FY2025 and on 2025 comparative columns in the 2026 reports; label derived periods as derived |
| No investor presentation or slide content supplied; releases substitute. The presentation is referenced but outside the pack | Low | CP-1A, CP-2 | Treat release narrative as management language; do not claim slide coverage |
| Comparability: segment realignment in the second quarter of 2026, product-category restatements in each 2026 quarter, intangible derecognition in the second quarter, and a prior-year cash flow line reclassification in the 10-K | Medium | CP-1, CP-2, CP-5 | Use the basis stated in each source and say which report each product-category figure comes from |
| Acquisition accounting not complete at the 10-K date for the January 2, 2026 acquisition. [K10 page:103] "accounting for this business combination has not been completed" and no pro forma information is presented | Low | CP-1A, CP-2 | Treat acquired-business contribution as unaudited and unadjusted |
| No subsequent-events note found in the Q3 report and no 8-K or other filing after the Q3 filing is in the pack, so events between the Q3 report and the cutoff cannot be assessed | Low | CP-1A, CP-2, CP-5 | Say events after the Q3 report are Not supplied |
| Text extraction flattens tables to one value per line, splits negative-value parentheses across lines and breaks statements across chunks; no fidelity review against the original HTML | Medium | CP-1, CP-5 | Re-read each figure on its page and join chunks when a table spans a break |
| Context leaves borrower, parent, guarantors, ratings, quotes, deal terms, market capitalisation, peers and research questions blank | Low | CP-2 | Treat as Not supplied, never zero; no market, rating or peer input is available |

## Next module

Proceed to CP-1 (financial data extraction). Carry forward as limitations: legal documents not supplied; guarantors unnamed; covenant headroom beyond the availability trigger not printed; no maturity table after the annual one; Adjusted EBITDA and the leverage ratio are management-attributed and sourced only from the releases; segment and product-category bases changed in 2026; and tables are flattened so each figure must be confirmed on its page. Start from Q3 pages:2-4 (statements), Q3 page:13 (debt), Q3 page:27 (availability and liquidity) and R3 pages:12-14 (reconciliations), with K10 pages:71-72 and K10 pages:92-96 for the FY2025 basis. CP-1A should start from K10 page:2 and Q3 pages:9-10; CP-2 and CP-5 should treat every limitation above as inherited.
