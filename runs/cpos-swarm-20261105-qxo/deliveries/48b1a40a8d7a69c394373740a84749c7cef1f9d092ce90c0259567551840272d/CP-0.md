## Request

Module CP-0 (source readiness) for QXO, Inc. (ticker QXO, issuer id qxo), as of 2026-11-05, pathway credit_snapshot, reporting currency USD, current period Q2 2026 (quarter ended June 30, 2026), prior period FY2025. The run requests the minimum module set (CP-1, CP-1A, CP-2, CP-5) from filings and earnings releases only. This handoff answers one question: can the pinned source set support that work, and what remains blocked. It gives no credit conclusion, performs no normalisation or reconciliation, and treats source sufficiency as separate from completion of downstream analysis. Nothing dated after 2026-11-05 is used.

## Sources

Issuer sources relied on (each is a page-chunked text extraction of a filed document; extraction status is not a fidelity review):

| Source file | sha256 | Family and period |
| --- | --- | --- |
| 10-K_2025-12-31_qxo-20251231.htm.jsonl | 1b7dee5c3907814ca02da7e5177715b488778f3cfe6a6a69dbb9a2d892ae7bd4 | Form 10-K, fiscal year ended December 31, 2025, audited |
| 10-Q_2025-09-30_qxo-20250930.htm.jsonl | 38eff6a9b29b23e51b5e94454227cd801b8344fa3f2dbacbcff9586720ba1f5f | Form 10-Q, quarter ended September 30, 2025, unaudited |
| 10-Q_2026-03-31_qxo-20260331.htm.jsonl | f661446a2ae3c415c83c14493e42b107a6ed744b45a540466d49f9056424d438 | Form 10-Q, quarter ended March 31, 2026, unaudited |
| 10-Q_2026-06-30_qxo-20260630.htm.jsonl | 894ff623087578f719301215adbe097ad733e1b300a9d2d5bf4a10f19be9a21b | Form 10-Q, quarter ended June 30, 2026, unaudited |
| EX-99.1_2026-02-25_qxoq4-25earningsrelease.htm.jsonl | b326e55b305ddcd9c74b52354a08688ca3531d1057c5c1ee442c94d9779f5a35 | Earnings release dated 2026-02-25, fourth quarter and full year 2025 |
| EX-99.1_2026-05-12_qxoq1-26earningsrelease.htm.jsonl | cb6d12c2f11a6aae12e16b22f726607cf654ffc6f9c813c160df8563f9de9aa2 | Earnings release dated 2026-05-12, first quarter 2026 |
| EX-99.1_2026-08-13_qxoq2-26earningsrelease.htm.jsonl | 67328156dff6e164d45723d576bcfc4e259ba15144552671032a5a2232707d03 | Earnings release dated 2026-08-13, second quarter 2026 |

Run settings (not issuer evidence): context, sha256 6a7b1beefd6814e2c0ed169307a2fa7c8234de27933b1d6c6e62ef434dbf5add. It names USD, as-of and cutoff 2026-11-05, current period q2-2026, prior period fy-2025. Its deal terms, quotes, ratings, peers and research questions are empty; blanks are not zero.

Handoffs: none supplied. CP-0 is the first module in this run, so no upstream handoff exists to consume.

Ignored by the pack: the retrieval index file _retrieval.json is not a source.

Coverage unit counts (source chunks, shown as `page:N`): 10-K 111 of 111, 10-Q September 2025 81 of 81, 10-Q March 2026 68 of 68, 10-Q June 2026 99 of 99, release February 2026 10 of 10, release May 2026 9 of 9, release August 2026 11 of 11. These are chunk counts of the extraction, not printed page numbers, and establish no readiness by themselves.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filings and releases support the minimum credit snapshot for the QXO, Inc. consolidated group through the June 2026 quarter, with stated limitations. The TopBuild acquisition closed after quarter end and its effects are only partly reported. | Medium | No post-closing balance sheet, TopBuild financials or acquisition accounting is supplied, and the debt agreements are not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Quarterly statements, debt note, lease note and liquidity inputs are present for the latest quarter and the prior year-end. | Net debt, liquidity and coverage can be built from filed figures for the June 2026 balance sheet. | High |
| The company closed a large acquisition on July 1, 2026 and its accounting is incomplete. | Debt, preferred stock and earnings after the quarter are not yet on a reported balance sheet. | Medium |
| Beacon is the predecessor and QXO history before April 29, 2025 is a different business. | Year-on-year comparisons and trailing figures need explicit perimeter labels. | Medium |
| Indentures, credit agreements and predecessor financial information are listed as exhibits but not supplied. | Debt terms can only be taken from the filed notes, not from executed documents. | Medium |

### Readiness view

The effective source set is adequate to start the requested minimum work, with bounded limitations: READY_WITH_LIMITATIONS for CP-1, CP-1A, CP-2 and CP-5. The set holds one audited annual report, three interim reports and three earnings releases, all issued by QXO, Inc. and all text-searchable. No consumer is CONDITIONAL or BLOCKED on source grounds. The main limits are the post-quarter TopBuild closing (reported only in narrative and notes), the absence of executed debt documents, and the absence of any investor presentation. This is a statement of source sufficiency only; it does not evaluate any downstream input contract or assert normalised quarters.

### Source profile by document

Document family, authority and perimeter come from located content, not file names.

- **10-K, FY2025.** Filed annual report for QXO, Inc. Cover: `10-K_2025-12-31_qxo-20251231.htm.jsonl` page:1: "FORM 10-K" and "For the fiscal year ended: December 31, 2025". Audited: page:60: "We have audited the accompanying consolidated balance sheet of QXO, Inc." Controlling filed authority for FY2025 statements, debt, leases and equity notes. The index on page:59 lists two audit reports (PCAOB IDs 34 and 688); the second report opens on page:62 with "as of December 31, 2024", so the prior-year balance sheet and year were audited by a different firm from the FY2025 auditor. The 10-K therefore carries two auditors across the two years. FY2025 contains Beacon only from the acquisition date: `EX-99.1_2026-02-25_qxoq4-25earningsrelease.htm.jsonl` page:1: "include the legacy Beacon Roofing Supply, Inc. (“Beacon”) operational results from the date of acquisition on April 29, 2025".
- **10-Q, Q3 2025.** Interim, unaudited, supports quarter, nine-month and balance sheet at September 30, 2025, and the Beacon measurement-period goodwill adjustment (page:19). It is the only source for Q3 2025 discrete figures, which are needed for any trailing view together with the 10-K.
- **10-Q, Q1 2026.** Interim, unaudited, quarter ended March 31, 2026. Reports whole amounts with one decimal (goodwill table, page:10), whereas the June 2026 report changed rounding, see conflicts below.
- **10-Q, Q2 2026.** Latest interim filing, signed August 14, 2026 (page:99). Holds the debt note (page:44 to page:51), leases (page:51), equity and mezzanine equity (page:30 onward), acquisitions (page:18 to page:26) and MD&A (page:52 onward). Perimeter is QXO, Inc. and subsidiaries; debt sits at the subsidiary QXO Building Products, Inc. and the notes were issued by the Issuer, which assumed the Beacon financing: `10-Q_2026-06-30_qxo-20260630.htm.jsonl` page:45: "QXO Building Products assumed the obligations under the 2032 Notes and the 2032 Indenture". The term loan and ABL borrower is the subsidiary with Queen HoldCo, LLC as Holdings (page:47). Whether the parent QXO, Inc. itself is a guarantor of the notes is not stated in the pages read and is a gap.
- **Earnings releases (three).** Management documents furnished as Exhibit 99.1. They provide attributed non-GAAP measures (Adjusted EBITDA, Adjusted Net Income) with reconciliations and quarter versus year-to-date columns. They do not override the filings. The August release (`EX-99.1_2026-08-13_qxoq2-26earningsrelease.htm.jsonl` page:1) shows three-month and six-month columns, so quarter and year-to-date figures are separately available for June 2026.

### Coverage by evidence need

- **Statements and periods.** Balance sheet, operations and cash flow for the six months to June 30, 2026 are in the August release (page:7 to page:9) and the Q2 10-Q. Discrete quarters can be located: Q2 2026 (August release page:1), Q1 2026 (May release page:1), Q4 2025 (February release page:1), Q3 2025 (10-Q September 2025). Quarter and year-to-date distinctions are labelled in each release.
- **Debt.** The Q2 10-Q debt table lists each instrument with principal, carrying value and fair value: `10-Q_2026-06-30_qxo-20260630.htm.jsonl` page:44: "Term Loan Facility(2) $ 850 $ 829 $ 848" and "2032 Senior Secured Notes(4) 2,250 2,232 2,326". Rates, maturities, security and redemption terms are described in the note (page:45 to page:51).
- **Liquidity.** ABL capacity and letters of credit are printed: page:49: "the Borrower had $1.93 billion borrowing capacity under the ABL Facility" and page:51: "the Borrower and its restricted subsidiaries had $62 million in outstanding standby letters of credit issued under the ABL Facility". Whether the stated capacity is before or after the letters of credit is not stated in the passage; this is for the downstream liquidity step to resolve and flag.
- **Covenants.** Only one maintenance test is described, a springing test: page:50: "maintain a minimum fixed charge coverage ratio of 1.0 to 1.0 at any time that availability is less than". Compliance is stated for the indentures, term loan and ABL (page:46, page:48, page:50). Defined terms are not supplied, so a covenant-basis ratio cannot be rebuilt.
- **Cash interest and taxes.** Printed in the August release cash flow supplement (page:9): "Interest $ 106 $ 23" and "Income taxes, net of refunds $ 5 $ 35" for six months 2026 and 2025.
- **Leases.** Maturity table of operating and finance leases at June 30, 2026 is printed (page:51).
- **Preferred and mezzanine equity.** Series C Preferred Stock is mezzanine equity (page:36); Convertible and Mandatory Convertible Preferred are in equity with dividends in the cash flow statement (August release page:8 to page:9).
- **Segments and KPIs.** Net sales by line of business are in the August release (page:9). The Q2 10-Q states one operating segment (page:28: "views its operations and manages its business as a single operating segment") and plans new reportable segments after Kodiak and TopBuild (page:29: "plans to report financial information based on its new reportable segments in the future"). No segment profit measure exists in the pack; this is a limitation for CP-1.
- **Business and transaction narrative.** Beacon, Kodiak and TopBuild transactions, with funding, are described in the Q2 10-Q (page:53 to page:54): "The Company completed its acquisition of TopBuild for a purchase price of approximately $15 billion."

### Strongest contrary evidence and limitations

- **Subsequent event is incomplete.** The TopBuild closing date is after the balance sheet date, and the filing says: page:26: "initial accounting for the business combination is incomplete and the Company is not yet able to disclose the provisional amounts". Mechanism: the June 30 balance sheet shows escrowed proceeds as restricted cash, page:8 of the August release footnote: "restricted cash of $3.0 billion, representing the gross proceeds from the issuance of the 6.500% Senior Notes due 2031 and 6.875% Senior Notes due 2034". Debt, preferred stock, shares and earnings capacity after July 1, 2026 therefore sit outside the reported balance sheet. Consequence: any leverage or liquidity measure built on June 30, 2026 figures mixes a pre-closing balance sheet with a financing that closed on July 1, 2026, and downstream modules must show a pro forma debt bridge from narrative only and label it as constructed.
- **Perimeter changes.** QXO was a software and services company before Beacon: `10-Q_2026-06-30_qxo-20260630.htm.jsonl` page:18: "the financial results of QXO as of and for any periods prior to April 29, 2025 do not include the financial results of Beacon". Beacon was determined the predecessor (page:12). The pack carries no complete Beacon predecessor statements: page:98: "The predecessor financial information is included as Exhibit 99.1 to this Quarterly Report and is incorporated herein by reference" and the exhibit index (page:99) shows it as a prior filing, not in the pack. Consequence: FY2025 and first-half 2025 comparatives are not like-for-like with 2026, and Kodiak contributes only from April 1, 2026 (August release page:1: "from the date of acquisition on April 1, 2026"). Trailing twelve-month figures would blend four different perimeters.
- **Mid-year presentation change.** `10-Q_2026-06-30_qxo-20260630.htm.jsonl` page:12 records that rounding changed in the second quarter of 2026 to the nearest whole million, while earlier filings and the February and May releases show one decimal. Conflict locators: May release page:1 "$ 1,730.2" versus August release page:1 "$ 4,976". Consequence: sums across periods can differ by rounding; this is a presentation difference, not a restatement, and no restatement was found by a search for restatement language beyond the cover check box.
- **Executed documents absent.** The exhibit list shows the indentures, supplemental indentures and the incremental term loan amendment as filed exhibits (`10-Q_2026-06-30_qxo-20260630.htm.jsonl` page:98 and page:99) but none is in the pack. Consequence: covenant definitions, baskets, restricted payment tests, guarantor lists and change-of-control terms are known only through the note summaries. The filing says restrictions are not significant for common dividends (page:51), which is a management statement.
- **No presentation or Q3 2026 results.** No investor deck and no results for the quarter ended September 30, 2026 are in the pack, and the Q2 10-Q says the preliminary TopBuild purchase price allocation is expected in the September 2026 quarter report. Whether that report was available before the cutoff is not evidenced by the pack; nothing after the cutoff is assumed.
- **Management claims.** Market-position and target statements (for example the "$50 billion in annual revenue within the decade" target) are management assertions in the releases (August release page:2), not filed fact; non-GAAP measures carry management add-backs (restructuring, transaction, transformation, stock-based compensation) that need reconciliation to filed figures downstream.

### Consumer assessment

| Consumer | Status | Basis and limitations carried forward |
| --- | --- | --- |
| CP-1 (financial extraction, quarters and debt) | READY_WITH_LIMITATIONS | Statements, debt table, lease table, cash interest and tax are located. Limits: mixed rounding, perimeter breaks at the Beacon and Kodiak dates, no TopBuild statements, one operating segment so only line-of-business sales are available. |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Beacon, Kodiak and TopBuild transactions, funding and risk factors are described in the filings. Limits: TopBuild accounting incomplete; no executed merger or financing documents; market claims are management statements. |
| CP-2 (credit synthesis) | READY_WITH_LIMITATIONS | Depends on CP-1 and CP-1A handoffs sequenced by the planner; that dependency is not a source condition. Source limits above apply, in particular the pre-closing balance sheet and absent covenant definitions. |
| CP-5 (evidence review) | READY_WITH_LIMITATIONS | Evidence is locatable by chunk. No third-party, ratings or market data are supplied, so any claim needing them must be labelled outside the pack or a gap. |

### Command sheet

All four consumers: RUN, with the limitations above carried into each request. No consumer is marked DO NOT RUN.

## Calculations

None. CP-0 does not normalise, reconcile or calculate figures. Figures appear only inside quotations copied from the sources. The coverage counts above are counts of extraction chunks per file as supplied.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Post-closing (after July 1, 2026) balance sheet, TopBuild financial statements and purchase price allocation not supplied | High | CP-1, CP-2 | Obtain the September 2026 quarterly report if filed on or before 2026-11-05; otherwise build a labelled pro forma bridge from the Q2 10-Q narrative. |
| Executed indentures, credit agreements, ABL and term loan amendments not supplied | Medium | CP-1, CP-2, CP-5 | Obtain exhibits listed in the Q2 10-Q exhibit index; until then use note summaries only and mark definitions Not supplied. |
| Beacon predecessor financial information (Exhibit 99.1) not supplied | Medium | CP-1, CP-2 | Obtain the exhibit if a like-for-like prior period is required. |
| Prior-year (2024) statements in the 10-K were audited by a different firm; the legacy-QXO year is a different perimeter | Low | CP-1 | Label 2024 figures as legacy QXO and not comparable with 2025 and 2026. |
| Parent guarantee of the notes and entity-level (restricted group) financials not located | Medium | CP-1, CP-2 | Search notes and exhibits for guarantor tables; label parent versus subsidiary debt. |
| ABL capacity stated relative to letters of credit not specified | Low | CP-1, CP-2 | Treat the capacity and letters of credit as separate inputs and flag the ambiguity in liquidity. |
| Single operating segment today; new reportable segments are planned but not yet reported | Low | CP-1, CP-2 | Use line-of-business sales only; do not state segment margins. |
| No investor presentations; image and chart content not inspected | Low | CP-1A | Text extraction cannot support chart or image claims; none are made. |
| Rounding basis differs between releases and filings | Low | CP-1 | Label every figure with its source rounding. |
| Ratings, market quotes, peers and deal terms are blank in the context | Medium | CP-2, CP-5 | Not supplied; they are not treated as zero. |

## Next module

CP-1, then CP-1A, CP-2 and CP-5 as sequenced by CP-OS. Carry forward: the pre-closing June 30, 2026 balance sheet versus the financing that closed on July 1, 2026; the perimeter breaks (QXO before April 29, 2025, Beacon from that date, Kodiak from April 1, 2026); whole-million versus one-decimal rounding; reliance on note summaries for debt terms; and the open gaps above.
