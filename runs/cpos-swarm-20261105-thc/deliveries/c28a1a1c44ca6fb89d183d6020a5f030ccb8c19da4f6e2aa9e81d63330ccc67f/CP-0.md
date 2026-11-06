# CP-0 source readiness: TENET HEALTHCARE CORP (thc)

## Request

- Issuer: TENET HEALTHCARE CORP (issuer id `thc`; registrant name as filed: Tenet Healthcare Corporation, NYSE: THC), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run `thc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, reporting currency USD, current period Q3 2026, prior period FY2025. The requested consumers are CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned files and wrote this answer. No provider was called.
- Question: can the supplied public filings support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This answer gives no credit conclusion, legal interpretation or investment opinion, and it normalizes, reconciles and calculates nothing.
- Locators: `page:N` is the source chunk number in the pinned `.jsonl` text, not the printed page. Earnings-release text also carries its own printed "Page N" labels, which differ from the chunk numbers.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_thc-20251231.htm.jsonl | f11b8c51ccd0de901ead39554fe597e277a823a504d6f5879743322f2e033f67 | Form 10-K for the fiscal year ended December 31, 2025 (185 chunks) |
| 10-Q_2026-03-31_thc-20260331.htm.jsonl | ae2f3d08760ee554a01678cce38fd15c1f6dcfb4f1eb937aa8f7c46189f0123b | Form 10-Q for the quarter ended March 31, 2026 (50 chunks) |
| 10-Q_2026-06-30_thc-20260630.htm.jsonl | a8d86c65c6d20d928c4d4325b82f5d466ad3837698345b3d3bc00c8145f3cd72 | Form 10-Q for the quarter ended June 30, 2026 (57 chunks) |
| 10-Q_2026-09-30_thc-20260930.htm.jsonl | e79732f4107be2e25480e8b1b80ad38188b6eb8362209287bd06381751951a29 | Form 10-Q for the quarter ended September 30, 2026 (54 chunks) |
| EX-99.1_2026-04-30_thc-20260331ex991earningsr.htm.jsonl | 5ea4e9008424f03304d19bf4ecd566569d118ac8a64e8cca9032f7ad6a5e6de8 | Exhibit 99.1 earnings release dated April 30, 2026 (15 chunks) |
| EX-99.1_2026-07-23_thc-20260630ex991earningsr.htm.jsonl | 03d054c86dcde38802e070349b77939f6a497570e6b4a7e4537e884b4aff9ae1 | Exhibit 99.1 earnings release dated July 23, 2026 (16 chunks) |
| EX-99.1_2026-10-29_thc-20260930ex991earningsr.htm.jsonl | de8966425c6d51c46fec7968d415d855247be5599cd3f04bbba535aedb3bc95d | Exhibit 99.1 earnings release dated October 29, 2026 (16 chunks) |
| context | 0ee21d145e164a59cd564e90c45b59adffc7b68df2c1b6fb4dcb72027505ffb5 | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module, so no upstream handoff exists and none is relied on.

The pack also holds `_retrieval.json`, which CP-OS ignores. It is not a source here.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed documents cover audited annual and unaudited quarterly statements, the debt note, liquidity and the main transaction. They are enough to start all four requested analyses, each with stated limits. | Medium | Credit agreement, indentures, slide decks and anything after the latest earnings release are not supplied; covenant definitions cannot be checked. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt, revolver, letter-of-credit and covenant text is located in the latest annual and quarterly reports, but covenant tests are described only in the annual report. | Covenant headroom needs the executed documents, so any headroom view must rest on company wording alone. | Medium |
| Reported revenue and the company's adjusted earnings measure treat the early-termination consideration from the Conifer arrangement differently from ordinary revenue. | A reader who mixes the revenue lines or the adjusted measure overstates or understates recurring cash earnings. | High |
| The reported net-debt ratio comes from the release with no net-debt figure or definition supplied. | The ratio cannot be rebuilt from the sources, so it is attributed to management only. | High |
| September 2026 refinancing is documented in the quarterly report and release but the new indenture is not supplied. | New-note terms beyond the quarterly summary cannot be verified. | Medium |

### Readiness view

The effective source set is sufficient to run CP-1, CP-1A, CP-2 and CP-5, each with limitations. Audited FY2025 statements, three unaudited 2026 interim reports (the latest for the quarter ended September 30, 2026) and three issuer earnings releases are located and internally dated before the cutoff. The set cannot support work that depends on executed legal terms, guarantor-level detail, ratings, market pricing, slide decks or events after October 29, 2026. Those gaps are bounded and none blocks a consumer outright, so no consumer is CONDITIONAL or BLOCKED.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025 and unaudited Q1, Q2 and Q3 2026 statements, debt note, liquidity text and non-GAAP reconciliations are located. Cash flows are year-to-date, so discrete quarters need subtraction by the consumer. No XBRL or original HTML. |
| CP-1A | READY_WITH_LIMITATIONS | Business, segments, the Conifer and CommonSpirit agreements, ownership interests and the September 2026 refinancing are located. The Omnibus Agreement, the 8-K of February 2, 2026 and the new indenture are not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Can synthesize from CP-1 and CP-1A plus located covenant, liquidity and debt-structure text. Executed credit documents and ratings are not supplied. |
| CP-5 | READY_WITH_LIMITATIONS | All sources are chunked text with stable locators, so claims can be traced. Layout and visual checks against the filed HTML are not possible. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source register

#### Form 10-K for FY2025 (`10-K_2025-12-31_thc-20251231.htm.jsonl`)

- Family and authority: filed annual report; original authority for audited consolidated statements. page:1 states "Annual report pursuant to Section 13 or 15(d) of the Securities Exchange Act of 1934 for the fiscal year ended December 31, 2025".
- Audit: page:113 states "our report dated February 17, 2026, expressed an unqualified opinion on those financial statements"; signature page:184 "Date: February 17, 2026".
- Content located: long-term debt note and covenants at page:144 to page:149 (Note 8), guarantees at page:150 (Note 9), segment information at page:173 (Note 23) and the subsequent-event note at page:175 (Note 25).
- Perimeter: consolidated Tenet Healthcare Corporation and subsidiaries, including noncontrolling interests. Units are USD millions unless stated.
- Version relationship: the oldest of the three filing families. It controls FY2025 and December 31, 2025 facts, and it is the only supplied source that prints the covenant text, the credit agreement terms and the maturity ladder as of December 31, 2025.

#### Forms 10-Q for Q1, Q2 and Q3 2026

- Family and authority: filed, unaudited condensed reports. Each is separate and active; none replaces another. Period and signature evidence: the Q1 report is for the "quarterly period ended March 31, 2026" (page:1) and is dated "Date: April 30, 2026" (page:50); the Q2 report is for the "quarterly period ended June 30, 2026" (page:1) and is dated "Date: July 29, 2026" (page:57); the Q3 report is for the "quarterly period ended September 30, 2026" (page:1) and is dated "Date: October 29, 2026" (page:54).
- Q3 report (`10-Q_2026-09-30_thc-20260930.htm.jsonl`) is the latest and controls the September 30, 2026 balance sheet (page:2), nine-month statements of operations (page:2 and page:3), nine-month cash flows (page:3 and page:4), Note 5 debt (page:12 and page:13), segment note (page:24 and page:25), liquidity (page:49 to page:51) and the market-risk maturity table (page:52).
- Q1 and Q2 reports (`10-Q_2026-03-31_thc-20260331.htm.jsonl`, `10-Q_2026-06-30_thc-20260630.htm.jsonl`) supply the earlier 2026 quarter ends, the three-month and six-month comparisons and the debt note at each date (page:12 and page:13 in each). They are needed for any discrete Q2 or Q3 cash-flow derivation, because cash flows are year-to-date in every 10-Q.
- Basis: unaudited, with interim notes condensed. Page:6 of the Q3 report states that the interim notes omit "certain notes and disclosures that substantially duplicate those in our Annual Report", so covenant detail and some policies are only in the 10-K.

#### Earnings releases (Exhibit 99.1) of April 30, July 23 and October 29, 2026

- Family and authority: issuer press releases furnished as Exhibit 99.1; management-prepared, unaudited, with non-GAAP measures. They are attributed management claims, not filed-statement authority. Dates: "DALLAS — April 30, 2026" (page:1 of the first), "DALLAS — July 23, 2026" (page:1 of the second) and the October release (`EX-99.1_2026-10-29_thc-20260930ex991earningsr.htm.jsonl`) which opens "Tenet Reports Strong Third Quarter 2026 Results; Raises 2026 Financial Outlook" (page:1).
- What they add beyond the 10-Qs: Adjusted EBITDA definition and reconciliations (page:8 to page:15 of the October release), full-year Outlook (page:4 and page:5), adjusted free cash flow, and the net-debt-to-Adjusted-EBITDA ratio quoted on page:2.
- Version relationship: statement-of-operations figures repeat the 10-Q. The 10-Q controls those facts; the release is not independent corroboration of them.

#### Context (`context`)

- Run settings only. Ratings, quotes, deal terms, guarantors, borrower, parent, sponsor, peers and research questions are blank. A blank is not zero and not evidence of absence.

### Information-availability boundary

- Latest issuer document: the October 29, 2026 release and the 10-Q signed "Date: October 29, 2026" (page:54). Nothing is dated later in the pack.
- Cover-page share count is stated as of October 23, 2026 (page:1 of the Q3 report).
- The cutoff is November 5, 2026. Events between October 29, 2026 and the cutoff are Not supplied, not absent.
- The release says a "slide presentation associated with the webcast" and a supplemental financial disclosures document were to be posted on the company website (October release, page:5). Neither is in the pack.

### Identity and perimeter

- Reporting entity: Tenet Healthcare Corporation, a Nevada corporation, Commission File Number 1-7293, with common stock and "6.875% Senior Notes due 2031" listed (Q3 10-Q, page:1). Statements are consolidated with subsidiaries.
- Operating segments: Hospital Operations and Services, and Ambulatory Care (USPI Holding Company, Inc. and subsidiaries), per Note 1 (Q3 10-Q, page:5). Conifer Health Solutions, LLC was owned 76.2 percent at December 31, 2025 and wholly owned at September 30, 2026 (same page).
- Debt issuer: Tenet Healthcare Corporation. Secured notes are guaranteed by "certain of our wholly owned domestic hospital company subsidiaries" (10-K, page:145). The revolver obligations are "guaranteed by certain of our domestic wholly owned subsidiaries" (10-K, page:147). The guarantor list, restricted-group definition and any guarantor-level financial information are not supplied. Unresolved: whether the unsecured notes carry subsidiary guarantees is not stated in the located debt text.
- Noncontrolling interests are material to the perimeter: redeemable noncontrolling interests of $2,179 million and noncontrolling interests of $1,971 million at September 30, 2026 (Q3 10-Q, page:2). Consolidated debt, earnings and Adjusted EBITDA are before noncontrolling holders' shares; consumers must not treat consolidated Adjusted EBITDA as available to the issuer's creditors without that caveat.
- Currency and units: USD; the Q3 report states amounts are "expressed in millions (except per‑share amounts)" except where noted. The context currency matches the sources.

### Version relationships and conflicts

- Three quarterly reports, one annual report and three releases are distinct dated documents. None is a duplicate, draft or amendment. No unsigned or draft material is present.
- Presentation difference, not a conflict: revenue from contract termination is a separate line on the statement of operations (Q3 10-Q, page:2: "Revenue from contract termination 646 — 1,472 —"), while the release says the outlook for net operating revenues excludes it (October release, page:4: "Contract termination revenue recognized from the early conclusion of the RCM Agreements is not included in net operating revenues"). Consumers must keep the two revenue lines separate.
- Basis difference, not a conflict: the debt note total (Q3 10-Q page:12, "Total long-term debt 13,243 13,171") and the market-risk table total (page:52, "Fixed-rate long-term debt $ 27 $ 157 $ 1,931 $ 1,464 $ 3,493 $ 6,269 $ 13,341 $ 12,886") are stated on different bases; the market-risk table states that "unamortized discounts and issue costs are excluded from the table". The 10-K ladder (page:149) includes finance lease obligations. A consumer must not mix the three totals.
- Management claim versus filing: the net-debt-to-Adjusted-EBITDA ratio (October release, page:2: "was 2.11x at September 30, 2026 compared to 2.33x at June 30, 2026 and 2.25x at December 31, 2025") is a management claim. No filed statement or release table supplies a net-debt figure or definition for it. The release's one use of the term is that sentence.
- Adjusted EBITDA includes a $147 million favorable net effect in Q3 2026 that the release attributes to transition activities and a timing adjustment (October release, page:2: "resulted in a favorable net impact to Adjusted EBITDA of $147 million in the third quarter of 2026"). Management attribution; the filed 10-Q segment note (page:24) reproduces the reported Adjusted EBITDA but not that split.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, debt, liquidity, non-GAAP, cash flows | 10-K page:144 to page:149; Q3 10-Q page:2 to page:4, page:12, page:13, page:24, page:25, page:49 to page:52; October release page:8 to page:15 | Cash flows are year-to-date; net debt not supplied; LTM must be built from FY2025 and nine-month columns; contract-termination revenue and Adjusted EBITDA definitions differ from GAAP lines |
| CP-1A | Business, segments, ownership, transaction history | Q3 10-Q page:5, page:10, page:13; 10-K page:175 (Note 25); October release page:2 to page:4 | Omnibus Agreement, 8-K of February 2, 2026 and new indenture not supplied; no investor presentation |
| CP-2 | CP-1 and CP-1A outputs; covenants; liquidity; refinancing | 10-K page:147 to page:149; Q3 10-Q page:13, page:50, page:51 | Covenant definitions and compliance certificates not supplied; the quarterly report states only that the company was in compliance |
| CP-5 | Traceable claims | All seven filings have chunk locators | No original HTML or XBRL; printed page labels differ from chunk numbers |

### Analytical read-through

- Usable coverage: the audited FY2025 statements and the September 30, 2026 interim statements give a consistent filed base, and the three releases give management's adjusted measures and outlook. The debt note lists each series at December 31, 2025 and September 30, 2026, so the maturity profile and the September 2026 refinancing can be traced to filed text.
- Strongest contrary evidence and limits: the Q3 operating result includes a large separately stated contract-termination revenue line, and the company's Adjusted EBITDA is built to exclude it while including a transition and timing benefit. The set does not let a consumer test management's split. The release outlook (October release, page:4) is forward-looking management guidance, not filed evidence.
- Source risk mechanism: evidence of a one-time CommonSpirit consideration (Q3 10-Q page:5, "CHI’s payment to us of an aggregate amount equal to $1.900 billion in annual installments over the next three years") sits beside ordinary hospital and ambulatory revenue. The risk is a consumer capitalising the consideration as recurring earnings or ignoring the receivable (page:10: "The CHI Note Receivable requires three annual payments of approximately $453 million"). The downstream consequence is distorted leverage, coverage and cash conversion unless CP-1 keeps the lines apart.
- Second mechanism: the interim report states compliance but not the test levels (Q3 10-Q page:51: "with all such applicable covenants and conditions at September 30, 2026"). The test levels appear only in the annual report (10-K page:148, "effective maximum secured debt covenant of 4.25 to 1.00"; page:149, "a minimum fixed charge coverage ratio to be met if the designated excess availability under the revolving credit facility falls below $150 million"). A consumer must date them to December 31, 2025 and flag that amendments after that date are not visible.
- Liquidity inputs are located: cash (Q3 10-Q page:2), revolver availability and letters of credit (page:13: "we had no cash borrowings and less than $1 million of standby letters of credit outstanding under the Credit Agreement" and "we had $105 million of standby letters of credit outstanding under the LC Facility"), and the springing maturity in the annual report (10-K page:147). CP-1 must treat the borrowing base as availability, not commitment.
- What cannot proceed: legal interpretation of covenants or change-of-control terms, guarantor-level or structural-subordination analysis, ratings or market-based relative value, post-October 29, 2026 monitoring, and any check of the slide deck or supplemental disclosures.
- Next evidence action: supply the 2025 Credit Agreement, the LC Facility, the Forty-Third Supplemental Indenture and the other current indentures, the 8-K filings of September 22, 2026 and February 2, 2026, the Omnibus Agreement, the supplemental financial disclosures and slide deck, and any filing or release dated October 30 to November 5, 2026.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Every number above is a located quotation from a source and is not derived.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed 2025 Credit Agreement, LC Facility and indentures not supplied; the exhibit list cites a Forty-Third Supplemental Indenture dated September 22, 2026 (Q3 10-Q page:53) | High for legal work; Medium for CP-2 | CP-2, CP-5 | Supply the executed documents or the exhibits to the cited 8-K |
| Covenant test levels printed only in the 10-K (December 31, 2025); no compliance certificate or headroom figure | Medium | CP-1, CP-2 | Supply credit agreement and any amendment; treat test levels as dated December 31, 2025 |
| Net debt used for the reported ratio is neither defined nor tabulated in any supplied source | Medium | CP-1, CP-2, CP-5 | Supply the release supplemental disclosures or the 8-K tables; until then label the ratio as management's |
| Omnibus Agreement and the 8-K of February 2, 2026 are not supplied; only the 10-Q and release summaries | Medium | CP-1A, CP-2 | Supply the 8-K and exhibits |
| Slide presentation and supplemental financial disclosures referenced by the October release are not supplied | Low to Medium | CP-1A, CP-2 | Supply the decks; until then no deck or chart coverage is claimed |
| Events from October 30, 2026 to the cutoff are Not supplied | Medium | CP-1A, CP-2 | Supply later 8-Ks or confirm none |
| Guarantor list, restricted-group definition and guarantor-level financial information not supplied; guarantee status of the unsecured notes is not stated in the located text | Medium | CP-2 | Supply the indentures and any condensed guarantor information |
| Text conversion only; no original HTML or XBRL; tables are flattened | Low | CP-1, CP-5 | Check flagged tables against the filed HTML when available |
| No ratings, market prices, peer data or valuation inputs (context blanks) | Low for the selected modules | CP-2 | Not required for this scope; keep Not supplied |
| 2026 proxy statement and governance disclosures not supplied | Low | CP-1A | Supply if governance detail is required |

## Next module

- CP-1: use the 10-K and the Q3 10-Q as controlling for statements; keep debt, finance leases, redeemable noncontrolling interests and the CHI Note Receivable separate; keep annual, three-month and nine-month columns separate and derive discrete quarters from the year-to-date cash flows only with both periods cited; label Adjusted EBITDA, adjusted free cash flow and net-debt ratio as management non-GAAP; keep revenue from contract termination apart from net operating revenues.
- CP-1A: carry the CommonSpirit Omnibus Agreement, the Conifer redemption and the September 2026 refinancing as the central transactions; label material after October 29, 2026 as Not supplied.
- CP-2 and CP-5: carry the missing executed documents, the net-debt gap and the dating of the covenant text as restrictions; do not claim covenant headroom or guarantor coverage.
