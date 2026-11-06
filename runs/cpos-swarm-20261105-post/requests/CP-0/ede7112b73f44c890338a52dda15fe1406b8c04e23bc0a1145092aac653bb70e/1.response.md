## Request

Issuer: Post Holdings, Inc. (ticker POST, Missouri corporation, St. Louis; registrant on Form 10-K and Form 10-Q, SEC file number 1-35305). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot, public case, research run.

Question for this module: can the supplied source set support the requested downstream work (the four selected analytical modules CP-1, CP-1A, CP-2 and CP-5, and the report sections that draw on them), and what remains blocked. This module gives no credit conclusion, calculates nothing and normalises nothing.

Run settings (from the context file, which is not issuer evidence): reporting currency USD; current period `q3-2026`, prior period `fy-2025`. Post's fiscal year ends on September 30, so `q3-2026` is the fiscal third quarter ended June 30, 2026 (nine months fiscal 2026 year to date), and `fy-2025` is the fiscal year ended September 30, 2025. The sources are in USD, in millions, and use the same fiscal calendar, so there is no currency or period mismatch with the context. The context leaves deal terms, quotes, ratings, valuation inputs, peers and research questions blank; blank is treated as not supplied, never as zero.

## Sources

Page numbers below are the source chunks shown as `page:N`, not printed pages.

### Issuer sources relied on

| Source (exact name) | sha256 | Chunks |
| --- | --- | --- |
| 10-K_2025-09-30_post-20250930.htm.jsonl | d988e0426964cfec01029656ef227ac10adca18ba413287c184f18404a876a74 | 169 |
| 10-Q_2025-12-31_post-20251231.htm.jsonl | e9cc6f62805c1b1bab9b7edb1afd055ae5b09d286a5f5385add48be2adcd1950 | 43 |
| 10-Q_2026-03-31_post-20260331.htm.jsonl | 6ed320d389c86598b7ad5f845098fe00ce2f7584e166c2976b8679a029b0c42b | 51 |
| 10-Q_2026-06-30_post-20260630.htm.jsonl | 5c5310f7f925e1ac072ebdb2eef5ec580787271894d731c4b0f244a823ad7595 | 50 |
| EX-99.1_2026-02-03_ex99-1q12026er.htm.jsonl | 38e17081ebfa3fafaf0505f1bd57fb738f074e8b7b4014662d7731549585d17b | 19 |
| EX-99.1_2026-05-05_ex99-1q22026er.htm.jsonl | c699bde5529dd39cf184dac3c7c6fd8e1af3530dddd1b671a659bdd669e9f846 | 24 |
| EX-99.1_2026-08-06_ex99-1q32026er.htm.jsonl | fa25c942bbdfd0499284c17eaea7c77be614d163d4c3ae3f0600195efb353a9c | 22 |

### Run context

| Item | sha256 |
| --- | --- |
| context (user settings, not issuer evidence) | 42de786351216298f80706a9245ba3397a337baef9248bdb3ddc19ef12ef23d8 |

### Supplied handoffs

None. This is the first module of the run, so no upstream handoff exists.

### Pack file not used as evidence

`_retrieval.json` is pack metadata written by the fetcher (filing dates, accession numbers, file hashes). CP-OS ignores it. It is not a filed document and is not relied on here.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed documents cover the annual report, the three latest quarterly reports and the three matching earnings releases, so the planned financial, business and synthesis work can proceed with stated limits. | Medium | No credit agreement, indentures, ratings, market data or investor presentations were supplied, so legal terms and covenant headroom cannot be checked. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited annual statements and unaudited quarterly statements are present and complete for the company as one consolidated reporting entity. | Debt, liquidity and earnings work can rely on filed statements rather than management claims. | High |
| Debt terms come only from financing notes, not from the executed documents. | Guarantor lists, collateral detail, call terms and covenant definitions cannot be verified and stay summary-level. | Medium |
| The financial covenant is a secured leverage test, but the releases report a total leverage figure under a different definition. | Covenant headroom cannot be calculated from the pack. | Medium |
| Acquisitions, divestitures and share repurchases change the perimeter during the period. | Period comparisons need care, and no source after the third quarter release shows the position since June 30, 2026. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for the requested pathway. Every source is a filed statement or an issuer earnings release for one legal entity, Post Holdings, Inc., reported on a consolidated basis, and the periods line up with the run: the latest annual report covers the fiscal year ended September 30, 2025 and the latest quarterly report covers the quarter ended June 30, 2026. Filed statements control the figures; the earnings releases are issuer presentations that supply attributed adjusted measures, guidance and the net leverage and interest coverage reconciliation, and they never override a filing. No source is blocked, no identity boundary is unresolved, and nothing in the pack is dated after the cutoff. The limits are missing source types, not unreadable evidence: there are no executed financing documents, no ratings or market data, no investor presentations and nothing after the third quarter release. Those limits restrict legal, covenant and valuation analysis but do not prevent the four selected modules from running. Source sufficiency is not evaluated here for model-input acceptance: the assertion is SOURCE_SUFFICIENCY_ONLY, CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

### Source-by-source assessment

| Source | Document family and authority | Entity and perimeter | Period and basis | Located evidence (exact quote, page) |
| --- | --- | --- | --- | --- |
| 10-K_2025-09-30 | Annual report on Form 10-K; filed statement with audit opinion; controls annual facts | Post Holdings, Inc. and subsidiaries, consolidated; four reportable segments | Fiscal year ended September 30, 2025, with FY2024 and FY2023 comparatives; USD millions | "For the fiscal year ended September 30, 2025" (page:1); "Total Assets $ 13,528.4 $ 12,854.2" (page:95) |
| 10-Q_2025-12-31 | Quarterly report on Form 10-Q; unaudited filed statement | Same consolidated entity | Fiscal first quarter ended December 31, 2025, with September 30, 2025 balance sheet comparative | "For the quarterly period ended December 31, 2025" (page:1); "Total Assets $ 12,984.3 $ 13,528.4" (page:3) |
| 10-Q_2026-03-31 | Quarterly report on Form 10-Q; unaudited filed statement | Same consolidated entity | Fiscal second quarter ended March 31, 2026, year to date six months | "For the quarterly period ended March 31, 2026" (page:1); "Total Assets $ 12,977.2 $ 13,528.4" (page:3) |
| 10-Q_2026-06-30 | Quarterly report on Form 10-Q; unaudited filed statement; latest balance sheet in the pack | Same consolidated entity | Fiscal third quarter ended June 30, 2026, year to date nine months | "For the quarterly period ended June 30, 2026" (page:1); "Total Assets $ 12,852.7 $ 13,528.4" (page:3) |
| EX-99.1_2026-02-03 | Earnings release, Exhibit 99.1; issuer presentation of results, adjusted measures and guidance | Post Holdings, Inc., consolidated | Fiscal first quarter ended December 31, 2025 | "Post Holdings Reports Results for the First Quarter of Fiscal Year 2026; Raises Fiscal Year 2026 Outlook" (page:2) |
| EX-99.1_2026-05-05 | Earnings release, Exhibit 99.1 | Same | Fiscal second quarter ended March 31, 2026 | "Post Holdings Reports Results for the Second Quarter of Fiscal Year 2026; Affirms Fiscal Year 2026 Outlook" (page:2) |
| EX-99.1_2026-08-06 | Earnings release, Exhibit 99.1; latest source in the pack | Same | Fiscal third quarter ended June 30, 2026, nine months and twelve months ended June 30, 2026 | "Post Holdings Reports Results for the Third Quarter of Fiscal Year 2026; Narrows Fiscal Year 2026 Outlook" (page:2) |

### Version relationships

The three 10-Qs and the 10-K are separate periodic reports, not drafts or duplicates of each other, and all stay active. Each 10-Q repeats the September 30, 2025 balance sheet as its comparative, so the 10-K and later 10-Qs overlap on that date; the 10-K is the audited source for September 30, 2025 and the 10-Qs are consistent copies, for example the same total assets figure appears in all four filings. No amendment (10-K/A or 10-Q/A), waiver or supplement is present, and none is referred to in the text read. The three earnings releases each cover the same quarter as one of the 10-Qs; they are companions with different authority (issuer presentation versus filed statement), not duplicates. Releases disclose adjusted measures that the filings do not.

### Entity roles and perimeter

Borrower, issuer and parent are the same entity: Post Holdings, Inc. The text states that the revolving credit agreement is guaranteed and secured by subsidiaries and that senior notes are guaranteed by domestic subsidiaries, for example: "are secured by security interests in substantially all of our assets and the assets of our subsidiary guarantors, but excluding, in each case, real property" (10-Q June 30, 2026, page:39). The sources do not name the guarantor subsidiaries, the excluded subsidiaries or any unrestricted subsidiary, and do not give guarantor-only financial information. Consolidated statements include a noncontrolling interest (Weetabix East Africa and Alpen are described in the 10-Q June 30, 2026 notes, page:8), which is shown as a separate equity line and means consolidated figures are not all attributable to the borrower group. These distinctions stay open as gaps.

### Consumer assessment

| Consumer | Status | Evidence demanded and located | Limitation carried |
| --- | --- | --- | --- |
| CP-1 (canonical financial data and credit metrics) | READY_WITH_LIMITATIONS | Statements of operations, balance sheet, cash flows, debt note, segment tables, liquidity and covenant text, and adjusted EBITDA, net leverage and interest coverage reconciliations are all present. Debt table: "6.50% senior notes maturing March 2036 1,300.0 —" and "$ 7,676.0 $ 7,452.2" (10-Q June 30, 2026, page:17). Revolver: "As of June 30, 2026, the Revolving Credit Facility had no outstanding borrowings, outstanding letters of credit of $23.2 and an available borrowing capacity of $976.8." (page:21). Net leverage: "Net leverage as calculated under Post’s credit agreement 4.6x" (EX-99.1 August 2026, page:22). | Covenant ratio not reported in covenant form; fiscal-year labelling; perimeter changes; no fourth-quarter data; the first quarter release has no net leverage reconciliation. |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description, segments, acquisitions, divestitures and capital allocation are present in the 10-K and quarterly notes. Divestitures: "On December 1, 2025, the Company completed its previously announced sale of 8th Avenue’s pasta business" (10-Q June 30, 2026, page:10); "On May 1, 2026, the Company completed the sale of substantially all of the assets of" the Crystal Farms Business (page:12). Guidance: "Narrowed fiscal year 2026 Adjusted EBITDA (non-GAAP)* outlook to $1,560-$1,570 million" (EX-99.1 August 2026, page:2). | Public listed company with no sponsor and no pending financing transaction document; no investor presentations or management prepared remarks; guidance is management language. |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Draws only on upstream handoffs from CP-1 and CP-1A, which the sources support. | No rating, market or peer context (context blank); inherits all CP-1 and CP-1A limits. A missing upstream handoff is not a source condition. |
| CP-5 (evidence trace validation) | READY_WITH_LIMITATIONS | Needs the pinned sources to test cited quotes and cross-module figures; all seven are text-extracted and quotable. | Extraction fidelity of tables was not independently reviewed; checks are limited to the supplied text. |

### Coverage statement

All seven sources were extracted to text with 378 chunks in total, namely 169 for the 10-K, 43, 51 and 50 for the three 10-Qs, and 19, 24 and 22 for the three releases. Every source was read for identity, period and statement content; no chunk is marked blocked. Each coverage unit is retained as evidence, recorded as a gap in the Gaps section, or ignored with a basis (only `_retrieval.json`, which is pack metadata). The 10-K contains the audit report (page:91 to page:94), the full statements (page:94 to page:98), the long-term debt note (page:131 to page:142) and the exhibit index (page:163 to page:168). Short chunks, such as page:101 or page:111 of the 10-K, are page-break splits within tables or notes and the neighbouring chunks carry the remainder. This is text extraction only: no chart, image or presentation slide was inspected, and a successful extraction is not a fidelity review.

### Strongest contrary evidence and limitations

Evidence: the financial covenant is described as a springing secured net leverage test, "a secured net leverage ratio not to exceed 4.25:1.00" (10-Q June 30, 2026, page:23), tested only when revolver usage exceeds the stated share of commitments. Source risk mechanism: the only leverage ratio the pack reports is total net leverage under the credit agreement definition, "Net leverage as calculated under Post’s credit agreement 4.6x" (EX-99.1 August 2026, page:22), which uses principal debt less cash and a different numerator. No secured net leverage figure is printed in any source. Downstream consequence: CP-1 can show the reported total ratio and the stated covenant level, but cannot compute covenant headroom, and CP-2 must not describe headroom as measured.

Evidence: the debt note lists each instrument, but guarantee, security and call terms are given only in summary, and the 10-K exhibit index lists the governing documents, for example "4.1 Indenture (2029 Notes), dated as of July 3, 2019" (10-K, page:163), without including them. Source risk mechanism: summary note text is a filed statement but is not the executed document, so definitions, baskets, restricted payment capacity and release mechanics cannot be tested. Downstream consequence: legal, intercreditor and restricted-payment conclusions are not supportable from this pack; share repurchases are large and are disclosed ("Subsequent to the end of the third quarter of fiscal year 2026 through August 5, 2026, Post repurchased 0.4 million shares for $39.3 million", EX-99.1 August 2026, page:6), so the missing capacity definitions matter.

Evidence: the latest balance sheet is June 30, 2026 and the latest source is dated August 6, 2026, while the as-of date is November 5, 2026. Source risk mechanism: leverage, liquidity and share count may have moved since; the only post-quarter fact is the repurchase through August 5, 2026. Downstream consequence: the current period is the quarter ended June 30, 2026, and any statement about the position at the as-of date is outside the evidence.

### Conflicts and anomalies

1. Release dates against file names. The first quarter release file is labelled 2026-02-03, but the text reads "Post Holdings Reports Results for the First Quarter of Fiscal Year 2026; Raises Fiscal Year 2026 Outlook St. Louis - February 5, 2026" (EX-99.1_2026-02-03, page:2). The second quarter release file is labelled 2026-05-05, but the text reads "St. Louis - May 7, 2026" (EX-99.1_2026-05-05, page:2). The document text controls: use February 5, 2026 and May 7, 2026 as release dates. Both are well before the cutoff, so no cutoff effect.
2. Fiscal naming. File names such as `ex99-1q12026er` describe the fiscal first quarter, which ends December 31, 2025, not a calendar first quarter. Downstream labels must follow the document text.

## Calculations

None. CP-0 performs no calculation, normalisation or reconciliation. Every number quoted above is copied from a source as printed, with its locator. Ratios and sums are left to the downstream modules.

## Gaps

| Gap | Severity | Affected consumers | Why it matters | Remediation |
| --- | --- | --- | --- | --- |
| No credit agreement, amendments, joinders or indentures supplied; the 10-K exhibit index lists them only by title (context attachment `legal_documents` is none) | High for legal analysis; moderate for the snapshot | CP-1A, CP-2, CP-5 | Guarantors, collateral, covenant definitions, call schedules and baskets are known only from summary notes | Obtain the executed documents before any legal or restricted-payment conclusion |
| Secured net leverage ratio, the financing covenant metric, is not reported in any source; only total net leverage under the credit agreement definition is reported | High for covenant work | CP-1, CP-2 | Headroom is Not calculable from the pack | Obtain the compliance certificate or the credit agreement definitions |
| Net leverage reconciliation is absent from the first quarter release | Low | CP-1 | Trend of the reported ratio is available only for two of the three quarters | Use the two later releases; do not infer the first |
| No ratings, market prices, valuation inputs, peers or research questions (context blank) | Moderate | CP-2 | No external credit view or market-implied view; text mentions ratings only as a risk factor | State as Not supplied; any external data must be labelled as external |
| No investor presentations; earnings releases stand in for all three quarters. Prepared remarks and call transcripts are referred to ("Post will publish prepared remarks related to this release", EX-99.1 August 2026, page:8) but are not in the pack | Low to moderate | CP-1A | Management narrative and non-GAAP guidance bridges are limited to the release text | Use release text as attributed management language |
| No source after the August 6, 2026 release; no fiscal year 2026 annual report or fourth-quarter release; no position at the as-of date | Moderate | CP-1, CP-2 | Latest balance sheet is June 30, 2026 | Label all current figures as of June 30, 2026 |
| Guarantor subsidiaries, excluded and unrestricted subsidiaries not named; no guarantor-level financial information | Moderate | CP-1A, CP-2 | Structural subordination and asset coverage by entity cannot be assessed | Treat as Not supplied |
| Perimeter changes: acquisition of 8th Avenue effective July 1, 2025, sale of the pasta business on December 1, 2025 and sale of Crystal Farms on May 1, 2026 | Moderate | CP-1, CP-1A | Period comparisons and twelve-month figures mix different perimeters; the 10-Q gives pro forma data for the acquisition only ("Pro forma net sales", page:10) | Downstream modules must label perimeter on every comparison |
| Extraction is text only: charts, images and any formatting-dependent content were not inspected; the table layout is flattened into text | Low | all | Misread columns are possible in dense tables | CP-5 should open each cited locator |
| No amendment, waiver or supplement documents are in the pack, and none was found referred to as pending | Low | CP-1 | Absence is not proof that none exists | Not applicable beyond this note |

## Next module

Proceed to CP-1 (canonical financial data) with all seven sources, then CP-1A, CP-2 and CP-5 in that order. No consumer is marked DO NOT RUN. Carry these limits forward into each: label every figure by fiscal period (fiscal year ended September 30, 2025, quarter ended June 30, 2026, nine months ended June 30, 2026, twelve months ended June 30, 2026) and by perimeter; use filed statements first and releases as attributed management figures; report the credit-agreement net leverage and interest coverage as reported and do not present them as the springing covenant metric; write Not supplied for ratings, market data, guarantor detail and executed financing terms; and treat June 30, 2026 as the latest balance sheet date. The next evidence action, if the committee wants legal or covenant conclusions, is to obtain the credit agreement and the note indentures and the latest compliance certificate.
