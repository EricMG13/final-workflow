# CP-5 — Evidence trace and research-integrity QA: BAYTEX ENERGY CORP. (bte)

## Request

This is the evidence trace and research-integrity check for BAYTEX ENERGY CORP. (issuer id bte), as of 2026-11-05 with an information cutoff of 2026-11-05, pathway credit snapshot, minimum module set. It checks the readiness (CP-0), financial (CP-1), business and transaction (CP-1A) and synthesis (CP-2) handoffs against the pinned sources and against each other, and grades the result (absorbed CP-5A phase). The same host session wrote the four handoffs it checks, so this is a self-review, not an independent one. QA envelope: qa_status Passed; Confidence Score 44, band Low (from the repository's confidence_score.py, see Calculations); committee_status Requires More Work.

## Sources

### Issuer sources checked against

| Alias | Exact source name | sha256 |
| --- | --- | --- |
| S1 | 40-F_2025-12-31_bte-20251231.htm.jsonl | 7928c3aee2847a067565e87aab941fb0fa693ec3a05da16abf228b0aca516096 |
| S2 | 6-K-EX-99.1_2025-09-30_a991-q32025fs.htm.jsonl | 88b3b8e7d8e11703b95eab9a12edb425d85ec75970d2d968e209a9c3a366a490 |
| S3 | 6-K-EX-99.1_2025-12-31_a991-2025yepressrelease.htm.jsonl | 3673c1a3e44baf8845d8213620919370a57219f3e6310c71f221c475210c6b47 |
| S4 | 6-K-EX-99.1_2026-03-31_a991-q12026fs.htm.jsonl | 792eab73e1363b4073690efb2135aa655fd77f770258c41719cb471c48ece251 |
| S5 | 6-K-EX-99.1_2026-03-31_tm2613640d2_ex99-1.htm.jsonl | 9b4c8c62190d6a1b8a9c4e232069f5ad6fc7f4c944563935fd4bf5121d096095 |
| S6 | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | 16eeba2e704f92279ab76d18bdc0c26c8ff5c06bb58d42d66e8037ca77adddf4 |
| S7 | 6-K-EX-99.1_2026-08-05_tm2619297d2_ex99-1.htm.jsonl | 2da1f8d94e5a6b644192e34205faf74054d51d4cb86b7a7a5ff6f34cc5c6aa6a |

Run context (settings, not issuer evidence): /workspace/secdata/data/2026-11-05/contexts/1279495-baytex-energy-corp-bte.json, sha256 a4beb54d12cde8b01d2e19e329c06ce5b476e74c9a66d64a29ea9c069505e245.

### Supplied handoffs

| Module | sha256 | Checked for |
| --- | --- | --- |
| CP-0 | 68599e57819209c904b32c5e729b1780b103c65bf8c26f89178fef7d84c1f1ef | Source register, gaps, perimeter notes |
| CP-1 | aa3453dc0f8d425d3b66d145888845acf28f20d2c2a05f86208a8401329bec01 | Financial figures, chart tables, debt, liquidity, covenants |
| CP-1A | 6499170f9e77a8dc035850243b0c8922ee81f9c50f3b659fe2b401b3a1bba1da | Business and transaction facts, governance rows, corrections |
| CP-2 | f523ee54a91fece06487ba1d70d0c0f280ebbadb7cb89ddd333a0a5fe23bf06f | Credit view, key findings, risks, gaps |

Locators `Sn page:N` are chunks of the pinned `.jsonl` files (extracted copies under the run folder), not printed pages. Method: every register quotation in CP-0, CP-1 and CP-1A was searched on the page it cites; statement totals and reconciliations were re-added from numbers typed from the source pages; every derived figure was recomputed from source numbers and compared with the handoff; CP-2 figures were matched to CP-1, CP-1A or CP-2's own calculations.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is well traced to the filings and its numbers recompute. It supports a view of current debt, liquidity and covenants, but not of how well creditors are protected, because key documents are missing. | Medium | The same author wrote and checked all four handoffs, and the debt agreements, ownership and sale documents are not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every checked quotation sits on its cited page and every recomputed figure matches. | Debt, liquidity and covenant figures in the credit view can be relied on as stated. | High |
| Claims about guarantors, security, distribution limits, ownership and the sale terms are labelled as missing evidence, not asserted. | Creditor-protection conclusions stay open; labelled gaps are not weaknesses and not support. | High |
| Five minor defects: three locator or assumption issues, one stale pair of notes, and chart tables with no plotted liquidity or maturity values. | None changes a conclusion, but the liquidity and maturity charts will carry no numbers. | High |
| Management statements, including the plan to maintain net cash, are tagged as management language and not adopted. | Outlook claims should not be read as commitments binding the issuer. | Medium |

### Evidence trace view

The analysis is traceable enough to support a view of the issuer's current capital structure, liquidity and covenant position, but not a view on how much of its cash buffer is protected from distributions. Every figure the credit synthesis uses was recomputed from the cited statements and agrees, and every quoted passage in the three upstream registers sits on its cited page. The critical provenance gap is the absence of the credit agreement, note indenture, ownership record and sale agreement; the upstream modules label these as missing evidence, so no claim is unsupported, but the Medium confidence of the credit view depends on them. The affected decision is any judgment on creditor protection or future leverage. The remediation owner is the sourcing step, which must add those documents. Five minor defects change no conclusion.

| Traceability summary | Result |
| --- | --- |
| Register quotations checked against the cited page | 171 of 171 found (CP-0 37, CP-1 78, CP-1A 56) |
| Statement totals and reconciliations re-added from source numbers | 42 of 42 equal |
| Derived figures recomputed from source numbers | 30 of 30 equal to the handoffs |
| CP-2 figures traced | All found in CP-1, CP-1A or CP-2's own calculations |
| Material claims by lineage | 7 Directly Sourced, 3 Calculated, 3 Analyst Inference, 2 Insufficient Information |
| Open findings | 5 MINOR, none MATERIAL or CRITICAL |
| QA envelope | Passed; Confidence Score 44 (Low); committee status Requires More Work |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 40-F_2025-12-31_bte-20251231.htm.jsonl | High: filed annual report cover; exhibits not retained | Fiscal year ended December 31, 2025 | BAYTEX ENERGY CORP. | Registrant identity, officers, auditor, exhibit list | No financial statements; exhibits 99.1 to 99.4 absent | CP-0, CP-1A |
| S2 | 6-K-EX-99.1_2025-09-30_a991-q32025fs.htm.jsonl | High: filed unaudited interim statements | Q3 2025 and nine months | Consolidated including U.S. operations | Statements, prior debt structure, covenants | Pre-sale basis; not restated | CP-0, CP-1, CP-1A |
| S3 | 6-K-EX-99.1_2025-12-31_a991-2025yepressrelease.htm.jsonl | Medium: issuer press release with reconciliation tables | Q4 2025 and FY2025 | Consolidated with a Canada and discontinued split in some tables | FY2025 results, year-end debt and net cash, Eagle Ford sale | Unaudited release; audited statements not retained | CP-0, CP-1, CP-1A |
| S4 | 6-K-EX-99.1_2026-03-31_a991-q12026fs.htm.jsonl | High: filed unaudited interim statements | Q1 2026 | Continuing (Canada) with discontinued operations | Statements, notes, covenants | Contained in S5 | CP-1, CP-1A |
| S5 | 6-K-EX-99.1_2026-03-31_tm2613640d2_ex99-1.htm.jsonl | Mixed: High for statements, Medium for release and discussion | Q1 2026 | Same | Release, discussion, adjusted funds flow split, strategy | Management narrative | CP-1, CP-1A |
| S6 | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | High: filed unaudited interim statements | Q2 2026 and six months | Same | Statements, notes, covenants, net cash | Contained in S7 | CP-0, CP-1, CP-1A |
| S7 | 6-K-EX-99.1_2026-08-05_tm2619297d2_ex99-1.htm.jsonl | Mixed: High for statements, Medium for release and discussion | Q2 2026 | Same | Release, discussion, obligations, guidance, subsequent events | Management narrative | CP-0, CP-1, CP-1A |
| S8 | context (run settings) | User settings, not issuer evidence | As-of 2026-11-05 | Run identity | Pathway, dates, currency | Not issuer evidence | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Minimal debt and strong liquidity after the Eagle Ford sale | CP-1, CP-2 | Notes principal 91,107; facilities undrawn; cash 720,337 (C$ thousand) | Removes near-term debt-service and refinancing risk | Sets the current credit view | S6 page:1, page:8, page:9; S7 page:48 | Company-defined EBITDA and net cash |
| 2 | Cash returns exceed free cash flow | CP-1, CP-1A, CP-2 | Returns 342.9 against free cash flow 129.8 (C$ million) | The buffer that supports credit quality is discretionary | Sets future leverage tolerance | S7 page:47; S6 page:11 | Restricted-payment baskets not in the set |
| 3 | Oil price exposure with hedges expired | CP-1A, CP-2 | Free cash flow 1,705 in Q1 and 128,045 in Q2 (C$ thousand); no WTI hedges after Q2 2026 | Cash flow and net cash move with price | Sets downside sensitivity | S7 page:3, page:6 | No forecast or sensitivity supplied |
| 4 | Non-debt claims on cash | CP-1, CP-1A, CP-2 | Asset retirement 546,500; leases 60,256; CRA assertion 244.8 tax (C$ thousand, C$ thousand, C$ million) | Fixed and contingent calls on the same cash flow | Sets total claims view | S6 page:8, page:10, page:14 | Tax provision not stated |
| 5 | Missing creditor-protection documents | CP-0, CP-1, CP-2 | No credit agreement, indenture, ownership or sale agreement in the set | Guarantors, security and distribution limits cannot be tested | Caps confidence | S1 page:2, page:6 | Labelled as missing in every module |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revolver undrawn, secured, matures June 27, 2030; one note series US$64.1 million due 2032 | CP-1, CP-1A, CP-2 | S6 page:8, page:9, page:10; S7 page:48, page:49 | Yes | High | Directly Sourced | Supported | High | Traced |
| Liquidity of 1,465,937 (C$ thousand) | CP-1, CP-2 | S6 page:1, page:8, page:9 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Leverage 0.13x, net cash 0.75x and cover 9.31x on Bank EBITDA | CP-1, CP-2 | S6 page:9, page:18 | Yes | High inputs; company-defined denominators | Calculated | Supported with definition caveat | Medium | Recomputed equal |
| Covenant levels and compliance statement | CP-1 | S6 page:8, page:9 | Yes | High; management statement inside filed statements | Directly Sourced | Supported as a statement | Medium | Traced |
| Net cash 566,286 (C$ thousand) | CP-1, CP-2 | S6 page:18; S7 page:3 | Yes | High | Directly Sourced | Supported | High | Traced |
| Eagle Ford sale of December 19, 2025, net proceeds US$2.2 billion, and use of proceeds | CP-1A, CP-2 | S3 page:5; S7 page:38 | Yes | Medium: release; High: discussion | Directly Sourced | Supported as management statement | Medium | Traced |
| No WTI hedges after Q2 2026 | CP-1A, CP-2 | S7 page:6 | Yes | Medium: release | Directly Sourced | Supported | High | Traced |
| Non-debt claims: asset retirement, leases, CRA assertion | CP-1, CP-1A, CP-2 | S6 page:8, page:10, page:14 | Yes | High | Directly Sourced | Supported | High | Traced |
| Sum of asset retirement and lease obligations 606,756 (C$ thousand) | CP-2 | S6 page:8, page:10 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Distributions exceed free cash flow by 213.10 (C$ million) | CP-1A, CP-2 | S6 page:11; S7 page:3, page:47 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Free cash flow follows oil prices | CP-1A, CP-2 | S7 page:3 | Yes | High inputs | Analyst Inference | Supported by two quarters only | Medium | Reasoning traced |
| Single-basin concentration | CP-1A, CP-2 | S7 page:22 | Yes | High | Analyst Inference | Supported | Medium | Reasoning traced |
| Management plan to maintain net cash, break-even targets, industry-leading balance sheet | CP-1A, CP-2 | S5 page:2, page:4; S7 page:2 | Yes | Medium: management narrative | Directly Sourced | Supported as management language only | Low | Traced and correctly tagged |
| Ownership and control | CP-1A, CP-2 | No source in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Guarantors, security, distribution baskets, call prices | CP-1, CP-1A, CP-2 | No debt document in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cash 720,337 at June 30, 2026 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:1, balance sheet | CP-1 metrics table | Reported | High | Matches |
| Credit facilities mature June 27, 2030 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:8, note 8 | CP-1 debt register | Reported | High | Matches |
| Notes principal 91,107 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:9, note 9 | CP-1 debt register | Reported | High | Matches |
| Notes US$64.1 million | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:10, note 9 footnote | CP-1 debt register | Reported | High | Matches |
| Net cash (566,286) | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:18, note 19 | CP-1 metrics table | Reported company measure | High | Reconciliation re-added equal |
| Bank EBITDA 758.9 million | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:9, covenant footnote | CP-1 covenant table | Reported company measure | High | Matches |
| Financing and interest expense 81.5 million | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:9, covenant footnote | CP-1 covenant table | Reported company measure | High | Matches |
| Letters of credit 4.4 million | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:9, note 8 | CP-1 liquidity table | Reported | High | Matches |
| Asset retirement obligations 546,500 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:10, note 10 | CP-1 claims table | Reported | High | Matches |
| Lease obligations present value 60,256 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:8, note 7 | CP-1 claims table | Reported | High | Matches |
| Adjusted funds flow 254,433 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:18, note 19 | CP-1 metrics table | Reported company measure | High | Reconciliation re-added equal |
| Interest paid 842 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:3, cash flow statement | CP-1 metrics table | Reported | High | Matches |
| Free cash flow 128,045 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-08-05_tm2619297d2_ex99-1.htm.jsonl | S7 | page:3, results table | CP-1 metrics table | Reported company measure | Medium | Matches |
| Production 71,243 boe/d | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-08-05_tm2619297d2_ex99-1.htm.jsonl | S7 | page:25, results of operations | CP-1 metrics table | Reported | High | Matches |
| Contractual obligations total 297,150 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-08-05_tm2619297d2_ex99-1.htm.jsonl | S7 | page:50, contractual obligations | CP-1 maturity table | Reported | High | Columns and rows re-added equal |
| WTI average 92.79 in Q2 2026 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-08-05_tm2619297d2_ex99-1.htm.jsonl | S7 | page:3, benchmark prices | CP-1A credit translations | Reported | High | Matches |
| Net proceeds US$2.2 billion | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2025-12-31_a991-2025yepressrelease.htm.jsonl | S3 | page:5, 2025 results | CP-1A transaction summary | Reported by management | Medium | Matches |
| Net cash (765,785) at December 31, 2025 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2025-12-31_a991-2025yepressrelease.htm.jsonl | S3 | page:3, net cash table | CP-1 metrics table | Reported company measure | Medium | Matches S6 comparative |
| Interest coverage 10.5 at September 30, 2025 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2025-09-30_a991-q32025fs.htm.jsonl | S2 | page:9, covenant table | CP-1 chart data | Reported company measure | High | Matches |
| Bank EBITDA 661.0 million at March 31, 2026 | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-03-31_a991-q12026fs.htm.jsonl | S4 | page:9, covenant footnote | CP-1 chart data | Reported company measure | High | Matches |
| CRA tax asserted 244.8 million | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | S6 | page:14, note 15 | CP-1 claims table | Reported | High | Matches |
| Shareholder returns 342.9 million | runs/cpos-swarm-20261105-bte/source-text | 6-K-EX-99.1_2026-08-05_tm2619297d2_ex99-1.htm.jsonl | S7 | page:47, capital management | CP-1 latest quarter table | Reported by management | Medium | Components re-added equal |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Liquidity | CP-1 C1; CP-2 | Cash, facility commitment, drawings, letters of credit | Cash + (commitment − drawn − letters of credit) | Recomputed: 1,465,937; 1,503,469; 1,697,313 equal | Supported | High | Liquidity cover | S6 page:1, page:8, page:9; S4 page:1; S3 page:13 |
| Covenant Total Debt tie-out | CP-1 C2 | Notes principal 91,107; letters of credit 4,400 | Sum equals printed 95.5 million after rounding | Recomputed: 95,507 equal | Supported | High | Covenant definition | S6 page:9 |
| Leverage ratios | CP-1 C3; CP-2 | Total Debt, net cash, Bank EBITDA | Ratio of company-defined numerator to Bank EBITDA | Recomputed: 0.13, 0.14, −0.75, −0.89 equal | Supported with definition caveat | Medium | Leverage tolerance | S6 page:9, page:18; S4 page:9 |
| Interest cover | CP-1 C4; CP-2 | Bank EBITDA; financing and interest expense | Bank EBITDA / financing and interest expense | Recomputed: 9.31 and 5.54 equal | Supported with definition caveat | Medium | Debt service | S6 page:9; S4 page:9 |
| Covenant headroom | CP-1 C5; CP-2 | Floor 3.5; caps 4.0 and 3.5 | Floor × denominator; cap × Bank EBITDA | Recomputed: 285.25; 473.65; 3,035.6; 2,656.15 equal | Supported as arithmetic, not forecast | Medium | Covenant risk | S6 page:9 |
| Obligations and net cash tie-outs | CP-1 C6, C7 | Contractual obligations table; net cash reconciliation | Row and column re-adds | Recomputed: 297,150, 59,278 and 199,499 equal | Supported | High | Maturity and cash view | S7 page:50; S6 page:18 |
| Trailing adjusted funds flow | CP-1 C9 | Four continuing-basis quarters | Sum of Q3 2025, Q4 2025, Q1 2026, Q2 2026 | Recomputed: 674,704 and 0.135x equal | Supported as cross-check | Medium | Cross-check only | S3 page:4; S5 page:3; S6 page:18 |
| Share count roll and returns | CP-1A K1, K2 | Opening shares, vesting, cancellations; repurchase consideration, dividends, free cash flow | Roll-forward; sum and difference | Recomputed: 708,888; 342.85; 213.10 equal | Supported | High | Distribution capacity | S6 page:10, page:11; S7 page:3, page:47 |
| Non-debt claims and tax assertion | CP-2 C1, C2, C3 | Asset retirement, leases, cash, notes; CRA amounts; liquidity | Sums and ratios | Recomputed: 606,756; 0.8423; 6.66; 493.1; 16.09; 7.91 equal | Supported | High | Total claims view | S6 page:1, page:8, page:10, page:14 |
| Confidence Score | This handoff | 15 material claims, 17 of 17 registers, partial source gate, 5 MINOR | Script formula | 44, band Low | Script output | High | QA envelope | confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 FY2025 net loss row | Cites S6 page:7 for the Eagle Ford loss; that page describes the Viking impairment, and the loss and tax adjustment are on S3 page:6 | Imprecise locator | A reader checking the cited page does not find the Eagle Ford loss | Cite S3 page:6 for the loss | CP-1 financials table |
| MINOR | CP-1A transaction summary and operating table | Cites S3 page:6 quotes for "no impact to cash flow", which is on S3 page:1; the officer row quote omits the name, which is in the same chunk | Imprecise locator | Slower verification; no misquotation | Cite S3 page:1 and quote the name line | CP-1A transaction summary; company profile |
| MINOR | CP-0 G7, CP-1 chart rows and H1, CP-2 gap K2 | State that the December 31, 2025 covenant table sits in the audited statements; no pinned source says where it sits | Unverified location assumption | The remediation target could be wrong | Say "not in the set" and name the annual report as the likely location | CP-0, CP-1, CP-2 gaps |
| MINOR | CP-0 K1 and CP-1 H6 | Say the two year-to-date adjusted funds flow figures are "not reconciled"; the Q2 2026 release (S7 page:4) prints the split | Superseded note | A reader of the earlier handoffs sees an open conflict that is resolved | CP-1A and CP-2 correct it; carry the correction into delivery | CP-0, CP-1 |
| MINOR | CP-1 chart tables for liquidity and maturities | Every monetary cell is "Not supplied: reported in thousands of Canadian dollars", as the selector rule requires for a non-US dollar issuer, although the figures exist in C$ | Presentation limitation | The liquidity and maturity charts in the report will have no plotted values | Show the C$ figures in the report table beneath, as the Basis cells do | CP-1 chart selectors |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves by cover text | A wrong document would change every figure | None found | None |
| Locator precision | Strong | 171 of 171 register quotations on the cited page; three imprecise locators in prose | Slower checks | None on conclusions | Exact page locators for the three prose cases |
| Calculation reproducibility | Strong | 30 of 30 derived figures and 42 of 42 tie-outs recomputed equal | Calculation errors would move leverage | None found | None |
| Cross-module consistency | Strong | CP-2 figures all found upstream or in its own calculations; one superseded note resolved downstream | Inconsistent figures mislead a committee | None found | Carry the correction to delivery |
| Management versus documentary separation | Adequate | Management Language rows are tagged and not adopted in CP-1A and CP-2 | Outlook claims read as facts | Overstated protection | None |
| Reviewer independence | Weak | The same host wrote and checked all four handoffs | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |
| Evidence completeness | Adequate | Debt documents, ownership and sale agreement are absent but labelled | Protections cannot be tested | Caps committee status | Add the documents |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Debt agreements | Credit agreement with amendments and note indenture | Guarantors, security, distribution baskets and call terms cannot be tested | Credit view and risk table | Holds the view at Medium | SEDAR+ and EDGAR filings named in the Q2 2026 discussion |
| G2 | Ownership and sale terms | Annual information form; Eagle Ford sale agreement | Control, indemnities and retained liabilities are unknown | Governance rows, claims outside debt | Lowers confidence in governance conclusions | Annual report exhibit 99.1; sale agreement |
| G3 | Audited FY2025 statements | Annual report exhibits 99.2 and 99.3 | FY2025 covenant data, annual interest paid and tax provision are missing | FY2025 column | Limits trend view | Form 40-F exhibits |
| G4 | Recency | Any filing after August 5, 2026 and before the cutoff | Third quarter 2026 results and later events are not reflected | Whole run | Lowers currency of the view | EDGAR filings to 2026-11-05 |
| G5 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / bte-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed with one MINOR assumption finding and one superseded note | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, debt, liquidity, covenants, chart data | High | Six headings; accepted | Passed with two MINOR findings | All metrics recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, transaction, governance, corrections | High | Six headings; accepted | Passed with one MINOR locator finding | Corrects two upstream notes |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit view, findings, risks | High | Six headings; accepted | Passed | All figures traced |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | FY2025 net loss row | Supported | Locator for the Eagle Ford loss is on the wrong page | Cite S3 page:6 | None on conclusions |
| MINOR | CP-1A | Transaction summary, company profile | Supported | Two imprecise locators | Cite S3 page:1; quote the name line | None on conclusions |
| MINOR | CP-0, CP-1, CP-2 | Location of December 31, 2025 covenant data | Insufficient Information | Location asserted without a source | State only that it is not in the set | None on conclusions |
| None found | CP-1A, CP-2 | Management Language rows | Supported as management statements | Tagged correctly and not adopted | None | None |
| None found | CP-0, CP-1, CP-1A | 171 register quotations | Supported | All found on the cited page | None | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None found | CP-1 | Leverage, cover, liquidity, headroom recomputed equal | Bank EBITDA and net cash are company-defined; issuer reports no EBITDA; stated in CP-1 | None | None | None |
| None found | CP-1A | Share roll, returns and free cash flow difference recomputed equal | Free cash flow is a company non-GAAP measure | None | None | None |
| None found | CP-2 | Non-debt claims sum, tax sum and liquidity cover recomputed equal | Rounded display (16.1x, 84.2%) agrees with 16.09 and 0.8423 | None | None | None |
| MINOR | CP-0, CP-1 | Year-to-date adjusted funds flow on two perimeters | Consolidated 405,558 versus Canada 406,644 (C$ thousand) | Resolved by the split printed at S7 page:4 | Carry the correction to delivery | None on conclusions |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| None found | CP-1 | Credit facilities are secured; notes carry no significant financial maintenance covenants | Credit agreement; indenture | Statement notes only | Keep as summary-level; do not extend | Required before relying on terms |
| None found | CP-1, CP-2 | Guarantors, security, distribution baskets, call prices | Credit agreement; indenture | Not in the set; labelled as missing | None in this run | Required before any creditor-protection conclusion |
| None found | CP-1A | Gibson arrangement treated as a lease; Eagle Ford sale terms | Construction and Conveyance Agreement; sale agreement | Statement notes and release only | None in this run | Required for indemnities and retained liabilities |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None found | CP-1A, CP-2 | Management's "industry-leading balance sheet" | Peer data | Cannot be tested; tagged Management Language | Keep as management language | Low: not used as support |
| None found | CP-2 | No peer ranking, instrument recommendation or recovery conclusion | Not applicable to this module | Prohibition honoured | None | None |
| None found | CP-1A | Oil price and differential statements | Forward curve | Historical benchmark prices only | None | Low |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Year-to-date adjusted funds flow on two perimeters | CP-0 and CP-1 say not reconciled; CP-1A and CP-2 say resolved by the printed split | Carry the correction into delivery; earlier handoffs cannot be edited | A reader of CP-0 or CP-1 alone sees an open conflict |
| None found | CP-0, CP-1 | Role of Baytex Energy USA, Inc. | CP-1 corrects the CP-0 sentence; CP-1A and CP-2 follow CP-1 | None | None |
| None found | CP-1, CP-1A, CP-2 | Net cash, liquidity, covenant and claim figures | Same values in all three | None | None |
| None found | CP-1A | Guidance steps and Gibson timing | Sequential updates, not conflicts | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Duplication | The missing-document caveat is repeated in several modules | Present once in the report's gaps section | Reader fatigue only |
| None found | CP-2 | Materiality | The risk table ranks price exposure, distributions, non-debt claims, concentration and missing protections, consistent with the traced drivers | None | Supports the credit view |
| None found | All | Committee readiness | Facts are traced; protections are untested; self-review only | Independent review and added documents | Requires More Work |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Chart data: liquidity and debt maturities | Monetary cells carry "Not supplied: reported in thousands of Canadian dollars" for every row | Report assembler should use the Basis cells' C$ values, or show them in a table | Chart strip shows no plotted liquidity or maturity values |
| None found | CP-0, CP-1, CP-1A, CP-2 | Required headings, source and handoff hashes, Reader summary and view headings | None | None | None |
| None found | CP-1 | Chart data: leverage and interest cover | Numbers present for 2026 rows; Not supplied for FY2025 with reason | None | Charts plot Q3 2025, Q1 2026 and Q2 2026 |
| None found | CP-1A | Selector tables and prose section | One table each; prose only for the transaction summary | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I1 | MINOR | CP-1 | Imprecise locator | Eagle Ford loss cited to the wrong page | Cite S3 page:6 | None | Open |
| I2 | MINOR | CP-1A | Imprecise locator | Cash-flow statement and officer name locators | Cite S3 page:1; quote the name line | None | Open |
| I3 | MINOR | CP-0, CP-1, CP-2 | Unverified assumption | Location of December 31, 2025 covenant data asserted | Say not in the set | None | Open |
| I4 | MINOR | CP-0, CP-1 | Superseded note | Adjusted funds flow perimeter described as unreconciled | Carry the CP-1A correction | None | Open |
| I5 | MINOR | CP-1 | Presentation limitation | Liquidity and maturity chart cells carry no numbers | Use C$ values from the Basis cells | None | Open |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Each register quotation in CP-0, CP-1 and CP-1A searched, whitespace-normalised, on the source page it cites | 171 quotations parsed (CP-0 37, CP-1 78, CP-1A 56); all 171 found on the cited page |
| Q2 | Tie-outs | Balance-sheet subtotals and totals, cash roll-forwards, net cash and adjusted funds flow reconciliations, lease and asset retirement roll-forwards, contractual obligations rows and columns, income statement subtotals and interest note re-added from numbers typed from the source pages | 42 of 42 equal |
| Q3 | Metric recomputation | Derived figures in CP-1, CP-1A and CP-2 recomputed from source numbers and compared with the handoff text (liquidity at three dates, covenant tie-out, ratios, headroom, obligations, share roll, returns, non-debt claims, tax sum, liquidity cover) | 30 of 30 equal |
| Q4 | CP-2 figure trace | Every number in CP-2's findings matched to CP-1, CP-1A or CP-2's own calculations | All matched; eight values are CP-2's own (606,756; 0.8423; 84.2%; 6.66; 493.1; 16.09; 16.1; 7.91) and recompute equal |
| Q5 | Confidence Score | `confidence_score.py --lineage "Directly Sourced:7,Calculated:3,Analyst Inference:3,Insufficient Information:2" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:5` | score = clamp((0.6 × 72.67 + 0.4 × 100) × 0.7 − 15) = 43.52, rounded to 44; band Low; qa_status Passed |

## Gaps

- G1 Critical for the creditor-protection decision: the credit agreement, note indenture, ownership record and sale agreement are not in the pack. Every module labels this; none asserts the missing terms.
- G2: the audited FY2025 statements and annual information form are not in the pack.
- G3: nothing after the Q2 2026 documents is supplied; the as-of date is November 5, 2026.
- G4: no independent review; the same host wrote and checked all four handoffs, which is the main limit on this check and caps committee status.
- G5: the five MINOR issues I1 to I5 above; none changes a conclusion.

## Next module

- Report delivery: carry qa_status Passed, Confidence Score 44 (Low), committee status Requires More Work, and gap G1. Apply the corrections in I3 and I4 when assembling the report, and plot the liquidity and maturity charts from the C$ values in the Basis cells (I5).
- Independent review: another agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Sourcing: add the debt agreements, annual report exhibits, sale agreement and any filing after August 5, 2026, then rerun CP-1A, CP-2 and CP-5 in a new run folder.
