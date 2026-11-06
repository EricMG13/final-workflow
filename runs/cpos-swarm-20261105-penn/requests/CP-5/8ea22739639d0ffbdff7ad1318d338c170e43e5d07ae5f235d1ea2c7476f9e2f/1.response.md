## Request

PENN Entertainment, Inc., as of 2026-11-05, credit_snapshot pathway, USD. This module traces the claims in the readiness, financial, business and synthesis handoffs back to the seven pinned sources, recomputes their arithmetic, checks them against one another, and grades the run. It is independent of the modules it reviews and corrects them in this handoff only; the earlier handoffs cannot be edited.

## Sources

### Issuer sources re-read for the audit

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_penn-20251231.htm.jsonl | e6f090720b62a51573341a18254da71e5663d9a3ca11809ee32b87032414e4c4 |
| 10-Q_2026-03-31_penn-20260331.htm.jsonl | f74720e254c5d598fec44396bf0d01f4b1fcb35191eafe54dbae1433241cfe17 |
| 10-Q_2026-06-30_penn-20260630.htm.jsonl | e4a4a68372f7e9e6e78807b6eaf280e8a90a9eb8c02165e49ee603cc73e74ba7 |
| 10-Q_2026-09-30_penn-20260930.htm.jsonl | 289bd66b2b3ba7c0442b90807e0166affa057570b7680ca91b89ac74aa566568 |
| EX-99.1_2026-04-23_pennex991-q12026.htm.jsonl | bd58a1d530bb3cf8b4081bd3c78bc172ec144332ab675d2b2c776af0b2ffd599 |
| EX-99.1_2026-08-06_pennex991-q22026.htm.jsonl | 29f1d9698d7fe07b2e827f80ed415692eef3a01380a671b91317aa4e3711e167 |
| EX-99.1_2026-11-05_pennex991-q32026.htm.jsonl | 9cd3b27bc143946725e283ad70f7a65c0842d014c7b12f2cd6670b5aee829c8c |

Locators are `source page:N` where N is the extraction chunk number. "10-Q Q3" is the 10-Q for the quarter ended 2026-09-30; "release Q3" is the exhibit dated 2026-11-05.

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 8e6b52c72fe186ee073cb0e5f0c242ec3f53d4e3a091c87a50ef71a77d1acea5 |
| CP-1 | bee29e201472d452cc9be9f8fb6fde66557fd4e562944dfd264ac815d53f45f1 |
| CP-1A | 346fa2d6383c1d8f92e89a1bd113962215e843cc2f2fd3ae60a10b468485a1cb |
| CP-2 | 8780996c874add5b1a6281b62897c20b8dabce59c7d05d871e58c7f359b32434 |

Each handoff was opened and compared with the sources, not only with the other handoffs. Where this handoff differs from an earlier one it says so and gives the corrected statement; the earlier handoff stays as accepted.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The headline debt, liquidity, earnings and leverage figures trace to the filings and recompute exactly. Six minor issues were found and are corrected here; none changes a credit conclusion. | Medium | Review used extracted text, not rendered filings, and the debt documents are not supplied, so covenant and legal claims rest on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt of 2,806.6, cash of 1,044.8, liquidity of 2,020.9 and LTM Consolidated Adjusted EBITDA of 1,088.2 match the sources and tie to their components. | The core leverage and liquidity picture can be relied on within the stated definitions. | High |
| Three cash-flow lines cite the wrong page, and one statement about landlord payments should read 263.3 rather than 252.2. | Neither changes a ratio; the corrected landlord payment figure is the cash not deducted in EBITDA. | High |
| The 4.125% notes are senior unsecured and not subsidiary guaranteed, which an earlier handoff listed as not located. | The 2029 notes rank with the other notes; the gap is closed. | High |
| Covenant headroom, guarantor identity and lease terms rest on filing summaries because the executed documents are not supplied. | Legal protections cannot be verified from this record. | Medium |

### Evidence trace view

Every material claim in the four handoffs was traced to a located source span, and the arithmetic was recomputed from the cited figures. The headline financial claims hold: debt principal of 2,806.6 and cash of 1,044.8 at 2026-09-30, liquidity of 2,020.9, LTM Consolidated Adjusted EBITDA of 1,088.2, and the ratios derived from them, all recompute exactly and share one perimeter and period basis. A set of 186 figure and phrase checks against the cited pages found 179 at the cited location; the other 7 were examined individually and two were real locator errors, the rest check-string artifacts or an adjacent page already cited. The audit found six issues, all minor: wrong page numbers for three cash-flow lines and one working-capital reference, a statement that gaming taxes are the largest retail cost that is true for only two of four retail segments, a landlord-payment figure of 252.2 that should read 263.3, a gap for the 4.125% notes that the 10-K fills, and a cross-default described more broadly than the filing supports in two handoffs. None changes a ratio, a liquidity figure or the direction of the credit view, so the run is graded Passed with corrections logged. The strongest contrary reading is that the improvement is overstated: the company's debt measure leaves out financing obligations and finance leases of 4,359.4 and LTM net income is a loss of 11.0, so the handoffs already carry the extended-perimeter leverage of 5.63x. What would make the contrary view win is covenant definitions that count those obligations as debt, which the missing credit agreement prevents anyone from testing.

### Quality assurance status

| Field | Value |
| --- | --- |
| qa_status | Passed (six Minor issues, no Critical or Material issue) |
| committee_status | Draft Only: usable for discussion; covenant, guarantor and lease-term conclusions need the executed documents |
| Confidence band | Medium, capped because the debt documents, ratings and proxy data are not supplied and the checks used extracted text |
| Subsequent events | Handled correctly: the October 15, 2026 exchangeable share notice and the November 1, 2026 rent escalator are labelled subsequent and not blended into period figures |
| Cutoff | No source dated after 2026-11-05 was used |

### Input module register

| Module | Status | Material claims audited | Result |
| --- | --- | --- | --- |
| CP-0 | Accepted | Source coverage, periods, perimeter, 9 tie-outs | Supported; one locator corrected before acceptance |
| CP-1 | Accepted on second attempt | Statements, debt table, liquidity, maturities, leases, covenants, events, 4 charts | Supported with three issues (I1, I4, I5) |
| CP-1A | Accepted | Business model, profile, timeline, governance, 5 credit translations | Supported with three issues (I2, I3, I6) |
| CP-2 | Accepted | Credit view, findings, strengths, weaknesses, 7 risks | Supported; repeats the I6 wording and is otherwise consistent |

### Citation and evidence support audit

| Claim | Module | Locator checked | Result |
| --- | --- | --- | --- |
| Debt table, repayment schedule and total of 2,806.6 | CP-1 | 10-Q Q3 pages 15-16 | Supported |
| Revolver 1.0 billion, letters of credit 23.9, availability 976.1, maturity April 2031 | CP-1 | 10-Q Q3 pages 17-18 | Supported |
| Covenant levels 4.50 to 1.00, step up 5.00 to 1.00, 2.00 to 1.00, compliance statement | CP-1 | 10-Q Q3 pages 17 and 20 | Supported; ratio values not printed |
| Lease and financing obligation balances 2,309.8, 2,049.6, 3,798.2 | CP-1 | 10-Q Q3 pages 2 and 27 | Supported |
| Cash-flow lines: operating cash flow 626.4 and 401.0, capital expenditures 251.2 and 457.3, sale-leaseback proceeds 216.3 and 130.0 | CP-1 | Cited as 10-Q Q3 page:6; found on page:5 | Figures supported, locator wrong (issue I1) |
| Cash paid for interest 291.6 and 292.2, no share repurchases | CP-1 | 10-Q Q3 page:6 | Supported |
| LTM Consolidated Adjusted EBITDA 1,088.2, 999.1, 922.6 and FY2025 830.1 | CP-1 | Releases, 10-K page:74 | Supported as management measures |
| Segment Adjusted EBITDAR and revenue by segment | CP-1; CP-1A | 10-Q Q3 pages 15, 38, 40 | Supported |
| "Gaming taxes are the largest retail cost" | CP-1A | 10-Q Q3 page:37 | Partly supported (issue I3): true in Northeast (285.8) and Midwest (89.4); in South other segment items (67.3) exceed compensation (58.2) and gaming taxes (58.0); in West compensation (35.4) exceeds other items (34.9) and gaming taxes (26.3) |
| Working capital reference to the cash-flow statement | CP-1A | Cited as 10-Q Q3 page:6; on page:5 | Locator wrong (issue I2) |
| "252.2 is the part of landlord payments not deducted in EBITDA" | CP-1 | 10-Q Q3 pages 27 and 28 | Incorrect attribution (issue I4); see below |
| 4.125% Notes "ranking and guarantor wording not located" | CP-1 | 10-K page:139 | Gap fillable (issue I5): "4.125% senior unsecured notes", due July 1, 2029, issued at par, interest each January 1 and July 1, "not guaranteed by any of the Company's subsidiaries" except if certain guaranteed securities are later issued, redeemable from July 1, 2024 |
| Lease default is also a debt default | CP-1A; CP-2 | 10-Q Q3 page:20; 10-K page:35 | Overbroad (issue I6): the debt agreements cross-default to the Master Leases with GLPI; the 10-K names the AR PENN, 2023 and Pinnacle Master Leases. VICI Master Lease and Morgantown Lease cross-default is not stated |
| Interactive revenue ex gross-up 157.0 against 158.2; nine months 493.3 against 498.3 | CP-1; CP-1A; CP-2 | 10-Q Q3 pages 15, 56, 64 | Supported |
| ESPN-related advertising 52.0 in Q3 2025 | CP-1 | 10-Q Q3 page:41 | Supported |
| GLPI funding 130.0, 150.0, 216.3 and added rent 10.1, 11.7, 17.4 | CP-1A | 10-Q Q3 pages 22-23, 49-50 | Supported |
| Business facts: 28 jurisdictions, 42 properties in 19 states, employees, footprint | CP-1A | 10-K pages 6-7, 9, 21 | Supported (properties are at 2025-12-31) |
| Governance: HG Vora timeline, Cooperation Agreement, buybacks, authorization 750.0 | CP-1A | 10-K pages 29-30, 109; 10-Q Q3 page:80 | Supported |
| Pension, retiree medical and factoring obligations not found | CP-1 | Search of the 10-K and 10-Q Q3 | Supported by search |
| No creditor-adverse action found | CP-1A | Search for priming, uptier, drop-down and similar terms across the filings | Supported by search; the hits were betting "liability management" |
| Guidance amounts not supplied | CP-0; CP-1 | Search of releases and filings | Supported; only a full-year Interactive target is referred to, with no amount |

### Legal and structural claims audit

| Claim | Basis in the handoffs | Result |
| --- | --- | --- |
| Notes are senior unsecured and not subsidiary guaranteed (5.625%, 4.125%, 6.75%) | Filing descriptions, 10-Q Q3 page:18; 10-K page:139 | Supported by filing text; indentures not supplied, so clause-level support is absent |
| Credit facility obligations are collateralised by interests in owned real property with named exceptions | 10-K page:64 | Supported by filing text; security package and guarantors not supplied |
| AR PENN and 2023 Master Leases are cross-defaulted, cross-collateralized, coterminous and subject to a parent guarantee | 10-Q Q3 page:21 | Supported by filing text; lease documents not supplied |
| Debt agreements cross-default to the GLPI Master Leases | 10-Q Q3 page:20; 10-K page:35 | Supported with the scope noted in issue I6 |
| Covenant tests and levels | 10-Q Q3 page:17 | Supported; definitions and reported values not supplied, headroom correctly stated as Not calculable |
| Lease terms, escalators and rent resets | 10-Q Q3 pages 21-25 | Supported by filing text |

### Relative value and market claims audit

| Claim | Result |
| --- | --- |
| Fair values of 574.5 for the 6.75% notes and 375.0 for the 4.125% notes below principal (10-Q Q3 page:78) | Supported as disclosed fair values; the handoffs use them as a fact, not a price view |
| No peer ranking, instrument recommendation or recovery conclusion | None found in any handoff; CP-1A recovery mechanics are stated without an outcome |

### Cross-module consistency and version control

| Item | CP-1 | CP-1A | CP-2 | Result |
| --- | --- | --- | --- | --- |
| Debt principal at 2026-09-30 | 2,806.6 | 2806.6 (cited from CP-1) | 2,806.6 | Consistent |
| Cash at 2026-09-30 | 1,044.8 | Not restated | 1,044.8 | Consistent |
| Liquidity | 2,020.9 | Not restated | 2,020.9 | Consistent |
| LTM Consolidated Adjusted EBITDA | 1,088.2 | 1088.2 (cited from CP-1) | 1,088.2 | Consistent |
| Net and gross leverage | 1.62x and 2.58x | Not restated | 1.62x and 2.58x | Consistent |
| Obligations outside debt | 8,157.6 | 8157.6 | 8,157.6 | Consistent |
| Extended-perimeter net leverage | 5.63x | Not restated | 5.63x | Consistent, labelled analyst construction |
| Retail margin Q3 2026 | 33.7% | 33.7% | 33.7% | Consistent |
| Added rent on GLPI funding | Not restated | 7.9% | 7.9% | Consistent |
| Cross-default scope | Tied to the Master Leases (accurate) | General | General | CP-1A and CP-2 are broader than the filings (issue I6) |

Version control: the debt table changed version in 2026 (revolver and Term Loan A to 2031, Term Loan B to 2033). CP-1 labels the year-end 2025 table as the prior version; no handoff mixes the two without a label. The 2029 notes are the same instrument at both dates.

### Duplication, materiality and committee readiness

CP-2 repeats figures from CP-1 and CP-1A by design and adds no figure of its own. The reader summaries restate conclusions already in each handoff. The covenant limitation is repeated in every module; it is material because it blocks the headroom conclusion, so the repetition is acceptable. No duplicated analysis changes a conclusion. The run is usable as a filings-based snapshot for discussion.

### Handoff envelope and evidence trace audit

| Module | Six H2 headings in order | Issuer and as-of date in Request | Sources and hashes listed | Handoffs listed with hashes | Selector headings present once | Result |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | Yes | Yes | Yes | None supplied (correct) | Reader summary and Readiness view | Pass |
| CP-1 | Yes | Yes | Yes | CP-0 | Four chart tables, financials table | Pass |
| CP-1A | Yes | Yes | Yes | CP-0, CP-1 | Operating model, profile, transaction summary | Pass |
| CP-2 | Yes | Yes | Yes | CP-0, CP-1, CP-1A | Key findings, strengths and weaknesses | Pass |

### Consolidated issue log

| Issue | Severity | Module | Type | Description and correction | Status |
| --- | --- | --- | --- | --- | --- |
| I1 | Minor | CP-1 | Locator | Operating cash flow, capital expenditures and sale-leaseback proceeds are cited to 10-Q Q3 page:6; they are on page:5. Figures are correct. | Corrected here |
| I2 | Minor | CP-1A | Locator | Working capital row cites 10-Q Q3 page:6; the accrued expense and prepaid lines are on page:5. | Corrected here |
| I3 | Minor | CP-1A | Unsupported superlative | Gaming taxes are the largest retail cost line only in Northeast and Midwest. In South the largest line in Q3 2026 is other segment items (67.3, against compensation 58.2 and gaming taxes 58.0); in West it is compensation (35.4, against other segment items 34.9 and gaming taxes 26.3). | Corrected here |
| I4 | Minor | CP-1 | Attribution | CP-1 says the excess of landlord cash payments (746.6) over operating lease rent expense (494.4) of 252.2 is the part not deducted in EBITDA. The cash not deducted is the Pinnacle Master Lease and Morgantown Lease payments of 260.9 and 2.4, which is 263.3 (10-Q Q3 page:27). The 252.2 also reflects operating lease rent expense of 494.4 exceeding the 483.3 paid under the AR PENN, 2023 and VICI leases (219.3, 203.2, 60.8) by 11.1. | Corrected here |
| I5 | Minor | CP-1 | Fillable gap | The 4.125% Notes are described in the 10-K at page:139 as senior unsecured, due July 1, 2029, not guaranteed by subsidiaries; the Q3 10-Q does not repeat it. | Corrected here |
| I6 | Minor | CP-1A; CP-2 | Overbreadth | Cross-default to leases is stated for GLPI Master Leases in the filings, not for all landlord leases. The credit conclusion stands because the GLPI leases carry most of the rent. | Corrected here |

### Remediation priority map

Must fix before committee: none. Must fix before the handoffs are consumed downstream: read I1 to I6 with the accepted handoffs, in particular use 263.3 as the landlord cash not deducted in EBITDA, and use the GLPI Master Leases scope for cross-default. Monitoring follow-up: obtain the credit agreement, compliance certificate, indentures and executed leases, and re-run the covenant and cross-default conclusions. Formatting and hygiene: use `page:5` for the cash-flow lines and carry the corrected 4.125% notes description.

### Clearance decision

CLEARANCE DECISION: Pass with corrections. Critical issues: 0. Material issues: 0. Minor issues: 6. The run may be used as a filings-based snapshot for committee discussion (status Draft Only) with the corrections above and the limits on covenant, guarantor and lease-term conclusions. It does not clear any conclusion that needs the executed debt or lease documents.

## Calculations

All inputs come from the cited locators; amounts in US$m. Each handoff value was recomputed.

| Metric | Inputs | Recomputed | Handoff | Result |
| --- | --- | --- | --- | --- |
| Debt principal 2026-09-30 | 441.3 + 957.5 + 400.0 + 400.0 + 600.0 + 7.8 | 2,806.6 | 2,806.6 | Match |
| Repayment schedule | 8.1 + 433.1 + 33.1 + 433.2 + 33.2 + 1,865.9 | 2,806.6 | 2,806.6 | Match |
| Liquidity Q3 2026 | 1,044.8 + (1,000.0 - 23.9) | 2,020.9 | 2,020.9 | Match |
| LTM EBITDA | 830.1 + 862.4 - 604.3 | 1,088.2 | 1,088.2 | Match |
| Total debt / EBITDA, LTM Q3 2026 and FY2025 | 2,806.6 / 1,088.2; 2,904.1 / 830.1 | 2.579; 3.498 | 2.58x; 3.50x | Match |
| Net debt / EBITDA, LTM Q3 2026 and FY2025 | 1,761.8 / 1,088.2; 2,217.5 / 830.1 | 1.619; 2.671 | 1.62x; 2.67x | Match |
| Net debt LTM Q1 and Q2 2026 | 2,240.9 / 922.6; 1,927.5 / 999.1 | 2.429; 1.929 | 2.43x; 1.93x | Match |
| LTM cash interest | 383.0 - 292.2 + 291.6; 383.0 - 188.0 + 187.9; 383.0 - 102.0 + 107.8 | 382.4; 382.9; 388.8 | 382.4; 382.9; 388.8 | Match |
| Cash interest cover | 1,088.2 / 382.4; 830.1 / 383.0 | 2.846; 2.167 | 2.85x; 2.17x | Match |
| Obligations outside debt | 2,309.8 + 2,049.6 + 3,798.2; 2,309.8 + 2,049.6 | 8,157.6; 4,359.4 | 8,157.6; 4,359.4 | Match |
| Extended-perimeter leverage | (2,806.6 + 4,359.4) / 1,088.2; less cash 1,044.8 | 6.585; 5.625 | 6.59x; 5.63x | Match |
| Twelve-month maturity cover | 2,020.9 / 432.3, with 432.3 = 400.0 + 32.3 | 4.675 | 4.7 times | Match |
| Q3 EBITDA bridge | 58.3 + 36.0 + 4.6 - 9.8 | 89.1 (284.0 - 194.9) | 89.1 | Match |
| Segment bridge Q3 2026, nine months 2026, FY2025 | 483.5 - 31.6 - 167.9; 1,451.7 - 94.9 - 494.4 (with 38.7 loss); 1,461.8 - 631.7 | 284.0; 862.4; 830.1 | 284.0; 862.4; 830.1 | Match |
| LTM revenue, operating income, net income | 6,961.0 + 5,476.4 - 5,154.8; -673.6 + 355.9 + 656.1; -845.3 + 62.4 + 771.9 | 7,282.6; 338.4; -11.0 | 7,282.6; 338.4; (11.0) | Match |
| LTM operating cash flow, capital expenditures | 508.2 + 626.4 - 401.0; 647.7 + 251.2 - 457.3 | 733.6; 441.6 | 733.6; 441.6 | Match |
| Interactive ex gross-up | 348.4 - 191.4; 297.7 - 139.5; 1,056.0 - 562.7; 903.9 - 405.6 | 157.0; 158.2; 493.3; 498.3 | Same | Match |
| Added rent on GLPI funding | (10.1 + 11.7 + 17.4) / (130.0 + 150.0 + 216.3) | 7.90% | 7.9% | Match |
| Retail margin Q3 2026 and Q3 2025 | 501.8 / 1,489.5; 465.8 / 1,418.1 | 33.69%; 32.85% | 33.7%; 32.8% | Match |
| Landlord cash not deducted in EBITDA, nine months 2026 | 260.9 + 2.4 (Pinnacle and Morgantown); check 746.6 - (219.3 + 203.2 + 60.8) | 263.3; 263.3 | CP-1 stated 252.2 | Corrected (issue I4) |
| Rent expense LTM | 631.7 + 494.4 - 470.0 | 656.1 | 656.2 printed | 0.1 rounding in the source, disclosed in CP-1 |

Consistency of period and perimeter: every LTM figure combines the audited year, the nine months 2026 and the nine months 2025 on the consolidated perimeter; the debt figures are principal while the balance sheet carrying value is 2,768.3, a difference of 38.3 of discounts and costs that CP-1 states.

## Gaps

| Gap | Effect on the audit | Action |
| --- | --- | --- |
| Executed credit agreement, indentures, master leases and compliance certificate not supplied | Legal and covenant claims rest on filing summaries, so clause-level support is absent | Obtain and re-audit |
| Review used extracted text with chunk numbers, not rendered filings or XBRL | A flattened table could hide a sign or column error; the recomputations reduce this risk | Spot check the figures that drive conclusions |
| Ratings, quotes, proxy ownership data and guidance amounts not supplied | Not audited | Supply if needed |
| Guarantor identity for the credit facilities not located | Priority of bank debt against notes not testable | Obtain guarantor schedule |
| Confidence is capped at Medium | Reflects the gaps above, not a defect in the handoffs | None |

## Next module

This is the last module in the run. The report should assemble the four handoffs together with the six corrections in the issue log: page:5 for the cash-flow lines, the corrected gaming tax statement, 263.3 as the landlord cash not deducted in EBITDA, the 4.125% notes description, and the GLPI scope of cross-default. Any later work should start from the debt and lease documents.
