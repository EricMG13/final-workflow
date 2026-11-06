## Request

Module: source readiness for CNX Resources Corp (issuer id cnx, ticker CNX, registrant name in the filings "CNX Resources Corporation", Commission file number 001-14901). As-of date: 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit snapshot. Reporting currency: USD (the filings state dollars in thousands; the supplemental releases state dollars in millions). Current period: Q3 2026 (three and nine months ended September 30, 2026); prior period: FY2025 (year ended December 31, 2025).

Question answered: can the seven pinned filings support the requested downstream work (CP-1 financial data, CP-1A business and transaction context, CP-2 credit synthesis, CP-5 evidence trace review), and what remains blocked? This handoff gives no credit conclusion, no legal interpretation and no investment opinion, and it calculates and reconciles no figures. Selected assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

The run context holds the user's settings, not issuer evidence. Its deal terms, quotes, ratings, peers, precedents, market inputs and research questions are empty or blank; blank is not zero and each is carried as Not supplied. Attachments: no portfolio workbook, prior case, management bridge or legal documents.

## Sources

Issuer sources relied on (all pinned text extractions of SEC filings; sha256 is of the pinned `.jsonl` file; `page:N` below means the numbered text chunk of that file, not the printed page):

| Source file | Pages | sha256 |
| --- | --- | --- |
| 10-K_2025-12-31_cnx-20251231.htm.jsonl | 187 | 34906d26867f4063a9570548326f1aea238accaf202234ed312875cc66d730a2 |
| 10-Q_2026-03-31_cnx-20260331.htm.jsonl | 64 | f35c89e68df093f0b33c8b07e7cb640d444c8935ee3804f523cf6d7a71ff1fc7 |
| 10-Q_2026-06-30_cnx-20260630.htm.jsonl | 75 | 19c075fbeb27af8c1c213ff72323d0cfdbec50455060a5f2125b46e7ba51d5e1 |
| 10-Q_2026-09-30_cnx-20260930.htm.jsonl | 77 | 9faf7d3a55a356eeebefe08284a5f300d91a2458f040ef83dd387bbff3cef8f1 |
| EX-99.1_2026-04-30_ex991supplementalq126.htm.jsonl | 15 | 3a5697850deb2e3211d5d3185b6661a51563bd62fdb20267f3de757d37357681 |
| EX-99.1_2026-07-30_ex991supplementalq226.htm.jsonl | 14 | 2b713e19b995caa894ecb7c089bf8f3063b820ae69afc0691f484cdb6def48b2 |
| EX-99.1_2026-10-29_ex991supplementalq326.htm.jsonl | 14 | 8ed99193157f937c422b4de1e94f2baf28f198a6be7de2f9096adc91e46b5481 |

Run context (settings only, not issuer evidence): context, sha256 85b88b96cc0f2168f01ec8d7b4e089124543ac7d5895fc347354eca91d4820c2.

Supplied handoffs: none. CP-0 is the first module of this run, so CP-OS supplied no upstream handoff.

Ignored by the pack: `_retrieval.json` (a retrieval log, not issuer evidence). It was read only to confirm the form types, filing dates and accession numbers listed in the table below.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings are complete, current to the latest quarter and sufficient for the four downstream modules, with bounded limitations. They cover annual and quarterly statements, debt notes and covenant descriptions. | Medium | Credit agreements, indentures, ratings and market data are not supplied; covenant and guarantee terms rest on filing summaries only. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited annual and three unaudited quarterly filings plus three earnings supplements span the requested periods. | Statements, debt, liquidity and cash flow inputs can be located without leaving the pack. | Medium |
| Debt sits in two credit groups: the parent group and the midstream subsidiary group, which the parent does not guarantee. | Parent and subsidiary claims must be kept apart downstream; guarantor detail is described only in note text. | Medium |
| No executed credit agreement, indenture, rating report or post-quarter filing is supplied. | Covenant definitions, headroom and any event after the last filing cannot be verified from primary legal text. | Medium |
| Supplemental releases carry management-defined non-GAAP measures. | They are attributed support, not controlling evidence, and need reconciliation to the filed statements downstream. | Medium |

### Readiness view

The effective source set supports the requested work with limitations (READY_WITH_LIMITATIONS) for all four selected consumers. The filed statements and notes carry the controlling facts; the supplemental releases are attributed management support. The binding limitations are that no executed financing document, rating or market input is supplied and that the text extraction is chunked and flattened, so table structure and any charts are not independently verified. No source is blocked, no identity boundary is unresolved and no conflict between sources was found. This is source sufficiency only; downstream analytical handoffs are not a readiness condition.

### Source inventory and assessment

Locators below were opened and the quoted strings confirmed in the cited chunk (see Located evidence).

| Source | Document family and authority | Entity and perimeter | Period and basis | Version relationship |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | Annual report, Form 10-K, filed 2026-02-10 (per retrieval log); audited statements with auditor opinion (page:112); controls report (page:176). Controls the audited FY2025 facts. | CNX Resources Corporation and subsidiaries, consolidated; includes the midstream subsidiary CNX Midstream Partners LP (CNXM) | Fiscal year ended December 31, 2025; income statement for 2025, 2024, 2023; balance sheets at December 31, 2025 and 2024 | Base annual report; no amendment supplied; Q3 10-Q comparatives refer back to it |
| 10-Q Q1 2026 | Quarterly report, Form 10-Q, filed 2026-04-30; unaudited | Same consolidated perimeter | Three months ended March 31, 2026 | Separate active source; does not replace the 10-K |
| 10-Q Q2 2026 | Quarterly report, Form 10-Q, filed 2026-07-30; unaudited | Same | Three and six months ended June 30, 2026 | Separate active source |
| 10-Q Q3 2026 | Quarterly report, Form 10-Q, filed 2026-10-29, signed 2026-10-29 (page:77); unaudited | Same | Three and nine months ended September 30, 2026; balance sheet at September 30, 2026 against December 31, 2025 | Latest filing; the controlling source for the current period |
| EX-99.1 1Q 2026 | Earnings release supplement furnished 2026-04-30; management-prepared, attributed | Consolidated; non-GAAP reconciliations | Quarterly and trailing-twelve-month columns | Separate active source; supports, does not override, the 10-Q |
| EX-99.1 2Q 2026 | Same, furnished 2026-07-30 | Same | Same | Separate active source |
| EX-99.1 3Q 2026 | Same, furnished 2026-10-29 | Same | Same, to September 30, 2026 | Latest supplement |

The 10-K statements are stated in thousands of US dollars; the supplemental release reconciliations are stated in millions, so release figures are rounded and are not interchangeable with filing figures without a stated rounding basis.

### Entity and instrument roles

- Issuer and registrant: CNX Resources Corporation (Delaware; page:1 of each filing). The statements are consolidated; no separate stand-alone parent statements are supplied.
- Restricted subsidiaries guaranteeing the parent credit facility and the parent senior notes are described in note text; they are not named individually in the pinned notes. The 10-K exhibit index lists a subsidiaries exhibit "filed herewith" (page:186), but that exhibit is not part of the pinned text.
- CNXM (CNX Midstream Partners LP) is a separate credit group: the parent credit facility excludes it, and the filing states the parent is not a guarantor of the CNXM senior notes or the CNXM revolver. Downstream modules must keep the two groups apart.
- Parent covenant ratios exclude CNXM, its subsidiaries and its general partner; CNXM carries its own three covenants. The covenant definitions are summarised in the notes only.
- Trustee for the parent notes indentures: UMB Bank, N.A. (per the Q3 10-Q debt note and 10-K exhibit index).

### Coverage against the downstream needs

| Need | Where located | Status |
| --- | --- | --- |
| Discrete quarters | Income statement five-quarter columns in the Q3 supplement (page:4); balance sheets (page:5); cash flows (page:6); three-month columns in each 10-Q | Retained |
| Quarter versus year-to-date | Q3 10-Q income statement shows three and nine months (page:8); cash flows are nine months only (page:10) | Retained; discrete quarterly cash flows come from the supplement or by later difference |
| Fiscal years | 10-K Item 8 statements and notes (page:111 onward) | Retained |
| Segments | Q3 10-Q Note 14 (page:32 to page:35); 10-K Note 21 (page:163) | Retained; segment detail beyond these notes is not supplied |
| Add-backs and non-GAAP bridges | Q3 supplement EBITDAX and adjusted EBITDAX reconciliation (page:13); net debt (page:12) | Retained as management measures |
| KPIs, volumes, hedges | Q3 supplement production, activity and hedge tables (page:2, page:3); 10-Q market risk hedge table (page:75) | Retained |
| Facility-level debt and carrying values | Q3 10-Q Note 8 (page:19 to page:21) and Note 10 (page:21 to page:23); 10-K Notes 10 and 12 (page:142, page:144) | Retained |
| Covenants | Note 8 summaries of the parent and CNXM tests and compliance statements (page:20, page:21) | Retained as summary only; definitions and calculations not supplied |
| Cash-paid interest and tax | Q3 10-Q Note 16 (page:36); 10-K Note 16 (page:155) | Retained |
| Leases, pensions, commitments, litigation | 10-K Notes 13, 14, 20 (page:149, page:151, page:160); Q3 10-Q Note 11 (page:25) | Retained |
| Business and operating narrative | 10-K Item 1 and Item 7 (page:8, page:82); Q3 10-Q Item 2 (page:36) | Retained |
| Transactions and history | Q3 10-Q Note 4 acquisitions and dispositions (page:17); Note 10 financing events (page:22, page:23) | Retained |

### Consumer assessment

| Consumer | Status | Evidence demand and limitation carried forward |
| --- | --- | --- |
| CP-1 financial data | READY_WITH_LIMITATIONS | Statements, notes and discrete-quarter columns are located. Limitations: thousands against millions units; extraction is chunked text, so table layout must be checked against the cited chunk; Q4 2025 discrete amounts appear as a column in the supplements, not in a 10-Q. |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business description, segment note, acquisitions, dispositions and financing events are located. Limitations: no ownership or sponsor information in the context; no executed transaction documents; no management presentation deck, only release supplements. |
| CP-2 credit synthesis | READY_WITH_LIMITATIONS | Debt, liquidity, covenant summaries and compliance statements are located. Limitations: no ratings, no market data, no executed credit agreement or indenture, so covenant headroom and maturity terms rest on note summaries. |
| CP-5 evidence trace review | READY_WITH_LIMITATIONS | Every source is retained with a pinned hash and located chunks. Limitations: citations resolve to numbered chunks, not printed pages; non-GAAP figures in the supplements need the filed statements as the controlling comparison. |

DO NOT RUN set: empty. No consumer is conditional or blocked.

### Conflicts and version issues

No conflict between sources was found in the facts read: the debt and cash positions in the Q3 supplement (page:12) are consistent in label and period with the Q3 10-Q balance sheet and debt note, with the release rounded to millions. The comparison was a read-through only and no figure was recalculated here. Rounding and the thousands versus millions basis are a downstream reconciliation duty, not a conflict. The supplements are management claims that cannot override the filings.

### Located evidence

| Source | Locator | Quote |
| --- | --- | --- |
| 10-Q_2026-09-30_cnx-20260930.htm.jsonl | page:20 | The calculation of all of the ratios excludes CNXM, its subsidiaries, and its general partner. |
| 10-Q_2026-09-30_cnx-20260930.htm.jsonl | page:21 | *CNX is not a guarantor of CNXM's 4.75% Senior Notes due April 2030 or the CNXM Credit Facility. |
| 10-Q_2026-09-30_cnx-20260930.htm.jsonl | page:20 | CNX was in compliance with all financial covenants as of September 30, 2026. |
| 10-Q_2026-09-30_cnx-20260930.htm.jsonl | page:21 | CNXM was in compliance with all financial covenants as of September 30, 2026. |
| 10-Q_2026-09-30_cnx-20260930.htm.jsonl | page:22 | The New Notes are guaranteed by all of CNX's restricted subsidiaries that guarantee the CNX Credit Facility |
| 10-Q_2026-09-30_cnx-20260930.htm.jsonl | page:36 | The following table shows cash paid: |
| 10-Q_2026-09-30_cnx-20260930.htm.jsonl | page:77 | Dated: October 29, 2026 |
| 10-K_2025-12-31_cnx-20251231.htm.jsonl | page:112 | In our opinion, the consolidated financial statements present fairly, in all material respects |
| 10-K_2025-12-31_cnx-20251231.htm.jsonl | page:182 | Fourth Amended and Restated Credit Agreement, dated as of May 17, 2024 |
| EX-99.1_2026-10-29_ex991supplementalq326.htm.jsonl | page:12 | Net Debt: Total long-term debt minus cash, cash equivalents, and restricted cash. |
| EX-99.1_2026-10-29_ex991supplementalq326.htm.jsonl | page:13 | Adjusted EBITDAX TTM |

## Calculations

None. CP-0 does not normalize, reconcile or calculate figures. The only counts used are page counts of the pinned files (187, 64, 75, 77, 15, 14 and 14 pages) and the number of sources (seven issuer sources plus the run context).

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Not supplied: executed credit agreements and note indentures. They appear only in the 10-K exhibit index (page:182, page:183) and are incorporated by reference to earlier Form 8-K filings. | Medium | CP-1, CP-2, CP-5 | Obtain the exhibits if covenant definitions, baskets or maturity mechanics are to be tested; until then rely on the note summaries and label them as summaries. |
| Not supplied: credit ratings, market capitalization, market net debt, quotes, peers and precedents (context fields blank or empty; no rating report in the pack). | Medium | CP-2 | Treat as Not supplied; do not infer from the filings. |
| Not supplied: any document dated after 2026-10-29 and before the 2026-11-05 cutoff (for example a Form 8-K). The pack cannot show whether events occurred in that window. | Low | CP-1A, CP-2 | State the latest filing date, 2026-10-29, as the knowledge horizon; treat later events as unknown, not absent. |
| Not supplied: summarized financial information of guarantor and non-guarantor subsidiaries. A search of the 10-K and Q3 10-Q found no such disclosure. | Medium | CP-1, CP-2 | Keep the parent and CNXM groups separate using the note text; do not derive stand-alone parent figures. |
| Parse limitation: the extractions are fixed-size text chunks with tables flattened into running text; `page:N` is a chunk number, not a printed page. The supplements' tables of contents list printed pages up to 17, while the extractions hold 14 to 15 chunks. | Medium | CP-1, CP-5 | Open each cited chunk and confirm column order before using a figure. |
| Parse limitation: charts, images, the cover-page logo and any speaker content are not represented in the text; no presentation deck is supplied, only earnings release supplements. Image or chart coverage is not claimed. | Low | CP-1A | Do not rely on visual content; record it as a parse gap. |
| Source quality: management non-GAAP measures (EBITDAX, adjusted EBITDAX, net debt, free cash flow) are definitions chosen by the issuer; the covenant EBITDA definition differs from them and is not supplied. | Medium | CP-1, CP-2 | Label as management measures; do not equate with covenant ratios. |
| Units: filings in thousands, supplements in millions. | Low | CP-1, CP-5 | State the unit and rounding basis with every figure. |

## Next module

Proceed to CP-1 (financial data) on the pinned filings, then CP-1A, CP-2 and CP-5 in the order CP-OS sets. All four may run. Carry forward these limitations: filings control over supplements; chunk numbers are not printed pages; the parent and CNXM credit groups stay separate; covenant, guarantee and maturity terms are note summaries only; ratings, market data, guarantor financial information and documents after 2026-10-29 are Not supplied. CP-1 should take statements from the 10-K and the three 10-Qs, use the supplements only for discrete quarters and non-GAAP bridges with attribution, and keep the thousands and millions bases labelled.
