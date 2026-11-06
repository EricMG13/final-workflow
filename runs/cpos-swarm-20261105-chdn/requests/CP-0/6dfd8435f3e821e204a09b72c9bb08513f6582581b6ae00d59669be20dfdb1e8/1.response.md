## Request

Churchill Downs Incorporated (context name: Churchill Downs Inc, issuer id chdn, ticker CHDN), as of 2026-11-05, evidence cutoff 2026-11-05. Pathway: credit_snapshot. Reporting currency per context: USD. Current period per context: q3-2026; prior period: fy-2025. Requested downstream modules: CP-1, CP-1A, CP-2, CP-5.

Question answered here: can the seven pinned filings and earnings releases support those modules, and what remains blocked. This is a source-readiness review. It gives no credit conclusion, performs no normalization and calculates no figures. The context file carries no borrower, parent, guarantor, rating, quote or deal-term inputs (`"borrower_name": ""`, `"guarantors": []`, `"ratings": []`), so none of those roles can be taken from the context.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-12-31_chdn-20251231.htm.jsonl | 791973148b4d2826daf79f6e0ecd898b524ba905f6928d4b1fa58e745cfa58e6 | Audited annual report on Form 10-K, filed financial statements; controlling for FY2025 facts | Fiscal year ended December 31, 2025; consolidated; USD millions with one decimal |
| 10-Q_2026-03-31_chdn-20260331.htm.jsonl | 3d979cd66a5fd3c2d7447c580ef853c0c5a7867f89e2461cd6b817f9d370c641 | Unaudited quarterly report on Form 10-Q, filed | Quarter ended March 31, 2026; consolidated; USD whole millions |
| 10-Q_2026-06-30_chdn-20260630.htm.jsonl | 4eca3b557126cb1eb2e1c2c8c7ed3827f930ac9e114b1865fffc6dfad00959f1 | Unaudited quarterly report on Form 10-Q, filed | Quarter and six months ended June 30, 2026; consolidated; USD whole millions |
| 10-Q_2026-09-30_chdn-20260930.htm.jsonl | 7fff97ce9977f2b2156048dbf8e8996f9058aaa73d34344c7b548ba853ea7229 | Unaudited quarterly report on Form 10-Q, filed | Quarter and nine months ended September 30, 2026; consolidated; USD whole millions |
| EX-99.1_2026-04-22_ex991pressrelease04-22x26.htm.jsonl | bbdcb62a4845e34e0fdd4338c48e18f02c4eceb2b21c6ecefed1bd7b13c21521 | Earnings release (Exhibit 99.1); management attribution, non-GAAP reconciliations | First quarter 2026 |
| EX-99.1_2026-07-29_ex991pressrelease07-29x26.htm.jsonl | 85b22b14ac2149df8072938d3dbc3e8d85579a1e2355ea8fce27bcd305c203d4 | Earnings release (Exhibit 99.1); management attribution | Second quarter 2026 |
| EX-99.1_2026-10-28_ex991pressrelease10-28x26.htm.jsonl | ecea350f3f38425e2e2322d4e7d883986fb7f745d76fde798f61a64ba8bc0e4f | Earnings release (Exhibit 99.1); management attribution | Third quarter 2026 |

The context file (sha256 7c4f52e55b5e23c0fba0c45fbf91c794297fbfceecf1db4e9e336166f978aca8) holds the user's dated settings. It is not issuer evidence and was not used for any issuer fact. The file `_retrieval.json` in the pack folder was ignored by the launcher and was not read.

Hash note: each source's first chunk begins with a line of the form "Visible text of ... htm, sha256 ...". That inner hash is of the original HTML and differs from the sha256 of the pinned text file listed above. The pinned text-file sha256 is the identity used in this handoff; the inner hash is not independently checked.

### Supplied handoffs

None. CP-0 is the first module and CP-OS supplied no upstream handoff (the request lists `"handoffs": {}`).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases are enough to start the requested credit work, using the latest quarterly report as the anchor. Executed financing documents and current covenant figures are not in the set. | Medium | Latest covenant levels, the amended credit agreement and the note indentures are not supplied, so legal terms rest on summaries in the filings. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Facility-by-facility debt, maturities, interest terms and revolver availability are printed in the latest quarterly report. | Capital structure and liquidity work can be anchored on filed figures. | High |
| Covenant test levels and the reported ratios appear only in the annual report, as of year-end 2025. | Current covenant headroom cannot be read from the sources; it stays a gap. | Medium |
| Executed credit agreement, amendments and indentures are absent; only summaries and an exhibit list are supplied. | Guarantor, collateral and springing-maturity terms cannot be verified against executed documents. | Medium |
| No investor presentations are supplied; the quarterly earnings releases stand in. | Management claims are available but remain attributed claims, not filing facts. | Medium |

### Readiness view

The effective source set supports a credit snapshot on the consolidated Churchill Downs Incorporated perimeter. The annual report and three quarterly reports are filed statements and control over the releases. The set is READY_WITH_LIMITATIONS for the requested modules: the owner of each module can perform its method, with bounded gaps on covenants, executed legal terms, guarantor and restricted-group perimeter, and management guidance. No source is blocked, and no missing downstream handoff is treated as a source condition. This view concerns source sufficiency only (SOURCE_SUFFICIENCY_ONLY); it does not evaluate any downstream input contract, normalize quarters or reconcile figures.

### Per-source assessment

#### Annual report, FY2025 (10-K)

- Identity and perimeter: the cover states "For the fiscal year ended December 31, 2025" (page:1), and the registrant is Churchill Downs Incorporated, a single consolidated reporting entity. Evidence: statements and notes are in the pack (balance sheet at page:78, debt note at pages 108-113, segment note at pages 123-127, auditor's report at pages 128-131, exhibit index at pages 135-141).
- Controlling facts: audited FY2025 statements and the only printed financial-covenant table. Page:69 states "The Credit Agreement also contains financial covenants providing for the maintenance of a maximum consolidated secured net leverage ratio and maintenance of a minimum consolidated interest coverage ratio." and tabulates "Interest coverage ratio 3.9 to 1.0 > 2.5 to 1.0" and "Consolidated total secured net leverage ratio 1.4 to 1.0 < 4.0 to 1.0"; page:70 states "The Company was compliant with all applicable covenants on December 31, 2025."
- Unit basis: this source prints one decimal (for example "Total debt 5,155.1 4,938.7 216.4"), while the quarterly reports print whole millions. Cross-period tie-outs will carry rounding differences of that size.
- Limitation: the exhibit index at page:140 lists "10.26 Credit Agreement, dated as of December 27, 2017" by reference only; the agreement is not in the pack.

#### Quarterly reports, Q1, Q2 and Q3 2026 (10-Q)

- Periods: page:1 of each states "For the quarterly period ended March 31, 2026", "For the quarterly period ended June 30, 2026" and "For the quarterly period ended September 30, 2026" respectively. Q3 contains the statements of comprehensive income (page:2), balance sheet (page:3), cash flows (page:4) and notes (pages 6-28). Discrete quarters for Q1, Q2 and Q3 2026 are each available from their own report; a fourth-quarter 2025 figure is not printed in any supplied source as a discrete quarter and would have to be derived downstream.
- Debt detail at facility level, Q3 (page:13): "2031 Revolver $ 79 $ 657", "Term Loan B due 2033 500 —", "2027 Senior Notes 600 600", "2028 Senior Notes 700 700", "2030 Senior Notes 1,200 1,200", "2031 Senior Notes 600 600", "Total debt 4,748 5,155". Coupons and maturities for each note series are in the same note (page:16) and again in the MD&A (pages 47-48).
- Revolver availability, Q3 (page:14): "The Company had $1.1 billion available borrowing capacity, after consideration of $10 million in outstanding letters of credit, under the 2031 Revolver as of September 30, 2026." The text gives availability rounded to $0.1 billion, not to the million.
- Cash paid, Q3 (page:4): "Cash paid for interest $ 173 $ 193" and "Cash paid for income taxes 65 17" for the nine months of 2026 and 2025. The Q1 report prints "Cash paid for interest $ 43 $ 45" and the Q2 report prints "Cash paid for interest $ 139 $ 145" on their own cumulative bases (three and six months). Cash-paid interest and tax are therefore available on a year-to-date basis for each 2026 report; a stand-alone Q2 or Q3 figure would have to be derived downstream.
- Quarter versus year-to-date: Q3 prints three-month and nine-month columns side by side (page:2, "Total net revenue 696 683 2,339 2,260"). Q2 prints three-month and six-month columns. Downstream work must keep the two bases separate.
- Segment and adjusted measures: three reportable segments, plus All Other (Q3 page:25-27), and Adjusted EBITDA reconciliation in the MD&A (page:35: "Adjusted EBITDA 264 262 2 998 958 40").
- Subsequent events in Q3 (page:28): "On October 19, 2026, the Company redeemed the 2027 Senior Notes with borrowings from the 2031 Revolver." The balance sheet date figures therefore pre-date that redemption, and the 2027 Senior Notes line of "600" is outstanding at September 30, 2026 but not at the report date. Same page: a dividend and a repurchase authorization declared October 27, 2026.
- Net debt in the MD&A is a company definition: page:44 "Net debt $ 4,063 $ 5,067 $ (1,004)" is total debt net of current maturities and issuance costs, and is not net of cash. It differs from the "net bank leverage" metric in the releases.
- Covenant disclosure: the Q1, Q2 and Q3 reports do not contain a covenant table or a compliance statement. A text search of those three reports for "compliant" and "interest coverage ratio" returned no hits. Only the risk-factor and forward-looking statement language about covenants appears.

#### Earnings releases, Q1, Q2 and Q3 2026 (Exhibit 99.1)

- Authority: management-prepared, furnished; they provide attributed claims and non-GAAP reconciliations. They do not override the 10-Qs.
- Q3 release page:1 states "Record net revenue of $696 million, up $13 million or 2%" and "We ended the third quarter of 2026 with net bank leverage of 3.8x". The Q1 and Q2 releases state net bank leverage of 3.8x and 3.7x respectively. No source defines how net bank leverage is computed or reconciles it to the covenant ratio; the Q3 10-Q page:44 net debt figure is total debt net of current maturities and issuance costs and does not net cash.
- Q3 release page:3 repeats the credit agreement events: the eighth amendment closed on September 25, 2026 and a new 2033 term loan was entered.
- Guidance: a search for "guidance" and "outlook" found no hit in the three releases; the hits in the filings are accounting-standard text. No management guidance for the remainder of 2026 or beyond is therefore supplied. The Q3 10-Q page:43 gives expected 2026 project capital of "approximately $160 to $180 million".

### Coverage by requested consumer

| Consumer | Source verdict | Evidence demand and what is located | Limits carried forward |
| --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Entity, business, segments, history: 10-K Items 1 and 1A (pages 6-49), segment notes in 10-K and 10-Q | Perimeter is consolidated only; no restricted/unrestricted split or guarantor list in the pack |
| CP-1A | READY_WITH_LIMITATIONS | Financial statements for FY2025 and Q1 to Q3 2026, facility-level debt, cash paid for interest and taxes, Adjusted EBITDA reconciliations | One-decimal annual versus whole-million quarterly units; no discrete Q4 2025; no workbook or management bridge |
| CP-2 | READY_WITH_LIMITATIONS | Liquidity, maturities, revolver availability, leases and contractual obligations (Q3 10-Q pages 45-48) | No covenant figures after December 31, 2025; revolver availability rounded; post-quarter 2027 note redemption must be handled as a subsequent event |
| CP-5 | READY_WITH_LIMITATIONS | Narrative and risk disclosures, contingencies (Q3 10-Q page:24), release commentary | Release commentary is management attribution; no guidance, no ratings, no market data in the context |

## Calculations

None. CP-0 performs no calculation or normalization. Coverage counts only: seven issuer sources and one context file were pinned; 142 pages are present for the 10-K (page:1 to page:142), 37 for the Q1 10-Q, 45 for the Q2 10-Q, 51 for the Q3 10-Q, and 10, 13 and 15 for the three releases. These are chunk counts of extracted text, not a page-count proxy for readiness.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Financial covenant levels and reported ratios are printed only as of December 31, 2025 (10-K page:69); none for March, June or September 2026 | Medium | CP-2, CP-5 | Obtain the covenant compliance statement or compliance certificate, or state headroom as Not calculable |
| Executed Credit Agreement, the Eighth Amendment dated September 25, 2026 (Q3 10-Q exhibit 10.1, filed by reference to an 8-K of September 28, 2026) and the note indentures are not in the pack | Medium | CP-2, CP-5 | Add the 8-K exhibit and indentures; until then the springing-maturity and guarantor terms rest on 10-Q summaries |
| Guarantors, restricted and unrestricted subsidiaries and collateral perimeter: the 10-K says the facility is "collateralized by substantially all the wholly owned assets of the Company" but no guarantor list is supplied; the context lists none | Medium | CP-1, CP-2 | Add guarantor and subsidiary lists, or label the perimeter as consolidated parent only |
| "Net bank leverage" in the releases has no stated definition or reconciliation | Low | CP-1A, CP-2 | Treat as an attributed management claim; do not equate it with the covenant ratio |
| No investor presentation is supplied; the three earnings releases are the only management material | Low | CP-1, CP-5 | Acceptable per the pack design; no slide coverage is claimed |
| No management guidance in the releases | Low | CP-5 | Mark guidance Not supplied |
| Cash-paid interest and taxes are printed only on a cumulative basis (three, six and nine months), not as stand-alone Q2 or Q3 amounts | Low | CP-1A | Derive stand-alone quarters downstream from the cumulative lines |
| No discrete fourth-quarter 2025 figures; the 10-K prints the full year only | Low | CP-1A | Derive downstream from FY2025 less nine months, with the rounding caveat on mixed one-decimal and whole-million units |
| Extraction fidelity is not reviewed; text extraction of tables is assumed accurate where it ties to totals seen (for example Q3 note 8 debt table sums to the printed total) | Low | all | Spot-check locators downstream |

Conflicts: none found between filings and releases on the figures read. The "Debt exchanged in connection with refinancing 198" non-cash line (Q3 10-Q page:5) is an unexplained item in the extracted text and is flagged for downstream reading, not a conflict.

## Next module

CP-1, with CP-1A to follow, then CP-2 and CP-5 per the dependency order. Carry forward: consolidated perimeter only; the October 19, 2026 redemption of the 2027 Senior Notes as a subsequent event after the September 30, 2026 balance sheet; covenant figures only at December 31, 2025; the unit difference between the 10-K and the 10-Qs; and the attributed status of the releases. Next evidence action: add the Eighth Amendment, current credit agreement, indentures and a covenant compliance figure for September 30, 2026 if available.
