## Request

Module CP-0 (source readiness) for Century Communities, Inc. (ticker CCS, issuer id ccs), as of 2026-11-05 with cutoff 2026-11-05. Pathway: credit_snapshot, public case. Reporting currency: USD. Current period: Q3 2026 (quarter ended September 30, 2026). Prior period: FY2025 (year ended December 31, 2025). Requested downstream modules: CP-1, CP-1A, CP-2 and CP-5.

Question answered: can the seven pinned issuer sources support those modules, and what remains blocked or limited? This handoff gives source sufficiency only. It gives no credit conclusion and does not normalize, reconcile or calculate figures. The assertion is SOURCE_SUFFICIENCY_ONLY. Statement amounts are printed in USD thousands; narrative text and releases print USD millions. The context file holds the user's dated settings, not issuer evidence. Its blank fields (deal terms, quotes, ratings, valuation inputs, sponsor, parent, borrower) are left blank, not read as zero.

## Sources

### Issuer sources relied on

Hashes are the pinned sha256 of each retained text file. The first line of every file also prints a different sha256 for the original HTML text it was extracted from; the pinned value below is the one CP-OS verifies.

| Source (exact name) | Pinned sha256 | Pages retained |
| --- | --- | --- |
| 10-K_2025-12-31_ccs-20251231x10k.htm.jsonl | 40822bca77f3d1f280fa9bdb025667cff0a3cbada92f0367c2ce2aea0f14cd10 | 141 |
| 10-Q_2026-03-31_ccs-20260331x10q.htm.jsonl | 6dbfc2b9b1702aabe0ae62a15ab79d805237cf407bb87b6f748285ee6819232c | 61 |
| 10-Q_2026-06-30_ccs-20260630x10q.htm.jsonl | 7826d33d347b5ba4a0f0ded6692f553b2cb2eab216f48c0b48fab887a5e242a0 | 68 |
| 10-Q_2026-09-30_ccs-20260930x10q.htm.jsonl | 5bb6ede8961747c92feb57cbf28091469edbccbe289914d1a5a3c7cff3b959d0 | 74 |
| EX-99.1_2026-04-22_ccs-20260422xex99_1.htm.jsonl | ef23de5e89dc27836c0aa67c681d5f651593a95499849c764478ef4002ab9849 | 9 |
| EX-99.1_2026-07-22_ccs-20260722xex99_1.htm.jsonl | 8fa7d8813bf620e387c89f24634e9692af83d752a4591b259b033efbe214d3eb | 10 |
| EX-99.1_2026-10-28_ccs-20261028xex99_1.htm.jsonl | 1a2c31ec21a3900623ca510eba56234f123a5a1fb09a2e417f1dc9e6e8c01b85 | 11 |

### Run settings (not issuer evidence)

| Item | Pinned sha256 |
| --- | --- |
| context (1576940-century-communities-inc-ccs.json) | 3f4bc378facbce0f1396d451dfff0e16ea0431cd8d227bb7281acea631c866f1 |

The file _retrieval.json in the pack folder was ignored by the run. It is retrieval metadata, not issuer evidence.

### Handoffs relied on

None. CP-0 is the first module of this run, so CP-OS supplied no upstream handoff.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases cover the annual report, three quarters and three earnings releases through September 30, 2026, and can support the four requested modules with bounded limitations. | Medium | The credit agreement, its amendments and the indentures are not in the pack, so covenant levels are not available. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited FY2025 statements and unaudited statements for each of the first three quarters of 2026 are present, with notes, debt tables and non-GAAP reconciliations. | Debt, liquidity and earnings work can be sourced from filed statements. | High |
| Covenant levels and headroom are not printed anywhere in the pack; the filings state only compliance, and the September 30, 2026 amendment revised financial covenants. | Covenant headroom cannot be assessed from this pack. | High |
| The acquisition of HistoryMaker Homes closed October 7, 2026, after the balance sheet date, with purchase accounting not finalized and no funding source stated. | Post-quarter leverage and liquidity are not in the reported balance sheet. | High |
| No presentations, ratings, market quotes or deal terms were supplied; earnings releases stand in for presentations, and text extraction cannot confirm charts or images. | Management claims rest on releases; external credit views are absent. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for CP-1, CP-1A, CP-2 and CP-5. The pack holds the FY2025 Form 10-K, the Forms 10-Q for the quarters ended March 31, June 30 and September 30, 2026, and the three matching earnings releases, all for the single registrant Century Communities, Inc., with a latest filing date of 2026-10-29 (per _retrieval.json) and therefore inside the 2026-11-05 cutoff. Filed statements control the facts; the releases are management documents that give attributed, supporting claims. The limitations are bounded and do not stop any consumer: the debt agreements are not supplied, no discrete fourth quarter 2025 statement exists in the pack, the October 7, 2026 acquisition is outside the reported balance sheet, and no image or chart content was inspected. None of these is a source-readiness BLOCK, and none makes a missing downstream handoff a condition. Source sufficiency is not completion of any downstream analysis.

### Source-by-source assessment

Locators use the retained page number, written page:N, as shown in each file.

| Source | Document family and authority | Entity and perimeter | Period and basis | Located evidence |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31 | Annual report on Form 10-K, filed with the SEC on January 29, 2026 (stated in 10-Q_2026-09-30 page:6); audited, with an Ernst & Young LLP, Denver report dated January 28, 2026 that states the statements present fairly, in all material respects. Original authority for FY2025 facts. | Century Communities, Inc., a Delaware corporation, Commission File Number 001-36491, consolidated with subsidiaries; guarantors of the senior notes are substantially all wholly-owned operating subsidiaries. | FY2025 (year ended December 31, 2025), with FY2024 and FY2023 comparatives; USD; statements in thousands. | Total debt $ 1,443,145 and $ 1,476,213 at December 31, 2025 and 2024 (page:74, page:125); extinguishment of the 6.750% senior notes due 2027 (page:75); audit reports (page:104, page:106; internal control report page:96, page:97); exhibit index listing the Credit Agreement and indentures by reference (page:100, page:101). |
| 10-Q_2026-03-31 | Quarterly report on Form 10-Q for the quarter ended March 31, 2026; unaudited. Original authority for Q1 2026. | Same registrant and perimeter. | Q1 2026 (three months), compared with the prior-year quarter and December 31, 2025. | Balance sheet (page:2); debt table showing revolving line of credit 203,700 and total debt $ 1,527,621 (page:12); liquidity (page:43). |
| 10-Q_2026-06-30 | Quarterly report on Form 10-Q for the quarter ended June 30, 2026; unaudited. Original authority for Q2 2026 and six months 2026. | Same registrant and perimeter. | Q2 2026 (three months) and six months 2026. | Balance sheet (page:2); debt table showing revolving line of credit 329,600 and total debt $ 1,683,874 (page:13); liquidity (page:48). |
| 10-Q_2026-09-30 | Quarterly report on Form 10-Q for the quarter ended September 30, 2026 (filing date 2026-10-29 per the pack's _retrieval.json); unaudited. Original authority for Q3 2026 and nine months 2026. | Same registrant and perimeter; guarantor and non-guarantor split in the supplemental guarantor information. | Q3 2026 (three months) and nine months 2026, compared with the prior-year periods and December 31, 2025. | Balance sheet and statements of operations (page:2, page:3); cash flows (page:3, page:4); segments (page:9, page:10); debt note (page:14 to page:18); letters of credit and bonds (page:26); guarantor information (page:49, page:51); liquidity (page:52); EBITDA and net homebuilding debt tables (page:65, page:66); exhibits (page:73, page:74). |
| EX-99.1_2026-04-22 | Earnings press release (Exhibit 99.1), management document. Supporting claims only. | Same registrant. | Q1 2026. | Total liquidity $886.1 million and $89.8 million of cash (page:2). |
| EX-99.1_2026-07-22 | Earnings press release (Exhibit 99.1), management document. Supporting claims only. | Same registrant. | Q2 2026. | Total liquidity $802.4 million and $132.0 million of cash, including cash equivalents and cash held in escrow (page:2). |
| EX-99.1_2026-10-28 | Earnings press release (Exhibit 99.1), management document. Supporting claims only; carries the full-year 2026 outlook. | Same registrant. | Q3 2026. | Total liquidity $863.8 million, with $119.8 million of cash including cash equivalents and cash held in escrow (page:2); full-year 2026 outlook (page:2, page:3); HistoryMaker Homes acquisition (page:1, page:2). |

### Source profile review

- Financial reports: statements, notes, segment tables, debt tables, covenant-compliance statements, non-GAAP reconciliations and cash flows are present in the 10-K and in each 10-Q. Debt is tabulated at carrying value by instrument: 3.875% senior notes due August 2029, 6.625% senior notes due September 2033, construction loan agreements, other financing obligations, the revolving line of credit and the mortgage repurchase facilities, with total debt $ 1,812,587 at September 30, 2026 (10-Q_2026-09-30 page:14). Principal of each senior note is stated as $500.0 million (page:14, page:15).
- Earnings releases: they give quarter-based figures and attributed management narrative. The Q3 2026 release carries guidance (full-year 2026 deliveries of 9,350 to 9,650 homes and home sales revenues of $3.3 billion to $3.4 billion, EX-99.1_2026-10-28 page:3). Guidance is management's statement, not a filed fact.
- Legal and financing sources: no executed legal document is supplied. The Credit Agreement dated November 1, 2024 (10-K exhibit 10.10, page:101), the Incremental Joinder Agreement dated April 22, 2025 (10-K page:102), the First Amendment dated September 30, 2026 (10-Q_2026-09-30 page:73), and the indentures dated August 23, 2021 and September 17, 2025 (10-K page:100) appear only as exhibit references incorporated by reference. They are separate active sources that are absent, not collapsed into the filings. The context field legal_documents reads "none", which agrees.
- Workbooks: none supplied. Scans, images and decks: none supplied. The pack contains no presentations; the three releases replace them. Text extraction cannot support any claim of chart or image inspection, so none is made.

### Version relationships and conflicts

- Each 10-Q is a separate period report. The 10-K and the three 10-Qs are not duplicates of each other; each release is a management summary of the matching 10-Q period and does not replace it.
- The 2026 10-Qs print 2025 comparatives that were reclassified: inventory impairment moved into cost of home sales revenues from the fourth quarter of 2025 (10-Q_2026-09-30 page:6), and stock-based compensation was added to adjusted EBITDA from the fourth quarter of 2025 with prior periods recast (page:66). The original 2025 Forms 10-Q are not in the pack, so 2025 quarterly figures exist only in this recast form.
- Figure comparison between the Q3 2026 release and the Q3 2026 10-Q found no conflict: total liquidity $863.8 million in both (EX-99.1_2026-10-28 page:2; 10-Q_2026-09-30 page:52); homebuilding debt to capital 36.8% and net homebuilding debt to net capital 34.9% in both (page:66); net income $12.6 million in the release and $ 12,617 thousand in the statements (page:3).
- Wording difference, not a numeric conflict: the Q1 2026 release says "$89.8 million of cash" while the Q2 and Q3 releases say cash "including cash equivalents and cash held in escrow". The Q1 10-Q balance sheet prints cash and cash equivalents $ 78,182 and cash held in escrow $ 11,621 (10-Q_2026-03-31 page:2), so the Q1 release figure is the combined measure. Downstream modules must use the 10-Q definition.

### Consumer assessments

| Consumer | Status | Evidence demand and carried limitations |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Needs statements, debt, liquidity, cash flow and non-GAAP inputs by period. Present for FY2025, Q1, Q2 and Q3 2026. Limitations: no discrete Q4 2025 statement; 2025 comparatives are recast; covenant levels absent; release figures are supporting claims only. |
| CP-1A | READY_WITH_LIMITATIONS | Needs business, ownership and transaction facts. Present: segments, 16 states, the Inspire Home Loans mortgage business, the Century Living multi-family business, the supplemental guarantor structure and the October 7, 2026 acquisition of HistoryMaker Homes. Limitations: purchase accounting incomplete; no sponsor, parent or ratings in the context; guarantor list (10-Q exhibit 22.1) not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Draws only on upstream registers. Inherits every CP-1 and CP-1A limitation above. |
| CP-5 | READY_WITH_LIMITATIONS | Traces claims to evidence. Inherits the limitations above, including release-versus-filing authority and the recast comparatives. |

## Calculations

No new calculation was made. CP-0 does not normalize, reconcile or derive figures. Every figure above is reproduced as printed at its locator, in the unit and period the source prints. The only counts are the retained page counts in the Sources table (141, 61, 68, 74, 9, 10 and 11 pages), taken from the retained files. Page text is retained for every page; this readiness review read the located pages named in the assessment, so full-page reading of every other page is not asserted.

## Gaps

| Gap | Severity | Affected consumers | Remediation | Citation |
| --- | --- | --- | --- | --- |
| Credit Agreement (November 1, 2024), Incremental Joinder (April 22, 2025), First Amendment (September 30, 2026) and the two senior note indentures are not supplied. Financial covenant levels, step-downs, definitions and the covenant changes made by the First Amendment are therefore Not supplied; the filings state compliance only. | High | CP-1, CP-2, CP-5 | Add the executed agreements from the Form 8-K filings named in the exhibit lists. Until then covenant headroom is Not calculable. | 10-K page:100, page:101, page:102; 10-Q_2026-09-30 page:16, page:17, page:56, page:73 |
| Revolving line of credit availability: the filings print commitments of $1.2 billion, $456.0 million outstanding and a $250.0 million letter of credit sublimit, but letters of credit of $42.3 million are described as issued "under various facilities" without a split by facility. | Medium | CP-1, CP-2 | Downstream modules must show the liquidity inputs and state whether the letters of credit reduce revolver capacity as unresolved. | 10-Q_2026-09-30 page:16, page:17, page:26, page:52 |
| HistoryMaker Homes closed October 7, 2026 for initial cash consideration of approximately $160.2 million; the funding source, purchase price allocation, goodwill and debt assumed are not supplied, and the acquired balances are not in the September 30, 2026 balance sheet. | Medium | CP-1, CP-1A, CP-2 | Treat as a subsequent event; no pro forma figures are available. | 10-Q_2026-09-30 page:7, page:34; EX-99.1_2026-10-28 page:2 |
| No discrete fourth quarter 2025 statement or release is in the pack; last twelve months and fourth quarter figures would need a downstream derivation from FY2025 and nine-month figures, and the 2025 quarterly comparatives are recast. | Medium | CP-1 | Flag any LTM figure as derived, with its inputs and the recast basis. | 10-K page:74; 10-Q_2026-09-30 page:6, page:65, page:66 |
| Guarantor list (10-Q exhibit 22.1) and the full guarantor financial statements are not supplied; only summarized condensed supplemental data is printed. | Low | CP-1A, CP-2 | Use the summarized data as printed and name the gap. | 10-Q_2026-09-30 page:49, page:51, page:73 |
| No presentations; releases substitute. Text extraction flattens tables to one cell per line, and no chart or image content is inspected. Extraction success is not a fidelity review. | Low | All | Check each downstream figure against the cited page text. | All seven sources |
| Context carries no ratings, market quotes, deal terms, peers or valuation inputs. These are blank, not zero. | Medium | CP-2, CP-5 | Any rating or market view is Not supplied; do not infer one. | context |
| The pack ends at the 10-Q filed 2026-10-29. Filings between that date and the cutoff 2026-11-05 are not in the pack, so completeness up to the cutoff cannot be confirmed from it. | Low | All | State the latest-evidence date in each downstream handoff. | _retrieval.json; 10-Q_2026-09-30 |
| Management measures (EBITDA, adjusted EBITDA, net homebuilding debt to net capital, adjusted net income) are non-GAAP and defined by the company. | Low | CP-1, CP-2 | Label as company-defined; do not set against covenant definitions that are not supplied. | 10-Q_2026-09-30 page:65, page:66 |

## Next module

CP-1. It may proceed on all seven issuer sources. Instructions for CP-1: open the located pages for each figure; use the audited FY2025 10-K and the 10-Q for each 2026 quarter as the authority and the releases only as supporting claims; carry the covenant, revolver availability, acquisition and recast-comparative limitations above; and mark every derived figure with its inputs, period and perimeter.
