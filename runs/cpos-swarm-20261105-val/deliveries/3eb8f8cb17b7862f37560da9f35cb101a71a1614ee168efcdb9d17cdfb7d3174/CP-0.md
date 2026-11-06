# CP-0 — Source readiness: Valaris Ltd (val)

## Request

- Issuer: Valaris Ltd (issuer id `val`; the filings name the registrant "Valaris Limited", ticker VAL, Bermuda), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026; prior period FY2025.
- Run: `val-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The analyst read the pinned files and wrote this answer. No provider was called.
- Question: can the supplied public filings support the four consumers, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion. No figure is normalized, reconciled or calculated here.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_val-20251231.htm.jsonl | b0f40796936a513fe6362c5f87d6a2a2819cd2f6e423112bfcf4a7c94647ac50 | Annual report on Form 10-K, fiscal year ended December 31, 2025 (163 pages) |
| 10-Q_2026-03-31_val-20260331.htm.jsonl | 856b19f20ceb9a456e4cf71dc5d1f96d12072575504148e1684cf5301164037f | Quarterly report on Form 10-Q, quarter ended March 31, 2026 (53 pages) |
| 10-Q_2026-06-30_val-20260630.htm.jsonl | d045ec4aa0f0c5450f1ffc05520139072532c8f88ec1804bd561ac63d9d380b7 | Quarterly report on Form 10-Q, quarter ended June 30, 2026 (57 pages) |
| 10-Q_2026-09-30_val-20260930.htm.jsonl | 73a1a96ecd1c9340e41638f2528ea86ae030d4c896022c1e422144610c8461ec | Quarterly report on Form 10-Q, quarter ended September 30, 2026 (62 pages) |
| EX-99.1_2026-05-04_a03312026ex991pressrelease.htm.jsonl | fb13914842f3e3a58a0b5ccdbd3cb04d0eb99161ae6d4b18bdfd3afa295e84b5 | Exhibit 99.1 earnings release dated May 4, 2026 (17 pages) |
| EX-99.1_2026-08-05_a06302026ex991pressrelease.htm.jsonl | 21077052c215c76afaa6a29e3ea89e20e01ee6140be558608fa94290eaa87b1f | Exhibit 99.1 earnings release dated August 5, 2026 (17 pages) |
| EX-99.1_2026-11-02_a09302026ex991pressrelease.htm.jsonl | 649e9df09c58fc28e42170873dd9e204e4698e7b6a16ba8868ab909251dcc271 | Exhibit 99.1 earnings release dated November 2, 2026 (18 pages) |
| context | 630c8480b8c6896f51051152fc8ca75c81e04a78fc5ea8aebca9a62a14a6fd8f | User run settings; not issuer evidence |

Supplied handoffs: none (CP-0 is the first module). Locators are `page:N`, the source chunk number in the pinned `.jsonl` file, not the printed page. Each file opens with a line giving the sha256 of the underlying HTML; the hashes above are those of the pinned `.jsonl` files and are the ones CP-OS checks.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings are enough for a financial base view, a business and transaction view, a credit synthesis and an evidence trace, each with stated limits. The pending Transocean combination is the central transaction. | Medium | Covenant levels, ratings, executed debt documents, the combination agreement and ARO's own statements are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited FY2025 statements and three 2026 interim filings with matching earnings releases are located, with quarterly columns through Q3 2026. | Supports a last-twelve-months and quarterly credit view on a consolidated basis. | High |
| Debt is one 8.375% second lien note series due 2030 plus an undrawn $375.0 million revolver maturing 2028. | Debt terms are limited to two instruments, but guarantor and collateral detail rests on filing summaries only. | Medium |
| The revolver has three financial covenants, but no test level or reported figure is printed. | Covenant headroom cannot be assessed from these sources. | High |
| The pending Transocean combination changes ownership; the notes carry change-of-control terms, and whether the combination triggers them is not stated. | Post-closing credit profile and note treatment are not supplied; analysis stays standalone. | Medium |
| ARO is an unconsolidated 50/50 joint venture with notes receivable and possible capital calls; only summary disclosure is supplied. | ARO exposure can be sized from Valaris's disclosure but not tested against ARO's own accounts. | Medium |

### Readiness view

All four selected consumers are READY_WITH_LIMITATIONS. None is CONDITIONAL or BLOCKED, because each owner can perform its method on located, dated filings. The limitations are bounded gaps, not missing identity or period evidence. The perimeter is consolidated Valaris Limited and subsidiaries, with ARO accounted for under the equity method. The latest evidence is the Q3 2026 earnings release (November 2, 2026) and the Q3 2026 Form 10-Q (signed November 3, 2026), both before the cutoff. Nothing dated after the cutoff is supplied or used. Readiness here covers source sufficiency only; it does not say the downstream analysis is complete.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 (financial base view) | READY_WITH_LIMITATIONS | FY2025 audited statements (10-K page:105 to page:107) and Q3 2026 condensed statements (10-Q Q3 page:8 to page:10) are located. The Q3 release gives five discrete quarters (page:8 to page:11). Segment, backlog, utilization and debt text are located. Facility-level carrying values for the revolver are not needed: no amount is outstanding. Text extraction flattens tables. |
| CP-1A (business and transaction) | READY_WITH_LIMITATIONS | Business, segments, customers, the Transocean Business Combination Agreement, ARO and fleet actions are located (10-K page:8, page:76, page:155; 10-Q Q3 page:11, page:12, page:32). The agreement itself, a proxy or scheme document and later 8-Ks are not supplied. |
| CP-2 (credit synthesis) | READY_WITH_LIMITATIONS | Liquidity, debt, maturity, commitments and the covenant categories are located (10-Q Q3 page:51 to page:56; 10-K page:127 to page:129). Covenant levels, ratings and market prices are not supplied. |
| CP-5 (evidence trace) | READY_WITH_LIMITATIONS | Every source has stable page chunks, so claims can be traced. The original HTML, charts and images are not inspected. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source register

#### Form 10-K for FY2025 (`10-K_2025-12-31_val-20251231.htm.jsonl`)

- Family and authority: filed annual report, original authority for audited consolidated statements. page:1: "FORM 10-K", "For the fiscal year ended December 31, 2025", "Commission File Number 1-8097", "Valaris Limited". Signed February 20, 2026 (page:163). The Q3 10-Q (page:11) confirms the 10-K was "filed with the SEC on February 20, 2026".
- Audit: KPMG LLP (page:102, page:104, page:105); page:104 contains "served as the Company's auditor since".
- Statements located: balance sheet page:106, statements of operations page:105, cash flows page:107. Debt note from page:127 (2030 Second Lien Notes), page:128 (indenture covenants, 2028 Credit Agreement security), page:129 (revolver pricing, financial covenants). Fair values page:124. Contractual obligations page:91. Letters of credit page:93. Backlog page:76. ARO notes page:121 to page:124.
- Units: USD millions unless stated. Perimeter: consolidated Valaris Limited and subsidiaries; ARO is a variable interest entity that Valaris does not consolidate (page:122).

#### Forms 10-Q for Q1, Q2 and Q3 2026

- Q1 (`10-Q_2026-03-31_val-20260331.htm.jsonl`): "For the quarterly period ended March 31, 2026"; signed May 5, 2026 (page:53). Unaudited condensed statements (balance sheet page:9). Debt and revolver text page:19 to page:20.
- Q2 (`10-Q_2026-06-30_val-20260630.htm.jsonl`): "For the quarterly period ended June 30, 2026"; signed August 6, 2026 (page:57). Letters of credit text page:24 and page:51.
- Q3 (`10-Q_2026-09-30_val-20260930.htm.jsonl`): "For the quarterly period ended September 30, 2026"; signed November 3, 2026 (page:62). Statements page:8 to page:10; business combination page:11 to page:12 and page:32; debt page:21 to page:22; contingencies page:26; supplemental balances page:29 to page:30; liquidity page:51 to page:56. "As of October 29, 2026, there were 69,443,058 Common Shares of the registrant outstanding" (page:1).
- Authority: filed, unaudited, controlling for statement facts of their periods. The Q3 10-Q shows a three-month and nine-month column for 2026 and 2025, so quarter and year-to-date figures can be kept apart.
- Version relationship: the Q3 10-Q (page:11) says certain previously reported amounts "have been reclassified to conform to the current year presentation". Where the FY2025 comparatives differ from the 10-K, the 10-K remains the original audited source and the difference must be logged downstream, not smoothed.

#### Earnings releases (Exhibit 99.1)

- Dates: May 4, 2026 (`EX-99.1_2026-05-04_...`), August 5, 2026 (`EX-99.1_2026-08-05_...`), November 2, 2026 (`EX-99.1_2026-11-02_...`; page:1 "Hamilton, Bermuda, November 2, 2026").
- Authority: management-prepared, unaudited. They carry reported statements, segment Adjusted EBITDA (Q3 release page:10 to page:11, with the definition of Adjusted EBITDA in its footnote), backlog (page:11), average daily revenue, utilization and management narrative. Management narrative and backlog are attributed management claims, not audited facts.
- Version relationship: the Q3 release repeats statement figures that also appear in the Q3 10-Q (for example revenues, net income, cash and cash equivalents). Treat the 10-Q as controlling for statement facts and do not count the release as independent corroboration. The release alone supplies Adjusted EBITDA, backlog and five-quarter trends.
- The Q3 release (page:5) states that Valaris "does not intend to hold future earnings conference calls or provide updates to forward-looking guidance". No current guidance is therefore available beyond the capital expenditure range in the 10-Q (page:52).

### Information-availability boundary

- Every issuer document is dated on or before November 3, 2026, before the cutoff of 2026-11-05.
- Forward dates in the Q3 10-Q (shareholder meetings on November 24, 2026, court hearing on November 26, 2026, expected closing on or about December 1, 2026; page:12) are labelled issuer expectations, not events.
- Nothing dated between November 3, 2026 and the cutoff is supplied. Events in that window are Not supplied, not absent.

### Identity and perimeter

- Reporting entity: Valaris Limited, incorporated in Bermuda, NYSE common shares and warrants (page:1 of each filing); the Q3 release (page:5) calls it "a Bermuda exempted company limited by shares". The context leaves borrower, parent, guarantors and sponsor blank. That is not evidence that none exist.
- Debt issuers: "the Company and Valaris Finance Company LLC" ("Valaris Finance"), a wholly-owned subsidiary, issued the 2030 Second Lien Notes (10-Q Q3 page:21). The notes are guaranteed "by certain subsidiaries of the Company". The revolver is guaranteed by Valaris Finance and certain other subsidiaries (10-Q Q3 page:21; 10-K page:128). The guarantor list itself is not supplied.
- Pending acquirer: Transocean Ltd., a Swiss corporation, under a Business Combination Agreement dated February 9, 2026 (10-Q Q3 page:11). Valaris is the target. Transocean's own financial statements are not supplied.
- Unconsolidated affiliate: ARO Drilling, a 50/50 joint venture with Saudi Aramco, equity method (10-K page:122). Valaris holds notes receivable from ARO, leases rigs to ARO and may be asked for capital (10-Q Q3 page:54 to page:56). Operating results of ARO appear in the segment table as a reconciling item, so ARO segment figures are 100 percent of ARO and are not part of consolidated results (Q3 release page:4, footnote 1).
- Currency and units: USD, in millions, in the filings. No other currency is the reporting currency. A Malaysian assessment is stated in MYR with a dollar conversion (10-Q Q3 page:56).

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, discrete quarters, segments, debt, cash flow, Adjusted EBITDA | 10-K page:105 to page:107, page:127 to page:129; 10-Q Q3 page:8 to page:10, page:21 to page:22, page:51 to page:53; Q3 release page:8 to page:11 | Adjusted EBITDA is a company definition; one debt series, so no facility table beyond the notes and revolver; ARO shown as equity method |
| CP-1A | Business, fleet, customers, transaction, ARO, history | 10-K page:8, page:76; 10-Q Q3 page:11, page:12, page:29 to page:32; Q3 release page:1 to page:3 | Business Combination Agreement, scheme documents and later 8-Ks not supplied; ARO's own statements not supplied |
| CP-2 | CP-1 and CP-1A outputs; liquidity, covenants, commitments, claims outside debt | 10-Q Q3 page:26, page:29, page:51 to page:56; 10-K page:91, page:93, page:128 to page:129 | Covenant levels and ratings not supplied; Notes Receivable from ARO is an asset, not debt |
| CP-5 | Traceable claims | All seven sources have page chunks | Original HTML, charts and tables as filed are not inspected |

### Analytical read-through

- Usable coverage: seven dated filings span the FY2025 audited year and each 2026 quarter. Together they support a reported financial foundation, a last-twelve-months view from the Q3 release's discrete quarters, and a debt and liquidity description of a capital structure that has one note series and one undrawn revolver.
- Strongest contrary evidence: the pending Business Combination (10-Q Q3 page:11 to page:12) can change ownership, covenant treatment and the debt structure. The 10-K (page:127) says that on a "Change of Control Triggering Event" the issuers "may be required to make an offer to repurchase" the notes at "101.0%" of principal. The supplied set does not say whether that event is triggered by the Transocean transaction. It also does not give the combination financing, Transocean's capital structure or the post-closing group.
- Source risk mechanism: the revolver's "financial covenants that require us to maintain (i) a minimum book value of equity to total assets ratio, (ii) a minimum interest coverage ratio and (iii) a minimum amount of liquidity" (10-K page:129) carry no printed level, so a consumer cannot compute headroom and must not infer a pass from the statement that the company is "in compliance in all material respects". Compliance is a management assertion in a filing, not a tested ratio.
- Second mechanism: ARO is outside consolidated debt and earnings. Valaris reports notes receivable from ARO, an investment, lease receivables and payables, a contingent funding commitment for newbuild jackups, and ARO's own revolver and term loan (10-Q Q3 page:54 to page:56). A consumer that reads only consolidated debt omits an exposure that can call on Valaris cash. ARO's statements are not supplied, so the exposure can be described from Valaris's disclosure only.
- Third mechanism: letters of credit and surety bonds sit outside the revolver. The Q3 10-Q (page:26) says none "were issued under the 2028 Credit Agreement". Revolver availability therefore must not be reduced for them without evidence, and must not be assumed unaffected by other conditions on borrowing.
- What cannot proceed: covenant headroom against levels, rating-based pricing, post-closing credit analysis of the combined group, legal interpretation of the indenture and credit agreement, guarantor-level analysis, ARO standalone credit analysis.
- Next evidence action: supply the Business Combination Agreement and any scheme document or proxy, the Indenture dated April 19, 2023 and the 2028 Credit Agreement with covenant definitions, any ratings reports, ARO's financial statements, and any filing dated between November 3, 2026 and the cutoff.

### Debt and liquidity inputs located (no calculation)

- Notes: "$700.0 million" Initial Second Lien Notes (April 2023) and "$400.0 million" Additional Notes (August 2023) form one series, the 2030 Second Lien Notes, 8.375% per annum, maturing April 30, 2030, interest payable April 30 and October 30; issuers the Company and Valaris Finance; secured second lien (10-Q Q3 page:21; 10-K page:127). The 10-K contractual obligations table prints principal due in the "2029 and 2030" column of "1,100.0" and none earlier (10-K page:91).
- Revolver: the 2028 Credit Agreement, commitments of "$375.0 million", maturing April 3, 2028, "$150.0 million sublimit" for letters of credit, "no amounts outstanding" at September 30, 2026 (10-Q Q3 page:21 to page:22). Availability "$375.0 million" as of October 30, 2026 (page:51).
- Balance sheet: cash and cash equivalents $525.1 million and long-term debt $1,088.5 million at September 30, 2026 (10-Q Q3 page:9). No separate debt table is printed in the 10-Q; the carrying amount sits on the face of the balance sheet. The 10-K prints a carrying value of the notes, "$1,086.0", and a fair value, "$1,144.9", at December 31, 2025 (10-K page:124).
- Letters of credit and surety bonds: "$113.7 million", none under the revolver (10-Q Q3 page:26).

### Searches made before recording a gap

- Covenant levels: searched all seven sources for "minimum amount of liquidity", "minimum book value", "interest coverage ratio", "leverage ratio" and "maintenance covenant". Only the 10-K names the three tests (page:129, and a risk factor); the three 10-Qs say only that the company was "in compliance in all material respects". No source prints a threshold or a reported ratio. Recorded as Not supplied.
- Ratings: searched for "Moody", "S&P" and "credit rating". Hits are the pricing grid of the revolver and the pension discount rate; no issuer rating is printed. Recorded as Not supplied. The context `ratings` field is empty.
- Letters of credit: searched "letters of credit" and "surety". The Q3 10-Q (page:26 and page:55) prints $113.7 million of letters of credit and surety bonds, none under the revolver. No gap is recorded on this.
- Liquidity inputs: cash and the undrawn revolver are printed (10-Q Q3 page:51); restricted cash is printed separately (page:30). No gap is recorded on the inputs.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Coverage counts: seven issuer sources plus the context, no supplied handoffs.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Financial covenant levels and reported covenant figures not supplied (three tests named only) | High | CP-2 | Supply the 2028 Credit Agreement and compliance disclosures |
| Business Combination Agreement, scheme document, proxy and combination financing not supplied; effect on the notes and revolver not stated | High | CP-1A, CP-2 | Supply the agreement and any proxy or scheme document |
| Executed Indenture and 2028 Credit Agreement, guarantor list and collateral schedules not supplied | Medium | CP-2 | Supply executed documents |
| Events from November 3, 2026 to the cutoff not supplied | Medium | CP-1A, CP-2 | Supply later 8-Ks or confirm none |
| ARO standalone financial statements not supplied; only Valaris's disclosure | Medium | CP-1, CP-1A, CP-2 | Supply ARO statements if standalone analysis is needed |
| No ratings, market prices or peer data (context fields empty) | Low for the selected modules | CP-2 | Keep Not supplied |
| Adjusted EBITDA and backlog are management measures that appear only in the releases; the 10-Qs and the 10-K print no Adjusted EBITDA, and the release gives a definition and segment rows but no line-by-line bridge from net income | Medium | CP-1, CP-2 | Label as issuer measures; check the release definition |
| Reclassified prior-period amounts (Q3 10-Q page:11) may differ from the 10-K | Low | CP-1, CP-5 | Log any difference found downstream |
| Text extraction only; charts, images and original table layout not inspected | Low | CP-1, CP-5 | Check flagged tables against the filed HTML when available |

## Next module

- CP-1: treat the 10-K and 10-Qs as controlling for statement facts and the releases as issuer presentation. Keep Q3 2026, nine months 2026, FY2025 and last twelve months apart. Keep ARO equity-method figures separate from consolidated figures. Label Adjusted EBITDA as the issuer's non-GAAP measure.
- CP-1A: carry the pending Transocean Business Combination as the central transaction (agreement February 9, 2026; expected closing on or about December 1, 2026; termination fee $173.0 million in specified circumstances; 10-Q Q3 page:12). Label forward dates as expectations and anything after November 3, 2026 as Not supplied.
- CP-2: carry the missing covenant levels, ratings, executed documents and combination financing as restrictions; do not infer covenant headroom.
- CP-5: trace each claim to a page chunk; carry the restrictions above.
