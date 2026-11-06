## Request

Module CP-0, source readiness, for OPENLANE, Inc. (issuer id opln, NYSE: OPLN), pathway credit_snapshot, as-of date 2026-11-05, evidence cutoff 2026-11-05, reporting currency USD. The run asks whether the pinned source set can support the selected downstream consumers CP-1, CP-1A, CP-2 and CP-5, and what remains blocked. This module gives no credit conclusion, legal interpretation or investment opinion, and it calculates no figure. Source sufficiency is not completion of downstream analysis, and no downstream input contract is evaluated here (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED).

The context names current period q3-2026 and prior period fy-2025. The pack matches: the latest periodic filing covers the quarter and nine months ended September 30, 2026, and the latest annual filing covers the year ended December 31, 2025. The filings report in USD millions, which matches the context currency. Euro and Canadian dollar amounts appear only as facility sizes (euro 40 million lines of credit, C$175 million and C$500 million facilities) and must stay labelled as such.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-12-31_opln-20251231.htm.jsonl | 26a1eb6e044eb7884447c1771579bc95b55527d93c8454714335cfb05faebcc7 | Annual report on Form 10-K with audited statements; controlling for FY2025 audited facts | Year ended December 31, 2025, consolidated, USD millions |
| 10-Q_2026-03-31_opln-20260331.htm.jsonl | c46e877ea2548ae22544a835acae1b3618984f266ca5c5f8d9f1ce170a2f3661 | Quarterly report on Form 10-Q, unaudited filed statements | Quarter ended March 31, 2026 (Q1 2026) |
| 10-Q_2026-06-30_opln-20260630.htm.jsonl | 47753528b639818941177074a5796fb5ee4c271e3e7cb89f9ddc4bf548a73b8f | Quarterly report on Form 10-Q, unaudited filed statements | Three and six months ended June 30, 2026 (Q2 2026) |
| 10-Q_2026-09-30_opln-20260930.htm.jsonl | 9682e191d9ec651d5722722ac8ff03e1ea87ff7ece0722d12fcb449d04d13357 | Quarterly report on Form 10-Q, unaudited filed statements; latest filed period | Three and nine months ended September 30, 2026 (Q3 2026), signed November 4, 2026 |
| EX-99.3_2026-05-05_q12026openlaneearningssl.htm.jsonl | 2fc56068f78381bd02bfbe329da47d9ab40d86ee26db869d39406949616dc5f0 | Earnings slides furnished as Exhibit 99.3; management presentation with non-GAAP measures | Q1 2026, dated May 5, 2026 |
| EX-99.3_2026-08-04_q22026openlaneearningssl.htm.jsonl | 458d3c1fac99aaeefe126a46b683e88ca11580e6032ddf67da49e980bf2bff5d | Earnings slides furnished as Exhibit 99.3; management presentation with non-GAAP measures | Q2 2026, dated August 4, 2026 |
| EX-99.3_2026-11-04_q32026openlaneearningssl.htm.jsonl | bc88d193632549ac9eb968d3349190fc1ffa3b0842d97894dce16151e37cfd9a | Earnings slides furnished as Exhibit 99.3; management presentation with non-GAAP measures | Q3 2026, dated November 4, 2026 |

### Other pinned input

| Input | sha256 | Use |
| --- | --- | --- |
| context | 2fd2835b16fcd6e36fa06485261ee15d20c3a0b3f6cb56cfce407e6993d9ef70 | The requester's dated settings. It is not issuer evidence. It leaves borrower, parent, guarantors, sponsor, deal terms, quotes, ratings, peers and market data blank, and sets legal documents to none. Blank is not zero. |

The pack also held a file named _retrieval.json, which CP-OS ignored and this module did not use.

### Handoffs

| Module | sha256 | Note |
| --- | --- | --- |
| None supplied | Not applicable | CP-0 is the first module in this run. No upstream handoff exists, so none was consumed. |

### Short names used below

10-K FY2025, 10-Q Q1, 10-Q Q2, 10-Q Q3, Deck Q1, Deck Q2 and Deck Q3 refer, in table order, to the seven issuer sources. A locator `page:N` is the source chunk number in the pinned file, not the printed page. Quotes are exact substrings of the cited chunk.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and slide decks are enough to start the financial, business, credit synthesis and evidence-trace work for OPENLANE, with stated limits. No source is blocked and no identity boundary is unresolved. | Medium | The credit agreement, securitization agreements, guarantor list and ratings were not supplied, so legal terms rest on the filings' own summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited annual statements and three quarterly filings, with debt, liquidity and covenant text, are present up to the quarter ended September 30, 2026. | Debt and liquidity work can rest on filed statements rather than management claims. | High |
| Securitization obligations of the finance business sit on the balance sheet outside the long-term debt table. | A reader who takes only the term loan as debt will miss the larger collateralized obligations. | High |
| A December 31, 2025 collateral figure in the annual report was later corrected by the quarterly filings. | The later figure must be used for that date, and the annual figure treated as superseded. | High |
| The slide decks lose their chart content in text extraction. | Operating metrics must come from filed tables, not from the charts. | Medium |

### Readiness view

The effective source set can support CP-1, CP-1A, CP-2 and CP-5 for OPENLANE, Inc. The view for each is READY_WITH_LIMITATIONS: each owner can perform its method on located filed evidence, and the gaps below are bounded and carried forward rather than blocking. No consumer is CONDITIONAL or BLOCKED, because no source has blocked preparation, the issuer identity is resolved to the registrant itself, and every missing item (executed agreements, guarantor list, ratings, market data) limits the depth of legal or market work without preventing the owner's workflow. This view is source sufficiency only. It does not establish that quarterly inputs will normalize, that any figure reconciles, or that a downstream module will accept its inputs.

| Consumer | View | Evidence it demands and what is present | Limitations carried forward |
| --- | --- | --- | --- |
| CP-1 (financial and credit data) | READY_WITH_LIMITATIONS | Income statements, balance sheets, cash flows, debt note, securitization note, liquidity text, covenant text and Adjusted EBITDA reconciliations for FY2025, Q1 2026, Q2 2026 and Q3 2026, with the nine-month period in the latest 10-Q | G1, G3, G4, G6, G7 |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description, two segments (Marketplace and Finance), the Series A preferred repurchase and conversion, the October 2025 incremental term loans, the September 2026 securitization amendments, share repurchases, management letters in the decks | G2, G5, G8 |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Draws on the upstream registers. The sources supply the covenant, liquidity and securitization text those registers need | Inherits every limitation of CP-1 and CP-1A; G1, G2, G4 and G5 bear most |
| CP-5 (evidence trace validator) | READY_WITH_LIMITATIONS | Seven pinned, fully paged text sources against which quotes can be matched | Tables arrive flattened and charts are absent (G3, G6) |

### Coverage of the pack

Every page of every source was retained as extracted text: 371 of 371 pages across the seven sources (152 of 152, 55 of 55, 68 of 68, 71 of 71, 8 of 8, 8 of 8 and 9 of 9 pages in table order). Extraction status is not a fidelity review: tables arrive as running text and some column headings are split across chunks. The three decks are text only. No image, chart or speaker-note content is claimed as inspected, and chart data is a parse gap (G3).

### Source-by-source assessment

| Source | Document family and authority | Entity and perimeter | Period and basis | Version relationship | Locator and quote |
| --- | --- | --- | --- | --- | --- |
| 10-K FY2025 | Filed annual report, audited by KPMG LLP with an unqualified opinion; controlling for FY2025 | OPENLANE, Inc., Delaware registrant, consolidated; statements show continuing operations | Year ended December 31, 2025 with 2024 and 2023 comparatives | Base annual report; no amendment in the pack. One collateral figure in it is corrected by later 10-Qs (see G4) | 10-K FY2025 page:1 "For the fiscal year ended December 31, 2025" |
| 10-K FY2025 (audit) | Same | Same | Same | Same | 10-K FY2025 page:88 "Report of Independent Registered Public Accounting Firm (KPMG LLP, Indianapolis, IN, Auditor Firm ID: 185)" |
| 10-Q Q1 | Filed unaudited interim report, signed May 5, 2026 | Same registrant, consolidated | Quarter ended March 31, 2026 | Separate period; not superseded by later 10-Qs | 10-Q Q1 page:1 "For the quarterly period ended March 31, 2026" |
| 10-Q Q2 | Filed unaudited interim report, signed August 4, 2026 | Same | Three and six months ended June 30, 2026 | Separate period | 10-Q Q2 page:1 "For the quarterly period ended June 30, 2026" |
| 10-Q Q3 | Filed unaudited interim report, signed November 4, 2026; latest filed period; controlling for the latest balance sheet and covenant statement | Same | Three and nine months ended September 30, 2026 | Separate period; repeats the corrected December 31, 2025 collateral figure | 10-Q Q3 page:1 "For the quarterly period ended September 30, 2026" |
| Deck Q1 | Furnished slides; management presentation and non-GAAP measures, subordinate to filings | Consolidated, with Marketplace and Finance segment columns | Quarter, with quarterly series back to 2024 | Separate deck per quarter; each retained | Deck Q1 page:1 "Q1 2026 Earnings May 5, 2026" |
| Deck Q2 | Same | Same | Same | Same | Deck Q2 page:1 "Q2 2026 Earnings August 4, 2026" |
| Deck Q3 | Same; dated one day before the cutoff | Same | Same | Same | Deck Q3 page:1 "Q3 2026 Earnings November 4, 2026" |

### Perimeter and instrument roles

- Reporting entity: OPENLANE, Inc., a Delaware registrant, common stock listed as OPLN on the New York Stock Exchange (10-Q Q3 page:1 "Common Stock, par value $0.01 per share OPLN New York Stock Exchange"). The context leaves borrower, parent and guarantor fields blank. The filings identify the company itself as borrower under the Credit Agreement, with a Canadian subsidiary as borrower under the Canadian facility (10-Q Q3 page:18 "ADESA Auctions Canada Corporation, a subsidiary of the Company"). No parent entity is named in the sources read; that is not evidence that none exists above the registrant.
- Term loan and revolvers: the 2025 Incremental Term Loans, the Revolving Credit Facility and the Canadian Revolving Credit Facility are obligations under the Credit Agreement. Quote: 10-Q Q3 page:18 "guaranteed by certain of our domestic subsidiaries". The Canadian facility has a Canadian Borrower and its own guarantor set (10-Q Q3 page:20). The names of the guarantors are not in the text read (gap G2).
- Finance segment funding: AFC sells receivables to AFC Funding Corporation, a bankruptcy remote special purpose subsidiary that is consolidated, and AFCI has a separate Canadian facility. Quote: 10-Q Q3 page:15 "wholly-owned, bankruptcy remote, consolidated, special purpose subsidiary". The receivables sold are accounted for as secured borrowings, so the obligations appear as "Obligations collateralized by finance receivables" on the balance sheet (10-Q Q3 page:3), a liability line separate from "Long-term debt". The two lines are printed side by side: 10-Q Q3 page:17 "Total debt $ 545.9 $ 550.0" for the debt table and 10-Q Q3 page:3 "Obligations collateralized by finance receivables 2,064.1 1,758.3" for the securitization obligations. This is a perimeter distinction CP-1 and CP-2 must carry.
- Preferred equity: Series A convertible preferred stock held by affiliates of Apax and Periphas was partly repurchased in October 2025 and the rest converted to common stock in May 2026 (10-Q Q3 page:22). It is no longer outstanding at the latest balance sheet date (10-Q Q3 page:23).
- Non-GAAP perimeter: Adjusted EBITDA in the decks and 10-Qs is a company measure that deducts securitization interest in the Finance segment (Deck Q3 page:6 "Securitization interest"). Covenant EBITDA is defined separately in the Credit Agreement (10-Q Q3 page:54). The two definitions differ and the sources do not reconcile them.

### Information-availability boundary

- All seven sources are dated on or before the cutoff. The latest are the 10-Q Q3 (signed November 4, 2026) and Deck Q3 (November 4, 2026). The cutoff is 2026-11-05.
- Nothing dated November 5, 2026 or between the filing dates and the cutoff is supplied beyond these. An 8-K or other event after November 4, 2026 would be Not supplied, not absent.
- Subsequent events in the latest 10-Q are limited to share repurchase authorization and October 2026 repurchases (10-Q Q3 page:27 "In October 2026, the board of directors authorized an increase in the size of the Company’s $250 million share repurchase program").
- Forward-looking guidance in Deck Q3 is a management claim, not a filed fact (Deck Q3 page:5 "Revised Guidance (November 4, 2026)").

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Statements, debt table, securitization note, liquidity, covenant ratio, Adjusted EBITDA reconciliation | 10-Q Q3 page:2 to page:6 and page:17 to page:21; 10-K FY2025 page:122; Deck Q3 page:6 to page:8 | Debt and collateralized obligations are separate lines; December 31, 2025 collateral figure corrected |
| CP-1A | Business, segments, history, capital actions | 10-Q Q3 page:24 to page:27 and page:31; 10-K FY2025 page:4 to page:14 | No sponsor or transaction documents; Series A holders named only as affiliates |
| CP-2 | CP-1 and CP-1A outputs; covenant; liquidity; securitization terms | 10-Q Q3 page:54, page:56 and page:57 | Executed agreements not supplied; covenant definitions not verifiable |
| CP-5 | Traceable claims | All seven sources have chunk numbers | Charts absent; tables flattened |

### Analytical read-through

- Usable coverage: audited FY2025 statements and the three 2026 interim filings give a filed foundation for FY2025 and for the first, second and third quarters of 2026 and the nine months, with covenant and liquidity text in each filing. The nine months and the quarter are separate periods and must stay separate.
- Strongest contrary evidence: the Finance segment funds itself through receivable securitizations that the company accounts for as secured borrowings. The 10-Q Q3 states the committed U.S. liquidity and the Canadian facility size and that the agreements incorporate the Credit Agreement financial covenants (10-Q Q3 page:16 "The securitization agreements also incorporate the financial covenants of our Credit Agreement"). A consumer that reads only "Long-term debt" would omit the larger collateralized obligations.
- Source risk mechanism: the covenant ratio disclosed in the filings is a senior secured test that applies only on quarters in which loans under the revolvers are outstanding (10-Q Q3 page:54 "on which any loans under the Revolving Credit Facilities are outstanding"). The filing reports no borrowings on the revolvers (10-Q Q3 page:20 "there were no borrowings on the Revolving Credit Facilities"), and the ratio definition rests on Credit Agreement text that is not supplied. Any headroom conclusion therefore depends on a document outside the pack, and whether the test applies in a given quarter is a legal reading this module does not make.
- Version risk: the annual report gave a December 31, 2025 collateral figure that the 2026 10-Qs describe as an error and correct (10-Q Q3 page:16 "reflects the correction of an error from the $2,803.5 million previously disclosed in the 2025 Form 10-K"). The annual report remains the audited source for everything else, and the earlier figure sits at 10-K FY2025 page:77 and page:119.
- What cannot proceed: legal reading of the Credit Agreement and securitization agreements, guarantor-level analysis, rating or market-based work.
- Next evidence action: supply the Credit Agreement and its amendments (Exhibits 10.1a to 10.1d in the 10-Q Q3 exhibit index, including the Third Amendment dated June 30, 2026, whose terms the debt note does not describe), the Tenth Amended and Restated Receivables Purchase Agreement and its 2026 amendments (Exhibits 10.10a to 10.10c) and the Canadian Receivables Purchase Agreement and its amendments (Exhibits 10.11a to 10.11e), and Exhibit 21.1 of the annual report; confirm whether any 8-K after November 4, 2026 exists.

### Version conflicts and corrections

| Item | Earlier source and locator | Later source and locator | Downstream effect |
| --- | --- | --- | --- |
| Finance receivables serving as security for collateralized obligations at December 31, 2025 | 10-K FY2025 page:77 "$2,803.5 million and $2,335.1 million, respectively" | 10-Q Q3 page:16 "reflects the correction of an error from the $2,803.5 million previously disclosed in the 2025 Form 10-K" | Use the corrected figure for December 31, 2025 and treat the annual figure as superseded for that line only. The annual report is not otherwise restated. |
| Pack names for periods | Context labels q3-2026 and fy-2025 | Filings print quarter ended September 30, 2026 and year ended December 31, 2025 | No conflict. Labels agree. |

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Every number above is quoted from a source chunk.

## Gaps

| ID | Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| G1 | The Credit Agreement, its amendments, and the securitization and receivables purchase agreements are not supplied. Covenant levels, baskets and EBITDA definitions rest on the 10-Q summaries. The exhibit index lists a Third Amendment dated June 30, 2026 (10-Q Q3 page:68 "Third Amendment Agreement, dated as of June 30, 2026"), but the debt note describes only the First and Second Amendments, so its terms are Not supplied. | High for legal work; Medium for synthesis | CP-1, CP-2 | Supply the executed agreements named in the exhibit index |
| G2 | Guarantor names and the subsidiary list are not supplied. The filings say "certain of our domestic subsidiaries" without naming them. | Medium | CP-1A, CP-2 | Supply Exhibit 21.1 and the guarantor schedule |
| G3 | Chart content in the three slide decks (marketplace volumes, yield, finance metrics) is not in the extracted text. No inspected-image coverage is claimed. | Low to Medium | CP-1, CP-5 | Use the 10-Q operating tables for those metrics, or supply the slide images |
| G4 | The December 31, 2025 collateral figure in the annual report differs from the figure the 2026 10-Qs give for the same date. | Medium | CP-1, CP-2 | Carry the corrected figure and cite both locators |
| G5 | No credit ratings, market prices, peer data or valuation inputs are supplied. The context leaves them blank. | Low for the selected modules | CP-2 | Keep Not supplied; do not treat blank as zero |
| G6 | Text extraction flattens tables and splits some column headings across chunks, for example the liquidity table at 10-Q Q3 page:49 to page:50. | Low | CP-1, CP-5 | Check flagged tables against the filed HTML when available |
| G7 | Nothing after November 4, 2026 is supplied, and no 8-K for the quarter is in the pack. | Low | CP-1A, CP-2 | Supply later 8-Ks or confirm none |
| G8 | Management guidance and non-GAAP measures in the decks are management claims; the decks are not audited. | Low | CP-1A, CP-2 | Label as attributed claims; use filings where both exist |

## Next module

- CP-1: use the audited 10-K FY2025 and the three 10-Qs as controlling; keep the term loan, revolver and European lines (debt table) separate from "Obligations collateralized by finance receivables"; keep quarter, nine-month and year columns separate; use the corrected December 31, 2025 collateral figure; label the decks' Adjusted EBITDA and free cash flow as company non-GAAP.
- CP-1A: carry the two-segment structure, the Series A repurchase and conversion, the 2025 incremental term loans and the September 2026 securitization extensions as the main capital events; label anything after November 4, 2026 as Not supplied.
- CP-2 and CP-5: carry G1 and G2 as restrictions on covenant and guarantor statements; carry G3 and G6 as limits on chart and table checks.
