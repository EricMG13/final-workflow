# CP-0 — Source readiness: PRA GROUP INC (praa)

## Request

- Issuer: PRA GROUP INC (issuer id `praa`, ticker PRAA, Delaware, headquartered in Norfolk, Virginia), as-of date 2026-11-05, information cutoff 2026-11-05 (context).
- Run: `praa-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Current period q2-2026, prior period fy-2025, reporting currency USD (context settings, not issuer evidence).
- Requested modules: CP-1, CP-1A, CP-2 and CP-5 (the `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned source files and wrote this answer. No provider was called.
- Question: can the supplied public filings and earnings releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No credit conclusion, legal interpretation or investment opinion is given, and no figure is normalized, reconciled or calculated here. Figures are quoted as printed, with their source page.

## Sources

Locators are `page:N` of the pinned text files, which are source chunks and not printed page numbers. The sha256 values are those CP-OS pins for each file. The "Visible text of ... sha256" line on page 1 of each file is a hash of the original HTML text and is a different value; it is not used as a pin.

### Issuer sources relied on

| Source (exact name) | sha256 | Pages | Role |
| --- | --- | --- | --- |
| 10-K_2025-12-31_praa-20251231.htm.jsonl | acaea144d244584c3474f86549753d209ff125e0c5d293c88092a8b3609d005e | 114 of 114 | Annual report on Form 10-K for the fiscal year ended December 31, 2025 |
| 10-Q_2025-09-30_praa-20250930.htm.jsonl | 929f20928dbfde158b90287ecb3f34f89e93248de03667dc981595cbc1f16f43 | 52 of 52 | Quarterly report on Form 10-Q for the quarter ended September 30, 2025 |
| 10-Q_2026-03-31_praa-20260331.htm.jsonl | 5b8ee1fe62f8b0079ea63a2a1c4f92f69a59ebc645588dbcce6f190c45211b32 | 40 of 40 | Quarterly report on Form 10-Q for the quarter ended March 31, 2026 |
| 10-Q_2026-06-30_praa-20260630.htm.jsonl | d7a354d31f5af038cbd610321c408a92f38ffbe0be4451883080ac13fa2cd5a8 | 49 of 49 | Quarterly report on Form 10-Q for the quarter ended June 30, 2026 |
| EX-99.1_2026-02-26_q42025earningsrelease.htm.jsonl | ac28ac408106b5058aef5a7017ad24c9c2f1059768c1e80795f1a5ba0705218f | 12 of 12 | Exhibit 99.1 earnings release for Q4 and full year 2025, dated February 26, 2026 |
| EX-99.1_2026-05-07_q12026earningsrelease.htm.jsonl | 0cafa2dd16d8fe170df8f95a181353ea848b2d370eaa0bad903e81ca9ab40ac1 | 11 of 11 | Exhibit 99.1 earnings release for Q1 2026, dated May 7, 2026 |
| EX-99.1_2026-08-06_q22026earningsrelease.htm.jsonl | 90c4b9dc1bbbec8846231ce65b511117fe19795284263ee0dc2f0a68914940d4 | 13 of 13 | Exhibit 99.1 earnings release for Q2 2026, dated August 6, 2026 |

### Run settings (not issuer evidence)

| Source | sha256 | Role |
| --- | --- | --- |
| context (1185348-pra-group-inc-praa.json) | fb395d626a32c7d3e686eb338c55b901d79ab38a3782a023f0c732503b0056b3 | Dated user settings for this run. Blank fields (borrower, parent, guarantors, ratings, quotes, deal terms, valuation inputs, research questions) are unknown, not zero. |

CP-OS also lists `_retrieval.json` in the pack folder as ignored. It is not a source and nothing here relies on it.

### Supplied handoffs

None. CP-0 is the first module in this run and receives no upstream handoff.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied filings and releases, through the quarter ended June 30, 2026, support the planned financial, business, synthesis and trace work, with stated limits. Nothing after August 7, 2026 and no executed debt documents are supplied. | Medium | No executed credit agreements or indentures, no reported covenant ratio levels, and nothing dated after the August 2026 filings. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The European revolving facility was amended on April 30, 2026, but the amended agreement is not supplied. | Post-amendment covenant terms and maturity can only be read from summary text, not from the executed terms. | High |
| The filings state covenant compliance but do not print the covenant ratio levels. | Headroom to the stated limits cannot be read from the sources and would be a reader estimate. | High |
| The June 2026 European forecast review raised European ERC by $348.5 million, while the stated income effect on the forecast line is approximately $105 million. | The ERC step-up should not be read as earnings; ERC-based borrowing availability needs care. | Medium |
| The annual maturity table in the 10-K predates the European facility extension. | Maturity-wall work must use the later 10-Q terms, so the 10-K schedule is stale for that facility. | High |

### Readiness view

All four selected consumers are READY_WITH_LIMITATIONS. The effective source set is complete for the filed financial statements, notes, debt and liquidity disclosures, segment data and business description for the year ended December 31, 2025 and the quarter and six months ended June 30, 2026. It is not complete for executed legal terms, covenant calculations, ratings, market data or any event after August 7, 2026. No consumer is CONDITIONAL or BLOCKED, because the missing items bound the analysis and do not prevent any consumer's method from running. This is source sufficiency only; it does not say that downstream analysis is complete or that any downstream input contract is met.

| Consumer | Status | Command sheet | Basis and main limitation |
| --- | --- | --- | --- |
| CP-1 (financial facts) | READY_WITH_LIMITATIONS | RUN | Audited FY2025 and FY2024 statements, Q3 2025, Q1 2026 and Q2 2026 interim statements, facility-level debt and cash paid for interest are located. Tables are flattened text; segment history changed in Q4 2025. |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | RUN | Business, strategy, segments, management change, the European facility amendment and the August 2026 buyback authorization are located. The proxy statement and the 8-K filings are not supplied. |
| CP-2 (credit synthesis) | READY_WITH_LIMITATIONS | RUN | Debt, liquidity, availability and covenant text are located for December 31, 2025 and June 30, 2026. Executed agreements, covenant calculations and ratings are not supplied. |
| CP-5 (evidence trace) | READY_WITH_LIMITATIONS | RUN | Every source has page locators, so claims can be traced. Rendering, charts and original HTML or XBRL cannot be checked. |

### Source register

#### Form 10-K for fiscal 2025 (`10-K_2025-12-31_praa-20251231.htm.jsonl`)

- Family and authority: filed annual report, original authority for audited statements. page:1 "FORM 10-K ... For the fiscal year ended December 31, 2025 ... Commission File Number: 000-50058". Large accelerated filer (page:2).
- Audit: page:68 Ernst & Young LLP report, Richmond, Virginia, March 2, 2026; internal control audit referenced at page:107 and page:108. Signatures dated March 2, 2026 (page:114).
- Statements: balance sheet page:68 (December 31, 2025 and 2024), income statement page:69, cash flows page:71 (includes cash paid for interest), equity page:70. Units: "(in thousands)". USD.
- Debt and liquidity: Note 7 Borrowings from page:86 through page:92, including the facility terms and covenants (page:87 to page:89), senior note terms (page:90 to page:92) and a principal payment table by year (page:86). MD&A liquidity table at page:54 and availability summary at page:40.
- Other: ERC by year and purchase price multiples (page:50 to page:53), forward flow and leases (page:56 and page:57, page:86), goodwill (page:85), derivatives (page:93 to page:95), legal matters and multi-state investigation (page:102 and page:103), segments (page:103 to page:105), exhibit index (page:112 and page:113).
- Part III is incorporated by reference to a proxy statement (page:3). The proxy statement is not supplied.
- Perimeter: PRA Group, Inc. and its subsidiaries, consolidated, with noncontrolling interests (page:68).

#### Form 10-Q for the quarter ended September 30, 2025 (`10-Q_2025-09-30_praa-20250930.htm.jsonl`)

- Family and authority: filed quarterly report, unaudited. page:1 "For the quarterly period ended September 30, 2025".
- Statements: balance sheet page:2, income statement page:3 (three and nine months), cash flows page:6. Note 5 Borrowings page:12 and page:13. Goodwill impairment of the quarter at page:3 and page:12. Segments Note 12 at page:20. Liquidity at page:42 and page:43.
- Use: the only filed source for the Q3 2025 quarter. The Q4 2025 release also carries Q3 2025 quarterly columns (management presentation).
- Signature date not visible in the extracted text (page:52 shows only the officer title). This does not affect period identification, which rests on page:1.

#### Form 10-Q for the quarter ended March 31, 2026 (`10-Q_2026-03-31_praa-20260331.htm.jsonl`)

- Family and authority: filed quarterly report, unaudited, signed May 8, 2026 (page:40). page:1 "For the quarterly period ended March 31, 2026".
- Statements: balance sheet page:2, income statement page:3, cash flows page:4 and page:5. Note 5 Borrowings page:8 and page:9. Liquidity page:32 and page:33. ERC page:28. Segments Note 13 page:14 and page:15.
- Note 15 Subsequent Event (page:17): the European revolving credit facility was amended and restated on April 30, 2026. The Note 5 text on page:9 still gives the earlier maturity and refers forward to this amendment, so the two statements are one dated sequence and not a conflict.

#### Form 10-Q for the quarter ended June 30, 2026 (`10-Q_2026-06-30_praa-20260630.htm.jsonl`)

- Family and authority: filed quarterly report, unaudited, signed August 7, 2026 (page:49). page:1 "For the quarterly period ended June 30, 2026". Shares outstanding as of July 31, 2026 are on the cover.
- Statements: balance sheet page:2, income statement page:3 (three and six months with 2025 comparatives), equity page:4, cash flows page:5 (six months, with cash paid for interest and taxes). Units "(in thousands)". USD.
- Debt: Note 5 Borrowings at page:11, giving credit facility borrowings, each senior note series and the amended European facility terms. Liquidity and availability by facility at page:40 and page:41; borrowings and 12-month cash obligations at page:42.
- Other: Note 2 finance receivables and changes in expected recoveries (page:7 to page:10), derivatives (page:12), commitments (page:17), segments Note 13 (page:17 to page:19), Note 15 subsequent event (page:21), non-GAAP and ERC tables (page:35 to page:40), exhibit index (page:47 and page:48).
- Role: most recent filed statements in the pack and the controlling source for June 30, 2026 balances and for the post-amendment European facility terms stated in the filing.

#### Earnings releases (Exhibit 99.1)

- Q4 and full year 2025, February 26, 2026: headline results page:1, cash collections and purchases by source page:3 and page:4, income statement page:5 and page:6, Adjusted EBITDA and net income reconciliations page:11 and page:12. The release is dated before the 10-K audit report (March 2, 2026), so the 10-K controls for annual statement facts.
- Q1 2026, May 7, 2026: headline results page:1, reconciliations page:10 and page:11. The 10-Q for the same quarter controls for statement facts.
- Q2 2026, August 6, 2026: headline results page:1 to page:3, credit availability page:3, share repurchase page:4, statements page:6 and page:7, Adjusted EBITDA reconciliation for the last twelve months and fiscal 2025 at page:11. The 10-Q controls for statement facts.
- Authority: issuer-prepared, unaudited, furnished. They support attributed management narrative, non-GAAP measures and cash collections and purchases by source. They do not override a filing. They are not independent corroboration of figures that repeat the filings.

### Information-availability boundary and version relationships

- Latest dated source: the Q2 2026 10-Q signed August 7, 2026; the Q2 release is dated August 6, 2026. The as-of date and cutoff are 2026-11-05.
- Nothing dated between August 7, 2026 and the cutoff is supplied. Any 8-K, any report for the quarter ended September 30, 2026 and any financing or rating event in that window are Not supplied. That is not evidence that none exists.
- Subsequent events inside the pack: April 30, 2026 European facility amendment (Q1 10-Q page:17, Q2 10-Q page:11 and page:42) and the August 3, 2026 board approval of a new $150 million share repurchase program (Q2 10-Q page:21, Q2 release page:4).
- Each release and its same-period filing overlap. Retained for statement facts: the filing. Retained for non-GAAP measures not defined in the filing and for cash collections by source: the release, attributed to management.
- Q2 2025 as a discrete reporting period is not supplied as a filing; its comparatives appear in the Q2 2026 10-Q (three and six months columns, page:3) and the Q2 2026 release.
- Comparatives for December 31, 2025 appear in the Q1 and Q2 2026 10-Qs and in the 10-K. Whether any comparative was re-presented between filings has not been tested in CP-0; consumers must compare the same balance across the filings that print it.
- Segments: the 10-K states the business was reorganized from a single operating segment into U.S. and European reportable segments in Q4 2025 and that prior-year disclosures were recast (page:103 and page:104). The Q3 2025 10-Q segment note (page:20) states a single operating segment, so it predates that change, so 2025 segment data differs by basis across filings.

### Identity and perimeter

- Reporting entity: PRA Group, Inc., consolidated with subsidiaries and noncontrolling interests (balance sheet and income statement, Q2 10-Q page:2 and page:3). The context leaves borrower, parent and guarantor fields blank; that is not evidence they are absent.
- Debt instruments and parties as printed: North American credit facility (revolving and term loan) guaranteed by U.S. and Canadian subsidiaries and secured by a first priority lien on substantially all assets (10-K page:87); UK revolving credit facility secured by PRA Group UK Limited assets and certain equity interests (10-K page:88); European revolving credit facility, guaranteed by the Company, secured by equity interests in operating subsidiaries of the named borrowers (10-K page:89); 2028, 2029 and 2030 senior notes issued by the Company with guarantees from domestic restricted subsidiaries (10-K page:90 to page:92); 2032 senior notes issued by PRA Group Europe Holding II S.à r.l. and guaranteed by the Company and domestic restricted subsidiaries (10-K page:90).
- Covenants are written on "the Company's consolidated" ratios (10-K page:87 to page:89). The ratio definitions, the restricted group and any unrestricted subsidiaries are not in the supplied text. Treat as unresolved.
- Currency and units: statements and releases are USD in thousands; the 10-K MD&A and 10-Q MD&A text use millions. Europe is 54.0% of June 30, 2026 ERC (Q2 10-Q page:24) and non-U.S. amounts are translated (for example the 2032 senior notes are denominated in euro, EUR 300.0 million at issuance, 10-K page:90, and shown in USD in the borrowings tables). Constant-currency tables appear in the releases (Q2 release page:2). Balances move with exchange rates.
- Draft versus executed: all supplied documents are filed. No agreement, indenture or amendment is supplied, so no executed-versus-draft question arises for legal terms; they are simply absent.

### Document-level observations bearing on downstream use

- Maturity schedule: the 10-K principal payments table (page:86) is stated as of December 31, 2025 and carries the European facility at its earlier maturity. The Q2 10-Q (page:11, page:42) states the extension from November 23, 2027 to April 30, 2031 and that principal payments on borrowings run from February 2028 through September 2032, apart from quarterly term loan payments. For June 30, 2026 maturity work, the Q2 10-Q controls and the 10-K table must not be reused unadjusted.
- Covenant terms: the 10-K prints covenant tests per facility (page:87 to page:89), including a maximum ERC ratio of 45% on the European facility. The Q2 10-Q (page:11) states that the amendment reduced it to 40%. The Q2 10-Q confirms compliance as of June 30, 2026 (page:11, page:42) but prints no actual ratio level, and refers to the 10-K for facility detail. The Q1 10-Q (page:17) lists the changes "among other modifications" and says the aggregate revolving borrowings available and funding costs remained unchanged. Whether other European covenant terms changed on amendment is not verifiable without the amended agreement, which the Q2 10-Q lists as Exhibit 10.1 filed with that report (page:48) and which is not supplied.
- Availability: availability is printed by facility at December 31, 2025 (10-K page:54), March 31, 2026 (Q1 10-Q page:32) and June 30, 2026 (Q2 10-Q page:40 and page:41). It is split into an amount based on current ERC and an additional amount subject to borrowing base and advance rates. Availability is therefore tied to ERC and to the borrowing base definitions, which are not supplied in full.
- ERC: the European ERC step-up is $348.5 million per the Q2 10-Q (page:24) and approximately $349 million per the Q2 release (page:1), a rounding difference. The Q2 10-Q (page:9) states the positive adjustment to changes in expected future recoveries from the European forecast update was approximately $105 million, with partial offsets in other pools; the total positive adjustment to changes in expected future recoveries for the quarter is $74.2 million (page:9). Headline ERC change and income effect are different measures, and a consumer must carry both.
- Non-GAAP: Adjusted EBITDA is printed by the issuer for the last twelve months ended June 30, 2026 and for fiscal 2025 (Q2 release page:11), and its definition adds back recoveries collected and applied to finance receivables less changes in expected recoveries. It is a management non-GAAP measure, labelled as such in the 10-Q (page:24, page:35). The Q2 10-Q key metrics table (page:25) prints the last twelve months Adjusted EBITDA for both periods behind the stated 9.6% increase; the Q2 release reconciliation (page:11) prints the June 30, 2026 last-twelve-months and fiscal 2025 columns only, so the prior-year reconciliation is not supplied.
- Goodwill: a goodwill impairment of $412,611 thousand is recorded in the quarter ended September 30, 2025 (Q3 10-Q page:3) and carries into fiscal 2025 and the last twelve months. Net loss labels in the Adjusted EBITDA table (Q2 release page:11) refer to those long periods and not to the positive Q2 2026 quarter.
- Legal: the 10-K describes a multi-state Attorneys General investigation open since November 17, 2015 and an accrual for an estimated loss on that matter (page:102 and page:103). The Q2 10-Q states no material developments (page:17). The accrued amount is not stated in those pages.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Annual and interim statements, notes, debt by facility, cash paid for interest, segments, non-GAAP | 10-K page:68 to page:71, page:86 to page:92, page:103 to page:105; Q3 10-Q page:2 to page:6, page:12; Q1 10-Q page:2 to page:5, page:8; Q2 10-Q page:2 to page:5, page:11, page:17 to page:19; releases page:6 and page:11 | Cash flows in the 10-Qs are year-to-date, so a discrete quarter is a derivation from two supplied statements. Segment basis changed in Q4 2025. Text conversion flattens tables. |
| CP-1A | Business model, segments, strategy, management and governance, capital allocation, transactions | 10-K page:6 to page:15, page:35, page:96; Q2 10-Q page:24, page:25, page:42, page:43; Q2 release page:1 to page:4 | Proxy statement (governance and ownership) not supplied. 8-K filings that the exhibit index cites are not supplied. |
| CP-2 | Handoffs from CP-1 and CP-1A, plus covenants, availability, maturities, ERC, lease and commitment text | 10-K page:50 to page:57, page:86 to page:92; Q2 10-Q page:11, page:36 to page:42 | Executed agreements, covenant calculations, ratings, market prices and peers not supplied. |
| CP-5 | Traceable locators for every claim | All seven sources carry page locators | Rendering, charts, original HTML and XBRL cannot be inspected; the check is of text only. |

### Analytical read-through

- Usable coverage: seven filed or furnished documents, every page retained, cover the audited year ended December 31, 2025 and interim periods to June 30, 2026. Facility-level borrowings, availability and senior note terms are printed for December 31, 2025 and June 30, 2026, with March 31, 2026 in the Q1 10-Q. Cash paid for interest is printed in the 10-K and the 2026 10-Qs.
- Strongest contrary evidence: the covenants and the borrowing base depend on definitions in agreements that are not supplied, and the European facility was amended after the 10-K. The filings assert compliance but print no ratio levels, so headroom is not observable in the sources.
- Source risk mechanism: availability is partly "based on current ERC" and ERC rose by $348.5 million through a forecast revision in the quarter ended June 30, 2026. A consumer that treats ERC-based availability or the earnings effect as equally firm as cash collected would overstate certainty, because the revision is a management estimate (Q2 10-Q page:9).
- What cannot proceed: covenant headroom against agreement definitions, guarantor-level analysis, legal terms of the notes beyond the 10-K summaries, ratings analysis, valuation against market prices, and any assessment of events after August 7, 2026.
- Next evidence action: supply the Second Amended and Restated European credit agreement (Q2 10-Q Exhibit 10.1), the North American and UK credit agreements, the four indentures listed at Q2 10-Q page:48, any 8-K filed after the Q2 10-Q, and any report for the quarter ended September 30, 2026 that exists before the cutoff.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Every figure above is quoted as printed in the cited page, and the stated rounding relationship between $348.5 million and approximately $349 million is the issuer's own.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Amended European revolving credit agreement and the other credit agreements not supplied | High for legal and covenant work; Medium for synthesis | CP-2 | Supply Exhibit 10.1 of the Q2 10-Q and the North American and UK agreements |
| Indentures for the 2028, 2029, 2030 and 2032 senior notes not supplied | Medium | CP-2 | Supply the four indentures listed at Q2 10-Q page:48 |
| Actual covenant ratio levels not printed; only compliance statements | High | CP-2 | Supply compliance certificates or issuer disclosure of ratio levels; otherwise keep Not supplied |
| Covenant and borrowing base definitions (consolidated EBITDA, fixed charge coverage, ERC ratio, restricted group) not supplied | High | CP-2 | Supply the executed agreements |
| Events after August 7, 2026 (8-Ks, the report for the quarter ended September 30, 2026 if filed, financing, rating actions) not supplied | Medium | CP-1A, CP-2 | Supply later filings or confirm none |
| Q2 2025 filing and the prior-year last-twelve-months Adjusted EBITDA reconciliation not supplied (only the metric is printed, Q2 10-Q page:25) | Low | CP-1 | Use the comparatives in the Q2 2026 10-Q; do not build the prior reconciliation |
| Proxy statement for the 2026 annual meeting (Part III, governance, ownership) not supplied | Low | CP-1A | Supply if governance detail is needed |
| Quarterly earnings presentation slides referenced by the Q2 release not supplied | Low | CP-1A | Not required for the selected scope |
| No credit ratings, market prices, peer data or valuation inputs | Low for the selected modules | CP-2 | Keep Not supplied; context fields are blank |
| Accrued amount for the multi-state Attorneys General matter not stated in the 10-K contingencies note (page:102 and page:103) | Low to Medium | CP-2 | Keep Not supplied unless a supplied source states it |
| Text conversions only; original HTML, XBRL and charts not supplied | Low | CP-1, CP-5 | Check flagged tables against the filed HTML when available |
| Segment basis differs across 2025 filings (single segment before Q4 2025) | Medium | CP-1 | Use recast comparatives in the 2026 filings and label the basis |

## Next module

- CP-1: use the 10-K and the 10-Qs as controlling for statement facts; keep annual, quarterly and year-to-date columns separate; keep credit facility borrowings, each senior note series and unamortized premium and issuance costs separate; use the Q2 10-Q for June 30, 2026 maturities of the European facility and not the 10-K principal payment table; label the Adjusted EBITDA, Adjusted net income and cash efficiency measures as issuer non-GAAP.
- CP-1A: carry the April 30, 2026 European facility amendment, the Q4 2025 segment reorganization, the PRA 3.0 strategy and the August 3, 2026 buyback authorization as dated events; label anything after August 7, 2026 as Not supplied.
- CP-2 and CP-5: carry the missing executed agreements, the missing covenant ratio levels and the difference between the $348.5 million ERC step-up and its approximately $105 million forecast-line effect as restrictions; do not present compliance statements as measured headroom.
